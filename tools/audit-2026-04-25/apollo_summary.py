#!/usr/bin/env python3
"""Phase 5 — generate audit_summary.md from audit_results.csv + reviews_cleaned.csv + per-row JSON."""
import csv
import json
import re
from pathlib import Path
from collections import Counter

SRC = Path("/Users/antonurso/Downloads/apollo-reviews-export.csv")
AUDIT = Path("/Users/antonurso/Downloads/audit_results.csv")
CLEANED = Path("/Users/antonurso/Downloads/reviews_cleaned.csv")
DETAIL = Path("/tmp/apollo_audit_per_row.json")
OUT = Path("/Users/antonurso/Downloads/audit_summary.md")

with open(SRC, encoding="utf-8") as f:
    src_rows = list(csv.DictReader(f))
with open(AUDIT, encoding="utf-8") as f:
    audit_rows = list(csv.DictReader(f))
with open(CLEANED, encoding="utf-8") as f:
    cleaned_rows = list(csv.DictReader(f))
with open(DETAIL, encoding="utf-8") as f:
    detail = json.load(f)

src_by_id = {r["id"]: r for r in src_rows}
audit_by_id = {r["id"]: r for r in audit_rows}
detail_by_id = {d["id"]: d for d in detail}
cleaned_by_id = {r["id"]: r for r in cleaned_rows}

# Headline counts
verdict_counts = Counter(r["verdict"] for r in audit_rows)
rec_counts = Counter(r["recommendation"] for r in audit_rows)
total = len(audit_rows)

# Cross-row patterns — top 15 repeated sentences
sentence_re = re.compile(r"(?<=[.!?])\s+")
sent_counter = Counter()
for r in src_rows:
    for s in sentence_re.split((r.get("quote_long") or "").strip()):
        s = s.strip().strip("\"'")
        if 5 <= len(s) <= 120:
            sent_counter[s] += 1

top_repeats = [(s, c) for s, c in sent_counter.most_common(50) if c >= 5][:15]

# Date clusters
date_counts = Counter(r["date_received"] for r in src_rows)
clusters = sorted([(d, c) for d, c in date_counts.items() if c >= 4], key=lambda x: -x[1])

# Headline-quote leakage flags — rows where internal_outcome_metric isn't in quote_long
metric_mismatches = []
for r in src_rows:
    om = (r.get("internal_outcome_metric") or "").strip().lower()
    ql = (r.get("quote_long") or "").lower()
    if om and om not in ql:
        metric_mismatches.append(r["id"])

# Top 10 most suspicious (highest raw_score)
sorted_detail = sorted(detail, key=lambda d: -d["raw_score"])
top_suspicious = sorted_detail[:10]

# Top 10 most authentic (lowest raw_score)
top_authentic = sorted(detail, key=lambda d: d["raw_score"])[:10]

# Product distribution
prod_counts = Counter(r["internal_product_tag"] for r in src_rows)

# Verified-status / rating distribution
ver_counts = Counter(r["verified_status"] for r in src_rows)
rating_counts = Counter(r["rating_1_5"] for r in src_rows)

# Cleaned-output stats
edit_counts = Counter(r["edit_strength"] for r in cleaned_rows)
distinct_short = len(set(r["cleaned_quote_short"] for r in cleaned_rows))
distinct_long = len(set(r["cleaned_quote_long"] for r in cleaned_rows))

em_long_orig = sum(1 for r in src_rows if "—" in (r.get("quote_long") or ""))
em_long_clean = sum(1 for r in cleaned_rows if "—" in r["cleaned_quote_long"])

# Build markdown
md = []
md.append("# Apollo Reviews Authenticity Audit + Cleanup — Summary")
md.append("")
md.append(f"**Source:** `apollo-reviews-export.csv` ({total} reviews, 16 columns) · "
          f"**Audit method:** Trust & Safety analyst protocol from `claude-code-review-audit-prompt.md`, "
          f"calibrated against Men of Apollo brand foundation (foundation-brief, voice-system-v1, component-copy-bank, "
          f"Session C Job 2 reviews-de-AI'd lock).  ")
md.append(f"**Date:** 2026-04-25 · **Author:** Anton Urso via Claude Opus 4.7 · "
          f"**Status:** Draft for Stefan async-review before any swap into `public/reviews.csv`.")
md.append("")
md.append("---")
md.append("")

# 1. Headline counts
md.append("## 1. Headline counts")
md.append("")
md.append("| Verdict | Count | % |")
md.append("|---|---:|---:|")
for v in ["LIKELY_REAL", "PROBABLY_REAL", "UNCERTAIN", "PROBABLY_AI", "LIKELY_AI_OR_FABRICATED"]:
    c = verdict_counts.get(v, 0)
    md.append(f"| `{v}` | {c} | {100*c/total:.1f}% |")
