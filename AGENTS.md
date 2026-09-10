# AGENTS.md

This project follows **AI-DOC-1 v1.3**.

Standard source: `https://github.com/1990jk1990/AI-DOC-1`

This repository is also the canonical UI reference for applications that use **web-tui-kit**.

## Role

Act as the project's knowledge steward. The human user is not required to know where project information belongs.

You must:

- determine and maintain the correct canonical artifact automatically,
- inspect repository evidence before asking questions,
- ask only for material user-owned information that cannot be safely inferred,
- reconcile affected requirements, architecture, decisions, developer docs, tests, and implementation before completion,
- never preserve project knowledge only in chat history.

Do not ask the human whether to use OpenSpec, arc42, an ADR, or another documentation mechanism.

## Mandatory onboarding

Before non-trivial changes:

1. Read `ai-doc-1.yaml`.
2. Read `README.md` and `CONTRIBUTING.md`.
3. Read the relevant current specification under `openspec/specs/`.
4. Read relevant architecture and ADRs under `docs/`.
5. For UI work, read `DESIGN_SYSTEM.md`, `src/tokens.css`, `src/tui.css`, and `demo/index.html`.
6. Inspect relevant tests and GitHub work state.

## Canonical sources

- Expected behavior → `openspec/specs/`.
- Active non-trivial behavioral changes → `openspec/changes/`.
- Current architecture → `docs/architecture/`.
- Important rationale → `docs/decisions/`.
- Exact design-token values → `src/tokens.css`.
- Implementation → `src/`.
- Executable behavior evidence → `tests/`.
- Visual examples → `demo/index.html`.
- Open work → GitHub Issues/Projects.
- Release identity → Git tags/GitHub Releases.
- Secrets → external secret store; never this repository.

`DESIGN_SYSTEM.md` is a practical consumption guide. It may summarize canonical behavior but must point to OpenSpec and implementation rather than becoming a conflicting source of truth.

## Project-specific UI rules

Follow the current OpenSpec specification first. In particular, preserve these established design constraints unless the specification is deliberately changed:

- no rounded corners, gradients, blur, glass effects, soft shadows, or modern card-style visual language,
- monospace typography for core application chrome,
- hard light/dark borders for raised and recessed surfaces,
- canonical blue desktop background, grey surfaces, red title accents, and blue selections,
- native semantic HTML wherever practical,
- keyboard reachability for interactive controls,
- touch usability on Android without replacing the visual language with a separate mobile design,
- no hover-only operation,
- horizontal scrolling for tables that do not fit narrow viewports rather than silently dropping important columns.

Keep the baseline framework-independent. A consuming application may use a framework, but this library must not require one unless a future accepted decision changes that constraint.

## Adding or changing reusable components

For non-trivial component behavior changes:

1. update or create the relevant OpenSpec change/specification,
2. implement from existing tokens before adding one-off values,
3. update `demo/index.html` when a reusable visual pattern changes or is added,
4. add or update tests,
5. update architecture or an ADR only when the change affects current structure or durable rationale,
6. reconcile `DESIGN_SYSTEM.md` if its practical usage guidance is affected.

## Change classes

- Class 0 — trivial/internal: usually implementation/tests only.
- Class 1 — behavioral: OpenSpec + implementation/tests.
- Class 2 — architectural: relevant Class 1 artifacts + arc42 documentation + ADR when rationale is durable.
- Class 3 — operational/security/data/breaking: relevant lower-class artifacts + explicit safety, migration, deployment, or rollback material.

## Human interaction and safety

Ask only when intended behavior or scope remains materially ambiguous, a genuine user preference must choose among valid alternatives, security intent is unknown, destructive action needs authorization, or conflicting project rules cannot be resolved from repository evidence.

Never commit secrets or real production data. Explain destructive/high-impact actions and recovery implications before execution.

## Completion check

A UI change is complete only when affected canonical documentation is reconciled, tests pass, the result is visually consistent, keyboard and touch use remain viable, narrow-screen behavior remains intentional, and reusable patterns are represented in the demo where appropriate.
