# Motor Selection — FastAzJato4x4

> **Leaning toward: Castle Creations 1415 2400KV** — 4S native, runs cool (the original reason to drop the 3200KV), no proprietary connector. Pairs natively with the chosen Fire Phoenix ESC over standard JST-ZH.
>
> The HobbyWing EZRun 3665SD G3 2400KV was the prior top pick but is **vetoed** — proprietary waterproof sensor plug requires an adapter for any non-MAX10-G2 ESC. The Fire Phoenix ESC is chosen, so the proprietary plug is dead weight.
>
> Castle 1412 3200KV (in hand) still works but runs hot on 4S and requires a fan. Castle 1415 is the clean upgrade path with no connector issues.

---

## KV Target and Heat Reality

The original target was 3200KV — same as what's already running in the Slash 4x4. In practice the Castle 1412 3200KV gets hot enough on 4S to require a cooling fan. This is expected: 3200KV × 14.8V = ~47,000 RPM no-load, which pushes the motor hard especially in grass and offroad terrain where the drivetrain loads up under the high RPM.

KV is a no-load speed rating — same top speed at same KV on same voltage. The differences are torque, heat, and efficiency: stator size, lamination quality, and how the motor is wound for the voltage.

### What the Community Actually Runs

**Slash 4x4 on 4S:**
- 2400KV is the well-established sweet spot. Runs cool, strong torque, no fan needed with conservative gearing
- 3200KV on 4S works but runs hot in grass/offroad, generally needs a fan
- Community verdict: if heat is a concern, go 2400KV and gear up slightly

**E-Jato / Jato 4x4 electric on 4S:**
- 2200KV recommended for all-day running with no heat issues
- Builders going higher KV (3000+) report needing cooldown breaks and conservative gearing
- One builder with 2200KV on 4S and 26/38 gearing ran all day with no problems

**True 1/8 buggy on 4S (heavier chassis than Jato):**
- 1900–2200KV is the consensus. Motors at 1900KV are the most common race setup
- Higher KV on a heavier 1/8 platform just adds heat with no benefit
- The Jato 4x4 is lighter than a true 1/8 buggy, so 2400KV is arguably right at or just above the community-preferred range for this weight class

### Implication for This Build

Running 3200KV on 4S and needing a fan is not a setup problem — it's a physics problem. The motor is wound for a lower voltage ceiling and is being pushed. Dropping to 2400KV with G3 laminations eliminates the eddy current losses that generate most of the heat, and puts the build right in line with what experienced builders run on identical or heavier platforms. A fan becomes unnecessary weight and a mud/debris magnet.

---

## Motor Comparison

| Motor | Spec | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| Castle Creations 1412 | KV: 3200KV<br>Stator: 36x50mm<br>Weight: 265g<br>Cells: 4S (with care)<br>Sensored: Yes (works with HW ESC)<br>Splash: None | **In Hand** | Pro: In hand, proven on 4S, no regearing needed, lightest 4S option<br>Con: No splash protection, older lamination tech runs hotter, 4S needs conservative gearing | — |
| **Castle Creations 1415** | KV: **2400KV**<br>Stator: **36x69.5mm**<br>Weight: **318g**<br>Cells: **3-4S**<br>Sensored: **Yes (works with HW ESC)**<br>Splash: **None** | **Candidate** | Pro: 4S rated, 2400KV runs cool (no fan needed), longer can than 1412 for more torque, native JST-ZH sensor plug with Fire Phoenix<br>Con: No splash protection, heavier than 1412, requires regearing | — |
| ~~HobbyWing EZRun 3665SD G3 2400KV~~ | KV: 2400KV<br>Stator: 36x65mm<br>Weight: 305g<br>Cells: 2-4S<br>Sensored: Yes (proprietary waterproof plug — needs adapter)<br>Splash: IP64 | **Vetoed** | Pro: Only HobbyWing option with 4S + IP64; G3 laminations, sensored capable<br>Con: **Proprietary waterproof sensor plug — vetoed.** Needs HWA30810007 adapter for any non-MAX10-G2 ESC. 800KV lower requires regearing; additional cost | — |
| ~~HobbyWing EZRun 3652SD G3~~ | KV: 3300KV<br>Stator: 36x52mm<br>Weight: 227g<br>Cells: **3S max**<br>Sensored: Yes (JST-ZH)<br>Splash: IP5X | Ruled Out | Pro: Lightest motor in the group, G3 laminations, sensored<br>Con: 3S max — dealbreaker for 4S build | — |
| ~~HobbyWing EZRun 3665SD G3 3200KV~~ | KV: 3200KV<br>Stator: 36x65mm<br>Weight: 305g<br>Cells: **3S max**<br>Sensored: Yes (proprietary waterproof plug)<br>Splash: IP64 | Ruled Out | Pro: IP64, largest stator, G3 laminations<br>Con: 3S max — dealbreaker for 4S build; proprietary plug | — |
| ~~HobbyWing XeRun 3660SD G3~~ | KV: 3200KV<br>Stator: 36x60mm<br>Weight: 230g<br>Cells: **3S max**<br>Sensored: Yes (JST-ZH)<br>Splash: IP5X | Ruled Out | Pro: Lighter than EZRun 3665, competition-grade G3 laminations<br>Con: 3S max — dealbreaker for 4S build | — |
| ~~Castle Creations 1515 V2~~ | KV: 2200KV<br>Stator: 40x75mm<br>Weight: 429g<br>Cells: 2-6S<br>Sensored: Yes (works with HW ESC)<br>Splash: None | Ruled Out | Pro: True 1/8 scale, runs 6S, massive torque headroom<br>Con: 40mm can won't fit Jato chassis, 429g is overkill | — |

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
- In hand, proven on 4S
- 3200KV — no regearing needed
- Lightest 4S option at 265g
- Sensor connector works with HobbyWing sensored ESCs

**Cons:**
- **Confirmed heat issue** — runs hot enough on 4S to require a cooling fan. Fan adds weight and is a mud/debris trap on a buggy
- No splash or dust protection — no IP rating
- Older lamination technology — the heat isn't gearing, it's eddy current losses in the stator
- 3200KV on 4S is above what the community recommends for this weight class without active cooling

### HobbyWing EZRun 3665SD G3 2400KV — (HWA30402604)

**Pros:**
- **2400KV on 4S is the community consensus** for Slash 4x4 and e-Jato builds — runs cool without a fan, strong torque
- 4S native — no asterisks
- IP64 — dust-tight, water splash from any direction
- G3 thin laminations — significantly less heat at high RPM, the direct fix for the fan problem
- No fan needed — one less thing to break, clog, or add weight
- Sensored capable with adapter

**Cons:**
- Proprietary waterproof sensor plug — works natively with EZRun MAX10 G2, needs adapter (HWA30810007) for other ESCs
- Requires regearing to match previous top speed
- 305g — heaviest 4S option
- Not in hand — additional cost (~$65)

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
| Runs cool on 4S (no fan) | **No — confirmed hot** | **Yes — community verified** | No |
| Weight | 265g | 305g | 318g |
| Regearing needed | No | Yes | Yes |
| Cost | $0 (in hand) | ~$65+ | ~$80+ |

The Castle 1412 3200KV needing a fan on 4S is the clearest signal in this decision. Community experience on the Slash 4x4 and e-Jato shows 2400KV on 4S runs cool without a fan. That is not a minor convenience difference — a fan on a buggy picks up dirt, adds failure points, and signals the motor is thermally marginal. The EZRun 3665SD G3 2400KV with G3 laminations directly addresses the root cause.
