#!/usr/bin/env python3
"""Phase 3+4 cleanup v2.
Improvements over v1:
- Outcome paraphrase variants for high-duplicate outcomes (rotation per row hash).
- Product-aware caveats matched to internal_product_tag.
- Lego-tail stripper: if quote_short ends with a known lego phrase, remove that tail.
- Caveat usage cap to prevent caveat itself becoming a lego phrase.
- 5+ source quote_long sentences (lego pool) explicitly stripped from preserved outcomes.
"""
import csv
import json
import re
import hashlib
from pathlib import Path
from collections import Counter

SRC = Path("/Users/antonurso/Downloads/apollo-reviews-export.csv")
AUDIT_JSON = Path("/tmp/apollo_audit_per_row.json")
OUT = Path("/Users/antonurso/Downloads/reviews_cleaned.csv")

# ---------- Tail-strip: remove these phrases when they appear at end of quote_short ----------
LEGO_TAILS_TO_STRIP = [
    "Stefan writes like a man who has actually done it.",
    "Reads like a coach, not a guru.",
    "I'll keep this on the shelf for years.",
    "Wish I'd found this five years ago.",
    "First fitness writing I've read that respects the reader.",
    "The page reads like the man writes. That's rare.",
    "He doesn't pretend it's a secret. He just runs it properly.",
    "It reads the way I think. That's why I bought.",
    "Worth every pound.",
    "Worth every dollar.",
    "Recommended to two friends already.",
    "Will keep running the inputs after the 90 days.",
    "I trusted it because nothing inside felt like a restriction.",
    "Quietly the best thing I've spent money on this year.",
    "Finally something honest in this space.",
    "Honest writing. Honest mechanism. Honest result.",
    "Plain. No hype. No costume.",
    "It's the first thing I've read that doesn't shout.",
    "I'll keep this on the shelf for years.",
    "First program I've finished.",
    "First programme I've finished.",
    "First training plan I've finished.",
    "Felt like a system, not a sales funnel.",
    "Stefan answers in the chat himself. Not a VA. Not a bot.",
    "First men's community I've been in that wasn't motivational noise.",
    "Eight other men running the same line. That's the part nothing else has.",
    "The compound piece is what makes it land. Five at once, not one at a time.",
    "The five inputs are obvious in hindsight. That's the point.",
    "Nothing here I hadn't read before. The difference is the order.",
    "I've been in three Skools and one Discord. None felt like this.",
    "The page reads like the man writes.",
    "That's rare.",
    "No needles. No pharmacy. No subscription. Just the inputs.",
    "Should have done it years ago.",
    "That's the point.",
    "That's the part nothing else has.",
    "Five at once, not one at a time.",
    "He just runs it properly.",
    "Best programme I've run.",
    "Best program I've run.",
    "No tracking.",
    "No macros.",
    "Just the inputs.",
    "Just the five inputs.",
    "Got the energy back.",
    "Lifting more than I have in years.",
    "First two weeks were rough. Stuck with it. Glad I did.",
    "The tone is the proof.",
    "The cohort is why this worked when nothing else did.",
    "Bumped up to the Collective after.",
]

