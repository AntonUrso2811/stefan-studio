# COWORK-INSTALL.md — installing the Urso & Co brand kit into Cowork

Operator doc. Short, reproducible, one-time setup. Re-read when bumping the kit version or handing the install to a contractor.

---

## What you're installing

The `brand-kit/` folder is the **source of truth** for everything Urso & Co publishes — visual system + copy + voice. Cowork skills read from it when generating on-brand assets. They never write back to it; the design bench (Claude Design or any git-tracked editor) is the only place source changes are made.

---

## What Cowork actually needs

Cowork does **not** need the whole kit. It needs five files, mounted stably:

| File | What Cowork uses it for |
|---|---|
| `01-docs/SKILL.md` | Agent entrypoint. Tells any skill *how* to use the rest. |
| `01-docs/foundation-brief.md` | Archetype, positioning, offer ladder, nine-check quality floor. |
| `01-docs/component-copy-bank.md` | On-voice strings for every component. Pre-ship copy gate. |
| `01-docs/voice-system-v1.md` | Internal IP. Quality constraint — never surfaced in output. |
| `02-tokens/colors_and_type.css` | Colour + type reference for any visual output. |

The rest of the kit (preview cards, fonts, logos, deck, holding site) stays in the design bench. Cowork is for **ops and copy generation**, not for rendering visual artefacts.

---

## Install steps

### 1. Upload the kit to Cowork knowledge

Drop the `brand-kit/` folder into Cowork's knowledge workspace. Exact mechanic depends on your Cowork setup — either:

- Upload the ZIP as a knowledge pack, or
- Sync a git remote into `/knowledge/` via Cowork's source connector, or
- Paste the five files above into Cowork's resources tab individually.

**Recommended mount path:** `/knowledge/urso-brand/`

Keep this path **stable**. Skills reference it. If it moves, every skill breaks.

### 2. Verify the universal `/copy` skill is available

This install assumes a universal `/copy` skill already exists in Cowork (Claude Code–built). The Urso overlay skill (`copy-urso.md`) delegates craft to `/copy`, then applies the brand filter.

Test it with any throwaway task:
> *"Write one sentence about a fictional coffee brand."*

If `/copy` returns a clean sentence, proceed. If not, fix the universal skill before installing the overlay.

### 3. Install the `copy-urso` skill

Copy `skills/copy-urso.md` into Cowork's skills directory. Naming convention depends on your setup — common patterns:

- `/skills/copy-urso.md`
- `/skills/brand/urso/copy.md`
- Registered via Cowork's skill manager UI under the name `copy-urso`

Whatever the convention, **keep it separate from `/copy`** — never merge or fork the universal skill. The two are deliberately distinct.

### 4. Verify the install

Run one test invocation:

> *"Draft a LinkedIn post announcing the £1,497 audit. UK DTC founders. ~150 words."*

Expected response shape:

- **Final copy** — a draft, ~150 words, uses bank CTAs and bank pricing language.
- **Trace log** — table showing which bank strings were used.
- **Queue for Copy Bank v2** — any novel strings the skill generated, flagged for human review.

If the response is missing the trace log or the queue, the skill prompt didn't load properly. Re-check paths.

### 5. Add other skills as they come

Future skills that depend on this kit (e.g. `/design-urso`, `/voice-audit`, `/proposal-urso`) follow the same pattern:

- Read the same foundation files.
- Produce traceable output with a changelog.
- Refuse tasks outside the offer ladder.
- Queue novel material for human review, never promote autonomously.

---

## Path-stability rule

Every skill references the kit via paths relative to its mount root. If you mounted at `/knowledge/urso-brand/`, the skill reads `/knowledge/urso-brand/01-docs/foundation-brief.md`.

**Never move the mount root.** If you absolutely must, update every skill that references it in the same commit. Grep for the old path; replace atomically; test all skills after.

A broken mount path is silent — the skill will generate plausible-sounding off-voice copy without flagging the error. Budget time to catch this every time you touch paths.

---

## Versioning discipline

The kit and the skills version together:

- `foundation_version: v1.5` → `copy-urso v1.0` expects this.
- Foundation bumps to v1.6 → re-run skill test suite, bump `copy-urso` to v1.1 if the foundation change affects output.

When you bump the kit, update:

1. `brand-kit/CHANGELOG.md` — what changed and why.
2. `brand-kit/01-docs/foundation-brief.md` frontmatter — `foundation_version`.
3. Every skill's frontmatter — confirm it still matches the kit version.
4. Re-test each skill with a canonical task (the test suite in each skill's docs).

If you skip step 3, skills silently diverge from the source. Within two version bumps, your Cowork output starts drifting off-voice and you can't easily diagnose why.

---

## What must NEVER leak into Cowork output

Three categories. Treat as hard-reject in every skill:

1. **Voice System mechanics** — framework names, step numbers, internal filenames. `voice-system-v1.md` is consumed as a quality filter only.
2. **Unpublished case studies** — any client name, metric, or engagement detail not explicitly cleared for public use.
3. **Refused category language** — never describe the studio as an "AI agency". Ever. The foundation refuses this category and every skill must enforce it.

If Cowork output ever surfaces any of these, it's a bug in the skill prompt, not a judgement call. Fix the skill.

---

## Handoff checklist (for contractors / future operators)

When handing this install to someone else, they need:

- [ ] Read access to `brand-kit/` in Cowork knowledge
- [ ] Read access to `/skills/copy-urso.md` (and any sibling brand skills)
- [ ] Ability to test-invoke the skills without production side-effects
- [ ] This file (`COWORK-INSTALL.md`)
- [ ] `brand-kit/CLAUDE-CODE-REVIEW-PROMPT.md` — for the periodic critical audit
- [ ] Understanding that **the source of truth lives in the design bench, not Cowork**. Cowork reads; it does not write.

Without that last point, the system drifts. With it, the system compounds.

---

## Troubleshooting

**Symptom:** Skill returns off-voice copy (consultant-slop, generic SaaS phrases).
**Fix:** Check path integrity. Skill can't find foundation files → falls back to universal `/copy` only → no brand overlay applied.

**Symptom:** Skill returns final copy but no trace log / queue.
**Fix:** Skill prompt is truncated or the output format section wasn't loaded. Re-paste the skill.

**Symptom:** Skill refuses every task with "outside the offer ladder".
**Fix:** Offer ladder in `foundation-brief.md` is stale or the ask needs clarification. Update the foundation *first*, then re-run.

**Symptom:** Skill surfaces Voice System framework names in output.
**Fix:** Urgent — hard bug in the skill prompt's Step 4 filter. Pull the skill from production until fixed.

**Symptom:** Novel strings queue grows every invocation, never drains.
**Fix:** Process gap, not a skill bug. Schedule weekly Copy Bank review sessions to promote good candidates into `component-copy-bank.md` v2.

---

## Version

v1.0 — 2026-04-22. Install doc for `brand-kit/` v1.5 + `copy-urso` v1.0.
