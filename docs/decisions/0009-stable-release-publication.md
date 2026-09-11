# ADR-0009: Publish 1.0+ as stable GitHub Releases while retaining tagged vendoring

- Status: Accepted
- Date: 2026-09-11
- Related OpenSpec change: `openspec/changes/release-1.0.0/`
- Related issue: #32
- Supersedes: none
- Superseded by: none

## Context

The existing release workflow was designed for the pre-1.0 line and always passed `--prerelease` to GitHub Release publication. That behavior is correct for `v0.x.y`, but it would incorrectly mark `v1.0.0` as a prerelease even after the project deliberately accepts the normal Semantic Versioning stability commitment defined by the public-contract specification.

At the same time, reaching 1.0 does not create a demonstrated need for npm or another package registry. The current runtime remains static browser assets, the focused deterministic ZIP/checksum is already auditable, and direct vendoring from immutable tags remains sufficient for the documented consumer model.

## Decision

Keep one tag-triggered release workflow and choose GitHub publication state from the version line:

- `v0.*` tags continue to publish GitHub prereleases;
- `v1.0.0` and later stable-line tags publish normal GitHub Releases without prerelease status;
- every tag still passes the same tag/version, `main` ancestry, structural/docs, visual, interaction, accessibility-semantic, representative framework-recipe, and deterministic archive gates before publication.

Retain immutable tagged vendoring plus the deterministic focused ZIP/checksum as the primary distribution model at 1.0. Do not introduce npm/registry publication solely because the project reaches 1.0. A future registry path still requires a concrete consumer need and a separate accepted decision.

## Considered alternatives

- Keep `--prerelease` for `v1.0.0`. Rejected because it conflicts with the deliberate stable 1.0 compatibility commitment.
- Create a second independent stable-release workflow. Rejected because it would duplicate verification logic and increase drift risk.
- Publish npm at 1.0 and make it the primary distribution path. Rejected because no current runtime or consumer requirement justifies the additional supported distribution surface.
- Remove focused ZIP/checksum publication and rely only on GitHub source archives. Rejected because the focused deterministic artifact is already part of the accepted consumer/release contract.

## Consequences

### Positive

- GitHub release state matches the Semantic Version stability line.
- Pre-1.0 behavior remains unchanged for historical/future `v0.*` tags.
- One verification path continues to protect every release.
- Consumers keep an immutable, framework-independent, package-manager-free distribution path.
- 1.0 does not accidentally add registry/toolchain requirements.

### Negative / trade-offs

- The release workflow now contains a small version-line conditional that must remain covered by structural tests.
- Direct vendoring still lacks automatic package-manager upgrade metadata; that trade-off remains intentional until a concrete need justifies another distribution surface.

## Evidence / notes

`v0.9.0` was published from `410923e41e89e9ee6d899dc2e392b2f05320b57e` by Release workflow `34554424624`, which passed all established gates and produced focused ZIP SHA-256 `3bdcf9119675514a7210839d3fb9f800be0c356c0293c9795804f2e448c2ef28`. The 1.0 release branch changes publication state, not the browser runtime/public inventory.
