# Condition 21 — Tall Wardrobes, Shelves and Furniture Along Walls: Ceiling-Fan Aerodynamics Dossier

**Condition:** Floor-to-ceiling wardrobes, lofts and storage units that block the wall-climb return path on one or more sides of a room, producing a choked recirculation loop, uneven return flow and stagnant zones.

---

## 1. Condition definition

A ceiling fan's room-scale circulation depends on a complete loop: downward jet → floor impingement/spreading → **upward return along the walls** → re-entrainment at ceiling level back into the fan's inlet (the "fan jet / impingement / spreading / wall-zone / still-air zone" five-zone model described by Gao et al., 2017 — see Section 2). Indian bedrooms commonly line one or two walls with **floor-to-ceiling wardrobes** (typically 2.0–2.4 m tall, 0.55–0.65 m deep), open or closed lofts above cupboards, and bookshelves. This condition occurs where such storage physically intercepts the wall zone, i.e. where the upward-return air stream would otherwise rise.

- No BIS/IS 374:2019 clause addresses furniture-blocked return paths specifically; IS 374:2019 is a safety/performance (air delivery, power, service value, insulation) test standard for the free-standing fan, not an installed-room standard [UNVERIFIED — could not verify a specific installation clearance clause in IS 374:2019 text itself; see Section 1a].
- **How common in India:** Floor-to-ceiling wardrobes along one or two bedroom walls are extremely common in urban Indian apartments (modular/carpenter-built almirahs are near-universal in 1BHK/2BHK bedrooms), and lofts above are standard in kitchens and storage rooms. No national survey quantifying "% of Indian bedrooms with wall-to-wall wardrobes" was found in this search — this prevalence estimate is **[UNVERIFIED]**, based on general real-estate/interior-design trade commentary rather than a cited dataset.

### 1a. Typical geometry parameters (for later sections)
- Wardrobe height: 2.0–2.4 m (near full ceiling height of 2.6–3.2 m)
- Wardrobe depth from wall: 0.55–0.65 m
- Fraction of room perimeter typically occupied by wardrobe walls in a bedroom: often 1 full wall (≈25–35% of perimeter) up to 2 walls (≈45–60%) in compact apartments — **[UNVERIFIED]**, no cited survey found; stated as a reasoned estimate from common floor-plan practice.

---

## 2. Aerodynamic physics

### 2.1 The baseline (unobstructed) flow model
The best available quantitative baseline for this exact topic is a controlled chamber study from UC Berkeley's Center for the Built Environment (CBE): **Gao, Zhang, Arens et al., "Ceiling fan air speeds around desks and office partitions," *Building and Environment* 124 (2017) 412–440**, open-access at eScholarship (https://escholarship.org/uc/item/3pq2j9mh). It is the most directly relevant peer-reviewed, instrumented study found, though it models **desks/partitions**, not wardrobes — its findings are used here as the best physical analogue, flagged where extrapolated.

The paper proposes a **five-zone flow model** for a ceiling fan in a room:
1. **Fan jet** (the descending cylindrical column, confined within ~the blade diameter until ~0.6 m above the floor)
2. **Floor impingement zone** (stagnation/redirection as the jet hits the floor; impingement region radius ≈0.22H per the Beltaos–Rajaratnam turbulent-jet-impingement model, H = fan height above floor; measured impingement height ≈0.14H)
3. **Outward spreading zone** along the floor, 0.3–0.5 m deep
4. **Upward-flowing wall zone** — air rises along the wall after spreading outward, closing the loop back toward the ceiling and the fan's inlet
5. **Still-air zone** — the bulk of the room volume above floor level and away from the fan column, with only slow net upward motion (≈0.15–0.3 m/s outside the jet)

**This is the zone that tall wardrobes interrupt.** A full-height wardrobe sitting flush against a wall physically occupies the "upward-flowing wall zone," forcing the rising return air to detour around, over, or in front of the furniture face rather than hugging the wall.

