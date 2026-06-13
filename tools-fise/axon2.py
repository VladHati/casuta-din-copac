#!/usr/bin/env python3
"""Z-buffer raster renderer (pure numpy) for the casuta model.
Per-pixel depth test = correct occlusion (no painter's overlap bugs).
Auto edge-detection from a face-id buffer = clean visible outlines, hidden lines removed.
Output: crisp anti-aliased PNG (supersampled). IKEA line-art look.

Plus: per-step 2D label anchors. render() projects 3D anchor points through the SAME
transform used for the image and returns/emits final-image (x,y) px, so the page can
overlay crisp VECTOR text (labels / dimensions / part badges / arrowheads) on the raster.
Text is NEVER baked into the PNG."""
import math, json, numpy as np
from PIL import Image, ImageDraw
import axon as A   # geometry, proj, palettes, FACE_IDX, faceclass, fnorm, fcent, NEWLAYER, ACC, INK

def hex2rgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
INK=hex2rgb(A.INK); ACC=A.ACC; PAPER=hex2rgb("#FBFAF8")
EXPL=0.62   # explode lift (m) of the new layer; signed-off look

def faces_for(step, final=False):
    """final=True -> full assembly, no explode, nothing flagged new (clean overview)."""
    out=[]; expl=0.0 if (final or step in (1,2)) else EXPL
    ghosts=[]
    for s in A.SOLIDS:
        st=s['step']; mx=s['max']; layer=s['layer']
        if st is not None and st>step: continue
        if mx is not None and step>mx: continue
        if layer=='temp' and step>=9: continue
        isnew=(st==step) and not final
        pal=A.GREY_METAL if layer=='metal' else (A.GREY_NEW if isnew else A.GREY_BUILT)
        dy=expl if (isnew and layer==A.NEWLAYER.get(step)) else 0.0
        cw=[(c[0],c[1]+dy,c[2]) for c in s['c']]
        for idx in A.FACE_IDX:
            quad=[cw[i] for i in idx]; nrm=A.fnorm(quad)
            cen=A.fcent(quad); bc=A.fcent(cw)
            if sum((cen[i]-bc[i])*nrm[i] for i in range(3))<0: nrm=tuple(-v for v in nrm)
            out.append((quad, hex2rgb(pal[A.faceclass(nrm)])))
        if dy>0:
            ghosts.append([s['c'][i] for i in A.FACE_IDX[1]])  # top face final pos
    return out, ghosts

