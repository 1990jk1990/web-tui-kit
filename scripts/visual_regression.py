from __future__ import annotations

import argparse
from dataclasses import dataclass
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading

from PIL import Image, ImageChops, ImageEnhance
from playwright.sync_api import Browser, Page, sync_playwright


ROOT = Path(__file__).resolve().parents[1]
BASELINE_DIR = ROOT / "tests" / "visual" / "baselines"
RESULT_DIR = ROOT / "test-results" / "visual"


@dataclass(frozen=True)
class VisualCase:
    name: str
    path: str
    width: int
    height: int
    full_page: bool
    mobile: bool = False


CASES = (
    VisualCase("package-desktop", "/demo/index.html", 1280, 800, False),
    VisualCase("package-mobile", "/demo/index.html", 390, 844, True, True),
    VisualCase("dialogs-desktop", "/demo/dialogs.html", 1280, 1000, True),
    VisualCase("dialogs-mobile", "/demo/dialogs.html", 390, 844, True, True),
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


def prepare_page(page: Page, base_url: str, case: VisualCase) -> None:
    page.goto(f"{base_url}{case.path}", wait_until="networkidle")
    page.emulate_media(color_scheme="light", reduced_motion="reduce")
    page.evaluate("document.fonts.ready")
    page.add_style_tag(
        content="""
          *, *::before, *::after {
            animation: none !important;
            transition: none !important;
            scroll-behavior: auto !important;
            caret-color: transparent !important;
          }
        """
    )


def capture(browser: Browser, base_url: str, case: VisualCase, destination: Path) -> None:
    context = browser.new_context(
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
    try:
        page = context.new_page()
        prepare_page(page, base_url, case)
        destination.parent.mkdir(parents=True, exist_ok=True)
        page.screenshot(
            path=str(destination),
            full_page=case.full_page,
            animations="disabled",
        )
    finally:
        context.close()


def compare_images(expected_path: Path, actual_path: Path, diff_path: Path) -> tuple[int, float]:
    with Image.open(expected_path) as expected_image, Image.open(actual_path) as actual_image:
        expected = expected_image.convert("RGBA")
        actual = actual_image.convert("RGBA")

        if expected.size != actual.size:
            diff_path.parent.mkdir(parents=True, exist_ok=True)
            canvas = Image.new(
                "RGBA",
                (max(expected.width, actual.width), max(expected.height, actual.height)),
                (255, 255, 255, 255),
            )
            canvas.alpha_composite(actual, (0, 0))
            canvas.save(diff_path)
            return max(expected.width * expected.height, actual.width * actual.height), 1.0

        diff = ImageChops.difference(expected, actual)
        changed_pixels = sum(
            1 for pixel in diff.getdata() if max(pixel[0], pixel[1], pixel[2]) > 8
        )
        total_pixels = expected.width * expected.height
        ratio = changed_pixels / total_pixels if total_pixels else 0.0

        if changed_pixels:
            diff_path.parent.mkdir(parents=True, exist_ok=True)
            visible_diff = ImageEnhance.Contrast(diff.convert("RGB")).enhance(4.0)
            visible_diff.save(diff_path)

        return changed_pixels, ratio


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Capture or verify canonical web-tui-kit visual baselines."
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="Replace the reviewed baseline screenshots with the current render.",
    )
    parser.add_argument(
        "--max-diff-ratio",
        type=float,
        default=0.0001,
        help="Maximum ratio of pixels allowed to differ by more than 8 channel values.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    RESULT_DIR.mkdir(parents=True, exist_ok=True)

    server, thread = start_server()
    base_url = f"http://127.0.0.1:{server.server_port}"
    failures: list[str] = []

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                headless=True,
                args=["--font-render-hinting=none"],
            )
            try:
                for case in CASES:
                    baseline_path = BASELINE_DIR / f"{case.name}.png"
                    if args.update:
                        capture(browser, base_url, case, baseline_path)
                        print(f"UPDATED {case.name}: {baseline_path.relative_to(ROOT)}")
                        continue

                    actual_path = RESULT_DIR / f"{case.name}-actual.png"
                    diff_path = RESULT_DIR / f"{case.name}-diff.png"
                    capture(browser, base_url, case, actual_path)

                    if not baseline_path.exists():
                        failures.append(
                            f"{case.name}: missing baseline {baseline_path.relative_to(ROOT)}"
                        )
                        print(f"FAIL {failures[-1]}")
                        continue

                    changed_pixels, ratio = compare_images(
                        baseline_path, actual_path, diff_path
                    )
                    if ratio > args.max_diff_ratio:
                        failures.append(
                            f"{case.name}: {changed_pixels} pixels changed "
                            f"({ratio:.6%} > {args.max_diff_ratio:.6%})"
                        )
                        print(f"FAIL {failures[-1]}")
                    else:
                        actual_path.unlink(missing_ok=True)
                        diff_path.unlink(missing_ok=True)
                        print(
                            f"PASS {case.name}: {changed_pixels} changed pixels "
                            f"({ratio:.6%})"
                        )
            finally:
                browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    if failures:
        print("\nVisual regression failures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
