# Steering Bell Crank Selection — FastAzJato4x4

> **Leaning toward: generic AliExpress aluminum bell crank set (~$10)** — same family the K939 build already runs without issues. The bell crank is mostly a "doesn't have to be premium" part; the bigger steering performance wins come from the servo, not the bell crank brand.

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Bell Crank Comparison](#bell-crank-comparison)
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Fits Slash 4x4 / Jato 4x4 servo + bulkhead pattern** | Must | Has to bolt to the same mounting points as the OEM bell crank |
| **Bearing-supported (not bushing)** | Must | Bearings deliver consistent steering feel under load; bushings introduce slop within a few packs |
| **Doesn't flex measurably under servo load** | Must | Stock plastic bell cranks deflect under hard steering inputs from the chosen PTK 9752TG-D high-speed metal-gear servo — costs steering precision |
| **Cheap** | May | Bell cranks rarely fail in crashes (servo saver absorbs most impacts before the crank itself sees the load); upgrade for stiffness, not for crash survival |

---

## Bell Crank Comparison

| Bell Crank | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **Generic AliExpress aluminum servo bell crank set** | Material: **7075-T6 / 6061 aluminum**<br><br>Bearing-supported<br><br>Price: **~$10 shipped** | Pro: Bearing-supported, same set the K939 already runs without issues. Stiff enough for a strong servo, doesn't flex measurably<br><br>Con: QC varies seller-to-seller; no brand warranty | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/steering_aliexpress_aluminum_bell_crank.jpg` |
| 🔵 **Integy aluminum bell crank** (Slash 4x4 / Jato 4x4 fit) | Material: 7075-T6 aluminum<br><br>Bearing-supported<br><br>Price: $25-40 | Pro: Known brand, QC consistent, anodized color options, bearing-supported, full Slash family fit<br><br>Con: 2.5-4× the AliExpress generic for marginal real-world improvement | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/steering_integy_aluminum_bell_crank.jpg` |
| 🔵 **GPM aluminum bell crank** (Slash 4x4 / Jato 4x4) | Material: 7075-T6 aluminum<br><br>Price: $25-35 | Pro: Color options (orange, blue, red, black, etc.), well-machined, similar quality to Integy<br><br>Con: Same diminishing-returns story vs the AliExpress generic | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/steering_gpm_aluminum_bell_crank.jpg` |
| ❌ **Traxxas stock plastic bell crank** | Material: glass-filled nylon<br><br>Price: free (stock) | Pro: Free if stock car is sourced, bulletproof in crashes<br><br>Con: **Flexes under the chosen PTK 9752TG-D servo's load** — measurable on-throttle understeer because the crank is moving when the wheels should be. Servo's force is wasted bending plastic instead of turning wheels. **Any decent modern servo wildly over-powers stock** — practically useless out of the box. There's a workaround (add a washer under the spring perch to preload the saver tighter so it slips less), but installing it is a pain. Just spend the few bucks on a generic cheap aluminum bell crank and skip the headache | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/steering_traxxas_stock_bell_crank.jpg` |

---

## Notes

- **The servo matters more than the bell crank.** The K939 build's "aluminum bell crank + decent metal-gear servo" combo is the budget sweet spot — any further bell crank upgrade gets dominated by what servo you're driving it with.
- **Bearing replacement:** the AliExpress generic ships with standard 5×10×4mm bearings (same as everywhere else in the drivetrain). Easy to replace when they wear after many packs.
- **Servo saver — skip it.** The OEM Traxxas servo saver is **weak by modern standards** and doesn't actually buy you much: aluminum bell cranks eventually "weld" the saver into a fixed coupling anyway (slip surfaces fuse from heat + friction after enough cycles — desired for racing, supposedly bad for bashing). The build group's empirical answer on this is "**don't bother**" — the JX / PTK servos we run handle direct crash transmission for multi-year service lives (see [`servo_analysis.md`](servo_analysis.md#notes)), so the protection the OEM saver is supposed to provide isn't needed. Run the rig saverless.
- **Linkages / tie rods** are a separate sub-system not covered here. Stock plastic linkages are fine for the FastAzJato4x4; aluminum linkages add weight without benefit since the steering loads don't deflect plastic linkages noticeably.
