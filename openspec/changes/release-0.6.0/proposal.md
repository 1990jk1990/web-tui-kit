# Release 0.6.0

Status: Active
Related issue: #17
Change class: Class 3 — release/operational

## Motivation

The browser-interaction and compatibility-verification milestone is merged on `main` as `f704d5349a1dd0d253b279a25b929aaaa8d854fd`. The next step is to publish that accepted verification capability as immutable prerelease `v0.6.0` using the established deterministic release process.

## Proposed release state

- Set canonical repository `VERSION` to `0.6.0`.
- Move the completed browser-verification changelog entries into a dated `0.6.0` release section.
- Update current consumer/coding-agent references from `v0.5.0` to `v0.6.0` where they identify the recommended current release.
- Reconcile project maturity, framework integration, security-support wording, compatibility evidence, and release-maintainer examples for the new release.
- Keep physical Android Chrome/WebView explicitly unverified; `v0.6.0` publishes the automated Chromium/Firefox/touch evidence, not a new device claim.
- Use the existing deterministic release archive and tag-triggered prerelease workflow, now including the browser interaction gate before artifact publication.
- After merge, create immutable tag `v0.6.0` on the resulting `main` commit and verify the generated ZIP/checksum assets.

## Boundaries

This release preparation adds no runtime behavior, visual redesign, framework adapter, package registry, physical Android certification, or new browser claim beyond evidence already accepted in the merged v0.6 verification feature.

## Acceptance criteria

- `VERSION` is exactly `0.6.0`.
- Changelog/current-release references consistently describe `0.6.0`.
- Current recommended immutable consumer/coding-agent tag references point to `v0.6.0`.
- Security wording identifies `v0.6.0` as the next maintained pre-1.0 line after publication and no longer contains stale pre-v0.5 transition text.
- Compatibility documentation accurately describes the automated Chromium/Firefox/touch evidence and physical Android remains unverified.
- Structural tests, AI-DOC-1 validation, strict docs build, Chromium visual regression, Chromium/Firefox interaction regression, and deterministic release archive validation pass before merge.
- The active OpenSpec release change is archived before the PR is ready for merge.
- After merge, immutable `v0.6.0` is tagged, the Release workflow succeeds, ZIP/checksum assets are verified, and issue #17 can be closed.
