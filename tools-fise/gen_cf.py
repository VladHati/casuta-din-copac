# -*- coding: utf-8 -*-
"""Generator FISA-MONTAJ-contravantuiri. Toate desenele din mm reali."""

# ---------------- GEOMETRIE AS-BUILT (mm) ----------------
# X = latime, 0 = axa stalpilor din stanga (S1 spate / S4 fata), 2100 = dreapta (S2/S3)
# Y = adancime, 0 = axa stalpilor spate, 1780 = axa stalpilor fata, 2480 = nasul consolei
# Z = inaltime de la sol
P = 100          # stalp 100x100
GL_W, GL_H = 90, 200     # glulam 90x200
GL_LEN_X = (-100, 2200)  # glulam 2300, 100 iesire de fiecare parte
Z_GL_B, Z_GL_T = 1900, 2100
Z_JO_B, Z_JO_T = 2100, 2200
Z_DECK = 2228
Y_FRONT = 1780
Y_NOSE = 2480
JOISTS = [0, 280, 720, 1120, 1550, 2100]
Y_JO_BACK = 40
GLF_Y = (Y_FRONT - GL_W / 2, Y_FRONT + GL_W / 2)   # 1735..1825
GLB_Y = (50, 50 + GL_W)                            # 50..140  (in FATA stalpilor spate)
Z_TALPIC = (1620, 1800)
Z_POLITA = (1800, 1900)
TREE_X, TREE_Y, TREE_D = 500, Y_FRONT + 200, 160

# ---------------- CONTRAFISE ----------------
# fiecare: (nume, plan, z_jos, z_sus, run)
CF = {
    'CF1': dict(z0=1400, z1=2000, run=600),   # S4 -> glulam fata, spre +X
    'CF2': dict(z0=1400, z1=2000, run=600),   # S3 -> glulam fata, spre -X
    'CF3': dict(z0=1500, z1=2150, run=650),   # S4 -> joista 0, inainte (sub consola)
    'CF4': dict(z0=1500, z1=2150, run=650),   # S3 -> joista 2100, inainte
    'CF5': dict(z0=1450, z1=2150, run=700),   # S1 -> joista 0, inainte
    'CF6': dict(z0=1450, z1=2150, run=700),   # S2 -> joista 2100, inainte
}
CF7 = dict(z_s1=700, z_s2=1400)               # diagonala planului spate
T = 100  # grosime contrafisa (offcut 100x100 pus PLAT)

# ---------------- SVG helpers ----------------
CSS = """
  .w{fill:#e9e3d8;stroke:#8d8271;stroke-width:5}
  .w2{fill:#d6cab2;stroke:#5f574a;stroke-width:5}
  .st{fill:#ded5c4;stroke:#6f6656;stroke-width:5}
  .cf{fill:#f6d3cf;stroke:#b3261e;stroke-width:8}
  .old{fill:#dfe9e1;stroke:#1a6b3c;stroke-width:5}
  .hid{fill:none;stroke:#9a9a9a;stroke-width:4;stroke-dasharray:26 18}
  .gnd{stroke:#1a1a1a;stroke-width:7}
  .ctr{stroke:#b3261e;stroke-width:3;stroke-dasharray:40 14 8 14}
  .dimL{stroke:#b3261e;stroke-width:4}
  .lead{stroke:#444;stroke-width:4}
  .t{font-family:Helvetica,Arial,sans-serif;font-size:62px;fill:#1a1a1a}
  .ts{font-family:Helvetica,Arial,sans-serif;font-size:52px;fill:#555}
  .tb{font-family:Helvetica,Arial,sans-serif;font-size:66px;fill:#b3261e;font-weight:bold}
  .tg{font-family:Helvetica,Arial,sans-serif;font-size:52px;fill:#1a6b3c;font-weight:bold}
  .d{font-family:'Courier New',monospace;font-size:56px;fill:#b3261e;font-weight:bold}
  .ds{font-family:'Courier New',monospace;font-size:48px;fill:#444}
"""


def svg(vb, width_mm, body, extra=""):
    x0, y0, w, h = vb
    return (f'<svg viewBox="{x0} {y0} {w} {h}" style="width:{width_mm}mm;height:auto" '
            f'xmlns="http://www.w3.org/2000/svg">'
            f'<defs><marker id="a" markerWidth="9" markerHeight="9" refX="8" refY="4.5" '
            f'orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="#b3261e"/></marker>'
            f'<marker id="ag" markerWidth="9" markerHeight="9" refX="8" refY="4.5" '
            f'orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="#444"/></marker></defs>'
            f'<style>{CSS}{extra}</style>{body}</svg>')


