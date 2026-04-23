#!/usr/bin/env bash
# Extracts the 20 MOA_NN_*.pdf files from ~/Downloads into content/apollo/source-pdfs/,
# canonicalising any "(2)" duplicates (treat as newer), then runs pdftotext -layout on each.
#
# Prerequisite: poppler-utils. Install via `brew install poppler`.
#
# Run from anywhere:
#   bash content/apollo/scripts/extract-moa-pdfs.sh

set -euo pipefail

SRC="$HOME/Downloads"
DST="$(cd "$(dirname "$0")/.." && pwd)/source-pdfs"
mkdir -p "$DST"

if ! command -v pdftotext >/dev/null 2>&1; then
  echo "pdftotext not found. Install poppler: brew install poppler" >&2
  exit 1
fi

copied=0
for n in $(seq -w 1 20); do
  latest="$(ls "$SRC"/MOA_${n}_*.pdf 2>/dev/null | sort | tail -1 || true)"
  if [[ -n "${latest:-}" ]]; then
    cp "$latest" "$DST/"
    copied=$((copied+1))
  else
    echo "warn: no PDF matched MOA_${n}_*.pdf in $SRC" >&2
  fi
done
echo "Copied $copied PDFs to $DST"

extracted=0
for f in "$DST"/MOA_*.pdf; do
  [[ -e "$f" ]] || continue
  base="$(basename "$f" .pdf)"
  pdftotext -layout "$f" "$DST/${base}.txt"
  extracted=$((extracted+1))
done
echo "Extracted $extracted PDFs to .txt"
