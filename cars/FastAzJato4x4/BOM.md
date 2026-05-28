# Bill of Materials — FastAzJato4x4

Items decided by the analysis docs in this folder. Only parts with a clear pick **and** documented cost (or "in hand at $0") are listed — items marked TBD or in active research live in the [README's Parts List](README.md#parts-list) and the [TODO / Notes](README.md#todo--notes) section.

> See the linked analysis docs for the reasoning behind each pick.

---

## Electronics

| Part | Status | Source | Price | Decided by |
|---|---|---|---|---|
| **Fire Phoenix XeRun 120A Enhanced (Speed Dragon)** ESC | **In Hand** | Temu / AliExpress | $30.00 (sunk) | [`esc_analysis.md`](esc_analysis.md) |
| **Tekin Pro4 HD 2500KV** brushless motor (#TT2521) | **To buy** | [Tekin direct](https://store.teamtekin.com/pro4-hd-2500kv-brushless-motor/) | $69.99 | [`motor_analysis.md`](motor_analysis.md) |

---

## Drivetrain

| Part | Status | Source | Price | Decided by |
|---|---|---|---|---|
| **Traxxas E-Revo 1.0 front differential** | **In Hand** | — | $0 (sunk) | [`differential_analysis.md`](differential_analysis.md) |
| **Traxxas E-Revo 1.0 rear differential** | **In Hand** | — | $0 (sunk) | [`differential_analysis.md`](differential_analysis.md) |
| **Stock Traxxas center diff** (with 20k wt oil) | TBD source — likely from in-hand spares or Traxxas | LHS / Traxxas | ~$15 | [`differential_analysis.md`](differential_analysis.md#center-diff-oil) |
| **Center driveshaft** — pick on price and availability (stock plastic / stock metal / Tekno all fine) | TBD | LHS / AMain | $10-30 depending on choice | [`differential_analysis.md`](differential_analysis.md#center-driveshaft) |

---

## Suspension

| Part | Status | Source | Price | Decided by |
|---|---|---|---|---|
| **Traxxas #9033 — stock composite front shock tower** | **To buy** (or pull from spares — Traxxas spare commonly stocked at local hobby stores) | LHS / Traxxas / AMain | ~$6.00 | [`shock_tower_analysis.md`](shock_tower_analysis.md) |
| **Traxxas #9034 — stock composite rear shock tower** | **To buy** | LHS / Traxxas / AMain | ~$6.00 | [`shock_tower_analysis.md`](shock_tower_analysis.md) |

---

## Chassis & Body

| Part | Status | Source | Price | Decided by |
|---|---|---|---|---|
| **AliExpress CF chassis** (fits Traxxas Slash 4x4 VXL TRA6808 pattern) | **To buy** | AliExpress / Temu | ~$100 (or less) | [`chassis_analysis.md`](chassis_analysis.md) |
| **Traxxas stock plastic bumpers — front & rear** (Slash / Rustler / Jato 4x4 family) | **To buy** — specific part number TBD on final fit check | LHS / AMain | ~$10-15 / pair | [`bumper_analysis.md`](bumper_analysis.md) |
| **Front gearbox housing** | TBD analysis | — | — | TBD ([`gearbox_housing_analysis.md`](gearbox_housing_analysis.md) — pending) |
| **Rear gearbox housing** | TBD analysis | — | — | TBD ([`gearbox_housing_analysis.md`](gearbox_housing_analysis.md) — pending) |

---

## Cost summary

| Bucket | Sub-total |
|---|---|
| Already in hand (sunk cost — ESC + both diffs) | **$30.00** |
| To buy — locked spec | **$181.99** *(motor $70 + towers $12 + chassis $100)* |
| To buy — pending exact pick (center diff + driveshaft + bumpers + gearbox housings) | **~$50-80 estimated** |
| **Total estimated (chosen + estimated open items)** | **~$260-290** |

---

## Notes

- **ESC sensor adapter:** not needed. The Tekin Pro4 HD uses a dual-plug JST-ZH sensor harness that mates directly with the Fire Phoenix's JST-ZH sensor input. No adapter cable.
- **Cooling fan / heatsink:** not in the BOM. The chosen Pro4 HD 2500KV has the thermal mass to run bare on 4S — see [the cooling weight analysis](motor_analysis.md#real-world-weight-1412-3200kv--cooling-vs-1415-2400kv-bare).
- **Shock tower brace (TRA9061):** [vetoed](shock_tower_analysis.md#related-tower-bracing-optional), not in the BOM.
- **6mm vs 5mm drivetrain:** the in-hand E-Revo diffs dictate 6mm outdrives, which in turn mate the in-hand E-Revo CVDs and axles. Stock Jato/Slash 5mm diffs are physically incompatible — see [differential_analysis.md](differential_analysis.md).
- **Pinion / spur:** TBD, [reference table here](motor_analysis.md#pinion-reference-32p-tbd) — not yet decided.
- **Gearbox housings:** analysis pending. Front and rear gearbox housing options need a dedicated comparison doc.

For everything else (FLM arms, hubs, body, etc.) that's still being researched, see the [main README parts list](README.md#parts-list).
