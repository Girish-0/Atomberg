### 08 — Multiple Ceiling Fans in One Large Room or Hall
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | Extremely common in Indian halls, classrooms, dining rooms, temples, railway stations — "virtually every Indian living-dining hall... uses 2 or more ceiling fans" (§1) |
| SEV | 3 | Documented non-uniformity without coordination (Schiavon chamber study shows high speed under fan, low speed outside); sized fans still work but suboptimally (§2) |
| UNSOLVED | 3 | CBE/HVLS guidance exists but not adapted to Indian ceiling-fan sizes/room scale; Indian retail guidance is rule-of-thumb only ("4 ft blade-tip clearance for >225 sq ft") (§6) |
| PATENT_ROOM | 4 | Only one directly relevant patent family (WO2015171729A1 "Ceiling fan control system"); search found "far fewer than the target 10–20 relevant families"; most are AHU/cooling-fan patents (§8) |
| AERO_FIT | 4 | Speed synchronization (to avoid voltage-drop mismatch on shared regulators) and S/D spacing ratio are core aerodynamic levers; multi-fan blade/airfoil matching drives cell coverage (§2, §4) |
| EVIDENCE | 3 | Schiavon et al. (2018) chamber study is rigorous (20,160 measurement points for two-fan case) but lab-scale and likely only 1–2 fan models tested; exact numeric uniformity improvement "not extracted from search snippets — [UNVERIFIED]" (§7) |
| PROTO | 4 | Can test two matched 1200 mm fans in a 3×8 m hall with handheld anemometer grid at 0.5 m spacing, three heights per ASHRAE 55; low cost, measurable (§10) |
| **TOTAL** | 29 | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Schiavon chamber study: "**20,160 points double-fan case**; single-fan speed field is non-uniform (high under fan, low outside); combined two-fan field is **not a simple sum** of single-fan fields — depends on fan-speed mismatch and distance in complex ways" (§2, eScholarship PDF)
- CBE fan-cell method: fan diameter **0.2–0.4 × room width**, spacing **≥2.5×D**, fan-cell aspect ratio **≤1.5:1** (§1, CBE Fans Guidebook)
- Indian retail guidance: two identically sized fans recommended for halls **>225 sq ft (~21 m²)** with **≥4 ft blade-tip-to-blade-tip clearance** (§1, Atomberg size guide)
- Voltage-drop loss on shared regulator: "when two fans share one switch/regulator, voltage drop along the wiring run causes the fan electrically closer to the regulator to spin faster than the farther one" (§3, DIYChatroom forum)

**Core unsolved gap (1 sentence):** Indian residential market lacks a data-driven, India-specific multi-fan layout calculator or sensor-adaptive speed synchronization that accounts for room size, ceiling height, and measured voltage drop, leaving only rule-of-thumb clearances in use.

**Best concept direction from report (1–2 sentences):** Build a CBE-inspired, India-localized app-based layout tool (1200 mm BLDC fans, 2.6–3.2 m ceilings, common room sizes) combining D/W and S/D rules with wireless speed/phase synchronization that reads RPM feedback per fan and auto-trims slower units to match faster neighbours, avoiding shared-regulator voltage-drop asymmetry.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- WO2015171729A1 — Wireless control system/method to control plurality of ceiling fans in a defined location via wireless device (direct focus on multi-fan group control)
- US10317105B2 / US20110014061A1 / US8849463B2 — Array controller for multiple fan units (industrial/AHU precedent, moderate overlap if claim is "occupant comfort/airflow uniformity" not electrical efficiency)
- US6428282B1 / US11149738 — Fan speed synchronisation control (electronics cooling fans, low overlap for residential ceiling-fan-specific sync)

**Links to other conditions (NN list + why):**
- Condition 09 (Long narrow rooms): use two fans in series along long axis instead of one, per multi-fan spacing logic
- Condition 11 (Open plan): multi-fan zoning for broken recirculation loops in open-plan LKD layouts
- Condition 03 (High ceilings): multi-fan placement affects downrod length trade-offs in large volumes

---

