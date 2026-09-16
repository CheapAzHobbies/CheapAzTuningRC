# Battery Selection — Jato4x4_Mike

> **Running: the stock Traxxas holder posts with a 3D printed hold-down bar, on full length 4S packs.** The two stock bars (**7426** and **7426X**) between them cover **20mm to 44mm** of clearance, depending on which post hole they sit in and which way up they go, so **44mm is the stock ceiling**. The 47mm shorty this car sometimes takes only clears that because a printed bar flexes, which is why the printed one is on the car.
>
> **Four packs run here and all four fit well and work great:** the Gens Ace Redline 6300 and the three CNHL packs. **The HV packs are the better ones**, see [the packs](#the-packs).
>
> The mounting half of this doc is the main thing that does **not** carry over to the [FastAzJato4x4](../FastAzJato4x4/battery_analysis.md), which runs a CF chassis with an aluminium holder and straps and has no bar at all.

<p align="center"><img src="src/electronics_traxxas_battery_holders_low_high.jpg" height="260">&nbsp;<img src="../FastAzJato4x4/src/electronics_gensace_redline2_4s_6300_140c.webp" height="260"><br><em>The two holder heights · the Gens Ace Redline 6300 that sits under them. 🚧 an in-car shot of a pack strapped under the bar would beat both</em></p>

---

## Table of Contents

- [Key Requirements](#key-requirements) — what a bar has to do on this car
- [The holder](#the-holder) — post geometry, the 22mm and 37mm hole positions
- [Hold-down bar comparison](#hold-down-bar-comparison) — 7426 vs 7426X vs printed
- [Strap options](#strap-options) — Hot Racing vs GPM vs a plain strap, and why it barely matters
- [Max battery size](#max-battery-size) — 152 × 48 × 44mm
- [The packs](#the-packs) — the four that run here, and why HV wins
- [Mike's notesheet](#mikes-notesheet) — the source for every number on this page
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Pack fits inside 152 × 48 × 44mm** | Must | **The buying number.** Length **152mm** is the bar's inner span, width **48mm** is the tray, height **44mm** is the tallest stock bar setting. See [Max battery size](#max-battery-size) |
| **Height clears the bar** | Must | **44mm is the ceiling** and it is the dimension that actually bites. A 47mm shorty only goes in because the printed bar flexes |
| **Full length 4S** | Must | This car runs full length packs, which is where it splits from the FastAz shorty-only spec. Soft case or hard case both work |
| **Holds the pack down over rough ground** | Must | A pack that shifts under braking moves the CG and can pull on the leads |
| **Uses the stock holder posts** | Must | The posts are moulded into the chassis, so any bar has to land on those two holes |
| **HV cells** | May | **The HV packs are the better ones here**, more top speed and less sag. Not a hard requirement, the standard packs still run |
| **Adjustable without buying anything** | May | Flipping the bar or moving it to the other hole is free, so most height changes should need no new part |

---

## The holder

The holder post has **two hole positions**, and that choice matters more than which bar you own.

| Hole | Height to chassis floor | Note |
|---|---|---|
| **Lower** | **22mm** | The low mount, as supplied on the BL2S cars |
| **Upper** | **37mm** | **15mm above the lower hole**, the tall mount used on the 4S cars |

**The bar itself is 5mm thick**, and its inner span is **152mm**, which is what caps battery length.

<p align="center"><img src="src/electronics_traxxas_battery_holder_installed.jpg" height="375">&nbsp;<img src="src/electronics_battery_bar_3d_printed.jpg" height="375"><br><em>A holder mounted in the chassis · the 3D printed bar that actually runs on this car</em></p>

---

## Hold-down bar comparison

Each stock bar is **embossed with two numbers, one per flip orientation**, so two parts cover four heights. Combine that with the two post holes and each bar gives four possible clearances.

> *Spec format: Part · Embossed · Lower hole (22mm) · Upper hole (37mm) · Thickness · Span · Weight · Price*
>
> All figures **±1.5mm**, per the notesheet.

| Bar | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **3D printed bar** — *running* | **Part:** N/A (printed in house)<br>**Embossed:** N/A<br>**Lower hole (22mm):** N/A<br>**Upper hole (37mm):** N/A<br>**Thickness:** N/A 🚧 not measured<br>**Span:** N/A 🚧 not measured<br>**Weight:** N/A<br>**Price:** filament only | Pro: **Flexes enough that a 47mm shorty goes in**, which no stock bar manages, and a shorty sits mid-tray where there is most room rather than out at the tight sides. Free to reprint, and the height can be changed by editing the model instead of buying a part<br><br>Con: **Never measured**, so its actual clearance is unrecorded. Plastic flex is doing the work here, which is the reason it fits and also the reason it is the least positive clamp of the three | <img src="src/electronics_battery_bar_3d_printed.jpg" width="500"> |
| 🟢 **Traxxas 7426** — *in hand* | **Part:** **7426**<br>**Embossed:** **23mm / 25mm**<br>**Lower hole (22mm):** **23mm** or **25mm**<br>**Upper hole (37mm):** **36mm** or **40mm**<br>**Thickness:** 5mm<br>**Span:** 152mm<br>**Weight:** N/A<br>**Price:** N/A | Pro: The **finer pair of steps**, 23/25 low and 36/40 high, so it dials a pack in more precisely than the 7426X. Four usable heights from one part<br><br>Con: **Tops out at 40mm**, so it cannot hold anything near a 47mm shorty. The narrow 2mm spread between its two low settings makes the flip barely worth doing down there | <img src="src/electronics_traxxas_battery_bars_20mm_25mm.jpg" height="375">&nbsp;<img src="src/electronics_traxxas_battery_bars_29mm_23mm.jpg" height="375"><br><em>25mm face · 23mm face (shown beside the 7426X in both shots)</em> |
| 🟢 **Traxxas 7426X** — *in hand* | **Part:** **7426X**<br>**Embossed:** **20mm / 29mm**<br>**Lower hole (22mm):** **20mm** or **29mm**<br>**Upper hole (37mm):** **35mm** or **44mm**<br>**Thickness:** 5mm<br>**Span:** 152mm<br>**Weight:** N/A<br>**Price:** N/A | Pro: **The widest range of the two, 20mm to 44mm**, so it covers both the lowest setting available and the stock ceiling. **44mm is the tallest any stock bar reaches here**<br><br>Con: **Coarser steps**, a 9mm jump between its two low settings, so it is less precise than the 7426. Even at its highest it is **3mm short of a 47mm shorty** | <img src="src/electronics_traxxas_battery_bars_profile_a.jpg" height="375">&nbsp;<img src="src/electronics_traxxas_battery_bars_profile_b.jpg" height="375"><br><em>Both bars edge on, showing the profile difference that produces the two heights</em> |

---

## Strap options

A strap is the other way to hold a pack down, instead of a bar across the posts.

> **Honestly, pick whatever you like, it does not really matter.** Of the strap kits the **Hot Racing LCF126X06** is the best one: less metal, sits lower, and it wraps the pack better than the GPM. But **Mike prefers the plastic bar**, the car works either way, and none of this changes a lap time. A preference, written up as one.

> ⚠️ **Two buying traps.** **`TE126X06` is the 2WD Slash version**, not this one, and the names are a character apart. **`LCF126X06` is the 4x4 LCG part.** Also, **Powerhobby sell an equivalent tall hold-down for the same chassis at $24.74 free shipping** (or $19.99 + $4.99), so the Hot Racing is not the only way in. 🚧 Powerhobby part number not captured.

<p align="center"><img src="src/electronics_gpm_battery_strap_tj0126_black.jpg" width="110">&nbsp;<img src="src/electronics_gpm_battery_strap_tj0126_silver.jpg" width="110">&nbsp;<img src="src/electronics_gpm_battery_strap_tj0126_blue.jpg" width="110">&nbsp;<img src="src/electronics_gpm_battery_strap_tj0126_red.jpg" width="110">&nbsp;<img src="src/electronics_gpm_battery_strap_tj0126_orange.jpg" width="110">&nbsp;<img src="src/electronics_gpm_battery_strap_tj0126_green.jpg" width="110"><br><em>GPM TJ0126 in black, silver, blue, red, orange and green. Two alloy anchors plus the velcro strap</em></p>

> **What the GPM kit actually is:** **two 7075-T6 alloy anchor posts, each slotted for the strap, with two countersunk screws apiece, plus a velcro strap.** It is not a rigid bar. The alloy parts are the anchors the strap threads through, so it bolts to the chassis and the strap goes over the pack.

> *Spec format: Part · Type · Material · Fits · Colors · Includes · Weight · Price*

| Retention | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **Hot Racing LCF126X06, tall battery hold-downs** — *best of the strap kits* | **Part:** **LCF126X06** (listed as HRALCF126X06, UPC 083745540055)<br>**Type:** low alloy base plates + long buckled velcro strap<br>**Material:** blue anodised aluminum plates, woven velcro strap<br>**Fits:** Traxxas **Slash 4x4 LCG**, so it suits this car's [7422 LCG chassis](chassis_analysis.md)<br>**Colors:** blue<br>**Includes:** 2 base plates, 4 countersunk screws, 1 strap with buckle<br>**Weight:** N/A 🚧 not weighed<br>**Price:** **$28.88** free shipping (also listed $30.23, eBay RCBoyz, item 375749960312) | Pro: **Beats the GPM on every count that matters.** **Less metal and much flatter**, so it sits lower and carries less mass, and the **longer buckled strap wraps the pack** rather than just pinning it. Free 2 to 4 day shipping and free returns<br><br>Con: **Dearest of the lot at $28.88**, and blue only against the GPM's six colours. 🚧 **"Lighter" is read off the photo, not a scale**, so weigh it before treating that as fact | <img src="src/electronics_hotracing_battery_holddown_lcf126x06.jpg" width="500"> |
| 🟢 **The 3D printed bar** — *what this car actually runs* | **Part:** N/A (printed)<br>**Type:** rigid hold-down bar<br>**Material:** printed plastic<br>**Fits:** the stock holder posts<br>**Colors:** whatever is on the spool<br>**Includes:** bar only<br>**Weight:** N/A<br>**Price:** filament only | Pro: **Already on the car and free**, and its flex is what lets a 47mm pack clear a 44mm ceiling. Mike prefers the plastic<br><br>Con: Height is fixed by the print, where a strap is not. See [the bar comparison](#hold-down-bar-comparison) | (see [Hold-down bar comparison](#hold-down-bar-comparison)) |
| 🔵 **GPM TJ0126, alloy anchors + velcro strap** — *taller and heavier than the Hot Racing* | **Part:** **TJ0126**<br>**Type:** upright strap anchors + velcro strap<br>**Material:** **7075-T6 aluminum** anchors, woven velcro strap<br>**Fits:** Traxxas Jato / Slash **LOW-CG** (Ford Fiesta ST)<br>**Colors:** black, silver, blue, red, orange, green<br>**Includes:** 2 anchors, 4 countersunk screws, 1 strap<br>**Weight:** N/A 🚧 not weighed<br>**Price:** **$23.14** shipped (was $25.71, eBay HanHobby, item 820021371237). Other sellers list **$17.01 + $7.00 shipping**, so much the same | Pro: **Six colours**, against blue only for the Hot Racing, and machined 7075 anchors. Velcro takes any pack height, so the [44mm bar ceiling](#max-battery-size) stops mattering<br><br>Con: **Tall upright blocks, so more metal and a higher CG than the Hot Racing**, and its **shorter strap wraps the pack less well**, for about the same money. Ships from Shenzhen, 14 day returns | <img src="src/electronics_gpm_battery_strap_tj0126_black.jpg" width="250">&nbsp;<img src="src/electronics_gpm_battery_strap_tj0126_silver.jpg" width="250"><br><em>black · silver</em> |
| 🔵 **Plain strap, Traxxas OE style** — *cheapest* | **Part:** N/A (generic)<br>**Type:** strap<br>**Material:** woven strap with velcro<br>**Fits:** anything with strap slots<br>**Colors:** various<br>**Includes:** strap only<br>**Weight:** negligible<br>**Price:** **$2.38 to $4.29** ([LEDGER](../../LEDGER.md) #39, #40, a light green strap and a 250mm red one) | Pro: **A few dollars, and it holds a pack.** Takes any pack height, same as the GPM. Nothing to machine or print<br><br>Con: **No alloy anchors**, so it relies on whatever slots the chassis gives it. The one I would pass over if the GPM is on the table, though the difference is looks more than function | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/electronics_battery_strap_generic.jpg` |

---

## Max battery size

**L 152mm × W 48mm × H 44mm.** Each number comes from a different constraint:

| Dimension | Limit | Set by |
|---|---|---|
| **Length** | **152mm** | The bar's inner span |
| **Width** | **48mm** | Tray width |
| **Height** | **44mm** | The 7426X in the upper hole, high orientation, the tallest stock setting |

The notesheet also sketches the tray opening itself at **165 × 50mm**, which is the raw space before a bar goes on. The 152 × 48 × 44 figure is the one to buy against.

---

## The packs

**Four packs run on this car and all four fit well and work great.** This car takes **full length 4S packs**, which is where it and the [FastAzJato4x4](../FastAzJato4x4/battery_analysis.md) split: that car went shorty hardcase only, so the two no longer buy to one shared spec.

**Soft case or hard case, both run here.** No case requirement, unlike the FastAz, which went hardcase-only because of the sand at Meldrum.

> **The finding: the HV packs are the better ones.** Higher voltage (15.2V, 4.35V/cell) means more motor RPM and so more top speed than a standard 14.8V pack, and these are low internal resistance packs that sag less under a hard pull.

> *Spec format: Cells · Config · ROAR · Capacity · C-rating · Weight · Connector · Size · Price*

| Pack | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **Gens Ace Redline 2.0 4S HV 15.2V 6300mAh 140C** — *on loan from the FastAz* | **Cells:** 4S HV / **15.2V** (4.35V/cell)<br>**Config:** **4S1P** (confirmed on the listing)<br>**ROAR:** ✅ brand on the list<br>**Capacity:** 6300mAh (**95.76Wh**)<br>**C-rating:** 140C (marketing)<br>**Weight:** **452g**<br>**Connector:** 5.0mm bullet<br>**Size:** **139 × 47 × 37mm** full length hardcase<br>**Price:** **$107.38** (2025-10-22) | Pro: **The best pack that runs here.** HV, low IR, light for a 6300, and at **37mm tall it clears the 44mm ceiling with 7mm to spare**. Never fitted the FastAz shorty-only spec, so it found its home on this car<br><br>Con: **5.0mm bullet**, the odd one out against the CNHL fleet's EC5. Needs an HV charger. **On loan**, it may just become Mike's outright | <img src="../FastAzJato4x4/src/electronics_gensace_redline2_4s_6300_140c.webp" width="500"> |
| 🟢 **CNHL Ultra-Thin Racing LiHV 4S 15.2V 6000mAh 120C** — *hardcase* | **Cells:** 4S / **15.2V LiHV**<br>**Config:** **4S1P** (printed on the label)<br>**ROAR:** 🚧 not stated<br>**Capacity:** 6000mAh<br>**C-rating:** 120C (marketing)<br>**Weight:** N/A 🚧<br>**Connector:** EC5<br>**Size:** **138mm** full length hardcase 🚧 height not measured<br>**Price:** **$71.00** (2026-08-26) | Pro: **Most capacity of the CNHL three**, hardcase, and HV confirmed on the charger. Fits and works well<br><br>Con: **The worst measured IR of the group at ~4.47mΩ**, which works out around **11-19C true against the 120C on the label**. Priciest CNHL here | <img src="src/electronics_cnhl_ultrathin_6000_120c.jpg" width="500"><br><em>per-cell IR at 100% charge</em> |
| 🟢 **CNHL Lightning LiHV 4S 5500mAh 120C** — *soft case* | **Cells:** 4S / **15.2V LiHV** (per the listing)<br>**Config:** 🚧 not stated<br>**ROAR:** 🚧 not stated<br>**Capacity:** 5500mAh<br>**C-rating:** 120C (marketing)<br>**Weight:** N/A 🚧<br>**Connector:** EC5<br>**Size:** N/A 🚧 not measured<br>**Price:** **$54.46** (2026-08-26) | Pro: Fits and works well, mid capacity of the three, and the listing sells it as LiHV, so it should be in the better group<br><br>Con: **The only pack here never put on the charger for an IR check**, so its voltage class is listing-only and its true C is unknown | <img src="../FastAzJato4x4/src/electronics_cnhl_lightning_4s_5500_120c_hv.png" width="500"> |
| 🟢 **CNHL Racing Series 4S 5200mAh 90C** — *soft case* | **Cells:** 4S, **reads LiHV-4S (4.35V) on the charger**<br>**Config:** 🚧 not stated<br>**ROAR:** 🚧 not stated<br>**Capacity:** 5200mAh<br>**C-rating:** 90C (marketing)<br>**Weight:** N/A 🚧<br>**Connector:** EC5<br>**Size:** N/A 🚧 not measured<br>**Price:** **$52.51** (2026-08-26) | Pro: **Much the best IR of the group at ~2.23mΩ**, roughly **26-43C true**, so it holds voltage best under load despite carrying the lowest label rating. Cheapest pack here<br><br>Con: Smallest capacity. ⚠️ **Sold as a standard LiPo but the charger reads it as LiHV**, so the listing and the pack disagree, see the note below | <img src="src/electronics_cnhl_racing_5200_90c.jpg" width="500"><br><em>per-cell IR mid-charge</em> |

### IR checks

Measured on the HOTA T6, using the [E-Revo IR-to-True-C method](../ERevo_1.0/battery_analysis.md#c-ratings-and-internal-resistance) (`max A = sag ÷ IR`, `true C = max A ÷ Ah`). **Informational only**, the CNHL packs are not in the shared cycle tracker.

| Pack | Per-cell IR | Average | True C | Label |
|---|---|---|---|---|
| **CNHL Racing 5200** (mid-charge) | 2.3 / 2.2 / 2.3 / 2.1 mΩ | **~2.23mΩ** | **~26-43C** | 90C |
| **CNHL Ultra-Thin 6000** (100% charge) | 4.5 / 4.3 / 4.6 mΩ (4th didn't register) | **~4.47mΩ** | **~11-19C** | 120C |

<p align="center"><img src="src/electronics_cnhl_racing_5200_90c.jpg" width="380">&nbsp;<img src="src/electronics_cnhl_ultrathin_6000_120c.jpg" width="380"><br><em>CNHL Racing 90C 5200mAh, IR mid-charge · CNHL Ultra-Thin 120C 6000mAh, IR at 100%</em></p>

> ⚠️ **Every label here overstates the C-rating by a wide margin**, the 90C pack measuring better than the 120C one. **The cheapest pack has the best IR.** Treat the printed number as marketing and the IR as the real figure.

> **The listing and the charger disagree on the Racing 5200.** It is sold as a standard LiPo, but the charger reads **LiHV-4S (4.35V)**. Both CNHL packs that have been checked read HV, so the Lightning 5500 is probably HV too, but it has never been on the charger to confirm.

**Sharing works one way.** Shorties fit this car as well, so anything bought to the FastAz spec can run here, while the full length packs stay on this one.

---

## Mike's notesheet

Every dimension on this page is transcribed from Mike's handwritten sheet. It is kept here as the source, so the numbers can be checked against the original rather than trusted second hand.

<p align="center"><img src="src/electronics_battery_holder_bar_notesheet.jpg" width="600"><br><em>Mike's battery holder and bar measurements, the source for this doc</em></p>

---

## Notes

- **Why the printed bar is on the car.** The tallest stock setting is 44mm and the shorty is 47mm, so no stock bar clamps it. The printed bar flexes over that 3mm gap. A shorty also sits mid-tray, where clearance is best, rather than out at the sides where it is tightest.
- **Two parts, eight settings.** Between the two bars and the two post holes there are eight combinations from 20mm to 44mm. Before buying a taller bar, check whether flipping the one already fitted or moving it to the other hole gets there.
- **The tolerance is real.** Everything is **±1.5mm**, so treat a setting that lands within 1.5mm of a pack's height as a maybe, not a yes, and measure the pack rather than trusting its label.
- **None of this applies to the [FastAzJato4x4](../FastAzJato4x4/battery_analysis.md).** That car's CF chassis uses an aluminium holder and straps, so height is not a constraint there and there is no bar to flip. It is the main difference between the two builds.