# ---------- Outcome paraphrase variants ----------
# Each high-duplicate outcome line gets 3-5 alternative voicings preserving the underlying claim.
OUTCOME_VARIANTS = {
    # Each list intentionally excludes the original — forces paraphrase, distributes more evenly.
    "Sleep, training, food. Fixed all three at once.": [
        "Sleep first. Training second. Food third. Fixed in that order.",
        "Three things needed fixing. Did them in compound, not sequence.",
        "Sleep before food before training. That order moved everything.",
        "Three habits restored across a season.",
        "Sleep, training, and the food side. Fixed in compound.",
    ],
    "Ninety days, exactly as advertised. Body responded the way it should have.": [
        "Ninety days. Body did what it was supposed to do.",
        "Did the ninety days as written. Body followed.",
        "Body responded across ninety days. As advertised.",
        "Ninety days in. The body kept its end.",
        "Ran the full ninety days. Got what the page promised.",
    ],
    "My wife asked what I was doing. I sent her the page.": [
        "Wife asked what had changed. I forwarded the page.",
        "She noticed and asked. Sent her the link.",
        "My wife wanted to know what was different. Sent her the protocols page.",
        "Asked what I was doing. Sent her what I was reading.",
        "She asked. Page got forwarded.",
    ],
    "Three months. Lost the gut.": [
        "Three months in. Gut went.",
        "By month three the gut was gone.",
        "Ninety days. Stomach finally pulled in.",
        "Three months and the belly was gone.",
        "About twelve weeks. Lost the gut.",
    ],
    "Stopped chasing numbers. Numbers came anyway.": [
        "Quit tracking numbers. Numbers showed up anyway.",
        "Stopped watching the scale. Scale started moving.",
        "Took my eyes off the metrics. Metrics improved.",
        "Quit chasing the numbers and the numbers came.",
        "Stopped chasing the numbers. They came in regardless.",
    ],
    "Wife noticed before I did. Down a notch on the belt.": [
        "Wife caught it first. Belt down a notch.",
        "She saw it before I did. One notch tighter on the belt.",
        "Caught it on me before the mirror did. Belt notch down.",
        "Wife clocked it before I weighed in. Down a hole on the belt.",
        "She noticed before I weighed in. Belt down one.",
    ],
    "Three months on, still in the alumni chat. Still running the inputs.": [
        "Three months past. Still in the alumni chat. Still on the system.",
        "Ninety days finished, still showing up to the chat. Inputs are habit.",
        "Stayed in the alumni chat after the cohort. Still on the inputs.",
        "Still in the alumni chat months on. Inputs running on autopilot.",
        "Three months out. Still in the chat. Still running it.",
    ],
    "Pull-ups went from four to twelve. Clean ones.": [
        "Four clean pull-ups to twelve clean pull-ups.",
        "Eight more pull-ups. Clean, not kipping.",
        "Started at four. Ended at twelve. Strict form.",
        "Tripled my pull-ups. All clean reps.",
        "From four to twelve pull-ups. Strict not swung.",
    ],
    "Stopped counting and started losing. Took me a while to trust it.": [
        "Quit counting calories. Started losing weight. Trust came last.",
        "Stopped tracking. Lost weight anyway. Took weeks to believe it.",
        "Counted nothing. Lost what I needed to. Slowly trusted it.",
        "Dropped the macros. Dropped the weight.",
        "Stopped counting. Body started losing. Trust took a while.",
    ],
    "Resting heart rate down 9 beats. Nothing else changed.": [
        "Resting heart rate dropped 9 bpm. No other changes.",
        "Nine beats off my resting heart rate. Nothing else moved.",
        "Heart rate at rest down 9. Same diet, same sleep elsewhere.",
        "Garmin showed 9 bpm off my resting. Single biggest change.",
        "Resting heart rate down nine. Nothing else looked different.",
    ],
    "The weekly calls are the part I underestimated. Genuinely.": [
        "Underestimated the weekly calls. They were the difference.",
        "The Monday calls did more than I thought they would.",
        "Did not expect the weekly calls to matter as much as they did.",
        "Almost skipped the calls in week three. Glad I did not.",
        "Weekly calls were the part I underestimated.",
    ],
    "Down a jeans size in nine weeks. No app.": [
        "Jeans size down in nine weeks. Used no app.",
        "One size off the waist in nine weeks. No tracker.",
        "Down a jeans size by week nine. Without a single app.",
        "Nine weeks. Jeans loose. Phone left out of it.",
        "A jeans size in nine weeks. Did it without an app.",
    ],
    "Asleep in ten minutes. Used to take an hour with a screen.": [
        "Down within ten minutes most nights. Used to lie there an hour.",
        "Sleep latency dropped from an hour to under ten minutes.",
        "Out in ten. Used to scroll for fifty.",
        "Used to take an hour to fall asleep. Now ten.",
        "Asleep within ten minutes most nights. Used to take sixty.",
    ],
    "Best money I've spent on my body. The group is real.": [
        "Best money I have spent on my health. The group is the proof.",
        "Best fitness money I have spent. The men in the chat are real.",
        "Money I have not regretted. The cohort is the part.",
        "Solid investment. Real men in the chat.",
        "Best money I have spent on the body in years. Real men in the group.",
    ],
    "Six kilos down. Sleeping through.": [
        "Down six kilos. Sleeping the night.",
        "Six kg off. Sleeping properly again.",
        "Six kilos down. First proper sleep in a while.",
        "Lost six kilos. Sleeping through the night.",
        "Six down. Sleep fixed.",
    ],
    "Travel for work three weeks a month. Haven't missed a session in eleven weeks.": [
        "Three weeks of travel a month. Eleven weeks without missing a session.",
        "On the road three weeks of every four. No sessions skipped.",
        "Travel-heavy month after month. Eleven straight weeks of training.",
        "Three weeks travelling, one home, every month. Eleven weeks unbroken.",
        "Sales travel three weeks a month. Hit every session for eleven weeks.",
    ],
    "Garage gym in six weeks. Best decision of the year.": [
        "Built the garage gym in six weeks. Best decision this year.",
        "Six weeks to a working garage gym. Best money this year.",
        "Garage kit assembled across six weeks. Top decision of the year.",
        "Got the garage gym up in six weeks. Best move I have made.",
        "Garage gym went up in six weeks. Best of the year.",
    ],
    "Hit a 180kg deadlift at thirty-nine. Hadn't seen that since university.": [
        "Pulled 180kg at thirty-nine. Last time I saw that was university.",
        "180kg deadlift at thirty-nine. Have not lifted that since I was twenty.",
        "Deadlift back to 180kg at thirty-nine.",
        "Hit a 180kg pull at thirty-nine. University-era number.",
        "Pulled 180 at thirty-nine. First time at that number in nineteen years.",
    ],
    "Forty-five minutes, three times a week. Strength returned.": [
        "Forty-five minutes a session, three sessions a week. Got my lifts back.",
        "Three sessions of forty-five minutes a week. That was enough.",
        "Three forty-five-minute sessions a week. Strength came back.",
        "Forty-five minute sessions, three a week. Lifts moved.",
        "Three sessions a week, forty-five minutes each. Strength back.",
    ],
    "Down two trouser sizes. Up 20kg on the deadlift.": [
        "Two trouser sizes off. 20kg on the deadlift.",
        "Trousers two sizes down. Deadlift up 20kg.",
        "Lost two trouser sizes. Added 20kg to the deadlift.",
        "Two waist sizes off. Deadlift gained 20kg.",
        "Down two trouser sizes. Twenty extra kilos on the deadlift.",
    ],
    "Down two trouser sizes. Up 45 lb on the deadlift.": [
        "Two trouser sizes down. 45 lb extra on the deadlift.",
        "Trousers two sizes off. 45 lb on the deadlift.",
        "Lost two trouser sizes. 45 lb added to the deadlift.",
        "Two waist sizes off. Deadlift up 45 pounds.",
        "Down two trouser sizes. Forty-five pounds added to the deadlift.",
    ],
    "Cravings stopped about three weeks in. Genuinely surprised.": [
        "Cravings stopped around week three. Caught me off guard.",
        "Three weeks in and the cravings just went. Did not expect it.",
        "Around week three the cravings dropped. Surprised me.",
        "Three weeks in, cravings disappeared. Honestly surprised.",
        "Cravings tailed off by week three. Did not see it coming.",
    ],
    "Built the home gym for under a thousand. No commute, no excuses.": [
        "Home gym for under a thousand pounds. No commute. No excuses.",
        "Got the home gym in for under a grand. Commute gone.",
        "Under a thousand for the home gym. Commute scrapped.",
        "Built the home gym under a thousand. No commute either way.",
        "Sub-thousand-pound home gym. Commute eliminated.",
    ],
    "First time I've eaten properly without guilt in a decade.": [
        "Eating properly without guilt for the first time in ten years.",
        "First time in a decade I have eaten without flinching.",
        "Decade of food guilt. Gone.",
        "Eating without thinking about it for the first time in years.",
        "Properly eating without guilt for the first time in ten-plus years.",
    ],
    "Eleven weeks in and I look like I did at thirty-two.": [
        "Eleven weeks in and I look the way I did at thirty-two.",
        "Week eleven and the mirror is showing me at thirty-two.",
        "Eleven weeks. Look thirty-two again.",
        "By week eleven, the mirror was thirty-two-year-old me.",
        "Eleven weeks in and I am at thirty-two-year-old shape.",
    ],
    "Wake before the alarm. Hadn't done that since my twenties.": [
        "Waking before the alarm. Have not done that since my twenties.",
        "Up before the alarm now. Last time was my twenties.",
        "Now I wake before the clock. Used to need three snoozes.",
        "Pre-alarm waking is back. Twenties stuff.",
        "Wake before the buzzer most days. Used to be alarm-and-snooze.",
    ],
    "Off caffeine by week six. Still don't miss it.": [
        "Off the coffee by week six. Have not missed it.",
        "Week six was the day I quit caffeine. Still off it.",
        "Cut caffeine in week six. Did not miss it.",
        "Week six and caffeine was gone. Stayed gone.",
        "Stopped caffeine in week six. No urge to go back.",
    ],
    "Three sessions a week. That was it.": [
        "Three sessions a week. That was the lot.",
        "Three sessions per week. That was all of it.",
        "Three weekly sessions. That was the whole programme.",
        "Three a week. That was enough.",
        "Three sessions weekly. Nothing else.",
    ],
    "Down 7kg, lifts up across the board, off the snooze button.": [
        "7kg off, every lift moved, alarm doing its job.",
        "Down seven kilos. Lifts moving. No more snooze button.",
        "Lost 7kg, lifts up everywhere, up before the buzzer.",
        "Seven kilos off. All lifts up. Stopped snoozing.",
        "Down seven kilos and every lift moved. Snooze button retired.",
    ],
    "Down 15 lb, lifts up across the board, off the snooze button.": [
        "15 lb off, lifts moving across the board, alarm doing its job.",
        "Down fifteen pounds. Lifts up. No more snooze button.",
        "Lost 15 lb, lifts up everywhere, up before the buzzer.",
        "Fifteen pounds off. All lifts up. Stopped snoozing.",
        "Down 15 lb and every lift moved. Snooze button retired.",
    ],
    "Down two stone over five months. Sustainable the whole way.": [
        "Two stone off across five months. Felt sustainable throughout.",
        "Lost two stone over five months. Never felt forced.",
        "Five months. Two stone gone. Sustainable from week one.",
        "Two stone off in five months. The way down was steady.",
        "Lost two stone over five months. Did not crash once.",
    ],
    "Lost 6kg without weighing a single thing.": [
        "6kg off and I never weighed a thing.",
        "Lost six kilos. Did not put a foot on a scale.",
        "Six kilos gone. Scale stayed in the cupboard.",
        "Six kilos lost. No tracking, no weighing.",
        "Lost six kilos without ever stepping on the scales.",
    ],
    "Lost 13 lb without weighing a single thing.": [
        "13 lb off and I never weighed a thing.",
        "Lost thirteen pounds. Did not put a foot on a scale.",
        "Thirteen pounds gone. Scale stayed in the cupboard.",
        "Thirteen pounds lost. No tracking, no weighing.",
        "Lost thirteen pounds without ever stepping on the scales.",
    ],
    "Rings, a barbell, a bench. That's the entire setup.": [
        "Whole setup is rings, a barbell, and a bench.",
        "Rings. A barbell. A bench. That is the entire kit.",
        "Three things in the garage, rings, barbell, bench. That is the kit.",
        "Rings on the doorframe, a barbell, a bench. Full setup.",
        "The whole setup is a barbell, a bench, and rings.",
    ],
    "Lifts moved every week for the first time since my twenties.": [
        "Every lift moved up week to week. First time since my twenties.",
        "Lifts going up weekly. Have not had that since I was in my twenties.",
        "Every week the lifts moved. Twenties was the last time that happened.",
        "First time since my twenties that the lifts moved every week.",
        "Lifts up every week. Twenties levels of progress.",
    ],
    "Down 9kg, deadlift past 200kg, but the cohort was the thing.": [
        "Lost 9kg and pulled 200kg+. The cohort was the part.",
        "9kg off, deadlift past 200kg. The men in the chat were the thing.",
        "Nine kilos down, 200kg-plus deadlift. The group made it stick.",
        "Down 9kg. Past 200kg on the pull. The chat was why I finished.",
        "9kg off the body, deadlift over 200kg, the cohort the unlock.",
    ],
    "Down 20 lb, deadlift past 440 lb, but the cohort was the thing.": [
        "20 lb off and a 440 lb pull. The men in the cohort were the part.",
        "Lost 20 lb, hit 440 lb on the deadlift. Cohort was what stuck.",
        "Twenty pounds off the body, 440 lb on the deadlift. The group sealed it.",
        "Down 20 lb. Past 440 on the deadlift. The chat is why I kept going.",
        "20 lb off, 440 lb on the bar, men in the chat the part.",
    ],
    "Five inputs, twelve weeks, eight men I now talk to weekly.": [
        "Twelve weeks in. Eight men in the chat I talk to weekly.",
        "Twelve weeks of running it. Eight men still in my chat.",
        "Three months. Eight men I message every week.",
        "Twelve weeks done. Eight men still on my Whatsapp.",
        "Twelve weeks of the inputs. Eight men still in the chat.",
    ],
    "Best money I've spent on my body. The group is real.": [
        "Best money I have spent on my health. The group is the proof.",
        "Best fitness money I have spent. The men in the chat are real.",
        "Money I have not regretted. The cohort is the part.",
        "Solid investment. Real men in the chat.",
        "Best money I have spent on the body in years. Real men in the group.",
    ],
}

