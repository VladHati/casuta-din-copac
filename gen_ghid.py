#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Desene pentru GHID-CONSTRUCTIE-casa: izometrii pentru pasi + sectiuni la scara pentru cote.
Geometrie masurata 20.08.2026. Rama tuturor peretilor = rigla 46x46x3000 cumparata gata
(25 buc, decizie Vlad 21.08 — 46x46x4000 are stoc zero la Colosseum). NU se mai taie niciun dulap in lung. Dulapul de 200x50 are o
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
T    = 46                      # grosimea talpii/cununii (rigla 46x46)
VB   = 1700-2*T                # rigla 46: 1700 - 2*46 = 1608
assert VB == 1700-2*T, VB
PITCH_TXT = '8,2°'
SLdeg = math.degrees(SL)       # 8,18°

# ── cote pentru desenele de capitol (brief desene-etape-casa) ──
# Toate derivate din constante: schimba T si verticalele se muta singure.
VF     = 1600 - T                        # verticala perete fata (T=46 -> 1554)
assert VF == 1600-T, VF
# Lumina intre talpa si cununa, masurata 20.08 (cotele brute de atunci erau scrise pe o rama
# de 44; lumina e aceea plus 2x44). Verticala se scade din lumina, deci urmeaza grosimea ramei.
VL_CLEAR = [1669, 1741, 1818, 1890]
VL     = [c-2*T for c in VL_CLEAR]       # verticale laterale, fata->spate
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
FL_MONT = (1650, 1650+T)                 # montant de camp (latime = grosimea ramei)
FL_COLT = 274                            # coltul unde sta propteaua de 250
assert FL_FER[1]-FL_FER[0] == FER_F
assert FL_USA[1]-FL_USA[0] == GOL_USA
assert FL_MONT[1]+FL_COLT == WALL_F+(T-46), (FL_MONT[1], FL_COLT, WALL_F)
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

# ─────────────────────────── MATERIALE ───────────────────────────
# Fiecare piesa de lemn desenata isi poarta tipul si sectiunea.
# Cumparate = tonuri deschise, contur simplu. Existente pe santier = ton mai gri + hasura.
# (cheie): fill, eticheta pe piesa, eticheta din legenda, existent
MATS = {
 'ram' : ('#ece2c8', 'rigla 46×46',     'rigla 46×46×3000 — rama peretilor si tocurile', 0),
 'cap' : ('#d8c49a', 'caprior 44×100',  'caprior 44×100 = 2× scandura 22×100 laminate', 0),
 'scn' : ('#e3d5b3', 'scandura 22×100', 'scandura 22×100×4000',                   0),
 'lam' : ('#f7f2e8', 'lambriu 19×116',  'lambriu 19×116×4000',                     0),
 'osb' : ('#c9bd9a', 'OSB3 12',         'placa OSB3 12 mm',                       0),
 'ond' : ('#b07f57', 'Onduline',        'Onduline 2000×860',                      0),
 'sip' : ('#efe7d4', 'sipca 18×28',     'sipca 18×28 — bagheta de geam',          0),
 'plx' : (GLASS,     'plexi 4',         'plexiglas 4 mm',                         0),
 'pvc' : (GLASS,     'PVC 56×56',       'fereastra PVC 56×56',                    0),
 'st10': ('#b9ab8c', 'stalp 100×100',   'stalp spate 100×100 — pe santier',       1),
 'st9' : ('#b9ab8c', 'stalp 90×90',     'stalp fata 90×90 — pe santier',          1),
 'dul' : ('#c6b693', 'dulap 200×50',    'dulap 200×50×4000 — il ai',              1),
 'bara': ('#c6b693', 'bara 100×60',     'bara 100×60×3000 — o ai',                1),
 'dus' : ('#ded3b8', 'dusumea 28',      'dusumea larice 28×145 — pe santier',     1),
 'gri' : ('#ada085', 'grinda',          'grinda podelei — pe santier',            1),
 'met' : (METAL,     '',                'vinclu · coltar · placa metalica',       0),
}
_HX = [0]


