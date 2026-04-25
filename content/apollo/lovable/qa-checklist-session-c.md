# Session C v2 QA Checklist — modules typography pass (modules-only)

Internal gate. Anton ticks every box BEFORE Stefan handover. Session C v2 assumes Session A (20 modules loaded, verbatim body) and Session B (Protocol "Who is this for?" universal-entry, reviews consolidated) are live. v2 is **modules-only** — Jobs 2–4 from v1 (reviews rewrite, Higgs Field imagery, customer review submission) are deferred to Session D.

## Pre-flight (before pasting the Session C v2 prompt)

- [ ] Repo h2/h3 work confirmed live on main: `git log origin/main` shows `f1353c6` merged via `05104b7`
- [ ] Spot-check one module file in repo (e.g. `module-05-nutrition-framework.md`) — has `## ` and `### ` heading lines above paragraph groups
- [ ] Pre-v2 screenshots captured for **home, /protocols, /community** (will be used to verify those surfaces are unchanged after v2 deploys)
- [ ] Session A + B live previews still signed off

## Job 1 — Module pages: hierarchy + typography

### Typography
- [ ] Body text is 18px / 1.65 line-height on mobile, 19px / 1.7 on desktop (DOM computed style check)
- [ ] Measure capped at 66ch on desktop, 92vw on mobile
- [ ] Paragraph spacing is 1.25em, no first-line indent
- [ ] h1 matches spec (40/44 mobile, 56/60 desktop, letter-spacing −0.015em)
- [ ] h2 matches spec (28/34 mobile, 32/40 desktop, 2.5em top / 0.75em bottom margin, hair-rule border-top above)
- [ ] h3 matches spec (22/28 mobile, 24/30 desktop, 1.75em top / 0.5em bottom margin)
- [ ] Frontmatter lede renders at 22/30 mobile, 26/34 desktop, 400 weight, 70% opacity (only on module pages that have one)

### Auto-TOC + scroll progress
- [ ] Auto-TOC renders on module pages, derived from h2 headings only (not h3)
- [ ] Desktop: TOC in right-side margin OR inline above first h2 (whichever Lovable chose) — positioning stable on scroll
- [ ] Mobile: collapsible sticky drawer reachable from top-right, opens/closes cleanly, auto-closes on anchor tap
- [ ] Active h2 highlights as user scrolls past it
- [ ] Scroll-progress bar renders on module pages only (NOT on landers, NOT on home)
- [ ] Progress bar is 2px, hairline Apollo accent, fixed top of viewport, fills left-to-right

### Mobile readability + verbatim
- [ ] Module body prose is byte-identical to the source markdown (pick 3 modules at random, DOM extract minus heading text, diff against `content/apollo/modules/module-NN-*.md`)
- [ ] Mobile 320px render: no text cut off, no horizontal scroll, TOC drawer reachable without stretching
- [ ] Mobile 375px and 414px render: clean
- [ ] Stress-test on `module-10-nutrition-optimisation.md` (largest, 5,568 words) — page is scannable, TOC navigable
- [ ] Phase gating from Session A still works (Day 0/30/60/90 unlock gates)
- [ ] Frontmatter-driven card metadata on module list pages unchanged

## Cross-section regression — non-module surfaces MUST be unchanged

This is the critical scope-bleed check. Compare each surface against the pre-v2 screenshots captured in pre-flight.

- [ ] **Home page**: typography, layout, copy, hero, all components — pixel-identical (allow only sub-pixel font rendering differences)
- [ ] **/protocols lander**: typography, "Who is this for?" block, all sections — unchanged
- [ ] **/community lander**: typography, all sections — unchanged
- [ ] **Universal reviews block** (wherever it currently lives, home + Protocol + Community): exactly the same review entries, names, and copy as before v2
- [ ] **Imagery** (hero, module card, testimonial photos): same images as before v2 — no regen, no removal
- [ ] **Navigation chrome and footer**: unchanged
- [ ] **Type tokens**: if Lovable changed any global body / heading type tokens, confirm those changes are scoped to module pages only and do not bleed into any other surface
- [ ] DOM grep across home / /protocols / /community: zero unexpected changes flagged

## Lovable output verification

- [ ] Lovable's session output includes the four-point summary (changes, typography spec, regression confirmation, unfinished items)
- [ ] Lovable explicitly confirmed in writing: home, /protocols, /community, reviews block, imagery, and review submission area are unchanged from pre-v2 state
- [ ] Preview deploy URL is ready (production publish only after Stefan sign-off)

## Rollback readiness

- [ ] Pre-v2 typography state recoverable via Lovable's version history (or via re-applying old type token values from screenshots if needed)
- [ ] Repo-side: h2/h3 source markdown is independent of Lovable render — even a full Lovable rollback leaves the repo state intact

## Output + handover

- [ ] Summary-of-changes doc prepared for Stefan — emphasising "modules read better, landers untouched, reviews and photos coming in next round with the audit"
- [ ] `content/apollo/lovable/CHANGELOG.md` updated with the v2 execution date + any deviations from spec
- [ ] If rework needed → bump to `session-c-final-polish.v3.md`, log why in CHANGELOG

## Stefan sign-off trigger

Once all boxes above are ticked:
1. Hand Stefan the preview URL + summary-of-changes doc
2. Suggest he walk module-05 (nutrition framework), module-10 (nutrition optimisation), and module-19 (longevity) on mobile and desktop — these are the densest, where the typography fix matters most
3. Stefan signs off with explicit "modules read better"
4. Publish from preview → production
5. Commit any Stefan-requested edits to stefan-studio
