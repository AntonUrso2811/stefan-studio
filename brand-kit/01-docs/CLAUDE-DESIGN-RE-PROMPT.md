---
type: reference
status: current
updated: 2026-04-22
tags:
  - brand
  - handoff
  - prompt
  - claude-design
  - re-upload
aliases:
  - Claude Design Re-Prompt
  - Design Re-Upload
  - CDRP
---

# Claude Design — Re-Upload Package & Re-Prompt

> Use this when re-running Claude Design (claude.ai/design) so it produces output fully aware of: foundation v1.5, the wordmark selection (C1), the 4 outlined SVGs + 19 PNGs + favicon, the component copy bank, and the Voice System framework. This is the canonical "press play again" artefact for any future Claude Design re-run.

Sibling artefacts: [[FIRST-PROMPT]] (chat-mode), [[BRAND-KIT-PROMPT]] (Cowork kit production), [[BRAND-KIT-FINALISE-PROMPT]] (Cowork outline + raster), [[HOLDING-SITE-PROMPT]] (Cowork holding site build).

---

## Goal

Tell Claude Design that the brand kit is **finished and production-ready** — its job is to generate a *design system* (semantic tokens, component library, layout primitives, interaction states, motion principles) that *consumes* the existing brand kit, not redesigns it.

The design system Claude Design produces should serve **(a) marketing site** primarily — the holding site today, multi-page in month 3+. Not a product UI. Not a client template library (those are handled by pandoc/markdown).

---

## What you upload — exact manifest

### Field 1 — Company name and blurb

Paste this verbatim:

```
Urso & Co — AI operations studio for £1–10M UK DTC brands

Founded by an ex-DTC operator (multiple seven figures, 60,000+ units
shipped, exited Dec 2025). The studio installs voice-trained AI
operations into client workflows: CX triage, subscription churn
recovery, supplier ops hubs.

Brand foundation v1.5, fully locked. Visual system:
- Typography: Source Serif 4 (wordmark + display) + IBM Plex Sans
  (body / UI) + IBM Plex Mono (data / numbers)
- Colour: Ink #0f1114 (primary) + Bone #f6f2eb (secondary) +
  Ox-blood #5b1e24 (accent, ONE mark per asset rule) + Stone #c4bdb4
  (utility / structural)
- Wordmark: Concept 1 selected — title case "Urso & Co" with italic
  ampersand, default kerning, ink-only

OUTPUT GOAL: marketing site design system. Component primitives for
hero, body sections, CTA, footer + future case study card, pricing
tier card, ROI report card. NOT a product UI (no dashboard, forms,
auth, dropdowns, modals). NOT a client template library (PDFs from
markdown via pandoc handle that).

Voice register: operator, not consultant. "AI operations studio /
partner / practice" — never "AI agency". Specific numbers, plain
English, no "transform your business" vocabulary. Component-level
sample copy already specified in outputs/copy/component-copy-bank.md.
```

### Field 2 — Link code on GitHub

**Skip.** No public repo for the kit (private framework decision; foundation v1.4 onwards keeps voice-system internal for first 90 days).

### Field 3 — Link code from your computer

**Drag in the entire folder:**

```
/Users/antonurso/Documents/Claude/Projects/Urso & Co — 90 Day Build/urso-brand-handoff/
```

This folder is the canonical brand kit + foundation. Sub-folders Claude Design will see:

- `foundation/` — 8 docs covering avatar, positioning, voice, beliefs, identity, agency overlay
- `outputs/logo/` — 5 concept SVGs + 4 outlined SVGs + monogram + favicon + 19 PNGs + README
- `outputs/colour/colour-system.md` — palette + WCAG table + Pantone notes
- `outputs/typography/type-system.md` — type stack + scale + variable axes + fallback
- `outputs/templates/` — 5 applied templates (banner spec, email sig HTML, proposal, one-pager, invoice)
- `outputs/copy/component-copy-bank.md` — component-level on-voice copy strings
- `outputs/guidelines/brand-guidelines.md` — one-page contractor synthesis
- `methods/voice-system-v1.md` — internal IP (Voice System framework)
- `_context/` — 5 source briefs (positioning, voice, name, playbook, deep research takeaways)
- `CLAUDE.md` — orientation doc

**Do NOT upload:** the parent vault folder (`Urso & Co — 90 Day Build/`). That contains strategy docs, pipeline records, ops scripts irrelevant to design system generation. Only `urso-brand-handoff/` should be attached.

### Field 4 — Upload a .fig file

**Skip.** No Figma file exists. Outlined SVGs in `outputs/logo/` cover what a .fig would carry.

### Field 5 — Add fonts, logos and assets

Belt-and-braces — explicit asset uploads even though they're in the folder above. Drag in:

**Fonts (7 files):**

