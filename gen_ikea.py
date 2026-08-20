#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# BLOCAJ-COLT — desene izometrice, stil montaj IKEA.
# Un singur subiect: pe ce sta scandura noua din golul de la coltul din spate.
# Doua camere: ANSAMBLU (de deasupra puntii) si DETALIU (din afara, de la marginea puntii).
import math, json

C = math.cos(math.radians(30))
S = 0.5

INK="#1c1b18"; ACC="#14532d"; ACC2="#8a3016"; MUT="#6b675e"; LN="#cfc9bc"
GHOST = '#b9b1a0'
VOID  = '#463f35'

MAT = {
 'old':   dict(top='#e6ddc9', a='#d2c6aa', b='#bdae8d', edge='#8f8878'),
 'new':   dict(top='#e6ddc9', a='#d2c6aa', b='#bdae8d', edge=ACC2),
 'post':  dict(top='#d9cdb2', a='#c2b492', b='#ad9d78', edge='#5f5748'),
 'metal': dict(top='#cfcabe', a='#b6b0a3', b='#9c9587', edge=ACC2),
}

HATCH = ('<defs><pattern id="cuth" width="20" height="20" patternUnits="userSpaceOnUse" '
         'patternTransform="rotate(45)"><rect width="20" height="20" fill="#ded6c6"/>'
         '<line x1="0" y1="0" x2="0" y2="20" stroke="#a89d87" stroke-width="4"/></pattern></defs>')

def esc(s): return s.replace('&','&amp;').replace('<','&lt;')


class Iso:
    """mirror=False -> privitor la +x,+y,+z (de deasupra puntii): fete vizibile x1, y1, z1
       mirror=True  -> privitor la -x,+y,+z (din afara puntii):   fete vizibile x0, y1, z1"""
    def __init__(self, mirror=False):
        self.el = []; self.pts = []; self.defs = ''; self.m = mirror

    def p(self, x, y, z, track=True):
        sx = (y - x) * C if self.m else (x - y) * C
        sy = (x + y) * S - z
        if track: self.pts.append((sx, sy))
        return (sx, sy)

    def _poly(self, pts3, fill, stroke, sw, dash=None):
        pp = [self.p(*q) for q in pts3]
        d = f' stroke-dasharray="{dash}"' if dash else ''
        s = ' '.join(f'{a:.1f},{b:.1f}' for a, b in pp)
        self.el.append(f'<polygon points="{s}" fill="{fill}" stroke="{stroke}" '
                       f'stroke-width="{sw}" stroke-linejoin="round"{d}/>')

    def seg3(self, a, b, stroke=INK, sw=5, dash=None):
        (x1,y1), (x2,y2) = self.p(*a), self.p(*b)
        self.seg2(x1, y1, x2, y2, stroke, sw, dash)

    def seg2(self, x1, y1, x2, y2, stroke=INK, sw=5, dash=None):
        self.pts += [(x1,y1),(x2,y2)]
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                       f'stroke="{stroke}" stroke-width="{sw}"{d} stroke-linecap="round"/>')

    def txt2(self, x, y, s, size=36, fill=INK, anchor='middle', weight='normal'):
        self.pts += [(x - len(s)*size*0.34, y + size*0.4), (x + len(s)*size*0.34, y - size)]
        self.el.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="ui-monospace,Menlo,monospace" '
                       f'font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
                       f'font-weight="{weight}">{esc(s)}</text>')

    # ---------- corpuri ----------
    def _faces(self, b):
        x, y, z, dx, dy, dz = b
        x1, y1, z1 = x+dx, y+dy, z+dz
        xs = x if self.m else x1                      # fata laterala vizibila in x
        return ([(xs,y,z),(xs,y1,z),(xs,y1,z1),(xs,y,z1)],
                [(x,y1,z),(x1,y1,z),(x1,y1,z1),(x,y1,z1)],
                [(x,y,z1),(x1,y,z1),(x1,y1,z1),(x,y1,z1)])

    def box(self, b, mat, sw=5, cut=None):
        m = MAT[mat]; fa, fb, ft = self._faces(b)
        self._poly(fa, m['a'], m['edge'], sw)
        self._poly(fb, cut or m['b'], m['edge'], sw)
        self._poly(ft, m['top'], m['edge'], sw)

    def wire(self, b, stroke=GHOST, sw=4, dash='14,10'):
        for fp in self._faces(b):
            self._poly(fp, 'none', stroke, sw, dash=dash)

    def quad(self, pts3, fill, stroke='none', sw=0):
        self._poly(pts3, fill, stroke, sw)

    # ---------- sageti / suruburi ----------
    def arrow2(self, x1, y1, x2, y2, color=ACC2, sw=10, head=28):
        self.seg2(x1, y1, x2, y2, stroke=color, sw=sw)
        a = math.atan2(y2-y1, x2-x1)
        for k in (a+2.55, a-2.55):
            self.seg2(x2, y2, x2+head*math.cos(k), y2+head*math.sin(k), stroke=color, sw=sw)

    def screw3(self, a, b, color='#43403a', sw=9, buried=True):
        ax, ay = self.p(*a); bx, by = self.p(*b)
        vx, vy = bx-ax, by-ay
        self.seg2(ax, ay, ax+vx*0.18, ay+vy*0.18, stroke=color, sw=sw)
        self.seg2(ax+vx*0.18, ay+vy*0.18, bx, by, stroke=color, sw=sw,
                  dash='16,12' if buried else None)
        self.el.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="12" fill="{color}"/>')

    def svg(self, pad=80):
        xs = [q[0] for q in self.pts]; ys = [q[1] for q in self.pts]
        x0, x1 = min(xs)-pad, max(xs)+pad
        y0, y1 = min(ys)-pad, max(ys)+pad
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {y0:.0f} '
                f'{x1-x0:.0f} {y1-y0:.0f}" style="width:100%;height:auto;display:block">'
                + self.defs + '\n'.join(self.el) + '</svg>')


