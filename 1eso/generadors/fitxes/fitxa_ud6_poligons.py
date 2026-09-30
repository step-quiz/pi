#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud6-poligons.html: els polígons (unitat 6, fitxa 2).

Adapta l'activitat 4 de la situació «Sentit espacial» (el llibre, UD6: «Polígons»). Els polígons al
geoplà: quants costats i quants vèrtexs tenen, com es diuen, si són regulars i si són còncaus. Els
casos són els del llibre (els noms de 3, 5, 8 i 6 costats; el quadrat, el rectangle i el triangle
equilàter, regulars o no; l'error de la Irene: un hexàgon amb 5 vèrtexs) i els de la tasca 23.

La regla trencada (regla G): «un quadrat girat ja no és un quadrat» (pàgina 4).
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
from peces_comunes import *  # noqa: F401,F403
from peces_ud2 import *  # noqa: F401,F403
from peces_fraccions import *  # noqa: F401,F403
from peces_geo import *  # noqa: F401,F403

pagines = []
pagina = fes_pagina(pagines, "Unitat 6 · Polígons · pàgina")
NOM = {3: "triangle", 4: "quadrilàter", 5: "pentàgon", 6: "hexàgon", 7: "heptàgon", 8: "octàgon"}
PENTAGON = [[2, 0], [5, 2], [4, 5], [1, 5], [0, 2]]

# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>el geoplà i gomes elàstiques</b>. Fer un triangle i un quadrat. Comptar els costats i els vèrtexs.</div>
  <h1>Polígons</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:.8rem;width:6cm;margin-left:auto;margin-right:auto">
{geopla_d(PENTAGON, "Un pentàgon al geoplà", m=1.0).svg()}
  </div>
  <table style="margin-top:.5rem">
    <tr class="resolt"><td class="esq">Quants costats té?</td><td style="width:4cm">{ms("5")}</td></tr>
    <tr class="resolt"><td class="esq">Quants vèrtexs té?</td><td>{ms("5")}</td></tr>
    <tr class="resolt"><td class="esq">Com es diu?</td><td>{ms("Pentàgon")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Un polígon té tants vèrtexs com costats.</p>
    <p style="margin:.2rem 0 0">El nom diu quants costats té: el pentàgon en té 5.</p>
  </div>''')

# ===================================================================== pàgina 2: compta i escriu el nom
E1 = [("a", [[1, 0], [4, 0], [5, 2], [4, 4], [1, 4], [0, 2]], True), ("b", [[0, 5], [5, 5], [2, 0]], False),
      ("c", [[0, 1], [5, 1], [5, 4], [0, 4]], False), ("d", PENTAGON, False)]
it = []
for l, pts, r in E1:
    n = len(pts)
    it.append(caixa(f'''      <div style="display:flex;gap:.5cm;align-items:center">
        <p class="apartat" style="margin:0">{l})</p>
        <div style="width:3.2cm">{geopla_d(pts, f"Apartat {l}: un polígon al geoplà", m=0.55).svg("")}</div>
        <div>
          <p class="frase" style="margin:0;font-size:15pt">Costats: {ms(str(n)) if r else buit_curt()}</p>
          <p class="frase" style="margin:0;font-size:15pt">Nom: {ms(NOM[n]) if r else buit()}</p>
        </div>
      </div>''', r, ".3rem"))
N2 = [("a", 3, True), ("b", 5, False), ("c", 8, False), ("d", 6, False)]
it2 = "".join(f'''<tr{' class="resolt"' if r else ''}><td class="apartat" style="text-align:center">{l})</td><td style="text-align:center;font-size:17pt;font-weight:800">{n}</td>
        <td style="text-align:center">{ms(NOM[n]) if r else ""}</td><td style="text-align:center">{ms(str(n)) if r else ""}</td></tr>''' for l, n, r in N2)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Compta els costats de cada polígon. Escriu el nom. Mira la targeta.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Escriu el nom i quants vèrtexs té.</div></div>
    <table class="mini">
      <tr><th style="width:1.4cm"></th><th>Costats</th><th>Nom</th><th>Vèrtexs</th></tr>
      {it2}
    </table>
  </div>''')

