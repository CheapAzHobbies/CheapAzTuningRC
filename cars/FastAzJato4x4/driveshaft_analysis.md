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
| **Traxxas E-Revo 1.0 CVDs (chopped to fit)** | Type: CVD (constant-velocity)<br><br>Part: **TRA5451R** (set of 4) / **TRA5451X** (single)<br><br>Diff end: **6mm**<br><br>Price: **$24.97 set of 4** (Jenny's RC)<br><br>Mod: cut to length and rejoin with a 6mm threaded collet / metal tube (see method below) | **Chosen** | Pro: **Smoothest power delivery through full travel — no U-joint clearance problems.** 6mm, matches the E-Revo diffs and cups. The basis of the whole driveline<br><br>Con: Requires cutting + collet/solder work to shorten. Real Traxxas CVDs cost more than the knock-off | <img src="src/drivetrain_traxxas_e_revo_cvd_5451r.jpg" width="500"> |
| **Knock-off E-Revo 1.0 CVDs (chopped to fit)** | Type: CVD knock-off of TRA5451R<br><br>Diff end: 6mm<br><br>Price: **~$20–28 for a set of 4**<br><br>Mod: same collet / cut-to-length method<br><br>See [Knock-Off E-Revo CVDs](#knock-off-e-revo-cvds) | **Chosen — budget** | Pro: **Set of 4 for $20–28 — fantastic in real use on the E-Revo 1.0.** Indistinguishable from genuine TRA5451R in practice. Same 6mm fitment. Alt: swap diff outdrive to standard if 6mm cups not available<br><br>Con: Same cut + collet work required. Knock-off QC on paper, indistinguishable in practice | <a href="https://www.aliexpress.us/item/3256810555124966.html"><img src="src/drivetrain_knockoff_cvd_rcawd.jpg" width="500"></a> |
| **Traxxas E-Revo 1.0 U-joint shafts (chopped to fit)** | Type: U-joint style<br><br>Diff end: 6mm<br><br>Mod: chopped to fit<br><br>Part numbers: TBD — confirm | Candidate | Pro: 6mm, works, simpler than CVDs<br><br>Con: **Too large — hits the suspension arms at full extension.** Also catches the steering link sometimes. These clearance issues are why the CVDs are chosen over U-joints | <img src="src/drivetrain_traxxas_e_revo_ujoint_shaft.jpg" width="500"> |
| **FLM U-style driveshafts (hardened steel)** | Type: U-joint style<br><br>Material: **hardened steel**<br><br>Part numbers: TBD — confirm | Candidate | Pro: Hardened steel — strongest U-joint option, built for abuse<br><br>Con: Same U-joint clearance caution as the Traxxas U-joint shafts (arm / steering link at full travel) — verify clearance. Pricier than stock | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 couldn't find an FLM product image — save as `src/drivetrain_flm_ujoint_driveshaft.jpg` |
| **Traxxas Slash 4x4 stock axle (1st gen, U-joint)** | Type: stock Slash 4x4 U-joint half shaft<br><br>Part: **TRA6852X** (rear) / **TRA6851X** (front)<br><br>Fitment: 6mm, fits | Candidate | Pro: Cheap, widely available. Fits the build<br><br>Con: **Worst option — snaps like candy.** Only minor rubbing on the arms, not a full clearance hit, but the snapping issue makes this a last resort | <img src="src/drivetrain_traxxas_slash_stock_axle_6852x.jpg" width="500"> |
| **Traxxas Slash 4x4 HD steel CV (2nd gen)** | Type: nickel-plated steel CV w/ boots<br><br>Part: **TRA6851R** (front) / **TRA6852R** (rear)<br><br>U-joint pins held captive<br><br>Price: **$69.95** (set of 2) | Candidate | Pro: Steel CV, boots, captive pins — strong "2nd gen" upgrade, smooth like the E-Revo CVDs<br><br>Con: **Wildly expensive at $69.95.** May need to swap to stock Slash diff outdrives to match — easy swap, but extra step. Confirm 6mm fitment against the E-Revo cups | <img src="src/drivetrain_traxxas_slash_hd_cv_6851r.jpg" width="500"> |
| **Knock-off Slash 4x4 HD Steel CV** | Type: CV knock-off of TRA6851R<br><br>Diff end: 6mm<br><br>Price: **~$20–30 for a set** | Candidate | Pro: $20–30 — fraction of the Traxxas price for the same Steel CV design<br><br>Con: May need to swap to stock Slash diff outdrives — easy swap. QC varies on paper | <img src="src/drivetrain_traxxas_slash_hd_cv_knockoff_tra6851r.jpg" width="500"> |
| **Traxxas Slash 4x4 EHD axles (ok)** | Type: Extreme Heavy Duty telescoping, oversized U-joints<br><br>Part: **TRA6852A** (rear) / **TRA6851A** (front)<br><br>6mm stub axles | Candidate | Pro: Telescoping, oversized U-joints, 6mm stubs. OK for this build<br><br>Con: Nowhere near as strong as the true EHD TRA9051/9052 despite the same "EHD" name | <img src="src/drivetrain_traxxas_slash_ehd_6852a.jpg" width="500"> |
| **TRA9051 / TRA9052** Jato 4x4 VXL EHD Driveshafts | Type: Extreme Heavy Duty, native Jato 4x4 VXL fit<br><br>Part: **TRA9051** (front) / **TRA9052** (rear)<br><br>Set of 4: **90386-4 — $28.97** (Jenny's RC, out of stock)<br><br>Axle: **6mm** | Candidate | Pro: **Stronger than the standard EHD axles** despite sharing the "Extreme Heavy Duty" name. Native Jato 4x4 VXL fit, 6mm axle matches E-Revo diffs. Front + rear covered<br><br>Con: Tends to break at the threads like other axles | <img src="src/drivetrain_traxxas_ehd_driveshaft_tra9052.jpg" width="500"> |

---

## Knock-Off E-Revo CVDs

The knock-off E-Revo 1.0 CVDs run **~$20** and **perform identically to the genuine Traxxas CVDs** — no noticeable difference in real use. Same 6mm diff end, same chopped-to-fit method. For a wear item that gets cut down and rebuilt anyway, the knock-off is the sensible buy.

| Part | Spec | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **Knock-off E-Revo 1.0 CVD set** (e.g. RCAWD) | Diff end: 6mm<br><br>Price: **~$20**<br><br>Source: AliExpress / RCAWD / budget RC sellers<br><br>Part numbers: vary by seller | **Chosen — budget** | Pro: ~$20, works equally as well as genuine. Often ships with wheel hexes + hardware. Cheap enough to keep spares<br><br>Con: QC varies on paper; indistinguishable from OEM in practice | <img src="src/drivetrain_knockoff_cvd_rcawd.jpg" width="500"> |

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
| **Stock Traxxas aluminum (one-piece)** | Material: 6061-T6 aluminum, splined one-piece<br><br>Part: **TRA6755** (silver) / **TRA6855** (blue) | Candidate | Pro: Stock Slash 4x4 center shaft — light, stiff, splines onto the front/rear input shafts with no driveline play<br><br>Con: One-piece (non-telescoping); aluminum can bend in a hard hit | <img src="src/drivetrain_traxxas_center_driveshaft_6755.jpg" width="500"> |
| **Stock plastic / telescoping (dogbone)** | Material: composite/plastic-bodied telescoping<br><br>Part numbers: TBD — confirm | Candidate | Pro: Cheapest, lightest; telescoping absorbs some shock<br><br>Con: Will deform under hard 4S abuse over many packs | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/drivetrain_traxxas_stock_plastic_center_driveshaft.jpg` |
| **Tekno Big Bone aftermarket** | Type: center driveshaft + outdrives<br><br>Part: **TKR6855**<br><br>Material: hardened steel | Candidate | Pro: Best build quality, definitive durability win<br><br>Con: Most expensive — overkill for casual use | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 Tekno site blocked the image fetch — save as `src/drivetrain_tekno_center_driveshaft_tkr6855.jpg` |

---

## Notes

- **Why CVDs over U-joints:** the E-Revo 1.0 U-joint shafts (and FLM hardened-steel U-joints) work, but the U-joint **hits the suspension arm at full travel and catches the steering link** sometimes. The CVDs deliver power smoothly through the whole travel range without that clearance problem — that's why they're the pick.
- **Real vs knock-off CVD:** both work equally well. The ~$20 knock-off is the value choice since the shaft gets cut down and rebuilt anyway.
- **Collet pick logic:** threaded 6mm collet = cleanest, strongest join. Metal tube + solder = fallback if you don't have a collet. Either way, measure twice, cut once.
- **Center driveshaft pick logic:** bashing → stock plastic. Most builds → stock metal (best value). Race / heavy 4S abuse → Tekno. Breaks rarely and doesn't park the car when it does.
- **Confirmed part numbers:** E-Revo CVD = **TRA5451R/5451X**; Slash stock U-joint axle = **TRA6852X/6851X**; Slash HD steel CV = **TRA6852R/6851R**; Slash EHD = **TRA6852A/6851A**; alum center driveshaft = **TRA6755/6855**; Tekno center = **TKR6855**.
- **Still TBD:** the E-Revo U-joint shaft number, the FLM part number, and the plastic/telescoping center driveshaft number. Also verify 6mm fitment for the Slash axles against the E-Revo cups.
- **Images still needed:** E-Revo U-joint shaft, FLM hardened-steel driveshaft, plastic center driveshaft, and the Tekno TKR6855 (its site blocked the fetch).
