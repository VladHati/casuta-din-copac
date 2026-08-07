#!/usr/bin/env python3
"""iso2 — generator izometric vectorial (SVG) pentru fisele fazei 2.

Stil IKEA: line-art, piesa noua in accent, pozitia finala ca fantoma punctata,
sageti de miscare, baloane de reper, cote pe toate directiile.

Proiectie izometrica: sx=(x-z)*cos30 ; sy=(x+z)*sin30 - y   (y = sus, mm)
Sortare pictor: cheia = centrul (x+y+z) crescator -> departe intai.
Rulare: python3 iso2.py  -> scrie SVG-uri in ../assets/iso/
"""
import math, os

C30 = math.cos(math.radians(30)); S30 = 0.5

# ---------- paleta ----------
INK   = "#1a1a1a"
BUILT_T, BUILT_L, BUILT_R = "#efece6", "#ded8cc", "#cbc3b3"   # existent
NEW_T,  NEW_L,  NEW_R     = "#f6dcc6", "#eec3a0", "#e0a97e"   # piesa noua
MET_T,  MET_L,  MET_R     = "#e4e6e8", "#cfd3d7", "#b8bdc3"   # metal
ACC   = "#b3261e"
GHOST = "#9a9a9a"


def P(x, y, z):
    return ((x - z) * C30, (x + z) * S30 - y)


