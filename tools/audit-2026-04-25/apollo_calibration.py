#!/usr/bin/env python3
"""Phase 1 calibration on apollo-reviews-export.csv. Read-only."""
import csv
import re
from collections import Counter, defaultdict

SRC = "/Users/antonurso/Downloads/apollo-reviews-export.csv"

with open(SRC, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print(f"=== Row count: {len(rows)} ===\n")

# 1. Em-dash count per column
em_long = sum(1 for r in rows if "—" in (r.get("quote_long") or ""))
em_short = sum(1 for r in rows if "—" in (r.get("quote_short") or ""))
em_headline = sum(1 for r in rows if "—" in (r.get("internal_headline_draft") or ""))
em_outcome = sum(1 for r in rows if "—" in (r.get("internal_outcome_metric") or ""))
print(f"Em-dash rows in quote_long: {em_long}")
print(f"Em-dash rows in quote_short: {em_short}")
print(f"Em-dash rows in internal_headline_draft: {em_headline}")
print(f"Em-dash rows in internal_outcome_metric: {em_outcome}\n")

# 2. Semicolon count
semi_long = sum(1 for r in rows if ";" in (r.get("quote_long") or ""))
print(f"Semicolon rows in quote_long: {semi_long}\n")

# 3. Date clustering
dates = Counter(r["date_received"] for r in rows)
clustered = [(d, c) for d, c in dates.items() if c >= 4]
clustered.sort(key=lambda x: -x[1])
print(f"=== Dates with >=4 reviews ({len(clustered)} dates) ===")
for d, c in clustered[:20]:
    print(f"  {d}: {c}")
print()

# 4. Verified status
ver = Counter(r["verified_status"] for r in rows)
print(f"verified_status distribution: {dict(ver)}\n")

# 5. Rating distribution
rat = Counter(r["rating_1_5"] for r in rows)
print(f"rating_1_5 distribution: {dict(sorted(rat.items()))}\n")

# 6. Product tag distribution
prod = Counter(r["internal_product_tag"] for r in rows)
print("internal_product_tag distribution:")
for p, c in sorted(prod.items(), key=lambda x: -x[1]):
    print(f"  {p}: {c}")
print()

# 7. Sentence-level repetition in quote_long
sentence_re = re.compile(r"(?<=[.!?])\s+")
sent_counter = Counter()
for r in rows:
    q = (r.get("quote_long") or "").strip()
    for s in sentence_re.split(q):
        s = s.strip().strip("\"'")
        if 5 <= len(s) <= 120:
            sent_counter[s] += 1

print("=== Top 40 repeated sentences in quote_long (count >= 3) ===")
for s, c in sent_counter.most_common(40):
    if c >= 3:
        print(f"  {c:3d}× {s}")
print()

# 8. Phrase-level repetition (3-7 word ngrams)
def ngrams(text, n_min=4, n_max=8):
    words = re.findall(r"[A-Za-z']+", text.lower())
    for n in range(n_min, n_max+1):
        for i in range(len(words)-n+1):
            yield " ".join(words[i:i+n])

ng_counter = Counter()
for r in rows:
    q = (r.get("quote_long") or "")
    for ng in ngrams(q, 5, 6):
        ng_counter[ng] += 1

print("=== Top 30 repeated 5-6 word phrases (count >= 8) ===")
for ng, c in ng_counter.most_common(60):
    if c >= 8 and len(ng.split()) >= 5:
        print(f"  {c:3d}× {ng}")
print()

# 9. Headline / quote / metric coherence — flag rows where outcome_metric not in quote_long
print("=== Rows where internal_outcome_metric is NOT a substring of quote_long (likely template-assembly tells) ===")
mismatch_count = 0
mismatch_examples = []
for r in rows:
    q = (r.get("quote_long") or "").lower()
    om = (r.get("internal_outcome_metric") or "").strip().lower()
    if om and om not in q:
        mismatch_count += 1
        if len(mismatch_examples) < 15:
            mismatch_examples.append(f"  {r['id']} ({r['name_display']}): metric=\"{r['internal_outcome_metric']}\" | quote starts: \"{(r['quote_long'] or '')[:80]}...\"")
print(f"Mismatch count: {mismatch_count}/{len(rows)}")
for ex in mismatch_examples:
    print(ex)
print()

# 10. Quote_short verbatim within quote_long check
in_long = 0
not_in_long = []
for r in rows:
    qs = (r.get("quote_short") or "").strip()
    ql = (r.get("quote_long") or "").strip()
    if qs and qs in ql:
        in_long += 1
    elif qs:
        not_in_long.append(r['id'])
print(f"quote_short found verbatim in quote_long: {in_long}/{len(rows)}")
if not_in_long:
    print(f"  Exceptions ({len(not_in_long)}): {not_in_long[:15]}")
print()

# 11. Name reuse — are there many "different" reviewers with the same first name?
names = Counter(r["name_display"] for r in rows)
print("=== Name reuses (>=3 instances) ===")
for n, c in names.most_common(30):
    if c >= 3:
        print(f"  {c}× {n}")
print()

# 12. internal_source_status distribution
iss = Counter(r["internal_source_status"] for r in rows)
print(f"internal_source_status distribution: {dict(iss)}")
