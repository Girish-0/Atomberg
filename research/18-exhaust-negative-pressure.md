# Ceiling Fan Aerodynamics in Negative-Pressure Rooms (Kitchen/Bathroom Exhaust Fans, Chimneys)

*AtomQuest 2026 evidence dossier — Condition 18: Exhaust fans and negative-pressure rooms*

## 1. Condition definition

**Geometry/parameters.** A kitchen or attached bathroom runs a dedicated extract device — a wall-mounted axial exhaust fan (per IS 3588:1987, "Electric Axial Flow Fans," and IS 2312:1967 for propeller-type ventilating fans) [UNVERIFIED — exact current applicability of IS 2312 vs IS 3588 to modern products not independently confirmed] or a kitchen chimney/hood — while a ceiling fan runs in the same or an adjoining room. Typical Indian residential exhaust devices pull **200–400 CFM (≈340–680 m³/h)** for kitchens and **50–110 CFM (≈85–185 m³/h)** for bathrooms ([MrHomes CFM guide](https://www.mrhomes.in/blogs/guide/exhaust-fan-cfm-calculator-guide), [Home-Run exhaust fan comparison](https://home-run.co/blogs/homerun-knowledge-base/best-exhaust-fans-india-comparison)). Indian kitchen chimneys are commonly rated **≥1200 m³/h** ([Homestyler sizing guide](https://www.homestyler.com/article/floorplanner/how-to-choose-and-size-kitchen-exhaust-fans-for-indian-homes)). The target metric is kitchen air-change rate of **10–15 ACH** (enclosed) or **8–12 ACH** (semi-open) ([MrHomes](https://www.mrhomes.in/blogs/guide/exhaust-fan-cfm-calculator-guide)).

When extract flow exceeds the make-up air entering through doors/windows/gaps, the room (and often the flat) goes into **negative static pressure** relative to outdoors/adjacent spaces, driving infiltration through every leakage path — door undercuts, window gaps, duct penetrations, and, relevantly, back through the ceiling-fan room if doors are open. US mechanical codes (IMC §505, NFPA 96 §8.3.1) require make-up air above 400 CFM and cap negative pressure at 0.02 in w.c. ([Energy Vanguard](https://www.energyvanguard.com/blog/range-hood-makeup-air-the-basics/), [Streivor Design Guide 2](https://www.streivor.com/wp-content/uploads/2020/11/CKV-Design-Guide-2-Optimizing-Makeup-Air.pdf)); no equivalent mandatory Indian residential make-up-air code was found in this search [UNVERIFIED — no Indian code requiring make-up air for residential kitchen exhaust was located].

**Prevalence in India.** Kitchen and bathroom exhaust fans are near-universal in urban Indian apartments and increasingly common in independent houses; chimneys are now standard in mid-to-upper urban kitchens. No single published statistic on "fraction of Indian homes operating ceiling fan + kitchen exhaust simultaneously" was found [UNVERIFIED]. Qualitatively this is a **very high-frequency condition**: most Indian flats have a kitchen and an attached or nearby bathroom, each in near-constant competition for make-up air with whichever ceiling fans are running in adjoining rooms.

## 2. Aerodynamic physics

- **Pressure-driven short-circuit path.** A ceiling fan creates a closed recirculation loop (downwash core → floor spread → wall climb → ceiling return) only in a **pressure-neutral, sealed room**. When an adjoining space (kitchen/bathroom) is depressurized, the room with the ceiling fan becomes a net **source** of air leaving through the open door/gap toward the negative-pressure zone. This breaks the return-air loop: instead of recirculating back up to the fan's intake, part of the wall-climb air is diverted sideways toward the door/gap, is "short-circuited" out of the room, and is not available for re-entrainment — a well-documented general ventilation phenomenon termed **short-circuiting** between supply and exhaust paths ([PDHonline Kitchen Ventilation](https://www.pdhonline.com/courses/m228/m228content.pdf), [Air Quality Engineering – Kitchen Exhaust Facts](https://air-quality-eng.com/buyer-resources/articles/kitchen-exhaust-facts/)).
- **Reverse-flow / "obstruction" effect.** When an exhaust's induced suction pressure at a gap exceeds the discharge pressure the ceiling fan can sustain through that same opening, analysis of fan systems in series/parallel shows the weaker flow path can be forced into **reverse flow**, effectively turning what should be a supply path into part of the exhaust path; the rule of thumb cited is that if exhaust-induced velocity at a gap exceeds the local discharge velocity by **>20%**, reverse flow becomes likely ([Industrial Monitor Direct – Fan Pressure Conflict](https://industrialmonitordirect.com/blogs/knowledgebase/resolving-conflicting-fan-airflows-in-shared-exhaust-systems)). A ceiling fan's downwash is not a ducted discharge, so this 20% figure is for ducted-fan systems generally and is **not validated for an open-room ceiling-fan-vs-exhaust-fan case** [UNVERIFIED for this specific geometry — flagged as an analogy, not a measured result].
- **Infiltration adds a horizontal crossflow component.** As make-up air is drawn in through door/window gaps toward the negative-pressure kitchen/bathroom, it behaves like the cross-ventilation draft described in jet-in-crossflow theory (see also Condition 19 in this series): the ceiling fan's vertical downwash jet is deflected toward the depressurized zone, reducing floor-level coverage on the side away from the draft and increasing it on the near side, analogous to general jet-in-crossflow deflection documented for ventilation jets ([PMC – jet ventilation in crossflow, mine spaces](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10997619/)).
- **Net ventilation benefit is still positive for contaminant removal.** A DOE/LBNL-adjacent multi-room test-house study found that **ceiling-fan-driven air mixing increased removal rates of ultrafine and >1 µm particles** released in the kitchen, compared to a no-mixing baseline, across ventilated/naturally-ventilated/"pull-inward" test conditions ([OSTI – Impact of Ceiling Fan and Room Air Cleaner on Air Mixing and Fate](https://www.osti.gov/pages/servlets/purl/2538429)). This suggests the fan can *help* kitchen exhaust effectiveness by homogenizing contaminant concentration even while its own local recirculation loop is disrupted — a genuine trade-off between "whole-room contaminant control" (helped) and "localized occupant comfort/coverage" (hurt).
- **Gas-appliance safety interaction (kitchen-specific).** Strong depressurization from an exhaust fan/chimney, if make-up air is insufficient, can pull combustion products from an open-flame gas appliance away from or even back toward the burner/flue, producing **flame disturbance, flicker, or in severe cases backdraft/flame rollout** pulling CO into the room ([CanRoHeat – Backdraft & Negative Pressure Homes](https://canroheat.ca/backdraft-and-negative-pressure-homes), [HypoAir – Negative Pressure Ventilation Dangers](https://hypoair.com/blogs/news/negative-pressure-ventilation-can-be-dangerous-in-your-home-how-to-prevent-it), [JASpector – IRC 2024 Backdrafting](https://www.jaspector.com/codes/irc-2024/ch17-combustion-air/backdrafting-combustion-safety-irc-2024/)). Most Indian LPG stoves are unflued/open-combustion, not vented through a chimney flue the way North American furnaces are, so classic "flue backdraft" is less directly applicable; the relevant risk in Indian kitchens is **local flame flicker/instability from cross-drafts** created by the combined exhaust-fan suction and any ceiling fan or door-driven airflow near the stove, not CO backdraft through a flue [UNVERIFIED — no India-specific LPG flame-disturbance study found; inference from general backdraft literature plus known open-combustion stove design].
- **Governing non-dimensional/physical quantities.**
  - **Volumetric balance:** Q_exhaust − Q_infiltration − Q_makeup ≈ 0 at steady state; the deficit sets room depressurization (commonly characterized in Pa or in. w.c., with NFPA 96 capping it at 0.02 in w.c. ≈ 5 Pa for commercial kitchens — residential has no equivalent Indian limit found).
  - **Discharge coefficient / orifice equation** for infiltration through gaps: Q = Cd·A·√(2ΔP/ρ), i.e., leakage flow driven by the square root of the pressure differential — meaning airflow "stolen" from a ceiling-fan room through an open door scales with √ΔP, not linearly.
  - **Velocity ratio** (jet velocity ÷ crossflow velocity) governs how far the ceiling-fan downwash is deflected before reaching the floor, by analogy with jet-in-crossflow theory (Condition 19 framework applies directly here with the crossflow driven by pressure rather than wind).
  - No Richardson/Archimedes-number or Reynolds-number data specific to this exact fan-exhaust interaction was found in the literature search; all such analysis above is inferred from adjacent fields (HVAC make-up air engineering, mine ventilation, cold-storage air curtains) and should be treated as **physically reasonable but [UNVERIFIED] for the specific ceiling-fan/kitchen-exhaust case**.

## 3. Role of speed / RPM / frequency

No study was found that specifically varies ceiling-fan RPM against a kitchen/bathroom exhaust-fan pressure differential and reports effect size [UNVERIFIED — gap]. Reasoned implications, clearly marked as inference:
- A **lower ceiling-fan speed** reduces the momentum of the downwash jet, making it more susceptible to deflection/short-circuiting by the pressure-driven crossflow from the negative-pressure zone — i.e., the "jet overpowers crossflow" condition is less achievable at low RPM.
- **Higher RPM** increases jet momentum/thrust (∝ RPM² in simple actuator-disk thrust scaling) and so better resists deflection, but does nothing to fix the loss of return-air recirculation caused by the open door/gap itself — the air leaving through that gap is permanently lost from the loop regardless of fan speed.
- No evidence of resonance, beat-frequency or blade-pass-tone interaction specifically from running a ceiling fan with a kitchen exhaust fan was found; this is a different noise mechanism from the self-contained tonal/vibration issues covered elsewhere in this research series. Reverse/updraft mode and "natural breeze" pulsed modes have no documented benefit or harm specific to this condition [UNVERIFIED].

## 4. Blade and fan geometry levers

Because the dominant effect here is **room-level pressure/flow topology**, not local blade aerodynamics, geometry levers rank lower in impact than for most other conditions in this series:
1. **Thrust/momentum headroom (sweep, pitch, RPM range)** — a fan capable of higher static thrust at the same noise/power budget better resists crossflow deflection from the depressurized adjoining room. Ranked highest because it's the only lever with a plausible, mechanism-based effect.
2. **Downrod length / blade-to-ceiling clearance** — affects how much of the ceiling-level return air is captured before being drawn toward an open door; shorter clearance to ceiling may marginally help by keeping the return loop tighter and more resistant to lateral drafts, but this is speculative [UNVERIFIED].
3. **Number of blades/chord/twist** — no specific interaction with pressure-driven crossflow identified; same general levers as calm-room operation apply.
4. **Directional/asymmetric blade design** — a concept only (see §9), not observed in any current product addressing this condition specifically.

## 5. Materials and manufacturing

No material or manufacturing factor specific to the exhaust/negative-pressure condition was identified in the search — this condition is a room-airflow-topology problem, not a materials problem. Standard ceiling-fan material considerations (aluminium/ABS/ASA blades, stamped vs injection-moulded manufacture, balancing tolerances) apply unchanged from baseline; kitchen/bathroom humidity and grease considerations are already covered by Conditions 16 and 20 in this series and are not duplicated here.

## 6. Current market solutions

No ceiling-fan or exhaust-fan product was found in this search that explicitly markets a feature "addressing ceiling-fan/kitchen-exhaust pressure interaction." The table below lists baseline specs of relevant exhaust and ceiling-fan products found; none claim to solve this specific condition.

| Company | Model(s) | Sweep/Type | Air delivery | Power | Feature addressing this condition | Evidence | What it still fails to solve |
|---|---|---|---|---|---|---|---|
| Havells | VentilAir DX 230 mm exhaust fan | 230 mm axial | ~280–300 CFM (≈475–510 m³/h) | ~40 W | None found | [Home-Run comparison](https://home-run.co/blogs/homerun-knowledge-base/best-exhaust-fans-india-comparison), [MrHomes guide](https://www.mrhomes.in/blogs/guide/ultimate-exhaust-fan-buying-guide-2026) | No make-up-air coordination with ceiling fans elsewhere in the home |
| Crompton | Brisk Air / Ventair 230 mm | 200–230 mm axial | 250–270 CFM | 46–50 W | None found | [Home-Run comparison](https://home-run.co/blogs/homerun-knowledge-base/best-exhaust-fans-india-comparison) | Same |
| Bajaj | Freshee / Maxima DX | 225 mm axial | 260 CFM | 46 W | None found | [Home-Run comparison](https://home-run.co/blogs/homerun-knowledge-base/best-exhaust-fans-india-comparison) | Same |
| Atomberg | Renesa+/Erica/Elite (BLDC ceiling fans) | 1200 mm, 3-blade | 225–235 CMM, 5★ BEE | 28–35 W | None marketed for this condition | [VSC Times BLDC roundup](https://vsctimes.com/best-bldc-fans/) | No pressure-adaptive control |
| Crompton | Energion Hyperjet (BLDC ceiling fan) | 1200 mm | 220 CMM | 26 W | None marketed for this condition | [VSC Times BLDC roundup](https://vsctimes.com/best-bldc-fans/) | No pressure-adaptive control |
| Havells | Glaze (BLDC ceiling fan) | 1200 mm | 225 CMM | — | None marketed for this condition | [VSC Times BLDC roundup](https://vsctimes.com/best-bldc-fans/) | No pressure-adaptive control |
| Global — commercial kitchen industry | Make-up-air units (various HVAC brands, e.g. Greenheck, Accurex, Streivor) | Ducted supply fans, not ceiling fans | Sized to match exhaust (100% of exhaust per code) | Varies | **Make-up air fans coupled to exhaust-hood interlocks** — directly solves the pressure imbalance, but is a separate ducted appliance, not a ceiling fan feature | [Greenheck – When is Make-Up Air Required](https://www.greenheck.com/resources/blog/when-is-make-up-air-required-for-kitchens), [Accurex white paper](https://www.accurex.com/blog/white-papers/when-make-up-air-is-required-for-commercial-kitchens) | Commercial-scale, ducted, not applicable to Indian residential retrofit without construction |

**Conclusion:** the engineering solution to this condition already exists and is standard practice in commercial kitchens (make-up air units interlocked with exhaust) but has **no residential, retrofit-friendly, ceiling-fan-integrated equivalent** in the Indian market. This is the core market gap (see §9).

## 7. Academic and industry research

| Source | Method | Main finding | Limitation |
|---|---|---|---|
| [OSTI/DOE — Impact of Ceiling Fan and Room Air Cleaner on Air Mixing and Fate](https://www.osti.gov/pages/servlets/purl/2538429) | Multi-room test house, tracer particles/gas released in kitchen, three ventilation modes (exhaust-on/ceiling-off, exhaust-off/ceiling-off, exhaust-off/ceiling-on "pull-inward") | Ceiling-fan mixing increased removal rate of ultrafine and >1 µm particles vs. no-mixing baseline | US test house, not Indian geometry/furniture density; exact % removal increase not stated in search excerpt — needs primary-source verification [UNVERIFIED numeric value] |
| [ScienceDirect — benefit of kitchen exhaust fan use after cooking](https://www.sciencedirect.com/science/article/pii/S0360132318301112) | Experimental, residential kitchen, post-cooking exhaust fan operation | Quantifies pollutant decay improvement with exhaust fan use (numbers behind paywall, not independently verified here) | [UNVERIFIED] — full text not accessed |
| [ScienceDirect — kitchen hoods vs. natural ventilation openings on IAQ](https://www.sciencedirect.com/science/article/abs/pii/S2352710224032893) | Field/experimental comparison | Natural ventilation openings (not hoods) were the primary driver of residual PM reduction | Paywalled; mechanism detail not independently verified [UNVERIFIED] |
| [Journal of Building Performance Simulation — Validated transient CFD study of ceiling-fan-induced airflow](https://www.tandfonline.com/doi/abs/10.1080/19401493.2026.2678829) | CFD comparison of Dynamic Remeshing, Sliding Mesh, Overset Mesh with 4 turbulence models (k-ε, RNG k-ε, SST k-ω, transition k-kl-ω) against experimental data | **SST k-ω gave the most consistent agreement with experiment** for ceiling-fan-induced flow — directly relevant CFD methodology recommendation for any simulation of this condition | Does not itself model an exhaust-fan crossflow/pressure case; methodology transfers, result does not |
| [PMC — Jet ventilation in crossflow, confined mine spaces](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10997619/) | Experimental jet-in-crossflow study, velocity ratio and jet diameter varied | Identifies two distinct "air lake" flow-field regimes depending on velocity ratio | Mine-ventilation geometry, not residential room; transferable as an analogy only |
| [ScienceDirect — 3-D effects of air curtain restricting cold-room infiltration](https://www.sciencedirect.com/science/article/pii/S0307904X06000849) | CFD + experiment, air curtain under external pressure/stack effect | Confirms air curtain jets are not 2-D: edges deflect under pressure differential (Coandă effect in center, stack-driven deflection at edges) | Cold-storage air-curtain geometry, not a ceiling fan; analogy for pressure-driven jet deflection only |

No IIT/IISc/CEPT-specific study on this exact ceiling-fan/exhaust-fan interaction was located in this search [UNVERIFIED — gap, worth a targeted follow-up search of IIT repositories/theses].

**Recommended CFD approach for this condition** (based on the validated methodology above): transient 3-D CFD with **SST k-ω turbulence closure**, sliding-mesh or MRF treatment of the rotating ceiling-fan blades, and a **pressure-outlet or velocity-inlet boundary condition representing the exhaust fan's extract rate** at the kitchen/bathroom opening, with a separate ambient-pressure inlet (door/window crack) sized to the real leakage area to capture the √ΔP infiltration relationship.

## 8. Patent landscape

No patent was found in this search that specifically addresses **ceiling-fan and kitchen/room-exhaust-fan aerodynamic interaction or negative-pressure compensation**. The closest adjacent patents found (general exhaust/kitchen ventilation, not ceiling-fan-specific) are listed for reference; none should be read as directly overlapping or directly design-around-relevant to a ceiling-fan concept, since none combine a ceiling fan with exhaust-pressure sensing/compensation.

| Patent no. | Assignee | Core mechanism | Relevance to this condition | Overlap risk | Link |
|---|---|---|---|---|---|
| US9574779B2 | [unspecified in search result] | Exhaust apparatus for enhanced capture/containment | Kitchen exhaust capture, not ceiling-fan interaction | L | [Google Patents](https://patents.google.com/patent/US9574779) |
| EP1674799A1 | [unspecified] | Exhaust hood design | Kitchen hood only | L | [Google Patents](https://patents.google.com/patent/EP1674799A1/en) |
| US6159093A | [unspecified] | Powered exhaust fan | Generic exhaust fan | L | [Google Patents](https://patents.google.com/patent/US6159093) |
| CN211950910U | [unspecified] | Kitchen exhaust fan utility design | Generic kitchen exhaust fan | L | [Google Patents](https://patents.google.com/patent/CN211950910U/en) |
| CN202228391U | [unspecified] | "Negative pressure fan" utility design | Negative-pressure-labeled fan, but mechanism/context unclear from search result [UNVERIFIED] | L–M (needs direct read) | [Google Patents](https://patents.google.com/patent/CN202228391U/en) |
| US8770949B2 | [unspecified] | Ceiling fan (general) | Baseline ceiling-fan patent, no exhaust interaction | L | [Google Patents](https://patents.google.com/patent/US8770949B2/en) |
| US8100746 | [unspecified] | Indoor air quality systems and methods | IAQ system, possibly includes pressure balancing logic [UNVERIFIED — not read in full] | L–M | [USPTO PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8100746) |

**I could not verify** a 10–20 family patent landscape specifically on "ceiling fan + negative-pressure/exhaust-fan interaction" — the search strongly suggests **this is a white-space niche with little to no direct patent crowding**, but this conclusion itself should be confirmed with a dedicated Espacenet/InPASS/WIPO Patentscope search using CPC classes for ceiling fans (F04D25/08, F04D25/16) cross-referenced with pressure-sensing/exhaust-interlock classes — not performed in this pass [UNVERIFIED — recommend follow-up patent-specific search, this is research not a legal opinion].

## 9. Unsolved gaps and opportunities

**What's unsolved:** No residential ceiling fan or exhaust fan sold in India senses or compensates for the pressure imbalance / short-circuited recirculation it causes in an adjoining room. The commercial-kitchen solution (make-up-air fans interlocked with exhaust hoods, per Greenheck/Accurex/Streivor guidance) is **structurally and economically inapplicable** to Indian flats — it requires ducting and a separate supply fan. Gas-flame flicker/instability from cross-drafts in open-flame Indian kitchens is plausible but **unquantified** for the Indian cooking context.

**Concept directions:**
1. **Pressure/current-draw-based load sensing on the ceiling fan.** Mechanism: detect an abnormal increase in motor current or RPM droop at fixed PWM/voltage, which could indicate the fan's recirculation loop is being disrupted (higher aerodynamic drag asymmetry) by an open-door crossflow; respond by nudging speed up to compensate thrust loss. Expected benefit: partial restoration of felt air speed at occupant height. [UNVERIFIED expected %] Risk: current-draw changes from this cause are likely tiny compared to voltage-fluctuation noise (Condition 26), so signal-to-noise may be too poor — flag for bench validation. Cost: low (software/firmware only on existing BLDC controllers). Novelty vs. patents: likely novel combination, but not patent-searched in depth.
2. **Door-airflow baffle / jet-redirection accessory**, not a fan-electronics feature: a low-cost, passive deflector or door-gap air-curtain concept that reduces the short-circuit leakage path without touching the fan itself. Mechanism: physical ventilation fix, cheaper and more reliable than sensing. Risk: it's a room/door accessory, not a "fan aerodynamics" innovation — may fall outside AtomQuest's blade-aerodynamics scope. Cost: very low.
3. **Directional/two-zone blade pitch or dual-rotation fan** that can bias its downwash slightly against the prevailing infiltration direction, keeping more of the jet on the floor instead of being pulled toward the open door. Mechanism is speculative and unverified by any source found; would need original CFD/experimental validation before claiming benefit.
4. **Education/labeling feature**, not a product redesign: pair ceiling fans with simple guidance (e.g., in-app tip) to close doors between kitchen-exhaust operation and ceiling-fan rooms — a zero-engineering-cost mitigation, acknowledging the physics is largely a room-topology problem the fan cannot fully solve alone.
5. Given the apparent **absence of a close patent landscape** (see §8, itself unverified pending a dedicated patent search), a pressure/current-sensing adaptive ceiling fan feature is a plausible low-risk white-space concept worth a dedicated prior-art search before investment.

**Honest scoping note:** this condition is fundamentally a **room/building ventilation-balance problem**, and the ceiling fan is a secondary actor in it. The size of the opportunity for an "aerodynamics-led" ceiling-fan concept here is likely smaller than for conditions where the fan itself is the primary cause of the airflow deficit (e.g., low ceiling, corner mounting). This should be weighed in the cross-condition synthesis (prompt S1).

## 10. Measurement and validation plan

- **Setup:** A real two-room test (kitchen + adjoining bedroom/living room with a ceiling fan), with a controllable exhaust fan (variable CFM) and a controllable door-gap area.
- **Instruments:**
  - Differential pressure manometer/micromanometer (e.g., 0–50 Pa range) across the doorway, to quantify room ΔP at various exhaust CFM settings.
  - Hot-wire or vane anemometer grid at occupant height (0.3–0.6 m seated/lying, 1.1 m seated) in the ceiling-fan room, at fixed radial positions from fan center, under exhaust-off vs exhaust-on conditions.
  - Smoke/fog visualization at the doorway to visualize the short-circuit path and jet deflection qualitatively.
  - Power meter on both fans to log current draw concurrently with airflow changes (to test concept #1 above).
  - Sound meter, standard per existing fan-noise protocols, to rule out any exhaust-coupling noise artifact.
- **Grid points:** A minimum 3×3 horizontal grid at 1.1 m height plus the doorway transect, repeated at 3 exhaust-fan CFM settings (0, medium, full) × 2 door states (open/closed) × 2–3 ceiling-fan speeds.
- **Metrics:** % change in mean air speed at occupant height vs. exhaust-off baseline; room ΔP (Pa); doorway air velocity (m/s); fan motor current (A) and RPM.
- **CFD comparison target:** build the CFD model described in §7 (SST k-ω, sliding mesh, pressure/velocity boundary at kitchen opening) and validate against the above grid measurements before trusting it for concept screening.

## 11. Sensors and smart control

- **Current draw / RPM feedback** on BLDC ceiling fans is already a standard capability of most BLDC motor controllers (used today for speed regulation); repurposing it to infer aerodynamic load changes from an adjoining depressurized room is **not confirmed as implemented in any existing commercial product** found in this search [UNVERIFIED].
- **Differential pressure sensing** is mature and inexpensive in HVAC generally (e.g., Sensirion SDP3x-class MEMS differential pressure sensors referenced in [ThunderFly TFASPDIMU02](https://github.com/ThunderFly-aerospace/TFASPDIMU02), combining a differential pressure sensor with IMU/magnetometer) but these are aimed at airspeed/UAV applications; a direct consumer ceiling-fan integration was not found.
- No existing ceiling fan was found that senses occupancy, humidity, or pressure specifically to counteract an exhaust-fan-induced negative-pressure condition. This remains an open, low-maturity area, consistent with the "white space" flagged in §9.

## 12. Summary

**Executive summary:** Running a kitchen or bathroom exhaust fan (or chimney) alongside a ceiling fan in an Indian home creates a pressure imbalance that pulls part of the ceiling fan's return-air loop out of the room through the open door or gaps toward the depressurized space, short-circuiting its recirculation and deflecting its downwash jet — a mechanism well-documented in general HVAC make-up-air and jet-in-crossflow literature but never studied directly for this ceiling-fan-plus-residential-exhaust combination, so quantified effect sizes for Indian rooms do not exist in the public literature found here. Separately, strong exhaust suction without adequate make-up air is a known combustion/backdraft safety concern for gas appliances in general, though the Indian context (predominantly unflued open-flame LPG stoves) likely experiences this as localized flame flicker rather than classic flue backdraft — a plausible but unverified inference. No current market product (ceiling fan or exhaust fan) in India markets a feature addressing this interaction, and no close patent family was found, suggesting this is a genuine but comparatively narrow white-space opportunity, since the root cause is a room/building ventilation-balance problem that a ceiling fan alone cannot fully correct.

**Top 5 insights:**
1. The core mechanism is **short-circuiting of the ceiling fan's return-air loop** via the open door/gap toward the depressurized kitchen/bathroom — a pressure/flow-topology effect, not a blade-aerodynamics effect.
2. The commercial-kitchen industry already solves the pressure-imbalance problem with **interlocked make-up-air fans**, but this ducted solution doesn't transfer to Indian residential retrofit.
3. **No direct academic or patent literature** exists on the specific ceiling-fan/exhaust-fan interaction; all physics reasoning here is extrapolated from adjacent fields (HVAC make-up air, mine-ventilation jet-in-crossflow, cold-storage air curtains) and needs original testing.
4. **SST k-ω turbulence closure with sliding/overset mesh** is the best-validated CFD approach for ceiling-fan flows generally and should be the starting point for simulating this condition.
5. Gas-stove flame disturbance from negative pressure is a known general hazard, but **not quantified for Indian open-flame LPG stoves** — a genuine safety-relevant open question worth flagging to the team even though it's outside pure aerodynamics.

**Open questions / what could not be found:**
- Any measured % air-delivery or air-speed loss at occupant height caused specifically by a kitchen/bathroom exhaust fan running concurrently with a ceiling fan.
- Any India-specific study of LPG flame stability under negative kitchen pressure.
- Confirmation of whether IS 2312:1967 or IS 3588:1987 (or a newer unretrieved standard) is the currently enforced Indian standard for exhaust fans, and whether any Indian code mandates make-up air for residential kitchens.
- A dedicated Espacenet/InPASS/WIPO patent search (not completed here) to confirm the apparent absence of overlapping IP.
- Any IIT/IISc/CEPT thesis or paper specifically on this interaction.

## Sources

- [Industrial Monitor Direct — Fan Pressure Conflict: Preventing Stall and Recirculation](https://industrialmonitordirect.com/blogs/knowledgebase/resolving-conflicting-fan-airflows-in-shared-exhaust-systems)
- [The Building Code Forum — Negative air pressure in commercial kitchen](https://www.thebuildingcodeforum.com/forum/threads/negative-air-pressure-in-commercial-kitchen.28490/)
- [Air Quality Engineering — Kitchen Exhaust Facts](https://air-quality-eng.com/buyer-resources/articles/kitchen-exhaust-facts/)
- [Alephindia — BIS Certification for Electric Ceiling Type Fans IS 374](https://alephindia.in/isi-product/electric-ceiling-type-fans.php)
- [Stellar Test House — Electric Ceiling Fan Performance Test per IS 374:2019+A1:2022](https://stellartesthouse.com/electric-ceiling-fan-performance-test-as-per-is-3742019a12022/)
- [Hearth.com forum — Exhaust Fans and Negative Pressure](https://www.hearth.com/talk/threads/exhaust-fans-and-negative-pressure.86587/)
- [ROCIS — Kitchen Range Hoods Supplement 3: Caveats and Cautions](https://rocis.org/kitchen-range-hoods/kitchen-range-hoods-supplement-3/)
- [BASC PNNL — Look for Signs of a Gas Furnace Backdrafting](https://basc.pnnl.gov/diy-guides/look-signs-gas-furnace-backdrafting)
- [Energy Vanguard — Range Hood Makeup Air: The Basics](https://www.energyvanguard.com/blog/range-hood-makeup-air-the-basics/)
- [Greenheck — When is Make-Up Air Required for Kitchens](https://www.greenheck.com/resources/blog/when-is-make-up-air-required-for-kitchens)
- [Streivor — CKV Design Guide 2: Optimizing Makeup Air](https://www.streivor.com/wp-content/uploads/2020/11/CKV-Design-Guide-2-Optimizing-Makeup-Air.pdf)
- [Streivor — CKV Design Guide 3: Integrating Exhaust with HVAC](https://www.streivor.com/wp-content/uploads/2020/11/CKV-Design-Guide-3-Integrating-Exh-w-HVAC.pdf)
- [Underpressure Inc — Understanding Make-Up Air](https://underpressure-inc.com/insights/understanding-make-up-air-the-other-half-of-your-kitchen-exhaust-system)
- [USMadeSupply — NFPA 96: Kitchen Hood, Grease Duct & Exhaust Standard](https://usmadesupply.com/resources/building-codes-standards/fire-suppression-standards/nfpa-96)
- [Accurex — When Make-Up Air is Required for Commercial Kitchens](https://www.accurex.com/blog/white-papers/when-make-up-air-is-required-for-commercial-kitchens)
- [Homestyler — How to Choose and Size Kitchen Exhaust Fans for Indian Homes](https://www.homestyler.com/article/floorplanner/how-to-choose-and-size-kitchen-exhaust-fans-for-indian-homes)
- [MrHomes — Exhaust Fan CFM Calculator Guide](https://www.mrhomes.in/blogs/guide/exhaust-fan-cfm-calculator-guide)
- [MrHomes — Ultimate Exhaust Fan Buying Guide 2026](https://www.mrhomes.in/blogs/guide/ultimate-exhaust-fan-buying-guide-2026)
- [Home-Run — Best Exhaust Fans in India: Crompton, Havells, Orient](https://home-run.co/blogs/homerun-knowledge-base/best-exhaust-fans-india-comparison)
- [PDHonline — Fundamentals of Kitchen Ventilation (Course M228)](https://www.pdhonline.com/courses/m228/m228content.pdf)
- [Law.Resource.org — IS 3588:1987 Electric Axial Flow Fans](https://law.resource.org/pub/in/bis/S05/is.3588.1987.pdf)
- [Law.Resource.org — Electric Fans (ETD 5) manifest](https://law.resource.org/pub/in/bis/manifest.etd.5.html)
- [CanRoHeat — Backdraft & Negative Pressure Homes](https://canroheat.ca/backdraft-and-negative-pressure-homes)
- [NACHI — Backdrafting](https://www.nachi.org/backdrafting.htm)
- [HypoAir — Negative Pressure Ventilation Can Be Dangerous in Your Home](https://hypoair.com/blogs/news/negative-pressure-ventilation-can-be-dangerous-in-your-home-how-to-prevent-it)
- [JASpector — IRC 2024 Backdrafting and Combustion Safety](https://www.jaspector.com/codes/irc-2024/ch17-combustion-air/backdrafting-combustion-safety-irc-2024/)
- [OSTI/DOE — Impact of Ceiling Fan and Room Air Cleaner on Air Mixing and Fate](https://www.osti.gov/pages/servlets/purl/2538429)
- [ScienceDirect — The benefit of kitchen exhaust fan use after cooking](https://www.sciencedirect.com/science/article/pii/S0360132318301112)
- [ScienceDirect — Assessing the impact of kitchen hoods and ventilation openings on indoor air quality post-cooking](https://www.sciencedirect.com/science/article/abs/pii/S2352710224032893)
- [Taylor & Francis — Validated transient CFD study of ceiling fan-induced airflow](https://www.tandfonline.com/doi/abs/10.1080/19401493.2026.2678829)
- [PMC — Experimental study on flow characteristics of jet ventilation in crossflow in confined mine spaces](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10997619/)
- [ScienceDirect — Three-dimensional effects of an air curtain used to restrict cold room infiltration](https://www.sciencedirect.com/science/article/pii/S0307904X06000849)
- [Google Patents — US9574779B2](https://patents.google.com/patent/US9574779)
- [Google Patents — EP1674799A1](https://patents.google.com/patent/EP1674799A1/en)
- [Google Patents — US6159093A](https://patents.google.com/patent/US6159093)
- [Google Patents — CN211950910U](https://patents.google.com/patent/CN211950910U/en)
- [Google Patents — CN202228391U](https://patents.google.com/patent/CN202228391U/en)
- [Google Patents — US8770949B2](https://patents.google.com/patent/US8770949B2/en)
- [USPTO — Indoor air quality systems and methods (US8100746)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8100746)
- [VSC Times — 5 Best BLDC Fans in India 2026](https://vsctimes.com/best-bldc-fans/)
- [ThunderFly-aerospace — TFASPDIMU02 differential pressure + IMU sensor](https://github.com/ThunderFly-aerospace/TFASPDIMU02)