# ============================================================
# SCENA (mm). z = 0 -> fata de sus a dusumelei existente.
# ============================================================
YMAX  = 340
POST  = (  0,  40, -330,  90,  90, 480)
BEAM  = (190,   0, -128,  70, YMAX, 100)
DECK  = (190,   0,  -28, 200, YMAX,  28)
BLOCK = ( 90,  20, -128,  88, 290, 100)
COVER = ( 88,  15,  -28,  92, 300,  28)

BRA = [(178, 120, -128, 12, 60, 90), (108, 120, -140, 82, 60, 12)]
BRB = [(178, 235, -128, 12, 60, 90), (108, 235, -140, 82, 60, 12)]
BRACKETS = [BRA, BRB]


def base(f):
    f.quad([(90,0,0),(190,0,0),(190,YMAX,0),(90,YMAX,0)], VOID)     # golul, vazut de sus
    f.box(POST, 'post'); f.box(BEAM, 'old'); f.box(DECK, 'old')


def brackets(f, screws=True):
    for v, h in BRACKETS:
        f.box(h, 'metal', sw=4); f.box(v, 'metal', sw=4)
    if not screws: return
    for (vx, vy, vz, vdx, vdy, vdz) in [b[0] for b in BRACKETS]:
        for zz in (vz+26, vz+64):
            f.screw3((vx, vy+30, zz), (vx+52, vy+30, zz), sw=8)


def guides(f, b, dz):
    x, y, z, dx, dy, _ = b
    for cx, cy in [(x, y+dy), (x+dx, y+dy), (x+dx, y)]:
        a = f.p(cx, cy, z+dz, track=False); c = f.p(cx, cy, z, track=False)
        f.seg2(a[0], a[1], c[0], c[1], stroke=GHOST, sw=3, dash='13,10')


figs = {}

# ------------------------------------------------------------
# 1 · ASA E ACUM
# ------------------------------------------------------------
f = Iso()
base(f)
f.seg3((90, YMAX, 0), (190, YMAX, 0), stroke=MUT, sw=5)
f.seg3((90, YMAX, -18), (90, YMAX, 18), stroke=MUT, sw=5)
f.seg3((190, YMAX, -18), (190, YMAX, 18), stroke=MUT, sw=5)
lx, ly = f.p(140, YMAX, 0, track=False)
f.seg2(lx, ly + 26, lx - 96, ly + 92, stroke=MUT, sw=4)
f.txt2(lx - 110, ly + 106, 'gol ~100', size=38, fill=MUT, weight='bold', anchor='end')
ax, ay = f.p(140, 250, -170, track=False)
f.arrow2(ax, ay, ax, ay + 250, color=ACC2, sw=10)
f.txt2(ax, ay + 314, 'nimic dedesubt', size=40, fill=ACC2, weight='bold')
figs['acum'] = f.svg()

# ------------------------------------------------------------
# 2 · DOUA COLTARE, INSURUBATE IN GRINDA GROASA
# ------------------------------------------------------------
f = Iso()
base(f)
brackets(f)
figs['coltare'] = f.svg()

# ------------------------------------------------------------
# 3 · BLOCAJUL SE LASA PE COLTARE   <- raspunsul la "pe ce sta"
# ------------------------------------------------------------
LIFT = 320
f = Iso()
base(f)
brackets(f, screws=False)
f.wire(BLOCK)
f.box((BLOCK[0], BLOCK[1], BLOCK[2]+LIFT, BLOCK[3], BLOCK[4], BLOCK[5]), 'new')
guides(f, BLOCK, LIFT)
mx, my = f.p(134, 165, BLOCK[2]+LIFT+100, track=False)
f.arrow2(mx, my-210, mx, my-64, color=ACC2, sw=12, head=32)
figs['blocaj'] = f.svg()

# ------------------------------------------------------------
# 4 · SURUBURI OBLICE, DE SUS: in grinda si in stalp
# ------------------------------------------------------------
f = Iso()
base(f)
brackets(f, screws=False)
f.box(BLOCK, 'new')
for sy in (80, 165, 250):
    f.screw3((152, sy, -28), (248, sy, -122))
for sy in (60, 110):
    f.screw3((112, sy, -28), (26, sy, -118))
figs['suruburi'] = f.svg()

