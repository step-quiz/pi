#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud6-cercle.html: la circumferència (unitat 6, fitxa 5).

Adapta l'activitat de la circumferència de la situació «Sentit espacial» (el llibre, UD7, activitat
6). Només la idea, sense π = 3,14 (decisió del docent del 29/9/2026): el centre, el radi i el
diàmetre, que és el doble del radi (unitat 4); i la vora, que fa una mica més de 3 vegades el
diàmetre, com amb el cordill de la programació. Els casos: la roda de bicicleta de 70 cm i l'error de
la Nerea del llibre (fer servir el radi en lloc del diàmetre).

La regla trencada (regla G): «la vora fa 3 vegades el radi» (pàgina 4).
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
from peces_comunes import *  # noqa: F401,F403
from peces_ud2 import *  # noqa: F401,F403
from peces_fraccions import *  # noqa: F401,F403
from peces_geo import *  # noqa: F401,F403

pagines = []
pagina = fes_pagina(pagines, "Unitat 6 · La circumferència · pàgina")

# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>un cordill i una tapa rodona</b>. Resseguir la vora amb el cordill i posar-lo sobre el diàmetre: hi cap 3 vegades i una mica.</div>
  <h1>La circumferència</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:.8rem">
{cercle_d(2.0, "Una circumferència amb el centre, un radi de 2 cm i un diàmetre de 4 cm", radi=True, diametre=True, rot_radi="2 cm", rot_diam="4 cm").svg()}
  </div>
  <table style="margin-top:.4rem">
    <tr class="resolt"><td class="esq">Quant mesura el radi, del centre a la vora?</td><td style="width:4cm">{ms("2 cm")}</td></tr>
    <tr class="resolt"><td class="esq">Quant mesura el diàmetre, d'una vora a l'altra?</td><td>{ms("4 cm")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">El diàmetre és el doble del radi.</p>
    <p style="margin:.2rem 0 0">La vora fa una mica més de 3 vegades el diàmetre.</p>
  </div>''')

# ===================================================================== pàgina 2: les parts
E1 = [("a", cercle_d(1.2, "Apartat a: una circumferència amb una línia del centre a la vora", radi=True), "Radi", True),
      ("b", cercle_d(1.2, "Apartat b: una circumferència amb una línia d'una vora a l'altra pel centre", diametre=True, centre=False), "Diàmetre", False),
      ("c", cercle_d(1.2, "Apartat c: una circumferència amb un punt al mig"), "Centre", False),
      ("d", cercle_d(1.2, "Apartat d: una circumferència amb la vora gruixuda", centre=False, vora=True), "Circumferència", False)]
it = []
for l, dib, bona, r in E1:
    it.append(caixa(f'''      <div style="display:flex;gap:.5cm;align-items:center">
        <p class="apartat" style="margin:0">{l})</p>
        <div>{dib.svg("")}</div>
        <div style="flex:1;min-width:0">{tria(["Centre", "Radi", "Diàmetre", "Circumferència"], bona if r else None, mida="14pt", ample="2.4cm", ajusta=True)}</div>
      </div>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Com es diu el que està marcat? Mira la targeta.</div></div>
{chr(10).join(it)}
  </div>''')

# ===================================================================== pàgina 3: radi i diàmetre
E2 = [("a", 3, None, True), ("b", 5, None, False), ("c", None, 8, False), ("d", None, 70, False)]
files = []
for l, rr, dd, res in E2:
    if rr:
        dada = f'<td style="text-align:center;font-size:17pt;font-weight:800">{rr} cm</td>' + (f'<td style="text-align:center">{ms(f"{2 * rr} cm")}</td>' if res else '<td class="omplir"></td>')
    else:
        dada = '<td class="omplir"></td>' + f'<td style="text-align:center;font-size:17pt;font-weight:800">{dd} cm</td>'
    cls = ' class="resolt"' if res else ""
    files.append(f'<tr{cls}><td class="apartat" style="text-align:center">{l})</td>{dada}</tr>')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Omple la taula. El diàmetre és el doble del radi.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Del radi al diàmetre: el doble. Del diàmetre al radi: la meitat.</p></div>
    <table class="mini">
      <tr><th style="width:1.4cm"></th><th>El radi</th><th>El diàmetre</th></tr>
      {"".join(files)}
    </table>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
E3 = [("a", 10, 15, "No", "30", True), ("b", 6, 9, "No", "18", False), ("c", 8, 12, "No", "24", False), ("d", 5, 15, "Sí", "15", False)]
it = []
for l, d_, diu, bona, bo_n, r in E3:
    frase = "fa servir el diàmetre" if bona == "Sí" else "fa servir el radi"
    it.append(caixa(f'''      <div style="display:flex;gap:.6cm;align-items:center">
        <div>{cercle_d(0.9, f"Una circumferència de {d_} cm de diàmetre", diametre=True, rot_diam=f"{d_} cm").svg("")}</div>
        <div>
          <p style="margin:0;font-size:15pt;font-weight:700"><span class="apartat">{l})</span> Diàmetre de {d_} cm. La Nerea diu: una mica més de {diu} cm. Té raó?</p>
          <div style="display:flex;gap:.6cm;align-items:center">{tria(["Sí", "No"], bona if r else None, mida="14pt", ample="2cm")}<span class="frase" style="font-size:15pt;line-height:1.4">Una mica més de {ms(bo_n + " cm") if r else buit_curt() + " cm"}</span></div>
        </div>
      </div>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">La Nerea calcula la vora amb el radi. Té raó?</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">La vora fa una mica més de 3 vegades el diàmetre. Mira la targeta.</p></div>
{chr(10).join(it)}
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">La vora fa una mica més de 3 vegades el diàmetre, no el radi.</p>
    <p style="margin:.2rem 0 0">Amb el radi, el cordill només arriba a mitja volta.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
