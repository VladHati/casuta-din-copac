#!/usr/bin/env python3
"""Axonometric vector renderer for the casuta model. Pure Python -> SVG.
General hexahedra (axis boxes + oriented struts), per-face depth sort (real
occlusion), flat shading, outlines, ground shadow, built/new styling, explode+ghost."""
import math

# ---- geometry (m), mirrored from montaj-3d-complet.html ----
W=2.1; D=1.78; FLOOR=2.2; PS=0.1
deckThk=0.028; jH=0.1; beamH=0.20; beamD=0.09
beamTop=FLOOR-deckThk-jH; beamCy=beamTop-beamH/2; jCy=beamTop+jH/2
fCut=beamTop-beamH
backBeamZ=D-(PS/2+beamD/2); frontBeamZ=0.0
jBack=D-PS/2; jFront=-0.7; jCz=(jBack+jFront)/2; jLen=jBack-jFront
jx=[0.10,0.28,0.72,1.12,1.55,1.98]
tableY=FLOOR+0.58; trunkX=0.5; trunkZ=-0.2

PAPER="#FBFAF8"; ACC=(0xC2,0x69,0x3A)
COL={'post':(0xC4,0x9A,0x6C),'fpost':(0xC4,0x9A,0x6C),'offcut':(0xE6,0xD6,0xBC),
 'beam':(0xB0,0x7F,0x4F),'joist':(0xC8,0xA0,0x6A),'deck':(0xD8,0xC4,0x9B),
 'brace':(0xA8,0x62,0x3A),'metal':(0x9A,0xA0,0xA8),'trunk':(0x7A,0x5A,0x3C),
 'rail':(0xCB,0xA3,0x72),'anchor':(0x8A,0x8A,0x8A),'temp':(0xBE,0xB7,0xAB)}
MUTE=(0xEC,0xE6,0xDA)

