# -*- coding: utf-8 -*-
import pickle
import fb
from fb import PARTS, PROJ, render, PS, W, D, JX, BEAMB, JOB, DECKB, posts_stub, polite_g, beam_back_g, beam_front_g, joists_g, deck_g, g, N
DATA=pickle.load(open('data.pkl','rb'))

# ---- hero coperta: platforma finala, colorata ----
def cover_hero():
    base=posts_stub()+polite_g()+[beam_back_g(),beam_front_g()]+joists_g()+deck_g(15)
    top=DECKB+28
    rail=[]
    for (x,z) in [(20,-680),(W-20,-680),(20,D-20),(W-20,D-20)]:
        rail.append({'p1':(x,top,z),'p2':(x,top+1000,z),'thick':13,'col':fb.PAL['post']})
    rail+=[{'p1':(20,top+980,-680),'p2':(W-20,top+980,-680),'thick':10,'col':fb.PAL['post']},
           {'p1':(20,top+980,-680),'p2':(20,top+980,D-20),'thick':10,'col':fb.PAL['post']},
           {'p1':(W-20,top+980,-680),'p2':(W-20,top+980,D-20),'thick':10,'col':fb.PAL['post']}]
    tree=[{'x':450,'y':1280,'z':-300,'dx':160,'dy':1700,'dz':160,'mat':'tree','hl':True}]
    return render(base+tree, struts=rail, W=820)

# ---- sectiune materiale (curata, un singur stil) ----
MAT=[('le ai deja',[('ST','4','stalpi KVH 100x100'),('JO','4','barne Leroy (din 6 joiste)'),('PAP','4','papuci, deja in beton'),('F2','1','grund Köber 4 L')]),
     ('in comanda Hornbach (4.101 lei)',[('GR','2','grinzi glulam 90x200'),('JO','2','completare joiste'),('DL','17','dusumea larice'),('C1','4','coltare 100x90'),('C2','12','coltare 90x65'),('H1','1 pac','Heco 8x200'),('H2','1 pac','Heco 6x100'),('H3','1 pac','Heco 6x80'),('H4','2 pac','inox 5x60'),('B1','1','tija M12'),('B2','1 pac','M12x120 baza'),('B3','1 pac','saibe M12'),('B4','1 pac','piulite M12'),('F1','2','ulei tec')]),
     ('din offcut / de luat',[('PO','2','polite (offcut)'),('BL','~10','blocaje (offcut)'),('CF','6','contrafise (offcut)'),('PT','~6','proptele'),('F3','1','topcoat colorat')])]
PARTS2=dict(PARTS); PARTS2['F2']=('POZE/kober.jpg','Grund Köber 4 L'); PARTS2['F3']=('POZE/lemn.png','Topcoat colorat')

SAFETY=[('Inaltime 2,2 m','Balustrada de 1 m jur-imprejur, goluri sub 9 cm, poarta pe partea S3. Sub platforma, sol moale (scoarta/nisip) pe ~5 m².'),
 ('Copacul nu tine nimic','Corcodusul trece liber prin gaura cu joc de 3-5 cm. Blatul mesei se prinde de cadrul propriu, NICIODATA de copac.'),
 ('Ordinea de siguranta','Proptelele raman pana montezi contravantuirile. Nimeni nu sta pe consola (balcon) inainte de contrafisa de sub nas.'),
 ('Legaturi verificate','Coltare anti-ridicare la fiecare joista; coltar anti-smulgere la grinda din spate. Dupa montaj, reverifica strangerea buloanelor portante (polite + baza).'),
 ('Lemn protejat','Grund pe toata structura, ulei pe dusumea. Capetele de stalp in papuc, cu drenaj, sa nu putrezeasca.')]

