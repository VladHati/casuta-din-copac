# -*- coding: utf-8 -*-
import os
from iso import render, hframe, cam_window, PAL
from det import DETS
# Radacina proiectului = folderul parinte al lui tools-fise (robust pe orice masina).
PROJ=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PS=100;W=2100;D=1780
FRONTTOP=1872          # stalpii din fata, taiati la +1872 (top grinda fata sta pe ei)
BACKTOP=3260           # stalpii din spate desenati pana aici (real +4000, vezi eticheta)
BEAMB=1872; BEAMTOP=2072; JOB=2072; JOT=2172; DECKB=2172; DECKTOP=2200
RAIL=1000              # inaltimea balustradei deasupra dusumelei
JX=[100,280,720,1120,1550,1980]

def g(mat,x,y,z,dx,dy,dz): return {'x':x,'y':y,'z':z,'dx':dx,'dy':dy,'dz':dz,'mat':mat,'built':True}
def N(mat,x,y,z,dx,dy,dz,ex=None,code=None):
    d={'x':x,'y':y,'z':z,'dx':dx,'dy':dy,'dz':dz,'mat':mat,'hl':True}
    if ex:d['ex']=ex
    if code:d['code']=code
    return d
def bz(b): return dict(b,built=True,hl=False)         # marcheaza o piesa ca DEJA montata
def builts(*groups):
    out=[]
    for gp in groups: out+=[bz(b) for b in gp]
    return out

# ---- grupuri parametrice (un singur model care creste) -----------------------
def anchors(): return [g('anchor',x-12,0,z-12,PS+24,130,PS+24) for (x,z) in [(0,0),(W-PS,0),(0,D-PS),(W-PS,D-PS)]]
def posts_g(cut=True):
    """Un singur stalp parametric. Fata (z=0) taiat la +1872 dupa Fisa 2; spate (z=D-PS) raman lungi."""
    ft=FRONTTOP if cut else BACKTOP
    return [g('post',0,0,0,PS,ft,PS),g('post',W-PS,0,0,PS,ft,PS),
            g('post',0,0,D-PS,PS,BACKTOP,PS),g('post',W-PS,0,D-PS,PS,BACKTOP,PS)]
def polite_g(): return [g('polita',0,BEAMB-100,D-PS-90,PS,100,90),g('polita',W-PS,BEAMB-100,D-PS-90,PS,100,90)]
def beam_back_g(): return g('beam',0,BEAMB,D-90,W,200,90)
def beam_front_g(): return g('beam',0,BEAMB,0,W,200,90)
def joists_g(xs=JX): return [g('joist',x,JOB,-700,PS,PS,D+700) for x in xs]
def headers_g(): return [g('joist',280,JOB,-300,440,PS,PS),g('joist',280,JOB,-120,440,PS,PS)]
def tree_g():
    # spart la nivelul dusumelei: partea de sub podea + partea care iese (deseneaza corect prin podea)
    return [g('tree',450,1280,-300,160,DECKTOP-1280,160),g('tree',450,DECKTOP,-300,160,2780-DECKTOP,160)]
def block_g(): return [g('block',JX[i]+PS,JOB,-40,JX[i+1]-JX[i]-PS,PS,90) for i in range(len(JX)-1)]
def deck_g(n=17):
    out=[];z=-700
    for i in range(n): out.append(g('deck',-20,DECKB,z,W+40,28,140)); z+=150
    return out
GROUND=(-220,W+220,-220,D+220)
BR=PAL['brace']; WD=PAL['post']

# proptele temporare (struts)
props=[{'p1':(50,820,50),'p2':(-470,0,50),'thick':12,'col':BR},
       {'p1':(50,820,50),'p2':(50,0,-470),'thick':12,'col':BR},
       {'p1':(W-50,820,50),'p2':(W+470,0,50),'thick':12,'col':BR},
       {'p1':(W-50,820,50),'p2':(W-50,0,-470),'thick':12,'col':BR},
       {'p1':(50,1750,D-50),'p2':(50,0,D+470),'thick':12,'col':BR},
       {'p1':(W-50,1750,D-50),'p2':(W-50,0,D+470),'thick':12,'col':BR}]
# contravantuiri (struts)
braces=[{'p1':(55,BEAMB+170,30),'p2':(55,BEAMB-360,560),'thick':13,'col':BR},
        {'p1':(W-55,BEAMB+170,30),'p2':(W-55,BEAMB-360,560),'thick':13,'col':BR},
        {'p1':(40,BEAMB+170,8),'p2':(560,BEAMB-360,8),'thick':13,'col':BR},
        {'p1':(300,JOB-10,-660),'p2':(300,BEAMB-200,-30),'thick':13,'col':BR}]
