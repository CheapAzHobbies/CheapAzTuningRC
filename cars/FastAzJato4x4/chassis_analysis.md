# Chassis Selection — FastAzJato4x4

> **Chosen: AliExpress carbon fiber chassis** (fits Traxxas Slash 4x4 VXL TRA6808 family) — ~$100 or less. The chassis the entire FastAzJato4x4 build is named after. Cheap enough that "if it doesn't work I'll just buy another one" is a valid attitude.

---

## Table of Contents

- [Key Requirements](#key-requirements) — Must / May for the chassis pick
- [Chassis Comparison](#chassis-comparison) — every option considered
- [Notes](#notes) — fitment + "send it" reasoning

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Fits Slash 4x4 / Jato 4x4 mount points** | Must | Has to accept the gearbox housings, bulkheads, and shock mounts from the Traxxas drivetrain |
| **Carbon fiber** | Must | Light + stiff. The whole point of the custom-chassis build |
| **Cheap enough to be disposable** | May | Crashing CF chassis is a fact of life. ≤$150 = "send it"; $300+ = "preserve at all costs" |
| **Available without 2-month wait** | May | AliExpress and similar sellers ship in 2-4 weeks |

---

## Chassis Comparison

| Chassis | Material | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **AliExpress / Temu CF chassis** (fits TRA6808 Slash 4x4 VXL) | 3K carbon fiber, ~4mm | **Chosen** | Pro: **~$100 or less** — cheap enough to risk. Direct fit to the Slash 4x4 chassis pattern that the Jato 4x4 shares. Light + stiff. Disposable in a crash, easy to replace<br>Con: QC varies between sellers; CF quality not always spec'd; no warranty | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/chassis_aliexpress_cf_slash_4x4.jpg` |
| ~~Traxxas stock plastic chassis~~ | Composite nylon | **Vetoed** | Pro: Free (in box with the Jato 4x4), bulletproof in crashes<br>Con: Heaviest option, the entire point of the build is to swap this for something stiffer + lighter | (use stock car photo) |
| ~~Premium CF chassis (Pro-Line, Exotek, Avid)~~ | Premium 3K CF | **Vetoed** | Pro: Best CF quality, fitment tested<br>Con: $200-400 for a part that gets crashed regularly. Cost doesn't justify the QC bump for this build | — |
| ~~Aluminum chassis~~ | 7075-T6 | **Ruled Out** | Pro: Most durable<br>Con: Way too heavy. Aluminum chassis adds weight in the worst place (low and central, killing acceleration / handling) | — |

---

## Notes

- **Why TRA6808 fit pattern works:** the Slash 4x4 VXL and the Jato 4x4 share the same gearbox housings, bulkhead spacing, and shock mount geometry. A Slash 4x4 CF chassis bolts up to a Jato 4x4 drivetrain without modification.
- **Chassis is hopefully NOT actually disposable.** The original framing ("cheap enough to risk") was a worst-case attitude. The expected reality:
  - **Arms give way first** — FLM extended arms are bendable, take the hit, get reshaped back, keep driving (see [`arm_analysis.md`](arm_analysis.md))
  - **The whole build is light** — less mass = less kinetic energy in any given crash = less force into the chassis. A light car bouncing off something at 35 mph delivers less energy to the chassis than a heavy 1/8 truck would
  - **The minimal-bumper choice is a calculated risk**, not a "the chassis is disposable so whatever" attitude. Going [TRA9044 minimal-profile bumpers](bumper_analysis.md) accepts that some chassis hits will sneak through in exchange for cartwheel recovery
  - Net effect: the CF chassis should last considerably longer than the cheap price suggests, and "disposable" is really the fallback plan rather than the operating assumption
- **QC tip:** if buying from AliExpress, look for sellers with 95%+ positive feedback and >100 sold; avoid the brand-new listings. Photos in customer reviews are more honest than seller-supplied images.
