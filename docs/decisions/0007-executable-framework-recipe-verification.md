# ADR-0007: Executable verification for framework consumption recipes

- Status: Accepted
- Date: 2026-09-11
- Related OpenSpec change: `framework-recipe-execution-verification`
- Related issue: #24
- Supersedes: none
- Superseded by: none

## Context

ADR-0004 deliberately chose copy-ready React/Vue/template recipes instead of maintained adapter runtimes. Structural tests protect the recipes from duplicating the visual system or leaking framework dependencies into `src/`, but they cannot prove that the canonical JSX/SFC source still compiles and behaves correctly in a real consumer.

The project now has mature browser verification for the canonical runtime. The remaining explicit framework evidence gap is therefore recipe execution, not a need for new adapter APIs.

## Decision

Add a development/CI-only executable recipe verification harness.

A private toolchain under `tests/framework/` pins representative React, React DOM, Vue, Vue SFC compiler, and bundler versions. It compiles the canonical recipe files directly, renders them in the pinned Chromium environment already used by repository browser verification, and exercises the integration contract with canonical `src/` assets.

The verification proves representative compile/render/state/event interoperability for the pinned versions. It does not create a framework runtime, package, or exhaustive version-support promise.

Once stable, tagged release publication runs this verification before the deterministic release archive is built or published.

## Considered alternatives

- Keep source-text structural checks only.
- Add maintained React/Vue adapter packages and test those instead.
- Publish `web-tui-kit` through npm so framework tests can install it as a package.
- Maintain a broad framework-version matrix immediately.
- Use framework-specific copied CSS/runtime fixtures rather than the canonical assets.

## Consequences

### Positive

- Detects stale JSX/SFC syntax and actual integration failures that structural tests cannot catch.
- Verifies application-owned accept/cancel state handling together with canonical progressive enhancement.
- Keeps framework evidence tied to the same canonical runtime assets consumed downstream.
- Preserves ADR-0004: recipes remain examples, not maintained adapter APIs.

### Negative / trade-offs

- Repository CI now has a development-only Node/npm toolchain in addition to Python browser tooling.
- Direct framework/tool versions are representative evidence, not exhaustive version compatibility.
- npm dependency installation adds CI network/supply-chain surface, although it remains outside runtime/release artifacts and uses exact direct versions.

## Evidence / notes

The harness lives under `tests/framework/`, builds temporary browser fixtures under ignored `test-results/framework/`, and is driven by `scripts/framework_recipe_regression.py`. Framework dependencies must never move into `src/` or become required by consumers of the focused release runtime.
