MODEL: opus
EFFORT: xhigh

# BRIEF — Casa de sus: geometrie as-built (grinda 140 pe stalpii spate)

## GOAL

Propaga in toate fisierele canonice noua geometrie a casei de sus, masurata pe teren 10.08.2026. Cotele nominale vechi (M1 ~1772, perete fata = M1−300, panta 300/1100 = 15,3°) sunt caduce. Cand termini, cut list-ul din MANUAL-FAZA-2 se poate debita direct, fara recalcul.

## CONTENT — geometria noua (cifre finale, nu estimari)

Masurat de Vlad pe santier, 10.08.2026:

- Stalpii de 4 m din spate ies **1700 mm** peste dusumea. Deci **M1 = 1700** (masurat, nu nominal).
- Cei 2 stalpi 70×70 ai casei **sunt deja montati** pe tijele M12 si ies **1600 mm** peste dusumea. Nu se mai cumpara.

Element NOU, care nu exista in documentatia actuala:

- **Grinda spate 45×140, lungime 2200 mm, 1 bucata.** Se aseaza ORIZONTAL, culcata PE capetele celor doi stalpi de 4 m. Ridica reazemul acoperisului din spate de la 1700 la **1840**.

Geometria rezultata:

| Marime | Valoare |
|---|---|
| Reazem spate (top grinda 140) | 1840 |
| Reazem fata (top cununa peretelui din fata) | 1600 |
| Cadere pe adancimea A = 1100 | 240 |
| **Panta acoperis** | **240 / 1100 = 12,3°** |
| Perete spate (panou, fara grinda) | 1700 |
| Perete fata (panou, cu cununa) | 1600 |

**Stalpii 70×70 din fata se reteaza 42 mm la varf, de la 1600 la 1558.** Motiv: cununa de 42 sta PE capul stalpului; ca reazemul din fata sa cada exact la 1600, capul stalpului trebuie sa fie la 1558. Fara retezare, reazemul iese la 1642, caderea scade la 198 si panta la 10,2° — exact pe pragul minim Onduline pe sipci, fara marja.

### Cut list nou (inlocuieste integral tabelul din §8)

| Piesa | Sectiune | Lungime | Buc |
|---|---|---|---|
| Talpa + cununa spate / fata | 42×90 | L (2000) | 2 + 2 |
| Talpa + cununa laterale | 42×90 | A − 90 (1010) | 4 |
| **Grinda spate (pe capul stalpilor de 4 m)** | **45×140** | **2200** | **1** |
| Montanti spate | 45×45 | 1616 | 5 |
| Montanti fata (cu dublurile de la goluri) | 45×45 | 1516 | 7 |
| Montanti laterali (in trepte pe panta) | 45×45 | 1516 / 1636 / 1756 | 6 |
| Buiandrug usa · prag + buiandrug fereastra | 42×90 | 590 · 660 · 660 | 3 |
| Capriori (streasina 200 fata + 100 spate) | 42×90 | √(A²+240²) + 300 (**1426**) | 5 |
| Sipci acoperis | 45×45 | L + 200 (2200) | 4 |
| Stalpi fata 70×70 | — | **deja montati la 1600; se reteaza 42 → 1558** | 2 |
| OSB spate / fata / laterale | 12 mm | L×1840 · L×1600 · trapez A×(1600→1840) | 1 · 1 · 2 |

Formule pentru cine reface calculul: montanti spate = M1 − 84; montanti fata = 1600 − 84; caprior = √(A² + 240²) + 300.

### Prinderea grinzii de 140 — nod nou, critic

Grinda sta pe capatul de fibra al stalpului. Suruburile in capat de fibra tin aproximativ jumatate din valoarea normala, deci nodul NU se face cu suruburi verticale prin grinda in stalp.

- **Eclise laterale: 45×90 × 400 mm, cate una pe FIECARE fata a fiecarui nod = 4 bucati.** Suprapun stalpul si grinda, 2× surub 6×120 in stalp + 2× in grinda pentru fiecare eclisa. Total 16× 6×120 in plus.
- Alternativ acceptat: placa metalica perforata echivalenta pe ambele fete.
- Lantul anti-smulgere devine: caprior → ancora anti-vant → grinda 140 → eclise → stalp de 4 m. Scrie-l explicit in Pasul 4; fara el, grinda si acoperisul sunt o singura piesa care pleaca la vant.

### Cumparaturi — modificari

- **SCOATE** din Drum 2 randul `Stalp 70×70×3000, taiat 2× · 1 buc · ~90 lei` — stalpii sunt deja montati.
- **ADAUGA** in Drum 2: `Grinda 45×140 × 2200 (grinda spate) · 1 buc · ~60 lei`.
- **ADAUGA** in feronerie casa: `Surub 6×120 (T30)` creste de la ~22 la **~38** (16 in plus pentru eclise); `Eclise 45×90 × 400` — 4 buc, se taie din offcut de rigla, nu se cumpara separat daca exista rest.
- Totalul fazei ramane ~3.000 lei.

