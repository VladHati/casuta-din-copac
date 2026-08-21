MODEL: opus
EFFORT: xhigh

# BRIEF — desene la scara pentru fiecare etapa din ghid

## GOAL

Fiecare capitol din `GHID-CONSTRUCTIE-casa.html` capata desenele care ii lipsesc, ca sa se poata construi din ghid fara sa deschizi alt document. Azi capitolele noi au cate un singur desen general; E7 n-are niciunul.

Situatia curenta, numarata in HTML-ul construit:

| capitol | svg acum | trebuie |
|---|---|---|
| e3 peretele din spate | 4 | 4 *(nu se atinge)* |
| e4 peretii laterali | 1 | **5** |
| e5 peretele din fata | 1 | **4** |
| e6 acoperisul | 2 | **6** |
| e7 geamurile | 0 | **2** |

**13 desene noi.** Toate in `gen_ghid.py`, cu clasa `Fig` existenta, montate prin `build_ghid.py`. Nu se editeaza HTML direct, nu se adauga librarii.

E0 ramane cum e — blocul care cere pozele si cotele sta pe loc. Decizie Vlad: se face separat.

---

## REGULA CARE TINE TOTUL LEGAT

**Fiecare cota desenata se ia din constantele din capul lui `gen_ghid.py`, niciodata scrisa de mana ca sir.** `T`, `WALL_B`, `WALL_F`, `DEP_L`, `DEP_R`, `REZ_B`, `REZ_F`, `SPAN`, `SL`, `RAFT`, `EDGE`, `PAS`, `VB`, `PITCH_TXT`.

Daca un desen are nevoie de o cota care nu e constanta, **adaugi constanta**, nu textul. Motiv: geometria s-a mutat de trei ori in ultimele doua saptamani, si de fiecare data desenele au ramas in urma cu numere moarte scrise cu mana. A treia oara se opreste aici.

Constante noi de adaugat, daca nu exista deja:

```
VF   = 1600 - T          # verticala perete fata = 1552
VL   = [1573, 1645, 1722, 1794]   # verticale laterale, dinspre fata spre spate
GEAM = 490               # golul de geam lateral
GEAM_C = (543, 490, 542) # camp / gol / camp pe talpa laterala
PRAG = 950               # inaltimea pragului de geam lateral
STICLA = 440             # acrilicul, in gol de 490
BARA_F = 2155            # bara solida 100x60 a peretelui din fata
FER_F  = 570             # prag+buiandrug fereastra fata, intre jambe
```

---

## DESENELE

Stilul, paleta si grosimile de linie sunt cele din figurile existente (`INK`, `ACC`, `ACC2`, `MUT`, `LN`, `W1`–`W4`, `METAL`, `GLASS`). **Nu introduce culori noi.** Fiecare desen are cotele pe el, cu liniile de cota ale clasei `Fig`, si o `figcaption` scurta.

### E4 — peretii laterali (5 desene)

**D1. Elevatie perete lateral STANGA, la scara.**
Talpa **1580**, cununa inclinata **1596**, 4 verticale **1573 · 1645 · 1722 · 1794** dinspre fata spre spate. Golul de geam centrat: **543 / 490 / 542** pe talpa, prag la **950**. Fata peretelui e in stanga desenului, spatele in dreapta — inaltimea creste spre spate. Coteaza si inclinarea cununii.

**D2. Elevatie perete lateral DREAPTA.**
Identic, dar talpa **1570** si cununa **1586**. Verticalele raman aceleasi patru. **Desen separat, nu o nota pe D1** — omul de pe santier lucreaza cu un perete o data, si cele doua talpi difera cu 10 mm.

**D3. Detaliu gol de geam, sectiune orizontala.**
Gol **490**, acrilic **440×440** centrat → **25 mm joc pe fiecare latura**. Toc separat asezat in gol, sipci de fixare pe ambele fete. Arata ordinea de montaj cu sageti: sipca interioara → acrilic → sipca exterioara. Gaurile din acrilic se dau **+1 mm** fata de surub — coteaza-o pe desen, e cel mai usor de uitat si cel mai scump de gresit (acrilicul crapa).

