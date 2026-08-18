# Connectors Reference — FastAzJato4x4

Which battery/ESC connectors are worth running, and which to avoid. Not a tuning call, just a standing rule so the [mixed battery fleet](battery_analysis.md) all ends up on good plugs.

> **Stock on the build is EC5. The three good options are EC5, XT60, and XT90, run any of them.** **Avoid Deans (T-plug) and Tamiya.** Bullets (5mm / 3mm) are also fine if you want them, just not as common. Nothing else is worth bothering with.

---

| Connector | Rating (RC use) | Verdict | Notes |
|---|---|---|---|
| **EC5** | high (~120A), 5mm-bullet based | ⭐ **stock / chosen** | The build's connector. Solid, high current, self-insulating housing |
| **XT90** | high (~90A+) | 🟢 good | Big, great for the 140A ESC. **XT90-S** anti-spark version kills the plug-in spark on 4S |
| **XT60** | ~60A+ (plenty for a car) | 🟢 good | Compact. Fine here, it handles the bursty car current; anti-spark XT60E exists |
| **5mm / 3mm bullets** | high current | 🔵 fine (less common) | Fine if you prefer them, but **not as common** as EC5/XT. Bare pins, so insulate/heatshrink them yourself |
| ~~**Deans (T-plug)**~~ | — | ❌ **avoid** | **Burn up, corrode (black gunk), and melt.** Often go intermittent, doesn't conduct even when plugged in |
| ~~**Tamiya**~~ | — | ❌ **avoid** | High resistance, same failure mode as Deans, the worst of the lot |

---

## Notes

- **The three to use: EC5, XT60, XT90.** All good; pick by what your gear already wears. Nothing outside these (plus bullets) is worth it.
- **Deans / Tamiya are out** for good reason, they overheat, corrode, and fail intermittently under the current a 4S car pulls.
- **Adapters:** the [battery fleet](battery_analysis.md) is a mix (Zeee EC5 + Deans, SMC HCL SC5, Gens Ace 5mm bullet), so keep a few adapters on hand to get every pack onto the ESC's EC5, or re-terminate the good packs to EC5 / XT90.
