# Jato 4SS — Build Analysis Checklist

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
- [x] **Aero / body** — **Jato 3.3 shell (5511A red) chosen**, its integrated wing replaces the buggy wing; the AliExpress wing + TRA9046 mount dropped to spares. JConcepts P2 buggy-body fallback. `aero_analysis.md`
- [x] **Swaybars** — **decided: none** (track works better without them), `swaybar_analysis.md`
- [x] **Bearings** — OG stock-kit list + as-built modded (four **10×15×4** hub bearings in an 18→15mm sleeve for the Tekno-stub axles, confirmed; bare 10×18×5 noted as the alternative). **Costed: $7.21 for the car's 18**, priced per bearing from the 10-packs, plus $5.00 of TRA3775 bushings. Sleeve fitting written up, `bearings_reference.md`
- [x] **Steering knuckles / C-hubs + rear axle carriers**, Traxxas Raptor R Ultimate alloy purchased, `hub_analysis.md`
- [x] **Tie rods + camber links**, ACER titanium M4×60 turnbuckles (all 6 links, purchased) + RPM white long rod ends (running the cheap ones), `tie_rod_analysis.md`
- [x] **Steering bell crank**, GPM aluminum 6845X, in hand, `steering_bell_crank_analysis.md`
- [x] **Servos**, PTK 9752TG-D metal high-speed, in hand (8-pack bulk), `servo_analysis.md`
- [x] **17mm hubs**, AliExpress aftermarket 17mm splined hubs (E-Revo 1.0 fit) (black) on Tekno M6 stubs (front TKR1654-17, rear 5580), `hub_analysis.md`
- [x] **Wheels / tires** — **IMEX IMX7893 chrome rims + Mitsubishi-tread 26013 tires + blue closed-cell foams** mounted (17mm hex), `wheel_analysis.md`
- [x] **Battery** — **Gens Ace Redline 2.0 4S HV 6000mAh shorty (410 g), 2 bought Aug 31 2026.** Supersedes the earlier ~5200 target: the 6000 HV shorty won on **4S2P** construction (two cells paralleled per series group, so roughly half the internal resistance) at a weight that turned out fine. Fido Fi58130 at $55 is the value pick if buying again, `battery_analysis.md`
- [x] **Radio / receiver** — FlySky Noble NB4 + FGr4S V2 RX, in hand, `radio_analysis.md`
- [x] **Connectors** — EC5 stock; EC5/XT60/XT90 good, Deans/Tamiya avoided, `connector_reference.md`
- [x] **Charger** — HOTA T6 / SKYRC B6ACneo / B6neo+ / ToolkitRC M7 (all LiHV), `charger_analysis.md`
- [x] **BOM** — every part on the car priced, **~$1,115 total / ~$881 car only**. Sections in build order, axles with the drivetrain, `BOM.md`
- [x] **Bare-bones BOM** — the cheap route: **$200 running donor + ~$465 of parts = ~$665**. Donor options for any Traxxas 4x4, buy-new tiers, and a parts collage, `BOM_barebones.md`
- [x] **3D printed parts** — front + rear body mounts (TPU) and two posts each end (PETG), STL + editable STEP; plus the 18→15mm bearing sleeve, `aero_analysis.md` + `3d-models/`

---

## 🔨 In progress — needs finishing

- Nothing open right now.

---

## 📝 To do — no doc yet

- **All part analyses are written.** What's left is build / purchase (see loose ends) and track tuning, not new docs.

---

## 🔧 Loose ends / cleanups

- [x] **Rear Tekno 5580 stubs**, bought bare (no TKR5570-17 kit needed)
- [x] Hub bearings sorted: **10×15×4 in an 18→15mm sleeve**, fitted and running. Bare **10×18×5** is the alternative if the sleeve ever comes out
- [x] README synced: wheels/tires, pinion, battery and radio are all settled, and the cost figures track the BOM rows
- [ ] Confirm the **AliExpress steel diffs** (front + rear) in hand vs still to-buy
- [ ] Confirm the genuine Apache C1 body material vs the Amazon "aluminum" listing field

> **Not tracked here: things the analysis docs already mark as unknown.** If a spec isn't published, the doc says so where the part lives, and a reader finds it there rather than in a task list. That covers the **unstated bore** on the alloy big-bore shocks ([`shock_analysis.md`](shock_analysis.md)), the **TQ/TQi rebuild bearing sizes** ([`../../controllers/README.md`](../../controllers/README.md)), and which trim the **$325 new base Jato** is, where [`BOM_barebones.md`](BOM_barebones.md) simply carries both totals. **Stock levels aren't tracked at all**, in this file or in the analysis docs. A part's price and whether it's **discontinued** are lasting facts; whether a shop happens to have one today isn't, and it goes stale the moment it's written.
