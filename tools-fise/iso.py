# -*- coding: utf-8 -*-
import math
C=math.cos(math.radians(30)); S=math.sin(math.radians(30))
def proj(x,y,z): return ((x - z)*C, (x + z)*S - y)

def box_faces(x,y,z,dx,dy,dz):
    X0,X1=x,x+dx; Y0,Y1=y,y+dy; Z0,Z1=z,z+dz
    P=lambda X,Y,Z:(X,Y,Z)
    top=[P(X0,Y1,Z0),P(X1,Y1,Z0),P(X1,Y1,Z1),P(X0,Y1,Z1)]
    front=[P(X0,Y0,Z0),P(X1,Y0,Z0),P(X1,Y1,Z0),P(X0,Y1,Z0)]
    right=[P(X1,Y0,Z0),P(X1,Y0,Z1),P(X1,Y1,Z1),P(X1,Y1,Z0)]
    return {'top':top,'front':front,'right':right}

def _depth(b):
    cx=b['x']+b['dx']/2; cy=b['y']+b['dy']/2; cz=b['z']+b['dz']/2
    return -cx + cz - cy

SHADE={'top':'#ffffff','front':'#ECE7DF','right':'#DED8CD'}
HL   ={'top':'#FBE0CD','front':'#F2B98E','right':'#E8A06F'}
GHOST={'top':'#FbFAF8','front':'#F4F1EB','right':'#ECE8E1'}
INK='#161413'; ACC='#C2693A'
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
    if built: b=mix(b,'#ffffff',0.62)
    return {'top':light(b,0.13),'front':b,'right':dark(b,0.15)}, dark(PAL.get(mat,b),0.5 if not built else 0.32)

