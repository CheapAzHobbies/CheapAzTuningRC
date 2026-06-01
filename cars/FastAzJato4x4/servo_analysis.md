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
| ⭐ **PTK 9752TG-D** | Torque: ~25–50 kg-cm (model-dependent)<br><br>Speed: high (low-profile high-speed digital)<br><br>Gear: metal<br><br>HV: yes<br><br>Weight: TBD (waiting on photo) | Pro: **Already in hand, 8 spares bought at ~$19.65/ea**, well-matched to this build's chosen aluminum bell crank, low-profile fits the CF chassis cavity, HV<br><br>Con: Torque rating is sometimes overstated in PTK marketing; real-world numbers TBD by bench test | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/steering_ptk_9752tgd_servo.jpg` |
| ❌ ~~**JX Ecoboost CLS6336HV** — *predecessor*~~ | Torque: **36 kg-cm**<br><br>Speed: 0.07s / 60°<br><br>Gear: metal<br><br>HV: yes<br><br>Weight: **67.3 g** (measured) | Pro: Big torque number, JX reliability is well documented in heli circles, CNC aluminum housing<br><br>Con: **Superseded by the PTK 9752TG-D** in this build — kept here as the predecessor data point, not as a live candidate. $23.85/ea (cheapest seen) vs ~$19.65 PTK | <img src="src/steering_jx_cls6336hv_servo_weight.jpg" width="500"> |
| ❌ ~~**JX CLS6322HV** — *predecessor, retired from purchase*~~ | Torque: **21 kg-cm**<br><br>Speed: high (coreless digital)<br><br>Gear: metal<br><br>HV: yes<br><br>Weight: TBD (waiting on photo) | Pro: Cheapest seen — $17.13/ea in bulk, JX reliability, coreless = fast, **16 units already in the parts bin** (5 historical orders, see [`Deals/servos.md`](../../Deals/servos.md))<br><br>Con: **Superseded by the PTK 9752TG-D — retired from future purchases.** The existing 16-unit stockpile gets used up, then done. 21 kg-cm is also on the lower end for the aluminum bell crank + 4S steering load | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/steering_jx_cls6322hv_servo.jpg` |

---

## Weight Photos

Verified gram readings off the scale. Drop the inbox photos here as they get routed.

| Servo | Photo | Weight |
|-------|-------|--------|
| PTK 9752TG-D | 🚧 save as `src/steering_ptk_9752tgd_servo_weight.jpg` | TBD |
| **JX CLS6336HV** | <img src="src/steering_jx_cls6336hv_servo_weight.jpg" width="280"> | **67.3 g** |
| JX CLS6322HV | 🚧 save as `src/steering_jx_cls6322hv_servo_weight.jpg` | TBD |

---

## Notes

- **Why low-profile matters:** the CF chassis cavity has limited vertical clearance under the upper plate. Standard-height servos can foul; low-profile (~20mm body) clears easily.
- **Pricing context:** all three options are tracked in [`Deals/servos.md`](../../Deals/servos.md) with full order history. The PTK is the cheapest in-bulk; the JX CLS6336HV is the strongest dollar-per-kg if torque becomes the limit.
- **Bell crank cross-reference:** the chosen aluminum bell crank ([`steering_bell_crank_analysis.md`](steering_bell_crank_analysis.md)) does not need the strongest servo on the market — bell-crank stiffness only matters until the servo gets the wheels moving. The PTK's 25kg+ is enough headroom; jumping to the CLS6336HV's 36kg is upgrade-not-required territory.
