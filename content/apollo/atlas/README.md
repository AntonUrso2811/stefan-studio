# The Apollo Atlas

The scientific interlink layer for Men of Apollo. Cross-references every protocol, module, and framework piece to its underlying research and to the modern-day scientists who teach it.

**Status:** Phase 1 build (Session G) · 2026-04-27 · 24 seed entries, 4 scientist pages, 6 doctrine cards
**Source layer:** Founder Dossier `brand-kit/00-research/dossier-2026-04-25.md` · Foundation Brief `brand-kit/01-docs/foundation-brief.md` · Five Inputs framework on `/protocols`
**Consumer surface:** Lovable Members area at `https://preview--apollo-ascension-landing.lovable.app/members`

---

## What the Atlas is for

The site already cites studies inline (Leproult JAMA 2011, Wu Horm Metab Res 2011 on `/protocols`). The Atlas is what closes the credential void flagged in the Founder Dossier §8: a structured research interlink that lets every protocol claim be traced to a paper, a scientist, a doctrine line, and the Apollo modules it serves.

Three principles, locked:

1. **Voice first, citation second.** Every entry leads with Stefan's stance from the Dossier. The studies confirm. The studies do not authorise. Stefan's voice is the spine. Research is the rail.
2. **Plain English before technical.** Every entry has both. Technical lives next to plain language. A member who reads only the plain side gets the protocol. A member who reads both gets the mechanism.
3. **Two schemas, no others.** Every entry is `schema: pre` (Prompt → Response → Execution, for stimulus-based content) or `schema: ddd` (Doctrine → Default → Drift Check, for identity/system content). The Apollo Agent renders only these two shapes.

---

## Folder layout

```
content/apollo/atlas/
├── README.md                       # this file
├── index.yaml                      # master manifest — all entries, scientists, doctrine
├── entries/
│   ├── ce-001-cold-exposure-sympathetic.md   # 18 PRE entries
│   ├── ce-002-zone-2-mitochondrial-density.md
│   └── ce-NNN-*.md
│   └── dd-001-knowing-not-doing.md           # 6 DDD entries
│   └── dd-NNN-*.md
├── scientists/
│   ├── andrew-huberman.md
│   ├── peter-attia.md
│   ├── inigo-san-millan.md
│   └── susanna-soberg.md
└── doctrine/
    ├── d-01-knowing-not-doing.md             # 6 Dossier-pulled doctrine cards
    └── d-NN-*.md
```

---

## Entry frontmatter contract

Every entry uses this shape. Lovable consumes it via GitHub raw URL fetch (same pattern as the 20 module files).

```yaml
---
entry_id: ce-001                         # ce- for PRE, dd- for DDD
slug: cold-exposure-sympathetic          # URL slug
title: "Cold Exposure and Sympathetic Modulation"
schema: pre                              # pre | ddd
phase_relevance: [phase-1, phase-2, phase-3]
five_inputs: [calm-nervous-system, sleep] # which of the 5 Inputs this serves
mechanism_tags: [cold-exposure, sympathetic-tone, brown-adipose, recovery]
modules: [M07, M11, M18]                 # Apollo modules that use this
scientists: [andrew-huberman, susanna-soberg]
doctrine_refs: [d-02-effortless-not-extreme]
evidence_level: 3                        # 1-5
plain_english: "Short, brutal cold makes you alert and adapted. Done right, it bolts onto recovery, not training."
technical: "Vagal-tone modulation. β3-adrenoceptor activation. Mitochondrial biogenesis via PGC-1α."
prompt: "3 minutes, 11°C water, post-training, three to five times weekly."
response: "Catecholamine surge ~2.5x baseline. Brown adipose tissue activation. Vagal-tone shift on next-day HRV."
execution: "Apollo Recovery System (M07). Cold finisher. Track via Apollo Agent."
studies:
  - authors: "Søberg S, et al."
    year: 2021
    title: "Altered brown fat thermoregulation and enhanced cold-induced thermogenesis after deliberate cold exposure"
    venue: "Cell Reports Medicine"
    doi: "10.1016/j.xcrm.2021.100408"
    url: "https://www.cell.com/cell-reports-medicine/fulltext/S2666-3791(21)00302-7"
updated_at: 2026-04-27
---

## The Stance

(Pull from Founder Dossier or Foundation Brief — one sentence.)

## Plain English

(Two to four sentences. What it does, why a member should care.)

## Technical

(Two to four sentences. The mechanism, named.)

## The Studies

(Bulleted list of 1-3 studies in author-year-journal format. DOIs and URLs in frontmatter.)

## Linked Modules

(Bullet list mapping Apollo modules to specific protocols inside them.)

## Doctrine bridge

(One sentence. The Stefan-line this study confirms.)
```

