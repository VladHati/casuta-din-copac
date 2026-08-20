#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E0 — golul de la colturile din spate, pas cu pas.
Un singur model numeric; toate cotele din desene sunt calculate din el.
A, B, C sunt de masurat pe santier — schimbi trei numere aici si toate desenele se refac."""
import json, math
from kit import *

# ─────────── MODEL ───────────
m = {}
m['BP']   = 100      # stalp spate (masurat cu ruleta)
m['A']    = 100      # gol in FATA stalpului      ── DE MASURAT
m['B']    = 100      # gol LANGA stalp            ── DE MASURAT
m['C']    = 520      # adancimea golului          ── DE MASURAT
m['MASURAT'] = False

m['DT']   = 28
m['JO']   = 100
m['GLW'], m['GLH'] = 90, 200
m['VA'], m['VB'], m['VT'] = 90, 65, 3
m['DECK_W'], m['DECK_D'] = 2100, 2550
m['CONSOLA'] = 700

Z_DECK_B = -m['DT']
Z_JO_B   = Z_DECK_B - m['JO']
m['BLOC_H'] = m['JO'] - 10
Z_BLOC_B = Z_DECK_B - m['BLOC_H']
Z_VIN    = Z_BLOC_B

A,B,C,BP,DT,JO = m['A'],m['B'],m['C'],m['BP'],m['DT'],m['JO']
VA,VB,VT = m['VA'],m['VB'],m['VT']
NX, NY = BP+B, BP+A

F={}
NOM = '' if m['MASURAT'] else '   ·   forma e corecta, numerele sunt nominale'

def bands(g,x0,x1,y0,y1,brd=145,rost=5,fill=W1,sw=1.0):
    y=y1
    while y > y0+3:
        h=min(brd,y-y0)
        if h>5: g.bar(x0,y-h,x1-x0,h,fill=fill,sw=sw)
        y-=h+rost

def fin(g,t,sub=None,pad=34):
    g.bb[1]-=26 if sub else 14      # rezerva pentru titlu
    g.title(t,sub)
    return g.svg(pad=pad, extra_top=34 if sub else 18)

# ═══ 1 · UNDE ═══
g=D(0.108, fs=13)
W,Dp=m['DECK_W'],m['DECK_D']
bands(g,0,W,0,Dp)
for x in (0,W-NX):
    g.bar(x,Dp-NY,NX,NY,fill='#faf8f3',stroke='none')
    g.void(x,Dp-NY,NX,NY,col=WARN)
for x in (0,W-BP):
    g.hatch(x,Dp-BP,BP,BP,fill=W3,ang=45,gap=6)
    g.hatch(x+5,m['CONSOLA'],BP-20,BP-20,fill=W4,ang=45,gap=6)
g.bar(0,0,W,Dp,fill='none',stroke=INK,sw=2.4)
g.dimh(0,W,0,f'{W}',off=76,ext=1)
g.dimv(0,Dp,W,f'{Dp}',off=42,ext=1)
g.tx(W/2,Dp+95,'SPATE  —  spre vecin',size=12,fill=MUT)
g.tx(W/2,-165,'FATA  —  spre curte',size=12,fill=MUT)
# adnotari in gutiera din stanga
g.note(NX*0.5,Dp-NY*0.45,'golul, aici',dx=-150,dy=-40,fill=WARN,anchor='end',weight='700')
g.note(W-NX*0.5,Dp-NY*0.45,'si aici, in oglinda',dx=150,dy=-40,fill=WARN,anchor='start',weight='700')
g.note(BP/2,m['CONSOLA']+BP/2,'stalpii din fata',dx=-150,dy=30,fill=MUT,anchor='end')
g.note(BP*0.4,Dp*0.42,'dusumea existenta, 17 scanduri',dx=-150,dy=0,fill=MUT,anchor='end')
F['e0_unde']=fin(g,'UNDE','puntea vazuta de sus  ·  golul e la cele doua colturi din spate')

# ═══ 2 · ACUM, PLAN ═══
S=0.60
g=D(S,fs=13)
DX,DY=700,620
bands(g,0,DX,0,DY)
g.bar(0,DY-NY,NX,NY,fill='#faf8f3',stroke='none')
g.void(0,DY-NY,BP,A); g.void(BP,DY-NY,B,BP+A)
g.hatch(0,DY-BP,BP,BP,fill=W3,ang=45,gap=6)
g.tx(BP/2,DY-BP*0.45,'STALP',size=11,weight='700')
g.ln(0,0,0,DY,stroke=INK,sw=2.6); g.ln(0,DY,DX,DY,stroke=INK,sw=2.6)
g.dimv(DY-NY,DY-BP,-6,f'A = {A}',off=-30,fill=WARN,size=14,ext=1)
g.dimh(BP,NX,DY-NY,f'B = {B}',off=30,fill=WARN,size=14,ext=1)
g.dimh(0,BP,DY,'100',off=-30,fill=DIM,ext=1)
g.tx(DX*0.66,DY*0.30,'dusumea existenta',size=12,fill=MUT)
g.tx(DX*0.58,DY+64,'spre vecin',size=12,fill=MUT)
g.note(BP*0.5,DY-NY+A*0.4,'golul: o fasie in fata stalpului',dx=-190,dy=90,fill=WARN,anchor='end',weight='700')
g.note(BP+B*0.5,DY-BP*0.5,'si una langa el',dx=210,dy=-40,fill=WARN,anchor='start',weight='700')
F['e0_acum']=fin(g,'ACUM · vedere de sus','A si B sunt cele doua numere de masurat'+NOM)

# ═══ 3 · ACUM, SECTIUNE ═══
S=0.50
g=D(S,fs=13)
RX=700
g.hatch(-BP,-700,BP,700,fill=W3,ang=45,gap=6)
g.tx(-BP/2,-380,'stalp 100',size=11,fill=MUT,rot=-90)
x=A
n=0
while x<RX:
    w=min(145,RX-x)
    if w>10: g.bar(x,Z_DECK_B,w,DT,fill=W1,sw=1.2)
    x+=w+5; n+=1
g.void(0,-700,A,700)
g.ln(-BP-280,0,RX+40,0,stroke=DIM,sw=0.9,dash='7,5')
g.tx(-BP-290,-5,'0 = fata podelei',size=11,fill=DIM,anchor='end')
g.dimh(0,A,Z_DECK_B,f'A = {A}',off=-28,fill=WARN,size=14,ext=1)
g.dimv(Z_DECK_B,0,RX+20,'28',off=28,fill=DIM,ext=1)
g.tx(RX*0.55,Z_DECK_B-120,'dusumea 28×145, cu rost de 5',size=12,fill=MUT)
g.tx(A/2+330,-420,'AICI NU STIM CE E.',size=14,fill=WARN,weight='700',anchor='start')
g.tx(A/2+330,-480,'Poate grinda, poate joista de capat,',size=12,fill=WARN,anchor='start')
g.tx(A/2+330,-540,'poate nimic. Asta masori cu C.',size=12,fill=WARN,anchor='start')
g.tx(A/2+330,-640,'Fara raspunsul asta nu se poate',size=12,fill=MUT,anchor='start')
g.tx(A/2+330,-700,'alege in ce se insurubeaza vinclul.',size=12,fill=MUT,anchor='start')
g.arrow(A/2+310,-500,A/2+40,-420,stroke=WARN,sw=1.6)
F['e0_acum_sect']=fin(g,'ACUM · sectiune prin gol','taiat perpendicular pe marginea puntii')

# ═══ 4 · PRINCIPIUL ═══
S=0.74
G=180                                        # latimea santului, schematic
VTd=11                                       # grosime vinclu exagerata
ZV=Z_BLOC_B-VTd
g=D(S,fs=13)
def rim(ox):
    """marginea puntii: dusumea + lemn portant la dreapta, aer la stanga"""
    g.hatch(ox+G,Z_JO_B,180,JO,fill=W2,ang=45,gap=7)
    g.bar(ox+G,Z_DECK_B,180,DT,fill=W1,sw=1.4)
    g.tx(ox+G+90,Z_JO_B+JO/2,'lemn portant',size=10,fill=MUT)
    g.void(ox-30,Z_JO_B-120,G+30,abs(Z_JO_B-120-Z_DECK_B))
    g.tx(ox+G*0.32,Z_JO_B-60,'santul',size=10,fill=WARN)
    g.ln(ox-95,Z_JO_B-150,ox-95,Z_DECK_B+90,stroke=MUT,sw=1,dash='5,5')
    g.tx(ox-95,Z_JO_B-205,'marginea puntii',size=10,fill=MUT)
    g.tx(ox-95,Z_JO_B-250,'(dincolo: aer)',size=10,fill=MUT)
# stanga: gresit
ox=0
rim(ox)
g.bar(ox-30,Z_DECK_B,G+30,DT,fill=W1,sw=1.6)
g.arrow(ox+G*0.35,140,ox+G*0.35,DT+10,stroke=ACC2,sw=2.6)
g.tx(ox+G*0.35,178,'greutate',size=12,fill=ACC2)
g.poly([(ox-30,Z_DECK_B-120),(ox+G*0.5,Z_DECK_B-70),(ox+G,Z_DECK_B)],
       fill='none',stroke=ACC2,sw=1.8,dash='6,4',close=False)
g.tx(ox+G*0.16,Z_DECK_B-235,'se lasa in gol',size=12,fill=ACC2)
g.tx(ox+G/2,Z_JO_B-260,'GRESIT',size=15,fill=ACC2,weight='700')
g.tx(ox+G/2,Z_JO_B-322,'scandura peste sant: un capat',size=11,fill=MUT)
g.tx(ox+G/2,Z_JO_B-372,'pe muchie, celalalt pe nimic',size=11,fill=MUT)
# dreapta: corect
ox=760
rim(ox)
g.bracket(ox+G,ZV,VA,VB,t=VTd,fill=METAL,stroke=METAL2,flip=True,sw=1.8)
g.hatch(ox,Z_BLOC_B,G,m['BLOC_H'],fill=W2,ang=45,gap=7)
g.bar(ox-30,Z_DECK_B,G+30,DT,fill=W1,sw=1.6)
g.tx(ox+G/2,Z_BLOC_B+m['BLOC_H']*0.42,'blocaj',size=10,fill=MUT)
g.arrow(ox+G*0.35,140,ox+G*0.35,DT+10,stroke=ACC,sw=2.6)
g.tx(ox+G*0.35,178,'greutate',size=12,fill=ACC)
g.arrow(ox+G-VB/2,Z_BLOC_B+30,ox+G-VB/2,ZV+VTd+3,stroke=ACC,sw=1.7)
g.arrow(ox+G-VB/2+14,ZV+VTd*0.5,ox+G+66,ZV+VTd*0.5,stroke=ACC,sw=1.7)
g.tx(ox+G/2,Z_JO_B-260,'CORECT',size=15,fill=ACC,weight='700')
g.tx(ox+G/2,Z_JO_B-322,'blocajul sta pe polita de metal,',size=11,fill=MUT)
g.tx(ox+G/2,Z_JO_B-372,'prinsa in lemnul portant al puntii',size=11,fill=MUT)
g.notes(ox+G-VB*0.5,ZV,['vinclul','bratul scurt orizontal,','ca o polita de raft'],dx=190,dy=110,fill=METAL2)
F['e0_principiu']=fin(g,'PRINCIPIUL','de ce vinclu si nu doar o scandura  ·  schema, nu la scara')

# ═══ 5 · PIESELE ═══
S=0.80
g=D(S,fs=12)
def piesa(x, titlu, sub, fn):
    fn(x)
    g.tx(x, 205, titlu, size=13, weight='700')
    g.tx(x, 172, sub, size=11, fill=MUT)
def p_vinclu(x):
    g.bracket(x-VB/2,0,VA,VB,t=VT,fill=METAL,stroke=METAL2,sw=1.6)
    g.dimv(0,VA,x-VB/2-4,f'{VA}',off=-24,fill=DIM,ext=1)
    g.dimh(x-VB/2,x+VB/2,0,f'{VB}',off=26,fill=DIM,ext=1)
def p_blocaj(x):
    w=max(A,B)
    g.hatch(x-w/2,0,w,m['BLOC_H'],fill=W2,ang=45,gap=7)
    g.dimh(x-w/2,x+w/2,0,f'{w}',off=26,fill=DIM,ext=1)
    g.dimv(0,m['BLOC_H'],x+w/2+4,f"{m['BLOC_H']}",off=26,fill=DIM,ext=1)
def p_scand(x):
    g.bar(x-110,0,220,DT,fill=W1)
    g.dimh(x-110,x+110,0,'pe masura',off=26,fill=DIM,ext=1)
    g.dimv(0,DT,x+114,f'{DT}',off=26,fill=DIM,ext=1)
piesa(0,   'VINCLU 90×65',  '×2 pe latura · deja pe lista Leroy', p_vinclu)
piesa(360, 'BLOCAJ',        'taiat pe loc, din offcut',           p_blocaj)
piesa(760, 'SCANDURA',      'larice 28, ca restul podelei',       p_scand)
for i,(cod,n,rol,L) in enumerate([('5×40','×8','vincluri in lemn',40),
                                  ('8×140','×5','blocaj, dulgherie',140),
                                  ('5×60','×4','scandura de calcat',60)]):
    y=-150-i*90
    g.surub(-60,y,0,L,stroke=METAL2,sw=3.2)
    g.tx(180,y-4,f'{cod}   {n}   —   {rol}',size=12,anchor='start')
g.tx(380,-500,'Cantitatile sunt pentru O LATURA. Golul are doua laturi,',size=12,fill=WARN,weight='700')
g.tx(380,-550,'si sunt doua colturi  →  totul ×4.',size=12,fill=WARN,weight='700')
F['e0_piese']=fin(g,'PIESELE','la scara, una langa alta')


# ═══════════ PASI ═══════════
# plan al santului in L (origine = coltul exterior al stalpului)
DY  = 430          # cat din punte aratam pe verticala
DXP = 470          # ... si pe orizontala
SP  = 1.05         # scara desenelor de pas
VW  = 34           # latimea vinclului vazut de sus

def santul(g, blocaj=False, scandura=False):
    bands(g,0,DXP,0,DY)
    g.bar(0,DY-NY,NX,NY,fill='#faf8f3',stroke='none')
    if blocaj:
        g.hatch(0,DY-NY,BP,A,fill=W2,ang=45,gap=7)
        g.hatch(BP,DY-NY,B,BP+A,fill=W2,ang=-45,gap=7)
    elif scandura:
        g.bar(0,DY-NY,BP,A,fill=W1,sw=1.7)
        g.bar(BP,DY-NY,B,BP+A,fill=W1,sw=1.7)
    else:
        g.void(0,DY-NY,BP,A); g.void(BP,DY-NY,B,BP+A)
    g.hatch(0,DY-BP,BP,BP,fill=W3,ang=45,gap=6)
    g.tx(BP/2,DY-BP*0.45,'STALP',size=10,weight='700')
    g.ln(0,0,0,DY,stroke=INK,sw=2.6); g.ln(0,DY,DXP,DY,stroke=INK,sw=2.6)

def vincluri(g):
    """4 vincluri, vazute de sus: bratul scurt intra in sant, cel lung sta pe muchie"""
    out=[]
    nA = max(1, int(BP//150)+1)                          # 1 vinclu la ~150 mm de fasie
    for k in range(nA):
        vx = BP*(k+0.5)/nA
        g.bar(vx-VW/2, DY-NY, VW, VB, fill=METAL, stroke=METAL2, sw=1.4)
        g.ln(vx-min(VA,BP*0.9)/2, DY-NY, vx+min(VA,BP*0.9)/2, DY-NY, stroke=METAL2, sw=3.6)
        out.append((vx, DY-NY+VB/2))
    LB = BP+A
    nB = max(2, int(LB//150)+1)
    for k in range(nB):
        vy = DY-NY + LB*(k+0.5)/nB
        g.bar(NX-VB, vy-VW/2, VB, VW, fill=METAL, stroke=METAL2, sw=1.4)
        g.ln(NX, vy-min(VA,LB/nB*0.9)/2, NX, vy+min(VA,LB/nB*0.9)/2, stroke=METAL2, sw=3.6)
        out.append((NX-VB/2, vy))
    return out

# ═══ 6 · PLANUL DE MONTAJ ═══
g=D(SP,fs=12)
santul(g)
V=vincluri(g)
g.note(V[-1][0],V[-1][1],'vinclu',dx=190,dy=-40,fill=METAL2,weight='700')
g.notes(V[0][0],V[0][1],[f'{len(V)} vincluri pe colt','unul la fiecare ~150 mm de sant'],
        dx=-70,dy=150,fill=METAL2,anchor='end')
F['e0_plan_montaj']=fin(g,'UNDE VIN VINCLURILE',f'vedere de sus  ·  {len(V)} pe colt: {sum(1 for v in V if v[0]<BP)} pe fasia din fata stalpului, restul pe cea laterala')

# ─── sectiuni de montaj, toate la aceeasi scara si acelasi cadru ───
SS   = 1.5
G    = A                      # latimea santului in sectiune
RIM  = 300                    # cat aratam din punte
AIR  = 130                    # cat aratam dincolo de margine
ZBOT = -250
def cadru(g, trench_void=True):
    g.hatch(G,Z_JO_B,RIM,JO,fill=W2,ang=45,gap=7)          # lemnul portant, taiat
    g.bar(G,Z_DECK_B,RIM,DT,fill=W1,sw=1.5)                # dusumea existenta
    g.tx(G+RIM*0.62,Z_JO_B+JO/2,'lemn portant',size=11,fill=MUT)
    g.tx(G+RIM*0.62,Z_DECK_B/2-2,'dusumea',size=10,fill=MUT)
    g.ln(-AIR,0,G+RIM,0,stroke=DIM,sw=0.9,dash='7,5')
    if trench_void: g.void(0,ZBOT,G,abs(ZBOT-Z_DECK_B))
    g.ln(0,Z_DECK_B+60,0,ZBOT-30,stroke=MUT,sw=1,dash='5,5')
    g.tx(-AIR*0.5,Z_DECK_B-52,'marginea puntii',size=10,fill=MUT)
    g.tx(-AIR*0.5,Z_DECK_B-98,'(dincolo: aer)',size=10,fill=MUT)
    if trench_void: g.tx(G*0.5,ZBOT+30,'santul continua in jos',size=10,fill=WARN)

def vin(g, screws=False):
    g.bracket(G,Z_BLOC_B-VT,VA,VB,t=VT,fill=METAL,stroke=METAL2,flip=True,sw=1.7)
    if screws:
        for zz in (Z_BLOC_B-VT+18, Z_BLOC_B-VT+64):
            g.surub(G+2,zz,0,42,stroke=METAL2,sw=2.4)

# ═══ 7 · PASUL 1 ═══
g=D(SS,fs=12)
cadru(g); vin(g,screws=True)
g.dimv(Z_BLOC_B-VT,Z_BLOC_B-VT+VA,G+RIM*0.30,f'{VA}',off=26,fill=DIM,ext=1)
g.dimh(G-VB,G,Z_BLOC_B-VT,f'{VB}',off=30,fill=DIM,ext=1)
g.dimh(0,G,0,f'A = {A}',off=-26,fill=WARN,size=13,ext=1)
g.note(G+30,Z_BLOC_B-VT+64,'4 × surub 5×40, pregaurit 3 mm',dx=210,dy=118,fill=METAL2)
g.note(G-VB*0.5,Z_BLOC_B-VT,'bratul scurt, orizontal — polita',dx=-40,dy=64,fill=METAL2,anchor='end')
F['e0_s1']=fin(g,'PASUL 1 · vinclul','sectiune  ·  bratul lung se prinde in lemnul portant')

# ═══ 8 · PASUL 2 ═══
g=D(SS,fs=12)
cadru(g); vin(g)
g.hatch(0,Z_BLOC_B,G,m['BLOC_H'],fill=W4,ang=-45,gap=6)
g.tx(G*0.45,Z_BLOC_B+m['BLOC_H']*0.45,'blocaj',size=11,fill=INK)
g.dimv(Z_BLOC_B,Z_DECK_B,-AIR*0.15,f"{m['BLOC_H']}",off=-26,fill=ACC,ext=1)
g.dimv(Z_DECK_B,0,G+RIM*0.30,f'{DT}',off=26,fill=DIM,ext=1)
g.note(G*0.45,Z_BLOC_B,'se lasa singur pe cele doua polite',dx=-40,dy=150,fill=ACC,anchor='end',weight='700')
g.note(G*0.5,Z_DECK_B,'ramane 28 pana la fata podelei',dx=210,dy=-120,fill=ACC2)
F['e0_s2']=fin(g,'PASUL 2 · blocajul','sectiune  ·  inca nu se insurubeaza — doar se aseaza')

# ═══ 9 · PASUL 3 ═══
g=D(SS,fs=12)
cadru(g); vin(g)
g.hatch(0,Z_BLOC_B,G,m['BLOC_H'],fill=W4,ang=-45,gap=6)
g.tx(G*0.42,Z_BLOC_B+m['BLOC_H']*0.30,'blocaj',size=11,fill=INK)
g.surub(G*0.30,Z_DECK_B-2,-58,118,stroke=METAL2,sw=2.8)
g.ln(G*0.30,Z_DECK_B-2,G*0.30,Z_DECK_B-105,stroke=DIM,sw=0.9,dash='4,4')
g.tx(G*0.30+30,Z_DECK_B-92,'~30°',size=11,fill=WARN)
g.note(G*0.30,Z_DECK_B-2,'se da de sus, stand pe punte',dx=-40,dy=-95,fill=METAL2,anchor='end',weight='700')
g.note(G*0.30+62,Z_DECK_B-102,'varful ajunge in lemnul portant',dx=210,dy=60,fill=METAL2)
F['e0_s3']=fin(g,'PASUL 3 · suruburile 8×140','sectiune  ·  3 oblic in punte + 2 in stalp, pe fasie')

# ═══ 10 · PASUL 4 ═══
g=D(SS,fs=12)
cadru(g); vin(g)
g.hatch(0,Z_BLOC_B,G,m['BLOC_H'],fill=W4,ang=-45,gap=6)
g.bar(0,Z_DECK_B,G,DT,fill=W1,sw=1.8)
g.surub(G*0.5,0,-90,55,stroke=METAL2,sw=2.4)
g.ln(-AIR,0,G+RIM,0,stroke=ACC,sw=1.6,dash='9,5')
g.note(G*0.5,Z_DECK_B/2,'scandura de calcat, 28',dx=-60,dy=-110,fill=ACC,anchor='end',weight='700')
g.note(G+RIM*0.45,0,'acelasi nivel — verifica cu dreptarul',dx=-30,dy=-70,fill=ACC,anchor='middle')
F['e0_s4']=fin(g,'PASUL 4 · scandura','sectiune  ·  la nivel cu restul podelei')

# ═══ 11 · GATA ═══
g=D(SS,fs=12)
cadru(g,trench_void=False); vin(g)
g.hatch(0,Z_BLOC_B,G,m['BLOC_H'],fill=W4,ang=-45,gap=6)
g.bar(0,Z_DECK_B,G,DT,fill=W1,sw=1.8)
g.arrow(G*0.5,54,G*0.5,DT+8,stroke=ACC,sw=2.6)
g.arrow(G*0.5,Z_BLOC_B+34,G*0.5,Z_BLOC_B-VT+4,stroke=ACC,sw=1.8)
g.arrow(G-VB*0.5+14,Z_BLOC_B-VT*0.5,G+64,Z_BLOC_B-VT*0.5,stroke=ACC,sw=1.8)
g.tx(G*0.5,84,'calci aici',size=12,fill=ACC,weight='700')
g.note(G+64,Z_BLOC_B-VT*0.5,'greutatea pleaca in punte',dx=150,dy=64,fill=ACC,weight='700')
g.note(G-VB*0.7,Z_BLOC_B-VT,'vinclurile raman ascunse dedesubt',dx=-40,dy=90,fill=MUT,anchor='end')
F['e0_gata']=fin(g,'GATA','sectiune  ·  totul la nivel, nimic nu se vede de sus')

# ═══ 10 · DRUMUL GREUTATII ═══
g=D(0.85,fs=13)
lant=[('calci pe scandura',W1),('blocaj',W2),('vinclu',METAL),
      ('lemnul portant al puntii',W2),('stalpii puntii',W3),('pamant',GROUND)]
y=0
for i,(t,c) in enumerate(lant):
    g.bar(0,y,380,54,fill=c,stroke=INK,sw=1.4,r=3)
    g.tx(190,y+18,t,size=13,weight='700' if i in (2,3) else '400')
    if i<len(lant)-1: g.arrow(190,y-6,190,y-34,stroke=ACC,sw=2.2)
    y-=88
g.note(380,-88-27,'nodul care conteaza',dx=60,dy=0,fill=ACC,weight='700')
g.note(380,-176-27,'lemnul pe care calci in fiecare zi',dx=60,dy=0,fill=ACC)
F['e0_forta']=fin(g,'DRUMUL GREUTATII','de la talpa ta pana in pamant')

json.dump(F,open('figs_e0.json','w',encoding='utf-8'))
print('ok',len(F),'desene:',list(F))
