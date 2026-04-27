# Lovable Session G — Build the Apollo Atlas

**Paste this into Lovable.** Driver: Anton, end-to-end. Stefan reviews after Pass G.0 lands. Builds on Sessions A through F.

---

## Context

You are adding **The Apollo Atlas** to the Members area: a scientific interlink layer that cross-references every Apollo protocol, module, and framework piece to its underlying research and to modern-day scientists members already know (Huberman, Attia, San Millán, Søberg).

The Atlas is a structured, citation-grade content surface, presented in the dark dashboard chrome that already exists for Members. It pulls Apollo's voice (locked in `brand-kit/00-research/dossier-2026-04-25.md`) into research-grade format without crossing into academic register. Every entry is a reusable component reading content from versioned markdown files.

**Stefan-decision context:**
- Phase 1 ships **24 seed entries** across all 20 modules (full launch, all four Index tabs populated).
- Two sibling schemas: **PRE (Prompt → Response → Execution)** for 18 stimulus-based entries, **DDD (Doctrine → Default → Drift Check)** for 6 identity/system entries.
- Atlas is **not** a sidebar slot. Three discovery surfaces: Research sidecar embedded in module pages (primary), ⌘K global lookup (secondary), Modules / References tab toggle (tertiary). Deep-link URL `/members/atlas` and `/members/atlas/[slug]` preserved.

---

## Source content

All Atlas content lives in this repo:

```
content/apollo/atlas/
├── README.md                    # editorial guidelines + voice rules
├── index.yaml                   # master manifest
├── entries/
│   ├── ce-001 through ce-018    # 18 PRE entries
│   └── dd-001 through dd-006    # 6 DDD entries
├── scientists/
│   ├── andrew-huberman.md
│   ├── peter-attia.md
│   ├── inigo-san-millan.md
│   └── susanna-soberg.md
└── doctrine/
    └── d-01 through d-06        # 6 doctrine cards from Founder Dossier
```

Plus a dark-token CSS map: `brand-kit/02-tokens/colors_and_type.dark.css`.

Plus copy bank §11.5 Research voice: `brand-kit/01-docs/component-copy-bank.md` (added 2026-04-27).

### Path A — fetch from GitHub raw URLs (preferred)

URL pattern (same as Session A v2):
```
https://raw.githubusercontent.com/{OWNER}/stefan-studio/main/content/apollo/atlas/index.yaml
https://raw.githubusercontent.com/{OWNER}/stefan-studio/main/content/apollo/atlas/entries/{file}.md
https://raw.githubusercontent.com/{OWNER}/stefan-studio/main/content/apollo/atlas/scientists/{file}.md
https://raw.githubusercontent.com/{OWNER}/stefan-studio/main/content/apollo/atlas/doctrine/{file}.md
https://raw.githubusercontent.com/{OWNER}/stefan-studio/main/brand-kit/02-tokens/colors_and_type.dark.css
```

`index.yaml` is the manifest. Parse it first. Every entry, scientist, and doctrine has its own MD file referenced by path inside the manifest.

### Path B — inline fallback

If URL fetch fails, Anton pastes the manifest plus each MD file inline as fenced blocks in a follow-up message.

---

## Each entry file has this shape

PRE entry (`ce-NNN-*.md`):

```yaml
---
entry_id: ce-001
slug: cold-exposure-sympathetic
title: "Cold Exposure and Sympathetic Modulation"
schema: pre
phase_relevance: [phase-1, phase-2, phase-3]
five_inputs: [calm-nervous-system, sleep]
mechanism_tags: [cold-exposure, sympathetic-tone, brown-adipose, vagal-tone]
modules: [M07, M11, M18]
scientists: [andrew-huberman, susanna-soberg]
doctrine_refs: [d-02-effortless-not-extreme]
evidence_level: 3
plain_english: "..."
technical: "..."
prompt: "..."
response: "..."
execution: "..."
studies:
  - authors: "..."
    year: 2021
    title: "..."
    venue: "..."
    doi: "..."
    url: "..."
updated_at: 2026-04-27
---

## The Stance
(Body markdown — render verbatim. Do NOT rewrite.)

## Plain English
...

## Technical
...

## The Studies
...

## Linked Modules
...

## Doctrine bridge
...

## Apollo Agent — deep prompt
...
```

