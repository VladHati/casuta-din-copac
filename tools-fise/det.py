# -*- coding: utf-8 -*-
# Detalii de prindere, 2 vederi, simboluri clare (gandit ca IKEA).
INK='#161413'; ACC='#C2693A'
C={'post':'#E8973C','beam':'#3F8FA6','joist':'#7BAE52','deck':'#E9C277','polita':'#B083C6','metal':'#AAB2BB','brace':'#E2663B','tree':'#A56B41'}
def rect(x,y,w,h,fill,r=3):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{INK}" stroke-width="2.4"/>'
def txt(x,y,s,col='#5C574E',sz=10,anc='middle',w=400):
    return f'<text x="{x}" y="{y}" text-anchor="{anc}" font-family="Space Mono,monospace" font-size="{sz}" fill="{col}" font-weight="{w}">{s}</text>'
def cap(cx,cy):  # cap surub vizibil
    return f'<circle cx="{cx}" cy="{cy}" r="5.6" fill="{INK}"/><line x1="{cx-3.4}" y1="{cy}" x2="{cx+3.4}" y2="{cy}" stroke="#fff" stroke-width="1.4"/>'
def hidden(cx,cy):  # surub din spate / ascuns
    return f'<circle cx="{cx}" cy="{cy}" r="5.6" fill="#fff" stroke="{INK}" stroke-width="2" stroke-dasharray="2.4 2"/>'
def arrow(x1,y1,x2,y2,col=ACC,w=2.6):
    import math; a=math.atan2(y2-y1,x2-x1)
    h=''.join(f'<line x1="{x2}" y1="{y2}" x2="{x2-11*math.cos(a+d)}" y2="{y2-11*math.sin(a+d)}" stroke="{col}" stroke-width="{w}"/>' for d in (2.5,-2.5))
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"/>'+h
def badge(cx,cy,s):
    wbed=12+len(s)*7.4
    return f'<rect x="{cx-wbed/2}" y="{cy-9}" width="{wbed}" height="18" rx="5" fill="{INK}"/>'+txt(cx,cy+4,s,'#fff',11,'middle',700)

def panel(left,right,caption):
    # left/right = (title, body_svg) cu coord locale 0..176 x, 0..150 y
    def view(ox,title,body):
        return (f'<g transform="translate({ox},26)">'
                f'<rect x="0" y="0" width="176" height="158" rx="12" fill="#FBFAF8" stroke="#E7E3DB" stroke-width="1.5"/>'
                f'{txt(88,-8,title,ACC,10.5,"middle",700)}{body}</g>')
    return (f'<svg viewBox="0 0 380 220" xmlns="http://www.w3.org/2000/svg">'
            f'{view(6,left[0],left[1])}{view(198,right[0],right[1])}'
            f'<rect x="6" y="192" width="368" height="24" rx="7" fill="#fff" stroke="{ACC}" stroke-width="1.4"/>'
            f'{txt(190,208,caption,ACC,11.5,"middle",700)}</svg>')

# --- B2 baza stalp ---
B2=panel(
 ('VEDERE DIN FATA',
  rect(74,16,34,118,C['post'])+
  f'<path d="M64 134 v16 h48 v-16" fill="none" stroke="{INK}" stroke-width="3"/>'+rect(64,150,48,10,C['metal'])+
  cap(70,70)+cap(112,70)+arrow(40,70,62,70)+arrow(136,70,114,70)+txt(88,178,'papuc U',  '#5C574E',9)),
 ('DE SUS',
  rect(66,46,46,46,C['post'])+f'<path d="M58 40 h62 v62 h-62" fill="none" stroke="{INK}" stroke-width="3"/>'+
  cap(62,69)+cap(116,69)+txt(88,120,'bulon prin aripi',  '#5C574E',9)),
 'B2 x2 / stalp · M12 · strange cu cheia 19')

# --- B1 polita ---
B1=panel(
 ('LATERAL',
  rect(30,16,40,130,C['post'])+rect(70,60,52,46,C['polita'])+
  cap(60,76)+cap(60,100)+hidden(36,76)+hidden(36,100)+
  txt(96,128,'polita',  '#5C574E',9)+txt(150,70,'cap',ACC,9)+txt(150,150,'piulita spate',ACC,9)),
 ('DE SUS',
  rect(40,54,46,46,C['post'])+rect(86,62,40,30,C['polita'])+cap(64,77)+hidden(120,77)+
  txt(88,120,'prin polita -> stalp',  '#5C574E',9)),
 'B1 x2 / polita · cap pe fata, piulita pe spate')

# --- H1 grinda spate (oblic/toe) ---
H1B=panel(
 ('LATERAL',
  rect(28,30,40,116,C['post'])+rect(64,40,60,30,C['beam'])+rect(64,70,30,26,C['polita'])+
  arrow(108,52,86,86,ACC)+cap(86,86)+
  f'<path d="M96 70 a18 18 0 0 0 -10 16" fill="none" stroke="{ACC}" stroke-width="1.4"/>'+txt(120,64,'~30 grade',ACC,9,'start')+
  txt(150,150,'OBLIC (toe)',ACC,9)),
 ('DE SUS',
  rect(40,30,96,40,C['beam'])+rect(40,30,40,40,C['post'])+cap(70,46)+cap(70,58)+
  txt(100,120,'2 suruburi',  '#5C574E',9)),
 'H1 oblic in stalp · 2 buc · tin grinda lipita')

