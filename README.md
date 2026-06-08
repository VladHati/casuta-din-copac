# Casuta din copac — site + manual (live)

Site static (HTML + PDF) pentru proiectul casutei din copac. Live: **https://casuta-din-copac.netlify.app**

PDF-urile (`PDF/`) sunt **generate** din paginile HTML cu `build_pdfs.py` — nu se editeaza de mana.

---

## Cum lucrezi „live" (CI/CD)

Odata legat (vezi setup-ul de mai jos), fluxul e:

1. Modifici o pagina HTML sau dosarul `.md`.
2. `git commit` + `git push`.
3. GitHub Actions regenereaza automat PDF-urile si publica pe Netlify.
4. In ~1-2 min, **casuta-din-copac.netlify.app** e la zi.

Fara push manual, fara regenerat PDF de mana.

---

## Setup o singura data (≈5 min)

Pasii astia ii faci tu — cer autentificare GitHub/Netlify pe care un asistent nu o poate face.

### 1. Creezi repo-ul si dai push
Din folderul proiectului (repo-ul local e deja initializat cu un commit):

```bash
# varianta cu GitHub CLI (cea mai rapida)
gh repo create casuta-din-copac --private --source=. --push

# SAU manual: creezi repo gol pe github.com, apoi:
git remote add origin https://github.com/<user>/casuta-din-copac.git
git push -u origin main
```

### 2. Iei un token Netlify
Netlify → **User settings → Applications → Personal access tokens → New access token**. Copiaza-l.

### 3. Adaugi 2 secrete in GitHub
Repo → **Settings → Secrets and variables → Actions → New repository secret**:

| Nume | Valoare |
|---|---|
| `NETLIFY_AUTH_TOKEN` | token-ul de la pasul 2 |
| `NETLIFY_SITE_ID` | `a0af6853-169f-449b-8577-13e4aeea0253` |

### 4. Gata
Urmatorul `git push` pe `main` declanseaza workflow-ul (`.github/workflows/deploy.yml`):
build PDF → deploy pe Netlify. Vezi progresul in tab-ul **Actions** din repo.

---

## Build local (optional)

Daca vrei sa vezi PDF-urile fara CI:

```bash
pip install -r requirements.txt           # weasyprint, markdown, pypdf
# pe Ubuntu/Debian, pentru weasyprint:
# sudo apt-get install libpango-1.0-0 libpangocairo-1.0-0 libcairo2 libgdk-pixbuf-2.0-0
python3 build_pdfs.py                      # scrie in ./PDF/
```

---

## Structura

```
index.html              hub-ul (punct de pornire)
casuta-din-copac.html   prezentare (pentru Tudor)
catalog-piese.html      catalog piese + paritate (coduri)
ghid-montaj.html        ghid montaj 2D, pas cu pas
montaj-3d-complet.html  montaj 3D, 9 etape
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
PDF/                    artefacte generate (ignorate de Git)
POZE/                   fotografii de pe teren
```
