# Testing

## Structural project tests

Run the fast repository regression checks with:

```bash
python -m unittest discover -s tests -v
```

The test suite checks repository-level contracts such as demo asset references, required design tokens and component selectors, Escape-event behavior for opted-in windows and dialogs, optional `data-tui-list` keyboard-navigation behavior, preservation of native radio/text-entry keyboard semantics, disabled-choice handling, forced-colors token overrides, the canonical package-configuration dialog/checklist primitives, core dialog-gallery coverage, general component-gallery coverage, framework/template recipe reuse and dependency boundaries, browser-interaction and accessibility-semantic verification infrastructure, mobile viewport metadata, visual-regression infrastructure, release version/archive/workflow safeguards, and absence of selected forbidden modern visual effects or required motion effects.

`tests/test_framework_recipes.py` verifies that the React, Vue, and server-rendered recipes exist, reuse canonical `tui-*`/native-control/event contracts, do not embed a parallel visual style implementation, and keep framework names out of the canonical `src/` runtime.

`tests/test_interaction_regression.py` verifies that the browser interaction fixture consumes canonical runtime assets, the interaction runner covers Chromium/Firefox/touch cases and the required keyboard contracts, and the dedicated CI workflow remains read-only and uses the pinned Playwright dependency.

`tests/test_accessibility_regression.py` verifies that semantic automation runs against the canonical package/dialog demos, covers Chromium/Firefox/touch cases, checks browser roles/names/native states, keeps presentation-only helper annotations out of control accessible names, preserves a read-only CI matrix, and requires the semantic gate before release artifact publication.

`tests/test_release.py` executes the standard-library release builder in a temporary directory, verifies its exact archive member set, fixed timestamps, embedded version, SHA-256 checksum, tag/version mismatch rejection, and release-workflow verification ordering. Future releases must run visual, interaction, and accessibility-semantic browser verification before publication.

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

Accepted PNG baselines live in `tests/visual/baselines/`. The Linux GitHub Actions Chromium environment is the canonical rendering environment. Firefox interaction/semantic verification does not create a second pixel-baseline authority. Local output on another operating system can differ because browser/font rasterization depends on the platform.

When a comparison exceeds the narrow configured pixel tolerance, the command fails and retains actual/diff output in `test-results/visual/`. CI uploads that directory as the `visual-regression-failures` artifact on failure.

### Intentional visual changes

Do not weaken the comparison threshold or let normal CI overwrite a failing baseline. When an intentional UI change is accepted:

```bash
python scripts/visual_regression.py --update
python scripts/visual_regression.py
```

Review the resulting PNG changes together with the CSS/markup change. For the canonical project baselines, prefer generating/updating them in the same pinned Linux/Playwright environment used by CI. A Playwright upgrade also changes the Chromium build and therefore requires deliberate baseline regeneration/review.

The framework/template recipes themselves do not add a second visual baseline suite because they are consumption examples over the same canonical assets. The browser-openable server-rendered recipe may be manually inspected, while structural tests guard against visual-contract duplication. If a future adapter introduces its own rendering implementation, it would require separate visual evidence.

## Browser interaction regression

Browser-driven interaction verification uses the same pinned Playwright dependency but installs the engine requested by the test run.

For the complete local interaction matrix:

```bash
pip install -r requirements-visual.txt
python -m playwright install --with-deps chromium firefox
python scripts/interaction_regression.py
```

To run one engine only:

```bash
python scripts/interaction_regression.py --engine chromium
python scripts/interaction_regression.py --engine firefox
```

The runner serves `tests/browser/interaction.html`, which loads the canonical `src/` assets directly. It executes:

- Chromium desktop at 1280×800,
- Firefox desktop at 1280×800,
- Chromium at 390×844 with mobile/touch context enabled.

Desktop cases verify bubbling `tui:escape` dispatch, ArrowUp/ArrowDown/Home/End list focus navigation and wrapping, skipping disabled/inert/hidden/ARIA-disabled choices, no checkbox activation during focus movement, native radio-group arrow behavior, and native text-input caret movement. The touch case verifies the narrow viewport, coarse-pointer media query, touch capability, native checkbox tap activation, and Escape dispatch.

`.github/workflows/interaction-regression.yml` runs Chromium and Firefox as separate CI matrix jobs on pull requests and `main`. Failures retain a screenshot under `test-results/interaction/`, which CI uploads as an engine-specific failure artifact.

