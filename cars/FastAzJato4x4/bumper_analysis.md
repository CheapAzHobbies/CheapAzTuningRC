# Bumper Selection — FastAzJato4x4

> **Front + rear: leaning toward OEM Traxxas 9044 Front + Rear Skid Plates set ($7 for both pieces).** Sold as a single front+rear set, same part the K939 build already uses. Minimal-profile and dirt-cheap. Counterintuitive logic: gives almost no real impact protection, but **if the nose or tail hits the ground hard enough to matter, the car is going to cartwheel anyway**. A minimal bumper means the chassis end doesn't dig in, gives a chance to **throttle up and recover from a bad landing** instead of pivoting end-over.
>
> **You can't skip the bumpers entirely.** **The Traxxas bumpers retain the hinge pins on this chassis family**, without a bumper, the hinge pins migrate out of their bores and the arms come loose. Skipping them isn't a weight-saving option, it's a mechanical failure. They barely save any weight anyway.
>
> **Tempting front alternative: Rustler 4x4 front bumper (Traxxas TRA5435)**, slightly larger, doesn't extend past the wheels (or close to it), so it's still recovery-friendly. The blocker is **it's ugly**. Possible solve: **design a custom front wing mount / cosmetic shroud that integrates the Rustler bumper** so it looks intentional rather than retrofitted.

