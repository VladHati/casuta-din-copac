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

# ================= F1: SECTIUNE ANSAMBLU =================
f=Fig(2300,2100,padl=420,padr=120,padt=260,padb=300)
BY=2050
def yy(h): return BY-h
# punte
f.rect(-260,BY,2500,56,fill=WOOD2)
f.text(-400,BY+150,'puntea',size=FSS,fill=MUT,anchor='start')
# stalp 4m (spate) — perete spate pe linia 1100
f.rect(1100,yy(1700),90,1700+140,fill=WOOD2)
f.text(1145,yy(700),'stalp 4 m',size=FSS,fill=MUT,rot=-90)
# perete spate simplificat: talpa+cununa+montant
f.rect(1102,yy(1700),96,44); f.rect(1102,yy(44),96,44)
f.rect(1127,yy(1656),46,1612,fill=WOOD)
# dulap pe muchie deasupra (1700→1950)
f.rect(1122,yy(1950),46,250,fill=WOOD2)
# fata: stalp 90 pana la 1600 + cununa 44 → 1644
f.rect(0,yy(1600),90,1600,fill=WOOD2)
f.rect(-5,yy(1644),100,44)
f.text(126,yy(700),'stalp 90×90',size=FSS,fill=MUT,rot=-90)
# caprior: reazem fata (0,1644) → spate (1145,1950), prelungit 100 orizontal in ambele parti
x_f,y_f = 0,yy(1644); x_s,y_s = 1145,yy(1950)
slope=(y_f-y_s)/(x_f-x_s)
def pt(x): return (x, y_s + (x-x_s)*slope)
pF=pt(-100); pS=pt(1245)
ang=math.atan2(y_f-y_s,x_f-x_s); nx,ny=-math.sin(ang),math.cos(ang)
T=44
f.poly([pS,pF,(pF[0]-nx*T,pF[1]-ny*T),(pS[0]-nx*T,pS[1]-ny*T)],fill=WOOD)
f.poly([(pS[0]-nx*T,pS[1]-ny*T),(pF[0]-nx*T,pF[1]-ny*T),(pF[0]-nx*(T+26),pF[1]-ny*(T+26)),(pS[0]-nx*(T+26),pS[1]-ny*(T+26))],fill=ACC2)
m=pt(560)
f.text(m[0]-nx*160,m[1]-ny*160,'lemn inclinat 44×100 × 1342 · Onduline pe sipci',size=FSS,fill=INK,rot=-math.degrees(math.atan(0.266)))
f.text(m[0]+330,m[1]+250,'inclinare 15,6°',size=FSS,fill=MUT)
# muchia fata
f.line(pF[0],pF[1]+20,pF[0]-70,pF[1]+150,stroke=ACC2,sw=SWT)
f.text(pF[0]-80,pF[1]+210,'marginea la ~1614 — rotunjita, FARA jgheab',size=FSS,fill=ACC2,anchor='start')
# gard
f.rect(1560,yy(1800),36,1800+140,fill='#b8b2a6')
f.text(1578,yy(1050),'gard',size=FSS,fill=MUT,rot=-90)
# dims verticale (stanga, in pad)
f.dim(-190,BY,-190,yy(1600),'1600 stalp / usa',side='v')
f.dim(-320,BY,-320,yy(1644),'1644 sus, in fata',side='v')
# dims verticale dreapta-interior (intre perete si gard)
f.dim(1320,BY,1320,yy(1700),'1700 perete',side='v')
f.dim(1450,BY,1450,yy(1950),'1950 sus, in spate',side='v')
# dims orizontale
f.dim(0,BY+180,1100,BY+180,'1100 adancimea casei')
f.dim(1190,BY+180,1560,BY+180,'~300 gard',size=FSS)
# inset laminare — dreapta jos, sub gard? nu: dreapta sus e acoperis; pune sub dim orizontala, centrat dreapta
ix,iy=1700,yy(600)
f.text(ix+170,iy-150,'in loc de lemn 42×90:',size=FSS,fill=INK)
f.rect(ix,iy-60,340,60,fill=WOOD); f.rect(ix,iy,340,60,fill=WOOD)
f.text(ix+170,iy+140,'2× 22×100 = 44×100',size=FSS,fill=ACC,weight='bold')
f.text(ix+170,iy+200,'suruburi 4×40, in zigzag',size=FSS-8,fill=MUT)
figs['f1']=f.svg()

# ================= F2: SPATE =================
f=Fig(2000,1700,padl=340,padr=560,padt=140,padb=340)
H=1700; W=2000
f.rect(0,H-44,W,44); f.rect(0,0,W,44)
for x in [0,500,1000,1500,2000]:
    xx=min(max(x-23,0),W-46)
    f.rect(xx,44,46,H-88,fill=WOOD2 if x in (0,2000) else WOOD)
