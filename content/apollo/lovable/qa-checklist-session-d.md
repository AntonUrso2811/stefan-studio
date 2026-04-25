# QA Checklist — Lovable Session D (Conversion Polish)

**Pairs with:** `session-d-conversion-polish.v1.md`
**Run:** before Anton signs off, before Stefan async-review, before production publish.
**Format:** every line is a binary check. Any unchecked = ship halts.

---

## Pre-flight gates (verify each one passed before Session D ran)

- [ ] Gate 1 — Live-state PDFs at `~/Downloads/screencapture-preview-apollo-ascension-landing-lovable-app{,-protocols}-2026-04-25-08_3*.pdf` were the audit basis
- [ ] Gate 2 — Pricing locked at $97 stack / $34.99 individual; currency-decision deferred is acknowledged
- [ ] Gate 3 — Guarantee verbatim preserved (only em dash stripped)
- [ ] Gate 4 — /protocols hero locked verbatim; homepage hero kept identity-led mythic
- [ ] Gate 5 — Voice foundation route waiver acknowledged (extracted T1–T5; Stefan async)
- [ ] Gate 6 — Module body content untouched in this session
- [ ] Gate 7 — Higgs Field imagery state unchanged; no re-opening of pilot decision
- [ ] Gate 8 — Footer legal data supplied (privacy URL, terms URL, contact email, GDPR/cookie line) before Session D fired
- [ ] Gate 9 — /protocols agitation headline state confirmed in browser (render-clipped only OR missing-string-supplied)

---

## Job 0 — Cross-cutting verification

### 0.1 — Em-dash strip
- [ ] /protocols founder block: zero em dashes; rebuilt sentence reads *"Then something clicked and I rebuilt. Body first, then everything else."*
- [ ] Guarantee block (both surfaces): zero em dashes; reads *"…swap the blueprint for a different one. Or coach you through what's not working."*
- [ ] /protocols final exclusion block: zero em dashes; triad-of-fragments rewrite shipped (or comma fallback if approved)
- [ ] Em-dash scan across **all customer-facing strings on home and /protocols**: zero hits

### 0.2 — Reviews name format
- [ ] All 6 reviews use first-name + last-initial + period (Liam R., Nathan L., Richard T., Joe M., Matthew S., Niall O.) — or Anton-confirmed initial set
- [ ] No surnames in full anywhere in the reviews block

### 0.3 — Reviews duplicate dedup
- [ ] Liam's review no longer contains *"Stefan writes like a man who has actually done it"*
- [ ] Joe's review still contains the original line verbatim
- [ ] Liam's review reads as: *"I'd plateaued for eighteen months and stopped photographing my back. Hit a 180kg deadlift at thirty-nine. Hadn't seen that since university. Will keep running the inputs after the 90 days."*

### 0.4 — Review tags decision
- [ ] Product tags retained on each review card (TRACKING BLUEPRINT / THE COLLECTIVE / NUTRITION BLUEPRINT / RECOVERY BLUEPRINT)
- [ ] Decision recorded as settled in this checklist

### 0.5 — Header navigation
- [ ] Home and /protocols both render `MEN OF APOLLO | PRICING REVIEWS PROTOCOLS` (or Anton-overridden alternative)
- [ ] Nav strings byte-identical between the two pages

### 0.6 — Footer legal block
- [ ] Both pages render the new footer with: copyright line, Privacy link, Terms link, Contact email (mailto:), GDPR/cookie line
- [ ] All four placeholders filled with Anton-supplied values
- [ ] Footer typography is token-default (no new primitives)

---

## Job 1 — Homepage, per-section pass/fail

### 1.1 Hero
- [ ] Headline, sub, kicker, image, primary CTA, secondary CTA all unchanged
- [ ] New proof anchor (4.67 stars · 6 verified reviews) inserted between sub-line and primary CTA
- [ ] Proof anchor reuses existing star-rating component (no new primitive)

### 1.2 Identity bullets
- [ ] All 4 bullets unchanged verbatim (including bullet 04 *"a body that matches their ambition"*)
- [ ] Qualifier closer *"If three of the four lines describe you, keep reading."* unchanged

### 1.3 NEW — Problem agitation block
- [ ] New section inserted between identity bullets and reviews block
- [ ] Eyebrow *"THE PLAN YOU WERE HANDED"*; heading *"It's not you. It's the plan."*
- [ ] Body 3–6 sentences; includes at least one anaphoric-No or "without [X]" construction
- [ ] Zero em dashes
- [ ] No imagery in this block (typographic only)
- [ ] Voice spot-check passes (Anton reads aloud — sounds like Stefan)

