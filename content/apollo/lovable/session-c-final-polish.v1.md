# Lovable Session C — Stefan's final polish pass

**Paste this into Lovable as a single prompt.** Driver: Anton. Stefan reviews the finished state (live preview URL) after Session C completes. Ships on top of Session A (20 modules loaded, verbatim body) + Session B (Protocol lander "Who is this for?" rewrite, reviews consolidation, imagery pilot).

---

## Context

You are editing Stef's Apollo's Ascent site on Lovable. This session ships four fixes Stefan flagged on 2026-04-24 after reviewing the Session A+B preview. Do not change anything outside the scope listed below — no tokens, no layout system, no components outside the four areas named. Session A's verbatim-body contract still holds: module prose sentences remain byte-identical to the source markdown. Session C adds **presentation** (typography, named section headings already injected into the source MD by Anton before this session, auto-TOC, scroll-progress), **reviews integrity** (de-named, de-AI'd, real customer submission), and **imagery resolution** (Higgs Field pilot OR full image removal).

**Voice anchor.** Match the current live site's body-copy voice — specifically the module bodies and founder-voice paragraphs. Those are the passages that work. Do NOT anchor on any current review copy — that's the passage Stefan flagged as wrong.

**Output format.** After completing all four jobs, respond with:
1. Summary of every change, section-by-section.
2. Typography spec applied (confirm token names / CSS variables touched).
3. Reviews kept (list, exactly 4) + reviews removed (list).
4. Higgs Field pilot: 1 hero URL + 1 module card URL, with the exact prompts used.
5. Review submission form: Supabase table name, admin route path, rate-limit config.
6. Anything you couldn't complete + why.

Deploy to preview (not production). Anton will QA against `qa-checklist-session-c.md` before handing the preview URL to Stefan.

---

## Job 1 — Module hierarchy + typography

**Current state (per Stefan, 2026-04-24):** modules render as walls of dense prose. Stefan's exact words: "the modules inside are just text with no subheader chapters as in school... its like a wikipedia page and the text is very small. needs more clarity and easier to read."

**What Anton has already done (before this session):** the 20 source markdown files at `content/apollo/modules/module-NN-*.md` have been updated with named h2/h3 structural headings derived from the existing prose. Body sentences are byte-identical — only heading lines have been added above paragraph groups. Your job here is the **render layer**: typography, auto-TOC, scroll-progress, mobile readability.

**Verbatim contract (still in force):** do not rewrite or paraphrase any module body text. If a module's content appears to disagree with anything in this prompt, the MD file wins.

### Typography spec (apply to module pages, then regression-check landers)

**Body text:**
- Mobile: 18px / 1.65 line-height
- Desktop: 19px / 1.7 line-height
- Measure: 66ch max-width on desktop, 92vw on mobile
- Paragraph spacing: 1.25em between paragraphs. No first-line indent.

**Headings:**
- **h1** (module title): 40/44 mobile, 56/60 desktop, letter-spacing −0.015em
- **h2**: 28/34 mobile, 32/40 desktop, 2.5em top margin, 0.75em bottom margin, hair-rule `border-top: 1px solid Stone` immediately above
- **h3**: 22/28 mobile, 24/30 desktop, 1.75em top margin, 0.5em bottom margin

**Frontmatter lede** (subtitle on module pages, if present): 22/30 mobile, 26/34 desktop, 400 weight, 70% opacity.

### Auto-generated Table of Contents (module pages only)
- Derive from h2 headings only (not h3).
- Desktop: render at top of module page, sticky in right-side margin below a viewport offset, or inline above the first h2 if no margin space.
- Mobile: collapsed sticky drawer, icon in top-right. Tap to expand. Auto-close on anchor tap.
- Active section highlighted as the user scrolls past each h2.

### Scroll-progress bar (module pages only)
- Hairline bar at the top of the viewport, `position: fixed`, 2px tall, Apollo accent colour. Fills left-to-right as the user scrolls the module body.
- Do NOT add this to landers or the home page.

