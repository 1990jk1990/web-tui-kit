#!/usr/bin/env python3
from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import subprocess
import threading

from playwright.sync_api import Page, expect, sync_playwright


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "test-results" / "framework"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return


class VerificationServer(ThreadingHTTPServer):
    daemon_threads = True


def build_fixtures() -> None:
    subprocess.run(
        ["npm", "--prefix", str(ROOT / "tests" / "framework"), "run", "build-fixtures"],
        cwd=ROOT,
        check=True,
        timeout=60,
    )


def start_server():
    handler = partial(QuietHandler, directory=str(ROOT))
    server = VerificationServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def load_recipe(page: Page, url: str) -> None:
    page.set_default_timeout(5_000)
    page.set_default_navigation_timeout(10_000)
    page.goto(url, wait_until="load")


def activate_labeled_checkbox(checkbox) -> None:
    # Canonical TUI checkboxes visually hide the native input beneath the label.
    # Click the associated label so the browser performs normal label/input activation.
    checkbox.locator("xpath=ancestor::label[1]").click()


def assert_framework_recipe(page: Page, url: str, case_name: str) -> None:
    load_recipe(page, url)

    expect(page.get_by_role("heading", name="Package configuration")).to_be_visible()
    expect(page.get_by_role("group", name="Services to restart")).to_be_visible()

    accounts = page.get_by_role("checkbox", name="accounts-daemon.service")
    apache = page.get_by_role("checkbox", name="apache2.service")
    cron = page.get_by_role("checkbox", name="cron.service")
    ssh = page.get_by_role("checkbox", name="ssh.service")

    expect(accounts).to_be_checked()
    expect(apache).not_to_be_checked()
    expect(cron).to_be_checked()
    expect(ssh).to_be_checked()

    accounts.focus()
    page.keyboard.press("ArrowDown")
    expect(apache).to_be_focused()

    activate_labeled_checkbox(apache)
    expect(apache).to_be_checked()

    page.keyboard.press("Escape")
    events = page.evaluate("window.__frameworkEvents")
    assert events and events[-1]["type"] == "cancel", f"{case_name}: Escape did not reach application cancel handler"

    page.get_by_role("button", name="Ok").click()
    events = page.evaluate("window.__frameworkEvents")
    accepts = [event for event in events if event.get("type") == "accept"]
    assert accepts, f"{case_name}: accept callback/event was not observed"
    assert accepts[-1]["services"] == [
        "accounts-daemon.service",
        "apache2.service",
        "cron.service",
        "ssh.service",
    ], f"{case_name}: accept payload did not preserve native checkbox state"


def assert_server_rendered_recipe(page: Page, url: str) -> None:
    load_recipe(page, url)

    expect(page.get_by_role("heading", name="Package configuration")).to_be_visible()
    accounts = page.get_by_role("checkbox", name="accounts-daemon.service")
    apache = page.get_by_role("checkbox", name="apache2.service")

    expect(accounts).to_be_checked()
    expect(apache).not_to_be_checked()

    accounts.focus()
    page.keyboard.press("ArrowDown")
    expect(apache).to_be_focused()
    activate_labeled_checkbox(apache)
    expect(apache).to_be_checked()

    page.keyboard.press("Escape")
    expect(page.locator("#recipe-status")).to_contain_text("Application received tui:escape")

    selected = page.locator("form").evaluate(
        "form => new FormData(form).getAll('services')",
    )
    assert selected == [
        "accounts-daemon.service",
        "apache2.service",
        "cron.service",
        "ssh.service",
    ], "server-rendered recipe did not preserve ordinary form selection semantics"


def run() -> None:
    parser = argparse.ArgumentParser(description="Verify framework/template consumption recipes in Chromium")
    parser.add_argument("--skip-build", action="store_true", help="Use already-built test-results/framework fixtures")
    args = parser.parse_args()

    if not args.skip_build:
        print("BUILD framework fixtures", flush=True)
        build_fixtures()

    RESULTS.mkdir(parents=True, exist_ok=True)
    server, thread = start_server()
    base_url = f"http://127.0.0.1:{server.server_address[1]}"

    cases = [
        ("react", f"{base_url}/test-results/framework/react.html", assert_framework_recipe),
        ("vue", f"{base_url}/test-results/framework/vue.html", assert_framework_recipe),
        ("server-rendered", f"{base_url}/examples/server-rendered/package-configuration.html", assert_server_rendered_recipe),
    ]

    failures: list[str] = []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            try:
                for case_name, url, assertion in cases:
                    print(f"RUN {case_name}", flush=True)
                    page = browser.new_page(viewport={"width": 1280, "height": 800})
                    try:
                        if assertion is assert_framework_recipe:
                            assertion(page, url, case_name)
                        else:
                            assertion(page, url)
                        print(f"PASS {case_name}", flush=True)
                    except Exception as exc:
                        failures.append(f"{case_name}: {exc}")
                        page.screenshot(path=str(RESULTS / f"{case_name}-failure.png"), full_page=True)
                    finally:
                        page.close()
            finally:
                browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    if failures:
        raise SystemExit("\n".join(failures))


if __name__ == "__main__":
    run()