# balustrada (struts): stalpisori + mana curenta, jur-imprejur (inclusiv nasul consolei)
RTOP=DECKTOP+RAIL
RPOSTS=[(20,-680),(W-20,-680),(20,D-20),(W-20,D-20),(1040,-680)]
rail_posts=[{'p1':(x,DECKTOP,z),'p2':(x,RTOP,z),'thick':14,'col':WD} for (x,z) in RPOSTS]
rail_top=[{'p1':(20,RTOP,-680),'p2':(W-20,RTOP,-680),'thick':11,'col':WD},
          {'p1':(20,RTOP,D-20),'p2':(W-20,RTOP,D-20),'thick':11,'col':WD},
          {'p1':(20,RTOP,-680),'p2':(20,RTOP,D-20),'thick':11,'col':WD},
          {'p1':(W-20,RTOP,-680),'p2':(W-20,RTOP,D-20),'thick':11,'col':WD}]

# ---- CAMERA: scara FIXA (un singur sc + minx din ansamblul final), panoramata pe inaltime.
# Doua ferestre verticale, ACELASI scale: una pentru fundatie (Fisa 1-2, vede solul si toata
# inaltimea stalpilor), una pentru platforma (Fisa 3-11, picioarele lungi ies din cadru jos).
FULL=anchors()+posts_g()+polite_g()+[beam_back_g(),beam_front_g()]+joists_g()+headers_g()+tree_g()+block_g()+deck_g(17)
ALLSTR=props+braces+rail_posts+rail_top
WV=1000; PADV=84
MINX,SC=hframe(FULL,struts=ALLSTR,W=WV,pad=PADV)
XR=(-90,W+90); ZR=(-770,D+90)
CAM_BASE=cam_window((XR[0],XR[1],0,2380,ZR[0],ZR[1]),MINX,SC,W=WV,pad=PADV)
CAM_PLAT=cam_window((XR[0],XR[1],1180,3360,ZR[0],ZR[1]),MINX,SC,W=WV,pad=PADV)
def F(boxes,cam=None,**kw): return render(boxes,cam=cam if cam is not None else CAM_PLAT,**kw)

