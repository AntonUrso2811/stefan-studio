# QA Checklist — Lovable Session H (v2, Pass H.1)

Run after Lovable lands Pass H.1 (the Skool-mirroring inside-module surface). Tick each box. Anything failing → H.2 backlog at the bottom.

The H.0 grid surface is already shipped. This checklist focuses on the inside-module rebuild only. Any regression on the grid is a P0 — note in the backlog.

---

## 1. Module landing routing

- [ ] `/members/modules/apollo-initiation` (M02) routes to the first lesson, matching Skool's behaviour. URL becomes `/members/modules/apollo-initiation/what-the-next-30-days-will-do-to-you`.
- [ ] `/members/modules/mental-architecture` (M03) routes to the first lesson `/members/modules/mental-architecture/the-identity-shift`.
- [ ] Direct deep-link `/members/modules/apollo-initiation/action-1-set-a-fixed-wake-time` loads correctly.
- [ ] Bad slug `/members/modules/apollo-initiation/does-not-exist` returns 404 or graceful "lesson not found".

---

## 2. Rail anatomy — Module with WEEK groups (M02 Apollo Initiation)

- [ ] Header block shows `THE APOLLO INITIATION` (Source Serif 4, all caps, `--bone`)
- [ ] Progress bar below header: 4px tall, `--stone @ 20%` bg, `--ox-blood` fill
- [ ] Two top-level lesson rows render before the WEEK groups: `What the Next 30 Days Will Do to You`, `30-Day Overview: What Success Looks Like`
- [ ] Four collapsible group rows: `INITIATION WEEK 1` through `INITIATION WEEK 4` (or the literal H2 text from markdown — currently `WEEK 1: RESET + RHYTHM`, etc.)
- [ ] Each group row has a chevron icon, `lucide:chevron-down` collapsed / `lucide:chevron-up` expanded
- [ ] One closing top-level lesson after the groups: `Phase 1 Completion: Preparing for Phase 2`
- [ ] Below the lesson list: `APOLLO CODEX` caption + Codex entries wired to M02

---

## 3. Group expansion behaviour

- [ ] Clicking a group header toggles ONLY that group's expansion. Other groups retain their state.
- [ ] Expanding a group does NOT change the active lesson.
- [ ] When expanded, the group renders:
  - [ ] A small caption sub-header (the H2 text in IBM Plex Mono, all caps, `--stone`, e.g. `WEEK 1: RESET + RHYTHM`)
  - [ ] Then the H3 lesson rows, indented 16px
- [ ] Group expansion state persists across reloads (localStorage)
- [ ] Default state on first visit: WEEK 1 expanded, others collapsed (matches a sensible "where am I starting" default)

---

## 4. Rail anatomy — Module without WEEK groups (M03 Mental Architecture)

- [ ] Header block shows `APOLLO MENTAL ARCHITECTURE` (or `MENTAL ARCHITECTURE` per markdown frontmatter title)
- [ ] Progress bar below header
- [ ] All H2s render as flat lesson rows (no chevrons, no grouping):
  - [ ] `The Identity Shift`
  - [ ] `Discipline Over Motivation`
  - [ ] `The Consistency Compound`
  - [ ] `Mental Models for Training`
  - [ ] `Handling Failure and Setbacks`
  - [ ] `Environment Design`
  - [ ] `The Apollo Mindset Summary`
- [ ] No collapse/expand affordances anywhere in the rail
- [ ] APOLLO CODEX section follows below

---

## 5. Lesson page anatomy (right pane)

Open `/members/modules/apollo-initiation/action-1-review-your-apollo-scorecard` (Action 1 in WEEK 4).

- [ ] Top-right: empty circle for "mark complete" (`lucide:circle`)
- [ ] H1 (lesson title): `Action 1: Review Your Apollo Scorecard`, Source Serif 4, weight 600, ~28px, `--bone`
- [ ] Body renders verbatim from the H3 section in `module-02-apollo-initiation.md` (lines 1092–1126)
- [ ] H4-and-deeper sub-sections (if any) render as bold inline labels, NOT as separate rail items
- [ ] No em-dashes introduced into chrome (eyebrows, button labels, footer)
- [ ] Sign-off line `— Stef` (where present in markdown) renders verbatim

Open `/members/modules/apollo-initiation/30-day-overview-what-success-looks-like` (top-level lesson with H3 sub-sections).

