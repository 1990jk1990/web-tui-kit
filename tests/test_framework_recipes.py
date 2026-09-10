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


class FrameworkRecipeTests(unittest.TestCase):
    def setUp(self):
        self.react_path = ROOT / "examples/react/PackageConfiguration.jsx"
        self.vue_path = ROOT / "examples/vue/PackageConfiguration.vue"
        self.server_path = ROOT / "examples/server-rendered/package-configuration.html"
        self.react = self.react_path.read_text(encoding="utf-8")
        self.vue = self.vue_path.read_text(encoding="utf-8")
        self.server = self.server_path.read_text(encoding="utf-8")

    def test_framework_recipes_exist(self):
        for path in (self.react_path, self.vue_path, self.server_path):
            self.assertTrue(path.is_file(), f"missing integration recipe: {path}")
            self.assertGreater(path.stat().st_size, 500)

    def test_recipes_reuse_canonical_dialog_contract(self):
        for recipe in (self.react, self.vue, self.server):
            for fragment in (
                "tui-screen",
                "tui-dialog",
                "tui-dialog-title",
                "tui-checklist",
                "tui-check-row",
                "tui-mark",
                "tui-help",
                "tui-actions",
                "tui-button",
                "data-tui-list",
                "data-tui-escape-close",
                "tui:escape",
                "checkbox",
            ):
                self.assertIn(fragment, recipe)

    def test_recipes_do_not_embed_parallel_visual_styles(self):
        for recipe in (self.react, self.vue, self.server):
            lower = recipe.lower()
            self.assertNotIn("<style", lower)
            self.assertNotIn("--tui-desktop-bg", lower)
            self.assertNotIn("linear-gradient(", lower)
            self.assertNotIn("border-radius:", lower)
            self.assertNotIn("background-color:", lower)

    def test_server_rendered_recipe_loads_canonical_local_assets(self):
        parser = AssetParser()
        parser.feed(self.server)
        self.assertIn("../../src/tokens.css", parser.assets)
        self.assertIn("../../src/tui.css", parser.assets)
        self.assertIn("../../src/tui.js", parser.assets)

        for asset in parser.assets:
            path = (self.server_path.parent / asset).resolve()
            self.assertTrue(path.is_file(), f"server recipe asset does not exist: {asset}")

    def test_framework_names_do_not_enter_canonical_runtime(self):
        runtime = "\n".join(
            (ROOT / path).read_text(encoding="utf-8").lower()
            for path in ("src/tokens.css", "src/tui.css", "src/tui.js")
        )
        self.assertNotIn("react", runtime)
        self.assertNotIn("vue", runtime)


if __name__ == "__main__":
    unittest.main()