These interaction checks prove runtime behavior in the exercised Playwright browser builds. They do not certify assistive technology, physical Android hardware, Android WebView variants, software keyboard behavior, or other browsers not exercised by the suite.

## Accessibility semantics regression

Browser-driven accessibility semantic verification reuses the pinned Playwright dependency and directly exercises the canonical demos rather than a parallel accessibility-only fixture.

For the complete local semantic matrix:

```bash
pip install -r requirements-visual.txt
python -m playwright install --with-deps chromium firefox
python scripts/accessibility_regression.py
```

To run one engine only:

```bash
python scripts/accessibility_regression.py --engine chromium
python scripts/accessibility_regression.py --engine firefox
```

The runner exercises:

- `demo/index.html` in Chromium desktop,
- `demo/dialogs.html` in Chromium desktop,
- `demo/index.html` at 390×844 with Chromium mobile/touch context enabled,
- `demo/index.html` in Firefox desktop,
- `demo/dialogs.html` in Firefox desktop.

The suite uses browser role/name queries and native state/value checks. It verifies the named package surface and heading, checklist group and checkbox names/checked state, core action name, hostname textbox label association, named menu/radiogroup/checklist groups, menu/radio/checklist disabled state, and the native `Installing packages` progressbar with value `65`/max `100`.

The canonical `.tui-dialog` class is presentation-only, so the section-based demo surfaces are intentionally verified as named regions rather than being assigned or asserted as modal dialogs. Repeated visual helper hints such as `<Help>` are marked `aria-hidden="true"` in canonical rows when they are presentation-only, so they do not accidentally contaminate native control accessible names.

`.github/workflows/accessibility-regression.yml` runs Chromium and Firefox as separate read-only CI matrix jobs on pull requests and `main`. Failures retain diagnostic screenshots under `test-results/accessibility/`, uploaded as engine-specific artifacts.

### Evidence boundary

A passing semantic suite means the exercised browser engines expose the accepted roles, names, label associations, and native states for the tested canonical patterns. It does **not** by itself establish WCAG conformance, screen-reader output, assistive-technology interoperability, physical Android accessibility-service behavior, or usability for every disability/access method.

Those claims require separate manual/specialized evidence. Do not upgrade them to verified based only on browser semantic automation.

## Manual physical Android evidence

A small physical-device procedure lives in `docs/project/android-device-check.md`. Record the exact device, Android version, Chrome version, date, and observed results there only after an actual run. Do not infer device certification from the touch-capable Chromium CI case.

## Release artifact verification

Build the focused distribution with the version expected by the current repository state:

```bash
python scripts/build_release.py --version "v$(cat VERSION)" --check
```

This command uses only the Python standard library. It validates the explicit distribution allowlist, embedded version, fixed ZIP member timestamps, deterministic repeated builds, and SHA-256 checksum output. Generated artifacts live under `dist/` and are ignored by Git.

The tag-triggered release workflow repeats structural tests, AI-DOC-1 validation, documentation build, visual regression, cross-browser interaction verification, accessibility-semantic verification, and deterministic archive validation before it calls GitHub Release publication. It also rejects a tag that does not exactly match `VERSION` or whose commit is not contained in `main`.

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

Canonical visual rendering is automated for the package-configuration and core-dialog demos at representative Linux desktop and touch-capable narrow/mobile Chromium sizes. Runtime interaction behavior is additionally exercised in desktop Chromium, desktop Firefox, and narrow touch-capable Chromium. Browser-computed accessibility semantics are exercised in desktop Chromium/Firefox plus the narrow touch-capable Chromium package case. See `compatibility.md` for the evidence matrix and the distinction between browser automation, assistive-technology evidence, and physical Android verification.

The repository still does not provide automated real-screen-reader/assistive-technology sessions, physical-device CI, Android WebView/browser-version matrices, software-keyboard verification, real-device accessibility-service evidence, or an automated React/Vue version matrix for the source recipes.

`demo/index.html` remains the primary executable visual/semantic reference, `demo/components.html` provides broader component coverage, and `demo/dialogs.html` provides executable core-dialog coverage. `examples/` demonstrates framework/template consumption. Manual browser/device/framework/assistive-technology review remains useful evidence outside the automated matrix.