DDD entry (`dd-NNN-*.md`) has the same frontmatter pattern with `schema: ddd`, plus `doctrine`, `default_state`, `drift_check`, `review_cadence` fields, and body sections "The Doctrine / Why this doctrine matters / The Default / The Drift Check / Cadence / Voice notes".

Render bodies **verbatim**. Same lock as Session A. No rewriting. No improvements.

---

## What to build

### 1. Dark theme activation on Members area

Members area runs `[data-theme="dark"]` on the root container (or `<html>`). Import `colors_and_type.dark.css` after `colors_and_type.css`. The dark map preserves the cream tokens for the public site while inverting ground for any element that opts in.

The Atlas always renders dark, regardless of parent theme. The `.atlas` selector in the dark CSS file forces it.

### 2. Atlas Index page (route: `/members/atlas`)

Layout:

- **Hero (top):** H1 *"The Apollo Atlas"*. Sub: *"The scientific interlink layer for every Apollo protocol. Studies, scientists, and the locked doctrines that hold the system together."*
- **Tabs (sticky):** four tabs, default *"By Module"*. Tabs verbatim:
  - `By Module`
  - `By Scientist`
  - `By Mechanism`
  - `By Founder Doctrine`

#### Tab 1 — By Module
Render 20 module cards in a 4×5 grid (desktop), 2-col tablet, 1-col mobile. Each card shows:
- Module ID + title (e.g. *"M07 Apollo Recovery System"*)
- Phase chip (Onboarding / Phase 1 / etc.)
- Count of linked entries (e.g. *"3 entries"*)
- Top scientist for that module (e.g. *"Andrew Huberman, Susanna Søberg"*)
- One-line lede pulled from `content/apollo/modules/module-NN-*.md`

Click → filtered entry list for that module.

#### Tab 2 — By Scientist
Render 4 scientist cards (Huberman / Attia / San Millán / Søberg). Each card:
- Name + role + lowercase institution
- Initials avatar (no headshot in Phase 1; headshot upload in Phase 4)
- Count of entries citing them
- Primary modules (chip list)

Click → scientist directory page (route `/members/atlas/scientists/[id]`).

#### Tab 3 — By Mechanism
Render the `mechanism_tags` from `index.yaml` as a tag cloud or filterable list. Show entry count per tag. Click → filtered entry list.

#### Tab 4 — By Founder Doctrine
Render 6 doctrine cards (one per `doctrine/d-NN-*.md`). Each card:
- Locked doctrine line (in serif, italic, large)
- One-line "Why this matters"
- Linked Atlas entries (chip list)
- Linked modules (chip list)

Click → doctrine card detail page (route `/members/atlas/doctrine/[id]`).

### 3. Atlas Entry page (route: `/members/atlas/[slug]`)

Render PRE and DDD entries from frontmatter. Single-column layout, max-width 68rem (`var(--content-max)`), 68ch reading measure (`var(--measure)`).

#### Top of page

- **Phase tag chip**, **Five Inputs badge(s)**, **Evidence-level dot meter** (right-aligned)
- **H1** title
- **Lead** (1.25rem serif italic): one sentence pull from `plain_english` or the entry's "The Stance" section
- **Mechanism tag chips** (small)

#### Body sections

For PRE entries, render in this order, using the Atlas section headers from copy bank §11.5:

