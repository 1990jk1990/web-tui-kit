# Release and distribution preparation

Status: Active
Related issue: #3
Change class: Class 2 — release/distribution architecture

## Motivation

The design system now has reusable core dialog patterns, accessibility/keyboard safeguards, and automated visual regression coverage. The next step is to make a specific, reproducible pre-1.0 version consumable by other projects without changing the framework-independent runtime baseline.

## Proposed behavior

- Adopt Semantic Versioning for tagged releases, using `vMAJOR.MINOR.PATCH` Git tags and a plain `MAJOR.MINOR.PATCH` version file.
- Prepare `v0.4.0` as the first tagged project release.
- Keep direct vendoring of the versioned `src/` files as the primary consumption path.
- Produce a deterministic release ZIP containing the runtime files plus the practical usage/reference documents needed by downstream consumers.
- Publish release artifacts from a tag-triggered GitHub Actions workflow only after structural, documentation, and visual checks pass.
- Do not introduce npm/package-registry publishing in v0.4.0 because the runtime has no package-manager requirement and direct tagged vendoring already satisfies the target consumption model.
- Document compatibility evidence separately from compatibility claims. Automated Linux Chromium and touch-capable mobile-Chromium emulation count as current evidence; physical Android and broader browser/device checks must be identified honestly when not automated.
- Define the maintainer procedure for version bumps, changelog preparation, tagging, release verification, and rollback/replacement of a bad pre-1.0 release.

## Compatibility and boundaries

Release tooling may use Python, GitHub Actions, the GitHub CLI, Playwright, and other repository-development dependencies. None of those tools become dependencies of the browser runtime delivered under `src/`.

This milestone does not promise a stable v1.0 API, npm publication, framework adapters, or physical-device certification.

## Acceptance criteria

- A canonical version source exists and reports `0.4.0` for the first release.
- Release/versioning policy and release procedure are documented.
- A deterministic runtime ZIP can be built locally and validated by tests.
- Tag-triggered CI verifies the repository and publishes the versioned ZIP plus checksums to a GitHub Release.
- Direct vendoring from a tag remains the documented primary distribution path.
- Compatibility evidence is documented without overstating mobile emulation as physical Android testing.
- OpenSpec, architecture, changelog, README, contributor guidance, tests, and relevant project docs are reconciled.
- PR CI passes before the release change is merged and tagged.