CSS='''<style>
@page{size:A4;margin:15mm 14mm 16mm;@bottom-center{content:"Casuta din copac · Faza 1 · pagina " counter(page);font-family:'Space Mono',monospace;font-size:8.5pt;color:#A39C8E}}
@page:first{margin:0;@bottom-center{content:""}}
:root{--ink:#161413;--soft:#5C574E;--faint:#9A9388;--line:#E7E3DB;--acc:#C2693A;--wash:#FAF8F4;--crit:#C2412B;}
*{box-sizing:border-box}
body{margin:0;color:var(--ink);font-family:'Space Grotesk',system-ui,sans-serif;line-height:1.5;font-size:11pt}
.mono{font-family:'Space Mono',monospace}
h1,h2,h3{font-family:'Fraunces',Georgia,serif;font-weight:600;margin:0;letter-spacing:-.01em}
/* COVER */
.cover{height:297mm;padding:24mm 20mm;display:flex;flex-direction:column;background:linear-gradient(180deg,#FFFFFF,#FBF8F3);break-after:page}
.cover .kick{font-family:'Space Mono',monospace;font-size:11pt;letter-spacing:.28em;text-transform:uppercase;color:var(--acc)}
.cover h1{font-size:52pt;line-height:1;margin:6mm 0 4mm}
.cover .sub{font-size:14pt;color:var(--soft);max-width:130mm}
.cover .hero{margin:auto 0;display:flex;justify-content:center}
.cover .hero svg{width:100%;max-width:175mm;height:auto}
.cover .foot{display:flex;justify-content:space-between;border-top:2px solid var(--ink);padding-top:5mm;font-family:'Space Mono',monospace;font-size:9.5pt;color:var(--soft)}
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
.lg{display:inline-flex;align-items:center;gap:2mm;font-size:9pt;color:var(--soft)}.lg i{width:3.4mm;height:3.4mm;border-radius:1mm;border:1.6px solid #161413}
.tools{display:flex;flex-wrap:wrap;gap:2mm;margin-bottom:2mm}
.tool{font-family:'Space Mono',monospace;font-size:8.6pt;border:1px solid var(--line);background:var(--wash);border-radius:2mm;padding:1.4mm 2.6mm;color:var(--soft)}
.fkey{display:flex;flex-wrap:wrap;gap:2mm 5mm;margin:0 0 4mm;padding:3mm 3.5mm;background:var(--wash);border:1px solid var(--line);border-radius:3mm}
.fk{display:inline-flex;align-items:center;gap:2mm;font-size:9pt;color:var(--soft)}
.fnote{flex-basis:100%;margin-top:1mm;font-size:9pt;color:var(--soft)}.fnote b{color:#161413}
.step{padding:4mm 0;border-top:1px solid var(--line);break-inside:avoid}
.step .h{display:flex;gap:4mm;align-items:flex-start}
.bn{flex:0 0 9mm;width:9mm;height:9mm;border-radius:50%;background:var(--ink);color:#fff;display:grid;place-items:center;font-family:'Space Mono',monospace;font-weight:700;font-size:12pt}
.tx{font-size:11pt;line-height:1.45}
.step .drawbox,.step .zoombox,.step .warn{margin-left:13mm}
.drawbox{margin-top:3mm;border:1px solid var(--line);border-radius:3mm;background:var(--wash);padding:3mm}
.drawbox svg{width:100%;height:auto;display:block}
.zoombox{margin-top:3mm;border:1.4px dashed var(--acc);border-radius:3mm;background:#fff;padding:3mm 3.5mm;max-width:165mm}
.zoombox .zl{font-family:'Space Mono',monospace;font-size:8.6pt;letter-spacing:.1em;text-transform:uppercase;color:var(--acc);margin:0 0 2mm;font-weight:700}
.zoombox svg{width:100%;height:auto;display:block}
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
</style>'''

LEG=('<div class="legend">'+''.join(f'<span class="lg"><i style="background:{c}"></i>{n}</span>' for c,n in
 [('#E8973C','stalp'),('#3F8FA6','grinda'),('#7BAE52','joista'),('#E9C277','dusumea'),('#B083C6','polita'),('#AAB2BB','coltar'),('#E2663B','diagonala')])+'</div>')
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

# ---- ce construim facts ----
FACTS=[('Inaltime podea','2200 mm'),('Cadru stalpi','2100 × 1780 mm'),('Balcon (consola)','+700 mm'),
 ('Grinzi','glulam 90×200'),('Joiste','6 × 100×100'),('Balustrada','1 m, goluri <9 cm'),('Copac','corcodus Ø160, masa')]
facts=''.join(f'<li><span>{k}</span><b>{v}</b></li>' for k,v in FACTS)
mat_html=''
for gh,items in MAT:
    cards=''.join(pcard(c,q,n) for c,q,n in items)
    mat_html+=f'<div class="mgrp"><div class="gh">{gh}</div><div class="pg">{cards}</div></div>'
safe_html=''.join(f'<div class="scard"><h3>{t}</h3><p>{p}</p></div>' for t,p in SAFETY)
fise_html=''.join(fisa_html(s) for s in DATA)

HTML=f'''<!doctype html><html lang="ro"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
{CSS}</head><body>
<div class="cover">
  <div><div class="kick">Manual de constructie · Faza 1</div>
  <h1>Casuta<br>din copac</h1>
  <div class="sub">Platforma pe patru stalpi, pas cu pas — pentru Tudor si tata. Fiecare etapa cu piese, desene si verificare.</div></div>
  <div class="hero">{cover_hero()}</div>
  <div class="foot"><span>Tudor &amp; tata · 2026</span><span>11 etape · platforma + balcon</span></div>
</div>
<section class="sect"><div class="eyebrow">Imaginea de ansamblu</div><h2>Ce construim</h2>
  <p class="lead">O casuta ridicata la 2,2 m pe patru stalpi (nu in copac — corcodusul e prea subtire ca s-o tina). In spate, langa gard, partea inchisa; in fata, un balcon deschis care iese 700 mm peste stalpi. Copacul trece prin podeaua balconului si il retezam ca masuta.</p>
  <div class="cc"><div class="draw">{cover_hero()}</div><ul class="facts">{facts}</ul></div>
</section>
<section class="sect"><div class="eyebrow">De ce ai nevoie</div><h2>Materiale</h2>
  <p class="lead">Toate piesele, cu codul lor (acelasi cod in toate desenele). Ce ai deja, ce e in comanda Hornbach si ce iei din offcut.</p>
  {mat_html}
</section>
{fise_html}
<section class="sect"><div class="eyebrow">Inainte de joaca</div><h2>Siguranta &amp; verificare</h2>
  <p class="lead">Cinci reguli care nu se negociaza — un copil va sta la 2,2 m.</p>
  <div class="safe">{safe_html}</div>
</section>
</body></html>'''
open('book.html','w',encoding='utf-8').write(HTML)
print('book.html scris,', len(DATA),'fise')

# scrie manualul direct in proiect
from weasyprint import HTML as _H
_H('book.html').write_pdf(PROJ+'/PDF/Manual-Faza-1-complet.pdf')
print('Manual-Faza-1-complet.pdf scris in proiect')
