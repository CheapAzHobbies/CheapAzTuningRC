# Shock Selection — E-Revo 1.0

> **Chosen: Hot Bodies D8 97mm metal big bore (16mm bore)** — metal is deliberately the pick here, the opposite of the lighter plastic route on the [FastAzJato4x4](../FastAzJato4x4/shock_analysis.md). The E-Revo is a heavier truck, and the metal bodies let me **shim the shock end centered on the rocker with M3×1 mm shims**, while **RPM plastic push-rod rod ends** soak up all the stretch and abuse — cheap, repeatable maintenance. Running **4-hole 1.2 mm pistons** with **90wt front / 100wt rear** oil. The D8 is the same shock as the HPI Apache C1 (its plastic twin).

<p align="center"><img src="src/suspension_hb_d8_shocks_hbs67296.jpg" width="600"><br><em>Hot Bodies D8 97mm metal big bore (HBS67296) — 16mm bore, threaded body</em></p>

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Shock Comparison](#shock-comparison) — D8 metal vs plastic twins vs stock
- [Setup Spec — Piston & Oil](#setup-spec--piston--oil) — baseline, my numbers, and the why
- [Why Heavier Oil](#why-heavier-oil) — temperature stability vs shock fade
- [Linkage — Shimming & Rod Ends](#linkage--shimming--rod-ends)
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **97 mm big-bore (16 mm) class** | Must | Matches E-Revo ride height + travel; gives the plush, consistent damping the chassis needs |
| **Metal body** | Must (here) | Lets the shock end be shimmed centered on the rocker with M3×1 shims, and survives heavy-truck crashes without denting |
| **Threaded body** | Must | Adjustable preload is the point of an aftermarket shock |
| **Rebuildable** | Must | Comes apart to service — rebuild when one leaks or breaks, no fixed schedule |
| **Temperature-stable damping** | May | Heavier oil holds its rate as the shock heats up (resists shock fade) |

---

## Shock Comparison

| Shock | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **Hot Bodies D8 97mm** (metal big bore, HBS67296) | Bore: **16 mm**<br><br>Body: **metal**, threaded<br><br>Piston: **4 × 1.2 mm**<br><br>Oil: **90wt F / 100wt R**<br><br>Length: 97 mm shaft | Pro: **Metal body shims clean with M3×1** to center on the rocker, never dents, plush 16mm bore, rebuildable, same shock as the Apache C1<br><br>Con: Heavier than the plastic twin; discontinued (still produced as the Apache C1 / A929) | <img src="src/suspension_hb_d8_shocks_hbs67296.jpg" width="500"> |
| 🔵 **HPI Apache C1 / Wltoys A929** (plastic big bore) | Bore: **16 mm**<br><br>Body: **plastic**, threaded<br><br>Same internals as the D8<br><br>Price: cheap (A929 ~$16/pr) | Pro: **Much lighter**, cheap, identical 16mm bore and internals<br><br>Con: Plastic body flexes and won't take the M3 shim trick as cleanly; less ideal on a heavy truck — better suited to the lighter Jato build | <img src="src/suspension_hpi_shocks_apache_c1_107365.jpg" width="250"> <img src="src/suspension_wltoys_a929_shocks_a929-14.jpg" width="250"><br><em>Apache C1 · Wltoys A929</em> |
| 🚫 ~~**Stock Traxxas GTR** (E-Revo OEM)~~ | Body: aluminum, threaded<br><br>Piston: **2-hole** (OEM)<br><br>Smaller effective flow than the 4×1.2 setup | Pro: Came on the car, big-bore aluminum<br><br>Con: **Superseded by the D8** — the 2-hole OEM piston is the baseline I tuned away from; D8 gives a more tunable big-bore package | <img src="src/suspension_traxxas_gtr_shocks_stock.jpg" width="500"> |

---

## Setup Spec — Piston & Oil

- **Baseline:** the **4-hole 1.2 mm** piston is commonly recommended around **80wt front and rear**.
- **My setup:** **90wt front / 100wt rear.** The extra rear weight helps **prevent bucking and keeps the back of the car planted** over rough terrain. This sits at the **upper end of regular shock-oil weights** — if you'd rather stay in the standard oil range, run a piston with **fewer or smaller holes**.
- **Brand barely matters** — shock oils vary 2–3wt off each other anyway. I like **TLR** oils since they go up to 100wt (probably higher — didn't check).

### Bigger bore → lighter oil (why some go smaller-piston)

Some people drop to a smaller piston to stay on standard shock oils. The E-Revo originally shipped with a **2-hole piston**. The logic sounds backwards but holds: for the *same* hole size and count (e.g. 2-hole 1.3), a **bigger-bore shock has to force more oil through those holes** than a smaller one — so the bigger shock can run **lighter oil** to match the smaller (OG) shock's feel. For example, where a smaller shock wants ~**55wt**, a bigger-bore shock can run **40–45wt** with similar characteristics.

---

## Why Heavier Oil

I run at the top of the oil range on purpose: **heavier oil is significantly more temperature-stable**. It holds its damping rate across weather swings and resists **shock fade** — as the oil heats up during a run, a shock becomes less effective, and lighter oils lose their rate faster. The small consistency tax of running thick oil is worth it for damping that feels the same lap 1 and lap 10.

---

## Linkage — Shimming & Rod Ends

- **Metal D8 bodies shim easily with M3×1 mm shims** to keep the shock end **centered on the rocker** — clean, repeatable, and only possible because the body is metal (plastic flexes and won't hold the shim stack as precisely).
- **Push-rod rod ends are RPM (plastic)**, so all the stretch and abuse in the linkage is **consolidated onto a cheap, quick-swap part**. Same philosophy as the [aluminum rockers](rocker_analysis.md) — push wear onto whatever's cheapest to replace, and maintenance stays cheap.

---

## Notes

- **D8 = Apache C1.** The metal Hot Bodies D8 (HBS67296) and the plastic HPI Apache C1 are the same shock; the Wltoys A929 is a budget knock-off of the C1. Bodies and most internals interchange — see the [FastAzJato4x4 shock analysis](../FastAzJato4x4/shock_analysis.md) for the full big-bore parts breakdown (spare bodies, maintenance sets, spring charts).
- **Metal here, plastic there.** This build chooses metal for the shim trick + heavy-truck durability; the lighter Jato build chooses the plastic twin for weight. Same shock family, opposite trade-off.
- **Rebuild on condition, not schedule** — service a shock only when it leaks or breaks.
- **Springs:** running the stock D8 spring set (TBD if changed) — note final spring rates here once locked.