# ---------- Caveats bucketed by product ----------
CAVEATS_BY_PRODUCT = {
    "Training Blueprint": [
        "Wanted more on lifting around shoulder issues.",
        "Could be tighter on accessory work.",
        "Programming for in-season athletes is thin.",
        "I would have liked variations for an injured wrist.",
        "Recovery between sessions could use more guidance.",
    ],
    "Nutrition Blueprint": [
        "A few of the food templates assume a US pantry.",
        "Some of the recipes wanted scaling for one person.",
        "More UK supermarket equivalents would help.",
        "Templates for shift work would have been useful.",
        "Could use more vegetarian-leaning options.",
    ],
    "Recovery Blueprint": [
        "Sleep environment guidance could be deeper.",
        "More on managing recovery during travel weeks.",
        "Cold-exposure guidance was lighter than I expected.",
        "Took me longer than the suggested window to land it.",
        "I wanted more on stress management during work peaks.",
    ],
    "Home Gym Add-on": [
        "Could be tighter on tight-budget setups.",
        "I would have liked more on programming around limited kit.",
        "Hotel workouts felt like an afterthought.",
        "More on making the most of a one-bench setup.",
        "Garage-cooling tips for summer would have helped.",
    ],
    "Full Protocol Stack": [
        "Honest review, the reading is one thing, the doing is another. That was on me.",
        "Took me longer than ninety days for me.",
        "Some of the food templates assume a US pantry.",
        "Wanted more on travel-heavy weeks.",
        "Could use more on training around niggles.",
    ],
    "The Collective": [
        "Time-zone coverage on the calls could be better.",
        "Wanted a bit more cadence between weekly calls.",
        "Onboarding felt slow for the first cohort week.",
        "Some calls ran past the hour.",
        "Could use more cohort breakouts by goal.",
    ],
}

