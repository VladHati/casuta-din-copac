# -*- coding: utf-8 -*-
# Detalii de prindere, 2 vederi, text DOAR scurt in interior; descrierea in caption (fara taieri).
INK='#161413'; ACC='#C2693A'
C={'post':'#E8973C','beam':'#3F8FA6','joist':'#7BAE52','deck':'#E9C277','polita':'#B083C6','metal':'#AAB2BB','brace':'#E2663B','tree':'#A56B41'}
def rect(x,y,w,h,fill,r=3): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{INK}" stroke-width="2.4"/>'
def cap(cx,cy): return f'<circle cx="{cx}" cy="{cy}" r="5.4" fill="{INK}"/><line x1="{cx-3.2}" y1="{cy}" x2="{cx+3.2}" y2="{cy}" stroke="#fff" stroke-width="1.4"/>'
def hidden(cx,cy): return f'<circle cx="{cx}" cy="{cy}" r="5.4" fill="#fff" stroke="{INK}" stroke-width="2" stroke-dasharray="2.4 2"/>'
def tag(cx,cy,s,col=ACC): # eticheta mica, centrata (text scurt!)
    return f'<text x="{cx}" y="{cy}" text-anchor="middle" font-family="Space Mono,monospace" font-size="11" font-weight="700" fill="{col}">{s}</text>'
def lbl(cx,cy,s,col='#5C574E'):
    return f'<text x="{cx}" y="{cy}" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="{col}">{s}</text>'
import math
def arr(x1,y1,x2,y2,col=ACC,w=2.6):
    a=math.atan2(y2-y1,x2-x1)
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"/>'
            +''.join(f'<line x1="{x2}" y1="{y2}" x2="{x2-10*math.cos(a+d)}" y2="{y2-10*math.sin(a+d)}" stroke="{col}" stroke-width="{w}"/>' for d in (2.5,-2.5)))

# panou: 2 vederi (208x170) + caption full-width jos. Tot textul intern e scurt si in interior.
def panel(left,right,caption):
    def view(ox,title,body):
        return (f'<g transform="translate({ox},30)">'
                f'<rect x="0" y="0" width="208" height="170" rx="12" fill="#FBFAF8" stroke="#E7E3DB" stroke-width="1.5"/>'
                f'<text x="104" y="-9" text-anchor="middle" font-family="Space Mono,monospace" font-size="11" font-weight="700" fill="{ACC}">{title}</text>'
                f'{body}</g>')
    return (f'<svg viewBox="0 0 460 252" xmlns="http://www.w3.org/2000/svg" font-family="Space Grotesk,Arial,sans-serif">'
            f'{view(12,left[0],left[1])}{view(240,right[0],right[1])}'
            f'<rect x="12" y="222" width="436" height="24" rx="7" fill="#fff" stroke="{ACC}" stroke-width="1.4"/>'
            f'<text x="230" y="238" text-anchor="middle" font-family="Space Mono,monospace" font-size="12" font-weight="700" fill="{ACC}">{caption}</text></svg>')

B2=panel(('DIN FATA',
   rect(86,18,36,118,C['post'])+f'<path d="M76 136 v18 h56 v-18" fill="none" stroke="{INK}" stroke-width="3"/>'+rect(76,150,56,12,C['metal'])
   +cap(82,72)+cap(126,72)+arr(54,72,72,72)+arr(154,72,136,72)+lbl(104,182,'papuc U')),
 ('DE SUS',
   rect(80,52,48,48,C['post'])+f'<path d="M70 44 h68 v68 h-68" fill="none" stroke="{INK}" stroke-width="3"/>'+cap(74,76)+cap(134,76)+tag(104,150,'M12')),
 'B2  x2 / stalp  ·  strange cu cheia 19')

B1=panel(('LATERAL',
   rect(46,16,40,150,C['post'])+rect(86,66,52,46,C['polita'])+cap(74,82)+cap(74,106)+hidden(52,82)+hidden(52,106)+lbl(112,134,'polita')),
 ('DE SUS',
   rect(60,56,48,48,C['post'])+rect(108,64,40,32,C['polita'])+cap(86,80)+hidden(140,80)+lbl(104,150,'prin polita')),
 'B1  x2 / polita  ·  cap pe fata, piulita pe spate')

H1B=panel(('LATERAL',
   rect(40,34,40,118,C['post'])+rect(76,44,72,30,C['beam'])+rect(76,74,30,26,C['polita'])
   +arr(126,56,98,90)+cap(98,90)+tag(182,52,'~30')),
 ('DE SUS',
   rect(60,40,108,40,C['beam'])+rect(60,40,44,40,C['post'])+cap(92,50)+cap(92,64)+cap(92,78)+tag(150,120,'x3')),
 'H1 oblic in stalp  ·  x3  ·  tine grinda lipita')

