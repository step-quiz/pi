#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud1-ordre.html: l'ordre de les operacions.

És la tercera fitxa de la unitat 1, i adapta l'activitat 1_14 del grup
(«Jerarquia»). Fa servir les peces de dibuix de la primera fitxa (genfitxa.py) i
els casos, els dibuixos i les frases de la tasca 4 de la caixa d'eines.
"""
import os
import sys

_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])       # Dibuix, ms, buit, buit_curt, ULL, colors…

PEU = "Unitat 1 · Ordre · pàgina"
pagines = []


def pagina(cos, classe="full"):
    n = len(pagines) + 1
    pagines.append(f'<div class="{classe}">\n{cos.rstrip()}\n  <div class="pag">{PEU} {n}</div>\n</div>')


qu = lambda n: f"{n} quadret" if n == 1 else f"{n} quadrets"
fi = lambda n: f"{n} fila" if n == 1 else f"{n} files"


def escriu(t, a, b, c):
    """L'expressió, com a la caixa: sm «a + b · c», ms «b · c + a»,
    pm «(a + b) · c», mp «c · (a + b)»."""
    return {"sm": f"{a} + {b} · {c}", "ms": f"{b} · {c} + {a}",
            "pm": f"({a} + {b}) · {c}", "mp": f"{c} · ({a} + {b})"}[t]


def passos(t, a, b, c):
    """Els dos passos: (rètol, operació) × 2, i el resultat."""
    if t == "sm":
        return [("Primer, la multiplicació", f"{b} · {c} = {b * c}"),
                ("Després, la suma", f"{a} + {b * c} = {a + b * c}")], a + b * c
    if t == "ms":
        return [("Primer, la multiplicació", f"{b} · {c} = {b * c}"),
                ("Després, la suma", f"{b * c} + {a} = {b * c + a}")], b * c + a
    if t == "pm":
        return [("Primer, el parèntesi", f"{a} + {b} = {a + b}"),
                ("Després, la multiplicació", f"{a + b} · {c} = {(a + b) * c}")], (a + b) * c
    return [("Primer, el parèntesi", f"{a} + {b} = {a + b}"),
            ("Després, la multiplicació", f"{c} · {a + b} = {c * (a + b)}")], c * (a + b)


def dibuix(t, a, b, c, m, aria, claus=False, peus=False):
    """El dibuix de l'expressió, com a la caixa. sm i ms: el rectangle de la
    multiplicació i els quadrets solts, al costat on són a l'expressió. pm: a + b
    files de c quadrets, amb aire entre les dues colles. mp: c files de a + b
    quadrets, amb aire entre les dues colles de columnes."""
    G = 0.22                       # l'aire entre les dues colles
    esq = 1.9 if claus else 0.1    # lloc per al rètol de l'esquerra
    dalt = 0.8 if claus else 0.1
    baix = 0.75 if peus else 0.1
    if t in ("sm", "ms"):
        forat = 2.1 if claus else 0.9
        w_s, w_r = a * m, c * m
        amp = 0.1 + w_s + forat + w_r + 0.3 if t == "sm" else esq + w_r + 0.9 + w_s + 0.3
        d = Dibuix(amp, dalt + b * m + baix, aria)
        if t == "sm":
            xs, xr = 0.1, 0.1 + w_s + forat
        else:
            xr, xs = esq, esq + w_r + 0.9
        ys = dalt + (b - 1) * m
        d.rectangle(xr, dalt, b, c, m)
        d.rectangle(xs, ys, 1, a, m, fons="#fff")
        if claus:
            d.clau_dalt(xr, xr + w_r, dalt - 0.25, qu(c))
            d.clau_esq(xr - 0.2, dalt, dalt + b * m, fi(b))
        if peus:
            d.text(xr + w_r / 2, dalt + b * m + 0.6, f"{b} · {c} = {b * c}", 0.45, 700)
            d.text(xs + w_s / 2, dalt + b * m + 0.6, qu(a), 0.45, 700)
        return d
    if t == "pm":
        s = a + b
        d = Dibuix(esq + c * m + 0.3, dalt + s * m + G + baix, aria)
        d.rectangle(esq, dalt, a, c, m)
        d.rectangle(esq, dalt + a * m + G, b, c, m)
        if claus:
            d.clau_dalt(esq, esq + c * m, dalt - 0.25, qu(c))
            d.clau_esq(esq - 0.2, dalt, dalt + a * m, fi(a))
            d.clau_esq(esq - 0.2, dalt + a * m + G, dalt + s * m + G, fi(b))
        return d
    s = a + b
    d = Dibuix(esq + s * m + G + 0.3, dalt + c * m + baix, aria)
    d.rectangle(esq, dalt, c, a, m)
    d.rectangle(esq + a * m + G, dalt, c, b, m)
    if claus:
        d.clau_dalt(esq, esq + s * m + G, dalt - 0.25, qu(s))
        d.clau_esq(esq - 0.2, dalt, dalt + c * m, fi(c))
    return d


def buit_op(cm=5.2):
    """Un buit per escriure-hi a mà una operació sencera: «3 · 4 = 12»."""
    return f'<u style="display:inline-block;min-width:{cm}cm;padding:0"></u>'


def amb_marge(d, marge):
    """Afegeix marge al voltant d'un dibuix ja fet, perquè hi càpiga un cercle fet a mà."""
    d.el = [f'<g transform="translate({d.px(marge)} {d.px(marge)})">'] + d.el + ["</g>"]
    d.amp += 2 * marge
    d.alt += 2 * marge
    return d