## CONSTRAINTS

- Romana fara diacritice, ca in tot dosarul.
- `MANUAL-FAZA-2.html` este SURSA UNICA pentru Faza 2 (vezi SOURCE-OF-TRUTH.md). Editezi acolo, apoi regenerezi PDF-ul.
- NU atinge sectiunile balustrada (§F2) si scara (§F3). Nimic din ele nu se schimba.
- NU atinge documentele din `_archive/` — sunt arhivate intentionat.
- Nu inventa sectiuni de lemn care nu sunt in acest brief.

## FISIERE DE MODIFICAT (denumite explicit)

1. **`MANUAL-FAZA-2.html`** — principalul. Puncte concrete:
   - Linia ~109, tabelul de decizii: `Perete casa spate / fata | M1 / M1 − 300 | M1 = cat ies stalpii de 4 m peste dusumea (~1772)` → devine `Perete casa spate / fata | 1700 + grinda 140 / 1600 | masurat 10.08: M1 = 1700; stalpii fata sunt deja montati la 1600`.
   - Linia ~110: `Panta acoperis | 300 / 1100 = 15,3°` → `Panta acoperis | 240 / 1100 = 12,3°`.
   - §8 tabelul M1–M5, randul M1: nominal `~1772` → `1700 (masurat 10.08)`, coloana Real completata cu `1700`.
   - §8 blocul STOP: scoate conditia `M1 e sub 1700` (e masurat, e fix 1700) si pune in loc: `grinda de spate are sectiunea sub 140 mm inaltime (panta scade sub 12° si Onduline pe sipci cere minim 10°)`. Pastreaza celelalte 3 conditii de STOP neatinse.
   - §8 cut list: inlocuit integral cu tabelul de mai sus.
   - §8 nota `Simplificare optionala: ... cadru separat de 300 mm`: rescrie — grinda de 140 pe stalpi joaca acum acest rol partial; peretii laterali raman trapezoidali de la 1600 la 1840, iar OSB-ul lor se decupeaza pe rama.
   - Pasul 2 (Pregateste podeaua), punctul cu `Stalpii 70×70`: rescrie — stalpii sunt DEJA montati pe tije; pasul devine verificare (vertical pe doua fete, piulita ingropata, fara joc) + **retezarea a 42 mm din varf, de la 1600 la 1558**, trasat pe 4 fete si taiat cu HS7611K.
   - Pasul 3: adauga montarea grinzii de 140 pe capul stalpilor de 4 m, cu ecliseIe, INAINTE de capriori. Adauga in `GATA CAND`: `☐ grinda 140 pe stalpi, 4 eclise × 4× 6×120 · ☐ grinda la nivel pe ambele capete`.
   - Pasul 4: `taiati oblic la 15,3°` → `taiati oblic la 12,3°`. Adauga lantul anti-smulgere caprior → grinda → eclise → stalp. Adauga avertismentul de panta mica: la 12,3° pe sipci, suprapunerea laterala e obligatoriu de o onda intreaga si cuiele merg NUMAI in creasta, indesite pe randul de jos si pe ambele margini laterale — la panta mica apa urca in suprapunere. Sipcile raman la ≤450.
   - §Feronerie casa: `Surub 6×120 (T30) | ~22` → `~38`; rand nou `Eclise 45×90 × 400 | 4 | grinda spate → stalpii de 4 m`.
   - §9 Cumparaturi: modificarile de la sectiunea Cumparaturi de mai sus.
   - §11 Deschise: randul `Cele 5 masuratori M1–M5` → marcheaza M1 ca FACUT (1700, 10.08), restul raman deschise.
   - §12 Istoricul corectiilor: 3 randuri noi —
     - `Casa: M1 = 1700 masurat, nu ~1772 estimat` / `masuratoare pe teren 10.08`.
     - `Casa: grinda 45×140 pe capul stalpilor de 4 m` / `stalpii fata sunt deja montati la 1600 si nu se coboara; grinda ridica spatele la 1840 si recupereaza panta.`
     - `Casa: panta 12,3°, nu 15,3° · stalpii fata retezati 42 mm` / `cununa de 42 sta pe capul stalpului: fara retezare reazemul din fata iese la 1642, caderea la 198 si panta la 10,2° — exact pe pragul minim Onduline pe sipci.`

