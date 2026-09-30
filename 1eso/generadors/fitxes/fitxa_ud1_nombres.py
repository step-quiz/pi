import os
#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud1-nombres.html: centenes, desenes i unitats.

És la segona fitxa de la unitat 1, i adapta l'activitat 1_7 del grup («El nom
d'un nombre»). Fa servir les mateixes peces de dibuix que la primera fitxa
(genfitxa.py), perquè un quadret sigui igual a totes dues.
"""
import math, sys

from peces_comunes import *  # noqa: F401,F403  # Dibuix, ms, buit, buit_curt, ULL, colors…

PEU = "Unitat 1 · Nombres · pàgina"
MARCA = ('<svg viewBox="0 0 24 24" style="position:absolute;left:-3px;top:-6px;width:26px;height:26px">'
         '<path d="M4 13l5 6L21 3" fill="none" stroke="#3A3A3A" stroke-width="3.5" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')

pagines = []


def pagina(cos, classe="full"):
    n = len(pagines) + 1
    pagines.append(f'<div class="{classe}">\n{cos.rstrip()}\n  <div class="pag">{PEU} {n}</div>\n</div>')


from peces_nombres import peca, blocs  # noqa: E402,F401


def taula_xifres(c, dd, u, ma=False, cel="2.4cm"):
    v = (lambda t: ms(str(t))) if ma else str
    return (f'<table class="mini" style="width:auto;margin:0 auto"><tr><th style="width:{cel}">Centenes</th>'
            f'<th style="width:{cel}">Desenes</th><th style="width:{cel}">Unitats</th></tr>'
            f'<tr><td style="text-align:center;font-size:17pt;font-weight:800">{v(c)}</td>'
            f'<td style="text-align:center;font-size:17pt;font-weight:800">{v(dd)}</td>'
            f'<td style="text-align:center;font-size:17pt;font-weight:800">{v(u)}</td></tr></table>')


def xifres(n):
    return n // 100, n // 10 % 10, n % 10


def tria(opcions, bona=None):
    peces = []
    for o in opcions:
        if o == bona:
            peces.append(f'<label style="border-width:3px;border-color:var(--tinta)"><span class="quadret">{MARCA}</span>{o}</label>')
        else:
            peces.append(f'<label><span class="quadret"></span>{o}</label>')
    return '<div class="tria">' + "".join(peces) + "</div>"


# ===================================================================== pàgina 1
d = blocs(2, 4, 3, 0.26, "2 quadrats de 100, 4 columnes de 10 i 3 quadrets solts")
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>material de base 10</b> (plaques de 100, barres de 10 i cubs). Fer el 243 i dir-ne el nom en veu alta.</div>
  <h1>Centenes, desenes i unitats</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div class="figura neta" style="margin-top:1rem">
{d.svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .7rem">Són quadrats de 100, columnes de 10 i quadrets solts.</p>

  <table>
    <tr class="resolt"><td class="esq">Quants quadrats de 100 hi ha?</td><td style="width:4cm">{ms("2")}</td></tr>
    <tr class="resolt"><td class="esq">Quantes columnes de 10 hi ha?</td><td>{ms("4")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets solts hi ha?</td><td>{ms("3")}</td></tr>
  </table>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">Els quadrats de 100 són les centenes.</p>
    <p style="margin:0">Les columnes de 10 són les desenes.</p>
    <p style="margin:0 0 .5rem">Els quadrets solts són les unitats.</p>
    {taula_xifres(2, 4, 3)}
    <p style="font-size:30pt;font-weight:800;margin:.3rem 0 0">243</p>
    <p style="margin:0">Es llegeix: dos-cents quaranta-tres.</p>
  </div>''')

# ===================================================================== pàgina 2
files_t = []
for lletra, n, resolt in [("a", 243, True), ("b", 250, False), ("c", 403, False), ("d", 17, False)]:
    c, dd, u = xifres(n)
    # Els blocs, a 0,12 i no a 0,17: amb quatre quadrats de 100 (el 403), la columna dels blocs
    # empenyia la taula fora del full, i al PDF «El nombre» quedava tallat (29/9/2026).
    dib = blocs(c, dd, u, 0.12, f"Apartat {lletra}: {c} quadrats de 100, {dd} columnes de 10 i {u} quadrets solts")
    if resolt:
        cel = "".join(f'<td style="text-align:center">{ms(str(v))}</td>' for v in (c, dd, u)) + \
              f'<td style="text-align:center">{ms(str(n))}</td>'
    else:
        cel = '<td class="omplir"></td>' * 4
    files_t.append(f'''      <tr{' class="resolt"' if resolt else ''}>
        <td style="padding:.3rem .4rem"><span class="apartat">{lletra})</span>
{dib.svg("          ")}
        </td>
        {cel}
      </tr>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Mira els blocs. Escriu quants n'hi ha de cada. Després escriu el nombre.</div></div>
    <table class="mini" style="margin-top:.5rem">
      <tr><th>Els blocs</th><th style="width:2.2cm">Centenes</th><th style="width:2.2cm">Desenes</th><th style="width:2.2cm">Unitats</th><th style="width:2.2cm">El nombre</th></tr>
{chr(10).join(files_t)}
    </table>
  </div>

  <div class="avis puntejat">
    <p style="margin:0">Compta els blocs amb el dit.</p>
    <p style="margin:0">Si no n'hi ha cap, escriu un 0.</p>
  </div>''')

# ===================================================================== pàgina 3
files_p = []
for lletra, n, resolt in [("a", 243, True), ("b", 305, False), ("c", 124, False), ("d", 36, False)]:
    c, dd, u = xifres(n)
    dib = blocs(0, 0, 0, 0.17, f"Apartat {lletra}: 4 quadrats de 100, 9 columnes de 10 i 9 quadrets per pintar",
                buits=(4, 9, 9), pinta=(c, dd, u) if resolt else None)
    petita = (taula_xifres(c, dd, u, ma=True, cel="2.4cm") if resolt else
              '<table class="mini" style="width:auto;margin:0"><tr><th style="width:2.4cm">Centenes</th>'
              '<th style="width:2.4cm">Desenes</th><th style="width:2.4cm">Unitats</th></tr>'
              '<tr><td class="omplir" style="height:1.1cm"></td><td class="omplir" style="height:1.1cm"></td>'
              '<td class="omplir" style="height:1.1cm"></td></tr></table>')
    fons = ' class="resolt" style="border-radius:10px;padding:.35rem .5rem;margin-bottom:.45rem"' if resolt else ' style="padding:.35rem .5rem;margin-bottom:.45rem"'
    files_p.append(f'''    <div{fons}>
      <div style="display:flex;gap:.8cm;align-items:center;margin-bottom:.35rem">
        <p style="margin:0;font-size:17pt;font-weight:800;min-width:2cm"><span class="apartat">{lletra})</span> {n}</p>
        <div style="flex:0 0 auto">{petita}</div>
      </div>
{dib.svg("      ")}
    </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Escriu les xifres a la taula. Després pinta els blocs.</div></div>
{chr(10).join(files_p)}
  </div>''')

# ===================================================================== pàgina 4
NOMS_1 = [(1, "u"), (2, "dos"), (3, "tres"), (4, "quatre"), (5, "cinc"), (6, "sis"), (7, "set"), (8, "vuit"), (9, "nou")]
NOMS_2 = [(10, "deu"), (11, "onze"), (12, "dotze"), (13, "tretze"), (14, "catorze"), (15, "quinze"), (16, "setze"),
          (17, "disset"), (18, "divuit"), (19, "dinou")]
NOMS_3 = [(20, "vint"), (30, "trenta"), (40, "quaranta"), (50, "cinquanta"), (60, "seixanta"), (70, "setanta"),
          (80, "vuitanta"), (90, "noranta")]
NOMS_4 = [(100, "cent"), (200, "dos-cents"), (300, "tres-cents"), (400, "quatre-cents"), (500, "cinc-cents"),
          (600, "sis-cents"), (700, "set-cents"), (800, "vuit-cents"), (900, "nou-cents")]


def taula_noms():
    """Les quatre columnes en una sola taula, perquè les files quedin alineades."""
    cols = [NOMS_1, NOMS_2, NOMS_3, NOMS_4]
    files = []
    for i in range(max(len(c) for c in cols)):
        cel = ""
        for c in cols:
            if i < len(c):
                n, nom = c[i]
                cel += (f'<td style="border:0;text-align:right;font-weight:800;padding:.04rem .3rem .04rem .9rem">{n}</td>'
                        f'<td style="border:0;text-align:left;padding:.04rem .3rem">{nom}</td>')
            else:
                cel += '<td style="border:0"></td><td style="border:0"></td>'
        files.append("<tr>" + cel + "</tr>")
    return '<table style="width:auto;margin:0 auto">' + "".join(files) + "</table>"


clau_noms = f'''  <div class="clau" style="font-size:14pt;line-height:1.3">
    <h2>Els noms dels nombres</h2>
    <div style="font-size:14pt">{taula_noms()}</div>
    <p style="margin:.6rem 0 0">El guionet va entre les desenes i les unitats: <b>quaranta-tres</b>.</p>
    <p style="margin:0">També va entre les unitats i les centenes: <b>dos-cents</b>.</p>
    <p style="margin:0">Del 21 al 29 s'escriu amb una i: <b>vint-i-dos</b>.</p>
  </div>'''
NOMS_ITEMS = [("a", 243, "dos-cents quaranta-tres"), ("b", 510, None), ("c", 222, None), ("d", 108, None), ("e", 471, None)]
items_noms = "\n".join(
    f'''    <p class="frase" style="margin:.1rem 0;display:flex;gap:.6rem;align-items:baseline">'''
    f'''<span class="apartat">{l})</span><b style="min-width:1.6cm;display:inline-block">{n}</b>'''
    # La ratlla porta un espai dur: buida, el motor dels PDF no li trobava la línia de base i la
    # posava fora del full, i al PDF els apartats b) a e) no tenien on escriure (29/9/2026).
    + (f'''{ms(nom)}</p>''' if nom else f'''<u style="flex:1">&nbsp;</u></p>''')
    for l, n, nom in NOMS_ITEMS)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Escriu el nom de cada nombre. Mira la clau.</div></div>
{clau_noms}
    <div style="margin-top:.7rem">
{items_noms}
    </div>
  </div>''')

# ===================================================================== pàgina 5
QUIN = [("a", 305, [35, 305, 350], True), ("b", 108, [18, 180, 108], False), ("c", 60, [600, 6, 60], False),
        ("d", 510, [51, 510, 501], False)]
items_q = []
for lletra, n, opcions, resolt in QUIN:
    c, dd, u = xifres(n)
    dib = blocs(c, dd, u, 0.17, f"Apartat {lletra}: {c} quadrats de 100, {dd} columnes de 10 i {u} quadrets solts")
    fons = ' class="resolt" style="border-radius:10px;padding:.35rem .6rem;margin-bottom:.4rem"' if resolt else ' style="padding:.35rem .6rem;margin-bottom:.4rem"'
    explica = (f'\n      <p style="margin:.2rem 0 0;font-size:14pt">{c} centenes, {dd} desenes i {u} unitats.</p>'
               if resolt else "")
    items_q.append(f'''    <div{fons}>
      <div style="display:flex;gap:.8cm;align-items:center">
        <p class="apartat" style="margin:0">{lletra})</p>
        <div style="flex:0 0 auto">
{dib.svg("          ")}
        </div>
      </div>
      {tria(opcions, n if resolt else None)}{explica}
    </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Marca el nombre de cada dibuix.</div></div>
{chr(10).join(items_q)}
  </div>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">El 0 vol dir que en aquell lloc no hi ha cap bloc.</p>
    <p style="margin:.2rem 0 0">305 té 3 quadrats de 100, cap columna de 10 i 5 quadrets solts.</p>
  </div>''')

# ===================================================================== pàgina 6: la vida
def diners(n100, n10, n1, aria):
    b1w, b1h, b2w, b2h, r = 2.05, 1.1, 1.7, 0.95, 0.42
    g = 0.22
    amp = n100 * (b1w + g) + n10 * (b2w + g) + n1 * (2 * r + g) + 0.6
    d = Dibuix(amp, b1h + 0.2, aria)
    x = 0.1
    for _ in range(n100):
        d.cru(f'<rect x="{d.px(x)}" y="{d.px(0.1)}" width="{d.px(b1w)}" height="{d.px(b1h)}" rx="{d.px(0.12)}" '
              f'fill="{F2}" stroke="{G1}" stroke-width="2"/>')
        d.cru(f'<rect x="{d.px(x + 0.1)}" y="{d.px(0.2)}" width="{d.px(b1w - 0.2)}" height="{d.px(b1h - 0.2)}" '
              f'rx="{d.px(0.08)}" fill="none" stroke="{G3}" stroke-width="1"/>')
        d.text(x + b1w / 2, 0.1 + b1h / 2 + 0.16, "100 €", 0.44, 800)
        x += b1w + g
    x += 0.2
    for _ in range(n10):
        y = 0.1 + (b1h - b2h) / 2
        d.cru(f'<rect x="{d.px(x)}" y="{d.px(y)}" width="{d.px(b2w)}" height="{d.px(b2h)}" rx="{d.px(0.1)}" '
              f'fill="#fff" stroke="{G1}" stroke-width="2"/>')
        d.text(x + b2w / 2, y + b2h / 2 + 0.15, "10 €", 0.4, 800)
        x += b2w + g
    x += 0.2
    for _ in range(n1):
        cx, cy = x + r, 0.1 + b1h / 2
        d.cru(f'<circle cx="{d.px(cx)}" cy="{d.px(cy)}" r="{d.px(r)}" fill="{F2}" stroke="{G1}" stroke-width="2"/>')
        d.text(cx, cy + 0.13, "1 €", 0.34, 800)
        x += 2 * r + g
    return d


pagina(f'''  <h2>A la vida de cada dia</h2>

  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Quants euros hi ha?</div></div>
    <div class="resolt" style="border-radius:10px;padding:.4rem .6rem;margin-bottom:.5rem">
      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> 2 bitllets de 100 €, 4 bitllets de 10 € i 3 monedes d'1 €.</p>
{diners(2, 4, 3, "2 bitllets de 100 euros, 4 bitllets de 10 euros i 3 monedes d'1 euro").svg("      ")}
      <p class="frase" style="margin:.2rem 0 0">Hi ha {ms("243 €")}.</p>
    </div>
    <div style="padding:.4rem .6rem">
      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> 2 bitllets de 100 €, 2 bitllets de 10 € i 2 monedes d'1 €.</p>
{diners(2, 2, 2, "2 bitllets de 100 euros, 2 bitllets de 10 euros i 2 monedes d'1 euro").svg("      ")}
      <p class="frase" style="margin:.2rem 0 0">Hi ha {buit()} €.</p>
    </div>
  </div>

  <div class="exercici">
    <div class="tasca"><div class="n">6</div><div class="q">Paga amb bitllets i monedes.</div></div>
    <table class="mini">
      <tr><th></th><th>Bitllets de 100 €</th><th>Bitllets de 10 €</th><th>Monedes d'1 €</th></tr>
      <tr class="resolt"><td class="apartat">a) 305 €</td><td style="text-align:center">{ms("3")}</td><td style="text-align:center">{ms("0")}</td><td style="text-align:center">{ms("5")}</td></tr>
      <tr><td class="apartat">b) 250 €</td><td class="omplir"></td><td class="omplir"></td><td class="omplir"></td></tr>
      <tr><td class="apartat">c) 108 €</td><td class="omplir"></td><td class="omplir"></td><td class="omplir"></td></tr>
    </table>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 1 · Centenes, desenes i unitats · full per al professorat</p>

  <div class="abans">
    <b>Abans de començar.</b> Es diu sempre igual: «quadrats de 100», «columnes de 10» i
    «quadrets solts», i després «centenes», «desenes» i «unitats». Són les mateixes paraules que
    la caixa d'eines. Demaneu que llegeixi cada nombre en veu alta. Per escriure el nom, la clau de
    la pàgina 4 és al davant tota l'estona: no es demana de memòria.
  </div>

  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb material de base 10: fer el 243 amb 2 plaques, 4 barres i 3 cubs, i dir-ne el
  nom. Després, fer el 305 i dir que no hi ha cap barra. Si no hi ha material de base 10, serveixen
  quadrícules retallades: quadrats de 10 per 10, tires de 10 i quadrets solts.</p>

  <h3>1. Mira els blocs</h3>
  <table>
    <tr><th></th><th>Centenes</th><th>Desenes</th><th>Unitats</th><th>El nombre</th></tr>
    <tr><td>b)</td><td>2</td><td>5</td><td>0</td><td>250</td></tr>
    <tr><td>c)</td><td>4</td><td>0</td><td>3</td><td>403</td></tr>
    <tr><td>d)</td><td>0</td><td>1</td><td>7</td><td>17</td></tr>
  </table>
  <p><b>Error típic:</b> deixar el lloc buit quan no hi ha cap bloc d'un tipus. La casella del 0
  s'omple sempre: l'avís del final de la pàgina ho recorda. A l'apartat d, el 0 de les centenes no
  s'escriu al nombre: és 17, no 017.</p>

  <h3>2. Escriu les xifres i pinta els blocs</h3>
  <p>b) 305: 3 quadrats, cap columna i 5 quadrets. c) 124: 1 quadrat, 2 columnes i 4 quadrets.
  d) 36: cap quadrat, 3 columnes i 6 quadrets. Hi ha més siluetes de les que cal, a posta: triar
  quantes se'n pinten és la feina.</p>

  <h3>3. El nom del nombre</h3>
  <p>b) cinc-cents deu; c) dos-cents vint-i-dos; d) cent vuit; e) quatre-cents setanta-u. Es dona
  per bo «setanta-un»: «u» és el nom del nombre sol, i és el que fa servir el grup. <b>Error
  típic:</b> el guionet. Entre la centena i la resta no n'hi va: «cent vuit», i no «cent-vuit».</p>
</div>''')

pagines.append('''<div class="full sol">
  <h3>4. Marca el nombre de cada dibuix</h3>
  <p>b) 108; c) 60; d) 510. <b>Error típic:</b> escriure les xifres tal com se senten, sense el
  zero: «tres-cents cinc» → 35. És la regla trencada d'aquesta fitxa. No l'expliqueu: feu comptar
  els blocs i omplir la taula, i el 0 surt sol, a la casella de les desenes. Les opcions de cada
  apartat són les confusions de debò: el zero que falta i el zero que canvia de lloc. <b>Compta
  per als nivells alts, no per al mínim.</b></p>

  <h3>5 i 6. A la vida de cada dia</h3>
  <p>5b) 222 €. 6b) 250 €: 2 bitllets de 100 €, 5 de 10 € i cap moneda. 6c) 108 €: 1 bitllet de
  100 €, cap de 10 € i 8 monedes. És la mateixa decisió que als blocs: un bitllet de 100 € és una
  centena, un de 10 € és una desena i una moneda d'1 € és una unitat.</p>

  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=3</b> (3.1 Centenes,
  desenes i unitats; 3.2 Fes el nombre). La 3.2 dona un codi de verificació, que es llegeix a la
  pàgina de llegir codis. L'exemple resolt de la fitxa és el mateix que el de la caixa, el 243, i
  els nombres dels exercicis surten de la llista de la 3.2.</p>

  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb el material, el dibuix o la clau al davant. Els criteris de la SA del grup (1.3,
  2.1 i 8.1) són de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb material de base 10, fa un nombre de tres xifres i en diu el nom en veu alta.</li>
    <li>Diu quants quadrats de 100, columnes de 10 i quadrets solts té un dibuix, i escriu el nombre (exercici 1).</li>
    <li>Escriu les xifres d'un nombre a la taula i en pinta els blocs, també quan té un zero (exercici 2).</li>
    <li>Amb la clau al davant, escriu el nom d'un nombre de tres xifres amb els guionets (exercici 3).</li>
    <li>Paga una quantitat amb bitllets de 100 €, de 10 € i monedes d'1 € (exercici 6).</li>
    <li>Nivells alts: tria el 305 entre el 35, el 305 i el 350 per al mateix dibuix (exercici 4).</li>
  </ul>
</div>''')

# ===================================================================== el document
cap = '''<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Unitat 1 · Centenes, desenes i unitats</title>
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
</head>
<body>
<!--
  FITXA · Unitat 1 · Nombres naturals · Centenes, desenes i unitats
  La segona fitxa de la unitat. Adapta l'activitat 1_7 del grup («El nom d'un
  nombre»): fins al 999, amb quadrats de 100, columnes de 10 i quadrets solts,
  el mateix quadret de tot el curs. Els milers, els milions i els bilions de
  la taula de posicions del grup queden fora (regla D).

  Els casos són els de la caixa d'eines (regla 8): el 243 és l'exemple de la
  3.1, i els nombres dels exercicis surten de la llista de la 3.2.

  La regla trencada és el zero: «tres-cents cinc» escrit 35. Es desmunta amb els
  blocs (exercici 4) i la pàgina acaba amb la forma bona a la vista.

  Cada bloc .full acaba amb un </div> a principi de línia; els de dins van
  sagnats. Les regles són a docs/CRITERIS-DISSENY.md. Després de canviar
  res: eines/mesura.py, generadors/gen_pdf.py i eines/comprova.py.
-->

'''
html = cap + "\n\n".join(pagines) + "\n\n</body>\n</html>\n"
sortida = sys.argv[1] if len(sys.argv) > 1 else "ud1-nombres.html"
desa(html, sortida)
print(sortida, len(pagines), "blocs")
