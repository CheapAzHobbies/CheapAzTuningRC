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
| ⭐ **Zeee Premo 3S HV 4200mAh shorty (11.4V)** — *running, 4 in hand* | **Cells:** 3S1P / **11.4V LiHV**<br>**Capacity:** 4200mAh (claimed)<br>**C-rating:** 120C (marketing)<br>**Weight:** **231g** (±15g)<br>**Connector:** **XT60**<br>**Size:** **91 × 43.5 × 25mm** (±2mm), true shorty, soft case<br>**Energy:** 47.88Wh → **0.207 Wh/g**<br>**Price:** **$23.30/pack** all-time low (2025-09-21), $23.70 more recently; Amazon 2-pack $69.99 ($35/pack), **currently unavailable** | Pro: **Cheapest by a wide margin** at ~$23/pack, and the fleet has **4 working units at 83 cycles each** — proven longevity in this exact car. Zeee replaced a dead pack free of charge (#2 → #5), so the warranty is real<br><br>Con: **Capacity and C are marketing numbers** — Zeee publishes weight and dimensions, but nothing true-spec or factory-verified to check the 4200mAh / 120C against. **#2 died from sitting in storage** (self-discharge / degradation, not user error), so they don't tolerate long neglect. **Amazon listing is currently unavailable**, so restocks are the AliExpress/eBay route. One reviewer measured a Zeee pack at a fraction of its rated capacity, and Zeee publishes no true-spec number to check against | <img src="src/electronics_zeee_premo_3s_4200_120c.jpg" width="500"><br><em>91 × 43.5 × 25mm · 231g · 120C · XT60</em><br>[`/Deals/batteries.md`](../../Deals/batteries.md#zeee-premo-3s-4200mah-shorty-lihv-114v) |
| 🥈 **HOOVO 3S 4200mAh 120C 11.4V shorty (XT60)** — *lightest of the three, in the cart* | **Cells:** 3S1P / **11.4V**<br>**Capacity:** 4200mAh (claimed)<br>**C-rating:** 120C (marketing)<br>**Weight:** **214.4g**<br>**Connector:** **XT60**, soft case<br>**Size:** **93 × 43.8 × 25mm**, true shorty<br>**Energy:** 47.88Wh → **0.223 Wh/g**<br>**Price:** **$69.99 / 2-pack ($35.00/pack)**, in stock, Amazon (sold by Hoovo) | Pro: **Lightest pack here at 214.4g** — 17g under the Zeee, 63g under the SMC — and **best watts-per-gram of the three on published numbers**. Nearly identical footprint to the Zeee (93 vs 91mm long), so it drops into the same tray. **In stock**, unlike the Zeee, 30-day Amazon returns, 4.4★ over 95 ratings, and a reviewer measured **under 4mΩ/cell** internal resistance after two runs<br><br>Con: **The listing contradicts itself on HV** — it's sold as 11.4V High Voltage but the spec text says *"Cell voltage: 3.2~4.2V"* and *"never overcharge above 4.2V"*, which is standard-LiPo charging. **This car runs 4.35V/cell**, so that needs resolving before it goes in (see notes). **$35/pack vs the Zeee's $23.30** all-time low. Reviews are mixed on it actually delivering 4200mAh, and its "up to 300Wh/kg" claim doesn't survive its own numbers (47.88Wh ÷ 214.4g = **223 Wh/kg**) | <img src="src/electronics_hoovo_3s_4200_120c.jpg" width="500"><br><em>93 × 43.8 × 25mm · 214g · 47.88Wh · 120C · XT60</em> |
| 🥈 **SMC HV3 Flight 11.4V 3S 4200mAh 90C (4290-3S1P)** — *upgrade candidate, not bought* | **Cells:** 3S1P / **11.4V LiHV**<br>**Capacity:** **4200mAh @ 4.35V** — **3600mAh @ 4.20V** (both printed on the label)<br>**C-rating:** 90C (SMC true factory rate)<br>**Weight:** **277g** (554g for a series pair)<br>**Connector:** **any connector SMC offers** — SC5 (EC5/IC5 compatible) is the no-upcharge default, most others **+$1.50** (XT90, XT60, T-style, EC3), XT90 anti-spark +$2.00<br>**Size:** **140 × 44 × 23mm**, G10 top & bottom plates<br>**Energy:** 47.9Wh → **0.173 Wh/g** · 10AWG · 100% LCO<br>**Charge:** 1C-5C (higher rate = less mAh in and shorter life)<br>**Price:** **$31.95** + connector (~$33.45 with XT90) | Pro: **SMC publishes true-spec mAh and true factory C**, the honest exception to RC battery marketing. **Highest watts-per-gram on the market** per SMC. G10 end plates, 10AWG, and the label states both the 4.20V and 4.35V capacities instead of only the flattering one. **SC5 is EC5/IC5-compatible at no extra cost**<br><br>Con: **It's a flight pack, and SMC's own listing says the HV Flight series is hit-or-miss** — you must acknowledge a disclaimer to add it to the cart. **They run hot and must be temperature-monitored**, or cell life drops. **This fleet's SMC history is bad**: the [HCL-HP 5200s](../FastAzJato4x4/battery_analysis.md#notes) went DOA or died inside ~20 cycles while being babied. **~43% more per pack than the Premo** ($33.45 vs $23.30) | <img src="src/electronics_smc_hv3_flight_3s_4200_90c.jpg" width="500"><br><em>Label states 3600 @ 4.20V / 4200 @ 4.35V · 4290-3S1P · 47.9Wh</em> |

---

## Notes

- **The SMC is not a shorty, and that may end the discussion.** Zeee Premo = **91 × 43.5 × 25mm**; SMC HV3 = **140 × 44 × 23mm**. Same width, the SMC is 2mm thinner — but it is **49mm longer**, a 54% increase. This car carries **two packs**, so that's ~100mm of extra length to find. **Measure both Revo trays before considering the SMC at all**; on paper it looks like a full-length flight pack being compared against a shorty.
- **Watts-per-gram, all three (published numbers).** All are 11.4V / 4200mAh ≈ 47.9Wh, so weight decides it outright:

| Pack | Weight | Wh/g | Wh/kg | Size | $/pack |
|---|---|---|---|---|---|
| **HOOVO** | **214.4g** | **0.223** | 223 | 93 × 43.8 × 25 | $35.00 |
| Zeee Premo | 231g | 0.207 | 207 | 91 × 43.5 × 25 | $23.30 |
| SMC HV3 Flight | 277g | 0.173 | 173 | 140 × 44 × 23 | $33.45 |

  **The SMC finishes last on its own headline metric**, against a product page claiming the highest watts per gram on the market — it's 63g heavier than the HOOVO for the same energy, and it's the only one that isn't a shorty. **The honest caveat:** SMC's numbers are true-spec and verified, while HOOVO's and Zeee's are marketing — reviewers on both listings report packs falling short of the rating, and HOOVO's own "up to 300Wh/kg" claim is already 34% above what its published weight and Wh work out to. So it's a **verified 0.173 against two unverified higher numbers**. A capacity check on a Premo (four in hand, 83 cycles) would settle how much to trust that column.
- **The HOOVO's HV labeling needs resolving before it goes in this car.** It's sold as "11.4V High Voltage," but the same listing says *cell voltage 3.2~4.2V* and *never overcharge above 4.2V*. **11.4V nominal is HV (3.8V/cell), yet 4.2V/cell is standard-LiPo charging** — one of those is wrong. This car is built around **4.35V/cell** with LVC at 3.4V, so if the pack genuinely tops out at 4.2V it gives up the HV voltage the setup is tuned for and lands closer to a 3600mAh-equivalent, the same gap SMC prints openly on its label. Ask HOOVO which figure is real before committing.
- **On published numbers the Zeee wins watts-per-gram over the SMC.** The Zeee is 46g lighter per pack (92g over the series pair) for the same energy, so between the two packs this car has actually been offered, the cheaper one is also the lighter one.
- **The 4200 number is an HV number.** SMC prints both figures on the label: **4200mAh only at 4.35V/cell**, and **3600mAh if charged as a standard LiPo to 4.20V**. This car runs true LiHV, so it would get the 4200 — but the pack loses 14% of its capacity the moment it's charged conventionally. Most brands print only the bigger number.
- **Durability has decided every battery call in this fleet so far.** The Premos are at **83 cycles and still working**; the SMC HCL-HP packs in the [Jato analysis](../FastAzJato4x4/battery_analysis.md#notes) were the best-performing packs owned and **none passed ~20 cycles**, one arrived DOA. SMC's spec honesty is genuinely better than anyone else's, and their packs have still been the least durable thing here. That's the tension to weigh, not the spec sheet.
- **SMC calls the HV Flight series hit-or-miss themselves.** Between that, the mandatory cart disclaimer, and the "monitor temperature or you'll damage the cells" warning, this is a pack that asks for management. On a raced, jumped 6S truck that also sees beach days, that's a real ask.
- **Buy in pairs, always.** Anything bought here is **2× the per-pack price** ($63.90 + connectors for the SMC) because the car runs a series pair. Replace pairs together, from the same order.
- **LVC stays at 3.4V/cell** regardless of what goes in. Premo #2 was killed by over-discharge without balancing.
- **Still to log:** a measured capacity check on a Premo (published weight and dimensions are now logged). SMC's spec honesty is the real argument for switching, so the thing worth knowing is how far off Zeee's 4200 claim actually is on a pack with 83 cycles on it.
- **Connector note: SMC builds to whatever connector you ask for**, so plug type never constrains the choice with them — order it in **XT90** to match the MAX8 G2S directly (+$1.50). Worth noting the current Premos are **XT60** against an XT90 ESC, so this car is already running adapters. SC5 is the free default and is EC5/IC5-compatible, which suits the Jato fleet's EC5 packs rather than this one.