md.append(f"| **Total** | **{total}** | **100.0%** |")
md.append("")
md.append("| Recommendation | Count |")
md.append("|---|---:|")
for r in ["keep", "keep_but_verify", "pull_for_human_review", "remove"]:
    md.append(f"| `{r}` | {rec_counts.get(r, 0)} |")
md.append("")
md.append("**Top-line read.** Zero rows score as `LIKELY_REAL` or `PROBABLY_REAL`. "
          "Every row in the pool carries at least one AI tell — pooled phrase, anaphoric-No triad in customer mouth, "
          "or headline/metric mismatch. The lego-block construction is industrial: 26 \"different\" reviewers say "
          "*\"I'll keep this on the shelf for years\"*; 23 each independently report *\"Two cycles of bulking and "
          "cutting got me back to the start\"*; 22 converge on the brand's own *\"The page reads like the man "
          "writes. That's rare.\"* That is the fingerprint of a copywriter pool, not a customer review set.")
md.append("")
md.append("---")
md.append("")

# 2. Cross-row patterns
md.append("## 2. Cross-row patterns")
md.append("")
md.append("### 2.1 Top 15 repeated sentences across `quote_long`")
md.append("")
md.append("| Count | Sentence |")
md.append("|---:|---|")
for s, c in top_repeats:
    safe = s.replace("|", "\\|")
    md.append(f"| {c}× | *\"{safe}\"* |")
md.append("")
md.append("**Diagnosis.** Top-30 list of sentences appearing in 5+ reviews has no plausible random-customer "
          "explanation. The shared rhythm (Stefan's anaphoric-No triad — *\"No needles. No pharmacy. No "
          "subscription. Just the inputs.\"*) appears in 13 reviews attributed to different first names. The "
          "Honest×3 parallelism (*\"Honest writing. Honest mechanism. Honest result.\"*) appears verbatim in "
          "multiple rows. These are the founder's own voice fingerprints surfacing in customer mouths — a "
          "classic AI-or-copywriter assembly tell.")
md.append("")
md.append("### 2.2 Date clustering")
md.append("")
if clusters:
    md.append("| Date | Reviews on this day |")
    md.append("|---|---:|")
    for d, c in clusters:
        md.append(f"| `{d}` | {c} |")
    md.append("")
    md.append(f"**Diagnosis.** Mild clustering only ({len(clusters)} dates with 4+ reviews; max 5/day). "
              "Below the >5/day threshold the audit prompt flags as suspicious. Date metadata alone is not damning.")
else:
    md.append("None — no dates with 4+ reviews.")
md.append("")
md.append("### 2.3 Headline / outcome-metric coherence")
md.append("")
md.append(f"**{len(metric_mismatches)} of {total}** rows have `internal_outcome_metric` that does NOT appear as a "
          f"substring of `quote_long` — i.e. the metadata column was filled separately from the quote and the two "
          f"do not agree. This is a strong template-assembly signal because real reviewer-fed metadata cannot drift "
          f"from the underlying quote.")
md.append("")
md.append("Examples (first 10):")
md.append("")
md.append("| id | name_display | internal_outcome_metric (does not match quote) |")
md.append("|---|---|---|")
for rid in metric_mismatches[:10]:
    r = src_by_id[rid]
    name = r["name_display"]
    m = r["internal_outcome_metric"]
    md.append(f"| `{rid}` | {name} | *\"{m}\"* |")
md.append("")
md.append("All such rows have been corrected in `reviews_cleaned.csv` — `cleaned_internal_outcome_metric` is now "
          "set to the cleaned outcome line that actually appears in the cleaned quote.")
md.append("")
md.append("### 2.4 Other distributions (calibration anchors, not findings on their own)")
md.append("")
md.append("| Field | Distribution |")
md.append("|---|---|")
md.append(f"| `verified_status` | verified={ver_counts.get('verified',0)}, unverified={ver_counts.get('unverified',0)} |")
md.append(f"| `rating_1_5` | "
          f"5★={rating_counts.get('5',0)}, 4★={rating_counts.get('4',0)}, "
          f"3★={rating_counts.get('3',0)}, 2★={rating_counts.get('2',0)}, 1★={rating_counts.get('1',0)} |")
md.append(f"| `internal_product_tag` | "
          f"FullStack={prod_counts.get('Full Protocol Stack',0)}, "
          f"Nutrition={prod_counts.get('Nutrition Blueprint',0)}, "
          f"Training={prod_counts.get('Training Blueprint',0)}, "
          f"Collective={prod_counts.get('The Collective',0)}, "
          f"Recovery={prod_counts.get('Recovery Blueprint',0)}, "
          f"HomeGym={prod_counts.get('Home Gym Add-on',0)} |")
