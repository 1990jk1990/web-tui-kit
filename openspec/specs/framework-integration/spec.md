# Framework integration specification

## Purpose

This specification defines the accepted integration contract for consuming `web-tui-kit` from framework-based or server-rendered applications without changing the browser-native runtime baseline.

## Requirements

### Requirement: Framework integration recipes

The repository MUST provide copy-ready integration recipes for React, Vue, and server-rendered/template-oriented applications.

The recipes MUST demonstrate the canonical package-dialog class and semantic-control contracts rather than implementing a separate visual system.

#### Scenario: React consumer

- **GIVEN** a React application has vendored the canonical `src/` runtime assets from a pinned release
- **WHEN** it follows the React integration recipe
- **THEN** it MUST be able to render the package-dialog pattern with native controls and canonical classes without a `web-tui-kit` React runtime package

#### Scenario: Vue consumer

- **GIVEN** a Vue application has vendored the canonical `src/` runtime assets from a pinned release
- **WHEN** it follows the Vue integration recipe
- **THEN** it MUST be able to render the package-dialog pattern with native controls and canonical classes without a `web-tui-kit` Vue runtime package

#### Scenario: Server-rendered consumer

- **GIVEN** a server-rendered application emits HTML from templates
- **WHEN** it follows the server-rendered recipe
- **THEN** ordinary semantic form controls and canonical classes MUST be sufficient to receive the design-system presentation and progressive enhancement

### Requirement: Canonical runtime remains framework-independent

Framework integration material MUST NOT introduce React, Vue, a template engine, package manager, bundler, or framework-specific adapter as a dependency of `src/`.

#### Scenario: Consumer does not use a framework

- **GIVEN** a plain browser application consumes `src/`
- **WHEN** framework integration recipes are present in the repository
- **THEN** the application MUST NOT need any framework dependency that was introduced solely for those recipes

### Requirement: Recipes reuse the canonical visual contract

Framework/template recipes MUST use the canonical CSS classes and native-control patterns and MUST NOT embed a parallel copy of the design tokens or reusable component CSS.

#### Scenario: Maintainer changes a visual token

- **GIVEN** a canonical token or component style changes in `src/`
- **WHEN** framework integration recipes are reviewed
- **THEN** they SHOULD continue to consume the changed canonical asset rather than requiring a duplicated framework-specific style update

### Requirement: Application-owned lifecycle behavior

Framework/template consumers MUST treat `tui:escape` as an application signal. A recipe MAY show how to attach the event to framework lifecycle/state, but MUST NOT redefine the library event or imply that the library owns application navigation/closing behavior.

#### Scenario: Framework dialog receives Escape

- **GIVEN** a framework-rendered `.tui-dialog[data-tui-escape-close]` has `src/tui.js` loaded
- **WHEN** `tui:escape` is dispatched
- **THEN** the framework/application handler MUST decide whether to cancel, close, route, or otherwise respond

### Requirement: Optional list enhancement is not duplicated

When a recipe uses `data-tui-list`, it MUST rely on the canonical progressive enhancement from `src/tui.js` unless the consuming application intentionally replaces that contract.

#### Scenario: Checklist inside a framework

- **GIVEN** a React/Vue/template checklist uses `data-tui-list`
- **WHEN** the canonical JavaScript is loaded
- **THEN** the recipe MUST NOT add a competing ArrowUp/ArrowDown/Home/End navigation implementation for the same list

### Requirement: Stable downstream reference

Integration guidance MUST recommend immutable release tags for reproducible downstream use and coding-agent references rather than treating the moving `main` branch as a stable contract.

#### Scenario: Coding agent integrates a released design-system version

- **GIVEN** a project wants a stable `web-tui-kit` reference
- **WHEN** its implementation instructions are written
- **THEN** they SHOULD point to a specific immutable tag such as `v0.5.0` until the project intentionally upgrades

### Requirement: Adapter runtime requires a demonstrated gap

The project MUST NOT add a maintained framework adapter runtime solely for convenience while the browser-native contract is sufficient. A future adapter MUST be justified by a concrete integration capability gap and an accepted architecture/specification change.

#### Scenario: New framework wrapper proposal

- **GIVEN** a proposal asks to add maintained React/Vue/other adapter code
- **WHEN** existing semantic markup, canonical classes, CSS custom properties, and progressive events can already express the required behavior
- **THEN** the adapter SHOULD NOT be added as a new maintained runtime surface
