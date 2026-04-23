# Urso & Co — Design System

AI Operations Studio. UK. B2B. £1–10M DTC-focused, founder-led.

**Never** "AI agency." Studio, partner, or practice.

This folder is the working design system for every Urso & Co deliverable — public, internal, client-facing. Everything here derives from the brand foundation (`urso-brand-handoff/`, read-only, mounted externally at build time); nothing is invented.

## Sources

Foundation version **v1.5** (`brand/foundation-brief.md`). Status: **READY**. The three canonical inputs for every deliverable live in `brand/`:

- `brand/foundation-brief.md` — roll-up / index for the v1.5 brand foundation. Supersedes all earlier revisions. The `/copy` skill consumes this first.
- `brand/component-copy-bank.md` — explicit on-voice strings for components (CTAs, headers, pills, tooltips, card templates, error/empty states). **Use instead of generic SaaS placeholders.** Section *Copy review checklist* is the pre-ship gate.
- `brand/voice-system-v1.md` — the Voice System framework (Urso & Co IP, internal). Use as a quality constraint on any copy generated inside this system; do **not** surface its mechanics, step numbers, Skill filenames, or framework name in public output.

Supporting handoff artefacts (read-only, external at `urso-brand-handoff/`):

- `foundation/brand-identity.md` — Phase 5, locked. Archetype, register, vocabulary, visual system.
- `foundation/house-style.md` — agency overlay. Nine-check quality floor.
- `foundation/offer-brief.md` — five-tier ladder, Big Idea, positioning.
- `outputs/colour/colour-system.md`, `outputs/typography/type-system.md`, `outputs/guidelines/brand-guidelines.md`, `outputs/logo/README.md` — production specs.
- `HOLDING-SITE-PROMPT.md` — spec for the one-page site at ursoandco.co.uk.

Assets (wordmark SVGs + favicon) live in `assets/`. Self-hosted fonts live in `fonts/`.

## Index

| Path | What |
|---|---|
| `colors_and_type.css` | CSS vars for the full colour palette + type scale + semantic tag defaults. Drop into any page; base HTML inherits the brand. |
| `fonts/` | Self-hosted Source Serif 4 (upright + italic, variable TTF). |
| `assets/` | Outlined wordmark SVGs, stacked + lockup, favicon. |
| `brand/` | Canonical foundation inputs — **foundation-brief.md (v1.5)**, **component-copy-bank.md**, **voice-system-v1.md** (internal IP). |
| `preview/` | Design-system review cards — swatches, type specimens, components, patterns. Rendered in the Design System tab. |
| `ui_kits/holding-site/` | The first deliverable: one-page holding site for `ursoandco.co.uk`, hand-coded HTML + CSS, tokens-driven. |
| `SKILL.md` | Agent-Skill entrypoint for reusing this system in Claude Code or elsewhere. |

## Component copy

Before writing any component strings, read `brand/component-copy-bank.md`. It is the on-voice source for buttons, section headers, status pills, tooltips, card templates, form labels, empty / error / 404 states, and placeholder body copy. **Never substitute generic SaaS placeholders** ("Click here", "Learn more", "Get started", "Sign up"). The bank also lists banned CTAs and banned section headers — treat those as hard refuses.

The bank's *Copy review checklist* is the pre-ship gate for any component copy. Every string in `preview/` and `ui_kits/holding-site/` is drawn from it or passes the checklist.

## Voice System (internal IP — do not surface mechanics)

`brand/voice-system-v1.md` documents how Urso & Co installs voice-trained AI operations into clients. Inside this design system, treat it as a **quality constraint** on any copy you generate:

- Specificity over abstraction — every sentence names a specific number, tool, or moment.
- Restraint is the aesthetic — under-claim; let specifics do the work.
- Operator voice over consultant voice — *queue, margin, retention, install* over *synergy, KPI, transformation*.
- Founder DNA, not founder mimicry — capture how they think, not accent tics.
- Verbatim over paraphrase — quote the buyer back to themselves.
- No banned vocabulary, ever.
- Human-in-loop, always.

