from pathlib import Path
import json
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK_DIR = ROOT / "tests" / "framework"


class FrameworkExecutionContractTests(unittest.TestCase):
    def setUp(self):
        self.package = json.loads((FRAMEWORK_DIR / "package.json").read_text(encoding="utf-8"))
        self.builder = (FRAMEWORK_DIR / "build-fixtures.mjs").read_text(encoding="utf-8")
        self.runner = (ROOT / "scripts" / "framework_recipe_regression.py").read_text(encoding="utf-8")
        self.workflow = (ROOT / ".github" / "workflows" / "framework-recipe-regression.yml").read_text(encoding="utf-8")
        self.release_workflow = (ROOT / ".github" / "workflows" / "release.yml").read_text(encoding="utf-8")

    def test_framework_toolchain_is_private_and_direct_versions_are_exact(self):
        self.assertTrue(self.package["private"])
        self.assertEqual(self.package["type"], "module")
        expected = {"@vue/compiler-sfc", "esbuild", "react", "react-dom", "vue"}
        self.assertEqual(set(self.package["devDependencies"]), expected)
        for dependency, version in self.package["devDependencies"].items():
            self.assertRegex(version, r"^\d+\.\d+\.\d+$", dependency)
            self.assertNotRegex(version, r"[~^*xX><=| ]", dependency)

    def test_builder_compiles_canonical_recipe_sources(self):
        for path in (
            "examples/react/PackageConfiguration.jsx",
            "examples/vue/PackageConfiguration.vue",
            "/src/tokens.css",
            "/src/tui.css",
            "/src/tui.js",
        ):
            self.assertIn(path, self.builder)
        self.assertIn("compileScript", self.builder)
        self.assertIn("bundle: true", self.builder)
        self.assertIn('path.join(root, "test-results", "framework")', self.builder)

    def test_browser_runner_exercises_consumer_contracts(self):
        for fragment in (
            "react.html",
            "vue.html",
            "examples/server-rendered/package-configuration.html",
            'get_by_role("checkbox", name="apache2.service")',
            'page.keyboard.press("ArrowDown")',
            'page.keyboard.press("Escape")',
            'page.get_by_role("button", name="Ok").click()',
            "new FormData(form).getAll('services')",
        ):
            self.assertIn(fragment, self.runner)

    def test_framework_verification_workflow_is_read_only_and_pinned_at_direct_dependencies(self):
        for fragment in (
            "permissions:\n  contents: read",
            "actions/setup-node@v4",
            'node-version: "24"',
            "npm install --prefix tests/framework --no-package-lock --no-audit --no-fund",
            "python -m playwright install --with-deps chromium",
            "python scripts/framework_recipe_regression.py",
        ):
            self.assertIn(fragment, self.workflow)

    def test_release_runs_framework_verification_before_build_and_publication(self):
        verification = "python scripts/framework_recipe_regression.py"
        build = "python scripts/build_release.py"
        publication = 'gh release create "${GITHUB_REF_NAME}"'
        self.assertIn("actions/setup-node@v4", self.release_workflow)
        self.assertIn("npm install --prefix tests/framework --no-package-lock --no-audit --no-fund", self.release_workflow)
        self.assertIn(verification, self.release_workflow)
        self.assertLess(self.release_workflow.index(verification), self.release_workflow.index(build))
        self.assertLess(self.release_workflow.index(verification), self.release_workflow.index(publication))

    def test_framework_dependencies_do_not_enter_canonical_runtime(self):
        combined = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT / "src").iterdir() if path.is_file())
        self.assertIsNone(re.search(r"\b(?:react|react-dom|vue|esbuild|compiler-sfc)\b", combined, re.IGNORECASE))


if __name__ == "__main__":
    unittest.main()
