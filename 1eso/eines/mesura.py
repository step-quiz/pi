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

També mira l'amplada (29/9/2026): el que es veu no pot sortir més de mig centímetre
pel marge dret (a partir d'1,4 cm, surt del full i no s'imprimeix), i el text d'una
opció per marcar no pot sortir de la seva capsa.
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
    vessen, justes, totes, amples = [], [], [], []
    fonts = ([(f, "pàgina") for f in sorted(glob.glob(os.path.join(ARREL, "fitxes", "ud*.html")))]
             + [(f, "cara") for f in sorted(glob.glob(os.path.join(ARREL, "targetes", "*.html")))])
    for origen, paraula in fonts:
        nom = os.path.relpath(origen, ARREL)
        cap, alumnat, _ = paper.blocs(open(origen, encoding="utf-8").read())
        for i, full in enumerate(alumnat, 1):
            m = paper.mida(cap, full, os.path.dirname(origen))
            h = m["alcada"]
            totes.append((nom, paraula, i, h))
            if m["dreta"] > 0.5:
                amples.append(f"{nom} {paraula} {i}: surt {m['dreta']:.1f} cm pel marge dret")
            elif m["dreta"] > 0.3:
                justes.append(f"{nom} {paraula} {i}: arriba a {m['dreta']:.1f} cm dins del marge dret")
            if m["capses"]:
                amples.append(f"{nom} {paraula} {i}: text que surt de la capsa de l'opció: {', '.join(m['capses'])}")
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
    if amples:
        print(f"\n{len(amples)} PÀGINES MASSA AMPLES:")
        for v in amples:
            print("  ·", v)
    if vessen or amples:
        sys.exit(1)
    print("\nTotes caben en un A4, d'alt i d'ample.")


if __name__ == "__main__":
    main()
