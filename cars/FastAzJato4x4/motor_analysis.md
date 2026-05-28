# Motor Selection — FastAzJato4x4

> **Leaning toward: Castle Creations 1415 2400KV** — 4S native, runs cool (the original reason to drop the 3200KV), no proprietary connector. Pairs natively with the chosen Fire Phoenix ESC over standard JST-ZH. Castle 1412 3200KV is in hand and works, but runs hot on 4S and requires a fan; the 1415 2400KV is the clean upgrade path.

<p align="center"><img src="src/electronics_castle_1415_2400kv.jpg" width="600"></p>

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **4S LiPo support** | Must | Build runs 4S — motor has to handle 16.8V without burning windings |
| **36mm can, ≤70mm overall length** | Must | Physical fit in the FastAzJato4x4 motor mount. 42mm cans technically fit but make the car **fat, heavy, and sluggish** — same goes for anything over ~70mm long. **Exception**: a 40-42mm motor would be considered if it's actually *lighter* than the 36mm options (currently no 40mm+ candidate is — they're all heavier) |
| **2200–3200KV** | Must | Target range for 4S on a 1/10-class chassis. Below 2200 = sluggish; above 3200 = too hot on 4S even with a fan |
| **Sensored** | Must | Smooth starts, no cogging, low-speed control on the chosen Fire Phoenix ESC |
| **Standard sensor connector (JST-ZH or Castle native)** | Must | Fire Phoenix uses JST-ZH; proprietary Hobbywing G3 plugs require a $-and-cable adapter |
| **Rebuildable / serviceable** | Must | Bearings and brushes wear; motor has to come apart for maintenance, not get thrown away |
| **Documented bearing sizes** | Must | So replacement bearings can be sourced from any bearing supplier without guessing |
| **Solder tabs (not pre-wired)** | Must | Wires must terminate at solder tabs inside the can. Motors with wires running directly out of the body can't be re-wired without surgery if a wire pulls out |
| **Runs cool on 4S without a fan** | May | Strong preference. A fan and its mount add weight up high on the motor — purely a CG / weight argument, not reliability (user runs metal fans that basically never break unless smacked). 2400KV-class with modern (G3 / 4-pole) laminations runs cool on 4S; 3200KV-class generally needs cooling |
| **Splash / dust resistance** | May | Nice for offroad / wet conditions but build is mostly track |
| **Lightweight** | May | Lower mass helps acceleration and handling, especially in a 1/10-class chassis |
| **Cheap / in hand** | May | $0 if already owned beats $80+ for a new motor |

> **Castle naming convention:** the four-digit Castle model number is stator dimensions in tenths of an inch. **First two digits = stator diameter, last two digits = magnet length.** So a `1412` is a 1.4" diameter × 1.2" magnet stator (35.6mm × 30.5mm internal); a `1415` is 1.4" × 1.5" (35.6mm × 38.1mm); a `1515` is 1.5" × 1.5". The overall **can** is larger than the stator — Castle 14-series motors all use a 36mm OD can; 15-series and 17-series are bigger.

---

## Motor Comparison

