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


SUFFIX_PATTERN = re.compile(r"^(.+?)\s+-\s+([A-Z][A-Za-z0-9\s\-/&()]+)$")
CONNECTOR_WORDS = {"and", "of", "the", "in", "for", "on", "to", "a", "an", "with", "or", "&"}


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
    # TOC bullet lines — bullet + " - " + suffix that starts uppercase (ALL CAPS or Title Case).
    # Length-capped to avoid accidentally stripping prose bullets that happen to use "X - Y Z".
    if re.match(r"^•\s+[A-Z].+\s+-\s+[A-Z][A-Za-z0-9\s\-/&()]+\s*$", s) and len(s) < 120:
        return True
    # Standalone (ALLCAPS) parenthesised label — e.g. "(FOUNDATIONS)"
    if re.match(r"^\(\s*[A-Z][A-Z0-9\s\-/&]+\s*\)\s*$", s):
        return True
    # Standalone page number
    if re.match(r"^\d{1,3}$", s):
        return True
    # Stranded all-caps title fragments (pdf wraps, header decorations).
    # No lowercase, under 60 chars, only caps/digits/parens/dashes/slashes/ampersands/spaces.
    # Catches: "INITIATION", "FRAMEWORK (FOUNDATIONS)", "APOLLO NUTRITION FRAMEWORK",
    # "INITIATION WEEK 1", "PHASE 2 INTEGRATION" when stranded.
    # Preserves legit headers like "WEEK 1: RESET + RHYTHM" (has ":" and "+" → not matched).
    if (
        len(s) <= 60
        and re.match(r"^[A-Z0-9(]+(?:[\s()&\-/][A-Z0-9()]+)*$", s)
        and not any(c.islower() for c in s)
        and any(c.isalpha() for c in s)
    ):
        return True
    return False


def is_title_or_caps_suffix(suffix: str) -> bool:
    """Return True if suffix is ALL CAPS or Title Case — i.e. a module/section name.

    Permissive test: each word starts uppercase OR is a common connector word ("and", "of"...).
    Rejects prose that just happens to start with a capital, because prose contains multiple
    lowercase non-connector words in sequence.
    """
    # Quick accept: no lowercase at all
    if not any(c.islower() for c in suffix):
        return any(c.isupper() for c in suffix)
    # Title-Case check: split on whitespace + common separators
    words = [w for w in re.split(r"[\s/()&\-]+", suffix) if w]
    if not words or len(words) > 8:
        return False
    for w in words:
        if w.lower() in CONNECTOR_WORDS:
            continue
        if not w[0].isupper():
            return False
    return True


def strip_caps_suffix(line: str) -> str:
    """Strip trailing ' - Module Or Section Name' suffix (ALL CAPS or Title Case)."""
    s = line.rstrip()
    m = SUFFIX_PATTERN.match(s)
    if m and is_title_or_caps_suffix(m.group(2)):
        base = m.group(1).rstrip()
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
