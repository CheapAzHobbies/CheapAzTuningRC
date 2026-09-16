# Chassis Selection — Jato4x4_Mike

> **Running: the Traxxas 7422 LCG plastic chassis, a Powerhobby aluminum front bulkhead and a steel VG Racing upper brace.** This is the biggest divergence from the [FastAzJato4x4](../FastAzJato4x4/chassis_analysis.md), which went carbon fiber, and it is the decision that everything else on this car follows from. Plastic **flexes rather than cracking**, it was already here so there is nothing to buy, and **the only two bought parts are the two that actually break**. **The honest cheap route.**
>
> **The chassis itself came off a running Slash 4x4.** Slash 4x4 and Jato 4x4 are the **same platform**, so the tub, bulkheads and brace all carry over. Only the **towers, shocks and wing** differ between the two.
>
> ⚠️ **This choice is why several of this car's docs cannot be shared with the FastAz.** The battery bars, tray and max pack size only exist because there is a moulded plastic tub, see [`battery_analysis.md`](battery_analysis.md).

<p align="center"><img src="../FastAzJato4x4/src/chassis_powerhobby_alu_front_bulkhead.jpg" width="500"><br><em>Powerhobby aluminum front bulkhead, the one bought part on an otherwise stock chassis</em></p>

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Survives the front bulkhead load** | Must | The front is where bulkheads get loaded and where the plastic one gives up |
| **Takes metal arms without stripping** | Must | FLM arms strip a *plastic* bulkhead, so if metal arms go on, the front has to be alloy |
| **Upper brace that does not snap** | Must | The OEM upper brace breaks often enough that replacing it is routine, not optional |
| **Costs as close to nothing as possible** | Must | This is the budget half of the pair. The whole point is not buying a carbon kit |
| **Keeps the stock battery tray** | May | The tray and hold-down posts are moulded in, and this car uses them (see [`battery_analysis.md`](battery_analysis.md)) |

---

## Comparison

> *Spec format: Material · CG · Fits · Includes · Weight · Price*

