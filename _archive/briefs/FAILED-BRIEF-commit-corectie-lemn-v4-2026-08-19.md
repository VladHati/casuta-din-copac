MODEL: haiku
EFFORT: low

# BRIEF — commit 19.08 v4: STATUS + arhivare briefuri esuate (creat direct in terminal, bypass bridge)

## GOAL

Adauga o intrare noua in STATUS.md (continut exact mai jos) si arhiveaza cele 6 fisiere ramase de la incercarile v1+v2+v3 esuate. NU comite niciun fisier de continut (.html/.pdf/gen_scheme.py) — acelea sunt DEJA commise si pushuite manual de Vlad azi (commit-uri 2eede7f si 5764470), inainte ca acest brief sa fie scris. Singurul lucru care mai lipseste e intrarea din STATUS.md.

## CONTEXT

Acest brief inlocuieste v1, v2 SI v3 — toate trei au picat cu mesajul identic "Brief has no valid MODEL: line", desi linia 1 era `MODEL: haiku` de fiecare data. v1/v2 au picat inainte de restart-ul watcher-ului (proces impotmolit 4 saptamani, PID 86029, omorat de Vlad). v3 a picat LA FEL, cu procesul nou (PID 14741, repornit 19.08 11:50) — deci teoria "proces impotmolit" nu explica totul. v1/v2/v3 au fost toate create de Main (Cowork) si transferate pe Mac prin puntea de fisiere (SendUserFile + device_commit_files). Acest brief (v4) e creat DIRECT in terminalul lui Vlad, printr-un heredoc (`cat > fisier << 'EOF'`), ca sa elimine puntea de fisiere ca variabila — daca puntea introducea ceva invizibil (BOM, CRLF) intr-un check strict pe primul rand, un fisier scris direct in terminal nu ar avea acea problema.

Intre timp (cat watcher-ul era picat/testat), Vlad a facut manual din terminalul lui, direct:
- Commit `2eede7f`: cele 7 fisiere de continut (PROIECT-CASA, LISTA-LEROY, SCHEME-CASA html+pdf, gen_scheme.py) — corectia de geometrie + alocarea barnelor. Pushuit.
- Commit `5764470`: arhivarea briefurilor procesate din 18.08. Pushuit.

Deci istoricul git are deja aceste 2 commituri. Ramane doar STATUS.md (niciodata atins — toate cele 3 incercari au picat inainte sa apuce sa scrie ceva) si igiena celor 6 fisiere ramase pe disc de la v1/v2/v3.

## CONTENT — intrarea de adaugat in STATUS.md

Adauga urmatorul paragraf ca intrare noua, in acelasi format cu restul fisierului (o intrare = un paragraf dens, data la inceput, `| URMEAZA:` la final). Fisierul e in ordine cronologica inversa (cele mai noi intrari sus) — pune-o imediat DEASUPRA celei mai recente intrari cu data 2026-08-18. Copiaza textul de mai jos EXACT, fara sa il rescrii sau parafrazezi:

