# Framework integration recipes

Status: Active
Related issue: #7
Change class: Class 2 — integration architecture/documentation

## Motivation

`web-tui-kit` now has a tagged pre-1.0 release and a stable browser-native integration contract, but downstream applications may use React, Vue, or server-rendered templates. Humans and coding agents should be able to see exactly how those stacks consume the canonical runtime without inventing framework-specific styling or assuming a separate adapter package exists.

## Proposed behavior

- Add copy-ready React, Vue, and server-rendered integration recipes.
- Every recipe reuses the canonical `src/` asset, class, semantic-control, and custom-event contracts rather than reimplementing the design system.
- Keep `src/` framework-independent and free of React/Vue/template-engine dependencies.
- Document how consuming frameworks should handle asset loading, native form state, `tui:escape`, optional `data-tui-list` navigation, and immutable release tags.
- Treat recipes as consumption examples, not a second runtime or compatibility layer.
- Do not add a maintained framework adapter package unless a concrete capability gap is demonstrated that cannot be handled cleanly by the browser-native contract.

## Compatibility and boundaries

The React and Vue examples are source recipes intended to be copied into applications that already use those frameworks; this repository does not add those frameworks as development or runtime dependencies. The server-rendered recipe is browser-openable static HTML and represents the template-oriented integration shape.

No visual tokens or component CSS are duplicated in the recipes. The canonical visual implementation remains under `src/` and the canonical executable reference remains under `demo/`.

## Acceptance criteria

- React, Vue, and server-rendered recipes exist and use canonical class names/native controls.
- The recipes show application-owned handling of `tui:escape` without changing the library event contract.
- Framework-specific state handling does not replace native input semantics.
- No React/Vue/package-manager dependency is added to the base repository runtime or verification requirements.
- Structural tests enforce that recipes reuse the canonical design-system contract rather than embedding a parallel style implementation.
- Integration documentation explains stable tag pinning and the distinction between core runtime, recipes, and application logic.
- Architecture/ADR, README, developer docs, OpenSpec, and tests are reconciled.
