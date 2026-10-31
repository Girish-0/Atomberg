"""Builds the AtomQuest 2026 Stage-1 abstract PDF.
Edit TEAM below, then:  python3 Submission/build.py
Needs: weasyprint.  Output: Submission/<TeamName>_Track1.pdf
"""
import math, pathlib, subprocess

TEAM = {
    "name": "[TEAM NAME]",
    "institute": "[Institute name, City]",
    "dept": "[Department / Programme]",
    "mentor": "[Faculty mentor name, designation — or remove row]",
    "members": [  # name, programme & year, role, email, phone
        ("Girish N", "[Programme, Year]", "Lead · firmware & learning", "[email]", "[phone]"),
        ("[Member 2]", "[Programme, Year]", "Blade mechanics & aero tests", "[email]", "[phone]"),
        ("[Member 3]", "[Programme, Year]", "Electronics & motor control", "[email]", "[phone]"),
        ("[Member 4]", "[Programme, Year]", "Test rig, data & comfort trials", "[email]", "[phone]"),
    ],
}

HERE = pathlib.Path(__file__).parent
HOT, COOL, INK, MUTED, ACC = "#c2410c", "#1d4ed8", "#1b2128", "#5b6570", "#0b6e75"


# ---------- Figure 1: blade planform + section A-A ----------
def rot(px, py, cx, cy, deg):
    a = math.radians(deg)
    dx, dy = px - cx, py - cy
    return cx + dx * math.cos(a) - dy * math.sin(a), cy + dx * math.sin(a) + dy * math.cos(a)


def flap(hx, hy, deg, color, dash="", fill="none"):
    # tapered flap, chord 46 px, starting at hinge, base slope +9deg (camber continues)
    pts = [(hx - 4, hy - 2.6), (hx + 58, hy - 0.4), (hx + 58, hy + 0.7), (hx - 4, hy + 2.6)]
    pts = [rot(x, y, hx, hy, 9 + deg) for x, y in pts]
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
    return f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="1.3" {dash}/>'


def fig_blade():
    hx, hy = 500, 112
    s = [f'<svg viewBox="0 0 640 196" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans" font-size="9.5" fill="{INK}">']
    # planform
    s.append(f'<text x="8" y="14" font-weight="700" font-size="10">Top view · one blade (1200 mm sweep)</text>')
    s.append(f'<circle cx="30" cy="92" r="20" fill="#e6e9ec" stroke="{MUTED}"/><text x="30" y="95" text-anchor="middle" font-size="8">hub</text>')
    s.append(f'<path d="M50,84 L70,62 L292,58 Q300,60 300,66 L300,104 L70,112 L50,100 Z" fill="#dfe5ea" stroke="{INK}" stroke-width="1.1"/>')
    s.append(f'<path d="M214,94 L300,91 L300,104 L214,107 Z" fill="{HOT}" fill-opacity=".85" stroke="{INK}" stroke-width="1"/>')
    s.append(f'<rect x="204" y="91" width="12" height="18" rx="3" fill="#fff" stroke="{INK}"/>')
    s.append(f'<path d="M210,100 m-3,0 a3,3 0 1,1 6,0 a4.5,4.5 0 1,1 -9,0 a6,6 0 1,1 12,0" fill="none" stroke="{INK}" stroke-width=".8"/>')
    s.append(f'<line x1="258" y1="48" x2="258" y2="120" stroke="{MUTED}" stroke-dasharray="4 3"/><text x="262" y="45" font-size="8.5">A</text><text x="262" y="124" font-size="8.5">A</text>')
    s.append(f'<text x="70" y="52" font-size="8.5" fill="{MUTED}">leading edge · rigid aluminium, carries all primary loads</text>')
    s.append(f'<text x="176" y="146" font-size="8.5">flap: outer 35 % span × 25 % chord</text><text x="176" y="157" font-size="8.5">~15 g PETG on SS hinge pin</text>')
    s.append(f'<line x1="236" y1="137" x2="250" y2="106" stroke="{INK}" stroke-width=".6"/>')
    s.append(f'<text x="8" y="150" font-size="8.5">bimetal coil in fairing at flap</text><text x="8" y="161" font-size="8.5">root (r ≈ 0.44 m) — senses</text><text x="8" y="172" font-size="8.5">room air directly</text>')
    s.append(f'<line x1="120" y1="141" x2="204" y2="106" stroke="{INK}" stroke-width=".6"/>')
    # section A-A
    s.append(f'<text x="334" y="14" font-weight="700" font-size="10">Section A–A · what the coil does</text>')
    s.append(f'<path d="M336,122 Q420,78 {hx},{hy-1.5} L{hx},{hy+2} Q420,87 338,125 Z" fill="#dfe5ea" stroke="{INK}" stroke-width="1.1"/>')
    s.append(flap(hx, hy, -6, COOL, 'stroke-dasharray="4 2"'))
    s.append(flap(hx, hy, 0, MUTED, 'stroke-dasharray="1.5 2"'))
    s.append(flap(hx, hy, 8, HOT, "", HOT))
    s.append(f'<circle cx="{hx}" cy="{hy}" r="3.4" fill="#fff" stroke="{INK}" stroke-width="1.2"/>')
    s.append(f'<text x="566" y="111" fill="{COOL}" font-size="8.8">20 °C · −6°</text>')
    s.append(f'<text x="566" y="124" fill="{MUTED}" font-size="8.8">28 °C · stock</text>')
    s.append(f'<text x="566" y="139" fill="{HOT}" font-size="8.8" font-weight="700">38 °C · +8°</text>')
    s.append(f'<text x="342" y="150" font-size="8.5">≈ 0.8° of flap per °C  (θ = k·L·ΔT / t)</text>')
    s.append(f'<text x="342" y="162" font-size="8.5">hot → more camber &amp; effective pitch → more air per rev</text>')
    s.append(f'<text x="342" y="174" font-size="8.5">cool → flatter → softer draft, lower power per rev</text>')
    s.append(f'<text x="342" y="186" font-size="8.5" fill="{MUTED}">hard stops −6° / +10° · rotation 15–19 m/s at flap</text>')
    s.append(f'<path d="M352,40 l12,0" stroke="{INK}" marker-end="url(#a)"/><text x="368" y="43" font-size="8.5">blade motion</text>')
    s.append(f'<path d="M430,40 l0,14" stroke="{INK}" marker-end="url(#a)"/><text x="436" y="50" font-size="8.5">air pushed down</text>')
    s.append(f'<defs><marker id="a" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="{INK}"/></marker></defs>')
    s.append("</svg>")
    return "\n".join(s)


