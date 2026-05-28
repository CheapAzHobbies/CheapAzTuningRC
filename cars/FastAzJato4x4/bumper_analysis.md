# Bumper Selection — FastAzJato4x4

> **Front + rear: leaning toward OEM Traxxas 9044 Front + Rear Skid Plates set ($7 for both pieces).** Sold as a single front+rear set — same part the K939 build already uses. Minimal-profile and dirt-cheap. Counterintuitive logic: gives almost no real impact protection, but **if the nose or tail hits the ground hard enough to matter, the car is going to cartwheel anyway**. A minimal bumper means the chassis end doesn't dig in — gives a chance to **throttle up and recover from a bad landing** instead of pivoting end-over.
>
> **You can't skip the bumpers entirely.** **The Traxxas bumpers retain the hinge pins on this chassis family** — without a bumper, the hinge pins migrate out of their bores and the arms come loose. Skipping them isn't a weight-saving option, it's a mechanical failure. They barely save any weight anyway.
>
> **Tempting front alternative: Rustler 4x4 front bumper (Traxxas TRA5435)** — slightly larger, doesn't extend past the wheels (or close to it), so it's still recovery-friendly. The blocker is **it's ugly**. Possible solve: **design a custom front wing mount / cosmetic shroud that integrates the Rustler bumper** so it looks intentional rather than retrofitted.

