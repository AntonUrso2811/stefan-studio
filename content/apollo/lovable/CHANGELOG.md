# Lovable prompt changelog

Version history for the Apollo integration prompts. **Never overwrite** — bump the version, log the reason here.

## session-a-module-load

### v2 — 2026-04-23 (current)
- **Word-for-word extraction.** Stefan confirmed the intent is verbatim module content — no editorial restructuring. Module files rebuilt to frontmatter + cleaned body only (stripped the `## Summary` / `## Content map` / `## Frameworks / protocols` / `## Visual callouts` / `## Full body` scaffold that v1 introduced).
- Session A prompt rewritten: Lovable renders each module body exactly as-is, with frontmatter driving card metadata, phase gating, and next-step CTA. Explicit "do not rewrite" constraints.
- Phase architecture corrected to four phases (Phase 3 = MOA_14–18, Phase 4 = MOA_19–20) per MOA_01's "Phase 4 at Day 90" reference.
- QA checklist v2 lead with a verbatim spot-check as the primary gate.

### v1 — 2026-04-23 (superseded)
- Initial release with `## Summary` / `## Content map` / `## Frameworks / protocols` / `## Visual callouts` / `## Full body` scaffold. Stefan's feedback: "literally implemented word-for-word, for the exact content to be extracted" — the editorial layer was unnecessary.
- Kept in repo history only; v2 supersedes.

## session-b-feedback-fixes

### v1 — 2026-04-23
- Initial release. Ships three fixes per Stefan's feedback (2026-04-23):
  1. Protocol lander "Who is this for?" rewrite — universal-entry copy, hard-ban on business/executive framing.
  2. Reviews consolidation — one universal section, 4–6 entries, product-siloed sections archived.
  3. Imagery regen — placeholder `{{IMAGE_MODEL}}` for Anton to insert; pilot-then-batch.
- Voice anchor: current live site (module bodies + founder passages). `/brand` skill deferred to post-ship.
- Driver: Anton, end-to-end.

## session-c-final-polish

### v2 — 2026-04-25 (current)
- **Scope reduced to modules-only.** v2 ships only Job 1 from v1 (Lovable typography pass on module pages). Jobs 2 (reviews rewrite), 3 (Higgs Field imagery pilot), and 4 (customer review submission) are **deferred to Session D**, which will be authored alongside the in-flight conversion audit on the home + /protocols landers.
- **Why deferred.** Three reasons: (a) the conversion audit will land voice + structure decisions for reviews and imagery — touching them now forces a Session D re-do; (b) Stefan's brand foundation in `brand-kit/` is currently a stub — the `/brand` skill hasn't been run for him, so there's no canonical voice fingerprint, and reviews/imagery are downstream of voice; (c) the customer review submission form needs to mirror whatever Session D lands as the on-page review treatment, building it now risks scrap-and-rebuild.
- **Repo-side h2/h3 work already shipped.** Commit `f1353c6` (merged into main as `05104b7` via PR #1, 2026-04-25) added named h2/h3 structural headings to all 20 module markdown files. Body prose byte-identical — verified by stripping `## ` / `### ` prefixes from each modified file and diffing cleanly to its pre-Session-C version. Module-14 (Phase 3 overview) intentionally untouched (single short section).
- **v2 Lovable prompt** (`session-c-final-polish.v2.md`) is one job: render-layer typography for module pages (body 18/1.65 mobile, 19/1.7 desktop, 66ch measure, h2 hair-rule, h3 spec, auto-TOC from h2 only, sticky mobile drawer, scroll-progress bar). Hard out-of-scope statement on home, /protocols, /community, reviews block, imagery, submission form. Type tokens must be scoped to module pages only — no global bleed.
- **QA checklist rewritten** (`qa-checklist-session-c.md`) — modules-only typography spec checks + cross-section regression checks against pre-v2 screenshots of home / /protocols / /community to catch any scope bleed.
- v1 retained in repo for historical reference and as input material for Session D.
- Driver: Anton, end-to-end.

### v1 — 2026-04-24 (superseded)
- Final polish pass per Stefan's feedback (2026-04-24, WhatsApp 09:43–09:47 GMT+1). Four jobs:
  1. **Module hierarchy + typography** — named h2/h3 headings added to all 20 source MD files (prerequisite, pre-session), plus Lovable-side typography spec (18/1.65 body, 66ch measure, hair-rule h2s, auto-TOC from h2 only, sticky mobile drawer, scroll-progress bar on module pages).
  2. **Reviews rewrite (de-named + de-AI'd)** — exactly 4 reviews in the universal block, first-name + last-initial only, zero product specifics, zero em dashes, zero AI vocabulary, varied sentence rhythm. 8-entry sample pool provided; Lovable picks 4.
  3. **Higgs Field imagery pilot → batch OR remove** — Higgs Field (higgsfield.ai) explicitly supersedes the Session B `{{IMAGE_MODEL}}` placeholder and retires the prior OpenAI Images 2.0 strategy. Global positive-DNA prompt, global negative prompt, 3 paste-ready templates (hero / module card / testimonial). Binary Stefan gate on 1 hero + 1 module card before batch. Fallback on fail: remove all photographic imagery, typography-on-whitespace hero, typography module cards, initials-in-circle testimonials.
  4. **Customer review submission** — form on all three landers, Supabase `review_submissions` table with pending/approved/rejected status, `/admin/reviews` route gated to Stefan + Anton, edge-function rate limit (1 per IP per 24h), honeypot, auto-strip em dashes on approval. Email fallback if admin gating can't be done cleanly.
- **Verbatim contract re-framed (not broken).** Session A v2 locked "verbatim body" = no editorial scaffold, no paraphrase. Session C adds named h2/h3 structural headings derived verbatim from existing concept-lead sentences in the prose. Body sentences remain byte-identical. Headings are presentation, not content rewriting. Diff-verified: `git diff --word-diff` on `content/apollo/modules/` shows only added heading lines + matching blank-line spacing.
- **Execution order.** Jobs 1–3 ship in parallel. Job 4 ships after Job 2 locks the review data model. Stefan holds the binary gate on Job 3.
- Voice anchor: module bodies + founder-voice paragraphs (unchanged from Session B).
- Driver: Anton, end-to-end.
