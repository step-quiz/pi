"""Les peces dels quaderns de 1eso/ que no són al motor (comu/generadors/quadern.py).

    from peces import F, fraccions_dibuix, tira_svg, talls_svg, parella_tires

Els dibuixos són els de les fitxes del curs: el rectangle de les fraccions (tira) i el partit
en trossos desiguals (tira_talls), de 1eso/generadors/fitxes/peces_fraccions.py, i la fracció
escrita com a fracció (fr). No es tornen a fer: s'importen, perquè paper i quadern siguin iguals.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fitxes"))
from peces_fraccions import fr, fr_buit, tira, tira_talls, nom  # noqa: E402

from quadern import llista, ms  # noqa: E402

__all__ = ["F", "fr", "nom", "fraccions_dibuix", "tira_svg", "talls_svg", "parella_tires"]


def F(n, d):
    """Una fracció: dibuixada a la pàgina de l'alumnat (a mà a l'apartat resolt) i «3/4» al solucionari."""
    return (fr(n, d), f"{n}/{d}", fr(n, d, ma=True))


def tira_svg(n, d, W=6.0, **k):
    return tira(n, d, f"Rectangle partit en {d} trossos iguals, amb {n} de pintats", W=W, H=0.8, **k).svg("")


def talls_svg(talls, pintat, W=6.0):
    iguals = all(abs((b - a) - 1 / (len(talls) + 1)) < 1e-9 for a, b in zip([0] + list(talls), list(talls) + [1]))
    aria = f"Rectangle partit en {len(talls) + 1} trossos {'iguals' if iguals else 'que no són iguals'}, amb un de pintat"
    return tira_talls(talls, pintat, aria, W=W, H=0.8).svg("")


def parella_tires(a, b, W=6.0):
    """Dues fraccions, cada una amb el seu rectangle, una sota l'altra: per comparar el tros pintat."""
    fila = ('<div style="display:flex;align-items:center;gap:.8rem;margin:.2rem 0">'
            '<span style="flex:0 0 1.2cm;text-align:center">{}</span>{}</div>')
    return "".join(fila.format(fr(n, d), tira_svg(n, d, W)) for n, d in (a, b))


def fraccions_dibuix(apartats):
    """Cada apartat, un rectangle amb trossos pintats, i al costat la fracció i com es llegeix.
    L'a) ja va resolt. Els apartats són (pintats, trossos)."""
    def alumnat(lletra, it, resolt):
        n, d = it
        if resolt:
            resp = f'{fr(n, d, ma=True)}<span>Es llegeix: {ms(nom(n, d))}</span>'
        else:
            resp = f'{fr_buit()}<span>Es llegeix: <span class="buit" style="min-width:4.5cm"></span></span>'
        return f'{lletra}{tira_svg(n, d)}<div class="resposta">{resp}</div>'

    return llista(apartats, alumnat, lambda it: f"{it[0]}/{it[1]}, {nom(*it)}")
