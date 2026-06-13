# STATUS — Casuta din copac

Firul comun Main <-> Builder. O linie pe reper: data, ce s-a schimbat, ce urmeaza.

- 2026-06-13 — Audit complet al proiectului (Main). 11 defecte gasite (1 critic, 3 ridicate, 3 medii, 4 joase); structura verificata corecta. Raport: `PDF/Audit-complet-2026-06-13.pdf`. Scris `BRIEF-audit-fixes.md`. URMEAZA: Vlad decide F1 (granita de faza) + F3 (surub C1), apoi Builder executa brief-ul.
- 2026-06-13 14:05 | Reparat F2 (stalpisor 58×58, in fb.py + materiale.html), F4 (corcodus „+2780 de la sol", fb.py), F6 (README structura+PDF), F7 (tracker „10 trepte (11 niveluri)"), F8 (cod mort -> tools-fise/_arhiva/), F10 (lock gitignored OK). Regenerat fise HTML + TOATE PDF-urile (manual, sectiuni, Fisa-01..11, Fise-montaj); verificat 0× „7x7"/„deasupra podelei". Fix bonus: PROJ in fb.py acum derivat din __file__ (nu mai e cale de sesiune hardcodata). Commit local pe main. | URMEAZA: Vlad decide F1+F3 (vezi NEEDS-INPUT-audit-fixes.md) si face `git push` (contul Builder nu poate push).
