# Release 0.5.0

Status: Active
Related issue: #7
Change class: Class 3 — release/operational

## Motivation

The framework/template integration feature set is merged on `main` and the first pre-1.0 release process established by `v0.4.0` is already proven. The next step is to publish those accepted integration recipes and documentation as an immutable `v0.5.0` prerelease without changing the browser-native runtime contract.

## Proposed release state

- Set the canonical repository `VERSION` to `0.5.0`.
- Move the completed framework/template integration changelog entries into a dated `0.5.0` release section.
- Update consumer-facing stable references from `v0.4.0` to `v0.5.0` where they identify the recommended current release.
- Keep `v0.4.0` documentation references when they are explicitly historical examples rather than current installation guidance.
- Reconcile security support wording now that tagged pre-1.0 releases exist.
- Use the existing deterministic release archive, release workflow, compatibility evidence, and fix-forward policy without introducing a new distribution mechanism.
- After merge, create immutable tag `v0.5.0` on the release-preparation merge commit and let the verified tag workflow publish the prerelease assets.

## Boundaries

This release preparation does not add application behavior, new visual styles, package registries, framework runtime dependencies, or new compatibility claims. React/Vue/server-rendered material remains optional consumption guidance over the same canonical `src/` runtime.

## Acceptance criteria

- `VERSION` is exactly `0.5.0`.
- Changelog and current-release references consistently describe `0.5.0`.
- Security policy no longer contains stale pre-`v0.4.0` wording and states the current latest-release support policy accurately.
- Structural tests, AI-DOC-1 validation, strict documentation build, visual regression, and deterministic release archive validation pass before merge.
- The active OpenSpec release change is archived before the PR is made ready for merge.
- After merge, `v0.5.0` is tagged on the resulting `main` commit, the Release workflow succeeds, focused ZIP/checksum assets are verified, and issue #7 can be closed.