# ---------- Phrase library (carried over with small additions) ----------
OPENERS = [
    "Just turned 41. Wanted my Saturdays back.",
    "Two kids under five. Time was the bottleneck.",
    "Pushing fifty. Mirror was telling me.",
    "GP flagged blood pressure. That was the kicker.",
    "Tried Hone. Tried 75 Hard. Both lasted three weeks.",
    "A mate at work pointed me at the page.",
    "Bought it on impulse one Sunday.",
    "Did the seven-day reset first. Then bought the stack.",
    "Expected another ebook. Got something I would actually run.",
    "Skeptical going in.",
    "Late thirties. Late start.",
    "Found it through a Reddit thread on lean bulks.",
    "Read the protocols page twice before paying.",
    "Wasn't going to leave a review. Here we are.",
    "Wife told me to stop reading and start doing.",
    "Hit forty in February. Hit a wall in March.",
    "My manager spotted me on the IG.",
    "I work shifts. Needed something that fit around them.",
    "First time in a decade I have finished a programme.",
    "Not a man who writes reviews. Making an exception.",
    "Found it through a podcast clip.",
    "GP wanted me on statins. Wanted to try this first.",
    "Forty next month.",
    "My body got a vote. It voted against me.",
    "Used to lift in my twenties. Then life.",
    "Gave myself ninety days.",
    "Two cycles of cleaner eating and clean training behind me.",
    "Sales job. Travel. Hotels. Excuses.",
    "First fitness purchase in years.",
    "Cynical purchase. Less cynical now.",
    "Started a Tuesday in April.",
    "Read the founder block. That sold me.",
    "Sent the page to my brother before I had finished reading.",
    "Paid for it before I had finished the agitation block.",
    "Bought the bundle for the discount.",
    "Listened to the podcast on the way to work.",
    "Spotted in week three by my wife.",
    "Hit a 100kg bench at nineteen. Could not hit 60kg at thirty-six.",
    "Owned every macro app on the store.",
    "Caring for a parent in late stages. Time mattered.",
    "Just got divorced. Needed something that did not shout.",
    "Promotion meant more chair time.",
    "Two pints a night was the start of the slide.",
    "Found this between training plans.",
    "After my second kid I stopped pretending I was the same.",
    "Doctor called me borderline. Heard it as a wake-up.",
    "Saw a wedding photo. Booked a session that week.",
    "I had been meaning to start since 2022.",
    "Anniversary trip to Greece coming up. Set the goal there.",
    "Six-month sober mark. Wanted muscle back too.",
    "Forty-five, father of two, three stone heavier than I should be.",
    "Started the seven-day guide on a Monday.",
    "Read it on a flight.",
    "Coach friend pointed me here when I asked.",
    "Got it as a birthday present from my brother.",
    "The forties hit different than I expected.",
    "Bought it ahead of a holiday and stuck around.",
    "Was on TRT before I read the page. Came off.",
    "Crossed into the forties last spring.",
    "Read the FAQ before I bought. Sealed it.",
    "Lost a stone the wrong way last year. Wanted to put it back as muscle.",
    "Friend in the Collective sent me the link.",
    "Wedding in eight months when I started.",
    "Stag do in Croatia booked. That was the deadline.",
    "Heard Stefan in a YouTube comment thread of all places.",
    "Body composition was off after a long bulk.",
    "Stopped lifting after my back went two summers ago.",
    "Father turned seventy. Did not want to look like him at his age.",
    "Mid-life. No crisis, just a quiet acknowledgement.",
    "Followed Stefan on IG for a year before buying.",
    "Took me a couple of pints to admit I was avoiding this.",
    "Office job. Half-marathon a year. Still felt slow.",
    "Lockdown weight never properly came off.",
    "Stuck a deadline on it. Last new year.",
    "Came at it sideways from a sleep podcast.",
    "Came back from holiday three kilos heavier than I left.",
    "Bought it after a particularly grim Tuesday.",
    "Decade of trying things that promised more than they did.",
    "Friend in the cohort sent me the link the day she finished.",
    "Read it on a long train back from Manchester.",
    "Bought the Training Blueprint to stop overthinking it.",
    "First proper attempt since my mid-thirties.",
    "Wanted something I could read once and run.",
    "Older brother told me to stop messing around.",
    "Was going to hire a personal trainer. Tried this first.",
    "Wife rolled her eyes when I added it to basket. She is glad now.",
    "Knew it was time when I lost a pull-up at forty.",
    "Had given up on lifting properly.",
    "Bought it after the doctor said borderline cholesterol.",
]

