# -*- coding: utf-8 -*-
from iso import render, PAL
from det import DETS
PROJ="/sessions/funny-pensive-ritchie/mnt/CASUTA DIN COPAC"
PS=100;W=2100;D=1780
FT=1872; BT=2300; BEAMB=1872; BEAMTOP=2072; JOB=2072; JOT=2172; DECKB=2172
JX=[100,280,720,1120,1550,1980]

def g(mat,x,y,z,dx,dy,dz): return {'x':x,'y':y,'z':z,'dx':dx,'dy':dy,'dz':dz,'mat':mat,'built':True}
def N(mat,x,y,z,dx,dy,dz,ex=None,code=None):
    d={'x':x,'y':y,'z':z,'dx':dx,'dy':dy,'dz':dz,'mat':mat,'hl':True}
    if ex:d['ex']=ex
    if code:d['code']=code
    return d

def posts_full(stage):
    if stage==1:
        hf=hb=1500
    else:
        hf=1450; hb=1700   # fata mai jos (taiata), spate mai sus (schematic; cota reala in text)
    return [g('post',0,0,0,PS,hf,PS),g('post',W-PS,0,0,PS,hf,PS),g('post',0,0,D-PS,PS,hb,PS),g('post',W-PS,0,D-PS,PS,hb,PS)]
def posts_stub():
    s=420
    return [g('post',0,BEAMB-s,0,PS,s,PS),g('post',W-PS,BEAMB-s,0,PS,s,PS),g('post',0,BEAMB-s,D-PS,PS,s,PS),g('post',W-PS,BEAMB-s,D-PS,PS,s,PS)]
def polite_g(): return [g('polita',0,BEAMB-100,D-PS-90,PS,100,90),g('polita',W-PS,BEAMB-100,D-PS-90,PS,100,90)]
def beam_back_g(): return g('beam',0,BEAMB,D-90,W,200,90)
def beam_front_g(): return g('beam',0,BEAMB,0,W,200,90)
def joists_g(xs=JX): return [g('joist',x,JOB,-700,PS,PS,D+700) for x in xs]
def deck_g(n):
    out=[];z=-700
    for i in range(n): out.append(g('deck',-20,DECKB,z,W+40,28,140)); z+=150
    return out
def anchors(): return [g('anchor',x-12,0,z-12,PS+24,130,PS+24) for (x,z) in [(0,0),(W-PS,0),(0,D-PS),(W-PS,D-PS)]]
GROUND=(-220,W+220,-220,D+220)
BR=PAL['brace']; WD=PAL['post']
def F(boxes,**kw): return render(boxes,W=kw.pop('W',660),**kw)

