MODEL: opus
EFFORT: xhigh

# BRIEF — Continut v3: deciziile din 11.08 seara, propagate peste tot

## GOAL

Aliniaza documentele canonice la ultimele decizii Vlad (11.08 seara) si la constatarile din `AUDIT-2026-08-11.md`. Dupa brieful asta, lantul de precedenta e intreg: cine urmeaza SoT → MANUAL → GHID construieste varianta corecta.

## REGULA DE AUR A RULARII

**Commitul de continut se face INAINTE de regenerarea PDF/SVG.** Ordinea: editari text/cod → COMMIT 1 → regenerari → COMMIT 2. Daca regenerarea pica, munca de continut e deja salvata — raportezi partial, nu FAILED mut. (Lectia audit: 8/8 esecuri istorice = briefuri care tineau totul intr-o singura coada.)

## CONTENT — cifrele si deciziile (adevarul, verbatim)

- **Streasina fata 100, spate 100** (nu 200/100). **Caprior = √(1100² + 308²) + 200 = 1342** (nu 1442). Motiv: cu streasina 200, muchia acoperisului coboara la ~1586, sub inaltimea de intrare 1600 — copiii se lovesc cu capul.
- **FARA jgheab si burlan.** Ar atarna sub muchie, fix la nivelul capului. Apa pica pe terasa si se scurge printre scandurile de larice.
- **Pereti (varianta finala, canonic = `GHID-SIMPLU-casa.html`):** lambriu 12,5×96 orizontal suprapus 2 cm, batut DIRECT pe rama; FARA folie, FARA sipci de aerisire, FARA OSB. Rigidizare: **contrafise 45×45, brate 300/300 (taiate 424, capete 45°), 4 per perete = 16 total**; la peretele din fata, cele de sus se prind SI in stalpii 90×90. Interior liber. Diagonala 45×45×2400 in planul acoperisului RAMANE.
- **Geamuri laterale:** FIXE, acrilic 4 mm, 440×440, gol CENTRAT 305→705 de la coltul din spate, prag 950. Taiate din **2× placa acrilica 500×500** (500×250 NU poate da 440 — eroare veche, corectata). Sipca de retinere pe ambele fete, gauri +1 mm.
- **Lambriu: ~13 m²** (9,69 net × factor suprapunere 96/76 + pierderi), ~850 lei. **Delta pereti vs OSB = +680 lei** (nu +510, nu +883).
- **Scara: AMANATA** (decizie 11.08: "varianta simpla si usoara, later"). Materialele ei NU se mai cumpara. Din cei 3 dulapi 46×250×3000 deja cumparati, 1 = reazemul din spate al casei.
- **Balustrada: 8 stalpisori, 16 M10** (nu 7/14/12 — cifre vechi ramase pe alocuri).
- **Joiste-sora: SKIP DEFINITIV** (06.08) — nimic de cumparat pentru ele.

## FISIERE — editari punctuale

1. **`MANUAL-FAZA-2.html`**
   - Header: `Versiunea 1.0 · 6 august 2026` → `Versiunea 1.2 · 11 august 2026`.
   - §8 cut list, randul capriorilor: lungime `1442` → `1342`, formula → `√(A²+308²) + 200 (1342)`, nota streasina `200 fata + 100 spate` → `100 fata + 100 spate`.
   - §F4 Pasul 4: sterge randul cu `Jgheab pe marginea de jos + burlan...` si bifa `☐ jgheab + burlan` din GATA CAND; pune in loc nota: `FARA jgheab — apa pica pe terasa si se scurge printre scanduri. Un jgheab ar atarna fix la nivelul capului (muchia e la ~1,61 m).` Randul cu `Streasina din fata ajunge la ~3,70 de la sol` → recalculeaza: muchia la 1614 peste podea, podeaua la 2228 → `~3,84 de la sol; peste podea muchia e la ~1,61 — teseste muchia`. Taietura oblica a capriorilor ramane 15,6°.
   - §F4, oriunde descrie sistemul de perete (`sipci de ventilare`, `diagonale de lemn`, `folie`): inlocuieste cu trimitere scurta la GHID: `Sistemul de perete (lambriu direct pe rama, contrafise in colturi, fara folie) = GHID-SIMPLU-casa.html — el bate orice alta descriere a peretilor.` NU rescrie pasii peretilor in manual.
   - §9 Cumparaturi, Drum 1 — sterge randurile de scara: grinda 100×100 ×2, dulap 46×250 ×2, rigla 46×46 ×3, banda Tesa ×2, pavaj ×2, dibluri 6×60 (raman lazura+grund si acrilicul NUMAI daca nu dublezi randul de acrilic de mai jos). Randul `Bulon M10 +8 (4 balustrada + 4 scara)` → `+4 (balustrada; ai 12)`.
   - §9 Drum 2 — randul de pereti (`+883` sau `PLAN-pereti-lambriu`): → `Pereti: lambriu ~13 m² + inox 3,5×40 + 2× acrilic 500×500 + 5× rigla 45×45 — lista in GHID-SIMPLU-casa §7, delta +680 vs OSB`. Verifica ca OSB si stalpul 70×70 NU mai apar.
   - §9: recalculeaza `TOTAL FAZA 2` din randurile ramase (asteptat ~2.800-3.100; scrie cifra reala rezultata).
   - §2 si §4: scara marcata `AMANATA (11.08)` — poarta F3 ramane in ordine dar cu nota; NU sterge sectiunea F3 (geometria decisa ramane ca referinta pentru varianta viitoare).
   - §11 Deschise: randul scarii sa reflecte `varianta simpla, de decis`; adauga `poze noi santier (ultimele: 03.08)` si `M2-M4 de masurat` daca lipsesc.
   - §12 Istoricul corectiilor, randuri noi: streasina 100 + caprior 1342 (motivul de mai sus) · fara jgheab · pereti v2 = contrafise fara folie, GHID canonic · acrilic 500×500 · scara amanata · delta +680.
   - Oriunde in manual mai apar `7 stalpisori` / `14 M10` / `12 M10`: → 8 / 16.

