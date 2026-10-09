# AtomQuest 2026 — Condition 24: Soft Furnishings vs Hard Surfaces (Carpets, Curtains, Sofas vs Tile/Marble/Concrete)

**Room condition researched:** Absorptive surfaces (carpet, heavy curtains, upholstered sofas) compared with hard reflective surfaces (vitrified tile, marble, concrete) — effect on floor/wall boundary-layer friction and the recirculation loop, curtain flapping/window blockage, and acoustic differences (reverberant vs absorptive rooms).

---

## 1. Condition definition

A ceiling fan's downwash jet strikes the floor, spreads radially, climbs the walls and returns to the ceiling to re-enter the blade inflow (the classic "recirculation torus"). The nature of the floor and wall surfaces it slides across — and the presence of soft furnishings in that path — changes two independent things:

- **Aerodynamic**: the floor/wall boundary-layer friction coefficient and the obstruction/absorption of the horizontal floor jet by furniture, curtains and rugs.
- **Acoustic**: room reverberation time (RT60), which changes perceived fan noise even if the fan's own sound power is unchanged.

Typical Indian parameter ranges:
- Flooring: vitrified tile (most common, cost-efficient, durable [UNVERIFIED — no percentage-share data found], per [JK Cement flooring guide](https://www.jkcement.com/blog/flooring-solution/flooring-guide/)), marble, polished/exposed concrete, and (less commonly) wall-to-wall carpet or large area rugs in bedrooms/living rooms.
- Window treatments: cotton/polyester/sheer curtains are near-universal in Indian bedrooms and living rooms; heavy lined drapes are less common except in upscale homes.
- Upholstery: sofas, cushions and mattresses are common in living/bedrooms; prayer halls, classrooms and kitchens are mostly hard-surfaced.
- No India-specific survey quantifying the carpet-vs-hard-floor split was found in this search; the general flooring-guide sources describe vitrified tile as dominant and carpet as a minority choice (bedrooms, high-end furnishing) [UNVERIFIED for precise share]. Source: [JK Cement](https://www.jkcement.com/blog/flooring-solution/flooring-guide/), [Houzz India](https://www.houzz.in/magazine/which-tiles-are-perfect-for-indian-floors-stsetivw-vs~86143723).

## 2. Aerodynamic physics

**Floor jet and boundary layer.** CBE Berkeley's experimental characterisation of ceiling-fan airflow describes the descending jet narrowing until ~0.6 m above the floor, then impinging and spreading as a "horizontal floor jet" whose depth scales with fan diameter; at 0.3 m above a hard floor the measured speed was roughly half the jet core speed and evenly distributed (CBE Fans Guidebook, [case studies](https://cbe-berkeley.gitbook.io/fans-guidebook/full-guidebook/case-studies-for-researchers); [desk/partition study](https://escholarship.org/content/qt3pq2j9mh/qt3pq2j9mh_noSplash_f340ee940d7072e92c55ab3be91ca070.pdf)). This characterization was done over conventional (hard) flooring; no India-specific or CBE study directly comparing carpeted vs hard-floor boundary layers under a ceiling fan was found [UNVERIFIED — gap].

From general fluid-mechanics principles (not fan-specific literature found): a carpet or rug presents a rougher, more compliant, and air-permeable surface than tile/marble/concrete. Expected first-order effects, by extension of standard wall-bounded turbulent flow theory:
- **Higher skin friction (higher equivalent sand-grain roughness)** over carpet increases the turbulent boundary-layer thickness and wall shear, dissipating floor-jet momentum faster, so the stagnation/spread velocity at ankle height decays over a shorter radius than over tile.
- **Partial absorption/compliance** of carpet pile and padding can damp near-wall turbulence intensity slightly, reducing the "draft" sensation at floor level but also reducing the far-reach of the floor jet (the jet "dies" sooner), potentially shrinking effective coverage radius.
- **Furniture (sofas, beds) in the floor-jet path** act as bluff-body obstructions: they block the radial floor jet and the subsequent wall-climb, forcing local flow separation, horseshoe vortices around furniture legs, and dead/stagnant zones in their lee — directly analogous to the "furniture blocking the return path" discussed for condition 21 (tall wardrobes) in this same brief series. [UNVERIFIED — no dedicated study of furniture-induced blockage located; reasoning extended from general bluff-body/ventilation literature].
- **Curtains across the airflow path** near a window-adjacent fan or a crossflow path act as a porous screen: lightweight sheers flap and oscillate (literature on curtain movement attributes flapping to pressure differentials from drafts/cross-ventilation, not specifically fan-driven floor jets — see [curtainsuk.com](https://www.curtainsuk.com/blogs/news/do-curtains-really-help-keep-the-draft-out) and [Alibaba product-insights](https://www.alibaba.com/product-insights/how-to-stop-your-curtains-from-blowing-in-the-wind-with-simple-fixes.html)). A heavier/thicker curtain "spreads the force" and flaps less, implying a porosity-dependent pressure-drop response, but no quantified porosity-vs-velocity-reduction data (Darcy/Forchheimer coefficients) for curtain fabric under fan-driven flow was found [UNVERIFIED].

**Governing non-dimensional quantities (not found pre-derived for this condition in literature; stated here as the relevant physics, to be used with caution and validated by the team's own testing):**
- Wall roughness Reynolds number / equivalent sand roughness height (k_s) for carpet pile vs hard floor — governs whether the floor boundary layer is hydraulically smooth (tile/marble, low friction factor) or fully rough (carpet, higher friction factor).
- Porosity (open-area ratio) and permeability of curtain fabric — governs pressure drop across the screen (Darcy's law regime) and hence how much of the horizontal floor jet or wall-climb air can pass through vs be deflected/absorbed. No specific coefficients found for furnishing fabrics; textile-engineering porosity data could be sourced separately.
- No quantified % drop in air delivery, coverage area or velocity-at-occupant-height specific to carpet vs hard floor was found in any fan-aerodynamics source searched. **This is flagged [UNVERIFIED] — likely unstudied or unpublished for ceiling fans specifically.**

## 3. Role of speed / RPM / frequency

No literature specific to how carpet/curtain/furniture absorption changes the optimum RPM band was found. Reasoning by extension: because the floor-jet momentum dissipates faster over carpet/furnished floors, a higher RPM (more thrust/momentum) may be needed to achieve the same occupant-level air speed as over a hard floor, at the cost of motor power and noise. BLDC variable-speed and "natural breeze" pulsed modes (vendor-common features; see Section 6) are not documented as being tuned for floor-covering type specifically [UNVERIFIED]. No resonance/beat-frequency interaction with soft furnishings was found or is physically expected (furnishings are not structurally coupled to the fan-downrod system; compare with condition 28, wobble, which is a structural rather than furnishing issue).

## 4. Blade and fan geometry levers

No sources link blade geometry choices (sweep, blade count, chord, twist, winglets, downrod length) specifically to floor-covering or furnishing conditions. By extension of general ceiling-fan design knowledge: a fan that produces a wider, lower-velocity floor jet (larger sweep, lower RPM) spreads load over more floor area and may be less sensitive to local absorption/obstruction than a narrow, high-velocity jet from a small-sweep, high-RPM fan, because the latter's momentum is more concentrated and thus more affected by localized furniture blockage directly under it (condition 22 overlap). Ranking of levers for this specific condition is **not supported by found evidence** [UNVERIFIED] — flagged as a research gap rather than invented.

## 5. Materials and manufacturing

Not directly relevant to this condition (soft furnishings don't change blade material requirements). One tangential, verifiable point: dust and lint adhesion on blades (addressed in condition 20) can be elevated in carpeted/heavily-upholstered rooms because carpets and fabrics are known dust/fibre reservoirs that get resuspended by airflow — this is a plausible but [UNVERIFIED] mechanism specific to fans, though carpet fibre shedding and dust-trapping is well documented generally in flooring/allergen literature (not verified here with a fan-specific source).

## 6. Current market solutions

No manufacturer markets a ceiling fan feature explicitly addressing "carpet vs hard floor" or "soft furnishings." The table below lists general-purpose BLDC/5-star fans (verified specs) with a note that none claim a furnishing-specific feature.

| Company | Model(s) | Sweep / blades / RPM | Air delivery | Power | Service value | Feature for this condition | How it works | Evidence | Still fails to solve |
|---|---|---|---|---|---|---|---|---|---|
| Atomberg | Renesa | 1200 mm / 3 blade | 235 m³/min (CMM) | 28 W | ~8.2 CMM/W (5-star) | None specific | BLDC motor efficiency, standard blade | [vsctimes.com comparison](https://vsctimes.com/atomberg-vs-crompton-bldc-fan/) [marketing-adjacent, cross-check with BEE database before citing as certified] | No furnishing-aware control |
| Crompton | Energion HS / SilentPro | 1200 mm | 220 CMM | 35 W | ~8.6 CMM/W (SilentPro, per source) | None specific | BLDC | [vsctimes.com](https://vsctimes.com/atomberg-vs-crompton-bldc-fan/) | No furnishing-aware control |
| Havells | Ambrose BLDC / Glaze / Efficiencia Neo | 1200 mm | 225 CMM | 28–30 W | ~6.3 CMM/W (Efficiencia Neo) | None specific | BLDC | [vsctimes.com](https://vsctimes.com/best-bldc-fans/) | No furnishing-aware control |
| Orient, Usha, Bajaj, Polycab, Luminous, Superfan, Gorilla, Panasonic | — | — | — | — | — | — | — | No furnishing-specific marketing claim found in this search | — |
| Big Ass Fans / Hunter / Minka-Aire / Haiku / Dyson | — | HVLS / residential | — | — | — | Large-diameter, low-speed designs reduce local velocity concentration (general HVLS design philosophy) | Design guide | [Big Ass Fans Design Guide](https://learn.bigassfans.com/design-guide) | No explicit furnishing-interaction data published |

**Note:** all the CMM/W figures above come from secondary comparison sites, not directly from BEE's official database or the manufacturers' own certified datasheets — treat as [UNVERIFIED pending BEE Star Label database cross-check] rather than as certified test data. For an official check, BEE's own schedule is at [beestarlabel.com Schedule 8 PDF](https://www.beestarlabel.com/Content/Files/Schedule8-CF.pdf).

## 7. Academic and industry research

- CBE Berkeley (UC Berkeley Center for the Built Environment) — multiple studies on ceiling-fan floor-jet behaviour, air-speed uniformity, desks/partitions, and ceiling-fan-integrated air conditioning (CFIAC). Method: full-scale chamber measurements with anemometer grids. Key quantified finding: floor-jet speed at 0.3 m height ≈ half of jet core speed over a hard floor; air speed is spatially non-uniform even when temperature is uniform. Limitation: conducted over conventional hard/office flooring, not carpeted or furnished rooms — **no carpet/furnishing variant found**. Sources: [CBE Fans Guidebook — Ceiling fans](https://cbe-berkeley.gitbook.io/fans-guidebook/full-guidebook/ceiling-fans), [Ceiling fan air speeds around desks and partitions (eScholarship PDF)](https://escholarship.org/content/qt3pq2j9mh/qt3pq2j9mh_noSplash_f340ee940d7072e92c55ab3be91ca070.pdf), [Spatial Uniformity of Thermal Comfort from Ceiling Fans (eScholarship PDF)](https://escholarship.org/content/qt5fs9q6fq/qt5fs9q6fq.pdf), [CFIAC sidewall-jet interaction, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0360132320300184), [Buildings & Cities journal — CFIAC thermal comfort evaluation](https://journal-buildingscities.org/articles/10.5334/bc.137).
- Acoustic/reverberation literature (general building acoustics, not fan-specific): hard surfaces (concrete NRC ≈ 0.02) vs carpet+pad (NRC ≈ 0.55) vs heavy curtain (NRC ≈ 0.50); RT60 in all-hard residential rooms can be 2–4 s vs a comfortable conversational target of <0.8 s. Sources: [Carpet Institute Australia — acoustic benefits](https://www.carpetinstitute.com.au/residential/carpet-noise-pollution-reduction/), [Mass Loaded Vinyl Direct — hard vs soft acoustics guide](https://massloadedvinyldirect.com/guides/hard-vs-soft-materials-acoustics/), [JJ Flooring Group — acoustic white paper PDF](https://www.jjflooringgroup.com/wp-content/uploads/Acoustic_White_Tech_Paper_FINAL.pdf). These NRC/RT60 figures are general building-acoustics data, not measured specifically with an operating ceiling fan as the noise source — apply directly to "fan noise perception" with caution [UNVERIFIED extrapolation].
- No CFD study specifically modelling fan airflow interaction with carpet roughness or curtain porosity was located in this search. This is a genuine literature gap, not an omission.

## 8. Patent landscape

No patents specifically addressing "ceiling fan + soft furnishings/carpet/curtain interaction" were found — this appears to be an unclaimed niche. The table below lists general blade-noise-reduction patents found (relevant to the acoustic half of this condition, i.e. making the fan itself quieter so reverberant/hard rooms are less punishing), not furnishing-interaction patents specifically.

| Patent no. | Assignee | Priority date | Jurisdiction | Legal status | Core mechanism | Claim summary | Relevance to condition 24 | Overlap risk | Design-around idea | Link |
|---|---|---|---|---|---|---|---|---|---|---|
| US7494325B2 | [UNVERIFIED assignee] | [UNVERIFIED] | US | [UNVERIFIED] | Ridged blade surface | Ridges reduce fan noise output | Indirect — lower source noise helps in reverberant hard-surfaced rooms | L | Use micro-riblet surface finish instead of discrete ridges | [link](https://patents.google.com/patent/US7494325B2/en) |
| US20060110257A1 | [UNVERIFIED] | [UNVERIFIED] | US | [UNVERIFIED] | Dimpled blade surface | Dimples create turbulence altering deflection angle, raising speed & lowering noise | Indirect | L | Vary dimple density radially instead of uniform pattern | [link](https://patents.google.com/patent/US20060110257) |
| US20070154314A1 | [UNVERIFIED] | [UNVERIFIED] | US | [UNVERIFIED] | Splitter blades between primary blades | Reduces tonal blade-pass noise | Indirect | L | Use asymmetric splitter count | [link](https://patents.google.com/patent/US20070154314) |
| US20050147496A1 | [UNVERIFIED] | [UNVERIFIED] | US | [UNVERIFIED] | Roughened/serrated trailing edge | Minimises tonal acoustic emission | Indirect | L | Combine with winglet instead of serration | [link](https://patents.google.com/patent/US20050147496) |
| US20030095864A1 | [UNVERIFIED] | [UNVERIFIED] | US | [UNVERIFIED] | Blade end-pieces | Blocks tip vortices, raises efficiency, lowers noise | Indirect | L | Use swept tip instead of discrete end-piece | [link](https://patents.google.com/patent/US20030095864A1/en) |
| US5388956A | [UNVERIFIED] | [UNVERIFIED] | US | [UNVERIFIED] | Fan assembly noise reduction method | General noise-reduction assembly | Indirect | L | — | [link](https://patents.google.com/patent/US5388956) |
| US5448645A | [UNVERIFIED] | [UNVERIFIED] | US | [UNVERIFIED] | Active fan-blade noise cancellation | Electronic active noise cancellation | Indirect, but conceptually closest to "compensate for reverberant room" | M | Passive tuned-mass damper instead of active cancellation | [link](https://patents.google.com/patent/US5448645A/) |
| US4511310A | [UNVERIFIED] | [UNVERIFIED] | US | [UNVERIFIED] | Ceiling fan blade isolation (vibration) | Isolates blade vibration from motor/hub | Indirect (vibration, not acoustics-of-room) | L | — | [link](https://patents.google.com/patent/US4511310A/en) |
| US6776578B2 | [UNVERIFIED] | [UNVERIFIED] | US | [UNVERIFIED] | Winglet-enhanced fan | Winglets reduce tip vortex noise | Indirect | L | — | [link](https://patents.google.com/patent/US6776578B2/en) |
| US12180976 | [UNVERIFIED] | [UNVERIFIED] | US | [UNVERIFIED] | Ceiling fan airflow diffuser apparatus | Diffuses airflow pattern | Potentially relevant — a diffuser could be tuned to compensate for absorptive floors | M | Adjustable diffuser angle vs fixed | [link](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12180976) |

**Flag:** assignee, priority date, and legal status were NOT verifiable from the search snippets returned and are marked [UNVERIFIED] throughout — a full Google Patents/Espacenet/InPASS session (not snippet search) is needed to populate these fields reliably. This table should be treated as a starting shortlist, not a cleared freedom-to-operate analysis. No Indian Patent Office (InPASS) results were returned in this search round.

## 9. Unsolved gaps and opportunities

- **No fan-specific study quantifies how carpet, rugs, sofas or curtains change floor-jet reach, recirculation strength, or occupant-level air speed.** This is the single biggest gap: product teams currently design against bare-floor assumptions (per CBE's methodology) and then sell into living rooms/bedrooms that are frequently furnished and sometimes carpeted.
- **No published furniture-blockage % vs air-delivery-at-occupant-level data** — teams must generate this themselves (see Section 10).
- **Acoustic mismatch**: a fan tuned/tested for low dB(A) in a lab (typically hard, semi-reverberant test chamber per IS 374/BEE test method) may sound louder or "boomier" in an all-hard Indian living room (tile + bare walls) than the same fan in a furnished, carpeted one, due to RT60 differences of several seconds (Section 7). No product currently publishes room-dependent noise ratings.
- **3–5 concept directions (team-generated, to be validated — not sourced from literature):**
  1. *Adaptive floor-jet width control* (variable blade pitch or dual-zone blades) that widens the jet footprint in rooms with absorptive/furnished floors to compensate for faster momentum decay — quantified benefit unknown, needs CFD/lab test; novelty vs patents likely high (no blocking patent found) but engineering complexity and cost (variable-pitch mechanism) are significant.
  2. *Acoustic-adaptive speed profile*: use a microphone or accelerometer to estimate room reverberance (crude proxy: measure the fan's own blade-pass tone decay time after a brief speed pulse) and auto-select a quieter speed/mode in highly reverberant (bare, hard-surfaced) rooms — moderate novelty, overlaps conceptually with active-noise-cancellation patents (US5448645A) at the mechanism level if electronic cancellation is used, lower risk if implemented as pure speed-scheduling.
  3. *Low-tip-noise blade geometry* (riblets, serrated/roughened trailing edge, winglets) as a baseline improvement that helps specifically in hard-surfaced reverberant rooms — well-precedented in patents (Section 8), so novelty is low; treat as a "must-have baseline," not a differentiator.
  4. *Furniture-aware installation guidance* (a placement/clearance calculator in-app, analogous to Wi-Fi router placement tools) using room dimensions and furniture layout input to recommend downrod length/sweep — low aerodynamic novelty, but could be a UX differentiator; negligible patent risk.
  5. *Curtain-safe low mode near windows* — a pre-set speed cap for rooms where a user indicates curtains are near the fan's throw, reducing flapping/nuisance — low engineering cost, low novelty, mostly a software/UX feature.

## 10. Measurement and validation plan

- **Instruments**: an anemometer grid (hot-wire or omnidirectional vane) at 0.1 m, 0.3 m (lying height), 0.6 m, and 1.1 m (seated height) above the floor, covering a 0.5D-spaced grid out to the walls; a sound level meter (dB(A), with octave-band capability to see blade-pass tones) positioned at ear height in multiple spots; a power meter at the fan's supply.
- **Test matrix**: same fan, same room, same RPM settings, cycling through (a) bare hard floor + bare walls, (b) area rug/carpet added, (c) rug + sofa/bed placed under part of the floor-jet footprint, (d) sheer curtains added near a window within the jet's wall-climb path. Repeat at low/medium/high speed.
- **Metrics to report**: air speed decay curve vs radius at each height; reverberation time (RT60, via impulse/balloon-pop or swept-sine method) for each furnishing configuration; A-weighted SPL and tonal (blade-pass frequency) SPL; power draw (should be furnishing-invariant — confirms whether any change is purely acoustic/aerodynamic environment, not fan behaviour).
- **CFD cross-check**: model the floor and lower walls with a rough-wall boundary condition (equivalent sand-grain roughness representing carpet pile) vs smooth-wall (tile/marble); compare predicted near-floor velocity decay against the above anemometer grid. Use RANS (k-ω SST, as commonly used for ceiling-fan room flows) with MRF for the blade region; mesh refinement near floor/wall boundary layers is critical for roughness sensitivity. [No published mesh/BC recipe specific to this furnishing comparison was found — this is the team's own CFD setup to validate, not a sourced best-practice.]

## 11. Sensors and smart control

No existing product was found that senses floor covering or furnishing and adapts fan behaviour. A fan could in principle infer room reverberance from its own acoustic feedback (microphone sensing decay of its blade-pass tone) or infer airflow resistance from current-draw/RPM response, but no implementation or research prototype doing this was located [UNVERIFIED — plausible but unproven concept].

## 12. Summary

**Executive summary:** Soft furnishings (carpet, curtains, upholstery) versus hard surfaces (tile, marble, concrete) plausibly change two independent things about a ceiling fan's performance in a room — the aerodynamic recirculation loop (via floor/wall friction and furniture blockage) and the perceived noise (via room reverberation time, which differs by seconds between bare-hard and furnished rooms per general building-acoustics data). However, this research found **no fan-specific, quantified study** of the aerodynamic side of this condition: all floor-jet characterisation work located (CBE Berkeley) was done over conventional hard flooring, and no carpet/furniture-blockage variant exists in the literature found. The acoustic side is better supported by general building-acoustics NRC/RT60 data, though not measured with an operating ceiling fan as the source.

**Top 5 insights:**
1. CBE Berkeley's floor-jet characterisation (jet narrows to ~0.6 m, then spreads; speed at 0.3 m ≈ half of core) is the best available baseline, but it is a hard-floor baseline — no carpeted/furnished variant exists to compare against.
2. General acoustics data shows carpet/heavy-curtain NRC (~0.5) vs bare concrete (~0.02) — an enormous absorption difference that should materially change perceived fan noise, independent of the fan's actual sound power.
3. Furniture directly in the floor-jet's spread path (sofas, beds) is expected to create local blockage and dead zones by simple bluff-body reasoning, but no fan-specific quantification exists — this is the single largest evidence gap for this condition.
4. No patents specifically target furnishing-aware fan behaviour; the closest art is generic blade-noise-reduction patents (riblets, serrations, winglets, splitter blades, active cancellation) that address the acoustic half only indirectly and generically.
5. No manufacturer in the market table markets a feature for this condition — it is white space, but mostly because the underlying aerodynamic effect has not been measured or published, not because it has been tried and found unimportant.

**Open questions / what could not be found:**
- Quantified % change in air delivery or occupant-level velocity between carpeted and hard-floor rooms under an operating ceiling fan — not found, likely unstudied.
- Porosity/pressure-drop coefficients for typical Indian curtain fabrics under fan-driven airflow — not found.
- Any India-specific statistic on the prevalence of carpets/rugs vs hard flooring in Indian homes — not found (only general claims that vitrified tile dominates).
- Verified patent bibliographic data (assignee, priority date, legal status, jurisdiction) for the shortlisted patents — not obtainable from search snippets; needs a direct Google Patents/Espacenet/InPASS session.
- Any CFD study using rough-wall boundary conditions to represent carpet under a ceiling fan — not found.

---

## Sources

- [CBE Fans Guidebook — Ceiling fans](https://cbe-berkeley.gitbook.io/fans-guidebook/full-guidebook/ceiling-fans)
- [CBE Fans Guidebook — Case studies for researchers](https://cbe-berkeley.gitbook.io/fans-guidebook/full-guidebook/case-studies-for-researchers)
- [CBE Fans Guidebook — Fan options and key characteristics](https://cbe-berkeley.gitbook.io/fans-guidebook/practitioner-summary/fan-options-and-key-characteristics)
- [Ceiling fan air speeds around desks and office partitions (eScholarship PDF)](https://escholarship.org/content/qt3pq2j9mh/qt3pq2j9mh_noSplash_f340ee940d7072e92c55ab3be91ca070.pdf)
- [Spatial Uniformity of Thermal Comfort from Ceiling Fans (eScholarship PDF)](https://escholarship.org/content/qt5fs9q6fq/qt5fs9q6fq.pdf)
- [Ceiling-fan-integrated air conditioning: airflow and temperature characteristics (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0360132320300184)
- [Ceiling-fan-integrated air-conditioning: thermal comfort evaluations (Buildings & Cities journal)](https://journal-buildingscities.org/articles/10.5334/bc.137)
- [Big Ass Fans — Design Guide](https://learn.bigassfans.com/design-guide)
- [Carpet Institute Australia — Acoustic Benefits of Carpet](https://www.carpetinstitute.com.au/residential/carpet-noise-pollution-reduction/)
- [Mass Loaded Vinyl Direct — Hard vs Soft Materials Acoustics Guide](https://massloadedvinyldirect.com/guides/hard-vs-soft-materials-acoustics/)
- [JJ Flooring Group — How Flooring Affects Acoustic Performance (PDF)](https://www.jjflooringgroup.com/wp-content/uploads/Acoustic_White_Tech_Paper_FINAL.pdf)
- [CurtainsUK — Do curtains really help keep the draft out?](https://www.curtainsuk.com/blogs/news/do-curtains-really-help-keep-the-draft-out)
- [Alibaba product insights — How to stop curtains from blowing in the wind](https://www.alibaba.com/product-insights/how-to-stop-your-curtains-from-blowing-in-the-wind-with-simple-fixes.html)
- [JK Cement — Flooring Guide for Indian Homes](https://www.jkcement.com/blog/flooring-solution/flooring-guide/)
- [Houzz India — Which tiles are perfect for Indian floors](https://www.houzz.in/magazine/which-tiles-are-perfect-for-indian-floors-stsetivw-vs~86143723)
- [vsctimes.com — Atomberg vs Crompton BLDC Fan](https://vsctimes.com/atomberg-vs-crompton-bldc-fan/)
- [vsctimes.com — 5 Best BLDC Fans in India 2026](https://vsctimes.com/best-bldc-fans/)
- [BEE Star Label — Schedule 8 for Ceiling Fans (PDF)](https://www.beestarlabel.com/Content/Files/Schedule8-CF.pdf)
- [Bijli Bachao — New BEE Star Rating Standards for Ceiling Fans](https://www.bijlibachao.com/fans/new-beee-star-rating-standards-ceiling-fans.html)
- [Alephindia — BEE Star Ratings for Electric Ceiling Fans IS 374](https://alephindia.in/bee-star-ratings-for-electric-ceiling-fans-is-374.php)
- [US7494325B2 — Fan blade with ridges (Google Patents)](https://patents.google.com/patent/US7494325B2/en)
- [US20060110257A1 — Ceiling fan blade (Google Patents)](https://patents.google.com/patent/US20060110257)
- [US20070154314A1 — Reduction of tonal noise using splitter blades (Google Patents)](https://patents.google.com/patent/US20070154314)
- [US20050147496A1 — Fan with reduced noise generation (Google Patents)](https://patents.google.com/patent/US20050147496)
- [US20030095864A1 — Fan with reduced noise (Google Patents)](https://patents.google.com/patent/US20030095864A1/en)
- [US5388956A — Fan assembly and method for reducing fan noise (Google Patents)](https://patents.google.com/patent/US5388956)
- [US5448645A — Active fan blade noise cancellation system (Google Patents)](https://patents.google.com/patent/US5448645A/)
- [US4511310A — Ceiling fan blade isolation (Google Patents)](https://patents.google.com/patent/US4511310A/en)
- [US6776578B2 — Winglet-enhanced fan (Google Patents)](https://patents.google.com/patent/US6776578B2/en)
- [US12180976 — Ceiling fan airflow diffuser apparatus (USPTO PDF)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12180976)
