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

### v2 — 2026-04-25 (current — shipped, Stefan sign-off received 2026-04-25)
- **Status**: Stefan walked module-05 / module-10 / module-19 on mobile + desktop and signed off "modules read better". Anton publishes preview → production in Lovable. Session C closed.
- **Two iteration sub-rounds during execution:**
  - **v2.1 — markdown sync.** First Lovable run produced the typography components and CSS but Lovable's local `src/content/modules/*.md` were stale (zero h2/h3 in DOM). Sync prompt sent the canonical raw GitHub URLs for all 19 modules; Lovable updated its copies in place. Re-check: 10 h2 + 40 h3 in module-05, TOC populated, scroll-progress mounted. ✓
  - **v2.2 — body typography fix.** After v2.1, headings rendered correctly but body paragraphs were 14px / 22.4px (Tailwind `font-body` was winning the cascade over the unset `.module-reader p` rule). Patch added scoped `.module-reader p` rules for 18/1.65 mobile, 19/1.7 desktop. Re-check: body 19px / 32.3px on desktop. ✓
- **Verified post-ship** via Chrome MCP DOM inspection on /members module-05: h1 56/60 desktop, h2 32px with hair-rule on non-first h2s, h3 24px, body 19px / 1.7, TOC populated, scroll-progress mounted. Cross-section regression passed: home, /protocols, /members render unchanged from pre-v2 baseline (no `.module-reader` leak).
- **Minor outstanding (parked):** `.module-reader` max-width is 857px; spec was 66ch (~720px at 19px). Stefan did not flag the column width during sign-off — defer to a future session only if reader feedback surfaces it.
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

## session-d-conversion-polish

### v1.1 — 2026-04-25 (current — shipped to preview, Anton sign-off received 2026-04-25)
- **Status**: Anton signed off on Session D v1.1 after Chrome MCP DOM verification of all 4 patches. Preview URL `https://id-preview--43862afc-af1f-46ae-b75f-f46e2183ea06.lovable.app/` is now in Stefan async-review state. Production publish gated on Stefan's binary sign-off.
- **Patch loop (4 fixes on top of v1):**
  - **Patch 1 — Gate 9 line-height fix.** v1's `md:leading-[1.1]` was being beaten at lg+ breakpoints by Tailwind's `lg:text-6xl` paired `line-height: 1`. Added `lg:leading-[1.1]` to the agitation H2 classList. Computed line-height now 66px (1.1 × 60px). With `overflow: visible` the descenders render fully — visually clean despite scrollHeight technically still > clientHeight by 6px (mathematical artefact, not visual clipping).
  - **Patch 2 — Em-dash strip on 5 named legacy prose lines.** Stripped em-dashes from /protocols Pillars-bridge bullets (lines 619-621), ProtocolsBridge tagline (721), testosterone block (820), Pillars heading (923 — now reads *"Three pillars. One body that holds up for life."*), closer (1239). Structured list separators (Input 1 — Sleep) and numerical en-dashes (10–15%) intentionally left intact — flagged for Stefan async voice-purity review only.
  - **Patch 3 — Review name swap.** Lovable v1 invented 6 placeholder names (Liam R., Nathan L., Richard T., Joe M., Matthew S., Niall O.). Replaced verbatim with the canonical Session B/C pool: James R., Liam K., Tom H., Daniel P., Michael O., Alex T. Verified all 6 canonical names render and all 6 invented names are absent from DOM. Reviews data is now sourced from `public/reviews.csv`.
  - **Patch 4 — Q7 FAQ softened.** Lovable v1 wrote an unverified "48-hour review + 20-minute onboarding call" SLA. Replaced with: *"You get your PDFs instantly via email. The confirmation page also includes an option to apply for the Private Coaching Community. Applications are reviewed personally. If accepted, we'll be in touch with onboarding details within a few business days."* No 48-hour or 20-minute remnants in DOM.
