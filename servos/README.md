# Servo Value Matching — Premium vs. Cheap Alternative

> **Generic reference — no single winner.** The goal isn't picking one best servo, it's finding a **cheap servo whose real torque/speed at the voltage you actually run matches a quality servo's**, so you're not paying brand premium for performance you're not using. **Not tied to any one car** (shared, like [`batteries/`](../batteries/) and [`controllers/`](../controllers/)).

---

## Table of Contents

- [Why match per voltage, not headline spec](#why-match-per-voltage-not-headline-spec) — the trap this doc avoids
- [Spec format](#spec-format) — standard field order, and how to record a torque curve
- [Comparison table](#comparison-table) — premium references and their budget matches
- [Notes](#notes)

---

## Why match per voltage, not headline spec

A servo's box usually prints **one** torque number, tested at whatever voltage makes it look best, usually the top of its range (2S LiPo, 8.4V, HV). That number alone doesn't tell you what the servo does at the voltage your actual setup feeds it.

Torque and speed both climb with voltage on the same servo. So a $80 quality servo's printed "25kg·cm" at 8.4V doesn't mean a $15 servo also claiming "25kg·cm" is equivalent, if the cheap one's number was measured at a different voltage, or if it can't sustain that torque at the voltage you're actually running (4.8V and 6V analog-style setups are common in cheaper receivers/BECs, not just 2S LiPo).

**The matching method here:**
1. Take the quality servo's torque and speed **at every voltage its spec sheet lists** (typically 4.8V, 6.0V, 7.4V, 8.4V).
2. Find a cheaper servo that clears the **same numbers at the same voltage** you'll actually run, not just at some higher voltage.
3. Check the stuff torque/speed matching doesn't cover: **BEC current draw**, **digital vs. analog signal frequency**, **dead band**, **gear material**, **case/weather sealing**. A torque-matched cheap servo can still be a bad swap if it needs more current than your BEC supplies, or is digital-only on an analog-only setup (see the [PTK 9752TG-D notes](../shop/products.json) for exactly this kind of gotcha: needs 333Hz, not 50Hz, and a minimum 8A BEC).

---

## Spec format

> *Every row's Spec cell uses this order, `N/A` where unknown:* **Type · Performance · Gears · Case · Motor · Bearing · Refresh · Pulse width · Dead band · Neutral · Travel · Signal · Programmable · Size · Weight · Price**
>
> This replaces the standard `Torque · Speed · Voltage` fields (registered in [`CLAUDE.md`](../CLAUDE.md) for single-voltage servo docs) with one combined **Performance** field, since the whole point here is comparing torque *and* speed together at each voltage.

**Performance is a curve, not one number.** For every voltage the spec sheet lists, low to high, one `<br>`-separated line, torque and speed together:

```
**Performance:** 4.8V: 15kg·cm @ 0.095s/60°<br>6.0V: 18kg·cm @ 0.072s/60°<br>7.4V: 22kg·cm @ 0.060s/60°<br>8.4V: 25kg·cm @ 0.052s/60° (peak)
```

**Use whatever voltages the servo's own spec sheet actually lists** — don't invent a 4.8V or 6.0V figure a manufacturer never published just to fill the row. Most sheets cover **4.8V and 6.0V** (what a basic analog BEC feeds) plus **7.4V and 8.4V** (2S LiPo / HV), but not every servo publishes all four.

---

## Comparison table

**Sorted by max torque, best to worst** (highest kg·cm at the servo's top listed voltage, first). This is a ranked leaderboard, not a single-winner pick: 🟢 **In Hand** rows are servos already owned and used in this build group (see [`FastAzJato4x4/servo_analysis.md`](../cars/FastAzJato4x4/servo_analysis.md) for full history); 🔵 **Candidate** rows are premium servos used as reference points, not owned.

⚠️ **Some brands' printed torque numbers don't hold up under real load** (see [`Why match per voltage`](#why-match-per-voltage-not-headline-spec) above). Flag any known-inflated number in that row's Con line as it gets verified; unverified numbers are the spec sheet's claim, not a measured one.

| Servo | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| 🟢 **JX Ecoboost CLS6336HV** — *36kg·cm class, wrong size for Slash/Jato 4x4* | **Type:** Digital coreless metal-gear<br>**Performance:** 6.6V: 27.8kg·cm @ 0.14s/60°<br>7.4V: 35.6kg·cm @ 0.11s/60°<br>8.4V: 36kg·cm @ 0.09s/60° (peak)<br>**Gears:** Metal (hard-anodized aluminum)<br>**Case:** CNC metal<br>**Motor:** Coreless<br>**Bearing:** 2BB<br>**Refresh:** 330Hz<br>**Pulse width:** N/A<br>**Dead band:** 1µs<br>**Neutral:** 1520µs<br>**Travel:** 0-120° controllable (listed as 180°, mechanical sweep only)<br>**Signal:** standard PWM, JR<br>**Programmable:** No<br>**Size:** 40.5 × 20.2 × 40mm<br>**Weight:** 63g<br>**Price:** $23.85/unit (2023-12-23, [`Deals/servos.md`](../Deals/servos.md)), ~$28 now | Pro: **Highest raw torque here**, right tool for 1/8 truggy/crawler-class steering loads. Empirically validated on Mike's Arrma Kraton 1/8 truggy<br><br>Con: **Nearly 2x slower than the PTK or CLS6322HV at 7.4V** (~0.11 vs ~0.06s/60°). Not programmable. Oversized (and overweight) for a Slash/Jato 4x4-class steering load, torque this build doesn't need traded for speed it does | <img src="../cars/FastAzJato4x4/src/steering_jx_cls6336hv_servo.jpg" width="500"> |
| 🔵 **Savöx SB-2273SG** — *premium reference, not owned* | **Type:** Digital brushless, steel gear<br>**Performance:** 6.0V: 23kg·cm @ 0.12s/60°<br>7.4V: 28kg·cm @ 0.095s/60° (peak)<br>**Gears:** Steel<br>**Case:** N/A<br>**Motor:** Brushless<br>**Bearing:** N/A<br>**Refresh:** N/A<br>**Pulse width:** N/A<br>**Dead band:** N/A<br>**Neutral:** N/A<br>**Travel:** N/A<br>**Signal:** N/A<br>**Programmable:** N/A<br>**Size:** 40.3 × 20.2 × 38.7mm<br>**Weight:** 69g<br>**Price:** ~$70-90 new | Pro: **Brushless motor and steel gears**, 12-bit (4096) resolution, well-regarded competition brand. The number this doc exists to beat<br><br>Con: **Already flagged in-repo as bad value used** ([`MugenMBX8T_Eco/lot_analysis.md`](../cars/MugenMBX8T_Eco/lot_analysis.md)): sub-$20 PTK-class servos match or beat its torque/speed at a fraction of the price. Torque/speed here are spec-sheet numbers, not independently measured | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/servo_savox_sb2273sg.jpg` |
| 🟢 **PTK 9752TG-D** — *2S LiPo-ready, current pick for Slash/Jato 4x4-class* | **Type:** Digital coreless metal-gear<br>**Performance:** 5.0V: 15kg·cm @ 0.090s/60°<br>6.0V: 18kg·cm @ 0.072s/60°<br>7.4V: 22kg·cm @ 0.060s/60°<br>8.4V: 25kg·cm @ 0.052s/60° (peak)<br>**Gears:** Metal<br>**Case:** CNC metal<br>**Motor:** Coreless<br>**Bearing:** Double ball<br>**Refresh:** 333Hz<br>**Pulse width:** 500-2500µs<br>**Dead band:** 2µs<br>**Neutral:** N/A<br>**Travel:** 180° +(-)10°<br>**Signal:** SR/SHR/SFR/SXR/SSR<br>**Programmable:** Yes<br>**Size:** 42.2 × 20 × 27mm (low-profile)<br>**Weight:** 60.2g (measured)<br>**Price:** ~$19.65/ea bulk, $25 single | Pro: **Beats the Savöx SB-2273SG's speed at every shared voltage** (0.060s vs 0.095s @ 7.4V) for a quarter of the price, similar torque class (25 vs 28kg·cm @ top voltage). Low-profile, CNC metal case, programmable, proven across multiple builds in this group with no BEC brownout issues on a ≥5A BEC<br><br>Con: **High current draw, browns out weak (≤3A) BECs.** One field failure logged on a 1/8 truggy (2026-09-07), cause unconfirmed, possibly wrong class for true 1/8 truggy loads. See [full history](../cars/FastAzJato4x4/servo_analysis.md) for both | <img src="../cars/FastAzJato4x4/src/steering_ptk_9752tgd_servo_dimensions.jpg" width="500"> |
| 🟢 **JX CLS6322HV** — *predecessor to the PTK, retired, out of stock* | **Type:** Digital coreless metal-gear<br>**Performance:** 6.0V: 17.21kg·cm @ 0.09s/60°<br>7.4V: 21.06kg·cm @ 0.07s/60° (peak)<br>**Gears:** Metal<br>**Case:** N/A<br>**Motor:** Coreless<br>**Bearing:** 2BB<br>**Refresh:** 330Hz<br>**Pulse width:** N/A<br>**Dead band:** 1µs<br>**Neutral:** 1520µs<br>**Travel:** N/A<br>**Signal:** N/A<br>**Programmable:** N/A<br>**Size:** 55 × 20 × 40mm<br>**Weight:** 67.3g (measured)<br>**Price:** $17.13/ea in bulk (historical) | Pro: **Cheapest ever run in this group**, the standard for years (16 units across 5 orders). "Fish-tested": survived 10+ saltwater dunks despite no waterproof rating<br><br>Con: **Superseded and out of stock.** ~17% slower than the PTK at 7.4V, lowest torque ceiling here. Failure mode is electrical (pot/centering drift) after ~2 years 11 months, not mechanical — gears never stripped across all 16 units | <img src="../cars/FastAzJato4x4/src/steering_jx_cls6322hv_servo_weight.jpg" width="500"> |

---

## Notes

- **Match at the voltage you'll actually run, not the servo's best-case voltage.** A cheap servo that only hits the premium servo's torque at 8.4V is not a match for a build feeding it 6V.
- **Torque/speed matching is necessary but not sufficient.** Always cross-check BEC current draw, signal frequency (analog 50Hz vs. digital, often 300Hz+), dead band, and gear/case material separately, a cheap servo can match the torque curve and still be the wrong swap.
- **Brand honesty on spec sheets is still an open question for this doc.** The four rows above are spec-sheet numbers except where a build in this group has independently measured one (noted per row when so). Flag known-inflated brands/models here as they're identified.
- Full ownership history, failure modes, and BEC/frequency gotchas for the PTK and JX servos live in [`FastAzJato4x4/servo_analysis.md`](../cars/FastAzJato4x4/servo_analysis.md); price history in [`Deals/servos.md`](../Deals/servos.md).
