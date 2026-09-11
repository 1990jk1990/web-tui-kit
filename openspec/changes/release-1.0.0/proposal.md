# Release 1.0.0

Status: Active
Related issue: #32
Change class: Class 3 — release/version/distribution operation

## Motivation

`v0.9.0` completed and published the public-contract/readiness audit. The accepted public inventory is structurally protected, selected pre-1.0 cleanup is complete, every established release gate passed on the published v0.9 tag, the focused archive includes the public-contract guide, and no other focused product/technical gap is open. The remaining 1.0 work is therefore the deliberate stability/release transition rather than another feature cycle.

The existing tag workflow still publishes every release with `--prerelease`, so a 1.0 candidate must explicitly reconcile publication semantics before `v1.0.0` is tagged.

## Proposed change

- Set repository release identity to `1.0.0` and prepare the dated 1.0 changelog section.
- Reconcile consumer, coding-agent, framework/template, project maturity, security, compatibility, contributor, architecture, and maintainer guidance around the stable `v1.0.0` public-contract commitment.
- Update release/distribution requirements and automation so `v0.*` tags remain GitHub prereleases while `v1.0.0` and later major lines publish normal GitHub Releases after the same verification gates.
- Preserve immutable tagged vendoring and the deterministic focused ZIP/checksum as the current distribution model; do not add a registry merely because the project reaches 1.0.
- Preserve the exact public token/class/state/semantic-markup/data-attribute/event inventory established in v0.9 unless a separately justified change is discovered.
- Preserve explicit evidence boundaries for physical Android, assistive technology/WCAG, maintained framework adapters, and broad framework-version matrices.

## Boundaries

This release preparation does not introduce a visual redesign, new runtime component behavior, new public API names, npm/registry publication, maintained framework adapter packages, or unsupported certification claims.

`1.0.0` is the compatibility commitment for the already-audited browser-native public contract. The actual immutable Git tag is created only after the release-preparation PR is merged and all candidate gates are green.

## Verification plan

- Run project tests including public-contract and release-publication guards.
- Run AI-DOC-1 validation and strict MkDocs build.
- Run canonical Chromium visual regression.
- Run Chromium/Firefox interaction and accessibility-semantic verification.
- Run representative React/Vue/server-rendered recipe verification.
- Build deterministic focused archive for `v1.0.0` with `--check` and confirm public-contract/consumer references remain included.
- Inspect the complete diff and confirm runtime/public-contract inventory files do not change except documentation/specification semantics required for the stable release.
- Archive this OpenSpec change only after green verification, then merge the release PR.

## Expected outcome

A green release-preparation commit on `main` can be tagged immutably as `v1.0.0`. Tag-triggered automation publishes a normal GitHub Release, not a prerelease, with the deterministic focused ZIP and SHA-256 checksum. Starting with that release, normal Semantic Versioning applies to the declared public contract.
