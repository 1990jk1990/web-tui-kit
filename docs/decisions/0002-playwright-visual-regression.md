# ADR-0002: Playwright-based visual regression verification

- Status: Accepted
- Date: 2026-09-11
- Related OpenSpec change: `openspec/changes/visual-regression/`
- Related issue: #5
- Supersedes: none
- Superseded by: none

## Context

The repository is itself the canonical visual reference for downstream applications. Structural tests can prove that classes, tokens, and markup contracts exist, but they cannot detect unintended visual drift in layout, spacing, borders, typography, responsive composition, or selection presentation.

Visual baselines must be reproducible enough for CI, cover both desktop and narrow/mobile viewports, and must not introduce a runtime dependency into the design system.

## Decision

Use the Python Playwright package with a pinned version and its matching Chromium build as the canonical screenshot-rendering environment for visual regression tests.

A repository script starts a local static HTTP server, opens canonical demo pages in fixed viewports, waits for document fonts/readiness, captures screenshots, and compares them with reviewed PNG baselines under `tests/visual/baselines/`.

The canonical comparison environment is Linux CI. Failed comparisons retain actual and diff images as workflow artifacts. Intentional UI changes update baselines explicitly and review the resulting binary changes together with the implementation.

Playwright and image-comparison dependencies are development/CI dependencies only. They do not change ADR-0001: consuming applications still use the plain browser-native runtime from `src/` without a package manager or build step.

## Considered alternatives

- Continue with manual screenshot review only.
- Use DOM/CSS structural assertions as a proxy for visual output.
- Add a JavaScript test runner and package-manager-based project toolchain.
- Use a hosted third-party visual-testing service.

## Consequences

### Positive

- Detects visual drift that structural tests cannot see.
- Browser and rendering-engine versions can be pinned together.
- Works against the same static demo files users and coding agents inspect.
- Keeps verification tooling separate from the framework-independent runtime.
- Failure artifacts make visual changes inspectable without reproducing the run locally.

### Negative / trade-offs

- CI becomes slower because Chromium must be installed.
- Screenshot baselines are binary files and intentional changes require explicit review/update.
- Cross-platform local rendering can differ from the canonical Linux CI baseline because of font rasterization and system graphics differences.
- Visual regression does not prove accessibility or behavioral correctness; those concerns still require separate evidence.

## Evidence / notes

This decision implements issue #5 after the core dialog and accessibility/keyboard milestones were completed. The pinned Playwright release is part of the verification contract and should be upgraded deliberately with regenerated/reviewed baselines when its Chromium build changes.
