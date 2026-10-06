"""Les peces comunes de tots els generadors de 1eso/: la classe Dibuix, els colors,
ms(), buit(), buit_curt(), ULL, rect_sol(), graella_per_pintar() i desa().

Abans (fins al 30/9/2026) eren la primera part de fitxa_ud1.py, i els altres generadors
l'executaven amb exec(), tallada just a la línia «pagines = []». Si aquella línia es
movia, deixaven de funcionar, i un canvi en una peça no es veia d'on venia. Ara és un
mòdul: `from peces_comunes import *`.
"""
import os
import sys

CM = 37.795            # píxels CSS per centímetre
NEGRE, G1, G2, G3 = "#000", "#333", "#5E5E5E", "#8A8A8A"
VORA_SUAU, F1, F2, F3, F4 = "#BFBFBF", "#F2F2F2", "#E4E4E4", "#D4D4D4", "#C4C4C4"
MS = "#3A3A3A"         # la tinta de la lletra manuscrita
# Els rètols dels dibuixos: 12 pt com a mínim tal com surten al PDF (regla 3). 0,43 cm són
# 12,2 pt. Fins al 6/10/2026 eren 0,42 cm, que fan 11,9 pt, i alguns, 0,34 cm (9,6 pt).
RETOL = 0.43


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


class Dibuix:
    """Un SVG amb mides en centímetres. Tot es dibuixa en cm i es passa a px."""

    def __init__(self, amp, alt, aria, estil=""):
        self.amp, self.alt, self.aria, self.estil = amp, alt, aria, estil
        self.el = []

    def px(self, v):
        return f(v * CM)

    def quadret(self, x, y, m, fons=F3, traç=NEGRE, gruix=1.6, discontinu=False, aire=0.1):
        a = m * aire
        d = ' stroke-dasharray="4 3"' if discontinu else ""
        self.el.append(f'<rect x="{self.px(x + a / 2)}" y="{self.px(y + a / 2)}" width="{self.px(m - a)}" '
                       f'height="{self.px(m - a)}" rx="{self.px(m * 0.13)}" fill="{fons}" stroke="{traç}" '
                       f'stroke-width="{gruix}"{d}/>')

    def rectangle(self, x, y, files, cols, m, **k):
        for fi in range(files):
            for c in range(cols):
                self.quadret(x + c * m, y + fi * m, m, **k)

    def graella(self, x, y, files, cols, m):
        """La quadrícula buida per pintar-hi a mà."""
        self.el.append(f'<rect x="{self.px(x)}" y="{self.px(y)}" width="{self.px(cols * m)}" '
                       f'height="{self.px(files * m)}" fill="#fff" stroke="{G2}" stroke-width="1.6"/>')
        for fi in range(1, files):
            self.el.append(f'<line x1="{self.px(x)}" y1="{self.px(y + fi * m)}" x2="{self.px(x + cols * m)}" '
                           f'y2="{self.px(y + fi * m)}" stroke="{G3}" stroke-width="1"/>')
        for c in range(1, cols):
            self.el.append(f'<line x1="{self.px(x + c * m)}" y1="{self.px(y)}" x2="{self.px(x + c * m)}" '
                           f'y2="{self.px(y + files * m)}" stroke="{G3}" stroke-width="1"/>')

    def pintat(self, x, y, files, cols, m):
        """Un rectangle pintat a mà dins de la quadrícula: gris de llapis i la vora resseguida."""
        self.el.append(f'<rect x="{self.px(x)}" y="{self.px(y)}" width="{self.px(cols * m)}" '
                       f'height="{self.px(files * m)}" fill="{VORA_SUAU}" stroke="none"/>')
        for fi in range(1, files):
            self.el.append(f'<line x1="{self.px(x)}" y1="{self.px(y + fi * m)}" x2="{self.px(x + cols * m)}" '
                           f'y2="{self.px(y + fi * m)}" stroke="{G2}" stroke-width="1"/>')
        for c in range(1, cols):
            self.el.append(f'<line x1="{self.px(x + c * m)}" y1="{self.px(y)}" x2="{self.px(x + c * m)}" '
                           f'y2="{self.px(y + files * m)}" stroke="{G2}" stroke-width="1"/>')
        self.el.append(f'<rect x="{self.px(x)}" y="{self.px(y)}" width="{self.px(cols * m)}" '
                       f'height="{self.px(files * m)}" fill="none" stroke="{MS}" stroke-width="2.6" '
                       f'stroke-linejoin="round"/>')

    def text(self, x, y, t, mida=0.5, pes=400, ancora="middle", ma=False, color=NEGRE):
        """Un text. `mida` en cm. Amb ma=True, en lletra manuscrita."""
        estil = ' style="font-family:var(--manuscrita)"' if ma else ""
        c = MS if ma else color
        self.el.append(f'<text x="{self.px(x)}" y="{self.px(y)}" font-size="{self.px(mida)}" '
                       f'font-weight="{pes}" text-anchor="{ancora}" fill="{c}"{estil}>{t}</text>')

    def clau_dalt(self, x1, x2, y, t, mida=RETOL):
        self.el.append(f'<path d="M{self.px(x1)} {self.px(y + 0.2)} V{self.px(y)} H{self.px(x2)} '
                       f'V{self.px(y + 0.2)}" fill="none" stroke="{G2}" stroke-width="1.6"/>')
        self.text((x1 + x2) / 2, y - 0.15, t, mida, color=G1)

    def clau_esq(self, x, y1, y2, t, mida=RETOL):
        self.el.append(f'<path d="M{self.px(x + 0.2)} {self.px(y1)} H{self.px(x)} V{self.px(y2)} '
                       f'H{self.px(x + 0.2)}" fill="none" stroke="{G2}" stroke-width="1.6"/>')
        self.text(x - 0.15, (y1 + y2) / 2 + mida * 0.35, t, mida, ancora="end", color=G1)

    def cercle_ma(self, cx, cy, rx, ry):
        """Un encerclat fet a mà al voltant d'un dibuix."""
        self.el.append(f'<ellipse cx="{self.px(cx)}" cy="{self.px(cy)}" rx="{self.px(rx)}" ry="{self.px(ry)}" '
                       f'fill="none" stroke="{MS}" stroke-width="3" transform="rotate(-4 {self.px(cx)} '
                       f'{self.px(cy)})"/>')

    def cru(self, s):
        self.el.append(s)

    def svg(self, sagnat="    "):
        cap = (f'<svg viewBox="0 0 {self.px(self.amp)} {self.px(self.alt)}" '
               f'style="width:{f(self.amp)}cm;max-width:100%;margin:0 auto;{self.estil}" '
               f'role="img" aria-label="{self.aria}">')
        return sagnat + cap + "\n" + "\n".join(sagnat + "  " + e for e in self.el) + "\n" + sagnat + "</svg>"


