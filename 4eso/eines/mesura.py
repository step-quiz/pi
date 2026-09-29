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

També mira l'amplada (29/9/2026), com a 1eso/: el que es veu no pot sortir més de
mig centímetre pel marge dret (a partir d'1,4 cm, surt del full), i el text d'una
opció per marcar no pot sortir de la seva capsa.
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


MARGE_DRET_CM = 21 - 1.4        # a partir d'aquí, el que es veu surt del marge


def visible(caixa):
    """Text, dibuixos, o capses amb vora o fons. Una capsa buida i sense vora pot ser
    més ampla que la pàgina sense que es vegi res."""
    nom = type(caixa).__name__
    if nom == "TextBox" or "Replaced" in nom or (getattr(caixa, "element_tag", None) or "").endswith("svg"):
        return True
    estil = getattr(caixa, "style", None)
    if estil is None:
        return False
    try:
        return (estil["border_right_width"] > 0 or estil["border_bottom_width"] > 0
                or estil["background_color"][3] > 0)
    except (KeyError, TypeError, IndexError):
        return False


def mida(cap, full):
    """L'alçada del contingut (cm), quant surt pel marge dret (cm) i els textos que
    surten de la capsa de la seva opció (<label>)."""
    doc = HTML(string=cap + full + "</body></html>", base_url=FITXES + "/").render(stylesheets=[ALTA])
    limit = MARGE_DRET_CM / 2.54 * 96
    r = {"fons": 0.0, "dreta": 0.0, "capses": set()}

    def mira(caixa, label=None):
        if getattr(caixa, "element_tag", None) not in (None, "html"):
            r["fons"] = max(r["fons"], caixa.position_y + caixa.height)
        try:
            x2 = caixa.border_box_x() + caixa.border_width()
        except (AttributeError, TypeError):
            x2 = None
        if x2 is not None and visible(caixa):
            r["dreta"] = max(r["dreta"], x2 - limit)
        if getattr(caixa, "element_tag", None) == "label" and type(caixa).__name__ != "TextBox" and x2 is not None:
            if label is None or caixa.element is not label[0]:
                label = (caixa.element, x2)
        if type(caixa).__name__ == "TextBox" and label is not None and caixa.position_x + caixa.width > label[1] + 1:
            r["capses"].add(caixa.text.strip()[:24])
        for fill in getattr(caixa, "children", []):
            mira(fill, label)
    mira(doc.pages[0]._page_box)
    return r["fons"] / 96 * 2.54 - 1.3, max(0.0, r["dreta"] / 96 * 2.54), sorted(r["capses"])


def main():
    print(f"Alçada útil d'un A4: {UTIL:.1f} cm\n")
    vessen, justes, amples, total = [], [], [], 0
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
            h, dreta, capses = mida(cap, full)
            if dreta > 0.5:
                amples.append(f"ud{u} pàgina {i}: surt {dreta:.1f} cm pel marge dret")
            elif dreta > 0.3:
                justes.append(f"ud{u} pàgina {i}: arriba a {dreta:.1f} cm dins del marge dret")
            if capses:
                amples.append(f"ud{u} pàgina {i}: text que surt de la capsa de l'opció: {', '.join(capses)}")
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
    if amples:
        print(f"\n{len(amples)} PÀGINES MASSA AMPLES:")
        for v in amples:
            print("  ·", v)
    if vessen or amples:
        sys.exit(1)
    print("\nTotes caben en un A4, d'alt i d'ample.")


if __name__ == "__main__":
    main()
