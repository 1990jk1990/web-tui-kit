# Accessibility and keyboard interaction audit

Status: Completed
Related issue: #6
Related pull request: #12
Change class: Class 1 — behavioral refinement

## Motivation

The v0.2 dialog component set introduced optional list focus navigation. Before visual-regression baselines were frozen, keyboard behavior and high-contrast behavior needed refinement so the canonical examples would not encode avoidable accessibility problems.

## Delivered behavior

- Native radio groups retain native browser arrow-key selection behavior; `data-tui-list` no longer targets radio inputs.
- Optional list focus navigation targets enabled native checkboxes, buttons, links, and explicitly opted-in custom focusable list items while leaving text-entry controls alone.
- Disabled, inert, hidden, `aria-hidden`, and `aria-disabled` choices are skipped where applicable.
- Disabled checklist/radiolist/menu rows expose a muted disabled visual state.
- `forced-colors: active` maps canonical tokens to CSS system colors for high-contrast environments.
- The core stylesheet continues to avoid required decorative animation, transitions, and smooth scrolling.
- Documentation distinguishes `.tui-dialog` presentation from application-owned modal semantics.

## Boundaries

No custom ARIA listbox implementation, focus trapping, modal lifecycle management, accessibility framework, or browser automation was introduced. Native HTML semantics remain the baseline.

## Verification

- Repository regression tests cover the refined keyboard contract, disabled states, forced-colors tokens, and motion-free safeguards.
- OpenSpec, design-system guidance, architecture, testing docs, examples, and changelog were reconciled.
- GitHub Actions run `34534496852` completed successfully before archival.
