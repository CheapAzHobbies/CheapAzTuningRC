# FastAzJato4x4 — Build Analysis Checklist

Working tracker of which part analyses are done, in progress, or still to write.
Each item becomes a `<part>_analysis.md` following the format in [`CLAUDE.md`](../../CLAUDE.md).

---

## ✅ Done

- [x] **Motor** — `motor_analysis.md`
- [x] **ESC** — `esc_analysis.md`
- [x] **Shocks** (+ springs / pistons / oil / rebuild parts) — `shock_analysis.md`
- [x] **Shock tower** — `shock_tower_analysis.md`
- [x] **Suspension arms** (+ shock guards) — `arm_analysis.md`
- [x] **Chassis** — `chassis_analysis.md`
- [x] **Differential** (+ center diff, spur gear, diff oil) — `differential_analysis.md`
- [x] **Driveshafts** (+ center driveshaft) — `driveshaft_analysis.md`
- [x] **Gearbox / diff housing** — `gearbox_housing_analysis.md`
- [x] **Bumpers** — `bumper_analysis.md`
- [x] **Aero** (wing + wing mount) — `aero_analysis.md`
- [x] **Swaybars** — **decided: none** (track works better without them) — `swaybar_analysis.md`
- [x] **Bearings** — reference list of sizes + locations, not a tuning call — `bearings_reference.md`
- [x] **Steering knuckles / C-hubs + rear axle carriers** — Traxxas Raptor R Ultimate alloy purchased — `hub_carrier_analysis.md`

---

## 🔨 In progress — needs finishing

- [ ] **Steering bell crank** — `steering_bell_crank_analysis.md` exists but is all placeholder images and candidate-stage. Add real photos, lock a pick.

---

## 📝 To do — no doc yet

### Steering & front end
- [ ] **Servos** — PTK 9752TG-D is In Hand; write it up + alternatives, BEC/voltage needs, speed vs torque
- [ ] **Tie rods / turnbuckles** — pull in the **4mm front-rod upgrade** note from `arm_analysis.md`; front snaps stock rods on hard hits *(the fun one)*

### Wheels & tires
- [ ] **Wheels + tires** — biggest single gap. **Plan: Traxxas Jato 4x4 VXL rims (17 mm hex, 3.0") + RedSpider tires**, same setup as [Mike's Jato](../Jato4x4_Mike/README.md#wheels--tires).
- [ ] **Wheel hex hubs** — leaning Tekno OEM 17mm hex (from TKR1654-17 kit, pin-through); TRA6469 alt in hand (5.9g) but not yet chosen — `driveshaft_analysis.md#tekno-stubs-front--rear`

### Drivetrain
- [ ] **Pinion gear / final drive ratio** — gearing for the chosen motor/KV (spur already covered in the diff doc)

### Electronics
- [ ] **Battery** — pack selection for this car (capacity / C-rating / size-fit in the CF chassis); the shared `batteries/` is just a tracker
- [ ] **Radio / receiver** — FlySky FGr4S V2 is "Considering" in the BOM

### Body
- [x] **Body / shell** — covered in [`aero_analysis.md`](aero_analysis.md#body-comparison): JConcepts P2 (0684) leaning, Traxxas OEM 9018 family fallback

---

## 🔧 Loose ends / cleanups

- [ ] Fill the remaining image placeholders (steering bell crank rows)
- [ ] README: fill in part numbers + costs, finalize motor spec, add photos
- [ ] Confirm the genuine Apache C1 body material vs the Amazon "aluminum" listing field
