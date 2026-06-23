# ESC Selection — FastAzJato4x4

> **Chosen: Fire Phoenix XeRun 120A Enhanced (Speed Dragon)** — already in hand, fully waterproof (I verified full submersion myself), sensored JST-ZH, proven on 4S with 3200KV on Slash 4x4. Zero additional spend. Works natively with Castle 1412 / 1415 and standard Hobbywing motors.

<p align="center"><a href="https://www.aliexpress.com/item/4001205164437.html"><img src="src/electronics_firephoenix_xerun_120a_esc.jpg" width="500"></a></p>

---

## Table of Contents

- [Key Requirements](#key-requirements) — Must / May criteria
- [ESC Comparison](#esc-comparison) — every ESC option with specs and status
- [Sensor Connector Compatibility](#sensor-connector-compatibility) — motor ↔ ESC plug matrix
- [Detailed Notes](#detailed-notes) — bullet specs per ESC
- [Summary](#summary) — head-to-head recap table

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **4S LiPo support** | Must | ESC must handle 16.8V input |
| **Waterproof** | Must | Non-waterproof ESCs are ruled out regardless of other specs |
| **Sensored** | Must | Smooth starts, no cogging, low-speed control. Motor sensor connector compatibility matters |
| **1/10–1/8 scale current capacity** | Must | 36mm stator motors pull significant amps |
| **Lightweight** | May | Lower weight helps acceleration and handling — preferred but not required |
| **Good BEC** | May | >6V output and ≥5A current — needed to drive HV servos without voltage sag |

---

## ESC Comparison

> *Spec format: Cells · Current (A) · BEC · Sensored · Waterproof · Weight · Price*

| ESC | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **Fire Phoenix XeRun 120A Enhanced (Speed Dragon)** | **Cells:** 2-4S<br>**Current (A):** **120A**<br>**BEC:** 6V/5A or 7.4V/5A (solder mod)<br>**Sensored:** **Yes (JST-ZH)**<br>**Waterproof:** **Full submersion**<br>**Weight:** **105g**<br>**Price:** **$30 (in hand)** | Pro: Already owned, proven on 4S with 3200KV on Slash 4x4, fully waterproof (full soak), sensored, comes with fan, zero cost<br><br>Con: Lower amp rating than Castle Mamba options; Chinese market rebrand; 4S ceiling no headroom | <a href="https://www.aliexpress.com/item/4001205164437.html"><img src="src/electronics_firephoenix_xerun_120a_esc.jpg" width="500"></a> |
| 🔵 **Castle Mamba X** | **Cells:** 2-6S<br>**Current (A):** not published*<br>**BEC:** 8A peak, adj. 5.5/6.0/7.5/8.0V<br>**Sensored:** Yes (SmartSense)<br>**Waterproof:** Yes (epoxy)<br>**Weight:** 101g<br>**Price:** ~$190 | Pro: 6S rated, **officially supports the Castle 1412 in-hand motor**, adjustable BEC, datalogging<br><br>Con: Amps not published; no IP rating; fan must come off in wet conditions | <a href="https://www.castlecreations.com/en/mamba-x-esc-010-0155-00"><img src="src/electronics_castle_mamba_x.jpg" width="500"></a> |
| 🔵 **Castle Mamba Monster X** | **Cells:** 2-6S<br>**Current (A):** not published*<br>**BEC:** 8A peak, adj. 5.5/6.0/7.5/8.0V<br>**Sensored:** Yes (SmartSense)<br>**Waterproof:** Yes (epoxy)<br>**Weight:** 111g<br>**Price:** ~$200 | Pro: True 1/8 scale power handling, 6S overhead<br><br>Con: **Wrong motor class for the in-hand 1412** — spec'd for 1512 / 1515 only; overkill for 36mm motors | <a href="https://www.castlecreations.com/en/mamba-monster-x-esc-010-0145-00"><img src="src/electronics_castle_mamba_monster_x.jpg" width="500"></a> |
| 🔵 **Castle Copperhead 10** — *(budget)* | **Cells:** 2-4S<br>**Current (A):** not published*<br>**BEC:** 6A peak, sel. 5.5/7.5V<br>**Sensored:** Yes (SmartSense)<br>**Waterproof:** Yes (epoxy)<br>**Weight:** 71g<br>**Price:** ~$145 (sale ~$95) | Pro: Lightest on the list, **I run 2 on the K939 — never struggle or thermal**, CRYO-DRIVE keeps it cool<br><br>Con: 4S ceiling; vehicle weight cap ~7.5 lb (FastAzJato4x4 at the edge); spec'd for 1406 not the 1412 | <a href="https://www.castlecreations.com/en/copperhead-10-16-8v-wp-sensored-esc-010-0166-00"><img src="src/electronics_castle_copperhead_10.jpg" width="500"></a> |
| ❌ ~~HobbyWing EZRun MAX10 G2 140A~~ | **Cells:** 2-4S<br>**Current (A):** 140A<br>**BEC:** 6V or 7.4V @ 5A<br>**Sensored:** Yes (proprietary G3 port)<br>**Waterproof:** IP67<br>**Weight:** 120g<br>**Price:** ~$60 (combo ~$150) | Pro: IP67, lightest waterproof HW option, smart fan only spins when hot<br><br>Con: **Proprietary G3 sensor port — vetoed.** Needs HobbyWing adapter for any non-EZRun G3 motor | <a href="https://www.hobbywingdirect.com/products/ezrun-max10-g2-esc"><img src="src/electronics_hobbywing_ezrun_max10_g2_hw30102603.jpg" width="500"></a> |
| 🚫 ~~HobbyWing XeRun XR8 SCT~~ | **Cells:** 2-4S<br>**Current (A):** 140A<br>**BEC:** 6V / 3A<br>**Sensored:** Yes (JST-ZH)<br>**Waterproof:** **NO**<br>**Weight:** 91g<br>**Price:** ~$200 | Pro: Light at 91g, competition-grade<br><br>Con: **Not waterproof — hard no for this build**; BEC only 6V / 3A (fails HV-servo May requirement); superseded by XR8 PRO G3 | <a href="https://www.hobbywingdirect.com/collections/xerun-xr8-esc/sct"><img src="src/electronics_hobbywing_xerun_xr8_sct_hwa30113301.jpg" width="500"></a> |
| 🚫 ~~HobbyWing XeRun XR8 PRO G3~~ | **Cells:** 2-4S<br>**Current (A):** 200A<br>**BEC:** 6V or 7.4V adj., 6A continuous<br>**Sensored:** Yes / Sensorless<br>**Waterproof:** **NO**<br>**Weight:** 103g<br>**Price:** ~$150 | Pro: Newest XeRun racing ESC, 200A continuous, 4S match, OTA programmable<br><br>Con: **Not waterproof — XeRun racing line, hard no for this build** | <a href="https://www.hobbywingdirect.com/products/xr8-pro-g3-esc"><img src="src/electronics_hobbywing_xerun_xr8_pro_g3.jpg" width="500"></a> |
| 🚫 ~~HobbyWing EZRun MAX8 G2S~~ | **Cells:** 4S-6S<br>**Current (A):** 160A<br>**BEC:** 6A/15A, 6V/7.4V/8.4V<br>**Sensored:** Yes (JST-ZH)<br>**Waterproof:** Yes (enhanced)<br>**Weight:** 194g<br>**Price:** ~$140 | Pro: Highest amp rating among Hobbywing options, 6S overhead, Bluetooth, 32° turbo<br><br>Con: Way too heavy at 194g for a 1/10 build on 36mm motors | <a href="https://www.hobbywingdirect.com/products/ezrun-max8-esc-g2"><img src="src/electronics_hobbywing_ezrun_max8_g2s.jpg" width="500"></a> |

*Castle does not publish continuous amp ratings for surface ESCs. Community reports peaks of 100+ A on the Mamba X and Monster X.*

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

### Fire Phoenix XeRun 120A Enhanced (Speed Dragon) — Chosen

- Chinese market rebrand of the HobbyWing XeRun 120A Enhanced (强化速龙). Not the standard V3.1 — that's 2-3S only. The Enhanced version is 2-4S and waterproof.
- Dimensions: 43 × 36 × 33mm
- BEC: 6V/5A or 7.4V/5A (solder mod — done on my units)
- Burst current: 760A; resistance 0.0003 ohm
- Sensor input: JST-ZH — works with Castle 1412/1415 and standard Hobbywing motors. Needs adapter (HWA30810007) for EZRun 3665SD G3 proprietary plug.
- Fan included; powered directly from battery (max 8V). I confirmed the fan doesn't overspeed on 4S, so voltage is regulated in practice.
- I confirmed full submersion, not just splash resistant. Surprisingly capable for a $30 ESC.
- Proven on my car: 4S with 3200KV on Slash 4x4, zero issues. Cost $30 on Temu/AliExpress.

### Castle Mamba X — Candidate

- Dimensions: 54.4 × 35.2 × 30.0mm
- BEC: 8A peak, adjustable 5.5 / 6.0 / 7.5 / 8.0V (default 5.5V)
- Motor connectors: 4.0mm female bullets
- Recommended motors: Castle 1406 / 1410 / **1412** / 1415 sensored (1412 is in hand)
- Application: <7 lb at 6S, or 1/8 buggy <9 lb at 4S max
- 30mm fan included but must be removed for wet driving (not waterproof)
- Datalogging, telemetry, ROAR + Recon G6 certified, B-Link compatible
- MSRP $232, street ~$190

### Castle Mamba Monster X — Candidate

- 1/8-scale version of the Mamba X
- Dimensions: 53 × 49 × 36.4mm
- BEC: 8A peak, adjustable 5.5 / 6.0 / 7.5 / 8.0V
- Motor connectors: 6.5mm female bullets
- Recommended motors: Castle 1512 (1800/2650KV, 4S max) or 1515 (2200KV, 6S) — **does NOT officially support the in-hand 1412**
- Application: <15 lb with 2200KV, <9 lb with 1800/2650KV. Not for high-speed 1/8 (Infraction / Limitless / XO-1)
- 30mm fan included but must be removed for wet driving
- Datalogging, telemetry, B-Link compatible
- MSRP $245, street ~$200

### Castle Copperhead 10 — Candidate (budget)

- Dimensions: 55.6 × 35.3 × 33.8mm
- BEC: 6A peak, selectable 5.5 / 7.5V
- Motor connectors: 4.0mm female bullets
- Recommended motors: Castle 1406 series (4-pole 12-slot) — **does NOT officially support the in-hand 1412**
- Application: 1/10 vehicles up to 7.5 lb (FastAzJato4x4 is right at this limit with battery)
- Runs SmartSense, sensored-only, or brushed
- CRYO-DRIVE minimizes part-throttle heat; 30mm removable fan with dual-use fan guard
- Data Logging Lite, telemetry, B-Link 2 compatible
- **I run 2 on the K939 — never struggle or thermal**
- MSRP $177, street ~$145, sale prices as low as ~$95

### HobbyWing EZRun MAX10 G2 140A — Vetoed (proprietary connector)

- Dimensions: 53 × 39.5 × 37.2mm
- BEC: 6V or 7.4V @ 5A (switch-mode)
- Burst current: 880A
- Motor KV limit: 3S → ≤4000KV 3665; 4S → ≤2600KV 4268
- Only HobbyWing ESC in this range with full IP67
- Sold as combo with EZRun 3665SD G3 (proprietary waterproof sensor port lines up directly)
- For Castle / standard JST-ZH motors, needs HobbyWing Sensor Adapter (HWA30810007) — the reason for the veto
- Smart start-stop fan (only spins when hot), 32° turbo timing, OTA Bluetooth optional
- $60 ESC alone; $150 combo with 3665SD G3 3200KV motor

### HobbyWing XeRun XR8 SCT — Ruled Out (not waterproof)

- Older model in the XR8 family, superseded by XR8 PRO G3
- 38.5 × 36 × 30mm; BEC 6V / 3A; burst 760A
- Would have been the lightest at 91g — irrelevant since not waterproof

### HobbyWing XeRun XR8 PRO G3 — Ruled Out (not waterproof)

- Newest XeRun racing ESC
- Dimensions: 54.8 × 36.8 × 38.8mm
- BEC: 6V or 7.4V adjustable, 6A continuous switch-mode
- Burst 1080A; sensored or sensorless
- Motor KV limit: 2S → ≤4300KV 3660; 3S → ≤3600KV 3660; 4S → ≤3000KV 4268
- Programming via Tunalyzer and OTA programmer
- XeRun racing line — fan powered by BEC, no IP rating, ruled out for waterproof requirement
- MSRP $210, street ~$150

### HobbyWing EZRun MAX8 G2S — Ruled Out (too heavy)

- Built for 1/8 trucks and buggies with big motors — overkill for 36mm stator
- Dimensions: 60 × 48 × 40.5mm
- BEC: 6A / 15A switch-mode, 6V / 7.4V / 8.4V
- Burst 1080A
- Motor KV limit: 4S → ≤3000KV; 6S → ≤2400KV
- 32° turbo timing (+25% RPM with compatible motors), Bluetooth via HW LINK app
- Enhanced waterproof + dust-proof
- 194g is the heaviest ESC on this list by far

---

## Summary

| | Fire Phoenix 120A | Copperhead 10 | MAX10 G2 | Mamba X | Mamba Monster X |
|---|---|---|---|---|---|
| Max cells | 4S | 4S | 4S | 6S | 6S |
| 4S headroom | Tight | Tight | Tight | Comfortable | Comfortable |
| Waterproof | **Full soak** | Yes (epoxy) | IP67 | Yes (epoxy) | Yes (epoxy) |
| Sensored | Yes (JST-ZH) | Yes (SmartSense) | Yes (G3 port) | Yes (SmartSense) | Yes (SmartSense) |
| Weight | 105g | **71g** | 120g | 101g | 111g |
| Castle 1412 native | Works | SmartSense* | Adapter | **SmartSense (rated)** | SmartSense (not rated for 1412) |
| EZRun 3665SD G3 native | Adapter | Adapter | **Yes** | Adapter | Adapter |
| Price (approx) | **$30 (in hand)** | ~$145 ($95 sale) | ~$60 | ~$190 | ~$200 |

*Copperhead 10 is spec'd for 1406 motors; will physically work with 1412 sensor but outside official application range.*

> XeRun XR8 SCT, XR8 PRO G3, and EZRun MAX8 G2S removed — XeRuns are not waterproof, MAX8 G2S is too heavy. MAX10 G2 vetoed for proprietary connector.

**Pairing logic:**
- **Keep it simple, zero extra spend** → Fire Phoenix in hand + Castle 1412 in hand. Proven combo, $0 additional cost. **← Chosen path.**
- **Lightest possible waterproof ESC** → Copperhead 10 at 71g, ~$95 on sale. Pairs with Castle 1406; will run a 1412 but outside spec.
- **Want 6S headroom later** → Mamba X (for 1412/1415 motors) or Mamba Monster X (for 1512/1515 motors). All 4S ESCs are dead ends if voltage ever goes up.

**Weight priority:** Fire Phoenix (105g, $30, in hand) and Copperhead 10 (71g, ~$95 on sale) are the two lightest waterproof options. Copperhead is the lightest on the entire list.
