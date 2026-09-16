# Bare-Bones BOM — FastAzJato4x4

**Buy a running Jato 4x4 for $200, then spend ~$460 turning it into this car.** Total **~$660**, against ~$1,110 for the real build.

> This is not the car in [`BOM.md`](BOM.md). That one is the actual build, personal touches and bad decisions included. **This is the cheapest honest route to the same speed**, and it starts from a used 4S truck instead of a box of parts. Every price is a real one from the full BOM or its analysis docs, except the pinion and the battery, which are current retail and linked below.

**The starting point:** a **running Jato 4x4 VXL (90386-4, the 4S model) for $200**. **$200-250 is the real range** — anything priced above that sits unsold, so don't pay it. That comes with the bearings, the diffs, the gearbox housings, the shock towers, the GTR shocks, the body, the wing and its mount, the radio and a working 4S brushless system. **You keep all of it.** What you replace is what makes the car fast and what makes it survive.

## Cost Summary

| Section | Subtotal |
|---|---|
| [Donor Car](#donor-car) | $200.00 |
| [Chassis](#chassis) | $73.17 |
| [Suspension](#suspension) | $51.46 |
| [Hubs & Axles](#hubs--axles) | $81.11 |
| [Drivetrain](#drivetrain) | $57.10 |
| [Steering](#steering) | $84.53 |
| [Electronics](#electronics) | $77.64 |
| [Wheels](#wheels) | $25.45 |
| [Aero & Body](#aero--body) | $10.00 |
| **Total** | **~$660** |
| **Without the battery** | **~$602** |

**The radio, the ESC, the motor and nearly every bearing come with the donor**, which is why this lands near half the full build. **At the top of the donor range ($250) it's ~$710.**

**If you own a printer this drops to ~$651**, since the $10 of printing is about $1 of filament when it's your machine and your time.

---

## Donor Car

| Part | Qty | Source | Price | Doc |
|---|---|---|---|---|
| **Running Traxxas Jato 4x4 VXL, 90386-4**<br><sub>Note: the 4S model, bought used and running. Supplies the bearings, diffs, gearbox housings, shock towers, GTR shocks, body, wing, wing mount, radio and the 4S brushless system. **$200-250 is the market**, above that they don't sell</sub> | 1 | Used, private sale | **$200.00 each** | [Bearings](bearings_reference.md) |

**A Slash 4x4 works too.** The [CF chassis kit](chassis_analysis.md) is a **Slash 4x4 VXL (TRA6808) pattern**, so a Slash 4x4 donor drops onto it natively rather than in spite of it. **The variable is the rear hubs:** depending on the trim you may need to buy EHD rear carriers, and stock **TRA9050** EHD plastic is **$6.00 a pair** at Traxxas (about $6.99 at dealers), hinge pins and screws included. On a trim that already has them, it's a straight swap and costs nothing. Slashes are also more common used than Jatos, so the donor is easier to find.

**Or buy new.** A **base model Jato 4x4 is about $325 new**, $125 over a good used one, for an undamaged car with a warranty and no previous owner's crashes in it. ⚠️ **Check the trim before counting on that number:** if it's the **BL-2S (90154-4)** that's a **2S** brushless system, so add the [MAX10 G2 + 3665SD combo](esc_analysis.md) at **$127** to get the 4S power this build assumes, landing near **$912**. If the $325 car is already 4S-capable, it's **~$785** and nothing else on this list changes.

## Chassis

| Part | Qty | Source | Price | Doc |
|---|---|---|---|---|
| **Carbon fiber chassis kit, Slash 4x4 VXL TRA6808 pattern**<br><sub>Note: non-negotiable, and it **includes the aluminum bulkheads**, so the donor's front and rear bulkheads come straight off. Buying bulkheads separately is $36.99 for the Powerhobby front alone</sub> | 1 | AliExpress, RCTOYFUN | **$73.17 / kit** | [Chassis](chassis_analysis.md) |
| **Front + rear bulkhead tie bars**<br><sub>Note: DIY from scrap aluminum instead of Traxxas 6823</sub> | 2 | DIY | **$0** | [Chassis](chassis_analysis.md#notes) |

## Suspension

**Stock shocks and towers stay.** The donor's GTR XX-Longs are the documented "just fine" fallback, and its towers take the same hits as carbon ones.

| Part | Qty | Source | Price | Doc |
|---|---|---|---|---|
| **FLM26800 extended arms**<br><sub>Note: don't cheap out. The extra ~10mm of track per side is a handling change, not a looks change, and it's why the donor's arms and swaybars come off</sub> | 2 | FLM | **$25.73 / pair** | [Arms](arm_analysis.md) |

## Hubs & Axles

**Front gets the upgrade, rear stays stock plastic.** The rear sees almost no stress, so the donor's plastic carriers are kept and the money goes to the front, where things break.

| Part | Qty | Source | Price | Doc |
|---|---|---|---|---|
| **Integy C26402PURPLE billet C-hubs**<br><sub>Note: pre-EHD plastic-style C-hub, which is what makes it fit the XO-1 steering blocks</sub> | 1 | eBay, jontobitt1118 | **$13.62 / pair** | [Hubs](hub_analysis.md) |
| **GPM XO-1 alloy steering blocks** | 1 | GPM | **$19.16 / pair** | [Hubs](hub_analysis.md) |
| **Aftermarket 17mm splined wheel hubs, E-Revo 1.0 fit**<br><sub>Note: black, 2-3mm wider per corner. Replaces the donor's stock 17mm hexes, which go unused</sub> | 1 | AliExpress | **$8.36 / set of 4** | [17mm hubs](hub_analysis.md#17mm-wheel-hubs-hexes) |
| **Tekno TKR1654-17 front stubs**<br><sub>Note: the M6 stub the long-axle build needs</sub> | 1 | eBay, kool_toyz_4u | **$19.99 / pair** | [Stubs](driveshaft_analysis.md#tekno-stubs-front--rear) |
| **Tekno 5580 rear stubs**<br><sub>Note: bare stubs beat the $25.95 TKR5570-17 kit, whose hexes go unused anyway</sub> | 1 | eBay, mr-retro | **$16.90 / pair** | [Stubs](driveshaft_analysis.md#tekno-stubs-front--rear) |
| **10×15×4 sealed bearings, 6700-2RS**<br><sub>Note: the only bearings you buy. The donor's are 12×18×4, and the Tekno stub conversion changes the four hub corners to 10×15×4 in a sleeve. They sell in 10-packs, so the four you need come with six spares</sub> | 1 | AliExpress | **$3.08 / pack of 10** | [Bearings](bearings_reference.md#what-the-bearings-cost) |
| **3D-printed 18 → 15mm bearing sleeves**<br><sub>Note: printed at home, drops the 10×15×4 into the 18mm hub pocket. Super glue on the outer face of the ring only, then press in</sub> | 1 | DIY | **$0** | [Bearings](bearings_reference.md) |

## Drivetrain

**Diffs, gearbox housings and the center shaft all stay.** Only the four corner driveshafts get replaced, because the extended arms need the length and the stock shafts won't reach.

| Part | Qty | Source | Price | Doc |
|---|---|---|---|---|
| **Steel CV driveshafts, front + rear, knock-off TRA6851R / TRA6852R**<br><sub>Note: replaces all four donor driveshafts, which won't reach the extended arms</sub> | 1 | AliExpress, FengS Store | **$21.10 / set of 4** | [Driveshafts](driveshaft_analysis.md) |
| **Traxxas TRA6752 long output shafts**<br><sub>Note: the knock-off set's own shafts are too short to use</sub> | 4 | Nitro Hobbies | **$8.00 each** | [Driveshafts](driveshaft_analysis.md#2wd-long-cvds--6752-output-shafts-cheap-long-axle-build) |
| **Traxxas TRA6484X hardened steel pinion, 11T mod 1.0**<br><sub>Note: geared down from stock to 10-11T so it runs cool **without a fan**. 5mm bore for the Velineon shaft, set screw included</sub> | 1 | AMain | **$4.00 each** | [Motor](motor_analysis.md) |

## Steering

**All of it gets replaced.** The donor's plastic bell crank, camber links and steering links come off, and the titanium rods are the reason this section isn't cut.

| Part | Qty | Source | Price | Doc |
|---|---|---|---|---|
| **GPM 6845X aluminum bell crank**<br><sub>Note: replaces the stock plastic crank, ships with brass bushings</sub> | 1 | GPM | **$19.98 each** | [Bell crank](steering_bell_crank_analysis.md) |
| **Traxxas TRA3775 Oilite bushings, 5×8×2.5mm**<br><sub>Note: the four main pivots, replacing the ball bearings the GPM crank ships with</sub> | 1 | Traxxas | **$5.00 / pack** | [Bell crank](steering_bell_crank_analysis.md#key-requirements) |
| **GPM RUS416026ST-S servo link + 25T alloy horn**<br><sub>Note: servo horn to bell crank, 6pc set</sub> | 1 | GPM | **$7.61 / set** | [Bell crank](steering_bell_crank_analysis.md) |
| **ACER Racing titanium M4x60 turnbuckles**<br><sub>Note: non-negotiable, and they replace the donor's camber and steering links. They don't bend, so the wear goes onto cheap rod ends instead</sub> | 6 | ACER Racing | **$5.99 each** | [Tie rods](tie_rod_analysis.md) |
| **RPM 80511 long rod ends, white**<br><sub>Note: white has been discontinued since about 2022, but nobody buys white so it's usually cheaper</sub> | 1 | Tammies Hobbies | **$7.00 / pack of 12** | [Tie rods](tie_rod_analysis.md#rod-ends-the-plastic) |
| **Traxxas TRA5525 rod ends**<br><sub>Note: for the hollow balls</sub> | 1 | Traxxas | **$9.00 / pack of 12** | [Tie rods](tie_rod_analysis.md#rod-ends-the-plastic) |

## Electronics

**The ESC, motor and radio all come with the donor.** The only electronics you buy are the servo and a battery.

| Part | Qty | Source | Price | Doc |
|---|---|---|---|---|
| **PTK 9752TG-D servo**<br><sub>Note: replaces the donor's servo. Matches a $130 ProTek at 7.4V, so there's nothing to save here</sub> | 1 | AliExpress, PTK Servo Store | **$19.65 each** | [Servo](servo_analysis.md) |
| **Ovonic 4S 14.8V 6500mAh 120C hardcase**<br><sub>Note: **full length** (138 × 46 × 50mm), so it runs on the **stock battery posts**, no shorty tray needed. Sold as a 2-pack, so that's ~$29 a pack and you get a spare</sub> | 1 | Ovonic US | **$57.99 / 2-pack** | [Battery](battery_analysis.md) |
| **Receiver, mounted on the upper brace**<br><sub>Note: no RX box. The donor's receiver sits on top of the upper brace</sub> | 1 | Donor car | **$0** | [RX box](radio_analysis.md#rx-box-and-how-its-mounted) |

## Wheels

| Part | Qty | Source | Price | Doc |
|---|---|---|---|---|
| **HSP-style 1/8 buggy wheels + tires, 112 × 43mm (86B-801 black / 86W-801 white)**<br><sub>Note: tires and foams already mounted, so one line covers rims, tires and inserts. List $32.26, about $25.45 with coupons stacked. The donor's 1/10 3.0" wheels don't fit the 17mm hubs</sub> | 1 | AliExpress | **$25.45 / set of 4** | [Wheels](wheel_analysis.md) |

## Aero & Body

**The body, wing and wing mount all carry over free**, and the wing mount works because the donor's rear tower is the one it bolts to. The only cost here is the printing.

| Part | Qty | Source | Price | Doc |
|---|---|---|---|---|
| **Stock Jato 4x4 body + wing + TRA9046 wing mount** | 1 | Donor car | **$0** | [Body](aero_analysis.md#body-comparison) |
| **3D-printed body mounts + posts, front + rear**<br><sub>Note: still needed, the CF chassis has no clipless support. Mounts in TPU, posts in PETG, two posts at each end. **~$10 at a local print shop; about $1 of filament if the printer is yours**, which is why this is the one line that depends on who you are</sub> | 1 | Local print shop / DIY | **$10.00 / set** | [3D printed mounts](aero_analysis.md#3d-printed-body-mounts) |

---

## What comes off the donor and doesn't go back on

These are the parts you're buying past, so they become spares or resale. Worth listing them because a parted-out set claws back some of the $200.

| Donor part | Replaced by | Why |
|---|---|---|
| Stock arms | **FLM26800 extended arms** | ~10mm more track per side |
| Camber + steering links | **ACER titanium turnbuckles** | Stock links bend, titanium doesn't |
| Swaybars | nothing | Not run on this setup |
| Stock 17mm hexes | **Aftermarket splined 17mm hubs** | 2-3mm wider per corner, and they suit the Tekno stubs |
| Front + rear bulkheads | **CF chassis kit** | The kit includes alloy bulkheads |
| All four driveshafts | **Knock-off CVDs + TRA6752 shafts** | Stock shafts can't reach the extended arms |
| Stock plastic bell crank | **GPM 6845X alloy + TRA3775 bushings** | Plastic crank flexes, bearings chew the post |
| Stock servo | **PTK 9752TG-D** | Cheap and genuinely strong |
| Stock chassis | **CF chassis** | Lighter, stiffer, bulkheads included |

## What you don't cheap out on

- **CF chassis kit ($73.17).** Includes the aluminum bulkheads, so the "cheap" alternative costs more once you add them.
- **FLM26800 arms ($51.46).** The extra track changes how the car handles.
- **ACER titanium turnbuckles ($35.94).** They don't bend or snap, and the wear lands on $7 plastic rod ends instead.
- **Front alloy C-hubs and steering blocks ($32.78).** The front is where things break. The rear is plastic precisely because it doesn't.
- **PTK servo ($19.65).** Already the budget pick.

## Worth adding when you can

None of these are needed to drive it, so they're outside the $649.

| Part | Cost | Why |
|---|---|---|
| Diff oils, 30k front / 10k rear / 100k center | **$23.00** | The donor's diffs are filled with whatever's in them. This is the cheapest handling change on the car |
| Shock oils, 37.5wt front / 50wt rear | **$19.98** | The GTRs come filled with 30wt, which is fine to start |
| B'LASTER white lithium grease | **$6.99** | On the CVDs and gears |
| RPM 81042 wide front bumper | **$9.95** | More bumper than stock, and the front is what hits things |
| Kforce 26013 tires | **$3.87** | The cheapest part on the car and one of the ones that decides how it drives |

## What this doesn't buy you

**The full build's shocks, carbon rear tower, chrome rims, alloy rear carriers, touchscreen radio and race battery.** It's the same platform, the same geometry and very nearly the same speed, with the fun tax left off. For what that tax actually bought, see [Building It Cheaper](README.md#building-it-cheaper) in the README.
