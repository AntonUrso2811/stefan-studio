# CHANGELOG

All notable changes to the Urso & Co brand kit.

## v1.5.2 — 2026-04-22

**Added** the Cowork integration layer:

- `08-cowork/copy-urso.md` — brand-overlay copy skill for Cowork. Wraps the universal `/copy` skill with the Urso brand foundation. Delegates craft to `/copy`, applies Copy Bank + Voice System filters, returns traceable output (final copy + trace log + queue for Copy Bank v2 review).
- `COWORK-INSTALL.md` — operator doc for installing the kit into Cowork. Covers knowledge mount path, universal-skill dependency, path-stability rule, versioning discipline, troubleshooting, and the handoff checklist.

**Accessibility pass.** Removed seven `opacity:` values from body text on Bone across `index.html` — per foundation spec, body text uses pure Ink for AAA contrast. Opacity retained only on Ink grounds where Stone-on-Ink already passes AAA without it.

**Token discipline sweep.** Replaced two stray hex values with `color-mix(in oklab, …)` derivations from existing tokens:
- `05-preview/components-links.html` — hover state (`#7a3b42` → 75% ox-blood + 25% bone).
- `06-holding-site/index-print.html` — on-screen page surround (`#e8e4dc` → 85% bone + 15% stone).

## v1.5.1 — 2026-04-22

**Added** two assets that complete the kit:

- `07-deck/Brand Kit Presentation.html` — 12-slide brand deck (1920×1080). Cover · positioning · palette · one-mark rule · type · voice · vocabulary · offer ladder · hard rules · reference implementation · close. All paths relative; drop in anywhere.
- `CLAUDE-CODE-REVIEW-PROMPT.md` — paste-ready prompt for a senior-consultant-grade critical audit of the kit. Commissions strategic, copy, visual, system, and competitive reviews with ranked killshots. Designed for Claude Code or any agent with filesystem access.

## v1.5 — 2026-04-22

**Incorporated** the finalised foundation documents from the brand handoff:

- Added `01-docs/foundation-brief.md` (v1.5 roll-up, status READY).
- Added `01-docs/component-copy-bank.md` — on-voice strings for every component surface, plus banned CTAs + banned section headers + Copy review checklist.
- Added `01-docs/voice-system-v1.md` — the Voice System framework (internal IP).

**Corrected** the locked hero tagline to match the Copy Bank:

- Holding site and print variant were previously set to *"by an ex-DTC operator"*. Restored to the locked *"AI operations for DTC founders, by an ex-DTC founder."*

**Replaced** off-bank placeholder strings in the preview cards with explicit on-voice equivalents:

- Button labels → bank's primary CTAs ("Book a 20-minute discovery call", "Book the audit — £1,497", "Read the case study").
- Card template → bank's pricing-tier template (Audit · £1,497 · one-time fixed · 5-day sprint).
- Form inputs → bank's form labels (Brand name, Top one operational pain right now).
- Inline link example → "See the audit deliverables".
- Body type specimen → bank's short + medium placeholder samples.

**Kit reorganised** into a numbered, self-contained tree (`01-docs/` → `06-holding-site/`) with all relative paths rewritten so the kit works as a drop-in folder or ZIP.

## v1.0 — 2026-04-19

Initial design system synthesis from `urso-brand-handoff/`:

- Brand identity (Phase 5, locked) + house-style (nine-check quality floor) captured in README.
- Tokens layer (`colors_and_type.css`) — four-value palette, variable Source Serif 4 + Plex Sans + Plex Mono.
- Wordmark family copied and placed (primary / lockup / stacked / monogram / favicon).
- Preview card set covering colour, type, components, spacing, iconography, voice.
- One-page holding site (`ui_kits/holding-site/`) built as the first deliverable.
