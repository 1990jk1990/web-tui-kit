# 5. Building-block view

## Level 1: repository runtime blocks

### `src/tokens.css`

Defines the exact CSS custom properties for palette, typography, spacing, borders, shadows, window/dialog sizing, list sizing, progress sizing, and touch-sensitive minimum control sizing. It also owns the default `forced-colors` system-color overrides so high-contrast adaptation remains centralized with the palette contract.

Every canonical `--tui-*` custom-property name is part of the declared public theming surface. Compatibility protects each name and semantic purpose; exact default values remain implementation/versioned design data. The dedicated `.tui-help` presentation consumes `--tui-help`, including its forced-colors `LinkText` mapping.

### `src/tui.css`

Defines reusable CSS components and layouts for desktop/window surfaces, classic package-style dialogs, form controls, buttons, ordinary check/radio rows, dialog-style checklists and radiolists, action-menu rows, progress/gauges, tables, actions, and status bars. It consumes the token contract rather than hard-coding a second theme definition. Disabled choice states are derived from the underlying native disabled controls.

Canonical reusable `tui-*` class names are part of the declared public component surface. `.is-active` and `.is-selected` are supported only as scoped state hooks where combined with the documented TUI selectors. Selector grouping/order, pseudo-element technique, declaration order, and other implementation structure are not public APIs.

### `src/tui.js`

Provides small progressive enhancements while leaving application behavior to the consumer. It currently:

- dispatches `tui:escape` from an opted-in window or dialog when Escape is pressed,
- provides optional ArrowUp/ArrowDown/Home/End focus navigation inside containers marked with `data-tui-list`.

The public behavior names are `data-tui-escape-close`, `data-tui-list`, `data-tui-list-item`, and the bubbling `tui:escape` event with its originating keyboard event in `detail.sourceEvent`. Internal functions, constants, listener placement, and selector-construction technique are not public JavaScript APIs.

The list enhancement is deliberately narrow: it targets enabled checkboxes, buttons, links, and explicitly opted-in custom focusable list items. Native radio groups and text-entry controls are excluded so their browser keyboard semantics remain intact. Disabled, inert, hidden, and `aria-hidden` items are skipped. The enhancement changes focus only; native controls retain activation and selection semantics.

### `docs/project/public-contract.md`

Provides the practical downstream inventory for the public runtime: runtime files, all canonical token names/purposes, reusable classes, scoped states, semantic markup expectations, progressive data attributes/event, explicit non-public repository details, migration rules, and 1.0 exit criteria. Accepted behavior remains canonical in `openspec/specs/public-contract/spec.md`; ADR-0008 records the durable stability-boundary rationale.

The file is included in focused release archives so a downstream consumer does not need repository development files merely to identify supported interfaces.

### `demo/index.html`

Consumes the runtime blocks and presents the canonical Debian/Ubuntu package-configuration visual reference. It is an executable visual and semantic reference and regression aid, not a second implementation of the design system. Presentation-only helper hints inside native labels are excluded from accessible names.

The documented patterns demonstrated by the page are normative examples. Incidental IDs, sample text, option ordering, and page-specific wiring are non-public details.

### `demo/components.html` and `demo/dialogs.html`

Provide broader executable examples. `components.html` covers general-purpose controls and `dialogs.html` covers message, confirmation, input, action-menu, radiolist, checklist, and gauge compositions, including representative disabled choice states. The dialog gallery also provides canonical semantic evidence for label/control associations, named groups/regions, disabled state, and native progress semantics.

## Consumer integration examples

### `examples/react/PackageConfiguration.jsx`

A copy-ready React consumption recipe. It demonstrates framework-owned checkbox state and lifecycle-safe `tui:escape` handling while rendering native inputs and canonical `tui-*` classes. It is not part of the runtime and does not make React a repository dependency.

### `examples/vue/PackageConfiguration.vue`

A Vue Single File Component recipe using the same browser-native contract. It demonstrates Vue-owned state/emits without a Vue adapter layer in `src/`.

### `examples/server-rendered/package-configuration.html`

A browser-openable/template-oriented recipe. It loads the canonical assets directly and demonstrates ordinary form submission plus application-owned handling of the `tui:escape` signal.

`examples/README.md` and `docs/project/framework-integration.md` explain the shared integration rules. ADR-0004 records why recipes are preferred over maintained framework adapter runtimes at the current maturity level.

The recipe files are public consumption guidance, but their local component/variable names and the private compile/browser verification harness are not independent public adapter APIs.

## Development-support blocks

### Structural/documentation verification

- `openspec/` owns accepted behavior and active behavioral changes.
- `docs/` owns project information, current architecture, public-contract guidance, and durable rationale.
- `tests/test_repository.py` owns inexpensive structural/runtime-contract regression evidence.
- `tests/test_public_contract.py` owns the explicit token/class/state/data-attribute/event inventory guard and release-inclusion evidence for the public stability boundary.
- `tests/test_framework_recipes.py` owns framework/template recipe reuse and dependency-boundary evidence.
- `tests/test_interaction_regression.py` owns structural safeguards for the browser interaction fixture, runner, and CI workflow.
- `tests/test_accessibility_regression.py` owns structural safeguards for the accessibility semantic runner, canonical helper semantics, CI workflow, and release gate.
- `tests/test_release.py` owns release/version/archive/workflow regression evidence, including focused-archive inclusion of the public-contract guide and the requirement that future release publication runs visual, interaction, accessibility-semantic, and framework-recipe verification before artifact publication.
- `scripts/validate_ai_doc_1.py` and `scripts/sync_openspec_docs.py` own repository/documentation validation support.
- `.github/workflows/ai-doc-1.yml` runs the structural, AI-DOC-1, and documentation checks in CI.

