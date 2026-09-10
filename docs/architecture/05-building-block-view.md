# 5. Building-block view

## Level 1: repository runtime blocks

### `src/tokens.css`

Defines the exact CSS custom properties for palette, typography, spacing, borders, shadows, window sizing, and touch-sensitive minimum control sizing. Other runtime styles depend on these tokens.

### `src/tui.css`

Defines reusable CSS components and layouts such as desktop, window, panel, form controls, buttons, checks, radios, menus, tables, actions, and status bars. It consumes the token contract rather than hard-coding a second theme definition.

### `src/tui.js`

Provides small progressive enhancements. At present it listens for `Escape` and dispatches `tui:escape` from an opted-in `.tui-window[data-tui-escape-close]`. The consuming application owns the resulting action.

### `demo/index.html`

Consumes the runtime blocks and exercises the reusable patterns in one browser page. It is an executable visual reference and regression aid, not a second implementation of the design system.

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
        +--> src/tui.js  ----> browser DOM events

requirements ---> implementation ---> tests/demo evidence
architecture -----------------------> describes current structure
ADRs -------------------------------> explain durable rationale
```

No runtime block depends on MkDocs, Python, GitHub Actions, or AI-DOC-1 tooling.
