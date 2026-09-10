# Accessibility and keyboard interaction audit

Status: Active
Related issue: #6
Change class: Class 1 — behavioral refinement

## Motivation

The v0.2 dialog component set adds optional list focus navigation. Before visual-regression baselines are frozen, keyboard behavior and high-contrast behavior should be tightened so the canonical examples do not encode avoidable accessibility problems.

## Proposed behavior

- Native radio groups keep native browser arrow-key selection behavior; `data-tui-list` MUST NOT override radio inputs.
- Optional list focus navigation applies to native checkboxes, buttons, links, and explicitly opted-in custom list items, while leaving ordinary text-entry controls alone.
- Disabled checklist/radiolist rows expose a disabled visual state and are skipped by optional list navigation.
- Core controls provide an intentional forced-colors/high-contrast treatment using system colors.
- The core design system continues to avoid decorative animation and smooth scrolling, so reduced-motion users are not forced through motion effects.
- Documentation explicitly distinguishes visual dialog styling from application-level modal semantics.

## Boundaries

This change does not introduce a custom ARIA listbox implementation, focus trapping, modal lifecycle management, an accessibility framework, or browser automation. Native HTML semantics remain the baseline.

## Acceptance criteria

- Radio inputs are not intercepted by the optional list-navigation handler.
- Arrow navigation still works for opted-in checklist and action-menu examples.
- Disabled choice rows are visually identifiable and skipped by the handler.
- Forced-colors styles exist for the core interactive/selection surfaces.
- Regression tests cover the refined keyboard contract and reduced-motion/high-contrast safeguards.
- OpenSpec, design-system guidance, testing docs, and changelog are reconciled.