- **Verified post-ship via Chrome MCP** at viewport 1920: agitation H2 line-height 66px; Pillars heading em-dash absent; closer em-dash absent; 6 canonical review names present; Q7 softened text rendered exactly. Session A/B/C/Cv2 lock-survival check passed: module-pages verbatim contract intact, lander typography unchanged, reviews block sourced once and rendered consistently.
- **Outstanding pre-launch dependencies (post-Stefan-sign-off):**
  - Stefan must own `menofapollo.com` and configure the `hello@` inbox before public launch. If not done by go-live, swap footer contact line to `Questions? DM @stefs.way on Instagram` (instructed in the prompt itself).
  - UK-jurisdiction legal review of `/privacy` and `/terms` stub copy before public launch. URLs and routes don't change; only the body copy.
  - Currency decision USD vs GBP (audit X-08) — Stefan async, not a launch blocker.
  - Audit X-14 "ambition" identity bullet — Stefan async confirm.
  - Legacy /protocols functional list separators + numerical en-dashes — Stefan async voice-purity review only.
- Driver: Anton, end-to-end.

### v1 — 2026-04-25 (superseded by v1.1)
- **Conversion polish on home + /protocols** built from a dedicated pre-session audit (`audit-pre-session-d.md`). Three jobs: Job 0 cross-cutting fixes (em-dash strips on locked verbatim blocks; review name-format + duplicate-line + tags decisions; header nav harmonisation; footer legal block); Job 1 homepage (hero proof anchor; new problem-agitation block; **new mechanism-reveal block surfacing the Five Inputs on home — the single highest-impact change**; new "what you get inside the Collective" block; "transformation arc" → "90-day arc" swap; reviews repositioned below mechanism + what-you-get; new common-questions block; risk-reversal anchor); Job 2 /protocols (hero proof anchor; agitation-headline layout fix; **stack offer deduplicated to one placement**; mobile QA on mechanism-card study citations; FAQ voice-check pass).
- **Brand foundation authored.** The four brand-kit files at `brand-kit/01-docs/` (foundation-brief, voice-system-v1, component-copy-bank) plus `project-rules.md` are now Stefan-specific (replacing the Urso template stub). Authored 2026-04-25 via the **T1–T5 founder-unavailable extraction protocol** — Stefan was not available for the standard `/brand` interview, so voice was extracted from a tiered signal hierarchy: T1 deep-research dossier (`brand-kit/00-research/dossier-2026-04-25.md`) + 20 module bodies; T2 IG @stefs.way + YouTube @Stefswayy; T3 the live-site PDF captures; T4 customer reviews; T5 negative-space mapping. Every claim cites its source by tier; confidence is rated per section; gap report flags items only Stefan can resolve. Stefan async-reviews the foundation when he surfaces.
- **Audit architecture.** 49 issues catalogued across cross-cutting + home + /protocols against three rulesets (CF-1…10 conversion framework, V-1…7 voice principles, S-A/B/C/Cv2 session locks). Severity (Block/Major/Minor) × Readiness (Ship-ready/Anton-decision/Anton-data/Live-state-needed) — no PASS/FAIL collapse. 32 issues fed into Session D; 12 are settled (no-change rows surfaced for the "do not touch" list); 12 surfaced as Anton/Stefan decisions in §6 of the audit (em-dash policy, transformation-arc swap, currency, footer legal data, hero positioning, etc.). Round-trip integrity check: every audit issue has a Session D job hook OR an explicit why-not in audit §7.
- **Inherited locks (do not re-litigate).** S-A 20-module verbatim contract; S-B/Job1 zero-executive-language on /protocols; S-B/Job2 one-source-three-placements reviews; S-C/Job2 reviews de-AI'd rules; S-C/Job3 Higgs Field imagery pilot passed; S-Cv2 module-pages typography (lander typography unchanged in D). Cross-section regression block in `qa-checklist-session-d.md` re-verifies each lock survived.
- **Two pre-flight gates BLOCK Session D until Anton supplies them.** Gate 8: footer legal data (privacy URL, terms URL, contact email, GDPR/cookie line) — closes the pre-launch CF-10 footer issue across both pages. Gate 9: /protocols agitation-headline state (verify in browser whether the section header above the *"and stimulants to feel normal"* image is render-clipped or genuinely missing; supply string if missing). The other 7 pre-flight gates are PASS or WAIVED by what's already in the repo.
- **Out of scope** (explicitly excluded from D): module pages, module bodies, the customer review submission form (Session C v1 Job 4 deferred — not re-opened in D), pricing currency swap (USD ships as live; Stefan async-decides GBP later), Higgs Field imagery (settled).
- **Voice anchor:** the new brand-kit files + cadence anchors quoted verbatim from the live site (hero / mechanism / founder / guarantee / final exclusion). Refused-vocab list expanded to fitness/transformation analogues per dossier negative findings.
- **Sign-off chain.** Anton signs off on the audit before Session D fires. Anton runs `qa-checklist-session-d.md` after Lovable executes. Stefan async-reviews the brand-kit files + the Session D output before production publish. Preview-only deployment; production gated on Stefan binary sign-off.
- Driver: Anton, end-to-end.

