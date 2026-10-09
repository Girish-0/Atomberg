# AtomQuest 2026 – Ceiling Fan Aerodynamics: Research Prompts per Room Condition

## How to use
Each prompt has two parts:
1. **The common research framework (Part A).** It's identical for every condition.
2. **The condition brief (Part B).** It's different for each condition.

Paste **Part A + one Part B** into your deep-research model (Gemini Deep Research, ChatGPT Deep Research, Perplexity, etc.) as a single prompt. Run one condition per session so every report goes deep. Save each output as `research/<NN>-<condition>.pdf/md`. That builds the same staged evidence library the AMRX project used.

---

## PART A — Common research framework (paste this first, every time)

```
ROLE: You are a senior fluid-dynamics and product-engineering researcher who specialises in residential ceiling fans for the Indian market. You are preparing an evidence dossier for a hackathon team (Atomberg "AtomQuest 2026") designing a next-generation ceiling fan focused on aerodynamics.

CONTEXT: Indian homes: ceiling heights typically 2.6–3.2 m, fan sweeps 900–1400 mm (1200 mm most common), BLDC and induction motors, 230 V / 50 Hz mains with voltage fluctuation, inverter/solar backup, hot-humid and hot-dry climates. Relevant standards: IS 374:2019 (BIS) for ceiling fans, BEE star labelling (service value in m³/min/W), IEC 60879, ANSI/AMCA 230, ASHRAE 55 (thermal comfort / elevated air speed), ISO 7730.

ROOM CONDITION TO RESEARCH: <<see the condition brief below>>

PRODUCE A STRUCTURED REPORT WITH THESE SECTIONS:

1. Condition definition
   - Exact geometry/parameters that define this condition (dimensions, ratios, typical ranges in Indian homes).
   - How common is it in India (urban apartments, independent houses, rural, commercial)? Cite data if available.

2. Aerodynamic physics
   - What happens to the fan's inflow, the blade loading, the downwash jet, the floor spread, the wall return and the recirculation loop in this condition compared with an ideal centred fan in a square room.
   - The governing phenomena (e.g. inflow starvation, ground/wall effect, Coandă attachment, buoyancy vs momentum, crossflow jet deflection, tip-vortex interaction, swirl, turbulence intensity).
   - First-order equations or non-dimensional numbers (Reynolds number at the blade, Richardson/Archimedes number, jet spread rate, momentum theory / actuator disk thrust, clearance ratios such as h/D and wall-gap/D).
   - Quantified effects where literature has them: % drop in air delivery, change in velocity at occupant height (1.1 m seated, 0.3–0.6 m lying), coverage area, noise dB(A), power, wobble/vibration.

3. Role of speed / RPM / frequency
   - How rotational speed (RPM), tip speed and motor drive frequency (Hz, for BLDC/inverter control) change behaviour in this condition.
   - Is there an optimum speed band? Any resonance, beat-frequency, blade-pass-frequency noise or flicker issues?
   - Does variable speed, reverse rotation (updraft mode), pulsed or "natural breeze" modes help? Show evidence.

4. Blade and fan geometry levers
   - Which parameters matter most here: sweep diameter, number of blades, chord, twist distribution, pitch angle, airfoil section, camber, tip shape (winglets, rounded, serrated), hub size, downrod length and blade-to-ceiling clearance, canopy shape, motor-housing shape.
   - Rank the levers by expected impact for this condition.

5. Materials and manufacturing
   - Materials used for blades/hubs/housings (aluminium sheet, ABS, ASA, PP, glass-fibre-reinforced nylon, wood, composites, magnesium) and how weight, stiffness, surface finish, flutter, dust adhesion and moisture affect performance in this condition.
   - Manufacturing constraints (stamping, injection moulding, balancing, tolerances) and cost implications in INR.

6. Current market solutions (company-by-company table)
   Columns: Company | Model(s) | Sweep / blades / RPM | Air delivery (m³/min) | Power (W) | Service value | Feature that addresses this condition | How it works | Evidence (test data / claims) | What it still fails to solve.
   Cover at least: Atomberg, Crompton, Havells, Orient, Usha, Bajaj, Polycab, Luminous, Superfan/Versa Drive, Gorilla, Panasonic, plus global players (Big Ass Fans, Hunter, Minka-Aire, Modern Fan Co., Haiku, Dyson where relevant). Separate verified specs from marketing claims.

7. Academic and industry research
   - Key papers, theses, CFD and experimental studies (e.g. work on ceiling-fan airflow fields, IIT/IISc, CEPT, LBNL/CBE Berkeley, ASHRAE RP projects). For each: method, setup, main quantified finding, limitations.
   - Validated CFD approaches (MRF vs sliding mesh, turbulence model, mesh, boundary conditions) for simulating this condition.

8. Patent landscape
   Table: Patent no. | Assignee | Priority date | Jurisdiction | Legal status | Core mechanism | Independent-claim summary | Relevance to this condition | Overlap risk (H/M/L) | Design-around idea | Link.
   Search Google Patents, Espacenet, WIPO Patentscope and Indian Patent Office (InPASS). Aim for 10–20 relevant families. Flag any number you could not verify. This is research, not a legal opinion.

9. Unsolved gaps and opportunities
   - What no current product solves well for this condition, why (physics, cost, manufacturing, user behaviour, standards), and how big the gap is.
   - 3–5 concept directions an aerodynamics-focused team could pursue, each with: mechanism, expected benefit (quantified estimate), risks, cost impact, novelty vs patents.

10. Measurement and validation plan
   - How to test this condition cheaply in a real room or a scaled setup: instruments (hot-wire/hot-sphere anemometer, vane anemometer grid, smoke/fog visualisation, thermocouples, sound meter, power meter), grid points, and the metrics to report.
   - What a CFD study should model and what to compare it against.

11. Sensors and smart control (only if relevant)
   - Can the fan detect this condition (IMU wobble, current draw, temperature/humidity, ultrasonic distance, occupancy) and adapt automatically? Existing implementations?

12. Summary
   - A one-paragraph executive summary, a ranked list of the top 5 insights, and a list of open questions plus anything you could not find.

RULES:
- Cite every factual claim with a working link. Prefer primary sources (standards, datasheets, peer-reviewed papers, patents, BEE database) over blogs.
- Mark uncertain or unsourced items [UNVERIFIED]. Never invent numbers, patents or papers.
- Use SI units. Use tables wherever comparison is involved.
- Keep marketing claims separate from tested data.
```

