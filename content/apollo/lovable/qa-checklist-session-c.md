# Session C QA Checklist — four final polish fixes

Internal gate. Anton ticks every box BEFORE Stefan handover. Session C assumes Session A (20 modules loaded, verbatim body) and Session B (Protocol "Who is this for?" universal-entry, reviews consolidated to one universal block) are live.

## Pre-flight (before pasting the Session C prompt)

- [ ] Job 1 prerequisite complete: h2/h3 headings added to all 20 source MD files in `content/apollo/modules/`, each reviewed by Anton, committed in a dedicated pass before this session
- [ ] Diff verification: running `git diff --word-diff HEAD~1 HEAD -- content/apollo/modules/` shows ONLY added heading lines (`^#` or `^##` or `^###`) and matching blank-line spacing — zero changes to body prose
- [ ] Session A verbatim contract re-affirmed in `session-c-final-polish.v1.md` (structural headings framed as presentation, not content edit)
- [ ] Session A + B live previews signed off and Stefan has acknowledged them
- [ ] `content/apollo/lovable/pre-integration-snapshot/` still exists as rollback baseline (Session B snapshot)
- [ ] Anton's admin email for `/admin/reviews` gating is confirmed (Anton pastes separately — not hard-coded in the prompt)

## Job 1 — Module hierarchy + typography

### Typography
- [ ] Body text is 18px / 1.65 line-height on mobile, 19px / 1.7 on desktop (DOM computed style check)
- [ ] Measure capped at 66ch on desktop, 92vw on mobile
- [ ] Paragraph spacing is 1.25em, no first-line indent
- [ ] h1 matches spec (40/44 mobile, 56/60 desktop, letter-spacing −0.015em)
- [ ] h2 matches spec (28/34 mobile, 32/40 desktop, 2.5em top / 0.75em bottom margin, hair-rule border-top above)
- [ ] h3 matches spec (22/28 mobile, 24/30 desktop, 1.75em top / 0.5em bottom margin)
- [ ] Frontmatter lede renders at 22/30 mobile, 26/34 desktop, 400 weight, 70% opacity

### Auto-TOC + scroll progress
- [ ] Auto-TOC renders on module pages, derived from h2 headings only (not h3)
- [ ] Desktop: TOC in right-side margin OR inline above first h2 (whichever Lovable chose) — positioning stable on scroll
- [ ] Mobile: collapsible sticky drawer reachable from top-right, opens/closes cleanly, auto-closes on anchor tap
- [ ] Active h2 highlights as user scrolls past it
- [ ] Scroll-progress bar renders on module pages only (NOT on landers or home)
- [ ] Progress bar is 2px, hairline Apollo accent, fixed top of viewport, fills left-to-right

### Regression + verbatim
- [ ] Module body prose is byte-identical to the updated source MD (pick 3 modules at random, DOM extract, diff against file)
- [ ] Mobile 320px render: no text cut off, no horizontal scroll, TOC drawer reachable without stretching
- [ ] Mobile 375px and 414px render: clean
- [ ] Stress-test on `module-10-nutrition-optimisation.md` (largest, 5,568 words) — page is scannable, TOC navigable
- [ ] Phase gating from Session A still works (Day 0/30/60/90 unlock gates)
- [ ] Frontmatter-driven card metadata on module list pages unchanged

## Job 2 — Reviews rewrite (de-named + de-AI'd)

### Content
- [ ] Exactly 4 reviews in the universal block (count in DOM)
- [ ] Same 4 reviews appear on home + Protocol lander + Community lander (one source, three placements)
- [ ] Each name is first name + last initial maximum (regex: `^[A-Z][a-z]+ [A-Z]\.$`)
- [ ] Zero full surnames anywhere in the reviews block (grep DOM)
- [ ] Zero references to: executive, founder, high-performer, business-owner, entrepreneur, CEO, industry, role, company
- [ ] Zero product specifics: "module", "phase", "framework", "Apollo", "protocol", "nutrition plan", "training plan" — none appear in any review
- [ ] Zero metric or result numbers in any review
- [ ] Zero em dashes (—) across all reviews (grep)
- [ ] Zero semicolons, zero mid-sentence colons (grep)
- [ ] No review uses "journey", "transformative", "game-changer", "life-changing", "blown away", "next level", "unreal", "mind-blowing"
- [ ] No review is three perfectly-balanced superlative sentences
- [ ] No review opens with "I love" or "I was blown away"

### Rhythm
- [ ] Across the 4-entry set, at least 2 reviews have a sentence ≤ 5 words
- [ ] Across the 4-entry set, at least 2 reviews have a sentence > 20 words
- [ ] Read every kept review aloud — none sound AI-written

### Cleanup
- [ ] Any Session B review that named a collective member — removed from DOM
- [ ] Any Session B review that mentioned a specific module/phase/product — removed from DOM

## Job 3 — Imagery: Higgs Field pilot OR remove

### Pilot pass
- [ ] Higgs Field confirmed available in Lovable image picker. If not: STOPPED, pilot not attempted, affected slots listed for Anton to run externally
- [ ] Exactly 1 hero (Template 1) + 1 module card (Template 2) generated in pilot
- [ ] Pilot prompts match the templates in `session-c-final-polish.v1.md` verbatim, with global positive DNA and global negative prompt included
- [ ] Pilot URLs + exact prompts reported back in Lovable output
- [ ] Testimonial Template 3 NOT yet generated (batch only, after Stefan approval)

