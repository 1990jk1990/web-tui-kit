from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import zipfile


ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "VERSION"
VERSION_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")

DISTRIBUTION_FILES = (
    "VERSION",
    "README.md",
    "DESIGN_SYSTEM.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "SECURITY.md",
    "docs/project/framework-integration.md",
    "src/tokens.css",
    "src/tui.css",
    "src/tui.js",
    "demo/index.html",
    "demo/dialogs.html",
    "demo/components.html",
    "examples/README.md",
    "examples/react/PackageConfiguration.jsx",
    "examples/vue/PackageConfiguration.vue",
    "examples/server-rendered/package-configuration.html",
)

FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
FILE_MODE = 0o100644 << 16


def read_version() -> str:
    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not VERSION_RE.fullmatch(version):
        raise ValueError(f"VERSION is not a plain Semantic Version: {version!r}")
    return version


def normalize_expected_version(value: str) -> str:
    normalized = value[1:] if value.startswith("v") else value
    if not VERSION_RE.fullmatch(normalized):
        raise ValueError(f"expected version is not vMAJOR.MINOR.PATCH/MAJOR.MINOR.PATCH: {value!r}")
    return normalized


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def write_member(archive: zipfile.ZipFile, source: Path, archive_name: str) -> None:
    info = zipfile.ZipInfo(archive_name, date_time=FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = FILE_MODE
    info.create_system = 3
    archive.writestr(info, source.read_bytes())


def build_release(output_dir: Path, expected_version: str | None = None) -> tuple[Path, Path]:
    version = read_version()
    if expected_version is not None:
        expected = normalize_expected_version(expected_version)
        if expected != version:
            raise ValueError(f"tag/version mismatch: expected {expected}, VERSION contains {version}")

    missing = [path for path in DISTRIBUTION_FILES if not (ROOT / path).is_file()]
    if missing:
        raise FileNotFoundError(f"release inputs are missing: {', '.join(missing)}")

    output_dir.mkdir(parents=True, exist_ok=True)
    package_root = f"web-tui-kit-{version}"
    archive_path = output_dir / f"{package_root}.zip"
    checksum_path = output_dir / f"{package_root}.zip.sha256"

    with zipfile.ZipFile(archive_path, "w") as archive:
        for relative_path in sorted(DISTRIBUTION_FILES):
            write_member(
                archive,
                ROOT / relative_path,
                f"{package_root}/{relative_path}",
            )

    checksum_path.write_text(
        f"{sha256(archive_path)}  {archive_path.name}\n",
        encoding="utf-8",
        newline="\n",
    )
    return archive_path, checksum_path


def validate_release(archive_path: Path, version: str) -> None:
    package_root = f"web-tui-kit-{version}"
    expected = {f"{package_root}/{path}" for path in DISTRIBUTION_FILES}

    with zipfile.ZipFile(archive_path, "r") as archive:
        names = set(archive.namelist())
        if names != expected:
            missing = sorted(expected - names)
            extra = sorted(names - expected)
            raise ValueError(f"release archive contents mismatch; missing={missing}, extra={extra}")

        version_bytes = archive.read(f"{package_root}/VERSION")
        if version_bytes.decode("utf-8").strip() != version:
            raise ValueError("VERSION inside release archive does not match package version")

        for info in archive.infolist():
            if info.date_time != FIXED_ZIP_TIME:
                raise ValueError(f"non-deterministic timestamp in {info.filename}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the deterministic web-tui-kit distribution ZIP.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "dist",
        help="Directory for the release ZIP and SHA-256 checksum.",
    )
    parser.add_argument(
        "--version",
        help="Expected release version or tag (for example 0.4.0 or v0.4.0).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Build twice and fail if the resulting ZIP bytes are not deterministic.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    version = read_version()
    archive_path, checksum_path = build_release(args.output_dir, args.version)
    validate_release(archive_path, version)

    if args.check:
        first_digest = sha256(archive_path)
        archive_path, checksum_path = build_release(args.output_dir, args.version)
        validate_release(archive_path, version)
        second_digest = sha256(archive_path)
        if first_digest != second_digest:
            raise RuntimeError("release archive is not deterministic across consecutive builds")

    print(f"Built {display_path(archive_path)}")
    print(f"SHA256 {sha256(archive_path)}")
    print(f"Checksum {display_path(checksum_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