<p align="center"><img src="src/bumpers_traxxas_skid_plates_tra9044.jpg" width="400"><br><em>Traxxas TRA9044 Front + Rear Skid Plates — $7 for the set</em></p>

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Bumper Comparison](#bumper-comparison) — material families
- [Specific part-number options](#specific-part-number-options) — Slash / Rustler / Jato fits
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Retains the hinge pins** | Must | **The Traxxas bumpers on this chassis family hold the front and rear hinge pins in their bores.** No bumper = pins migrate = arms come loose = car is dead. This is a hard mechanical requirement, not a crash-protection one |
| **Bolts to the CF chassis bumper mount holes** | Must | The chassis is Slash 4x4 pattern, bumpers must match those mount points |
| **Doesn't put shocks in the crash path** | Must | Already broke an HPI Vorza 97mm shock on a rear-end hit with the back-side-shock geometry — avoid repeating |
| **Cheap** | Must | Bumpers double as skid plates on this build — they wear through use, not just crashes. Cheap = guilt-free replacement |
| **Absorbs impact, doesn't transfer to chassis** | May | Same logic as the shock tower analysis — a sacrificial bumper is nice for chassis longevity but the chassis is already disposable (~$100 CF), so this is a "nice to have" not a hard requirement |
| **Survives most crashes intact** | May | Cheap to replace either way, but fewer trips to the workbench is nice |
| **Lightweight** | May | Bumpers sit low on the chassis (not the worst place for weight), and skipping them isn't viable for mechanical reasons anyway — small lever to optimize |
| **Looks intentional** | May | Cosmetics. Rustler front bumper crushes on protection but loses on looks — drives the custom-shroud idea |

---

## Bumper Comparison

| Material family | Status | Pros / Cons | Notes |
|---|---|---|---|
| **Traxxas stock plastic + foam** (Slash / Rustler / Jato family) | **Leading** | Pro: Cheap, light, sacrificial. Widely stocked at every hobby store. Matches the chassis class. **Multi-role: front bumper also takes ground hits as a quasi-skid; stock Jato rear skid plate replaces a separate rear bumper entirely**<br>Con: Cracks under hard impacts; needs occasional replacement | Same "cheap consumable" reasoning as the chosen Traxxas stock shock towers |
| ~~Aluminum / billet bumpers~~ | **Vetoed** | Pro: Won't break in normal crashes. **Weight isn't the issue here** — bumpers sit low on the chassis (unlike shock towers up high), so the CG / handling penalty for aluminum is small<br>Con: **Bends instead of breaking — and once bent, it stays bent and looks bad permanently.** Can't reshape aluminum back to factory by hand; you live with the crooked bumper or replace it (at much higher cost than a $5 plastic). Plus the chassis-cascade problem (transfers impact to the CF chassis instead of cracking sacrificially) — see [shock tower aluminum nuance](shock_tower_analysis.md#material-properties-reference) | — |
| ~~Carbon fiber bumpers~~ | **Vetoed** | Pro: Stiff, light<br>Con: Brittle failure mode — when CF bumpers break, they explode and transfer the rest of the energy to the chassis. Worst of both worlds for the role bumpers play | — |
| ~~Skipping the bumpers entirely~~ | **Ruled Out** | Pro: "Saves weight"<br>Con: **Not actually a weight-savings option — the Traxxas bumpers retain the hinge pins on this chassis family.** No bumper = pins migrate out = arms come loose. Cars die from this. And weight savings is minimal anyway since the bumpers are tiny plastic parts | — |

---

## Specific part-number options

The Slash 4x4 / Rustler 4x4 / Jato 4x4 family share the same bumper mount pattern, so multiple Traxxas part numbers work.

### OEM set (front + rear together)

| Part | Fits | Status | Price | Notes |
|---|---|---|---|---|
| **TRA9044 — Traxxas Front + Rear Skid Plates** | Native Slash 4x4 / Jato 4x4 family fit | **Leading** | **$7.00** for the pair | Sold as a single set with both pieces — same part the [K939 build](../K939/README.md) already uses. Minimal profile, light, cheap, holds the hinge pins. Default pick |

### Alternative front bumper (cosmetic / protection upgrade)

| Part | Fits | Status | Price | Notes |
|---|---|---|---|---|
| **TRA5435 — Rustler 4x4 front bumper** | Same Slash 4x4 chassis family | Candidate (with custom mount) | ~$8-10 | Slightly larger than the TRA9044 front, doesn't extend past the wheels. Better protection without locking the car into cartwheels. **Ugly stock; would need a custom front wing mount / cosmetic shroud to look intentional** — see [3D Models](README.md#3d-models) TODO. Would replace the TRA9044's front piece while keeping the rear |
| **TRA5535 — original 2WD Jato front bumper** | Native to the original 2WD Jato. **Not a direct fit on the Jato 4x4 — can be drilled to fit** | Candidate (with drilling) | ~$6-8 | An option if you want the 2WD Jato's specific front-end aesthetic on the 4x4 chassis. Mounting holes don't line up out of the box; needs the user to drill new mount holes through the bumper to match the Jato 4x4 / Slash 4x4 chassis pattern. Cheap and direct labor — nothing exotic |
| ~~TRA6835 — Slash 4x4 front bumper~~ | Slash 4x4 chassis pattern | Vetoed | ~$8 | Larger than the Rustler / TRA9044 front; extends further forward = more likely to dig in on a bad landing and trigger a cartwheel. Wrong direction for this build's recovery-focused logic |

> Verify exact fit with the chosen AliExpress CF chassis before ordering. Mount-hole spacing is the key check. **TRA9044 ships as a pair (front + rear), so ordering one part number covers both ends.**

---

## Notes

- **Hinge-pin retention is the hard requirement.** The Traxxas Slash 4x4 / Jato 4x4 family of bumpers includes integrated retainers that hold the front and rear arm hinge pins in their bores. **Skipping the bumpers is not viable** — pins walk out, arms come loose, car dies. This is the Must that locks bumpers into the BOM regardless of any crash-protection argument.
- **Recovery-focused logic on the front bumper:** a Jato 4x4 hitting nose-first hard enough to need a bumper is already in a bad landing. The bumper's job here isn't to absorb the impact — it's to **not catch the ground and trigger a cartwheel** before you can power out of it. Smaller bumper = less ground contact = better chance to throttle through and save the run.
- **Why no premium / aftermarket bumpers:** the chassis is intended as disposable (~$100 CF). Spending $40-60 on premium bumpers for a chassis you might crash-replace is upside-down value.
- **Sacrificial logic still matters but isn't a Must:** with a disposable CF chassis, the "save the expensive chassis" argument for sacrificial bumpers softens — the chassis isn't expensive enough to engineer around. Bumpers being cheap matters more than them being sacrificial in the strict shock-tower sense.
- **Custom front-bumper / wing-mount integration (TODO):** if the Rustler 4x4 front bumper proves to give meaningful crash protection without sacrificing recovery, a custom front-end shroud / wing mount that integrates the bumper would be worth a 3D print. Tracked in [3D Models](README.md#3d-models). Goal: keep the Rustler's better protection geometry while making it look like an intentional part of the car rather than a retrofit.
- **Photos:** TRA9044 set photo wired in (shared with the K939 build's same part). 🚧 Need image for the Rustler 4x4 alternative front bumper (TRA5435) if the custom-shroud option proceeds — save as `src/bumpers_traxxas_rustler_4x4_front_tra5435.jpg` when available.
