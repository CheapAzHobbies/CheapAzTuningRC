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

**The one axle deviation:** the custom axles (**Tekno stubs + the Traxxas knock-off CVDs**) need a smaller-ID bearing than the Raptor R EHD hubs' **12×18×4**. Two ways to get there, a bare **10×18×5** dropped in, or a **10×15×4 in a sleeve**. This car runs the sleeve. Dropping the ID from 12mm to 10mm (and going **5mm** thick, a common off-the-shelf size, vs a non-standard 10×18×4) is what lets the Tekno M6 stub seat. **Fitted and running.** Full reasoning in [`hub_carrier_analysis.md`](hub_carrier_analysis.md#bearings--hardware).

**Alternative (no special bearing to buy):** turn a thin **brass bushing / sleeve (15mm ID → 18mm OD)** to fill the gap between the hub's 18mm pocket and a **10×15×4** bearing, press-fit it in with retaining compound (green Loctite), then run four **10×15×4** (a cheap, common size). Their **10mm ID already fits the Tekno stub**, so this path skips the 10×18×5 entirely. Trade-off: a bit of machining/press work per corner vs just dropping in the off-the-shelf 10×18×5.

**Why sleeve at all rather than buy the bigger bearing:** **10×15×4 is far easier to source** than a 10×18×5, and this car already runs four of them in the diff outdrives, so it's one size to stock instead of two. The bare 10×18×5 route also means **shaving the hubs**, which is what [Mike's Jato](../Jato4x4_Mike/README.md) had to do.

**Third option, printed instead of turned:** the same sleeve can just be **3D printed**, **18mm OD, 15mm ID, 4mm thick**, which drops a common **10×15×4** bearing into the hub's 18mm pocket with no machining and nothing to shave down. It also lands the track width exactly where it should be, **1mm per side**, rather than chasing it by trimming a 17mm adapter. Print it in something dimensionally stable, PETG rather than PLA, and retain it the same way with green Loctite. 🚧 Not printed or fitted yet, so treat the fit as unverified. Worth saving the STL into `3d-models/` once it's made.

Everything else follows the baseline: diffs are back to **stock Jato 4x4 (5mm)**, and the front/rear hubs are **Traxxas Raptor R Ultimate EHD alloy** (same 6×12×4 / 12×18×4 EHD bearing sizes as the kit).

---

## This car, as built (modded)

The actual bearing list running on FastAzJato4x4: the hub axle bearings are **10×15×4 in a sleeve**, not a bare 10×18×5. The sleeve fills the hub's 18mm pocket down to 15mm, so a common cheap bearing does the job and **nothing has to be shaved**. The rest is the stock kit.

> **[Mike's Jato](../Jato4x4_Mike/README.md) took the other route:** a **larger bearing straight into the inner wheel hub**, which works but **means shaving the hubs to make it fit**. Same problem, two answers. This car sleeves the pocket down, his opens the hub up.

| Size (mm) | Qty | Where on this car |
|---|---|---|
| **10×15×4** ⚙️ | 4 | **Custom axle hubs (Tekno stub + knock-off CVD), in an 18→15mm sleeve, the mod** |
| **6×12×4** | 6 | Wheel hubs / axle carriers |
| **12×18×4** | 1* | Transmission / center driveline (the non-hub one) |
| **10×15×4** | 4 | Diff outdrives (same size as the hubs above, 8 total on the car) |
| **8×16×5** | 2 | Diff inputs |
| **5×8×2.5** | 4 | Steering bellcrank |
| **5×11×4** | 1 | Center / slipper |

**Total: 22 bearings** (same count as OG, four hub 12×18×4 swapped to 10×15×4 in sleeves).

> **\*** The OG kit lists five 12×18×4 without a published per-position split; this assumes four of them sit in the hub corners (now 10×18×5) and one stays in the transmission/center. Confirm against the actual hardware. If you take the **brass-bushing alternative** above, drop the 10×18×5 row and add four more **10×15×4** (sleeved) instead.


---

## Three builds side by side

The hub bearing is the only thing that differs. Everything else is the stock BL-2S set.

| Position | Stock BL-2S | This car (FastAz) | Mike's Jato |
|:---|:---:|:---:|:---:|
| **Hub / axle** | **12×18×4** ×4 | **10×15×4** ×4 **in an 18→15mm sleeve** | **10×18×5** ×4 **direct** |
| What it costs | nothing, it's stock | printing or turning a sleeve | **shaving the hubs to fit** |
| Bearing availability | common | **common, and shared with the diff outdrives** | harder to find |
| Distinct sizes to stock | 6 | **6** | **7** |
| Wheel hubs / carriers | 6×12×4 ×6 | 6×12×4 ×6 | 6×12×4 ×6 |
| Diff outdrives | 10×15×4 ×4 | 10×15×4 ×4 | 10×15×4 ×4 |
| Diff inputs | 8×16×5 ×2 | 8×16×5 ×2 | 8×16×5 ×2 |
| Transmission / centre | 12×18×4 ×5 total | 12×18×4 ×1 | 12×18×4 ×1 |
| Steering bellcrank | 5×8×2.5 ×4 | 5×8×2.5 ×4 | 5×8×2.5 ×4 |
| Centre / slipper | 5×11×4 ×1 | 5×11×4 ×1 | 5×11×4 ×1 |
| **Total** | **22** | **22** | **22** |

**Why the split happened.** Both cars run custom axles (Tekno stubs on knock-off CVDs) which need a **10mm ID** where the Raptor R EHD hubs came with **12×18×4**. Getting a 10mm ID into an 18mm pocket has two answers: fill the pocket down to a bearing you can buy, or open the hub up to take a bigger one.

**This car sleeves it.** No machining, and the **10×15×4 is already in the parts box** for the diff outdrives, so it adds no new size to the parts box, and it's the easier bearing to find.

**Mike's opens the hub.** A bare 10×18×5 drops straight in once the hubs are shaved, so no sleeve to make, but it's a permanent modification to the hubs and a bearing that's harder to source.

🚧 Mike's list is inferred from the hub bearing being the only stated difference. Confirm the rest against his car before ordering off it.



Sources: [Avid Jato 4x4 BL-2s kit (90154-4)](https://www.avidrc.com/flexkit/?kit=4380&kitname=Jato+4x4+BL-2S+%2890154-4%29) · [Avid Jato 4x4 BL-2s](https://www.rcteam.com/en/products/avid-complete-bearing-kit-traxxas-jato-4x4-bl-2s-av-trx-jto-4x4-bl2s)
