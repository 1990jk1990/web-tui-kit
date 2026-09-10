# web-tui-kit design system

## 1. Visual reference

The design language is inspired by classic Debian/Ubuntu package configuration screens built around debconf, `dialog`, and `whiptail`.

This is a browser UI, not a terminal emulator. Applications may use normal HTML forms, tables, APIs, routing, and JavaScript while presenting them with a classic text-interface visual language.

## 2. Core principles

**Hard edges.** Rectangles only. No rounded corners.

**Monospace typography.** The UI should feel text-oriented even when rendered in a graphical browser.

**Beveled surfaces.** Raised controls use a light top/left edge and dark bottom/right edge. Recessed controls reverse that relationship.

**Limited palette.** A blue application background, grey surfaces, dark text, red headings, and blue selections form the default theme.

**Dense but usable.** Desktop layouts may be compact. On touch devices the same visual language gets larger hit areas rather than a different design.

**Semantic HTML first.** Prefer native buttons, inputs, labels, fieldsets, tables, and links.

## 3. Canonical tokens

The exact machine-readable values live in `src/tokens.css`.

| Token | Purpose |
| --- | --- |
| `--tui-desktop-bg` | page/application background |
| `--tui-surface` | window and control surface |
| `--tui-text` | primary text |
| `--tui-muted` | secondary text |
| `--tui-title` | important dialog/window title |
| `--tui-selection-bg` | selected row / active choice |
| `--tui-selection-text` | text on selected areas |
| `--tui-border-light` | raised top/left edge |
| `--tui-border-dark` | raised bottom/right edge |
| `--tui-focus` | keyboard focus indicator |

Spacing and sizing tokens are also centralized in `src/tokens.css`.

## 4. Typography

Use the following family category:

```css
font-family: var(--tui-font);
```

The default stack prefers commonly available Linux/Android monospace fonts and falls back to the generic `monospace` family.

Avoid mixing proportional UI fonts into the core application chrome.

## 5. Windows and panels

Use `.tui-window` for the primary dialog/panel surface.

A window should:

- sit on the canonical blue desktop background,
- have a grey surface,
- use a hard bevel and hard offset shadow,
- remain readable at narrow widths,
- use `.tui-title` for its main heading.

Nested content groups may use `.tui-panel`.

## 6. Buttons

Use native `<button>` elements with `.tui-button`.

Buttons are raised by default and appear pressed while active. Focus is indicated independently from hover so keyboard navigation remains obvious.

Action rows use `.tui-actions`.

## 7. Checkbox and radio controls

Use `.tui-check` for checkbox rows and `.tui-radio` for radio rows. The native input remains present for semantics and keyboard behavior while the visible marker uses the text-oriented `[ ]`, `[x]`, `( )`, and `(*)` language.

## 8. Text inputs and selects

Use `.tui-input`, `.tui-select`, and `.tui-textarea`.

These controls are recessed rather than raised. They must retain normal HTML form behavior.

## 9. Lists, menus, and selection

Use `.tui-menu` and `.tui-menu-item` for selectable navigation or action lists. `.is-selected` marks the current item.

Selection uses `--tui-selection-bg` and `--tui-selection-text`.

## 10. Tables

Use `.tui-table-wrap` around `.tui-table`. On narrow screens the wrapper scrolls horizontally. Do not hide important columns merely to fit a phone viewport.

## 11. Status information

Use `.tui-statusbar` for short application-level state or keyboard hints. It should visually belong to the same system, not resemble a modern toast or floating card.

## 12. Keyboard behavior

Native browser keyboard behavior is preferred. `src/tui.js` adds only small progressive enhancements.

For `.tui-window[data-tui-escape-close]`, pressing `Escape` dispatches a `tui:escape` event. The consuming application decides whether to hide, navigate, or otherwise close the window.

Do not trap focus unless a consuming application implements a true modal dialog.

## 13. Touch behavior

For coarse pointers, interactive elements receive larger minimum heights and padding. Visual borders, colors, typography, and component structure remain unchanged.

## 14. Responsive behavior

At small widths:

- outer page padding is reduced,
- windows can use the full available width,
- action rows may wrap,
- tables scroll,
- no component should require hover.

## 15. Things that do not belong in the default theme

- rounded corners
- pill buttons
- gradients
- blur
- translucent glass effects
- soft box shadows
- floating material-style cards
- icon-only controls without accessible text
- arbitrary per-page color palettes

## 16. Compatibility target

The baseline target is current Chromium-based browsers on Linux and Android, while retaining standards-based behavior that also works in current Firefox.
