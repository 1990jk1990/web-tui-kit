# Framework and template integration recipes

These examples show how consuming applications can assemble the canonical `web-tui-kit` browser contract from common application stacks.

They are **not** a second implementation of the design system and they are not published framework adapter packages. Exact visuals and behavior remain owned by `src/`, OpenSpec, and the canonical demos. The intentionally supported downstream names and semantic relationships are inventoried in `docs/project/public-contract.md`.

## Stable consumption

For reproducible downstream use, vendor files from immutable stable release tag `v1.0.1` rather than the moving `main` branch. A consuming project normally copies:

```text
src/tokens.css
src/tui.css
src/tui.js   # optional unless progressive JS enhancements are needed
```

Load `tokens.css` before `tui.css`. Load `tui.js` once when using `data-tui-escape-close` or `data-tui-list` progressive enhancement.

Starting with 1.0, normal Semantic Versioning applies to the browser-native contract these recipes emit. The recipes remain guidance rather than separately versioned adapter APIs.

## Recipes

- `react/PackageConfiguration.jsx` demonstrates controlled React form state while retaining native checkbox semantics and application-owned `tui:escape` handling.
- `vue/PackageConfiguration.vue` demonstrates the same contract in a Vue Single File Component.
- `server-rendered/package-configuration.html` is browser-openable and shows the shape a server-side template loop can emit while preserving ordinary form submission semantics.

## Executable verification

Repository CI compiles the canonical React and Vue files above with exact representative direct development versions and renders them in pinned Linux Chromium with canonical `src/` assets. The same smoke run exercises the server-rendered example. This protects the checked-in recipes from silently becoming stale while keeping all framework/compiler/bundler dependencies under test tooling rather than in `src/`.

The pinned verification versions are evidence anchors, not a support matrix for every React/Vue/tooling release. See `docs/project/framework-integration.md`, `docs/project/testing.md`, and `docs/project/compatibility.md` for exact versions, local commands, and evidence limits.

## Integration rules

Do not copy CSS declarations out of `src/tui.css` into framework components. Reuse the canonical public classes. Do not recreate tokens in JavaScript or framework theme objects when the public CSS custom properties can be consumed directly.

Native form controls remain the semantic source of truth. Framework state may control their values, but should not replace them with non-semantic clickable containers.

`tui:escape` is an application signal, not an automatic close command. The consuming app decides whether Escape hides a dialog, routes elsewhere, cancels a workflow, or does nothing.

`data-tui-list` is optional progressive focus navigation. Frameworks should not add a second ArrowUp/ArrowDown/Home/End handler on the same list unless they intentionally replace that contract.

See `docs/project/framework-integration.md` for detailed guidance and `docs/project/public-contract.md` for the supported stability boundary.
