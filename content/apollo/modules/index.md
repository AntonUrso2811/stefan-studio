# Apollo — Program Index

Men of Apollo is a 90+ day progressive programme delivered across four phases. Each phase unlocks at day thresholds (Phase 2 at Day 30, Phase 3 at Day 60, Phase 4 at Day 90) and deepens the work of the prior phase. The 20 modules below are the full content library.

## Phase architecture

```
Day 0  ──────┐
             │
             ▼
       ┌─────────────┐
       │ Onboarding  │   MOA_01 — Welcome: Start Here           tier: shared
       └──────┬──────┘
              │
              ▼
Day 0–30
       ┌─────────────────────────────┐
       │   Phase 1 — Foundation      │   tier: protocol
       ├─────────────────────────────┤
       │ MOA_02  Apollo Initiation   │
       │ MOA_03  Mental Architecture │
       │ MOA_04  Training System     │
       │ MOA_05  Nutrition Framework │
       │ MOA_06  Mobility System     │
       │ MOA_07  Recovery System     │
       └──────────┬──────────────────┘
                  │
                  ▼
Day 30–60
       ┌─────────────────────────────────┐
       │   Phase 2 — Integration         │   tier: community
       ├─────────────────────────────────┤
       │ MOA_08  Advanced Training       │
       │ MOA_09  Intermittent Fasting    │
       │ MOA_10  Nutrition Optimisation  │
       │ MOA_11  Recovery/Stress Mastery │
       │ MOA_12  Body Recomposition      │
       │ MOA_13  Phase 2 Integration     │
       └──────────┬──────────────────────┘
                  │
                  ▼
Day 60–90
       ┌─────────────────────────────────────────┐
       │   Phase 3 — Mastery                     │   tier: community
       ├─────────────────────────────────────────┤
       │ MOA_14  Phase 3 Overview                │
       │ MOA_15  Advanced Physical Optimisation  │
       │ MOA_16  Gut-Brain Axis                  │
       │ MOA_17  Training Specialisation         │
       │ MOA_18  Sleep & Circadian Mastery       │
       └──────────┬──────────────────────────────┘
                  │
                  ▼
Day 90+
       ┌─────────────────────────────────┐
       │   Phase 4 — Longevity           │   tier: community
       ├─────────────────────────────────┤
       │ MOA_19  Longevity Optimisation  │
       │ MOA_20  The Integrated Life     │
       └─────────────────────────────────┘
```

## Site IA recommendation

**Phased-unlock library.** The site renders four phase cards (plus Onboarding) in the members area. A phase card shows its modules once the member has reached the unlock day (auto-timed from signup). Revisit-anytime once unlocked. No forced linear consumption.

- **Members landing** — hero, "Start Here" CTA to MOA_01, phase map showing current progress
- **Phase card** — phase name, unlock status (locked / unlocking Day X / unlocked), list of modules with read status, phase-opener module featured
- **Module page** — lede, summary, content map (as navigable in-page anchors), frameworks as reproducible visual cards, full body, next-step CTA to the following module

## Tier mapping — Protocol vs Community

- **`tier: shared`** — MOA_01 Welcome. Both Protocol-tier (low-ticket) and Community-tier (high-ticket) members land here.
- **`tier: protocol`** — MOA_02–07 (Phase 1 Foundation). The universal entry. Low-ticket customers consume this.
- **`tier: community`** — MOA_08–20 (Phase 2–4). Advanced content gated behind Community membership.

## Full module table

