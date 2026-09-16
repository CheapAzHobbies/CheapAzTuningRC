# Traxxas Jato 4x4 — Mike's

> Mike's car. Related to but not the same as the [FastAzJato4x4](../FastAzJato4x4/README.md) build (which is co-developed with Mike). Setup notes recorded here for reference and cross-build tuning.

---

## Table of Contents

- [Car Overview](#car-overview)
- [Suspension](#suspension)
- [Steering](#steering)
- [Chassis](#chassis)
- [Drivetrain](#drivetrain)
- [Batteries](#batteries)
- [Wheels & Tires](#wheels--tires)
- [Aero & Body](#aero--body)
- [Electronics](#electronics)
- [Tuning Notes](#tuning-notes)
- [Parts Purchased](#parts-purchased)
- [TODO / Notes](#todo--notes)

---

## Car Overview

**Base Car:** Traxxas Jato 4x4 — Mike's personal build.

> **This is the car the [FastAzJato4x4](../FastAzJato4x4/README.md) was born out of.** Mike's Jato came first and the R&D happened here: the diff and shock oils, the pistons and the custom axle build were all worked out on this car, together, and the FastAz inherited the answers. So where the two docs agree, **this is the origin and that one is the copy** — worth knowing when the settings look identical.
>
> The two have since diverged. This car keeps the **plastic chassis**, runs **different hubs**, and solves the hub-bearing problem the opposite way (bigger bearing, shaved hexes, rather than a sleeve). Those differences are the interesting part and are called out section by section below.
>
> Originally noted as "Slash" — it's actually a Jato 4x4.

---

## Suspension

### Shock Oil

| Position | Weight |
|----------|--------|
| Front | **37.5wt** (Losi TLR74030, 468 cSt) |
| Rear | **50wt** (Associated 5480 FT, 650 cSt) |

> **Same spec as the [FastAzJato4x4](../FastAzJato4x4/shock_analysis.md#setup-spec-springs--pistons--oil), and this car is where it was arrived at** — the two were tuned together, starting here. Rear heavier than front because the motor sits at the back and the car is tail-heavy for a 1/8.

### Pistons

| Position | Piston |
|----------|--------|
| Front | 6 hole × 1.4 |
| Rear | 6 hole × 1.2 |

---

## Steering

| Component | Part | Weight (pair) |
|-----------|------|---------------|
| Front C-Hub / Caster Block | **Stock plastic EHD**, running now | N/A |
| Front Steering Block / Knuckle | **MonsterKingz alloy**, running now | N/A |
| Rear Hub Carriers | **Stock plastic EHD**, running now. **Plan: swap to a shaved-down MonsterKingz rear hub** for the slim Raptor R look at a lower price | N/A |
| ~~LIGHT HOUSE Aluminum Front C Hub/Knuckle Arm~~ (black) | **Broke**, retired | 25.5 g bare · 36.4 g w/ hardware |
| ~~LIGHT HOUSE Aluminum Front Hub/Knuckle Arm~~ (black) | **Broke**, retired | 22.4 g bare · 34.9 g w/ hardware |

> **Why the change:** the Lighthouse front C-hub and carrier broke, so Mike moved onto a **MonsterKingz metal set bought off the FastAzJato4x4 for $50** (2026-09-07). **It didn't fail stock**, he'd filed the hinge pocket for droop. Full write-up, the measured Lighthouse weights, the shaved 17mm hexes and the planned rear shave are all in [`hub_analysis.md`](hub_analysis.md).

---

## Chassis

| Component | Part | Notes |
|---|---|---|
| Chassis | **Stock plastic** | **The big divergence from the [FastAzJato4x4](../FastAzJato4x4/chassis_analysis.md), which went carbon fiber.** Plastic flexes rather than cracking, and it's already on the car, so there's nothing to buy |
| Front bulkhead | **Powerhobby aluminum** | The front is where bulkheads get loaded and where the plastic one gives up. On the FastAz this came bundled with the CF chassis kit; here it's the standalone part (~$36.99 on its own, [`chassis_analysis.md`](../FastAzJato4x4/chassis_analysis.md#bulkheads-front--rear)) |

> **Worth noting for anyone pricing a build:** this combination is the honest cheap route. A plastic chassis plus one alloy front bulkhead covers the part that actually fails, without the carbon kit. It's also the pairing that makes [metal arms risky](../FastAzJato4x4/arm_analysis.md) — FLM arms strip a *plastic* bulkhead, which is exactly why the alloy front matters here.

---

## Drivetrain

| Position | Part |
|----------|------|
| Pinion | **12T 32P** |
| Spur | **54T** |

### Custom Axles (shared with FastAzJato4x4)

> **Bearings:** this car runs a **bare 10×18×5 in the hub**, which needed the **17mm hex adapters shaved down** to fit, not the hub carriers. The FastAz solves the same problem with a sleeve and a 10×15×4 instead, so only the hub position differs. Full list, costs and the route comparison in [`bearings_reference.md`](bearings_reference.md).

Both Jatos run **custom axles built from chopped E-Revo 1.0 CVDs**. Length is dialed on an **adjustable threaded prototype** first, then the **final axles are welded** to that length (simpler, tools on hand, a fresh set is cheap to remake). **Shorter axle = front.** Full build write-up and the rejected join methods are in [`FastAzJato4x4/driveshaft_analysis.md`](../FastAzJato4x4/driveshaft_analysis.md#shortening--joining-e-revo-cvds-custom-axles-wip).

### Diff Oil

> **This car is where the setup came from.** Mike's Jato was the first of the two, and the oils were tuned here together before the [FastAzJato4x4](../FastAzJato4x4/differential_analysis.md) inherited them. Both cars run the same spec.

| Diff | Weight | Note |
|---|---|---|
| **Front** | **30k** (Traxxas TRA5136) | Calms torque steer on the heavy 4S car |
| **Center** | **100k** (Traxxas TRA5130) | Holds drive stability |
| **Rear** | **10k, run greased** (Traxxas TRA5135) | Drive off the corner |

---

## Batteries

> **Mounting, bar heights and max pack size live in [`battery_analysis.md`](battery_analysis.md).** Max best fit is **152 × 48 × 44mm**.

Runs **full length 4S packs**, which is where this car and the [FastAzJato4x4](../FastAzJato4x4/battery_analysis.md) split. That car went **shorty hardcase only**, so the two no longer buy to one shared spec.

**Soft case or hard case, both run here.** No case requirement on this car, unlike the FastAz, which went hardcase-only because of the sand at Meldrum.

**The three CNHL packs bought 2026-08-26 run on this car:** Racing 5200 (soft), Lightning 5500 (soft), Ultra-Thin 6000 (hardcase).

**IR check on the Racing 5200** (HOTA T6, mid-charge): 2.3 / 2.2 / 2.3 / 2.1 mΩ per cell, ~2.23mΩ avg. Using the [E-Revo IR-to-True-C method](../ERevo_1.0/battery_analysis.md#c-ratings-and-internal-resistance) (`max A = sag ÷ IR`, `true C = max A ÷ Ah`), that's roughly **26-43C true** (0.3V/0.5V sag) against the **90C printed on the label**. Charger reads LiHV-4S(4.35V), so this pack is **HV**. Informational only, the CNHL packs aren't in the shared cycle tracker.

<p align="center"><img src="src/electronics_cnhl_racing_5200_90c.jpg" width="500"><br><em>CNHL Racing 90C 5200mAh, per-cell IR mid-charge</em></p>

**IR check on the Ultra-Thin 6000** (HOTA T6, charge done 100%): 4.5 / 4.3 / 4.6 mΩ per cell (4th cell didn't register), ~4.47mΩ avg. Same method: roughly **11-19C true** against the **120C printed on the label**. Also reads LiHV-4S(4.35V) on the charger, so both CNHL packs photographed so far are **HV**, not standard voltage. The third pack in this order, the Lightning 5500, hasn't been photographed yet, so its voltage class is unconfirmed. Informational only.

<p align="center"><img src="src/electronics_cnhl_ultrathin_6000_120c.jpg" width="500"><br><em>CNHL Ultra-Thin 120C 6000mAh, 15.2V, per-cell IR at 100% charge</em></p>

**Gens Ace Redline 2.0 4S HV 6300mAh 140C** also runs here — full-length (139 × 47 × 37mm, 452g), not a shorty, so it never fit the FastAzJato4x4's shorty-only spec but works well on this car. Bought 2025-10-22 for $107.38 (see [`FastAzJato4x4/battery_analysis.md`](../FastAzJato4x4/battery_analysis.md) for full specs and price history). Currently on loan/testing here; may just become Mike's outright since it works well and this build doesn't run long 4S packs.

**Sharing still works one way:** shorties fit this car as well, so anything bought to the FastAz spec can run here, while the full length packs stay on this one.

Height is the one real constraint, and **44mm is the stock ceiling**, not the 35mm quoted here before. 35mm is just one setting (the 7426X bar in the upper hole, low orientation); the same bar flipped over gives **44mm**. This car runs a **3D printed battery bar**, and **a 47mm shorty goes in regardless**, since the printed bar flexes over the last 3mm and a shorty sits in the middle of the tray rather than out at the sides where the clearance is tight. Full geometry, both stock bars and the max pack size in [`battery_analysis.md`](battery_analysis.md).

---

## Wheels & Tires

| Item | Spec |
|---|---|
| **Rims** | **Traxxas Jato 4x4 VXL 3.0" dished wheels — 17 mm hex** (white). Assembled tire+wheel set: **TRA9074-WHT**; wheels-only sold separately (verify exact SKU). |
| **Tires** | **RedSpider** tires **mounted on the Traxxas Jato 4x4 rims** to widen the track |

> **Wide-track trick:** we took the RedSpider tires and mounted them on the **Traxxas Jato 4x4 rims**, which push the wheels out and **widen the track (stance) by a lot**. It worked great here, more stability and corner grip. Note this puts it **outside ROAR width limits**, fine for a bash/fun setup like Mike's.
>
> **Wear-in:** these RedSpider tires take **~7 battery packs of running to fully wear in** before they reach maximum grip / performance — don't judge them when fresh.
>
> The **[FastAzJato4x4](../FastAzJato4x4/README.md) runs the same RedSpider tires but on standard-width rims** (not the wide Traxxas-rim trick) to **stay ROAR legal**.

---

## Aero & Body

| Component | Part | Notes |
|-----------|------|-------|
| Body / shell | Traxxas Jato 4x4 body, green (exact SKU TBD) | $36.00, paid for by me — tracked in [`/LEDGER.md`](../../LEDGER.md), not here |

---

## Electronics

| Component | Part |
|-----------|------|
| Motor | **Castle Creations 1412 3200KV** |

**Motor bearing service tracking:** bearings replaced ~2026-09-06, first run on them 2026-09-12. Tracked by weekend run count (no battery tracker for this car) in [`maintenance/README.md`](../../maintenance/README.md), the goal is catching the next replacement before they blow rather than after.

---

## Tuning Notes

**12T 32P pinion on a 54T spur + Castle 1412 3200KV is the keeper combo.**

Original intuition was that **higher RPM** = better air control, so chasing the smallest pinion was the obvious move. Real-world finding: **torque matters as much as RPM** — gearing for the **power-band sweet spot** (12T here, not the tiniest pinion) makes mid-air corrections feel just as responsive as the high-RPM theory promised, *and* keeps the motor cooler because it's neither lugging nor screaming.

Subjective on-track:
- **Motor runs noticeably cooler** vs the previous taller gearing
- **Power band lands where it's useful** — more usable thrust through the whole throttle, not just at the top
- **"WOOOOO" sound is higher than ever before** — the motor is actually getting up into its happy RPM range
- **Car feels lighter and faster overall** — less effort everywhere, throttle response sharper

Cross-reference for the FastAzJato4x4 pinion decision (currently TBD): the 12T 32P / 3200KV combo on this Jato is the empirical data point that pinion sizing is **not** purely a top-speed equation — gearing for the power-band sweet spot beats gearing for theoretical max RPM.

---

## Parts Purchased

| Date | Part | Qty | Total | Source |
|------|------|-----|-------|--------|
| 2026-09-07 | MonsterKingz / G-Maxx 7075 alloy hub set (front + rear) | 1 set | $50.00 | Bought off the [FastAzJato4x4](../FastAzJato4x4/hub_analysis.md) |
| 2026-05-19 | LIGHT HOUSE Aluminum Front C Hub/Knuckle Arm for Traxxas Jato 4x4 BL-2S (black) | 1 | $15.29 | AliExpress — LIGHT HOUSE 188527 Store |
| 2026-05-19 | LIGHT HOUSE Aluminum Front Hub/Knuckle Arm for Traxxas Jato 4x4 BL-2S (black) | 1 | $14.42 | AliExpress — LIGHT HOUSE 188527 Store |

> Both items shipped on the same order **#8210896333264866** — subtotal $29.71, paid **$24.67** ($5.04 off). Free returns within 90 days.

> Money Mike owes for parts (FLM arms, E-Revo CVD axle set) is tracked in [`/LEDGER.md`](../../LEDGER.md), not here.

---

## TODO / Notes

- [x] Chassis confirmed: **stock plastic + Powerhobby alloy front bulkhead**
- [ ] Weigh the car (no all-up figure recorded yet)
- [ ] Confirm the arm setup vs the FastAzJato4x4
- [ ] Add electronics + drivetrain details
- [ ] Add photos
