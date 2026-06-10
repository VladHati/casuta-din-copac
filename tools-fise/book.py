# -*- coding: utf-8 -*-
import pickle
import fb
from fb import PARTS, PROJ, render, PS, W, D, JX, BEAMB, JOB, DECKB, posts_stub, polite_g, beam_back_g, beam_front_g, joists_g, deck_g, g, N
DATA=pickle.load(open('data.pkl','rb'))

# ---- hero coperta: platforma finala, colorata ----
def cover_hero():
    ph=950
    A=[g('post',0,0,0,PS,ph,PS),g('post',W-PS,0,0,PS,ph,PS),g('post',0,0,D-PS,PS,ph,PS),g('post',W-PS,0,D-PS,PS,ph,PS)]
    beams=[g('beam',0,ph,0,W,200,90),g('beam',0,ph,D-90,W,200,90)]
    JY=ph+200
    joists=[g('joist',x,JY,-700,PS,PS,D+700) for x in JX]
    # dusumea doar pe partea din spate (casa), ca sa se vada joistele in fata (balcon)
    deck=[];z=250
    while z<D-40: deck.append(g('deck',-20,JY+PS,z,W+40,28,140)); z+=150
    tree=[{'x':470,'y':ph-260,'z':-300,'dx':150,'dy':1500,'dz':150,'mat':'tree'}]
    L=[{'t':'ST','at':(-360,ph+120,60),'to':(50,ph-60,50),'color':fb.PAL['post']},
       {'t':'GR','at':(W+330,ph+120,45),'to':(W-60,ph+100,45),'color':fb.PAL['beam']},
       {'t':'JO','at':(180,JY+520,-720),'to':(150,JY+50,-360),'color':fb.PAL['joist']},
       {'t':'DL','at':(W+340,JY+360,D-260),'to':(W-200,JY+128,D-260),'color':fb.PAL['deck']},
       {'t':'copac','at':(470,ph+1380,-220),'to':(545,ph+250,-220),'color':fb.PAL['tree']}]
    D2=[{'p1':(100,JY,-700),'p2':(100,JY,0),'t':'consola 700'}]
    return render(A+beams+joists+deck+tree, labels=L, dims=D2, W=860)

# ---- sectiune materiale (curata, un singur stil) ----
MAT=[('le ai deja',[('ST','4','stalpi KVH 100x100'),('JO','4','joiste (din lotul de 6)'),('PAP','4','papuci, deja in beton'),('F2','1','grund Köber 4 L')]),
     ('in comanda Hornbach (4.101 lei)',[('GR','2','grinzi glulam 90x200'),('JO','2','completare joiste'),('DL','17','dusumea larice'),('C1','4','coltare 100x90'),('C2','14','coltare 90x65 (12 joiste + 2 grinda spate)'),('H1','1 pac','Heco 8x200'),('H2','1 pac','Heco 6x100'),('H3','1 pac','Heco 6x80'),('H4','2 pac','inox 5x60'),('B1','1','tija M12 (taie 4x ~220)'),('B2','1 pac','M12x120 baza'),('B3','1 pac','saibe M12'),('B4','1 pac','piulite M12'),('F1','2','ulei tec')]),
     ('din offcut',[('PO','2','polite'),('BL','~12','blocaje'),('RM','2','traverse rama copac'),('CF','6','contrafise'),('PT','~6','proptele')]),
     ('Faza 2 / de ales (nu opreste startul)',[('SB','~6','stalpisor balustrada 70x70'),('SP','set','sipci, gol <9 cm'),('MC','~7 m','mana curenta'),('BM','~12','bulon M10 balustrada'),('F3','1','topcoat colorat exterior')])]
PARTS2=dict(PARTS); PARTS2['F2']=('POZE/kober.jpg','Grund Köber 4 L'); PARTS2['F3']=('POZE/lemn.png','Topcoat colorat')