def rect(x, y, w, h, cls, extra=""):
    return f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" class="{cls}" {extra}/>'


def txt(x, y, s, cls="t", anchor="start", rot=None):
    tr = f' transform="rotate({rot} {x:.0f} {y:.0f})"' if rot else ""
    return (f'<text x="{x:.0f}" y="{y:.0f}" class="{cls}" '
            f'text-anchor="{anchor}"{tr}>{s}</text>')


def line(x1, y1, x2, y2, cls="lead", extra=""):
    return (f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
            f'class="{cls}" {extra}/>')


def band(x, y, w, h, ang, cls="cf"):
    """dreptunghi rotit in jurul coltului stanga-jos (pt contrafise inclinate)"""
    return (f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" '
            f'class="{cls}" transform="rotate({ang:.2f} {x:.0f} {y:.0f})"/>')


def dimh(x1, x2, y, label, cls="d", off=0):
    """cota orizontala"""
    s = line(x1, y, x2, y, "dimL", 'marker-end="url(#a)" marker-start="url(#a)"')
    s += line(x1, y - 55, x1, y + 55, "dimL") + line(x2, y - 55, x2, y + 55, "dimL")
    s += txt((x1 + x2) / 2, y - 28 + off, label, cls, "middle")
    return s


def dimv(y1, y2, x, label, side="right"):
    s = line(x, y1, x, y2, "dimL", 'marker-end="url(#a)" marker-start="url(#a)"')
    s += line(x - 55, y1, x + 55, y1, "dimL") + line(x - 55, y2, x + 55, y2, "dimL")
    a = "start" if side == "right" else "end"
    dx = 40 if side == "right" else -40
    s += txt(x + dx, (y1 + y2) / 2 + 20, label, "d", a)
    return s


# =========================================================
# P1 — ELEVATIE FATA  (planul stalpilor din fata, X-Z)
# =========================================================
def view_front():
    b = []
    Z = lambda z: -z  # noqa
    b.append(line(-380, 0, 2480, 0, "gnd"))
    b.append(txt(-380, 90, "sol", "ts"))
    b.append(rect(GL_LEN_X[0], Z(Z_DECK), GL_LEN_X[1] - GL_LEN_X[0], Z_DECK - Z_JO_T, "w"))
    for jx in JOISTS:
        b.append(rect(jx - 50, Z(Z_JO_T), 100, 100, "w2"))
    b.append(rect(GL_LEN_X[0], Z(Z_GL_T), GL_LEN_X[1] - GL_LEN_X[0], GL_H, "st"))
    b.append(txt(1050, Z(2015), "GLULAM FATA 90&#215;200", "ts", "middle"))
    for sx, nm in ((0, "S4"), (2100, "S3")):
        b.append(rect(sx - 50, Z(1900), 100, 1900, "st"))
        b.append(txt(sx, 200, nm, "t", "middle"))
    c = CF['CF1']
    L = ((c['run']) ** 2 + (c['z1'] - c['z0']) ** 2) ** 0.5
    for sx, sgn, nm in ((0, +1, "CF1"), (2100, -1, "CF2")):
        x0 = sx + sgn * 50
        y0 = Z(c['z0'])
        if sgn > 0:
            b.append(f'<g transform="translate({x0},{y0}) rotate(-45)">'
                     f'<rect x="0" y="-{T}" width="{L:.0f}" height="{T}" class="cf"/></g>')
        else:
            b.append(f'<g transform="translate({x0},{y0}) rotate(45)">'
                     f'<rect x="-{L:.0f}" y="-{T}" width="{L:.0f}" height="{T}" class="cf"/></g>')
        b.append(txt(sx + sgn * 640, Z(1470), nm, "tb", "middle"))
    b.append(dimv(Z(c['z0']), Z(c['z1']), -250, "600", "left"))
    b.append(dimh(50, 50 + c['run'], Z(1230), "600"))
    b.append(txt(-250, Z(c['z0']) + 150, "z=1400", "ds", "middle"))
    b.append(txt(1050, Z(1720), "capat sus: pe fata glulamului, la z=2000", "ts", "middle"))
    b.append(txt(1050, Z(1620), "capat jos: pe fata laterala a stalpului, z=1400", "ts", "middle"))
    b.append(txt(1050, Z(900), "CF1 si CF2 stau pe fata DINSPRE INTERIOR (sub podea),", "ts", "middle"))
    b.append(txt(1050, Z(800), "ca sa nu se bata cu trunchiul corcodusului. Aici sunt desenate vizibile.", "ts", "middle"))
    b.append(dimh(0, 2100, 330, "2100 intre axe", "d"))
    b.append(dimv(Z(2228), 0, 2430, "2228"))
    return svg((-620, -2560, 3300, 3000), 168, "".join(b))



