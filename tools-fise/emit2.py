# -*- coding: utf-8 -*-
import pickle
from fb import PARTS, PROJ
DATA=pickle.load(open('data.pkl','rb'))
NAV='''<header class="topnav"><div class="tn-in"><a class="tn-logo" href="index.html"><span class="tn-mark">&#9651;</span>Casuta din copac</a><nav class="tn-links">
<a href="timeline.html" data-k="stadiu">Stadiu</a><a href="ghid-montaj.html" data-k="ghid">Ghid</a><a href="materiale.html" data-k="materiale">Materiale</a><a href="imbinari.html" data-k="imbinari">Imbinari</a><a href="modele-3d.html" data-k="3d">3D</a><a href="casuta-din-copac.html" data-k="dosar">Dosar</a>
</nav></div><div class="tn-crumb"><a href="index.html">Acasa</a><span>&rsaquo;</span><a href="ghid-montaj.html">Ghid</a><span>&rsaquo;</span><a href="fise.html">Fise montaj</a><span>&rsaquo;</span><b>{cr}</b></div></header><script>(function(){{var p=new URLSearchParams(location.search);if(p.has("embed")){{document.documentElement.classList.add("emb");return;}}var a=document.querySelector('.tn-links a[data-k="ghid"]');if(a)a.classList.add("on");}})();</script>'''
CSS='''<style>
:root{--ink:#161413;--soft:#5C574E;--faint:#9A9388;--line:#E7E3DB;--acc:#C2693A;--paper:#FFFFFF;--wash:#FAF8F4;--crit:#C2412B;}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:'Space Grotesk',system-ui,sans-serif;line-height:1.5}
.wrap{max-width:920px;margin:0 auto;padding:0 22px}.mono{font-family:'Space Mono',monospace}a{color:var(--acc);text-decoration:none}
.fh{display:grid;grid-template-columns:1fr 1.1fr;gap:28px;align-items:center;padding:30px 0 24px;border-bottom:3px solid var(--ink)}
@media(max-width:760px){.fh{grid-template-columns:1fr}}
.fh .kick{font-family:'Space Mono',monospace;font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--acc)}
.fh h1{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:clamp(28px,4.6vw,44px);line-height:1.04;margin:8px 0 14px;letter-spacing:-.02em}
.meta{display:flex;flex-wrap:wrap;gap:8px}
.mtag{display:inline-flex;align-items:center;gap:6px;font-family:'Space Mono',monospace;font-size:11px;border:1.5px solid var(--ink);border-radius:999px;padding:5px 11px}
.mtag.crit{border-color:var(--crit);color:var(--crit)}
.herodraw{border:1px solid var(--line);border-radius:16px;background:var(--wash);padding:10px}.herodraw svg{width:100%;height:auto;display:block}
.stepart{position:relative;margin:0;display:block;line-height:0}.stepart img{width:100%;height:auto;display:block;border-radius:10px}.stepart .ovl{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.sec{padding:28px 0;border-bottom:1px solid var(--line)}
.sh{font-family:'Space Mono',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--faint);margin:0 0 16px}
.pg{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}@media(max-width:760px){.pg{grid-template-columns:repeat(2,1fr)}}
.pc{border:1px solid var(--line);border-radius:14px;overflow:hidden;background:#fff;display:flex;flex-direction:column}
.pc .im{height:96px;background:var(--wash);display:grid;place-items:center;border-bottom:1px solid var(--line)}
.pc .im img{max-width:88%;max-height:80px;object-fit:contain;mix-blend-mode:multiply}.pc .im .ph{font-family:'Space Mono',monospace;font-size:26px;color:#d9d2c6;font-weight:700}
.pc .bd{padding:9px 11px;display:flex;flex-direction:column;gap:3px}.pc .row1{display:flex;justify-content:space-between;align-items:center}
.pc .code{font-family:'Space Mono',monospace;font-weight:700;font-size:13px;background:var(--ink);color:#fff;border-radius:6px;padding:1px 8px}
.pc .qt{font-family:'Space Mono',monospace;font-weight:700;font-size:14px}.pc .nm{font-size:12px;font-weight:600;line-height:1.2}.pc .nt{font-size:11px;color:var(--soft)}
.legend{display:flex;flex-wrap:wrap;gap:14px;padding:14px 0 0}.lg{display:inline-flex;align-items:center;gap:7px;font-size:12.5px;color:var(--soft)}.lg i{width:16px;height:16px;border-radius:4px;border:2px solid #161413;display:inline-block}.lg b{color:#161413;font-family:'Space Mono',monospace}
.tools{display:flex;flex-wrap:wrap;gap:8px}.tool{font-family:'Space Mono',monospace;font-size:12px;border:1px solid var(--line);background:var(--wash);border-radius:8px;padding:7px 12px;color:var(--soft)}
.fkey{display:flex;flex-wrap:wrap;gap:10px 18px;margin:0 0 18px;padding:13px 15px;background:#FAF8F4;border:1px solid var(--line);border-radius:12px}
.fk{display:inline-flex;align-items:center;gap:7px;font-size:12.5px;color:var(--soft)}
.fnote{flex-basis:100%;margin-top:4px;font-size:12.5px;color:var(--soft)}.fnote b{color:#161413}
.step{padding:20px 0;border-top:1px solid var(--line)}.step .h{display:flex;gap:16px;align-items:flex-start}
.step:first-child{border-top:none}
.bn{flex:0 0 46px;width:46px;height:46px;border-radius:50%;background:var(--ink);color:#fff;display:inline-flex;align-items:center;justify-content:center;line-height:1;font-family:'Space Mono',monospace;font-weight:700;font-size:20px}
.step .tx{font-size:16.5px;line-height:1.5}.step .drawbox,.step .zoombox,.step .warn{margin-left:62px}
.drawbox{margin-top:14px;border:1px solid var(--line);border-radius:14px;background:var(--wash);padding:12px;text-align:center}.drawbox svg{max-height:360px;max-width:100%;width:auto;height:auto;display:inline-block}
.zoombox{margin-top:14px;display:block;border:1.5px dashed var(--acc);border-radius:14px;background:#fff;padding:12px 14px;max-width:620px}
.zoombox .zl{font-family:'Space Mono',monospace;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--acc);margin:0 0 8px;font-weight:700}
.zoombox svg{width:100%;height:auto;display:block}
.warn{display:flex;gap:10px;align-items:flex-start;margin-top:12px;background:#FBEEE4;border:1px solid #F0D8C4;border-left:4px solid var(--acc);border-radius:10px;padding:11px 13px;font-size:14px;color:#7a4a2c;max-width:640px}
.warn b{color:var(--crit);font-size:16px;line-height:1.1}
.check{list-style:none;padding:0;margin:0;display:grid;gap:10px}.check li{display:flex;align-items:flex-start;gap:11px;font-size:15px}
.check .bx{flex:0 0 auto;width:22px;height:22px;border:2px solid var(--ink);border-radius:6px;margin-top:1px}
.fnav{display:flex;justify-content:space-between;gap:12px;padding:26px 0 70px}
.fnav a{font-family:'Space Mono',monospace;font-size:13px;font-weight:700;border:1.5px solid var(--ink);border-radius:10px;padding:10px 16px;color:var(--ink)}
.fnav a:hover{background:var(--ink);color:#fff}.fnav a.dis{opacity:.3;pointer-events:none}
@media print{.topnav,.tn-crumb,.fnav{display:none!important}.sec,.step,.pc{break-inside:avoid}body{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
</style>'''
LEG=('<div class="legend">'
 '<span class="lg"><i style="background:#E8973C"></i><b>ST</b>&nbsp;stalp</span>'
 '<span class="lg"><i style="background:#3F8FA6"></i><b>GR</b>&nbsp;grinda</span>'
 '<span class="lg"><i style="background:#7BAE52"></i><b>JO</b>&nbsp;joista</span>'
 '<span class="lg"><i style="background:#E9C277"></i><b>DL</b>&nbsp;dusumea</span>'
 '<span class="lg"><i style="background:#B083C6"></i><b>PO</b>&nbsp;polita</span>'
 '<span class="lg"><i style="background:#AAB2BB"></i><b>C1/C2</b>&nbsp;coltar</span>'
 '<span class="lg"><i style="background:#E2663B"></i><b>CF</b>&nbsp;diagonala</span>'
 '</div>')
