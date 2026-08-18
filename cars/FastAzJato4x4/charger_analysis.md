# Charger Selection — FastAzJato4x4

> **Plenty on hand, all modern smart chargers that do LiHV** (needed for the [Gens Ace HV pack](battery_analysis.md)). For this build the go-to is a **DC charger fed by the HOTA H24 / P24 GaN power supply**; the **SKYRC B6ACneo** is the grab-and-go option since it has AC built in (no separate PSU). At 4S 5200-6300, charge at ~1C (5-6A), any of these handles that easily.

---

## Chargers on hand

> *Spec format: Chemistries · Cells · Power (DC / AC / PD) · Channels · Max current · Interfaces · Price*

| Charger | Spec | Notes |
|---|---|---|
| ⭐ **HOTA T6** | **DC 300W / PD 90W**, **dual channel**, 1-6S, LiHV<br>XT60 + USB-C in, 2.4" IPS | **Most capable, dual channel** so it charges two packs at once. Needs a DC/PD source (the H24/P24 below). Have two of these |
| 🟢 **SKYRC B6ACneo** | DC 200W / **AC 60W** / 10A, 1-6S, LiPo/LiFe/LiIon/**LiHV**/NiMH/NiCd/Pb | **Grab-and-go, AC built in** (no separate PSU). The convenient one for quick charges |
| 🟢 **SKYRC B6neo+** | DC 240W / PD 126W, 1-6S, LiHV | Higher-power B6neo; needs a DC/PD source |
| 🟢 **SkyRC B6neo** (Global Ltd) | DC 200W / PD 80W, 1-6S, LiHV | The original B6neo; DC/PD source needed |
| 🔵 **ToolkitRC M7** | DC 200W / 10A, 1-6S, LiHV<br>+ voltage/servo checker, ESC tester, RX test, LCD IPS | Solid charger **plus a pile of bench-test tools**. DC source needed |

---

## Power supply

| Unit | Spec | Notes |
|---|---|---|
| **HOTA H24 + P24** | **245W GaN** AC adapter / **P24 PD 248W** USB-C, 3-6S **XT60** + Type-C out | Powers the DC chargers (T6 / B6neo / M7) off the wall via XT60 or USB-C PD. This is what turns the DC-only chargers into a full setup |

---

## Charging accessories on hand

| Item | Use |
|---|---|
| **Parallel charging board** (XT90 / XT60 / EC5 / EC3 / XT30 / T, 6S) | Charge several packs in parallel off one channel |
| **USB-C PD trigger boards** (PD/QC decoy, 9/12/15/20V) | Pull fixed PD voltage from USB-C bricks to feed a DC charger |
| **Balance-lead adapters** (6S→3S, 4S→2×2S JST-XH) | Split/adapt balance plugs for the various packs |
| **4.0→5.0mm stepped bullet adapters** | Charge-lead bullet conversions |

---

## Notes

- **All of these do LiHV**, so the **Gens Ace 15.2V HV pack** charges fine, just select the LiHV/HV mode, not standard LiPo (LiHV tops at 4.35V/cell vs 4.2V).
- **Charge rate:** 1C is the safe default, ~5.2A for a 5200, ~6.3A for a 6300. Higher rates (the SMC packs allow up to 5C) put fewer mAh in and shorten cycle life, so stick near 1C for longevity. The 10A chargers (B6ACneo / M7) cover 1C on any of these packs.
- **DC vs AC:** most of these are **DC-only** and need the **H24/P24** (or any 12-24V supply / PD source). The **B6ACneo** is the only one with AC built in.
- **Match the charge lead** to the pack connector per [`connector_reference.md`](connector_reference.md); the parallel board covers most plug types.
