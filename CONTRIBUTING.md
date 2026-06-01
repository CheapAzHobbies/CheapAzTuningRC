# How to Add a New Car or Update a Build

## Adding a New Car

1. Create a folder at the repo root named after the car (e.g. `FastAzJato/`)
2. Inside it, create:
   ```
   CarName/
   ├── README.md      ← main build doc (copy template below)
   ├── src/           ← all photos go here
   └── 3d-models/    ← all STL files go here
   ```
3. Add the car to the root `README.md` table under **Cars**

---

## README Template Structure

Each car README follows this order:

| Section | What goes here |
|---------|---------------|
| **Car Overview** | Base car name, brief description, overview photo |
| **Track & Setup Philosophy** | Where you race, why setup choices were made |
| **Suspension** | Shocks, springs, oil weight, swaybars |
| **Drivetrain** | Driveshafts, hubs, diff, pinion, spur |
| **Electronics** | ESC, motor, battery |
| **Steering** | Bell crank, servo, linkages |
| **Aero & Body** | Wing, body, wheels |
| **Bumpers** | Front and rear bumpers/skid plates |
| **Parts List** | Single unified table (see below) |
| **3D Models** | List of STL files in `3d-models/` |
| **TODO / Notes** | Outstanding items |

---

## Parts List Table Format

All parts go in one table with these columns:

```
| Part # | Description | Category | Cost | Source | Photo |
```

- **Part #** — use the manufacturer part number. If no part number exists, use `Generic`
- **Description** — full name of the part including key specs
- **Category** — one of: `Base Car`, `Suspension`, `Drivetrain`, `Electronics`, `Steering`, `Aero`, `Body`, `Bumpers`
- **Cost** — full retail price regardless of how you got it. Note if gifted or free in parentheses e.g. `$83.75 (gifted)`
- **Source** — where it was purchased (e.g. `Amazon`, `eBay — seller_name`, `Tammies`, `AliExpress`)
- **Photo** — `![](src/filename.jpg)` or `—` if no photo yet

---

## Image Naming Convention

All images go in `CarName/src/` and follow this format:

```
[section]_[brand]_[part-description]_[part-number].[ext]
```

**Sections:** `base`, `suspension`, `drivetrain`, `electronics`, `steering`, `aero`, `body`, `bumpers`, `overview`

**Brand:** the manufacturer (e.g. `traxxas`, `hpi`, `hb`, `tekno`, `castle`, `strc`, `wltoys`, `gmaxx`, `cobra`). Omit if the part is generic / AliExpress / no real brand.

**Examples:**
```
suspension_hpi_shocks_apache_c1_107365.jpg
drivetrain_traxxas_center_diff_tra6814.jpg
electronics_castle_esc_copperhead10.jpg
bumpers_traxxas_skid_plates_tra9044.jpg
body_pink_white.jpg                    (generic — brand omitted)
```

Rules:
- All lowercase
- Underscores, no spaces
- Brand right after section
- Include part number at the end when available

---

## Shared Resources

| Resource | Location | Notes |
|----------|----------|-------|
| Batteries | `batteries/` | Shared across all cars — log charge cycles here |
| Battery Deals | `Battery_Deals/` | Cheapest battery prices seen, by date — cross-source (eBay / AliExpress / Amazon) |
| AliExpress Codes | `AliExpress_Codes/` | Active AliExpress sitewide promo codes ranked by % off |
| Deals | `Deals/` | Pricing snapshots and sale tracking (per sale event) |
| 3D Models | `CarName/3d-models/` | Per-car STL files |

---

## Battery Tracking

Copy `batteries/TEMPLATE.md` and rename it for each pack (e.g. `batteries/pack1.md`).  
Log every charge cycle with date, mAh put in, and resting voltage after.

---

## Battery Deals

Add a row to `Battery_Deals/README.md` whenever a battery is bought (or seen at a notable low).  
Structure: **grouped by battery model** (one sub-table per model) with newest-first inside each group, plus a top "Lowest Per-Pack Price by Model" summary so you can scan all-time lows in one glance.  
Per-row columns: Date, Qty, Total, $/pack, Coupon, Source.

---

## AliExpress Codes

When a sitewide AliExpress promo is running (SSUS, summer sale, 11.11, etc.), add the active codes to `AliExpress_Codes/README.md`.  
Columns: Code, Discount (e.g. `$X off $Y+`), % Off, Notes.  
Sort by **% Off descending** — best discount on top.

---

## Deals

Add a new `.md` file under `Deals/` for each sale event.  
Name format: `brand_sale-name_year.md` (e.g. `castle_creations_memorial_day_2026.md`)
