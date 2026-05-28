# CLAUDE.md

Guidance for Claude when working in this repo. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the human-facing structure docs (folder layout, README template, parts table format, image naming).

---

## Repo at a glance

- `cars/<CarName>/` — one folder per build. Each has `README.md`, optional `src/` (photos) and `3d-models/` (STLs).
- `batteries/` — shared across all cars. `README.md` is the master tracker; `TEMPLATE.md` is the per-pack log template.
- `Deals/` — pricing snapshots / sale tracking.
- Root `README.md` — index table of all cars.

## Branch policy

- **Push directly to `main`.** No feature branches, no PRs unless explicitly asked.
- Commit and push after each logical change so nothing sits uncommitted.

## When the user gives setup info

The user dumps tuning info as free-form lists. Route each item into the right car's `README.md` section:

- Motor / ESC / battery → **Electronics**
- Shocks, shock oil, pistons, springs, swaybars, linkage rod sizes → **Suspension**
- Diffs (front/center/rear), diff oil, pinion, spur, driveshafts → **Drivetrain**
- Steering bell crank, servo → **Steering**

The user often says "may have extra info like random screw sizes that won't need to be included" — skip those unless they're clearly a tuning/build spec.

New info from the user **overrides** existing values in the README, even if the existing value looks correct — the old value may just be stale notes the user never updated. Don't ask before overwriting; just update.

## Cars belonging to others

The user's friend Mike has related builds (FastAzJato4x4 is co-developed with him). Mike's cars get their own folder under `cars/` (e.g. `cars/Jato4x4_Mike/`) with a note linking back to the related user build.

## Battery tracker conventions (`batteries/README.md`)

- Three tables: **Active — LiPo**, **Active — Non-LiPo**, **Retired**.
- **Newest at top** in every table — sort by Acquired date descending.
- The number after the colon in user dumps (e.g. `Reaction 4000mah: 432`) is **cycle count**.
- Dates in parens at the top of a group (e.g. `(8/5/19)`) apply to every battery listed under that group until the next date.
- Multi-pack entries (e.g. `TATTU ... ×6`) get one row per pack with `#1`, `#2`, etc. suffix so per-pack cycles stay distinct.
- Energizer AA "silver" cells are **NiMH** despite the user sometimes calling them "Lithium".

## Image handling

The user often uploads images inline that need to be saved into a car's `src/` folder.

- Image naming convention is in `CONTRIBUTING.md` — `[section]_[part-description]_[part-number].[ext]`, all lowercase with underscores.
- If the md file already references an image path (e.g. `src/suspension_shock_tower_stock_front.jpg`), **rename incoming images to match that exact path** rather than inventing a new name.
- If no path is referenced yet, follow the CONTRIBUTING.md naming scheme and update the md file to point at the new filename in the same commit.

## Commit messages

- Short imperative title (≤ 70 chars), then a one- or two-sentence body explaining the why.
- Match the existing repo style — see `git log --oneline` for examples.
- Do not include model identifiers or session URLs in commits.

## What not to do

- Don't open PRs unless asked.
- Don't create CLAUDE.md-style planning/decision docs as separate files — work from conversation.
- Don't add backwards-compat shims or `_old`-style renames; just edit in place.
- Don't speculate on chemistry, part numbers, or specs — if uncertain, leave TBD or ask.
