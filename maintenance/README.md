# Service Interval Tracking

> **Goal: replace a wear part before it fails, not after.** Calendar time doesn't tell you much, since some cars run every weekend and some sit for a month, what actually wears a part out is **use**. This doc logs wear parts by usage count so a real "replace by N runs" number can be estimated instead of guessed. **Not tied to any one car** (shared, like [`batteries/`](../batteries/) and [`controllers/`](../controllers/)).

---

## Method

**Usage metric depends on what's tracked for that car:**

- **E-Revo 1.0 and Jato 4SS** — use **battery charge count** as the usage proxy. Both cars' packs have cycle counts logged in [`batteries/README.md`](../batteries/README.md), and each charge cycle is one run, so the battery tracker already does the counting.
- **Jato4x4 (Mike's)** — his packs aren't in the shared tracker, so usage is counted as **battery packs run**, logged manually here. He is at **4 packs** on the current motor bearings.

**How an interval actually gets set.** One failure is an anecdote. The number only becomes usable after **3 to 5 failures of the same part**, at which point the charge counts at each failure give a range, and the replacement interval goes just under the low end of it. Until a part has that many data points, the entries here are raw history rather than a recommendation.

**Logging a new wear part:** record the install date and the usage count at install (0, unless it's a mid-life swap). Update the usage count after every run until the part fails or gets replaced again, at which point the usage-since-install number becomes a real data point for "replace by X" going forward, not a guess.

---

## Wear Item Tracking

| Car | Item | Installed | Usage Metric | Runs/Charges Since Install | Notes |
|---|---|---|---|---|---|
| Jato4x4 (Mike's) | Motor bearings (Castle Creations 1412 3200KV) | ~2026-09-06 (approximate, "last week") | Battery packs run (manual count) | **4** (first run 2026-09-12) | Running **S605ZZ 5×14×5 ABEC-9** rather than stock, since the stock ones work but burn up quickly. Replaced proactively, not after a failure. Log each further pack here to build toward a real interval estimate |

---

## Notes

- **Why motor bearings in particular.** The motor lasts effectively forever, the bearings do not, and **a bearing that lets go damages the rotor**, so a part worth a couple of dollars writes off a motor worth a hundred. That asymmetry is what makes counting runs worth the effort at all.
- **No failure data yet for any item above** — the whole point of tracking from install is to get a real number the next time one wears out, instead of guessing at the interval again.
- **Mike's Jato run count is a manual log**, since there's no battery tracker for his packs. Update it here after each weekend he runs the car.
- **Cross-reference for E-Revo 1.0 and Jato 4SS:** their usage counts live in [`batteries/README.md`](../batteries/README.md) already (Zeee Premo / HOOVO pairs for the E-Revo, Gens Ace Redline pair for the Jato 4SS), pull the current cycle count from there rather than duplicating it here, add a row to the table above only when a specific wear part needs its own install-date baseline tracked against that count.
- **Jato 4SS centre driveline bearing.** A plan to [sleeve the odd 10×16×5 down to a 10×15×4](../cars/Jato4SS/bearings_reference.md#the-centre-sleeve-16--15mm) was considered and reverted, too much risk at a position that's already taken one bearing to failure. Running the native 10×16×5, no sleeve.
- As more wear items get tracked here (skid plates, bearings, gears, etc.), this becomes the place to look before assuming a part "should still be fine", check what it's actually seen.
