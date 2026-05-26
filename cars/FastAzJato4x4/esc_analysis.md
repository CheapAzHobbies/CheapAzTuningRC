# ESC Selection — FastAzJato4x4

> **Status: Undecided.** Build runs 4S. Motor not yet chosen — ESC selection depends partly on motor sensor connector.

---

## Key Requirements

- **4S LiPo** — ESC must support 16.8V input
- **Sensored** — smooth starts, no cogging; motor sensor connector compatibility matters
- **Splash/water resistance** — outdoor buggy, not a pool toy but needs protection
- **1/10–1/8 scale current capacity** — 36mm stator motors pull significant amps

---

## ESC Comparison

| ESC | Cells | Amps (cont) | Weight | Waterproof | Sensored | Status | Why Choose | Why Not | Photo / Link |
|---|---|---|---|---|---|---|---|---|---|
| **Fire Phoenix XeRun 120A Enhanced (Speed Dragon)** | **2-4S** | **120A** | **105g** | **Full submersion (user verified)** | **Yes (JST-ZH)** | **In Hand** | Already owned and proven on 4S with 3200KV on Slash 4x4 — zero cost, fully waterproof (full soak), sensored, comes with fan | 120A continuous is the lowest amp rating here; Chinese market rebrand; 4S ceiling no headroom | <a href="https://www.aliexpress.com/item/4001205164437.html"><img src="https://oss.hobbywing.com/cars/XeRun/XeRunXR8SCT/1.png" width="80"></a> |
| **HobbyWing EZRun MAX10 G2 140A** | 2-4S | 140A | 120g | IP67 | Yes (proprietary G3 port) | **Candidate** | Sold as combo with EZRun 3665SD G3 — native sensor plug match, IP67, lightest HW option | 4S ceiling (no headroom), proprietary sensor port needs adapter for non-EZRun G3 motors | <a href="https://www.hobbywingdirect.com/products/ezrun-max10-g2-esc"><img src="https://oss.hobbywing.com/EZRUN%20MAX10%20G2/enimage/img1.png" width="80"></a> |
| **Castle Mamba X** | 2-6S | ~180A* | 101g | Yes (epoxy) | Yes (SmartSense) | **Candidate** | Lightest ESC in the list, 6S rated so 4S is well within spec, works natively with Castle motors | Amps not published by Castle; no IP rating (potted epoxy, not IP-rated) | <a href="https://www.castlecreations.com/en/mamba-x-esc-010-0155-00"><img src="https://castlecreationscom-2.azureedge.net/img/product/Mamba_X_10th_Scale-18-B.jpg" width="80"></a> |
| **Castle Mamba Monster X** | 2-6S | ~200A* | 111g | Yes (epoxy) | Yes (SmartSense) | **Candidate** | True 1/8 scale power handling, 6S overhead, works natively with Castle motors | Amps not published; slightly heavier than Mamba X; 1/8 overkill for 36mm motors | <a href="https://www.castlecreations.com/en/mamba-monster-x-esc-010-0145-00"><img src="https://castlecreationscom-1.azureedge.net/img/product/010-0145-00_1-B.jpg" width="80"></a> |
| **HobbyWing XeRun XR8 SCT** | 2-4S | 140A | 91g | **NO** | Yes (JST-ZH) | Candidate (dry only) | Lightest HW option, competition-grade, full sensored, works with standard JST-ZH motors | **Not waterproof** — confirmed by HobbyWing spec sheet; 4S ceiling | <a href="https://www.hobbywingdirect.com/collections/xerun-xr8-esc/sct"><img src="https://oss.hobbywing.com/cars/XeRun/XeRunXR8SCT/1.png" width="80"></a> |
| **Castle Copperhead 10** | 2-4S | ~100A* | 71g | Yes (epoxy) | Yes (SmartSense) | Candidate (budget) | Lightest and cheapest option, waterproof, sensored, 4S capable | 4S ceiling, lower amp headroom, designed for lighter 1/10 vehicles | <a href="https://www.castlecreations.com/en/copperhead-10-16-8v-wp-sensored-esc-010-0166-00"><img src="https://castlecreationscom-1.azureedge.net/img/product/900x900_010-0166-00_(2)-B.jpg" width="80"></a> |
| HobbyWing EZRun MAX8 G2S | 3-6S | 160A | 192g | IP67 | Yes (JST-ZH) | Ruled Out | Highest amp headroom, IP67, 6S | Way too heavy at 192g for a 1/10 build on 36mm motors | <a href="https://www.hobbywingdirect.com/products/ezrun-max8-esc-g2"><img src="https://oss.hobbywing.com/cars/EzRun/EzRunMaxG2S/1.png" width="80"></a> |

*Castle does not publish continuous amp ratings for surface ESCs.*

---

## Sensor Connector Compatibility

| ESC | Castle 1412 / 1415 | HW XeRun 3660SD G3 | HW EZRun 3665SD G3 | HW EZRun 3652SD G3 |
|---|---|---|---|---|
| **Fire Phoenix XeRun 120A Enhanced** | Works | Works (JST-ZH) | Needs adapter (HWA30810007) | Works (JST-ZH) |
| HobbyWing EZRun MAX10 G2 | Works | Works (JST-ZH) | **Native fit (proprietary G3 port)** | Works (JST-ZH) |
| HobbyWing XeRun XR8 SCT | Works | Works (JST-ZH) | Needs adapter (HWA30810007) | Works (JST-ZH) |
| Castle Mamba X | **Native (SmartSense)** | Works | Needs adapter | Works |
| Castle Mamba Monster X | **Native (SmartSense)** | Works | Needs adapter | Works |
| Castle Copperhead 10 | **Native (SmartSense)** | Works | Needs adapter | Works |