class Fig:
    def __init__(self,x0=0,y0=0,x1=0,y1=0,fs=15):
        self.vb=(x0,y0,x1-x0,y1-y0); self.el=[]; self.fs=fs
        _HX[0]+=1; self.hid=_HX[0]; self.mats=[]
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
    def piece(self,x,y,w,h,mat,label=True,sw=1.6,stroke=INK,dash=None):
        """Deseneaza o piesa de lemn: fill dupa material, hasura daca e existenta,
           eticheta in piesa daca incape. Materialul intra in legenda desenului."""
        fill,short,_long,exist = MATS[mat]
        self.rect(x,y,w,h,fill=fill,stroke=stroke,sw=sw,dash=dash)
        if not hasattr(self,'mats'): self.mats=[]
        if mat not in self.mats: self.mats.append(mat)
        if exist:
            self.el.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
                           f'fill="url(#hx{self.hid})" stroke="none"/>')
        if label and short:
            fs=9.5; need=len(short)*fs*0.56
            if w>=need+8 and h>=fs+7:
                self.text(x+w/2,y+h/2+fs*0.36,short,size=fs,fill=MUT)
            elif h>=need+8 and w>=fs+7:
                self.text(x+w/2,y+h/2,short,size=fs,fill=MUT,rot=-90)
        return self

    def key(self,cols=2,size=10):
        """Legenda desenului: doar materialele care apar in el."""
        ms=getattr(self,'mats',[])
        if not ms: return self
        x0,y0,x1,y1=self.bb
        top=y1+30; sw_,gap,rowh = 20,9,19
        colw=max(len(MATS[m][2]) for m in ms)*size*0.58+sw_+gap+30
        for i,m in enumerate(ms):
            cx=x0+(i%cols)*colw; cy=top+(i//cols)*rowh
            fill,_s,lng,exist=MATS[m]
            self.rect(cx,cy,sw_,11,fill=fill,stroke=INK,sw=1)
            if exist:
                self.el.append(f'<rect x="{cx:.1f}" y="{cy:.1f}" width="{sw_}" height="11" '
                               f'fill="url(#hx{self.hid})" stroke="none"/>')
            self.text(cx+sw_+gap,cy+9,lng,size=size,fill=MUT,anchor='start')
        return self

    def svg(self,pad=26):
        x0,y0,x1,y1=self.bb
        x,y,w,h = x0-pad, y0-pad, (x1-x0)+2*pad, (y1-y0)+2*pad
        dfs=(f'<defs><pattern id="hx{self.hid}" width="8" height="8" patternUnits="userSpaceOnUse" '
             f'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" '
             f'stroke="#00000026" stroke-width="2.6"/></pattern></defs>')
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" '
                f'style="width:100%;height:auto;display:block">'+dfs+'\n'.join(self.el)+'</svg>')

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
f.rect(X(600),Y(560),X(90),X(760),fill=W2); f.text(X(645),Y(420),'stalp 90×90 (existent)',size=12,fill=ACC2,rot=-90)
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
f.text(X(W/2),Y(H+260),'talpa si cununa: rigla 46×46',size=13,fill=MUT)
figs['e4_perete']=f.svg()

# ============ E4 · ridicarea pe rampa ============
S=0.078; X=lambda mm: mm*S; Y=lambda mm: -mm*S
f=Fig()
DECK_X0,DECK_X1,DZ=2150,4300,2228
RX0,RZ0 = -1250,60                      # baza rampei; panta ~34 grade pe scanduri de 4 m
f.rect(X(RX0-300),Y(0),X((DECK_X1+300)-(RX0-300)),X(60),fill=GROUND,stroke='none')
for px in (2250,4100): f.piece(X(px),Y(DZ),X(100),X(DZ),'st10',label=False)
f.piece(X(DECK_X0),Y(DZ),X(DECK_X1-DECK_X0),X(70),'dus',label=False)
f.piece(X(2250),Y(DZ+1700),X(100),X(1700),'st10',label=False)
# rampa — doua scanduri de 4 m, provizoriu
f.poly([(X(RX0),Y(RZ0)),(X(DECK_X0),Y(DZ)),(X(DECK_X0),Y(DZ-120)),(X(RX0),Y(RZ0-120))],fill=MATS['scn'][0])
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
f.mats.append('scn')
figs['e4_ridicare']=f.key().svg()

# ============ E4 · prinderea in stalp ============
f=Fig()
box(f,0,0,0, 100,100,900, top=W2,left=W3,right=W4)
box(f,100,10,120, 520,80,660, top=W1,left=W2,right=W3)
for zz in (190,410,450,650):
    x,y=iso(100,50,zz); screw(f,x-2,y,ang=-6,L=30)
x,y=iso(100,50,930); f.text(x-10,y-26,'4 suruburi 8×140',size=15,fill=METAL2)
x,y=iso(100,50,900); f.text(x-10,y-8,'unul jos · doua la mijloc · unul sus',size=12,fill=MUT)
x,y=iso(50,50,-60);  f.text(x,y+44,'stalpul de 4 m — deja pe santier, nu se cumpara',size=13,fill=ACC2)
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
    f.piece(X(0),Y(T),X(dep),X(T),'ram')                               # talpa
    f.poly([(X(0),Y(tops[0])),(X(dep),Y(tops[3])),
            (X(dep),Y(tops[3]+T)),(X(0),Y(tops[0]+T))],fill=MATS['ram'][0])   # cununa inclinata
    for xi,v in zip(xs,VL):                                            # verticale
        f.piece(X(xi),Y(T+v),X(T),X(v),'ram',label=False)
        f.text(X(xi+T/2),Y(T+v/2),str(v),size=10.5,fill=MUT,rot=-90)
    gx0,gx1=camp,camp+GEAM                                            # golul de geam, centrat pe talpa
    f.piece(X(gx0),Y(PRAG),X(GEAM),X(T),'ram')                         # pragul
    f.piece(X(gx0),Y(PRAG+GEAM+T),X(GEAM),X(T),'ram')                  # buiandrugul
    f.piece(X(gx0),Y(PRAG+GEAM),X(GEAM),X(GEAM),'plx',stroke=ACC,label=False)
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
    f.text(X(mx),Y(-470),'toata rama peretelui e din aceeasi rigla de 46×46',size=11,fill=ACC)
    return f.key().svg()

