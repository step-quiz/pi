#!/usr/bin/env python3
"""Torna a fer els gràfics de les fitxes i els hi posa.

    python3 generadors/posa_grafics.py         (des de 4eso/)

Els gràfics de les fitxes no es dibuixen a mà: els fan els scripts gen_grafics*.py,
que escriuen un grafics*.json en aquesta carpeta. A les fitxes, cada gràfic va entre
dos marcadors:

    <!--grafic:PILOTA_GRAN--><svg …>…</svg><!--/grafic-->

Aquest script executa els generadors i substitueix el que hi ha entre cada parell de
marcadors pel gràfic nou. Si un marcador anomena un gràfic que cap generador no fa,
o un gràfic no surt a cap fitxa, ho diu i no toca res.

Abans d'aquest script (29/9/2026) els gràfics s'enganxaven a mà, i els documents
parlaven d'uns marcadors §NOM§ i d'un aplica_millores.py que ja no hi eren.
"""
import glob, json, os, re, subprocess, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ARREL = os.path.dirname(AQUI)
GENERADORS = ["gen_grafics.py", "gen_grafics2.py", "gen_grafics3.py", "gen_grafics4.py", "gen_grafics5.py"]
MARCADOR = re.compile(r"<!--grafic:(\w+)-->.*?<!--/grafic-->", re.S)


def main():
    for g in GENERADORS:
        r = subprocess.run([sys.executable, g], cwd=AQUI, capture_output=True, text=True)
        if r.returncode:
            sys.exit(f"{g} ha fallat:\n{r.stdout}{r.stderr}")
        print(f"  {g}: fet")
    grafics = {}
    for j in sorted(glob.glob(os.path.join(AQUI, "grafics*.json"))):
        with open(j, encoding="utf-8") as f:
            grafics.update(json.load(f))

    problemes, fets, usats = [], {}, set()
    fitxes = sorted(glob.glob(os.path.join(ARREL, "fitxes", "ud*.html")))
    textos = {f: open(f, encoding="utf-8").read() for f in fitxes}
    for f, text in textos.items():
        for nom in MARCADOR.findall(text):
            if nom not in grafics:
                problemes.append(f"{os.path.basename(f)}: el marcador grafic:{nom} no és de cap generador")
            usats.add(nom)
    for nom in sorted(set(grafics) - usats):
        problemes.append(f"el gràfic {nom} no surt a cap fitxa")
    if problemes:
        print("\nPROBLEMES (no s'ha tocat cap fitxa):")
        for p in problemes:
            print("  ·", p)
        sys.exit(1)

    for f, text in textos.items():
        nou = MARCADOR.sub(lambda m: f"<!--grafic:{m[1]}-->{grafics[m[1]]}<!--/grafic-->", text)
        if nou != text:
            with open(f, "w", encoding="utf-8") as sortida:
                sortida.write(nou)
            fets[os.path.basename(f)] = len(MARCADOR.findall(nou))
    print()
    for nom, n in fets.items():
        print(f"  {nom}: {n} gràfics posats al dia")
    if not fets:
        print("  Cap canvi: les fitxes ja tenien els gràfics d'ara.")
    print("\nDesprés: python3 eines/mesura.py, python3 generadors/gen_pdf.py i python3 eines/comprova.py")


if __name__ == "__main__":
    main()
