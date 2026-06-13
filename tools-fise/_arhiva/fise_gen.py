# -*- coding: utf-8 -*-
import os
from iso import render
PROJ="/sessions/funny-pensive-ritchie/mnt/CASUTA DIN COPAC"

# ---- geometrie (mm) ----
PS=100; W=2100; D=1780
JX=[100,280,720,1120,1550,1980]
FRONT_TOP=1872; BACK_TOP=2300; BEAM_TOP=2072; JO_TOP=2172; DECK_TOP=2200

WHITE='#ffffff'; GRAY='#f3efe9'
def b(x,y,z,dx,dy,dz,**k): d=dict(x=x,y=y,z=z,dx=dx,dy=dy,dz=dz); d.update(k); return d

def posts(stage, clip=None):
    fh = 2600 if stage==1 else FRONT_TOP
    P=[]
    coords=[(0,0),(W-PS,0),(0,D-PS),(W-PS,D-PS)]
    for i,(x,z) in enumerate(coords):
        top = fh if i<2 else BACK_TOP
        y0=0; dy=top
        if clip and clip<top: y0=clip; dy=top-clip
        P.append(b(x,y0,z,PS,dy,PS,fill=WHITE))
    return P

def polite(): # 2 blocuri sub grinda spate, pe fata interioara a stalpilor spate
    return [b(0,1772,D-PS-90,PS,100,90,fill=WHITE),
            b(W-PS,1772,D-PS-90,PS,100,90,fill=WHITE)]

def beam_back(): return b(0,1872,D-90,W,200,90,fill=WHITE)
def beam_front(): return b(0,1872,0,W,200,90,fill=WHITE)
def joists():
    return [b(x,JO_TOP,-700,PS,PS,D+700,fill=WHITE) for x in JX]
def deck(n=17):
    out=[]; z=-700
    for i in range(n):
        out.append(b(-20,DECK_TOP-28,z,W+40,28,140,fill=WHITE)); z+=150
    return out

# scena acumulata pana la 'stage', cu piesele 'cur' evidentiate
def scene(stage, clip=None, hl=None, extras=None):
    hl=hl or set(); S=[]
    def add(boxes,key):
        for bx in boxes:
            if key in hl: bx=dict(bx); bx['hl']=True; bx.pop('fill',None)
            S.append(bx)
    add(posts(stage,clip),'posts')
    if stage>=3: add(polite(),'polite')
    if stage>=4: add([beam_back()],'beam_back')
    if stage>=5: add([beam_front()],'beam_front')
    if stage>=6: add(joists(),'joists')
    if stage>=10: add(deck(17 if stage>10 else 9),'deck')
    if extras: 
        for e in extras: S.append(e)
    return S

PARTS={
 'ST':('POZE/COD_7337253.png','Stalp KVH 100x100'),
 'GR':('POZE/COD_5483835.png','Grinda glulam 90x200'),
 'JO':('POZE/COD_7337253.png','Joista 100x100'),
 'DL':('POZE/COD_6224073.png','Dusumea larice 28x145'),
 'PO':('POZE/lemn.png','Polita (offcut 100x100)'),
 'BL':('POZE/lemn.png','Blocaj (offcut)'),
 'CF':('POZE/lemn.png','Contrafisa (offcut)'),
 'PT':('POZE/lemn.png','Proptea temporara'),
 'C1':('POZE/COD_738965.png','Coltar 100x100x90'),
 'C2':('POZE/COD_738910.png','Coltar 90x90x65'),
 'H1':('POZE/COD_10434633.png','Heco 8x200'),
 'H2':('POZE/COD_10434398.png','Heco 6x100'),
 'H3':('POZE/COD_10434139.png','Heco 6x80'),
 'H4':('POZE/COD_10528829.png','Inox 5x60'),
 'B1':('POZE/COD_12130958.png','Tija M12 (taie 220)'),
 'B2':('POZE/COD_6834285.png','Bulon M12x120'),
 'B3':('POZE/COD_3840897.png','Saiba M12'),
 'B4':('POZE/COD_3830642.png','Piulita M12'),
 'F1':('POZE/COD_5509678.png','Ulei tec'),
 'PAP':('POZE/papuc.svg','Papuc reazem U'),
}

def hero(stage, **kw): return render(scene(stage, clip=kw.get('clip'), hl=kw.get('hl'), extras=kw.get('extras')),
                                     screws=kw.get('screws'), dims=kw.get('dims'), W=kw.get('W',640))

# proptele (diagonale) ca extras pt stage 1
def props_extra():
    e=[]
    for (x,z,dx,dz) in [(-300,300,80,80)]:
        pass
    # 4 proptele scurte diagonale la baza (schematic, ca niste cutii inclinate evitate) -> folosim linii in caption
    return e

