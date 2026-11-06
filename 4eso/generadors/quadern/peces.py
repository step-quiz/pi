"""Les peces dels quaderns de 4eso/ que no són al motor (comu/generadors/quadern.py).

    from peces import balances

La balança és la de la fitxa de la UD4 (u4/fitxa.html, pàgina 5): una bossa amb una x és
el número que no sabem, i els daus són unitats. Aquí els plats són una mica més amples,
perquè hi càpiguen fins a quatre bosses o dotze daus (en dos pisos).
"""
from quadern import llista, NEG, FONS2, TIP

DAU, PAS_DAU = 20, 23          # el costat d'un dau i el pas entre daus
BOSSA_W, BOSSA_H, PAS_BOSSA = 34, 28, 38
PLAT = 140                     # l'amplada útil de cada plat
BASE = 95                      # on comencen els plats


def _plat(cx, bosses, daus):
    """Les bosses i els daus d'un plat centrat a cx, posats en files de baix a dalt (dues com a
    molt: fins a sis daus per fila)."""
    peces = [("b", BOSSA_W, PAS_BOSSA)] * bosses + [("d", DAU, PAS_DAU)] * daus
    files, fila, ample = [], [], 0
    for p in peces:
        if fila and ample + p[1] > PLAT:
            files.append(fila)
            fila, ample = [], 0
        fila.append(p)
        ample += p[2]
    if fila:
        files.append(fila)
    assert len(files) <= 2, (bosses, daus)
    o, base = [], BASE
    for fila in files:
        ample = sum(p[2] for p in fila) - (fila[-1][2] - fila[-1][1])
        x = cx - ample / 2
        alt = max(BOSSA_H if p[0] == "b" else DAU for p in fila)
        for tipus, w, pas in fila:
            if tipus == "b":
                o.append(f'<rect x="{x:g}" y="{base - BOSSA_H:g}" width="{BOSSA_W}" height="{BOSSA_H}" rx="7" '
                         f'fill="#fff" stroke="{NEG}" stroke-width="3"/>'
                         f'<text x="{x + BOSSA_W / 2:g}" y="{base - 8:g}" text-anchor="middle" font-size="20" '
                         f'font-weight="800" fill="{NEG}" {TIP}>x</text>')
            else:
                o.append(f'<rect x="{x:g}" y="{base - DAU:g}" width="{DAU}" height="{DAU}" fill="#D4D4D4" '
                         f'stroke="{NEG}" stroke-width="2.5"/>')
            x += pas
        base -= alt + 3
    return "".join(o)


def balanca(bosses, daus_esq, daus_dreta):
    """La balança en equilibri: `bosses` bosses i `daus_esq` daus a l'esquerra, `daus_dreta` daus
    a la dreta. Totes fan la mateixa mida: 7 cm d'ample."""
    quin = (f"{bosses} bosses" if bosses > 1 else "una bossa") + (f" i {daus_esq} daus" if daus_esq else "")
    plats = "".join(f'<line x1="{cx}" y1="18" x2="{cx}" y2="{BASE}" stroke="{NEG}" stroke-width="2.5"/>'
                    f'<path d="M{cx - 72} {BASE}h144l-11 13H{cx - 61}z" fill="{FONS2}" stroke="{NEG}" '
                    f'stroke-width="3" stroke-linejoin="round"/>' for cx in (75, 235))
    return (f'<svg viewBox="0 0 310 132" style="width:7cm" role="img" '
            f'aria-label="Balança: {quin} contra {daus_dreta} daus">'
            f'<rect x="148" y="18" width="14" height="102" fill="{NEG}"/>'
            f'<rect x="118" y="118" width="74" height="10" rx="4" fill="{NEG}"/>'
            f'<line x1="8" y1="18" x2="302" y2="18" stroke="{NEG}" stroke-width="6" stroke-linecap="round"/>'
            f'{plats}{_plat(75, bosses, daus_esq)}{_plat(235, 0, daus_dreta)}</svg>')


