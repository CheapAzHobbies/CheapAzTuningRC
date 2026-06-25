# ESC + Motor Selection — E-Revo 1.0

> **Leaning: Hobbywing EZRun MAX8 GS2 ESC + 4278SD 2250KV G2R combo (HWI38010607), $208.99.** Switching from the Castle path. Not for speed (KV is basically identical to the Castle 1515, so same top end on 6S) but for the **G2S reliability** (no cutout at ramps), telemetry, waterproofing, and value. Price tracked in [`Deals/escs.md`](../../Deals/escs.md); the Castle Memorial Day numbers are in [`Deals/castle_creations_memorial_day_2026.md`](../../Deals/castle_creations_memorial_day_2026.md).

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **6S capable** | Must | The E-Revo runs 6S (2× 3S LiHV) |
| **Waterproof / dustproof** | Must | Dirt track + occasional beach |
| **No power cutout on jumps / extremes** | Must | A cut mid-ramp wrecks the landing; the Hobbywing **G2S** fixes the plain G2's cutout issue |
| **BEC strong enough for the digital servo** | Must | Needs a solid switch-mode BEC, no brownouts |
| **Sensored** | May | Smoother low-speed control out of corners |
| **Telemetry / programmable** | May | Logging temps/voltage/RPM helps tuning |

---

## ESC Comparison

> *Spec format: Cells · Current (A) · BEC · Sensored · Waterproof · Weight · Price*

| ESC | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **Hobbywing EZRun MAX8 GS2** | **Cells:** 4S–6S<br>**Current (A):** N/A (MAX8-class)<br>**BEC:** 6A/15A switch-mode, 6–8.4V<br>**Sensored:** Yes<br>**Waterproof:** Yes (+ dustproof)<br>**Weight:** 194 g<br>**Price:** $208.99 combo (see [Deals](../../Deals/escs.md)) | Pro: **G2S = no cutout at ramps/extremes;** 3× 680µF caps (870µF, +74% vs MAX8, no external cap needed); frameless fan + radiator cooling; 32° turbo timing (+25% RPM); HW Link app + Bluetooth logging; LVC / thermal / fail-safe / reverse-polarity protection. **Dims 60×48×40.5 mm**<br><br>Con: Locked to the Hobbywing ecosystem; OTA programmer / LCD box sold separately | — |
| 🥈 **Castle Mamba Monster X (ESC-only, 010-0145-00)** | **Cells:** 6S (25.2V) WP<br>**Current (A):** N/A<br>**BEC:** N/A<br>**Sensored:** Yes-capable<br>**Waterproof:** Yes<br>**Weight:** N/A<br>**Price:** $147.96 (Memorial Day + 26% student) | Pro: **Cheapest path — reuses the owned 1515 2200KV motor** (no second motor to buy); proven Castle reliability + Castle Link<br><br>Con: No combo motor/spare; Memorial-Day pricing was a one-time sale (May 2026) | — |

---

## Motor Comparison

> *Spec format: Type · KV · Cells · Can · Shaft · Sensored · Poles/Slots · Rotor · Max RPM · Max temp · Bearings · Rebuildable · Weight · Price*

| Motor | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| 🟢 **Castle 1515 2200KV** — *owned* | **Type:** Brushless sensored<br>**KV:** 2200<br>**Cells:** 6S<br>**Can:** 1515 (~36 mm)<br>**Shaft:** N/A<br>**Sensored:** Yes<br>**Poles/Slots:** N/A<br>**Rotor:** N/A<br>**Max RPM:** N/A<br>**Max temp:** N/A<br>**Bearings:** N/A<br>**Rebuildable:** N/A<br>**Weight:** N/A<br>**Price:** owned | Pro: **Already owned** — pair with the Castle Monster X ESC for the cheapest fast setup<br><br>Con: Smaller can than the 4278; tied to the Castle ESC path | — |
| 🔵 **Hobbywing 4278SD G2R 2250KV** — *comes in the combo* | **Type:** Brushless sensored (waterproof sensor)<br>**KV:** 2250<br>**Cells:** 3–6S<br>**Can:** 4278 (42 mm dia × 78 mm)<br>**Shaft:** N/A<br>**Sensored:** Yes<br>**Poles/Slots:** N/A<br>**Rotor:** N/A<br>**Max RPM:** N/A<br>**Max temp:** N/A<br>**Bearings:** N/A<br>**Rebuildable:** N/A<br>**Weight:** N/A<br>**Price:** included in $208.99 combo | Pro: **Bigger 42 mm can** = more torque headroom + cooler running; lower internal resistance (G2R); waterproof sensor; ships with the ESC<br><br>Con: Redundant if reusing the 1515; only worth it for the spare/bigger motor | — |

---

## Notes

- **Speed: it's a wash.** Castle 1515 **2200KV** vs Hobbywing 4278SD **2250KV** — same KV, so same RPM/top speed on the same 6S + gearing. The brand swap doesn't make the truck faster; **traction (tires/setup) and gearing do.**
- **Why switch to Hobbywing anyway:** the **G2S doesn't cut out at ramps / in extreme conditions** (the plain G2 does), plus telemetry, waterproofing, and a combo that's **~$39 under the equivalent Castle combo** with a spare 4278 motor.
- **Cheapest equally-fast path:** keep the owned **1515 2200KV** and add just the **Castle Monster X ESC ($147.96)** — same speed, no second motor. The Hobbywing combo only wins on reliability/telemetry/spare-motor, not speed.
- **Open decision:** if going Hobbywing, run the combo's **4278SD** or keep the **1515** on the MAX8 GS2 — both are 6S, ~same KV.
- **Cheaper combo option (verify motor):** Hobbywing-direct **MAX8 G2S combo for $187** (code **HWTRYOUTS**), ~$22 under the eBay 4278SD/$208.99. The listing is inconsistent — checkout says **4274SD G2R**, learn-more says **4268/4278 SD G2** (likely a typo). **Confirm the motor + gen before ordering** (4274 = 396 g vs 4278 = 455 g; G2R is the updated motor). If it ships the **4278SD G2R**, it's the **same combo as the eBay 38010607 for $22 less**. See [`Deals/escs.md`](../../Deals/escs.md).
- **Price + buying note (G2S not G2)** live in [`Deals/escs.md`](../../Deals/escs.md).
