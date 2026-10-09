# Comparison Cards: Conditions 15–21

---

### 15 — Hot-Roof Top-Floor Rooms / Tin & Asbestos-Sheet Roofs
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | Tier-2/3 India, rural, construction/labour housing (§1, prevalence) |
| SEV | 4 | Roof surface 40–55 °C, radiant asymmetry exceeds ISO 7730 comfort thresholds (§2, physics) |
| UNSOLVED | 5 | No mainstream product feature found addressing hot-roof radiant load (§6, market solutions) |
| PATENT_ROOM | 4 | Temperature-differential patents exist but not direct IR/radiant sensing (§8, patent landscape) |
| AERO_FIT | 2 | Dominant discomfort is radiant, not convective; fan airflow cannot fix mean radiant temperature (§2, physics ceiling) |
| EVIDENCE | 3 | ISO 7730 standards cited, CBE/cool-roof studies analogous, but no India-specific hot-roof ceiling-fan test (§7, research) |
| PROTO | 4 | IR sensor + firmware and reflective coating are room-testable with IR thermometer, anemometer grid (§10, validation plan) |
| **TOTAL** | **28** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Roof surfaces commonly reach 40–55 °C under direct summer sun in India (§1, condition definition)
- Radiant temperature asymmetry discomfort threshold ~5 K (Category A/B) to 7 K (Category C) per ISO 7730 (§2, physics)
- Cool-roof coatings cut indoor temps up to ~3.9 °C (May, unconditioned) in Indian field tests (§7, research)
- Fan-driven convection raised radiant slab cooling capacity 16% (at 24 °C) and 26% (at 26 °C) per CBE Berkeley study (§2, physics)

**Core unsolved gap (1 sentence):** No current product addresses the radiant channel at all; every mainstream fan (Atomberg, Crompton, Bajaj, Orient, etc.) only offers faster air movement, which raises convective offset but cannot touch mean radiant temperature, and physics suggests a hard ceiling exists for what blade-only solutions can achieve.

**Best concept direction from report (1–2 sentences):** IR/thermopile ceiling-surface sensor + auto speed boost to detect roof surface heat directly and pre-emptively run at max CMM, or reflective/low-absorptivity top-surface blade coating to reduce blade heat-soak and re-radiation, paired with guidance on passive roof-side mitigation (insulation, light-colour coating) since the biggest gains may be roof-side, not fan-side.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US5189412A (temperature-triggered reverse mode [UNVERIFIED assignee]); US6189799B1 (occupancy + temperature sensing [UNVERIFIED]); US6415984B1 (continuation [UNVERIFIED]); CA2717398A1 / AU2009212565B2 / US8900041B2 / US12006945B2 (temperature-differential control [UNVERIFIED — appears to be one patent family across jurisdictions]).

**Links to other conditions (NN list + why):** 16 (humidity + radiant heat interact with blade material durability); 05 (blade-obstruction proximity at low clearance worsens radiant exposure); 02 (low-ceiling fans have reduced clearance, worse for hot-roof cases).

---

### 16 — Humidity-Monsoon / Coastal Climates
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | Coastal/NE + monsoon-universal across India; seasonal effect (§1, prevalence) |
| SEV | 3 | ~1.2 m/s air speed needed for comfort vs ~0.8 m/s baseline; corrosion risk to blades (§2, physics; §5, materials) |
| UNSOLVED | 4 | No corrosion test data, no RH-aware speed control, potential air-speed gap (§9, gaps) |
| PATENT_ROOM | 3 | 3–4 general coating/corrosion patents found, no humidity-specific family (§8, patents) |
| AERO_FIT | 1 | ~1% density change; main issue is evaporative cooling (comfort), not aerodynamics (§2, physics) |
| EVIDENCE | 4 | CBE/ASHRAE evidence on air-speed need; IS 374:2019 mandates corrosion testing but no India-specific field/CFD (§7, research; §5, materials) |
| PROTO | 5 | RH-aware speed control is firmware-only; durability tests per IS 374:2019 are standard (§10, validation) |
| **TOTAL** | **25** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Humid air is roughly 1% less dense than dry air at the same temperature (85°F, RH 20%→90%), with negligible (~1%) effect on volumetric airflow (§2, physics)
- CBE Berkeley found >80% of subjects rated conditions acceptable at 28°C/80%RH, 30°C/60%RH, 30°C/80%RH with fan-driven air movement; ~1.2 m/s needed at 30°C/80%RH (§3, speed)
- IS 374:2019 explicitly includes humidity-chamber and rust-resistance testing as part of BIS certification (§5, materials)
- Condensation combined with airborne dust creates adherent biofilm substrate for mould growth in HVAC contexts (§2, physics)

