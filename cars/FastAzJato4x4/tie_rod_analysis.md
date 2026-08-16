# Tie Rod & Camber Link Selection — FastAzJato4x4

> **Direction: 4mm steel turnbuckles front (steering toe links + front camber links), stock M3 Jato 3.3 steel turnbuckles rear.** Nothing bought yet for the front. The stock plastic front rods snap on hard hits behind the FLM aluminum arms, so the front moves to 4mm steel. The rear already ran steel M3 turnbuckles from the Jato 3.3, so it stays as-is. On length: there is no single molded length to buy, because these are threaded turnbuckles. You buy a rod whose adjustment range covers the target and thread it to fit. The FLM front arms sit +9.6mm/side over stock, so the front links land roughly stock + 10mm. Set that at test-fit, do not order a fixed number.

---

## Table of Contents

- [Which links this covers](#which-links-this-covers) — the four rod/turnbuckle links and their jobs
- [Key Requirements](#key-requirements) — 4mm steel, adjustable, reaches the wider front
- [Front steering tie rods (toe links)](#front-steering-tie-rods-toe-links) — the part that snaps most
- [Camber links (upper links)](#camber-links-upper-links) — front to steel, rear already fine
- [Servo-to-bellcrank link](#servo-to-bellcrank-link) — already chosen, cross-ref only
- [Length reference](#length-reference) — why there is no single number to buy
- [Price History](#price-history) — nothing purchased for the front yet
- [Notes](#notes)

---

## Which links this covers

All the adjustable rod/turnbuckle links on the car. "Tie rod" gets used loosely, so to be clear about what each one does:

| Link | What it does | Sets | This build |
|---|---|---|---|
| **Front steering tie rod (toe link)** | Bellcrank/drag link to front steering knuckle | Front toe | TBD: 4mm steel turnbuckle, stock+10mm range |
| **Front camber link (upper link)** | Front tower/bulkhead to top of C-hub carrier | Front camber | TBD: 4mm steel turnbuckle |
| **Rear camber link (upper link)** | Rear tower to top of rear carrier | Rear camber, a little rear toe | Stock M3 Jato 3.3 steel turnbuckle, fine |
| **Servo to bellcrank link (drag link)** | Servo horn to bellcrank | Steering centering | Done: GPM RUS416026ST-S, in hand ([`steering_bell_crank_analysis.md`](steering_bell_crank_analysis.md#servo-horn--servo-to-bellcrank-link)) |

The Jato 4x4 has no separate front lower link. The lower arm is the FLM/ProTrac arm itself, covered in [`arm_analysis.md`](arm_analysis.md).

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **4mm steel rod on the front (not plastic)** | Must | Stock plastic front tie rods and camber links snap on hard hits behind the FLM aluminum arms. The metal arm does not give, so the load goes into the links. 4mm steel takes the hit instead of shattering. Called out in [`arm_analysis.md`](arm_analysis.md#arm-comparison) |
| **Adjustable turnbuckle (threaded both ends)** | Must | Front track grew about 10mm/side with the FLM arms, so the links have to thread out to reach, and toe/camber must be tunable on a race car. Fixed molded rods can do neither |
| **Reaches stock length + ~10mm on the front** | Must | The +9.6mm/side from the FLM26800 arms pushes the outer ball studs outboard. The rod's adjustment range must cover that, not just stock length |
| **Rod ends match the alloy hubs and FLM studs** | Must | Front runs the Raptor R Ultimate EHD alloy hubs ([`hub_carrier_analysis.md`](hub_carrier_analysis.md)). The ball-stud size has to seat in those and in the FLM arm studs |
| **Spring steel or stainless, not soft aluminum** | May | Aluminum turnbuckles bend and gall on the threads. Spring steel is why the rear Jato 3.3 rods survived. Keep that up front |
| **Bends before it snaps** | May | Same failure philosophy as the arms. A bent steel rod straightens and keeps running. A shattered plastic one is a tow-back |

---

## Front steering tie rods (toe links)

The one that snaps most. Stock is a molded plastic rod sized for the 92mm arm, so it is both too short and too brittle for this front end.

> *Spec format: Type · Material · MPN · Fits · Adjustable · Length · Price*

| Rod | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **GPM spring-steel turnbuckle set** — *front target, not yet bought* | **Type:** Threaded turnbuckle<br>**Material:** Spring steel<br>**MPN:** TBD (GPM Rustler/Slash 4x4 line, same family as the in-hand RUS416026ST-S)<br>**Fits:** Slash 4x4 / Rustler 4x4 / Jato 4x4 ball-stud pattern<br>**Adjustable:** Yes, both ends<br>**Length:** Set to **~stock + 10mm** at test-fit<br>**Price:** TBD | Pro: **Steel, adjustable, and a brand already on the car.** The servo link is this exact family and it holds up. Threads out to cover the wider FLM front track. Bends instead of snapping<br><br>Con: Confirm the rod length range actually reaches stock+10mm before buying. Price not pinned yet | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/steering_gpm_tie_rod_set.jpg` |
| 🔵 **Generic AliExpress 4mm steel turnbuckle set** | **Type:** Threaded turnbuckle<br>**Material:** Steel (grade varies)<br>**MPN:** Generic<br>**Fits:** Slash 4x4 / Jato 4x4 pattern<br>**Adjustable:** Yes<br>**Length:** Adjustable<br>**Price:** ~$8-12 shipped | Pro: Cheapest 4mm steel option. Same pattern the rest of the Slash-family parts use. Comes with rod ends<br><br>Con: Thread quality and rod-end plastic vary, may need to swap ends. No warranty | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/steering_generic_4mm_turnbuckle_set.jpg` |
| ❌ ~~**Traxxas stock plastic tie rod**~~ | **Type:** Fixed molded rod<br>**Material:** Glass-filled nylon<br>**MPN:** N/A<br>**Fits:** Slash 4x4 / Jato 4x4 OEM<br>**Adjustable:** No<br>**Length:** Stock (sized for 92mm arm)<br>**Price:** ~$5 | Pro: Cheap, OEM, light<br><br>Con: **Snaps on hard hits behind the aluminum arm,** the exact failure this doc fixes. **Too short for the FLM front track** and not adjustable, so it cannot be lengthened. Vetoed for the front | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/steering_traxxas_stock_plastic_tie_rod.jpg` |

---

## Camber links (upper links)

Front snaps like the tie rods, so it goes to 4mm steel. Rear is already steel from the Jato 3.3, so it is left alone.

> *Spec format: Type · Material · MPN · Fits · Adjustable · Length · Price*

| Link | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| 🟢 **Stock M3 Jato 3.3 steel turnbuckle** — *rear, in hand* | **Type:** Threaded turnbuckle<br>**Material:** Steel (Jato 3.3 OEM)<br>**MPN:** Jato 3.3 OEM<br>**Fits:** Jato rear<br>**Adjustable:** Yes, M3<br>**Length:** Stock Jato 3.3<br>**Price:** Already owned | Pro: **Already steel and already adjustable.** The Jato 3.3 shipped M3 turnbuckles, which is why the rear never had the snapping problem. Sets rear camber plus a little rear toe. No change needed<br><br>Con: M3 is thinner than the 4mm front, which is fine because the rear sees less impact load | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/steering_traxxas_jato33_m3_camber_link.jpg` |
| ⭐ **4mm steel turnbuckle** — *front, same set as the toe links* | **Type:** Threaded turnbuckle<br>**Material:** Spring/stainless steel<br>**MPN:** TBD<br>**Fits:** Slash 4x4 / Jato 4x4 pattern<br>**Adjustable:** Yes<br>**Length:** Reach the alloy-hub upper mount over the wider track<br>**Price:** TBD | Pro: **Buy it in the same set as the front toe links,** so one 4mm steel order covers both front links. Adjustable camber, survives the hits the plastic did not<br><br>Con: Same open question as the toe links: confirm the length range and the ball-stud fit into the Raptor R alloy carrier upper hole | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/steering_gpm_front_camber_link_4mm.jpg` |

---

## Servo-to-bellcrank link

Already chosen and in hand: **GPM RUS416026ST-S,** spring-steel turnbuckle plus 25T alloy servo horn, 8.0g measured. Full write-up lives in [`steering_bell_crank_analysis.md`](steering_bell_crank_analysis.md#servo-horn--servo-to-bellcrank-link). It is listed here only so the linkage picture is complete. It is not a front steering tie rod and not a camber link, so do not confuse it for one.

<p align="center"><img src="src/steering_gpm_servo_horn_link_rus416026st-s_weight.jpg" width="500"><br><em>GPM RUS416026ST-S, the servo-to-bellcrank link, already in hand. Same steel-turnbuckle family the front toe and camber links should come from.</em></p>

---

## Length reference

The question "what length do we need" has no fixed answer, and that is not a gap in the notes. It is how turnbuckles work.

- **These are threaded rods, not molded parts.** A turnbuckle threads in and out over a range. You set toe (front tie rod) and camber (camber links) by adjusting it on the car. So the thing to buy is an adjustment range, not a length.
- **The front got about 10mm wider per side.** From [`arm_analysis.md`](arm_analysis.md#notes), the FLM26800 front arm measures **101.6mm hole-to-hole vs 92mm stock TRA3655, so +9.6mm/side.** That pushes the front outer ball studs outboard by about that much, so the front links have to reach **stock + 10mm.** A stock-length plastic rod cannot physically get there.
- **The alloy hubs move the mounting point too.** Front runs the Raptor R Ultimate EHD alloy carriers ([`hub_carrier_analysis.md`](hub_carrier_analysis.md)), so the upper (camber) and outer (toe) ball-stud positions follow that geometry, not stock plastic. One more reason to set length on the car, not from a catalog.
- **Rear is unchanged in practice.** Stock Jato 3.3 M3 steel turnbuckles, adjusted for the rear-arm geometry as normal.

**What to actually do at build/test-fit:**

1. Bolt up the FLM front arms and Raptor R alloy hubs.
2. Thread the 4mm front turnbuckles out until the toe link and camber link reach their ball studs with the wheels at target toe and camber.
3. Measure that length once, then log it here so re-orders and spares are a known number instead of a re-measure.

Until step 3 happens, "front is about stock + 10mm, run 4mm steel turnbuckles" is the honest spec.

---

## Price History

| Date | Price | Discount Path | Notes |
|------|-------|---------------|-------|
| — | **TBD** | — | Front 4mm steel turnbuckle set (toe + camber). Not purchased yet. Rear M3 Jato 3.3 steel turnbuckles already in hand, no cost to add |

---

## Notes

- **Front snaps because the arm does not give.** The FLM aluminum arm transfers impact straight into whatever is next in line: bulkhead, tie rods, camber links. Plastic links lose. 4mm steel is the fix, the same reason the rear survives on steel M3 rods. Cross-ref: [`arm_analysis.md`](arm_analysis.md#arm-comparison) (con column) and the "arms as the intended fuse" note in [`arm_analysis.md`](arm_analysis.md#notes).
- **Buy the front links as one order.** The front toe links and front camber links are both 4mm steel turnbuckles, so one set covers both. It is a single line item, not two.
- **Rear is done.** Stock Jato 3.3 M3 steel turnbuckles. It is the one part of the linkage that never needed touching, which is easy to forget when the front is the loud problem.
- **Do not count the servo link twice.** GPM RUS416026ST-S (servo to bellcrank) is already chosen and in hand, and it lives in [`steering_bell_crank_analysis.md`](steering_bell_crank_analysis.md#servo-horn--servo-to-bellcrank-link). It is a different link from the steering tie rods.
- **Log the measured front length after test-fit** and update the [Length reference](#length-reference) and [Price History](#price-history) here. That turns the TBD into a real number for spares.
- **Ball-stud fit is the one thing to verify before ordering.** The rod ends have to seat in the Raptor R alloy carrier holes and the FLM arm studs. Check the ball size when the 4mm set is picked.
