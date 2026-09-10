# web-tui-kit design system

This document is the practical guide for consuming the design system.

For AI-DOC-1 source-of-truth purposes, **accepted behavior is canonical under `openspec/specs/`**, exact token values are canonical in `src/tokens.css`, and implementation is canonical in `src/`. If this guide disagrees with those sources, correct the stale guide rather than creating a parallel rule.

## 1. Visual reference

The design language is inspired by classic Debian/Ubuntu package configuration screens built around debconf, `dialog`, and `whiptail`.

This is a browser UI, not a terminal emulator. Applications may use normal HTML forms, tables, APIs, routing, and JavaScript while presenting them with a classic text-interface visual language.

The primary executable reference is `demo/index.html`. `demo/components.html` is a broader component gallery.

## 2. Core principles

**Hard edges.** Rectangles only. No rounded corners.

**Monospace typography.** The UI should feel text-oriented even when rendered in a graphical browser.

**Beveled surfaces.** Raised controls use a light top/left edge and dark bottom/right edge. Recessed controls reverse that relationship.

**Limited palette.** A blue application background, grey surfaces, dark text, red headings/help accents, and blue selections form the default theme.

**Dense but usable.** Desktop layouts may be compact. On touch devices the same visual language gets larger hit areas rather than a different design.

**Semantic HTML first.** Prefer native buttons, inputs, labels, fieldsets, tables, and links.

## 3. Canonical tokens

The exact machine-readable values live in `src/tokens.css`.

| Token | Purpose |
| --- | --- |
| `--tui-desktop-bg` | page/application background |
| `--tui-surface` | window and control surface |
| `--tui-surface-light` | recessed/light content surface |
| `--tui-text` | primary text |
| `--tui-muted` | secondary text |
| `--tui-title` | dialog title and access-key accent |
| `--tui-selection-bg` | focused/selected row background |
| `--tui-selection-text` | text on selected areas |
| `--tui-help` | contextual help accent |
| `--tui-border-light` | raised top/left edge |
| `--tui-border-dark` | raised bottom/right edge |
| `--tui-focus` | keyboard focus indicator |
| `--tui-dialog-max` | package-style dialog maximum width |
| `--tui-list-row-min-height` | checklist row sizing |
| `--tui-scrollbar-size` | classic checklist scrollbar sizing |

Spacing and sizing values are also centralized in `src/tokens.css`.

## 4. Typography

Use:

```css
font-family: var(--tui-font);
```

The default stack prefers commonly available Linux/Android monospace fonts and falls back to the generic `monospace` family. Avoid mixing proportional UI fonts into the core application chrome.

## 5. Windows and package-style dialogs

Use `.tui-window` for general application panels and `.tui-dialog` for the classic package-configuration composition.

A package-style dialog normally has this structure:

```html
<main class="tui-screen">
  <section class="tui-dialog" aria-labelledby="dialog-title">
    <h1 class="tui-dialog-title" id="dialog-title">Package configuration</h1>
    <p class="tui-dialog-copy">Choose an option.</p>
    ...
  </section>
</main>
```

`.tui-dialog-title` is intentionally positioned over the top edge so the title visually interrupts the bevel, matching the classic dialog/whiptail composition. `.tui-screen` centers the dialog without making the design system a terminal emulator.

Nested content groups may use `.tui-panel`. General page sections may use `.tui-section` for canonical vertical spacing.

## 6. Buttons and access keys

Use native `<button>` elements with `.tui-button`. Buttons are raised by default and appear pressed while active. Focus is indicated independently from hover.

The angle brackets are added by the component styling. To mark a visible access key, use `.tui-hotkey` inside the button text:

```html
<button class="tui-button" type="button" accesskey="o">
  <span class="tui-hotkey">O</span>k
</button>
```

Action rows use `.tui-actions`.

## 7. Checkbox and radio controls

For ordinary form rows, use `.tui-check` and `.tui-radio`. The native input remains present for semantics and keyboard behavior while the visible marker uses `[ ]`, `[x]`, `( )`, and `(*)`.

For package-style scrollable multi-selection, use `.tui-checklist` with `.tui-check-row`:

```html
<div class="tui-checklist" role="group" aria-label="Services">
  <label class="tui-check-row">
    <input type="checkbox" checked>
    <span class="tui-mark" aria-hidden="true"></span>
    <span>ssh.service</span>
    <span class="tui-help">&lt;Help&gt;</span>
  </label>
</div>
```

Checkbox state and row focus are deliberately separate. Checking changes the marker; keyboard focus or `.is-selected` applies the blue selection treatment to the row. Long checklists scroll vertically.

`.tui-help` is intended for short contextual text such as `<Help>`, not long explanations.

## 8. Text inputs and selects

Use `.tui-input`, `.tui-select`, and `.tui-textarea`. These controls are recessed rather than raised and retain normal HTML form behavior.

## 9. Lists, menus, and selection

Use `.tui-menu` and `.tui-menu-item` for selectable navigation or action lists. `.is-selected` marks the current item. Selection colors come from the canonical selection tokens.

## 10. Tables

Use `.tui-table-wrap` around `.tui-table`. On narrow screens the wrapper scrolls horizontally. Do not hide important columns merely to fit a phone viewport.

## 11. Status information

Use `.tui-statusbar` for short application-level state or keyboard hints. It should visually belong to the same system, not resemble a modern toast or floating card.

## 12. Keyboard behavior

Native browser keyboard behavior is preferred. `src/tui.js` adds only small progressive enhancements.

For `.tui-window[data-tui-escape-close]` or `.tui-dialog[data-tui-escape-close]`, pressing `Escape` dispatches a `tui:escape` event. The consuming application decides whether to hide, navigate, or otherwise close the surface.

Do not trap focus unless a consuming application implements a true modal dialog.

## 13. Touch and responsive behavior

For coarse pointers, interactive elements receive larger minimum heights and padding while borders, colors, typography, and component structure remain in the same visual language.

At small widths, outer page padding is reduced, windows/dialogs can use the full available width, action rows may wrap, checklist help text may move below the label, tables scroll, and no component may require hover to operate.

## 14. Things that do not belong in the default theme

- rounded corners or pill controls
- gradients
- blur or translucent glass effects
- soft box shadows
- floating material-style cards
- icon-only controls without accessible text
- arbitrary per-page color palettes

## 15. Compatibility target

The current compatibility requirement is defined in `openspec/specs/web-tui-kit/spec.md`. The implementation is designed around standards-based browser features for current Chromium-based browsers on Linux and Android and should remain usable in current Firefox.
