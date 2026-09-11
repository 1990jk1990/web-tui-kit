# Release 0.9.0

Status: Completed preparation
Related issue: #30
Change class: Class 3 — release/version/distribution operation

## Motivation

The public-contract and 1.0-readiness audit is complete on `main` after PR #29. The repository now has an explicit supported browser-native surface, structural drift protection, a compatibility/deprecation policy, and evidence-based 1.0 exit criteria. Those completed changes need an immutable pre-1.0 release identity before the project evaluates whether it is ready to make the stronger `1.0.0` stability commitment.

## Accepted release state

- Canonical repository `VERSION` is `0.9.0`.
- Completed public-contract/readiness entries are recorded under the dated `0.9.0` changelog heading.
- Current consumer, coding-agent, framework-integration, getting-started, examples, security, maturity, and release-maintainer guidance point to or describe the `v0.9.0` line consistently.
- `docs/project/public-contract.md` remains part of the deterministic focused archive and the declared token/class/state/data-attribute/event surface remains protected by structural regression tests.
- The accepted evidence boundary remains explicit: browser/mobile/accessibility/framework automation is regression evidence, not physical Android, assistive-technology/WCAG, registry, maintained-adapter, or exhaustive framework-version certification.
- The tag-triggered prerelease workflow continues to require structural/docs, Chromium visual, Chromium/Firefox interaction, Chromium/Firefox accessibility-semantic, representative framework-recipe, and deterministic archive gates before publication.

## Boundaries

This release preparation introduces no new runtime/component behavior beyond the already-merged v0.9 audit result. It does not add registry publication, framework adapters, physical Android certification, assistive-technology/WCAG certification, or an exhaustive framework-version claim.

Publication remains a prerelease because `0.9.0` is still pre-1.0. The actual immutable Git tag is created only after this preparation PR is merged to `main`.

## Verification

Final pre-archive PR head `1129d2147b0da6cf6c80e8032d1e03e4f4b32cb3` passed:

- AI-DOC-1/project tests/docs workflow `34553265468`; 52 project tests passed, including the deterministic release-builder/archive checks against `VERSION=0.9.0`, public-contract inventory protection, and strict documentation build.
- Chromium visual regression workflow `34553265507` with canonical baselines unchanged.
- Chromium/Firefox browser interaction regression workflow `34553265427`.
- Chromium/Firefox accessibility-semantic regression workflow `34553265421`.
- Representative React/Vue/server-rendered framework recipe regression workflow `34553265451`.
- The complete release-preparation diff was reviewed before archival; changes are limited to release identity, changelog/current-version references, release documentation, and this focused OpenSpec release record.

## Operational follow-up

After this preparation PR is merged, create immutable annotated tag `v0.9.0` on the resulting `main` commit. The Release workflow must pass every gate before publishing the focused ZIP/checksum assets. Verify the tag/release identity and SHA-256 asset, update issue #30 and roadmap #10 with final publication evidence, and only then evaluate the accepted 1.0 exit criteria.
