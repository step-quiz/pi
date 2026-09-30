"""peca() i blocs(): els blocs de centenes, desenes i unitats de fitxa_ud1_nombres.py,
que també fan servir la unitat 5 i la targeta dels decimals. Fins al 30/9/2026, els altres
generadors executaven aquell tros de fitxa_ud1_nombres.py; ara és un mòdul."""
import math  # noqa: F401

from peces_comunes import *  # noqa: F401,F403


def peca(d, x, y, files, cols, m, estil):
    """Un bloc: un quadrat de 100 (10 per 10), una columna de 10 (10 per 1) o
    un quadret (1 per 1). estil: 'ple' (per llegir), 'buit' (per pintar) o
    'pintat' (l'apartat resolt, pintat a mà)."""
    fons, traç, gruix, linia = {
        "ple": (F3, NEGRE, 1.4, G3),
        "buit": ("#fff", G2, 1.2, F4),
        "pintat": (VORA_SUAU, MS, 2.2, G2),
    }[estil]
    d.cru(f'<rect x="{d.px(x)}" y="{d.px(y)}" width="{d.px(cols * m)}" height="{d.px(files * m)}" '
          f'fill="{fons}" stroke="{traç}" stroke-width="{gruix}" stroke-linejoin="round"/>')
    for fi in range(1, files):
        d.cru(f'<line x1="{d.px(x)}" y1="{d.px(y + fi * m)}" x2="{d.px(x + cols * m)}" y2="{d.px(y + fi * m)}" '
              f'stroke="{linia}" stroke-width="0.7"/>')
    for c in range(1, cols):
        d.cru(f'<line x1="{d.px(x + c * m)}" y1="{d.px(y)}" x2="{d.px(x + c * m)}" y2="{d.px(y + files * m)}" '
              f'stroke="{linia}" stroke-width="0.7"/>')


def blocs(c, dd, u, m, aria, buits=None, pinta=None):
    """Els blocs d'un nombre, en una fila: quadrats de 100, columnes de 10 i
    quadrets solts (tres per fila, com els punts d'un dau).
    Sense `buits`: c, dd i u blocs plens, per llegir. Si no n'hi ha cap d'un
    tipus, aquell lloc no hi és: al paper, es compta el que es veu.
    Amb `buits` = (quadrats, columnes, quadrets): les siluetes per pintar, i
    `pinta` = (c, d, u) diu quantes van pintades (l'apartat resolt)."""
    gq, gc, gu, gz = 0.28, 0.12, 0.08, 0.5
    S = 10 * m
    nq, nc, nu = buits if buits else (c, dd, u)
    pq, pc, pu = pinta if pinta else (0, 0, 0)
    zones = []
    if nq:
        zones.append(("q", nq * S + (nq - 1) * gq))
    if nc:
        zones.append(("c", nc * m + (nc - 1) * gc))
    if nu:
        zones.append(("u", min(nu, 3) * m + (min(nu, 3) - 1) * gu))
    amp = sum(w for _, w in zones) + gz * (len(zones) - 1) + 0.2
    d = Dibuix(max(amp, 1.0), S + 0.2, aria)
    x = 0.1
    for tipus, w in zones:
        if tipus == "q":
            for i in range(nq):
                estil = "pintat" if i < pq else ("buit" if buits else "ple")
                peca(d, x + i * (S + gq), 0.1, 10, 10, m, estil)
        elif tipus == "c":
            for i in range(nc):
                estil = "pintat" if i < pc else ("buit" if buits else "ple")
                peca(d, x + i * (m + gc), 0.1, 10, 1, m, estil)
        else:
            files = math.ceil(nu / 3)
            for i in range(nu):
                fi, co = i // 3, i % 3
                y = 0.1 + S - (files - fi) * m - (files - fi - 1) * gu
                estil = "pintat" if i < pu else ("buit" if buits else "ple")
                peca(d, x + co * (m + gu), y, 1, 1, m, estil)
        x += w + gz
    return d


__all__ = [n for n in dir() if not n.startswith("__")]
