from __future__ import annotations

import argparse
from dataclasses import dataclass
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re
import threading

from playwright.sync_api import Browser, Locator, Page, sync_playwright


ROOT = Path(__file__).resolve().parents[1]
RESULT_DIR = ROOT / "test-results" / "accessibility"


@dataclass(frozen=True)
class AccessibilityCase:
    name: str
    engine: str
    path: str
    kind: str
    width: int
    height: int
    mobile: bool = False


CASES = (
    AccessibilityCase("chromium-package", "chromium", "/demo/index.html", "package", 1280, 800),
    AccessibilityCase("chromium-dialogs", "chromium", "/demo/dialogs.html", "dialogs", 1280, 1000),
    AccessibilityCase("chromium-package-touch", "chromium", "/demo/index.html", "package-touch", 390, 844, True),
    AccessibilityCase("firefox-package", "firefox", "/demo/index.html", "package", 1280, 800),
    AccessibilityCase("firefox-dialogs", "firefox", "/demo/dialogs.html", "dialogs", 1280, 1000),
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


def exactly_one(locator: Locator, description: str) -> Locator:
    count = locator.count()
    require(count == 1, f"expected one {description}, found {count}")
    return locator


def verify_package_semantics(page: Page) -> None:
    surface = exactly_one(
        page.get_by_role("region", name="Package configuration", exact=True),
        "named package region",
    )
    exactly_one(
        surface.get_by_role("heading", name="Package configuration", exact=True, level=1),
        "package heading",
    )
    require(
        page.get_by_role("dialog").count() == 0,
        "presentation-only .tui-dialog unexpectedly exposes dialog semantics",
    )

    services = exactly_one(
        surface.get_by_role("group", name="Services to restart", exact=True),
        "services checklist group",
    )
    checkboxes = services.get_by_role("checkbox")
    require(checkboxes.count() == 12, f"expected 12 service checkboxes, found {checkboxes.count()}")

    accounts = exactly_one(
        services.get_by_role("checkbox", name="accounts-daemon.service", exact=True),
        "accounts-daemon checkbox",
    )
    apache = exactly_one(
        services.get_by_role("checkbox", name="apache2.service", exact=True),
        "apache2 checkbox",
    )
    require(accounts.is_checked(), "accounts-daemon checkbox lost checked state")
    require(not apache.is_checked(), "apache2 checkbox unexpectedly checked")
    require(
        services.get_by_role("checkbox", name=re.compile(r"Help", re.IGNORECASE)).count() == 0,
        "presentation-only Help text leaked into a checkbox accessible name",
    )

    exactly_one(surface.get_by_role("button", name="Ok", exact=True), "package Ok action")


def verify_dialogs_semantics(page: Page) -> None:
    require(
        page.get_by_role("dialog").count() == 0,
        "presentation-only .tui-dialog examples unexpectedly expose dialog semantics",
    )

    message = exactly_one(page.get_by_role("region", name="Message box", exact=True), "Message box region")
    exactly_one(message.get_by_role("heading", name="Message box", exact=True, level=1), "Message box heading")
    exactly_one(message.get_by_role("button", name="Ok", exact=True), "Message box Ok action")

    confirmation = exactly_one(page.get_by_role("region", name="Confirmation", exact=True), "Confirmation region")
    exactly_one(confirmation.get_by_role("button", name="Yes", exact=True), "Confirmation Yes action")
    exactly_one(confirmation.get_by_role("button", name="No", exact=True), "Confirmation No action")

    input_box = exactly_one(page.get_by_role("region", name="Input box", exact=True), "Input box region")
    hostname = exactly_one(input_box.get_by_role("textbox", name="Hostname", exact=True), "Hostname textbox")
    require(hostname.input_value() == "homeserver.local", "hostname input value changed unexpectedly")

    menu = exactly_one(page.get_by_role("region", name="Menu", exact=True), "Menu region")
    actions = exactly_one(menu.get_by_role("group", name="Available actions", exact=True), "Available actions group")
    exactly_one(actions.get_by_role("button", name="View service status", exact=True), "View service status action")
    unavailable_action = exactly_one(
        actions.get_by_role("button", name="Install optional plugin", exact=True),
        "disabled optional-plugin action",
    )
    exactly_one(
        actions.get_by_role("button", name="Restart selected services", exact=True),
        "Restart selected services action",
    )
    exactly_one(
        actions.get_by_role("button", name="Open configuration", exact=True),
        "Open configuration action",
    )
    require(unavailable_action.is_disabled(), "disabled menu action lost native disabled state")

    radio_region = exactly_one(page.get_by_role("region", name="Radiolist", exact=True), "Radiolist region")
    startup = exactly_one(radio_region.get_by_role("radiogroup", name="Startup mode", exact=True), "Startup mode radiogroup")
    safe = exactly_one(startup.get_by_role("radio", name="Safe mode", exact=True), "Safe mode radio")
    normal = exactly_one(startup.get_by_role("radio", name="Normal mode", exact=True), "Normal mode radio")
    performance = exactly_one(startup.get_by_role("radio", name="Performance mode", exact=True), "Performance mode radio")
    require(safe.is_checked(), "Safe mode radio lost selected state")
    require(not normal.is_checked(), "Normal mode radio unexpectedly selected")
    require(performance.is_disabled(), "Performance mode radio lost disabled state")

    checklist_region = exactly_one(page.get_by_role("region", name="Checklist", exact=True), "Checklist region")
    checklist = exactly_one(
        checklist_region.get_by_role("group", name="Services to restart", exact=True),
        "dialog services checklist group",
    )
    nginx = exactly_one(checklist.get_by_role("checkbox", name="nginx.service", exact=True), "nginx checkbox")
    legacy = exactly_one(checklist.get_by_role("checkbox", name="legacy.service", exact=True), "legacy checkbox")
    require(nginx.is_checked(), "nginx checkbox lost checked state")
    require(legacy.is_disabled(), "legacy checkbox lost disabled state")

    gauge = exactly_one(page.get_by_role("region", name="Gauge", exact=True), "Gauge region")
    progress = exactly_one(
        gauge.get_by_role("progressbar", name="Installing packages", exact=True),
        "Installing packages progressbar",
    )
    native_progress = progress.evaluate(
        """
        (element) => ({
          tag: element.tagName,
          value: element.value,
          max: element.max,
        })
        """
    )
    require(native_progress == {"tag": "PROGRESS", "value": 65, "max": 100}, f"unexpected progress semantics: {native_progress!r}")


def verify_touch_semantics(page: Page) -> None:
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
    verify_package_semantics(page)


def new_context(browser: Browser, case: AccessibilityCase):
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


def run_case(browser: Browser, base_url: str, case: AccessibilityCase) -> None:
    context = new_context(browser, case)
    page: Page | None = None
    try:
        page = context.new_page()
        page.goto(f"{base_url}{case.path}", wait_until="networkidle")
        if case.kind == "package":
            verify_package_semantics(page)
        elif case.kind == "dialogs":
            verify_dialogs_semantics(page)
        elif case.kind == "package-touch":
            verify_touch_semantics(page)
        else:
            raise AssertionError(f"unknown accessibility case kind: {case.kind}")
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
        description="Verify web-tui-kit browser accessibility semantics."
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
        print("\nAccessibility semantic regression failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
