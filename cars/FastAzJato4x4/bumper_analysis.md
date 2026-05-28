# Bumper Selection — FastAzJato4x4

> **Front: leaning toward OEM Jato 4x4 front bumper.** Counterintuitive logic: the Jato bumper gives almost no real protection, but **if the nose hits the ground hard enough to matter, the car is going to cartwheel anyway**. A minimal bumper means the nose doesn't dig in — gives a chance to **throttle up and recover from a bad landing** instead of pivoting end-over. A bigger bumper digs into the ground and locks you into the cartwheel.
>
> **Tempting alternative: Rustler 4x4 front bumper** — slightly larger, doesn't extend past the wheels (or close to it), so it's still recovery-friendly. The blocker is **it's ugly**. Possible solve: **design a custom front wing mount / cosmetic shroud that integrates the Rustler bumper** so it looks intentional rather than retrofitted.
>
> **Rear: leaning toward Traxxas stock plastic** from the Slash 4x4 / Jato family — exact part number depends on the resolved [wing mount cascade decision](aero_analysis.md#shock-tower-compatibility-cascade).

---

## Table of Contents

- [Key Requirements](#key-requirements) — Must / May for the bumper pick
- [Bumper Comparison](#bumper-comparison) — material families
- [Specific part-number options](#specific-part-number-options) — Slash / Rustler / Jato fits
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Bolts to the CF chassis bumper mount holes** | Must | The chassis is Slash 4x4 pattern, bumpers must match those mount points |
| **Absorbs impact, doesn't transfer to chassis** | Must | Same logic as the shock tower analysis — a sacrificial bumper saves expensive parts |
| **Survives most crashes intact** | May | Cheap to replace either way, but fewer trips to the workbench is nice |
| **Lightweight** | May | Bumpers sit at the extreme ends of the car — every gram amplified for polar moment / handling |
| **Cheap** | May | Bumpers eat crashes; consumable part |

---

## Bumper Comparison

| Material family | Status | Pros / Cons | Notes |
|---|---|---|---|
| **Traxxas stock plastic + foam** (Slash / Rustler / Jato family) | **Candidate (leading)** | Pro: **Sacrificial — flexes and absorbs impact** instead of transferring to the chassis. Foam backing damps high-frequency hits. Cheap, light, widely stocked at every hobby store. Matches the chassis class<br>Con: Cracks under hard impacts; needs occasional replacement | Same "sacrificial-part" reasoning as the chosen Traxxas stock shock towers |
| ~~Aluminum / billet bumpers~~ | **Vetoed** | Pro: Won't break in normal crashes<br>Con: **Transfers all impact to the chassis** (cracks the CF chassis instead of cracking a $5 bumper). Heavy. Sitting at the ends of the car = worst place to add weight (handling penalty). Looks cool, drives worse. **Same aluminum-failure-cascade problem as shock towers** — see [shock tower aluminum nuance](shock_tower_analysis.md#material-properties-reference) | — |
| ~~Carbon fiber bumpers~~ | **Vetoed** | Pro: Stiff, light<br>Con: Brittle failure mode — when CF bumpers break, they explode and transfer the rest of the energy to the chassis. Worst of both worlds for the role bumpers play | — |
| ~~Skipping bumpers entirely~~ | **Ruled Out** | "Saves weight"<br>Con: First crash cracks the chassis. Don't | — |

---

## Specific part-number options

The Slash 4x4 / Rustler 4x4 / Jato 4x4 family share the same bumper mount pattern, so multiple Traxxas part numbers work.

### Front bumper

| Part | Fits | Status | Notes |
|---|---|---|---|
| **TRA5535 — Jato 4x4 front bumper** | Native Jato fit | **Leading** | Minimal profile, low ground contact area = recoverable from bad landings. The "let the car cartwheel only if it really has to" pick |
| TRA5435 — Rustler 4x4 front bumper | Same Slash 4x4 chassis family | Candidate (with custom mount) | Slightly larger than the Jato bumper, doesn't extend past the wheels. Better protection without locking the car into cartwheels. **Ugly stock; would need a custom front wing mount / cosmetic shroud to look intentional** — see [3D Models](README.md#3d-models) TODO |
| TRA6835 — Slash 4x4 front bumper | Slash 4x4 chassis pattern | Vetoed | Larger than the Rustler / Jato; extends further forward = more likely to dig in on a bad landing and trigger a cartwheel. Wrong direction for this build's recovery-focused logic |

### Rear bumper

Rear bumper choice is constrained by the [wing mount cascade decision](aero_analysis.md#shock-tower-compatibility-cascade) — the OEM Jato wing mount and STRC backflash conversion bolt to different rear bumper geometry.

| Part | Fits | Status | Notes |
|---|---|---|---|
| **TRA5536 — Jato 4x4 rear bumper** | Native Jato fit, pairs with OEM Jato wing mount | **Leading if going OEM Jato wing mount** | Same minimal-profile logic as the front |
| TRA6836 — Slash 4x4 rear bumper | Slash 4x4 chassis pattern, pairs with STRC backflash conversion | Candidate (if going STRC conversion) | Use this if the wing mount cascade lands on the STRC option |
| TRA5536 — Rustler 4x4 rear bumper | Same family | Candidate | (Note: same part number as some Jato listings — verify with seller before ordering) |

> All part numbers above are starting points — verify exact fit with the chosen AliExpress CF chassis before ordering. Mount-hole spacing is the key check.

---

## Notes

- **Recovery-focused logic on the front bumper:** a Jato 4x4 hitting nose-first hard enough to need a bumper is already in a bad landing. The bumper's job here isn't to absorb the impact — it's to **not catch the ground and trigger a cartwheel** before you can power out of it. Smaller bumper = less ground contact = better chance to throttle through and save the run.
- **Why no premium / aftermarket bumpers:** the chassis is intended as disposable (~$100 CF). Spending $40-60 on premium bumpers for a chassis you might crash-replace is upside-down value.
- **Sacrificial logic carries over from shock towers:** the chosen direction in this build is "let cheap plastic parts absorb the energy so expensive parts (chassis, diffs, motor) don't have to."
- **Custom front-bumper / wing-mount integration (TODO):** if the Rustler 4x4 front bumper proves to give meaningful crash protection without sacrificing recovery, a custom front-end shroud / wing mount that integrates the bumper would be worth a 3D print. Tracked in [3D Models](README.md#3d-models). Goal: keep the Rustler's better protection geometry while making it look like an intentional part of the car rather than a retrofit.
- **Photos & exact part numbers TBD** — finalize when ordering, based on which specific Jato / Rustler / Slash bumper shape clears the bodywork and arm geometry on the FastAzJato4x4.