### Mobile readability regression
- Check 320px, 375px, 414px widths. Body text must not compress below 18px.
- Stress-test against `module-10-nutrition-optimisation.md` (the largest module, ~5,568 words).
- Module pages on mobile must be thumb-navigable — TOC drawer reachable without stretching.

**Keep in scope:** module page template, type scale, TOC component, scroll-progress bar.
**Out of scope:** module content (already updated in source MD), lander type, navigation chrome, footer, auth flows.

---

## Job 2 — Reviews rewrite (de-named + de-AI'd)

**Current state (per Stefan, 2026-04-24):** existing reviews name specific people ("from within the collective") and mention specific things they're reviewing. The collective is empty right now — it's lifetime access, so any named reviewer who doesn't actually appear inside breaks trust when members join. Separately, the review copy reads AI-written (em dashes, balanced rhythm, AI vocabulary).

**Action.**

### Replace every review across the site with the 4-entry universal block below

Use exactly **4 reviews**, picked from the 8-entry pool in the next section. The same 4 reviews appear in the universal reviews block reused across home / Protocol lander / Community lander (one source, three placements — already wired from Session B Job 2).

### Rules for every review
- **Name format**: first name + last initial maximum ("James R."). Never full surnames. Never titles, roles, companies, industries, or any identifying detail.
- **Length**: 1–3 sentences. Hard cap 60 words.
- **Content**: generic positive signal only. Zero product specifics. Zero module / phase / framework names. Zero metric or result numbers. A review must be copy-paste-able to a different fitness product and still make sense — but each one should still sound like a different human voice.
- **Banned lexicon**: "journey", "transformative", "game-changer", "life-changing", "blown away", "next level", "took me to another level", "unreal", "mind-blowing".
- **Banned punctuation**: em dashes (—) across all reviews. No semicolons. No colons mid-sentence.
- **Banned structure**: rule-of-three ("X, Y, and Z"), balanced superlative trios, three perfectly-rhythmic sentences.
- **Rhythm requirements across the 4-entry set**: at least two reviews have a sentence ≤ 5 words; at least two run past 20 words. One grammatical imperfection across the set (dropped article, fragment) is welcome. Voices should feel distinct.

### Sample pool (pick any 4 — all pass the constraint set)

1. **James R.** — "Best decision I've made in a while. The structure just works for me. Felt different within a month."
2. **Liam K.** — "Clear, honest, no nonsense. I've stuck with this longer than anything else I've tried. That's the whole review."
3. **Tom H.** — "Finally something that doesn't treat me like I'm an idiot. Sustainable. I actually look forward to training now."
4. **Daniel P.** — "Took me a couple of weeks to trust it. Once I did, everything clicked. My head's in a better place too."
5. **Ben M.** — "No hype. Just the work. Exactly what I needed."
6. **Michael O.** — "I've tried a lot of programmes. This is the one I didn't quit. My wife's noticed."
7. **Alex T.** — "Honestly? I was sceptical. Reading Stef's stuff made me rethink a bunch of what I thought I knew."
8. **Harry S.** — "Doing the work. Feeling the difference. That's all I came here for."

### Remove, do not archive
- Any Session B review that referenced a named person from the collective, or that mentioned a specific module / phase / product — delete. (The Session B archive location still exists from the prior session if Stefan wants them back; no need to re-archive here.)
- Spot-grep the DOM for: full surnames, "module", "phase", "framework", "Apollo", and product-specific claims. All must be gone from the reviews block.

**Keep in scope:** the universal reviews block on home + Protocol lander + Community lander.
**Out of scope:** everything else on those pages.

---

## Job 3 — Imagery: Higgs Field regen OR remove (binary gate)

