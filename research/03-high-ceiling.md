# AtomQuest 2026 Evidence Dossier — Condition 03: High and Double-Height Ceilings (>3.5 m)

ROLE context: Evidence dossier for Atomberg "AtomQuest 2026" hackathon team, aerodynamics focus, Indian residential/commercial ceiling fans.

## 1. Condition definition

High/double-height ceilings — duplexes, old bungalows, halls, temples, schools, lofts, showrooms — typically run **3.5–6 m** floor-to-ceiling, versus the standard Indian apartment 2.6–3.2 m assumed in BIS/BEE testing. Occupant breathing/sleeping height stays fixed at 1.1 m (seated) and 0.3–0.6 m (lying), so the **jet throw distance from blade plane to occupant roughly doubles** compared with a standard room.

- A practical downrod-selection chart used by Indian/US retailers: 12 ft ceiling → 24 in downrod; 13 ft → 36 in; 14 ft → 48 in; 15 ft+ → 60 in [UNVERIFIED — retailer guidance, not BIS-sourced] ([learnmetrics.com](https://learnmetrics.com/ceiling-fan-downrod-length/), [Crompton blog](https://www.crompton.co.in/blogs/fans-guide/ceiling-fan-height-from-floor)).
- For large halls/commercial spaces, 1400–1500 mm sweep fans are marketed specifically for "vaulted ceilings, tall rooms" — e.g. Usha Swift 1400 mm (166 m³/min, 375 rpm, 72 W) and Bajaj 1400 mm BLDC (up to 280 CMM, 70 W) for rooms 150–300 sq ft ([fybros.com](https://www.fybros.com/blog/ceiling-fan-sweep-size-guide-india), [ushafans.com](https://www.ushafans.com/swift-1400-mm)).
- I could not locate the exact IS 374:2019 clause text specifying minimum/maximum downrod length or blade-to-ceiling clearance for high-ceiling installations — this needs direct BIS document access [UNVERIFIED].
- Prevalence in India: no national survey data found quantifying the share of homes with >3.5 m ceilings. Qualitatively concentrated in older bungalows/havelis, duplexes/triplexes, temples, school and prayer halls, and new-build double-height living rooms in upper-mid/premium housing [UNVERIFIED — no cited statistic found].
- The commercial/industrial analogue is the HVLS (high-volume low-speed) fan market (Big Ass Fans etc.), explicitly engineered for ceilings 20–35+ ft, which is a useful adjacent-scale reference even though it's a different product class ([humongousfan.com](https://humongousfan.com/hvls-fan-sizing-airflow-guide/)).

## 2. Aerodynamic physics

- **Jet decay over long throw.** The fan's downwash behaves like a free turbulent jet from an actuator disk: it entrains ambient air, the jet cross-section spreads, and centerline velocity decays roughly with distance from the disk. The longer the ceiling-to-floor path, the more decay before the jet reaches occupant height — so delivered air speed at 1.1 m drops faster than proportionally with ceiling height. Momentum/actuator-disk theory (mass conservation + momentum change across the disk gives thrust; the streamtube expands downstream) is the first-order model for this ([ScienceDirect – Momentum Theory overview](https://www.sciencedirect.com/topics/engineering/momentum-theory)); exact % velocity-loss-vs-height data for residential ceiling fans specifically was not found in the search and should be [UNVERIFIED] pending CFD/field measurement.
- **Thermal stratification defeats a short/weak jet.** In tall rooms (especially under hot roofs — see condition 15), warm air pools near the ceiling. A conventional ceiling fan's downwash is "not maintained in a columnar pattern from ceiling to floor" in high rooms and "often disperses or diffuses well above the floor," making conventional fans largely ineffective as destratification devices at scale, per the Big Ass Fans "Temperature destratification systems" patent family description ([USPTO patent 9714663/11365743/11053948](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9714663)). Small-diameter high-speed fans (SDHSF) have been proposed in commercial literature as maintaining a more coherent, less-decaying jet over long throw distances than large slow fans ([ResearchGate — Performance Comparison of Destratification Fans for Large Spaces](https://www.researchgate.net/publication/304713559_Performance_Comparison_of_Destratification_Fans_for_Large_Spaces)).
- **Buoyancy vs momentum (Richardson/Archimedes number).** In a stratified tall room the fan's downward momentum jet competes against buoyant restoring forces from the warm ceiling layer; a high Richardson number regime means the jet loses coherence/penetration before reaching the floor. This is the same physics invoked for condition 13 (stratification) but amplified here purely by the larger vertical travel distance.
- **Governing non-dimensional numbers relevant here:** blade Reynolds number (chord × tip speed / ν — largely unchanged by ceiling height, it's a blade-design variable); jet spread rate/decay constant (function of initial disk diameter and turbulence, not of room height, but the *distance* it must travel before reaching the occupant is what room height changes); Richardson/Archimedes number for buoyancy-vs-momentum competition at long throw; clearance ratio h/D (fan-to-ceiling) which is now large and not limiting; downrod-length-to-diameter ratio (structural, affects wobble, not directly airflow).
- **Quantified effects:** no residential-fan-specific % air-delivery-loss-vs-ceiling-height dataset was found in the search; the only quantified Indian-market data point found is nominal rated air delivery at the fan (e.g. 166 m³/min for a 1400 mm fan) measured per BEE protocol at the fan itself, not at occupant height in a 4–6 m room — so the gap between rated service value and delivered occupant-level comfort in tall rooms remains [UNVERIFIED] and is itself a research gap (see Section 9).

## 3. Role of speed / RPM / frequency

- Raising RPM increases disk thrust and initial jet velocity, which should partially compensate for decay over a longer throw, but also increases blade-tip Reynolds number, noise, and power — this is a design trade-off, not free.
- Winter/destratification research (Harvard study cited by patent literature) found that running a fan **forward at variable low speed** to actively mix the room can use *less energy* than running a leading-edge/reverse-mode fan backward — "the most effective way to destratify air is to spin fans slowly in the forward direction, which will mix the air vertically" ([Harvard DASH — Comparing Modes of Operation for Residential Ceiling Fans](https://dash.harvard.edu/server/api/core/bitstreams/7312037d-ec98-6bd4-e053-0100007fdf3b/content)). This directly contradicts the common "reverse fan in winter for high ceilings" folk advice, and is relevant evidence Atomberg could use.
- Patented "automatic destratification" control systems (US8900041, US11598344, US12006945 — assignee not fully confirmed in search snippet, [UNVERIFIED]) use ceiling-vs-floor temperature sensors to automatically trigger winter destratification routines by varying motor speed.
- No specific resonance/beat-frequency/blade-pass-noise data tied to tall-room long-downrod operation was found; the only related finding is structural: long downrods amplify any pre-existing blade imbalance, risking wobble (see Section 4) rather than an aerodynamic resonance per se [UNVERIFIED for any acoustic resonance claim].
- BLDC/inverter drive frequency control is the natural lever for a "tall-room mode": could ramp RPM/pulse pattern to push jet penetration deeper before settling to a lower, quieter sustaining speed — no evidence found that any Indian brand currently implements a ceiling-height-aware speed profile [gap — see Section 9].

## 4. Blade and fan geometry levers

Ranked by expected impact for long-throw/high-ceiling condition (reasoned from the physics above; impact ranking is engineering judgement, not a literature-sourced ranking):

1. **Downrod length** — the primary lever actually used in practice today; lowers the blade plane closer to occupant height, directly cutting jet-decay distance. Retailer charts above show the de-facto industry rule of thumb.
2. **Sweep diameter** — larger sweep (1400–1500 mm) gives a larger initial jet cross-section and total thrust, partially offsetting decay; this is the second lever the Indian market already uses for halls.
3. **Pitch angle / blade chord and twist** — higher pitch/chord increases thrust per RPM, directly raising initial jet momentum. Rank 3 because it affects power/noise more directly than downrod/sweep changes.
4. **Number of blades** — more blades can increase swept-area solidity and smooth torque ripple, secondary effect on throw.
5. **Tip shape (winglets, rounded, serrated)** — reduces tip-vortex losses, modest efficiency gain, unlikely to materially fix long-throw decay on its own.
6. **Hub size / motor housing shape** — affects inflow blockage near the center, secondary for tall rooms specifically.
7. **Canopy shape** — negligible for this condition; relevant mainly to conditions 1/5/6 (cavity, obstruction, light kit).

No peer-reviewed or manufacturer-published ranking specific to "high ceiling" was found; this ranking is a physics-based inference and should be flagged as [UNVERIFIED — not literature-ranked] pending CFD/experimental confirmation.

## 5. Materials and manufacturing

- Longer downrods under self-weight and rotating blade loads need adequate bending stiffness; a too-long/thin rod risks bending or breaking under combined gravity and wind-gust loading in semi-open tall spaces ([DoItYourself.com forum discussion](https://www.doityourself.com/forum/electrical-ac-dc/646848-extending-ceiling-fan-longer-down-rod.html) — informal source, [UNVERIFIED] for any quantitative load limit).
- No material-specific (aluminium vs ABS vs composite blade) data tied specifically to high-ceiling/long-downrod operation was found; standard blade-material trade-offs (weight for lower bearing load and easier balancing, stiffness to resist flutter) apply generically but nothing condition-specific was located [gap].
- Manufacturing/cost implication: extended downrods, reinforced mounting hooks and possibly heavier-duty motor bearings to handle the longer lever arm add BOM cost; no INR figures found in the search [UNVERIFIED].

## 6. Current market solutions

| Company | Model(s) | Sweep / blades / RPM | Air delivery (m³/min) | Power (W) | Service value | Feature addressing tall rooms | How it works | Evidence | Still fails to solve |
|---|---|---|---|---|---|---|---|---|---|
| Usha | Swift 1400 mm | 1400 mm / 375 rpm | 166 | 72 | ~2.3 (calc.) | Large sweep for halls | Bigger disk area → more total thrust | [ushafans.com](https://www.ushafans.com/swift-1400-mm) | No stated downrod/long-throw optimisation; marketing claim, not independently tested |
| Bajaj | "Big fan for hall" 1400 mm BLDC | 1400 mm, BLDC | up to 280 (CMM) | 70 | ~4.0 (calc.) | Marketed for 150–300 sq ft halls | Larger sweep + BLDC efficiency | [bajajelectricals.com](https://www.bajajelectricals.com/collections/big-fan-for-hall) | Marketing claim; no independent long-throw/high-ceiling test data found |
| Various India brands (Khaitan, Havells, Atomberg etc.) | 1400/1500 mm sweep SKUs | varies | ~250–280 CMM claimed | 65–72 | ~4–4.3 (calc.) | Sold for "vaulted ceilings, tall rooms" per retailer copy | Larger disk area | [fybros.com sweep guide](https://www.fybros.com/blog/ceiling-fan-sweep-size-guide-india) | No brand found publishing occupant-level (1.1 m) velocity data at 4–6 m ceiling height — [UNVERIFIED gap] |
| Big Ass Fans | i6 series, Warehouse HVLS | downrod 36–60 in for 16–18 ft ceilings; HVLS up to 10,121 CFM | commercial-scale, not residential m³/min | n/a (industrial) | n/a | Purpose-built downrod kits by ceiling-height band; destratification patents | Large slow-rotating disk, high total airflow, patented destratification control | [premiumhomesource.com](https://www.premiumhomesource.com/products/big-ass-fans-i6-48-downrod-in-black-ceiling-height-16-18-ft), [USPTO destratification patents](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9714663) | Commercial/industrial scale and cost, not a residential retrofit solution |
| Hunter Industrial | Adjustable downrod kits | varies | n/a | n/a | n/a | Explicit "adjustable downrod" guidance for height-matching | Mechanical length adjustment | [industrialfans.hunterfan.com](https://industrialfans.hunterfan.com/blogs/hunter-industrial-blog/adjustable-downrod) | Industrial product, not adapted to residential BLDC ceiling fans |

Crompton, Havells, Orient, Polycab, Luminous, Superfan/Versa Drive, Gorilla, Panasonic, Minka-Aire, Hunter (residential), Modern Fan Co., Haiku, Dyson: no condition-specific (high-ceiling/long-downrod optimised) product or test data was found for these brands in this search session — flagged as a gap rather than assumed absent [UNVERIFIED — not found, not confirmed absent].

## 7. Academic and industry research

| Study | Method | Key finding | Limitation |
|---|---|---|---|
| Validated transient CFD study of ceiling fan-induced airflow (Journal of Building Performance Simulation, 2026) | 3D transient URANS CFD, multiple turbulence models vs measured data, "typical ceiling fan available in India" | Best agreement using SST k-ω turbulence model | Room/ceiling-height specifics not confirmed in abstract snippet [UNVERIFIED] — [tandfonline.com](https://www.tandfonline.com/doi/abs/10.1080/19401493.2026.2678829) |
| Transient 3D CFD modelling of ceiling fans (ScienceDirect) | CFD vs chamber measurements | Validates transient CFD approach for fan-induced airflow | Standard-height chamber, not explicitly tall-room [UNVERIFIED] — [sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0360132317302743) |
| Performance Comparison of Destratification Fans for Large Spaces (ResearchGate/ScienceDirect) | Comparative performance review | SDHSF (small-diameter high-speed fans) maintain velocity over longer throw than large slow fans; large fans ineffective at destratifying tall spaces | Commercial/industrial focus, not residential ceiling fan geometry — [researchgate.net](https://www.researchgate.net/publication/304713559_Performance_Comparison_of_Destratification_Fans_for_Large_Spaces) |
| Comparing Modes of Operation for Residential Ceiling Fans (Harvard DASH thesis/paper) | Energy/thermal modelling of forward vs reverse mode | Slow forward-mode operation destratifies more energy-efficiently than reverse mode | Thesis-level; needs independent replication — [dash.harvard.edu](https://dash.harvard.edu/server/api/core/bitstreams/7312037d-ec98-6bd4-e053-0100007fdf3b/content) |
| CBE Berkeley human-subject chamber studies (various) | 96 human-subject tests, environmental chamber | Minimum air velocity ~0.4 m/s at 26 °C up to 0.9 m/s at 30 °C for comfort; upward-blowing fans give more uniform vertical velocity profile than downward-blowing | Standard-height chamber; not tested at 4–6 m ceiling — [escholarship.org](https://escholarship.org/content/qt5fs9q6fq/qt5fs9q6fq.pdf) |

No IIT/IISc-specific high-ceiling ceiling-fan CFD paper was located in this search; the India-specific CFD paper found (tandfonline, 2026) validates a model against a "typical ceiling fan available in India" but the snippet did not confirm it studied high-ceiling geometry specifically [UNVERIFIED].

**Validated CFD approach (synthesised from above):** transient 3D URANS with SST k-ω or Spalart-Allmaras turbulence model, rotating blade region handled via sliding mesh or MRF (moving reference frame), validated against hot-wire/chamber measurements; this is the approach the closest India-relevant paper used.

## 8. Patent landscape

| Patent no. | Assignee | Core mechanism | Relevance to tall rooms | Overlap risk | Design-around idea | Link |
|---|---|---|---|---|---|---|
| US6357714B1 | [UNVERIFIED assignee] | Multiple telescoping, spring-loaded downrods, length-adjustable via threaded engagement | High — directly addresses variable ceiling height | M | Use a single continuously-adjustable composite rod rather than multiple discrete rods | [patents.google.com](https://patents.google.com/patent/US6357714) |
| US6443702B1 | [UNVERIFIED assignee] | Motorized lifting/lowering telescoping pipe for fan height | High — motorized height adjustment | M | Manual quick-release clamp instead of motorized mechanism | [patents.google.com](https://patents.google.com/patent/US6443702B1/en) |
| US6644928B1 | [UNVERIFIED assignee] | Retractable suspension device, adjustable upper/lower tube | High — direct downrod-length adjustability | M | Different locking mechanism (cam-lock vs threaded) | [patents.google.com](https://patents.google.com/patent/US6644928B1/en) |
| US20090074587A1 | [UNVERIFIED assignee] | Telescopic ceiling fan with adjustable lifting structure | High | M | — | [patents.google.com](https://patents.google.com/patent/US20090074587A1/en) |
| US9714663 (and related 11365743, 11053948) | Big Ass Fans (per patent family naming convention; [UNVERIFIED — not independently confirmed assignee name in this session]) | Temperature-sensor-driven automatic destratification control routines | High — directly targets high-ceiling stratification | H | Use a lower-cost single ceiling/floor delta-T sensor pair with BLDC speed ramp rather than full automatic routine patent claims (needs claim-by-claim legal review) | [image-ppubs.uspto.gov 9714663](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9714663) |
| US8900041 / US11598344 / US12006945 | [UNVERIFIED assignee] | "Automatic control system for ceiling fan based on temperature differentials" — winter destratification routine via motor controller | High | H | Avoid patented control-loop structure; use simple threshold-based speed step rather than claimed continuous feedback algorithm (needs claim review) | [image-ppubs.uspto.gov 11598344](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11598344) |
| US8123479 | [UNVERIFIED assignee] | Method to minimize oscillation in ceiling fans via accelerometer-detected wobble | Medium — relevant to long-downrod wobble risk, not throw/jet physics directly | M | — | [image-ppubs.uspto.gov 8123479](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8123479) |

This list is short of the 10–20 family target stated in the brief — a deeper Espacenet/WIPO Patentscope/InPASS search (not accessible as plain web search in this session) is needed to reach that count and to confirm assignees, priority dates, jurisdictions and legal status. **All assignee names, priority dates, legal-status and jurisdiction fields above are [UNVERIFIED]** since only Google Patents/USPTO snippet titles were retrieved, not full bibliographic data. This is research, not a legal opinion.

## 9. Unsolved gaps and opportunities

- **No Indian brand publishes occupant-level (1.1 m, lying 0.3–0.6 m) air-speed data for 1400/1500 mm fans at 4–6 m ceiling height.** BEE service value is measured at the fan, not at the floor in a tall room — the real comfort delivered in temples/halls/duplexes is essentially undocumented. Gap size: potentially large, since this is exactly the use case where current products are sized but not validated for the end comfort metric. [UNVERIFIED — inferred gap, no explicit study found confirming or denying it]
- **No ceiling-height-aware BLDC speed/mode profile found in the market** — a "tall room mode" that ramps RPM higher at startup to punch the jet through a longer throw/stratified layer, then settles to a quieter sustaining speed, was not found as an existing feature.
- **Conflicting evidence on reverse/winter mode** (Harvard finding that slow forward mixing beats reverse mode) suggests an opportunity: a validated, India-climate-tested "destratification mode" using BLDC's fine speed control, marketed with real data rather than the folk "reverse in winter" advice.
- **Concept directions for an aerodynamics-led team (reasoned proposals, not literature-sourced claims):**
  1. *Adaptive-thrust tall-room mode*: BLDC controller detects downrod length (via a mechanical encoder or user setting) and ceiling-floor ∆T (cheap thermistor pair) and raises initial RPM/thrust to compensate for longer throw, then drops to an efficient sustaining speed. Expected benefit: better occupant-height air speed per watt in halls — magnitude [UNVERIFIED, needs CFD/field test]. Risk: added sensor cost, certification complexity under BEE. Novelty vs patents: likely overlaps US8900041/11598344 claim scope for "temperature-differential-based control" — needs careful design-around on the control algorithm.
  2. *High-sweep, low-decay blade profile*: optimise twist/pitch distribution specifically to maximise jet coherence length (minimise early entrainment/spreading) rather than just peak CMM, borrowing SDHSF logic from commercial destratification fans. Expected benefit: more delivered velocity at floor for same rated CMM. Risk: possible noise/efficiency trade-off, no existing data quantifies the gain for residential scale.
  3. *Height-matched, pre-calibrated downrod + mount kit* (analogous to Hunter Industrial's by-ceiling-height downrod kits) sold as an accessory with a stiffness/wobble spec validated for Indian installation practices (hooks, flexible slabs). Addresses the wobble risk flagged in Section 3/5. Low novelty, but currently absent from the Indian residential market as a branded, validated kit.
  4. *Dual-mode (comfort / destratify) BLDC programme* validated against the Harvard forward-vs-reverse finding, marketed with Atomberg's own measured data to differentiate from "just reverse it" folk advice. Low cost (software-only), but needs an actual Indian-room experiment to claim any number.
  5. *Multi-fan layout guidance for large halls*, adapting the HVLS 2–2.5×D spacing rule to multiple 1400 mm residential/commercial fans in temples/halls — currently no Indian-market guidance found for this.

## 10. Measurement and validation plan

- **Instruments:** hot-wire or hot-sphere anemometer at 1.1 m (seated) and 0.3–0.6 m (lying) grid points under the fan at radii 0, 0.5D, 1.0D; vane-anemometer grid for a coarse floor-plane map; smoke/fog visualisation to see jet coherence/decay visually over the long throw; thermocouples at ceiling, mid-height and floor to quantify stratification (∆T); sound meter (dB(A)) and power meter at each test speed.
- **Grid/protocol:** repeat at multiple downrod lengths (e.g. 300/600/900/1200 mm) and multiple ceiling heights if a scaled or adjustable-height test rig is available, at 2–3 RPM settings each, to build an empirical decay curve of occupant-height velocity vs (ceiling height − downrod length) and vs RPM.
- **Metrics to report:** mean and turbulence-intensity of air speed at occupant planes, ∆T ceiling-floor before/after fan operation (destratification effectiveness), dB(A), W, and service value recomputed at occupant level (not just at the fan) to compare against BEE's at-the-fan number.
- **CFD comparison:** model the same geometry (3D transient URANS, SST k-ω or Spalart-Allmaras, sliding-mesh rotating blade region) per the validated approach in Section 7, and compare predicted vs measured occupant-height velocity and decay curve — this directly tests whether CFD can be trusted to explore downrod-length/RPM combinations cheaper than physical prototyping.

## 11. Sensors and smart control

- Ceiling-floor ∆T sensing (two cheap thermistors/thermocouples) is the enabling sensor for any destratification-aware mode — already used in the patented "automatic control system for ceiling fan based on temperature differentials" family (Section 8).
- Accelerometer/IMU-based wobble detection (US8123479) is directly relevant risk mitigation for the longer-downrod case, where any blade imbalance is mechanically amplified.
- No evidence found of any current product auto-detecting *ceiling height* itself (e.g. via ultrasonic distance to floor) to self-tune a "tall room mode" — this is an open opportunity, not a solved problem [UNVERIFIED — not found, flagged as gap rather than confirmed absent].

## 12. Summary

**Executive summary:** High and double-height ceilings (>3.5 m) stretch the ceiling fan's downwash jet over a much longer throw before it reaches occupant height, so the jet decays and loses coherence more before doing useful work — an effect worsened by thermal stratification common in tall, hot-roofed Indian spaces. The Indian market's current answer is almost entirely mechanical and empirical: longer downrods (sized by simple ceiling-height charts) and larger 1400–1500 mm sweep fans for halls, with no found evidence that any brand validates or publishes actual occupant-level air speed in these rooms, nor any BLDC "tall-room" speed/mode profile. Adjacent industries (HVLS/destratification fans) have patented temperature-sensor-driven destratification control and documented that slow forward-mode mixing beats the conventional "reverse the fan in winter" advice — both are transferable, underexploited insights for a residential BLDC product.

**Top 5 insights:**
1. Delivered (occupant-height) performance in tall rooms is essentially undocumented in the Indian market — BEE service value is measured at the fan, not at the floor 4–6 m below.
2. Downrod length and sweep diameter are the only levers the market currently uses; RPM/mode profiling by ceiling height is unexploited.
3. The "reverse the fan in winter for destratification" folk wisdom is contradicted by at least one study (Harvard) favoring slow forward-mode mixing — a BLDC-enabled, data-backed alternative is a low-cost differentiation opportunity.
4. Patented automatic ∆T-based destratification control exists in the HVLS/industrial space (Big Ass Fans family) but is not found in Indian residential ceiling fans — a design-around opportunity, pending full claim review.
5. Long-downrod installations mechanically amplify blade-imbalance wobble; this is a manufacturing/QA issue more than an aerodynamic one, but it's a real adoption barrier for any tall-room product push.

**Open questions / what could not be found:**
- Exact IS 374:2019 clause on blade-to-ceiling and downrod limits for tall rooms [UNVERIFIED].
- Any India-specific prevalence statistic for >3.5 m ceiling homes [UNVERIFIED].
- Any brand's independently-tested occupant-height velocity data at 4–6 m ceiling height [not found].
- Full patent family details (assignee, priority date, jurisdiction, legal status) beyond the short list in Section 8 — needs direct Espacenet/WIPO Patentscope/InPASS search access, not available via plain web search in this session.
- Any quantified %-air-delivery-loss-vs-ceiling-height curve for residential ceiling fans specifically (only qualitative/commercial-HVLS statements were found).

## Sources

- [Ceiling Fan Downrod Length Chart (learnmetrics.com)](https://learnmetrics.com/ceiling-fan-downrod-length/)
- [Crompton — How to Choose the Right Ceiling Fan Height](https://www.crompton.co.in/blogs/fans-guide/ceiling-fan-height-from-floor)
- [Ceiling Fan Size Guide 2026 (fybros.com)](https://www.fybros.com/blog/ceiling-fan-sweep-size-guide-india)
- [Usha Swift 1400 mm](https://www.ushafans.com/swift-1400-mm)
- [Bajaj Big Fan for Hall](https://www.bajajelectricals.com/collections/big-fan-for-hall)
- [Performance Comparison of Destratification Fans for Large Spaces — ResearchGate](https://www.researchgate.net/publication/304713559_Performance_Comparison_of_Destratification_Fans_for_Large_Spaces)
- [Temperature destratification systems — USPTO 9714663](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9714663)
- [Temperature destratification systems — USPTO 11365743](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11365743)
- [Temperature destratification systems — USPTO 11053948](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11053948)
- [Automatic control system for ceiling fan based on temperature differentials — USPTO 11598344](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11598344)
- [Automatic control system for ceiling fan based on temperature differentials — USPTO 12006945](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12006945)
- [Automatic control system for ceiling fan based on temperature differentials — USPTO 8900041](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8900041)
- [Method to minimize oscillation in ceiling fans — USPTO 8123479](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8123479)
- [Comparing Modes of Operation for Residential Ceiling Fans — Harvard DASH](https://dash.harvard.edu/server/api/core/bitstreams/7312037d-ec98-6bd4-e053-0100007fdf3b/content)
- [Thermal destratification — Wikipedia](https://en.wikipedia.org/wiki/Thermal_destratification)
- [Momentum Theory overview — ScienceDirect Topics](https://www.sciencedirect.com/topics/engineering/momentum-theory)
- [HVLS Fan Sizing and Airflow Guide — humongousfan.com](https://humongousfan.com/hvls-fan-sizing-airflow-guide/)
- [Big Ass Fans i6 48" Downrod product page](https://www.premiumhomesource.com/products/big-ass-fans-i6-48-downrod-in-black-ceiling-height-16-18-ft)
- [Hunter Industrial — Adjustable Downrod](https://industrialfans.hunterfan.com/blogs/hunter-industrial-blog/adjustable-downrod)
- [Validated transient CFD study of ceiling fan-induced airflow — Journal of Building Performance Simulation](https://www.tandfonline.com/doi/abs/10.1080/19401493.2026.2678829)
- [Transient three-dimensional CFD modelling of ceiling fans — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0360132317302743)
- [Spatial Uniformity of Thermal Comfort from Ceiling Fans — eScholarship (CBE Berkeley)](https://escholarship.org/content/qt5fs9q6fq/qt5fs9q6fq.pdf)
- [US6357714B1 — Ceiling fan with multiple downrods — Google Patents](https://patents.google.com/patent/US6357714)
- [US6443702B1 — Motorized ceiling fan lifting and lowering apparatus — Google Patents](https://patents.google.com/patent/US6443702B1/en)
- [US6644928B1 — Retractable suspension device of a ceiling fan — Google Patents](https://patents.google.com/patent/US6644928B1/en)
- [US20090074587A1 — Telescopic Ceiling Fan — Google Patents](https://patents.google.com/patent/US20090074587A1/en)
- [BEE Star rating standards — bijlibachao.com](https://www.bijlibachao.com/fans/new-beee-star-rating-standards-ceiling-fans.html)