2. **`SOURCE-OF-TRUTH.md`**
   - Tabelul "Cine guverneaza ce", rand NOU: `| Pereti casa de sus (lambriu, contrafise, geamuri laterale) | GHID-SIMPLU-casa.html | actual — bate PLAN-pereti-lambriu.html (v1, istoric) |`.
   - `M10 total 14 (7 stalpisori × 2)` → `M10 total 16 (8 stalpisori × 2)`.
   - Randul de buget: adauga `+ delta pereti lambriu ~680` la total (noul all-in ~11,1-11,3k).

3. **`PLAN-pereti-lambriu.html`** — banner DEPASIT sus, stil identic cu cel de pe CASA-plan-constructie.html: `DEPASIT 11.08 — varianta finala a peretilor (contrafise, fara folie, lambriu direct pe rama) e in GHID-SIMPLU-casa.html. Pastrat ca istoric.` NIMIC altceva editat in el.

4. **`Tracker_materiale_casuta.xlsx`** (openpyxl; pastreaza formatarea existenta, editezi doar celule):
   - `Stalpisori` 7 → 8; `M10` 12 → 16.
   - Randul/randurile joiste-sora (Debitare P4d si orice echivalent): marcheaza in celula de status/nota `SKIP DEFINITIV 06.08 — NU se cumpara`.
   - Randurile de scara (60×140, 45×190 etc.): nota `AMANAT 11.08`.
   - NU adauga randuri noi de lambriu (lista de pereti traieste in GHID §7 — pune o nota `Pereti Faza 2: vezi GHID-SIMPLU-casa §7` pe foaia principala daca exista loc natural).

5. **`project-instructions.md`** — actualizeaza cotele peretilor (1800/1500 → 1700+dulap 250 = 1950 / 1642) si orice alta cifra de casa evident veche.

6. **`tools-fise/gen_casa.py`** — streasina fata din 200 → 100 in geometrie si etichete (cauta `-200`/`200` in contextul streasinii si eticheta aferenta); verifica ca lungimea capriorului afisata devine 1342.

→ **COMMIT 1** (toate cele de mai sus): mesaj `continut v3: streasina 100/caprior 1342/fara jgheab, pereti canonic=GHID, scara amanata, tracker 8/16+skip sisters, SoT lant intreg`.

7. **Regenerari** (dupa COMMIT 1): SVG-urile casei din `gen_casa.py` → `assets/iso/` · `MANUAL-FAZA-2.pdf` din HTML (env: /tmp/pdfenv sau recreeaza micromamba weasyprint+pypdf+numpy+pillow). GHID-SIMPLU-casa.pdf NU se regenereaza (e curent).

→ **COMMIT 2**: `regen: SVG casa + MANUAL-FAZA-2.pdf pe geometria 11.08`.

8. **`STATUS.md`** — linie noua in capul listei: data, ce s-a facut, hash-urile ambelor commituri, `URMEAZA: Vlad push (24+ commituri!) + poze + M2-M4`. Intra in COMMIT 2 (sau commit 3 separat, indiferent).

## DONE MEANS

- `grep -rn "1442\|jgheab\|Jgheab" MANUAL-FAZA-2.html` → 1442 zero; jgheab DOAR in §12 istoric si in nota "FARA jgheab".
- `grep -n "7 stalpisori\|total 14\|M10.*12 buc" SOURCE-OF-TRUTH.md MANUAL-FAZA-2.html` → zero.
- `MANUAL-FAZA-2.html` contine `1342`, `Versiunea 1.2`, trimiterea la GHID pentru pereti; §9 fara randuri de scara si fara OSB.
- PLAN-pereti-lambriu.html are bannerul DEPASIT; GHID-SIMPLU-casa.html NEatins.
- Tracker: 8 / 16 / SKIP vizibile; fisierul se deschide fara eroare in openpyxl dupa salvare.
- MANUAL-FAZA-2.pdf regenerat are data/versiunea noua si cut list-ul cu 1342, netaiat intre pagini.
- 2-3 commituri noi; `git status --short` curat (minus brieful asta cu prefix).
- Push NU se face de aici.

## VERIFY

Ruleaza aritmetica: √(1100²+308²)=1142,3 → +200 = 1342; 1642−28 (panta pe 100) = 1614 muchia; 1614+2228 = 3842. Randeaza PDF-ul si UITA-TE la paginile modificate (cut list, Pasul 4, §9): fara suprapuneri, fara orfani. Confirma fiecare DONE MEANS individual. Daca regenerarea PDF pica de 2 ori: lasi COMMIT 1 cum e, scrii in STATUS `PDF neregenerat — de reluat`, si te opresti curat (nu FAILED mut).

## IF STUCK

- Tracker-ul nu se poate edita fara sa strice formule → editeaza DOAR celulele numerice/notele; daca si asta pica, sari peste pasul 4, noteaza in STATUS, continua restul.
- Nu gasesti un rand mentionat exact cum e descris → cauta dupa cifra (1442, 200, 7 stalpisori); daca tot nu exista, noteaza in STATUS si mergi mai departe — NU inventa continut nou.
- index.lock reapare → sterge-l o data; a doua oara STOP → NEEDS-INPUT cu eroarea exacta.
