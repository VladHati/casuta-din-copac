# -*- coding: utf-8 -*-
import math, heapq
C=math.cos(math.radians(30)); S=math.sin(math.radians(30))
def proj(x,y,z): return ((x - z)*C, (x + z)*S - y)

def box_faces(x,y,z,dx,dy,dz):
    X0,X1=x,x+dx; Y0,Y1=y,y+dy; Z0,Z1=z,z+dz
    P=lambda X,Y,Z:(X,Y,Z)
    top=[P(X0,Y1,Z0),P(X1,Y1,Z0),P(X1,Y1,Z1),P(X0,Y1,Z1)]
    front=[P(X0,Y0,Z0),P(X1,Y0,Z0),P(X1,Y1,Z0),P(X0,Y1,Z0)]
    right=[P(X1,Y0,Z0),P(X1,Y0,Z1),P(X1,Y1,Z1),P(X1,Y1,Z0)]
    return {'top':top,'front':front,'right':right}

# ---- depth ordering ----------------------------------------------------------
# View ray is along (1,1,1); the visible faces (top/front/right) show that the
# camera sits at large x, small z, large y.  So "nearer" grows with +x, +y, -z.
# A single centroid cannot order two long members that cross (a beam on x vs a
# joist on z) because the crossing is resolved by HEIGHT, not by the centroid.
# So we use a pairwise separating-axis test: if two boxes are separated along an
# axis, the box on the near side of that axis occludes.  Build a "draw-before"
# graph and topo-sort it (centroid as tie-break / cycle fallback).
def _N(b): return (b['x']+b['dx']/2)+(b['y']+b['dy']/2)-(b['z']+b['dz']/2)
def _ext(b): return (b['x'],b['x']+b['dx'],b['y'],b['y']+b['dy'],b['z'],b['z']+b['dz'])
def _rel(a,b,eps=1.0):
    # +1 : a is FARTHER than b (draw a first).  -1 : a is nearer.  0 : tangled.
    ax0,ax1,ay0,ay1,az0,az1=a; bx0,bx1,by0,by1,bz0,bz1=b
    if ax1<=bx0+eps: return  1   # a lower x  -> farther
    if bx1<=ax0+eps: return -1
    if ay1<=by0+eps: return  1   # a lower y  -> farther
    if by1<=ay0+eps: return -1
    if az0>=bz1-eps: return  1   # a higher z -> farther
    if bz0>=az1-eps: return -1
    return 0
def order_boxes(boxes):
    n=len(boxes); E=[_ext(b) for b in boxes]
    adj={i:[] for i in range(n)}; indeg=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            r=_rel(E[i],E[j])
            if r>0: adj[i].append(j); indeg[j]+=1
            elif r<0: adj[j].append(i); indeg[i]+=1
    h=[(_N(boxes[i]),i) for i in range(n) if indeg[i]==0]; heapq.heapify(h)
    out=[]; seen=set()
    while h:
        _,i=heapq.heappop(h)
        if i in seen: continue
        seen.add(i); out.append(i)
        for j in adj[i]:
            indeg[j]-=1
            if indeg[j]==0: heapq.heappush(h,(_N(boxes[j]),j))
    if len(out)<n:                       # cycle: append leftovers far->near
        out+=sorted([i for i in range(n) if i not in seen], key=lambda i:_N(boxes[i]))
    return [boxes[i] for i in out]

# ---- palette -----------------------------------------------------------------
INK='#161413'; ACC='#C2693A'; BUILT_OC='#8C877C'
PAL={'post':'#E8973C','beam':'#3F8FA6','joist':'#7BAE52','deck':'#E9C277','polita':'#B083C6',
     'metal':'#AAB2BB','brace':'#E2663B','tree':'#A56B41','anchor':'#94A0AB','block':'#CBA24B','wood':'#E2C58A'}
def _h2(c): c=c.lstrip('#'); return tuple(int(c[i:i+2],16) for i in (0,2,4))
def _h(t): return '#%02x%02x%02x'%t
def mix(c1,c2,t):
    a=_h2(c1);b=_h2(c2); return _h(tuple(round(a[i]+(b[i]-a[i])*t) for i in range(3)))
