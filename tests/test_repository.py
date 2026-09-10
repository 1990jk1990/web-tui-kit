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
        self.assert_local_assets_exist(self.demo, ROOT / "demo")
        self.assert_local_assets_exist(self.gallery, ROOT / "demo")

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
        ):
            self.assertIn(token, self.tokens)

    def test_core_component_selectors_are_implemented(self):
        for selector in (
            ".tui-screen",
            ".tui-window",
            ".tui-panel",
            ".tui-dialog",
            ".tui-dialog-title",
            ".tui-button",
            ".tui-hotkey",
            ".tui-check",
            ".tui-radio",
            ".tui-checklist",
            ".tui-check-row",
            ".tui-help",
            ".tui-input",
            ".tui-select",
            ".tui-menu",
            ".tui-table",
            ".tui-statusbar",
        ):
            self.assertIn(selector, self.css)

    def test_escape_event_contract_is_present_for_windows_and_dialogs(self):
        self.assertIn('event.key !== "Escape"', self.javascript)
        self.assertIn('.tui-window[data-tui-escape-close]', self.javascript)
        self.assertIn('.tui-dialog[data-tui-escape-close]', self.javascript)
        self.assertIn('new CustomEvent("tui:escape"', self.javascript)

    def test_canonical_demo_is_package_configuration_reference(self):
        self.assertIn('name="viewport"', self.demo)
        self.assertIn('class="tui-screen"', self.demo)
        self.assertIn('class="tui-dialog"', self.demo)
        self.assertIn('class="tui-dialog-title"', self.demo)
        self.assertIn('Package configuration', self.demo)
        self.assertIn('class="tui-checklist"', self.demo)
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

    def test_default_css_avoids_forbidden_visual_effects(self):
        css = self.css.lower()
        for fragment in (
            "linear-gradient(",
            "radial-gradient(",
            "backdrop-filter:",
            "filter: blur(",
        ):
            self.assertNotIn(fragment, css)


if __name__ == "__main__":
    unittest.main()
