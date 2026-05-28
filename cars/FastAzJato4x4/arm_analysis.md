# Suspension Arm Selection — FastAzJato4x4

> **Tracked in-build pick: FLM Rustler rear extended arms (USA-made)** — already referenced in the build description. Pick TBD pending direct comparison of all five variants below. Five known options total in this analysis; two TBD slots flagged for the variants the user hasn't recalled yet.

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Arm Comparison](#arm-comparison) — 5 variants (3 known + 2 TBD)
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Fits Slash 4x4 / Jato 4x4 hinge pin + mount geometry** | Must | Has to bolt to the chosen CF chassis bulkheads + accept stock-pattern hinge pins, ball studs, shock mount points |
| **Handles 4S 1/10–1/8 class loads** | Must | Hard landings on the 1/8-buggy-class Jato chassis stress arms more than typical 1/10 SCT use |
| **Doesn't shatter on impact** | Must | Arms breaking mid-run is a tow-back; need ductile failure (bend / crack progressively) not catastrophic snap |
| **Reasonable wheelbase / track width** | Must | Extended arms increase wheelbase / track — affects body fit, drivetrain length (CVDs), and overall handling balance |
| **Stiff under cornering load** | May | Less arm flex = sharper steering response, but more flex = more impact compliance. Race vs basher trade |
| **Cheap / available** | May | Arms are top-3 most-broken parts on a hard-driven 4S build |
| **Front + rear both available** | May | Mixing-and-matching front vs rear from different vendors complicates geometry tuning |

---

## Arm Comparison

| Arm | Length / Material | Status | Pros / Cons | Photo / Link |
|---|---|---|---|---|
| **FLM Rustler rear extended arms (USA-made)** | Extended length, **bendable** (deforms instead of snapping; can be reshaped back to general geometry by hand after crashes — per user experience on prior builds) | **Candidate (in build description, likely lead)** | Pro: Specialty extended-length arms designed for the Rustler rear that work well on the Jato 4x4 chassis for the 1/8-buggy-class wheelbase. USA-made, premium QC, well-regarded in the racing community. Extended length suits the FastAzJato4x4 build target. **The expected first-to-break part on this build — but they bend instead of shattering, and you can roughly reshape them back and keep driving.** Better failure mode than catastrophic snap<br>Con: Pricier than stock, harder to source, rear only (front needs paired option). Reshaped arms aren't back to factory geometry — fine for bashing, not ideal for racing precision | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/suspension_flm_rustler_rear_extended_arms.jpg` |
| **Traxxas Slash 4x4 OEM arms** (original, older spec) | Stock length, glass-filled nylon | Candidate | Pro: **Stiff** — best for sharp steering response and consistent geometry under cornering load. Cheapest option, widely stocked at every hobby store, well-tested<br>Con: **Breaks more easily** — the stiffness comes from a more brittle nylon mix. Big crashes / hard landings can snap an arm where the EHD would just flex | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/suspension_traxxas_slash_4x4_oem_arms.jpg` |
| **Traxxas Slash 4x4 EHD (Extreme Heavy Duty) arms** | Stock length, reinforced nylon with rubber-toughened additive | Candidate | Pro: **Stronger / more durable** — the rubber additive lets the arm flex slightly under impact instead of snapping. Survives crashes that would break the OEM<br>Con: **Flexes a bit more** under cornering load — small loss of steering precision vs the OEM, but most drivers won't notice on dirt | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="300"><br>🚧 save as `src/suspension_traxxas_slash_4x4_ehd_arms.jpg` |
| **TBD — variant #4** | TBD | TBD | User-flagged: there are two more variants in the comparison that need to be filled in once recalled. Likely candidates: RPM aftermarket, Traxxas Rustler 4x4 stock, Traxxas Jato 4x4 stock, or GPM aluminum | — |
| **TBD — variant #5** | TBD | TBD | (Second of the two user-flagged TBD variants) | — |

---

## Notes

- **OEM vs EHD trade**: stiffer = more precise but more breakable; flexier = more durable but slightly vaguer steering feel. The classic plastic-formulation trade-off — same physics as the [shock tower aluminum-vs-composite discussion](shock_tower_analysis.md#material-properties-reference) but with two flavors of plastic instead of two materials.
- **Why aluminum arms aren't in this analysis**: arms see large bending loads on landings. Aluminum arms transfer those loads to the chassis mounts / bulkheads (same failure-cascade logic as the [shock tower analysis](shock_tower_analysis.md#material-properties-reference)), and even when they don't break they bend permanently and throw geometry off. Plastic arms — both OEM and EHD — are the right material for the role.
- **RPM arms (when added to the comparison)** — known for tougher-than-stock plastic, slightly heavier, multi-color options. Sit between OEM stiffness and EHD compliance.
- **Front-rear matching**: keep front and rear arms in the same family / generation if possible. Mixing stock-length OEM front with FLM extended rear changes geometry intentionally; mixing stiff fronts with flex rears unintentionally couples handling feel to terrain in ways that are hard to tune out.
- **CVD compatibility**: the chosen E-Revo CVDs are already chopped to fit the FastAzJato4x4. Changing arm length (FLM extended rear, for example) may re-affect CVD length — verify before finalizing.
- **Photos & TBD variants**: this analysis is partial. Fill in the two TBD rows once the user recalls them and we'll narrow to a final pick.