def equacio(bosses, daus_esq, daus_dreta):
    x = "x" if bosses == 1 else f"{bosses}x"
    return f"{x} + {daus_esq} = {daus_dreta}" if daus_esq else f"{x} = {daus_dreta}"


def passos(bosses, daus_esq, daus_dreta):
    """El camí de la solució: treure els daus de cada banda i, si hi ha més d'una bossa,
    repartir. Torna (els passos, el valor de la x)."""
    v, r = divmod(daus_dreta - daus_esq, bosses)
    assert r == 0 and v > 0, (bosses, daus_esq, daus_dreta)
    p = [equacio(bosses, daus_esq, daus_dreta)]
    if daus_esq and bosses > 1:
        p.append(f"{bosses}x = {daus_dreta - daus_esq}")
    p.append(f"x = {v}")
    return p, v


def balances(apartats):
    """Cada apartat, una balança, i al costat la cadena per escriure l'equació i la x. Els
    apartats són (bosses, daus a l'esquerra, daus a la dreta). L'a) ja va resolt."""
    def alumnat(lletra, it, resolt):
        p, _ = passos(*it)
        if resolt:
            cadena = ('<div class="cadena resolt" style="border-radius:9px;padding:.3rem .6rem">'
                      + '<span class="fletxa">→</span>'.join(
                          f'<span class="ms" style="font-size:17pt">{t}</span>' for t in (p[0], p[-1]))
                      + "</div>")
        else:
            cadena = ('<div class="cadena"><span class="baula buida"></span><span class="fletxa">→</span>'
                      '<span class="baula buida"></span></div>')
        return f'{lletra}{balanca(*it)}<div class="resposta">{cadena}</div>'

    def sol(it):
        return " → ".join(passos(*it)[0])
    return llista(apartats, alumnat, sol)


# ------------------------------------------------- la recta (UD1) --

def recta(a, creu=None, ma=False):
    """El tros de recta de a a a + 1, partit en desenes, com la de la fitxa de la UD1 (pàgina 4).
    Amb `creu`, una creu en aquell punt: escrita a mà (`ma`, l'apartat resolt) o impresa (per
    llegir-ne el número). El dibuix fa 13 cm d'ample."""
    from quadern import MANUS
    x0, x1, y = 12, 128, 16
    px = lambda v: x0 + (v - a) * (x1 - x0)                                    # noqa: E731
    o = [f'<line x1="{x0 - 6}" y1="{y}" x2="{x1 + 6}" y2="{y}" stroke="{NEG}" stroke-width="1.2"/>']
    for k in range(11):
        h = 4.5 if k in (0, 10) else 3.2 if k == 5 else 2.2
        o.append(f'<line x1="{px(a + k / 10):g}" y1="{y - h}" x2="{px(a + k / 10):g}" y2="{y + h}" '
                 f'stroke="{NEG}" stroke-width="{1.1 if k in (0, 5, 10) else .7}"/>')
    for v in (a, a + 1):
        o.append(f'<text x="{px(v):g}" y="{y + 10.5}" text-anchor="middle" font-size="6" font-weight="700" '
                 f'fill="{NEG}" {TIP}>{v}</text>')
    if creu is not None:
        c, r = px(creu), 3.2
        col, g = (MANUS, 1.4) if ma else (NEG, 1.2)
        o.append(f'<path d="M{c - r:g} {y - r - 5:g}l{2 * r:g} {2 * r:g}M{c + r:g} {y - r - 5:g}l{-2 * r:g} {2 * r:g}" '
                 f'stroke="{col}" stroke-width="{g}" stroke-linecap="round" fill="none"/>'
                 f'<line x1="{c:g}" y1="{y - 3:g}" x2="{c:g}" y2="{y:g}" stroke="{col}" stroke-width=".8" stroke-dasharray="1 1"/>')
    return (f'<svg viewBox="0 0 140 30" style="width:13cm;max-width:100%" role="img" '
            f'aria-label="Recta del {a} al {a + 1}, partida en desenes">{"".join(o)}</svg>')
