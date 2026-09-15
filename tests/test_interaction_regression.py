from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class InteractionRegressionContractTests(unittest.TestCase):
    def setUp(self):
        self.fixture = (ROOT / "tests/browser/interaction.html").read_text(encoding="utf-8")
        self.runner = (ROOT / "scripts/interaction_regression.py").read_text(encoding="utf-8")
        self.workflow = (ROOT / ".github/workflows/interaction-regression.yml").read_text(encoding="utf-8")
        self.requirements = (ROOT / "requirements-visual.txt").read_text(encoding="utf-8")

    def test_fixture_consumes_canonical_runtime_assets(self):
        self.assertIn('href="../../src/tokens.css"', self.fixture)
        self.assertIn('href="../../src/tui.css"', self.fixture)
        self.assertIn('src="../../src/tui.js"', self.fixture)
        self.assertNotIn("<style", self.fixture)
        self.assertEqual(self.fixture.count("<script"), 1)

    def test_fixture_covers_interaction_contracts(self):
        for fragment in (
            'id="escape-surface"',
            "data-tui-escape-close",
            'id="navigation-list"',
            "data-tui-list",
            'id="nav-check-disabled"',
            " disabled",
            " inert",
            " hidden",
            'aria-disabled="true"',
            'id="nav-custom" data-tui-list-item tabindex="0"',
            'id="radio-first"',
            'id="radio-second"',
            'id="text-input"',
            'id="touch-row"',
            'id="touch-checkbox"',
            '<dialog\n      id="native-dialog-surface"',
            'id="native-dialog-title"',
        ):
            self.assertIn(fragment, self.fixture)

    def test_runner_covers_chromium_firefox_and_touch(self):
        self.assertIn("InteractionCase(\"chromium-desktop\", \"chromium\"", self.runner)
        self.assertIn("InteractionCase(\"chromium-touch\", \"chromium\", 390, 844, True)", self.runner)
        self.assertIn("InteractionCase(\"firefox-desktop\", \"firefox\"", self.runner)
        self.assertIn('choices=("all", "chromium", "firefox")', self.runner)
        self.assertIn("is_mobile=case.mobile", self.runner)
        self.assertIn("has_touch=case.mobile", self.runner)
        self.assertIn('window.matchMedia("(pointer: coarse)").matches', self.runner)
        self.assertIn('touch_row = page.locator("#touch-row")', self.runner)
        self.assertIn("touch_row.tap()", self.runner)

    def test_runner_asserts_keyboard_contracts(self):
        for fragment in (
            'page.keyboard.press("Escape")',
            'page.keyboard.press("ArrowDown")',
            'page.keyboard.press("ArrowUp")',
            'page.keyboard.press("Home")',
            'page.keyboard.press("End")',
            '"nav-button"',
            '"nav-link"',
            '"nav-custom"',
            '"radio-second"',
            "selection == [1, 1, \"text-input\"]",
            "focus navigation unexpectedly toggled checkbox state",
        ):
            self.assertIn(fragment, self.runner)

    def test_runner_asserts_native_dialog_title_overflow_contract(self):
        for fragment in (
            "verify_native_dialog_title_overflow",
            'document.querySelector("#native-dialog-surface")',
            'document.querySelector("#native-dialog-title")',
            "getComputedStyle(dialog).overflow",
            'geometry["overflow"] == "visible"',
            'geometry["titleTop"] < geometry["dialogTop"]',
        ):
            self.assertIn(fragment, self.runner)

    def test_workflow_runs_engine_matrix_read_only(self):
        self.assertIn("permissions:\n  contents: read", self.workflow)
        self.assertIn("engine: [chromium, firefox]", self.workflow)
        self.assertIn("fail-fast: false", self.workflow)
        self.assertIn("pip install -r requirements-visual.txt", self.workflow)
        self.assertIn('python -m playwright install --with-deps "${{ matrix.engine }}"', self.workflow)
        self.assertIn('python scripts/interaction_regression.py --engine "${{ matrix.engine }}"', self.workflow)
        self.assertIn("if: failure()", self.workflow)
        self.assertIn("interaction-regression-${{ matrix.engine }}-failures", self.workflow)

    def test_interaction_suite_reuses_pinned_playwright(self):
        self.assertIn("playwright==1.62.0", self.requirements)


if __name__ == "__main__":
    unittest.main()