2. **`tools-fise/gen_casa.py`** — liniile 11–13: `A = 1100` ramane; `H = 1772` → `H = 1840` (reazem spate, nu perete); `HF = H - 300` → `HF = 1600`. Linia ~99, eticheta de cota `"300 = panta pe 1100 → 15,3°"` → `"240 = panta pe 1100 → 12,3°"`. Regenereaza SVG-urile casei in `assets/iso/`.

3. **`SOURCE-OF-TRUTH.md`** — linia `- Perete casa de sus: 1800 spate / 1500 fata (inlocuieste vechiul 1300).` → `- Casa de sus (as-built 10.08): perete spate 1700 + grinda 140 pe stalpi = reazem 1840; perete fata 1600 (stalpi 70×70 deja montati, retezati la 1558). Panta 240/1100 = 12,3°.`

4. **`CASUTA-DIN-COPAC.md`** — randul de tabel `| Perete casa de sus | 1800 mm spate / 1500 mm fata |` si paragraful de la §"Casa de sus" (`pereti 1800 (spate) -> 1500 (fata)`) → aliniaza la cifrele noi. Sterge din acel paragraf `Ramase de ales: invelitoarea (Onduline vs policarbonat) si usa vs gol` — ambele sunt decise (Onduline; usa = gol deschis). Trimiterea catre `CASA-plan-constructie.html` se inlocuieste cu `MANUAL-FAZA-2.html`.

5. **`MANUAL-FAZA-2.pdf`** — regenerat din HTML cu pipeline-ul existent.

6. **`STATUS.md`** — o linie noua in capul fisierului, formatul obisnuit: data, ce s-a schimbat, ce urmeaza.

## DONE MEANS

- `grep -n "1772\|15,3°\|15.3\|M1 − 300\|M1 - 300\|1800 spate\|1500 fata"` in radacina proiectului (excluzand `_archive/`) intoarce **zero** rezultate in fisierele canonice de mai sus. Aparitiile din §12 Istoricul corectiilor sunt permise si asteptate — acolo cifrele vechi se citeaza ca istoric.
- `MANUAL-FAZA-2.html` contine `12,3°`, `1840`, `1616`, `1516`, `1426`, `1558` si randul de cut list pentru grinda `45×140`.
- `MANUAL-FAZA-2.pdf` regenerat, se deschide, are cel putin 21 pagini, si tabelul de cut list din §8 nu e taiat intre pagini.
- SVG-urile casei din `assets/iso/` sunt regenerate si arata panta mai mica; niciun text suprapus in ele.
- Randul `Stalp 70×70×3000` nu mai apare in lista de cumparaturi; randul `Grinda 45×140` apare.
- `STATUS.md` are linia noua.
- Totul comis pe `main`, un commit sau doua, mesaj descriptiv. Push-ul NU se face de aici — ramane la Vlad.

## VERIFY

Deschide rezultatul la latime desktop si la 390px, consola curata, apoi confirma fiecare punct din DONE MEANS individual inainte de a raporta done. In plus, specific pentru build-ul asta:

1. Ruleaza tu insuti aritmetica: 1840 − 1600 = 240; atan(240/1100) = 12,31°; √(1100² + 240²) = 1126; 1126 + 200 + 100 = 1426. Daca vreo cifra din manual nu se potriveste, cifra din manual e gresita — repara-o.
2. Randeaza PDF-ul si UITA-TE la paginile casei: cut list intreg pe o pagina, desenele fara text suprapus, `GATA CAND`-urile fara orfani de pagina.
3. `grep -c "15,3"` pe HTML — rezultatul asteptat este exact numarul de aparitii din §12 (istoric). Orice aparitie in afara §12 e un bug.

## IF STUCK

- **Daca 45×140 nu exista la raft** (Builder nu poate sti, dar scrie regula in manual): sectiunile 145 sau 150 sunt acceptabile si mai bune — reazemul urca la 1845/1850, panta la 12,4°/12,5°. Sectiuni sub 140 NU sunt acceptabile. Scrie asta ca nota in manual langa randul de cut list.
- **Daca `gen_casa.py` nu ruleaza** (dependinte lipsa): recreeaza env-ul asa cum e documentat in README/STATUS (micromamba, weasyprint + pypdf + numpy + pillow). Daca tot pica, comite modificarile de text si de cod, marcheaza SVG-urile ca neregenerate in STATUS, si NU raporta done pe punctul de SVG.
- **Daca gasesti alte fisiere din radacina care mai contin 1772 / 15,3° / 1800-1500** in afara celor 4 numite: aliniaza-le si listeaza-le in STATUS. Fisierele din `_archive/` nu se ating.
- **Daca ceva din brief contrazice ce gasesti in fisier:** brieful castiga la cifre, fisierul castiga la structura. Nu rescrie sectiuni intregi ca sa incapa cifrele — fa editari punctuale.