figs['lat_stanga']=lateral_elev(DEP_L,CUN_L)
figs['lat_dreapta']=lateral_elev(DEP_R,CUN_R)

# ── D3 · detaliu gol de geam, sectiune orizontala ──
# x = de-a lungul peretelui (golul 490, lat); y = prin grosime (exagerat): interior jos, exterior sus.
f=Fig()
S=0.5; X=lambda mm: mm*S; Y=lambda mm: -mm*S
DEPz=200; c=DEPz/2                                                    # grosimea desenata (exagerat)
f.piece(X(-150),Y(DEPz),X(150),X(DEPz),'ram',label=False)            # toc stanga (rama golului)
f.piece(X(GEAM),Y(DEPz),X(150),X(DEPz),'ram',label=False)            # toc dreapta
f.text(X(-75),Y(c),'toc · rigla 46×46',size=10,fill=MUT,rot=-90)
f.text(X(GEAM+75),Y(c),'toc · rigla 46×46',size=10,fill=MUT,rot=-90)
f.piece(X(JOC),Y(c+14),X(STICLA),X(28),'plx',stroke=ACC,label=False)  # acrilic 440, centrat
f.text(X(GEAM/2),Y(c),'acrilic',size=11,fill=ACC,weight='600')
for sx0 in (0,GEAM-70):                                              # sipci pe ambele fete, la marginile golului
    f.piece(X(sx0),Y(c-16),X(70),X(28),'sip',label=False)            # sipca interioara (jos)
    f.piece(X(sx0),Y(c+72),X(70),X(28),'sip',label=False)            # sipca exterioara (sus)
f.text(X(35),Y(c-30),'1 · sipca interioara 18×28',size=9.5,fill=MUT,anchor='start')
f.text(X(35),Y(c+50),'3 · sipca exterioara 18×28',size=9.5,fill=MUT,anchor='start')
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
figs['lat_geam']=f.key().svg()

# ── D4 · detaliu colt cu contrafisa ──
f=Fig()
S=0.42; X=lambda mm: mm*S; Y=lambda mm: -mm*S
L4=360
f.piece(X(0),Y(T),X(L4),X(T),'ram',label=False)              # talpa
f.piece(X(0),Y(L4),X(T),X(L4-T),'ram',label=False)           # verticala de colt
f.text(X(T/2),Y(L4*0.68),'verticala · rigla 46×46',size=10,fill=MUT,rot=-90)
f.text(X(L4*0.66),Y(T/2),'talpa · rigla 46×46',size=10,fill=MUT)
A=(T+BRAT,T+T); B=(T+T,T+BRAT)                               # capetele contrafisei (pe fata interioara)
f.line(X(A[0]),Y(A[1]),X(B[0]),Y(B[1]),stroke=INK,sw=20)     # contur contrafisa
f.line(X(A[0]),Y(A[1]),X(B[0]),Y(B[1]),stroke=MATS['ram'][0],sw=16)   # corpul (rigla 46 pe diagonala)
f.text(X((A[0]+B[0])/2+46),Y((A[1]+B[1])/2+46),f'contrafisa · rigla 46×46 · {DIAG}',size=10.5,fill=INK,rot=45,anchor='middle')
f.dim(X(T),Y(-44),X(T+BRAT),Y(-44),f'brat {BRAT}',size=11)   # brat pe talpa
f.dim(X(-44),Y(T),X(-44),Y(T+BRAT),f'brat {BRAT}',vertical=True,off=-10,size=11)  # brat pe verticala
f.note(X(A[0]),Y(A[1]),'taiere 45°',dx=X(44),dy=-16,anchor='start',fill=ACC2,size=10)
f.note(X(B[0]),Y(B[1]),'taiere 45°',dx=X(-8),dy=-48,anchor='end',fill=ACC2,size=10)
f.text(X(L4),Y(-74),'tot din rigla 46×46, din resturi',size=10.5,fill=MUT,anchor='end')
figs['lat_colt']=f.key().svg()

