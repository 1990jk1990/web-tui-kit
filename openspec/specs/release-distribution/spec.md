# Release and distribution specification

## Purpose

This specification defines the accepted pre-1.0 release identity, distribution, and compatibility-evidence contract for `web-tui-kit`.

## Requirements

### Requirement: Semantic release identity

The project MUST use a plain `MAJOR.MINOR.PATCH` value in the repository-root `VERSION` file and MUST use an immutable `vMAJOR.MINOR.PATCH` Git tag for each corresponding release.

Before `1.0.0`, compatible fixes SHOULD increment PATCH, while new public components/behavior or intentional breaking changes to the evolving pre-1.0 public contract SHOULD increment MINOR.

#### Scenario: Tag/version match

- **GIVEN** a release tag is `v0.4.0`
- **WHEN** release automation reads `VERSION`
- **THEN** the file MUST contain exactly `0.4.0` or the release MUST fail

### Requirement: Tagged vendoring is the primary distribution path

Pre-1.0 consumers MUST be able to use the project without npm, another package registry, or a build step by copying the runtime from an immutable release tag.

Documentation MUST recommend pinning a tag/version rather than copying from the moving `main` branch for reproducible downstream use.

#### Scenario: Direct consumer vendoring

- **GIVEN** a consuming application wants the released UI kit
- **WHEN** it selects an immutable release tag
- **THEN** it MUST be able to copy `src/tokens.css`, `src/tui.css`, and optionally `src/tui.js` without installing repository development tooling

### Requirement: Focused deterministic release archive

Each tagged release MUST be able to produce a focused `web-tui-kit-MAJOR.MINOR.PATCH.zip` and matching SHA-256 checksum. The ZIP MUST contain the documented runtime/reference file set under one versioned top-level directory and MUST use deterministic member ordering/timestamps so repeated builds from the same commit produce identical ZIP bytes.

#### Scenario: Consecutive release builds

- **GIVEN** unchanged repository content and the same `VERSION`
- **WHEN** the release builder runs twice
- **THEN** both ZIP files MUST have the same SHA-256 digest

#### Scenario: Archive version identity

- **GIVEN** the release builder creates `web-tui-kit-0.4.0.zip`
- **WHEN** its embedded `VERSION` is inspected
- **THEN** it MUST also contain `0.4.0`

### Requirement: Focused archive includes consumer integration references

When the repository provides accepted consumer integration recipes/guidance, the focused release archive MUST include those copy-ready references alongside the canonical runtime so downstream consumers and coding agents do not need the full development repository merely to understand framework/template consumption.

The integration references MUST remain examples/guidance and MUST NOT turn framework dependencies into runtime dependencies of the released `src/` assets.

#### Scenario: Framework consumer downloads focused archive

- **GIVEN** a tagged release includes the accepted React, Vue, and server-rendered recipes
- **WHEN** a consumer downloads the focused release ZIP
- **THEN** the archive MUST contain the framework-integration guide and those recipes in addition to the canonical runtime assets

### Requirement: Verified tag-triggered publication

A matching version tag MUST trigger release automation. Before publishing artifacts, the workflow MUST verify that the tag matches `VERSION`, that the tagged commit is contained in `main`, and that structural tests, AI-DOC-1 validation, documentation build, visual regression, and release-archive validation succeed.

The release workflow MAY use repository write permission only for release publication after verification.

#### Scenario: Tag points outside main

- **GIVEN** a matching-looking release tag points to a commit not contained in `main`
- **WHEN** release automation runs
- **THEN** publication MUST fail before creating the GitHub Release

#### Scenario: Verification failure

- **GIVEN** any mandatory release check fails
- **WHEN** the tag workflow runs
- **THEN** it MUST NOT publish the focused release artifacts

### Requirement: GitHub prerelease publication

Pre-1.0 tag automation MUST publish the focused ZIP and checksum as assets of a GitHub prerelease associated with the immutable tag.

#### Scenario: Successful pre-1.0 tag

- **GIVEN** a valid `v0.x.y` tag on `main` passes all release checks
- **WHEN** publication runs
- **THEN** a GitHub prerelease MUST be created for that tag with the ZIP and checksum attached

### Requirement: Registry publishing is optional and currently absent

The pre-1.0 distribution contract MUST NOT require npm or another package registry. Adding registry publication later requires a concrete consumer need and a deliberate follow-up decision because it creates another supported distribution surface.

#### Scenario: Consumer uses a pre-1.0 release

- **GIVEN** a consumer wants a tagged pre-1.0 release
- **WHEN** it follows the documented primary installation path
- **THEN** no npm account, Node.js installation, package-manager lockfile, or registry credential MUST be required

### Requirement: Compatibility claims follow evidence

Release documentation MUST distinguish compatibility targets from environments actually exercised by automated or manual evidence.

Automated touch/mobile Chromium emulation MAY support the Android browser design target, but MUST NOT be described as physical Android device certification.

#### Scenario: Mobile compatibility statement

- **GIVEN** release evidence consists of Playwright Chromium with mobile/touch emulation
- **WHEN** Android compatibility is documented
- **THEN** the documentation MUST identify that evidence as representative mobile-Chromium rendering and disclose that physical Android device/WebView verification is separate

### Requirement: Bad releases fix forward

Published version tags SHOULD be treated as immutable. A faulty pre-1.0 release SHOULD be corrected with a new Semantic Version rather than moving the existing tag to another commit.

#### Scenario: Defect found after publication

- **GIVEN** `v0.4.0` has already been published and a defect is discovered
- **WHEN** maintainers prepare the correction
- **THEN** they SHOULD publish a new version such as `v0.4.1` rather than retargeting `v0.4.0`