SAFETY=[('Inaltime 2,2 m','Balustrada de 1 m jur-imprejur, goluri sub 9 cm, poarta pe partea S3. Sub platforma, sol moale (scoarta/nisip) pe ~5 m².'),
 ('Copacul nu tine nimic','Corcodusul trece liber prin gaura cu joc de 3-5 cm. Blatul mesei se prinde de cadrul propriu, NICIODATA de copac.'),
 ('Ordinea de siguranta','Proptelele raman pana montezi contravantuirile. Nimeni nu sta pe consola (balcon) inainte de contrafisa de sub nas.'),
 ('Legaturi verificate','Coltare anti-ridicare la fiecare joista; coltar anti-smulgere la grinda din spate. Dupa montaj, reverifica strangerea buloanelor portante (polite + baza).'),
 ('Lemn protejat','Grunduieste lemnul de structura INAINTE de montaj; ulei pe dusumea DUPA montaj. Capetele de stalp in papuc, cu drenaj, sa nu putrezeasca.')]

CSS='''<style>
@page{size:A4;margin:15mm 14mm 16mm;@bottom-center{content:"Casuta din copac · Faza 1 · pagina " counter(page);font-family:'Space Mono',monospace;font-size:8.5pt;color:#A39C8E}}
@page:first{margin:0;@bottom-center{content:""}}
:root{--ink:#161413;--soft:#5C574E;--faint:#9A9388;--line:#E7E3DB;--acc:#C2693A;--wash:#FAF8F4;--crit:#C2412B;}
*{box-sizing:border-box}
body{margin:0;color:var(--ink);font-family:'Space Grotesk',system-ui,sans-serif;line-height:1.5;font-size:11pt}
.mono{font-family:'Space Mono',monospace}
h1,h2,h3{font-family:'Fraunces',Georgia,serif;font-weight:600;margin:0;letter-spacing:-.01em}
/* COVER */
.cover{position:relative;height:297mm;display:flex;flex-direction:column;justify-content:flex-end;break-after:page;overflow:hidden;color:#fff;background:#26241f url('POZE/santier-3.jpg') center/cover no-repeat}
.cover .scrim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,18,15,.12) 0%,rgba(20,18,15,0) 30%,rgba(20,18,15,.55) 62%,rgba(20,18,15,.88) 100%)}
.cover .ct{position:relative;padding:0 22mm 22mm}
.cover .kick{font-family:'Space Mono',monospace;font-size:11pt;letter-spacing:.26em;text-transform:uppercase;color:#fff;opacity:.95}
.cover h1{font-size:54pt;line-height:1;margin:6mm 0 5mm;color:#fff}
.cover .sub{font-size:13.5pt;color:#fff;opacity:.95;max-width:140mm}
.cover .foot{display:flex;justify-content:space-between;border-top:1.5px solid rgba(255,255,255,.45);padding-top:5mm;margin-top:8mm;font-family:'Space Mono',monospace;font-size:9.5pt;color:#fff;opacity:.92}
/* SECTION headers */
.sect{break-before:page;padding-top:2mm}
.eyebrow{font-family:'Space Mono',monospace;font-size:9pt;letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin-bottom:2mm}
.sect>h2{font-size:30pt;line-height:1.02;margin-bottom:4mm;border-bottom:3px solid var(--ink);padding-bottom:3mm}
.lead{color:var(--soft);font-size:11.5pt;max-width:150mm;margin:0 0 6mm}
/* ce construim */
.cc{display:grid;grid-template-columns:1fr 1fr;gap:8mm;align-items:start}
.cc .draw{border:1px solid var(--line);border-radius:4mm;background:var(--wash);padding:4mm}
.cc .draw svg{width:100%;height:auto;display:block}
.facts{list-style:none;padding:0;margin:0}
.facts li{display:flex;justify-content:space-between;gap:6mm;padding:2.4mm 0;border-bottom:1px solid var(--line);font-size:11pt}
.facts li b{font-family:'Space Mono',monospace;color:var(--ink)}
/* materiale grid */
.mgrp{margin:0 0 6mm}
.mgrp .gh{font-family:'Space Mono',monospace;font-size:9.5pt;letter-spacing:.12em;text-transform:uppercase;color:var(--faint);margin:0 0 3mm}
.pg{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}
.pc{border:1px solid var(--line);border-radius:3mm;overflow:hidden;break-inside:avoid}
.pc .im{height:24mm;background:var(--wash);display:grid;place-items:center;border-bottom:1px solid var(--line)}
.pc .im img{max-width:84%;max-height:20mm;object-fit:contain;mix-blend-mode:multiply}
.pc .bd{padding:2mm 2.6mm}
.pc .r1{display:flex;justify-content:space-between;align-items:center}
.pc .code{font-family:'Space Mono',monospace;font-weight:700;font-size:9.5pt;background:var(--ink);color:#fff;border-radius:2mm;padding:0 2mm}
.pc .qt{font-family:'Space Mono',monospace;font-weight:700;font-size:10pt}
.pc .nm{font-size:8.6pt;color:var(--soft);margin-top:1mm;line-height:1.2}
/* fisa */
.fisa{break-before:page}
.fhead{display:grid;grid-template-columns:1fr 1.05fr;gap:7mm;align-items:center;border-bottom:3px solid var(--ink);padding-bottom:4mm;margin-bottom:5mm}
.fhead .kick{font-family:'Space Mono',monospace;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--acc)}
.fhead h2{font-size:25pt;line-height:1.03;margin:2mm 0 3mm}
.meta{display:flex;flex-wrap:wrap;gap:2mm}
.mtag{font-family:'Space Mono',monospace;font-size:8.5pt;border:1.4px solid var(--ink);border-radius:99px;padding:1mm 3mm}
.mtag.crit{border-color:var(--crit);color:var(--crit)}
.herodraw{border:1px solid var(--line);border-radius:4mm;background:var(--wash);padding:3mm}
.herodraw svg{width:100%;height:auto;display:block}
.sh{font-family:'Space Mono',monospace;font-size:9pt;letter-spacing:.14em;text-transform:uppercase;color:var(--faint);margin:5mm 0 3mm}
.legend{display:flex;flex-wrap:wrap;gap:2mm 5mm;margin:0 0 4mm}
.lg{display:inline-flex;align-items:center;gap:1.6mm;font-size:9pt;color:var(--soft)}.lg b{color:#161413;font-family:'Space Mono',monospace}.lg i{width:3.4mm;height:3.4mm;border-radius:1mm;border:1.6px solid #161413}
.tools{display:flex;flex-wrap:wrap;gap:2mm;margin-bottom:2mm}
.tool{font-family:'Space Mono',monospace;font-size:8.6pt;border:1px solid var(--line);background:var(--wash);border-radius:2mm;padding:1.4mm 2.6mm;color:var(--soft)}
.fkey{display:flex;flex-wrap:wrap;gap:2mm 5mm;margin:0 0 4mm;padding:3mm 3.5mm;background:var(--wash);border:1px solid var(--line);border-radius:3mm}
.fk{display:inline-flex;align-items:center;gap:2mm;font-size:9pt;color:var(--soft)}
.fnote{flex-basis:100%;margin-top:1mm;font-size:9pt;color:var(--soft)}.fnote b{color:#161413}
.step{padding:4mm 0;border-top:1px solid var(--line);break-inside:avoid}
.step .h{display:flex;gap:4mm;align-items:flex-start}
.bn{flex:0 0 9mm;width:9mm;height:9mm;border-radius:50%;background:var(--ink);color:#fff;display:inline-flex;align-items:center;justify-content:center;line-height:1;font-family:'Space Mono',monospace;font-weight:700;font-size:12pt}
.tx{font-size:11pt;line-height:1.45}
.step .drawbox,.step .zoombox,.step .warn{margin-left:13mm}
.drawbox{margin-top:3mm;border:1px solid var(--line);border-radius:3mm;background:var(--wash);padding:3mm;text-align:center}
.drawbox svg{max-height:72mm;max-width:100%;width:auto;height:auto;display:inline-block}
.zoombox{margin-top:3mm;border:1.4px dashed var(--acc);border-radius:3mm;background:#fff;padding:3mm 3.5mm;max-width:165mm}
.zoombox .zl{font-family:'Space Mono',monospace;font-size:8.6pt;letter-spacing:.1em;text-transform:uppercase;color:var(--acc);margin:0 0 2mm;font-weight:700}
.zoombox svg{max-height:48mm;max-width:100%;width:auto;height:auto;display:block;margin:0 auto}
.warn{display:flex;gap:2.6mm;align-items:flex-start;margin-top:3mm;background:#FBEEE4;border:1px solid #F0D8C4;border-left:3px solid var(--acc);border-radius:2.6mm;padding:2.6mm 3mm;font-size:10pt;color:#7a4a2c;max-width:150mm}
.warn b{color:var(--crit)}
.check{list-style:none;padding:0;margin:0;display:grid;gap:2.4mm}
.check li{display:flex;align-items:flex-start;gap:3mm;font-size:10.5pt}
.check .bx{flex:0 0 auto;width:4.6mm;height:4.6mm;border:1.8px solid var(--ink);border-radius:1.4mm;margin-top:.5mm}
/* siguranta */
.safe{display:grid;gap:4mm}
.scard{border:1px solid var(--line);border-left:4px solid var(--acc);border-radius:3mm;padding:4mm 5mm;break-inside:avoid}
.scard h3{font-size:14pt;margin:0 0 1.5mm}
.scard p{margin:0;color:var(--soft);font-size:10.5pt}
.toollist{list-style:none;padding:0;margin:0;columns:2;column-gap:10mm}.toollist li{break-inside:avoid;padding:2.6mm 0;border-bottom:1px solid var(--line)}.toollist b{display:block;font-size:11pt}.toollist span{font-size:9.5pt;color:var(--soft)}
</style>'''