# ---- zoom-uri 2D colorate ----
Z_ANCHOR='''<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
<rect x="120" y="10" width="60" height="120" fill="#E8973C" stroke="#161413" stroke-width="2.6"/>
<path d="M108 130 v40 h84 v-40" fill="none" stroke="#161413" stroke-width="3.2"/>
<rect x="108" y="168" width="84" height="14" fill="#94A0AB" stroke="#161413" stroke-width="2.2"/>
<text x="150" y="196" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">papuc in beton</text>
<circle cx="118" cy="150" r="5" fill="#161413"/><circle cx="182" cy="150" r="5" fill="#161413"/>
<rect x="196" y="142" width="44" height="17" rx="4" fill="#161413"/><text x="218" y="155" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="Space Mono,monospace">B2 x2</text>
<text x="60" y="150" text-anchor="middle" font-family="Space Grotesk" font-size="12" fill="#C2693A">slab!</text></svg>'''
Z_POLITA='''<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="10" width="64" height="180" fill="#E8973C" stroke="#161413" stroke-width="2.6"/><text x="72" y="184" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#fff">stalp</text>
<rect x="104" y="90" width="80" height="70" fill="#B083C6" stroke="#161413" stroke-width="2.6"/><text x="144" y="178" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">polita</text>
<text x="144" y="84" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#C2693A">sus la +1872</text>
<circle cx="96" cy="112" r="6" fill="#161413"/><circle cx="96" cy="146" r="6" fill="#161413"/>
<line x1="96" y1="112" x2="230" y2="100" stroke="#161413" stroke-width="2.4"/><line x1="96" y1="146" x2="230" y2="170" stroke="#161413" stroke-width="2.4"/>
<rect x="230" y="90" width="44" height="17" rx="4" fill="#161413"/><text x="252" y="103" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="Space Mono,monospace">B1 x2</text>
<text x="252" y="180" text-anchor="middle" font-family="Space Grotesk" font-size="11" fill="#5C574E">+ saiba B3, piulita B4</text></svg>'''
Z_C2='''<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="140" width="260" height="44" fill="#3F8FA6" stroke="#161413" stroke-width="2.6"/><text x="60" y="132" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">grinda</text>
<rect x="130" y="70" width="64" height="72" fill="#7BAE52" stroke="#161413" stroke-width="2.6"/><text x="162" y="62" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">joista</text>
<path d="M194 100 h20 v42" fill="none" stroke="#AAB2BB" stroke-width="7"/><path d="M194 100 h20 v42" fill="none" stroke="#161413" stroke-width="2"/>
<rect x="220" y="92" width="40" height="17" rx="4" fill="#161413"/><text x="240" y="105" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="Space Mono,monospace">C2 x1</text>
<path d="M162 60 v-22" stroke="#C2693A" stroke-width="2.8" marker-end="url(#u)"/><defs><marker id="u" markerWidth="10" markerHeight="10" refX="4" refY="1" orient="auto"><path d="M0 8 L4 0 L8 8 z" fill="#C2693A"/></marker></defs>
<text x="162" y="30" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#C2693A">tine jos consola</text></svg>'''
Z_BLOC='''<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg">
<rect x="70" y="30" width="46" height="150" fill="#7BAE52" stroke="#161413" stroke-width="2.6"/><rect x="204" y="30" width="46" height="150" fill="#7BAE52" stroke="#161413" stroke-width="2.6"/>
<text x="93" y="22" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">joista</text><text x="227" y="22" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">joista</text>
<rect x="116" y="96" width="88" height="42" fill="#CBA24B" stroke="#161413" stroke-width="2.6"/><text x="160" y="122" text-anchor="middle" font-family="Space Grotesk" font-size="13" fill="#161413">BL</text>
<line x1="124" y1="92" x2="150" y2="138" stroke="#161413" stroke-width="2.8"/>
<rect x="96" y="70" width="40" height="17" rx="4" fill="#161413"/><text x="116" y="83" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="Space Mono,monospace">H3</text>
<text x="250" y="96" font-family="Space Grotesk" font-size="11" fill="#C2693A">oblic</text></svg>'''
Z_DECK='''<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="120" width="260" height="30" fill="#7BAE52" stroke="#161413" stroke-width="2.6"/><text x="46" y="142" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">joista</text>
<rect x="50" y="80" width="110" height="30" rx="3" fill="#E9C277" stroke="#161413" stroke-width="2.6"/><rect x="170" y="80" width="110" height="30" rx="3" fill="#E9C277" stroke="#161413" stroke-width="2.6"/>
<line x1="160" y1="74" x2="170" y2="74" stroke="#C2693A" stroke-width="2.8"/><text x="165" y="66" text-anchor="middle" font-family="Space Mono,monospace" font-size="11" fill="#C2693A">5 mm</text>
<circle cx="85" cy="96" r="5" fill="#161413"/><circle cx="130" cy="96" r="5" fill="#161413"/><circle cx="205" cy="96" r="5" fill="#161413"/><circle cx="250" cy="96" r="5" fill="#161413"/>
<rect x="254" y="88" width="34" height="17" rx="4" fill="#161413"/><text x="271" y="101" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="Space Mono,monospace">H4</text>
<text x="120" y="170" font-family="Space Grotesk" font-size="11" fill="#5C574E">2 suruburi pe fiecare joista</text></svg>'''
Z_RAIL='''<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg">
<rect x="20" y="150" width="280" height="14" fill="#E9C277" stroke="#161413" stroke-width="2.6"/><text x="36" y="180" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">podea / cadru</text>
<rect x="50" y="40" width="12" height="112" fill="#E8973C" stroke="#161413" stroke-width="2.6"/><rect x="250" y="40" width="12" height="112" fill="#E8973C" stroke="#161413" stroke-width="2.6"/>
<rect x="50" y="40" width="212" height="12" fill="#E8973C" stroke="#161413" stroke-width="2.6"/>
<g stroke="#161413" stroke-width="2"><line x1="86" y1="52" x2="86" y2="152"/><line x1="120" y1="52" x2="120" y2="152"/><line x1="154" y1="52" x2="154" y2="152"/><line x1="188" y1="52" x2="188" y2="152"/><line x1="222" y1="52" x2="222" y2="152"/></g>
<text x="103" y="105" font-family="Space Mono,monospace" font-size="10" fill="#C2693A">&lt;9 cm</text>
<line x1="34" y1="46" x2="34" y2="152" stroke="#C2693A" stroke-width="1.8"/><text x="22" y="100" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#C2693A" transform="rotate(-90 22 100)">1 m</text></svg>'''
Z_BRACE='''<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
<rect x="50" y="20" width="40" height="160" fill="#E8973C" stroke="#161413" stroke-width="2.6"/><text x="70" y="14" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">stalp</text>
<rect x="40" y="30" width="170" height="34" fill="#3F8FA6" stroke="#161413" stroke-width="2.6"/><text x="160" y="24" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">grinda</text>
<polygon points="90,74 122,74 220,180 188,180" fill="#E2663B" stroke="#161413" stroke-width="2.6"/>
<text x="170" y="150" font-family="Space Grotesk" font-size="11" fill="#fff" transform="rotate(46 170 150)">CF</text>
<circle cx="100" cy="84" r="4.5" fill="#161413"/><circle cx="107" cy="98" r="4.5" fill="#161413"/><circle cx="114" cy="112" r="4.5" fill="#161413"/>
<rect x="120" y="78" width="44" height="17" rx="4" fill="#161413"/><text x="142" y="91" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="Space Mono,monospace">H1 x3</text></svg>'''
Z_TABLE='''<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="120" width="220" height="14" fill="#E9C277" stroke="#161413" stroke-width="2.6"/><text x="150" y="150" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#5C574E">podea balcon</text>
<rect x="140" y="20" width="22" height="160" fill="#A56B41" stroke="#161413" stroke-width="2.4"/><text x="151" y="195" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#7A5A3C">copac</text>
<ellipse cx="151" cy="40" rx="46" ry="9" fill="#C99A5E" stroke="#161413" stroke-width="2.2"/><text x="220" y="40" font-family="Space Grotesk" font-size="11" fill="#161413">blat</text>
<line x1="125" y1="120" x2="125" y2="134" stroke="#C2693A" stroke-width="2.6"/><line x1="162" y1="120" x2="162" y2="134" stroke="#C2693A" stroke-width="2.6"/>
<text x="100" y="116" font-family="Space Mono,monospace" font-size="10" fill="#C2693A">joc 3-5 cm</text>
<text x="150" y="86" text-anchor="middle" font-family="Space Grotesk" font-size="10.5" fill="#161413">blat pe cadru,<tspan x="150" dy="13">NU pe copac</tspan></text></svg>'''
print("base+zoom color ok")

