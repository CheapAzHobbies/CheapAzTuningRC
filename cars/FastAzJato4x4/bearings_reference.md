# Bearings Reference — FastAzJato4x4

Not a tuning decision, just the full list of bearings the build needs. The baseline matches the **Traxxas Jato 4x4 BL-2s (90154-4) complete bearing kit**, it's a 1/8-class platform, so bigger bearings than a Slash 4x4. Run sealed (rubber-shielded) bearings throughout for offroad. Two tables below: the **OG stock-kit baseline**, and the **as-built list for this car** with the axle mod applied.

## OG — Stock Jato 4x4 BL-2s kit (baseline)

| Size (mm) | Qty | Typical location |
|---|---|---|
| **6×12×4** | 6 | Wheel hubs / axle carriers |
| **12×18×4** | 5 | Diffs + transmission / center driveline |
| **10×15×4** | 4 | Hubs / diff outdrives |
| **8×16×5** | 2 | Diff inputs |
| **5×8×2.5** | 4 | Steering bellcrank |
| **5×11×4** | 1 | Center / slipper |

**Total: 22 bearings.**

> The "typical location" column is best-effort, Avid doesn't publish the exact per-position split. Pop everything apart and confirm sizes against the actual hardware before ordering.

---

## What changed on this car

**The one axle deviation, confirmed and working:** the custom axles (**Tekno stubs + the Traxxas knock-off CVDs**) run a **10×18×5** hub bearing at **all four corners (×4)** in place of the Raptor R EHD hubs' **12×18×4** axle bearing. Dropping the ID from 12mm to 10mm (and going **5mm** thick, a common off-the-shelf size, vs a non-standard 10×18×4) is what lets the Tekno M6 stub seat. **Fitted and running.** Full reasoning in [`hub_carrier_analysis.md`](hub_carrier_analysis.md#bearings--hardware).

**Alternative (no special bearing to buy):** turn a thin **brass bushing / sleeve (15mm ID → 18mm OD)** to fill the gap between the hub's 18mm pocket and a **10×15×4** bearing, press-fit it in with retaining compound (green Loctite), then run four **10×15×4** (a cheap, common size). Their **10mm ID already fits the Tekno stub**, so this path skips the 10×18×5 entirely. Trade-off: a bit of machining/press work per corner vs just dropping in the off-the-shelf 10×18×5.

Everything else follows the baseline: diffs are back to **stock Jato 4x4 (5mm)**, and the front/rear hubs are **Traxxas Raptor R Ultimate EHD alloy** (same 6×12×4 / 12×18×4 EHD bearing sizes as the kit).

---

## This car, as built (modded)

The actual bearing list running on FastAzJato4x4: the four hub axle bearings are **10×18×5** for the Tekno-stub / knock-off-CVD axles; the rest is the stock kit.

| Size (mm) | Qty | Where on this car |
|---|---|---|
| **10×18×5** ⚙️ | 4 | **Custom axle hubs (Tekno stub + knock-off CVD), the mod** |
| **6×12×4** | 6 | Wheel hubs / axle carriers |
| **12×18×4** | 1* | Transmission / center driveline (the non-hub one) |
| **10×15×4** | 4 | Diff outdrives |
| **8×16×5** | 2 | Diff inputs |
| **5×8×2.5** | 4 | Steering bellcrank |
| **5×11×4** | 1 | Center / slipper |

**Total: 22 bearings** (same count as OG, four hub 12×18×4 swapped to 10×18×5).

> **\*** The OG kit lists five 12×18×4 without a published per-position split; this assumes four of them sit in the hub corners (now 10×18×5) and one stays in the transmission/center. Confirm against the actual hardware. If you take the **brass-bushing alternative** above, drop the 10×18×5 row and add four more **10×15×4** (sleeved) instead.

---

Sources: [Avid Jato 4x4 BL-2s kit (90154-4)](https://www.avidrc.com/flexkit/?kit=4380&kitname=Jato+4x4+BL-2S+%2890154-4%29) · [Avid Jato 4x4 BL-2s](https://www.rcteam.com/en/products/avid-complete-bearing-kit-traxxas-jato-4x4-bl-2s-av-trx-jto-4x4-bl2s)
