#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud4-dobletriple.html: dobles i triples (unitat 4, fitxa 4).
Adapta les activitats 1 i 2 (És gran o petit?, De dobles o de triples) de la situació «És gran l'ou del kiwi?»: el nucli
de comparar mides relativament (un ou petit pot ser el doble d'un altre ou
petit, encara que tots dos siguin petits comparats amb l'ocell)."""
import os
import sys
from peces_comunes import *  # noqa: F401,F403
from peces_ud2 import *  # noqa: F401,F403
from peces_fraccions import *  # noqa: F401,F403
pagines = []
pagina = fes_pagina(pagines, "Unitat 4 · Dobles i triples · pàgina")


def dobles(n, k, m=None):
    """Dues files de quadrets, alineades a l'esquerra: `n` quadrets a dalt (la
    fila petita) i `n * k` a baix (el doble o el triple), amb ratlles fines a
    la fila de baix cada `n` quadrets, perquè es vegi quantes vegades hi cap.
    Sense `m`, la mida s'ajusta perquè la fila gran no passi de 6.2 cm d'ample."""
    gran = n * k
    if m is None:
        m = min(0.6, 6.2 / gran)
    aire = 0.16
    D = Dibuix(gran * m + 0.2, 2 * m + aire + 0.2, f"Una fila de {n} quadrets, i una altra de {gran}")
    D.rectangle(0.1, 0.1, 1, n, m, fons=F3)
    D.rectangle(0.1, 0.1 + m + aire, 1, gran, m, fons=F4)
    for i in range(1, k):
        x = 0.1 + i * n * m
        D.cru(f'<line x1="{D.px(x)}" y1="{D.px(0.1 + m + aire + 0.06)}" x2="{D.px(x)}" '
              f'y2="{D.px(0.1 + 2 * m + aire - 0.06)}" stroke="{G1}" stroke-width="1.6" stroke-dasharray="4 3"/>')
    return D


# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs</b>. Fer una fila de 3 i, a sota, una altra de 6. Comptar quantes vegades hi cap la fila petita.</div>
  <h1>Dobles i triples</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:1rem;width:9cm;margin-left:auto;margin-right:auto">
{dobles(3, 2, m=0.85).svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.5rem 0 .8rem">Hi ha una fila de 3 quadrets, i una altra de 6. La fila petita hi cap 2 vegades.</p>
  <table>
    <tr class="resolt"><td class="esq">Quantes vegades hi cap la fila petita?</td><td style="width:4.4cm">{ms("2 vegades")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">3 · 2 = 6</p>
    <p style="margin:.2rem 0;font-weight:700">6 és el doble de 3.</p>
  </div>''')

# ===================================================================== pàgina 2: fes el doble o el triple
E1 = [("a", 3, 2, True), ("b", 5, 2, False), ("c", 4, 3, False), ("d", 2, 3, False)]
it = []
for l, n, k, r in E1:
    gran = n * k
    cos = dobles(n, k)
    resultat = ms(str(gran)) if r else buit_curt()
    paraula = "doble" if k == 2 else "triple"
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span> Fila de {n}. Fes el {paraula}. Compta quants quadrets té.</p>
      <div style="width:{gran * 0.6 + 0.4:.1f}cm">{cos.svg("")}</div>
      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">El {paraula} de {n} és {resultat}.</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Fes el doble o el triple de la fila. Compta els quadrets.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">El doble és 2 vegades. El triple és 3 vegades.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 3: quantes vegades hi cap
E2 = [("a", 3, 3, True), ("b", 6, 2, False), ("c", 5, 3, False), ("d", 3, 2, False)]
it = []
for l, n, k, r in E2:
    gran = n * k
    cos = dobles(n, k)
    bona = ("El doble" if k == 2 else "El triple") if r else None
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span> Quantes vegades hi cap la fila petita?</p>
      <div style="width:{gran * 0.6 + 0.4:.1f}cm">{cos.svg("")}</div>
      {tria(["El doble", "El triple"], bona, mida="14pt", ample="3.2cm")}''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">És el doble o el triple? Marca la resposta. Compta els quadrets de la fila petita. Mira quantes vegades hi cap.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Un ou de kiwi fa 6 cm. Un ou de gallina fa 6 cm. Un ocell kiwi fa 40 cm. Una gallina fa 50 cm.</div></div>
    <div class="clau" style="margin:.3rem 0 .6rem"><p style="margin:0">Compara l'ou amb l'ocell que el fa, no un ou amb l'altre.</p></div>
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Quin ou és més gran, comparat amb l'ocell que el fa?</p>
      <p class="frase" style="margin:0">{ms("El del kiwi")}: 6 cm és molt, comparat amb 40 cm.</p>""", True)}
{caixa("""      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Els dos ous fan la mateixa mida (6 cm). Vol dir que els dos ocells són igual de grans?</p>
      """ + tria(["Sí", "No"], mida="14pt", ample="2.5cm"))}
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Un ou petit pot ser gran, comparat amb l'ocell que el fa.</p>
    <p style="margin:.2rem 0 0">Un ou de kiwi és petit, però és molt gran comparat amb la mida del kiwi.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
V = [("a", "Dues plantes fan 4 cm. Al cap d'una setmana, en fan 8 i 12.", 4, [8, 12], True),
     ("b", "Un cotxe de joguina fa 5 cm. Un cotxe de veritat en fa 400.", None, None, False)]
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Compara les mides. Digues quantes vegades és més gran.</div></div>
{caixa("""      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Dues plantes fan 4 cm. Al cap d'una setmana, en fan 8 i 12.</p>
      <p class="frase" style="margin:0">La primera és """ + ms("el doble") + """: 4 · 2 = 8. La segona és """ + ms("el triple") + """: 4 · 3 = 12.</p>""", True)}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Un cotxe de joguina fa 5 cm d'alt. Una porta de casa en fa 200. La joguina, és gran o petita comparada amb una porta?</p>
      <p class="frase" style="margin:0">{buit_curt()}: 5 cm és molt petit comparat amb 200 cm.</p>""")}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 4 · Dobles i triples · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> El doble i el triple es llegeixen en dues files de quadrets, una sota
    l'altra: la de dalt és el nombre petit, la de baix és el doble o el triple. Serveix per comparar
    mides relatives: un ou petit pot ser el doble d'un altre ou petit, i és aquí on la situació «És
    gran l'ou del kiwi?» hi arriba (un ou de kiwi és petit en absolut, però molt gran comparat amb
    la mida del kiwi). Els casos són els de la tasca 17 de la caixa.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs: una fila de 3 i, a sota, una altra de 6. Comptar quantes vegades hi
  cap la fila petita (2 vegades). És l'exemple de la pàgina 1: 3 · 2 = 6, el doble de 3.</p>
  <h3>1. Fes el doble o el triple</h3>
  <p>b) 10; c) 12; d) 6. Multiplicar per 2 és el doble; per 3, el triple.</p>
  <h3>2. Quantes vegades hi cap</h3>
  <p>b) El doble; c) El triple; d) El doble. Es compta de tants en tants quadrets com la fila
  petita, des de l'esquerra.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>3. L'ou del kiwi</h3>
  <p>b) No. <b>Error típic:</b> pensar que dos ous de la mateixa mida volen dir dos ocells igual de
  grans, sense mirar l'ocell que els fa. És la regla trencada d'aquesta fitxa. No l'expliqueu: que
  compari cada ou amb la mida del seu ocell, no un ou amb l'altre.</p>
  <h3>4. A la vida de cada dia</h3>
  <p>b) Petita: 5 cm és molt petit comparat amb 200 cm, com l'ou del kiwi comparat amb l'ocell.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=17</b> (17.1 El doble i el
  triple; 17.2 Quantes vegades hi cap?). La 17.2 dona un codi de verificació.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta de les taules al davant. Els criteris de la SA del grup (1.3, 2.1, 5.1 i
  6.1) són de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb miniblocs, fa el doble o el triple d'una fila.</li>
    <li>Diu quantes vegades hi cap la fila petita (exercici 2).</li>
    <li>Nivells alts: explica per què un ou petit pot ser gran comparat amb l'ocell (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 4 · Dobles i triples", """  FITXA · Unitat 4 · És gran l'ou del kiwi? · Dobles i triples
  La quarta fitxa de la unitat 4, i el nucli de la situació d'aprenentatge: el
  doble i el triple es llegeixen en dues files de quadrets, i serveixen per
  comparar mides relatives (un ou petit pot ser gran, comparat amb l'ocell que
  el fa). Sis dels deu casos de la tasca 17 de la caixa (regla 8); el cas
  9 x 2 = 18 queda fora perquè la fila no cap bé en una pàgina de paper.

  La regla trencada és pensar que dues mides absolutes iguals volen dir la
  mateixa proporció (exercici 3).""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud4-dobletriple.html")
