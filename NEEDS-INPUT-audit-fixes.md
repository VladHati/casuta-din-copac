# NEEDS-INPUT — audit-fixes (13.06.2026)

Reparatiile autonome sunt FACUTE si verificate (F2, F4, F6, F7, F8, F10 + materiale.html).
Doua decizii raman pe tine (asa cere brief-ul) plus un pas de livrare. Raspunde printr-un brief nou.

---

## 1. F1 — granita de faza (DECIZIE)

Unde sta balustrada + masa-copac: Faza 1 sau Faza 2?

- [ ] **A. Balustrada + masa = FAZA 1** (recomandat). Faza 2 ramane doar pereti, acoperis, scara.
      Daca alegi asta, aplic: `ghid-montaj.html` footer (scot balustrada/masa din lista Faza 2),
      `tools-fise/book.py` L30 (mut SB/SP/MC/BM in grupul Faza 1), `tools-fise/fb.py` (scot orice „(Faza 2)" de pe piesele de balustrada).
- [ ] **B. Ramane Faza 2** — nu schimb nimic la granita. (status quo)

Nota: defectul de dimensiune (F2, stalpisor 7x7 → 58×58) e DEJA reparat, indiferent de raspuns.

---

## 2. F3 — surubul din coltarul C1 (DECIZIE de siguranta)

Coltarul C1 (grinda fata pe varful stalpilor, Fisa 5) — ce surub intra in el?

- [ ] **A. Heco 6×100** — confirmi ca asta merge in C1.
      Aplic: `tools-fise/fb.py` fisa-05 chip `('H1','~12','in coltare')` → `('H2','~12','in coltare')`;
      `imbinari.html` nodul A „Heco 8×200" → „Heco 6×100" (text + chip). NU ating nodul D (contrafise) — acolo 8×200 ramane corect.
- [ ] **B. Alt surub** — daca producatorul coltarului Alberts recomanda alt conector, scrie-mi codul exact.
- [ ] **C. Lasa 8×200** — daca de fapt 8×200 e bun si in C1.

Pana raspunzi, C1 e neatins (inca foloseste H1 = Heco 8×200).

---

## 3. Livrare (push + deploy) — nevoie de tine

Reparatiile sunt COMMIT-uite local pe `main`, dar NU sunt push-uite / deployate. Doua motive:
1. Contul Builder e fara credentiale (nu poate face push pe GitHub VladHati/casuta-din-copac).
2. Regula din CLAUDE.md root: „Never push — local history only."

**Ca sa intre live** (Netlify deploy automat la push pe `main`), din contul tau principal:
```
cd "/Users/Shared/Builds/CASUTA DIN COPAC"
git push origin main
```
Recomand sa rezolvi intai F1 + F3 (sa intre tot odata), altfel push-uiesc acum doar reparatiile autonome.

---

## Nota tehnica — regenerarea PDF-urilor

PDF-urile au fost regenerate (manual + sectiuni + Fisa-01..11 + Fise-montaj). Pe contul Builder,
`weasyprint` nu mergea (lipsea `pango`, iar `brew install pango` cere admin/sudo pe care contul nu-l are).
Am rezolvat printr-un mediu izolat (micromamba/conda-forge in `/tmp`, fara sudo) — toate PDF-urile sunt la zi.
Daca vrei sa regenerezi tu local pe viitor: `brew install pango` (din contul tau cu admin), apoi
`python3 tools-fise/fb.py && python3 tools-fise/emit2.py && python3 tools-fise/idx2.py && python3 tools-fise/book.py && python3 build_pdfs.py`.
