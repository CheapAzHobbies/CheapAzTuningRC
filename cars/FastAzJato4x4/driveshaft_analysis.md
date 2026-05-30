# Driveshaft Selection — FastAzJato4x4

> **Chosen:**
> - **Axle (wheel) driveshafts: E-Revo 1.0 CVDs, chopped to fit.** Real or the ~$20 knock-off — both work equally well. Shortened with a 6mm threaded collet (or metal tube): thread/solder both cut ends into the collet to the right length. 6mm to match the E-Revo diffs and cups.
> - **Center driveshaft: pick on price and availability** — all options work, consequence-free choice.

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Axle (Wheel) Driveshaft Comparison](#axle-wheel-driveshaft-comparison)
- [Knock-Off E-Revo CVDs](#knock-off-e-revo-cvds)
- [Shortening E-Revo CVDs (collet method)](#shortening-e-revo-cvds-collet-method)
- [Center Driveshaft Comparison](#center-driveshaft-comparison)
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **6mm at the diff end** | Must | Must mate the chosen E-Revo 1.0 **6mm** diff outdrives and cups (see [`differential_analysis.md`](differential_analysis.md)). The whole driveline is built around 6mm |
| **Fits Jato 4x4 hub / wheel end** | Must | Outer end has to seat the wheel hex / stub axle without modification |
| **Clears the arm + steering link at full travel** | Must | U-joint style shafts can foul the suspension arm at full droop and catch the steering link — must clear through the whole travel range |
| **Survives 4S power** | Must | Has to transmit full torque without twisting or stripping |
| **Cheap / available** | May | Wear item — the ~$20 knock-off CVD route keeps replacements painless |

---

## Axle (Wheel) Driveshaft Comparison

| Driveshaft | Spec | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **Traxxas E-Revo 1.0 CVDs (chopped to fit)** | Type: CVD (constant-velocity)<br><br>Diff end: **6mm**<br><br>Mod: cut to length and rejoin with a 6mm threaded collet / metal tube (see method below)<br><br>Part numbers: TBD — confirm | **Chosen** | Pro: **Smoothest power delivery through full travel — no U-joint clearance problems.** 6mm, matches the E-Revo diffs and cups. The basis of the whole driveline<br><br>Con: Requires cutting + collet/solder work to shorten. Real Traxxas CVDs cost more than the knock-off | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_e_revo_cvd.jpg` |
| **Knock-off E-Revo 1.0 CVDs (chopped to fit)** | Type: CVD knock-off<br><br>Diff end: 6mm<br><br>Price: **~$20**<br><br>Mod: same collet / cut-to-length method<br><br>See [Knock-Off E-Revo CVDs](#knock-off-e-revo-cvds) | **Chosen — budget** | Pro: **~$20 and works equally as well as the real E-Revo CVDs.** No noticeable difference in use. Same 6mm fitment<br><br>Con: Same cut + collet work required. Knock-off QC on paper, but indistinguishable in practice | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_knockoff_e_revo_cvd.jpg` |
| **Traxxas E-Revo 1.0 U-joint shafts (chopped to fit)** | Type: U-joint style<br><br>Diff end: 6mm<br><br>Mod: chopped to fit<br><br>Part numbers: TBD — confirm | Candidate | Pro: 6mm, works, simpler than CVDs<br><br>Con: **U-joint hits the suspension arm at full travel** and **catches the steering link sometimes** — the clearance issue that pushes the CVDs ahead of it | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_e_revo_ujoint_shaft.jpg` |
| **FLM U-style driveshafts (hardened steel)** | Type: U-joint style<br><br>Material: **hardened steel**<br><br>Part numbers: TBD — confirm | Candidate | Pro: Hardened steel — strongest U-joint option, built for abuse<br><br>Con: Same U-joint clearance caution as the Traxxas U-joint shafts (arm / steering link at full travel) — verify clearance. Pricier than stock | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_flm_ujoint_driveshaft.jpg` |
| **Traxxas Slash 4x4 1st-gen axles** | Type: stock Slash 4x4 (1st gen)<br><br>Part numbers: TBD — confirm<br><br>Fitment: confirm pin size vs E-Revo 6mm cups | Candidate | Pro: Cheap, widely available stock part<br><br>Con: Confirm 6mm fitment against the E-Revo cups before committing | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_slash_1stgen_axle.jpg` |
| **Traxxas Slash 4x4 2nd-gen axles (EHD ok)** | Type: stock Slash 4x4 (2nd gen)<br><br>**EHD (Extreme Heavy Duty) axles are also ok**<br><br>Part numbers: TBD — confirm | Candidate | Pro: Newer stock axle, EHD version is the heavy-duty upgrade and works fine here<br><br>Con: Confirm 6mm fitment against the E-Revo cups before committing | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_slash_2ndgen_axle.jpg` |

---

## Knock-Off E-Revo CVDs

The knock-off E-Revo 1.0 CVDs run **~$20** and **perform identically to the genuine Traxxas CVDs** — no noticeable difference in real use. Same 6mm diff end, same chopped-to-fit method. For a wear item that gets cut down and rebuilt anyway, the knock-off is the sensible buy.

| Part | Spec | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **Knock-off E-Revo 1.0 CVD set** | Diff end: 6mm<br><br>Price: **~$20**<br><br>Source: AliExpress / budget RC sellers<br><br>Part numbers: TBD — confirm | **Chosen — budget** | Pro: ~$20, works equally as well as genuine. Cheap enough to keep spares<br><br>Con: QC varies on paper; indistinguishable from OEM in practice | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_knockoff_e_revo_cvd.jpg` |

---

## Shortening E-Revo CVDs (collet method)

The E-Revo 1.0 CVDs are longer than the Jato 4x4 needs, so they get **cut down to length** and rejoined. Two ways:

1. **6mm threaded collet** — cut both ends, thread the two cut ends, and thread them into the collet to set the exact length. The collet is the coupler in the middle.
2. **6mm metal tube** — slide the cut ends into a metal tube and **solder them together** at the right length.

Either way the goal is the same: shorten the E-Revo CVD to the correct Jato 4x4 length while keeping it concentric and strong. Thread + collet is cleanest; solder + tube is the fallback. Measure against the installed diff and hub before cutting — cut once.

---

## Center Driveshaft Comparison

**Take: pick on price and availability — all options work.** This is the diff-to-diff shaft, not the wheel axles. Differences come down to durability under abuse, not performance.

| Driveshaft | Spec | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **Stock Traxxas plastic** | Material: plastic<br><br>Part numbers: TBD | Candidate | Pro: Cheapest, lightest<br><br>Con: Will deform under hard 4S abuse over many packs | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_stock_plastic_center_driveshaft.jpg` |
| **Stock Traxxas metal** | Material: steel<br><br>Part numbers: TBD | Candidate | Pro: More durable than plastic, ~10g weight penalty<br><br>Con: Slightly more expensive than plastic | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_stock_metal_center_driveshaft.jpg` |
| **Tekno aftermarket** | Material: hardened steel<br><br>Part numbers: TBD | Candidate | Pro: Best build quality, definitive durability win<br><br>Con: Most expensive — overkill for casual use | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_tekno_center_driveshaft.jpg` |

---

## Notes

- **Why CVDs over U-joints:** the E-Revo 1.0 U-joint shafts (and FLM hardened-steel U-joints) work, but the U-joint **hits the suspension arm at full travel and catches the steering link** sometimes. The CVDs deliver power smoothly through the whole travel range without that clearance problem — that's why they're the pick.
- **Real vs knock-off CVD:** both work equally well. The ~$20 knock-off is the value choice since the shaft gets cut down and rebuilt anyway.
- **Collet pick logic:** threaded 6mm collet = cleanest, strongest join. Metal tube + solder = fallback if you don't have a collet. Either way, measure twice, cut once.
- **Center driveshaft pick logic:** bashing → stock plastic. Most builds → stock metal (best value). Race / heavy 4S abuse → Tekno. Breaks rarely and doesn't park the car when it does.
- **Part numbers still TBD** — E-Revo CVD / U-joint shaft numbers, FLM part number, and the Slash 1st/2nd-gen + EHD axle numbers need confirming. Also verify 6mm fitment for the Slash axles against the E-Revo cups.
