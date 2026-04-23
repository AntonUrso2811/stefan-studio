# ⚠️ TODO — STEFAN BRAND CONTENT NOT YET AUTHORED

This file was cloned from the urso-studio template. Replace the content below
with Stefan-specific brand material by running the /brand skill in Claude Code:

    /brand — Author foundation brief for Stefan

Until then, this file is INVALID and any tool that reads it must refuse.

Original Urso content is preserved below as reference structure only.

---


---
type: method
version: v1
status: current
generated_from: reverse-engineered 2026-04-22 from foundation/, outputs/, _context/, plus founder voice patterns observed across 2026-04-19 + 2026-04-22 sessions
last_edited: 2026-04-22
tags:
  - method
  - voice
  - copy
  - framework
  - internal
  - urso-co-ip
aliases:
  - Voice System
  - Urso & Co Voice System
  - VS-v1
  - Voice Framework
updated: 2026-04-22
---

# Voice System — Urso & Co Method Doc

> **Internal IP — version 1.** The framework Urso & Co uses to install voice-trained operations into client AI workflows. Reverse-engineered from the patterns visible across the brand foundation + observable founder behaviour. Anton reacts; v2 incorporates corrections.
>
> **Why this exists**: AI-generated content sounds identical across brands. Generic Claude / GPT output reads the same whether it's for a coffee subscription, a B2B SaaS, or a recruitment agency. The Voice System ensures every workflow output Urso & Co installs sounds like the *client's* brand — by construction at workflow-output time, not by manual polish pass after.

---

## What it is

A **5-step capture + apply system** for translating a brand's actual voice into a Cowork-installable Skill that runs at the workflow output layer. Per-client. Productised. Reusable across every workflow installed for that client.

It's not:

- A prompt template
- A "better way to talk to Claude"
- A copywriting service
- A creative agency offering
- An LLM fine-tune

It is:

- A diagnostic process (the Voice Fingerprint deliverable)
- A spec doc (the Fingerprint output)
- A composable Skill (`voice-calibration.md` per client workspace)
- An ongoing calibration cadence (monthly / weekly / quarterly per tier)

---

## Inputs the framework requires

Before any voice work happens, the audit collects:

1. **Brand corpus** — past brand-authored content
   - 3-month sample of marketing emails (Klaviyo / Mailchimp / Beehiiv)
   - 3 months of social posts (Instagram / LinkedIn / TikTok captions, NOT just published content — IG Stories voiceovers count)
   - Past customer-facing CX replies (Gorgias / Zendesk threads)
   - Existing brand guidelines if any
2. **Founder voice samples — RAW**
   - DMs they've sent (with sensitive content redacted)
   - Voice notes they've recorded (transcribed)
   - Off-cuff posts (not the polished ones)
   - Podcast transcripts where the founder spoke unscripted
   - **Critical**: marketing-polished content is *polluted input* — it produces a fingerprint of the brand's current voice, not the founder's actual voice. The Voice Sample Validator catches this (see § Failure modes).
3. **Customer voice samples — verbatim**
   - Trustpilot / G2 / Yotpo reviews (5-star for love language, 1-star for horror language)
   - Discovery / sales call transcripts (Fathom / Granola / Loom AI)
   - Support tickets that escalated (these are highest-signal)
   - Forum / Reddit / Facebook group posts where the brand or its category gets discussed
4. **Refused vocabulary list** — words and phrases the brand never uses, even if competitors do
5. **Owned vocabulary list** — words the brand uses freely, that signal the brand's specific operator stance
6. **Structural patterns** — sentence patterns the brand uses, sentence patterns it would never use

Inputs (1)–(3) are *evidence*; (4)–(6) are *constraints*. Both are required.

---

## Outputs the framework produces

**Per client engagement**:

1. **Voice Fingerprint** — the spec document. Audit deliverable. Living artefact (updated quarterly minimum). Lives at `<client-workspace>/context/brand-voice-spec.md`.
2. **`voice-calibration.md` Skill** — installed in the client's Cowork workspace. Composable with every other workflow Skill. Lives at `<client-workspace>/skills/voice-calibration.md`.
3. **Per-component copy strings** — for design system or applied template needs. Drawn from the [[../outputs/copy/component-copy-bank|component copy bank]] template, customised for the client's specific vocabulary.
4. **Calibration review reports** — monthly (Growth tier), weekly (Partner tier), quarterly (Voice System Install). Each report cites 3-5 output samples with on-voice / drift verdict + correction notes.