# ── D5 · perete lateral in sectiune verticala, cu lambriul (detaliu marit) ──
f=Fig()
S=1.5; X=lambda mm: mm*S; Y=lambda mm: -mm*S
LT=19;   LW=116; OV=13                                       # lambriu 19×116, uluc ~13
RH5=2*(LW-OV)+LW                                             # inaltimea ramei = cat acopera 3 lamele
f.piece(X(0),Y(T+RH5),X(T),X(RH5),'ram',label=False)       # rama 46×46 (in sectiune, verticala)
f.text(X(T/2),Y(T+RH5*0.5),'rama · rigla 46×46',size=10,fill=MUT,rot=-90)
for i in range(3):
    yb=T + i*(LW-OV)
    f.piece(X(T),Y(yb+LW),X(LT),X(LW),'lam',label=False)     # lamela pe fata ramei
    f.rect(X(T),Y(yb+LW),X(LT),X(OV),fill=MATS['ram'][0],stroke=INK)   # zona de suprapunere (falt)
    sy=yb+LW-LW/2                                            # surubul intra in rama
    f.line(X(T+LT),Y(sy),X(2),Y(sy),stroke=METAL2,sw=3)
    f.line(X(4),Y(sy-6),X(2),Y(sy),stroke=METAL2,sw=3); f.line(X(4),Y(sy+6),X(2),Y(sy),stroke=METAL2,sw=3)
ytop=T+RH5
f.dim(X(0),Y(ytop+24),X(T),Y(ytop+24),'48',size=10)
f.dim(X(T),Y(ytop+24),X(T+LT),Y(ytop+24),'12,5',size=10)
f.note(X(T+LT),Y(T+RH5-LW*0.5),'lambriu 19×116',dx=X(30),dy=-18,anchor='start',size=11)
f.note(X(T+LT),Y(T+(LW-OV)+LW-OV/2),'falt: calca peste',dx=X(30),dy=6,anchor='start',size=10)
f.note(X(T+LT),Y(T+(LW-OV)+LW-OV/2-18),'lamela de sub ea',dx=X(30),dy=24,anchor='start',size=10)
f.note(X(T+2),Y(T+LW*0.5),'surub in fiecare verticala',dx=X(30),dy=34,anchor='start',fill=METAL2,size=10)
f.text(X(0),Y(T-30),'direct pe rama:',size=10.5,fill=ACC2,anchor='start')
f.text(X(0),Y(T-50),'fara folie, fara sipci, fara OSB',size=10.5,fill=ACC2,anchor='start')
figs['lat_sect']=f.key().svg()


# ══════════════════ NODURI · cum se intalnesc peretii ══════════════════
LT = 12.5                       # grosimea lambriului
BAG = T                         # bagheta de colt = rigla 46x48 din rest

def colt_plan(post, et_a, et_b, note_post):
    """Plan de sus la un colt. Stalpul e imbinarea: peretii nu se ating.
       Exteriorul spate = sus (y<0), exteriorul lateral = stanga (x<0)."""
    f=Fig(); S=1.9; X=lambda mm: mm*S; Y=lambda mm: mm*S
    # stalpul, in plan
    f.piece(X(0),Y(0),X(post),X(post),'st10' if post==BP else 'st9',sw=2,label=False)
    f.text(X(post/2),Y(post/2)+4,f'{post}×{post}',size=11,fill=INK)
    # rama peretelui A (spate/fata): pleaca din stalp spre dreapta, grosime T pe y
    f.piece(X(post),Y(0),X(210),X(T),'ram',label=False)
    f.text(X(post+118),Y(T/2)+4,'rigla 46×46',size=10,fill=MUT)
    # rama peretelui B (lateral): pleaca din stalp in jos, grosime T pe x
    f.piece(X(0),Y(post),X(T),X(210),'ram',label=False)
    f.text(X(T/2),Y(post+118),'rigla 46×46',size=10,fill=MUT,rot=-90)
    # lambriu pe peretele A — trece peste stalp, pana la fata exterioara a lateralei
    f.piece(X(-LT),Y(-LT),X(post+210+LT),X(LT),'lam',label=False)
    # lambriu pe peretele B — se opreste in muchia celui de sus
    f.piece(X(-LT),Y(0),X(LT),X(post+210),'lam',label=False)
    # bagheta de colt, peste imbinare, pe fata peretelui A
    f.piece(X(-LT),Y(-LT-BAG),X(BAG),X(BAG),'ram',stroke=ACC2,sw=2,label=False)
    f.note(X(-LT+BAG),Y(-LT-BAG/2),f'bagheta de colt — rigla 46×46, din rest',dx=X(34),dy=-16,anchor='start',fill=ACC2,size=11)
    f.note(X(-LT/2),Y(post+96),'lambriu 19×116',dx=X(-14),dy=X(52),anchor='end',size=10)
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
    return f.key()

