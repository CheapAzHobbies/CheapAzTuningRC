# Motor Selection — Jato4x4_Mike

> **Running: Castle Creations 1412 3200KV on an 11T 32P pinion and 54T spur, through a Castle Mamba X 6S.** The motor is the same one the [FastAzJato4x4](../FastAzJato4x4/motor_analysis.md#castle-creations-1412-3200kv--in-hand) has in hand, so its specs are not repeated here. **What is unique to this car is the gearing, and the finding that came out of it.**
>
> **Gearing for the power band beat chasing the smallest pinion**, which overturned the assumption the build started with. **The write-up below was recorded at 12T, and the car has since moved to 11T.** The finding stands as reached; the gearing simply came down one tooth after it.

<p align="center"><img src="../FastAzJato4x4/src/electronics_castle_1412_3200kv.jpg" width="500"><br><em>Castle Creations 1412 3200KV, shared with the FastAz. Full specs in that doc</em></p>

---

## The gearing finding

**The original intuition was wrong.** Going in, the assumption was that **higher RPM equals better air control**, so chasing the smallest pinion was the obvious move.

**What actually happened: torque matters as much as RPM.** Gearing for the **power-band sweet spot** (12T here, not the tiniest pinion available) made mid-air corrections feel just as responsive as the high-RPM theory promised, **and** kept the motor cooler because it is neither lugging nor screaming.

| Observation | Result |
|---|---|
| **Motor temperature** | **Noticeably cooler** than the previous taller gearing |
| **Power band** | **Lands where it is useful**, more usable thrust across the whole throttle rather than only at the top |
| **Sound** | Higher than ever before, the motor is getting into its happy RPM range |
| **Overall feel** | Car feels lighter and faster, less effort everywhere, sharper throttle response |

> **Why this matters beyond this car.** It is the empirical data point that **pinion sizing is not purely a top-speed equation**. Gearing for the power-band sweet spot beat gearing for theoretical max RPM, on the same motor. The FastAz cites this when picking its own pinion. Tooth options in the [FastAz pinion reference](../FastAzJato4x4/motor_analysis.md#pinion-reference-32p).

---

## Setup

| Item | Spec |
|---|---|
| **Motor** | **Castle Creations 1412 3200KV** (specs in the [FastAz doc](../FastAzJato4x4/motor_analysis.md#castle-creations-1412-3200kv--in-hand)) |
| **Pinion** | **11T 32P** (was 12T when the finding above was made) |
| **Spur** | **54T** |
| **ESC** | **Castle Mamba X SCT**, bought as a combo with this motor (**010-0155-13**). ⚠️ **4S max with this motor**, see [`esc_analysis.md`](esc_analysis.md) |
| **Cooling** | N/A 🚧 not recorded |

---

## Motor bearing service

**Bearings replaced ~2026-09-06, first run on them 2026-09-12.** The car has run **4 battery packs** on them since.

**Running the S605ZZ 5×14×5 ABEC-9** rather than the stock Castle bearings. **The stock ones work, they just burn up quickly**, and these last longer in the same motor. Full spec, price and the sourcing caveat in [`bearings_reference.md`](bearings_reference.md#the-motor-bearing-s605zz).

🚧 **How many packs a set lasts is still unknown.** The count is logged in [`maintenance/README.md`](../../maintenance/README.md) and keeps climbing until a set wears out, which is what turns this into a real replacement interval instead of a guess.

---

## Price History

The motor was not bought on its own. It came in the **010-0155-13 combo** with the Mamba X SCT, so the receipt and the RMA replacement are in [`esc_analysis.md`](esc_analysis.md#price-history).

---

## Notes

- **The motor is shared, the gearing is not.** Motor comparison, KV theory and the stator arguments all live in the [FastAz motor doc](../FastAzJato4x4/motor_analysis.md). Only this car's gearing and the result are recorded here.
- **This is the origin of the pinion reasoning on both cars.** Mike's Jato came first, so the power-band conclusion was reached here and the FastAz inherited it.
- **🚧 No temperatures were logged.** "Noticeably cooler" is subjective. A logged temp before and after would turn the best finding on this car into a hard number.
