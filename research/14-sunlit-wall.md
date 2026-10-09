# Condition 14 — Sunlit Wall or Window (Uneven Solar Heating) — Ceiling Fan Aerodynamics Dossier

*AtomQuest 2026 evidence dossier. Prepared for an aerodynamics-focused hackathon team designing a next-generation ceiling fan for Indian homes.*

---

## 1. Condition definition

**Geometry/parameters.** One wall of the room — most often a window wall or an unshaded masonry wall — receives direct solar radiation for part of the day (typically east-facing in the morning, west-facing in the afternoon/evening, and on upper floors also through skylights). This creates:
- A near-wall warm boundary layer and/or a window-driven convective plume on that one side of the room, while the opposite wall and the rest of the room remain closer to ambient temperature.
- An asymmetric horizontal temperature gradient across the room (hot side vs. cool side), superimposed on the fan's symmetric downwash/recirculation pattern.
- The effect is strongest in rooms with a single large unshaded window or glazed door on one wall, uninsulated masonry exposed to direct sun (west-facing bedroom walls are the classic Indian case), or a skylight/sun-facing dormer.

Quantitatively: Solar Heat Gain Coefficient (SHGC) governs how much radiation enters/is absorbed. Clear single glazing has SHGC ≈ 0.82, i.e., ~82% of incident solar radiation enters as heat ([Studiomatrx — Thermal Performance of Windows: Reading the Spec Sheet](https://www.studiomatrx.org/guides/thermal-performance-of-windows-india)). On a sun-facing wall, solar gain through clear glass "can swamp other heat transfer mechanisms" ([same source](https://www.studiomatrx.org/guides/thermal-performance-of-windows-india)). No single quantified value for the resulting room-air temperature asymmetry (°C difference, hot-side vs. cool-side) in a typical Indian bedroom was found in the sources retrieved — **[UNVERIFIED]**: treat any specific ΔT figure as an estimate until measured.

**Prevalence in India.** No direct Indian survey quantifying the share of homes with one dominant sun-facing wall/window was found in this search pass — **[UNVERIFIED]**. Qualitatively, the condition is extremely common because: (a) most urban apartments and independent houses in India have only one or two external walls with windows (interior walls shared with neighbours), so solar exposure is inherently one-sided; (b) west- and east-facing bedrooms without external shading are common in dense urban plotting; (c) top-floor units with west-facing glazed doors/balconies are frequent in mid-rise housing. This condition frequently co-occurs with Condition 15 (hot-roof top-floor rooms) and Condition 13 (thermal stratification), but is distinguished by being a **horizontal/lateral** asymmetry rather than a purely vertical one.

---

## 2. Aerodynamic physics

**Baseline (symmetric room).** A ceiling fan creates a downward momentum jet (actuator-disk thrust) that impinges on the floor, spreads radially, climbs the walls (wall-jet/Coandă-like attachment), and returns along the ceiling to be re-ingested — a toroidal recirculation cell. In an idealised centred fan in a square room this cell is rotationally symmetric.

**With a sunlit wall.** The physics is a **buoyant-plume-vs-forced-jet interaction**, structurally similar to a "jet in crossflow" problem but here the "crossflow" is itself a natural-convection plume rising off the warm wall/window:
- The warm wall generates a vertical buoyant boundary-layer flow (a wall plume) rising from floor to ceiling on that side of the room. Convection numerical studies of window-driven mixed convection confirm that "airflow pattern and temperature distribution are sensitive to the solar heat gain and, hence, to the type of glass used" ([ScienceDirect — Effect of window-glass type on solar heat gain and velocity/temperature distributions](https://www.sciencedirect.com/science/article/pii/S2214157X23004975)).
- This rising plume meets the fan's radially-spreading floor jet and ceiling-return flow asymmetrically: on the hot-wall side, the fan's downward jet must fight an opposing buoyant upward current near the wall, while on the cool side the fan's wall-climb and return flow proceeds largely unopposed.
- Net effect (based on general jet-in-crossflow / buoyant-jet theory, not condition-specific Indian data — **[UNVERIFIED]** for exact magnitude): the recirculation torus is pushed/skewed toward the cool side; the hot-side floor region gets a weaker, more turbulent air-speed delta; a measurable asymmetry in air speed at occupant height (e.g., the "hot side" of a bed vs. "cool side") can be expected but has not been directly quantified for ceiling-fan rooms in literature found here.
- Governing dimensionless groups: **Richardson/Archimedes number** Ri = gβΔT·L / U² (buoyancy force vs. fan-jet momentum force) — a high Ri near the hot wall means buoyancy can locally overpower or distort the fan's downwash; **Reynolds number** at the blade tip (Re = ρ·V_tip·c/μ) governs blade boundary-layer behaviour and is not directly altered by this condition; jet-spread-rate correlations for the floor jet are modified by the superimposed horizontal buoyancy-driven cross-flow near the hot wall, analogous to jet deflection in a crosswind (see jet-in-crossflow literature: deflection and vortex structures controlled by a velocity/momentum ratio between the jet and the opposing flow — [ResearchGate, "The jet in crossflow"](https://www.researchgate.net/publication/277619426_The_jet_in_crossflow); [ResearchGate — "An experimental study of elevated round jets deflected in a crosswind"](https://www.researchgate.net/publication/223507740_An_experimental_study_of_elevated_round_jets_deflected_in_a_crosswind)).
- A directly relevant finding: an air plume from a ceiling fan at 0.5–1.0 m/s can offset a 2.8–3.3 °C temperature rise for comfort purposes — i.e. fan-driven elevated air speed is a proven *compensating* mechanism for warm conditions in general ([search summary citing ceiling-fan energy-savings literature](https://www.sciencedirect.com/science/article/abs/pii/S1359431108003189)), which is directly relevant to why "point the fan breeze at the hot side more" is a plausible design lever (Section 9).

**Quantified effects specific to this exact condition (sunlit wall + ceiling fan):** not found in the literature retrieved in this pass. No peer-reviewed study was located that directly measures % air-delivery loss, velocity asymmetry, or comfort-vote asymmetry for a ceiling fan operating against one solar-heated wall. **[UNVERIFIED — treat as an open research gap, see Section 9.]**

---

## 3. Role of speed / RPM / frequency

- General elevated-air-speed comfort data from UC Berkeley's Center for the Built Environment (CBE) is directly transferable: at higher ambient/operative temperatures, elevated air movement significantly improves comfort votes versus still air (p<0.001); without air movement the ASHRAE 55 80%-acceptability limit is reached around 26 °C/60–80% RH or 28 °C/60% RH, but *with* air movement more than 80% of subjects found 28–30 °C acceptable ([CBE Berkeley research, cited via search](https://cbe.berkeley.edu/research/epic-integrating-smart-ceiling-fans-study/); related: [Human comfort and perceived air quality in warm/humid environments with ceiling fans](https://www.sciencedirect.com/science/article/abs/pii/S0360132315001614)).
- Preferred air speeds in these CBE studies often exceeded the ASHRAE 0.8 m/s "no personal control" limit, with speeds up to 1.05 m/s maintaining comfort at 28–29.5 °C/50% RH ([CBE Berkeley, cited via search](https://escholarship.org/content/qt5fs9q6fq/qt5fs9q6fq.pdf)).
- For the sunlit-wall condition specifically, the inference (not directly tested in literature found) is that a uniform single-speed setting under-serves the hot side and may slightly over-cool the already-comfortable side. A spatially- or temporally-modulated speed/pulse ("natural breeze" mode) could, in principle, be biased to run harder during hot-wall-plume hours (midday/afternoon on a west wall) — this is an extrapolation, **[UNVERIFIED]** for this exact condition, no direct study found.
- No resonance, beat-frequency, or blade-pass noise issue specific to a one-sided thermal plume was found in the literature; this condition is thermal/aerodynamic, not structural, so RPM-linked vibration coupling (see Condition 28) is not expected to be condition-specific here.
- Reverse/updraft mode: relevant mainly to destratification (Condition 13) rather than lateral asymmetry; no evidence found that reverse mode corrects a sunlit-wall asymmetry. **[UNVERIFIED]**

---

## 4. Blade and fan geometry levers

No sunlit-wall-specific blade-geometry study was found. Based on first-order reasoning from the jet-in-crossflow/buoyant-plume physics in Section 2, ranked by *plausible* impact (not validated by condition-specific test data — mark all as **[UNVERIFIED]** until measured):

1. **Fan placement/offset toward the hot wall** (a placement/architectural lever, not blade geometry) — biases the downwash to counter the plume before it develops; cheapest lever, but conflicts with Condition 7 (near-wall mounting) trade-offs.
2. **Asymmetric/directional blade pitch or twist** (non-uniform pitch around the azimuth, synchronized electronically or mechanically with blade position) — could, in principle, deliver more thrust on the hot-wall side of each revolution. No existing commercial product found implementing this for thermal asymmetry; patents exist for *reversible* asymmetric blades for forward/reverse airflow efficiency (US6116856A, below) but not for azimuthally-varying thrust.
3. **Blade count / sweep diameter** — larger sweep closer to the hot wall increases momentum reach into the plume zone, but conflicts with wall-clearance safety rules (see Condition 7/2).
4. **Winglets/tip shape** — could reduce tip-vortex losses generally, improving overall thrust-per-watt, which indirectly helps overcome a stronger opposing plume, but is not condition-specific.
5. **Downrod length / blade-to-ceiling clearance** — affects overall jet throw and might marginally change how far the downwash projects before meeting the rising plume, but this is a second-order effect versus placement.

---

## 5. Materials and manufacturing

No condition-specific material requirement was identified (unlike, e.g., Condition 16's humidity/corrosion drivers or Condition 12's weather-rating drivers). Standard blade/hub/housing materials (aluminium sheet, ABS/ASA/PP, glass-fibre-reinforced nylon) are unaffected by lateral thermal asymmetry. The only plausible material lever is on the **electronics side**: if a solution involves a thermal/IR sensor (Section 11) facing the hot wall, sensor housing would need to tolerate elevated local radiant temperature near the canopy — a minor, not fan-blade-related, consideration. **[UNVERIFIED — no source found addressing this specific interaction.]**

---

## 6. Current market solutions

No company was found marketing a ceiling-fan feature specifically targeting "sunlit wall / asymmetric solar heating." The table below lists general smart/sensing and airflow-direction features from major brands that are the *closest adjacent* capabilities (temperature sensing, app control, reverse mode) — none of these are verified to specifically detect or compensate for a one-sided solar plume.

| Company | Model(s) | Sweep / blades / RPM | Air delivery (m³/min) | Power (W) | Service value | Feature closest to this condition | How it works | Evidence | What it still fails to solve |
|---|---|---|---|---|---|---|---|---|---|
| Atomberg | Renesa 1400mm | 1400mm, 3-blade | ~270 | 28 | High (BLDC) | None condition-specific; app/voice control, Inverter Stabilization (165–285V) | BLDC + IoT control | [Atomberg product page](https://atomberg.com/atomberg-renesa-halo-bldc-motor-3-blade-ceiling-fan); [Atomberg catalogue PDF](https://lightinside.in/wp-content/uploads/2025/07/Atomberg-Fans-Catalogue-Summer-2025-2-sided-LR.pdf) | No directional/asymmetric thrust or wall-plume sensing |
| Atomberg | Efficio Alpha | — | ~230 | 28 | High | Uniform symmetric downwash only | BLDC | [Atomberg product page](https://atomberg.com/products/shop-ceiling-fans-atomberg-efficio-alpha-bldc-motor-with-remote-3-blade-ceiling-fan) | Same as above |
| Atomberg | Ikano 1400mm | 1400mm, 3-blade | ~255 | 35 | High | Same | BLDC | [Atomberg product page](https://atomberg.com/products/shop-ceiling-fans-atomberg-ikano-bldc-motor-with-remote-3-blade-ceiling-fan-1) | Same as above |
| Various (US patent holders, not confirmed sold in India) | "Automatic occupancy and temperature control" fans | — | — | — | — | Single ambient-temperature sensor + PIR occupancy to vary fan speed | Room-average temperature sensing, not spatial/directional | [US6415984B1](https://patents.google.com/patent/US6415984B1/en); [US5996898A](https://patents.google.com/patent/US5996898A/en); [US6189799B1](https://patents.google.com/patent/US6189799B1/en) | Senses only bulk room temperature — cannot detect *lateral* asymmetry from a sunlit wall; no directional response |
| Big Ass Fans (global, HVLS) | Haiku / SenseME | — | — | — | — | Onboard thermostat + occupancy sensing (SenseME) | Adjusts speed to room temperature, not spatial gradient | **[UNVERIFIED — not independently confirmed in this search pass; based on general brand knowledge, no link retrieved]** | Same limitation — bulk sensing, not directional |
| Crompton, Havells, Orient, Usha, Bajaj, Polycab, Luminous, Superfan, Gorilla, Panasonic, Hunter, Minka-Aire, Modern Fan Co., Dyson | — | — | — | — | — | No condition-specific feature found | — | **[UNVERIFIED — no company-specific evidence located for this exact condition in this search pass; further brand-by-brand searching needed]** | Gap is market-wide |

**Conclusion for Section 6:** No manufacturer claim or verified spec was found addressing lateral solar-plume compensation. This is consistent with Section 9's conclusion that this is a genuine, largely unaddressed gap — but the market table above is **incomplete**; a dedicated follow-up search per brand (spec sheets, patents filed by each OEM) is recommended before finalizing a competitive claim.

---

## 7. Academic and industry research

- **Window-glass type vs. room airflow/temperature (mixed convection CFD):** ANSYS Fluent, RNG k-ε turbulence model, used to study how window-glass SHGC affects resulting indoor velocity and temperature distribution in air-conditioned rooms — directly relevant methodology (not ceiling-fan-specific) for how a solar-heated glazing surface distorts room airflow. ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2214157X23004975))
- **Jet-in-crossflow / buoyant plume deflection literature** (not room/fan-specific, but foundational physics): jet deflection by an opposing flow or buoyant plume is governed by a momentum/velocity ratio and produces counter-rotating vortex pairs and shear-layer/horseshoe vortices that control plume deformation ([ResearchGate — "The jet in crossflow"](https://www.researchgate.net/publication/277619426_The_jet_in_crossflow); [ResearchGate — "An experimental study of elevated round jets deflected in a crosswind"](https://www.researchgate.net/publication/223507740_An_experimental_study_of_elevated_round_jets_deflected_in_a_crosswind); [Springer — buoyant jets/plumes in turbulent channel crossflow, DNS](https://link.springer.com/article/10.1007/s10652-024-09974-0)).
- **CBE Berkeley ceiling fan comfort studies:** multiple controlled-chamber human-subject studies (2012 onward) quantify elevated-air-speed comfort benefits and preferred speeds versus ASHRAE 55 limits ([escholarship PDF](https://escholarship.org/content/qt5fs9q6fq/qt5fs9q6fq.pdf); [ScienceDirect — Human comfort and perceived air quality with ceiling fans](https://www.sciencedirect.com/science/article/abs/pii/S0360132315001614); [CBE project page — EPIC smart ceiling fans/thermostats](https://cbe.berkeley.edu/research/epic-integrating-smart-ceiling-fans-study/)). CBE also maintains an "Advanced Ceiling Fan Design Tool" and a fans guidebook with design tools ([CBE design tool](https://cbe.berkeley.edu/research/advanced-ceiling-fan-design-tool); [CBE fans guidebook](https://cbe-berkeley.gitbook.io/fans-guidebook/full-guidebook/design-tools)) — useful reference for CFD/validation methodology in Section 10, though not confirmed to address lateral solar asymmetry specifically.
- **Direct academic study of "ceiling fan + sunlit wall / asymmetric solar heating"**: none found in this search pass. This is flagged as a literature gap (Section 9), not a confirmed absence of all research — a deeper search (IIT/IISc theses, ASHRAE RP project database, CEPT Ahmedabad) is recommended as a follow-up and was not exhaustively completed here. **[UNVERIFIED — gap, not proof of non-existence.]**
- **CFD approach recommendation (inferred from standard practice, not condition-specific source):** Reynolds-Averaged Navier-Stokes (RANS) with buoyancy (Boussinesq or full compressible) coupled to a rotating reference frame (MRF) for the fan blades, validated against point velocity/temperature measurements, is the standard approach used in the window-glass mixed-convection study above and is a reasonable starting template — **[UNVERIFIED]** for this exact condition's mesh/BC choices since no condition-specific CFD paper was found.

---

## 8. Patent landscape

Patents found address *adjacent* mechanisms (directional/reversible blades, occupancy+temperature sensing) but none explicitly claims detection of or compensation for a **laterally asymmetric solar-driven thermal plume**. All of the below are flagged for the design team to review directly before any design-around decision; this is research, not legal opinion.

| Patent no. | Assignee | Priority date | Jurisdiction | Legal status | Core mechanism | Independent-claim summary | Relevance to this condition | Overlap risk | Design-around idea | Link |
|---|---|---|---|---|---|---|---|---|---|---|
| US6116856A | Patterson Technique, Inc. | **[UNVERIFIED — date not confirmed in this pass]** | US | **[UNVERIFIED]** | Bi-directional fan, asymmetric reversible blades | Blades asymmetric in shape, orientation adjustable between two positions for different forward/reverse efficiency | Low-Med — asymmetric blade concept exists but for forward/reverse switching, not azimuthal thrust bias | M | Design a blade whose asymmetry is fixed and radially-biased rather than reversible-flip based | [Google Patents](https://patents.google.com/patent/US6116856A/en) |
| US8721305B2 | **[UNVERIFIED — assignee not confirmed]** | **[UNVERIFIED]** | US | **[UNVERIFIED]** | Ceiling fan with variable blade pitch and variable speed control | Inserts allow blade angle-of-attack adjustment without changing hub/blade geometry | Low-Med — variable pitch is a lever, but patent targets efficiency/speed range, not thermal-plume compensation | L-M | Use variable pitch per-blade-position rather than globally | [Google Patents (USPTO PDF)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8721305) |
| US7726945B2 | **[UNVERIFIED — assignee not confirmed]** | **[UNVERIFIED]** | US | **[UNVERIFIED]** | Industrial (HVLS) ceiling fan, tiltable blade tips | Blade tips tilt upward to broaden air distribution | Low — distribution breadth, not lateral thermal compensation | L | N/A — different scale/application (HVLS) | [Google Patents](https://patents.google.com/patent/US7726945B2/en) |
| US6415984B1 | **[UNVERIFIED — assignee not confirmed, appears linked to Danny Parker/Kendall Johnston research, FSEC]** | **[UNVERIFIED]** | US | **[UNVERIFIED]** | Automatic occupancy + temperature control for ceiling fan | PIR occupancy sensor + room temperature sensor on fan motor, housed together, varies speed with temp, suspends motion-control at night | Medium — closest existing approach to "sensing + adaptive speed," but senses bulk room temp only, not spatial/directional gradient | M | Add a **directional** (e.g., multi-point or IR-array) temperature sensor instead of single-point, to detect lateral asymmetry specifically | [Google Patents](https://patents.google.com/patent/US6415984B1/en); [related paper](https://stars.library.ucf.edu/patents/48/) |
| US5996898A / US6189799B1 | Same family as above | **[UNVERIFIED]** | US | **[UNVERIFIED]** | Same occupancy+temperature family | Same | Same as above | M | Same | [US5996898A](https://patents.google.com/patent/US5996898A/en); [US6189799B1](https://patents.google.com/patent/US6189799B1/en) |
| US10379208 / US10823831 / US11906611 / US12158514 | **[UNVERIFIED — assignee not confirmed, likely a ceiling-fan OEM smart-control family]** | **[UNVERIFIED]** | US | **[UNVERIFIED]** | Fan speed control device with adaptive algorithms, occupancy/vacancy detection | Controls rotational speed/direction based on detected occupancy/vacancy, uses noise-cancelling/image-stabilization-style adaptive algorithms | Low-Med — modern adaptive-control family; could overlap if any claim covers "environmental sensor array driving differential control" | M | Avoid claim overlap by using a single scalar sensor input mapped to speed only, OR explicitly claim multi-zone spatial sensing as the novel element | [USPTO PDFs: 10379208](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10379208), [10823831](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10823831), [11906611](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11906611), [12158514](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12158514) |

**Gap note:** Only ~7 families found and most are only partially relevant; the brief's target of 10–20 relevant families was not reached in this pass. A dedicated InPASS (Indian Patent Office) and Espacenet search specifically for "ceiling fan directional airflow sensor" and "ceiling fan asymmetric thermal compensation" was not completed here and is recommended as a follow-up. **[UNVERIFIED — coverage incomplete.]**

---

## 9. Unsolved gaps and opportunities

**What nobody solves today:** No fan on the market senses or compensates for a laterally asymmetric solar thermal plume. Existing "smart" fans (Section 6, 8) sense only bulk/average room temperature and/or occupancy — a single scalar — so they cannot tell that one side of the room is hotter than the other, let alone bias airflow toward it. The physics gap (Section 2) is real (buoyant plume vs. symmetric downwash) but **not yet quantified** in literature for this specific geometry — this is itself part of the opportunity (nobody has published the baseline loss number, so claiming a fix is currently unverifiable and should be measured first, see Section 10).

**Why unsolved:** (a) cost — adding spatial/directional sensing (vs. one thermistor) raises BOM cost; (b) physics complexity — detecting a plume vs. detecting general room heating requires either multiple sensors or an IR camera/array, uncommon in a ₹2,000–6,000 consumer fan; (c) user behaviour — most users simply run the fan at max speed regardless, which partially self-corrects by over-powering any asymmetry, reducing perceived urgency for manufacturers; (d) standards — IS 374:2019/BEE testing is a single-point, still-air-cube air-delivery test, with no spatial-uniformity or asymmetry metric, so there is no certification pressure to solve this.

**Concept directions (quantified estimates are placeholders pending Section-10 testing — mark all as early-stage hypotheses):**

1. **Multi-point/IR-array temperature sensing + differential blade pitch or dual-fan bias.** Mechanism: detect which side of the room is warmer (e.g., 2–4 point IR or thermistor array at the canopy, or a cheap thermopile looking outward) and bias airflow (via variable individual blade pitch, or asymmetric RPM in a twin-fan room) toward the hot side. Expected benefit: **[UNVERIFIED estimate]** possibly restoring comfort-vote parity between the two room halves; needs lab measurement. Risk: added cost/complexity, calibration drift. Cost impact: moderate (added sensors + actuation). Novelty vs. patents: likely novel relative to Section 8 (closest patents sense occupancy/bulk temp only) — moderate overlap risk with the US6415984B1 family if not carefully differentiated.
2. **Software-only mitigation via oscillating/pulsed "natural breeze" mode timed to the sun's path.** Mechanism: no new sensor — use a real-time-clock + user-entered window orientation (in the companion app) to run a scheduled asymmetric pulse pattern (e.g., longer high-speed bursts in the afternoon for a west-facing room). Expected benefit: low-cost comfort improvement, no hardware change. Risk: not adaptive to cloud cover/actual plume; purely schedule-based. Cost impact: near-zero (firmware only). Novelty: likely low patent risk since it is a software scheduling feature, but weak compared to true sensing.
3. **Low-cost single off-axis thermistor + simple two-zone logic.** Mechanism: one extra temperature sensor mounted at the canopy edge facing the presumed hot wall (installer selects orientation at setup) compared against the existing central/ambient sensor; drives an existing variable-speed BLDC controller harder when a ΔT threshold is exceeded. Expected benefit: incremental; cheapest "do something" option. Risk: single-point sensor captures only one direction, won't generalize to arbitrary room layouts. Cost impact: low (one extra thermistor + firmware logic). Novelty: differentiates from Section 8 patents by using differential (two-sensor) logic rather than single bulk-temperature logic — worth checking against US6415984B1 claims carefully.
4. **Reflective/low-emissivity window film or shading recommendation bundled with the fan app (non-aerodynamic, behavioural).** Mechanism: app nudges user to add window film/curtain based on detected ΔT, addressing the root cause (solar gain) rather than compensating aerodynamically. Expected benefit: could be larger than any fan-side fix, since SHGC reduction attacks the plume at its source. Risk: outside "aerodynamics" scope the hackathon is judged on; may be seen as a cop-out rather than an innovation. Cost impact: zero fan-side cost, but not a hardware differentiator.
5. **Asymmetric/bi-modal blade pitch (two opposing blades with different fixed pitch) to create an inherently non-uniform-but-stable thrust distribution** biased toward one side, selectable at installation (installer points the "high-thrust" side at the sun-facing wall). Mechanism: borrows directly from the reversible-asymmetric-blade concept in US6116856A but fixes the bias rather than flipping it. Expected benefit: **[UNVERIFIED]**, likely modest without active sensing, and risks non-uniform vibration/wobble (interacts with Condition 28) since asymmetric static thrust around the hub can create cyclic loading. Cost impact: low (geometry change only, no new electronics). Novelty: moderate; must be checked for overlap with US6116856A and US8721305B2 claims.

---

## 10. Measurement and validation plan

**Cheap real-room test:**
- **Setup:** A typical bedroom/living room (per Part A context: ~3×3.5 m, 2.75 m ceiling) with one wall/window exposed to direct sun for a known period (track via a simple solar-position calculation or just "west wall, 2–5 pm").
- **Instruments:** 
  - Hot-wire or hot-sphere anemometer (or an array of cheap vane/hot-wire anemometers) for air speed.
  - A grid of thermocouples or cheap DS18B20-style digital temperature sensors at 2–3 heights (0.1 m, 0.6 m, 1.1 m — ankle/seated/head per ASHRAE 55 convention) and at least 2 horizontal positions (near hot wall, near cool wall).
  - Smoke/fog visualisation (incense stick or fog machine) to visually confirm plume deflection of the downwash on video.
  - Sound meter (dB(A)) and power meter (W) — standard instrumentation, per Part A.
- **Grid points:** Minimum a 3×3 horizontal grid (hot-wall side, centre, cool-wall side) × 3 heights = 9 points, measured with fan off (baseline plume only), fan on at low/med/high speed, and across at least two times of day (midday direct sun vs. evening no-sun) to isolate the plume's real contribution.
- **Metrics to report:** air speed asymmetry (Δv between hot-side and cool-side at occupant height, m/s), temperature asymmetry (ΔT, °C) with and without the fan running, comfort-relevant combined metric (e.g., SET* or simple ASHRAE 55 elevated-air-speed offset calculation), noise (dB(A)), power draw (W).
- **What this directly fills:** this is exactly the quantified baseline missing from Sections 2 and 9 above — recommended as the team's first deliverable before building any sensing/control hardware.

**CFD study:** Model the room as a buoyancy-coupled RANS simulation (Boussinesq approximation sufficient for the small ΔT expected, full compressible if ΔT is large) with the fan represented via MRF (moving reference frame) rotating blade zone, k-ω SST or RNG k-ε turbulence closure (consistent with the window-glass mixed-convection methodology cited in Section 7), solar gain applied as a wall heat-flux or temperature boundary condition on the sun-facing wall/window (calibrated from measured wall surface temperature, not assumed). Validate against the real-room grid-point measurements above (air speed and temperature at the same 9+ points) before trusting the CFD for design iteration.

---

## 11. Sensors and smart control

Directly relevant, since this condition is fundamentally about *detecting an asymmetry the fan currently cannot see*:
- **Existing implementations** only detect bulk/average room temperature and/or occupancy (PIR), as catalogued in Section 8 (US5996898A, US6189799B1, US6415984B1, and the newer US10379208 family) — none detect spatial/directional temperature gradients.
- **IMU wobble, current draw** sensing (relevant to Condition 28) are unrelated to this condition.
- **Plausible new sensing approaches** (not found as existing products — opportunity, see Section 9, Concept 1 and 3): a 2-point or array thermistor/IR setup, or even reusing a smartphone-app-entered "which wall gets sun" input combined with time-of-day scheduling (Section 9, Concept 2) as a zero-new-hardware stopgap.
- No evidence found of ultrasonic distance or occupancy sensing being relevant to *this specific* condition (those are more relevant to Condition 2/21/22 clearance detection).

---

## 12. Summary

**Executive summary:** A sunlit wall or window creates a one-sided buoyant thermal plume that is physically expected — by general jet-in-crossflow and buoyant-plume theory — to skew a ceiling fan's symmetric downwash/recirculation pattern toward the cooler side of the room, leaving the hot side under-served. However, this exact interaction has not been directly measured or published for residential ceiling fans in the literature surfaced in this research pass: the quantified "how much worse is it" number does not yet exist, and no current product (Atomberg or competitors) senses or compensates for this lateral asymmetry — all commercial "smart" sensing found is bulk/average-temperature or occupancy-only. The clearest opportunity is therefore two-staged: first, measure the real baseline asymmetry in a real Indian room (Section 10) — a cheap, fast experiment the team should run before anything else — and second, pursue a differential/spatial sensing approach (Section 9, Concepts 1 or 3) that is likely to clear existing patents (Section 8) if designed around multi-point/directional sensing rather than the single-point bulk-temperature logic those patents claim.

**Top 5 insights:**
1. The core physics (buoyant plume opposing/skewing a forced downwash jet) is well-established in general fluid dynamics (jet-in-crossflow, buoyant plume literature) but has **not been published for this specific ceiling-fan-room configuration** — this is a genuine literature gap, not just a market gap.
2. Elevated air speed from a ceiling fan is independently proven (CBE Berkeley) to meaningfully extend comfort at higher temperatures (up to 1.05 m/s maintaining comfort at 28–29.5 °C) — so the *tool* for compensating a hot side (more airflow there) is well-validated in principle, even though the *diagnosis* (detecting the asymmetry) is not solved.
3. All existing "smart" occupancy/temperature-sensing ceiling-fan patents (US5996898A family, US6415984B1, and the newer US10xxxxxx family) use a single bulk sensor — none claim spatial/directional sensing, leaving a plausible, patent-clear design space for differential/multi-point sensing.
4. IS 374:2019 / BEE testing measures air delivery in a controlled, symmetric still-air setup with no spatial-uniformity or asymmetry metric — so there is no regulatory pressure today pushing manufacturers to address this, reinforcing that it is a genuine unexploited differentiator rather than a solved-but-unmarketed problem.
5. The cheapest, fastest next step is not a new blade or sensor — it's the Section 10 real-room measurement, because every subsequent design decision (whether sensing is even worth adding, how big the fix needs to be) depends on a baseline number that does not yet exist in literature.

**Open questions / what could not be found:**
- No quantified ΔT (hot-side vs. cool-side) or Δv (air-speed asymmetry) for a typical Indian room with one sun-facing wall and a running ceiling fan.
- No direct academic paper (IIT/IISc, CEPT, LBNL/CBE, ASHRAE RP) specifically studying ceiling fans under one-sided solar thermal loading — only adjacent window-glass/mixed-convection CFD studies and general buoyant-plume/jet-in-crossflow theory were found.
- Patent search coverage is incomplete (only ~7 families found vs. the 10–20 target); InPASS (Indian Patent Office) and Espacenet were not separately queried in this pass.
- No company-by-company verification completed beyond Atomberg's own spec sheets; competitor (Crompton, Havells, Orient, Usha, Bajaj, Polycab, Luminous, Superfan, Gorilla, Panasonic, Hunter, Minka-Aire, Modern Fan Co., Dyson) specs and any condition-specific claims were not individually verified — flagged as a follow-up task.
- No Indian-specific prevalence statistic for "homes with one dominant sun-facing wall/window" was found.

---

## Sources

- [Atomberg — Renesa Halo product page](https://atomberg.com/atomberg-renesa-halo-bldc-motor-3-blade-ceiling-fan)
- [Atomberg — Efficio Alpha product page](https://atomberg.com/products/shop-ceiling-fans-atomberg-efficio-alpha-bldc-motor-with-remote-3-blade-ceiling-fan)
- [Atomberg — Ikano product page](https://atomberg.com/products/shop-ceiling-fans-atomberg-ikano-bldc-motor-with-remote-3-blade-ceiling-fan-1)
- [Atomberg — Summer 2025 catalogue PDF](https://lightinside.in/wp-content/uploads/2025/07/Atomberg-Fans-Catalogue-Summer-2025-2-sided-LR.pdf)
- [Studiomatrx — Thermal Performance of Windows: Reading the Spec Sheet (India)](https://www.studiomatrx.org/guides/thermal-performance-of-windows-india)
- [ScienceDirect — Effect of window-glass type on solar heat gain and velocity/temperature distributions inside air-conditioned rooms](https://www.sciencedirect.com/science/article/pii/S2214157X23004975)
- [ScienceDirect — Thermal comfort enhancement by using a ceiling fan](https://www.sciencedirect.com/science/article/abs/pii/S1359431108003189)
- [ResearchGate — The jet in crossflow](https://www.researchgate.net/publication/277619426_The_jet_in_crossflow)
- [ResearchGate — An experimental study of elevated round jets deflected in a crosswind](https://www.researchgate.net/publication/223507740_An_experimental_study_of_elevated_round_jets_deflected_in_a_crosswind)
- [Springer — Characteristics of planar buoyant jets and plumes in a turbulent channel crossflow (DNS)](https://link.springer.com/article/10.1007/s10652-024-09974-0)
- [ResearchGate — The thermal interaction of a buoyant plume from a calandria tube with an oblique jet](https://www.researchgate.net/publication/309546126_The_thermal_interaction_of_a_buoyant_plume_from_a_calandria_tube_with_an_oblique_jet)
- [CBE Berkeley — EPIC: Integrating Smart Ceiling Fans and Thermostats](https://cbe.berkeley.edu/research/epic-integrating-smart-ceiling-fans-study/)
- [CBE Berkeley — Spatial Uniformity of Thermal Comfort from Ceiling Fans (eScholarship PDF)](https://escholarship.org/content/qt5fs9q6fq/qt5fs9q6fq.pdf)
- [ScienceDirect — Human comfort and perceived air quality in warm and humid environments with ceiling fans](https://www.sciencedirect.com/science/article/abs/pii/S0360132315001614)
- [CBE Berkeley — Advanced Ceiling Fan Design Tool](https://cbe.berkeley.edu/research/advanced-ceiling-fan-design-tool)
- [CBE Berkeley — Fans Guidebook, Design tools](https://cbe-berkeley.gitbook.io/fans-guidebook/full-guidebook/design-tools)
- [Alephindia — BEE Star Ratings for Electric Ceiling Fans IS 374](https://alephindia.in/bee-star-ratings-for-electric-ceiling-fans-is-374.php)
- [Bijli Bachao — New BEE Star Rating Standards for Ceiling Fans in India](https://www.bijlibachao.com/fans/new-beee-star-rating-standards-ceiling-fans.html)
- [BL-India — BIS ISI and BEE Certification for Ceiling Fans — IS 374:2019](https://www.bl-india.com/products/ceiling-fans)
- [Google Patents — US6116856A, Bi-directional fan having asymmetric, reversible blades](https://patents.google.com/patent/US6116856A/en)
- [Google Patents — US7726945B2, Industrial ceiling fan](https://patents.google.com/patent/US7726945B2/en)
- [USPTO PDF — US8721305B2, Ceiling fan with variable blade pitch and variable speed control](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8721305)
- [Google Patents — US5996898A, Automatic occupancy and temperature control for ceiling fan operation](https://patents.google.com/patent/US5996898A/en)
- [Google Patents — US6189799B1, Automatic occupancy and temperature control for ceiling fan operation](https://patents.google.com/patent/US6189799B1/en)
- [Google Patents — US6415984B1, Automatic occupancy and temperature control for ceiling fan operation](https://patents.google.com/patent/US6415984B1/en)
- [UCF STARS — Automatic Occupancy and Temperature Control for Ceiling Fan Operation (Parker & Johnston)](https://stars.library.ucf.edu/patents/48/)
- [USPTO PDF — US10379208, Fan speed control device](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10379208)
- [USPTO PDF — US10823831, Fan speed control device](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10823831)
- [USPTO PDF — US11906611, Fan speed control device](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11906611)
- [USPTO PDF — US12158514, Fan speed control device](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12158514)