1. The Stance
2. Doctrine card (pulls from first `doctrine_refs[0]` linked doctrine)
3. Plain English / Technical (two-column on desktop, stacked on mobile)
4. **PRE block** (three-column responsive): PROMPT / RESPONSE / EXECUTION columns, monospace caps labels, content from frontmatter
5. The Studies (paper-style numbered list, citation chips, DOI/URL link)
6. Modern voices (scientist chips that link to scientist directory pages)
7. Linked Modules (deep-links to module pages)
8. Doctrine bridge (one-sentence closer, italic serif)
9. Apollo Agent deep-prompt button (renders the verbatim prompt from the entry as a clickable button labelled *"Ask Apollo →"*)

For DDD entries, replace step 4 with a **DDD block** (DOCTRINE / DEFAULT / DRIFT CHECK columns) and replace section labels with the DDD-specific headers from copy bank §11.5.

**Bottom rail:** Previous entry / Next entry / Open Founder Dossier ↗ / Discuss in Community ↗

### 4. Scientist Directory page (route: `/members/atlas/scientists/[id]`)

Render scientist MD files. Layout:

- **Header:** name, role, institution (lowercase), initials avatar
- **Plain English** section (the framing paragraph)
- **What Apollo uses** section (bulleted list)
- **What Apollo does not echo** section (bulleted list)
- **Atlas entries citing this scientist** (entry cards in a 2-col grid)
- **Apollo modules informed by their work** (chip list)
- **Honest note** section (where present)
- External link to canonical resource (one link, no link farm)

### 5. Doctrine card detail (route: `/members/atlas/doctrine/[id]`)

Render doctrine MD files. Layout:

- **Locked line** at the top, large, serif italic, ox-blood-warm hairline
- **Source citation** (e.g. *"Founder Dossier §1, Instagram bio verbatim"*) in monospace caption
- **Why this doctrine matters** body
- **The Default** body
- **The Drift Check** body (with the question pulled out as a quote)
- **Voice notes** section
- **Linked Atlas entries** + **Linked modules** chip lists at the bottom

### 6. ⌘K global lookup (header)

Add a `⌘K Atlas` keyboard shortcut + clickable button in the Members header. Opens a modal with a search input. Three result groups:

- **Scientists** (search by name)
- **Mechanism tags** (search by tag)
- **Doctrine lines** (search by text)

Each result is a deep-link to the corresponding page.

### 7. Modules / References tab toggle on `/members/modules`

At the top of the Modules page (the existing 20-module library view), add a tab toggle:

```
[Modules]  [References]
```

`References` opens the Atlas Index inside the Modules page chrome (no full route change). Allows destination-mode browsing without burning a sidebar slot.

### 8. Research sidecar on every module page

This is the **primary discovery surface**. Embedded right column on desktop (≥1024px), drawer-collapsed on tablet, accordion-folded on mobile.

For each module page, query `index.yaml` for Atlas entries where `modules` includes the current module ID. Render up to 7 entries in a sidecar with header:

```
RESEARCH
Linked Atlas entries for this module.
```

Each entry: small card with title, scientist chip, evidence-level dots, click-through to full Atlas entry.

If a module has zero linked entries, hide the sidecar entirely (do not show empty state).

### 9. Apollo Agent deep-prompt deep-link

Every Atlas entry's "Ask Apollo →" button should pre-fill the Apollo Agent chat with the verbatim question from the entry frontmatter. URL pattern:

```
/members/apollo-agent?prefill={url-encoded question}
```

Apollo Agent reads the prefill query parameter and inserts it as the first message in the chat.

---

## Voice rails (apply to every UI string)

Pulled from `brand-kit/01-docs/foundation-brief.md` §5–§7 and `component-copy-bank.md` §11.5.

**Owned vocabulary** (use freely): protocol, blueprint, system, input, stack, framework, the five inputs.

**Refused vocabulary** (zero hits): alpha, sigma, grind, beast, savage, warrior, spartan, conquer, TRT, peptides, macros, motivation, hype, no excuses, brotherhood, tribe, transform, journey, unlock (verb), unleash, level up, game-changer.

**Punctuation bans:** no em dashes, no semicolons, no mid-sentence colons, no exclamation marks on primary CTAs.