**Core unsolved gap (1 sentence):** Every "anti-rust"/"electroplated" claim found is brand marketing without published independent test data (salt-spray ASTM B117 or humidity-chamber cycling); meanwhile occupants need 1.0–1.2 m/s air speed at head height to stay comfortable in high RH, near or above what many fans deliver, but this target is unverified against real Indian room measurements.

**Best concept direction from report (1–2 sentences):** RH-aware auto-speed control: add a cheap capacitive RH sensor to BLDC controller firmware; above ~75–80% RH, auto-raise target air speed toward the 1.0–1.2 m/s occupant-height band identified by CBE research. Also publish, third-party-verified corrosion test data as a marketing/trust differentiator, closing the evidence gap with actual salt-spray (ASTM B117) or IS 374:2019 humidity-chamber results rather than unsubstantiated brand claims.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US20110104397A1 (printing patterned powder-coat [UNVERIFIED]); WO2015047756A1 (sacrificial anode layer [UNVERIFIED]); US20150211371A1 (ceiling fan blade manufacturing method [UNVERIFIED]); US10309663 (condensation control system [UNVERIFIED]).

**Links to other conditions (NN list + why):** 15 (heat + humidity + poor evaporative cooling combined in coastal summer); 20 (dust + moisture condensation creates film faster); 05 (blade corrosion affects stiffness and flutter risk at high RPM).

---

### 17 — Ceiling Fan Used Together With an Air Conditioner
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 3 | Common pairing in AC-equipped urban homes, but report finds no national dataset and notes it is "rare in rural/un-electrified-AC contexts" — not calibrated as near-universal (§1, definition) |
| SEV | 2 | AC provides main cooling; fan is auxiliary for mixing and draft avoidance below 22.5°C (§2, physics) |
| UNSOLVED | 4 | No AC-aware automatic speed control despite existing IoT hardware in Atomberg/Crompton (§9, gaps) |
| PATENT_ROOM | 3 | US8900041B2, US9353964B2, and others on HVAC/fan coordination exist (§8, patents) |
| AERO_FIT | 2 | Fan-driven mixing dominates; leverage is speed/RPM control, not aerodynamic blade redesign (§2, physics) |
| EVIDENCE | 4 | UC Berkeley CFIAC chamber/human-subject studies + 36% compressor-savings field study (§7, research) |
| PROTO | 5 | Standard anemometer grid + AC + fan in a real room (§10, validation plan) |
| **TOTAL** | **25** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Rooms at 26–28°C with fan-on achieve ~73.7–100% acceptance, comparable to 23°C fan-off reference; near-neutral sensation at 28°C + low downward fan vs 26°C reference (§2, physics)
- SET model correctly predicts comfort (not simple PMV/PPD) with R² = 0.9 (§2, physics)
- Two-year retrofit field study: 36% measured compressor energy savings with 99 automated ceiling fans staged with AC (§7, research)
- ASHRAE 55 caps air speed at 0.15 m/s for operative temperatures below 22.5°C to avoid local cold draft discomfort (§2, physics)

**Core unsolved gap (1 sentence):** No Indian BLDC fan (Atomberg, Crompton, Havells) implements automatic AC-state-aware speed control despite having IR remote + app/IoT hardware already in their products; the only verified, quantified coordination result (36% compressor energy savings) comes from a US commercial automated-fan retrofit, leaving a clear market gap for coordinated residential fan+AC operation tuned to the SET-optimal comfort point.

