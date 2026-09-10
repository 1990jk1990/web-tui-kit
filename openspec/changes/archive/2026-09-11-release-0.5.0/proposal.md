# Release 0.5.0

Status: Completed preparation
Related issue: #7
Change class: Class 3 — release/operational

## Motivation

The framework/template integration feature set is merged on `main` and the first pre-1.0 release process established by `v0.4.0` is proven. This change prepares those accepted integration recipes and documentation for publication as immutable prerelease `v0.5.0` without changing the browser-native runtime contract.

## Accepted release state

- Canonical repository `VERSION` is `0.5.0`.
- Framework/template integration changes are recorded under the dated `0.5.0` changelog heading.
- Current consumer/coding-agent references point to immutable `v0.5.0`; historical `v0.4.0` references remain only where they describe prior release history or examples deliberately tied to that release.
- Security support wording reflects that tagged pre-1.0 releases are active and only the latest published pre-1.0 line plus active development are expected to receive fixes.
- The existing deterministic release archive includes the accepted framework/template integration guide and recipes.
- The existing tag-triggered release workflow, compatibility evidence, and fix-forward policy remain unchanged.

## Boundaries

This preparation adds no application behavior, visual style, package registry, framework runtime dependency, or new compatibility claim. React/Vue/server-rendered material remains optional consumption guidance over the same canonical `src/` runtime.

## Verification

- Structural/project tests passed, including deterministic release archive validation against `VERSION=0.5.0`.
- AI-DOC-1 structural validation passed.
- Strict MkDocs documentation build passed.
- Existing desktop/mobile visual regression baselines passed unchanged.
- The complete release-preparation diff was reviewed before archival.

## Operational follow-up

After this preparation PR is merged, repository owner action remains: create immutable tag `v0.5.0` on the resulting `main` commit. The existing Release workflow must then pass and publish the focused ZIP/checksum assets. Issue #7 remains open until that publication and checksum verification are complete.