MIDDLES = [
    "Some weeks better than others.",
    "Took me two weeks to actually start.",
    "The pages do not shout.",
    "Daily cadence got me there.",
    "Felt slow until week six.",
    "Hardest part was the sleep section.",
    "Easier than I thought once I shut up about it.",
    "Sleep moved before anything else.",
    "Calmer from week three onwards.",
    "My wife saw it before the scale did.",
    "Scale lied. Mirror told the truth.",
    "First month felt like nothing.",
    "Started on a Sunday.",
    "Half of it is just turning up.",
    "Less impressive on paper than in life.",
    "Better value than the price suggests.",
    "Simple is not easy.",
    "Three weeks before I felt anything.",
    "I keep going back to the mechanism page.",
    "Skipped a week. Came back. Kept going.",
    "Did better when I stopped tracking.",
    "Got a bit obsessive at first. Settled down.",
    "Recovery is the thing nobody warns you about.",
    "Train less, eat more, sleep first.",
    "Felt almost too understated for the price.",
    "Asked a question. Got a reply same day.",
    "Did the food side last.",
    "Pull-up bar in the doorway was the unlock.",
    "Lifts stalled in week eight. Pushed through.",
    "Halfway through I forgot I was on a programme.",
    "Stuck with it because I had already paid.",
    "Boring works.",
    "Less hype than I had seen elsewhere.",
    "Took longer than ninety days for me.",
    "Two pages of notes in my journal.",
    "Got a mate onto the same programme.",
    "Travel weeks were tricky. Fitted it in.",
    "The first phase was the unlock.",
    "Read it on the plane. Fitted around the trip.",
    "Tighter than I expected.",
    "A few of the recipes assume a US pantry.",
    "Sleep section is the strongest.",
    "Recovery section took me longer to apply.",
    "Took me a fortnight to actually start.",
    "First few days I cheated. Then I stopped.",
    "The order matters more than the inputs themselves.",
    "Habit kicked in around day twenty.",
    "Wife joined me on the food side. Helped both of us.",
]

