# Lovable Session H.1 — Inside-module surface, mirroring Skool's classroom

**Pass:** H.1 (follow-up to H.0; same `session-h-classroom-shell` branch / PR #8)
**Goal:** Replace H.0's "two-pane lesson rail with H2 anchors" inside-module surface with the **exact pattern members already know from Men of Apollo on Skool** — a left rail of distinct lesson pages, with collapsible WEEK-style groups where the markdown signals one. The grid surface from H.0 stays as-is.

**Non-goals:** edit any module body content. Re-shape Codex. Touch the public marketing site or /members/community. Add inline video, attachments UI, or per-lesson comments.

---

## Why v1's D1 was wrong

v1's D1 decision was "lesson rail = visual TOC over module H2s, no file split". That was specced before we had access to the Men of Apollo Skool classroom inside-module view. We've now walked through it (live, logged in, captured 27 Apr 2026):

**Skool's actual inside-module is:**
- A LEFT RAIL of distinct lesson rows (each is its own URL), not anchors over one page
- Some rows are top-level lessons; some are **collapsible group headers** with chevron indicators
- Each lesson click swaps the main pane content (URL changes, content swaps; rail group state preserved)
- Lesson page anatomy: title + circle "mark complete" icon top-right + body content (single column)
- No comments, no attachments UI, no prev/next nav at the bottom of the lesson body
- Mobile: rail stacks above content (assumed; not captured this pass)

So D1 must flip from "anchors over one page" to "distinct lesson pages with optional grouping". The implementation is still light, because the existing Apollo module markdown ALREADY encodes the structure.

---

## What we observed in the Men of Apollo Skool classroom

Reference URL (gated, login required): `https://www.skool.com/men-of-apollo-7705/classroom`

### Module landing → first lesson

When a member clicks a module card in the classroom, Skool routes them to `/classroom/{module-id}?md={first-lesson-id}` and renders:

**Left rail (~280px):**
```
THE APOLLO INITIATION                         <-- module title, all caps, eyebrow
[████████░░░░░░░░░░] 0%                       <-- progress bar

What the Next 30 Days Will Do to You         <-- top-level lesson row
30-Day Overview: What Success Looks Like     <-- top-level lesson row

INITIATION WEEK 1                          ⌄ <-- collapsed group, chevron down
INITIATION WEEK 2                          ⌄
INITIATION WEEK 3                          ⌄
INITIATION WEEK 4                          ⌃ <-- expanded group, chevron up
  WEEK 4: CONSISTENCY + IDENTITY             <-- sub-header inside group, NOT clickable
  Action 1: Review Your Apollo Scorecard     <-- lesson row inside group (active)
  Action 2: Identify Your Weak Links
  Action 3: Lock In Your Personal Training…  <-- truncated with ellipsis
  Action 4: Identity Shift
  Week 4 Summary and Checklist
  Phase 1 Completion: Preparing for Phase 2
```

**Active lesson:** highlighted with a soft cream/yellow background fill across the full rail row width. (For Apollo dark mode: use `--bone @ 8% opacity` over `--ink`, or a faint `--ox-blood @ 12%` tint — pick during preview.)

**Group expand/collapse:** clicking a group header toggles only that group's expansion. Does NOT change the active lesson. Other expanded groups stay expanded. State is local UI (no URL change).

**Rail rows truncate** at width with ellipsis. Hover does not reveal the full title — you have to click to see it (acceptable; we won't add tooltips for v1).

### Lesson page (right pane)

```
┌──────────────────────────────────────────────────┐
│ Action 1: Review Your Apollo Scorecard       ⊙   │  <-- title + mark-complete circle
│                                                  │
│ Pull out your Scorecards from Weeks 1, 2, and    │
│ 3. Look at them side by side.                    │
│                                                  │
│ What to look for:                                │  <-- bold inline section header
│                                                  │
│ Bodyweight and waist trends: Has your weight     │  <-- bold label + body para
│ changed? Has your waist measurement changed?…    │
│                                                  │
│ Training performance: Are you getting stronger?… │
│                                                  │
│ [more bold-label/body pairs]                     │
│                                                  │
│ What to do with this data:                       │
│                                                  │
│ Don't just look at it, act on it. Identify your  │
│ weakest pillar…                                  │
│                                                  │
│ Write down your top 1-2 weak links.              │
└──────────────────────────────────────────────────┘
```

**Anatomy:**
- Title: bold, ~20px, sentence case (matches the rail row title)
- Mark-complete affordance: empty circle (`⊙`) in the top-right of the title row. When ticked, fills with `--ox-blood` and a checkmark glyph.
- Body: single column, max ~720px. Plain paragraphs. **Bold inline labels** for sub-sections (no H2/H3 in lesson body — formatting is bold-paragraph not heading hierarchy).
- Some closing lessons end with a sign-off line: `— Stef`. Render verbatim from markdown.
- NO comments, NO attachments UI, NO prev/next CTA at bottom of body.

### URL pattern

- Classroom: `/classroom`
- Module: `/classroom/{module-slug-or-id}` (in Skool: opaque ID like `3d2ea192`; in Lovable: use the existing module slug, e.g. `apollo-initiation`)
- Lesson: `/classroom/{module}?md={lesson-id}` in Skool. In Lovable, use a sub-path or query — recommend sub-path: `/members/modules/{module-slug}/{lesson-slug}` for cleaner deep-linking.

---

## D1 (revised) — distinct lesson pages, with WEEK-prefix grouping

**Lock:** Each H2 in a module's markdown becomes a row in the rail. H2s starting with the literal token `WEEK ` (case-insensitive, optional colon after) become collapsible group headers. Their child H3s become individual lesson pages within the group. All other H2s are flat top-level lesson pages.

The convention is already encoded in the existing markdown — no content surgery needed. Examples confirmed by direct file inspection:

**M02 Apollo Initiation** (uses WEEK groups):
```
## What the Next 30 Days Will Do to You    → top-level lesson
## 30-Day Overview: What Success Looks Like → top-level lesson
## WEEK 1: RESET + RHYTHM                  → drop-down GROUP
  ### Action 1: Set a Fixed Wake Time        → lesson inside group
  ### Action 2: Morning Sunlight + Walking   → lesson
  ### Action 3: Remove Liquid Calories…      → lesson
  ### Action 4: Three Full-Body Training…    → lesson
  ### Action 5: 10-Minute Daily Mobility     → lesson
  ### Action 6: Digital Wind-Down Routine    → lesson
  ### Week 1: Summary and Checklist          → lesson
## WEEK 2: STRUCTURE + SYSTEMS             → drop-down GROUP
  [5 actions + summary]
## WEEK 3: STRENGTH + CONDITIONING BASE    → drop-down GROUP
  [4 actions + summary]
## WEEK 4: CONSISTENCY + IDENTITY          → drop-down GROUP
  [4 actions + summary]
## Phase 1 Completion: Preparing for Phase 2 → top-level lesson (closer)
```

**M03 Mental Architecture** (no WEEK groups):
```
## The Identity Shift                  → top-level lesson
  ### How to Build Discipline:           → renders as bold sub-section INSIDE the lesson body
## Discipline Over Motivation          → top-level lesson
  ### Protecting Consistency:            → bold sub-section
## The Consistency Compound            → top-level lesson
[etc]
```

**Renderer rule (one regex, one branch):**
```
foreach H2 in module.body:
  if H2.text matches /^WEEK\s+\d+/i:
    render as collapsible group; children H3s are lessons
  else:
    render as flat lesson; children H3s render as bold sub-headers WITHIN the lesson body
```

That's it. No frontmatter changes. No file splits. The 19 non-WEEK modules render as flat lesson lists. M02 (Apollo Initiation) renders with the four WEEK drop-downs.

---

## Surface spec — `/members/modules/{module-slug}` and child lesson routes

### Routing

- `/members/modules/{module-slug}` → routes to the FIRST lesson of that module (matches Skool: clicking a module card lands you on the first lesson, not a separate "module overview" page)
- `/members/modules/{module-slug}/{lesson-slug}` → renders that specific lesson with the rail showing the active state

`{lesson-slug}` is the kebab-cased H2 (or H3, for grouped lessons) text. Example: `/members/modules/apollo-initiation/action-1-set-a-fixed-wake-time`.

### Layout (desktop)

```
[ ← Back to Modules ]                                   THE APOLLO INITIATION
                                                        ────────────────────
┌─────────────────────────┬───────────────────────────────────────────────┐
│ THE APOLLO INITIATION   │                                            ⊙  │
│ [progress 0%]           │  Action 1: Review Your Apollo Scorecard       │
│                         │                                               │
│ What the Next 30 Days…  │  Pull out your Scorecards from Weeks 1, 2,    │
│ 30-Day Overview…        │  and 3. Look at them side by side.            │
│                         │                                               │
│ INITIATION WEEK 1     ⌃ │  What to look for:                            │
│   WEEK 1: RESET + RHY…  │                                               │
│   Action 1: Set Fixed…  │  Bodyweight and waist trends: Has your        │
│   Action 2: Morning…    │  weight changed? …                            │
│   ...                   │                                               │
│   Week 1 Summary…       │  [body continues, single column]              │
│                         │                                               │
│ INITIATION WEEK 2     ⌄ │                                               │
│ INITIATION WEEK 3     ⌄ │                                               │
│ INITIATION WEEK 4     ⌄ │                                               │
│                         │                                               │
│ Phase 1 Completion…     │                                               │
│                         │                                               │
│ APOLLO CODEX            │                                               │
│ → CE-001                │                                               │
│ → DD-001                │                                               │
└─────────────────────────┴───────────────────────────────────────────────┘
```

### Top bar

- Left: `← Back to Modules` (routes to `/members/modules`).
- Right: module title in `--stone`, IBM Plex Mono caption, all caps, sticky on scroll.

### Left rail (sticky, 280px)

**Header block** (fixed at top of rail):
- Module title: Source Serif 4, weight 600, 18px, `--bone`. All caps.
- Progress bar: 4px tall, full rail width, `--stone @ 20%` background, `--ox-blood` fill.
- 24px gap below the bar.

**Lesson list** (scrollable below header):

Renders by walking the module markdown's H2s in order:

1. **Top-level lesson** (H2 not matching WEEK regex): single row.
   - Padding: 12px 16px
   - Text: lesson title (the H2 heading), IBM Plex Sans, 14px, `--stone`. Truncate at width with ellipsis.
   - State: hover → `--bone`. Active → background `--ox-blood @ 12%`, text `--bone`, 2px `--ox-blood` left border.

2. **Group header** (H2 matching `^WEEK\s+\d+/i`): collapsible row.
   - Padding: 12px 16px
   - Text: full H2 text (e.g. `INITIATION WEEK 1` — render verbatim from markdown which uses `WEEK 1: RESET + RHYTHM` naming, but keep what the file says). IBM Plex Sans, 14px, weight 600, `--bone`. All caps.
   - Right side: chevron icon (`lucide:chevron-down` collapsed, `lucide:chevron-up` expanded), `--stone`.
   - Click toggles only this group's expansion. Persist state to localStorage so refresh keeps the user's open groups.
   - When expanded, render group children below with 16px left indent (relative to group header padding):
     - **Optional sub-header**: render the H2 text WITHOUT the "WEEK X" prefix as a small all-caps caption above the lesson list — e.g. for `## WEEK 1: RESET + RHYTHM`, render `WEEK 1: RESET + RHYTHM` itself as a tiny IBM Plex Mono caption (10px, `--stone`, letter-spacing 0.08em) above the H3 list. Skool shows this same pattern (the sub-header `WEEK 1: RESET + RHYTHM` appears above the actions when the group is expanded).
     - **Lesson rows** (H3s under this H2): same anatomy as top-level lesson rows, just indented.

After all H2s, render the **APOLLO CODEX** block (already specced in v1):
- 32px gap, then caption `APOLLO CODEX` in IBM Plex Mono.
- One row per Codex entry where this module is in the entry's `serves_modules` field of `content/apollo/codex/index.yaml`.
- Format: `→ {entry_id} {entry_title}`. Click → `/members/codex/{entry_id}`.

### Main pane (right)

- Top-right: empty circle (`lucide:circle`) for "mark complete". Tap toggles state. When complete: `lucide:check-circle-2` filled with `--ox-blood`, `--bone` glyph.
- Title (H1 of the page): the lesson's heading text — for top-level lessons this is the H2; for grouped lessons this is the H3. Source Serif 4, weight 600, 28px, `--bone`. Sentence case (preserve casing from markdown).
- 24px gap.
- Body: render the section of markdown body that BELONGS to this lesson. Specifically:
  - For a top-level lesson (H2): body = everything between this H2 and the next H2 (exclusive). Render markdown verbatim — paragraphs, bold inline labels, bullet lists, blockquotes, all preserved.
  - For a grouped lesson (H3 inside a WEEK H2): body = everything between this H3 and the next H3 (or the next H2). Render verbatim.
  - Inside the body, H3s (for top-level lessons) and H4s (for grouped lessons, if any) render as bold sub-headers inline (like Skool's "What to look for:" pattern), NOT as separate rail items.
- 48px gap, then the bottom anchor.

### Bottom of main pane (kept from v1)

- 1px `--stone @ 20%` divider
- **RESOURCES** header (IBM Plex Mono caption, all caps, `--stone`)
- Codex entries wired to this module (deduped against the rail Codex section): `→ {entry_id} {entry_title}` rows
- 32px gap
- `Discuss this in Community →` row, full-width, deep-links to `/members/community?tag=module-{NN}` where NN is the module's two-digit number
- 48px gap
- Footer nav: `← Previous lesson` / `Next lesson →` based on the rail's flat order (treat the rail as a linear list when computing prev/next, including walking into expanded groups). Only `Next lesson →` shows on the first lesson of M01; only `← Previous lesson` shows on the last lesson of M20.

### Mark-complete state (v1, localStorage)

- Lesson level: key `apollo:lesson:{module-slug}:{lesson-slug}` → `true | false`
- Rail visual: ticked lessons show a small `lucide:check-circle-2` glyph in `--ox-blood` to the LEFT of the lesson title (16×16, 8px gap to title)
- Module-level progress: percentage = (lessons-marked-complete / total-lessons) × 100. Drives the rail header progress bar AND the card progress bar on `/members/modules`.
- H.2 will migrate this to Supabase. Keep key shape stable.

### Responsive (mobile <768px)

- Rail collapses to a top-anchored button: `Lessons (3/12)` (count of complete / total).
- Tapping opens a full-height drawer from the left containing the rail.
- Selecting a lesson dismisses the drawer.
- Main pane fills viewport width (with standard 16px page padding).
- Mark-complete circle stays top-right of the lesson title.

---

## D2, D3, D4 (unchanged from v1)

- **D2 — Typographic covers:** unchanged. (Already shipped from H.0; cards in the live Lovable preview now show the module title centered with A-mark and ox-blood rule.)
- **D3 — Defer per-lesson comments:** unchanged. Footer "Discuss in Community →" still routes to `/members/community?tag=module-NN`.
- **D4 — Locked phases visible with countdown:** unchanged. (The locked teaser body in v1 still applies — when the whole module is gated, the lesson rail is hidden and the body is replaced with the unlock countdown.)

---

## Brand and voice (locked, same as v1)

- Tokens from `brand-kit/02-tokens/colors_and_type.dark.css`. No hex literals.
- Source Serif 4 on H1/title; IBM Plex Sans on rail rows and body; IBM Plex Mono on eyebrows/caption/badges.
- Markdown body content rendered verbatim. No em-dashes introduced into chrome strings. UK English preserved in body.
- Sign-off lines like `— Stef` (em-dash + name) appear in some modules' body content. Render verbatim. Do not rewrite.

---

## Acceptance for Pass H.1

Smoke-test against the updated `qa-checklist-session-h.md`. Specifically:

1. `/members/modules/apollo-initiation` lands on the first lesson (`What the Next 30 Days Will Do to You`) by default.
2. Rail shows two top-level lessons, then four `INITIATION WEEK X` collapsible groups, then `Phase 1 Completion: Preparing for Phase 2` as a closer top-level lesson, then APOLLO CODEX section.
3. Clicking a WEEK group toggles only that group's expansion. Other groups stay as they were.
4. Inside an expanded WEEK group, the first row is the WEEK sub-header (small caption), then the action lessons.
5. Clicking a lesson swaps the main pane content. URL updates to `/members/modules/apollo-initiation/{lesson-slug}`. Rail active state moves.
6. Lesson body renders verbatim from the markdown source. Open `module-02-apollo-initiation.md` and side-by-side compare three lessons: an Action, the 30-Day Overview (which has H3 sub-sections like "Physical Changes"), and the Phase 1 Completion closer.
7. M03 (Mental Architecture) renders with NO drop-down groups — flat list of H2 lessons. Inside each lesson, H3s render as bold sub-headers inline, not as separate rail items.
8. M07 (Recovery System) renders flat. Same pattern as M03.
9. Mark-complete circle works at lesson level. Toggling it updates the rail glyph and the module progress bar in the rail header. Reload preserves state. Returning to `/members/modules` shows the card progress bar updated.
10. `Discuss this in Community →` deep-links correctly with the right module-NN tag.
11. Mobile: rail becomes a `Lessons (X/Y)` drawer.
12. The H.0 grid surface (`/members/modules`) is unchanged.

---

## Out of scope for H.1

- Per-lesson video uploads (no assets exist; Skool's lessons we observed were text-only)
- Per-lesson comments (D3, defer)
- Re-authoring lessons that exist on Skool but not yet in the markdown — Apollo Initiation has 33 lessons on Skool but the markdown captures all of them already; spot-check confirmed M02's H2/H3 layout matches Skool exactly. Any drift is a content task, not a shell task.
- Supabase persistence (H.2)
- Apollo Agent integration changes
- Cards on `/members/modules` (already shipped in H.0; do not touch)

---

## Reference (live Skool URLs)

The following URLs require an authenticated Men of Apollo membership. Anton can validate the brief side-by-side by clicking through:

- Classroom index: `https://www.skool.com/men-of-apollo-7705/classroom`
- Apollo Initiation module (lands on first lesson): `https://www.skool.com/men-of-apollo-7705/classroom/3d2ea192`
- Specific lesson example (Action 1 in Week 4): `https://www.skool.com/men-of-apollo-7705/classroom/3d2ea192?md=87af3623238a46769bf99b102f1ba8e1`

If Anton wants screenshot artefacts in the repo for offline reference, he can drop them into `content/apollo/lovable/reference/skool-men-of-apollo/` — the directory is created and tracked. Naming convention: `0X-{module}-{state}.png`.