```
2026-08-19 (Main, Cowork) | CORECTIE GEOMETRIE: dulapii cumparati sunt REAL 200×50×4000 (nu 46×250×3000 cum scria planul — Vlad confirmat "acelasi lemn, cote corectate"). Plus 2 barne noi, decizie Vlad: 1× 3000×100×60 → lemnul de sus al peretelui din FATA (inlocuieste cununa laminata 44×100, latura 60 in sus) si 1× 4000×90×90 → rezerva stalp. Geometrie recalculata si verificata fata de spec-ul real Onduline (min 5°, verificat web): reazem spate 1900 (1700+200), reazem fata 1660 (1600+60), cadere 240, panta 12,3° (era 15,6°) — de 2,5x peste minimul Onduline, sigur, sipcile la ≤45cm deja specificate acopera cerinta. STOP vechi din S0 ("dulap sub 250mm") SCOS — era prag intern, nu spec producator. Caprior 1342→1331, muchia 1614→1638 (mai bine pt clearance cap copii). Verticalele peretelui fata raman 1556 (neschimbate — post-referentiate, cancel out cu grosimea barei de sus). CORECTIE IN ACEEASI ZI: propunerea initiala pt cele 2 bare 200×50×4000 ramase (coardele scarii F3) a fost RESPINSA de Vlad — scara va fi o varianta mai usoara, discutie separata, mai incolo; lemnul NU e pentru ea. Raman rezerva flexibila (taiate in lung sau in alte forme, dupa nevoia reala, ca sa economiseasca de la cumparaturi). BUG GASIT+REPARAT in LISTA-LEROY: randul de scandura 22×100×4000 avea "14 (+1 rezerva)"/278 lei scris, dar planul de taiere (§10) cerea intotdeauna 28 buc (14 bare laminate ×2) — corectat la 28/~557 lei; bug vechi, independent de corectia de azi, doar descoperit acum. Buget total ~3.000-3.150 → ~3.280-3.430 lei (diferenta = aproape toata bugul de scandura, nu cumparaturi noi — barele 100×60/90×90/200×50 sunt deja ale lui Vlad). Actualizate + regenerate + verificate (pypdf text-check + pdftoppm vizual pe f1/f3/f4/f5), de doua ori in aceeasi zi (a doua oara ca sa scoata earmark-ul de scara): PROIECT-CASA (§1, S0 STOP+nota corectie, §7 tabel+nota, §8 scandura+caprior+muchia, §10 plan taiere, §11, footer), LISTA-LEROY (nota corectie, rand scandura, total, NU cumperi), SCHEME-CASA (f1/f3/f4/f5 regenerate din gen_scheme.py + 2 captions text), gen_scheme.py (F1/F3/F4/F5). Memoria de proiect (casuta-casa-de-sus) rescrisa cu GEOMETRIE FINALA re-blocata 19.08. Commis manual de Vlad din terminal (2eede7f continut + 5764470 arhivare), pushuit — watcher-ul Builder a picat de 3 ori cu fals-negativ "no valid MODEL: line" (v1/v2 inainte de restart, v3 dupa restart — cauza exacta inca neclara, brief v4 creat direct in terminal ca sa testeze puntea de fisiere ca sursa). | URMEAZA: alocarea finala a celor 2 bare 200×50×4000 (+ posibil 90×90×4000) ramane deschisa — rezerva flexibila, de discutat cand apare nevoia reala.
```

## CONSTRAINTS

- NU edita, NU regenera, NU comite niciun fisier de continut (.html/.pdf/gen_scheme.py) — sunt deja commise si pushuite de Vlad manual (2eede7f, 5764470). Daca `git status --short` arata vreunul din ele ca modificat sau netracked, STOP imediat (vezi PAS 0, pasul 3) — nu presupune, nu commite, scrie NEEDS-INPUT.
- Nu parafraza intrarea STATUS de mai sus — copiaz-o exact.
- Daca STATUS.md are deja o intrare cu data 2026-08-19 (posibil ramasa dintr-o rulare partiala anterioara) — NU duplica; inlocuieste-o cu textul de mai sus sau adauga-l langa ea, dupa cum pare mai curat citind contextul.
- Muta (nu sterge) toate cele 6 fisiere ramase de la incercarile picate v1+v2+v3 in `_archive/briefs/` (acelasi loc ca arhivarile anterioare — vezi commit 5764470): `FAILED-BRIEF-commit-corectie-lemn-2026-08-19.md`, `NEEDS-INPUT-BRIEF-commit-corectie-lemn-2026-08-19.md`, `FAILED-BRIEF-commit-corectie-lemn-v2-2026-08-19.md`, `NEEDS-INPUT-BRIEF-commit-corectie-lemn-v2-2026-08-19.md`, `FAILED-BRIEF-commit-corectie-lemn-v3-2026-08-19.md`, `NEEDS-INPUT-BRIEF-commit-corectie-lemn-v3-2026-08-19.md`.
- Acest brief insusi (`BRIEF-commit-corectie-lemn-v4-2026-08-19.md`) ramane la radacina cat ruleaza (RUNNING) — nu-l muta pe tine insuti in timp ce esti activ.

