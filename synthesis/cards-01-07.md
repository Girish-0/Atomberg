# AtomQuest 2026 — Condition Cards 01–07

### 01 — Recessed / Cove False Ceiling Mounting
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | False/POP ceilings with cove are default aesthetic in urban apartments/bedrooms; marketed by interior designers (§1, Coohom design articles); no national statistic found [UNVERIFIED] |
| SEV | 3 | CBE clearance rule 0.2×D ≈ 240 mm typically violated by false-ceiling installs (§2); inflow starvation mechanism credible but cavity-specific % loss unmeasured [UNVERIFIED] |
| UNSOLVED | 4 | No brand publishes "as installed in false ceiling" air-delivery data (§6); Atomberg's dual canopy/plate system is mechanical fit only, not aero fix |
| PATENT_ROOM | 4 | Thin patent landscape: only generic downrod/mounting-bracket mechanics, no cove-specific prior art (§8) |
| AERO_FIT | 5 | Blade-to-ceiling clearance, hub profile, blade root geometry, inflow area are direct aerodynamic levers (§4, rank 1–4) |
| EVIDENCE | 2 | CBE guidance is generic open-ceiling h/D; no cove-cavity CFD or experimental study found (§7 gap); cavity recirculation extrapolated from lid-driven-cavity analogy [UNVERIFIED] |
| PROTO | 4 | Adjustable mock cove (depth 0–300 mm, gap width variable), hot-wire grid, smoke visualization, power meter — bench test feasible (§10) |
| **TOTAL** | **31** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- CBE minimum 20 cm (8 in), optimum ≥31 cm (12 in) blade-to-ceiling clearance, and h/D ≈0.2 rule for starvation threshold ([CBE Fans Guidebook](https://cbe-berkeley.gitbook.io/fans-guidebook/full-guidebook/ceiling-fan-installation-and-integration-with-hvac-system))
- Atomberg Renesa uses different mounting hardware: top canopy for ≥240 mm downrod gap, ceiling plate + bottom canopy for <240 mm gap ([Atomberg Renesa listing](https://www.chandruandco.com/product-view.php?product=atomberg+Renesa+1200mm))
- Typical Indian false ceiling peripheral drop is 200–300 mm, installer-used downrod is often 75–125 mm, net clearance often well under 150 mm ([Atomberg false-ceiling blog](https://atomberg.com/blogs/blog/false-ceiling-fan))
- Blade-geometry optimization study: +21% airflow, +54% service value, −22% power at 300 RPM [needs primary-source verification — [UNVERIFIED](https://www.jafmonline.net/article_1855_9669d857c1f611ebab91f7cd6008ecea.pdf)]

**Core unsolved gap (1 sentence):** No published quantification of airflow/service-value loss specific to cove-cavity false-ceiling installs, and no brand publishes rated air delivery as installed (only per open-ceiling BEE test chamber).

**Best concept direction from report (1–2 sentences):** Low-profile, large-inflow-area hub/motor shroud compensating for restricted vertical gap within the same false-ceiling envelope; or blade root geometry re-optimised for restricted/asymmetric inflow. A cove-aware mounting clearance calculator bundled with the fan is a low-cost, non-aerodynamic but high-leverage installer-behaviour fix.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US6196804B1, US10498099B2, US9982679B2 (all generic downrod/mounting hardware, [UNVERIFIED assignees]); US5595068A (AC unit short-circuit flow analogy); US8641375 (recessed exhaust fan + light, separate product class, not a downrod-mounted room fan).

**Links to other conditions (NN list + why):** Condition 02 (low ceiling/hugger — same inflow-starvation physics, different geometry driver: clearance above vs downrod-constrained); Condition 03 (high ceiling — opposite end of clearance spectrum but similar jet-decay/return-path issues); Condition 06 (light kit — hub blockage can compound cove cavity effect).

---

### 02 — Low Ceiling / Hugger / Flush-Mount Fans (<2.6 m ceiling height)
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 3 | 2.4–2.6 m ceilings common in budget apartments, lofts, PMAY units; hugger fans marketed for "low ceiling" and "duplex upper floor" use; no India-specific prevalence data found [UNVERIFIED] |
| SEV | 3 | Hugger fans cited as moving "40% less airflow" than downrod fans [UNVERIFIED — single secondary source]; inflow starvation mechanism credible (clearance ratio h/D ≈ 0.08 vs standard ≈0.25) but quantified loss unproven |
| UNSOLVED | 4 | No Indian brand publishes independently tested air-delivery comparison for hugger vs standard mount at same blade/motor; current products address mechanical fit only |
| PATENT_ROOM | 4 | Patent landscape incomplete; only 3 loosely relevant candidates surfaced (US10989207, US11293458, US7927071), all unverified; no "low-clearance inlet redesign" patent family identified |
| AERO_FIT | 5 | Blade-to-ceiling clearance, blade span, blade pitch, hub shape, canopy design are direct aero/geometry levers (§4, ranked 1–5) |
| EVIDENCE | 2 | US consumer-guide clearance recommendations (6–12 inch minimum) are non-peer-reviewed directional guidance; CBE/LBNL data apply to standard clearance only; no Indian BLDC hugger-specific CFD found (§7 gap) |
| PROTO | 4 | Adjustable-height ceiling rig (2.4–3.0 m range), hot-wire grid, smoke visualization, power meter at multiple clearances — feasible bench test |
| **TOTAL** | **30** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Hugger fans recommended at 6–12 inches (≈150–300 mm) blade-to-ceiling clearance; 8 inches often cited as optimum ([Delmar Fans](https://www.delmarfans.com/educate/best-ceiling-fans-for-8ft-ceilings), [Parrot Uncle](https://parrotuncle.com/blogs/news/ceiling-fan-clearance-how-much-space-do-you-need-from-the-ceiling)); these are US consumer guides, not peer-reviewed
- Atomberg Renesa Enzel 1200 mm: 255 CMM claimed, ≈28 W at top speed, sold with "additional ceiling plate for false/low ceilings" ([Atomberg retail](https://atomberg.com/atomberg-renesa-halo-bldc-motor-3-blade-ceiling-fan), [Smartprix](https://www.smartprix.com/fans/atomberg-brand)) — marketing claim, not independently tested
- "Clearance ratio h/D ≈ 0.08 for hugger (100 mm gap ÷ 1200 mm sweep) vs ≈0.25 for standard downrod (300 mm gap)" — engineering estimate, no source quantifies delivery-vs-h/D curve for Indian BLDC fans
- IS 374:2019 specifies minimum floor clearance ~2.1 m (7 ft) but clause text not verified from accessible sources

**Core unsolved gap (1 sentence):** No quantified clearance-vs-delivery curve exists for Indian 1200 mm BLDC hugger fans; no brand tests and publishes air delivery specifically at hugger mounting vs standard downrod.

**Best concept direction from report (1–2 sentences):** Raised or flared central inlet above the hub to recover inflow volume within the low-profile envelope; or shorter-span, higher-pitch blade set specifically tuned for low h/D rather than a shrunk standard design. BLDC controller compensation via current-sensing to detect low-clearance install and re-tune speed curve is a software-only option.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US10989207 [UNVERIFIED assignee], US11293458, US11828301, US11828292, US7927071, US7665967 — all [UNVERIFIED] for relevance to hugger inlet aerodynamics; no dedicated hugger-clearance patent family identified in this search.

**Links to other conditions (NN list + why):** Condition 01 (recessed ceiling — same inflow-starvation mechanism, different cause); Condition 03 (high ceiling — opposite end of jet-throw spectrum but shares return-path constraints); Condition 06 (light kit — hub blockage compounds clearance constraint).

---

### 03 — High and Double-Height Ceilings (>3.5 m)
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 3 | >3.5 m ceilings concentrated in duplexes, bungalows, halls, temples, schools, premium housing (§1); no national survey data found [UNVERIFIED]; qualitatively niche vs standard 2.6–3.2 m apartments |
| SEV | 4 | Jet decay over long throw is documented physics (momentum theory; §2); thermal stratification in tall hot-roofed rooms is real problem (§2, Big Ass Fans patent); no residential-fan-specific "% velocity loss at occupant height vs ceiling height" data found [UNVERIFIED magnitude] |
| UNSOLVED | 4 | No Indian brand publishes occupant-level (1.1 m, 0.3–0.6 m) air-speed data for 1400/1500 mm fans at 4–6 m ceiling (§9); BEE service value measured at fan, not floor; "tall-room mode" speed profile not found in market |
| PATENT_ROOM | 2 | Report's own patent table rates US9714663/US11365743/US11053948 and US8900041/US11598344/US12006945 (temperature-differential destratification control — directly the mechanism the report's top concept direction proposes) as Overlap risk **H** (§8); this is a crowded area with on-point patents found, not a thin/no-patent landscape, so calibration anchor caps this well below 4 |
| AERO_FIT | 5 | Downrod length, sweep diameter, pitch angle, blade chord, RPM/mode profiling (adaptive thrust mode, "tall-room mode") are core aero levers (§4, ranked 1–7) |
| EVIDENCE | 2 | Jet decay mechanism is standard fluid mechanics; one paper validates CFD for "typical Indian fan" (tandfonline 2026) but scope unconfirmed; Harvard forward-vs-reverse finding contradicts folk "reverse in winter" but is thesis-level; no residential-fan occupant-height test at 4–6 m found |
| PROTO | 4 | Tall rig or 4–6 m available room, anemometer grid at multiple heights (1.1 m, 0.6 m, 0.3 m), thermocouples for stratification, smoke visualization, power meter — measurable |
| **TOTAL** | **29** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Retailer downrod-selection rule: 12 ft ceiling → 24 in downrod; 13 ft → 36 in; 14 ft → 48 in; 15 ft+ → 60 in ([learnmetrics.com](https://learnmetrics.com/ceiling-fan-downrod-length/), [Crompton blog](https://www.crompton.co.in/blogs/fans-guide/ceiling-fan-height-from-floor)) [UNVERIFIED as engineering standard, retail guidance only]
- Large-sweep fans for halls: Usha Swift 1400 mm, 166 m³/min, 375 rpm, 72 W; Bajaj 1400 mm BLDC up to 280 CMM, 70 W, marketed for 150–300 sq ft rooms ([fybros.com](https://www.fybros.com/blog/ceiling-fan-sweep-size-guide-india), [ushafans.com](https://www.ushafans.com/swift-1400-mm))
- Harvard finding: slow forward-mode operation destratifies more energy-efficiently than reverse mode, contradicting folk "reverse in winter" advice ([Harvard DASH](https://dash.harvard.edu/server/api/core/bitstreams/7312037d-ec98-6bd4-e053-0100007fdf3b/content))
- SDHSF (small-diameter high-speed fans) maintain velocity over longer throw than large slow fans for commercial destratification ([ResearchGate destratification comparison](https://www.researchgate.net/publication/304713559_Performance_Comparison_of_Destratification_Fans_for_Large_Spaces))

**Core unsolved gap (1 sentence):** No Indian brand publishes occupant-height air-speed data for tall rooms, and no BLDC "tall-room mode" speed profile that ramps RPM to punch jet through longer throw is found in the market.

**Best concept direction from report (1–2 sentences):** Adaptive-thrust tall-room mode: BLDC controller detects downrod length and ceiling-floor temperature difference, raises initial RPM to punch jet through stratified layer, then settles to efficient sustaining speed. Dual-mode destratification profile validated against Harvard forward-vs-reverse finding and marketed with measured Indian-room data as a differentiation from folk advice.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US6357714B1, US6443702B1, US6644928B1, US20090074587A1 (all telescoping/adjustable downrod, [UNVERIFIED assignees]); US9714663, US11365743, US11053948, US8900041, US11598344, US12006945 (destratification control, [UNVERIFIED assignees]); US8123479 (wobble minimization via accelerometer, [UNVERIFIED]).

**Links to other conditions (NN list + why):** Condition 01 (recessed ceiling — both involve inflow/return-path constraints but opposite ends of vertical spectrum); Condition 04 (sloped ceiling — both have asymmetric inflow but mechanism differs); Condition 13 (thermal stratification — high ceilings amplify stratification problem; tall-room mode and slow forward mixing directly apply).

---

### 04 — Sloped / Vaulted / Pitched Ceilings (10°–45° pitch)
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 2 | Sloped roofs in Kerala, coastal, hill-style houses, attics, resorts (§1); no national survey data; Indian fan vendors sell "angle mount" brackets, but no Atomberg/Crompton/Havells technical guidance found — anecdotal prevalence, not quantified [UNVERIFIED] |
| SEV | 2 | Asymmetric inflow (uphill side starved, downhill side open) and 1P cyclic blade loading are plausible mechanisms (§2); but no measured air-delivery loss, velocity at occupant height, or noise increase for slope angles 10–45° found anywhere — entirely [UNVERIFIED] magnitude |
| UNSOLVED | 4 | No aerodynamic (blade/hub) solution exists in market or literature, but mechanical re-leveling brackets (Hunter SCA-P, Modern Forms 45° kit) DO exist and are sold in market to solve the downrod hang-vertical problem (§6); calibration anchor caps UNSOLVED at 5 only if the report found NO product addressing it at all — here a mechanical product exists, same as conditions 01/02, so capped at 4 |
| PATENT_ROOM | 4 | Mounting-bracket patents found (US9086074B2, US5090654A, US5725190A, US5947436A — all [UNVERIFIED assignees], all mechanical-only); no aerodynamic-compensation patent identified (§8 gap); white space appears open but search incomplete (InPASS not queried) |
| AERO_FIT | 5 | Azimuth-asymmetric blade pitch (cyclic or fixed), off-center hub, slope-angle-aware adaptive speed mode, horizontally-articulated hub to keep disk plane flat despite ceiling slope are plausible aero levers (§9, concepts 1–4) |
| EVIDENCE | 1 | No published ceiling-fan CFD or experimental study of tilted rotor plane found; only HAWT (wind turbine) yaw/tilt-misalignment literature on 1P cyclic loading cited (§2, §7); extrapolation to ceiling-fan geometry is [UNVERIFIED] and untested |
| PROTO | 3 | Adjustable-slope mock ceiling (variable 0–45°), anemometer grid, IMU for cyclic vibration, smoke visualization, sound meter — more complex than fixed-geometry rig but feasible |
| **TOTAL** | **26** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Slope adapter rating bands: Hunter Original for 34–45°; Hunter SCA-P for >34–<56°; Modern Forms "45° Slope Kit" for 0–45°; some ball-joint designs limited to 15–28° (§1, §4, [Ferguson Hunter](https://www.fergusonhome.com/hunter-sloped-ca/s1228273), [Modern Fan Co.](https://modernfan.com/ceiling-fans/45-degree-slope-kit/))
- HAWT wind-turbine literature: "1P (one-per-revolution) peaks of the thrust spectrum are significantly increased with blade misalignments" ([ScienceDirect HAWT cyclic loads](https://www.sciencedirect.com/science/article/abs/pii/S0960148117310121)); but ceiling-fan application [UNVERIFIED]
- General install guidance for sloped ceilings: keep blades ≥7 ft (≈2.1 m) above floor and 8–10 in (≈200–250 mm) below the ceiling plane at its lowest point, with ≥18 in (≈450 mm) blade-tip clearance from walls/beams, more on steep vaults ([Lemon Thistle](https://www.lemonthistle.com/install-ceiling-fan-sloped-ceiling/))
- IS 374:2019 clause on slope-specific mounting clearance could not be verified from accessible sources [UNVERIFIED]

**Core unsolved gap (1 sentence):** No CFD, experimental study, or market product addresses the aerodynamic (blade/hub) asymmetry caused by sloped ceilings; only mechanical re-leveling brackets exist, leaving the underlying 1P cyclic loading and clearance asymmetry untouched.

**Best concept direction from report (1–2 sentences):** Azimuth-asymmetric blade pitch (passive fixed or active cyclic, like helicopter blades) to compensate for uphill/downhill clearance asymmetry and flatten 1P loading; or IMU-detected slope angle at commissioning triggering an adaptive speed cap / "slope mode" in BLDC control to manage vibration/wobble. A slope-aware, BIS-referenced installation spec for the Indian market (non-aerodynamic but market-first) is a low-novelty but high-differentiation opportunity.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US9086074B2, US5090654A, US5725190A, US5947436A (all mechanical mounting/bracket, [UNVERIFIED assignees]); GB2503907A (tilt mechanism, [UNVERIFIED scope]); US6872054B2 (mounting system, [UNVERIFIED relevance]).

**Links to other conditions (NN list + why):** Condition 01 (recessed ceiling — both have asymmetric inflow but vertical vs angular driver); Condition 07 (corner/wall — both produce 1P/azimuthal cyclic loading and pressure imbalance); Condition 28 (vibration/wobble — long downrods in tall rooms amplify blade imbalance, sloped geometry adds cyclic loading).

---

### 05 — Exposed Beams, Ducts, and Ceiling Obstructions
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 2 | Exposed RCC beams in older independent houses, duplexes, budget apartments; wooden beams/trusses in Kerala/Himachal heritage construction (§1); no India-specific incidence survey found [UNVERIFIED] |
| SEV | 2 | Inflow starvation on beam-side sector and 1P BPF tonal noise are plausible mechanisms (§2, analogous to tip-clearance fan-noise and hidden-fan obstruction literature), but no measured air-delivery loss or dB(A) increase for a ceiling-beam geometry found anywhere [UNVERIFIED magnitude] |
| UNSOLVED | 5 | No manufacturer markets ANY feature — not even a mechanical workaround — addressing beam/obstruction-aware mounting (§6: "no manufacturer...markets any feature addressing beam/obstruction-adjacent mounting — this itself is the headline gap"); unlike conditions 01/02/04 (where mounting-kit products exist), here zero products of any kind were found, meeting the calibration anchor's "NO product addresses it" bar for a 5 |
| PATENT_ROOM | 4 | Report explicitly flags this patent search as thin/incomplete ("falls far short of the 10-20 relevant-family target...mark the entire patent landscape for this condition as [INCOMPLETE/UNVERIFIED]", §8); calibration anchor caps a thin search that "found few" at max 4, not 5 |
| AERO_FIT | 4 | Blade-to-ceiling clearance, blade count, hub inlet-ring design (per Lin & Hsieh hidden-fan study: 80 mm min blockage distance, 30 mm max ring height) are plausible aero levers (§4), but beam-specific application unproven |
| EVIDENCE | 2 | Lin & Hsieh 2014 hidden-fan study is closest quantified prior art (housed fan, not free rotor + external beam — geometry differs); BPF tonal mechanism is generic but unquantified for beam case; no IIT/IISc/CEPT study on beams found (§7 gap) |
| PROTO | 4 | Simulated beam (adjustable depth 150–450 mm, tip clearance 0–1.5×D), radial anemometer grid (4–8 points, 2–3 radii to detect asymmetry), smoke, sound meter per IS 374 geometry, power meter — feasible bench test (§10) |
| **TOTAL** | **27** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- IS 374:2019 specifies "any projecting beam or ceiling structure... no closer than 1 m above the fan-blade test plane"; test-chamber exclusion rule, not an in-home performance limit ([BIS IS 374:2019 PDF](https://indianfanassociation.com/wp-content/uploads/2023/01/BIS-IS-374-2019-and-Ammendment-1.pdf))
- Lin & Hsieh hidden-ceiling-fan study: minimum blockage distance 80 mm, max ring-plate height 30 mm improve performance from restricted inflow scenario ([Lin & Hsieh 2014 SAGE/Hindawi](https://journals.sagepub.com/doi/10.1155/2014/214967)); housed-fan geometry, not free-rotor-plus-external-beam case
- General installer guidance: 8–12 inch blade-to-ceiling minimum (§1, §4) — non-quantified directional guidance from consumer sources, not BIS
- Transient 3D CFD study (J. Building Performance Simulation 2026) validates Overset Mesh + SST k-ω methodology for ceiling-fan airflow, reporting BPF-linked periodic velocity/turbulence fluctuations decaying with distance (§7, [tandfonline](https://www.tandfonline.com/doi/abs/10.1080/19401493.2026.2678829)) — baseline methodology for beam study, but no obstruction geometry included

**Core unsolved gap (1 sentence):** No quantified measurement of air-delivery loss, occupant-level velocity reduction, or BPF tonal-noise increase caused by a ceiling beam in the inflow path; mechanism is plausible but entirely unmeasured.

**Best concept direction from report (1–2 sentences):** Asymmetric downrod offset or tilt kit that positions fan disk away from beam's shadow; or blade inlet-ring geometry (per Lin & Hsieh guidance) adapted to recover beam-side inflow loss. Sensor-free, torque-ripple-smoothing control to dampen 1P periodic loading is a software-only lever leveraging existing BLDC compensation.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US20050141997A1 [UNVERIFIED] (abandoned, blade-proximity safety sensor, low relevance); US8241017B2, US8770949B2 [UNVERIFIED] (internal bearing/hub clearance, low relevance). Patent landscape incomplete; dedicated patent-database search flagged as follow-up (§8 gap).

**Links to other conditions (NN list + why):** Condition 01 (recessed ceiling — both involve inflow starvation, different geometry); Condition 06 (light kit — both have hub-region blockage causing 1P loading and dead-zone flow); Condition 07 (corner/wall — both produce asymmetric loading and cyclic 1P/1P-related vibration).

---

### 06 — Ceiling Fan with Integrated Light Kit or Chandelier
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 3 | Underlight BLDC fans are "fast-growing premium segment" (Crompton, Orient, Atomberg, Havells SKUs); mainstream in urban bedrooms/living rooms; decorative chandelier hybrids remain niche high-end (§1, §6) — no market-share % found [UNVERIFIED prevalence of underlight ≥50% of market] |
| SEV | 3 | Hub-blockage dead-zone mechanism is documented at ~15%-of-D threshold (§2, ResearchGate study); stroboscopic flicker risk is qualitatively reported across user forums (§3, Houzz/Hi-Hyperlite) but NOT clinically studied for Indian BLDC RPM bands (300–350 RPM = 15–17.5 Hz BPF, inside 3–70 Hz photosensitivity risk); quantified air-delivery loss from light-kit addition not measured [UNVERIFIED severity] |
| UNSOLVED | 4 | All underlight SKUs (Crompton Blossom, Orient Aeroslim/Spectra, Atomberg Renesa) lack A/B comparison of air delivery with/without light ring (§6, §9); stroboscopic flicker documented qualitatively but no solution published in underlight products found (§3) |
| PATENT_ROOM | 3 | US5795220A (diffuser apparatus) and US12180976 (frustoconical diffuser + anti-strobe light direction) already claim airflow + light geometry solutions (§8); HIGH overlap risk; but InPASS not searched, Indian patents may fill white space |
| AERO_FIT | 4 | Hub/light-ring diameter (sets blockage ratio β), vertical offset (inflow side vs downwash side), blade root shape, diffuser-ring geometry (frustoconical, finned, perforated) are aero levers (§4, ranked 1–4) — not light color/direction per se |
| EVIDENCE | 2 | Hub-blockage CFD on bare motors exists (ScienceDirect, ResearchGate); 15%-of-D threshold is cited (§2); light-kit-specific CFD or test NOT found (§7 gap); strobe risk band from generic photosensitivity literature, not fan-specific clinical study; "40% underlight fans in Indian market" [UNVERIFIED] |
| PROTO | 4 | Same blade/motor/RPM, compare (a) no light kit, (b) stock underlight, (c) candidate diffuser ring; hot-wire grid at occupant height + near-hub zone; lux meter / high-speed camera for flicker; straightforward A/B/C comparison (§10) |
| **TOTAL** | **27** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Hub blockage threshold: "when the diameter of the central hub is greater than 15% of the diameter of the cylindrical ring, a dead zone around the rotation axis is generated where air does not circulate" ([ResearchGate investigating aerodynamic performance](https://www.researchgate.net/publication/299975586_Investigating_Aerodynamic_Performance_of_a_Ceiling_Fan))
- Stroboscopic flicker risk band: photosensitive epilepsy literature cites ~3–70 Hz risk, 15–20 Hz "of greatest concern" ([Epilepsy Action](https://www.epilepsy.org.uk/info/seizure-triggers/photosensitive-epilepsy), [FlickerSense](https://www.flickersense.org/led-health-effects/flicker-below-100-hz-scientific-literature))
- Typical Indian 3-blade fan at 300–350 RPM: blade-pass frequency ≈ 15–17.5 Hz (RPM/60 × blades) — squarely in provocative flicker band (§3)
- Crompton Blossom: 1200 mm, ~245 CMM, 12 W LED underlight, "aerodynamic ABS body" claim ([Crompton collection](https://www.crompton.co.in/collections/ceiling-fans/underlight-fans)) — marketing claim, not independently tested for light-kit airflow penalty

**Core unsolved gap (1 sentence):** No published independent quantification of air-delivery loss caused specifically by an underlight ring or chandelier body (vs a plain hub), and no stroboscopic-flicker mitigation found in current underlight products despite user complaints.

**Best concept direction from report (1–2 sentences):** Integrate diffusing function (per US12180976 or US5795220A concept) into blade root camber/twist rather than a separate ring, recovering hub-zone velocity without added parts; or RPM-synchronized anti-strobe light control that pulses/dims integrated underlight at a rate that avoids aligning with blade-pass-frequency harmonics. Separate up/down light assemblies straddling blade plane (reportedly used by some manufacturers) is lower-novelty existing workaround.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US5795220A (motor within diffuser, light assembly), US12180976 (frustoconical diffuser + anti-strobe light direction, both [UNVERIFIED assignees]); US6354801B1, US6171060, US9696026 (hub/light integration variants, mostly [UNVERIFIED or likely expired]); USD875288, USD1109311S1 (design patents, Hunter, low functional relevance).

**Links to other conditions (NN list + why):** Condition 01 (recessed ceiling — both involve hub blockage/dead-zone flow); Condition 05 (exposed beams — both produce 1P loading from hub-region obstruction); Condition 28 (vibration — underlight asymmetric mass can couple with blade imbalance on wobble).

---

### 07 — Corner / Off-Centre / Near-Wall Mounting
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | 4 | Very common in small urban bedrooms; electrician-fixed ceiling boxes often off-centre; beds pushed against walls for space in 1BHK/2BHK box apartments (§1); no India survey found, but qualitatively "very common" across building types [UNVERIFIED precise % but prevalence is real] |
| SEV | 2 | Inflow starvation on near-wall side, Coandă attachment, cyclic azimuthal loading, cone tilt are plausible mechanisms (§2); but NO measured air-delivery loss, velocity at occupant height, or noise change vs wall-gap/D ratio found for any fan anywhere (§2 final point, §9) — entirely unmeasured [UNVERIFIED severity] |
| UNSOLVED | 5 | NO manufacturer markets near-wall or corner-compensation feature; six Indian brands searched (Atomberg, Crompton, Havells, Orient, Bajaj, Usha) — none offer wall-clearance guidance or product (§6, §9); complete market gap |
| PATENT_ROOM | 4 | No near-wall-compensation patent found specifically, but the report's own patent table (§8) rates US6116856A and US10989207 at Overlap risk **M** (moderate), not zero; combined with the single-pass, InPASS-not-queried search depth, the calibration anchor's "thin search that found few" rule caps this at 4, not 5 |
| AERO_FIT | 5 | Asymmetric fixed blade pitch/chord, offset-hub or tilt-adjustable downrod/canopy, sensor-adaptive speed/mode, shorter-sweep designs are plausible aero/control levers directly targeting wall asymmetry (§9, concepts 1–4) |
| EVIDENCE | 1 | **NO peer-reviewed or CFD study of ceiling fan vs wall-gap/D <0.5 found anywhere** (§2 final, §7, §9); closest physics analogs are CBE/LBNL mount-distance findings (conflicting thresholds >0.3 m "no effect" vs ≤0.4 m "effect," unverified vs primary source) and HVAC diffuser Coandă literature (sidewall jets, not ceiling fans); mechanism is plausible but entirely [UNVERIFIED] quantitatively |
| PROTO | 4 | Place fan at wall-gap/D ratios (0.2, 0.35, 0.5, 0.8×D) in fixed room, anemometer grid at 2 heights, smoke visualization, IMU for cyclic vibration, sound meter, power meter — feasible bench test (§10) |
| **TOTAL** | **30** | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- Installer guidance: keep blade tips roughly **half the fan diameter** from the nearest wall, e.g. ~18 in (≈460 mm) for a 36 in fan ([This Old House sizing](https://www.thisoldhouse.com/fans/21018783/how-to-size-up-a-ceiling-fan), [SMAFan clearance guide](https://smafan.com/blogs/smart-home/ceiling-fan-clearance-guide))
- Secondary certification-consultancy sources claim "60 cm minimum wall clearance" and "300 mm blade-to-ceiling minimum" as BIS/IS 374:2019 requirements, but primary standard text not verified from accessible sources ([InstaCertify](https://instacertify.com/resources/standards/mandatory-bis-standard/isi-mark-electric-ceiling-fans), [BISregistrationcertificate.com](https://bisregistrationcertificate.com/blog/bis-certification-for-electric-ceiling-fans/))
- CBE/LBNL full-scale 78-test laboratory finding (secondary summary): mount distance >0.3 m (for 1.5 m fan) does NOT notably affect room air speeds; vs separate claim that mount distance ≤0.4 m (for 1.4 m fan) DOES affect airflow ([primary PDF unverified, fetch failed](https://escholarship.org/uc/item/4p479663)) — conflicting, secondary summaries only [UNVERIFIED]
- Coandă-effect mechanism from HVAC sidewall diffuser literature: "supply air flow is attached to the ceiling [wall] due to the Coandă effect" under certain velocity ratios ([ResearchGate sidewall jet](https://www.researchgate.net/publication/338525067_Ceiling-Fan-Integrated_Air_Conditioning_airflow_and_temperature_characteristics_of_a_sidewall-supply_jet_interacting_with_a_ceiling_fan)) — diffuser context, not ceiling-fan-near-wall case [UNVERIFIED transferability]

**Core unsolved gap (1 sentence):** **No published study, CFD model, or market product quantifies air-delivery, occupant-level velocity, or noise change for ceiling fans mounted with wall-gap <0.5×D** — this is the single largest literature and market gap identified across all seven conditions.

**Best concept direction from report (1–2 sentences):** Asymmetric fixed blade pitch/chord distributed to bias disk loading away from the near wall, flattening the net cone tilt; or mechanical offset-hub/tilt-adjustable downrod kit allowing installers to angle disk away from wall at install time. IMU-detected asymmetric vibration signature characteristic of near-wall operation triggering adaptive speed cap is a software-only lever reusing wobble-detection logic from condition 28.

**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** US6116856A [UNVERIFIED] (bi-directional asymmetric reversible blades — overlap risk M); US10989207 (low-profile directional centrifugal fan — overlap risk M); US8152453 (angled mounting for sloped ceilings — low-moderate overlap risk L, repurposable for lateral tilt); US9528529, US9638209B1 [UNVERIFIED] (multi-directional blade angles, blade attachment — low relevance).

**Links to other conditions (NN list + why):** Condition 01 (recessed ceiling — both have asymmetric inflow but different geometry driver); Condition 04 (sloped ceiling — both produce 1P/azimuthal cyclic loading and pressure imbalance); Condition 05 (exposed beams — both have asymmetric obstruction to return path); Condition 28 (vibration/wobble — near-wall cyclic loading and inflow asymmetry couple with blade imbalance).

---

## Summary Table

| NN | Condition | TOTAL | Rank | Evidence strength | Aerodynamics centrality | Market gap |
|---|---|---|---|---|---|---|
| 01 | Recessed/False Ceiling | 31 | 1 | Weak (clearance rule only) | High (hub, blade root) | High (mounting kit exists, no aero fix, no installed data) |
| 02 | Low Ceiling/Hugger | 30 | 2 (tied) | Weak (consumer guides, unquantified) | High (inlet geometry) | High (mounting kit exists, no tested hugger aero) |
| 07 | Corner/Near-Wall | 30 | 2 (tied) | Extremely weak (zero studies found) | High (asymmetric pitch, offset hub) | Very high (no brand feature at all, no aero study) |
| 03 | High Ceiling | 29 | 4 | Weak (mechanism only, no residential test) | High (RPM mode, pitch) | High (occupant-level data gap, but destratification-control patents found with HIGH overlap risk) |
| 05 | Exposed Beams | 27 | 5 (tied) | Very weak (hidden-fan study only) | Moderate (inlet ring, blade count) | Very high (zero brand features of any kind; patent search flagged incomplete) |
| 06 | Light Kit/Chandelier | 27 | 5 (tied) | Weak (hub-blockage CFD generic, strobe unquantified) | Moderate (root shape, diffuser) | Moderate (patents exist but gap in published test) |
| 04 | Sloped Ceiling | 26 | 7 | Very weak (only HAWT analogy, no CF) | Moderate-High (blade pitch, hub) | High (mechanical slope-adapter kits exist in market; no aero solution) |

## Verification log

Arithmetic (TOTAL = FREQ+SEV+UNSOLVED+PATENT_ROOM+2×AERO_FIT+EVIDENCE+PROTO) was wrong on all 7 cards — the stated TOTAL did not match the sum of the stated component scores. Component-level calibration errors (vs. rubric calibration anchors) were also found and fixed on cards 03, 04, 05, 07. All fixes below.

1. **Card 01** — TOTAL: 34 → 31. Reason: arithmetic error; 4+3+4+4+(2×5)+2+4 = 31, not 34. No component scores changed.
2. **Card 02** — TOTAL: 34 → 30. Reason: arithmetic error; 3+3+4+4+(2×5)+2+4 = 30, not 34. No component scores changed.
3. **Card 03** — PATENT_ROOM: 4 → 2. Reason: calibration anchor violation. The report's own patent table (§8) rates the destratification-control patents (US9714663, US11365743, US11053948, US8900041, US11598344, US12006945) — directly the mechanism behind the report's top concept direction — as Overlap risk **H** (high). This is a crowded space with on-point patents found, not a "thin search that found few" (which caps at 4); crowded/high-overlap maps to a low PATENT_ROOM score per the rubric's 1=crowded anchor.
4. **Card 03** — TOTAL: 36 → 29. Reason: arithmetic error (31 vs. stated 36) plus the PATENT_ROOM fix above (31 → 29 after 4→2, i.e. −2).
5. **Card 04** — UNSOLVED: 5 → 4. Reason: calibration anchor violation. Anchor states UNSOLVED=5 only if the report found NO product addressing the condition at all. The report's §6 documents mechanical slope-adapter brackets (Hunter SCA-P, Modern Forms 45° kit) actually sold in market that solve the downrod hang-vertical problem — the same pattern as conditions 01/02, which were correctly capped at 4 for this reason. Card 04 was inconsistently scored 5.
6. **Card 04** — TOTAL: 31 → 26. Reason: arithmetic error (27 vs. stated 31) plus the UNSOLVED fix above (27 → 26 after 5→4, i.e. −1).
7. **Card 05** — UNSOLVED: 4 → 5. Reason: calibration anchor violation (undercorrected in the other direction). The report's §6 explicitly states "no manufacturer...markets any feature addressing beam/obstruction-adjacent mounting" — zero products of any kind (not even a mechanical workaround, unlike 01/02/04). This meets the anchor's "NO product addresses it" bar for UNSOLVED=5, matching the treatment given to condition 07.
8. **Card 05** — PATENT_ROOM: 5 → 4. Reason: calibration anchor violation. The report explicitly flags its own patent search as incomplete ("falls far short of the 10–20 relevant-family target...mark the entire patent landscape for this condition as [INCOMPLETE/UNVERIFIED]", §8). The anchor caps a thin search that "found few" at max 4, not 5.
9. **Card 05** — TOTAL: 32 → 27. Reason: arithmetic error (27 vs. stated 32); the UNSOLVED (+1) and PATENT_ROOM (−1) fixes above net to zero change versus the corrected arithmetic baseline.
10. **Card 06** — TOTAL: 30 → 27. Reason: arithmetic error; 3+3+4+3+(2×4)+2+4 = 27, not 30. No component scores changed.
11. **Card 07** — PATENT_ROOM: 5 → 4. Reason: calibration anchor violation. The report's own patent table (§8) rates US6116856A and US10989207 at Overlap risk **M** (moderate) — not zero — so patents were in fact found reading on adjacent concepts. Combined with the single-pass, InPASS-not-queried search depth noted in the report, the anchor's "thin search that found few" rule caps this at 4, not 5.
12. **Card 07** — TOTAL: 36 → 30. Reason: arithmetic error (31 vs. stated 36) plus the PATENT_ROOM fix above (31 → 30 after 5→4, i.e. −1).
13. **Summary Table** — all TOTAL, Rank, and Market-gap-column text updated to match the corrected per-card scores above. New sum: 200 (was stated as 233); new average: 28.6 (was stated as 33.3). New ranking: 01 (31) > 02=07 (30) > 03 (29) > 05=06 (27) > 04 (26). This spread (26–31) is consistent with the rubric's calibration-anchor expectation that TOTALs across the full 28-report set should range roughly 18–36, and that a batch where every card scores ≥30 is miscalibrated — after these fixes, 5 of 7 cards in this batch now score below 30.

No quoted facts, numbers, links, or patent numbers were altered — all were checked against the 7 source reports (01–07) and found to appear verbatim (including [UNVERIFIED] tags) with no invented content.

**TOTAL cards: 7 | TOTAL SCORE SUM: 200 (average 28.6)**
