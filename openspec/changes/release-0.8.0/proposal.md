# Release 0.8.0

Status: Active preparation
Related issue: #26
Change class: Class 3 — release/operational

## Motivation

The executable framework-recipe verification milestone is merged on `main` as `9391877671cf861e84ddcbe33994f33fde1b6152`. This change prepares that accepted capability for publication as immutable prerelease `v0.8.0` using the established deterministic release process.

## Proposed release state

- Set canonical repository `VERSION` to `0.8.0`.
- Move the completed executable framework-recipe verification entries into a dated `0.8.0` changelog section.
- Point current consumer, coding-agent, and framework-integration references at immutable `v0.8.0`.
- Reconcile project maturity, getting-started, release-maintainer, and security-support wording for the new release.
- Preserve the accepted evidence boundary: pinned React/Vue/compiler/bundler versions are representative compile/runtime evidence, not an exhaustive support matrix; browser semantic/touch evidence still does not establish WCAG, real assistive-technology, or physical Android certification.
- Keep the deterministic focused archive as the distribution artifact and require structural/docs, visual, cross-browser interaction, accessibility-semantic, framework-recipe, and deterministic archive gates before publication.

## Boundaries

This release preparation adds no new runtime behavior, visual redesign, framework adapter, package-registry distribution, browser support claim, physical-device claim, or assistive-technology claim beyond the accepted v0.8 feature work.

Development-only Node/framework/compiler/bundler dependencies and generated verification fixtures remain outside the focused runtime archive and downstream requirements.

## Verification plan

- Run structural/project tests and deterministic release archive validation against `VERSION=0.8.0`.
- Run AI-DOC-1 validation and strict MkDocs documentation build.
- Run canonical Chromium visual regression unchanged.
- Run Chromium/Firefox interaction regression, including the representative narrow touch-capable Chromium case.
- Run Chromium/Firefox accessibility-semantic regression, including the representative narrow touch-capable Chromium package case.
- Run executable React/Vue/server-rendered recipe regression with the exact pinned representative verification versions.
- Review the complete release-preparation diff before archival and merge.

## Operational follow-up

After this preparation PR is merged, create immutable tag `v0.8.0` on the resulting `main` commit. The Release workflow must pass every gate before publishing the focused ZIP/checksum assets. Verify checksum and release identity, then update issue #26 and roadmap #10 with final publication evidence.
