#!/usr/bin/env python3
"""Fa el quadern d'activitats de cada unitat: quadern/udN.html.

    python3 generadors/gen_quadern.py          (des de 4eso/)
    python3 generadors/gen_quadern.py 3        (només la UD3)

El quadern és per practicar DESPRÉS de la fitxa. Està fet de blocs, un per cada
exercici de la fitxa, i cada bloc té activitats «germanes» (el mateix tipus
d'exercici amb altres números i altres contextos) i activitats de repte (una mica
diferents: el camí al revés, un pas més, una decisió nova).

Cada activitat porta dues marques, i el filtre de la pàgina (js/quadern.js) les llegeix:

    data-n="1|2|3"   a partir de quina quantitat surt: 1 petit, 2 mitjà, 3 elevat.
                     Les germanes de cada bloc van 1, 2, 3, 3: petit en dona una per
                     exercici de la fitxa, mitjà dues i elevat quatre.
    data-repte       només si és de repte. Surt si el docent tria «Amb repte», i
                     també segons la quantitat (data-n).

El solucionari porta les mateixes marques en el mateix ordre: el filtre amaga les
mateixes entrades, i els números (comptadors CSS, que se salten el que està amagat)
coincideixen sempre amb els de les pàgines de l'alumnat.

El contingut de cada unitat és a generadors/quadern/udN.py. Aquest fitxer és el motor:
les peces (taula, tria, ofertes, dibuixos) i la pàgina. Les peces fan servir les
classes de css/fitxa.css, perquè el quadern es llegeixi com la fitxa: la mateixa
cadena, les mateixes taules, el primer apartat resolt en lletra manuscrita.

Els quaderns no s'editen a mà. eines/comprova.py torna a fer cada quadern i avisa si
el fitxer de quadern/ no és el que surt del generador.
"""
import glob, importlib.util, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ARREL = os.path.dirname(AQUI)
DADES = os.path.join(AQUI, "quadern")
SORTIDA = os.path.join(ARREL, "quadern")

NEG, GRIS, MANUS, CLAR, FONS, FONS2, VORA = "#000", "#5E5E5E", "#3A3A3A", "#BFBFBF", "#F2F2F2", "#E4E4E4", "#8A8A8A"
TIP = 'font-family="system-ui"'


# ------------------------------------------------------------------ números --

def num(x):
    """Un nombre en català: coma decimal i espai als milers (1 400, 25 000)."""
    x = round(x, 6)
    if x == int(x):
        s = f"{int(x):,}".replace(",", " ")
    else:
        enter, dec = f"{x:.6f}".rstrip("0").split(".")
        s = f"{int(enter):,}".replace(",", " ") + "," + dec
    return s


def eur(x):
    """Un preu: sempre dos decimals, «0,90 €»."""
    return f"{x:.2f}".replace(".", ",") + " €"


def esc(e):
    return "1 : " + num(e)


def ms(t):
    return f'<span class="ms">{t}</span>'


LLETRES = "abcdefgh"
BUIT = '<span class="buit"></span>'
MARCA = ('<svg viewBox="0 0 24 24" style="position:absolute;left:-3px;top:-6px;width:26px;height:26px">'
         f'<path d="M4 13l5 6L21 3" fill="none" stroke="{MANUS}" stroke-width="3.5" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')
ICONES = {"calc": "#i-calc", "regle": "#i-regle", "llapis": "#i-llapis"}


# ------------------------------------------------------------------- peces --
# Cada peça torna (html de l'alumnat, html del solucionari).

def tasca(q, ico=None):
    icona = f'\n        <svg class="ico" style="margin-left:.4rem"><use href="{ICONES[ico]}"/></svg>' if ico else ""
    return (f'    <div class="tasca"><div class="n"></div>ESTRELLA\n'
            f'      <div class="q">{q}{icona}</div></div>\n')


def nota(t):
    return f'    <p class="nota-act">{t}</p>\n' if t else ""


