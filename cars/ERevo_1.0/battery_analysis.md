# Battery Selection — E-Revo 1.0

> **Target: matched pairs of 3S LiHV 4200mAh shorty packs, run in series for 6S.** Running **4× Zeee Premo 3S HV 4200mAh** from the shared [battery fleet](../../batteries/README.md) — two in the car at a time, two on charge. The **SMC HV3 Flight 4290-3S1P** is the upgrade candidate: more watts per gram and honest published specs, but it's a *flight* pack that SMC themselves warn runs hot, and this fleet already has a bad SMC durability record.

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **3S, run as a series pair → 6S** | Must | The MAX8 G2S (3-8S) + Castle 1515 2200KV setup runs 6S as two 3S packs in series |
| **LiHV (11.4V nominal, 4.35V/cell)** | Must | The car is set up around HV — 25.2V nominal / 26.1V hot off the charger at 6S. Charger must have LiHV mode |
| **Bought as matched pairs, same order** | Must | Series pairs must stay voltage-matched; mismatched packs drift and one gets over-discharged |
| **~4200mAh class** | Must | Sets the run time this car is geared and tuned around |
| **LVC set to 3.4V/cell** | Must | Premo #2 died from over-discharge with no balancing — this is a hard rule now, not a preference |
| **Fits the Revo battery trays** | Must | Shorty form factor, verify L × W × H per pack |
| **Survives a raced, jumped 6S truck** | May | Durability has been the deciding factor here more often than peak output — see [Notes](#notes) |

---

> *Spec format: Cells · Capacity · C-rating · Weight · Connector · Size · Price*

## Pack comparison

| Pack | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **Zeee Premo 3S HV 4200mAh shorty (11.4V)** — *running, 4 in hand* | **Cells:** 3S / **11.4V LiHV**<br>**Capacity:** 4200mAh<br>**C-rating:** N/A (marketing)<br>**Weight:** 🚧 TBD, weigh a pack<br>**Connector:** 🚧 TBD<br>**Size:** shorty, 🚧 TBD<br>**Price:** **$23.30/pack** all-time low (2025-09-21), $23.70 more recently | Pro: **Cheapest by a wide margin** at ~$23/pack, and the fleet has **4 working units at 83 cycles each** — proven longevity in this exact car. Zeee replaced a dead pack free of charge (#2 → #5), so the warranty is real<br><br>Con: No published weight, true capacity, or real C rating — the numbers are marketing. **#2 died from sitting in storage** (self-discharge / degradation, not user error), so they don't tolerate long neglect. Weight and dimensions still unlogged | [`/Deals/batteries.md`](../../Deals/batteries.md#zeee-premo-3s-4200mah-shorty-lihv-114v) |
| 🥈 **SMC HV3 Flight 11.4V 3S 4200mAh 90C (4290-3S1P)** — *upgrade candidate, not bought* | **Cells:** 3S1P / **11.4V LiHV**<br>**Capacity:** **4200mAh @ 4.35V** — **3600mAh @ 4.20V** (both printed on the label)<br>**C-rating:** 90C (SMC true factory rate)<br>**Weight:** **277g** (554g for a series pair)<br>**Connector:** **SC5 (EC5/IC5 compatible)** at no upcharge; XT90 / XT60 / T-style / EC3 **+$1.50**, XT90 anti-spark +$2.00<br>**Size:** **140 × 44 × 23mm**, G10 top & bottom plates<br>**Energy:** 47.9Wh · 10AWG · 100% LCO<br>**Charge:** 1C-5C (higher rate = less mAh in and shorter life)<br>**Price:** **$31.95** + connector (~$33.45 with XT90) | Pro: **SMC publishes true-spec mAh and true factory C**, the honest exception to RC battery marketing. **Highest watts-per-gram on the market** per SMC. G10 end plates, 10AWG, and the label states both the 4.20V and 4.35V capacities instead of only the flattering one. **SC5 is EC5/IC5-compatible at no extra cost**<br><br>Con: **It's a flight pack, and SMC's own listing says the HV Flight series is hit-or-miss** — you must acknowledge a disclaimer to add it to the cart. **They run hot and must be temperature-monitored**, or cell life drops. **This fleet's SMC history is bad**: the [HCL-HP 5200s](../FastAzJato4x4/battery_analysis.md#notes) went DOA or died inside ~20 cycles while being babied. **~43% more per pack than the Premo** ($33.45 vs $23.30) | <img src="src/electronics_smc_hv3_flight_3s_4200_90c.jpg" width="500"><br><em>Label states 3600 @ 4.20V / 4200 @ 4.35V · 4290-3S1P · 47.9Wh</em> |

---

## Notes

- **The 4200 number is an HV number.** SMC prints both figures on the label: **4200mAh only at 4.35V/cell**, and **3600mAh if charged as a standard LiPo to 4.20V**. This car runs true LiHV, so it would get the 4200 — but the pack loses 14% of its capacity the moment it's charged conventionally. Most brands print only the bigger number.
- **Durability has decided every battery call in this fleet so far.** The Premos are at **83 cycles and still working**; the SMC HCL-HP packs in the [Jato analysis](../FastAzJato4x4/battery_analysis.md#notes) were the best-performing packs owned and **none passed ~20 cycles**, one arrived DOA. SMC's spec honesty is genuinely better than anyone else's, and their packs have still been the least durable thing here. That's the tension to weigh, not the spec sheet.
- **SMC calls the HV Flight series hit-or-miss themselves.** Between that, the mandatory cart disclaimer, and the "monitor temperature or you'll damage the cells" warning, this is a pack that asks for management. On a raced, jumped 6S truck that also sees beach days, that's a real ask.
- **Buy in pairs, always.** Anything bought here is **2× the per-pack price** ($63.90 + connectors for the SMC) because the car runs a series pair. Replace pairs together, from the same order.
- **LVC stays at 3.4V/cell** regardless of what goes in. Premo #2 was killed by over-discharge without balancing.
- **Still to log:** weight, dimensions, and connector for the Zeee Premo. Without its weight there's no way to check SMC's watts-per-gram claim against what's already in the car — and that claim is the main reason to consider the switch.
- **Connector note:** the MAX8 G2S is on **XT90**, so the SMC needs the +$1.50 XT90 option or an adapter. Its free SC5 option is EC5/IC5-compatible, which suits the Jato fleet's EC5 packs, not this car.
