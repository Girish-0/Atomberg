# AtomQuest 2026 — Cross-Condition Comparison (28 Conditions)

Sources: `rubric.md`, `cards-01-07.md`, `cards-08-14.md`, `cards-15-21.md`, `cards-22-28.md`. TOTALs below are the orchestrator-verified figures (arithmetic and calibration-anchor corrected); do not recompute.

## 1. Executive Summary

Across 28 verified room/usage conditions, the strongest aerodynamics-led opportunities cluster around three physics problems that nobody in the Indian market has tooled a blade or control strategy for: (a) the fan's own downwash jet being short-circuited at the source — by furniture directly beneath it (22), by a slow-speed/low-Reynolds blade regime it was never optimized for (27), or by restricted hub inflow from mounting (01, 02, 05, 06); (b) the jet being deflected or starved by an asymmetric boundary — a nearby wall, wardrobe, slope, or long/narrow room shape (07, 04, 09, 21); and (c) the jet competing with an external flow — natural cross-ventilation, exhaust-fan negative pressure, a solar thermal plume, or a long throw into a stratified ceiling layer (19, 18, 14, 13, 03). Every one of the top-scoring conditions shares two traits: AERO_FIT of 4–5 (blade geometry or RPM/control strategy genuinely is the core lever, not materials or electronics) and EVIDENCE capped at 1–3 (the physics is borrowed from adjacent literature — HVAC diffusers, UAV ground effect, wind-turbine 1P loading, industrial destratification — never measured on an actual Indian ceiling fan in these exact geometries). That combination — real, plausible, high-frequency aerodynamic gaps with essentially zero primary evidence and thin/incomplete patent landscapes — is exactly the white space a hackathon team can occupy: cheap bench rigs (anemometer grids, smoke visualization, adjustable mock ceilings) can generate the first-ever quantified data for conditions that affect most Indian bedrooms and halls every night.

## 2. Full Matrix (sorted by TOTAL, tiered)

Scores within ±2 TOTAL points are effectively tied — treat tier boundaries as soft, not hard cutoffs.

### Tier 1 — Primary targets (TOTAL ≥ 30)

| NN | Condition | FREQ | SEV | UNSOLVED | PATENT_ROOM | AERO_FIT | EVIDENCE | PROTO | **TOTAL** |
|---|---|---|---|---|---|---|---|---|---|
| 25 | High occupancy (classrooms/halls) | 4 | 4 | 5 | 4 | 4 | 4 | 4 | **33** |
| 22 | Bed/table under fan (ground effect) | 4 | 4 | 4 | 3 | 5 | 3 | 4 | **32** |
| 27 | Low-speed / sleep operation | 4 | 4 | 5 | 2 | 5 | 3 | 4 | **32** |
| 19 | Cross-ventilation / natural wind | 4 | 3 | 5 | 4 | 4 | 3 | 5 | **32** |
| 01 | Recessed/false-ceiling mounting | 4 | 3 | 4 | 4 | 5 | 2 | 4 | **31** |
| 09 | Long, narrow rooms (AR>2) | 4 | 3 | 5 | 4 | 5 | 1 | 4 | **31** |
| 10 | Small rooms (bath/kitchen) | 5 | 3 | 4 | 4 | 4 | 2 | 5 | **31** |
| 02 | Low ceiling / hugger mount | 3 | 3 | 4 | 4 | 5 | 2 | 4 | **30** |
| 07 | Corner / near-wall mounting | 4 | 2 | 5 | 4 | 5 | 1 | 4 | **30** |
| 21 | Tall wardrobes along walls | 5 | 3 | 5 | 4 | 3 | 2 | 5 | **30** |

### Tier 2 — Secondary / cluster-support (TOTAL 24–29)

| NN | Condition | FREQ | SEV | UNSOLVED | PATENT_ROOM | AERO_FIT | EVIDENCE | PROTO | **TOTAL** |
|---|---|---|---|---|---|---|---|---|---|
| 03 | High / double-height ceilings | 3 | 4 | 4 | 2 | 5 | 2 | 4 | **29** |
| 08 | Multiple fans, one large room | 4 | 3 | 3 | 4 | 4 | 3 | 4 | **29** |
| 14 | Sunlit wall / window | 4 | 3 | 5 | 4 | 4 | 1 | 4 | **29** |
| 23 | Mosquito nets / canopies | 3 | 5 | 5 | 4 | 3 | 2 | 4 | **29** |
| 15 | Hot-roof top-floor rooms | 4 | 4 | 5 | 4 | 2 | 3 | 4 | **28** |
| 05 | Exposed beams / obstructions | 2 | 2 | 5 | 4 | 4 | 2 | 4 | **27** |
| 06 | Integrated light kit | 3 | 3 | 4 | 3 | 4 | 2 | 4 | **27** |
| 11 | Open-plan / L-shaped spaces | 3 | 3 | 4 | 4 | 4 | 2 | 3 | **27** |
| 04 | Sloped / vaulted ceilings | 2 | 2 | 4 | 4 | 5 | 1 | 3 | **26** |
| 12 | Semi-open (balconies/verandas) | 2 | 4 | 4 | 4 | 3 | 2 | 4 | **26** |
| 13 | Thermal stratification | 3 | 4 | 3 | 2 | 4 | 2 | 4 | **26** |
| 16 | Humidity-monsoon / coastal | 4 | 3 | 4 | 3 | 1 | 4 | 5 | **25** |
| 17 | Fan used with AC | 3 | 2 | 4 | 3 | 2 | 4 | 5 | **25** |
| 20 | Dust/smoke/grease fouling | 4 | 4 | 4 | 3 | 2 | 2 | 4 | **25** |
| 24 | Soft furnishings vs hard floors | 3 | 2 | 4 | 5 | 2 | 2 | 4 | **24** |

