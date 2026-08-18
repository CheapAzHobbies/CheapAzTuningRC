# FastAzJato4x4 — Build Analysis Checklist

Working tracker of which part analyses are done, in progress, or still to write.
Each item becomes a `<part>_analysis.md` following the format in [`CLAUDE.md`](../../CLAUDE.md).

---

## ✅ Done

- [x] **Motor**, `motor_analysis.md`
- [x] **ESC**, `esc_analysis.md`
- [x] **Shocks** (+ springs / pistons / oil / rebuild parts, stock GTR fallback), `shock_analysis.md`
- [x] **Shock tower**, `shock_tower_analysis.md`
- [x] **Suspension arms** (+ shock guards), `arm_analysis.md`
- [x] **Chassis**, `chassis_analysis.md`
- [x] **Differential** (+ center diff, spur gear, diff oil), `differential_analysis.md`
- [x] **Driveshafts** (+ center driveshaft), `driveshaft_analysis.md`
- [x] **Gearbox / diff housing**, `gearbox_housing_analysis.md`
- [x] **Bumpers**, `bumper_analysis.md`
- [x] **Aero** (wing + wing mount), `aero_analysis.md`
- [x] **Body / shell**, in [`aero_analysis.md`](aero_analysis.md#body-comparison): JConcepts P2 (0684) leaning, Jato 3.3 red in hand, Traxxas OEM fallback
- [x] **Swaybars** — **decided: none** (track works better without them), `swaybar_analysis.md`
- [x] **Bearings** — OG stock-kit list + as-built modded (four **10×18×5** hub bearings for the Tekno-stub axles, confirmed; brass/alu sleeve alt noted), `bearings_reference.md`
- [x] **Steering knuckles / C-hubs + rear axle carriers**, Traxxas Raptor R Ultimate alloy purchased, `hub_carrier_analysis.md`
- [x] **Tie rods + camber links**, ACER titanium M4×60 turnbuckles (all 6 links, purchased) + RPM white long rod ends (running the cheap ones), `tie_rod_analysis.md`
- [x] **Steering bell crank**, GPM aluminum 6845X, in hand, `steering_bell_crank_analysis.md`
- [x] **Servos**, PTK 9752TG-D metal high-speed, in hand (8-pack bulk), `servo_analysis.md`
- [x] **Wheel hexes**, front Tekno TKR1654-17 + rear TKR5570-17 SCT410 kit (star 17mm hexes), `wheel_hex_analysis.md`

---

## 🔨 In progress — needs finishing

- Nothing open right now.

---

## 📝 To do — no doc yet

### Wheels & tires
- [ ] **Wheels + tires**, biggest single gap. **Plan: Traxxas Jato 4x4 VXL rims (17 mm hex, 3.0") + RedSpider tires**, same setup as [Mike's Jato](../Jato4x4_Mike/README.md#wheels--tires).

### Drivetrain
- [ ] **Pinion gear / final drive ratio**, **16/17/18T (5mm bore) came with the metal center diff** ($0), just pick one for the 3665SD 2400KV (spur already covered in the diff doc). [Pinion reference](motor_analysis.md#pinion-reference-32p)

### Electronics
- [ ] **Battery**, pack selection for this car (capacity / C-rating / size-fit in the CF chassis); the shared `batteries/` is just a tracker
- [ ] **Radio / receiver**, FlySky FGr4S V2 is "Considering" in the BOM

---

## 🔧 Loose ends / cleanups

- [ ] Buy the **TKR5570-17 rear kit** for the rear 17mm hexes (5580 stubs already in hand)
- [ ] Confirm the **AliExpress steel diffs** (front + rear) in hand vs still to-buy
- [ ] Source the **10×18×5 hub bearings** (or the alu/SS sleeve + 10×15×4 alternative) — spec confirmed and fitted
- [ ] README: keep synced as the open picks (wheels/tires, pinion, battery, radio) finalize
- [ ] Confirm the genuine Apache C1 body material vs the Amazon "aluminum" listing field