### 2.2 Governing phenomena in the wardrobe-obstructed case
- **Choked return loop / inflow starvation:** With the wall-zone return path blocked by a flush, floor-to-ceiling solid surface, the air that would normally rise along the wall and re-enter the fan's upper inlet must find an alternate path — either further out into the room (widening the still-air zone) or around the ends of the wardrobe run, concentrating return flow at the room's open walls/corners. The CBE study shows analogous behaviour with furniture obstacles (tables/partitions): adding a solid obstacle near the floor **redirects the jet's spreading flow laterally rather than letting it continue radially outward**, and the obstacle "forced [the jet] to spill outward" over/around itself — the measured air speed and "corrective power" (cooling-equivalent metric) **increase in some newly-redirected regions and are suppressed in the blocked direction** (Case 5: "the downward jet in the occupied region to the west of the table suppresses the spread there," while regions to the north/south, where air was diverted, saw enhanced spread).
- **Stagnant zones:** The narrow gap between a tall wardrobe face and the adjacent still-air zone becomes a low-momentum dead pocket — consistent with the paper's general finding that the "still air zone" has only ~0.15–0.3 m/s net upward motion even without obstruction; a wardrobe reduces momentum further in its lee.
- **Asymmetric/uneven recirculation:** Where a wardrobe occupies only one or two walls (not all four), the obstructed-side circulation is pushed to use the open-wall sides preferentially, making the room's flow field asymmetric even when the fan is centred — directly analogous to the Case 5 vs Case 6 contrast in the CBE study, where blocking one return path (linear partition) diverted flow to the ends, and blocking two sides (corner partition) **concentrated and made airflow at occupant level MORE uniform within the open quadrant** ("the corner partition created the most uniform air speed in the workstation for all heights except at 1.7 m").
- **Ground/wall effect interaction:** Because the wardrobe is a vertical solid plane from floor to ceiling (not a mid-height table), it most resembles a "wall extension" rather than a floor obstacle — it primarily affects zones 3–4 (spreading + wall return), with less direct effect on the jet core itself (zone 1) unless the wardrobe also narrows the inlet-side clearance (see Condition 07, near-wall mounting, for a related but distinct effect on the *fan's own inlet*, which is governed separately).
- **Coandă-type attachment:** A flush wardrobe face presents a smooth vertical surface the rising return flow can attach to (Coandă effect), which may partially restore an attached wall-jet-like return path along the wardrobe face itself, rather than a full stagnation — this is a plausible mechanism but was **not found quantified in literature for this specific geometry; [UNVERIFIED]**.

### 2.3 First-order equations / non-dimensional numbers
- **Jet impingement scaling (Beltaos & Rajaratnam, used by Gao et al.):** impingement-zone radius ≈ 0.22·H; impingement height ≈ 0.14·H, where H = fan mounting height above floor (H ≈2.3 m gave radius ≈0.5 m, height ≈0.3 m in the CBE chamber test — directly measured and matched the empirical model).
- **Threshold air speed for perceptible fan cooling:** 0.3 m/s is used by Gao et al. and ASHRAE Standard 55 context as the lowest speed that both penetrates the body's natural convective plume and is distinctly perceptible as cooling.
- **Clearance/blockage ratio:** No fan-specific non-dimensional "wall-furniture blockage ratio" was found in the literature search; the general fan-engineering obstruction literature (industrial fan inlet-obstruction guidance, e.g. Qpedia/QATS) states obstruction effect "is directly correlated to the size of the obstruction" but gives no universal formula for ceiling fans. **[UNVERIFIED]** for a specific quantified ceiling-fan wardrobe-blockage % formula.
- **Richardson/Archimedes number:** Not directly relevant to this condition (isothermal flow assumption; thermal stratification interactions are covered in Condition 13, not this brief).

### 2.4 Quantified effects from literature
| Parameter | Measured effect | Source / confidence |
|---|---|---|
| Jet/floor spreading radius with no furniture | 0.7–1.2 m radius (coverage ≥0.3 m/s threshold), growing as height drops from 1.7 m to 0.6 m | Gao et al. 2017, Table 1 (measured) |
| Spreading radius with table obstacle under/near jet | Increases to 0.9–1.5+ m on open side, up to ~40% larger than base case in some directions | Gao et al. 2017, Tables 2–3 (measured) |
| Peak air speed at 0.6 m (mid-body height) at 0.6 m from fan centre | 0.3 m/s (no obstacle, Case 1) → 0.6–1.0+ m/s (with table/partition diverting flow, Cases 2–6) | Gao et al. 2017 §3.2 (measured) |
| Corner-partition (2-side blockage) vs linear (1-side blockage) occupant-level uniformity | Corner blockage gave the *most uniform* air speed in the open quadrant of all 6 tested cases | Gao et al. 2017 §3.6 (measured) |
| False-ceiling presence (different but related obstruction case) | ~37% lower average airflow vs. no false ceiling | Cited in search-result summary of obstruction literature; **[UNVERIFIED — could not open primary source to confirm exact study and methodology]** |
| Wall-clearance efficiency rule-of-thumb (fan-to-wall, not furniture-specific) | ≥24″ (≈0.6 m) ≈100% efficiency; 18″≈92%; 12″≈70%; <12″ <50% | Industry/installation-guide figures (non-peer-reviewed); **[UNVERIFIED — consumer-advice source, not a cited test report]** |

No study was found that directly measures "% air-delivery loss vs. % of room perimeter blocked by floor-to-ceiling wardrobes." This is a genuine literature gap (see Section 9).

---

## 3. Role of speed / RPM / frequency

- The CBE chamber study tested fan levels 2, 4 and 6 (70.5–175 RPM on a 1524 mm Haiku fan) for the **unobstructed** case and found the **spatial flow pattern (peak/hollow locations) was essentially invariant with speed** — only the magnitude scaled. This suggests (by extension, not directly tested) that the *qualitative* effect of a wardrobe-blocked wall zone — redirected return flow, altered uniformity — would persist in **pattern** across speed settings, with only the magnitude of velocity in the diverted zones scaling with RPM. This inference is **reasoned extrapolation, not directly tested for the furniture case — [UNVERIFIED]**.
- No evidence was found of resonance, beat-frequency or blade-pass-tone issues specifically arising from wall-furniture blockage (as opposed to blade-obstruction proximity, which is Condition 05's territory). **[UNVERIFIED — no literature found]**.
- Reverse/updraft mode could theoretically reduce the dependence on a clear wall-zone return path, since updraft mode draws air up through the room centre and pushes it outward near the ceiling rather than relying on floor-level spreading and wall climb — but no study was found testing updraft mode specifically against wall-furniture blockage. **[UNVERIFIED — plausible but unverified hypothesis]**.

---

## 4. Blade and fan geometry levers

Ranked by expected relevance to *this specific condition* (not overall fan performance):

1. **Sweep diameter relative to room width** — a smaller sweep leaves a larger still-air margin before furniture is even reached, reducing dependence on a long-throw wall return; a larger sweep pushes the spreading zone right up to the wardrobe face, maximizing the interaction (and the potential gain from fixing it). [Reasoned from the zone model, not directly tested for this trade-off — UNVERIFIED for quantified optimum.]
2. **Downrod length / blade-to-ceiling clearance** — affects jet throw distance to the floor (H in the impingement formula) but is not the primary lever for a *wall-return* blockage; secondary relevance.
3. **Number of blades / blade pitch / twist** — affects jet strength and swirl, which in turn affects how strongly the jet's spreading flow is deflected when it does interact with furniture (per the Case 4a/4b swirl-direction finding in Gao et al. — swirl direction changes which side of an obstacle receives more deflected flow); a design lever but secondary to placement.
4. **Tip shape / winglets** — affects tip-vortex strength and jet coherence; no literature link found to furniture-blocked return paths specifically. **[UNVERIFIED relevance to this condition]**.
5. **Canopy/hub shape, motor housing** — minor; affects the fan's own inlet clearance (Condition 02/07 territory), not the room-level return path this condition targets.

No source was found ranking these levers specifically *for the furniture-blocked-wall case* — the ranking above is this report's reasoned synthesis from the general zone-flow physics, not a literature-sourced ranking. **Flagged as [UNVERIFIED] ranking.**

---

## 5. Materials and manufacturing

This section is not strongly differentiated by the wardrobe/furniture condition specifically (material choice does not change how the room-level recirculation loop behaves). Standard ceiling-fan blade materials remain relevant for general performance:
- Blade materials: stamped aluminium sheet, ABS/ASA/PP injection-moulded composites, glass-fibre-reinforced nylon — chosen for stiffness-to-weight ratio, balancing tolerance, surface finish (affects dust adhesion, tangential to Condition 20) and cost.
- No material-selection guidance specific to wall-furniture-blocked rooms was found in this search. **[UNVERIFIED — no condition-specific material literature found]**.

---

## 6. Current market solutions

No manufacturer marketing material, datasheet or test report found in this search explicitly addresses "fan designed for rooms with floor-to-ceiling wardrobes/blocked wall return." This is a genuinely under-addressed condition in current market communication — companies market "smart," "BLDC," "high air delivery" fans generically, not furniture-aware designs.

| Company | Model(s) | Sweep / blades / RPM | Air delivery (m³/min) | Power (W) | Service value | Feature addressing this condition | How it works | Evidence | What it still fails to solve |
|---|---|---|---|---|---|---|---|---|---|
| Atomberg | Renesa Elite (BLDC) | 1200 mm, 3-blade | ~230 CMM | 35 W | ~6.6 (derived, declared ~8.2 per a 2024 test report for a related model) | None specific — general high air delivery / BLDC speed control via remote | BLDC motor, electronic speed control | Atomberg product pages; third-party test report (5.imimg.com, 2024) — **marketing + 1 test report, not independently verified by this research** | No furniture/wall-blockage-aware airflow adaptation found |
| Crompton | Energion Hyperjet (BLDC) | 1200 mm | ~220 CMM | 26 W | High (BEE 5-star range) | None specific | ActivBLDC motor | Crompton marketing copy (secondary source) | Same — no furniture-aware feature found |
| Havells | "Stealth"/BLDC range | 1200 mm | — | 28–35 W | BEE-rated | Low-noise focus, not placement-aware | BLDC motor | Havells marketing (secondary) | No wall/furniture adaptive feature found |
| Orient | Aero series | 1200 mm | High among peers (claimed) | — | — | Silent operation claim | Aerofoil blades | Orient marketing (secondary) | No furniture-aware feature found |
| Usha | — | 1200 mm | — | — | — | Energy efficiency claim | — | Usha marketing (secondary) | No furniture-aware feature found |
| Bajaj, Polycab, Luminous, Superfan, Gorilla, Panasonic | — | — | — | — | — | — | — | **Not found in this search round — would need dedicated follow-up per brand** | — |
| Big Ass Fans / Haiku | Haiku L | 1524 mm | — | 2–16 W (6 speed levels) | — | Installation guidance: minimum 1 m (3 ft) clearance from walls/obstructions, 15.4% of diameter ceiling clearance ("starvation distance") | Published installation/design guide specifies clearance to avoid "starvation" but is a **general wall clearance rule, not wardrobe-specific** | Big Ass Fans installation guide (bigassfans.com); used as the test fan in the Gao et al. 2017 CBE study | Guidance addresses the *fan's own* clearance, not room-level furniture-blocked return paths |
| Hunter, Minka-Aire, Modern Fan Co., Dyson | — | — | — | — | — | — | — | Not found in this search round | — |

**Overall market finding:** No manufacturer (Indian or global) was found marketing a feature that explicitly compensates for a furniture-blocked wall-return path. All identified "feature" claims are either (a) general wall-clearance installation advice (treating the *fan's* inflow, not the room's return loop) or (b) unrelated efficiency/noise/smart-control claims. This gap is itself a Section 9 finding.

---

## 7. Academic and industry research

| Study | Method | Setup | Main quantified finding | Limitations |
|---|---|---|---|---|
| Gao, Zhang, Arens, Present, Ning, Zhai, Pantelic, Luo, Zhao, Raftery, Liu — "Ceiling fan air speeds around desks and office partitions," *Building and Environment* 124 (2017) 412–440 | Experimental — 5-anemometer vertical "tree" (0.1, 0.6, 0.75, 1.1, 1.7 m heights), 7×6 or 13×6/8 grid, 30 cm spacing, isothermal chamber, fog/incense flow visualisation | 5.49×5.49×2.53 m chamber, 1524 mm Haiku ceiling fan, 6 table/partition configurations (no furniture, table under fan, table at edge/corner, table+linear partition, table+corner partition) | Established the 5-zone flow model; quantified how obstacles **redirect, not just reduce**, fan-driven airflow — corner-blocking produced the most uniform occupant-level air speed of all tested cases | Uses **desks and partitions, not floor-to-ceiling wardrobes** — partition height tested (1.4 m) is well below ceiling (2.53 m), so does NOT fully occupy the wall-zone return path the way a true floor-to-ceiling wardrobe would. Single fan, single room geometry, isothermal (no thermal buoyancy). This is the closest available analogue, not a direct study of this condition. |
| Ho, et al. (CFD study referenced in search results) | Numerical CFD, 2D/3D | Room with AC, ceiling fan, and a standing person | Investigated obstruction effects on airflow/heat transfer | Variable tested was fan speed, not obstacle location — **[could not access full paper in this search round; details UNVERIFIED beyond the secondary summary]** |
| Scheatzle et al. (cited in Gao et al.'s literature review) | Experimental, thermal comfort study with desks | Room with desks | Took air-speed measurements to place subjects, but did not quantitatively report them | Not usable for quantified obstruction data per Gao et al.'s own characterization |
| Beltaos & Rajaratnam (jet impingement theory, cited by Gao et al.) | Analytical/empirical, circular turbulent impinging jets | General jet-on-flat-surface | Impingement zone height ≈0.14H, radius ≈0.22H | Generic jet theory, not fan-specific; used as a validation check by Gao et al. and found to match their measurements well |

**Gap explicitly stated by the authors themselves (2017):** "We are not aware of any studies that evaluate the effects of obstacle *location* on the air speed profiles... Obstacle effects on comfort cooling have also not been reported in the literature" (at time of writing) — and ASHRAE TC 216 was, as of that paper, only beginning to develop fan-placement testing standards. No more recent (2018–2026) study specifically on floor-to-ceiling wall furniture was found in this search round. **[This is the single most load-bearing finding of Section 9 — literature gap confirmed by the field's own leading researchers.]**

### CFD methodology notes (general, not condition-specific)
- MRF (Multiple Reference Frame) vs sliding mesh: MRF is cheaper and commonly used for steady-state ceiling-fan CFD; sliding mesh needed for transient/wake-interaction detail. Specific turbulence-model/mesh guidance for the wardrobe-blocked case was not found in this search round. **[UNVERIFIED]**.

---

## 8. Patent landscape

No patent specifically claiming "ceiling fan compensating for furniture-blocked wall-return airflow" was found in this search round. Below are the closest-matching patents found via Google Patents search; **all core-mechanism/claim summaries should be independently re-verified against the full patent text before any product/IP decision** — treat as a starting list, not a legal clearance.

| Patent no. | Assignee | Priority date | Jurisdiction | Legal status | Core mechanism | Relevance to this condition | Overlap risk | Design-around idea | Link |
|---|---|---|---|---|---|---|---|---|---|
| US9638209B1 | [UNVERIFIED — not confirmed from search snippet] | [UNVERIFIED] | US | [UNVERIFIED] | Trailing-edge "air dam"/spoiler on blade to redirect turbulent flow downward | Low–Medium — redirects blade-level flow, not room-level wall-return path | L | Different mechanism (room-level sensing vs blade spoiler) | https://patents.google.com/patent/US9638209B1/en |
| US20060210401A1 | [UNVERIFIED] | [UNVERIFIED] | US | [UNVERIFIED] | Blade angle-of-attack optimisation root-to-tip; dihedral for wider downward air divergence | Low — widens the jet's spread footprint generally, not wall-zone specific | L | N/A | https://patents.google.com/patent/US20060210401 |
| US11111930 | [UNVERIFIED] | [UNVERIFIED] | US | [UNVERIFIED] | Asymmetric flat-bottom airfoil (semi-symmetric about chord) to increase downward flow volume | Low–Medium — asymmetric blade could in principle be tuned to push more air toward the open (non-wardrobe) side of a room, but no such application claimed | L–M | Possible design-around: electronically-controlled yaw/tilt rather than fixed asymmetric airfoil | https://patents.google.com/patent/US11111930 |
| US10302094 | [UNVERIFIED] | [UNVERIFIED] | US | [UNVERIFIED] | Pivoting blade-tip attachments adjustable to a set angle of incidence to redirect airflow to a "desired location" | **Medium** — this is the closest conceptual match: user/installer-adjustable airflow redirection, which could be aimed away from a wardrobe-blocked side | M | A sensor-driven automatic version (vs. this patent's apparently manual/fixed adjustment) could design around it | https://patents.google.com/patent/US10302094 |
| WO2015095753A1 | [UNVERIFIED] | [UNVERIFIED] | WO (PCT) | [UNVERIFIED] | Interactive occupant-tracking fan — sensors direct airflow toward a detected target/occupant | Low–Medium — occupant-tracking logic *could* be adapted to "furniture-map-aware" airflow direction, but as described it targets people, not static obstructions | L | Different sensing target (static room geometry vs occupant) | https://patents.google.com/patent/WO2015095753A1/en |
| US7711659B2 | [UNVERIFIED] | [UNVERIFIED] | US | [UNVERIFIED] | Adaptive fan management system with thermal sensing | Low — general adaptive control, not furniture/wall-blockage specific | L | N/A | https://patents.google.com/patent/US7711659B2/en |

**This is far short of the requested 10–20 family count.** A full patent-landscape pass requires dedicated searches on Espacenet, WIPO Patentscope and Indian Patent Office InPASS, which were **not queried in this research round** (only Google Patents, via general web search, was accessed). **Flag: patent section is incomplete and should be treated as a preliminary scan only — recommend a dedicated patent-search follow-up before any design-around or freedom-to-operate conclusion.**

---

## 9. Unsolved gaps and opportunities

- **Core gap:** No product, standard, or (as of this search) post-2017 peer-reviewed study directly quantifies how a floor-to-ceiling wardrobe occupying part of a room's perimeter changes occupant-level air delivery, uniformity, or comfort. The closest analogue (Gao et al. 2017) used short partitions (1.4 m, well below a 2.5 m ceiling) and tables, not full-height wardrobes — so even the best available data under-represents how completely the wall-return path is blocked in the real Indian-bedroom case.
- **Why the gap exists:** likely a mix of (a) low perceived "aerodynamic glamour" of a placement/furniture problem vs. blade/motor R&D, (b) difficulty of generalizing "furniture configuration" into a standard test protocol, (c) BIS/BEE testing is done in an empty/standardised chamber (free-air, unobstructed) by definition, so it structurally cannot capture this effect, and (d) the asymmetric, room-specific nature of furniture placement makes it hard to design one fixed product feature that solves it. **[Reasoning here is this report's synthesis, not a cited explanation.]**
- **Size of the gap:** Given the CBE study showed occupant-level air speed at mid-body height roughly **doubling to tripling** (0.3 m/s → 0.6–1.0+ m/s) purely from redirected flow around a *partial, low-height* obstacle, a full-height wardrobe blocking one or two walls plausibly has an even larger redirection effect on where airflow concentrates versus stagnates — but the magnitude for a full-height case is **not quantified in any source found; this is the single clearest "we don't know" flag in this dossier.**

### Concept directions for an aerodynamics-led team
1. **Asymmetric / directional blade pitch or electronically-skewed thrust vector** aimed away from the furniture-blocked side, set at install time (dip-switch/app configuration during setup, user selects "wardrobe wall: north"). *Mechanism:* bias the jet's spreading-zone skew (as seen passively in Gao et al.'s swirl-direction Case 4a/4b finding) toward the open side of the room. *Expected benefit:* plausibly restores occupant-level uniformity closer to the open-room baseline — **magnitude unquantified, needs lab validation**. *Risk:* added complexity/cost for BLDC controller; may reduce coverage on the blocked side entirely. *Novelty vs patents:* appears to sit in a gap relative to the Medium-overlap-risk US10302094 (pivoting blade tips) — a fixed-pitch/electronically-biased approach rather than mechanical tip adjustment may design around it, but needs legal confirmation.
2. **Variable/dual rotation direction exploiting swirl-direction asymmetry.** Mechanism: Gao et al.'s Case 4a/4b showed swirl direction changes which table edge receives more deflected airflow; a reversible-rotation BLDC fan could let the installer or an auto-calibration routine pick the rotation sense that biases flow toward the open wall. *Expected benefit:* low-cost (software-only, since most BLDC fans already support reverse/updraft mode) — **magnitude unquantified**. *Risk:* minimal; *Cost impact:* near zero (existing hardware). *Novelty:* likely low patent risk since it reuses existing reverse-rotation hardware in a new control logic.
3. **Smart wall-sensing / auto-placement-aware speed-zoning** — ultrasonic or IMU/current-draw-based "room mapping" at commissioning (fan briefly operates at a few speeds while a simple app-paired sensor or manual input records where walls/furniture are) feeding into an adaptive speed/swirl profile. *Mechanism:* combine Section 11 sensing ideas with concept 1/2 control logic. *Expected benefit:* unquantified, this is the most novel but highest-R&D-cost direction. *Risk:* significant added BOM cost and complexity for average consumer. *Novelty:* Medium — occupant-tracking patent (WO2015095753A1) is adjacent but targets people, not static furniture; a furniture/wall-mapping variant appears less crowded.
4. **Vented/perforated wardrobe-top or gap-leaving installation guidance** — not a fan redesign at all, but a labelled installation/CAD guideline (e.g., "leave 100–150 mm air gap between wardrobe top and ceiling") that Atomberg could publish as a value-added install-guidance feature bundled with the product (QR code / app tip). *Mechanism:* restores a partial wall-return path without any blade/motor change. *Expected benefit:* plausibly large relative to cost (near-zero R&D) but **completely unquantified — this is a hypothesis, not a tested finding**. *Risk:* depends on carpenters/installers actually following guidance; *Cost impact:* ~zero product cost, pure documentation/marketing play. *Novelty:* not patentable as a physical product feature, but could be a differentiator via app/AR room-planning tools.
5. **Oval/elongated or dual-smaller-fan layouts biased toward open walls** for rooms with wardrobes on 2+ sides — overlaps with Condition 09 (long narrow rooms) and Condition 08 (multi-fan) territory; flagged as a cross-condition concept worth exploring in the Part B follow-up synthesis (S1) prompt.

All five concepts above are this report's own reasoned proposals in response to the prompt's instruction to suggest concept directions — **they are not drawn from a specific cited source** describing these exact concepts, and all quantified-benefit claims are marked unverified pending lab/CFD testing (Section 10).

---

## 10. Measurement and validation plan

Closely following the validated methodology of Gao et al. (2017), adapted for a full-height wardrobe:

- **Test setup:** A room (or scaled chamber) with one or two walls fitted with a true floor-to-ceiling wardrobe mock-up (plywood/MDF panel, full height, 0.55–0.65 m deep), vs. a no-furniture baseline, vs. partial-height partition baseline (to compare against the 2017 study's partition case and isolate the effect of *full* vs *partial* height blockage).
- **Instruments:**
  - Vertical "tree" of 4–5 omnidirectional low-speed anemometers (hot-sphere/hot-wire or equivalent, accuracy ≥±0.02 m/s or 1% of reading, per the CBE study's Sensor Inc. units) at heights matching ASHRAE 55 comfort-standard points: 0.1 m, 0.6 m, 1.1 m, plus 1.7 m and a table/bed-height point as relevant.
  - Smoke/fog generator for qualitative flow visualisation of the wall-zone deflection around the wardrobe face.
  - Sound meter (dB(A)) to check whether deflected flow near the wardrobe edge creates audible turbulence/whoosh.
  - Power meter at the fan to log W and confirm BEE-declared service value is unaffected by room layout (it shouldn't be — power draw is a motor/blade property, not a room property — but worth confirming no load-related RPM sag).
- **Grid:** 30 cm spacing grid as in Gao et al., extended to 2× blade radius from fan centre in all directions, with denser sampling near the wardrobe face and at the open-wall "escape" zones.
- **Metrics to report:** mean air speed by height and position, "corrective power" (cooling-equivalent °C metric, as defined in Gao et al.'s cited reference), coverage area at the 0.3 m/s threshold, and a computed **uniformity index** (e.g. coefficient of variation of occupant-height air speed across the occupied zone) comparing wardrobe-present vs baseline.
- **CFD comparison:** Model the same geometry (MRF rotor model, k-ω SST or similar turbulence closure commonly used in ceiling-fan CFD per the earlier-cited studies — **specific best-practice guidance for this exact case not found in this search, [UNVERIFIED]**) and validate against the physical measurements before using CFD alone to explore wardrobe height/depth/coverage-percentage sensitivity sweeps.

---

## 11. Sensors and smart control

- **IMU/current-draw sensing:** Used elsewhere in fan literature for wobble/imbalance detection (Condition 28 territory); no evidence found of current-draw or IMU being used to infer *room furniture layout*. **[UNVERIFIED — no existing implementation found]**.
- **Ultrasonic distance sensing:** Plausible mechanism for a fan to "map" wall/furniture distance asymmetrically (similar in principle to robot-vacuum wall-following sensors), which could feed a directional-bias control strategy (Concept 3, Section 9). No existing ceiling-fan product using ultrasonic room-mapping was found in this search. **[UNVERIFIED — no existing implementation found; this remains a greenfield opportunity]**.
- **Occupancy sensing:** WO2015095753A1 (interactive occupant-tracking fan, Section 8) is the closest existing implementation, but it targets people, not static furniture geometry — a meaningfully different sensing/control problem.
- **Overall assessment:** smart sensing for furniture-aware airflow control appears to be an **open, unaddressed niche** in both the patent and product literature found in this search round.

---

## 12. Summary

**Executive summary:** Floor-to-ceiling wardrobes along one or two bedroom walls — a near-ubiquitous feature of Indian apartment bedrooms — physically block the "wall-return zone" that closes a ceiling fan's room-scale recirculation loop. No peer-reviewed study was found that tests this exact geometry; the best available analogue (Gao et al. 2017, UC Berkeley CBE, *Building and Environment*) used shorter desks/partitions and found that even partial, low-height obstacles **redirect** airflow dramatically — roughly doubling to tripling occupant-level air speed in some zones while suppressing it in others — with a corner (two-side) blockage producing the *most uniform* occupant-level airflow of all tested configurations, a counter-intuitive and directly usable finding. No manufacturer (Indian or global) was found marketing a feature that explicitly addresses furniture-blocked wall-return paths, and the patent landscape search (preliminary, Google Patents only) found no close match — making this a genuinely open opportunity space for an aerodynamics-led design team, best pursued through either passive design guidance (installation gap recommendations) or active directional/sensing control, both requiring new physical testing since no existing dataset directly answers the question.

**Top 5 insights, ranked:**
1. The 5-zone flow model (jet / impingement / spreading / wall-return / still-air) from Gao et al. (2017) is the correct physical framework for this condition, and furniture blockage acts specifically on zone 4 (wall return).
2. Obstacles don't just reduce airflow — they **redirect** it, sometimes *increasing* occupant-level air speed in adjacent open zones (measured 2–3× increase at mid-body height in the closest analogue study).
3. Blocking **two** adjacent sides (corner case) produced **better** occupant-level uniformity than blocking one side (linear case) in the one directly relevant controlled experiment found — a non-obvious, testable, and currently unexploited design insight.
4. No standard (IS 374:2019, BEE/BIS testing) captures this condition because certification testing is inherently done in an unobstructed free-air setting — meaning any product gain here would be a genuine differentiator not visible in a spec-sheet comparison.
5. The patent landscape (as far as searched) is **not crowded** for furniture/wall-blockage-aware airflow control specifically — the closest patents (pivoting blade tips, occupant tracking) target adjacent but distinct problems, suggesting room for a design-around.

**Open questions / what could not be found:**
- No direct quantitative study of full-height (floor-to-ceiling) wardrobe blockage on ceiling-fan air delivery/uniformity — the central data gap.
- No Indian-specific survey data on prevalence of wall-to-wall wardrobes in Indian bedrooms.
- No complete patent-family landscape (only a shallow Google Patents pass was done; Espacenet, WIPO Patentscope and InPASS were not queried in this round).
- No data on noise effects (dB(A)) of deflected flow against a wardrobe face.
- No CFD best-practice reference validated specifically for this obstruction geometry.
- Full company-by-company specs for Bajaj, Polycab, Luminous, Superfan/Versa Drive, Gorilla, Panasonic, Hunter, Minka-Aire, Modern Fan Co., Dyson were not retrieved in this search round and remain to be filled in.

---

## Sources

- Gao, Y., Zhang, H., Arens, E., Present, E., Ning, B., Zhai, Y., Pantelic, J., Luo, M., Zhao, L., Raftery, P., Liu, S. (2017). "Ceiling fan air speeds around desks and office partitions." *Building and Environment*, 124, 412–440. https://escholarship.org/uc/item/3pq2j9mh (open access, read in full for this report)
- CBE Ceiling Fan Design Guide, Paul Raftery and David Douglass-Jaimes, UC Berkeley Center for the Built Environment: https://cbe.berkeley.edu/wp-content/uploads/2020/04/CBE-Ceiling-Fan-Design-Guide-V0.pdf (fetch attempt failed to extract text; cited indirectly via search summary — [UNVERIFIED primary read])
- CBE Fans Guidebook, "Ceiling fans": https://cbe-berkeley.gitbook.io/fans-guidebook/full-guidebook/ceiling-fans
- Big Ass Fans / Haiku installation and design guides: https://bigassfans.com/docs/haiku/haiku/haiku-standard-install-guide.pdf ; https://learn.bigassfans.com/design-guide
- DESIGN AND CFD ANALYSIS OF CEILING FAN FOR REGULAR ROOM SIZE: https://www.researchgate.net/publication/354808244_DESIGN_AND_CFD_ANALYSIS_OF_CEILING_FAN_FOR_REGULAR_ROOM_SIZE and https://iaeme.com/MasterAdmin/Journal_uploads/IJMET/VOLUME_11_ISSUE_4/IJMET_11_04_004.pdf
- Transient three-dimensional CFD modelling of ceiling fans, ScienceDirect: https://www.sciencedirect.com/science/article/pii/S0360132317302743
- Qpedia / QATS, "How Obstruction Affects [fan performance]": https://www.qats.com/Qpedia-Article/Qpedia_Jun10_How_Obstruction_affects_the_performance_of_a_fan
- US9638209B1, Google Patents: https://patents.google.com/patent/US9638209B1/en
- US20060210401A1, Google Patents: https://patents.google.com/patent/US20060210401
- US11111930, Justia Patents: https://patents.justia.com/patent/11111930
- US10302094 (ceiling fan blade attachment, pivot control): referenced via USPTO image search (image-ppubs.uspto.gov); not independently re-confirmed via Google Patents in this session — **[UNVERIFIED link reliability]**
- WO2015095753A1, Google Patents: https://patents.google.com/patent/WO2015095753A1/en
- US7711659B2, Google Patents: https://patents.google.com/patent/US7711659B2/en
- BEE star rating / service-value thresholds for ceiling fans: https://www.crompton.co.in/blogs/fans-guide/mandatory-bee-star-rating-for-ceiling-fans-india-s-revolutionary-step-towards-energy-conservation ; https://bldcfans.in/guides/bee-star-rating-ceiling-fans — figures reported as m³/min/W thresholds; **[secondary/trade sources, not the primary BEE schedule document itself — recommend verifying against beestarlabel.com or the official BEE notification before quoting externally]**
- Atomberg product pages (Renesa Elite, Renesa Halo, Ikano, 1400mm range): https://atomberg.com/products/atomberg-renesa-elite-bldc-motor-3-blade-ceiling-fan ; https://atomberg.com/collections/1400mm-ceiling-fan — **marketing material, not independently verified test data**
- Atomberg Anrio BLDC third-party test report (2024): https://5.imimg.com/data5/ANDROID/Doc/2025/8/534299569/VM/VC/YX/18593599/atomberg-anrio-bldc-pdf.pdf — **[UNVERIFIED — not opened/confirmed in this session, cited only via search-summary snippet]**
- Crompton, Havells, Orient, Usha comparison commentary (secondary/trade source, not datasheets): https://www.housegyan.com/blog/crompton-vs-havells-vs-orient-fans ; https://proudlymadeinindia.com/havells-vs-crompton/ — **marketing/trade-blog claims, explicitly not verified test data**
- IS 374:2019 BIS certification overview (secondary compliance-consultancy sources, not the IS standard text itself): https://evtlindia.com/isi-mark/bis-certification-for-electric-ceiling-type-fans-is-374-2019 ; https://corpbiz.io/learning/bis-certification-for-electric-fans/ — **[UNVERIFIED — primary IS 374:2019 standard document was not accessed in this session]**

**Note on completeness:** This dossier was produced from a single research session using web search and a small number of full-document fetches (notably the Gao et al. 2017 paper, read in full). It should be treated as a solid first pass anchored on one strong primary source, not an exhaustive literature/patent review. The most actionable next step is a dedicated, deeper patent search (Espacenet/WIPO/InPASS) and, ideally, commissioning the Section 10 physical test, since no existing study directly measures this exact condition.
