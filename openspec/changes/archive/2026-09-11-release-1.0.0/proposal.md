# Release 1.0.0

Status: Completed preparation
Related issue: #32
Change class: Class 3 — release/version/distribution operation

## Motivation

`v0.9.0` completed and published the public-contract/readiness audit. The accepted public inventory is structurally protected, selected pre-1.0 cleanup is complete, every established release gate passed on the published v0.9 tag, the focused archive includes the public-contract guide, and no other focused product/technical gap is open. The remaining 1.0 work is therefore the deliberate stability/release transition rather than another feature cycle.

The pre-1.0 tag workflow always used `--prerelease`; this preparation reconciles publication semantics before `v1.0.0` is tagged.

## Accepted release state

- Canonical repository `VERSION` is `1.0.0`.
- The dated `1.0.0` changelog section records the stable public-contract transition without introducing new runtime behavior.
- Consumer, coding-agent, framework/template, getting-started, maturity, compatibility, security, contributor, architecture, and maintainer guidance consistently describe the stable `v1.0.0` line.
- Starting with 1.0, normal Semantic Versioning applies to the public token/class/state/semantic-markup/data-attribute/event inventory established by the v0.9 audit.
- The public inventory itself is unchanged by the 1.0 version transition; no `src/` file or canonical demo/baseline changes in this release-preparation PR.
- Release automation publishes `v0.*` tags as prereleases and `v1.0.0`/later stable-line tags as normal GitHub Releases after the same mandatory verification gates.
- Immutable tagged vendoring and the deterministic focused ZIP/checksum remain the current primary distribution model; 1.0 does not introduce npm/registry publication.
- Physical Android, real assistive-technology/WCAG, maintained framework-adapter, and broad framework-version evidence boundaries remain explicit.
- ADR-0009 records the stable GitHub Release publication decision.

## Boundaries

This release preparation introduces no visual redesign, new runtime component behavior, new public API names, npm/registry publication, maintained framework adapter package, or unsupported certification claim.

`1.0.0` is the compatibility commitment for the already-audited browser-native public contract. The actual immutable Git tag is created only after this preparation PR is merged to `main`.

## Verification

Pre-archive PR head `78172fcfc16fc71d5dfcf19d04aa8127f5cce336` passed the complete candidate matrix:

- AI-DOC-1/project tests/docs workflow `34555411188`; 53 project tests passed, including the deterministic `VERSION=1.0.0` archive builder, public-contract inventory protection, stable-vs-prerelease publication guard, AI-DOC validation, and strict MkDocs build.
- Chromium visual regression workflow `34555411201` passed against the existing canonical package/dialog desktop and touch-capable baselines.
- Chromium/Firefox browser interaction regression workflow `34555411194` passed.
- Chromium/Firefox accessibility-semantic regression workflow `34555411143` passed.
- Representative React/Vue/server-rendered framework recipe regression workflow `34555411148` passed.
- The complete PR diff was reviewed: changed paths are limited to release automation/identity, specifications/tests, documentation/ADR/OpenSpec, and consumer reference text; there are no changes under `src/`, canonical demos, or visual baselines.
- The deterministic release test confirms the focused archive still includes `docs/project/public-contract.md`, framework integration guidance/recipes, canonical runtime files, and the exact documented allowlist.

## Operational follow-up

After this preparation PR is merged, create immutable annotated tag `v1.0.0` on the resulting `main` commit. The Release workflow must pass every established gate before publishing a **normal stable GitHub Release** with the focused ZIP/checksum assets. Verify tag/release identity and SHA-256, then update/close #32 and canonical roadmap #10.