# corner sign table & faces (local x,y,z in -1/1)
CS=[(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]
FACE_IDX=[(0,1,5,4),(3,7,6,2),(0,4,7,3),(1,2,6,5),(0,3,2,1),(4,5,6,7)]

SOLIDS=[]  # dict: corners(8 world pts), ck, layer, step, max
def addbox(w,h,d,ck,x,y,z,layer,step,maxstep=None):
    c=[(x+sx*w/2,y+sy*h/2,z+sz*d/2) for sx,sy,sz in CS]
    SOLIDS.append(dict(c=c,ck=ck,layer=layer,step=step,max=maxstep))
def addstrut(ax,ay,az,bx,by,bz,sec,ck,layer,step):
    A=(ax,ay,az); B=(bx,by,bz)
    axis=[B[i]-A[i] for i in range(3)]; L=math.sqrt(sum(v*v for v in axis)) or 1e-6
    axis=[v/L for v in axis]
    up=(0,1,0) if abs(axis[1])<0.98 else (1,0,0)
    u=cross(up,axis); u=norm(u); v=cross(axis,u); v=norm(v)
    ctr=[(A[i]+B[i])/2 for i in range(3)]
    c=[]
    for sx,sy,sz in CS:
        c.append(tuple(ctr[i]+sx*(sec/2)*u[i]+sy*(L/2)*axis[i]+sz*(sec/2)*v[i] for i in range(3)))
    SOLIDS.append(dict(c=c,ck=ck,layer=layer,step=step,max=None))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(a):
    l=math.sqrt(sum(v*v for v in a)) or 1e-6; return tuple(v/l for v in a)

# shoes + anchors
for px,pz in [(0,0),(W,0),(0,D),(W,D)]:
    addbox(0.14,0.10,0.14,'anchor',px,0.05,pz,'sol',1)
    addbox(0.02,0.14,0.12,'metal',px-0.06,0.15,pz,'sol',1)
    addbox(0.02,0.14,0.12,'metal',px+0.06,0.15,pz,'sol',1)
# posts
addbox(PS,3.7,PS,'post',0,1.85,D,'posts',1); addbox(PS,3.7,PS,'post',W,1.85,D,'posts',1)
addbox(PS,fCut,PS,'fpost',0,fCut/2,0,'posts',1); addbox(PS,fCut,PS,'fpost',W,fCut/2,0,'posts',1)
addbox(PS,3.7-fCut,PS,'offcut',0,(fCut+3.7)/2,0,'posts',1,2); addbox(PS,3.7-fCut,PS,'offcut',W,(fCut+3.7)/2,0,'posts',1,2)
# temp props (diagonals)
addstrut(0,0.9,D,-0.45,0.05,D,0.05,'temp','temp',1); addstrut(W,0.9,D,W+0.45,0.05,D,0.05,'temp','temp',1)
addstrut(0,0.9,0,-0.45,0.05,0,0.05,'temp','temp',1); addstrut(W,0.9,0,W+0.45,0.05,0,0.05,'temp','temp',1)
# polita + M12
def POL(px):
    addbox(0.12,0.10,0.10,'beam',px,beamCy-beamH/2-0.05,backBeamZ,'beams',3)
    addbox(0.024,0.024,0.13,'metal',px,beamCy-beamH/2-0.028,backBeamZ+0.01,'metal',3)
    addbox(0.024,0.024,0.13,'metal',px,beamCy-beamH/2-0.072,backBeamZ+0.01,'metal',3)
POL(0); POL(W)
# beams
addbox(W+0.16,beamH,beamD,'beam',W/2,beamCy,backBeamZ,'beams',4)
addbox(W+0.16,beamH,beamD,'beam',W/2,beamCy,frontBeamZ,'beams',5)
def C1(px,pz):
    addbox(0.09,0.012,0.08,'metal',px+0.06,beamCy-beamH/2,pz,'metal',5)
    addbox(0.012,0.09,0.08,'metal',px+0.052,beamCy-beamH/2-0.045,pz,'metal',5)
C1(0,frontBeamZ); C1(W,frontBeamZ)
# joists + C2
for x in jx: addbox(0.1,jH,jLen,'joist',x,jCy,jCz,'joists',6)
for x in jx:
    addbox(0.05,0.07,0.012,'metal',x+0.055,jCy-0.015,frontBeamZ+0.05,'metal',6)
    addbox(0.05,0.07,0.012,'metal',x+0.055,jCy-0.015,backBeamZ-0.05,'metal',6)
# tree+headers
addbox(0.34,jH,0.06,'joist',trunkX,jCy,-0.05,'joists',7); addbox(0.34,jH,0.06,'joist',trunkX,jCy,-0.35,'joists',7)
addbox(0.17,tableY,0.17,'trunk',trunkX,tableY/2,trunkZ,'tree',7)
# blocking
for i in range(len(jx)-1):
    cx=(jx[i]+jx[i+1])/2; bw=(jx[i+1]-jx[i])-0.1
    addbox(bw,jH,0.08,'joist',cx,jCy,backBeamZ,'block',8); addbox(bw,jH,0.08,'joist',cx,jCy,frontBeamZ,'block',8)
# braces (diagonals)
addstrut(0,1.05,jBack,0,fCut,0.05,0.08,'brace','brace',9); addstrut(W,1.05,jBack,W,fCut,0.05,0.08,'brace','brace',9)
addstrut(0.05,1.05,0,0.95,fCut,0,0.08,'brace','brace',9); addstrut(W-0.05,1.05,0,W-0.95,fCut,0,0.08,'brace','brace',9)
addstrut(0,1.1,0.05,0,jCy-0.06,-0.55,0.07,'brace','brace',9); addstrut(W,1.1,0.05,W,jCy-0.06,-0.55,0.07,'brace','brace',9)
# deck
deckY=FLOOR-deckThk/2; hz=(-0.36,-0.04); hx=(0.35,0.65); z=jFront+0.075
while z<=jBack-0.02:
    if hz[0]<z<hz[1]:
        addbox(hx[0],deckThk,0.145,'deck',hx[0]/2,deckY,z,'deck',10); addbox(W-hx[1],deckThk,0.145,'deck',(W+hx[1])/2,deckY,z,'deck',10)
    else: addbox(W,deckThk,0.145,'deck',W/2,deckY,z,'deck',10)
    z+=0.15
# rail
_railposts=set()
def railSeg(x1,z1,x2,z2):
    mx,mz=(x1+x2)/2,(z1+z2)/2; lx,lz=abs(x2-x1),abs(z2-z1); h=lx>lz
    addbox((lx+0.06) if h else 0.08,0.06,0.08 if h else (lz+0.06),'rail',mx,FLOOR+1.0,mz,'rail',11)
    for (x,z) in ((x1,z1),(x2,z2)):
        k=(round(x,2),round(z,2))
        if k in _railposts: continue
        _railposts.add(k); addbox(0.08,1.0,0.08,'rail',x,FLOOR+0.5,z,'rail',11)
railSeg(0,-0.7,W,-0.7); railSeg(0,-0.7,0,D-1.1); railSeg(W,-0.7,W,-0.05); railSeg(W,0.30,W,D-1.1)

NEWLAYER={1:'posts',2:'posts',3:'beams',4:'beams',5:'beams',6:'joists',7:'tree',8:'block',9:'brace',10:'deck',11:'rail'}

YAW=math.radians(40); PITCH=math.radians(30)
cyw,syw=math.cos(YAW),math.sin(YAW); cp,sp=math.cos(PITCH),math.sin(PITCH)
def proj(p):
    x=p[0]-W/2; y=p[1]; z=p[2]-jCz
    x1=x*cyw+z*syw; z1=-x*syw+z*cyw; y1=y
    y2=y1*cp + z1*sp; z2=-y1*sp + z1*cp   # camera ABOVE, looking down (bird's-eye 3/4)
    return (x1, -y2, z2)
def fcent(pts): n=len(pts); return tuple(sum(p[i] for p in pts)/n for i in range(3))
def fnorm(c3):
    a=[c3[1][i]-c3[0][i] for i in range(3)]; b=[c3[2][i]-c3[0][i] for i in range(3)]
    return norm(cross(a,b))
INK="#1A1712"
# line-art face greys by orientation: top / x-side / z-side / bottom
GREY_BUILT={'top':'#FFFFFF','x':'#ECEAE5','z':'#DBD8D1','bot':'#CDCAC3'}
GREY_NEW  ={'top':'#FAE6D5','x':'#EDC8A8','z':'#E2B791','bot':'#D6A87F'}
GREY_METAL={'top':'#EFEFEF','x':'#DCDCDC','z':'#C9C9C9','bot':'#BEBEBE'}
def faceclass(nrm):
    if nrm[1]>0.5: return 'top'
    if nrm[1]<-0.5: return 'bot'
    return 'x' if abs(nrm[0])>=abs(nrm[2]) else 'z'

def render(step,fname,S=300,MARGIN=70):
    faces=[]
    expl=0.0 if step in (1,2) else 0.6
    for s in SOLIDS:
        st=s['step']; mx=s['max']; layer=s['layer']
        if st is not None and st>step: continue
        if mx is not None and step>mx: continue
        if layer=='temp' and step>=9: continue
        isnew=(st==step)
        pal=GREY_METAL if layer=='metal' else (GREY_NEW if isnew else GREY_BUILT)
        dy=expl if (isnew and layer==NEWLAYER.get(step)) else 0.0
        cw=[(c[0],c[1]+dy,c[2]) for c in s['c']]
        for idx in FACE_IDX:
            quad=[cw[i] for i in idx]; nrm=fnorm(quad)
            cen=fcent(quad); bc=fcent(cw)
            if sum((cen[i]-bc[i])*nrm[i] for i in range(3))<0: nrm=tuple(-v for v in nrm)
            scr=[proj(p) for p in quad]; depth=sum(p[2] for p in scr)/4
            faces.append((depth,[(p[0],p[1]) for p in scr],pal[faceclass(nrm)],isnew))
        if dy>0:
            quad=[s['c'][i] for i in FACE_IDX[1]]; scr=[proj(p) for p in quad]
            faces.append((9e9,[(p[0],p[1]) for p in scr],None,'ghost'))
    faces.sort(key=lambda f:f[0],reverse=True)
    allp=[pt for _,poly,_,_ in faces for pt in poly]
    minx=min(p[0] for p in allp);maxx=max(p[0] for p in allp)
    miny=min(p[1] for p in allp);maxy=max(p[1] for p in allp)
    Wpx=int((maxx-minx)*S+2*MARGIN); Hpx=int((maxy-miny)*S+2*MARGIN)
    def T(p): return ((p[0]-minx)*S+MARGIN,(p[1]-miny)*S+MARGIN)
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{Wpx}" height="{Hpx}" viewBox="0 0 {Wpx} {Hpx}">',
         f'<rect width="{Wpx}" height="{Hpx}" fill="{PAPER}"/>']
    for depth,poly,fill,flag in faces:
        pts=' '.join(f'{T(p)[0]:.1f},{T(p)[1]:.1f}' for p in poly)
        if flag=='ghost':
            out.append(f'<polygon points="{pts}" fill="none" stroke="{hx(ACC)}" stroke-width="2" stroke-dasharray="7 5" stroke-opacity="0.9"/>')
        else:
            sw='2.4' if flag else '1.8'
            out.append(f'<polygon points="{pts}" fill="{fill}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"/>')
    out.append('</svg>'); open(fname,'w').write('\n'.join(out)); return fname
def hx(rgb): return '#%02X%02X%02X'%rgb
def lerp(a,b,t): return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))

if __name__=='__main__':
    import sys
    for s in (sys.argv[1:] or ['1','6']):
        render(int(s),f'/sessions/amazing-sleepy-lamport/mnt/outputs/axon_step{s}.svg'); print('wrote',s)
