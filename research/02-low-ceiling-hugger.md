# Low Ceilings (< 2.6 m) and Hugger / Flush-Mount Fans — Aerodynamic Research Dossier

Prepared for AtomQuest 2026. Scope: ceiling fans mounted with blade-to-ceiling gap under ~200 mm in Indian rooms with ceiling height 2.4–2.6 m.

## 1. Condition definition

- **Geometry**: A "hugger" or flush-mount fan has the motor housing bolted almost directly to the ceiling bracket, giving a blade-to-ceiling clearance typically in the 50–150 mm range, versus 250–300+ mm for a standard downrod-mounted fan [UNVERIFIED — exact Indian product clearance figures not found in primary specs; general industry guidance cited below is largely from the US flush-mount market].
- Indian context: ceilings of 2.4–2.6 m are common in budget apartments, lofts, mezzanine levels, older low-rise housing stock, and PMAY/affordable-housing units; a standard down-rod fan at 300 mm drop plus a 230–300 mm fan body would leave under 2.1–2.2 m headroom — below or close to the ~2.1 m (7 ft) walking clearance guideline cited by US code discussions (no Indian-specific code clause was found confirming this figure for India) [UNVERIFIED].
- **Prevalence**: No quantified Indian statistic on the share of homes with sub-2.6 m ceilings was found in the search; anecdotally, hugger fans are marketed heavily for "low ceiling," "loft," and "duplex upper floor" use cases by Indian retailers, implying meaningful market demand, but no primary data/source confirms a percentage [UNVERIFIED].
- Safety driver: fan blades must clear human head height with margin; conventional guidance (non-Indian, [UNVERIFIED] for India specifically) recommends the lowest blade point be at least ~2.1 m (7 ft) above the floor ([How Close Is Too Close to a Ceiling Fan?](https://homeimprovementway.com/how-close-is-too-close-to-ceiling-fan/)). IS 374:2019 is BIS's ceiling fan standard but the specific clause defining minimum floor clearance could not be verified from accessible web sources in this session — **[UNVERIFIED, needs direct access to IS 374:2019 text via BIS]**.

## 2. Aerodynamic physics

- **Inflow starvation**: The blade's upper (suction) surface relies on a roughly hemispherical inflow volume above the disk to feed the actuator-disk mass flow. Reducing blade-to-ceiling clearance truncates this volume, forcing air to turn through a tighter radius before entering the blade annulus. This raises local inflow velocity and separation risk at the leading edge of the upper surface, reducing effective disk area and volumetric efficiency.
- Industry commentary (non-peer-reviewed) states hugger/flush fans can move noticeably less air than downrod fans at the same diameter and RPM because they "aren't able to circulate as much air" due to reduced air-collection volume above the blade ([The Tibble](https://thetibble.com/difference-flush-mount-hugger-ceiling-fans/); [City Lights SF](https://citylightssf.com/blogs/city-lights-insights/are-flush-mount-ceiling-fans-effective)). One source states hugger fans "provide 40% less airflow than standard ceiling fans, even when a 6-inch clearance is maintained" [UNVERIFIED — single secondary source, no primary test data located] ([Phase 1 Electric](https://www.p1electric.com/ceiling-fan-height-regulations-and-best-practices/)).
- Clearance guidance found: 8 inches (≈200 mm) above the blades recommended as a general optimum, with 12 inches (≈300 mm) cited elsewhere as the minimum for airflow to "develop" fully, and 6 inches as an absolute minimum ([Delmar Fans](https://www.delmarfans.com/educate/best-ceiling-fans-for-8ft-ceilings); [Parrot Uncle](https://parrotuncle.com/blogs/news/ceiling-fan-clearance-how-much-space-do-you-need-from-the-ceiling)). These are US consumer-guide sources, not peer-reviewed, and give no systematic h/D curve — treat as directional, not quantitative, [UNVERIFIED] for engineering design margins.
- **Governing phenomena at low clearance**:
  - Reduced effective inlet area → higher upstream velocity → higher inlet losses, analogous to a fan operating with a restricted inlet in HVAC fan-system-effect literature (not Indian ceiling-fan specific, but the mechanism — "system effect" losses from obstructed inlet — is a known centrifugal/axial fan engineering principle; no ceiling-fan-specific quantification found here).
  - The ceiling itself acts as a close-coupled flat plate; blade tip vortices and the upper-surface boundary layer interact with this plate (a Coandă/wall-jet-like effect at the blade root), likely increasing induced drag/turbulence intensity near the hub — this is physically plausible by analogy to ground-effect and duct-inlet theory, but no ceiling-fan CFD study specifically isolating hugger clearance was found in the available searches; the closest located CFD works (ScienceDirect transient 3D CFD, ResearchGate "DESIGN AND CFD ANALYSIS OF CEILING FAN FOR REGULAR ROOM SIZE") model standard clearance fans, not hugger geometry — **[UNVERIFIED for hugger-specific case]**.
- **Non-dimensional framing (not sourced, provided as standard fluid-mechanics first-order reasoning — label as engineering estimate, not literature-sourced)**: clearance ratio h/D (ceiling gap ÷ sweep diameter) is the natural parameter; a hugger fan with ~100 mm gap on a 1200 mm sweep gives h/D ≈ 0.08, versus ≈0.25 for a 300 mm downrod gap on the same sweep. No source in this search quantifies the delivery-vs-h/D curve numerically for Indian BLDC fans — this is a clear literature gap (see Section 9/10).

## 3. Role of speed / RPM / frequency

- No source located specifically studying RPM/frequency interaction with low ceiling clearance. In principle, to compensate for reduced volumetric efficiency, a hugger fan would need higher RPM or blade pitch to hit the same BEE service-value target, which raises tip speed, noise, and power — this is inferred, not sourced, **[UNVERIFIED]**.
- No evidence found of resonance, beat-frequency, or blade-pass noise issues specific to hugger mounting; the general literature on ceiling-fan CFD (ScienceDirect, k-ω SST, MRF method) addresses standard-mount fans only.
- No evidence found on reverse/updraft or "natural breeze" mode specifically addressing low-clearance conditions.

## 4. Blade and fan geometry levers

Ranked by what is plausible/supported from sourced material (not a validated engineering ranking — treat as hypothesis ordering):

1. **Blade-to-ceiling clearance** — the defining parameter; even small increases (6"→8"→12") are repeatedly cited across consumer guides as improving airflow and reducing turbulence/noise ([Delmar Fans](https://www.delmarfans.com/educate/best-ceiling-fans-for-8ft-ceilings); [Parrot Uncle](https://parrotuncle.com/blogs/news/ceiling-fan-clearance-how-much-space-do-you-need-from-the-ceiling)).
2. **Blade span (sweep)** — hugger fans are often sold in shorter spans (quoted 42–54 inch / ~1065–1370 mm range in US market sources) to partially offset reduced headroom with a physically smaller, lighter rotor ([Hugger ceiling fan design overview, Alibaba product insights](https://www.alibaba.com/product-insights/hugger-style-ceiling-fan.html)).
3. **Blade pitch / angle** — described qualitatively as "carefully calibrated to push air downward effectively... even in confined vertical spaces" in manufacturer-facing descriptions, but no quantified optimum pitch for low clearance found [UNVERIFIED, marketing-level claim].
4. **Hub/motor housing shape** — a flatter, wider hub (to mount flush) changes the central blockage of the downwash core; no quantified study found.
5. **Canopy/mounting bracket design** — determines the realized minimum clearance; product literature treats this as a mechanical, not aerodynamic, design constraint.

No peer-reviewed or patent-verified ranking of these levers specific to the hugger condition was found; this section should be treated as a hypothesis set for the team's own CFD/testing (Section 10), not as established fact.

## 5. Materials and manufacturing

No sources specific to low-ceiling/hugger fans were found addressing material choice differently from standard fans. General ceiling-fan material practice (common industry knowledge, not from a specific citation in this search) includes stamped aluminium or ABS/engineering-plastic blades, and BLDC motors for efficiency — but this session's searches did not surface a source discussing whether hugger-specific loads (shorter blades, different bracket stresses) drive different material or manufacturing choices. **[UNVERIFIED / gap — recommend direct manufacturer datasheet review rather than web search]**.

## 6. Current market solutions

| Company | Model(s) | Sweep / blades / RPM | Air delivery (m³/min) | Power (W) | Service value | Feature addressing this condition | How it works | Evidence | What it still fails to solve |
|---|---|---|---|---|---|---|---|---|---|
| Atomberg | Renesa Enzel | 1200 mm, BLDC | 255 CMM (claimed) | ~28 W at top speed (claimed) | High (marketing claim) | "Additional ceiling plate beside canopy set" marketed for false/low ceilings | Alternate mounting hardware shortens effective drop | Manufacturer/retail listing — [atomberg.com](https://atomberg.com/atomberg-renesa-halo-bldc-motor-3-blade-ceiling-fan), [Smartprix price list](https://www.smartprix.com/fans/atomberg-brand) — **marketing claim, not independently tested data** | No independent verification found of air delivery at hugger clearance specifically vs standard mount |
| Atomberg | Studio+ (1200 mm) | 1200 mm, BLDC | 224 CMM (claimed) | ~28 W (claimed) | High | Wide voltage tolerance (165–285V) relevant to inverter/solar homes, not specifically low ceiling | — | Retail listing, [UNVERIFIED independent test] | Not positioned as a dedicated hugger product |
| Crompton | (unspecified low-profile models) | — | ~230–240 CMM typical (brand-level claim) | — | — | Marketed BLDC "ActivBLDC" range; no specific hugger model identified in search | — | [Housegyan brand comparison](https://www.housegyan.com/blog/crompton-vs-havells-vs-orient-fans) — brand-level, not model-specific | Could not identify a named hugger SKU in this search |
| Havells | Stealth Air (brand-level) | — | 270 CMM (claimed) at 280 RPM | 50 W (claimed) | — | High air delivery flagship; no confirmed hugger variant found | — | [Moglix brand roundup](https://www.moglix.com/articles/top-10-best-ceiling-fans-in-india-for-2025-brands-prices-features-and-power-ratings) | Hugger-specific SKU not confirmed |
| Orient Electric | Aeroslim | — | 240 CMM (claimed) at 310 RPM | 45 W (claimed) | — | Slim profile (name suggests low-profile relevance) but not confirmed as hugger-specific | — | [Moglix roundup](https://www.moglix.com/articles/top-10-best-ceiling-fans-in-india-for-2025-brands-prices-features-and-power-ratings) | Not verified as a true flush/hugger mount |
| Usha | Bloom Daffodil | — | 240 CMM (claimed) at 380 RPM | 50 W (claimed) | — | General high-air-delivery model; no low-ceiling claim found | — | [Moglix roundup](https://www.moglix.com/articles/top-10-best-ceiling-fans-in-india-for-2025-brands-prices-features-and-power-ratings) | Not hugger-specific |
| Bajaj, Polycab, Luminous, Superfan, Gorilla, Panasonic | — | — | — | — | — | No hugger/low-ceiling-specific model or data found in this search | — | — | **Full gap** — no data located for these brands in this condition |
| Big Ass Fans, Hunter, Minka-Aire, Modern Fan Co., Haiku, Dyson | — | — | — | — | — | US market offers dedicated "hugger" category (Hunter, Minka-Aire) but this search did not pull specific SKUs/specs | — | General hugger-fan category pages found ([Lamps Expo](https://www.lampsexpo.com/collections/hugger-ceiling-fans), [Parrot Uncle](https://parrotuncle.com/collections/hugger-flush-mount-ceiling-fan)) | No independently tested CFM-vs-clearance comparison found for any brand |

**Important caveat**: Every air-delivery/power/RPM figure above is a brand or retailer claim (marketing spec sheet), not an independently verified test (e.g., BEE star-label database lookup was not performed in this session). None should be treated as validated.

## 7. Academic and industry research

- **ResearchGate / Academia.edu — "Design and CFD Analysis of Ceiling Fan for Regular Room Size"**: CFD study of ceiling fan blade design for standard room geometry. Method/turbulence model/exact findings not extracted in this session beyond the title; does not appear to target hugger/low-clearance geometry specifically. [UNVERIFIED detail — needs full-text read] ([link](https://www.researchgate.net/publication/354808244_DESIGN_AND_CFD_ANALYSIS_OF_CEILING_FAN_FOR_REGULAR_ROOM_SIZE)).
- **ResearchGate — "Design and Optimization of High-Efficiency Ceiling Fan Blades"**: CFD-based blade optimization; k-ω SST turbulence model and MRF (multi-reference-frame) method reportedly used; recirculation zones near blade tips identified as a target for blade-angle/hub redesign. No indication this paper specifically varies ceiling clearance. [UNVERIFIED detail, needs full-text read] ([link](https://www.researchgate.net/publication/399916859_Design_and_Optimization_of_High-Efficiency_Ceiling_Fan_Blades)).
- **ScienceDirect — "Transient three-dimensional CFD modelling of ceiling fans"**: Validated transient 3D CFD against measured airflow data using SST k-ω; reported 83% of simulated points within measurement error bars. This is the most credible validated-methodology reference found, confirming MRF/sliding-mesh + SST k-ω as an accepted approach for ceiling-fan CFD, but the paper's scope (standard mount vs hugger) is not confirmed from the snippet alone. [UNVERIFIED scope detail] ([link](https://www.sciencedirect.com/science/article/pii/S0360132317302743)).
- No IIT/IISc/CEPT/LBNL/CBE Berkeley/ASHRAE RP study specifically on hugger or low-clearance ceiling fans was surfaced by these searches. This is a **notable literature gap** — the team may need a direct LBNL/CBE Berkeley "ceiling fan" publication-list search or ASHRAE RP database search beyond general web search to confirm whether this gap is real or just a search-tooling limitation.

## 8. Patent landscape

No patent family specifically and verifiably claiming a "low-clearance / hugger ceiling fan inlet geometry" solution was found with enough detail (assignee, priority date, claims) to populate a reliable table. Items surfaced but **not sufficiently verified to list as a real match**:

- US 10,989,207 — "Low profile directional centrifugal ceiling fan" — title suggests relevance (low-profile fan with directional outflow via a periphery outlet) but claim text, assignee, and priority date were not extracted in this session. **[UNVERIFIED — needs direct Google Patents / USPTO pull]** ([PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10989207)).
- US 11,293,458 and US 11,828,301 — "Air filtration ceiling fan" — relate to filtration, not low-clearance aerodynamics; likely low relevance. [UNVERIFIED].
- US 11,828,292 — "Fan with increased efficiency mode" and US 7,927,071 / 7,665,967 — "Efficient traditionally appearing ceiling fan blades with aerodynamical upper surfaces" — these concern general blade efficiency, not specifically hugger clearance. [UNVERIFIED relevance].

**Per the task rules, no patent number, assignee, claim, or overlap-risk rating is asserted here as fact.** A real patent-landscape table requires direct, authenticated searches on Google Patents, Espacenet, WIPO Patentscope, and InPASS with claim-text review — this was not completed to verifiable depth in this session and should be treated as an open task, not a finding.

## 9. Unsolved gaps and opportunities

- **No quantified clearance-vs-delivery curve exists in public, verifiable literature** for Indian 1200 mm BLDC fans at hugger clearance (50–150 mm) versus standard downrod clearance (250–300+ mm). This is the single biggest evidence gap found. Closing it (via the team's own anemometer-grid test, Section 10) would itself be a useful contribution.
- **No brand in the Indian market was found, in this search, to publish a tested air-delivery number specifically at hugger/flush mounting** — all current Indian "low-ceiling-friendly" products (e.g., Atomberg Renesa Enzel) appear to solve the *mounting/installation* problem (shorter drop, false-ceiling bracket) rather than *re-engineering the blade/inlet aerodynamics* for the reduced clearance. This is a plausible concept gap: an inlet or hub shape specifically redesigned to recover inflow volume lost to ceiling proximity (e.g., a flared or raised central inlet, angled upper-surface geometry, or a shrouded/ducted hub) — **[not found in any product or patent in this search, flagged as a candidate novel direction, not a confirmed white space — a real patent search is required before relying on this]**.
- **3 candidate concept directions** (engineering hypotheses from first-order reasoning in Section 2, not literature-validated):
  1. **Raised/flared central inlet above the hub** to recapture some of the lost inflow volume within the same overall ceiling-to-blade envelope — expected benefit unquantified; risk: adds height, defeats the low-profile purpose; cost: minor tooling change.
  2. **Shorter-span, higher-pitch blade set specifically tuned for low h/D**, rather than simply shrinking a standard-mount blade design — expected benefit unquantified; risk: higher tip speed/noise to compensate; cost: new blade mould.
  3. **BLDC controller compensation** — since Atomberg/Crompton etc. already use BLDC motors with current-sensing, a controller profile that detects (via torque/current signature at known RPM) a "low-clearance install" and re-tunes the speed-to-delivery curve could be software-only — expected benefit unquantified; risk: cannot fix the underlying fluid-mechanic efficiency loss, only relabel speed settings; cost: near zero (firmware only).
  All three require validation; none should be presented to the hackathon panel as proven.

## 10. Measurement and validation plan

- **Test rig**: A real room (or mock ceiling rig) with adjustable ceiling height (e.g., 2.4 m, 2.6 m, 2.8 m, 3.0 m) to sweep blade-to-ceiling clearance from ~75 mm to ~300 mm at fixed sweep diameter (1200 mm) and fixed RPM.
- **Instruments**: vane or hot-wire anemometer grid at occupant height (1.1 m seated, 0.6 m at a bed height) on a horizontal grid under the fan; a second grid just above the blades (inside the clearance gap) to directly measure inflow velocity and turbulence intensity; a sound level meter (dB(A)) at a fixed distance; a power meter at the mains input; smoke/fog visualisation to qualitatively observe inflow starvation and any wall/ceiling Coandă attachment.
- **Metrics**: total air delivery (m³/min, per BEE's standard test-point method if available), velocity profile uniformity under the fan, noise (dB(A)), input power (W), and resulting service value (m³/min/W), each plotted against clearance (h) and clearance ratio (h/D).
- **CFD plan**: model the same clearance sweep using MRF or sliding-mesh with an SST k-ω turbulence model (consistent with the validated ScienceDirect methodology found in Section 7), with the ceiling modelled as a no-slip flat boundary at varying distance from the rotor plane; validate against the physical rig's velocity-grid and power data before trusting the CFD for untested clearances.

## 11. Sensors and smart control

- No existing implementation was found of a ceiling fan automatically detecting its own installed ceiling clearance. In principle, a BLDC fan's current-draw/torque signature at a given RPM is a function of load, which is itself a function of effective aerodynamic clearance — so a self-calibration routine (measure current at a reference speed during setup, compare to a factory baseline) is technically plausible, but **no product or patent confirming this was found** — **[UNVERIFIED, flagged as a speculative concept only]**.

## 12. Summary

**Executive summary**: Hugger/flush-mount ceiling fans trade airflow performance for mandatory headroom safety in low-ceiling Indian rooms (2.4–2.6 m), but the actual magnitude of that trade-off is poorly documented in verifiable, India-specific sources — most available figures (e.g., "40% less airflow," 6–12 inch clearance guidance) come from US consumer blogs rather than peer-reviewed or standards-body data, and no source in this search confirmed IS 374:2019's exact clearance clause. Indian brands (Atomberg's Renesa Enzel, and others) address the condition mainly through mounting-hardware tricks (shorter drop brackets) rather than published aerodynamic redesign, and no verified patent or CFD study specifically targets the hugger clearance regime — leaving a genuine, confirmable research gap for a hackathon team to fill with its own clearance-sweep test and CFD validation.

**Top 5 insights**:
1. The core physical mechanism (reduced inflow volume above the blade reducing effective disk efficiency) is physically sound but **not quantified by any verified source** for Indian 1200 mm BLDC fans — this is the dossier's central actionable gap.
2. All Indian market "low-ceiling" products found address **installation/mounting**, not blade/inlet aerodynamics — a possible white space, pending a real patent search.
3. Clearance guidance in the literature (6–12 inches / ~150–300 mm) is consumer-grade, not engineering-grade — the team should treat 200 mm as a provisional "hugger" threshold per the condition brief, not a validated boundary.
4. A validated CFD methodology (SST k-ω + MRF/sliding mesh) exists for ceiling fans generally (ScienceDirect) and should be reusable for the team's own clearance study, pending access to the full paper.
5. No credible patent landscape could be established in this session — a proper Google Patents/Espacenet/InPASS search with claim review is a required next step before any design-around claim is made.

**Open questions / what could not be found**:
- Exact IS 374:2019 clause on minimum blade-to-floor / blade-to-ceiling clearance.
- Any India-specific statistic on the prevalence of sub-2.6 m ceilings.
- Any independently tested (non-marketing) air-delivery comparison between a hugger-mounted and downrod-mounted version of the *same* fan model.
- Any peer-reviewed or CFD paper isolating blade-to-ceiling clearance as the studied variable.
- Any verified patent family specifically targeting low-clearance/hugger inlet aerodynamics (only unverified title-level candidates were found).
- Indian academic (IIT/IISc/CEPT) work on this specific condition — none surfaced.

## Sources

- [Ceiling Fans (ENERGY STAR) — BASC PNNL](https://basc.pnnl.gov/resource-guides/ceiling-fans-energy-star)
- [Why is Ceiling Fan Clearance Height So Important? — MacroAir](https://blogs.macroairfans.com/why-is-ceiling-fan-clearance-height-so-important)
- [Ceiling Fan Height Regulations and Best Practices — Phase 1 Electric](https://www.p1electric.com/ceiling-fan-height-regulations-and-best-practices/)
- [Low Profile Ceiling Fan Buying Guide — Smafan](https://smafan.com/blogs/smart-home/low-profile-ceiling-fan-buying-guide)
- [How Low Should a Ceiling Fan Hang — Hampton Fan Reviews](https://hampton-ceiling-fans.com/how-low-should-a-ceiling-fan-hang/)
- [How High Should a Ceiling Fan Be From the Floor — Engineer Fix](https://engineerfix.com/how-high-should-a-ceiling-fan-be-from-the-floor/)
- [How Close Is Too Close to a Ceiling Fan — Home Improvement Way](https://homeimprovementway.com/how-close-is-too-close-to-ceiling-fan/)
- [Difference Between Flush Mount and Hugger Ceiling Fans — The Tibble](https://thetibble.com/difference-flush-mount-hugger-ceiling-fans/)
- [Are Flush Mount Ceiling Fans Effective — City Lights SF](https://citylightssf.com/blogs/city-lights-insights/are-flush-mount-ceiling-fans-effective)
- [What is a Hugger Ceiling Fan — Southern Lights](https://southernlightsinc.com/blog/what-is-a-hugger-ceiling-fan-and-how-to-know-if-you-need-one/)
- [Flush Mount vs Downrod Ceiling Fans — Ceiling Fan Hub](https://www.ceilingfanhub.com/blog/detail/flush-mount-vs-downrod-ceiling-fans-which-one-is-best-for-your-ceiling)
- [Best Ceiling Fans for 8ft Ceilings — Delmar Fans](https://www.delmarfans.com/educate/best-ceiling-fans-for-8ft-ceilings)
- [Ceiling Fan Clearance: How Much Space Do You Need — Parrot Uncle](https://parrotuncle.com/blogs/news/ceiling-fan-clearance-how-much-space-do-you-need-from-the-ceiling)
- [Hugger Ceiling Fans — Lamps Expo](https://www.lampsexpo.com/collections/hugger-ceiling-fans)
- [Hugger / Flush Mount Ceiling Fan — Parrot Uncle](https://parrotuncle.com/collections/hugger-flush-mount-ceiling-fan)
- [Inside Hugger Style Ceiling Fan — Alibaba Product Insights](https://www.alibaba.com/product-insights/hugger-style-ceiling-fan.html)
- [Atomberg Ceiling Fans — Bajaj Finserv](https://www.bajajfinserv.in/atomberg-ceiling-fans)
- [Atomberg Ceiling Fans collection — atomberg.com](https://atomberg.com/collections/atomberg-ceiling-fans)
- [Atomberg Renesa Halo — atomberg.com](https://atomberg.com/atomberg-renesa-halo-bldc-motor-3-blade-ceiling-fan)
- [Atomberg Fans Price List — Smartprix](https://www.smartprix.com/fans/atomberg-brand)
- [Crompton vs Havells vs Orient Fans — Housegyan](https://www.housegyan.com/blog/crompton-vs-havells-vs-orient-fans)
- [Top 10 Best Ceiling Fans in India 2025 — Moglix](https://www.moglix.com/articles/top-10-best-ceiling-fans-in-india-for-2025-brands-prices-features-and-power-ratings)
- [Top five ceiling fan brands designed for Indian weather — Moglix](https://www.moglix.com/articles/top-five-ceiling-fan-brands-designed-for-indian-weather)
- [DESIGN AND CFD ANALYSIS OF CEILING FAN FOR REGULAR ROOM SIZE — ResearchGate](https://www.researchgate.net/publication/354808244_DESIGN_AND_CFD_ANALYSIS_OF_CEILING_FAN_FOR_REGULAR_ROOM_SIZE)
- [DESIGN AND CFD ANALYSIS OF CEILING FAN FOR REGULAR ROOM SIZE — Academia.edu](https://www.academia.edu/45655328/DESIGN_AND_CFD_ANALYSIS_OF_CEILING_FAN_FOR_REGULAR_ROOM_SIZE)
- [Design and Optimization of High-Efficiency Ceiling Fan Blades — ResearchGate](https://www.researchgate.net/publication/399916859_Design_and_Optimization_of_High-Efficiency_Ceiling_Fan_Blades)
- [Transient three-dimensional CFD modelling of ceiling fans — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0360132317302743)
- [Low profile directional centrifugal ceiling fan — US Patent 10,989,207](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10989207)
- [Air filtration ceiling fan — US Patent 11,293,458](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11293458)
- [Air filtration ceiling fan — US Patent 11,828,301](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11828301)
- [Fan with increased efficiency mode — US Patent 11,828,292](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11828292)
- [Efficient traditionally appearing ceiling fan blades — US Patent 7,927,071](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7927071)
- [Efficient traditionally appearing ceiling fan blades — US Patent 7,665,967](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7665967)