# ===== zoom-uri / scheme 2D (pentru pasii fara izometrie) =====================
Z_ANCHOR='''<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
<rect x="120" y="10" width="60" height="120" fill="#E8973C" stroke="#161413" stroke-width="2.6"/>
<path d="M108 130 v40 h84 v-40" fill="none" stroke="#161413" stroke-width="3.2"/>
<rect x="108" y="168" width="84" height="14" fill="#94A0AB" stroke="#161413" stroke-width="2.2"/>
<text x="150" y="196" text-anchor="middle" font-family="Space Mono,monospace" font-size="11" fill="#5C574E">papuc in beton</text>
<circle cx="118" cy="150" r="5" fill="#161413"/><circle cx="182" cy="150" r="5" fill="#161413"/>
<rect x="196" y="142" width="48" height="19" rx="4" fill="#161413"/><text x="220" y="156" text-anchor="middle" fill="#fff" font-size="12" font-weight="700" font-family="Space Mono,monospace">B2 x2</text></svg>'''
# Fisa 3 / pas: gaureste 2 gauri in polita
Z_DRILL='''<svg viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg" font-family="Space Grotesk,Arial">
<rect x="40" y="20" width="70" height="170" fill="#E8973C" stroke="#161413" stroke-width="2.6"/><text x="75" y="206" text-anchor="middle" font-family="Space Mono,monospace" font-size="11" fill="#5C574E">stalp spate</text>
<rect x="110" y="70" width="96" height="74" fill="#B083C6" stroke="#161413" stroke-width="2.6"/><text x="158" y="160" text-anchor="middle" font-family="Space Mono,monospace" font-size="11" fill="#5C574E">polita</text>
<circle cx="150" cy="92" r="7" fill="#fff" stroke="#161413" stroke-width="2.4"/><circle cx="150" cy="122" r="7" fill="#fff" stroke="#161413" stroke-width="2.4"/>
<line x1="206" y1="92" x2="300" y2="78" stroke="#C2693A" stroke-width="3"/><path d="M300 78 l-12 -2 m12 2 l-9 8" stroke="#C2693A" stroke-width="3" fill="none"/>
<rect x="278" y="60" width="56" height="20" rx="4" fill="#C2693A"/><text x="306" y="74" text-anchor="middle" fill="#fff" font-size="12" font-weight="700" font-family="Space Mono,monospace">Ø13</text>
<text x="240" y="130" font-family="Space Grotesk" font-size="12" fill="#5C574E">2 gauri strapunse</text></svg>'''
# Fisa 8 / pas: taie blocajul la masura intre joiste
Z_CUTBLOC='''<svg viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg" font-family="Space Grotesk,Arial">
<rect x="40" y="40" width="38" height="130" fill="#7BAE52" stroke="#161413" stroke-width="2.6"/><rect x="262" y="40" width="38" height="130" fill="#7BAE52" stroke="#161413" stroke-width="2.6"/>
<text x="59" y="32" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">joista</text><text x="281" y="32" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">joista</text>
<rect x="100" y="92" width="140" height="40" fill="#CBA24B" stroke="#161413" stroke-width="2.6"/><text x="170" y="118" text-anchor="middle" font-family="Space Grotesk" font-size="14" fill="#161413">BL</text>
<line x1="78" y1="150" x2="262" y2="150" stroke="#C2693A" stroke-width="1.8"/><line x1="78" y1="144" x2="78" y2="156" stroke="#C2693A" stroke-width="1.8"/><line x1="262" y1="144" x2="262" y2="156" stroke="#C2693A" stroke-width="1.8"/>
<rect x="146" y="140" width="48" height="20" rx="4" fill="#fff" stroke="#C2693A" stroke-width="1.4"/><text x="170" y="155" text-anchor="middle" fill="#C2693A" font-size="12" font-weight="700" font-family="Space Mono,monospace">la fix</text>
<line x1="226" y1="70" x2="250" y2="58" stroke="#161413" stroke-width="3"/><text x="250" y="54" font-family="Space Grotesk" font-size="11" fill="#5C574E">taie pe masura</text></svg>'''
# Fisa 10 / pas: distantier 5 mm intre scanduri
Z_SPACER='''<svg viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg" font-family="Space Grotesk,Arial">
<rect x="30" y="120" width="280" height="26" fill="#7BAE52" stroke="#161413" stroke-width="2.4"/><text x="48" y="140" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">joista</text>
<rect x="40" y="64" width="120" height="40" rx="3" fill="#E9C277" stroke="#161413" stroke-width="2.6"/><rect x="178" y="64" width="120" height="40" rx="3" fill="#E9C277" stroke="#161413" stroke-width="2.6"/>
<rect x="164" y="60" width="10" height="48" fill="#AAB2BB" stroke="#161413" stroke-width="2"/>
<line x1="160" y1="50" x2="178" y2="50" stroke="#C2693A" stroke-width="2"/><line x1="160" y1="46" x2="160" y2="54" stroke="#C2693A" stroke-width="2"/><line x1="178" y1="46" x2="178" y2="54" stroke="#C2693A" stroke-width="2"/>
<rect x="146" y="26" width="46" height="20" rx="4" fill="#C2693A"/><text x="169" y="40" text-anchor="middle" fill="#fff" font-size="12" font-weight="700" font-family="Space Mono,monospace">5 mm</text>
<text x="169" y="178" text-anchor="middle" font-family="Space Grotesk" font-size="11.5" fill="#5C574E">un cui ca distantier, apoi insurubezi</text></svg>'''
# Fisa 10 / pas: ulei pe dusumea
Z_OIL='''<svg viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg" font-family="Space Grotesk,Arial">
<rect x="30" y="110" width="280" height="40" rx="3" fill="#E9C277" stroke="#161413" stroke-width="2.6"/><text x="40" y="170" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">dusumea larice</text>
<g stroke="#C99A5E" stroke-width="4" stroke-linecap="round"><line x1="60" y1="124" x2="120" y2="124"/><line x1="150" y1="134" x2="210" y2="134"/><line x1="230" y1="124" x2="290" y2="124"/></g>
<rect x="150" y="40" width="36" height="46" rx="3" fill="#5C574E" stroke="#161413" stroke-width="2.4"/><rect x="160" y="28" width="16" height="14" fill="#5C574E" stroke="#161413" stroke-width="2.2"/>
<rect x="120" y="84" width="70" height="12" rx="3" fill="#A56B41" stroke="#161413" stroke-width="2.2"/><text x="200" y="62" font-family="Space Mono,monospace" font-size="11" fill="#C2693A">ulei tec F1</text>
<text x="100" y="60" font-family="Space Grotesk" font-size="12" fill="#5C574E">DUPA montaj</text></svg>'''
# Fisa 11 / pas POARTA: unde pe latura S3
Z_GATE='''<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" font-family="Space Grotesk,Arial">
<text x="180" y="18" text-anchor="middle" font-family="Space Mono,monospace" font-size="11" fill="#5C574E">latura S3 (unde urca scara) — vedere din fata</text>
<line x1="20" y1="150" x2="340" y2="150" stroke="#E9C277" stroke-width="10"/>
<g stroke="#E8973C" stroke-width="11" stroke-linecap="round"><line x1="34" y1="60" x2="34" y2="150"/><line x1="134" y1="60" x2="134" y2="150"/><line x1="226" y1="60" x2="226" y2="150"/><line x1="326" y1="60" x2="326" y2="150"/></g>
<line x1="34" y1="64" x2="134" y2="64" stroke="#E8973C" stroke-width="8"/><line x1="226" y1="64" x2="326" y2="64" stroke="#E8973C" stroke-width="8"/>
<g stroke="#161413" stroke-width="2"><line x1="58" y1="68" x2="58" y2="150"/><line x1="82" y1="68" x2="82" y2="150"/><line x1="106" y1="68" x2="106" y2="150"/><line x1="250" y1="68" x2="250" y2="150"/><line x1="274" y1="68" x2="274" y2="150"/><line x1="298" y1="68" x2="298" y2="150"/></g>
<rect x="150" y="70" width="60" height="80" fill="#FBEEE4" stroke="#C2693A" stroke-width="2.4" stroke-dasharray="6 5"/>
<text x="180" y="116" text-anchor="middle" font-family="Space Mono,monospace" font-size="13" font-weight="700" fill="#C2693A">POARTA</text>
<text x="84" y="190" text-anchor="middle" font-family="Space Grotesk" font-size="11" fill="#5C574E">travee fixa, goluri &lt;9 cm</text>
<text x="276" y="190" text-anchor="middle" font-family="Space Grotesk" font-size="11" fill="#5C574E">travee fixa</text></svg>'''
print("scheme 2D ok")

