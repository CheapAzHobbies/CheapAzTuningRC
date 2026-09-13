# Service Interval Tracking

> **Goal: replace a wear part before it fails, not after.** Calendar time doesn't tell you much, since some cars run every weekend and some sit for a month, what actually wears a part out is **use**. This doc logs wear parts by usage count so a real "replace by N runs" number can be estimated instead of guessed. **Not tied to any one car** (shared, like [`batteries/`](../batteries/) and [`controllers/`](../controllers/)).

---

## Method

**Usage metric depends on what's tracked for that car:**

- **E-Revo 1.0 and FastAzJato4x4** — use **battery charge count** as the usage proxy. Both cars' packs have cycle counts logged in [`batteries/README.md`](../batteries/README.md), and each charge cycle is one run, so the battery tracker already does the counting.
- **Jato4x4 (Mike's)** — no battery cycle tracking exists for his car in this repo (his packs aren't in the shared tracker), so use **weekend run count** instead, logged manually here.

**Logging a new wear part:** record the install date and the usage count at install (0, unless it's a mid-life swap). Update the usage count after every run until the part fails or gets replaced again, at which point the usage-since-install number becomes a real data point for "replace by X" going forward, not a guess.

---

## Wear Item Tracking

| Car | Item | Installed | Usage Metric | Runs/Charges Since Install | Notes |
|---|---|---|---|---|---|
| Jato4x4 (Mike's) | Motor bearings (Castle Creations 1412 3200KV) | ~2026-09-06 (approximate, "last week") | Weekend runs (manual count) | **1** (first run 2026-09-12) | Replaced proactively, not after a failure, goal is to catch the next replacement before they blow rather than after. Log each future weekend run here to build toward a real interval estimate |

---

## Notes

- **No failure data yet for any item above** — the whole point of tracking from install is to get a real number the next time one wears out, instead of guessing at the interval again.
- **Mike's Jato run count is a manual log**, since there's no battery tracker for his packs. Update it here after each weekend he runs the car.
- **Cross-reference for E-Revo 1.0 and FastAzJato4x4:** their usage counts live in [`batteries/README.md`](../batteries/README.md) already (Zeee Premo / HOOVO pairs for the E-Revo, Gens Ace Redline pair for the FastAzJato4x4), pull the current cycle count from there rather than duplicating it here, add a row to the table above only when a specific wear part needs its own install-date baseline tracked against that count.
- As more wear items get tracked here (skid plates, bearings, gears, etc.), this becomes the place to look before assuming a part "should still be fine", check what it's actually seen.
