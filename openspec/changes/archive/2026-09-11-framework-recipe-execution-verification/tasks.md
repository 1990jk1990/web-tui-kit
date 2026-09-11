# Tasks

- [x] Add the pinned development-only framework verification toolchain under `tests/framework/`.
- [x] Compile the canonical React and Vue recipes without duplicating reusable runtime/styling.
- [x] Add browser-driven smoke verification for React, Vue, and server-rendered consumers.
- [x] Add structural safeguards for framework verification boundaries and exact direct dependency versions.
- [x] Add a dedicated read-only CI workflow.
- [x] Gate future tagged releases on the stable framework recipe verification before artifact build/publication.
- [x] Reconcile the framework integration OpenSpec contract, architecture, ADR, testing/compatibility/framework docs, AGENTS/CONTRIBUTING, release guidance, and changelog.
- [x] Run structural tests, AI-DOC-1 validation, strict docs build, framework recipe verification, visual regression, interaction regression, and accessibility semantic regression.
- [x] Review the complete diff, archive this change, and prepare the PR for merge.

Final pre-archive verification on branch head `509f2128928781d98e6bbb1a6ccecd2502a10d5d` was green for AI-DOC-1/project/docs validation (`34549641808`), visual regression (`34549641815`), browser interaction regression (`34549641802`), accessibility semantics regression (`34549641830`), and framework recipe regression (`34549641826`).
