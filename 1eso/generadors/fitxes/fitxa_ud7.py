#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud7.html: patrons de quadrets (unitat 7, fitxa 1).

Adapta les activitats 1 i 2 de la situació «Llenguatge algebraic i patrons» (el llibre, UD8:
«Patrons a l'entorn» i «Patrons numèrics i geomètrics»). Un patró creix sempre igual: què hi ha de
fix i què s'hi afegeix, i quants en té la figura següent. Els casos són els del llibre (la cadena
3, 5, 7; les successions 6, 11, 16, 21 i 80, 72, 64, 56; els escuradents; l'error d'en Pau) i els de
la tasca 26 de la caixa.

La regla trencada (regla G): en Pau diu que 2, 4, 6, 8 «creix multiplicant per 2» (pàgina 4).
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
pagina = fes_pagina(pagines, "Unitat 7 · Patrons de quadrets · pàgina")

# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs</b>. Fer les figures 1, 2 i 3 d'un patró, i després la 4.</div>
  <h1>Patrons de quadrets</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div style="display:flex;gap:1.2cm;align-items:flex-end;justify-content:center;margin-top:.8rem">
    {figures_d(2, 1, 3, 0.75, "Un patró")}
  </div>
  <table style="margin-top:.6rem">
    <tr class="resolt"><td class="esq">Quants quadrets té cada figura?</td><td style="width:4.4cm">{ms("3, 5 i 7")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets més té cada figura?</td><td>{ms("2")}</td></tr>
    <tr class="resolt"><td class="esq">Quants en té la figura 4?</td><td>{ms("7 + 2 = 9")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Un patró creix sempre igual.</p>
    <p style="margin:.2rem 0 0">El quadret blanc és fix. Cada figura té 2 quadrets més.</p>
  </div>''')

# ===================================================================== pàgina 2: la figura 4
E1 = [("a", 2, 0, True), ("b", 3, 0, False), ("c", 1, 2, False), ("d", 3, 1, False)]
it = []
for l, a, b, r in E1:
    q4 = a * 4 + b
    it.append(caixa(f'''      <p style="margin:0 0 .15rem"><span class="apartat">{l})</span></p>
      <div style="display:flex;gap:.7cm;align-items:flex-end;flex-wrap:wrap">{figures_d(a, b, 3, 0.48, f"Apartat {l}")}</div>
      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">Cada figura té {ms(str(a)) if r else buit_curt()} quadrets més. La figura 4 té {ms(str(q4)) if r else buit_curt()} quadrets.</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Mira les figures 1, 2 i 3. Quants quadrets té la figura 4?</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Compta quants quadrets més té la figura 3 que la 2.</p></div>
{chr(10).join(it)}
  </div>''')

# ===================================================================== pàgina 3: patrons de nombres
S = [("a", [6, 11, 16, 21], 5, True), ("b", [5, 10, 15, 20], 5, False), ("c", [3, 7, 11, 15], 4, False),
     ("d", [80, 72, 64, 56], -8, False)]
files = []
for l, sq, d, r in S:
    seg = [sq[-1] + d, sq[-1] + 2 * d]
    cel = (f'<td style="text-align:center">{ms(str(seg[0]))}</td><td style="text-align:center">{ms(str(seg[1]))}</td>'
           f'<td style="text-align:center">{ms(("+" if d > 0 else "−") + " " + str(abs(d)))}</td>' if r else
           '<td class="omplir"></td><td class="omplir"></td><td class="omplir"></td>')
    files.append(f'''      <tr{' class="resolt"' if r else ''}><td style="font-size:17pt;font-weight:800;padding:.2rem .5rem"><span class="apartat">{l})</span> {", ".join(map(str, sq))}</td>{cel}</tr>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Escriu els dos nombres següents. Escriu també quant se suma o es resta cada vegada.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Mira quant hi ha de l'un a l'altre. El d va cap avall: és la taula del 8.</p></div>
    <table class="mini">
      <tr><th>El patró</th><th style="width:2.4cm">Següent</th><th style="width:2.4cm">I el següent</th><th style="width:3cm">Cada vegada</th></tr>
{chr(10).join(files)}
    </table>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
P = [("a", [2, 4, 6, 8], "Suma sempre el mateix", True), ("b", [3, 6, 9, 12], "Suma sempre el mateix", False),
     ("c", [1, 2, 4, 8], "Multiplica per 2", False), ("d", [5, 10, 15, 20], "Suma sempre el mateix", False)]
