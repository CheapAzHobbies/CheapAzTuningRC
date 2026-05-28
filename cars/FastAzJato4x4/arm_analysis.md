# Suspension Arm Selection — FastAzJato4x4

> **Chosen: FLM Extended Rear Arms FLM26800** — the only rear arm that extends the wheelbase ~10mm per side. That extra droop and width is the main reason this Jato competes against expensive purpose-built buggies. Metal arms normally transfer force to hinge pins and break other things, but these bend instead of snap — you pound them back into shape and you're still in the race. Extensively tested: lots of wrecks, sometimes bent, always reshaped and back on track. Makes the car feel super rigid, like a proper race car, at a fraction of buggy weight.

<p align="center">
  <img src="src/suspension_flm_rustler_rear_extended_arms_flm26800.jpg" width="600"><br>
  <em>FLM Extended Rear Arms FLM26800 — $30, Made in USA</em>
</p>

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
| **FLM Extended Rear Arms** FLM26800 | CNC billet 6061 aluminum. Extended length: +~10mm wheelbase per arm. Pin-to-pin: 78.1mm / 82.55mm (adjustable width). Extra shock positions. Made in USA. $30.00 (list $40.00) | **Chosen** | Pro: **Only arm that extends the wheelbase** — ~10mm per side increases droop by a large margin, massive handling improvement. Makes the Jato feel like a proper race car vs expensive buggies at a fraction of the weight. Extensively tested: bent many times in hard wrecks, always pounded back into shape and continued racing. **Bends instead of snaps — you're still in the race with a bent arm, not stranded with a broken one.** Adjustable width, extra shock positions, USA-made CNC quality<br><br>Con: Metal arms can transfer more force to hinge pins than nylon. Rear only — front needs a separate solution. Harder to source than Traxxas stock. Bent arms are close to geometry but never perfect — acceptable for bashing, less ideal for precision racing | <img src="src/suspension_flm_rustler_rear_extended_arms_flm26800.jpg" width="500"> |
| **Traxxas Slash 4x4 OEM arms** (original, older spec) | Stock length, glass-filled nylon | Candidate | Pro: **Stiff** — best for sharp steering response and consistent geometry under cornering load. Cheapest option, widely stocked at every hobby store, well-tested<br><br>Con: **Breaks more easily** — the stiffness comes from a more brittle nylon mix. Big crashes / hard landings can snap an arm where the EHD would just flex | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/suspension_traxxas_slash_4x4_oem_arms.jpg` |
| **Traxxas Slash 4x4 EHD (Extreme Heavy Duty) arms** | Stock length, reinforced nylon with rubber-toughened additive | Candidate | Pro: **Stronger / more durable** — the rubber additive lets the arm flex slightly under impact instead of snapping. Survives crashes that would break the OEM<br><br>Con: **Flexes a bit more** under cornering load — small loss of steering precision vs the OEM, but most drivers won't notice on dirt | <img src="https://placehold.co/300x200/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/suspension_traxxas_slash_4x4_ehd_arms.jpg` |
| **TBD — variant #4** | TBD | TBD | User-flagged: there are two more variants in the comparison that need to be filled in once recalled. Likely candidates: RPM aftermarket, Traxxas Rustler 4x4 stock, Traxxas Jato 4x4 stock, or GPM aluminum | — |
| **TBD — variant #5** | TBD | TBD | (Second of the two user-flagged TBD variants) | — |

---

## Notes

- **OEM vs EHD trade**: stiffer = more precise but more breakable; flexier = more durable but slightly vaguer steering feel. The classic plastic-formulation trade-off — same physics as the [shock tower aluminum-vs-composite discussion](shock_tower_analysis.md#material-properties-reference) but with two flavors of plastic instead of two materials.
- **Arms as the intended fuse:** on this build the design intent is that **arms give way first**, before the chassis or other expensive parts. The FLM extended arms (bendable, reshape-able) are perfect for that role — they take the hit, get bent back close to spec, and the car keeps driving. The CF chassis and the rest of the drivetrain are protected by the arms acting as the sacrificial layer. See [`chassis_analysis.md`](chassis_analysis.md#notes) for how this informs the chassis durability expectation and [`bumper_analysis.md`](bumper_analysis.md#notes) for why the minimal-bumper choice is acceptable given this hierarchy.
- **Why aluminum arms aren't in this analysis**: arms see large bending loads on landings. Aluminum arms transfer those loads to the chassis mounts / bulkheads (same failure-cascade logic as the [shock tower analysis](shock_tower_analysis.md#material-properties-reference)), and even when they don't break they bend permanently and throw geometry off. Plastic arms — both OEM and EHD — are the right material for the role.
- **RPM arms (when added to the comparison)** — known for tougher-than-stock plastic, slightly heavier, multi-color options. Sit between OEM stiffness and EHD compliance.
- **Front-rear matching**: keep front and rear arms in the same family / generation if possible. Mixing stock-length OEM front with FLM extended rear changes geometry intentionally; mixing stiff fronts with flex rears unintentionally couples handling feel to terrain in ways that are hard to tune out.
- **CVD compatibility**: the chosen E-Revo CVDs are already chopped to fit the FastAzJato4x4. Changing arm length (FLM extended rear, for example) may re-affect CVD length — verify before finalizing.
- **Photos & TBD variants**: this analysis is partial. Fill in the two TBD rows once the user recalls them and we'll narrow to a final pick.
