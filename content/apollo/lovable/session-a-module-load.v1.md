# Lovable Session A — Load 20 Apollo modules into phased-unlock library

**Paste this into Lovable as the single-session prompt.** Driver: Anton, end-to-end. Execute in chunks if context fills. Stefan reviews at the end of Session A + B combined — do not ping between chunks.

---

## Context

You are building out the course content on Stef's Apollo (Men of Apollo) site. 20 module pages, organised into four phases with a shared Onboarding entry. Members unlock phases at Day 0 / 30 / 60 / 90. Revisit-anytime once unlocked.

**Voice rule.** The module markdown is Stef's own words, verbatim from his course notes. Do NOT rewrite any body content. You may format, add in-page navigation, render frameworks as visual cards — but do not edit prose, add filler, or change phrasing.

**Design rule.** Match the existing site's tokens, type, and component system exactly. No new colours, no new component primitives. If something can be built with an existing component, use it. New layouts only where existing patterns genuinely do not fit.

**Scope.** This session is about loading the 20 modules + the phase-gating IA. Copy edits to existing lander pages + reviews + imagery are handled in Session B — do not touch them here.

---

## Source content

All 20 module markdown files live in the `stefan-studio` repo under `content/apollo/modules/`. Two delivery paths:

### Path A — fetch from GitHub raw URLs (preferred)

URL pattern:
`https://raw.githubusercontent.com/{OWNER}/stefan-studio/main/content/apollo/modules/module-{NN}-{slug}.md`

Manifest:
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

Also fetch `content/apollo/modules/index.md` for the program architecture.

### Path B — inline fallback

If URL fetch is unreliable in your context, I'll paste module files as fenced code blocks in a follow-up message. Tell me which you prefer BEFORE you start executing.

---

## Schema

Every module file starts with YAML frontmatter:
```yaml
---
module_id: NN
slug: <slug>
title: <Title>
phase: onboarding | phase-1 | phase-2 | phase-3 | phase-4
order_in_phase: N
tier: shared | protocol | community
visibility: published | draft
dependencies: [slug, ...]
updated_at: YYYY-MM-DD
source_pdf: <filename>.pdf
lessons: N
lede: "opener quote"
next_step: "transition text"
---
```

Then these sections in order:
1. `## Summary` — 2-3 sentence hook
2. `## Content map` — bullet list of lessons/sections
3. `## Frameworks / protocols` — named systems with detail for reproducible visual cards
4. `## Visual callouts` — diagrams/tables/scorecards to reproduce visually
5. `## Full body` — Stef's full prose, verbatim

---

## What to build

### 1. Information architecture (phased-unlock library)

- **Members landing page** — hero, "Start Here" CTA to MOA_01, phase progress map
- **Phase card component** — phase name, unlock state (Locked / Unlocks Day X / Unlocked Day X), list of modules with read-status indicator
- **Module page template** — renders the frontmatter fields + sections with in-page nav

### 2. Phase cards (create 5)

| Card | Modules | Unlock | Tier visibility |
|---|---|---|---|
| Onboarding | MOA_01 | Day 0, all tiers | shared |
| Phase 1 — Foundation | MOA_02–07 | Day 0 | protocol + community |
| Phase 2 — Integration | MOA_08–13 | Day 30 | community only |
| Phase 3 — Mastery | MOA_14–18 | Day 60 | community only |
| Phase 4 — Longevity | MOA_19–20 | Day 90 | community only |

Protocol-tier members see only Onboarding + Phase 1 cards. Community-tier members see all five, with Phase 2/3/4 locked until their respective day thresholds.

### 3. Module page template

For each module, render:

**Header band**
- Phase + Module number + title
- `lede` as hero quote
- Lesson count + reading time estimate

**Body**
- `Summary` — rendered as intro paragraph
- `Content map` — rendered as a table of contents with in-page anchor links to sections inside Full body
- `Frameworks / protocols` — each named framework becomes a reproducible visual card (not just text). Match existing site's card component. Protocols with numbered steps → numbered list inside card. Protocols with tiers/levels → tiered layout.
- `Visual callouts` — each callout becomes its own visual component: diagram, scoring visual, decision tree, checklist, table, etc. Use the best-matching existing component; new component only if none fits.
- `Full body` — full prose rendered as long-form content with heading hierarchy preserved

**Footer**
- `next_step` as CTA
- Link to next module in sequence (by order_in_phase + phase)
- "Back to phase" link

### 4. Navigation

- Global nav — Home / Protocol / Community / About / Login
- Members nav (post-login) — Dashboard / Phases / Calls / Community / Profile
- Phase cards visible on the Phases page; module pages accessible from their phase card

---

## Chunked execution (if context budget tight)

Execute in 4 passes. Stop and confirm before the next:

**Pass A.0** — Scaffolding + Onboarding
- Phase card component + 5 phase cards rendered (empty of modules for Phases 1-4 yet)
- Module page template
- MOA_01 Welcome rendered end-to-end
- Members landing with phase progress map
- Deploy to preview. Verify.

**Pass A.1** — Phase 1 Foundation (Protocol tier)
- MOA_02 Apollo Initiation
- MOA_03 Mental Architecture
- MOA_04 Training System
- MOA_05 Nutrition Framework
- MOA_06 Mobility System
- MOA_07 Recovery System
- Verify phase-card lists, in-page nav, framework visuals.

**Pass A.2** — Phase 2 Integration (Community tier)
- MOA_08 through MOA_13
- Verify community-tier gating; Protocol members should not see Phase 2 card.

**Pass A.3** — Phase 3 Mastery + Phase 4 Longevity
- MOA_14 through MOA_20
- Verify all 20 modules live; full site walkthrough.

---

## Output format (after each pass)

Respond with:
1. Summary of pages created or updated (paths).
2. Any content issues — missing frameworks, ambiguous visual callouts, malformed frontmatter.
3. Screenshots of the phase cards page + one sample module page (mobile + desktop).
4. Flags for anything you could not complete + why.

Do NOT deploy to production. Preview deploy only. Anton QAs against `qa-checklist-session-a.md` before Stefan handover.