def render(step, fname, S=230, SS=4, M=64, final=False):
    faces,ghosts=faces_for(step, final=final)
    # project
    def pr(p): return A.proj(p)
    proj_faces=[]; allx=[]; ally=[]
    for quad,col in faces:
        sc=[pr(p) for p in quad]  # (X,Y,depth)
        proj_faces.append((sc,col)); allx+= [p[0] for p in sc]; ally+=[p[1] for p in sc]
    minx,maxx=min(allx),max(allx); miny,maxy=min(ally),max(ally)
    Wp=int((maxx-minx)*S+2*M); Hp=int((maxy-miny)*S+2*M)
    Ws,Hs=Wp*SS,Hp*SS
    def T(p): return ((p[0]-minx)*S*SS+M*SS, (p[1]-miny)*S*SS+M*SS)
    color=np.empty((Hs,Ws,3),np.float32); color[:]=PAPER
    zbuf=np.full((Hs,Ws),1e9,np.float32)
    idbuf=np.full((Hs,Ws),-1,np.int32)
    yy,xx=np.mgrid[0:Hs,0:Ws]
    fid=0
    for sc,col in proj_faces:
        # quad -> 2 triangles
        P=[T(p) for p in sc]; Dd=[p[2] for p in sc]
        for tri in ((0,1,2),(0,2,3)):
            (x0,y0),(x1,y1),(x2,y2)=P[tri[0]],P[tri[1]],P[tri[2]]
            d0,d1,d2=Dd[tri[0]],Dd[tri[1]],Dd[tri[2]]
            xmin=max(int(min(x0,x1,x2)),0); xmax=min(int(max(x0,x1,x2))+1,Ws)
            ymin=max(int(min(y0,y1,y2)),0); ymax=min(int(max(y0,y1,y2))+1,Hs)
            if xmin>=xmax or ymin>=ymax: continue
            sx=xx[ymin:ymax,xmin:xmax]; sy=yy[ymin:ymax,xmin:xmax]
            den=((y1-y2)*(x0-x2)+(x2-x1)*(y0-y2))
            if abs(den)<1e-6: continue
            w0=((y1-y2)*(sx-x2)+(x2-x1)*(sy-y2))/den
            w1=((y2-y0)*(sx-x2)+(x0-x2)*(sy-y2))/den
            w2=1-w0-w1
            inside=(w0>=0)&(w1>=0)&(w2>=0)
            depth=w0*d0+w1*d1+w2*d2
            reg_z=zbuf[ymin:ymax,xmin:xmax]
            m=inside&(depth<reg_z)
            reg_z[m]=depth[m]
            reg_c=color[ymin:ymax,xmin:xmax]; reg_c[m]=col
            reg_i=idbuf[ymin:ymax,xmin:xmax]; reg_i[m]=fid
        fid+=1
    # edge detection from idbuffer (visible face boundaries + silhouette)
    e=np.zeros((Hs,Ws),bool)
    e[:, :-1]|= idbuf[:,:-1]!=idbuf[:,1:]
    e[:-1, :]|= idbuf[:-1,:]!=idbuf[1:,:]
    e[:, 1:] |= idbuf[:,1:]!=idbuf[:,:-1]
    e[1:, :] |= idbuf[1:,:]!=idbuf[:-1,:]
    color[e]=INK   # no thickening: avoids flooding thin edge-on members; SS downsample gives AA
    # downsample (box AA)
    img=color.reshape(Hp,SS,Wp,SS,3).mean(axis=(1,3)).astype(np.uint8)
    im=Image.fromarray(img,'RGB')
    # ghosts: dashed accent outline of final top-face, drawn at downsampled scale
    dr=ImageDraw.Draw(im)
    def Td(p): return ((p[0]-minx)*S+M, (p[1]-miny)*S+M)        # final-image px of a PROJECTED point
    def Pp(p3): return Td(A.proj(p3))                            # final-image px of a 3D world point
    for quad in ghosts:
        pts=[Td(A.proj(p)) for p in quad]; pts.append(pts[0])
        for i in range(len(pts)-1): dash_line(dr,pts[i],pts[i+1],ACC,2)
    im.save(fname)

    # ---- label anchors (vector overlay data) -------------------------------
    rd=lambda v:round(v,1)
    items=[]
    for it in _ov(step, final):
        k=it['kind']
        if k=='note':
            fx,fy=it['rel']; items.append({'kind':'note','text':it['text'],
                'x':rd(fx*Wp),'y':rd(fy*Hp),'align':it.get('align','middle')})
        elif k=='badge':
            x,y=Pp(it['p']); items.append({'kind':'badge','text':it['text'],'x':rd(x),'y':rd(y)})
        elif k=='callout':
            x,y=Pp(it['p']); fx,fy=it['rel']
            items.append({'kind':'callout','text':it['text'],'tx':rd(fx*Wp),'ty':rd(fy*Hp),'px':rd(x),'py':rd(y)})
        elif k=='dim':
            ax,ay=Pp(it['a']); bx,by=Pp(it['b'])
            items.append({'kind':'dim','text':it['text'],'ax':rd(ax),'ay':rd(ay),'bx':rd(bx),'by':rd(by)})
        elif k=='arrow':
            ax,ay=Pp(it['a']); bx,by=Pp(it['b'])
            items.append({'kind':'arrow','ax':rd(ax),'ay':rd(ay),'bx':rd(bx),'by':rd(by)})
    # auto drop-in arrow(s): point down onto the final seat. One per cluster if <=2 clusters, else one central.
    if ghosts and not final:
        groups={}
        for q in ghosts:
            c=A.fcent(q); groups.setdefault(round(c[0],1),[]).append(c)
        if len(groups)<=2: seats=[ (sum(p[0] for p in g)/len(g),sum(p[1] for p in g)/len(g),sum(p[2] for p in g)/len(g)) for g in groups.values()]
        else:
            cg=[A.fcent(q) for q in ghosts]
            seats=[(sum(c[0] for c in cg)/len(cg),sum(c[1] for c in cg)/len(cg),sum(c[2] for c in cg)/len(cg))]
        for (gx,gy,gz) in seats:
            a=Pp((gx,gy+EXPL*0.62,gz)); b=Pp((gx,gy+0.05,gz))
            items.append({'kind':'arrow','ax':rd(a[0]),'ay':rd(a[1]),'bx':rd(b[0]),'by':rd(b[1])})

    meta={'w':Wp,'h':Hp,'items':items}
    jname=fname.rsplit('.',1)[0]+'.json'
    json.dump(meta,open(jname,'w'),ensure_ascii=False)
    return meta

def dash_line(dr,a,b,color,w,dash=9,gap=6):
    dx,dy=b[0]-a[0],b[1]-a[1]; L=math.hypot(dx,dy) or 1; ux,uy=dx/L,dy/L; t=0
    while t<L:
        x1,y1=a[0]+ux*t,a[1]+uy*t; t2=min(t+dash,L); x2,y2=a[0]+ux*t2,a[1]+uy*t2
        dr.line([x1,y1,x2,y2],fill=color,width=w); t+=dash+gap