props=[{'p1':(50,820,50),'p2':(-470,0,50),'thick':12,'col':BR},
       {'p1':(50,820,50),'p2':(50,0,-470),'thick':12,'col':BR},
       {'p1':(W-50,820,50),'p2':(W+470,0,50),'thick':12,'col':BR},
       {'p1':(W-50,820,50),'p2':(W-50,0,-470),'thick':12,'col':BR},
       {'p1':(50,1750,D-50),'p2':(50,0,D+470),'thick':12,'col':BR},
       {'p1':(W-50,1750,D-50),'p2':(W-50,0,D+470),'thick':12,'col':BR}]

def stage1():
    A=anchors()
    s12=F(A+[N('post',0,0,D-PS,PS,1500,PS,ex=(0,600,0),code='ST'),N('post',W-PS,0,D-PS,PS,1500,PS),N('post',0,0,0,PS,1500,PS),N('post',W-PS,0,0,PS,1500,PS)],ground=GROUND,W=640)
    s3=F(posts_full(1),ground=GROUND,W=620,dims=[{'p1':(0,0,-PS),'p2':(0,1500,-PS),'t':'PLUMB'}],labels=[{'t':'stalpi 4 m','at':(W,1650,50),'color':'#5C574E'}])
    s4=F(posts_full(1),struts=props,ground=GROUND,W=640,labels=[{'t':'proptele PT','at':(W+250,500,50),'color':BR}])
    return [dict(t='Aseaza toti 4 stalpii in papucii lor din beton, coborati drept in U. Cei 2 din spate raman LUNGI (4 m).',svg=s12,warn=False),
            dict(t='Adu fiecare stalp perfect vertical (la plumb), verificat pe doua fete cu bolobocul.',svg=s3,warn=False),
            dict(t='Sprijina fiecare stalp cu 2 proptele la baza. La cei 2 stalpi inalti din spate, pune si cate o proptea spre varf.',svg=s4,warn=True),
            dict(t='Prinde suruburile B2 in papuc DOAR slab (2 / stalp) — sa poti inca corecta. Le strangi la fisa 2.',svg=None,zoom=DETS['B2'],warn=False)]