| Chassis | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **Traxxas 7422 LCG plastic chassis** — *running* | **Material:** composite nylon<br>**CG:** **LCG** (low centre of gravity)<br>**Fits:** Slash 4x4 / Jato 4x4 **LCG** pattern<br>**Includes:** battery tray + moulded hold-down posts<br>**Weight:** N/A 🚧 not weighed<br>**Price:** **$20.00** ([LEDGER](../../LEDGER.md) #80) | Pro: **$20 and plastic flexes instead of cracking.** This is the chassis the Jato 4x4 ships with anyway. Keeps the moulded battery tray and hold-down posts, which is what makes the [bar system](battery_analysis.md) work<br><br>Con: Flexes more than carbon, and the **front bulkhead area is the known failure point**, which is why the alloy bulkhead goes on. Heavier than a CF deck | <img src="../FastAzJato4x4/src/chassis_traxxas_oem_lcg_tra7422.jpg" width="500"> |
| ⭐ **VG Racing steel LCG chassis brace** — *running, replaces the OEM upper brace* | **Material:** **steel**, powder coated flat black<br>**CG:** sits high on the chassis<br>**Fits:** ⚠️ **LCG ONLY** (68086 Slash / Rally LCG). **Will not fit HCG**<br>**Includes:** brace only<br>**Weight:** N/A 🚧 not weighed<br>**Price:** **$18.99**, free shipping (eBay seller **vgracing**, item 396188510700) | Pro: **Replaces the other part that actually breaks.** The OEM upper brace fails often enough that swapping it is routine, and steel ends it. Sold specifically to stop a fatal chassis crack. Made in Los Angeles, 30 day returns<br><br>Con: ⚠️ **LCG only, so the HCG version of this car cannot use it.** Heavier than OEM plastic and it sits high, the worst place for CG. **MPN "Does Not Apply"**, so it is sourced by seller and listing, not a part number | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/chassis_vg_racing_steel_upper_brace.jpg` |
| ⭐ **Powerhobby aluminum front bulkhead** — *running* | **Material:** aluminum<br>**CG:** N/A<br>**Fits:** Jato 4x4 / Slash 4x4 front<br>**Includes:** bulkhead only<br>**Weight:** N/A 🚧 not weighed<br>**Price:** **~$36.99** standalone | Pro: **Covers the one part that actually breaks** without buying a chassis. On the FastAz this came bundled with the CF kit; here it is the standalone part. **It is what makes metal arms survivable** on a plastic chassis<br><br>Con: The only part on this car that had to be bought for the chassis. ~$36.99 is a real chunk of a budget build | <img src="../FastAzJato4x4/src/chassis_powerhobby_alu_front_bulkhead.jpg" width="500"> |
| 🚫 ~~**OEM plastic upper brace**~~ — *replaced* | **Material:** plastic<br>**CG:** stock<br>**Fits:** native<br>**Includes:** brace only<br>**Weight:** N/A<br>**Price:** $0, came on the car | Pro: Lighter than steel and free, being the part that was already fitted<br><br>Con: **Breaks often.** That is the whole reason it is off the car | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/chassis_oem_plastic_upper_brace.jpg` |
| 🚫 ~~**AliExpress CF LCG chassis**~~ — *the FastAz route, not taken* | **Material:** carbon fiber<br>**CG:** low (LCG)<br>**Fits:** Slash 4x4 pattern<br>**Includes:** aluminium battery holder + straps, front bulkhead<br>**Weight:** see [FastAz](../FastAzJato4x4/chassis_analysis.md#chassis-comparison)<br>**Price:** see [FastAz](../FastAzJato4x4/chassis_analysis.md#price-history) | Pro: Lower CG, stiffer, and its aluminium holder and straps **remove the battery height limit entirely**. Bundles the front bulkhead<br><br>Con: **Costs money this build is not spending**, and carbon cracks where plastic flexes. Loses the moulded tray, so none of this car's [bar geometry](battery_analysis.md) would apply | <img src="../FastAzJato4x4/src/chassis_aliexpress_cf_slash_4x4.png" width="500"> |

---

## Price History

| Date | Price | Discount Path | Notes |
|---|---|---|---|
| 🚧 date not recorded | **$18.99** | Free shipping | VG Racing steel LCG chassis brace, eBay seller **vgracing**, item 396188510700. ⚠️ LCG only |
| 2026-04-28 | **$36.99** | — | Powerhobby aluminum front bulkhead, see [FastAz](../FastAzJato4x4/chassis_analysis.md#bulkheads-front--rear) |
| 🚧 checkpoint 6/25 | **$20.00** | — | Traxxas 7422 LCG chassis, [LEDGER](../../LEDGER.md) #80. A 7477 LCG spur gear cover ($3.00, #79) went with it |

**Chassis side of the car: $75.98.**

---

## Notes

- ⚠️ **This car is LCG, and that constrains what fits.** The VG Racing brace is **LCG only and will not fit HCG**, and the [LCG bulkheads](../FastAzJato4x4/chassis_analysis.md#bulkheads-front--rear) are the same. Confirmed three ways: the **7422 LCG chassis** and the **7477 LCG spur cover** in the [LEDGER](../../LEDGER.md), and the brace fitting at all. **Check LCG vs HCG before ordering anything for this chassis.**
- **Plastic plus two steel/alloy parts is the honest cheap route.** The **front bulkhead** and the **upper brace** are the two things that actually break, so those are the two things bought. Everything else stays stock. Anyone pricing a Jato build should look at this before a carbon kit.
- **Start from a running Slash 4x4.** It is the same platform, so the chassis, bulkheads and brace all transfer. Only the **towers, shocks and wing** have to be bought to make it a Jato 4x4, which is the cheapest route onto this platform.
- **The upper brace is a known breaker, like the front bulkhead.** Both are replaced for the same reason. The difference is the brace sits high, so the steel version puts weight where CG likes it least. Worth weighing if a lighter alloy one turns up.
- **The bulkhead is not optional if metal arms go on.** FLM arms strip a plastic bulkhead, which is exactly why the alloy front matters here. See the [FastAz arm analysis](../FastAzJato4x4/arm_analysis.md).
- **This decision propagates.** The moulded tray and hold-down posts are chassis features, so the [battery bar geometry](battery_analysis.md) is unique to this car and does not transfer to the FastAz in either direction.
- **Nothing here is weighed yet.** Neither the stock chassis nor the bulkhead has a figure, so the weight case against carbon is currently reasoning rather than measurement.
