# Project overview

## Purpose

`web-tui-kit` is a reusable browser UI design system for applications that should present a consistent text-oriented interface inspired by Debian debconf, `dialog`, and `whiptail`.

Its primary use case is to let independent browser applications share one UI language and to give humans and coding assistants a durable reference that can be reused instead of recreating the style from screenshots or chat history.

## Users

- developers building browser-based tools,
- AI coding agents implementing those tools,
- end users operating the resulting interfaces on Linux desktops and Android devices.

## Scope

The repository provides design tokens, CSS component styles, small progressive-enhancement JavaScript, an explicit public consumer-contract/stability boundary, executable visual/semantic references, requirements, architecture documentation, development guidance, structural regression tests, browser-driven Chromium visual regression baselines for canonical demos, cross-browser interaction verification in Chromium/Firefox, browser accessibility-semantic verification in Chromium/Firefox, representative narrow touch-browser evidence, deterministic tagged release artifacts for direct vendoring, framework/template integration recipes that reuse the canonical browser-native contract, and development-only executable verification that compiles/runs those canonical recipes with representative pinned framework/tool versions.

The canonical visual/semantic reference is `demo/index.html`: a centered package-style dialog with a blue desktop background, grey beveled surface, red title accent, recessed scrollable checklist, blue focused row, text-style checkbox markers, contextual help accents, and angle-bracket actions. Its native labels/groups/headings are also exercised by browser semantic regression.

`demo/dialogs.html` is the executable catalog for common dialog compositions: message, yes/no confirmation, input, action menu, radiolist, checklist, and progress/gauge. It also supplies canonical semantic evidence for labels, groups, native state, and progress. `demo/components.html` provides broader general component coverage.

`examples/react/`, `examples/vue/`, and `examples/server-rendered/` show how different application stacks consume the same semantic markup/class/event contract. They are consumption recipes rather than separate framework runtimes. Their representative compile/runtime verification remains development/CI-only and does not change the consumer dependency model.

The accepted behavioral, public-contract, verification, release/distribution, and framework-integration contracts are canonical in `openspec/specs/`. `docs/project/public-contract.md` provides the practical inventory of supported token/class/state/data-attribute/event names, required semantic markup relationships, non-public repository detail, migration rules, and 1.0 exit criteria.

## Non-goals

`web-tui-kit` is not a terminal emulator, ncurses binding, application backend, routing framework, or full application framework. Consuming applications remain responsible for their domain logic, data access, authentication, routing, and application-specific behavior. Development-only browser/accessibility/framework verification and release tooling is not part of the runtime contract consumed by applications.

The project does not maintain React/Vue adapter runtimes or require framework dependencies in `src/`. A future adapter requires a demonstrated integration gap and a deliberate architecture/specification change. Tagged direct vendoring remains the baseline distribution model. Pinned framework verification versions are evidence anchors rather than a broad support-version promise.

Automated touch-capable Chromium evidence is not physical Android/Android WebView certification. Browser role/name/state automation is not a WCAG conformance statement and is not screen-reader/assistive-technology certification. Physical-device and real assistive-technology evidence are recorded separately only after actual runs.

The 1.0 readiness policy does not manufacture those unperformed evidence domains into certification requirements. A future accepted requirement may add one deliberately, but the current 1.0 decision is based on the declared browser-native public contract and existing release gates.

## Maturity

The project is pre-1.0. Version `0.9.0` packages the established visual foundation, core dialog patterns, accessibility/keyboard refinement, canonical Chromium visual regression, deterministic release/distribution workflow, React/Vue/server-rendered consumption recipes, browser-driven Chromium/Firefox interaction verification with representative narrow touch behavior, browser-driven accessibility-semantic verification of canonical roles, names, labels, native states, and progress semantics, executable compile/runtime verification for the canonical React/Vue/server-rendered recipes with pinned representative framework/tool versions, and the explicit browser-native public consumer contract with structural drift protection and pre/post-1.0 compatibility rules.

The framework-independent `src/` runtime and immutable tagged-vendoring model remain unchanged. Linux Chromium remains the sole screenshot-baseline authority; pinned framework versions are representative evidence rather than an exhaustive support matrix, and physical Android plus real assistive-technology/WCAG verification remain separate evidence domains.

The v0.9 readiness audit selected no public class/token/event/data-attribute rename or removal beyond correcting `.tui-help` to consume its already-declared `--tui-help` token. The accepted public-contract specification now defines explicit evidence-based 1.0 exit criteria. After `v0.9.0` publication, those criteria are evaluated directly; if they remain satisfied and no new focused gap is identified, the next milestone is deliberate `1.0.0` release preparation rather than an automatic or arbitrary version bump.
