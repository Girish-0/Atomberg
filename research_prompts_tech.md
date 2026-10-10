# Deep Research Prompts — Tech & Intelligence Track (AtomQuest 2026)

Three standalone prompts for Gemini Deep Research. Paste each one separately.

---

## Prompt 1 — Fan speed / rotation-frequency control for air spread and comfort

```
Context: I am on a team in AtomQuest 2026 (Atomberg, India) designing a smarter BLDC ceiling fan (1200 mm, ~50–350 RPM). I want to know whether controlling the fan's rotation speed/frequency PATTERN — not just the steady speed level — can improve how air spreads in a room and how comfortable people feel under different temperature and humidity conditions. I want only proven, published, or patented approaches I can build on.

Research and report on:

1. Physics: how ceiling-fan RPM changes air delivery (CMM), the downwash jet's shape, throw distance, spread radius, air speed at seated (1.1 m) and lying (0.6 m) height, turbulence intensity, and blade-passing frequency. Include fan scaling laws (flow ∝ RPM, pressure ∝ RPM², power ∝ RPM³) and where real ceiling fans deviate from them.
2. Time-varying / modulated speed: research on fluctuating, pulsed, sinusoidal, random "natural breeze" or "simulated wind" airflow vs constant airflow. What modulation periods and amplitudes (e.g. 0.3–1 Hz gusts, 1/f spectra) have been shown to improve thermal comfort or perceived cooling? Cite the human-subject studies (Zhu, Ouyang, Huang, Fountain, CBE Berkeley, Chinese "natural wind" studies) and give the numbers.
3. Speed vs climate: published evidence on the optimal air speed at different air temperatures and relative humidities (ASHRAE 55 elevated-air-speed method, SET, ISO 7730 draught rating, Indian Model for Adaptive Comfort / IMAC). Turn it into a table: temperature × humidity → recommended air speed at the occupant → approximate fan RPM. Point out where high humidity changes the answer (evaporative cooling of sweat).
4. Is there any evidence that specific RPMs "spread" air better (wider coverage) rather than just pushing more air? Look at blade-tip-vortex, jet-spreading, and wall-jet studies, and at CFD of ceiling fans at different RPMs.
5. Acoustics: how RPM and modulation affect noise (blade-passing tone, motor PWM/commutation whine), and which speed bands to avoid at night.
6. Patents: find patents on ceiling- and pedestal-fan speed modulation, natural-breeze modes, temperature/humidity-based automatic speed control, and comfort-index-driven fan control (e.g. US 9,103,346, Big Ass Fans SenseME, Panasonic, Havells, Atomberg, Orient, Crompton, Xiaomi, Dyson, Chinese CN patents). For each patent give: number, assignee, filing date, likely expiry, key claim in one line, and whether it is still in force.
7. Commercial products: which fans already offer breeze/nature modes or temperature-humidity auto modes, what each actually does, and any measured evidence that it works.
8. BLDC implementation: how modulation is done in a BLDC controller (sensorless FOC/trapezoidal, acceleration limits, how fast a 1200 mm fan can actually change speed given blade inertia, energy cost of modulation).

Output: an executive summary; a "proven vs claimed vs speculative" table; the temperature/humidity → air speed → RPM table; recommended modulation patterns with sources; a patent table; open gaps that nobody has studied. Cite every number with its source and mark anything unverified.
```

---

## Prompt 2 — On-device tiny AI that learns how a user uses the fan

