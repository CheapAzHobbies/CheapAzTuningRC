# FastAzJato4x4

> Custom prototype E-Buggy built on a Traxxas Jato 4x4 platform. AliExpress carbon-fiber LCG chassis, FLM26800 extended arms (front) + ProTrac PRO6082-01 (rear), E-Revo 1.0 CVDs chopped to fit, stock Jato hex hubs, Tekin Pro4 HD 2500KV + Fire Phoenix XeRun 120A on 4S, plastic Apache C1 / Wltoys A929 big-bore shocks (metal Hot Bodies B8/D8 as the runner-up).
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
| Arms | FLM26800 extended (front) + ProTrac PRO6082-01 (rear) | [`arm_analysis.md`](arm_analysis.md) |
| Shock towers | Jato stock #9033 front + Slash 4x4 Extreme HD TRA9039 rear (Meelobee) | [`shock_tower_analysis.md`](shock_tower_analysis.md) |
| Arm guards | TRA6732 front + TRA6733 rear | [`arm_analysis.md`](arm_analysis.md#shock-guards) |
| Swaybars | None | Track works better without them — [`swaybar_analysis.md`](swaybar_analysis.md) |

---

## Drivetrain

| Component | Part | Notes |
|-----------|------|-------|
| Diffs (front + rear) | Traxxas E-Revo 1.0 (6mm) | In hand — [`differential_analysis.md`](differential_analysis.md) |
| Axle CVDs | E-Revo 1.0 CVDs (or knock-off), chopped to fit | [`driveshaft_analysis.md`](driveshaft_analysis.md) |
| Center diff | Stock TRA6814 OEM plastic + 20k wt oil | [`differential_analysis.md`](differential_analysis.md#center-diff) |
| Center driveshaft | Stock Slash 4x4 alum TRA6855 (215mm) | [`driveshaft_analysis.md`](driveshaft_analysis.md#center-driveshaft-comparison) |
| Spur gear | TRA3956R 54T plastic | [`differential_analysis.md`](differential_analysis.md#spur-gear) |
| Pinion | **12T 32P** on a 3200KV (matches Mike's Jato) → **16T 32P** if running a **2400KV** for the same top speed (12 × 3200/2400 = 16) | Lower-KV motor geared taller to the same top end |
| Diff / gearbox housings | Traxxas plastic — TRA6881 front / TRA6880 rear ($4 ea) | [`gearbox_housing_analysis.md`](gearbox_housing_analysis.md) |
| Hubs | Traxxas Jato 4x4 stock hex hubs | — |
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
| Bell crank | Generic AliExpress aluminum bell crank set | [`steering_bell_crank_analysis.md`](steering_bell_crank_analysis.md) |
| Knuckles + carriers | 7075 alum front steering + C-hub & rear axle carriers — Jato 4x4 | $46.80, eBay (MonsterKingz) |
| Servo | PTK 9752TG-D Metal High Speed — 1/8 1/10 | In hand — $25.00 |
| Tie rods | TBD — front needs 4mm rod upgrade | see [`arm_analysis.md`](arm_analysis.md) |

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
| — | FLM Extended Arms (USA made) | Suspension | — | — | — | — |
| #9033 / TRA9039 | Stock front (#9033) + Slash 4x4 Extreme HD rear (TRA9039) shock towers — CF towers vetoed | Suspension | ~$12 | LHS / AMain | Chosen | — |
| 107365 / A929-14 | HPI Apache C1 / Wltoys A929 plastic 97mm big-bore shocks (front + rear) | Suspension | ~$16–30/pr | Amazon / AliExpress | Chosen | — |
| — | Traxxas E-Revo CVDs (chopped to fit) | Drivetrain | — | — | — | — |
| — | Traxxas E-Revo Differentials (x2) | Drivetrain | — | — | In Hand | — |
| TRA5153 | Traxxas Drive Cup (2) — E-Revo 1.0 standard (x2 pairs / 4 total) | Drivetrain | $8.00/pair | [AMain Hobbies](https://www.amainhobbies.com) | In Hand | — |
| — | Traxxas Jato 4x4 Stock Hex Hubs | Drivetrain | — | — | — | — |
| — | 7075 Aluminum Front Steering + C Hub & Rear Axle Carriers — Jato 4x4 | Steering | $46.80 | eBay (MonsterKingz) | Considering | — |
| — | PTK 9752TG-D Metal High Speed Servo — 1/8 1/10, 2S LiPo ready | Steering | $25.00 | Temu | In Hand | — |
| — | Fire Phoenix XeRun 120A Enhanced (Speed Dragon) — Waterproof, 4S | Electronics | $30.00 | Temu | In Hand | — |
| — | FlySky FGr4S V2 Receiver — AFHDS3, PWM/PPM/IBUS, IPX4, Bidirectional | Electronics | $28.49 | AliExpress | Considering | — |
| #TT2521 | Tekin Pro4 HD 2500KV brushless motor | Electronics | $69.99 | Tekin direct | To buy | — |

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