# --- C1 grinda fata pe varf ---
C1=panel(
 ('FATA A',
  rect(64,70,46,76,C['post'])+rect(40,30,94,40,C['beam'])+rect(54,52,16,70,C['metal'])+
  cap(62,64)+cap(62,50)+cap(62,96)+cap(62,118)+
  txt(150,56,'2 in grinda',ACC,9,'start')+txt(150,108,'2 in stalp',ACC,9,'start')),
 ('FATA B (opus)',
  rect(64,70,46,76,C['post'])+rect(40,30,94,40,C['beam'])+rect(104,52,16,70,C['metal'])+
  cap(112,64)+cap(112,50)+cap(112,96)+cap(112,118)+txt(88,138,'inca un coltar',  '#5C574E',9)),
 'C1 x2 / stalp · 2 suruburi in stalp + 2 in grinda, fiecare')

# --- C2 joista anti-lift ---
C2=panel(
 ('LATERAL',
  rect(34,86,120,40,C['beam'])+rect(78,30,40,56,C['joist'])+rect(118,60,14,52,C['metal'])+
  cap(126,72)+cap(126,86)+cap(126,104)+arrow(98,28,98,12,ACC)+txt(98,150,'',  '#5C574E',9)+
  txt(150,150,'ridicare',ACC,9)),
 ('DE SUS',
  rect(30,60,120,30,C['beam'])+rect(76,40,40,70,C['joist'])+cap(120,66)+cap(120,84)+
  txt(88,128,'coltar pe lateral',  '#5C574E',9)),
 'C2 x2 / joista (fata + spate) · TOTAL 12')

# --- H3 blocaj ---
H3=panel(
 ('LATERAL',
  rect(28,30,40,120,C['joist'])+rect(120,30,40,120,C['joist'])+rect(60,70,62,40,'#CBA24B')+
  arrow(74,56,62,84,ACC)+cap(62,84)+arrow(108,56,120,84,ACC)+cap(120,84)+txt(91,128,'BL',INK,11,'middle',700)),
 ('SUS',
  rect(40,40,30,90,C['joist'])+rect(116,40,30,90,C['joist'])+rect(70,70,46,30,'#CBA24B')+cap(78,85)+cap(108,85)+
  txt(93,150,'peste grinda',  '#5C574E',9)),
 'H3 oblic, cate 1-2 / capat')

# --- CF contrafisa ---
CF=panel(
 ('CAPAT pe stalp',
  rect(40,20,34,130,C['post'])+f'<polygon points="74,70 100,70 150,150 124,150" fill="{C["brace"]}" stroke="{INK}" stroke-width="2.4"/>'+
  cap(86,84)+cap(94,98)+cap(102,112)+txt(150,60,'3 suruburi',ACC,9,'start')),
 ('directie',
  f'<polygon points="40,40 64,40 150,150 126,150" fill="{C["brace"]}" stroke="{INK}" stroke-width="2.4"/>'+
  arrow(60,60,84,92,ACC)+cap(52,52)+cap(64,68)+cap(76,84)+txt(96,150,'taie pe potriveala',  '#5C574E',9)),
 'H1 x3 / fiecare capat · fara coltar')

# --- H4 dusumea ---
H4=panel(
 ('DE SUS',
  rect(20,30,40,130,C['joist'])+rect(116,30,40,130,C['joist'])+
  rect(8,64,160,30,C['deck'])+cap(40,79)+cap(136,79)+txt(88,150,'2 / joista',  '#5C574E',9)),
 ('LATERAL',
  rect(30,96,116,30,C['joist'])+rect(34,66,52,28,C['deck'])+rect(92,66,52,28,C['deck'])+
  cap(60,80)+cap(118,80)+f'<line x1="86" y1="60" x2="92" y2="60" stroke="{ACC}" stroke-width="2.6"/>'+txt(89,52,'5 mm',ACC,9)),
 'H4 x2 / joista · INOX · cui doar ca distantier')

# --- RAIL balustrada ---
RAIL=panel(
 ('LATERAL',
  rect(20,150,150,16,C['deck'])+rect(30,128,140,18,C['joist'])+rect(70,30,26,116,C['post'])+
  cap(76,118)+cap(76,138)+txt(150,60,'in CADRU',ACC,9,'start')+txt(96,184,'nu in dusumea!',ACC,9)),
 ('',
  f'<line x1="40" y1="40" x2="40" y2="150" stroke="{C["post"]}" stroke-width="12" stroke-linecap="round"/>'+
  f'<line x1="136" y1="40" x2="136" y2="150" stroke="{C["post"]}" stroke-width="12" stroke-linecap="round"/>'+
  f'<line x1="40" y1="46" x2="136" y2="46" stroke="{C["post"]}" stroke-width="9" stroke-linecap="round"/>'+
  ''.join(f'<line x1="{x}" y1="50" x2="{x}" y2="150" stroke="{INK}" stroke-width="2"/>' for x in (64,84,104))+
  txt(88,150,'gol < 9 cm',ACC,9)),
 'Stalpisor bulonat de cadru · gol intre sipci < 9 cm')

DETS={'B2':B2,'B1':B1,'H1B':H1B,'C1':C1,'C2':C2,'H3':H3,'CF':CF,'H4':H4,'RAIL':RAIL}
import pickle; pickle.dump(DETS,open('dets.pkl','wb'))
print('detalii prinderi:', list(DETS))