**Best concept direction from report (1–2 sentences):** AC-state-aware fan speed control via IR/current-sensing on the AC unit or a simple room-temperature-trend-based schedule that automatically steps fan speed down as room temperature falls, targeting the SET-optimal point rather than a fixed user-selected speed. Alternatively, a reverse/updraft "cold-draft mitigation" mode specifically marketed for fan+AC bedrooms, reducing ankle-level cold-draft complaints as the room cools below ~22.5°C.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US8900041B2 (automatic temperature-differential fan control [UNVERIFIED]); US9353964B2 (wirelessly-enabled HVAC control [UNVERIFIED]); US8688243B2 (fan control within HVAC systems [UNVERIFIED]); US11449020B2 (ceiling fan controls thermostat via occupant presence [UNVERIFIED]).

**Links to other conditions (NN list + why):** 13 (thermal stratification + fan destratification); 18 (negative-pressure exhaust interference); 28 (vibration/wobble at high sustained speed if fan runs continuously at AC-assisting speed).

---

### 18 — Exhaust-Negative-Pressure Rooms
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | Kitchen/bathroom exhaust universal in urban apartments; high-frequency conflict (§1, definition) |
| SEV | 2 | Short-circuit effect + jet deflection proven in literature, but quantified effect size on occupant coverage unknown; LPG safety unquantified (§2, physics; §9, gaps) |
| UNSOLVED | 4 | No product senses/compensates for negative pressure; commercial make-up-air solution not retrofit-friendly (§9, gaps; §6, market) |
| PATENT_ROOM | 5 | No specific ceiling fan + exhaust-fan interaction patents found; flagged as white-space (§8, patent landscape) |
| AERO_FIT | 1 | Core mechanism is pressure-driven short-circuit, not aerodynamic blade design (§2, physics; §9, note) |
| EVIDENCE | 2 | DOE/LBNL particle study cited; jet-in-crossflow analogues from mine ventilation; no direct fan+exhaust study (§2, physics; §7, research) |
| PROTO | 4 | Standard chamber-test approach with pressure manometer and anemometer grid (§10, validation plan) |
| **TOTAL** | **23** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Typical Indian kitchen exhaust pulls 200–400 CFM (≈340–680 m³/h); bathroom 50–110 CFM (≈85–185 m³/h); kitchen chimneys ≥1200 m³/h (§1, definition)
- Kitchen air-change rate target: 10–15 ACH (enclosed) or 8–12 ACH (semi-open) (§1, definition)
- NFPA 96 (US code) caps negative pressure at 0.02 in w.c. ≈ 5 Pa; no equivalent mandatory Indian residential make-up-air code found [UNVERIFIED] (§1, definition)
- Ceiling-fan-driven air mixing increased removal rate of ultrafine and >1 µm particles vs. no-mixing baseline, per DOE/LBNL study (§2, physics)

**Core unsolved gap (1 sentence):** Running a kitchen or bathroom exhaust fan alongside a ceiling fan creates a pressure imbalance that pulls part of the ceiling fan's return-air loop out of the room through the open door/gap toward the depressurized space, short-circuiting its recirculation and deflecting its downwash jet — a mechanism well-documented in general HVAC make-up-air and jet-in-crossflow literature but never studied directly for this ceiling-fan-plus-residential-exhaust combination, so quantified effect sizes for Indian rooms do not exist.

**Best concept direction from report (1–2 sentences):** Pressure/current-draw-based load sensing on the ceiling fan to detect an abnormal increase in motor current or RPM droop at fixed PWM/voltage, which could indicate the fan's recirculation loop is disrupted, and respond by nudging speed up to compensate thrust loss. Alternatively, a passive door-airflow baffle or jet-redirection accessory that reduces the short-circuit leakage path without touching the fan itself.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US9574779B2 (exhaust apparatus for enhanced capture [UNVERIFIED]); EP1674799A1 (exhaust hood design [UNVERIFIED]); US6159093A (powered exhaust fan [UNVERIFIED]); CN211950910U (kitchen exhaust fan utility [UNVERIFIED]); CN202228391U ("negative pressure fan" utility [UNVERIFIED]).

