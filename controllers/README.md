# Radio Transmitter (Controller) Comparison

> **Generic reference — no single winner.** Surface radios run from throwaway kit units to pro racing rigs, and each tier has its place depending on budget, how much tuning/telemetry you want, and which receiver ecosystem you're locked into. This doc compares the tiers so a specific controller can be slotted in later. **Not tied to any one car** (shared, like [`batteries/`](../batteries/)).

---

## Table of Contents

- [What to evaluate](#what-to-evaluate) — the factors that actually matter
- [Spec format](#spec-format) — standard field order for every row
- [Comparison by tier](#comparison-by-tier) — kit / budget / mid / premium
- [Protocols & ecosystems](#protocols--ecosystems) — what the receiver locks you into
- [Notes](#notes)

---

## What to evaluate

| Factor | What it affects |
|---|---|
| **Form factor (wheel vs stick)** | Surface RC uses **wheel/pistol** radios; sticks are for air. Drives ergonomics for long sessions |
| **Channels** | 2 (steer + throttle) is the floor; extra channels run gyro gain, 2-speed, lights, diff locks, etc. |
| **Protocol / receiver ecosystem** | Locks you into one brand's receivers (Flysky AFHDS, Spektrum DSMR, Futaba T-FHSS, Sanwa FH5, ExpressLRS). Switching later is costly |
| **Latency / response** | Pro radios feel more direct off-center; matters for racing, less for bashing |
| **Built-in gyro support** | Steering stability on loose/low-grip surfaces; needs a capable radio **and** a gyro receiver |
| **Telemetry** | Pack voltage, temps, RPM back to the radio; needs a compatible RX + sensors |
| **Model memory** | How many cars one radio stores |
| **Adjustability** | EPA, expo, dual-rate, ABS/brake, throttle curves |
| **Battery** | AA cells vs built-in rechargeable LiPo; runtime |
| **Price** | ~$40 throwaway to $400+ pro |

---

## Spec format

> *Every row's Spec cell uses this fixed order, `N/A` where unknown or not applicable:* **Type · Channels · Protocol · Receivers · Gyro · Telemetry · Model memory · Display · Battery · Price**

---

## Comparison by tier

No ⭐ winner — these are 🔵 reference points by tier. A specific controller gets added as its own row when it comes in.

| Radio | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| 🔵 **Kit-bundled — Traxxas TQ / TQi** | **Type:** wheel<br>**Channels:** 2–3<br>**Protocol:** Traxxas TQ 2.4 GHz<br>**Receivers:** Traxxas only<br>**Gyro:** via model-side TSM (not in radio)<br>**Telemetry:** TQi only (Bluetooth + Traxxas Link app)<br>**Model memory:** N/A<br>**Display:** none (TQ) / phone (TQi)<br>**Battery:** AA<br>**Price:** free with kit (~$60–130 standalone) | Pro: Comes with Traxxas RTRs; TQi adds app telemetry + stability tuning<br><br>Con: Minimal tuning, locked to Traxxas RX, no real screen | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/controller_traxxas_tq_tqi.jpg` |
| 🔵 **Budget — Flysky FS-GT5 / GT3C** | **Type:** wheel<br>**Channels:** 3–6<br>**Protocol:** AFHDS 2A<br>**Receivers:** Flysky (cheap, plentiful)<br>**Gyro:** model-dependent<br>**Telemetry:** basic (voltage)<br>**Model memory:** ~10–20<br>**Display:** small mono LCD<br>**Battery:** AA<br>**Price:** ~$40–70 | Pro: Cheap, reliable, dirt-cheap receivers to outfit many cars<br><br>Con: Basic feel, older protocol, limited tuning | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/controller_flysky_gt5.jpg` |
| 🔵 **Mid — Flysky Noble NB4 / NB4+** | **Type:** wheel<br>**Channels:** 4+<br>**Protocol:** AFHDS3<br>**Receivers:** Flysky AFHDS3 (e.g. FGR4S)<br>**Gyro:** yes (with gyro RX)<br>**Telemetry:** yes<br>**Model memory:** many<br>**Display:** color touchscreen<br>**Battery:** built-in LiPo<br>**Price:** ~$160–230 | Pro: Color touchscreen, gyro + telemetry, rechargeable, strong value<br><br>Con: Smaller RX ecosystem than Spektrum/Futaba; AFHDS3 is newer/less universal | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/controller_flysky_noble_nb4.jpg` |
| 🔵 **Premium racing — Sanwa M17 / Futaba 7PX / Spektrum DX6R** | **Type:** wheel<br>**Channels:** 4+<br>**Protocol:** Sanwa FH5 / Futaba T-FHSS / Spektrum DSMR<br>**Receivers:** brand-specific (large ecosystems)<br>**Gyro:** yes (brand SSL / stability RX)<br>**Telemetry:** full<br>**Model memory:** many<br>**Display:** large color<br>**Battery:** built-in LiPo<br>**Price:** ~$300–450+ | Pro: Lowest latency, best ergonomics/feel, deep tuning + telemetry, big RX ecosystems<br><br>Con: Expensive; receivers add up fast; overkill for bashing | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/controller_premium_racing.jpg` |

---

## Protocols & ecosystems

- **Flysky AFHDS 2A / AFHDS3** — cheapest receivers; AFHDS3 adds gyro/telemetry support. Good value lock-in.
- **Spektrum DSMR** — huge US support, receivers everywhere, AVC stability on some RX.
- **Futaba T-FHSS / Sanwa FH5** — premium racing, low latency, brand-only receivers.
- **Traxxas TQ / TQi** — closed system; TQi adds Bluetooth telemetry via the Traxxas Link phone app.
- **ExpressLRS (ELRS)** — open, very long range / low latency; mostly air but surface options exist; DIY-friendly.

---

## Notes

- **No single winner — match the radio to the use.** Bashing / kit running: TQ/TQi or budget Flysky. Modern features on a budget: Noble NB4. Racing feel: Sanwa / Futaba / Spektrum.
- **You buy into a receiver ecosystem, not just a radio.** Every car needs a matching RX, so switching brands later means re-buying receivers.
- **Gyro/stability needs both ends** — a capable radio plus a gyro receiver (or a model-side unit like Traxxas TSM).
- Specific controllers get added as their own rows as they come in.
