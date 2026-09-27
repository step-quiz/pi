#!/usr/bin/env python3
"""Genera 1eso/targetes/fraccions.html: la targeta de consulta «Els noms de les fraccions».

Decisió del docent del 26/9/2026: el grup demana els noms de memòria, i la regla B diu que el
que s'ha de recordar va a una targeta. Cara 1: els noms, del mig al dotzè. Cara 2: com es
llegeix una fracció, els tipus, les equivalents i la regla de la suma.
"""
import os
import sys
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])

NOMS = [(2, "mig", "mitjos", 2), (3, "terç", "terços", 2), (4, "quart", "quarts", 3), (5, "cinquè", "cinquens", 2),
        (6, "sisè", "sisens", 5), (7, "setè", "setens", 3), (8, "vuitè", "vuitens", 3), (9, "novè", "novens", 4),
        (10, "desè", "desens", 7), (11, "onzè", "onzens", 2), (12, "dotzè", "dotzens", 5)]
NUM = {1: "un", 2: "dos", 3: "tres", 4: "quatre", 5: "cinc", 6: "sis", 7: "set", 8: "vuit"}


def fr(n, d, mida="17pt"):
    """La fracció escrita com a fracció. La marca .fr és la que llegeix eines/comprova.py."""
    return (f'<span class="fr" style="display:inline-block;vertical-align:middle;text-align:center;line-height:1.05;'
            f'font-weight:800;margin:0 .1em;font-size:{mida}">'
            f'<span style="display:block;border-bottom:.09em solid;padding:0 .18em .04em">{n}</span>'
            f'<span style="display:block;padding:.04em .18em 0">{d}</span></span>')


