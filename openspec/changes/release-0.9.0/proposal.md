# Release v0.9.0

Status: Active
Related issue: #30
Change class: Class 3 — release/version/distribution operation

## Motivation

The public-contract and 1.0-readiness audit is complete on `main` after PR #29. The repository now has an explicit supported browser-native surface, structural drift protection, a compatibility/deprecation policy, and evidence-based 1.0 exit criteria. Those completed changes need an immutable pre-1.0 release identity before the project evaluates whether it is ready to make the stronger `1.0.0` stability commitment.

## Proposed change

- Set repository release identity to `0.9.0` and finalize the dated changelog section.
- Point current downstream/coding-agent/framework guidance at immutable tag `v0.9.0`.
- Reconcile project maturity, security-supported-version wording, and maintainer release guidance for the v0.9 line.
- Preserve the public-contract guide in the focused deterministic archive.
- Verify the current structural/docs, visual, interaction, accessibility-semantic, representative framework-recipe, public-contract, and deterministic archive gates before merge and again through the tag-triggered Release workflow.
- Publish `v0.9.0` as the final planned prerelease for this audit milestone, then evaluate the already-accepted 1.0 exit criteria separately.

## Boundaries

This release preparation introduces no new runtime/component behavior beyond the already-merged v0.9 audit result. It does not add registry publication, framework adapters, physical Android certification, assistive-technology/WCAG certification, or an exhaustive framework-version claim.

The actual immutable Git tag is created only after the release-preparation PR is merged to `main`. Publication remains a prerelease because `0.9.0` is still pre-1.0.

## Verification plan

- Run project tests including public-contract and release-archive guards.
- Run AI-DOC-1 validation and strict MkDocs build.
- Run canonical Chromium visual regression.
- Run Chromium/Firefox interaction and accessibility-semantic verification.
- Run representative React/Vue/server-rendered recipe verification.
- Build the deterministic focused archive for `v0.9.0` with `--check` and confirm `docs/project/public-contract.md` is included.
- Inspect the complete release-preparation diff and archive this OpenSpec change before merge.

## Expected outcome

A green release-preparation commit on `main` can be tagged immutably as `v0.9.0`; tag-triggered automation publishes the focused ZIP and SHA-256 checksum as a GitHub prerelease. Once publication evidence is verified, the project can evaluate the accepted 1.0 exit criteria with a stable v0.9 reference point.