# ---- desene detaliu 2D (zoom bule), stil simplu alb-negru ----
DET_POLITA='''<svg viewBox="0 0 360 230" xmlns="http://www.w3.org/2000/svg">
<rect x="60" y="20" width="70" height="200" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<text x="95" y="40" text-anchor="middle" font-family="Space Mono,monospace" font-size="11" fill="#5C574E">stalp spate</text>
<rect x="130" y="120" width="80" height="70" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<text x="170" y="210" text-anchor="middle" font-family="Space Mono,monospace" font-size="11" fill="#5C574E">polita</text>
<circle cx="120" cy="140" r="5.5" fill="#161413"/><circle cx="120" cy="172" r="5.5" fill="#161413"/>
<line x1="120" y1="140" x2="250" y2="120" stroke="#161413" stroke-width="2.2"/>
<line x1="120" y1="172" x2="250" y2="195" stroke="#161413" stroke-width="2.2"/>
<rect x="250" y="108" width="34" height="18" rx="4" fill="#161413"/><text x="267" y="121" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="Space Mono,monospace">B1</text>
<rect x="250" y="186" width="34" height="18" rx="4" fill="#161413"/><text x="267" y="199" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="Space Mono,monospace">B1</text>
<text x="300" y="155" font-family="Space Grotesk" font-size="12" fill="#C2693A">2 buloane</text>
</svg>'''

DET_C2='''<svg viewBox="0 0 360 230" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="150" width="280" height="50" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<text x="60" y="142" font-family="Space Mono,monospace" font-size="11" fill="#5C574E">grinda</text>
<rect x="150" y="80" width="70" height="74" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<text x="185" y="72" text-anchor="middle" font-family="Space Mono,monospace" font-size="11" fill="#5C574E">joista</text>
<path d="M220 110 h22 v44" fill="none" stroke="#161413" stroke-width="5"/>
<rect x="248" y="96" width="34" height="18" rx="4" fill="#161413"/><text x="265" y="109" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="Space Mono,monospace">C2</text>
<path d="M185 70 v-22" stroke="#C2693A" stroke-width="2.4" marker-end="url(#a)"/>
<defs><marker id="a" markerWidth="10" markerHeight="10" refX="4" refY="1" orient="auto"><path d="M0 8 L4 0 L8 8 z" fill="#C2693A"/></marker></defs>
<text x="185" y="40" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#C2693A">vrea sa se ridice</text>
</svg>'''

DET_BLOC='''<svg viewBox="0 0 360 230" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="150" width="280" height="40" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<text x="55" y="178" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">grinda</text>
<rect x="90" y="40" width="48" height="150" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<rect x="222" y="40" width="48" height="150" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<text x="114" y="32" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">joista</text>
<text x="246" y="32" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">joista</text>
<rect x="138" y="120" width="84" height="40" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<text x="180" y="145" text-anchor="middle" font-family="Space Grotesk" font-size="13" fill="#161413">BL</text>
<line x1="146" y1="116" x2="170" y2="160" stroke="#161413" stroke-width="2.6"/>
<rect x="120" y="96" width="34" height="18" rx="4" fill="#161413"/><text x="137" y="109" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="Space Mono,monospace">H3</text>
<text x="270" y="110" font-family="Space Grotesk" font-size="12" fill="#C2693A">oblic</text>
</svg>'''

DET_DECK='''<svg viewBox="0 0 360 210" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="140" width="280" height="34" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<text x="55" y="164" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">joista</text>
<rect x="60" y="96" width="120" height="34" rx="3" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<rect x="190" y="96" width="120" height="34" rx="3" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<line x1="180" y1="90" x2="190" y2="90" stroke="#C2693A" stroke-width="2.6"/>
<text x="185" y="80" text-anchor="middle" font-family="Space Mono,monospace" font-size="11" fill="#C2693A">5 mm</text>
<circle cx="100" cy="113" r="5" fill="#161413"/><circle cx="150" cy="113" r="5" fill="#161413"/>
<circle cx="230" cy="113" r="5" fill="#161413"/><circle cx="280" cy="113" r="5" fill="#161413"/>
<rect x="300" y="104" width="34" height="18" rx="4" fill="#161413"/><text x="317" y="117" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="Space Mono,monospace">H4</text>
</svg>'''

DET_BRACE='''<svg viewBox="0 0 360 230" xmlns="http://www.w3.org/2000/svg">
<rect x="70" y="20" width="44" height="190" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<text x="92" y="14" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">stalp</text>
<rect x="40" y="40" width="190" height="40" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<text x="180" y="34" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">grinda</text>
<polygon points="114,90 150,90 250,200 214,200" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<text x="205" y="165" font-family="Space Grotesk" font-size="12" fill="#5C574E" transform="rotate(46 205 165)">contrafisa CF</text>
<circle cx="126" cy="100" r="4.5" fill="#161413"/><circle cx="133" cy="114" r="4.5" fill="#161413"/><circle cx="140" cy="128" r="4.5" fill="#161413"/>
<rect x="150" y="96" width="34" height="18" rx="4" fill="#161413"/><text x="167" y="109" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="Space Mono,monospace">H1</text>
<text x="60" y="225" font-family="Space Grotesk" font-size="11" fill="#C2693A">3 suruburi / capat</text>
</svg>'''
