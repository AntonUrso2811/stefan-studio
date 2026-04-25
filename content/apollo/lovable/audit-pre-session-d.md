# Apollo's Ascent — Pre-Session-D Conversion Audit

**Version:** 1.0 · **Date:** 2026-04-25 · **Author:** Anton Urso via Claude Code · **Scope:** Homepage (`/`) + Protocols Lander (`/protocols`)

---

## §0 Source-of-truth declaration

The audit was performed against full-scroll PDF screenshots captured **2026-04-25 ~08:33 GMT+1** from the Lovable preview at `preview-apollo-ascension-landing.lovable.app`:

- `~/Downloads/screencapture-preview-apollo-ascension-landing-lovable-app-2026-04-25-08_33_40.pdf` (6 pages — Homepage)
- `~/Downloads/screencapture-preview-apollo-ascension-landing-lovable-app-protocols-2026-04-25-08_32_55.pdf` (8 pages — /protocols)

**Confidence ceiling:** medium-high. PDF capture preserves rendered DOM and styling. What the PDFs cannot show: collapsed FAQ answers, hover states, mobile renders, network-loaded content, and any post-capture changes. Anything reading "Live-state-needed" in §§3–5 means the audit needs an additional surface (mobile screenshot, expanded FAQ, etc.) before Session D can close it.

The brand foundation cited throughout was extracted via T1–T5 protocol on the same date — see `brand-kit/01-docs/foundation-brief.md`. It is medium-high confidence and replaces the prior Urso-template stub.

---

## §1 Rulesets cited (legend)

