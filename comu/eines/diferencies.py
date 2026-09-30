#!/usr/bin/env python3
"""Les diferències entre les còpies de 1eso/ i 4eso/.

    python3 comu/eines/diferencies.py              la taula de tots els fitxers compartits
    python3 comu/eines/diferencies.py js/codi.js   les diferències d'un fitxer, línia a línia

1eso/ va néixer com a còpia de 4eso/, i es va decidir que cada curs tingués la seva
còpia dels fitxers de la caixa d'eines i del paper: així un canvi en un curs no pot
trencar l'altre. Però les còpies s'han anat separant sense que cap eina ho ensenyés.
Aquest script no canvia res ni falla mai: només ho fa visible, perquè quan s'arregla
una cosa en un curs es vegi si també cal a l'altre.

Els fitxers del MOTOR (MOTOR, a sota) són els que haurien de ser iguals o gairebé: si
algun dia hi ha 2n i 3r, aquests són els que haurien d'anar a comu/.

Només fa servir la biblioteca estàndard (30/9/2026).
"""
import difflib
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CURSOS = ("1eso", "4eso")
# El motor de la caixa: el que no depèn del contingut de cap curs.
MOTOR = {"js/nucli.js", "js/tasca.js", "js/codi.js", "js/app.js", "css/tokens.css"}
FORA = {"docs", "fitxes", "targetes", "pdf", "dades", "generadors", "fonts", "docx", "moduls"}


def compartits():
    """Els fitxers que hi ha, amb el mateix camí, a totes dues carpetes."""
    trobats = []
    base = os.path.join(REPO, CURSOS[0])
    for arrel, dirs, fitxers in os.walk(base):
        dirs[:] = [d for d in dirs if d not in FORA and not d.startswith((".", "__"))]
        for f in fitxers:
            rel = os.path.relpath(os.path.join(arrel, f), base)
            if f.endswith((".js", ".css", ".html", ".py")) and \
                    os.path.exists(os.path.join(REPO, CURSOS[1], rel)):
                trobats.append(rel)
    return sorted(trobats)


def linies(curs, rel):
    with open(os.path.join(REPO, curs, rel), encoding="utf-8") as f:
        return f.read().splitlines()


def taula():
    files = []
    for rel in compartits():
        a, b = linies(CURSOS[0], rel), linies(CURSOS[1], rel)
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        canvis = sum(max(i2 - i1, j2 - j1) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal")
        files.append((rel in MOTOR, rel, len(a), len(b), canvis, sm.ratio()))
    print(f"{'Fitxer':28} {'1eso':>6} {'4eso':>6} {'diferents':>10} {'iguals':>7}")
    for motor, rel, na, nb, canvis, r in sorted(files, key=lambda x: (not x[0], -x[5])):
        marca = "  motor" if motor else ""
        print(f"{rel:28} {na:6} {nb:6} {canvis:10} {r:6.0%}{marca}")
    print("\nMotor: haurien de ser iguals o gairebé. La resta és de cada curs a posta.")
    print("Per veure'n un: python3 comu/eines/diferencies.py js/codi.js")


def detall(rel):
    a, b = linies(CURSOS[0], rel), linies(CURSOS[1], rel)
    sys.stdout.writelines(l + "\n" for l in difflib.unified_diff(
        a, b, f"{CURSOS[0]}/{rel}", f"{CURSOS[1]}/{rel}", lineterm="", n=2))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        detall(sys.argv[1])
    else:
        taula()
