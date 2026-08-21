MODEL: opus
EFFORT: xhigh

# BRIEF — ghid interactiv complet pentru casa

## GOAL

`GHID-CONSTRUCTIE-casa.html` devine **singurul document de executie al casei**: acopera tot drumul de la golul din colt pana la geamuri, si tine minte bifele intre sesiuni. Azi se opreste la peretele din spate (E0–E4) si pierde progresul la fiecare refresh.

Se lucreaza prin generatoare, ca acum: `gen_ghid.py` (desene → `figs_ghid.json`), `gen_2d.py` (desene 2D → `figs_2d.json`), `build_ghid.py` (asamblare HTML). **Nu se editeaza HTML-ul direct.**

---

## PARTEA 1 — schimbarea de material (se face prima, restul depinde de ea)

### Rama peretilor trece pe rigla 48×48×4000

Decizie Vlad, 20.08.2026. Inlocuieste atat bara laminata 44×100, cat si capitolul „Fasiile".

**Produs:** rigla nerindeluita, lemn rasinoase, FSC, **48 × 48 × 4000 mm — 29,90 lei/bucata**, 4,1 kg. `https://www.leroymerlin.ro/produse/grinzi-lemn/1631/rigla-nerindeluita-lemn-rasinoase-48-x-48-x-4000-mm/122728`

**Cantitate: 13 bucati.** Plan de taiere (bin-packing pe bare de 4000):

| bara | ce iese | total |
|---|---|---|
| 1–2 | 1604 + 1604 | verticale spate |
| 3 | 1604 + 1552 | ultima spate + prima fata |
| 4–5 | 1552 + 1552 | verticale fata |
| 6–7 | 1573 + 1794 | verticale laterale |
| 8–9 | 1645 + 1722 | verticale laterale |
| 10 | 1990 + 1990 | talpa + cununa spate |
| 11 | 1970 + 1596 | talpa fata + cununa laterala stanga |
| 12 | 1580 + 1570 | talpi laterale |
| 13 | 1586 + contrafise | cununa laterala dreapta |

Contrafisele ies din resturi. Cost total **~389 lei**.

**De ce nu laminat:** 20 de scanduri 22×100×4000 (~398 lei) cereau ~240 de suruburi de laminare inainte sa se construiasca ceva, si dadeau un panou de spate de 43–52 kg. Cu rigle: zero laminare, panou ~32–41 kg. Panoul ala se ridica in doi, la 2,2 m, pe o punte fara balustrada — greutatea conteaza mai mult decat cei 9 lei diferenta.

**De ce nu profil solid 45×100:** nu exista la 4000 pe leroymerlin.ro (verificat 20.08). Cele apropiate — 42×70×3000 (39,50 lei) si 60×100×3000 (97 lei) — sunt la 3000, deci o verticala de 1604 iese una singura pe bara, cu 1396 mm resturi.

### Ce se schimba in cote

Talpa si cununa cresc de la 44 la 48. **Verticalele scad cu 8 mm** (4 jos + 4 sus) fata de valorile blocate pe 20.08. Exceptie peretele din fata: sus nu are cununa, are bara solida 100×60 asezata pe capetele stalpilor — acolo scade doar cu 4.

| | 20.08 (laminat 44) | nou (rigla 48) |
|---|---|---|
| verticale spate ×5 | 1612 | **1604** |
| verticale fata ×5 | 1556 | **1552** |
| verticale laterale ×4/perete | 1581 · 1653 · 1730 · 1802 | **1573 · 1645 · 1722 · 1794** |

**Nu se schimba nimic altceva.** Reazemele (1900 / 1660), spanul (1670), panta (8,2°), capriorul (1889), latimile de taiere (1990 / 1970), adancimile (1580 / 1570), golurile de geam si de usa raman exact cum sunt. Cadere si panta se masoara intre reazeme, iar reazemele nu depind de grosimea ramei.

In `gen_ghid.py`: `T = 48`. Verifica prin cod ca `VB = 1700 - 2*T = 1604`. Daca gasesti `T=44` sau `T=46` undeva, e relicva.

### Fasiile ies din plan

Capitolul `e3` „Fasiile" descrie taierea unui dulap in lung, in fasii de 100. **Se sterge complet** — blocul `CH.append(dict(id='e3', ...))` din `build_ghid.py` si desenele lui din `gen_ghid.py`. Docstring-ul din `gen_ghid.py` se rescrie: rama e din rigla 48×48 cumparata gata, nu dulap taiat in lung.

### Sirul „46×250" e geometrie moarta

