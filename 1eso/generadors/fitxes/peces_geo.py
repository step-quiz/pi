"""Peces de dibuix de la geometria (unitat 6): la targeta «Formes» i les fitxes ud6*.

S'hi entra amb exec(), després de les peces de la unitat 1 (fitxa_ud1.py): fa servir Dibuix i els
colors d'allà. Totes les mides en cm. Els mateixos models que la caixa (tasques 22 a 25): la
cantonada d'un quadret, discontínua, és l'angle recte; els polígons, al geoplà; els angles d'un
triangle, numerats, i junts fan un angle pla.
"""
import math


def _pt(cx, cy, r, graus):
    t = math.radians(graus)
    return cx + r * math.cos(t), cy - r * math.sin(t)


def _linia(d, x1, y1, x2, y2, color=None, gruix=3, extra=""):
    d.cru(f'<line x1="{d.px(x1)}" y1="{d.px(y1)}" x2="{d.px(x2)}" y2="{d.px(y2)}" stroke="{color or NEGRE}" '
          f'stroke-width="{gruix}" stroke-linecap="round"{extra}/>')


def _punt(d, x, y, r=0.09, color=None):
    d.cru(f'<circle cx="{d.px(x)}" cy="{d.px(y)}" r="{d.px(r)}" fill="{color or NEGRE}"/>')


def _sector(d, cx, cy, r, g1, g2, fons=F2, gruix=1.4):
    x1, y1 = _pt(cx, cy, r, g1)
    x2, y2 = _pt(cx, cy, r, g2)
    gran = 1 if g2 - g1 > 180 else 0
    d.cru(f'<path d="M{d.px(cx)} {d.px(cy)} L{d.px(x1)} {d.px(y1)} A{d.px(r)} {d.px(r)} 0 {gran} 0 {d.px(x2)} {d.px(y2)} Z" '
          f'fill="{fons}" stroke="{G1}" stroke-width="{gruix}"/>')


def _cantonada(d, x, y, c=0.7):
    """La cantonada d'un quadret al vèrtex (x, y), discontínua: l'angle recte de referència."""
    d.cru(f'<path d="M{d.px(x + c)} {d.px(y)} V{d.px(y - c)} H{d.px(x)}" fill="none" stroke="{G2}" '
          f'stroke-width="2.2" stroke-dasharray="5 3"/>')


def angle_d(graus, aria, llarg=2.1, cantonada=True, arc=True):
    """Un angle: el vèrtex a baix, un costat cap a la dreta i l'altre obert `graus`.
    Amb `cantonada`, la cantonada del quadret al vèrtex, discontínua."""
    amp = 2 * llarg + 0.6 if graus > 90 else llarg + 0.9
    vx = llarg + 0.3 if graus > 90 else 0.4
    vy = llarg * max(0.25, math.sin(math.radians(min(graus, 90)))) + 0.4 if graus < 180 else 0.95
    alt = vy + 0.35
    d = Dibuix(amp, alt, aria)
    if arc:
        _sector(d, vx, vy, 0.5, 0, graus)
    if cantonada:
        _cantonada(d, vx, vy)
    _linia(d, vx, vy, vx + llarg, vy)
    x2, y2 = _pt(vx, vy, llarg, graus)
    _linia(d, vx, vy, x2, y2)
    _punt(d, vx, vy)
    return d


def _fletxa(d, x, y, graus, mida=0.28):
    """Una punta de fletxa a (x, y), apuntant cap a `graus`."""
    a = _pt(x, y, mida, graus + 150)
    b = _pt(x, y, mida, graus - 150)
    d.cru(f'<path d="M{d.px(x)} {d.px(y)} L{d.px(a[0])} {d.px(a[1])} L{d.px(b[0])} {d.px(b[1])} Z" fill="{NEGRE}"/>')