# ------------------------------------------------------------
# 5 · SCANDURA DE CALCAT, DEASUPRA
# ------------------------------------------------------------
LIFTC = 260
f = Iso()
base(f)
brackets(f, screws=False)
f.box(BLOCK, 'new')
f.wire(COVER)
f.box((COVER[0], COVER[1], COVER[2]+LIFTC, COVER[3], COVER[4], COVER[5]), 'new')
guides(f, COVER, LIFTC)
mx, my = f.p(134, 165, COVER[2]+LIFTC+28, track=False)
f.arrow2(mx, my-190, mx, my-56, color=ACC2, sw=12, head=32)
figs['scandura'] = f.svg()

# ------------------------------------------------------------
# 6 · GATA
# ------------------------------------------------------------
f = Iso()
base(f)
brackets(f, screws=False)
f.box(BLOCK, 'new'); f.box(COVER, 'new')
figs['gata'] = f.svg()

# ------------------------------------------------------------
# 7 · DETALIU MARE — alta camera: privit din afara puntii.
#     Blocajul e taiat, ca sa se vada polita coltarului de dedesubt.
# ------------------------------------------------------------
DY0, DY1, DCUT = 40.0, 250.0, 150.0
f = Iso(mirror=True)
f.defs = HATCH
CUT = 'url(#cuth)'
f.box((190, DY0, -128, 70, DY1-DY0, 100), 'old')
f.box((190, DY0,  -28, 90, DY1-DY0,  28), 'old')
f.box((108, 170, -140, 82, 60, 12), 'metal', sw=4)
f.box((178, 170, -128, 12, 60, 90), 'metal', sw=4)
f.box(( 90, DY0, -128, 88, DCUT-DY0, 100), 'new', cut=CUT)
f.box(( 88, DY0-6, -28, 92, DCUT-DY0+6, 28), 'new', cut=CUT)
for zz in (-102, -60):
    f.screw3((178, 200, zz), (236, 200, zz), sw=8)
a1 = f.p(134, DCUT, 250, track=False); a2 = f.p(134, DCUT, 46, track=False)
f.arrow2(a1[0], a1[1], a2[0], a2[1], color=ACC2, sw=14, head=38)
figs['detaliu'] = f.svg()

# ------------------------------------------------------------
# 8 · NU ASA
# ------------------------------------------------------------
f = Iso()
base(f)
f.box(COVER, 'new')
ax, ay = f.p(140, 322, -60, track=False)
f.arrow2(ax, ay, ax, ay+220, color=ACC2, sw=10)
cx, cy = f.p(134, 165, 0, track=False)
for dx in (-1, 1):
    f.seg2(cx + dx*176, cy - 120, cx - dx*176, cy + 120, stroke=ACC2, sw=20)
figs['nu'] = f.svg()

# ------------------------------------------------------------
# PLAN mic — cele doua laturi ale golului, la fiecare colt
# ------------------------------------------------------------
f = Iso()
f.el += ['<rect x="0" y="0" width="330" height="70" fill="#cfc9bc" stroke="#1c1b18" stroke-width="5"/>',
         '<rect x="0" y="70" width="70" height="260" fill="#cfc9bc" stroke="#1c1b18" stroke-width="5"/>',
         '<rect x="70" y="70" width="100" height="100" fill="#d9cdb2" stroke="#1c1b18" stroke-width="5"/>',
         '<polygon points="270,70 330,70 330,330 70,330 70,270 270,270" fill="#e6ddc9" stroke="#1c1b18" stroke-width="5"/>',
         '<polygon points="170,70 270,70 270,270 70,270 70,170 170,170" fill="none" stroke="#8a3016" stroke-width="8"/>']
f.pts += [(0,0),(330,330)]
f.txt2(222, 152, 'A', size=48, fill=ACC2, weight='bold')
f.txt2(120, 238, 'B', size=48, fill=ACC2, weight='bold')
figs['plan'] = f.svg(pad=40)

# ------------------------------------------------------------
# ICOANE PIESE
# ------------------------------------------------------------
f = Iso(); f.box((0,0,0, 88, 290, 100), 'new'); figs['ic_blocaj'] = f.svg(pad=30)
f = Iso(mirror=True); f.box((0,0,-12, 82, 60, 12), 'metal', sw=4); f.box((70,0,0, 12, 60, 90), 'metal', sw=4)
figs['ic_coltar'] = f.svg(pad=30)
f = Iso(); f.box((0,0,0, 92, 300, 28), 'new'); figs['ic_scandura'] = f.svg(pad=30)
f = Iso()
f.seg2(0, 0, 250, 0, stroke='#43403a', sw=18)
for i in range(9):
    x = 66 + i*20
    f.seg2(x, -17, x, 17, stroke='#43403a', sw=5)
f.seg2(0, -30, 0, 30, stroke='#43403a', sw=18)
f.seg2(250, 0, 292, 0, stroke='#43403a', sw=7)
figs['ic_surub'] = f.svg(pad=30)

json.dump(figs, open('figs_ikea.json', 'w'))
print('ok', {k: len(v) for k, v in figs.items()})