V = [("a", "Un plat de 20 cm de diàmetre.", "El radi fa 10 cm. La vora fa una mica més de 60 cm.", True),
     ("b", "Un got de 8 cm de diàmetre.", "", False),
     ("c", "Un rellotge de paret de 30 cm de diàmetre.", "", False),
     ("d", "Una roda de bicicleta de 70 cm de diàmetre.", "", False)]
it = []
for l, t, res, r in V:
    cos = (f'<p class="frase" style="margin:0;font-size:15pt">{ms(res)}</p>' if r else
           f'<p class="frase" style="margin:0;font-size:15pt">El radi fa {buit_curt()} cm. La vora fa una mica més de {buit_curt()} cm.</p>')
    it.append(caixa(f'''      <p style="margin:0 0 .1rem"><span class="apartat">{l})</span> {t}</p>
      {cos}''', r, ".3rem"))
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Escriu el radi i quant mesura la vora, més o menys.</div></div>
{chr(10).join(it)}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 6 · La circumferència · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Només la idea, sense π = 3,14: el centre, el radi, el diàmetre (el doble
    del radi, com el doble de la unitat 4) i la vora, que fa una mica més de 3 vegades el diàmetre.
    Calcular amb π demana multiplicar decimals, i queda fora. La targeta «Formes» ho porta.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb un cordill i objectes rodons (una tapa, un got): resseguir la vora amb el cordill
  i posar-lo sobre el diàmetre. Hi cap 3 vegades i una mica. És l'activitat del grup per descobrir π.</p>
  <h3>1. Les parts</h3>
  <p>b) diàmetre; c) centre; d) circumferència (la vora).</p>
  <h3>2. Radi i diàmetre</h3>
  <p>b) 10 cm; c) 4 cm; d) 35 cm (la roda de bicicleta del llibre: la meitat de 70). <b>Error típic:</b>
  fer el doble quan toca la meitat. La clau diu cap a on va cada un.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>3. La Nerea · la regla trencada</h3>
  <p>b) No: una mica més de 18 cm. c) No: una mica més de 24 cm. d) Sí: amb el diàmetre de 5 cm, una mica
  més de 15 cm. <b>Error típic:</b> fer servir el radi en lloc del diàmetre, com la Nerea del llibre. És la
  regla trencada d'aquesta fitxa. No l'expliqueu: que ho provi amb el cordill i un radi, i veurà que
  només arriba a mitja volta. L'apartat d és a posta. <b>Compta per als nivells alts, no per al mínim.</b></p>
  <h3>4. A la vida de cada dia</h3>
  <p>b) radi 4 cm, una mica més de 24 cm. c) radi 15 cm, una mica més de 90 cm. d) radi 35 cm, una mica
  més de 210 cm: la roda avança això a cada volta (el cas del llibre).</p>
  <h3>La caixa d'eines</h3>
  <p>La circumferència no té tasca pròpia a la caixa. Per repassar la unitat, les tasques 22 a 25.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta «Formes» al davant. Els criteris de la SA del grup (1.1, 3.1, 5.1, 6.1, 7.1 i
  9.1) són de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb un cordill i un objecte rodó, diu que la vora fa una mica més de 3 vegades el diàmetre.</li>
    <li>Diu el nom del centre, el radi, el diàmetre i la circumferència (exercici 1).</li>
    <li>Passa del radi al diàmetre i al revés: el doble i la meitat (exercicis 2 i 4).</li>
    <li>Nivells alts: diu per què la vora no fa 3 vegades el radi (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 6 · La circumferència", """  FITXA · Unitat 6 · Sentit espacial · La circumferència
  La cinquena fitxa de la unitat 6. Només la idea, sense π = 3,14: centre, radi,
  diàmetre (el doble del radi) i la vora, una mica més de 3 vegades el diàmetre.
  Els casos són els del llibre (la roda de bicicleta, la Nerea).

  La regla trencada és calcular la vora amb el radi: la Nerea, pàgina 4.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud6-cercle.html")
