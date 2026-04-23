# Session B QA Checklist — three feedback fixes

Internal gate. Anton ticks every box BEFORE Stefan handover. Pre-integration snapshot at `content/apollo/lovable/pre-integration-snapshot/` MUST exist before Session B runs (rollback baseline).

## Pre-flight (before pasting the Session B prompt)

- [ ] Pre-integration snapshot committed — screenshots of Protocol lander + Community lander + home + imagery + current reviews text
- [ ] Current imagery downloaded to `pre-integration-snapshot/hero-imagery/` as rollback baseline
- [ ] `{{IMAGE_MODEL}}` placeholder in `session-b-feedback-fixes.v1.md` replaced with confirmed model name (or placeholder strategy selected)
- [ ] Voice anchor passages selected from the live site and pasted into the prompt as positive reference
- [ ] Session A live and signed off (Session B assumes 20 modules already loaded)

## Job 1 — Protocol lander "Who is this for?" rewrite

- [ ] Current business-people-focused block removed entirely
- [ ] Replaced with universal-entry copy per the draft anchors (adapted to live-site voice)
- [ ] Zero references to: executives, founders, high-performers, business-owners, entrepreneurs, CEOs
- [ ] Copy reads aloud cleanly — matches Stef's live-site voice rhythm
- [ ] Community lander "Who is this for?" UNCHANGED (high-ticket framing preserved)
- [ ] Spot-check in browser: Protocol lander section vs Community lander section — clearly differentiated audiences
- [ ] Mobile + desktop render clean

## Job 2 — Reviews consolidation

- [ ] Per-product review sections deleted — nutrition page, training page, any others
- [ ] ONE universal reviews section created
- [ ] Section reused in: home page, Protocol lander, Community lander
- [ ] NOT re-fragmented into multiple sections
- [ ] 4–6 reviews total (count exactly)
- [ ] Each review passes all three criteria: specific detail, human rhythm, Stef-adjacent voice
- [ ] Every review that opens with "I love" / uses "transformative|journey|game-changer" without context / reads as balanced superlatives — removed
- [ ] Removed reviews archived in Lovable (draft block or hidden `/reviews-archive` page) — NOT hard-deleted
- [ ] Read every kept review aloud — none read AI-written
- [ ] If borderline, preserved (Stefan's final cut decision)

## Job 3 — Imagery regeneration

- [ ] `{{IMAGE_MODEL}}` locked into prompt BEFORE execution
- [ ] Pilot pass completed: ONE hero + ONE module card only
- [ ] Pilot regenerated with the named model (confirm in output metadata/URL)
- [ ] If named model unavailable: STOPPED, listed affected images, no silent fallback to prior model
- [ ] Anton's aesthetic-gate approval on pilot BEFORE batch
- [ ] Batch regen executes only after pilot approval
- [ ] All regenerated images match direction: lived-in physique/lifestyle, natural light, real environments
- [ ] Zero images read as generic gym stock / AI-sheen / over-polished "fitness hero" tropes
- [ ] Aspect ratios correct: hero 16:9, module card 4:3, testimonial 1:1
- [ ] Logos, icons, diagrams, non-photographic illustrations UNTOUCHED

## Rollback readiness

- [ ] Current (pre-regen) imagery still present at `pre-integration-snapshot/hero-imagery/`
- [ ] If pilot missed: one-line revert plan documented (e.g. "re-upload pre-integration hero to /hero-image-1")
- [ ] Removed reviews retrievable from archive location

## Cross-section

- [ ] Session A's 20 modules still render correctly (no regression from Session B edits)
- [ ] No accidental edits outside the three fix surfaces (landers, reviews, imagery)
- [ ] Mobile + desktop render pass across all edited pages

## Output + handover

- [ ] Lovable's session output logged — summary of every change, before/after Protocol snippet, reviews kept/archived lists, image URLs regenerated
- [ ] Summary-of-changes doc prepared for Stefan
- [ ] Preview deploy URL ready (production publish only after Stefan sign-off)
- [ ] `content/apollo/lovable/CHANGELOG.md` updated with the v1 execution date + any deviations
- [ ] If rework needed → bump to `session-b-feedback-fixes.v2.md`, log why in CHANGELOG

## Stefan sign-off trigger

Once all boxes above are ticked:
1. Hand Stefan the preview URL + summary-of-changes doc
2. Stefan walks through the site on mobile + desktop
3. Stefan signs off with explicit "it's done"
4. Publish from preview → production
5. Commit the final prompt versions + snapshot to stefan-studio
