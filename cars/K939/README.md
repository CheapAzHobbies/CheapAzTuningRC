# CheapAzTuningRC — Wltoys K939

> Build log, part list, setup notes, and battery tracker for my K939 twin-motor build.

---

## Table of Contents

- [Car Overview](#car-overview)
- [Track & Setup Philosophy](#track--setup-philosophy)
- [Suspension](#suspension)
- [Drivetrain](#drivetrain)
- [Electronics](#electronics)
- [Steering](#steering)
- [Aero & Body](#aero--body)
- [Bumpers](#bumpers)
- [Parts List & Costs](#parts-list--costs)
- [Battery Tracker](#battery-tracker)
- [3D Models](#3d-models)
- [TODO / Notes](#todo--notes)

---

## Car Overview

**Base Car:** Wltoys K939  
Twin motor, roughly equivalent to a Slash 4x4 HCG platform.

![Car Overview](cars/K939/src/car_overview.jpg)

---

## Track & Setup Philosophy

**Track:** Meldrum Bar Park  
Dusty hardpack with heavy ruts and rough bumps. No swaybars — the track rewards suspension compliance over roll stiffness.

---

## Suspension

### Shocks
**HPI Racing Big Bore Sport Shock Set (97mm) Apache C1**  
Part #: `107365` — 2pcs

![Shocks](cars/K939/src/shocks.jpg)

| Position | Spring | Notes |
|----------|--------|-------|
| Front | White (included with Apache C1) | Stock Apache C1 spring |
| Rear | Grey 52gf (Hot Bodies 67453) | 76mm, softer for bump compliance |

**Hot Bodies Grey Spring:** `Hot Bodies 67453 Big Bore Shock Spring 76mm 52gf Gray (2) Vorza D8S`

### Shock Oil
| Position | Weight |
|----------|--------|
| Front | 30wt |
| Rear | 30wt |

> Subject to change based on track conditions.

### Swaybars
None — removed for Meldrum Bar Park conditions.

![Suspension Layout](cars/K939/src/suspension.jpg)

---

## Drivetrain

- **Driveshafts:** Tekno
- **Drive Cups:** Tekno
- **Pinion:** TBD

![Drivetrain](cars/K939/src/drivetrain.jpg)

---

## Electronics

**Dual Motor Setup**

| Component | Part | Qty |
|-----------|------|-----|
| ESC | Castle Creations Copperhead 10 | 2 |
| Motor | 1412 3200kv | 2 |

![Electronics](cars/K939/src/electronics.jpg)

---

## Steering

- **Bell Crank Set:** Aluminum servo bell crank set (AliExpress, ~$10)
- **Pinion side:** TBD

![Steering](cars/K939/src/steering.jpg)

---

## Aero & Body

### Wing Mount
**STRC ST Racing Concepts 1/8 E-Buggy Conversion Kit for Traxxas Slash (Blue)**  
Part #: `SPTST6808B` — using wing mount only (received free)

### Rear Wing
White wing  
[AliExpress listing](https://www.aliexpress.us/item/3256807547003209.html)  
Cost: **$3.70**

![Wing](cars/K939/src/wing.jpg)

### Wheels
Yellow  
[AliExpress listing](https://www.aliexpress.us/item/3256808385588220.html)  
Cost: **$20.00**

![Wheels](cars/K939/src/wheels.jpg)

### Body
Pink & White  
[AliExpress listing](https://www.aliexpress.us/item/3256806297685912.html)  
Cost: **$25.00**

> 3D printed body mount not included yet.

![Body](cars/K939/src/body.jpg)

---

## Bumpers

| Part # | Description | Position | Cost | Source | Photo |
|--------|-------------|----------|------|--------|-------|
| TRA9044 | Traxxas Front & Rear Skid Plates | Front & Rear | $7.00 | Tammies | ![TRA9044](cars/K939/src/TRA9044.jpg) |

---

## Parts List & Costs

| Part | Part # | Cost | Source |
|------|--------|------|--------|
| Base Car — Wltoys K939 | — | — | — |
| Apache C1 Shocks (97mm) | HPI 107365 | — | — |
| Hot Bodies Grey Springs (52gf) | HB 67453 | — | — |
| Castle Creations Copperhead 10 ESC (x2) | — | — | — |
| 1412 3200kv Motor (x2) | — | — | — |
| Tekno Driveshafts | — | — | — |
| Tekno Drive Cups | — | — | — |
| STRC Wing Mount | SPTST6808B | $0.00 (free) | — |
| White Rear Wing | — | $3.70 | AliExpress |
| Yellow Wheels | — | $20.00 | AliExpress |
| Pink & White Body | — | $25.00 | AliExpress |
| Traxxas Front & Rear Skid Plates | TRA9044 | $7.00 | Tammies |
| Aluminum Servo Bell Crank | — | $10.00 | AliExpress |
| Pinion | TBD | — | — |
| **Total (known)** | | **$65.70** | |

---

## Battery Tracker

Track charge cycles per battery pack.

| Battery ID | Chemistry | Capacity | Charge Cycles | Notes |
|------------|-----------|----------|---------------|-------|
| Pack 1 | — | — | 0 | — |
| Pack 2 | — | — | 0 | — |

> See [`batteries/`](batteries/) folder for per-pack logs.

---

## 3D Models

> See [`3d-models/`](cars/K939/3d-models/) folder for all custom STL files.

| Model | Description | Status |
|-------|-------------|--------|
| Body Mount | Custom mount for AliExpress body | Pending |

---

## TODO / Notes

- [ ] Add pinion gear part number
- [ ] Add body mount 3D model
- [ ] Add photos for all sections
- [ ] Log battery specs and start tracking cycles
- [ ] Document shock oil changes if setup changes
