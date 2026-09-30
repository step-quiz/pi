#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud6.html: punts, rectes i angles (unitat 6, fitxa 1).

Adapta les activitats 2 i 3 de la situació «Sentit espacial» (el llibre, UD6: «Les peces bàsiques
de la geometria» i «Angles»). La cantonada d'un quadret, o d'un full, és l'angle recte: un angle agut
és més petit, un obtús és més gran i un de pla és una recta. Sense transportador (decisió del docent
del 29/9/2026). Els casos són els del llibre (l'estrella, la regla, la llanterna; 88° que sembla
recte; el rellotge) i els de la tasca 22 de la caixa.

La regla trencada (regla G): «costats més llargs, angle més gran» (pàgina 5).
"""
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
from peces_comunes import *  # noqa: F401,F403
from peces_ud2 import *  # noqa: F401,F403
from peces_fraccions import *  # noqa: F401,F403
from peces_geo import *  # noqa: F401,F403

pagines = []
pagina = fes_pagina(pagines, "Unitat 6 · Punts, rectes i angles · pàgina")
NOMS = ["Agut", "Recte", "Obtús", "Pla"]
nom_de = lambda g: "Agut" if g < 90 else "Recte" if g == 90 else "Obtús" if g < 180 else "Pla"

# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>un full de paper</b>. Doblegar-lo dues vegades: la cantonada és l'angle recte. Comparar-la amb angles de la classe.</div>
  <h1>Punts, rectes i angles</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:.8rem">
{angle_d(55, "Un angle, amb la cantonada d'un quadret al vèrtex", llarg=3.4).svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .5rem">La línia discontínua és la cantonada d'un quadret.</p>
  <table>
    <tr class="resolt"><td class="esq">L'angle és més petit que la cantonada?</td><td style="width:4cm">{ms("Sí")}</td></tr>
    <tr class="resolt"><td class="esq">Com es diu?</td><td>{ms("Agut")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">La cantonada d'un quadret és l'angle recte.</p>
    <p style="margin:.2rem 0 0">Més petit: <b>agut</b>. Igual: <b>recte</b>. Més gran: <b>obtús</b>. Una recta: <b>pla</b>.</p>
  </div>''')

# ===================================================================== pàgina 2: les peces
E1 = [("a", "segment", True), ("b", "recta", False), ("c", "semirecta", False), ("d", "punt", False)]
it = []
for l, t, r in E1:
    # Les quatre opcions, en una sola fila (nowrap): amb la lletra a 14 pt, la peça i els
    # espais s'estrenyen perquè «Semirecta» hi càpiga. Si passaven a una segona fila, la
    # pàgina no cabia en un A4 (29/9/2026).
    it.append(caixa(f'''      <div style="display:flex;gap:.25cm;align-items:center">
        <p class="apartat" style="margin:0">{l})</p>
        <div style="width:1.6cm">{peca_linia(t, f"Apartat {l}: una peça per dir-ne el nom", amp=1.6).svg("")}</div>
        <div style="flex:1;min-width:0">{tria(["Punt", "Segment", "Semirecta", "Recta"], t.capitalize() if r else None, mida="14pt", ample="2cm", ajusta=True).replace("flex-wrap:wrap", "flex-wrap:nowrap")}</div>
      </div>''', r, ".25rem"))
OBJ = [("a", "Una estrella al cel", "Punt", True), ("b", "La vora d'una regla", "Segment", False),
       ("c", "La llum d'una llanterna", "Semirecta", False), ("d", "La vora d'una taula", "Segment", False)]
it2 = []
for l, t, bona, r in OBJ:
    it2.append(caixa(f'''      <p style="margin:0 0 .1rem"><span class="apartat">{l})</span> {t}</p>
      {tria(["Punt", "Segment", "Semirecta"], bona if r else None, mida="14pt", ample="2.8cm")}''', r, ".25rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Com es diu cada dibuix? Mira la targeta.</div></div>
{chr(10).join(it)}
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">A què s'assembla més? Marca la resposta.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it2)}
    </div>
  </div>''')

# ===================================================================== pàgina 3: dues rectes
E3 = [("a", "perpendiculars", True), ("b", "paral·leles", False), ("c", "secants", False), ("d", "perpendiculars", False)]
it = []
for l, t, r in E3:
    # Les rectes, a 2 cm i no a 3: amb la lletra a 14 pt, «Perpendiculars» fa la capsa més
    # ampla, i la columna de la dreta sortia del full (29/9/2026).
    it.append(caixa(f'''      <div style="display:flex;gap:.3cm;align-items:center">
        <p class="apartat" style="margin:0">{l})</p>
        <div style="width:2cm">{rectes_d(t, f"Apartat {l}: dues rectes", marca=False, amp=2.0, alt=1.5).svg("")}</div>
        <div>{tria(["Paral·leles", "Secants", "Perpendiculars"], t.capitalize() if r else None, mida="14pt", ample="3.4cm", columna=True)}</div>
      </div>''', r, ".25rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Com són les dues rectes? Posa la cantonada d'un full on es tallen.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Si es tallen i fan una cantonada, són perpendiculars.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 4: quin angle és
E4 = [("a", 40, True), ("b", 125, False), ("c", 90, False), ("d", 180, False), ("e", 80, False), ("f", 150, False)]
it = []
for l, g, r in E4:
    it.append(caixa(f'''      <div style="display:flex;gap:.4cm;align-items:center">
        <p class="apartat" style="margin:0">{l})</p>
        <div style="width:3.6cm;display:flex;justify-content:center">{angle_d(g, f"Apartat {l}: un angle, amb la cantonada al vèrtex", llarg=1.6).svg("")}</div>
        <div>{tria(NOMS, nom_de(g) if r else None, mida="14pt", ample="2.4cm")}</div>
      </div>''', r, ".25rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Quin angle és? Mira la cantonada discontínua.</div></div>
{chr(10).join(it)}
  </div>''')

# ===================================================================== pàgina 5: la regla trencada
E5 = [("a", (45, 2.4), (120, 1.0), "Angle 2", True), ("b", (90, 2.4), (90, 1.0), "Iguals", False),
      ("c", (60, 1.0), (30, 2.4), "Angle 1", False), ("d", (150, 1.0), (130, 2.0), "Angle 1", False)]
it = []
for l, (g1, l1), (g2, l2), bona, r in E5:
    it.append(caixa(f'''      <p style="margin:0 0 .1rem;font-size:15pt;font-weight:700"><span class="apartat">{l})</span> Quin angle és més gran?</p>
      <div style="display:flex;gap:.3cm;align-items:center">
        <div style="display:flex;gap:.3cm;align-items:flex-end">
          <div><p style="margin:0;font-weight:800;font-size:16pt">1</p>{angle_d(g1, "L'angle 1", llarg=l1 * 0.7, cantonada=False).svg("")}</div>
          <div><p style="margin:0;font-weight:800;font-size:16pt">2</p>{angle_d(g2, "L'angle 2", llarg=l2 * 0.7, cantonada=False).svg("")}</div>
        </div>
        <div>{tria(["Angle 1", "Angle 2", "Iguals"], bona if r else None, mida="14pt", ample="2.6cm", columna=True)}</div>
      </div>''', r, ".25rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">En Marc diu que l'angle amb els costats més llargs és el més gran. Té raó?</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Mira quant s'obre, no quant fan els costats.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Els costats llargs o curts no canvien l'angle.</p>
    <p style="margin:.2rem 0 0">Un angle és més gran quan s'obre més.</p>
  </div>''')

# ===================================================================== pàgina 6: la vida (el rellotge)
V = [("a", 3, "Recte", True), ("b", 6, "Pla", False), ("c", 1, "Agut", False), ("d", 5, "Obtús", False)]
it = []
for l, h, bona, r in V:
    it.append(caixa(f'''      <p style="margin:0 0 .1rem"><span class="apartat">{l})</span> Les {h} en punt</p>
      <div style="display:flex;gap:.5cm;align-items:center">
        <div style="width:3cm">{rellotge(h, f"Un rellotge a les {h} en punt").svg("")}</div>
        <div>{tria(NOMS, bona if r else None, mida="14pt", ample="1.8cm", columna=True)}</div>
      </div>''', r, ".3rem"))
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">6</div><div class="q">Les dues agulles del rellotge fan un angle. Quin angle és?</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 6 · Punts, rectes i angles · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> La cantonada d'un quadret, o d'un full, és l'angle recte, i la resta
    d'angles es comparen amb ella. Sense transportador: els graus (90° i 180°) només surten com a nom,
    a la targeta «Formes». Els dibuixos porten la cantonada discontínua al vèrtex, com a la caixa
    (tasca 22).
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb un full: doblegar-lo per la meitat i una altra vegada. La cantonada que surt és
  un angle recte. Posar-la a la cantonada de la taula, a la porta i a la tisora oberta: igual, més
  gran o més petit.</p>
  <h3>1 i 2. Les peces</h3>
  <p>1b) recta; c) semirecta; d) punt. 2b) segment; c) semirecta (comença a la llanterna i no
  s'acaba); d) segment. Són els casos del llibre. <b>Error típic:</b> dir recta a un segment: la
  recta no té extrems.</p>
  <h3>3. Dues rectes</h3>
  <p>b) paral·leles; c) secants; d) perpendiculars. Amb la cantonada del full: si encaixa on es tallen,
  són perpendiculars.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>4. Quin angle és</h3>
  <p>b) obtús; c) recte; d) pla; e) agut; f) obtús. L'apartat e (80°) sembla recte: és el cas de 88°
  del llibre. Amb la cantonada al vèrtex es veu que és una mica més petit.</p>
  <h3>5. En Marc · la regla trencada</h3>
  <p>b) iguals (dos angles rectes); c) l'angle 1; d) l'angle 1. <b>Error típic:</b> triar l'angle amb els
  costats més llargs, que és el que fa en Marc. És la regla trencada d'aquesta fitxa. No l'expliqueu:
  que posi la cantonada del full a cada angle, o que allargui els costats curts amb un regle. A la
  caixa (22.1), el comptador dels costats ho ensenya. <b>Compta per als nivells alts, no per al mínim.</b></p>
  <h3>6. A la vida de cada dia · el rellotge</h3>
  <p>b) pla; c) agut; d) obtús. És el rellotge del llibre. Les 9 en punt també fan un angle recte.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=22</b> (22.1 Obre l'angle;
  22.2 Quin angle és?). La 22.2 dona un codi de verificació. L'exemple de la fitxa és el de la caixa:
  un angle agut amb la cantonada al vèrtex.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta «Formes» o la cantonada d'un full al davant. Els criteris de la SA del grup
  (1.1, 3.1, 5.1, 6.1, 7.1 i 9.1) són de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb la cantonada d'un full, diu si un angle és més petit, igual o més gran que el recte.</li>
    <li>Diu el nom de les peces bàsiques: punt, segment, semirecta i recta (exercicis 1 i 2).</li>
    <li>Diu si dues rectes són paral·leles, secants o perpendiculars (exercici 3).</li>
    <li>Diu si un angle és agut, recte, obtús o pla (exercicis 4 i 6).</li>
    <li>Nivells alts: diu per què la llargada dels costats no canvia l'angle (exercici 5).</li>
  </ul>
</div>''')

document("Unitat 6 · Punts, rectes i angles", """  FITXA · Unitat 6 · Sentit espacial · Punts, rectes i angles
  La primera fitxa de la unitat 6. Adapta les activitats 2 i 3 de la situació (el
  llibre, UD6: les peces bàsiques i els angles). La cantonada d'un quadret és
  l'angle recte, i la resta d'angles es comparen amb ella: sense transportador.
  Els casos són els del llibre i els de la tasca 22 de la caixa (regla 8).

  La regla trencada és «costats més llargs, angle més gran»: en Marc, pàgina 5.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud6.html")