## session-e-proof-block-reset

### v1 — 2026-04-25 (current — plan approved, generation pending)
- **Override:** Session D Pre-flight Gate 7 ("Higgs Field photographic imagery live on both pages. Pilot passed. Do not re-open.") and the Session D entry above ("Higgs Field imagery (settled)").
- **Grounds for override:** the current proof block (3 before/after diptychs, "SIX MONTHS APART") is a structural violation of three locked brand rules from the foundation brief authored 2026-04-25:
  1. Refused vocab — "transformation" is Tier-A banned per `voice-system-v1.md` and `component-copy-bank.md`. The diptych's visual grammar IS transformation regardless of caption wording. Visual grammar is voice.
  2. Archetype lock — `foundation-brief.md` locks Sage/Mentor + Sovereign, NOT Hero. Before/after is the Hero archetype's signature visual move (the journey, the arc, the underdog crossing the threshold). Stefan is positioned as already-arrived, dispensing the protocol.
  3. No-origin-story posture — dossier §8 documents the deliberate absence of a transformation narrative as brand-defining. AI-generated "before" imagery imports that narrative back in.
- The Session C/Job3 pilot approval (2026-04-24) pre-dates the foundation-brief lock (2026-04-25) and therefore did not weigh these constraints. **This is a structural reset, not a craft refinement.**
- **New direction:** v5 arrived-state portraits — three single-frame Apollonian portraits of three men in their held state, photographed in the cinematic-domestic register the dossier locks (Casey Neistat → Matt D'Avella → Will Tennyson lineage; Sony FX3; Apollonian, not Herculean). No before. No transformation. The protocol holds the state.
- **Dual-model A/B parallel generation.** Higgs Field (locked) + Google Gemini Nano Banana Pro 2 (added 2026-04-25 per Anton). Both models run on every persona brief; the best frame wins per persona regardless of which model produced it. Higgs Field's strength is cinematic register; Nano Banana Pro 2's strength is photorealism + scene coherence + better hands/faces. Decision rule at QC time is purely visual quality + brand fit.
- **Section copy update:** heading "WHAT THE 90-DAY ARC ACTUALLY PRODUCES" → `THIS IS WHAT THE PROTOCOL HOLDS.` Sub: `No injections. No shortcuts. Run honestly.` Per-image captions drop the time-delta format ("MONTH 0 → MONTH 6") in favour of present-tense subject metadata: `M., 38. 14 months in.` / `T., 41. Year two.` / `S., 35. 9 months in.`
- **Deliverables in repo:**
  - `~/Documents/Studio/men-of-apollo/deliverables/image-prompts-v5-arrived-state.md` — dual-model prompt pack with 6 prompts (3 personas × 2 models), universal negative + persona tails (Higgs Field), 8-point QC gate, selection rule, caption/heading spec, model-win tracking table
  - `~/Documents/Studio/men-of-apollo/deliverables/higgsfield-prompts-v4-plain-wall.md` — marked SUPERSEDED with banner pointing to v5
  - `content/apollo/lovable/session-e-proof-block-reset.v1.md` — paste-ready Lovable change brief for Stefan: section heading copy, sub copy, 3 captions, 3 alt texts, image attachment slots, sign-off lines
  - This CHANGELOG entry
- **Plan:** `/Users/antonurso/.claude/plans/one-thing-that-we-bright-fairy.md` (approved 2026-04-25)
- **Approver gate:** Stefan binary YES/NO on 3 winning images + new section copy before Lovable swap.
- **Status pipeline:** Plan approved → Phase A docs (this commit) → Phase B image generation pending Anton → Phase C Stefan binary gate → Phase D Lovable swap → Phase E live verification → Phase F docs close.
- **Out of scope:** the testimonial / "WHAT MEN ARE SAYING" social-proof block (real screenshots stay), all other section copy, typography stack (locked in Session C), site migration off Lovable, video proof block.
- Driver: Anton, end-to-end.

---

## session-f-reviews-pull-and-form

### v1 — 2026-04-25 (current — Stefan binary sign-off received 2026-04-25; Lovable execution and production publish proceeding per the locked sequence)
- **Override:** Session B Job 2 (one-source-three-placements reviews block — manufactured 6-card render on home + /protocols + Collective deflection) and the Session D Job 0.2/0.3/0.4 review-block patches (name format normalisation, dedup, product tags). The data binding from `public/reviews.csv` to the Reviews block is severed.
- **Grounds for override:** the 2026-04-25 audit of the upstream 251-row review pool (`apollo-reviews-export.csv`) returned **zero rows scoring `LIKELY_REAL` or `PROBABLY_REAL`**. Quantitative tells:
  1. The top sentence appears 26 times across "different" reviewers (*"I'll keep this on the shelf for years."*); top 40 sentences each appear 3–26 times.
  2. Stefan's anaphoric-No fingerprint (*"No needles. No pharmacy. No subscription. Just the inputs."*) appears verbatim in 13 customer mouths — a structural impossibility for independent reviewers.
  3. 100% of `quote_short` values are byte-identical substrings of `quote_long` (automated extraction tell).
  4. 18/251 rows have `internal_outcome_metric` that does not appear anywhere in `quote_long` (template-assembly tell).
  5. 78% 5★, 18% 4★, 4% 3★, **zero 1–2★** — probabilistic impossibility for real customer data.
- The Session C v1 Job 2 lock (de-AI'd reviews, 4-from-8 universal block) was implemented in good faith but was never able to repair authorship. Session D Patch 3 swapped the placeholder names for "canonical" names from the same pool — surface fix only. **This is a structural reset, not a craft refinement.**
- **Decision authority:** Stefan delegated direction to Anton on 2026-04-25 (*"as long as it desires the best outcome"*). Anton ratified Hybrid B+ (pull + activate form) on 2026-04-25.
- **New direction:** pull the manufactured Reviews block from home + /protocols. Replace with a minimal holding section (eyebrow `Reviews`, header `Open for real reviews.`, 60-word body explaining the position, link down to YouTube comments block). Keep the existing "What Men Write Back" YouTube-comments block (real, sourced unedited from Stefan's actual YouTube comments per `foundation-brief.md` §4) — it remains as social proof. Activate the Session C v1 Job 4 customer review submission form (deferred since 2026-04-23) with Supabase `review_submissions` table, edge-function rate limit (1 per IP-hash per 24h, SHA-256 + salt, no raw IPs stored), `/admin/reviews` moderation route gated to `hello@menofapollo.com` and `ops.controlplane@gmail.com` (with email-fallback if Lovable cannot gate the route in this session), honeypot anti-bot, and an auto-strip-on-approval pass for em-dashes / semicolons / mid-sentence colons. The relaunched Reviews block reads from `reviews_published` view (filtered to `status = 'approved'`) and stays pulled until that view returns ≥ 6 rows.
- **Why this is the brand decision, not a regression.** The brand's strongest line is *"This is not for everyone."* Manufactured testimonials are incompatible with that positioning. Pulling the block until real reviews exist closes the only material legal/reputational exposure on the site (testimonial-fraud surface area under UK ASA / FTC). Aligns with Stefan's restraint-as-aesthetic register and the Sage/Sovereign archetype lock.
- **Audit artefacts (decision-support, not customer-facing):**
  - `~/Downloads/audit_results.csv` — 251 rows, verdict + signals + recommendation
  - `~/Downloads/reviews_cleaned.csv` — tiered cleanup output (21 light scrub, 176 medium rewrite, 54 heavy rewrite); kept as reference, never ships as customer-attributed text
  - `~/Downloads/heavy_triage.csv` — 38 keep / 16 remove decisions on the 54 LIKELY_AI_OR_FABRICATED rows
  - `~/Downloads/audit_summary.md` — full report with cross-row patterns and caveats
  - `~/Downloads/stefan_review_brief.md` — async-review brief originally drafted for Stefan; superseded by his delegation but retained for audit trail
- **Deliverables in repo:**
  - `content/apollo/lovable/session-f-reviews-pull-and-form.v1.md` — paste-ready Lovable change brief, two jobs (pull + form)
  - `content/apollo/lovable/qa-checklist-session-f.md` — post-deploy QA checklist for Anton
  - This CHANGELOG entry
  - `brand-kit/01-docs/component-copy-bank.md` §2.2 to be updated by Lovable: existing `Reviews` strings marked `PULLED — pending real submissions`; new `LIVE` entry for `Open for real reviews.` holding header
  - `public/reviews.csv` retained in repo, but binding severed; sibling `public/reviews.README.md` documents the deprecation
- **CTA register update:** `SUBMIT REVIEW →` added to the locked CTA list (foundation-brief §8 / project-rules.md / component-copy-bank.md §3). Anton sign-off only; Stefan async-confirms.
- **Inherited locks (unchanged):** S-A 20-module verbatim; S-B/Job1 protocols zero-exec; S-C v1 Job 2 review-content rules (apply to whatever lands in `reviews_published` going forward); S-Cv2 module typography; S-D Job 0/1/2 conversion blocks; S-E proof-block reset (imagery untouched).
- **Out of scope:** the "What Men Write Back" YouTube block (verbatim hold), module pages, all Session D conversion blocks, all Session E imagery, the Collective application form, any auto-relaunch of the Reviews block (manual session triggered when `reviews_published` ≥ 6 and Stefan signs off), confirmation emails to submitters (deliberate — keeps surface area small).
- **Approver gate:** Stefan binary YES/NO on the preview before production publish. Sign-off block on `qa-checklist-session-f.md`.
- **Stefan sign-off:** **Received 2026-04-25.** Production publish authorised. Lovable execution + QA gate for Anton; production publish gated only on Anton (no second Stefan gate required).
- **Status pipeline:** Plan approved (2026-04-25) → **Stefan sign-off received (2026-04-25)** → Lovable execution → Anton runs `qa-checklist-session-f.md` against preview → production publish → form open for real submissions → `reviews_published` accumulates → Reviews block relaunch in a future session when count ≥ 6.
- **Driver:** Anton, end-to-end. Stefan async-approved direction and brief.
- **Component copy bank update (2026-04-25):** §2.2 marked old `Reviews` strings `PULLED — pending real submissions`; new `LIVE` entries added for the holding section header `Open for real reviews.`, the 60-word body, the YouTube-link microcopy, and the form sub + disclosure. §3 added `SUBMIT REVIEW →` to the locked CTA register.
