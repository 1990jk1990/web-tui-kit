# Public consumer contract

This page is the practical inventory of the consumer-facing `web-tui-kit` surface. Accepted compatibility behavior is canonical in `openspec/specs/public-contract/spec.md`; exact token values and implementation remain canonical in `src/`.

The purpose of this inventory is to make the stability boundary explicit before 1.0. A name listed here is intentionally supported for downstream use. Repository details called out as non-public may change without a consumer migration as long as the documented behavior remains intact.

## Runtime files

The public runtime consists of:

| File | Contract |
| --- | --- |
| `src/tokens.css` | public CSS custom properties and default theme values |
| `src/tui.css` | reusable component/layout/state presentation |
| `src/tui.js` | optional progressive keyboard/custom-event enhancement |

Load `tokens.css` before `tui.css`. `tui.js` is optional unless the application uses `data-tui-escape-close`, `data-tui-list`, or `data-tui-list-item` behavior.

No framework, package manager, bundler, Python runtime, Node.js runtime, or repository test tooling is part of the browser runtime contract.

## Public CSS custom properties

All canonical `--tui-*` custom properties declared in `src/tokens.css` are supported theming hooks. Their **names and purposes** are the compatibility contract; exact defaults may evolve when the meaning stays compatible and applicable visual evidence is updated.

### Palette and state

| Token | Purpose |
| --- | --- |
| `--tui-desktop-bg` | page/application background |
| `--tui-surface` | raised window/control surface |
| `--tui-surface-light` | recessed/light content surface |
| `--tui-text` | primary text |
| `--tui-muted` | secondary and disabled text |
| `--tui-title` | title/mnemonic accent |
| `--tui-selection-bg` | focused/selected area background |
| `--tui-selection-text` | text on focused/selected areas |
| `--tui-help` | contextual help accent |
| `--tui-border-light` | raised light edge |
| `--tui-border-mid` | intermediate/divider/scrollbar edge |
| `--tui-border-dark` | recessed/dark edge |
| `--tui-shadow` | hard window/dialog shadow |
| `--tui-focus` | focus indicator |
| `--tui-danger` | danger/status accent |
| `--tui-success` | success/status accent |

### Typography

| Token | Purpose |
| --- | --- |
| `--tui-font` | canonical monospace-oriented font stack |
| `--tui-font-size` | base UI font size |
| `--tui-line-height` | base UI line height |

### Spacing

`--tui-space-1` through `--tui-space-6` are the supported spacing scale, from smallest to largest canonical spacing step.

### Borders, sizing, and geometry

| Token | Purpose |
| --- | --- |
| `--tui-border-width` | canonical raised/recessed border thickness |
| `--tui-shadow-offset` | hard window/dialog shadow offset |
| `--tui-window-max` | general window maximum width |
| `--tui-dialog-max` | package-style dialog maximum width |
| `--tui-control-min-height` | minimum control target height |
| `--tui-list-row-min-height` | minimum choice-row target height |
| `--tui-scrollbar-size` | classic scrollable-list scrollbar sizing |
| `--tui-progress-height` | gauge/progress height |

The forced-colors media block intentionally changes values to CSS system colors. Consumer overrides should preserve the semantic meaning of a token rather than treating its current literal default as the API.

## Public component classes

The following `tui-*` classes are intentionally reusable consumer hooks.

### Page, surface, and layout

- `tui-desktop`
- `tui-screen`
- `tui-window`
- `tui-panel`
- `tui-dialog`
- `tui-dialog--compact`
- `tui-dialog-title`
- `tui-dialog-copy`
- `tui-section`
- `tui-stack`
- `tui-grid`
- `tui-field`
- `tui-actions`

### Typography and status helpers

- `tui-title`
- `tui-heading`
- `tui-muted`
- `tui-hotkey`
- `tui-help`
- `tui-kbd`
- `tui-success`
- `tui-danger`
- `tui-statusbar`

### Form controls and choices

- `tui-input`
- `tui-select`
- `tui-textarea`
- `tui-button`
- `tui-check`
- `tui-radio`
- `tui-choice-list`
- `tui-checklist`
- `tui-radiolist`
- `tui-check-row`
- `tui-radio-row`
- `tui-mark`
- `tui-menu-row`
- `tui-menu`
- `tui-menu-item`

### Progress and tables

- `tui-gauge`
- `tui-progress`
- `tui-gauge-value`
- `tui-table-wrap`
- `tui-table`

There are 42 current public `tui-*` classes in total. Structural regression tests compare this inventory with the canonical runtime so an accidental addition/removal cannot silently become or cease to be public surface.

## Public scoped state hooks

Two generic state-class names are intentionally supported only in combination with the TUI component selectors that consume them:

- `.is-active` on `.tui-button`
- `.is-selected` on checklist rows, radio rows, menu rows/items, and table rows where implemented

These names are not global styling APIs. An unrelated `.is-selected` elsewhere in an application receives no design-system contract.

## Semantic markup expectations

The public surface includes important HTML relationships because the library intentionally relies on native browser semantics rather than replacing them with a JavaScript component runtime.

