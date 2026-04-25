---
session: E — proof block reset
version: v1 — 2026-04-25
status: PASTE-READY for Lovable (pending Stefan binary gate on 3 winning images)
scope: homepage `/` proof block + `/protocols` proof block — both pages, identical content
audit-override: Session D Gate 7. See `CHANGELOG.md` § session-e-proof-block-reset for full grounds.
prompt-pack: `~/Documents/Studio/men-of-apollo/deliverables/image-prompts-v5-arrived-state.md`
plan: `/Users/antonurso/.claude/plans/one-thing-that-we-bright-fairy.md`
approver: Stefan (binary YES/NO before Lovable swap)
driver: Anton, end-to-end
---

# Session E — Proof Block Reset (Lovable Change Brief)

> **What's changing:** Replace the 3 before/after diptych images on the proof block (both `/` and `/protocols`) with 3 single-frame "arrived state" portraits. Update section heading + sub + per-image captions + alt text per the spec below. Same section position, same component, same number of images — only the images themselves and the surrounding copy change.
>
> **Why:** Brand-foundation alignment. The diptych structure violates Sage-archetype + refused-vocab locks. Full grounds in `CHANGELOG.md` § session-e-proof-block-reset and the v5 prompt pack §1.
>
> **What stays:** Component structure, layout, section position, the 3-up grid, gold accent caption styling, and the "WHAT MEN ARE SAYING" real-screenshot social proof block below (untouched).

---

## 1. Pre-flight checklist (Anton, before opening Lovable)