def stage2():
    P=posts_full(2)
    s1=F(P,W=620,dims=[{'p1':(0,0,-PS),'p2':(0,1450,-PS),'t':'+2200 podea'}])
    s2=F(P,W=620,dims=[{'p1':(0,1150,-PS),'p2':(0,1450,-PS),'t':'328'}],labels=[{'t':'+1872 sprijin','at':(0,1150,-PS-300),'color':'#C2693A'}])
    off=[N('post',0,1450,0,PS,300,PS,ex=(0,420,0)),N('post',W-PS,1450,0,PS,300,PS,ex=(0,420,0))]
    s3=F(P+off,W=660,labels=[{'t':'taie la +1872','at':(W/2,1500,-220),'color':'#C2693A'},{'t':'offcut pt polite','at':(W/2,2050,0),'color':'#5C574E'}])
    return [dict(t='Marcheaza +2200 (fata podelei) pe toti 4 stalpii. Foloseste o scandura dreapta + boloboc, nu masura separat.',svg=s1,warn=False),
            dict(t='Coboara 328 mm si marcheaza +1872 — aici sta talpa GRINZII pe polite. Grinda 200 + joista 100 + dusumea 28 = 328, asa ajungi la +2200, fata podelei.',svg=s2,warn=True),
            dict(t='Taie DOAR stalpii din fata (S3, S4) la +1872. Partea taiata o pastrezi pentru polite. Stalpii din spate raman INTREGI.',svg=s3,warn=True),
            dict(t='Teseste muchia taiata. Abia acum strange definitiv suruburile B2 de la baza.',svg=None,zoom=DETS['B2'],warn=False)]
def stage3():
    base=posts_stub()
    s1=F(base+[N('polita',0,BEAMB-100,D-PS-90,PS,100,90,ex=(0,0,-650),code='PO')],W=600,dims=[{'p1':(0,BEAMB,D-PS-90),'p2':(0,BEAMB,D-PS),'t':'sus +1872'}])
    s3=F(base+polite_g(),W=600,screws=[{'at':(40,BEAMB-45,D-PS-90),'dir':(0,0,1),'code':'B1','n':2,'len':150},{'at':(W-PS+55,BEAMB-45,D-PS-90),'dir':(0,0,1),'code':'B1','n':2,'len':150}])
    return [dict(t='Aseaza polita (bloc 100x100 din offcut) pe fata interioara a stalpului din spate, cu fata de sus la +1872.',svg=s1,warn=False),
            dict(t='Gaureste prin polita in stalp: 2 gauri de 13 mm.',svg=None,warn=False),
            dict(t='Bate 2 buloane M12 (B1) cu saiba (B3) prin polita in stalp; strange cu piulita (B4) pe spate. Repeta la al doilea stalp.',svg=s3,zoom=DETS['B1'],warn=True)]
def stage4():
    base=posts_stub()+polite_g()
    s1=F(base+[N('beam',0,BEAMB,D-90,W,200,90,ex=(0,700,0),code='GR')],W=660)
    s2=F(base+[N('beam',0,BEAMB,D-90,W,200,90)],W=660,dims=[{'p1':(W,BEAMB+200,D-45),'p2':(W,BEAMB,D-45),'t':'sus +2072'}],screws=[{'at':(60,BEAMB+150,D-95),'dir':(0,0,-1),'code':'H1','len':150}])
    return [dict(t='Ridicati in DOI grinda din spate si asezati-o pe cele doua polite. Sta pe polita — nu o tineti voi.',svg=s1,warn=True),
            dict(t='Verifica fata de sus la +2072 si orizontalitatea pe toata lungimea.',svg=s2,warn=False),
            dict(t='Prinde grinda de fiecare stalp cu 3 suruburi H1 oblice PLUS un coltar metalic in stalp si in grinda (anti-smulgere). Grinda nu trebuie sa se poata ridica de pe polita.',svg=None,zoom=DETS['H1B'],warn=True)]