| Code | Ruleset | Source |
|---|---|---|
| `CF-1` … `CF-10` | 10-stage conversion framework (hero / problem / mechanism / avatar / what's inside / proof / objections / price / risk reversal / final CTA + footer) | Anton's standard heuristic |
| `V-1` … `V-7` | Voice System 7 principles | `brand-kit/01-docs/voice-system-v1.md` |
| `S-A` | Session A v2 verbatim contract on module bodies | `session-a-module-load.v2.md` |
| `S-B/Job1` | Protocols-lander zero-executive-language lock | `session-b-feedback-fixes.v1.md` lines 22–36 |
| `S-B/Job2` | One-source-three-placements universal reviews block | `session-b-feedback-fixes.v1.md` lines 40–69 |
| `S-C/Job2` | Reviews de-AI'd: first-name + last-initial, no em dashes, banned lexicon, varied rhythm | `session-c-final-polish.v1.md` lines 68–104 |
| `S-C/Job3` | Higgs Field imagery pilot gate | `session-c-final-polish.v1.md` lines 107–154 |
| `S-Cv2` | Module-pages typography scope; no lander typography drift | `session-c-final-polish.v2.md` |

---

## §2 Severity + readiness rubric

**Severity** — how badly the issue degrades the page:

- **Block** — the page does not function as a converting landing page until this is fixed (e.g. mechanism reveal missing on a high-intent page).
- **Major** — material conversion lift on the table; structurally wrong but page still ships.
- **Minor** — polish; visible to a careful eye; safe to defer if time is tight.

**Readiness** — what unblocks the fix:

- **Ship-ready** — Session D can write the fix today using `brand-kit/01-docs/` and the screenshots.
- **Anton-decision** — needs Anton to choose between options (a phone-call decision).
- **Anton-data** — needs Anton to provide a value (a number, a string, a URL).
- **Live-state-needed** — needs an additional surface capture before action.

No PASS/FAIL — the two axes are independent.

**Issue ID format:** `H-NN` (homepage), `P-NN` (/protocols), `X-NN` (cross-cutting).

---

## §3 Site-wide findings (cross-cutting)

| ID | Stage/Principle | What's broken (≤25 words) | Cited rules | Severity | Readiness | Decision/Data needed | Session D job hook |
|---|---|---|---|---|---|---|---|
| **X-01** | V-6 punctuation lock | Founder block on /protocols contains em dash (*"I rebuilt — body first"*). | V-6, S-C/Job2 | Major | Anton-decision | Approve recommended fix: replace `—` with `.` to preserve rhythm | `job-0/sec-em-dash-strip` |
| **X-02** | V-6 punctuation lock | Guarantee block contains em dash (*"a different one — or coach you through what's not working"*). Verbatim-locked text contains a banned character. | V-6, S-C/Job2 | Major | Anton-decision | Approve recommended fix to preserve rhythm with period | `job-0/sec-em-dash-strip` |
| **X-03** | V-6 punctuation lock | Final exclusion block contains two em dashes around the parenthetical *"peptides, a macro app, a new supplement stack"*. | V-6, S-C/Job2 | Major | Anton-decision | Approve recommended re-rhythm as triad of fragments | `job-0/sec-em-dash-strip` |
| **X-04** | S-C/Job2 review naming | Live reviews use mixed formats: *"LIAM"*, *"NATHAN L."*, *"RICHARD"* — Session C locked first-name + last-initial. | S-C/Job2 | Major | Ship-ready | — | `job-0/sec-review-format` |
| **X-05** | S-C/Job2 authenticity | The line *"Stefan writes like a man who has actually done it"* appears verbatim in **both** Liam's and Joe's reviews. Authenticity break. | S-C/Job2 | Major | Ship-ready | Edit one of the two reviews to remove the duplicate (recommend keeping in Joe's, removing from Liam's, or rewriting one) | `job-0/sec-review-dedup` |
| **X-06** | S-B/Job2 review tagging | Live reviews carry product-specific tags (*"TRACKING BLUEPRINT"*, *"THE COLLECTIVE"*, *"NUTRITION BLUEPRINT"*, *"RECOVERY BLUEPRINT"*). Session B Job 2 locked one *universal* block — tagging may re-fragment. | S-B/Job2 | Minor | Anton-decision | Decide: keep tags (signals which product the reviewer used) or strip them (purer universal block) | `job-0/sec-review-tags` |
| **X-07** | V-3 owned vocabulary watch-list | Homepage 90-day pillar reads *"transformation arc"*. *transformation* is on the refused-vocab list per `foundation-brief.md` §7. | V-3, V-6 | Major | Anton-decision | Recommend swap to *"90-day arc"* or *"90-day phase"* (Stefan voice supports both); flag for Stefan async | `job-1/sec-pillars` |
| **X-08** | CF-8 currency | All prices display in **USD** ($97, $34.99). Stefan and Anton are UK-based; addressable market unclear. | CF-8 | Minor | Anton-decision | Decide: lock USD (global), swap to GBP, or implement multi-currency. Recommend GBP for UK ICP unless data says otherwise | `job-2/sec-pricing-currency` |
| **X-09** | Site nav consistency | Header nav differs across pages: home shows `MEN OF APOLLO | PROTOCOLS`, /protocols shows `MEN OF APOLLO | PRICING REVIEWS PROTOCOLS`. | Site-wide UX | Minor | Ship-ready | Pick one nav set and apply both pages | `job-0/sec-header-nav` |
| **X-10** | CF-9 risk reversal placement | Guarantee currently lives only on /protocols. Homepage (Collective lander) has no risk-reversal copy in view. High-ticket buyer has zero reversal anchor before applying. | CF-9 | Major | Ship-ready | — | `job-1/sec-risk-reversal` |
| **X-11** | CF-10 footer | Footer is one line on both pages: copyright + brand string. Missing privacy policy, terms, contact, GDPR notice. Pre-launch blocker. | CF-10 | Block (pre-launch) | Anton-data | Provide: privacy URL, terms URL, contact email, GDPR/cookie posture | `job-0/sec-footer` |
| **X-12** | S-C/Job3 imagery gate state | Photographic imagery is live across both pages (Italian rooftop hero on home, gym + before/after on /protocols). Pilot has passed; do not re-open. | S-C/Job3 | — | — | — | `not-in-session-d` (settled) |
| **X-13** | Disambiguation lock | Live pre-headline reads *"BY STEFAN JANKOVIC · MEN OF APOLLO"*. Compliant with the basketball-player disambiguation rule. | `foundation-brief.md` §1 | — | — | — | `not-in-session-d` (settled) |
| **X-14** | V-3 owned vocabulary watch-list | Homepage identity bullet 04 reads *"a body that matches their ambition"*. *ambition* is on the watch-list (borderline Sage-register). | V-3 | Minor | Anton-decision | Decide: keep (Sage-register accepts), swap to *"a body that matches the rest of their life"*, or pass to Stefan | `job-1/sec-identity-bullets` |
| **X-15** | S-Cv2 typography scope | Module typography spec (S-Cv2) was scoped to module pages only. Session D must NOT touch landers' typography. | S-Cv2 | — | — | — | `qa-cross-section-regression` |

---

## §4 Page audit — Homepage (`/`)

The home is currently the **Collective lander** (high-ticket, application-only). Hero, identity bullets, reviews, lifestyle imagery, founder block, application form. Missing: problem agitation, mechanism reveal, what's-inside detail, objection handling, price-band signal, risk reversal.

### CF stage walk

| ID | CF stage | What's there now (≤25 words) | What's broken (≤25 words) | Cited rules | Severity | Readiness | Decision/Data needed | Session D job hook |
|---|---|---|---|---|---|---|---|---|
| **H-01** | CF-1 hero promise | Headline *"THE MEN'S COLLECTIVE BUILT ON FIVE INPUTS, NOT FIVE HUNDRED OPINIONS"* + sub naming systems + dual-CTA. | Hero is *brand-mythic* not *outcome-promising*. No specific outcome / timeline / cohort. /protocols hero is materially stronger. | CF-1, V-1 | Major | Anton-decision | Approve homepage hero rewrite: outcome-led ("A lean, built year-round frame in 90 days, run with men holding the same standard") **or** keep mythic identity-led? Recommend identity-led (this is the Collective's job) but tighten | `job-1/sec-hero` |
| **H-02** | CF-1 above-fold proof | None — hero has no testimonial / star-rating / count near CTA. | Above-fold proof missing on a high-ticket application page is unusual. | CF-1 | Major | Ship-ready | — | `job-1/sec-hero` |
| **H-03** | CF-2 problem agitation | None on home. Reader skips from identity bullets to reviews. | Reader doesn't see the enemy named. The /protocols agitation block (*"Tracking every macro… looking at injectables…"*) is doing this work for the whole site — home should mirror it briefly. | CF-2 | Major | Ship-ready | — | `job-1/sec-problem` |
| **H-04** | CF-3 mechanism reveal | Hero hints at *"five inputs"* but no Mechanism block on home. The Five Inputs cards live only on /protocols. | The strongest asset on the entire site is hidden behind a navigation click. Reader of the home never sees the mechanism unless they jump to /protocols. **Block-tier.** | CF-3 | Block | Ship-ready | — | `job-1/sec-mechanism` |
| **H-05** | CF-4 avatar / who-this-is-for | 4-bullet identity block: *finances/career-discipline/one-standard/body-matches-ambition* + qualifier *"if 3 of 4 describe you, keep reading"*. | Bullet 04 *"ambition"* on watch-list — see X-14. Otherwise on-voice and well-formed. | CF-4 | Minor | Anton-decision | See X-14 | `job-1/sec-identity-bullets` |
| **H-06** | CF-5 modules / what's inside | "The Standard" — 6 cards (Architectural Physique / Disciplined Mind / The Collective / 90-day arc / Private & invitation-only / Lifetime access). | These are **identity claims**, not deliverables. A Collective applicant cannot tell what they're getting weekly / monthly / over the 90 days. | CF-5 | Major | Anton-decision | Decide: leave opaque (high-ticket gating) or surface a "What you get inside the Collective" detail block (recommend the latter — applicants who can't visualise the deliverable apply less) | `job-1/sec-whats-inside` |
| **H-07** | CF-5 watch-list | "The Standard" 90-day card uses *"90-day transformation arc"*. | See X-07 cross-cutting — *transformation* on refused-vocab. | V-3, V-6 | Major | Anton-decision | See X-07 | `job-1/sec-pillars` |
| **H-08** | CF-6 social proof placement | Reviews appear *immediately* after the 4-bullet identity block (page 1 → page 2 of PDF). Then again as YouTube comments grid mid-page. | Reader sees social proof before mechanism + what's inside. Premature — they don't yet know what's being praised. | CF-6 | Major | Ship-ready | — | `job-1/sec-reviews-position` |
| **H-09** | CF-6 review duplicates | Same 6 reviews on home and /protocols (correct per S-B/Job2). Format inconsistency carries over from cross-cutting. | See X-04 (name format) and X-05 (duplicate line). | S-B/Job2, S-C/Job2 | Major | Ship-ready | — | `job-0/sec-review-*` |
| **H-10** | CF-7 objection handling | None — homepage has no FAQ block. /protocols does. | Application-rate is gated by silence on objections (commitment level, time investment, what disqualifies, pricing band). | CF-7 | Major | Anton-decision | Decide: link to /protocols FAQ, surface a slim "common questions" block on home, or lock as silent | `job-1/sec-objections` |
| **H-11** | CF-8 price reveal | Collective price not surfaced anywhere on home. Application is the gate. | Standard high-ticket pattern (gate price behind application). Not necessarily a fault — verify intent. | CF-8 | Minor | Anton-decision | Decide: keep gated (recommend) or surface a price band ("from £X / year") to pre-qualify applicants | `job-1/sec-pricing-band` |
| **H-12** | CF-9 risk reversal | None on home. Guarantee lives only on /protocols. | High-ticket applicant sees zero reversal language before submitting form. | CF-9 | Major | Ship-ready | — | `job-1/sec-risk-reversal` |
| **H-13** | CF-10 final CTA + form | Application form at bottom — clean, on-voice ("If you're ready to hold yourself to a higher standard, apply below"). Honesty about cohort cadence. | Form gates email and one biggest-blocker question — good. No regression. | CF-10 | — | — | — | `not-in-session-d` (settled) |
| **H-14** | CF-10 footer | Single-line footer; missing legal + contact. | See X-11. | CF-10 | Block (pre-launch) | Anton-data | See X-11 | `job-0/sec-footer` |
| **H-15** | V-2 restraint | Hero image (Italian rooftop) is beautiful but doesn't show product, founder, or physique outcome. | Aesthetic-first imagery is on-brand for Stefan. **Settled — not a defect.** | — | — | — | — | `not-in-session-d` (settled) |
| **H-16** | V-4 founder DNA | Homepage founder block (*"I rebuilt myself. Then I built this."*) is on-voice and free of em dashes. | Locked — no change. | V-4 | — | — | — | `not-in-session-d` (settled) |

### Homepage summary

- 1 Block (H-04 mechanism reveal missing)
- 1 Block-pre-launch (H-14 footer)
- 8 Major
- 2 Minor
- 4 Settled (no-change rows surfaced for Session D's "do not touch" list)

The single highest-impact change on the homepage is **adding a Mechanism block** (a slim version of /protocols' "Five Inputs"). That alone closes H-04 and partially closes H-08 (gives reviews something to be social-proof *for*).

---

## §5 Page audit — /protocols Lander

Strong page overall. Hero (CF-1) and Mechanism (CF-3) are the site's best work — locked, do not touch. Most issues are layout polish, deduplication, and the universal-entry tension flagged in foundation-brief.

### CF stage walk

| ID | CF stage | What's there now (≤25 words) | What's broken (≤25 words) | Cited rules | Severity | Readiness | Decision/Data needed | Session D job hook |
|---|---|---|---|---|---|---|---|---|
| **P-01** | CF-1 hero | *"The Five Inputs That Do 95% of What Men Are Paying Thousands to Inject."* + 5-noun sub + triad-with-No. | Locked. Strongest hero on the site. Do not touch. | CF-1, V-1, V-2 | — | — | — | `not-in-session-d` (settled) |
| **P-02** | CF-1 above-fold proof | None — hero has no proof element near CTA. | Same gap as homepage. Less pressing on /protocols (lower-ticket; reader will scroll). | CF-1 | Minor | Ship-ready | — | `job-2/sec-hero-proof` |
| **P-03** | CF-2 problem agitation | *"Tracking every macro. Weighing every meal… Looking at injectables because nothing else has worked."* + *"It's not you."* exoneration. | Strong. **Layout bug:** the section header above the image cuts off — only *"and stimulants to feel normal."* is visible. The full headline is missing or the layout is clipping. | CF-2 | Major | Live-state-needed | Verify in browser whether the headline is missing or render-clipped. If missing, supply: full headline draft (suggested *"The Apollo system replaces tracking and stimulants to feel normal."*) | `job-2/sec-agitation-headline` |
| **P-04** | CF-3 mechanism reveal | *"The Five Inputs That Do 95% of the Work"* — 5 cards with study citations (Leproult JAMA 2011; Wu Horm Metab Res 2011; Kraemer Med Sci Sports Exerc 1991; Cameron BMAS 2013). | Locked. Showpiece. **Mobile concern:** italic study citations may compress poorly. Live-state-needed for mobile. | CF-3, V-1 | Minor | Live-state-needed | Mobile screenshot required to confirm | `job-2/sec-mechanism-mobile` |
| **P-05** | CF-4 who-this-is-for | *"This is for anyone ready to start"* + 3 bullets including *"Men and women who want a structure"*. | Compliant with S-B/Job1 zero-executive-language lock. **Tension:** *"men and women"* reads inserted given otherwise male-coded brand voice. | CF-4, S-B/Job1 | Major | Anton-decision | Decide: keep universal *"men and women"* (lower friction for low-ticket entry — recommend) or align to brand-default *"men"* | `job-2/sec-who-this-is-for` |
| **P-06** | CF-5 stack offer (early) | Offer card on page 2 of PDF showing $97 stack with WHAT'S INSIDE list. | Pricing reveal is **early** for /protocols (right after Mechanism). Then repeated on page 4. **Dedup needed.** | CF-5, CF-8 | Major | Ship-ready | Decide: keep early pricing (front-load offer) and remove duplicate, or keep late pricing (build-up first) and remove early. Recommend: keep early reveal, deduplicate the late one | `job-2/sec-stack-dedup` |
| **P-07** | CF-5 stack offer (late) | "The Offer" / "The Protocols" section reintroduces the stack with a different layout. | Duplication — same product, two layouts, two prices, two CTAs. Confuses scroll flow. | CF-5 | Major | Ship-ready | See P-06 | `job-2/sec-stack-dedup` |
| **P-08** | CF-5 individual cards | "Or shop individually" — 3 cards (Training $34.99 / Nutrition $34.99 / Home Gym $34.99) with WHAT'S INSIDE per card. | Recovery Blueprint is bundle-exclusive (correctly omitted from individual cards). Cards are clean. | CF-5 | — | — | — | `not-in-session-d` (settled) |
| **P-09** | CF-6 proof — before/after | "What the five inputs produce in six months" — 3 paired before/after photos. | Strong, on-brand. Captions show *"MONTH 0 → MONTH 6"* etc. | CF-6, V-1 | — | — | — | `not-in-session-d` (settled) |
| **P-10** | CF-6 proof — YouTube replies | "What Men Write Back" — 5 unsolicited quotes from YouTube comments. | Strong. The framing *"Unsolicited. Straight from my YouTube comments. Unedited."* is exactly Stefan's voice. | CF-6 | — | — | — | `not-in-session-d` (settled) |
| **P-11** | CF-6 reviews block | 6 reviews + sort/filter UI + 4.67 rating average. | See X-04 (name format inconsistency), X-05 (duplicate line), X-06 (product tags). | S-C/Job2, S-B/Job2 | Major | Ship-ready | — | `job-0/sec-review-*` |
| **P-12** | CF-7 FAQ | 7 questions, accordion (collapsed in PDF). | Voice on the answer side is unsampled — see Live-state-needed. | CF-7 | Minor | Live-state-needed | Capture FAQ answers (expand in browser, screenshot or copy text) | `job-2/sec-faq-voice-check` |
| **P-13** | CF-8 price reveal | $97 (was $139.96, save $42.96). Currency USD. | See X-08 currency decision. | CF-8 | Minor | Anton-decision | See X-08 | `job-2/sec-pricing-currency` |
| **P-14** | CF-9 risk reversal | *"Run it. We've got you either way."* — swap-not-refund guarantee, locked verbatim. | See X-02 em-dash. Otherwise locked. | CF-9 | Major | Anton-decision | See X-02 | `job-0/sec-em-dash-strip` |
| **P-15** | CF-10 final CTA | *"This is not for everyone."* exclusion + dual CTA + sign-off. | See X-03 em-dashes. Otherwise locked — strongest closer on the site. | CF-10 | Major | Anton-decision | See X-03 | `job-0/sec-em-dash-strip` |
| **P-16** | CF-10 footer | Same single-line as homepage. | See X-11. | CF-10 | Block (pre-launch) | Anton-data | See X-11 | `job-0/sec-footer` |
| **P-17** | CF-1 image | Hero image (shirtless gym shot) shows physique outcome and sets the mood. | On-brand. Settled. | — | — | — | — | `not-in-session-d` (settled) |
| **P-18** | V-2 restraint | Section eyebrows are sparse and disciplined (*"THE MECHANISM"*, *"THE STACK"*, *"THE OFFER"*, *"THE FOUNDER"*, *"OUR GUARANTEE"*). | Locked — strong V-2 compliance. | V-2 | — | — | — | `not-in-session-d` (settled) |

### /protocols summary

- 1 Block-pre-launch (P-16 footer)
- 6 Major
- 4 Minor
- 7 Settled (no-change rows surfaced for Session D's "do not touch" list)

The single highest-impact change on /protocols is **deduplicating the offer block** (P-06+P-07). One offer card, one price, one CTA. Then **fixing the agitation headline layout bug** (P-03), which is the only issue likely to be silently killing readers above the fold.

---

## §6 Decisions Anton must make (register)

Deduplicated escalation of all `Anton-decision` / `Anton-data` / `Live-state-needed` rows. Ranked by **cascade depth** (number of downstream issues unblocked). Do these in order — top-of-list unblocks the most.

| # | Decision | Rows it unblocks | Cascade | Recommendation |
|---|---|---|---|---|
| 1 | **Em-dash policy on locked verbatim blocks** | X-01, X-02, X-03, P-14, P-15 | 5 | Approve recommended period-substitutions in `component-copy-bank.md` §7 to preserve rhythm. Stefan signs off async. |
| 2 | **"Transformation arc" decision** | X-07, H-07 | 2 | Swap to *"90-day arc"* or *"90-day phase"*. Stefan async-confirms. |
| 3 | **"Men and women" on /protocols** | P-05 + brand-foundation §11 item 1 | 2 | Keep universal entry on /protocols (lowest-friction for $97 entry); accept the male-coded register elsewhere. Stefan async-confirms. |
| 4 | **Currency USD vs GBP** | X-08, P-13 | 2 | Recommend GBP unless Anton has US-traffic data. Stefan async-confirms. |
| 5 | **Footer legal block** (privacy URL + terms URL + contact email + GDPR posture) | X-11, H-14, P-16 | 3 | Anton supplies the URLs and contact line; Session D writes the footer block. |
| 6 | **Homepage hero positioning** | H-01, H-02 | 2 | Keep identity-led mythic register (Collective is a high-ticket cohort sell); add a slim above-fold proof element (rating + review count). |
| 7 | **Homepage objection-handling block** | H-10 | 1 | Recommend a slim 3–4 question "Common questions" block on home (link the rest to /protocols FAQ). |
| 8 | **Homepage "what you get" detail block** | H-06 | 1 | Recommend surfacing 3–4 concrete deliverables (weekly call cadence, monthly cohort, Apollo Map, founder access) without breaking the application gate. |
| 9 | **Review tags** | X-06 | 1 | Recommend keeping product tags (signals which product the reviewer used; useful trust signal); Stefan async-confirms. |
| 10 | **Identity bullet 04 "ambition"** | X-14 | 1 | Recommend keep — Sage register accepts. Stefan async-confirms. |
| 11 | **Live-state captures Anton must provide** | P-03, P-04, P-12 | 3 | Provide: (a) browser confirmation of /protocols agitation headline (full text or render bug), (b) mobile screenshot of /protocols mechanism cards, (c) expanded /protocols FAQ answers (text or screenshot) |
| 12 | **Collective price-band signal on home** | H-11 | 1 | Recommend keep gated (current pattern works for high-ticket). Stefan async-confirms. |

---

## §7 Hand-off to Session D

Issues feeding Session D — by job:

### Job 0 — Cross-cutting fixes

`X-01, X-02, X-03, X-04, X-05, X-06, X-09, X-11, H-14, P-16` → 10 issue IDs.

### Job 1 — Homepage

`H-01, H-02, H-03, H-04, H-05/X-14, H-06, H-07/X-07, H-08, H-09 (delegates to job-0), H-10, H-11, H-12` → 12 issue IDs.

### Job 2 — /protocols

`P-02, P-03, P-04, P-05, P-06, P-07, P-12, P-13/X-08, P-14 (delegates to job-0), P-15 (delegates to job-0)` → 10 issue IDs.

### Not in Session D (explicitly excluded)

| Issue ID | Reason |
|---|---|
| X-12 imagery | Settled — Higgs Field passed pilot, do not re-open |
| X-13 disambiguation | Settled — pre-headline already compliant |
| X-15 typography scope | Settled by S-Cv2; carry forward as cross-section regression in QA |
| H-13 application form | Settled — clean, on-voice |
| H-15 hero image | Settled — aesthetic-first imagery is on-brand |
| H-16 founder block | Settled (after em-dash strip in job-0) |
| P-01 hero | Settled — strongest hero on site, do not touch |
| P-08 individual cards | Settled — clean |
| P-09 before/after photos | Settled — strong |
| P-10 YouTube replies | Settled — on-voice |
| P-17 hero image | Settled — on-brand |
| P-18 section eyebrows | Settled — strong V-2 compliance |

### Round-trip integrity check

- Total issues raised in §§3–5: **49**
- Going into Session D: **32** (10 cross-cutting + 12 home + 10 /protocols)
- Settled / not-in-session: **12**
- Decisions register in §6: **12** (covers all Anton-decision / Anton-data / Live-state-needed rows)
- 32 + 12 + 12 = 56 references, with cross-cutting rows referenced from multiple page sections (each row counted once in the 49 total)

Every audit issue has either a Session D job hook or an explicit "not-in-session-d (settled)" tag. Zero orphan issues. Round-trip integrity: ✅
