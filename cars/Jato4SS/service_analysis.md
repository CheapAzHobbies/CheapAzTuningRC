# Service Log — Jato 4SS

Real-world failures from actually driving the car, kept separate from the part-selection analysis docs (those cover why a part was picked, not what broke on it in the field). Newest first.

| Date | Milestone (Total Runs) | What Broke | What Fixed |
|---|---|---|---|
| 2026-10-01 | **22 total runs** on the Gens Ace Redline 6000 pair (4 of those today, broke on the last) | **Center diff field failure.** The chassis-mounted bearing the [center diff](differential_analysis.md#center-diff)'s output shaft passes through on its way to the [center driveshaft (7455)](driveshaft_analysis.md#center-driveshaft-comparison), bundled with that shaft's take-off kit, not one of the diff's own internal bearings, seized. The output shaft spun against it instead of the bearing turning in its seat, and the friction heat melted/damaged material right at that point. That knocked the shaft (and the spur on the end of it) out of true alignment, which put the spur at a weird angle and ultimately cracked the **TRA6814** housing. ⚠️ This bearing is a different size than the MonsterKingz / OEM hub bearings already documented (see [`bearings_reference.md`](bearings_reference.md)); 🚧 exact size not yet measured. 🚧 Whether anything downstream (pinion, CVDs, gearbox housing) also took damage isn't confirmed | Rebuilding the TRA6814 with a fresh **TRA6884 housing + TRA6883 gear set** (~$20). 🚧 The seized chassis bearing itself still needs replacing, a new housing alone won't fix a repeat if that isn't also swapped. <p align="center"><img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_center_diff_tra6814_cracked_housing.jpg`</p> |
| 2026-09-27 | 🚧 not logged | **Bent front arm.** Vick collided with the car mid-turn on the track, not a jump impact. The [FLM26800 arm](arm_analysis.md#notes) bent, still driveable, not snapped | Straightened with two crescent wrenches (or a hammer and anvil). Exactly the fuse behavior the arm choice was made for, the first real incident logged against it |

---

## Notes

- **Why separate from the analysis docs:** `<part>_analysis.md` docs are about why a part was chosen; this log is about what actually happened to it under real driving. Keeping failures here instead of buried in a part's Notes section keeps both docs on-topic and gives a single place to check "what's broken on this car and when."
- **Milestone (Total Runs)** is a mile-marker, the cumulative run count on the pack(s) in use when the failure happened, like an odometer reading, not just that day's count (see [`battery_analysis.md`](battery_analysis.md) for the full cycle tracking).
- See also the [README Gallery](README.md#gallery) for the same events with photos, and each linked `<part>_analysis.md` for the part's own spec/comparison context.
