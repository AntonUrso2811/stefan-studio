# Session A v2 QA Checklist — 20-module verbatim load

Internal gate. Anton ticks every box BEFORE Stefan handover. Any unchecked box = fix or document as flagged.

## Verbatim-render check (most important — Stefan's primary intent)

Spot-check three modules (different phases — recommend MOA_01, MOA_10, MOA_20). For each:
- [ ] Copy any paragraph from the rendered page
- [ ] Compare to `content/apollo/modules/module-NN-*.md` body
- [ ] **Zero differences** — no rephrased sentences, no added words, no removed words, no localisation changes, no heading rewrites, no bullet restructuring
- [ ] "recognise" / "optimise" / "behaviour" / "prioritise" — British spellings intact
- [ ] "Men of Apollo" terminology intact
- [ ] Stef's "- Stef" sign-offs intact where present

If any spot-check fails: Lovable rewrote content. Re-run the module load with a sharper prompt before Stefan handover.

## Coverage

- [ ] 20 module pages live (preview URL walkthrough)
- [ ] MOA_01 Welcome — Onboarding card, shared tier
- [ ] MOA_02–07 — Phase 1 Foundation card, protocol + community visible
- [ ] MOA_08–13 — Phase 2 Integration card, community only
- [ ] MOA_14–18 — Phase 3 Mastery card, community only
- [ ] MOA_19–20 — Phase 4 Longevity card, community only
- [ ] Program index page (if exposed publicly) matches `content/apollo/modules/index.md`

## IA + tier gating

- [ ] Phase cards render in order: Onboarding · Phase 1 · Phase 2 · Phase 3 · Phase 4
- [ ] Phase 2 locked for accounts under Day 30; Phase 3 under Day 60; Phase 4 under Day 90
- [ ] Lock state shows "Unlocks Day X" not just "Locked"
- [ ] Admin-unlock works on a test account
- [ ] Revisit-anytime works — can return to a completed module
- [ ] Protocol-tier test account sees ONLY Onboarding + Phase 1 cards
- [ ] Community-tier test account sees all five phase cards
- [ ] Shared tier (MOA_01) visible to both test accounts

## Module page rendering

- [ ] `title` from frontmatter renders as H1 (not part of body)
- [ ] `lede` from frontmatter renders as hero subtitle (pulled from frontmatter, not re-derived from body)
- [ ] Body rendered as long-form content — paragraphs, bullets, numbered lists preserved
- [ ] Blockquote lines (prefixed with `>`) render as quotes
- [ ] Section headings in body (short title-ish lines) render as H2/H3 based on position — no rewrites
- [ ] `next_step` from frontmatter renders as footer CTA line
- [ ] "Next module" link points to the next module in sequence (by phase + order_in_phase)
- [ ] "Back to phase" link works

## No editorial additions

- [ ] NO "Summary" or "Key takeaways" section inserted by Lovable
- [ ] NO "Frameworks" visual cards inserted
- [ ] NO icons / emoji / decorative images added by the model
- [ ] NO "In this module you'll learn..." intro Lovable wrote on its own
- [ ] NO content rewritten as bullets when source was paragraphs, or vice versa

## Cross-references

- [ ] References to "Phase 1" / "Phase 2" etc. in prose are consistent with phase-card IA
- [ ] References to other modules ("Module 1", "see the Nutrition module") are not broken or mis-linked — if Lovable autolinks, check a sample; if not, leave as plain text
- [ ] Phase 4 modules (MOA_19–20) reference "Phase 4" and "ninety-plus days" intact

## Responsive + performance

- [ ] Mobile render pass at 320px — no overflow, type hierarchy clear, cards stack
- [ ] Tablet render pass at 768px
- [ ] Desktop render pass at 1440px
- [ ] Module page load time < 2s on the largest module (MOA_02 at ~61KB, MOA_08 at ~58KB)
- [ ] Long modules don't crash the renderer (MOA_02 Apollo Initiation — spot check)

## Regression check (Session B territory still untouched)

- [ ] Home page unchanged from pre-integration snapshot
- [ ] Protocol lander unchanged
- [ ] Community lander unchanged
- [ ] Existing reviews sections unchanged
- [ ] Existing imagery unchanged
- [ ] No console errors on any module page
- [ ] No broken links across the 20 modules + phase cards

## Sign-off

- [ ] All boxes above checked OR flagged with explanation
- [ ] Preview URL ready for Stefan + summary of changes doc
- [ ] Pre-integration snapshot at `content/apollo/lovable/pre-integration-snapshot/` confirmed in place before Session B
