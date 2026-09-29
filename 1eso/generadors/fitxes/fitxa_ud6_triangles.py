#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud6-triangles.html: els triangles (unitat 6, fitxa 3).

Adapta l'activitat 5 de la situació «Sentit espacial» (el llibre, UD6: «Triangles»). Els tres angles
d'un triangle, junts, fan un angle pla: el grup ho fa retallant cartolines. Els triangles es diuen
pels costats (equilàter, isòsceles, escalè: les ratlletes marquen els costats iguals) i pels angles
(rectangle, acutangle, obtusangle: amb la cantonada d'un quadret). Els casos són els del llibre
(costats 4-4-4, 5-5-8 i 3-4-6; el senyal de perill) i els de la tasca 24 de la caixa.

La regla trencada (regla G): «un triangle més gran té els angles més grans» (pàgina 4).
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(AQUI, "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(AQUI, "peces_ud2.py"), encoding="utf-8").read())
exec(open(os.path.join(AQUI, "peces_fraccions.py"), encoding="utf-8").read())
exec(open(os.path.join(AQUI, "peces_geo.py"), encoding="utf-8").read())

pagines = []
pagina = fes_pagina(pagines, "Unitat 6 · Triangles · pàgina")
escala = lambda pts, k: [(x * k, y * k) for x, y in pts]
EQUI = regular(3, 1.3)
ISO = [(0, 0), (2.0, 0), (1.0, 2.2)]
ESC = [(0, 0), (2.6, 0), (0.7, 1.5)]
ISO_G = [(0, 0), (2, 1), (1, 2)]
RECT = [(0, 0), (2.4, 0), (0, 1.8)]
OBT = [(0, 0), (2.8, 0), (-0.7, 1.2)]
ACU = [(0, 0), (2.2, 0), (1.0, 1.9)]
RECT_G = [(0, 1), (1.5, 0), (2.5, 1.5)]

# ===================================================================== pàgina 1
T1 = [(0, 0), (5.0, 0), (1.7, 3.6)]
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>un triangle de cartolina</b>. Pintar els tres angles, retallar-los i posar-los junts: fan una recta.</div>
  <h1>Triangles</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div style="display:flex;gap:1cm;justify-content:center;align-items:flex-end;margin-top:.6rem">
    <div>{triangle_d(T1, "Un triangle amb els tres angles numerats", arcs=True).svg("")}</div>
    <div>{junts_d(angles_de(T1), "Els tres angles, junts, fan un angle pla", r=2.4).svg("")}</div>
  </div>
  <table style="margin-top:.5rem">
    <tr class="resolt"><td class="esq">Quants angles té el triangle?</td><td style="width:4.4cm">{ms("3")}</td></tr>
    <tr class="resolt"><td class="esq">Junts, què fan?</td><td>{ms("Un angle pla")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Els tres angles d'un triangle, junts, fan un angle pla.</p>
    <p style="margin:.2rem 0 0">Passa amb tots els triangles, grans i petits.</p>
  </div>''')

# ===================================================================== pàgina 2: pels costats
E1 = [("a", EQUI, [1, 1, 1], "Equilàter", True), ("b", ISO, [0, 1, 1], "Isòsceles", False),
      ("c", ESC, [1, 2, 3], "Escalè", False), ("d", ISO_G, [1, 0, 1], "Isòsceles", False)]
it = []
for l, pts, mq, bona, r in E1:
    it.append(caixa(f'''      <div style="display:flex;gap:.5cm;align-items:center">
        <p class="apartat" style="margin:0">{l})</p>
        <div style="width:3.2cm;display:flex;justify-content:center">{triangle_d(pts, f"Apartat {l}: un triangle amb ratlletes als costats iguals", marques=mq).svg("")}</div>
        <div>{tria(["Equilàter", "Isòsceles", "Escalè"], bona if r else None, mida="13pt", ample="3cm", columna=True)}</div>
      </div>''', r, ".3rem"))
N2 = [("a", "4, 4 i 4", "Equilàter", True), ("b", "5, 5 i 8", "Isòsceles", False), ("c", "3, 4 i 6", "Escalè", False)]
files = "".join(f'''<tr{' class="resolt"' if r else ''}><td class="apartat" style="text-align:center">{l})</td><td style="text-align:center;font-size:17pt;font-weight:800">{c}</td><td style="text-align:center">{ms(b) if r else ""}</td></tr>''' for l, c, b, r in N2)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Mira les ratlletes: marquen els costats iguals. Com es diu el triangle?</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Els costats fan aquests centímetres. Com es diu el triangle?</div></div>
    <table class="mini">
      <tr><th style="width:1.4cm"></th><th>Els tres costats</th><th>El triangle</th></tr>
      {files}
    </table>
  </div>''')