### 09 — Long, Narrow Rooms and Corridors (Aspect Ratio > 2)
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | Common in Indian redevelopment apartments; structural bays 2.7–3.6 m wide + elongated living-dining 6–9 m produce AR > 2 "routinely"; narrow bedrooms, corridors, galley kitchens typical (§1) |
| SEV | 3 | Dead zones at room ends documented anecdotally ("far corners stay still") but not peer-reviewed quantified; wall impingement on both short walls is physics-confirmed but magnitude unverified (§2) |
| UNSOLVED | 5 | "No commercial ceiling fan or published study specifically addresses non-uniform coverage in AR>2 rooms; the field solution (two fans) is a system-level fix, not a product-level aerodynamic innovation — a genuine, evidenced-by-absence gap" (§9) |
| PATENT_ROOM | 4 | Patent search for directional/footprint-shaping patents fell "well short of the 10–20 relevant-family target"; no on-point hits for "long/narrow room ceiling fan"; no InPASS search completed (§8) |
| AERO_FIT | 5 | Sweep diameter, multi-fan placement along long axis, blade twist/pitch bias, and downrod length are core aerodynamic levers directly addressing dead-zone coverage asymmetry (§4) |
| EVIDENCE | 1 | "No peer-reviewed quantitative study of ceiling-fan performance in long/narrow (AR>2) rooms was found in this search pass — this is a genuine literature gap, not an omission" (§2); only inferred from general wall-jet and jet-decay physics |
| PROTO | 4 | Build/rent or scale a 3×8 m test room (or 1:3 scale model) with fan at centre on short axis; measure velocity grid along long axis at three heights with anemometer (§10) |
| **TOTAL** | 31 | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Floor-jet impingement zone: ~**0.5 m radius at 2.3 m mounting height**; jet does not spread beyond blade diameter until **~0.8 m above floor** (§2, CBE Berkeley PSV studies)
- Wall-jet momentum loss: up to **~50% from friction/turbulent mixing** in a radial wall-jet geometry analogous to near-wall floor flow (§2, MDPI Energies 2021 radial wall-jet study)
- Narrow-room geometry: in a 3×8 m room with 1.2 m fan centred, wall-gap/D ≈ **0.75** on both short walls simultaneously, entering zone where wall interaction applies "on both sides simultaneously, unlike a single-wall case" (§2)
- IS 374:2019 minimum air delivery by sweep: **130 m³/min for 900 mm sweep vs 210 m³/min for 1200 mm sweep** (§4)

**Core unsolved gap (1 sentence):** No literature or product quantifies how aspect ratio AR>2 degrades effective coverage, prevents both a ceiling-fan-specific aerodynamic fix (all commercial solutions are just "use two smaller fans") and a physics-based design rule beyond rule-of-thumb clearances.

**Best concept direction from report (1–2 sentences):** Design a blade with biased/asymmetric pitch (higher pitch on the long-axis-facing arc, lower on the short-axis-facing arc) to preferentially project thrust along the room's long axis, reducing near-wall impingement severity while extending dead-zone reach, validated by CFD against a measured 3×8 m test room airflow.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- US7413410B2 — Twisted blade with graduated dihedral for wider divergence (possible prior art overlap if using similar dihedral logic; design-around via fixed asymmetric pitch rather than graduated dihedral)
- US6116856A — Bi-directional fan with asymmetric reversible blades (related asymmetry concept; differentiate via axis-biased fixed geometry rather than reversible switching)
- US10989207B2 — Centrifugal fan with directional outlet (medium overlap if using directional outlet; design-around via axial-fan-based mechanism)
- US20130309068A1 — Fan oscillating mechanism with oval cam (low overlap; addresses oscillation, not corridor-specific aerodynamics)

**Links to other conditions (NN list + why):**
- Condition 08 (Multi-fan): two-fan placement rules from Condition 08 directly apply to AR>2 long-axis distribution
- Condition 07 (Near-wall mounting): near-wall impingement physics on both short walls is Condition 07 doubled
- Condition 09 mirrors back to Condition 08 for solution strategy

---