def brace(x0,y0,sx,sy,arm,label=None,lx=0,ly=0):
    f.line(x0+sx*arm,y0,x0,y0+sy*arm,stroke=ACC,sw=26)
    if label: f.text(x0+sx*arm+lx,y0+sy*arm/2+ly,label,size=FSS,fill=ACC)
brace(46,H-44,1,-1,300); brace(W-46,H-44,-1,-1,300)
brace(46,44,1,1,150);    brace(W-46,44,-1,1,150)
f.text(430,H-330,'proptele jos: brate 300 (424)',size=FSS,fill=ACC,anchor='start')
f.text(430,260,'proptele sus: brate 150 (212)',size=FSS,fill=ACC,anchor='start')
for i,x in enumerate([0,500,1000,1500]):
    f.dim(x,H+150,x+500,H+150,'500')
f.dim(0,H+280,W,H+280,'2000')
f.dim(-190,0,-190,H,'1700',side='v')
f.dim(2190,44,2190,H-44,'lemne verticale 1612 ×5',side='v',fill=ACC,toff=-30)
f.text(2400,H-500,'lemnul de jos si de sus: bara 44×100',size=FSS,fill=MUT,rot=-90)
figs['f2']=f.svg()

# ================= F3: LATERAL =================
f=Fig(1010,1998,padl=420,padr=340,padt=170,padb=330)
TL=1010; BYL=1950
def topy(x): return BYL-(1644+(1950-1644)*x/TL)
f.rect(0,BYL-44,TL,44)
f.poly([(0,topy(0)),(TL,topy(TL)),(TL,topy(TL)+48),(0,topy(0)+48)],fill=WOOD)
# verticale capete
f.rect(0,topy(0)+48,46,BYL-44-(topy(0)+48),fill=WOOD2)
f.rect(TL-46,topy(TL)+48,46,BYL-44-(topy(TL)+48),fill=WOOD2)
gx0,gx1=260,750
# dubluri gol
f.rect(gx0-46,topy(gx0-23)+48,46,BYL-44-(topy(gx0-23)+48))
f.rect(gx1,topy(gx1+23)+48,46,BYL-44-(topy(gx1+23)+48))
# prag (top 950) si buiandrug (bottom 1440)
f.rect(gx0,BYL-950,490,44)
f.rect(gx0,BYL-1484,490,44)
f.rect(gx0,BYL-1440,490,490,fill=GLASS,stroke=ACC,sw=SW)
f.text(gx0+245,BYL-1180,'GOL 490×490',size=FS,fill=ACC,weight='bold')
# mijloc taiat: jos sub prag, sus deasupra buiandrugului
f.rect(gx0+245-23,BYL-906,46,862,fill=WOOD)
f.rect(gx0+245-23,topy(gx0+245)+48,46,(BYL-1484)-(topy(gx0+245)+48),fill=WOOD)
# contrafise
f.line(46+150,BYL-44,46,BYL-44-150,stroke=ACC,sw=26)
f.line(TL-46-150,BYL-44,TL-46,BYL-44-150,stroke=ACC,sw=26)
f.line(46+150,topy(96)+96,46,topy(96)+96+150,stroke=ACC,sw=26)
f.line(TL-46-150,topy(TL-96)+96,TL-46,topy(TL-96)+96+150,stroke=ACC,sw=26)
f.text(30,topy(0)-150,'proptelele: toate scurte (212)',size=FSS,fill=ACC,anchor='start')
f.text(30,topy(0)-90,'— cele lungi nu incap langa gol',size=FSS-8,fill=ACC,anchor='start')
# dims
f.dim(0,BYL+150,gx0,BYL+150,'260',size=FSS)
f.dim(gx0,BYL+150,gx1,BYL+150,'490')
f.dim(gx1,BYL+150,TL,BYL+150,'260',size=FSS)
f.dim(0,BYL+280,TL,BYL+280,'lemnul de jos ~1010 (taiat pe loc)')
f.dim(-190,BYL,-190,BYL-950,'950 prag',side='v')
f.dim(-330,BYL,-330,BYL-1644,'1644 fata',side='v')
f.dim(1180,BYL,1180,BYL-1950,'1950 spate',side='v')
f.text(TL/2,topy(TL/2)-90,'lemnul de sus, inclinat',size=FSS,fill=MUT)
figs['f3']=f.svg()

# ================= F4: FATA =================
f=Fig(2000,1644,padl=420,padr=340,padt=150,padb=430)
BYF=1644
f.rect(0,BYF-44,2000,44); f.rect(0,0,2000,44)
f.rect(0,44,90,1600-44,fill=WOOD2); f.rect(1910,44,90,1600-44,fill=WOOD2)
for x0,x1 in [(205,250),(820,865),(980,1025),(1575,1620),(1742,1788)]:
    f.rect(x0,44,x1-x0,BYF-88)
