# Release 0.7.0

Status: Active
Related issue: #22
Change class: Class 3 — release/operational

## Motivation

The accessibility-semantics verification milestone is merged on `main` as `7e48eed48cc1b70bc717c989167a30a0c50b4be7`. This change prepares that accepted capability for publication as immutable prerelease `v0.7.0` using the established deterministic release process.

## Proposed release state

- Set canonical repository `VERSION` to `0.7.0`.
- Move completed accessibility-semantic changelog entries into a dated `0.7.0` release heading.
- Point current consumer/coding-agent/framework integration references to immutable `v0.7.0`.
- Reconcile project maturity, getting-started, release-maintainer, and security-support wording for the new release.
- Preserve the accepted evidence boundary: automated browser role/name/native-state verification is useful regression evidence, not WCAG conformance, screen-reader/assistive-technology certification, or physical Android accessibility-service verification.
- Keep the existing deterministic focused archive as the distribution artifact and the tag-triggered prerelease workflow with structural/docs, visual, cross-browser interaction, accessibility-semantic, and deterministic archive gates before publication.

## Boundaries

This release preparation adds no new runtime behavior, visual redesign, framework adapter, package registry, browser claim, physical-device claim, or assistive-technology claim beyond the accepted v0.7 feature work.

## Acceptance criteria

- `VERSION` and current release references consistently identify `0.7.0` / `v0.7.0`.
- The changelog contains a dated `0.7.0` accessibility-semantics release section and leaves `Unreleased` ready for later work.
- Security support wording identifies `v0.7.0` as the maintained pre-1.0 line after publication.
- Consumer and coding-agent references use the immutable release tag rather than `main`.
- Structural tests, AI-DOC-1 validation, strict MkDocs build, canonical Chromium visual regression, Chromium/Firefox interaction regression, Chromium/Firefox accessibility semantic regression, and deterministic release build succeed.
- The complete release-preparation diff is reviewed and the change is archived before merge.

## Operational follow-up

After this preparation PR is merged, create immutable tag `v0.7.0` on the resulting `main` commit. The Release workflow must then pass and publish the focused ZIP/checksum assets. Verify the checksum and release identity, then update issue #22 and roadmap #10 with the final publication evidence.
