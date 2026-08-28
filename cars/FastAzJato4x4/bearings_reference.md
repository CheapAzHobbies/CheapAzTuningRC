# Bearings Reference — FastAzJato4x4

Not a tuning decision, just the full list of bearings the build needs. The baseline matches the **Traxxas Jato 4x4 BL-2s (90154-4) complete bearing kit**, it's a 1/8-class platform, so bigger bearings than a Slash 4x4. Run sealed (rubber-shielded) bearings throughout for offroad. Two tables below: the **OG stock-kit baseline**, and the **as-built list for this car** with the axle mod applied.

## OG — Stock Jato 4x4 BL-2s kit (baseline)

| Size (mm) | Qty | Typical location |
|---|---|---|
| **6×12×4** | 6 | **5117 / 5117A**, steering blocks (front), axle carriers (rear) |
| **12×18×4** | 5 | **5120 / 5120A**, the hub / axle carrier bearing, front and rear |
| **10×15×4** | 4 | **5119 / 5119A**, differentials **and the transmission**, not the hubs |
| **8×16×5** | 2 | **5118**, diff inputs, one front one rear |
| **5×8×2.5** | 4 | **TRA5114** ball bearing, steering bellcrank. **Swapped out on this car** for **TRA3775** Oilite bushings, same 5×8×2.5 |
| **5×11×4** | 1 | Center / slipper |

**Total: 22 bearings.**

