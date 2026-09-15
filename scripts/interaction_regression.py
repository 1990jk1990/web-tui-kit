from __future__ import annotations

import argparse
from dataclasses import dataclass
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading

from playwright.sync_api import Browser, Page, sync_playwright


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = "/tests/browser/interaction.html"
RESULT_DIR = ROOT / "test-results" / "interaction"


@dataclass(frozen=True)
class InteractionCase:
    name: str
    engine: str
    width: int
    height: int
    mobile: bool = False


CASES = (
    InteractionCase("chromium-desktop", "chromium", 1280, 800),
    InteractionCase("chromium-touch", "chromium", 390, 844, True),
    InteractionCase("firefox-desktop", "firefox", 1280, 800),
)


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        return


def start_server() -> tuple[ThreadingHTTPServer, threading.Thread]:
    handler = lambda *args, **kwargs: QuietHandler(
        *args, directory=str(ROOT), **kwargs
    )
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def active_id(page: Page) -> str:
    return page.evaluate("document.activeElement?.id || ''")


def install_escape_probe(page: Page) -> None:
    page.evaluate(
        """
        () => {
          window.__tuiEscapeEvents = [];
          document.addEventListener("tui:escape", (event) => {
            window.__tuiEscapeEvents.push({
              targetId: event.target?.id || "",
              bubbles: event.bubbles,
              hasSourceEvent: Boolean(event.detail?.sourceEvent),
            });
          });
        }
        """
    )


def verify_escape_dispatch(page: Page) -> None:
    install_escape_probe(page)
    page.locator("#escape-focus").focus()
    page.keyboard.press("Escape")
    events = page.evaluate("window.__tuiEscapeEvents")
    require(len(events) == 1, f"expected one tui:escape event, got {events!r}")
    event = events[0]
    require(event["targetId"] == "escape-surface", f"wrong Escape target: {event!r}")
    require(event["bubbles"] is True, f"tui:escape did not bubble: {event!r}")
    require(event["hasSourceEvent"] is True, f"tui:escape lost sourceEvent: {event!r}")


def verify_native_dialog_title_overflow(page: Page) -> None:
    geometry = page.evaluate(
        """
        () => {
          const dialog = document.querySelector("#native-dialog-surface");
          const title = document.querySelector("#native-dialog-title");
          dialog.show();
          const dialogRect = dialog.getBoundingClientRect();
          const titleRect = title.getBoundingClientRect();
          return {
            overflow: getComputedStyle(dialog).overflow,
            dialogTop: dialogRect.top,
            titleTop: titleRect.top,
          };
        }
        """
    )
    require(
        geometry["overflow"] == "visible",
        f"native dialog outer overflow clips the border title: {geometry!r}",
    )
    require(
        geometry["titleTop"] < geometry["dialogTop"],
        f"native dialog title no longer protrudes above the top bevel: {geometry!r}",
    )


def verify_list_navigation(page: Page) -> None:
    first = page.locator("#nav-check-first")
    first.focus()
    require(first.is_checked(), "fixture precondition failed: first checkbox should start checked")

    page.keyboard.press("ArrowDown")
    require(active_id(page) == "nav-button", "ArrowDown did not skip disabled checkbox")

    page.keyboard.press("ArrowDown")
    require(active_id(page) == "nav-link", "ArrowDown did not skip inert content")

    page.keyboard.press("ArrowDown")
    require(active_id(page) == "nav-custom", "ArrowDown did not skip hidden/ARIA-disabled items")

    page.keyboard.press("ArrowDown")
    require(active_id(page) == "nav-check-first", "ArrowDown did not wrap to first item")

    page.keyboard.press("ArrowUp")
    require(active_id(page) == "nav-custom", "ArrowUp did not wrap to last item")

    page.keyboard.press("Home")
    require(active_id(page) == "nav-check-first", "Home did not focus first enabled item")

    page.keyboard.press("End")
    require(active_id(page) == "nav-custom", "End did not focus last enabled item")

    require(first.is_checked(), "focus navigation unexpectedly toggled checkbox state")


