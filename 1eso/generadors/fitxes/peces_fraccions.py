"""Peces comunes dels generadors de les fitxes de la unitat 3 (les fraccions).

S'hi entra amb exec(), després de genfitxa.py i ud2comu.py: fa servir Dibuix, ms, buit,
buit_curt, ULL, els colors, tria, fes_pagina i document.
"""
NUMS = ["zero", "un", "dos", "tres", "quatre", "cinc", "sis", "set", "vuit", "nou", "deu", "onze", "dotze"]
SING = {2: "mig", 3: "terç", 4: "quart", 5: "cinquè", 6: "sisè", 7: "setè", 8: "vuitè", 9: "novè", 10: "desè",
        11: "onzè", 12: "dotzè"}
PLUR = {2: "mitjos", 3: "terços", 4: "quarts", 5: "cinquens", 6: "sisens", 7: "setens", 8: "vuitens", 9: "novens",
        10: "desens", 11: "onzens", 12: "dotzens"}
nom = lambda n, d: NUMS[n] + " " + (SING[d] if n == 1 else PLUR[d])


def fr(n, d, mida="17pt", ma=False):
    """La fracció escrita com a fracció. La marca .fr és la que llegeix eines/comprova.py.
    Amb `ma`, escrita a mà (l'apartat resolt)."""
    lletra = "font-family:'Caveat',cursive;font-weight:700;color:var(--manuscrit);" if ma else "font-weight:800;"
    if ma:   # la lletra manuscrita, un 40% més gran, com la resta de l'escrit a mà (regla 4)
        mida = f"{float(mida[:-2]) * 1.4:.0f}pt"
    return (f'<span class="fr" style="display:inline-block;vertical-align:middle;text-align:center;line-height:1.05;'
            f'{lletra}margin:0 .1em;font-size:{mida}">'
            f'<span style="display:block;border-bottom:.09em solid;padding:0 .18em .04em">{n}</span>'
            f'<span style="display:block;padding:.04em .18em 0">{d}</span></span>')


def fr_buit(mida="17pt"):
    """Una fracció per omplir: dues caixes, una damunt de l'altra, amb la ratlla al mig."""
    c = "display:block;min-width:1.1cm;height:1.05cm"
    return (f'<span style="display:inline-block;vertical-align:middle;text-align:center;margin:0 .1em;font-size:{mida}">'
            f'<span style="{c};border:1.5px dashed var(--gris-2);border-bottom:2.5px solid var(--tinta);border-radius:6px 6px 0 0"></span>'
            f'<span style="{c};border:1.5px dashed var(--gris-2);border-top:0;border-radius:0 0 6px 6px"></span></span>')


def tira(n, d, aria, W=8.0, H=0.9, mes=0, treu=0, k=1, ma=False, buida=False, meitat=False):
    """El rectangle de les fraccions, com a la caixa. Els `n` primers pintats (impresos, o a
    mà amb `ma`); els `mes` següents en gris més fosc (el segon sumand); els `treu` darrers
    pintats, ratllats (el que es resta); amb `k` > 1, cada tros partit en k (discontinu).
    Amb `buida`, tots blancs, per pintar. Si no hi caben, en posa més d'un."""
    unitats = max(1, -(-(n + mes) // d))
    aire = 0.3
    D = Dibuix(W + 0.2, unitats * (H + aire) - aire + 0.2, aria)
    w = W / d
    resta, m = n, mes
    for u in range(unitats):
        y = 0.1 + u * (H + aire)
        p = min(d, resta); resta -= p
        q = min(d - p, m); m -= q
        for i in range(d):
            if buida or i >= p + q:
                fons, traç, g = "#fff", G2, 1.2
            elif i < p:
                fons, traç, g = (VORA_SUAU, MS, 1.8) if ma else (F3, G2, 1.2)
            else:
                fons, traç, g = G3, G2, 1.2
            D.cru(f'<rect x="{D.px(0.1 + i * w)}" y="{D.px(y)}" width="{D.px(w)}" height="{D.px(H)}" fill="{fons}" '
                  f'stroke="{traç}" stroke-width="{g}"/>')
            if treu and u == unitats - 1 and p - treu <= i < p:
                D.cru(f'<line x1="{D.px(0.1 + i * w + 0.12)}" y1="{D.px(y + H - 0.12)}" x2="{D.px(0.1 + (i + 1) * w - 0.12)}" '
                      f'y2="{D.px(y + 0.12)}" stroke="{MS}" stroke-width="2.4" stroke-linecap="round"/>')
        if k > 1:
            for j in range(1, d * k):
                if j % k:
                    x = 0.1 + j * w / k
                    D.cru(f'<line x1="{D.px(x)}" y1="{D.px(y + 0.08)}" x2="{D.px(x)}" y2="{D.px(y + H - 0.08)}" '
                          f'stroke="{G2}" stroke-width="1" stroke-dasharray="4 3"/>')
        D.cru(f'<rect x="{D.px(0.1)}" y="{D.px(y)}" width="{D.px(W)}" height="{D.px(H)}" fill="none" stroke="{G1}" stroke-width="2.4"/>')
        if meitat:   # la meitat del rectangle, per comparar-hi (el full de 1/2 + 1/4)
            D.cru(f'<line x1="{D.px(0.1 + W / 2)}" y1="{D.px(max(0.02, y - 0.08))}" x2="{D.px(0.1 + W / 2)}" '
                  f'y2="{D.px(y + H + 0.08)}" stroke="{NEGRE}" stroke-width="2.6" stroke-dasharray="6 4"/>')
    return D


def tira_talls(talls, pintat, aria, W=8.0, H=0.9):
    """Un rectangle partit pels punts `talls` (entre 0 i 1): trossos que poden ser desiguals.
    El tros número `pintat` va pintat. Per a la regla trencada de la fitxa 1."""
    D = Dibuix(W + 0.2, H + 0.2, aria)
    punts = [0] + list(talls) + [1]
    for i in range(len(punts) - 1):
        x0, x1 = punts[i] * W, punts[i + 1] * W
        D.cru(f'<rect x="{D.px(0.1 + x0)}" y="{D.px(0.1)}" width="{D.px(x1 - x0)}" height="{D.px(H)}" '
              f'fill="{F3 if i == pintat else "#fff"}" stroke="{G2}" stroke-width="1.2"/>')
    D.cru(f'<rect x="{D.px(0.1)}" y="{D.px(0.1)}" width="{D.px(W)}" height="{D.px(H)}" fill="none" stroke="{G1}" stroke-width="2.4"/>')
    return D


def caixa(cos, resolt=False, marge=".45rem"):
    fons = ' class="resolt"' if resolt else ""
    return f'''    <div{fons} style="border-radius:10px;padding:.35rem .6rem;margin-bottom:{marge}">
{cos}
    </div>'''