### 10 — Small Rooms (Bathrooms, Kitchens, Study Rooms < 8 m²)
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 5 | Nearly every urban apartment and independent house has at least one bathroom, utility room, or small kitchen under 8 m²; market presence of dedicated 600/750/900 mm SKUs from Atomberg, Havells, Crompton, Orient confirms sustained demand (§1) |
| SEV | 3 | Wall-choking and re-ingestion recirculation documented by CFD (two-cell structure, low-effectiveness band) but no quantified % air-delivery or velocity loss for D/room-width > 0.4 found in this pass (§2, §7) |
| UNSOLVED | 4 | "The entire market response is 'just use a smaller fan'" to reduce D/W back toward ≤0.4; no product addresses the wall-choking/re-ingestion recirculation physics directly (§9 Gap 1) |
| PATENT_ROOM | 4 | No patents specifically targeting "oversized fan in small room" condition found; nearest are small-diameter blade aerodynamic-efficiency patents (US7665967, US6071077A, etc.) not wall-proximity-specific (§8) |
| AERO_FIT | 4 | Wall-aware tip geometry (raked, serrated, or winglet designs tuned for wall-gap/D < 0.3–0.4), reduced sweep diameter, variable/two-stage effective sweep are primary aero levers (§4 ranking, §9 Concept 1–2) |
| EVIDENCE | 2 | One CFD study (ResearchGate, enclosed-room ceiling fan) confirms two-cell recirculation but only abstract-level access (quantified figures not extracted); no IIT/IISc/CEPT residential small-room study found (§7) |
| PROTO | 5 | Test in actual bathrooms (3–5 m²), kitchens (5–8 m²), study rooms with grid anemometer at occupant heights; cheap, real-world locations readily available (§10 setup) |
| **TOTAL** | 31 | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- BEE service-value minimums by sweep: 900/1050 mm sweep **≥3.1 CMM/W minimum**; 1200 mm sweep **≥4.0 CMM/W minimum** with air delivery ≥210 m³/min (§6, Bijli Bachao BEE summary)
- Recirculation structure: CFD identifies a "**two-cell structure**: a large-scale recirculation cell between room centerline and sidewalls, plus a smaller secondary recirculation cell trapped between floor and downwash jet; a broad band between the fan's radius and the walls shows **very low, largely ineffective air speed**" (§2, ResearchGate CFD study)
- Small-sweep fan RPM: Atomberg's 600 mm BLDC fan specified at **840 RPM** vs roughly **350–380 RPM typical for 1200 mm fan** (§3, Atomberg 600mm product page)
- Atomberg 600 mm specs: **110 CMM**, **28 W**, **~3.9 CMM/W** (calculated from stated figures) (§6, Atomberg product page)

**Core unsolved gap (1 sentence):** BEE service-value ratings are measured in an open test chamber, not in small enclosed rooms with D/room-width > 0.4, leaving a certification gap between nameplate air-delivery and real in-room ventilation effectiveness for the most common residential small-room/bathroom installations.

**Best concept direction from report (1–2 sentences):** Design wall-aware tip geometry (serrated or winged tips tuned for wall-gap/D < 0.4) on 600–900 mm small-sweep fans to reduce the sharpness of the wall-climb/re-ingestion loop at the small-room scale, preserving thrust while improving real-world ventilation effectiveness; validate in a 4 m² test bathroom against CFD Boussinesq model.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- US7665967 — "Efficient traditionally appearing ceiling fan blades with aerodynamical upper surfaces" for small-diameter blades (moderate overlap; differentiate via tip/wall-interaction focus rather than upper-surface camber only)
- US6071077A — Swept fan blade (low overlap; general blade sweep patent)
- US7413410B2 / US20060210401A1 — Ceiling fan blade (low overlap; general blade geometry)
- US9995313 — Ceiling fan blade (low overlap; general blade geometry)

**Links to other conditions (NN list + why):**
- Condition 07 (Near-wall mounting): wall-proximity flow physics same as near-wall condition but on all four walls simultaneously in small rooms
- Condition 20 (Humid kitchens/bathrooms): material corrosion concerns compound with this condition in typical small-room installation locations

---

### 11 — Open-Plan, L-Shaped, and Double-Height Spaces
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 3 | Open-plan LKD (living-kitchen-dining) now standard in mid-to-premium apartments (Mumbai, Bengaluru, Pune, NCR, Hyderabad); L-shaped and double-height foyers common in duplexes/farmhouses; prevalence unquantified ("[UNVERIFIED] — no single published statistic found quantifying the %") (§1) |
| SEV | 3 | Commercial sizing guides suggest 30–40% coverage drop from same fan in enclosed room; 40–50% airflow loss at zone edges reported; but sourced from consumer guides, not independently tested ("[UNVERIFIED commercial source]") (§2) |
| UNSOLVED | 4 | "No product in the surveyed Indian or global catalogues explicitly markets a feature for open-plan, L-shaped, or double-height-void rooms" — every spec sheet addresses generic room, not geometry-aware claim (§9) |
| PATENT_ROOM | 4 | Patent search for directional/zoning patents fell short of 10–20 family target; no patents found that "squarely cover synchronised multi-fan zoning or stack-effect-aware reverse mode" (§8) |
| AERO_FIT | 4 | Multi-fan zoning (not single oversized fan), directional blade pitch for off-axis wings, and stack-effect-aware control for double-height voids are core aero levers; sweep diameter and placement primary drivers (§4) |
| EVIDENCE | 2 | Physics transfer from wall-jet/free-jet decay is "low-risk, the quantification is not yet done"; CBE Berkeley wall-jet research is sound but not specifically for open-plan ceiling-fan use; no IIT/IISc/CEPT India study found (§7, §12 insight #1) |
| PROTO | 3 | Requires building or instrumenting real open-plan rooms or two-zone test rigs with controlled missing-wall setup; more complex than single-room tests but feasible (§10) |
| **TOTAL** | 27 | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Published sizing guidance: **"effective coverage can drop 30–40%"** relative to the same fan's rated coverage in an enclosed room of equal area, in open floor plans, because there is no wall to contain/redirect the floor jet (§2, whatsizeappliance.com sizing discussion)
- Big Ass Fans guidance: "**two or more mid-size fans (52–62", positioned per functional zone) rather than one oversized fan** for open-plan rooms over ~400 sq ft (37 m²); one large 72" fan produces **40–50% less airflow** at zones away from centre, whereas zoning was reported to give roughly **70% better coverage**" (§4, Big Ass Fans/consumer-guide sourced [UNVERIFIED])
- Wall-jet physics: "wall-confluent jets have slow velocity decay and can cover almost the whole floor precisely because the wall turns and sustains them — remove the wall and the jet instead behaves closer to a free jet, whose centerline velocity decays as roughly x^(−1/3) with no wall-driven re-acceleration" (§2, ScienceDirect wall-jet and free-jet decay literature)
- Stack effect: in a double-height/stairwell void, stack effect can move air vertically whenever a top-to-bottom temperature or density difference exists; hot-weather downward stack flow can either reinforce or fight a fan's downwash depending on season/time of day (§2, Wikipedia and aeroseal.com stack-effect explainers)