f = colt_plan(BP,'perete SPATE','perete LATERAL','peretii nu se ating: stalpul e imbinarea')
figs['nod_colt_spate']=f.svg()

f = colt_plan(FP,'perete FATA','perete LATERAL','acelasi nod, stalp mai subtire')
figs['nod_colt_fata']=f.svg()

# ── N3 · sus la spate: laterala trece peste cununa spatelui ──
f=Fig(); S=1.05; X=lambda mm: mm*S; Y=lambda mm: -mm*S
B0=1180                                                              # de aici in jos, stalpul e rupt
f.piece(X(0),Y(1700),X(BP),X(1700-B0),'st10',sw=2,label=False)       # stalpul spate, partea de sus
f.text(X(BP/2),Y(1420),'stalp 100×100',size=11,fill=ACC2,rot=-90)
for _a,_b in [(-6,BP*0.3),(BP*0.3,BP*0.62),(BP*0.62,BP+6)]:
    f.line(X(_a),Y(B0+(9 if _a<BP*0.4 else -9)),X(_b),Y(B0+(-9 if _a<BP*0.4 else 9)),stroke=INK,sw=1.4)
f.piece(X(BP),Y(1700),X(520),X(T),'ram',label=False)                 # cununa peretelui din spate
f.text(X(BP+260),Y(1700-T/2)+4,'cununa · rigla 46×46',size=10.5,fill=MUT)
f.piece(X(0),Y(1900),X(BP+520),X(200),'dul',stroke=ACC2,sw=2,label=False)   # dulapul de reazem, pe muchie
f.text(X((BP+520)/2),Y(1800)+5,'dulap 200×50 pe muchie — taiat 2200',size=11,fill=ACC2)
f.dim(X(BP+520+40),Y(1700),X(BP+520+40),Y(1900),'200',vertical=True,size=11)
# capriorul, peste dulap
f.poly([(X(-140),Y(1900)),(X(BP+520),Y(1900)),(X(BP+520),Y(2000)),(X(-140),Y(2000))],fill=MATS['cap'][0],stroke=INK)
f.text(X(200),Y(1950)+4,'caprior 44×100 (2× scandura 22×100)',size=10.5,fill=MUT)
f.mats.append('cap')
# peretele lateral, vazut din capat (grosimea T), oprit la 1893
f.piece(X(-140-T),Y(1893),X(T),X(1893-B0),'ram',dash='5 4',label=False)
f.text(X(-140-T/2),Y(1500),'perete lateral',size=10,fill=MUT,rot=-90)
f.dim(X(-140-T-34),Y(B0),X(-140-T-34),Y(1893),'1893 peste podea',vertical=True,size=11)
f.dim(X(BP+520+110),Y(B0),X(BP+520+110),Y(1700),'1700',vertical=True,size=11)
f.line(X(-140-T),Y(1893),X(0),Y(1893),stroke=ACC2,sw=1.4,dash='4 4')
f.note(X(-140-T),Y(1893),'cununa se scrie pe caprior, la fata locului',dx=X(20),dy=X(150),anchor='start',fill=ACC2,size=10.5)
f.text(X(200),Y(B0-90),'SECTIUNE — coltul din spate, sus',size=11,fill=MUT)
figs['nod_sus_spate']=f.key().svg()

# ── N4 · sus la fata: bara 100×60 peste stalpi ──
f=Fig(); S=1.05; X=lambda mm: mm*S; Y=lambda mm: -mm*S
B0=1120
f.piece(X(0),Y(1600),X(FP),X(1600-B0),'st9',sw=2,label=False)        # stalp fata
f.text(X(FP/2),Y(1360),'stalp 90×90',size=11,fill=ACC2,rot=-90)
for _a,_b in [(-6,FP*0.3),(FP*0.3,FP*0.62),(FP*0.62,FP+6)]:
    f.line(X(_a),Y(B0+(9 if _a<FP*0.4 else -9)),X(_b),Y(B0+(-9 if _a<FP*0.4 else 9)),stroke=INK,sw=1.4)
