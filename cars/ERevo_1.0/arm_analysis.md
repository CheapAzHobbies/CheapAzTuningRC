# Suspension Arm Selection — E-Revo 1.0

> **Front: keep the stock Traxxas arms. Rear: RPM 80562 True Track conversion.** Two opposite calls, one reason each. The RPM front A-arms **flex too much**, and that flex lets the front wheels deflect under power until it **snaps the CVDs** I run, so the stiffer stock front arms stay. At the rear, the **RPM True Track** kit deletes the rear toe links entirely, locking in a fixed **1.5° per side (3° total) toe-in** and killing rear bump steer. That removes a wandering wear/adjustment point and gives a rear end that tracks straight on rough dirt. True Track in hand, **$32.95** (PowerHobby).

<p align="center"><a href="https://www.powerhobby.com/products/rpm-80562-true-track-rear-a-arm-conversion-kit-black-traxxas-revo"><img src="src/suspension_rpm_truetrack_rear_arm_80562.jpg" width="600"></a><br><em>RPM 80562 True Track rear A-arm conversion (black) — deletes the rear toe links, locks 3° toe-in</em></p>

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Front Arms](#front-arms) — why stock beats RPM up front (CVD survival)
- [Rear Arms](#rear-arms) — True Track conversion: fixed toe, no bump steer, less upkeep
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Front arms stiff enough not to flex into the CVDs** | Must | RPM front arms flex under power and that deflection breaks the CVDs I run |
| **Hold rear toe without wandering** | Must | Stock rear toe links shift and need re-checking; want a fixed, repeatable toe |
| **Fewer wear / adjustment points** | May | Toe links and lower pillow balls are extra maintenance; deleting them = less upkeep |
| **Durable on dirt + occasional beach** | Must | Basher use; corrosion and grit are constant |

---

## Front Arms

> **Keep the stock Traxxas front arms.** This is the rare case where stock beats the RPM upgrade. RPM molds its arms soft so they survive crashes by flexing, but that same flex lets the front hub deflect under power and load the CVD at an angle until it breaks. The CVD is the expensive part, so the stiffer stock arm protects it.

| Arm | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **Stock Traxxas front arms** — *chosen front* | Material: stock composite<br><br>Stiffness: **higher than RPM**<br><br>Cost: OEM | Pro: **Stiff enough to keep the front hub square under power, so the CVDs survive.** Protects the expensive driveshaft, which is the whole point<br><br>Con: Less crash-forgiving than RPM; can crack in a big hit (cheap to replace, and rarer than the CVD breakage RPM caused) | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/suspension_traxxas_front_arm_stock.jpg` |
| ❌ ~~**RPM front A-arms** (RPM70372 front-left; sold as left / right halves)~~ | Material: molded composite<br><br>Stiffness: **soft / flexible**<br><br>Fits: 1/10 Revo / E-Revo V1 / Summit | Pro: Nearly uncrushable in a crash, cheap, dyeable<br><br>Con: **Too flexible** — flexes under power and lets the front wheel deflect, which **breaks the CVDs**. Trades a rare arm crack for repeated, pricier CVD failures, so it is a net loss on this truck | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/suspension_rpm_front_arm_70372.jpg` |

---

## Rear Arms

> **RPM 80562 True Track rear A-arm conversion.** The standout reason is maintenance: it **deletes the rear toe links** (the "toe bar"), so there is nothing back there to bend, wander, or re-shim. It locks the rear toe at a **fixed 1.5° per side (3° total)**, kills rear bump steer, and the kit is **32 g lighter** than the stock arms + links it replaces.

| Arm | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **RPM 80562 True Track rear conversion** (black) — *chosen rear, in hand* | Toe: **fixed 1.5°/side, 3° total**, non-adjustable<br><br>Lower mount: stock pillow ball **replaced by a 4 mm hinge pin** (constant toe)<br><br>Upper mount: **stock pillow ball retained** (camber stays adjustable)<br><br>Weight: **~32 g lighter** than stock arms + toe links<br><br>Fits: all Traxxas Revo<br><br>Price: **$32.95** (PowerHobby) | Pro: **Deletes the rear toe links** = no bump steer and one less maintenance point. **Fixed, repeatable 3° toe-in** for straight rear tracking on rough dirt. Lighter than stock. Installs with the Traxxas 3932 flat-head screws<br><br>Con: Rear toe is now **fixed, not adjustable** (fine if 3° is your number); composite can still break in a huge hit | <a href="https://www.powerhobby.com/products/rpm-80562-true-track-rear-a-arm-conversion-kit-black-traxxas-revo"><img src="src/suspension_rpm_truetrack_rear_arm_80562.jpg" width="500"></a> |
| 🚫 ~~**Stock Traxxas rear arms + toe links** (TRA5328 / TRA5327)~~ | Toe: **adjustable** via toe links (10–19 setting range)<br><br>Lower mount: pillow ball<br><br>Includes the separate rear toe links | Pro: Rear toe is adjustable; OEM-correct<br><br>Con: The **toe links bend and shift** = rear bump steer and a recurring check/adjust item. More parts, more pillow balls, heavier | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/suspension_traxxas_rear_arm_stock_tra5328.jpg` |

---

## Notes

- **Why opposite picks front vs rear.** Front is about **stiffness** (protect the CVD), so stock wins. Rear is about **deleting a wear point and locking toe**, so the RPM True Track wins. Same brand, opposite outcome, because the failure mode is different at each end.
- **The CVD is what RPM front arms cost you.** RPM's soft arms flex under power; the front hub deflects and loads the CVD at an angle until it snaps. The driveshaft is far more expensive and annoying to replace than a stock arm, so the stiffer stock arm is the cheaper choice over time.
- **Pin vs pillow ball (rear hub bottom).** The True Track swaps the **lower** rear pillow ball for a **4 mm hinge pin**, which is what fixes the toe angle (a pillow ball can rotate, a pin cannot). The **upper** mount keeps its pillow ball so camber is still adjustable. This change happens at the rear axle carrier, so it also shows up in [`hub_analysis.md`](hub_analysis.md).
- **Fixed 3° is a feature here.** Adjustable rear toe sounds nice, but in practice the links just drift off the setting. Locking 3° in with a pin removes the guesswork and the maintenance.
- **Install hardware.** The True Track kit mounts with the **Traxxas 3932 flat-head screws (3×6 mm)** from the same PowerHobby order.
