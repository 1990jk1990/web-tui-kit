# 5. Building-block view

## Level 1: repository runtime blocks

### `src/tokens.css`

Defines the exact CSS custom properties for palette, typography, spacing, borders, shadows, window/dialog sizing, list sizing, progress sizing, and touch-sensitive minimum control sizing. It also owns the default `forced-colors` system-color overrides so high-contrast adaptation remains centralized with the palette contract.

### `src/tui.css`

Defines reusable CSS components and layouts for desktop/window surfaces, classic package-style dialogs, form controls, buttons, ordinary check/radio rows, dialog-style checklists and radiolists, action-menu rows, progress/gauges, tables, actions, and status bars. It consumes the token contract rather than hard-coding a second theme definition. Disabled choice states are derived from the underlying native disabled controls.

### `src/tui.js`

Provides small progressive enhancements while leaving application behavior to the consumer. It currently:

- dispatches `tui:escape` from an opted-in window or dialog when Escape is pressed,
- provides optional ArrowUp/ArrowDown/Home/End focus navigation inside containers marked with `data-tui-list`.

The list enhancement is deliberately narrow: it targets enabled checkboxes, buttons, links, and explicitly opted-in custom focusable list items. Native radio groups and text-entry controls are excluded so their browser keyboard semantics remain intact. Disabled, inert, hidden, and `aria-hidden` items are skipped. The enhancement changes focus only; native controls retain activation and selection semantics.

### `demo/index.html`

Consumes the runtime blocks and presents the canonical Debian/Ubuntu package-configuration visual reference. It is an executable visual reference and regression aid, not a second implementation of the design system.

### `demo/components.html` and `demo/dialogs.html`

Provide broader executable examples. `components.html` covers general-purpose controls and `dialogs.html` covers message, confirmation, input, action-menu, radiolist, checklist, and gauge compositions, including representative disabled choice states.

## Consumer integration examples

### `examples/react/PackageConfiguration.jsx`

A copy-ready React consumption recipe. It demonstrates framework-owned checkbox state and lifecycle-safe `tui:escape` handling while rendering native inputs and canonical `tui-*` classes. It is not part of the runtime and does not make React a repository dependency.

### `examples/vue/PackageConfiguration.vue`

A Vue Single File Component recipe using the same browser-native contract. It demonstrates Vue-owned state/emits without a Vue adapter layer in `src/`.

### `examples/server-rendered/package-configuration.html`

A browser-openable/template-oriented recipe. It loads the canonical assets directly and demonstrates ordinary form submission plus application-owned handling of the `tui:escape` signal.

`examples/README.md` and `docs/project/framework-integration.md` explain the shared integration rules. ADR-0004 records why recipes are preferred over maintained framework adapter runtimes at the current maturity level.

## Development-support blocks

### Structural/documentation verification

- `openspec/` owns accepted behavior and active behavioral changes.
- `docs/` owns project information, current architecture, and durable rationale.
- `tests/test_repository.py` owns inexpensive structural/runtime-contract regression evidence.
- `tests/test_framework_recipes.py` owns framework/template recipe reuse and dependency-boundary evidence.
- `tests/test_release.py` owns release/version/archive/workflow regression evidence.
- `scripts/validate_ai_doc_1.py` and `scripts/sync_openspec_docs.py` own repository/documentation validation support.
- `.github/workflows/ai-doc-1.yml` runs the structural, AI-DOC-1, and documentation checks in CI.

### Visual verification

- `requirements-visual.txt` pins the Playwright and Pillow development dependencies used for screenshots and image comparison.
- `scripts/visual_regression.py` starts a local static server, launches pinned Chromium through Playwright, captures deterministic canonical cases, and compares them with accepted baselines.
- `tests/visual/baselines/` stores the reviewed PNG baseline images for desktop and touch-capable narrow/mobile cases.
- `test-results/visual/` is generated failure output and is not committed.
- `.github/workflows/visual-regression.yml` installs the pinned browser, performs read-only comparison on pull requests and `main`, and uploads failure artifacts when necessary.

### Release and distribution

- `VERSION` is the canonical plain Semantic Version for the repository state intended for tagging.
- `RELEASING.md` defines the maintainer release procedure and fix-forward policy.
- `scripts/build_release.py` creates and validates a deterministic focused distribution ZIP plus SHA-256 checksum from an explicit file allowlist.
- `dist/` is generated release output and is not committed.
- `.github/workflows/release.yml` validates a `vMAJOR.MINOR.PATCH` tag on `main`, runs the full repository release gates, builds the focused artifacts, and publishes a GitHub prerelease only after successful verification.
- `docs/project/compatibility.md` records exercised compatibility evidence separately from target claims.

## Dependency direction

```text
consuming application / demo / integration recipe
        |
        +--> src/tokens.css
        +--> src/tui.css ----> token variables
        +--> src/tui.js  ----> browser DOM events/focus

React/Vue/template application
        |
        +--> generates semantic markup + tui-* classes
        +--> owns application state/lifecycle
        +--> does not become a dependency of src/

visual test runner ----> demo + src runtime assets
        |
        +--> pinned Playwright/Chromium
        +--> reviewed PNG baselines

VERSION + tagged main commit
        |
        +--> release builder ----> focused ZIP + SHA-256
        +--> release workflow ---> verification gates ---> GitHub prerelease

requirements ---> implementation ---> tests/demo/examples/visual/release evidence
architecture --------------------------------> describes current structure
ADRs ----------------------------------------> explain durable rationale
```

No runtime block depends on React, Vue, a template engine, MkDocs, Python, Playwright, Pillow, Chromium, GitHub Actions, the GitHub CLI, or AI-DOC-1 tooling. Those dependencies exist only in consuming applications or repository development, verification, and release paths.