def taula(q, cap, files, omplir, ico=None, abans="", despres="", amples=None, esq=(), sol_nota=""):
    """Una taula com les de la fitxa. La primera fila va resolta en lletra manuscrita;
    a les altres, les columnes d'`omplir` surten buides i la resta, com a dada.
    `esq`: columnes alineades a l'esquerra (les que porten una frase)."""
    n = len(cap)
    amples = amples or [round(88 / n)] * n
    th = '<th style="width:10%"></th>' + "".join(
        f'<th style="width:{a}%">{c}</th>' for a, c in zip(amples, cap))
    o = [tasca(q, ico), abans, f'    <table>\n      <tr>{th}</tr>\n']
    for i, fila in enumerate(files):
        assert len(fila) == n, (q, fila)
        lletra = LLETRES[i]
        if i == 0:
            cel = "".join(f'<td class="ms{" esq" if j in esq else ""}">{v}</td>' for j, v in enumerate(fila))
            o.append(f'      <tr class="resolt"><td class="ms">{lletra})</td>{cel}</tr>\n')
        else:
            cel = "".join('<td class="omplir"></td>' if j in omplir
                          else f'<td class="dada{" esq" if j in esq else ""}">{v}</td>'
                          for j, v in enumerate(fila))
            o.append(f'      <tr><td><b>{lletra})</b></td>{cel}</tr>\n')
    o.append("    </table>\n")
    o.append(despres)
    sol = ["<table><tr><th></th>" + "".join(f"<th>{c}</th>" for c in cap) + "</tr>"]
    for i, fila in enumerate(files):
        sol.append(f"<tr><td>{LLETRES[i]})</td>" + "".join(
            f"<td><b>{v}</b></td>" if j in omplir else f"<td>{v}</td>" for j, v in enumerate(fila)) + "</tr>")
    sol.append("</table>")
    if sol_nota:
        sol.append(f"<p>{sol_nota}</p>")
    return "".join(o), "".join(sol)


def tria(q, apartats, ico=None, abans="", compacta=False, sol_nota=""):
    """Apartats de marcar una opció. `apartats`: (text o html, [opcions], la bona).
    El primer ja va marcat."""
    o = [tasca(q, ico), abans]
    sol = []
    for i, (text, opcions, bona) in enumerate(apartats):
        marge = ".6rem" if i == 0 else "1.1rem"
        o.append(f'    <div style="margin-top:{marge}"><span class="apartat">{LLETRES[i]})</span> {text}</div>\n')
        o.append(f'    <div class="tria{" compacta" if compacta else ""}">\n')
        for k, op in enumerate(opcions):
            if i == 0 and k == bona:
                o.append(f'      <label style="border-width:3px;border-color:var(--tinta)"><span class="quadret">'
                         f'{MARCA}</span>{op}</label>\n')
            else:
                o.append(f'      <label><span class="quadret"></span>{op}</label>\n')
        o.append("    </div>\n")
        sol.append(f"{LLETRES[i]}) <b>{opcions[bona]}</b>")
    s = "<p>" + " &nbsp;·&nbsp; ".join(sol) + "</p>"
    if sol_nota:
        s += f"<p>{sol_nota}</p>"
    return "".join(o), s


