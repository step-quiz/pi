#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud7-simbols.html: de la paraula al símbol (unitat 7, fitxa 3).

Adapta l'activitat 3 de la situació «Llenguatge algebraic i patrons» (el llibre, UD8: «De la paraula
al símbol: variable i expressió»). La lletra n és un nombre qualsevol; «el triple d'un nombre»
s'escriu 3 · n, sempre amb el punt (decisió del docent del 29/9/2026). Sense equacions: traduir i
calcular per a un valor. Els casos són els del llibre (el triple, un nombre menys 7, la meitat, el
següent; n + 10, 5 · n, n − 1, n : 4; els valors per a n = 3 i n = 10; l'error de la Zoe) i els de la
tasca 27 de la caixa.

La regla trencada (regla G): posar el nombre al costat en lloc de multiplicar (la Zoe: «si n = 3,
2n = 23»), a la pàgina 4. Les igualtats falses van dins de .revisa.
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
pagina = fes_pagina(pagines, "Unitat 7 · De la paraula al símbol · pàgina")

# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs i una capsa</b>. A la capsa hi ha uns quants blocs: és la n. Fer el triple: tres capses iguals.</div>
  <h1>De la paraula al símbol</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:.8rem">
{patro_d(3, 0, 4, 0.8, "Tres files de 4 quadrets: el triple de 4").svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .5rem">El triple d'un nombre: tres files iguals.</p>
  <table>
    <tr class="resolt"><td class="esq">Quantes files hi ha?</td><td style="width:4.4cm">{ms("3")}</td></tr>
    <tr class="resolt"><td class="esq">Si cada fila té 4 quadrets, quants quadrets hi ha en total?</td><td>{ms("3 · 4 = 12")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">La lletra n és un nombre qualsevol.</p>
    <p style="margin:.1rem 0 0">El triple d'un nombre s'escriu:</p>
    <p style="margin:.1rem 0 0;font-size:26pt;font-weight:800">3 · n</p>
    <p style="margin:0">Si n és 4: 3 · 4 = 12.</p>
  </div>''')

# ===================================================================== pàgina 2: escriu el símbol i les paraules
S1 = [("a", "El triple d'un nombre", "3 · n", True), ("b", "Un nombre menys 7", "n − 7", False),
      ("c", "La meitat d'un nombre", "n : 2", False), ("d", "El següent d'un nombre", "n + 1", False),
      ("e", "El doble d'un nombre, més 1", "2 · n + 1", False)]
f1 = "\n".join(f'''      <tr{' class="resolt"' if r else ''}><td style="padding:.2rem .5rem;font-size:15pt"><span class="apartat">{l})</span> {t}</td>
        <td style="text-align:center">{ms(sm) if r else ""}</td></tr>''' for l, t, sm, r in S1)
S2 = [("a", "n + 10", "Un nombre més 10", True), ("b", "5 · n", "", False), ("c", "n − 1", "", False), ("d", "n : 4", "", False)]
f2 = "\n".join(f'''      <tr{' class="resolt"' if r else ''}><td style="padding:.2rem .5rem;font-size:18pt;font-weight:800;text-align:center"><span class="apartat">{l})</span> {sm}</td>
        <td style="text-align:center">{ms(t) if r else ""}</td></tr>''' for l, sm, t, r in S2)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Escriu el símbol. Fes servir la lletra n. Mira la targeta.</div></div>
    <table class="mini">
      <tr><th>La frase</th><th style="width:5cm">El símbol</th></tr>
{f1}
    </table>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Escriu amb paraules què vol dir cada símbol.</div></div>
    <table class="mini">
      <tr><th style="width:4cm">El símbol</th><th>Amb paraules</th></tr>
{f2}
    </table>
  </div>''')

# ===================================================================== pàgina 3: calcula
C = [("a", "4 · n", lambda n: 4 * n, True), ("b", "n + 12", lambda n: n + 12, False),
     ("c", "2 · n + 5", lambda n: 2 * n + 5, False), ("d", "3 · n + 2", lambda n: 3 * n + 2, False)]
def cal(sm, n, fn):
    return sm.replace("n", str(n)) + " = " + str(fn(n))
files = "\n".join(f'''      <tr{' class="resolt"' if r else ''}><td style="padding:.2rem .5rem;font-size:18pt;font-weight:800;text-align:center"><span class="apartat">{l})</span> {sm}</td>
        <td style="text-align:center">{ms(cal(sm, 3, fn)) if r else ""}</td><td style="text-align:center">{ms(cal(sm, 10, fn)) if r else ""}</td></tr>''' for l, sm, fn, r in C)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Posa el nombre on hi ha la n. Calcula.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Primer es multiplica, després se suma. Mira la targeta de les taules.</p></div>
    <table class="mini">
      <tr><th style="width:4cm">El símbol</th><th>Si n és 3</th><th>Si n és 10</th></tr>
{files}
    </table>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
Z = [("a", 3, "2 · n", "23", 6, True), ("b", 4, "5 · n", "54", 20, False), ("c", 1, "3 · n", "31", 3, False),
     ("d", 2, "n + 1", "3", 3, False)]