### Stefan gate (binary)
- [ ] Stefan has seen the 2 pilot images
- [ ] Stefan's binary pass/fail recorded in CHANGELOG before any batch regen

### If pilot PASSES
- [ ] Batch regen uses same global DNA + negative prompt on every image
- [ ] Aspect ratios correct: 16:9 hero (1920×1080), 4:3 module card (1200×900), 1:1 testimonial (800×800)
- [ ] Every batched image exports clean — no logos, watermarks, text overlays
- [ ] Logos, icons, diagrams, non-photographic illustrations UNTOUCHED
- [ ] Spot-check 3 random images against "photoreal enough" criteria (pores, window catchlight, lived-in physique, environment imperfection)

### If pilot FAILS (fallback)
- [ ] All photographic imagery removed across home + Protocol lander + Community lander + module pages
- [ ] Hero slots replaced with typography-on-whitespace treatment (single large headline, whitespace, hair-rule, lede as sub)
- [ ] Module cards replaced with typography cards (title + frontmatter lede)
- [ ] Testimonial avatars replaced with initials-in-circle (first + last initial matching review names)
- [ ] No broken image references anywhere (DOM scan)
- [ ] Fallback logged in CHANGELOG + Lovable output summary

## Job 4 — Customer review submission

### Form
- [ ] Form renders below universal reviews block on home + Protocol lander + Community lander
- [ ] Section heading "Share your experience" present
- [ ] Sub-copy "Real reviews only. We read every one." present
- [ ] Fields: name (first + last initial, regex enforced), rating (1–5 stars), review_text (250-char cap + live counter), email (required), honeypot (hidden)
- [ ] Submit button uses existing Apollo accent token (no new primitive)

### Supabase
- [ ] Table `review_submissions` created with columns: id, name, rating, review_text, email, status (default `pending`), submitted_at, ip_hash, approved_at, approved_by
- [ ] RLS: insert-only from public; select/update gated to admin
- [ ] Edge function `rate-limit-review-submission` enforces 1 submission per ip_hash per 24h
- [ ] Test: 2nd submission from same IP within 24h returns the friendly 200 message, not an error
- [ ] Test: honeypot-filled submission is silently rejected
- [ ] Test: valid submission writes a row with `status = pending`

### Admin route
- [ ] `/admin/reviews` exists
- [ ] Auth gate: only Stefan's email + Anton's email can access
- [ ] Pending submissions listed with name, rating, review_text, email, submitted_at
- [ ] Approve action: sets status=approved, approved_at=now(), approved_by=<admin email>, strips em dashes from review_text
- [ ] Reject action: sets status=rejected, review does not publish
- [ ] Approved reviews surface via a `reviews_published` view that the universal reviews block reads
- [ ] Test: approve a submission, confirm it appears in the live reviews block only AFTER approval

### Email fallback (if admin route gating fails)
- [ ] On submission, email sent to Stefan + Anton with content + signed approve/reject links
- [ ] Approve link hits an edge function that moves the row into `reviews_published`
- [ ] Reject link sets status=rejected
- [ ] Fallback logged in Lovable output summary

## Cross-section regression

- [ ] Session A: 20 modules still render, verbatim body preserved (modulo new heading lines), phase gating intact
- [ ] Session B: Protocol lander "Who is this for?" still universal-entry (zero business/executive references)
- [ ] Session B: universal reviews block still placed on all three landers (now with new Session C copy)
- [ ] No accidental edits outside the four fix surfaces
- [ ] Mobile + desktop render pass across all edited pages
- [ ] No console errors, no 404s on any module page, no broken anchor links in auto-TOC

## Rollback readiness

- [ ] Pre-Session-C module MD files recoverable via `git checkout <pre-session-c-commit> -- content/apollo/modules/` if heading pass needs rework
- [ ] Session B pre-integration imagery snapshot still at `content/apollo/lovable/pre-integration-snapshot/hero-imagery/` (untouched)
- [ ] If Higgs fallback engaged: one-line revert plan documented in CHANGELOG (e.g. "re-upload pre-integration hero to /hero-image-1 if Stefan changes mind")

## Output + handover

- [ ] Lovable's session output logged with the six-point summary (changes, typography spec, reviews kept/removed, Higgs pilot URLs+prompts, form+admin config, unfinished items)
- [ ] Summary-of-changes doc prepared for Stefan (plain-language)
- [ ] Preview deploy URL ready (production publish only after Stefan sign-off)
- [ ] `content/apollo/lovable/CHANGELOG.md` updated with v1 execution date + any deviations from the spec
- [ ] If rework needed → bump to `session-c-final-polish.v2.md`, log why in CHANGELOG

## Stefan sign-off trigger

Once all boxes above are ticked:
1. Hand Stefan the preview URL + summary-of-changes doc
2. Stefan walks through the site on mobile + desktop
3. Stefan hits the Higgs pilot binary gate (pass/fail) and records decision
4. If pass: batch regen + QA re-run before full sign-off
5. Stefan signs off with explicit "it's done"
6. Publish from preview → production
7. Commit the final prompt versions + any Stefan-requested edits to stefan-studio
