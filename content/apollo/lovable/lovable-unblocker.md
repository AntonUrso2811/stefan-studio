# Lovable Session D — paste-ready unblocker

**When Lovable halts at Pre-flight Gates 8 and 9, paste the block below into the Lovable chat verbatim.**

If any value differs from your reality, override it inline before pasting (don't ship `<<ANTON_OVERRIDE>>` to Lovable — replace it).

---

## Paste-ready block

```
GATE 8 — FOOTER LEGAL DATA:
   Privacy URL:    /privacy
   Terms URL:      /terms
   Contact email:  hello@menofapollo.com   <<ANTON_OVERRIDE if Stefan uses a different inbox>>
   GDPR / cookie:  We use only essential cookies. No third-party trackers.

GATE 9 — /PROTOCOLS AGITATION HEADLINE:
   Verified in browser. Headline is render-clipped only — no missing text.
   (Layout fix: ensure the section header above the "and stimulants to feel
   normal" image is fully visible at 320px / 375px / 414px / 1024px / 1440px
   viewport widths. No string change required.)

DECISIONS REGISTER (audit §6) — all 12 LOCKED PER RECOMMENDATION:
   1. Em-dash strip on locked verbatim blocks: APPROVED (period substitutions per component-copy-bank §7; triad rewrite for final exclusion block)
   2. "transformation arc" → "90-day arc": APPROVED
   3. "Men and women" stays on /protocols (universal entry): APPROVED
   4. Currency: ship USD as live; GBP deferred to later session
   5. Footer legal block: per Gate 8 above
   6. Homepage hero: identity-led mythic + proof anchor (per Job 1.1): APPROVED
   7. Homepage common-questions block (per Job 1.8): APPROVED
   8. Homepage what-you-get inside Collective (per Job 1.5): APPROVED
   9. Review product tags (TRACKING BLUEPRINT etc.): KEEP
   10. Identity bullet 04 "ambition": KEEP
   11. Live-state: agitation headline assumed render-clipped (per Gate 9); mobile mechanism-card QA done in-Lovable; FAQ answers surfaced in your Final Output
   12. Collective price band on home: KEEP GATED

Proceed with Job 0, Job 1, Job 2 in order. Preview-only deploy. Return the
Final Output block in the exact shape specified in the prompt.
```

---

## Notes on the defaults

**Privacy / Terms URLs (`/privacy` and `/terms`):**
Relative paths. Lovable should generate stub pages at these routes if they don't exist yet. Stefan signs off the actual policy text before production publish. If you already have an external policy host (Termly / iubenda), replace with the absolute URL before pasting.

**Contact email (`hello@menofapollo.com`):**
Best-guess placeholder. The live site footer doesn't currently surface a contact email — flag for Stefan async-confirm. If he uses `stefan@`, `team@`, `hello@`, or a personal address, override before pasting.

**GDPR / cookie line:**
Defensible default for a UK digital product running essential cookies only. If you add third-party trackers (Plausible, GA, FB pixel, Hotjar) before launch, swap to: *"We use essential cookies plus minimal analytics. See Privacy for details."*

**Agitation headline:**
The PDF capture from 2026-04-25 08:32 shows the line *"and stimulants to feel normal."* sitting alone above the gym-shot image — clearly the tail of a longer headline. Treating this as a render-clip (the full string exists in the DOM but the layout cuts it visually) is the conservative read. If Stefan or Anton later confirms the string is genuinely missing, a small follow-up patch supplies it.

---

## After Lovable returns the Final Output

1. Open the preview URL it provides
2. Capture full-scroll PDFs of `/` and `/protocols` post-execution
3. Run `qa-checklist-session-d.md` top-to-bottom — cross-section regression block is the load-bearing one
4. Send the PDFs + Lovable's Final Output text back into Claude Code for voice-check before forwarding to Stefan

If anything in Lovable's response looks off, paste the response back into Claude Code and we triage before proceeding.
