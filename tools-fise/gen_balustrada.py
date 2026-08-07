#!/usr/bin/env python3
"""Diagrame izometrice pas-cu-pas pentru BALUSTRADA (faza F2).
Toate cotele in mm, as-built 06.08. Ruleaza: python3 gen_balustrada.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from iso2 import Scene, P

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "iso")

# ---- geometrie as-built (mm) ----
W      = 2100          # latime punte (axe joiste capat)
DEPTH  = 2440          # adancime punte (nas -> spate)
TER    = 1340          # adancimea terasei libere (pana la linia casei)
JW, JH = 100, 200      # joista
DECK   = 28            # dusumea
POST   = 58            # stalpisor
H_F, H_L = 1100, 1000  # inaltime balustrada fata / laturi
LAP    = 200           # suprapunere pe joista
RAIL_W, RAIL_H = 70, 45
JX = [0, 280, 720, 1120, 1550, 2100]      # axe joiste
PF = [0, 720, 1550, 2100]                 # stalpisori fata
PL = [670, 1340]                          # stalpisori laterali (de la nas)

y_j = 0            # talpa joistei = 0
y_top = JH         # top joista = 200
y_dk = JH + DECK   # fata dusumelei = 228


def deck(sc, joists=True):
    if joists:
        for x in JX:
            sc.box(x - JW / 2, y_j, 0, JW, JH, DEPTH)
    sc.box(-JW / 2, y_top, 0, W + JW, DECK, DEPTH)


# ================= 1. ANSAMBLU =================
def s1():
    sc = Scene()
    deck(sc)
    # stalpisori fata (h 1100)
    for x in PF:
        sc.box(x - POST / 2, y_top - LAP, -POST, POST, LAP + DECK + H_F, POST, "new")
    # stalpisori laterali (h 1000)
    for z in PL:
        for x in (0, W):
            sx = x - POST / 2 + (-POST if x == 0 else JW / 2)
            sc.box(x - POST / 2, y_top - LAP, z, POST, LAP + DECK + H_L, POST, "new")
    # mana curenta fata + lisa
    for yy, hh in ((y_dk + H_F - RAIL_H, RAIL_H), (y_dk + 40, RAIL_H)):
        sc.box(-JW / 2, yy, -POST, W + JW, hh, RAIL_W, "new")
    # mana curenta laterale
    for x in (0, W):
        for yy in (y_dk + H_L - RAIL_H, y_dk + 40):
            sc.box(x - RAIL_W / 2, yy, 0, RAIL_W, RAIL_H, TER, "new")
    # cote — plasate in afara geometriei
    sc.dim((0, y_j, -POST), (W, y_j, -POST), (0, 620), "2100 latime punte")
    sc.dim((W, y_j, 0), (W, y_j, TER), (760, 260), "1340 terasa")
    sc.dim((0, y_dk, -POST), (0, y_dk + H_F, -POST), (-420, 0), "1100 FATA")
    sc.dim((W, y_dk, TER), (W, y_dk + H_L, TER), (620, 0), "1000 LATURI")
    sc.dim((0, 0, DEPTH), (0, y_dk, DEPTH), (-420, 0), "228 fata dusumelei")
    # travei fata
    sc.dim((0, y_dk + H_F, -POST), (720, y_dk + H_F, -POST), (0, -260), "720")
    sc.dim((720, y_dk + H_F, -POST), (1550, y_dk + H_F, -POST), (0, -260), "830")
    sc.dim((1550, y_dk + H_F, -POST), (2100, y_dk + H_F, -POST), (0, -260), "550")
    for i, x in enumerate(PF):
        sc.tag(x, y_dk + H_F + 120, -POST / 2, "ABCD"[i])
    for i, z in enumerate(PL):
        sc.tag(0, y_dk + H_L + 120, z, "EF"[i])
        sc.tag(W, y_dk + H_L + 120, z, "GH"[i])
    sc.lead(1550, y_dk + H_F, -POST / 2, 260, -620,
            "8 stalpisori · fata pe AXELE joistelor 0 · 720 · 1550 · 2100")
    sc.lead(W / 2, y_dk, DEPTH - 300, 380, -180, "spate: fara balustrada — aici vine casa", cls="s")
    sc.lead(W, y_dk + H_L, 670, 560, 340, "poarta + scara (latura dreapta)", cls="s")
    sc.save(os.path.join(OUT, "bal-1-ansamblu.svg"))


# ================= 2. STALPISOR — piesa =================
def s2():
    sc = Scene()
    L = 1330
    sc.box(0, 0, 0, POST, L, POST, "new")
    # gauri
    for hy in (50, 150):
        sc.rod(-20, hy - 6, POST / 2 - 6, POST + 40, 12, 12, "met")
        sc.dim((0, 0, 0), (0, hy, 0), (-190, 0), str(hy))
    sc.dim((0, 0, POST), (0, L, POST), (-330, 0), "1330 (fata) · 1230 (latura)")
    sc.dim((0, L, 0), (POST, L, 0), (0, -150), "58")
    sc.lead(POST, 150, POST / 2, 200, -60, "2 gauri Ø11 strapunse")
    sc.lead(POST / 2, L, POST / 2, 160, -120, "capatul cu REZERVA — se reteaza la final")
    sc.lead(POST / 2, 0, POST / 2, -160, 150, "capatul de JOS (intra pe joista)", anchor="end")
    sc.note(0, 0, "")
    sc.save(os.path.join(OUT, "bal-2-stalpisor.svg"))


# ================= 3. MONTAJ pe joista =================
def s3():
    sc = Scene()
    Lz = 800
    sc.box(-JW / 2, y_j, 0, JW, JH, Lz)                 # joista de capat
    sc.box(-JW / 2, y_top, 0, 360, DECK, Lz)            # dusumea (fragment)
    # fantoma pozitie finala
    sc.ghost(-JW / 2 - POST, y_top - LAP, 300, POST, LAP + DECK + 700, POST)
    # stalpisor explodat, ridicat si dat lateral
    ox, oy = -420, 780
    sc.box(-JW / 2 - POST + ox, y_top - LAP + oy, 300, POST, LAP + DECK + 700, POST, "new")
    sc.arrow((-JW / 2 - POST + ox + POST / 2, y_top - LAP + oy - 90, 330),
             (-JW / 2 - POST + POST / 2, y_top - LAP + 130, 330))
    # buloane, explodate spre stanga-fata
    for hy in (y_top - LAP + 50, y_top - LAP + 150):
        sc.rod(-JW / 2 - POST - 520, hy - 6, 300 + POST / 2 - 6, 240, 12, 12, "met")
        sc.arrow((-JW / 2 - POST - 250, hy, 300 + POST / 2), (-JW / 2 - POST - 40, hy, 300 + POST / 2))
    sc.lead(-JW / 2 - POST - 420, y_top - LAP + 100, 330, -300, -300,
            "2× M10×120 + 2 saibe late + piulita", anchor="end")
    sc.dim((-JW / 2 - POST, y_top - LAP, 300 + POST), (-JW / 2 - POST, y_top, 300 + POST), (-360, 0), "200 lap pe joista")
    sc.lead(-JW / 2, y_j + JH / 2, Lz, 300, 300, "joista de capat 100×200", cls="s")
    sc.lead(150, y_top + DECK, Lz - 120, 480, 120, "dusumea 28", cls="s")
    sc.lead(-JW / 2 - POST / 2, y_top - LAP + 900, 300, -260, -180,
            "gaureste Ø11 prin joista DUPA ce ai insemnat prin stalpisor", anchor="end", cls="s")
    sc.save(os.path.join(OUT, "bal-3-montaj.svg"))


# ================= 4. MANA CURENTA + LISA =================
def s4():
    sc = Scene()
    span = 830
    for x in (0, span):
        sc.box(x - POST / 2, 0, 0, POST, H_F, POST)
    sc.box(-POST, H_F - RAIL_H, -12, span + 2 * POST, RAIL_H, RAIL_W, "new")
    sc.box(-POST / 2, 40, -12, span + POST, RAIL_H, RAIL_W, "new")
    sc.arrow((span / 2, H_F + 320, 30), (span / 2, H_F + 20, 30))
    sc.dim((0, 0, 0), (0, H_F, 0), (-210, 0), "1100 / 1000")
    sc.dim((0, 0, 0), (0, 40, 0), (210, 60), "40")
    sc.dim((0, H_F, POST), (span, H_F, POST), (0, -190), "travee max 830")
    sc.lead(span / 2, H_F, 20, 210, -230, "mana curenta 45×70 — 2× Heco 6×100 pe fiecare stalpisor")
    sc.lead(span / 2, 40 + RAIL_H, 20, 260, 150, "lisa jos — 2× Heco 6×80 la fiecare capat")
    sc.lead(0, H_F, 0, -250, -140, "imbinarile cad DEASUPRA unui stalpisor, taiate 45°", anchor="end")
    sc.note(0, 0, "")
    sc.save(os.path.join(OUT, "bal-4-rails.svg"))


# ================= 5. LAMELE =================
def s5():
    sc = Scene()
    span, LAM, PITCH, GAP = 830, 18, 106, 88
    for x in (0, span):
        sc.box(x - POST / 2, 0, 0, POST, H_F, POST)
    sc.box(-POST, H_F - RAIL_H, -12, span + 2 * POST, RAIL_H, RAIL_W)
    sc.box(-POST / 2, 40, -12, span + POST, RAIL_H, RAIL_W)
    n = int((span - POST) / PITCH)
    for i in range(n):
        x = POST / 2 + 30 + i * PITCH
        sc.box(x, 40 + RAIL_H, 0, LAM, H_F - RAIL_H - 40 - RAIL_H, 28, "new")
    x0 = POST / 2 + 30
    sc.dim((x0, H_F - RAIL_H, 28), (x0 + PITCH, H_F - RAIL_H, 28), (0, -150), "pas 106")
    sc.dim((x0 + LAM, 40 + RAIL_H + 300, 28), (x0 + PITCH, 40 + RAIL_H + 300, 28), (0, 210), "gol 88", flip=True)
    sc.lead(x0 + PITCH * 3, H_F - RAIL_H, 14, 240, -170, "18×28 · 1 inox 4×50 sus + 1 jos, oblic")
    sc.lead(x0 + PITCH, 40 + RAIL_H + 100, 14, -260, 190, "PREGAURESTE 3 mm — sipca de 18 crapa", anchor="end")
    sc.note(0, 0, "")
    sc.save(os.path.join(OUT, "bal-5-lamele.svg"))


# ================= 6. POARTA =================
def s6():
    sc = Scene()
    GW, GH = 560, 900
    sc.box(-POST, 0, 0, POST, H_L, POST)            # stalpisor
    sc.box(GW, 0, 0, POST, H_L, POST)               # stalpisor opus
    # rama poarta
    sc.box(0, 100, 10, GW, RAIL_H, 45, "new")
    sc.box(0, 100 + GH - RAIL_H, 10, GW, RAIL_H, 45, "new")
    sc.box(0, 100, 10, RAIL_H, GH, 45, "new")
    sc.box(GW - RAIL_H, 100, 10, RAIL_H, GH, 45, "new")
    for i in range(4):
        sc.box(90 + i * 106, 145, 16, 18, GH - 90, 28, "new")
    sc.dim((0, 100, 45), (GW, 100, 45), (0, 240), "gol 560", flip=True)
    sc.dim((0, 100, 45), (0, 100 + GH, 45), (-200, 0), "900")
    sc.arrow((GW / 2, 100 + GH / 2, 400), (GW / 2, 100 + GH / 2, 90))
    sc.lead(-POST / 2, 100 + GH - RAIL_H, POST / 2, -230, -150, "2 balamale cu ARC — se inchide singura", anchor="end")
    sc.lead(GW, 100 + GH, 45, 230, -110, "zavor SUS, la 1000 de dusumea")
    sc.lead(GW / 2, 100 + GH / 2, 350, 200, 200, "se deschide spre PUNTE, niciodata spre gol")
    sc.note(0, 0, "")
    sc.save(os.path.join(OUT, "bal-6-poarta.svg"))


if __name__ == "__main__":
    for f in (s1, s2, s3, s4, s5, s6):
        f()