C1=panel(('FATA A',
   rect(78,72,46,82,C['post'])+rect(54,34,108,38,C['beam'])+rect(66,54,18,74,C['metal'])
   +cap(75,50)+cap(75,64)+cap(75,100)+cap(75,124)),
 ('FATA B (opus)',
   rect(78,72,46,82,C['post'])+rect(54,34,108,38,C['beam'])+rect(124,54,18,74,C['metal'])
   +cap(133,50)+cap(133,64)+cap(133,100)+cap(133,124)),
 'C1: 2 coltare / stalp  ·  fiecare cu 2 in stalp + 2 in grinda')

C2=panel(('LATERAL',
   rect(40,96,128,38,C['beam'])+rect(86,40,44,56,C['joist'])+rect(130,64,16,54,C['metal'])
   +cap(138,76)+cap(138,92)+cap(138,108)+arr(108,38,108,20)+tag(150,160,'ridicare')),
 ('DE SUS',
   rect(36,64,136,32,C['beam'])+rect(86,44,40,72,C['joist'])+cap(132,72)+cap(132,88)+lbl(104,150,'pe lateral')),
 'C2  x2 / joista (fata + spate)  ·  TOTAL 12')

H3=panel(('LATERAL',
   rect(36,30,40,124,C['joist'])+rect(132,30,40,124,C['joist'])+rect(72,72,64,40,'#CBA24B')
   +arr(86,58,74,86)+cap(74,86)+arr(122,58,134,86)+cap(134,86)+tag(104,98,'BL',INK)),
 ('DE SUS',
   rect(46,40,32,96,C['joist'])+rect(130,40,32,96,C['joist'])+rect(78,72,52,32,'#CBA24B')+cap(86,88)+cap(122,88)+lbl(104,156,'peste grinda')),
 'H3 oblic  ·  cate 1-2 / capat')

CF=panel(('CAPAT pe stalp',
   rect(44,20,34,140,C['post'])+f'<polygon points="78,74 104,74 160,160 134,160" fill="{C["brace"]}" stroke="{INK}" stroke-width="2.4"/>'
   +cap(90,88)+cap(98,102)+cap(106,116)+tag(150,60,'x3')),
 ('DIRECTIE',
   f'<polygon points="44,44 70,44 168,160 142,160" fill="{C["brace"]}" stroke="{INK}" stroke-width="2.4"/>'
   +lbl(66,150,'taie pe masura')),
 'H1  x3 / fiecare capat  ·  fara coltar')

H4=panel(('DE SUS',
   rect(24,30,40,128,C['joist'])+rect(140,30,40,128,C['joist'])+rect(14,66,184,30,C['deck'])+cap(44,81)+cap(160,81)),
 ('LATERAL',
   rect(34,100,140,30,C['joist'])+rect(40,68,56,28,C['deck'])+rect(104,68,56,28,C['deck'])+cap(64,82)+cap(128,82)
   +f'<line x1="96" y1="60" x2="104" y2="60" stroke="{ACC}" stroke-width="2.6"/>'+tag(100,52,'5 mm')),
 'H4  x2 / joista  ·  INOX  ·  gol de 5 mm')

RAIL=panel(('LATERAL',
   rect(20,150,168,14,C['deck'])+rect(30,128,148,18,C['joist'])+rect(78,30,26,116,C['post'])
   +cap(84,116)+cap(84,138)+tag(150,70,'in cadru')),
 ('FATA',
   f'<line x1="40" y1="40" x2="40" y2="150" stroke="{C["post"]}" stroke-width="12" stroke-linecap="round"/>'
   +f'<line x1="160" y1="40" x2="160" y2="150" stroke="{C["post"]}" stroke-width="12" stroke-linecap="round"/>'
   +f'<line x1="40" y1="46" x2="160" y2="46" stroke="{C["post"]}" stroke-width="9" stroke-linecap="round"/>'
   +''.join(f'<line x1="{x}" y1="50" x2="{x}" y2="150" stroke="{INK}" stroke-width="2"/>' for x in (72,96,120))+tag(104,120,'<9 cm')),
 'Stalpisor bulonat de CADRU  ·  goluri sub 9 cm')

TABLE=panel(('LATERAL',
   rect(20,118,168,14,C['deck'])+rect(92,28,24,104,C['tree'])
   +f'<ellipse cx="104" cy="40" rx="44" ry="9" fill="#C99A5E" stroke="{INK}" stroke-width="2.2"/>'
   +f'<line x1="84" y1="118" x2="84" y2="132" stroke="{ACC}" stroke-width="2.4"/><line x1="116" y1="118" x2="116" y2="132" stroke="{ACC}" stroke-width="2.4"/>'
   +tag(104,150,'joc 3-5 cm')),
 ('REGULA',
   rect(40,120,128,14,C['deck'])+rect(70,70,68,50,C['deck'])+cap(104,96)
   +lbl(104,150,'blat pe cadru')+tag(104,58,'NU pe copac')),
 'Blatul pe cadrul lui propriu  ·  NICIODATA pe copac')

DETS={'B2':B2,'B1':B1,'H1B':H1B,'C1':C1,'C2':C2,'H3':H3,'CF':CF,'H4':H4,'RAIL':RAIL,'TABLE':TABLE}
import pickle; pickle.dump(DETS,open('dets.pkl','wb'))
print('det rescris:', list(DETS))
