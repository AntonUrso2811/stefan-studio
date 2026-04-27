# QA Checklist — Lovable Session H.0 (Skool-classroom shell)

Run this in the Lovable preview after Pass H.0 lands. Tick each box. Anything failing → Pass H.1 backlog at the bottom.

---

## 1. Modules grid (`/members/modules`)

### Layout
- [ ] 3-column card grid renders on desktop ≥1024px
- [ ] 2-column on tablet 768–1023px
- [ ] 1-column on mobile <768px
- [ ] Page H1 reads "Modules" with subtitle "20 modules · 4 phases · the full path"
- [ ] All five phase sections present in order: Phase 1 · Phase 2 · Phase 3 · Phase 4 · Onboarding (M01 at bottom)

### Phase headers
- [ ] Each phase H2 reads correctly (Foundation / Integration / Mastery / Longevity / Onboarding)
- [ ] Right-side chip shows `0/6 complete` for unlocked phases, `Locked · Unlocks Day 30` (etc.) for gated
- [ ] Subtitle line shows `Day 0–30 · All members`, `Day 30–60 · Community tier`, etc.
- [ ] 1px stone divider below subtitle

### Card anatomy
- [ ] Cover region shows large module numeral (Source Serif 4 display, ~84px)
- [ ] A-mark glyph below numeral
- [ ] 2px ox-blood horizontal rule centered
- [ ] Phase tint barely perceptible across phases (P1 neutral → P4 slight ox-blood warm)
- [ ] Eyebrow `PHASE X · MODULE N` in IBM Plex Mono all caps, stone
- [ ] Title in Source Serif 4, display case, bone
- [ ] Tagline = module `lede` from frontmatter, IBM Plex Sans, stone, max 2 lines with ellipsis
- [ ] Footer strip: 4px progress bar (stone bg, ox-blood fill) + tier badge (Protocol/Community) right-aligned

### Card states
- [ ] **Hover:** card lifts 4px, border goes ox-blood @ 60%, title gets ox-blood underline pulse
- [ ] **Locked (P2/P3/P4):** cover opacity 40%, lock icon top-right, footer shows `Unlocks Day X` chip
- [ ] **Completed:** progress bar at 100%, ✓ chip top-right, no other state changes

### Click behaviour
- [ ] Click M02 card → routes to `/members/modules/apollo-initiation`
- [ ] Click M07 card → routes to `/members/modules/recovery-system`
- [ ] Click any locked card (e.g. M08) → routes to teaser state at `/members/modules/{slug}`

### Coverage
- [ ] All 20 modules present (M01 through M20)
- [ ] Each module appears in exactly one phase
- [ ] M01 (Welcome) appears in Onboarding section at bottom

---

## 2. Module detail (any unlocked module — test M02 first)

### Top bar
- [ ] Left link `← Back to Modules` → returns to `/members/modules`
- [ ] Right shows eyebrow `Phase 1 · Module 02` (IBM Plex Mono, all caps, stone)
- [ ] Eyebrow stays sticky on scroll (desktop only)

### Lesson rail (left, 280px sticky)
- [ ] Section header `LESSONS` in IBM Plex Mono caption all caps
- [ ] One row per H2 found in the module's markdown body
- [ ] Each row: ○ icon (unchecked) or ✓ icon (checked) + title from H2 heading text
- [ ] Click a lesson row → smooth-scroll to that H2 anchor, no page reload
- [ ] Currently-visible H2 → its rail row becomes bold + ox-blood left border
- [ ] Below lessons: 32px gap, then `APOLLO CODEX` header
- [ ] Codex rows show `→ {entry_id} {entry_title}` for entries wired to this module
- [ ] Click Codex row → routes to `/members/codex/{entry_id}`

### Main pane top
- [ ] H1 = module title in Source Serif 4, 48px, bone
- [ ] Sub-headline = module `lede` from frontmatter, IBM Plex Sans, 20px, stone
- [ ] Top-right: `Mark module complete` button — disabled state initially, label says "Complete all lessons to mark module"
- [ ] After all lessons checked: button activates, label becomes `✓ Mark module complete`, ox-blood bg

### Body
- [ ] Body content renders verbatim from `content/apollo/modules/module-XX-*.md` — open the source file in a separate tab and spot-check 3 paragraphs match exactly
- [ ] H2 sections render with anchor IDs (kebab-cased)
- [ ] No content has been summarised, rewritten, or shortened
- [ ] At end of each H2 section: small `[ ○ Mark complete ]` button. Click → `[ ✓ Complete ]` in ox-blood. Rail row updates simultaneously.

