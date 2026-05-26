# Motor Selection — FastAzJato4x4

> **Status: Undecided — see trade-offs below.**
>
> No HobbyWing motor hits 3200KV + 4S + sensored simultaneously. The Castle 1412 is the only verified 4S 3200KV option but runs sensorless on the HobbyWing ESC and has no splash protection.

---

## Why 3200KV

The Jato 4x4 platform is lighter than a typical 1/8 buggy. Higher KV runs fine here because there's less chassis mass to fight. On 4S (14.8V nominal), 3200KV gives plenty of top-end without needing to push a larger, heavier stator.

KV is a no-load speed rating — two motors with the same KV on the same voltage run the same top speed. The differences that matter are torque, heat, and efficiency, which come down to stator size, lamination quality, and sealing.

---

## Motor Comparison

| Motor | KV | Stator | Weight | Cell Rating | Sensored | Splash | Status | Why Choose | Why Not |
|---|---|---|---|---|---|---|---|---|---|
| **HobbyWing EZRun 3665SD G3** | **2400KV** | **36x65mm** | **305g** | **2-4S** | **Yes (JST-ZH)** | **IP64** | **Candidate** | Only HobbyWing option with 4S + sensored + IP64 — the clean build | 800KV lower requires regearing, heaviest motor, additional cost |
| Castle Creations 1415 | 2400KV | 36x69.5mm | 318g | 3-4S | Yes (proprietary) | None | Candidate | 4S rated, slightly longer/more torque than 1412, same KV as EZRun candidate | Runs sensorless on HobbyWing ESC, no splash protection, heavier than 1412 |
| Castle Creations 1412 | 3200KV | 36x50mm | 265g | 4S (with care) | Yes (proprietary) | None | In Hand | Already in hand, proven on 4S, no regearing needed, lightest option | No splash protection, runs sensorless on HobbyWing ESC, older lamination tech runs hotter |
| HobbyWing EZRun 3652SD G3 | 3300KV | 36x52mm | 227g | **3S max** | Yes (JST-ZH) | IP5X | Ruled Out | Lightest motor in the lineup, sensored native, G3 laminations | 3S max — dealbreaker for 4S build; shorter can means less torque |
| HobbyWing EZRun 3665SD G3 | 3200KV | 36x65mm | 305g | **3S max** | Yes (JST-ZH) | IP64 | Ruled Out | IP64, G3 laminations, sensored native, largest stator in this group | 3S max — same dealbreaker as XeRun despite being EZRun tier |
| HobbyWing XeRun 3660SD G3 | 3200KV | 36x60mm | 230g | **3S max** | Yes (JST-ZH) | IP5X | Ruled Out | Lighter than EZRun 3665, competition-grade G3 laminations, sensored native | 3S max — hard no for a 4S build |
| Castle Creations 1515 V2 | 2200KV | 40x75mm | 429g | 2-6S | Yes (proprietary) | None | Ruled Out | True 1/8 scale motor, runs 6S, massive torque headroom | Way too heavy at 429g, 40mm diameter won't fit Jato chassis, overkill for this build |

---

## Why XeRun 3660SD G3 3200KV Was Ruled Out

3S maximum cell rating. This build runs 4S. End of story.

---

## Why EZRun 3665SD G3 3200KV Was Ruled Out

Same problem — **3S max**, despite being the EZRun (bashing) tier and a longer 65mm can. HobbyWing winds the 3200KV stator for lower voltage across both product lines. Only the lower KV variants of the 3665 are 4S rated.

---

## The Real Trade-Off: Castle 1412 vs EZRun 3665SD G3 2400KV

### Castle Creations 1412 3200KV — In Hand

**Pros:**
- Proven 4S capable — user has run this motor on 4S with the Fire Phoenix ESC on a Slash 4x4 with no issues
- 3200KV — same top speed as intended, no regearing needed
- Lighter than the EZRun 3665SD G3 at 265g vs 305g

**Cons:**
- No splash or dust protection — no IP rating
- Proprietary Castle sensor connector doesn't match HobbyWing JST-ZH — runs sensorless on the Fire Phoenix ESC (cogging at low speed, rougher starts)
- Older lamination technology — runs hotter than G3-series at equivalent output
- Castle says 4S is OK for buggies under ~4lb with conservative gearing and temp monitoring — not worry-free

### HobbyWing EZRun 3665SD G3 2400KV — (HWA30402604)

**Pros:**
- 4S native — no asterisks
- IP64 — dust-tight, water splash from any direction
- Sensored JST-ZH — plugs natively into the Fire Phoenix ESC, full sensored operation
- G3 laminations — less heat than Castle 1412 at equivalent output
- Same physical size as 3200KV variant

**Cons:**
- 2400KV — 800KV lower than target. Same top speed is achievable by running a smaller pinion (fewer teeth) or larger spur, but requires regearing from scratch
- Heaviest of all options at 305g
- Motor not in hand — additional cost

---

## ESC Compatibility

**ESC in use:** Fire Phoenix XeRun 120A Enhanced (Speed Dragon) — waterproof, 4S, sensored.

This is a Chinese market rebrand of the HobbyWing XeRun 120A Enhanced (强化速龙), not the standard V2.1. The enhanced version is waterproof and 4S-capable. Sensor input is JST-ZH, native to the EZRun line. Castle's proprietary sensor plug does not match — Castle 1412 runs sensorless on this ESC.

---

## Summary

| | Castle 1412 3200KV | EZRun 3665SD G3 2400KV |
|---|---|---|
| 4S rated | Yes (with care) | Yes (native) |
| Splash protection | No | IP64 |
| Sensored on HW ESC | No (runs sensorless) | Yes |
| G3 laminations | No | Yes |
| Weight | 265g | 305g |
| Regearing needed | No | Yes |
| Cost | $0 (in hand) | ~$65+ |

If this is primarily a basher and sensorless low-speed behavior is acceptable, the Castle 1412 in hand is the simpler path — it already works proven. If smooth sensored starts, splash protection, and G3 heat efficiency matter more, the EZRun 3665SD G3 2400KV is the correct motor, at the cost of regearing and an additional purchase.
