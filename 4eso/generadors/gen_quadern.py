#!/usr/bin/env python3
"""Fa el quadern d'activitats de cada unitat: quadern/udN.html.

    python3 generadors/gen_quadern.py          (des de 4eso/)
    python3 generadors/gen_quadern.py 3        (només la UD3)

El quadern és per practicar DESPRÉS de la fitxa. Està fet de blocs, un per cada
exercici de la fitxa. Cada bloc té una activitat «germana» (el mateix tipus
d'exercici amb altres números i altres contextos) i una de repte (una mica
diferent: el camí al revés, un pas més, una decisió nova).

EL FILTRE (decisió del docent, 5/11/2026)
El nombre d'activitats no canvia: el que canvia és quants apartats té cada una.
Cada activitat té el seu apartat a) resolt i 12 apartats per fer:

    petit    a) resolt + b, c, d              (3 per fer)
    mitjà    a) resolt + b … g                (6 per fer)
    elevat   a) resolt + b … m                (12 per fer)

Cada apartat porta data-n="1|2|3" (a partir de quina quantitat surt), i el filtre
(js/quadern.js) amaga els que no toquen. Com que els que s'amaguen sempre són els
últims, les lletres que queden van seguides sense haver-les de tornar a posar.
Un dibuix que només serveix per a uns quants apartats (un plànol, un mapa) va amb
ells dins d'una .seccio, que porta la mateixa marca i s'amaga amb ells.

Les activitats de repte porten data-repte: surten si el docent tria «Amb repte», i
els seus apartats creixen igual (3, 6 o 12).

El solucionari porta les mateixes marques en el mateix ordre: el filtre amaga les
mateixes entrades. Els números de les activitats són comptadors CSS, que se salten
el que està amagat, i coincideixen sempre amb els de les pàgines de l'alumnat.

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

NEG, GRIS, MANUS, CLAR, FONS, FONS2 = "#000", "#5E5E5E", "#3A3A3A", "#BFBFBF", "#F2F2F2", "#E4E4E4"
TIP = 'font-family="system-ui"'

# Quants apartats per fer hi ha a cada quantitat, i quants n'hi ha en total (amb l'a).
PER_FER = {1: 3, 2: 6, 3: 12}
APARTATS = 1 + PER_FER[3]
LLETRES = "abcdefghijklmnopqrstuvwxyz"


def nivell(k):
    """A partir de quina quantitat surt l'apartat k (0 és l'a, el resolt)."""
    return 1 if k <= PER_FER[1] else 2 if k <= PER_FER[2] else 3


# ------------------------------------------------------------------ números --

def num(x):
    """Un nombre en català: coma decimal i espai als milers (1 400, 25 000)."""
    x = round(x, 6)
    if x == int(x):
        return f"{int(x):,}".replace(",", " ")
    enter, dec = f"{x:.6f}".rstrip("0").split(".")
    return f"{int(enter):,}".replace(",", " ") + "," + dec


def eur(x):
    """Un preu: sempre dos decimals, «0,90 €»."""
    return f"{x:.2f}".replace(".", ",") + " €"


def esc(e):
    return "1 : " + num(e)


def ms(t):
    return f'<span class="ms">{t}</span>'


BUIT = '<span class="buit"></span>'
MARCA = ('<svg viewBox="0 0 24 24" style="position:absolute;left:-3px;top:-6px;width:26px;height:26px">'
         f'<path d="M4 13l5 6L21 3" fill="none" stroke="{MANUS}" stroke-width="3.5" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')
ICONES = {"calc": "#i-calc", "regle": "#i-regle", "llapis": "#i-llapis"}


def opcio(text, marcada):
    if marcada:
        return (f'<label style="border-width:3px;border-color:var(--tinta)"><span class="quadret">'
                f'{MARCA}</span>{text}</label>')
    return f'<label><span class="quadret"></span>{text}</label>'


def ap(k, cos, etiqueta="div", classe=""):
    """Un apartat: porta la marca de la quantitat a partir de la qual surt."""
    c = ("ap " + classe).strip()
    return f'<{etiqueta} class="{c}" data-n="{nivell(k)}">{cos}</{etiqueta}>'


def seccio(k0, cos):
    return f'    <div class="seccio" data-n="{nivell(k0)}">\n{cos}    </div>\n'


def nota(t):
    return f'    <p class="nota-act">{t}</p>\n'


# ------------------------------------------------------------------- peces --
# Una activitat és una llista de seccions. Cada secció és una funció que rep la
# posició del seu primer apartat (k0) i torna (alumnat, solucionari, quants apartats).

def taula(cap, files, omplir, abans="", amples=None, esq=(), sol_nota=""):
    """Una taula com les de la fitxa. Si és la primera fila de l'activitat, va resolta
    en lletra manuscrita; a les altres, les columnes d'`omplir` surten buides."""
    def fes(k0):
        n = len(cap)
        am = amples or [round(88 / n)] * n
        th = '<th style="width:10%"></th>' + "".join(f'<th style="width:{a}%">{c}</th>' for a, c in zip(am, cap))
        o = [abans, f'    <table>\n      <thead><tr>{th}</tr></thead>\n      <tbody>\n']
        s = ["<table><tr><th></th>" + "".join(f"<th>{c}</th>" for c in cap) + "</tr>"]
        for i, fila in enumerate(files):
            assert len(fila) == n, fila
            k = k0 + i
            if k == 0:
                cel = f'<td class="ms">a)</td>' + "".join(
                    f'<td class="ms{" esq" if j in esq else ""}">{v}</td>' for j, v in enumerate(fila))
                o.append("        " + ap(k, cel, "tr", "resolt") + "\n")
            else:
                cel = f"<td><b>{LLETRES[k]})</b></td>" + "".join(
                    '<td class="omplir"></td>' if j in omplir
                    else f'<td class="dada{" esq" if j in esq else ""}">{v}</td>' for j, v in enumerate(fila))
                o.append("        " + ap(k, cel, "tr") + "\n")
            s.append(ap(k, f"<td>{LLETRES[k]})</td>" + "".join(
                f"<td><b>{v}</b></td>" if j in omplir else f"<td>{v}</td>" for j, v in enumerate(fila)), "tr"))
        o.append("      </tbody>\n    </table>\n")
        s.append("</table>" + (f"<p>{sol_nota}</p>" if sol_nota else ""))
        return seccio(k0, "".join(o)), seccio(k0, "".join(s)), len(files)
    return fes