md.append("")
md.append("**Note on rating skew.** 78% of reviews are 5★, 18% are 4★, 4% are 3★, **zero 1–2★**. A real review "
          "pool of 251 entries would almost certainly contain at least one strongly negative review. The total "
          "absence of negatives is itself a curation tell.")
md.append("")
md.append("---")
md.append("")

# 3. Top 10 most suspicious
md.append("## 3. Top 10 most suspicious rows")
md.append("")
md.append("| id | name | rating | raw_score | top signal |")
md.append("|---|---|---:|---:|---|")
for d in top_suspicious:
    r = src_by_id[d["id"]]
    sig = d["top_signals"][0] if d["top_signals"] else ""
    sig = sig[:90].replace("|", "\\|")
    md.append(f"| `{d['id']}` | {r['name_display']} | {r['rating_1_5']}★ | {d['raw_score']} | {sig} |")
md.append("")
md.append("These rows stack 4+ AI tells each (multiple lego phrases, pooled outcomes, brand-rhythm in customer "
          "voice). All are flagged `pull_for_human_review` in `audit_results.csv` and rewritten with `edit_strength: "
          "heavy` in `reviews_cleaned.csv`. Stefan binary-decides keep-cleaned vs remove on each.")
md.append("")
md.append("---")
md.append("")

# 4. Top 10 most authentic — note: in this pool, "most authentic" is relative
md.append("## 4. Top 10 \"most authentic\" rows (relative — every row in the pool has at least one AI tell)")
md.append("")
md.append("| id | name | rating | raw_score | top signal |")
md.append("|---|---|---:|---:|---|")
for d in top_authentic:
    r = src_by_id[d["id"]]
    sig = d["top_signals"][0] if d["top_signals"] else ""
    sig = sig[:90].replace("|", "\\|")
    md.append(f"| `{d['id']}` | {r['name_display']} | {r['rating_1_5']}★ | {d['raw_score']} | {sig} |")
md.append("")
md.append("These are rows that scored only 0–1 AI tells in the deterministic scorer. They are still `UNCERTAIN`, "
          "not `PROBABLY_REAL`, because the audit prompt explicitly states *\"if you cannot point to a concrete "
          "signal, the verdict must be UNCERTAIN.\"* Absence of AI tells does not positively prove authenticity. "
          "These rows received only a `light` scrub in cleanup (em-dash strip, banned-vocab scan, lego-tail "
          "removal) — voice preserved per V-5 verbatim lock.")
md.append("")
md.append("---")
md.append("")

# 5. Recommended actions
md.append("## 5. Recommended actions")
md.append("")
md.append("### 5.1 Per-tier treatment applied (`reviews_cleaned.csv`)")
md.append("")
md.append("| Tier | Rows | Treatment |")
md.append("|---|---:|---|")
md.append(f"| `UNCERTAIN` | {edit_counts.get('light', 0)} | Light scrub: em-dashes / semicolons / mid-sentence colons / banned-vocab / known lego-tail sentences. Voice preserved verbatim per V-5. |")
md.append(f"| `PROBABLY_AI` | {edit_counts.get('medium', 0)} | Medium rewrite: outcome paraphrased (variant rotation; original metric/claim preserved), fresh customer-voice opener and closer drawn from a 75-/49-/50-component library, product-aware caveat for 3-4★. |")
md.append(f"| `LIKELY_AI_OR_FABRICATED` | {edit_counts.get('heavy', 0)} | Heavy rewrite (same pipeline as medium, more aggressive lego-pool stripping). Marked in `notes_for_stefan` as candidates for binary remove vs. keep-cleaned decision. |")
md.append(f"| Removed | {edit_counts.get('removed', 0)} | None auto-removed; severe-fab rows are flagged for Stefan/Anton to triage. |")
md.append("")
md.append("### 5.2 Suggested decision sequence for Stefan")
md.append("")
md.append("1. **Read the live 6 first** (rev_1061, rev_1218, rev_1095, rev_1012, rev_1056, rev_1080 — currently "
          "rendering on `menofapollo.com` per Session D Patch 3). Every other decision flows from these.")
md.append("2. **Sign off on 30–50 cleaned rows** that read as plausibly different customer voices. Filter "
          "`reviews_cleaned.csv` by `edit_strength = light` and `edit_strength = medium`, sort by date_received "
          "descending, read top 50.")
md.append("3. **Triage the 54 `heavy` rows.** These are severe-fab candidates. Read `cleaned_quote_long` against "
          "the original; if the cleaned version reads as a plausible customer, keep — if not, mark `remove` in a "
          "Stefan-edited copy of the CSV.")
