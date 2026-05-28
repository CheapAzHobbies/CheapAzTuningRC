# Bill of Materials — FastAzJato4x4

Items decided by the analysis docs in this folder. Only parts with a clear pick **and** documented cost are listed — items marked TBD or in active research live in the [README's Parts List](README.md#parts-list) and the [TODO / Notes](README.md#todo--notes) section.

> See the linked analysis docs for the reasoning behind each pick.

---

## Electronics

| Part | Status | Source | Price | Decided by |
|---|---|---|---|---|
| **Fire Phoenix XeRun 120A Enhanced (Speed Dragon)** ESC | **In Hand** | Temu / AliExpress | $30.00 (sunk) | [`esc_analysis.md`](esc_analysis.md) |
| **Tekin Pro4 HD 2500KV** brushless motor (#TT2521) | **To buy** | [Tekin direct](https://store.teamtekin.com/pro4-hd-2500kv-brushless-motor/) | $69.99 | [`motor_analysis.md`](motor_analysis.md) |

---

## Suspension

| Part | Status | Source | Price | Decided by |
|---|---|---|---|---|
| **Traxxas #9033 — stock composite front shock tower** | **To buy** (or pull from spares — Traxxas spare commonly stocked at local hobby stores) | LHS / Traxxas / AMain | ~$6.00 | [`shock_tower_analysis.md`](shock_tower_analysis.md) |
| **Traxxas #9034 — stock composite rear shock tower** | **To buy** | LHS / Traxxas / AMain | ~$6.00 | [`shock_tower_analysis.md`](shock_tower_analysis.md) |

---

## Cost summary

| Bucket | Sub-total |
|---|---|
| Already in hand (sunk cost) | **$30.00** |
| To buy | **$81.99** |
| **Total (build to chosen-spec)** | **$111.99** |

---

## Notes

- **ESC sensor adapter:** not needed. The Tekin Pro4 HD uses a dual-plug JST-ZH sensor harness that mates directly with the Fire Phoenix's JST-ZH sensor input. No adapter cable.
- **Cooling fan / heatsink:** not in the BOM. The chosen Pro4 HD 2500KV has the thermal mass to run bare on 4S — see [the cooling weight analysis](motor_analysis.md#real-world-weight-1412-3200kv--cooling-vs-1415-2400kv-bare).
- **Shock tower brace (TRA9061):** [vetoed](shock_tower_analysis.md#related-tower-bracing-optional), not in the BOM.
- **Pinion / spur:** TBD, [reference table here](motor_analysis.md#pinion-reference-32p-tbd) — not yet decided.

For everything else (chassis, arms, hubs, body, etc.) that's still being researched, see the [main README parts list](README.md#parts-list).
