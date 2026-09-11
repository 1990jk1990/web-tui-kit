# Executable framework recipe verification

Status: Completed
Related issue: #24
Change class: Class 2 — architecture/verification

## Motivation

The React and Vue consumption recipes were protected by structural tests, but they were not compiled and executed against representative framework versions. `docs/project/testing.md` and ADR-0004 recorded this as a remaining verification trade-off/gap.

A stale JSX/SFC recipe could therefore remain structurally valid while failing in an actual consumer. This change closes that concrete evidence gap without introducing framework adapters or framework dependencies into the canonical runtime.

## Implemented change

- Added a development/CI-only framework verification harness under `tests/framework/` with exact representative React, Vue, compiler, and bundler direct versions.
- Compile the canonical `examples/react/PackageConfiguration.jsx` and `examples/vue/PackageConfiguration.vue` source recipes rather than copying them into test-only implementations.
- Render the compiled recipes in pinned Chromium with canonical `src/tokens.css`, `src/tui.css`, and `src/tui.js` assets.
- Verify native checkbox state changes, optional `data-tui-list` focus movement, `tui:escape` delivery into application-owned cancel handlers, and accept callback/event payloads.
- Include the browser-openable server-rendered recipe in the same consumer smoke boundary to verify ordinary form semantics and canonical progressive enhancement.
- Added a dedicated read-only CI workflow and the same recipe verification gate to tagged release publication before artifact creation.
- Keep Node/framework/build dependencies out of `src/`, out of focused release runtime requirements, and out of downstream consumption requirements.

## Boundaries

This change does not add a React/Vue adapter package, npm distribution for `web-tui-kit`, framework-specific reusable styling, or a broad support promise for every framework version. Pinned representative versions are verification evidence only.

Linux Chromium remains the browser used for this consumer-integration smoke evidence. Existing Chromium/Firefox runtime and accessibility suites continue to own browser-engine compatibility evidence for the canonical browser-native contract.

## Acceptance evidence

- Canonical React and Vue recipe files compile with the pinned development-only toolchain.
- Browser smoke verification renders each canonical recipe using canonical runtime assets.
- React and Vue checks prove native selection changes, list focus enhancement, Escape-to-cancel handling, and accept payloads.
- The server-rendered recipe proves canonical selection/form semantics and Escape handling without a framework runtime.
- Structural tests prevent framework verification dependencies from entering `src/` or being mistaken for downstream runtime dependencies.
- Dedicated read-only framework recipe CI is green alongside AI-DOC-1/docs, visual, interaction, and accessibility-semantic verification.
- Tagged release publication runs stable framework recipe verification before release artifacts are built/published.
- OpenSpec, architecture, ADR, testing/compatibility/framework documentation, release guidance, and AGENTS/CONTRIBUTING guidance are reconciled.