# ===== etapele (single growing model) =========================================
def stage1():
    A=anchors()
    P=posts_g(cut=False)  # toti 4 lungi (taierea fetei vine la Fisa 2)
    pl=[N('post',0,0,D-PS,PS,BACKTOP,PS,ex=(0,650,0),code='ST'),N('post',W-PS,0,D-PS,PS,BACKTOP,PS),
        N('post',0,0,0,PS,BACKTOP,PS),N('post',W-PS,0,0,PS,BACKTOP,PS)]
    s1=F(A+pl,ground=GROUND,labels=[{'t':'spate S1·S2 (4 m)','at':(W+260,1900,D-50),'color':'#5C574E'},
                                    {'t':'fata S3·S4','at':(W+150,900,40),'color':'#5C574E'}])
    s3=F(A+P,ground=GROUND,dims=[{'p1':(0,0,-PS),'p2':(0,1500,-PS),'t':'PLUMB'}])
    s4=F(A+P,struts=props,ground=GROUND,labels=[{'t':'proptele PT','at':(-360,500,50),'color':BR}])
    return [dict(t='Aseaza toti 4 stalpii in papucii lor din beton, coborati drept in U. TOTI raman lungi acum — fata o tai la Fisa 2.',svg=s1,warn=None),
            dict(t='Adu fiecare stalp perfect vertical (la plumb), verificat pe doua fete cu bolobocul.',svg=s3,warn=None),
            dict(t='Sprijina fiecare stalp cu 2 proptele la baza. La cei 2 stalpi inalti din spate, pune si cate o proptea spre varf.',svg=s4,
                 warn='Verifica fiecare stalp la plumb pe 2 fete inainte de a strange proptelele.'),
            dict(t='Prinde suruburile B2 in papuc DOAR slab (2 / stalp) — sa poti inca corecta. Le strangi la Fisa 2.',svg=None,zoom=DETS['B2'],warn=None)]
def stage2():
    A=anchors(); Plong=posts_g(cut=False)
    s1=F(builts(A)+Plong,dims=[{'p1':(0,0,-PS),'p2':(0,2200,-PS),'t':'+2200 podea'}])
    s2=F(builts(A)+Plong,dims=[{'p1':(0,BEAMB,-PS),'p2':(0,2200,-PS),'t':'328'}],
         labels=[{'t':'+1872 talpa grinzii','at':(-340,BEAMB,0),'color':'#C2693A'}])
    off=[N('post',0,FRONTTOP,0,PS,BACKTOP-FRONTTOP,PS,ex=(0,360,0),code='offcut'),
         N('post',W-PS,FRONTTOP,0,PS,BACKTOP-FRONTTOP,PS,ex=(0,360,0))]
    Pcut=posts_g(cut=True)
    s3=F(builts(A,[Pcut[2],Pcut[3]])+[bz(Pcut[0]),bz(Pcut[1])]+off,
         labels=[{'t':'taie la +1872','at':(-300,FRONTTOP,0),'color':'#C2693A'}])
    return [dict(t='Marcheaza +2200 (fata podelei) pe toti 4 stalpii. Foloseste o scandura dreapta + boloboc, nu masura separat fiecare.',svg=s1,warn=None),
            dict(t='Coboara 328 mm si marcheaza +1872 — aici sta talpa GRINZII. Grinda 200 + joista 100 + dusumea 28 = 328, asa ajungi la +2200.',svg=s2,
                 warn='Linia +1872 trebuie identica pe toti 4 stalpii.'),
            dict(t='Taie DOAR stalpii din fata (S3, S4) la +1872. Partea taiata o pastrezi pentru polite. Stalpii din spate raman INTREGI.',svg=s3,
                 warn='Taie doar fata. Stalpii din spate raman intregi — ei sunt stalpii Fazei 2.'),
            dict(t='Teseste muchia taiata. Abia acum strange definitiv suruburile B2 de la baza.',svg=None,zoom=DETS['B2'],warn=None)]