| # | Title | Phase | Order | Tier | Lessons | Lede |
|---|---|---|---|---|---|---|
| 01 | Welcome — Start Here | Onboarding | 1 | shared | 7 | You made it. |
| 02 | Apollo Initiation | Phase 1 | 1 | protocol | 30 | The next 30 days are going to change you. |
| 03 | Mental Architecture | Phase 1 | 2 | protocol | 7 | Everything you have learned is worthless without the right mental architecture. |
| 04 | Apollo Training System | Phase 1 | 3 | protocol | 23 | This is not a powerlifting program. This is not a bodybuilding program either. |
| 05 | Apollo Nutrition Framework | Phase 1 | 4 | protocol | 14 | Forget everything the fitness industry has told you about eating. |
| 06 | Apollo Mobility System | Phase 1 | 5 | protocol | 7 | A strong man who cannot move well is not capable. |
| 07 | Apollo Recovery System | Phase 1 | 6 | protocol | 11 | You do not grow in the gym. You grow when you recover. |
| 08 | Advanced Training | Phase 2 | 1 | community | 60 | Now we sharpen the blade. |
| 09 | Intermittent Fasting Mastery | Phase 2 | 2 | community | 33 | You have heard about intermittent fasting. Some of it is true. |
| 10 | Nutrition Optimisation | Phase 2 | 3 | community | 37 | Phase 1 gave you the foundation. Now we add precision tools. |
| 11 | Recovery & Stress Mastery | Phase 2 | 4 | community | 48 | You will understand stress as a unified system. |
| 12 | Body Recomposition | Phase 2 | 5 | community | 31 | Body recomposition is the holy grail. |
| 13 | Phase 2 Integration | Phase 2 | 6 | community | 23 | You have the knowledge. Information without implementation is worthless. |
| 14 | Phase 3 Overview | Phase 3 | 1 | community | 1 | You have spent sixty days in the forge. |
| 15 | Advanced Physical Optimisation | Phase 3 | 2 | community | 34 | Phase 1 and Phase 2 built your body. This module refines how you inhabit it. |
| 16 | Gut-Brain Axis | Phase 3 | 3 | community | 19 | This is the module most fitness programs will never give you. |
| 17 | Training Specialisation | Phase 3 | 4 | community | 13 | It is time to specialise. |
| 18 | Sleep & Circadian Mastery | Phase 3 | 5 | community | 7 | You will not fight your biology. You will align with it. |
| 19 | Longevity Optimisation | Phase 4 | 1 | community | 8 | Most men optimise for the next 30 days. You are going to optimise for the next 30 years. |
| 20 | The Integrated Life | Phase 4 | 2 | community | 6 | How do you sustain this? Not for another 30 days. For the rest of your life. |

Total: **418 lessons across 20 modules.**

## Sequence dependencies

Every Phase 1 module depends on MOA_02 Apollo Initiation (the 30-day protocol that installs the foundation). Every Phase 2 module depends on completion of Phase 1. Every Phase 3 module depends on completion of Phase 2. Phase 4 depends on Phase 3.

Within each module, `dependencies: [slug, slug]` in the frontmatter captures the specific cross-references (e.g. MOA_11 Recovery/Stress Mastery depends on MOA_07 Recovery System; MOA_16 Gut-Brain Axis depends on MOA_05 Nutrition Framework + MOA_10 Nutrition Optimisation).

## Notes for Stefan to confirm during review

1. **Phase 3 module count.** MOA_14 (Phase 3 Overview) explicitly says "Four modules. Each one goes deep." MOA_15–18 are four modules, which matches. Proposed mapping: Phase 3 = MOA_14–18, Phase 4 = MOA_19–20. If you intended Phase 3 = MOA_14–20 (seven modules), say so and I'll re-tag MOA_19/20.

2. **Tier mapping.** Draft assumes Protocol-tier = Phase 1 fundamentals (MOA_02–07), Community-tier = everything from Phase 2 onwards. Confirm or specify different cuts (e.g. Phase 3 Mastery as its own super-tier, etc.).

3. **Lesson counts.** Pulled from each PDF's "Total Lessons: N" metadata. A few modules have large counts (MOA_02: 30, MOA_08: 60, MOA_11: 48) — these are the multi-week programme modules rather than single-read lessons.

4. **MOA_01 vs naming.** MOA_01's frontmatter phase is `onboarding` (not `phase-1`). It's intentionally outside the numbered phases — both tiers see it. If you want it under Phase 1, change phase in module-01-welcome.md and index.md.
