# web-tui-kit specification

## Purpose

This specification defines the currently accepted externally relevant behavior of `web-tui-kit`. Exact CSS values are implementation details owned by `src/tokens.css`; architecture and rationale live in their respective canonical documents.

## Requirements

### Requirement: Reusable browser UI baseline

The system MUST provide a browser-consumable UI design-system baseline that does not require a JavaScript framework, package manager, bundler, or application build step at runtime.

#### Scenario: Plain browser integration

- **GIVEN** a consuming application can serve static files
- **WHEN** it includes the runtime files from `src/` using the documented order and markup patterns
- **THEN** the core design-system presentation MUST be usable without installing a JavaScript framework

### Requirement: Classic text-interface visual language

The default theme MUST use a visual language inspired by Debian debconf, `dialog`, and `whiptail`: monospace-oriented typography, a blue application background, grey surfaces, hard raised/recessed borders, red title accents, and blue selection states.

The default theme MUST NOT introduce rounded or pill-shaped controls, gradients, blurred effects, translucent glass styling, soft shadows, or modern floating-card aesthetics.

#### Scenario: Default window rendering

- **GIVEN** a page uses the default tokens and `.tui-window`
- **WHEN** it is rendered without a theme override
- **THEN** the window MUST use the established hard-edged surface and bevel language rather than modern rounded-card styling

### Requirement: Canonical package-configuration dialog

The design system MUST provide a `.tui-dialog` pattern that can reproduce the characteristic package-configuration composition used by classic Debian/Ubuntu text interfaces: a grey beveled dialog on the blue desktop, a red title visually interrupting the top border, compact explanatory copy, a recessed selection area, and centered angle-bracket actions.

#### Scenario: Reference dialog rendering

- **GIVEN** a page uses `.tui-screen`, `.tui-dialog`, `.tui-dialog-title`, and `.tui-actions`
- **WHEN** it is rendered with the default theme
- **THEN** the result MUST preserve the canonical hard-edged dialog composition on desktop and narrow viewports

### Requirement: Checklist selection pattern

The design system MUST provide a scrollable checklist pattern using `.tui-checklist` and `.tui-check-row`. Checkbox state and keyboard focus/row selection MUST remain distinct: checking an item changes its `[ ]` marker, while focusing or selecting a row uses the canonical blue selection treatment.

Checklist rows MAY expose short contextual help text using `.tui-help`.

#### Scenario: Keyboard-focused checklist row

- **GIVEN** a checklist row contains a native checkbox
- **WHEN** that checkbox receives keyboard focus
- **THEN** the row MUST expose a visible selected/focused state while the checkbox remains operable through normal browser keyboard behavior

#### Scenario: Long checklist

- **GIVEN** a checklist contains more rows than fit its configured maximum height
- **WHEN** the checklist is rendered
- **THEN** the selection area MUST scroll rather than expanding the dialog without bound

### Requirement: Central design tokens

Reusable palette, typography, spacing, border, shadow, scrollbar, and control-sizing values MUST be centralized as CSS custom properties in `src/tokens.css` rather than independently redefined per component.

#### Scenario: Component style reuse

- **GIVEN** a reusable component needs an established design value
- **WHEN** the component is implemented or changed
- **THEN** it MUST consume the relevant canonical token where one exists

### Requirement: Core component patterns

The design system MUST provide reusable patterns for windows/panels, package-style dialogs, buttons, checkbox and radio rows, scrollable checklists, text/select/textarea inputs, menus/selections, tables, action rows, and status information.

#### Scenario: Consumer uses a documented component

- **GIVEN** a component pattern exists in the design system
- **WHEN** a consuming application follows its documented semantic markup and CSS classes
- **THEN** it MUST receive the design-system presentation without recreating that component's visual language independently

### Requirement: Semantic and keyboard-friendly controls

Interactive component patterns SHOULD use native semantic HTML controls wherever practical. Interactive controls MUST remain keyboard reachable, and hover MUST NOT be the only way to operate or understand a control.

#### Scenario: Keyboard operation

- **GIVEN** a page built from the design system contains native buttons, inputs, and links
- **WHEN** a keyboard user navigates the page
- **THEN** those controls MUST remain reachable through normal browser keyboard navigation and MUST expose a visible focus state

### Requirement: Touch-compatible responsive behavior

The same visual language MUST remain usable on narrow Android-style touch viewports. Responsive behavior MAY increase hit areas, reduce outer spacing, wrap actions, move short help text below a row label, and permit horizontal table scrolling, but MUST NOT replace the interface with an unrelated modern mobile-card design.

#### Scenario: Narrow coarse-pointer viewport

- **GIVEN** the UI is rendered on a narrow viewport with a coarse pointer
- **WHEN** controls and tables no longer fit the desktop spacing
- **THEN** interactive targets MUST remain usable and layout MUST adapt without abandoning the canonical visual language

### Requirement: Preserve table information on narrow screens

Tables that cannot fit the available width SHOULD scroll horizontally rather than silently removing important columns solely to fit the viewport.

#### Scenario: Wide table on a phone

- **GIVEN** a table contains more information than fits the narrow viewport
- **WHEN** it is displayed inside `.tui-table-wrap`
- **THEN** the user MUST be able to reach the overflow horizontally without the component automatically deleting columns

### Requirement: Progressive Escape handling

For a `.tui-window` or `.tui-dialog` that opts in with `data-tui-escape-close`, pressing the Escape key MUST dispatch a bubbling `tui:escape` custom event. The UI kit MUST NOT unilaterally decide whether the consuming application hides, navigates away from, or otherwise closes the surface.

#### Scenario: Opted-in surface receives Escape

- **GIVEN** an opted-in TUI window or dialog is present
- **WHEN** the user presses Escape
- **THEN** the library MUST dispatch `tui:escape` from the applicable surface so the consuming application can decide the resulting action

### Requirement: Linux and Android browser use

The implementation MUST prioritize standards-based behavior suitable for current Chromium-based browsers on Linux desktop and Android. It SHOULD remain usable in current Firefox where the required web standards are supported.

#### Scenario: Supported browser families

- **GIVEN** a consuming application uses documented component patterns without application-specific incompatibilities
- **WHEN** it is opened in a current Chromium-based Linux or Android browser
- **THEN** the design-system baseline MUST render and operate without requiring a platform-specific client application

### Requirement: Executable visual references

The repository MUST provide a browser-openable canonical package-configuration reference at `demo/index.html` and MAY provide additional component-gallery pages. Demo pages MUST reference the canonical runtime assets instead of duplicating their implementation.

#### Scenario: Maintainer reviews the canonical style

- **GIVEN** the repository is served as static files
- **WHEN** a maintainer opens `demo/index.html`
- **THEN** the page MUST load the canonical runtime assets from `src/` and present the package-configuration dialog as the primary visual reference