# =========================================================
# P2 — ELEVATIE SPATE (planul stalpilor din spate, X-Z)
# =========================================================
def view_back():
    import math
    b = []
    Z = lambda z: -z  # noqa
    TOP = 2700
    b.append(line(-380, 0, 2480, 0, "gnd"))
    b.append(txt(-380, 90, "sol", "ts"))
    for sx, nm in ((0, "S1"), (2100, "S2")):
        b.append(rect(sx - 50, Z(TOP), 100, TOP, "st"))
        b.append(txt(sx, 200, nm, "t", "middle"))
        b.append(f'<path d="M{sx-70},{Z(TOP)+40} l40,-30 l-80,-45 l40,-30 l40,-25" '
                 f'fill="none" stroke="#1a1a1a" stroke-width="6"/>')
        b.append(txt(sx + 110, Z(TOP) + 20, "continua la 4000", "ts"))
    for sx in (0, 2100):
        b.append(rect(sx - 50, Z(Z_POLITA[1]), 100, Z_POLITA[1] - Z_TALPIC[0], "old"))
        b.append(f'<path d="M{sx-50},{Z(Z_TALPIC[0])} l100,0 l0,-160 z" class="old"/>')
    b.append(txt(1050, Z(1660), "polita + talpic + contrafisa 45&#176; (verde) = EXISTENTE", "tg", "middle"))
    b.append(txt(1050, Z(1560), "reazem de nod. NU sunt contravantuire.", "tg", "middle"))
    b.append(rect(GL_LEN_X[0], Z(Z_GL_T), GL_LEN_X[1] - GL_LEN_X[0], GL_H, "st"))
    b.append(txt(1050, Z(2015), "GLULAM SPATE &#8212; sta IN FATA stalpilor, pe polite", "ts", "middle"))
    b.append(rect(GL_LEN_X[0], Z(Z_DECK), GL_LEN_X[1] - GL_LEN_X[0], Z_DECK - Z_JO_T, "w"))
    for jx in JOISTS:
        b.append(rect(jx - 50, Z(Z_JO_T), 100, 100, "w2"))
    x1, z1 = 50, CF7['z_s1']
    x2, z2 = 2050, CF7['z_s2']
    ang = -math.degrees(math.atan2(z2 - z1, x2 - x1))
    L = ((x2 - x1) ** 2 + (z2 - z1) ** 2) ** 0.5
    b.append(f'<g transform="translate({x1},{Z(z1)}) rotate({ang:.2f})">'
             f'<rect x="-110" y="-45" width="{L+220:.0f}" height="145" class="cf"/></g>')
    b.append(txt(1050, Z(1310), "CF7 &#183; diagonala planului spate &#183; rigla 45&#215;145", "tb", "middle"))
    b.append(dimv(Z(0), Z(z1), -250, "700", "left"))
    b.append(dimv(Z(0), Z(z2), 2350, "1400"))
    b.append(txt(1050, Z(430), "singura piesa care nu iese din offcut", "ts", "middle"))
    b.append(dimh(0, 2100, 330, "2100 intre axe", "d"))
    return svg((-620, -2960, 3350, 3400), 168, "".join(b))



