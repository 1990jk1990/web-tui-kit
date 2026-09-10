# Testing

## Structural project tests

Run the fast repository regression checks with:

```bash
python -m unittest discover -s tests -v
```

The test suite checks repository-level contracts such as demo asset references, required design tokens and component selectors, Escape-event behavior for opted-in windows and dialogs, optional `data-tui-list` keyboard-navigation behavior, preservation of native radio/text-entry keyboard semantics, disabled-choice handling, forced-colors token overrides, the canonical package-configuration dialog/checklist primitives, core dialog-gallery coverage, general component-gallery coverage, framework/template recipe reuse and dependency boundaries, mobile viewport metadata, visual-regression infrastructure, release version/archive/workflow safeguards, and absence of selected forbidden modern visual effects or required motion effects.

`tests/test_framework_recipes.py` verifies that the React, Vue, and server-rendered recipes exist, reuse canonical `tui-*`/native-control/event contracts, do not embed a parallel visual style implementation, and keep framework names out of the canonical `src/` runtime.

`tests/test_release.py` executes the standard-library release builder in a temporary directory, verifies its exact archive member set, fixed timestamps, embedded version, SHA-256 checksum, tag/version mismatch rejection, and release-workflow verification ordering.

## Visual regression

The canonical screenshot suite uses the exact development dependencies in `requirements-visual.txt` and the Chromium build installed by that Playwright release.

Install and run it with:

```bash
pip install -r requirements-visual.txt
python -m playwright install --with-deps chromium
python scripts/visual_regression.py
```

The runner serves the repository locally and checks four reviewed cases:

- `demo/index.html` at 1280×800 desktop,
- `demo/index.html` at 390×844 touch-capable mobile,
- `demo/dialogs.html` at 1280×1000 desktop,
- `demo/dialogs.html` at 390×844 touch-capable mobile.

The mobile cases enable Playwright's mobile/touch context flags in addition to using a narrow viewport. This is intentional: it exercises `@media (pointer: coarse)` sizing and padding rather than treating a phone-sized screenshot as a narrow mouse-driven desktop browser.

Accepted PNG baselines live in `tests/visual/baselines/`. The Linux GitHub Actions environment is the canonical rendering environment. Local output on another operating system can differ because browser/font rasterization depends on the platform.

When a comparison exceeds the narrow configured pixel tolerance, the command fails and retains actual/diff output in `test-results/visual/`. CI uploads that directory as the `visual-regression-failures` artifact on failure.

### Intentional visual changes

Do not weaken the comparison threshold or let normal CI overwrite a failing baseline. When an intentional UI change is accepted:

```bash
python scripts/visual_regression.py --update
python scripts/visual_regression.py
```

Review the resulting PNG changes together with the CSS/markup change. For the canonical project baselines, prefer generating/updating them in the same pinned Linux/Playwright environment used by CI. A Playwright upgrade also changes the Chromium build and therefore requires deliberate baseline regeneration/review.

The framework/template recipes themselves do not add a second visual baseline suite because they are consumption examples over the same canonical assets. The browser-openable server-rendered recipe may be manually inspected, while structural tests guard against visual-contract duplication. If a future adapter introduces its own rendering implementation, it would require separate visual evidence.

## Release artifact verification

Build the focused distribution with the version expected by the current repository state:

```bash
python scripts/build_release.py --version "v$(cat VERSION)" --check
```

This command uses only the Python standard library. It validates the explicit distribution allowlist, embedded version, fixed ZIP member timestamps, deterministic repeated builds, and SHA-256 checksum output. Generated artifacts live under `dist/` and are ignored by Git.

The tag-triggered release workflow repeats structural tests, AI-DOC-1 validation, documentation build, visual regression, and deterministic archive validation before it calls GitHub Release publication. It also rejects a tag that does not exactly match `VERSION` or whose commit is not contained in `main`.

## AI-DOC-1 structure

```bash
python scripts/validate_ai_doc_1.py
```

## Documentation build

```bash
pip install -r requirements-docs.txt
python scripts/sync_openspec_docs.py
mkdocs build --strict
```

## Compatibility evidence and current limits

Visual rendering is automated for the canonical package-configuration and core-dialog demos at representative Linux desktop and touch-capable narrow/mobile Chromium sizes. See `compatibility.md` for the evidence matrix and the distinction between mobile Chromium emulation and physical Android verification.

The repository does not yet provide automated Firefox rendering, browser-driven interaction flows beyond the small JavaScript contract tests, accessibility-tree/assistive-technology testing, physical-device coverage, or an automated React/Vue version matrix for the source recipes.

`demo/index.html` remains the primary executable visual reference, `demo/components.html` provides broader component coverage, and `demo/dialogs.html` provides executable core-dialog coverage. `examples/` demonstrates framework/template consumption. Manual browser/device/framework review is still useful evidence outside the automated matrix.
