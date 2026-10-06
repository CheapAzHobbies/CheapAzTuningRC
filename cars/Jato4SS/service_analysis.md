# Service Log — Jato 4SS

Real-world failures from actually driving the car, kept separate from the part-selection analysis docs (those cover why a part was picked, not what broke on it in the field). Newest first.

## Current Status

**28 total runs** as of 2026-10-05, 0 runs since the last failure (bell crank, same day). Synced from the [battery tracker](../../batteries/README.md) whenever it updates, not just when something breaks, so this number growing with no new row below is itself the signal that nothing's failed in a while.

---

| Date | Milestone (Total Runs) | What Broke | What Fixed |
|---|---|---|---|
| 2026-10-05 | **28** | **Bell crank locked up**, first of 2 runs today<br>• [GPM 6845X](steering_bell_crank_analysis.md) (TRA3775 bushings) bound up mid-session<br>• Dirt got past the bushing seal into the pivot, packed it solid | • Disassembled, cleaned the dirt out of the pivots, reassembled<br>• Back together, driveable |
| 2026-10-01 | **22** | **Center diff field failure**, 4 batteries run today, broke on the last<br>• [Chassis bearing](differential_analysis.md#center-diff) at the output shaft seized, shaft spun, melted/cracked the **TRA6814** housing, knocked the spur out of true<br>• Measured **10×16×5**, different from the hub bearings ([`bearings_reference.md`](bearings_reference.md))<br>• ⚠️ 2026-10-03 teardown: [rear diff](differential_analysis.md#front--rear-diff-comparison)'s both outdrive bearings also seized, housing damaged/misaligned<br>• 🚧 Probable root cause: rear bearing drag loaded the center diff bearing until it seized too<br>• 🚧 Downstream damage (pinion, CVDs, front diff, gearbox) unconfirmed | • Rebuilding TRA6814: fresh **TRA6884 housing + TRA6883 gear set** (~$20)<br>• Fill switched: 100k oil → **white lithium grease** ([`differential_analysis.md#center-diff-oil`](differential_analysis.md#center-diff-oil))<br>• Spur: 54T TRA3956R → **50T TRA6842R**, cuts rotating mass ([`differential_analysis.md#spur-gear`](differential_analysis.md#spur-gear))<br>• 🚧 Chassis bearing (10×16×5) still needs replacing<br>• 🚧 Rear diff needs new bearings + housing, not yet repaired<br><p align="center"><img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_center_diff_tra6814_cracked_housing.jpg`</p> |
| 2026-09-27 | **18** | **Bent front arm**<br>• Vick collided mid-turn, not a jump impact<br>• [FLM26800 arm](arm_analysis.md#notes) bent, still driveable | • Straightened with two crescent wrenches<br>• Exactly the fuse behavior it was chosen for |

---

## Troubleshooting

General diagnostic notes from driving this car, not tied to one dated incident, carried forward so the next weird symptom gets checked in the right order.

| Symptom | Likely Cause | Check First |
|---|---|---|
| **Motor mesh keeps loosening** after tightening it against the spur | • Usually under-torqued **motor mount screws or pinion set screw**, heat + vibration walks them loose<br>• Failing **center diff bearing** is the other cause, further down the list | • Check if the motor's shifted, retighten + **red threadlocker** (Loctite 262/271)<br>• Check the pinion for loose/spinning, same fix<br>• Tighten the pinion warm if you can, not required<br>• Center diff only if neither moved |
| **Clicking under power**, sounds like it's from the rear | The **center diff**, not the rear diff. Any center diff (AliExpress, Traxxas OEM, etc.) | Center diff first, rear diff bearing second, easiest-to-reach first |

---

## Notes

- **Why separate from the analysis docs:** `<part>_analysis.md` docs are about why a part was chosen; this log is about what actually happened to it under real driving. Keeping failures here instead of buried in a part's Notes section keeps both docs on-topic and gives a single place to check "what's broken on this car and when."
- **Milestone (Total Runs)** is a single number, the cumulative run count when the failure happened, like an odometer reading, not just that day's count (see [`battery_analysis.md`](battery_analysis.md) for the full cycle tracking). Each new entry logs whatever the running total is at that point (22, then the next one might land at 40, and so on), it's not a fixed checkpoint schedule. Same-day detail (which run it broke on, how many today) goes in the What Broke cell instead.
- See also the [README Gallery](README.md#gallery) for the same events with photos, and each linked `<part>_analysis.md` for the part's own spec/comparison context.
- **Current Status updates with every battery log entry**, not just failures. It's the all-time odometer; the gap between it and the last Milestone row is how long the car's gone without breaking anything.
