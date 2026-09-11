# Tasks

- [ ] Inventory the documented and implemented consumer-facing runtime surface across `src/`, OpenSpec, `DESIGN_SYSTEM.md`, demos, integration guidance, and release contents.
- [ ] Classify public versus demo/test/internal-only tokens, classes, events, data attributes, markup expectations, and integration patterns.
- [ ] Review the current public names/contracts for inconsistencies worth correcting before 1.0; document any intentional migration.
- [ ] Add or reconcile accepted OpenSpec requirements for the public-surface boundary and stability rules.
- [ ] Define compatibility, deprecation, migration, and removal policy for public contract changes before and after 1.0.
- [ ] Add structural regression tests protecting the declared public contract from silent removal or rename.
- [ ] Reconcile `DESIGN_SYSTEM.md`, project/framework guidance, architecture/ADR material, release docs, and compatibility evidence.
- [ ] Define concrete evidence-based 1.0 exit criteria and keep unsupported physical Android / real AT / WCAG / exhaustive framework-version claims outside those criteria unless real evidence is added.
- [ ] Run project tests, AI-DOC-1 validation, strict MkDocs build, and any applicable visual/interaction/accessibility/framework regression gates.
- [ ] Inspect the complete diff, archive the OpenSpec change, prepare a focused PR, and merge only after green verification.