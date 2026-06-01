# Servo Selection — FastAzJato4x4

> **Chosen: PTK 9752TG-D Metal High-Speed Low-Profile Servo** — the **successor to the JX CLS series** the build ran previously. Already in hand from a previous build, $25 sunk; bulk-bought 8-pack at ~$19.65/ea on 2026-06-01 as spares ([`Deals/servos.md`](../../Deals/servos.md)). The JX servos (CLS6322HV / CLS6336HV) are the predecessor data points — kept in the comparison below for context, not as live candidates.

<p align="center"><img src="https://placehold.co/600x400/eee/333?text=IMAGE+NEEDED" width="600"><br>🚧 save as <code>src/steering_ptk_9752tgd_servo.jpg</code> · <em>Chosen — PTK 9752TG-D low-profile metal-gear digital servo</em></p>

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Servo Comparison](#servo-comparison)
- [Weight Photos](#weight-photos)
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Fits Slash 4x4 / Jato 4x4 servo cavity** | Must | Has to bolt into the CF chassis servo mount without modification |
| **Metal gear train** | Must | Plastic gears strip under hard steering inputs at 4S throttle |
| **High torque (≥ 20 kg-cm)** | Must | Drives the chosen aluminum bell crank under load without stalling |
| **High speed (≤ 0.10s / 60°)** | Must | Steering response has to keep up with chassis on quick direction changes |
| **High voltage (HV) capable** | May | Lets it run direct off the BEC at 7.4V for the best torque/speed numbers — most modern receivers/BECs are HV anyway |
| **Light** | May | Mounted high in the chassis cavity, every gram up there hurts CG. Weight photos in the [Weight Photos](#weight-photos) section |

---

## Servo Comparison

| Servo | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **PTK 9752TG-D** | **Voltage:** 4.8V – 7.4V (HV)<br><br>**Speed @ 6.0V:** TBD sec/60°<br><br>**Speed @ 7.4V:** TBD sec/60°<br><br>**Torque @ 6.0V:** TBD kg-cm<br><br>**Torque @ 7.4V:** TBD kg-cm<br><br>**Gear:** metal<br><br>**Motor:** TBD (likely coreless)<br><br>**Profile:** low-profile<br><br>**Weight:** TBD (waiting on photo) | Pro: **Proven on Mike's Jato 4x4 — faster and better steering response than the JX it replaced.** Already in hand, 8 spares bought at ~$19.65/ea. Well-matched to the chosen aluminum bell crank, low-profile fits the CF chassis cavity, HV<br><br>Con: **High current draw — can brown out weak BECs (≤3A class).** Known marginal on the E-Revo 1.0's Castle Mamba X internal **3A BEC** at full lock under load. Pair with a stronger BEC (≥5A) or run an external/standalone BEC if pairing with a low-amp ESC | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/steering_ptk_9752tgd_servo.jpg` |
| 🚫 ~~**JX Ecoboost CLS6336HV** — *wrong class (1/8 truggy / Kraton)*~~ | **Voltage:** 6.0V – 8.4V (HV)<br><br>**Speed @ 6.0V:** ~0.10 sec/60°<br><br>**Speed @ 7.4V:** ~0.07 sec/60°<br><br>**Torque @ 6.0V:** ~30 kg-cm<br><br>**Torque @ 7.4V:** 36 kg-cm<br><br>**Gear:** metal<br><br>**Motor:** coreless<br><br>**Profile:** standard-height<br><br>**Weight:** TBD | Pro: Big torque number, suited to **1/8 truggy / Kraton-class** steering loads where 30+ kg-cm is actually needed<br><br>Con: **Wrong tool for this build.** The FastAzJato doesn't need 36 kg-cm — the steering loads here don't even pull a 21 kg servo to its limit. **Slightly slower on paper** vs the CLS6322HV (~0.07 vs ~0.06 sec/60° @ 7.4V) per the published spec numbers. Trading the small spec-sheet speed margin for torque you'll never use is a net loss | <img src="src/steering_jx_cls6336hv_servo.jpg" width="500"> |
| ❌ ~~**JX CLS6322HV** (EcoBoost branding) — *predecessor, retired & out of stock*~~ | **Voltage:** 4.8V – 7.4V (HV)<br><br>**Speed @ 6.0V:** ~0.08 sec/60°<br><br>**Speed @ 7.4V:** ~0.06 sec/60°<br><br>**Torque @ 6.0V:** ~18 kg-cm<br><br>**Torque @ 7.4V:** 21 kg-cm<br><br>**Gear:** metal<br><br>**Motor:** coreless<br><br>**Profile:** standard-height<br><br>**Weight:** **67.3 g** (measured) | Pro: Cheapest seen historically — $17.13/ea in bulk, the standard the build group ran for years (16 acquired across 5 orders, see [`Deals/servos.md`](../../Deals/servos.md))<br><br>Con: **Superseded by the PTK 9752TG-D — retired & all 16 units used up.** Friends in the group still run their remaining ones, but no more orders are going in. 21 kg-cm @ 7.4V is on the lower end for the aluminum bell crank + 4S steering load | <img src="src/steering_jx_cls6322hv_servo_weight.jpg" width="500"> |

---

## Weight Photos

Verified gram readings off the scale. Drop the inbox photos here as they get routed.

| Servo | Photo | Weight |
|-------|-------|--------|
| PTK 9752TG-D | 🚧 save as `src/steering_ptk_9752tgd_servo_weight.jpg` | TBD |
| JX CLS6336HV | 🚧 save as `src/steering_jx_cls6336hv_servo_weight.jpg` | TBD |
| **JX CLS6322HV** | <img src="src/steering_jx_cls6322hv_servo_weight.jpg" width="280"> | **67.3 g** |

---

## Notes

- **Why low-profile matters:** the CF chassis cavity has limited vertical clearance under the upper plate. Standard-height servos can foul; low-profile (~20mm body) clears easily.
- **Pricing context:** all three options are tracked in [`Deals/servos.md`](../../Deals/servos.md) with full order history. The PTK is the cheapest in-bulk; the JX CLS6336HV is the strongest dollar-per-kg if torque becomes the limit.
- **JX failure mode (why PTK is the successor):** the JX CLS6322HVs don't blow up — they **lose the ability to center reliably**. After enough cycles the pot or the centering circuit drifts, so the servo will hold an offset position instead of returning to neutral. **The oldest unit in the bin died this way on 2025-05-31.** That's a track-killing failure (the car pulls one way at rest, eats one tire), and it's the empirical reason the PTK 9752TG-D is the going-forward pick rather than reordering JX.
- **Bell crank cross-reference:** the chosen aluminum bell crank ([`steering_bell_crank_analysis.md`](steering_bell_crank_analysis.md)) does not need the strongest servo on the market — bell-crank stiffness only matters until the servo gets the wheels moving. The PTK's torque is enough headroom; jumping to the CLS6336HV's 36 kg-cm is upgrade-not-required territory.
- **BEC sizing for PTK:** the PTK 9752TG-D pulls a lot of current at peak. The **Castle Mamba X has only a 3A internal BEC**, which has browned out under full-lock steering load with this servo on the E-Revo 1.0. **Verify the ESC's BEC is ≥5A** (or add an external BEC) before running PTK on a new car. The FastAzJato4x4's chosen Fire Phoenix XeRun 120A Enhanced ESC BEC rating needs to be checked — see [`esc_analysis.md`](esc_analysis.md).