Apare in `gen_2d.py`, `gen_ghid.py`, `build_ghid.py`, `SCHEME-2D-casa.html`. Lemnul real, confirmat de Vlad pe 19.08 si reconfirmat pe 20.08, e **200×50×4000**. Inlocuieste peste tot. Titlul figurii „cum se taie dulapul de 46×250" devine **„cum se taie dulapul de 200×50"**.

Bara aia are o singura treaba: **reazemul din spate** — taiata la 2200, asezata pe muchie cu 200 in sus, peste capetele stalpilor si peste cununa peretelui din spate (ambele la 1700) → reazem continuu la **1900**. Nimic altceva nu se face din ea.

### Lista de cumparaturi

`LISTA-LEROY-2026-08-17.html` si capitolul `e2` din ghid:
- **adauga** rigla 48×48×4000, **13 buc, 29,90 lei/buc = 388,70 lei** — rama tuturor peretilor
- **reduce** randul de scandura 22×100×4000 de la 20 la **6 buc**. Nu dispare: capriorii raman 44×100 laminat. 5 capriori × 1889 = 9445 mm, doi pe bara laminata de 4000 → **3 bare = 6 scanduri** (~120 lei). Inchiderile de 454 dintre capriori ies din resturi.
- nota pentru cine verifica: vechea cantitate de 20 de scanduri dadea 9 bare laminate = 36 m de 44×100, dar rama cerea ~41,5 m plus capriorii inca 9,4 m. **Cifra veche era deja scurta** — nu incerca sa o reconciliezi, e inlocuita.
- **verifica** randul de rigla 46×46×3000 (20 buc in lista veche): daca era pentru contrafise, cantitatea scade — contrafisele ies acum din resturile de 48×48. Daca era pentru tocurile de geam, ramane. **Nu sterge randul fara sa gasesti in documente pentru ce era.** Daca nu poti stabili, lasa-l si scrie intrebarea in STATUS.md.
- recalculeaza totalul si scrie-l in ambele locuri, sa nu divergheze

---

## PARTEA 2 — capitolele noi

Structura finala, in ordine (numerotarea se reasaza dupa stergerea fasiilor):

| id | nume | titlu |
|---|---|---|
| e0 | E0 | Scandura care lipseste *(exista, nu se atinge)* |
| e1 | E1 | Restantele podelei si cioata *(exista, nu se atinge)* |
| e2 | E2 | Drumul la Leroy *(exista — se corecteaza lista)* |
| e3 | **E3** | Peretele din spate *(actualul `e4`, redenumit + cote noi)* |
| e4 | **E4** | Peretii laterali *(nou)* |
| e5 | **E5** | Peretele din fata *(nou)* |
| e6 | **E6** | Acoperisul *(nou)* |
| e7 | **E7** | Geamurile si verificarea finala *(nou)* |

Fiecare capitol nou tine acelasi tipar ca `e0`–`e4`: `sub`, `zi` (timp estimat), `lead`, blocuri `gate` / `stop` / `warn` / `need` unde e cazul, si o lista `steps([...])` cu pasi bifabili.

### Geometria — cote verbatim, nu se recalculeaza nimic

Sursa: masuratorile de santier confirmate 20.08 (`MASURATORI-CONFIRMARE-2026-08-20.html`), plus corectia de grosime din Partea 1. Toate in mm.

**Cadrul general**
- latime de taiere: spate **1990**, fata **1970**
- adancime: stanga (S1–S3) **1580**, dreapta (S2–S4) **1570**
- stalpi: spate **100×100**, fata **90×90**; stalpii din fata ies **1600** peste podea
- dreptunghiul e in afara echerului cu ~20 mm → **peretii sunt trapeze usoare, fiecare talpa se taie la fata locului**
- reazem spate **1900**, reazem fata **1660**, span **1670**, cadere **240**, panta **8,2°**
- caprior **1889**, streasina **100** fata si **100** spate, muchia din fata **1646** peste podea
- rama: **rigla 48×48**; lambriu **12,5×96** direct pe rama, fara folie, fara sipci, fara OSB

**E3 — peretele din spate**
- talpa **1990**, cununa **1990**, verticale **1604** ×5
- talpa se prinde prin podea, in grinzile de dedesubt, cu **6×140 la fiecare 400 mm**
- reazemul (dulapul 200×50 taiat la 2200) se aseaza peste cununa SI peste capetele stalpilor, fixat cu **vinclu 90×65 pe ambele fete la ~500** + placa metalica pe fiecare stalp

