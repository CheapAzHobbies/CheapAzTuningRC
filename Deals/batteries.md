# Battery Deals

Price tracking for battery sales/coupons across all sources (eBay, AliExpress, Amazon, etc.). All I care about here is **cost** — the cheapest each pack has been seen, when, and what code got it there.

> Per-pack cycle history lives in [`/batteries/`](../batteries/). This file is just for buy-low timing.

**Rule of thumb:** typically **cheaper to buy on eBay** — wait for coupon codes (FAVEDEAL20, etc.) before pulling the trigger. AliExpress is sometimes competitive on sale days (Summer Sale, 11.11) but eBay's sitewide coupons stack on already-discounted seller listings, which is usually the lowest path for Zeee, CNHL, Ovonic, etc.

> **Heads up:** Zeee's eBay listings often say "LiPo" in the title, but if the voltage is **11.4V** (not 11.1V) it's the **HV** chemistry — same Premo pack as the AliExpress listing. 11.1V = standard LiPo, 11.4V = LiHV.

---

## Lowest Per-Pack Price by Model

At-a-glance: cheapest **per-pack** ever seen for each model I run / care about.

| Model | Chem | All-Time Low $/pack | When | Source |
|-------|------|---------------------|------|--------|
| Zeee Premo 3S 4200mAh Shorty (11.4V HV) | LiHV | **$23.30** | 2025-09-21 | AliExpress — ZEEE Direct Store |
| CNHL Racing Series 5200mAh 4S 90C (EC5) | LiPo | **$52.51** | 2026-08-26 | ChinaHobbyLine |
| Gens Ace Redline 2.0 6000mAh 4S HV 140C | LiHV | **$92.26** | 2026-08-31 | eBay — mugrc-store |
| CNHL Lightning LiHV 5500mAh 4S 120C (EC5) | LiHV | **$54.46** | 2026-08-26 | ChinaHobbyLine |
| CNHL Ultra-Thin Racing LiHV 6000mAh 4S 120C (EC5) | LiHV | **$71.00** | 2026-08-26 | ChinaHobbyLine |

---

## Deal History — by Battery Model

All recorded deals grouped by model, newest first within each group.

### Gens Ace Redline 2.0 6000mAh 4S HV 140C (hardcase, 5.0mm bullet)

Competition HV hardcase, part **GEA60004S14S**. Bought as a matched pair for the [FastAzJato4x4](../cars/FastAzJato4x4/battery_analysis.md).

| Date | Qty | Total | $/pack | Coupon | Source |
|------|-----|-------|--------|--------|--------|
| 2026-08-31 | 2 | **$184.51** | **$92.26** | none (list $230.64, seller discount) | eBay — mugrc-store |

- **$46 under list per pack** without a coupon, the seller's own price. Ships from the USA, 90-day warranty, delivered in 3 days.
- Cross-check against the older **6300** Redline at **$107.38/pack**: the 6000 is **$15 cheaper, 42g lighter**, and only 300mAh smaller.

---

### CNHL 4S packs (ChinaHobbyLine)

Bought as a set of three for the [FastAzJato4x4](../cars/FastAzJato4x4/battery_analysis.md) — one of each candidate, to settle by testing rather than by spec sheet. **`WELCOME` took ~2.75% off each line** (first-order code), and **shipping is free over $159**, which the three packs cleared on their own.

| Date | Pack | Qty | Paid | List | Coupon | Source |
|------|------|-----|------|------|--------|--------|
| 2026-08-26 | Racing Series 5200mAh 90C | 1 | **$52.51** | $53.99 | WELCOME | ChinaHobbyLine |
| 2026-08-26 | Lightning LiHV 5500mAh 120C | 1 | **$54.46** | $55.99 | WELCOME | ChinaHobbyLine |
| 2026-08-26 | Ultra-Thin Racing LiHV 6000mAh 120C | 1 | **$71.00** | $72.99 | WELCOME | ChinaHobbyLine |
| | **Order total** | **3** | **$177.97** | $182.97 | −$5.00 | Free shipping (over $159) |

- **`WELCOME`** — first-order discount, ~2.75% per line. Small, but it stacks on top of already-listed prices.
- **Free shipping over $159**, so a three-pack order pays its own freight; a single pack would not.
- **The store also runs "Buy 2, Get the 3rd Free" periodically** — not active on this order. Worth waiting for it on a repeat buy, since it beats WELCOME by a wide margin.
- The Ultra-Thin 6000 shipped as a **pre-order, ~7 days out**; the other two were in stock.

---

### Zeee Premo 3S 4200mAh Shorty (LiHV, 11.4V)

Same pack across eBay and AliExpress — Zeee sells it as "Premo" on AliExpress and the eBay listing title misleadingly says "LiPo" while the spec confirms 11.4V (HV chemistry).

| Date | Qty | Total | $/pack | Coupon | Source |
|------|-----|-------|--------|--------|--------|
| 2026-06-01 | **4** | **$94.78** | $23.70 | **20% off** ($118.48 list, $23.70 off) | eBay — zeee_store_us |
| 2025-09-21 | 2 | **$46.59** | **$23.30** | (TBD — listed $58.26, paid $46.59) | AliExpress — ZEEE Direct Store (Order 8204556163634866) |