def stage3():
    A=anchors(); P=posts_g()
    base=builts(A,P)
    s1=F(base+[N('polita',0,BEAMB-100,D-PS-90,PS,100,90,ex=(-650,0,0),code='PO')],
         dims=[{'p1':(0,BEAMB,D-PS-90),'p2':(0,BEAMB,D-PS),'t':'sus +1872'}])
    s3=F(base+polite_g(),screws=[{'at':(40,BEAMB-45,D-PS-90),'dir':(0,0,1),'code':'B1','n':2,'len':150},
                                 {'at':(W-PS+55,BEAMB-45,D-PS-90),'dir':(0,0,1),'code':'B1','n':2,'len':150}])
    return [dict(t='Aseaza polita (bloc 100x100 din offcut) pe fata interioara a stalpului din spate, cu fata de sus la +1872.',svg=s1,warn=None),
            dict(t='Gaureste prin polita in stalp: 2 gauri strapunse de 13 mm pe fiecare polita.',svg=Z_DRILL,warn=None),
            dict(t='Bate 2 buloane M12 (B1) cu saiba (B3) prin polita in stalp; strange cu piulita (B4) pe spate. Repeta la al doilea stalp.',svg=s3,zoom=DETS['B1'],
                 warn='Strange buloanele M12 pana polita nu se mai misca deloc.')]
def stage4():
    A=anchors(); P=posts_g()
    base=builts(A,P,polite_g())
    s1=F(base+[N('beam',0,BEAMB,D-90,W,200,90,ex=(0,700,0),code='GR')])
    s2=F(base+[N('beam',0,BEAMB,D-90,W,200,90)],
         dims=[{'p1':(W,BEAMB,D-45),'p2':(W,BEAMTOP,D-45),'t':'sus +2072'}],
         screws=[{'at':(60,BEAMB+150,D-95),'dir':(0,0,-1),'code':'H1','len':150}])
    return [dict(t='Ridicati in DOI grinda din spate si asezati-o pe cele doua polite. Sta pe polita — nu o tineti voi.',svg=s1,
                 warn='Grinda sta pe polite; nu o tineti voi cat o prindeti.'),
            dict(t='Verifica fata de sus la +2072 si orizontalitatea pe toata lungimea.',svg=s2,warn=None),
            dict(t='Prinde grinda de fiecare stalp cu 3 suruburi H1 oblice PLUS un coltar C2 anti-smulgere in stalp si in grinda. Grinda nu trebuie sa se poata ridica de pe polita.',svg=None,zoom=DETS['H1B'],
                 warn='Coltar C2 anti-smulgere la fiecare capat — grinda spate nu se poate ridica de pe polita.')]
def stage5():
    A=anchors(); P=posts_g()
    base=builts(A,P,polite_g(),[beam_back_g()])
    s1=F(base+[N('beam',0,BEAMB,0,W,200,90,ex=(0,700,0),code='GR')])
    C1=[N('metal',0,BEAMB,-12,130,40,114,code='C1'),N('metal',W-130,BEAMB,-12,130,40,114)]
    s2=F(base+[beam_front_g()]+C1,screws=[{'at':(60,BEAMB+120,5),'dir':(0,-1,0),'code':'H2','len':150}],
         dims=[{'p1':(W,BEAMTOP,45),'p2':(W,BEAMTOP,D-45),'t':'ambele +2072'}])
    return [dict(t='Asezati grinda din fata PE varful stalpilor S3/S4 (taiati). Sprijin direct pe lemn, la +1872.',svg=s1,
                 warn='Sprijin direct pe varful taiat la +1872, perfect orizontal.'),
            dict(t='Prinde cu cate un coltar C1 pe fiecare fata (2/stalp) + suruburi H2 in stalp si in grinda.',svg=s2,zoom=DETS['C1'],warn=None),
            dict(t='Verifica: ambele grinzi orizontale, varful la +2072. Ai cadrul de baza.',svg=None,
                 warn='Ambele grinzi la +2072, perfect orizontale, inainte de a continua.')]
def stage6():
    A=anchors(); P=posts_g()
    base=builts(A,P,polite_g(),[beam_back_g(),beam_front_g()])
    s1=F(base,labels=[{'t':str(x),'at':(x,BEAMTOP+300+(i%2)*230,0),'to':(x,BEAMTOP,0),'color':'#C2693A'} for i,x in enumerate(JX)])
    s2=F(base+[N('joist',100,JOB,-700,PS,PS,D+700,code='JO')],
         dims=[{'p1':(100,JOB,-700),'p2':(100,JOB,0),'t':'700 consola'}],
         arrows=[{'p1':(150,JOB+620,-350),'p2':(150,JOB+130,-350)}])
    s3=F(base+[N('joist',x,JOB,-700,PS,PS,D+700) for x in JX])
    s4=F(builts(A,P,polite_g(),[beam_back_g(),beam_front_g()],joists_g()),
         screws=[{'at':(150,JOT,5),'dir':(0,-1,0),'code':'C2','n':2,'len':150}])
    return [dict(t='Marcheaza pe ambele grinzi pozitiile celor 6 joiste, de la coltul S4: 100 / 280 / 720 / 1120 / 1550 / 1980 mm.',svg=s1,warn=None),
            dict(t='Aseaza prima joista peste ambele grinzi, la pozitia 100. Capatul din fata iese 700 mm in gol — asta e consola (balconul).',svg=s2,
                 warn='Consola de 700 mm trebuie egala la toate joistele.'),
            dict(t='Aseaza toate cele 6 joiste la pozitiile marcate. Fiecare reazema pe AMBELE grinzi.',svg=s3,warn=None),
            dict(t='La FIECARE reazem (fata + spate) prinde un coltar C2 pe lateral — 12 in total. Tine joista jos la consola.',svg=s4,zoom=DETS['C2'],
                 warn='Coltar C2 la fiecare reazem, fata si spate. Niciun reazem nelegat.')]