def linia_pas(et, contingut):
    return (f'<p class="frase" style="margin:0;font-size:15pt;line-height:1.9;white-space:nowrap">'
            f'<span style="font-size:14pt;color:var(--gris-2)">{et}:</span> {contingut}</p>')


def apartat_passos(lletra, t, a, b, c, resolt):
    ps, _ = passos(t, a, b, c)
    linies = "\n".join("      " + linia_pas(et, ms(op) if resolt else buit_op()) for et, op in ps)
    fons = (' class="resolt" style="border-radius:10px;padding:.3rem .6rem;margin-bottom:.35rem"' if resolt
            else ' style="padding:.3rem .6rem;margin-bottom:.35rem"')
    return f'''    <div{fons}>
      <p style="margin:0 0 .05rem;font-size:19pt;font-weight:800"><span class="apartat">{lletra})</span> {escriu(t, a, b, c)}</p>
{linies}
    </div>'''


# ===================================================================== pàgina 1
d = dibuix("sm", 2, 3, 4, 0.85, "3 files de 4 quadrets i, al costat, 2 quadrets solts", claus=True)
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs</b>. Fer un rectangle de 3 files de 4 i posar-hi 2 miniblocs solts al costat. Comptar-los tots.</div>
  <h1>L'ordre de les operacions</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div class="figura neta" style="margin-top:1rem">
{d.svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .8rem">Hi ha un rectangle i quadrets solts.</p>

  <table>
    <tr class="resolt"><td class="esq">Quants quadrets té el rectangle?</td><td style="width:4cm">{ms("12")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets solts hi ha?</td><td>{ms("2")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets hi ha en total?</td><td>{ms("14")}</td></tr>
  </table>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">Primer, la multiplicació: 3 · 4 = 12.</p>
    <p style="margin:0">Després, la suma: 2 + 12 = 14.</p>
    <p style="font-size:30pt;font-weight:800;margin:.3rem 0">2 + 3 · 4 = 14</p>
    <p style="margin:0;font-weight:700">Sense parèntesis, primer es multiplica.</p>
  </div>''')

# ===================================================================== pàgina 2
SENSE = [("a", "sm", 2, 3, 4, True), ("b", "sm", 1, 2, 5, False), ("c", "ms", 3, 5, 2, False),
         ("d", "sm", 3, 2, 3, False), ("e", "ms", 1, 2, 4, False)]
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Fes primer la multiplicació. Després fes la suma.</div></div>
    <div class="avis puntejat" style="margin:.3rem 0 .6rem">Sense parèntesis, primer es multiplica. Busca el punt.</div>
{chr(10).join(apartat_passos(*x) for x in SENSE)}
  </div>''')

# ===================================================================== pàgina 3
dm = dibuix("pm", 2, 3, 4, 0.55, "2 files de 4 quadrets i, sota, 3 files més de 4 quadrets: 5 files de 4", claus=True)
AMB = [("a", "pm", 1, 4, 2, True), ("b", "mp", 1, 2, 4, False), ("c", "pm", 3, 1, 2, False),
       ("d", "mp", 2, 2, 3, False)]
pagina(f'''  <h2>Amb parèntesi</h2>
  <div style="display:flex;gap:1cm;align-items:center;justify-content:center">
    <div style="flex:0 0 auto">
{dm.svg("      ")}
    </div>
    <div style="text-align:center;white-space:nowrap">
      <p style="margin:0">Primer, el parèntesi: 2 + 3 = 5.</p>
      <p style="margin:0">Després, la multiplicació: 5 · 4 = 20.</p>
      <p style="font-size:26pt;font-weight:800;margin:.25rem 0">(2 + 3) · 4 = 20</p>
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center;font-weight:700;margin:.5rem 0 .8rem">Amb parèntesis, primer es fa el parèntesi.</div>

  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Fes primer el parèntesi. Després fes la multiplicació.</div></div>
{chr(10).join(apartat_passos(*x) for x in AMB)}
  </div>''')

# ===================================================================== pàgina 4
def expr_marca(t, a, b, c, marca):
    """L'expressió amb els signes separats, per poder-los encerclar. Amb marca,
    el signe que es fa primer va encerclat a mà."""
    peca = lambda s, primer: (f'<span class="encerclat" style="padding:0 .45rem">{s}</span>' if marca and primer
                              else f'<span style="padding:0 .45rem">{s}</span>')
    mult_primer = t in ("sm", "ms")
    suma, mult = peca("+", not mult_primer), peca("·", mult_primer)
    if t == "sm":
        return f"{a} {suma} {b} {mult} {c}"
    if t == "ms":
        return f"{b} {mult} {c} {suma} {a}"
    if t == "pm":
        return f"({a} {suma} {b}) {mult} {c}"
    return f"{c} {mult} ({a} {suma} {b})"


BARREJA = [("a", "sm", 2, 3, 4, True), ("b", "pm", 2, 3, 4, False), ("c", "ms", 3, 5, 2, False),
           ("d", "mp", 1, 2, 4, False), ("e", "sm", 1, 2, 5, False), ("f", "pm", 1, 4, 2, False),
           ("g", "sm", 3, 2, 3, False), ("h", "mp", 2, 2, 3, False)]
caselles4 = []
for lletra, t, a, b, c, resolt in BARREJA:
    _, r = passos(t, a, b, c)
    final = ms(str(r)) if resolt else buit_curt()
    fons = ' class="resolt"' if resolt else ""
    caselles4.append(f'''      <div{fons} style="border-radius:10px;padding:.45rem .6rem">
        <p class="frase" style="margin:0;font-size:23pt;font-weight:800;white-space:nowrap;line-height:2.1"><span class="apartat" style="font-size:14pt">{lletra})</span> {expr_marca(t, a, b, c, resolt)} = {final}</p>
      </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Marca el signe de l'operació que es fa primer. Després escriu el resultat.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem .8cm;margin-top:.5rem">
{chr(10).join(caselles4)}
    </div>
  </div>

  <div class="clau" style="margin-top:1.2rem">
    <p style="margin:0">Sense parèntesis, primer es multiplica. Busca el punt.</p>
    <p style="margin:0">Amb parèntesis, primer es fa el parèntesi.</p>
  </div>''')

# ===================================================================== pàgina 5
def parella5(lletra, titol, t_bo, opcions, a, b, c, resolt, m=0.47):
    """Dos dibuixos per a la mateixa expressió: el bo i el que surt de fer-ho
    d'esquerra a dreta. Tots dos a la mateixa escala."""
    cols = []
    for t in opcions:
        _, r = passos(t, a, b, c)
        dd = amb_marge(dibuix(t, a, b, c, m, f"Un dibuix de {qu(r)}"), 0.45)
        if resolt and t == t_bo:
            dd.cercle_ma(dd.amp / 2, dd.alt / 2, dd.amp / 2 - 0.08, dd.alt / 2 - 0.05)
        compte = ms(str(r)) if resolt else buit_curt()
        cols.append(f'''        <div style="text-align:center">
{dd.svg("          ")}
          <p class="frase" style="margin:.15rem 0 0;font-size:15pt">Quadrets: {compte}</p>
        </div>''')
    fons = ' class="resolt" style="border-radius:10px;padding:.3rem .5rem"' if resolt else ""
    return f'''    <p style="margin:.7rem 0 .1rem;font-size:19pt;font-weight:800"><span class="apartat">{lletra})</span> {titol}</p>
    <div{fons}>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:.6cm;align-items:end">
{chr(10).join(cols)}
      </div>
    </div>'''


pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Marca el dibuix de cada operació. Compta els quadrets dels dos dibuixos.</div></div>
{parella5("a", "2 + 3 · 4", "sm", ["sm", "pm"], 2, 3, 4, True)}
{parella5("b", "(1 + 2) · 5", "pm", ["sm", "pm"], 1, 2, 5, False)}
{parella5("c", "1 + 2 · 5", "sm", ["pm", "sm"], 1, 2, 5, False)}
  </div>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">2 + 3 · 4 = 14. Primer es multiplica.</p>
    <p style="margin:.2rem 0 0">Per fer primer la suma cal un parèntesi: (2 + 3) · 4 = 20.</p>
  </div>''')

# ===================================================================== pàgina 6: la vida
def iogurt(d, x, y, w=0.5, h=0.68):
    d.cru(f'<path d="M{d.px(x)} {d.px(y)} H{d.px(x + w)} L{d.px(x + w - 0.06)} {d.px(y + h)} H{d.px(x + 0.06)} Z" '
          f'fill="#fff" stroke="{G1}" stroke-width="1.8" stroke-linejoin="round"/>')
    d.cru(f'<line x1="{d.px(x - 0.03)}" y1="{d.px(y + 0.1)}" x2="{d.px(x + w + 0.03)}" y2="{d.px(y + 0.1)}" '
          f'stroke="{G1}" stroke-width="2.2"/>')


def iogurts(paquets, solts, aria):
    w, g, gp = 0.5, 0.08, 0.35
    amp_p = 4 * w + 3 * g + 0.2
    amp = solts * (w + 0.15) + 0.9 + paquets * (amp_p + gp) + 0.2
    d = Dibuix(amp, 1.1, aria)
    x = 0.1
    for _ in range(solts):
        iogurt(d, x, 0.25)
        x += w + 0.15
    x += 0.75
    for _ in range(paquets):
        d.cru(f'<rect x="{d.px(x)}" y="{d.px(0.12)}" width="{d.px(amp_p)}" height="{d.px(0.9)}" rx="{d.px(0.1)}" '
              f'fill="{F2}" stroke="{G2}" stroke-width="1.4"/>')
        for k in range(4):
            iogurt(d, x + 0.1 + k * (w + g), 0.25)
        x += amp_p + gp
    return d


def ous(capses, solts, aria):
    r = 0.24
    amp_c = 3 * 0.62 + 0.25
    amp = solts * 0.62 + 0.9 + capses * (amp_c + 0.35) + 0.2
    d = Dibuix(amp, 1.55, aria)
    x = 0.1
    for _ in range(solts):
        d.cru(f'<ellipse cx="{d.px(x + 0.28)}" cy="{d.px(1.05)}" rx="{d.px(r)}" ry="{d.px(0.3)}" fill="#fff" '
              f'stroke="{G1}" stroke-width="1.8"/>')
        x += 0.62
    x += 0.7
    for _ in range(capses):
        d.cru(f'<rect x="{d.px(x)}" y="{d.px(0.1)}" width="{d.px(amp_c)}" height="{d.px(1.35)}" rx="{d.px(0.15)}" '
              f'fill="{F2}" stroke="{G2}" stroke-width="1.4"/>')
        for fi_ in range(2):
            for co in range(3):
                d.cru(f'<ellipse cx="{d.px(x + 0.43 + co * 0.62)}" cy="{d.px(0.45 + fi_ * 0.65)}" rx="{d.px(r)}" '
                      f'ry="{d.px(0.29)}" fill="#fff" stroke="{G1}" stroke-width="1.8"/>')
        x += amp_c + 0.35
    return d


def bosses(n, pomes, peres, aria):
    amp_b = (pomes + peres) * 0.62 + 0.3
    d = Dibuix(n * (amp_b + 0.45) + 0.2, 1.5, aria)
    x = 0.1
    for _ in range(n):
        d.cru(f'<path d="M{d.px(x)} {d.px(0.35)} H{d.px(x + amp_b)} L{d.px(x + amp_b - 0.15)} {d.px(1.4)} '
              f'H{d.px(x + 0.15)} Z" fill="{F2}" stroke="{G1}" stroke-width="1.8" stroke-linejoin="round"/>')
        d.cru(f'<path d="M{d.px(x + amp_b * 0.3)} {d.px(0.35)} Q{d.px(x + amp_b / 2)} {d.px(0.02)} '
              f'{d.px(x + amp_b * 0.7)} {d.px(0.35)}" fill="none" stroke="{G1}" stroke-width="1.8"/>')
        for k in range(pomes + peres):
            cx = x + 0.46 + k * 0.62
            if k < pomes:
                d.cru(f'<circle cx="{d.px(cx)}" cy="{d.px(0.92)}" r="{d.px(0.25)}" fill="#fff" stroke="{G1}" stroke-width="1.8"/>')
                d.cru(f'<line x1="{d.px(cx)}" y1="{d.px(0.67)}" x2="{d.px(cx + 0.06)}" y2="{d.px(0.55)}" stroke="{G1}" stroke-width="1.8"/>')
            else:
                d.cru(f'<path d="M{d.px(cx)} {d.px(0.58)} C{d.px(cx + 0.14)} {d.px(0.62)} {d.px(cx + 0.3)} {d.px(1.12)} '
                      f'{d.px(cx)} {d.px(1.2)} C{d.px(cx - 0.3)} {d.px(1.12)} {d.px(cx - 0.14)} {d.px(0.62)} {d.px(cx)} '
                      f'{d.px(0.58)} Z" fill="{G3}" stroke="{G1}" stroke-width="1.8"/>')
        x += amp_b + 0.45
    return d


pagina(f'''  <h2>A la vida de cada dia</h2>

  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Quants n'hi ha? Escriu l'operació.</div></div>
    <div class="resolt" style="border-radius:10px;padding:.4rem .6rem;margin-bottom:.4rem">
      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> 2 iogurts solts i 3 paquets de 4 iogurts.</p>
{iogurts(3, 2, "2 iogurts solts i 3 paquets de 4 iogurts").svg("      ")}
      <p class="frase" style="margin:.15rem 0 0">{ms("2 + 3 · 4 = 14 iogurts")}</p>
    </div>
    <div style="padding:.4rem .6rem">
      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> 3 ous solts i 2 capses de 6 ous.</p>
{ous(2, 3, "3 ous solts i 2 capses de 6 ous").svg("      ")}
      <p class="frase" style="margin:.15rem 0 0">L'operació: {buit_op(6)}</p>
      <p class="frase" style="margin:0">Hi ha {buit_curt()} ous.</p>
    </div>
  </div>

  <div class="exercici">
    <div class="tasca"><div class="n">6</div><div class="q">Quantes peces de fruita hi ha? Escriu l'operació.</div></div>
    <div class="duo">
      <div class="resolt" style="border-radius:10px;padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">a)</span> 2 bosses. A cada bossa hi ha 3 pomes i 1 pera.</p>
{bosses(2, 3, 1, "2 bosses amb 3 pomes i 1 pera a cada una").svg("        ")}
        <p class="frase" style="margin:.15rem 0 0">{ms("2 · (3 + 1) = 8 peces")}</p>
      </div>
      <div style="padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">b)</span> 3 bosses. A cada bossa hi ha 2 pomes i 2 peres.</p>
{bosses(3, 2, 2, "3 bosses amb 2 pomes i 2 peres a cada una").svg("        ")}
        <p class="frase" style="margin:.15rem 0 0">L'operació:</p>
        <p class="frase" style="margin:0">{buit_op(6.5)}</p>
        <p class="frase" style="margin:0">Hi ha {buit_curt()} peces.</p>
      </div>
    </div>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 1 · L'ordre de les operacions · full per al professorat</p>

  <div class="abans">
    <b>Abans de començar.</b> Es diu sempre igual, com a la caixa d'eines: «Primer, la
    multiplicació. Després, la suma.» Amb parèntesi: «Primer, el parèntesi.» La targeta de les
    taules és al davant tota l'estona, i totes les sumes es fan sense portar-ne. Demaneu que busqui
    el punt abans de fer res: trobar-lo és la meitat de la feina.
  </div>

  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs: fer 3 files de 4, posar-hi 2 miniblocs solts al costat i comptar-los
  tots: 14. Després, fer 5 files de 4, que és el que surt si primer se suma el 2 i el 3: 20. Són
  dues construccions diferents, i per això no donen el mateix.</p>

  <h3>1. Sense parèntesi</h3>
  <table>
    <tr><th></th><th>Primer, la multiplicació</th><th>Després, la suma</th></tr>
    <tr><td>b) 1 + 2 · 5</td><td>2 · 5 = 10</td><td>1 + 10 = 11</td></tr>
    <tr><td>c) 5 · 2 + 3</td><td>5 · 2 = 10</td><td>10 + 3 = 13</td></tr>
    <tr><td>d) 3 + 2 · 3</td><td>2 · 3 = 6</td><td>3 + 6 = 9</td></tr>
    <tr><td>e) 2 · 4 + 1</td><td>2 · 4 = 8</td><td>8 + 1 = 9</td></tr>
  </table>
  <p>A la c i a la e, la multiplicació ja és la primera d'esquerra a dreta: fer-ho en ordre de
  lectura també surt bé. A la b i a la d, no.</p>

  <h3>2. Amb parèntesi</h3>
  <table>
    <tr><th></th><th>Primer, el parèntesi</th><th>Després, la multiplicació</th></tr>
    <tr><td>b) 4 · (1 + 2)</td><td>1 + 2 = 3</td><td>4 · 3 = 12</td></tr>
    <tr><td>c) (3 + 1) · 2</td><td>3 + 1 = 4</td><td>4 · 2 = 8</td></tr>
    <tr><td>d) 3 · (2 + 2)</td><td>2 + 2 = 4</td><td>3 · 4 = 12</td></tr>
  </table>

  <h3>3. Què es fa primer?</h3>
  <p>b) la suma del parèntesi, 20; c) la multiplicació, 13; d) la suma del parèntesi, 12; e) la
  multiplicació, 11; f) la suma del parèntesi, 10; g) la multiplicació, 9; h) la suma del
  parèntesi, 12. Si marca bé el signe però s'equivoca en el resultat, el que falla és el càlcul:
  que miri la targeta.</p>