FKEY=('<div class="fkey">'
 '<span class="fk"><svg width="20" height="20"><circle cx="10" cy="10" r="6" fill="#161413"/><line x1="6.5" y1="10" x2="13.5" y2="10" stroke="#fff" stroke-width="1.6"/></svg>cap surub (fata vazuta)</span>'
 '<span class="fk"><svg width="20" height="20"><circle cx="10" cy="10" r="6" fill="#fff" stroke="#161413" stroke-width="2" stroke-dasharray="2.4 2"/></svg>surub/piulita ascuns (pe spate)</span>'
 '<span class="fk"><svg width="30" height="16"><line x1="3" y1="8" x2="22" y2="8" stroke="#C2693A" stroke-width="2.6"/><path d="M22 8 L16 4 M22 8 L16 12" stroke="#C2693A" stroke-width="2.6" fill="none"/></svg>directia de insurubare</span>'
 '<span class="fk"><b style="color:#161413">oblic</b> = la unghi (toe-screw)</span>'
 '<div class="fnote">Folosim <b>suruburi + buloane</b>, nu cuie. (Singurul cui e distantierul de 5 mm la dusumea.)</div>'
 '</div>')
def pcard(code,qty,note):
    if code=='—':
        return f'<div class="pc"><div class="im"><span class="ph">?</span></div><div class="bd"><div class="row1"><span class="code">—</span><span class="qt">{qty}</span></div><div class="nt">{note}</div></div></div>'
    img,name=PARTS.get(code,('',code))
    return f'<div class="pc"><div class="im"><img src="{img}" alt="{name}" loading="lazy"></div><div class="bd"><div class="row1"><span class="code">{code}</span><span class="qt">{qty}</span></div><div class="nm">{name}</div><div class="nt">{note}</div></div></div>'