# fereastra: gol vertical 950→1520
f.rect(250,BYF-950,570,44)      # prag, top la 950
f.rect(250,BYF-1564,570,44)     # buiandrug, bottom la 1520
f.rect(250,BYF-1520,570,570,fill=GLASS,stroke=ACC,sw=SW)
f.text(535,BYF-1230,'FEREASTRA 570×570',size=FS,fill=ACC,weight='bold')
# usa
f.rect(1025,44,550,BYF-88,fill='#f5f1e8',stroke=ACC2,sw=SW)
f.text(1300,820,'USA 550',size=FS,fill=ACC2,weight='bold')
f.text(1300,900,'liber 1600',size=FSS,fill=ACC2)
f.text(1300,BYF+95,'lemnul de jos se taie aici — LA FINAL',size=FSS,fill=ACC2)
# contrafise
f.line(1910-250,BYF-44,1910,BYF-44-250,stroke=ACC,sw=26)
f.text(1815,BYF-330,'250',size=FSS,fill=ACC)
f.line(90+150,44,90,44+150,stroke=ACC,sw=26)
f.line(1910-150,44,1910,44+150,stroke=ACC,sw=26)
f.text(0,BYF+400,'stanga-jos: fara proptea (nu incape) — e stalpul',size=FSS-8,fill=MUT,anchor='start')
# dims
f.dim(0,BYF+200,250,BYF+200,'250',size=FSS)
f.dim(250,BYF+200,820,BYF+200,'570')
f.dim(820,BYF+200,1025,BYF+200,'205',size=FSS)
f.dim(1025,BYF+200,1575,BYF+200,'550')
f.dim(1575,BYF+200,2000,BYF+200,'425',size=FSS)
f.dim(0,BYF+330,2000,BYF+330,'2000 intre fetele stalpilor')
f.dim(-190,BYF,-190,BYF-950,'950 prag',side='v')
f.dim(-330,BYF,-330,0,'1644',side='v')
f.dim(2180,BYF-44,2180,BYF-1600,'1600 stalp',side='v')
f.text(45,BYF-820,'3 suruburi in stalp',size=FSS,fill=MUT,rot=-90)
f.text(1955,BYF-820,'ancora anti-vant, 2 variante',size=FSS,fill=MUT,rot=-90)
figs['f4']=f.svg()

# ================= F5: ACOPERIS DE SUS =================
f=Fig(2200,1342,padl=470,padr=470,padt=260,padb=330)
W5,D5=2200,1342
f.rect(0,0,W5,D5,fill='#f5f1e8',stroke=LN,sw=SWT)
f.rect(0,0,W5,60,fill=WOOD2)
f.text(W5/2,-170,'SPATE / GARD',size=FSS,fill=MUT)
f.text(W5/2,-100,'scandura groasa 46×250 × 2200, sub linia asta (iese 10 cm lateral)',size=FSS-6,fill=MUT)
for cx in [100,600,1100,1600,2100]:
    f.rect(cx-50,0,100,D5)
for cx in [350,850,1350,1850]:
    f.rect(cx-22,70,44,110,fill=WOOD2)
    f.rect(cx-22,D5-250,44,110,fill=WOOD2)
f.text(350,300,'inchideri ~400',size=FSS,fill=MUT)
f.line(70,D5-40,W5-70,90,stroke=ACC,sw=30)
f.text(W5/2+180,D5/2+130,'sipca in diagonala, 2400',size=FSS,fill=ACC,rot=-30)
for sy in [140,540,940,1290]:
    f.rect(0,sy-23,W5,46,fill='none',stroke=ACC2,sw=4)
f.text(-30,540,'sipci 2200, la ≤450',size=FSS,fill=ACC2,anchor='end',rot=-90)
f.dim(100,D5+150,600,D5+150,'500'); f.dim(600,D5+150,1100,D5+150,'500')
f.dim(1100,D5+150,1600,D5+150,'500'); f.dim(1600,D5+150,2100,D5+150,'500')
f.dim(100,D5+280,2100,D5+280,'lemnele inclinate — in dreptul verticalelor din pereti')
f.dim(2330,0,2330,D5,'lemn inclinat 1342',side='v')
f.text(W5+330,D5/2,'TERASA in jos',size=FSS,fill=MUT,rot=-90)
f.text(0,D5+280+90,'',size=FSS)
f.text(-440,D5/2,'',size=FSS)
figs['f5']=f.svg()

json.dump(figs,open('figs.json','w'))
print('ok', {k:len(v) for k,v in figs.items()})