# ===== label-anchor model (3D points in canonical axon coords) ================
# kinds: badge(text,p3d) · note(text,rel x/y in [0,1]) · dim(text,a3d,b3d) · arrow(a3d,b3d)
def _ov(step, final=False):
    W,D,F,PS=A.W,A.D,A.FLOOR,A.PS
    jCy=A.jCy; bC=A.beamCy; bk=A.backBeamZ; E=EXPL
    polY=bC-A.beamH/2-0.05                     # polita top-ish (final)
    def B(t,p): return {'kind':'badge','text':t,'p':p}
    def CO(t,p,fx,fy): return {'kind':'callout','text':t,'p':p,'rel':(fx,fy)}
    def NO(t,fx,fy,a='middle'): return {'kind':'note','text':t,'rel':(fx,fy),'align':a}
    def DM(t,a,b): return {'kind':'dim','text':t,'a':a,'b':b}
    if final:   # OVERVIEW (Ce construim) — callouts to the margins, center stays clean
        return [CO('ST',(W,3.4,D),0.86,0.12), CO('copac',(A.trunkX,2.55,A.trunkZ),0.13,0.20),
                CO('GR',(W,A.beamTop,0),0.90,0.66), CO('JO',(0.10,jCy,-0.6),0.10,0.74),
                CO('DL',(1.55,F-A.deckThk/2,1.1),0.90,0.40),
                NO('platforma la 2,2 m  .  balcon 700 mm in consola  .  balustrada 1 m',0.5,0.975)]
    if step==1:
        return [B('ST',(0,2.95,D)),
                NO('S1.S2 spate (4 m)  .  S3.S4 fata (taiate la +1872)',0.5,0.975)]
    if step==2:
        return [DM('+2200 podea',(W,2.20,0),(W+0.44,2.20,0)),
                DM('+1872 taie',(W,1.872,0),(W+0.44,1.872,0)),
                NO('taie la 1872, NU la 2200  .  partea taiata = polite',0.5,0.975)]
    if step==3:
        return [B('PO',(0,polY+E,bk)), DM('+1872',(0,polY,bk),(-0.40,polY,bk)),
                NO('polita din offcut  .  2 buloane M12 / polita',0.5,0.975)]
    if step==4:
        return [B('GR',(W/2,bC+E,bk)), DM('+2072',(W,A.beamTop,bk),(W+0.42,A.beamTop,bk)),
                NO('grinda spate sta PE polite  .  3 H1 + coltar C2 anti-smulgere',0.5,0.975)]
    if step==5:
        return [B('GR',(W/2,bC+E,0)), B('C1',(0,A.beamTop,0)), B('C1',(W,A.beamTop,0)),
                DM('+2072',(0,A.beamTop,0),(-0.42,A.beamTop,0)),
                NO('grinda fata pe varful stalpilor taiati  .  2 coltare C1 / stalp',0.5,0.975)]
    if step==6:
        return [B('JO x6',(0.10,jCy+E,-0.55)), B('C2',(0.155,jCy,0.0)),
                DM('700 consola',(0.10,jCy+E,-0.7),(0.10,jCy+E,0.0)),
                NO('pozitii pe grinda: 100 . 280 . 720 . 1120 . 1550 . 1980',0.5,0.975)]
    if step==7:
        return [B('copac',(A.trunkX,2.30,A.trunkZ)),
                DM('+2780',(A.trunkX,2.78,A.trunkZ),(A.trunkX,3.05,A.trunkZ)),
                NO('reteaza la +2780  .  joc de 3-5 cm jur-imprejur',0.5,0.975)]
    if step==8:
        return [B('blocaje',(0.50,jCy+E,bk)),
                NO('blocaje scurte intre joiste, peste fiecare grinda (fata + spate)',0.5,0.975)]
    if step==9:
        return [B('CF',(0.0,(1.05+1.872)/2+E,(bk+0.05)/2)),
                NO('contrafise pe toate planurile + sub nas  .  apoi SCOATE proptelele de la baza',0.5,0.975)]
    if step==10:
        return [B('DL 28x145',(0.0,F-A.deckThk/2+E,-0.45)),
                NO('prima scandura la margine  .  gol egal de 5 mm intre scanduri',0.5,0.975)]
    if step==11:
        rx=0.02
        return [B('poarta . S3',(W/2,F+0.30,-0.7)),
                DM('1 m',(rx,F+E,-0.68),(rx,F+1.0+E,-0.68)),
                NO('mana curenta la 1 m  .  goluri sub 9 cm  .  poarta pe latura S3',0.5,0.975)]
    return []

