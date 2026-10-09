# Addressable Gaps — Aerodynamics-Led Ceiling Fan (AtomQuest 2026)

Built from the 28 research reports (`research/`), the checked cards (`cards-*.md`), [comparison.md](comparison.md), and the NotebookLM follow-up answers (marked **NB**).
The 28 room conditions boil down to **6 kinds of gap**. Each gap lists the conditions it covers, the evidence, and whether our team can realistically address it.

---

## G1. Measurement gap: no metric for what users actually feel  ★ strongest pitch angle
**What's missing:** The fan industry rates a fan by one number, measured at one point under ideal conditions:
- Service value (air delivery in m³/min ÷ power in W) is measured **only at maximum speed** in an open test chamber (**NB**: IS 374:2019 only covers max speed; we still need to read the clause text itself).
- Nobody publishes:
  - **low-speed** service value (R27)
  - **as-installed** air delivery under a false ceiling, as a hugger, or in a small room (R01, R02, R10)
  - **air speed where people sit or lie** (R03, R11)
  - **how evenly the air is spread** across a room (R25)
  - **how gusty/turbulent the air feels** at the bed (R22)

**Why it's ours:** It's cheap to measure (an anemometer grid and a power meter), and it reframes the whole problem: *"star ratings measure the wrong thing."*

**Deliverable:** A proposed "Real-Room Comfort Rating" — service value at speed 1 and 2, air speed at 1.1 m (seated) and 0.6 m (lying), a uniformity index, and turbulence intensity at bed height.

**Covers:** 27, 22, 01, 02, 03, 10, 11, 25

---

## G2. Low-speed blade aerodynamics  ★
**What's missing:**
- Indian fans run at low speed for many hours each night, but their blades are designed for maximum speed.
- At low RPM the blade's Reynolds number drops, so air separates from the blade surface earlier and lift falls.
- Sleep modes are only timers that step the speed down (R27).

**Evidence:**
- Low-speed blade patents claim the same airflow at **140 RPM** that a normal blade needs **270 RPM** for, and up to **~26%** more air at low speed. These are the patent holder's own claims, not independently tested (R27 §2).
- **NB:** US 6,039,541 was filed in the 1990s, so it is **likely expired**. Its twist schedule may be free to build on. Confirm the expiry on Google Patents.

**Open question:** We still need Atomberg's actual RPM at each speed step, to see whether speeds 1–2 actually fall in the 50–200 RPM band those patents target.

**Covers:** 27, 23 (fan-only part), 25 (quiet operation)

---

## G3. Fixed blade geometry vs. two operating regimes  ★ white space
**What's missing:**
- One fixed blade has to work at both low and high speed.
- **NB confirmed:** no fan product or patent in our sources changes blade pitch or twist **automatically** with RPM. The closest existing designs are:
  - US 8,721,305: manual pitch inserts
  - US 10,302,094: manually pivoting blade tips
  - US 6,116,856: blades reversible between two fixed positions

**Opportunity:**
- Make a **passive** RPM-dependent twist using centrifugal force or blade flexibility. The blade bends to a different twist as it speeds up, with no motor or actuator needed.
- This solves the conflict the reviewer flagged in the multi-condition concept: low-speed efficiency versus a flatter air outflow.

**Risks:** Imbalance and wobble (R28), fatigue, cost, and noise. A prototype has to prove all four are acceptable.

**Covers:** 27, 22, and the whole low-vs-high speed trade-off

---

## G4. Short-throw / impingement jet shaping  ★
**What's missing:**
- When a bed or table sits under the fan, the high-turbulence impingement zone moves up to where the person is.
- Every product responds by slowing down. None of them changes the **shape** of the air jet (R22).

**Evidence:**
- **NB:** The CBE study used a **1524 mm Big Ass Fans Haiku** at **70–175 RPM**, blade height ≈ **2.3 m**, in a 5.49 × 5.49 × 2.53 m chamber.
- It tested **desks and 1.4 m partitions, not beds**. Applying it to beds is our extrapolation.
- It did not use an Indian 1200 mm fan running at higher RPM.
- **This makes our own bed-scale test both novel and necessary.**

