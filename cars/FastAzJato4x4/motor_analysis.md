# Motor Selection — FastAzJato4x4

> **Status: Undecided — ESC not chosen yet. Motor choice depends on ESC sensor compatibility.**
>
> No HobbyWing motor hits 3200KV + 4S simultaneously. Castle 1412 3200KV (in hand) is the only verified 4S 3200KV option. Castle sensored motors are compatible with HobbyWing sensored ESCs. The EZRun 3665SD G3 uses a proprietary waterproof sensor plug designed for the MAX10 G2 ESC — needs an adapter for other ESCs.

---

## Why 3200KV

The Jato 4x4 platform is lighter than a typical 1/8 buggy. Higher KV runs fine here because there's less chassis mass to fight. On 4S (14.8V nominal), 3200KV gives plenty of top-end without needing to push a larger, heavier stator.

KV is a no-load speed rating — two motors with the same KV on the same voltage run the same top speed. The differences that matter are torque, heat, and efficiency, which come down to stator size, lamination quality, and sealing.

---

## Motor Comparison

| Motor | KV | Stator | Weight | Cell Rating | Sensored | Splash | Status | Why Choose | Why Not |
|---|---|---|---|---|---|---|---|---|---|
| **HobbyWing EZRun 3665SD G3** | **2400KV** | **36x65mm** | **305g** | **2-4S** | **Yes (proprietary waterproof plug — needs adapter)** | **IP64** | **Candidate** | Only HobbyWing option with 4S + IP64; G3 laminations, sensored capable | 800KV lower requires regearing; proprietary sensor plug needs adapter for most ESCs; additional cost |
| Castle Creations 1415 | 2400KV | 36x69.5mm | 318g | 3-4S | Yes (works with HW ESC) | None | Candidate | 4S rated, longer can than 1412 for more torque, sensored works with HobbyWing ESC | No splash protection, heavier than 1412, requires regearing |
| Castle Creations 1412 | 3200KV | 36x50mm | 265g | 4S (with care) | Yes (works with HW ESC) | None | In Hand | In hand, proven on 4S, no regearing needed, lightest 4S option | No splash protection, older lamination tech runs hotter, 4S needs conservative gearing |
| HobbyWing EZRun 3652SD G3 | 3300KV | 36x52mm | 227g | **3S max** | Yes (JST-ZH) | IP5X | Ruled Out | Lightest motor in the group, G3 laminations, sensored | 3S max — dealbreaker for 4S build |
| HobbyWing EZRun 3665SD G3 | 3200KV | 36x65mm | 305g | **3S max** | Yes (proprietary waterproof plug) | IP64 | Ruled Out | IP64, largest stator, G3 laminations | 3S max — dealbreaker for 4S build |
| HobbyWing XeRun 3660SD G3 | 3200KV | 36x60mm | 230g | **3S max** | Yes (JST-ZH) | IP5X | Ruled Out | Lighter than EZRun 3665, competition-grade G3 laminations | 3S max — dealbreaker for 4S build |
| Castle Creations 1515 V2 | 2200KV | 40x75mm | 429g | 2-6S | Yes (works with HW ESC) | None | Ruled Out | True 1/8 scale, runs 6S, massive torque headroom | 40mm can won't fit Jato chassis, 429g is overkill |

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
- Proven 4S capable — run on 4S on a Slash 4x4 with no issues
- 3200KV — same top speed as target, no regearing needed
- Lightest 4S option at 265g
- Sensored connector works with HobbyWing sensored ESCs

**Cons:**
- No splash or dust protection — no IP rating
- Older lamination technology — runs hotter than G3-series at equivalent output
- Castle says 4S OK for buggies under ~4lb with conservative gearing and temp monitoring — not worry-free

### HobbyWing EZRun 3665SD G3 2400KV — (HWA30402604)

**Pros:**
- 4S native — no asterisks
- IP64 — dust-tight, water splash from any direction
- G3 laminations — less heat than Castle 1412 at equivalent output
- Sensored capable

**Cons:**
- Proprietary waterproof sensor plug — designed to match the EZRun MAX10 G2 ESC. Requires an adapter cable (HWA30810007) to work with other sensored ESCs
- 2400KV — 800KV lower than target. Requires regearing to hit the same top speed
- Heaviest option at 305g
- Motor not in hand — additional cost

---

## ESC Not Yet Chosen

ESC selection is TBD. Notes that affect the choice:

- **Castle sensored motors** (1412, 1415): sensor connector works with HobbyWing sensored ESCs directly
- **HobbyWing EZRun 3665SD G3**: uses a proprietary waterproof sensor plug. Works natively with the EZRun MAX10 G2 ESC. Requires HobbyWing Sensor Adapter Cable (HWA30810007) for other ESCs
- **HobbyWing XeRun and EZRun 3652 motors**: standard JST-ZH sensor plug, works with any sensored HobbyWing ESC

---

## Summary

| | Castle 1412 3200KV | EZRun 3665SD G3 2400KV | Castle 1415 2400KV |
|---|---|---|---|
| 4S rated | Yes (with care) | Yes (native) | Yes (native) |
| Splash protection | No | IP64 | No |
| Sensored on HW ESC | Yes | Yes (needs adapter) | Yes |
| G3 laminations | No | Yes | No |
| Weight | 265g | 305g | 318g |
| Regearing needed | No | Yes | Yes |
| Cost | $0 (in hand) | ~$65+ | ~$80+ |