def peca_linia(tipus, aria, amp=4.4):
    """Les peces bàsiques: punt, segment (dos extrems), semirecta (un extrem i una fletxa) i recta
    (dues fletxes: no s'acaba mai)."""
    d = Dibuix(amp, 0.9, aria)
    y, x1, x2 = 0.45, 0.4, amp - 0.4
    if tipus == "punt":
        _punt(d, amp / 2, y, 0.13)
        return d
    _linia(d, x1, y, x2, y)
    if tipus == "segment":
        _punt(d, x1, y, 0.12); _punt(d, x2, y, 0.12)
    elif tipus == "semirecta":
        _punt(d, x1, y, 0.12); _fletxa(d, x2 + 0.1, y, 0)
    elif tipus == "recta":
        _fletxa(d, x1 - 0.1, y, 180); _fletxa(d, x2 + 0.1, y, 0)
    return d


def rectes_d(tipus, aria, marca=False, amp=4.0, alt=2.6):
    """Dues rectes: paral·leles (mai no es tallen), secants (es tallen) o perpendiculars (es
    tallen i fan una cantonada; amb `marca`, la cantonada dibuixada)."""
    d = Dibuix(amp, alt, aria)
    if tipus == "paral·leles":
        for y in (alt * 0.38, alt * 0.78):
            _linia(d, 0.3, y + alt * 0.12, amp - 0.3, y - alt * 0.12)
    elif tipus == "secants":
        _linia(d, 0.3, alt - 0.2, amp - 0.3, 0.2)
        _linia(d, 0.3, alt * 0.3, amp - 0.3, alt * 0.75)
    else:
        cx, cy = amp / 2, alt / 2
        _linia(d, 0.3, cy, amp - 0.3, cy)
        _linia(d, cx, 0.2, cx, alt - 0.2)
        if marca:
            d.cru(f'<path d="M{d.px(cx + 0.35)} {d.px(cy)} V{d.px(cy - 0.35)} H{d.px(cx)}" fill="none" stroke="{G1}" stroke-width="2"/>')
    return d


def geopla_d(pts, aria, m=0.55, n=6, fons=F3):
    """El geoplà de n per n punts i un polígon pels punts `pts` ([x, y], y cap avall)."""
    d = Dibuix((n - 1) * m + 0.6, (n - 1) * m + 0.6, aria)
    X = lambda v: 0.3 + v * m
    for i in range(n):
        for j in range(n):
            _punt(d, X(i), X(j), 0.05, G3)
    if pts:
        d.cru(f'<polygon points="{" ".join(f"{d.px(X(x))},{d.px(X(y))}" for x, y in pts)}" fill="{fons}" '
              f'stroke="{G1}" stroke-width="3" stroke-linejoin="round"/>')
        for x, y in pts:
            _punt(d, X(x), X(y), 0.08)
    return d


def regular(n, r, gir=None):
    """Els vèrtexs d'un polígon regular de n costats, de radi r (y cap amunt). Per defecte, amb un
    vèrtex a dalt si n és senar i amb el costat de dalt pla si és parell."""
    if gir is None:
        gir = 90 if n % 2 else 90 + 180 / n
    return [(r * math.cos(math.radians(gir + k * 360 / n)), r * math.sin(math.radians(gir + k * 360 / n)))
            for k in range(n)]


def poligon_d(pts, aria, fons=F3, marge=0.25):
    """Un polígon qualsevol (coordenades en cm, y cap amunt com a les matemàtiques)."""
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    x0, y1 = min(xs) - marge, max(ys) + marge
    d = Dibuix(max(xs) - min(xs) + 2 * marge, max(ys) - min(ys) + 2 * marge, aria)
    d.cru(f'<polygon points="{" ".join(f"{d.px(x - x0)},{d.px(y1 - y)}" for x, y in pts)}" fill="{fons}" '
          f'stroke="{G1}" stroke-width="3" stroke-linejoin="round"/>')
    return d


