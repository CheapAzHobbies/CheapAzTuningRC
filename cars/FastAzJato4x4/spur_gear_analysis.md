# Spur Gear Selection — FastAzJato4x4

> **Chosen: Plastic OEM spur gear (TRA6842R 50T or TRA6843 52T)** — plastic is correct by design. The spur gear is the intentional sacrificial failure point in the drivetrain. In a bad crash it strips before transferring force to the metal pinion, driveshafts, and gearbox — protecting far more expensive parts. Lasts a long time under normal use and is dirt cheap to replace.

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Spur Gear Comparison](#spur-gear-comparison)
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Plastic material** | Must | Plastic is the **intentional sacrificial failure point** — strips in a crash before the metal pinion, driveshafts, or gearbox take the hit. Metal spur gears transfer crash energy into more expensive components |
| **32P / 0.8M pitch** | Must | Slash 4x4 / Jato 4x4 platform standard — all gearbox housings and pinions use this pitch |
| **No slipper clutch** | Must | Slipper clutch works on high-grip surfaces — doesn't handle well on dirt tracks. This build is set up for dirt/low-grip offroad. Center diff (TRA6814) is the correct setup |
| **Fits Slash 4x4 / Jato 4x4 center diff gearbox** | Must | Must seat correctly in the center diff housing (TRA6814 / TRA6884) |
| **Cheap** | Must | It's a consumable part. At $3–5 it should be guilt-free to replace |
| **Correct tooth count for desired gear ratio** | May | Tooth count affects top speed vs torque — tune to motor KV and track conditions |

---

## Spur Gear Comparison

| Spur Gear | Spec | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **TRA6842R — 50T plastic** | Teeth: **50T**<br><br>Pitch: 32P / 0.8M<br><br>Material: plastic<br><br>Price: **~$3** | Candidate | Pro: Cheap, correct material, correct pitch. 50T gives a slightly taller ratio vs 54T<br><br>Con: — | <img src="../../K939/src/drivetrain_traxxas_spur_gear_tra6842r_50t.png" width="500"> |
| **TRA6843 — 52T plastic** | Teeth: **52T**<br><br>Pitch: 32P / 0.8M<br><br>Material: plastic<br><br>Price: **~$3** | Candidate | Pro: Cheap, correct material. 52T splits the difference between 50T and 54T<br><br>Con: — | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_spur_gear_tra6843_52t.jpg` |
| ~~**TRA3956 / TRA3956R — 54T plastic (slipper)**~~ | Teeth: 54T<br><br>Pitch: 32P / 0.8M<br><br>Material: plastic<br><br>Type: slipper clutch assembly<br><br>Price: ~$22 | Vetoed | Pro: 54T stock ratio<br><br>Con: **Slipper clutch doesn't handle well on dirt/low-grip tracks** — only effective on high-grip surfaces. This build is for dirt offroad. Center diff is the correct setup | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_spur_gear_tra3956_54t.jpg` |
| ~~**TRA6878A — Complete Slipper Clutch**~~ | Part: **TRA6878A**<br><br>Type: complete slipper clutch assembly<br><br>Price: **$20.00** | Vetoed | Pro: Works well on high-grip surfaces<br><br>Con: **Doesn't handle well on dirt/low-grip tracks** — this build is set up for dirt offroad, not high-grip. Center diff (TRA6814) is the correct setup | <img src="src/drivetrain_traxxas_slipper_clutch_tra6878a.jpg" width="500"> | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_slipper_clutch_tra6878a.jpg` |
| ~~**Hot Racing SSLF254D — 54T steel**~~ | Teeth: 54T<br><br>Pitch: 32P / 0.8M<br><br>Material: hardened steel<br><br>Price: ~$15 | Vetoed | Pro: Won't strip under abuse<br><br>Con: **Wrong design philosophy** — metal spur transfers crash energy to the pinion and drivelines instead of stripping. Defeats the purpose of having a sacrificial failure point | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_hot_racing_spur_gear_sslf254d.jpg` |
| ~~**GPM SSLA054T — 54T steel**~~ | Teeth: 54T<br><br>Pitch: 32P / 0.8M<br><br>Material: hardened steel<br><br>Price: $19.90 | Vetoed | Pro: CNC machined, black finish<br><br>Con: Same metal spur problem — no sacrificial failure point. More expensive than plastic for a worse outcome | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_gpm_spur_gear_ssla054t.jpg` |
| ~~**Integy T8573 — 50T steel**~~ | Teeth: 50T<br><br>Pitch: 32P / 0.8M<br><br>Material: billet steel<br><br>Price: $26.99 | Vetoed | Pro: Billet steel construction<br><br>Con: Metal spur — wrong failure mode. $26.99 for a part that should cost $3 and be plastic | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_integy_spur_gear_t8573.jpg` |
| ~~**Robinson Racing RRP7954 — 54T steel**~~ | Teeth: 54T<br><br>Pitch: 32P / 0.8M<br><br>Material: hardened steel<br><br>Price: ~$30–35 | Vetoed | Pro: Premium machined steel<br><br>Con: Same metal spur problem. Most expensive option for the worst outcome | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_robinson_racing_spur_gear_rrp7954.jpg` |

---

## Notes

- **Why plastic wins:** the spur gear is the least expensive, most accessible part in the drivetrain chain. In a crash, it strips first — before the pinion, CVDs, diff outdrives, or gearbox housing take the hit. A $3 spur gear saving a $30 pinion and $80 in CVD/driveline parts is exactly the right trade-off.
- **Metal spur = wrong failure mode:** a metal spur that won't strip transfers crash energy directly into the pinion and downstream drivetrain. You save the $3 plastic gear and destroy far more expensive parts.
- **Tooth count and gear ratio:** all 32P / 0.8M gears are compatible. Choose tooth count based on motor KV and desired top speed vs torque balance. 50T–54T is the standard range for 4S offroad builds.
- **Slipper vs center diff:** slipper clutch (TRA6878A) works on high-grip surfaces but doesn't handle well on dirt/low-grip tracks — this build is set up for dirt offroad. Center diff (TRA6814) is the correct setup. Use center-diff specific spur gears (TRA6842R, TRA6843) which seat directly in the center diff housing, not slipper assembly gears (TRA3956).
