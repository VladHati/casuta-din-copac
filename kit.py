#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trusa de desen 2D. Primitive in mm, adnotari in px, bbox auto-fit.
Extinsa fata de gen_2d.py cu: hasura de sectiune, suruburi, sageti, bule numerotate,
zone de necunoscut, si un ajutor de bara de titlu."""
import math

INK="#1c1b18"; ACC="#14532d"; ACC2="#8a3016"; MUT="#6b675e"; DIM="#8a857a"; LN="#d6d0c4"
W1="#e8dfcc"; W2="#d9cdb2"; W3="#c4b696"; W4="#b1a281"
METAL="#9aa1ad"; METAL2="#6f7683"; GLASS="#d7e6e8"; GROUND="#c8c2b4"
VOID="#f2ede2"; WARN="#a8541c"; OK="#14532d"

def esc(s): return s.replace('&','&amp;').replace('<','&lt;')

_UID=[0]
def uid(p='p'):
    _UID[0]+=1; return f'{p}{_UID[0]}'

class D:
    def __init__(self, scale, fs=13):
        self.s=scale; self.el=[]; self.defs=[]; self.fs=fs; self.bb=[1e9,1e9,-1e9,-1e9]
    def X(self,mm): return mm*self.s
    def Y(self,mm): return -mm*self.s
    def _t(self,x,y):
        b=self.bb; b[0]=min(b[0],x); b[1]=min(b[1],y); b[2]=max(b[2],x); b[3]=max(b[3],y)
    def touch(self,x,y): self._t(self.X(x),self.Y(y))

    # ── primitive, in mm ──
    def bar(self,x,y,w,h,fill=W1,stroke=INK,sw=1.5,dash=None,r=0,op=1):
        X,Y=self.X(x),self.Y(y+h); W,H=self.X(w),self.X(h)
        da=f' stroke-dasharray="{dash}"' if dash else ''
        rr=f' rx="{r}"' if r else ''
        self.el.append(f'<rect x="{X:.1f}" y="{Y:.1f}" width="{W:.1f}" height="{H:.1f}" fill="{fill}" '
                       f'fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{da}{rr}/>')
        self._t(X,Y); self._t(X+W,Y+H)
    def ln(self,x1,y1,x2,y2,stroke=INK,sw=1.3,dash=None,cap='round'):
        X1,Y1,X2,Y2=self.X(x1),self.Y(y1),self.X(x2),self.Y(y2)
        da=f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{X2:.1f}" y2="{Y2:.1f}" stroke="{stroke}" '
                       f'stroke-width="{sw}"{da} stroke-linecap="{cap}"/>')
        self._t(X1,Y1); self._t(X2,Y2)
    def poly(self,pts,fill=W1,stroke=INK,sw=1.5,dash=None,op=1,close=True):
        P=[(self.X(a),self.Y(b)) for a,b in pts]
        s=' '.join(f'{a:.1f},{b:.1f}' for a,b in P)
        da=f' stroke-dasharray="{dash}"' if dash else ''
        tag='polygon' if close else 'polyline'
        f2='none' if not close else fill
        self.el.append(f'<{tag} points="{s}" fill="{f2}" fill-opacity="{op}" stroke="{stroke}" '
                       f'stroke-width="{sw}"{da} stroke-linejoin="round"/>')
        [self._t(a,b) for a,b in P]
    def circ(self,x,y,rpx,fill=INK,stroke='none',sw=1):
        X,Y=self.X(x),self.Y(y)
        self.el.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{rpx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        self._t(X-rpx,Y-rpx); self._t(X+rpx,Y+rpx)

    # ── hasura de sectiune ──
    def hatch(self,x,y,w,h,fill=W2,stroke=INK,sw=1.5,ang=45,gap=7,col=None,dense=False):
        """dreptunghi taiat in sectiune: fond + linii inclinate"""
        col=col or MUT
        i=uid('h')
        g=4 if dense else gap
        self.defs.append(
            f'<pattern id="{i}" width="{g}" height="{g}" patternTransform="rotate({ang})" patternUnits="userSpaceOnUse">'
            f'<line x1="0" y1="0" x2="0" y2="{g}" stroke="{col}" stroke-width="0.9" opacity="0.55"/></pattern>')
        self.bar(x,y,w,h,fill=fill,stroke=stroke,sw=sw)
        X,Y=self.X(x),self.Y(y+h)
        self.el.append(f'<rect x="{X:.1f}" y="{Y:.1f}" width="{self.X(w):.1f}" height="{self.X(h):.1f}" '
                       f'fill="url(#{i})" stroke="none"/>')
    def hatchpoly(self,pts,fill=W2,stroke=INK,sw=1.5,ang=45,gap=7,col=None):
        col=col or MUT; i=uid('h')
        self.defs.append(
            f'<pattern id="{i}" width="{gap}" height="{gap}" patternTransform="rotate({ang})" patternUnits="userSpaceOnUse">'
            f'<line x1="0" y1="0" x2="0" y2="{gap}" stroke="{col}" stroke-width="0.9" opacity="0.55"/></pattern>')
        self.poly(pts,fill=fill,stroke=stroke,sw=sw)
        P=' '.join(f'{self.X(a):.1f},{self.Y(b):.1f}' for a,b in pts)
        self.el.append(f'<polygon points="{P}" fill="url(#{i})" stroke="none"/>')

    # ── gol / necunoscut ──
    def void(self,x,y,w,h,label=None,col=WARN):
        """zona goala: fond palid + X pe diagonale + contur punctat"""
        self.bar(x,y,w,h,fill=VOID,stroke=col,sw=1.4,dash='6,4')
        self.ln(x,y,x+w,y+h,stroke=col,sw=0.9,dash='4,4')
        self.ln(x,y+h,x+w,y,stroke=col,sw=0.9,dash='4,4')
        if label: self.tx(x+w/2,y+h/2,label,fill=col,size=self.fs-2,weight='700')

    # ── text si adnotari ──
    def tx(self,x,y,s,size=None,fill=INK,anchor='middle',weight='400',rot=None,mono=True,px=False,op=1):
        size=size or self.fs
        X,Y=(x,y) if px else (self.X(x),self.Y(y))
        fam='ui-monospace,Menlo,monospace' if mono else 'system-ui,Helvetica,sans-serif'
        r=f' transform="rotate({rot} {X:.1f} {Y:.1f})"' if rot is not None else ''
        self.el.append(f'<text x="{X:.1f}" y="{Y:.1f}" font-family="{fam}" font-size="{size}" fill="{fill}" '
                       f'fill-opacity="{op}" text-anchor="{anchor}" font-weight="{weight}"{r}>{esc(s)}</text>')
        w=len(s)*size*0.58; dx={'middle':w/2,'start':0,'end':w}[anchor]
        if rot is None: self._t(X-dx,Y-size); self._t(X-dx+w,Y+size*0.4)
        else: self._t(X-size,Y-w/2); self._t(X+size,Y+w/2)

    def dimh(self,x1,x2,y,label=None,off=22,fill=DIM,size=None,ext=0):
        Y=self.Y(y)+off; X1,X2=self.X(x1),self.X(x2)
        if ext:
            for X in (X1,X2):
                self.el.append(f'<line x1="{X:.1f}" y1="{self.Y(y):.1f}" x2="{X:.1f}" y2="{Y+ (4 if off>0 else -4):.1f}" '
                               f'stroke="{fill}" stroke-width="0.7" opacity="0.6"/>')
        self.el.append(f'<line x1="{X1:.1f}" y1="{Y:.1f}" x2="{X2:.1f}" y2="{Y:.1f}" stroke="{fill}" stroke-width="1"/>')
        for X in (X1,X2):
            self.el.append(f'<line x1="{X:.1f}" y1="{Y-5:.1f}" x2="{X:.1f}" y2="{Y+5:.1f}" stroke="{fill}" stroke-width="1"/>')
        self._t(X1,Y-6); self._t(X2,Y+6)
        self.tx((X1+X2)/2,Y-7,label if label is not None else f'{round(x2-x1)}',size=size or self.fs-1,fill=fill,px=True)

    def dimv(self,y1,y2,x,label=None,off=-22,fill=DIM,size=None,ext=0):
        X=self.X(x)+off; Y1,Y2=self.Y(y1),self.Y(y2)
        if ext:
            for Y in (Y1,Y2):
                self.el.append(f'<line x1="{self.X(x):.1f}" y1="{Y:.1f}" x2="{X+(4 if off<0 else -4):.1f}" y2="{Y:.1f}" '
                               f'stroke="{fill}" stroke-width="0.7" opacity="0.6"/>')
        self.el.append(f'<line x1="{X:.1f}" y1="{Y1:.1f}" x2="{X:.1f}" y2="{Y2:.1f}" stroke="{fill}" stroke-width="1"/>')
        for Y in (Y1,Y2):
            self.el.append(f'<line x1="{X-5:.1f}" y1="{Y:.1f}" x2="{X+5:.1f}" y2="{Y:.1f}" stroke="{fill}" stroke-width="1"/>')
        self._t(X-6,Y1); self._t(X+6,Y2)
        self.tx(X-6,(Y1+Y2)/2,label if label is not None else f'{round(abs(y2-y1))}',
                size=size or self.fs-1,fill=fill,rot=-90,px=True)

    def note(self,x,y,s,dx=60,dy=-40,fill=MUT,anchor='start',size=None,weight='400',dot=True):
        X,Y=self.X(x),self.Y(y)
        self.el.append(f'<line x1="{X:.1f}" y1="{Y:.1f}" x2="{X+dx:.1f}" y2="{Y+dy:.1f}" stroke="{fill}" stroke-width="1"/>')
        if dot: self.el.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="2.6" fill="{fill}"/>')
        self.tx(X+dx+(5 if anchor=='start' else -5),Y+dy-3,s,fill=fill,anchor=anchor,
                size=size or self.fs-1,px=True,weight=weight)

    def notes(self,x,y,lines,dx=60,dy=-40,fill=MUT,anchor='start',size=None,lh=16):
        """acelasi leader, mai multe randuri"""
        X,Y=self.X(x),self.Y(y)
        self.el.append(f'<line x1="{X:.1f}" y1="{Y:.1f}" x2="{X+dx:.1f}" y2="{Y+dy:.1f}" stroke="{fill}" stroke-width="1"/>')
        self.el.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="2.6" fill="{fill}"/>')
        for i,s in enumerate(lines):
            self.tx(X+dx+(5 if anchor=='start' else -5), Y+dy-3+i*lh, s, fill=fill, anchor=anchor,
                    size=size or self.fs-1, px=True, weight='700' if i==0 else '400')

    def bule(self,x,y,n,fill=ACC2,rpx=11):
        """bula numerotata, ancorata pe desen"""
        X,Y=self.X(x),self.Y(y)
        self.el.append(f'<circle cx="{X:.1f}" cy="{Y:.1f}" r="{rpx}" fill="{fill}"/>')
        self.el.append(f'<text x="{X:.1f}" y="{Y+4.4:.1f}" font-family="ui-monospace,Menlo,monospace" '
                       f'font-size="{rpx*1.15:.0f}" fill="#fff" text-anchor="middle" font-weight="700">{n}</text>')
        self._t(X-rpx,Y-rpx); self._t(X+rpx,Y+rpx)

    def arrow(self,x1,y1,x2,y2,stroke=ACC2,sw=2,dash=None,head=7):
        X1,Y1,X2,Y2=self.X(x1),self.Y(y1),self.X(x2),self.Y(y2)
        a=math.atan2(Y2-Y1,X2-X1)
        da=f' stroke-dasharray="{dash}"' if dash else ''
        self.el.append(f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{X2-head*0.8*math.cos(a):.1f}" '
                       f'y2="{Y2-head*0.8*math.sin(a):.1f}" stroke="{stroke}" stroke-width="{sw}"{da} stroke-linecap="round"/>')
        p=[(X2,Y2),(X2-head*math.cos(a-0.4),Y2-head*math.sin(a-0.4)),(X2-head*math.cos(a+0.4),Y2-head*math.sin(a+0.4))]
        self.el.append('<polygon points="'+' '.join(f'{a2:.1f},{b:.1f}' for a2,b in p)+f'" fill="{stroke}"/>')
        self._t(X1,Y1); self._t(X2,Y2)

    def surub(self,x,y,ang,L,stroke=METAL2,sw=2.6,label=None,lsize=None,head=True):
        """surub desenat ca linie cu cap; ang in grade, 0 = spre dreapta, masurat in plan-desen"""
        a=math.radians(ang)
        X1,Y1=self.X(x),self.Y(y)
        X2,Y2=X1+self.X(L)*math.cos(a), Y1-self.X(L)*math.sin(a)
        self.el.append(f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{X2:.1f}" y2="{Y2:.1f}" stroke="{stroke}" '
                       f'stroke-width="{sw}" stroke-linecap="round"/>')
        if head:
            hx,hy=X1-3*math.cos(a),Y1+3*math.sin(a)
            self.el.append(f'<line x1="{hx-5*math.sin(a):.1f}" y1="{hy-5*math.cos(a):.1f}" '
                           f'x2="{hx+5*math.sin(a):.1f}" y2="{hy+5*math.cos(a):.1f}" stroke="{stroke}" stroke-width="{sw*1.1}" stroke-linecap="round"/>')
        # varf ascutit
        self.el.append(f'<polygon points="{X2:.1f},{Y2:.1f} {X2-6*math.cos(a-0.28):.1f},{Y2+6*math.sin(a-0.28):.1f} '
                       f'{X2-6*math.cos(a+0.28):.1f},{Y2+6*math.sin(a+0.28):.1f}" fill="{stroke}"/>')
        self._t(X1,Y1); self._t(X2,Y2)
        if label:
            self.tx((X1+X2)/2,(Y1+Y2)/2-9,label,size=lsize or self.fs-2,fill=stroke,px=True)

    def bracket(self,x,y,a,b,t=3,fill=METAL,stroke=METAL2,flip=False,sw=1.4):
        """vinclu in sectiune: L cu bratul vertical de a si cel orizontal de b, grosime t (mm).
        Coltul la (x,y). flip=False -> bratul orizontal spre +x, cel vertical in sus."""
        sx = 1 if not flip else -1
        pts=[(x,y),(x+sx*b,y),(x+sx*b,y+t),(x+sx*t,y+t),(x+sx*t,y+a),(x,y+a)]
        self.poly(pts,fill=fill,stroke=stroke,sw=sw)

    def title(self,s,sub=None,size=15):
        """bara de titlu deasupra desenului — se apeleaza LA FINAL, foloseste bbox curent"""
        x0,y0,x1,_=self.bb
        self.tx((x0+x1)/2, y0-14, s, size=size, fill=INK, weight='700', px=True)
        if sub: self.tx((x0+x1)/2, y0+4, sub, size=size-3, fill=MUT, px=True)

    def svg(self,pad=30,extra_top=0):
        x0,y0,x1,y1=self.bb
        y0-=extra_top
        dfs=('<defs>'+''.join(self.defs)+'</defs>') if self.defs else ''
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0-pad:.0f} {y0-pad:.0f} '
                f'{x1-x0+2*pad:.0f} {y1-y0+2*pad:.0f}" style="width:100%;height:auto;display:block">'
                +dfs+'\n'.join(self.el)+'</svg>')