def ofertes(q, apartats, ico="calc", abans="", sol_nota=""):
    """Comparar ofertes amb el preu d'1, com l'exercici 6 de la U3.
    `apartats`: (producte, [opció…], la bona). Cada opció és un dict:
        nom    el que es marca («El pack»)
        diu    l'oferta tal com es llegeix
        compte el compte que porta al preu d'1 («5,10 ÷ 6»), sense el resultat
        val    el preu d'1 («0,85 € el litre»)
        buit   (opcional) el que surt a sota quan no està resolt; per defecte, «compte =»
    El primer apartat ja va resolt."""
    o = [tasca(q, ico), abans]
    files = []
    for i, (producte, ops, bona) in enumerate(apartats):
        marge = ".7rem" if i == 0 else "1rem"
        tres = " tres" if len(ops) > 2 else ""
        o.append(f'    <div style="margin-top:{marge}"><span class="apartat">{LLETRES[i]})</span> {producte}</div>\n')
        o.append(f'    <div class="parella-op{tres}">\n')
        for op in ops:
            if i == 0:
                peu = ms((op["compte"] + " = " if op["compte"] else "") + f'<b>{op["val"]}</b>')
                o.append(f'      <div class="oferta resolt">{op["diu"]}<br>\n        {peu}</div>\n')
            else:
                peu = op.get("buit", f'<b>{op["compte"]} =</b>' if op["compte"] else "")
                o.append(f'      <div class="oferta">{op["diu"]}' + (f"<br>{peu}" if peu else "") + "</div>\n")
        o.append("    </div>\n")
        o.append(f'    <div class="tria{" compacta" if tres else ""}">\n')
        for k, op in enumerate(ops):
            if i == 0 and k == bona:
                o.append(f'      <label style="border-width:3px;border-color:var(--tinta)"><span class="quadret">'
                         f'{MARCA}</span>{op["nom"]}</label>\n')
            else:
                o.append(f'      <label><span class="quadret"></span>{op["nom"]}</label>\n')
        o.append("    </div>\n")
        comptes = " · ".join((f'{op["compte"]} = ' if op["compte"] else "") + op["val"] for op in ops)
        files.append(f"<tr><td>{LLETRES[i]})</td><td>{producte.rstrip('.')}</td><td>{comptes}</td>"
                     f"<td><b>{ops[bona]['nom']}</b></td></tr>")
    sol = ("<table><tr><th></th><th>Producte</th><th>El preu d'1</th><th>Guanya</th></tr>"
           + "".join(files) + "</table>")
    if sol_nota:
        sol += f"<p>{sol_nota}</p>"
    return "".join(o), sol


def taula_fila(cap, valors, buits=(), resolts=()):
    """Una taula horitzontal de dues files (magnitud i valors), per a directa i inversa.
    `buits`: posicions que s'han d'omplir; `resolts`: posicions escrites a mà."""
    o = ['    <table class="mini fila">\n']
    for r, (nom, fila) in enumerate(zip(cap, valors)):
        cel = []
        for k, v in enumerate(fila):
            if r == 1 and k in buits:
                cel.append('<td class="omplir"></td>')
            elif r == 1 and k in resolts:
                cel.append(f'<td class="ms">{v}</td>')
            else:
                cel.append(f"<td>{v}</td>")
        o.append(f'      <tr><th>{nom}</th>{"".join(cel)}</tr>\n')
    o.append("    </table>\n")
    return "".join(o)


# ----------------------------------------------------------------- dibuixos --

def planol(espais, zoom=1, mides=True, aria="Plànol"):
    """Un plànol fet de rectangles. Les mesures dels espais són en cm del plànol.
    1 unitat de l'SVG = 1 mm de paper: amb zoom 1 el dibuix és de mida real (si
    s'imprimeix al 100 %); amb zoom 2, el doble de gran perquè hi càpiguen els noms.
    Cada espai: (nom, x, y, ample, alt) o (nom, x, y, ample, alt, "moble")."""
    m = 4
    W = max(e[1] + e[3] for e in espais) * 10 * zoom + 2 * m
    H = max(e[2] + e[4] for e in espais) * 10 * zoom + 2 * m
    rects, textos = [], []
    for e in espais:
        nom, x, y, w, h = e[:5]
        moble = len(e) > 5
        X, Y, Wr, Hr = m + x * 10 * zoom, m + y * 10 * zoom, w * 10 * zoom, h * 10 * zoom
        fons = FONS2 if moble else FONS
        gruix = 0.8 if moble else 1
        rects.append(f'<rect x="{X:g}" y="{Y:g}" width="{Wr:g}" height="{Hr:g}" fill="{fons}" '
                     f'stroke="{NEG}" stroke-width="{gruix}"/>')
        cx, cy = X + Wr / 2, Y + Hr / 2
        if mides and not moble:
            textos.append(f'<text x="{cx:g}" y="{cy - 0.6:g}">{nom}</text>'
                          f'<text x="{cx:g}" y="{cy + 5.4:g}" font-size="4.3" fill="{GRIS}">'
                          f'{num(w)} × {num(h)} cm</text>')
        else:
            textos.append(f'<text x="{cx:g}" y="{cy + 1.6:g}">{nom}</text>')
    return (f'    <svg class="planol" style="width:{W / 10:g}cm" viewBox="0 0 {W:g} {H:g}" role="img" '
            f'aria-label="{aria}">\n      <g>{"".join(rects)}</g>\n'
            f'      <g {TIP} font-size="4.6" fill="{NEG}" text-anchor="middle">{"".join(textos)}</g>\n'
            f'    </svg>\n')


