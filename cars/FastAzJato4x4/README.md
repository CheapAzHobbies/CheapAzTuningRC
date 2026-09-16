<h1 align="center">FastAzJato4x4 · the "Super Jato"</h1>

<p align="center">
  <img src="src/overview_fastazjato_dirt_tires.jpg" width="720"><br>
  <em>IMEX chrome rims on the $3.87 Mitsubishi-tread tires with blue race foams</em>
</p>

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/status-built%20%26%20running-2ea44f?style=for-the-badge">
  <img alt="Power" src="https://img.shields.io/badge/power-4S%20LiPo-d7263d?style=for-the-badge">
  <img alt="Weight" src="https://img.shields.io/badge/weight-2.868%20kg-444?style=for-the-badge">
  <img alt="Build cost" src="https://img.shields.io/badge/build-~%24876-444?style=for-the-badge">
</p>

<p align="center">
  <b>A custom 4S electric buggy built on a Traxxas Jato 4x4.</b><br>
  Carbon-fiber LCG chassis, FLM extended arms, Hot Bodies D8 big bores and a Hobbywing MAX10 G2 + 3665SD 2400KV, all under an OG Jato 3.3 shell. Built to soak up the ruts at Meldrum Bar.
</p>

<p align="center">
  <img src="src/overview_fastazjato_imex_slicks_side.jpg" width="270">&nbsp;<img src="src/overview_fastazjato_front_detail.jpg" width="270">&nbsp;<img src="src/overview_fastazjato_rear_drivetrain.jpg" width="270"><br>
  <em>The stretched look on the IMEX rally slicks · front bumper and steering · rear shocks and CVDs</em>
</p>

---

## At a Glance

| Area | Setup |
|---|---|
| 🧱 **Chassis** | AliExpress / Cobra Racing carbon-fiber LCG, Slash 4x4 pattern |
| 🔌 **Power** | Hobbywing EZRun MAX10 G2 140A + 3665SD G3 2400KV |
| 🔋 **Battery** | Gens Ace Redline 2.0 4S HV 6000mAh 140C shorty (410 g) |
| ⚙️ **Gearing** | 16T pinion on a 54T spur, FDR 3.38 |
| 🌀 **Shocks** | Hot Bodies D8 97mm big bore, 37.5wt front / 50wt rear |
| 🦾 **Arms** | FLM26800 metal extended, about 10mm wider per side |
| 🎯 **Steering** | PTK 9752TG-D servo, GPM 6845X alloy bell crank, Integy purple C-hubs + GPM XO-1 front blocks, Raptor R rear carriers |
| 🏁 **Body** | Traxxas Jato 3.3 red (5511A) with its own integrated wing |
| 🛞 **Wheels** | IMEX IMX7893 chrome Rally rims, $3.87 Mitsubishi-tread 26013 tires, blue race foams |
| 🔧 **Wheel cost** | ~$52 up front (rims + tires + foams), ~$4 per tire change after that |
| ⚖️ **Weight** | 2.868 kg all up |
| 💰 **Build cost** | ~$876 for the car, ~$1,110 with the battery and radio, see [`BOM.md`](BOM.md) |
| 📍 **Home track** | Meldrum Bar Park, Gladstone OR |

## Table of Contents

