from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class AccessibilityRegressionContractTests(unittest.TestCase):
    def setUp(self):
        self.runner = (ROOT / "scripts/accessibility_regression.py").read_text(encoding="utf-8")
        self.workflow = (ROOT / ".github/workflows/accessibility-regression.yml").read_text(encoding="utf-8")
        self.release_workflow = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
        self.requirements = (ROOT / "requirements-visual.txt").read_text(encoding="utf-8")
        self.package_demo = (ROOT / "demo/index.html").read_text(encoding="utf-8")
        self.dialog_demo = (ROOT / "demo/dialogs.html").read_text(encoding="utf-8")

    def test_runner_uses_canonical_demos_and_cross_browser_cases(self):
        for fragment in (
            '"/demo/index.html"',
            '"/demo/dialogs.html"',
            'AccessibilityCase("chromium-package", "chromium"',
            'AccessibilityCase("chromium-dialogs", "chromium"',
            'AccessibilityCase("chromium-package-touch", "chromium", "/demo/index.html", "package-touch", 390, 844, True)',
            'AccessibilityCase("firefox-package", "firefox"',
            'AccessibilityCase("firefox-dialogs", "firefox"',
            'choices=("all", "chromium", "firefox")',
            "is_mobile=case.mobile",
            "has_touch=case.mobile",
        ):
            self.assertIn(fragment, self.runner)

    def test_runner_asserts_browser_exposed_semantics(self):
        for fragment in (
            'get_by_role("region", name="Package configuration", exact=True)',
            'get_by_role("group", name="Services to restart", exact=True)',
            'get_by_role("checkbox", name="accounts-daemon.service", exact=True)',
            'get_by_role("textbox", name="Hostname", exact=True)',
            'get_by_role("group", name="Available actions", exact=True)',
            'get_by_role("radiogroup", name="Startup mode", exact=True)',
            'get_by_role("radio", name="Performance mode", exact=True)',
            'get_by_role("progressbar", name="Installing packages", exact=True)',
            'page.get_by_role("dialog").count() == 0',
            '"PROGRESS"',
            '"value": 65',
            '"max": 100',
        ):
            self.assertIn(fragment, self.runner)

    def test_presentation_helpers_are_hidden_from_accessible_names(self):
        for demo in (self.package_demo, self.dialog_demo):
            helpers = re.findall(r'<span class="tui-help"[^>]*>', demo)
            self.assertGreater(len(helpers), 0)
            for helper in helpers:
                self.assertIn('aria-hidden="true"', helper)

    def test_workflow_runs_read_only_engine_matrix(self):
        self.assertIn("permissions:\n  contents: read", self.workflow)
        self.assertIn("engine: [chromium, firefox]", self.workflow)
        self.assertIn("fail-fast: false", self.workflow)
        self.assertIn("pip install -r requirements-visual.txt", self.workflow)
        self.assertIn('python -m playwright install --with-deps "${{ matrix.engine }}"', self.workflow)
        self.assertIn('python scripts/accessibility_regression.py --engine "${{ matrix.engine }}"', self.workflow)
        self.assertIn("if: failure()", self.workflow)
        self.assertIn("accessibility-regression-${{ matrix.engine }}-failures", self.workflow)

    def test_accessibility_suite_reuses_pinned_playwright(self):
        self.assertIn("playwright==1.62.0", self.requirements)

    def test_future_release_runs_accessibility_gate_before_build(self):
        accessibility = self.release_workflow.index("python scripts/accessibility_regression.py")
        build = self.release_workflow.index("python scripts/build_release.py")
        publish = self.release_workflow.index('gh release create "${GITHUB_REF_NAME}"')
        self.assertLess(accessibility, build)
        self.assertLess(accessibility, publish)


if __name__ == "__main__":
    unittest.main()
