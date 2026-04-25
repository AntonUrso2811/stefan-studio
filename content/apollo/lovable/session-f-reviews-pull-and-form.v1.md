# Lovable Session F — Reviews Block Pull + Customer Submission Form

**Paste this into Lovable as a single prompt.** Driver: Anton. Stefan delegated direction (2026-04-25 — *"as long as it desires the best outcome"*). Anton signs off on the audit-trail outputs. Stefan async-reviews the live preview before production publish. Ships on top of Session A (20 modules), Session B (feedback fixes), Session C (final polish + S-C/Job2 reviews-de-AI'd lock), Session D v1.1 (conversion polish), and Session E (proof-block reset).

---

## Context

The 2026-04-25 reviews audit (`/Users/antonurso/Downloads/audit_results.csv`, 251 rows) found **zero rows scoring `LIKELY_REAL` or `PROBABLY_REAL`** — the entire upstream review pool is copywriter-assembled. Smoking-gun signals:

- 26 different reviewers say *"I'll keep this on the shelf for years"*
- 23 each independently say *"Two cycles of bulking and cutting got me back to the start"*
- 22 converge on the brand's own *"The page reads like the man writes. That's rare."*
- Stefan's anaphoric-No fingerprint (*"No needles. No pharmacy. No subscription. Just the inputs."*) appears verbatim in 13 customer mouths
- 78% 5-star, zero 1–2-star — probabilistically impossible for real customer data

Even after a tiered brand-compliant cleanup (Session F predecessor work, `reviews_cleaned.csv` saved to Anton's Downloads) that produced 235 acceptable rows, every cleaned row remains *brand-compliant copywriter-assembled*, not real customer voice.

**Session F decision (Anton + Stefan, 2026-04-25):**

1. **Pull the manufactured Reviews block** from home + /protocols.
2. **Keep the "What Men Write Back" YouTube-comments block** (real, sourced unedited from Stefan's actual YouTube comments per foundation-brief §4) — that block remains as social proof.
3. **Activate the Session C v1 Job 4 customer review submission form** (deferred since 2026-04-23) so real moderated reviews can accumulate.
4. **Re-launch the Reviews block when 6+ moderated real submissions exist** (target: within 90 days of launch).

**Why this is the brand decision, not a regression.** The brand's strongest line is *"This is not for everyone."* That positioning is incompatible with manufactured testimonials. Pulling the block until real reviews exist *is* the on-voice move. It also closes the only material legal/reputational exposure on the site (testimonial-fraud surface area).

---

## Pre-flight gates

| # | Gate | Status | Evidence |
|---|---|---|---|
| 1 | 2026-04-25 audit run on full 251-row pool | PASS | `audit_results.csv`, `audit_summary.md` in Anton's Downloads |
| 2 | Cleanup pipeline produced 235 acceptable rows | PASS | `reviews_cleaned.csv`, 247/251 distinct cleaned long-form quotes |
| 3 | 54 heavy-tier rows triaged 38 keep / 16 remove | PASS | `heavy_triage.csv` |
| 4 | Stefan delegated direction (best-outcome rubric) | PASS | Anton + Stefan exchange 2026-04-25 |
| 5 | Anton ratified Hybrid B+ (pull + activate form) | PASS | Anton green-light 2026-04-25 |
| 6 | "What Men Write Back" YouTube block currently rendering on T3 | PASS | Per `audit-pre-session-d.md` and foundation-brief §4 |
| 7 | Verbatim contracts (S-A 20-module, S-B/Job1 protocols zero-exec, S-C/Job2 reviews-de-AI'd, S-Cv2 module typography, S-D Job 0/1/2) | INTACT | Cross-section regression in QA checklist |
| 8 | Imagery (S-C/Job3 Higgs Field, S-E proof-block reset) | INTACT | Out-of-scope for Session F |
| 9 | Footer contact `hello@menofapollo.com` and stub `/privacy` /`/terms` pages | INTACT | Delivered in S-D Job 0.6/0.7 |

**Out of scope (do NOT touch):**

- Module pages, module body content (S-A verbatim contract).
- The "What Men Write Back" YouTube comments block (keep rendering exactly as it currently does on T3).
- Higgs Field imagery / Session E proof-block (settled).
- Hero, Mechanism reveal, "What you get inside the Collective", The Standard, FAQ, Founder block, Guarantee, Final exclusion (S-D locks).
- The Collective application form (separate from review submission form).
- The 251-row `apollo-reviews-export.csv` file — does not ship anywhere as customer-attributed text. Stays in repo as audit reference.

---

## Voice anchor (read before writing any new string)

### Refused vocabulary (one hit fails review)

```
alpha · sigma · high-value · king · chad · top G
grind · grindset · hustle · no days off · 4am club · beast mode
beast · savage · warrior · spartan · conquer · dominate · crush
TRT · peptides · cycle · enhanced · gear
macros · calorie deficit · IIFYM · tracking calories · weighing food (except as enemy)
motivation · hype · push through · no excuses
brotherhood · tribe · the boys · lions · wolves
journey · transformative · transform · game-changer · life-changing · blown away
next level · unleash · unlock (verb) · seamless · leverage (verb) · revolutionary
level up · take it to another level · mind-blowing · unreal
```

### Punctuation hard rules

- ❌ Em dashes (`—`) anywhere in customer-facing copy.
- ❌ Semicolons in customer-facing copy.
- ❌ Mid-sentence colons in customer-facing copy.
- ❌ Caps-lock shouting (one exception: *"FINALLY"* — sparingly).
- ❌ Profanity.
- ❌ Exclamation marks on primary CTAs.

### CTA register (use only these strings on primary buttons)

```
START THE 90-DAY BUILD →
GET THE FULL STACK →
APPLY FOR THE COLLECTIVE →
START WITH THE PROTOCOLS →
START THE TRAINING PROTOCOL →
START THE NUTRITION PROTOCOL →
ADD THE HOME GYM →
SUBMIT APPLICATION →
SUBMIT REVIEW →   ← NEW for Job 2 form
```

`SUBMIT REVIEW →` is added to the locked CTA register as part of this session.

---

## Job 1 — Pull the manufactured Reviews block `[Mode: Verbatim deletion + replacement microcopy]`

**Closes:** the testimonial-fraud surface area on home + /protocols.

### 1.1 Identify the block

The block currently renders in three placements per Session B Job 2 ("one source, three placements"):
- **Homepage `/`** — between Mechanism reveal and final CTA, eyebrow `Reviews`, header *"Past clients of the Protocols and the Collective. Names shortened to first name and initial."*, currently 6 cards (James R., Liam K., Tom H., Daniel P., Michael O., Alex T.) sourced from `public/reviews.csv`.
- **/protocols** — same component, same data source.
- **Collective deflection block on /protocols** — closer link *"More stories inside the Collective →"* under the universal block.

### 1.2 Replace the entire reviews block with a holding section

**Remove:** the entire 6-card block, the header, the sub, the rating line (`★★★★ 4.67  6 REVIEWS`), the `VERIFIED` badges, the `NEWEST | HIGHEST RATING` sort tabs, and the closer `YOU'VE REACHED THE END. THANK YOU FOR READING.`

**Replace with** this minimal holding section in the same position on home + /protocols:

```
EYEBROW:  Reviews
HEADER:   Open for real reviews.

BODY (one paragraph, ≤ 60 words):
We've decided to launch without manufactured reviews. The submission form
below is open. As real men finish the Protocols and the Collective and
write back, those words go here. If you've run the system and want to
share what changed, the form takes a minute.

LINK:     Read the unsolicited YouTube replies block below ↓
```

**Constraints:**

- Body is the new on-voice declarative — no em dashes, no semicolons, no banned vocabulary. Confirms Stefan's "this is not for everyone" register.
- The link points to the existing "What Men Write Back" YouTube comments block, which **remains in its current position** on both pages.
- Below this holding section, render the new Job 2 submission form (see §Job 2).
- Do NOT delete `public/reviews.csv` — keep the file in the repo, but the data binding is severed. Mark the file with a top comment: `# 2026-04-25 — Source severed. Audit-only reference. Do not re-bind without Stefan sign-off.` (CSV doesn't support comments; instead add a sibling file `public/reviews.README.md` with the same note.)

### 1.3 The "What Men Write Back" YouTube block stays exactly as it is

This is a separate block already on T3. Do NOT touch it. Verify it still renders unchanged after Job 1 ships. The current eyebrow (*"Replies"*), header (*"What Men Write Back"*), and sub (*"Unsolicited. Straight from my YouTube comments. Unedited."*) all stay verbatim.

### 1.4 Sort tabs / rating badge / count

The `★★★★ 4.67  6 REVIEWS` rating line, `NEWEST | HIGHEST RATING` sort tabs, and `VERIFIED` badges all go away with the manufactured block. They will return when the moderated submission queue (Job 2) accumulates enough rows for the block to relaunch.

### 1.5 Update component-copy-bank.md to reflect Job 1

In `brand-kit/01-docs/component-copy-bank.md` §2.2 (Proof / social-proof sections), mark the existing `Reviews` strings as `PULLED — pending real submissions (Session F, 2026-04-25)`. Do NOT delete the strings. Add a `LIVE` entry for the new holding section header *"Open for real reviews."* and the body paragraph.

### 1.6 Out of scope for Job 1

- Module pages, module bodies (S-A verbatim contract).
- The "Replies" / "What Men Write Back" YouTube block (keep verbatim).
- The Collective application form (separate from review submission form).
- Any other block on home or /protocols.

---

## Job 2 — Customer review submission form (Supabase + admin route + rate limit)

**Closes:** Session C v1 Job 4 (deferred since 2026-04-23). Activates the path for real moderated reviews.

### 2.1 Form fields

Inline form, rendered directly below the holding section (Job 1.2) on home + /protocols.

```
LABEL                INPUT TYPE          CONSTRAINTS
First name           text                required, ≤ 30 chars
Last initial         text                required, exactly 1 char A–Z
Email                email               required, validated, never displayed publicly
Rating               radio 1-5 stars     required, default unselected
Review text          textarea            required, ≤ 250 chars hard cap, live counter under input
[honeypot field]     text, hidden        must be empty on submit
SUBMIT REVIEW →      primary button      use the locked CTA from §CTA register
```

**Microcopy under the form:**

```
SUB:  Real reviews only. We read every one.
DISCLOSURE: Submissions are moderated. Approved reviews appear with first name + last initial only. Email is never displayed.
```

### 2.2 Supabase wiring

**Table:** `review_submissions`

```sql
create table public.review_submissions (
  id            uuid primary key default gen_random_uuid(),
  first_name    text not null,
  last_initial  text not null check (last_initial ~ '^[A-Z]$'),
  email         text not null,
  rating        smallint not null check (rating between 1 and 5),
  review_text   text not null check (char_length(review_text) <= 250),
  status        text not null default 'pending' check (status in ('pending','approved','rejected')),
  ip_hash       text not null,
  submitted_at  timestamptz not null default now(),
  approved_at   timestamptz,
  approved_by   text,
  rejected_at   timestamptz,
  rejected_by   text
);
create index review_submissions_status_idx on public.review_submissions (status, submitted_at desc);
create index review_submissions_iphash_idx on public.review_submissions (ip_hash, submitted_at desc);
```

**View** (read-only public surface for the future re-launched Reviews block):

```sql
create view public.reviews_published as
  select first_name || ' ' || last_initial || '.' as name_display,
         rating, review_text, approved_at as date_received
  from public.review_submissions
  where status = 'approved'
  order by approved_at desc;
```

The future re-launched Reviews block reads `reviews_published`, not `review_submissions`. The block stays pulled (per Job 1) until this view returns 6+ rows.

**Edge function** `rate-limit-review-submission`:

- 1 submission per `ip_hash` per 24h rolling window.
- On duplicate submission: return HTTP 200 with friendly body *"Thanks, we already got one from you recently."* — do not leak rate-limit internals or HTTP 429.
- Hash IP with SHA-256 + a server-side salt before storing. Do not store raw IPs.
- Honeypot field: if non-empty on submit, return 200 success silently and do not insert (silent bot rejection).

### 2.3 Admin moderation route

- **Path:** `/admin/reviews`
- **Gating:** auth required. Restricted to two whitelisted email addresses — `hello@menofapollo.com` (Stefan) and `ops.controlplane@gmail.com` (Anton). Use Supabase Auth or Lovable's auth primitive — whichever ships cleaner.
- **List view:** all rows ordered by `submitted_at desc`, columns visible: `first_name`, `last_initial`, `rating`, `review_text`, `email`, `submitted_at`, `status`.
- **Per-row actions:**
  - **Approve:** sets `status = 'approved'`, `approved_at = now()`, `approved_by = <admin email>`. Auto-strip em-dashes, semicolons, and mid-sentence colons from `review_text` before write (cleanup applied at approval, not at submission).
  - **Reject:** sets `status = 'rejected'`, `rejected_at = now()`, `rejected_by = <admin email>`. No reason captured (avoids PII / dispute risk).
- **Approved reviews enter `reviews_published` view automatically.**

### 2.4 Fallback if Lovable cannot gate `/admin/reviews` cleanly

If admin-route gating cannot be implemented in Lovable within this session, ship the form + Supabase table + edge function, and route approval via email instead:

- Each new submission triggers a Supabase webhook to a small server that emails both `hello@menofapollo.com` and `ops.controlplane@gmail.com` with the row content + an "Approve" link (one-time-token, expires 7 days, click = sets status=approved on that row).
- The email-fallback path stays in place until proper admin-route gating ships in Session G.

### 2.5 Placement

- Render the form immediately below the holding section (Job 1.2) on **home** and **/protocols**.
- Do NOT render on the Collective deflection block on /protocols (deflection block is reserved for the application CTA).
- Do NOT render on module pages.

### 2.6 Empty-state for the future Reviews block

When `reviews_published` returns 0 rows, the holding section (Job 1.2) is what renders. When it returns 1–5 rows, render the holding section + a preview line *"First N submitted. The block re-launches when we have six."* When it returns ≥ 6 rows, the holding section gets replaced by the relaunched Reviews block (separate Session — do NOT auto-relaunch in Session F).

### 2.7 Out of scope for Job 2

- Auto-relaunch of the Reviews block. That is a separate session triggered manually when `reviews_published` count ≥ 6 and Stefan signs off.
- Email notifications to submitters (no confirmation email sent to the reviewer; deliberate — keeps the surface area small).
- Multi-language support, GDPR consent banner (verified empty-cookie posture in S-D Job 0.6 — preserve).

---

## Final output

After Jobs 1–2 complete, respond with:

1. URL of the deploy preview.
2. Six-bullet summary:
   - **Job 1 status:** holding section live on home + /protocols. Manufactured Reviews block removed.
   - **Job 1 verification:** "What Men Write Back" YouTube block still renders. `public/reviews.csv` retained but unbinded; `public/reviews.README.md` added.
   - **Job 2 status:** form rendering on home + /protocols. `review_submissions` table exists in Supabase.
   - **Job 2 verification:** test submission goes through edge-function rate limit, lands in `pending` state, visible at `/admin/reviews` (or email-fallback delivered).
   - **Locks intact:** S-A 20-module verbatim, S-B/Job1, S-C/Job2 rules unchanged in code (data binding severed but rules preserved), S-Cv2, S-D Job 0/1/2, S-E proof-block.
   - **Anything you could not finish:** explicit list.
3. Anton runs `qa-checklist-session-f.md` against the preview before handing the URL to Stefan for binary sign-off.

Deploy to **preview**, not production. Production publish is gated on Stefan binary sign-off.

---

## Cross-reference

- Audit artefacts → `~/Downloads/audit_results.csv`, `~/Downloads/reviews_cleaned.csv`, `~/Downloads/audit_summary.md`, `~/Downloads/heavy_triage.csv`, `~/Downloads/stefan_review_brief.md`
- Foundation → `brand-kit/01-docs/foundation-brief.md`
- Voice → `brand-kit/01-docs/voice-system-v1.md`
- Component copy bank → `brand-kit/01-docs/component-copy-bank.md` (this session updates §2.2)
- Project rules → `project-rules.md`
- QA checklist → `content/apollo/lovable/qa-checklist-session-f.md`
- CHANGELOG → `content/apollo/lovable/CHANGELOG.md` (this session adds the Session F entry)
