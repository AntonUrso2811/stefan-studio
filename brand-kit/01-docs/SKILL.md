---
name: urso-and-co-design
description: Use this skill to generate well-branded interfaces and assets for Urso & Co — the UK AI operations studio for £1–10M DTC brands — either for production or throwaway prototypes/mocks/decks. Contains the locked brand foundation (v1.5 — colour, type, voice, iconography), self-hosted brand fonts, the component copy bank (on-voice strings), the internal-IP Voice System framework used as a quality constraint, and a one-page holding-site UI kit.
user-invocable: true
---

Read `README.md` first. It is the manifest and the foundation version (currently **v1.5**) lives there.

Then, before writing any copy, read the three canonical inputs in `brand/`:

1. `brand/foundation-brief.md` — roll-up of the brand foundation, status READY, v1.5.
2. `brand/component-copy-bank.md` — on-voice strings for every component type. **Use these instead of generic SaaS placeholders.** Banned CTAs and banned section headers are listed; treat those as hard refuses. The *Copy review checklist* at the end of that file is the pre-ship gate.
3. `brand/voice-system-v1.md` — **internal IP.** The voice framework Urso & Co installs into clients. Use its 7 principles as a quality constraint on generated copy. Do not surface its mechanics (framework name, step numbers, Skill filenames, Fingerprint, calibration cadences, failure-mode taxonomy) in any public-facing output.

Then, depending on the task:

- **Visual taste call** — open `colors_and_type.css` (tokens) and the preview cards under `preview/` (swatches, type, components).
- **Voice / copy call** — `README.md` has the short-form content fundamentals; the full vocabulary (use-freely + refused) lives there too. Always cross-check against `brand/component-copy-bank.md`. Sentence fingerprint: 12–18 words, declarative, periodic, noun-first; one idea per paragraph.
- **UI work** — the holding site at `ui_kits/holding-site/` is the reference implementation. Its `site.css` shows how to layer brand-level work over the `colors_and_type.css` tokens. Nothing in that kit uses JS, shadows, gradients, or icons — by design.
- **Logos / marks** — `assets/` contains the outlined wordmark family (primary / lockup / stacked / monogram) and the favicon. Never substitute the typeface; never italicise anything except the ampersand; never place the mark inside a shape.
- **Fonts** — Source Serif 4 is self-hosted from `fonts/` as a variable TTF (`opsz` 8–60, `wght` 200–900). The tokens file wires it via `@font-face` and sets `font-variation-settings` per heading level.

## Hard rules before shipping anything

1. Never call Urso & Co an "AI agency." Studio, partner, or practice.
2. One ox-blood mark per asset. Default composition is Ink (`#0f1114`) on Bone (`#f6f2eb`).
3. Two typefaces per asset — Source Serif 4 and IBM Plex Sans. Mono only for data.
4. No gradients, no shadows, no emoji, no hashtags, no stock or AI imagery.
5. UK English throughout. `£` symbol before the number, no decimals on round figures. ISO dates in metadata.
6. **Locked hero tagline**: *"AI operations for DTC founders, by an ex-DTC founder."* Do not paraphrase on the hero surface. (Sub-taglines with "ex-DTC operator" language are fine in secondary positions — see the Copy Bank.)
7. Refused vocabulary (partial): transformation, synergy, unlock, seamless, leverage (verb), game-changer, cutting-edge, revolutionary, AI-powered. Full list in `README.md` + the `brand/` files.
8. **Never "Click here", "Learn more", "Get started", "Sign up", "Submit"** — the bank's banned CTAs. Replace with a specific action naming a specific outcome.

## Workflow

If creating visual artefacts (slides, mocks, throwaway prototypes), copy assets out of `assets/` and create static HTML files; the tokens import cleanly from `colors_and_type.css`. Pull every copy string from `brand/component-copy-bank.md` first; only hand-author new strings if the bank doesn't cover the surface, and when you do, run them through the bank's *Copy review checklist* before shipping.

If working on production code, read the handoff references cited in `README.md` → *Sources* to go deeper than the synthesis stored here.

If invoked without other guidance, ask the user what they're building — a page, a deck, an asset — then follow the rules above and the visual foundations in `README.md`.
