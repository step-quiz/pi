#!/usr/bin/env python3
"""Genera els PDF de cada unitat: un per a l'alumnat i un per al professorat.

    pip install weasyprint --break-system-packages
    python3 generadors/gen_pdf.py

Cada fitxa és una sola pàgina HTML amb diversos blocs `.full`. L'últim és el
solucionari (`.full.sol`). Aquest script parteix la fitxa en dos documents:

    pdf/udN-alumnat.pdf       tots els .full menys el solucionari
    pdf/udN-solucionari.pdf   només el solucionari

El mateix per a les fitxes de repàs (udN-repas.html → udN-repas-alumnat.pdf…), i cada
targeta de consulta (targetes/NOM.html) fa un sol PDF amb totes les cares:
pdf/targeta-NOM.pdf.

A pdf/empremtes.json hi va l'empremta de la font de cada PDF (eines/empremta.py):
eines/comprova.py la torna a calcular i diu quins PDF han quedat vells.

PER QUÈ CAL UN FULL D'ESTIL A PART
El navegador i el motor de paginació no mesuren igual. Aquí es fixa la geometria
de la pàgina amb @page i es treu el padding de `.full`, que a pantalla fa de
marge del full i en PDF duplicaria el marge de la pàgina. El cos de 14 pt NO es
toca: si alguna pàgina no cabés, s'ha d'arreglar la fitxa, no encongir la lletra.
"""
import glob, json, os, re, sys

try:
    from weasyprint import HTML, CSS
except ImportError:
    sys.exit("Falta WeasyPrint:  pip install weasyprint --break-system-packages")

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ARREL, "eines"))
from empremta import empremta  # noqa: E402  (només biblioteca estàndard)
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


def fonts():
    """Les pàgines de paper, en ordre: cada fitxa (udN.html i, si en té, udN-repas.html) i
    cada targeta de consulta (targetes/NOM.html). Torna (camí, nom del PDF, és targeta)."""
    fitxes = sorted(glob.glob(os.path.join(FITXES, "ud*.html")),
                    key=lambda f: (int(re.search(r"ud(\d+)", f)[1]), "-" in os.path.basename(f), f))
    targetes = sorted(glob.glob(os.path.join(ARREL, "targetes", "*.html")))
    return ([(f, os.path.basename(f)[:-5], False) for f in fitxes]
            + [(f, "targeta-" + os.path.basename(f)[:-5], True) for f in targetes])


def main():
    os.makedirs(SORTIDA, exist_ok=True)
    problemes = []
    empremtes = {}
    for origen, nom, targeta in fonts():
        e = {"font": os.path.relpath(origen, ARREL), "empremta": empremta(os.path.relpath(origen, ARREL))}
        cap, alumnat, sol = blocs(open(origen, encoding="utf-8").read())
        if targeta:
            # Una targeta és un sol PDF amb totes les cares, per imprimir a doble cara.
            desti = f"{nom}.pdf"
            n1 = escriu(cap, alumnat, os.path.join(SORTIDA, desti))
            if n1 != len(alumnat):
                problemes.append(f"{nom}: {len(alumnat)} cares però {n1} pàgines al PDF")
            print(f"  {nom:22}  {n1} cares")
            empremtes[desti] = e
            continue
        n1 = escriu(cap, alumnat, os.path.join(SORTIDA, f"{nom}-alumnat.pdf"))
        n2 = escriu(cap, sol, os.path.join(SORTIDA, f"{nom}-solucionari.pdf"))

        # Cada .full de l'alumnat ha de ser exactament una pàgina.
        if n1 != len(alumnat):
            problemes.append(f"{nom}: {len(alumnat)} pàgines de fitxa però {n1} al PDF")
        # Si hi ha text manuscrit, el PDF ha de portar Caveat. Fins al 29/9/2026 no hi
        # era: els 14 PDF sortien amb el model resolt en lletra d'impremta i no avisava ningú.
        for blocs_, desti in ((alumnat, f"{nom}-alumnat.pdf"), (sol, f"{nom}-solucionari.pdf")):
            if MANUSCRITA.search("".join(blocs_)) and not any(
                    "Caveat" in n for n in lletres_del_pdf(os.path.join(SORTIDA, desti))):
                problemes.append(f"{desti}: hi ha text manuscrit però el PDF no porta Caveat")
        print(f"  {nom:22}  alumnat {n1} pàg.  ·  solucionari {n2} pàg.")
        empremtes[f"{nom}-alumnat.pdf"] = empremtes[f"{nom}-solucionari.pdf"] = e

    # L'empremta de cada PDF: eines/comprova.py la torna a calcular i avisa si és vell.
    with open(os.path.join(SORTIDA, "empremtes.json"), "w", encoding="utf-8") as f:
        json.dump(empremtes, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")

    if problemes:
        print("\nPROBLEMES:")
        for p in problemes:
            print("  ·", p)
        print("\nPassa `python3 eines/mesura.py` per veure quina pàgina vessa i quant.")
        sys.exit(1)
    print(f"\nFets a {os.path.relpath(SORTIDA, ARREL)}/")


if __name__ == "__main__":
    main()
