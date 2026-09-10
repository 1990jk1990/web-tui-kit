from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "ai-doc-1.yaml",
    "mkdocs.yml",
    "docs/index.md",
    "docs/project/overview.md",
    "docs/project/getting-started.md",
    "docs/project/development.md",
    "docs/project/technology-stack.md",
    "docs/project/testing.md",
    "docs/architecture/01-introduction-and-goals.md",
    "docs/architecture/04-solution-strategy.md",
    "docs/architecture/05-building-block-view.md",
    "docs/architecture/09-architecture-decisions.md",
    "docs/decisions/0000-template.md",
    "openspec/specs/web-tui-kit/spec.md",
    "tests/test_repository.py",
    ".github/workflows/ai-doc-1.yml",
]

missing = [path for path in REQUIRED if not (ROOT / path).exists()]
if missing:
    print("AI-DOC-1 core files missing:")
    for path in missing:
        print(f" - {path}")
    sys.exit(1)

for forbidden in ("AI_NOTES.md", "CHATGPT_CONTEXT.md", "CURRENT_AI_CONTEXT.md"):
    if (ROOT / forbidden).exists():
        print(f"Forbidden parallel AI context file detected: {forbidden}")
        sys.exit(1)

manifest = (ROOT / "ai-doc-1.yaml").read_text(encoding="utf-8")
if 'version: "1.3"' not in manifest:
    print("ai-doc-1.yaml does not declare AI-DOC-1 v1.3")
    sys.exit(1)

print("AI-DOC-1 structural validation passed.")