### Visual verification

- `requirements-visual.txt` pins the Playwright and Pillow development dependencies used for browser verification and image comparison.
- `scripts/visual_regression.py` starts a local static server, launches pinned Chromium through Playwright, captures deterministic canonical cases, and compares them with accepted baselines.
- `tests/visual/baselines/` stores the reviewed PNG baseline images for desktop and touch-capable narrow/mobile cases.
- `test-results/visual/` is generated failure output and is not committed.
- `.github/workflows/visual-regression.yml` installs pinned Chromium, performs read-only comparison on pull requests and `main`, and uploads failure artifacts when necessary.

### Browser interaction verification

- `tests/browser/interaction.html` is a purpose-built semantic fixture that loads the canonical `src/` assets directly. It contains representative opted-in surfaces, list items, radios, text input, disabled/inert/hidden states, and a touch target without reimplementing runtime behavior.
- `scripts/interaction_regression.py` serves the repository and executes the fixture in Chromium desktop, Firefox desktop, and narrow touch-capable Chromium contexts.
- The runner verifies `tui:escape`, `data-tui-list` navigation/wrapping and skipped choices, preservation of native checkbox/radio/text-entry behavior, and touch/coarse-pointer context with native tap activation.
- `test-results/interaction/` contains generated failure screenshots and is not committed.
- `.github/workflows/interaction-regression.yml` runs a Chromium/Firefox matrix on pull requests and `main`, uploading failure screenshots when necessary.

### Accessibility semantics verification

- `scripts/accessibility_regression.py` serves the canonical `demo/index.html` and `demo/dialogs.html` pages directly instead of maintaining a parallel accessibility-only fixture.
- The runner verifies browser-computed named regions/headings/groups, checkbox/radio/button/textbox/progressbar names, checked/disabled native state, label associations, and native progress value/max in Chromium and Firefox desktop contexts.
- A narrow touch-capable Chromium package case confirms that the same core semantic identities remain available in the representative mobile/touch context.
- `test-results/accessibility/` contains generated diagnostic screenshots on failures and is not committed.
- `.github/workflows/accessibility-regression.yml` runs a Chromium/Firefox read-only matrix on pull requests and `main`, uploading engine-specific failure screenshots when necessary.
- This evidence is browser accessibility-mapping evidence, not screen-reader, assistive-technology, WCAG-conformance, or physical-device certification. ADR-0006 records that boundary.

### Release and distribution

- `VERSION` is the canonical plain Semantic Version for the repository state intended for tagging.
- `RELEASING.md` defines the maintainer release procedure, public-contract compatibility/deprecation policy, and fix-forward policy.
- `scripts/build_release.py` creates and validates a deterministic focused distribution ZIP plus SHA-256 checksum from an explicit file allowlist, including `docs/project/public-contract.md`.
- `dist/` is generated release output and is not committed.
- `.github/workflows/release.yml` validates a `vMAJOR.MINOR.PATCH` tag on `main`, runs the full repository release gates including visual, interaction, accessibility-semantic, and framework-recipe browser verification, builds the focused artifacts, and publishes a GitHub prerelease only after successful verification.
- `docs/project/compatibility.md` records exercised compatibility evidence separately from target claims and public API stability.

## Dependency direction

```text
consuming application / demo / integration recipe
        |
        +--> public contract guide/spec
        +--> src/tokens.css
        +--> src/tui.css ----> token variables
        +--> src/tui.js  ----> browser DOM events/focus

React/Vue/template application
        |
        +--> generates semantic markup + tui-* classes
        +--> owns application state/lifecycle
        +--> does not become a dependency of src/

public-contract structural tests ----> src tokens/classes/js + contract docs

visual test runner ----> demo + src runtime assets
        |
        +--> pinned Playwright/Chromium
        +--> reviewed PNG baselines

interaction runner ----> tests/browser fixture ----> src runtime assets
        |
        +--> pinned Playwright/Chromium desktop + touch context
        +--> pinned Playwright/Firefox desktop

accessibility semantic runner ----> canonical demos ----> src runtime assets
        |
        +--> browser role/name/native-state queries
        +--> pinned Playwright/Chromium desktop + touch context
        +--> pinned Playwright/Firefox desktop

VERSION + tagged main commit
        |
        +--> release builder ----> focused ZIP + SHA-256 + public contract guide
        +--> release workflow ---> structural/docs/visual/interaction/accessibility/framework gates ---> GitHub prerelease

requirements ---> implementation ---> tests/demo/examples/browser/release evidence
architecture ----------------------------------------> describes current structure
ADRs ------------------------------------------------> explain durable rationale
```

No runtime block depends on React, Vue, a template engine, MkDocs, Python, Playwright, Pillow, Chromium, Firefox, GitHub Actions, the GitHub CLI, or AI-DOC-1 tooling. Those dependencies exist only in consuming applications or repository development, verification, and release paths.
