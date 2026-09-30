"""Peces comunes dels generadors de les fitxes de la unitat 2.

S'hi entra amb exec(), després de les peces de la unitat 1 (genfitxa.py): fa servir
Dibuix, ms, buit, buit_curt, ULL i els colors d'allà.
"""

MARCA = ('<svg viewBox="0 0 24 24" style="position:absolute;left:-3px;top:-6px;width:26px;height:26px">'
         '<path d="M4 13l5 6L21 3" fill="none" stroke="#3A3A3A" stroke-width="3.5" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def fes_pagina(pagines, peu):
    def pagina(cos, classe="full"):
        n = len(pagines) + 1
        pagines.append(f'<div class="{classe}">\n{cos.rstrip()}\n  <div class="pag">{peu} {n}</div>\n</div>')
    return pagina


def tria(opcions, bona=None, revisa=False, mida="15pt", columna=False, ample="3.4cm", ajusta=False):
    """Opcions per marcar, senceres i sense partir-se. Amb `revisa`, cada opció va dins
    de .revisa: poden ser igualtats falses a posta, i comprova.py no les comprova.
    Amb `ajusta`, en fila, cada capsa mesura com a mínim el seu text (flex:1 1 auto): per a
    opcions de llargades molt diferents («Circumferència»). Sense, totes fan el mateix, i
    un text més llarg que `ample` sortia de la capsa al PDF (29/9/2026). No és el valor per
    defecte perquè, dins d'una altra fila flexible, el motor dels PDF parteix les opcions en
    dues files encara que hi càpiguen: cal mirar-ho pàgina per pàgina."""
    peces = []
    for o in opcions:
        text = f'<span class="revisa">{o}</span>' if revisa else o
        estil = ("flex:1 1 auto;" if ajusta else "") + f"min-width:{ample};white-space:nowrap;font-size:{mida}"
        if o == bona:
            peces.append(f'<label style="{estil};border-width:3px;border-color:var(--tinta)"><span class="quadret">{MARCA}</span>{text}</label>')
        else:
            peces.append(f'<label style="{estil}"><span class="quadret"></span>{text}</label>')
    if columna:
        # Una fila per opció. Amb flex-direction:column, WeasyPrint (el motor dels PDF) estirava
        # les opcions i les encavalcava, encara que Chromium les ensenyés bé: va passar als PDF
        # d'ud2-repartir i d'ud3-sumes (trobat el 29/9/2026). Cada opció, dins del seu .tria.
        # El .tria és una taula: `ample` és l'amplada mínima i, si el text és més llarg, la
        # capsa creix amb el text. Amb `width`, «Obtusangle» o «Perpendiculars» sortien de la
        # capsa al PDF (29/9/2026).
        return (f'<div style="margin:.25rem 0">' +
                "".join(f'<div class="tria" style="margin:0 0 .35rem;display:table;width:{ample}">{p}</div>' for p in peces) +
                "</div>")
    return f'<div class="tria" style="margin:.25rem 0;flex-wrap:wrap">' + "".join(peces) + "</div>"


def graella100(estil, aria, m=1.0):
    """La graella de 100, amb la lletra a la mida del quadret (14 pt amb 1 cm).
    estil(n) → None, "imprès" (gris d'impremta), "a_ma" (pintat a mà), "ratllat_ma"
    (ratllat a mà) o "encerclat_ma" (encerclat a mà)."""
    d = Dibuix(10 * m + 0.2, 10 * m + 0.2, aria)
    for n in range(1, 101):
        f, c = (n - 1) // 10, (n - 1) % 10
        x, y = 0.1 + c * m, 0.1 + f * m
        e = estil(n) if estil else None
        fons = {"imprès": F3, "a_ma": VORA_SUAU}.get(e, "#fff")
        d.cru(f'<rect x="{d.px(x)}" y="{d.px(y)}" width="{d.px(m)}" height="{d.px(m)}" fill="{fons}" '
              f'stroke="{MS if e == "a_ma" else G2}" stroke-width="{2 if e in ("imprès", "a_ma") else 1.1}"/>')
        mida = min(0.47, m * 0.46) * (0.85 if n == 100 else 1)
        d.text(x + m / 2, y + m / 2 + mida * 0.36, str(n), mida, 800 if e in ("imprès", "a_ma", "encerclat_ma") else 400)
        if e == "ratllat_ma":
            d.cru(f'<line x1="{d.px(x + 0.12 * m)}" y1="{d.px(y + 0.88 * m)}" x2="{d.px(x + 0.88 * m)}" y2="{d.px(y + 0.12 * m)}" '
                  f'stroke="{MS}" stroke-width="2.2" stroke-linecap="round"/>')
        if e == "encerclat_ma":
            d.cercle_ma(x + m / 2, y + m / 2, m * 0.46, m * 0.42)
    return d


def rectangles_de(n):
    return [(a, n // a) for a in range(1, int(n ** 0.5) + 1) if n % a == 0]


def divisors_de(n):
    return sorted({x for a, b in rectangles_de(n) for x in (a, b)})


def dibuix_rectangles(n, m, aria, rotuls=True):
    """Tots els rectangles de n, un sota l'altre i a la mateixa escala, com a la
    tasca 7.1 de la caixa, amb el rètol «2 · 6» a l'esquerra."""
    rs = rectangles_de(n)
    esq = 1.9 if rotuls else 0.1
    alt = sum(a * m for a, _ in rs) + 0.35 * (len(rs) - 1) + 0.2
    d = Dibuix(esq + n * m + 0.2, alt, aria)
    y = 0.1
    for a, b in rs:
        if rotuls:
            d.text(esq - 0.3, y + a * m / 2 + 0.15, f"{a} · {b}", 0.42, 800, ancora="end")
        d.rectangle(esq, y, a, b, m)
        y += a * m + 0.35
    return d


def arbre(n, parts, aria, buit_=False, m=1.0):
    """L'arbre de factors d'un nombre de tres factors primers com a molt, amb el conveni
    de la fitxa: a cada partició, el primer a l'esquerra i el que es torna a partir a la
    dreta. `parts` = [(a, b), (c, d)]: n = a · b i b = c · d. Amb `buit_`, només l'arrel
    i els cercles buits (per omplir). Els primers de la punta, amb un segon cercle."""
    r = 0.52 * m
    W, H = 6.4 * m, 4.6 * m
    d = Dibuix(W, H, aria)
    nodes = [(W / 2, r + 0.1, n, False)]
    (a, b) = parts[0]
    x1, y1 = W / 2 - 1.3 * m, r + 0.1 + 1.7 * m
    x2, y2 = W / 2 + 1.3 * m, y1
    nodes += [(x1, y1, a, True), (x2, y2, b, len(parts) == 1)]
    arestes = [(0, 1), (0, 2)]
    if len(parts) > 1:
        (c, e) = parts[1]
        y3 = y2 + 1.7 * m
        nodes += [(x2 - 1.1 * m, y3, c, True), (x2 + 1.1 * m, y3, e, True)]
        arestes += [(2, 3), (2, 4)]
    for i, j in arestes:
        xa, ya, *_ = nodes[i]; xb, yb, *_ = nodes[j]
        d.cru(f'<line x1="{d.px(xa)}" y1="{d.px(ya + r)}" x2="{d.px(xb)}" y2="{d.px(yb - r)}" stroke="{G1}" stroke-width="2"/>')
    for k, (x, y, v, primer) in enumerate(nodes):
        d.cru(f'<circle cx="{d.px(x)}" cy="{d.px(y)}" r="{d.px(r)}" fill="#fff" stroke="{G1}" stroke-width="2"/>')
        if buit_ and k > 0:
            continue
        if primer:
            d.cru(f'<circle cx="{d.px(x)}" cy="{d.px(y)}" r="{d.px(r - 0.1)}" fill="none" stroke="{G1}" stroke-width="1.2"/>')
        d.text(x, y + 0.2, str(v), 0.55, 800)
    return d


def document(titol, comentari, pagines, sortida):
    cap = f'''<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titol}</title>
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
</head>
<body>
<!--
{comentari.rstrip()}

  Cada bloc .full acaba amb un </div> a principi de línia; els de dins van
  sagnats. Les regles són a docs/CRITERIS-DISSENY.md. Després de canviar
  res: eines/mesura.py, generadors/gen_pdf.py i eines/comprova.py.
-->

'''
    html = cap + "\n\n".join(pagines) + "\n\n</body>\n</html>\n"
    open(sortida, "w", encoding="utf-8").write(html)
    print(sortida, len(pagines), "blocs")