**Opportunity:** A wider, gentler outflow by design (blade tip loading, twist, hub shape) that lowers turbulence at 0.6 m (bed height) without lowering total air delivery.

**Covers:** 22, 10 (small rooms), 02 (low ceilings), 21 (blocked return path)

---

## G5. A fan that doesn't know its environment (sensing + RPM-aero control)
These are "smart" gaps, but the fix is still aerodynamic, because RPM controls the jet.

| Sub-gap | Evidence | Cond. |
|---|---|---|
| Cross-draft pushes the downwash sideways; the fan doesn't respond | No direct study. **NB:** Jayasree et al. 2022 found that opening a window cut uneven airflow from **76% to 39%** in larger bedrooms (abstract only). This is the **first ceiling-fan-specific data point** we have on this. | 19, 18, 14 |
| AC running at the same time: no automatic fan–AC coordination | CBE: the fan's downwash takes over the occupied zone. A US field study saved 36% of compressor energy with automated staging (R17). | 17 |
| Hot air pooled at the ceiling: no sensing of the ceiling-to-floor temperature difference | Only industrial HVLS fans do this (R13). | 13, 03, 15 |
| Installation unknown: false ceiling, hugger, corner, slope | Nothing self-calibrates for its installation (R01, R02, R04, R07). | 01, 02, 04, 07 |
| Wobble is only fixed by manual kits | Imbalance could be detected from motor current (R28). | 28 |

**Opportunity:** A fan that measures its room and installation when it's first installed, then adjusts. The BLDC controller already measures current and RPM, so some sensing comes free.

**Risks:**
- Detecting a cross-draft from motor current is unproven (R19, plus the reviewer's note).
- A cheap anemometer adds cost to every fan.

---

## G6. Installation geometry: asymmetry and inflow starvation
**What's missing:** No product, CFD study or measurement covers:
- fans mounted near a wall or in a corner, where wall-gap/D < 0.5 (R07: "the single largest literature gap")
- sloped ceilings, where the problem is uneven airflow, not just how the fan hangs (R04)
- a recessed cove cavity above the fan (R01)
- low ceilings with hugger fans (R02)
- beams in the inflow path (R05)
- a light kit blocking the hub (R06)

**Opportunity:**
- A hub or canopy shape that pulls in air better when clearance is short (hugger and cove installs).
- A clearance-vs-air-delivery curve, which nobody has published.

**Covers:** 01, 02, 04, 05, 06, 07, 09

---

## Out of scope for an aero pitch (mention only as add-ons)
| Gap | Why drop it |
|---|---|
| 26 Voltage/inverter | BLDC fans already solve it |
| 16 Humidity / 12 Balcony IP rating / 20 Dust | Materials or certification problems, not aerodynamics |
| 15 Hot roof | The heat is radiant; a blade can't fix that |
| 18 Exhaust fan | A room-pressure problem, and the effect is small |
| 24 Soft furnishings | Unmeasured, and the room isn't something we control |

---

## Our own test produces what nobody has published
Every top condition rests on **analogue data**, never a test of an Indian 1200 mm fan in a bedroom (comparison §7). So one cheap test rig produces several "first" datasets at once:
1. Service value and air-speed map at speeds 1–5, not just maximum (G1, G2)
2. Bed under the fan vs open floor: air speed and turbulence at 0.6 m (G4)
3. Box fan as a cross-draft, at 0.3–1.0 m/s: how far the downwash is pushed (G5)
4. Hugger vs standard downrod, plus a mock cove cavity (G6)

## Verify before the pitch
- [ ] The actual IS 374:2019 clause text: is low-speed testing really absent?
- [ ] US 6,039,541 expiry on Google Patents
- [ ] Atomberg's RPM at each speed step
- [ ] The full text of Jayasree et al. 2022
- [ ] A prior-art search for passive/centrifugal variable-twist fan blades, in any fan category
