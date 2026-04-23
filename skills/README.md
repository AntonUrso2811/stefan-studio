# skills/

Source of truth for all Urso agent skills. Edited here and nowhere else. Cowork and Claude Code consume via git-sync, symlink, or plugin install.

## Structure (Cowork-plugin format)

Each skill lives in its own folder with a `SKILL.md` entry point. This matches the agency-skills plugin pattern so Cowork's plugin installer can mount each skill cleanly.

```
skills/
├── copy/
│   └── SKILL.md              (universal craft skill)
├── copy-urso/
│   └── SKILL.md              (Urso brand overlay)
└── README.md                 (this file)
```

## Current skills

- **`copy/SKILL.md`** — universal craft skill. Copywriting and copy review pipeline. Brand-agnostic.
- **`copy-urso/SKILL.md`** — Urso & Co brand overlay. Wraps `/copy` with the brand foundation, Component Copy Bank, and Voice System quality checks. Depends on `copy/SKILL.md`.

## Rules

- **Do not edit skills anywhere else.** This directory is canonical. Downstream copies (Cowork plugin mounts, `~/.claude/skills/`, etc.) must sync from here.
- **No forks.** If a skill needs a variant, it gets its own folder — don't branch in place.

## Version policy

- Each skill's frontmatter `version` bumps on any material prompt change (new rules, new stages, changed behaviour). Non-material edits (typos, formatting) do not bump.
- `copy-urso/SKILL.md` carries a `foundation_version` field. It must match the current `foundation_version` of [../brand-kit/01-docs/foundation-brief.md](../brand-kit/01-docs/foundation-brief.md). If the foundation bumps, review `copy-urso/SKILL.md` and bump its `foundation_version` after reconciling.

## Consumption patterns

| Surface | How it loads the skill |
|---|---|
| Claude Code | Symlinks at `~/.claude/skills/<skill-name>/SKILL.md` → this repo's `skills/<skill-name>/SKILL.md`. Auto-pulled on SessionStart hook. |
| Cowork | Installed as a plugin from the `urso-studio` GitHub repo. Each skill folder is mounted as an invocable `/skill-name`. |
| Claude Design | Reads via Project-level GitHub connector. Uses skills as context for proposals; does not invoke them directly (Design can't execute skills). |

## Dependencies on brand-kit

`copy-urso/SKILL.md` references paths under `../brand-kit/01-docs/` (foundation-brief, component-copy-bank, voice-system-v1). For the skill to function correctly, the consuming surface must also have access to `brand-kit/`. Cowork plugin installs of the full `urso-studio` repo carry both; installs of `skills/` alone will fail the knowledge-read step.