f.piece(X(FP),Y(1600),X(520),X(T),'ram',label=False)                 # ultima vertical + rama fata
f.text(X(FP+260),Y(1600-T/2)+4,'rama fata · rigla 46×46',size=10.5,fill=MUT)
f.piece(X(-60),Y(1660),X(FP+560),X(60),'bara',stroke=ACC2,sw=2,label=False)   # bara 100x60, 60 in sus
f.text(X((FP+500)/2),Y(1630)+5,'bara 100×60 — 60 in sus, taiata 2155',size=11,fill=ACC2)
f.dim(X(FP+520+40),Y(1600),X(FP+520+40),Y(1660),'60',vertical=True,size=11)
f.poly([(X(-200),Y(1660)),(X(FP+520),Y(1660)),(X(FP+520),Y(1760)),(X(-200),Y(1760))],fill=MATS['cap'][0],stroke=INK)
f.text(X(120),Y(1710)+4,'caprior 44×100 (2× scandura 22×100)',size=10.5,fill=MUT)
f.mats.append('cap')
f.piece(X(-200-T),Y(1666),X(T),X(1666-B0),'ram',dash='5 4',label=False)
f.text(X(-200-T/2),Y(1400),'perete lateral',size=10,fill=MUT,rot=-90)
f.dim(X(-200-T-34),Y(B0),X(-200-T-34),Y(1666),'1666 peste podea',vertical=True,size=11)
f.dim(X(FP+520+110),Y(B0),X(FP+520+110),Y(1600),'1600',vertical=True,size=11)
f.note(X(-200-T),Y(1666),'aceeasi scriere pe caprior ca la spate',dx=X(20),dy=X(150),anchor='start',fill=ACC2,size=10.5)
f.text(X(160),Y(B0-90),'SECTIUNE — coltul din fata, sus',size=11,fill=MUT)
figs['nod_sus_fata']=f.key().svg()


# ══════════════════════ E4 · peretele din fata — detalii ══════════════════════

# ── F1 · bara de sus, in plan: calca pe rama SI pe amandoi stalpii ──
f=Fig(); S=0.32; X=lambda mm: mm*S; Y=lambda mm: mm*S
BD  = 100                                  # bara vazuta de sus: latura de 100
BY  = -170                                 # bara, desenata deasupra planului
f.text(X(-FP),Y(BY-118),'PLAN — vazut de sus',size=11,fill=MUT,anchor='start')
f.piece(X(-FP-2),Y(BY),X(BARA_F),X(BD),'bara',stroke=ACC2,sw=2.4,label=False)
f.text(X(WALL_F/2),Y(BY+BD/2)+5,f'bara solida 100×60  —  taiata la {BARA_F}',size=12.5,fill=ACC2)
f.dim(X(-FP-2),Y(BY-58),X(-FP-2+BARA_F),Y(BY-58),f'{BARA_F}',size=13,fill=ACC2)
for px in (-FP, WALL_F):                   # cei doi stalpi din fata
    f.piece(X(px),Y(0),X(FP),X(FP),'st9',sw=2,label=False)
    f.text(X(px+FP/2),Y(FP/2)+4,'90×90',size=10,fill=INK)
    f.text(X(px+FP/2),Y(FP+92),'stalp EXISTENT',size=10,fill=ACC2,weight='700')
f.piece(X(0),Y(0),X(WALL_F),X(T),'ram',label=False)
f.text(X(WALL_F/2),Y(T/2)+4,f'rama peretelui — rigla {T}×{T}, taiata la {WALL_F}',size=11,fill=MUT)
f.dim(X(0),Y(FP+62),X(WALL_F),Y(FP+62),f'{WALL_F}  —  lumina intre stalpi',size=12)
f.line(X(-FP+FP/2),Y(BY+BD),X(-FP+FP/2),Y(0)); f.dot(X(-FP+FP/2),Y(BY+BD))
f.line(X(WALL_F+FP/2),Y(BY+BD),X(WALL_F+FP/2),Y(0)); f.dot(X(WALL_F+FP/2),Y(BY+BD))
f.text(X(WALL_F/2),Y(FP+210),'Calca integral pe amandoi stalpii — de aia e mai lunga decat peretele.',size=12.5,fill=ACC2)
f.text(X(WALL_F/2),Y(FP+330),'Rigla de 48 nu o inlocuieste.',size=11.5,fill=MUT)
figs['fata_bara']=f.key().svg()

