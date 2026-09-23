#!/usr/bin/env python3
"""Fa els PDF de les fitxes i de les targetes de consulta.

    pip install weasyprint --break-system-packages      (només el primer cop)
    python3 1eso/generadors/gen_pdf.py                   (des de l'arrel del repositori)

Què fa:

    fitxes/udN.html      →  pdf/udN-alumnat.pdf  i  pdf/udN-solucionari.pdf
    targetes/NOM.html    →  pdf/targeta-NOM.pdf  (totes les cares)

Cada bloc .full ha de ser exactament una pàgina. Si en surt una de més, algun
bloc vessa: `python3 1eso/eines/mesura.py` diu quin i quant.

També escriu pdf/empremtes.json: per a cada PDF, l'empremta de la seva font i
de tot el que decideix com surt (fulls d'estil, lletra, aquest procés). Així
`eines/comprova.py` sap si un PDF ha quedat vell després d'un canvi.
"""
import glob, json, os, re, sys

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ARREL, "eines"))
import paper  # noqa: E402

try:
    import weasyprint  # noqa: F401
except ImportError:
    sys.exit("Falta WeasyPrint:  pip install weasyprint --break-system-packages")

SORTIDA = os.path.join(ARREL, "pdf")
MANUSCRITA = re.compile(r'class="[^"]*\b(ms|et-resolt)\b')


def escriu(cap, fulls, carpeta, desti):
    doc = paper.document(cap, fulls, carpeta)
    doc.write_pdf(desti)
    return len(doc.pages)


def comprova_lletra(font_html, desti, problemes):
    """Si la font té text manuscrit, el PDF ha de portar Caveat a dins.

    Sense aquesta comprovació, un PDF fet en un ordinador sense la lletra surt
    igualment, però amb el model resolt en lletra d'impremta, i no avisa ningú.
    """
    if MANUSCRITA.search(font_html) and not any("Caveat" in n for n in paper.lletres_del_pdf(desti)):
        problemes.append(f"{os.path.basename(desti)}: hi ha text manuscrit però el PDF no porta "
                         f"Caveat (lletres: {paper.lletres_del_pdf(desti)})")


def main():
    os.makedirs(SORTIDA, exist_ok=True)
    empremtes, problemes = {}, []

    for origen in sorted(glob.glob(os.path.join(ARREL, "fitxes", "ud*.html"))):
        nom = os.path.basename(origen)[:-5]
        rel = os.path.relpath(origen, ARREL)
        html = open(origen, encoding="utf-8").read()
        cap, alumnat, sol = paper.blocs(html)
        carpeta = os.path.dirname(origen)
        pdf_a = os.path.join(SORTIDA, f"{nom}-alumnat.pdf")
        pdf_s = os.path.join(SORTIDA, f"{nom}-solucionari.pdf")
        n1 = escriu(cap, alumnat, carpeta, pdf_a)
        n2 = escriu(cap, sol, carpeta, pdf_s) if sol else 0
        if n1 != len(alumnat):
            problemes.append(f"{nom}: {len(alumnat)} pàgines de fitxa però {n1} al PDF")
        if not sol:
            problemes.append(f"{nom}: no té solucionari (.full.sol)")
        comprova_lletra("".join(alumnat), pdf_a, problemes)
        e = paper.empremta(rel)
        empremtes[f"{nom}-alumnat.pdf"] = {"font": rel, "pagines": n1, "empremta": e}
        empremtes[f"{nom}-solucionari.pdf"] = {"font": rel, "pagines": n2, "empremta": e}
        print(f"  {nom:8} alumnat {n1} pàg. · solucionari {n2} pàg.")

    for origen in sorted(glob.glob(os.path.join(ARREL, "targetes", "*.html"))):
        nom = os.path.basename(origen)[:-5]
        rel = os.path.relpath(origen, ARREL)
        html = open(origen, encoding="utf-8").read()
        cap, cares, _ = paper.blocs(html)
        desti = os.path.join(SORTIDA, f"targeta-{nom}.pdf")
        n = escriu(cap, cares, os.path.dirname(origen), desti)
        if n != len(cares):
            problemes.append(f"targeta {nom}: {len(cares)} cares però {n} pàgines al PDF")
        comprova_lletra(html, desti, problemes)
        empremtes[f"targeta-{nom}.pdf"] = {"font": rel, "pagines": n, "empremta": paper.empremta(rel)}
        print(f"  targeta {nom}: {n} pàg. · lletres: {', '.join(paper.lletres_del_pdf(desti))}")

    with open(os.path.join(SORTIDA, "empremtes.json"), "w", encoding="utf-8") as f:
        json.dump(empremtes, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")

    if problemes:
        print("\nPROBLEMES:")
        for p in problemes:
            print("  ·", p)
        print("\nPassa `python3 1eso/eines/mesura.py` per veure quina pàgina vessa i quant.")
        sys.exit(1)
    print(f"\nFets a {os.path.relpath(SORTIDA, os.path.dirname(ARREL))}/")


if __name__ == "__main__":
    main()