### Footer block
- [ ] `RESOURCES` header in IBM Plex Mono caption
- [ ] Resources list shows same Codex entries as the rail (deduplicated)
- [ ] `Discuss this in Community →` row, full-width, click routes to `/members/community?tag=module-02`
- [ ] Footer nav: left `← Previous module` (hidden on M01), right `Next: {Module Title} →` (hidden on M20)
- [ ] Previous/next routes resolve correctly per manifest order

---

## 3. Locked-module teaser (test M08, M14, or M19 with system date pretending to be Day 0)

- [ ] Page renders with same top bar + H1 + sub-headline
- [ ] Body region replaced with: lock icon (32px, stone) + "This module unlocks on Day {X}. Stay the course." + back-to-modules link
- [ ] Lesson rail hidden
- [ ] Codex rail section still renders if entries are wired
- [ ] Top-right mark-complete button hidden

---

## 4. Voice + content fidelity

Spot-check four modules from different phases. Open each module page side-by-side with its source markdown.

- [ ] **M02** (`module-02-apollo-initiation.md`) — body identical
- [ ] **M07** (`module-07-recovery-system.md`) — body identical
- [ ] **M13** (`module-13-phase-2-integration.md`) — body identical
- [ ] **M19** (`module-19-longevity-optimisation.md`) — body identical

For each:
- [ ] No em-dashes introduced into chrome strings (eyebrows, buttons, CTAs, badges)
- [ ] UK English preserved in body (e.g. "optimise", "behaviours" — not Americanised)
- [ ] No refused-vocab leaked into chrome (cross-check `brand-kit/01-foundation/foundation-brief.md` §6)

---

## 5. Brand fidelity

- [ ] All colours sourced from `brand-kit/02-tokens/colors_and_type.dark.css` — open DevTools → inspect any element → confirm `color`/`background-color` resolve to `var(--ink|bone|ox-blood|stone)`. No raw hex literals.
- [ ] Source Serif 4 used on H1, H2, H3, card titles, cover numerals
- [ ] IBM Plex Sans used on body text, taglines, button labels
- [ ] IBM Plex Mono used on eyebrows, captions, badges
- [ ] --ox-blood used as single accent — count ox-blood instances per state. Each state (default, hover, focus, link, badge) should pick at most one ox-blood role, not stack them.

---

## 6. Mark-complete state persistence

- [ ] Tick a lesson on M02 → reload page → state persists (✓ stays in rail and on the inline button)
- [ ] Tick all lessons on M02 → "Mark module complete" button activates → click it → reload → module shows complete
- [ ] Return to `/members/modules` → M02 card progress bar shows correct % (lessons-complete / total-lessons)
- [ ] Phase 1 header chip shows `1/6 complete`
- [ ] DevTools → Application → Local Storage → keys are formatted as `apollo:lesson:{slug}:{anchor}` and `apollo:module:{slug}:complete`

---

## 7. Mobile experience (≤540px)

- [ ] Cards stack 1-column with full anatomy
- [ ] Module detail rail becomes a drawer triggered by a `Lessons (X/Y)` button
- [ ] Drawer slides from left, full-height, dismissible by tap-outside or Esc
- [ ] Mark-complete buttons remain tappable
- [ ] Footer nav stacks vertically (Previous block above Next block)
- [ ] No horizontal overflow

---

## 8. Routing + edge cases

- [ ] Direct URL `/members/modules/apollo-initiation` loads the module detail correctly
- [ ] Bad slug `/members/modules/does-not-exist` → 404 or graceful "module not found" state
- [ ] Sidebar nav unchanged (Apollo, Anton Urso, Dashboard, Modules, Apollo Codex, Training, Recovery, Kitchen, Journal, Apollo Agent, Community, Messages, Leaderboard, Members, Calendar, Map, Settings — all still present)
- [ ] `/members/codex`, `/members/community`, `/members/agent` routes unchanged from Session G state

---

## H.1 backlog (record failures here)

For each failing item above, log:

| Item | Severity (block / polish) | Notes |
|---|---|---|
|   |   |   |

When the H.1 backlog is non-empty, write the next pass brief at `content/apollo/lovable/session-h-skool-classroom-shell.v2.md` and run a focused fix pass.
