# Battery Selection — FastAzJato4x4

> **Target: any reputable 4S (14.8V) LiPo, 5000-5400mAh, ~5200 is the sweet spot.** On this light chassis, **6000mAh packs are too heavy** (hurt handling) and **4200mAh runs out too fast**, so 5000-5400 balances run time against weight. Running **Zeee 4S 5200mAh 100C (EC5) soft-case** packs, right in the window, pulled from the shared [battery fleet](../../batteries/README.md).

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **4S (14.8V)** | Must | The MAX10 G2 + 3665SD 2400KV combo is geared/tuned for 4S |
| **5000-5400mAh (~5200 sweet spot)** | Must | Enough run time without the weight penalty. 6000 is too heavy, 4200 is too short |
| **Fits the CF chassis tray** | Must | Verify pack dimensions against the CF chassis battery slot before buying |
| **Enough C-rating for the 140A ESC** | May | Any modern reputable pack (~50C+) handles the current fine at this capacity, not a limiting factor |
| **Connector matches the ESC** | May | Match the MAX10 G2 connector or adapt |

---

## Capacity comparison (why 5000-5400)

> *Spec format: Cells · Capacity · C-rating · Weight · Connector · Size · Price*

| Pack | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **Zeee 4S 5200mAh 100C (EC5), soft case** — *running* | **Cells:** 4S / 14.8V<br>**Capacity:** **5200mAh** (in the sweet spot)<br>**C-rating:** 100C (marketing, see note)<br>**Weight:** **518g**<br>**Connector:** **EC5**<br>**Size:** soft case, verify vs CF tray<br>**Price:** cheap 2-packs (Amazon) | Pro: **Right in the 5000-5400 window**, soft-case, EC5, cheap 2-packs. Running these<br><br>Con: The 100C is a marketing number (see C note), but it pushes plenty for the 140A ESC either way | <img src="src/electronics_zeee_4s_5200_100c.jpg" width="500"> |
| 🔵 **Zeee 4S 5200mAh 50C hardcase (Deans)** — *alt 5200, hardcase* | **Cells:** 4S / 14.8V<br>**Capacity:** 5200mAh (sweet spot)<br>**C-rating:** 50C (marketing)<br>**Weight:** **~480g** (hardcase)<br>**Connector:** Deans (T-plug)<br>**Size:** hardcase, verify vs CF tray<br>**Price:** ~$49.99 | Pro: In the 5200 sweet spot, and the **hardcase adds crash/impact protection**<br><br>Con: Heavier than the soft-case 100C EC5 running pack, lower 50C rating, Deans plug (adapt to EC5). Often sold out | <img src="src/electronics_zeee_4s_5200_50c_hardcase.jpg" width="500"> |
| 🔵 **HCL-HP 4S 5200mAh 150C hardcase (52150-4S1P, SMC)** — *best performance, but fragile* | **Cells:** 4S / 14.8V<br>**Capacity:** 5200mAh (true ±5%)<br>**C-rating:** 150C (SMC true rate; **Power Factor 390**)<br>**Weight:** **558g** (hardcase)<br>**Connector:** SC5 (EC5/IC5 compatible)<br>**Size:** 49 × 47 × 139mm hardcase<br>**Price:** **$49.95 each** (bought **3**, $149.85) | Pro: **Absolute best performance of the bunch**, low IR gives strong acceleration/speed and stays cooler. 100% LCO cells. In the 5200 sweet spot, and SMC actually publishes an honest Power Factor / true C (see note)<br><br>Con: **Not durable, you have to baby it.** Fails early even with a high cutoff, and it doesn't like impacts or being shaken hard. One arrived **DOA (a defect)**, and the rest **didn't make it past ~20 charge cycles**, frail within 6 months despite following SMC's care rules. Hardcase adds weight (558g) | <img src="src/electronics_hclhp_4s_5200_150c_hardcase.jpg" width="500"> |
| 🔵 **Gens Ace Redline 2.0 4S HV 15.2V 6300mAh 140C** — *HV competition pack, in hand* | **Cells:** 4S HV / **15.2V** (4.35V/cell)<br>**Capacity:** 6300mAh<br>**C-rating:** 140C<br>**Weight:** **452g** (light for a 6300 HV)<br>**Connector:** 5.0mm bullet<br>**Size:** hardcase, verify vs CF tray<br>**Price:** **$107.38** (paid; list ~$127.71) | Pro: **Higher top speed** (HV 15.2V = more motor RPM than 14.8V). **Very light for its capacity** (452g for a 6300 HV). Low-IR competition pack, made for 1/8 racing<br><br>Con: **Pricey (~$128).** Felt like **softer torque but higher top speed** (see note, it's the delivery character + HV, not weight). Needs an **HV charger** and an ESC that tolerates 15.2V (17.4V full charge) | <img src="src/electronics_gensace_redline_4s_hv_6300.jpg" width="500"> |
| 🔵 **4S 4200mAh** | **Cells:** 4S / 14.8V<br>**Capacity:** 4200mAh<br>**C-rating:** N/A<br>**Weight:** lighter<br>**Connector:** N/A<br>**Size:** smaller<br>**Price:** N/A | Pro: Lighter and more nimble<br><br>Con: **Run time too short** for a session, you're swapping packs constantly | <img src="https://placehold.co/500x300/eee/333?text=4S+4200" width="500"> |
| 🔵 **Zeee 4S 6000mAh 60C (Deans), soft case** — *too heavy for this chassis* | **Cells:** 4S / 14.8V<br>**Capacity:** 6000mAh<br>**C-rating:** 60C (marketing)<br>**Weight:** **573g**<br>**Connector:** Deans (T-plug)<br>**Size:** larger soft case<br>**Price:** ~$69.59 | Pro: Longest run time of the bunch<br><br>Con: **Too heavy**, the extra mass hurts handling on this light chassis. Deans plug (would need adapting to the EC5 setup) | <img src="src/electronics_zeee_4s_6000_60c.jpg" width="500"> |

---

## The C-rating math (a fun sanity check)

Max continuous current a C-rating *claims* = **C × capacity (Ah)**. Run the numbers and the claim collapses, the pack's own lead wire would melt long before it hit that current.

| Pack | C-rate | Claimed continuous (C × Ah) | Lead wire | Wire's realistic RC ceiling |
|---|---|---|---|---|
| Zeee 5200 50C hardcase | 50C | 50 × 5.2 = **260A** | ~10-12 AWG | ~60-150A |
| Zeee 6000 60C | 60C | 60 × 6.0 = **360A** | ~12 AWG | ~40-100A |
| Zeee 5200 **100C** soft | 100C | 100 × 5.2 = **520A** | ~12 AWG | ~40-100A |
| Gens Ace 6300 **140C** | 140C | 140 × 6.3 = **882A** | 5.0mm bullet leads | ~150A |
| SMC HCL-HP 5200 **150C** | 150C | 150 × 5.2 = **780A** | **10 AWG** (per SMC) | ~60-150A |

**The punchline:** a "100C" 5200 claims **520A continuous**, but its ~12AWG lead taps out around **40-100A** in RC use. The HCL-HP's 150C implies **780A through a 10AWG wire** that realistically carries maybe **60-150A**. That's **5-10× over** what the wire can pass, the lead would glow and melt at a fraction of the rated C, never mind the cells, tabs, or connectors. For context, a car's starter cable (huge, short) moves a few hundred amps; these little silicone leads are not doing 500-880A.

So the headline C number is physically impossible to sustain, it's a **marketing power scale**, useful only within one brand (see the note below). The honest exception is **SMC's Power Factor** (390 on the HCL-HP), a real metric instead of a fantasy amp figure, even though their own "150C" label implies that impossible 780A.

---

## Notes

- **Brand-agnostic.** Any reputable 4S pack in the 5000-5400mAh window works, this is a capacity/weight call, not a brand call. Which specific packs are owned lives in the shared [battery tracker](../../batteries/README.md).
- **C-ratings are mostly marketing, don't cross-shop them between brands.** The advertised C rarely survives the math (true C × capacity would be an absurd current the pack can't actually deliver), so a "100C" from one brand is not the same as "100C" from another. C is only useful as a **relative power scale within one brand**: a 100C Zeee vs a 50C Zeee tells you something; a 100C Zeee vs a 100C Tattu tells you nothing. Buy on **brand reputation + capacity**, and treat C as an in-brand relative number only. At this capacity any reputable pack pushes plenty for the 140A MAX10 G2 regardless. **One honest exception: SMC** publishes a real **Power Factor** (e.g. 390 on the HCL-HP) and rates true-spec mAh / true factory C, which is a far better cross-brand yardstick than the usual inflated C numbers.
- **Performance vs durability, pick your poison.** The **SMC HCL-HP** is the best-performing pack I've run but the **least durable**, fails early, hates impacts/vibration, one died before its first charge, and **none lasted past ~20 charge cycles** (one was a straight **DOA defect**), frail inside 6 months even babied per SMC's rules. One DOA is a genuine dud, that happens to any brand and isn't a knock (and **SMC replaced the DOA free under warranty**, good service there), but **the rest dying by ~20 cycles under different circumstances while following SMC's care rules is the pattern, a fundamental durability problem with the pack, not user handling**. The **Zeee 5200** gives up some peak punch but is the reliable daily pack. Also sold in a **3S variant (52150-3S1P, $37.95)** for 3S cars.
- **Check the fit.** Confirm the pack's length/width/height clears the CF chassis battery tray and strap before committing to a size.
- **Why the HV Gens Ace felt like less torque but more top speed (likely).** Two things, and neither is weight (at 452g it's actually **lighter** than the running Zeee 5200 soft at 518g). First, **HV (15.2V, 4.35V/cell) runs higher voltage than standard 14.8V**, and top speed scales with voltage (more motor RPM), so the top end climbs. Second, it's a **low-internal-resistance competition pack**, so it **sags less** than a cheaper pack. A pack that sags more gives a sharp voltage spike off the line that *feels* like a big torque hit, then droops; the Gens Ace holds voltage steady and delivers smoothly, so it **feels softer off the line while actually pulling harder up top**. So it trades that punchy initial hit for smoother, faster power, not a real loss of torque.
- **Weight reference (per pack):** Zeee 5200 100C soft **518g** · Zeee 5200 50C hardcase ~480g · Zeee 6000 60C 573g · SMC HCL-HP 5200 150C hardcase 558g · Gens Ace Redline 6300 HV 140C **452g**. Note the **Gens Ace is the lightest of the lot despite the most capacity + HV**, lighter than even the running Zeee 5200 soft (518g), that's the premium competition-pack difference. The cheap Zeee packs are heavy.
