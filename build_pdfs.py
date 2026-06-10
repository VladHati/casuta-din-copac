#!/usr/bin/env python3
"""
Regenereaza toate PDF-urile din paginile HTML + dosarul Markdown.
Ruleaza local sau in CI (GitHub Actions). Iesirea merge in ./PDF/.

  python3 build_pdfs.py

Dependinte: weasyprint, markdown, pypdf  (vezi requirements.txt)
Sistem: libpango + libcairo (in CI le instalam cu apt).
"""
import os, time
from weasyprint import HTML
import markdown
from pypdf import PdfWriter

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "PDF")
os.makedirs(OUT, exist_ok=True)

# (sursa HTML, fisier PDF)
PAGES = [
    ("casuta-din-copac.html", "00-Prezentare.pdf"),
    ("ghid-montaj.html",      "02-Ghid-montaj-pas-cu-pas.pdf"),
    ("imbinari.html",         "03-Imbinari.pdf"),
    ("audit.html",            "04-Audit-tehnic.pdf"),
    ("materiale.html",        "06-Materiale.pdf"),
]

DOSSIER_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Space+Grotesk:wght@400;500;600;700&display=swap');
@page{size:A4;margin:22mm 20mm}
body{font-family:'Space Grotesk',system-ui,sans-serif;color:#26241F;line-height:1.55;font-size:11.5pt}
h1,h2,h3{font-family:'Fraunces',Georgia,serif;font-weight:600;color:#1C1C1C;line-height:1.1}
h1{font-size:26pt;margin:0 0 6pt;border-bottom:3px solid #1C1C1C;padding-bottom:8pt}
h2{font-size:16pt;margin:20pt 0 6pt}
h3{font-size:13pt;margin:14pt 0 4pt}
table{border-collapse:collapse;width:100%;font-size:10.5pt;margin:8pt 0}
th,td{border:1px solid #ccc;padding:5pt 8pt;text-align:left}
th{background:#1C1C1C;color:#fff}
hr{border:none;border-top:1px solid #E2E2E2;margin:16pt 0}
code{background:#f3efe8;padding:1pt 4pt;border-radius:3px;font-family:monospace}
ul,ol{padding-left:18pt}
li{margin:3pt 0}
</style>"""

def build_dossier():
    md = open(os.path.join(ROOT, "CASUTA-DIN-COPAC.md"), encoding="utf-8").read()
    body = markdown.markdown(md, extensions=["tables", "fenced_code"])
    doc = f"<!doctype html><html lang='ro'><head><meta charset='utf-8'>{DOSSIER_CSS}</head><body>{body}</body></html>"
    HTML(string=doc, base_url=ROOT).write_pdf(os.path.join(OUT, "05-Dosar-proiect.pdf"))

def main():
    for src, out in PAGES:
        t = time.time()
        HTML(os.path.join(ROOT, src)).write_pdf(os.path.join(OUT, out))
        print(f"OK {src:30s} -> PDF/{out} ({time.time()-t:.1f}s)")
    build_dossier()
    print("OK dosar -> PDF/05-Dosar-proiect.pdf")

    # Manual combinat
    order = ["00-Prezentare.pdf",
             "02-Ghid-montaj-pas-cu-pas.pdf", "06-Materiale.pdf",
             "03-Imbinari.pdf", "04-Audit-tehnic.pdf",
             "05-Dosar-proiect.pdf"]
    w = PdfWriter()
    for f in order:
        w.append(os.path.join(OUT, f))
    with open(os.path.join(OUT, "Manual-Faza-1-complet.pdf"), "wb") as fh:
        w.write(fh)
    print("OK manual combinat -> PDF/Manual-Faza-1-complet.pdf")

if __name__ == "__main__":
    main()
