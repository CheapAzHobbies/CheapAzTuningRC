# Motor Selection — FastAzJato4x4

> **Leaning toward: Castle Creations 1415 2400KV** — 4S native, runs cool (the original reason to drop the 3200KV), no proprietary connector. Pairs natively with the chosen Fire Phoenix ESC over standard JST-ZH. Castle 1412 3200KV is in hand and works, but runs hot on 4S and requires a fan; the 1415 2400KV is the clean upgrade path.

<p align="center"><img src="https://placehold.co/600x400/eee/333?text=IMAGE+NEEDED" width="600"><br>🚧 save Castle 1415 photo as <code>src/electronics_castle_1415_2400kv.jpg</code></p>

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **4S LiPo support** | Must | Build runs 4S — motor has to handle 16.8V without burning windings |
| **36mm can, ≤70mm overall length** | Must | Physical fit in the FastAzJato4x4 motor mount. 42mm cans technically fit but make the car **fat, heavy, and sluggish** — same goes for anything over ~70mm long |
| **2200–3200KV** | Must | Target range for 4S on a 1/10-class chassis. Below 2200 = sluggish; above 3200 = too hot on 4S even with a fan |
| **Sensored** | Must | Smooth starts, no cogging, low-speed control on the chosen Fire Phoenix ESC |
| **Standard sensor connector (JST-ZH or Castle native)** | Must | Fire Phoenix uses JST-ZH; proprietary Hobbywing G3 plugs require a $-and-cable adapter |
| **Runs cool on 4S without a fan** | May | Strong preference. A fan is added weight, mud trap, failure point. 2400KV-class with modern (G3 / 4-pole) laminations runs cool on 4S; 3200KV-class generally needs cooling |
| **Splash / dust resistance** | May | Nice for offroad / wet conditions but build is mostly track |
| **Lightweight** | May | Lower mass helps acceleration and handling, especially in a 1/10-class chassis |
| **Cheap / in hand** | May | $0 if already owned beats $80+ for a new motor |

> **Castle naming convention:** the four-digit Castle model number is stator dimensions in tenths of an inch. **First two digits = stator diameter, last two digits = magnet length.** So a `1412` is a 1.4" diameter × 1.2" magnet stator (35.6mm × 30.5mm internal); a `1415` is 1.4" × 1.5" (35.6mm × 38.1mm); a `1515` is 1.5" × 1.5". The overall **can** is larger than the stator — Castle 14-series motors all use a 36mm OD can; 15-series and 17-series are bigger.

---

## Motor Comparison

| Motor | Spec | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **Castle Creations 1412** | KV: 3200KV<br>Stator: 36x50mm<br>Weight: 265g<br>Cells: 4S (with care)<br>Sensored: Yes (Castle / JST-ZH compat)<br>Price: $0 (in hand) | **In Hand** | Pro: Free, proven on 4S, no regearing, lightest 4S option<br>Con: Runs hot on 4S — needs a fan; no IP rating; older lamination tech | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/electronics_castle_1412_3200kv.jpg` |
| **Castle Creations 1415 2400KV** | KV: **2400KV**<br>Stator: **36x69.5mm**<br>Weight: **318g**<br>Cells: **3-4S**<br>Sensored: **Yes (Castle / JST-ZH compat)**<br>Price: **~$80** | **Candidate** | Pro: 4S native, 2400KV runs cool without a fan, longer can = more torque, native pair with Fire Phoenix<br>Con: Heaviest 4S Castle option, no IP rating, requires regearing for top speed | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/electronics_castle_1415_2400kv.jpg` |
| ~~HobbyWing EZRun 3665SD G3 2400KV~~ | KV: 2400KV<br>Stator: 36x65mm<br>Weight: 305g<br>Cells: 2-4S<br>Sensored: Yes (**proprietary G3 plug**)<br>Price: ~$65 | **Vetoed** | Pro: Only Hobbywing option with 4S + IP64, G3 thin laminations<br>Con: **Proprietary G3 sensor plug — needs HWA30810007 adapter for the chosen Fire Phoenix ESC.** Adapter cost and one more failure point | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/electronics_hobbywing_ezrun_3665sd_g3_2400kv.jpg` |
| ~~HobbyWing EZRun 3652SD G3~~ | KV: 3300KV<br>Stator: 36x52mm<br>Weight: 227g<br>Cells: **3S max**<br>Sensored: Yes (JST-ZH)<br>Price: ~$60 | **Ruled Out** | Pro: Lightest motor in the group, G3 laminations<br>Con: **3S max — fails the 4S Must** | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/electronics_hobbywing_ezrun_3652sd_g3.jpg` |
| ~~HobbyWing EZRun 3665SD G3 3200KV~~ | KV: 3200KV<br>Stator: 36x65mm<br>Weight: 305g<br>Cells: **3S max**<br>Sensored: Yes (proprietary G3 plug)<br>Price: ~$65 | **Ruled Out** | Pro: IP64, largest stator, G3 laminations<br>Con: **3S max — fails the 4S Must.** Also has the proprietary plug problem | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/electronics_hobbywing_ezrun_3665sd_g3_3200kv.jpg` |
| ~~HobbyWing XeRun 3660SD G3~~ | KV: 3200KV<br>Stator: 36x60mm<br>Weight: 230g<br>Cells: **3S max**<br>Sensored: Yes (JST-ZH)<br>Price: ~$70 | **Ruled Out** | Pro: Lighter than EZRun 3665, competition-grade G3 laminations<br>Con: **3S max — fails the 4S Must** | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/electronics_hobbywing_xerun_3660sd_g3.jpg` |
| ~~Castle Creations 1515 V2~~ | KV: 2200KV<br>Stator: 40x75mm<br>Weight: 429g<br>Cells: 2-6S<br>Sensored: Yes (Castle / JST-ZH compat)<br>Price: ~$100 | **Ruled Out** | Pro: True 1/8 scale, runs 6S, massive torque headroom<br>Con: **40mm can won't fit the Jato chassis** (fails the 36mm-class Must); 429g is overkill | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/electronics_castle_1515_v2_2200kv.jpg` |

