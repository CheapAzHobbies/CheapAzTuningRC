# Shock Selection — FastAzJato4x4

> **Chosen: HPI Apache C1 plastic big bore (or the Wltoys A929 knock-off of it) front + rear** — **much lighter** than the metal version, and the plastic bodies are protected on this build by the corrected shock-tower geometry (the tower config from last time — see [shock tower analysis](shock_tower_analysis.md)) plus the [arm guards](arm_analysis.md#shock-guards). It's the same 97mm **16mm big-bore** shock as the metal **Hot Bodies D8 / B8 (HBS67296)** — **the metal version is the runner-up**, deployed only if plastic bodies keep getting destroyed.
>
> **Current spec target** (subject to TBD on oil weight):
> - **Springs:** **white 59gf (HB 67454, 76mm) front + gray 52gf (HB 67453, 76mm) rear** — same as K939 spec
> - **Pistons:** 1.4mm × 6 holes, front + rear
> - **Oil:** 45wt front, **50-60wt rear (TBD)** — final pick depends on track conditions
> - **Shock length:** 97 mm (Apache C1 / D8 front spec — see [reference note](#hot-bodies-big-bore-shock-spring-chart-full-lineup) for what "97mm" actually measures); D8 rears optionally 112 mm if going the full mixed-length D8 setup
>
> **Traxxas Big Bore XX-Long (2662) is vetoed:** it was "big bore" years ago, but its **10mm bore** isn't by today's standards (vs the C1/D8's 16mm) — a waste of money even at $26.95. The aluminum **GTR XX-Long (7462X, 13mm bore)** is the better OEM option if you want an in-production aluminum shock, but still less plush than the big-bore C1/D8.

<p align="center">
  <img src="src/suspension_hpi_shocks_apache_c1_107365.jpg" width="500">&nbsp;<img src="src/suspension_hb_b8_shocks.jpg" width="500"><br>
  <em>Chosen: HPI Apache C1 plastic big bore (or the Wltoys A929 knock-off) — much lighter · Runner-up: Hot Bodies D8 / B8 metal big bore</em>
</p>

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Shock Comparison](#shock-comparison) — body / brand options
- [Replacement Parts (shock bodies)](#replacement-parts-shock-bodies) — spare HB 67435 bodies
- [Setup Spec (Springs / Pistons / Oil)](#setup-spec-springs--pistons--oil)
- [Plastic vs Metal Body Trade-off](#plastic-vs-metal-body-trade-off)
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **97mm big-bore class** | Must | Matches the FastAzJato4x4 ride height + arm geometry; smaller shocks don't have the travel |
| **Threaded body for adjustable preload** | Must | Setup tunability is the whole point of an aftermarket shock |
| **Standard pistons + shaft** | Must | Common spares + tunable pistons available off the shelf |
| **Rebuildable** | Must | Shocks need re-oiling and seal replacement every 10-20 packs |
| **Reasonably priced** | May | Premium racing shocks cost more than the chosen motor — diminishing returns for offroad use |
| **Metal body** | May | Light enough plastic is acceptable; metal is the optimization for crash resistance |

---

## Shock Comparison

| Shock | Spec | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **HPI Racing Apache C1** — 97mm big bore | Body: **plastic**<br><br>Bore: **16mm**<br><br>Length: 97mm<br><br>Part: **#107365** (MPN H107365)<br><br>Price: **~$20–30/pair** | **Chosen** — most likely config (front + rear); In Hand on K939 | Pro: Light, threaded, rebuildable, well-tuned out of the box, **same internal design as the Hot Bodies D8**. Apache C1 = HPI's plastic version of the D8 shock<br><br>Con: Plastic body cracks under hard impacts (rocks, rollovers, rear-end hits) | <img src="src/suspension_hpi_shocks_apache_c1_107365.jpg" width="500"> |
| **Wltoys A929** (Apache C1 knock-off) | Body: **plastic**<br><br>Bore: 16mm<br><br>Part: **A929-14**<br><br>Price: **~$15.99/set** (white springs incl.) | **Chosen — budget equal** | Pro: **Knock-off of the Apache C1 — the same 97mm big-bore plastic shock for a fraction of the price.** Parts interchange with the C1 / D8 / B8. Cheapest way into the chosen shock<br><br>Con: **Ships from China — slow delivery.** Knock-off QC on paper. **Horror story: some ship with the shock caps super-glued shut** — soak in **acetone** to free them for rebuilds. **Would happily run these, but availability is unproven** — no order placed yet | <img src="src/suspension_wltoys_a929_shocks_a929-14.jpg" width="500"> |
| **Hot Bodies B8 shock set** | Body: **aluminum** (metal)<br><br>Bore: 16mm big bore<br><br>Set of **4** (white springs)<br><br>Price: **$65.99 used** | **In Hand — scored used** | Pro: **The metal big-bore set the user actually wanted** — scored used as a set of 4. Metal body shrugs off impacts; same 16mm big-bore class as the Apache C1. **Hard to find** — only the plastic Apache C1 is comparable<br><br>Con: Used-market only / scarce; heavier than the plastic C1 (which is why the C1 is still the most-likely running config) | <img src="src/suspension_hb_b8_shocks.jpg" width="500"> |
| **Hot Bodies D8** (metal body) | Body: **aluminum** (metal)<br><br>Bore: 16mm<br><br>Part: **HBS67296**<br><br>Incl. piston set (1.3 / 1.4 / 1.5mm)<br><br>Price: $57.99 new (disc.) / $30–80 used | **Runner-up — metal** (buy-new equivalent of the in-hand B8) | Pro: **Same design + internals as the Apache C1** but metal-bodied — survives impacts that crack the plastic version. Same 97mm big-bore shock sold as the Apache C1 and the Wltoys knock-off<br><br>Con: 15–20g heavier per shock (aluminum body adds mass at the corners). **Discontinued new** — buy when you spot one | <img src="src/suspension_hb_d8_shocks_hbs67296.jpg" width="500"> |
| **Losi 8IGHT shocks** (8B/8T) | Body: aluminum<br><br>Bore: big bore<br><br>Part: **LOSA5417** (set of 4)<br><br>Price: pricey — **unobtanium** | Candidate | Pro: 1/8-class big-bore option, community-confirmed on Slash 4x4 (RCU). **Two ways to fit:** (1) full LOSA5417 set with the **original Slash 4x4 tower** (the fronts are slightly shorter), or (2) **buy two rears and run rears front + back with the Jato towers** (rear tower height is the same across all rear-tower variants)<br><br>Con: **LOSA5417 is unobtanium right now** — discontinued / very hard to find. Pricey; metal-body weight | <img src="src/suspension_losi_8ight_shocks_losa5417.jpg" width="500"> |
| **Traxxas GTR shocks** — XX-Long, aluminum PTFE | Body: aluminum (PTFE hard-anodized)<br><br>Bore: **13mm**<br><br>Part: **7462X**<br><br>Price: **$36.95/pair** (incl. 30wt oil)<br><br>Variants: **7462 / 7462G** anodized alum · **7462-GRAY** composite (cheapest) · **7461** = shorter "Long" | **Candidate** (stock OEM option) | Pro: **Come stock on the higher Slash 4x4 trims (Ultimate / Platinum).** Hard-anodized aluminum, PTFE bores, TiN shafts (no stiction), threaded collars, X-rings. Native Traxxas fit, **in production** (unlike the discontinued D8)<br><br>Con: **13mm bore vs the C1/D8's 16mm** — holds less oil, so the **C1/D8 are significantly more plush and consistent**. Heavier than the plastic C1; springs sold separately | <img src="src/suspension_traxxas_gtr_shocks_xxl_7462x.jpg" width="500"> |
| ~~**Traxxas Big Bore XX-Long**~~ | Body: aluminum (PTFE hard-anodized)<br><br>Bore: **10mm**<br><br>Part: **2662**<br><br>Price: $26.95/pair | **Vetoed** | Pro: Classic shock — aluminum PTFE body, TiN shafts, native Traxxas fit, cheap<br><br>Con: **Waste of money.** Was "big bore" back in the day, but **10mm is not big bore by modern standards** — smaller than the GTR (13mm) and well under the C1/D8 (16mm). For similar money the Apache C1 is far more plush | <img src="src/suspension_traxxas_big_bore_xxl_2662.jpg" width="500"> |

### Replacement Parts (shock bodies)

Spares to keep on hand for when an Apache C1 shock body gets destroyed in a crash. Worth stashing one set so a cracked body doesn't sideline the car.

| Part | Spec | Fits | Photo |
|---|---|---|---|
| **Hot Bodies 67435** — Big Bore shock body set | Threaded **aluminum** bodies, **2 pcs** | Apache C1 / HB D8 big-bore shocks | <img src="src/suspension_hb_shock_body_67435.jpg" width="250"> |
| **HPI 67515** — Big Bore Shock Maintenance Set | Rebuild kit: X-rings, silicone o-rings, bladders + caps, seal spacers | Apache C1 / HB D8 big-bore shocks | <img src="src/suspension_hpi_shock_maintenance_set_67515.jpg" width="250"> |
| **Hot Bodies 67437** — Big Bore Shock Bottom Cap | O-ring sealed threaded **bottom caps, 2-pack** (Vorza / D8S big bore), **pink anodized** | Apache C1 / HB D8 big-bore shocks | <img src="src/suspension_hb_shock_bottom_cap_67437.jpg" width="250"> |

> **Bonus:** because the 67435 bodies are aluminum, replacing a cracked plastic Apache C1 body with these effectively does the [metal-body upgrade](#plastic-vs-metal-body-trade-off) one shock at a time — no need to buy whole D8s.

---

## Setup Spec (Springs / Pistons / Oil)

This is the target tuning — same as the K939 build, adjusted slightly for the FastAzJato4x4's heavier curb weight.

| Position | Spring | Piston | Oil |
|---|---|---|---|
| **Front** | **White 59gf** (Hot Bodies #67454, 76mm — stock Apache C1 / D8) | **1.4mm × 6 holes** | **45wt** |
| **Rear** | **Grey 52gf** (Hot Bodies #67453, 76mm — soft for bump compliance) | **1.4mm × 6 holes** | **50-60wt (TBD)** — start at 50, bump to 60 if too plush |

**Why this setup:**
- **White 59gf front + grey 52gf rear** = stock Apache C1 / D8 spec, K939-tested. Slightly softer rear gives more bump compliance over hardpack
- **Spring sourcing:** the HPI Apache C1 and Hot Bodies D8 both ship stock with **white** springs. On real **D8 buggy take-offs** you'll typically find a **grey + white combo** — which is exactly this front (white) / rear (grey) pairing, so used take-off springs are a cheap, easy source
- 1.4mm × 6 holes = mid-range damping, good general-purpose piston. Tighter holes (1.2-1.3mm) increase damping for smoother tracks; bigger holes (1.5-1.6mm) loosen damping for whoops
- 45wt front / 50-60wt rear = rear heavier to control squat under power and rebound from jumps. 60wt is the upper end if 50wt feels too floaty on landings

### Hot Bodies Big Bore Shock Spring chart (full lineup)

All HB Big Bore springs sold as a pair. The chosen pair is bolded. **Shorter springs (60mm)** suit shorter shock bodies / tighter packaging; **76mm** is the most common length for 97mm-eye-to-eye Apache C1 / D8 fronts.

| Part # | Color | Length | Rate | Sold as |
|---|---|---|---|---|
| HB 67446 | Gray | 60 mm | 74 gf | pair |
| HB 67448 | Blue | 60 mm | 89 gf | pair |
| HB 67449 | Orange | 60 mm | 98 gf | pair |
| HB 67450 | Green | 68 mm | 59 gf | pair |
| HB 67451 | Yellow | 68 mm | 68 gf | pair |
| HB 67452 | Red | 68 mm | 81 gf | pair |
| **HB 67453** | **Gray** | **76 mm** | **52 gf** | **pair — chosen rear** |
| **HB 67454** | **White** | **76 mm** | **59 gf** | **pair — chosen front** |
| HB 67455 | Blue | 76 mm | 63 gf | pair |
| HB 67456 | Orange | 76 mm | 74 gf | pair |

> **Shock length reference**: Apache C1 / D8 fronts are spec'd as **97 mm**. Hot Bodies D8 rears are an optional **112 mm** (HBS67298) if you want longer rear droop / travel — note the longer rear shock body changes which spring length fits cleanly.
>
> **Caveat on what "97mm" / "112mm" actually means**: Hot Bodies / HPI don't explicitly define which measurement they're using. RC forum convention (RCTech, RCU) treats these numbers as **overall pin-to-pin length at full extension** (effectively eye-to-eye when you treat the mounting holes as eyes). The threaded body alone would be ~55-65mm; the rest is shaft + caps. Some manufacturers spec at-rest installed length instead. Verify with a caliper on an actual shock before ordering specific aftermarket parts that depend on exact length.

---

## Plastic vs Metal Body Trade-off

The Apache C1 (plastic) and Hot Bodies D8 (metal) are **the same shock internally** — same shaft, same piston interface, same internal volume, same external dimensions. The body material is the only meaningful difference.

| | Apache C1 (plastic) | D8 (metal) |
|---|---|---|
| Weight (each) | ~45-50g | ~60-65g |
| Impact resistance | Cracks under hard hits on body | Dents but doesn't crack |
| Repairability after impact | Replace whole body | Often still usable, sometimes straighten |
| Price (pair) | $20-30 | $58 new (disc.), $30-80 used |
| Heat (sustained running) | Plastic insulates — oil stays hotter, fades faster | Aluminum sheds heat — more consistent damping over a long pack |
| Handling impact of weight | Lighter unsprung mass = better bump response | 4×15-20g = ~80g added across all corners — small but measurable |

**Take:** start with the plastic Apache C1 already known to work on the K939. **Upgrade to metal D8 only if shock-body damage becomes a recurring problem** in real crashes on this build. Don't pre-emptively pay the weight + cost penalty for a problem you might not have.

---

## Notes

- **One shock, three flavors — and all parts interchange.** The genuine **Hot Bodies D8 / B8 (HBS67296)**, the **HPI Apache C1 (107365)**, and the **Wltoys A929 knock-off** are the same 97mm big-bore shock. Bodies, shafts, pistons, springs, caps, and boots **swap freely between Apache C1 and D8** — so you can rebuild or upgrade one piece at a time (e.g. drop a metal [67435 body](#replacement-parts-shock-bodies) into a plastic Apache C1). If you find unlabeled "big bore buddy shocks" with no size listed, they're most likely these — run them front and rear.
- **Losi 8IGHT (LOSA5417) fitment, two ways:** the full set has **slightly shorter fronts**, so to run the whole set you need the **original Slash 4x4 tower**. The simpler path is to **buy two of the rear shocks and run rears at both ends with the Jato towers** — the **rear tower height is the same across all rear-tower variants**, so any rear tower mounts them at the same height. Note LOSA5417 is currently unobtanium.
- **"XXL" / "XX-Long" = long travel, not big bore.** The XX-Long designation refers to the shock's **travel / length** (longer shaft + body), which is independent of bore diameter. A shock can be XX-Long but small-bore — the GTR (13mm) and 2662 (10mm) both are. Don't read "XX-Long" as "big bore."
- **Bore size is why the C1/D8 win over the GTR:** the Apache C1 / D8 are **16mm bore**, the Traxxas GTR XX-Long is **13mm**. The bigger bore holds more oil, which makes the C1/D8 **significantly more plush and consistent** — the GTR is a good, in-production aluminum shock, but it can't match the big-bore damping. The GTR's edge is availability (the D8 is discontinued) and a PTFE/TiN-slick, in-stock OEM option.
- The K939 build uses Apache C1 (plastic) and has not had a body-cracking problem in ~~years~~ many packs — the FastAzJato4x4 *might* be fine on plastic too. The trigger to swap to metal D8 would be **first cracked body**, not pre-emptive optimization.
- **Shock tower geometry interacts with shock survival** — see the [aero analysis cascade](aero_analysis.md#shock-tower-compatibility-cascade). The "shocks at the back of the car" geometry from the OEM Jato wing mount + #9034 stock tower is the root cause of past shock body damage. Solving the geometry problem (STRC backflash kit) is potentially a cheaper insurance than upgrading shock bodies to metal.
- **Oil weight is climate-dependent** — silicone shock oil thickens in cold weather. The 45wt front / 50-60wt rear target assumes mild conditions; bump down 5wt per side if running in cold.
- **Rebuild schedule:** every 10-20 packs, pull shocks apart, inspect seals + o-rings, replace oil. Plastic shock o-rings degrade faster than the metal D8's; another small win for the metal upgrade if rebuild frequency matters.
