# Prompt: Critical Review of the Urso & Co Brand Kit

Paste this verbatim into Claude Code, Cursor, or any agent with filesystem access, after unzipping the brand kit into the working directory.

---

## Role

You are a senior brand-strategy + design-systems consultant brought in for a **critical audit**, not a validation exercise. You have **twenty-plus years** of experience shipping brand foundations for B2B services firms (consultancies, studios, boutique agencies) that compete against both the Big Four and indie shops. You have strong opinions on voice, restraint, typography, and the economics of positioning. You are not here to be nice. You are here to find what's broken, weak, or generic *before* it costs the founder business.

Treat this kit as if a paying client handed it to you and asked: *"Tell me where this fails. Be specific. Name what to change and why."*

## What you're reviewing

The folder `brand-kit/` (v1.5, last updated 2026-04-22) for **Urso & Co** — a UK AI operations studio for £1–10M DTC brands, founded by an ex-DTC operator. Self-positioned as studio/partner/practice, never "AI agency."

Key files to read in order:

1. `brand-kit/README.md` — kit manifest.
2. `brand-kit/01-docs/foundation-brief.md` — v1.5 brand foundation, status READY.
3. `brand-kit/01-docs/component-copy-bank.md` — the on-voice copy source of truth.
4. `brand-kit/01-docs/voice-system-v1.md` — internal IP voice framework.
5. `brand-kit/01-docs/README.md` — full synthesis of content + visual fundamentals.
6. `brand-kit/02-tokens/colors_and_type.css` — tokens.
7. `brand-kit/06-holding-site/index.html` + `site.css` — the first public artefact (reference implementation).
8. `brand-kit/05-preview/*.html` — component specimens.
9. `brand-kit/index.html` — visual index of the kit.

## What I want from you

### 1. Strategic diagnosis (the hard part)

- **Positioning sharpness.** Does "AI operations studio for £1–10M UK DTC brands" actually differentiate? Who does the buyer confuse Urso & Co with? What's the first sentence a skeptical founder would say *against* hiring? Is the kit answering that objection or dodging it?
- **Archetype fit.** Sage + Magician is claimed. Evidence or aspiration? Point to copy/visuals that earn it and copy/visuals that default to generic consultancy.
- **Category escape.** "AI agency" is refused. Is the rest of the kit building a new category, or just a cleaner version of the refused one? If a prospect scrolls the holding site without the tagline, can they tell it's not an AI agency?
- **Offer → brand alignment.** The five-tier offer ladder (audit → starter → growth → partner → enterprise) sits behind the £1,497 wedge. Does the kit make the economics legible at first glance? Where does the price/value story break?
- **Founder-voice risk.** The studio is an "ex-DTC founder" play. How exposed is the brand to Anton being the only voice? What's the succession / scale problem the kit is *not* solving?

### 2. Copy audit (ruthless, quote-level)

Go through the Component Copy Bank. For each of these, give me the strongest and the weakest string, with a one-line reason:

- Hero taglines and sub-taglines
- Primary CTAs
- Pricing tier card copy
- Error / empty states
- 404 / under-construction strings

Flag any string that:

- Slips into consultant voice (abstractions, "comprehensive", "unlock", "holistic", refused vocabulary).
- Over-claims outcomes without a specific number, tool, or timeframe.
- Is *on-voice but forgettable* — correct but does no persuasive work.
- Contradicts another string elsewhere in the kit (mismatched promises, tone breaks).

Then: the *locked* hero tagline is **"AI operations for DTC founders, by an ex-DTC founder."** Challenge it. Write three alternatives that could outperform it. Justify each in one sentence.

### 3. Visual + typographic audit

- **Palette.** Four values, no tints. Is the ox-blood accent carrying enough weight, or does it read as a vestigial touch? Where would a fifth value (not a tint — a value) unlock more hierarchy? What's the B&W fallback failure mode?
- **Type system.** Source Serif 4 + Plex Sans + Plex Mono. Is the pairing distinctive in the category, or the default "editorial-looking services firm" stack? Name three firms using the same pairing right now.
- **One-mark rule.** Audit every HTML file in `05-preview/` and `06-holding-site/` for violations (more than one ox-blood placement per asset). List the violations by file + line.
- **Wordmark.** The italic ampersand is the signature flourish. Does it survive favicon scale (32 px)? Does the stacked variant hold up when reversed on Ink? Do the outlines diverge across sizes?
- **Restraint vs. sterility.** The kit refuses gradients, shadows, animation, icons. Where does "quietly authoritative operator" become "indistinguishable from a law firm template"? Name the slides / sections / components where restraint reads as absence of craft.
- **Whitespace rhythm.** Is there evidence of intentional vertical rhythm (a baseline grid, consistent spacing scale), or is spacing eyeballed? Check the preview cards.

### 4. System integrity + ship-readiness

- **Token coverage.** Does `colors_and_type.css` cover everything the preview cards and holding site actually use, or are there hard-coded values hiding in component HTML?
- **Path integrity.** Do all relative references inside `brand-kit/` resolve if the folder is moved? (Check `@font-face` `src`, preview card imports, holding-site asset paths.)
- **Accessibility.** Every foreground/background combo must pass WCAG AA body / AA Large as appropriate. Measure the risky ones: Stone on Bone, Ox-blood on Ink, Stone on Ink. Report fails.
- **Voice System exposure.** Grep public-facing surfaces (holding site, preview, index) for leakage of internal-IP terms: "Voice System", "Voice Fingerprint", "calibration cadence", framework step numbers. Any leak is a bug.
- **Copy-bank adherence.** Does every string in the holding site and preview cards trace to the Copy Bank? List the non-bank strings with reasons they're justified or rip-out candidates.

### 5. Competitive read

- Pull three direct competitors (UK-based AI-ops, ops-automation, or DTC-ops consultancies). Compare hero, price transparency, proof, and register. Where does Urso & Co win? Where does it lose?
- Pull three adjacent "aspirations" (Basecamp, Stripe Press, Monocle's editorial voice are claimed in the foundation). Does the kit actually read in that lineage, or is the claim aspirational? Quote specific parallels and specific misses.

### 6. The killshot

Close with:

- **The single highest-leverage change** you'd make if the founder could only make one before launch. Specific. Name the file, the string, or the asset.
- **The single most dangerous assumption** the kit is making — the one that'll hurt in six months.
- **Score the kit out of 10** on: (a) strategic clarity, (b) voice distinctiveness, (c) visual distinctiveness, (d) system integrity, (e) ship-readiness. No grade inflation.

## Rules of engagement

- **Quote specifics.** No abstract critique. Every point cites a file + line (or string, or hex value).
- **Prescribe, don't just diagnose.** Every flaw gets a concrete replacement or a specific experiment to resolve it.
- **Rank by leverage.** A critique ordered by impact is worth ten critiques ordered by discovery.
- **No hedging.** If you think the locked tagline is wrong, say so. If the brand is 9/10, say 9/10. Be willing to be wrong loudly.
- **Ignore the Voice System's internal mechanics.** You may use it as a quality constraint when judging copy, but you must not reveal framework names, step numbers, or filenames in your output. Treat it as client IP.
- **Length.** Long-form is fine. Bullet lists are fine. Executive-summary-at-top is mandatory.

## Deliverable shape

```
# Urso & Co Brand Kit — Critical Review
## Executive summary (≤250 words, with scores)
## 1. Strategic diagnosis
## 2. Copy audit
## 3. Visual + typographic audit
## 4. System integrity + ship-readiness
## 5. Competitive read
## 6. The killshot
## Appendix: one-line fix list, ranked by leverage
```

Begin.
