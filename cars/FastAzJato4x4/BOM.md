# Bill of Materials — FastAzJato4x4

Items decided by the analysis docs in this folder. Only parts with a clear pick **and** documented cost (or "in hand at $0") are listed — items marked TBD or in active research live in the [README's Parts List](README.md#parts-list) and the [TODO / Notes](README.md#todo--notes) section.

> See the linked analysis docs for the reasoning behind each pick.

---

## Electronics

| Part | Status | Source | Price | Decided by |
|---|---|---|---|---|
| **Fire Phoenix XeRun 120A Enhanced (Speed Dragon)** ESC | **In Hand** | Temu / AliExpress | $30.00 (sunk) | [`esc_analysis.md`](esc_analysis.md) |
| **Tekin Pro4 HD 2500KV** brushless motor (#TT2521) | **To buy** | [Tekin direct](https://store.teamtekin.com/pro4-hd-2500kv-brushless-motor/) | $69.99 | [`motor_analysis.md`](motor_analysis.md) |
| **PTK 9752TG-D Metal High Speed Servo** | **In Hand** | Temu | $25.00 (sunk) | (existing build pick) |

---

## Drivetrain

| Part | Status | Source | Price | Decided by |
|---|---|---|---|---|
| **Traxxas E-Revo 1.0 front differential** | **In Hand** | — | $0 (sunk) | [`differential_analysis.md`](differential_analysis.md) |
| **Traxxas E-Revo 1.0 rear differential** | **In Hand** | — | $0 (sunk) | [`differential_analysis.md`](differential_analysis.md) |
| **Stock Traxxas center diff** + **20k wt oil** | To buy from spares / LHS | LHS / Traxxas | ~$15 + $5 oil | [`differential_analysis.md`](differential_analysis.md#center-diff-oil) |
| **Center driveshaft** — stock plastic / stock metal / Tekno (pick cheapest in stock) | To buy | LHS / AMain | $10-30 | [`differential_analysis.md`](differential_analysis.md#center-driveshaft) |
| **Front gearbox housing** — Traxxas stock plastic or compatible kit (Wltoys K939 / Remo EMU9 / HQ727) | To buy | AliExpress / LHS / Traxxas | $10-20 | [`gearbox_housing_analysis.md`](gearbox_housing_analysis.md) |
| **Rear gearbox housing** — Traxxas stock plastic or compatible kit | To buy | AliExpress / LHS / Traxxas | $10-20 | [`gearbox_housing_analysis.md`](gearbox_housing_analysis.md) |
| **TRA5153 Traxxas Drive Cup** (E-Revo standard, x2 pairs = 4 total) | **In Hand** | AMain | $16.00 (sunk, gifted) | (drivetrain compatibility — referenced in [`differential_analysis.md`](differential_analysis.md)) |

---

## Suspension

| Part | Status | Source | Price | Decided by |
|---|---|---|---|---|
| **Traxxas #9033 — stock composite front shock tower** | To buy (or pull from spares) | LHS / Traxxas / AMain | ~$6.00 | [`shock_tower_analysis.md`](shock_tower_analysis.md) |
| **Traxxas #9034 — stock composite rear shock tower** | To buy | LHS / Traxxas / AMain | ~$6.00 | [`shock_tower_analysis.md`](shock_tower_analysis.md) — **note: pending [aero cascade decision](aero_analysis.md#shock-tower-compatibility-cascade)** (STRC backflash kit would swap this for older Slash-style tower) |
| **HPI Apache C1 97mm big-bore shocks (#107365)** — front + rear set | To buy (4× shocks, 2 pairs) | Amazon / Hobby-Sports | $39.98 (2 pairs × $19.99) | [`shock_analysis.md`](shock_analysis.md) |
| **Hot Bodies HB67453 grey 52gf 76mm springs** — rear | To buy | eBay / power_hobby | $11.75 | [`shock_analysis.md`](shock_analysis.md#setup-spec-springs--pistons--oil) |
| **1.4mm × 6 hole shock pistons** (Apache C1 / D8 compatible) — 4 sets | To buy | LHS | ~$10 | [`shock_analysis.md`](shock_analysis.md#setup-spec-springs--pistons--oil) |
| **Silicone shock oil 45wt** (front) | To buy | LHS | ~$6 / bottle | [`shock_analysis.md`](shock_analysis.md#setup-spec-springs--pistons--oil) |
| **Silicone shock oil 50-60wt** (rear, exact weight TBD) | To buy | LHS | ~$6 / bottle | [`shock_analysis.md`](shock_analysis.md#setup-spec-springs--pistons--oil) |

---

## Steering

| Part | Status | Source | Price | Decided by |
|---|---|---|---|---|
| **Generic AliExpress aluminum servo bell crank set** (same family as K939 build) | To buy | AliExpress | ~$10.00 | [`steering_bell_crank_analysis.md`](steering_bell_crank_analysis.md) |

---

## Chassis & Body

| Part | Status | Source | Price | Decided by |
|---|---|---|---|---|
| **AliExpress CF chassis** (fits Traxxas Slash 4x4 VXL TRA6808 pattern) | To buy | AliExpress / Temu | ~$100 (or less) | [`chassis_analysis.md`](chassis_analysis.md) |
| **Front bumper** — Traxxas TRA5535 Jato 4x4 OEM (minimal-profile, recovery-friendly) | To buy | LHS / AMain | ~$6-8 | [`bumper_analysis.md`](bumper_analysis.md#front-bumper) |
| **Rear bumper** — Traxxas TRA5536 Jato 4x4 OEM (assumes OEM wing mount path; switches to TRA6836 Slash 4x4 if STRC conversion is chosen) | To buy — pending [wing mount cascade](aero_analysis.md#shock-tower-compatibility-cascade) | LHS / AMain | ~$6-8 | [`bumper_analysis.md`](bumper_analysis.md#rear-bumper) |

---

## Aero

| Part | Status | Source | Price | Decided by |
|---|---|---|---|---|
| **Generic AliExpress 1/8 buggy wing** | **In Hand** (or to buy if not already) | AliExpress | ~$3-8 | [`aero_analysis.md`](aero_analysis.md) |
| **Wing mount** — OEM Jato 4x4 (default) or STRC SPTST6808B backflash conversion | **Decision pending** — see [shock tower compatibility cascade](aero_analysis.md#shock-tower-compatibility-cascade) | LHS / AMain | OEM ~$10-20, STRC ~$30-50 (free if STRC SPTST6808B already in hand from K939 build) | [`aero_analysis.md`](aero_analysis.md) |

---

## Cost summary

| Bucket | Sub-total |
|---|---|
| **Already in hand (sunk cost)** — ESC, both E-Revo diffs, servo, drive cups | **$71** |
| **To buy — locked spec** — motor, shock towers, chassis, Apache C1 shocks + springs + pistons + oils, bell crank | **~$214** |
| **To buy — pending exact pick** — center diff + driveshaft, gearbox housings (front + rear), bumpers, wing + wing mount | **~$60-120** |
| **Total estimated (chosen + estimated open items)** | **~$345-405** |

---

## Notes

- **ESC sensor adapter:** not needed. The Tekin Pro4 HD uses a dual-plug JST-ZH sensor harness that mates directly with the Fire Phoenix's JST-ZH sensor input. No adapter cable.
- **Cooling fan / heatsink:** not in the BOM. The chosen Pro4 HD 2500KV has the thermal mass to run bare on 4S — see [the cooling weight analysis](motor_analysis.md#real-world-weight-1412-3200kv--cooling-vs-1415-2400kv-bare).
- **Shock tower brace (TRA9061):** [vetoed](shock_tower_analysis.md#related-tower-bracing-optional), not in the BOM.
- **6mm vs 5mm drivetrain:** the in-hand E-Revo diffs dictate 6mm outdrives, which in turn mate the in-hand E-Revo CVDs and axles. Stock Jato/Slash 5mm diffs are physically incompatible — see [differential_analysis.md](differential_analysis.md).
- **Aluminum gearbox housings:** vetoed — CF chassis already has a metal skid plate protecting the diffs from below, making the aluminum-housing upgrade redundant. See [gearbox_housing_analysis.md](gearbox_housing_analysis.md#why-aluminum-isnt-worth-it-on-this-build).
- **Aluminum bumpers / shock towers:** vetoed per the sacrificial-failure logic. Aluminum on this build is reserved for the bell crank only (where stiffness under steering load matters and crash exposure is low).
- **Cross-decision dependency:** the rear shock tower pick depends on the wing mount decision. OEM Jato wing mount + #9034 stock tower exposes rear shocks to rear-end crashes (broke an HPI Vorza 97mm previously). STRC backflash conversion + older Slash 4x4 rear tower protects shocks but invalidates the chosen #9034. See [`aero_analysis.md`](aero_analysis.md#shock-tower-compatibility-cascade).
- **Pinion / spur:** TBD, [reference table here](motor_analysis.md#pinion-reference-32p-tbd) — not yet decided.
- **Metal vs plastic shock bodies:** running Apache C1 plastic out of the gate; upgrade to Hot Bodies D8 metal only if body cracks become a recurring problem. See [shock_analysis.md plastic-vs-metal](shock_analysis.md#plastic-vs-metal-body-trade-off).

For everything else (FLM arms, hubs, body, etc.) that's still being researched, see the [main README parts list](README.md#parts-list).
