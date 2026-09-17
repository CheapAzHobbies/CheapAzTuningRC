# Battery Mount Selection — Jato4x4_Mike

> **Running: a 3D printed hold-down bar on the stock Traxxas retainers.** The stock bars stop at **44mm** of clearance; the printed one flexes, which is the only reason a **47mm** pack goes in. Straps are the alternative and are compared alongside the bars below.
>
> ⚠️ **LCG only.** Both stock hold-downs are for the **low-CG 4X4 chassis** and do not fit the standard one, which suits this car's [7422 LCG tub](chassis_analysis.md).
>
> **Which pack to buy** is a separate question, in [`battery_analysis.md`](battery_analysis.md).

<p align="center"><img src="src/electronics_traxxas_battery_holddown_7426x_kit.jpg" height="200">&nbsp;<img src="src/electronics_battery_bar_3d_printed.jpg" height="200"><br><em>The stock <strong>Traxxas 7426X</strong> kit, extended bar plus both retainers, what the <strong>4S</strong> car ships with (the <strong>2S</strong> gets the shorter <strong>7426</strong>) · the 3D printed bar this car runs instead</em></p>

---

## Table of Contents

- [Key Requirements](#key-requirements) — what the mounting has to do
- [The holder](#the-holder) — retainer geometry, the 22mm and 37mm holes
- [Holding the pack down](#holding-the-pack-down) — bars and straps in one table
- [Max battery size](#max-battery-size) — where 152 × 48 × 44mm comes from
- [Mike's notesheet](#mikes-notesheet) — the source for every number here
- [Notes](#notes)

---

## Key Requirements

<div align="center">

| Requirement | Type | Why |
|---|---|---|
| **Holds the pack down over rough ground** | Must | A pack that shifts under braking moves the CG and can pull on the leads |
| **Has front and rear retainers** | Must | The retainers are what the bar lands on, and **they come with the hold-down kit** (7426 / 7426X), they are not moulded into the chassis. Each has two hole positions |
| **Adjustable without buying anything** | May | Flipping the bar or moving it to the other hole is free, so most height changes should need no new part |

</div>

---

## The holder


**The retainers come with the hold-down kit, not with the chassis.** Both **7426** and **7426X** are sold as a bar **plus front and rear retainers**, so buying a bar buys the mounts too. Each retainer has **two hole positions**, and that choice matters more than which bar you own. **The front and rear retainers are different shapes and are not interchangeable**, the rear being the taller slotted one.

<div align="center">

| Hole | Height to chassis floor | Note |
|---|---|---|
| **Lower** | **22mm** | The low mount, as supplied on the BL2S cars |
| **Upper** | **37mm** | **15mm above the lower hole**, the tall mount used on the 4S cars |

</div>

**Every bar here is 5mm thick**, the printed one included, and the inner span is **152mm**, which is what caps battery length.

> ⚠️ **LCG only.** Traxxas state both hold-downs are for the **low-CG 4X4 chassis** and **do not fit the standard chassis**. That suits this car's [7422 LCG tub](chassis_analysis.md); the full conversion kit is **7421**.

<p align="center"><img src="src/electronics_traxxas_battery_holder_installed.jpg" height="375">&nbsp;<img src="src/electronics_traxxas_battery_holders_low_high.jpg" height="375"><br><em>The <strong>front</strong> retainer, mounted · the <strong>rear</strong> retainer, the taller slotted one, with its two hole positions visible</em></p>

---

---

## Holding the pack down


Two ways to do it, a **bar across the stock posts** or a **strap**. They are alternatives to each other, so they sit in one table.

> **Pick whatever you like, it genuinely does not matter.** This car runs the printed bar because **Mike prefers the plastic**. Of the strap kits the **Hot Racing LCF126X06** is the best one. None of it changes a lap time.

> *Spec format: Part · Type · Clearance · Material · Fits · Colors · Includes · Weight · Price*
>
> Bar clearances are **±1.5mm**, per the notesheet. Each stock bar is **embossed with two numbers, one per flip orientation**, so with the two post holes each bar gives four clearances.

<div align="center">

| Retention | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **3D printed bar** — *running* | **Part:** N/A (printed in house)<br>**Type:** rigid bar<br>**Clearance:** 🚧 not measured, but it flexes past the 44mm stock ceiling<br>**Material:** printed plastic, **5mm thick** like the stock bars<br>**Fits:** the stock retainers<br>**Colors:** whatever is on the spool<br>**Includes:** bar only, it reuses the retainers from a stock kit<br>**Weight:** N/A 🚧 not weighed<br>**Price:** filament only | Pro: **Flexes enough that a 47mm shorty goes in**, which no stock bar manages, and a shorty sits mid-tray where there is most room rather than out at the tight sides. Free to reprint, and the height changes by editing the model instead of buying a part<br><br>Con: **Never measured**, so its actual clearance is unrecorded. Plastic flex is doing the work, which is both why it fits and why it is the least positive clamp here | <img src="src/electronics_battery_bar_3d_printed.jpg" width="500"> |
| 🟢 **Traxxas 7426** — *in hand, the 2S car's kit* | **Part:** **7426**, "Low-CG Battery Hold-Down with Retainers"<br>**Type:** rigid bar, **the shorter one, stock on the 2S cars**<br>**Clearance:** embossed **23 / 25mm**. **23 or 25mm** in the lower hole, **36 or 40mm** in the upper<br>**Material:** plastic, 5mm thick<br>**Fits:** ⚠️ **low-CG 4X4 chassis only, not the standard chassis**. 152mm span<br>**Colors:** black, plus slate gray as **7426-SLGRY**<br>**Includes:** **bar + front and rear retainers**<br>**Weight:** N/A 🚧<br>**Price:** **$6.50 / kit** | Pro: The **finer pair of steps**, 23/25 low and 36/40 high, so it dials a pack in more precisely than the 7426X. Four usable heights from one part<br><br>Con: **Tops out at 40mm**, so it cannot hold anything near a 47mm shorty. The 2mm spread between its two low settings makes the flip barely worth doing down there | <img src="src/electronics_traxxas_battery_holddown_7426_kit.jpg" width="250">&nbsp;<img src="src/electronics_traxxas_battery_holddown_7426_slgry_kit.jpg" width="250"><br><em>the 7426 kit, bar plus both retainers · the same in slate gray, <strong>7426-SLGRY</strong></em><br><img src="src/electronics_traxxas_battery_bars_20mm_25mm.jpg" height="375">&nbsp;<img src="src/electronics_traxxas_battery_bars_29mm_23mm.jpg" height="375"><br><em>25mm face · 23mm face (shown beside the 7426X in both shots)</em> |
| 🟢 **Traxxas 7426X** — *in hand, the 4S car's kit* | **Part:** **7426X**, "Low-CG **Extended** Battery Hold-Down w/ Retainers"<br>**Type:** rigid bar, extended for taller packs, **stock on the 4S cars**<br>**Clearance:** embossed **20 / 29mm**. **20 or 29mm** in the lower hole, **35 or 44mm** in the upper<br>**Material:** plastic, 5mm thick<br>**Fits:** ⚠️ **low-CG 4X4 chassis only, not the standard chassis**. 152mm span<br>**Colors:** black<br>**Includes:** **bar + front and rear retainers**<br>**Weight:** N/A 🚧<br>**Price:** **$6.50 / kit** | Pro: **The widest range of the two, 20mm to 44mm**, covering both the lowest setting available and the stock ceiling. **44mm is the tallest any stock bar reaches here**<br><br>Con: **Coarser steps**, a 9mm jump between its two low settings, so less precise than the 7426. Even at its highest it is **3mm short of a 47mm shorty** | <img src="src/electronics_traxxas_battery_holddown_7426x_kit.jpg" width="500"><br><em>the 7426X kit: the extended bar plus the two retainers, which are different shapes and not interchangeable</em><br><img src="src/electronics_traxxas_battery_bars_profile_a.jpg" height="375">&nbsp;<img src="src/electronics_traxxas_battery_bars_profile_b.jpg" height="375"><br><em>Both bars edge on, showing the profile difference that produces the two heights</em> |
| 🔵 **Hot Racing LCF126X06** — *best of the strap kits, not fitted* | **Part:** **LCF126X06** (listed HRALCF126X06, UPC 083745540055)<br>**Type:** low alloy base plates + long buckled velcro strap<br>**Clearance:** any, the strap takes whatever height the pack is<br>**Material:** blue anodised aluminum plates, woven strap<br>**Fits:** Traxxas **Slash 4x4 LCG**, so it suits the [7422 LCG chassis](chassis_analysis.md)<br>**Colors:** blue<br>**Includes:** **2 base plates (front and rear differ)**, 4 countersunk screws, 1 strap with buckle<br>**Weight:** N/A 🚧 not weighed<br>**Price:** **$28.88** free shipping (also listed $30.23, eBay RCBoyz, item 375749960312) | Pro: **Beats the GPM on every count that matters.** **Less metal and much flatter**, so it sits lower and carries less mass, and the **longer buckled strap wraps the pack** rather than just pinning it. Velcro also sidesteps the 44mm ceiling entirely<br><br>Con: ⚠️ **`TE126X06` is the 2WD Slash version**, one character away, so order carefully. **Powerhobby sell an equivalent for this chassis at $24.74** free shipping (or $19.99 + $4.99), 🚧 part number not captured. Blue only, front and rear plates are not interchangeable, and 🚧 **"lighter" is read off the photo, not a scale** | <img src="src/electronics_hotracing_battery_holddown_lcf126x06.jpg" width="500"><br><em>the kit: 2 plates, 4 screws, strap</em><br><img src="src/electronics_hotracing_battery_holddown_lcf126x06_front.jpg" width="250">&nbsp;<img src="src/electronics_hotracing_battery_holddown_lcf126x06_rear.jpg" width="250"><br><em>front · rear, fitted. Listing photos, not this car, and the pack shown is 160 × 45 × 49mm, over this car's limit</em> |
| 🔵 **GPM TJ0126** — *taller and heavier than the Hot Racing* | **Part:** **TJ0126**<br>**Type:** **two upright 7075-T6 alloy strap anchors plus a velcro strap**, not a rigid bar. The alloy parts are what the strap threads through<br>**Clearance:** any, velcro<br>**Material:** 7075-T6 aluminum anchors, woven strap<br>**Fits:** Traxxas Jato / Slash **LOW-CG** (Ford Fiesta ST)<br>**Colors:** black, silver, blue, red, orange, green<br>**Includes:** 2 anchors, 4 countersunk screws, 1 strap<br>**Weight:** N/A 🚧 not weighed<br>**Price:** **$23.14** shipped (was $25.71, eBay HanHobby, item 820021371237); other sellers **$17.01 + $7.00**, much the same | Pro: **Six colours** against blue only for the Hot Racing, and machined 7075 anchors. Velcro takes any pack height, so the [44mm ceiling](#max-battery-size) stops mattering<br><br>Con: **Tall upright blocks, so more metal and a higher CG than the Hot Racing**, and its **shorter strap wraps the pack less well**, for about the same money. Ships from Shenzhen, 14 day returns | <img src="src/electronics_gpm_battery_strap_tj0126_black.jpg" width="110">&nbsp;<img src="src/electronics_gpm_battery_strap_tj0126_silver.jpg" width="110">&nbsp;<img src="src/electronics_gpm_battery_strap_tj0126_blue.jpg" width="110">&nbsp;<img src="src/electronics_gpm_battery_strap_tj0126_red.jpg" width="110">&nbsp;<img src="src/electronics_gpm_battery_strap_tj0126_orange.jpg" width="110">&nbsp;<img src="src/electronics_gpm_battery_strap_tj0126_green.jpg" width="110"><br><em>black · silver · blue · red · orange · green</em> |

</div>

---

---

## Max battery size


**L 152mm × W 48mm × H 44mm.** Each number comes from a different constraint:

<div align="center">

| Dimension | Limit | Set by |
|---|---|---|
| **Length** | **152mm** | The bar's inner span |
| **Width** | **48mm** | Tray width |
| **Height** | **44mm** | The 7426X in the upper hole, high orientation, the tallest stock setting |

</div>

The notesheet also sketches the tray opening itself at **165 × 50mm**, which is the raw space before a bar goes on.

> ⚠️ **152mm is not a hard length limit, it is the span at full height.** The bar curves up towards each end, so **a low pack fits under the curve and can run longer**. The 160mm Racing 5200 goes in at 37mm tall, and a straight bar takes it without trouble. **Treat 152 × 48 × 44 as the safe box for a tall pack**, and check the curve yourself if the pack is long but low.

---

---

## Mike's notesheet


Every dimension on this page is transcribed from Mike's handwritten sheet. It is kept here as the source, so the numbers can be checked against the original rather than trusted second hand.

<p align="center"><img src="src/electronics_battery_holder_bar_notesheet.jpg" width="600"><br><em>Mike's battery holder and bar measurements, the source for this doc</em></p>

---

---

## Notes

- **Two parts, eight settings.** Between the two bars and the two retainer holes there are eight combinations from 20mm to 44mm. **Before buying a taller bar, try flipping the one you have or moving it to the other hole.**
- **Measure the pack, not the label.** Everything here carries **±1.5mm**, so a setting within 1.5mm of a pack's height is a maybe, not a yes.
- **There is no separate "Traxxas OE strap" to buy.** The OE arrangement *is* the plastic bar on its retainers, listed above. A plain generic strap is $2 to $4 ([LEDGER](../../LEDGER.md) #39, #40) if you want one anyway.