```
Context: I am on a team in AtomQuest 2026 (Atomberg, India) building a BLDC ceiling fan with a small embedded controller that runs a tiny AI model fully offline (no cloud). The model must quietly observe how a person uses the fan (on/off times, speed changes, remote/app commands, room temperature and humidity, time of day, day of week, season, presence) and then automatically set the fan the way the user prefers. It must keep adapting: for example, if the user changes the speed at 11 pm on two consecutive days, the fan should apply that change itself on day 3. A single one-off change should not overwrite the learned habit.

Research and report on:

1. Hardware: low-cost microcontrollers and SoCs that can run on-device ML and ON-DEVICE LEARNING inside a fan (power budget <1 W, BOM cost in INR/USD at volume). Compare ESP32-S3, ESP32-C6, STM32 (incl. STM32N6 / Cube.AI), Nordic nRF54, Arm Cortex-M55 + Ethos-U55, Raspberry Pi RP2350, Kendryte K210, Syntiant, GreenWaves GAP9, Ambiq Apollo4/5, Infineon PSoC Edge, and any others. Give: CPU/NPU, RAM, flash, Wi-Fi/BLE, price, power, and whether they can train/update a model on the device. Note which ones Atomberg-class fans plausibly already use (many smart fans use ESP32-class chips).
2. Frameworks: TensorFlow Lite Micro / LiteRT, Edge Impulse, STM32Cube.AI, microTVM, emlearn, TinyML on-device training libraries (TinyOL, TinyTL, MCUNet / PockEngine, "TinyML on-device training" papers by Song Han's lab), and simple non-neural options.
3. Algorithms suited to habit learning on a microcontroller, with a pros/cons and memory/compute table:
   - frequency/count-based habit tables per time slot (e.g. 15-min bins × weekday/weekend)
   - exponential moving averages and decay
   - Bayesian / Beta-Binomial preference updating
   - decision trees / random forest (emlearn), k-NN
   - online / incremental learning, Hoeffding trees
   - contextual multi-armed bandits and lightweight reinforcement learning using user overrides as negative reward
   - small sequence models (tiny RNN/LSTM/TCN) for predicting next action
   - change-point detection to tell a "new habit" (repeated N days) apart from a "one-off" change
   How have smart thermostats (Nest Learning Thermostat, ecobee), smart lights and smart ACs solved exactly this "learn the schedule, adapt after repeated overrides" problem? Give details of their logic where published or patented.
4. Inputs/sensors: which signals are worth having (temperature, humidity, PIR/mmWave presence, ambient light, time, remote IR/RF and app commands, motor current/RPM already available in the BLDC driver), their cost, and which give the most predictive value for comfort.
5. Comfort-aware learning: combining the learned user preference with physics comfort models (ASHRAE 55 / IMAC adaptive comfort, SET) so the model generalizes to new weather, e.g. it learns "user prefers about X air speed at Y °C and Z % RH" instead of just "speed 3 at 11 pm".
6. Practical design issues: cold start (sensible defaults), multiple users in one room, guests and holidays, seasonal drift, forgetting old habits, explainability ("fan is in learned mode"), and how quickly the user can override. Store model in flash safely (wear leveling, power cuts, which are common in India).
7. Privacy and safety: benefits of fully local learning; any Indian DPDP Act 2023 implications for occupancy data; failsafes.
8. Patents and prior art: patents on learning/adaptive fan control, learning thermostats (Nest/Google, Honeywell, ecobee), and appliance usage-pattern learning. Give number, assignee, filing date, likely expiry, key claim, and how to design around it. Also list existing "AI fans" in India and globally and what they actually learn.
9. Evaluation: how to measure success in a hackathon — prediction accuracy of the next user action, reduction in manual adjustments per day, energy saved, comfort votes; suggest a simulation using synthetic user logs.

Output: executive summary; a recommended reference architecture (hardware + algorithm + data flow) for a ₹-cost-sensitive fan; comparison tables for hardware and algorithms; pseudocode for the "repeat 2 days → apply on day 3" adaptation rule; patent table; risks and open gaps. Cite sources for every claim and mark unverified ones.
```

---

## Prompt 3 — Temperature-triggered two-way shape-changing materials for fan blades