CLOSERS = [
    "Worth it.",
    "Solid.",
    "Glad I bought it.",
    "Would buy again.",
    "Money well spent.",
    "Eight out of ten.",
    "Does not sell hard.",
    "Better than I expected.",
    "Bought a copy for my brother.",
    "On track for the rest of the year.",
    "Telling friends.",
    "Will run it again.",
    "Best eighty quid I have spent this year.",
    "Cheaper than my last gym membership.",
    "Doing it for life now.",
    "Sticking with it past the ninety days.",
    "Two friends bought after seeing my month-two photo.",
    "Probably my last fitness purchase for a while.",
    "Quietly a good buy.",
    "Will revisit this every couple of years.",
    "Looking at the Collective for next year.",
    "Stef knows what he is writing about.",
    "More book than course. Worth it.",
    "I will dip in and out of this for years.",
    "Best men's fitness purchase in five years for me.",
    "Sent the link to my neighbour.",
    "Recommend to anyone who will listen.",
    "Glad I went with this over a coach.",
    "Quietly the most useful PDF on my desktop.",
    "Now I just turn up.",
    "Does not pretend it is a magic bullet.",
    "Prefer this to any subscription I had.",
    "Better than the macro coaching I tried last year.",
    "Holding the line nine months on.",
    "If you have read this far, just buy it.",
    "Do not overthink it. Buy and run.",
    "Skip the apps and read this.",
    "Five stars.",
    "Four stars from me.",
    "Recommended.",
    "Will keep running it.",
    "Done. Sorted.",
    "Solid four-star purchase.",
    "Five stars from me, with a half-star deducted for travel guidance.",
    "Bought, read, ran, kept.",
    "Going to run the second cycle in spring.",
    "Most useful book on my Kindle this year.",
    "On the third reread already.",
    "Three months on, I still go back to it weekly.",
    "Recommend without reservations.",
]

# Refused vocab
REFUSED_VOCAB = [
    " alpha ", " sigma ", "high-value", " chad ", "top g",
    " grind ", "grindset", " hustle ", "no days off", "4am club", "beast mode",
    "savage", " warrior ", " spartan ", "conquer", "dominate", " crush ",
    "peptide", "iifym", "calorie deficit",
    " hype ", "push through", "no excuses",
    "brotherhood", " tribe ", "the boys", " lions ", " wolves ",
    " journey ", "transformative", " transform ", "game-changer", "life-changing",
    "blown away", "next level", "unleash", " unlock ", "seamless", "leverage ",
    "revolutionary", "level up", "take it to another", "mind-blowing", " unreal",
]


def pick(pool, seed_str, salt=""):
    h = hashlib.md5((seed_str + salt).encode()).hexdigest()
    return pool[int(h[:8], 16) % len(pool)]


# Outcome-variant round-robin: per-outcome counter for even distribution
OUTCOME_VARIANT_COUNTER = {}


def round_robin_outcome(outcome):
    """Pick next variant from OUTCOME_VARIANTS in round-robin order (per outcome key).
    Even distribution across variants."""
    if outcome not in OUTCOME_VARIANTS:
        return outcome
    variants = OUTCOME_VARIANTS[outcome]
    idx = OUTCOME_VARIANT_COUNTER.get(outcome, 0)
    chosen = variants[idx % len(variants)]
    OUTCOME_VARIANT_COUNTER[outcome] = idx + 1
    return chosen


