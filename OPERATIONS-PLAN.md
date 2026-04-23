# Urso & Co — Operations Plan

**Single source of truth for how the studio operates across Claude Design, Claude Code, and Cowork.**
**Version** 1.1 · **Last updated** 2026-04-23

Paste this document into any agent, any session, and it will have full context to continue the work correctly.

---

## 0. How to use this file

- If anything elsewhere conflicts with this document, **this document wins** — unless a later dated revision has been committed to `stefan-studio/main`.
- Any agent reading this (Claude Design, Claude Code, or a Cowork skill) should treat sections 1–3 as canonical context and sections 4–6 as the executable plan + rules.
- Do not skip steps. Do not parallelise unless a step says parallelisable. Each step assumes the prior one is complete.

---

## 1. The three surfaces and what they own

| Surface | Role | Reads from repo | Writes to repo |
|---|---|---|---|
| **Claude Design** (design bench project) | Visual exploration, hi-fi mocks, variations, brand-kit evolution. | `brand-kit/`, `skills/` | Proposes via chat; human commits. |
| **Claude Code** | Production engineering. Site build, deploys, git workflows, long-lived maintenance. | `brand-kit/`, `skills/`, `site/` | Commits directly, with human review. |
| **Cowork** | Runtime ops + copy generation via skills. | `brand-kit/`, `skills/` via git-sync. | Never writes. Output is ephemeral per invocation. |

---

## 2. The single source of truth

One private git monorepo: **`stefan-studio`** on GitHub.

```
stefan-studio/
├── brand-kit/                      ← source of truth for BRAND
│   ├── 01-docs/                    (foundation, copy bank, voice system, SKILL, README)
│   ├── 02-tokens/                  (colors_and_type.css)
│   ├── 03-fonts/                   (self-hosted Source Serif 4)
│   ├── 04-logos/                   (wordmark SVGs + favicon)
│   ├── 05-preview/                 (design-system review cards)
│   ├── 06-holding-site/            (reference HTML implementation)
│   ├── 07-deck/                    (12-slide brand deck)
│   ├── index.html                  (visual kit overview)
│   ├── README.md
│   ├── CHANGELOG.md
│   ├── COWORK-INSTALL.md
│   └── CLAUDE-CODE-REVIEW-PROMPT.md
│
├── skills/                         ← source of truth for SKILLS
│   ├── copy.md                     (universal craft skill)
│   ├── copy-urso.md                (Urso brand overlay)
│   └── README.md                   (skills index + versioning policy)
│
├── site/                           ← production site (added in Phase 5)
│   └── (Astro project)
│
├── OPERATIONS-PLAN.md              ← THIS FILE
├── README.md                       ← monorepo overview
└── .gitignore
```

**Rules:**

1. **Nothing outside this repo is authoritative.** Not Cowork's UI. Not Claude Code's local skill cache. Not this design project. If it isn't in git, it doesn't count.
2. **Brand and skills travel together.** When brand bumps v1.5 → v1.6, skills re-version to match.
3. **Every consumer is read-only with respect to the repo.** Cowork syncs. Claude Code points at it. Design references it. No surface writes back except via explicit human-reviewed commits.

---

## 3. Current state (2026-04-22)

- **Design project (Claude Design):** Complete brand-kit v1.5.2 assembled; pending export. Includes a working `copy-urso.md` skill (currently at `brand-kit/08-cowork/copy-urso.md`; will move to `skills/` during install).
- **Claude Code:** A `/copy` skill exists; maturity unconfirmed — a 3-task test happens in Step 2.
- **Cowork:** A `/copy` skill has been pasted in manually. Will be replaced by a git-synced version during install.
- **GitHub:** `stefan-studio` repo may or may not exist — Step 1 handles it.
- **Live site:** `ursoandco.co.uk` not yet live; holding page designed but not deployed.

---

## 4. The install plan — sequential, ten steps

Estimated total time: **3–5 hours across 1–2 days**.

### Phase 1 — Foundation

#### Step 1 — Create the empty git repo
**Where:** GitHub · **Time:** 10 min · **Who:** You

1. Create a **private** repo named `stefan-studio`.
2. Do NOT initialise with README, .gitignore, or license — those come in Step 4.
3. Copy the SSH URL (`git@github.com:YOURUSER/stefan-studio.git`).