# ── F2 · fereastra: prag si buiandrug intre jambe (stivuire ca la laterale) ──
f=Fig(); S=0.34; X=lambda mm: mm*S; Y=lambda mm: -mm*S
J0,J1 = FL_FER                                             # 161 → 731
f.text(X(J0-T-90),Y(1600+300),'ELEVATIE — zona ferestrei, din exterior',size=11,fill=MUT,anchor='start')
f.piece(X(J0-T-90),Y(T),X(J1-J0+2*T+180),X(T),'ram',label=False)          # talpa
f.piece(X(J0-T),Y(T+VF),X(T),X(VF),'ram',label=False)                     # jamba stanga
f.piece(X(J1),Y(T+VF),X(T),X(VF),'ram',label=False)                       # jamba dreapta
f.text(X(J0-T/2),Y(T+VF/2),f'jamba {VF}',size=10,fill=MUT,rot=-90)
f.text(X(J1+T/2),Y(T+VF/2),f'jamba {VF}',size=10,fill=MUT,rot=-90)
f.piece(X(J0-T-90),Y(1600+60),X(J1-J0+2*T+180),X(60),'bara',stroke=ACC2,sw=2,label=False)  # bara de sus
f.text(X((J0+J1)/2),Y(1600+28)+4,'bara 100×60',size=10.5,fill=ACC2)
f.piece(X(J0),Y(PRAG),X(J1-J0),X(T),'ram',stroke=ACC,sw=2,label=False)         # prag
f.text(X((J0+J1)/2),Y(PRAG-T/2)+4,'prag · rigla 46×46',size=9.5,fill=MUT)
f.piece(X(J0),Y(PRAG+FER_F+T),X(J1-J0),X(T),'ram',stroke=ACC,sw=2,label=False) # buiandrug
f.text(X((J0+J1)/2),Y(PRAG+FER_F+T/2)+4,'buiandrug · rigla 46×46',size=9.5,fill=MUT)
f.piece(X(J0),Y(PRAG+FER_F),X(J1-J0),X(FER_F),'pvc',stroke=ACC2,sw=2,dash='7 5',label=False)
f.text(X((J0+J1)/2),Y(PRAG+FER_F/2)+6,f'GOL {FER_F}×{FER_F}',size=13,fill=ACC2,weight='600')
f.text(X((J0+J1)/2),Y(PRAG+FER_F/2)+82,'aici intra fereastra PVC 56×56',size=10.5,fill=MUT)
f.dim(X(J0),Y(-130),X(J1),Y(-130),f'{FER_F} — intre jambe',size=12,fill=ACC)
f.dim(X(J0-T-150),Y(0),X(J0-T-150),Y(PRAG),f'prag {PRAG}',vertical=True,size=12,fill=ACC)
f.dim(X(J1+T+150),Y(PRAG),X(J1+T+150),Y(PRAG+FER_F),str(FER_F),vertical=True,size=12,fill=ACC2)
f.dim(X(J1+T+330),Y(0),X(J1+T+330),Y(1600),'1600',vertical=True,size=12)
f.text(X((J0+J1)/2),Y(-320),'Prag si buiandrug se pun INTRE jambe, nu peste ele.',size=12.5,fill=ACC)
f.text(X((J0+J1)/2),Y(-450),'Aceeasi metoda ca la geamurile laterale.',size=11,fill=MUT)
figs['fata_fereastra']=f.key().svg()

# ── F3 · prinderea stalpului din fata: 4 suruburi oblice, fara tije ──
f=Fig(); S=0.80; X=lambda mm: mm*S; Y=lambda mm: -mm*S
DECK, JOIST = 28, 200
JX0, JX1 = -430, 520                                        # cat se vede din grinda
f.text(X(JX0),Y(-JOIST-150),'SECTIUNE — piciorul stalpului din fata',size=11,fill=MUT,anchor='start')
f.piece(X(JX0),Y(0),X(JX1-JX0),X(JOIST),'gri',sw=1.6,label=False)          # grinda
f.text(X(JX0+110),Y(-JOIST*0.72)+4,'grinda podelei',size=10.5,fill=MUT,anchor='start')
f.piece(X(JX0),Y(DECK),X(JX1-JX0),X(DECK),'dus',sw=1.4,label=False)        # dusumea
f.text(X(JX0+90),Y(DECK/2)+4,'dusumea larice 28×145',size=9.5,fill=MUT,anchor='start')
PT = 470                                                                    # cat se vede din stalp
f.piece(X(0),Y(PT),X(FP),X(PT-DECK),'st9',sw=2.2,label=False)              # stalpul
f.text(X(FP/2),Y(400),'stalp 90×90',size=11,fill=ACC2,rot=-90)
for _a,_b in [(-6,FP*0.3),(FP*0.3,FP*0.62),(FP*0.62,FP+6)]:                # rupere de stalp
    f.line(X(_a),Y(PT+(9 if _a<FP*0.4 else -9)),X(_b),Y(PT+(-9 if _a<FP*0.4 else 9)),stroke=INK,sw=1.4)
TAN=0.30                                                                    # ~17° fata de verticala
LSUR, VSUR = 140, 134                                                       # surub 8x140: coboara 134, merge lateral 41
# coltarele, pe fata dinspre privitor — desenate in urma, ca sa nu para ca se ciocnesc de suruburi
for sgn in (-1,1):
    xv = -14 if sgn<0 else FP
    f.piece(X(xv),Y(DECK+150),X(14),X(150-DECK),'met',stroke=METAL2,sw=1.1,dash='4 3',label=False)
    xh = xv-62 if sgn<0 else FP
    f.piece(X(xh),Y(DECK+14),X(76),X(14),'met',stroke=METAL2,sw=1.1,dash='4 3',label=False)