def stage7():
    A=anchors(); P=posts_g()
    base=builts(A,P,polite_g(),[beam_back_g(),beam_front_g()],joists_g())
    ram=[N('joist',280,JOB,-300,440,PS,PS,code='RM'),N('joist',280,JOB,-120,440,PS,PS)]
    s1=F(base+ram,dims=[{'p1':(280,JOB,-210),'p2':(720,JOB,-210),'t':'gaura copac'}])
    tree=[N('tree',450,1280,-300,160,DECKTOP-1280,160),N('tree',450,DECKTOP,-300,160,2780-DECKTOP,160,code='copac')]
    s2=F(base+tree,labels=[{'t':'reteaza la +2780','at':(450,2880,-220),'color':'#C2693A'}])
    return [dict(t='Intre joistele de la 280 si 720 — trunchiul cade chiar intre ele, fara sa le atinga — monteaza 2 traverse scurte (RM) care inchid rama gaurii.',svg=s1,warn=None),
            dict(t='Reteaza corcodusul la ~+2780 de la sol (≈580 peste podea). Lasa joc de 3-5 cm jur-imprejurul trunchiului.',svg=s2,
                 warn='Joc de 3-5 cm in jurul trunchiului — copacul se misca in vant.'),
            dict(t='Blatul mesei se fixeaza de podea, prin cadrul lui — NICIODATA de copac.',svg=None,zoom=DETS['TABLE'],
                 warn='Blatul se prinde de cadrul lui propriu, NICIODATA de copac.')]
def stage8():
    A=anchors(); P=posts_g()
    base=builts(A,P,polite_g(),[beam_back_g(),beam_front_g()],joists_g())
    bl=[N('block',JX[i]+PS,JOB,-40,JX[i+1]-JX[i]-PS,PS,90,code=('BL' if i==0 else None)) for i in range(len(JX)-1)]
    s2=F(base+bl)
    return [dict(t='Taie bucati scurte de lemn (blocaje, BL) exact cat distanta dintre joiste.',svg=Z_CUTBLOC,warn=None),
            dict(t='Pune cate un blocaj intre joiste, PESTE fiecare grinda (fata si spate).',svg=s2,warn=None),
            dict(t='Prinde fiecare blocaj cu suruburi H3 oblic. Opresc joistele sa se rasuceasca — podeaua devine ferma.',svg=None,zoom=DETS['H3'],warn=None)]
def stage9():
    A=anchors(); P=posts_g()
    base=builts(A,P,polite_g(),[beam_back_g(),beam_front_g()],joists_g(),block_g())
    s2=F(base,struts=braces,labels=[{'t':'contrafise CF','at':(-360,500,300),'color':BR}])
    s4=F(base,struts=[{'p1':(50,1750,D-50),'p2':(50,900,D+470),'thick':12,'col':BR},
                      {'p1':(W-50,1750,D-50),'p2':(W-50,900,D+470),'thick':12,'col':BR}],
         labels=[{'t':'doar la varf RAMAN','at':(W+200,1820,D+300),'color':'#C2693A'}])
    return [dict(t='Masoara si taie capatul fiecarei contrafise (diagonala) pe potriveala.',svg=None,zoom=DETS['CF'],warn=None),
            dict(t='Monteaza contravantuirile in planul stang, drept, fata si sub nasul consolei. La contrafisa de sub nas prinde-o pe LATERAL sau adauga un coltar — acolo lucreaza la intindere. Platforma devine rigida.',svg=s2,
                 warn='Contrafisele prinse la AMBELE capete inainte de a scoate proptelele.'),
            dict(t='Prinde fiecare capat cu 3 suruburi H1.',svg=None,zoom=DETS['CF'],warn=None),
            dict(t='SCOATE proptelele de la baza. Cele de la varful stalpilor inalti din spate RAMAN pana la peretii din Faza 2.',svg=s4,
                 warn='Scoti doar proptelele de la baza; cele de la varful stalpilor spate raman pana in Faza 2.')]