def tria(apartats, abans="", en_linia=False):
    """Apartats de marcar una opció: (text o html, [opcions], la bona). El primer de
    l'activitat ja va marcat. `en_linia`: el text i les opcions a la mateixa fila."""
    def fes(k0):
        o, s = [abans], []
        for i, (text, opcions, bona) in enumerate(apartats):
            k = k0 + i
            lletra = f'<span class="apartat">{LLETRES[k]})</span>'
            ops = "".join(opcio(op, k == 0 and j == bona) for j, op in enumerate(opcions))
            if en_linia:
                o.append("    " + ap(k, f'<div class="text">{lletra} {text}</div><div class="tria">{ops}</div>',
                                    classe="tria-linia") + "\n")
            else:
                o.append("    " + ap(k, f'<div>{lletra} {text}</div><div class="tria">{ops}</div>',
                                    classe="tria-bloc") + "\n")
            s.append(ap(k, f'{" · " if i else ""}{LLETRES[k]}) <b>{opcions[bona]}</b>', "span"))
        return seccio(k0, "".join(o)), seccio(k0, "    <p>" + "".join(s) + "</p>\n"), len(apartats)
    return fes


def taula_tria(apartats, opcions):
    """Una taula petita de dues files i, al costat, les opcions per marcar.
    `apartats`: (nom, [magnitud 1, magnitud 2], [[valors 1], [valors 2]], la bona)."""
    def fes(k0):
        o, s = [], []
        for i, (nom, mags, valors, bona) in enumerate(apartats):
            k = k0 + i
            files = "".join(f"<tr><th>{m}</th>" + "".join(f"<td>{v}</td>" for v in fila) + "</tr>"
                            for m, fila in zip(mags, valors))
            ops = "".join(opcio(op, k == 0 and j == bona) for j, op in enumerate(opcions))
            o.append("    " + ap(k, f'<div><span class="apartat">{LLETRES[k]})</span> {nom}</div>'
                                   f'<div class="costat"><table class="mini fila">{files}</table>'
                                   f'<div class="tria columna">{ops}</div></div>', classe="taula-tria") + "\n")
            s.append(ap(k, f'{" · " if i else ""}{LLETRES[k]}) <b>{opcions[bona]}</b>', "span"))
        return seccio(k0, "".join(o)), seccio(k0, "    <p>" + "".join(s) + "</p>\n"), len(apartats)
    return fes


