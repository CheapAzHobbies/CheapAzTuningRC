# Shock Selection — FastAzJato4x4

> **Leaning toward: Hot Bodies D8 (metal-body version)** — same physical design as the HPI Apache C1 already in hand on the K939 build, but **metal body** instead of plastic. The plastic Apache C1 is fine and light (planned for front + rear on this build); the metal D8 is an optimization if shock-body damage in crashes becomes a problem.
>
> **Current spec target** (subject to TBD on oil weight):
> - **Springs:** white (front) + grey 52gf (rear) — same as K939 spec
> - **Pistons:** 1.4mm × 6 holes, front + rear
> - **Oil:** 45wt front, **50-60wt rear (TBD)** — final pick depends on track conditions
>
> **Traxxas Big Bore XXL shocks are explicitly vetoed:** they were "big bore" when released years ago but are not by modern standards, and they're way overpriced for the performance.

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Shock Comparison](#shock-comparison) — body / brand options
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

| Shock | Body material | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **HPI Racing Apache C1 (#107365)** — 97mm big bore | Plastic | **In Hand** (running on K939) — planned for FastAzJato4x4 front + rear | Pro: Light, cheap (~$20/pair), threaded, rebuildable, well-tuned out of the box, **same internal design as the Hot Bodies D8 below**. Apache C1 = HPI's plastic version of the D8 shock<br>Con: Plastic body cracks under hard impacts (rocks, rollovers, rear-end hits) | <img src="src/suspension_hpi_shocks_apache_c1_107365.jpg" width="300"> |
| **Hot Bodies D8 (metal body)** | Metal (aluminum) | **Leaning toward — the optimization step from the Apache C1** | Pro: **Same physical design and internals as the Apache C1** but with a metal body — survives impacts that would crack the plastic version. ~$35-50/pair, still way cheaper than premium racing shocks<br>Con: ~15-20g heavier per shock (aluminum body adds mass at the corners — small handling penalty); more expensive | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/suspension_hot_bodies_d8_shocks.jpg` |
| ~~Traxxas Big Bore XXL~~ | Plastic | **Vetoed** | Pro: Native fit to a Traxxas chassis, factory body color match<br>Con: **Not actually big bore by modern standards** — the "XXL" name is marketing from when the shock first launched; today's real big bores are larger diameter. Overpriced ($50-70/pair) for what they deliver. No tuning advantage over the cheaper Apache C1 / D8 | — |
| **GTR Shocks** (Pro-Line, JConcepts, etc.) | Aluminum | **Vetoed (overkill)** | Pro: Premium racing shock, best tuning options, most adjustability, top-tier internals<br>Con: $80-150/pair. Diminishing returns for a basher / casual race build — the Apache C1 / D8 covers 90% of what GTRs do for a fraction of the cost | — |

---

## Setup Spec (Springs / Pistons / Oil)

This is the target tuning — same as the K939 build, adjusted slightly for the FastAzJato4x4's heavier curb weight.

| Position | Spring | Piston | Oil |
|---|---|---|---|
| **Front** | White (stock Apache C1 / D8) | **1.4mm × 6 holes** | **45wt** |
| **Rear** | **Grey 52gf** (Hot Bodies #67453, 76mm — soft for bump compliance) | **1.4mm × 6 holes** | **50-60wt (TBD)** — start at 50, bump to 60 if too plush |

**Why this setup:**
- White front spring = stock baseline, well-matched to typical front weight bias
- Grey 52gf rear = softer than stock, prioritizes bump compliance over roll stiffness — picked because the target tracks have rough hardpack
- 1.4mm × 6 holes = mid-range damping, good general-purpose piston. Tighter holes (1.2-1.3mm) increase damping for smoother tracks; bigger holes (1.5-1.6mm) loosen damping for whoops
- 45wt front / 50-60wt rear = rear heavier to control squat under power and rebound from jumps. 60wt is the upper end if 50wt feels too floaty on landings

---

## Plastic vs Metal Body Trade-off

The Apache C1 (plastic) and Hot Bodies D8 (metal) are **the same shock internally** — same shaft, same piston interface, same internal volume, same external dimensions. The body material is the only meaningful difference.

| | Apache C1 (plastic) | D8 (metal) |
|---|---|---|
| Weight (each) | ~45-50g | ~60-65g |
| Impact resistance | Cracks under hard hits on body | Dents but doesn't crack |
| Repairability after impact | Replace whole body | Often still usable, sometimes straighten |
| Price (pair) | ~$20 | ~$35-50 |
| Heat (sustained running) | Plastic insulates — oil stays hotter, fades faster | Aluminum sheds heat — more consistent damping over a long pack |
| Handling impact of weight | Lighter unsprung mass = better bump response | 4×15-20g = ~80g added across all corners — small but measurable |

**Take:** start with the plastic Apache C1 already known to work on the K939. **Upgrade to metal D8 only if shock-body damage becomes a recurring problem** in real crashes on this build. Don't pre-emptively pay the weight + cost penalty for a problem you might not have.

---

## Notes

- The K939 build uses Apache C1 (plastic) and has not had a body-cracking problem in ~~years~~ many packs — the FastAzJato4x4 *might* be fine on plastic too. The trigger to swap to metal D8 would be **first cracked body**, not pre-emptive optimization.
- **Shock tower geometry interacts with shock survival** — see the [aero analysis cascade](aero_analysis.md#shock-tower-compatibility-cascade). The "shocks at the back of the car" geometry from the OEM Jato wing mount + #9034 stock tower is the root cause of past shock body damage. Solving the geometry problem (STRC backflash kit) is potentially a cheaper insurance than upgrading shock bodies to metal.
- **Oil weight is climate-dependent** — silicone shock oil thickens in cold weather. The 45wt front / 50-60wt rear target assumes mild conditions; bump down 5wt per side if running in cold.
- **Rebuild schedule:** every 10-20 packs, pull shocks apart, inspect seals + o-rings, replace oil. Plastic shock o-rings degrade faster than the metal D8's; another small win for the metal upgrade if rebuild frequency matters.
