#!/usr/bin/env python3
"""Mesura si cada pàgina de l'alumnat i cada cara de targeta cap en un A4.

    pip install weasyprint --break-system-packages      (només el primer cop)
    python3 1eso/eines/mesura.py                         (des de l'arrel del repositori)

Cada bloc .full ha de ser exactament una pàgina impresa. Aquest script el
renderitza en una pàgina molt alta, mira on acaba el contingut i ho compara amb
l'alçada útil d'un A4, amb el mateix full d'estil que fa servir gen_pdf.py
(tots dos el prenen d'eines/paper.py). El solucionari no s'hi inclou: pot
ocupar les pàgines que calgui, perquè és per a l'adult.

Si una pàgina vessa, l'arreglada NO és encongir la lletra —el cos de 14 pt és
una restricció del projecte— sinó treure'n contingut o partir-la en dues.
"""
import glob, os, sys

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ARREL, "eines"))
import paper  # noqa: E402

try:
    import weasyprint  # noqa: F401
except ImportError:
    sys.exit("Falta WeasyPrint:  pip install weasyprint --break-system-packages")


def main():
    print(f"Alçada útil d'un A4: {paper.UTIL_CM:.1f} cm\n")
    vessen, justes, totes = [], [], []
    fonts = ([(f, "pàgina") for f in sorted(glob.glob(os.path.join(ARREL, "fitxes", "ud*.html")))]
             + [(f, "cara") for f in sorted(glob.glob(os.path.join(ARREL, "targetes", "*.html")))])
    for origen, paraula in fonts:
        nom = os.path.relpath(origen, ARREL)
        cap, alumnat, _ = paper.blocs(open(origen, encoding="utf-8").read())
        for i, full in enumerate(alumnat, 1):
            h = paper.alcada_cm(cap, full, os.path.dirname(origen))
            totes.append((nom, paraula, i, h))
            if h > paper.UTIL_CM:
                vessen.append(f"{nom} {paraula} {i}: sobren {h - paper.UTIL_CM:.1f} cm")
            elif paper.UTIL_CM - h < 1.0:
                justes.append(f"{nom} {paraula} {i}: només hi queda {paper.UTIL_CM - h:.1f} cm")

    for nom, paraula, i, h in totes:
        print(f"  {nom:24} {paraula} {i}: {h:4.1f} cm · en queden {paper.UTIL_CM - h:4.1f}")
    print(f"\nPàgines mesurades: {len(totes)}")
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