def ofertes(apartats):
    """Comparar ofertes amb el preu d'1, com l'exercici 6 de la U3.
    `apartats`: (producte, [opció…], la bona). Cada opció és un dict:
        nom    el que es marca («El pack»)
        diu    l'oferta tal com es llegeix
        compte el compte que porta al preu d'1 («5,10 ÷ 6»), sense el resultat
        val    el preu d'1 («0,85 € el litre»)
    El primer apartat de l'activitat ja va resolt."""
    def fes(k0):
        o, files = [], []
        for i, (producte, ops, bona) in enumerate(apartats):
            k = k0 + i
            tres = " tres" if len(ops) > 2 else ""
            targetes = []
            for op in ops:
                if k == 0:
                    targetes.append(f'<div class="oferta resolt">{op["diu"]}<br>'
                                    + ms(f'{op["compte"]} = <b>{op["val"]}</b>') + "</div>")
                else:
                    targetes.append(f'<div class="oferta">{op["diu"]}<br><b>{op["compte"]} =</b></div>')
            marques = "".join(opcio(op["nom"], k == 0 and j == bona) for j, op in enumerate(ops))
            o.append("    " + ap(k, f'<div><span class="apartat">{LLETRES[k]})</span> {producte}</div>'
                                   f'<div class="parella-op{tres}">{"".join(targetes)}</div>'
                                   f'<div class="tria{" compacta" if tres else ""}">{marques}</div>',
                                classe="oferta-ap") + "\n")
            comptes = " · ".join(f'{op["compte"]} = {op["val"]}' for op in ops)
            files.append(ap(k, f"<td>{LLETRES[k]})</td><td>{producte.rstrip('.')}</td><td>{comptes}</td>"
                               f"<td><b>{ops[bona]['nom']}</b></td>", "tr"))
        sol = ("    <table><tr><th></th><th>Producte</th><th>El preu d'1</th><th>Guanya</th></tr>"
               + "".join(files) + "</table>\n")
        return seccio(k0, "".join(o)), seccio(k0, sol), len(apartats)
    return fes


def quadricula(llargades, quadrets=12, abans=""):
    """Parets per dibuixar sobre una quadrícula d'1 cm de mida real. Cada apartat és una
    fila: el rètol a l'esquerra (la mida de veritat en metres, escala 1 : 100) i els
    quadrets. El primer de l'activitat ja va dibuixat."""
    def fes(k0):
        o, s = [abans], []
        et = 30
        W, H = et + quadrets * 10 + 2, 13
        for i, L in enumerate(llargades):
            k = k0 + i
            g = [f'<text x="1" y="8.6" font-size="5" fill="{NEG}" {TIP}><tspan font-weight="700">'
                 f'{LLETRES[k]})</tspan> {num(L)} m</text>']
            for q in range(quadrets + 1):
                g.append(f'<line x1="{et + q * 10}" y1="1.5" x2="{et + q * 10}" y2="11.5" stroke="{CLAR}" stroke-width=".35"/>')
            for yy in (1.5, 11.5):
                g.append(f'<line x1="{et}" y1="{yy}" x2="{et + quadrets * 10}" y2="{yy}" stroke="{CLAR}" stroke-width=".35"/>')
            if k == 0:
                g.append(f'<line x1="{et}" y1="6.5" x2="{et + L * 10:g}" y2="6.5" stroke="{MANUS}" '
                         f'stroke-width="1.6" stroke-linecap="round"/>'
                         f'<text x="{et + L * 10 + 3:g}" y="8.6" font-size="6.5" fill="{MANUS}" '
                         f'font-family="Caveat, cursive">{num(L)} cm</text>')
            o.append("    " + ap(k, f'<svg class="real-cm" style="width:{W / 10:g}cm" viewBox="0 0 {W} {H}" '
                                   f'role="img" aria-label="Quadrícula per dibuixar una paret de {num(L)} m">'
                                   f'{"".join(g)}</svg>', classe="fila-quad") + "\n")
            s.append(ap(k, f'{" · " if i else ""}{LLETRES[k]}) <b>{num(L)} cm</b>', "span"))
        return seccio(k0, "".join(o)), seccio(k0, "    <p>" + "".join(s) + "</p>\n"), len(llargades)
    return fes


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
        rects.append(f'<rect x="{X:g}" y="{Y:g}" width="{Wr:g}" height="{Hr:g}" fill="{FONS2 if moble else FONS}" '
                     f'stroke="{NEG}" stroke-width="{0.8 if moble else 1}"/>')
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