LEG=('<div class="legend">'+''.join(f'<span class="lg"><i style="background:{c}"></i><b>{cod}</b>&nbsp;{n}</span>' for c,cod,n in
 [('#E8973C','ST','stalp'),('#3F8FA6','GR','grinda'),('#7BAE52','JO','joista'),('#E9C277','DL','dusumea'),('#B083C6','PO','polita'),('#AAB2BB','C1/C2','coltar'),('#E2663B','CF','contrafisa')])+'</div>')
FKEY=('<div class="fkey">'
 '<span class="fk"><svg width="16" height="16"><circle cx="8" cy="8" r="5" fill="#161413"/><line x1="5" y1="8" x2="11" y2="8" stroke="#fff" stroke-width="1.4"/></svg>cap surub (fata)</span>'
 '<span class="fk"><svg width="16" height="16"><circle cx="8" cy="8" r="5" fill="#fff" stroke="#161413" stroke-width="1.8" stroke-dasharray="2 1.6"/></svg>ascuns (pe spate)</span>'
 '<span class="fk"><svg width="26" height="14"><line x1="2" y1="7" x2="19" y2="7" stroke="#C2693A" stroke-width="2.4"/><path d="M19 7 L14 4 M19 7 L14 10" stroke="#C2693A" stroke-width="2.4" fill="none"/></svg>directie</span>'
 '<span class="fk"><b style="color:#161413">oblic</b> = la unghi</span>'
 '<div class="fnote">Folosim <b>suruburi + buloane</b>, nu cuie.</div></div>')

