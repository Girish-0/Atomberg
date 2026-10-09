### 22 — Bed, Dining Table or Desk Directly Under the Fan (Ground/Surface Effect)
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | Arguably the single most common ceiling-fan use case in Indian homes — fan over bed/table is near-universal per room layout constraints (§1), though no national survey quantifying "% of fans with furniture directly below" was found |
| SEV | 4 | Jet impingement plane moves from floor to furniture-top surface where occupant sits; floor-impingement speed ≈ 50% of peak jet speed at 0.3 m above impingement plane (CBE study, §2), with elevated turbulence intensity in stagnation zone |
| UNSOLVED | 4 | No product found that senses the furniture geometry and adapts blade pitch/speed/airflow direction; existing "Sleep mode" products adapt speed over time or occupancy, not the aerodynamic profile to compensate for shortened, impinging jet (§9) |
| PATENT_ROOM | 3 | Patent search yielded only handful of on-point families (US20140322002A1 "Sleepfan", US6415984/US6189799 occupancy-control, twisted-blade low-RPM patents [UNVERIFIED number]); incomplete pass (10–20 target families not reached, InPASS/Espacenet not searched) (§8) |
| AERO_FIT | 5 | Blade pitch angle, sweep diameter, blade count, and downrod length are ranked by expected relevance to short-throw impinging-jet-onto-a-person scenario; flat, more axial exit profile reduces peak core velocity (§4); core fix is aerodynamic geometry, not just speed control |
| EVIDENCE | 3 | CBE desk/partition study directly measures jet impingement, floor jet narrowing, and high-shear wall-jet formation; desk/office geometry analogous to bed but different room scale (§7); no India-specific bed-impingement quantification located |
| PROTO | 4 | Replicate CBE desk-study method at bed/table scale: mount fan at Indian ceiling height, place bed/table directly beneath, grid-map air speed/turbulence intensity at 0.1 m intervals, smoke visualization of impingement/wall-jet pattern (§10) |
| **TOTAL** | **32** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Jet stays within blade-tip width until <0.6 m from the impingement surface; speed at 0.3 m above floor ≈ 50% of jet peak (CBE study, §2)
- Ground-effect thrust change up to ~26% versus open space in UAV ducted-fan analogues at small clearances [UNVERIFIED for this specific application] (MDPI Drones, §2)
- A table in the jet path deflects flow over its edges "quite equally," shifting the impingement plane up to desk height (CBE study via ResearchGate, §2)
- Big Ass Fans SenseMe uses temperature, humidity, and PIR motion sensing to infer in-bed/asleep state and automatically steps fan speed down (company blog, §3)

**Core unsolved gap (1 sentence):** No product adapts its aerodynamic profile (blade geometry, jet shape) to the surface-impingement condition; all current "Sleep mode" solutions work by reducing speed alone, leaving turbulence-intensity-driven draft complaints unaddressed.

**Best concept direction from report (1–2 sentences):** Surface-proximity-adaptive blade pitch/twist profile — a blade designed to flatten/widen the exit velocity profile when a close reflective surface (bed/table) is detected via simple ultrasonic/IR distance sensor at hub, trading peak velocity for uniformity to cut draft/gustiness at furniture height (Concept 1, §9).

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- US20140322002A1 ("Sleepfan") — larger inlet area lowers flow speed for sleep use [UNVERIFIED — not extracted]
- US6415984 / US6189799 — Automatic occupancy and temperature control for ceiling fan operation [UNVERIFIED]
- Twisted-blade low-RPM patents [UNVERIFIED — patent number not independently confirmed] — twisted blade claimed to increase airflow at low RPM
- Big Ass Fans "patented silent motor" [UNVERIFIED — claim text not retrieved, only referenced via company blog]

**Links to other conditions (NN list + why):**
- **Condition 27 (Low-speed sleep):** overlapping user scenario (bed occupancy at night); low-speed aerodynamic optimization applies here too
- **Condition 21 (Furniture/obstructions in room):** similar bluff-body obstruction logic to tall wardrobes blocking recirculation
- **Condition 13 (Stratification):** furnishing surfaces create thermal plume interactions analogous to buoyancy vs momentum competition

---

### 23 — Mosquito Nets, Canopies and Partitions: Ceiling-Fan Aerodynamics

| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 3 | Mosquito nets described as "the single most widely practised" vector-control measure in tropical/sub-tropical households [UNVERIFIED for India-specific %]; seasonal/regional prevalence varies; no BIS/BEE statistic quantifying net-usage rate under ceiling fans located (§1) |
| SEV | 5 | One Indian study reports air velocity inside net dropping from ~0.93 m/s to effectively ~0 m/s with net in place (abstract-level, full text not accessible); this falls below ASHRAE 55's 0.2 m/s threshold for elevated-air-speed comfort benefit, effectively nullifying the fan's purpose (§2) |
| UNSOLVED | 5 | No mainstream Indian or global ceiling-fan brand offers a mode, sensor response, or geometry change specifically for net/canopy/partition use (§6); only related precedent is non-commercial Ghanaian malaria-prevention research concept (in-net auxiliary fan), never integrated with ceiling-fan control (§3) |
| PATENT_ROOM | 4 | Only ~6 directly relevant families found (short of 10–20 target), all Chinese utility models (unexamined, low presumption of validity) plus one pre-modern US patent; no patent claims a ceiling-fan speed/mode control responding to sensed net/screen condition (§8) |
| AERO_FIT | 3 | Core physics is porous-screen pressure-drop problem, not ceiling-fan aerodynamics per se (§2); screen's loss coefficient dominates at low velocities fans produce; auxiliary in-net airflow device bypasses rather than over-powers the screen (§3, §9) |
| EVIDENCE | 2 | One key Indian study (abstract-only, full text blocked 403 error); greenhouse insect-screen literature provides quantitative analogue (discharge coefficients 0.151–0.325, porosity-dependent); no quantified Indian bed-net porosity/mesh data or BIS standard (§7) |
| PROTO | 4 | Bench-measure 2–3 Indian bed-net samples' ΔP-vs-velocity curve, fit Darcy–Forchheimer porous model; then grid-measure in-net velocity across fan speeds using hot-wire anemometer at 4–6 probe points inside net at lying and seated heights (§10) |
| **TOTAL** | **29** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- In-net velocity ≈ 0 m/s vs ≈ 0.93 m/s without net (Indian study abstract, ResearchGate 369561105, §2)
- Fine insect-proof screen reduced inflow velocity by ~75% at reference wind speed of 1 m/s [UNVERIFIED for bed-net mesh specifically] (ResearchGate greenhouse-screen study, §2)
- Discharge coefficient for insect screens ranged from 0.151–0.325 for porosities of 26–36% at approach velocity of 0.25 m/s (ResearchGate, §2)
- Net imposes near-total velocity sink at the boundary; screen loss coefficient is highest at low approach velocities typical of fan-driven flow (~0.5–2 m/s, per non-dimensional screen-Reynolds-number framing) [UNVERIFIED — inference, needs direct test] due to viscous-dominated Forchheimer regime (§2)

**Core unsolved gap (1 sentence):** No ceiling fan — Indian or global — has a net-aware feature (adaptive speed, geometry, or auxiliary airflow), and the physics show simply increasing RPM has diminishing returns against screen pressure loss scaling with velocity squared.

**Best concept direction from report (1–2 sentences):** Low-power auxiliary "spot" air mover integrated into the net frame/pole, powered off the room's fan circuit or USB, replacing the Ghana solar-prototype concept with a mains/low-voltage Indian version — this bypass mechanism is the only precedent with supporting evidence (Concept 2, §9).

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- CN205231302U — Ceiling fan mounted inside a mosquito net with dockable power cord [UNVERIFIED — claim text not independently verified]
- CN202234224U — Mosquito net with a fan centered at the top [UNVERIFIED]
- CN2127440Y — "Breeze" ceiling-fan hanger for use inside mosquito net [UNVERIFIED]
- CN203362580U — "Mosquito-repellent ceiling fan" [UNVERIFIED — appears to combine mosquito repellent dispersal with fan]

**Links to other conditions (NN list + why):**
- **Condition 24 (Soft furnishings):** both involve porous/absorptive obstructions altering jet development; net is extreme case (near-total blockage) vs curtain/carpet (partial friction/absorption)
- **Condition 22 (Furniture under fan):** net-canopy placement over bed creates similar shortened-throw, impingement-like scenario

---

### 24 — Soft Furnishings vs Hard Surfaces (Carpets, Curtains, Sofas vs Tile/Marble/Concrete)

| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 3 | Vitrified tile described as dominant flooring, carpet as minority choice (bedrooms, high-end homes) in Indian homes [UNVERIFIED for precise share]; cotton/polyester curtains near-universal in bedrooms/living rooms, heavy drapes less common except upscale (§1) |
| SEV | 2 | Floor jet momentum dissipates faster over carpet; room reverberation time (RT60) differs by seconds between bare-hard (~2–4 s) and furnished rooms (~0.8 s target) (general building-acoustics data, §7); but no fan-specific quantified % drop in air delivery or occupant-level velocity was found (§2) |
| UNSOLVED | 4 | No manufacturer markets ceiling fan feature explicitly addressing "carpet vs hard floor" or furnishing interaction (§6); floor-jet characterisation work located (CBE) was done only over conventional hard flooring — no carpeted/furnished variant exists in literature (§7) |
| PATENT_ROOM | 5 | No patents specifically addressing "ceiling fan + soft furnishings/carpet/curtain interaction" were found; only general blade-noise-reduction patents (riblets, serrations, winglets, splitter blades, active cancellation) found as indirect precedent (§8) |
| AERO_FIT | 2 | Carpet presents rougher, more compliant surface; expected higher skin friction and faster boundary-layer decay, but no dedicated study of furnishing-induced blockage under a ceiling fan was located; acoustic (room reverberation) effects dominant, not primary blade-geometry leverage |
| EVIDENCE | 2 | CBE Berkeley's floor-jet characterisation (jet narrows until ~0.6 m, then spreads; speed at 0.3 m ≈ half of core) is a hard-floor baseline only; general building-acoustics NRC/RT60 data (carpet ~0.55, concrete ~0.02) provided but not measured with operating ceiling fan as source [UNVERIFIED extrapolation] (§7) |
| PROTO | 4 | Real-room test, same fan at same RPM settings, cycling through (a) bare hard floor + bare walls, (b) area rug/carpet added, (c) rug + sofa/bed under part of floor-jet, (d) sheer curtains near window (§10) |
| **TOTAL** | **24** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Floor-jet speed at 0.3 m above a hard floor ≈ roughly half the jet core speed; jet stays within blade-tip diameter until <0.6 m from floor (CBE study, §2)
- Hard surfaces (concrete NRC ≈ 0.02) vs carpet+pad (NRC ≈ 0.55) vs heavy curtain (NRC ≈ 0.50) — enormous absorption difference (building-acoustics data, §7)
- RT60 in all-hard residential rooms can be 2–4 s vs comfortable conversational target of <0.8 s (Carpet Institute Australia, Mass Loaded Vinyl Direct, §7)
- No quantified % drop in air delivery, coverage area or velocity-at-occupant-height specific to carpet vs hard floor was found in any fan-aerodynamics source searched [UNVERIFIED — likely unstudied] (§2)

**Core unsolved gap (1 sentence):** No fan-specific quantified study exists isolating how carpet, rugs, sofas, or curtains change floor-jet reach, recirculation strength, or occupant-level air speed — this is the single biggest evidence gap.

**Best concept direction from report (1–2 sentences):** Adaptive floor-jet width control (variable blade pitch or dual-zone blades) that widens the jet footprint in rooms with absorptive/furnished floors to compensate for faster momentum decay — quantified benefit unknown, needs CFD/lab test (Concept 1, §9).

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- US7494325B2 — Ridged blade surface reduces fan noise output [UNVERIFIED assignee]
- US20060110257A1 — Dimpled blade surface alters deflection angle, raising speed & lowering noise [UNVERIFIED]
- US20070154314A1 — Splitter blades between primary blades reduce tonal blade-pass noise [UNVERIFIED]
- US20050147496A1 — Roughened/serrated trailing edge minimises tonal acoustic emission [UNVERIFIED]
- US5448645A — Active fan-blade noise cancellation [UNVERIFIED] — conceptually closest to compensating for reverberant room
- US12180976 — Ceiling fan airflow diffuser apparatus [UNVERIFIED] — diffuser could be tuned to compensate for absorptive floors

**Links to other conditions (NN list + why):**
- **Condition 22 (Furniture under fan):** overlapping scenario where furniture (sofas, beds) blocks radial floor jet in same room
- **Condition 23 (Mosquito nets):** both involve porous/absorptive obstructions altering jet, though nets are more extreme case

---

### 25 — High Occupancy (Classrooms, Offices, Prayer Halls, Gatherings)

| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | Naturally ventilated classrooms without AC are the overwhelming majority of Indian government and most private schools; ceiling fans near-universal there (§1); no quantified national count of naturally-ventilated classrooms or prayer halls, but prevalence is implicit across institutional scale |
| SEV | 4 | Measured seat-to-seat air-speed non-uniformity documented in Indian university classrooms: air speed at seats directly under a fan can be 2–4× that of seats between fans or near walls/corners in same classroom (ScienceDirect, §2); noise-comfort-productivity trade-off found (productivity peaked at lower noise/temperature than comfort max, §3) |
| UNSOLVED | 5 | No residential/light-commercial Indian ceiling-fan brand was found marketing a product explicitly tuned for classrooms, prayer halls, or dense-seating halls (uniform multi-seat coverage, noise-vs-speech-intelligibility tuning, or multi-fan synchronization) — this absence is itself evidence (§6, §9) |
| PATENT_ROOM | 4 | Only 2 patents surfaced (US6,189,799 occupancy control, US9,719,525 "Medallion fan"); thin result short of 10–20 target; dedicated patent-landscape pass on multi-fan synchronized control, occupancy/CO₂-sensor-driven fan speed, and crowd-density adaptive HVAC/fan not completed (§8) |
| AERO_FIT | 4 | Occupant bodies act as bluff-body obstructions raising effective "floor" from 0 m to ~0.4–1.2 m (chair/seated/standing height), shortening usable jet throw; lower-speed torque efficiency and low-noise blade design (Rank 1, §4); wider, more uniform floor-footprint reduces row-to-row inequity (Rank 2) |
| EVIDENCE | 4 | Strong peer-reviewed Indian field studies: (a) thermal comfort in naturally ventilated classrooms (ScienceDirect, §7), (b) thermal + acoustic comfort & productivity in university classrooms, 828 student samples (ScienceDirect, §7), (c) non-uniform fan-induced air documented in Indian lecture halls (ScienceDirect, §7); CBE Berkeley elevated-air-speed database >35,000 occupant responses (§3, §7) |
| PROTO | 4 | Real-room test with 30+ seated subjects or heated manikins/space heaters at ~70–100 W each; grid of anemometers at seated head height (~1.1 m) and standing/floor-seated height (~0.3–0.6 m); smoke/fog visualization around thermal manikin at varying speeds to observe plume-vs-downwash interaction (§10) |
| **TOTAL** | **33** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Air speed at seats directly under fan can be 2–4× that of seats between fans or near walls/corners in same classroom (ScienceDirect non-uniform fan-induced air, §2)
- Comfort up to 33.8 °C at 1.2 m/s air velocity; 80% acceptable 23.4–29.7 °C operative temperature (Indian field study, composite climate, §3, §7)
- 59.9 dBA accepted at 28.8 °C, with productivity peaking around 27.8–29.8 °C operative temperature at ~56 dBA (Indian lecture-hall study, 11 naturally-ventilated halls, 828 student samples, §2, §3)
- Occupants generally prefer more air movement than codes/providers assume; >80% acceptability with air movement at multiple T/RH conditions (CBE Berkeley >35,000 occupant responses, §3)

**Core unsolved gap (1 sentence):** No product targets row-to-row uniformity in multi-seat rooms, and the noise-vs-airflow trade-off is not tuned for speech-critical rooms where productivity actually peaks at lower noise levels than the comfort temperature maximum.

**Best concept direction from report (1–2 sentences):** Uniformity-tuned blade/airfoil for broad, flat velocity profile — redesign twist/chord distribution to spread the core jet rather than concentrate it, reducing under-fan vs between-fan speed ratio; expected benefit is more even seat-to-seat comfort (Concept 1, §9).

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- US6,189,799 — Automatic occupancy and temperature control for ceiling fan operation [UNVERIFIED]
- US9,719,525 — "Medallion fan" [UNVERIFIED] — decorative/structural fan patent, low direct relevance

**Links to other conditions (NN list + why):**
- **Condition 27 (Low-speed sleep):** overlapping concern with low-speed operation and cogging-torque noise in occupied spaces
- **Condition 08 (Multi-fan interaction):** overlapping concept of fan-to-fan recirculation and dead-zone formation in large rooms with multiple units
- **Condition 22 (Furniture under fan):** similar "elevated occupant floor" effect to short-throw ground-effect logic

---

### 26 — Voltage Fluctuation, Low Voltage and Inverter/Solar Backup

| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 3 | Voltage instability described as "a daily reality" in semi-urban and rural distribution networks [UNVERIFIED — no CEA/DISCOM dataset quantifying % of Indian households facing sub-180 V conditions regularly was retrieved]; off-grid and weak-grid rural households show markedly different electricity-consumption patterns (ScienceDirect, §1) |
| SEV | 2 | Induction motor torque falls with V²; 10% undervoltage produces ~19% torque loss, fan can stall/hum (§2); no peer-reviewed or BIS lab dataset specifically quantifying m³/min loss vs supply voltage for Indian ceiling fans was found [UNVERIFIED] (§2) |
| UNSOLVED | 4 | No independent, India-specific, quantified test data exists comparing actual air-delivery/RPM stability of induction vs BLDC across real 160–270 V field distribution; marketing claims of "90–300 V" unverified in this research pass (§9) |
| PATENT_ROOM | 3 | 7 patent families found (short of 10–20 target): IN374068 (Superfan wall-regulator compatibility), IITB BLDC wall-regulator [UNVERIFIED], US7,557,526B2, WO2009090662A2, DE102016224448A1, US20140265963A1, US6392372B1; InPASS/Espacenet pass not completed (§8) |
| AERO_FIT | 1 | This condition is fundamentally an electronics/motor-control problem, not a blade-aerodynamics problem; BLDC controller with regulated DC bus decouples blade RPM from line-voltage swings; blade-lever work (sweep, chord, twist) is largely orthogonal to this brief (§9, §12) |
| EVIDENCE | 2 | TI Technical Article "Designing an Energy-efficient BLDC Ceiling Fan Solution" and TIDA-00386 reference design (90–265 Vac, 24 Vdc ±1% regulation, >85% efficiency) is the single most concrete quantified primary-source document found; rest is generic motor knowledge, not ceiling-fan-specific aerodynamics (§7) |
| PROTO | 5 | Single ceiling fan on adjustable AC supply (variac, 140–270 V at 50 Hz) plus modified-sine and pure-sine inverter runs; anemometer grid, true-RMS power meter, sound level meter, tachometer; step voltage in ~10 V increments, log RPM, CMM, power, THD, dB(A) at each point (§10) |
| **TOTAL** | **21** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- BLDC fan's driver regulates internal DC bus (commonly ~24 V in commercial reference designs) independent of line voltage, so motor speed and blade RPM/airflow stay essentially constant across rated AC input window (§2)
- TI TIDA-00386 reference design: 90–265 Vac universal input, 24 Vdc regulated bus at ±1% regulation across full input range, >85% efficiency at all load/line conditions (TI tool page, user guide, §7)
- Induction motor torque T ∝ V²; a 10% undervoltage produces roughly 19% torque loss while speed drops only ~1.5% (§2)
- Modified-sine-wave inverter carries high total harmonic distortion — commonly cited as THD > 15%, versus grid/utility target of <3% (Edecoa, epanorama.net, §2)

**Core unsolved gap (1 sentence):** No India-specific bench dataset quantifying real-world air-delivery stability of induction vs BLDC fans across the actual 160–270 V field distribution exists — this is the single biggest evidence gap and the clearest low-cost opportunity for hackathon team testing.

**Best concept direction from report (1–2 sentences):** Dual-input (AC/DC) power stage — single power board accepts both 230 V AC and 12–48 V DC bus, auto-detects source; eliminates inverter conversion loss for solar users [benefit % UNVERIFIED]; requires patent-landscape confirmation and feasibility read on dual-input topology cost (Concept 1, §9).

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- IN374068 (Superfan) — Wall-mounted regulator translated into BLDC control signals; "Speed control system for BLDC Motor based fan using wall mounted regulator" [UNVERIFIED — exact priority date not confirmed]
- IITB patent [UNVERIFIED — number not retrieved] — Wall-mounted speed regulator for BLDC; AC-DC converter → DC controller w/ speed knob → DC-AC converter inside motor
- US7,557,526B2 — Brushless motor control circuit assembly; "booster and compensation circuit" for voltage compensation [UNVERIFIED assignee, legal status]
- WO2009090662A2 / A3 — BLDC motor driven ceiling fan with passive PFC circuit [UNVERIFIED assignee]
- DE102016224448A1 — BLDC ceiling fan rated across broad voltage band (~85–600 V) [UNVERIFIED assignee, claim detail]