def render(boxes, struts=None, screws=None, dims=None, arrows=None, labels=None, ground=None, W=640, pad=58):
    boxes=[dict(b) for b in boxes]; struts=struts or []; screws=screws or []
    dims=dims or []; arrows=list(arrows or []); labels=labels or []
    # pieces with explode: draw shifted, add motion arrow + ghost target
    draw_boxes=[]; ghosts=[]
    for b in boxes:
        ex=b.get('ex')
        if ex:
            tgt=dict(b); 
            db=dict(b); db['x']+=ex[0]; db['y']+=ex[1]; db['z']+=ex[2]; db['hl']=True
            draw_boxes.append(db); ghosts.append(tgt)
            c0=(db['x']+db['dx']/2, db['y']+db['dy']/2, db['z']+db['dz']/2)
            c1=(b['x']+b['dx']/2, b['y']+b['dy']/2, b['z']+b['dz']/2)
            arrows.append({'p1':c0,'p2':c1,'motion':True})
        else:
            draw_boxes.append(b)
    # collect projected pts for bounds
    pts=[]
    allb=draw_boxes+ghosts
    for b in allb:
        for f in box_faces(b['x'],b['y'],b['z'],b['dx'],b['dy'],b['dz']).values():
            pts+=[proj(*p) for p in f]
    for s in struts: pts+=[proj(*s['p1']),proj(*s['p2'])]
    for s in screws: pts.append(proj(*s['at']))
    for a in arrows: pts+=[proj(*a['p1']),proj(*a['p2'])]
    for d in dims: pts+=[proj(*d['p1']),proj(*d['p2'])]
    if ground: pts+=[proj(ground[0],0,ground[2]),proj(ground[1],0,ground[3])]
    xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
    minx,maxx,miny,maxy=min(xs),max(xs),min(ys),max(ys)
    sc=(W-2*pad)/max(1,(maxx-minx)); H=(maxy-miny)*sc+2*pad
    def tx(p): return ((p[0]-minx)*sc+pad,(p[1]-miny)*sc+pad)
    def TP(P): return tx(proj(*P))
    out=[f'<svg viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" font-family="Space Grotesk,Arial,sans-serif">']
    def poly(face,fill,lw,oc=INK):
        d=' '.join(f'{TP(p)[0]:.1f},{TP(p)[1]:.1f}' for p in face)
        return f'<polygon points="{d}" fill="{fill}" stroke="{oc}" stroke-width="{lw}" stroke-linejoin="round"/>'
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
    # ghost targets (dashed top outline)
    for g in ghosts:
        f=box_faces(g['x'],g['y'],g['z'],g['dx'],g['dy'],g['dz'])['top']
        d=' '.join(f'{TP(p)[0]:.1f},{TP(p)[1]:.1f}' for p in f)
        out.append(f'<polygon points="{d}" fill="none" stroke="{ACC}" stroke-width="1.6" stroke-dasharray="6 5"/>')
    # boxes far->near
    for b in sorted(draw_boxes,key=_depth,reverse=True):
        fa=box_faces(b['x'],b['y'],b['z'],b['dx'],b['dy'],b['dz'])
        new=b.get('hl'); built=bool(b.get('built')) and not new
        mat=b.get('mat','wood'); base=b.get('fill')
        cols,oc=facecols(mat, base, built)
        lw=3.4 if new else (2.0 if built else 2.6)
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
        out.append(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" stroke="{ACC}" stroke-width="3.2"{st}/>')
        ang=math.atan2(p2[1]-p1[1],p2[0]-p1[0])
        for da in (2.5,-2.5):
            hx=p2[0]-15*math.cos(ang+da); hy=p2[1]-15*math.sin(ang+da)
            out.append(f'<line x1="{p2[0]:.1f}" y1="{p2[1]:.1f}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{ACC}" stroke-width="3.2"/>')
    # screws: chevron shaft + arrowhead into wood + code/qty badge
    for s in screws:
        at=TP(s['at']); d=s.get('dir',(0,-1,0)); L=s.get('len',150)
        tail=(s['at'][0]-d[0]*L,s['at'][1]-d[1]*L,s['at'][2]-d[2]*L); t2=TP(tail)
        ang=math.atan2(at[1]-t2[1],at[0]-t2[0])
        out.append(f'<line x1="{t2[0]:.1f}" y1="{t2[1]:.1f}" x2="{at[0]:.1f}" y2="{at[1]:.1f}" stroke="{INK}" stroke-width="2.6"/>')
        # threads
        for i in range(1,5):
            t=i/5.2; cxp=t2[0]+(at[0]-t2[0])*t; cyp=t2[1]+(at[1]-t2[1])*t
            ox=6*math.cos(ang+math.pi/2); oy=6*math.sin(ang+math.pi/2)
            out.append(f'<line x1="{cxp-ox:.1f}" y1="{cyp-oy:.1f}" x2="{cxp+ox:.1f}" y2="{cyp+oy:.1f}" stroke="{INK}" stroke-width="1.6"/>')
        for da in (2.5,-2.5):
            hx=at[0]-12*math.cos(ang+da); hy=at[1]-12*math.sin(ang+da)
            out.append(f'<line x1="{at[0]:.1f}" y1="{at[1]:.1f}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{INK}" stroke-width="2.6"/>')
        if s.get('code'):
            lab=s['code']+(f"  x{s['n']}" if s.get('n') else '')
            wbed=10+len(lab)*7.2
            out.append(f'<rect x="{t2[0]-wbed/2:.1f}" y="{t2[1]-24:.1f}" width="{wbed:.1f}" height="17" rx="4" fill="{INK}"/>')
            out.append(f'<text x="{t2[0]:.1f}" y="{t2[1]-11.5:.1f}" fill="#fff" font-size="11" font-weight="700" text-anchor="middle" font-family="Space Mono,monospace">{lab}</text>')
    # dims with extension ticks
    for d in dims:
        a=TP(d['p1']); b=TP(d['p2'])
        out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{ACC}" stroke-width="1.6"/>')
        ang=math.atan2(b[1]-a[1],b[0]-a[0])+math.pi/2
        for P in (a,b):
            out.append(f'<line x1="{P[0]-6*math.cos(ang):.1f}" y1="{P[1]-6*math.sin(ang):.1f}" x2="{P[0]+6*math.cos(ang):.1f}" y2="{P[1]+6*math.sin(ang):.1f}" stroke="{ACC}" stroke-width="1.6"/>')
        mx,my=(a[0]+b[0])/2,(a[1]+b[1])/2
        t=d['t']; wbed=10+len(t)*7.5
        out.append(f'<rect x="{mx-wbed/2:.1f}" y="{my-20:.1f}" width="{wbed:.1f}" height="16" rx="4" fill="#fff" stroke="{ACC}" stroke-width="1.2"/>')
        out.append(f'<text x="{mx:.1f}" y="{my-8:.1f}" fill="{ACC}" font-size="11.5" font-weight="700" text-anchor="middle" font-family="Space Mono,monospace">{t}</text>')
    # labels
    for l in labels:
        p=TP(l['at']); col=l.get('color',INK); t=l['t']; wbed=10+len(t)*7
        if l.get('to'):
            q=TP(l['to'])
            out.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{col}" stroke-width="1.2"/>')
            out.append(f'<circle cx="{q[0]:.1f}" cy="{q[1]:.1f}" r="2.6" fill="{col}"/>')
        out.append(f'<rect x="{p[0]-wbed/2:.1f}" y="{p[1]-9:.1f}" width="{wbed:.1f}" height="17" rx="4" fill="#fff" stroke="{col}" stroke-width="1.2"/>')
        out.append(f'<text x="{p[0]:.1f}" y="{p[1]+3.5:.1f}" fill="{col}" font-size="11" font-weight="700" text-anchor="middle" font-family="Space Mono,monospace">{t}</text>')
    out.append('</svg>')
    return '\n'.join(out)