---

## PART B — Condition briefs (pick one and append it after Part A)

### Group 1 — Ceiling architecture

**01. Recessed / cove false ceiling (POP, gypsum)**
```
CONDITION: The fan is mounted inside or just below a recessed cove or tray false ceiling, so a cavity sits above the blades. Research inflow starvation into the blade upper surface, the effect of cavity depth and diameter relative to fan sweep, re-circulating eddies trapped in the cavity, short downrods, noise amplification from the cavity, and heat build-up from cove LED lighting. Include how false-ceiling installers choose downrod length today and any manufacturer guidance on minimum blade-to-ceiling clearance.
```

**02. Low ceilings (< 2.6 m) and hugger / flush-mount fans**
```
CONDITION: A low ceiling (2.4–2.6 m, common in apartments, lofts and top-floor rooms) forces hugger or short-downrod mounting with a blade-to-ceiling gap under 200 mm. Research the clearance-ratio effect on air delivery, the safety clearance from blades to the floor (IS/IEC requirements), how hugger fans redesign inlet geometry, and the trade-off between safety height and airflow.
```

**03. High and double-height ceilings (> 3.5 m)**
```
CONDITION: High ceilings (3.5–6 m: duplexes, old bungalows, halls, temples, schools). Research jet decay over long throw distances, the effect of downrod extension, thermal stratification destroying the downward jet, the need for higher thrust per watt, and whether long downrods cause wobble and resonance.
```

**04. Sloped / vaulted / pitched ceilings**
```
CONDITION: The fan is mounted on a sloped ceiling (10°–45°, attics, top-floor sloped slabs, Kerala/hill-style roofs). Research asymmetric inflow (one side choked, the other open), uneven blade loading per revolution (cyclic loads, 1P/2P vibration), tilting and deflection of the air cone, wobble, angled-mount kits, and minimum slope limits from manufacturers.
```

**05. Exposed beams and ceiling obstructions**
```
CONDITION: Exposed concrete or wooden beams, ducts, or a chandelier/lighting close to the fan's inflow region. Research how obstructions break up the return-air loop into eddies, the effect of beam depth and distance from the blade tip, periodic blade-obstruction interaction noise (blade-pass tones), and recommended clearances.
```

**06. Fan with integrated light kit or chandelier**
```
CONDITION: A light kit or decorative chandelier mounted under the hub, or fan-chandelier hybrids. Research the hub-blockage effect on the downwash core, the heat added by lighting, flicker/strobing from blade shadows at certain RPMs (stroboscopic effect), and how decorative fan makers trade off aesthetics against airflow.
```

### Group 2 — Placement in the room

**07. Corner / off-centre / near-wall mounting**
```
CONDITION: The fan is mounted off-centre, near one or two walls (wall-gap less than 0.5×D), often because of the bed position, beams or electrical points. Research the asymmetric wall effect, pressure imbalance, buffeting, extra noise, tilting of the air cone, Coandă attachment to the wall, the minimum recommended wall clearance, and whether asymmetric or directional blade designs could compensate.
```

