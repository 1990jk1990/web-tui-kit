# Framework integration recipes

Status: Completed
Related issue: #7
Change class: Class 2 — integration architecture/documentation

## Motivation

`web-tui-kit` has a tagged pre-1.0 release and a stable browser-native integration contract, but downstream applications may use React, Vue, or server-rendered templates. Humans and coding agents need concrete examples showing how those stacks consume the canonical runtime without inventing framework-specific styling or assuming a separate adapter package exists.

## Accepted behavior

- Added copy-ready React, Vue, and server-rendered integration recipes.
- Every recipe reuses the canonical `src/` asset, class, semantic-control, and custom-event contracts rather than reimplementing the design system.
- `src/` remains framework-independent and free of React/Vue/template-engine dependencies.
- Integration guidance documents asset loading, native form state, `tui:escape`, optional `data-tui-list` navigation, and immutable release tags.
- Recipes are consumption examples, not a second runtime or compatibility layer.
- The focused release archive now includes the integration guide and recipes so downstream consumers can use them without the full development repository.
- No maintained framework adapter package is introduced because no concrete capability gap was demonstrated.

## Compatibility and boundaries

The React and Vue examples are source recipes intended to be copied into applications that already use those frameworks; this repository does not add those frameworks as development or runtime dependencies. The server-rendered recipe is browser-openable static HTML and represents the template-oriented integration shape.

No visual tokens or component CSS are duplicated in the recipes. The canonical visual implementation remains under `src/` and the canonical executable reference remains under `demo/`.

## Verification

- Structural recipe tests pass and guard canonical class/event reuse plus the no-parallel-styling/runtime-dependency boundary.
- Existing repository/release structural tests pass, including the expanded deterministic release allowlist.
- AI-DOC-1 structural validation and strict MkDocs build pass.
- Existing desktop/mobile visual baselines remain unchanged and pass.
- PR diff was reviewed before archival.

## Result

The browser-native contract is sufficient for the evaluated React, Vue, and server-rendered integration scenarios. ADR-0004 records the decision to prefer recipes over maintained adapter runtimes until a real capability gap justifies another public integration layer.
