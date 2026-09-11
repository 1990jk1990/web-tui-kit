# Releasing web-tui-kit

This document is the maintainer procedure for versioned releases and the compatibility policy that governs the declared public consumer contract.

## Versioning policy

`web-tui-kit` uses Semantic Versioning (`MAJOR.MINOR.PATCH`). The canonical plain version is stored in `VERSION`; Git tags use the same value with a `v` prefix, for example `VERSION=0.9.0` and tag `v0.9.0`.

The supported downstream stability boundary is defined in `openspec/specs/public-contract/spec.md` and inventoried in `docs/project/public-contract.md`. Version classification applies to that declared public surface rather than every visible repository implementation detail.

Before `1.0.0`, compatibility is still evolving:

- increment **PATCH** for compatible fixes/refinements that do not intentionally change documented public component contracts,
- increment **MINOR** for new public components/behavior or intentional breaking changes to the evolving pre-1.0 public contract,
- any intentional pre-1.0 public break must be called out in `CHANGELOG.md` and include migration guidance when an existing consumer pattern must change,
- reserve **MAJOR 1** for the point where the project deliberately declares the documented public UI contract stable enough for normal Semantic Versioning compatibility expectations.

Starting with `1.0.0`:

- **PATCH** releases preserve the declared public contract while delivering compatible fixes,
- **MINOR** releases may add compatible public surface and may deprecate existing surface,
- **MAJOR** releases are required for incompatible removal/rename, required semantic-markup changes, token repurposing, or breaking changes to documented events/data attributes,
- planned public removals should be deprecated with replacement/migration guidance in at least one prior MINOR release before later MAJOR removal, except when an urgent security/legal/standards issue requires faster action.

Changing a public token's literal default value is not automatically a breaking API change when its name and documented semantic purpose remain compatible. Repurposing the token is a contract change.

A release tag is immutable. Never move an existing published tag to a different commit. If a release is bad, fix forward with a new version. A GitHub Release may be marked withdrawn in its notes, but the original tag/artifacts should remain available for auditability unless there is a security/legal reason requiring removal.

## 1.0 readiness gate

Do not choose `1.0.0` merely because the project has reached a particular 0.x number. Before a 1.0 release-preparation branch is opened:

1. the public inventory/stability policy must be accepted and structurally protected;
2. selected pre-1.0 public naming/semantic cleanup from the readiness audit must be complete;
3. the full existing release gates must pass for the candidate contract;
4. README/design/framework/release/changelog documentation must consistently state the 1.0 compatibility commitment;
5. the focused archive must include `docs/project/public-contract.md`;
6. evidence gaps must remain accurately bounded rather than being presented as certifications that were not performed.

Physical Android-device certification, real screen-reader/assistive-technology certification, WCAG certification, registry publication, maintained framework adapters, and an exhaustive framework-version matrix are not current 1.0 prerequisites unless a later accepted requirement deliberately makes one mandatory.

After `v0.9.0` is published and its release evidence is verified, evaluate these criteria directly before creating any `1.0.0` release-preparation branch.

## Release contents

The canonical focused distribution is built by:

```bash
python scripts/build_release.py --version "v$(cat VERSION)" --check
```

The command verifies that the expected tag version matches `VERSION`, builds a deterministic ZIP under `dist/`, validates its exact file list/timestamps, builds the ZIP twice when `--check` is supplied, and writes a matching SHA-256 checksum file.

The focused archive contains the runtime under `src/`, executable demos, copy-ready framework/template recipes under `examples/`, the framework-integration guide, the public-contract guide, `VERSION`, `README.md`, `DESIGN_SYSTEM.md`, `AGENTS.md`, `CHANGELOG.md`, and `SECURITY.md`. GitHub also provides its normal source archives for the complete repository. Development-only framework verification dependencies and generated fixtures are not distribution contents.

## Release-preparation checklist

1. Start from current `main` and create a focused release-preparation branch.
2. Decide the next Semantic Version by evaluating the actual declared public-contract impact, then update `VERSION`.
3. Move completed user-visible entries in `CHANGELOG.md` from `Unreleased` into the dated release heading; include explicit migration notes for any intentional public-contract break/deprecation.
4. Reconcile OpenSpec, `docs/project/public-contract.md`, architecture/ADRs, README, contributor/release docs, compatibility evidence, and any consumer integration references included in the focused archive.
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
npm install --prefix tests/framework --no-package-lock --no-audit --no-fund
python scripts/framework_recipe_regression.py
python scripts/build_release.py --version "v$(cat VERSION)" --check
```

6. Review the complete diff and confirm there are no secrets, generated `site/`, `dist/`, `test-results/`, or `tests/framework/node_modules/` directories committed.
7. Confirm `tests/test_public_contract.py` agrees with the intended public token/class/state/data-attribute/event inventory and that no newly implemented public name is left unclassified.
8. Merge the release-preparation PR only after required CI is green.
9. Create the immutable tag `v$(cat VERSION)` on the resulting `main` commit.

## Tag-triggered release automation

Pushing a matching `vMAJOR.MINOR.PATCH` tag starts `.github/workflows/release.yml`. The workflow:

1. verifies the tag exactly matches `VERSION`,
2. verifies the tagged commit is contained in `main`,
3. runs project tests (including the public-contract structural guard), AI-DOC-1 validation, and strict documentation build,
4. runs the pinned Chromium visual-regression suite,
5. runs the pinned Chromium/Firefox browser-interaction suite, including the narrow touch-capable Chromium case,
6. runs the pinned Chromium/Firefox accessibility-semantic suite, including the narrow touch-capable Chromium package case,
7. installs the private pinned representative framework/tool verification dependencies and runs executable React/Vue/server-rendered recipe smoke checks in Chromium,
8. builds and validates the deterministic distribution ZIP/checksum, including the public-contract guide,
9. creates a GitHub **prerelease** for current pre-1.0 tags and uploads the focused ZIP and SHA-256 checksum.

Before 1.0, the workflow's prerelease flag is intentional. When the project deliberately prepares `1.0.0`, release automation/publication semantics must be reconciled so 1.0 is not accidentally published as a prerelease merely because the pre-1.0 workflow still contains `--prerelease`.

The accessibility gate is browser semantic regression evidence only; it is not a WCAG conformance or screen-reader certification step. The framework-recipe gate is representative compile/runtime evidence for the exact pinned verification versions; it is not an exhaustive React/Vue compatibility matrix.

The release job uses repository `contents: write` only for GitHub Release publication. Runtime consumers do not depend on GitHub Actions, Python, Playwright, Chromium, Firefox, Node.js, npm, React, Vue, esbuild, or other release/verification tooling. Framework/template examples in the archive remain optional consumption references and do not make those frameworks runtime dependencies.

## Verification after tagging

Confirm that the tag workflow completed successfully, the GitHub Release points to the intended tag/commit, the ZIP and `.sha256` files are attached, and the checksum matches the downloaded ZIP. Confirm the focused archive contains the documented runtime/reference allowlist, including `docs/project/public-contract.md` and integration recipes when they are part of accepted behavior. Then verify README/version references still point consumers at immutable tags rather than the moving `main` branch.

## Distribution policy

Direct vendoring from an immutable tag is the primary distribution method for pre-1.0 releases. Do not add an npm or other registry publication path merely for convenience; a new distribution surface requires a concrete consumer need and a deliberate follow-up decision. The npm toolchain used to verify framework recipes is development/CI-only and does not change this policy.

The distribution policy itself is a separate architectural/product decision from the 1.0 compatibility commitment. A 1.0 release does not require npm publication if tagged vendoring remains sufficient for actual consumers.
