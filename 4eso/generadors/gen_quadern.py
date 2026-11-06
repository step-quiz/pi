#!/usr/bin/env python3
"""Fa els quaderns d'activitats de 4eso/: uN/quadern.html.

    python3 4eso/generadors/gen_quadern.py          (tots)
    python3 4eso/generadors/gen_quadern.py 3        (només la UD3)

El motor és comú a tots els cursos: comu/generadors/quadern.py (abans, fins al 6/11/2026,
era aquí mateix, a 4eso/generadors/gen_quadern.py). El contingut de cada quadern és a
generadors/quadern/udN.py. Aquest fitxer només diu el curs.
"""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "comu", "generadors"))
import quadern  # noqa: E402

if __name__ == "__main__":
    quadern.main(curs="4eso")
