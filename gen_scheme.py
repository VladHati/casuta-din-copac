#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Scheme la scara — v2: pad mare, etichete scurte, zero text in afara canvasului.
import math, json

INK="#1c1b18"; ACC="#14532d"; ACC2="#8a3016"; MUT="#6b675e"; LN="#cfc9bc"
WOOD="#e8dfcc"; WOOD2="#d9cdb2"; GLASS="#dce8ea"
FS=56; FSS=48; SW=6; SWT=3

def esc(s): return s.replace('&','&amp;').replace('<','&lt;')

class Fig:
    def __init__(self, w, h, padl=380, padr=380, padt=200, padb=380):
        self.w=w; self.h=h; self.pl=padl; self.pr=padr; self.pt=padt; self.pb=padb; self.el=[]
    def rect(self,x,y,w,h,fill=WOOD,stroke=INK,sw=SW,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def line(self,x1,y1,x2,y2,stroke=INK,sw=SWT,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{stroke}" stroke-width="{sw}"{d} stroke-linecap="round"/>')
    def poly(self,pts,fill=WOOD,stroke=INK,sw=SW):
        p=' '.join(f'{x:.0f},{y:.0f}' for x,y in pts)
        self.el.append(f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    def text(self,x,y,s,size=FS,fill=INK,anchor='middle',weight='normal',rot=None):
        r=f' transform="rotate({rot} {x:.0f} {y:.0f})"' if rot is not None else ''
        self.el.append(f'<text x="{x:.0f}" y="{y:.0f}" font-family="ui-monospace,Menlo,monospace" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{r}>{esc(s)}</text>')
    def dim(self,x1,y1,x2,y2,label,side='h',size=FS,fill=MUT,toff=-22):
        self.line(x1,y1,x2,y2,stroke=fill,sw=SWT)
        for (x,y) in [(x1,y1),(x2,y2)]:
            if side=='h': self.line(x,y-26,x,y+26,stroke=fill,sw=SWT)
            else: self.line(x-26,y,x+26,y,stroke=fill,sw=SWT)
        mx,my=(x1+x2)/2,(y1+y2)/2
        if side=='h': self.text(mx,my+toff,label,size=size,fill=fill)
        else: self.text(mx+toff,my,label,size=size,fill=fill,rot=-90)
    def svg(self):
        vw=self.w+self.pl+self.pr; vh=self.h+self.pt+self.pb
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-self.pl} {-self.pt} {vw} {vh}" style="width:100%;height:auto;display:block">'
                + '\n'.join(self.el) + '</svg>')

figs={}

# ================= GEOMETRIE REALA — masurata 20.08.2026, confirmata de Vlad =================
# Lumina intre fetele stalpilor: spate 1995 / fata 1975 ; adancime 1580 (S1-S3) si 1570 (S2-S4).
# Stalpi verificati cu ruleta: spate 100x100, fata 90x90. Inaltimi peste podea: 1700 / 1600.
# Reazeme acoperis: spate 1700+200 (dulap pe muchie) = 1900 ; fata 1600+60 (bara 100x60) = 1660.
WB, WF   = 1995, 1975          # lumina intre stalpi, spate / fata
WALL_B   = WB - 5              # talpa+cununa perete spate  = 1990
WALL_F   = WF - 5              # talpa perete fata          = 1970
DEP      = 1575                # adancime medie (1580 / 1570 — fiecare lateral se taie pe cota lui)
BP, FP   = 100, 90             # sectiuni stalpi
REZ_B, REZ_F = 1900, 1660
SPAN     = DEP + BP/2 + FP/2   # 1670 — intre reazeme, centru la centru
SL       = math.atan2(REZ_B-REZ_F, SPAN)   # 8,18 grade
RAFT     = round((SPAN+200)/math.cos(SL))  # 1889, cu streasini 100+100
EDGE     = round(REZ_F - 100*math.tan(SL)) # 1646, muchia din fata peste podea
PAS      = WALL_B/4            # 497,5 intre capriori
BLOC     = round(PAS-44)       # 454, inchiderile dintre capriori
TOPBAR   = WF + 2*FP           # 2155, bara 100x60 calca pe ambii stalpi
LAT_F    = round(REZ_F + (FP/2)*math.tan(SL))   # 1666 — inaltimea lateralului la capatul din fata
LAT_B    = round(REZ_B - (BP/2)*math.tan(SL))   # 1893 — la capatul din spate

# ================= F1: SECTIUNE ANSAMBLU =================
f=Fig(2400,2100,padl=420,padr=200,padt=260,padb=340)
BY=2050
def yy(h): return BY-h
f.rect(-260,BY,2700,56,fill=WOOD2)
f.text(-400,BY+150,'puntea',size=FSS,fill=MUT,anchor='start')
# stalpul de 4 m (spate) — axa la SPAN, sectiune BP
f.rect(SPAN-BP/2,yy(1700),BP,1700+140,fill=WOOD2)
f.text(SPAN,yy(700),'stalp 4 m',size=FSS,fill=MUT,rot=-90)
# perete spate: talpa + cununa + un montant
f.rect(SPAN-BP/2+2,yy(1700),BP-4,44); f.rect(SPAN-BP/2+2,yy(44),BP-4,44)
f.rect(SPAN-23,yy(1656),46,1612,fill=WOOD)
# dulap 200x50 pe muchie, 1700 -> 1900
f.rect(SPAN-25,yy(1900),50,200,fill=WOOD2)
# fata: stalp 90x90 pana la 1600 + bara solida 100x60 -> 1660
f.rect(-FP/2,yy(1600),FP,1600,fill=WOOD2)
f.rect(-50,yy(1660),100,60)
f.text(FP,yy(700),'stalp 90×90',size=FSS,fill=MUT,rot=-90)
# capriorul: reazem fata (0,1660) -> reazem spate (SPAN,1900), prelungit 100 orizontal in ambele parti
x_f,y_f = 0,yy(REZ_F); x_s,y_s = SPAN,yy(REZ_B)
slope=(y_f-y_s)/(x_f-x_s)
def pt(x): return (x, y_s + (x-x_s)*slope)
pF=pt(-100); pS=pt(SPAN+100)
ang=math.atan2(y_f-y_s,x_f-x_s); nx,ny=-math.sin(ang),math.cos(ang)
T=44
f.poly([pS,pF,(pF[0]-nx*T,pF[1]-ny*T),(pS[0]-nx*T,pS[1]-ny*T)],fill=WOOD)
# stratul de deasupra: OSB + Onduline (panta sub 10° -> astereala continua)
f.poly([(pS[0]-nx*T,pS[1]-ny*T),(pF[0]-nx*T,pF[1]-ny*T),(pF[0]-nx*(T+30),pF[1]-ny*(T+30)),(pS[0]-nx*(T+30),pS[1]-ny*(T+30))],fill=ACC2)
m=pt(SPAN*0.42)
f.text(m[0]-nx*170,m[1]-ny*170,f'lemn inclinat 44×100 × {RAFT} · OSB 12 + Onduline',size=FSS,fill=INK,rot=-math.degrees(SL))
f.text(m[0]+430,m[1]+270,f'inclinare {math.degrees(SL):.1f}°'.replace('.',','),size=FSS,fill=MUT)
# muchia din fata
f.line(pF[0],pF[1]+20,pF[0]-70,pF[1]+150,stroke=ACC2,sw=SWT)
f.text(pF[0]-80,pF[1]+300,f'marginea la ~{EDGE} — rotunjita, FARA jgheab',size=FSS,fill=ACC2,anchor='start')
# gard
f.rect(SPAN+430,yy(1800),36,1800+140,fill='#b8b2a6')
f.text(SPAN+448,yy(1050),'gard',size=FSS,fill=MUT,rot=-90)
# cote verticale
f.dim(-190,BY,-190,yy(1600),'1600 stalp / usa',side='v')
f.dim(-320,BY,-320,yy(1660),'1660 sus, in fata',side='v')
f.dim(SPAN+200,BY,SPAN+200,yy(1700),'1700 perete',side='v')
f.dim(SPAN+330,BY,SPAN+330,yy(1900),'1900 sus, in spate',side='v')
# cote orizontale
f.dim(FP/2,BY+180,SPAN-BP/2,BY+180,f'{DEP} lumina intre stalpi (masurat)')
f.dim(0,BY+310,SPAN,BY+310,f'{round(SPAN)} intre reazeme')
f.dim(SPAN+BP/2,BY+180,SPAN+430,BY+180,'~300 gard',size=FSS)
# inset laminare
ix,iy=420,yy(760)
f.text(ix+170,iy-150,'in loc de lemn 42×90:',size=FSS,fill=INK)
f.rect(ix,iy-60,340,60,fill=WOOD); f.rect(ix,iy,340,60,fill=WOOD)
f.text(ix+170,iy+140,'2× 22×100 = 44×100',size=FSS,fill=ACC,weight='bold')
f.text(ix+170,iy+200,'suruburi 4×40, in zigzag',size=FSS-8,fill=MUT)
figs['f1']=f.svg()

# ================= F2: SPATE =================
f=Fig(WALL_B,1700,padl=340,padr=620,padt=140,padb=340)
H=1700; W=WALL_B
f.rect(0,H-44,W,44); f.rect(0,0,W,44)
XS=[round(i*PAS) for i in range(5)]
for x in XS:
    xx=min(max(x-23,0),W-46)
    f.rect(xx,44,46,H-88,fill=WOOD2 if x in (XS[0],XS[-1]) else WOOD)
def brace(x0,y0,sx,sy,arm,label=None,lx=0,ly=0):
    f.line(x0+sx*arm,y0,x0,y0+sy*arm,stroke=ACC,sw=26)
    if label: f.text(x0+sx*arm+lx,y0+sy*arm/2+ly,label,size=FSS,fill=ACC)
brace(46,H-44,1,-1,300); brace(W-46,H-44,-1,-1,300)
brace(46,44,1,1,150);    brace(W-46,44,-1,1,150)
f.text(430,H-330,'proptele jos: brate 300 (424)',size=FSS,fill=ACC,anchor='start')
f.text(430,260,'proptele sus: brate 150 (212)',size=FSS,fill=ACC,anchor='start')
for i in range(4):
    f.dim(XS[i],H+150,XS[i+1],H+150,str(XS[i+1]-XS[i]))
f.dim(0,H+280,W,H+280,f'{W} — taiat pe M3 real ({WB}) minus 5')
f.dim(-190,0,-190,H,'1700',side='v')
f.dim(W+190,44,W+190,H-44,'lemne verticale 1612 ×5',side='v',fill=ACC,toff=-30)
f.text(W+420,H-500,'lemnul de jos si de sus: bara 44×100',size=FSS,fill=MUT,rot=-90)
figs['f2']=f.svg()

# ================= F3: LATERAL =================
f=Fig(DEP,LAT_B,padl=430,padr=380,padt=250,padb=520)
TL=DEP; BYL=LAT_B
def topy(x): return BYL-(LAT_F+(LAT_B-LAT_F)*x/TL)
f.rect(0,BYL-44,TL,44)
f.poly([(0,topy(0)),(TL,topy(TL)),(TL,topy(TL)+48),(0,topy(0)+48)],fill=WOOD)
# 4 verticale: capete + doua care fac si jambele golului
VX=[0,497,1033,TL-46]
for i,x in enumerate(VX):
    f.rect(x,topy(x+23)+48,46,BYL-44-(topy(x+23)+48),fill=WOOD2 if i in (0,3) else WOOD)
gx0,gx1=543,1033
f.rect(gx0,BYL-950,gx1-gx0,44)          # prag, fata de sus la 950
f.rect(gx0,BYL-1484,gx1-gx0,44)         # buiandrug
f.rect(gx0,BYL-1440,490,490,fill=GLASS,stroke=ACC,sw=SW)
f.text(gx0+245,BYL-1180,'GOL 490×490',size=FS,fill=ACC,weight='bold')
# contrafise — toate scurte
f.line(46+150,BYL-44,46,BYL-44-150,stroke=ACC,sw=26)
f.line(TL-46-150,BYL-44,TL-46,BYL-44-150,stroke=ACC,sw=26)
f.line(46+150,topy(96)+96,46,topy(96)+96+150,stroke=ACC,sw=26)
f.line(TL-46-150,topy(TL-96)+96,TL-46,topy(TL-96)+96+150,stroke=ACC,sw=26)
f.text(30,topy(0)-190,'proptelele: toate scurte (212)',size=FSS,fill=ACC,anchor='start')
f.text(30,topy(0)-130,'— cele lungi nu incap langa gol',size=FSS-8,fill=ACC,anchor='start')
# cote
f.dim(0,BYL+150,gx0,BYL+150,str(gx0),size=FSS)
f.dim(gx0,BYL+150,gx1,BYL+150,'490')
f.dim(gx1,BYL+150,TL,BYL+150,str(TL-gx1),size=FSS)
f.dim(0,BYL+280,TL,BYL+280,f'talpa {DEP} — se taie pe loc (1580 pe o parte, 1570 pe cealalta)')
f.dim(-200,BYL,-200,BYL-950,'950 prag',side='v')
f.dim(-340,BYL,-340,BYL-LAT_F,f'{LAT_F} fata',side='v')
f.dim(TL+200,BYL,TL+200,0,f'{LAT_B} spate',side='v')
f.text(TL/2,topy(TL/2)-90,'lemnul de sus, inclinat',size=FSS,fill=MUT)
f.text(TL/2,BYL+420,'verticale, dinspre fata spre spate: 1581 · 1653 · 1730 · 1802',size=FSS,fill=ACC)
figs['f3']=f.svg()

# ================= F4: FATA =================
f=Fig(WALL_F,1660,padl=470,padr=420,padt=170,padb=620)
BYF=1660; WF4=WALL_F
f.rect(0,BYF-44,WF4,44)                       # talpa, intre stalpi
f.rect(-FP,0,TOPBAR,60)                       # bara 100x60, calca pe ambii stalpi
f.rect(-FP,60,FP,1600,fill=WOOD2); f.rect(WF4,60,FP,1600,fill=WOOD2)   # stalpii, de la podea la 1600
# montanti: jambe fereastra, jambe usa, un montant de camp
for x0 in [115,731,892,1488,1650]:
    f.rect(x0,60,46,BYF-104)
f.rect(161,BYF-950,570,44)      # prag fereastra, fata de sus la 950
f.rect(161,BYF-1564,570,44)     # buiandrug
f.rect(161,BYF-1520,570,570,fill=GLASS,stroke=ACC,sw=SW)
f.text(446,BYF-1230,'GOL 570×570',size=FS,fill=ACC,weight='bold')
f.text(446,BYF-1160,'(fereastra PVC 56×56)',size=FSS-10,fill=ACC)
f.text(WF4/2,-80,'lemnul de sus: bara 100×60 (a ta, nu se lamineaza) — 2155, calca pe ambii stalpi',size=FSS-10,fill=ACC,anchor='middle')
f.rect(938,44,550,BYF-88,fill='#f5f1e8',stroke=ACC2,sw=SW)
f.text(1213,820,'USA 550',size=FS,fill=ACC2,weight='bold')
f.text(1213,900,'liber 1600',size=FSS,fill=ACC2)
f.text(1213,BYF+95,'lemnul de jos se taie aici — LA FINAL',size=FSS,fill=ACC2)
# contrafise: sus 2 scurte, jos-dreapta una lunga (in golul de 274, fara sa atinga montantul de camp)
f.line(WF4-250,BYF-44,WF4,BYF-44-250,stroke=ACC,sw=26)
f.text(WF4-160,BYF-330,'250',size=FSS,fill=ACC)
f.line(150,44,0,44+150,stroke=ACC,sw=26)
f.line(WF4-150,44,WF4,44+150,stroke=ACC,sw=26)
f.text(0,BYF+580,'stanga-jos: fara proptea (nu incape) — coltul e chiar stalpul',size=FSS-8,fill=MUT,anchor='start')
# cote
f.dim(0,BYF+200,161,BYF+200,'161',size=FSS)
f.dim(161,BYF+200,731,BYF+200,'570')
f.dim(731,BYF+200,938,BYF+200,'207',size=FSS)
f.dim(938,BYF+200,1488,BYF+200,'550')
f.dim(1488,BYF+200,WF4,BYF+200,str(WF4-1488),size=FSS)
f.dim(0,BYF+330,WF4,BYF+330,f'{WF4} — lumina intre stalpi ({WF}) minus 5')
f.dim(-FP,BYF+460,-FP+TOPBAR,BYF+460,f'{TOPBAR} peste stalpi — bara de sus')
f.dim(-200,BYF,-200,BYF-950,'950 prag',side='v')
f.dim(-340,BYF,-340,0,'1660',side='v')
f.dim(WF4+FP+190,BYF,WF4+FP+190,BYF-1600,'1600 stalp',side='v')
f.text(-45,BYF-820,'rama in stalp: 3× surub 6×120',size=FSS-8,fill=MUT,rot=-90)
f.text(WF4+45,BYF-820,'2 vincluri 90×65 (anti-ridicare)',size=FSS-8,fill=MUT,rot=-90)
figs['f4']=f.svg()

# ================= F5: ACOPERIS DE SUS =================
W5,D5=2200,RAFT
f=Fig(W5,D5,padl=560,padr=470,padt=280,padb=560)
f.rect(0,0,W5,D5,fill='#f5f1e8',stroke=LN,sw=SWT)
f.rect(0,0,W5,60,fill=WOOD2)
f.text(W5/2,-190,'SPATE / GARD',size=FSS,fill=MUT)
f.text(W5/2,-120,'scandura groasa 200×50 × 2200, sub linia asta (iese ~10 cm lateral)',size=FSS-6,fill=MUT)
# capriorii: 44 lati (nu 100 — bugul vechi facea inchiderile sa iasa 400 in loc de 454)
CX=[round(105+i*PAS) for i in range(5)]
for cx in CX:
    f.rect(cx-22,0,44,D5)
for a,b in zip(CX,CX[1:]):
    mid=(a+b)/2
    f.rect(mid-((b-a)-44)/2,80,(b-a)-44,110,fill=WOOD2)
    f.rect(mid-((b-a)-44)/2,D5-260,(b-a)-44,110,fill=WOOD2)
f.text((CX[0]+CX[1])/2,320,f'inchideri {BLOC}',size=FSS,fill=MUT)
# astereala continua: 2 placi OSB
f.line(0,1250,W5,1250,stroke=ACC,sw=8,dash='30,20')
f.text(-70,D5/2,'OSB3 12 mm — astereala continua',size=FSS,fill=ACC,anchor='middle',rot=-90)
f.text(W5-40,1250-40,f'imbinarea placilor: 2200×1250 + 2200×{D5-1250}',size=FSS-10,fill=ACC,anchor='end')
f.text(W5/2,D5+430,'FARA sipci si FARA sipca diagonala — placa face bracajul singura',size=FSS,fill=ACC2)
f.text(W5/2,D5+500,'panta sub 10° → Onduline cere astereala continua (spec producator)',size=FSS-8,fill=MUT)
for i in range(4):
    f.dim(CX[i],D5+150,CX[i+1],D5+150,str(CX[i+1]-CX[i]))
f.dim(CX[0],D5+280,CX[-1],D5+280,'lemnele inclinate — in dreptul verticalelor din pereti')
f.dim(W5+330,0,W5+330,D5,f'lemn inclinat {D5}',side='v')
f.text(W5+430,D5/2,'TERASA in jos',size=FSS,fill=MUT,rot=-90)
figs['f5']=f.svg()

# ================= F6: DETALIU — ANCORAREA STALPULUI DIN FATA (suruburi oblice) =================
def badge(fig,x,y,n):
    fig.el.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="24" fill="{ACC}" stroke="{INK}" stroke-width="3"/>')
    fig.el.append(f'<text x="{x:.0f}" y="{y+9:.0f}" font-family="ui-monospace,Menlo,monospace" font-size="28" fill="#ffffff" text-anchor="middle" font-weight="bold">{n}</text>')

f=Fig(620,590,padl=110,padr=110,padt=70,padb=40)

f.text(140,-25,'…continua pana la 1600',size=FSS-14,fill=MUT)
f.rect(40,0,200,380,fill=WOOD2)                            # stalp
f.rect(260,416,340,130,fill=WOOD2,stroke=LN)                # grinda
f.rect(-60,380,680,36,fill=WOOD)                            # scandura podelei
f.rect(240,280,24,100,fill='#b8b2a6',stroke=INK,sw=4)        # coltar - latura verticala
f.rect(240,368,120,12,fill='#b8b2a6',stroke=INK,sw=4)        # coltar - latura orizontala
for ty in (295,320,345):
    f.line(216,ty,240,ty,stroke=INK,sw=5)                    # suruburi coltar-stalp
f.line(420,380,465,480,stroke='#8a8578',sw=14)               # surub oblic 1
f.line(465,380,510,480,stroke='#8a8578',sw=14)               # surub oblic 2
f.line(-60,416,620,416,stroke=LN,sw=3,dash='10,8')           # linia dedesubtul puntii

badge(f,140,100,'1')
badge(f,300,374,'2')
badge(f,490,430,'3')
badge(f,-30,398,'4')
badge(f,560,500,'5')

figs['f6']=f.svg()

# ================= F7 v3: DETALIU — GOLUL DE PODEA LA COLTUL DIN SPATE (corectat 19.08: sprijin real, numerotare unificata A+B) =================
# Numerotare unica pe ambele panouri (acelasi element = acelasi numar in A si in B):
# 1 stalp · 2 dusumea existenta · 3 blocaj nou · 4 coltar tip etajera · 5 suruburi sistrate
# 6 grinda veche (capat) · 7 scandura cosmetica noua · 8 perete spate · 9 aer, fara sprijin
XB = 760  # offset panoul B (sectiune) fata de panoul A (plan)
f=Fig(XB+400, 460, padl=90, padr=110, padt=130, padb=60)

# ---------- PANOUL A: PLAN (vedere de sus) ----------
f.text(240,-90,'A · PLAN, vedere de sus',size=FSS-16,fill=INK,weight='bold')
f.text(240,-56,'(schema, nu la scara)',size=FSS-18,fill=MUT)

f.rect(170,0,310,60,fill=LN)                                  # 8 perete spate, deja imbracat — context
f.rect(0,170,60,230,fill=LN)                                  # perete lateral — context (acelasi perete)
f.rect(60,60,110,110,fill=WOOD2)                               # 1 stalpul de colt
f.poly([(270,60),(480,60),(480,400),(60,400),(60,270),(270,270)],fill=WOOD)   # 2 podeaua existenta, buna
f.poly([(170,60),(270,60),(270,270),(60,270),(60,170),(170,170)],fill=WOOD,stroke=ACC2,sw=SW)  # 3 blocaj nou — o singura piesa in L
f.rect(145,130,60,35,fill='#b8b2a6',stroke=INK,sw=4)            # 4 coltar la stalp (vezi panoul B pt orientare reala)
f.line(150,140,200,140,stroke=INK,sw=5)
f.line(150,148,200,148,stroke=INK,sw=5)
f.line(150,156,200,156,stroke=INK,sw=5)
f.line(260,160,282,160,stroke=INK,sw=5)                         # 5 suruburi blocaj -> grinda veche (sistrat)
f.line(260,180,282,180,stroke=INK,sw=5)
f.dim(170,305,270,305,'~100',size=FSS-14,fill=MUT,toff=-22)     # gol masurat

badge(f,90,110,'1')
badge(f,340,330,'2')
badge(f,160,225,'3')
badge(f,192,148,'4')
badge(f,300,210,'5')
badge(f,400,30,'8')

# ---------- PANOUL B: SECTIUNE VERTICALA prin blocaj ----------
bx = lambda v: XB+v
f.text(bx(200),-90,'B · SECTIUNE VERTICALA',size=FSS-16,fill=INK,weight='bold')
f.text(bx(200),-56,'ce tine blocajul, de fapt',size=FSS-18,fill=MUT)

f.rect(bx(20),20,110,300,fill=WOOD2)                             # 1 stalp, taiat — continua in pamant
f.rect(bx(290),140,110,90,fill=WOOD,stroke=LN)                   # 6 capatul grinzii vechi, existent
f.rect(bx(130),140,160,110,fill=WOOD2,stroke=ACC2,sw=SW)         # 3 blocaj nou — structural
f.rect(bx(90),105,300,30,fill=WOOD,stroke=ACC2,sw=SWT)           # 7 scandura cosmetica noua, deasupra
f.rect(bx(103),190,30,90,fill='#b8b2a6',stroke=INK,sw=4)         # 4 coltar — latura verticala, in stalp
f.rect(bx(130),250,80,20,fill='#b8b2a6',stroke=INK,sw=4)         # 4 coltar — latura orizontala, POLITA sub blocaj
for ty in (205,225,245):
    f.line(bx(108),ty,bx(133),ty,stroke=INK,sw=4)                 # suruburi coltar -> stalp
for tx in (150,170,190):
    f.line(bx(tx),243,bx(tx),257,stroke=INK,sw=4)                  # suruburi blocaj -> polita coltarului
f.line(bx(280),160,bx(300),160,stroke=INK,sw=5)                   # 5 suruburi blocaj -> grinda veche (sistrat)
f.line(bx(280),190,bx(300),190,stroke=INK,sw=5)
for ax,ay in [(150,330),(180,350),(210,330),(240,350)]:
    f.line(bx(ax),ay,bx(ax)+22,ay+22,stroke=LN,sw=3,dash='6,6')   # 9 aer — hatch
f.text(bx(75),355,'stalp -> pamant',size=FSS-20,fill=MUT)
f.text(bx(210),430,'aer, fara sprijin',size=FSS-16,fill=MUT)

badge(f,bx(75),160,'1')
badge(f,bx(118),262,'4')
badge(f,bx(210),178,'3')
badge(f,bx(345),178,'6')
badge(f,bx(115),120,'7')
badge(f,bx(290),225,'5')
badge(f,bx(210),390,'9')

figs['f7']=f.svg()

json.dump(figs,open('figs.json','w'))
print('ok', {k:len(v) for k,v in figs.items()})