- [ ] All 3 winning images selected from §7 of v5 prompt pack and saved locally as PNG/JPEG (3:2 landscape, ≥2048px long edge)
- [ ] Filenames standardised: `apollo-arrived-marcus.jpg`, `apollo-arrived-tom.jpg`, `apollo-arrived-sam.jpg` (or whatever fits Lovable's asset library convention)
- [ ] §9 model-win tracking table in v5 prompt pack filled in
- [ ] Stefan has signed off binary YES on the 3 images + this brief's copy
- [ ] Have the live preview URL open in a separate tab for spot-check after publish: `https://preview--apollo-ascension-landing.lovable.app/`

---

## 2. Section heading (paste-ready, both pages — identical)

```
THIS IS WHAT THE PROTOCOL HOLDS.
```

**Position:** above the 3-image grid, both `/` and `/protocols`. Replaces the current heading "What the 90-day arc actually produces" (or whichever heading is currently live).

**Styling:** keep current H2 styling on the section — same size, weight, colour as the prior heading. No new typography; just text content changes.

---

## 3. Sub-heading (paste-ready, both pages — identical)

```
No injections. No shortcuts. Run honestly.
```

**Position:** directly below the section heading, above the image grid.

**Styling:** keep current sub-heading styling. (This sub already exists in the v4 pending caption upgrade — carry it forward.)

---

## 4. Per-image captions (paste-ready)

The captions appear directly below each image in the 3-up grid. Order is fixed left-to-right (or top-to-bottom on mobile).

| Image slot | Caption (paste verbatim) |
|---|---|
| 1 (Marcus, kitchen) | `M., 38. 14 months in.` |
| 2 (Tom, home gym) | `T., 41. Year two.` |
| 3 (Sam, balcony) | `S., 35. 9 months in.` |

**Styling:** gold accent colour, letter-spacing 0.2em, ~70% body font size, all-caps optional. **Carry forward the caption styling that was specced for the v4 pending caption upgrade** ("MONTH 0 → MONTH 6" was supposed to use this styling — apply it here instead).

**Replaces:** the current "SIX MONTHS APART" captions on both pages (and the pending "MONTH 0 → MONTH 6" replacement that was queued — both are now obsolete).

---

## 5. Per-image alt text (paste-ready, both pages — identical)

In Lovable's image asset settings, set the alt text per image. This is the accessibility + SEO layer.

| Image slot | Alt text (paste verbatim) |
|---|---|
| 1 (Marcus, kitchen) | `Lean man in his late 30s pouring morning coffee in a sunlit kitchen, white t-shirt, calm and present.` |
| 2 (Tom, home gym) | `Lean athletic man in his early 40s sitting after a home-gym workout, towel around his neck, breathing.` |
| 3 (Sam, balcony) | `Lean man in his mid 30s on an outdoor balcony at dawn, linen shirt open, looking at the horizon.` |

---

## 6. Lovable swap — step-by-step

1. Open Lovable preview in browser. Edit mode.
2. Navigate to homepage `/`.
3. Locate the proof block (currently 3 before/after diptychs with "SIX MONTHS APART" captions, heading "What the 90-day arc actually produces").
4. **Image 1:** Click image slot 1, replace with `apollo-arrived-marcus.jpg`. Set alt text per §5 row 1. Set caption per §4 row 1.
5. **Image 2:** Click image slot 2, replace with `apollo-arrived-tom.jpg`. Set alt text per §5 row 2. Set caption per §4 row 2.
6. **Image 3:** Click image slot 3, replace with `apollo-arrived-sam.jpg`. Set alt text per §5 row 3. Set caption per §4 row 3.
7. Update section heading text per §2.
8. Update sub-heading text per §3 (or confirm it matches if v4 pending sub already shipped).
9. Save / publish to preview.
10. Navigate to `/protocols`. Repeat steps 3-9 for the equivalent proof block on the protocols page.
11. Save / publish to preview.

**Note:** if the proof block has been extracted into a Lovable shared component (per the Phase B+ pending refactor), steps 3-10 collapse to one edit that flows to both pages. Confirm in Lovable whether the component is shared or duplicated before starting.

---

## 7. Live verification (after publish)

Open `https://preview--apollo-ascension-landing.lovable.app/` in browser. Run all checks. Each must PASS.

### Homepage `/`
- [ ] Section heading reads exactly: `THIS IS WHAT THE PROTOCOL HOLDS.`
- [ ] Sub reads exactly: `No injections. No shortcuts. Run honestly.`
- [ ] 3 images render in correct order (Marcus, Tom, Sam)
- [ ] Each caption matches §4 verbatim
- [ ] Alt text on each image matches §5 (DOM inspect to confirm)
- [ ] Caption styling matches spec (gold, letter-spaced, ~70% size)
- [ ] No remnant "SIX MONTHS APART" or "MONTH 0 → MONTH 6" anywhere in the section
- [ ] No remnant "What the 90-day arc actually produces" anywhere in the section
- [ ] No "transformation", "before/after", "journey", "arc" in the proof block scope

### `/protocols`
- [ ] All of the above, identical

### Mobile (390px viewport, iPhone)
- [ ] Captions don't truncate
- [ ] Images don't squish — maintain 3:2 aspect ratio
- [ ] Stack vertically on mobile if that's the responsive behaviour

### Voice + brand
- [ ] Visual eyeball: 3 images read as cinematic-domestic, not gym-influencer or Instagram-filter
- [ ] Builds read as Apollonian (lean + proportionate), NOT bodybuilder, NOT shredded
- [ ] No logos, branded gym wear, or supplement props visible in any image

### Accessibility
- [ ] Lighthouse accessibility check on both pages confirms alt text picked up
- [ ] No accessibility regressions vs prior live state

---

## 8. Sign-off lines

| Owner | Action | Status |
|---|---|---|
| Anton | Generated images per v5 prompt pack §3-§4, applied §6 QC, selected winners per §7 | ☐ |
| Anton | Filled in §9 model-win tracking table in v5 prompt pack | ☐ |
| Stefan | Binary YES on 3 winning images + this brief's copy | ☐ |
| Anton | Executed Lovable swap per §6 above | ☐ |
| Anton | Live verification per §7 above — all checks PASS | ☐ |
| Stefan | Notified of ship | ☐ |

---

## 9. Rollback plan

If Stefan returns NO at the binary gate or if §7 verification fails:

1. **Single-revision NO** — adjust the failing element (image, caption, copy) and re-submit one round to Stefan. Do NOT re-trigger Lovable swap until Stefan YES.
2. **Second NO** — escalate to call. Do not iterate further async.
3. **Live verification fail post-publish** — revert the proof block to v4 state in Lovable (keep the v4 images and "MONTH 0 → MONTH 6" captions as the rollback target). Re-open as Session E v2 with a corrected brief.

---

## 10. References

- Plan: `/Users/antonurso/.claude/plans/one-thing-that-we-bright-fairy.md`
- v5 prompt pack: `~/Documents/Studio/men-of-apollo/deliverables/image-prompts-v5-arrived-state.md`
- v4 prompt pack (SUPERSEDED): `~/Documents/Studio/men-of-apollo/deliverables/higgsfield-prompts-v4-plain-wall.md`
- Audit override: `content/apollo/lovable/CHANGELOG.md` § session-e-proof-block-reset
- Brand foundation: `brand-kit/01-docs/foundation-brief.md`, `voice-system-v1.md`, `component-copy-bank.md`
- Research dossier: `brand-kit/00-research/dossier-2026-04-25.md`
