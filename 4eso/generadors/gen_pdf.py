#!/usr/bin/env python3
"""Genera els PDF de cada unitat: un per a l'alumnat i un per al professorat.

    pip install weasyprint --break-system-packages
    python3 generadors/gen_pdf.py

Cada fitxa és una sola pàgina HTML amb diversos blocs `.full`. L'últim és el
solucionari (`.full.sol`). Aquest script parteix la fitxa en dos documents:

    pdf/udN-alumnat.pdf       tots els .full menys el solucionari
    pdf/udN-solucionari.pdf   només el solucionari

PER QUÈ CAL UN FULL D'ESTIL A PART
El navegador i el motor de paginació no mesuren igual. Aquí es fixa la geometria
de la pàgina amb @page i es treu el padding de `.full`, que a pantalla fa de
marge del full i en PDF duplicaria el marge de la pàgina. El cos de 14 pt NO es
toca: si alguna pàgina no cabés, s'ha d'arreglar la fitxa, no encongir la lletra.
"""
import os, re, sys

try:
    from weasyprint import HTML, CSS
except ImportError:
    sys.exit("Falta WeasyPrint:  pip install weasyprint --break-system-packages")

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FITXES = os.path.join(ARREL, "fitxes")
SORTIDA = os.path.join(ARREL, "pdf")

# Carlito té les mètriques de Calibri i s'assembla a la font de sistema amb què
# es van dissenyar les fitxes. Si no hi és, el motor cau a la que trobi.
FULL_PDF = """
@page { size: A4; margin: 1.3cm 1.4cm; }
html { font-family: "Carlito", "DejaVu Sans", sans-serif; }
.full { min-height: 0 !important; max-width: none !important;
        padding: 0 !important; margin: 0 !important; display: block !important;
        break-after: page; page-break-after: always; }
.full:last-child { break-after: auto; page-break-after: auto; }
.no-imprimir { display: none !important; }
"""


def blocs(html):
    """Separa la capçalera, les pàgines de l'alumnat i el solucionari."""
    cap = html[:html.index("<body>") + 6]
    fulls = re.findall(r'<div class="full[^"]*">.*?\n</div>', html, re.S)
    alumnat = [f for f in fulls if 'class="full sol"' not in f]
    solucionari = [f for f in fulls if 'class="full sol"' in f]
    return cap, alumnat, solucionari


MANUSCRITA = re.compile(r'class="[^"]*\b(ms|et-resolt)\b')


def lletres_del_pdf(cami):
    """Els noms de les lletres incrustades en un PDF (només biblioteca estàndard).
    Els diccionaris poden anar dins de fluxos comprimits: es busquen als bytes i a
    cada flux descomprimit. El nom surt amb un prefix de subconjunt, /ABCDEF+Caveat."""
    import zlib
    with open(cami, "rb") as f:
        dades = f.read()
    trossos = [dades]
    for m in re.finditer(rb"stream\r?\n", dades):
        fi = dades.find(b"endstream", m.end())
        try:
            trossos.append(zlib.decompress(dades[m.end():fi]))
        except zlib.error:
            pass
    noms = set()
    for tros in trossos:
        noms |= {n.decode("latin-1") for n in re.findall(rb"/BaseFont\s*/[A-Z]{6}\+([\w-]+)", tros)}
    return sorted(noms)


def escriu(cap, fulls, desti):
    doc = HTML(string=cap + "\n".join(fulls) + "</body></html>", base_url=FITXES + "/")
    pagines = doc.render(stylesheets=[CSS(string=FULL_PDF)])
    pagines.write_pdf(desti)
    return len(pagines.pages)


def main():
    os.makedirs(SORTIDA, exist_ok=True)
    problemes = []
    for u in range(1, 8):
        origen = os.path.join(FITXES, f"ud{u}.html")
        if not os.path.exists(origen):
            continue
        cap, alumnat, sol = blocs(open(origen, encoding="utf-8").read())

        n1 = escriu(cap, alumnat, os.path.join(SORTIDA, f"ud{u}-alumnat.pdf"))
        n2 = escriu(cap, sol, os.path.join(SORTIDA, f"ud{u}-solucionari.pdf"))

        # Cada .full de l'alumnat ha de ser exactament una pàgina.
        if n1 != len(alumnat):
            problemes.append(f"ud{u}: {len(alumnat)} pàgines de fitxa però {n1} al PDF")
        # Si hi ha text manuscrit, el PDF ha de portar Caveat. Fins al 29/9/2026 no hi
        # era: els 14 PDF sortien amb el model resolt en lletra d'impremta i no avisava ningú.
        for blocs_, desti in ((alumnat, f"ud{u}-alumnat.pdf"), (sol, f"ud{u}-solucionari.pdf")):
            if MANUSCRITA.search("".join(blocs_)) and not any(
                    "Caveat" in n for n in lletres_del_pdf(os.path.join(SORTIDA, desti))):
                problemes.append(f"{desti}: hi ha text manuscrit però el PDF no porta Caveat")
        print(f"  ud{u}  alumnat {n1} pàg.  ·  solucionari {n2} pàg.")

    if problemes:
        print("\nPROBLEMES:")
        for p in problemes:
            print("  ·", p)
        print("\nPassa `python3 eines/mesura.py` per veure quina pàgina vessa i quant.")
        sys.exit(1)
    print(f"\nFets a {os.path.relpath(SORTIDA, ARREL)}/")


if __name__ == "__main__":
    main()
