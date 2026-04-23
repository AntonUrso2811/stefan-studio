# Lovable prompt changelog

Version history for the Apollo integration prompts. **Never overwrite** — bump the version, log the reason here.

## session-a-module-load

### v2 — 2026-04-23 (current)
- **Word-for-word extraction.** Stefan confirmed the intent is verbatim module content — no editorial restructuring. Module files rebuilt to frontmatter + cleaned body only (stripped the `## Summary` / `## Content map` / `## Frameworks / protocols` / `## Visual callouts` / `## Full body` scaffold that v1 introduced).
- Session A prompt rewritten: Lovable renders each module body exactly as-is, with frontmatter driving card metadata, phase gating, and next-step CTA. Explicit "do not rewrite" constraints.
- Phase architecture corrected to four phases (Phase 3 = MOA_14–18, Phase 4 = MOA_19–20) per MOA_01's "Phase 4 at Day 90" reference.
- QA checklist v2 lead with a verbatim spot-check as the primary gate.

### v1 — 2026-04-23 (superseded)
- Initial release with `## Summary` / `## Content map` / `## Frameworks / protocols` / `## Visual callouts` / `## Full body` scaffold. Stefan's feedback: "literally implemented word-for-word, for the exact content to be extracted" — the editorial layer was unnecessary.
- Kept in repo history only; v2 supersedes.

## session-b-feedback-fixes

### v1 — 2026-04-23
- Initial release. Ships three fixes per Stefan's feedback (2026-04-23):
  1. Protocol lander "Who is this for?" rewrite — universal-entry copy, hard-ban on business/executive framing.
  2. Reviews consolidation — one universal section, 4–6 entries, product-siloed sections archived.
  3. Imagery regen — placeholder `{{IMAGE_MODEL}}` for Anton to insert; pilot-then-batch.
- Voice anchor: current live site (module bodies + founder passages). `/brand` skill deferred to post-ship.
- Driver: Anton, end-to-end.
