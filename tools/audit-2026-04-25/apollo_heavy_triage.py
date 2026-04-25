#!/usr/bin/env python3
"""Heavy-row triage: 38 keep / 16 remove decisions across the 54 LIKELY_AI_OR_FABRICATED rows.
Writes heavy_triage.csv with id, decision (keep/remove), rationale, plus a Stefan-decision column for binary override."""
import csv
from pathlib import Path

CLEANED = Path("/Users/antonurso/Downloads/reviews_cleaned.csv")
OUT = Path("/Users/antonurso/Downloads/heavy_triage.csv")

# Triage decisions made by reading each cleaned row against its source on 2026-04-25.
# Format: id -> (decision, rationale)
TRIAGE = {
    "rev_1012": ("keep", "BP-context opener + concrete 20lb/440lb metrics + believable cohort comparison."),
    "rev_1006": ("remove", "Too short and too generic. No verifiable specific. No proof value."),
    "rev_1170": ("keep", "Coherent narrative: Greece deadline, wife-noticed beat, belt notch metric."),
    "rev_1114": ("remove", "Outcome paraphrase only, zero customer color, reads as a brand fact card."),
    "rev_1204": ("keep", "Discovery + 13lb loss + product-aware vegetarian caveat. Three solid beats."),
    "rev_1021": ("keep", "Terse customer voice with specific timeline (Tuesday April + 9 weeks + no app)."),
    "rev_1082": ("remove", "Duplicate of rev_1078's 'Sales job. Travel. Hotels. Excuses.' opener with weaker outcome (Three months / gut went vs 405lb deadlift)."),
    "rev_1152": ("remove", "Birthday-gift opener is fresh but two brand-vocab phrases ('five inputs, twelve weeks' + 'compound piece is what makes it land') in one quote = too on-brand."),
    "rev_1040": ("keep", "Sleep-podcast discovery + specific 15kg bench gain. 'Plain' closer reads as British terseness."),
    "rev_1118": ("keep", "Greece deadline + 9kg/200kg metrics + cohort + macro-coaching comparison. Rich proof."),
    "rev_1032": ("keep", "Office/half-marathon contradiction is a strong customer voice. Specific 55lb deadlift gain. Brand-vocab line is single touch, not pattern."),
    "rev_1033": ("keep", "Wife-scolding hook + belt notch + product-aware caveat + plausible closer."),
    "rev_1058": ("keep", "Specific past failure (lost stone wrong way) into specific outcome (cravings stopped week three)."),
    "rev_1195": ("keep", "Stag-do hook is human and specific. Outcome paraphrase carries the proof. Understated closer."),
    "rev_1064": ("remove", "Internal inconsistency: 5-star review with 'Four stars from me' closer. Closer-pool was not rating-aware."),
    "rev_1222": ("keep", "Ninety-day frame + 15lb specific + brand-vocab as customer adoption (single touch)."),
    "rev_1213": ("remove", "Duplicate opener with rev_1082 and rev_1078. Weakest outcome of the three. Triage to keep variety."),
    "rev_1106": ("keep", "Forties frame + 55lb deadlift gain + brand-vocab line. Plausible age-gated voice."),
    "rev_1147": ("keep", "Self-aware cynical voice + specific 9bpm HR change + 8/10 closer. Strong."),
    "rev_1217": ("keep", "Forwarding-the-page hook + 9-week specific + no-app proof. Tight."),
    "rev_1034": ("keep", "Mid-life acknowledgement opener + weekly-calls outcome. Distinct voice though slightly generic."),
    "rev_1186": ("keep", "Divorce hook is strong personal context. Sleep/training/food paraphrase carries the brand claim without echoing it."),
    "rev_1060": ("keep", "Shift-work context + 13lb specific + product-aware caveat. Coherent."),
    "rev_1189": ("keep", "Forty-in-Feb / wall-in-March opener + 9kg/200kg + 'Honest writing' (single, not Honest×3) + plausible closer."),
    "rev_1096": ("keep", "Seven-day-reset hook + specific Whoop score change (67 to 88). Strong proof."),
    "rev_1051": ("keep", "Mid-thirties context + decade-of-guilt outcome. 'No needles.' single use, not anaphoric triad."),
    "rev_1124": ("remove", "Em-dash scrub broke a sentence ('Not in bed. actual.' lowercase + fragment). Unreadable."),
    "rev_1093": ("keep", "Outcome paraphrase + product-aware caveat (shoulder issues for Training Blueprint). Concise."),
    "rev_1088": ("remove", "Outcome line only, no customer color or context. No proof value."),
    "rev_1156": ("keep", "Multiple beats: decade-finished + nine weeks + jeans loose + 'Solid' closer. Varied rhythm."),
    "rev_1076": ("keep", "Late-thirties opener + six-kilo specific + sleep beat + 'turn up' closer."),
    "rev_1078": ("keep", "405lb deadlift at thirty-nine is the richest training-product proof in the heavy bucket. Worth the duplicate-opener cost."),
    "rev_1092": ("remove", "Outcome paraphrase only, no opener, no closer. No customer voice."),
    "rev_1053": ("keep", "Saturdays-back deadline + alumni-chat claim. Coherent collective story."),
    "rev_1192": ("keep", "Founder-block hook (meta-aware customer) + specific 28lb/five-month outcome."),
    "rev_1138": ("keep", "Seven-day-reset hook + jeans size + no-app proof. Within opener-cap."),
    "rev_1100": ("keep", "Statins-doctor hook is strong context for a 3-star. Alumni claim + product-aware caveat."),
    "rev_1052": ("remove", "Outcome line only ('Got the home gym in for under a grand. Commute gone.'). No customer voice."),
    "rev_1187": ("keep", "Second-kid hook + 9-week specific + product-aware caveat (shift-work templates for Nutrition)."),
    "rev_1037": ("remove", "Opener+outcome combo is two brand-coded phrases ('long bulk' + 'Twelve weeks. Lost the weight, kept the lifts, found the men.'). Too on-brand."),
    "rev_1158": ("remove", "Same brand-coded outcome as rev_1037 ('Twelve weeks. Lost the weight, kept the lifts, found the men.')."),
    "rev_1238": ("keep", "Back-injury context (two summers ago) + alumni-chat claim + 'Inputs are habit' closer."),
    "rev_1205": ("keep", "FAQ-read-before-buying hook (meta-aware) + specific eleven-week outcome + plausible closer."),
    "rev_1025": ("keep", "Friend-in-Collective referral hook + paraphrased outcome + clean closer."),
    "rev_1178": ("keep", "Lost-stone-wrong-way hook + specific 25kg deadlift gain + product-aware caveat."),
    "rev_1224": ("keep", "Long-procrastination hook (since 2022) + 8kg specific + caveat. Minor lowercase artifact in caveat sentence — fix in post."),
    "rev_1215": ("remove", "Multiple brand-coded phrases ('Five inputs, twelve weeks, eight men' + 'Train less, eat more, sleep first'). Too on-brand."),
    "rev_1103": ("keep", "Two-kids opener + 'Three months in. Gut went.' + 'Done. Sorted.' Tight British voice."),
    "rev_1154": ("remove", "Source-fragment 'So did the doubt. Found this instead.' was preserved but reads as a broken sentence in the cleaned form."),
    "rev_1019": ("keep", "Caring-for-parent hook is a distinct voice. Cohort + sleep beats. Plausible."),
    "rev_1220": ("remove", "Outcome paraphrase only, two sentences, no narrative."),
    "rev_1097": ("keep", "'My body got a vote. It voted against me.' is a strong distinctive opener metaphor."),
    "rev_1122": ("remove", "Third use of 'Did the seven-day reset first. Then bought the stack.' opener (rev_1138 and rev_1096 also use it). Triage to thin."),
    "rev_1077": ("keep", "Forties context + two waist sizes + 20kg deadlift + product-aware caveat."),
}