# ---------- Figure 2: system block diagram ----------
def box(x, y, w, h, title, lines=(), fill="#fff", stroke=INK, tcol=INK, dash=""):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="1.1" {dash}/>',
           f'<text x="{x+7}" y="{y+13}" font-weight="700" fill="{tcol}">{title}</text>']
    for i, l in enumerate(lines):
        out.append(f'<text x="{x+7}" y="{y+25+i*10.5}" font-size="8.3" fill="{MUTED}">{l}</text>')
    return "\n".join(out)


def arrow(d, color=INK, dash="", label=None, lx=0, ly=0):
    a = f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.2" {dash} marker-end="url(#b)"/>'
    if label:
        a += f'<text x="{lx}" y="{ly}" font-size="8" fill="{color}">{label}</text>'
    return a


def fig_blocks():
    s = [f'<svg viewBox="0 0 700 262" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans" font-size="9.3" fill="{INK}">',
         f'<defs><marker id="b" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="context-stroke"/></marker></defs>']
    # room column
    s.append(box(4, 6, 92, 250, "ROOM", (), "#f3f5f7", MUTED, MUTED))
    for i, (t, sub) in enumerate([("Temperature", "& humidity"), ("Person", "awake / asleep"), ("Light level", "lights-off = bed"), ("User", "remote · app")]):
        y = 26 + i * 44
        s.append(f'<rect x="12" y="{y}" width="76" height="34" rx="4" fill="#fff" stroke="{MUTED}"/>'
                 f'<text x="18" y="{y+14}" font-size="8.8" font-weight="700">{t}</text><text x="18" y="{y+26}" font-size="8" fill="{MUTED}">{sub}</text>')
    s.append(f'<rect x="12" y="206" width="76" height="40" rx="4" fill="#fff" stroke="{HOT}"/><text x="18" y="221" font-size="8.8" font-weight="700" fill="{HOT}">Room air</text><text x="18" y="233" font-size="8" fill="{MUTED}">reaches blade</text><text x="18" y="242" font-size="8" fill="{MUTED}">directly</text>')
    # sensors
    s.append(box(112, 6, 104, 196, "SENSORS (3.3 V)", ()))
    for i, (t, sub) in enumerate([("SHT40", "T ±0.2 °C, RH ±1.8 %"), ("LD2410 radar", "24 GHz · breathing"), ("Ambient light", "VEML7700"), ("IR receiver", "existing remote")]):
        y = 26 + i * 44
        s.append(f'<text x="120" y="{y+14}" font-size="8.8" font-weight="700">{t}</text><text x="120" y="{y+26}" font-size="8" fill="{MUTED}">{sub}</text>')
        s.append(arrow(f"M88,{y+17} L110,{y+17}", MUTED))
    # MCU
    s.append(box(234, 6, 214, 196, "ESP32-C6  (RISC-V 160 MHz, offline)", (), "#eef6f6", ACC, ACC))
    s.append(box(244, 26, 194, 38, "BRAIN · habit learner", ("Bayesian table + 2-night rule → comfort offset",)))
    s.append(box(244, 72, 194, 50, "REFLEX · comfort controller", ("T×RH → target air speed (SET / IMAC)", "→ Breeze · Sleep · Humid-flush RPM profile")))
    s.append(box(344, 130, 94, 64, "Blade-state", ("current vs RPM", "residual → flap", "angle estimate")))
    s.append(box(244, 130, 94, 64, "Safety", ("manual wins <50 ms", "RPM clamps", "watchdog, brown-out")))
    s.append(arrow("M341,64 L341,70", ACC))
    s.append(arrow("M216,104 L242,104", INK))
    s.append(arrow("M391,128 L391,123", ACC))
    # driver / motor / rotor
    s.append(box(468, 6, 100, 74, "BLDC DRIVER", ("24 V SELV (proto)", "UART / PWM in", "INA226 current, tach")))
    s.append(arrow("M438,92 L452,92 L452,44 L466,44", INK))
    s.append(box(586, 6, 108, 74, "MOTOR", ("1200 mm ceiling fan", "50–350 RPM", "I ≈ 0.06 kg·m²")))
    s.append(arrow("M568,43 L584,43", INK))
    s.append(box(468, 100, 226, 102, "ROTOR · BODY  (no electronics)", ("3 blades, each with bimetal coil → trailing-edge flap", "• +0.8° flap per °C, τ ≈ 10–30 s", "• matched in sets of 3, tip tracking ≤ 2 mm", "• fails safe to stock (neutral) blade shape"), "#fff4ee", HOT, HOT))
    s.append(arrow("M640,80 L640,98", INK, label="torque", lx=646, ly=93))
    s.append(arrow("M500,99 L500,83", ACC, 'stroke-dasharray="3 2"'))
    s.append(f'<text x="505" y="93" font-size="7.8" fill="{ACC}">flap load → current</text>')
    s.append(arrow("M468,66 L460,66 L460,160 L440,160", ACC, 'stroke-dasharray="3 2"'))
    # passive path room air -> rotor
    s.append(arrow("M88,226 L600,226 L600,204", HOT, 'stroke-dasharray="5 3"', "PASSIVE PATH — room heat reshapes the blade, electronics off", 300, 221))
    # outputs
    s.append(arrow("M660,202 L660,230", INK))
    s.append(box(468, 232, 226, 26, "→ Air speed & gust pattern at the person", (), "#fff", INK))
    s.append(box(112, 232, 336, 26, "Matter / BLE → AC set-point, exhaust fan, app (stretch)", (), "#fff", MUTED, MUTED, 'stroke-dasharray="3 2"'))
    s.append(arrow("M260,202 L260,230", MUTED, 'stroke-dasharray="3 2"'))
    s.append("</svg>")
    return "\n".join(s)


CSS = f"""
@page {{ size: A4; margin: 12mm 13mm 12mm 13mm;
  @bottom-left {{ content: "AtomQuest 2026 · Track 1 Fan · {TEAM['name']}"; font: 7.5pt 'Noto Sans'; color: {MUTED}; }}
  @bottom-right {{ content: "page " counter(page) " of 3"; font: 7.5pt 'Noto Sans'; color: {MUTED}; }} }}
@page :first {{ counter-increment: page 0; @bottom-left {{ content: none }} @bottom-right {{ content: none }} }}
* {{ box-sizing: border-box; }}
body {{ font-family: 'Noto Sans', 'Liberation Sans', sans-serif; font-size: 8.55pt; line-height: 1.38; color: {INK}; margin: 0; }}
h1 {{ font-size: 25pt; line-height: 1.1; margin: 0 0 6pt; letter-spacing: -.3pt; }}
h2 {{ font-size: 10.6pt; margin: 9pt 0 3pt; padding-bottom: 2pt; border-bottom: 1.2pt solid {INK}; letter-spacing: .1pt; }}
h2 .n {{ color: {ACC}; margin-right: 4pt; }}
h3 {{ font-size: 9pt; margin: 6pt 0 1.5pt; color: {ACC}; }}
p {{ margin: 0 0 4pt; }}
.lead {{ font-size: 9.3pt; }}
b, strong {{ font-weight: 700; }}
.hot {{ color: {HOT}; }} .cool {{ color: {COOL}; }} .muted {{ color: {MUTED}; }} .acc {{ color: {ACC}; }}
table {{ width: 100%; border-collapse: collapse; margin: 2pt 0 4pt; font-size: 8pt; line-height: 1.3; }}
th {{ text-align: left; font-weight: 700; border-bottom: 1pt solid {INK}; padding: 2.2pt 4pt; background: #f1f4f6; }}
td {{ border-bottom: .5pt solid #cfd5da; padding: 2.2pt 4pt; vertical-align: top; }}
td.num {{ white-space: nowrap; font-weight: 700; }}
.fig {{ margin: 3pt 0 2pt; }} .fig svg {{ width: 100%; }}
.cap {{ font-size: 7.5pt; color: {MUTED}; margin: 0 0 4pt; }}
.cols {{ display: flex; gap: 10pt; }} .cols > div {{ flex: 1; }}
.box {{ border: .8pt solid #cfd5da; border-left: 3pt solid {ACC}; padding: 4pt 7pt; margin: 4pt 0; background: #f7f9fa; }}
.box.warn {{ border-left-color: {HOT}; background: #fff8f4; }}
ul {{ margin: 1pt 0 4pt; padding-left: 12pt; }} li {{ margin: 0 0 1.5pt; }}
.page {{ page-break-after: always; }}
.kicker {{ font-size: 8pt; letter-spacing: 1.6pt; color: {ACC}; font-weight: 700; text-transform: uppercase; }}
.stats {{ display: flex; gap: 8pt; margin: 12pt 0; }}
.stat {{ flex: 1; border-top: 2pt solid {INK}; padding-top: 4pt; }}
.stat .v {{ font-size: 17pt; font-weight: 700; line-height: 1.1; }} .stat .l {{ font-size: 8pt; color: {MUTED}; }}
.ph {{ background: #fff3c4; }}
"""

members = "\n".join(
    f"<tr><td><b>{n}</b></td><td>{p}</td><td>{r}</td><td>{e}</td><td>{ph}</td></tr>" for n, p, r, e, ph in TEAM["members"])

HTML = f"""<!doctype html><html><head><meta charset="utf-8"><title>{TEAM['name']} — Track 1 Abstract</title><style>{CSS}</style></head><body>

<!-- ============ INTRO PAGE (excluded from page count) ============ -->
<div class="page">
<p class="kicker">AtomQuest 2026 · Stage 1 Abstract · Track 1 — Fan</p>
<h1>The Fan That Adapts</h1>
<p class="lead" style="font-size:11.5pt;max-width:150mm">A 1200 mm BLDC ceiling fan whose <b class="hot">blades reshape themselves with room temperature</b> — no sensor, wire or battery on the rotor — with a <b>climate-aware speed controller</b> and a <b>tiny offline learner</b> built around them.</p>

<div class="stats">
 <div class="stat"><div class="v">0</div><div class="l">electronics on the rotor — the blade itself is the thermostat</div></div>
 <div class="stat"><div class="v">+10–15 %</div><div class="l">air at the same RPM when the room is hot (target, to be measured A/B)</div></div>
 <div class="stat"><div class="v">2 nights</div><div class="l">for the fan to learn a user's comfort offset; &lt; 2 KB RAM, no cloud</div></div>
 <div class="stat"><div class="v">≈ ₹15 k</div><div class="l">Level-1 prototype; ≈ ₹350–500 added per unit at volume (est.)</div></div>
</div>

<h2><span class="n">A</span>Team &amp; institutional context</h2>
<table>
<tr><th style="width:22%">Team name</th><td class="ph"><b>{TEAM['name']}</b></td></tr>
<tr><th>Institute</th><td class="ph">{TEAM['institute']}</td></tr>
<tr><th>Department / programme</th><td class="ph">{TEAM['dept']}</td></tr>
<tr><th>Faculty mentor</th><td class="ph">{TEAM['mentor']}</td></tr>
</table>
<table>
<tr><th>Member</th><th>Programme &amp; year</th><th>Role in this project</th><th>Email</th><th>Phone</th></tr>
{members}
</table>

<h2><span class="n">B</span>Track &amp; areas of exploration</h2>
<p><b>Track 1 · Fan.</b> Primary area: <b>blade design for energy efficiency, air throw and low noise.</b> Combined with: <b>fan as a smart-home enabler (ambient temperature &amp; humidity triggers).</b></p>
<p><b>Why both:</b> a blade that changes shape with heat is only half a product. The motor controller must know the room's temperature and humidity — and know what the blade is already doing — or the two will over-react to the same heat. The same sensors then make the fan the room's climate node for the AC and exhaust fan.</p>

<h2><span class="n">·</span>How we got here</h2>
<p>Before choosing a solution we mapped where ceiling fans under-perform in Indian homes: <b>28 room/usage conditions</b> (false ceilings, hot roofs, monsoon humidity, beds and mosquito nets under the fan, inverter power, …), each researched against ~600 sources, scored on a fixed rubric and stress-tested in a hostile review. The strongest finding drove everything in this abstract:</p>
<div class="box"><b>Fans are designed and rated at maximum speed in an open test chamber. They are used at low speed, at night, over a bed, while the room cools several °C and humidity climbs.</b> A fixed blade and a fixed speed step cannot be right for both a 34 °C afternoon and a 25 °C dawn — so the user wakes up and reaches for the remote. We found no fan product or active patent that changes blade shape automatically with the room.</div>
<p class="muted" style="margin-top:8pt">Reading guide — p.1: idea and quantified claims · p.2: why it is technically feasible, including safety · p.3: components, cost, sourcing risk and the build plan to Round 2.</p>
</div>

<!-- ============ PAGE 1 ============ -->
<div class="page">
<h2><span class="n">1</span>The idea — what we are building and how it works</h2>
<p>We are building a ceiling fan that adapts at three levels. <b class="hot">Body:</b> the outer 35 % of each blade carries a 25 %-chord trailing-edge flap turned by a helical <b>thermostatic-bimetal coil</b> that sits in the blade's own airflow. Above a 28 °C neutral point the flap deflects down (~0.8° per °C), adding camber and effective pitch so every revolution moves more air; below it the flap rises and the fan gives a softer, lower-power draft. Nothing on the rotor needs power — the blade is the thermostat, and it keeps working on a plain wall regulator. <b class="acc">Reflex:</b> a temperature/humidity sensor feeds firmware that converts T × RH into a target air speed at the person (ASHRAE-55 / Indian IMAC comfort models), then shapes RPM into a slow, natural "breeze", an inaudible sleep ramp, or a humid-flush pattern. <b class="acc">Brain:</b> an ESP32-C6 learns each household's comfort offset from their own remote overrides and shifts the Reflex target — fully offline, &lt; 2 KB of RAM. The firmware infers the blade's current shape from motor current, so the mechanics and the software never double-react to the same heat.</p>

<div class="fig">{fig_blade()}</div>
<p class="cap">Fig. 1 — The Body layer. The rigid front 75 % of the blade is unchanged and carries every primary load; only a light flap moves. Coil length 250 mm, strip 20 × 0.5 mm, high-flexivity bimetal.</p>

<h2><span class="n">2</span>Baseline vs target — what we will prove, and how</h2>
<table>
<tr><th style="width:27%">Metric</th><th style="width:20%">Baseline (today's fan)</th><th style="width:21%">Our target</th><th>How we measure it</th></tr>
<tr><td>Air delivery at a fixed speed setting, room at 35 °C vs 22 °C</td><td>0 % — blade is fixed</td><td class="num"><span class="hot">+10 to +15 % hot</span><br><span class="cool">−8 to −10 % cool</span></td><td>Same motor &amp; RPM, swap stock ↔ morphing blades (true A/B); anemometer grid 1.5 m below</td></tr>
<tr><td>Power at a fixed speed setting in a cool room (20–22 °C)</td><td>unchanged</td><td class="num">≈ −20 to −25 %</td><td>Wattmeter on driver input</td></tr>
<tr><td>Energy / electronics needed for that adaptation</td><td>—</td><td class="num">0 W · 0 sensors on rotor</td><td>By design; demo with electronics switched off</td></tr>
<tr><td>Flap response to a room temperature step</td><td>—</td><td class="num">τ ≈ 10–30 s · ≥ 0.6°/°C</td><td>Thermal chamber 15 → 45 °C, laser-on-mirror</td></tr>
<tr><td>Mean RPM needed for the same comfort vote (breeze vs steady air)</td><td>steady RPM</td><td class="num">≥ 10 % lower RPM (≈ −25 % motor power)</td><td>Blind A/B, ≥ 8 volunteers, sensation vote at 30 °C</td></tr>
<tr><td>Night: speed-change rate &amp; noise at bed height</td><td>step change per speed level</td><td class="num">≤ 3 RPM/s ramps · ≤ 32 dB(A)</td><td>Sound meter 1.2 m below hub; RPM log from tach</td></tr>
<tr><td>Manual remote corrections per night</td><td>logged in week 1 (3 users)</td><td class="num">≤ 0.3 after 7 nights</td><td>30-day synthetic user, then live logs</td></tr>
<tr><td>AC set-point at equal comfort <span class="muted">(stretch)</span></td><td>24 °C</td><td class="num">26 °C (≈ −12 % AC energy)</td><td>BEE: ~6 % AC energy per °C</td></tr>
</table>

<h2><span class="n">3</span>Why we believe this is new</h2>
<ul>
<li><b>A passively morphing ceiling-fan blade.</b> Passive thermal pitch control exists only in an expired 1982 automotive engine-fan patent (US 4,487,551); fan patents we found change pitch only manually. Full search before Round 2.</li>
<li><b>Motor current as a blade-shape sensor.</b> A morphed blade needs more torque at the same RPM; the driver's current-vs-RPM residual tells the firmware the flap angle for free — closing the loop between passive mechanics and active control.</li>
<li><b>Learning a comfort offset, not a schedule.</b> "Speed 4 at 11 pm" learned in a heatwave misfires in the monsoon; "this user likes 1 °C cooler than the model" does not.</li>
</ul>
</div>

<!-- ============ PAGE 2 ============ -->
<div class="page">
<h2><span class="n">4</span>Technical feasibility — how it works and why it is buildable</h2>

<h3>Body — the morphing blade (numbers we designed to)</h3>
<p><b>Actuator choice.</b> We compared eight smart materials. <b>Thermostatic bimetal</b> wins: linear, no functional hysteresis or fatigue, cheap, and proven for decades inside rotating automotive fan clutches. NiTi shape-memory wire with a steel bias spring is our backup (two-state "snap" version at the blade root); shape-memory polymers and liquid-crystal elastomers creep under centrifugal load, wax actuators weigh 50–120 g and take minutes, and "trained" two-way NiTi loses 30–60 % of its stroke over time.</p>
<p><b>Stroke.</b> Coil rotation θ = k·L·ΔT / t: with specific curvature k ≈ 28 × 10⁻⁶ K⁻¹ (high-flex grade, to confirm on datasheet), L = 250 mm, t = 0.5 mm → <b>≈ 0.8° per °C</b>, ±8° over a ±10 °C swing. With flap effectiveness ≈ 0.5, that is ~4° effective angle change on the outer span — which, by r² weighting, produces ~60 % of the blade's thrust. Since flow scales roughly with √thrust, <b>+10–15 % air delivery</b> at the same RPM is a conservative blade-element estimate.</p>
<p><b>Loads.</b> Dynamic pressure at the flap (r ≈ 0.52 m, 350 RPM) is ≈ 220 Pa, giving a hinge moment of ≈ 3 N·mm. Coil stiffness is ≈ 2 N·mm per degree (blocked torque ≈ 17 N·mm per 10 °C), and a 20 % overhang balance halves the air load → <b>speed-induced flap error &lt; 1°</b>; the slight back-off at top speed acts as a natural limiter. Centrifugal pull on the 15 g flap is <b>10 N at 350 RPM and 16 N at the 1.25× overspeed test (438 RPM)</b>, taken axially by a thrust shoulder on a 3 mm stainless hinge pin rated well over 1 kN.</p>
<p><b>Thermal response.</b> A 0.5 mm steel strip in 5–19 m/s airflow has a time constant of ≈ 10–30 s — the blade tracks the room, not the motor (the coil sits 0.44 m from the hub). Ceiling-level air is 1–2 °C warmer than at the bed; the neutral point is set by rotating the coil arbor (a calibration screw), not by changing parts.</p>

<h3>Reflex — climate-tuned speed patterns</h3>
<p>Air movement of ~1 m/s at the occupant offsets ≈ 2–3 °C of operative temperature (ASHRAE 55, SET method). A 16-row T × RH map (50–350 RPM) sets the base speed. Human studies show fluctuating airflow at <b>0.2–1 Hz with a 1/f ("natural wind") spectrum</b> feels cooler than steady air at the same mean speed. The rotor's inertia (≈ 0.06 kg·m²) makes 0.5 Hz speed swings costly (~+28 % energy), so we split the job: firmware makes <b>slow ±10–15 % swings over 10–30 s with jerk-limited S-curves (≤ 12 RPM/s, ≤ 10 % extra torque)</b>, and the blade wake supplies the fast gusts. <b>Sleep</b> holds a ≤ 150 RPM band and ramps at ≤ 3 RPM/s as the room cools. <b>Humid-flush</b> (≥ 32 °C and ≥ 70 % RH, where extra speed adds little evaporative cooling) uses a low base speed with a short burst every ~45 s.</p>

<h3>Brain — tiny offline learning</h3>
<p>Overrides are binned by half-hour × {{awake, asleep}} into a table of comfort offsets (°C) with Beta-Bayesian confidence. A change is adopted only if it repeats on <b>two consecutive nights</b>; one-offs decay. It runs in <b>&lt; 2 KB RAM and &lt; 100 cycles per update</b> on an ESP32-C6 (≈ ₹113 at volume, Wi-Fi 6/BLE/Thread → Matter). We rejected on-device neural networks (forgetting, flash wear) and bandit "exploration" (nobody wants an experiment at 2 am). A 24 GHz radar sees a <b>sleeping</b> person's breathing where PIR fails; lights-off marks bedtime. Cold start uses the physics map; seasons shifting the weekly mean temperature fall back to physics until new habits form; two disagreeing users default to the lower speed. Learned data is saved daily plus a brown-out-triggered save (~12 ms); everything stays on the device.</p>

<div class="box warn"><b>Safety-critical aspects.</b> (1) <b>No electronics, wiring or slip rings on the rotor.</b> (2) Flap retained by pin + thrust shoulder designed for the 438 RPM overspeed case; hard stops at −6° / +10° prevent over-travel above 45 °C; a light torsion spring returns the flap to the stock (neutral) shape if a coil breaks — failure looks like a normal fan. (3) Three actuators matched as a set; blade-tip tracking ≤ 2 mm verified by strobe before every spin test; spin tests run behind a mesh guard. (4) Bimetal isolated from aluminium by POM bushes and nickel plating (monsoon galvanic corrosion). (5) A manual command always overrides automation within 50 ms; RPM limits are clamped in the driver; a watchdog falls back to the last manual speed. (6) Our prototype electronics are <b>24 V SELV</b> — no team-built mains circuitry; the product path is a UART link to the fan's existing controller.</div>

<h3>Situations it handles — one product, not eight modes</h3>
<table>
<tr><th style="width:34%">Situation</th><th>What the fan does</th><th style="width:16%">Layer</th></tr>
<tr><td>Hot afternoon, 34 °C / 50 % RH</td><td>Flaps down (more air per rev) + breeze pattern at a higher target speed</td><td>Body + Reflex</td></tr>
<tr><td>Cool dawn or winter, 22–25 °C</td><td>Flaps up — softer, lower-power draft; base speed steps down without a click</td><td>Body + Reflex</td></tr>
<tr><td>Monsoon, 30 °C / 80 % RH</td><td>Humid-flush bursts instead of pointless top speed</td><td>Reflex</td></tr>
<tr><td>Person asleep and still</td><td>Radar keeps Sleep mode on (a PIR fan would switch off)</td><td>Brain</td></tr>
<tr><td>User always wants it cooler around 1 am</td><td>Learns a −1 °C offset; applies it from night 3</td><td>Brain</td></tr>
<tr><td>Power cut, Wi-Fi down, plain regulator</td><td>Blades still adapt; learned habits survive in flash</td><td>Body</td></tr>
<tr><td>Electronics fault</td><td>Watchdog → last manual speed; blade adaptation unaffected</td><td>Safety</td></tr>
</table>
</div>

<!-- ============ PAGE 3 ============ -->
<div>
<h2><span class="n">5</span>Execution feasibility</h2>
<h3>System-level block diagram</h3>
<div class="fig">{fig_blocks()}</div>
<p class="cap">Fig. 2 — Two independent paths reach the air: an electronic path (sensors → ESP32-C6 → driver → motor) and a passive path (room air → bimetal → flap). Motor current closes the loop between them.</p>

<div class="cols">
<div>
<h3>Components &amp; rough BOM (Level-1 prototype)</h3>
<table>
<tr><th>Item</th><th>≈ ₹</th><th>Risk</th></tr>
<tr><td>1200 mm 24 V BLDC ceiling fan + 2nd blade set (stock A/B reference)</td><td class="num">4,500</td><td class="hot">Med</td></tr>
<tr><td>High-flex bimetal strip, 1 m (coils wound in-house)</td><td class="num">1,200</td><td class="hot">Med</td></tr>
<tr><td>NiTi wire + bias springs (Concept B backup)</td><td class="num">1,300</td><td>Low</td></tr>
<tr><td>PETG flaps, SS pins, POM bushes, torsion springs</td><td class="num">1,500</td><td>Low</td></tr>
<tr><td>ESP32-C6 DevKit, SHT40, LD2410, VEML7700, IR rx</td><td class="num">2,000</td><td>Low</td></tr>
<tr><td>INA226, optical tach, 24 V SMPS, buck, wiring</td><td class="num">1,200</td><td>Low</td></tr>
<tr><td>Vane anemometer, sound meter, thermal test box</td><td class="num">3,300</td><td>Low</td></tr>
<tr><td><b>Total (order of magnitude)</b></td><td class="num">≈ 15,000</td><td></td></tr>
</table>
<p class="muted" style="font-size:7.6pt">At volume (our estimate): 3 coils + flaps + pins ≈ ₹150–250; sensors + MCU ≈ ₹200–250, less if the fan's existing Wi-Fi module hosts the firmware.</p>
</div>
<div>
<h3>Component sourcing risk</h3>
<ul>
<li><b>Bimetal strip</b> — Indian manufacturer (Shivalik Bimetal), but sample lead time may be 1–3 weeks. <i>Fallback:</i> coils from dial thermometers / automotive fan-clutch spares for the first static tests.</li>
<li><b>24 V BLDC fan</b> — must accept an external speed command. <i>Fallback:</i> off-the-shelf 24 V sensorless BLDC driver.</li>
<li><b>Custom-fabricated:</b> flaps (3D-printed), coil winding + stress relief, trailing-edge slot machining — all in-house.</li>
<li><b>Imported:</b> LD2410, ESP32-C6 modules — stocked by Indian distributors; nothing long-lead.</li>
</ul>
<h3>What we deliberately do not claim</h3>
<p style="font-size:8pt">Morphing does not give "free" air: by momentum theory +12 % flow costs ~+40 % ideal power whichever way you get it. The gain is <b>who decides</b> (the blade, passively), a <b>lower-power gentle mode</b> when cool, and — our hypothesis to test — <b>less noise</b> than buying the same air with tip speed (+12 % RPM ≈ +2.5 dB by V⁵ scaling).</p>
</div>
</div>

<h3>Build plan to Round 2 — a working Level-1 prototype</h3>
<table>
<tr><th style="width:9%">Week</th><th style="width:47%">Body (mechanics)</th><th>Reflex + Brain (firmware)</th></tr>
<tr><td><b>1</b></td><td>Order parts; wind &amp; stress-relieve 4 coils; static chamber 15 → 45 °C. <b>Go/no-go:</b> ≥ 0.6°/°C, trio matched within ±0.1°/°C — else switch to NiTi root hinge (Concept B).</td><td>ESP32-C6 bring-up: SHT40, radar, IR remote decode, tach, INA226; closed-loop RPM control on the 24 V driver.</td></tr>
<tr><td><b>2</b></td><td>Slot blades, fit flaps; spin test 50 → 350 → 438 RPM behind guard; strobe tip tracking; record current-vs-RPM signature at each flap angle.</td><td>T × RH map + Breeze / Sleep / Humid-flush profiles; habit learner validated on a 30-day synthetic user on PC, then ported.</td></tr>
<tr><td><b>3</b></td><td>A/B airflow grid (stock vs morphing set) with the room at ~22 °C and heated to ~35 °C; power and noise at each speed.</td><td>Blade-state estimator from current residual; integrate all three layers; safety overrides &amp; watchdog tests.</td></tr>
<tr><td><b>4</b></td><td colspan="2"><b>Level-1 demo:</b> one fan, three layers. Warm the blade and watch the flap move with every electronic switched off; anemometer reading rises live. Then a live dashboard of T, RH, RPM, estimated flap angle and learned offset — plus our measured data pack against every target in Section 2.</td></tr>
</table>
</div>
</body></html>"""

out_html = HERE / "abstract.html"
out_html.write_text(HTML, encoding="utf-8")
pdf = HERE / f"{TEAM['name'].strip('[]').replace(' ', '')}_Track1.pdf"
subprocess.run(["weasyprint", str(out_html), str(pdf)], check=True)
print(pdf)