**E4 — peretii laterali** (doi pereti, fiecare pe cota lui)
- talpa: stanga **1580**, dreapta **1570**
- cununa inclinata: stanga **1596**, dreapta **1586**
- verticale, 4 pe perete, dinspre fata spre spate: **1573 · 1645 · 1722 · 1794**
- gol geam centrat: **543 / 490 / 542** (camp / gol / camp), prag la **950**
- geam fix **440×440** in gol de **490**, toc separat, sipci pe ambele fete, gauri +1 mm
- contrafise: toate 4 colturile, **212 mm** pe diagonala, brat **150 mm**

**E5 — peretele din fata**
- rama **1970**; layout masurat de la fata interioara a stalpului stang:
  - **115** camp
  - jamba
  - fereastra **161 → 731**
  - jamba
  - usa **938 → 1488**
  - jamba
  - montant de camp **1650 → 1696**
  - colt **274** pentru propteaua de 250
- verticale **1552** ×5
- prag + buiandrug fereastra: **570, intre jambe** (aceeasi metoda ca la geamurile laterale)
- fereastra PVC **56×56**, singura care se deschide, spre terasa
- lemnul de sus = bara solida **100×60**, latura de 60 in sus, **taiata la 2155** — trebuie sa calce pe rama SI pe amandoi stalpii. Nu se lamineaza, nu se inlocuieste cu rigla.
- contrafise: sus **2× 212 / brat 150**; jos-dreapta **~350 / brat 250**; jos-stanga **se sare** (coltul e chiar stalpul de 90×90)
- **usa: golul de 1600 liber se face prin taierea talpii LA FINAL**, dupa ce peretele e ridicat, legat si verificat la echer. Gol **550** latime. Daca talpa se taie inainte, peretele isi pierde rigiditatea la transport si ridicare.
- prindere finala stalpi fata: **4× surub dulgherie 8×140** infiletat oblic la ~15–20° in grinda de dedesubt (2 de-o parte, 2 de cealalta) + **coltar 90×65 pe fiecare fata a stalpului**. Tot de sus, fara piulite. Nu exista tije M12 in podea — nu au existat niciodata.