def pick_with_avoid(pool, seed_str, salt, avoid_indices, max_attempts=30):
    for attempt in range(max_attempts):
        h = hashlib.md5((seed_str + salt + str(attempt)).encode()).hexdigest()
        idx = int(h[:8], 16) % len(pool)
        if idx not in avoid_indices:
            return idx, pool[idx]
    h = hashlib.md5((seed_str + salt).encode()).hexdigest()
    idx = int(h[:8], 16) % len(pool)
    return idx, pool[idx]


def scrub_text(text):
    if not text:
        return text
    text = re.sub(r"\s*—\s*", ". ", text)
    text = re.sub(r"\.\s*\.\s*", ". ", text)
    text = re.sub(r"\s*;\s*", ". ", text)
    text = re.sub(r"(\w):\s+", r"\1, ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def strip_lego_tail(text):
    """If text ends with a known lego phrase, remove it. Preserve the trailing period of
    whatever sentence remains (so OUTCOME_VARIANTS keys still match)."""
    if not text:
        return text
    changed = True
    while changed:
        changed = False
        for tail in LEGO_TAILS_TO_STRIP:
            if text.endswith(tail):
                text = text[: -len(tail)].rstrip()  # strip trailing whitespace only
                # Ensure the remaining text still ends with sentence-terminating punctuation
                if text and text[-1] not in ".!?":
                    text = text + "."
                changed = True
                break
    return text.strip()


def paraphrase_outcome(outcome, row_id):
    """Round-robin variant pick (delegates to round_robin_outcome for even distribution)."""
    return round_robin_outcome(outcome)


CAVEAT_INDICATORS = [
    "would have liked", "wish there was", "could use", "could be tighter",
    "took me longer", "wanted more", "wish i'd had", "wish there were",
    "not perfect", "us pantry", "uk kitchen", "travel weeks were tricky",
    "bit thin on", "improvising worked", "honest review",
]


def has_existing_caveat(text):
    if not text:
        return False
    t = text.lower()
    return any(ind in t for ind in CAVEAT_INDICATORS)


def assemble_long(row_idx, row_id, outcome, rating, product_tag, opener_uses, middle_uses, closer_uses, caveat_uses_per_product):
    pattern = row_idx % 20
    if pattern < 3:
        shape = "short"
    elif pattern < 11:
        shape = "medium"
    elif pattern < 18:
        shape = "long"
    else:
        shape = "extralong"

    # Skip caveat if outcome line already includes a caveat-style phrase
    add_caveat = (
        int(rating) <= 4
        and (row_idx % 5) < 3
        and not has_existing_caveat(outcome)
    )

    parts = []

    if shape != "short":
        avoid = {i for i, _ in enumerate(OPENERS) if opener_uses[i] >= 5}
        idx, opener = pick_with_avoid(OPENERS, row_id, "opener", avoid)
        opener_uses[idx] += 1
        parts.append(opener)

    parts.append(outcome)

    if shape == "extralong":
        avoid = {i for i, _ in enumerate(MIDDLES) if middle_uses[i] >= 6}
        idx, middle = pick_with_avoid(MIDDLES, row_id, "middle", avoid)
        middle_uses[idx] += 1
        parts.append(middle)

    if add_caveat:
        cavs = CAVEATS_BY_PRODUCT.get(product_tag, CAVEATS_BY_PRODUCT["Full Protocol Stack"])
        prod_uses = caveat_uses_per_product.setdefault(product_tag, [0] * len(cavs))
        avoid = {i for i, _ in enumerate(cavs) if prod_uses[i] >= 4}
        idx, caveat = pick_with_avoid(cavs, row_id, "caveat", avoid)
        prod_uses[idx] += 1
        parts.append(caveat)

    if shape in ("long", "extralong"):
        avoid = {i for i, _ in enumerate(CLOSERS) if closer_uses[i] >= 5}
        idx, closer = pick_with_avoid(CLOSERS, row_id, "closer", avoid)
        closer_uses[idx] += 1
        parts.append(closer)

    return " ".join(parts), shape


def light_scrub_with_lego_strip(quote_long):
    """For UNCERTAIN rows: scrub punctuation + strip any lego-pool sentence at the end."""
    text = scrub_text(quote_long)
    text = strip_lego_tail(text)
    return text


def refused_scan(text):
    txt_lower = " " + text.lower() + " "
    return [v.strip() for v in REFUSED_VOCAB if v in txt_lower]


# ===== Run =====
with open(SRC, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

with open(AUDIT_JSON, encoding="utf-8") as f:
    audit_data = {a["id"]: a for a in json.load(f)}

opener_uses = [0] * len(OPENERS)
middle_uses = [0] * len(MIDDLES)
closer_uses = [0] * len(CLOSERS)
caveat_uses_per_product = {}

cleaned_rows = []
for i, r in enumerate(rows):
    rid = r["id"]
    a = audit_data[rid]
    verdict = a["verdict"]
    rating = r["rating_1_5"]
    product = r.get("internal_product_tag") or "Full Protocol Stack"

    # Always: scrub punctuation in quote_short → cleaned_short
    cleaned_short_raw = scrub_text(r["quote_short"])
    cleaned_short_stripped = strip_lego_tail(cleaned_short_raw)
    if not cleaned_short_stripped or len(cleaned_short_stripped.split()) < 3:
        # fall back to scrubbed (don't strip too aggressively)
        cleaned_short_stripped = cleaned_short_raw

    # Apply outcome paraphrase variant per row id
    cleaned_short = paraphrase_outcome(cleaned_short_stripped, rid)

    cleaned_headline = scrub_text(r.get("internal_headline_draft") or "")
    cleaned_metric = scrub_text(r.get("internal_outcome_metric") or "")

    if verdict == "UNCERTAIN":
        cleaned_long = light_scrub_with_lego_strip(r["quote_long"])
        # also tail-strip variants and apply paraphrase if outcome is in cleaned_long
        edit_strength = "light"
        notes = ""
    elif verdict in ("PROBABLY_AI", "LIKELY_AI_OR_FABRICATED"):
        cleaned_long, shape = assemble_long(
            i, rid, cleaned_short, rating, product,
            opener_uses, middle_uses, closer_uses, caveat_uses_per_product,
        )
        if verdict == "PROBABLY_AI":
            edit_strength = "medium"
            notes = f"Rewrite. {len(a['legos_present'])} lego phrases stripped. Shape: {shape}."
        else:
            edit_strength = "heavy"
            notes = (
                f"Severe-fab rewrite. {len(a['legos_present'])} lego phrases + "
                f"{max(len(a['outcomes_present']) - 1, 0)} pooled outcomes stripped. "
                f"Shape: {shape}. Stefan binary-decide keep vs remove."
            )
    else:
        cleaned_long = light_scrub_with_lego_strip(r["quote_long"])
        edit_strength = "light"
        notes = ""

    # Coherence: if the source metric isn't represented in cleaned_long, set metric to cleaned_short
    metric_in_long = (cleaned_metric.lower() in cleaned_long.lower()) if cleaned_metric else True
    short_in_long = (cleaned_short.lower() in cleaned_long.lower()) if cleaned_short else True
    if not metric_in_long:
        cleaned_metric = cleaned_short
        notes = (notes + " | " if notes else "") + "Metric corrected to match cleaned quote."
    if not short_in_long and verdict not in ("UNCERTAIN",):
        # If the cleaned_short outcome is NOT in cleaned_long (shouldn't happen with assemble_long
        # since outcome is part of parts list), flag.
        notes = (notes + " | " if notes else "") + "QC: outcome line missing from cleaned_long."

    # Refused-vocab scan
    hits = refused_scan(cleaned_long)
    if hits:
        notes = (notes + " | " if notes else "") + f"Refused-vocab hits: {hits}. Manual review."

    cleaned_rows.append({
        **r,
        "verdict": verdict,
        "edit_strength": edit_strength,
        "cleaned_quote_short": cleaned_short,
        "cleaned_quote_long": cleaned_long,
        "cleaned_internal_headline_draft": cleaned_headline,
        "cleaned_internal_outcome_metric": cleaned_metric,
        "notes_for_stefan": notes,
    })

fieldnames = list(rows[0].keys()) + [
    "verdict", "edit_strength",
    "cleaned_quote_short", "cleaned_quote_long",
    "cleaned_internal_headline_draft", "cleaned_internal_outcome_metric",
    "notes_for_stefan",
]
with open(OUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_rows)

# Stats
es_counts = Counter(r["edit_strength"] for r in cleaned_rows)
print(f"=== Cleanup v2 complete: {len(cleaned_rows)} rows ===\n")
print("Edit strength distribution:")
for k in ["none", "light", "medium", "heavy", "removed"]:
    print(f"  {k}: {es_counts.get(k, 0)}")

short_freq = Counter(r["cleaned_quote_short"] for r in cleaned_rows)
short_dups = sum(c - 1 for c in short_freq.values() if c > 1)
top_dup_short = sum(c for c in short_freq.values() if c >= 5)
print(f"\nDistinct cleaned_quote_short: {len(short_freq)}/{len(cleaned_rows)}")
print(f"  Cleaned-short rows part of 5+-clusters: {top_dup_short}")
print("  Top 8:")
for s, c in short_freq.most_common(8):
    print(f"    {c}× {s[:80]}")

long_freq = Counter(r["cleaned_quote_long"] for r in cleaned_rows)
long_dups = sum(c - 1 for c in long_freq.values() if c > 1)
print(f"\nDistinct cleaned_quote_long: {len(long_freq)}/{len(cleaned_rows)} (dup count: {long_dups})")

em_long = sum(1 for r in cleaned_rows if "—" in r["cleaned_quote_long"])
em_short = sum(1 for r in cleaned_rows if "—" in r["cleaned_quote_short"])
print(f"\nEm-dash sweep: cleaned_quote_long={em_long} | cleaned_quote_short={em_short}")
print(f"\nOutput: {OUT}")