def stage5():
    base=posts_stub()+polite_g()+[beam_back_g()]
    s1=F(base+[N('beam',0,BEAMB,0,W,200,90,ex=(0,700,0),code='GR')],W=660)
    C1=[N('metal',0,BEAMB,-12,130,40,114,code='C1'),N('metal',W-130,BEAMB,-12,130,40,114)]
    s2=F(base+[beam_front_g()]+C1,W=660,screws=[{'at':(60,BEAMB+120,5),'dir':(0,-1,0),'code':'H1','len':150}],dims=[{'p1':(W,BEAMTOP,45),'p2':(W,BEAMTOP,D-45),'t':'ambele +2072'}])
    return [dict(t='Asezati grinda din fata PE varful stalpilor S3/S4 (taiati). Sprijin direct pe lemn.',svg=s1,warn=True),
            dict(t='Prinde cu cate un coltar C1 pe fiecare fata (2/stalp) + suruburi H1 in stalp si in grinda.',svg=s2,zoom=DETS['C1'],warn=False),
            dict(t='Verifica: ambele grinzi orizontale, varful la +2072. Ai cadrul de baza.',svg=None,warn=False)]
def stage6():
    base=posts_stub()+polite_g()+[beam_back_g(),beam_front_g()]
    s1=F(base,W=700,labels=[{'t':str(x),'at':(x,BEAMB+340+(i%3)*210,0),'to':(x,BEAMB+200,0),'color':'#C2693A'} for i,x in enumerate([100,280,720,1120,1550,1980])])
    s2=F(base+joists_g([280,720,1120,1550,1980])+[N('joist',100,JOB,-700,PS,PS,D+700,ex=(0,560,0),code='JO')],W=680,dims=[{'p1':(100,JOB,-700),'p2':(100,JOB,0),'t':'700 consola'}])
    s3=F(base+joists_g(),W=680)
    s4=F(base+joists_g(),W=680,screws=[{'at':(150,JOT,5),'dir':(0,-1,0),'code':'C2','n':2,'len':150}])
    return [dict(t='Marcheaza pe ambele grinzi pozitiile celor 6 joiste, de la coltul S4: 100 / 280 / 720 / 1120 / 1550 / 1980 mm.',svg=s1,warn=False),
            dict(t='Aseaza prima joista peste ambele grinzi. Capatul din fata iese 700 mm in gol (consola = balconul).',svg=s2,warn=True),
            dict(t='Aseaza toate cele 6 joiste la pozitiile marcate.',svg=s3,warn=False),
            dict(t='La FIECARE reazem (fata + spate) prinde un coltar C2 pe lateral — 12 in total. Tine joista jos la consola.',svg=s4,zoom=DETS['C2'],warn=True)]
def stage7():
    base=posts_stub()+polite_g()+[beam_back_g(),beam_front_g()]+joists_g()
    ram=[N('joist',280,JOB,-300,440,PS,PS,code='RM'),N('joist',280,JOB,-120,440,PS,PS)]
    s1=F(base+ram,W=680,dims=[{'p1':(280,JOB,-210),'p2':(720,JOB,-210),'t':'gaura copac'}])
    tree=[N('tree',450,1280,-300,160,1500,160,code='copac')]
    s2=F(base+tree,W=680,labels=[{'t':'reteaza la +2780','at':(530,2820,-220),'color':'#C2693A'}])
    return [dict(t='Intre joistele de la 280 si 720 — trunchiul cade chiar intre ele, fara sa le atinga — monteaza 2 traverse scurte (RM) care inchid rama gaurii.',svg=s1,warn=False),
            dict(t='Reteaza corcodusul la ~+2780 (deasupra podelei). Lasa joc de 3-5 cm jur-imprejurul trunchiului.',svg=s2,warn=True),
            dict(t='Blatul mesei se fixeaza de podea, prin cadrul lui — NICIODATA de copac.',svg=None,zoom=DETS['TABLE'],warn=True)]
