#!/usr/bin/env python3
"""
Rebuild each module markdown file to: frontmatter + verbatim cleaned body only.

Preserves the existing YAML frontmatter (module_id, slug, title, phase, tier,
lede, next_step, etc.) and replaces everything after the closing `---` with
the cleaned body from /content/apollo/source-pdfs/bodies/MOA_NN_*.md.

Removes the editorial sections (## Summary, ## Content map, ## Frameworks /
protocols, ## Visual callouts, ## Full body) that were scaffolded during
module authoring. Stefan's intent is a word-for-word extraction — the cleaned
body IS the module content.

Usage:
    python3 rebuild-modules.py
"""
import re
from pathlib import Path

APOLLO = Path(__file__).resolve().parent.parent
MODULES_DIR = APOLLO / "modules"
BODIES_DIR = APOLLO / "source-pdfs" / "bodies"


def load_body(num: str) -> str:
    candidates = list(BODIES_DIR.glob(f"MOA_{num}_*.md"))
    if not candidates:
        raise SystemExit(f"No body file found for MOA_{num}")
    return candidates[0].read_text()


def rebuild(mod_file: Path) -> str:
    m = re.match(r"module-(\d+)-", mod_file.name)
    if not m:
        return f"skip (not a module file): {mod_file.name}"
    num = m.group(1)

    content = mod_file.read_text()
    if not content.startswith("---\n"):
        return f"skip (no frontmatter): {mod_file.name}"

    # Split on "\n---\n" to grab the YAML block
    # content is: "---\n<yaml>\n---\n<rest>"
    after_open = content[len("---\n"):]
    close_idx = after_open.find("\n---\n")
    if close_idx == -1:
        return f"skip (no closing frontmatter delimiter): {mod_file.name}"
    frontmatter = after_open[:close_idx]

    body = load_body(num).rstrip() + "\n"

    new = f"---\n{frontmatter}\n---\n\n{body}"
    mod_file.write_text(new)
    return f"rebuilt {mod_file.name} ({len(new)} bytes, body {len(body)} bytes)"


def main() -> None:
    for mod_file in sorted(MODULES_DIR.glob("module-*.md")):
        print(rebuild(mod_file))


if __name__ == "__main__":
    main()