def doble_recta(cm, per_cm, unitat="m", dalt="al mapa (cm)", w=560, h=124):
    """La doble recta de la fitxa (gen_grafics5.doble_mapa), amb l'escala que calgui:
    a dalt els cm del mapa, a baix el que valen de veritat. El primer tram, ombrejat."""
    baix = f"de veritat ({unitat})"
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


def linies(llargades, primera=0):
    """Línies de mida real per mesurar amb el regle. 1 unitat = 1 mm. Cada línia porta
    la lletra (en majúscula) de l'apartat de la taula que la mesura."""
    fila, x0 = 13, 12
    W = x0 + 100 + 8
    H = fila * len(llargades) + 4
    o = []
    for i, L in enumerate(llargades):
        y = 8 + i * fila
        x1 = x0 + L * 10
        o.append(f'<text x="2" y="{y + 1.8:g}" font-size="5" font-weight="700" fill="{NEG}" {TIP}>'
                 f'{LLETRES[primera + i].upper()}</text>'
                 f'<line x1="{x0}" y1="{y}" x2="{x1:g}" y2="{y}" stroke="{NEG}" stroke-width="1.2"/>'
                 f'<path d="M{x0} {y - 2.5}v5M{x1:g} {y - 2.5}v5" stroke="{NEG}" stroke-width="1.2"/>')
    return (f'    <svg class="real-cm" style="width:{W / 10:g}cm" viewBox="0 0 {W:g} {H:g}" role="img" '
            f'aria-label="Línies per mesurar">{"".join(o)}</svg>\n')


# --------------------------------------------------------------- la pàgina --

def act(q, seccions, ico=None, repte=False, nota_sol=""):
    """Una activitat: la consigna, la icona, les seccions i si és de repte."""
    return dict(q=q, ico=ico, seccions=seccions, repte=repte, nota_sol=nota_sol)


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


def munta(a):
    """L'html d'una activitat (alumnat i solucionari) a partir de les seves seccions."""
    k, alumnat, sol = 0, [], []
    for s in a["seccions"]:
        h, so, quants = s(k)
        alumnat.append(h)
        sol.append(so)
        k += quants
    assert k == APARTATS, f"«{a['q']}»: té {k} apartats i n'ha de tenir {APARTATS} (l'a i {PER_FER[3]} per fer)"
    icona = (f'\n        <svg class="ico" style="margin-left:.4rem"><use href="{ICONES[a["ico"]]}"/></svg>'
             if a["ico"] else "")
    cap = (f'    <div class="tasca"><div class="n"></div>{ESTRELLA if a["repte"] else ""}\n'
           f'      <div class="q">{a["q"]}{icona}</div></div>\n')
    return cap + "".join(alumnat), "".join(sol)


def comprova_unitat(u):
    """Les regles del quadern que no es poden trencar."""
    for b in u.BLOCS:
        germanes = [a for a in b["acts"] if not a["repte"]]
        reptes = [a for a in b["acts"] if a["repte"]]
        assert germanes and reptes, f"{b['titol']}: cada bloc té una germana i una de repte"
        assert b["acts"] == germanes + reptes, f"{b['titol']}: la de repte va després de la germana"