**Current state (per Stefan, 2026-04-24):** "the photos still look a bit off not fully there yet, if we cant make them look very real then we just remove it because it does more harm than good." The Session B placeholder `{{IMAGE_MODEL}}` is **superseded**. Stefan explicitly named **Higgs Field** (higgsfield.ai) as the image model for this session.

**Gate mechanic.** Generate **1 hero + 1 module card pilot**. Pause. Report the URLs + exact prompts used back to Anton. Stefan gives a binary pass/fail. If either misses, flip to **full image removal** (fallback below). No batch regen until Stefan says go.

### "Photoreal enough" criteria (Stefan's gate)
- Skin shows pores, micro-wrinkles, slight asymmetry.
- Eye catchlights are window-shaped, not ring-light donuts.
- Hair has stray strands; not every strand placed.
- Physique is lived-in (BF% roughly 12–18), not magazine-shredded.
- Environment has incidental imperfection (crumb on counter, uneven light, draped hoodie).
- Test: "Would Stefan mistake this for a friend's phone photo?" Yes = pass. "Nice render" = fail.

### Global positive DNA (prepend to every Higgs Field prompt)

> Documentary lifestyle photograph. Shot on Leica Q3, 28mm f/1.7, natural light only. Kodak Portra 400 film grain, slightly warm colour bias. Available light, no studio strobes, no fill flash. Slight motion blur acceptable. Candid asymmetric composition, subject not facing camera directly. Skin shows realistic texture — pores, faint sweat sheen, hair imperfection. Body proportions lived-in, natural body fat, not gym-photoshoot lean.

### Global negative prompt (append to every prompt, verbatim)

> plastic skin, airbrushed, porcelain skin, symmetrical face, perfect hair, perfect teeth, bodybuilder physique, oiled skin, shredded abs, vascular arms, ring-light catchlight, studio strobe, softbox lighting, seamless backdrop, stock photo, shutterstock, getty, cgi, 3d render, ai-generated, hyper-real, oversaturated, teal-and-orange, instagram filter, glossy magazine fitness, supplement ad, model pose, hand-on-hip, flexing, staring at camera, product placement, brand logo, watermark, text overlay, lens-flare sticker, bokeh background circles, perfect composition, rule-of-thirds overused, neon, glow, light leak added in post, hdr, beauty retouching

### Three paste-ready prompt templates

**Pilot pass uses Template 1 (hero) + Template 2 (module card) only.** Do not generate Template 3 or anything else until Stefan approves the pilot.

**Template 1 — Hero (16:9, export 1920×1080):**
> [global positive DNA] 28-year-old man in a worn navy cotton t-shirt sitting on a wooden bench at the edge of a small home kitchen, morning light from an east-facing window, steam rising from a black coffee on the counter behind him. He is mid-thought, looking down and left, not at camera. Slightly messy hair, two-day stubble, visible collarbone, lean but not shredded, soft waist, hands loose on his knees. Candid asymmetric framing, horizon slightly tilted, subject placed left of centre. Shallow depth of field but not blown out, some counter texture visible. [global negative prompt]. 16:9.

**Template 2 — Module card (4:3, export 1200×900):**
> [global positive DNA] Interior of a real independent gym, chalk dust on a rubber floor, mismatched weight plates on a rack, window light only, no ring lights. 32-year-old man mid-set of a trap-bar deadlift, focused on the floor two metres ahead, not the camera. Plain grey t-shirt slightly damp at the collar, practical training shorts, scuffed trainers. Real sweat, flushed face, slight grimace. Background partially out of focus but a second lifter visible doing their own thing. Ambient, unposed. [global negative prompt]. 4:3.

**Template 3 — Testimonial / avatar (1:1, export 800×800) — BATCH ONLY, after pilot approval:**
> [global positive DNA] Head and shoulders of a 35-year-old man in a park at golden hour, sitting on a low wall, slight turn of the head mid-conversation, eyes catching the low sun not the camera. Three-day beard, natural skin texture including a small scar near the eyebrow, hair moved slightly by wind. Plain knit jumper, no logos. Background soft trees, no sharp bokeh balls. Composition slightly off-centre. Natural depth of field, no beauty retouching. [global negative prompt]. 1:1.