def angles_de(pts):
    """Els angles (en graus) d'un triangle, a cada vèrtex."""
    r = []
    for i, p in enumerate(pts):
        a, b = pts[(i + 1) % 3], pts[(i + 2) % 3]
        u, v = (a[0] - p[0], a[1] - p[1]), (b[0] - p[0], b[1] - p[1])
        r.append(math.degrees(math.acos((u[0] * v[0] + u[1] * v[1]) / (math.hypot(*u) * math.hypot(*v)))))
    return r


def triangle_d(pts, aria, marques=None, arcs=False, marge=0.4, cantonada_a=None):
    """Un triangle (coordenades en cm, y cap amunt). `marques` = [k0, k1, k2]: quantes ratlletes porta
    cada costat (el costat i va del vèrtex i al i+1); els costats iguals porten les mateixes. Amb
    `arcs`, cada angle numerat (1, 2 i 3). Amb `cantonada_a` = i, la cantonada discontínua al vèrtex i."""
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    x0, y1 = min(xs) - marge, max(ys) + marge
    d = Dibuix(max(xs) - min(xs) + 2 * marge, max(ys) - min(ys) + 2 * marge, aria)
    P = [(x - x0, y1 - y) for x, y in pts]
    d.cru(f'<polygon points="{" ".join(f"{d.px(x)},{d.px(y)}" for x, y in P)}" fill="{F1}" stroke="{G1}" '
          f'stroke-width="3" stroke-linejoin="round"/>')
    fons_arc = [F3, F2, VORA_SUAU]
    if arcs:
        for i, (px_, py_) in enumerate(P):
            a, b = P[(i + 1) % 3], P[(i + 2) % 3]
            ga = math.degrees(math.atan2(-(a[1] - py_), a[0] - px_))
            gb = math.degrees(math.atan2(-(b[1] - py_), b[0] - px_))
            dd = (gb - ga) % 360
            g1, g2 = (ga, ga + dd) if dd <= 180 else (gb, gb + (360 - dd))
            _sector(d, px_, py_, 0.45, g1, g2, fons=fons_arc[i], gruix=1.2)
            tx, ty = _pt(px_, py_, 0.72, (g1 + g2) / 2)
            d.text(tx, ty + 0.13, str(i + 1), 0.36, 800)
    if marques:
        for i, k in enumerate(marques):
            (xa, ya), (xb, yb) = P[i], P[(i + 1) % 3]
            mx, my = (xa + xb) / 2, (ya + yb) / 2
            L = math.hypot(xb - xa, yb - ya)
            ux, uy = (xb - xa) / L, (yb - ya) / L
            for j in range(k):
                off = (j - (k - 1) / 2) * 0.14
                cx, cy = mx + ux * off, my + uy * off
                _linia(d, cx - uy * 0.2, cy + ux * 0.2, cx + uy * 0.2, cy - ux * 0.2, G1, 2.2)
    if cantonada_a is not None:
        px_, py_ = P[cantonada_a]
        _cantonada(d, px_, py_, 0.5)
    return d


def junts_d(angles, aria, r=1.6):
    """Els tres angles, un al costat de l'altre al mateix punt: fan un angle pla."""
    d = Dibuix(2 * r + 1.0, r + 0.7, aria)
    cx, cy = r + 0.5, r + 0.4
    _linia(d, 0.2, cy, 2 * r + 0.8, cy, G1, 2.4)
    fons = [F3, F2, VORA_SUAU]
    ini = 0
    for i, g in enumerate(angles):
        _sector(d, cx, cy, r, ini, ini + g, fons=fons[i], gruix=1.4)
        tx, ty = _pt(cx, cy, r * 0.62, ini + g / 2)
        d.text(tx, ty + 0.16, str(i + 1), 0.45, 800)
        ini += g
    _punt(d, cx, cy, 0.08)
    return d


