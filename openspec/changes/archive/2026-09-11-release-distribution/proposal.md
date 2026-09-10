# Release and distribution preparation

Status: Completed (repository preparation); post-merge publication tracked by #3
Related issue: #3
Related pull request: #14
Change class: Class 2 — release/distribution architecture

## Motivation

The design system now has reusable core dialog patterns, accessibility/keyboard safeguards, and automated visual regression coverage. The next step is to make a specific, reproducible pre-1.0 version consumable by other projects without changing the framework-independent runtime baseline.

## Delivered behavior

- Adopted Semantic Versioning for tagged releases, using `vMAJOR.MINOR.PATCH` Git tags and a plain `MAJOR.MINOR.PATCH` version file.
- Prepared `v0.4.0` as the first tagged project release.
- Kept direct vendoring of the versioned `src/` files as the primary consumption path.
- Added a deterministic focused release ZIP containing the runtime files plus the practical usage/reference documents needed by downstream consumers, with a SHA-256 checksum.
- Added tag-triggered GitHub Actions publication that verifies tag/version identity, main ancestry, structural tests, documentation, visual baselines, and deterministic release artifacts before publishing a GitHub prerelease.
- Did not introduce npm/package-registry publishing in v0.4.0 because the runtime has no package-manager requirement and direct tagged vendoring satisfies the target consumption model.
- Documented compatibility evidence separately from compatibility claims. Automated Linux Chromium and touch-capable mobile-Chromium emulation count as current evidence; physical Android and broader browser/device checks remain explicitly unverified.
- Defined the maintainer procedure for version bumps, changelog preparation, tagging, release verification, and fix-forward handling of a bad pre-1.0 release.
- Defined a pre-1.0 security-support policy and release-integrity guidance.

## Compatibility and boundaries

Release tooling may use Python, GitHub Actions, the GitHub CLI, Playwright, and other repository-development dependencies. None of those tools become dependencies of the browser runtime delivered under `src/`.

This milestone does not promise a stable v1.0 API, npm publication, framework adapters, or physical-device certification.

## Verification

Pull request #14 ran the repository's structural/documentation workflow and visual-regression workflow successfully before archival. The complete branch diff was inspected after the release builder was corrected to support output directories outside the repository and the tag trigger was simplified to a reliable glob plus the strict `VERSION` equality gate.

The actual `v0.4.0` tag and GitHub prerelease are intentionally post-merge operational steps. They remain tracked by issue #3 and must follow `RELEASING.md`; this archive does not claim that publication has already happened.

## Acceptance criteria status

- Canonical version source reports `0.4.0`: complete.
- Release/versioning policy and release procedure: complete.
- Deterministic runtime ZIP and checksum validated by tests: complete.
- Tag-triggered verification/publication workflow: complete; real tag execution pending post-merge.
- Direct vendoring from immutable tags documented as the primary distribution path: complete.
- Compatibility evidence documented without overstating mobile emulation: complete.
- OpenSpec, architecture, changelog, README, contributor/security guidance, tests, and project docs reconciled: complete.
- PR CI passes before merge/tag: complete for the archived branch state; final CI reruns after archival must also remain green.
