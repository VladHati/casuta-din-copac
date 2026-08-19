MODEL: haiku
EFFORT: low

# BRIEF — commit 19.08: corectie geometrie (lemn real) + alocare 5 barne noi + bug scandura reparat

## GOAL

Adauga o intrare noua in STATUS.md (continut exact mai jos) si comite fisierele deja rescrise pe disc de Main. Niciun fisier de continut nu se editeaza sau regenereaza — toate exista deja corecte pe disc, cu o singura exceptie: STATUS.md, unde TU adaugi intrarea (Main n-a putut re-sincroniza STATUS.md prin bridge azi — a picat cu eroare "untrusted_device" la staging).

## CONTEXT

Vlad a confirmat ca dulapii cumparati sunt REAL 200×50×4000 (nu 46×250×3000 cum scria planul vechi) si a decis alocarea a inca 2 barne noi (100×60×3000 → lemnul de sus din fata, 90×90×4000 → rezerva). Main a recalculat geometria acoperisului, verificat spec-ul real Onduline pe web, gasit si reparat un bug vechi in cantitatea de scandura din LISTA-LEROY, si a rescris/regenerat/verificat (pypdf + pdftoppm) toate documentele + memoria de proiect.

## CONTENT — intrarea de adaugat in STATUS.md

Adauga urmatorul paragraf ca intrare noua, in acelasi format cu restul fisierului (o intrare = un paragraf dens, data la inceput, `| URMEAZA:` la final). Fisierul e in ordine cronologica inversa (cele mai noi intrari sus) — pune-o imediat DEASUPRA celei mai recente intrari cu data 2026-08-18. Copiaza textul de mai jos EXACT, fara sa il rescrii sau parafrazezi:

```
2026-08-19 (Main, Cowork) | CORECTIE GEOMETRIE: dulapii cumparati sunt REAL 200×50×4000 (nu 46×250×3000 cum scria planul — Vlad confirmat "acelasi lemn, cote corectate"). Plus 2 barne noi, decizie Vlad: 1× 3000×100×60 → lemnul de sus al peretelui din FATA (inlocuieste cununa laminata 44×100, latura 60 in sus) si 1× 4000×90×90 → rezerva stalp. Geometrie recalculata si verificata fata de spec-ul real Onduline (min 5°, verificat web): reazem spate 1900 (1700+200), reazem fata 1660 (1600+60), cadere 240, panta 12,3° (era 15,6°) — de 2,5x peste minimul Onduline, sigur, sipcile la ≤45cm deja specificate acopera cerinta. STOP vechi din S0 ("dulap sub 250mm") SCOS — era prag intern, nu spec producator. Caprior 1342→1331, muchia 1614→1638 (mai bine pt clearance cap copii). Verticalele peretelui fata raman 1556 (neschimbate — post-referentiate, cancel out cu grosimea barei de sus). Cele 2 bare 200×50×4000 ramase (nefolosite la reazem) → rezervate pt coardele scarii F3 (amanata, de confirmat atunci). BUG GASIT+REPARAT in LISTA-LEROY: randul de scandura 22×100×4000 avea "14 (+1 rezerva)"/278 lei scris, dar planul de taiere (§10) cerea intotdeauna 28 buc (14 bare laminate ×2) — corectat la 28/~557 lei; bug vechi, independent de corectia de azi, doar descoperit acum. Buget total ~3.000-3.150 → ~3.280-3.430 lei (diferenta = aproape toata bugul de scandura, nu cumparaturi noi — barele 100×60/90×90/200×50 sunt deja ale lui Vlad). Actualizate + regenerate + verificate (pypdf text-check + pdftoppm vizual pe f1/f3/f4/f5): PROIECT-CASA (§1, S0 STOP+nota corectie, §7 tabel+nota, §8 scandura+caprior+muchia, §10 plan taiere, footer), LISTA-LEROY (nota corectie, rand scandura, total, NU cumperi), SCHEME-CASA (f1/f3/f4/f5 regenerate din gen_scheme.py + 2 captions text), gen_scheme.py (F1/F3/F4/F5). Memoria de proiect (casuta-casa-de-sus) rescrisa cu GEOMETRIE FINALA re-blocata 19.08. | URMEAZA: Vlad `git push origin main` dupa commit; confirmare alocare 200×50×4000 ramase la inceputul F3 (scara); STATUS.md n-a putut fi re-sincronizat de Main prin bridge azi (eroare untrusted_device la staging) — intrarea asta a fost adaugata de Builder direct pe disc.
```

## CONSTRAINTS

- Nu edita, nu regenera niciun alt fisier de continut (.html/.pdf/gen_scheme.py) — sunt deja corecte pe disc, scrise de Main azi.
- Nu parafraza intrarea STATUS de mai sus — copiaz-o exact.
- Daca STATUS.md are deja o intrare cu data 2026-08-19 (posibil scrisa separat) — NU duplica; adauga continutul de mai sus ca paragraf separat langa ea, sau semnaleaza in STATUS ca exista un conflict de editare, dupa cum pare mai potrivit citind contextul.

## PAS 0

Daca exista `.git/index.lock` (0 bytes, vechi): sterge-l O data si continua. Daca reapare: STOP, scrie NEEDS-INPUT cu eroarea exacta.

## COMMIT 1 — geometrie corectata + lemn alocat + bug scandura reparat

```
git add AUDIT-2026-08-17.md PROIECT-CASA-2026-08-17.html PROIECT-CASA-2026-08-17.pdf LISTA-LEROY-2026-08-17.html LISTA-LEROY-2026-08-17.pdf SCHEME-CASA-2026-08-17.html SCHEME-CASA-2026-08-17.pdf gen_scheme.py
git commit -m "Corectie geometrie acoperis cu lemnul real (200x50, nu 46x250) + alocare 2 barne noi (100x60 fata, 90x90 rezerva) + bug reparat in cantitatea de scandura 22x100 din LISTA-LEROY (14->28 buc). Panta 15.6->12.3 grade, verificata peste minimul real Onduline (5 grade). Vezi STATUS 19.08 pt detalii complete."
```

(Daca `git status` arata ca AUDIT-2026-08-17.md nu are modificari fata de HEAD, scoate-l din `git add` si `git commit` — adauga doar fisierele chiar modificate.)

## COMMIT 2 — STATUS

```
git add STATUS.md
git commit -m "STATUS: corectie geometrie lemn real + alocare barne + bug scandura (19.08)"
```

## DONE MEANS

- STATUS.md contine noua intrare 2026-08-19, textul de mai sus, nealterat, in pozitia corecta (imediat deasupra intrarii 2026-08-18).
- 2 commituri noi peste HEAD-ul actual.
- `git status --short` curat, minus brieful asta (RUNNING) si eventuale `.DS_Store`.
- Push NU se face de aici — ramane la Vlad.

## VERIFY

Inainte sa scrii DONE in STATUS.md: deschide STATUS.md si confirma ca intrarea noua e acolo, completa, in locul corect, fara duplicate. `git log --oneline -3` arata cele 2 commituri noi. `git status --short` curat (minus brieful si .DS_Store). Daca oricare pica, repara si reverifica — nu raportezi done pe un check picat.
