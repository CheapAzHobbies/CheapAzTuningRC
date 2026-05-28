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

## Analysis docs (motor, ESC, shock tower, etc.)

When the user asks for a part-selection comparison, save it as
`cars/<CarName>/<part>_analysis.md` (alongside `motor_analysis.md`,
`esc_analysis.md`, `shock_tower_analysis.md`).

**Stay on topic.** A `<part>_analysis.md` covers that one part only. If
relevant tangents come up during research (e.g. chassis weights came
up while analyzing shock towers), drop them — don't append a "related
research" section. Keep the doc tight on its subject.

### Document structure

1. **Title** — `# <PartType> Selection — <CarName>`
2. **Lead recommendation blockquote** — one paragraph: `> **Chosen / Leaning toward: <name>** — short reason`
3. **Hero image(s)** of the chosen / leading item at 600px wide, centered with `<p align="center">`, wrapping the product-page link. If the chosen item is actually two parts (e.g. front + rear shock tower), put both at 300px inside one centered `<p>` with `&nbsp;` between them and a centered italic caption below. Skip if no image exists yet.
4. `---`
5. **Key Requirements table** (see below)
6. **Comparison table** (see below)
7. Detailed per-item notes, sensor compatibility, summary, etc. as needed

### Key Requirements table

```
| Requirement | Type | Why |
|---|---|---|
| **<requirement>** | Must / May | <one-line reason> |
```

- **Must** = hard requirement; any option that fails it is automatically Ruled Out.
- **May** = preference / nice-to-have; missing it doesn't disqualify.
- List each requirement once — don't repeat the same requirement in different words across multiple rows.

### Comparison table

```
| <PartType> | Spec | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **Brand Model** | Key: value<br>Key: value<br>... | **Chosen** / **In Hand** / **Candidate** / **Vetoed** / Ruled Out | Pro: ...<br>Con: ... | <a href="<product-page-url>"><img src="src/<image-filename>" width="300"></a> |
```

Rules:
- **Spec** column: keep it short — only the essentials needed for at-a-glance comparison (typically Cells, Amps, Weight, Waterproof, Sensored, Price). Each key/value pair on its own line via `<br>`. Bold the row label and matching spec values for the leading candidate. Everything else (BEC, dimensions, motor compatibility, application limits, certifications, programming features, etc.) belongs in the Detailed Notes section below, **as bullets** under each item — not crammed into the table cell.
- **Status** values, in priority order:
  - `Chosen` — final selection
  - `In Hand` — already owned
  - `Candidate` — under consideration
  - `Vetoed` — user-rejected for a soft reason (e.g. proprietary connector, brand preference)
  - `Ruled Out` — hard technical dealbreaker (e.g. wrong voltage, won't fit)
- **Row order**: Chosen / In Hand / Candidate rows at the top of the table, Vetoed / Ruled Out rows at the bottom. Strike through the row label with `~~name~~` for Vetoed and Ruled Out.
- **Pros / Cons**: single cell with `Pro: ...<br>Con: ...`. Keep both on the same row even when one is short.
- **Photo / Link**: `<a href="...product-page..."><img src="src/<filename>" width="300"></a>`. 300px in the table is large enough to read on mobile; 600px for the hero image of the chosen item. Use a local `src/` image when one exists; fall back to an external image only if no local one is available. Use `—` if no photo or link yet.
- **Consistency audit**: claims like "lightest", "cheapest", "highest amp" must be checked against the actual numbers in the table. If multiple rows make conflicting claims, fix them (e.g. "lightest waterproof option" or "lightest 6S-capable" — narrow the claim instead of dropping it).
- **Filename**: image names follow the image scheme above (`[section]_[brand]_[description]_[part-number].[ext]`).

## Commit messages

- Short imperative title (≤ 70 chars), then a one- or two-sentence body explaining the why.
- Match the existing repo style — see `git log --oneline` for examples.
- Do not include model identifiers or session URLs in commits.

## What not to do

- Don't open PRs unless asked.
- Don't create CLAUDE.md-style planning/decision docs as separate files — work from conversation.
- Don't add backwards-compat shims or `_old`-style renames; just edit in place.
- Don't speculate on chemistry, part numbers, or specs — if uncertain, leave TBD or ask.
