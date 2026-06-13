# -*- coding: utf-8 -*-
import os
import fise_gen as F
from fise_gen import hero, PARTS, PROJ, PS, W, D, JX, b, BACK_TOP, DECK_TOP, BEAM_TOP, JO_TOP

def C1boxes():
    return [b(0,1872,-10,120,40,110,hl=True), b(W-120,1872,-10,120,40,110,hl=True)]
def blockboxes():
    out=[]
    for i in range(len(JX)-1):
        x0=JX[i]+PS; x1=JX[i+1]; out.append(b(x0,BEAM_TOP, -5, x1-x0, PS, 100, hl=True))
    return out
def treebox():
    return [b(440,1400,-300,160,1400,160,fill='#efe7da')]
def railboxes():
    r=[]; H=1000; top=DECK_TOP
    # 4 corner posts
    for (x,z) in [(0,-700),(W-58,-700),(0,D-58),(W-58,D-58)]:
        r.append(b(x,top,z,58,H,58,hl=True))
    # top rails (perimeter, 4 bars)
    r.append(b(0,top+H-40,-700,W,40,40,hl=True))      # front
    r.append(b(0,top+H-40,D-40,W,40,40,hl=True))      # back
    r.append(b(0,top+H-40,-700,40,40,D+700,hl=True))  # left
    r.append(b(W-40,top+H-40,-700,40,40,D+700,hl=True))# right
    return r

# (num, slug, kick, title, time, two_people, parts[(code,qty,note)], tools[], steps[(txt,detail_svg_or_None,warn)], check[], hero_svg)
def heroes():
    return {
1: hero(1, hl={'posts'}, W=560,
        screws=[{'at':(50,170,50),'dir':(0,1,0),'len':190,'code':'B2'},
                {'at':(W-50,170,50),'dir':(0,1,0),'len':190,'code':'B2'}]),
2: hero(2, hl={'posts'}, W=560,
        dims=[((0,0,0),(0,1872,0),'+1872'), ((0,1872,0),(PS,1872,0),'taie')]),
3: hero(3, clip=1400, hl={'polite'}, W=560,
        screws=[{'at':(50,1822,D-PS-90),'dir':(0,0,1),'len':150,'code':'B1'}]),
4: hero(4, clip=1400, hl={'beam_back'}, W=600,
        screws=[{'at':(60,1900,D-95),'dir':(0,-1,0),'len':150,'code':'H1'}]),
5: hero(5, clip=1400, hl={'beam_front'}, extras=C1boxes(), W=600,
        screws=[{'at':(60,1900,10),'dir':(0,-1,0),'len':150,'code':'H1'}]),
6: hero(6, clip=1400, hl={'joists'}, W=640,
        dims=[((100,JO_TOP,-700),(100,JO_TOP,0),'700 consola')]),
7: hero(7, clip=1400, extras=treebox(), W=640,
        dims=[((280,JO_TOP,200),(720,JO_TOP,200),'gaura')]),
8: hero(8, clip=1400, extras=blockboxes(), W=640),
9: hero(9, clip=1200, W=640),
10: hero(10, clip=1400, hl={'deck'}, W=640),
11: hero(11, clip=1400, extras=railboxes(), W=640),
}

