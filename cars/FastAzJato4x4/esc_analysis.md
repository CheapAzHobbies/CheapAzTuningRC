# ESC Selection — FastAzJato4x4

> **Status: Undecided.** Build runs 4S. Motor not yet chosen — ESC selection depends partly on motor sensor connector.

---

## Key Requirements

- **4S LiPo** — ESC must support 16.8V input
- **Sensored** — smooth starts, no cogging; motor sensor connector compatibility matters
- **Waterproof — hard requirement.** If it's not waterproof it's not being used. Non-waterproof ESCs are ruled out regardless of other specs.
- **Sensored — hard requirement.** Must support sensored motor operation for smooth starts and low-speed control.
- **1/10–1/8 scale current capacity** — 36mm stator motors pull significant amps

---

## ESC Comparison

| ESC | Spec | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **Fire Phoenix XeRun 120A Enhanced (Speed Dragon)** | Cells: **2-4S**<br>Amps: **120A**<br>Weight: **105g**<br>Waterproof: **Full submersion (user verified)**<br>Sensored: **Yes (JST-ZH)** | **In Hand** | Pro: Already owned and proven on 4S with 3200KV on Slash 4x4 — zero cost, fully waterproof (full soak), sensored, comes with fan<br>Con: Lower amp rating than the Hobbywing / Castle Mamba options; Chinese market rebrand; 4S ceiling no headroom | <a href="https://www.aliexpress.com/item/4001205164437.html"><img src="src/electronics_firephoenix_xerun_120a_esc.jpg" width="300"></a> |
| **HobbyWing EZRun MAX10 G2 140A** | Cells: 2-4S<br>Amps: 140A<br>Weight: 120g<br>Waterproof: IP67<br>Sensored: Yes (proprietary G3 port) | **Candidate** | Pro: Sold as combo with EZRun 3665SD G3 — native sensor plug match, IP67, lightest waterproof HW option<br>Con: 4S ceiling (no headroom), proprietary sensor port needs adapter for non-EZRun G3 motors | <a href="https://www.hobbywingdirect.com/products/ezrun-max10-g2-esc"><img src="src/electronics_hobbywing_ezrun_max10_g2_hw30102603.jpg" width="300"></a> |
| **Castle Mamba X** | Cells: 2-6S<br>Amps: ~180A*<br>Weight: 101g<br>Waterproof: Yes (epoxy)<br>Sensored: Yes (SmartSense) | **Candidate** | Pro: Lightest 6S-capable ESC in the list, 6S rated so 4S is well within spec, works natively with Castle motors<br>Con: Amps not published by Castle; no IP rating (potted epoxy, not IP-rated) | <a href="https://www.castlecreations.com/en/mamba-x-esc-010-0155-00"><img src="https://castlecreationscom-2.azureedge.net/img/product/Mamba_X_10th_Scale-18-B.jpg" width="300"></a> |
| **Castle Mamba Monster X** | Cells: 2-6S<br>Amps: ~200A*<br>Weight: 111g<br>Waterproof: Yes (epoxy)<br>Sensored: Yes (SmartSense) | **Candidate** | Pro: True 1/8 scale power handling, 6S overhead, works natively with Castle motors<br>Con: Amps not published; slightly heavier than Mamba X; 1/8 overkill for 36mm motors | <a href="https://www.castlecreations.com/en/mamba-monster-x-esc-010-0145-00"><img src="https://castlecreationscom-1.azureedge.net/img/product/010-0145-00_1-B.jpg" width="300"></a> |
| ~~HobbyWing XeRun XR8 SCT~~ | Cells: 2-4S<br>Amps: 140A<br>Weight: 91g<br>Waterproof: **NO**<br>Sensored: Yes (JST-ZH) | **Ruled Out** | Pro: Second lightest ESC on the list (after Copperhead), competition-grade<br>Con: **Not waterproof — hard no for this build** | <a href="https://www.hobbywingdirect.com/collections/xerun-xr8-esc/sct"><img src="src/electronics_hobbywing_xerun_xr8_sct_hwa30113301.jpg" width="300"></a> |
| **Castle Copperhead 10** | Cells: 2-4S<br>Amps: ~100A*<br>Weight: 71g<br>Waterproof: Yes (epoxy)<br>Sensored: Yes (SmartSense) | Candidate (budget) | Pro: Lightest on the list and cheapest to buy new, waterproof, sensored, 4S capable<br>Con: 4S ceiling, lower amp headroom, designed for lighter 1/10 vehicles | <a href="https://www.castlecreations.com/en/copperhead-10-16-8v-wp-sensored-esc-010-0166-00"><img src="https://castlecreationscom-1.azureedge.net/img/product/900x900_010-0166-00_(2)-B.jpg" width="300"></a> |
| HobbyWing EZRun MAX8 G2S | Cells: 3-6S<br>Amps: 160A<br>Weight: 192g<br>Waterproof: IP67<br>Sensored: Yes (JST-ZH) | Ruled Out | Pro: Highest published amp rating among the Hobbywing options, IP67, 6S<br>Con: Way too heavy at 192g for a 1/10 build on 36mm motors | <a href="https://www.hobbywingdirect.com/products/ezrun-max8-esc-g2"><img src="src/electronics_hobbywing_ezrun_max8_g2s.jpg" width="300"></a> |

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
- User-confirmed: proven on 4S with 3200KV on a Slash 4x4, zero issues. Cost $30 on Temu/AliExpress. Already in hand.
- **Specs confirmed from listing:**
  - Voltage: 2-4S LiPo
  - Continuous / Burst: 120A / 760A
  - Resistance: 0.0003 ohm
  - BEC: 6V/5A or 7.4V/5A (solder mod — done on user's units)
  - Dimensions: 43 × 36 × 33mm
  - Weight: **105g**
  - Fan: included — listing says powered directly from battery (max 8V), but user confirmed fan does not overspeed on 4S, so voltage is regulated in practice
- **Fully waterproof — user confirmed full submersion, not just splash resistant.** Surprisingly capable for a $30 Chinese ESC.
- Sensor input: JST-ZH — works with Castle 1412/1415 and standard HobbyWing motors. Needs adapter (HWA30810007) for EZRun 3665SD G3 proprietary plug.
- Zero cost — already in hand.

### HobbyWing EZRun MAX10 G2 140A

- IP67 — the only HobbyWing ESC in this range with a full IP rating
- Designed specifically as a combo unit with the EZRun 3665SD G3 motor (proprietary waterproof sensor port lines up directly)
- If running a Castle or standard JST-ZH motor, needs the HobbyWing Sensor Adapter Cable (HWA30810007)
- 4S ceiling — no voltage headroom above the build requirement
- 120g with wires, 53 × 39.5 × 37.2mm

### HobbyWing XeRun XR8 SCT — Ruled Out

- **Not waterproof — ruled out.** HobbyWing's own spec sheet confirms waterproof: No. This build requires waterproof. End of story.
- Would have been the lightest ESC on the list at 90.5g — irrelevant.

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

| | Fire Phoenix 120A | Copperhead 10 | MAX10 G2 | Mamba X | Mamba Monster X |
|---|---|---|---|---|---|
| Max cells | 4S | 4S | 4S | 6S | 6S |
| 4S headroom | Tight | Tight | Tight | Comfortable | Comfortable |
| Waterproof | **Full soak** | Yes (epoxy) | IP67 | Yes (epoxy) | Yes (epoxy) |
| Sensored | Yes (JST-ZH) | Yes (SmartSense) | Yes (G3 port) | Yes (SmartSense) | Yes (SmartSense) |
| Weight | 105g | **71g** | 120g | 101g | 111g† |
| Castle motor (native) | Works | SmartSense | Adapter | SmartSense | SmartSense |
| EZRun 3665SD G3 (native) | Adapter | Adapter | **Yes** | Adapter | Adapter |
| Price (approx) | **$30 (in hand)** | ~$70 | ~$85 | ~$125 | ~$135 |

†Mamba Monster X listed without battery connector — add ~10–15g for installed weight

> XeRun XR8 SCT removed — not waterproof, hard no for this build.

**Pairing logic:**
- **Keep it simple, zero extra spend** → Fire Phoenix in hand + Castle 1412 in hand. Proven combo, $0 additional cost.
- **Lightest possible waterproof ESC** → Copperhead 10 at 71g, ~$70. Pairs well with Castle 1412/1415.
- **Going EZRun 3665SD G3 2400KV** → MAX10 G2 is the native matched combo; Fire Phoenix/Copperhead need sensor adapter.
- **Want 6S headroom later** → Mamba X or Mamba Monster X only — all 4S ESCs are dead ends if voltage ever goes up.

**Weight priority:** Fire Phoenix (105g, $30, in hand) and Copperhead 10 (71g, ~$70) are the two lightest waterproof options. Copperhead is the lightest on the entire list.