# ===== vector overlay SVG (sized to the PNG pixel box, scaled by the page) =====
def overlay_svg(meta):
    w,h=meta['w'],meta['h']; items=meta['items']
    fb=w*0.0265; fn=w*0.0225; fd=w*0.0215; sw=max(w*0.0030,1.6)
    INKx='#161413'; ACCx='#C2693A'; SOFT='#3C3833'
    o=[f'<svg class="ovl" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid meet" '
       f'xmlns="http://www.w3.org/2000/svg" font-family="Space Mono, monospace">']
    def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    def clampx(x,anchor,tw):
        pad=fd*0.6
        if anchor=='start': x0,x1=x,x+tw
        elif anchor=='end': x0,x1=x-tw,x
        else: x0,x1=x-tw/2,x+tw/2
        if x1>w-pad: x-=(x1-(w-pad)); x0-=(x1-(w-pad))
        if x0<pad: x+=(pad-x0)
        return x
    def pill(x,y,text,fs,fill=INKx,fg='#fff'):
        t=esc(text); bw=len(text)*fs*0.66+fs*0.8; bh=fs*1.5; rx=bh*0.28
        return (f'<rect x="{x-bw/2:.1f}" y="{y-bh/2:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="{rx:.1f}" fill="{fill}"/>'
                f'<text x="{x:.1f}" y="{y+fs*0.36:.1f}" text-anchor="middle" font-size="{fs:.1f}" '
                f'font-weight="700" fill="{fg}">{t}</text>')
    for it in items:
        k=it['kind']
        if k=='badge':
            x=clampx(it['x'],'middle',len(it['text'])*fb*0.66+fb*0.8)
            o.append('<g>'+pill(x,it['y'],it['text'],fb)+'</g>')
        elif k=='callout':
            tx=clampx(it['tx'],'middle',len(it['text'])*fb*0.66+fb*0.8); ty=it['ty']; px_,py_=it['px'],it['py']
            o.append(f'<g><line x1="{tx:.1f}" y1="{ty:.1f}" x2="{px_:.1f}" y2="{py_:.1f}" '
                     f'stroke="{ACCx}" stroke-width="{sw:.1f}"/>'
                     f'<circle cx="{px_:.1f}" cy="{py_:.1f}" r="{sw*1.7:.1f}" fill="{ACCx}"/>'
                     +pill(tx,ty,it['text'],fb)+'</g>')
        elif k=='note':
            t=esc(it['text']); al=it.get('align','middle')
            x=clampx(it['x'],al,len(it['text'])*fn*0.55)
            o.append(f'<text x="{x:.1f}" y="{it["y"]:.1f}" text-anchor="{al}" font-size="{fn:.1f}" '
                     f'font-family="Space Grotesk, sans-serif" fill="{SOFT}">{t}</text>')
        elif k=='dim':
            t=esc(it['text']); ax,ay,bx,by=it['ax'],it['ay'],it['bx'],it['by']
            dx,dy=bx-ax,by-ay; L=math.hypot(dx,dy) or 1; px,py=-dy/L,dx/L; tk=fd*0.5
            tick=lambda X,Y:(f'<line x1="{X-px*tk:.1f}" y1="{Y-py*tk:.1f}" x2="{X+px*tk:.1f}" '
                             f'y2="{Y+py*tk:.1f}" stroke="{ACCx}" stroke-width="{sw:.1f}"/>')
            anchor='start' if bx>=ax else 'end'
            tx=clampx(bx+(fd*0.4 if bx>=ax else -fd*0.4),anchor,len(it['text'])*fd*0.62)
            o.append(f'<g><line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" '
                     f'stroke="{ACCx}" stroke-width="{sw:.1f}"/>{tick(ax,ay)}{tick(bx,by)}'
                     f'<text x="{tx:.1f}" y="{by+fd*0.35:.1f}" text-anchor="{anchor}" font-size="{fd:.1f}" '
                     f'font-weight="700" fill="{ACCx}">{t}</text></g>')
        elif k=='arrow':
            ax,ay,bx,by=it['ax'],it['ay'],it['bx'],it['by']
            a=math.atan2(by-ay,bx-ax); hl=fb*0.8
            o.append(f'<g><line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" '
                     f'stroke="{ACCx}" stroke-width="{sw*1.1:.1f}"/>'
                     +''.join(f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{bx-hl*math.cos(a+d):.1f}" '
                              f'y2="{by-hl*math.sin(a+d):.1f}" stroke="{ACCx}" stroke-width="{sw*1.1:.1f}"/>'
                              for d in (0.5,-0.5))+'</g>')
    o.append('</svg>')
    return ''.join(o)

if __name__=='__main__':
    import sys
    for s in (sys.argv[1:] or ['1','6']):
        render(int(s),f'/tmp/r_step{s}.png'); print('wrote',s)
