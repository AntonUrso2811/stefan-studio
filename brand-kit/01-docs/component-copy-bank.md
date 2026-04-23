# ⚠️ TODO — STEFAN BRAND CONTENT NOT YET AUTHORED

This file was cloned from the urso-studio template. Replace the content below
with Stefan-specific brand material by running the /brand skill in Claude Code:

    /brand — Author foundation brief for Stefan

Until then, this file is INVALID and any tool that reads it must refuse.

Original Urso content is preserved below as reference structure only.

---


---
type: brand
status: current
version: v1
generated_from: brand-identity.md + house-style.md + offer-brief.md + avatar.md + voice-and-principles.md
last_edited: 2026-04-22
tags:
  - brand
  - copy
  - components
  - design-system
  - kit
aliases:
  - Component Copy Bank
  - Copy Bank
  - Design System Copy
updated: 2026-04-22
---

# Component Copy Bank — Urso & Co

> Sample copy for design system components and applied templates. Every string here is on-voice — drop into Claude Design / Figma / Cowork-generated UI without modification. Closes the gap between brand voice principles ([[brand-identity]], [[house-style]]) and component-level copy where generators default to generic SaaS strings.
>
> **Use this when**: feeding any design system generator, populating component templates, scaffolding a marketing site, or briefing a contractor on copy.

---

## Buttons / CTAs

### Primary CTAs (one per asset, pick one)

- **"Book a 20-minute discovery call"** — default for hero / footer
- **"Book the audit — £1,497"** — for the offer-aware buyer (post-discovery)
- **"Send a one-line brief"** — softer entry, for cold audiences
- **"See the audit deliverables"** — when the question is "what do I get"

### Secondary CTAs

- "Read the case study"
- "Download the brief (PDF)"
- "See the workflow live"
- "Walk me through the install"

### Tertiary / inline

- "Or email studio@ursoandco.co.uk"
- "Skip to tiers"
- "What's an audit?" (inline glossary link)

### Banned CTAs (don't generate)

- ❌ "Click here", "Learn more", "Find out more"
- ❌ "Get started" (generic; replace with the specific action)
- ❌ "Sign up", "Subscribe" (no signups; bookings only)
- ❌ "Submit" (label the action: "Send brief", "Book call")

---

## Section headers

### Hero (above the fold)

- **Tagline (locked)**: *"AI operations for DTC founders, by an ex-DTC founder."*
- **Sub-tagline alternates**:
  - "I ran a pair of gourmet salt DTC brands to multiple seven figures. Now I install the ops infrastructure I wish I'd had."
  - "AI operations studio for £1–10M UK DTC brands. Five-day audits. Voice-trained installs. UK-based."

### What we do / install

- "What we install"
- "Three workflows. Five days. Working systems."
- "The ops layer your intuition deserves"
- "Voice-trained operations, installed in your stack"

### How we work

- "How an audit runs"
- "Five days, fixed price, working PoC at the end"
- "From cold call to retainer in 14 days"

### Pricing / tiers

- "Tiers"
- "Audit. Then four ways to retain us."
- "What £1,497 actually buys"

### Selected work / case studies

- "Selected work"
- "What we've shipped"
- "Case studies — by the workflow installed, not the vertical"

### About / founder

- "About Urso & Co"
- "Why this studio exists"
- "I ran a brand for 3.5 years. Here's what I install now."

### Compliance / footer

- *"UK-based · GDPR, PECR, EU AI Act posture from day one."*
- *"Urso & Co Ltd · Companies House #16980197 · ICO registered"*

### Banned section headers

- ❌ "Welcome to Urso & Co" (welcome copy is for products, not consultancies)
- ❌ "Our team" (single founder; use "About" or skip)
- ❌ "Transform your operations" (banned verb)
- ❌ "Unlock your potential" (banned verb)
- ❌ "Our services" (consultancy-generic; name the specific offer)
- ❌ "Why choose us" (positioning-defensive register)

---

## Status pills / badges

Short, all-caps in IBM Plex Sans Medium, Stone or Ox-blood depending on context.

- **AVAILABLE NOW** — tiers with capacity (Stone)
- **WAITLIST** — tiers at capacity (Ox-blood, the one-mark)
- **AUDIT-FIRST** — retainers requiring prior audit (Stone)
- **FROM AUDIT #3** — Voice System Install unlock condition (Stone)
- **NEW** — for genuinely new content; sparingly (Stone)
- **DRAFT** — work in progress, never on public surfaces (Stone, internal only)