**Across the studio** (Urso & Co IP, not client-specific):

- This method doc itself (versioned `v1`, `v2`, `v3`...)
- Aggregate pattern library: rhythm signatures, common archetype mappings, refused-vocabulary baselines per vertical
- Voice Sample Validator heuristic (see § Failure modes)

---

## Mechanics — the 5-step capture phase

Runs during the audit (5-day sprint).

### Step 1 — Corpus collection (Audit Day 1–2)

Discovery conversation with founder + corpus extraction. Collect a minimum of:

- **5 brand emails** (3-month sample, varied: launch, transactional, win-back, founder voice)
- **5 founder posts/DMs** (raw, not marketing-polished — flag if all available samples are polished)
- **3 customer testimonials in their words** (Trustpilot, G2, recorded calls)
- **1 existing brand guideline doc** (or note its absence)
- **3 examples of "this isn't us" copy** — content the founder rejected and why

Capture in `<client-workspace>/context/corpus/`. Keep raw — no editing.

### Step 2 — Pattern extraction (Audit Day 2–3)

Run a structured analysis against the corpus. Outputs become the Voice Fingerprint draft:

- **Sentence length** — average, variance, max, min
- **Rhythm** — periodic vs flowing, declarative vs interrogative ratio
- **Voice** — active vs passive ratio (target: ≥85% active)
- **Vocabulary frequency** — top 50 most-used content words (excluding stop words)
- **Vocabulary absence** — generic-competitor words this brand avoids (helps surface refused list)
- **Sentence pattern library** — 5–10 templates the brand re-uses (e.g., *"X. Then Y."* / *"Your X is Y. We make it Z."*)
- **Banned vocabulary** — words this brand wouldn't be caught dead using

This step is currently manual + structured. v2 candidate: automate via a Python script that runs corpus analysis and emits a structured report.

### Step 3 — Voice Fingerprint draft (Audit Day 3–4)

Synthesise the patterns into a Voice Fingerprint document with the same 7+ sections as [[../foundation/brand-identity|brand-identity.md]] uses for Urso & Co itself:

- **Archetype** — Pearson 12, primary + optional secondary
- **Register** — named (e.g., "quietly authoritative operator")
- **Voice character** — the specific narrator (a person, not a role)
- **Cultural ancestors** — 3–5 named refs
- **Aspirational identity** — who the buyer becomes
- **Signature vocabulary** — 8–10 owned words
- **Refused vocabulary** — 8–10 banned words
- **Sentence fingerprint** — length / rhythm / structure with examples
- **Do/Don't worked examples** — minimum 5 pairs, drawn from the client's actual past content

Every field tagged `[INFERRED from corpus]` until the founder confirms. Provenance stays in the doc.

### Step 4 — Founder calibration call (Audit Day 4)

Walk the founder through the Voice Fingerprint draft. For each field, get explicit:

- **Y** — confirmed as written
- **E** — edit, here's what it should say
- **F** — flip, this is wrong, here's what it actually is

Document founder edits verbatim. Replace `[INFERRED]` with `[CONFIRMED YYYY-MM-DD]`.

**Critical**: this is not an interview. It's a reaction session. The framework does the work; the founder reacts. Faster, higher quality, captures founder taste without forcing founder to articulate from scratch (which most founders can't do well even when they have strong taste).

### Step 5 — voice-calibration Skill installation (Audit Day 5)

Translate the Voice Fingerprint into a Cowork-readable Skill at `<client-workspace>/skills/voice-calibration.md`.

The Skill structure:

