# web-tui-kit design system

This document is the practical guide for consuming the design system.

For AI-DOC-1 source-of-truth purposes, **accepted behavior is canonical under `openspec/specs/`**, exact token values are canonical in `src/tokens.css`, and implementation is canonical in `src/`. If this guide disagrees with those sources, correct the stale guide rather than creating a parallel rule.

## 1. Visual reference

The design language is inspired by classic Debian/Ubuntu package configuration screens built around debconf, `dialog`, and `whiptail`.

This is a browser UI, not a terminal emulator. Applications may use normal HTML forms, tables, APIs, routing, and JavaScript while presenting them with a classic text-interface visual language.

The canonical package-configuration reference is `demo/index.html`. Broader component and dialog examples live in `demo/components.html` and `demo/dialogs.html`.

## 2. Core principles

**Hard edges.** Rectangles only. No rounded corners.

**Monospace typography.** The UI should feel text-oriented even when rendered in a graphical browser.

**Beveled surfaces.** Raised controls use a light top/left edge and dark bottom/right edge. Recessed controls reverse that relationship.

**Limited palette.** A blue application background, grey surfaces, dark text, red headings/help accents, and blue selections form the default theme.

**Dense but usable.** Desktop layouts may be compact. On touch devices the same visual language gets larger hit areas rather than a different design.

**Semantic HTML first.** Prefer native buttons, inputs, labels, fieldsets, tables, progress elements, and links. Styling must not replace native control semantics unnecessarily.

## 3. Canonical tokens

The exact machine-readable values live in `src/tokens.css`.

| Token | Purpose |
| --- | --- |
| `--tui-desktop-bg` | page/application background |
| `--tui-surface` | window and control surface |
| `--tui-surface-light` | recessed/light content surface |
| `--tui-text` | primary text |
| `--tui-muted` | secondary/disabled text |
| `--tui-title` | dialog title and access-key accent |
| `--tui-selection-bg` | focused/selected row background |
| `--tui-selection-text` | text on selected areas |
| `--tui-help` | contextual help accent |
| `--tui-border-light` | raised top/left edge |
| `--tui-border-dark` | raised bottom/right edge |
| `--tui-focus` | keyboard focus indicator |
| `--tui-dialog-max` | package-style dialog maximum width |
| `--tui-list-row-min-height` | dialog-list row sizing |
| `--tui-scrollbar-size` | classic list scrollbar sizing |
| `--tui-progress-height` | canonical gauge/progress height |

Spacing and sizing values are also centralized in `src/tokens.css`.

When `forced-colors: active` is reported by the browser, the default tokens map to CSS system colors such as `Canvas`, `CanvasText`, `Highlight`, `HighlightText`, `GrayText`, and `LinkText`. Do not defeat those overrides with per-component hard-coded colors.

## 4. Typography

Use:

```css
font-family: var(--tui-font);
```

The default stack prefers commonly available Linux/Android monospace fonts and falls back to the generic `monospace` family. Avoid mixing proportional UI fonts into the core application chrome.

## 5. Windows and dialogs

Use `.tui-window` for a general application surface. Use `.tui-dialog` for the classic package-configuration composition with `.tui-dialog-title` positioned over the top bevel. `.tui-dialog--compact` constrains simple message, confirmation, input, and gauge dialogs.

A full-screen centered dialog may be wrapped in `.tui-screen`.

Typical message box:

```html
<section class="tui-dialog tui-dialog--compact" aria-labelledby="message-title">
  <h1 class="tui-dialog-title" id="message-title">Message</h1>
  <p class="tui-dialog-copy">Operation completed.</p>
  <div class="tui-actions">
    <button class="tui-button" type="button">Ok</button>
  </div>
</section>
```

`.tui-dialog` is a visual component, not a modal implementation. If an application needs a true modal, it must provide appropriate native `<dialog>` or equivalent dialog semantics, focus/lifecycle handling, and dismissal behavior. The UI kit does not add focus traps automatically.

A yes/no dialog uses the same composition with two `.tui-button` actions. An input dialog adds a native input styled with `.tui-input` inside `.tui-field`.

Nested content groups may use `.tui-panel`. General page sections may use `.tui-section` for canonical vertical spacing.

## 6. Buttons and access keys

Use native `<button>` elements with `.tui-button`. Buttons are raised by default and appear pressed while active. Focus is indicated independently from hover.

The angle brackets are added by the component styling. `.tui-hotkey` may underline a visible mnemonic character. Native `accesskey` behavior is browser/platform dependent, so only add an `accesskey` when the consuming application intentionally accepts that platform behavior.

```html
<button class="tui-button" type="button" accesskey="o">
  <span class="tui-hotkey">O</span>k
</button>
```

Action rows use `.tui-actions`.

## 7. Checkbox and radio controls

