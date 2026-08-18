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
| ⭐ **Zeee 4S 5200mAh 100C (EC5), soft case** — *running* | **Cells:** 4S / 14.8V<br>**Capacity:** **5200mAh** (in the sweet spot)<br>**C-rating:** 100C (marketing, see note)<br>**Weight:** medium<br>**Connector:** **EC5**<br>**Size:** soft case, verify vs CF tray<br>**Price:** cheap 2-packs (Amazon) | Pro: **Right in the 5000-5400 window**, soft-case, EC5, cheap 2-packs. Running these<br><br>Con: The 100C is a marketing number (see C note), but it pushes plenty for the 140A ESC either way | <img src="src/electronics_zeee_4s_5200_100c.jpg" width="500"> |
| 🔵 **HCL-HP 4S 5200mAh 150C hardcase (52150-4S1P, SMC)** — *best performance, but fragile* | **Cells:** 4S / 14.8V<br>**Capacity:** 5200mAh (true ±5%)<br>**C-rating:** 150C (SMC true rate; **Power Factor 390**)<br>**Weight:** **558g** (hardcase)<br>**Connector:** SC5 (EC5/IC5 compatible)<br>**Size:** 49 × 47 × 139mm hardcase<br>**Price:** **$49.95 each** | Pro: **Absolute best performance of the bunch**, low IR gives strong acceleration/speed and stays cooler. 100% LCO cells. In the 5200 sweet spot, and SMC actually publishes an honest Power Factor / true C (see note)<br><br>Con: **Not durable, you have to baby it.** Fails early even with a high cutoff, and it doesn't like impacts or being shaken hard. Had one **fail before its first charge**; the set went frail within **6 months** despite following SMC's care rules. Hardcase adds weight (558g) | <img src="src/electronics_hclhp_4s_5200_150c_hardcase.jpg" width="500"> |
| 🔵 **4S 4200mAh** | **Cells:** 4S / 14.8V<br>**Capacity:** 4200mAh<br>**C-rating:** N/A<br>**Weight:** lighter<br>**Connector:** N/A<br>**Size:** smaller<br>**Price:** N/A | Pro: Lighter and more nimble<br><br>Con: **Run time too short** for a session, you're swapping packs constantly | <img src="https://placehold.co/500x300/eee/333?text=4S+4200" width="500"> |
| 🔵 **4S 6000mAh** | **Cells:** 4S / 14.8V<br>**Capacity:** 6000mAh<br>**C-rating:** N/A<br>**Weight:** heavier<br>**Connector:** N/A<br>**Size:** larger<br>**Price:** N/A | Pro: Longest run time<br><br>Con: **Too heavy**, the extra mass hurts handling on this light chassis | <img src="https://placehold.co/500x300/eee/333?text=4S+6000" width="500"> |

---

## Notes

- **Brand-agnostic.** Any reputable 4S pack in the 5000-5400mAh window works, this is a capacity/weight call, not a brand call. Which specific packs are owned lives in the shared [battery tracker](../../batteries/README.md).
- **C-ratings are mostly marketing, don't cross-shop them between brands.** The advertised C rarely survives the math (true C × capacity would be an absurd current the pack can't actually deliver), so a "100C" from one brand is not the same as "100C" from another. C is only useful as a **relative power scale within one brand**: a 100C Zeee vs a 50C Zeee tells you something; a 100C Zeee vs a 100C Tattu tells you nothing. Buy on **brand reputation + capacity**, and treat C as an in-brand relative number only. At this capacity any reputable pack pushes plenty for the 140A MAX10 G2 regardless. **One honest exception: SMC** publishes a real **Power Factor** (e.g. 390 on the HCL-HP) and rates true-spec mAh / true factory C, which is a far better cross-brand yardstick than the usual inflated C numbers.
- **Performance vs durability, pick your poison.** The **SMC HCL-HP** is the best-performing pack I've run but the **least durable**, fails early, hates impacts/vibration, one died before its first charge, and the set went frail inside 6 months even babied per SMC's rules. The **Zeee 5200** gives up some peak punch but is the reliable daily pack. Also sold in a **3S variant (52150-3S1P, $37.95)** for 3S cars.
- **Check the fit.** Confirm the pack's length/width/height clears the CF chassis battery tray and strap before committing to a size.
