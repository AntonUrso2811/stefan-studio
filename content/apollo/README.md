# content/apollo

Source of truth for Stefan's **Apollo** course content — 20 modules across 4 phases, plus the Lovable handover package that publishes them.

## What's in here

```
content/apollo/
├── README.md                               # this file
├── modules/                                # 20 module markdown + program index
├── source-pdfs/                            # PDF originals + .txt extractions (inputs)
├── lovable/                                # Lovable handover package
│   ├── CHANGELOG.md                        # prompt version history
│   ├── session-a-module-load.v1.md         # Session A: 20-module load
│   ├── session-b-feedback-fixes.v1.md      # Session B: 3 feedback fixes
│   ├── qa-checklist-session-a.md
│   ├── qa-checklist-session-b.md
│   └── pre-integration-snapshot/           # pre-change state (rollback baseline)
└── scripts/
    └── extract-moa-pdfs.sh                 # PDF → .txt extractor (run once)
```

## Authoritative direction

- **Module content** → edit the markdown in `modules/`. Git is the source of truth. Lovable re-renders from here.
- **Lovable prompts** → edit versioned files (`session-X.vN.md`). Never overwrite — bump the version, log in `CHANGELOG.md`.
- **Pre-integration snapshot** → do not delete. Rollback baseline for imagery, reviews, lander copy.

## Phase architecture

| Phase | Modules | Tier |
|---|---|---|
| Onboarding | MOA_01 Welcome — Start Here | shared |
| Phase 1 — Foundation | MOA_02 Apollo Initiation · MOA_03 Mental Architecture · MOA_04 Training System · MOA_05 Nutrition Framework · MOA_06 Mobility System · MOA_07 Recovery System | protocol |
| Phase 2 — Integration | MOA_08 Advanced Training · MOA_09 IF Mastery · MOA_10 Nutrition Optimisation · MOA_11 Recovery/Stress Mastery · MOA_12 Body Recomposition · MOA_13 Phase 2 Integration | community |
| Phase 3 — Mastery | MOA_14 Phase 3 Overview · MOA_15 Advanced Physical Optimisation · MOA_16 Gut-Brain Axis · MOA_17 Training Specialisation · MOA_18 Sleep/Circadian Mastery · MOA_19 Longevity Optimisation · MOA_20 The Integrated Life | community |

See `modules/index.md` for the full IA + sequence logic.

## Running the extraction

One-shot after `brew install poppler`:
```bash
bash content/apollo/scripts/extract-moa-pdfs.sh
```
Copies the 20 MOA_NN PDFs from `~/Downloads/` (preferring `(2)` versions), runs `pdftotext -layout`, writes `.txt` alongside each `.pdf` in `source-pdfs/`.

## Status

- **2026-04-23** — content/apollo/ scaffolded; 20-module extraction + Lovable handover in flight. Pre-integration snapshot pending Anton's Lovable session.