---

## KV Reference

KV is a no-load speed rating — same top speed at same KV on same voltage. The differences between options at the same KV are torque, heat, and efficiency (stator size, lamination quality, how the motor is wound for the voltage).

The original target was 3200KV — same as the Slash 4x4. In practice the Castle 1412 3200KV gets hot enough on 4S to require a cooling fan: 3200KV × 14.8V = ~47,000 RPM no-load, which pushes the motor hard especially in grass and offroad where the drivetrain loads up at high RPM.

### Community Consensus (4S)

| Platform | Recommended KV on 4S | Notes |
|----------|---------------------|-------|
| Slash 4x4 | 2400KV | Sweet spot, runs cool, no fan needed with conservative gearing. 3200KV works but runs hot |
| E-Jato / Jato 4x4 electric | 2200KV | All-day running, no heat issues. 3000KV+ needs cooldown breaks |
| True 1/8 buggy (heavier) | 1900-2200KV | 1900KV is most common race setup; higher KV on heavier chassis just adds heat |

The FastAzJato4x4 is lighter than a true 1/8 buggy, so **2400KV is at or just above the community-preferred range** for this weight class. A 1412 3200KV running hot on 4S isn't a setup problem — it's a physics problem. Dropping to 2400KV with G3 laminations eliminates the eddy-current losses driving the heat, and a fan becomes unnecessary weight and a mud magnet.

---

## Sensor Connector Compatibility

| Motor | Fire Phoenix XeRun 120A (chosen ESC) | Castle Mamba X | HW EZRun MAX10 G2 |
|---|---|---|---|
| Castle 1412 / 1415 | **Native (JST-ZH compat)** | **Native (SmartSense)** | Works |
| HW EZRun 3665SD G3 (2400 or 3200) | Needs adapter (HWA30810007) | Needs adapter | **Native** |
| HW EZRun 3652SD G3 / XeRun 3660SD G3 | Works (JST-ZH) | Works | Works (JST-ZH) |

---

## Detailed Notes

### Castle Creations 1412 3200KV — In Hand

- Already owned, proven on 4S with the Fire Phoenix ESC on the Slash 4x4
- 36×50mm stator — the smallest can in the comparison; lightest 4S option at 265g
- **Confirmed heat issue on 4S** — requires a cooling fan to stay in safe operating temps in grass / offroad. Fan adds weight, picks up mud / debris, adds a failure point
- Older lamination technology — the heat isn't gearing, it's eddy-current losses in the stator
- No splash / dust protection
- 3200KV on 4S is above what the community recommends for this weight class without active cooling
- Pairs natively with Fire Phoenix ESC via the JST-ZH sensor connector
- $0 — already in hand