</div>''')

pagines.append('''<div class="full sol">
  <h3>4. Marca el dibuix de cada operació</h3>
  <p>b) (1 + 2) · 5: el dibuix de 3 files de 5, amb 15 quadrets. L'altre en té 11. c) 1 + 2 · 5:
  el dibuix de 2 files de 5 i 1 quadret solt, amb 11 quadrets. L'altre en té 15.</p>
  <p><b>Error típic:</b> fer-ho d'esquerra a dreta, com es llegeix:
  <span class="ratllat">2 + 3 · 4 = 20</span>. És la regla trencada d'aquesta fitxa. No
  l'expliqueu: feu comptar els quadrets dels dos dibuixos. El de 2 + 3 · 4 en té 14; el de 20 és
  un altre dibuix, el de (2 + 3) · 4. L'apartat b demana el dibuix del parèntesi a posta: si
  sempre marca el que té quadrets solts, encara no mira el parèntesi. <b>Compta per als nivells
  alts, no per al mínim.</b></p>

  <h3>5 i 6. A la vida de cada dia</h3>
  <p>5b) 3 + 2 · 6 = 15 ous. 6b) 3 · (2 + 2) = 12 peces. Es donen per bones les operacions escrites
  en un altre ordre si surt el mateix resultat: 2 · 6 + 3 = 15. El que compta és que la
  multiplicació surti del dibuix: les capses o les bosses.</p>

  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=4</b> (4.1 Mira l'ordre;
  4.2 Què es fa primer?). La 4.2 dona un codi de verificació, que es llegeix a la pàgina de llegir
  codis. L'exemple resolt de la fitxa és el mateix que el de la caixa, 2 + 3 · 4, i les
  operacions dels exercicis surten de la llista de la 4.2.</p>

  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (1.3, 2.1 i 8.1) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Davant de 2 + 3 · 4, busca el punt i diu en veu alta «primer, la multiplicació» (pàgina 1 i exercici 1).</li>
    <li>Fa pas a pas una operació amb una suma i una multiplicació, sense parèntesi (exercici 1).</li>
    <li>Fa primer el parèntesi (exercici 2).</li>
    <li>Marca quina operació es fa primer, amb parèntesi i sense (exercici 3).</li>
    <li>Escriu l'operació d'una situació de la vida, amb la multiplicació que surt del dibuix (exercicis 5 i 6).</li>
    <li>Nivells alts: tria el dibuix bo entre el de 2 + 3 · 4 i el de (2 + 3) · 4 (exercici 4).</li>
  </ul>