- [ ] H1: `30-Day Overview: What Success Looks Like`
- [ ] Body shows H3 sub-sections (`Physical Changes`, `Performance Changes`, `Energy and Recovery`, `Habit Installation`, `Mindset Shift`) as **bold inline sub-headers within the same lesson page** — NOT as separate rail items
- [ ] Body content matches markdown verbatim

Open `/members/modules/mental-architecture/the-identity-shift` (M03, no groups).

- [ ] Lesson body renders correctly with H3 sub-sections as bold inline sub-headers
- [ ] Footer `Discuss this in Community →` routes to `/members/community?tag=module-03`

---

## 6. Mark-complete behaviour

- [ ] Click the empty circle on a lesson → fills with `--ox-blood` background, `--bone` checkmark glyph
- [ ] Rail row for that lesson shows a small filled checkmark glyph to the LEFT of the title
- [ ] Reload page → state persists (localStorage key `apollo:lesson:{module-slug}:{lesson-slug}` = true)
- [ ] Module progress bar in the rail header updates to reflect (completed / total) %
- [ ] Return to `/members/modules` → that module's card progress bar reflects the same %
- [ ] Phase header chip on `/members/modules` reflects modules-complete / total

---

## 7. Footer nav

- [ ] `← Previous lesson` and `Next lesson →` show below the body, separated by a divider
- [ ] Walking next/prev follows the FLAT rail order, including navigating into expanded WEEK groups
- [ ] Hidden as expected: previous-link absent on first lesson of M01; next-link absent on last lesson of M20

---

## 8. URL patterns

- [ ] Lesson URLs follow `/members/modules/{module-slug}/{lesson-slug}`
- [ ] `{lesson-slug}` is kebab-cased H2 (top-level) or H3 (grouped) text
- [ ] Special characters stripped from slugs: colons, plus signs, brackets all gone (e.g. `Action 3:Remove Liquid Calories and Processed Food` → `action-3-remove-liquid-calories-and-processed-food`)
- [ ] Group headers (WEEK X H2s) do NOT have routable URLs — clicking the group header only toggles expansion

---

## 9. Voice + content fidelity

Spot-check 4 lessons across modules.

- [ ] M02 / `Action 1: Set a Fixed Wake Time` — body identical to markdown
- [ ] M07 / `Recovery Philosophy` — body identical
- [ ] M13 (first lesson) — body identical
- [ ] M19 (first lesson) — body identical

For each:
- [ ] No em-dashes added to chrome
- [ ] UK English preserved (e.g. "optimise", "behaviours")
- [ ] No refused-vocab leaked into chrome (cross-check `brand-kit/01-foundation/foundation-brief.md` §6)

---

## 10. Brand fidelity

- [ ] All colours from `brand-kit/02-tokens/colors_and_type.dark.css` (no hex literals in components — DevTools spot-check)
- [ ] Source Serif 4 on H1, card titles, module title in rail header
- [ ] IBM Plex Sans on lesson rail rows + body paragraphs
- [ ] IBM Plex Mono on eyebrows / sub-headers / badges
- [ ] `--ox-blood` used as single accent — one role per state, not multiplied across hover + active + focus + link

---

## 11. Mobile (<768px)

- [ ] Rail collapses to a `Lessons (X/Y)` button anchored at the top
- [ ] Tapping the button opens a left-side drawer at full height
- [ ] Drawer contains the same rail content (groups + lessons + Codex)
- [ ] Selecting a lesson dismisses the drawer and loads the lesson page
- [ ] Drawer dismissable by tap-outside or Escape key
- [ ] Mark-complete circle remains tappable in lesson header
- [ ] Footer nav stacks vertically (Previous block above Next block)
- [ ] No horizontal overflow

---

## 12. Regression check (H.0 surfaces unchanged)

- [ ] `/members/modules` grid: 3-col phase-grouped cards still render
- [ ] Phase headers, locked-phase chips, card hover, card progress bars all behave as in H.0
- [ ] M01 (Onboarding) still appears in the Onboarding section at the bottom of the grid
- [ ] Sidebar nav unchanged: Apollo, Anton Urso, Dashboard, Modules, Apollo Codex, Training, Recovery, Kitchen, Journal, Apollo Agent, Community, Messages, Leaderboard, Members, Calendar, Map, Settings
- [ ] `/members/codex`, `/members/community`, `/members/agent` routes unchanged

---

## H.2 backlog (record failures)

| Item | Severity (block / polish) | Notes |
|---|---|---|
|   |   |   |

When the H.2 backlog is non-empty, write the next pass brief at `content/apollo/lovable/session-h-skool-classroom-shell.v3.md` and run a focused fix pass.