---

## Tooltips / inline microcopy

- on **£1,497**: *"Fixed-price 5-day audit. No discovery-dependent pricing. No deferred terms."*
- on **"voice-trained"**: *"Every workflow output composes through your brand voice spec. Generic AI output never ships."*
- on **"GoCardless"**: *"UK B2B Direct Debit. ~£4 max collection cost per invoice. Capped fee."*
- on **"MSA"**: *"Master Services Agreement. 3-month minimum, 30-day rolling notice."*
- on **"DPA"**: *"Data Processing Addendum. Signed at retainer kick-off, scoped to the workflows installed."*
- on **"Cowork workspace"**: *"Per-client Claude workspace with installed Skills + voice context. Yours; lives on your stack."*
- on **"Voice Fingerprint"**: *"Diagnostic deliverable from the audit. Brand voice spec doc that powers every workflow output."*

---

## Form labels (sparse — Cal.com handles bookings)

If a discovery form ever ships:

- "Brand name"
- "Annual revenue band" (radio: <£500k / £500k–£1M / £1M–£3M / £3M–£10M / >£10M)
- "Team size" (radio: 1–5 / 6–20 / 21+)
- "Top one operational pain right now" (textarea, 1 sentence)
- "Best email"
- *Submit button*: **"Send brief"** (never "Submit")

Form helper text:

- *"60 seconds. No newsletter. Reply within one working day."*

---

## Card copy templates

### Case study card — ICP variant

```
[Anonymised brand name or named with consent]
"Recovered 14% of subscription LTV in 60 days"

Installed: subscription churn recovery workflow. Voice-trained
Klaviyo flows. Cancel-reason capture. Founder-time reclaimed:
6 hours/week.

Metric badge (large, ox-blood): +14% LTV
Footer: 90 days · Growth tier · UK skincare brand · £3M revenue
```

### Case study card — Adjacent variant

```
[Named with written consent — e.g., Men of Apollo]
"Installed the program backend for a 500k-follower coaching platform"

Voice-trained content layer + high-ticket program operations
infrastructure. Backend systems live in the client's stack.

Metric badge (large, ox-blood): backend ops live
Footer: ongoing · Partner tier · Creator + high-ticket coaching
```

### Pricing tier card

```
Tier name (h3): Audit
Price (large display, ox-blood — the one-mark): £1,497
Frequency line (small): one-time, fixed

Description (3 lines max):
5-day sprint. Ops map, working proof-of-concept, Voice Fingerprint,
90-day roadmap. Delivered before any retainer is proposed.

CTA: Book the audit — £1,497
```

### Pricing tier card — retainer

```
Tier name (h3): Growth
Price: £2,997
Frequency: per month
Footer: 3-month minimum · 30-day rolling notice

Description:
2–3 installed workflows. Weekly Loom. Bi-weekly strategy calls.
Cowork workspace + Skills library. Voice spec applied across
workflows + monthly calibration review.

CTA: See what's included
```

### ROI report card (monthly retention asset)

```
Header: Month [N] — [Client name]
Sub-header: [Date range]

Three metrics blocks (each with one large number in ox-blood,
when present — but ONLY one block ox-blood per card):
- Hours reclaimed: [n]
- Revenue influenced: £[n]
- Costs avoided: £[n]

One-line founder quote (italic, indented):
"[Client's verbatim feedback, with permission]"

Footer: Workflows in production · Next month focus · Scope check
```

---

## Empty states (when product UI emerges)

For a future internal client portal or admin UI:

- "No workflows installed yet — start with the audit."
- "No retainer active — book a discovery call."
- "Voice System Install unlocks after audit #3."
- "No reports for this month yet — your next ROI report ships day 25."

---

## Error / alert copy

- **Generic error**: *"Something broke. Email studio@ursoandco.co.uk and we'll sort it within one working day."*
- **404**: *"That page doesn't exist. [Back to home](/) or [book a call](/discovery)."*
- **Form validation**: *"[Field] is required."* (no exclamation marks; no "oops")
- **Booking confirmation**: *"Confirmed. You'll get a calendar invite from studio@ursoandco.co.uk within 5 minutes. If it doesn't arrive, check spam, then email me."*

---

## Sample lorem / placeholder copy (for design system templates)