| Motor | Spec | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **Castle Creations 1412 3200KV** (#060-0085-00) | KV: 3200<br>Can: 36mm × 62.5mm<br>Weight: 265g (with wires)<br>Cells: **2-4S** (Castle says up to 3S ideal, 4S with conservative gearing)<br>Sensored: Yes (Castle SmartSense / sensored / sensorless)<br>Price: **$0 in hand** (retail $119.95) | **In Hand** | Pro: Free, proven on 4S with Fire Phoenix, no regearing, lightest 4S option, 75,000 max RPM, M3 mount @ 25.4mm spacing<br>Con: Castle explicitly rates it 3S-ideal; 4S "needs conservative gearing and a close eye on temps" — runs hot on 4S in practice, fan basically required | <img src="src/electronics_castle_1412_3200kv.jpg" width="300"> |
| **Castle Creations 1415 2400KV** (#060-0060-00) | KV: **2400**<br>Can: **36mm × 69.5mm** (just under the 70mm Must)<br>Weight: **318g** (with wires)<br>Cells: **3-4S** (4S native, no caveats)<br>Sensored: **Yes — SmartSense / sensored / sensorless; ROAR-standard sensor port**<br>Price: **$129.95** (list $159) | **Candidate** | Pro: 4S native (no conservative gearing required), 2400KV runs cool without a fan, **improved 4-pole 12-slot design with less heat**, **rebuildable** (front bell/bearing or rotor/shaft replaceable), QuietSense sensor noise shielding, 75,000 RPM max, fan optional<br>Con: Heaviest 4S Castle option at 318g, no IP rating, requires regearing for top speed | <img src="src/electronics_castle_1415_2400kv.jpg" width="300"> |
| ~~HobbyWing EZRun 3665SD G3 2400KV~~ (#30402604) | KV: 2400<br>Can: 37mm × 65.8mm<br>Weight: 304.5g<br>Cells: **2-4S**<br>Sensored: Yes (**proprietary G3 plug**)<br>Price: ~$70 (MSRP $120) | **Vetoed** | Pro: 4S + IP67, modular detachable design, **bearings documented** (front 16×5×5 / rear 11×5×5), 4-pole, R = 0.00816Ω<br>Con: **Proprietary G3 sensor plug — needs HWA30810007 adapter for the chosen Fire Phoenix ESC.** Adapter cost and one more failure point | <img src="src/electronics_hobbywing_ezrun_3665sd_g3.jpg" width="300"> |
| ~~HobbyWing EZRun 3652SD G3 3300KV~~ (#30402603) | KV: 3300<br>Can: 37mm × 53mm<br>Weight: 227g<br>Cells: **2-3S max**<br>Sensored: Yes (JST-ZH)<br>Price: ~$60 (MSRP $93) | **Ruled Out** | Pro: Lightest motor in the group, IP67, modular detachable, **bearings documented** (front 13×5×4 / rear 11×5×5), 4-pole<br>Con: **2-3S max — fails the 4S Must.** Hobbywing sells 4100KV and 5400KV variants in this can too, all 3S max or lower | <img src="src/electronics_hobbywing_ezrun_3652sd_g3.jpg" width="300"> |
| ~~HobbyWing EZRun 3665SD G3 3200KV~~ (#30402607) | KV: 3200<br>Can: 37mm × 65.8mm<br>Weight: 304.5g<br>Cells: **2-3S max**<br>Sensored: Yes (proprietary G3 plug)<br>Price: ~$70 (MSRP $120) | **Ruled Out** | Pro: IP67, modular detachable, bearings documented, 4-pole, R = 0.00555Ω<br>Con: **2-3S max — fails the 4S Must.** Also has the proprietary plug problem | <img src="src/electronics_hobbywing_ezrun_3665sd_g3.jpg" width="300"><br><em>shared photo with 2400KV — physically identical motor</em> |
| ~~HobbyWing XeRun 3660SD G3 3200KV~~ | KV: 3200<br>Can: ~36mm × 60mm<br>Weight: 230g<br>Cells: **3S max**<br>Sensored: Yes (JST-ZH)<br>Price: ~$100 (MSRP $140) | **Ruled Out** | Pro: Lighter than EZRun 3665, competition-grade racing line<br>Con: **3S max — fails the 4S Must** | <img src="src/electronics_hobbywing_xerun_3660sd_g3.jpg" width="300"> |
| ~~Castle Creations 1515 V2 2200KV~~ (#060-0093-00) | KV: 2200<br>Can: **40mm × 75.4mm** (41.4mm with fins)<br>Weight: 426g with wires (380g without)<br>Cells: 2-6S<br>Sensored: Yes (SmartSense / sensored / sensorless)<br>Price: $195.95 (list $239.75) | **Ruled Out** | Pro: True 1/8 scale, runs 6S, rebuildable, **explicit gold-plated solder tabs**, Kevlar-wrapped rotor, 180°C-rated magnets, 10 AWG silicone wire<br>Con: **40mm × 75.4mm — fails BOTH the 36mm can Must and the ≤70mm length Must.** 426g is overkill for a 1/10 build; Castle explicitly targets 1/8 buggies / truggies and 1/10 monster trucks up to 15 lb | <img src="src/electronics_castle_1515_v2_2200kv.jpg" width="300"> |

---

## KV Reference

KV is a no-load speed rating — same top speed at same KV on same voltage. The differences between options at the same KV are torque, heat, and efficiency (stator size, lamination quality, how the motor is wound for the voltage).

The original target was 3200KV — same as the Slash 4x4. In practice the Castle 1412 3200KV gets hot enough on 4S to require a cooling fan: 3200KV × 14.8V = ~47,000 RPM no-load, which pushes the motor hard especially in grass and offroad where the drivetrain loads up at high RPM.

### Community Consensus (4S)

| KV | Character | Notes |
|----|-----------|-------|
| **1900-2200KV** | Smooth, all-day cool | Common race setup on true 1/8 buggies; light on the Jato 4x4 — usable but leaves performance on the table |
| **2400KV** | Cool, balanced | Slash 4x4 / e-Jato sweet spot. No fan needed with conservative gearing. Strong torque |
| **3000KV** | Borderline | Works but needs cooldown breaks and conservative gearing |
| **3200KV** | **Super pipey**, runs hot | Sudden / peaky power delivery, lots of top end. Generally needs a fan on 4S. What's currently in the in-hand Castle 1412 |

The FastAzJato4x4 is lighter than a true 1/8 buggy, so **2400KV is at or just above the community-preferred range** for this weight class. A 1412 3200KV running hot on 4S isn't a setup problem — it's a physics problem. Dropping to 2400KV with G3 / 4-pole 12-slot laminations eliminates the eddy-current losses driving the heat, and a fan becomes unnecessary.

### Open question: 2400KV vs 3200KV geared to the same top speed — which accelerates faster?

If both motors are geared (different pinion) to hit the same top speed:
- The 3200KV motor uses a smaller pinion (higher gear reduction) — gear ratio multiplies torque at the wheels
- The 2400KV motor uses a bigger pinion (lower gear reduction) — less mechanical advantage but the motor itself is more efficient and generates more torque per amp

Conventional wisdom is mixed:
- "Pipey" higher-KV motors with strong gearing-down often punch harder off the corner but run hotter and draw more amps
- Lower-KV motors with less gearing-down tend to be smoother and more efficient, often comparable or slightly slower in 0-x accel but with way better thermal headroom

**TODO**: Verify with actual run data — would need timed acceleration runs with 1412 3200KV (e.g. 15T pinion) vs 1415 2400KV (e.g. 19-21T pinion) on the same battery / track to settle it for this build.

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
- Castle part **#060-0085-00**; retail **$119.95** (list $146.80)
- Stator: 1.4" × 1.2" (per Castle naming); **can: 36mm OD × 62.5mm length** — fits the 36mm / ≤70mm Must
- Weight: **265.4g** (9.4oz) with wires
- Shaft: 15mm long × 1/8" (3.17mm) diameter
- Mounting: M3 bolts @ 25.4mm spacing
- Connectors: 4mm male Castle Bullet Connectors attached to **replaceable 13-gauge wires**; sensor wire 210mm included
- Max RPM: 75,000
- **Castle's official application rating**: 1/10 SC trucks / monster trucks / rock racers up to 6.5 lb on **up to 3S LiPo**. Castle says it "can be run on a 4s LiPo with very conservative gearing and keep a close eye on temperatures" — i.e. 4S is out-of-spec but possible if you're careful with gearing and watch temps. Runs hot in practice and basically requires a fan. **Real cost of the fan: weight (fan + mount) sitting up high on the motor** — user runs metal fans that don't fail in practice, so reliability isn't the issue; the issue is grams in the wrong place
- Older lamination tech — the heat isn't gearing, it's eddy-current losses in the stator
- Sensor board has silicone conformal coating (water-resistant sensor PCB), but sensor connector itself is not water resistant — Castle recommends dielectric grease on connectors after wet running
- Castle's recommended ESCs for this motor: **Mamba X**, Copperhead 10, Sidewinder 4, Cobra 10 — all confirmed in the ESC analysis
- $0 — already in hand

### Castle Creations 1415 2400KV — Candidate (leading)

- Castle part **#060-0060-00**; retail **$129.95** (list $159.00)
- Stator: 1.4" × 1.5" (per Castle naming); **can: 36mm OD × 69.5mm length** — just under the 70mm Must
- Weight: **318g** (11.2oz) with wires — heaviest 4S Castle option
- Shaft: 15.5mm long × 1/8" (3.17mm) diameter
- Mounting: M3 bolts @ 25mm spacing (note: 25mm vs 1412's 25.4mm — same drill pattern in practice but check before mounting)
- Connectors: 4mm male Castle Bullet Connectors
- Max RPM: 75,000
- **Castle's official rating**: 3S-4S LiPo, 1/10 SC trucks up to 6.5 lb. 4S is native (no "with care" caveat like the 1412)
- **Improved 4-pole 12-slot design** — better efficiency, runs cooler than the 1412
- **REBUILDABLE design** — front bell/bearing assembly and rotor/shaft assembly are user-replaceable (meets the serviceability requirement)
- QuietSense™ tech shields sensors from coil noise; Flux Shield™ + secondary sense magnets for precise startups
- ROAR-standard sensor port with labeled connections
- No mechanical timing adjustments needed — sensor alignment handles it automatically
- Optional cooling fan (Castle says "coming soon" but motor designed to not need one)
- Sensor board has silicone conformal coating (water-resistant PCB); sensor connector is not water resistant — dielectric grease recommended after wet running
- Castle's recommended ESCs: **Mamba X**, Sidewinder 4, Cobra 10, Mamba Max Pro, Copperhead 10. Fire Phoenix is not on the official list but uses standard JST-ZH which connects to the included Castle sensor wire
- $129.95 — additional cost over the in-hand 1412

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