```markdown
# voice-calibration — <client name>

When invoked by another Skill, enforce these rules on the draft output:

## 1. Vocabulary check
- Owned words (use freely): [list from Voice Fingerprint]
- Refused words (never use): [list from Voice Fingerprint]
- If draft contains any refused word → rewrite without it
- Reject draft if owned-word density < 15% of content words

## 2. Sentence fingerprint check
- Average length: [X] words (variance ±[Y])
- Reject draft if average sentence length is more than 30% off target
- Use one of these signature patterns where natural: [pattern list]
- Avoid these patterns: [pattern list]

## 3. Anchor check
- Every claim must be anchored to a specific number, tool, or named moment
- Reject draft if it makes any claim with no anchor

## 4. Restraint check
- If draft sounds like SaaS pitch / consultancy deck / wellness brand → rewrite
- If draft contains exclamation marks → remove
- If draft uses "we are passionate about" or equivalent → rewrite

## 5. Architecture check
- Use UK English (colour, organisation, behaviour) [or US if specified]
- £ symbol (or $) without decimals on round figures
- ISO dates internally; natural-language dates in user-facing copy

Output: voice-calibrated draft + a one-line explanation of each rule applied.
Human review required before any client-facing send.
```

The Skill becomes a function any other workflow Skill can compose with. Per-workflow output runs through it before reaching `deliverables/`.

---

## Mechanics — the application phase (steady-state)

When a client workflow generates copy:

1. The originating workflow Skill (e.g., `subscription-churn-recovery.md`) drafts the message based on its trigger (cohort signal, customer behaviour, etc.)
2. Before output, the workflow Skill **composes with `voice-calibration.md`**
3. voice-calibration runs the 5 checks above
4. Output ships to `<client-workspace>/deliverables/<date>-<workflow>.md` for human review
5. Human reviewer (Anton or VA) signs off; output sends via the workflow's normal channel (Klaviyo, Gorgias, Notion, email)

**The composition step is non-optional.** Workflow Skill templates are written so they cannot output without invoking voice-calibration. This is the design discipline that makes the system non-bypassable.

---

## Principles — the 7 rules

These are the load-bearing beliefs the framework runs on. If a workflow output violates any of these, voice-calibration rejects it.

1. **Specificity over abstraction** — every sentence names a specific number, tool, or moment. *"Your Gorgias queue is 340 tickets deep on Mondays"* beats *"Your CX process has bottlenecks."*
2. **Restraint is the aesthetic** — under-claim, let specifics do the work. The brand that shouts signals desperation; the brand that speaks quietly with precision signals competence.
3. **Operator voice over consultant voice** — *queue, margin, retention, install* over *synergy, KPI, transformation*. Operators trust operators.
4. **Founder DNA, not founder mimicry** — capture how they *think*, not their *accent*. The fingerprint distils patterns, not personality tics.
5. **Verbatim over paraphrase** — quote the buyer back to themselves whenever possible. The avatar's own words land harder than any agency copywriter's interpretation.
6. **No banned vocabulary, ever** — the refused list is absolute. One slip ships generic.
7. **Human-in-loop, always** — voice-trained output ships through human review before reaching named customers. Autonomy is a design choice per workflow with the client, never a default.

---

## Architecture — Cowork-native deployment

Per-client file tree (locked):

```
~/studio/<client-slug>/
├── CLAUDE.md                       # client objectives, escalation rules
├── skills/
│   ├── voice-calibration.md        # ← THE Voice System for THIS client
│   ├── cx-triage.md                # workflow Skill (composes with voice-calibration)
│   ├── churn-recovery.md           # workflow Skill (composes with voice-calibration)
│   ├── weekly-report.md            # workflow Skill (composes with voice-calibration)
│   └── monthly-roi-report.md       # workflow Skill (composes with voice-calibration)
├── context/
│   ├── brand-voice-spec.md         # the Voice Fingerprint output
│   ├── corpus/                     # source material, raw
│   │   ├── past-emails.md
│   │   ├── founder-posts.md
│   │   ├── customer-quotes.md
│   │   └── refused-list.md
│   └── customer-personas.md
└── deliverables/                   # workflow outputs land here, human-reviewed before send
```

**Per-client.** **Compounds.** The framework's outputs (Voice Fingerprint, voice-calibration Skill) belong to the client — they walk away with them at engagement end. The framework itself (this method doc, the 5-step capture procedure, the principles, the Voice Sample Validator) is Urso & Co IP — not licensed to clients, not productised publicly in v1 timeframe.

