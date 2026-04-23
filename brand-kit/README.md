# Urso & Co — Brand Kit

**Version 1.5.2** · Foundation status: **READY** · Last update: 2026-04-22

This folder is the complete, self-contained brand kit for Urso & Co — the UK AI operations studio for £1–10M DTC brands. Everything needed to produce an on-brand asset is here: docs, tokens, fonts, logos, component specimens, and the production holding-site source.

**Open `index.html` in a browser for a visual overview of what the kit contains.**

## What's inside

| Folder | What |
|---|---|
| `01-docs/` | Canonical documents. Start here. |
| `02-tokens/` | `colors_and_type.css` — the single CSS file that wires colours, fonts, and type scale into any HTML. |
| `03-fonts/` | Self-hosted Source Serif 4 (upright + italic, variable TTF). IBM Plex Sans + Mono load from Google Fonts via the tokens file. |
| `04-logos/` | Outlined wordmark family + favicon. SVG. |
| `05-preview/` | Design-system review cards — one HTML file per token / component, viewable in a browser. |
| `06-holding-site/` | Production source for `ursoandco.co.uk` — the first deliverable. Reference implementation for how the tokens are applied. |
| `07-deck/` | **Brand Kit Presentation** — 12-slide deck (1920×1080) walking through positioning, palette, type, voice, offer ladder, rules, and the reference implementation. Open `Brand Kit Presentation.html`. |
| `../skills/copy-urso.md` | Cowork integration — brand-overlay `copy-urso.md` skill that wraps the universal `/copy` skill with the Urso brand overlay. Now lives at repo root in `skills/` (sibling to `brand-kit/`). |
| `COWORK-INSTALL.md` | Operator doc for installing the kit + skills into Cowork. Path-stability rule, versioning discipline, troubleshooting. |
| `CLAUDE-CODE-REVIEW-PROMPT.md` | Paste-ready prompt for a rigorous third-party critical audit of this kit. |

## Reading order

1. `01-docs/README.md` — full manifest: content fundamentals, visual foundations, use-freely and refused vocabulary, component-level rules.
2. `01-docs/foundation-brief.md` — v1.5 roll-up. Archetype, register, positioning, five-tier offer ladder, nine-check quality floor.
3. `01-docs/component-copy-bank.md` — on-voice strings for every component. **Use instead of generic SaaS placeholders.** The Copy review checklist at the end is the pre-ship gate.
4. `01-docs/voice-system-v1.md` — the Voice System framework (Urso & Co IP, internal). Use as a quality constraint on generated copy. **Do not surface its mechanics publicly** — framework name, step numbers, Fingerprint deliverable, calibration cadences, or the failure-mode taxonomy.
5. `01-docs/SKILL.md` — agent-skill entrypoint for reusing this system in Claude Code.

## Quick reference — the hard rules

1. **Never** call Urso & Co an "AI agency." Studio, partner, or practice.
2. **One ox-blood mark per asset.** Default composition is Ink (`#0f1114`) on Bone (`#f6f2eb`).
3. **Two typefaces per asset** — Source Serif 4 + IBM Plex Sans. Mono only for data.
4. **No** gradients · shadows · emoji · hashtags · stock or AI imagery · rounded corners above 2 px · scroll animations.
5. **UK English throughout.** `£` before the number, no decimals on round figures. ISO dates in metadata.
6. **Locked hero tagline** — *"AI operations for DTC founders, by an ex-DTC founder."* Do not paraphrase on the hero surface.
7. **Refused vocabulary** (partial): transformation · synergy · unlock · seamless · leverage (v.) · game-changer · cutting-edge · revolutionary · AI-powered. Full list in `01-docs/README.md`.
8. **Banned CTAs** — "Click here" · "Learn more" · "Get started" · "Sign up" · "Submit". Replace with a specific action naming a specific outcome.

## Paths & relative refs

All internal references inside this kit are relative, so the kit works whether opened as a folder, zipped, or dropped into a monorepo unchanged. If you lift `02-tokens/colors_and_type.css` into another project, copy `03-fonts/` alongside it and update the `@font-face` `src: url("../03-fonts/…")` paths to match.

## Licence

- **Source Serif 4** — SIL OFL 1.1 (Adobe). Self-hosted copy included.
- **IBM Plex Sans + Mono** — SIL OFL 1.1 (IBM). Loaded from Google Fonts.
- **Wordmark, photography, copy, voice system, all `brand/` documents** — © Urso & Co. All rights reserved.

## Contact

studio@ursoandco.co.uk · Companies House #16980197 · ICO-registered · UK