If `~/.local/share/fonts/urso/` exists from the brand kit finalisation run, drag from there. Otherwise download fresh from Google Fonts:

| File | Source |
|---|---|
| `SourceSerif4-VariableFont_opsz,wght.ttf` | https://fonts.google.com/specimen/Source+Serif+4 |
| `SourceSerif4-Italic-VariableFont_opsz,wght.ttf` | same ZIP |
| `IBMPlexSans-Regular.ttf` | https://fonts.google.com/specimen/IBM+Plex+Sans |
| `IBMPlexSans-Medium.ttf` | same ZIP |
| `IBMPlexSans-SemiBold.ttf` | same ZIP |
| `IBMPlexMono-Regular.ttf` | https://fonts.google.com/specimen/IBM+Plex+Mono |
| `IBMPlexMono-Medium.ttf` | same ZIP |

**Logo SVGs (4 files — production-ready, font-independent):**

- `urso-brand-handoff/outputs/logo/wordmark-primary-outlined.svg`
- `urso-brand-handoff/outputs/logo/wordmark-monogram-outlined.svg`
- `urso-brand-handoff/outputs/logo/wordmark-stacked-outlined.svg`
- `urso-brand-handoff/outputs/logo/wordmark-lockup-outlined.svg`

**Favicon (1 file):**

- `urso-brand-handoff/outputs/logo/favicon.ico`

**Sample PNGs (3 files for raster reference):**

- `urso-brand-handoff/outputs/logo/png/wordmark-primary-800.png`
- `urso-brand-handoff/outputs/logo/png/wordmark-lockup-460.png`
- `urso-brand-handoff/outputs/logo/png/monogram-256.png`

Total: 7 fonts + 4 SVGs + 1 .ico + 3 PNGs = **15 files**.

### Field 6 — Any other notes?

Paste this verbatim. This is where the non-visual rules live, plus the voice system + copy bank pointers Claude Design needs to honour:

```
LOCKED — DO NOT RE-LITIGATE:

Visual:
- Wordmark: use wordmark-primary-outlined.svg as canonical mark
- Lockup (with descriptor): use wordmark-lockup-outlined.svg for
  banner / proposal cover / hero blocks
- Monogram: use wordmark-monogram-outlined.svg for favicon /
  app icon / square avatar
- Stacked: use wordmark-stacked-outlined.svg for square plate marks
- One ox-blood mark per asset (component, page, banner) — typically
  the price in a pricing card OR an inline link OR the CTA hover
  state; NOT the wordmark itself (the wordmark is ink-only, ox-blood
  is reserved for content accents)
- B&W first: every component must read at full authority with colour
  stripped
- Ink #0f1114 on Bone #f6f2eb is the default surface
- Reverse-out (Bone on Ink) permitted for hero blocks and CTAs
- Bone on Ox-blood permitted for short passages only (pricing badges,
  status pills)
- Ink on Ox-blood is BANNED (1.49:1 contrast — fails WCAG)
- Stone is structural only (dividers, captions, metadata) — never
  body text on Bone (1.67:1 contrast — fails WCAG)

Banned visuals:
- Gradients of any kind
- 3D blobs, glassmorphism, neumorphism
- Stock photography
- AI-generated imagery
- Geometric-sans fonts (Inter, Poppins, Manrope, DM Sans, Outfit)
- Emojis in any brand surface
- Hashtags in any brand surface
- Drop shadows on the wordmark
- Outline / stroke on the wordmark
- Wordmark inside a badge shape or filled tile
- "EST. 2026" or any heritage tagline construction

Banned vocabulary (component sample copy AND any generated text):
- "AI agency" — always "AI operations studio / partner / practice"
- "transformation", "synergy", "unlock" (verb), "seamless"
- "leverage" (as verb)
- "game-changer", "cutting-edge", "revolutionary"
- "AI-powered" (redundant)
- "Click here", "Learn more", "Get started", "Sign up"

Voice register:
- UK English (colour, organisation, behaviour) — not US
- £ symbol, no decimals on round figures (£1,497 not £1,497.00)
- Numbers preserved as-shipped (60,000+ units, not "many thousands")
- ISO dates internally; natural-language dates in user-facing copy

Component sample copy:
- USE the explicit strings in outputs/copy/component-copy-bank.md
- That doc covers: CTAs, section headers, status pills, tooltips,
  card templates (case study ICP / adjacent, pricing tier, ROI
  report), empty states, error copy, sample placeholder copy at
  3 lengths (short / medium / long — drop-in replacement for lorem
  ipsum)
- Do NOT generate generic SaaS sample copy ("Welcome to Urso & Co",
  "Get started today", "Sign up now") — those violate the voice

Voice System framework reference:
- The full framework lives at methods/voice-system-v1.md
- Generated component copy should pass the 7 principles in that doc:
  specificity over abstraction, restraint, operator voice, founder
  DNA not mimicry, verbatim over paraphrase, no banned vocab,
  human-in-loop always

OUTPUT FORMAT PREFERENCE:
- HTML + Tailwind (or vanilla CSS with custom properties) over Next.js
  for v1 — holding site is one page, doesn't need framework overhead
- CSS custom properties at :root for the 4 colours, type scale,
  spacing scale (8px base recommended)
- Mobile-first responsive, single breakpoint at 768px
- Lighthouse target: 95+ on every metric

WCAG (measured):
- Ink on Bone: 16.95:1 — AAA
- Bone on Ink: 16.95:1 — AAA
- Ox-blood on Bone: 11.36:1 — AAA
- Bone on Ox-blood: 11.36:1 — AAA
- Stone on Ink: 10.16:1 — AAA
- Ink on Ox-blood: 1.49:1 — FAIL (banned)
- Stone on Bone: 1.67:1 — FAIL as text (structural use only)

Foundation reference: foundation/foundation-brief.md (status READY, v1.5)
Quality floor: foundation/house-style.md (9-check production checklist)
Voice framework: methods/voice-system-v1.md (internal IP — do not
generate output that exposes the framework's mechanics; use it as
constraint on copy quality)
```

