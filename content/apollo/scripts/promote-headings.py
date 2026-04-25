#!/usr/bin/env python3
"""
promote-headings.py — Add markdown heading markers to plain-text section titles
in Apollo module files. Surgical: only matching lines get prefixed with `## ` or
`### `; no other content is touched.

Usage:
    python3 promote-headings.py <module_path> <config_path>

config_path is a JSON file with shape:
    {
      "h2": ["Section title 1", "Section title 2", ...],
      "h3": ["Sub-heading 1", "Sub-heading 2", ...]
    }

Each entry must match a full line in the module file exactly (no leading or
trailing whitespace, no partial matches). The script prepends `## ` to every h2
match and `### ` to every h3 match, in place. Lines that already start with `#`
are skipped. Missing matches are reported on stderr but don't abort.
"""
import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: promote-headings.py <module_path> <config_path>", file=sys.stderr)
        return 2

    module_path = Path(sys.argv[1])
    config_path = Path(sys.argv[2])

    config = json.loads(config_path.read_text())
    h2_titles = set(config.get("h2", []))
    h3_titles = set(config.get("h3", []))

    overlap = h2_titles & h3_titles
    if overlap:
        print(f"ERROR: h2/h3 overlap: {overlap}", file=sys.stderr)
        return 1

    text = module_path.read_text()
    lines = text.split("\n")

    h2_hits = {t: 0 for t in h2_titles}
    h3_hits = {t: 0 for t in h3_titles}

    for i, line in enumerate(lines):
        if line.startswith("#"):
            continue
        if line in h2_titles:
            lines[i] = "## " + line
            h2_hits[line] += 1
        elif line in h3_titles:
            lines[i] = "### " + line
            h3_hits[line] += 1
        # NOTE: no break — promote ALL matching lines for the same title.
        # If a title legitimately appears twice (e.g. "The Structure:" used in
        # multiple sections), both should become headings.

    module_path.write_text("\n".join(lines))

    missing_h2 = [t for t, c in h2_hits.items() if c == 0]
    missing_h3 = [t for t, c in h3_hits.items() if c == 0]
    duplicate_h2 = [t for t, c in h2_hits.items() if c > 1]
    duplicate_h3 = [t for t, c in h3_hits.items() if c > 1]

    if missing_h2:
        print(f"WARN: h2 not found: {missing_h2}", file=sys.stderr)
    if missing_h3:
        print(f"WARN: h3 not found: {missing_h3}", file=sys.stderr)
    if duplicate_h2:
        print(f"WARN: h2 matched multiple times: {duplicate_h2}", file=sys.stderr)
    if duplicate_h3:
        print(f"WARN: h3 matched multiple times: {duplicate_h3}", file=sys.stderr)

    h2_count = sum(1 for c in h2_hits.values() if c > 0)
    h3_count = sum(1 for c in h3_hits.values() if c > 0)
    print(f"OK: {h2_count} h2 + {h3_count} h3 promoted in {module_path.name}")
    return 0 if not (missing_h2 or missing_h3 or duplicate_h2 or duplicate_h3) else 1


if __name__ == "__main__":
    sys.exit(main())