def rellotge(hora, aria, r=1.35):
    """Un rellotge a una hora en punt: l'agulla llarga al 12 i la curta a l'hora."""
    d = Dibuix(2 * r + 0.3, 2 * r + 0.3, aria)
    cx = cy = r + 0.15
    d.cru(f'<circle cx="{d.px(cx)}" cy="{d.px(cy)}" r="{d.px(r)}" fill="#fff" stroke="{G1}" stroke-width="2.5"/>')
    for k in range(12):
        x1, y1 = _pt(cx, cy, r * 0.86, 90 - k * 30)
        x2, y2 = _pt(cx, cy, r * 0.97, 90 - k * 30)
        _linia(d, x1, y1, x2, y2, G2, 2 if k % 3 else 3)
    x, y = _pt(cx, cy, r * 0.78, 90)
    _linia(d, cx, cy, x, y, NEGRE, 3.5)
    x, y = _pt(cx, cy, r * 0.55, 90 - hora * 30)
    _linia(d, cx, cy, x, y, NEGRE, 5)
    _punt(d, cx, cy, 0.08)
    return d


def figura_quadrets(cel, m, aria, rotuls=False, fons=F3):
    """Una figura feta de quadrets (`cel` = [(fila, columna)]) sobre una quadrícula suau, amb la
    vora gruixuda: el perímetre són els costats de quadret d'aquesta vora. Amb `rotuls`, si és un
    rectangle, el nombre de costats de quadret de cada costat, per fora."""
    fs = [f for f, _ in cel]; cs = [c for _, c in cel]
    F, C = max(fs) + 1, max(cs) + 1
    marge = 0.75 if rotuls else 0.15
    d = Dibuix(C * m + 2 * marge, F * m + 2 * marge, aria)
    d.graella(marge, marge, F, C, m)
    conj = set(cel)
    for f, c in cel:
        d.cru(f'<rect x="{d.px(marge + c * m)}" y="{d.px(marge + f * m)}" width="{d.px(m)}" height="{d.px(m)}" '
              f'fill="{fons}" stroke="{G2}" stroke-width="1"/>')
    for f, c in cel:
        x, y = marge + c * m, marge + f * m
        for df, dc, x1, y1, x2, y2 in [(-1, 0, x, y, x + m, y), (1, 0, x, y + m, x + m, y + m),
                                       (0, -1, x, y, x, y + m), (0, 1, x + m, y, x + m, y + m)]:
            if (f + df, c + dc) not in conj:
                _linia(d, x1, y1, x2, y2, NEGRE, 4.5)
    if rotuls:
        d.text(marge + C * m / 2, marge - 0.2, str(C), 0.45, 800)
        d.text(marge + C * m / 2, marge + F * m + 0.55, str(C), 0.45, 800)
        d.text(marge - 0.35, marge + F * m / 2 + 0.16, str(F), 0.45, 800)
        d.text(marge + C * m + 0.35, marge + F * m / 2 + 0.16, str(F), 0.45, 800)
    return d


def rectangle_cel(f, c):
    return [(i, j) for i in range(f) for j in range(c)]


def cercle_d(r, aria, centre=True, radi=False, diametre=False, rot_radi=None, rot_diam=None, vora=False):
    """Una circumferència de radi r (cm): el centre, un radi (cap a dalt a la dreta) i un
    diàmetre (horitzontal), amb el nombre a sobre si es vol. Amb `vora`, la circumferència més
    gruixuda: és la vora que es mesura amb el cordill."""
    d = Dibuix(2 * r + 0.6, 2 * r + 0.6, aria)
    cx = cy = r + 0.3
    d.cru(f'<circle cx="{d.px(cx)}" cy="{d.px(cy)}" r="{d.px(r)}" fill="{F1}" stroke="{NEGRE if vora else G1}" '
          f'stroke-width="{5 if vora else 2.5}"/>')
    if diametre:
        _linia(d, cx - r, cy, cx + r, cy, NEGRE, 3)
        _punt(d, cx - r, cy, 0.07); _punt(d, cx + r, cy, 0.07)
        if rot_diam:
            d.text(cx, cy + min(0.5, r * 0.55), rot_diam, min(0.42, r * 0.34), 800)
    if radi:
        x, y = _pt(cx, cy, r, 50)
        _linia(d, cx, cy, x, y, NEGRE, 3)
        _punt(d, x, y, 0.07)
        if rot_radi:
            tx, ty = _pt(cx, cy, r * 0.55, 72)
            d.text(tx, ty, rot_radi, 0.42, 800)
    if centre:
        _punt(d, cx, cy, 0.1)
    return d


