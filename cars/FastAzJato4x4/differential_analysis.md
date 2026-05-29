# Differential Selection — FastAzJato4x4

> **Chosen:**
> - **Front & rear diffs: Traxxas E-Revo 1.0 with XO-1 I-bar cross pin** — E-Revo housing gives the only 6mm outdrives that mate with the chosen E-Revo CVDs. XO-1 I-bar cross pin swapped inside for added strength. All other diffs (Jato 4x4, Slash 4x4, XO-1) use 5mm outdrives and are ruled out.
> - **Center diff: stock Traxxas with 20k wt oil** — user-tested across multiple builds, no reason to change.
> - **Center driveshaft: pick on price and availability** — all options work, consequence-free choice.

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Front & Rear Diff Comparison](#front--rear-diff-comparison)
- [Center Diff Oil](#center-diff-oil)
- [Center Driveshaft](#center-driveshaft)
- [Sources](#sources)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **6mm outdrives** (front & rear) | Must | Match the chosen E-Revo CVDs and axles already in hand — all stock Jato/Slash/XO-1 diffs are 5mm and won't accept them |
| **Fits Jato 4x4 gearbox housing** | Must | Has to physically bolt up to the chassis mounts |
| **Sealed for oil** | Must | Tunable damping via diff oil viscosity |
| **Field-rebuildable** | May | Diff service is routine; user-rebuildable beats throw-and-replace |
| **Reasonably available / cheap** | May | Diffs are wear items; replacements should be easy to source |

---

## Front & Rear Diff Comparison

| Diff | Spec | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **Traxxas E-Revo 1.0 diffs + XO-1 I-bar** | Outdrive: **6mm**<br>Internal upgrade: **XO-1 I-bar cross pin** (I-shaped, stronger than standard round cross pin)<br>Part numbers: TBD — verify E-Revo 1.0 front/rear diff part numbers | **Chosen — In Hand** | Pro: **Only 6mm outdrive diff that mates the in-hand E-Revo CVDs.** XO-1 I-bar cross pin swapped inside adds significant strength. **Plastic housing stays rounder longer than aluminum** — holds fluid better, more tolerant to minor bending. 1/8-class internals in a 1/10 chassis — overbuilt for the role. $0 cost (already in hand)<br><br>Con: Heavier than stock Jato diffs; E-Revo diff cases require minor fitting to the Jato gearbox housing. **Must fill half full only** — overfilling plastic diff housings causes them to explode under pressure (user error, not a design flaw) | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_e_revo_diff.jpg` |
| ~~**Traxxas XO-1 diffs**~~ | Outdrive: **5mm**<br>Internal: I-bar cross pin<br>Part numbers: TBD | Ruled Out | Pro: I-bar cross pin is the strongest stock Traxxas diff internals<br><br>Con: **5mm outdrives — same incompatibility as Jato/Slash stock diffs.** I-bar cross pin is salvaged and used inside the E-Revo housing; the XO-1 diff case itself is not used | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_xo1_diff.jpg` |
| ~~**GPM aftermarket diffs**~~ | Outdrive: TBD — verify<br>Material: aluminum housing<br>Part numbers: TBD | Ruled Out | Pro: Precision machined, looks clean<br><br>Con: Outdrive size TBD — verify before ordering. **Aluminum housings auger out faster than plastic** — lose roundness quicker, less tolerant to bending, don't hold fluid as long. Heavier than plastic | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_gpm_diff.jpg` |
| ~~**Integy aftermarket diffs**~~ | Outdrive: TBD — verify<br>Material: aluminum housing<br>Part numbers: TBD | Ruled Out | Pro: Aftermarket precision, machined to tight tolerances<br><br>Con: Outdrive size TBD — verify before ordering. Same aluminum housing problem as GPM — augers out faster, less bending tolerance, doesn't hold fluid as long as plastic | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_integy_diff.jpg` |
| ~~Traxxas Jato 4x4 stock diffs~~ | Outdrive: 5mm<br>Part numbers: TBD | **Ruled Out** | Pro: Native fit to the Jato 4x4 gearbox housing<br><br>Con: **5mm outdrives — physically can't mate the in-hand E-Revo CVDs or axles** | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_jato_4x4_stock_diff.jpg` |
| ~~Traxxas Slash 4x4 stock diffs~~ | Outdrive: 5mm<br>Part numbers: TBD | **Ruled Out** | Same 5mm outdrive problem as Jato 4x4 stock diff | (reuses `src/drivetrain_traxxas_jato_4x4_stock_diff.jpg`) |

### Why 6mm wins

The drivetrain compatibility chain is rigid:
- **E-Revo CVDs (chopped to fit)** — 6mm cups
- **E-Revo axles** — 6mm
- **Diffs must be 6mm to mate both ends**

Every stock Traxxas diff (Jato 4x4, Slash 4x4, XO-1) uses 5mm outdrives. The E-Revo 1.0 is the only option with 6mm, making it the only compatible diff for this build.

---

## Center Diff Oil

**Chosen: 20,000 wt (20k cSt).** User-tested across multiple builds, lands in the sweet spot between freewheeling traction handoff and progressive lockup under throttle.

| Oil weight | Behavior | Use case |
|---|---|---|
| 5k cSt | Very fluid, lots of differentiation, freewheels in turns | Light-traction surfaces (sand, very loose) |
| 10k cSt | Quicker freewheel, less lockup under power | Tight indoor tracks |
| **20k cSt ⭐** | Balanced — diffs under hard throttle, freewheels at part-throttle | **Chosen — general offroad / 4S dirt** |
| 50k cSt | Mostly locked, all-four-wheels-pull feel | Crawling, low-grip climbs |
| 100k+ | Effectively locked spool | Drag/speed-run with grip |

**Fill level: half full only.** Overfilling plastic diff housings causes them to explode under pressure — this is user error. Fill to half, no more.

**Why not just lock the center diff?** Locked center = no torque differentiation front-to-rear = chassis pushes / pivots awkwardly on uneven surfaces. 20k gives the locked-feel under power without the disadvantages on rough offroad.

---

## Center Driveshaft

**Take: pick on price and availability — all options work.** Differences come down to durability under abuse, not performance.

| Driveshaft | Spec | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **Stock Traxxas plastic** | Material: plastic<br>Part numbers: TBD | Candidate | Pro: Cheapest, lightest<br><br>Con: Will deform under hard 4S abuse over many packs | — |
| **Stock Traxxas metal** | Material: steel<br>Part numbers: TBD | Candidate | Pro: More durable than plastic, ~10g weight penalty<br><br>Con: Slightly more expensive than plastic | — |
| **Tekno aftermarket** | Material: hardened steel<br>Part numbers: TBD | Candidate | Pro: Best build quality, definitive durability win<br><br>Con: Most expensive — overkill for casual use | — |

**Pick logic:** bashing → stock plastic. Most builds → stock metal (best value). Race / heavy 4S abuse → Tekno. This part breaks rarely and doesn't park the car when it does — spend the budget on motors, batteries, and tires first.

---

## Sources

- E-Revo CVD / diff compatibility — community confirmation in [RC Talk forum threads](https://www.rctalk.com/forum/threads/traxxas-jato-4x4.144356/) on Jato 4x4 builds using E-Revo drivetrain parts
- Center diff oil viscosity — Castle Creations / RPM tuning guides + user experience
