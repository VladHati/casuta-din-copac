#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SCHEME 2D — casa de sus. Vederi ortogonale, toate derivate dintr-un singur model numeric.
Fiecare cota din desen e calculata, nu scrisa de mana. La final se tipareste un tabel de auto-verificare."""
import math, json

INK="#1c1b18"; ACC="#14532d"; ACC2="#8a3016"; MUT="#6b675e"; DIM="#8a857a"; LN="#d6d0c4"
W1="#e8dfcc"; W2="#d9cdb2"; W3="#c4b696"; W4="#b1a281"
METAL="#9aa1ad"; METAL2="#6f7683"; GLASS="#d7e6e8"; GROUND="#c8c2b4"; HATCH="#efeadf"

# ─────────────────────────── MODEL ───────────────────────────
M = {}
M['WB_clear'] = 1995          # lumina intre stalpii din spate (masurat)
M['WF_clear'] = 1975          # lumina intre stalpii din fata (masurat)
M['DEP_L']    = 1580          # adancime, latura S1-S3 (masurat)
M['DEP_R']    = 1570          # adancime, latura S2-S4 (masurat)
M['BP']       = 100           # sectiune stalp spate
M['FP']       = 90            # sectiune stalp fata
M['H_B']      = 1700          # stalpi spate peste podea
M['H_F']      = 1600          # stalpi fata peste podea
M['DULAP']    = 200           # scandura groasa pe muchie
M['BARA_F']   = 60            # bara 100x60, latura in sus
M['T']        = 48            # grosimea talpii / cununii (rigla 48x48)
M['D']        = 48            # adancimea ramei (rigla 48x48, nu mai e fasie de 100)
M['STREASINA']= 100

d = M
d['WALL_B'] = d['WB_clear']-5
d['WALL_F'] = d['WF_clear']-5
d['DEP']    = (d['DEP_L']+d['DEP_R'])/2
d['REZ_B']  = d['H_B']+d['DULAP']
d['REZ_F']  = d['H_F']+d['BARA_F']
d['SPAN']   = d['DEP']+d['BP']/2+d['FP']/2
d['DROP']   = d['REZ_B']-d['REZ_F']
d['SL']     = math.atan2(d['DROP'], d['SPAN'])
d['SLdeg']  = math.degrees(d['SL'])
d['RAFT']   = (d['SPAN']+2*d['STREASINA'])/math.cos(d['SL'])
d['EDGE']   = d['REZ_F']-d['STREASINA']*math.tan(d['SL'])
d['PAS']    = d['WALL_B']/4
d['BLOC']   = d['PAS']-44          # inchideri intre capriori (44 lati), nu grosimea ramei
d['VB']     = d['H_B']-2*d['T']
d['VF']     = d['H_F']-d['T']
d['LATF']   = d['REZ_F']+(d['FP']/2)*math.tan(d['SL'])
d['LATB']   = d['REZ_B']-(d['BP']/2)*math.tan(d['SL'])
d['TOPBAR'] = d['WF_clear']+2*d['FP']
d['GOL_USA'],d['USA_LIBER'] = 550,1600
d['GOL_GEAM'],d['PRAG'] = 490,950
d['GOL_FER'] = 570
# verticalele laterale sunt cote VERBATIM, blocate 20.08: vechile (laminat 44)
# 1581/1653/1730/1802 minus 8 (rama trece pe rigla 48: -4 jos -4 sus). Nu se recalculeaza.
d['VLAT_OLD'] = [1581, 1653, 1730, 1802]
d['VLAT']     = [v-8 for v in d['VLAT_OLD']]        # 1573 · 1645 · 1722 · 1794
assert d['VLAT'] == [1573,1645,1722,1794], d['VLAT']

def vlat(x, L):
    """inaltimea peretelui lateral la distanta x de capatul din fata"""
    return d['LATF'] + (d['LATB']-d['LATF'])*x/L

def esc(s): return s.replace('&','&amp;').replace('<','&lt;')

# ─────────────────────────── DESEN ───────────────────────────
class D:
    def __init__(self, scale, fs=13):
        self.s=scale; self.el=[]; self.fs=fs; self.bb=[1e9,1e9,-1e9,-1e9]
    def X(self,mm): return mm*self.s
    def Y(self,mm): return -mm*self.s
    def _t(self,x,y):
        b=self.bb; b[0]=min(b[0],x); b[1]=min(b[1],y); b[2]=max(b[2],x); b[3]=max(b[3],y)
    # --- primitive in mm ---
    def bar(self,x,y,w,h,fill=W1,stroke=INK,sw=1.5,dash=None):
        X,Y=self.X(x),self.Y(y+h); W,H=self.X(w),self.X(h)
        da=f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<rect x="{X:.1f}" y="{Y:.1f}" width="{W:.1f}" height="{H:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}/>')
        self._t(X,Y); self._t(X+W,Y+H)
    def ln(self,x1,y1,x2,y2,stroke=INK,sw=1.3,dash=None):
        X1,Y1,X2,Y2=self.X(x1),self.Y(y1),self.X(x2),self.Y(y2)
        da=f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{X2:.1f}" y2="{Y2:.1f}" stroke="{stroke}" stroke-width="{sw}"{da} stroke-linecap="round"/>')
        self._t(X1,Y1); self._t(X2,Y2)
    def poly(self,pts,fill=W1,stroke=INK,sw=1.5,dash=None):
        P=[(self.X(a),self.Y(b)) for a,b in pts]
        s=' '.join(f'{a:.1f},{b:.1f}' for a,b in P)
        da=f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<polygon points="{s}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da} stroke-linejoin="round"/>')
        [self._t(a,b) for a,b in P]
    # --- adnotari in px ---
    def tx(self,x,y,s,size=None,fill=INK,anchor='middle',weight='400',rot=None,mono=True,px=False):
        size=size or self.fs
        X,Y=(x,y) if px else (self.X(x),self.Y(y))
        fam='ui-monospace,Menlo,monospace' if mono else 'system-ui,Helvetica,sans-serif'
        r=f' transform="rotate({rot} {X:.1f} {Y:.1f})"' if rot is not None else ''
        self.el.append(f'<text x="{X:.1f}" y="{Y:.1f}" font-family="{fam}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{r}>{esc(s)}</text>')
        w=len(s)*size*0.58; dx={'middle':w/2,'start':0,'end':w}[anchor]
        self._t(X-dx,Y-size); self._t(X-dx+w,Y+size*0.4)
    def dimh(self,x1,x2,y,label=None,off=22,fill=DIM,size=None):
        """cota orizontala; y = cota in mm la care se traseaza, off = px in jos"""
        Y=self.Y(y)+off; X1,X2=self.X(x1),self.X(x2)
        self.el.append(f'<line x1="{X1:.1f}" y1="{Y:.1f}" x2="{X2:.1f}" y2="{Y:.1f}" stroke="{fill}" stroke-width="1"/>')
        for X in (X1,X2):
            self.el.append(f'<line x1="{X:.1f}" y1="{Y-5:.1f}" x2="{X:.1f}" y2="{Y+5:.1f}" stroke="{fill}" stroke-width="1"/>')
        self._t(X1,Y-6); self._t(X2,Y+6)
        self.tx((X1+X2)/2,Y-7,label or f'{round(x2-x1)}',size=size or self.fs-1,fill=fill,px=True)
    def dimv(self,y1,y2,x,label=None,off=-22,fill=DIM,size=None):
        X=self.X(x)+off; Y1,Y2=self.Y(y1),self.Y(y2)
        self.el.append(f'<line x1="{X:.1f}" y1="{Y1:.1f}" x2="{X:.1f}" y2="{Y2:.1f}" stroke="{fill}" stroke-width="1"/>')
        for Y in (Y1,Y2):
            self.el.append(f'<line x1="{X-5:.1f}" y1="{Y:.1f}" x2="{X+5:.1f}" y2="{Y:.1f}" stroke="{fill}" stroke-width="1"/>')
        self._t(X-6,Y1); self._t(X+6,Y2)
        self.tx(X-6,(Y1+Y2)/2,label or f'{round(abs(y2-y1))}',size=size or self.fs-1,fill=fill,rot=-90,px=True)
    def note(self,x,y,s,dx=60,dy=-40,fill=MUT,anchor='start',size=None):
        X,Y=self.X(x),self.Y(y)
        self.el.append(f'<line x1="{X:.1f}" y1="{Y:.1f}" x2="{X+dx:.1f}" y2="{Y+dy:.1f}" stroke="{fill}" stroke-width="1"/>')
        self.el.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="2.6" fill="{fill}"/>')
        self.tx(X+dx+(5 if anchor=='start' else -5),Y+dy-3,s,fill=fill,anchor=anchor,size=size or self.fs-1,px=True)
    def svg(self,pad=30):
        x0,y0,x1,y1=self.bb
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0-pad:.0f} {y0-pad:.0f} {x1-x0+2*pad:.0f} {y1-y0+2*pad:.0f}" '
                f'style="width:100%;height:auto;display:block">'+'\n'.join(self.el)+'</svg>')

F={}

# ═══════════ 1. PLAN — casa vazuta de sus ═══════════
g=D(0.115)
BPx, FPx = d['BP'], d['FP']
W_out = d['WB_clear']+2*BPx                      # 2195, exteriorul stalpilor din spate
# adancimi (y = 0 la fata din spate a stalpului spate)
yB0, yB1 = 0, BPx                                 # stalpul spate
yF0 = yB1 + d['DEP']                              # fata din spate a stalpului fata
yF1 = yF0 + FPx
# stalpi spate
g.bar(0,yB0,BPx,BPx,fill=W3); g.bar(W_out-BPx,yB0,BPx,BPx,fill=W3)
# stalpi fata, centrati pe aceeasi axa
fx0 = (W_out-(d['WF_clear']+2*FPx))/2
g.bar(fx0,yF0,FPx,FPx,fill=W3); g.bar(fx0+d['WF_clear']+FPx,yF0,FPx,FPx,fill=W3)
# perete spate (in banda stalpilor)
g.bar(BPx+2.5,yB0,d['WALL_B'],d['D'],fill=W1)
# perete fata
g.bar(fx0+FPx+2.5,yF0,d['WALL_F'],d['D'],fill=W1)
# pereti laterali, intre ele
g.bar(BPx,yB1,d['D'],d['DEP'],fill=W2); g.bar(W_out-BPx-d['D'],yB1,d['D'],d['DEP'],fill=W2)
# goluri, proiectate
usa_x = fx0+FPx+2.5+938
g.bar(usa_x,yF0+30,d['GOL_USA'],40,fill=GLASS,stroke=ACC2)
g.tx(usa_x+d['GOL_USA']/2,yF1+300,'usa 550',size=12,fill=ACC2)
fer_x = fx0+FPx+2.5+161
g.bar(fer_x,yF0+30,d['GOL_FER'],40,fill=GLASS,stroke=ACC)
g.tx(fer_x+d['GOL_FER']/2,yF1+300,'fereastra 570',size=12,fill=ACC)
for sx,lbl in ((BPx+d['D']/2,'geam 490'),(W_out-BPx-d['D']/2,'geam 490')):
    gy=yB1+(d['DEP']-d['GOL_GEAM'])/2
    g.bar(sx-20,gy,40,d['GOL_GEAM'],fill=GLASS,stroke=ACC)
# cote — spatele in JOS pe ecran (y=0), fata in SUS
g.dimh(BPx,W_out-BPx,yB0,f"{d['WB_clear']}  lumina spate (masurat)",off=34)
g.dimh(0,W_out,yB0,f"{round(W_out)}  exteriorul stalpilor din spate",off=64)
g.dimh(fx0+FPx,fx0+FPx+d['WF_clear'],yF1,f"{d['WF_clear']}  lumina fata (masurat)",off=-34)
g.dimv(yB1,yF0,0,f"{round(d['DEP'])}  adancime",off=-30)
g.tx(W_out/2,yB0-980,'SPATE  ·  spre gard',size=13,fill=MUT)
g.tx(W_out/2,yF1+620,'FATA  ·  spre terasa',size=13,fill=MUT)
g.note(BPx+d['D']/2,yB1+420,'perete lateral · rigla 48 adancime',dx=-70,dy=6,anchor='end')
g.note(W_out-BPx-d['D']/2,yB1+900,'geam fix 490×490, la mijloc',dx=70,dy=6)
g.note(BPx+500,yB0+d['D']/2,'perete spate, in banda stalpilor',dx=-30,dy=190,anchor='end')
g.tx(W_out/2,yF1+1150,'PLAN — casa vazuta de sus',size=14,fill=MUT)
F['plan']=g.svg()

# ═══════════ 2. SECTIUNE LONGITUDINALA ═══════════
g=D(0.115)
x_f, x_s = 0, d['SPAN']                          # axele reazemelor
g.bar(-500,-60,x_s+1200,60,fill=GROUND,stroke='none')
g.tx(-460,-130,'puntea',size=12,fill=MUT,anchor='start')
# stalp fata + bara de sus
g.bar(x_f-d['FP']/2,0,d['FP'],d['H_F'],fill=W3)
g.bar(x_f-50,d['H_F'],100,d['BARA_F'],fill=W1)
# stalp spate + perete + dulap
g.bar(x_s-d['BP']/2,0,d['BP'],d['H_B'],fill=W3)
g.bar(x_s-25,d['H_B'],50,d['DULAP'],fill=W1)
# caprior
c=math.cos(d['SL']); t=math.tan(d['SL'])
def zr(x): return d['REZ_F']+(x-x_f)*t
p0=(-d['STREASINA'], zr(-d['STREASINA'])); p1=(x_s+d['STREASINA'], zr(x_s+d['STREASINA']))
nx,ny=-math.sin(d['SL']),math.cos(d['SL'])
TH=100
g.poly([p0,p1,(p1[0]-nx*TH,p1[1]+ny*TH),(p0[0]-nx*TH,p0[1]+ny*TH)],fill=W1)
# OSB + onduline
for off,fill,lab in ((TH,ACC2,None),):
    g.poly([(p0[0]-nx*TH,p0[1]+ny*TH),(p1[0]-nx*TH,p1[1]+ny*TH),
            (p1[0]-nx*(TH+55),p1[1]+ny*(TH+55)),(p0[0]-nx*(TH+55),p0[1]+ny*(TH+55))],fill=fill,stroke=INK)
g.tx(x_s*0.42,zr(x_s*0.42)+250,f"caprior 44×100 × {round(d['RAFT'])}",size=13,fill=INK,rot=-d['SLdeg'])
g.tx(x_s*0.42,zr(x_s*0.42)+165,'OSB 12 + Onduline',size=12,fill=ACC2,rot=-d['SLdeg'])
g.tx(x_s*0.62,zr(x_s*0.62)-230,f"panta {d['SLdeg']:.1f}°".replace('.',','),size=14,fill=ACC)
# cote
g.dimv(0,d['H_F'],x_f-260,f"{d['H_F']} stalp fata")
g.dimv(0,d['REZ_F'],x_f-400,f"{d['REZ_F']} reazem fata")
g.dimv(0,d['H_B'],x_s+300,f"{d['H_B']} perete spate",off=22)
g.dimv(0,d['REZ_B'],x_s+440,f"{d['REZ_B']} reazem spate",off=22)
g.dimh(x_f,x_s,-60,f"{round(d['SPAN'])}  intre reazeme",off=34)
g.dimh(x_f-d['FP']/2,x_s-d['BP']/2,-60,f"{round(d['DEP'])} lumina intre stalpi",off=62)
g.dimh(-d['STREASINA'],x_f,d['REZ_F']+200,f"{d['STREASINA']}",off=-16,size=11)
g.dimh(x_s,x_s+d['STREASINA'],d['REZ_B']+200,f"{d['STREASINA']}",off=-16,size=11)
g.note(-d['STREASINA'],zr(-d['STREASINA']),f"muchia la {round(d['EDGE'])} peste podea · FARA jgheab",dx=-30,dy=-90,anchor='end',fill=ACC2)
F['sectiune']=g.svg()

# ═══════════ 3. ELEVATIE SPATE ═══════════
g=D(0.135)
W,H,T = d['WALL_B'],d['H_B'],d['T']
g.bar(0,0,W,T,fill=W2); g.bar(0,H-T,W,T,fill=W2)
XS=[round(i*d['PAS']) for i in range(5)]
for x in XS:
    g.bar(min(max(x-23,0),W-46),T,46,H-2*T,fill=W1)
for (bx,sx,by,sy,arm) in ((46,1,T,1,300),(W-46,-1,T,1,300),(46,1,H-T,-1,150),(W-46,-1,H-T,-1,150)):
    g.ln(bx+sx*arm,by,bx,by+sy*arm,stroke=ACC,sw=4)
for i in range(4): g.dimh(XS[i],XS[i+1],0,off=26)
g.dimh(0,W,0,f"{W}   =  lumina masurata {d['WB_clear']} − 5 mm joc",off=54)
g.dimv(0,H,0,f"{H}",off=-26)
g.dimv(T,H-T,W,f"verticale {d['VB']} ×5",off=26,fill=ACC)
g.tx(W/2,H+700,'PERETE SPATE — vazut din exterior',size=14,fill=MUT)
g.note(46+150,T+150,'proptea jos: brate 300 (424)',dx=60,dy=-30,fill=ACC)
g.note(W-46-75,H-T-75,'proptea sus: brate 150 (212)',dx=-60,dy=-40,anchor='end',fill=ACC)
F['spate']=g.svg()

# ═══════════ 4. ELEVATIE LATERAL ═══════════
g=D(0.135)
L=d['DEP_L']; T=d['T']
hf,hb=d['LATF'],d['LATB']
g.bar(0,0,L,T,fill=W2)
g.poly([(0,hf-T),(L,hb-T),(L,hb),(0,hf)],fill=W2)
gx0=(L-d['GOL_GEAM'])/2; gx1=gx0+d['GOL_GEAM']    # golul centrat pe talpa (545..1035 pe 1580)
VX=[0,gx0-48,gx1,L-48]               # capete + verticalele care marginesc golul (din gx0/gx1, nu scrise de mana)
for x in VX:
    top=vlat(x+24,L)-T
    g.bar(x,T,48,top-T,fill=W1)
g.bar(gx0,d['PRAG']-T,d['GOL_GEAM'],T,fill=W2)
g.bar(gx0,d['PRAG']+d['GOL_GEAM'],d['GOL_GEAM'],T,fill=W2)
g.bar(gx0,d['PRAG'],d['GOL_GEAM'],d['GOL_GEAM'],fill=GLASS,stroke=ACC)
g.tx(gx0+d['GOL_GEAM']/2,d['PRAG']+d['GOL_GEAM']/2,'GOL 490×490',size=13,fill=ACC,weight='600')
for (bx,sx,by,sy) in ((46,1,T,1),(L-46,-1,T,1)):
    g.ln(bx+sx*150,by,bx,by+sy*150,stroke=ACC,sw=4)
g.ln(46+150,vlat(120,L)-T,46,vlat(120,L)-T-150,stroke=ACC,sw=4)
g.ln(L-46-150,vlat(L-120,L)-T,L-46,vlat(L-120,L)-T-150,stroke=ACC,sw=4)
cL=round((L-d['GOL_GEAM'])/2); cR=round((d['DEP_R']-d['GOL_GEAM'])/2)   # 545 stanga · 540 dreapta
g.dimh(0,gx0,0,off=26,size=11); g.dimh(gx0,gx1,0,off=26); g.dimh(gx1,L,0,off=26,size=11)
g.dimh(0,L,0,f"talpa {L} ({cL}/{d['GOL_GEAM']}/{cL})  ·  cealalta laterala {d['DEP_R']} ({cR}/{d['GOL_GEAM']}/{cR})",off=54)
g.dimv(0,hf,0,f"{round(hf)} in fata",off=-26)
g.dimv(0,hb,L,f"{round(hb)} in spate",off=26)
g.dimv(0,d['PRAG'],gx0,f"prag {d['PRAG']}",off=-26,fill=ACC)
g.tx(L/2,hb+700,'PERETE LATERAL — din exterior · FATA in stanga, SPATE in dreapta',size=13,fill=MUT)
vs=' · '.join(str(v) for v in d['VLAT'])
g.tx(L/2,-820,f'verticale, de la fata spre spate:  {vs}',size=13,fill=ACC)
F['lateral']=g.svg()

# ═══════════ 5. ELEVATIE FATA ═══════════
g=D(0.135)
W,H,T,FP2 = d['WALL_F'],d['H_F'],d['T'],d['FP']
g.bar(-FP2,0,FP2,H,fill=W3); g.bar(W,0,FP2,H,fill=W3)
g.bar(-FP2,H,d['TOPBAR'],d['BARA_F'],fill=W1)
g.bar(0,0,W,T,fill=W2)
for x0 in (115,731,892,1488,1650): g.bar(x0,T,46,H-T,fill=W1)
g.bar(161,d['PRAG']-T,d['GOL_FER'],T,fill=W2)
g.bar(161,d['PRAG']+d['GOL_FER'],d['GOL_FER'],T,fill=W2)
g.bar(161,d['PRAG'],d['GOL_FER'],d['GOL_FER'],fill=GLASS,stroke=ACC)
g.tx(161+d['GOL_FER']/2,d['PRAG']+d['GOL_FER']/2,'GOL 570',size=13,fill=ACC,weight='600')
g.bar(938,0,d['GOL_USA'],H,fill='#f7f3ea',stroke=ACC2)
g.tx(938+d['GOL_USA']/2,H/2,'USA 550',size=14,fill=ACC2,weight='600')
g.tx(938+d['GOL_USA']/2,H/2-160,f"liber {d['USA_LIBER']}",size=12,fill=ACC2)
g.ln(W-250,T,W,T+250,stroke=ACC,sw=4)
g.ln(150,T,0,T+150,stroke=ACC,sw=4); g.ln(W-150,T,W,T+150,stroke=ACC,sw=4)
for a,b in ((0,161),(161,731),(731,938),(938,1488),(1488,W)): g.dimh(a,b,0,off=26,size=11)
g.dimh(0,W,0,f"rama {W}  =  lumina masurata {d['WF_clear']} − 5",off=54)
g.dimh(-FP2,W+FP2,H+d['BARA_F'],f"bara de sus 100×60  ×  {round(d['TOPBAR'])}  — calca pe amandoi stalpii",off=-30,fill=ACC)
g.dimv(0,H,-FP2,f"{H} stalp",off=-26)
g.dimv(0,d['PRAG'],161,f"prag {d['PRAG']}",off=-26,fill=ACC)
g.tx(W/2,-820,f"verticale {d['VF']} ×5  ·  talpa se taie la usa LA FINAL",size=13,fill=ACC2)
g.tx(W/2,H+1150,'PERETE FATA — din exterior',size=14,fill=MUT)
F['fata']=g.svg()

# ═══════════ 6. PLAN ACOPERIS ═══════════
g=D(0.115)
W5=d['WB_clear']+2*d['BP']; D5=d['RAFT']
g.bar(0,0,W5,D5,fill=HATCH,stroke=LN)
g.bar(0,D5-60,W5,60,fill=W2)
CX=[round(102+i*d['PAS']) for i in range(5)]
for cx in CX: g.bar(cx-22,0,44,D5,fill=W1)
for a,b in zip(CX,CX[1:]):
    g.bar(a+22,D5-330,b-a-44,110,fill=W2); g.bar(a+22,150,b-a-44,110,fill=W2)
g.ln(0,1250,W5,1250,stroke=ACC,sw=2.5,dash='14,9')
g.tx(W5/2,1250+90,f"imbinarea placilor de OSB   ·   2200×1250  +  2200×{round(D5-1250)}",size=12,fill=ACC)
for i in range(4): g.dimh(CX[i],CX[i+1],0,off=26)
g.dimh(CX[0],CX[-1],0,'capriorii, in dreptul verticalelor din pereti',off=54)
g.dimv(0,D5,W5,f"caprior {round(D5)}",off=26)
g.dimh(0,W5,D5,f"{round(W5)}  =  dulapul de 2200, taiat",off=-30)
g.tx(W5/2,D5+220,'SPATE / GARD',size=12,fill=MUT)
g.tx(W5/2,-230,'TERASA',size=12,fill=MUT)
g.tx((CX[0]+CX[1])/2,D5-460,f"inchideri {round(d['BLOC'])}",size=12,fill=MUT)
F['acoperis']=g.svg()

# ═══════════ 7. DETALIU ACOPERIS — straturi ═══════════
g=D(0.62)
g.bar(0,0,520,100,fill=W1); g.tx(260,50,'caprior 44×100',size=12)
g.bar(0,100,520,12,fill=W3); g.note(430,106,'OSB3 12 mm',dx=50,dy=-24,fill=ACC)
zz=[]
for i in range(11):
    x=i*47
    zz += [(x,112),(x+12,138),(x+24,138),(x+35,112)]
g.poly([(0,112)]+zz+[(520,112)],fill=ACC2,stroke=ACC2,sw=1)
g.note(140,138,'Onduline — cuiele NUMAI pe varf',dx=40,dy=-46,fill=ACC2)
g.note(200,112,'in adancitura curge apa: fiecare cui de acolo e o gaura',dx=-30,dy=64,anchor='end')
g.dimv(0,100,0,'100',off=-22); g.dimv(100,112,0,'12',off=-22)
g.tx(260,-90,'DETALIU ACOPERIS — sectiune prin straturi (scara 1:1,6)',size=13,fill=MUT)
F['strat']=g.svg()


# ═══════════ 8. COLT SPATE — plan (principiu) ═══════════
g=D(0.62)
g.bar(0,0,420,100,fill=W2); g.tx(210,50,'grinda de margine',size=11,fill=MUT)
g.bar(0,100,420,240,fill=W1); g.tx(210,230,'dusumea',size=11,fill=MUT)
g.bar(460,0,90,90,fill=W3); g.tx(505,45,'stalp',size=11,fill=MUT)
g.bar(420,0,40,100,fill=HATCH,stroke=ACC2,sw=1.4,dash='5,4')
g.bar(420,100,130,40,fill=HATCH,stroke=ACC2,sw=1.4,dash='5,4')
g.tx(660,60,'GOL',size=13,fill=ACC2,anchor='start')
g.tx(660,10,'latura A',size=11,fill=ACC2,anchor='start')
g.tx(660,110,'latura B',size=11,fill=ACC2,anchor='start')
g.dimh(420,460,0,'~100',off=30,fill=ACC2)
g.tx(275,-420,'COLT SPATE — PLAN, vedere de sus  ·  schema de principiu',size=13,fill=MUT)
g.tx(275,-510,'golul e in L in jurul stalpului · se face pe amandoua laturile, la amandoua colturile',size=12,fill=DIM)
F['colt_plan']=g.svg()

# ═══════════ 9. COLT SPATE — sectiune (principiu) ═══════════
g=D(0.62)
g.bar(-40,-120,760,120,fill=GROUND,stroke='none')
g.bar(0,0,420,200,fill=W2)
g.bar(0,200,420,28,fill=W1)
g.bar(460,-200,90,760,fill=W3)
# vinclu, ca polita
g.bar(388,152,32,9,fill=METAL,stroke=METAL2)
g.bar(420,152,46,9,fill=METAL,stroke=METAL2)
# blocaj + scandura
g.bar(420,161,40,67,fill='#cdbf9c')
g.bar(388,228,132,28,fill=W1)
# suruburi
for sx in (412,436,456): g.ln(sx,228,sx-78,66,stroke=METAL2,sw=2.2)
for sy in (330,430): g.ln(462,sy,406,sy-46,stroke=METAL2,sw=2.2)
# cote si etichete, toate in afara conturului
g.dimh(420,460,-120,'~100',off=30,fill=ACC2)
g.dimv(0,228,-40,'228',off=-26)
g.note(210,100,'grinda de margine',dx=-60,dy=60,anchor='end')
g.note(505,300,'stalpul de colt',dx=90,dy=0)
g.note(443,157,'vinclu 90×65 — polita',dx=150,dy=-110)
g.note(440,195,'blocaj, taiat pe loc',dx=190,dy=-56)
g.note(454,242,'scandura de calcat',dx=210,dy=6)
g.note(390,150,'3× 8×140 oblic in grinda',dx=-70,dy=-70,anchor='end',fill=METAL2)
g.note(430,400,'2× 8×140 in stalp',dx=120,dy=64,fill=METAL2)
g.tx(300,-420,'COLT SPATE — SECTIUNE  ·  schema de principiu, cotele se iau pe teren',size=13,fill=MUT)
g.tx(300,-510,'greutatea: scandura → blocaj → vinclu → grinda → stalpii puntii → pamant',size=12,fill=ACC)
F['colt_sect']=g.svg()

# ═══════════ 10. PRINDEREA PERETELUI IN STALP ═══════════
g=D(0.30)
g.bar(0,0,100,d['H_B'],fill=W3); g.tx(50,d['H_B']+80,'stalp de 4 m',size=12,fill=MUT)
g.bar(100,d['T'],48,d['VB'],fill=W1); g.tx(124,900,'verticala de capat · rigla 48',size=11,fill=MUT,rot=-90)
g.bar(100,0,420,d['T'],fill=W2); g.bar(100,d['H_B']-d['T'],420,d['T'],fill=W2)
for zz in (150,700,900,1560):
    g.ln(146,zz,20,zz,stroke=METAL2,sw=2.6)
    g.ln(40,zz-14,20,zz,stroke=METAL2,sw=2.6); g.ln(40,zz+14,20,zz,stroke=METAL2,sw=2.6)
g.note(60,900,'4× surub 8×140  ·  unul jos, doua la mijloc, unul sus',dx=-40,dy=-90,anchor='end',fill=METAL2)
g.note(50,150,'gaura de 6 mm data inainte in stalp — altfel crapa',dx=-40,dy=150,anchor='end',fill=ACC2)
g.dimv(d['T'],d['H_B']-d['T'],560,f"{d['VB']}",off=24)
g.tx(300,-320,'PRINDEREA PERETELUI DIN SPATE IN STALP — elevatie',size=13,fill=MUT)
F['prindere']=g.svg()

# ═══════════ 11. REAZEMUL DIN SPATE — dulapul de 200×50 pe muchie ═══════════
g=D(0.17)
POST=100
g.bar(0,0,POST,d['H_B'],fill=W3)                              # stalpul spate, pana la 1700
g.tx(POST/2,d['H_B']/2,'stalp spate · 1700',size=11,fill=MUT,rot=-90)
g.bar(25,d['H_B'],50,d['DULAP'],fill=W1)                      # dulapul 200x50, pe muchie
g.tx(50,d['H_B']+d['DULAP']/2,'200',size=12,fill=INK,rot=-90)
g.dimh(25,75,d['H_B']+d['DULAP'],'50',off=-14,size=11)
g.dimv(0,d['H_B'],0,f"{d['H_B']}",off=-26)
g.dimv(0,d['REZ_B'],POST,f"{d['REZ_B']}  reazem",off=26,fill=ACC)
g.note(75,d['REZ_B'],'dulap 200×50 · pe muchie, 200 in sus · taiat la 2200',dx=80,dy=-46,fill=ACC)
g.note(75,d['H_B']+40,'calca pe cununa peretelui (1700) SI pe capetele stalpilor (1700)',dx=95,dy=70,anchor='start')
g.tx(POST/2,-300,'REAZEMUL DIN SPATE — dulapul de 200×50, cum se aseaza',size=13,fill=MUT)
g.tx(POST/2,-370,'o singura bara, taiata la 2200, pe muchie · nimic altceva nu se face din ea',size=11,fill=DIM)
F['reazem']=g.svg()

json.dump(F,open('figs_2d.json','w'))

# ─────────────────── AUTO-VERIFICARE ───────────────────
print('=== MODEL — verificare ===')
chk=[('lumina spate (masurat)',d['WB_clear'],1995),('lumina fata (masurat)',d['WF_clear'],1975),
     ('talpa spate',d['WALL_B'],1990),('talpa fata',d['WALL_F'],1970),
     ('adancime',d['DEP'],1575),('span reazeme',d['SPAN'],1670),
     ('reazem spate',d['REZ_B'],1900),('reazem fata',d['REZ_F'],1660),
     ('panta grade',round(d['SLdeg'],2),8.18),('caprior',round(d['RAFT']),1889),
     ('muchie',round(d['EDGE']),1646),('pas capriori',d['PAS'],497.5),
     ('inchideri',round(d['BLOC']),454),('verticale spate',d['VB'],1604),
     ('verticale fata',d['VF'],1552),('bara de sus fata',round(d['TOPBAR']),2155),
     ('lateral: inaltime fata',round(d['LATF']),1666),('lateral: inaltime spate',round(d['LATB']),1893)]
bad=0
for n,got,exp in chk:
    ok = abs(got-exp)<=1
    if not ok: bad+=1
    print(f"  {'OK ' if ok else 'X  '} {n:28s} {got}")
print(f"  verticale laterale (verbatim): " + ' · '.join(str(v) for v in d['VLAT']))
print(f"\n  {len(F)} desene · {bad} nepotriviri")
print('  ', {k:len(v) for k,v in F.items()})