def patro_d(a, b, n, m, aria):
    """Una figura del patró a · n + b, com a la caixa (tasca 26): la part fixa (b quadrets, blancs
    i discontinus, en una columna a l'esquerra) i a files de n quadrets grisos. En paper no hi ha
    color: la part fixa es distingeix pel traç."""
    alt = max(a, b, 1)
    x_n = (m * 1.35 if b else 0)
    d = Dibuix(x_n + n * m + 0.2, alt * m + 0.2, aria)
    y0 = 0.1 + alt * m
    for i in range(b):
        d.quadret(0.1, y0 - (i + 1) * m, m, fons="#fff", traç=G1, gruix=1.8, discontinu=True)
    for f_ in range(a):
        for c in range(n):
            d.quadret(0.1 + x_n + c * m, y0 - (f_ + 1) * m, m)
    return d


def figures_d(a, b, fins, m, aria_patro):
    """Les figures 1 a `fins` d'un patró, de costat, amb el número a sota."""
    return "".join(f'''<div style="text-align:center"><div>{patro_d(a, b, n, m, f"{aria_patro}: la figura {n}, amb {a * n + b} quadrets").svg("")}</div>
        <p style="margin:.1rem 0 0;font-size:14pt;font-weight:800">{n}</p></div>''' for n in range(1, fins + 1))


def barres_d(dades, aria, m=0.42, ini=0, max_eix=None, buit=False, pintades=None, pas=2):
    """Un gràfic de barres de quadrets, com a la caixa (tasca 28): cada quadret és 1. `ini`: on
    comença l'eix (per a la regla trencada: un eix que no comença a zero). Amb `buit`, la quadrícula
    per pintar-hi les barres; `pintades` = quantes barres ja van pintades a mà (l'apartat resolt)."""
    top = max_eix or max(v for _, v in dades)
    files = top - ini
    esq, baix, amp_b = 1.0, 0.9, 1.9
    W = esq + len(dades) * amp_b + 0.3
    H = files * m + baix + 0.4
    d = Dibuix(W, H, aria)
    y0 = 0.3 + files * m
    for k in range(files + 1):
        v = ini + k
        y = y0 - k * m
        if (v - ini) % pas == 0 or k == files:
            d.cru(f'<line x1="{d.px(esq)}" y1="{d.px(y)}" x2="{d.px(W - 0.1)}" y2="{d.px(y)}" stroke="{G3}" stroke-width="0.9"/>')
            d.text(esq - 0.18, y + 0.12, str(v), 0.34, 400, ancora="end")
    _linia(d, esq, y0, esq, 0.2, G1, 2.2)
    _linia(d, esq, y0, W - 0.1, y0, G1, 2.2)
    for i, (et, v) in enumerate(dades):
        x = esq + i * amp_b + (amp_b - m) / 2
        n = v - ini
        if buit and not (pintades and i < pintades):
            d.graella(x, y0 - files * m, files, 1, m)
        else:
            for k in range(n):
                if buit:
                    d.pintat(x, y0 - (k + 1) * m, 1, 1, m)
                else:
                    d.quadret(x, y0 - (k + 1) * m, m)
        d.text(esq + i * amp_b + amp_b / 2, y0 + 0.5, et, 0.34, 700)
    return d