def light(c,t): return mix(c,'#ffffff',t)
def dark(c,t): return mix(c,'#000000',t)
def facecols(mat, base, built):
    b=base if base else PAL.get(mat,PAL['wood'])
    if built:
        b=mix(b,'#ffffff',0.46)                       # tint, but colour still reads
        return {'top':light(b,0.10),'front':b,'right':dark(b,0.12)}, BUILT_OC
    return {'top':light(b,0.13),'front':b,'right':dark(b,0.15)}, dark(PAL.get(mat,b),0.5)

# ---- camera ------------------------------------------------------------------
def _pts(boxes,struts=(),arrows=(),dims=(),ground=None,extra=()):
    pts=[]
    for b in boxes:
        for f in box_faces(b['x'],b['y'],b['z'],b['dx'],b['dy'],b['dz']).values():
            pts+=[proj(*p) for p in f]
    for s in struts: pts+=[proj(*s['p1']),proj(*s['p2'])]
    for a in arrows: pts+=[proj(*a['p1']),proj(*a['p2'])]
    for d in dims: pts+=[proj(*d['p1']),proj(*d['p2'])]
    if ground: pts+=[proj(ground[0],0,ground[2]),proj(ground[1],0,ground[3])]
    pts+=[proj(*p) for p in extra]
    return pts
def make_cam(boxes,struts=(),ground=None,W=940,pad=92,extra=()):
    pts=_pts(boxes,struts=struts,ground=ground,extra=extra)
    xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
    minx,maxx,miny,maxy=min(xs),max(xs),min(ys),max(ys)
    sc=(W-2*pad)/max(1,(maxx-minx)); H=(maxy-miny)*sc+2*pad
    return {'minx':minx,'miny':miny,'sc':sc,'W':W,'H':H,'pad':pad}

def hframe(boxes,struts=(),W=940,pad=92):
    """Cadru orizontal + scara, calculate O DATA din ansamblul final (independent de inaltime)."""
    pts=_pts(boxes,struts=struts)
    xs=[p[0] for p in pts]
    minx,maxx=min(xs),max(xs)
    sc=(W-2*pad)/max(1,(maxx-minx))
    return minx,sc

def cam_window(frame_box, minx, sc, W=940, pad=92):
    """O fereastra verticala (acelasi sc, acelasi minx) -> camera panoramata pe inaltime."""
    x0,x1,y0,y1,z0,z1=frame_box
    ys=[]
    for X in (x0,x1):
        for Z in (z0,z1):
            for Y in (y0,y1): ys.append(proj(X,Y,Z)[1])
    miny,maxy=min(ys),max(ys); H=(maxy-miny)*sc+2*pad
    return {'minx':minx,'miny':miny,'sc':sc,'W':W,'H':H,'pad':pad}

# ---- render ------------------------------------------------------------------
FS_BADGE=16; FS_DIM=16; FS_LABEL=15.5
_SVGN=[0]

