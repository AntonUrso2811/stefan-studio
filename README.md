# stefan-studio

Single source of truth for **Urso & Co** — the UK AI operations studio for £1–10M DTC brands.

## Layout

```
stefan-studio/
├── brand-kit/   # canonical brand foundation (v1.5.2) — docs, tokens, fonts, logos, preview, holding-site, deck
├── skills/      # canonical agent skills — copy (universal craft) + copy-urso (brand overlay)
└── site/        # placeholder for the production Astro site (future)
```

## Source-of-truth domains

- **`brand-kit/`** — the brand foundation. Edited here. Cowork and other downstream consumers sync from this directory.
- **`skills/`** — agent skill prompts. Edited here. Cowork and Claude Code consume via git-sync or symlink. See [skills/README.md](skills/README.md).

## Operations

The operations plan for this studio lives at [brand-kit/OPERATIONS-PLAN.md](brand-kit/OPERATIONS-PLAN.md).

## Versioning

- `brand-kit/` follows its own semver in [brand-kit/CHANGELOG.md](brand-kit/CHANGELOG.md).
- Each skill in `skills/` carries a `version` field in its frontmatter. `copy-urso.md` additionally carries a `foundation_version` that must match the current `brand-kit/01-docs/foundation-brief.md` version.

## Rules

- Skills and brand-kit are edited **here and nowhere else**.
- Never delete-and-recreate files. Edit in place — paths are permanent.
