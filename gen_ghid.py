#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Desene pentru GHID-CONSTRUCTIE-casa: izometrii pentru pasi + sectiuni la scara pentru cote.
Geometrie masurata 20.08.2026. Rama tuturor peretilor = rigla 48x48x4000 cumparata gata
(13 buc, decizie Vlad 20.08). NU se mai taie niciun dulap in lung. Dulapul de 200x50 are o
singura treaba: reazemul din spate, taiat la 2200, asezat pe muchie cu 200 in sus."""
import math, json, re

INK="#1c1b18"; ACC="#14532d"; ACC2="#8a3016"; MUT="#6b675e"; LN="#cfc9bc"
W1="#e8dfcc"; W2="#d9cdb2"; W3="#c4b696"; W4="#b6a888"
METAL="#9aa1ad"; METAL2="#6f7683"; GLASS="#dce8ea"; GROUND="#b9b2a3"

WB, WF = 1995, 1975
WALL_B, WALL_F = WB-5, WF-5
DEP_L, DEP_R = 1580, 1570
BP, FP = 100, 90
REZ_B, REZ_F = 1900, 1660
SPAN = 1670
SL   = math.atan2(REZ_B-REZ_F, SPAN)
RAFT = 1889
EDGE = 1646
PAS  = WALL_B/4
T    = 48                      # grosimea talpii/cununii (rigla 48x48)
VB   = 1700-2*T                # 1604
assert VB == 1604, VB          # rigla 48: 1700 - 2*48 = 1604
PITCH_TXT = '8,2°'
SLdeg = math.degrees(SL)       # 8,18°

# ── cote pentru desenele de capitol (brief desene-etape-casa) ──
# Toate derivate din constante: schimba T si verticalele se muta singure.
VF     = 1600 - T                        # verticala perete fata = 1552
assert VF == 1552, VF
VL     = [1573, 1645, 1722, 1794]        # verticale laterale, fata->spate (verbatim 20.08)
GEAM   = 490                             # golul de geam lateral
# Campul (talpa − gol)/2 se calculeaza din talpa fiecarui perete — nu se scrie ca sir,
# altfel diverge cand geometria se muta: stanga 1580 -> 545, dreapta 1570 -> 540.
def CAMP(dep): return (dep - GEAM)//2    # camp de fiecare parte a golului, centrat pe talpa
assert CAMP(DEP_L)*2 + GEAM == DEP_L == 1580, (CAMP(DEP_L), DEP_L)   # 545 + 490 + 545
assert CAMP(DEP_R)*2 + GEAM == DEP_R == 1570, (CAMP(DEP_R), DEP_R)   # 540 + 490 + 540
PRAG   = 950                             # inaltimea pragului de geam lateral
STICLA = 440                             # acrilicul, in gol de 490
JOC    = (GEAM - STICLA)//2              # 25 mm joc pe fiecare latura
assert JOC == 25, JOC
BARA_F = WF + 2*FP                       # bara solida 100x60 a peretelui fata = 2155
assert BARA_F == 2155, BARA_F
FER_F  = 570                             # prag+buiandrug fereastra fata, intre jambe
CUN_L  = round(DEP_L/math.cos(SL))       # cununa inclinata lateral stanga = 1596
CUN_R  = round(DEP_R/math.cos(SL))       # cununa inclinata lateral dreapta = 1586
assert (CUN_L, CUN_R) == (1596, 1586), (CUN_L, CUN_R)
BRAT   = 150                             # bratul contrafisei pe fiecare latura
DIAG   = round(BRAT*math.sqrt(2))        # contrafisa pe diagonala = 212
assert DIAG == 212, DIAG
GOL_USA, USA_LIBER = 550, 1600           # golul de usa: 550 latime, 1600 liber vertical
# perete fata — layout masurat de la fata interioara a stalpului stang (brief D6)
FL_CAMP = 115                            # camp pana la prima jamba
FL_FER  = (161, 731)                     # golul ferestrei (latime 570)
FL_USA  = (938, 1488)                    # golul usii (latime 550)
FL_MONT = (1650, 1696)                   # montant de camp (latime 46)
FL_COLT = 274                            # coltul unde sta propteaua de 250
assert FL_FER[1]-FL_FER[0] == FER_F
assert FL_USA[1]-FL_USA[0] == GOL_USA
assert FL_MONT[1]+FL_COLT == WALL_F, (FL_MONT[1], FL_COLT, WALL_F)
# acoperis
DROP    = REZ_B - REZ_F                   # cadere = 240
assert DROP == 240, DROP
BLOC    = round(PAS) - 44                 # inchideri intre capriori = 454 (498 - 44)
assert BLOC == 454, BLOC
RW, RH  = 44, 100                         # sectiunea capriorului: 44 orizontal, 100 vertical
STREASINA = 100
OSB_LEN = 2200                            # latimea acoperisului (dulapul de 2200 taiat)
OSB_W1, OSB_W2 = 1250, round(RAFT-1250)   # placile OSB: 2200x1250 + 2200x639
assert OSB_W2 == 639, OSB_W2

def esc(s): return s.replace('&','&amp;').replace('<','&lt;')

class Fig:
    def __init__(self,x0=0,y0=0,x1=0,y1=0,fs=15):
        self.vb=(x0,y0,x1-x0,y1-y0); self.el=[]; self.fs=fs
        self.bb=[1e9,1e9,-1e9,-1e9]
    def t_(self,x,y):
        b=self.bb; b[0]=min(b[0],x); b[1]=min(b[1],y); b[2]=max(b[2],x); b[3]=max(b[3],y)
    def raw(self,s):
        self.el.append(s)
        for m in re.finditer(r'points="([^"]+)"',s):
            for p in m.group(1).split():
                a,b_=p.split(','); self.t_(float(a),float(b_))
        for m in re.finditer(r'translate\(([-\d.]+) ([-\d.]+)\)',s):
            self.t_(float(m.group(1))-110,float(m.group(2))-30); self.t_(float(m.group(1))+110,float(m.group(2))+30)
    def rect(self,x,y,w,h,fill=W1,stroke=INK,sw=1.6,dash=None,rx=0):
        d=f' stroke-dasharray="{dash}"' if dash else ''; r=f' rx="{rx}"' if rx else ''
        self.el.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}{r}/>')
        self.t_(x,y); self.t_(x+w,y+h)
    def poly(self,pts,fill=W1,stroke=INK,sw=1.6,dash=None):
        p=' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)
        d=f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d} stroke-linejoin="round"/>')
        [self.t_(a,b_) for a,b_ in pts]
    def line(self,x1,y1,x2,y2,stroke=INK,sw=1.4,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"{d} stroke-linecap="round"/>')
        self.t_(x1,y1); self.t_(x2,y2)
    def path(self,d,fill='none',stroke=INK,sw=1.4,dash=None):
        da=f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da} stroke-linecap="round"/>')
        for m in re.finditer(r'(-?[\d.]+) (-?[\d.]+)',d): self.t_(float(m.group(1)),float(m.group(2)))
    def text(self,x,y,s,size=None,fill=INK,anchor='middle',weight='400',rot=None,mono=True):
        size=size or self.fs
        fam='ui-monospace,Menlo,monospace' if mono else 'system-ui,-apple-system,Helvetica,sans-serif'
        r=f' transform="rotate({rot} {x:.1f} {y:.1f})"' if rot is not None else ''
        self.el.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{r}>{esc(s)}</text>')
        wpx=len(s)*size*0.58
        dx={'middle':wpx/2,'start':0,'end':wpx}[anchor]
        self.t_(x-dx,y-size); self.t_(x-dx+wpx,y+size*0.4)
    def dim(self,x1,y1,x2,y2,label,vertical=False,fill=MUT,off=-9,size=13):
        self.line(x1,y1,x2,y2,stroke=fill,sw=1); t=6
        for (x,y) in [(x1,y1),(x2,y2)]:
            if vertical: self.line(x-t,y,x+t,y,stroke=fill,sw=1)
            else: self.line(x,y-t,x,y+t,stroke=fill,sw=1)
        mx,my=(x1+x2)/2,(y1+y2)/2
        if vertical: self.text(mx+off,my,label,size=size,fill=fill,rot=-90)
        else: self.text(mx,my+off,label,size=size,fill=fill)
    def badge(self,x,y,n,c=ACC):
        self.el.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="{c}" stroke="#fff" stroke-width="2.5"/>')
        self.t_(x-14,y-14); self.t_(x+14,y+14)
        self.text(x,y+4.6,str(n),size=13,fill='#fff',weight='700')
    def dot(self,x,y,r=2.6,fill=MUT):
        self.el.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}"/>')
        self.t_(x-r,y-r); self.t_(x+r,y+r)
    def note(self,x,y,s,dx,dy,anchor='start',fill=MUT,size=12):
        self.line(x,y,x+dx,y+dy,stroke=fill,sw=1); self.dot(x,y,fill=fill)
        self.text(x+dx+(5 if anchor=='start' else -5),y+dy-3,s,size=size,fill=fill,anchor=anchor)
    def arrow(self,x1,y1,x2,y2,stroke=ACC,sw=2.2):
        self.line(x1,y1,x2,y2,stroke=stroke,sw=sw)
        a=math.atan2(y2-y1,x2-x1); L=8
        self.line(x2,y2,x2-L*math.cos(a-0.42),y2-L*math.sin(a-0.42),stroke=stroke,sw=sw)
        self.line(x2,y2,x2-L*math.cos(a+0.42),y2-L*math.sin(a+0.42),stroke=stroke,sw=sw)
    def svg(self,pad=26):
        x0,y0,x1,y1=self.bb
        x,y,w,h = x0-pad, y0-pad, (x1-x0)+2*pad, (y1-y0)+2*pad
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" '
                f'style="width:100%;height:auto;display:block">'+'\n'.join(self.el)+'</svg>')

K=0.55
def iso(x,y,z): return ((x-y)*math.cos(math.radians(30))*K, ((x+y)*math.sin(math.radians(30))-z)*K)
def box(f,ox,oy,oz,dx,dy,dz,top=W1,left=W2,right=W3,stroke=INK,sw=1.4,alpha=None):
    p=lambda X,Y,Z: iso(ox+X,oy+Y,oz+Z)
    A=p(0,0,dz);B=p(dx,0,dz);C=p(dx,dy,dz);D=p(0,dy,dz);E=p(0,0,0);F_=p(dx,0,0);G=p(dx,dy,0)
    op=f' opacity="{alpha}"' if alpha else ''
    for pts,fill in (((A,B,C,D),top),((A,B,F_,E),left),((B,C,G,F_),right)):
        s=' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)
        f.raw(f'<polygon points="{s}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"{op}/>')
def screw(f,x,y,ang=-60,L=26,c=METAL2):
    a=math.radians(ang); dx,dy=math.cos(a)*L,math.sin(a)*L
    f.line(x,y,x+dx,y+dy,stroke=c,sw=3); f.line(x+dx*0.7,y+dy*0.7,x+dx,y+dy,stroke=c,sw=6)

figs={}

# ============ E0 · coltul din spate ============
def corner(f, brackets=False, block=False, board=False):
    box(f,0,0,0, 460,100,200, top=W2,left=W3,right=W4)              # grinda de margine
    box(f,0,100,180, 460,300,28, top=W1,left=W2,right=W3)           # dusumea
    box(f,500,0,-150, 90,90,520, top=W2,left=W3,right=W4)           # stalpul de colt
    if brackets:
        for gy in (14,62):
            box(f,426,gy,150, 34,24,6, top=METAL,left=METAL2,right=METAL2)
            box(f,460,gy,150, 46,24,6, top=METAL,left=METAL2,right=METAL2)
    if block: box(f,460,0,156, 40,100,52, top="#cdbf9c",left=W4,right="#a89a76")
    if board: box(f,426,0,180, 116,100,28, top=W1,left=W2,right=W3)

f=Fig()
corner(f)
x,y=iso(480,50,180); f.line(x,y,x+110,y-64,stroke=ACC2,sw=1.4)
f.text(x+118,y-68,'gol ~100 — nimic dedesubt',size=15,fill=ACC2,anchor='start')
x,y=iso(500,50,-90); f.text(x,y+30,'stalpul de colt, infipt in pamant',size=13,fill=MUT)
x,y=iso(160,300,208); f.text(x,y+26,'dusumeaua existenta',size=13,fill=MUT)
x,y=iso(120,0,100); f.text(x-30,y+40,'grinda groasa de la marginea podelei',size=13,fill=MUT,anchor='end')
figs['e0_acum']=f.svg()

f=Fig()
corner(f,brackets=True,block=True,board=True)
x,y=iso(430,40,158); f.badge(x-40,y+4,1)
x,y=iso(480,50,190); f.badge(x+4,y-34,2)
x,y=iso(486,50,208); f.badge(x+52,y+6,3)
for i,(n,s) in enumerate([('1','doua vincluri, ca doua polite pe grinda'),
                          ('2','blocajul se lasa pe ele'),
                          ('3','scandura de calcat, la nivel cu podeaua')]):
    f.text(-150,270+i*24,f'{n}  {s}',size=15,fill=INK,anchor='start',mono=False)
figs['e0_gata']=f.svg()

S=0.34; X=lambda mm: mm*S; Y=lambda mm: -mm*S
f=Fig()
f.rect(X(-60),Y(-40),X(920),X(120),fill=GROUND,stroke='none')
f.rect(X(0),Y(200),X(500),X(200),fill=W2); f.text(X(250),Y(96),'grinda groasa',size=13,fill=MUT)
f.rect(X(0),Y(228),X(500),X(28),fill=W1)
f.rect(X(600),Y(560),X(90),X(760),fill=W2); f.text(X(645),Y(420),'stalp 90×90',size=12,fill=MUT,rot=-90)
f.rect(X(470),Y(176),X(30),X(6),fill=METAL,stroke=METAL2)
f.rect(X(500),Y(176),X(46),X(6),fill=METAL,stroke=METAL2)
f.text(X(556),Y(166),'vinclu 90×65 — polita',size=13,fill=METAL2,anchor='start')
f.rect(X(500),Y(228),X(100),X(52),fill='#cdbf9c'); f.text(X(550),Y(194),'blocaj',size=12)
f.rect(X(470),Y(256),X(130),X(28),fill=W1); f.text(X(535),Y(268),'scandura',size=11)
for sx in (520,555,585): f.line(X(sx),Y(254),X(sx-40),Y(146),stroke=METAL2,sw=2.4)
f.text(X(455),Y(118),'3× 8×140 oblic in grinda',size=13,fill=METAL2,anchor='end')
for sy in (300,370): f.line(X(600),Y(sy),X(556),Y(sy-18),stroke=METAL2,sw=2.4)
f.text(X(700),Y(350),'2× 8×140 in stalp',size=13,fill=METAL2,anchor='start')
f.dim(X(500),Y(320),X(600),Y(320),'gol ~100',fill=ACC2)
f.text(X(300),Y(-95),'calci pe scandura → blocaj → vinclu → grinda groasa → pamant',size=13,fill=ACC)
figs['e0_sectiune']=f.svg()

# ============ E1 · cioata ============
S=0.155; X=lambda mm: mm*S; Y=lambda mm: -mm*S
f=Fig()
f.rect(X(-120),Y(0),X(2500),X(30),fill=W2); f.text(X(-110),Y(-150),'puntea',size=13,fill=MUT,anchor='start')
f.rect(X(300),Y(1600),X(90),X(1600),fill=W2)
f.rect(X(295),Y(1660),X(100),X(60),fill=W1)
f.rect(X(1970),Y(1700),X(100),X(1700),fill=W2)
f.rect(X(1970),Y(1900),X(50),X(200),fill=W1)
f.poly([(X(245),Y(1652)),(X(2120),Y(1922)),(X(2120),Y(1966)),(X(245),Y(1696))],fill=W1)
f.text(X(1150),Y(1930),'acoperisul',size=13,fill=MUT)
f.line(X(245),Y(1646),X(140),Y(1548),stroke=ACC2,sw=1.4)
f.text(X(130),Y(1528),f'muchia {EDGE}',size=13,fill=ACC2,anchor='end')
f.rect(X(700),Y(1500),X(150),X(1500),fill=W3)
f.line(X(690),Y(1500),X(1080),Y(1500),stroke=ACC2,sw=1,dash='4,4')
f.line(X(690),Y(1646),X(1080),Y(1646),stroke=ACC2,sw=1,dash='4,4')
f.dim(X(1090),Y(1646),X(1090),Y(1500),'138',vertical=True,off=-11,fill=ACC2)
f.text(X(1150),Y(1600),'= treapta directa',size=12,fill=ACC2,anchor='start')
f.text(X(1150),Y(1480),'pe acoperis',size=12,fill=ACC2,anchor='start')
f.dim(X(660),Y(1500),X(660),Y(0),'1500 acum',vertical=True,off=-11,fill=ACC2)
f.rect(X(1400),Y(700),X(150),X(700),fill='#cdbf9c')
f.rect(X(1335),Y(742),X(280),X(42),fill=W1)
f.dim(X(1660),Y(742),X(1660),Y(0),'700 dupa',vertical=True,off=13,fill=ACC)
f.text(X(1475),Y(830),'masuta',size=13,fill=ACC)
f.text(X(1475),Y(-150),'taiat la 600–750',size=13,fill=ACC)
figs['e1_cioata']=f.svg()

# ============ E3 · peretele din spate, elevatie ============
S=0.172; X=lambda mm: mm*S; Y=lambda mm: -mm*S
f=Fig()
H=1700; W=WALL_B
f.rect(X(0),Y(T),X(W),X(T),fill=W2)
f.rect(X(0),Y(H),X(W),X(T),fill=W2)
XS=[round(i*PAS) for i in range(5)]
for x0 in XS:
    xx=min(max(x0-23,0),W-46)
    f.rect(X(xx),Y(H-T),X(46),X(H-2*T),fill=W1)
f.line(X(46+300),Y(T),X(46),Y(T+300),stroke=ACC,sw=5)
f.line(X(W-46-300),Y(T),X(W-46),Y(T+300),stroke=ACC,sw=5)
f.line(X(46+150),Y(H-T),X(46),Y(H-T-150),stroke=ACC,sw=5)
f.line(X(W-46-150),Y(H-T),X(W-46),Y(H-T-150),stroke=ACC,sw=5)
f.text(X(W/2),Y(H+520),'proptele: jos brate de 300 (424) · sus brate de 150 (212)',size=13,fill=ACC)
for i in range(4): f.dim(X(XS[i]),Y(-330),X(XS[i+1]),Y(-330),str(XS[i+1]-XS[i]))
f.dim(X(0),Y(-640),X(W),Y(-640),f'{W}   —   M3 real 1995, minus 5 mm joc',size=14)
f.dim(X(-150),Y(0),X(-150),Y(H),'1700',vertical=True,off=-12)
f.dim(X(W+150),Y(T),X(W+150),Y(H-T),f'verticale {VB} ×5',vertical=True,off=-12,fill=ACC)
f.text(X(W/2),Y(H+260),'talpa si cununa: rigla 48×48',size=13,fill=MUT)
figs['e4_perete']=f.svg()

# ============ E4 · ridicarea pe rampa ============
S=0.078; X=lambda mm: mm*S; Y=lambda mm: -mm*S
f=Fig()
DECK_X0,DECK_X1,DZ=2150,4300,2228
RX0,RZ0 = -1250,60                      # baza rampei; panta ~34 grade pe scanduri de 4 m
f.rect(X(RX0-300),Y(0),X((DECK_X1+300)-(RX0-300)),X(60),fill=GROUND,stroke='none')
for px in (2250,4100): f.rect(X(px),Y(DZ),X(100),X(DZ),fill=W3)
f.rect(X(DECK_X0),Y(DZ),X(DECK_X1-DECK_X0),X(70),fill=W2)
f.rect(X(2250),Y(DZ+1700),X(100),X(1700),fill=W3)
# rampa
f.poly([(X(RX0),Y(RZ0)),(X(DECK_X0),Y(DZ)),(X(DECK_X0),Y(DZ-120)),(X(RX0),Y(RZ0-120))],fill=W1)
# panoul
ang=math.degrees(math.atan2((DZ-RZ0)*S,(DECK_X0-RX0)*S))
cx,cy=X((RX0+DECK_X0)/2), Y((RZ0+DZ)/2+170)
f.raw(f'<g transform="translate({cx:.1f} {cy:.1f}) rotate({-ang:.1f})">'
      f'<rect x="-92" y="-17" width="184" height="34" fill="{W1}" stroke="{INK}" stroke-width="1.8"/>'
      f'<text x="0" y="5.5" font-family="ui-monospace,Menlo,monospace" font-size="14" fill="{INK}" text-anchor="middle">panoul ~32-41 kg</text></g>')
# franghia
f.path(f'M {X(2300):.1f} {Y(DZ+1300):.1f} Q {X(1700):.1f} {Y(DZ+250):.1f} {cx:.1f} {cy:.1f}',stroke=ACC2,sw=2.2,dash='8,6')
# oameni
def om(x,zb,lbl,side):
    f.raw(f'<circle cx="{X(x):.1f}" cy="{Y(zb)-32:.1f}" r="10" fill="{METAL2}"/>')
    f.line(X(x),Y(zb)-22,X(x),Y(zb)-3,stroke=METAL2,sw=3.4)
    f.text(X(x),Y(zb)-46,lbl,size=13,fill=MUT,anchor=side)
om(-900,60,'unul jos, impinge','end')
om(3100,DZ+70,'unul sus, trage','middle')
# etichete, fiecare in spatiu liber
f.text(X(500),Y(-330),'doua scanduri de 4 m, ca rampa  —  panta ~34°',size=13,fill=MUT)
f.text(X(3400),Y(DZ-420),'puntea, 2,2 m',size=13,fill=MUT)
f.text(X(2450),Y(DZ+1560),'franghie legata de stalpul de 4 m si de rama',size=13,fill=ACC2,anchor='start')
f.text(X(2450),Y(DZ+1400),'daca scapa, nu pleaca peste margine',size=12,fill=MUT,anchor='start')
f.text(X(1200),Y(-720),'zi fara vant  ·  2 adulti  ·  copiii nu sunt pe punte si nu sunt sub panou',size=15,fill=ACC2,weight='700')
figs['e4_ridicare']=f.svg()

# ============ E4 · prinderea in stalp ============
f=Fig()
box(f,0,0,0, 100,100,900, top=W2,left=W3,right=W4)
box(f,100,10,120, 520,80,660, top=W1,left=W2,right=W3)
for zz in (190,410,450,650):
    x,y=iso(100,50,zz); screw(f,x-2,y,ang=-6,L=30)
x,y=iso(100,50,930); f.text(x-10,y-26,'4 suruburi 8×140',size=15,fill=METAL2)
x,y=iso(100,50,900); f.text(x-10,y-8,'unul jos · doua la mijloc · unul sus',size=12,fill=MUT)
x,y=iso(50,50,-60);  f.text(x,y+44,'stalpul de 4 m',size=13,fill=MUT)
x,y=iso(500,50,700); f.text(x+26,y-30,'capatul peretelui',size=13,fill=MUT,anchor='start')
f.text(-260,250,'gaura de 6 mm data inainte in stalp — altfel crapa',size=14,fill=ACC2,anchor='start',mono=False)
figs['e4_prindere']=f.svg()

# ══════════════════════ E4 · peretii laterali ══════════════════════

# ── D1/D2 · elevatie perete lateral (parametric) ──
def lateral_elev(dep, cun):
    S=0.175; X=lambda mm: mm*S; Y=lambda mm: -mm*S
    f=Fig()
    camp=CAMP(dep)                                    # 545 stanga · 540 dreapta
    tops=[T+v for v in VL]
    xs=[0, camp-T, camp+GEAM, dep-T]                  # 0 · camp-48 · camp+490 · dep-48
    f.rect(X(0),Y(T),X(dep),X(T),fill=W2)                              # talpa
    f.poly([(X(0),Y(tops[0])),(X(dep),Y(tops[3])),
            (X(dep),Y(tops[3]+T)),(X(0),Y(tops[0]+T))],fill=W2)        # cununa inclinata
    for xi,v in zip(xs,VL):                                            # verticale
        f.rect(X(xi),Y(T+v),X(T),X(v),fill=W1)
        f.text(X(xi+T/2),Y(T+v/2),str(v),size=11,fill=MUT,rot=-90)
    gx0,gx1=camp,camp+GEAM                                            # golul de geam, centrat pe talpa
    f.rect(X(gx0),Y(PRAG),X(GEAM),X(T),fill=W2)                        # pragul
    f.rect(X(gx0),Y(PRAG+GEAM+T),X(GEAM),X(T),fill=W2)                 # buiandrugul
    f.rect(X(gx0),Y(PRAG+GEAM),X(GEAM),X(GEAM),fill=GLASS,stroke=ACC)
    f.text(X((gx0+gx1)/2),Y(PRAG+GEAM/2),f'GOL {GEAM}',size=12,fill=ACC,weight='600')
    yd=Y(-70)
    f.dim(X(0),yd,X(gx0),yd,str(camp),size=11)
    f.dim(X(gx0),yd,X(gx1),yd,str(GEAM))
    f.dim(X(gx1),yd,X(dep),yd,str(camp),size=11)
    f.dim(X(0),Y(-260),X(dep),Y(-260),f'talpa {dep}',size=13)
    px=X(gx0)-26
    f.dim(px,Y(0),px,Y(PRAG),f'prag {PRAG}',vertical=True,off=-10,fill=ACC)
    mx=dep/2; my=(tops[0]+tops[3])/2+T/2
    f.text(X(mx),Y(my)+30,f'cununa {cun}',size=12,fill=ACC,rot=-SLdeg)
    f.text(X(0),Y(-370),'FATA',size=11,fill=MUT,anchor='start')
    f.text(X(dep),Y(-370),'SPATE  (mai inalt)',size=11,fill=MUT,anchor='end')
    return f.svg()

figs['lat_stanga']=lateral_elev(DEP_L,CUN_L)
figs['lat_dreapta']=lateral_elev(DEP_R,CUN_R)

# ── D3 · detaliu gol de geam, sectiune orizontala ──
# x = de-a lungul peretelui (golul 490, lat); y = prin grosime (exagerat): interior jos, exterior sus.
f=Fig()
S=0.5; X=lambda mm: mm*S; Y=lambda mm: -mm*S
DEPz=200; c=DEPz/2                                                    # grosimea desenata (exagerat)
f.rect(X(-150),Y(DEPz),X(150),X(DEPz),fill=W3,stroke=INK)            # toc stanga (rama golului)
f.rect(X(GEAM),Y(DEPz),X(150),X(DEPz),fill=W3,stroke=INK)           # toc dreapta
f.text(X(-75),Y(c),'toc',size=11,fill=MUT,rot=-90)
f.text(X(GEAM+75),Y(c),'toc',size=11,fill=MUT,rot=-90)
f.rect(X(JOC),Y(c+14),X(STICLA),X(28),fill=GLASS,stroke=ACC)         # acrilic 440, centrat
f.text(X(GEAM/2),Y(c),'acrilic',size=11,fill=ACC,weight='600')
for sx0 in (0,GEAM-70):                                              # sipci pe ambele fete, la marginile golului
    f.rect(X(sx0),Y(c-16),X(70),X(28),fill=W1,stroke=INK)            # sipca interioara (jos)
    f.rect(X(sx0),Y(c+72),X(70),X(28),fill=W1,stroke=INK)           # sipca exterioara (sus)
f.text(X(35),Y(c-30),'1 · sipca interioara',size=9.5,fill=MUT,anchor='start')
f.text(X(35),Y(c+50),'3 · sipca exterioara',size=9.5,fill=MUT,anchor='start')
f.text(X(GEAM/2),Y(c+34),'2 · acrilic (din exterior)',size=9.5,fill=ACC,anchor='middle')
f.text(X(GEAM+165),Y(c-4),'interior',size=10,fill=MUT,anchor='start')
f.text(X(GEAM+165),Y(c+84),'exterior',size=10,fill=MUT,anchor='start')
# cote de-a lungul golului
f.dim(X(0),Y(DEPz+52),X(GEAM),Y(DEPz+52),f'gol {GEAM}',size=12)
f.dim(X(JOC),Y(DEPz+18),X(GEAM-JOC),Y(DEPz+18),f'acrilic {STICLA}',size=11,fill=ACC)
f.dim(X(0),Y(-46),X(JOC),Y(-46),str(JOC),size=10,fill=ACC2)
f.dim(X(GEAM-JOC),Y(-46),X(GEAM),Y(-46),str(JOC),size=10,fill=ACC2)
f.text(X(GEAM/2),Y(-84),'joc 25 pe fiecare latura (490 − 440)',size=10.5,fill=ACC2)
# surub prin acrilic + gaura +1 mm
scx=GEAM-95
f.line(X(scx),Y(c+86),X(scx),Y(c-2),stroke=METAL2,sw=3)
f.text(X(scx),Y(c+100),'+1 mm',size=11,fill=ACC2,weight='600')
figs['lat_geam']=f.svg()

# ── D4 · detaliu colt cu contrafisa ──
f=Fig()
S=0.42; X=lambda mm: mm*S; Y=lambda mm: -mm*S
L4=360
f.rect(X(0),Y(T),X(L4),X(T),fill=W2,stroke=INK)              # talpa
f.rect(X(0),Y(L4),X(T),X(L4-T),fill=W1,stroke=INK)           # verticala de colt
f.text(X(T/2),Y(L4*0.68),'verticala',size=10,fill=MUT,rot=-90)
f.text(X(L4*0.66),Y(T/2),'talpa',size=10,fill=MUT)
A=(T+BRAT,T+T); B=(T+T,T+BRAT)                               # capetele contrafisei (pe fata interioara)
f.line(X(A[0]),Y(A[1]),X(B[0]),Y(B[1]),stroke=INK,sw=20)     # contur contrafisa
f.line(X(A[0]),Y(A[1]),X(B[0]),Y(B[1]),stroke=W3,sw=16)      # corpul (rigla 48 pe diagonala)
f.text(X((A[0]+B[0])/2+46),Y((A[1]+B[1])/2+46),f'contrafisa {DIAG}',size=11,fill=INK,rot=45,anchor='middle')
f.dim(X(T),Y(-44),X(T+BRAT),Y(-44),f'brat {BRAT}',size=11)   # brat pe talpa
f.dim(X(-44),Y(T),X(-44),Y(T+BRAT),f'brat {BRAT}',vertical=True,off=-10,size=11)  # brat pe verticala
f.note(X(A[0]),Y(A[1]),'taiere 45°',dx=X(44),dy=-16,anchor='start',fill=ACC2,size=10)
f.note(X(B[0]),Y(B[1]),'taiere 45°',dx=X(-8),dy=-48,anchor='end',fill=ACC2,size=10)
f.text(X(L4),Y(-74),'rigla 48×48 (din rest)',size=10.5,fill=MUT,anchor='end')
figs['lat_colt']=f.svg()

# ── D5 · perete lateral in sectiune verticala, cu lambriul (detaliu marit) ──
f=Fig()
S=1.5; X=lambda mm: mm*S; Y=lambda mm: -mm*S
LT=12.5; LW=96; OV=18                                        # lambriu 12,5×96, falt ~18
RH5=2*(LW-OV)+LW                                             # inaltimea ramei = cat acopera 3 lamele
f.rect(X(0),Y(T+RH5),X(T),X(RH5),fill=W2,stroke=INK)       # rama 48×48 (in sectiune, verticala)
f.text(X(T/2),Y(T+RH5*0.5),'rama 48×48',size=10,fill=MUT,rot=-90)
for i in range(3):
    yb=T + i*(LW-OV)
    f.rect(X(T),Y(yb+LW),X(LT),X(LW),fill=W1,stroke=INK)     # lamela pe fata ramei
    f.rect(X(T),Y(yb+LW),X(LT),X(OV),fill=W2,stroke=INK)     # zona de suprapunere (falt) cu lamela de deasupra
    sy=yb+LW-LW/2                                            # surubul intra in rama
    f.line(X(T+LT),Y(sy),X(2),Y(sy),stroke=METAL2,sw=3)
    f.line(X(4),Y(sy-6),X(2),Y(sy),stroke=METAL2,sw=3); f.line(X(4),Y(sy+6),X(2),Y(sy),stroke=METAL2,sw=3)
ytop=T+RH5
f.dim(X(0),Y(ytop+24),X(T),Y(ytop+24),'48',size=10)
f.dim(X(T),Y(ytop+24),X(T+LT),Y(ytop+24),'12,5',size=10)
f.note(X(T+LT),Y(T+RH5-LW*0.5),'lambriu 12,5×96',dx=X(30),dy=-18,anchor='start',size=11)
f.note(X(T+LT),Y(T+(LW-OV)+LW-OV/2),'falt: calca peste',dx=X(30),dy=6,anchor='start',size=10)
f.note(X(T+LT),Y(T+(LW-OV)+LW-OV/2-18),'lamela de sub ea',dx=X(30),dy=24,anchor='start',size=10)
f.note(X(T+2),Y(T+LW*0.5),'surub in fiecare verticala',dx=X(30),dy=34,anchor='start',fill=METAL2,size=10)
f.text(X(0),Y(T-30),'direct pe rama:',size=10.5,fill=ACC2,anchor='start')
f.text(X(0),Y(T-50),'fara folie, fara sipci, fara OSB',size=10.5,fill=ACC2,anchor='start')
figs['lat_sect']=f.svg()


# ══════════════════ NODURI · cum se intalnesc peretii ══════════════════
LT = 12.5                       # grosimea lambriului
BAG = T                         # bagheta de colt = rigla 48x48 din rest

def colt_plan(post, et_a, et_b, note_post):
    """Plan de sus la un colt. Stalpul e imbinarea: peretii nu se ating.
       Exteriorul spate = sus (y<0), exteriorul lateral = stanga (x<0)."""
    f=Fig(); S=1.9; X=lambda mm: mm*S; Y=lambda mm: mm*S
    # stalpul, in plan
    f.rect(X(0),Y(0),X(post),X(post),fill=W3,stroke=INK,sw=2)
    f.text(X(post/2),Y(post/2)+5,f'{post}×{post}',size=11,fill=INK)
    # rama peretelui A (spate/fata): pleaca din stalp spre dreapta, grosime T pe y
    f.rect(X(post),Y(0),X(210),X(T),fill=W2,stroke=INK)
    f.text(X(post+118),Y(T/2)+4,f'rama {T}',size=10,fill=MUT)
    # rama peretelui B (lateral): pleaca din stalp in jos, grosime T pe x
    f.rect(X(0),Y(post),X(T),X(210),fill=W2,stroke=INK)
    f.text(X(T/2),Y(post+118),f'rama {T}',size=10,fill=MUT,rot=-90)
    # lambriu pe peretele A — trece peste stalp, pana la fata exterioara a lateralei
    f.rect(X(-LT),Y(-LT),X(post+210+LT),X(LT),fill=W1,stroke=INK)
    # lambriu pe peretele B — se opreste in muchia celui de sus
    f.rect(X(-LT),Y(0),X(LT),X(post+210),fill=W1,stroke=INK)
    # bagheta de colt, peste imbinare, pe fata peretelui A
    f.rect(X(-LT),Y(-LT-BAG),X(BAG),X(BAG),fill=W4,stroke=ACC2,sw=2)
    f.note(X(-LT+BAG),Y(-LT-BAG/2),f'bagheta de colt {BAG}×{BAG}, din rest',dx=X(34),dy=-16,anchor='start',fill=ACC2,size=11)
    f.note(X(-LT/2),Y(post+96),'lambriu 12,5',dx=X(-14),dy=X(52),anchor='end',size=10)
    # suruburi: fiecare perete in stalp, oblic
    for k in range(2):
        yy=post*0.3+k*post*0.4
        f.line(X(post+34),Y(yy),X(post-30),Y(yy+16),stroke=METAL2,sw=3)
    for k in range(2):
        xx=post*0.3+k*post*0.4
        f.line(X(xx),Y(post+34),X(xx+16),Y(post-30),stroke=METAL2,sw=3)
    f.note(X(post+30),Y(post*0.62),'8×140 oblic in stalp',dx=X(46),dy=X(40),anchor='start',fill=METAL2,size=10.5)
    f.text(X(post+210),Y(-LT-BAG-26),et_a,size=11,fill=ACC,anchor='end')
    f.text(X(-LT-BAG-14),Y(post+210),et_b,size=11,fill=ACC,anchor='end',rot=-90)
    f.text(X(post+40),Y(post+250),note_post,size=10.5,fill=ACC2,anchor='start')
    f.text(X(post+30),Y(-LT-BAG-52),'PLAN — vazut de sus',size=11,fill=MUT,anchor='start')
    return f

f = colt_plan(BP,'perete SPATE','perete LATERAL','peretii nu se ating: stalpul e imbinarea')
figs['nod_colt_spate']=f.svg()

f = colt_plan(FP,'perete FATA','perete LATERAL','acelasi nod, stalp mai subtire')
figs['nod_colt_fata']=f.svg()

# ── N3 · sus la spate: laterala trece peste cununa spatelui ──
f=Fig(); S=1.05; X=lambda mm: mm*S; Y=lambda mm: -mm*S
B0=1180                                                              # de aici in jos, stalpul e rupt
f.rect(X(0),Y(1700),X(BP),X(1700-B0),fill=W3,stroke=INK,sw=2)        # stalpul spate, partea de sus
f.text(X(BP/2),Y(1420),'stalp 100',size=11,fill=MUT,rot=-90)
for _a,_b in [(-6,BP*0.3),(BP*0.3,BP*0.62),(BP*0.62,BP+6)]:
    f.line(X(_a),Y(B0+(9 if _a<BP*0.4 else -9)),X(_b),Y(B0+(-9 if _a<BP*0.4 else 9)),stroke=INK,sw=1.4)
f.rect(X(BP),Y(1700),X(520),X(T),fill=W2,stroke=INK)                 # cununa peretelui din spate
f.text(X(BP+260),Y(1700-T/2)+4,'cununa perete spate',size=10.5,fill=MUT)
f.rect(X(0),Y(1900),X(BP+520),X(200),fill=W4,stroke=ACC2,sw=2)       # dulapul de reazem, pe muchie
f.text(X((BP+520)/2),Y(1800)+5,'dulap 200×50 pe muchie',size=11,fill=ACC2)
f.dim(X(BP+520+40),Y(1700),X(BP+520+40),Y(1900),'200',vertical=True,size=11)
# capriorul, peste dulap
f.poly([(X(-140),Y(1900)),(X(BP+520),Y(1900)),(X(BP+520),Y(2000)),(X(-140),Y(2000))],fill=W1,stroke=INK)
f.text(X(200),Y(1950)+4,'caprior 44×100',size=10.5,fill=MUT)
# peretele lateral, vazut din capat (grosimea T), oprit la 1893
f.rect(X(-140-T),Y(1893),X(T),X(1893-B0),fill=W2,stroke=INK,dash='5 4')
f.text(X(-140-T/2),Y(1500),'perete lateral (capat)',size=10,fill=MUT,rot=-90)
f.dim(X(-140-T-34),Y(B0),X(-140-T-34),Y(1893),'1893 peste podea',vertical=True,size=11)
f.dim(X(BP+520+110),Y(B0),X(BP+520+110),Y(1700),'1700',vertical=True,size=11)
f.line(X(-140-T),Y(1893),X(0),Y(1893),stroke=ACC2,sw=1.4,dash='4 4')
f.note(X(-140-T),Y(1893),'cununa se scrie pe caprior, la fata locului',dx=X(20),dy=X(150),anchor='start',fill=ACC2,size=10.5)
f.text(X(200),Y(B0-90),'SECTIUNE — coltul din spate, sus',size=11,fill=MUT)
figs['nod_sus_spate']=f.svg()

# ── N4 · sus la fata: bara 100×60 peste stalpi ──
f=Fig(); S=1.05; X=lambda mm: mm*S; Y=lambda mm: -mm*S
B0=1120
f.rect(X(0),Y(1600),X(FP),X(1600-B0),fill=W3,stroke=INK,sw=2)        # stalp fata
f.text(X(FP/2),Y(1360),'stalp 90',size=11,fill=MUT,rot=-90)
for _a,_b in [(-6,FP*0.3),(FP*0.3,FP*0.62),(FP*0.62,FP+6)]:
    f.line(X(_a),Y(B0+(9 if _a<FP*0.4 else -9)),X(_b),Y(B0+(-9 if _a<FP*0.4 else 9)),stroke=INK,sw=1.4)
f.rect(X(FP),Y(1600),X(520),X(T),fill=W2,stroke=INK)                 # ultima vertical + rama fata
f.text(X(FP+260),Y(1600-T/2)+4,'rama perete fata',size=10.5,fill=MUT)
f.rect(X(-60),Y(1660),X(FP+560),X(60),fill=W4,stroke=ACC2,sw=2)      # bara 100x60, 60 in sus
f.text(X((FP+500)/2),Y(1630)+5,'bara 100×60 — 60 in sus',size=11,fill=ACC2)
f.dim(X(FP+520+40),Y(1600),X(FP+520+40),Y(1660),'60',vertical=True,size=11)
f.poly([(X(-200),Y(1660)),(X(FP+520),Y(1660)),(X(FP+520),Y(1760)),(X(-200),Y(1760))],fill=W1,stroke=INK)
f.text(X(120),Y(1710)+4,'caprior 44×100',size=10.5,fill=MUT)
f.rect(X(-200-T),Y(1666),X(T),X(1666-B0),fill=W2,stroke=INK,dash='5 4')
f.text(X(-200-T/2),Y(1400),'perete lateral (capat)',size=10,fill=MUT,rot=-90)
f.dim(X(-200-T-34),Y(B0),X(-200-T-34),Y(1666),'1666 peste podea',vertical=True,size=11)
f.dim(X(FP+520+110),Y(B0),X(FP+520+110),Y(1600),'1600',vertical=True,size=11)
f.note(X(-200-T),Y(1666),'aceeasi scriere pe caprior ca la spate',dx=X(20),dy=X(150),anchor='start',fill=ACC2,size=10.5)
f.text(X(160),Y(B0-90),'SECTIUNE — coltul din fata, sus',size=11,fill=MUT)
figs['nod_sus_fata']=f.svg()


json.dump(figs,open('figs_ghid.json','w'))
print('ok',{k:len(v) for k,v in figs.items()})