---

## Calibration cadence

Voice drifts as brands evolve. Calibration cadence is built into every retainer tier:

| Tier | Frequency | What gets reviewed |
|---|---|---|
| **Audit** (one-off) | Day 4 of audit | Initial Voice Fingerprint with founder reaction (Y/E/F) |
| **Starter retainer** | None built-in | One workflow only, voice spec stable for the engagement length |
| **Growth retainer** | 1× per month | Voice spec accuracy as brand evolves; 3–5 output samples reviewed; minor edits to Fingerprint approved |
| **Partner retainer** | 1× per week | Tighter calibration; output samples reviewed weekly; vocabulary list pruned and grown |
| **Voice System Install** (£19k) | Quarterly for 12 months | Re-calibration as client business changes; major Fingerprint revisions; v2 / v3 of the Skill |

**Drift signal**: if any calibration review flags >20% of sampled outputs as off-voice, schedule an immediate Fingerprint refresh, regardless of the next scheduled review.

---

## Failure modes — what goes wrong, what to do

### 1. Polished corpus problem
**Symptom**: founder provides only marketing-polished samples; Fingerprint captures the *current brand voice*, not the *founder's actual voice*.
**Fix**: insist on raw samples — DMs, voice notes, off-cuff IG Stories. Use the Voice Sample Validator (below) to flag polish.
**Voice Sample Validator heuristic**: scan each sample for these polish signals:
- CTAs (*"link in bio," "DM me," "sign up below"*)
- Hashtags (≥3 per sample)
- Emoji density >1 per 100 words
- AI-tell phrases (*"delve," "tapestry," "leverage," "harness"*)
- All sentences between 12–18 words (real speech varies wildly)
- *"In today's [X]"* or *"Whether you're X or Y"* constructions
- 5+ power words per 100 words (*"transform," "unlock," "discover," "proven"*)
If any 3+ signals fire on a sample → flag, request rawer alternative.

### 2. Drift over time
**Symptom**: brand voice evolves (new product launch, audience shift, founder maturation), Fingerprint goes stale.
**Fix**: calibration review cadence (above). Drift trigger at >20% off-voice samples.

### 3. Generic-fallback problem
**Symptom**: under load (high-volume CX day, peak holiday), Cowork may produce generic output if voice-calibration Skill isn't invoked correctly by the workflow Skill.
**Fix**: workflow Skill template requires voice-calibration composition as the *last* step before output. Composition is non-optional in the Skill structure.

### 4. Founder over-edit
**Symptom**: founder rewrites every output, defeating the system. Eventually the founder is doing the work the system was supposed to do.
**Fix**: weekly review where founder picks 3 examples to flag (not every output). Flagged examples feed Fingerprint refinements. Output ships without founder pre-approval after the first 30 days unless flagged.

### 5. Vocabulary inflation
**Symptom**: over time the refused list grows to 50+ words; the owned list grows to 30+; both lose enforcement teeth.
**Fix**: quarterly vocabulary prune. Hold each list to ~10 items. Demote rarely-flagged words to a secondary list (informational, not enforced).

### 6. Multi-brand portfolio
**Symptom**: client owns multiple brands (M&A, holding company, sub-brand structure). One Voice Fingerprint can't cover all.
**Fix**: one Fingerprint per brand. One Cowork workspace per brand. Workspace tree replicated. Pricing scales accordingly (each brand is a separate audit + retainer line).

### 7. Client team over-rides
**Symptom**: client's internal CX or marketing team rewrites Cowork output before send because they "have their own voice." Cowork output goes unused.
**Fix**: include client team in the Day 4 calibration call. Get their reactions captured in the Fingerprint. Make the framework theirs, not Urso & Co's imposition.

---

## What's documented now (v1) vs not yet

### v1 documents:

- The "what it is" framing
- Inputs / outputs / mechanics (capture + apply)
- The 7 principles
- Architecture (Cowork deployment per client)
- Calibration cadence per tier
- 7 failure modes + fixes

### v1 does NOT document yet (v2 candidates):

