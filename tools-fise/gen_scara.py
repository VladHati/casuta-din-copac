#!/usr/bin/env python3
"""Schema izometrica a SCARII (faza F3). Toate cotele in mm.
Geometrie corectata 06.08: panta reala = atan(202,5/190) = 46,8 grade
(cei 49,5 gradele din documentele anterioare = diagonala sol-punte, NU panta scarii).
Sectiuni: varianta Leroy Colosseum — coarda 100x100, treapta 46x250, tachet 46x46x80.
Rulare: python3 gen_scara.py"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from iso2 import Scene, P

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "iso")

# ---------- geometrie ----------
RISE, GOING = 202.5, 190          # urcare / calcatura
NR, NT      = 11, 10              # urcari / trepte fizice
H_TOT       = RISE * NR           # 2227,5 ≈ 2228
RUN         = GOING * NT          # 1900
PITCH       = math.degrees(math.atan(RISE / GOING))   # 46,8°
SLOPE       = RISE / GOING
CO          = 100                 # coarda 100x100
TR_T, TR_D, TR_L = 46, 250, 600   # treapta: gros / adancime / lungime
TA          = 46                  # tachet 46x46
TA_L        = 80                  # lungime tachet
WID         = 600                 # lumina intre coarde
SLAB        = 60                  # grosime dala
PERP        = CO / math.cos(math.radians(PITCH))      # 146 — grosimea pe verticala

# linia nasurilor: y = 202,5 + SLOPE*x  (trece prin nasul treptei 1 si prin muchia puntii)
def ynose(x): return RISE + SLOPE * x

def stringer_profile(x0=-40, x1=RUN):
    """profil lateral al coardei: sub linia nasurilor, taiat orizontal jos si vertical sus"""
    return [(x0, ynose(x0) - PERP), (x1, ynose(x1) - PERP), (x1, ynose(x1)), (x0, ynose(x0))]


def treads(sc, pal="new", key0=0):
    """cele 10 trepte + tachetii lor"""
    for i in range(NT):
        top = RISE * (i + 1)
        xf  = GOING * i                      # nasul treptei
        sc.box(xf, top - TR_T, 0, TR_D, TR_T, TR_L, pal, key=key0 + i)
        for z in (0, WID - TA):              # tacheti sub capete
            sc.box(xf + 40, top - TR_T - TA, z if z == 0 else WID - TA,
                   TA_L, TA, TA, "met", key=key0 + i - 0.5)


# ================= 1. ANSAMBLU =================
def s1():
    sc = Scene()
    # sol + dala
    sc.box(-260, -SLAB, -180, 620, SLAB, WID + 360, "built", key=-9e5)
    # coarda din spate (z=0)
    sc.poly_z(stringer_profile(), -CO, CO, "new", key=-8e5)
    treads(sc)
    # coarda din fata (z=600)
    sc.poly_z(stringer_profile(), WID, CO, "new", key=9e5)
    # punte
    sc.box(RUN, H_TOT - 28, -180, 700, 28, WID + 360, "built", key=8e5)
    sc.box(RUN, H_TOT - 228, -180, 700, 200, WID + 360, "built", key=7.9e5)

    sc.dim((0, -SLAB, -180), (RUN, -SLAB, -180), (0, 760), "1900 baza = 10 × 190")
    sc.dim((RUN + 700, 0, -180), (RUN + 700, H_TOT, -180), (760, 0), "2228 = 11 × 202,5")
    # o singura treapta cotata, departe de restul
    sc.dim((GOING * 6, RISE * 7, 0), (GOING * 7, RISE * 7, 0), (0, -300), "190")
    sc.dim((GOING * 7, RISE * 7, 0), (GOING * 7, RISE * 8, 0), (-540, 0), "202,5")
    sc.dim((0, ynose(0) - PERP, 0), (0, ynose(0) - PERP, WID), (-880, 700), "600 lumina intre coarde")
    sc.lead(GOING * 7, RISE * 7.5, 0, -420, -760, f"panta reala {PITCH:.1f}°  =  202,5 / 190", anchor="end")
    sc.lead(GOING * 2 + TR_D / 2, RISE * 3, WID / 2, -520, 640,
            "treapta 46 × 250 × 600 — iese 60 peste cea de jos, deci talpa are 250", anchor="end")
    sc.lead(RUN + 350, H_TOT, WID / 2, 520, -420, "PUNTEA +2228")
    sc.lead(0, -SLAB / 2, WID + 200, 460, 420, "dale 400×400×60 sub fiecare coarda")
    sc.lead(RUN - 500, ynose(RUN - 500) - PERP / 2, WID + CO, 560, 180,
            "coarda 100×100 — bara de 3 m, taiata la ~2930")
    sc.save(os.path.join(OUT, "sc-1-ansamblu.svg"))


# ================= 2. DETALIU TACHET + TREAPTA =================
def s2():
    sc = Scene()
    x0 = 0
    top = RISE
    prof = [(-200, ynose(-200) - PERP), (420, ynose(420) - PERP),
            (420, ynose(420)), (-200, ynose(-200))]
    sc.poly_z(prof, 0, CO, "built", key=-1e5)
    # tachet montat
    sc.box(40, top - TR_T - TA, CO, TA_L, TA, TA, "new", key=0)
    # treapta explodata in sus
    sc.box(x0, top - TR_T + 700, CO, TR_D, TR_T, 300, "new", key=1e5)
    sc.ghost(x0, top - TR_T, CO, TR_D, TR_T, 300)
    sc.arrow((x0 + TR_D / 2, top - TR_T + 640, CO + 150), (x0 + TR_D / 2, top + 130, CO + 150))
    # capete de surub pe tachet
    for i, xx in enumerate((58, 80, 102)):
        sc.rod(xx, top - TR_T - TA + (10 if i % 2 == 0 else 26), CO + TA, 11, 11, 70, "met")
    sc.dim((40, top - TR_T - TA, CO + TA + 70), (40 + TA_L, top - TR_T - TA, CO + TA + 70), (-120, 300), "80", flip=True)
    sc.dim((x0, top - TR_T + 700, CO), (x0 + TR_D, top - TR_T + 700, CO), (0, -230), "250")
    sc.dim((x0 + TR_D, top - TR_T + 700, CO + 300), (x0 + TR_D, top + 700, CO + 300), (300, 0), "46")
    sc.lead(80, top - TR_T - TA + 18, CO + TA + 70, 300, 300, "3× Heco 6×80 in zigzag, pregaurit 4 mm")
    sc.lead(x0 + 60, top + 700, CO + 150, -320, -300, "treapta: 2× inox 5×60 la fiecare capat", anchor="end")
    sc.lead(360, ynose(360) - PERP / 2, CO, 340, 340, "coarda 100×100 — ramane INTREAGA, nu se cresteaza")
    sc.lead(x0 + TR_D, top - TR_T, CO + 150, 340, -140, "pozitia finala (fantoma)", cls="s")
    sc.save(os.path.join(OUT, "sc-2-tachet.svg"))


# ================= 3. PRINDEREA DE SUS =================
def s3():
    sc = Scene()
    # joista de capat + dusumea
    sc.box(RUN, H_TOT - 228, -200, 260, 200, WID + 400, "built", key=1e5)
    sc.box(RUN - 60, H_TOT - 28, -200, 320, 28, WID + 400, "built", key=1.1e5)
    # coarda, ultimii 900 mm
    prof = [(RUN - 900, ynose(RUN - 900) - PERP), (RUN, ynose(RUN) - PERP),
            (RUN, ynose(RUN)), (RUN - 900, ynose(RUN - 900))]
    sc.poly_z(prof, 0, CO, "new", key=-1e5)
    # buloane
    for hy in (H_TOT - 60, H_TOT - 150):
        sc.rod(RUN - 40, hy - 6, CO / 2 - 6, 340, 12, 12, "met")
    sc.dim((RUN, H_TOT, WID), (RUN, H_TOT - 60, WID), (420, 0), "60")
    sc.dim((RUN, H_TOT, WID + 120), (RUN, H_TOT - 150, WID + 120), (640, 0), "150")
    sc.lead(RUN + 120, H_TOT - 105, CO / 2, 420, -320, "2× M10×120 strapuns prin joista + saibe late")
    sc.lead(RUN - 700, ynose(RUN - 700) - PERP / 2, CO, -420, 300, "taietura VERTICALA, lipita de joista", anchor="end")
    sc.lead(RUN + 130, H_TOT - 200, WID + 300, 380, 300, "joista de capat 100×200")
    sc.box(RUN - 130, H_TOT - 300, CO, 130, 14, CO, "met", key=2e5)
    sc.box(RUN - 14, H_TOT - 420, CO, 14, 134, CO, "met", key=2e5)
    sc.lead(RUN - 90, H_TOT - 300, CO + CO, -300, 380, "coltar dedesubt — preia forfecarea", anchor="end")
    sc.save(os.path.join(OUT, "sc-3-sus.svg"))


# ================= 4. BAZA =================
def s4():
    sc = Scene()
    sc.box(-300, -SLAB, -100, 700, SLAB, 700, "built", key=-9e5)   # dala
    prof = [(-40, ynose(-40) - PERP), (700, ynose(700) - PERP),
            (700, ynose(700)), (-40, ynose(-40))]
    sc.poly_z(prof, 0, CO, "new", key=0)
    # opritor in fata coardei
    sc.box(-140, 0, 0, 60, 60, CO, "new", key=1e5)
    for xx in (-125, -95):
        sc.rod(xx, -20, CO / 2 - 5, 10, 80, 10, "met")
    sc.box(-40, ynose(-40) - PERP - 8, 0, 200, 8, CO, "met", key=0.5e5)
    sc.dim((-300, -SLAB, 600), (400, -SLAB, 600), (0, 320), "dala 400×400×60", flip=True)
    sc.lead(-110, 60, CO / 2, -400, -260, "opritor 45×45 — 2 dibluri + surub 6×60 in dala", anchor="end")
    sc.lead(60, ynose(60) - PERP - 8, CO / 2, 380, 300, "fasie EPDM/folie: lemnul NU sta direct pe beton")
    sc.lead(500, ynose(500) - PERP / 2, CO, 400, -300, "taietura de jos ORIZONTALA (sta plan pe dala)")
    sc.save(os.path.join(OUT, "sc-4-baza.svg"))


# ================= 5. MANA CURENTA =================
def s5():
    sc = Scene()
    sc.poly_z(stringer_profile(), WID, CO, "built", key=-1e5)
    treads(sc, "built", key0=-5e4)
    sc.poly_z(stringer_profile(), -CO, CO, "built", key=-9e5)
    # montanti pe fata exterioara (z = WID+CO)
    for xx in (200, 950, 1700):
        yb = ynose(xx) - PERP
        sc.box(xx, yb, WID + CO, TA, 900 + PERP, TA, "new", key=5e5)
    # mana curenta paralela cu panta
    hp = [(150, ynose(150) + 900 - 46), (1800, ynose(1800) + 900 - 46),
          (1800, ynose(1800) + 900), (150, ynose(150) + 900)]
    sc.poly_z(hp, WID + CO, TA, "new", key=6e5)
    sc.dim((950, ynose(950), WID + CO + TA), (950, ynose(950) + 900, WID + CO + TA), (420, 0), "900 masurat VERTICAL de la nas")
    sc.dim((200, ynose(200) + 900, WID + CO), (950, ynose(950) + 900, WID + CO), (0, -320), "~750 intre montanti")
    sc.lead(950, ynose(950) + 900, WID + CO + TA, 420, -420, "mana curenta 46×46 — pe AMBELE parti")
    sc.lead(200, ynose(200) + 400, WID + CO + TA, -420, 260, "3× Heco 6×100 pe fiecare montant, zigzag", anchor="end")
    sc.lead(1800, ynose(1800) + 900, WID + CO, 400, 300, "se prelungeste pana la stalpisorul portii")
    sc.save(os.path.join(OUT, "sc-5-mana.svg"))


if __name__ == "__main__":
    print(f"panta {PITCH:.2f}° · urcare {RISE} · calcatura {GOING} · "
          f"coarda ax {math.hypot(RUN, RISE*NT):.0f} mm")
    for f in (s1, s2, s3, s4, s5):
        f()
