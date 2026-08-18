# Radio / Receiver Selection — FastAzJato4x4

> **Chosen: FlySky Noble NB4 transmitter + FlySky FGr4S V2 receiver, in hand.** A color-touchscreen surface radio with telemetry and model memory, paired with the FGr4S V2 RX. This is what's running the car, not a shortlist.

---

## Key Requirements

| Requirement | Type | Why |
|---|---|---|
| **Surface radio, wheel-style** | Must | It's an RC car; wheel + trigger ergonomics |
| **Pairs with the FGr4S V2 RX** | Must | The receiver on hand; the NB4 runs the FlySky FGr4-series RXs |
| **Telemetry** | May | Pack voltage / temp on the handset is handy at the track |
| **Model memory** | May | One handset across multiple cars |

---

## Comparison

> *Spec format: Type · Channels · Protocol · Receivers · Gyro · Telemetry · Model memory · Display · Battery · Price*

| Radio | Spec | Pros / Cons | Photo / Link |
|---|---|---|---|
| ⭐ **FlySky Noble NB4** (+ FGr4S V2 RX) — *in hand, running* | **Type:** Surface / wheel TX<br>**Channels:** 4<br>**Protocol:** FlySky 2.4GHz (Noble)<br>**Receivers:** **FGr4S V2** (also FGr4 / FGr4P)<br>**Gyro:** N/A (gyro-gain channel supported; no built-in gyro)<br>**Telemetry:** Yes<br>**Model memory:** Yes<br>**Display:** Color touchscreen<br>**Battery:** Built-in Li (verify cell)<br>**Price:** in hand | Pro: **Color-touchscreen, telemetry, model memory**, running the FGr4S V2 RX already on hand. Good handset for the money<br><br>Con: 4 channels (plenty for a car). Some exact specs (battery cell, RX outputs) to verify off the units | <img src="https://placehold.co/500x300/eee/333?text=FlySky+NB4" width="500"><br>🚧 save as `src/electronics_flysky_nb4_radio.jpg` |

---

## Notes

- **FGr4S V2 receiver:** the 4-channel FlySky RX paired to the NB4, on hand. Confirm the exact output types (servo / SBUS-style) against the unit when wiring.
- **Gyro:** the NB4 supports assigning a gyro-gain channel if a steering gyro gets added later, but there's no gyro built into the handset or the FGr4S RX.
- A few spec cells are left to **verify off the actual hardware** (handset battery, RX outputs) rather than guess.
