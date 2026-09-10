# ADR-0001: Framework-independent browser-native baseline

- Status: Accepted
- Date: 2026-09-10
- Related OpenSpec change: none; this records the initial accepted baseline
- Related issue: none
- Supersedes: none
- Superseded by: none

## Context

The repository is intended to be reused by multiple independent browser applications and by coding assistants that need a small canonical UI reference. Existing project goals explicitly avoid framework lock-in and the initial implementation is already directly consumable as HTML, CSS, and JavaScript without a build step.

A framework requirement at the design-system layer would force otherwise unrelated consuming applications to adopt the same runtime or add an adapter merely to obtain the visual system.

## Decision

The `web-tui-kit` runtime baseline is plain browser-native CSS and JavaScript with semantic HTML contracts. It does not require a JavaScript framework, package manager, bundler, or application build step.

Consuming applications may use frameworks or build systems. They are compatible when they preserve the documented component semantics, class contracts, and accepted behavior.

## Considered alternatives

- Build the kit directly as components for one JavaScript framework.
- Adopt a general-purpose CSS/component framework and theme it to resemble the target style.
- Require custom Web Components as the primary integration contract.

## Consequences

### Positive

- Low integration cost for plain and framework-based applications.
- Small runtime and small conceptual surface for humans and coding agents.
- No framework lifecycle or package-manager dependency in the UI kit itself.

### Negative / trade-offs

- Consumers must assemble semantic markup instead of importing framework-specific components.
- Rich stateful widgets may require careful progressive enhancement as the library grows.
- Framework-specific wrappers, if desired later, must remain adapters around the canonical browser-native contract unless this decision is superseded.

## Evidence / notes

The rationale above is supported by the existing repository goals and initial implementation. It does not attempt to reconstruct motivations beyond those durable project facts.