# ===================================================================== pàgina 3: regular o no, còncau o no
REG = [("a", poligon_d([(0, 0), (1.8, 0), (1.8, 1.8), (0, 1.8)], "Apartat a: un quadrat"), "Regular", True),
       ("b", poligon_d([(0, 0), (3, 0), (3, 1.5), (0, 1.5)], "Apartat b: un rectangle que no és quadrat"), "No regular", False),
       ("c", poligon_d(regular(3, 1.2), "Apartat c: un triangle amb els tres costats iguals"), "Regular", False),
       ("d", poligon_d([(0, 0), (2.4, 0), (2.8, 1.2), (1.2, 2.0), (0.2, 1.4)], "Apartat d: un pentàgon amb costats diferents"), "No regular", False)]
it = []
for l, dib, bona, r in REG:
    it.append(caixa(f'''      <div style="display:flex;gap:.5cm;align-items:center">
        <p class="apartat" style="margin:0">{l})</p>
        <div style="width:3.2cm;display:flex;justify-content:center">{dib.svg("")}</div>
        <div>{tria(["Regular", "No regular"], bona if r else None, mida="14pt", ample="3cm", columna=True)}</div>
      </div>''', r, ".3rem"))
CON = [("a", [[0, 0], [5, 0], [5, 5], [3, 5], [3, 2], [0, 2]], "Còncau", True), ("b", [[0, 1], [5, 1], [5, 4], [0, 4]], "Convex", False)]
it3 = []
for l, pts, bona, r in CON:
    it3.append(caixa(f'''      <div style="display:flex;gap:.5cm;align-items:center">
        <p class="apartat" style="margin:0">{l})</p>
        <div style="width:3cm">{geopla_d(pts, f"Apartat {l}: un polígon al geoplà", m=0.5).svg("")}</div>
        <div>{tria(["Còncau", "Convex"], bona if r else None, mida="14pt", ample="2.6cm", columna=True)}</div>
      </div>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">És regular? Mira si tots els costats són iguals.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Regular: tots els costats i tots els angles són iguals.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Té alguna cantonada cap endins? Si en té, és còncau.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it3)}
    </div>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
QG = [("a", [[2, 0], [4, 2], [2, 4], [0, 2]], "Sí", True), ("b", [[1, 1], [4, 1], [4, 4], [1, 4]], "Sí", False),
      ("c", [[1, 0], [5, 4], [4, 5], [0, 1]], "No", False), ("d", [[2, 1], [3, 2], [2, 3], [1, 2]], "Sí", False)]
it = []
for l, pts, bona, r in QG:
    it.append(caixa(f'''      <div style="display:flex;gap:.5cm;align-items:center">
        <p class="apartat" style="margin:0">{l})</p>
        <div style="width:3.2cm">{geopla_d(pts, f"Apartat {l}: un quadrilàter al geoplà", m=0.55).svg("")}</div>
        <div><p style="margin:0 0 .1rem;font-size:15pt">És un quadrat?</p>{tria(["Sí", "No"], bona if r else None, mida="14pt", ample="2.2cm", columna=True)}</div>
      </div>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">En Nil diu que un quadrat girat ja no és un quadrat. Té raó?</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Un quadrat té 4 costats iguals i 4 cantonades. Gira el full i mira el dibuix.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Un quadrat girat també és un quadrat.</p>
    <p style="margin:.2rem 0 0">Té 4 costats iguals i 4 cantonades. Està girat, però és el mateix quadrat.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
V = [("a", "Un senyal de stop", poligon_d(regular(8, 1.2), "Un senyal de stop, amb 8 costats"), 8, True),
     ("b", "Un senyal de perill", poligon_d(regular(3, 1.3), "Un senyal de perill, amb 3 costats"), 3, False),
     ("c", "Una porta", poligon_d([(0, 0), (1.4, 0), (1.4, 2.6), (0, 2.6)], "Una porta, amb 4 costats"), 4, False),
     ("d", "Una peça d'una pilota", poligon_d(regular(6, 1.2), "Una peça d'una pilota, amb 6 costats"), 6, False)]
it = []
for l, t, dib, n, r in V:
    it.append(caixa(f'''      <p style="margin:0 0 .1rem"><span class="apartat">{l})</span> {t}</p>
      <div style="display:flex;gap:.5cm;align-items:center">
        <div style="width:3cm;display:flex;justify-content:center">{dib.svg("")}</div>
        <p class="frase" style="margin:0;font-size:15pt">{ms(NOM[n]) if r else buit()}</p>
      </div>''', r, ".3rem"))
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">6</div><div class="q">Quin polígon és? Compta els costats i escriu el nom.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 6 · Polígons · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Els polígons es fan al geoplà, com a la caixa (tasca 23). Es compten
    els costats posant el dit a un vèrtex i donant tota la volta. Els noms de 3 a 8 costats són a la
    targeta «Formes»: no es demanen de memòria.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb el geoplà i gomes: fer un triangle i un quadrat, i comptar costats i vèrtexs.
  Si no hi ha geoplà, serveix un full de punts.</p>
  <h3>1 i 2. Els noms</h3>
  <p>1b) 3, triangle; c) 4, quadrilàter; d) 5, pentàgon. 2b) pentàgon, 5; c) octàgon, 8; d) hexàgon,
  6 (els casos del llibre). <b>Error típic:</b> comptar un vèrtex menys, com la Irene del llibre (un
  hexàgon amb 5 vèrtexs): el polígon sempre té tants vèrtexs com costats.</p>
  <h3>3 i 4. Regular, còncau</h3>
  <p>3b) no regular: els costats no són iguals; c) regular; d) no regular. 4b) convex. Són els casos
  del llibre.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>5. En Nil · la regla trencada</h3>
  <p>b) Sí; c) No: té 4 cantonades, però dos costats són molt més llargs (és un rectangle girat); d) Sí.
  <b>Error típic:</b> dir que un quadrat girat ja no és un quadrat, com en Nil. És la regla trencada
  d'aquesta fitxa. No l'expliqueu: que giri el full fins que el quadrat quedi recte. L'apartat c és a
  posta: girat, tampoc no és un quadrat, perquè no ho era. <b>Compta per als nivells alts, no per al
  mínim.</b></p>
  <h3>6. A la vida de cada dia</h3>
  <p>b) triangle; c) quadrilàter (un rectangle); d) hexàgon.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=23</b> (23.1 El polígon al
  geoplà; 23.2 Com es diu?). La 23.2 dona un codi de verificació, i sempre hi surten el quadrat girat
  i un polígon còncau.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta «Formes» al davant. Els criteris de la SA del grup (1.1, 3.1, 5.1, 6.1, 7.1
  i 9.1) són de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb el geoplà, fa un polígon i en compta els costats i els vèrtexs.</li>
    <li>Diu el nom d'un polígon de 3 a 8 costats amb la targeta (exercicis 1, 2 i 6).</li>
    <li>Diu si un polígon és regular i si és còncau (exercicis 3 i 4).</li>
    <li>Nivells alts: reconeix un quadrat girat (exercici 5).</li>
  </ul>
</div>''')

document("Unitat 6 · Polígons", """  FITXA · Unitat 6 · Sentit espacial · Polígons
  La segona fitxa de la unitat 6. Adapta l'activitat 4 de la situació (el llibre,
  UD6: «Polígons»): costats, vèrtexs, noms, regulars i còncaus, al geoplà. Els
  casos són els del llibre i els de la tasca 23 de la caixa (regla 8).

  La regla trencada és «un quadrat girat ja no és un quadrat»: en Nil, pàgina 4.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud6-poligons.html")
