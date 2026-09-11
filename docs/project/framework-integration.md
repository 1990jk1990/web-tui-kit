# Framework integration

## Principle

`web-tui-kit` remains browser-native. Frameworks consume the documented HTML/class/event contract; they do not become part of the design-system runtime.

The canonical implementation is still:

```text
src/tokens.css
src/tui.css
src/tui.js
```

React, Vue, server-rendered templates, or another application architecture may generate the semantic markup, own application state, and decide navigation/lifecycle behavior around that runtime.

## Pin a release first

For reproducible applications and coding-agent work, copy/vendor from an immutable tag such as `v0.7.0` rather than `main`. This prevents later design-system development from silently changing an existing consumer.

When upgrading to a newer tag, review `CHANGELOG.md`, accepted OpenSpec, and relevant demos before updating vendored assets.

## Asset loading

Load `tokens.css` before `tui.css`. `tui.js` is optional unless the application wants the library's progressive Escape dispatch or `data-tui-list` focus navigation.

Framework build systems may import or copy these files in their normal asset pipeline. That pipeline is application-owned; `web-tui-kit` does not require one.

## Semantic controls and state

Use native buttons, inputs, selects, textareas, forms, links, and progress elements where the canonical patterns call for them. A framework may control the value/checked state of those elements, but should keep the native element in the rendered output.

Do not replace checkboxes or radio buttons with generic clickable `<div>` elements merely to fit framework state management. The design system deliberately styles native controls and depends on their browser semantics.

## `tui:escape`

When `src/tui.js` is loaded, a `.tui-window` or `.tui-dialog` marked with `data-tui-escape-close` dispatches a bubbling `tui:escape` custom event when Escape is pressed.

The consuming application owns the consequence. React/Vue components should attach/remove an event listener for their mounted surface and invoke the application's cancel/close/navigation action. The library does not hide the DOM node itself.

## `data-tui-list`

A container marked with `data-tui-list` receives the optional ArrowUp/ArrowDown/Home/End focus-navigation enhancement from `src/tui.js`.

Do not add competing framework key handlers to the same list unless the application intentionally replaces the library contract. Native radio groups and text-entry controls remain excluded from the enhancement so their browser behavior is preserved.

## Styling boundaries

Framework components should use canonical classes such as `.tui-dialog`, `.tui-checklist`, `.tui-check-row`, `.tui-button`, and `.tui-actions` rather than copying declarations from `src/tui.css` into CSS-in-JS, scoped component styles, or a framework theme object.

Application-specific layout around the design system is allowed. Changes intended to become reusable visual behavior belong back in `web-tui-kit`, not in a private framework wrapper.

## Recipes

- `examples/react/PackageConfiguration.jsx`
- `examples/vue/PackageConfiguration.vue`
- `examples/server-rendered/package-configuration.html`

The React and Vue files are source recipes, not standalone runnable applications in this repository. They assume the consuming application already has the respective framework/toolchain. The server-rendered example is directly browser-openable when the repository is served statically.

## Why there is no adapter package

The current browser-native contract already maps cleanly to React, Vue, and server-rendered markup. A maintained adapter layer would create additional API/versioning/framework-maintenance surfaces without solving a demonstrated capability gap.

If a future consumer identifies behavior that cannot be expressed cleanly through semantic markup, canonical classes, CSS custom properties, and the existing custom-event/progressive-enhancement contracts, that concrete gap can justify a new adapter proposal. Until then, recipes are the lower-risk integration mechanism.