<p align="center"><img src="src/bumpers_traxxas_skid_plates_tra9044.jpg" width="500"><br><em>Traxxas TRA9044 Front + Rear Skid Plates, $7 for the set</em></p>

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Bumper Options](#bumper-options) — OEM set, front alternatives, rear alternatives
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **No integrated front LEDs** | Must | Front bumper takes direct hits, LEDs in the bumper get destroyed immediately. Lights belong elsewhere, not in the impact zone |
| **Retains the hinge pins** | Must | **The Traxxas bumpers on this chassis family hold the front and rear hinge pins in their bores.** No bumper = pins migrate = arms come loose = car is dead. This is a hard mechanical requirement, not a crash-protection one |
| **Bolts to the CF chassis bumper mount holes** | Must | The chassis is Slash 4x4 pattern, bumpers must match those mount points |
| **Cheap** | Must | Bumpers double as skid plates on this build, they wear through use, not just crashes. Cheap = guilt-free replacement |
| **Doesn't put shocks in the crash path** | May | Already broke an HPI Vorza 97mm shock on a rear-end hit with the back-side-shock geometry, but tbh that crash was kind of a freak accident, not a routine failure mode. Worth avoiding if cheap to design around, but not a hard requirement |
| **Absorbs impact, doesn't transfer to chassis** | May | Nice for chassis longevity, but the extended FLM arms are the primary fuse, they bend before real chassis damage occurs. This is a "nice to have" not a hard requirement |
| **Survives most crashes intact** | May | Cheap to replace either way, but fewer trips to the workbench is nice |
| **Lightweight** | May | Bumpers sit low on the chassis (not the worst place for weight), and skipping them isn't viable for mechanical reasons anyway, small lever to optimize |
| **Looks intentional** | May | Cosmetics. Rustler front bumper crushes on protection but loses on looks, drives the custom-shroud idea |

---

## Bumper Options

### OEM set — front + rear together (the leading default)

> *Spec format: Type · Material · Position · Fits · Includes · Weight · Price*

| Part | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **TRA9044, Traxxas Front + Rear Skid Plates** | **Type:** Skid plates (pair)<br>**Material:** glass-filled nylon<br>**Position:** Front + rear<br>**Fits:** Jato 4x4 / Slash 4x4 family<br>**Includes:** N/A<br>**Weight:** N/A<br>**Price:** **$7.00** for the set | Pro: Sold as a single set with both pieces, same part the [K939 build](../K939/README.md) already uses. Minimal profile, light, cheap, holds the hinge pins. Default pick<br><br>Con: Minimal impact protection (intentional, per the recovery-focused logic above) | <a href="https://traxxas.com/products/parts/9044"><img src="src/bumpers_traxxas_skid_plates_tra9044.jpg" width="500"></a> |
| 🔵 **TRA6736 + TRA6737, Rustler 4x4 BL-2s Front + Rear Bumpers** | **Type:** Bumpers (pair)<br>**Material:** glass-filled nylon<br>**Position:** Front (6736) + rear (6737)<br>**Fits:** Rustler 4x4 BL-2s<br>**Includes:** N/A<br>**Weight:** N/A<br>**Price:** ~$5 (Jenny's RC, pulled from new) | Pro: Front+rear set, same as TRA9044 approach. Standard non-LED bumper. **Rustler bumpers are good at protecting the shocks, the front bumper perfectly guards the front shocks.** Pulled from new models at Jenny's RC for cheap<br><br>Con: **Not discontinued, in stock on AliExpress**, so limited availability isn't a worry. Rustler 4x4 BL-2s specific, verify mount compatibility with CF chassis | <img src="src/bumpers_traxxas_rustler_4x4_front_rear_6736_6737.jpg" width="500"> |

### Front bumper alternatives

| Part | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| 🔵 **TRA6736, Rustler 4×4 Front Bumper + Support** | **Type:** Front bumper + support<br>**Material:** glass-filled nylon<br>**Position:** Front<br>**Fits:** Rustler 4×4<br>**Includes:** front bumper + support<br>**Weight:** N/A<br>**Price:** **$6.00** | Pro: Cheap OEM front bumper with support included. Standard non-LED version. **Good at protecting the front shocks**<br><br>Con: Same profile as other stock bumpers, light frontal protection beyond shielding the shocks | <img src="src/bumpers_traxxas_rustler_4x4_front_6736.jpg" width="500"> |
| 🔵 **RPM 81042, Jato 4×4 / Rustler 4×4 Wide Front Bumper** | **Type:** Wide front bumper<br>**Material:** RPM reinforced composite (flexible, returns to shape)<br>**Position:** Front<br>**Fits:** **Stampede 4×4, Rustler 4×4, Telluride, Jato 4×4**<br>**Includes:** mount points for stock upper bumper<br>**Weight:** N/A<br>**Price:** **$9.95** | Pro: **Native Jato 4×4 fit**, drops straight in, no geometry question. Absorbs impact and returns to original shape. **Good at protecting the front shocks**, plus the front diff and chassis. Cheap. Incorporates mount points for stock upper bumper. Replaces stock #6735 & #6736<br><br>Con: Wide profile, may conflict with recovery-focused landing logic (same concern as TRA6835). Eliminates stock upper bumper support on Rustler 4×4 | <img src="src/bumpers_rpm_wide_front_81042.jpg" width="500"> |
| ❌ ~~**TRA5535, Traxxas original 2WD Jato front bumper**~~ | **Type:** Front bumper<br>**Material:** glass-filled nylon<br>**Position:** Front<br>**Fits:** 2WD Jato (NOT 4x4, holes don't line up)<br>**Includes:** N/A<br>**Weight:** N/A<br>**Price:** **$4.50** (back order) | Pro: Cheap<br><br>Con: Holes don't line up, needs drilling. **4x4-native equivalents exist** (TRA6736, TRA6797, RPM 81042); no reason to drill a 2WD part | <img src="src/bumpers_traxxas_2wd_jato_front_tra5535.jpg" width="500"> |
| ❌ ~~**RPM 80025, Slash 4×4 Front Bumper + Skid Plate**~~ | **Type:** Front bumper + skid plate (3-piece: skid mount + skid plate + bumper)<br>**Material:** RPM reinforced composite<br>**Position:** Front<br>**Fits:** Slash 4×4 (replaces #6835)<br>**Includes:** 3-piece: skid mount + skid plate + bumper<br>**Weight:** N/A<br>**Price:** **$15.95** | Pro: **Best aftermarket bumper**, simpler than OEM, eliminates support ring + 4 screws. Modular: remove bumper and run skid plate only (saves 27g) for racing, reinstall for bashing. Light canister compatible (RPM #80982/80983) for night running without LEDs in impact zone<br><br>Con: Same cartwheel issue as TRA6835, wide profile catches the ground on nose-first landings | <img src="src/bumpers_rpm_80025_slash_4x4_front.jpg" width="500"> |
| ❌ ~~**RPM 80022, Slash 4x4 Front Bumper + Skid Plate**~~ | **Type:** Front bumper + skid plate<br>**Material:** RPM reinforced composite<br>**Position:** Front<br>**Fits:** Slash 4x4 (LCG + non-LCG)<br>**Includes:** N/A<br>**Weight:** N/A<br>**Price:** ~$15-20 | Pro: RPM flexible composite, lots of protection, modular skid plate. Good for nudging stuck/rolled cars back over in pack racing<br><br>Con: Wide profile catches the ground on nose-first landings and triggers cartwheels, same reason as TRA6835 | <img src="src/bumpers_rpm_80022_slash_4x4_front.jpg" width="500"> |
| ❌ ~~**TRA6797, Rustler 4×4 Front Bumper w/LED Lights**~~ | **Type:** Front bumper w/ LEDs<br>**Material:** glass-filled nylon<br>**Position:** Front<br>**Fits:** Rustler 4×4<br>**Includes:** N/A<br>**Weight:** N/A<br>**Price:** **$14.95** | Pro: Night running visibility<br><br>Con: Requires TRA6588 power supply. **Front bumper takes direct hits, LEDs get destroyed immediately.** Fails the no-front-LED Must requirement | <img src="src/bumpers_traxxas_rustler_4x4_front_led_6797.jpg" width="500"> |
| ❌ ~~**TRA6736X, Rustler 4×4 Front LED Bumper + Support (replacement)**~~ | **Type:** Front LED bumper + support<br>**Material:** glass-filled nylon<br>**Position:** Front<br>**Fits:** Rustler 4×4 (fits 6795 LED Light Kit)<br>**Includes:** front LED bumper + support<br>**Weight:** N/A<br>**Price:** **$10.00** | Pro: Cheaper LED-housing option<br><br>Con: **Same problem as TRA6797, LEDs in the impact zone get destroyed immediately.** Fails the no-front-LED Must requirement | <img src="src/bumpers_traxxas_rustler_4x4_front_led_support_6736x.jpg" width="500"> |
| ❌ ~~TRA6835, Traxxas Slash 4x4 front bumper + mount~~ — *(for this build)* | **Type:** Front bumper + mount<br>**Material:** glass-filled nylon<br>**Position:** Front<br>**Fits:** Slash 4x4 chassis pattern<br>**Includes:** bumper + mount<br>**Weight:** N/A<br>**Price:** ~$8 | Pro: **Best impact protection of any OEM bumper here**, large profile actually absorbs hits and keeps the front end intact. **Useful in pack racing**, broad face is good for nudging a stuck or rolled car back over without having to stop. **Good for beginners**, newer drivers crash more, and the extra protection means more time driving and less time replacing broken parts<br><br>Con: Larger profile = **near-vertical-landing recovery is nearly impossible**, the bumper catches the ground and pivots the car end-over before you can throttle out. Wrong direction for this build's recovery-focused logic, but absolutely the right pick if your priorities are different | <img src="src/bumpers_traxxas_slash_4x4_front_tra6835.jpg" width="500"> |

### Rear bumper alternatives

The OEM TRA9044 set already covers the rear. These are options if you want to upgrade just the rear piece while keeping the TRA9044 front, or swap to a different rear style.

| Part | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ❌ ~~**Aluminum Rear Bumper Mount, Rustler 4×4 (6823/6737 compatible)**~~ | **Type:** Rear bumper mount<br>**Material:** Aluminum<br>**Position:** Rear<br>**Fits:** Rustler 4×4 (6823/6737 compatible)<br>**Includes:** N/A<br>**Weight:** N/A<br>**Price:** $7.99 + $9.00 shipping (~$17 total) | Pro: Stiffer than plastic, won't sand down<br><br>Con: Seller: crazyracer (eBay). **Unnecessary weight, and misses the point.** The front plastic bumper always wears first, ground contact sands it down faster than the rear. Since bumpers come as a front+rear pair, when the front wears out you buy a new set anyway and get a fresh rear for free. Upgrading just the rear to aluminum adds weight without solving anything. Would only make sense if the front bumper was sold individually | <img src="src/bumpers_crazyracer_alum_rear_mount_6737.jpg" width="500"> |
| ❌ ~~**TRA6737X, Rustler 4×4 Rear LED Bumper + Support (replacement)**~~ | **Type:** Rear LED bumper + support<br>**Material:** glass-filled nylon<br>**Position:** Rear<br>**Fits:** Rustler 4×4 (fits 6795 LED Light Kit)<br>**Includes:** rear LED bumper + support<br>**Weight:** N/A<br>**Price:** **$10.00** | Pro: Has a bottom skid plate component that could theoretically be used on its own<br><br>Con: Why spend money on this when Jato 4x4 front+rear bumpers come as a cheap pair, just buy the native set | <img src="src/bumpers_traxxas_rustler_4x4_rear_led_support_6737x.jpg" width="500"> |
| ❌ ~~**TRA6836, Traxxas Slash 4x4 rear bumper + mount**~~ | **Type:** Rear bumper + mount<br>**Material:** glass-filled nylon<br>**Position:** Rear<br>**Fits:** Slash 4x4 chassis pattern<br>**Includes:** bumper + mount<br>**Weight:** N/A<br>**Price:** ~$8 | Pro: Bigger / sturdier than TRA9044 rear piece<br><br>Con: Too large, interferes with wheel/wing mounts. **Could be trimmed down to just the small skid/bumper piece, but what's the point when you can just get the Jato 4x4 bumper anyway** | <img src="src/bumpers_traxxas_slash_4x4_rear_tra6836.jpg" width="500"> |
| ❌ ~~**RPM 80122, Slash 4x4 Rear Bumper**~~ | **Type:** Rear bumper<br>**Material:** RPM reinforced composite<br>**Position:** Rear<br>**Fits:** Slash 4x4 (LCG + non-LCG)<br>**Includes:** N/A<br>**Weight:** N/A<br>**Price:** ~$12-15 | Pro: RPM bulletproof composite<br><br>Con: Too large, interferes with wheel/wing mounts. Wrong platform on top of it. **Could be trimmed down to just the small skid/bumper piece, but what's the point when you can just get the Jato 4x4 bumper anyway** | <img src="src/bumpers_rpm_80122_slash_4x4_rear.jpg" width="500"> |

> **TRA9044 ships as a pair (front + rear) and is the cheapest path**, the alternatives are for specific upgrades, not replacements for the OEM set in the general case.

---

## Notes

- **Hinge-pin retention is the hard requirement.** The Traxxas Slash 4x4 / Jato 4x4 family of bumpers includes integrated retainers that hold the front and rear arm hinge pins in their bores. **Skipping the bumpers is not viable**, pins walk out, arms come loose, car dies. This is the Must that locks bumpers into the BOM regardless of any crash-protection argument.
- **Recovery-focused logic on the front bumper:** a Jato 4x4 hitting nose-first hard enough to need a bumper is already in a bad landing. The bumper's job here isn't to absorb the impact, it's to **not catch the ground and trigger a cartwheel** before you can power out of it. Smaller bumper = less ground contact = better chance to throttle through and save the run.
- **Why no premium / aftermarket bumpers:** the extended FLM arms bend before real chassis damage occurs, the chassis is not disposable, it's protected. Spending $40-60 on premium bumpers on top of that is upside-down value.
- **Minimal-bumper choice is a calculated risk:** the CF chassis is durable and the FLM extended arms are the intended fuse, they bend and reshape, absorbing hits before they reach the chassis. The chosen TRA9044 minimal-profile bumpers accept some chassis-hit risk in exchange for cartwheel recovery. Cheap bumpers matter because they're consumables, not because the chassis is expendable (see [`chassis_analysis.md`](chassis_analysis.md#notes) and [`arm_analysis.md`](arm_analysis.md)).
- **Custom front-bumper / wing-mount integration (TODO):** a custom front-end shroud / wing mount that integrates a front bumper would be worth a 3D print. Tracked in [3D Models](README.md#3d-models). Goal: keep better protection geometry while making it look like an intentional part of the car rather than a retrofit.
- **Photos:** TRA9044 set photo wired in (shared with the K939 build's same part).
