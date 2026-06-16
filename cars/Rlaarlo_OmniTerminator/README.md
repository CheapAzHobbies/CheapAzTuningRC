# Rlaarlo Omni-Terminator

> 1/10 4WD brushless monster truck — **kept mostly stock**. This page is a build/maintenance log, not a deep parts analysis: the plan is stock running gear plus a few easy items (shock oil, wheels/tires, basic alloy hubs) and the cheap durability swaps the community already agrees on. The big takeaway from owners: **the driveline is what breaks — stock up on dog bones, diff cups, and gears.**

> 🎓 **Graduation gift** from my dad, **Hien Nguyen**, for finishing my **Electrical Engineering** degree at **Portland State University** (graduated June 14, 2026).

*Photo TBD.*

---

## Table of Contents

- [Overview](#overview)
- [Track & Setup Philosophy](#track--setup-philosophy)
- [Known Weak Points — what breaks](#known-weak-points--what-breaks)
- [Maintenance Parts to Keep On Hand](#maintenance-parts-to-keep-on-hand)
- [Planned Light Upgrades](#planned-light-upgrades)
- [Option Parts Catalog](#option-parts-catalog)
- [3D Models](#3d-models)
- [Parts List](#parts-list)
- [TODO / Notes](#todo--notes)
- [Sources](#sources)

---

## Overview

| Spec | Value |
|------|-------|
| Class | 1/10 4WD brushless monster truck |
| Version | **Carbon** |
| Motor | 3650 **2650KV** brushless |
| ESC | **60A** brushless w/ fan |
| Battery | 3S LiPo (2200–4400mAh) |
| Top speed | ~50 mph (claimed) |
| Carbon extras | CF plates on suspension arms, radio with **voltage telemetry + gyro**, better motor/ESC vs base |

---

## Track & Setup Philosophy

Same as the rest of the fleet: set up for **Meldrum Bar Park** (dirt track), with occasional **beach** running. Kept **mostly stock** — only spend where it stops breakage (cheap hardened driveline parts) or matters for dirt.

**Cost note:** Rlaarlo upgrade/spare parts are surprisingly **pricier than a comparable Traxxas Slash's** — another reason to keep this one mostly stock and only buy the cheap durability swaps.

---

## Known Weak Points — what breaks

The truck has a "well-built basher" reputation, and the **failures cluster in the driveline**. Tagged by confidence: **👥 = owners directly report it** (ARRMA forum, RCTalk, Rlaarlo group), **🔧 = my inference** (catalog availability + general basher wear, *not* a specific owner complaint).

1. 👥 **Dog bones / CVD driveshafts** — the #1 failure. Driveline parts can need replacing after as few as **~10 packs**. Stock up, or upgrade to the hardened S2 / 45# steel CVDs.
2. 👥 **Differential drive cups** — round out / strip where the dog bone seats. The **S2 drive-cup upgrade** is the common fix.
3. 👥 **Pinion / spur gears strip** — stock gears strip; owners report a **hardened aftermarket pinion** (Amazon) lasts much longer.
4. 👥 **Steering knuckles** — you (the owner) confirmed the stock plastic knuckles break.
5. 🔧 **Center differential (65T)** — a metal upgrade is sold and it's in the driveline, but I didn't see it as a *loud* complaint.
6. 🔧 **Hexes / bearings / shocks** — normal wear on any basher, not Omni-specific.

**Arms & bumpers — why they're *not* high on the list:** I expected them too, but found **no strong owner reports of suspension arms or bumpers breaking**. The Carbon version adds CF plates to stiffen the arms (a hint they *can* break under abuse), but it's not a common complaint, which fits the "well-built" rep. There's no traditional bumper part either — the **body shell (R11078)** takes front hits. So arms/body are listed as low-confidence spares, not must-haves.

---

## Maintenance Parts to Keep On Hand

Prioritized — 🔴 buy before you run it hard, 🟡 nice to have, 🟢 occasional. **Confidence:** 👥 = owners directly report it failing; 🔧 = my call (sensible spare / catalog item, no specific owner quote). Part numbers are universal; pricing is TBD (see note below).

| Pri | Src | Part | Rlaarlo # | Why | Photo |
|---|---|---|---|---|---|
| 🔴 | 👥 | S2 hardened CVD driveshafts | R11141 (front) / R11142 (rear) | Dog bones fail first; S2 hardened outlasts stock | <img src="src/drivetrain_rlaarlo_cvd_driveshafts_r11141.jpg" width="180"> |
| 🔴 | 👥 | Standard front CVD driveshafts (2-pack) | R11036 | Cheaper stock-style spare to keep around | |
| 🔴 | 👥 | S2 diff drive cups | R11145 (also R11146/47/48) | Cups round out where the bone seats | <img src="src/drivetrain_rlaarlo_diff_drive_cups_r11145.jpg" width="180"> |
| 🔴 | 👥 | Hardened M1 pinion | R11155 (24T) / R11156 (26T) / R11157 (28T) — **or any generic M1** | Stock pinion strips; hardened lasts far longer. **M1 is a standard module**, so a generic hardened M1 pinion (e.g. **Surpass Hobby**) is way cheaper than the Rlaarlo-branded one | <img src="src/drivetrain_rlaarlo_pinion_24t_r11155.jpg" width="180"> |
| 🔴 | 👥 | Steering knuckles / hubs (alloy) | R11132 (front) / R11133 (rear) | **Stock plastic knuckles break** — alloy is a real fix, not cosmetic | <img src="src/suspension_rlaarlo_front_steering_hubs_r11132.jpg" width="180"> |
| 🟢 | 🔧 | 65T central differential | R11139 (34T diff = R11140) | **Not a common break, just wears over time.** Skip the alloy diff (not worth it) — if it wears, replacing the cheaper **housing** beats buying a whole diff | <img src="src/drivetrain_rlaarlo_center_diff_65t_r11139.jpg" width="180"> |
| 🟡 | 🔧 | Suspension arms (upper, S2) | R11130 (front) / R11131 (rear) | Carbon CF plates hint arms can break, but not a common report | |
| 🟡 | 🔧 | H17 alloy hex adaptors | RZ062 (or R11151) | Hexes round out | <img src="src/drivetrain_rlaarlo_hex_adapters_h17_rz062.jpg" width="180"> |
| 🟡 | 🔧 | Shock absorbers (2-pack) + oil | R11001 | Leak/bend; oil for tuning | |
| 🟡 | 🔧 | Full bearing kit | ABEC-3 set (eBay) | Dirt and sand kill bearings; keep a reseal set | |
| 🟢 | 🔧 | Servo saver (alloy upgrade) | R11137 (stock) | Protects the steering servo; alloy version available (fits RZ001 / 1/10 rally) | <img src="src/steering_rlaarlo_aluminum_servo_saver.jpg" width="180"> |

> **Where to buy / pricing:** I can't scrape live AliExpress prices (login wall), so $ figures are TBD. Sources:
> - **Official Rlaarlo AliExpress store** — [RLAARLO Original Parts for OMNI-TERMINATOR](https://www.aliexpress.us/item/3256807605383286.html) (genuine parts, most complete single listing — pick the part from the dropdown).
> - **Third-party "for Rlaarlo" sellers** (AliExpress / Amazon / eBay) — usually cheaper for generic wear parts (CVDs, hexes, bearings, M1 pinion); quality varies.
> - **Benchmark (FairRC):** S2 diff cup ~**$12.99**, S2 CVD driveshaft ~**$29.99** — use these to judge if an AliExpress price is actually a deal.
>
> Paste a listing or cart total and I'll fill in a price column.

> **Center diff vs spool:** **R11139 (65T) is the center _differential_** — the one to keep. **R11144 (60T) / R11154 (33T)** are **solid center gear / drive-shaft (spool)** parts — a locked-center setup with no diff action, *not* a diff wear replacement.
>
> **Buying just the housing:** **yes** — the diff **housing, drive cups, and gear set are sold individually** (Rlaarlo direct, FairRC, SeriousRC), so a worn diff usually only needs the cheap housing, not a whole new diff.

---

## Planned Light Upgrades

Keeping it mostly stock — only these:

- **Hardened steel pinion** (cheap insurance against the most common strip).
- **S2 hardened CVDs + S2 diff drive cups** — the one durability swap every owner recommends.
- **Aluminum hubs / steering:** front steering hubs (R11132), rear hub carriers (R11133), alloy upper steering brace (R11134), alloy gearbox cover (R11138).
- **Shock oil tuning** — dial damping for dirt (analysis later if it's worth a doc).
- **Wheels/tires:** a grippier dirt tire for Meldrum if the stock tires don't hook up.

---

## Option Parts Catalog

Full Rlaarlo option/upgrade sheet (every part number) and the AL alloy modification-kit overview — handy for ordering spares by R-number.

<p align="center">
  <img src="src/reference_rlaarlo_omniterminator_alloy_mod_kit_p2.jpg" width="440">&nbsp;<img src="src/reference_rlaarlo_omniterminator_option_parts_p1.jpg" width="440"><br>
  <em>AL alloy modification kit (reinforced diffs, S2 transmission rods, alloy swing-arm braces, H17 hexes) · Option parts (R11130–R11158, RZ062, RZ066)</em>
</p>

---

## 3D Models

### ⭐ Rear skid plate — simon vezina (chosen, STL included)

**Rlaarlo Omni Terminator Skid Plates** by **simon vezina** — covers the underside of the main chassis. Licensed **CC BY-NC 4.0** (free, attribution + non-commercial), so the STL **is included** here: [`3d-models/skid_plate_rear_simon_vezina/`](3d-models/skid_plate_rear_simon_vezina/). I only print the **rear skid** (the set also has full / left / right).

**Why this over the Cults plate below:**
- The Cults design has a **flaw** — you screw into a **tiny piece of plastic that shears off**.
- This one is **easier to print** and just uses **longer bolts (or stock)**.

<p align="center"><img src="src/reference_rlaarlo_skid_plate_simon_vezina.jpg" width="460"></p>

> Source: [Printables](https://www.printables.com/model/1251771-rlaarlo-omni-terminator-skid-plates/files) · License **CC BY-NC 4.0** (credit simon vezina, non-commercial — don't sell prints). See `ATTRIBUTION.txt` in the model folder.

### Reference only (not redistributed)

❌ **Rear Chassis Skid Plate / Bottom Cover** by **OG_Cranck** — a **CULTS "Private Use"** (paid) design, so the STL is **not committed** here (would break the license). Also superseded by simon's design (the tiny-plastic shear-off flaw above). Re-download from your Cults purchases: [Cults3D](https://cults3d.com/en/3d-model/game/rear-chassis-skid-plate-protector-for-rlaarlo-omni-terminator-bottom-cover-upgr). Same designer also has a **Differential & Gear Cover** and a **Shock Preload Spacer** on [their Cults profile](https://cults3d.com/en/users/OG_Cranck/3d-models).

<p align="center"><img src="src/reference_rlaarlo_skid_plate_og_cranck.jpg" width="200"></p>

---

## Parts List

| Part # | Description | Category | Cost | Source | Photo |
|--------|-------------|----------|------|--------|-------|
| — | Rlaarlo Omni-Terminator **Carbon** | Base Car | gift | Rlaarlo (grad gift) | — |

---

## TODO / Notes

- [x] Version confirmed: **Carbon**
- [ ] Add a photo of the car
- [ ] Order the 🔴 driveline spares before hard running
- [ ] Decide on hardened pinion source

---

## Sources

- [Rlaarlo Omni-Terminator product page](https://rlaarlo.com/products/rlaarlo-carbon-fiber-black-omni-terminator-rz001b-c)
- [SeriousRC — Omni-Terminator spare parts & upgrades](https://www.seriousrc.co.uk/collections/rlaarlo-omni-terminator-truck-spare-parts-and-upgrades)
- [ARRMA RC Forum — Omni-Terminator thread](https://www.arrmaforum.com/threads/rlaarlo-omni-terminator-monster-truck.67774/)
- [RCTalk — Omni-Terminator thread](https://www.rctalk.com/forum/threads/omni-terminator.147457/)
- [Rlaarlo — differential / drive-cup upgrade guides](https://rlaarlo.com/blogs/support-video/rlaarlo-omni-terminator-upgrades-differential-housing-and-differential-drive-cup-upgrade-parts)
