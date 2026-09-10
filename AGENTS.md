# Instructions for coding assistants

This repository is the canonical UI reference for applications that use **web-tui-kit**.

## Required workflow

1. Read `DESIGN_SYSTEM.md` before implementing or changing UI.
2. Reuse `src/tokens.css` and `src/tui.css` whenever possible.
3. Reuse an existing component pattern before creating a new one.
4. Treat `demo/index.html` as an executable visual reference.
5. Keep changes framework-independent unless the consuming application explicitly requires a framework.

## Visual rules

- Do not introduce rounded corners.
- Do not introduce gradients.
- Do not introduce blurred or soft shadows.
- Do not introduce glassmorphism, Material Design, Bootstrap styling, Tailwind UI aesthetics, or modern card-style visual language.
- Use a monospace font stack.
- Use hard light/dark borders to create the classic raised/recessed dialog appearance.
- Preserve the blue desktop background and grey dialog surfaces unless a documented theme explicitly overrides them.
- Use red titles sparingly, matching the debconf/dialog reference style.
- Selected or focused list items use the canonical blue selection color.

## Interaction rules

- Every interactive control must remain keyboard reachable.
- Native semantic HTML is preferred over custom ARIA widgets.
- `Enter` should activate the focused button or control naturally.
- `Escape` may close dismissible dialogs when the host application supports it.
- Touch targets must remain usable on Android without changing the visual language.
- Hover must never be the only way to discover or operate a control.

## Responsive rules

- Preserve the same UI language on narrow screens.
- Do not transform the interface into modern mobile cards.
- Windows may become nearly full-width on small screens.
- Long tables should scroll horizontally rather than silently dropping columns.

## Adding components

When a component is missing:

1. build it from the existing tokens,
2. add a documented example to `demo/index.html`,
3. document any new token in `DESIGN_SYSTEM.md`,
4. avoid one-off values when an existing token can be reused.

## Definition of done

A UI change is complete when it is visually consistent, usable with keyboard and touch, responsive on narrow screens, and represented in the demo when it introduces a reusable pattern.