**Links to other conditions (NN list + why):**
- **Condition 27 (Low-speed sleep):** BLDC's superior voltage-regulation performance is especially beneficial at low-speed operation where induction motors lose torque margin severely
- **Condition 28 (Wobble):** voltage sag may induce torque ripple that excites vibration, coupling to mechanical imbalance effects

---

### 27 — Low-Speed Operation and Sleep/Night Comfort

| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | Indian households overwhelmingly run fans at reduced speed at night — anecdotal/market common-knowledge; no nationwide usage-pattern survey with low-speed-hours statistics found [UNVERIFIED] (§1); most brands market dedicated "sleep mode" that auto-decrements speed (Atomberg, Havells) (§1) |
| SEV | 4 | Blade-chord Reynolds number drops into low-Re transitional regime at 1–2 speed setting (~7.5 m/s tip speed vs ~19 m/s at full speed); airfoil lift-to-drag ratio degrades sharply (laminar separation, earlier stall onset) (§2); service value (m³/min/W) generally worse at low speed than BEE-rated max-speed value [UNVERIFIED — no low-speed service-value dataset found] (§2) |
| UNSOLVED | 5 | BEE/IS 374:2019 testing only mandates measurement at maximum speed — low-speed performance is not part of mandatory test, so no public low-speed service-value data exists [UNVERIFIED — no low-speed test clause located] (§1); nearly all Indian household blades are optimized around mid-to-high speed, not low-RPM band (§9) |
| PATENT_ROOM | 2 | Multiple US patent families: US6,039,541 + family (6,659,721, 7,210,910, 6,884,034, 7,396,212, 7,927,071) covering blade twist/camber/taper for 50–200 RPM band; US9,103,346B1 pulsed/natural-breeze control; US10,883,509 smart sensor-driven control — high overlap risk (§8) |
| AERO_FIT | 5 | Twist distribution (root-to-tip pitch schedule) is Rank 1 lever (patented low-RPM blades use large root twist ≈25–40° vs generic single compromise angle); airfoil camber/thickness distribution ranked 2; blade chord taper ranked 3 (§4); core fix is blade-geometry aerodynamics, not speed-only control |
| EVIDENCE | 3 | Dedicated low-speed blade designs show ~10% airflow gain at high speed, up to ~26% gain at low speed (US patent literature, vendor-reported [UNVERIFIED independent replication], §2); CFD study shows medium-speed operation, not minimum, gives most spatially uniform floor-level air velocity [UNVERIFIED generalization] (ScienceDirect, §2); one IEEE study reports 7.1 dB noise reduction from motor cogging-torque design (§3, §7) |
| PROTO | 4 | Hot-wire anemometer grid at 0.1 m, 0.3–0.6 m (lying/bed), 1.1 m (seated) heights covering 0.5D-spaced grid; dB(A) with octave-band capability at speed 1–2; power meter (true RMS); thermocouples for local DR calculation per ISO 7730 (§10) |
| **TOTAL** | **32** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Ordinary ceiling-fan blade needs ~270 RPM to deliver same airflow that low-RPM-optimized blade delivers at ~140 RPM; measured improvements: ~10% airflow gain at high speed, up to ~26% gain at low speed (US patent literature, §2)
- At low RPM (120 RPM), tip speed drops to ≈7.5 m/s and chord Reynolds number falls toward ~10⁴ or below (low-Re/transitional regime where airfoil lift-to-drag ratio degrades sharply) vs full speed (~300 RPM, chord Re order 10⁴–10⁵) (§2)
- BLDC motor cogging-torque noise reduction: stator-tooth shaping and magnet skewing reduced noise by 7.1 dB in published study (IEEE, §3)
- Medium-speed operation, not maximum or minimum, gives most spatially uniform floor-level air velocity distribution (~0.45 m/s average in CFD study) (ScienceDirect CFD/AC+fan, §2)

**Core unsolved gap (1 sentence):** BEE/IS 374:2019 testing ignores low-speed performance entirely — there is no official metric for the condition users rely on most hours per day, and all identified Indian-market "sleep modes" are timer-based speed step-downs, not adaptive or aerodynamically differentiated.