class Scene:
    def __init__(self):
        self.items = []   # (depth, svg)
        self.over  = []   # linii/sageti desenate peste geometrie
        self.texts = []   # (x, y, s, cls, anchor) — randate la final, cu fs calculat

    # ---------- primitive ----------
    def box(self, x, y, z, w, h, d, pal="built", label=None, op=1.0, key=None):
        """coltul (x,y,z) = min pe toate axele; w=X, h=Y(sus), d=Z"""
        t, l, r = {"built": (BUILT_T, BUILT_L, BUILT_R),
                   "new":   (NEW_T,   NEW_L,   NEW_R),
                   "met":   (MET_T,   MET_L,   MET_R)}[pal]
        X, Y, Z = x + w, y + h, z + d
        top  = [P(x, Y, z), P(X, Y, z), P(X, Y, Z), P(x, Y, Z)]
        rt   = [P(X, y, z), P(X, Y, z), P(X, Y, Z), P(X, y, Z)]   # fata +x
        fr   = [P(x, y, Z), P(X, y, Z), P(X, Y, Z), P(x, Y, Z)]   # fata +z
        sw = 3.2
        g = (f'<g opacity="{op}">'
             + self._poly(fr, r, sw) + self._poly(rt, l, sw) + self._poly(top, t, sw)
             + '</g>')
        self.items.append((key if key is not None else x + y + z + (w + h + d) / 2, g))
        if label:
            self.tag(x + w / 2, y + h, z + d / 2, label)
        return self

    def poly_z(self, pts, z, d, pal="built", key=None, op=1.0):
        """extrudeaza un poligon 2D (lista de (x,y), sens trigonometric) pe Z, de la z la z+d"""
        t, l, r = {"built": (BUILT_T, BUILT_L, BUILT_R),
                   "new":   (NEW_T,   NEW_L,   NEW_R),
                   "met":   (MET_T,   MET_L,   MET_R)}[pal]
        sw = 3.2
        parts = []
        n = len(pts)
        for i in range(n):                       # fete laterale vizibile
            (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
            dx, dy = x2 - x1, y2 - y1
            if (dy - dx) <= 0:                   # normala (dy,-dx) nu vine spre privitor
                continue
            quad = [P(x1, y1, z), P(x2, y2, z), P(x2, y2, z + d), P(x1, y1, z + d)]
            shade = l if abs(dx) > abs(dy) else r
            parts.append(self._poly(quad, shade, sw))
        cap = [P(px, py, z + d) for px, py in pts]   # capacul +Z
        parts.append(self._poly(cap, t, sw))
        cx = sum(p[0] for p in pts) / n; cy = sum(p[1] for p in pts) / n
        self.items.append((key if key is not None else cx + cy + z + d / 2, "".join(parts)))
        return self

    def ghost(self, x, y, z, w, h, d):
        X, Y, Z = x + w, y + h, z + d
        for quad in ([P(x, Y, z), P(X, Y, z), P(X, Y, Z), P(x, Y, Z)],
                     [P(X, y, z), P(X, Y, z), P(X, Y, Z), P(X, y, Z)],
                     [P(x, y, Z), P(X, y, Z), P(X, Y, Z), P(x, Y, Z)]):
            pts = " ".join(f"{a:.1f},{b:.1f}" for a, b in quad)
            self.items.append((-1e9, f'<polygon points="{pts}" fill="none" stroke="{GHOST}" '
                                    f'stroke-width="2.6" stroke-dasharray="14 10"/>'))
        return self

    def rod(self, x, y, z, w, h, d, pal="met"):
        return self.box(x, y, z, w, h, d, pal)

    def _poly(self, quad, fill, sw):
        pts = " ".join(f"{a:.1f},{b:.1f}" for a, b in quad)
        return f'<polygon points="{pts}" fill="{fill}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"/>'

    # ---------- adnotari (mereu deasupra) ----------
    def txt(self, x, y, z, s, dx=0, dy=0, cls="l", anchor="start"):
        px, py = P(x, y, z)
        self.texts.append((px + dx, py + dy, s, cls, anchor))
        return self

    def lead(self, x, y, z, dx, dy, s, cls="l", anchor="start"):
        """text cu linie de indicatie de la punctul 3D"""
        px, py = P(x, y, z)
        self.over.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{px+dx:.1f}" y2="{py+dy:.1f}" '
                         f'stroke="{INK}" stroke-width="2.2"/>')
        self.over.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="{INK}"/>')
        self.texts.append((px + dx, py + dy, s, cls, anchor, True))
        return self

    def tag(self, x, y, z, s, dx=0, dy=None):
        px, py = P(x, y, z)
        self.texts.append((px + dx, py, s, "bal", "middle", False, True))
        return self

    def dim(self, p1, p2, off=(0, 0), s="", flip=False):
        """cota intre doua puncte 3D, deplasata in ecran cu off"""
        a = P(*p1); b = P(*p2)
        ax, ay = a[0] + off[0], a[1] + off[1]
        bx, by = b[0] + off[0], b[1] + off[1]
        self.over.append(
            f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{ax:.1f}" y2="{ay:.1f}" stroke="{ACC}" stroke-width="1.6" stroke-dasharray="6 6"/>'
            f'<line x1="{b[0]:.1f}" y1="{b[1]:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{ACC}" stroke-width="1.6" stroke-dasharray="6 6"/>'
            f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{ACC}" stroke-width="2.6" '
            f'marker-start="url(#dt)" marker-end="url(#dt)"/>')
        mx, my = (ax + bx) / 2, (ay + by) / 2
        self.texts.append((mx, my, s, "d", "middle", False, False, flip))
        return self

    def arrow(self, p1, p2, col=ACC, w=6):
        a = P(*p1); b = P(*p2)
        self.over.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                         f'stroke="{col}" stroke-width="{w}" marker-end="url(#ar)"/>')
        return self

    def note(self, sx, sy, s, cls="l", anchor="start"):
        self.texts.append((sx, sy, s, cls, anchor))
        return self

    # ---------- iesire ----------
    def svg(self, pad=None):
        import re
        body = "".join(s for _, s in sorted(self.items, key=lambda t: t[0])) + "".join(self.over)
        xs, ys = [], []
        for m in re.finditer(r'points="([^"]+)"', body):
            for pair in m.group(1).split():
                a, b = pair.split(","); xs.append(float(a)); ys.append(float(b))
        for tag_ in ("x1", "x2", "cx"):
            for m in re.finditer(tag_ + r'="(-?\d+\.?\d*)"', body): xs.append(float(m.group(1)))
        for tag_ in ("y1", "y2", "cy"):
            for m in re.finditer(tag_ + r'="(-?\d+\.?\d*)"', body): ys.append(float(m.group(1)))
        if not xs: xs, ys = [0], [0]
        ext = max(max(xs) - min(xs), max(ys) - min(ys))
        fs = max(22.0, ext / 34.0)                 # text scalat cu desenul
        if pad is None: pad = ext * 0.05 + fs

        # emite textele si extinde bbox-ul cu latimea lor estimata
        tsvg = []
        for t in self.texts:
            tx, ty, s, cls, anchor = t[0], t[1], t[2], t[3], t[4]
            is_lead = len(t) > 5 and t[5]
            is_bal  = len(t) > 6 and t[6]
            flip    = len(t) > 7 and t[7]
            size = fs + 2 if is_bal else (fs if cls != "s" else fs - 4)
            if is_bal:
                r = size * 0.95
                tsvg.append(f'<circle cx="{tx:.1f}" cy="{ty - r*1.7:.1f}" r="{r:.1f}" fill="{ACC}"/>')
                tsvg.append(f'<text class="bal" style="font-size:{size:.1f}px" x="{tx:.1f}" '
                            f'y="{ty - r*1.7 + size*0.36:.1f}" text-anchor="middle">{s}</text>')
                xs += [tx - r, tx + r]; ys += [ty - r*2.7, ty]
                continue
            oy = ty + (size * 0.9 if flip else -size * 0.42) if cls == "d" else ty + size * 0.34
            ox = tx + (size * 0.35 if (is_lead and anchor == "start") else
                       (-size * 0.35 if (is_lead and anchor == "end") else 0))
            tsvg.append(f'<text class="{cls}" style="font-size:{size:.1f}px" x="{ox:.1f}" y="{oy:.1f}" '
                        f'text-anchor="{anchor}">{s}</text>')
            wid = 0.56 * size * len(s)
            if anchor == "start":   xs += [ox, ox + wid]
            elif anchor == "end":   xs += [ox - wid, ox]
            else:                   xs += [ox - wid / 2, ox + wid / 2]
            ys += [oy - size, oy + size * 0.35]
        body += "".join(tsvg)

        x0, x1 = min(xs) - pad, max(xs) + pad
        y0, y1 = min(ys) - pad, max(ys) + pad
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {y0:.0f} {x1-x0:.0f} {y1-y0:.0f}">'
                '<defs>'
                f'<marker id="ar" markerWidth="11" markerHeight="11" refX="9" refY="5.5" orient="auto">'
                f'<path d="M0,0 L11,5.5 L0,11 Z" fill="{ACC}"/></marker>'
                f'<marker id="dt" markerWidth="9" markerHeight="9" refX="4.5" refY="4.5" orient="auto">'
                f'<circle cx="4.5" cy="4.5" r="3.4" fill="{ACC}"/></marker>'
                '</defs>'
                f'<style>text{{font-family:Helvetica,Arial,sans-serif}}'
                f'.l{{fill:{INK}}}.s{{fill:#555}}'
                f'.d{{fill:{ACC};font-family:"Courier New",monospace;font-weight:bold}}'
                f'.bal{{fill:#fff;font-weight:bold}}</style>'
                + body + '</svg>')

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w").write(self.svg())
        print("scris", path)
