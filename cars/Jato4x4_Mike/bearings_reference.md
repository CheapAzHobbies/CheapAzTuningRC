# Bearings Reference — Jato4x4_Mike

Not a tuning decision, just the list of bearings this car runs. The baseline is the **Traxxas Jato 4x4 BL-2s (90154-4)** kit, same as the [FastAzJato4x4](../FastAzJato4x4/bearings_reference.md), because both are the same 1/8-class platform. Run sealed (rubber-shielded) bearings throughout for offroad.

> **This car and the FastAz split at exactly one position, the hub.** Both run custom axles that need a **10mm ID** where the EHD hubs came with a **12×18×4**. This car **opens the hub up** and drops a bare **10×18×5** straight in. The FastAz **fills the pocket down** with a sleeve and runs a **10×15×4**. Same problem, two answers.

---

## This car, as built

The hub corners run a **bare 10×18×5**, which is 5mm thick against a 4mm pocket, so **1mm has to come out of something**. On this car it comes out of the **17mm hex adapters**, which get shaved down. **The hub carriers themselves stay stock.**

| Size (mm) | Qty | Where on this car |
|---|---|---|
| **10×18×5** ⚙️ | 4 | **Hub / axle corners, bare, direct into the EHD pocket. The mod** |
| **6×12×4** | 6 | Steering blocks (front), axle carriers (rear) |
| **10×15×4** | 4 | Diff outdrives |
| **12×18×4** | 1 | Transmission / centre driveline |
| **8×16×5** | 2 | Diff inputs, one front one rear |
| **5×8×2.5** | 4 | Steering bellcrank (**TRA5114**, kept as bearings on this car) |
| **5×11×4** | 1 | Centre / slipper |

**Total: 22 bearings**, across **7 distinct sizes**.

> **Note the bellcrank difference.** The FastAz swapped its four **TRA5114** bellcrank bearings for **TRA3775 Oilite bushings**, because a bellcrank only rocks through a small arc and the balls dig into one spot instead of rolling onto fresh metal. **This car still runs the bearings there**, so it is a known future failure point rather than a solved one.

---

## Why this route

Three places the 1mm can come from, and this car picked the second:

| Route | What gets cut | Reversible | Who runs it |
|---|---|---|---|
| **Sleeve the pocket down** | Nothing, you make an 18→15mm sleeve | ✅ yes | [FastAzJato4x4](../FastAzJato4x4/bearings_reference.md) |
| ⭐ **Shave the 17mm hex adapters** | The adapters | ❌ no | **This car** |
| **Deepen the carrier pocket** | 1mm off the carrier, needs a lathe or mill | ❌ no | Nobody, tooling |

**The argument for this route is that there is nothing to make.** No sleeve to print or turn, no press fit to get square. Buy the bearing, shave the adapters, done. The cost is that **the cut is permanent** and the adapters are the part you sacrifice.

**The argument against** is that **10×18×5 is the harder bearing to source.** It is a completely standard size, it is just not one RC cars use, so it comes from a bearing supplier rather than with a hobby order. The FastAz route reuses a **10×15×4** that is already in the parts box for the diff outdrives.

> ⚠️ **Deepening the carrier pocket is technically the best answer** and is bearing-identical to this car, since both end up on the **10×18×5**. It is not used here only because keeping a 1mm cut square in an alloy carrier wants a lathe or mill, and off-axis is worse than either other route.

---

## What the hub bearing costs

| Size (mm) | On the car | Unit price | Line cost | Source |
|---|---|---|---|---|
| **10×18×5** (S61810ZZ, stainless) | 4 | **$1.45** | **$5.80** | $14.45 / 10-pack |

**The hub bearings are the expensive four on this car** at $1.45 each, against **$0.21 to $0.79** for every other size on the [FastAz list](../FastAzJato4x4/bearings_reference.md#what-the-bearings-cost). That is the real price of this route: about **$4.60 more** than the four sleeved 10×15×4 would cost, plus the permanently shaved adapters, in exchange for having nothing to fabricate.

🚧 The remaining sizes on this car have not been costed separately. They match the FastAz sizes, so the [FastAz cost table](../FastAzJato4x4/bearings_reference.md#what-the-bearings-cost) is the closest figure until this car's own orders are logged.

---

## Bearings by position

Since **a bearing position does not disappear when you change what sits in it**, every route totals 22. Only the hub corners differ.

| Position | Stock BL-2S | This car (Mike's) | FastAzJato4x4 |
|:---|:---:|:---:|:---:|
| **Hub / axle** | **12×18×4** ×4 | **10×18×5** ×4 **direct** | **10×15×4** ×4 in an **18 × 15 × 4mm sleeve** |
| What it costs | nothing, it's stock | **shaving the 17mm hex adapters** | printing or turning a sleeve |
| Bearing availability | common | **standard size, just not an RC one** | **already in the parts box** |
| Distinct sizes | 6 | **7** | **6** |
| **Reversible?** | n/a | ❌ no, the adapters are cut | ✅ yes, pull the sleeve |
| Steering blocks / carriers | 6×12×4 ×6 | 6×12×4 ×6 | 6×12×4 ×6 |
| Diff outdrives | 10×15×4 ×4 | 10×15×4 ×4 | 10×15×4 ×4 |
| Diff inputs | 8×16×5 ×2 | 8×16×5 ×2 | 8×16×5 ×2 |
| Transmission / centre | 12×18×4 ×5 total | 12×18×4 ×1 | 12×18×4 ×1 |
| Steering bellcrank | 5×8×2.5 ×4 (TRA5114) | 5×8×2.5 ×4 (TRA5114) | **TRA3775 Oilite bushings ×4** |
| Centre / slipper | 5×11×4 ×1 | 5×11×4 ×1 | 5×11×4 ×1 |
| **Total** | **22** | **22** | **22** (18 bearings + 4 bushings) |

<p align="center"><img src="../FastAzJato4x4/src/suspension_bearing_tra5117_6x12x4.jpg" height="150">&nbsp;<img src="../FastAzJato4x4/src/suspension_bearing_tra5119_10x15x4.jpg" height="150">&nbsp;<img src="../FastAzJato4x4/src/suspension_bearing_tra5120_12x18x4.jpg" height="150"><br><em>TRA5117 6×12×4 · TRA5119 10×15×4 · TRA5120A 12×18×4. 🚧 no photo of the 10×18×5 yet</em></p>

---

## Notes

- **The hexes are the consumable here.** Shaving them is what buys the bigger bearing, so treat a shaved 17mm hex as a wear part. See [`hub_analysis.md`](hub_analysis.md#17mm-wheel-hexes) for which hex and why the solid screw-pin design makes the cut riskier.
- **The bellcrank bearings are a known weak spot that has not been addressed.** The FastAz moved to Oilite bushings after the bearings chewed the steering post. The same failure is available on this car.
- **Sizes and quantities are inherited, not independently verified.** The FastAz list was checked against the Avid kit for the Jato 4x4 BL-2S (90154-4) and the Traxxas exploded views. This car shares the platform, so the same counts apply, but **this car's own bearings have not been physically counted**.