def pcard(code,qty,note):
    img,name=PARTS2.get(code,('',code))
    return f'<div class="pc"><div class="im"><img src="{img}" alt=""></div><div class="bd"><div class="r1"><span class="code">{code}</span><span class="qt">{qty}</span></div><div class="nm">{note}</div></div></div>'

def fisa_html(s):
    crit=s['diff']=='CRITIC'
    hero=s['steps'][0].get('svg') or (s['steps'][1].get('svg') if len(s['steps'])>1 else '')
    mt=f'<span class="mtag">~{s["time"]}</span><span class="mtag {("crit" if crit else "")}">{s["diff"]}</span>'+('<span class="mtag">2 persoane</span>' if s['ppl'] else '')
    parts=''.join(pcard(*p) for p in s['parts'] if p[0]!='—')
    if not parts: parts='<div class="pc"><div class="bd"><div class="nm">'+s['parts'][0][2]+'</div></div></div>'
    tools=''.join(f'<span class="tool">{t}</span>' for t in s['tools'])
    steps=''
    for i,st in enumerate(s['steps'],1):
        big=f'<div class="drawbox">{st["svg"]}</div>' if st.get('svg') else ''
        zoom=f'<div class="zoombox"><div class="zl">zoom &middot; cum se prinde</div>{st["zoom"]}</div>' if st.get('zoom') else ''
        warn='<div class="warn"><b>!</b><div><b>CRITIC</b> &mdash; opreste-te si verifica.</div></div>' if st.get('warn') else ''
        steps+=f'<div class="step"><div class="h"><div class="bn">{i}</div><div class="tx">{st["t"]}</div></div>{big}{zoom}{warn}</div>'
    checks=''.join(f'<li><span class="bx"></span><span>{c}</span></li>' for c in s['check'])
    return (f'<section class="fisa"><div class="fhead"><div><div class="kick">{s["kick"]}</div>'
            f'<h2>{s["title"]}</h2><div class="meta">{mt}</div></div><div class="herodraw">{hero}</div></div>'
            f'{LEG}<div class="sh">Piese</div><div class="pg">{parts}</div>'
            f'<div class="sh">Scule</div><div class="tools">{tools}</div>'
            f'<div class="sh">Pas cu pas</div>{FKEY}{steps}'
            f'<div class="sh">Gata cand</div><ul class="check">{checks}</ul></section>')


