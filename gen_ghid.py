#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Desene pentru GHID-CONSTRUCTIE-casa: izometrii pentru pasi + sectiuni la scara pentru cote.
Geometrie masurata 20.08.2026. Rama din dulap 46x250 taiat in lung (fasii de 100)."""
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
T    = 46                      # grosimea talpii/cununii
VB   = 1700-2*T                # 1608
PITCH_TXT = '8,2°'

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

# ============ E3 · taierea dulapului in lung ============
f=Fig()
box(f,0,0,0, 1300,250,46, top=W1,left=W2,right=W3)
for yy in (100,204):
    a=iso(0,yy,46); b=iso(1300,yy,46)
    f.line(a[0],a[1],b[0],b[1],stroke=ACC2,sw=2.2,dash='9,6')
x,y=iso(650,50,46);  f.text(x,y-6,'fasia 1 — 100',size=14,fill=ACC)
x,y=iso(650,152,46); f.text(x,y-6,'fasia 2 — 100',size=14,fill=ACC)
x,y=iso(650,228,46); f.text(x,y-4,'rest ~42',size=12,fill=MUT)
x,y=iso(-60,125,23); f.text(x-12,y,'46',size=14,fill=MUT,anchor='end')
x,y=iso(1360,125,23); f.text(x+14,y,'250',size=14,fill=MUT,anchor='start')
x,y=iso(200,100,46)
f.rect(x-46,y-96,92,60,fill=METAL,stroke=METAL2,rx=6)
f.text(x,y-60,'circular',size=11,fill='#fff')
f.line(x-70,y-30,x+180,y-30,stroke=METAL2,sw=5)
f.text(x+200,y-34,'rigla dreapta, prinsa cu cleme',size=13,fill=METAL2,anchor='start')
f.text(-260,250,'un dulap 46×250×4000 → 2 fasii de 100 (rama) + 1 fasie de ~42×46 (verticale)',size=15,fill=INK,anchor='start',mono=False)
f.text(-260,274,'adancime de taiere 46 mm — circularul taie 65, merge lejer',size=13,fill=MUT,anchor='start',mono=False)
figs['e3_taiere']=f.svg()

# ============ E4 · peretele din spate, elevatie ============
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
f.text(X(W/2),Y(H+260),'talpa si cununa: fasie de 46×100',size=13,fill=MUT)
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
      f'<text x="0" y="5.5" font-family="ui-monospace,Menlo,monospace" font-size="14" fill="{INK}" text-anchor="middle">panoul ~50 kg</text></g>')
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

json.dump(figs,open('figs_ghid.json','w'))
print('ok',{k:len(v) for k,v in figs.items()})