def stage8():
    base=posts_stub()+polite_g()+[beam_back_g(),beam_front_g()]+joists_g()
    bl=[N('block',JX[i]+PS,JOB,-40,JX[i+1]-JX[i]-PS,PS,90,code=('BL' if i==0 else None)) for i in range(len(JX)-1)]
    s2=F(base+bl,W=680)
    return [dict(t='Taie bucati scurte de lemn (blocaje, BL) cat distanta dintre joiste.',svg=None,warn=False),
            dict(t='Pune cate un blocaj intre joiste, PESTE fiecare grinda (fata si spate).',svg=s2,warn=False),
            dict(t='Prinde fiecare blocaj cu suruburi H3 oblic. Opresc joistele sa se rasuceasca — podeaua devine ferma.',svg=None,zoom=DETS['H3'],warn=False)]
def stage9():
    base=posts_stub()+polite_g()+[beam_back_g(),beam_front_g()]+joists_g()
    br=[{'p1':(55,BEAMB+170,30),'p2':(55,BEAMB-360,560),'thick':13,'col':BR},
        {'p1':(W-55,BEAMB+170,30),'p2':(W-55,BEAMB-360,560),'thick':13,'col':BR},
        {'p1':(40,BEAMB+170,8),'p2':(560,BEAMB-360,8),'thick':13,'col':BR},
        {'p1':(300,JOB-10,-660),'p2':(300,BEAMB-200,-30),'thick':13,'col':BR}]
    s2=F(base,struts=br,W=680,labels=[{'t':'contrafise CF','at':(W+250,500,300),'color':BR}])
    s4=F(posts_stub(),struts=[{'p1':(50,1750,D-50),'p2':(50,900,D+470),'thick':12,'col':BR},{'p1':(W-50,1750,D-50),'p2':(W-50,900,D+470),'thick':12,'col':BR}],W=600,labels=[{'t':'doar la varf RAMAN','at':(W/2,1820,D+520),'color':'#C2693A'}])
    return [dict(t='Masoara si taie capatul fiecarei contrafise (diagonala) pe potriveala.',svg=None,zoom=DETS['CF'],warn=False),
            dict(t='Monteaza contravantuirile in planul stang, drept, fata si sub nasul consolei. La contrafisa de sub nas prinde-o pe LATERAL sau adauga un coltar — acolo lucreaza si la intindere. Platforma devine rigida.',svg=s2,warn=True),
            dict(t='Prinde fiecare capat cu 3 suruburi H1.',svg=None,zoom=DETS['CF'],warn=False),
            dict(t='SCOATE proptelele de la baza. Cele de la varful stalpilor inalti din spate RAMAN pana la peretii din Faza 2.',svg=s4,warn=True)]
def stage10():
    base=posts_stub()+polite_g()+[beam_back_g(),beam_front_g()]+joists_g()
    s1=F(base+[N('deck',-20,DECKB,-700,W+40,28,140,ex=(0,420,0),code='DL')],W=680,screws=[{'at':(120,DECKB+28,-630),'dir':(0,-1,0),'code':'H4','n':2,'len':140}])
    s3=F(base+deck_g(15),W=680,labels=[{'t':'decupaj la copac','at':(530,DECKB+260,-220),'color':'#C2693A'}])
    return [dict(t='Aseaza prima scandura la marginea din fata, perpendicular pe joiste. 2 suruburi inox (H4) pe fiecare joista.',svg=s1,zoom=DETS['H4'],warn=False),
            dict(t='Lasa 5 mm intre scanduri (pune un cui ca distantier). Apa se scurge, lemnul respira.',svg=None,warn=True),
            dict(t='Continua pana acoperi tot. La copac, taie scandurile in jurul gaurii, cu joc.',svg=s3,warn=False),
            dict(t='Dupa montaj, da cu ulei (F1) pe toata dusumeaua de larice.',svg=None,warn=False)]
