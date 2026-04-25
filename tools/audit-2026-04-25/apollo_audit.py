#!/usr/bin/env python3
"""Phase 2 audit on apollo-reviews-export.csv. Deterministic scoring keyed to calibration.
Outputs audit_results.csv + per-row JSON with signals for downstream cleanup."""
import csv
import json
import re
from pathlib import Path

SRC = Path("/Users/antonurso/Downloads/apollo-reviews-export.csv")
OUT_AUDIT = Path("/Users/antonurso/Downloads/audit_results.csv")
OUT_JSON = Path("/tmp/apollo_audit_per_row.json")

# Lego-phrase pool — sentences that appear in 5+ different reviews
# (extracted from calibration; each is a copywriter-assembly signature)
LEGO_PHRASES = [
    "I'll keep this on the shelf for years.",
    "Will keep running the inputs after the 90 days.",
    "Two cycles of bulking and cutting got me back to the start.",
    "The page reads like the man writes. That's rare.",
    "I trusted it because nothing inside felt like a restriction.",
    "Finally something honest in this space.",
    "Recommended to two friends already.",
    "Stefan writes like a man who has actually done it.",
    "Quietly the best thing I've spent money on this year.",
    "Three years of MyFitnessPal and I weighed more than when I started.",
    "Wish I'd found this five years ago.",
    "First fitness writing I've read that respects the reader.",
    "Reads like a coach, not a guru.",
    "Two-plus years in the gym. Photos told a different story.",
    "Energy was gone by 3pm. Coffee stopped working months ago.",
    "Sleep, training, food. Fixed all three at once. Should have done it years ago.",
    "No needles. No pharmacy. No subscription. Just the inputs.",
    "It reads the way I think. That's why I bought.",
    "A clinic told me I qualified for TRT. I wasn't ready for that.",
    "I'd read everything. Owned three apps. Body still drifting.",
    "Worth every pound.",
    "Worth every dollar.",
    "First program I've finished.",
    "First programme I've finished.",
    "Nothing here I hadn't read before. The difference is the order.",
    "I'd been training four times a week for two years and going backwards.",
    "Came across the page through a YouTube search. Stayed for the tone.",
    "Bought this on a Tuesday. By Friday I'd already changed my evenings.",
    "I knew what to do. I just wasn't doing it.",
    "Forty was getting close and I felt fifty.",
    "I caught a photo of myself holding my daughter. That was enough.",
    "I'd let it slip for a decade. My son was old enough to notice.",
    "I'd plateaued for eighteen months and stopped photographing my back.",
    "Lifts had stalled. Sleep was bad. I'd given up on the mirror.",
    "Got quoted a TRT panel last spring. Wanted one more honest attempt first.",
    "A friend on semaglutide kept telling me to try it. I'm glad I waited.",
    "I was three weeks from booking the consult. Tried this first.",
    "My boy turned six and outran me on a beach. That was the morning.",
    "My father had a heart attack at fifty-eight. I'm thirty-eight.",
    "Tracking macros became the workout. The body never followed.",
    "The Hone quote came in. So did the doubt. Found this instead.",
    "Heard Stefan on a podcast clip. Liked the register.",
    "Saw the IG post about the five inputs. Made too much sense.",
    "Bulk, cut, repeat. Same composition every time. Three cycles in.",
    "A mate on the Collective sent me the bundle link.",
    "Found the page after months of looking for something not shouty.",
    "Stefan answers in the chat himself. Not a VA. Not a bot.",
    "Eight other men running the same line. That's the part nothing else has.",
    "First two weeks were rough. Stuck with it. Glad I did.",
    "First men's community I've been in that wasn't motivational noise.",
    "Honest writing. Honest mechanism. Honest result.",
    "Plain. No hype. No costume.",
    "He doesn't pretend it's a secret. He just runs it properly.",
    "The compound piece is what makes it land. Five at once, not one at a time.",
    "Felt like a system, not a sales funnel.",
    "It's the first thing I've read that doesn't shout.",
    "The five inputs are obvious in hindsight. That's the point.",
    "I've been in three Skools and one Discord. None felt like this.",
]

