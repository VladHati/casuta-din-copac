MODEL: haiku
EFFORT: low

# BRIEF — continuare commit 17.08: intrebarea GHID e transata, executa commit-urile

## RASPUNSUL LA NEEDS-INPUT-commit-2026-08-17

Verificat din Main, direct pe obiectele git (blob `26a9372` din commit `7a09120`), fara comenzi git prin mount:

- Versiunea COMISA (11.08 10:44) = GHID **"varianta 2"**, 27 KB — draft timpuriu: fara detaliile de geam (490/570), fara tabelul de montanti, fara sectiunea Leroy Colosseum.
- Versiunea de pe DISC (mtime 12.08 10:53) = **"varianta 6 · 13 capitole"**, 107 KB — canonul real: toate deciziile din 11.08 seara, corectiile auditului 11.08 (acrilic, lambriu 13 m²), preturile Leroy live. E fisierul pe care il refera SoT, memoria de proiect si PROIECT-CASA.
- Concluzie: evolutie legitima v2→v6 (sesiunea de seara 11.08, PDF regenerat 12.08). Nu e corupere. **GHID-SIMPLU-casa.html + .pdf INTRA in COMMIT 1.**

## DE EXECUTAT

Exact COMMIT 1, COMMIT 2, COMMIT 3 din `BRIEF-commit-audit-proiect-2026-08-17.md` (arhivat sau in radacina), cu GHID inclus in COMMIT 1. In mesajul lui COMMIT 1 adauga la final: `+ GHID v6 (verificat vs blob comis, evolutie legitima)`.

Apoi:
- muta `NEEDS-INPUT-commit-2026-08-17.md` in `_archive/briefs/` (rezolvat, commit separat sau in COMMIT 3),
- linie noua in STATUS cu hash-urile,
- push NU (ramane la Vlad).

## DONE MEANS

`git status --short` curat (minus briefurile RUNNING/DONE de arhivat la final) · 3 commituri noi peste `e58ae92` · STATUS actualizat.