def doble_recta(cm, per_cm, unitat="m", dalt="al mapa (cm)", baix=None, w=560, h=124):
    """La doble recta de la fitxa (gen_grafics5.doble_mapa), amb l'escala que calgui:
    a dalt els cm del mapa, a baix el que valen de veritat. El primer tram, ombrejat."""
    baix = baix or f"de veritat ({unitat})"
    x0, x1, yd, yb = 178, 542, 46, 96
    def px(k): return x0 + k / cm * (x1 - x0)
    o = [f'<rect x="{px(0):.1f}" y="{yd}" width="{px(1) - px(0):.1f}" height="{yb - yd}" fill="{FONS}"/>',
         f'<text x="{x0 - 14}" y="{yd + 6}" text-anchor="end" font-size="20" fill="{GRIS}" {TIP}>{dalt}</text>',
         f'<text x="{x0 - 14}" y="{yb + 6}" text-anchor="end" font-size="20" fill="{GRIS}" {TIP}>{baix}</text>']
    for k in range(cm + 1):
        o.append(f'<line x1="{px(k):.1f}" y1="{yd}" x2="{px(k):.1f}" y2="{yb}" stroke="#D4D4D4" stroke-width="1"/>')
    for y, valors in ((yd, [num(k) for k in range(cm + 1)]), (yb, [num(k * per_cm) for k in range(cm + 1)])):
        o.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{NEG}" stroke-width="2.5"/>')
        for k, et in enumerate(valors):
            dy = -14 if y == yd else 26
            o.append(f'<line x1="{px(k):.1f}" y1="{y - 7}" x2="{px(k):.1f}" y2="{y + 7}" stroke="{NEG}" stroke-width="2"/>')
            o.append(f'<text x="{px(k):.1f}" y="{y + dy}" text-anchor="middle" font-size="20" fill="{NEG}" {TIP}>{et}</text>')
    return (f'    <div class="figura neta"><svg viewBox="0 0 {w} {h}" role="img" aria-label="Doble recta: '
            f'centímetres del mapa i {unitat} de veritat"><rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>'
            f'{"".join(o)}</svg></div>\n')


def linies(llargades, resolta=0):
    """Línies de mida real per mesurar amb el regle. 1 unitat = 1 mm."""
    fila, x0 = 13, 12
    W = x0 + max(llargades) * 10 + 8
    H = fila * len(llargades) + 4
    o = []
    for i, L in enumerate(llargades):
        y = 8 + i * fila
        x1 = x0 + L * 10
        o.append(f'<text x="2" y="{y + 1.8:g}" font-size="5" font-weight="700" fill="{NEG}" {TIP}>{"ABCDEFGH"[i]}</text>'
                 f'<line x1="{x0}" y1="{y}" x2="{x1:g}" y2="{y}" stroke="{NEG}" stroke-width="1.2"/>'
                 f'<path d="M{x0} {y - 2.5}v5M{x1:g} {y - 2.5}v5" stroke="{NEG}" stroke-width="1.2"/>')
    return (f'    <svg class="real-cm" style="width:{W / 10:g}cm" viewBox="0 0 {W:g} {H:g}" role="img" '
            f'aria-label="Línies per mesurar">{"".join(o)}</svg>\n')


