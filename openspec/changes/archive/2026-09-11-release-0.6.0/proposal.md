# Release 0.6.0

Status: Completed preparation
Related issue: #17
Change class: Class 3 — release/operational

## Motivation

The browser-interaction and compatibility-verification milestone is merged on `main` as `f704d5349a1dd0d253b279a25b929aaaa8d854fd`. This change prepares that accepted verification capability for publication as immutable prerelease `v0.6.0` using the established deterministic release process.

## Accepted release state

- Canonical repository `VERSION` is `0.6.0`.
- Completed browser-verification changelog entries are recorded under the dated `0.6.0` release heading.
- Current consumer/coding-agent references point to immutable `v0.6.0`; historical older-version references remain only where they describe prior release history.
- Project maturity, getting-started, framework-integration, release-maintainer, and security-support wording are reconciled for the new release.
- Physical Android Chrome/WebView remains explicitly unverified; `v0.6.0` publishes automated Chromium/Firefox/touch evidence, not a new device-certification claim.
- The existing deterministic focused archive remains the distribution artifact, and the tag-triggered prerelease workflow now includes browser-interaction verification before publication.

## Boundaries

This release preparation adds no runtime behavior, visual redesign, framework adapter, package registry, physical Android certification, or browser claim beyond evidence already accepted in the merged v0.6 verification feature.

## Verification

- Structural/project tests passed, including deterministic release archive validation against `VERSION=0.6.0`.
- AI-DOC-1 structural validation and strict MkDocs documentation build passed in CI.
- Canonical Chromium visual regression passed unchanged.
- Chromium desktop, narrow touch-capable Chromium, and Firefox desktop interaction regression passed.
- The complete release-preparation diff was reviewed before archival.

## Operational follow-up

After this preparation PR is merged, repository owner action remains: create immutable tag `v0.6.0` on the resulting `main` commit. The Release workflow must then pass and publish the focused ZIP/checksum assets. Verify the checksum and release identity, update issues #17 and #10 as appropriate, and close #17 only after publication succeeds.