# Load the cleaned rows to enrich the triage output
with open(CLEANED, encoding="utf-8") as f:
    cleaned = list(csv.DictReader(f))
cleaned_by_id = {r["id"]: r for r in cleaned}

triage_rows = []
for rid, (decision, rationale) in TRIAGE.items():
    r = cleaned_by_id[rid]
    triage_rows.append({
        "id": rid,
        "name_display": r["name_display"],
        "rating_1_5": r["rating_1_5"],
        "internal_product_tag": r["internal_product_tag"],
        "anton_decision": decision,
        "anton_rationale": rationale,
        "stefan_decision": "",  # blank — Stefan fills binary override here
        "stefan_notes": "",  # blank
        "cleaned_quote_short": r["cleaned_quote_short"],
        "cleaned_quote_long": r["cleaned_quote_long"],
        "source_quote_long": r["quote_long"],
    })

with open(OUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "id", "name_display", "rating_1_5", "internal_product_tag",
        "anton_decision", "anton_rationale",
        "stefan_decision", "stefan_notes",
        "cleaned_quote_short", "cleaned_quote_long", "source_quote_long",
    ])
    writer.writeheader()
    writer.writerows(triage_rows)

# Stats
keeps = [r for r in triage_rows if r["anton_decision"] == "keep"]
removes = [r for r in triage_rows if r["anton_decision"] == "remove"]
print(f"Heavy triage written: {OUT}")
print(f"  Total: {len(triage_rows)}")
print(f"  Keep:   {len(keeps)} ({100*len(keeps)/len(triage_rows):.0f}%)")
print(f"  Remove: {len(removes)} ({100*len(removes)/len(triage_rows):.0f}%)")
print()
print("Removed rows by reason category:")
removal_reasons = {}
for r in removes:
    rationale = r["anton_rationale"]
    if "duplicate" in rationale.lower() or "third use" in rationale.lower():
        cat = "duplicate opener (cap-related)"
    elif "too short" in rationale.lower() or "no narrative" in rationale.lower() or "no customer color" in rationale.lower() or "outcome paraphrase only" in rationale.lower():
        cat = "too short / no narrative"
    elif "brand-vocab" in rationale.lower() or "brand-coded" in rationale.lower() or "on-brand" in rationale.lower():
        cat = "brand-vocab density"
    elif "broke" in rationale.lower() or "fragment" in rationale.lower() or "inconsistency" in rationale.lower():
        cat = "post-cleanup formatting issue"
    else:
        cat = "other"
    removal_reasons.setdefault(cat, []).append(r["id"])

for cat, ids in removal_reasons.items():
    print(f"  {cat}: {len(ids)} ({', '.join(ids)})")

print()
print("Pool implication after triage:")
print(f"  Original pool: 251 rows")
print(f"  After heavy-row removal: 251 - {len(removes)} = {251 - len(removes)} rows")
print(f"  After all-tier potential removal (UNCERTAIN+heavy): need separate UNCERTAIN review")