---

## Detailed Notes

### Fire Phoenix XeRun 120A Enhanced (Speed Dragon) — In Hand

- Chinese market rebrand of the HobbyWing XeRun 120A Enhanced (强化速龙). Not the standard V3.1 — that's 2-3S only. The enhanced version is 2-4S and waterproof.
- User-confirmed: proven on 4S with 3200KV on a Slash 4x4, zero issues. Cost ~$30 on Temu/AliExpress.
- **Specs confirmed from listing:**
  - Voltage: 2-4S LiPo
  - Continuous / Burst: 120A / 760A
  - Resistance: 0.0003 ohm
  - BEC: 6V/5A or 7.4V/5A (solder mod — done on user's units)
  - Dimensions: 43 × 36 × 33mm
  - Weight: **105g**
  - Fan: included, powered directly from battery (5V/0.16A, max 8V)
- **Fully waterproof — user confirmed full submersion, not just splash resistant.** Surprisingly capable for a $30 Chinese ESC.
- Sensor input: JST-ZH — works with Castle 1412/1415 and standard HobbyWing motors. Needs adapter (HWA30810007) for EZRun 3665SD G3 proprietary plug.
- Zero cost — already in hand.

### HobbyWing EZRun MAX10 G2 140A

- IP67 — the only HobbyWing ESC in this range with a full IP rating
- Designed specifically as a combo unit with the EZRun 3665SD G3 motor (proprietary waterproof sensor port lines up directly)
- If running a Castle or standard JST-ZH motor, needs the HobbyWing Sensor Adapter Cable (HWA30810007)
- 4S ceiling — no voltage headroom above the build requirement
- 120g with wires, 53 × 39.5 × 37.2mm

### HobbyWing XeRun XR8 SCT

- **Not waterproof** — HobbyWing's own spec sheet lists waterproof: No. Confirmed. This is a competition ESC not intended for wet conditions.
- Competition XeRun tier — tighter tolerances, more aggressive timing options
- 90.5g, 54.1 × 37.2 × 36.1mm
- Best pick only if the build stays dry (indoor track, no puddles)

### HobbyWing EZRun MAX8 G2S

- Built for 1/8 scale trucks and buggies with big motors — overkill for 36mm stator
- 192g is the heaviest ESC on this list by far
- 3-6S, IP67, 160A — technically covers everything but adds unnecessary weight

### Castle Mamba X

- 2-6S, so 4S is well within the comfortable operating range (not pushing the voltage ceiling)
- Waterproof via CNC aluminum + potted epoxy — not IP-rated but Castle considers it waterproof
- SmartSense sensored mode works natively with Castle 1412 and 1415 motors
- For HobbyWing EZRun 3665SD G3 with proprietary plug: needs adapter
- 101g, 54.4 × 35.2 × 30.0mm
- Datalogging built in

### Castle Mamba Monster X

- The 1/8 scale version of the Mamba X — slightly larger and heavier but same voltage range
- More appropriate current capacity for heavy 1/8 builds; marginal benefit here on a lighter Jato platform
- 111g, 53 × 49 × 36.4mm

### Castle Copperhead 10

- Budget/entry-level Castle sensored option — 4S max, waterproof, sensored
- Lightest ESC on the list at 71g
- Designed for 1/10 vehicles up to ~7.5lb — the Jato build may be at the upper edge of what this ESC was meant for
- Good value if budget is a factor and 4S ceiling is acceptable

---

## Summary

| | Fire Phoenix 120A | MAX10 G2 | Mamba X | Mamba Monster X | XR8 SCT | Copperhead 10 |
|---|---|---|---|---|---|---|
| Max cells | 4S | 4S | 6S | 6S | 4S | 4S |
| 4S headroom | Tight | Tight | Comfortable | Comfortable | Tight | Tight |
| Waterproof | **Full soak** | IP67 | Yes (epoxy) | Yes (epoxy) | **No** | Yes (epoxy) |
| Weight | 105g | 120g | 101g | 111g† | 91g | 71g |
| Castle motor (native) | Works | Adapter | SmartSense | SmartSense | Works | SmartSense |
| EZRun 3665SD G3 (native) | Adapter | **Yes** | Adapter | Adapter | Adapter | Adapter |
| Price (approx) | **$0 (in hand)** | ~$85 | ~$125 | ~$135 | ~$125 | ~$70 |

†Mamba Monster X listed without battery connector — add ~10–15g for installed weight

**Pairing logic:**
- Running **Castle 1412 (in hand), want to spend $0 on ESC** → Fire Phoenix in hand is the obvious pick — proven combo
- Running **EZRun 3665SD G3 2400KV** → MAX10 G2 is the native matched combo; Fire Phoenix needs adapter
- Want **6S upgrade path** later → Mamba X or Mamba Monster X only (all 4S ESCs are dead ends if voltage goes up)
- **Budget** → Copperhead 10 or Fire Phoenix (in hand) cover 4S + sensored + waterproof for the least money
- **Best overall for this build** → Fire Phoenix if staying with Castle motor; MAX10 G2 if going EZRun 3665SD G3
