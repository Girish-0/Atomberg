# Comparison Rubric (shared by all agents — do not deviate)

Source reports: /home/girish/Documents/Atomberg/research/NN-*.md (28 files).
Goal: AtomQuest 2026 (Atomberg) team building an **aerodynamics-led** ceiling fan innovation. Find which room conditions are the best targets.

## Scores (integer 1–5, each needs a one-line justification citing the report section)
| Key | Dimension | 1 = | 5 = |
|---|---|---|---|
| FREQ | How common in Indian homes | rare / niche | most homes |
| SEV | Severity of airflow/comfort/energy loss | negligible | large, quantified loss |
| UNSOLVED | Market gap (inverse of market coverage) | well solved by products | nobody addresses it |
| PATENT_ROOM | Freedom vs patents (inverse of crowding) | crowded, high overlap | white space |
| AERO_FIT | Can blade/fan aerodynamics (geometry, RPM control, airflow shaping) be the core fix? | fix is non-aero (electrical, installation, materials only) | aero is the core lever |
| EVIDENCE | Strength of evidence in the report | mostly [UNVERIFIED] | primary sources with numbers |
| PROTO | Feasibility to prototype + test in a hackathon (cheap rig, measurable) | needs big lab | bench test in a room |

TOTAL = FREQ + SEV + UNSOLVED + PATENT_ROOM + 2×AERO_FIT + EVIDENCE + PROTO  (max 40)

## Card template (one per report, exactly this format)
```
### NN — <condition name>
| Key | Score | Justification (report §) |
|---|---|---|
| FREQ | x | ... |
| SEV | x | ... |
| UNSOLVED | x | ... |
| PATENT_ROOM | x | ... |
| AERO_FIT | x | ... |
| EVIDENCE | x | ... |
| PROTO | x | ... |
| **TOTAL** | xx | |

**Top quantified facts (max 4, copied exactly with source link from the report):**
- ...
**Core unsolved gap (1 sentence):** ...
**Best concept direction from report (1–2 sentences):** ...
**Key patents to design around (numbers exactly as in report, keep [UNVERIFIED] tags):** ...
**Links to other conditions (NN list + why):** ...
```

## Rules
- Use ONLY what the report says. Never add outside facts, never invent numbers or patent numbers.
- Preserve [UNVERIFIED] tags on anything copied.
- If the report lacks info for a score, score conservatively and say "not in report".

## Calibration anchors (added by orchestrator — all verifiers MUST apply these so batches are comparable)
- AERO_FIT 5 only if blade geometry / airflow shaping / RPM-aero control is THE fix (e.g. low-speed blade stall, airflow redirection). 3 = aero helps but sensing/control/installation does most. 1–2 = electrical/materials/installation fix (e.g. voltage regulation, wobble balancing, corrosion).
- EVIDENCE 5 requires condition-specific measured data from primary sources. If the report's key numbers are mostly [UNVERIFIED] or borrowed from analogue studies, max 3.
- UNSOLVED 5 only if the report found NO product addressing it. PATENT_ROOM 5 only if the report found essentially no relevant patents; a thin search that "found few" is max 4.
- FREQ 5 = almost every Indian home (e.g. bed under fan, low-speed night use). Niche (sloped ceilings, balconies, chandeliers) = 1–2.
- Expected spread: across all 28, TOTALs should range roughly 18–36; a batch where every card scores ≥30 is miscalibrated.