- ⚖️ [Weight](#weight)
- 🏁 [Track & Setup Philosophy](#track--setup-philosophy)
- 🌀 [Suspension](#suspension)
- ⚙️ [Drivetrain](#drivetrain)
- 🔌 [Electronics](#electronics)
- 🎯 [Steering](#steering)
- 🛞 [Aero & Body](#aero--body)
- 🛡️ [Bumpers](#bumpers)
- 📚 [Deep Dives](#deep-dives)
- 🧾 [Parts List](#parts-list)
- 💸 [Building It Cheaper](#building-it-cheaper)
- 🖨️ [3D Models](#3d-models)
- ✅ [TODO / Notes](#todo--notes)

---

## Weight

**Fully loaded, all up: 2.868 kg (6.32 lb)**, weighed in pieces on one pan (everything that goes on the car, battery included).

<p align="center"><img src="src/overview_fastazjato_total_weight.jpeg" width="500"><br><em>2.868 kg on the WeighMax, the complete car weighed in pieces</em></p>

Component weights measured so far, all of them in the analysis docs: body shell **160 g** ([`aero_analysis.md`](aero_analysis.md)), CF chassis kit **357.2 g** ([`chassis_analysis.md`](chassis_analysis.md)), MAX10 G2 ESC, 3665SD motor, Zeee 5200 pack **518 g** ([`battery_analysis.md`](battery_analysis.md)). The 2.868 kg weigh-in was on that Zeee; the Gens Ace Redline 6000 now on the car is **410 g**, so it runs about **2.76 kg** all up. The battery alone is about **18% of the all-up weight**, which is why the [pack choice](battery_analysis.md) is judged on grams before capacity.

---

## Track & Setup Philosophy

I run this at the **Meldrum Bar Public RC Car Course** in Meldrum Bar Park (Gladstone, OR), a really blown-out dirt track: deep ruts, choppy braking bumps, dry loose dirt over a hard base. It's **casual / fun racing now** (transponder-timed racing was discontinued), so **no personal transponder is needed**. That surface drives the whole setup. It rewards compliance and forgiveness over outright top speed, so the car is built to soak up the rough and stay planted.

- **Official races are banned there as of Aug 2026.** Organised racing at the park got shut down, so what's left is informal running. The setup philosophy below doesn't change, the track and the way people drive it are the same, there's just no formal event to build for.
- **When it does run, it's open class and no rules.** Everything is fair game in the same heat: buggies, truggies, and 1/5 and monster class like X-Maxx, XRT and the Teknos. Nobody is trying to wreck anybody, but **racing is rubbing**, and with that spread of sizes on one track **landing on someone, or getting landed on, is normal**. A 1/5 or an X-Maxx coming down on this truck is a different kind of load than a crash into dirt. It's most of why durability decides parts here ahead of outright performance.
- **Soft, big-bore suspension.** Hot Bodies D8 metal big-bore shocks on soft springs (white 59gf front, grey 52gf rear) soak up the ruts. Oil is 50wt rear / 37.5wt front (down from an earlier 45wt/60wt), the rear still the firmer of the two to control squat and rebound on the chop. No swaybars, I want the wheels working independently over the bumps.
- **Wide track for stability.** FLM26800 extended arms stretch the track width about 10mm per side, which calms the car over rough ground and adds droop.
- **Diffs tuned for a loose surface.** 30k front to calm torque steer, 10k greased rear for drive off the corner, 100k center (Traxxas TRA5130) to hold drive stability.
- **Geared for punch, not top speed.** 16T pinion (FDR 3.38) on the 3665SD 2400KV keeps it punchy and cooler on a technical, rough track where you rarely hold full throttle.
- **Built to survive crashes.** Metal arms that bend instead of snap, alloy hubs on Tekno stubs (Integy C-hubs + GPM XO-1 blocks up front, Raptor R carriers out back), and a **minimal skid plate at the rear** so a bad landing lets me throttle out instead of digging in and cartwheeling. Up front is the **RPM 81042 wide bumper**, which sounds like the opposite but isn't: **it sits far enough forward that touching it means the car is already too nose down**, and it shouldn't ever get that vertical while racing. In normal driving nothing reaches it, and in a real frontal hit it takes the load instead of the diff.
- **Body:** the OG Jato 3.3 stadium-truck shell, because it looks cool and stands out from every buggy on the track. Its own integrated wing means no separate buggy wing or mount.
- **Wheels:** IMEX 1/8th Rally chrome rims, bought purely because they're baller, and yes I paid extra. The chrome ricer look plus the stretched stance from the extended arms makes it look like an extended-swingarm GSX-R. It looks great and still performs well. Right now they wear the $3.87 Mitsubishi-tread 26013 tires with blue race foams. The glued rally slicks they came with (the glue had gone on the old rims) were great on track and fun to drift, but not for racing.

---

## Suspension

<p align="center">
  <img src="src/suspension_hb_d8_shocks_used_set.jpg" width="190">&nbsp;<img src="src/suspension_flm_rustler_rear_extended_arms_flm26800.jpg" width="190">&nbsp;<img src="src/suspension_shock_tower_traxxas_stock_front_9033.jpg" width="190">&nbsp;<img src="src/suspension_shock_tower_gmaxx_cf.jpg" width="190"><br>
  <em>Hot Bodies D8 big bores · FLM26800 extended arms · stock #9033 front tower · MonsterKingz CF rear tower</em>
</p>

| Component | Part | Notes |
|-----------|------|-------|
| Shocks | **Hot Bodies D8 metal 97mm big bore** (HBS67296), front + rear | Used set, [`shock_analysis.md`](shock_analysis.md) |
| Springs / pistons / oil | White 59gf front + grey 52gf rear · 1.4mm×6 pistons · **37.5wt F (Losi TLR74030) / 50wt R (Associated 5480 FT)** | Springs and pistons came with the D8 set, [`shock_analysis.md`](shock_analysis.md#setup-spec-springs--pistons--oil) |
| Arms | **FLM26800 metal extended**, front + rear | $25.73/pair, [`arm_analysis.md`](arm_analysis.md) |
| Shock standoffs | HB Racing HBS67410, 1 pair (rear CF tower) | [`shock_analysis.md`](shock_analysis.md#shock-standoffs--mounting) |
| Upper shock screws (front) | **Traxxas wheelie bar shoulder screws**, 2 | Pulled from a free TRA5472 Revo bar; rebuy as TRA4976 ($4 for 2), [`shock_tower_analysis.md`](shock_tower_analysis.md#front-shock-mounting-wheelie-bar-shoulder-screws) |
| Shock towers | **Stock Traxxas #9033 front + MonsterKingz (G-Maxx) carbon fiber rear** | Plastic up front, carbon rear sized for the big bores + 67410 standoffs, [`shock_tower_analysis.md`](shock_tower_analysis.md) |
| Swaybars | None | Track works better without them, [`swaybar_analysis.md`](swaybar_analysis.md) |

---

## Drivetrain

<p align="center">
  <img src="src/drivetrain_aliexpress_knockoff_slash4x4_steel_diff.png" width="250">&nbsp;<img src="src/drivetrain_aliexpress_center_diff_alum_steel.jpg" width="250">&nbsp;<img src="src/drivetrain_traxxas_slash_hd_cv_knockoff_tra6851r.jpg" width="250"><br>
  <em>Steel front / rear diffs · metal center diff with 54T spur · HD steel CVDs</em>
</p>

| Component | Part | Notes |
|-----------|------|-------|
| Diffs (front + rear) | **AliExpress knock-off Slash 4x4 steel diffs** (5mm, with I-bar) | 30k front / 10k greased rear, [`differential_analysis.md`](differential_analysis.md) |
| Center diff + spur | **AliExpress metal center diff**, integrated steel 54T spur | Came with 16/17/18T pinions, [`differential_analysis.md`](differential_analysis.md#center-diff) |
| Center diff oil | **Traxxas 100k (TRA5130)** | $8 at Tammies Hobby, [`differential_analysis.md`](differential_analysis.md#center-diff-oil) |
| Grease | **B'LASTER white lithium** | CVDs and gears, not inside the diffs. $6.99 at Harbor Freight, [`driveshaft_analysis.md`](driveshaft_analysis.md#grease-cvds--gears) |
| Pinion | **16T 32P** on the 3665SD 2400KV, FDR 3.38 | 17T / 18T on hand to retune, [`motor_analysis.md`](motor_analysis.md#pinion-reference-32p) |
| Center driveshaft | Jato 4x4 BL-2S take-off shaft (7455) | $2.49, [`driveshaft_analysis.md`](driveshaft_analysis.md#center-driveshaft-comparison) |
| Axle CVDs | Knock-off Slash 4x4 HD steel CV driveshafts, front + rear (TRA6851R / TRA6852R clones, 5mm) + **4× TRA6752 long output shafts** | [`driveshaft_analysis.md`](driveshaft_analysis.md) |
| Stubs | Tekno M6: front **TKR1654-17**, rear **5580** (bought bare) | [`driveshaft_analysis.md`](driveshaft_analysis.md#tekno-stubs-front--rear) |
| 17mm hubs | **AliExpress aftermarket 17mm splined hubs (E-Revo 1.0 fit)**, black, all four corners | $8.36, 2-3mm wider per corner, [`hub_analysis.md`](hub_analysis.md#17mm-wheel-hubs-hexes) |
| Gearbox housings | Traxxas TRA6881 front / TRA6880 rear | $4 each, [`gearbox_housing_analysis.md`](gearbox_housing_analysis.md) |
| Bearings | Hub bearings fitted; full sealed kit still open | [`bearings_reference.md`](bearings_reference.md) |

---

## Electronics

<p align="center">
  <img src="src/electronics_hobbywing_ezrun_max10_g2_hw30102603.jpg" width="190">&nbsp;<img src="src/electronics_hobbywing_ezrun_3665sd_g3.jpg" width="190">&nbsp;<img src="src/electronics_gensace_redline2_4s_6000_140c.png" width="190">&nbsp;<img src="src/electronics_flysky_nb4_radio.jpg" width="190"><br>
  <em>MAX10 G2 ESC · 3665SD G3 motor · Gens Ace Redline 6000 shorty · FlySky Noble NB4</em>
</p>

| Component | Part | Notes |
|-----------|------|-------|
| ESC | **Hobbywing EZRun MAX10 G2 140A** | ✅ bought 2026-06-25 as a $127 combo, [`esc_analysis.md`](esc_analysis.md) |
| Motor | **Hobbywing EZRun 3665SD G3 2400KV** (4-pole) | Came with the combo, [`motor_analysis.md`](motor_analysis.md) |
| Battery | **Gens Ace Redline 2.0 4S HV 6000mAh 140C**, shorty hardcase | 410 g; the spec is a 4S hardcase shorty, [`battery_analysis.md`](battery_analysis.md) |
| Radio / receiver | **FlySky Noble NB4** TX + **FGr4S V2** RX | [`radio_analysis.md`](radio_analysis.md) |

<p align="center"><img src="src/overview_fastazjato_rx_box_battery_layout.jpeg" width="500"><br><em>Receiver box and battery layout</em></p>

---

## Steering

<p align="center">
  <img src="src/steering_ptk_9752tgd_servo_dimensions.jpg" width="150">&nbsp;<img src="src/steering_gpm_aluminum_bell_crank_6845x.jpg" width="150">&nbsp;<img src="../K939/src/suspension_integy_caster_block_c26402purple.jpg" width="150">&nbsp;<img src="src/suspension_gpm_xo1_alloy_front_knuckle.jpg" width="150">&nbsp;<img src="src/suspension_traxxas_raptor_r_ultimate_alloy_hubs.jpg" width="150"><br>
  <em>PTK 9752TG-D servo · GPM alloy bell crank · Integy purple C-hub · GPM XO-1 front block · Raptor R (rear carriers used)</em>
</p>

| Component | Part | Notes |
|-----------|------|-------|
| Servo | **PTK 9752TG-D** metal gear, high speed | $19.65, [`servo_analysis.md`](servo_analysis.md) |
| Bell crank | **GPM aluminum bell crank (6845X)** | $19.98, [`steering_bell_crank_analysis.md`](steering_bell_crank_analysis.md) |
| Front C-hubs | **Integy C26402PURPLE** billet alloy, purple | $13.62, originally bought for the K939, [`hub_analysis.md`](hub_analysis.md) |
| Front steering blocks | **GPM XO-1 alloy knuckle** | $19.16, XO-1 bearing geometry suits the Tekno M6 stubs, [`hub_analysis.md`](hub_analysis.md) |
| Rear carriers | **Traxxas Raptor R Ultimate alloy (9065)** | From the $68.73 Raptor R set, [`hub_analysis.md`](hub_analysis.md) |
| Tie rods + camber links | **ACER titanium M4x60** rods (6) + RPM long rod ends (white 80511) + Traxxas hollow balls, ~61mm (96mm c-t-c) | [`tie_rod_analysis.md`](tie_rod_analysis.md) |

---

## Aero & Body

<p align="center">
  <img src="src/body_traxxas_jato33_red_5511a.jpg" width="190">&nbsp;<img src="src/aero_imex_rally_chrome_wheels.png" width="190">&nbsp;<img src="src/aero_generic_tires_mitsubishi_26013.jpg" width="190">&nbsp;<img src="src/aero_closed_cell_foams_blue.jpg" width="190"><br>
  <em>Jato 3.3 red shell · IMEX chrome Rally rims · Mitsubishi-tread 26013 tires · blue closed-cell foams</em>
</p>

| Component | Part | Notes |
|-----------|------|-------|
| Body / shell | **Traxxas Jato 3.3 red (5511A)** | $34.47, clearance holes cut for the tall towers, [`aero_analysis.md`](aero_analysis.md#body-comparison) |
| Wing | The Jato 3.3 shell's own integrated wing | No separate wing or mount, [`aero_analysis.md`](aero_analysis.md#body-comparison) |
| Rims | **IMEX IMX7893 1/8 Rally chrome** (17mm hex) | Bought for the look. A bit narrower than standard, so standard 1/8 tires go on with some finesse. The glued rally slicks came off: fun to drift, not for racing, [`wheel_analysis.md`](wheel_analysis.md#rims-bare-wheels) |
| Tires | **Kforce Mitsubishi-tread 26013** (110 × 43mm, natural rubber, 35°), set of 4 | $3.87 shipped. Softer, but very durable once worn in, [`wheel_analysis.md`](wheel_analysis.md#tires-tire-only-mount-on-your-own-rims) |
| Foam inserts | Blue closed-cell race foams, reusable | Keeps it planted, less rim slap, [`wheel_analysis.md`](wheel_analysis.md#foam-inserts) |

---

## Bumpers

<p align="center">
  <img src="src/bumpers_rpm_wide_front_81042_black.webp" height="220">&nbsp;<img src="src/bumpers_traxxas_skid_plates_tra9044.jpg" height="220"><br>
  <em>RPM 81042 wide front bumper · Traxxas TRA9044 (rear skid plate used)</em>
</p>

| Component | Part | Notes |
|-----------|------|-------|
| Front | **RPM 81042 wide front bumper** (black) | $9.95, [`bumper_analysis.md`](bumper_analysis.md) |
| Rear | **Traxxas TRA9044 skid plate** | From the $7 front + rear set, the only rear plate that covers the tongue, [`bumper_analysis.md`](bumper_analysis.md) |

---

## Deep Dives

Every part choice above was decided in its own analysis doc.

| Suspension | Drivetrain | Electronics | Chassis, Body & Steering | Tracking |
|---|---|---|---|---|
| [Shocks](shock_analysis.md) | [Diffs](differential_analysis.md) | [ESC](esc_analysis.md) | [Chassis](chassis_analysis.md) | [BOM](BOM.md) |
| [Shock towers](shock_tower_analysis.md) | [Driveshafts](driveshaft_analysis.md) | [Motor](motor_analysis.md) | [Body & aero](aero_analysis.md) | [Checklist](CHECKLIST.md) |
| [Arms](arm_analysis.md) | [Gearbox housings](gearbox_housing_analysis.md) | [Battery](battery_analysis.md) | [Bumpers](bumper_analysis.md) | |
| [Swaybars](swaybar_analysis.md) | [17mm hubs](hub_analysis.md#17mm-wheel-hubs-hexes) | [Charger](charger_analysis.md) | [Wheels](wheel_analysis.md) | |
| [Hubs](hub_analysis.md) | [Bearings](bearings_reference.md) | [Radio](radio_analysis.md) | [Bell crank](steering_bell_crank_analysis.md) | |
| | | [Servo](servo_analysis.md) | [Tie rods](tie_rod_analysis.md) | |
| | | [Connectors](connector_reference.md) | | |

---

## Parts List

Every part on the car, with prices, sources and subtotals, lives in **[`BOM.md`](BOM.md)**. It opens with a photo collage of the build.

---

## Building It Cheaper

This car got expensive because I bought the fun, gimmicky stuff. **About $146 of it comes off without changing how the car drives**, and some of the expensive picks genuinely earn their place.

| On the car | Paid | Cheaper option | Cost | Saves |
|---|---|---|---|---|
| HB D8 metal big bores + HBS67410 standoffs | $77.98 | **Stock Jato 4x4 GTR XX-Long** (7462-GRAY), springs included, no standoffs needed, [`shock_analysis.md`](shock_analysis.md) | $22.97 | **$55.01** |
| Gens Ace Redline 6000 shorty | $92.26 | Fido RC Fi58130 5800 shorty, [`battery_analysis.md`](battery_analysis.md) | $55.00 | **$37.26** |
| MonsterKingz CF tower set + #9033 front | $39.29 | **Plastic both ends**: #9033 front + TRA9039 rear, **$6.00 each**, [`shock_tower_analysis.md`](shock_tower_analysis.md) | $12.00 | **$27.29** |
| IMEX chrome rims + Kforce tires + blue race foams | $51.93 | HSP-style swirl wheels, tires **and** foams already on, [`wheel_analysis.md`](wheel_analysis.md) | ~$25.45 | **~$26.48** |
| **Total** | | | | **~$146** |

**That lands the same car near ~$964 all in, or ~$823 without the radio**, against ~$1,110 as built.

> **Taken all the way, that's the [bare-bones BOM](BOM_barebones.md): ~$660.** Buy a **running Jato 4x4 VXL for $200** (the market is $200-250) and spend ~$460 on the parts that actually matter — CF chassis, FLM arms, front alloy hubs, titanium rods, the long-axle conversion and a servo. The donor's ESC, motor, radio, bearings, diffs, shocks, towers, body and wing all stay on the car.

**Rear stubs, confirmed:** buying the **bare rear stubs at $16.90 a pair** beats the $25.95 TKR5570-17 kit, whose hexes go unused since the car runs the $8.36 aftermarket 17mm hubs. **Saves $9.05.**

**Optional, only if you don't care about the look:** a generic AliExpress 1/8 buggy shell runs ~$25 against the $34.47 Jato 3.3 take-off, so **~$9 more**. The OG shell is most of this car's character, so it stays.

### Don't cheap out on these

- **CF chassis kit ($73.17), non-negotiable.** It **comes with the aluminum bulkheads**, so it replaces a separate bulkhead buy (Powerhobby alone is $36.99). Cheaper up front than building the same thing out of a stock chassis plus bulkheads, [`chassis_analysis.md`](chassis_analysis.md).
- **FLM26800 arms ($51.46).** The extra ~10mm of track per side is a handling change, not a looks change, [`arm_analysis.md`](arm_analysis.md).
- **Alloy hubs and carriers.** They're what survives landing on, or under, a 1/5 scale car. Only the *purple* on the Integy C-hubs was a colour pick, [`hub_analysis.md`](hub_analysis.md).
- **ACER titanium turnbuckles ($35.94), non-negotiable.** They don't bend or snap, so they pay for themselves in rods you never rebuy. The wear goes on **cheap plastic rod ends** instead (RPM white 80511, ~$7-9 for 12), which is the whole point: break the part that costs a few dollars, [`tie_rod_analysis.md`](tie_rod_analysis.md).
- **MAX10 G2 + 3665SD combo ($127).** Matched pair, no sensor adapter, and it sets the ceiling for the whole drivetrain.
- **Kforce 26013 tires ($3.87).** The cheapest part on the car and one of the ones that decides how it drives.
- **Blue closed-cell race foams ($8.08).** Worth it, but the foams that come in the HSP wheels are only **marginally** worse, so that's a fair place to save.
- **PTK 9752TG-D servo ($19.65).** Already the budget pick, and it matches a $130 ProTek at 7.4V.

### What the fun tax actually bought

- **IMEX chrome rims ($39.98).** Bought purely because they're baller. The HSP set is the same swirl rim with tires on for less.
- **CF rear tower ($33.29).** Light and stiff, and it looks the part, but the plastic tower is $6 and takes the same hits.
- **D8 metal big bores ($73.99).** A real upgrade over the stock GTRs, and also the single biggest line you can cut.

## 3D Models

> STL files live in [`3d-models/`](3d-models/), with the **editable STEP** next to each body part. Print settings, materials and the screws that go with them are in [`aero_analysis.md`](aero_analysis.md#3d-printed-body-mounts).

| Model | Description | Status |
|-------|-------------|--------|
| `SJato_Front_Body_Mount.stl` | Front body mount, **TPU**, 1 off. 80 × 18 × 7 mm | **On the car** |
| `SJato_Rear_Body_Mount.stl` | Rear body mount, **TPU**, 1 off. 55 × 37 × 7 mm | **On the car** |
| `SJato_Front_Body_Post.stl` | Front body post, **PETG**, **2 off**. 20 × 20 × 35 mm | **On the car** |
| `SJato_Rear_Body_Post.stl` | Rear body post, **PETG**, **2 off**. 20 × 20 × 48 mm | **On the car** |
| 18 → 15 mm bearing sleeve | Drops a common 10×15×4 into the 18 mm hub pocket, so nothing has to be shaved. Glue the outer face of the ring only and press it in, [`bearings_reference.md`](bearings_reference.md) | **On the car** |
| `JatoE_Wing_Mount.stl` | Wing mount, printed. Not fitted, since the Jato 3.3 shell carries its own integrated wing | Spare / for a buggy body |
| Custom front-end shroud / wing mount + Rustler bumper integration | Cosmetic shroud that integrates the Rustler 4x4 front bumper (better crash protection, ugly stock) into a clean wing mount. Discussed in [`bumper_analysis.md`](bumper_analysis.md#notes) | Idea / TODO |

## TODO / Notes

- [x] Rear Tekno 5580 stubs + aftermarket 17mm hubs
- [x] Bearings costed out: **$7.21** for the car's 18, bought by size in 10-packs, [`bearings_reference.md`](bearings_reference.md#what-the-bearings-cost)
- [x] Motor locked in: Hobbywing 3665SD G3 2400KV
- [x] Full-car build photos
