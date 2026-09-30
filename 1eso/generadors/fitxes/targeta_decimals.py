#!/usr/bin/env python3
"""Genera 1eso/targetes/decimals.html: la targeta de consulta «Decimals i arrels» (unitat 5).

Decisió del docent del 29/9/2026, amb el pla de la unitat 5. És el «Quadern d'eines» del llibre del
grup i la fitxa dels quadrats perfectes que proposa la pestanya d'inclusió de la programació.

  Cara 1 · Els decimals. Les tres peces (el quadrat de 100 és 1 unitat, la columna és 1 dècima, el
           quadret és 1 centèsima), com s'escriu i com es llegeix un decimal (2,43 i 3,04), i les
           tres regles de la unitat: comparar, arrodonir i sumar.
  Cara 2 · Un nombre, moltes cares (la fracció, el decimal i el percentatge al mateix quadrat de
           100) i els quadrats i les arrels, de 1 · 1 a 10 · 10.

Regla B: una targeta no porta dibuixos nous. Els blocs són els de la unitat 1 (fitxa_ud1_nombres.py)
i el quadrat de 100 és el dels percentatges de la unitat 4, pintat per columnes com a la caixa
(tasca 21). Tot fins a 9,99 i fins a 100: la targeta de les taules acaba a 10 · 10.

    python3 1eso/generadors/fitxes/targeta_decimals.py 1eso/targetes/decimals.html
"""
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(AQUI, "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])                      # Dibuix, els colors, ms…
_nombres = open(os.path.join(AQUI, "fitxa_ud1_nombres.py"), encoding="utf-8").read()
exec(_nombres[_nombres.index("def peca("):_nombres.index("def taula_xifres(")])   # peca() i blocs()
_fr = open(os.path.join(AQUI, "peces_fraccions.py"), encoding="utf-8").read()
exec(_fr[_fr.index("def fr("):_fr.index("def fr_buit(")])    # fr(): la fracció, amb la marca .fr


def quadrat100(n, m, aria):
    """El quadrat de 100 amb n quadrets pintats, columna a columna i de dalt a baix (com a la caixa,
    tasca 21): 25 quadrets són 2 columnes i 5 quadrets."""
    d = Dibuix(10 * m + 0.2, 10 * m + 0.2, aria)
    x0 = y0 = 0.1
    for i in range(n):
        col, fila = divmod(i, 10)
        d.cru(f'<rect x="{d.px(x0 + col * m)}" y="{d.px(y0 + fila * m)}" width="{d.px(m)}" height="{d.px(m)}" '
              f'fill="{F3}" stroke="none"/>')
    for k in range(1, 10):
        d.cru(f'<line x1="{d.px(x0)}" y1="{d.px(y0 + k * m)}" x2="{d.px(x0 + 10 * m)}" y2="{d.px(y0 + k * m)}" '
              f'stroke="{G3}" stroke-width="0.8"/>')
        d.cru(f'<line x1="{d.px(x0 + k * m)}" y1="{d.px(y0)}" x2="{d.px(x0 + k * m)}" y2="{d.px(y0 + 10 * m)}" '
              f'stroke="{G3}" stroke-width="0.8"/>')
    d.cru(f'<rect x="{d.px(x0)}" y="{d.px(y0)}" width="{d.px(10 * m)}" height="{d.px(10 * m)}" fill="none" '
          f'stroke="{G1}" stroke-width="2"/>')
    return d


def peca_sola(files, cols, m, aria):
    """Una peça dels blocs, sola: el quadrat de 100, la columna de 10 o el quadret."""
    d = Dibuix(cols * m + 0.2, files * m + 0.2, aria)
    peca(d, 0.1, 0.1, files, cols, m, "ple")
    return d


def costat(k, m, aria):
    """El quadrat de k per k, amb la clau del costat a dalt: l'arrel és el costat (unitat 1, tasca 2.3)."""
    d = Dibuix(k * m + 0.3, k * m + 0.95, aria)
    d.rectangle(0.15, 0.8, k, k, m)
    d.clau_dalt(0.15, 0.15 + k * m, 0.62, str(k), 0.5)
    return d


# Les cel·les de la taula de posicions, com la de la caixa (tasca 18) i la de la unitat 1.
TH = 'style="width:2.1cm"'
TD = 'style="text-align:center;font-size:20pt;font-weight:800"'


def posicions(u, dd, c):
    return (f'<table class="mini" style="width:auto;margin:0"><tr><th {TH}>Unitats</th>'
            f'<th style="width:.5cm;border:0;background:none"></th><th {TH}>Dècimes</th><th {TH}>Centèsimes</th></tr>'
            f'<tr><td {TD}>{u}</td><td style="border:0;text-align:center;font-size:22pt;font-weight:800">,</td>'
            f'<td {TD}>{dd}</td><td {TD}>{c}</td></tr></table>')


# ============================================================= cara 1: els decimals
m1 = 0.3
peces = [
    (peca_sola(10, 10, m1, "Un quadrat de 10 files de 10 quadrets"), "1 unitat", "1", "Quadrat de 100"),
    (peca_sola(10, 1, m1, "Una columna de 10 quadrets"), "1 dècima", "0,1", "Columna de 10"),
    (peca_sola(1, 1, m1, "Un quadret"), "1 centèsima", "0,01", "Quadret"),
]
caselles = "\n".join(f'''    <div style="flex:1 1 0;text-align:center">
      <p style="font-size:14pt;color:var(--gris-2);margin:0 0 .15cm;white-space:nowrap">{nom}</p>
      <div style="height:3.25cm;display:flex;align-items:flex-end;justify-content:center">{d.svg("")}</div>
      <p style="font-size:17pt;font-weight:800;margin:.2cm 0 0;white-space:nowrap">{nomd} = <span style="font-size:22pt">{num}</span></p>
    </div>''' for i, (d, nomd, num, nom) in enumerate(peces))

blocs243 = blocs(2, 4, 3, 0.21, "Els blocs de 2,43: 2 quadrats de 100, 4 columnes de 10 i 3 quadrets")
cara1 = f'''<div class="full targeta">
  <h1 class="cara-titol">Els decimals</h1>
  <div style="display:flex;gap:.9cm;align-items:flex-start">
{caselles}
  </div>
  <p style="font-size:15pt;margin:.35cm 0 0">10 quadrets fan 1 columna: 10 centèsimes fan 1 dècima.</p>
  <p style="font-size:15pt;margin:.1cm 0 0">10 columnes fan 1 quadrat: 10 dècimes fan 1 unitat.</p>

  <h2 style="font-size:16pt;margin:.5cm 0 .2cm">Com s'escriu i com es llegeix</h2>
  <div style="display:flex;gap:.7cm;align-items:center">
    <div>{blocs243.svg("")}</div>
    <div>{posicions(2, 4, 3)}</div>
  </div>
  <table style="border-collapse:collapse;margin:.3cm 0 0">
    <tr><td style="border:0;padding:.05rem .6rem .05rem 0;font-size:20pt;font-weight:800;text-align:left">2,43</td>
        <td style="border:0;padding:.05rem 0;font-size:15pt;text-align:left">dues unitats i quaranta-tres centèsimes</td></tr>
    <tr><td style="border:0;padding:.05rem .6rem .05rem 0;font-size:20pt;font-weight:800;text-align:left">3,04</td>
        <td style="border:0;padding:.05rem 0;font-size:15pt;text-align:left">tres unitats i quatre centèsimes: el 0 guarda el lloc</td></tr>
  </table>

  <section class="clau" style="margin-top:.45cm">
    <h2>Per recordar</h2>
    <p><b>Comparar.</b> Escriu els dos amb dues xifres després de la coma: 0,8 és 0,80. Com que 80 és més que 75, 0,8 és més gran que 0,75.</p>
    <p><b>Arrodonir a les dècimes.</b> Mira les centèsimes. 5 o més, amunt: 3,47 s'arrodoneix a 3,5. Menys de 5, avall: 3,42 s'arrodoneix a 3,4.</p>
    <p style="margin:0"><b>Sumar i restar.</b> La coma sota la coma: <span style="white-space:nowrap">2,50 + 1,35 = 3,85</span>.</p>
  </section>
  <p class="diu"><b>Com ho dic:</b> «2,43: 2 quadrats, 4 columnes i 3 quadrets.»</p>
  <div class="pag">Targeta dels decimals · cara 1</div>
</div>'''

# ============================================================= cara 2: moltes cares, i les arrels
CARES = [(1, 2), (1, 4), (3, 4), (1, 5), (1, 10)]           # els percentatges de la unitat 4
th = 'style="font-size:14pt;color:var(--gris-2);border:0;padding:0 .3rem .15rem;font-weight:600"'
files = []
for n, dnm in CARES:
    q = 100 // dnm * n
    dec = f"0,{q // 10}" if q % 10 == 0 else f"0,{q:02d}"
    dib = quadrat100(q, 0.16, f"El quadrat de 100 amb {q} quadrets pintats")
    files.append(f'''    <tr>
      <td style="border:0;padding:.05rem .3rem">{dib.svg("")}</td>
      <td style="border:0;padding:.05rem .3rem;text-align:center">{fr(n, dnm)}</td>
      <td style="border:0;padding:.05rem .3rem;text-align:center;font-size:20pt;font-weight:800">{dec}</td>
      <td style="border:0;padding:.05rem .3rem;text-align:center;font-size:20pt;font-weight:800">{q} %</td>
      <td style="border:0;padding:.05rem .3rem;font-size:14pt">{q} quadrets de 100</td>
    </tr>''')
QUADRATS = "\n".join(
    f'''    <tr>{"".join(f'<td style="border:0;padding:.08rem .35rem;font-size:17pt;white-space:nowrap">{k} · {k} = {k * k}</td>'
                     f'<td style="border:0;padding:.08rem 1.1rem .08rem .35rem;font-size:17pt;font-weight:800;white-space:nowrap">√{k * k} = {k}</td>'
                     for k in (a, a + 5))}</tr>'''
    for a in range(1, 6))
cara2 = f'''<div class="full targeta">
  <h1 class="cara-titol">Un nombre, moltes cares</h1>
  <table style="border-collapse:collapse;width:auto">
    <tr><th {th}>Al quadrat de 100</th><th {th}>Fracció</th><th {th}>Decimal</th><th {th}>Percentatge</th><th {th}></th></tr>
{chr(10).join(files)}
  </table>
  <p style="font-size:15pt;margin:.2cm 0 0">Pinta la fracció al quadrat de 100 i compta les columnes i els quadrets.</p>

  <h2 style="font-size:16pt;margin:.4cm 0 .1cm">Els quadrats i les arrels</h2>
  <table style="border-collapse:collapse;width:auto">
{QUADRATS}
  </table>
  <div style="display:flex;gap:.6cm;align-items:center;margin-top:.35cm">
    <div style="flex:0 0 auto">{costat(4, 0.42, "Un quadrat de 4 files de 4 quadrets: el costat fa 4").svg("")}</div>
    <section class="clau" style="flex:1 1 auto">
      <p><b>L'arrel és el costat del quadrat.</b> <span style="white-space:nowrap">√16 = 4</span>, perquè <span style="white-space:nowrap">4 · 4 = 16</span>. No és la meitat.</p>
      <p style="margin:0">Si el nombre no és a la llista, l'arrel és entre dos nombres. Per exemple, 20 és entre 16 i 25: <span style="white-space:nowrap">√20</span> és entre 4 i 5.</p>
    </section>
  </div>
  <div class="pag">Targeta dels decimals · cara 2</div>
</div>'''

cap = '''<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Decimals i arrels · targeta de consulta</title>
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
</head>
<body>
<!--
  TARGETA DE CONSULTA · Decimals i arrels
  La tercera targeta, de la unitat 5 (decisió del docent del 29/9/2026). S'imprimeix a doble cara,
  girant per la vora llarga, i es plastifica.

  Cara 1: les tres peces (unitat, dècima i centèsima), com s'escriu i com es llegeix un decimal, i
  les regles de comparar, arrodonir i sumar. Cara 2: la fracció, el decimal i el percentatge al
  mateix quadrat de 100, i els quadrats i les arrels de 1 · 1 a 10 · 10.

  Surt de generadors/fitxes/targeta_decimals.py: si s'hi ha de canviar res, es canvia allà i es
  torna a generar. Després, eines/comprova.py i el PDF amb generadors/gen_pdf.py.
-->

'''
html = cap + cara1 + "\n\n" + cara2 + "\n\n</body>\n</html>\n"
sortida = sys.argv[1] if len(sys.argv) > 1 else "decimals.html"
open(sortida, "w", encoding="utf-8").write(html)
print(sortida)
