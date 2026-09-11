# Release 0.7.0

Status: Completed preparation
Related issue: #22
Change class: Class 3 — release/operational

## Motivation

The accessibility-semantics verification milestone is merged on `main` as `7e48eed48cc1b70bc717c989167a30a0c50b4be7`. This change prepares that accepted capability for publication as immutable prerelease `v0.7.0` using the established deterministic release process.

## Accepted release state

- Canonical repository `VERSION` is `0.7.0`.
- Completed accessibility-semantic changelog entries are recorded under the dated `0.7.0` release heading.
- Current consumer/coding-agent/framework integration references point to immutable `v0.7.0`.
- Project maturity, getting-started, release-maintainer, and security-support wording are reconciled for the new release.
- The accepted evidence boundary remains explicit: automated browser role/name/native-state verification is useful regression evidence, not WCAG conformance, screen-reader/assistive-technology certification, or physical Android accessibility-service verification.
- The existing deterministic focused archive remains the distribution artifact, and the tag-triggered prerelease workflow includes structural/docs, visual, cross-browser interaction, accessibility-semantic, and deterministic archive gates before publication.

## Boundaries

This release preparation adds no new runtime behavior, visual redesign, framework adapter, package registry, browser claim, physical-device claim, or assistive-technology claim beyond the accepted v0.7 feature work.

## Verification

- Structural/project tests passed, including deterministic release archive validation against `VERSION=0.7.0`.
- AI-DOC-1 structural validation and strict MkDocs documentation build passed in CI.
- All canonical Chromium visual regression baselines passed unchanged.
- Chromium desktop, narrow touch-capable Chromium, and Firefox desktop interaction regression passed.
- Chromium desktop/package-dialog, narrow touch-capable Chromium package, and Firefox desktop accessibility semantic regression passed.
- The complete release-preparation diff was reviewed before archival; only intended release identity/documentation/OpenSpec files changed.

## Operational follow-up

After this preparation PR is merged, create immutable tag `v0.7.0` on the resulting `main` commit. The Release workflow must then pass and publish the focused ZIP/checksum assets. Verify the checksum and release identity, then update issue #22 and roadmap #10 with the final publication evidence.