# =========================================================
# P3 — SECTIUNE LATERALA (x = 0, planul Y-Z)
# =========================================================
def view_side():
    import math
    b = []
    Z = lambda z: -z  # noqa
    TOP = 2700
    b.append(line(-300, 0, 2760, 0, "gnd"))
    b.append(txt(-300, 90, "sol", "ts"))
    b.append(rect(-50, Z(TOP), 100, TOP, "st"))
    b.append(txt(0, 200, "S1", "t", "middle"))
    b.append(f'<path d="M-70,{Z(TOP)+40} l40,-30 l-80,-45 l40,-30 l40,-25" '
             f'fill="none" stroke="#1a1a1a" stroke-width="6"/>')
    b.append(txt(90, Z(TOP) + 20, "4000", "ts"))
    b.append(rect(Y_FRONT - 50, Z(1900), 100, 1900, "st"))
    b.append(txt(Y_FRONT, 200, "S4", "t", "middle"))
    b.append(rect(GLB_Y[0], Z(Z_GL_T), GL_W, GL_H, "w2"))
    b.append(rect(GLF_Y[0], Z(Z_GL_T), GL_W, GL_H, "w2"))
    b.append(txt(250, Z(2040), "GL spate", "ts"))
    b.append(txt(1620, Z(2040), "GL fata", "ts", "end"))
    b.append(rect(GLB_Y[0], Z(Z_POLITA[1]), 110, Z_POLITA[1] - Z_TALPIC[0], "old"))
    b.append(f'<path d="M50,{Z(Z_TALPIC[0])} l0,-170 l170,170 z" class="old"/>')
    b.append(txt(330, Z(1180), "polita + talpic + contrafisa 45&#176;", "tg"))
    b.append(txt(330, Z(1080), "= EXISTENTE, nu sunt contravantuire", "tg"))
    b.append(rect(Y_JO_BACK, Z(Z_JO_T), Y_NOSE - Y_JO_BACK, 100, "w2"))
    b.append(rect(Y_JO_BACK, Z(Z_DECK), Y_NOSE - Y_JO_BACK, Z_DECK - Z_JO_T, "w"))
    b.append(txt(1330, Z(2155), "JOISTA DE CAPAT 100&#215;100", "ts", "middle"))
    c = CF['CF5']
    ang = -math.degrees(math.atan2(c['z1'] - c['z0'], c['run']))
    L = ((c['run']) ** 2 + (c['z1'] - c['z0']) ** 2) ** 0.5
    b.append(f'<g transform="translate(50,{Z(c["z0"])}) rotate({ang:.2f})">'
             f'<rect x="-40" y="-{T}" width="{L+80:.0f}" height="{T}" class="cf"/></g>')
    b.append(txt(210, Z(1900), "CF5", "tb"))
    c3 = CF['CF3']
    ang3 = -math.degrees(math.atan2(c3['z1'] - c3['z0'], c3['run']))
    L3 = ((c3['run']) ** 2 + (c3['z1'] - c3['z0']) ** 2) ** 0.5
    b.append(f'<g transform="translate({Y_FRONT+50},{Z(c3["z0"])}) rotate({ang3:.2f})">'
             f'<rect x="-40" y="-{T}" width="{L3+70:.0f}" height="{T}" class="cf"/></g>')
    b.append(txt(2250, Z(1810), "CF3", "tb"))
    b.append(txt(2250, Z(1710), "tine si consola", "ts"))
    b.append(rect(Y_FRONT + 50, Z(c3['z0']), 90, 120, "cf"))
    b.append(txt(1640, Z(1520), "blocaj de reazem sub CF3", "tb", "end"))
    b.append(txt(1640, Z(1420), "obligatoriu &#8212; nu lasa sarcina in suruburi", "ts", "end"))
    b.append(line(1670, Z(1540), Y_FRONT + 40, Z(1440), "lead", 'marker-end="url(#ag)"'))
    b.append(dimh(Y_FRONT, Y_NOSE, 330, "700 consola"))
    b.append(dimh(0, Y_FRONT, 570, "1780 intre axe"))
    b.append(dimv(Z(1900), 0, -270, "1900", "left"))
    b.append(dimv(Z(2228), Z(1900), 2700, "328"))
    b.append(txt(2860, Z(1850), "top dusumea 2228", "ds", "end"))
    b.append(dimh(Y_FRONT + 50, Y_FRONT + 50 + c3['run'], Z(2320), "650"))
    b.append(dimh(50, 50 + c['run'], Z(2320), "700"))
    b.append(txt(2860, Z(560), "SPRE CURTE &#8594;", "ts", "end"))
    b.append(txt(-180, Z(560), "&#8592; SPRE GARD", "ts"))
    return svg((-620, -2990, 3620, 3600), 168, "".join(b))



