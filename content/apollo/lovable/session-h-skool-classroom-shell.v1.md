# Lovable Session H — Skool-Classroom Shell for Members → Modules

**Pass:** H.0
**Goal:** Replace the current dense vertical Modules list with a Skool-classroom-style card grid, and replace the single-column module detail page with a two-pane lesson-rail layout. All Apollo content stays verbatim. Brand tokens stay locked. This is a shell rebuild only — no new content authoring.

**Non-goals:** edit any module body content. Re-shape the Apollo Codex. Touch the public marketing site. Add per-lesson video, per-lesson comments, or split modules into separate lesson files. Replace the typographic cover system with stock photography.

---

## Reference pattern (Skool classroom)

Members already know this shape from the existing Men of Apollo Skool community. We are mirroring its rhythm in Lovable, dressed in Apollo's dark-mode tokens.

**Classroom (module index):** 3-column card grid. Each card = cover · title · 1–2 line tagline · progress bar. Locked cards stay visible, greyed, with an unlock condition shown ("Unlocks Day 30"). Phase headers above each row when grouping.

**Module detail:** two-pane layout. Left rail (~280px sticky) lists lessons with checkmarks (○ unchecked, ✓ complete). Right pane = title, sub-headline, body, resources, mark-complete top-right, footer prev/next. Mobile: rail collapses to drawer.

Public reference community (visual benchmark): https://www.skool.com/educate/classroom

---

## Locked decisions for Pass H.0

**D1 — Lesson rail = visual TOC over each module's H2 sections.** Do NOT split module markdown into separate lesson files. Each H2 inside a module's markdown body becomes one row in the lesson rail, anchor-linked to that section. The body content renders verbatim as a single document; the rail provides Skool-style navigation feel without re-cutting content.

**D2 — Typographic covers, no photography.** Each card cover is generated from tokens: large numeral (Source Serif 4 display, ~84px) + A-mark glyph + 2px ox-blood horizontal rule + phase-specific accent (subtle background tint per phase). No image assets. No stock photos.

**D3 — Defer lesson-level comments.** Each module page ends with a "Discuss this in Community →" CTA that deep-links to `/members/community?tag=module-{NN}`. Do not build a per-lesson comment thread component.

**D4 — Locked phases stay visible, greyed, with countdown.** Phase 2/3/4 cards render fully even when gated. Greyed cover, lock icon, "Unlocks Day {30|60|90}" badge. Clicking a locked card routes to a teaser state (the same module page, but body replaced with: "This module unlocks on Day {X}. Stay the course."). Phase header chip shows `Locked · Unlocks Day {X}` instead of a progress count.

---

## Data sources (read-only, do NOT edit)

The shell pulls from existing files in the repo. Treat all of these as immutable for Pass H.0.

| What | Path |
|---|---|
| Phase + module manifest (20 rows) | `content/apollo/modules/index.md` |
| Module body content (one MD per module) | `content/apollo/modules/module-01-welcome.md` … `module-20-the-integrated-life.md` |
| Codex → module wiring | `content/apollo/codex/index.yaml` |
| Codex entry bodies | `content/apollo/codex/entries/*.md` |
| Brand tokens (light) | `brand-kit/02-tokens/colors_and_type.css` |
| Brand tokens (dark, Members area) | `brand-kit/02-tokens/colors_and_type.dark.css` |
| Existing module-detail spec (extended, not replaced) | `content/apollo/lovable/session-a-module-load.v2.md` |
| Existing Codex surface spec (untouched, referenced) | `content/apollo/lovable/session-g-codex-build.md` |

For each module, the markdown frontmatter exposes: `slug`, `phase`, `lede`, `tier`, `next_step`, `dependencies`. Use `lede` for card taglines and module sub-headlines. Use `slug` for routing. Use `next_step` for footer nav.

---

## Surface 1 — `/members/modules` (the grid)

Replace the current vertical phase-list layout with phase-headed rows of cards.

### Layout structure

```
[ /members/modules — page header ]
   H1: Modules
   Sub: 20 modules · 4 phases · the full path

[ Phase 1 — Foundation ]                              0/6 complete
   Day 0–30 · All members
   ─────────────────────────────────────────────────
   [ Card M02 ]   [ Card M03 ]   [ Card M04 ]
   [ Card M05 ]   [ Card M06 ]   [ Card M07 ]

[ Phase 2 — Integration ]              Locked · Unlocks Day 30
   Day 30–60 · Community tier
   ─────────────────────────────────────────────────
   [ Card M08 (greyed) ] [ Card M09 (greyed) ] [ Card M10 (greyed) ]
   [ Card M11 (greyed) ] [ Card M12 (greyed) ] [ Card M13 (greyed) ]

[ Phase 3 — Mastery ]                  Locked · Unlocks Day 60
[ Phase 4 — Longevity ]                Locked · Unlocks Day 90

[ Onboarding ]                                        0/1 complete
   Shared · All members
   ─────────────────────────────────────────────────
   [ Card M01 ]
```