def rect_sol(files, cols, m, aria, marge=0.1):
    d = Dibuix(cols * m + 2 * marge, files * m + 2 * marge, aria)
    d.rectangle(marge, marge, files, cols, m)
    return d


def graella_per_pintar(files, cols, m, aria, pinta=None):
    d = Dibuix(cols * m + 0.1, files * m + 0.1, aria)
    d.graella(0.05, 0.05, files, cols, m)
    if pinta:
        d.pintat(0.05, 0.05, pinta[0], pinta[1], m)
    return d


ULL = ('<svg class="ull" viewBox="0 0 48 48" aria-hidden="true"><path d="M3 24s8-13 21-13 21 13 21 13-8 '
       '13-21 13S3 24 3 24z" fill="#F2F2F2" stroke="#000" stroke-width="3" stroke-linejoin="round"/>'
       '<circle cx="24" cy="24" r="7" fill="#000"/></svg>')


def ms(t):
    return f'<span class="ms">{t}</span>'


def buit():
    return "<u></u>"


def buit_curt():
    """Un buit per a un número d'una o dues xifres: prou llarg per escriure-hi a mà,
    i prou curt perquè la frase no es parteixi en dues línies."""
    return '<u style="padding:0 1.1rem"></u>'


def desa(html, sortida):
    """Escriu l'HTML amb una capçalera que diu de quin generador surt: si algú l'edités a
    mà, el canvi es perdria la pròxima vegada que es generés. eines/comprova.py la mira."""
    generador = os.path.basename(sys.argv[0])
    avis = (f"<!-- Generat per 1eso/generadors/fitxes/{generador}. No l'editis a mà: "
            f"canvia el generador i torna'l a passar. -->\n")
    if html.startswith("<!DOCTYPE html>\n"):
        html = "<!DOCTYPE html>\n" + avis + html[len("<!DOCTYPE html>\n"):]
    else:
        html = avis + html
    # La barra de dalt, només a la pantalla: tornar a l'índex i baixar el PDF (30/9/2026).
    nom = os.path.basename(sortida)[:-5]
    if nom.startswith("ud"):
        pdfs = (f'<a class="pdf" href="../pdf/{nom}-alumnat.pdf" download>PDF de l\'alumnat</a>'
                f'<a class="pdf" href="../pdf/{nom}-solucionari.pdf" download>PDF del solucionari</a>')
    else:
        pdfs = f'<a class="pdf" href="../pdf/targeta-{nom}.pdf" download>PDF per imprimir</a>'
    barra = (f'<nav class="navega no-imprimir" aria-label="Navegació">'
             f'<a href="../fitxes.html">← totes les fitxes</a>{pdfs}</nav>\n')
    html = html.replace("<body>\n", "<body>\n" + barra, 1)
    with open(sortida, "w", encoding="utf-8") as f:
        f.write(html)


__all__ = [n for n in dir() if not n.startswith("__")]
