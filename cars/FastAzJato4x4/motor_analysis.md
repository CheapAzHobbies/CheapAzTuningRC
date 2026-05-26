# Motor Selection — FastAzJato4x4

> **Chosen Motor: HobbyWing EZRun 3665SD G3 3200KV** (HWA30402607)

---

## Why 3200KV

The Jato 4x4 platform is lighter than a typical 1/8 buggy. Higher KV runs fine here because there's less chassis mass to fight. On 4S (14.8V nominal), 3200KV gives plenty of top-end without needing to push a larger, heavier stator.

KV is a no-load speed rating — two motors with the same KV on the same voltage run the same top speed. The differences that matter are torque, heat, and efficiency, which come down to stator size, lamination quality, and sealing.

---

## Motor Comparison

| Motor | KV | Stator | Cell Rating | Sensored | Splash | Notes |
|---|---|---|---|---|---|---|
| Castle Creations 1412-3200 | 3200KV | 36x50mm | 4S | Yes (proprietary) | No | Old lamination tech, no seal, Castle sensor = sensorless on HobbyWing ESC |
| HobbyWing XeRun 3660SD G3 | 3200KV | 36x60mm | **3S max** | Yes (JST-ZH) | IP5X (dust only) | Ruled out — 3S max is a dealbreaker on this 4S build |
| **HobbyWing EZRun 3665SD G3** | **3200KV** | **36x65mm** | **4S** | **Yes (JST-ZH)** | **IP64** | **Winner** |

---

## Why Castle 1412 Was Ruled Out

1. **No splash protection.** No IP rating. Jato is being run outdoor on a CF buggy chassis — water ingress is real.
2. **Proprietary sensor connector.** Castle uses its own sensor plug. The Fire Phoenix XeRun 120A ESC uses the HobbyWing sensor standard (JST-ZH). Mismatched connectors = running sensorless, which defeats the purpose of sensored operation — cogging at low speed, rougher starts.
3. **Older lamination technology.** G3-series motors use thinner stator laminations, which reduce eddy current losses at high RPM. Less wasted energy as heat. The 1412 predates this and runs hotter for the same output.

---

## Why XeRun 3660SD G3 Was Ruled Out

One reason: **3S maximum cell rating.** This build runs 4S. End of story.

(The XeRun line is HobbyWing's competition/racing tier — spec'd tighter, higher tolerances, but that 3S ceiling is a hard limit for a 4S battery pack.)

---

## Why EZRun 3665SD G3 Is the Pick

- **IP64 rated** — dust-tight + protected against water splashes from any direction. Right for a buggy.
- **4S rated** — matches the battery setup.
- **Sensored, JST-ZH connector** — plugs natively into the Fire Phoenix XeRun 120A ESC. Full sensored operation: smooth starts, no cogging.
- **G3 laminations** — same thin-lamination low-loss stator tech as the XeRun line. Less heat than the Castle 1412 at equivalent output.
- **36x65mm stator** — 5mm longer can than the Castle 1412 (36x50mm) and 5mm longer than the XeRun 3660 (36x60mm). More copper = marginally more torque at the same KV.
- **EZRun tier** — HobbyWing's bashing/recreational line. Built for abuse, not spec racing. More forgiving for a one-off build than the competition XeRun spec.

---

## ESC Compatibility

**ESC in use:** Fire Phoenix XeRun 120A Enhanced (Speed Dragon) — waterproof, 4S, sensored.

This is a Chinese market rebrand of the HobbyWing XeRun 120A Enhanced (强化速龙), not the standard V2.1. The enhanced version is waterproof and 4S-capable. Sensor input is JST-ZH, native to the EZRun 3665SD G3. No adapter needed.

---

## Summary

Same KV = same top speed. The EZRun 3665SD G3 wins on heat management (G3 laminations), protection (IP64), sensored compatibility (JST-ZH native), and cell rating (4S). The Castle 1412 loses on sealing and sensor protocol. The XeRun 3660SD G3 loses on cell rating.