H=heroes()
STAGES=[
 dict(n=1,slug='fisa-01',kick='FISA 1 / 11',title='Stalpii in ancore',time='2-3 ore',ppl=True,diff='Mediu',
   parts=[('ST','4','la lungime mare, NU taia inca'),('PAP','4','deja in beton'),('B2','8','2 / stalp'),('PT','~6','proptele')],
   tools=['Cheie 19 (M12)','Nivela / boloboc','Bormasina','2 persoane'],
   steps=[('Pune fiecare stalp in papucul lui. Lasa-l la lungimea mare — taierea vine la fisa 2.',None,False),
          ('Prinde suruburile B2 in papuc doar SLAB (sa poti misca stalpul).',None,False),
          ('Adu fiecare stalp la plumb (vertical perfect) pe doua fete, cu nivela pe o latura.',None,False),
          ('Sprijina fiecare stalp cu 2 proptele (PT) la baza. La cei 2 stalpi inalti din spate, pune si cate o proptea spre varf.',None,True)],
   check=['Toti 4 stalpii verticali pe ambele fete','Proptele la fiecare stalp','Suruburile inca slabe (se string la fisa 2)']),
 dict(n=2,slug='fisa-02',kick='FISA 2 / 11',title='Nivel +2200 si taiere stalpi fata',time='1-2 ore',ppl=False,diff='CRITIC',
   parts=[('ST','—','doar cei 2 din fata se taie')],
   tools=['Nivela cu furtun / laser','Creion','Fierastrau','Echer'],
   steps=[('Marcheaza +2200 (fata podelei) pe toti 4 stalpii. Foloseste o scandura dreapta + nivela, nu masura separat.',None,False),
          ('Coboara 328 mm si marcheaza +1872 — acolo se sprijina podeaua (grinda 200 + joista 100 + dusumea 28).',None,True),
          ('Taie DOAR stalpii din fata (S3, S4) la +1872. Cei din spate raman intregi.',None,True),
          ('Teseste muchia taiata. Abia acum strange definitiv suruburile de la baza.',None,False)],
   check=['Linia +1872 identica pe toti stalpii','Doar stalpii fata taiati','Stalpii spate INTREGI','Suruburi baza stranse']),
 dict(n=3,slug='fisa-03',kick='FISA 3 / 11',title='Polite pe stalpii din spate',time='1 ora',ppl=False,diff='CRITIC',
   parts=[('PO','2','bloc 100x100 din offcut'),('B1','4','tija taiata ~220, 2/polita'),('B3','4','saibe'),('B4','4','piulite')],
   tools=['Bormasina + burghiu 13','Cheie 19','Bomfaier (taie tija)'],
   steps=[('Pe fata fiecarui stalp din spate, asaza polita (PO) cu fata de sus exact la +1872.',F.DET_POLITA,False),
          ('Gaureste prin polita in stalp, 2 gauri de 13 mm.',None,False),
          ('Bate cate 2 buloane M12 (B1) cu saiba (B3); strange cu piulita (B4) pe spatele stalpului.',F.DET_POLITA,True)],
   check=['Ambele polite cu fata sus la +1872','2 buloane bine stranse / polita','Polita nu se misca deloc']),
 dict(n=4,slug='fisa-04',kick='FISA 4 / 11',title='Grinda din spate pe polite',time='1 ora',ppl=True,diff='CRITIC',
   parts=[('GR','1','grinda glulam spate'),('H1','~4','o tin lipita de stalpi')],
   tools=['2 persoane','Bormasina','Nivela'],
   steps=[('Ridicati in DOI grinda si asezati-o pe cele doua polite. Sta pe polita — nu o tineti voi.',None,True),
          ('Verifica fata de sus la +2072 si orizontalitatea.',None,False),
          ('Prinde grinda de stalpi cu suruburi H1 (toe-screw) ca sa stea lipita.',None,False)],
   check=['Grinda sta pe ambele polite','Fata sus la +2072, orizontala','Prinsa de stalpi cu H1']),
 dict(n=5,slug='fisa-05',kick='FISA 5 / 11',title='Grinda din fata pe varful stalpilor',time='1 ora',ppl=True,diff='CRITIC',
   parts=[('GR','1','grinda glulam fata'),('C1','4','coltar, 2/stalp'),('H1','~12','in coltare')],
   tools=['2 persoane','Bormasina','Nivela'],
   steps=[('Asezati grinda din fata PE varful stalpilor S3/S4 (sprijin direct).',None,True),
          ('Prinde cu cate un coltar C1 pe fiecare fata + suruburi H1 in stalp si in grinda.',None,False),
          ('Verifica: ambele grinzi orizontale, varful la +2072.',None,False)],
   check=['Grinda fata pe varful stalpilor','Cate 2 coltare C1 / stalp','Ambele grinzi la +2072, la nivel']),
 dict(n=6,slug='fisa-06',kick='FISA 6 / 11',title='Cele 6 joiste',time='2 ore',ppl=True,diff='CRITIC',
   parts=[('JO','6','100x100, dintr-o bucata'),('C2','12','coltar, 2/joista'),('H2','~60','in coltare')],
   tools=['Bormasina','Ruleta','Creion','Echer'],
   steps=[('Asaza cele 6 joiste peste ambele grinzi. Pozitii de la S4: 100 / 280 / 720 / 1120 / 1550 / 1980 mm.',None,False),
          ('Capetele din fata ies 700 mm in consola (balconul). Joista e dintr-o singura bucata.',None,True),
          ('La fiecare reazem, prinde un coltar C2 pe lateral — tine joista jos (anti-ridicare la consola).',F.DET_C2,True)],
   check=['6 joiste la pozitiile corecte','Consola 700 mm in fata','Cate 2 coltare C2 / joista (12 total)']),
 dict(n=7,slug='fisa-07',kick='FISA 7 / 11',title='Gaura copacului si masa',time='1-2 ore',ppl=False,diff='Atentie',
   parts=[('BL','2','traverse = rama gaurii'),('H3','~6','prindere rama')],
   tools=['Fierastrau','Bormasina','Ruleta'],
   steps=[('Intre joistele de la 280 si 720 (spre S4), pune 2 traverse = rama gaurii copacului.',None,False),
          ('Reteaza corcodusul la ~+2780 (deasupra podelei). Lasa joc 3-5 cm jur-imprejurul trunchiului.',None,True),
          ('Blatul mesei se va fixa de podea, prin cadrul lui — NICIODATA de copac.',None,True)],
   check=['Rama gaurii intre joistele 280-720','Joc 3-5 cm in jurul trunchiului','Blatul NU se sprijina pe copac']),
 dict(n=8,slug='fisa-08',kick='FISA 8 / 11',title='Blocaje intre joiste',time='1 ora',ppl=False,diff='Normal',
   parts=[('BL','~10','bucati scurte din offcut'),('H3','~20','oblic')],
   tools=['Fierastrau','Bormasina'],
   steps=[('Taie bucati scurte (blocaje) cat distanta dintre joiste.',F.DET_BLOC,False),
          ('Pune cate un blocaj intre joiste PESTE fiecare grinda.',None,False),
          ('Prinde-le cu suruburi H3 oblic. Opresc joistele sa se rasuceasca.',F.DET_BLOC,False)],
   check=['Blocaje peste ambele grinzi, intre toate joistele','Prinse oblic cu H3','Podeaua e ferma, nu se mai misca']),
 dict(n=9,slug='fisa-09',kick='FISA 9 / 11',title='Contravantuiri si scoatem proptelele',time='2 ore',ppl=False,diff='CRITIC',
   parts=[('CF','6','diagonale din offcut'),('H1','~18','3 / capat')],
   tools=['Fierastrau','Bormasina','Echer'],
   steps=[('Monteaza contravantuirile (diagonalele) in planul stang, drept, fata si sub nasul consolei.',F.DET_BRACE,False),
          ('Prinde fiecare capat cu 3 suruburi H1. Acum platforma e rigida.',F.DET_BRACE,False),
          ('SCOATE proptelele de la baza. Cele de la varful stalpilor inalti RAMAN pana la peretii din Faza 2.',None,True)],
   check=['Diagonale pe toate planurile + sub consola','3 suruburi / capat','Proptele baza scoase; cele de varf raman']),
 dict(n=10,slug='fisa-10',kick='FISA 10 / 11',title='Dusumeaua de larice',time='3-4 ore',ppl=False,diff='Normal',
   parts=[('DL','17','scanduri larice 28x145'),('H4','~204','2 / joista'),('F1','2','ulei tec')],
   tools=['Bormasina','Cui ca distantier (5 mm)','Pensula'],
   steps=[('Asaza scandurile peste joiste, perpendicular. 2 suruburi inox (H4) pe fiecare joista.',F.DET_DECK,False),
          ('Lasa 5 mm intre scanduri (un cui ca distantier). La copac, taie scandurile in jurul gaurii cu joc.',F.DET_DECK,True),
          ('Dupa montaj, da cu ulei (F1) pe toata dusumeaua.',None,False)],
   check=['Toate scandurile prinse cu 2 H4 / joista','Gol egal de 5 mm','Decupaj curat la copac','Uns cu ulei']),
 dict(n=11,slug='fisa-11',kick='FISA 11 / 11',title='Balustrada si poarta',time='3-4 ore',ppl=False,diff='CRITIC',
   parts=[('—','—','stalpisori + sipci + mana curenta (Faza 2)')],
   tools=['Bormasina','Nivela','Fierastrau'],
   steps=[('Monteaza balustrada de 1 m jur-imprejurul balconului, inclusiv pe nasul consolei.',None,True),
          ('Goluri sub 9 cm intre sipci (un copil nu trebuie sa incapa).',None,True),
          ('Poarta pe partea S3 (opusa mesei-copac), unde urca scara. Stalpisorii se buloneaza de CADRU, nu de dusumea.',None,True)],
   check=['Balustrada 1 m jur-imprejur','Goluri sub 9 cm peste tot','Poarta pe S3','Stalpisori prinsi de cadru, testati prin impingere']),
]
for s in STAGES: s['hero']=H[s['n']]
print('STAGES def OK:',len(STAGES))
import json
# salveaza pt pasul de emit
import pickle
pickle.dump(STAGES, open('stages.pkl','wb'))
