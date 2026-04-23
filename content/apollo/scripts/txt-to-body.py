#!/usr/bin/env python3
"""
Transform a pdftotext -layout .txt dump into a clean markdown body.

Line-by-line approach:
- Skip boilerplate (MOA header, pagination, watermarks, TOC bullets, standalone page numbers)
- Strip trailing "- SECTION NAME" suffix from lines (all-caps after last " - ")
- Collapse excess blank lines + intra-paragraph padding
- Leave content + headings as markdown paragraphs

Usage:
    python3 txt-to-body.py <input.txt> [output.md]
"""
import re
import sys
from pathlib import Path


ALL_CAPS_SUFFIX = re.compile(r"^(.+?)\s+-\s+([A-Z][A-Z\s\-/&]+)$")


def is_boilerplate(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    # "MEN OF APOLLO" top banner
    if s == "MEN OF APOLLO":
        return True
    # "MOA NN: TITLE" line (including continuations like "INITIATION")
    if re.match(r"^MOA \d+:", s):
        return True
    # "Course Notes — Personal Reference"
    if s.startswith("Course Notes"):
        return True
    # "Total Lessons: N | Date: ... | Source: ..."
    if s.startswith("Total Lessons:"):
        return True
    # PERSONAL USE ONLY watermark (variably spaced)
    if re.sub(r"\s+", "", s).upper() == "PERSONALUSEONLY":
        return True
    # Pagination footer
    if re.match(r"^Men of Apollo\s*[—-]\s*Personal Notes\s*\d*$", s):
        return True
    # Contents header
    if s == "Contents":
        return True
    # "Module NN of 20 • N lessons extracted"
    if re.match(r"^Module \d+ of 20\s*•\s*\d+ lessons extracted\s*$", s):
        return True
    # TOC bullet lines (bullet point + dash + suffix)
    if re.match(r"^•\s+.+\s+-\s+[A-Z][A-Z\s\-/&]+\s*$", s):
        return True
    # Standalone page number
    if re.match(r"^\d{1,3}$", s):
        return True
    # Stranded all-caps continuation lines (pdf title wraps).
    # Allow: 1-3 words, all uppercase letters only (plus spaces), no punctuation.
    # This catches "INITIATION", "SYSTEM", "FRAMEWORK" etc. that are orphaned from their module title.
    # Preserves legit headers like "WEEK 1: RESET + RHYTHM" (has colon/plus → not matched).
    if re.match(r"^[A-Z]{2,}(?: [A-Z]{2,}){0,2}$", s):
        return True
    return False


def strip_caps_suffix(line: str) -> str:
    """Strip trailing ' - SECTION NAME' where section name is all caps."""
    s = line.rstrip()
    m = ALL_CAPS_SUFFIX.match(s)
    if m:
        # Check if suffix is all caps (allowing spaces, dashes, slashes, ampersands)
        suffix = m.group(2)
        if suffix.replace(" ", "").replace("-", "").replace("/", "").replace("&", "").isupper():
            base = m.group(1).rstrip()
            # Recurse in case of nested caps suffixes
            return strip_caps_suffix(base)
    return s


def clean(text: str) -> str:
    lines = text.splitlines()
    out = []
    for raw in lines:
        # Normalise any unicode non-breaking spaces
        line = raw.replace("\u00a0", " ")
        if is_boilerplate(line):
            continue
        line = strip_caps_suffix(line)
        # Collapse runs of 4+ spaces inside a line (pdftotext padding)
        line = re.sub(r"(?<=\S) {4,}(?=\S)", " ", line)
        out.append(line)

    text = "\n".join(out)
    # Collapse 3+ newlines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = Path(sys.argv[1])
    raw = src.read_text()
    cleaned = clean(raw)
    if len(sys.argv) >= 3:
        Path(sys.argv[2]).write_text(cleaned)
    else:
        sys.stdout.write(cleaned)


if __name__ == "__main__":
    main()