**Best concept direction from report (1–2 sentences):** Low-RPM-optimized blade profile (twist/camber/taper schedule tuned for 100–200 RPM) — spanwise blade redesign with root twist ≈25–40° tapering to tip twist ≈5–11°, as documented in US patent literature; expected benefit plausibly 10–25% better air delivery per Watt at speed 1–2 (Concept 1, §9).

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- US6,039,541 — High efficiency ceiling fan; twist/camber/taper for 50–200 RPM band (H overlap risk)
- US6,659,721 — High efficiency ceiling fan blades (geometry variant) (H overlap risk)
- US7,396,212 — "High efficiency twisted leaf blade ceiling fan" (H overlap risk)
- US7,665,967 / US7,927,071 — Efficient traditionally appearing ceiling fan blades with hidden aerodynamical upper surfaces (H overlap risk — disguises efficient low-speed airfoil inside conventional look)
- US9,103,346B1 — "Household fan for providing the feel of a natural breeze" — pulsed/random-extrema intensity control (H overlap risk for any "random/pseudo-random pulsing" sleep mode)
- US10,883,509 — "Smart ceiling fan, and its method of operation" (M overlap risk for sensor-driven speed adaptation)
- US11,828,292 — "Fan with increased efficiency mode" (M overlap risk for discrete mode distinct from normal operation)

**Links to other conditions (NN list + why):**
- **Condition 22 (Furniture under fan):** overlapping user scenario (bed under fan at night); short-throw ground-effect logic applies similarly
- **Condition 26 (Voltage fluctuation):** BLDC's superior low-speed torque control under voltage sag is especially beneficial in sleep mode
- **Condition 28 (Wobble):** low-speed operation exhibits higher sensitivity to blade imbalance and cogging-torque ripple since airflow masking is minimal

---

### 28 — Wobble, Vibration and Imbalance in Real Installations

| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | Wobble/balancing described as "one of the most common ceiling-fan consumer complaints and DIY-repair topics" (numerous manufacturer support pages, balancing-kit products exist); plausibly worse in India because of (a) false/POP ceilings with wooden batten supports, (b) long downrods, (c) hand-finished blade stamping, (d) voltage fluctuation (§1) |
| SEV | 2 | 1P cyclic loading produces visible "orbit" wobble transmitted through downrod into ceiling; deflects floor-level jet footprint cyclically (§2); but no quantified CFD study isolating this precession effect on floor air-speed distribution was located [UNVERIFIED — inferred from momentum theory, not cited measurement] (§2); no quantified comfort/performance degradation data found (§12) |
| UNSOLVED | 5 | No mainstream Indian ceiling fan brand markets an active, sensed anti-wobble/balancing feature; current market response entirely passive (factory QC + manufacturing tolerance) or reactive/manual (user-applied balancing clips/weights) — confirmed gap within searches performed [UNVERIFIED as exhaustive claim] (§6, §9) |
| PATENT_ROOM | 3 | ~10 families found: US5593281A, US5256037A (self-balancing rings), US7500831B2 (Hunter Fan self-balancing), US8123479 (accelerometer detection), US20090208333A1 (impact-triggered safety stop), CN1222654A (manual test-clip method), WO2023056181A1 (Microsoft tapered-notch hub, recent, H overlap risk), plus others; InPASS not directly queried (§8) |
| AERO_FIT | 1 | Wobble is fundamentally a 1×RPM mechanical force/moment problem driven by blade mass/pitch mismatch, amplified by system resonance (fan + downrod + ceiling mount); primarily a manufacturing/structural issue, not blade aerodynamics per se (§1, §2, §12) |
| EVIDENCE | 2 | General turbomachinery vibration-analysis methodology documented (impact testing, Bode analysis, spring-mass modeling) from industrial fan literature (Robinson Fans, Power-MI, Texas A&M TAMU OAKTrust), transferred to ceiling fans by analogy [UNVERIFIED for ceiling-fan case specifically] (§7); patents on sensing/balancing mechanisms exist but no India-specific wobble-amplitude comparison study (§7) |
| PROTO | 4 | Tri-axial MEMS accelerometer on motor housing; anemometer grid under fan to correlate wobble with floor-level air-speed unevenness; stroboscope or high-speed camera for visual blade-tip orbit; test matrix across rigid slab vs false-ceiling mount, short vs long downrod, factory-balanced vs deliberately introduced imbalance (§10) |
| **TOTAL** | **22** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Any blade-to-blade difference in mass, pitch angle, or aerodynamic chord produces a force/moment that cycles once per revolution (1P load) — documented in general turbomachinery vibration literature (Plant Engineering, §2)
- Fan–downrod–ceiling assembly behaves as mass-spring(-damper) system; wobble amplitude spikes when 1P excitation frequency (= operating RPM/60, e.g. 3.5–6 Hz for typical 300–350 RPM household fan) coincides with system natural frequency (§2)
- Permissible residual unbalance for general-purpose fans and motors typically expressed as ISO 21940-11 (formerly ISO 1940-1) balance quality grade G6.3 [UNVERIFIED for Indian manufacturers' actual tolerance classes] (§2, vibromera.eu)
- Self-balancing motor ring with movable spheres/liquid (US5256037A, 1993) and self-actuating retrofit balancer (US5593281A, 1990s) are old patents; adoption in current retail products [UNVERIFIED] (§6)

**Core unsolved gap (1 sentence):** No mainstream Indian ceiling-fan brand markets an active, sensed anti-wobble feature, and the foundational root cause — blade-to-blade mass/pitch mismatch — remains controlled only by passive factory QC and user-applied manual balancing, leaving a clear market and product-design gap.

**Best concept direction from report (1–2 sentences):** Motor-electrical-signature imbalance detection using existing BLDC controller telemetry (phase current ripple at 1×RPM as proxy for mechanical imbalance) — zero added hardware cost, likely avoids accelerometer-specific patent claims (US8123479/US20090208333A1), but detection sensitivity/reliability is unproven (Concept 2, §9).

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):**
- US5593281A — Universal retrofit dynamic-balancing apparatus; self-actuating balancer [UNVERIFIED exact priority date] (H overlap risk)
- US5256037A — Self-balancing motor via ring of movable spheres/liquid (M overlap risk — old patent, likely expired) [UNVERIFIED legal status]
- US7500831B2 — Self-balancing fan (Hunter Fan Co.); accelerometer-based auto-balancing [UNVERIFIED legal status] (H–M overlap risk)
- US8123479 — Accelerometer detects lateral/orbital wobble; installer feedback interface (M–H overlap risk)
- US20090208333A1 — Accelerometer detects blade impact/imbalance; motor stops rotation (safety-stop triggered) [status UNVERIFIED] (M overlap risk)
- WO2023056181A1 (Microsoft Technology Licensing) — Self-balancing hub with tapered-notch blade interfaces; recent, well-resourced assignee (H overlap risk)

