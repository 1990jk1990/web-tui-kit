# Native dialog title overflow compatibility

Status: Accepted for implementation
Related issue: #37
Change class: Class 1 — behavioral

## Motivation

A real downstream consumer (`lighting-service`) used the public `.tui-dialog` presentation class on native `<dialog>` elements and found that the canonical `.tui-dialog-title` could be clipped at the top border. The title is intentionally positioned across the top bevel with an absolute position and negative vertical translation, but the outer `.tui-dialog` did not explicitly neutralize overflow behavior. Native `<dialog>` user-agent styling can supply scrolling/overflow behavior, and consumer-added overflow on the outer surface has the same clipping effect.

The downstream application therefore had to add `overflow: visible` to each modal dialog even though the visual title treatment belongs to the design system.

## Accepted behavior

- The canonical `.tui-dialog` outer surface keeps overflow visible so `.tui-dialog-title` can protrude across the top bevel when used on a native `<dialog>` element.
- Native `<dialog>` remains application-owned for modal semantics and lifecycle; this change only fixes presentation compatibility.
- Consumers that need scrollable dialog content place scrolling on an inner content/list region rather than on the outer `.tui-dialog` surface.
- No new public class, token, data attribute, event, or semantic requirement is introduced.

## Compatibility

This is a compatible stable-line bug fix to existing public `.tui-dialog` behavior. It preserves the 1.x public surface and is suitable for a future PATCH release; `VERSION` is intentionally unchanged outside release preparation.

## Verification

The existing cross-browser interaction fixture will gain a native `<dialog>` case that verifies the canonical outer surface computes to visible overflow and that the title geometrically protrudes above the dialog border in Chromium, Firefox, and the representative narrow touch-capable Chromium context. Structural tests will guard that browser fixture/runner coverage remains present.