**Core unsolved gap (1 sentence):** No published India-specific quantified study isolates how much velocity/comfort actually drops in real open-plan vs. enclosed rooms, and no product offers synchronised multi-fan zoning or stack-effect-aware reverse mode, leaving the 30–40% coverage-loss numbers unverified.

**Best concept direction from report (1–2 sentences):** Deploy two BLDC fans in zone-matched placement (one serving living, one serving kitchen/dining in open-plan LKD) with wireless synchronisation that uses occupancy/temperature feedback from each zone to individually trim speed — allowing the cooler zone to run slower while maintaining comfort in the hotter zone, closing a virtual "recirculation loop" between the two fans' domains; validate in real open-plan apartments.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- US10989207B2 — Low-profile centrifugal fan with directional outlet (medium overlap; design-around via axial fan with electronic (not mechanical) directional control)
- CN2145274Y — Rotating/tiltable blade assembly for 360° directable supply (medium overlap; use electronic rather than mechanical blade repositioning)
- US7726945B2 — Industrial fan blades tiltable lengthwise (low overlap; is industrial-scale specific)
- US7413410B2 — Twisted blade with graduated dihedral (medium overlap if using similar dihedral logic; differentiate via wider-spread design philosophy)

**Links to other conditions (NN list + why):**
- Condition 08 (Multi-fan): multi-fan spacing and synchronization rules apply directly to open-plan zoning strategy
- Condition 09 (Long narrow rooms): L-shaped wing coverage is similar to far-end dead-zone in AR>2 rooms
- Condition 13 (Thermal stratification): stack effect in double-height voids overlaps with buoyancy-driven mixing

---