**Links to other conditions (NN list + why):** 19 (pressure-driven crossflow similar to wind-driven cross-ventilation); 16 (humidity in kitchens compounds the exhaust-fan problem); 12 (semi-outdoor/damp exhaust-driven conditions).

---

### 19 — Cross-Ventilation (Door–Window Drafts) and Natural Wind
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | Common in independent houses & hot-dry/composite climates; less in sealed dense urban (§1, definition) |
| SEV | 3 | Jet deflection + stagnant zones per JICF physics; coverage shifts but not eliminated (§2, physics) |
| UNSOLVED | 5 | No product, no design guidance for crossflow interaction (§9, gaps; §6, market solutions) |
| PATENT_ROOM | 4 | US20050141997A1 has wind sensor (Medium overlap); others are tangential (§8, patents) |
| AERO_FIT | 4 | Jet-in-crossflow is core aerodynamic problem; velocity ratio r is the design parameter (§2, physics; §4, levers) |
| EVIDENCE | 3 | CBE sidewall-jet study is analogue (not direct); JICF theory cited secondhand; no India-specific test (§7, research) |
| PROTO | 5 | Desk-fan cross-draft + anemometer grid + smoke visualization (§10, validation plan) |
| **TOTAL** | **32** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Cross-ventilation air speeds in Indian homes typically 0.19–0.83 m/s, some configurations reaching 1–2 m/s (§1, definition)
- Outdoor prevailing wind speeds at 10 m height for major Indian cities: Mumbai 3.6, Chennai 3.4, Kolkata 2.7, Bengaluru 2.8 m/s (§1, definition)
- CBE field measurements in 4 Californian buildings: ceiling fans produced mean air speeds 0.2–1.8 m/s downward vs 0.2–0.5 m/s updraft (§3, speed)
- Jet velocity ratio r = U_jet / U_crossflow governs deflection; where r ≈ 1 (fan and draft comparable magnitude), strong deflection/asymmetry should be expected (§2, physics)

**Core unsolved gap (1 sentence):** When a ceiling fan runs under a natural door-window cross-draft (0.3–2 m/s), the fan's downwash is deflected horizontally by jet-in-crossflow physics — a well-understood phenomenon in general engineering but never studied specifically for residential ceiling fans in Indian rooms — so no quantified coverage-loss or air-speed-at-occupant-height change exists in the literature, leaving this a genuine white-space opportunity despite being an everyday condition in cross-ventilated homes.