**08. Multiple fans in one large room or hall**
```
CONDITION: Two or more ceiling fans in a large hall, living-dining room, classroom or office. Research how adjacent recirculation cells interact (merging vs competing), turbulent shear zones between fans, optimal spacing (multiples of D), same- vs opposite-rotation directions, synchronised speed control, and multi-fan layout guidelines from ASHRAE/CBE and HVLS makers.
```

**09. Long, narrow rooms and corridors**
```
CONDITION: A high aspect-ratio room (length/width > 2, e.g. 3 m × 8 m). Research early wall impingement on the near walls, dead zones at the far ends, an elliptical vs circular jet footprint, the case for oval/non-circular coverage, multiple smaller fans vs one large fan, and directional airflow concepts.
```

**10. Small rooms (bathrooms, kitchens, study rooms < 8 m²)**
```
CONDITION: Very small rooms where the fan sweep is large compared with the room (D/room-width > 0.4). Research over-sized fan behaviour, re-ingesting of its own wake, choosing a smaller sweep, noise in small reflective rooms, and suitability limits by room area.
```

**11. Open-plan, L-shaped and double-height spaces**
```
CONDITION: Open-plan living/kitchen/dining areas, L-shaped rooms, or a fan near a staircase or double-height void, with no nearby walls to return air. Research weak return loops, breeze spreading thin, air escaping through the void, perceived velocity loss, and design or placement responses.
```

**12. Semi-open spaces (balconies, verandas, sit-outs, covered terraces)**
```
CONDITION: The fan runs in a semi-outdoor space with one or more open sides, ambient wind, dust, rain spray and humidity. Research how ambient wind interacts with the downwash, IP/weather ratings, corrosion and UV degradation of materials, and wet-rated outdoor fan designs.
```

### Group 3 — Thermal environment

**13. Thermal stratification (hot air pooled at the ceiling)**
```
CONDITION: Vertical temperature gradients of 2–6 °C between ceiling and floor, especially in top-floor rooms under concrete slabs or tin roofs. Research the fan drawing in hot, less dense air, buoyancy vs momentum (Archimedes/Richardson number), whether the fan destratifies or just re-circulates hot air onto occupants, the comfort impact, the case for reverse/updraft mode, and temperature-aware speed control.
```

**14. Sunlit wall or window (uneven solar heating)**
```
CONDITION: One wall or a large window receives direct sun, creating a thermal plume or updraft on one side of the room. Research the asymmetric convection interacting with the fan jet, airflow being pushed to one side, comfort asymmetry for occupants, and adaptive or directional approaches.
```

**15. Hot-roof top-floor rooms and tin/asbestos-sheet roofs**
```
CONDITION: Radiant heat from the ceiling slab or sheet roof (ceiling surface 40–55 °C in Indian summers). Research the fan pushing heated boundary-layer air onto occupants, the radiant vs convective comfort balance, whether speed or direction changes help, and the effect of heat on blade and motor materials.
```

**16. High humidity / monsoon / coastal climates**
```
CONDITION: Relative humidity of 70–95% (Mumbai, Chennai, Kerala, the North-East). Research the effect of air density and humidity on fan performance, perceived cooling (evaporative effect) vs air speed, the ASHRAE 55 elevated-air-speed comfort zone, condensation, corrosion of metal blades and motor, mould/dust adhesion on blades, and material selection.
```

### Group 4 — Competing ventilation and pressure

**17. Fan used together with an air conditioner**
```
CONDITION: A split/window AC throws a cold horizontal jet across the room while the ceiling fan runs. Research the crossflow shearing the fan's downward air column, cold-air distribution vs short-circuiting the AC return, the energy savings from raising the AC setpoint with a fan (literature data), optimal fan speed with an AC, AC–fan co-ordination features (IR/smart integration), and draft discomfort.
```

**18. Exhaust fans and negative-pressure rooms**
```
CONDITION: Kitchens and attached bathrooms with strong exhaust fans, or rooms with a kitchen chimney, giving negative pressure and infiltration through gaps. Research how a net pressure difference and an extract flow distort the fan's recirculation loop, short-circuit paths, and the interaction with gas-stove flames or smoke (kitchen safety).
```

**19. Cross-ventilation (door–window drafts) and natural wind**
```
CONDITION: An open door and window create a horizontal through-draft of 0.3–2 m/s across the room. Research jet deflection by the crossflow (jet-in-crossflow theory, velocity ratio), loss of coverage under the fan, whether the fan should cooperate with or oppose the cross-draft, and hybrid ventilation strategies.
```