**Exit:** Empty private repo exists at a known URL.

---

#### Step 2 — Reconcile skill files to canonical versions
**Where:** Your local machine · **Time:** 20 min · **Who:** You

1. **Test Claude Code's `/copy` on three tasks:**
   - *"Write one sentence about a fictional coffee brand."*
   - *"Draft a 50-word product description for a reusable water bottle."*
   - *"Write a LinkedIn post headline about hiring your first engineer."*
   If output is consistently clean without hand-editing, it's mature. If not, iterate on the prompt until it is.
2. **Save Claude Code `/copy` source** to Desktop as `copy.md`.
3. **Save Cowork `/copy` source** to Desktop as `copy-cowork-current.md`.
4. **Diff the two.** If identical, delete `copy-cowork-current.md`. If different, merge any salvageable improvements from Cowork into `copy.md` (Claude Code wins by default — that's where you iterate), then delete the Cowork file.
5. **Download** `brand-kit/08-cowork/copy-urso.md` from this design project to Desktop as `copy-urso.md`.

**Exit:** Two files on Desktop — `copy.md` (canonical craft) + `copy-urso.md` (canonical overlay). Do NOT install them anywhere yet.

---

#### Step 3 — Export the brand-kit ZIP
**Where:** Claude Design (this project) · **Time:** 2 min · **Who:** You

1. Grab the most recent "Urso & Co Brand Kit v1.5.2 (ZIP)" download card, or ask me to regenerate it.
2. Save to Desktop as `brand-kit.zip`.

**Exit:** `brand-kit.zip` on Desktop alongside `copy.md` and `copy-urso.md`.

---

### Phase 2 — Seed the monorepo

#### Step 4 — Claude Code seeds the repo
**Where:** Claude Code · **Time:** 30 min · **Who:** Claude Code with the prompt in §7

1. Open a fresh Claude Code session in a directory where you want the local clone (e.g. `~/projects/`).
2. Attach the three files from your Desktop (`brand-kit.zip`, `copy.md`, `copy-urso.md`).
3. Paste the "Seed prompt" from §7 of this document, replacing `GIT_REPO_URL` with your actual URL from Step 1.
4. Claude Code clones, structures, commits in logical chunks, pushes.
5. Confirm on GitHub that the tree matches the structure in §2.

**Exit:** `stefan-studio` on GitHub is populated correctly.

---

### Phase 3 — Wire Cowork

#### Step 5 — Replace Cowork's manual knowledge + skills with git-synced versions
**Where:** Cowork · **Time:** 30 min · **Who:** You

1. In Cowork's knowledge workspace, **delete any manually uploaded `brand-kit/`**.
2. In Cowork's skills manager, **delete the manually pasted `/copy` skill**.
3. Add a git source connector pointing at `stefan-studio` (use Cowork's source-integrations or knowledge-sync feature).
4. Configure two mounts from that source:
   - Knowledge: `stefan-studio/brand-kit/` → `/knowledge/stefan-brand/`
   - Skills: `stefan-studio/skills/` → Cowork's skills directory
5. Sync cadence: **on-push** if webhooks supported, else **hourly**.
6. Trigger initial sync. Verify in Cowork's UI:
   - `copy` skill visible.
   - `copy-urso` skill visible.
   - `brand-kit/` knowledge indexed.

**Test invocation:**
> `/copy-urso — Draft a LinkedIn post announcing the £1,497 audit. UK DTC founders. ~150 words.`

Expected response:
1. **Final copy** — ~150 words, bank CTAs + bank pricing language.
2. **Trace log** — table of bank strings used.
3. **Queue for Copy Bank v2** — novel strings flagged.

If blocks 2 or 3 are missing, skill didn't load — debug paths.

**Exit:** `/copy-urso` works end-to-end from git-synced sources.

---

### Phase 4 — Design the site

#### Step 6 — Build remaining site screens
**Where:** Claude Design (this project) · **Time:** 2–3 sessions · **Who:** Me, with your sign-off per screen

Create a new folder `site-design/` sibling to `brand-kit/`. Build in this order, 2–3 variations each:

1. Services page (five-tier offer ladder).
2. About (founder story).
3. Contact / booking (path to £1,497 audit).
4. Case studies shell (placeholder until material clears).

Each screen uses `brand-kit/02-tokens/colors_and_type.css`, pulls copy from `component-copy-bank.md` where possible. Novel copy → run `/copy-urso` in Cowork, paste result back.

**Exit:** All screens signed off.

---

#### Step 7 — Export site handoff package
**Where:** Claude Design (this project) · **Time:** 10 min · **Who:** Me

1. ZIP the finalised `site-design/` folder.
2. Generate `CLAUDE-CODE-SITE-BUILD.md` — handoff prompt for Claude Code to convert static HTML → Astro.

**Exit:** `site-design.zip` + `CLAUDE-CODE-SITE-BUILD.md` on your Desktop.

---

### Phase 5 — Ship to production

#### Step 8 — Claude Code builds the Astro site
**Where:** Claude Code · **Time:** ~1–2 hours Claude Code work · **Who:** Claude Code

1. Fresh session inside your local `stefan-studio/` clone.
2. Attach `site-design.zip`.
3. Paste `CLAUDE-CODE-SITE-BUILD.md`.
4. Claude Code scaffolds Astro into `site/`, converts pages, wires tokens, wires form handler (Resend), configures Cloudflare Pages, commits, pushes.

**Exit:** `site/` is a working Astro project on main. Local `npm run build` succeeds.

---

#### Step 9 — Deploy to Cloudflare Pages
**Where:** Cloudflare dashboard · **Time:** 20 min · **Who:** You

1. Cloudflare Pages → Create project → Connect to GitHub → pick `stefan-studio`.
2. Build: `npm run build` in `site/`, output `site/dist/`.
3. Env vars: add `RESEND_API_KEY` (or whichever form service was chosen).
4. First deploy runs in ~2 min.
5. Add custom domain `ursoandco.co.uk`. Update DNS at your registrar per Cloudflare's instructions.
6. Wait for propagation. Verify `https://ursoandco.co.uk` loads.

**Exit:** Live site on custom domain.

---

### Phase 6 — Close the sync loop

#### Step 10 — Point Claude Code at the git-synced skills
**Where:** Your local machine · **Time:** 10 min · **Who:** You

Goal: Claude Code's `/copy` is the same file Cowork reads.

Option A (if Claude Code supports configurable skill folder): point it at `~/projects/stefan-studio/skills/`.
Option B (if Claude Code reads `~/.claude/skills/` only): symlink:
```bash
ln -s ~/projects/stefan-studio/skills/copy.md ~/.claude/skills/copy.md
ln -s ~/projects/stefan-studio/skills/copy-urso.md ~/.claude/skills/copy-urso.md
```
Option C (fallback): pre-commit hook that copies `skills/*.md` into Claude Code's cache on every commit.

Verify: `/copy` in Claude Code and `/copy` in Cowork produce identical output for the same task. If they differ, sync is broken.

**Exit:** One skill file, two consumers, zero drift.

---

## 5. The five rules of ongoing operation

1. **Brand and skill changes originate in Claude Design (this project).** Never edit `brand-kit/` or `skills/` from Claude Code or Cowork directly.
2. **Every kit/skill change bumps the version.** Update `CHANGELOG.md` and frontmatter. Skills match the brand version they depend on.
3. **Commits to `main` propagate automatically.** Cloudflare rebuilds the site. Cowork re-syncs. Claude Code's symlink reflects the change on next use.
4. **All published copy goes through `/copy-urso` in Cowork.** No free-generating brand copy anywhere else — including this design project.
5. **Quarterly audit** — run `brand-kit/CLAUDE-CODE-REVIEW-PROMPT.md` against the kit. Fix any drift it finds.
6. **Session-start ritual.** Any Claude Design or Cowork session that will produce on-brand output reads `project-rules.md` + `brand-kit/INDEX.md` + the frontmatter of `brand-kit/01-docs/foundation-brief.md` and `skills/copy-urso.md` at the top of the session, and quotes their first lines back to the user. This catches version drift before any work is proposed.

---

## 6. What to do right now

Your immediate sequence, no decisions needed:

1. ✅ Step 1 — Create the empty GitHub repo.
2. ✅ Step 2 — Reconcile `/copy` skill files to one canonical `copy.md`.
3. ✅ Step 3 — Grab `brand-kit.zip` from this project.
4. ↩︎ Come back here. Say *"ready for Step 4."* I'll confirm the Claude Code seed prompt in §7 is current, then you run it in Claude Code.

Everything past Step 4 flows from the seed being correct. Don't run Step 5 until Step 4 is confirmed on GitHub.

---

## 7. Claude Code seed prompt (for Step 4)

Paste **exactly this** into Claude Code after attaching `brand-kit.zip`, `copy.md`, `copy-urso.md`. Replace only the `GIT_REPO_URL` placeholder.

```markdown
# Seed stefan-studio monorepo

You are setting up the initial state of the `stefan-studio` monorepo. Context: this is the single source of truth for Urso & Co — a UK AI operations studio for £1–10M DTC brands. The repo holds the brand kit, skills, and (later) the production site.

I have attached three files:
- `brand-kit.zip` — complete brand kit v1.5.2.
- `copy.md` — canonical universal `/copy` craft skill.
- `copy-urso.md` — Urso brand overlay skill.

## Task

1. Clone the empty repo at `GIT_REPO_URL` into the current directory.

2. Build this structure inside the clone:
   ```
   stefan-studio/
   ├── brand-kit/           (extract from brand-kit.zip)
   ├── skills/
   │   ├── copy.md          (from attached copy.md)
   │   ├── copy-urso.md     (from attached copy-urso.md)
   │   └── README.md        (you write; see below)
   ├── site/                (empty placeholder with .gitkeep)
   ├── OPERATIONS-PLAN.md   (if present in the brand-kit zip's root, move it here; else skip — user will add later)
   ├── README.md            (you write; see below)
   └── .gitignore
   ```

3. Extract `brand-kit.zip` into `brand-kit/`. If the ZIP's top-level is a folder already called `brand-kit`, unwrap one level so contents land directly in `brand-kit/`.

4. If `brand-kit/08-cowork/copy-urso.md` exists after extraction, DELETE it — skills now live at the repo root in `skills/`. Remove the `08-cowork/` folder if it's empty afterwards. Then update these three files to reference `skills/copy-urso.md` instead of `brand-kit/08-cowork/copy-urso.md`:
   - `brand-kit/COWORK-INSTALL.md`
   - `brand-kit/README.md`
   - `brand-kit/index.html`

5. Write `skills/README.md`:
   - Purpose: source of truth for all Urso agent skills.
   - Current skills: `copy.md` (universal craft), `copy-urso.md` (Urso brand overlay).
   - Rule: skills are edited here and nowhere else. Cowork and Claude Code consume via git-sync or symlink.
   - Version policy: skill frontmatter `version` bumps on material prompt change. `foundation_version` frontmatter must match the current `brand-kit/01-docs/foundation-brief.md` version.

6. Write `README.md` (repo root): monorepo overview, the two source-of-truth domains (brand-kit, skills), the site folder (future), and a link to `OPERATIONS-PLAN.md` as the canonical operational doc.

7. Write `.gitignore` with standard Node/Astro ignores: `node_modules/`, `dist/`, `.env*`, `.DS_Store`, `.vscode/`, `.idea/`.

8. Commit in logical chunks using conventional commits:
   - `chore: initial commit — .gitignore + README`
   - `chore: vendor brand-kit v1.5.2`
   - `feat: add skills/ with copy + copy-urso`
   - `docs: update brand-kit references from 08-cowork to skills/` (only if step 4 made edits)

9. Push to origin main.

10. Report back with:
    - Repo URL.
    - Final tree view.
    - Any decisions you made (ZIP unwrap, whether `08-cowork/` was removed, etc).

## Rules

- Do not modify skill file contents. They are canonical.
- Do not modify brand-kit content except the three path updates in step 4.
- If anything is ambiguous, ask before guessing.
- Use conventional commits format.
```

---

## 8. Revision history

- **v1.0 · 2026-04-22** — initial document, produced during Claude Design session prior to install.
- **v1.1 · 2026-04-23** — added repo-level `project-rules.md` (machine-readable rules) and `brand-kit/INDEX.md` (per-doc jurisdiction + tiebreak). Added §5 rule 6 (session-start ritual). Proposal originated in Claude Design; committed via Claude Code.
