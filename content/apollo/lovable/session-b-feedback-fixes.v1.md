# Lovable Session B — Stefan's three feedback fixes

**Paste this into Lovable as a single prompt.** Driver: Anton. Stefan reviews the finished state (live preview URL) after Session A + B complete.

---

## Context

You are editing Stef's Apollo site on Lovable. This session ships three fixes Stefan flagged. Do not change anything outside the scope listed below — no tokens, no type, no layout system, no components outside the three areas named.

**Voice anchor.** Match the current live site's body-copy voice — specifically the module bodies and founder-voice paragraphs. Those are the passages that work. Do NOT anchor on the current Protocol lander "Who is this for?" block or current review copy — those are the passages Stefan flagged as wrong. Emulate signals that work; reject signals flagged below.

**Output format.** After completing all three jobs, respond with:
1. Summary of every change, section-by-section.
2. Before/after snippet for Protocol lander "Who is this for?".
3. Reviews kept (list) + reviews archived (list).
4. Images regenerated (count + URLs).
5. Anything you couldn't complete + why.

---

## Job 1 — Protocol lander "Who is this for?" rewrite

**Current state (per Stefan):** the Protocol lander's "Who is this for?" block mirrors the Community lander's and implies business-people / executives. That's wrong — Protocol is the **low-ticket** entry. It should speak to anyone starting their Apollo journey.

**Action:** replace the current block with universal-entry copy. Draft anchors below (rewrite in the live site's voice, do not paste verbatim):

- Anyone ready to start — no prior training background needed.
- Men and women who want a structured way in, not another scattered plan.
- Anyone who's tried five programmes and wants one they actually finish.
- Anyone curious about the Apollo method before committing to the community.

**Hard negative constraint.** Do NOT reference executives, founders, high-performers, business-owners, entrepreneurs, or CEOs. Those terms belong only on the Community lander. Regression to the existing language = fail; ask for the Community-lander copy instead if you need a positioning reference for where that framing goes.

**Keep in scope:** the Protocol lander "Who is this for?" section only.
**Out of scope:** everything else on the Protocol lander. The Community lander's "Who is this for?" stays unchanged.

---

## Job 2 — Reviews consolidation

**Current state (per Stefan):** reviews are scattered across product sub-pages (nutrition, training, etc.), there are too many, and some read AI-written.

**Action:**

1. **Delete every per-product review section** (nutrition-page reviews, training-page reviews, any other product-siloed review block). Do NOT re-fragment — reviews live in ONE place from now on.

2. **Create a single universal reviews section.** Reuse it in:
   - Home page social-proof slot
   - Protocol lander social-proof slot
   - Community lander social-proof slot

3. **Keep 4–6 reviews total.** Selection criteria (pick reviews that meet ALL three):
   - **Specific detail** — names a behaviour, a result, a moment. Not generic praise.
   - **Human rhythm** — sentence lengths vary, some casual, occasional grammatical imperfection.
   - **Stef-adjacent voice** — reads like someone who actually followed the protocol. Real.

4. **Delete any review that:**
   - Opens with "I love…" or "I was blown away…"
   - Uses "transformative" / "journey" / "game-changer" without concrete context
   - Is three perfectly-balanced sentences of superlatives
   - Could be copy-pasted to any fitness product and still make sense

5. **Archive, do not hard-delete.** Move removed reviews into a draft/comment block inside Lovable so Stefan can restore any you cut. If Lovable has no archive primitive, paste them into a hidden/unpublished page called `/reviews-archive`.

6. **Final cut is Stefan's.** If a review is borderline, keep it — Stefan will prune. Bias toward preserve.

**Keep in scope:** all review sections across the site.
**Out of scope:** everything else on the pages you touch.

---

## Job 3 — Imagery regeneration

**Current state (per Stefan):** hero and module imagery looks off. Stefan wants a regen using the newest OpenAI image model (released 2026-04-21/22).

**Model to use:** `{{IMAGE_MODEL}}`

**If `{{IMAGE_MODEL}}` is not available in Lovable's image-generation picker: STOP this job. List the affected images and which surface they live on. Do NOT silently fall back to a prior model.**

**Pilot first, batch second.** The first regen pass is ONE hero image + ONE module card image only. Pause. Report back with URLs + prompt used. Do not touch any other imagery until the pilot is confirmed.

**Direction for the model:**
- Subject: lived-in physique/lifestyle photography. Real environments.
- Lighting: natural, soft, minimal styling.
- Tone: calm, confident, un-forced.
- Avoid: generic gym stock, AI-sheen, over-polished, "fitness hero" tropes, hyper-saturated colour grading, impossible-looking physiques.
- Reference: keep the aesthetic continuity with the current site direction that IS working (if any) — call out which current images we're preserving as reference.

**Aspect ratios (standard web):**
- Hero — 16:9
- Module card — 4:3
- Testimonial / avatar — 1:1

**Rollback baseline.** Current imagery has been archived at `content/apollo/lovable/pre-integration-snapshot/hero-imagery/` before this session started. One-line revert if the pilot misses.

**Keep in scope:** hero + module card + testimonial imagery.
**Out of scope:** logos, icons, diagrams, any illustrations that aren't photographic.

---

## Final output

After Jobs 1, 2, and 3 complete, respond with the five-point summary from the Context section. Flag anything you could not finish.

Deploy to preview (not production). Anton will QA against `content/apollo/lovable/qa-checklist-session-b.md` before handing the preview URL to Stefan.
