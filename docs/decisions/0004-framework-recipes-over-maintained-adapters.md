# ADR-0004: Framework recipes over maintained adapters

- Status: Accepted
- Date: 2026-09-11
- Related OpenSpec change: `framework-integration-recipes`
- Related issue: #7
- Supersedes: none
- Superseded by: none

## Context

`web-tui-kit` deliberately exposes a browser-native integration contract: semantic HTML, canonical CSS classes/custom properties, and small progressive JavaScript events/focus behavior. The project now needs to show downstream React, Vue, and server-rendered consumers how to use that contract.

A maintained framework adapter layer would add additional public APIs, framework-version compatibility work, package/distribution surfaces, and potential drift from the canonical browser implementation. The current integration needs can already be expressed by framework-generated semantic markup and ordinary event/state handling.

## Decision

Provide copy-ready framework/template **recipes**, not a maintained adapter runtime.

`src/` remains the only canonical runtime implementation. React, Vue, and template examples consume the same class, native-control, and event contracts as plain HTML. They may demonstrate framework-owned state/lifecycle integration, but they must not duplicate the visual implementation or introduce framework dependencies into the base package.

A future adapter proposal requires a concrete capability gap that cannot be handled cleanly with the existing browser-native contract.

## Considered alternatives

- Publish React component wrappers as a separate package.
- Publish Vue components as a separate package.
- Maintain a generic Web Component wrapper layer for all frameworks.
- Provide documentation only, without copy-ready source examples.

## Consequences

### Positive

- Keeps the canonical runtime small and framework-independent.
- Gives humans and coding agents concrete integration examples without new runtime dependencies.
- Avoids duplicated styling and adapter-specific API/versioning burden.
- Lets each consuming framework own normal application state/lifecycle behavior.

### Negative / trade-offs

- Consumers still copy/compose markup instead of importing prebuilt framework components.
- Recipes are illustrative source, not independently version-tested against every framework release.
- If a real framework integration gap appears later, it still requires a new deliberate design decision.

## Evidence / notes

The React, Vue, and server-rendered recipes introduced with issue #7 demonstrate that the current package-dialog contract can be expressed without a framework adapter layer. ADR-0001 remains in force: framework-specific integration must wrap or generate the canonical browser-native contract rather than replace it.
