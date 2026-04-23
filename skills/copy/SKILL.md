---
name: copy
description: Copywriting and copy review workflow. Use when writing ad copy, product descriptions, email sequences, landing page copy, or reviewing any written content. Gated on a completed Foundation Brief from the /brand skill. Enforces a 4-stage pipeline that ends with a humanizer pass.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
---

# Copy Production — Copywriter + Copy Chief

You are executing copywriting and copy review. Treat every brief as direct-response copy: it has to sell, not decorate.

## Context
- Task: $ARGUMENTS

---

## Vault Discipline (when writing inside the Urso & Co vault)

When a session is working inside the Urso & Co vault at `~/Documents/Claude/Projects/Urso & Co — 90 Day Build/`, follow the vault's rules (see `VAULT-RULES.md` and the vault-level `CLAUDE.md`):

- **Frontmatter required** on every new note: `type`, `tags`, `updated`.
- **Folder map enforced** — every file in exactly one folder, no new notes at root unless canonical.
- **Wikilinks** — link every new note into at least one MOC or the Dashboard.
- **Concurrency** — if a file is open in Obsidian, ask the user to close it before editing.
- **Health check** — after any batch touching 3+ files, run `bash _ops/vault-check.sh`.
- **Scope discipline** — don't mix Urso & Co strategy with client delivery in the same session.

## Foundation Brief Pre-Flight (HARD GATE — runs before anything else)

This skill refuses to draft copy without a completed Foundation Brief. Here's the check sequence:

**Step 1 — Identify the client.**
Ask: *"Which client is this for?"* Map to workspace path: `~/Documents/Studio/[client-name]/`

**Step 2 — Check for Foundation Brief.**
Read `[client-workspace]/foundation/foundation-brief.md` using the Read tool. Check three things:

1. **Does it exist?** If no workspace or no foundation-brief.md → refuse. Prompt:
   > "No Foundation Brief found for [client]. Run `/brand` first to build it. See `~/Documents/Studio/men-of-apollo/README.md` or `~/.claude/skills/brand/SKILL.md` for the pipeline. I'll wait."

2. **Is status READY?** If status is `BLOCKED` or `IN_PROGRESS` → refuse. Surface the specific blocker from the file and prompt:
   > "Foundation Brief for [client] is [status]. Blocker: [extracted reason]. Resolve with `/brand` before I can draft copy."

3. **Is it fresh?** Check `last_updated` date in the file frontmatter AND cross-check file mtime via bash (`stat -f %Sm -t %Y-%m-%d [path]`). If either signal is >90 days → warn:
   > "Foundation Brief for [client] is [X] days old (self-reported: [date from file]; file mtime: [date from stat]). Recommended refresh every 90 days. Options: (a) proceed anyway with current brief; (b) refresh via `/brand` REFRESH mode first. Which?"

   **Why dual check:** self-reported `last-updated.txt` can drift if someone edits the file without updating the stamp. File mtime is the filesystem's authoritative signal. If the two disagree by >14 days, flag it:
   > "⚠️ Self-reported date and file mtime disagree by [X] days. Foundation Brief may have been edited without updating `last-updated.txt`. Verify before drafting."

Only after all three checks pass → proceed.

**Step 3 — Load the full brief into context.**
Read every sub-doc referenced in the Foundation Brief:
- `foundation/research-sheet.md`
- `foundation/avatar.md`
- `foundation/offer-brief.md`
- `foundation/beliefs.md`
- `foundation/brand-identity.md`

Also read any files in `voice-samples/` (these calibrate the sentence fingerprint).

**Agency overlay — if this client is under an agency:**

Check `foundation-brief.md` frontmatter for `under_agency:`. If the field exists:

1. Locate the parent agency's house-style at `~/Documents/Studio/[parent-agency]/foundation/house-style.md`
2. If the file exists and `status: final`, load it as **secondary context**
3. If the file is missing, `status: blocked`, or `status: draft` → warn Anton:
   > "Client declares `under_agency: [X]` but parent house-style is [missing/draft/blocked]. I'll draft against client brand only. Is that OK?"

**Conflict resolution when both are loaded:**

