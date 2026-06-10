# Casuta din copac — site + manual (live)

Site static (HTML + PDF) pentru proiectul casutei din copac. Live: **https://casuta-din-copac.netlify.app**

Repo: **github.com/VladHati/casuta-din-copac** → conectat la Netlify (deploy automat la fiecare push pe `main`).

PDF-urile din `PDF/` sunt **generate** din paginile HTML cu `build_pdfs.py` si commit-uite in repo (Netlify le serveste direct, fara build).

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

```
index.html              hub-ul (punct de pornire)
casuta-din-copac.html   prezentare (pentru Tudor)
catalog-piese.html      catalog piese + paritate (coduri)
ghid-montaj.html        ghid montaj 2D, pas cu pas
montaj-3d-complet.html  montaj 3D, 11 etape
imbinari-ghid.html      imbinari + audit (printabil)
imbinari-3d-ghid.html   imbinari 3D exploded
imbinare-3d.html        nod detaliu 3D
imbinari.html           produse + imbinari color
platforma-3d.html       platforma 3D
scara-3d.html           scara 3D (Faza 2)
audit.html              audit tehnic & design
CASUTA-DIN-COPAC.md     dosarul proiectului
Tracker_materiale_casuta.xlsx   buget + comanda Hornbach (cu coduri piesa)
build_pdfs.py           genereaza PDF-urile (-> PDF/)
PDF/                    PDF-urile (commit-uite, servite de Netlify)
POZE/                   fotografii de pe teren
netlify.toml            config publicare
```
