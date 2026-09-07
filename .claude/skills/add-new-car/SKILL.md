---
name: add-new-car
description: Scaffold a new car build folder in this repo. Use when adding a car that isn't in cars/ yet, or when you need the per-car README section order or the Parts List table column format. Covers the folder layout, the README template, and the Parts List columns.
---

# Adding a new car

1. Create `cars/<CarName>/` at the repo root.
2. Inside it: `README.md` (main build doc, template below), `src/` (photos), `3d-models/` (STLs).
3. Add the car to the root `README.md` **Cars** table.

## Per-car README template

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

## Parts List table format

One table, these columns: `| Part # | Description | Category | Cost | Source | Photo |`

- **Part #** — manufacturer part number, or `Generic` if none.
- **Description** — full name including key specs.
- **Category** — one of: `Base Car`, `Suspension`, `Drivetrain`, `Electronics`, `Steering`, `Aero`, `Body`, `Bumpers`.
- **Cost** — full retail price regardless of how obtained. Note gifted/free in parens, e.g. `$83.75 (gifted)`.
- **Source** — where bought (`Amazon`, `eBay — seller`, `Tammies`, `AliExpress`).
- **Photo** — `![](src/filename.jpg)` or `—` if none yet.