For ordinary form rows, use `.tui-check` and `.tui-radio`. The native input remains present for semantics and keyboard behavior while the visible marker uses `[ ]`, `[x]`, `( )`, and `(*)`.

For dialog-style scrolling lists, use `.tui-checklist` with `.tui-check-row` or `.tui-radiolist` with `.tui-radio-row`. Each row contains the native input, `.tui-mark`, label text, and optionally `.tui-help`.

Radio lists deliberately preserve native browser radio-group arrow behavior and therefore should **not** use `data-tui-list`:

```html
<div class="tui-radiolist" role="radiogroup" aria-label="Mode">
  <label class="tui-radio-row">
    <input type="radio" name="mode" checked>
    <span class="tui-mark" aria-hidden="true"></span>
    <span>Safe mode</span>
    <span class="tui-help">&lt;Recommended&gt;</span>
  </label>
</div>
```

Checkbox/radio state and row focus are deliberately separate. Checking or selecting changes the marker; keyboard focus or `.is-selected` applies the blue selection treatment to the row. Disabled inputs give their containing rows the muted disabled treatment automatically.

`.tui-help` is intended for short contextual text such as `<Help>`, not long explanations.

## 8. Input controls

Use `.tui-input`, `.tui-select`, and `.tui-textarea`. These controls are recessed rather than raised and retain normal HTML form behavior. Text-entry controls are never targets of the optional list-navigation enhancement, so arrow keys remain available for caret/selection behavior.

## 9. Menu and choice lists

`.tui-choice-list` is the generic recessed container for dialog-style choices. `.tui-menu-row` is a full-width native button for action/menu lists.

Use the optional `data-tui-list` attribute when a checklist or action list should support terminal-like focus navigation. Supported list items are enabled native checkboxes, enabled buttons, enabled links, and custom focusable elements that explicitly use `data-tui-list-item` plus a non-negative `tabindex`.

- `ArrowUp` and `ArrowDown` move focus and wrap at the ends.
- `Home` focuses the first enabled supported item.
- `End` focuses the last enabled supported item.
- disabled, inert, hidden, and `aria-hidden` items are skipped.
- normal `Tab` reachability is preserved.
- activation and selection remain native; the enhancement does not synthesize Space/Enter behavior.
- native radios and text-entry controls are intentionally not intercepted.

The enhancement does not create a custom ARIA listbox or replace native semantics.

The older `.tui-menu` / `.tui-menu-item` pattern remains available for navigation-link menus.

## 10. Gauge and progress

Use native `<progress>` with `.tui-progress`, normally inside `.tui-gauge`. A visible numeric value may use `.tui-gauge-value`.

```html
<div class="tui-gauge">
  <label for="progress">Installing packages</label>
  <progress class="tui-progress" id="progress" value="65" max="100">65%</progress>
  <div class="tui-gauge-value" aria-hidden="true">65%</div>
</div>
```

The progress element owns the semantic value; the visible percentage is decorative when it repeats the same value.

## 11. Tables

Use `.tui-table-wrap` around `.tui-table`. On narrow screens the wrapper scrolls horizontally. Do not hide important columns merely to fit a phone viewport.

## 12. Status information

Use `.tui-statusbar` for short application-level state or keyboard hints. It should visually belong to the same system, not resemble a modern toast or floating card. If status content changes dynamically and must be announced, the consuming application is responsible for choosing an appropriate live-region strategy.

## 13. Escape behavior

Native browser keyboard behavior is preferred. `src/tui.js` adds only small progressive enhancements.

For `.tui-window[data-tui-escape-close]` or `.tui-dialog[data-tui-escape-close]`, pressing `Escape` dispatches a bubbling `tui:escape` event. The consuming application decides whether to hide, navigate, or otherwise close the surface.

Do not trap focus unless a consuming application implements a true modal dialog.

## 14. Motion, touch, and responsive behavior

The core stylesheet does not require decorative animations, transitions, or smooth scrolling. The interface therefore remains usable without forcing motion effects on users who prefer reduced motion.

For coarse pointers, interactive elements receive larger minimum heights and padding while borders, colors, typography, and component structure remain in the same visual language.

At small widths, outer page padding is reduced, windows/dialogs can use the full available width, action rows may wrap, list help text may move below the main label, tables scroll, and no component may require hover to operate.

## 15. Things that do not belong in the default theme

- rounded corners or pill controls
- gradients
- blur or translucent glass effects
- soft box shadows
- floating material-style cards
- icon-only controls without accessible text
- arbitrary per-page color palettes
- interaction that is available only through hover
- custom keyboard behavior that replaces a native control's expected semantics without a documented requirement

## 16. Compatibility target

The current compatibility requirement is defined in `openspec/specs/web-tui-kit/spec.md`. The implementation is designed around standards-based browser features for current Chromium-based browsers on Linux and Android and should remain usable in current Firefox.