# =========================================================
# P4 — PLAN DE SUS
# =========================================================
def view_plan():
    b = []
    for jx in JOISTS:
        b.append(rect(jx - 50, Y_JO_BACK, 100, Y_NOSE - Y_JO_BACK, "w"))
    b.append(rect(GL_LEN_X[0], GLB_Y[0], GL_LEN_X[1] - GL_LEN_X[0], GL_W, "w2"))
    b.append(rect(GL_LEN_X[0], GLF_Y[0], GL_LEN_X[1] - GL_LEN_X[0], GL_W, "w2"))
    for (sx, sy, nm) in ((0, 0, "S1"), (2100, 0, "S2"), (0, Y_FRONT, "S4"), (2100, Y_FRONT, "S3")):
        b.append(rect(sx - 50, sy - 50, 100, 100, "st"))
        b.append(txt(sx + (95 if sx == 0 else -95), sy + 25, nm, "t",
                     "start" if sx == 0 else "end"))
    b.append(f'<circle cx="{TREE_X}" cy="{TREE_Y}" r="{TREE_D/2}" fill="#e6efe6" '
             f'stroke="#1a6b3c" stroke-width="7"/>')
    b.append(txt(TREE_X, TREE_Y + 250, "corcodus &#216;160", "tg", "middle"))
    # CF1 / CF2 pe fata INTERIOARA a glulamului fata
    yin = GLF_Y[0] - T
    b.append(rect(50, yin, 600, T, "cf"))
    b.append(txt(350, yin - 60, "CF1", "tb", "middle"))
    b.append(rect(2100 - 50 - 600, yin, 600, T, "cf"))
    b.append(txt(1750, yin - 60, "CF2", "tb", "middle"))
    b.append(rect(-150, Y_FRONT + 50, T, 650, "cf"))
    b.append(txt(-200, Y_FRONT + 420, "CF3", "tb", "end"))
    b.append(rect(2150, Y_FRONT + 50, T, 650, "cf"))
    b.append(txt(2300, Y_FRONT + 420, "CF4", "tb", "start"))
    b.append(rect(-150, 50, T, 700, "cf"))
    b.append(txt(-200, 430, "CF5", "tb", "end"))
    b.append(rect(2150, 50, T, 700, "cf"))
    b.append(txt(2300, 430, "CF6", "tb", "start"))
    b.append(rect(0, GLB_Y[1] + 25, 2100, 145, "cf"))
    b.append(txt(1050, GLB_Y[1] + 380, "CF7 &#183; sub glulam, z=700 &#8594; 1400", "tb", "middle"))
    b.append(dimh(0, 2100, -350, "2100"))
    b.append(dimv(0, Y_FRONT, 2640, "1780"))
    b.append(dimv(Y_FRONT, Y_NOSE, 2640, "700"))
    b.append(txt(1050, Y_NOSE + 400, "NAS CONSOLA", "ts", "middle"))
    b.append(txt(1050, -520, "SPRE GARD", "ts", "middle"))
    for jx in JOISTS:
        b.append(txt(jx, Y_NOSE + 190, str(jx), "ds", "middle"))
    b.append(txt(TREE_X + 150, TREE_Y + 480,
                 "CF1/CF2 stau pe fata interioara ca sa ocoleasca trunchiul", "tg"))
    return svg((-620, -680, 3500, 3700), 152, "".join(b))