Order: render Phase 1 first (the working area), then Phase 2, 3, 4 in sequence, then Onboarding (M01) at the bottom as a "start here" anchor.

### Phase header anatomy

- **H2:** `Phase 1 — Foundation` · Source Serif 4, weight 600, --bone
- **Right-aligned chip:** `0/6 complete` (when phase unlocked) OR `Locked · Unlocks Day 30` (when gated). IBM Plex Mono caption, --stone background tint.
- **Subtitle:** `Day 0–30 · All members` (for Phase 1) / `Day 30–60 · Community tier` (Phase 2) / `Day 60–90 · Community tier` (Phase 3) / `Day 90+ · Community tier` (Phase 4) / `Shared · All members` (Onboarding). IBM Plex Sans, body sm, --stone.
- **Divider:** 1px --stone rule below the subtitle, 24px margin to the card row.

### Card anatomy (one card per module)

```
┌────────────────────────────────────────┐
│                                        │
│            02                          │  <-- numeral cover
│            ▲                           │  <-- A-mark
│            ──                          │  <-- ox-blood rule
│                                        │
├────────────────────────────────────────┤
│ PHASE 1 · MODULE 02                    │  <-- eyebrow
│ Apollo Initiation                      │  <-- title
│ The first 30 days of the forge.        │  <-- tagline (lede)
├────────────────────────────────────────┤
│ ▮▮▮░░░░░░░  30%   Protocol             │  <-- progress + tier
└────────────────────────────────────────┘
```

**Cover region (top, ~60% of card height):**
- Large numeral, Source Serif 4 display, ~84px, --bone, centered.
- A-mark glyph below numeral (24px, --stone).
- 2px horizontal rule below A-mark, 32px wide, centered, --ox-blood.
- Phase tint as subtle background (Phase 1 = neutral ink, Phase 2 = +2% --ox-blood, Phase 3 = +4% --ox-blood, Phase 4 = +6% --ox-blood, Onboarding = neutral ink). Tints are barely perceptible — phase-coding without being decorative.

**Eyebrow:**
- `Phase 1 · Module 02` — IBM Plex Mono, all caps, 11px, letter-spacing 0.08em, --stone.

**Title:**
- Module title from `index.md` row — Source Serif 4, weight 600, 22px, --bone. Display case (not all-caps).

**Tagline:**
- Module `lede` from frontmatter — IBM Plex Sans, regular, 14px, line-height 1.5, --stone. Truncate at 2 lines with ellipsis.

**Footer strip:**
- Progress bar — 4px tall, full card width, --stone background, --ox-blood fill from 0% to N%.
- Right side of strip (below bar): tier badge (`Protocol` or `Community`) in IBM Plex Mono caption, --stone. If locked, replace with lock icon + `Day X` text.

**Card states:**
- **Default:** background = --ink, border 1px --stone @ 12% opacity.
- **Hover:** translateY(-4px), border --ox-blood @ 60%, ox-blood 1px underline pulse on title (200ms ease).
- **Locked:** cover region opacity 40%, lock icon top-right of cover region, footer strip replaced with `Unlocks Day 30` chip. Hover still works. Click routes to teaser state.
- **Completed:** progress bar at 100%, small ✓ chip top-right of cover region, --bone color.

**Card click:** routes to `/members/modules/{slug}` (slug from frontmatter).

### Responsive behaviour

- Desktop ≥1024px: 3-column grid, 24px gap.
- Tablet 768–1023px: 2-column grid, 20px gap.
- Mobile <768px: 1-column grid, 16px gap. Cards keep full anatomy, just stack.
- Phase headers stay sticky-top within their phase scroll region on desktop only.

---

## Surface 2 — `/members/modules/{slug}` (the inside)

Replace the current single-column markdown page with a two-pane Skool-style layout.

### Layout structure