TOOLS=[('Boloboc / nivela cu furtun','verticalitate + orizontalitate'),('Bormasina + biti','suruburi Heco si gauri'),('Burghiu lemn 13 mm','gauri pentru buloane M12'),('Cheie 19 (M12)','buloane baza + polita'),('Cheie M10','balustrada (Faza 2)'),('Bomfaier','taiat tija filetata'),('Fierastrau / circular','taieri stalpi, dusumea, offcut'),('Echer mare','unghiuri drepte'),('Ruleta + creion','masuratori, trasaj'),('Cui 5 mm','distantier intre scanduri'),('Pensula','grund + ulei'),('2 persoane','la grinzi si ridicari')]
tools_html=''.join(f'<li><b>{t}</b><span>{d}</span></li>' for t,d in TOOLS)
SCULE_SECT=('<section class="sect"><div class="eyebrow">Trusa completa</div><h2>Scule de care ai nevoie</h2>''<p class="lead">Pregateste-le pe toate inainte de start. Pe fiecare fisa apar doar sculele etapei.</p>''<ul class="toollist">'+tools_html+'</ul></section>')

# ---- ce construim facts ----
FACTS=[('Inaltime podea','2200 mm'),('Cadru stalpi','2100 × 1780 mm'),('Balcon (consola)','+700 mm'),
 ('Grinzi','glulam 90×200'),('Joiste','6 × 100×100'),('Balustrada','1 m, goluri sub 9 cm'),('Copac','corcodus Ø160, masa')]
facts=''.join(f'<li><span>{k}</span><b>{v}</b></li>' for k,v in FACTS)
mat_html=''
for gh,items in MAT:
    cards=''.join(pcard(c,q,n) for c,q,n in items)
    mat_html+=f'<div class="mgrp"><div class="gh">{gh}</div><div class="pg">{cards}</div></div>'
safe_html=''.join(f'<div class="scard"><h3>{t}</h3><p>{p}</p></div>' for t,p in SAFETY)
fise_html=''.join(fisa_html(s) for s in DATA)

