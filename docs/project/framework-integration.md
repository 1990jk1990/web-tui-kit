# Framework integration

## Principle

`web-tui-kit` remains browser-native. Frameworks consume the documented HTML/class/event contract; they do not become part of the design-system runtime.

The canonical implementation is still:

```text
src/tokens.css
src/tui.css
src/tui.js
```

The supported downstream names and semantic relationships are inventoried in `docs/project/public-contract.md` and specified in `openspec/specs/public-contract/spec.md`. Framework code should depend on that declared surface rather than incidental demo IDs, test fixture details, or repository verification implementation.

React, Vue, server-rendered templates, or another application architecture may generate the semantic markup, own application state, and decide navigation/lifecycle behavior around that runtime.

## Pin a release first

For reproducible applications and coding-agent work, copy/vendor from immutable tag `v0.9.0` rather than `main`. This prevents later design-system development from silently changing an existing consumer.

When upgrading to a newer tag, review `CHANGELOG.md`, `docs/project/public-contract.md`, accepted OpenSpec, and relevant demos before updating vendored assets. Before 1.0, an intentional public-contract break uses a MINOR version and explicit migration guidance; after 1.0, normal Semantic Versioning rules apply to the declared public surface.

## Asset loading

Load `tokens.css` before `tui.css`. `tui.js` is optional unless the application wants the library's progressive Escape dispatch or `data-tui-list` focus navigation.

Framework build systems may import or copy these files in their normal asset pipeline. That pipeline is application-owned; `web-tui-kit` does not require one.

## Semantic controls and state

Use native buttons, inputs, selects, textareas, forms, links, and progress elements where the canonical patterns call for them. A framework may control the value/checked state of those elements, but should keep the native element in the rendered output.

Do not replace checkboxes or radio buttons with generic clickable `<div>` elements merely to fit framework state management. The design system deliberately styles native controls and depends on their browser semantics. Required child/sibling relationships for marker patterns such as `.tui-check-row` + native input + `.tui-mark` are part of the documented public component contract.

## `tui:escape`

When `src/tui.js` is loaded, a `.tui-window` or `.tui-dialog` marked with `data-tui-escape-close` dispatches a bubbling `tui:escape` custom event when Escape is pressed. The event carries the originating keyboard event as `detail.sourceEvent`.

The consuming application owns the consequence. React/Vue components should attach/remove an event listener for their mounted surface and invoke the application's cancel/close/navigation action. The library does not hide the DOM node itself.

## `data-tui-list`

A container marked with `data-tui-list` receives the optional ArrowUp/ArrowDown/Home/End focus-navigation enhancement from `src/tui.js`.

Do not add competing framework key handlers to the same list unless the application intentionally replaces the library contract. Native radio groups and text-entry controls remain excluded from the enhancement so their browser behavior is preserved. Custom focusable items may opt in with public `data-tui-list-item` plus a non-negative `tabindex`.

## Styling boundaries

Framework components should use canonical public classes such as `.tui-dialog`, `.tui-checklist`, `.tui-check-row`, `.tui-button`, and `.tui-actions` rather than copying declarations from `src/tui.css` into CSS-in-JS, scoped component styles, or a framework theme object.

Application-specific layout around the design system is allowed. Changes intended to become reusable visual behavior belong back in `web-tui-kit`, not in a private framework wrapper.

All canonical `--tui-*` custom properties are public theming hooks by name and semantic purpose. Consumers should override tokens rather than reaching into declaration order or private selector implementation.

## Recipes

- `examples/react/PackageConfiguration.jsx`
- `examples/vue/PackageConfiguration.vue`
- `examples/server-rendered/package-configuration.html`

The React and Vue files are source recipes, not standalone runnable applications in this repository. They assume the consuming application already has the respective framework/toolchain. The server-rendered example is directly browser-openable when the repository is served statically.

These recipe files are supported integration guidance, but example component names, local variable names, fixture IDs, generated bundles, and test-harness APIs are not separately versioned public runtime APIs. The stable contract is the browser-native output they demonstrate.

## Executable recipe verification

The repository also compiles and browser-executes the canonical React and Vue source recipes with a private development-only harness under `tests/framework/`. The representative pinned direct versions are React `19.0.0`, React DOM `19.0.0`, Vue `3.5.13`, `@vue/compiler-sfc` `3.5.13`, and esbuild `0.24.2`. The harness renders with the canonical `src/` assets and verifies native checkbox state, `data-tui-list` focus movement, `tui:escape` delivery to application handlers, and accept payloads. The server-rendered recipe is smoke-tested in the same Chromium run for ordinary form state and Escape handling.

These versions are evidence anchors, not the supported-version range of `web-tui-kit`. Passing them shows that the checked-in recipes compile and interoperate with representative current framework tooling; it does not establish compatibility with every React/Vue release. The Node/npm/compiler/bundler dependencies are repository verification tooling only and are not required by consumers or included in `src/`.

Run the verification locally with:

```bash
npm install --prefix tests/framework --no-package-lock --no-audit --no-fund
pip install -r requirements-visual.txt
python -m playwright install --with-deps chromium
python scripts/framework_recipe_regression.py
```

## Why there is no adapter package

The current browser-native contract already maps cleanly to React, Vue, and server-rendered markup. A maintained adapter layer would create additional API/versioning/framework-maintenance surfaces without solving a demonstrated capability gap.

Executable recipe verification strengthens this strategy without changing it: the project tests the recipes as consumers of the browser-native contract rather than promoting them into a second runtime surface.

If a future consumer identifies behavior that cannot be expressed cleanly through semantic markup, canonical classes, CSS custom properties, and the existing custom-event/progressive-enhancement contracts, that concrete gap can justify a new adapter proposal. Until then, recipes are the lower-risk integration mechanism.
