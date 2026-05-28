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
| **Accepts standard Traxxas Jato 4x4 parts** | Must | Gearbox housings, bulkheads, shock mounts, bumper mounts — all stock Traxxas hardware must bolt on without modification |
| **Carbon fiber** | May | Light + stiff, ideal for this build — but the hard requirement is fit, not material |
| **Cheap** | May | Arms are the intended fuse, chassis should last — but ≤$150 keeps the "just buy another one" option open if something goes wrong |
| **Available without 2-month wait** | May | AliExpress and similar sellers ship in 2-4 weeks |

---

## Chassis Comparison

| Chassis | Material | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **AliExpress / Temu CF chassis** (fits TRA6808 Slash 4x4 VXL) | 3K carbon fiber, ~4mm | **Chosen** | Pro: **~$100 or less**. Direct fit to the Slash 4x4 chassis pattern that the Jato 4x4 shares. Light + stiff. Easy to replace if needed<br><br>Con: QC varies between sellers; CF quality not always spec'd; no warranty | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/chassis_aliexpress_cf_slash_4x4.jpg` |
| ~~Traxxas stock plastic chassis~~ | Composite nylon | **Vetoed** | Pro: Free (in box with the Jato 4x4), bulletproof in crashes<br><br>Con: Heaviest option, the entire point of the build is to swap this for something stiffer + lighter | (use stock car photo) |
| ~~Premium CF chassis (Pro-Line, Exotek, Avid)~~ | Premium 3K CF | **Vetoed** | Pro: Best CF quality, fitment tested<br><br>Con: $200-400 for a part that gets crashed regularly. Cost doesn't justify the QC bump for this build | — |
| ~~Aluminum chassis~~ | 7075-T6 | **Ruled Out** | Pro: Most durable<br><br>Con: Way too heavy. Aluminum chassis adds weight in the worst place (low and central, killing acceleration / handling) | — |

---

## Notes

- **Why TRA6808 fit pattern works:** the Slash 4x4 VXL and the Jato 4x4 share the same gearbox housings, bulkhead spacing, and shock mount geometry. A Slash 4x4 CF chassis bolts up to a Jato 4x4 drivetrain without modification.
- **Chassis is not disposable — arms are the fuse.** FLM extended arms bend and reshape before real chassis damage occurs (see [`arm_analysis.md`](arm_analysis.md)). The whole build is light, so less kinetic energy reaches the chassis in a crash vs a heavy 1/8 truck. The cheap price is a bonus, not the operating assumption.
- **QC tip:** if buying from AliExpress, look for sellers with 95%+ positive feedback and >100 sold; avoid the brand-new listings. Photos in customer reviews are more honest than seller-supplied images.