### If Higgs Field is not available in Lovable's image picker
STOP. Do not silently fall back to a prior model. List the affected image slots + the prompts you would have used. Hand back to Anton — he will run Higgs Field externally and upload the approved assets.

### Fallback if the pilot fails (Stefan gate)
- Remove ALL photographic imagery across home + Protocol lander + Community lander + module pages.
- Replace each hero slot with a typography-on-whitespace treatment: single large Apollo headline, generous whitespace, one hair-rule, frontmatter lede as sub-headline.
- Module card images become typography cards (module title + frontmatter lede).
- Testimonial avatars become initials in a circle (first + last initial, matching the new review naming format).
- Log the fallback in the output summary. No follow-up Higgs work this cycle.

**Keep in scope:** hero + module card + testimonial imagery, and their typography-only fallbacks.
**Out of scope:** logos, icons, diagrams, non-photographic illustrations — untouched regardless of gate outcome.

---

## Job 4 — Customer review submission

**Action.** Add a review-submission form below the universal reviews block on home + Protocol lander + Community lander. Submissions are moderated — nothing publishes live.

### Form fields
- `name`: first name + last initial. Client-side regex enforced. Max 20 chars.
- `rating`: 1–5 stars.
- `review_text`: 250-character hard cap. Live counter visible below input.
- `email`: required, hidden from public display, used only for moderation follow-up.
- Honeypot field (hidden, any submission with this field filled is silently rejected).

### Supabase wiring
- Table: `review_submissions`
- Columns: `id` (uuid), `name` (text), `rating` (int), `review_text` (text), `email` (text), `status` (text, default `pending`), `submitted_at` (timestamptz, default now()), `ip_hash` (text, for rate limit), `approved_at` (timestamptz, nullable), `approved_by` (text, nullable)
- RLS: insert-only from public; select/update gated to admin role
- Edge function `rate-limit-review-submission`: 1 submission per `ip_hash` per 24h window. On duplicate, return 200 with a friendly "Thanks, we already got one from you recently." — do not leak rate-limit internals.

### Admin moderation route
- Path: `/admin/reviews`
- Auth gate: Stefan's email + Anton's email (Anton will paste his address separately — DO NOT hard-code any email in this prompt; ask if missing).
- Columns shown: name, rating, review_text, email, submitted_at.
- Actions: approve / reject.
- On approve: `status = approved`, `approved_at = now()`, `approved_by = <admin email>`. Auto-strip em dashes from `review_text` before surfacing. Approved reviews enter a separate `reviews_published` view that the universal reviews block reads.
- On reject: `status = rejected`. No publish.

### Placement on each lander
- Below the universal reviews block.
- Section heading: "Share your experience"
- Sub-copy: "Real reviews only. We read every one."
- Submit button uses the existing Apollo accent token — do not introduce a new primitive.

### Fallback if Supabase is unavailable or Lovable can't gate `/admin/reviews` cleanly
- Submit form writes to a Supabase table anyway.
- Admin route is skipped — instead, every new submission triggers an email to Stefan + Anton with the content + one-click approve/reject links (signed URLs).
- On approve, the edge function moves it into `reviews_published`.
- Log the fallback in the output summary.

**Keep in scope:** the form, the Supabase table + edge function + email fallback, the admin route (if clean), placement on the three landers.
**Out of scope:** redesign of the existing universal reviews block, new auth system, user accounts.

---

## Final output

After Jobs 1–4 complete, respond with the six-point summary from the Context section. Flag anything you could not finish. Include deploy-preview URL at the top of the response.

Deploy to preview (not production). Anton will QA against `content/apollo/lovable/qa-checklist-session-c.md` before handing the preview URL to Stefan.