### Tier 3 — Drop candidates (TOTAL < 24)

| NN | Condition | FREQ | SEV | UNSOLVED | PATENT_ROOM | AERO_FIT | EVIDENCE | PROTO | **TOTAL** |
|---|---|---|---|---|---|---|---|---|---|
| 18 | Exhaust negative-pressure rooms | 4 | 2 | 4 | 5 | 1 | 2 | 4 | **23** |
| 28 | Wobble / vibration / imbalance | 4 | 2 | 5 | 3 | 1 | 2 | 4 | **22** |
| 26 | Voltage fluctuation / inverter | 3 | 2 | 4 | 3 | 1 | 2 | 5 | **21** |

## 3. Cluster Analysis (shared aerodynamic mechanism)

**Cluster A — Hub/inflow starvation (reduced clearance or hub-region blockage cuts the jet's source area):** 01 (recessed ceiling), 02 (hugger/low ceiling), 05 (exposed beams), 06 (light kit). Mechanism: blade-to-ceiling clearance falls below the CBE h/D≈0.2 starvation threshold, or the hub/light-ring exceeds the ~15%-of-D dead-zone blockage ratio (R06 §2, ResearchGate). Combined frequency is large — these four span false-ceiling cove apartments, budget hugger installs, older RCC-beam houses, and the fast-growing underlight segment (R06 §1). Combined evidence is uniformly weak (EVIDENCE 2 on all four): every report relies on a generic CBE clearance rule or hub-blockage-% analogy, never a ceiling-fan-specific CFD/experimental study of the exact geometry (R01 §7 gap; R02 §7 gap; R05 §7 gap; R06 §7 gap). Combined TOTAL: 31+30+27+27 = 115.

**Cluster B — Asymmetric boundary / off-axis mounting (1P cyclic loading, shortened recirculation on one side):** 04 (sloped ceiling), 07 (corner/near-wall), 09 (long narrow rooms), 21 (tall wardrobes). Mechanism: the fan's surroundings are closer or more obstructed on one azimuthal side than physics assumes — a tilted ceiling plane, a nearby wall, both end-walls of a corridor, or a floor-to-ceiling wardrobe blocking the wall-return path — producing asymmetric inflow/outflow and 1P cyclic blade loading (R04 §2 HAWT-yaw analogy; R07 §2; R09 §2; R21 §2.4 Gao et al.). Report 07 explicitly calls this "the single largest literature and market gap identified across all seven conditions" in its batch (R07 Core unsolved gap). Combined evidence is the weakest in the whole dataset (EVIDENCE 1 on three of four). Combined TOTAL: 26+30+31+30 = 117.

**Cluster C — External-flow / buoyancy competition with the fan's jet:** 19 (cross-ventilation), 18 (exhaust negative pressure), 14 (sunlit wall thermal plume), 13 (thermal stratification), 03 (high ceilings / long throw). Mechanism: the fan's downward momentum jet must compete with or is deflected by an external flow field — a natural door/window draft (jet-in-crossflow velocity ratio r = U_jet/U_crossflow, R19 §2), a depressurizing exhaust fan (short-circuit/jet deflection, R18 §2), a one-sided solar thermal plume (R14 §2), a buoyant ceiling-level hot layer (Richardson number framework, R13 §2), or simple jet decay over a long vertical throw (R03 §2). This is the broadest cluster by condition count and covers an enormous share of Indian housing (naturally ventilated homes, any kitchen/bath exhaust, any sun-facing room, any top-floor flat, any hall/duplex). AERO_FIT is strong for 19/14/03 (4–5) but weak for 18 (1, pressure-driven, not blade-aero) — 18 belongs here physically but is a poor aero-fix target on its own. Combined TOTAL: 32+23+29+26+29 = 139.

**Cluster D — Low-Reynolds / low-velocity regime:** 27 (low-speed sleep operation), 23 (mosquito nets). Mechanism: at low approach velocity — either because the blade itself is running at reduced RPM (chord Reynolds number falls toward ~10⁴, laminar separation, R27 §2) or because the flow must pass through a porous screen whose loss coefficient scales with velocity² (Darcy–Forchheimer regime, R23 §2) — standard full-speed blade design is aerodynamically mismatched to the actual operating condition. Both conditions occur nightly for a large share of Indian households (sleep mode near-universal, nets seasonal/regional). Combined TOTAL: 32+29 = 61, but very high AERO_FIT relevance (27 is AERO_FIT 5, the single best-evidenced "blade geometry IS the fix" case in the dataset via patented twist-schedule data).

**Cluster E — Furniture / floor-jet interaction:** 22 (bed/table under fan), 24 (soft furnishings vs hard floors), with partial overlap from 21 and 23. Mechanism: the downwash jet's impingement plane and spreading radius are altered by what sits on or near the floor — a bed/desk raises the impingement plane and increases turbulence intensity in the stagnation zone (CBE desk study, R22 §2); carpet/curtains change skin-friction and absorb floor-jet momentum differently than hard flooring (R24 §2). 22 is the single most universal condition card in the dataset (fan-over-bed is "arguably the single most common ceiling-fan use case in Indian homes," R22 §1) and scores the highest AERO_FIT (5) of any Tier-1 condition tied with 01/02/04/09/07/27. Combined TOTAL: 32+24 = 56.

**Cluster F — System-level / multi-fan coordination (not single-blade aero, but RPM/control strategy):** 08 (multi-fan halls), 09 (long rooms — also Cluster B), 11 (open-plan zoning), 25 (high-occupancy uniformity). Mechanism: single-fan solutions don't scale to room shape/occupant density; the lever is synchronized speed control and placement/spacing ratios (CBE fan-cell method, R08 §1) or uniformity-tuned blade twist to flatten under-fan vs between-fan speed ratios (R25 §9 Concept 1). Combined TOTAL: 29+31+27+33 = 120 — the highest combined score of any cluster, driven mainly by 25's 33.

**Non-cluster / largely non-aero (see §6, Drop list):** 15 (radiant, not convective), 16 (humidity/corrosion, materials), 17 (AC coordination, control not blade), 20 (dust/grease, coatings), 26 (voltage, electronics), 28 (wobble, mechanical balance), 12 (sealing/IP rating, materials).

## 4. Top 3 Targets

**Why Condition 25 (TOTAL 33, the single highest score in the dataset) is not one of the three targets below:** 25's score is inflated by breadth, not by being a cleaner single-blade aero fix than 22/27/19. Three reasons, each sourced to R25:
1. **Diluted AERO_FIT lever.** R25 ranks five levers for this condition (§4); only the #1 and #2 (low-noise low-speed blade design, uniformity-tuned airfoil) are blade-geometry levers, and both are mechanically identical to levers already claimed by Targets 2 (27) and 1 (22) — R25's own "Links to other conditions" ties 25 to 27 and 22 for exactly this reason (cards-22-28.md). Picking 25 as a separate Top-3 slot would mean re-selling the same twist/camber and flattened-profile levers under a noisier, harder-to-isolate problem statement (occupant thermal plumes, CO₂ mixing, speech-noise trade-offs — R25 §2–3) rather than adding a genuinely distinct aero mechanism.
2. **Heavier, costlier prototype.** R25's own validation plan (§10) calls for "30+ seated subjects or heated manikins/space heaters" plus a multi-point grid and tracer-gas CO₂ decay test — a materially bigger bench rig than the single-fan, single-bed/table/box-fan rigs specified for 22, 27, and 19 (R22 §10, R27 §10, R19 §10), even though PROTO is scored the same (4) across all four.
3. **Best-evidenced concept direction is non-aero.** R25 §9's five concept directions are led by multi-fan app synchronization and occupancy/CO₂-adaptive sensing — control/software features, not blade redesign — and the report's own "Top 5 insights" (§12) foreground the noise-vs-productivity trade-off and the unverified aerosol-trapping hypothesis as the highest-priority open items, not a blade-geometry fix.

Net: 25's raw TOTAL is highest because FREQ/SEV/UNSOLVED/EVIDENCE all score well on strong Indian classroom field-study data, but the condition's *aerodynamic* opportunity is already captured (partially, per §5) by the 09/25 footprint-uniformity lever inside the multi-condition concept below, rather than warranting its own standalone target. If the orchestrator's calibration anchors are applied strictly as a pure-TOTAL ranking, 25 would displace 19 for the third slot — the team should treat this as a close call (25 vs 19 are both plausible #3 picks) and revisit it once the uniformity-blade bench test (shared with 22) produces data.

### Target 1 — Condition 22: Bed/Table Directly Under the Fan (Ground/Surface Effect)

**The problem:** The fan's downwash jet, designed around an assumed ~2.1–2.7 m throw to the floor, instead impinges on a bed or table surface much closer to the blade plane, shifting the impingement/stagnation zone upward and raising turbulence intensity exactly where the occupant's head is.

**Key verified facts (with sources):**
- "Jet stays within blade-tip width until <0.6 m from the impingement surface; speed at 0.3 m above floor ≈ 50% of jet peak" (CBE study, R22 §2).
- "A table in the jet path deflects flow over its edges 'quite equally,' shifting the impingement plane up to desk height" (CBE study via ResearchGate, R22 §2).
- Ground-effect thrust change up to ~26% versus open space documented in UAV ducted-fan analogues at small clearances [UNVERIFIED for this specific application] (MDPI Drones, R22 §2).
- Big Ass Fans SenseMe uses temperature/humidity/PIR sensing to infer in-bed state and steps speed down (company blog, R22 §3) — but this is speed-only, not aerodynamic-profile adaptation.

**Why it is unsolved:** No product adapts blade geometry or jet shape to the surface-impingement condition; every existing "sleep mode" reduces speed alone, leaving turbulence-intensity-driven draft complaints unaddressed (R22 Core unsolved gap). AERO_FIT is the highest in the Tier-1 set (5): a flatter, wider exit-velocity profile is a geometry fix, not a sensing fix.

**Patents to design around [UNVERIFIED tags preserved]:** US20140322002A1 ("Sleepfan" — larger inlet area lowers flow speed [UNVERIFIED — not extracted]); US6415984 / US6189799 (automatic occupancy and temperature control [UNVERIFIED]); twisted-blade low-RPM patents [UNVERIFIED — patent number not independently confirmed]; Big Ass Fans "patented silent motor" [UNVERIFIED — claim text not retrieved].

**Measurable success metric:** Reduce peak turbulence intensity (or velocity variance) at bed/table height (0.3–0.6 m) by a target % versus a stock blade at matched mean air speed and power draw, measured with a hot-wire anemometer grid at 0.1 m resolution.

**Cheap prototype test:** Replicate the CBE desk-study method at bed/table scale — mount fan at Indian ceiling height, place bed/table directly beneath, grid-map air speed and turbulence intensity at 0.1 m intervals, smoke-visualize the impingement/wall-jet pattern, and A/B the stock blade against a flattened-twist candidate blade (R22 §10).

### Target 2 — Condition 27: Low-Speed Operation and Sleep/Night Comfort

**The problem:** Nearly all Indian households run fans at reduced speed (settings 1–2) at night, but blade geometry is optimized for a single mid-to-high-speed compromise angle, so at low RPM the blade enters a low-Reynolds-number regime where lift-to-drag collapses — and BEE/IS 374:2019 testing never measures this condition at all.

**Key verified facts (with sources):**
- "Ordinary ceiling-fan blade needs ~270 RPM to deliver same airflow that low-RPM-optimized blade delivers at ~140 RPM; measured improvements: ~10% airflow gain at high speed, up to ~26% gain at low speed" (US patent literature, R27 §2).
- "At low RPM (120 RPM), tip speed drops to ≈7.5 m/s and chord Reynolds number falls toward ~10⁴ or below... vs full speed (~300 RPM, chord Re order 10⁴–10⁵)" (R27 §2).
- BLDC motor cogging-torque noise reduction: stator-tooth shaping and magnet skewing reduced noise by 7.1 dB (IEEE study, R27 §3).
- "BEE/IS 374:2019 testing only mandates measurement at maximum speed — low-speed performance is not part of mandatory test" [UNVERIFIED — no low-speed test clause located] (R27 §1).

**Why it is unsolved:** No official metric exists for the speed setting users rely on most hours per day; all identified Indian "sleep modes" are timer-based speed step-downs, not aerodynamically differentiated blades (R27 Core unsolved gap). AERO_FIT = 5, the best-evidenced "blade geometry is literally the fix" case in the dataset, backed by quantified (if vendor-reported) patent-literature numbers.

**Patents to design around:** US6,039,541 + family (6,659,721, 7,210,910, 6,884,034, 7,396,212, 7,927,071) covering twist/camber/taper for 50–200 RPM band — High overlap risk; US9,103,346B1 (pulsed "natural breeze" control) — High overlap; US10,883,509 (smart sensor-driven control) — Medium overlap; US11,828,292 (increased-efficiency mode) — Medium overlap. PATENT_ROOM is the lowest in the Tier-1 set (2) — this is the most crowded target of the three.

**Measurable success metric:** % improvement in air delivery (CMM) per Watt at fixed low-RPM settings (speed 1–2) versus a stock blade at identical motor/RPM, replicating the ~10–26% gain claimed in patent literature but independently measured.

**Cheap prototype test:** Hot-wire anemometer grid at 0.1 m, 0.3–0.6 m (bed height), and 1.1 m (seated) heights on a 0.5D-spaced grid at speed settings 1–2; dB(A) with octave-band capability; true-RMS power meter; thermocouples for local draught-risk (DR) per ISO 7730 (R27 §10).

### Target 3 — Condition 19: Cross-Ventilation (Door–Window Drafts) and Natural Wind

**The problem:** When a ceiling fan runs under a natural cross-draft from open doors/windows (common in independent houses and hot-dry/composite-climate homes), the downwash jet is deflected horizontally by jet-in-crossflow (JICF) physics — a textbook engineering phenomenon never studied for residential ceiling fans specifically.

**Key verified facts (with sources):**
- "Cross-ventilation air speeds in Indian homes typically 0.19–0.83 m/s, some configurations reaching 1–2 m/s" (R19 §1).
- "Outdoor prevailing wind speeds at 10 m height for major Indian cities: Mumbai 3.6, Chennai 3.4, Kolkata 2.7, Bengaluru 2.8 m/s" (R19 §1).
- "CBE field measurements in 4 Californian buildings: ceiling fans produced mean air speeds 0.2–1.8 m/s downward vs 0.2–0.5 m/s updraft" (R19 §3).
- "Jet velocity ratio r = U_jet / U_crossflow governs deflection; where r ≈ 1 ... strong deflection/asymmetry should be expected" [UNVERIFIED — reasoned from non-fan JICF literature by analogy, not a measured fan result] (R19 §2).

**Why it is unsolved:** "A well-understood phenomenon in general engineering but never studied specifically for residential ceiling fans in Indian rooms — so no quantified coverage-loss or air-speed-at-occupant-height change exists in the literature" despite being an everyday condition (R19 Core unsolved gap). It also anchors the broadest mechanism cluster in the dataset (Cluster C, 5 conditions, combined TOTAL 139), making a fix here potentially reusable for 18/14/13/03.

**Defensibility caveat:** Every piece of physics evidence behind this pick is an analogue, not a direct ceiling-fan measurement — R19 itself flags this repeatedly: the closest experimental precedent (CBE's sidewall-jet-vs-fan chamber study) used a mechanical HVAC supply jet, not natural wind, and its numeric results were never retrieved in this research pass (R19 §2, §7, §12 open questions); the foundational jet-in-crossflow vortex-structure physics (Fric & Roshko 1994) was "referenced secondhand," not read in full text (R19 §7); and no India-specific or fan-specific test of the fan-plus-natural-draft interaction exists anywhere in the literature surveyed (R19 §7, §12). This is why EVIDENCE is capped at 3, not 5, and why the team should treat r≈1 and the resulting "strong deflection should be expected" claim as a testable hypothesis to validate with the §10 box-fan rig before committing engineering resources — not as a confirmed ceiling-fan finding. The choice is still defensible as a hackathon target (the physics is standard and the bench test is cheap), but it is weaker evidentially than Targets 1 and 2, which at least have one *direct* ceiling-fan-adjacent chamber measurement (R22's CBE desk study) or a patent-quantified blade comparison (R27).

**Patents to design around:** US8249731B2 (smart air ventilation with occupancy/sound sensing [UNVERIFIED]); US11353033 (ceiling fan with integrated sensing unit [UNVERIFIED]); US20050141997A1 (proximity safety + wind-speed sensor [UNVERIFIED]); CN103452879A ("natural wind" ceiling fan [UNVERIFIED]); US6415984B1 (occupancy/temperature control [UNVERIFIED]).

**Measurable success metric:** Restore occupant-height (≤0.6 m) downward velocity to within a target % of the no-draft baseline when a 0.3–2 m/s lateral cross-draft is introduced, via RPM boost or jet-column tightening, measured by anemometer grid + smoke visualization.

**Cheap prototype test:** Desk-fan-generated cross-draft + anemometer grid + smoke visualization (R19 §10) — a low-cost rig that reuses a simple box fan to simulate the 0.3–2 m/s crossflow and tests whether an ultrasonic/hot-wire-triggered RPM boost restores the velocity ratio r.

## 5. Multi-Condition Design Concept

**"Dual-Regime Adaptive Blade + Disturbance-Responsive BLDC Control"** — a single 1200 mm BLDC fan combining:

1. **Blade geometry:** a spanwise twist/camber schedule optimized for the low-RPM sleep regime (root twist ≈25–40° tapering to tip twist ≈5–11°, per the R27 patent-literature numbers) combined with a flattened/widened exit-velocity profile near the hub (per R22's surface-proximity concept) that trades peak core velocity for a broader, more uniform floor/furniture-height footprint.
2. **Hub/inlet:** an enlarged, low-profile inflow-area shroud that recovers delivery lost to restricted blade-to-ceiling clearance.
3. **Control:** motor phase-current-ripple sensing (reused from the wobble-detection literature, no added hardware) or a simple on-body anemometer that detects an abnormal thrust/RPM mismatch and briefly boosts RPM to restore jet velocity ratio against an external disturbance.

**Conditions covered, and how:**
- **27 (low-speed sleep)** — directly, via the low-RPM twist schedule (primary design target).
- **22 (bed/table under fan)** — directly, via the flattened exit profile reducing impingement turbulence at furniture height.
- **01, 02, 05, 06 (hub/inflow starvation cluster)** — via the enlarged inflow-area hub/shroud recovering clearance-constrained delivery.
- **19 (crossflow deflection)** — partially, via the disturbance-responsive RPM boost restoring jet velocity ratio r when a lateral disturbance is sensed.
- **09 (long rooms)** — partially, via the wider, more uniform floor footprint reducing under-fan-vs-away-from-fan speed inequity.

**18 is deliberately NOT listed as covered**, even partially, despite sharing Cluster C's external-flow mechanism with 19. Condition 18's own card and report score AERO_FIT = 1 and state the root cause is "pressure-driven short-circuit, not aerodynamic blade design" (R18 §2, §9) — the fix is a room/door ventilation-balance problem, not a jet the fan's own RPM can out-run. R18 §9 explicitly flags that its closest analogue to this concept's "disturbance-responsive RPM boost" (current-draw/RPM-droop load sensing) likely has too poor a signal-to-noise ratio to be workable ("current-draw changes from this cause are likely tiny compared to voltage-fluctuation noise... flag for bench validation," R18 §9). Treating 18 as "partially covered" here would contradict its own Drop-list justification in §6; the concept's RPM-boost lever is scoped to 19 (wind-driven crossflow, AERO_FIT 4) only.

**What it explicitly does NOT cover:**
- **14, 13 (sunlit wall / thermal stratification)** — no IR/thermal sensing is included; the control logic only reacts to velocity/current disturbance, not a buoyant thermal plume, so these need a separate ΔT-sensing feature.
- **04, 07 (sloped ceiling, near-wall mounting)** — these need an azimuth-asymmetric (not axisymmetric) blade pitch or a tilt/offset mounting kit; the concept's blade is still axisymmetric.
- **21, 24 (wardrobe wall-return blockage, soft furnishings)** — these are room-geometry/furnishing problems; the blade design doesn't change the wall-return path.
- **23 (mosquito nets)** — the report's own best-evidenced fix is a bypass auxiliary air mover inside the net, not a ceiling-fan blade change; standard RPM increase has diminishing returns against velocity²-scaling screen losses.
- **15, 16, 17, 20, 26, 28 (radiant heat, humidity/corrosion, AC coordination, dust/grease, voltage, wobble)** — all non-aero by AERO_FIT score; see §6.

### Engineering risks

The concept bundles two blade-geometry objectives and a sensing-driven control objective onto one physical blade; none of the three has been validated together, and at least two plausibly conflict:

- **Twist schedule vs. flattened exit profile may pull in opposite directions.** The low-RPM twist/camber schedule (R27 §4) exists to *recover* lift and air delivery that low-Re operation would otherwise lose — i.e., it pushes toward a higher, more concentrated exit velocity for a given RPM. The flattened/widened exit profile (R22 §9 Concept 1) deliberately *trades away* peak core velocity for uniformity to cut turbulence intensity at bed/furniture height. A single fixed-geometry blade cannot simultaneously maximize low-RPM lift recovery and minimize peak exit velocity — these are different points on the same twist/camber design space, not independent, additive features. Comparison.md's own §8 Open Questions already flags this exact tension ("does boosting RPM to counter a cross-draft undo the low-speed comfort/noise benefit... can both coexist on one blade") but §5 as written presents the combination as settled rather than as the open engineering question it is. Neither R22 nor R27 tested a blade that does both; this needs its own CFD/bench iteration before being presented as a single coherent concept, not two concepts glued together.
- **"Disturbance-responsive RPM boost" needs a sensor the concept hand-waves.** Point 3 proposes "motor phase-current-ripple sensing... or a simple on-body anemometer." These are not interchangeable: phase-current ripple is a wobble/imbalance-detection signal (R28's domain), not a validated proxy for lateral crossflow or thrust loss — no report in this dataset (including R19, R18) found or tested current-ripple as a crossflow sensor, and R18 §9 explicitly flags that a closely related current-draw-based load-sensing concept likely has too poor a signal-to-noise ratio against ordinary voltage fluctuation to be workable. The anemometer alternative is physically sound (R19 §11) but is added hardware the concept claims to avoid ("no added hardware") — the two options in point 3 are not equivalent fallbacks, they trade off cost against physical plausibility.
- **RPM boost vs. low-speed-sleep objective directly compete.** The primary design target (27) is to make low-RPM (≈100–200 RPM) operation good; the disturbance-response control (19) reacts to a crossflow by *raising* RPM. If a cross-draft is detected during sleep-mode operation, the control logic must choose between the quiet/low-speed comfort goal and the coverage-restoration goal — the concept does not specify an arbitration rule, and this is the same unresolved conflict already named in §8's Open Questions.
- **Enlarged hub/inlet shroud interacts with blade root geometry.** The hub/inlet lever (point 2, from the Cluster A clearance-starvation analogy) and the twist schedule's large root twist (≈25–40°, point 1) both modify the blade-root region; no source in this dataset analyzes whether an enlarged low-profile shroud is mechanically compatible with that root twist angle, or whether it reintroduces the hub-blockage dead zone Cluster A is meant to fix (R06 §2 hub-blockage-% analogy). Treat as unvalidated until a combined CAD/CFD pass is done.

None of this invalidates the concept as a hackathon starting point, but §5 should be read as a bundle of testable hypotheses competing for the same blade geometry and the same control budget, not a finished design — consistent with §8's own Open Questions, which this subsection makes explicit rather than leaving implicit.

## 6. Conditions to Drop

- **26 (Voltage fluctuation)** — AERO_FIT 1; fundamentally an electronics/motor-control problem already solved by any BLDC regulated-DC-bus design (R26 §9, §12).
- **28 (Wobble/vibration)** — AERO_FIT 1; root cause is blade-to-blade mass/pitch manufacturing mismatch and mechanical resonance, not aerodynamic design (R28 §1, §2).
- **15 (Hot-roof radiant load)** — AERO_FIT 2; dominant discomfort channel is radiant, and "fan airflow cannot fix mean radiant temperature" — a physics ceiling the report states explicitly (R15 justification).
- **16 (Humidity/corrosion)** — AERO_FIT 1; the aerodynamic effect of humid air is ~1% density change (negligible); the real issues are evaporative-cooling comfort and material corrosion (R16 justification).
- **17 (Fan + AC)** — AERO_FIT 2; already measurably addressed by speed-coordination control (36% compressor savings demonstrated in a field study, R17 §7); the lever is RPM/control scheduling, not blade redesign.
- **18 (Exhaust negative pressure)** — AERO_FIT 1; the mechanism is pressure-driven short-circuit flow, not blade aerodynamics (R18 §2, §9).
- **20 (Dust/grease fouling)** — AERO_FIT 2; leading-edge dust accumulation is a surface-roughness/coating problem, and two Indian brands already sell marketed "anti-dust" lines addressing it, even if unverified (R20 §6).
- **12 (Semi-open balconies/verandas)** — FREQ capped at 2 per rubric's niche-condition calibration anchor; AERO_FIT 3 with the primary lever being IP-rated sealing/materials (Hunter WeatherMax playbook), not blade geometry (R12 justification).

## 7. Evidence-Risk Register

Claims the Top-3 recommendation depends on that remain [UNVERIFIED], abstract-only, or analogue-based — verify before committing engineering resources:

- **Condition 22:** The CBE desk/partition study is a direct measurement but at office-desk scale, not bed/bedroom scale — "analogous ... but different room scale" (R22 §7). The UAV ducted-fan ground-effect thrust-change figure (~26%) is explicitly [UNVERIFIED for this specific application] (R22 §2). The "Sleepfan" patent's larger-inlet-area claim was never independently extracted from the patent text (R22 patents list).
- **Condition 27:** The 10–26% airflow-gain figures for low-RPM-optimized blades come from US patent literature (vendor-reported), with no independent replication found (R27 §2). The low-Re chord-Reynolds-number degradation is a standard aerodynamics extrapolation, not a ceiling-fan-specific measurement. EVIDENCE is capped at 3 for this reason.
- **Condition 19:** The CBE sidewall-jet study used in the report is an HVAC-diffuser analogue, not a direct ceiling-fan-plus-crossflow test; "JICF theory cited secondhand" (R19 §7). No India-specific test of fan-plus-natural-draft interaction exists.
- **Cluster-wide:** Every Tier-1 condition's EVIDENCE score is 1–3 (never 4–5) — no condition in this entire 28-card set has a primary, condition-specific, Indian-residential ceiling-fan CFD or chamber study. All mechanisms are physics-plausible extrapolations borrowed from adjacent domains: HVAC sidewall/wall-jet literature, UAV ground-effect studies, wind-turbine 1P cyclic-loading literature, industrial/warehouse destratification data, and generic porous-screen/insect-net discharge-coefficient studies.
- **Patents:** Nearly every patent number across all 28 cards carries an [UNVERIFIED assignee] or [UNVERIFIED legal status/relevance] tag, and multiple reports explicitly flag their own patent-landscape search as "incomplete" or "short of the 10–20 relevant-family target" (e.g., R01 §8, R05 §8, R09 §8, R19 §8, R27 §8). PATENT_ROOM scores should be treated as directional, not a cleared freedom-to-operate opinion.
- **Prevalence (FREQ):** No condition card cites a hard national statistic for its own frequency claim — every FREQ score is qualitative/anecdotal ("[UNVERIFIED]" appears in nearly every FREQ justification across the dataset, e.g. R22 §1, R27 §1, R19 §1).

## 8. Open Questions

- No Indian-residential, condition-specific CFD or chamber study exists for any of the three chosen targets (22, 27, 19) — should the team commission a baseline measurement pass before any blade-geometry redesign, given how much of each report's SEV/EVIDENCE score rests on borrowed-domain physics?
- Real prevalence data (what % of Indian homes have a bed/table directly under the fan; what % run sleep mode nightly; what % are meaningfully cross-ventilated) is [UNVERIFIED] everywhere — is there an existing BEE/census/market-research dataset the team can pull instead of assuming near-universality?
- Patent freedom-to-operate for the Target-2 (27) low-speed blade concept is the weakest in the Tier-1 set (PATENT_ROOM 2, multiple High-overlap-risk families) — does a real InPASS/Espacenet search change the viable design space before committing to a twist-schedule approach?
- Does the combined "Dual-Regime Adaptive Blade" concept's two control objectives (low-RPM sleep optimization vs. disturbance-responsive RPM boost for crossflow) conflict — i.e., would boosting RPM to counter a cross-draft undo the low-speed comfort/noise benefit the sleep-mode design is built around?
- Which single geometry change — the low-RPM twist schedule (27) or the flattened exit-velocity profile (22) — dominates the aerodynamic benefit, and can both coexist on one blade, or does the hackathon prototype need to pick one and treat the other as a stretch goal?

---

## Review log

Hostile-panel audit (aerodynamicist / Atomberg PM / hackathon judge / patent analyst), checked against `rubric.md`, `cards-*.md`, and the 28 `research/NN-*.md` reports.

1. **Arithmetic / cluster-sum check (§2, §3).** Recomputed all 28 TOTALs from their component scores and all six cluster sums (A–F). Every value already matched the orchestrator-verified target list and the stated cluster sums (115, 117, 139, 61, 56, 120) exactly — no arithmetic errors found. No change made.
2. **Card-score vs. matrix-score check.** Spot-checked conditions 18, 19, 22, 25, 27 against their cards in `cards-15-21.md` / `cards-22-28.md`: every per-dimension score (FREQ/SEV/UNSOLVED/PATENT_ROOM/AERO_FIT/EVIDENCE/PROTO) matches the matrix row exactly. No change made.
3. **§5 "Conditions covered" — Condition 18 contradiction (old → new).** Old: "19, 18 (crossflow/negative-pressure deflection) — partially, via the disturbance-responsive RPM boost..." sat alongside §6's Drop-list entry for 18 ("AERO_FIT 1; mechanism is pressure-driven short-circuit flow, not blade aerodynamics"). New: split into a 19-only "covered" bullet and an explicit paragraph stating 18 is NOT covered, citing R18 §2/§9 (AERO_FIT 1, and R18's own flagged concern that a current-draw-based sensing approach has poor signal-to-noise). Reason: the document cannot score 18 as a Drop condition (non-aero fix) in §6 while also claiming the aero-led concept in §5 partially solves it — that is the contradiction named in the task. Resolved in favor of the Drop-list verdict, since AERO_FIT=1 is independently justified by both the card and the report, and the only candidate sensing mechanism for the RPM-boost response was explicitly flagged by R18 itself as doubtful.
4. **§4 — missing justification for Condition 25 (TOTAL 33, highest in the dataset, not in Top 3).** Old: no mention of 25 anywhere in §4. New: added a sourced justification paragraph (diluted/shared AERO_FIT lever already claimed by 22/27 per R25's own cross-links; heavier 30-subject/manikin prototype rig vs. the single-fan rigs for 22/27/19 per R25 §10 vs. R22/R27/R19 §10; best-evidenced concept directions in R25 §9 are multi-fan sync and CO₂ sensing, not blade redesign) plus an explicit concession that 25 vs. 19 is a close call under a pure-TOTAL reading. Reason: task 2 required either a justification or a revised Top 3; the justification holds up against the source reports, so the Top 3 (22/27/19) is kept, with the close-call caveat made explicit rather than hidden.
5. **Target 3 (19) — overstated certainty on the r≈1 claim.** Old: "Jet velocity ratio r = U_jet/U_crossflow governs deflection; where r ≈ 1 ... strong deflection/asymmetry should be expected" presented as a plain "Key verified fact." New: appended "[UNVERIFIED — reasoned from non-fan JICF literature by analogy, not a measured fan result]." Reason: R19 §2 derives this by analogy from non-fan jet-in-crossflow literature and the report's own §7/§12 call the CBE analogue indirect and the India-specific fan+crossflow interaction untested; EVIDENCE is capped at 3, not 5, precisely because of this, so the inline claim should carry the same caveat the score already implies.
6. **Target 3 (19) — cross-ventilation defensibility (task 5).** Added a new "Defensibility caveat" paragraph after "Why it is unsolved," citing R19 §2/§7/§12: the CBE chamber study used a mechanical supply jet (not natural wind) and its numbers were never retrieved; Fric & Roshko (1994) was cited secondhand; no India-specific or fan-specific test exists. Reason: task 5 asked whether the all-analogue evidence base for 19 is defensible as a Top-3 pick — it is defensible as a cheap, high-value hackathon bet, but the write-up previously read more confidently than the underlying EVIDENCE=3 score warrants; the caveat makes the evidentiary gap explicit without demoting 19 from the Top 3.
7. **New "Engineering risks" subsection under §5 (task 4).** Added after the "does NOT cover" list. Covers: (a) the low-RPM twist schedule (R27 §4, recovers lift/air-delivery) and the flattened exit-velocity profile (R22 §9, trades away peak velocity for uniformity) pull in opposite directions on the same twist/camber design space and have never been combined or tested together; (b) "motor phase-current-ripple sensing... or a simple on-body anemometer" are non-equivalent fallbacks — current-ripple sensing for crossflow detection has no supporting source in this dataset and R18 §9 flags a closely related current-draw concept as likely too noisy, while the anemometer option re-adds the hardware the concept claims to avoid; (c) the RPM-boost-for-crossflow objective directly competes with the low-RPM-sleep-quiet objective with no arbitration rule specified; (d) the enlarged hub/inlet shroud (Cluster A lever) and the large root-twist angle (27's lever) both modify the blade root with no combined analysis found. Reason: task 4 asked whether the multi-condition concept is physically coherent and whether the disturbance-responsive control's sensor needs are addressed — they are not fully addressed as written, and this subsection makes the gaps explicit rather than letting §5 read as a finished design.

**Verdict — is the Top 3 robust?** Qualified yes. Targets 1 (22) and 2 (27) rest on the strongest evidence in the dataset (a direct, if differently-scaled, CBE chamber measurement for 22; a quantified, if vendor-reported, patent-literature comparison for 27) and survive scrutiny with only a sourcing-format note, not a substantive correction. Target 3 (19) is defensible as the best "white space + cheap bench test" pick but is evidentially the weakest of the three — entirely analogue-based — and is a closer call against Condition 25 than the original document acknowledged; both points are now flagged explicitly rather than left implicit. The one real internal contradiction found (Condition 18) is fixed. The multi-condition concept in §5 is a reasonable hackathon starting hypothesis but was previously presented as more settled than it is; the new Engineering risks subsection corrects that without requiring a change to which three conditions are targeted.

---
*File: /home/girish/Documents/Atomberg/synthesis/comparison.md*