## PAS 0 — verificari inainte de orice commit

1. Daca exista `.git/index.lock` (0 bytes, vechi): sterge-l O data si continua. Daca reapare: STOP, scrie NEEDS-INPUT cu eroarea exacta.
2. Ruleaza `git log --oneline -5`. Confirma ca hash-urile `2eede7f` si `5764470` apar in istoric. Daca NU apar (niciunul sau vreunul lipseste): STOP, scrie NEEDS-INPUT — repo-ul nu e in starea asteptata, explica exact ce arata `git log`, nu continua.
3. Ruleaza `git status --short`. Confirma ca NICIUNUL din aceste 7 fisiere nu apare (nici M, nici ??): `PROIECT-CASA-2026-08-17.html`, `PROIECT-CASA-2026-08-17.pdf`, `LISTA-LEROY-2026-08-17.html`, `LISTA-LEROY-2026-08-17.pdf`, `SCHEME-CASA-2026-08-17.html`, `SCHEME-CASA-2026-08-17.pdf`, `gen_scheme.py`. Daca vreunul apare: STOP, scrie NEEDS-INPUT cu output-ul exact de la `git status --short` — nu le commite fara instructiuni noi.

## COMMIT 1 — STATUS

```
git add STATUS.md
git commit -m "STATUS: corectie geometrie lemn real + alocare barne + bug scandura (19.08)"
```

## COMMIT 2 — arhivare briefuri esuate v1+v2+v3

```
mkdir -p _archive/briefs
mv FAILED-BRIEF-commit-corectie-lemn-2026-08-19.md NEEDS-INPUT-BRIEF-commit-corectie-lemn-2026-08-19.md FAILED-BRIEF-commit-corectie-lemn-v2-2026-08-19.md NEEDS-INPUT-BRIEF-commit-corectie-lemn-v2-2026-08-19.md FAILED-BRIEF-commit-corectie-lemn-v3-2026-08-19.md NEEDS-INPUT-BRIEF-commit-corectie-lemn-v3-2026-08-19.md _archive/briefs/
git add _archive/briefs
git commit -m "Archive briefuri esuate corectie-lemn v1+v2+v3 (fals-negativ MODEL-line, cauza in investigare)"
```

## DONE MEANS

- STATUS.md contine noua intrare 2026-08-19, textul de mai sus, nealterat, in pozitia corecta (imediat deasupra intrarii 2026-08-18).
- Cele 6 fisiere FAILED/NEEDS-INPUT v1+v2+v3 mutate in `_archive/briefs/`, nu la radacina.
- 2 commituri noi peste HEAD-ul actual (STATUS + arhivare), NIMIC din cele 7 fisiere de continut in ele.
- `git status --short` curat, minus brieful asta (RUNNING) si eventuale `.DS_Store`.
- Push NU se face de aici — ramane la Vlad.

## VERIFY

Inainte sa scrii DONE in STATUS.md: deschide STATUS.md si confirma ca intrarea noua e acolo, completa, in locul corect, fara duplicate. `git log --oneline -4` arata cele 2 commituri noi DEASUPRA lui `5764470`. `git status --short` curat (minus brieful si .DS_Store). Confirma ca niciunul din cele 7 fisiere de continut nu a fost adaugat/commis de tine (verifica `git show --stat HEAD` si `git show --stat HEAD~1` — trebuie sa contina DOAR STATUS.md, respectiv fisierele din _archive/briefs/). Daca oricare pica, repara si reverifica — nu raportezi done pe un check picat.

## IF STUCK

Daca orice pas de mai sus cere o decizie care nu e acoperita explicit aici, sau un check de la PAS 0 pica: STOP, nu improviza, nu comite fisiere de continut "ca sa fie sigur", scrie NEEDS-INPUT cu situatia exacta (output de comanda, nu parafraza) si opreste-te acolo.