### 12 — Semi-Open Spaces (Balconies, Verandas, Sit-Outs, Covered Terraces)
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 2 | Report's own §1 prevalence claim is qualitative/unquantified ("[UNVERIFIED]", retailer-category-page evidence only); per rubric calibration anchors, semi-open spaces (balconies/verandas/sit-outs) are an explicitly-listed niche condition (cf. balconies example), not an almost-every-home condition — scored conservatively per calibration override, not per the report's own framing (§1) |
| SEV | 4 | Ambient wind as jet-in-crossflow phenomenon is physically significant; floor-level return-air path is weakened/absent, causing breeze to "escape outward rather than recirculating" (§2); wind-induced side loads on wall-mount brackets plausible but unquantified |
| UNSOLVED | 4 | "No major Indian ceiling-fan brand in this search was found publishing an explicit IP-rated wet/damp outdoor-fan line comparable to Hunter's WeatherMax or Big Ass Fans' Haiku Outdoor"; Indian brands rely on generic "corrosion-resistant"/"rust-free" claims, not certified IPX4+ ingress protection (§6) |
| PATENT_ROOM | 4 | Google Patents search returned mostly US design patents for housing shapes and separate protective-cover utility patents; no dedicated InPASS (Indian Patent Office) search completed; housing-sealing patents lower overlap risk for built-in sealed design (§8) |
| AERO_FIT | 3 | Motor/housing sealing and IP rating rank #1 (materials/engineering), but blade aerodynamics are secondary; jet-in-crossflow physics is relevant but not yet validated at ceiling-fan scale for outdoor wind interaction (§4, §7) |
| EVIDENCE | 2 | "No peer-reviewed paper, thesis, or CFD study specifically addressing ceiling-fan performance under ambient outdoor wind / jet-in-crossflow conditions was located"; CFD studies on enclosed rooms and general jet-in-crossflow literature found, but not ceiling-fan-specific outdoor study (§7) |
| PROTO | 4 | Can test on actual balconies/verandas with anemometer grid under varying ambient wind (0.3–3 m/s), comparing enclosed baseline vs. open-wall vs. outdoor crossflow (§10) |
| **TOTAL** | 26 | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Typical semi-open space dimensions: **balconies 1.2–2.5 m deep × 2–4 m wide; verandas/sit-outs 2–4 m deep × 3–8 m long** (§1)
- IP rating standard (global): IPX2/IPX3 = damp-rated (tolerates humidity, not direct water); IPX4+ (commonly IP44) = wet-rated (tolerates direct rain/spray) (§5, Hunter Fan and Today's Fans documentation)
- Hunter WeatherMax design: sealed motor housing, corrosion-resistant finish, stainless-steel hardware, UV-stabilised composite blades specifically for rain/humidity/salt-air resistance (§5, Hunter WeatherMax collection documentation)
- Big Ass Fans Haiku Outdoor: **aircraft-grade aluminium airfoils**, claims up to **~17,300–17,500 CFM (≈490 m³/min)** at under **35 dBA** on 84" model (§5, bigassfans.com cutsheet)

**Core unsolved gap (1 sentence):** IS 374:2019 (Indian ceiling-fan standard) does not define wet/damp IP-rated test classes, and no major Indian brand publishes certified ingress-protection ratings for balcony/veranda fans, leaving only generic "corrosion-resistant" marketing language versus the proven Hunter/Big Ass Fans IP44+ approach.

**Best concept direction from report (1–2 sentences):** Engineer a sealed BLDC motor housing (IP44-equivalent for damp/covered spaces, IP54+ for wet/fully open terraces), use UV-stabilised ABS or aircraft-grade aluminium blade stock, and stainless fasteners, following the Hunter WeatherMax/Big Ass Fans Haiku Outdoor material/sealing playbook but localised to 230 V/50 Hz and 1200 mm sweep; publish third-party certification (BIS or international equivalent) to credibly differentiate from unverified "rust-free" claims.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- US5681147A — Ceiling fan motor housing assembly (medium relevance to housing design; design-around via sealed architecture with distinct sealing method)
- US20040141848A1 — Protective cover over fan blades/motor housing (low-medium relevance; is aftermarket cover, not integral sealing)
- US20110305571A1 — Ceiling fan protective cover (low relevance; removable cover concept)
- USD938572S1, USD877314S1, USD991435S1, others — US design patents for motor-housing shapes (low direct relevance; block appearance, not function; any new housing form factor with distinct ornamental design avoids)

**Links to other conditions (NN list + why):**
- Condition 16 (Humid kitchens): humidity/corrosion resistance materials apply similarly to both semi-open verandas and humid kitchens
- Condition 13 (Thermal stratification): stack effect in open verandas connected to interior rooms creates mixed thermal/convection regime
- Condition 15 (Hot-roof top-floor): exposed terraces and top-floor balconies share radiant heat load concerns

---

### 13 — Thermal Stratification (Hot Air Pooled at the Ceiling)
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 3 | Top-floor flats under RCC slabs or tin/asbestos roofs are "the dominant case" in India; overlaps heavily with Condition 15; no BEE/census statistic found on prevalence (§1) |
| SEV | 4 | Documented vertical temperature gradients ~0.7 °C/m (≈2 °C floor-to-ceiling normal) to 3.0 °C in warehouses; Indian top-floors show roof-to-room differentials of **6–8 °C [UNVERIFIED exact India-residential figures]**; stratification significantly affects comfort under ceiling (§1, §2 physics) |
| UNSOLVED | 3 | Patented dual-sensor ΔT-based destratification exists (commercial/industrial: Big Ass Fans, Panasonic Atmosphere) but "no evidence was found of any residential 1200 mm Indian ceiling fan marketing an explicit destratification mode" (§6) |
| PATENT_ROOM | 2 | US8900041B2 and family (ceiling/floor dual-temperature-sensor with PI control on ΔT) directly cover literal dual-sensor destratification logic — "High" overlap risk for any such approach; broader thermal-control patents (US10801508, US11719249) also present medium-high overlap (§8) |
| AERO_FIT | 4 | Thrust-per-watt (penetration against buoyant counter-flow), blade-to-ceiling clearance (inflow-starvation management), downrod length, pitch angle, and winglets are primary levers; governing Richardson-number physics well-understood (§4) |
| EVIDENCE | 2 | Industrial/warehouse field and CFD evidence robust (26.4% gas-savings documented); but "No IIT/IISc/CEPT-specific published study on residential ceiling-fan destratification in Indian homes was located"; all quantified figures are US/EU/warehouse scale, not Indian residential (§7, §12 insight #1) |
| PROTO | 4 | Instrument a real Indian top-floor room with RCC/tin roof in summer; measure vertical ΔT (floor-to-ceiling thermocouple string), occupant-height velocity, time-to-steady-state across multiple speed settings (§10); feasible and directly fills India-specific gap |
| **TOTAL** | 26 | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Baseline stratification: vertical temperature gradients of **~0.7 °C/m** (unmixed) can be cut to **~0.3 °C/m** (with fan), roughly **half the unmixed gradient** (§1, ResearchGate "Performance Comparison of Destratification Fans for Large Spaces")
- Warehouse destratification field data: vertical gradients up to **3.0 °C annually**; destratification measurably reduced ceiling-level temp by up to **4.0 °C (summer)** and raised floor-level temp by up to **7.0 °C (winter)** (§2, ScienceDirect warehouse studies)
- Richardson-number framework: Ri = g·ΔT·L / (T·V²) governs competition between fan momentum flux and buoyant restoring force; when Ri is large (weak jet, strong gradient) downwash loses momentum before reaching floor and "hot ceiling layer slumps back upward"; when Ri is small (strong jet, weak gradient) jet fully penetrates and mixes (§2, OSTI Richardson's number reference)
- Harvard thesis finding: "continuous, variable-speed forward-direction operation can destratify more efficiently (lower energy) than running in reverse ('leading paddle' mode)" — reverse mode is **not automatically better** and can waste energy (§2, Harvard DASH thesis)

**Core unsolved gap (1 sentence):** No Indian residential ceiling fan implements true ceiling-floor ΔT-sensing destratification control (the most evidence-backed mechanism used industrially), and all quantified destratification data come from warehouse/commercial scale, leaving India-specific performance for 1200 mm BLDC fans in typical 2.6–3.2 m rooms unvalidated.

**Best concept direction from report (1–2 sentences):** Implement a single-sensor algorithmic stratification estimator (ceiling-mounted ambient sensor + motor current-draw/torque proxy for load changes) feeding a PI control loop that ramps fan speed proportionally to an inferred ΔT, avoiding the literal dual-sensor design-around risk of US8900041B2; pair with continuous low-speed forward operation (not seasonal reverse mode) shown more efficient in Harvard residential study.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- US8900041B2 / CA2717398A1 — Ceiling/floor dual-temperature-sensor controller with Winter/Summer modes; PI control on ΔT targeting ΔT→0 (**High overlap risk** for literal dual-sensor approach; design-around via single-sensor + model-based ΔT estimate or IMU current-draw proxies)
- US6189799B1 / US5996898A / US6415984B1 — Occupancy + temperature control family (Medium overlap if combining occupancy with temperature, but this is on/off control, not stratification-specific ΔT mechanism)
- US10801508 / US11719249 — Integrated thermal comfort control system with variable mode of operation (**Medium-High overlap** if claims are broad; differentiate via narrower aerodynamic innovation rather than control-logic alone)

**Links to other conditions (NN list + why):**
- Condition 15 (Hot-roof top-floor): radiant heat from 60–70 °C RCC slab is separate from air-stratification problem; fan mixing cannot solve radiant load alone
- Condition 14 (Sunlit wall): both create vertical/lateral temperature asymmetry; stratification is vertical, sunlit wall is horizontal
- Condition 11 (Open-plan): stack effect in double-height voids compounds stratification in mixed convection regime

---

### 14 — Sunlit Wall or Window (Uneven Solar Heating)
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | One-sided window/wall very common: "most urban apartments and independent houses in India have only one or two external walls with windows... so solar exposure is inherently one-sided"; no direct survey found but qualitatively extremely common (§1) |
| SEV | 3 | Asymmetric thermal plume expected from jet-in-crossflow physics but "not yet quantified in literature for this specific geometry"; comfort impact inferred (buoyant plume vs. symmetric downwash) but unverified at occupant height (§2, §9) |
| UNSOLVED | 5 | "No fan on the market senses or compensates for a laterally asymmetric solar thermal plume"; all commercial "smart" fans sense only bulk/average room temperature and/or occupancy, not spatial/directional gradients (§9) |
| PATENT_ROOM | 4 | Patents found address adjacent mechanisms (directional/reversible blades, occupancy+temperature sensing) but none explicitly claims detection of or compensation for "laterally asymmetric solar-driven thermal plume"; no InPASS search completed (§8) |
| AERO_FIT | 4 | Multi-point/IR-array sensing + differential blade pitch or dual-fan bias (Concept 1), asymmetric/bi-modal blade pitch (Concept 5), and software-only oscillating "natural breeze" modes (Concept 2) are primary aero/control levers (§9) |
| EVIDENCE | 1 | "Direct academic study of 'ceiling fan + sunlit wall / asymmetric solar heating': none found in this search pass"; only adjacent window-glass mixed-convection CFD and general buoyant-plume/jet-in-crossflow theory available, not ceiling-fan-specific (§7, §12 insight #1) |
| PROTO | 4 | Test in typical sun-exposed bedroom (3×3.5 m, 2.75 m ceiling) with one wall/window in direct sun; measure thermal asymmetry (hot-side vs. cool-side temp/velocity grid) across 2–3 heights and times of day (§10); low cost, real-world locations |
| **TOTAL** | 29 | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Clear glazing solar heat gain: SHGC (Solar Heat Gain Coefficient) for clear single glazing ≈ **0.82**, i.e. **~82% of incident solar radiation enters as heat**; on a sun-facing wall, solar gain "can swamp other heat transfer mechanisms" (§1, Studiomatrx — Thermal Performance of Windows guide)
- Elevated-air-speed comfort offset (CBE Berkeley): at higher ambient/operative temperatures, elevated air movement significantly improves comfort votes (p<0.001); preferred air speeds often exceeded **0.8 m/s "no personal control" limit**, with speeds up to **1.05 m/s maintaining comfort at 28–29.5 °C/50% RH** (§3, CBE Berkeley comfort studies cited via eScholarship)
- ASHRAE 55 acceptable operative temperature without air movement: **~26 °C/60–80% RH or 28 °C/60% RH**, but *with* air movement more than 80% of subjects found **28–30 °C acceptable** (§3, CBE Berkeley research)
- Jet-in-crossflow governing parameter: jet deflection and vortex structures controlled by **velocity/momentum ratio between the jet and opposing buoyant plume flow** (§2, ResearchGate "The jet in crossflow" and "elevated round jets deflected in a crosswind" studies)

**Core unsolved gap (1 sentence):** No published India-specific measurement quantifies how much air-speed or comfort asymmetry a ceiling fan creates when facing a one-sided solar thermal plume, and no product senses or compensates for this lateral asymmetry beyond bulk-room-temperature logic.

**Best concept direction from report (1–2 sentences):** Pair a low-cost multi-point thermistor or single off-axis IR sensor (mounted at canopy edge facing presumed hot wall, installer-selectable at setup) with simple two-zone firmware logic that increases fan speed when ΔT (directional − reference) exceeds a threshold, biasing airflow toward the hot side without the full spatial-sensing complexity or patent overlap of multi-array solutions; validate with real-room thermal-asymmetry baseline test (Section 10) before production.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- US6116856A — Bi-directional fan with asymmetric reversible blades (low-medium relevance; differentiate via fixed radial bias rather than reversible flip for thermal compensation)
- US6415984B1 / US5996898A / US6189799B1 — Automatic occupancy + temperature control family (Medium overlap if combining occupancy with temperature; design-around via differential multi-point sensing rather than single bulk-temp logic)
- US8721305B2 — Ceiling fan with variable blade pitch and variable speed control (low-medium overlap; use variable pitch per-blade-position rather than global adjustment)
- US10379208 / US10823831 / US11906611 / US12158514 — Modern adaptive-control fan family (medium overlap; avoid claim overlap by using single scalar sensor input or explicitly claim multi-zone spatial sensing as novel element)

**Links to other conditions (NN list + why):**
- Condition 13 (Thermal stratification): both create asymmetric temperature fields (vertical vs. lateral); may co-exist in top-floor sun-exposed rooms
- Condition 15 (Hot-roof top-floor): radiant heat from 60–70 °C ceiling is separate from solar-window plume but compounding in corner cases
- Condition 03 (High ceilings): tall rooms amplify the jet-plume interaction distance along the descending downwash path

---

| Report | FREQ | SEV | UNSOLVED | PATENT_ROOM | AERO_FIT | EVIDENCE | PROTO | TOTAL |
|--------|------|-----|----------|-------------|----------|----------|-------|-------|
| 08 | 4 | 3 | 3 | 4 | 4 | 3 | 4 | **29** |
| 09 | 4 | 3 | 5 | 4 | 5 | 1 | 4 | **31** |
| 10 | 5 | 3 | 4 | 4 | 4 | 2 | 5 | **31** |
| 11 | 3 | 3 | 4 | 4 | 4 | 2 | 3 | **27** |
| 12 | 2 | 4 | 4 | 4 | 3 | 2 | 4 | **26** |
| 13 | 3 | 4 | 3 | 2 | 4 | 2 | 4 | **26** |
| 14 | 4 | 3 | 5 | 4 | 4 | 1 | 4 | **29** |

## Verification log

1. **Card 09 — "Top quantified facts" bullet 4**: old → "Field practice: Indian retail guidance recommends two 1200 mm fans instead of one oversized fan for long rectangular halls; single 1400 mm fan leaves 'corners stagnant' (§2, Atomberg size guide)" → new → "IS 374:2019 minimum air delivery by sweep: 130 m³/min for 900 mm sweep vs 210 m³/min for 1200 mm sweep (§4)". Reason: that quote (including the "Atomberg size guide" citation) does not appear anywhere in 09-long-narrow-room.md — it is the near-verbatim text from 08-multi-fan.md §1, misattributed to report 09. Replaced with a real quantified fact that is actually in report 09 §4.
2. **Card 12 — FREQ score**: old → 4 → new → 2 (TOTAL recomputed, see #4). Reason: rubric's calibration anchors explicitly list balconies as a niche example requiring FREQ 1–2 ("Niche (sloped ceilings, balconies, chandeliers) = 1–2"). Condition 12 is specifically balconies/verandas/sit-outs/covered terraces, so the anchor applies directly regardless of report 12's own (unquantified, [UNVERIFIED]) claim of high prevalence. Calibration anchors are instructed to override individual-report framing for cross-batch comparability.
3. **Card 12 — "Top quantified facts" bullet 1**: old → "Solar heating of Indian roof: in Delhi summer (ambient ~42 °C, solar radiation ~900 W/m²), an untreated RCC roof slab surface reaches 65–70 °C; ceiling (slab underside) runs 4–7 °C cooler than roof surface; overall roof-to-room differentials of 6–8 °C common on hot top floors [UNVERIFIED precision] (§1, Sterling Technotrade and Houzz India sources)" → new → "Typical semi-open space dimensions: balconies 1.2–2.5 m deep × 2–4 m wide; verandas/sit-outs 2–4 m deep × 3–8 m long (§1)". Reason: the Delhi-roof-temperature figure and its Sterling Technotrade/Houzz India citations appear only in 13-thermal-stratification.md §1, not anywhere in 12-semi-open-balcony.md — a fabricated/cross-contaminated fact attributed to the wrong report. Replaced with an actual quantified fact from report 12 §1.
4. **Card 12 — TOTAL**: old → 28 → new → 26. Reason: recomputed as FREQ(2)+SEV(4)+UNSOLVED(4)+PATENT_ROOM(4)+2×AERO_FIT(3=6)+EVIDENCE(2)+PROTO(4) = 26, following the FREQ correction in #2 (original 28 was arithmetically correct for the old FREQ=4 but is now stale).
5. **Card 13 — "Top quantified facts" bullet 1 citation**: old → "(§1, Purdue e-Pubs IHPBC / ResearchGate Performance Comparison study)" → new → "(§1, ResearchGate \"Performance Comparison of Destratification Fans for Large Spaces\")". Reason: in 13-thermal-stratification.md §1, the 0.7→0.3 °C/m figure is sourced only to the ResearchGate "Performance Comparison..." study; the Purdue e-Pubs IHPBC source in the same section supports a separate, different figure (3.0 °C/yr warehouse gradient, 8.5 °F max daily gradient). The two sources had been incorrectly merged onto one fact.
6. **Summary table — row 12**: FREQ column old → 4 → new → 2; TOTAL column old → 28 → new → 26, to match the corrected card.
7. **Summary table — "NN" sum-of-totals row removed** (previously: `| **NN** | **27** | **23** | **28** | **26** | **28** | **16** | **28** | **204** |`). Reason: per rubric instruction, a column-sum-of-independent-condition-scores row is meaningless (scores are not additive across unrelated conditions) and must be removed.

All other scores, justifications, patent numbers, links, and "core unsolved gap"/"best concept direction" text in cards 08, 09, 10, 11, 13, 14 were checked against their source reports and TOTAL arithmetic recomputed — no further discrepancies found. Card 08's TOTAL (29), 09's (31), 10's (31), 11's (27), 13's (26), 14's (29) were all independently recomputed from their component scores and confirmed correct as originally written.