def stage10():
    A=anchors(); P=posts_g()
    base=builts(A,P,polite_g(),[beam_back_g(),beam_front_g()],joists_g(),block_g())
    s1=F(base+[N('deck',-20,DECKB,-700,W+40,28,140,ex=(0,420,0),code='DL')],
         screws=[{'at':(120,DECKB+28,-630),'dir':(0,-1,0),'code':'H4','n':2,'len':140}])
    s3=F(base+[bz(b) for b in deck_g(17)],labels=[{'t':'decupaj la copac','at':(450,DECKTOP+360,-220),'color':'#C2693A'}])
    return [dict(t='Aseaza prima scandura la marginea din fata, perpendicular pe joiste. 2 suruburi inox (H4) pe fiecare joista.',svg=s1,zoom=DETS['H4'],warn=None),
            dict(t='Lasa 5 mm intre scanduri (pune un cui ca distantier). Apa se scurge, lemnul respira.',svg=Z_SPACER,
                 warn='Gol egal de 5 mm intre toate scandurile.'),
            dict(t='Continua pana acoperi tot — toate 17 scandurile ajung la grinda din spate. La copac, taie scandurile in jurul gaurii, cu joc.',svg=s3,warn=None),
            dict(t='Dupa montaj, da cu ulei (F1) pe toata dusumeaua de larice.',svg=Z_OIL,warn=None)]
def stage11():
    A=anchors(); P=posts_g()
    base=builts(A,P,polite_g(),[beam_back_g(),beam_front_g()],joists_g(),block_g(),deck_g(17))
    s1=F(base,struts=rail_posts)
    s2=F(base,struts=rail_posts+rail_top,dims=[{'p1':(20,DECKTOP,-680),'p2':(20,RTOP,-680),'t':'1 m'}])
    return [dict(t='Monteaza stalpisorii balustradei (SB, 58x58), bulonati de CADRU (joiste/grinda), nu de dusumea. Jur-imprejur, inclusiv pe nasul consolei.',svg=s1,zoom=DETS['RAIL'],
                 warn='Stalpisorii se prind de cadru (joiste/grinda), nu de dusumea.'),
            dict(t='Pune mana curenta sus, la 1 m inaltime, pe tot conturul.',svg=s2,zoom=DETS['RAIL'],
                 warn='Mana curenta exact la 1 m, pe tot conturul.'),
            dict(t='Umple cu sipci (SP), cu goluri sub 9 cm (un copil nu trebuie sa incapa sau sa se catere usor).',svg=None,zoom=DETS['RAIL'],
                 warn='Goluri sub 9 cm peste tot.'),
            dict(t='Lasa o poarta pe partea S3 (opusa mesei-copac), unde urca scara. Testeaza balustrada impingand cu putere.',svg=Z_GATE,
                 warn='Poarta pe S3; testeaza toata balustrada impingand cu putere.')]