- **Specific prompt templates for each step.** Currently in Anton's head; v2 should specify the exact prompts the operator runs at each capture step.
- **Worked example showing the framework on a real corpus.** Stefan / Men of Apollo is the obvious candidate — when engagement permits publication and Stefan consents, write up his Voice Fingerprint as a worked-example case study.
- **Quantitative calibration metrics.** Currently the rules in voice-calibration.md are qualitative ("if draft sounds like SaaS pitch"). v2 should add measurable thresholds (% owned-vocabulary density, sentence-length variance ranges).
- **Edge cases** — multi-brand portfolios (covered briefly in Failure mode 6), brand voice transitions during M&A, client team handovers, founder departures.
- **Pricing rationale** — when to apply audit-only voice work vs full Voice System Install. Currently in [[../foundation/offer-brief|offer-brief.md]] but not cross-linked to the framework.
- **Quality benchmarks** — what "good" looks like when reviewing voice-trained output. Currently relies on Anton's taste; v2 should codify enough that a contractor or VA can apply the standard.

---

## Provenance

This v1 was reverse-engineered on **2026-04-22** from observable artefacts in the Urso & Co vault:

- [[../foundation/voice|voice-and-principles.md]] (in `_context/`) — vocabulary lists, sentence patterns, visual hierarchy
- [[../foundation/brand-identity|brand-identity.md]] — do/don't worked examples, sentence fingerprint, archetype, cultural ancestors
- [[../foundation/house-style|house-style.md]] — refused vocabulary, language conventions, scaffolding rules
- [[../foundation/founder-insight-interview|founder-insight-interview.md]] — Q6 (frictionless scale aspiration), Q7 (intuition-not-knowledge — kills "we'll teach you" register)
- [[../foundation/offer-brief|offer-brief.md]] — UMP/UMS statements about voice-trained ops, headline candidates demonstrating the patterns in action
- [[../outputs/copy/component-copy-bank|component-copy-bank.md]] — applied component-level copy showing the patterns at micro level
- Session conversation patterns (Anton's own voice in sessions on 2026-04-19 and 2026-04-22)
- The `/brand` skill's Voice Sample Validator heuristic (informed Failure mode 1's checklist)

**Not yet captured** (still in Anton's head, awaiting his correction):

- The exact step-by-step procedure he uses when applying the framework on a new client
- Specific prompt templates / Skill code that operationalise the framework in Cowork
- His criteria for picking which brand archetype fits which client (currently inferred from category)
- Edge case handling beyond the 7 failure modes documented

**Anton's review path**: read this v1, mark every section with one of:

- ✓ accurate, ship as-is
- ~ partially accurate, here's the correction
- ✗ wrong, here's what it actually is
- + missing, here's what to add

v2 incorporates corrections + adds the items in "v1 does NOT document yet."

---

## Public release status

**Private. Not for redistribution.** This framework is Urso & Co's IP. Reasoning captured in the project memory:

> *Anton owns timing decisions for public release of the Voice System framework. Pre-committed for first 90 days: no public Skill / SDK / API release. Framework lives as private Skills inside per-client Cowork workspaces, never on the Anthropic marketplace. Revisit month 9+ if delivery history supports it.*

When (and if) the framework moves to public release in month 9+:

- Productise as a Claude Skill on the Anthropic marketplace
- Companion documentation (this doc, with worked examples) becomes a paid asset or a free lead magnet
- Decision deferred — driven by delivery history, not present timeline

---

## Related

- [[../foundation/foundation-brief|Foundation Brief]] — workspace roll-up
- [[../foundation/brand-identity|Brand Identity]] — applied to Urso & Co itself
- [[../foundation/house-style|House Style]] — agency overlay
- [[../outputs/copy/component-copy-bank|Component Copy Bank]] — voice applied at component level
- [[../foundation/founder-insight-interview|Founder Insight Interview]] — Q6 / Q7 source for the framework's positioning
- [[../foundation/offer-brief|Offer Brief]] — commercial wrapper (Voice Fingerprint as audit deliverable, voice-calibration in retainers, Voice System Install £19k)
- [[../../_MOC/Brand|MOC — Brand]] — parent map of content
