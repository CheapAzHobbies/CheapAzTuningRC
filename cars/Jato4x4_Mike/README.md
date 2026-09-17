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

**Base Car:** started as a **running Traxxas Slash 4x4**, built up to Jato 4x4 spec.

> **This is the car the [FastAzJato4x4](../FastAzJato4x4/README.md) was born out of.** Mike's Jato came first and the R&D happened here: the diff and shock oils, the pistons and the custom axle build were all worked out on this car, together, and the FastAz inherited the answers. So where the two docs agree, **this is the origin and that one is the copy**, worth knowing when the settings look identical.
>
> The two have since diverged. This car keeps the **plastic chassis**, runs **different hubs**, and solves the hub-bearing problem the opposite way (bigger bearing, shaved hexes, rather than a sleeve). Those differences are the interesting part and are called out section by section below.
>
> **On the Slash vs Jato question: it started as a running Slash 4x4**, and that is not a correction to make, it is the build. **The two are the same platform**, so the donor carries straight over. What makes it a Jato 4x4 is the **towers, shocks and wing**, which are the parts that actually differ between them. Anyone pricing this build should start from a running Slash 4x4 and budget those three.

---

## Suspension

### Shock Oil

| Position | Weight |
|----------|--------|
| Front | **37.5wt** (Losi TLR74030, 468 cSt) |
| Rear | **50wt** (Associated 5480 FT, 650 cSt) |