**D4. Detaliu colt cu contrafisa.**
Contrafisa **212 mm** pe diagonala, brat **150 mm** pe fiecare latura, asezata intre talpa si verticala de colt. Sectiunea contrafisei iese din resturile de rigla **48×48**. Arata unghiul de taiere la ambele capete.

**D5. Perete lateral in sectiune verticala, cu lambriul.**
Rama **48×48**, lambriu **12,5×96** direct pe rama — **fara folie, fara sipci, fara OSB**. Arata cum se suprapun lamelele si unde intra surubul. Un singur detaliu, marit.

### E5 — peretele din fata (4 desene)

**D6. Elevatie perete fata, la scara.**
Rama **1970**, verticale **1552**. Layout-ul masurat de la fata interioara a stalpului stang, cotat cap la cap:

```
115 camp | jamba | fereastra 161 → 731 | jamba | usa 938 → 1488 | jamba | montant de camp 1650 → 1696 | colt 274
```

Coltul de **274** e locul propteaței de **250**. Prag + buiandrug fereastra: **570, intre jambe** — nu peste ele.

**D7. Detaliu bara de sus, 100×60 taiata la 2155.**
Sectiune care arata de ce **2155** si nu 1970: bara trebuie sa calce pe rama **SI** pe amandoi stalpii de 90×90. Coteaza cat iese peste fiecare stalp. Latura de **60 in sus**.

**D8. Detaliu prindere stalp fata.**
**4 × surub dulgherie 8×140** oblic la **15–20°** in grinda de dedesubt, doua de-o parte, doua de cealalta, plus **coltar 90×65 pe fiecare fata a stalpului**. Doua vederi: din fata si in sectiune, cu unghiul cotat. Scrie pe desen: **tot de sus, fara piulite, fara tije prin podea.**

**D9. Golul de usa — ordinea de taiere.**
Doua stari alaturate: **inainte** (talpa intreaga, peretele rigid, gata de ridicat) si **dupa** (talpa taiata, gol **550** latime, **1600** liber pe verticala). Eticheta intre ele: **taierea se face ultima, cu peretele deja ridicat, legat si verificat la echer.**

### E6 — acoperisul (6 desene: 2 existente + 4 noi)

**D10. Plan de sus — capriorii.**
**5 capriori**, pas **498**, inchideri **454** intre ei (498 − 44), streasina **100** in fata si **100** in spate. Coteaza si latimea totala.

**D11. Sectiune longitudinala prin panta.**
Reazem spate **1900**, reazem fata **1660**, span **1670**, cadere **240**, panta **8,2°**, caprior **1889**, muchia din fata **1646** peste podea. Asta e desenul-cheie al capitolului — deseneaza-l mare, pe latime.

**D12. Sectiunea capriorului — orientarea.**
**100 pe verticala, 44 pe orizontala.** Alaturi, aceeasi piesa pusa gresit, taiata cu o linie rosie si eticheta: **asa lucreaza pe axa slaba.** Un desen mic, dar e greseala care se face si nu se mai vede dupa ce s-a pus OSB-ul peste.

**D13. Plan OSB si Onduline, doua straturi peste acelasi contur.**
OSB3 12 mm: **2 placi**, taiate **2200×1250** si **2200×639**, suruburi **4×45 la ~250**. Peste el, **3 placi Onduline una langa alta, intregi** — panta masoara 1889, placa are 2000, nu se taie nimic pe lungime. Arata suprapunerea laterala dintre placi.
Nota pe desen: **nu exista sipci si nu exista sipca diagonala** — placa de OSB face bracajul singura, iar Onduline cere astereala continua sub 10°.

### E7 — geamurile (2 desene)

**D14. Montajul geamului lateral fix, pas cu pas.**
Trei stari alaturate: toc gol → acrilic asezat cu jocul de 25 → sipca exterioara pusa. Montaj **din exterior**.

