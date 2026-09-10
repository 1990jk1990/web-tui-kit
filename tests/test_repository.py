from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AssetParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "link" and attributes.get("href"):
            self.assets.append(attributes["href"])
        if tag == "script" and attributes.get("src"):
            self.assets.append(attributes["src"])


class RepositoryContractTests(unittest.TestCase):
    def setUp(self):
        self.demo = (ROOT / "demo/index.html").read_text(encoding="utf-8")
        self.gallery = (ROOT / "demo/components.html").read_text(encoding="utf-8")
        self.dialogs = (ROOT / "demo/dialogs.html").read_text(encoding="utf-8")
        self.tokens = (ROOT / "src/tokens.css").read_text(encoding="utf-8")
        self.css = (ROOT / "src/tui.css").read_text(encoding="utf-8")
        self.javascript = (ROOT / "src/tui.js").read_text(encoding="utf-8")

    def assert_local_assets_exist(self, html, base_dir):
        parser = AssetParser()
        parser.feed(html)
        self.assertTrue(parser.assets)
        for asset in parser.assets:
            if "://" in asset:
                continue
            path = (base_dir / asset).resolve()
            self.assertTrue(path.exists(), f"demo asset does not exist: {asset}")

    def test_demo_local_assets_exist(self):
        for html in (self.demo, self.gallery, self.dialogs):
            self.assert_local_assets_exist(html, ROOT / "demo")

    def test_core_design_tokens_are_declared(self):
        for token in (
            "--tui-desktop-bg",
            "--tui-surface",
            "--tui-text",
            "--tui-title",
            "--tui-selection-bg",
            "--tui-selection-text",
            "--tui-help",
            "--tui-border-light",
            "--tui-border-dark",
            "--tui-font",
            "--tui-control-min-height",
            "--tui-dialog-max",
            "--tui-list-row-min-height",
            "--tui-scrollbar-size",
            "--tui-progress-height",
        ):
            self.assertIn(token, self.tokens)

    def test_forced_colors_override_core_tokens_with_system_colors(self):
        self.assertIn("@media (forced-colors: active)", self.tokens)
        for system_color in ("Canvas", "CanvasText", "GrayText", "Highlight", "HighlightText", "LinkText"):
            self.assertIn(system_color, self.tokens)

    def test_core_component_selectors_are_implemented(self):
        for selector in (
            ".tui-screen",
            ".tui-window",
            ".tui-panel",
            ".tui-dialog",
            ".tui-dialog--compact",
            ".tui-dialog-title",
            ".tui-button",
            ".tui-hotkey",
            ".tui-check",
            ".tui-radio",
            ".tui-choice-list",
            ".tui-checklist",
            ".tui-radiolist",
            ".tui-check-row",
            ".tui-radio-row",
            ".tui-menu-row",
            ".tui-help",
            ".tui-input",
            ".tui-select",
            ".tui-menu",
            ".tui-gauge",
            ".tui-progress",
            ".tui-table",
            ".tui-statusbar",
        ):
            self.assertIn(selector, self.css)

    def test_escape_event_contract_is_present_for_windows_and_dialogs(self):
        self.assertIn('event.key === "Escape"', self.javascript)
        self.assertIn('.tui-window[data-tui-escape-close]', self.javascript)
        self.assertIn('.tui-dialog[data-tui-escape-close]', self.javascript)
        self.assertIn('new CustomEvent("tui:escape"', self.javascript)

    def test_optional_list_navigation_contract_is_present(self):
        self.assertIn('[data-tui-list]', self.javascript)
        self.assertIn('input[type="checkbox"]:not(:disabled)', self.javascript)
        self.assertIn('button:not(:disabled)', self.javascript)
        self.assertIn('[data-tui-list-item][tabindex]', self.javascript)
        self.assertNotIn('input:not(:disabled)', self.javascript)
        self.assertNotIn('input[type="radio"]', self.javascript)
        for key in ("ArrowUp", "ArrowDown", "Home", "End"):
            self.assertIn(f'"{key}"', self.javascript)
        self.assertIn("event.preventDefault()", self.javascript)
        self.assertIn("items[nextIndex].focus()", self.javascript)
        self.assertIn('element.closest("[inert]")', self.javascript)

    def test_canonical_demo_is_package_configuration_reference(self):
        self.assertIn('name="viewport"', self.demo)
        self.assertIn('class="tui-screen"', self.demo)
        self.assertIn('class="tui-dialog"', self.demo)
        self.assertIn('class="tui-dialog-title"', self.demo)
        self.assertIn('Package configuration', self.demo)
        self.assertIn('class="tui-checklist" data-tui-list', self.demo)
        self.assertIn('class="tui-check-row"', self.demo)
        self.assertIn('class="tui-help"', self.demo)
        self.assertIn('type="checkbox"', self.demo)
        self.assertIn('autofocus', self.demo)
        self.assertIn('<button', self.demo)

    def test_component_gallery_keeps_general_controls_visible(self):
        self.assertIn('type="checkbox"', self.gallery)
        self.assertIn('type="radio"', self.gallery)
        self.assertIn('class="tui-input"', self.gallery)
        self.assertIn('class="tui-select"', self.gallery)
        self.assertIn('class="tui-menu"', self.gallery)
        self.assertIn('class="tui-table"', self.gallery)
        self.assertIn('./dialogs.html', self.gallery)

    def test_dialog_gallery_covers_core_dialog_patterns(self):
        for title in (
            "Message box",
            "Confirmation",
            "Input box",
            "Menu",
            "Radiolist",
            "Checklist",
            "Gauge",
        ):
            self.assertIn(title, self.dialogs)

        for fragment in (
            'class="tui-dialog tui-dialog--compact"',
            'class="tui-choice-list" data-tui-list',
            'class="tui-radiolist" role="radiogroup"',
            'class="tui-radio-row"',
            'class="tui-checklist" data-tui-list',
            'class="tui-menu-row"',
            '<progress class="tui-progress"',
        ):
            self.assertIn(fragment, self.dialogs)

        self.assertNotIn('class="tui-radiolist" data-tui-list', self.dialogs)
        self.assertGreaterEqual(self.dialogs.count(" disabled"), 2)
        self.assertIn("Native radio arrow-key behavior is preserved.", self.dialogs)

    def test_disabled_choice_states_are_styled(self):
        self.assertIn(".tui-check-row:has(input:disabled)", self.css)
        self.assertIn(".tui-radio-row:has(input:disabled)", self.css)
        self.assertIn(".tui-menu-row:disabled", self.css)
        self.assertIn("cursor: not-allowed", self.css)

    def test_core_css_avoids_forbidden_visual_effects_and_motion(self):
        css = self.css.lower()
        for fragment in (
            "linear-gradient(",
            "radial-gradient(",
            "backdrop-filter:",
            "filter: blur(",
            "scroll-behavior: smooth",
            "transition:",
            "animation:",
        ):
            self.assertNotIn(fragment, css)


if __name__ == "__main__":
    unittest.main()
