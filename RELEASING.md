# Releasing web-tui-kit

This document is the maintainer procedure for tagged pre-1.0 releases.

## Versioning policy

`web-tui-kit` uses Semantic Versioning (`MAJOR.MINOR.PATCH`). The canonical plain version is stored in `VERSION`; Git tags use the same value with a `v` prefix, for example `VERSION=0.6.0` and tag `v0.6.0`.

Before `1.0.0`, compatibility is still evolving:

- increment **PATCH** for compatible fixes/refinements that do not intentionally change documented public component contracts,
- increment **MINOR** for new components, new supported behavior, or intentional breaking changes to the pre-1.0 public contract,
- reserve **MAJOR 1** for the point where the project declares the documented public UI contract stable enough for normal Semantic Versioning compatibility expectations.

A release tag is immutable. Never move an existing published tag to a different commit. If a release is bad, fix forward with a new version. A GitHub Release may be marked withdrawn in its notes, but the original tag/artifacts should remain available for auditability unless there is a security/legal reason requiring removal.

## Release contents

The canonical focused distribution is built by:

```bash
python scripts/build_release.py --version "v$(cat VERSION)" --check
```

The command verifies that the expected tag version matches `VERSION`, builds a deterministic ZIP under `dist/`, validates its exact file list/timestamps, builds the ZIP twice when `--check` is supplied, and writes a matching SHA-256 checksum file.

The focused archive contains the runtime under `src/`, executable demos, copy-ready framework/template recipes under `examples/`, the framework-integration guide, `VERSION`, `README.md`, `DESIGN_SYSTEM.md`, `AGENTS.md`, `CHANGELOG.md`, and `SECURITY.md`. GitHub also provides its normal source archives for the complete repository.

## Pre-release checklist

1. Start from current `main` and create a focused release-preparation branch.
2. Decide the next Semantic Version and update `VERSION`.
3. Move completed user-visible entries in `CHANGELOG.md` from `Unreleased` into the dated release heading.
4. Reconcile OpenSpec, architecture/ADRs, README, contributor/release docs, compatibility evidence, and any consumer integration references included in the focused archive.
5. Run:

```bash
python -m unittest discover -s tests -v
python scripts/validate_ai_doc_1.py
pip install -r requirements-docs.txt
python scripts/sync_openspec_docs.py
mkdocs build --strict
pip install -r requirements-visual.txt
python -m playwright install --with-deps chromium firefox
python scripts/visual_regression.py
python scripts/interaction_regression.py
python scripts/accessibility_regression.py
python scripts/build_release.py --version "v$(cat VERSION)" --check
```

6. Review the complete diff and confirm there are no secrets, generated `site/`, `dist/`, or `test-results/` directories committed.
7. Merge the release-preparation PR only after required CI is green.
8. Create the immutable tag `v$(cat VERSION)` on the resulting `main` commit.

## Tag-triggered release automation

Pushing a matching `vMAJOR.MINOR.PATCH` tag starts `.github/workflows/release.yml`. The workflow:

1. verifies the tag exactly matches `VERSION`,
2. verifies the tagged commit is contained in `main`,
3. runs project tests, AI-DOC-1 validation, and strict documentation build,
4. runs the pinned Chromium visual-regression suite,
5. runs the pinned Chromium/Firefox browser-interaction suite, including the narrow touch-capable Chromium case,
6. runs the pinned Chromium/Firefox accessibility-semantic suite, including the narrow touch-capable Chromium package case,
7. builds and validates the deterministic distribution ZIP/checksum,
8. creates a GitHub **prerelease** and uploads the focused ZIP and SHA-256 checksum.

The accessibility gate is browser semantic regression evidence only; it is not a WCAG conformance or screen-reader certification step.

The release job uses repository `contents: write` only for GitHub Release publication. Runtime consumers do not depend on GitHub Actions, Python, Playwright, Chromium, Firefox, or any other release tooling. Framework/template examples in the archive remain optional consumption references and do not make those frameworks runtime dependencies.

## Verification after tagging

Confirm that the tag workflow completed successfully, the GitHub Release points to the intended tag/commit, the ZIP and `.sha256` files are attached, and the checksum matches the downloaded ZIP. Confirm the focused archive contains the documented runtime/reference allowlist, including integration recipes when they are part of accepted behavior. Then verify README/version references still point consumers at immutable tags rather than the moving `main` branch.

## Distribution policy

Direct vendoring from an immutable tag is the primary distribution method for pre-1.0 releases. Do not add an npm or other registry publication path merely for convenience; a new distribution surface requires a concrete consumer need and a deliberate follow-up decision.