### 1.4 NEW — Mechanism reveal
- [ ] New section inserted after problem agitation
- [ ] Eyebrow *"THE MECHANISM"*; heading *"The Five Inputs That Do 95% of the Work"* (matches /protocols heading verbatim)
- [ ] 5 cards rendered: Sleep · Sunlight · Heavy Compound Lifts · Real Food · A Calm Nervous System
- [ ] Each card body ≤ 25 words
- [ ] No study citations on home cards (those stay on /protocols)
- [ ] Foot link *"See how each input runs in detail →"* points to /protocols Mechanism anchor
- [ ] Cards reuse the /protocols Mechanism card component (no new primitive)
- [ ] Typographic-only imagery in cards on home

### 1.5 NEW — "What you get inside the Collective"
- [ ] New section inserted after Mechanism reveal
- [ ] Eyebrow *"INSIDE THE COLLECTIVE"*; heading *"What every member runs."*
- [ ] 4 deliverable cards rendered (cohort phase / weekly call / Apollo Map / direct coaching from Stefan)
- [ ] Voice register: minimalist-operator
- [ ] Foot link *"Or start with the Protocols → /protocols"*
- [ ] Cards reuse existing card component

### 1.6 The Standard cards (single substitution)
- [ ] *"transformation arc"* → *"90-day arc"* (only in the 90-day card)
- [ ] All other text in all 6 cards unchanged

### 1.7 Reviews position
- [ ] Reviews block now sits between "The Standard" 6-card block and "Proof" before/after block
- [ ] Reviews content (6 reviews + rating + sort/filter) unchanged from pre-Session-D
- [ ] Reviews block is byte-identical to /protocols reviews block (one-source-three-placements survives)

### 1.8 NEW — Common questions block
- [ ] New section inserted between "Replies" (YouTube comments grid) and "The Founder" block
- [ ] Heading *"Before you apply."*
- [ ] 3–4 question/answer pairs, all answers visible (not collapsed)
- [ ] Each answer ≤ 25 words
- [ ] Zero em dashes
- [ ] *"What does this cost?"* answer does NOT surface a price band
- [ ] Foot link *"Full FAQ on the Protocols page →"* to /protocols FAQ anchor

### 1.9 NEW — Risk reversal anchor
- [ ] One-sentence anchor inserted in "Before the Collective" block, after existing copy *"Run solo until the next cohort opens"*
- [ ] Anchor reads (or matches): *"Either way, you're covered. Run the 90-day programme. If by day 30 your energy, sleep, and strength haven't moved in the right direction, we swap the blueprint or coach you through it."*
- [ ] Existing CTA unchanged
- [ ] Zero em dashes

### 1.10 Pricing band on home
- [ ] No price band shipped on home (Collective stays application-gated — settled)

---

## Job 2 — /protocols, per-section pass/fail

### 2.1 Hero
- [ ] Headline, sub, kicker, image, primary CTA, secondary CTA all unchanged

### 2.2 Hero proof anchor
- [ ] Proof anchor (4.67 stars · 6 verified reviews) inserted below "Or apply for the Collective" link
- [ ] Same component as Job 1.1

### 2.3 Problem agitation headline
- [ ] **Conditional check:**
  - If render-clipped: section header above the *"and stimulants to feel normal"* image is fully visible at 320px / 375px / 414px / 1024px / 1440px viewport widths
  - If missing-string-supplied: Anton-supplied headline string inserted verbatim above the image
- [ ] Block surrounds and body copy unchanged

### 2.4 Mechanism cards
- [ ] All 5 cards unchanged in copy
- [ ] Mobile QA at 320 / 375 / 414 px: italic study citations remain readable (legibility check)
- [ ] If a CSS adjustment was made for mobile citations, scoped to `.mechanism-card .citation` only — no other typography touched

### 2.5 Who is this for
- [ ] All 3 bullets unchanged verbatim (including *"Men and women who want a structure to follow…"*)

### 2.6 Stack offer dedup
- [ ] One stack-offer card on /protocols (not two)
- [ ] Surviving card shows: $97 price, was $139.96, save $42.96, 4-blueprint WHAT'S INSIDE list, 4.67-star rating with VERIFIED REVIEWS count, primary CTA *"GET THE FULL STACK →"*, BEST VALUE badge
- [ ] Removed placement is fully gone (no orphan elements, no broken section eyebrow)
- [ ] No new layout primitive introduced

### 2.7 Individual cards
- [ ] 3 cards (Training / Nutrition / Home Gym) unchanged
- [ ] Recovery Blueprint not surfaced as individual SKU
- [ ] All 3 prices read $34.99

