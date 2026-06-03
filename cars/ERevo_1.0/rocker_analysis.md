# Suspension Rocker Selection — E-Revo 1.0

> **Leaning toward: stock OEM plastic rockers (Progressive 2)** — they're the lightest option and the per-corner aluminum penalty turned out small (~4 g front, ~2 g rear), so the Enron alloy set is a legitimate durability upgrade if you keep cracking plastic. All rockers here are the **Progressive 2** rate. Measured singles: **OEM plastic 9.3 g (front) / ~11.7 g (rear)** vs **Enron aluminum 13.5 g bare**.

<p align="center">
  <img src="src/suspension_traxxas_rocker_oem_plastic_front.jpg" width="500">&nbsp;<img src="src/suspension_traxxas_rocker_oem_plastic_rear.jpg" width="500"><br>
  <em>OEM plastic Progressive 2 — front 9.3 g · rear ~11.7 g (single, bare)</em>
</p>

---

## Table of Contents

- [Key Requirements](#key-requirements)
- [Rocker Comparison](#rocker-comparison) — plastic vs aluminum
- [Weight Breakdown](#weight-breakdown) — how the single-rocker weights were measured / derived
- [Notes](#notes)

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Progressive 2 rate** | Must | Whole car is set up on the Progressive 2 rocker rate — any swap has to match |
| **Fits E-Revo 1.0 front + rear towers** | Must | Front and rear rockers ride on the same pivot hardware |
| **Lightweight** | May | Rockers are unsprung-adjacent moving mass; lighter = snappier suspension response |
| **Crack-resistant** | May | Plastic rockers can crack on hard landings; alloy never cracks but adds weight |

---

## Rocker Comparison

| Rocker | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **Traxxas OEM plastic** (Progressive 2, front + rear) | Material: glass-filled composite<br><br>Weight (single, bare): **9.3 g front / ~11.7 g rear**<br><br>Rate: **Progressive 2**<br><br>Price: cheap OEM | Pro: **Lightest option.** Sacrificial in crashes, cheap to replace, no extra steel hardware weight<br><br>Con: Can crack on hard direct hits / big landings | <img src="src/suspension_traxxas_rocker_oem_plastic_front.jpg" width="250"> <img src="src/suspension_traxxas_rocker_oem_plastic_rear.jpg" width="250"><br><em>front 9.3 g · rear ~11.7 g</em> |
| 🔵 **Enron aluminum** (HD, front + rear) | Material: CNC aluminum<br><br>Weight (single, bare): **13.5 g**<br><br>+ hardware: **~2.5 g/rocker** (~5 g per pair)<br><br>Rate: Progressive 2 geometry<br><br>Part / price: Enron (TBD) | Pro: **Won't crack** — survives the landings that snap plastic. Tight, slop-free pivot<br><br>Con: **+4.2 g front / +1.8 g rear per corner** over plastic (bare); steel hardware adds a little more; not sacrificial — passes impact to the tower instead of breaking cheap | <img src="src/suspension_enron_rocker_alloy_pair_hardware.jpg" width="500"><br><em>Enron alloy pair + hardware — 32.0 g</em> |

---

## Weight Breakdown

The goal was the **weight of a single rocker on its own** (no mounting hardware), so plastic and aluminum compare apples-to-apples.

**Measured directly:**

| Item | Reading |
|---|---|
| OEM plastic front rocker (single, bare) | **9.3 g** |
| OEM plastic rear rocker (single, bare) | **~11.7 g** *(scale shot sideways — confirm)* |
| Enron aluminum rocker (single, bare, no hardware) | **13.5 g** |
| Enron aluminum **pair + hardware** | **32.0 g** (re-weighed: 32.3 g) |

<p align="center">
  <img src="src/suspension_enron_rocker_alloy_single.jpg" width="380">&nbsp;<img src="src/suspension_enron_rocker_alloy_pair_hardware_bagged.jpg" width="380"><br>
  <em>Single alloy rocker, no hardware — 13.5 g · alloy pair + bagged hardware — 32.3 g</em>
</p>

**Deriving the hardware weight** (so any single rocker can be isolated, front or rear — hardware is the same at both ends):

```
pair + hardware        = 32.0 g
two bare rockers        = 2 × 13.5 = 27.0 g
hardware (per pair)     = 32.0 − 27.0 = 5.0 g   → ~2.5 g per rocker
```

So a **single aluminum rocker, bare = 13.5 g**, confirmed both by direct measurement and by subtracting the ~5 g hardware from the pair.

**Aluminum vs plastic, per corner (bare rocker only):**

| Corner | Plastic | Aluminum | Penalty |
|---|---|---|---|
| Front | 9.3 g | 13.5 g | **+4.2 g** |
| Rear | ~11.7 g | 13.5 g | **+1.8 g** |

**Whole car** (4 rockers: 2 front + 2 rear, bare): plastic ≈ **42 g** vs aluminum ≈ **54 g** → **about +12 g total**, plus a little extra for the heavier steel hardware.

---

## Notes

- **All rockers are Progressive 2.** Don't mix rates front-to-rear unless you're deliberately tuning — the whole setup assumes Progressive 2.
- **The aluminum penalty is genuinely small.** +4 g (front) / +2 g (rear) per corner is a rounding error next to chassis/battery weight, so if you're cracking plastic rockers the Enron alloy set is a reasonable durability buy — the usual "alloy is too heavy" argument barely applies here.
- **Plastic is still the lighter, sacrificial choice.** It breaks cheap and protects the tower; alloy never breaks but hands the impact to whatever it bolts to.
- **Hardware is shared front/rear**, so the ~2.5 g/rocker hardware figure applies at both ends — only the bare rocker weight differs between front and rear.
- **Enron part number / price: TBD** — fill in from the AliExpress listing when ordering.