# ===================================================================== pàgina 3: pels angles
E3 = [("a", RECT, 0, "Rectangle", True), ("b", OBT, None, "Obtusangle", False),
      ("c", ACU, None, "Acutangle", False), ("d", RECT_G, None, "Rectangle", False)]
it = []
for l, pts, c, bona, r in E3:
    it.append(caixa(f'''      <div style="display:flex;gap:.5cm;align-items:center">
        <p class="apartat" style="margin:0">{l})</p>
        <div style="width:3.4cm;display:flex;justify-content:center">{triangle_d(pts, f"Apartat {l}: un triangle", cantonada_a=c).svg("")}</div>
        <div>{tria(["Rectangle", "Acutangle", "Obtusangle"], bona if r else None, mida="13pt", ample="3.2cm", columna=True)}</div>
      </div>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Posa la cantonada d'un full a cada angle. Com es diu el triangle?</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Un angle igual que la cantonada: rectangle. Un de més gran: obtusangle. Tots més petits: acutangle.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
P4 = [("a", RECT, escala(RECT, 1.4), "Iguals", True), ("b", ACU, escala(ACU, 1.4), "Iguals", False),
      ("c", ACU, OBT, "Diferents", False), ("d", escala(OBT, 0.75), escala(OBT, 1.2), "Iguals", False)]
it = []
for l, t1, t2, bona, r in P4:
    it.append(caixa(f'''      <p style="margin:0 0 .1rem;font-size:15pt;font-weight:700"><span class="apartat">{l})</span> Els angles dels dos triangles són…</p>
      <div style="display:flex;gap:.5cm;align-items:center">
        <div style="display:flex;gap:.3cm;align-items:flex-end">
          <div>{triangle_d(t1, "El primer triangle", arcs=True, marge=0.3).svg("")}</div>
          <div>{triangle_d(t2, "El segon triangle", arcs=True, marge=0.3).svg("")}</div>
        </div>
        <div>{tria(["Iguals", "Diferents"], bona if r else None, mida="13pt", ample="2.6cm", columna=True)}</div>
      </div>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">En Pau diu que el triangle gran té els angles més grans. Té raó?</div></div>
{chr(10).join(it)}
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">La mida no canvia els angles.</p>
    <p style="margin:.2rem 0 0">Un triangle gran i un de petit amb la mateixa forma tenen els mateixos angles.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
V = [("a", "Un senyal de perill", EQUI, [1, 1, 1], "Equilàter", "Acutangle", True),
     ("b", "Un escaire", [(0, 0), (2.2, 0), (0, 2.2)], [1, 0, 1], "Isòsceles", "Rectangle", False),
     ("c", "Un tros de pizza", [(0, 0), (1.4, 0), (0.7, 2.6)], [0, 1, 1], "Isòsceles", "Acutangle", False),
     ("d", "Una rampa", [(0, 0), (3.0, 0), (3.0, 1.2)], [1, 2, 3], "Escalè", "Rectangle", False)]
files = "".join(f'''<tr{' class="resolt"' if r else ''}><td class="apartat" style="padding:.2rem .4rem">{l}) {t}</td>
        <td style="text-align:center;padding:.15rem">{triangle_d(p, t, marques=mq, marge=0.25).svg("")}</td>
        <td style="text-align:center">{ms(c) if r else ""}</td><td style="text-align:center">{ms(a) if r else ""}</td></tr>''' for l, t, p, mq, c, a, r in V)
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Quin triangle és, pels costats i pels angles? Mira la targeta.</div></div>
    <table class="mini">
      <tr><th style="width:4.4cm"></th><th>El dibuix</th><th>Pels costats</th><th>Pels angles</th></tr>
      {files}
    </table>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 6 · Triangles · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Els tres angles d'un triangle, junts, fan un angle pla: és l'activitat
    del grup amb cartolines, i la tasca 24 de la caixa. Els triangles es diuen pels costats (les
    ratlletes marquen els iguals) i pels angles (amb la cantonada d'un full). Tots els noms són a la
    targeta «Formes». Sense graus: 180° només surt com a nom.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb un triangle de cartolina: pintar-ne els angles de tres colors, retallar-los i
  posar-los junts. Fan una recta. Si cada alumne en fa un de diferent, es veu que passa amb tots.</p>
  <h3>1 i 2. Pels costats</h3>
  <p>1b) isòsceles; c) escalè; d) isòsceles (girat). 2b) isòsceles; c) escalè (els casos del
  llibre). <b>Error típic:</b> dir equilàter a qualsevol triangle «que sembla igual»: cal mirar les
  ratlletes.</p>
  <h3>3. Pels angles</h3>
  <p>b) obtusangle; c) acutangle; d) rectangle (girat: l'angle recte no és a baix). Amb la cantonada
  del full a cada angle es veu sense graus.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>4. En Pau · la regla trencada</h3>
  <p>b) iguals; c) diferents: no tenen la mateixa forma; d) iguals. <b>Error típic:</b> «un triangle
  més gran té els angles més grans», com en Pau. És la regla trencada d'aquesta fitxa. No l'expliqueu:
  que posi la cantonada del full a l'angle recte de tots dos (apartat a), o que retalli dos triangles
  de la mateixa forma i en compari els angles. L'apartat c és a posta: si la forma canvia, els angles
  també. <b>Compta per als nivells alts, no per al mínim.</b></p>
  <h3>5. A la vida de cada dia</h3>
  <p>b) isòsceles, rectangle; c) isòsceles, acutangle; d) escalè, rectangle. El senyal de perill és el
  repte del llibre.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=24</b> (24.1 Els tres
  angles; 24.2 Quin triangle és?). La 24.2 dona un codi de verificació, i sempre hi surt un rectangle
  girat. A la 24.1 hi ha un triangle petit i un de gran: tenen la mateixa suma.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta «Formes» o la cantonada d'un full al davant. Els criteris de la SA del grup
  (1.1, 3.1, 5.1, 6.1, 7.1 i 9.1) són de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb un triangle de cartolina, posa els tres angles junts i diu que fan un angle pla.</li>
    <li>Diu si un triangle és equilàter, isòsceles o escalè, amb les ratlletes o les mesures (exercicis 1 i 2).</li>
    <li>Diu si un triangle és rectangle, acutangle o obtusangle, amb la cantonada (exercici 3).</li>
    <li>Nivells alts: diu per què la mida no canvia els angles (exercici 4).</li>
  </ul>
</div>''')

document("Unitat 6 · Triangles", """  FITXA · Unitat 6 · Sentit espacial · Triangles
  La tercera fitxa de la unitat 6. Adapta l'activitat 5 de la situació (el llibre,
  UD6: «Triangles»): els tres angles junts fan un angle pla; els triangles pels
  costats i pels angles. Els casos són els del llibre i els de la tasca 24 de la
  caixa (regla 8).

  La regla trencada és «un triangle més gran té els angles més grans»: en Pau,
  pàgina 4.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud6-triangles.html")
