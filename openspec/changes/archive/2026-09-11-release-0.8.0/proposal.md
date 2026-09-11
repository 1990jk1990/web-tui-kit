# Release 0.8.0

Status: Completed preparation
Related issue: #26
Change class: Class 3 — release/operational

## Motivation

The executable framework-recipe verification milestone is merged on `main` as `9391877671cf861e84ddcbe33994f33fde1b6152`. This change prepares that accepted capability for publication as immutable prerelease `v0.8.0` using the established deterministic release process.

## Accepted release state

- Canonical repository `VERSION` is `0.8.0`.
- Completed executable framework-recipe verification entries are recorded under the dated `0.8.0` release heading.
- Current consumer, coding-agent, and framework-integration references point to immutable `v0.8.0`.
- Project maturity, getting-started, release-maintainer, and security-support wording are reconciled for the new release.
- The accepted evidence boundary remains explicit: pinned React/Vue/compiler/bundler versions are representative compile/runtime evidence, not an exhaustive support matrix; browser semantic/touch evidence still does not establish WCAG, real assistive-technology, or physical Android certification.
- The deterministic focused archive remains the distribution artifact, and the tag-triggered prerelease workflow includes structural/docs, visual, cross-browser interaction, accessibility-semantic, representative framework-recipe, and deterministic archive gates before publication.
- Development-only Node/framework/compiler/bundler dependencies and generated verification fixtures remain outside the focused runtime archive and downstream requirements.

## Boundaries

This release preparation adds no new runtime behavior, visual redesign, framework adapter, package-registry distribution, browser support claim, physical-device claim, or assistive-technology claim beyond the accepted v0.8 feature work.

## Verification

Final pre-archive PR head `97592ec2758d858aa861e67bc90f08f93ed37f18` passed:

- AI-DOC-1/project tests/docs workflow `34550710382`, including deterministic release archive validation against `VERSION=0.8.0`.
- Chromium visual regression workflow `34550710384` with canonical baselines unchanged.
- Chromium/Firefox browser interaction regression workflow `34550710411`, including the representative narrow touch-capable Chromium case.
- Chromium/Firefox accessibility-semantic regression workflow `34550710424`, including the representative narrow touch-capable Chromium package case.
- Executable React/Vue/server-rendered framework recipe regression workflow `34550710386` with the exact pinned representative verification versions.
- The complete release-preparation diff was reviewed before archival; only intended release identity, documentation, OpenSpec, and stable-reference files changed.

## Operational follow-up

After this preparation PR is merged, create immutable tag `v0.8.0` on the resulting `main` commit. The Release workflow must pass every gate before publishing the focused ZIP/checksum assets. Verify checksum and release identity, then update issue #26 and roadmap #10 with final publication evidence.
