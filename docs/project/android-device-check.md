# Physical Android device check

This page defines the small manual evidence procedure for the Android design target. It is deliberately separate from the automated touch-capable Chromium suite: emulation is useful evidence, but it is not a physical-device result.

## Current evidence status

No physical Android device result is recorded yet for the v0.6 verification milestone. Do not describe physical Android Chrome or Android WebView as independently verified until a completed record is added below from an actual device run.

## Before testing

Serve the exact repository commit or immutable tag being evaluated from a machine reachable by the Android device. Record that commit/tag with the result.

Open the canonical pages in current Chrome for Android:

- `demo/index.html`
- `demo/dialogs.html`

The server-rendered recipe under `examples/server-rendered/package-configuration.html` may also be checked when validating integration examples, but it is not required for the core device result.

## Minimum manual check

1. In portrait orientation, confirm the blue desktop and grey package-style dialogs remain readable without horizontal page overflow.
2. Tap several checklist rows and confirm native checkbox state changes while the classic marker/selection language remains legible.
3. Scroll the canonical checklist and confirm the list scrolls independently without making controls unreachable.
4. Activate representative buttons in `demo/dialogs.html` and confirm touch targets are practical to hit without hover.
5. Focus the hostname input, edit text using the Android software keyboard, and confirm the input remains visible and editable.
6. Check the radiolist with touch and confirm only one native radio remains selected.
7. Rotate once to landscape and back to portrait; confirm the page remains operable and no important control becomes permanently clipped.

This check is intentionally small. Accessibility-service behavior, multiple Android vendors, Android WebView embedding, old browser versions, and performance/latency require separate evidence if they become material.

## Evidence record template

Copy this block for each actual run; do not fill fields from assumptions or emulation.

```text
Date:
Repository commit/tag:
Device manufacturer/model:
Android version:
Chrome version:
Portrait layout: PASS/FAIL + notes
Checklist touch/scroll: PASS/FAIL + notes
Buttons/touch targets: PASS/FAIL + notes
Software keyboard/input: PASS/FAIL + notes
Radiolist: PASS/FAIL + notes
Orientation change: PASS/FAIL + notes
Overall result: PASS/FAIL
Tester notes:
```

## Recorded runs

None yet.
