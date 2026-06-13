# Casuta din copac — site + manual (live)

Site static (HTML + PDF) pentru proiectul casutei din copac. Live: **https://casuta-din-copac.netlify.app**

Repo: **github.com/VladHati/casuta-din-copac** → conectat la Netlify (deploy automat la fiecare push pe `main`).

PDF-urile din `PDF/` sunt **generate** din doua surse, ambele commit-uite in repo (Netlify le serveste direct, fara build):
- **Sectiunile** (00, 02, 03, 04, 05, 06) — din `build_pdfs.py` (paginile HTML de sectiune).
- **Fisele de montaj + manualul combinat** (Fisa-01..11, Manual-Faza-1-complet, Fise-montaj-Faza-1) — din `tools-fise/book.py`.

---

## Cum lucrezi „live"

1. Modifici o pagina HTML sau dosarul `.md`.
2. Daca s-a schimbat continut care apare in PDF: `python3 build_pdfs.py` (regenereaza `PDF/`).
3. `git add -A && git commit -m "..." && git push`.
4. Netlify publica automat in ~1 min pe **casuta-din-copac.netlify.app**.

---

## Setup (deja facut)

- Repo creat si push-uit pe GitHub.
- Netlify (site `casuta-din-copac`) legat de repo, cu: build command = gol, publish directory = `.`.

Nu sunt necesare token-uri sau secrete — Netlify publica fisierele statice direct din repo.

---

## Build local PDF (cand schimbi continut)

```bash
pip install weasyprint markdown pypdf
# pe macOS, pentru weasyprint: brew install pango
python3 build_pdfs.py        # scrie in ./PDF/
```

---

## Structura

Pagini principale:
```
index.html              hub-ul (punct de pornire)
casuta-din-copac.html   prezentare (pentru Tudor)
materiale.html          materiale + buget + coduri Hornbach (pagina reala)
ghid-montaj.html        ghid montaj 2D, pas cu pas
montaj-3d-complet.html  montaj 3D, 11 etape
platforma-3d.html       platforma 3D
scara-3d.html           scara 3D (Faza 2)
imbinari.html           produse + imbinari color
imbinare-3d.html        nod detaliu 3D
modele-3d.html          index modele 3D
fise.html               toate fisele de montaj intr-o pagina
fisa-01.html ... fisa-11.html   fisele de montaj individuale (generate)
scule.html              lista scule
timeline.html           planul pe etape
audit.html              audit tehnic & design
CASUTA-DIN-COPAC.md     dosarul proiectului
Tracker_materiale_casuta.xlsx   buget + comanda Hornbach (cu coduri piesa)
```

Redirect-uri (pagini vechi care trimit catre cele noi):
```
catalog-piese.html       -> materiale.html
comanda-corespondent.html-> materiale.html
imbinari-ghid.html       -> imbinari.html
imbinari-3d-ghid.html    -> imbinari.html
```

Generatoare si resurse:
```
build_pdfs.py           genereaza PDF-urile de sectiune (00,02,03,04,05,06) -> PDF/
tools-fise/             generatorul de fise: fb.py + book.py -> fisa-*.html + Fisa-*.pdf + manual
PDF/                    PDF-urile (commit-uite, servite de Netlify)
POZE/                   fotografii de pe teren
netlify.toml            config publicare
```
