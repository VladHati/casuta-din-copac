#!/usr/bin/env python3
"""Diagrame izometrice pentru CASA (faza F4). Cote nominale — reale = formule de M1/M2/M3.
Rulare: python3 gen_casa.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from iso2 import Scene

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "iso")

L    = 2000    # lumina intre stalpii de 4 m (M3)
A    = 1100    # adancimea casei (M2)
H    = 1772    # inaltime perete spate (M1)
HF   = H - 300 # perete fata
PL   = 42      # talpa/cununa: 42 grosime, 90 latime
PW   = 90
ST   = 45      # montant 45x45
OSB  = 12
JX   = [0, 280, 720, 1120, 1550, 2100]


# ============ 1. PERETE PANOU, JOS PE IARBA ============
def s1():
    sc = Scene()
    # talpa si cununa culcate (90 lat pe orizontala, 42 grosime)
    sc.box(0, 0, 0, L, PL, PW, "new")
    sc.box(0, HF - PL, 0, L, PL, PW, "new")
    # montanti
    xs = [0, 500, 1000, 1500, L - ST]
    for x in xs:
        sc.box(x, PL, 0, ST, HF - 2 * PL, ST, "new")
    # montant dublu la capete
    sc.box(ST, PL, 0, ST, HF - 2 * PL, ST, "new")
    sc.box(L - 2 * ST, PL, 0, ST, HF - 2 * PL, ST, "new")
    # OSB partial, ridicat (explodat)
    sc.box(0, PL + 700, -520, L, HF - 2 * PL, OSB, "met")
    sc.arrow((L / 2, PL + 640, -500), (L / 2, PL + 60, ST + 40))
    sc.dim((0, 0, PW), (L, 0, PW), (0, 420), "L = lumina intre stalpi (M3), nominal 2000", flip=True)
    sc.dim((0, 0, 0), (0, HF, 0), (-420, 0), "inaltime perete")
    sc.dim((0, PL, 0), (500, PL, 0), (0, -300), "~500 interax")
    sc.lead(ST, HF - PL, ST, -380, -420, "montant DUBLU la fiecare capat de perete", anchor="end")
    sc.lead(L / 2, PL + 700, -520 + OSB, 420, -360, "OSB 12 — suruburi 4×60 la 150 pe margini, 300 in camp")
    sc.lead(L / 2, 0, PW, 420, 420, "talpa si cununa 42×90, asezate pe LAT")
    sc.lead(1000, HF / 2, ST, -420, 300, "diagonalele panoului egale ±3 mm INAINTE de OSB", anchor="end")
    sc.save(os.path.join(OUT, "ca-1-panou.svg"))


# ============ 2. RIDICAREA — ORDINEA SI LANTUL ============
def s2():
    sc = Scene()
    # dusumea + joiste (fragment)
    for x in JX:
        sc.box(x - 50, -200, -300, 100, 200, A + 500, "built", key=-9e5)
    sc.box(-100, 0, -300, 2300, 28, A + 500, "built", key=-8e5)
    # stalpi 4 m
    for x in (0, L):
        sc.box(x - 50, 28, A - 50, 100, H + 260, 100, "built", key=-7e5)
    # perete spate (1)
    sc.box(0, 28, A - PW, L, H, PW, "new", key=1e5)
    # laterale (2)
    sc.box(0, 28, 0, PW, HF, A - PW, "new", key=2e5)
    sc.box(L - PW, 28, 0, PW, HF, A - PW, "new", key=2e5)
    # fata (3)
    sc.box(0, 28, 0, L, HF, PW, "new", key=3e5)
    # stalpi fata 70x70
    for x in (0, L):
        sc.box(x - 35, 28, -70, 70, HF, 70, "new", key=3.5e5)
    sc.tag(L / 2, 28 + H, A, "1")
    sc.tag(0, 28 + HF, A / 2, "2")
    sc.tag(L / 2, 28 + HF, 0, "3")
    sc.lead(L / 2, 28 + H - 200, A, 460, -420, "1 · SPATE — 6 tirfoane M10×120 in stalpii de 4 m (3 pe fiecare)")
    sc.lead(0, 28 + HF - 300, A / 2, -460, -200, "2 · LATERALE — 4× 6×120 + 2 coltare in fiecare colt", anchor="end")
    sc.lead(L / 2, 28 + 200, 0, 460, 420, "3 · FATA — la fel in colturi + 3× 6×120 in fiecare stalp 70×70")
    sc.lead(0, 28, -70, -460, 300, "stalpii 70×70 pe tijele M12 deja montate", anchor="end")
    sc.lead(1120, 0, -300, 300, 460, "TALPILE: 6×140 (NU 5×80) — 42 talpa + 28 dusumea + 70 in joista")
    sc.dim((0, 28, A), (L, 28, A), (0, -560), "L")
    sc.dim((0, 28, 0), (0, 28, A), (-560, 300), "A = adancime (M2)")
    sc.save(os.path.join(OUT, "ca-2-ridicare.svg"))


# ============ 3. ACOPERISUL SI LANTUL ANTI-VANT ============
def s3():
    sc = Scene()
    # cununi
    sc.box(0, 0, A - PW, L, PL, PW, "built", key=-1e5)
    sc.box(0, -300, 0, L, PL, PW, "built", key=-1e5)
    # capriori
    for x in (0, 500, 1000, 1500, 2000 - 90):
        sc.poly_z([(-200, -300 - 55), (A + 100, 0 - 55), (A + 100, 0 + 35), (-200, -300 + 35)],
                  0, 90, "new", key=x)
    # sipci
    for t in (0.05, 0.32, 0.6, 0.88):
        zz = -200 + t * (A + 300)
        yy = -300 - 55 + t * 300 + 45
        sc.box(-100, yy, zz, L + 200, 45, 45, "new", key=1e6 + t)
    sc.lead(1000, -180, 500, 460, -420, "5 capriori 42×90 la 500 interax")
    sc.lead(500, -60, -100, -460, 320, "sipci 45×45 la ≤450 — nu 500 (zapada)", anchor="end")
    sc.lead(1500, -40, A - PW, 460, 320, "ANCORA anti-vant la AMBELE capete ale FIECARUI caprior")
    sc.lead(0, -300, -200, -460, -300, "streasina fata 200 — teseste muchia, e la inaltimea capului", anchor="end")
    sc.dim((0, 0, A - PW), (0, -300, A - PW), (-380, 0), "300 = panta pe 1100 → 15,3°")
    sc.dim((0, 0, A), (500, 0, A), (0, -300), "500")
    sc.save(os.path.join(OUT, "ca-3-acoperis.svg"))


if __name__ == "__main__":
    for f in (s1, s2, s3):
        f()