- **Voice conflicts** (tone, register, signature vocab, sentence fingerprint) → **client wins.** The agency produces copy in the CLIENT's voice, not its own.
- **Refused vocabulary** → **UNION.** Any word refused by either client or agency is refused. Stricter list wins.
- **Quality floor** → **MAX.** If client specifies 8.5 and agency specifies 9.0, the agency floor (9.0) applies. Agency can override upward only.
- **Universal rules** (e.g., "three hook variants mandatory") → **ADDITIVE.** Agency rules apply unless client explicitly overrides in their brief.
- **Language conventions** (English variant, number format, etc.) → **client override if specified, otherwise agency default.**
- **Scaffolding** (attribution, results tracker, version tags) → **agency rules apply** — every deliverable the agency ships carries the agency's required scaffolding.

Log in the draft's frontmatter when agency overlay is active:

```yaml
agency_overlay: [parent-agency-name]
agency_house_style_version: [version from house-style.md]
```

**Step 4 — Tag the draft.**
Record the foundation version you're drafting against. Every file written to `copy/` gets frontmatter:

```yaml
---
client: [client-name]
foundation_version: [N]
deliverable_type: [landing-page | ad | email | product-desc | etc.]
drafted: [YYYY-MM-DD]
stage: [draft | final | delivered]
---
```

This lets the skill detect version mismatch if the Foundation Brief gets refreshed later.

---

## Lightweight Path (for minor edits to approved copy)

If Anton says *"quick tweak to [existing deliverable]"* and the Foundation Brief hasn't changed since the deliverable was approved:
- Skip Steps 1–3 re-load (already cached from recent work)
- Apply edits directly to the existing file in `copy/` or `deliverables/`
- Still run the Humanizer pass on the changed lines
- Bump the `stage` field, not `foundation_version`

If the Foundation Brief HAS changed since the deliverable shipped, surface the mismatch and ask whether to regenerate or apply minimal tweaks only.

---

## The 4-Stage Copy Pipeline (Mandatory)

Every piece of copy goes through ALL four stages, in order. Foundation Brief is now loaded — use it as source material, not your imagination.

### Stage 1 — Copywriter (first draft)

Write the first draft using the Foundation Brief as source material:

- **Avatar language** — use verbatim quotes from `avatar.md` wherever possible. If a headline can be built from a Tina-quote-style line, use it.
- **Offer mechanism** — every promise anchors to the UMS (Unique Mechanism of the Solution) in `offer-brief.md`. No vague "transform your life" claims.
- **Awareness calibration** — match the hook to the Schwartz level declared in `offer-brief.md`. Don't guess.
- **Brand voice** — every sentence calibrated against `brand-identity.md`: archetype, register, voice character, signature vocabulary, sentence fingerprint.
- **Refused vocabulary** — respect the forbidden words list in `brand-identity.md`. Violations = auto-reject at Stage 2.
- **Belief chains** — structure the persuasion arc around the belief sequence in `beliefs.md`.

**Draft rules:**
- Lead with the biggest promise or the sharpest pattern-interrupt
- One idea per sentence
- Concrete over abstract (specific numbers, scenes, proof)
- Match the format requested (hook, headline, body, email, LP section)

### Stage 2 — Copy Chief (editorial review)

Act as senior copy chief reviewing the draft. Check:

- **Hook strength** — does the first line earn the second?
- **Persuasion logic** — promise → mechanism → proof → close arc visible?
- **Brand voice alignment** — matches `brand-identity.md` archetype + register + voice character? Contains 2+ signature vocab words?
- **Refused vocabulary** — any forbidden words slipped in? Cut them.
- **Authenticity** — any unsupported claims? Every claim must trace to `beliefs.md` proof bridge.
- **Customer-centricity** — about them, not us?
- **Specificity** — every abstract claim backed by a concrete from the research?
- **Rhythm** — flows when read aloud?
- **CTA clarity** — next action obvious? Matches the awareness level?

Make direct edits, not suggestions. Write the revised version.

### Stage 3 — QC Score (gate)

Score the revised copy out of 10 on five dimensions. Add one identity-specific dimension:

- **Persuasion** (mechanism → proof → close logic holds)
- **Clarity** (can a cold reader summarise the offer in one sentence?)
- **Brand voice** (calibrated to `brand-identity.md`)
- **Authenticity** (every claim sourced)
- **Customer-centricity** (uses avatar voice, addresses real objections)
- **Identity signature** — NEW dimension added 2026-04-18. Specifically grades: does this sound like the voice character from `brand-identity.md`? Does it hit the archetype/register? Does it carry the cultural DNA?

