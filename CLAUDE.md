# CLAUDE.md

Single source of guidance for working in this repo (folder layout, README template, parts table format, image naming, analysis-doc format, git workflow). Read this one file; there is no separate CONTRIBUTING doc.

**Git workflow.** This is a real git repo with a GitHub remote. Before editing, know the state: `git status`, `git branch -vv`, `git remote -v`. Push directly to `main` (see [Branch policy](#branch-policy)).

---

## Repo at a glance

- `cars/<CarName>/` — one folder per build. Each has `README.md`, optional `src/` (photos) and `3d-models/` (STLs).
- `batteries/` — shared across all cars. `README.md` is the master tracker; `TEMPLATE.md` is the per-pack log template.
- `Deals/` — **single home for all price tracking + coupon codes**. Generic-part deals (batteries, servos, ESCs, etc.) and sitewide promo codes live here. See `Deals/README.md` for the file index.
- `inbox/` — **dropzone for unsorted files** (images, order receipts, screenshots, PDFs, 3D models). User drops files here when they can't route them manually; Claude inspects, routes to the right place, and deletes from `inbox/` after.
- Root `README.md` — index table of all cars.

## Adding a new car

1. Create `cars/<CarName>/` at the repo root.
2. Inside it: `README.md` (main build doc, template below), `src/` (photos), `3d-models/` (STLs).
3. Add the car to the root `README.md` **Cars** table.

### Per-car README template

Each car `README.md` follows this section order:

| Section | What goes here |
|---|---|
| **Car Overview** | Base car name, brief description, overview photo |
| **Track & Setup Philosophy** | Where you race, why setup choices were made |
| **Suspension** | Shocks, springs, oil weight, swaybars |
| **Drivetrain** | Driveshafts, hubs, diff, pinion, spur |
| **Electronics** | ESC, motor, battery |
| **Steering** | Bell crank, servo, linkages |
| **Aero & Body** | Wing, body, wheels |
| **Bumpers** | Front and rear bumpers/skid plates |
| **Parts List** | Single unified table (format below) |
| **3D Models** | List of STL files in `3d-models/` |
| **TODO / Notes** | Outstanding items |

### Parts List table format

One table, these columns: `| Part # | Description | Category | Cost | Source | Photo |`

- **Part #** — manufacturer part number, or `Generic` if none.
- **Description** — full name including key specs.
- **Category** — one of: `Base Car`, `Suspension`, `Drivetrain`, `Electronics`, `Steering`, `Aero`, `Body`, `Bumpers`.
- **Cost** — full retail price regardless of how obtained. Note gifted/free in parens, e.g. `$83.75 (gifted)`.
- **Source** — where bought (`Amazon`, `eBay — seller`, `Tammies`, `AliExpress`).
- **Photo** — `![](src/filename.jpg)` or `—` if none yet.

## Inbox workflow

When the user says **"check inbox"** (or drops files and describes them), do this for every file in `inbox/` (except `README.md`):

1. **Identify it.** Read the file (Read tool for images / PDFs / md; Bash `file` if unsure). What part / car / deal / category does it relate to?
2. **Pick the destination** using the same routing rules below:
   - Part photo of an existing build → `cars/<CarName>/src/` with `[section]_[brand]_[part]_[part-#].[ext]` naming (see [Image handling](#image-handling)).
   - Order receipt / cart screenshot for a **generic part** (battery / servo / ESC / etc.) → add a row to the matching `Deals/<category>.md`.
   - Order receipt / cart screenshot for a **car-specific part** → add a row to that car's `<part>_analysis.md` Price History section.
   - 3D model file (`.stl`, `.step`) → `cars/<CarName>/3d-models/`.
   - Random spec / tuning info → relevant car README section.
3. **Move the file to its destination** with `mv` via Bash (don't copy-then-delete). For images, that's the right `src/` folder with the proper `[section]_[brand]_[part]_[part-#].[ext]` filename. For 3D models, the right `3d-models/` folder. **Inbox is a transit point — pictures should end up at their permanent location, not be deleted.**
   - **Scale / weight photos:** when a photo shows a digital scale with a part on it, Read the image, **transcribe the gram reading**, and update the **Weight** cell in the relevant table (e.g. the analysis doc's Weight Photos table, the spec cell of a comparison row, etc.) in the same commit that moves the photo. Filename convention: `[section]_[brand]_[part]_[part-#]_weight.jpg`. Don't just save the image — capture the number it conveys.
   - **Scale / spec readings** in general (caliper measurements, voltmeter screens, etc.) follow the same rule: read the value, write it into the relevant table, then move the image.
4. **For pure info screenshots** (e.g. a receipt where the value has already been transcribed into a `.md` row): if there's a sensible permanent home (e.g. `Deals/src/` for deal-related screenshots), `mv` there; otherwise the source file may be deleted since the info is preserved in the markdown destination.
5. **Never leave processed files lingering in `inbox/`** — every file either reaches its permanent home via `mv` or gets deleted when it has no permanent home.
6. **If a file can't be routed with confidence**, leave it in `inbox/` and ask the user where it belongs.

The `inbox/README.md` itself is sticky — never delete that.

## Where deal info goes

When the user shares a price/coupon, route it to the right place inside `Deals/`:

- **Battery price** (any brand, any source) → `Deals/batteries.md`. **Grouped by model** with newest-first inside each group, plus a top "Lowest Per-Pack Price by Model" summary. Each row: date, qty, total, $/pack, coupon, source.
- **Servo price** → `Deals/servos.md`. Same grouped-by-model structure.
- **ESC price** → `Deals/escs.md`. Same structure.
- **AliExpress coupon code** (sitewide promo like SSUS14) → `Deals/aliexpress_codes.md`. Active-sale table sorted by % off descending.
- **Car-specific part price** (the chassis for FastAzJato4x4, the motor for K939) → that part's `<part>_analysis.md` Price History section. Cross-link to the relevant `Deals/<file>.md` if a code there helped.
- **One-time sale event** (brand-wide, e.g. Castle Memorial Day) → new `Deals/brand_sale-name_year.md`.

If a new generic-part category comes up (connectors, wire, bearings, etc.) and a deal isn't a one-off, create `Deals/<category>.md` following the same structure.

**Always include the order ID** in a deal/purchase row when the user shares one (e.g. AliExpress `Order 8211906604074866`). It makes it easy to look up the order later for warranty / dispute / re-order.

**When a part is purchased** (not just compared), make three updates in the same commit:
1. Add a `✅ purchased` row to the part's `<part>_analysis.md` Price History.
2. Flip the part's status in `BOM.md` from `To buy` → `Purchased <date>`, update the price to the actual paid amount, and recompute the cost-summary totals.
3. If the part is generic (battery, servo, ESC), add a row to the matching `Deals/<category>.md` too.

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

- **Naming convention:** `[section]_[brand]_[part-description]_[part-number].[ext]`, all lowercase, underscores (no spaces), brand right after section, part number at the end when available.
  - **Sections:** `base`, `suspension`, `drivetrain`, `electronics`, `steering`, `aero`, `body`, `bumpers`, `overview`.
  - **Brand:** the manufacturer (`traxxas`, `hpi`, `hb`, `tekno`, `castle`, `strc`, `wltoys`, `gmaxx`, `cobra`). Omit if generic / AliExpress / no real brand.
  - Examples: `suspension_hpi_shocks_apache_c1_107365.jpg` · `drivetrain_traxxas_center_diff_tra6814.jpg` · `electronics_castle_esc_copperhead10.jpg` · `body_pink_white.jpg` (generic, brand omitted).
- If the md file already references an image path (e.g. `src/suspension_shock_tower_stock_front.jpg`), **rename incoming images to match that exact path** rather than inventing a new name.
- If no path is referenced yet, follow the naming scheme above and update the md file to point at the new filename in the same commit.

## Analysis docs (motor, ESC, shock tower, etc.)

When the user asks for a part-selection comparison, save it as
`cars/<CarName>/<part>_analysis.md` (alongside `motor_analysis.md`,
`esc_analysis.md`, `shock_tower_analysis.md`).

**Stay on topic.** A `<part>_analysis.md` covers that one part only. If
relevant tangents come up during research (e.g. chassis weights came
up while analyzing shock towers), drop them, don't append a "related
research" section. Keep the doc tight on its subject.

**Writing style.** Keep prose tight and scannable. **No em dashes** in
body text or notes; use commas, periods, parentheses, or shorter
sentences instead. **Avoid walls of text**; prefer tables and short
bullets over long paragraphs. If a note runs past ~2 lines, break it
up or move the detail into a table.

**Simulations.** When a physics simulation helps answer a build
question, save the script under `cars/<CarName>/sim/` with a
descriptive name (e.g. `motor_acceleration_sim.py`), generate any
output charts into `cars/<CarName>/src/` per the image naming scheme,
and document it as a section in the relevant `<part>_analysis.md`.
The doc section should:
1. State the question the sim answers (and link to a GitHub issue if
   one exists).
2. Explain the physics in plain language a HS student can follow.
3. List inputs and parameters with units.
4. Show results (table + embedded chart from `src/`).
5. Call out caveats and what the sim oversimplifies.
6. Tell the reader how to re-run the script with the deps and command.

### Document structure

1. **Title** — `# <PartType> Selection — <CarName>`
2. **Lead recommendation blockquote** — one paragraph: `> **Chosen / Leaning toward: <name>** — short reason`
3. **Hero image(s)** of the chosen / leading item, always inside `<p align="center">`. **Always centered — no exceptions.** **The hero goes directly after the lead blockquote and ABOVE everything else — before the Key Requirements and the comparison table. Never bury it below a table or after discussion paragraphs** (a reader should see the chosen item's photo first, not a table that mentions other brands).
   - **1 image**: 600px wide. **Plain `<img>` — never wrap photos in an `<a href>` product link (external links rot and break).**
   - **2 images (max)**: side by side at 500px each, separated by `&nbsp;`, both inside one `<p align="center">`. Caption on a new line below using `<br><em>left · right</em>`.
   - Skip if no image exists yet.
   ```html
   <!-- 1 image -->
   <p align="center"><img src="src/file.jpg" width="600"><br><em>Caption</em></p>

   <!-- 2 images side by side -->
   <p align="center">
     <img src="src/left.jpg" width="500">&nbsp;<img src="src/right.jpg" width="500"><br>
     <em>Left caption · Right caption</em>
   </p>
   ```
4. `---`
5. **Key Requirements table** (see below)
6. **Comparison table** (see below)
7. **Price History** (optional) — once a part actually gets purchased, add a `## Price History` section with a table tracking actual paid prices over time. Columns: `Date | Price | Discount Path | Notes`. Mark the row that was actually purchased with `✅ **purchased**` and include the order ID in Notes. Cross-link to `Deals/aliexpress_codes.md` (or wherever the code came from) when a coupon helped.
8. Detailed per-item notes, sensor compatibility, summary, etc. as needed

**Table of Contents.** Once an analysis doc grows past ~5 `##` sections, add a `## Table of Contents` with bulleted markdown links right after the hero image. Format each link as `[Section Name](#section-anchor) — short one-line summary` so the TOC also serves as a "what's in this doc" overview.

### Key Requirements table

```
| Requirement | Type | Why |
|---|---|---|
| **<requirement>** | Must / May | <one-line reason> |
```

- **Must** = hard requirement; any option that fails it is automatically Ruled Out.
- **May** = preference / nice-to-have; missing it doesn't disqualify.
- List each requirement once — don't repeat the same requirement in different words across multiple rows.
- Anti-properties (things to avoid, like "made of metal" for bumpers) belong in the Comparison table's Pros/Cons cell on the affected rows, not as a separate Requirement row.

### Comparison table

```
| <PartType> | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **Brand Model** | Key: value<br>Key: value<br>... | Pro: ...<br><br>Con: ... | <img src="src/<image-filename>" width="500"> |
```

Rules:
- **Fixed columns — never improvise the layout.** Every comparison table uses exactly these four columns in this order: `| <PartType> | Spec | Pros / Cons | Photo / Link |`. **There is no separate Status column** — status is shown as an emoji prefix on the row label in the first column (see legend below). Do **not** rename the second column or replace it with a single attribute (e.g. `Material`, `Body material`, `Weight`, `Color`) — those are `key: value` lines *inside* the Spec cell, never their own column. Copy the column layout from an existing doc — **`esc_analysis.md` is the canonical reference**. If a doc is in a different format (extra Status column, single-attribute second column), fix it to match.
- **Status = an emoji on the first-column label, not its own column.** Legend (priority order):
  - ⭐ `Chosen` — final selection (also used for `Leading` / leaning-toward)
  - 🟢 `In Hand` — already owned
  - 🥈 `Runner-up` — second choice / fallback if the chosen falls through
  - 🔵 `Candidate` — under consideration
  - ❌ `Vetoed` — user-rejected for a soft reason (e.g. proprietary connector, brand preference)
  - 🚫 `Ruled Out` — hard technical dealbreaker (e.g. wrong voltage, won't fit)

  The emoji goes first, then the **bold** part name: `| ⭐ **FLM26800** | ... |`. A status qualifier (front/rear, budget, etc.) goes after the name in italics: `⭐ **FLM26800** — *front*`. For Vetoed / Ruled Out the emoji sits before the strikethrough: `🚫 ~~**Name**~~`.
- **Spec** column: keep it short — only the essentials needed for at-a-glance comparison (typically Cells, Amps, Weight, Waterproof, Sensored, Price). Each key/value pair on its own line via `<br>`. Bold the row label and matching spec values for the leading candidate. Everything else (BEC, dimensions, motor compatibility, application limits, certifications, programming features, etc.) belongs in the Detailed Notes section below, **as bullets** under each item — not crammed into the table cell.
- **Row order**: ⭐ / 🟢 / 🥈 / 🔵 rows at the top of the table, ❌ / 🚫 rows at the bottom.
- **Pros / Cons**: single cell with `Pro: ...<br><br>Con: ...` — use a double `<br>` between Pro and Con to add a blank line for readability. Keep both on the same row even when one is short. Keep each line short and punchy — no long run-on sentences.
- **Photo / Link**: `<img src="src/<filename>" width="500">` — **plain image, never wrapped in an `<a href>` product link** (external product links rot and break, so don't include them). **Minimum 500px in the table**; 600px for the hero image of the chosen item. Use a local `src/` image when one exists; fall back to an external image only if no local one is available.
- **Multi-part items**: when one row covers a pair (e.g. front + rear shock tower), show both photos side-by-side at 250px each with `&nbsp;` between, plus a centered `<em>` caption naming each. Example:
  ```html
  <img src="src/...front.jpg" width="250"> <img src="src/...rear.jpg" width="250"><br><em>front · rear</em>
  ```
- **Keep images inside the table**: never move photos out of the table into a separate gallery section below — the table must be self-contained. The Photo/Link column stays in every comparison table. If an image feels too small, increase the `width` attribute (minimum 500px), not remove it from the table.
- **Chosen row in the table**: include the photos in the Photo cell too — don't write "see hero above". The table should be self-contained.
- **Same-brand, cross-platform parts**: if a brand sells two variants for similar-but-different cars (e.g. GPM SLA028 for Slash 4x4 vs TJ028 for Jato 4x4), split into two rows — the right-fit row gets its own status emoji, the wrong-fit row gets 🚫 `Ruled Out` for geometry mismatch and exists to warn future readers not to order it.
- **Shared photos**: when several rows are physically the same part with different windings or trim (e.g. Hobbywing EZRun 3665SD G3 in 2400 / 3200 / 4000KV — same can, different windings), use the same `src/` image for all of them. The leading row gets the `<img>` tag; later rows show `(reuses src/<filename>)` to make the relationship obvious without duplicating the photo.
- **Missing photos**: if no image exists yet, use a placeholder so the user knows one is needed — never use a bare `—`. Format:
  ```html
  <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/<expected-filename>.jpg`
  ```
  The expected filename should follow the `[section]_[brand]_[description]_[part-number].[ext]` convention so the user can drop the image straight in.
- **Consistency audit**: claims like "lightest", "cheapest", "highest amp" must be checked against the actual numbers in the table. If multiple rows make conflicting claims, fix them (e.g. "lightest waterproof option" or "lightest 6S-capable" — narrow the claim instead of dropping it).
- **Filename**: image names follow the image scheme above (`[section]_[brand]_[description]_[part-number].[ext]`).

### Standardized Spec cell format (ALL analysis docs)

**This applies to every comparison table in the whole repo, not just one part type.** Each part category has a **fixed Spec field order**, written one `**Key:** value` per `<br>` line, in the **same order in every row**. Use **`N/A`** when a field doesn't apply or isn't known yet — **never drop a field**, so rows stay aligned and scannable. Anything extra (special offset, brand notes, availability quirks) goes in the Pros/Cons cell, not the Spec block.

When you start a **new part category**, define its field order once (add a short `> *Spec format: A · B · C ...*` note above the first table in that doc) and then reuse that exact order for every row and every future doc on that category. **Register the order in the list below** so it's reused, not reinvented:

- **Tires / wheels:** Type · Tread · Compound · Dia · Width · Rim · Hex · Weight · Foam · Pre-glued · Price
- **Radio controllers (transmitters):** Type · Channels · Protocol · Receivers · Gyro · Telemetry · Model memory · Display · Battery · Price
- **Arms (A-arms):** Type · Material · Position · Fits · Wheelbase · Pivot/Hardware · Stiffness · Toe · Origin · Weight · Price
- **Bumpers:** Type · Material · Position · Fits · Includes · Weight · Price
- **Shocks:** Type · Bore · Length · Body material · Piston · Mounting · Part · Spring · Oil · Price
- **Hubs / axle carriers:** Type · Material · Bearing sizes · Hex · Fits · Pivot/Hardware · Brand · Colors · Toe · Warranty · Includes · Weight · Price
- **Rockers:** Type · Material · Rate · Pivot/Hardware · Fits · Colors · Weight · Price
- **Rods (turnbuckles / pushrods):** Type · Material · MPN · Fits · Adjustable · Length · Price
- **Bodies:** Type/Part · Material · Finish · Includes · Fits · Price
- **ESCs:** Cells · Current (A) · BEC · Sensored · Waterproof · Weight · Price
- **Motors:** Type · KV · Cells · Can · Shaft · Sensored · Poles/Slots · Rotor · Max RPM · Max temp · Bearings · Rebuildable · Weight · Price
- **Servos:** Type · Torque · Speed · Voltage · Gears · Case · Motor · Bearing · Refresh · Pulse width · Dead band · Neutral · Travel · Signal · Programmable · Size · Weight · Price
- **Shock towers:** Material · Thickness · Dimensions · Weight · Failure mode · Price
- **Gearbox housings:** Material · Part · Weight · Price
- **Steering bell cranks:** Material · Pivots · Fits · Price
- **Sway bars:** Part · Bars · Rates · Mounting · Includes · Price
- **Chassis:** Material · CG · Fits · Includes · Weight · Price
- **Differentials:** Outdrive · Housing · Internals · Part · Fits · Price
- **Spur gears:** Teeth · Pitch · Material · Fits · Price
- **Driveshafts (axle):** Type · Part · Diff end · Fits · Price
- **Driveshafts (center):** Type · Material · Part · Length · Price
- **Wheel hexes:** Type · Part · Material · Stub fit · Wheel pattern · Retention · Weight · Price
- **Wings:** Part · Material · Size · Fits · Weight · Price
- **Motor cooling (heatsink/fan):** Heatsink · Fans · Suits · Footprint · Fan max RPM · Cable · Weight · Price
- *(add new categories here as they are created)*

If you write an analysis for a category not yet listed, pick a sensible field order, apply it consistently, and append it to this registry.

## Commit messages

- Short imperative title (≤ 70 chars), then a one- or two-sentence body explaining the why.
- Match the existing repo style — see `git log --oneline` for examples.
- Do not include model identifiers or session URLs in commits.

## What not to do

- Don't open PRs unless asked.
- Don't create CLAUDE.md-style planning/decision docs as separate files — work from conversation.
- Don't add backwards-compat shims or `_old`-style renames; just edit in place.
- Don't speculate on chemistry, part numbers, or specs — if uncertain, leave TBD or ask.
