#!/usr/bin/env python3
"""Mesura si cada pàgina de l'alumnat cap en un A4.

    pip install weasyprint --break-system-packages
    python3 eines/mesura.py

Cada bloc `.full` d'una fitxa ha de ser exactament una pàgina impresa. Aquest
script el renderitza en una pàgina molt alta, mira on acaba el contingut i ho
compara amb l'alçada útil d'un A4. El solucionari no s'hi inclou: pot ocupar
les pàgines que calgui, perquè és per a l'adult.

Passa-ho cada vegada que afegeixis contingut a una fitxa. Si una pàgina vessa,
l'arreglada NO és encongir la lletra —el cos de 14 pt és una restricció del
projecte— sinó treure'n contingut o partir-la en dues.
"""
import os, re, sys

try:
    from weasyprint import HTML, CSS
except ImportError:
    sys.exit("Falta WeasyPrint:  pip install weasyprint --break-system-packages")

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FITXES = os.path.join(ARREL, "fitxes")
UTIL = 29.7 - 2.6          # A4 menys els marges d'1,3 cm de dalt i de baix

ALTA = CSS(string='''
@page { size: 21cm 200cm; margin: 1.3cm 1.4cm; }
html { font-family: "Carlito", "DejaVu Sans", sans-serif; }
.full { min-height:0 !important; max-width:none !important; padding:0 !important;
        margin:0 !important; display:block !important; }
.no-imprimir { display:none !important; }
''')


def alcada_cm(cap, full):
    doc = HTML(string=cap + full + "</body></html>", base_url=FITXES + "/").render(stylesheets=[ALTA])
    def fons(caixa, m=0):
        if getattr(caixa, "element_tag", None) not in (None, "html"):
            m = max(m, caixa.position_y + caixa.height)
        for fill in getattr(caixa, "children", []):
            m = fons(fill, m)
        return m
    return fons(doc.pages[0]._page_box) / 96 * 2.54 - 1.3


def main():
    print(f"Alçada útil d'un A4: {UTIL:.1f} cm\n")
    vessen, justes, total = [], [], 0
    for u in range(1, 8):
        origen = os.path.join(FITXES, f"ud{u}.html")
        if not os.path.exists(origen):
            continue
        html = open(origen, encoding="utf-8").read()
        cap = html[:html.index("<body>") + 6]
        for i, full in enumerate(re.findall(r'<div class="full[^"]*">.*?\n</div>', html, re.S), 1):
            if 'class="full sol"' in full:
                continue
            total += 1
            h = alcada_cm(cap, full)
            if h > UTIL:
                vessen.append(f"ud{u} pàgina {i}: sobren {h-UTIL:.1f} cm")
            elif UTIL - h < 1.0:
                justes.append(f"ud{u} pàgina {i}: només hi queda {UTIL-h:.1f} cm")

    print(f"Pàgines de l'alumnat mesurades: {total}")
    if justes:
        print("\nAnar amb compte si s'hi afegeix res:")
        for j in justes:
            print("  ·", j)
    if vessen:
        print(f"\n{len(vessen)} PÀGINES QUE NO CABEN:")
        for v in vessen:
            print("  ·", v)
        sys.exit(1)
    print("\nTotes caben en un A4.")


if __name__ == "__main__":
    main()