### Click "Continue to generation"

Submit. Watch for these failure signals in the output:

- Falls back to Inter / Poppins / system sans → ✗ reject, re-prompt with explicit Source Serif 4 + IBM Plex Sans references
- Adds gradients, 3D, glassmorphism → ✗ reject
- Uses "AI agency" anywhere in copy → ✗ reject
- Generates more than one ox-blood mark per component → ✗ reject
- Outputs Next.js scaffold when HTML+Tailwind would do → flag, ask for HTML alternative
- Generates lorem ipsum or generic SaaS sample copy → ✗ reject, point at component-copy-bank.md

---

## What you should get back

Best case (when input is honoured):

- A **design tokens file** (CSS custom properties or Tailwind config) codifying the 4 colours + type scale + spacing scale
- A **component library preview** (HTML or React) covering hero, body sections, CTA buttons, footer, case study card, pricing tier card, ROI report card
- All sample text drawn from `component-copy-bank.md` strings
- Wordmark + lockup placed correctly across components
- Favicon embedded in the preview
- Lighthouse-clean HTML output (if HTML format chosen)

Worst case (if Claude Design can't parse the markdown specs cleanly):

- Generic-in-your-palette output that ignores the voice + copy specs
- Ineffective regeneration despite clear input

If worst case fires: switch to Cowork (HOLDING-SITE-PROMPT.md) instead. Hand-coded HTML in 30–60 minutes is faster than fighting a generator.

---

## After Claude Design produces output

Two paths:

### Path A — Output is good
1. Download the design system files from Claude Design
2. Save to `~/studio/ursoandco-site/` (project folder, not in vault)
3. Adapt the holding site index.html from the generated component primitives
4. Deploy via Vercel CLI: `cd ~/studio/ursoandco-site && npx vercel --prod`
5. Point DNS at Vercel
6. Update email signature with the live wordmark URL
7. Done — holding site live

### Path B — Output isn't good enough
1. Skip Claude Design for the holding site
2. Use [[HOLDING-SITE-PROMPT]] in a fresh Cowork session
3. Cowork produces the holding site directly from the brand kit
4. Same deploy path

Either way, the email signature, LinkedIn banner, and applied templates can proceed.

---

## Re-upload checklist (tick before clicking Continue)

- [ ] Company name + blurb pasted (Field 1)
- [ ] `urso-brand-handoff/` folder dragged into Field 3
- [ ] 7 font files dragged into Field 5
- [ ] 4 outlined SVGs dragged into Field 5
- [ ] favicon.ico dragged into Field 5
- [ ] 3 sample PNGs dragged into Field 5
- [ ] Notes block pasted into Field 6
- [ ] Output goal stated (marketing site design system, not product UI)
- [ ] Banned-list explicit (visuals + vocabulary)
- [ ] Component copy bank referenced

---

## Related

- [[_MOC/Brand]] — parent map of content
- [[foundation-brief|Foundation Brief]] — status READY, v1.5
- [[brand-identity|Brand Identity]] — visual + voice system
- [[house-style|House Style]] — quality floor
- [[methods/voice-system-v1|Voice System Method]] — internal IP
- [[outputs/copy/component-copy-bank|Component Copy Bank]] — on-voice strings
- [[BRAND-KIT-PROMPT]] — Cowork kit production prompt (used)
- [[BRAND-KIT-FINALISE-PROMPT]] — Cowork outline + raster (used)
- [[HOLDING-SITE-PROMPT]] — Cowork holding site fallback (if Claude Design output isn't good enough)
- [[FIRST-PROMPT]] — Chat-mode first prompt
