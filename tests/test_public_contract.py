from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]

PUBLIC_TOKENS = {
    "--tui-desktop-bg",
    "--tui-surface",
    "--tui-surface-light",
    "--tui-text",
    "--tui-muted",
    "--tui-title",
    "--tui-selection-bg",
    "--tui-selection-text",
    "--tui-help",
    "--tui-border-light",
    "--tui-border-mid",
    "--tui-border-dark",
    "--tui-shadow",
    "--tui-focus",
    "--tui-danger",
    "--tui-success",
    "--tui-font",
    "--tui-font-size",
    "--tui-line-height",
    "--tui-space-1",
    "--tui-space-2",
    "--tui-space-3",
    "--tui-space-4",
    "--tui-space-5",
    "--tui-space-6",
    "--tui-border-width",
    "--tui-shadow-offset",
    "--tui-window-max",
    "--tui-dialog-max",
    "--tui-control-min-height",
    "--tui-list-row-min-height",
    "--tui-scrollbar-size",
    "--tui-progress-height",
}

PUBLIC_CLASSES = {
    "tui-desktop",
    "tui-screen",
    "tui-window",
    "tui-panel",
    "tui-dialog",
    "tui-dialog--compact",
    "tui-dialog-title",
    "tui-dialog-copy",
    "tui-section",
    "tui-title",
    "tui-heading",
    "tui-muted",
    "tui-stack",
    "tui-grid",
    "tui-field",
    "tui-input",
    "tui-select",
    "tui-textarea",
    "tui-button",
    "tui-hotkey",
    "tui-help",
    "tui-actions",
    "tui-check",
    "tui-radio",
    "tui-choice-list",
    "tui-checklist",
    "tui-radiolist",
    "tui-check-row",
    "tui-radio-row",
    "tui-mark",
    "tui-menu-row",
    "tui-menu",
    "tui-menu-item",
    "tui-gauge",
    "tui-progress",
    "tui-gauge-value",
    "tui-table-wrap",
    "tui-table",
    "tui-statusbar",
    "tui-kbd",
    "tui-success",
    "tui-danger",
}

PUBLIC_STATE_CLASSES = {"is-active", "is-selected"}
PUBLIC_DATA_ATTRIBUTES = {
    "data-tui-escape-close",
    "data-tui-list",
    "data-tui-list-item",
}


class PublicContractTests(unittest.TestCase):
    def setUp(self):
        self.tokens_css = (ROOT / "src/tokens.css").read_text(encoding="utf-8")
        self.tui_css = (ROOT / "src/tui.css").read_text(encoding="utf-8")
        self.tui_js = (ROOT / "src/tui.js").read_text(encoding="utf-8")
        self.contract_doc = (ROOT / "docs/project/public-contract.md").read_text(encoding="utf-8")
        self.contract_spec = (ROOT / "openspec/specs/public-contract/spec.md").read_text(encoding="utf-8")

    def test_all_tui_tokens_are_declared_and_classified(self):
        implemented = set(re.findall(r"(--tui-[a-z0-9-]+)\s*:", self.tokens_css))
        self.assertEqual(implemented, PUBLIC_TOKENS)

        individually_documented = PUBLIC_TOKENS - {
            "--tui-space-2",
            "--tui-space-3",
            "--tui-space-4",
            "--tui-space-5",
        }
        for token in individually_documented:
            self.assertIn(f"`{token}`", self.contract_doc)
        self.assertIn("`--tui-space-1` through `--tui-space-6`", self.contract_doc)

    def test_all_tui_component_classes_are_implemented_and_classified(self):
        implemented = set(re.findall(r"\.((?:tui)[a-z0-9_-]*)", self.tui_css))
        self.assertEqual(implemented, PUBLIC_CLASSES)
        for class_name in PUBLIC_CLASSES:
            self.assertIn(f"`{class_name}`", self.contract_doc)

    def test_public_scoped_state_hooks_are_explicit(self):
        implemented_states = set(re.findall(r"\.((?:is)-(?:active|selected))", self.tui_css))
        self.assertEqual(implemented_states, PUBLIC_STATE_CLASSES)
        for state in PUBLIC_STATE_CLASSES:
            self.assertIn(f".{state}", self.contract_doc)

    def test_progressive_javascript_names_are_protected(self):
        for attribute in PUBLIC_DATA_ATTRIBUTES:
            self.assertIn(attribute, self.tui_js)
            self.assertIn(f"`{attribute}`", self.contract_doc)
            self.assertIn(f"`{attribute}`", self.contract_spec)
        self.assertIn('new CustomEvent("tui:escape"', self.tui_js)
        self.assertIn("bubbles: true", self.tui_js)
        self.assertIn("detail: { sourceEvent: event }", self.tui_js)
        self.assertIn("`tui:escape`", self.contract_doc)
        self.assertIn("`tui:escape`", self.contract_spec)

    def test_help_class_consumes_help_token(self):
        match = re.search(r"\.tui-help\s*\{(?P<body>[^}]*)\}", self.tui_css, re.DOTALL)
        self.assertIsNotNone(match)
        self.assertIn("color: var(--tui-help);", match.group("body"))
        self.assertIn("--tui-help: LinkText;", self.tokens_css)

    def test_semantic_contract_keeps_native_control_expectations(self):
        for fragment in (
            "`.tui-button` and `.tui-menu-row` are intended for native buttons",
            "`.tui-progress` is intended for a native `<progress>` element",
            "`.tui-dialog` remains presentation-only",
            "`.tui-check-row` / `.tui-radio-row` retain native checkbox/radio inputs",
        ):
            self.assertIn(fragment, self.contract_spec)

    def test_stability_policy_preserves_history_and_active_1_0_contract(self):
        for fragment in (
            "Pre-1.0 compatibility policy",
            "Post-1.0 compatibility and deprecation policy",
            "1.0 readiness is evidence-based",
        ):
            self.assertIn(fragment, self.contract_spec)
        self.assertIn("Starting with `1.0.0`", self.contract_doc)
        self.assertIn("## 1.0 stability evidence", self.contract_doc)
        self.assertIn("Physical Android certification", self.contract_doc)

    def test_public_contract_is_a_release_input(self):
        builder = (ROOT / "scripts/build_release.py").read_text(encoding="utf-8")
        release_tests = (ROOT / "tests/test_release.py").read_text(encoding="utf-8")
        for content in (builder, release_tests):
            self.assertIn('"docs/project/public-contract.md"', content)


if __name__ == "__main__":
    unittest.main()