it = []
for l, n, sm, diu, bo_v, r in Z:
    bona = "Sí" if str(bo_v) == diu else "No"
    it.append(caixa(f'''      <p style="margin:0 0 .1rem;font-size:16pt;font-weight:800"><span class="apartat">{l})</span> Si n és {n}, <span class="revisa">{sm} = {diu}</span></p>
      <p style="margin:0 0 .1rem;font-size:15pt">La Zoe diu que sí. Té raó?</p>
      {tria(["Sí", "No"], bona if r else None, mida="13pt", ample="2.2cm")}
      <p class="frase" style="margin:0;font-size:15pt">{sm} val {ms(str(bo_v)) if r else buit_curt()}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">La Zoe posa el nombre al costat, en lloc de multiplicar. Té raó?</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">El punt vol dir multiplicar.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">El punt vol dir multiplicar.</p>
    <p style="margin:.2rem 0 0">Si n és 3, 2 · n és 2 · 3 = 6, no 23. Per això aquí sempre escrivim el punt.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
V = [("a", "Una entrada de cinema costa 6 €. Quant paguen n amics?", "6 · n", "Si són 4 amics: 6 · 4 = 24 €", True),
     ("b", "La Laia té n cromos i compra 5 cromos més. Quants cromos té?", "", "Si n és 12:", False),
     ("c", "Un taxi cobra 3 € per pujar i 2 € per quilòmetre. Quant costa fer n quilòmetres?", "", "Si són 5 quilòmetres:", False)]
it = []
for l, t, sm, cas, r in V:
    it.append(caixa(f'''      <p style="margin:0 0 .15rem"><span class="apartat">{l})</span> {t}</p>
      <p class="frase" style="margin:0">El símbol: {ms(sm) if r else buit()}</p>
      <p class="frase" style="margin:0">{ms(cas) if r else cas + " " + buit()}</p>''', r, ".35rem"))
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Escriu el símbol. Després calcula.</div></div>
{chr(10).join(it)}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 7 · De la paraula al símbol · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> La lletra n és un nombre qualsevol. El producte s'escriu sempre amb el punt
    (3 · n, la decisió de la unitat); la targeta diu que el grup ho escriu 3n. No hi ha equacions:
    només traduir i calcular per a un valor. La taula de traducció és a la targeta «Patrons i símbols».
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs i capses: a cada capsa, els mateixos blocs (és la n, i no se sap
  quants són). El triple són tres capses. Obrir-les: si n'hi ha 4 a cada una, n'hi ha 12.</p>
  <h3>1 i 2. Traduir</h3>
  <p>1b) n − 7; c) n : 2; d) n + 1; e) 2 · n + 1 (els casos del llibre). 2b) cinc vegades un nombre (el
  quíntuple); c) un nombre menys 1 (l'anterior); d) la quarta part d'un nombre.</p>
  <h3>3. Calcula</h3>
  <p>b) 15 i 22; c) 2 · 3 + 5 = 11 i 2 · 10 + 5 = 25; d) 3 · 3 + 2 = 11 i 3 · 10 + 2 = 32 (els del llibre).
  <b>Error típic:</b> sumar abans de multiplicar. La clau ho recorda.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>4. La Zoe · la regla trencada</h3>
  <p>b) No: 5 · 4 = 20. c) No: 3 · 1 = 3. d) Sí: 2 + 1 = 3. <b>Error típic:</b> posar el nombre al costat
  (2n amb n = 3, 23), com la Zoe del llibre. És la regla trencada d'aquesta fitxa, i és per això que
  aquí sempre s'escriu el punt. L'apartat d és a posta: amb una suma, la Zoe encerta. <b>Compta per
  als nivells alts, no per al mínim.</b></p>
  <h3>5. A la vida de cada dia</h3>
  <p>b) n + 5; si n és 12, 17 cromos. c) 2 · n + 3; per a 5 quilòmetres, 2 · 5 + 3 = 13 €. <b>La c) compta
  per als nivells alts</b>: té una part fixa, com els patrons.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=27</b> (27.1 La paraula i el
  símbol; 27.2 Quin és el símbol?). La 27.2 dona un codi de verificació.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (2.1, 3.1, 4.1, 5.1 i 7.2) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb capses i miniblocs, fa el doble o el triple d'un nombre que no se sap.</li>
    <li>Escriu una frase amb símbols, i un símbol amb paraules (exercicis 1 i 2).</li>
    <li>Calcula una expressió per a un valor de n (exercicis 3 i 5).</li>
    <li>Nivells alts: diu per què 2 · n no és 23 quan n és 3 (exercici 4).</li>
  </ul>
</div>''')

document("Unitat 7 · De la paraula al símbol", """  FITXA · Unitat 7 · Llenguatge algebraic i patrons · De la paraula al símbol
  La tercera fitxa de la unitat 7. Adapta l'activitat 3 de la situació (el llibre,
  UD8): la lletra n és un nombre qualsevol, i «el triple d'un nombre» s'escriu
  3 · n, sempre amb el punt. Els casos són els del llibre i els de la tasca 27.

  La regla trencada és posar el nombre al costat: la Zoe, pàgina 4. Les igualtats
  falses van dins de .revisa.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud7-simbols.html")