**20. Dust, smoke, kitchen grease and pollution**
```
CONDITION: Rooms with heavy dust (roadside homes, rural, construction areas), cooking oil fumes or incense smoke. Research dust and grease accumulation on blade leading edges, the airfoil roughness effect on air delivery over months (% degradation), imbalance and wobble from uneven deposits, anti-dust coatings (hydrophobic, anti-static) and dust-repellent blade geometries, cleaning frequency, and particle resuspension from the floor.
```

### Group 5 — Furniture and obstacles

**21. Tall wardrobes, shelves and furniture along walls**
```
CONDITION: Floor-to-ceiling wardrobes, lofts and storage that block the wall-climb return path on one or more sides. Research the choked return loop, uneven recirculation, stagnant zones behind furniture, and how blocking a percentage of the perimeter changes air delivery at occupant level.
```

**22. Bed, dining table or desk directly under the fan (ground effect)**
```
CONDITION: A raised surface 0.5–0.8 m high directly beneath the fan, which shortens the jet throw. Research the jet impinging on a near surface, high-velocity rebound, turbulence and gusty sensation in the sleeping/seating zone, papers blowing away at desks, low-speed comfort needs while sleeping (draft risk, ASHRAE draught rating), and fan modes for sleep.
```

**23. Mosquito nets, canopies and partitions**
```
CONDITION: A mosquito net over the bed, cloth canopies, or partition screens within the airflow. Research the porous-screen pressure drop (net porosity vs velocity reduction), air speed inside the net, and fan settings/designs that maintain comfort inside nets (very common in Indian homes).
```

**24. Soft furnishings: curtains, carpets, sofas vs hard surfaces**
```
CONDITION: Absorptive surfaces (carpet, heavy curtains, upholstered sofas) compared with hard reflective surfaces (vitrified tile, marble, concrete). Research the floor and wall boundary-layer friction effects on the recirculation speed, curtains flapping and blocking windows, and the acoustic differences (fan noise in reverberant vs absorptive rooms).
```

**25. High occupancy (classrooms, offices, prayer halls, gatherings)**
```
CONDITION: Many occupants seated or standing under fans: body heat plumes, the obstruction effect of people, CO2/air quality, and noise requirements. Research coverage uniformity, fan density per m², heat plumes from people opposing the downwash, and comfort data from field studies in Indian classrooms and offices.
```

### Group 6 — Electrical and operating conditions (affect speed/Hz)

**26. Voltage fluctuation, low voltage and inverter/solar backup**
```
CONDITION: Supply between 160–270 V, frequent low voltage in rural areas, operation on a home inverter (square/modified-sine wave), or solar DC. Research how voltage and waveform affect RPM and airflow (induction vs BLDC), speed holding, efficiency at low voltage, motor hum/noise on inverters, and BLDC controller strategies to keep aerodynamic output constant.
```

**27. Low-speed operation and sleep / night comfort**
```
CONDITION: The fan runs at its lowest 1–2 speed settings for long hours, e.g. overnight in winter-transitional seasons. Research blade aerodynamic efficiency at low Reynolds numbers (laminar separation, stall at low RPM), the minimum perceptible air speed, noise floors and motor tonal noise at low speed, airflow uniformity at low RPM, and blade designs optimised for the low-speed regime.
```

**28. Vibration, wobble and imbalance in real installations**
```
CONDITION: Fan wobble from imperfect blade balance, uneven mounting hooks, flexible ceilings, long downrods or bent blades. Research how wobble couples with the aerodynamics (cyclic loading, tilted thrust), the natural frequencies of the fan–downrod system vs operating RPM, balancing standards and tolerances, IMU-based wobble detection, and safety implications.
```

---

## Suggested follow-up prompts (after all condition reports are collected)

**S1. Cross-condition synthesis**
```
Attached are research reports on N room conditions affecting ceiling-fan aerodynamics in Indian homes. Build a matrix: condition × (frequency in Indian homes, severity of airflow loss, current market coverage, patent crowding, feasibility for an aerodynamics-led solution). Identify the 3 conditions with the biggest unsolved, high-frequency impact. Then identify any single blade/fan design innovation that addresses several conditions at once.
```

**S2. Adversarial review**
```
Act as a hostile review panel (an aerodynamicist, an Atomberg product manager, a manufacturing engineer, a BEE/BIS certification expert, a cost analyst). Attack our chosen concept [describe]. For each issue: the claim attacked, the failure mechanism, severity, evidence, the test that would settle it, and a fix. End with a must-fix list.
```

**S3. Patent design-around check**
```
For our concept [describe], search for the closest prior art (Google Patents, Espacenet, InPASS). List the top 15 with claim overlap analysis and design-around options, and identify claimable novel features. This is research, not a legal opinion.
```
