# Chassis Selection — FastAzJato4x4

> **Chosen: AliExpress carbon fiber chassis** (fits Traxxas Slash 4x4 VXL TRA6808 family) — ~$100 or less. The chassis the entire FastAzJato4x4 build is named after. Mounts all standard Traxxas Jato 4x4 parts directly.

---

## Table of Contents

- [Key Requirements](#key-requirements) — Must / May for the chassis pick
- [Chassis Comparison](#chassis-comparison) — every option considered
- [Notes](#notes) — fitment + "send it" reasoning

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Jato 4x4 / Slash 4x4 chassis pattern** | Must | Must be specifically for the 4x4 platform — 2WD chassis have different mount spacing and will not work |
| **Accepts standard Traxxas Jato 4x4 parts** | Must | Gearbox housings, bulkheads, shock mounts, bumper mounts — all stock Traxxas hardware must bolt on without modification |
| **Carbon fiber** | May | Light + stiff, ideal for this build — but the hard requirement is fit, not material |
| **Cheap** | May | Arms are the intended fuse, chassis should last — but ≤$150 keeps the "just buy another one" option open if something goes wrong |
| **Available without 2-month wait** | May | AliExpress and similar sellers ship in 2-4 weeks |

---

## Chassis Comparison

| Chassis | Material | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **AliExpress / Cobra Racing CF Chassis Kit** (fits TRA6808 / 6087 / 6804 Slash 4x4 VXL) | Material: Genuine carbon fiber + aluminum alloy (not fiberglass or CF-look plastic)<br>Type: LCG (Low Center of Gravity)<br>Includes: alum front+rear bulkheads, adjustable alum motor mount (3S–8S), alum battery holder + strap, alum servo mount, CF center brace, all hardware + schematic<br>Motor fit: VXL-3s, 550 type, Castle 1515 + similar<br>Install: no cutting/drilling, ~60–90 min<br>Tested: large pinion gear-up to 125 MPH<br>Sold as: same kit under multiple brand names (AliExpress generics, Cobra Racing, etc.) | **Chosen** | Pro: **~$100 or less**. Complete kit — no separate bulkhead, motor mount, or servo mount purchases needed. Genuine CF, significantly lighter than aluminum. Direct fit to Slash 4x4 / Jato 4x4 pattern. Castle 1515 compatible. Easy to replace if needed<br><br>Con: QC varies between sellers; no warranty. **Weight vs OEM plastic unconfirmed** — kit has aluminum components throughout; needs a weigh-in to verify it's actually lighter than stock | <img src="src/chassis_aliexpress_cf_slash_4x4.png" width="500"> |
| ~~Traxxas OEM HCG chassis (6822)~~ | Composite nylon<br>Type: HCG (High Center of Gravity) | **Vetoed** | Pro: Free (in box with Jato 4x4), tough in crashes<br><br>Con: High center of gravity hurts handling. Heavier and less stiff than CF. Whole point of this build is to replace it | <img src="src/chassis_traxxas_oem_hcg_6822.jpg" width="500"> |
| ~~Traxxas OEM LCG chassis (TRA7422)~~ | Composite nylon<br>Type: LCG (Low Center of Gravity) | **Vetoed** | Pro: Lower CG than HCG version — better handling than standard. Tough in crashes<br><br>Con: Still plastic and heavier/less stiff than CF. The CF kit is also LCG, so no reason to stay on plastic | <img src="src/chassis_traxxas_oem_lcg_tra7422.jpg" width="500"> |
| ~~Premium CF chassis (Pro-Line, Exotek, Avid)~~ | Premium 3K CF | **Vetoed** | Pro: Best CF quality, fitment tested<br><br>Con: $200-400 for a part that gets crashed regularly. Cost doesn't justify the QC bump for this build | — |
| ~~**STRC LCG Chassis — Slash 4×4**~~ | Material: 4mm CNC aluminum lower + 2.5mm graphite upper deck<br>Includes: alum bulkhead, motor mount + cam, rear suspension mounts, battery brackets, servo mount, sway bar mounts, all hardware<br>Price: ~$99<br>Design: 2S lipo / 550 motor (3S compatible w/ possible plug mods)<br>Status: **Discontinued** | Vetoed | Pro: CNC machined, hard anodized, comprehensive kit, LCG design — well engineered for its time. Same price as the CF kit<br><br>Con: **Discontinued.** Aluminum lower chassis also adds weight vs CF | <img src="src/chassis_strc_alum_lcg_slash_4x4.jpg" width="500"> |
| ~~Aluminum chassis~~ | 7075-T6 | **Ruled Out** | Pro: Most durable<br><br>Con: Way too heavy. Aluminum chassis adds weight in the worst place (low and central, killing acceleration / handling) | — |

---

## Notes

- **Why TRA6808 fit pattern works:** the Slash 4x4 VXL and the Jato 4x4 share the same gearbox housings, bulkhead spacing, and shock mount geometry. A Slash 4x4 CF chassis bolts up to a Jato 4x4 drivetrain without modification.
- **Chassis is not disposable — arms are the fuse.** FLM extended arms bend and reshape before real chassis damage occurs (see [`arm_analysis.md`](arm_analysis.md)). The whole build is light, so less kinetic energy reaches the chassis in a crash vs a heavy 1/8 truck. The cheap price is a bonus, not the operating assumption.
- **Aluminum bulkheads included in the kit** — the CF chassis comes with aluminum alloy bulkheads, so no separate purchase needed. Plastic front bulkheads break anyway, so this is a pro. Weight vs OEM still unconfirmed — needs a weigh-in.
- **QC tip:** if buying from AliExpress, look for sellers with 95%+ positive feedback and >100 sold; avoid the brand-new listings. Photos in customer reviews are more honest than seller-supplied images.