def quadricula(apartats, quadrets=12):
    """Una quadrícula d'1 cm de mida real per dibuixar-hi parets. `apartats`:
    (rètol, llargada en cm o None si l'ha de dibuixar l'alumnat). El primer ve dibuixat."""
    et, fila = 30, 16
    W = et + quadrets * 10 + 2
    H = len(apartats) * fila + 2
    o = []
    for i, (rotul, L) in enumerate(apartats):
        y0 = 1 + i * fila
        o.append(f'<text x="1" y="{y0 + 9.6:g}" font-size="5" fill="{NEG}" {TIP}>'
                 f'<tspan font-weight="700">{LLETRES[i]})</tspan> {rotul}</text>')
        for k in range(quadrets + 1):
            o.append(f'<line x1="{et + k * 10}" y1="{y0 + 3}" x2="{et + k * 10}" y2="{y0 + 13}" stroke="{CLAR}" stroke-width=".35"/>')
        for yy in (y0 + 3, y0 + 13):
            o.append(f'<line x1="{et}" y1="{yy}" x2="{et + quadrets * 10}" y2="{yy}" stroke="{CLAR}" stroke-width=".35"/>')
        if i == 0 and L:
            o.append(f'<line x1="{et}" y1="{y0 + 8}" x2="{et + L * 10:g}" y2="{y0 + 8}" stroke="{MANUS}" '
                     f'stroke-width="1.6" stroke-linecap="round"/>'
                     f'<text x="{et + L * 10 + 3:g}" y="{y0 + 10:g}" font-size="6.5" fill="{MANUS}" '
                     f'font-family="Caveat, cursive">{num(L)} cm</text>')
    return (f'    <svg class="real-cm" style="width:{W / 10:g}cm" viewBox="0 0 {W:g} {H:g}" role="img" '
            f'aria-label="Quadrícula per dibuixar">{"".join(o)}</svg>\n')


# --------------------------------------------------------------- la pàgina --

def act(n, peca, repte=False, nota_sol=""):
    """Una activitat: a partir de quina quantitat surt (1, 2 o 3) i si és de repte."""
    assert n in (1, 2, 3)
    alumnat, sol = peca
    return dict(n=n, repte=repte, alumnat=alumnat, sol=sol, nota_sol=nota_sol)


SIMBOLS = f'''<svg style="display:none" aria-hidden="true">
  <symbol id="i-calc" viewBox="0 0 48 48">
    <rect x="7" y="3" width="34" height="42" rx="6" fill="{NEG}"/>
    <rect x="12" y="8" width="24" height="12" rx="3" fill="{FONS2}"/>
    <g fill="#B0B0B0"><circle cx="16" cy="27" r="3"/><circle cx="24" cy="27" r="3"/><circle cx="32" cy="27" r="3"/>
    <circle cx="16" cy="36" r="3"/><circle cx="24" cy="36" r="3"/><circle cx="32" cy="36" r="3"/></g>
  </symbol>
  <symbol id="i-regle" viewBox="0 0 48 48">
    <rect x="3" y="16" width="42" height="16" rx="2" fill="{FONS}" stroke="{NEG}" stroke-width="3"/>
    <g stroke="{NEG}" stroke-width="2.5"><path d="M10 16v6M17 16v9M24 16v6M31 16v9M38 16v6"/></g>
  </symbol>
  <symbol id="i-llapis" viewBox="0 0 48 48">
    <path d="M8 40l3-11L33 7l8 8-22 22z" fill="{FONS}" stroke="{NEG}" stroke-width="3" stroke-linejoin="round"/>
    <path d="M28 12l8 8M11 29l8 8" stroke="{NEG}" stroke-width="3"/>
  </symbol>
  <symbol id="i-repte" viewBox="0 0 48 48">
    <path d="M24 4l5.9 12.6 13.8 1.7-10.2 9.5 2.7 13.7L24 34.8l-12.2 6.7 2.7-13.7L4.3 18.3l13.8-1.7z"
      fill="#fff" stroke="{NEG}" stroke-width="3.2" stroke-linejoin="round"/>
  </symbol>
</svg>'''

ESTRELLA = '<svg class="estrella" role="img" aria-label="Un pas més"><use href="#i-repte"/></svg>'


def recompte(blocs):
    """Quantes activitats surten a cada combinació del filtre."""
    totes = [a for b in blocs for a in b["acts"]]
    return {(n, r): sum(1 for a in totes if a["n"] <= n and (r or not a["repte"]))
            for n in (1, 2, 3) for r in (False, True)}