**Do not** name the framework, step numbers, Skill filenames, Fingerprint deliverable, calibration cadences, or its internal failure-mode taxonomy in public-facing output (holding site, proposals, marketing copy). Internal references — this README, `SKILL.md`, agent instructions — may cite it.

## Content fundamentals

**Register.** Quietly authoritative operator. Basecamp restraint; Stripe Press typographic confidence; Monocle editorial register; a well-designed accountant's letterhead, modernised.

**Archetype.** Sage + Magician. Deliberately *not* Hero ("we'll revolutionise X" is banned) and *not* Caregiver ("we'll take care of everything" misreads the buyer's operator DNA).

**Narrator.** Mid-career operator, 30s–40s. Calm. Specific. Dry. Never exclamation-marks. Never rhetorical questions. No emojis, no hashtags, anywhere.

**Pronouns.** Mostly first-person singular when it's Anton speaking ("I ran a brand for 3.5 years") and second-person when it's the studio addressing the reader ("Your Gorgias queue is 340 tickets deep on Mondays"). Avoid corporate "we" as the default subject — it reads like a generic agency.

**Casing.** Sentence case on all UI copy, buttons, H1–H3. Small-caps via `text-transform: uppercase` + `+0.06em` tracking only on H6 labels. All-caps in body copy is banned — reads heritage.

**Currency.** `£` before the number, no decimals unless meaningful: `£1,497`, `£2,997/mo`, never `£1,497.00`.

**Dates.** ISO for internal / metadata (`2026-04-19`). Natural-language in copy: "Easter Sunday 2025", "December 2025 exit". Never US `mm/dd/yyyy`.

**Numbers.** Specific, never rounded for cleanness. `60,000+ units`, not `60k` in formal copy. Tabular numerals wherever numbers sit in columns.

**UK English, always.** colour, organisation, behaviour, licence (n) / license (v), metre, enrol.

**Oxford comma.** Avoided by default; used only when ambiguity would otherwise result.

**Em dash.** `—` with spaces on either side. One per paragraph, maximum.

### Use freely (signature vocabulary)
ops · install · ship · workflow · voice-trained · runbook · backend · queue · margin · retention · velocity · lever · rig · wire · trenches · stack · loop · audit · cadence · bandwidth

### Never, under any circumstance (refused vocabulary)
agency · transformation · synergy · unlock · seamless · leverage *(verb)* · game-changer · cutting-edge · revolutionary · AI-powered · dive in · circle back · touch base · reach out · at the end of the day · in today's fast-paced world · world-class · best-in-class · next-gen · holistic · end-to-end · deep dive · low-hanging fruit · ideate

### Sentence fingerprint — worked examples

| Do | Don't |
|---|---|
| *"I ran a brand for 3.5 years and sold it. Now I install the ops infrastructure I wish I'd had."* | *"We are a team of passionate AI operations experts serving ambitious e-commerce brands."* |
| *"Five days. £1,497. Working system at the end of it."* | *"Our comprehensive AI readiness audit delivers transformational insights."* |
| *"Your Gorgias queue is 340 tickets deep on Mondays. We take it to 40."* | *"We help brands unlock next-generation customer experience capabilities."* |
| *"UK-based. GDPR, PECR, and EU AI Act posture from day one."* | *"We're a global AI-first studio delivering enterprise-grade compliance-adjacent solutions."* |

Declarative. Periodic. 12–18 words on average, varying wildly. Noun-first, verb second, specific detail third.

## Visual foundations

**Colour.** Four values, no tints.

| Token | Hex | Role |
|---|---|---|
| Ink | `#0f1114` | Primary — wordmark, body, headings. Warm near-black, never pure `#000`. |
| Bone | `#f6f2eb` | Secondary — default page ground. Warm off-white, paper register. |
| Ox-blood | `#5b1e24` | Accent — **one mark per asset**. Deep muted burgundy; reads as ink dried on paper. |
| Stone | `#c4bdb4` | Utility — dividers, captions on Ink grounds, metadata. Never text on Bone (1.67:1 fails). |

Default composition is Ink on Bone. The one-mark rule is doctrine: pick *one* placement for Ox-blood per asset — the italic ampersand in the wordmark, an inline link, a hairline rule, a single numeric accent, or a hover state. Using it twice is a bug. B&W fallback passes on every asset — ox-blood desaturates to deep charcoal, not black, not silver.

**Type.** Source Serif 4 (wordmark + H1–H3 + display) + IBM Plex Sans (body + UI + H4–H6) + IBM Plex Mono (data only, never prose). Two faces per asset; Mono is the third only inside data blocks. The ampersand in "Urso & Co" is always set in Source Serif 4 Italic 600 — the single typographic flourish.

**Banned faces.** Inter, Poppins, Manrope, DM Sans, Outfit, Work Sans, Futura, Avenir, Playfair, Didot, Bodoni, Roboto, Open Sans, Times New Roman, Arial, Helvetica, Calibri. Any script / brush / handwritten display face.

**Spacing.** Rhythm over grid. Whitespace is structure, not emptiness. Body copy at 60–75 characters per line. Paragraph spacing does the work; no first-line indents. Sections separated by whitespace and hairline Stone rules — nothing else. No alternating row fills, no card shadows to fake structure.

**Backgrounds.** Bone on default. Occasional reversed-out blocks on Ink for hero pull-quotes, footer strips, CTA fills. **No gradients.** No patterned backgrounds, no textures, no repeating motifs, no "hero illustration." The page is the page.

**Imagery.** Typography on whitespace is the default "hero image." If imagery enters (later, with photographer brief) it is documentary, desaturated or colour-calibrated warm (Bone-register neutrals), uncropped-at-angle, and never stock. **Banned:** stock photography, AI-generated imagery, 3D blobs, neon glows, circuit-board motifs, "AI brain" illustrations, bear mascots / forest imagery, emojis.

**Borders.** 1 px Stone hairlines only. No dashed, dotted, or double rules. No coloured left-border accents on cards — it reads as a 2020 SaaS trope.

**Radii.** Sharp corners by default (`border-radius: 0`). One narrow exception: form inputs and buttons may use `2px` for optical softness at small sizes. Anything above `4px` drifts into SaaS register.

**Cards.** Hairline border, no shadow, no rounded corners. Flat, paper-like. Elevation is communicated by position and type size, not by drop shadow.

**Shadows.** None. No elevation system. No `box-shadow` anywhere in the UI. If something needs to feel "up," use type weight or whitespace.

**Transparency and blur.** None in v1. No `backdrop-filter`. No 70% overlays. If a surface needs to differ from the page, it differs by colour (Bone → Ink), not by translucency.

**Hover states.** Links: colour shifts from Ox-blood `#5b1e24` to `#7a3b42` (the "lighter burgundy" functional state — not a palette entry, never exported as a brand colour) and a 1 px border-bottom appears. Buttons: invert — Ink fill → Ox-blood fill, Bone text throughout. No background-colour "highlight" sweeps. No shimmer, pulse, or glow.

**Press states.** No colour change; a subtle `transform: translateY(1px)` only, 80 ms. Never shrink the element — no `scale(0.98)` bounces. The UI is a printed page that happens to respond; not a mobile app.

**Focus states.** 2 px Ox-blood outline at 2 px offset. Keyboard-visible only (`:focus-visible`). No glow.

**Animation.** Near-none. The brand is a printed page, not a product surface. Allowed: link colour transitions (120 ms, ease), button fill inversions (120 ms, ease), fade-in on page load at hero (200 ms, ease-out) — *if at all*. Banned: parallax, scroll-linked effects, reveal-on-scroll chains, Lottie files, bouncy easings, tilt-on-hover cards.

**Easing.** `ease` or `ease-out` for the handful of transitions. No `cubic-bezier` flourishes.

**Iconography.** Text-first. See `preview/iconography.html`. No icon adjacent to body text. No emoji, no unicode icon glyphs as decoration (`✔` `→` `●` etc. in copy). Em dash (`—`), hyphen (`-`), bullet (`·`), numerals, and hairline rules are the only visual glyphs allowed in flowing copy. Lucide may be imported as a last resort for genuine UI chrome (close button on a modal, for example) — stroked at 1.5 px, Ink colour. Flagged: no icon system has been commissioned yet; ask before adding any.

**Ampersand.** Feature, not filler. Always italic Source Serif 4 600. Optional Ox-blood tint on hero assets *only* if the accent is not used elsewhere in that asset.

**Scale discipline.** Every mark reads at 24 px favicon and at 2 m banner. If it breaks at either, it isn't done.

**Layout rules.**
- `text-align: left` everywhere. No justification (produces rivers in Plex Sans). No centred body.
- Single column narrow (measure: 68 ch). Two columns only in editorial templates (one-pager, proposal cover).
- H1 occurs once per document.
- No fixed headers with transparency. If a header needs to persist, it persists as opaque Bone with a Stone hairline.

## Iconography

**Approach.** Typography is the iconography. The brand's mark *is* the wordmark; the wordmark's decorative moment is the italic ampersand. Beyond that: hairline rules, em dashes, bullet middots (`·`), and numerals in IBM Plex Mono do the visual work.

**No icon font. No icon sprite. No SVG icon set has been commissioned for v1.** See `assets/` — it contains exactly the wordmark family (primary, lockup, stacked, monogram) and the favicon.

**Emoji.** Never. Banned in brand assets, proposals, client-facing deliverables, and throughout the site.

**Unicode glyphs in copy.** Allowed only as typographic cadence — `—`, `·`, `–`, `£`, `&` where appropriate. Disallowed as decoration: `→`, `✔`, `●`, `▸`, tick marks, arrows, stars, emoji-derived marks.

**If genuine UI chrome needs a mark** (a close button on a modal, a sort arrow in a data table), use an inline SVG drawn at 1.5 px stroke weight in Ink, visual size 16–20 px. Lucide is the nearest-acceptable CDN substitute if a set is needed quickly — flag the substitution; it is not an Urso & Co decision yet.

**When in doubt.** Delete the icon. Use a word or a number instead.

## Fonts

Source Serif 4 is **self-hosted** from `fonts/` as a variable TTF (opsz 8–60, wght 200–900, upright + italic), wired via `@font-face` in `colors_and_type.css`. IBM Plex Sans + Mono load from Google Fonts (SIL OFL 1.1) at the top of the same file.

- Source Serif 4 — variable TTF, self-hosted. `fonts/SourceSerif4-VariableFont_opsz_wght.ttf` + `-Italic-` variant.
- IBM Plex Sans — weights 300 / 400 / 500 / 600 + 400 italic (Google).
- IBM Plex Mono — weights 400 / 500 (Google).

Optical-size axis is tuned per heading level (hero: 60, h1/h2: 48, h3: 32, editorial body: 14) via `font-variation-settings` in the tokens file.

For offline or embedded delivery, convert IBM Plex to self-hosted WOFF2 and swap the Google `@import` for a local `@font-face` block. Fallback stacks map serif → Georgia (deliberate; Georgia holds the operator-editorial register better than Times at body sizes), sans → system-sans, mono → system-mono.

## Design-system review cards

`preview/` holds small HTML cards (≈700 × 150 px each) showing every piece of the system in isolation — colour swatches, type specimens, component states, spacing, iconography rules. Registered into the Design System tab, grouped into Type, Colors, Spacing, Components, and Brand sections.

## UI kits

| Kit | Purpose | Path |
|---|---|---|
| `holding-site` | The first deliverable. One-page `ursoandco.co.uk`: hero lockup, tagline, positioning paragraph, Cal.com CTA, compliance footer. | `ui_kits/holding-site/index.html` |

No slides deck is shipped in this system (none was provided in the handoff, and the studio's first public artefact is the holding site, not a deck). If slide templates are commissioned later, they live at `slides/`.

## Caveats

- **No icon system exists.** Intentional for v1. Flagged.
- **No dark mode.** Intentional per `colour-system.md` handling notes.
- **No photography brief.** Typography carries the brand; imagery is out of scope.
- **Cal.com account placeholder.** The holding site CTA points to `https://cal.com/ursoandco/discovery` — URL set; account setup lives outside this project.

## Related

- `SKILL.md` — Agent-Skill entrypoint.