it = []
for l, sq, bona, r in P:
    it.append(caixa(f'''      <p style="margin:0 0 .1rem;font-size:18pt;font-weight:800"><span class="apartat">{l})</span> {", ".join(map(str, sq))}</p>
      {tria(["Multiplica per 2", "Suma sempre el mateix"], bona if r else None, mida="13pt", ample="3.8cm", columna=True)}''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">En Pau diu que 2, 4, 6, 8 creix multiplicant per 2. Té raó? Com creix cada patró?</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Comprova el patró amb el tercer nombre, no només amb el segon.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Comprova sempre el tercer nombre.</p>
    <p style="margin:.2rem 0 0">2 · 2 = 4, però 4 · 2 = 8, i el tercer és 6. El patró 2, 4, 6, 8 suma 2 cada vegada.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Les taules d'un menjador es posen en fila. Quantes cadires hi caben?</div></div>
    <table class="mini">
      <tr><th>Taules</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th></tr>
      <tr class="resolt"><th>Cadires</th><td style="text-align:center">4</td><td style="text-align:center">6</td><td style="text-align:center">8</td>
        <td style="text-align:center">{ms("10")}</td><td class="omplir"></td></tr>
    </table>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Amb escuradents es fan quadrats en fila. Quants escuradents calen?</div></div>
    <table class="mini">
      <tr><th>Quadrats</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th></tr>
      <tr><th>Escuradents</th><td style="text-align:center">4</td><td style="text-align:center">7</td><td style="text-align:center">10</td>
        <td class="omplir"></td><td class="omplir"></td></tr>
    </table>
    <p class="frase" style="margin:.2rem 0 0">Cada quadrat nou porta {buit_curt()} escuradents més.</p>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 7 · Patrons de quadrets · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Un patró creix sempre igual: el que hi ha de fix (el quadret blanc,
    discontinu) i el que s'hi afegeix a cada figura. És la tasca 26 de la caixa, on la part fixa surt
    en taronja. La targeta «Patrons i símbols» porta un exemple.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs: fer les figures 1, 2 i 3 del patró de la pàgina 1 (3, 5 i 7 blocs) i
  construir la 4. Si els blocs fixos són d'un altre color, es veu què s'hi afegeix.</p>
  <h3>1. La figura 4</h3>
  <p>b) s'afegeixen 3; la figura 4 en té 12. c) s'afegeix 1; en té 6. d) s'afegeixen 3; en té 13.</p>
  <h3>2. Patrons de nombres</h3>
  <p>b) 25, 30 (+ 5). c) 19, 23 (+ 4). d) 48, 40 (− 8, la taula del 8 cap avall). La a) és del llibre, i la
  d) també.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>3. En Pau · la regla trencada</h3>
  <p>b) suma sempre el mateix (3); c) multiplica per 2: 1, 2, 4, 8; d) suma sempre el mateix (5).
  <b>Error típic:</b> mirar només el primer pas (2 · 2 = 4) i dir que multiplica per 2, com en Pau del
  llibre. És la regla trencada d'aquesta fitxa. No l'expliqueu: que ho comprovi amb el tercer nombre.
  L'apartat c és a posta: n'hi ha que sí que multipliquen per 2. <b>Compta per als nivells alts, no
  per al mínim.</b></p>
  <h3>4 i 5. A la vida de cada dia</h3>
  <p>4) 5 taules, 12 cadires (s'afegeixen 2 a cada taula). 5) 13 i 16 escuradents; cada quadrat nou
  n'afegeix 3 (els escuradents del llibre).</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=26</b> (26.1 El patró; 26.2
  Quants en té la següent?). La 26.2 dona un codi de verificació; les respostes falses són sumar-ne
  sempre 1 i multiplicar per 2, l'error d'en Pau.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (2.1, 3.1, 4.1, 5.1 i 7.2) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb miniblocs, construeix la figura següent d'un patró.</li>
    <li>Diu quants quadrets s'afegeixen i quants en té la figura següent (exercici 1).</li>
    <li>Continua un patró de nombres i diu què s'hi fa cada vegada (exercicis 2, 4 i 5).</li>
    <li>Nivells alts: diu per què 2, 4, 6, 8 no multiplica per 2 (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 7 · Patrons de quadrets", """  FITXA · Unitat 7 · Llenguatge algebraic i patrons · Patrons de quadrets
  La primera fitxa de la unitat 7. Adapta les activitats 1 i 2 de la situació (el
  llibre, UD8): un patró creix sempre igual, què hi ha de fix i què s'hi afegeix.
  Els casos són els del llibre i els de la tasca 26 de la caixa (regla 8).

  La regla trencada és «2, 4, 6, 8 creix multiplicant per 2»: en Pau, pàgina 4.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud7.html")