### Castle Creations 1415 2400KV — Candidate (leading)

- 36×69.5mm stator — longer can than the 1412 for more torque
- 2400KV on 4S is the community sweet spot for cool-running operation without a fan
- 4S native, no asterisks
- No IP rating — same as the 1412, no splash protection
- 318g — heavier than the 1412 (265g) and 3665SD G3 2400KV (305g)
- Requires regearing to compensate for the lower KV vs the 1412 (3200 → 2400KV)
- Native JST-ZH sensor connector pairs directly with the chosen Fire Phoenix ESC
- ~$80 — additional cost over the in-hand 1412

### HobbyWing EZRun 3665SD G3 2400KV — Vetoed (proprietary connector)

- 36×65mm stator, 305g
- 4S native with IP64 splash + dust rating — the only Hobbywing option that hits both
- G3 thin laminations significantly reduce eddy-current losses at high RPM — would run cool on 4S
- **Vetoed**: proprietary waterproof sensor plug. Native fit only with the EZRun MAX10 G2 ESC, which itself was vetoed for the same proprietary-port reason. Needs adapter HWA30810007 to use with Fire Phoenix or any standard JST-ZH ESC
- Adapter cost (~$10) and one more cable in the loom
- ~$65

### HobbyWing EZRun 3652SD G3 — Ruled Out (3S max)

- 36×52mm stator, lightest in the group at 227g
- G3 laminations, JST-ZH sensor (would pair fine with Fire Phoenix)
- IP5X dust resistance
- **3S max cell rating — fails the 4S Must**. Hobbywing winds the 3300KV stator for lower voltage

### HobbyWing EZRun 3665SD G3 3200KV — Ruled Out (3S max + proprietary)

- 36×65mm stator, 305g, IP64
- **3S max cell rating — fails the 4S Must**. Same problem as the 3652 — Hobbywing only winds the 3200KV variant for 3S in the EZRun line
- Also has the proprietary G3 sensor plug (would have been vetoed even if 4S rated)

### HobbyWing XeRun 3660SD G3 3200KV — Ruled Out (3S max)

- 36×60mm stator, 230g — lighter than the EZRun 3665
- JST-ZH sensor connector
- Competition-grade XeRun line with G3 laminations
- **3S max cell rating — fails the 4S Must**

### Castle Creations 1515 V2 2200KV — Ruled Out (too big)

- 40×75mm stator — true 1/8 scale motor
- 2-6S rated, ~$100
- **40mm can won't fit the Jato chassis motor mount — fails the 36mm-class Must**
- 429g would be massive overkill on a 1/10-class chassis anyway

---

## Pinion Reference (32P, TBD)

Pinion not yet chosen — depends on which motor lands. Spur is the **50T 32-pitch TRA6842R** (same as the K939 setup). Reference table for common 32P pinion sizes:

| Pinion (32P) | FDR with 50T spur | Speed character | Typical motor pairing |
|---|---|---|---|
| 13T | 3.85 | Crawler / low end / cool | High-KV 3200KV+, slow speed-focused |
| 15T | 3.33 | Tame, low motor temp | Castle 1412 3200KV starting point — keeps it cooler |
| 17T | 2.94 | Balanced street / track | 2400KV stock-ish gearing |
| 19T | 2.63 | Faster, more top end | **Likely starting point for Castle 1415 2400KV** |
| 21T | 2.38 | High-speed bias | 2400KV with strong battery |
| 23T | 2.17 | Top-end aggressive | 2200KV on light vehicle |
| 25T | 2.00 | Speed-run territory | 2200KV-class only — monitor temps |

> FDR (Final Drive Ratio) shown is the spur-to-pinion only; multiply by the internal transmission ratio (~2.78:1 for Slash/Jato 4x4) for the true wheel ratio. Lower FDR = faster top speed but more heat / less torque. Higher FDR = more punch but lower top speed.

---

## Sources

- [Castle Creations 1415 product page](https://www.castlecreations.com/en/1410-sensored-motor)
- [Hobbywing EZRun 3665SD G3 product page](https://www.hobbywingdirect.com/products/ezrun-3665sd-g3-motor)
- [Hobbywing Sensor Adapter Cable HWA30810007](https://www.hobbywingdirect.com/products/sensor-adapter-cable-30810007)
- Community KV consensus: Slash 4x4 / e-Jato builder threads on RCTalk and ARRMA Forum