def emit(s,prev,nxt):
    crit=s['diff']=='CRITIC'
    parts=''.join(pcard(*p) for p in s['parts'])
    tools=''.join(f'<span class="tool">{t}</span>' for t in s['tools'])
    hero=s['draw']
    steps=''
    for i,st in enumerate(s['steps'],1):
        big=f'<div class="drawbox">{st["svg"]}</div>' if st.get('svg') else ''
        zoom=f'<div class="zoombox"><div class="zl">zoom &middot; cum se prinde</div>{st["zoom"]}</div>' if st.get('zoom') else ''
        wt=st.get('warn')
        warn=f'<div class="warn"><b>!</b><div><b>CRITIC</b> &mdash; {wt}</div></div>' if wt else ''
        steps+=f'<div class="step"><div class="h"><div class="bn">{i}</div><div class="tx">{st["t"]}</div></div>{big}{zoom}{warn}</div>'
    checks=''.join(f'<li><span class="bx"></span><span>{c}</span></li>' for c in s['check'])
    mtags=f'<span class="mtag">~{s["time"]}</span><span class="mtag {("crit" if crit else "")}">{s["diff"]}</span>'+('<span class="mtag">2 persoane</span>' if s['ppl'] else '')
    pv=f'<a href="{prev}">&larr; Fisa anterioara</a>' if prev else '<a class="dis">&larr;</a>'
    nx=f'<a href="{nxt}">Fisa urmatoare &rarr;</a>' if nxt else '<a href="fise.html">Toate fisele</a>'
    html=f'''<!doctype html><html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{s["kick"]} — {s["title"]} · Casuta din copac</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
{CSS}<link rel="stylesheet" href="assets/site.css"><script defer src="assets/site.js"></script></head><body>
{NAV.format(cr="Fisa "+str(s["n"]))}
<div class="wrap">
 <section class="fh"><div><div class="kick">{s["kick"]}</div><h1>{s["title"]}</h1><div class="meta">{mtags}</div></div><div class="herodraw">{hero}</div></section>
 {LEG}
 <section class="sec"><div class="sh">Piese pentru aceasta etapa</div><div class="pg">{parts}</div></section>
 <section class="sec"><div class="sh">Scule</div><div class="tools">{tools}</div></section>
 <section class="sec"><div class="sh">Pas cu pas</div>{FKEY}{steps}</section>
 <section class="sec"><div class="sh">Gata cand</div><ul class="check">{checks}</ul></section>
 <div class="fnav">{pv}{nx}</div>
</div></body></html>'''
    open(f'{PROJ}/{s["slug"]}.html','w',encoding='utf-8').write(html)
for i,s in enumerate(DATA):
    emit(s, DATA[i-1]['slug']+'.html' if i>0 else None, DATA[i+1]['slug']+'.html' if i<len(DATA)-1 else None)
print('emis', len(DATA))