---

## Voice rails (apply to every Atlas string)

Pulled from `foundation-brief.md` §5 Voice Principles, §6 Owned Vocabulary, §7 Refused Vocabulary. Hard rules:

**Owned vocabulary** (use freely): *protocol, blueprint, system, input, stack, framework, the five inputs, lean, simple, sustainable, effortless, structured, calm, lived-in, year-round, honest.*

**Refused vocabulary** (zero hits): *alpha, sigma, grind, beast, savage, warrior, spartan, conquer, TRT, peptides, macros, calorie deficit, IIFYM, motivation, hype, no excuses, brotherhood, tribe, transform, journey, unlock (verb), unleash, level up, game-changer.*

**Punctuation bans:** no em dashes (`—`), no semicolons, no mid-sentence colons, no exclamation marks on primary CTAs, no profanity, no caps-lock shouting.

**Citation register:**
- ✅ *"In ${journal} (${year}), ${authors} found that…"*
- ✅ *"${name}, ${role} at ${institution}…"* (institution lowercase per house style)
- ❌ *"Studies show…"* (banned — too generic)
- ❌ *"Experts say…"* (banned — authority crutch)
- ❌ *"Science says…"* (banned)

**Stance register:**
- ✅ *"Stefan's stance:"*
- ✅ *"What Apollo uses:"*
- ✅ *"What we don't echo:"*

The Stefan-Dossier line is the spine. Research is the rail. Science as confirmation, not crutch.

---

## Five Inputs taxonomy (top-level)

Every Atlas entry must tag at least one of the five `five_inputs` values. These are the spine of `/protocols` and pre-exist in customer-facing copy.

| Input | Tag | Description |
|---|---|---|
| 1 | `sleep` | Sleep architecture, duration, timing, temperature |
| 2 | `sunlight` | Circadian-light, melatonin onset, vitamin D |
| 3 | `heavy-compound-lifts` | Resistance training, strength, hypertrophy, neural drive |
| 4 | `real-food` | Whole-food nutrition, protein anchor, fibre, fasting |
| 5 | `calm-nervous-system` | HRV, vagal tone, cold exposure, breath, recovery |

Mechanism tags are secondary and may be invented per entry, but every entry must map cleanly to ≥1 Input.

---

## Schema selection rules

**Use `schema: pre` (Prompt → Response → Execution) when:**
- The entry teaches a deliberate stimulus the member applies
- A biological or cognitive cascade can be cited
- A daily-checkable Apollo protocol exists

**Use `schema: ddd` (Doctrine → Default → Drift Check) when:**
- The content is identity, framing, or system-level (M01, M03, M13, M14, M19, M20)
- There is no atomic stimulus
- The Apollo behaviour is "what flows when no decision is made," not "what to do today"

If you find yourself forcing a citation slot, switch the entry to DDD.

---

## Maintenance

Atlas content lives as `.md` and `.yaml` in this folder. Lovable fetches via GitHub raw URL on build. Editing this folder updates the live Atlas without touching Lovable.

Adding an entry: drop a new `.md` in `entries/`, append to `index.yaml`, push. The next Lovable rebuild picks it up.

Voice review: every new entry runs through the `foundation-brief.md` §10 quality checklist before merge.
