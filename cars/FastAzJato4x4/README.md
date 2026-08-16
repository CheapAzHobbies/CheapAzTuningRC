# FastAzJato4x4

> Custom prototype E-Buggy built on a Traxxas Jato 4x4 platform. AliExpress carbon-fiber LCG chassis, FLM26800 extended arms (front) + ProTrac PRO6082-01 (rear), Slash 4x4-pattern CVDs on Tekno M6 stubs (stock Jato 4x4 diffs, 5mm), stock Jato hex hubs, Hobbywing EZRun MAX10 G2 140A + 3665SD G3 2400KV combo on 4S (Fire Phoenix XeRun 120A also in hand as spare), plastic Apache C1 / Wltoys A929 big-bore shocks (metal Hot Bodies B8/D8 as the runner-up).
>
> **Build Status: WIP — actively sourcing parts. Car does not exist yet.**

---

## Table of Contents

- [Car Overview](#car-overview)
- [Track & Setup Philosophy](#track--setup-philosophy)
- [Suspension](#suspension)
- [Drivetrain](#drivetrain)
- [Electronics](#electronics)
- [Steering](#steering)
- [Aero & Body](#aero--body)
- [Bumpers](#bumpers)
- [Parts List](#parts-list)
- [3D Models](#3d-models)
- [TODO / Notes](#todo--notes)

> **Decision-locked parts** with a chosen part and confirmed cost live in [`BOM.md`](BOM.md).

---

## Car Overview

**Base Car:** Traxxas Jato 4x4 (heavily modified — custom carbon fiber chassis build)

_No build photo yet — the car doesn't physically exist; this is a parts-selection / planning build._

---

## Track & Setup Philosophy

TBD

---

## Suspension

| Component | Part | Notes |
|-----------|------|-------|
| Shocks | HPI Apache C1 / Wltoys A929 plastic 97mm big bore (front + rear) | Metal HB B8/D8 = runner-up — [`shock_analysis.md`](shock_analysis.md) |
| Springs / pistons / oil | White 59gf front + grey 52gf rear · 1.4mm×6 pistons · 45wt F / 50-60wt R | [`shock_analysis.md`](shock_analysis.md#setup-spec-springs--pistons--oil) |
| Arms | FLM26800 extended (front) + ProTrac PRO6082-01 (rear) | Front purchased $25.73 (bulk order) — [`arm_analysis.md`](arm_analysis.md) |
| Shock towers | Jato stock #9033 front + Slash 4x4 Extreme HD TRA9039 rear (Meelobee) | [`shock_tower_analysis.md`](shock_tower_analysis.md) |
| Arm guards | TRA6732 front + TRA6733 rear | [`arm_analysis.md`](arm_analysis.md#shock-guards) |
| Swaybars | None | Track works better without them — [`swaybar_analysis.md`](swaybar_analysis.md) |

---

## Drivetrain

| Component | Part | Notes |
|-----------|------|-------|
| Diffs (front + rear) | Traxxas Jato 4x4 stock (5mm) — back to stock | To buy — E-Revo 1.0 (6mm) now spares — [`differential_analysis.md`](differential_analysis.md) |
| Axle CVDs | Knock-off Slash 4x4 HD steel CV (5mm) + Tekno M6 stubs | In hand — [`driveshaft_analysis.md`](driveshaft_analysis.md) |
| Center diff | Stock TRA6814 OEM plastic + 20k wt oil | [`differential_analysis.md`](differential_analysis.md#center-diff) |
| Center driveshaft | Jato 4x4 BL-2S take-off shaft (7455), $2.49 — bought instead of TRA6855 | Purchased — [`driveshaft_analysis.md`](driveshaft_analysis.md#center-driveshaft-comparison) |
| Spur gear | TRA3956R 54T plastic | [`differential_analysis.md`](differential_analysis.md#spur-gear) |
| Pinion | **12T 32P** on a 3200KV (matches Mike's Jato) → **16T 32P** if running a **2400KV** for the same top speed (12 × 3200/2400 = 16) | Lower-KV motor geared taller to the same top end |
| Diff / gearbox housings | Traxxas plastic — TRA6881 front / TRA6880 rear ($4 ea) | [`gearbox_housing_analysis.md`](gearbox_housing_analysis.md) |
| Wheel hexes | Leaning Tekno OEM 17mm hex (pin-through, from TKR1654-17 kit); TRA6469 alt in hand, 5.9g; TKR5570-17 star hex for stock Traxxas rims | Not yet finalized — [`wheel_hex_analysis.md`](wheel_hex_analysis.md) |
| Bearings | Full sealed kit (Slash 4x4 sizes) | [`bearings_reference.md`](bearings_reference.md) |

---

## Electronics

| Component | Part | Notes |
|-----------|------|-------|
| ESC | **Hobbywing EZRun MAX10 G2 140A** — ✅ bought Jun 25 2026 ($127 combo); Fire Phoenix XeRun 120A also in hand | [`esc_analysis.md`](esc_analysis.md) |
| Motor | **Hobbywing EZRun 3665 G3 2400KV** (4-pole, came with the combo) — supersedes the Tekin Pro4 HD plan | [`motor_analysis.md`](motor_analysis.md) |
| Battery | 4S LiPo | — |
| Receiver | FlySky FGr4S V2 | Considering |

---

## Steering

| Component | Part | Notes |
|-----------|------|-------|
| Bell crank | GPM aluminum bell crank (6845X), $19.98 | In hand — [`steering_bell_crank_analysis.md`](steering_bell_crank_analysis.md) |
| Knuckles + carriers | Traxxas Raptor R Ultimate alloy hubs (EHD, front + rear) | ✅ purchased 2026-07-29 — $68.73, eBay (toysion) — [`hub_carrier_analysis.md`](hub_carrier_analysis.md) |
| Servo | PTK 9752TG-D Metal High Speed — 1/8 1/10 | In hand — $19.65 (1 of 8 bulk-bought) |
| Tie rods + camber links | ACER Racing Titanium M4x60 turnbuckles (10-pack) — all 6 links, ~61mm | ✅ purchased $59.90 — [`tie_rod_analysis.md`](tie_rod_analysis.md) |

---

## Aero & Body

| Component | Part | Notes |
|-----------|------|-------|
| Wing | Generic AliExpress 1/8 buggy wing | [`aero_analysis.md`](aero_analysis.md) |
| Wing mount | OEM Jato 4x4 TRA9046 via Meelobee technique (on Slash 4x4 Extreme HD rear tower) | [`aero_analysis.md`](aero_analysis.md) |
| Body / shell | JConcepts P2 (0684) leaning; Traxxas OEM 9018 family fallback | [`aero_analysis.md`](aero_analysis.md#body-comparison) |

---

## Bumpers

| Component | Part | Notes |
|-----------|------|-------|
| Front + rear | Traxxas TRA9044 front + rear skid plates ($7 set) | [`bumper_analysis.md`](bumper_analysis.md) |
| Front shock guard (alt) | Rustler TRA6736 / RPM 81042 — both guard the front shocks well | [`bumper_analysis.md`](bumper_analysis.md) |

---

## Parts List

| Part # | Description | Category | Cost | Source | Status | Photo |
|--------|-------------|----------|------|--------|--------|-------|
| — | Traxxas Jato 4x4 | Base Car | — | — | — | — |
| — | RC Carbon Fiber Chassis Kit fit for Traxxas Slash VXL 4x4 TRA6808 | Chassis | $100.26 | [Temu](https://www.temu.com) / [AliExpress](https://a.aliexpress.com/_mPWcAS3) | Considering | — |
| FLM26800 | FLM Extended Arms (front, USA made) — 1 of a 4-pair bulk order ($102.90 total) | Suspension | $25.73 | FLM | Purchased | ![](src/suspension_flm_rustler_rear_extended_arms_flm26800.jpg) |
| #9033 / TRA9039 | Stock front (#9033) + Slash 4x4 Extreme HD rear (TRA9039) shock towers — CF towers vetoed | Suspension | ~$12 | LHS / AMain | Chosen | — |
| 107365 / A929-14 | HPI Apache C1 / Wltoys A929 plastic 97mm big-bore shocks (front + rear) | Suspension | ~$16–30/pr | Amazon / AliExpress | Chosen | — |
| — | Knock-off Slash 4x4 HD Steel CV driveshafts (5mm) + Tekno M6 stubs, order #8211906604054866 | Drivetrain | $21.10 | AliExpress — FengS Store | In Hand | — |
| — | Traxxas Jato 4x4 stock front + rear diffs (5mm) | Drivetrain | ~$25.94 (2×$12.97) | Jenny's RC | To buy | — |
| — | Traxxas E-Revo 1.0 Differentials (x2, 6mm — now spares, wrong outdrive) | Drivetrain | — | — | In Hand | — |
| TRA5153 | Traxxas Drive Cup (2) — E-Revo 1.0 standard (x2 pairs / 4 total, now spares — mates the E-Revo 6mm diff only) | Drivetrain | $8.00/pair | [AMain Hobbies](https://www.amainhobbies.com) | In Hand | — |
| — | Traxxas Jato 4x4 Stock Hex Hubs | Drivetrain | — | — | — | — |
| 9063/9064/9065 | Traxxas Raptor R Ultimate alloy hubs — EHD front C-hubs + steering blocks + rear stub axle carriers, full set | Steering | $68.73 | eBay (toysion) | Purchased 2026-07-29 | ![](src/suspension_traxxas_raptor_r_ultimate_alloy_hubs.jpg) |
| — | 7075 Aluminum Front Steering + C Hub & Rear Axle Carriers — Jato 4x4 (MonsterKingz, demoted to fallback/spare) | Steering | $46.80 | eBay (MonsterKingz) | In Hand | ![](src/suspension_monsterkingz_alloy_uprights_jato4x4.jpg) |
| — | PTK 9752TG-D Metal High Speed Servo — 1/8 1/10, 2S LiPo ready (1 of 8 bulk-bought) | Steering | $19.65 | AliExpress — PTK Servo Store | In Hand | — |
| — | ACER Racing Titanium M4x60 Turnbuckles (10-pack) — all 6 tie rods + camber links, ~61mm, + 4 spares | Steering | $59.90 | ACER Racing | Purchased 2026-08-16 | ![](src/steering_acer_titanium_turnbuckle_m4x60.jpg) |
| 38020343 | Hobbywing EZRun MAX10 G2 140A + 3665SD G3 2400KV combo (ESC + motor) | Electronics | $127.00 | Hobbywing direct | Purchased 2026-06-25 | — |
| — | Fire Phoenix XeRun 120A Enhanced (Speed Dragon) — Waterproof, 4S (now spare/fallback) | Electronics | $30.00 | Temu | In Hand | — |
| — | FlySky FGr4S V2 Receiver — AFHDS3, PWM/PPM/IBUS, IPX4, Bidirectional | Electronics | $28.49 | AliExpress | Considering | — |

---

## 3D Models

> See [`3d-models/`](3d-models/) for all custom STL files.

| Model | Description | Status |
|-------|-------------|--------|
| Custom front-end shroud / wing mount + Rustler bumper integration | Cosmetic shroud that integrates the Rustler 4x4 front bumper (better crash protection, ugly stock) into a clean wing mount. Discussed in [`bumper_analysis.md`](bumper_analysis.md#notes) | Idea / TODO |

---

## TODO / Notes

- [ ] Fill in all part numbers and costs
- [ ] Add photos
- [ ] Document CF chassis eBay link
- [ ] Finalize motor spec
