# Traxxas Jato 4x4 — Mike's

> Mike's car. Related to but not the same as the [FastAzJato4x4](../FastAzJato4x4/README.md) build (which is co-developed with Mike). Setup notes recorded here for reference and cross-build tuning.

---

## Table of Contents

- [Car Overview](#car-overview)
- [Suspension](#suspension)
- [Drivetrain](#drivetrain)
- [Electronics](#electronics)
- [Tuning Notes](#tuning-notes)
- [TODO / Notes](#todo--notes)

---

## Car Overview

**Base Car:** Traxxas Jato 4x4 — Mike's personal build.

> Originally noted as "Slash" — it's actually a Jato 4x4. Shares lineage / tuning notes with my FastAzJato4x4 but is its own car.

---

## Suspension

### Shock Oil

| Position | Weight |
|----------|--------|
| Front | 45wt |
| Rear | 60wt |

### Pistons

| Position | Piston |
|----------|--------|
| Front | 6 hole × 1.4 |
| Rear | 6 hole × 1.2 |

---

## Drivetrain

| Position | Part |
|----------|------|
| Pinion | **11T 32P** |

---

## Electronics

| Component | Part |
|-----------|------|
| Motor | **Castle Creations 1412 3200KV** |

---

## Tuning Notes

**11T 32P pinion + Castle 1412 3200KV is the keeper combo.**

Original intuition was that **higher RPM** = better air control, so a smaller pinion was the obvious move. Real-world finding: **torque matters as much as RPM** — the smaller pinion lets the motor reach the **top of its power band more easily**, which makes mid-air corrections feel just as responsive as the high-RPM theory promised, *and* keeps the motor cooler because it's not lugging.

Subjective on-track:
- **Motor runs noticeably cooler** vs the previous taller gearing
- **Power band lands where it's useful** — more usable thrust through the whole throttle, not just at the top
- **"WOOOOO" sound is higher than ever before** — the motor is actually getting up into its happy RPM range
- **Car feels lighter and faster overall** — less effort everywhere, throttle response sharper

Cross-reference for the FastAzJato4x4 pinion decision (currently TBD): the 11T 32P / 3200KV combo on this Jato is the empirical data point that pinion sizing is **not** purely a top-speed equation — gearing for the power-band sweet spot beats gearing for theoretical max RPM.

---

## TODO / Notes

- [ ] Confirm chassis / hub / arm setup vs FastAzJato4x4
- [ ] Add electronics + drivetrain details
- [ ] Add photos