> ✅ **Sizes and quantities verified 2026-08-27** against the [Avid complete kit for the Jato 4x4 BL-2S (90154-4)](https://avidrc.com/flexkit/?kit=4380), which lists 6×12×4 ×6, 12×18×4 ×5, 5×8×2.5 ×4, 10×15×4 ×4, 8×16×5 ×2, 5×11×4 ×1. All six match, 22 total.
>
> ✅ **Positions confirmed from the Traxxas exploded views** (Jato 4x4, 90386-4, rev 250801, front / rear / transmission sheets) by reading the part number printed beside each bearing. Free to view on [traxxas.com](https://traxxas.com/parts-finder), not reproduced here since the drawings are Traxxas copyright.
>
> **Two things that corrects:** the **12×18×4 is the hub bearing**, not a diff or transmission one, and the **10×15×4 runs in the transmission as well as the diffs**, not in the hubs. 🚧 Per-position quantities still want a physical count, since a drawing labels a part number once even where it appears at both corners.

---

## What changed on this car

**The one axle deviation.** The custom axles (Tekno stubs on knock-off CVDs) need a **10mm ID** where the Raptor R EHD hubs came with **12×18×4**. Two ways to get a 10mm ID into an 18mm pocket:

| | Sleeve it down ⭐ *this car* | Open it up *(Mike's)* |
|:---|:---|:---|
| **Bearing** | 10×15×4 | 10×18×5 |
| **Needs** | a sleeve, 18mm OD × 15mm ID × 4mm | the 17mm hex adapters shaved down |
| **Make it** | ✅ **printed in PETG, fitted and working**, or turn it in brass | nothing to make |
| **Sourcing** | easy, already in the diff outdrives | harder, and a 7th size to stock |
| **Permanent?** | no | yes, the adapters are cut |

Press the sleeve in with green Loctite. ✅ **The printed version is fitted and working**, so no lathe needed. 🚧 Save the STL into `3d-models/`.

Everything else follows the baseline: diffs are back to **stock Jato 4x4 (5mm)**, and the front/rear hubs are **Traxxas Raptor R Ultimate EHD alloy** (same 6×12×4 / 12×18×4 EHD bearing sizes as the kit).

---

## This car, as built (modded)

The actual bearing list running on FastAzJato4x4: the hub axle bearings are **10×15×4 in a sleeve**, not a bare 10×18×5. The sleeve fills the hub's 18mm pocket down to 15mm, so a common cheap bearing does the job and **nothing has to be shaved**. The rest is the stock kit.

> **[Mike's Jato](../Jato4x4_Mike/README.md) took the other route:** a **larger bearing straight into the inner wheel hub**, which works but **means shaving down the 17mm hex adapters to clear it**, not the hub carriers. Same problem, two answers. This car sleeves the pocket down, his opens the hub up.

| Size (mm) | Qty | Where on this car |
|---|---|---|
| **10×15×4** ⚙️ | 4 | **Custom axle hubs (Tekno stub + knock-off CVD), in an 18→15mm sleeve, the mod** |
| **6×12×4** | 6 | Wheel hubs / axle carriers |
| **12×18×4** | 1* | Transmission / center driveline (the non-hub one) |
| **10×15×4** | 4 | Diff outdrives (same size as the hubs above, 8 total on the car) |
| **8×16×5** | 2 | Diff inputs |
| ~~**5×8×2.5**~~ | 0 | **Not fitted.** The four **TRA5114** bellcrank bearings were swapped for **TRA3775** Oilite bushings |
| **5×11×4** | 1 | Center / slipper |

**Total: 18 ball bearings + 4 Oilite bushings** (22 positions, same as OG). Two swaps from stock: the four hub **12×18×4** became **10×15×4 in sleeves**, and the four bellcrank **TRA5114** bearings became **TRA3775** bushings. **The bearings lock up and chew the steering post**, because a bell crank only rocks through a tiny arc so the balls dig into the same spot instead of rolling onto fresh metal. The bushings just slide, and the post survives. Full reasoning in [`steering_bell_crank_analysis.md`](steering_bell_crank_analysis.md#key-requirements) (see [`steering_bell_crank_analysis.md`](steering_bell_crank_analysis.md)).

> **\*** **The split follows from the count.** A bearing position doesn't disappear when you change what sits in it, so **all three builds total 22**. The mod swaps the **four hub corners**, so of the five stock 12×18×4 exactly **four were hub axle positions** and **one is the transmission/centre**. That's arithmetic rather than an assumption, though it does rest on the hub corners having been 12×18×4 in the first place, which is what the Raptor R EHD hubs take.


---

## Three builds side by side

The hub bearing is the only thing that differs. Everything else is the stock BL-2S set, and since **a bearing position doesn't disappear when you change what sits in it**, **all three builds total 22**. Only the size in the hub corners changes.

| Position | Stock BL-2S | This car (FastAz) | Mike's Jato |
|:---|:---:|:---:|:---:|
| **Hub / axle** | **12×18×4** ×4 | **10×15×4** ×4 in an **18 × 15 × 4mm sleeve** | **10×18×5** ×4 **direct** |
| What it costs | nothing, it's stock | printing or turning a sleeve, **18mm OD × 15mm ID × 4mm** | **shaving down the 17mm hex adapters** |
| Bearing availability | common | **common, and shared with the diff outdrives** | harder to find |
| Distinct sizes to stock | 6 | **6** | **7** |
| Wheel hubs / carriers | 6×12×4 ×6 | 6×12×4 ×6 | 6×12×4 ×6 |
| Diff outdrives | 10×15×4 ×4 | 10×15×4 ×4 | 10×15×4 ×4 |
| Diff inputs | 8×16×5 ×2 | 8×16×5 ×2 | 8×16×5 ×2 |
| Transmission / centre | 12×18×4 ×5 total | 12×18×4 ×1 | 12×18×4 ×1 |
| Steering bellcrank | 5×8×2.5 ×4 (TRA5114) | **TRA3775 Oilite bushings ×4** | 5×8×2.5 ×4 (TRA5114) |
| Centre / slipper | 5×11×4 ×1 | 5×11×4 ×1 | 5×11×4 ×1 |
| **Total positions** | **22** | **22** (18 bearings + 4 bushings) | **22** |

**Why the split happened.** Both cars run custom axles (Tekno stubs on knock-off CVDs) which need a **10mm ID** where the Raptor R EHD hubs came with **12×18×4**. Getting a 10mm ID into an 18mm pocket has two answers: fill the pocket down to a bearing you can buy, or open the hub up to take a bigger one.

**This car sleeves it.** No machining, and the **10×15×4 is already in the parts box** for the diff outdrives, so it adds no new size to the parts box, and it's the easier bearing to find.

**Mike's opens the hub.** A bare 10×18×5 drops straight in, but the **17mm hex adapters have to be shaved down** to clear it. **That's the adapters, not the hub carriers**, which stay stock. No sleeve to make, but it's a permanent cut on the adapters and a bearing that's harder to source.

🚧 Mike's list is inferred from the hub bearing being the only stated difference. Confirm the rest against his car before ordering off it.



Sources: [Avid Jato 4x4 BL-2s kit (90154-4)](https://www.avidrc.com/flexkit/?kit=4380&kitname=Jato+4x4+BL-2S+%2890154-4%29) · [Avid Jato 4x4 BL-2s](https://www.rcteam.com/en/products/avid-complete-bearing-kit-traxxas-jato-4x4-bl-2s-av-trx-jto-4x4-bl2s)