**E6 — acoperisul**
- capriori **44×100 laminat** (2× scandura 22×100, suruburi 4×40 in zigzag la 300), **5 bucati**, pas **498**, lungime **1889**. **Capriorii NU trec pe rigla 48×48** — sectiunea patrata nu are rigiditatea ceruta la span 1670. Aici se lamineaza, si numai aici: 3 bare, din cele 6 scanduri din lista.
- **orientarea capriorului: 100 pe verticala, 44 pe orizontala.** Pus invers, lucreaza pe axa slaba.
- inchideri intre capriori: **454** (498 − 44)
- prindere capriori: **2× vinclu 90×65 pe fiecare capat**
- astereala: **2 placi OSB3 12 mm** (2500×1250), taiate la **2200×1250** si **2200×639**, insurubate cu **4×45 la ~250 mm**
- **NU exista sipci si nu exista sipca diagonala.** Placa de OSB face bracajul singura.
- Onduline: **3 placi, una langa alta, intregi.** Panta masoara 1889, placa are 2000 — nu se taie nimic pe lungime.
- de ce OSB si nu sipci: verificat pe uk.onduline.com — intre 5° si 10° producatorul cere astereala continua (*„must be installed on full deck"*). Sipcile sunt permise abia peste 10°. Suntem la 8,2°.

**E7 — geamurile si verificarea finala**
- 2 geamuri laterale fixe **440×440**, toc separat, montate din exterior
- fereastra PVC **56×56** in peretele din fata
- checklist final

### Ordinea de ridicare — pasul care lipseste azi

Peretele din spate se imbraca complet **jos pe iarba** (rama + lambriu + contrafise), apoi se urca pe punte. Panoul cantareste **~32–41 kg** cu lambriu si vopsea.

Scrie metoda explicit in `e3`, ca pasi bifabili:
- doi oameni, nu unul
- panoul urca **culcat**, pe muchia lunga, sprijinit pe marginea puntii, apoi se roteste in picioare pe punte
- **puntea nu are balustrada** — margine libera la 2,2 m pe toate laturile pe toata durata capitolului
- se leaga provizoriu de stalpi inainte sa se dea drumul din maini

Peretii laterali (`e4`) se asambleaza **pe punte**, nu jos — nu incap sa fie urcati gata facuti.

---

## PARTEA 3 — stratul interactiv

Tot in `build_ghid.py`, in blocul de `<script>` de la final. Fara librarii externe, fisier autonom.

1. **Bifele se tin minte.** `localStorage`, o cheie pe bifa, formata din id-ul capitolului + indexul pasului (ex. `ghid.e4.03`). Se citesc la incarcare si se aplica inainte de primul `upd()`. Ambalat in `try/catch` — daca storage-ul e blocat, pagina merge mai departe fara sa crape.

2. **Progres pe capitol, nu doar global.** Langa fiecare intrare din `nav`, un contor mic `3/7`. Cand capitolul e complet, intrarea primeste un semn de terminat. Bara globala din nav ramane.

3. **Gate-uri care blocheaza.** Un capitol poate declara `blocat_de='e0'`. Cat timp capitolul-parinte nu e bifat complet, capitolul blocat apare estompat, cu bifele dezactivate si o bara rosie deasupra care spune de ce. Un buton **„sar peste"** il deblocheaza, dar lasa o eticheta permanenta de avertisment in capul capitolului, care nu dispare.

   Un singur gate real: **`e3` (peretele din spate) e blocat de `e0` (golul din colt).** Motivul, scris in bara: talpa peretelui din spate se prinde prin podea, in grinzile de dedesubt, la fiecare 40 cm. Exact la colturi nu are in ce sa intre. Dupa ce peretele e ridicat, la coltul ala nu se mai ajunge niciodata.

4. **Bon de taiere per capitol.** La inceputul fiecarui capitol, un tabel pliabil: piesa · cota (mm) · bucati · din ce lemn. Se completeaza din cotele de mai sus. Bifabil si el, separat de pasi — se taie tot inainte de asamblat.

5. **Scule per capitol.** Rand scurt sub titlu, cu ce scule cere capitolul. Sursa: `SCULE-DISPONIBILE.md`. Nu inventa scule pe care Vlad nu le are — daca un pas cere ceva ce nu e in fisierul ala, scrie-o ca `stop`, nu ca pas.

6. **Mod telefon.** Sub 720 px: o singura coloana, `nav` devine bara lipita sus cu capitolul curent si un `select` pentru sarit intre capitole. Suprafata minima de atins pentru bife: **44×44 px** — se apasa cu degetul manusat.

7. **Reset.** Buton per capitol („sterge bifele din capitolul asta") si unul global in `nav`, cu confirmare inline (nu `confirm()` — dialogurile de browser blocheaza).

8. **Nota din footer** — „Bifele se pierd la reincarcarea paginii" — se sterge. Nu mai e adevarata.

Tema, tipografie si paleta raman exact cum sunt. Nu redesena nimic.

---

## PARTEA 4 — siguranta

Adauga in `e7`, **primul rand din checklistul final**, inaintea oricarei alte bife:

> **Balustrada nu exista.** Terasa are margine libera la 2,2 m. Casa poate fi terminata integral, cu toate bifele verzi, si copiii tot nu au voie sus. Balustrada e faza urmatoare (F2). Pana atunci, scara se ia de langa punte intre sesiunile de lucru.

Randul asta nu poate fi bifat ca „rezolvat" — e o eticheta, nu un pas.

---

## PARTEA 5 — canonul

Dupa ce ghidul e complet si verificat, si **numai dupa**:

- adauga in capul acestor fisiere o bara vizibila: **„DEPASIT. Documentul de executie al casei e `GHID-CONSTRUCTIE-casa.html`."** — `GHID-SIMPLU-casa.html`, `MANUAL-FAZA-2.html`, `PLAN-pereti-lambriu.html`, `PROIECT-CASA-2026-08-17.html`
- `SCHEME-2D-casa.html` **nu** primeste bara — ramane anexa de desene a ghidului. Leaga-le intre ele.
- `SOURCE-OF-TRUTH.md`: rescrie sectiunea casei. `GHID-CONSTRUCTIE-casa.html` = executie. `SCHEME-2D-casa.html` = desene. `LISTA-LEROY-2026-08-17` = cumparaturi. Sterge geometria moarta din el (1950, 46×250, 15,6°, caprior 1342).
- `NEEDS-INPUT-commit-2026-08-17.md` → `_archive/`

---

## CONSTRAINTS

- Romana, fara diacritice.
- Limbaj de santier. Zero jargon de inginerie: nu „element vertical de rigidizare", ci „scandura pusa pieziș in colt". Un om care n-a mai construit nimic trebuie sa poata executa capitolul.
- **Nu inventa cote.** Fiecare numar din ghid vine din lista de mai sus sau din `MASURATORI-CONFIRMARE-2026-08-20.html`. Daca un pas cere o cota care nu e nicaieri, scrie un bloc `stop` care cere masuratoarea. Nu estima.
- **Nu inventa desene.** Un desen se face doar daca geometria lui e complet definita de cotele de mai sus. Altfel, capitolul merge fara desen. `e0` are deja precedentul: acolo scrie explicit ca desenele lipsesc pentru ca nu exista pozele.
- Fisier autonom. Fara CDN, fara fonturi externe, fara framework.
- Fara deploy. Fisierul sta in folder.
- Nu atinge `e0` si `e1` — sunt verificate.

## DONE MEANS

- `GHID-CONSTRUCTIE-casa.html` are 8 capitole: E0, E1, E2, E3 spate, E4 laterale, E5 fata, E6 acoperis, E7 geamuri. Capitolul „Fasiile" nu mai exista nicaieri in fisier.
- Bifezi cateva casute, dai refresh — raman bifate. Butonul de reset le sterge.
- `e3` apare blocat cat timp `e0` nu e complet; „sar peste" il deblocheaza si lasa avertismentul pe ecran.
- `grep -c "46×250\|46x250" gen_2d.py gen_ghid.py build_ghid.py SCHEME-2D-casa.html GHID-CONSTRUCTIE-casa.html` → **0** peste tot.
- `grep -n "T=46\|T = 46\|T=44\|T = 44" gen_ghid.py` → gol. `T = 48` si `1604` apar in cod.
- Verticalele din HTML sunt **1604** (spate), **1552** (fata), **1573 / 1645 / 1722 / 1794** (laterale). Vechile **1612 / 1556 / 1581 / 1653 / 1730 / 1802** nu mai apar nicaieri in ghid.
- `LISTA-LEROY-2026-08-17.html` are randul de rigla 48×48×4000 (13 buc, 388,70 lei) si randul de scandura 22×100×4000 redus la 6 buc, etichetat explicit „doar pentru capriori".
- Cele 4 documente vechi poarta bara „DEPASIT". `SCHEME-2D-casa.html` nu o poarta.
- Randul despre balustrada e primul in checklistul final din `e7` si nu e bifabil.
- `python3 gen_ghid.py && python3 gen_2d.py && python3 build_ghid.py` ies toate 0.

## VERIFY

Deschide rezultatul la latime de desktop **si la 390 px**, consola curata, apoi confirma fiecare punct din DONE MEANS individual inainte sa raportezi gata.

In plus, obligatoriu:
- Bifeaza tot capitolul `e0`, verifica ca `e3` se deblocheaza singur.
- Refresh dupa bifare — starea supravietuieste. Reset — starea dispare.
- La 390 px: nav-ul nu acopera continutul, bifele se apasa fara zoom, niciun tabel nu iese din ecran.
- **Verificare aritmetica independenta:** recalculeaza din cod ca `1700 − 2×48 = 1604` si ca fiecare verticala laterala noua e exact vechea minus 8. Daca nu se potriveste, opreste-te si scrie in STATUS.md.
- Citeste capitolele E3–E7 cu ochiul unui om care n-a mai construit nimic. Orice propozitie care presupune ceva nespus se rescrie.
- Verifica prin `grep` ca fiecare cota din PARTEA 2 apare in HTML-ul final. Daca una lipseste, capitolul e incomplet.

## IF STUCK

- **Un capitol are nevoie de un desen pe care nu-l poti construi corect din cotele date** → scrie capitolul fara desen si pune un bloc `stop` care spune exact ce masuratoare sau poza lipseste. Modelul e in `e0`. Nu reconstitui din descriere.
- **`gen_ghid.py` si `gen_2d.py` se contrazic pe o cota** → castiga `MASURATORI-CONFIRMARE-2026-08-20.html` plus corectia de grosime din Partea 1. Scrie contradictia in STATUS.md.
- **Nu stii pentru ce era rigla 46×46×3000 din lista** → las-o in lista, neschimbata, si scrie intrebarea in STATUS.md. Nu sterge randuri de cumparaturi pe ghicite.
- **Nu gasesti in `SCULE-DISPONIBILE.md` o scula ceruta de un pas** → nu presupune ca o are. Bloc `stop` cu scula lipsa.
- **Renumerotarea capitolelor sparge ancorele** → id-urile din HTML pot ramane `e0..e7` fara sa corespunda etichetei afisate. Prioritatea e ca `nav` si `href`-urile sa fie coerente, nu ca id-ul sa fie egal cu numarul de pe eticheta.
- **Bara „DEPASIT" ar strica randarea PDF-ului unui document vechi** → pune-o oricum. PDF-urile vechi sunt oricum depasite.