def tira(n, d, W, H, aria, mes=0):
    """El rectangle de la caixa: d trossos iguals, n de pintats (i `mes` en gris més fosc)."""
    unitats = max(1, -(-(n + mes) // d))
    D = Dibuix(W + 0.2, unitats * (H + 0.25) - 0.25 + 0.2, aria)
    w = W / d
    resta, m = n, mes
    for u in range(unitats):
        y = 0.1 + u * (H + 0.25)
        p = min(d, resta); resta -= p
        q = min(d - p, m); m -= q
        for i in range(d):
            fons = F3 if i < p else (G3 if i < p + q else "#fff")
            D.cru(f'<rect x="{D.px(0.1 + i * w)}" y="{D.px(y)}" width="{D.px(w)}" height="{D.px(H)}" fill="{fons}" '
                  f'stroke="{G2}" stroke-width="1.2"/>')
        D.cru(f'<rect x="{D.px(0.1)}" y="{D.px(y)}" width="{D.px(W)}" height="{D.px(H)}" fill="none" stroke="{G1}" stroke-width="2.2"/>')
    return D


# ===================================================================== cara 1: els noms
files = []
for d, s1, p1, ex in NOMS:
    t = tira(1, d, 4.2, 0.55, f"Un rectangle de {d} trossos, amb un de pintat")
    files.append(f'''      <tr>
        <td style="border:0;padding:.18rem .3rem;width:4.6cm">{t.svg("")}</td>
        <td style="border:0;padding:.18rem .3rem;text-align:center;width:1.6cm">{fr(1, d)}</td>
        <td style="border:0;padding:.18rem .4rem;font-size:16pt;font-weight:700;text-align:left">un {s1}</td>
        <td style="border:0;padding:.18rem .3rem;text-align:center;width:1.6cm">{fr(ex, d)}</td>
        <td style="border:0;padding:.18rem .4rem;font-size:16pt;text-align:left">{NUM[ex]} {p1}</td>
      </tr>''')
cara1 = f'''<div class="full targeta">
  <h1 class="cara-titol">Els noms de les fraccions</h1>
  <table style="width:100%;border-collapse:collapse">
      <tr><th style="border:0;text-align:left;font-size:12pt;color:var(--gris-2)">El dibuix</th><th style="border:0;font-size:12pt;color:var(--gris-2)" colspan="2">Un</th><th style="border:0;font-size:12pt;color:var(--gris-2)" colspan="2">Més d'un</th></tr>
{chr(10).join(files)}
  </table>
  <section class="clau" style="margin-top:.6cm">
    <p>Del 5 en endavant, un s'acaba en <b>-è</b>: un cinquè.</p>
    <p>Si n'hi ha més d'un, s'acaba en <b>-ens</b>: dos cinquens.</p>
    <p>El de dalt es diu com sempre: un, dos, tres, quatre…</p>
  </section>
  <div class="pag">Targeta de les fraccions · cara 1</div>
</div>'''

# ===================================================================== cara 2: com es llegeix
TIPUS = [(0, "Nul·la", "No hi ha res pintat."), (3, "Pròpia", "És menys d'un rectangle."),
         (4, "Unitat", "És tot el rectangle."), (5, "Impròpia", "És més d'un rectangle.")]
files_t = "\n".join(f'''      <tr>
        <td style="border:0;padding:.2rem .3rem;text-align:center;width:1.6cm">{fr(n, 4)}</td>
        <td style="border:0;padding:.2rem .3rem;width:5cm">{tira(n, 4, 4.4, 0.5, f"{n} trossos pintats de 4").svg("")}</td>
        <td style="border:0;padding:.2rem .4rem;font-size:15pt;text-align:left"><b>{nom}.</b> {frase}</td>
      </tr>''' for n, nom, frase in TIPUS)
equiv = "\n".join(f'''      <tr>
        <td style="border:0;padding:.15rem .3rem;text-align:center;width:1.6cm">{fr(n, d)}</td>
        <td style="border:0;padding:.15rem .3rem">{tira(n, d, 8.4, 0.5, f"{n} trossos pintats de {d}").svg("")}</td>
      </tr>''' for n, d in [(1, 2), (2, 4), (4, 8)])
cara2 = f'''<div class="full targeta">
  <h1 class="cara-titol">Com es llegeix una fracció</h1>
  <div style="display:flex;gap:.8cm;align-items:center">
    <div style="flex:0 0 auto">{fr(3, 4, "44pt")}</div>
    <div style="font-size:15pt;line-height:1.5">
      <p style="margin:0"><b>3</b>: els trossos pintats. És el <b>numerador</b>.</p>
      <p style="margin:0"><b>4</b>: els trossos que hi ha. És el <b>denominador</b>.</p>
      <p style="margin:0">Es llegeix: tres quarts.</p>
    </div>
  </div>
  <div style="margin:.25cm 0 .4cm">{tira(3, 4, 9.0, 0.7, "Un rectangle de 4 trossos, amb 3 de pintats").svg("")}</div>

  <h2 style="font-size:16pt;margin:.2cm 0 .1cm">Els quatre tipus</h2>
  <table style="width:100%;border-collapse:collapse">
{files_t}
  </table>

  <h2 style="font-size:16pt;margin:.35cm 0 .1cm">Equivalents: el mateix tros pintat</h2>
  <table style="border-collapse:collapse">
{equiv}
  </table>
  <p style="font-size:15pt;margin:.1cm 0 0">{fr(1, 2)} = {fr(2, 4)} = {fr(4, 8)}</p>

  <section class="clau" style="margin-top:.35cm">
    <h2>Sumar</h2>
    <p>Els de baix han de ser iguals, i no se sumen: {fr(3, 8)} + {fr(2, 8)} = {fr(5, 8)}</p>
  </section>
  <div class="pag">Targeta de les fraccions · cara 2</div>
</div>'''

cap = '''<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Els noms de les fraccions · targeta de consulta</title>
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
</head>
<body>
<!--
  TARGETA DE CONSULTA · Els noms de les fraccions
  La segona targeta, al costat de la de les taules (decisió del docent del
  26/9/2026). El grup demana els noms de memòria; aquí es miren. S'imprimeix a
  doble cara, girant per la vora llarga, i es plastifica.

  Cara 1: els noms, del mig al dotzè, amb el plural. Cara 2: com es llegeix
  una fracció, els quatre tipus, les equivalents i la regla de la suma. El
  dibuix és el mateix rectangle de la caixa d'eines (tasques 9 a 12).

  Les fraccions van dins de .fr: eines/comprova.py les llegeix com «3/4» i en
  comprova les igualtats. Si canvies res, passa'l, i torna a fer el PDF amb
  generadors/gen_pdf.py.
-->

'''
html = cap + cara1 + "\n\n" + cara2 + "\n\n</body>\n</html>\n"
sortida = sys.argv[1] if len(sys.argv) > 1 else "fraccions.html"
open(sortida, "w", encoding="utf-8").write(html)
print(sortida)
