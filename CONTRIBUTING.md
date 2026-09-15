# Contributing

`web-tui-kit` is open source under the MIT License. By submitting a contribution, you agree that your contribution may be distributed under the repository's MIT License.

The project follows AI-DOC-1 v1.3 and treats the repository as durable project memory.

## Before changing the project

Read `AGENTS.md` first. For UI changes, also read the relevant current specification under `openspec/specs/`, `DESIGN_SYSTEM.md`, the affected files under `src/`, and `demo/index.html`.

For changes to public tokens, reusable classes, semantic component markup, `data-tui-*` behavior, `tui:escape`, versioning/deprecation policy, or public-contract stability, also read `openspec/specs/public-contract/spec.md`, `docs/project/public-contract.md`, ADR-0008, and `tests/test_public_contract.py`.

For framework/template integration changes, also read `docs/project/framework-integration.md`, `examples/README.md`, the relevant recipe under `examples/`, ADR-0001, ADR-0004, and ADR-0007.

For browser verification or compatibility-evidence changes, also read `openspec/specs/browser-verification/spec.md`, `docs/project/testing.md`, `docs/project/compatibility.md`, ADR-0002, and ADR-0005.

For accessibility-semantic verification changes, also read `openspec/specs/accessibility-verification/spec.md`, `docs/project/testing.md`, `docs/project/compatibility.md`, ADR-0006, and the canonical demo markup being asserted.

For release/version/distribution changes, also read `VERSION`, `RELEASING.md`, the release/distribution OpenSpec, the public-contract specification, and the relevant ADRs, including ADR-0009 for stable release publication semantics.

## Workflow

Use a focused branch and pull request for non-trivial changes. Keep unrelated functional changes separate so review and rollback remain straightforward.

Behavioral changes must update the relevant OpenSpec artifacts. Architectural changes must update the relevant files under `docs/architecture/`; create an ADR under `docs/decisions/` only when the rationale is durable and useful later.

When adding/changing a public `--tui-*` token, `tui-*` class, scoped state hook, semantic component relationship, progressive data attribute, or custom event, update the public-contract spec/inventory and structural guard in the same change. Do not allow a new public-looking name to appear accidentally without classifying it. Starting with 1.0, normal Semantic Versioning applies to the declared public contract: incompatible public changes require a MAJOR release, while compatible additions/deprecations belong in MINOR releases with appropriate migration/deprecation guidance.

When adding a reusable component, prefer existing tokens and patterns, update the demo, and add regression evidence in `tests/`.

When adding or changing a framework/template recipe, keep framework dependencies out of `src/`, retain native semantic controls, reuse canonical `tui-*` classes/events, add structural tests that prevent parallel CSS/runtime drift, and update executable recipe verification when the integration behavior changes. Framework/build dependencies under `tests/framework/` are verification tooling only and must not become downstream requirements.

When changing keyboard/custom-event/list-navigation behavior, add or update browser-driven interaction evidence. Keep interaction fixtures on canonical `src/` assets and do not turn Playwright/Chromium/Firefox into runtime dependencies.

When changing canonical roles, labels, names, disabled/checked state, progress semantics, or helper markup, add/update browser-driven semantic evidence. Prefer native HTML semantics; do not introduce ARIA merely to make a test pass when an equivalent native element already exists. Browser semantic automation is not screen-reader or WCAG certification.

Do not change `VERSION` casually. Version changes belong to release preparation and must follow `RELEASING.md`. Published release tags are immutable; fix a bad release forward with a new Semantic Version rather than moving an existing tag.

## Verification

Before requesting review, run the fast repository/documentation checks:

```bash
python -m unittest discover -s tests -v
python scripts/validate_ai_doc_1.py
pip install -r requirements-docs.txt
python scripts/sync_openspec_docs.py
mkdocs build --strict
```

For UI or visual changes, also run the pinned Chromium screenshot suite:

```bash
pip install -r requirements-visual.txt
python -m playwright install --with-deps chromium
python scripts/visual_regression.py
```

For JavaScript interaction, keyboard, compatibility-evidence, or release-gate changes, run the browser interaction suite:

```bash
pip install -r requirements-visual.txt
python -m playwright install --with-deps chromium firefox
python scripts/interaction_regression.py
```

For semantic/accessibility-evidence or release-gate changes, run the accessibility semantics suite:

```bash
pip install -r requirements-visual.txt
python -m playwright install --with-deps chromium firefox
python scripts/accessibility_regression.py
```

For framework/template recipe, framework-evidence, or release-gate changes, also run the representative executable recipe verification:

```bash
npm install --prefix tests/framework --no-package-lock --no-audit --no-fund
pip install -r requirements-visual.txt
python -m playwright install --with-deps chromium
python scripts/framework_recipe_regression.py
```

The pinned React/Vue/tooling versions are representative verification evidence, not a promise of compatibility with every framework version. Do not move the Node/framework tooling into `src/` or require it for ordinary release consumers.

If an intended visual change makes the suite fail, do not weaken the threshold or allow CI to overwrite the baseline. Regenerate deliberately with `python scripts/visual_regression.py --update`, review the resulting PNG changes, then rerun the normal comparison. The Linux GitHub Actions Chromium environment is the canonical rendering environment; Firefox interaction/semantic evidence is not a second pixel-baseline authority. See `docs/project/testing.md` for details.

For release-preparation changes, also build the deterministic distribution artifact:

```bash
python scripts/build_release.py --version "v$(cat VERSION)" --check
```

Document pre-existing failures separately from failures introduced by a change. Do not claim a physical Android result from Playwright mobile/touch emulation; use `docs/project/android-device-check.md` for actual device evidence. Do not claim screen-reader behavior or WCAG conformance from browser role/name assertions alone.

## Distribution

Direct vendoring from an immutable release tag is the current primary distribution model. The focused archive includes `LICENSE` and `docs/project/public-contract.md` so consumers receive the license and supported surface alongside the runtime. `v0.*` tags are prereleases; stable-line tags beginning with `v1.0.0` are normal GitHub Releases. Do not add npm or another package-registry publication path without a concrete consumer need and a deliberate follow-up architectural decision.

Framework-specific examples under `examples/` are consumption recipes, not separately versioned adapter packages. A maintained adapter runtime requires a concrete integration gap and an accepted follow-up decision.

## Documentation

Do not create chat logs, AI context dumps, or parallel `new`/`v2`/`final` documentation. Update the canonical source for the information being changed. Do not edit `docs/generated/` manually.

## Security

Never commit credentials, access tokens, private keys, production secrets, or real production data. See `SECURITY.md`.
