# Servo Value Matching — Premium vs. Cheap Alternative

> **Generic reference — no single winner.** The goal isn't picking one best servo, it's finding a **cheap servo whose real torque/speed at the voltage you actually run matches a quality servo's**, so you're not paying brand premium for performance you're not using. **Not tied to any one car** (shared, like [`batteries/`](../batteries/) and [`controllers/`](../controllers/)).

---

## Table of Contents

- [Why match per voltage, not headline spec](#why-match-per-voltage-not-headline-spec) — the trap this doc avoids
- [Spec format](#spec-format) — standard field order, and how to record a torque curve
- [Comparison table](#comparison-table) — premium references and their budget matches
- [Notes](#notes)

---

## Why match per voltage, not headline spec

A servo's box usually prints **one** torque number, tested at whatever voltage makes it look best, usually the top of its range (2S LiPo, 8.4V, HV). That number alone doesn't tell you what the servo does at the voltage your actual setup feeds it.

Torque and speed both climb with voltage on the same servo. So a $80 quality servo's printed "25kg·cm" at 8.4V doesn't mean a $15 servo also claiming "25kg·cm" is equivalent, if the cheap one's number was measured at a different voltage, or if it can't sustain that torque at the voltage you're actually running (4.8V and 6V analog-style setups are common in cheaper receivers/BECs, not just 2S LiPo).

**The matching method here:**
1. Take the quality servo's torque and speed **at every voltage its spec sheet lists** (typically 4.8V, 6.0V, 7.4V, 8.4V).
2. Find a cheaper servo that clears the **same numbers at the same voltage** you'll actually run, not just at some higher voltage.
3. Check the stuff torque/speed matching doesn't cover: **BEC current draw**, **digital vs. analog signal frequency**, **dead band**, **gear material**, **case/weather sealing**. A torque-matched cheap servo can still be a bad swap if it needs more current than your BEC supplies, or is digital-only on an analog-only setup (see the [PTK 9752TG-D notes](../shop/products.json) for exactly this kind of gotcha: needs 333Hz, not 50Hz, and a minimum 8A BEC).

---

## Spec format

> *Every row's Spec cell uses this fixed order (registered in [`CLAUDE.md`](../CLAUDE.md) for all servo docs), `N/A` where unknown:* **Type · Torque · Speed · Voltage · Gears · Case · Motor · Bearing · Refresh · Pulse width · Dead band · Neutral · Travel · Signal · Programmable · Size · Weight · Price**

**Torque is a curve here, not one number.** List every voltage the spec sheet gives, low to high, on its own `<br>`-separated line inside the Torque field:

```
**Torque:** 15kg·cm@4.8V<br>18kg·cm@6.0V<br>22kg·cm@7.4V<br>25kg·cm@8.4V (peak)
```

Same idea for **Speed** if the sheet lists it per voltage too. If a servo only publishes one voltage's numbers, record just that one, don't invent the rest.

---

## Comparison table

No ⭐ winner. **🔵 Candidate** rows are premium reference points (the servo being matched against); **🥈 Runner-up** rows are the budget servo proposed as its match, with a qualifier noting which premium servo it's matched to. Add pairs as they're researched.

| Servo | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| 🔵 **Example Premium Co. XYZ-9000** — *premium reference, template row* | **Type:** N/A<br>**Torque:** 15kg·cm@4.8V<br>18kg·cm@6.0V<br>22kg·cm@7.4V<br>25kg·cm@8.4V (peak)<br>**Speed:** N/A<br>**Voltage:** N/A<br>**Gears:** N/A<br>**Case:** N/A<br>**Motor:** N/A<br>**Bearing:** N/A<br>**Refresh:** N/A<br>**Pulse width:** N/A<br>**Dead band:** N/A<br>**Neutral:** N/A<br>**Travel:** N/A<br>**Signal:** N/A<br>**Programmable:** N/A<br>**Size:** N/A<br>**Weight:** N/A<br>**Price:** N/A | Pro: TEMPLATE ROW — delete or edit once a real premium servo is researched<br><br>Con: N/A | <img src="https://placehold.co/500x300/eee/333?text=IMAGE+NEEDED" width="500"><br>🚧 save as `src/servo_brand_model.jpg` |

---

## Notes

- **Match at the voltage you'll actually run, not the servo's best-case voltage.** A cheap servo that only hits the premium servo's torque at 8.4V is not a match for a build feeding it 6V.
- **Torque/speed matching is necessary but not sufficient.** Always cross-check BEC current draw, signal frequency (analog 50Hz vs. digital, often 300Hz+), dead band, and gear/case material separately, a cheap servo can match the torque curve and still be the wrong swap.
- Specific servos get added as their own rows as they're researched. Delete the template row once the first real pair goes in.