</div>''')

# ===================================================================== el document
cap = '''<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Unitat 1 · L'ordre de les operacions</title>
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
</head>
<body>
<!--
  FITXA · Unitat 1 · Nombres naturals · L'ordre de les operacions
  La tercera fitxa de la unitat. Adapta l'activitat 1_14 del grup
  («Jerarquia»): sumes i multiplicacions, amb parèntesi i sense. Les
  potències, les restes i les divisions de l'activitat del grup queden fora.

  Els casos, els dibuixos i les frases són els de la tasca 4 de la caixa
  d'eines (regla 8): 2 + 3 · 4 és l'exemple de la 4.1, i les operacions dels
  exercicis surten de la llista de la 4.2. Totes les sumes es fan sense
  portar-ne, i totes les multiplicacions són de la targeta.

  La regla trencada és fer-ho d'esquerra a dreta: 2 + 3 · 4 = 20. Es desmunta
  amb el dibuix (exercici 4) i la pàgina acaba amb la forma bona a la vista.

  Cada bloc .full acaba amb un </div> a principi de línia; els de dins van
  sagnats. Les regles són a docs/CRITERIS-DISSENY.md. Després de canviar
  res: eines/mesura.py, generadors/gen_pdf.py i eines/comprova.py.
-->

'''
html = cap + "\n\n".join(pagines) + "\n\n</body>\n</html>\n"
sortida = sys.argv[1] if len(sys.argv) > 1 else "ud1-ordre.html"
open(sortida, "w", encoding="utf-8").write(html)
print(sortida, len(pagines), "blocs")