```
[ ← Back to Modules ]                          Phase 1 · Module 02
                                               ───────────────────
┌──────────────┬──────────────────────────────────────────────────┐
│              │                                 [✓ Mark complete] │  <-- top-right
│ LESSONS      │  Apollo Initiation                                │  <-- H1
│              │  The first 30 days of the forge.                  │  <-- sub
│ ○ Welcome    │                                                   │
│ ○ The Forge  │  ## Welcome to the Initiation                     │  <-- H2 anchors
│ ○ Day 1      │  [body content rendered verbatim from MD]        │
│ ✓ Day 7      │                                                   │
│ ○ ...        │  ## The Forge                                     │
│              │  ...                                              │
│              │                                                   │
│ APOLLO CODEX │  ─────                                            │
│ → CE-001     │  RESOURCES                                        │
│ → DD-001     │  → Codex CE-001 Cold Exposure & Sympathetic Mod.  │
│              │  → Codex DD-001 Knowing Is Not Doing              │
│              │                                                   │
│              │  Discuss this in Community →                      │
│              │                                                   │
│              │  ← Previous module    Next: Mental Architecture → │
└──────────────┴──────────────────────────────────────────────────┘
```

### Top bar

- Left: `← Back to Modules` link, IBM Plex Sans body, --stone, hover --bone. Routes to `/members/modules`.
- Right: eyebrow `Phase X · Module N`, IBM Plex Mono caption, all caps, --stone. Sticky on scroll for desktop.

### Lesson rail (left, 280px sticky)

- Sticky position, top-aligned to top bar bottom.
- Section header: `LESSONS` — IBM Plex Mono caption, all caps, letter-spacing 0.08em, --stone, 24px margin-bottom.
- Lesson list: one row per H2 found in the module's markdown body.
  - Title text taken from the H2 heading text.
  - Anchor link generated from kebab-cased H2 (e.g. `## The Forge` → `#the-forge`).
  - Status icon: ○ (empty circle, --stone) when unchecked, ✓ (filled, --bone on --ox-blood disc) when complete.
  - Current lesson (the H2 the viewport is currently scrolled to): bold + 2px --ox-blood left border, --bone text.
  - Click: smooth-scroll to anchor, no page reload.
  - Spacing: 12px vertical between rows, 16px left padding for icon + 12px gap to title.
- Below lesson list: 32px gap, then a second section.
- Section header: `APOLLO CODEX` — same style as `LESSONS`.
- Codex list: rows for each Codex entry where this module is in the entry's `serves_modules` field in `content/apollo/codex/index.yaml`.
  - Format: `→ {entry_id} {entry_title}` (e.g. `→ CE-001 Cold Exposure & Sympathetic Modulation`).
  - Hover: --bone text + ox-blood underline.
  - Click: routes to `/members/codex/{entry_id}` (existing route from Session G).

### Main pane (right)

- Width: fills remaining viewport minus rail + standard 32px page padding.
- Top-right: `Mark module complete` button.
  - Disabled state: greyed (--stone @ 40%), label `Complete all lessons to mark module`.
  - Active state (all H2-anchors checked): --ox-blood background, --bone text, label `✓ Mark module complete`. Click toggles module-level completion state.
- H1: module title from frontmatter (`title` in MD frontmatter, fall back to first `# H1` in file). Source Serif 4, weight 600, 48px, --bone.
- Sub-headline: module `lede` from frontmatter. IBM Plex Sans, regular, 20px, --stone, 16px margin-top from H1.
- Divider: 1px --stone @ 20% opacity, 32px margin above and below.
- Body: render the module markdown verbatim. NO content edits. NO summarisation.
  - H2 sections render with anchor IDs (kebab-cased from heading text).
  - At the end of each H2 section's content, append a small `[ ○ Mark complete ]` button. Click toggles the lesson-level checkmark in the rail. Once clicked, button shows `[ ✓ Complete ]` in --ox-blood.
- After the last H2's content + mark-complete button, render the footer block.

### Footer block (inside main pane)

- Divider: 1px --stone @ 20%, 48px margin above.
- **Resources** header: IBM Plex Mono caption all caps, --stone, 16px margin-bottom.
- Resources list: same Codex entries as the rail (deduplicated). Format: `→ {entry_id} {entry_title}`. Click routes to `/members/codex/{entry_id}`.
- 32px gap.
- **Discuss in Community** CTA: full-width row with right arrow chevron. Label: `Discuss this in Community →`. Click routes to `/members/community?tag=module-{NN}` where NN is the module's two-digit number.
- 48px gap.
- **Footer nav** row: split into two halves.
  - Left: `← Previous module` — title of previous module by manifest order. Routes to `/members/modules/{prev-slug}`. Hidden if current module is M01.
  - Right: `Next: {Module Title} →` — title of next module from `next_step` frontmatter field, or by manifest order. Routes to `/members/modules/{next-slug}`. Hidden if current module is M20.

### Mark-complete state (v1)

- Use browser localStorage keyed by `apollo:lesson:{module-slug}:{anchor-id}` for lesson-level checkmarks.
- Use `apollo:module:{module-slug}:complete` for module-level state.
- Roll up to phase-level by counting completed modules per phase: surfaces in the phase header chip on `/members/modules` (e.g. `2/6 complete`).
- H.1 will migrate to Supabase. Keep state shape identical so migration is a swap of storage adapter, not a re-design.