META=[
 (1,'fisa-01','FISA 1 / 11','Stalpii in papuci','2-3 ore',True,'Mediu',[('ST','4','la lungime mare, NU taia'),('PAP','4','deja in beton'),('B2','8','2 / stalp'),('PT','~6','proptele')],['Cheie 19 (M12)','Boloboc','Bormasina','2 persoane'],['Toti 4 stalpii verticali pe 2 fete','Proptele la fiecare stalp','Suruburi inca slabe']),
 (2,'fisa-02','FISA 2 / 11','Nivel +2200 si taiere stalpi fata','1-2 ore',False,'CRITIC',[('ST','—','doar cei 2 din fata se taie')],['Nivela cu furtun / laser','Creion','Fierastrau','Echer'],['Linia +1872 identica pe toti','Doar stalpii fata taiati','Stalpii spate INTREGI','Suruburi baza stranse']),
 (3,'fisa-03','FISA 3 / 11','Polite pe stalpii din spate','1 ora',False,'CRITIC',[('PO','2','offcut 100x100'),('B1','4','tija ~220'),('B3','8','2 / bulon: cap + piulita'),('B4','4','piulite')],['Bormasina + burghiu 13','Cheie 19','Bomfaier'],['Ambele polite sus la +1872','2 buloane stranse / polita','Polita nu se misca']),
 (4,'fisa-04','FISA 4 / 11','Grinda din spate pe polite','1 ora',True,'CRITIC',[('GR','1','grinda spate'),('C2','2','coltar anti-smulgere'),('H1','6','3 oblice / capat')],['2 persoane','Bormasina','Nivela'],['Grinda pe ambele polite','Fata sus la +2072','Coltar anti-smulgere la fiecare capat','Buloane polita REVERIFICATE dupa asezarea grinzii']),
 (5,'fisa-05','FISA 5 / 11','Grinda din fata pe varful stalpilor','1 ora',True,'CRITIC',[('GR','1','grinda fata'),('C1','4','2 / stalp'),('H2','~12','in coltare')],['2 persoane','Bormasina','Nivela'],['Grinda pe varful stalpilor','2 coltare C1 / stalp','Ambele grinzi la +2072']),
 (6,'fisa-06','FISA 6 / 11','Cele 6 joiste','2 ore',True,'CRITIC',[('JO','6','dintr-o bucata'),('C2','12','2 / joista'),('H2','~60','in coltare')],['Bormasina','Ruleta','Creion','Echer'],['6 joiste la pozitii','Consola 700 mm','12 coltare C2']),
 (7,'fisa-07','FISA 7 / 11','Gaura copacului si masa','1-2 ore',False,'Atentie',[('RM','2','traverse = rama gaurii'),('H3','~6','prindere')],['Fierastrau','Bormasina','Ruleta'],['Rama intre joistele 280-720','Joc 3-5 cm in jurul trunchiului','Blatul NU pe copac']),
 (8,'fisa-08','FISA 8 / 11','Blocaje intre joiste','1 ora',False,'Normal',[('BL','~10','offcut'),('H3','~20','oblic')],['Fierastrau','Bormasina'],['Blocaje peste ambele grinzi','Prinse oblic cu H3','Podeaua e ferma']),
 (9,'fisa-09','FISA 9 / 11','Contravantuiri si scoatem proptelele','2 ore',False,'CRITIC',[('CF','6','diagonale'),('H1','~18','3 / capat')],['Fierastrau','Bormasina','Echer'],['Diagonale pe toate planurile + sub consola','3 suruburi / capat','Proptele baza scoase; varf raman']),
 (10,'fisa-10','FISA 10 / 11','Dusumeaua de larice','3-4 ore',False,'Normal',[('DL','17','larice 28x145'),('H4','~204','2 / joista'),('F1','2','ulei')],['Bormasina','Cui distantier 5 mm','Pensula'],['Toate scandurile cu 2 H4 / joista','Gol egal de 5 mm','Decupaj la copac','Uns cu ulei']),
 (11,'fisa-11','FISA 11 / 11','Balustrada si poarta','3-4 ore',False,'CRITIC',[('SB','~7','stalpisor 58x58, de cadru'),('SP','~24','sipci, gol <9 cm'),('MC','~7 m','mana curenta sus'),('BM','~12','bulon M10 in cadru')],['Bormasina','Nivela','Fierastrau'],['Mana curenta la 1 m de la dusumea','Goluri sub 9 cm peste tot','Poarta pe S3','Stalpisori bulonati de cadru, testati prin impingere']),
]
STEPFN={1:stage1,2:stage2,3:stage3,4:stage4,5:stage5,6:stage6,7:stage7,8:stage8,9:stage9,10:stage10,11:stage11}
import pickle
DATA=[dict(n=n,slug=sl,kick=k,title=ti,time=tm,ppl=pp,diff=df,parts=pa,tools=to,check=ch,steps=STEPFN[n]()) for (n,sl,k,ti,tm,pp,df,pa,to,ch) in META]
pickle.dump(DATA,open('data.pkl','wb'))
print('DATA color gata:',len(DATA),'pasi',sum(len(d['steps']) for d in DATA))

PARTS={'ST':('POZE/COD_7337253.png','Stalp KVH 100x100'),'GR':('POZE/COD_5483835.png','Grinda glulam 90x200'),
 'JO':('POZE/COD_7337253.png','Joista 100x100'),'DL':('POZE/COD_6224073.png','Dusumea larice 28x145'),
 'PO':('POZE/lemn.png','Polita (offcut)'),'BL':('POZE/lemn.png','Blocaj (offcut)'),'CF':('POZE/lemn.png','Contrafisa (offcut)'),
 'PT':('POZE/lemn.png','Proptea temporara'),'C1':('POZE/COD_738965.png','Coltar 100x100x90'),'C2':('POZE/COD_738910.png','Coltar 90x90x65'),
 'H1':('POZE/COD_10434633.png','Heco 8x200'),'H2':('POZE/COD_10434398.png','Heco 6x100'),'H3':('POZE/COD_10434139.png','Heco 6x80'),
 'H4':('POZE/COD_10528829.png','Inox 5x60'),'B1':('POZE/COD_12130958.png','Tija M12 (taie 220)'),'B2':('POZE/COD_6834285.png','Bulon M12x120'),
 'B3':('POZE/COD_3840897.png','Saiba M12'),'B4':('POZE/COD_3830642.png','Piulita M12'),'F1':('POZE/COD_5509678.png','Ulei tec'),'PAP':('POZE/papuc.svg','Papuc reazem U'),'SB':('POZE/lemn.png','Stalpisor 58x58'),'SP':('POZE/lemn.png','Sipci balustrada'),'MC':('POZE/lemn.png','Mana curenta'),'BM':('POZE/bolt-m10.svg','Bulon M10'),'RM':('POZE/lemn.png','Traverse rama'),'F2':('POZE/kober.jpg','Grund Köber'),'F3':('POZE/lemn.png','Topcoat colorat')}