```
Context: I am on a team in AtomQuest 2026 (Atomberg, India) designing a ceiling fan (1200 mm, 3 blades, ~50–350 RPM, indoor ambient roughly 15–45 °C) whose blades passively change shape with temperature, with no motor or actuator. I want a material or structure that has TWO stable, repeatable shapes at two temperatures: as the room gets hotter the blade (or part of it, e.g. a trailing-edge flap, tip, or twist section) changes one way (e.g. more pitch/camber → more airflow), and as the room cools it returns the other way. It must reverse by itself for many years of daily cycles. I will choose the exact shape direction later.

Research and report on:

1. Candidate materials and structures, compared in a table (actuation temperature range and whether it can be tuned to ~25–35 °C, achievable strain/deflection, force, hysteresis, one-way vs TRUE two-way behavior, cycle life/fatigue, response time, creep, density, cost per kg, manufacturability, UV/humidity durability):
   - Shape memory alloys: NiTi (Nitinol), Cu-based (CuAlNi, CuZnAl), Fe-based; the two-way shape memory effect (TWSME) and the training methods needed; and SMA wire/spring + bias spring designs that give two-way motion from a one-way alloy.
   - Shape memory polymers (SMP) and two-way / reversible SMPs; SMP composites.
   - Liquid crystal elastomers (LCE).
   - Thermostatic bimetals and trimetals (proven in thermostats, car radiator flaps, self-opening vents) — deflection formulas and how much curvature per °C.
   - Thermally responsive laminates/composites with mismatched CTE, and 4D-printed structures (PLA/TPU, hydrogel-free).
   - Wax/paraffin thermal actuators (as in car thermostats).
   - Any other passive thermal actuators.
2. The core physics problem: indoor temperature only swings a few °C to ~20 °C. Which materials give useful, visible shape change over such a SMALL temperature window near room temperature? Give real deflection numbers.
3. Loads on a ceiling fan blade: centrifugal force, aerodynamic lift/drag, and vibration at 50–350 RPM for a 1200 mm fan. Estimate them and check whether each candidate can generate enough force/stiffness to hold its shape against these loads without fluttering or causing imbalance (all blades must morph identically).
4. Where to put the morphing element: whole blade twist vs trailing-edge flap vs tip vs root pitch hinge; aerodynamic effect of a few degrees of pitch/camber change on air delivery; and what blade-shape change direction helps in hot vs cool conditions.
5. Prior art in adjacent fields: morphing/adaptive aircraft wings and flaps with SMA, passive variable-pitch propellers, wind-turbine bend-twist coupling and aeroelastic tailoring, SMA chevrons (Boeing variable-geometry chevrons), SMA rotor-blade tabs (helicopters), thermally adaptive building facades/vents, self-adjusting radiator louvres, and any thermally morphing fan or impeller blades (computer cooling fans, HVAC, automotive).
6. Patents: search for temperature-responsive / shape-memory fan blades, impellers, louvres and passive variable-pitch fans (US, CN, IN, EP, JP). For each: number, assignee, filing date, likely expiry, key claim, overlap with my idea. Identify the white space.
7. Reliability and safety: fatigue over ~10 years of daily cycles (≈3,650+ thermal cycles plus millions of rotations), functional fatigue / shape-memory degradation, corrosion and humidity in India, temperature overshoot, failure modes, and how a failure keeps the fan safe and balanced. Any relevant IS/IEC fan safety standards.
8. Prototyping for a hackathon: cheapest way to build and test a demo (buy Nitinol wire/sheet or bimetal strip, typical suppliers and cost in India, training procedures, attachment methods), plus a test plan (heat gun / climate box, measure deflection angle, airflow with anemometer at two temperatures).

Output: executive summary; a material comparison table with a clear ranked recommendation for a 25–35 °C two-way blade actuator; force/deflection feasibility estimates; prior-art and patent tables; design concepts (sketch descriptions) with pros/cons; reliability risks; and a prototype bill of materials and test plan. Cite every number and mark unverified claims.
```
