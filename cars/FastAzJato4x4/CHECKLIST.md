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

---

## 🔨 In progress — needs finishing

- [ ] **Steering bell crank** — `steering_bell_crank_analysis.md` exists but is all placeholder images and candidate-stage. Add real photos, lock a pick.

---

## 📝 To do — no doc yet

### Steering & front end
- [ ] **Servos** — PTK 9752TG-D is In Hand; write it up + alternatives, BEC/voltage needs, speed vs torque
- [ ] **Tie rods / turnbuckles** — pull in the **4mm front-rod upgrade** note from `arm_analysis.md`; front snaps stock rods on hard hits *(the fun one)*
- [ ] **Steering knuckles / C-hubs + rear axle carriers** — MonsterKingz 7075 alum set in the BOM

### Wheels & tires
- [ ] **Wheels + tires** — biggest single gap
- [ ] **Hubs / wheel hexes** — stock Jato 4x4 hex vs alum upgrades

### Drivetrain
- [ ] **Pinion gear / final drive ratio** — gearing for the chosen motor/KV (spur already covered in the diff doc)

### Electronics
- [ ] **Battery** — pack selection for this car (capacity / C-rating / size-fit in the CF chassis); the shared `batteries/` is just a tracker
- [ ] **Radio / receiver** — FlySky FGr4S V2 is "Considering" in the BOM

### Body
- [ ] **Body / shell** — `Aero & Body` in the README is still TBD for the body itself

---

## 🔧 Loose ends / cleanups

- [ ] Fill the remaining image placeholders (steering bell crank rows)
- [ ] README: fill in part numbers + costs, finalize motor spec, add photos
- [ ] Confirm the genuine Apache C1 body material vs the Amazon "aluminum" listing field
