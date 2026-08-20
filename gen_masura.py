#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fisa de masurat golul de la colturile din spate. Trei numere pe colt."""
import json
from kit import *

F={}
BP=100                 # stalp spate, masurat cu ruleta
A,B,C = 100,100,520    # NECUNOSCUTE — desenate nominal, ca sa se vada forma

# ═════════════ 1 · PLAN ═════════════
S=0.62
g=D(S,fs=13)
DX,DY = 820,660                    # cat din punte aratam
PY0 = DY-BP                        # fata din fata a stalpului
NX, NY0 = BP+B, DY-BP-A            # decupajul: latime NX, de la NY0 in sus

# dusumea: benzi stanga-dreapta, cu rost; ocolesc decupajul
brd, rost = 145, 5
yy = DY
while yy > 0:
    h = min(brd, yy)
    if h > 6: g.bar(0, yy-h, DX, h, fill=W1, sw=1.1)
    yy -= h+rost
# decupajul din dusumea: se taie peste benzi
g.bar(0, NY0, NX, BP+A, fill='#faf8f3', stroke='none')

# golul in L
g.void(0,  NY0, BP, A)
g.void(BP, NY0, B, BP+A)

# stalpul
g.hatch(0,PY0,BP,BP,fill=W3,ang=45,gap=6)
g.tx(BP/2,PY0+BP*0.55,'STALP',size=11,weight='700')
g.tx(BP/2,PY0+BP*0.18,'100',size=10,fill=MUT)

# marginile puntii
g.ln(0,0,0,DY,stroke=INK,sw=2.6)
g.ln(0,DY,DX,DY,stroke=INK,sw=2.6)

# cote — doar litere, explicatiile stau in text
g.dimv(NY0,PY0,-6,'A',off=-30,fill=WARN,size=17,ext=1)
g.dimh(BP,NX,NY0,'B',off=30,fill=WARN,size=17,ext=1)
g.tx(-46,(NY0+PY0)/2-34,'?',size=15,fill=WARN,weight='700',px=False) if False else None

# etichete de orientare, departe de desen
g.tx(DX*0.55, DY+58, 'spre vecin  —  spatele puntii', size=12, fill=MUT)
g.tx(-64, DY*0.45, 'marginea puntii', size=12, fill=MUT, rot=-90)
g.tx(DX*0.62, DY*0.42, 'dusumea existenta', size=12, fill=MUT)
g.tx(DX*0.5, -78, 'VEDERE DE SUS  ·  coltul din spate', size=16, weight='700')
g.tx(DX*0.5, -128, 'stai pe punte, te uiti in jos', size=12, fill=MUT)
F['masura_plan']=g.svg(pad=36)

# ═════════════ 2 · SECTIUNE ═════════════
S=0.55
g=D(S,fs=13)
DT=28
g.hatch(-BP,-680,BP,680,fill=W3,ang=45,gap=6)          # stalpul, taiat vertical
g.tx(-BP/2,-360,'stalp',size=11,fill=MUT,rot=-90)
g.bar(B,-DT,520,DT,fill=W1)                            # dusumea, dincolo de gol
g.tx(B+260,-DT/2-3,'dusumea',size=11,fill=MUT)
g.void(0,-680,B,680)
g.arrow(B/2,-40,B/2,-640,stroke=WARN,sw=2.2)
g.tx(B/2+44,-360,'C',size=17,fill=WARN,weight='700')
g.ln(-BP-190,0,B+560,0,stroke=DIM,sw=0.9,dash='7,5')
g.tx(-BP-200,-5,'nivelul podelei',size=11,fill=DIM,anchor='end')
g.dimh(0,B,-700,'B',off=26,fill=WARN,size=15,ext=1)
g.tx(B/2+150,-880,'C = pana unde vezi cand te uiti in gol.',size=12,fill=WARN,anchor='start')
g.tx(B/2+150,-950,'Daca vezi pamantul, scrie "gol".',size=12,fill=WARN,anchor='start')
g.tx(B/2+150,-1060,'Se vede grinda groasa dedesubt?  DA / NU',size=12,fill=ACC2,anchor='start',weight='700')
g.tx(B/2+100,200,'SECTIUNE  ·  prin gol',size=16,weight='700')
F['masura_sect']=g.svg(pad=36)

json.dump(F,open('figs_masura.json','w',encoding='utf-8'))
print('ok', {k:len(v) for k,v in F.items()})