def stage11():
    base=posts_stub()+polite_g()+[beam_back_g(),beam_front_g()]+joists_g()+deck_g(15)
    top=DECKB+28
    rp=[{'p1':(x,top,z),'p2':(x,top+1000,z),'thick':14,'col':WD} for (x,z) in [(20,-680),(W-20,-680),(20,D-20),(W-20,D-20)]]
    s1=F(base,struts=rp,W=680)
    rail=rp+[{'p1':(20,top+980,-680),'p2':(W-20,top+980,-680),'thick':11,'col':WD},{'p1':(20,top+980,D-20),'p2':(W-20,top+980,D-20),'thick':11,'col':WD},{'p1':(20,top+980,-680),'p2':(20,top+980,D-20),'thick':11,'col':WD},{'p1':(W-20,top+980,-680),'p2':(W-20,top+980,D-20),'thick':11,'col':WD}]
    s2=F(base,struts=rail,W=680,dims=[{'p1':(20,top,-680),'p2':(20,top+1000,-680),'t':'1 m'}])
    return [dict(t='Monteaza stalpisorii balustradei, bulonati de CADRU (joiste/grinda), nu de dusumea. Jur-imprejur, inclusiv pe nasul consolei.',svg=s1,zoom=DETS['RAIL'],warn=True),
            dict(t='Pune mana curenta sus, la 1 m inaltime, pe tot conturul.',svg=s2,zoom=DETS['RAIL'],warn=True),
            dict(t='Umple cu sipci, cu goluri sub 9 cm (un copil nu trebuie sa incapa sau sa se catere usor).',svg=None,zoom=DETS['RAIL'],warn=True),
            dict(t='Lasa o poarta pe partea S3 (opusa mesei-copac), unde urca scara. Testeaza balustrada impingand cu putere.',svg=None,warn=True)]

META=[
 (1,'fisa-01','FISA 1 / 11','Stalpii in papuci','2-3 ore',True,'Mediu',[('ST','4','la lungime mare, NU taia'),('PAP','4','deja in beton'),('B2','8','2 / stalp'),('PT','~6','proptele')],['Cheie 19 (M12)','Boloboc','Bormasina','2 persoane'],['Toti 4 stalpii verticali pe 2 fete','Proptele la fiecare stalp','Suruburi inca slabe']),
 (2,'fisa-02','FISA 2 / 11','Nivel +2200 si taiere stalpi fata','1-2 ore',False,'CRITIC',[('ST','—','doar cei 2 din fata se taie')],['Nivela cu furtun / laser','Creion','Fierastrau','Echer'],['Linia +1872 identica pe toti','Doar stalpii fata taiati','Stalpii spate INTREGI','Suruburi baza stranse']),
 (3,'fisa-03','FISA 3 / 11','Polite pe stalpii din spate','1 ora',False,'CRITIC',[('PO','2','offcut 100x100'),('B1','4','tija ~220'),('B3','8','2 / bulon: cap + piulita'),('B4','4','piulite')],['Bormasina + burghiu 13','Cheie 19','Bomfaier'],['Ambele polite sus la +1872','2 buloane stranse / polita','Polita nu se misca']),
 (4,'fisa-04','FISA 4 / 11','Grinda din spate pe polite','1 ora',True,'CRITIC',[('GR','1','grinda spate'),('C2','2','coltar anti-smulgere'),('H1','6','3 oblice / capat')],['2 persoane','Bormasina','Nivela'],['Grinda pe ambele polite','Fata sus la +2072','Coltar anti-smulgere la fiecare capat','Buloane polita REVERIFICATE dupa asezarea grinzii']),
 (5,'fisa-05','FISA 5 / 11','Grinda din fata pe varful stalpilor','1 ora',True,'CRITIC',[('GR','1','grinda fata'),('C1','4','2 / stalp'),('H1','~12','in coltare')],['2 persoane','Bormasina','Nivela'],['Grinda pe varful stalpilor','2 coltare C1 / stalp','Ambele grinzi la +2072']),
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
 'B3':('POZE/COD_3840897.png','Saiba M12'),'B4':('POZE/COD_3830642.png','Piulita M12'),'F1':('POZE/COD_5509678.png','Ulei tec'),'PAP':('POZE/papuc.svg','Papuc reazem U'),'SB':('POZE/lemn.png','Stalpisor 7x7 (Faza 2)'),'SP':('POZE/lemn.png','Sipci balustrada'),'MC':('POZE/lemn.png','Mana curenta'),'BM':('POZE/COD_6834285.png','Bulon M10'),'RM':('POZE/lemn.png','Traverse rama'),'F2':('POZE/kober.jpg','Grund Köber'),'F3':('POZE/lemn.png','Topcoat (Faza 2)')}
