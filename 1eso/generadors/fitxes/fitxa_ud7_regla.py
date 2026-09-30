#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud7-regla.html: la regla d'un patró (unitat 7, fitxa 2).

Adapta l'activitat 4 de la situació «Llenguatge algebraic i patrons» (el llibre, UD8: «El terme
general d'un patró»). La figura n té a · n + b quadrets: el que creix va davant de la n i el que és
fix va al final. Sempre amb el punt (decisió del docent del 29/9/2026). Els casos són els del llibre
(4, 8, 12, 16; 6, 7, 8, 9; 10, 20, 30; la taula del 7; l'error de la Ivet: 5, 8, 11, 14 → 3 · n) i
els de la tasca 26 de la caixa. Figures fins a la 10: cap nombre no passa de 999.

La regla trencada (regla G): oblidar la part fixa (la Ivet, pàgina 4).
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
from peces_comunes import *  # noqa: F401,F403
from peces_ud2 import *  # noqa: F401,F403
from peces_fraccions import *  # noqa: F401,F403
from peces_geo import *  # noqa: F401,F403

pagines = []
pagina = fes_pagina(pagines, "Unitat 7 · La regla del patró · pàgina")
regla = lambda a, b: (f"{a} · n" if a != 1 else "n") + (f" + {b}" if b else "")

# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs de dos colors</b>. Els fixos d'un color i els que creixen de l'altre. Fer les figures 1, 2 i 3.</div>
  <h1>La regla del patró</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div style="display:flex;gap:1.2cm;align-items:flex-end;justify-content:center;margin-top:.8rem">
    {figures_d(3, 2, 3, 0.55, "El patró 3 · n + 2")}
  </div>
  <table style="margin-top:.6rem">
    <tr class="resolt"><td class="esq">Quants quadrets fixos hi ha?</td><td style="width:4.4cm">{ms("2")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets més té cada figura?</td><td>{ms("3")}</td></tr>
    <tr class="resolt"><td class="esq">La regla</td><td>{ms("3 · n + 2")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">El que creix va davant de la n. El que és fix va al final.</p>
    <p style="margin:.2rem 0 0;font-size:24pt;font-weight:800">3 · n + 2</p>
    <p style="margin:0">La figura 10: 3 · 10 + 2 = 32.</p>
  </div>''')

# ===================================================================== pàgina 2: omple la taula
E1 = [("a", 2, 0, True), ("b", 3, 1, False), ("c", 2, 3, False), ("d", 5, 0, False)]
files = []
for l, a, b, r in E1:
    vals = [a * n + b for n in (1, 2, 3, 4, 10)]
    cel = ""
    for k, v in enumerate(vals):
        if r:
            cel += f'<td style="text-align:center">{ms(str(v))}</td>'
        elif k < 2:                                    # les dues primeres, donades: fan de pista
            cel += f'<td style="text-align:center;font-size:16pt;font-weight:700">{v}</td>'
        else:
            cel += '<td class="omplir"></td>'
    files.append(f'''      <tr{' class="resolt"' if r else ''}><td style="font-size:17pt;font-weight:800;padding:.2rem .5rem"><span class="apartat">{l})</span> {regla(a, b)}</td>{cel}</tr>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Fes servir la regla. Omple la taula: quants quadrets té cada figura?</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Posa el número de la figura on hi ha la n. Figura 3 amb 2 · n: 2 · 3 = 6.</p></div>
    <table class="mini">
      <tr><th>La regla</th><th>Figura 1</th><th>Figura 2</th><th>Figura 3</th><th>Figura 4</th><th>Figura 10</th></tr>
{chr(10).join(files)}
    </table>
  </div>''')

# ===================================================================== pàgina 3: escriu la regla
E2 = [("a", [3, 5, 7, 9], "2 · n + 1", True), ("b", [4, 8, 12, 16], "4 · n", False),
      ("c", [6, 7, 8, 9], "n + 5", False), ("d", [10, 20, 30, 40], "10 · n", False)]
files = "\n".join(f'''      <tr{' class="resolt"' if r else ''}><td style="font-size:17pt;font-weight:800;padding:.25rem .5rem"><span class="apartat">{l})</span> {", ".join(map(str, sq))}</td>
        <td style="text-align:center">{ms(rg) if r else ""}</td></tr>''' for l, sq, rg, r in E2)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Escriu la regla de cada patró.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem">
      <p style="margin:0 0 .2rem">1. Quant creix cada vegada? Aquest nombre va davant de la n.</p>
      <p style="margin:0">2. Compara la figura 1 amb aquest nombre. El que sobra és fix.</p>
    </div>
    <table class="mini">
      <tr><th>El patró</th><th style="width:6cm">La regla</th></tr>
{files}
    </table>
    <p style="margin:.4rem 0 0;font-size:14pt">A la a): creix 2, i la figura 1 té 3. De 2 a 3 en sobra 1: 2 · n + 1.</p>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
P = [("a", [5, 8, 11, 14], "3 · n", "No", "3 · n + 2", True), ("b", [4, 7, 10, 13], "3 · n", "No", "3 · n + 1", False),
     ("c", [3, 6, 9, 12], "3 · n", "Sí", "3 · n", False), ("d", [7, 9, 11, 13], "2 · n", "No", "2 · n + 5", False)]
it = []
for l, sq, diu, bona, rg, r in P:
    it.append(caixa(f'''      <p style="margin:0 0 .1rem;font-size:17pt;font-weight:800"><span class="apartat">{l})</span> {", ".join(map(str, sq))}</p>
      <p style="margin:0 0 .1rem;font-size:15pt">La Ivet diu: {diu}. Té raó?</p>
      {tria(["Sí", "No"], bona if r else None, mida="14pt", ample="2.2cm")}
      <p class="frase" style="margin:0;font-size:15pt">La regla bona: {ms(rg) if r else buit()}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">La Ivet mira quant creix i escriu la regla. Té raó? Comprova la regla amb la figura 1.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Compta també la part fixa.</p>
    <p style="margin:.2rem 0 0">Amb 3 · n, la figura 1 fa 3 · 1 = 3. Però en té 5: sobren 2. La regla és 3 · n + 2.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">La taula del 7 també és un patró: 7, 14, 21, 28…</div></div>
{caixa(f"""      <p class="frase" style="margin:0"><span class="apartat">a)</span> La regla: {ms("7 · n")}</p>""", True, ".3rem")}
{caixa(f"""      <p class="frase" style="margin:0"><span class="apartat">b)</span> El número 10 del patró: {buit()}</p>""", False, ".3rem")}
{caixa(f"""      <p class="frase" style="margin:0"><span class="apartat">c)</span> El 56 és el número {buit_curt()} del patró. Mira la targeta de les taules.</p>""", False, ".3rem")}
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Les taules del menjador, en fila. Amb 1 taula, 4 cadires. Amb 2 taules, 6 cadires. Amb 3 taules, 8 cadires.</div></div>
{caixa(f"""      <p class="frase" style="margin:0">La regla: {buit()}. Per a 10 taules calen {buit_curt()} cadires.</p>""", False, ".3rem")}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 7 · La regla del patró · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> La regla d'un patró de quadrets: el que creix a cada figura va davant de
    la n, i el que és fix va al final. Sempre amb el punt: 3 · n + 2 (la decisió de la unitat). Es
    comprova amb la figura 1. No és una equació: la n és el número de la figura, i se substitueix.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs de dos colors: els 2 fixos d'un color i els que creixen, de l'altre. A
  cada figura se'n posen 3 més. És el patró de la Ivet (5, 8, 11), vist amb blocs.</p>
  <h3>1. Omple la taula</h3>
  <p>b) 3 · n + 1: 4, 7, 10, 13 i 31. c) 2 · n + 3: 5, 7, 9, 11 i 23. d) 5 · n: 5, 10, 15, 20 i 50.</p>
  <h3>2. Escriu la regla</h3>
  <p>b) 4 · n; c) n + 5; d) 10 · n (els casos del llibre). <b>Error típic:</b> escriure el primer nombre
  en lloc del que creix (6 · n per a 6, 7, 8, 9).</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>3. La Ivet · la regla trencada</h3>
  <p>b) No: 3 · n + 1. c) Sí: 3 · n. d) No: 2 · n + 5. <b>Error típic:</b> escriure només el que creix i
  oblidar la part fixa, com la Ivet del llibre. És la regla trencada d'aquesta fitxa. No l'expliqueu:
  que comprovi la regla amb la figura 1. L'apartat c és a posta: quan no hi ha part fixa, la Ivet
  encerta. <b>Compta per als nivells alts, no per al mínim.</b></p>
  <h3>4 i 5. A la vida de cada dia</h3>
  <p>4b) 7 · 10 = 70. 4c) el 8 (7 · 8 = 56), la pregunta del llibre. 5) 2 · n + 2; per a 10 taules,
  2 · 10 + 2 = 22 cadires.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=26</b> (26.1 El patró, que
  ensenya la regla de cada patró i la figura que es vulgui fins a la 10).</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (2.1, 3.1, 4.1, 5.1 i 7.2) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb miniblocs de dos colors, diu què és fix i què creix.</li>
    <li>Fa servir una regla per saber quants quadrets té una figura (exercici 1).</li>
    <li>Escriu la regla d'un patró (exercici 2).</li>
    <li>Nivells alts: comprova una regla amb la figura 1 i hi posa la part fixa (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 7 · La regla del patró", """  FITXA · Unitat 7 · Llenguatge algebraic i patrons · La regla del patró
  La segona fitxa de la unitat 7. Adapta l'activitat 4 de la situació (el llibre,
  UD8: «El terme general»): a · n + b, el que creix davant de la n i el que és fix
  al final. Els casos són els del llibre i els de la tasca 26 de la caixa.

  La regla trencada és oblidar la part fixa: la Ivet, pàgina 4.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud7-regla.html")
