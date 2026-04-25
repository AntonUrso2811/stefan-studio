# QA Checklist — Session F (Reviews Pull + Submission Form)

**Run after Lovable executes `session-f-reviews-pull-and-form.v1.md` against the preview.** Anton signs off before handing the preview URL to Stefan for binary production-publish decision.

**Preview URL pattern:** `https://id-preview--<lovable-uuid>.lovable.app/`

---

## Job 1 — Manufactured Reviews block pulled

### 1A — Homepage `/`

- [ ] Old 6-card Reviews block (James R., Liam K., Tom H., Daniel P., Michael O., Alex T.) is **gone** from the DOM.
- [ ] Eyebrow `Reviews` + header `Open for real reviews.` is present in the same position the old block occupied.
- [ ] Holding-section body paragraph reads exactly as written in §1.2 of the change brief (≤ 60 words).
- [ ] Link `Read the unsolicited YouTube replies block below ↓` is present and resolves to the YouTube comments block on the same page.
- [ ] `★★★★ 4.67  6 REVIEWS` rating line is **gone**.
- [ ] `NEWEST | HIGHEST RATING` sort tabs are **gone**.
- [ ] `VERIFIED` badges are **gone**.
- [ ] Closer `YOU'VE REACHED THE END. THANK YOU FOR READING.` is **gone**.

### 1B — `/protocols`

- [ ] Same checks as 1A. Old 6-card block gone, holding section in place.
- [ ] The Collective deflection block (closer link `More stories inside the Collective →`) on /protocols still renders unchanged.

### 1C — "What Men Write Back" YouTube block

- [ ] Block still renders on home + /protocols in its current position.
- [ ] Eyebrow `Replies`, header `What Men Write Back`, sub `Unsolicited. Straight from my YouTube comments. Unedited.` all present and **byte-identical** to pre-Session-F state.
- [ ] None of the YouTube comment cards have been altered.

### 1D — Repo state

- [ ] `public/reviews.csv` file still exists in the repo (do NOT delete).
- [ ] `public/reviews.README.md` exists with the line `2026-04-25 — Source severed. Audit-only reference. Do not re-bind without Stefan sign-off.` (or equivalent wording).
- [ ] No component in the codebase reads from `public/reviews.csv` after Session F. Verify via grep: `grep -r "reviews.csv" src/ → no hits`, `grep -r "reviews_published" src/ → hits only in the future-relaunch placeholder (or nowhere yet)`.

### 1E — Voice / copy QA

- [ ] Holding-section body contains zero em-dashes (`—`).
- [ ] Holding-section body contains zero semicolons.
- [ ] Holding-section body contains zero mid-sentence colons.
- [ ] Holding-section body contains zero refused-vocabulary hits per `foundation-brief.md` §7.
- [ ] Header `Open for real reviews.` is on-voice (declarative, restraint, operator register).

---

## Job 2 — Customer review submission form

### 2A — Form renders correctly

- [ ] Form renders **immediately below** the holding section on homepage `/`.
- [ ] Form renders **immediately below** the holding section on `/protocols`.
- [ ] Form does **not** render on any module page (MOA_01 through MOA_20).
- [ ] Form does **not** render on the Collective deflection block on /protocols.

### 2B — Form fields and validation

- [ ] **First name** field — text, required, max 30 chars. Submit blocked if empty.
- [ ] **Last initial** field — text, required, single uppercase A–Z. Submit blocked if empty or invalid.
- [ ] **Email** field — email, required, format-validated. Submit blocked if invalid.
- [ ] **Rating** field — 1–5 stars, radio, required, no default. Submit blocked if no rating chosen.
- [ ] **Review text** — textarea, required, hard cap 250 chars. Live character counter visible under the input.
- [ ] **Honeypot** — hidden field, not visible to humans. If filled (by a bot), submission silently succeeds (HTTP 200) but no row inserted.
- [ ] **`SUBMIT REVIEW →`** button — primary CTA styling matching the locked register. No exclamation mark. Disabled when validation fails.

### 2C — Microcopy

- [ ] Sub-text `Real reviews only. We read every one.` renders below the form.
- [ ] Disclosure text `Submissions are moderated. Approved reviews appear with first name + last initial only. Email is never displayed.` renders below the sub.
- [ ] Both passages contain zero em-dashes / semicolons / refused-vocab hits.

### 2D — Supabase wiring

- [ ] `review_submissions` table exists in Supabase with the schema in §2.2 of the change brief.
- [ ] `reviews_published` view exists and returns 0 rows immediately after Session F deploy.
- [ ] Indexes `review_submissions_status_idx` and `review_submissions_iphash_idx` both exist.
- [ ] Submitting a test review from the form inserts a row with `status = 'pending'` and `submitted_at` populated.

### 2E — Edge function `rate-limit-review-submission`

- [ ] First submission from a fresh IP succeeds.
- [ ] Second submission from the same IP within 24h returns HTTP 200 with body containing the friendly text *"Thanks, we already got one from you recently."* — does not return HTTP 429 or leak rate-limit internals.
- [ ] `ip_hash` column stores the SHA-256 hash of `IP + server-salt`, not the raw IP. Verify by inspecting one row.
- [ ] Honeypot test: filling the hidden field and submitting returns HTTP 200 success but no row is inserted in `review_submissions`.