f.note(X(-76),Y(DECK+90),'vinclu 90×60, pe fata dinspre tine',dx=X(-110),dy=X(170),anchor='end',fill=METAL2,size=11)
# suruburile, in planul taieturii: intra pe fata stalpului si coboara in grinda
for face,zs in ((0,(60,105)),(FP,(60,105))):
    sgn = 1 if face==0 else -1                                              # oblic spre INTERIORUL stalpului
    for z0 in zs:
        f.line(X(face),Y(z0),X(face+sgn*VSUR*TAN),Y(z0-VSUR),stroke=METAL2,sw=3.8)
SX,SZ = FP-VSUR*TAN*0.45, 105-VSUR*0.45
f.note(X(SX),Y(SZ),'4× surub dulgherie 8×140',dx=X(300-SX),dy=X(280-SZ),anchor='start',fill=METAL2,size=11.5)
f.text(X(FP+300),Y(190),'oblic la 15-20°, doua pe fiecare fata',size=10.5,fill=MUT,anchor='start')
f.text(X(FP+300),Y(100),'varful ramane in grinda, nu iese pe dedesubt',size=10.5,fill=MUT,anchor='start')
f.text(X(FP/2),Y(PT+150),'FARA tije M12. Nu cauta gauri de bulon — nu sunt.',size=12.5,fill=ACC2)
figs['fata_stalp']=f.key().svg()

# ── F4 · usa: talpa intreaga la ridicare, taiata dupa ──
f=Fig(); S=0.125; X=lambda mm: mm*S; Y=lambda mm: -mm*S
U0,U1 = FL_USA                                             # 938 → 1488
def _panou(ox, taiat, titlu, sub, culoare):
    if taiat:
        f.piece(X(ox),Y(T),X(U0),X(T),'ram',sw=1.6,label=False)
        f.piece(X(ox+U1),Y(T),X(WALL_F-U1),X(T),'ram',sw=1.6,label=False)
    else:
        f.piece(X(ox),Y(T),X(WALL_F),X(T),'ram',sw=1.6,label=False)
    for vx in (0, U0-T, U1, WALL_F-T):
        f.piece(X(ox+vx),Y(VF+T),X(T),X(VF),'ram',sw=1.4,label=False)
    f.piece(X(ox),Y(1600+60),X(WALL_F),X(60),'bara',stroke=ACC2,sw=1.8,label=False)
    if taiat:
        f.rect(X(ox+U0),Y(USA_LIBER),X(GOL_USA),X(USA_LIBER-T),fill='#fff',stroke=culoare,sw=2.6,dash='9 6')
        f.text(X(ox+(U0+U1)/2),Y(USA_LIBER*0.52),f'USA {GOL_USA}',size=13,fill=culoare,weight='600')
        f.dim(X(ox+WALL_F+210),Y(T),X(ox+WALL_F+210),Y(USA_LIBER),f'{USA_LIBER} liber',vertical=True,size=11.5,fill=culoare)
    else:
        for xx in (U0,U1):
            f.line(X(ox+xx),Y(T),X(ox+xx),Y(USA_LIBER),stroke=culoare,sw=1.6,dash='5 5')
        f.text(X(ox+(U0+U1)/2),Y(USA_LIBER*0.52),'aici VA fi usa',size=12,fill=culoare)
        f.text(X(ox+WALL_F/2),Y(-120),'talpa INTREAGA, pe toata lungimea',size=12,fill=ACC,weight='700')
    f.text(X(ox+WALL_F/2),Y(1600+430),titlu,size=14,fill=culoare,weight='700')
    f.text(X(ox+WALL_F/2),Y(1600+250),sub,size=11.5,fill=MUT)
_panou(0,    False,'1 · pana sus, talpa nu se taie','panoul ramane rigid la transport si la ridicare',ACC)
_panou(2650, True, '2 · dupa ridicare si echer',    'abia acum tai talpa, cu fierastraul sabie',       ACC2)
f.arrow(X(2140),Y(VF*0.55),X(2530),Y(VF*0.55),stroke=INK,sw=2.8)
f.text(X(2335),Y(-420),'Daca tai talpa mai devreme, peretele se indoaie exact cand atarna in maini.',size=12.5,fill=ACC2)
f.text(X(1250),Y(VF+T+560),'talpa · jambe · montanti: toate din rigla 46×46',size=11,fill=MUT)
figs['fata_usa']=f.key().svg()


json.dump(figs,open('figs_ghid.json','w'))
json.dump({'T':T,'VB':VB,'VF':VF,'VL':VL,'CUN_L':CUN_L,'CUN_R':CUN_R,'DIAG':DIAG,
           'WALL_B':WALL_B,'WALL_F':WALL_F,'DEP_L':DEP_L,'DEP_R':DEP_R,'BARA_F':BARA_F,
           'RIGLA':'46×46×3000','BARE_CH':{'e2':7,'e3':12,'e4':6},'BARE_TOT':27},
          open('cote.json','w'), ensure_ascii=False)
json.dump(MATS,open('mats.json','w'))
print('ok',{k:len(v) for k,v in figs.items()})