# Outcome-line pool (the "result" sentences) — these recur as the conversion payload
OUTCOME_LINES = [
    "Hit a 180kg deadlift at thirty-nine. Hadn't seen that since university.",
    "Pull-ups went from four to twelve. Clean ones.",
    "Squat up 30kg. First time past bodyweight in years.",
    "Squat up 65 lb. First time past bodyweight in years.",
    "Five inputs, twelve weeks, eight men I now talk to weekly.",
    "Forty-five minutes, three times a week. Strength returned.",
    "Resting heart rate down 9 beats. Nothing else changed.",
    "Asleep in ten minutes. Used to take an hour with a screen.",
    "Wake before the alarm. Hadn't done that since my twenties.",
    "Stopped counting and started losing. Took me a while to trust it.",
    "Stopped chasing numbers. Numbers came anyway.",
    "Down two trouser sizes. Up 20kg on the deadlift.",
    "Down two trouser sizes. Up 45 lb on the deadlift.",
    "My wife asked what I was doing. I sent her the page.",
    "Wife noticed before I did. Down a notch on the belt.",
    "Six kilos down. Sleeping through.",
    "Three months. Lost the gut.",
    "Eleven weeks in and I look like I did at thirty-two.",
    "Ninety days, exactly as advertised. Body responded the way it should have.",
    "Lifts moved every week for the first time since my twenties.",
    "Travel for work three weeks a month. Haven't missed a session in eleven weeks.",
    "First time I've eaten properly without guilt in a decade.",
    "Cravings stopped about three weeks in. Genuinely surprised.",
    "Off MyFitnessPal for the first time in four years.",
    "The weekly calls are the part I underestimated. Genuinely.",
    "The other men in the group are why I finished.",
    "Three months on, still in the alumni chat. Still running the inputs.",
    "Down a jeans size in nine weeks. No app.",
    "Down 28 lb over five months. Sustainable the whole way.",
    "Down two stone over five months. Sustainable the whole way.",
    "Eight kilos off and I'm eating more than I used to.",
    "Off caffeine by week six. Still don't miss it.",
    "Eight hours actual sleep.",
    "Whoop sleep score up from 67 to 88 over two months.",
    "Built the home gym for under a thousand. No commute, no excuses.",
    "Built the garage gym for under a grand.",
    "Garage gym in six weeks. Best decision of the year.",
    "Hotel room workouts that actually do something. Finally.",
    "Best money I've spent on my body. The group is real.",
    "Bench went from 200 lb for three to 225 lb for five.",
    "Bench went from 90kg for three to 100kg for five.",
    "Added 25kg to my deadlift in eleven weeks.",
    "Added 55 lb to my deadlift in eleven weeks.",
    "Added 15kg to my bench in a hundred days.",
    "Added 35 lb to my bench in a hundred days.",
    "Lost 6kg without weighing a single thing.",
    "Lost 13 lb without weighing a single thing.",
    "Hit a 405 lb deadlift at thirty-nine. Hadn't seen that since university.",
    "Down 9kg, deadlift past 200kg, but the cohort was the thing.",
    "Down 20 lb, deadlift past 440 lb, but the cohort was the thing.",
    "Rings, a barbell, a bench. That's the entire setup.",
    "Off MyFitnessPal for the first time in four years. No macros.",
    "Three months. Lost the gut. Got the energy back.",
    "Down 7kg, lifts up across the board, off the snooze button.",
    "Down 15 lb, lifts up across the board, off the snooze button.",
    "Down a jeans size in nine weeks.",
    "Three sessions a week. That was it.",
    "Morning sunlight walk became the part I refuse to miss.",
]

# Specificity markers — concrete numerals + units suggest the reviewer named a real metric
SPECIFICITY_RE = re.compile(
    r"\b(?:\d+\s?(?:kg|lb|lbs|km|miles?|mins?|minutes?|hours?|hrs?|days?|weeks?|months?|years?|stone|pounds?|hours?))\b"
    r"|\b(?:\$|£)\d+",
    re.IGNORECASE,
)

# Brand-vocab echo (problematic when used in customer voice without personal framing)
BRAND_VOCAB = ["five inputs", "the protocols", "the collective", "five at once", "the inputs"]