def comprova_unitat(u):
    """Les regles del quadern que no es poden trencar."""
    for b in u.BLOCS:
        germanes = [a["n"] for a in b["acts"] if not a["repte"]]
        assert germanes and germanes[0] == 1, f"{b['titol']}: la primera activitat ha de sortir sempre (n=1, sense repte)"
        assert germanes == sorted(germanes), f"{b['titol']}: les germanes van de menys a més (1, 2, 3)"
        reptes = [a for a in b["acts"] if a["repte"]]
        assert b["acts"][:len(germanes)] == [a for a in b["acts"] if not a["repte"]], \
            f"{b['titol']}: les de repte van al final del bloc"
        assert reptes, f"{b['titol']}: cada bloc té alguna activitat de repte"


def genera(num_u):
    u = carrega(num_u)
    comprova_unitat(u)
    blocs = u.BLOCS
    r = recompte(blocs)
    alumnat, sol = [], []
    for b in blocs:
        exercici, pagina = b["mira"]
        cap = (f'  <h2>{b["titol"]}</h2>\n'
               f'  <p class="mira">Com l\'exercici {exercici} de la fitxa, a la pàgina {pagina}.</p>\n')
        cos = []
        entrades = []
        for i, a in enumerate(b["acts"]):
            marca = f' data-n="{a["n"]}"' + (" data-repte" if a["repte"] else "")
            html = a["alumnat"].replace("ESTRELLA", ESTRELLA if a["repte"] else "")
            cos.append(f'  <div class="exercici act"{marca}>\n{html}  </div>\n')
            nota_a = f'<p class="per-que">{a["nota_sol"]}</p>' if a["nota_sol"] else ""
            repte = '<p class="repte-sol">Repte</p>' if a["repte"] else ""
            entrades.append(f'  <div class="sol-act"{marca}>{repte}{a["sol"]}{nota_a}</div>\n')
        # El títol del bloc no es queda sol a baix d'una pàgina: va amb la primera activitat,
        # que surt sempre.
        alumnat.append(f'<section class="bloc">\n<div class="inici">\n{cap}{cos[0]}</div>\n{"".join(cos[1:])}</section>\n')
        sol.append(f'  <h3>{b["titol"]} · com l\'exercici {exercici} de la fitxa</h3>\n'
                   + (f'  <p>{b["nota_sol"]}</p>\n' if b.get("nota_sol") else "") + "".join(entrades))

    taula_r = ("<table><tr><th></th><th>Petit</th><th>Mitjà</th><th>Elevat</th></tr>"
               f"<tr><td>Com les de la fitxa</td><td>{r[1, False]}</td><td>{r[2, False]}</td><td>{r[3, False]}</td></tr>"
               f"<tr><td>Amb repte</td><td>{r[1, True]}</td><td>{r[2, True]}</td><td>{r[3, True]}</td></tr></table>")

    return f'''<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Unitat {u.NUM} · Quadern d'activitats</title>
<!--
  Quadern d'activitats · Unitat {u.NUM} ({u.TITOL})
  NO S'EDITA A MÀ. El fa generadors/gen_quadern.py a partir de generadors/quadern/ud{u.NUM}.py.

  Activitats per practicar després de la fitxa, amb els mateixos criteris que la fitxa
  (docs/CRITERIS-DISSENY.md): blanc i negre, cap paràgraf, 14 pt cap amunt i el
  primer apartat de cada activitat resolt en lletra manuscrita.

  El filtre de dalt (només a la pantalla) tria quantes activitats surten i si n'hi ha
  de repte. Imprimir: el botó «Imprimeix el quadern», o Ctrl+P, A4, amb «Gràfics de
  fons» activat. El solucionari s'imprimeix a part, amb el seu botó.
-->
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
<link rel="stylesheet" href="../css/quadern.css">
<style>@page {{ @bottom-left {{ content: "Quadern d'activitats · Unitat {u.NUM}" }} }}</style>
</head>
<body class="amb-repte">

<nav class="navega no-imprimir" aria-label="Navegació"><a href="../fitxes.html">← totes les fitxes</a><a class="boto" href="../fitxes/ud{u.NUM}.html">la fitxa de la unitat</a></nav>

<div class="filtres no-imprimir" role="region" aria-label="Tria les activitats">
  <div class="grup">
    <span class="et" id="et-n">Nombre d'activitats</span>
    <div class="botons" data-filtre="n" role="group" aria-labelledby="et-n">
      <button type="button" data-valor="1" aria-pressed="false">Petit <small>{r[1, False]}</small></button>
      <button type="button" data-valor="2" aria-pressed="true">Mitjà <small>{r[2, False]}</small></button>
      <button type="button" data-valor="3" aria-pressed="false">Elevat <small>{r[3, False]}</small></button>
    </div>
  </div>
  <div class="grup">
    <span class="et" id="et-repte">Tipus</span>
    <div class="botons" data-filtre="repte" role="group" aria-labelledby="et-repte">
      <button type="button" data-valor="0" aria-pressed="true">Com les de la fitxa</button>
      <button type="button" data-valor="1" aria-pressed="false">Amb repte {ESTRELLA}</button>
    </div>
  </div>
  <div class="grup accions">
    <p class="recompte" id="recompte" aria-live="polite"></p>
    <div class="botons">
      <button type="button" id="imprimeix">Imprimeix el quadern</button>
      <button type="button" id="imprimeix-sol">Imprimeix el solucionari</button>
      <button type="button" id="mostra-sol" aria-expanded="false" aria-controls="solucionari">Mostra el solucionari</button>
    </div>
  </div>
</div>

{SIMBOLS}

<main class="quadern alumnat">
  <h1>Quadern d'activitats</h1>
  <p class="subtitol-q">Unitat {u.NUM} · {u.TITOL}</p>
  <p class="nom">Nom: <span></span></p>
  <p class="llegenda">{ESTRELLA} Un pas més.</p>

{"".join(alumnat)}</main>

<div class="quadern sol" id="solucionari">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat {u.NUM} · Quadern d'activitats · full per al professorat</p>
  <div class="abans">
    <p style="margin:0"><b>Com es fa servir.</b> El quadern és per després de la fitxa: cada bloc
    torna a un exercici de la fitxa, i la frase de sota del títol diu quin. A dalt de la pàgina es
    tria quantes activitats surten i si n'hi ha de repte (amb estrella). Els números de les
    activitats i els d'aquest solucionari es tornen a comptar sols, i sempre coincideixen si
    s'imprimeixen amb el mateix filtre. Es pot enviar un enllaç amb el filtre posat:
    <code>quadern/ud{u.NUM}.html?n=1&amp;repte=1</code> (n: 1 petit, 2 mitjà, 3 elevat).</p>
  </div>
  <p><b>Quantes activitats surten:</b></p>
  {taula_r}
  <p>Les de repte no són més llargues ni tenen més text: fan el mateix camí al revés, hi afegeixen
  un pas o demanen una decisió nova. Totes tenen el primer apartat resolt, com la fitxa.</p>
{"".join(sol)}
  <h3>Què mirar per avaluar</h3>
  <p>{u.AVALUAR}</p>
</div>

<script src="../js/quadern.js"></script>
</body>
</html>
'''


def carrega(num_u):
    cami = os.path.join(DADES, f"ud{num_u}.py")
    spec = importlib.util.spec_from_file_location(f"quadern_ud{num_u}", cami)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, AQUI)
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.path.remove(AQUI)
    return mod


def unitats():
    return sorted(int(re.search(r"ud(\d+)\.py$", f)[1]) for f in glob.glob(os.path.join(DADES, "ud*.py")))


def main():
    quines = [int(a) for a in sys.argv[1:]] or unitats()
    os.makedirs(SORTIDA, exist_ok=True)
    for n in quines:
        html = genera(n)
        with open(os.path.join(SORTIDA, f"ud{n}.html"), "w", encoding="utf-8") as f:
            f.write(html)
        r = recompte(carrega(n).BLOCS)
        print(f"  quadern/ud{n}.html  ·  petit {r[1, False]} ({r[1, True]} amb repte)"
              f"  ·  mitjà {r[2, False]} ({r[2, True]})  ·  elevat {r[3, False]} ({r[3, True]})")


if __name__ == "__main__":
    main()
