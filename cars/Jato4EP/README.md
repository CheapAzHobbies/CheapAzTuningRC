<div align="center">

# T H E · 4 E P · G A Z E T T E

**JATO 4×4 EXPERIMENTAL PROTOTYPE** · OWNER: MICHEAL RITCHIE · PRINTED ON THE BENCH SINCE 2026

`VOL. I . . . . . No. 1 . . . . . THURSDAY, SEPTEMBER 17, 2026 . . . . . PRICE 25¢`

</div>

---

<div align="center">

## SLASH DONOR REBUILT TO JATO SPEC; RIVAL CAR BORN ON SAME BENCH

### *Towers, shocks and a wing were all it took · Faster car followed, but this one came first*

<sub><b>BY THE GARAGE DESK</b> · Special to the CheapAz Tuning Wire</sub>

</div>

> **Jato 4EP, the Jato 4×4 Experimental Prototype.** Owned and driven by **Micheal Ritchie**, and the bench the [Jato 4SS](../Jato4SS/README.md) was developed on (that build is co-developed with him). The name is the job: this is where a setting gets tried before it is trusted. Setup notes recorded here for reference and cross-build tuning.

---

<div align="center">

**· INSIDE THIS ISSUE ·**

| Page | Section | The story |
|:---|:---|:---|
| **A1** | [Car Overview](#car-overview) | Slash donor, Jato spec, and why this one is the original |
| **A2** | [Suspension](#suspension) | Oils and pistons, tuned here first |
| **A3** | [Steering](#steering) | An alloy knuckle on a plastic C-hub, and the part that broke |
| **A4** | [Chassis](#chassis) | Plastic and proud, with one alloy bulkhead |
| **B1** | [Drivetrain](#drivetrain) | Shared axles, greased rear diff |
| **B2** | [Batteries](#batteries) | Four packs, and the cutoff that matters |
| **B3** | [Wheels & Tires](#wheels--tires) | The wide-track trick |
| **B4** | [Aero & Body](#aero--body) | Green, and billed elsewhere |
| **C1** | [Electronics](#electronics) | Castle combo and the bearing count |
| **C2** | [Tuning Notes](#tuning-notes) | **OPINION:** the pinion finding |
| **D1** | [Parts Purchased](#parts-purchased) | Classifieds |
| **D2** | [Analysis Docs](#analysis-docs) | Our regular columns |
| **D3** | [TODO / Notes](#todo--notes) | Coming next issue |

</div>

---

<div align="center"><sub><b>PAGE A1</b> · THE FRONT PAGE</sub></div>

## Car Overview

**Base Car:** started as a **running Traxxas Slash 4x4**, built up to Jato 4x4 spec.

> **This is the car the [Jato 4SS](../Jato4SS/README.md) was born out of.** Mike's Jato came first and the R&D happened here: the diff and shock oils, the pistons and the custom axle build were all worked out on this car, together, and the 4SS inherited the answers. So where the two docs agree, **this is the origin and that one is the copy**, worth knowing when the settings look identical.
>
> The two have since diverged. This car keeps the **plastic chassis**, runs **different hubs**, and solves the hub-bearing problem the opposite way (bigger bearing, shaved hexes, rather than a sleeve). Those differences are the interesting part and are called out section by section below.
>
> **On the Slash vs Jato question: it started as a running Slash 4x4**, and that origin is the build. **The two are the same platform**, so the donor carries straight over. What makes it a Jato 4x4 is the **towers, shocks and wing**, which are the parts that actually differ between them. Anyone pricing this build should start from a running Slash 4x4 and budget those three.

---

<div align="center"><sub><b>PAGE A2</b> · SUSPENSION DESK</sub></div>

## Suspension

### Shock Oil

<div align="center">

| Position | Weight |
|:---|:---|
| Front | **37.5wt** (Losi TLR74030, 468 cSt) |
| Rear | **50wt** (Associated 5480 FT, 650 cSt) |

</div>

> **Same spec as the [Jato 4SS](../Jato4SS/shock_analysis.md#setup-spec-springs--pistons--oil), and this car is where it was arrived at**, the two were tuned together, starting here. Rear heavier than front because the motor sits at the back and the car is tail-heavy for a 1/8.
>
> 🔧 **If the rear packs, drop it to 47.5wt** (Associated FT, 613 cSt), one small step down from the 50wt in it now. This car's rear piston is the more restrictive **6 × 1.2**, so it is likelier to pack than the 4SS. See [`shock_analysis.md`](shock_analysis.md#if-the-rear-packs).

### Pistons

<div align="center">

| Position | Piston |
|:---|:---|
| Front | 6 hole × 1.4 |
| Rear | 6 hole × 1.2 |

</div>

---

<div align="center"><sub><b>PAGE A3</b> · STEERING DESK</sub></div>

## Steering

<div align="center"><sub><i>"IT DIDN'T FAIL STOCK" · Filed hinge pocket blamed in C-hub failure</i></sub></div>

<div align="center">

| Component | Part | Weight (pair) |
|:---|:---|:---|
| Front C-Hub / Caster Block | **Stock plastic EHD**, running now | N/A |
| Front Steering Block / Knuckle | **MonsterKingz alloy**, running now | N/A |
| Rear Hub Carriers | **Stock plastic EHD**, running now. **Plan: swap to a shaved-down MonsterKingz rear hub** for the slim Raptor R look at a lower price | N/A |
| ~~LIGHT HOUSE Aluminum Front C Hub/Knuckle Arm~~ (black) | **Broke**, retired | 25.5 g bare · 36.4 g w/ hardware |
| ~~LIGHT HOUSE Aluminum Front Hub/Knuckle Arm~~ (black) | **Broke**, retired | 22.4 g bare · 34.9 g w/ hardware |

</div>

> **Why the change:** the Lighthouse front C-hub and carrier broke, so Mike moved onto a **MonsterKingz metal set bought off the Jato 4SS for $50** (2026-09-07). **It didn't fail stock**, he'd filed the hinge pocket for droop. Full write-up, the measured Lighthouse weights and the planned rear shave are all in [`hub_analysis.md`](hub_analysis.md). The **shaved 17mm hexes** now live with the stubs that gate them, in [`driveshaft_analysis.md`](driveshaft_analysis.md#17mm-wheel-hexes).

---

<div align="center"><sub><b>PAGE A4</b> · CHASSIS DESK</sub></div>

## Chassis

<div align="center">

| Component | Part | Notes |
|:---|:---|:---|
| Chassis | **Traxxas 7422 LCG plastic** ($20) | **The big divergence from the [Jato 4SS](../Jato4SS/chassis_analysis.md), which went carbon fiber.** Plastic flexes rather than cracking. ⚠️ **It's the LCG chassis, so LCG-only parts are what fit** |
| Front bulkhead | **Powerhobby aluminum** | The front is where bulkheads get loaded and where the plastic one gives up. On the 4SS this came bundled with the CF chassis kit; here it's the standalone part (~$36.99 on its own, [`chassis_analysis.md`](../Jato4SS/chassis_analysis.md#bulkheads-front--rear)) |
| Centre brace | **Steel, VG-style** ($18.99) | **The Slash came with no brace**, so this was added, not replaced (the *Jato* OE brace is the one that breaks). ⚠️ **LCG only, won't fit HCG.** Cheaper pick is the **$6 plastic 9024**, see [`chassis_analysis.md`](chassis_analysis.md#chassis-bracing) |

</div>

> **The honest cheap route:** a plastic chassis plus one alloy front bulkhead covers the part that actually fails, without the carbon kit. It's also the pairing that makes [metal arms risky](../Jato4SS/arm_analysis.md), FLM arms strip a *plastic* bulkhead. Full reasoning, and why this choice makes the [battery mounting](battery_mount_analysis.md) unique to this car, in [`chassis_analysis.md`](chassis_analysis.md).

---

<div align="center"><sub><b>PAGE B1</b> · DRIVETRAIN DESK</sub></div>

## Drivetrain

<div align="center">

| Position | Part |
|:---|:---|
| Pinion | **11T 32P** |
| Spur | **54T** |

</div>

### Custom Axles (shared with Jato 4SS)

> **Bearings:** this car runs a **bare 10×18×5 in the hub**, which needed the **17mm hex adapters shaved down** to fit, not the hub carriers. The 4SS solves the same problem with a sleeve and a 10×15×4 instead, so only the hub position differs. Full list, costs and the route comparison in [`bearings_reference.md`](bearings_reference.md).

Both Jatos run the same **knock-off Slash / Jato 4x4 HD steel CV driveshafts** (TRA6851R + TRA6852R clones) on **TRA6752 long output shafts at all four corners**, with **Tekno stubs**. **The axles are basically the Jato 4x4 part**, so they bolt straight in with **no cutting, welding or joining**. Full assembly and costs in [`Jato4SS/driveshaft_analysis.md`](../Jato4SS/driveshaft_analysis.md#2wd-long-cvds--6752-output-shafts-cheap-long-axle-build).

### Diff Oil

> **This car is where the setup came from.** Mike's Jato was the first of the two, and the oils were tuned here together before the [Jato 4SS](../Jato4SS/differential_analysis.md) inherited them. **The front and centre match on both cars, but the rear does not**, since this one is greased rather than oiled.

<div align="center">

| Diff | Weight | Note |
|:---|:---|:---|
| **Front** | **30k** (Traxxas TRA5136) | Calms torque steer on the heavy 4S car |
| **Center** | **100k** (Traxxas TRA5130) | Holds drive stability |
| **Rear** | **Blue grease, no oil** (Dynamite DYNE4201) | Drive off the corner. **Light coat, never packed**, see [`differential_analysis.md`](differential_analysis.md) |

</div>

---

<div align="center"><sub><b>PAGE B2</b> · POWER DESK</sub></div>

## Batteries

> **Two docs:** [`battery_analysis.md`](battery_analysis.md) for the packs and the IR checks, [`battery_mount_analysis.md`](battery_mount_analysis.md) for the retainers, bar heights and max pack size.

⚠️ **Low-voltage cutoff: 3.5V per cell.** HV packs stay punchy right to the end, so nothing warns you that they're nearly done.

**Max pack 152 × 48 × 44mm**, full length 4S, soft or hard case. **Four packs run here**, the Gens Ace Redline 6300 and three CNHL, and **the HV ones are the better packs**. Prices are in [`BOM.md`](BOM.md#batteries). **Likely moving to hardcase** so grit stops chafing the soft packs.

---

<div align="center"><sub><b>PAGE B3</b> · TIRE DESK</sub></div>

## Wheels & Tires

<div align="center">

| Item | Spec |
|:---|:---|
| **Rims** | **Traxxas 9070-WHT**, Jato 4x4 VXL 3.0" dished, 17 mm hex, white |
| **Foams** | **Blue race foams**, between the rim and the tire |
| **Tires** | **RedSpider** tires **mounted on the Traxxas Jato 4x4 rims** to widen the track |

</div>

> **Wide-track trick:** RedSpider tires mounted on the wider **Traxxas Jato 4x4 rims**, which pushes the wheels out and **widens the stance by a lot**. More stability and corner grip, at the cost of being **outside ROAR width**. The 4SS runs the same tire on standard rims to stay legal. Also note these take **~7 packs to wear in**. Full write-up in [`wheel_analysis.md`](wheel_analysis.md).

---

<div align="center"><sub><b>PAGE B4</b> · BODY SHOP</sub></div>

## Aero & Body

<div align="center">

| Component | Part | Notes |
|:---|:---|:---|
| Body / shell | Traxxas Jato 4x4 body, green (exact SKU TBD) | $36.00, paid for by me, tracked in [`/LEDGER.md`](../../LEDGER.md), not here |

</div>

---

<div align="center"><sub><b>PAGE C1</b> · ELECTRONICS DESK</sub></div>

## Electronics

<div align="center">

| Component | Part |
|:---|:---|
| Motor | **Castle Creations 1412 3200KV** |
| ESC | **Castle Mamba X SCT**, combo **010-0155-13** with the motor, $198.71. ⚠️ **4S max with this motor**, see [`esc_motor_analysis.md`](esc_motor_analysis.md) |

</div>

**Motor bearing service tracking:** bearings replaced ~2026-09-06, first run on them 2026-09-12, **4 battery packs run since**. Running **S605ZZ 5×14×5 ABEC-9** rather than the stock bearings, which work but burn up quickly ([`bearings_reference.md`](bearings_reference.md#the-motor-bearing-s605zz)). Counted by packs in [`maintenance/README.md`](../../maintenance/README.md), the goal is catching the next replacement before they blow rather than after.

> Motor, gearing and the power-band finding are written up in [`esc_motor_analysis.md`](esc_motor_analysis.md). **EC5 is the main battery connection**, with everything fitted listed in [`connector_reference.md`](connector_reference.md).

---

<div align="center"><sub><b>PAGE C2</b> · OPINION</sub></div>

## Tuning Notes

<div align="center"><sub><i>FROM THE DRIVER'S SEAT · The smallest pinion was the wrong target all along</i></sub></div>

**Gearing for the power band, not the smallest pinion, is the finding.** It was reached at **12T**; the car has since come down to **11T**.

Original intuition was that **higher RPM** = better air control, so chasing the smallest pinion was the obvious move. Real-world finding: **torque matters as much as RPM**, gearing for the **power-band sweet spot** (12T here, not the tiniest pinion) makes mid-air corrections feel just as responsive as the high-RPM theory promised, *and* keeps the motor cooler because it's neither lugging nor screaming.

The on-track observations, the service tracking and the full write-up are in [`esc_motor_analysis.md`](esc_motor_analysis.md). It's also the empirical data point behind the Jato 4SS pinion decision: pinion sizing is **not** purely a top-speed equation.

---

<div align="center"><sub><b>PAGE D1</b> · CLASSIFIEDS</sub></div>

## Parts Purchased

<div align="center">

| Date | Part | Qty | Total | Source |
|:---|:---|:---|:---|:---|
| 2026-09-07 | MonsterKingz / G-Maxx 7075 alloy hub set (front + rear) | 1 set | $50.00 | Bought off the [Jato 4SS](../Jato4SS/hub_analysis.md) |
| 2026-05-19 | LIGHT HOUSE Aluminum Front C Hub/Knuckle Arm for Traxxas Jato 4x4 BL-2S (black) | 1 | $15.29 | AliExpress, LIGHT HOUSE 188527 Store |
| 2026-05-19 | LIGHT HOUSE Aluminum Front Hub/Knuckle Arm for Traxxas Jato 4x4 BL-2S (black) | 1 | $14.42 | AliExpress, LIGHT HOUSE 188527 Store |

</div>

> Both items shipped on the same order **#8210896333264866**, subtotal $29.71, paid **$24.67** ($5.04 off). Free returns within 90 days.

> Money Mike owes for parts (FLM arms, E-Revo CVD axle set) is tracked in [`/LEDGER.md`](../../LEDGER.md), not here.

---

<div align="center"><sub><b>PAGE D2</b> · OUR REGULAR COLUMNS</sub></div>

## Analysis Docs

Each one is a summary of **what is fitted**, with a link out to the [Jato 4SS](../Jato4SS/README.md) doc for the full comparison.

<div align="center">

| | | | | |
|:---|:---|:---|:---|:---|
| [Shocks](shock_analysis.md) | [Diffs](differential_analysis.md) | [ESC, motor & gearing](esc_motor_analysis.md) | [Chassis](chassis_analysis.md) | [BOM](BOM.md) |
| [Shock towers](shock_tower_analysis.md) | [Driveshafts](driveshaft_analysis.md) | — | [Body & aero](aero_analysis.md) | [Bumpers](bumper_analysis.md) |
| [Arms](arm_analysis.md) | [Gearbox housings](gearbox_housing_analysis.md) | [Battery packs](battery_analysis.md) | [Wheels](wheel_analysis.md) | [Connectors](connector_reference.md) |
| — | [17mm hexes](driveshaft_analysis.md#17mm-wheel-hexes) | [Battery mounting](battery_mount_analysis.md) | [Bell crank](steering_bell_crank_analysis.md) | [Charger](charger_analysis.md) |
| [Hubs](hub_analysis.md) | [Bearings](bearings_reference.md) | [Radio](radio_analysis.md) | [Tie rods](tie_rod_analysis.md) | [Servo](servo_analysis.md) |

</div>

---

<div align="center"><sub><b>PAGE D3</b> · COMING IN NEXT WEEK'S EDITION</sub></div>

## TODO / Notes

- [x] Chassis confirmed: **Traxxas 7422 LCG + Powerhobby alloy front bulkhead + steel centre brace**
- [x] Electronics and drivetrain recorded: Mamba X SCT + 1412 combo, 11T/54T, TRA6855 centre shaft, stock housings
- [x] Arm setup confirmed against the 4SS: **FLM26800**, and the Slash-vs-Jato shock mount costs ~5mm of wheelbase
- [ ] Weigh the car (no all-up figure recorded yet)
- [ ] Add photos of the car itself, most shots here are of parts

---

<div align="center">

<sub><b>THE 4EP GAZETTE</b> · Published irregularly from the bench · All prices as paid, all weights as measured<br>
Sister publication: <a href="../Jato4SS/README.md">The 4SS Jato 4x4</a> · Accounts settled in the <a href="../../LEDGER.md">LEDGER</a></sub>

</div>