**Citation register:**
- ✅ *"In ${journal} (${year}), ${authors} found that…"*
- ❌ *"Studies show…"* (banned)
- ❌ *"Experts say…"* (banned)

**Stance register:**
- ✅ *"Stefan's stance:"*
- ✅ *"What Apollo uses:"*
- ✅ *"What we don't echo:"*

---

## Chunked execution (if context budget tight)

Stop and confirm after each pass:

**Pass G.0** — Scaffolding
- Dark theme activation on Members
- Atlas Index page (route + 4 tabs, By Module tab populated only)
- Atlas Entry template (renders one MD entry, both schemas supported)
- One full Atlas entry rendered end-to-end (suggest: ce-001 Cold Exposure)
- Preview deploy. Anton verifies. Stefan reviews aesthetic.

**Pass G.1** — Content load (24 entries + 4 scientists + 6 doctrines)
- All 24 entries fetched and rendered
- All 4 scientist directory pages rendered
- All 6 doctrine detail pages rendered
- All 4 Atlas Index tabs populated

**Pass G.2** — Discovery surfaces
- ⌘K global lookup wired (header)
- Modules / References tab toggle on /members/modules
- Research sidecar on all 20 module pages

**Pass G.3** — Apollo Agent integration
- Deep-prompt buttons functional on every Atlas entry
- Apollo Agent reads `?prefill=` and inserts first message
- End-to-end test: click button on ce-001 → Apollo Agent opens with the cold-exposure question pre-loaded

---

## What NOT to do this session

- Do NOT add "Atlas" as a new sidebar slot. Members sidebar is locked. Discovery is via sidecar + ⌘K + tab toggle.
- Do NOT add Phase 4 features: scientist headshots, "Discuss in Community" deep-links, member analytics. Those are post-launch.
- Do NOT improve the Founder Dossier excerpts. Verbatim quotes only.
- Do NOT introduce new colours outside the dark token map. The map is intentionally minimal (one warm-shifted accent, two ink layers, two rule weights).
- Do NOT generate placeholder content or "lorem ipsum" entries. The 24 entries are real and complete; do not pad.
- Do NOT cite scientists or studies that are not in `index.yaml`. The current 4 scientists and the 18 entries' citation lists are exhaustive for Phase 1.

---

## Output format (after each pass)

1. Summary of pages and routes created.
2. Spot-check: render one Atlas entry end-to-end (suggest ce-001 or dd-001) and paste rendered HTML or screenshot.
3. Voice scan: confirm zero hits against the refused-vocabulary list. Confirm no em dashes in customer-facing copy.
4. Frontmatter parsing errors flagged.
5. Screenshots of: Atlas Index By Module tab, one Atlas Entry page (PRE), one Atlas Entry page (DDD), one Scientist Directory page, the Research sidecar embedded in a module page, the ⌘K modal.
6. Flags for anything you couldn't complete and why.

Do NOT deploy to production. Preview deploy only. Anton QAs against `qa-checklist-session-g.md` before Stefan handover.

---

## QA checklist (Anton fills out, Stefan signs off)

Same shape as Session A through F QA checklists. Will be authored as `qa-checklist-session-g.md` after Pass G.0 lands.

Pre-checklist Stefan questions (raise during Pass G.0):
1. Does the Atlas feel like Apollo, or like an academic library bolted on? (Aesthetic check.)
2. Is the dark accent (warm-shifted ox-blood) right, or should it shift further toward gold or cream? (Token check.)
3. Is the PRE three-column block legible on mobile when collapsed to vertical? (Layout check.)
4. Does the Research sidecar feel ambient or noisy when reading a module? (Discovery check.)
5. Is the ⌘K placement / shortcut conflict-free with the Apollo Agent and other Members shortcuts? (UX check.)

If any answer is *"not quite right"*, do not push G.1 to G.0 yet. Iterate the aesthetic first. Content is ready and stable.