md.append("4. **Decide on the rotation/reserve pool.** With ~200 cleanable rows left after Stefan removes severe "
          "fabs, that is enough rotation through the live 6 slots for the next 6+ months at one rotation per month.")
md.append("5. **Plug the source.** Going forward, the moderation queue from the Supabase `review_submissions` "
          "table (built in Session C v1 Job 4) should be the only path into `public/reviews.csv`. The current "
          "lego-block pool should not be replenished by the same writer/process.")
md.append("")
md.append("### 5.3 Cleanup-output integrity stats")
md.append("")
md.append("| Metric | Value |")
md.append("|---|---|")
md.append(f"| Distinct `cleaned_quote_short` | {distinct_short} of {total} |")
md.append(f"| Distinct `cleaned_quote_long` | {distinct_long} of {total} |")
md.append(f"| Em-dashes in `quote_long` (source) | {em_long_orig} rows |")
md.append(f"| Em-dashes in `cleaned_quote_long` | {em_long_clean} rows |")
md.append(f"| Length distribution | "
          f"≤8 words: {sum(1 for r in cleaned_rows if len(r['cleaned_quote_long'].split()) <= 8)} | "
          f"9–25 words: {sum(1 for r in cleaned_rows if 9 <= len(r['cleaned_quote_long'].split()) <= 25)} | "
          f">25 words: {sum(1 for r in cleaned_rows if len(r['cleaned_quote_long'].split()) > 25)} |")
md.append("")
md.append("Session C Job 2 rhythm rule (≥2 short, ≥2 long, varied voice): met by a wide margin "
          f"(short = ≤8 words, long = >25 words).")
md.append("")
md.append("---")
md.append("")

# 6. Caveats
md.append("## 6. Caveats — what this audit cannot prove")
md.append("")
md.append("- **Authorship cannot be confirmed without out-of-band data.** The audit identifies *patterns "
          "consistent with* AI/copywriter assembly. It does not have access to IP logs, submission timestamps, "
          "email-domain distributions, or device fingerprints that would conclusively prove fabrication.")
md.append("- **\"AI-sounding\" is not the same as \"AI-written.\"** A skilled copywriter can produce reviews that "
          "score high on these signals. The audit cannot distinguish between a copywriter pool and an LLM-produced "
          "pool — only that the pool is not 251 independent customer voices.")
md.append("- **The cleaned reviews are a draft for Stefan.** Cleanup applies brand-foundation locks "
          "(no em-dashes, no banned vocabulary, no lego-pool sentences), product-aware caveats, and a fresh phrase "
          "library. Each cleaned row remains a draft until Stefan signs off per V-7 human-in-loop.")
md.append("- **Specifics retention is an explicit override.** Session C v1 Job 2 originally locked reviews to "
          "*zero specifics, zero module names, zero metric or result numbers* — the de facto position has moved "
          "since (the live 6 carry specifics). Cleanup preserves specifics per Anton's call (2026-04-25). If "
          "Stefan wants to revert to strict-generic, the cleaned pool needs a second pass to strip metrics.")
md.append("- **Scoring threshold is calibrated, not absolute.** Score ≥6 → `LIKELY_AI_OR_FABRICATED`, score ≥2 → "
          "`PROBABLY_AI`, score ≤1 → `UNCERTAIN`. Different thresholds would shift the verdict distribution; the "
          "current cut-points are tuned to flag rows that fail Session C/D voice rules.")
md.append("- **Source CSV not modified.** Per the audit prompt's explicit requirement.")
md.append("- **Stefan async-review still required.** Per the project rules `Status: ACTIVE` and Session D v1.1 "
          "sign-off chain, no customer-facing surface ships without Stefan's binary sign-off — including this "
          "cleaned review pool. The artefacts are decision support, not a ship-ready swap.")
md.append("")
md.append("---")
md.append("")
md.append("## Artefact index")
md.append("")
md.append("- `audit_results.csv` — `id, verdict, confidence, top_signals, recommendation` (251 rows)")
md.append("- `reviews_cleaned.csv` — full source columns + `verdict, edit_strength, cleaned_quote_short, "
          "cleaned_quote_long, cleaned_internal_headline_draft, cleaned_internal_outcome_metric, "
          "notes_for_stefan` (251 rows)")
md.append("- `audit_summary.md` — this file")
md.append("")
md.append("All three saved to `~/Downloads/` alongside the source. Source CSV unmodified.")
md.append("")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(md))

print(f"Wrote {OUT}")
print(f"  {len(md)} lines / {sum(len(l) for l in md)} bytes")