When a design system needs placeholder body text in a Source Serif 4 / Plex Sans component, use ON-VOICE strings instead of lorem ipsum:

### Short (for card descriptions, ~20 words)

> The ops layer your intuition deserves. Voice-trained workflows installed in five days, run from your Cowork workspace.

### Medium (for hero sub-taglines, ~40 words)

> AI operations studio for £1–10M UK DTC brands. Founded by an ex-DTC operator who scaled a pair of gourmet salt brands to multiple seven figures across UK and US. We install the ops infrastructure your team actually adopts.

### Long (for about / explainer sections, ~80 words)

> Most AI agencies sell tools. We sell the operator judgement that makes the tools work in a real DTC business. The audit produces an ops map, a working proof-of-concept, a voice fingerprint, and a 90-day roadmap. Five days, £1,497, fixed price. Retainers cover voice-trained content inside installed workflows. Standalone projects price separately. UK-based. GDPR, PECR, and EU AI Act posture from day one.

---

## Copy review checklist (use against any generated component output)

Before any component copy ships:

- [ ] No banned vocabulary (agency, transformation, synergy, unlock, seamless, leverage-as-verb, game-changer, cutting-edge, revolutionary, AI-powered)
- [ ] No banned CTAs (Click here, Learn more, Get started, Sign up)
- [ ] CTAs name a specific action with a specific outcome
- [ ] Section headers carry specific nouns (not vague gerunds like "Innovating Together")
- [ ] UK English (colour, organisation, behaviour) — not US
- [ ] £ symbol, no decimals on round figures (£1,497 not £1,497.00)
- [ ] Numbers preserved as-shipped (60,000+ units, not "many thousands")
- [ ] One ox-blood mark per component — usually a price or a single inline link
- [ ] No exclamation marks
- [ ] No emojis (unless explicitly user-requested for a specific surface — never in brand assets)
- [ ] No hashtags
- [ ] No "AI agency" — always "AI operations studio / partner / practice"

---

## Voice register quick check

Read the generated copy aloud. If it sounds like:

| Sound | Verdict |
|---|---|
| A peer DTC founder explaining what they do at a dinner table | ✓ on voice |
| A senior operator briefing their team on a Monday | ✓ on voice |
| A McKinsey deck cover | ✗ rewrite |
| A Skool-graduate Loom thumbnail | ✗ rewrite |
| A SaaS landing page from 2022 | ✗ rewrite |
| A wellness brand on Instagram | ✗ rewrite |
| A law firm letterhead from 1980 | ✗ rewrite (too stiff — we're modern) |

---

## How to use this with Claude Design specifically

Two paths:

### A — If Claude Design is still in input phase

Paste this entire file's contents into the **"Any other notes?"** field, OR upload `component-copy-bank.md` via the assets uploader. The generator now has explicit string examples for buttons, headers, microcopy, and cards — drift risk drops dramatically.

### B — If Claude Design has already generated output

Review the generated design system pass-by-pass against this bank. For every component with sample copy:

1. Is the CTA on the bank? If not, replace.
2. Is the section header on the bank? If not, replace.
3. Is the tooltip / microcopy on-voice? If not, replace from this bank.
4. If this bank doesn't have the specific string needed, *generate it on-voice* using the principles in [[brand-identity#Voice character]] — then add it back to this bank for v2.

---

## Updates / v2 candidates

This is v1 — covers the obvious component categories. Add to this bank as new component types emerge:

- Onboarding tour copy (when the holding site grows into a richer site)
- Email sequence subject lines + preheaders (when outbound starts week 4)
- LinkedIn post hook variants (built-in-public posts, when case studies land)
- Slack response templates (for retained client communications)
- ROI report narrative paragraphs (for the monthly client deliverable)

Each v2 update bumps the version number and gets a CHANGELOG line.

---

## Related

- [[brand-identity]] — Phase 5 (voice principles, sentence fingerprint, signature/refused vocabulary)
- [[house-style]] — agency overlay (refused vocabulary list, scaffolding conventions, language conventions)
- [[offer-brief]] — Phase 3 (locked tagline, headline candidates, hook variants)
- [[avatar]] — Phase 2 (verbatim avatar voice anchor)
- [[urso-brand-handoff/_context/voice-and-principles|Voice & Principles]] — source brief
- [[foundation-brief]] — roll-up
- [[_MOC/Brand]] — parent map of content
