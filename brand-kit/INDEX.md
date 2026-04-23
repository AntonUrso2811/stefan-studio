# brand-kit / INDEX

Canonical jurisdiction for each document in `01-docs/`. When two docs appear to disagree, the **tiebreak order** below decides.

## Files and their jurisdictions

| File | Owns | Does NOT own |
|---|---|---|
| `foundation-brief.md` | Positioning, archetype, audience, commercial model, offer ladder strategy. Refused-vocabulary canonical list. | Specific shippable copy strings. Voice principles beyond one-sentence summary. |
| `component-copy-bank.md` | **Every on-voice string that ships.** Hero tagline (locked), CTAs, headlines, microcopy, banned-CTA list. | Strategy. Why strings exist. |
| `voice-system-v1.md` | Voice principles (7), method IP, how to generate novel copy on-voice. **Internal — do not expose mechanics in user-facing output.** | Specific strings. Positioning. |
| `README.md` | Metadata about this directory, build provenance. | Rules. |
| `SKILL.md` | `urso-and-co-design` skill entry point — how the design skill reads this kit. | Brand rules. |
| `CLAUDE-DESIGN-RE-PROMPT.md` | Operational re-upload manifest for Claude Design. | Brand rules. |

## Tiebreak order (when docs disagree)

1. **`component-copy-bank.md`** — for any copy string that ships on a surface.
2. **`voice-system-v1.md`** — for any voice principle or "how do I write this on-voice?" question.
3. **`foundation-brief.md`** — for any positioning, archetype, commercial, or refused-vocabulary question.

## Cross-repo pointers

- **Refused words + hero tagline + banned CTAs + hard visual rules (machine-readable):** `../project-rules.md` at repo root.
- **One ox-blood mark rule** — strategic intent in `foundation-brief.md`; enforced visually in `02-tokens/` + `05-preview/`.
- **Skills that consume this kit:** `../skills/copy-urso.md` (wraps `../skills/copy.md` + applies brand overlay).

## Versioning

This directory's content is versioned via `foundation-brief.md` frontmatter (`foundation_version`). When that version bumps, audit:

- `component-copy-bank.md` — add/retire strings as positioning shifts.
- `voice-system-v1.md` — adjust principles only if foundational vocabulary changed.
- `../skills/copy-urso.md` — bump skill `foundation_version` frontmatter to match.
- `../project-rules.md` — update version-coupling note; mirror any refused-word list change.
