# Re-evaluation of Findings & Gaps (2026-10-10)

Critical second pass over `comparison.md` and `gaps.md`. Goal: what holds up, what's weak, what's missing before we pick solutions.

## 1. What holds up
- **Core thesis is sound:** fans are designed and rated at max speed in an open chamber, but used at low speed, over a bed, in a real room. That mismatch (G1 + G2) is the strongest, cheapest-to-prove story.
- **AERO_FIT filter is correct.** Dropping 15, 16, 17, 18, 20, 26 and 28 from the aero pitch is right.
- **Own-test-data angle** (comparison §7) is the real differentiator: every Tier-1 score rests on analogue evidence, so the first measured dataset is itself a contribution.

## 2. Where the findings are weaker than they look
| Issue | Why it matters | Fix |
|---|---|---|
| **Ranking is fragile.** FREQ is [UNVERIFIED] on every card and EVIDENCE is 1–3 across Tier 1. Tier-1 TOTALs differ by only 0–3 points, about the ±2 noise band. | Saying "Top 3 by score" will not survive a judge's question. | Pitch by **mechanism and user moment**, not score. Use the score only as a filter. |
| **22 and 27 are one target, not two.** Both describe the same moment: a fan on speed 1–2 at night over a bed. | Splitting them makes us look like we have three ideas when we really have one strong one. | Merge them into a single **"Night-bedroom regime"** target: low RPM, short throw, a person at 0.6 m. |
| **19 (cross-ventilation) is likely overstated.** Fan downwash near the blades is about 2–4 m/s and room drafts are 0.2–0.8 m/s, so r is usually well above 1. Strong deflection only happens at low fan speed or near a window. Urban flats increasingly run with windows closed and the AC on. | SEV may be about 2, not 3. The fix is also control/sensing (AERO_FIT closer to 3), and current-ripple sensing is unproven. | Demote 19 to a "stretch/test" item. If we want a third slot, 25 or Cluster A (01/02 hugger and false ceiling) is a cleaner aero story. |
| **The "Dual-Regime" concept conflicts with itself** (comparison §5 risks). A twist that recovers low-RPM lift pulls against a flatter exit profile, and an RPM boost pulls against the sleep goal. | A single fixed blade can't do both. | This is exactly why **G3 (passive RPM-dependent twist)** is the most interesting idea: it is the mechanism that resolves the conflict. |
| **Patent picture for 27 is mixed, not just "crowded".** US 6,039,541 (1990s filing) is probably expired, but later family members (e.g. 7,927,071) may still be live into the late 2020s. | Reusing the twist schedule blindly could infringe the live members. | Check the legal status of each family member, not just the parent. |
| **G3 prior art lies outside fans.** Wind turbine "bend-twist coupling / aeroelastic tailoring", passively adaptive propellers, and flexible-blade cooling fans all exist. | "No fan product does it" ≠ novel. A judge or patent examiner will look there. | Run a prior-art search in those fields before we claim white space. |
| **IS 374 low-speed claim is still unverified.** | G1's whole pitch ("ratings measure the wrong thing") depends on it. | Read the clause text before the pitch. |

## 3. Gaps the research never covered
1. **Atomberg's own baseline.** We don't have their RPM per speed step, blade material and process, or what their existing Sleep/Boost modes actually do. Every concept has to beat their product, not a generic fan.
2. **The user's voice.** There is no survey or review mining (Amazon/Flipkart complaints such as "too much air on bed at speed 1", "noise at night", "no air under false ceiling"). FREQ is all guesswork, and a 30-person survey would turn it into numbers.
3. **Manufacturability and cost.** Blades are usually die-cast aluminium, sheet metal, or ABS. A flexing or passive-twist blade needs composite or plastic, which brings fatigue, creep in the Indian heat, balance tolerance and BOM delta. None of this is scored.
4. **Noise as a first-class metric.** Night use is noise-limited, but the scoring rubric has no noise dimension.
5. **Comfort physics.** We measure air speed, but comfort means draught rate, turbulence and SET (ISO 7730 / ASHRAE 55). We need to pick the comfort metric before we build the rig.
6. **Test-rig realism.** A hot-wire grid is expensive and fragile, so a vane anemometer or low-cost thermal anemometer plus smoke may be the real budget option. Measurement uncertainty has not been planned.
7. **Safety and standards for any moving or flexing blade.** Blade retention, tip deflection near the downrod, IS/IEC safety: unaddressed.

## 4. Re-ranked view (my recommendation)
1. **Night-bedroom regime (22 + 27, with G2/G3 as the levers).** Most frequent, aero is the fix, and it can be tested in one bedroom.
2. **Real-Room Comfort Rating (G1).** This is the measurement framing and the proof tool for #1. It's cheap and a strong pitch.
3. **Hub/inflow starvation (Cluster A: 01, 02).** False ceilings and huggers are growing fast, and a clearance-vs-delivery curve is easy to measure.
4. Stretch: 19 cross-draft and 25 uniformity, kept as test cases on the same rig.

## 5. Verify list (updated)
- [ ] IS 374:2019 clause text and the BEE star-label test speed
- [ ] Legal status of the whole US 6,039,541 family
- [ ] Prior art: passive/aeroelastic variable twist (wind turbines, propellers, fans)
- [ ] Atomberg RPM per speed step and the blade material
- [ ] Jayasree et al. 2022 full text
- [ ] Quick user survey or review mining to replace the FREQ guesses
