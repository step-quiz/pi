#!/usr/bin/env python3
"""Genera 1eso/targetes/patrons.html: la targeta de consulta «Patrons i símbols» (unitat 7).

Pla validat pel docent el 29/9/2026. Cara 1: els patrons (què hi ha de fix i què s'hi afegeix, la
taula, la regla a · n + b i la figura 10). Cara 2: de la paraula al símbol (la taula de traducció,
sempre amb el punt: 2 · n) i com es llegeix un gràfic de barres. Cap dibuix nou (regla B): els de
la caixa (tasques 26 a 28) i de les fitxes.

    python3 1eso/generadors/fitxes/targeta_patrons.py 1eso/targetes/patrons.html
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(AQUI, "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(AQUI, "peces_geo.py"), encoding="utf-8").read())

TD = 'style="border:1.5px solid var(--vora);padding:.2rem .6rem;text-align:center;font-size:16pt"'
TH = 'style="border:1.5px solid var(--vora);padding:.2rem .6rem;background:var(--fons-2);font-size:14pt"'

cara1 = f'''<div class="full targeta">
  <h1 class="cara-titol">Patrons</h1>
  <p style="font-size:15.5pt;margin:0 0 .2cm">Un patró creix sempre igual. Mira què és <b>fix</b> i què <b>creix</b>.</p>
  <div style="display:flex;gap:.9cm;align-items:flex-end;justify-content:center">
    {figures_d(2, 1, 3, 0.55, "El patró 2 · n + 1")}
  </div>
  <p style="font-size:14.5pt;margin:.25cm 0 0">El quadret blanc és fix. Cada figura té 2 quadrets més.</p>
  <table style="border-collapse:collapse;margin:.3cm auto 0">
    <tr><th {TH}>Figura</th><td {TD}>1</td><td {TD}>2</td><td {TD}>3</td><td {TD}>4</td><td {TD}>10</td></tr>
    <tr><th {TH}>Quadrets</th><td {TD}>3</td><td {TD}>5</td><td {TD}>7</td><td {TD}>9</td><td {TD}>21</td></tr>
  </table>
  <section class="clau" style="margin-top:.4cm">
    <h2>La regla</h2>
    <p>El que creix va davant de la n. El que és fix va al final: <b>2 · n + 1</b>.</p>
    <p>La figura 10: 2 · 10 + 1 = 21.</p>
    <p style="margin:0">Comprova la regla amb la figura 1: 2 · 1 + 1 = 3. Ha de donar el que té la figura 1.</p>
  </section>
  <div class="pag">Targeta dels patrons · cara 1</div>
</div>'''

TRAD = [("El doble d'un nombre", "2 · n"), ("El triple d'un nombre", "3 · n"), ("La meitat d'un nombre", "n : 2"),
        ("Un nombre més 5", "n + 5"), ("Un nombre menys 1", "n − 1"), ("El següent d'un nombre", "n + 1"),
        ("L'anterior d'un nombre", "n − 1")]
files = "\n".join(f'    <tr><td style="border:1.5px solid var(--vora);padding:.15rem .6rem;font-size:15pt">{p}</td>'
                  f'<td style="border:1.5px solid var(--vora);padding:.15rem .6rem;font-size:19pt;font-weight:800;text-align:center">{s}</td></tr>'
                  for p, s in TRAD)
cara2 = f'''<div class="full targeta">
  <h1 class="cara-titol">De la paraula al símbol</h1>
  <p style="font-size:15.5pt;margin:0 0 .2cm">La lletra <b>n</b> és un nombre qualsevol.</p>
  <table style="border-collapse:collapse;margin:0 auto">
    <tr><th {TH}>La frase</th><th {TH}>El símbol</th></tr>
{files}
  </table>
  <p style="font-size:14.5pt;margin:.25cm 0 0">Si n és 4: el triple, 3 · 4 = 12. El següent, 4 + 1 = 5.</p>
  <p style="font-size:14.5pt;margin:.1cm 0 0">El punt vol dir multiplicar. El grup ho escriu 2n; aquí, 2 · n.</p>
  <section class="clau" style="margin-top:.4cm">
    <h2>Llegir un gràfic de barres</h2>
    <p>1. El títol: de què parla.</p>
    <p>2. Sota cada barra: què compta.</p>
    <p>3. L'eix: quant val cada ratlla. Ha de començar a 0.</p>
    <p style="margin:0">4. On acaba la barra: aquest és el nombre.</p>
  </section>
  <div class="pag">Targeta dels patrons · cara 2</div>
</div>'''

cap = '''<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Patrons i símbols · targeta de consulta</title>
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
</head>
<body>
<!--
  TARGETA DE CONSULTA · Patrons i símbols
  La cinquena targeta, de la unitat 7 (pla validat pel docent el 29/9/2026). S'imprimeix a doble
  cara, girant per la vora llarga, i es plastifica. Cara 1: els patrons i la regla. Cara 2: de la
  paraula al símbol, sempre amb el punt (2 · n), i com es llegeix un gràfic de barres.

  Surt de generadors/fitxes/targeta_patrons.py: si s'hi ha de canviar res, es canvia allà i es torna
  a generar. Després, eines/comprova.py i el PDF amb generadors/gen_pdf.py.
-->

'''
html = cap + cara1 + "\n\n" + cara2 + "\n\n</body>\n</html>\n"
sortida = sys.argv[1] if len(sys.argv) > 1 else "patrons.html"
open(sortida, "w", encoding="utf-8").write(html)
print(sortida)