> **Same spec as the [FastAzJato4x4](../FastAzJato4x4/shock_analysis.md#setup-spec-springs--pistons--oil), and this car is where it was arrived at**, the two were tuned together, starting here. Rear heavier than front because the motor sits at the back and the car is tail-heavy for a 1/8.
>
> 🔧 **If the rear packs, drop it to 47.5wt** (Associated FT, 613 cSt), one small step down from the 50wt in it now. This car's rear piston is the more restrictive **6 × 1.2**, so it is likelier to pack than the FastAz. See [`shock_analysis.md`](shock_analysis.md#if-the-rear-packs).

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
| Chassis | **Traxxas 7422 LCG plastic** ($20) | **The big divergence from the [FastAzJato4x4](../FastAzJato4x4/chassis_analysis.md), which went carbon fiber.** Plastic flexes rather than cracking. ⚠️ **It's the LCG chassis, so LCG-only parts are what fit** |
| Front bulkhead | **Powerhobby aluminum** | The front is where bulkheads get loaded and where the plastic one gives up. On the FastAz this came bundled with the CF chassis kit; here it's the standalone part (~$36.99 on its own, [`chassis_analysis.md`](../FastAzJato4x4/chassis_analysis.md#bulkheads-front--rear)) |
| Centre brace | **Steel, VG-style** ($18.99) | **The Slash came with no brace**, so this was added, not replaced (the *Jato* OE brace is the one that breaks). ⚠️ **LCG only, won't fit HCG.** Cheaper pick is the **$6 plastic 9024**, see [`chassis_analysis.md`](chassis_analysis.md#chassis-bracing) |

> **The honest cheap route:** a plastic chassis plus one alloy front bulkhead covers the part that actually fails, without the carbon kit. It's also the pairing that makes [metal arms risky](../FastAzJato4x4/arm_analysis.md), FLM arms strip a *plastic* bulkhead. Full reasoning, and why this choice makes the [battery mounting](battery_mount_analysis.md) unique to this car, in [`chassis_analysis.md`](chassis_analysis.md).

---

## Drivetrain

| Position | Part |
|----------|------|
| Pinion | **11T 32P** |
| Spur | **54T** |

### Custom Axles (shared with FastAzJato4x4)

> **Bearings:** this car runs a **bare 10×18×5 in the hub**, which needed the **17mm hex adapters shaved down** to fit, not the hub carriers. The FastAz solves the same problem with a sleeve and a 10×15×4 instead, so only the hub position differs. Full list, costs and the route comparison in [`bearings_reference.md`](bearings_reference.md).

Both Jatos run **custom axles built from chopped E-Revo 1.0 CVDs**. Length is dialed on an **adjustable threaded prototype** first, then the **final axles are welded** to that length (simpler, tools on hand, a fresh set is cheap to remake). **Shorter axle = front.** Full build write-up and the rejected join methods are in [`FastAzJato4x4/driveshaft_analysis.md`](../FastAzJato4x4/driveshaft_analysis.md#shortening--joining-e-revo-cvds-custom-axles-wip).

### Diff Oil

> **This car is where the setup came from.** Mike's Jato was the first of the two, and the oils were tuned here together before the [FastAzJato4x4](../FastAzJato4x4/differential_analysis.md) inherited them. **The front and centre match on both cars, but the rear does not**, since this one is greased rather than oiled.

| Diff | Weight | Note |
|---|---|---|
| **Front** | **30k** (Traxxas TRA5136) | Calms torque steer on the heavy 4S car |
| **Center** | **100k** (Traxxas TRA5130) | Holds drive stability |
| **Rear** | **Blue grease, no oil** (Dynamite DYNE4201) | Drive off the corner. **Light coat, never packed**, see [`differential_analysis.md`](differential_analysis.md) |

---

## Batteries

> **Two docs:** [`battery_analysis.md`](battery_analysis.md) for the packs and the IR checks, [`battery_mount_analysis.md`](battery_mount_analysis.md) for the retainers, bar heights and max pack size.

⚠️ **Low-voltage cutoff: 3.5V per cell.** HV packs stay punchy right to the end, so nothing warns you that they're nearly done.

**Max pack 152 × 48 × 44mm**, full length 4S, soft or hard case. **Four packs run here**, the Gens Ace Redline 6300 and three CNHL, and **the HV ones are the better packs**. Prices are in [`BOM.md`](BOM.md#batteries). **Likely moving to hardcase** so grit stops chafing the soft packs.

---

## Wheels & Tires

| Item | Spec |
|---|---|
| **Rims** | **Traxxas 9070-WHT**, Jato 4x4 VXL 3.0" dished, 17 mm hex, white |
| **Foams** | **Blue race foams**, between the rim and the tire |
| **Tires** | **RedSpider** tires **mounted on the Traxxas Jato 4x4 rims** to widen the track |

> **Wide-track trick:** RedSpider tires mounted on the wider **Traxxas Jato 4x4 rims**, which pushes the wheels out and **widens the stance by a lot**. More stability and corner grip, at the cost of being **outside ROAR width**. The FastAz runs the same tire on standard rims to stay legal. Also note these take **~7 packs to wear in**. Full write-up in [`wheel_analysis.md`](wheel_analysis.md).

---

## Aero & Body

| Component | Part | Notes |
|-----------|------|-------|
| Body / shell | Traxxas Jato 4x4 body, green (exact SKU TBD) | $36.00, paid for by me, tracked in [`/LEDGER.md`](../../LEDGER.md), not here |

---

## Electronics

| Component | Part |
|-----------|------|
| Motor | **Castle Creations 1412 3200KV** |
| ESC | **Castle Mamba X SCT**, combo **010-0155-13** with the motor, $198.71. ⚠️ **4S max with this motor**, see [`esc_analysis.md`](esc_analysis.md) |

**Motor bearing service tracking:** bearings replaced ~2026-09-06, first run on them 2026-09-12. Tracked by weekend run count (no battery tracker for this car) in [`maintenance/README.md`](../../maintenance/README.md), the goal is catching the next replacement before they blow rather than after.

> Motor, gearing and the power-band finding are written up in [`motor_analysis.md`](motor_analysis.md).

---

## Tuning Notes

**Gearing for the power band, not the smallest pinion, is the finding.** It was reached at **12T**; the car has since come down to **11T**.

Original intuition was that **higher RPM** = better air control, so chasing the smallest pinion was the obvious move. Real-world finding: **torque matters as much as RPM**, gearing for the **power-band sweet spot** (12T here, not the tiniest pinion) makes mid-air corrections feel just as responsive as the high-RPM theory promised, *and* keeps the motor cooler because it's neither lugging nor screaming.

The on-track observations, the service tracking and the full write-up are in [`motor_analysis.md`](motor_analysis.md). It's also the empirical data point behind the FastAzJato4x4 pinion decision: pinion sizing is **not** purely a top-speed equation.

---

## Parts Purchased

| Date | Part | Qty | Total | Source |
|------|------|-----|-------|--------|
| 2026-09-07 | MonsterKingz / G-Maxx 7075 alloy hub set (front + rear) | 1 set | $50.00 | Bought off the [FastAzJato4x4](../FastAzJato4x4/hub_analysis.md) |
| 2026-05-19 | LIGHT HOUSE Aluminum Front C Hub/Knuckle Arm for Traxxas Jato 4x4 BL-2S (black) | 1 | $15.29 | AliExpress, LIGHT HOUSE 188527 Store |
| 2026-05-19 | LIGHT HOUSE Aluminum Front Hub/Knuckle Arm for Traxxas Jato 4x4 BL-2S (black) | 1 | $14.42 | AliExpress, LIGHT HOUSE 188527 Store |

> Both items shipped on the same order **#8210896333264866**, subtotal $29.71, paid **$24.67** ($5.04 off). Free returns within 90 days.

> Money Mike owes for parts (FLM arms, E-Revo CVD axle set) is tracked in [`/LEDGER.md`](../../LEDGER.md), not here.

---

## Analysis Docs

Each one is a summary of **what is fitted**, with a link out to the [FastAzJato4x4](../FastAzJato4x4/README.md) doc for the full comparison.

| | | | | |
|---|---|---|---|---|
| [Shocks](shock_analysis.md) | [Diffs](differential_analysis.md) | [ESC](esc_analysis.md) | [Chassis](chassis_analysis.md) | [BOM](BOM.md) |
| [Shock towers](shock_tower_analysis.md) | [Driveshafts](driveshaft_analysis.md) | [Motor](motor_analysis.md) | [Body & aero](aero_analysis.md) | [Bumpers](bumper_analysis.md) |
| [Arms](arm_analysis.md) | [Gearbox housings](gearbox_housing_analysis.md) | [Battery packs](battery_analysis.md) | [Wheels](wheel_analysis.md) | [Connectors](connector_reference.md) |
| [Swaybars](swaybar_analysis.md) | [17mm hexes](hub_analysis.md#17mm-wheel-hexes) | [Battery mounting](battery_mount_analysis.md) | [Bell crank](steering_bell_crank_analysis.md) | [Charger](charger_analysis.md) |
| [Hubs](hub_analysis.md) | [Bearings](bearings_reference.md) | [Radio](radio_analysis.md) | [Tie rods](tie_rod_analysis.md) | [Servo](servo_analysis.md) |

---

## TODO / Notes

- [x] Chassis confirmed: **Traxxas 7422 LCG + Powerhobby alloy front bulkhead + steel centre brace**
- [x] Electronics and drivetrain recorded: Mamba X SCT + 1412 combo, 11T/54T, TRA6855 centre shaft, stock housings
- [x] Arm setup confirmed against the FastAz: **FLM26800**, and the Slash-vs-Jato shock mount costs ~5mm of wheelbase
- [ ] Weigh the car (no all-up figure recorded yet)
- [ ] Add photos of the car itself, most shots here are of parts
