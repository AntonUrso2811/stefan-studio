# Lovable Session C v2 — Modules typography pass (modules-only)

**Paste this into Lovable as a single prompt.** Driver: Anton. Stefan reviews the finished state (live preview URL) after Session C v2 completes. Ships on top of Session A (20 modules loaded, verbatim body) + Session B (Protocol lander "Who is this for?" rewrite, reviews consolidation already deployed). Supersedes `session-c-final-polish.v1.md`.

---

## Context

You are editing Stef's Apollo's Ascent site on Lovable. This session is **modules-only**. The home page, /protocols lander, and any other lander are **out of scope** in this session — they will be addressed in Session D, which is being authored alongside a conversion audit currently in flight.

What changed in the repo (already shipped, merged to main as commit `05104b7` via PR #1): every module markdown file at `content/apollo/modules/module-NN-*.md` now has named **h2 and h3** structural headings derived verbatim from concept-lead sentences already in the prose. Body sentences are byte-identical to the prior verbatim-body state — only heading lines were added. Module-14 (Phase 3 overview) was intentionally left untouched (single short section).

Session A v2's verbatim-body contract still holds: do not rewrite or paraphrase any module body text. If a module's content appears to disagree with anything in this prompt, the markdown file wins.

This session ships **one job**: the Lovable render-layer typography that makes the new h2/h3 hierarchy actually readable on the device it's served on. Stefan's feedback was specifically that modules read like a Wikipedia page with text "very small". This pass fixes that.

**Voice anchor.** Match the current live site's body-copy voice — specifically the module bodies and founder-voice paragraphs. This job does not touch copy, only render.

**Output format.** After completing the job, respond with:
1. Summary of every change, file-by-file or component-by-component.
2. Typography spec applied (confirm the token names / CSS variables touched).
3. Regression check: explicit confirmation that home, /protocols, and any other lander render unchanged from before this prompt.
4. Anything you couldn't complete + why.

Deploy to preview (not production). Anton will QA against `qa-checklist-session-c.md` before handing the preview URL to Stefan.

---

## Job 1 — Module pages: hierarchy + typography (Lovable render layer)

**Current state (per Stefan, 2026-04-24):** modules render as walls of dense prose. Stefan's exact words: "the modules inside are just text with no subheader chapters as in school... its like a wikipedia page and the text is very small. needs more clarity and easier to read."

**What's already done in the repo (do not touch the markdown files):** all 20 modules have named h2/h3 structural headings now. Your job is the **render layer** — typography, auto-TOC, scroll-progress, mobile readability — applied to the **module page template only**.

### Typography spec (apply to module pages)

**Body text:**
- Mobile: 18px / 1.65 line-height
- Desktop: 19px / 1.7 line-height
- Measure: 66ch max-width on desktop, 92vw on mobile
- Paragraph spacing: 1.25em between paragraphs. No first-line indent.

**Headings:**
- **h1** (module title from frontmatter): 40/44 mobile, 56/60 desktop, letter-spacing −0.015em
- **h2**: 28/34 mobile, 32/40 desktop, 2.5em top margin, 0.75em bottom margin, hair-rule `border-top: 1px solid Stone` immediately above
- **h3**: 22/28 mobile, 24/30 desktop, 1.75em top margin, 0.5em bottom margin

**Frontmatter lede** (subtitle on module pages, if present): 22/30 mobile, 26/34 desktop, 400 weight, 70% opacity.

### Auto-generated Table of Contents (module pages only)
- Derive from h2 headings only (not h3).
- Desktop: render at top of module page, sticky in right-side margin below a viewport offset, or inline above the first h2 if no margin space.
- Mobile: collapsed sticky drawer, icon in top-right. Tap to expand. Auto-close on anchor tap.
- Active section highlighted as the user scrolls past each h2.

### Scroll-progress bar (module pages only)
- Hairline bar at the top of the viewport, `position: fixed`, 2px tall, Apollo accent colour. Fills left-to-right as the user scrolls the module body.
- Do NOT add this to landers, the home page, or any other surface.

### Mobile readability regression
- Check 320px, 375px, 414px widths. Body text must not compress below 18px.
- Stress-test against `module-10-nutrition-optimisation.md` (the largest module, ~5,568 words).
- Module pages on mobile must be thumb-navigable — TOC drawer reachable without stretching.

**Keep in scope:** module page template, type scale tokens scoped to module pages, TOC component, scroll-progress bar.

**Out of scope (do not modify under any circumstance):**
- Module content — the markdown files are sealed for this session.
- Home page typography, layout, copy, or any component on it.
- /protocols lander typography, copy, "Who is this for?" block, or any component on it.
- /community lander typography, copy, or any component on it.
- The universal reviews block — wherever it currently lives, leave it. Reviews are deferred to Session D.
- Imagery — hero, module card, testimonial photos. All deferred to Session D.
- Customer review submission form, Supabase wiring, admin moderation routes — deferred to Session D.
- Navigation chrome, footer, auth flows.

If type tokens are global and changing them on module pages would change them elsewhere, **scope the new tokens to module pages only** (e.g. body class, layout slot, route-specific stylesheet) — do not let the typography change leak.

---

## Final output

After Job 1 completes, respond with the four-point summary from the Context section. Flag anything you could not finish. Include the deploy-preview URL at the top of the response.

**Critical confirmation required:** state explicitly that home, /protocols, /community, the reviews block, imagery, and the customer review submission area are unchanged from their pre-v2 state.

Deploy to preview (not production). Anton will QA against `content/apollo/lovable/qa-checklist-session-c.md` before handing the preview URL to Stefan.
