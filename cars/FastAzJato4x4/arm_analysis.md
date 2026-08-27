# Suspension Arm Selection — FastAzJato4x4

> **Chosen: FLM26800 metal arms front + rear.** FLM aluminum at both ends for stiffness and maximum impact resistance. ProTrac PRO6082-01 was the ideal rear on weight grounds (plastic, same ~10mm extension, no bulkhead stripping), but it's discontinued and now dropped, so FLM runs both ends. Metal arms normally transfer force to hinge pins and break other things, but these bend instead of snap, you pound them back into shape and you're still in the race. Extensively tested: lots of wrecks, sometimes bent, always reshaped and back on track. Makes the car feel super rigid, like a proper race car, at a fraction of buggy weight.

<p align="center">
  <a href="https://www.fastlanemachine.net/proddetail.php?prod=FLM26800"><img src="src/suspension_flm_rustler_rear_extended_arms_flm26800.jpg" width="600"></a><br>
  <em>FLM Extended Rear Arms FLM26800, $25.73/pair paid (bulk order), Made in USA</em>
</p>

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Arm Comparison](#arm-comparison) — 6 variants
- [Shock Guards](#shock-guards) — keeps debris out of drivetrain, crash protection
- [Price History](#price-history)
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Fits Slash 4x4 / Jato 4x4 hinge pin + mount geometry** | Must | Has to bolt to the chosen CF chassis bulkheads + accept stock-pattern hinge pins, ball studs, shock mount points |
| **Handles 4S 1/10–1/8 class loads** | Must | Hard landings on the 1/8-buggy-class Jato chassis stress arms more than typical 1/10 SCT use |
| **Doesn't shatter on impact** | Must | Arms breaking mid-run is a tow-back; need ductile failure (bend / crack progressively) not catastrophic snap |
| **Reasonable wheelbase / track width** | Must | Extended arms increase track width, affects body fit, drivetrain length (CVDs), and overall handling balance |
| **Stiff under cornering load** | May | Less arm flex = sharper steering response, but more flex = more impact compliance. Race vs basher trade |
| **Cheap / available** | May | Arms are top-3 most-broken parts on a hard-driven 4S build |
| **Front + rear both available** | May | Mixing-and-matching front vs rear from different vendors complicates geometry tuning |

---

## Arm Comparison

> *Spec format: Type · Material · Position · Fits · Wheelbase · Pivot/Hardware · Stiffness · Toe · Origin · Weight · Price*

| Arm | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **FLM26800** Extended track width, *front + rear* | **Type:** Extended track width, **3655-pattern arm stretched +~10mm**, run at **both ends** here. *Not* a stock Rustler arm: the Rustler 4x4 rear arm IS the stock TRA3655 (≈92mm), same as Slash 4x4. The FLM is 10mm past that.<br>**Material:** **6061 aluminum CNC**<br>**Position:** Front + rear (2 pairs)<br>**Fits:** Slash 4x4 / Stampede 4x4 / Rustler 4x4 / Rally / XO-1 / Jato 4x4 (shared TRA3655 arm pattern)<br>**Track width:** **101.6mm hole-to-hole vs 92mm stock TRA3655 (both measured) → +9.6mm/arm**<br>**Pivot/Hardware:** Adjustable width, extra shock positions<br>**Stiffness:** N/A<br>**Toe:** N/A<br>**Origin:** Made in USA<br>**Weight:** N/A<br>**Price:** **$25.73/pair paid** (bulk order, $40 list) | Pro: **Extends track width ~10mm per side**, increases droop by a large margin, massive handling improvement. Makes the Jato feel like a proper race car vs expensive buggies at a fraction of the weight. **Cost math: bend it back 3 times and you've already saved money over buying shorter stock arms that snap more often.** Bends instead of snaps, still in the race. Bending isn't common, reshapes to near-stock easily<br><br>Con: Metal arm trade-off knowingly accepted for the track width gains. **Strips the bulkhead only on a plastic one** — this car runs the aluminum front and rear bulkheads that ship with the CF chassis kit ([`chassis_analysis.md`](chassis_analysis.md#bulkheads-front--rear)), and [Mike's Jato](../Jato4x4_Mike/README.md) runs a metal one, so neither car is exposed to it. On a stock plastic bulkhead it's a real cost. Hard hits now break **only the RPM rod ends**, which is the cheap end of the link on purpose — all 6 links run ACER titanium M4x60 turnbuckles with RPM long rod ends, so the ~$0.70 plastic gives way instead of the rod, the hub or the bulkhead ([`tie_rod_analysis.md`](tie_rod_analysis.md)). **Also forces longer axles** — nothing off the shelf reaches +10mm per side, so this runs the **custom combo axle**: knock-off Slash 4x4 CV bodies with **TRA6752 long output shafts at the front only**, Tekno TKR1654-17 front stubs and the TKR5570-17 SCT410 rear kit ([`driveshaft_analysis.md`](driveshaft_analysis.md#axle-wheel-driveshaft-comparison)). Chopped and rejoined E-Revo 1.0 CVDs are the fallback, not the build | <a href="https://www.fastlanemachine.net/proddetail.php?prod=FLM26800"><img src="src/suspension_flm_rustler_rear_extended_arms_flm26800.jpg" width="500"></a> |
| 🚫 ~~**PRO6082-01** ProTrac extended track width~~, *dropped, discontinued* | **Type:** Extended track width<br>**Material:** Nylon<br>**Position:** Front + rear set<br>**Fits:** Slash 4x4 / Jato 4x4 pattern<br>**Track width:** **+~10mm/arm**<br>**Pivot/Hardware:** N/A<br>**Stiffness:** N/A<br>**Toe:** N/A<br>**Origin:** N/A<br>**Weight:** N/A<br>**Price:** $13.75 | Pro: Would have been the **ideal rear arm** on weight, same track width extension as FLM, rear sees less stress so plastic is fine. No bulkhead stripping — though that only counts on a plastic bulkhead, and this car has aluminum ones<br><br>Con: **Discontinued and now dropped**, couldn't source it, so FLM runs both ends. Snaps on hard hits rather than bending back. **Would have needed the same longer axles** — the +10mm forces them, not the arm material, so this was never the cheaper path it looks like ([`driveshaft_analysis.md`](driveshaft_analysis.md#axle-wheel-driveshaft-comparison)) | <img src="src/suspension_proline_protrac_arms_pro6082-01.jpg" width="500"> |
| 🔵 **TRA3655X** Standard track width OEM | **Type:** Standard track width<br>**Material:** Hardened plastic<br>**Position:** Front or rear<br>**Fits:** Slash 4x4 / Jato 4x4 pattern<br>**Track width:** Standard<br>**Pivot/Hardware:** N/A<br>**Stiffness:** N/A<br>**Toe:** N/A<br>**Origin:** N/A<br>**Weight:** N/A<br>**Price:** $10 | Pro: **2nd stiffest overall, the stiffest plastic arm** (only the FLM aluminum beats it). **Will never go out of stock**, knock-offs from Remohobby, Hanqui 727 feel and last the same as OEM. Effectively unlimited supply. Works front and rear<br><br>Con: Brittle nylon snaps on hard hits. No track width extension | <img src="src/suspension_traxxas_slash4x4_oem_arms_tra3655x.jpg" width="500"> |
| 🔵 **TRA3655-BLK** Standard track width HD | **Type:** Standard track width<br>**Material:** HD composite<br>**Position:** Front or rear<br>**Fits:** Slash 4x4 / Jato 4x4 pattern<br>**Track width:** Standard<br>**Pivot/Hardware:** N/A<br>**Stiffness:** N/A<br>**Toe:** N/A<br>**Origin:** N/A<br>**Weight:** N/A<br>**Price:** $12 | Pro: In-stock successor to TRA3655R. Available in multiple colors<br><br>Con: **Middle ground flex**, flexier than TRA3655X, stiffer than RPM. No track width extension | <img src="src/suspension_traxxas_hd_arms_tra3655-blk.jpg" width="500"> |
| 🔵 **TRA3655** Standard track width original | **Type:** Standard track width<br>**Material:** Original nylon<br>**Position:** Front or rear<br>**Fits:** Slash 4x4 / Jato 4x4 pattern<br>**Track width:** Standard<br>**Pivot/Hardware:** N/A<br>**Stiffness:** N/A<br>**Toe:** N/A<br>**Origin:** N/A<br>**Weight:** N/A<br>**Price:** $9.99 | Pro: **Stiff plastic, just behind the TRA3655X.** Still a solid choice for a standard Slash race build, still physically available<br><br>Con: Harder to source, discontinued at AMain. No track width extension | <img src="src/suspension_traxxas_oem_original_arms_tra3655.jpg" width="500"> |
| 🚫 ~~**TRA3655R** Standard track width HD~~ | **Type:** Standard track width<br>**Material:** HD composite<br>**Position:** Front or rear<br>**Fits:** Slash 4x4 / Jato 4x4 pattern<br>**Track width:** Standard<br>**Pivot/Hardware:** N/A<br>**Stiffness:** N/A<br>**Toe:** N/A<br>**Origin:** N/A<br>**Weight:** N/A<br>**Price:** $12 | Pro: Flexes instead of snapping, works cold weather<br><br>Con: **Discontinued online**, AMain lists as discontinued. No track width extension | <img src="src/suspension_traxxas_slash4x4_hd_arms_tra3655r.jpg" width="500"> |
| ❌ ~~**RPM80702** Standard track width~~ | **Type:** Standard track width<br>**Material:** Flexible nylon<br>**Position:** Front or rear<br>**Fits:** Slash 4x4 / Jato 4x4 pattern<br>**Track width:** Standard<br>**Pivot/Hardware:** N/A<br>**Stiffness:** N/A<br>**Toe:** N/A<br>**Origin:** N/A<br>**Weight:** N/A<br>**Price:** N/A | Pro: Great for bashing, won't break<br><br>Con: **Most flexible**, flex transfers load into driveshafts, and only the thickest CVDs survive that. **Warps from just sitting in storage**, unacceptable for racing | <img src="src/suspension_rpm_arms_rpm80702.jpg" width="500"> |

---

## Shock Guards

Plastic guards that mount around the arm / drivetrain area. Keep dirt, grass, and debris out of the driveshafts mid-run, and provide light crash protection on the lower chassis. Lightweight, the main value is protection, not structure.

> *Spec format: Part · Material · Position · Fits · Weight · Price*

| Guard | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **TRA6732** Front Arm Guards | **Part:** TRA6732<br>**Material:** Composite, lightweight<br>**Position:** Front<br>**Fits:** Slash 4x4 (listed for Stampede 4x4); also RPM arms<br>**Weight:** N/A<br>**Price:** **$9.95** | Pro: **No front bumper on this build, front shocks and arms are exposed. These are essential.** Protects shocks and arms from frontal impacts, including accidental contact with other cars on track. Shields against debris kicked up by the car in front. Keeps grass out of driveshafts. Includes all hardware<br><br>Con: Adds a tiny amount of weight, negligible in practice since it's plastic | <a href="https://www.amazon.com/dp/B00FIIWV9I"><img src="src/suspension_traxxas_arm_guards_tra6732.jpg" width="500"></a> |
| ⭐ **TRA6733** Rear Arm Guards | **Part:** TRA6733<br>**Material:** Composite<br>**Position:** Rear<br>**Fits:** Slash 4x4 / Jato 4x4 pattern<br>**Weight:** N/A<br>**Price:** **$7.00** | Pro: Same composite construction as front. Shields rear driveline from dirt and rocks being thrown up into it. In stock at HobbyTown<br><br>Con: Adds a tiny amount of weight, negligible in practice since it's plastic | <img src="src/suspension_traxxas_arm_guards_rear_tra6733.jpg" width="500"> |

---

## Price History

| Date | Price | Discount Path | Notes |
|---|---|---|---|
| 2026-07-02 | **$25.73/pair** ✅ **purchased** | **FLM July 1st sale, 25% off** ($30→$22.50/pair before shipping). Bulk order, 4 pairs, $120 subtotal − $30 discount + $12.90 shipping = $102.90 total | Order #4658, direct from FLM. 1 of the 4 pairs went to [Mike's Jato 4x4](../Jato4x4_Mike/README.md) (tracked in [`/LEDGER.md`](../../LEDGER.md#mike--running-account), not here); remainder is this build's front (+ spares). **Annual sale, see [`Deals/flm_july_sale_2026.md`](../../Deals/flm_july_sale_2026.md), check again next July.** |

---

## Notes
- **Track width, not wheelbase.** Longer suspension arms move the wheel *outboard*, which is track width. Wheelbase is front axle to rear axle and no arm changes it — that takes moving the bulkheads. The giveaway is that the FLM gain is quoted **per side**, which is a track measurement, and the clincher is the [longer axles](driveshaft_analysis.md#axle-wheel-driveshaft-comparison): driveshaft length is set by diff outdrive to hub, a lateral distance, so a genuine wheelbase change would need no new axles at all. **This applies to any +10mm track arm, not just the FLM** — the axles follow the track width, whatever brand of arm creates it.


- **OEM vs EHD trade**: stiffer = more precise but more breakable; flexier = more durable but slightly vaguer steering feel. The classic plastic-formulation trade-off, same physics as the [shock tower aluminum-vs-composite discussion](shock_tower_analysis.md#material-properties-reference) but with two flavors of plastic instead of two materials.
- **Arms as the intended fuse:** on this build the design intent is that **arms give way first**, before the chassis or other expensive parts. The FLM extended arms (bendable, reshape-able) are perfect for that role, they take the hit, get bent back close to spec, and the car keeps driving. The CF chassis and the rest of the drivetrain are protected by the arms acting as the sacrificial layer. See [`chassis_analysis.md`](chassis_analysis.md#notes) for how this informs the chassis durability expectation and [`bumper_analysis.md`](bumper_analysis.md#notes) for why the minimal-bumper choice is acceptable given this hierarchy.
- **Measured hole-to-hole length** (inner hinge pin to outer pivot, caliper):
  - **TRA2555 / 2555X** (Slash 2WD rear) = **84mm**
  - **TRA3655 / 3655X** (all 4x4 + Rustler/Stampede 2WD rear) = **92mm** (+8mm)
  - **RPM80702** = **92mm** (stock-length, matches 3655)
  - **FLM26800** (extended) = **101.6mm** (+9.6mm over 3655)
  - Note: published part specs (3655 = 100mm, 2555 = 92mm) are *overall* length, not these hole-to-hole figures. The 3655 is the longest stock arm in this pattern; FLM is the only longer option.
- **Flex stiffness hierarchy** (stiffest to most flexible): FLM26800 aluminum → **TRA3655X OEM (stiffest plastic, 2nd overall)** → TRA3655 original (discontinued) → TRA3655-BLK HD → RPM (vetoed, warps from storage).
- **Front-rear matching**: keep front and rear arms in the same family / generation if possible. Mixing stock-length OEM front with FLM extended rear changes geometry intentionally; mixing stiff fronts with flex rears unintentionally couples handling feel to terrain in ways that are hard to tune out.
- **CVD compatibility**: the chosen Slash 4x4-pattern CVDs (knock-off + Tekno M6 stubs, see [`driveshaft_analysis.md`](driveshaft_analysis.md)) may be too short for the **FLM extended arm (101.6mm hole-to-hole)** vs 92mm stock TRA3655, which widens the track ~10mm/side, verify at test-fit. The old E-Revo CVD chop-to-90.5mm build (now a fallback, see [Measured lengths](driveshaft_analysis.md#measured-lengths-prototype)) was sized for this same track width if that path is ever revisited.

