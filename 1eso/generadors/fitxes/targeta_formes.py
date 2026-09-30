#!/usr/bin/env python3
"""Genera 1eso/targetes/formes.html: la targeta de consulta «Formes» (unitat 6).

Pla validat pel docent el 29/9/2026. És el «quadre-vocabulari» de la paret de l'aula que proposa la
programació (SA6) i el «Quadern d'eines» del llibre.

  Cara 1 · Angles i rectes. La cantonada d'un quadret és l'angle recte: agut, recte, obtús i pla,
           cada un amb la cantonada discontínua al vèrtex. Punt, segment, semirecta i recta, i les
           rectes paral·leles, secants i perpendiculars.
  Cara 2 · Polígons, triangles i mesures. Els noms dels polígons de 3 a 8 costats, regular i
           còncau; els triangles pels costats (marques) i pels angles; els tres angles junts fan un
           angle pla; el perímetre i la circumferència.

Regla B: cap dibuix nou. Són els de la caixa (tasques 22 a 25) i de les fitxes de la unitat. Els
graus (90° i 180°) només surten com a nom, perquè els angles es comparen amb la cantonada.

    python3 1eso/generadors/fitxes/targeta_formes.py 1eso/targetes/formes.html
"""
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(AQUI, "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(AQUI, "peces_geo.py"), encoding="utf-8").read())

C = 'style="border:0;padding:.08rem .3rem;vertical-align:middle"'


def fila(dib, nom, frase):
    return (f'<tr><td {C}>{dib.svg("")}</td><td {C}><b style="font-size:16pt">{nom}</b></td>'
            f'<td {C}><span style="font-size:14.5pt">{frase}</span></td></tr>')


ANGLES = [(50, "Agut", "Més petit que la cantonada."), (90, "Recte · 90°", "Igual que la cantonada."),
          (130, "Obtús", "Més gran que la cantonada."), (180, "Pla · 180°", "Els dos costats fan una recta.")]
angles = "\n".join(fila(angle_d(g, f"Un angle {n.split(' ')[0].lower()}, amb la cantonada d'un quadret al vèrtex", llarg=1.75),
                        n, fr) for g, n, fr in ANGLES)
PECES = [("punt", "Punt", "Un lloc. No es pot mesurar."), ("segment", "Segment", "Té dos extrems. Es pot mesurar."),
         ("semirecta", "Semirecta", "Té un extrem i no s'acaba."), ("recta", "Recta", "No té cap extrem.")]
peces = "\n".join(fila(peca_linia(t, f"Un{'a' if t in ('semirecta', 'recta') else ''} {t}", amp=3.0), n, fr) for t, n, fr in PECES)
RECTES = [("paral·leles", "Paral·leles", "No es tallen mai."), ("secants", "Secants", "Es tallen."),
          ("perpendiculars", "Perpendiculars", "Es tallen i fan una cantonada.")]
rectes = "\n".join(fila(rectes_d(t, f"Dues rectes {t}", marca=True, amp=2.6, alt=1.6), n, fr) for t, n, fr in RECTES)

cara1 = f'''<div class="full targeta">
  <h1 class="cara-titol">Angles i rectes</h1>
  <p style="font-size:15.5pt;margin:0 0 .2cm">La cantonada d'un quadret és l'<b>angle recte</b>. Els altres angles es comparen amb la cantonada.</p>
  <table style="border-collapse:collapse;width:auto">
{angles}
  </table>
  <p style="font-size:14.5pt;margin:.15cm 0 0">Els costats llargs o curts no canvien l'angle.</p>
  <h2 style="font-size:16pt;margin:.4cm 0 .1cm">Les peces</h2>
  <table style="border-collapse:collapse;width:auto">
{peces}
  </table>
  <h2 style="font-size:16pt;margin:.35cm 0 .1cm">Dues rectes</h2>
  <table style="border-collapse:collapse;width:auto">
{rectes}
  </table>
  <div class="pag">Targeta de les formes · cara 1</div>
</div>'''

# ------------------------------------------------------------------ cara 2
NOMS = [(3, "triangle"), (4, "quadrilàter"), (5, "pentàgon"), (6, "hexàgon"), (7, "heptàgon"), (8, "octàgon")]
pols = "".join(f'''<td style="border:0;text-align:center;padding:0 .15rem">{poligon_d(regular(n, 0.62), f"Un {nom}", fons=F2, marge=0.1).svg("")}
      <p style="margin:.05rem 0 0;font-size:14pt"><b>{n}</b><br>{nom}</p></td>''' for n, nom in NOMS)
tri_costats = [([(0, 0), (2, 0), (1, 1.73)], [1, 1, 1], "Equilàter", "3 costats iguals."),
               ([(0, 0), (1.8, 0), (0.9, 1.9)], [0, 1, 1], "Isòsceles", "2 costats iguals."),
               ([(0, 0), (2.2, 0), (0.5, 1.3)], [1, 2, 3], "Escalè", "Cap costat igual.")]
tc = "".join(f'''<td style="border:0;text-align:center;padding:0 .3rem">{triangle_d(p, f"Un triangle {n.lower()}", marques=mq, marge=0.3).svg("")}
      <p style="margin:0;font-size:14pt"><b>{n}</b></p><p style="margin:0;font-size:14pt">{fr}</p></td>''' for p, mq, n, fr in tri_costats)
tri_angles = [([(0, 0), (2, 0), (0, 1.6)], 0, "Rectangle", "Té un angle recte."),
              ([(0, 0), (2, 0), (0.9, 1.6)], None, "Acutangle", "3 angles aguts."),
              ([(0, 0), (2.4, 0), (-0.6, 1.0)], None, "Obtusangle", "Té un angle obtús.")]
ta = "".join(f'''<td style="border:0;text-align:center;padding:0 .3rem">{triangle_d(p, f"Un triangle {n.lower()}", cantonada_a=c, marge=0.3).svg("")}
      <p style="margin:0;font-size:14pt"><b>{n}</b></p><p style="margin:0;font-size:14pt">{fr}</p></td>''' for p, c, n, fr in tri_angles)

cara2 = f'''<div class="full targeta">
  <h1 class="cara-titol">Polígons i triangles</h1>
  <p style="font-size:15pt;margin:0 0 .1cm">El nom diu quants costats té. Té tants vèrtexs com costats.</p>
  <table style="border-collapse:collapse;width:auto;margin:0 auto"><tr>
    {pols}
  </tr></table>
  <p style="font-size:14.5pt;margin:.2cm 0 0"><b>Regular:</b> tots els costats i tots els angles són iguals. <b>Còncau:</b> té una cantonada cap endins.</p>
  <h2 style="font-size:16pt;margin:.35cm 0 .05cm">Els triangles, pels costats</h2>
  <table style="border-collapse:collapse;width:auto;margin:0 auto"><tr>{tc}</tr></table>
  <h2 style="font-size:16pt;margin:.3cm 0 .05cm">Els triangles, pels angles</h2>
  <table style="border-collapse:collapse;width:auto;margin:0 auto"><tr>{ta}</tr></table>
  <section class="clau" style="margin-top:.35cm">
    <p>Els tres angles d'un triangle, junts, fan un <b>angle pla</b>: 180°.</p>
    <p><b>Perímetre:</b> la vora, la suma de tots els costats.</p>
    <p style="margin:0"><b>Circumferència:</b> el diàmetre és el doble del radi. La vora fa una mica més de 3 vegades el diàmetre.</p>
  </section>
  <section class="diu">
    <h2>Com ho dic</h2>
    <p>«Aquest angle és més petit que la cantonada: és agut.»</p>
    <p>«El perímetre és la vora. L'àrea són els quadrets de dins.»</p>
  </section>
  <div class="pag">Targeta de les formes · cara 2</div>
</div>'''

cap = '''<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Formes · targeta de consulta</title>
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
</head>
<body>
<!--
  TARGETA DE CONSULTA · Formes
  La quarta targeta, de la unitat 6 (pla validat pel docent el 29/9/2026). S'imprimeix a doble
  cara, girant per la vora llarga, i es plastifica. Cara 1: angles i rectes, amb la cantonada del
  quadret. Cara 2: polígons, triangles, el perímetre i la circumferència.

  Surt de generadors/fitxes/targeta_formes.py: si s'hi ha de canviar res, es canvia allà i es torna
  a generar. Després, eines/comprova.py i el PDF amb generadors/gen_pdf.py.
-->

'''
html = cap + cara1 + "\n\n" + cara2 + "\n\n</body>\n</html>\n"
sortida = sys.argv[1] if len(sys.argv) > 1 else "formes.html"
open(sortida, "w", encoding="utf-8").write(html)
print(sortida)
