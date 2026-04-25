# Apollo Reviews Audit + Cleanup Toolchain — 2026-04-25 Archive

Five Python scripts that audited the 251-row `apollo-reviews-export.csv` review pool, rewrote the AI-assembled rows against the Men of Apollo brand foundation, and produced the artefacts in `~/Downloads/`. Archived here for reproducibility and for the May 9 scheduled review-queue audit agent.

**Origin session:** Apollo Reviews Authenticity Audit + Brand-Compliant Cleanup (2026-04-25).
**Status:** One-off. The pipeline ran once against the pre-launch pool. Real reviews going forward come from the Supabase `review_submissions` queue (Session F Job 2 — `content/apollo/lovable/session-f-reviews-pull-and-form.v1.md`).

## Scripts

| File | Phase | Purpose |
|---|---|---|
| `apollo_calibration.py` | 1 | Calibration pass — phrase repetition, date clusters, headline-metric mismatch, em-dash sweep. Read-only. Output: stdout summary. |
| `apollo_audit.py` | 2 | Per-row deterministic authenticity scorer. Output: `~/Downloads/audit_results.csv` + `/tmp/apollo_audit_per_row.json`. |
| `apollo_cleanup_v2.py` | 3+4 | Tiered cleanup keyed to verdict — light scrub for UNCERTAIN, medium rewrite for PROBABLY_AI, heavy rewrite for LIKELY_AI_OR_FABRICATED. Phrase library + outcome paraphrase variants + product-aware caveats + round-robin variant rotation + double-caveat suppression. Output: `~/Downloads/reviews_cleaned.csv`. |
| `apollo_heavy_triage.py` | 4.1 | Triage of the 54 LIKELY_AI_OR_FABRICATED rows — 38 keep / 16 remove with Anton-rationale per row. Output: `~/Downloads/heavy_triage.csv`. |
| `apollo_summary.py` | 5 | Generates the long-form audit summary markdown. Output: `~/Downloads/audit_summary.md`. |

## Run order

```bash
# from this directory
python3 apollo_calibration.py     # informational only
python3 apollo_audit.py           # writes audit_results.csv + per-row JSON
python3 apollo_cleanup_v2.py      # writes reviews_cleaned.csv
python3 apollo_heavy_triage.py    # writes heavy_triage.csv (depends on hard-coded TRIAGE dict)
python3 apollo_summary.py         # writes audit_summary.md
```

All scripts hard-code the source path `~/Downloads/apollo-reviews-export.csv` and write to `~/Downloads/`. To use against a different CSV, modify the `SRC` and `OUT` constants at the top of each script.

## Why these are kept here

1. **Reproducibility.** If anyone questions the audit verdict, this is the source code that produced it.
2. **Future audits.** If a new review-pool batch arrives, these scripts give a starting point.
3. **The May 9 scheduled agent** ([routine](https://claude.ai/code/routines/trig_01P3di11pK43Srbj7nCsFx4e)) embeds the scoring algorithm in its prompt, but if it ever needs to point at a fuller implementation, this is the canonical version.

## What they don't do

- They don't query Supabase. The `review_submissions` table introduced in Session F Job 2 needs a different read path (Supabase MCP connector or service-role-key access). Not implemented here.
- They don't auto-publish. `reviews_cleaned.csv` is decision-support only; nothing ships customer-facing without Stefan binary sign-off.
- They don't replace the brand pipeline. The phrase library and outcome variants encode brand-foundation rules but are not a substitute for `/copy` + `/humanizer` for net-new copy.

## Findings summary (recorded for posterity)

- **251 / 251 rows** scored as copywriter-assembled. Zero `LIKELY_REAL` / `PROBABLY_REAL`.
- Top duplicate sentence: `"I'll keep this on the shelf for years."` — 26 reviewers.
- Stefan's anaphoric-No fingerprint (`"No needles. No pharmacy. No subscription. Just the inputs."`) appears verbatim in 13 customer mouths.
- 18 / 251 rows have `internal_outcome_metric` that does not appear in `quote_long` (template-assembly tell).
- After cleanup: 247 / 251 distinct cleaned long-form quotes (started at ~30 distinct).
- Heavy-row triage: 38 keep / 16 remove of the 54 LIKELY_AI_OR_FABRICATED rows.
- Decision: pull the manufactured Reviews block. Activate the customer submission form. See Session F.
