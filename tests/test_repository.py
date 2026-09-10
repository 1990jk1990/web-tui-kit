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
        self.tokens = (ROOT / "src/tokens.css").read_text(encoding="utf-8")
        self.css = (ROOT / "src/tui.css").read_text(encoding="utf-8")
        self.javascript = (ROOT / "src/tui.js").read_text(encoding="utf-8")

    def test_demo_local_assets_exist(self):
        parser = AssetParser()
        parser.feed(self.demo)
        self.assertTrue(parser.assets)
        for asset in parser.assets:
            if "://" in asset:
                continue
            path = (ROOT / "demo" / asset).resolve()
            self.assertTrue(path.exists(), f"demo asset does not exist: {asset}")

    def test_core_design_tokens_are_declared(self):
        for token in (
            "--tui-desktop-bg",
            "--tui-surface",
            "--tui-text",
            "--tui-title",
            "--tui-selection-bg",
            "--tui-selection-text",
            "--tui-border-light",
            "--tui-border-dark",
            "--tui-font",
            "--tui-control-min-height",
        ):
            self.assertIn(token, self.tokens)

    def test_core_component_selectors_are_implemented(self):
        for selector in (
            ".tui-window",
            ".tui-panel",
            ".tui-button",
            ".tui-check",
            ".tui-radio",
            ".tui-input",
            ".tui-select",
            ".tui-menu",
            ".tui-table",
            ".tui-statusbar",
        ):
            self.assertIn(selector, self.css)

    def test_escape_event_contract_is_present(self):
        self.assertIn('event.key !== "Escape"', self.javascript)
        self.assertIn('new CustomEvent("tui:escape"', self.javascript)

    def test_demo_includes_mobile_viewport_and_native_controls(self):
        self.assertIn('name="viewport"', self.demo)
        self.assertIn('type="checkbox"', self.demo)
        self.assertIn('type="radio"', self.demo)
        self.assertIn('<button', self.demo)

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