### 2F — Admin route `/admin/reviews`

- [ ] Route exists at `/admin/reviews`.
- [ ] Unauthenticated visit is blocked (redirect or 401 / 403).
- [ ] Anton's email `ops.controlplane@gmail.com` can authenticate and see the queue.
- [ ] Stefan's email `hello@menofapollo.com` can authenticate (stub or real, depending on inbox configuration in S-D).
- [ ] List view shows columns: `first_name`, `last_initial`, `rating`, `review_text`, `email`, `submitted_at`, `status`. Ordered by `submitted_at desc`.
- [ ] **Approve** action: sets `status = 'approved'`, `approved_at = now()`, `approved_by = <admin email>`. Auto-strips em-dashes / semicolons / mid-sentence colons from `review_text` before write.
- [ ] **Reject** action: sets `status = 'rejected'`, `rejected_at`, `rejected_by`. No reason captured.
- [ ] After approve, the row appears in `reviews_published` view.

### 2G — Email fallback (only if Lovable cannot gate `/admin/reviews` in this session)

- [ ] New submission triggers email to both `hello@menofapollo.com` and `ops.controlplane@gmail.com` with row content.
- [ ] Email contains a one-time-token "Approve" link (expires 7 days). Click = sets `status = 'approved'`.
- [ ] Email-fallback path is documented in CHANGELOG entry as the interim solution to be replaced in Session G.

---

## Cross-section regression — locks survived?

### S-A — 20-module verbatim contract

- [ ] Random spot-check: pick MOA_05, MOA_10, MOA_15, MOA_19. Open each module page and verify the body content matches `content/apollo/modules/<slug>.md` byte-for-byte (only h2/h3 headings differ, per S-C structural addendum).

### S-B/Job 1 — /protocols zero-executive-language lock

- [ ] /protocols "Who the Protocols are for" block contains zero executive / founder / CEO language. Lock from `session-b-feedback-fixes.v1.md` Job 1.

### S-C v1 Job 2 — original reviews-de-AI'd rules

- [ ] The S-C/Job 2 rules (no em-dashes in any review, no banned vocab, varied rhythm, first-name + last-initial format) are STILL the rules — they apply to whatever future content lands in `reviews_published`. Job 1 of Session F pulls the data binding; it does not delete the rules.
- [ ] Auto-strip on approval (§2F bullet) implements the em-dash + semicolon + mid-colon scrub at the point of approval, replacing the previous reliance on Lovable's strip-on-render.

### S-Cv2 — module typography

- [ ] Body 18/1.65 mobile, 19/1.7 desktop, 66ch measure, h2 hair-rule, scroll-progress on module pages only — all unchanged.

### S-D Job 0 — cross-cutting fixes

- [ ] Em-dash strips on the 5 named legacy prose lines (S-D Patch 2) still hold.
- [ ] Header navigation harmonisation (S-D Job 0.5) unchanged.
- [ ] Footer legal block (S-D Job 0.6) unchanged. `hello@menofapollo.com` and `© 2026 ALL RIGHTS RESERVED · MEN OF APOLLO ...` line still render.
- [ ] `/privacy` and `/terms` stub pages (S-D Job 0.7) still render with stub copy.

### S-D Job 1 — Homepage

- [ ] Hero, identity bullets, NEW agitation block, NEW mechanism reveal, NEW "what you get inside the Collective", The Standard cards, founder block, common-questions, final CTA — all unchanged.

### S-D Job 2 — /protocols

- [ ] Hero, agitation, mechanism, stack offer (single placement), FAQ, guarantee, final exclusion — all unchanged.

### S-E — proof-block reset

- [ ] Whatever proof-block state was sign-off-approved in Session E renders unchanged. Session F does not touch imagery.

---

## Voice / copy hard scans

### Em-dash sweep

- [ ] `grep -rn "—" src/` against the deployed preview source returns zero hits in customer-facing copy. Structural list separators (e.g. `Input 1 — Sleep`) and numerical en-dashes (e.g. `10–15%`) are flagged but acceptable per S-D Patch 2.

### Banned vocabulary sweep

- [ ] `grep -rn -i -E "(transform|game-changer|life-changing|next level|unleash|unlock|seamless|revolutionary|level up|mind-blowing|grindset|hustle|beast mode|alpha|sigma|chad|brotherhood|tribe|the boys)" src/` returns zero hits in customer-facing strings.

### Punctuation hard rules

- [ ] `grep -rn ";" src/` against customer-facing copy → zero hits.

---

## Sign-off block

> **Anton sign-off:** ☐ All checks pass. ☐ Some failures (list below). Date: ____________
>
> **Failures (if any):** ____________
>
> **Hand-off URL to Stefan:** ____________
>
> **Stefan binary decision:** ☐ Production publish approved ☐ Hold + revisions: ____________

---

## Notes

- If any check in §Cross-section regression fails, **halt** before handing to Stefan. The lock survival is non-negotiable.
- If §2 (form) cannot be completed cleanly in one Lovable run (e.g. Supabase wiring takes longer than expected), ship Job 1 alone to preview and defer Job 2 to a Session F.1 patch. Job 1 is the load-bearing brand decision; Job 2 is the operational follow-up.
- Stefan async-review uses the preview URL only. Production publish is the binary gate.