**Best concept direction from report (1–2 sentences):** Draft-adaptive RPM boost using an ultrasonic or hot-wire anemometer on the fan body/downrod to detect lateral air movement; firmware briefly raises RPM to restore higher velocity ratio r and preserve downward coverage when a strong cross-draft is detected. Alternatively, a tighter jet-column geometry (cf. Hunter's AirColumn concept) marketed specifically for naturally-ventilated/semi-open rooms, where a higher-momentum, narrower jet should resist deflection better than a wide, diffuse jet per JICF scaling.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US8249731B2 (smart air ventilation with occupancy/sound sensing [UNVERIFIED]); US11353033 (ceiling fan with integrated sensing unit [UNVERIFIED]); US20050141997A1 (ceiling fan proximity safety + wind speed sensor [UNVERIFIED]); CN103452879A ("natural wind" ceiling fan [UNVERIFIED]); US6415984B1 (automatic occupancy and temperature control [UNVERIFIED]).

**Links to other conditions (NN list + why):** 07 (off-centre mounting + cross-draft interaction); 13 (thermal stratification + wind-driven buoyancy coupling); 02 (high-ceiling rooms reduce draft effect).

---

### 20 — Dust, Smoke, Kitchen Grease and Pollution
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | Anti-dust lines sold by major brands (mass-market implication); highest in roadside/construction/kitchens (§1, prevalence) |
| SEV | 4 | ~25% airflow loss from LEDA; 30–50% from grease (analogues); increases power (§2, physics) |
| UNSOLVED | 4 | Crompton/Atomberg sell "anti-dust" products, but claims are unverified marketing and grease/self-cleaning/sensor sub-gaps remain unaddressed (§6, §9, gaps) |
| PATENT_ROOM | 3 | 6 coating/mechanical patents found; Medium overlap on coating chemistry (§8, patents) |
| AERO_FIT | 2 | LEDA is surface-roughness effect (material/coating domain), not blade aerodynamic design (§2, physics; §4, levers) |
| EVIDENCE | 2 | SSRN LEDA paper behind paywall (secondary summary only); wind-turbine analogues; no India field data (§7, research) |
| PROTO | 4 | 1–3 month real-room test is feasible; grease comparison test is easy; standard CFD (§10, validation plan) |
| **TOTAL** | **25** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Leading-edge dust accumulation (LEDA) measured at 2–12 mm thickness (§1, definition)
- Secondary summary of SSRN LEDA study: ~25% airflow drop, ~15% RPM loss, ~10% increase in power draw for dusty vs clean fan [UNVERIFIED — could not independently confirm by direct PDF access] (§2, physics)
- Wind-turbine-airfoil roughness: max lift drop up to 30%; 140 µm roughness → lift-to-drag ratio fell 40% (§2, physics)
- Commercial kitchen exhaust-fan grease fouling: 30–50% airflow reduction, 8–25 g/blade mass shift within 1,000 hours (§2, physics)

**Core unsolved gap (1 sentence):** While Crompton claims 50% dust-accumulation reduction and Atomberg markets "anti-dust" blades nationally, no independent, third-party-verified quantification exists for how much dust/grease fouling actually degrades a residential Indian ceiling fan's air delivery, service value, or balance over realistic months-long exposure — all commercial claims are marketing, and grease-fouling data exists only for commercial kitchen exhaust fans, not residential ceiling fans near cooking areas.

**Best concept direction from report (1–2 sentences):** Leading-edge-focused coating/geometry — since LEDA concentrates at the leading edge, a locally-reinforced, smoother, or differently-coated leading-edge strip (rather than whole-blade coating) could be a cheaper, more durable mitigation. Alternatively, IMU/current-draw-based fouling/imbalance detection with a "clean me" alert to prompt user cleaning before airflow degrades significantly, leveraging the imbalance mechanism already documented in grease/exhaust-fan literature.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US6022192A (automatic cleaning pad units via centrifugal force [UNVERIFIED]); CN104912837A (antistatic self-cleaning blade with graphene [UNVERIFIED]); US20110076478A1 (dust-repellent nanoparticle surfaces [UNVERIFIED]); US20120224967A1 (elastic dust-clinging cover [UNVERIFIED]); US6050258 / US5809993 (exhaust fan with dry lubricant coating [UNVERIFIED]).

**Links to other conditions (NN list + why):** 16 (dust + moisture condensation creates adherent film faster); 28 (uneven fouling causes imbalance/vibration); 20 and 21 (dust in kitchens overlaps with exhaust-negative-pressure and wardrobe-blocked rooms).

---

### 21 — Tall Wardrobes, Shelves and Furniture Along Walls
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 5 | "near-ubiquitous" in Indian apartments; floor-to-ceiling almirahs standard (§1, definition) |
| SEV | 3 | Gao et al. shows redirection/stagnation with partial obstacles; full-height case unquantified (§2, physics; §9, gap) |
| UNSOLVED | 5 | No direct study of floor-to-ceiling wardrobes; no market feature found (§9, gap; §6, market) |
| PATENT_ROOM | 4 | ~6 patents found, none squarely on furniture-awareness; US10302094 is closest (Medium overlap) (§8, patents) |
| AERO_FIT | 3 | Wall-return blockage is topological; jet-redirection fix uses aerodynamics of JICF (§2, physics; §4, levers) |
| EVIDENCE | 2 | Gao et al. 2017 is best available but uses short partitions, not floor-to-ceiling; no direct study (§7, research; §9, gap) |
| PROTO | 5 | Follow Gao et al. methodology with full-height wardrobe + anemometer tree (§10, validation) |
| **TOTAL** | **30** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Jet/floor spreading radius with no furniture: 0.7–1.2 m (coverage ≥0.3 m/s threshold) (§2.4, Gao et al. 2017, Table 1)
- Spreading radius with table obstacle: increases to 0.9–1.5+ m on open side, up to ~40% larger than base case (§2.4, Gao et al. 2017, Tables 2–3) |
- Peak air speed at 0.6 m height: 0.3 m/s (no obstacle) → 0.6–1.0+ m/s (with obstacle diverting flow) (§2.4, Gao et al. 2017 §3.2) |
- Corner-partition (2-side blockage) gave the *most uniform* air speed at occupant level of all 6 tested cases (§2.4, Gao et al. 2017 §3.6) |

**Core unsolved gap (1 sentence):** Floor-to-ceiling wardrobes along one or two bedroom walls — a near-ubiquitous feature of Indian apartments — physically block the "wall-return zone" that closes a ceiling fan's room-scale recirculation loop, yet no peer-reviewed study has tested this exact geometry; the best available analogue (Gao et al. 2017) used short desks/partitions (1.4 m, below a 2.53 m ceiling) and found that even partial obstacles redirect airflow dramatically, but how completely blocking the wall return with a full-height wardrobe affects occupant-level comfort and uniformity remains unquantified.

**Best concept direction from report (1–2 sentences):** Asymmetric/directional blade pitch or electronically-skewed thrust vector aimed away from the furniture-blocked side (set at install time via app configuration: "wardrobe wall: north") to bias the jet's spreading-zone skew toward the open side of the room, exploiting the passive swirl-direction asymmetry effect observed by Gao et al. Alternatively, publish installation guidance recommending leaving a 100–150 mm air gap between wardrobe top and ceiling to restore a partial wall-return path — a zero-R&D marketing/documentation play with potentially large comfort benefit.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US9638209B1 (trailing-edge air dam/spoiler [UNVERIFIED]); US20060210401A1 (blade angle-of-attack optimization [UNVERIFIED]); US11111930 (asymmetric flat-bottom airfoil [UNVERIFIED]); US10302094 (pivoting blade-tip attachments for airflow redirection [UNVERIFIED]); WO2015095753A1 (interactive occupant-tracking fan [UNVERIFIED]); US7711659B2 (adaptive fan management with thermal sensing [UNVERIFIED]).

**Links to other conditions (NN list + why):** 09 (long narrow rooms + dual-fan layout); 07 (off-centre mounting + wall blockage interaction); 02 (low ceilings worsen wall-return obstruction).

---

## Summary Table

| NN | Condition | TOTAL |
|---|---|---|
| 15 | Hot-Roof Top-Floor | 28 |
| 16 | Humidity-Monsoon | 25 |
| 17 | Fan With AC | 25 |
| 18 | Exhaust-Negative-Pressure | 23 |
| 19 | Cross-Ventilation | 32 |
| 20 | Dust-Smoke-Grease | 25 |
| 21 | Tall Wardrobes | 30 |


---

## Verification log

Applied the rubric's calibration anchors (added by orchestrator) and checked TOTAL arithmetic, score justifications against the source reports, and verbatim accuracy of quoted facts/patents for all 7 cards (15–21). Changes made:

1. **Card 15 (Hot-Roof):** TOTAL 30 → 28. Arithmetic error — FREQ4+SEV4+UNSOLVED5+PATENT_ROOM4+2×AERO_FIT(2)+EVIDENCE3+PROTO4 = 28, not 30. Individual scores were already consistent with calibration anchors (AERO_FIT=2 correctly reflects a non-aero/radiant fix; EVIDENCE=3 correctly reflects analogue-only evidence); only the sum was wrong.
2. **Card 16 (Humidity-Monsoon):** TOTAL 24 → 25. Arithmetic error — FREQ4+SEV3+UNSOLVED4+PATENT_ROOM3+2×AERO_FIT(1)+EVIDENCE4+PROTO5 = 25, not 24.
3. **Card 17 (Fan With AC):** FREQ 5 → 3, justification reworded. Calibration anchor: "FREQ 5 = almost every Indian home." Report explicitly states no national prevalence dataset exists and that the condition is "rare in rural/un-electrified-AC contexts" — AC+fan pairing is common among AC-owning urban households but not close to universal nationally, so 5 was miscalibrated. Recomputing TOTAL with FREQ=3 and all other scores unchanged gives 25, which already matched the card's stated TOTAL (so only the FREQ score itself, not the arithmetic, needed correction). Also fixed a fact-quoting error: the bullet "28°C + low-downward-fan achieves ~73.7–100% acceptance, comparable to 26°C fan-off reference conditions" conflated two separate report statements (rooms at 26–28°C fan-on vs. 23°C fan-off; and 28°C+low-fan vs. 26°C reference for near-neutral sensation) into an unsupported combined claim ("26°C fan-off" does not appear in the source). Reworded to state both comparisons accurately per report §2.
4. **Card 18 (Exhaust-Negative-Pressure):** TOTAL 22 → 23. Arithmetic error — FREQ4+SEV2+UNSOLVED4+PATENT_ROOM5+2×AERO_FIT(1)+EVIDENCE2+PROTO4 = 23, not 22. PATENT_ROOM=5 was checked against the anchor ("5 only if essentially no relevant patents found") and is justified — report found only distant/non-overlapping adjacent patents and explicitly calls this a white-space niche.
5. **Card 19 (Cross-Ventilation):** TOTAL 28 → 32. Arithmetic error — FREQ4+SEV3+UNSOLVED5+PATENT_ROOM4+2×AERO_FIT(4)+EVIDENCE3+PROTO5 = 32, not 28. Checked AERO_FIT=4 strictly against the double-weighted rubric guidance (5 only if blade/airflow aerodynamics is the core fix): the report frames this condition as a textbook jet-in-crossflow problem where velocity ratio (thrust/disk loading, jet-column tightness) is the governing design lever, distinct from the control/sensing-dominated conditions 17/18/20 — 4 is justified, not inflated. The corrected TOTAL of 32 is within the batch's expected 18–36 spread and does not make the batch over-calibrated (other totals remain below 30).
6. **Card 20 (Dust-Smoke-Grease):** UNSOLVED 5 → 4, justification reworded; TOTAL 24 → 25. Calibration anchor: "UNSOLVED 5 only if the report found NO product addressing it." The report documents that Crompton and Atomberg both sell marketed "anti-dust" ceiling fan lines (§6) — a product does exist addressing the surface problem, even though independent verification of the claims is absent (§9) — so 5 was miscalibrated; corrected to 4, consistent with how Card 16's analogous "anti-rust" marketing-claim situation was scored. Recomputed TOTAL with UNSOLVED=4 and all other scores unchanged = 25.
7. **Card 21 (Tall Wardrobes):** TOTAL 27 → 30. Arithmetic error — FREQ5+SEV3+UNSOLVED5+PATENT_ROOM4+2×AERO_FIT(3)+EVIDENCE2+PROTO5 = 30, not 27. All individual scores were already consistent with the calibration anchors and were left unchanged. Also removed a stray trailing "|" artifact at the end of the first quantified-fact bullet (formatting leftover, not a factual issue).
8. **Summary Table:** Updated all seven TOTAL values to match the corrected per-card totals (15:28, 16:25, 17:25, 18:23, 19:32, 20:25, 21:30).

No quoted facts, patent numbers, or links were found to be fabricated or missing from the source reports; all [UNVERIFIED] tags were preserved correctly. No other score (FREQ/SEV/PATENT_ROOM/EVIDENCE/PROTO) beyond those listed above required correction — AERO_FIT scores across all 7 cards were re-checked strictly against the double-weighted rubric and found appropriately differentiated (1–2 for electrical/materials/pressure-topology fixes in cards 15/16/17/18/20; 3–4 for cards 19/21 where blade-geometry/airflow-shaping genuinely does more of the work).