### Responsive behaviour

- Desktop ≥1024px: two-pane as drawn, rail 280px, content fluid.
- Tablet 768–1023px: rail collapses to top of page as a horizontal-scroll lesson chip strip. APOLLO CODEX section moves to a separate collapsed `<details>` block below the chip strip.
- Mobile <768px: rail becomes a drawer toggled by a button labelled `Lessons (4/12)`. Drawer slides in from left, full-height, dismissible by tap outside or Esc.
- Mark-complete buttons remain tappable at all widths.
- Footer nav stacks vertically on mobile.

### Locked-module teaser state

If a module is in a phase that hasn't unlocked yet (Phase 2 before Day 30, Phase 3 before Day 60, Phase 4 before Day 90), the page renders the same shell with one substitution: the body region (between sub-headline and footer) is replaced with a single block:

```
[ lock icon, 32px, --stone ]

This module unlocks on Day {X}.
Stay the course.

[ ← Back to Modules ]
```

Lesson rail is hidden (no anchors to scroll to). Codex section in rail still renders if there are entries wired to the module — gives members a preview of what's ahead. Top-right mark-complete button is hidden.

---

## Brand and voice rules (locked)

**Tokens:** consume only from `brand-kit/02-tokens/colors_and_type.dark.css` for Members area. NO hex literals in components. The four roles:
- `--ink` — page ground in dark mode (deepest)
- `--bone` — primary text on dark
- `--ox-blood` — single accent (one role per state, do not multiply)
- `--stone` — secondary structure (borders, dividers, subdued text)

**Type:**
- Source Serif 4 (variable, self-hosted): all H1, H2, H3, card titles, large numerals on covers.
- IBM Plex Sans (Google): body text, taglines, button labels, CTAs.
- IBM Plex Mono (Google): eyebrows, captions, badges, code-like content.
- Type scale: 1.250 major third, base 16px. Hero 72px. H1 48px. H2 32px. H3 22px. Body 16px. Body sm 14px. Caption 11–13px.

**Voice (preserve, do not introduce):**
- Module body content is rendered verbatim from markdown. Do NOT rewrite, summarise, or "improve" any sentence.
- Do NOT introduce em-dashes (`—`) anywhere in chrome strings (eyebrows, button labels, CTAs, footer text, badges). Use commas, colons, semicolons, periods. Em-dashes that appear in module body content stay as-is.
- Refused vocabulary list lives in `brand-kit/01-foundation/foundation-brief.md` §6. Chrome copy must not introduce any of those words. If unsure, use plain English.
- Stefan's UK English spelling is preserved in body content (e.g. "optimise", "behaviours"). Do not Americanise.

**Iconography:**
- Stroke icons only, 1.5px stroke, --stone default, --bone on hover.
- Icon set: lucide-react.
- Lock icon: `lucide:lock`. Check icon: `lucide:check`. Arrow icons: `lucide:arrow-left` / `lucide:arrow-right`. Chevron: `lucide:chevron-right`.

---

## Out of scope for Pass H.0

- Per-lesson video uploads. No video assets exist.
- Per-lesson comment threads. Discussion lives in `/members/community`.
- Splitting modules into separate lesson markdown files. Lesson rail is a TOC over H2s.
- Real-photography card covers. Typographic only for v1.
- Supabase persistence of mark-complete state. Use localStorage; H.1 migrates.
- Apollo Agent deep-link from inside lessons. Already partially wired in Session G; do not change.
- Sidebar nav, top-level routes, /members/codex, /members/community, /members/agent — leave untouched.

---

## Acceptance (what "done" means for H.0)

A signed-off Pass H.0 means all of:

1. `/members/modules` renders the 3-column phase-grouped card grid as specified, with all 20 modules in their correct phases and Phase 2/3/4 visibly locked with countdown chips.
2. Clicking any unlocked card lands on the two-pane module detail page with a working lesson rail and verbatim body content.
3. Mark-complete state persists across page reloads via localStorage, and rolls up to phase-level progress chips on the modules grid.
4. Codex entries appear in both the rail and the resources block on every module page where the Codex YAML wiring specifies the module in `serves_modules`.
5. All tokens sourced from CSS variables (no hex literals). Source Serif 4 + IBM Plex Sans + IBM Plex Mono used as specified.
6. Mobile experience works: card grid stacks, rail becomes a drawer, mark-complete buttons remain tappable.
7. No module body content has been edited. Voice and UK English preserved.

After Lovable runs the brief, Anton smoke-tests against `content/apollo/lovable/qa-checklist-session-h.md` and logs failures for Pass H.1 if any surface.