def render(boxes, struts=None, screws=None, dims=None, arrows=None, labels=None,
           ground=None, cam=None, W=940, pad=92):
    boxes=[dict(b) for b in boxes]; struts=struts or []; screws=screws or []
    dims=dims or []; arrows=list(arrows or []); labels=labels or []
    # explode: draw shifted (highlighted), full wireframe ghost at target, motion arrow
    draw_boxes=[]; ghosts=[]
    for b in boxes:
        ex=b.get('ex')
        if ex:
            tgt=dict(b)
            db=dict(b); db['x']+=ex[0]; db['y']+=ex[1]; db['z']+=ex[2]; db['hl']=True
            draw_boxes.append(db); ghosts.append(tgt)
            c0=(db['x']+db['dx']/2, db['y']+db['dy']/2, db['z']+db['dz']/2)
            c1=(b['x']+b['dx']/2, b['y']+b['dy']/2, b['z']+b['dz']/2)
            arrows.append({'p1':c0,'p2':c1,'motion':True})
        else:
            draw_boxes.append(b)
    if cam is None:
        cam=make_cam(draw_boxes+ghosts,struts=struts,ground=ground,W=W,pad=pad,
                     extra=[a['p1'] for a in arrows]+[a['p2'] for a in arrows]
                           +[d['p1'] for d in dims]+[d['p2'] for d in dims]
                           +[l['at'] for l in labels])
    minx,miny,sc,Wd,H=cam['minx'],cam['miny'],cam['sc'],cam['W'],cam['H']
    def tx(p): return ((p[0]-minx)*sc+cam['pad'],(p[1]-miny)*sc+cam['pad'])
    def TP(P): return tx(proj(*P))
    _SVGN[0]+=1; cid=f'vp{_SVGN[0]}'
    out=[f'<svg viewBox="0 0 {Wd:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" font-family="Space Grotesk,Arial,sans-serif">',
         f'<defs><clipPath id="{cid}"><rect x="0" y="0" width="{Wd:.0f}" height="{H:.0f}"/></clipPath></defs>',
         f'<g clip-path="url(#{cid})">']
    def poly(face,fill,lw,oc=INK,dash=None):
        d=' '.join(f'{TP(p)[0]:.1f},{TP(p)[1]:.1f}' for p in face)
        da=f' stroke-dasharray="{dash}"' if dash else ''
        return f'<polygon points="{d}" fill="{fill}" stroke="{oc}" stroke-width="{lw}" stroke-linejoin="round"{da}/>'
    # ground (hatched) at y=0
    if ground:
        gx0,gx1,gz0,gz1=ground
        corners=[(gx0,0,gz0),(gx1,0,gz0),(gx1,0,gz1),(gx0,0,gz1)]
        d=' '.join(f'{TP(c)[0]:.1f},{TP(c)[1]:.1f}' for c in corners)
        out.append(f'<polygon points="{d}" fill="#F6F3EE" stroke="#CFC8BB" stroke-width="1.5"/>')
        n=10
        for i in range(n+1):
            t=i/n
            a=TP((gx0+(gx1-gx0)*t,0,gz0)); b=TP((gx0+(gx1-gx0)*t,0,gz1))
            out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#E6E0D5" stroke-width="1"/>')
    # ghost targets: full wireframe (all 3 faces dashed)
    for gb in ghosts:
        fa=box_faces(gb['x'],gb['y'],gb['z'],gb['dx'],gb['dy'],gb['dz'])
        for k in ('right','front','top'):
            out.append(poly(fa[k],'none',1.7,ACC,dash='6 5'))
    # boxes far -> near
    for b in order_boxes(draw_boxes):
        fa=box_faces(b['x'],b['y'],b['z'],b['dx'],b['dy'],b['dz'])
        new=b.get('hl'); built=bool(b.get('built')) and not new
        mat=b.get('mat','wood'); base=b.get('fill')
        cols,oc=facecols(mat, base, built)
        lw=3.6 if new else (1.7 if built else 2.8)
        for k in ('right','front','top'):
            out.append(poly(fa[k],cols[k],lw,oc))
    # struts (diagonals/props/rails) as thick projected bars
    for s in struts:
        a=TP(s['p1']); b=TP(s['p2']); th=s.get('thick',9)
        col=s.get('col', ACC if s.get('hl') else INK)
        out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{col}" stroke-width="{th}" stroke-linecap="round"/>')
        out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#fff" stroke-width="{max(1,th-5)}" stroke-linecap="round" opacity=".18"/>')
    # motion + plain arrows
    for a in arrows:
        p1=TP(a['p1']); p2=TP(a['p2'])
        dash='7 6' if a.get('motion') else None
        st=f' stroke-dasharray="{dash}"' if dash else ''
        out.append(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" stroke="{ACC}" stroke-width="3.4"{st}/>')
        ang=math.atan2(p2[1]-p1[1],p2[0]-p1[0])
        for da in (2.5,-2.5):
            hx=p2[0]-17*math.cos(ang+da); hy=p2[1]-17*math.sin(ang+da)
            out.append(f'<line x1="{p2[0]:.1f}" y1="{p2[1]:.1f}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{ACC}" stroke-width="3.4"/>')
    # screws: chevron shaft + arrowhead into wood + code/qty badge
    for s in screws:
        at=TP(s['at']); d=s.get('dir',(0,-1,0)); L=s.get('len',150)
        tail=(s['at'][0]-d[0]*L,s['at'][1]-d[1]*L,s['at'][2]-d[2]*L); t2=TP(tail)
        ang=math.atan2(at[1]-t2[1],at[0]-t2[0])
        out.append(f'<line x1="{t2[0]:.1f}" y1="{t2[1]:.1f}" x2="{at[0]:.1f}" y2="{at[1]:.1f}" stroke="{INK}" stroke-width="2.8"/>')
        for i in range(1,5):
            t=i/5.2; cxp=t2[0]+(at[0]-t2[0])*t; cyp=t2[1]+(at[1]-t2[1])*t
            ox=6*math.cos(ang+math.pi/2); oy=6*math.sin(ang+math.pi/2)
            out.append(f'<line x1="{cxp-ox:.1f}" y1="{cyp-oy:.1f}" x2="{cxp+ox:.1f}" y2="{cyp+oy:.1f}" stroke="{INK}" stroke-width="1.7"/>')
        for da in (2.5,-2.5):
            hx=at[0]-13*math.cos(ang+da); hy=at[1]-13*math.sin(ang+da)
            out.append(f'<line x1="{at[0]:.1f}" y1="{at[1]:.1f}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{INK}" stroke-width="2.8"/>')
        if s.get('code'):
            lab=s['code']+(f"  x{s['n']}" if s.get('n') else '')
            wbed=14+len(lab)*8.6
            out.append(f'<rect x="{t2[0]-wbed/2:.1f}" y="{t2[1]-30:.1f}" width="{wbed:.1f}" height="22" rx="5" fill="{INK}"/>')
            out.append(f'<text x="{t2[0]:.1f}" y="{t2[1]-14.5:.1f}" fill="#fff" font-size="{FS_BADGE}" font-weight="700" text-anchor="middle" font-family="Space Mono,monospace">{lab}</text>')
    # dims with extension ticks
    for d in dims:
        a=TP(d['p1']); b=TP(d['p2'])
        out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{ACC}" stroke-width="1.8"/>')
        ang=math.atan2(b[1]-a[1],b[0]-a[0])+math.pi/2
        for P in (a,b):
            out.append(f'<line x1="{P[0]-7*math.cos(ang):.1f}" y1="{P[1]-7*math.sin(ang):.1f}" x2="{P[0]+7*math.cos(ang):.1f}" y2="{P[1]+7*math.sin(ang):.1f}" stroke="{ACC}" stroke-width="1.8"/>')
        mx,my=(a[0]+b[0])/2,(a[1]+b[1])/2
        t=d['t']; wbed=14+len(t)*9
        out.append(f'<rect x="{mx-wbed/2:.1f}" y="{my-26:.1f}" width="{wbed:.1f}" height="21" rx="5" fill="#fff" stroke="{ACC}" stroke-width="1.4"/>')
        out.append(f'<text x="{mx:.1f}" y="{my-11:.1f}" fill="{ACC}" font-size="{FS_DIM}" font-weight="700" text-anchor="middle" font-family="Space Mono,monospace">{t}</text>')
    # labels
    for l in labels:
        p=TP(l['at']); col=l.get('color',INK); t=l['t']; wbed=12+len(t)*8.6
        if l.get('to'):
            q=TP(l['to'])
            out.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{col}" stroke-width="1.4"/>')
            out.append(f'<circle cx="{q[0]:.1f}" cy="{q[1]:.1f}" r="3" fill="{col}"/>')
        out.append(f'<rect x="{p[0]-wbed/2:.1f}" y="{p[1]-12:.1f}" width="{wbed:.1f}" height="22" rx="5" fill="#fff" stroke="{col}" stroke-width="1.4"/>')
        out.append(f'<text x="{p[0]:.1f}" y="{p[1]+3.5:.1f}" fill="{col}" font-size="{FS_LABEL}" font-weight="700" text-anchor="middle" font-family="Space Mono,monospace">{t}</text>')
    # cod piesa (badge pe piesele care au 'code')
    for b in draw_boxes:
        if b.get('code'):
            cx=b['x']+b['dx']/2; cy=b['y']+b['dy']; cz=b['z']+b['dz']/2
            P=TP((cx,cy,cz)); s=str(b['code']); wb=18+len(s)*10
            out.append(f'<line x1="{P[0]:.1f}" y1="{P[1]-11:.1f}" x2="{P[0]:.1f}" y2="{P[1]+2:.1f}" stroke="{INK}" stroke-width="1.5"/>')
            out.append(f'<rect x="{P[0]-wb/2:.1f}" y="{P[1]-34:.1f}" width="{wb:.1f}" height="24" rx="6" fill="{INK}"/>')
            out.append(f'<text x="{P[0]:.1f}" y="{P[1]-17:.1f}" fill="#fff" font-size="{FS_BADGE+1}" font-weight="700" text-anchor="middle" font-family="Space Mono,monospace">{s}</text>')
    out.append('</g></svg>')
    return '\n'.join(out)
