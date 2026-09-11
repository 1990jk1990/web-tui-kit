from pathlib import Path
import hashlib
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


class ReleaseContractTests(unittest.TestCase):
    def setUp(self):
        self.version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.builder = (ROOT / "scripts/build_release.py").read_text(encoding="utf-8")
        self.workflow = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")

    def test_version_is_plain_semver(self):
        self.assertRegex(self.version, VERSION_RE)

    def test_release_builder_creates_valid_deterministic_archive(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory)
            subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts/build_release.py"),
                    "--output-dir",
                    str(output_dir),
                    "--version",
                    f"v{self.version}",
                    "--check",
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )

            archive_path = output_dir / f"web-tui-kit-{self.version}.zip"
            checksum_path = output_dir / f"web-tui-kit-{self.version}.zip.sha256"
            self.assertTrue(archive_path.is_file())
            self.assertTrue(checksum_path.is_file())

            expected_digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
            checksum = checksum_path.read_text(encoding="utf-8").strip()
            self.assertEqual(checksum, f"{expected_digest}  {archive_path.name}")

            package_root = f"web-tui-kit-{self.version}"
            expected_members = {
                f"{package_root}/{path}"
                for path in (
                    "VERSION",
                    "README.md",
                    "DESIGN_SYSTEM.md",
                    "AGENTS.md",
                    "CHANGELOG.md",
                    "SECURITY.md",
                    "docs/project/framework-integration.md",
                    "src/tokens.css",
                    "src/tui.css",
                    "src/tui.js",
                    "demo/index.html",
                    "demo/dialogs.html",
                    "demo/components.html",
                    "examples/README.md",
                    "examples/react/PackageConfiguration.jsx",
                    "examples/vue/PackageConfiguration.vue",
                    "examples/server-rendered/package-configuration.html",
                )
            }

            with zipfile.ZipFile(archive_path, "r") as archive:
                self.assertEqual(set(archive.namelist()), expected_members)
                self.assertEqual(
                    archive.read(f"{package_root}/VERSION").decode("utf-8").strip(),
                    self.version,
                )
                for info in archive.infolist():
                    self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0))

    def test_release_builder_rejects_tag_version_mismatch(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            result = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts/build_release.py"),
                    "--output-dir",
                    temporary_directory,
                    "--version",
                    "v999.999.999",
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("tag/version mismatch", result.stderr)

    def test_release_workflow_verifies_before_publication(self):
        for fragment in (
            '"v*.*.*"',
            "permissions:\n  contents: write",
            "actions/setup-node@v4",
            'node-version: "24"',
            'test "${GITHUB_REF_NAME}" = "v$(cat VERSION)"',
            'git merge-base --is-ancestor "${GITHUB_SHA}" origin/main',
            "python -m unittest discover -s tests -v",
            "python scripts/validate_ai_doc_1.py",
            "mkdocs build --strict",
            "python -m playwright install --with-deps chromium firefox",
            "python scripts/visual_regression.py",
            "python scripts/interaction_regression.py",
            "python scripts/accessibility_regression.py",
            "npm install --prefix tests/framework --no-package-lock --no-audit --no-fund",
            "python scripts/framework_recipe_regression.py",
            'python scripts/build_release.py --version "${GITHUB_REF_NAME}" --check',
            'gh release create "${GITHUB_REF_NAME}"',
            "--verify-tag",
            "--prerelease",
        ):
            self.assertIn(fragment, self.workflow)

        publication = self.workflow.index('gh release create "${GITHUB_REF_NAME}"')
        build = self.workflow.index("python scripts/build_release.py")
        for verification in (
            'test "${GITHUB_REF_NAME}" = "v$(cat VERSION)"',
            'git merge-base --is-ancestor "${GITHUB_SHA}" origin/main',
            "python -m unittest discover -s tests -v",
            "python scripts/visual_regression.py",
            "python scripts/interaction_regression.py",
            "python scripts/accessibility_regression.py",
            "python scripts/framework_recipe_regression.py",
        ):
            self.assertLess(self.workflow.index(verification), build)
            self.assertLess(self.workflow.index(verification), publication)
        self.assertLess(build, publication)

    def test_release_archive_inputs_are_explicit(self):
        self.assertIn("DISTRIBUTION_FILES = (", self.builder)
        self.assertIn("FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)", self.builder)
        self.assertIn("sorted(DISTRIBUTION_FILES)", self.builder)
        self.assertIn("sha256", self.builder)
        self.assertIn("display_path", self.builder)
        self.assertIn('"examples/react/PackageConfiguration.jsx"', self.builder)
        self.assertIn('"examples/vue/PackageConfiguration.vue"', self.builder)
        self.assertIn('"examples/server-rendered/package-configuration.html"', self.builder)
        self.assertNotIn("site/", self.builder)
        self.assertNotIn("test-results/", self.builder)
        self.assertNotIn("tests/framework/node_modules/", self.builder)


if __name__ == "__main__":
    unittest.main()
