# Wheel Hexes — FastAzJato4x4

> **The 17mm hex that mounts the wheel onto the Tekno M6 stub.** This build runs 17mm wheels on the [Tekno M6 stubs](driveshaft_analysis.md#tekno-stubs-front--rear), so it needs a 17mm hex — but the M6 stub is a smaller/different profile than what these hexes are cut for, so the hex gets **lightly filed to seat**.
>
> - **Leaning: Tekno OEM 17mm hex** (pin-through, from the **TKR1654-17** kit). The cross-pin passes *through* the hex, so the hold is more secure and it's **more forgiving if you shave it thin** to fit the M6 stub.
> - **In hand alt: Traxxas TRA6469** (17mm splined aluminum, 5.9g) — works, but it's a solid screw-pin hex, so filing it thin is riskier.
> - **Stock Traxxas rims are the catch:** their inner **star pattern won't seat on a standard 17mm hex** without cutting the rim out. If you want to run stock Traxxas wheels, use the **Tekno SCT410 star hex (TKR5570-17)**, whose star profile matches them. This build sidesteps it by running standard 17mm wheels (RedSpider etc.) on a standard hex.

<p align="center"><img src="src/drivetrain_tekno_1654-17_front_hub_adapter.jpg" width="300">&nbsp;<img src="src/drivetrain_traxxas_wheel_hub_17mm_tra6469_weight.jpg" width="300"><br><em>Leaning: Tekno OEM 17mm hex (pin-through, in the TKR1654-17 kit) · alt: Traxxas TRA6469 17mm splined aluminum, 5.9g</em></p>

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Comparison](#comparison)
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **17mm hex** | Must | The wheels this build runs are 17mm — the hex has to be 17mm |
| **Seats on the Tekno M6 stub** | Must | The M6 stub is a smaller/different profile, so the hex must fit it — in practice this means **light filing** of the hex bore/chamfer |
| **Forgiving when shaved thin** | May | Since the hex gets filed to fit, a **pin-through** design tolerates thin shaving better than a solid screw-pin hex |
| **Matches the wheel's inner pattern** | May | Standard 17mm wheels drop on any 17mm hex; **stock Traxxas star-pattern rims need the special star hex** or the rim cut out |

---

## Comparison

> *Spec format: Type · Part · Material · Stub fit · Wheel pattern · Retention · Weight · Price*

| Hex | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **Tekno OEM 17mm hex** (pin-through) — *leaning* | **Type:** 17mm hex, pin-through<br>**Part:** included in **TKR1654-17** (front M6 adapter kit)<br>**Material:** Aluminum<br>**Stub fit:** Tekno M6 stub — **light filing (~0.2–0.5mm)** to seat<br>**Wheel pattern:** Standard 17mm<br>**Retention:** **Cross-pin passes through the hex** (pin-through)<br>**Weight:** N/A (not yet weighed)<br>**Price:** Included in TKR1654-17 (**$23.15/pr**) | Pro: **The pin-through design is the reason it's the pick** — the cross-pin runs through the hex for a more secure hold, and it's **more forgiving if shaved thin** to clear the M6 stub. Already in hand with the front adapter kit, so **no extra buy** — the same shaved hex works front and rear<br><br>Con: Not yet photographed/weighed. Still needs the light filing like any 17mm hex on an M6 stub | <img src="src/drivetrain_tekno_1654-17_front_hub_adapter.jpg" width="500"> |
| 🔵 **Traxxas TRA6469** — *in hand, alternative* | **Type:** 17mm splined hex<br>**Part:** TRA6469<br>**Material:** 6061-T6 aluminum, blue-anodized<br>**Stub fit:** Cut for 6mm axles — **file to the chamfer/bevel edge** to seat on the M6 stub<br>**Wheel pattern:** Standard 17mm<br>**Retention:** Screw pin 4×13mm w/ threadlock<br>**Weight:** **5.9g** measured<br>**Price:** N/A | Pro: **In hand, genuine Traxxas alloy, weighed at 5.9g.** Standard 17mm, seats after filing to the chamfer/bevel — the same shaved hub works front and rear<br><br>Con: **Solid screw-pin, not pin-through** — filing it thin is riskier than the Tekno hex, so it's the fallback, not the pick | <img src="src/drivetrain_traxxas_wheel_hub_17mm_tra6469_weight.jpg" width="500"> |
| 🔵 **Tekno SCT410 star hex (TKR5570-17)** — *only if running stock Traxxas rims* | **Type:** 17mm star-drive hub adapter (SCT410)<br>**Part:** TKR5570-17 (2pc set — the same kit the TKR5580 stub belongs to)<br>**Material:** Aluminum<br>**Stub fit:** SCT410 stub kit (mates the TKR5580 stub)<br>**Wheel pattern:** **Star profile — seats stock Traxxas rims** that a standard 17mm hex can't take without cutting<br>**Retention:** N/A<br>**Weight:** N/A<br>**Price:** **$34.99** (full kit) | Pro: **The only clean way to run stock Traxxas star-pattern wheels** on this setup — its star profile matches the rim, no cutting the rim out. Comes with the SCT410 stub kit<br><br>Con: **Not needed here** — this build runs standard 17mm wheels on a standard hex, so it uses the Tekno M6 hexes instead. Pricier as a full kit | <img src="src/drivetrain_tekno_sct410_star_hex_tkr5570-17.jpg" width="500"> |

---

## Notes

- **Why the hex gets filed:** the 17mm hexes are cut for a 6mm axle / their own stub, and the **Tekno M6 stub is a smaller/different profile**, so the hex bore/chamfer needs a light shave (~0.2–0.5mm) to seat. See the [Tekno stubs section](driveshaft_analysis.md#tekno-stubs-front--rear) for the stubs these mount to.
- **Pin-through beats screw-pin when shaving thin.** The Tekno OEM hex's cross-pin runs *through* the hex, so even shaved thin it holds securely — the reason it's leaning over the solid TRA6469, which relies on a screw pin and has less meat to give up.
- **The stock-Traxxas-rim trap.** Stock Traxxas wheels have a **star-shaped inner pattern** that will **not** drop onto a plain 17mm hex — you'd have to cut the star out of the rim or swap to the **TKR5570-17 star hex**. This build avoids the whole issue by running standard 17mm wheels (RedSpider etc.) on a standard hex.
- **Same shaved hub, front and rear.** Whichever hex is picked, the same filing works at both ends — one modification, four hexes.
- **Hubs + bearings are separate.** Hub carriers and bearing sizing (10×18×5 inner for the Raptor R + M6 front, etc.) live in [`hub_carrier_analysis.md`](hub_carrier_analysis.md), not here.