# =========================================================
# P5 — DETALIU PRINDERE
# =========================================================
def view_detail():
    import math
    b = []
    # detaliu marit, nu la scara
    PW, MH = 300, 300          # latime stalp / inaltime grinda in desen
    b.append(rect(-PW, 0, 2000, MH, "w2"))
    b.append(txt(-PW + 40, MH - 90, "GLULAM (90) sau JOISTA (100)", "ts"))
    b.append(rect(-PW, MH, PW, 2000, "st"))
    b.append(txt(-PW - 60, 620, "STALP", "ts", "end"))
    b.append(txt(-PW - 60, 710, "100&#215;100", "ts", "end"))
    # contrafisa: banda la 45 grade
    A = (-PW - 40, 1720)
    L, W = 2150, 300
    ux, uy = math.cos(math.radians(-45)), math.sin(math.radians(-45))
    nx, ny = -uy, ux            # normala (pointing up-left)
    def pt(t, sv):
        return (A[0] + t * ux + sv * nx, A[1] + t * uy + sv * ny)
    b.append(f'<g transform="translate({A[0]},{A[1]}) rotate(-45)">'
             f'<rect x="0" y="-{W}" width="{L}" height="{W}" class="cf"/></g>')
    # suruburi: triunghi in zona de suprapunere peste stalp
    def screw(p):
        cx, cy = p
        return (f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="46" fill="#fff" stroke="#b3261e" '
                f'stroke-width="14"/><line x1="{cx-32:.0f}" y1="{cy:.0f}" x2="{cx+32:.0f}" '
                f'y2="{cy:.0f}" stroke="#b3261e" stroke-width="14"/>')
    for t, sv in ((190, 100), (190, 205), (340, 152)):
        b.append(screw(pt(t, sv)))
    for t, sv in ((1760, 80), (1760, 230), (1920, 155)):
        b.append(screw(pt(t, sv)))
    b.append(txt(-PW - 120, 1900, "3&#215; Heco 8&#215;160", "tb", "end"))
    b.append(txt(-PW - 120, 2000, "in stalp, in triunghi", "ts", "end"))
    b.append(txt(1560, 300, "3&#215; in glulam", "tb"))
    b.append(txt(1560, 400, "2&#215; in joista (are doar 100 inaltime)", "ts"))
    b.append(txt(340, 1780, "CONTRAFISA &#8212; offcut 100&#215;100", "tb"))
    b.append(txt(340, 1880, "pus PLAT peste ambele piese", "ts"))
    # unghi + cote schematice
    b.append(line(0, 1290, 1290, 1290, "hid"))
    b.append(line(1290, 300, 1290, 1400, "hid"))
    b.append(dimh(0, 1290, 1620, "run = rise"))
    b.append(txt(1130, 1230, "45&#176;", "d"))
    b.append(txt(-PW, 2380, "8&#215;160 prin 100 de contrafisa = 60 mm patrundere.", "t"))
    b.append(txt(-PW, 2480, "Nu iese pe partea cealalta nici prin stalp (100), nici prin glulam (90).", "ts"))
    b.append(txt(-PW, 2580, "Pregauresti &#216;5 DOAR prin contrafisa. Detaliu marit &#8212; nu la scara.", "ts"))
    return svg((-1050, -160, 3350, 2960), 158, "".join(b))



# =========================================================
# P6 — ORDINEA / POARTA DE SECVENTA
# =========================================================
def view_seq():
    b = []
    steps = [
        ("1", "PLAN STANGA", "CF3 + CF5", "apoi scoti X-ul temporar de pe stanga"),
        ("2", "PLAN DREAPTA", "CF4 + CF6", "apoi scoti X-ul temporar de pe dreapta"),
        ("3", "PLAN FATA", "CF1 + CF2", "apoi scoti X-ul temporar din fata"),
        ("4", "PLAN SPATE", "CF7", "proptelele de la VARFUL stalpilor spate RAMAN"),
    ]
    y = 0
    for (n, t1, t2, t3) in steps:
        b.append(rect(0, y, 2600, 300, "w"))
        b.append(f'<rect x="0" y="{y}" width="300" height="300" fill="#1a1a1a"/>')
        b.append(txt(150, y + 205, n, "t", "middle") .replace('fill:#1a1a1a', ''))
        b.append(f'<text x="150" y="{y+205}" text-anchor="middle" '
                 f'font-family="Helvetica" font-size="150" fill="#fff" '
                 f'font-weight="bold">{n}</text>')
        b.append(txt(370, y + 130, t1 + " &#183; " + t2, "t"))
        b.append(txt(370, y + 235, t3, "ts"))
        y += 360
    b.append(f'<rect x="0" y="{y+40}" width="2600" height="300" fill="#fdf1f0" '
             f'stroke="#b3261e" stroke-width="10"/>')
    b.append(txt(60, y + 175, "NICIODATA doua plane descoperite in acelasi timp.", "tb"))
    b.append(txt(60, y + 275, "Contrafisa prinsa la AMBELE capete inainte sa atingi proptelele.", "ts"))
    return svg((-40, -40, 2700, y + 400), 168, "".join(b))


VIEWS = dict(front=view_front(), back=view_back(), side=view_side(),
             plan=view_plan(), detail=view_detail(), seq=view_seq())

if __name__ == "__main__":
    import json, sys
    out = {k: v for k, v in VIEWS.items()}
    with open("views.json", "w") as f:
        json.dump(out, f)
    print("ok", {k: len(v) for k, v in out.items()})