OUT=PROJ+'/PDF/Manual-Faza-1-complet.pdf'
TOCCSS="<style>.toc{list-style:none;padding:0;margin:6mm 0 0}.toc li{display:flex;align-items:baseline;gap:3mm;padding:2.4mm 0;border-bottom:1px solid var(--line);font-size:11.5pt}.toc .tl{color:var(--ink)}.toc .tp{margin-left:auto;font-family:'Space Mono',monospace;font-weight:700;color:var(--acc)}.toc .num{font-family:'Space Mono',monospace;color:var(--faint);width:9mm;display:inline-block}</style>"
DOC=f'''<!doctype html><html lang="ro"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
{CSS}{TOCCSS}</head><body>
<div class="cover"><div class="scrim"></div><div class="ct">
  <div class="kick">Manual de constructie · Faza 1</div>
  <h1>Casuta<br>din copac</h1>
  <div class="sub">Platforma pe patru stalpi, langa corcodusul din gradina — pas cu pas, pentru Tudor si tata.</div>
  <div class="foot"><span>Tudor &amp; tata · 2026</span><span>11 etape · platforma + balcon</span></div>
</div></div>
<section class="sect"><div class="eyebrow">Imaginea de ansamblu</div><h2>Ce construim</h2>
  <p class="lead">O casuta ridicata la 2,2 m pe patru stalpi (nu in copac — corcodusul e prea subtire ca s-o tina). In spate, langa gard, partea inchisa; in fata, un balcon deschis care iese 700 mm peste stalpi. Copacul trece prin podeaua balconului si il retezam ca masuta. <b>Numerotam stalpii: S1-S2 = spate (raman lungi, 4 m), S3-S4 = fata (se taie la +1872).</b></p>
  <div class="cc"><div class="draw">{cover_hero()}</div><ul class="facts">{facts}</ul></div>
</section>
__TOC__
<section class="sect"><div class="eyebrow">De ce ai nevoie</div><h2>Materiale</h2>
  <p class="lead">Toate piesele, cu codul lor (acelasi cod in toate desenele). Ce ai deja, ce e in comanda Hornbach si ce iei din offcut.</p>
  {mat_html}
</section>
{SCULE_SECT}
{fise_html}
<section class="sect"><div class="eyebrow">Inainte de joaca</div><h2>Siguranta &amp; verificare</h2>
  <p class="lead">Cinci reguli care nu se negociaza — un copil va sta la 2,2 m.</p>
  <div class="safe">{safe_html}</div>
</section>
</body></html>'''
from weasyprint import HTML as _H
import fitz
def build(toc_html):
    open('book.html','w',encoding='utf-8').write(DOC.replace('__TOC__',toc_html))
    _H('book.html', base_url=PROJ+'/').write_pdf(OUT)
# pasul 1: cuprins gol (acelasi numar de randuri => paginatie stabila)
entries=[('','Ce construim','Imaginea de ansamblu'),('','Materiale','De ce ai nevoie'),('','Scule','Trusa completa')]
entries+=[(str(s['n']),s['title'],'FISA'+str(s['n'])+'/11') for s in DATA]
entries+=[('','Siguranta &amp; verificare','Inainte de joaca')]
def toc(rowsdata):
    li=''.join(f'<li><span class="num">{n}</span><span class="tl">{lbl}</span><span class="tp">{pg}</span></li>' for n,lbl,pg in rowsdata)
    return f'<section class="sect"><div class="eyebrow">Navigare</div><h2>Cuprins</h2><ul class="toc">{li}</ul></section>'
build(toc([(n,lbl,'··') for n,lbl,_ in entries]))
d=fitz.open(OUT)
def pageof(needle):
    nn=needle.replace(' ','').upper()
    for i in range(d.page_count):
        if nn in d[i].get_text().replace(' ','').upper(): return str(i+1)
    return ''
rows=[(n,lbl,pageof(key)) for n,lbl,key in entries]
d.close()
build(toc(rows))
print('Manual cu cuprins scris,', len(DATA),'fise')
