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

## Development-support blocks

- `openspec/` owns accepted behavior and active behavioral changes.
- `docs/` owns project information, current architecture, and durable rationale.
- `tests/` owns executable regression evidence.
- `scripts/` owns documentation synchronization and repository-structure validation.
- `.github/workflows/` runs the checks in CI.

## Dependency direction

```text
consuming application / demo
        |
        +--> src/tokens.css
        +--> src/tui.css ----> token variables
        +--> src/tui.js  ----> browser DOM events/focus

requirements ---> implementation ---> tests/demo evidence
architecture -----------------------> describes current structure
ADRs -------------------------------> explain durable rationale
```

No runtime block depends on MkDocs, Python, GitHub Actions, or AI-DOC-1 tooling.