def genera(num_u):
    u = carrega(num_u)
    comprova_unitat(u)
    alumnat, sol = [], []
    for b in u.BLOCS:
        exercici, pagina = b["mira"]
        cos, entrades = [], []
        for a in b["acts"]:
            html, s = munta(a)
            marca = " data-repte" if a["repte"] else ""
            cos.append(f'  <div class="exercici act"{marca}>\n{html}  </div>\n')
            nota_a = f'<p class="per-que">{a["nota_sol"]}</p>' if a["nota_sol"] else ""
            repte = '<p class="repte-sol">Repte</p>' if a["repte"] else ""
            entrades.append(f'  <div class="sol-act"{marca}>{repte}\n{s}  {nota_a}</div>\n')
        alumnat.append(f'<section class="bloc">\n  <h2>{b["titol"]}</h2>\n'
                       f'  <p class="mira">Com l\'exercici {exercici} de la fitxa, a la pàgina {pagina}.</p>\n'
                       f'{"".join(cos)}</section>\n')
        sol.append(f'  <h3>{b["titol"]} · com l\'exercici {exercici} de la fitxa</h3>\n'
                   + (f'  <p>{b["nota_sol"]}</p>\n' if b.get("nota_sol") else "") + "".join(entrades))
    nb = len(u.BLOCS)
    ng = sum(1 for b in u.BLOCS for a in b["acts"] if not a["repte"])
    nr = sum(1 for b in u.BLOCS for a in b["acts"] if a["repte"])

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

  El filtre de dalt (només a la pantalla) tria quants apartats té cada activitat i si
  hi ha activitats de repte. Imprimir: el botó «Imprimeix el quadern», o Ctrl+P, A4,
  amb «Gràfics de fons» activat. El solucionari s'imprimeix a part, amb el seu botó.
-->
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
<link rel="stylesheet" href="../css/quadern.css">
<style>@page {{ @bottom-left {{ content: "Quadern d'activitats · Unitat {u.NUM}" }} }}</style>
</head>
<body class="amb-repte">

<nav class="navega no-imprimir" aria-label="Navegació"><a href="../quadern.html">← tots els quaderns</a><a class="boto" href="../fitxes/ud{u.NUM}.html">la fitxa de la unitat</a></nav>

<div class="filtres no-imprimir" role="region" aria-label="Tria les activitats">
  <div class="grup">
    <span class="et" id="et-n">Apartats de cada activitat</span>
    <div class="botons" data-filtre="n" role="group" aria-labelledby="et-n">
      <button type="button" data-valor="1" aria-pressed="false">Petit <small>{PER_FER[1]}</small></button>
      <button type="button" data-valor="2" aria-pressed="true">Mitjà <small>{PER_FER[2]}</small></button>
      <button type="button" data-valor="3" aria-pressed="false">Elevat <small>{PER_FER[3]}</small></button>
    </div>
  </div>
  <div class="grup">
    <span class="et" id="et-repte">Activitats</span>
    <div class="botons" data-filtre="repte" role="group" aria-labelledby="et-repte">
      <button type="button" data-valor="0" aria-pressed="true">Com les de la fitxa <small>{ng}</small></button>
      <button type="button" data-valor="1" aria-pressed="false">Amb repte {ESTRELLA} <small>{ng + nr}</small></button>
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
    <p style="margin:0"><b>Com es fa servir.</b> El quadern és per després de la fitxa: hi ha un bloc
    per cada exercici de la fitxa ({nb} blocs), i la frase de sota del títol diu quin. Cada bloc té
    una activitat com la de la fitxa i, si es tria «Amb repte», una altra una mica diferent, amb
    estrella. A dalt de la pàgina es tria quants apartats té cada activitat: a) resolt i
    {PER_FER[1]} per fer (petit), {PER_FER[2]} (mitjà) o {PER_FER[3]} (elevat). El nombre
    d'activitats no canvia. Les lletres i els números d'aquest solucionari coincideixen sempre
    amb els del quadern si s'imprimeixen amb el mateix filtre. Es pot enviar un enllaç amb el
    filtre posat: <code>quadern/ud{u.NUM}.html?n=1&amp;repte=1</code> (n: 1 petit, 2 mitjà,
    3 elevat).</p>
  </div>
  <p>Les de repte no tenen més text que les altres: fan el mateix camí al revés, hi afegeixen un
  pas o demanen una decisió nova. Totes tenen el primer apartat resolt, com la fitxa.</p>
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
        with open(os.path.join(SORTIDA, f"ud{n}.html"), "w", encoding="utf-8") as f:
            f.write(genera(n))
        u = carrega(n)
        ng = sum(1 for b in u.BLOCS for a in b["acts"] if not a["repte"])
        print(f"  quadern/ud{n}.html  ·  {ng} activitats ({2 * ng} amb repte)  ·  "
              f"a) resolt i {PER_FER[1]}, {PER_FER[2]} o {PER_FER[3]} apartats per fer")


if __name__ == "__main__":
    main()
