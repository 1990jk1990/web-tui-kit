# Framework and template integration recipes

These examples show how consuming applications can assemble the canonical `web-tui-kit` browser contract from common application stacks.

They are **not** a second implementation of the design system and they are not published framework adapter packages. Exact visuals and behavior remain owned by `src/`, OpenSpec, and the canonical demos.

## Stable consumption

For reproducible downstream use, vendor files from an immutable release tag such as `v0.4.0` rather than the moving `main` branch. A consuming project normally copies:

```text
src/tokens.css
src/tui.css
src/tui.js   # optional unless progressive JS enhancements are needed
```

Load `tokens.css` before `tui.css`. Load `tui.js` once when using `data-tui-escape-close` or `data-tui-list` progressive enhancement.

## Recipes

- `react/PackageConfiguration.jsx` demonstrates controlled React form state while retaining native checkbox semantics and application-owned `tui:escape` handling.
- `vue/PackageConfiguration.vue` demonstrates the same contract in a Vue Single File Component.
- `server-rendered/package-configuration.html` is browser-openable and shows the shape a server-side template loop can emit while preserving ordinary form submission semantics.

## Integration rules

Do not copy CSS declarations out of `src/tui.css` into framework components. Reuse the canonical classes. Do not recreate tokens in JavaScript or framework theme objects when CSS custom properties can be consumed directly.

Native form controls remain the semantic source of truth. Framework state may control their values, but should not replace them with non-semantic clickable containers.

`tui:escape` is an application signal, not an automatic close command. The consuming app decides whether Escape hides a dialog, routes elsewhere, cancels a workflow, or does nothing.

`data-tui-list` is optional progressive focus navigation. Frameworks should not add a second ArrowUp/ArrowDown/Home/End handler on the same list unless they intentionally replace that contract.

See `docs/project/framework-integration.md` for detailed guidance.