### 2.8 Proof / Replies / Reviews
- [ ] Before/after photos block unchanged (3 paired photos + section header)
- [ ] YouTube replies block unchanged (5 quotes + sub-line)
- [ ] Reviews block normalised per Job 0 (name format, dedup, tags); content otherwise unchanged

### 2.9 FAQ
- [ ] All 7 FAQ answers surfaced as text in the Final output (Lovable expanded them)
- [ ] Anton voice-checked the answers — passed (or fix shipped)

### 2.10 Pricing currency
- [ ] USD currency unchanged
- [ ] Currency-decision flagged for Stefan async

### 2.11 Guarantee block
- [ ] Em-dash stripped per Job 0.1
- [ ] All other guarantee text unchanged

### 2.12 Final exclusion block
- [ ] Em dashes stripped per Job 0.1
- [ ] All other exclusion-block text unchanged
- [ ] *"NINETY DAYS. FIVE INPUTS. ONE STANDARD."* kicker unchanged
- [ ] *"— I'll see you inside."* sign-off unchanged (note: this is an em-dash-followed-by-space, used as a sign-off prefix; preserve as Stefan's signature closer; not subject to em-dash strip rule which applies to mid-sentence dashes)

---

## Job 3 — Plumbing

- [ ] No new primitives introduced (or, if introduced, documented in Final output with name + props shape + justification)
- [ ] No global token changes
- [ ] No lander typography drift since C v2

---

## Cross-section regression (locks survived)

The most important block in this checklist. Any failure here halts ship.

### Verbatim contract on module bodies (S-A v2)
- [ ] Random spot-check: open `/modules/welcome` (MOA_01), copy paragraph 1 of body, compare to `content/apollo/modules/module-01-welcome.md` body paragraph 1 — byte-identical
- [ ] Same spot-check on `/modules/nutrition-optimisation` (MOA_10) — byte-identical
- [ ] Same spot-check on `/modules/the-integrated-life` (MOA_20) — byte-identical

### Reviews — one source, three placements (S-B/Job2)
- [ ] Home reviews block, /protocols reviews block, and the Collective deflection (if it shows reviews) all read the **same 6 reviews** from a single data source
- [ ] All three placements show the same star rating (4.67), same count (6), same sort/filter UI

### Reviews de-AI'd (S-C/Job2)
- [ ] Zero em dashes in any review body
- [ ] No review uses banned-lexicon (journey, transformative, game-changer, etc.)
- [ ] Names in first-name + last-initial format
- [ ] Liam's review no longer contains the duplicate Stefan-line

### Higgs Field imagery (S-C/Job3)
- [ ] All photographic imagery on home + /protocols is the same as pre-Session-D (Italian rooftop hero on home; gym hero, before/after triad, founder block image, lifestyle blocks on /protocols)
- [ ] No new image generation occurred
- [ ] No image was replaced or regenerated

### Protocol-lander zero-executive-language (S-B/Job1)
- [ ] /protocols still uses universal-entry "Anyone ready to start" framing
- [ ] Zero instances of: executive, founder, CEO, business owner, entrepreneur, high-performer (in any /protocols copy)

### Module-pages typography (S-Cv2)
- [ ] Module pages render identically to post-C-v2 state — body 18/1.65 mobile and 19/1.7 desktop, 66ch measure, hair-rule h2s, auto-TOC from h2 only, scroll-progress bar
- [ ] No lander typography token changed

---

## Output handover

- [ ] Lovable's Final output produced in the exact shape specified in the prompt
- [ ] FAQ answers (all 7) included as text in Final output
- [ ] Voice-check confirmation block (refused-vocab / em-dash / CTA register / lock-survival) included
- [ ] Preview URL provided
- [ ] Commit boundary hash provided
- [ ] Lovable did not push to production

---

## Sign-off triggers (binary)

- [ ] **Anton sign-off:** all checks above pass; no rollback triggers fired; ready to send to Stefan async
- [ ] **Stefan async-review:** binary "ship" or "re-do with notes"; if "re-do" trigger rollback per session-d-conversion-polish.v1.md §Rollback
- [ ] **Production publish:** only after Stefan ships — preview URL → production deployment

---

## Rollback readiness

- [ ] Pre-Session-D commit hash documented (recorded in Final output before Session D fires)
- [ ] Lovable snapshot ID documented at the same point
- [ ] No DB migration debt (Session D has no schema changes)
- [ ] Revert path tested: ≤ 2 minutes from "rollback" call to preview reverted
- [ ] Trigger conditions list (5 items) is on every reviewer's screen during sign-off
