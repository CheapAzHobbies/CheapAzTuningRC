# Differential Selection — FastAzJato4x4

> **Chosen:**
> - **Front & rear diffs: Traxxas E-Revo** — already in hand. The E-Revo diffs use **6mm outdrives** which mate with the chosen E-Revo CVDs (chopped to fit). Jato 4x4 / Slash 4x4 stock diffs use 5mm outdrives which **physically can't fit E-Revo cups, and the smaller diff openings can't accept E-Revo axles either** — wrong direction of compatibility.
> - **Center diff: stock Traxxas** with **20k wt oil** — user-tested over multiple builds, no reason to change.
> - **Center driveshaft: doesn't really matter** — Tekno, stock metal, stock plastic all work. Pick on price and availability.

---

## Table of Contents

- [Key Requirements](#key-requirements) — Must / May for the diff pick
- [Front & Rear Diff Comparison](#front--rear-diff-comparison) — why E-Revo over Jato/Slash stock
- [Center Diff Oil](#center-diff-oil) — viscosity choice
- [Center Driveshaft](#center-driveshaft) — quick summary, basically doesn't matter
- [Sources](#sources)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **6mm outdrives** (front & rear) | Must | Match the chosen E-Revo CVDs and E-Revo axles already in hand |
| **Fits Jato 4x4 gearbox housing** | Must | Has to physically bolt up to the chassis mounts |
| **Sealed for oil** | Must | Tunable damping via diff oil viscosity |
| **Field-rebuildable** | May | Diff service is routine; user-rebuildable beats throw-and-replace |
| **Reasonably available / cheap** | May | Diffs are wear items; replacements should be easy to source |

---

## Front & Rear Diff Comparison

| Diff | Outdrive | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **Traxxas E-Revo 1.0 differentials (x2 — front & rear)** | **6mm** | **In Hand** | Pro: **Mates the in-hand E-Revo CVDs and axles** (5mm Jato/Slash diffs can't); sealed, rebuildable, field-tunable with diff oil; user has both in hand at $0 cost. Stout 1/8-class internals despite the 1/10 chassis<br>Con: Heavier than Jato 4x4 stock; E-Revo diff cases require minor fitting to the Jato gearbox housing | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/drivetrain_traxxas_e_revo_diff.jpg` |
| ~~Traxxas Jato 4x4 stock diffs~~ | 5mm | **Ruled Out** | Pro: Native fit to the Jato 4x4 gearbox housing<br>Con: **5mm outdrives won't accept the in-hand E-Revo CVD cups, and the 5mm diff axles won't fit E-Revo cups either.** Wrong direction of compatibility. Would force ditching the E-Revo CVDs and axles | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/drivetrain_traxxas_jato_4x4_stock_diff.jpg` |
| ~~Traxxas Slash 4x4 stock diffs~~ | 5mm | **Ruled Out** | Same 5mm outdrive problem as the Jato 4x4 stock diff | (would share Jato stock photo) |

### Why 6mm wins

The drivetrain compatibility chain is rigid:
- **E-Revo CVDs (chopped to fit)** — 6mm cups
- **E-Revo axles** — 6mm
- **Diffs must be 6mm to mate both ends**

Going with 5mm diffs would force replacing the CVDs and the axles, which defeats the in-hand-parts advantage and opens up a much bigger sourcing problem. The E-Revo diff is the dependency that everything else in the drivetrain already accepts.

---

## Center Diff Oil

**Chosen: 20,000 wt (20k cSt).** User-tested across multiple builds, lands in the sweet spot between freewheeling traction handoff and progressive lockup under throttle. No reason to deviate.

| Oil weight | Behavior | Use case |
|---|---|---|
| 5k cSt | Very fluid, lots of differentiation, freewheels in turns | Light-traction surfaces (sand, very loose) |
| 10k cSt | Quicker freewheel, less lockup under power | Tight indoor tracks |
| **20k cSt ⭐** | Balanced — diffs under hard throttle, freewheels at part-throttle | **Chosen — general offroad / 4S dirt** |
| 50k cSt | Mostly locked, all-four-wheels-pull feel | Crawling, low-grip climbs |
| 100k+ | Effectively locked spool | Drag/speed-run with grip |

**Why not just lock the center diff (spool / locker)?**
- Locked center = no torque differentiation front-to-rear = chassis pushes / pivots awkwardly on uneven surfaces
- 20k gives the locked-feel under power without the disadvantages on rough offroad

---

## Center Driveshaft

**Take: pick on price and availability, all options work.** The center driveshaft is one of the most consequence-free choices in a Jato 4x4 build. Differences between options come down to durability under abuse, not performance — none of them cost you measurable speed or handling on this chassis.

| Option | Status | Notes |
|---|---|---|
| **Stock Traxxas plastic** | Candidate | Cheapest, lightest. Will deform under hard 4S abuse over many packs but cheap to replace |
| **Stock Traxxas metal** | Candidate | More durable than plastic, slight weight penalty (~10 g), pennies more |
| **Tekno aftermarket** | Candidate | Best build quality, most expensive, definitive durability win — overkill for casual use |
| **Other (GPM, RPM, etc.)** | Candidate | Vary in quality, no clear winner |

**Pick logic:**
- Bashing budget build → stock plastic
- Most builds → stock metal (best value)
- Race / heavy 4S abuse → Tekno

**Honestly:** this is a part that breaks rarely and even when it does it doesn't park the car. **Spend the budget on motors, batteries, and tires before optimizing this.**

---

## Sources

- E-Revo CVD / diff compatibility — community confirmation in [RC Talk forum threads](https://www.rctalk.com/forum/threads/traxxas-jato-4x4.144356/) on Jato 4x4 builds using E-Revo drivetrain parts
- Center diff oil viscosity — Castle Creations / RPM tuning guides + user experience