- `.tui-button` and `.tui-menu-row` should be native `<button>` controls.
- `.tui-input`, `.tui-select`, and `.tui-textarea` should style the corresponding native form elements.
- `.tui-check` and `.tui-radio` retain native checkbox/radio inputs followed by their visible label span.
- `.tui-check-row` and `.tui-radio-row` retain native inputs and the adjacent `.tui-mark` span used for the text marker.
- `.tui-progress` should be a native `<progress>` element; repeated visible percentage text may use `.tui-gauge-value` and may be presentation-only.
- `.tui-table` should remain semantic table markup inside `.tui-table-wrap` when horizontal overflow is required.
- `.tui-dialog` is presentation only. A true modal is application-owned and must use native `<dialog>` or another deliberate application-level semantic/lifecycle implementation.

The exact IDs, copy, row order, sample values, and page-specific wiring in `demo/` are examples rather than stable API.

## Public progressive JavaScript names

`src/tui.js` exposes behavior through DOM attributes/events rather than an imported JavaScript module API.

| Name | Contract |
| --- | --- |
| `data-tui-escape-close` | opt-in attribute on `.tui-window` / `.tui-dialog` for Escape signaling |
| `tui:escape` | bubbling custom event emitted for the opted-in surface |
| `event.detail.sourceEvent` | originating keyboard event carried by `tui:escape` |
| `data-tui-list` | opt-in list focus-navigation container |
| `data-tui-list-item` | opt-in marker for a custom focusable list item used with non-negative `tabindex` |

ArrowUp/ArrowDown/Home/End behavior, skipped states, radio/text-input exclusions, and native activation behavior are defined in `openspec/specs/web-tui-kit/spec.md`.

Internal JavaScript constants, helper functions, selector construction, event-listener placement, or implementation style are not public APIs.

## Framework/template integration boundary

React, Vue, and server-rendered examples are public **consumption guidance**, not adapter packages. Consumers may copy/adapt those recipes, but the stable runtime contract remains the resulting native markup, TUI classes/custom properties, `data-tui-*` attributes, and `tui:escape` behavior.

The following are not public runtime APIs:

- example component/local variable names,
- fixture/test IDs,
- generated framework verification bundles,
- `tests/framework/` helper interfaces,
- exact pinned React/Vue/esbuild versions used as representative CI evidence.

A consumer can therefore change framework versions or its application architecture without requiring a `web-tui-kit` runtime adapter, provided it continues to emit the supported browser-native contract.

## Explicitly non-public repository details

Do not build downstream dependencies on:

- `demo/` IDs, exact explanatory text, sample option names, or ordering,
- files under `tests/`, `test-results/`, visual baseline names, or browser fixture details,
- `scripts/` Python APIs or function names,
- GitHub Actions job/step names and workflow implementation details,
- generated `docs/generated/`, `site/`, `dist/`, or framework verification output,
- CSS declaration/selector order, selector grouping, pseudo-element technique, or media-query organization,
- JavaScript private local/helper names,
- exact browser/framework/tool versions used as verification evidence.

The canonical demos remain the normative visual/semantic reference for **documented reusable patterns**. This does not make incidental demo-page implementation details public API.

## Compatibility and migration policy

### Before 1.0

- PATCH: compatible fixes/refinements that preserve documented public contracts.
- MINOR: new public capability and any intentional incompatible change to the evolving pre-1.0 public contract.
- Any pre-1.0 breaking public change must be explicit in `CHANGELOG.md` and include migration guidance where an existing consumer pattern must change.
- Published tags stay immutable; fixes move forward to a new version.

### Starting at 1.0

- PATCH preserves the declared public contract.
- MINOR may add compatible surface and deprecate existing surface.
- MAJOR is required for incompatible removal/rename, required semantic-markup changes, token repurposing, or breaking changes to documented events/data attributes.
- Planned public removals should be deprecated with replacement/migration guidance in at least one prior MINOR release before removal in a later MAJOR release. Urgent security/legal/standards cases may require faster action, but the break and migration must still be explicit.

Changing a token's default value is not automatically a breaking API change if the token retains the same documented purpose. Changing its purpose is.

## Pre-1.0 cleanup found by the audit

The audit found one implementation inconsistency worth correcting without renaming public surface: the public `--tui-help` token existed, including a forced-colors `LinkText` override, while `.tui-help` incorrectly consumed `--tui-title`. `v0.9` corrects `.tui-help` to consume `--tui-help`. Normal default pixels remain unchanged because both normal tokens currently share the same red value; forced-colors behavior now matches the documented token purpose.

No other current class, token, event, or `data-tui-*` name requires a pre-1.0 rename/removal from the audited surface.

## 1.0 exit criteria

The project may prepare `1.0.0` after all of the following are true:

1. this public inventory and the OpenSpec stability rules are accepted and protected by structural tests;
2. selected pre-1.0 cleanup is complete, with no known intentional public rename/removal still waiting for the audit;
3. structural tests, AI-DOC-1 validation, strict docs build, canonical Chromium visual regression, Chromium/Firefox interaction regression, Chromium/Firefox accessibility-semantic regression, representative framework-recipe regression, and deterministic release-archive validation pass for the candidate;
4. 1.0 release docs/changelog consistently state the normal Semantic Versioning stability commitment;
5. the focused release archive includes this guide and the canonical consumer references;
6. evidence boundaries remain explicit rather than turning unperformed physical-device, assistive-technology, WCAG, registry, or broad framework-matrix work into unsupported claims.

Physical Android certification, real screen-reader/assistive-technology certification, WCAG certification, npm publication, maintained React/Vue adapters, and a broad framework-version matrix are not current 1.0 prerequisites. They remain separate evidence/product decisions unless a future accepted requirement makes one mandatory.