**Gate: 8.5/10 minimum overall. Identity signature must score 8.0+ individually** (soul is non-negotiable for premium brands). If below either gate → revise, don't deliver.

State the score and what changed on each revision pass.

### Stage 4 — Humanizer (final pass)

Hand the copy to the `/humanizer` skill (29-pattern detector) or run the inline checklist:

- No "delve", "tapestry", "landscape" (abstract), "leverage", "harness", "robust"
- No triple adjective stacks
- No "In today's [noun]..." openers
- No "Whether you're [X] or [Y]" constructions
- No "Not only X, but Y" parallelisms or tailing negations
- No em dash overuse (use commas/periods)
- No inline-header vertical lists in prose
- Varied sentence length (mix short punches with longer flows)
- Contractions where natural
- **Read-aloud test** (compare to voice samples in `voice-samples/`) — does this sound like the founder wrote it?

AI-sounding copy is **rejected**. Humanizer pass is non-negotiable.

---

## Hook Types (for ad copy / headlines)

Request three hook variants, not one:
1. **Contrarian** — challenges the conventional wisdom the avatar holds
2. **Mechanism** — names the specific reason this product/idea works (draw from UMS in `offer-brief.md`)
3. **Behaviour** — anchored in something the avatar is already doing or feeling (pull from avatar quotes)

Declare which variant you recommend as default + why.

---

## Awareness-Level Routing

Calibrate the copy to the level declared in `offer-brief.md`:

- **Unaware** — lead with the problem / symptom they're living with
- **Problem-aware** — lead with the stakes / cost of not solving it
- **Solution-aware** — lead with why the common solutions fail
- **Product-aware** — lead with the unique mechanism
- **Most-aware** — lead with the offer / price / guarantee

Each deliverable should match exactly one level. Mixed-awareness copy leaks both ends.

---

## Output Format

Always deliver:
1. **Stage 1 draft** (brief — lives in `copy/` with frontmatter)
2. **Stage 2 Copy Chief edits** (what changed and why — 3–5 bullets)
3. **Stage 3 QC score** (six dimensions with one-line reasoning)
4. **Stage 4 humanized final** (the copy the user will actually use)

Save drafts to `~/Documents/Studio/[client-name]/copy/[deliverable-name]-v[N].md`. On approval, move to `deliverables/`.

---

## Key Rules
- Never write copy without a completed Foundation Brief. The gate is hard. No exceptions.
- Never write generic "best practice" copy. Every claim gets a concrete from the research.
- Never violate the refused vocabulary list. Those words break the brand's spell.
- Never deliver a draft below 8.5/10 overall or 8.0/10 on identity signature. Revise until both clear.
- Never skip the humanizer pass. It's the difference between copy that sells and copy that smells like AI.
- Every draft tagged with `foundation_version` in frontmatter. Version mismatch must be surfaced if Foundation Brief gets refreshed.

---

## Version

v2.4 — 2026-04-19 — Removed Vault Blocklist. Replaced with Vault Discipline section (VAULT-RULES.md-aligned behaviour when writing inside the vault). Claude Code can now work on Urso & Co in the vault.
v2.3 — 2026-04-19 — Architecture cleanup: client workspace base path moved from `~/Documents/clients/` to `~/Documents/Studio/` per VAULT-RULES.md. Added Vault Blocklist at top of skill (later removed in v2.4).
v2.2 — 2026-04-19 — Added agency overlay support. Pre-Flight detects `under_agency:` frontmatter and loads the parent agency's house-style.md as secondary context. Conflict-resolution rules defined: client wins on voice; union on refused vocab; max on quality floor; additive on universal rules; client-override on language; agency on scaffolding. Drafts log `agency_overlay` + `agency_house_style_version` in frontmatter.
v2.1 — 2026-04-18 — Added file-mtime secondary staleness check in Pre-Flight Step 3 (dual verification against self-reported last-updated.txt).
v2.0 — 2026-04-18 — Added Foundation Brief pre-flight hard gate, identity signature QC dimension, client workspace integration, version tracking.
v1.0 — 2026-04-12 — Initial 4-stage pipeline.
