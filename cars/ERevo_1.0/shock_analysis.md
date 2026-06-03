# Shock Selection — E-Revo 1.0

> **Chosen: Hot Bodies D8 97mm metal big bore (16mm bore)** — metal is deliberately the pick here, the opposite of the lighter plastic route on the [FastAzJato4x4](../FastAzJato4x4/shock_analysis.md). The E-Revo is a heavier truck, and the metal bodies let me **shim the shock end centered on the rocker with M3×1 mm shims**, while **RPM plastic push-rod rod ends** soak up all the stretch and abuse — cheap, repeatable maintenance. Running **4-hole 1.2 mm pistons** with **90wt front / 100wt rear** oil. The D8 is the same shock as the HPI Apache C1 (its plastic twin).

<p align="center"><img src="src/suspension_hb_d8_shocks_hbs67296.jpg" width="600"><br><em>Hot Bodies D8 97mm metal big bore (HBS67296) — 16mm bore, threaded body</em></p>

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Shock Comparison](#shock-comparison) — D8 metal vs plastic twins vs stock
- [Setup Spec — Piston & Oil](#setup-spec--piston--oil) — baseline, my numbers, and the why
- [Why Heavier Oil](#why-heavier-oil) — temperature stability vs shock fade
- [Springs](#springs) — Acxess springs, equivalence chart, and the 50–55 mm length issue
- [Linkage — Shimming & Rod Ends](#linkage--shimming--rod-ends)
- [Mounting (3D-printed)](#mounting-3d-printed) — my Thingiverse shock-to-chassis adapters
- [Assembly](#assembly-hbhpi-big-bore--revo-gen-1) — building the HB/HPI shocks onto the Revo Gen 1
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

**What "bore" means:** the bore is the **inside diameter of the shock body** — effectively the size of the piston face. A bigger bore = a **bigger piston**.

**Why a bigger bore needs lighter oil:** for the *same* suspension movement (same shaft speed and travel), a **bigger piston sweeps more oil volume** on each stroke. That larger volume still has to squeeze through the **same piston holes** (same count and size), so it's forced through **faster and meets more resistance — i.e. more damping**. To bring the damping back down to where a smaller shock sat, you run **thinner (lighter) oil** in the bigger shock.

So it sounds backwards — *bigger shock, lighter oil* — but it's just compensating for the extra oil the bigger piston shoves through the same holes. The E-Revo originally shipped with a **2-hole piston**, and some people deliberately drop to a smaller piston (fewer / smaller holes) to stay on standard oil weights. For example, where a smaller shock wants ~**55wt**, a bigger-bore shock can run **40–45wt** with similar characteristics.

---

## Why Heavier Oil

I run at the top of the oil range on purpose: **heavier oil is significantly more temperature-stable**. It holds its damping rate across weather swings and resists **shock fade** — as the oil heats up during a run, a shock becomes less effective, and lighter oils lose their rate faster. The small consistency tax of running thick oil is worth it for damping that feels the same lap 1 and lap 10.

---

## Springs

**The springs that come with the HB D8 are not right for this build.** The D8 is a **1/8 buggy** shock, and its included springs are rated for a buggy's weight. The **E-Revo is a much heavier machine** — a massive truggy with big tires and a high CG. Bolt the D8 buggy springs straight on and the truck **sags into its travel and bottoms out**, with no rate left to hold ride height or control the weight on landings.

**Use Acxess Springs** ([acxesspring.com](https://www.acxesspring.com/)) — I bought mine from [thespringstore.com](https://www.thespringstore.com/). The chart below maps each Acxess spring to its **equivalent GTR spring color and rate** (rates copied from the original GTR shock table). Mix and match by rate. Assume **~60 mm length** unless noted.

| Equiv GTR color | Rate (N/mm) | Acxess industrial part # |
|---|---|---|
| Yellow | 2.8 | PC077-938-7000-MW-2333-CG-N-IN |
| White | 2.9 | PC085-975-7630-SST-2335-C-N-IN |
| Orange / Green | 3.3 | PC085-975-7630-MW-2335-C-N-IN |
| ⭐ **Gold** *(my front)* | **3.73** (63.5 mm) | PC092-975-9000-MW-2500-CG-N-IN |
| ⭐ **Tan** *(my rear)* | **4.0** | PC085-975-6630-MW-2335-C-N-IN |
| Black | 4.5 | PC096-975-8000-SST-2346-C-N-IN |
| Silver / Pink | 5.2 | PC096-975-8000-MW-2346-C-N-IN |
| Blue | 5.9 | PC105-1014-8000-SST-2355-C-N-IN |
| Purple | 6.2 (63.5 mm) | PC112-1010-10800-MW-2500-CG-N-IN |

- **My setup:** **Gold front / Tan rear.**
- **General rule: softer front, stiffer rear.** Pick a front color, then go one step up the chart for the rear — e.g. **Silver front → Blue rear**.

### ⚠️ Spring length — go 50–55 mm, not 60 mm

**Big issue with the springs I recommend:** don't run the **60 mm** springs shown in the kit picture. They *will* wear in and eventually settle to near-perfect ride height with the right droop — but you should just start with **50–55 mm** springs. Anything **shorter than ~55 mm** is about perfect: it nearly covers the whole shock body and looks clean. (I already spent ~$55 on the 60–63 mm springs, so I'm running those for now.)

---

## Linkage — Shimming & Rod Ends

- **Metal D8 bodies shim easily with M3×1 mm shims** to keep the shock end **centered on the rocker** — clean, repeatable, and only possible because the body is metal (plastic flexes and won't hold the shim stack as precisely).
- **Push-rod rod ends are RPM (plastic)**, so all the stretch and abuse in the linkage is **consolidated onto a cheap, quick-swap part**. Same philosophy as the [aluminum rockers](rocker_analysis.md) — push wear onto whatever's cheapest to replace, and maintenance stays cheap.

---

## Mounting (3D-printed)

✅ **Solved with my own custom shock-mount adapters** — published on Thingiverse: **[thing:7090606](https://www.thingiverse.com/thing:7090606)**. They let true 1/8 big-bore shocks (97 mm Hot Bodies D8 / HPI 107365 Apache C1) bolt onto the **Revo Gen 1** chassis. **Works with swaybars** (slight trimming). Tuned for racing, not max-air bashing — but the editable STEP files are included if you want to take it further.

Files in [`3d-models/shock_mounts/`](3d-models/shock_mounts/):
- `Front_Shock_Mount.stl` / `Rear_Shock_Mount.stl` — print-ready
- `EREVO_Front_Shock_Mount_Upgrade.step` / `EREVO_Rear_Shock_Mount_Upgrade.step` — editable CAD

<p align="center">
  <img src="src/suspension_shock_mount_front_3d.png" width="380">&nbsp;<img src="src/suspension_shock_mount_rear_3d.png" width="380"><br>
  <em>Front · rear shock-mount adapters (Revo Gen 1 → 97 mm big bore)</em>
</p>

---

## Assembly (HB/HPI big bore → Revo Gen 1)

Steps to set the HPI / Hot Bodies shocks up front and rear with these mounts:

1. **Drill the stock eyelet** — enlarge the hole in the stock shock-shaft eyelet until it reaches the ball joint.
2. **Trim the eyelet** — shorten it so the threaded part of the shaft can screw in deep enough to **just touch (or nearly touch) the ball**.
3. **Assemble the internals** — install the **original bump-stop** inside the body, then stack the **kit washer**, then the **1.2 mm 4-hole piston** on top, and fasten with the provided **lock nut**. Fill with **80wt oil** — the baseline for both front and rear.
4. **Cap setup** — press-fit the ball joint from the **original GTR cap / eyelet** into the new shock cap; make sure it sits **flush**.

**Oil cross-reference:** 50wt in the stock Revo Gen 1 shocks feels similar to **80–90wt in these HB/HPI big bores** — the bigger bore needs heavier oil for the same feel (see [Bigger bore → lighter oil](#bigger-bore--lighter-oil-why-some-go-smaller-piston)). 80wt is the baseline; I run [90wt front / 100wt rear](#setup-spec--piston--oil).

---

## Notes

- **D8 = Apache C1.** The metal Hot Bodies D8 (HBS67296) and the plastic HPI Apache C1 are the same shock; the Wltoys A929 is a budget knock-off of the C1. Bodies and most internals interchange — see the [FastAzJato4x4 shock analysis](../FastAzJato4x4/shock_analysis.md) for the full big-bore parts breakdown (spare bodies, maintenance sets, spring charts).
- **Metal here, plastic there.** This build chooses metal for the shim trick + heavy-truck durability; the lighter Jato build chooses the plastic twin for weight. Same shock family, opposite trade-off.
- **Rebuild on condition, not schedule** — service a shock only when it leaks or breaks.
