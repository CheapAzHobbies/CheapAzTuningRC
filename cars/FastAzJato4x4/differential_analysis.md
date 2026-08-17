# Differential Selection — FastAzJato4x4

> **Chosen:**
> - **Front & rear diffs: AliExpress knock-off Slash 4x4 steel diffs (5mm), ~$15.26 for the pair.** Strong steel, come assembled with the I-bar brace, and 5mm matches the **Slash 4x4-pattern CVDs on Tekno M6 stubs** (see [`driveshaft_analysis.md`](driveshaft_analysis.md)). The stock Jato 4x4 diff is the native-fit fallback; the 6mm E-Revo 1.0 diffs (owned) are spares.
> - **Center diff: AliExpress metal center diff (~$20), comes pre-filled with the correct oil.** Fully assembled, and its **integrated steel 54T spur is the build's spur** (no separate spur to fit). The lighter TRA6814 plastic is the alternative.
> - **Spur gear: the integrated steel 54T spur on the AliExpress center diff.**

<p align="center"><img src="src/drivetrain_aliexpress_knockoff_slash4x4_steel_diff.png" height="240">&nbsp;<img src="src/drivetrain_aliexpress_center_diff_alum_steel.jpg" height="240"><br><em>The chosen drivetrain: AliExpress knock-off Slash 4x4 steel front/rear diff (5mm, I-bar) · AliExpress metal center diff (integrated steel 54T spur)</em></p>

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Front & Rear Diff Comparison](#front--rear-diff-comparison)
- [Alternative Upgrade Parts](#alternative-upgrade-parts)
- [Center Diff](#center-diff)
- [Center Diff Oil](#center-diff-oil)
- [Front & Rear Diff Oil](#front--rear-diff-oil)
- [Spur Gear](#spur-gear)
- [Sources](#sources)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **5mm outdrives (stock Jato 4x4 / Slash 4x4)** | Must | Must match the **Slash 4x4-pattern CVDs / Tekno M6 stub axle build** we're actually running (see [`driveshaft_analysis.md`](driveshaft_analysis.md)), not the E-Revo 6mm cups |
| **Fits Jato 4x4 gearbox housing** | Must | Has to physically bolt up to the chassis mounts |
| **Sealed for oil** | Must | Tunable damping via diff oil viscosity |
| **Field-rebuildable** | May | Diff service is routine; being able to rebuild it myself beats throw-and-replace |
| **Reasonably available / cheap** | May | Diffs are wear items; replacements should be easy to source |

---

## Front & Rear Diff Comparison

> *Spec format: Outdrive · Housing · Internals · Part · Fits · Price*

| Diff | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **AliExpress knock-off Slash 4x4 steel diff (RS RC Store)** — *chosen, front + rear* | **Outdrive:** **5mm** (Slash 4x4 pattern)<br>**Housing:** Steel<br>**Internals:** typically **comes built with the I-bar** spider-gear brace (not guaranteed every batch, but not a dealbreaker if absent)<br>**Part:** N/A (generic; rebuild gear set 6882/5379, ~$7.68)<br>**Fits:** Slash 4x4 VXL / Stampede / Rustler / Remo HQ727 (5mm)<br>**Price:** **$15.26 / 2** (2-pack coupon; $9.22 for 1). 🚧 confirm in hand (screenshot on PC) | Pro: **Strong steel, dirt cheap, 5mm matches the axle build, and it comes assembled with the I-bar.** Two (front + rear) for ~$15, cheaper than the stock Jato diff and stronger<br><br>Con: Generic AliExpress QC / availability (sale ends). No warranty. Confirm the I-bar is there on arrival | <img src="src/drivetrain_aliexpress_knockoff_slash4x4_steel_diff.png" width="500"> |
| 🟢 **Traxxas E-Revo 1.0 diffs** — *in hand, now spares* | **Outdrive:** **6mm**<br>**Housing:** Plastic<br>**Internals:** I-bar spider gear braces stock<br>**Part:** Assembled TRA5380; ring gear TRA5379X; carrier rebuild TRA3978; gear set rebuild TRA5382X<br>**Fits:** Jato 4x4 gearbox (minor fitting)<br>**Price:** **~$14.97** assembled (Jenny's RC, cheapest complete diff); already owned, $0 sunk | Pro: Cheap, easy to maintain, I-bar spider gear braces stock. **Plastic housing outlasts aluminum.** Front and rear are identical parts. GPM ER1200TS is the aftermarket ring-gear replacement<br><br>Con: **Wrong outdrive for the current axle plan**, the build moved to 5mm Slash 4x4-pattern CVDs, so these drop to spares/fallback unless the axle plan moves back to 6mm E-Revo CVDs. Heavier than stock Jato diffs; requires minor fitting to the Jato gearbox housing. **Must fill half full only**, overfilling plastic diff housings causes them to explode under pressure | <img src="src/drivetrain_traxxas_e_revo_diff_assembled_tra5379x.jpg" width="500"><br><img src="src/drivetrain_traxxas_diff_carrier_housing_tra3978.jpg" width="500">&nbsp;<img src="src/drivetrain_traxxas_e_revo_diff_gear_set_tra5382x.jpg" width="500"><br><em>assembled · TRA3978 carrier housing · TRA5382X gear set</em> |
| 🥈 **Traxxas Jato 4x4 stock diffs** — *native-fit fallback* | **Outdrive:** **5mm**<br>**Housing:** Plastic<br>**Internals:** TRA6882 gear set (same as XO-1); ring gear TRA6879<br>**Part:** assembled Jato 4x4 diff (part # TBD 🚧); rebuild = TRA6882 gear set + TRA6879 ring gear<br>**Fits:** Native Jato 4x4 / Slash 4x4<br>**Price:** ~$12.97 assembled (Jato 4x4, Jenny's RC, 5 in stock) | Pro: **Native 5mm fit, no gearbox-housing fitting, in stock.** Same TRA6882 gear set as XO-1. The safe fallback if the AliExpress steel diff has QC problems<br><br>Con: Plastic, and pricier than the AliExpress steel 2-pack. Same TRA6882 internals as XO-1, no real upgrade | <img src="src/drivetrain_traxxas_jato_4x4_stock_diff.jpg" width="500"> |
| 🚫 ~~**Wltoys K939 diffs (E-Revo knock-off)**~~ | **Outdrive:** **6mm** (E-Revo compatible)<br>**Housing:** Plastic<br>**Internals:** I-bar spider gear braces included<br>**Part:** TBD, K939 specific (K939 spare parts listings)<br>**Fits:** E-Revo / Jato 4x4 drivetrain<br>**Price:** N/A | Pro: E-Revo diff knock-off, 6mm outdrives, same I-bar internals as the E-Revo. Surprisingly includes the I-bar for a budget knock-off<br><br>Con: **Wrong outdrive now.** Was the budget option for the 6mm E-Revo CVD plan; the axle plan moved to 5mm, so this no longer applies here | <img src="src/drivetrain_traxxas_e_revo_diff_assembled_tra5379x.jpg" width="500"> |
| 🚫 ~~**Traxxas XO-1 diffs**~~ | **Outdrive:** **5mm**<br>**Housing:** TRA3978 carrier ($4.25, same heavy-duty housing shared with E-Revo)<br>**Internals:** TRA6882 I-bar spider gear set; ring gear TRA6879 / TRA5379X<br>**Part:** TRA3978 carrier + TRA6882 gear set<br>**Fits:** XO-1 pattern<br>**Price:** ~$29.99 assembled (Jenny's RC, out of stock) | Pro: 5mm outdrive now matches the axle plan. Uses same TRA3978 carrier as E-Revo. I-bar gear set (TRA6882) is strong<br><br>Con: $29.99 and out of stock vs the native Jato 4x4 stock diff at $12.97, in stock, with the same TRA6882 gear set. No reason to source XO-1 parts when the Jato diff is cheaper and already available | <img src="src/drivetrain_traxxas_xo1_diff_jennys_rc.jpg" width="500"><br><img src="src/drivetrain_traxxas_xo1_diff_diagram.jpg" width="500"><br><img src="src/drivetrain_traxxas_xo1_spider_gear_set.jpg" width="500"><br><em>Jenny's RC listing · diff housing TRA3978 · spider gear set w/ I-bar</em> |
| 🚫 ~~**GPM SLA1337FR, Slash 4x4 / Jato 4x4 front + rear diff set**~~ | **Outdrive:** TBD, likely 5mm<br>**Housing:** 7075-T6 aluminum alloy<br>**Internals:** 4140 carbon steel gears<br>**Part:** SLA1337FR<br>**Fits:** Slash 4x4, Jato 4x4, Rustler 4x4, XO-1, and more<br>**Price:** **$75.90** (out of stock) | Pro: 4140 steel gears for durability. Complete matched front+rear set. Wide Traxxas 4x4 compatibility. If 5mm, now outdrive-compatible with the axle plan<br><br>Con: **$75.90 for aluminum housing** that augers out faster than plastic, holds fluid worse, and costs 5× the native Jato 4x4 stock diff. Out of stock | <img src="src/drivetrain_gpm_diff_sla1337fr.jpg" width="500"> |
| 🚫 ~~**Integy C31463, Slash 4x4 / Stampede 4x4 / Rustler 4x4 diff**~~ | **Outdrive:** TBD, likely 5mm<br>**Housing:** TBD (likely aluminum)<br>**Internals:** N/A<br>**Part:** C31463<br>**Fits:** Slash 4x4 pattern<br>**Price:** **$18.49** (sale from $24.99), in stock | Pro: Cheapest aftermarket option here, in stock. If 5mm, now outdrive-compatible with the axle plan<br><br>Con: Material TBD, if aluminum housing, augers out faster, holds fluid worse than plastic. At $18.49 it's still more expensive than the native Jato 4x4 stock diff ($12.97) | <img src="src/drivetrain_integy_diff_c31463.jpg" width="500"> |

### Alternative Upgrade Parts

Optional ring gear / pinion upgrades for the E-Revo diff. All vetoed, marginal gains over stock that don't justify the cost.

> *Spec format: Part · Material · Gears · Price*

| Part | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ❌ ~~**GPM ER1200TS, Carbon Steel Bevel Gear Set (29T/11T)**~~ | **Part:** ER1200TS<br>**Material:** Carbon steel, nitride hardened, helical spiral cut<br>**Gears:** 29T ring bevel + 11T pinion, 1.0 module (6pc inc. screws)<br>**Price:** **$43.90** (out of stock) | Pro: Nitride hardened, helical spiral cut, carbon steel. Replaces TRA5379X<br><br>Con: Marginal gains, stock TRA5379X in the assembled diff is fine. $43.90 and out of stock | <img src="src/drivetrain_gpm_bevel_gears_er1200ts.jpg" width="500"> |
| ❌ ~~**GPM ER1337TS, Hard Steel Spiral Gears (13T/37T)**~~ | **Part:** ER1337TS<br>**Material:** Hard steel, spiral cut<br>**Gears:** 13T + 37T matched pair<br>**Price:** **$36.90** | Pro: Hard steel, spiral cut geometry<br><br>Con: Marginal gains, unlikely to outperform stock. $36.90 not worth it | <img src="src/drivetrain_gpm_spiral_gears_er1337ts.jpg" width="500"> |
| ❌ ~~**Traxxas TRA5379R, Spiral Cut Ring Gear + Pinion**~~ | **Part:** TRA5379R<br>**Material:** Spiral cut ring gear + pinion<br>**Gears:** Ring gear + pinion<br>**Price:** **$39.95** | Pro: Spiral cut geometry theoretically smoother<br><br>Con: Marginal gains at best, stock already covers this fine. $39.95 not worth it | <img src="src/drivetrain_traxxas_spiral_cut_ring_gear_tra5379r.jpg" width="500"> |

### Why 5mm (stock) wins now

The axle plan changed, the build now runs the **Slash 4x4-pattern CVDs on the Tekno M6 stub build**, not the E-Revo 1.0 CVDs:
- **Slash 4x4-pattern CVDs (knock-off TRA6851R/6852R style)**, 5mm cups, feeding the **Tekno M6 17mm stubs** front + rear (see [`driveshaft_analysis.md`](driveshaft_analysis.md))
- **Diffs must be 5mm to mate that axle**

That makes the **native Jato 4x4 stock diff** the correct pick again, cheapest, in stock, no gearbox-housing fitting required. The in-hand E-Revo 1.0 diffs (already owned, $0 sunk) drop to spares/fallback unless the axle plan ever moves back to 6mm E-Revo CVDs.

---

## Center Diff

> **Chosen: AliExpress metal center diff (alum body + integrated steel 54T spur), ~$20, comes pre-filled with the correct oil.** One cheap fully-assembled unit that includes the spur and the oil, so there is nothing separate to buy or fit. It trades the lighter TRA6814 plastic (and the plastic-fuse failure mode) for a cheap all-in-one metal diff, a tradeoff taken knowingly. The TRA6814 OEM plastic is the lighter alternative if you would rather keep the separate plastic spur fuse.

<p align="center"><img src="src/drivetrain_aliexpress_center_diff_alum_steel.jpg" width="600"><br><em>AliExpress metal center diff (alum body + integrated steel 54T spur), ~$20, 74.6 g</em></p>

> *Spec format: Part · Housing · Spur · Oil · Weight · Fits · Price*

| Center Diff | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **AliExpress Heavy Duty Centre Diff (alum body + steel 54T spur)** — *chosen* | **Part:** Tolex (generic)<br>**Housing:** aluminum<br>**Spur:** **steel 54T, integrated** (this is the build's spur, so the separate plastic TRA3956R is now a spare)<br>**Oil:** **comes pre-filled** with the correct wt (fully assembled)<br>**Weight:** **74.6 g** (measured, incl. steel 54T spur + assembled output shaft)<br>**Fits:** Slash 4x4 / Hoss 4x4 VXL<br>**Price:** **~$20** ($15.23 sale / $23.43 list) | Pro: **Chosen: one cheap (~$20) fully-assembled metal unit with the integrated steel 54T spur, no separate spur to buy or fit.** A knock-off of the $69.95 TRA6780. Complete drop-in<br><br>Con: **Heavier (74.6 g) than the TRA6814 plastic**, and the **integrated steel spur removes the plastic-fuse failure mode** (see [spur gear](#spur-gear)). Aluminum housing augers out faster than plastic. Weight + fuse tradeoff taken knowingly for the cheap all-in-one metal diff | <img src="src/drivetrain_aliexpress_center_diff_alum_steel.jpg" width="500"> |
| 🔵 **TRA6814, Traxxas Pre-Built Center Diff Kit** — *lighter plastic alternative* | **Part:** TRA6814 (rebuild: TRA6884 housing + TRA6883 gear set)<br>**Housing:** Plastic<br>**Spur:** N/A (separate spur)<br>**Oil:** Tunable via silicone oil (sealed, pre-filled)<br>**Weight:** N/A<br>**Fits:** Slash 4x4, Jato 4x4<br>**Price:** **$39.95** complete (~$20 built from TRA6884 + TRA6883) | Pro: **Lighter than the metal AliExpress unit** and keeps the plastic-fuse failure mode (needs the separate plastic spur). Pre-built, sealed, tunable. **Cheaper to build from components**, TRA6884 ($5) + TRA6883 ($15) = ~$20 vs $39.95. $5 housing rebuild when worn<br><br>Con: Not the pick here (went with the cheap all-in-one metal unit). $39.95 for the complete kit if not building from parts | <img src="src/drivetrain_traxxas_center_diff_tra6814.jpg" width="500"><br><img src="src/drivetrain_traxxas_center_diff_housing_tra6884.jpg" width="500">&nbsp;<img src="src/drivetrain_traxxas_center_diff_gear_set_tra6883.jpg" width="500"><br><em>TRA6814 complete · TRA6884 housing · TRA6883 gear set</em> |
| 🔵 **TRA6780A, Pro-Built Center Diff** | **Part:** TRA6780A<br>**Housing:** plastic (black)<br>**Spur:** steel 54T 32-pitch (integrated)<br>**Oil:** 500k (pre-filled, nearly locked)<br>**Weight:** N/A<br>**Fits:** Hoss / Slash / Stampede / Rustler 4x4<br>**Price:** $60.00 | Pro: Plastic housing, stays round, holds fluid, outlasts aluminum. Pre-built, sealed, $60<br><br>Con: Integrated steel spur kills the plastic-fuse failure mode. 500k oil = nearly locked center, too stiff for offroad dirt use. Outdrive size TBD, verify 6mm | <img src="src/drivetrain_traxxas_pro_built_center_diff_tra6780a.jpg" width="500"> |
| 🔵 **TRA6780R, Pro-Built Center Diff** | **Part:** TRA6780R<br>**Housing:** plastic (black)<br>**Spur:** steel 50T 32-pitch (integrated)<br>**Oil:** 20m (pre-filled)<br>**Weight:** N/A<br>**Fits:** Hoss / Slash / Stampede / Rustler 4x4<br>**Price:** $60.00 | Pro: Plastic housing. Pre-built, sealed, $60. 50T spur<br><br>Con: Integrated steel spur kills the plastic-fuse failure mode. Outdrive size TBD, verify 6mm | <img src="src/drivetrain_traxxas_pro_built_center_diff_tra6780r.jpg" width="500"> |
| ❌ ~~**TRA6780, Complete Center 4X4 Diff Kit (alum housing + steel 54T spur)**~~ | **Part:** TRA6780 (Autramodel.cz)<br>**Housing:** aluminum<br>**Spur:** steel 54T (integrated)<br>**Oil:** N/A<br>**Weight:** **137g** (0.137 kg) measured<br>**Fits:** Hoss / Slash / Stampede / Rustler 4x4<br>**Price:** $69.95 | Pro: Complete bolt-in unit, alum housing + steel spur is durable on paper<br><br>Con: **Tons of unneeded rotational weight**, heavy alum housing + steel spur add spinning mass right in the driveline. **Aluminum housing augers out** (wears oblong) faster than plastic and holds fluid worse. Steel spur kills the plastic-fuse failure mode. **$69.95**, same alum+steel design as the ~$20 AliExpress unit, just 3.5× the price | <img src="src/drivetrain_traxxas_complete_center_diff_tra6780.jpg" width="500"> |

### Slipper Clutch (alternative to center diff — vetoed)

A slipper clutch replaces the center diff entirely. Vetoed here because it doesn't suit this build's surface.

> *Spec format: Part · Type · Price*

| Part | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ❌ ~~**TRA6878A, Complete Slipper Clutch**~~ | **Part:** TRA6878A<br>**Type:** complete slipper clutch assembly (replaces center diff)<br>**Price:** **$20.00** | Pro: Works well on high-grip surfaces<br><br>Con: **Doesn't handle well on dirt/low-grip tracks**, this build is set up for dirt offroad, not high-grip. Center diff (TRA6814) is the correct setup | <img src="src/drivetrain_traxxas_slipper_clutch_tra6878a.jpg" width="500"> |

---

## Center Diff Oil

**Chosen: 20,000 wt (20k cSt).** I’ve tested it across several builds, lands in the sweet spot between freewheeling traction handoff and progressive lockup under throttle.

| Oil weight | Behavior | Use case |
|---|---|---|
| 5k cSt | Very fluid, lots of differentiation, freewheels in turns | Light-traction surfaces (sand, very loose) |
| 10k cSt | Quicker freewheel, less lockup under power | Tight indoor tracks |
| **20k cSt ⭐** | Balanced, diffs under hard throttle, freewheels at part-throttle | **Chosen, general offroad / 4S dirt** |
| 50k cSt | Mostly locked, all-four-wheels-pull feel | Crawling, low-grip climbs |
| 100k+ | Effectively locked spool | Drag/speed-run with grip |

**Fill level: half full only.** Overfilling plastic diff housings causes them to explode under pressure, this is operator error. Fill to half, no more.

**Why not just lock the center diff?** Locked center = no torque differentiation front-to-rear = chassis pushes / pivots awkwardly on uneven surfaces. 20k gives the locked-feel under power without the disadvantages on rough offroad.

---

## Front & Rear Diff Oil

**Front: ~7k wt (recommended starting point)**, shared target with [Mike's Jato](../Jato4x4_Mike/README.md#diff-oil). On loose / low-grip dirt with this 4S car, ~7k keeps steering while the 20k center holds drive stability.

| Diff | Weight | Tuning |
|---|---|---|
| **Front** | **~7k wt** (start) | **Lighter (5k)** = more turn-in on the slickest days; **heavier (10k+)** = calmer if it torque-steers / plows |
| **Rear** | TBD | Set after front + center are dialed |

> Same target as Mike's Jato (the two share this setup), dial it on track, then lock the value in on both cars. *(This is the Jato E-buggy figure; the [E-Revo](../ERevo_1.0/README.md) runs a heavier **30k** front because it's a different, heavier platform.)*

---

## Spur Gear

> **Decision changed: running the integrated steel 54T spur that comes on the [AliExpress metal center diff](#center-diff).** So the build has no separate spur. The separate **TRA3956R 54T plastic spur does not fit this metal center diff** (it mounts to a plastic center diff like the TRA6814), so it is only relevant if you ever go back to that plastic-center-diff setup. The plastic-spur analysis below is kept for that reference.
>
> **Plastic-spur reference (the TRA3956R 54T, for a plastic center diff):** plastic is a sacrificial failure point, in a bad crash it strips before transferring force to the metal pinion, driveshafts, and gearbox. 54T over 50T/52T: **more teeth spread the load and wear more evenly**, and **54T lands the gearing where we want it.** Cheap to replace.

<p align="center"><img src="src/drivetrain_traxxas_spur_gear_tra3956r_54t.jpg" width="600"><br><em>TRA3956R 54T plastic spur, the plastic-center-diff option (not used; the metal center diff has its own steel spur)</em></p>

### Spur Gear Requirements

| Requirement | Type | Why |
|---|---|---|
| **Plastic material** | Must | Plastic is the **intentional sacrificial failure point**, strips in a crash before the metal pinion, driveshafts, or gearbox take the hit. Metal spur gears transfer crash energy into more expensive components |
| **32P / 0.8M pitch** | Must | Slash 4x4 / Jato 4x4 platform standard, all gearbox housings and pinions use this pitch |
| **No slipper clutch** | Must | Slipper clutch works on high-grip surfaces, doesn't handle well on dirt tracks. This build is set up for dirt/low-grip offroad. Center diff (TRA6814) is the correct setup |
| **Fits Slash 4x4 / Jato 4x4 center diff gearbox** | Must | Must seat correctly in the center diff housing (TRA6814 / TRA6884) |
| **Cheap** | Must | It's a consumable part. At $3–5 it should be guilt-free to replace |
| **Correct tooth count for desired gear ratio** | May | Tooth count affects top speed vs torque, tune to motor KV and track conditions |

### Spur Gear Comparison

> *Spec format: Teeth · Pitch · Material · Fits · Price*

| Spur Gear | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **TRA3956R, 54T plastic (center diff)** | **Teeth:** **54T**<br>**Pitch:** 32P / 0.8M<br>**Material:** black plastic<br>**Fits:** TRA6814 center differential<br>**Price:** **$3.00** | Pro: $3, correct plastic-fuse material, fits the TRA6814 center diff. **54T = more teeth, so load spreads and wears more evenly, slightly stronger than 50T/52T.** Lands our gearing exactly where we want it<br><br>Con:, | <img src="src/drivetrain_traxxas_spur_gear_tra3956r_54t.jpg" width="500"> |
| 🔵 **TRA6842R, 50T plastic** | **Teeth:** **50T**<br>**Pitch:** 32P / 0.8M<br>**Material:** black plastic<br>**Fits:** Center diff housing<br>**Price:** **$3.00** | Pro: $3, correct material, correct pitch. 50T gives a slightly taller ratio vs 52T<br><br>Con: Fewer teeth than the chosen 54T, load spread over less contact | <img src="src/drivetrain_traxxas_spur_gear_tra6842r_50t.jpg" width="500"> |
| 🔵 **TRA6843R, 52T plastic** | **Teeth:** **52T**<br>**Pitch:** M0.8 / 32P<br>**Material:** black plastic<br>**Fits:** Center diff housing (OD 43mm / ID 22.5mm)<br>**Price:** **$3.00** | Pro: $3, correct material. 52T sits between 50T and 54T<br><br>Con: Fewer teeth than the chosen 54T | <img src="src/drivetrain_traxxas_spur_gear_tra6843r_52t.jpg" width="500"> |
| ❌ ~~**Hot Racing SSLF254D, 54T steel**~~ | **Teeth:** 54T<br>**Pitch:** 32P / 0.8M<br>**Material:** hardened steel<br>**Fits:** Center diff housing<br>**Price:** ~$15 | Pro: Won't strip under abuse<br><br>Con: **Wrong design philosophy**, metal spur transfers crash energy to the pinion and drivelines instead of stripping. Defeats the purpose of having a sacrificial failure point | <img src="src/drivetrain_hot_racing_spur_gear_sslf254d.jpg" width="500"> |
| ❌ ~~**GPM SSLA054T, 54T steel**~~ | **Teeth:** 54T<br>**Pitch:** 32P / 0.8M<br>**Material:** hardened steel<br>**Fits:** Center diff housing<br>**Price:** $19.90 | Pro: CNC machined, black finish<br><br>Con: Same metal spur problem, no sacrificial failure point. More expensive than plastic for a worse outcome | <img src="src/drivetrain_gpm_spur_gear_ssla054t.jpg" width="500"> |
| ❌ ~~**Integy T8573, 50T steel**~~ | **Teeth:** 50T<br>**Pitch:** 32P / 0.8M<br>**Material:** billet steel<br>**Fits:** Center diff housing<br>**Price:** **$24.83** (sale from $26.99) | Pro: Billet steel construction<br><br>Con: Metal spur, wrong failure mode. $24.83 for a part that should cost $3 and be plastic | <img src="src/drivetrain_integy_spur_gear_t8573.jpg" width="500"> |
| ❌ ~~**Robinson Racing RRP7954, 54T steel**~~ | **Teeth:** 54T<br>**Pitch:** 32P / 0.8M<br>**Material:** hardened black steel<br>**Fits:** Slipper clutch eliminator (bolts direct, no slipper pads)<br>**Price:** **$18.22** (list $19.80) | Pro: Hardened black steel, well-reviewed, takes brushless 6S abuse<br><br>Con: Same metal spur problem, no sacrificial failure point. Cheaper than I assumed, but still wrong failure mode for this build | <img src="src/drivetrain_robinson_racing_spur_gear_rrp7954.jpg" width="500"> |

### Spur Gear Notes

- **Why plastic wins:** the spur gear is the least expensive, most accessible part in the drivetrain chain. In a crash, it strips first, before the pinion, CVDs, diff outdrives, or gearbox housing take the hit. A $3 spur gear saving a $30 pinion and $80 in CVD/driveline parts is exactly the right trade-off.
- **Metal spur = wrong failure mode:** a metal spur that won't strip transfers crash energy directly into the pinion and downstream drivetrain. You save the $3 plastic gear and destroy far more expensive parts.
- **Tooth count and gear ratio:** all 32P / 0.8M gears are compatible. Choose tooth count based on motor KV and desired top speed vs torque balance. 50T–54T is the standard range for 4S offroad builds.
- **Slipper vs center diff:** slipper clutch (TRA6878A) works on high-grip surfaces but doesn't handle well on dirt/low-grip tracks, this build is set up for dirt offroad. Center diff (TRA6814) is the correct setup. Use center-diff specific spur gears (TRA6842R, TRA6843R) which seat directly in the center diff housing, not slipper assembly gears.

---

## Sources

- E-Revo CVD / diff compatibility, community confirmation in [RC Talk forum threads](https://www.rctalk.com/forum/threads/traxxas-jato-4x4.144356/) on Jato 4x4 builds using E-Revo drivetrain parts
- Center diff oil viscosity, Castle Creations / RPM tuning guides + my own experience
