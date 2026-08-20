#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Exporta desenele ca PNG cu fundal transparent, pentru Freeform / whiteboard.
import json, os, re, shutil
from playwright.sync_api import sync_playwright

OUT = 'FREEFORM-PNG'
LONG = 2200            # latura lunga, px

IKEA = json.load(open('figs_ikea.json'))
SCHM = json.load(open('figs.json'))
VERI = open('verificare_svg.txt').read()

JOBS = [
    # (subfolder, filename, svg)
    ('01-gol-colt', '01-asa-e-acum',            IKEA['acum']),
    ('01-gol-colt', '02-doua-vincluri',         IKEA['coltare']),
    ('01-gol-colt', '03-blocaj-pe-vincluri',    IKEA['blocaj']),
    ('01-gol-colt', '04-suruburi-oblice',       IKEA['suruburi']),
    ('01-gol-colt', '05-scandura-deasupra',     IKEA['scandura']),
    ('01-gol-colt', '06-gata',                  IKEA['gata']),
    ('01-gol-colt', '07-detaliu-taietura',      IKEA['detaliu']),
    ('01-gol-colt', '08-nu-asa',                IKEA['nu']),
    ('01-gol-colt', '09-plan-colt-A-B',         IKEA['plan']),
    ('01-gol-colt', '10-piesa-vinclu',          IKEA['ic_coltar']),
    ('01-gol-colt', '11-piesa-blocaj',          IKEA['ic_blocaj']),
    ('02-casa',     'F1-sectiune-ansamblu',     SCHM['f1']),
    ('02-casa',     'F2-perete-spate',          SCHM['f2']),
    ('02-casa',     'F3-perete-lateral',        SCHM['f3']),
    ('02-casa',     'F4-perete-fata',           SCHM['f4']),
    ('02-casa',     'F5-acoperis',              SCHM['f5']),
    ('02-casa',     'F6-ancorare-stalp-fata',   SCHM['f6']),
    ('03-verificare', 'patratura-stalpi',       VERI),
]


def sized(svg):
    """inlocuieste stilul inline cu dimensiuni px calculate din viewBox."""
    m = re.search(r'viewBox="(-?[\d.]+) (-?[\d.]+) ([\d.]+) ([\d.]+)"', svg)
    vw, vh = float(m.group(3)), float(m.group(4))
    k = LONG / max(vw, vh)
    w, h = round(vw * k), round(vh * k)
    svg = re.sub(r'style="[^"]*"', f'style="width:{w}px;height:{h}px;display:block"', svg, count=1)
    return svg, w, h


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        pg = b.new_page(viewport={'width': 1200, 'height': 900},
                        device_scale_factor=1)
        for sub, name, svg in JOBS:
            d = os.path.join(OUT, sub)
            os.makedirs(d, exist_ok=True)
            s, w, h = sized(svg)
            html = ('<html><head><style>html,body{margin:0;padding:0;background:transparent}'
                    '</style></head><body>' + s + '</body></html>')
            open('/tmp/_px.html', 'w').write(html)
            pg.set_viewport_size({'width': w + 4, 'height': h + 4})
            pg.goto('file:///tmp/_px.html')
            el = pg.query_selector('svg')
            el.screenshot(path=os.path.join(d, name + '.png'), omit_background=True)
            print(f'{sub}/{name}.png  {w}x{h}')
        b.close()


main()