**D15. Fereastra PVC 56×56 in peretele din fata.**
Pozitia in rama fata de layout-ul din D6 (161 → 731), cum se prinde in jambe si in pragul de 570. E singura care se deschide — arata sensul de deschidere spre terasa.

---

## CONSTRAINTS

- Romana, fara diacritice.
- **Nu inventa cote.** Fiecare numar e in brief-ul asta sau in constantele din `gen_ghid.py`. Daca un desen cere ceva ce nu ai — un unghi de teșire, o distanta intre suruburi — **nu il estima**: deseneaza fara cota aia si scrie un bloc `stop` in capitol care spune ce lipseste. Precedentul e in `e0`.
- Desenele trebuie sa fie **citibile la 390 px latime**. Daca un desen nu incape, sparge-l in doua, nu il micsora pana devine ilizibil.
- Fisier autonom. Fara CDN, fara fonturi externe.
- Fara deploy.
- Nu atinge `e0`, `e1`, `e2` si cele 4 desene existente din `e3`.

## DONE MEANS

- Numarul de `<svg>` pe sectiune in HTML-ul construit: **e3=4 · e4=5 · e5=4 · e6=6 · e7=2**.
- Fiecare desen nou are `figcaption`.
- `grep` pe HTML-ul final gaseste, pe desene: `1580` `1596` `1570` `1586` `1573` `1645` `1722` `1794` `543` `490` `542` `950` `440` `212` `150` `1970` `1552` `115` `161` `731` `938` `1488` `1650` `1696` `274` `570` `2155` `8×140` `550` `1600` `498` `454` `1900` `1660` `1670` `240` `1889` `1646` `2200` `1250` `639`.
- **Zero cote scrise ca sir literal in `gen_ghid.py`** acolo unde exista constanta. Verificare: schimbi `T` de la 48 la 50, rulezi generatoarele, si verticalele din desene se muta singure. Pune `T` inapoi pe 48 dupa test.
- `python3 gen_ghid.py && python3 gen_2d.py && python3 build_ghid.py` ies toate 0.
- Consola paginii: zero erori.

## VERIFY

Deschide rezultatul la desktop **si la 390 px**, consola curata, apoi confirma fiecare punct din DONE MEANS individual inainte sa raportezi gata.

In plus, obligatoriu:
- **Randeaza fiecare desen nou si uita-te la el.** Nu te baza pe faptul ca SVG-ul e valid. Cauta: text care iese din cadru, cote suprapuse, linii de cota care arata spre nimic, piese desenate la latimea gresita.
- **Testul celor 44 mm:** capriorul se deseneaza 44 lat, nu 100. Bugul asta a fost deja gasit o data in F5 din `SCHEME-CASA` si a produs „inchideri ~400" in loc de 454. Verifica-l explicit pe D10 si D12.
- Verifica ca D1 si D2 chiar difera — talpa 1580 fata de 1570, cununa 1596 fata de 1586. Daca ies identice, generatorul primeste acelasi parametru de doua ori.
- La 390 px: niciun desen nu forteaza scroll orizontal pe pagina.
- **Scrie linia in `STATUS.md` inainte de commit.** Ultimele doua rulari au facut treaba corect si au murit fara sa raporteze — ghidul a ramas 12 fisiere necomise, marcat FAILED degeaba.

## IF STUCK

- **Un desen cere o cota care nu e nicaieri** → deseneaza-l fara ea, pune blocul `stop` in capitol, si scrie in STATUS.md ce lipseste. Nu estima.
- **Nu poti desena D8 (prindere stalp) fara sa stii grosimea grinzii de dedesubt** → foloseste `SCHEME-2D-casa.html`, care are deja sectiuni prin podea. Daca nici acolo nu e, `stop`.
- **Doua fisiere se contrazic pe o cota** → castiga `MASURATORI-CONFIRMARE-2026-08-20.html`, apoi constantele din `gen_ghid.py`. Scrie contradictia in STATUS.md.
- **Un desen iese prea inghesuit ca sa fie citibil** → sparge-l in doua figuri cu `figcaption`-uri separate. Mai bine doua desene clare decat unul complet si ilizibil.