def verify_native_radio_behavior(page: Page) -> None:
    first = page.locator("#radio-first")
    second = page.locator("#radio-second")
    first.focus()
    require(first.is_checked(), "fixture precondition failed: first radio should start selected")

    page.keyboard.press("ArrowDown")
    require(second.is_checked(), "native radio ArrowDown did not select the next enabled radio")
    require(active_id(page) == "radio-second", "native radio ArrowDown did not move focus")
    require(not first.is_checked(), "native radio group retained two selected values")


def verify_text_entry_behavior(page: Page) -> None:
    text_input = page.locator("#text-input")
    text_input.focus()
    page.evaluate("document.querySelector('#text-input').setSelectionRange(2, 2)")

    page.keyboard.press("ArrowLeft")
    selection = page.evaluate(
        """
        () => {
          const input = document.querySelector("#text-input");
          return [input.selectionStart, input.selectionEnd, document.activeElement?.id || ""];
        }
        """
    )
    require(selection == [1, 1, "text-input"], f"ArrowLeft was intercepted: {selection!r}")

    page.keyboard.press("ArrowRight")
    selection = page.evaluate(
        """
        () => {
          const input = document.querySelector("#text-input");
          return [input.selectionStart, input.selectionEnd, document.activeElement?.id || ""];
        }
        """
    )
    require(selection == [2, 2, "text-input"], f"ArrowRight was intercepted: {selection!r}")


def verify_touch_context(page: Page) -> None:
    environment = page.evaluate(
        """
        () => ({
          width: window.innerWidth,
          coarse: window.matchMedia("(pointer: coarse)").matches,
          touchPoints: navigator.maxTouchPoints,
        })
        """
    )
    require(environment["width"] == 390, f"unexpected mobile viewport: {environment!r}")
    require(environment["coarse"] is True, f"coarse pointer media query inactive: {environment!r}")
    require(environment["touchPoints"] > 0, f"touch capability missing: {environment!r}")

    touch_row = page.locator("#touch-row")
    checkbox = page.locator("#touch-checkbox")
    require(not checkbox.is_checked(), "fixture precondition failed: touch checkbox starts checked")
    touch_row.tap()
    require(checkbox.is_checked(), "tapping the visible checkbox row did not toggle its native checkbox")


def verify_desktop_contracts(page: Page) -> None:
    verify_native_dialog_title_overflow(page)
    verify_escape_dispatch(page)
    verify_list_navigation(page)
    verify_native_radio_behavior(page)
    verify_text_entry_behavior(page)


def new_context(browser: Browser, case: InteractionCase):
    return browser.new_context(
        viewport={"width": case.width, "height": case.height},
        screen={"width": case.width, "height": case.height},
        device_scale_factor=1,
        is_mobile=case.mobile,
        has_touch=case.mobile,
        locale="en-US",
        timezone_id="UTC",
        color_scheme="light",
        reduced_motion="reduce",
    )


def run_case(browser: Browser, base_url: str, case: InteractionCase) -> None:
    context = new_context(browser, case)
    page: Page | None = None
    try:
        page = context.new_page()
        page.goto(f"{base_url}{FIXTURE_PATH}", wait_until="networkidle")
        if case.mobile:
            verify_native_dialog_title_overflow(page)
            verify_touch_context(page)
            verify_escape_dispatch(page)
        else:
            verify_desktop_contracts(page)
    except Exception:
        RESULT_DIR.mkdir(parents=True, exist_ok=True)
        if page is not None:
            try:
                page.screenshot(path=str(RESULT_DIR / f"{case.name}-failure.png"), full_page=True)
            except Exception:
                pass
        raise
    finally:
        context.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify web-tui-kit interaction contracts in real browser engines."
    )
    parser.add_argument(
        "--engine",
        choices=("all", "chromium", "firefox"),
        default="all",
        help="Run all configured engines or only one Playwright browser engine.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    failures: list[str] = []
    selected = [case for case in CASES if args.engine == "all" or case.engine == args.engine]

    server, thread = start_server()
    base_url = f"http://127.0.0.1:{server.server_port}"

    try:
        with sync_playwright() as playwright:
            for case in selected:
                browser_type = getattr(playwright, case.engine)
                browser = browser_type.launch(headless=True)
                try:
                    run_case(browser, base_url, case)
                    print(f"PASS {case.name}")
                except Exception as error:
                    failures.append(f"{case.name}: {error}")
                    print(f"FAIL {failures[-1]}")
                finally:
                    browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    if failures:
        print("\nInteraction regression failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())