# Lovable Session A v2 — Load 20 Apollo modules, verbatim

**Paste this into Lovable.** Driver: Anton, end-to-end. Execute in chunks if context fills. Stefan reviews once at the end of Session A + B combined.

---

## Context

You are loading 20 course modules onto Stef's Apollo (Men of Apollo) site. The content is Stef's own course notes, already extracted and cleaned. Your job is **to render each module's content verbatim** on its own page, with the metadata from the frontmatter driving the card / navigation / tier-gating.

**Do not edit the module content.** No rewriting. No summarising. No inserting visual "frameworks" callouts. No shortening. No expanding. No "improving" headings. No adding icons. No filler. If the source says "bs," the page says "bs."

The module body is rendered exactly as it appears in the markdown. Stef wants word-for-word.

---

## Source content

All 20 module markdown files live in the `stefan-studio` repo under `content/apollo/modules/`.

### Path A — fetch from GitHub raw URLs (preferred)

URL pattern:
`https://raw.githubusercontent.com/{OWNER}/stefan-studio/main/content/apollo/modules/module-{NN}-{slug}.md`

Module manifest:
```
module-01-welcome.md
module-02-apollo-initiation.md
module-03-mental-architecture.md
module-04-training-system.md
module-05-nutrition-framework.md
module-06-mobility-system.md
module-07-recovery-system.md
module-08-advanced-training.md
module-09-intermittent-fasting-mastery.md
module-10-nutrition-optimisation.md
module-11-recovery-stress-mastery.md
module-12-body-recomposition.md
module-13-phase-2-integration.md
module-14-phase-3-overview.md
module-15-advanced-physical-optimisation.md
module-16-gut-brain-axis.md
module-17-training-specialisation.md
module-18-sleep-circadian-mastery.md
module-19-longevity-optimisation.md
module-20-the-integrated-life.md
```

Also fetch `content/apollo/modules/index.md` for the program architecture (phase map + tier/dependency logic — reference only; do not render this page publicly).

### Path B — inline fallback

If URL fetch fails, Anton pastes each module file inline as fenced blocks in a follow-up message.

---

## Each module file has this shape

```
---
module_id: NN
slug: <slug>
title: <Module Title>
phase: onboarding | phase-1 | phase-2 | phase-3 | phase-4
order_in_phase: N
tier: shared | protocol | community
visibility: published | draft
dependencies: [slug, ...]
updated_at: YYYY-MM-DD
source_pdf: <filename>.pdf
lessons: N
lede: "opener quote for cards"
next_step: "transition text for footer CTA"
---

<Body — Stef's content, verbatim. Render exactly as-is.>
```

---

## What to build

### 1. Phase-gating IA (five phase cards)

| Card | Modules | Unlock day | Tier visibility |
|---|---|---|---|
| Onboarding | MOA_01 | Day 0, all members | shared |
| Phase 1 — Foundation | MOA_02–07 | Day 0 | protocol + community |
| Phase 2 — Integration | MOA_08–13 | Day 30 | community only |
| Phase 3 — Mastery | MOA_14–18 | Day 60 | community only |
| Phase 4 — Longevity | MOA_19–20 | Day 90 | community only |

Protocol-tier members see only Onboarding + Phase 1. Community-tier members see all five, with later phases time-locked.

### 2. Phase card component

- Phase name
- Unlock state: `Unlocked Day X` / `Unlocks Day X` / `Locked`
- List of modules (use frontmatter `title` + `lede` for the card teaser)
- Read-status indicator per module

### 3. Module page template

Each module page is simple — no editorial overlays:

**Header**
- `title` from frontmatter (as H1)
- Phase + module-number breadcrumb (e.g. "Phase 1 · Module 3")
- Optional: `lessons` count (e.g. "7 lessons") and reading time estimate
- `lede` as a hero subtitle (pulled from frontmatter, not from body)

**Body**
- Render the module markdown body **verbatim**. Preserve:
  - All text exactly as written
  - Paragraph breaks
  - Bulleted / numbered lists
  - Stef's section headings (they appear as plain lines — render them as H2/H3 based on position and length, but do not rewrite them)
  - Quoted lines prefixed with `>` — render as blockquotes
- Do NOT:
  - Add "Summary", "Key takeaways", "Frameworks" sections
  - Add icons, emoji, or decorative divider images
  - Reformat lists into cards
  - Shorten any passage
  - Change "recognise" to "recognize" or any other localisation
  - Reorder paragraphs

**Footer**
- `next_step` quote from frontmatter as a soft-CTA line
- Link to next module in sequence (by `phase` + `order_in_phase`)
- "Back to [phase name]" link

### 4. Nothing else

This session loads content. Do not:
- Touch the Protocol lander, Community lander, reviews, or imagery (those are Session B)
- Redesign the site shell
- Introduce new colours, typography, or component primitives
- Generate placeholder imagery to "illustrate" a module

---

## Chunked execution (if context budget tight)

Stop and confirm after each chunk:

**Pass A.0** — Scaffolding
- Phase card component + 5 phase cards wired (no module content yet)
- Module page template ready
- MOA_01 Welcome rendered end-to-end
- Members landing page with phase progress map
- Preview deploy. Anton verifies.

**Pass A.1** — Phase 1 Foundation (Protocol tier)
- MOA_02 through MOA_07 loaded

**Pass A.2** — Phase 2 Integration (Community tier)
- MOA_08 through MOA_13 loaded. Confirm Protocol members do not see this phase card.

**Pass A.3** — Phase 3 Mastery + Phase 4 Longevity (Community tier)
- MOA_14 through MOA_20 loaded. Confirm all 20 modules live.

---

## Output format (after each pass)

1. Summary of pages created (paths).
2. Spot-check: quote three paragraphs verbatim from one loaded module, pasted from the rendered page, to prove no rewrites happened.
3. Any frontmatter parsing errors.
4. Screenshots of phase-cards page + one sample module page (mobile + desktop).
5. Flags for anything you couldn't complete and why.

Do NOT deploy to production. Preview deploy only. Anton QAs against `qa-checklist-session-a.md` before Stefan handover.
