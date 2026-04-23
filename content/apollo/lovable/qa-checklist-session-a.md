# Session A QA Checklist — 20-module load

Internal gate. Anton ticks every box BEFORE Stefan handover. Any unchecked box = fix or document as flagged.

## Coverage

- [ ] 20 module pages live (preview URL walkthrough)
- [ ] MOA_01 Welcome — Onboarding card, shared tier
- [ ] MOA_02–07 — Phase 1 Foundation card, protocol + community visible
- [ ] MOA_08–13 — Phase 2 Integration card, community only
- [ ] MOA_14–18 — Phase 3 Mastery card, community only
- [ ] MOA_19–20 — Phase 4 Longevity card, community only
- [ ] Program index page matches `content/apollo/modules/index.md`

## IA + gating

- [ ] Phase cards render in order: Onboarding · Phase 1 · Phase 2 · Phase 3 · Phase 4
- [ ] Phase 2 locked for accounts under Day 30; Phase 3 under Day 60; Phase 4 under Day 90
- [ ] Lock state shows "Unlocks Day X" not just "Locked"
- [ ] Admin-unlock (test account) works for QA
- [ ] Revisit-anytime works — can return to a completed module
- [ ] Protocol-tier test account sees ONLY Onboarding + Phase 1 cards
- [ ] Community-tier test account sees all five phase cards
- [ ] Shared tier (MOA_01) visible to both test accounts

## Module page rendering

- [ ] Lede rendered as hero quote (not buried)
- [ ] Summary rendered as intro paragraph, not H2 header
- [ ] Content map renders as TOC with in-page anchor links
- [ ] Anchor links actually jump to sections in Full body
- [ ] Frameworks / protocols rendered as visual cards, not plain text
- [ ] Visual callouts rendered with best-match existing component (spot-check MOA_05 Apollo Plate, MOA_11 HRV Deviation card, MOA_20 Environment Audit)
- [ ] Full body preserves Stef's prose verbatim — no rewrites, no AI-smoothing
- [ ] `next_step` CTA links to the next module in sequence
- [ ] "Back to phase" link works

## Voice + content fidelity

- [ ] Read aloud Summary of 3 random modules — matches Stef's rhythm (direct, no filler, no "additionally" / "moreover")
- [ ] Full body passages checked against `content/apollo/source-pdfs/MOA_NN_*.pdf` originals — no deviations
- [ ] British-English spellings preserved (optimisation, recognise, prioritise, behaviour)
- [ ] "Men of Apollo" terminology intact across modules
- [ ] Phase 4 (MOA_19–20) references to "Phase 4" and "ninety-plus days" intact

## Cross-references

- [ ] Module dependencies resolve — if MOA_16 says "see Module 1" that links to Phase 3 Module 1 (MOA_14 or 15 depending on mapping), not the global MOA_01
- [ ] References to "Phase 1" / "Phase 2" in prose are internally consistent with the phase-card IA
- [ ] Phase-opener modules (MOA_02, MOA_08 via MOA_13's preview, MOA_14, MOA_19 implicitly) frame each phase clearly

## Responsive + performance

- [ ] Mobile render pass at 320px — no overflow, type hierarchy clear, cards stack
- [ ] Tablet render pass at 768px
- [ ] Desktop render pass at 1440px
- [ ] Framework cards readable on mobile (not crushed)
- [ ] Module page load time < 2s on a module with Full body length (spot-check MOA_02 at ~60KB, MOA_08 at ~57KB)

## Regression check

- [ ] Home page unchanged from pre-integration snapshot (no accidental edits)
- [ ] Protocol lander unchanged from pre-integration snapshot (that's Session B's territory)
- [ ] Community lander unchanged from pre-integration snapshot
- [ ] Existing reviews sections unchanged (that's Session B's territory)
- [ ] Existing imagery unchanged (that's Session B's territory)
- [ ] No console errors on any module page
- [ ] No broken links across the 20 modules + phase cards + index page

## Sign-off

- [ ] All boxes above checked OR flagged with explanation
- [ ] Preview URL ready for Stefan + summary of changes doc prepared
- [ ] Pre-integration snapshot at `content/apollo/lovable/pre-integration-snapshot/` confirmed in place before pushing Session B