def score_row(r):
    quote_long = (r.get("quote_long") or "").strip()
    quote_short = (r.get("quote_short") or "").strip()
    headline = (r.get("internal_headline_draft") or "").strip()
    metric = (r.get("internal_outcome_metric") or "").strip()

    signals = []
    score = 0

    # 1. Lego phrase count
    legos_present = [p for p in LEGO_PHRASES if p in quote_long]
    if legos_present:
        score += min(len(legos_present), 6)
        plural = "phrase" if len(legos_present) == 1 else "phrases"
        # Truncate at word boundary
        sample = legos_present[0]
        if len(sample) > 50:
            words = sample.split()
            sample = ""
            for w in words:
                if len(sample) + len(w) + 1 > 50:
                    break
                sample = (sample + " " + w).strip()
            sample = sample.rstrip(",.") + "..."
        signals.append(f"{len(legos_present)} pooled {plural} ({sample!r})")

    # 2. Outcome-line reuse — flag if outcome is from shared pool
    outcomes_present = [o for o in OUTCOME_LINES if o in quote_long]
    if len(outcomes_present) >= 1:
        # outcome line itself is allowed, but if 2+ that's high template
        if len(outcomes_present) >= 2:
            score += 1
            signals.append(f"{len(outcomes_present)} pooled outcome lines")

    # 3. Em-dash present (lock violation)
    if "—" in quote_long or "—" in quote_short:
        score += 1
        signals.append("em-dash present (lock violation)")

    # 4. Headline / metric mismatch
    metric_lower = metric.lower()
    quote_lower = quote_long.lower()
    if metric and metric_lower not in quote_lower:
        score += 1
        m_short = metric if len(metric) <= 40 else metric[:37].rsplit(" ", 1)[0] + "..."
        signals.append(f"outcome_metric ({m_short!r}) absent from quote — template assembly tell")

    # 5. Brand-vocab echo without personal framing
    for bv in BRAND_VOCAB:
        if bv in quote_long.lower() and "i" not in quote_long.split(bv)[0][-15:].lower():
            # if "five inputs" is preceded by no first-person pronoun in nearby context, treat as brand echo
            pass  # too noisy; skip strict check

    # 6. Specificity — counter-signal (subtract from score)
    specifics = SPECIFICITY_RE.findall(quote_long)
    if specifics:
        # Specificity counts only if it's not just from a pooled outcome line
        if len(outcomes_present) == 0:
            score -= 2
            signals.append(f"original specifics ({specifics[0]}) not from outcome pool")
        elif len(specifics) >= 3:
            # multiple specifics across pooled+original
            pass

    # 7. Anaphoric-No triad in customer voice (Stefan signature)
    no_triad = re.search(r"No \w+\.\s*No \w+", quote_long)
    if no_triad:
        score += 1
        signals.append("anaphoric-No triad (Stefan voice fingerprint in customer mouth)")

    # 8. Honest×3 / similar parallelisms (Stefan-rhythm-in-customer-mouth)
    if "Honest writing. Honest mechanism. Honest result." in quote_long:
        score += 1
        if not any("Honest writing" in s for s in signals):
            signals.append("Honest×3 parallelism (Stefan rhythm)")

    # Verdict mapping
    if score >= 6:
        verdict = "LIKELY_AI_OR_FABRICATED"
        confidence = "high"
        recommendation = "remove"
    elif score >= 4:
        verdict = "LIKELY_AI_OR_FABRICATED"
        confidence = "medium"
        recommendation = "pull_for_human_review"
    elif score >= 2:
        verdict = "PROBABLY_AI"
        confidence = "medium"
        recommendation = "pull_for_human_review"
    elif score == 1:
        verdict = "UNCERTAIN"
        confidence = "low"
        recommendation = "keep_but_verify"
    elif score == 0:
        verdict = "UNCERTAIN"
        confidence = "low"
        recommendation = "keep_but_verify"
    else:  # negative score
        verdict = "PROBABLY_REAL"
        confidence = "low"
        recommendation = "keep"

    if not signals:
        signals.append("no strong AI tells; generic positive register")

    return {
        "id": r["id"],
        "verdict": verdict,
        "confidence": confidence,
        "top_signals": signals[:3],  # limit to 3
        "recommendation": recommendation,
        "raw_score": score,
        "legos_present": legos_present,
        "outcomes_present": outcomes_present,
        "specifics": specifics,
    }

# Run
with open(SRC, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

audit_rows = []
detail_rows = []
for r in rows:
    a = score_row(r)
    audit_rows.append({
        "id": a["id"],
        "verdict": a["verdict"],
        "confidence": a["confidence"],
        "top_signals": " | ".join(a["top_signals"]),
        "recommendation": a["recommendation"],
    })
    detail_rows.append({**a, "src": r})

# Write audit_results.csv
with open(OUT_AUDIT, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "verdict", "confidence", "top_signals", "recommendation"])
    writer.writeheader()
    writer.writerows(audit_rows)

# Write per-row detail JSON for cleanup phase
with open(OUT_JSON, "w", encoding="utf-8") as f:
    # JSON-friendly: drop the src dict
    json.dump([{k: v for k, v in d.items() if k != "src"} for d in detail_rows], f, indent=1)

# Print summary
from collections import Counter
verdict_counts = Counter(a["verdict"] for a in audit_rows)
rec_counts = Counter(a["recommendation"] for a in audit_rows)
print(f"=== Audit complete: {len(audit_rows)} rows ===\n")
print("Verdict distribution:")
for v in ["LIKELY_REAL", "PROBABLY_REAL", "UNCERTAIN", "PROBABLY_AI", "LIKELY_AI_OR_FABRICATED"]:
    print(f"  {v}: {verdict_counts.get(v, 0)}")
print()
print("Recommendation distribution:")
for r in ["keep", "keep_but_verify", "pull_for_human_review", "remove"]:
    print(f"  {r}: {rec_counts.get(r, 0)}")
print()
print(f"Audit CSV written: {OUT_AUDIT}")
print(f"Per-row detail JSON: {OUT_JSON}")

# Show top 10 worst rows (highest score)
sorted_d = sorted(detail_rows, key=lambda d: -d["raw_score"])
print("\n=== Top 10 most suspicious (highest raw_score) ===")
for d in sorted_d[:10]:
    print(f"  {d['id']} score={d['raw_score']} {d['verdict']}: {d['top_signals'][0][:80]}")

# Show bottom 10 (most likely real)
print("\n=== Top 10 most likely authentic (lowest raw_score) ===")
for d in sorted_d[-10:]:
    print(f"  {d['id']} score={d['raw_score']} {d['verdict']}: {d['top_signals'][0][:80]}")
