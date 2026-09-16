# Battery Mount Selection — Jato4x4_Mike

> **Running: the stock Traxxas holder posts with a 3D printed hold-down bar.** The two stock bars (**7426** and **7426X**) between them cover **20mm to 44mm** of clearance, depending on which post hole they sit in and which way up they go, so **44mm is the stock ceiling**. The 47mm shorty this car sometimes takes only clears that because a printed bar flexes, which is why the printed one is on the car. This whole topic is the main thing that does **not** carry over to the [FastAzJato4x4](../FastAzJato4x4/battery_analysis.md), which runs a CF chassis with an aluminium holder and straps and has no bar at all.

<p align="center"><img src="src/electronics_traxxas_battery_holders_low_high.jpg" width="600"><br><em>The two holder heights: the tall one standing at the back, the low one lying in front</em></p>

---

## Table of Contents

- [Key Requirements](#key-requirements) — what a bar has to do on this car
- [The holder](#the-holder) — post geometry, the 22mm and 37mm hole positions
- [Hold-down bar comparison](#hold-down-bar-comparison) — 7426 vs 7426X vs printed
- [Max battery size](#max-battery-size) — 152 × 48 × 44mm
- [Mike's notesheet](#mikes-notesheet) — the source for every number on this page
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Clears the pack height** | Must | 44mm is the tallest the stock bars reach, and the packs run here go up to 47mm |
| **Holds the pack down over rough ground** | Must | A pack that shifts under braking moves the CG and can pull on the leads |
| **Uses the stock holder posts** | Must | The posts are moulded into the chassis, so any bar has to land on those two holes |
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

## Max battery size

**L 152mm × W 48mm × H 44mm.** Each number comes from a different constraint:

| Dimension | Limit | Set by |
|---|---|---|
| **Length** | **152mm** | The bar's inner span |
| **Width** | **48mm** | Tray width |
| **Height** | **44mm** | The 7426X in the upper hole, high orientation, the tallest stock setting |

The notesheet also sketches the tray opening itself at **165 × 50mm**, which is the raw space before a bar goes on. The 152 × 48 × 44 figure is the one to buy against.

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