**Links to other conditions (NN list + why):**
- **Condition 03 (High ceiling/long downrod):** long downrods lower system natural frequency into normal operating-speed range, exacerbating resonance-amplified wobble
- **Condition 27 (Low-speed sleep):** cogging-torque tonal noise becomes relatively more audible at low speed where airflow masking is minimal, and low-speed operation exhibits higher sensitivity to imbalance
- **Condition 26 (Voltage fluctuation):** voltage sag/torque ripple from modified-sine inverters may excite vibration modes in an otherwise marginal balance condition

---

| NN | TOTAL |
|---|---|
| 22 | 32 |
| 23 | 29 |
| 24 | 24 |
| 25 | 33 |
| 26 | 21 |
| 27 | 32 |
| 28 | 22 |

## Verification log

- **Card 23 (Mosquito nets)** — "Top quantified facts" bullet 3 ("Net imposes near-total velocity sink..."): old → "(high loss coefficient at low approach velocities typical of fan-driven flow, ~0.5–2 m/s) due to viscous-dominated Forchheimer regime (§2)"; new → "screen loss coefficient is highest at low approach velocities typical of fan-driven flow (~0.5–2 m/s, per non-dimensional screen-Reynolds-number framing) [UNVERIFIED — inference, needs direct test] due to viscous-dominated Forchheimer regime (§2)". Reason: the report's "~0.5–2 m/s" figure appears only in the §2 "non-dimensional framing" paragraph, which is explicitly marked `[UNVERIFIED — inference, needs direct test]` (it is the researcher's own derived framing, not a sourced measurement). The adjacent "mechanism" sentence in the report actually cites a different range, "0.3–1.5 m/s," for fan-driven air speeds at occupant height. The card had merged the two sentences and attached the unverified 0.5–2 m/s figure to the mechanism claim without preserving its [UNVERIFIED] tag — a rule violation (tags must be preserved on anything copied). Fixed by keeping the figure but restoring its correct unverified-inference attribution and tag.

All other scores, arithmetic (TOTAL = FREQ+SEV+UNSOLVED+PATENT_ROOM+2×AERO_FIT+EVIDENCE+PROTO), quoted facts, links, and patent numbers across cards 22, 24, 25, 26, 27, and 28 were checked against their source reports and the rubric/calibration anchors and found consistent — no further changes made.
