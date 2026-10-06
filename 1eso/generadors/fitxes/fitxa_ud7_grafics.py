#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud7-grafics.html: taules i gràfics de barres (unitat 7, fitxa 4).

Adapta l'activitat 5 de la situació «Llenguatge algebraic i patrons» (el llibre, UD8: «Interpretar
gràfics i taules de la vida real»). Només barres i taules (decisió del docent del 29/9/2026): un
gràfic de barres són columnes de quadrets, i cada quadret és 1. Els casos són els del llibre (com
venen a l'institut: 12, 8, 6 i 4; la lectura crítica dels gràfics de dos cursos) i els de la tasca
28 de la caixa.

La regla trencada (regla G): «si la barra és el doble d'alta, n'hi ha el doble», amb un eix que no
comença a zero (pàgina 4). La lectura crítica del llibre compara dos cursos; aquí, «classe A» i «classe B»,
perquè el material no porta noms de cursos (anonimat).
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
from peces_comunes import *  # noqa: F401,F403
from peces_ud2 import *  # noqa: F401,F403
from peces_fraccions import *  # noqa: F401,F403
from peces_geo import *  # noqa: F401,F403

pagines = []
pagina = fes_pagina(pagines, "Unitat 7 · Taules i gràfics · pàgina")
INSTITUT = [("A peu", 12), ("Bus", 8), ("Bici", 6), ("Cotxe", 4)]
ESPORT = [("Futbol", 9), ("Bàsquet", 7), ("Natació", 5), ("Dansa", 6)]
FRUITA = [("Poma", 7), ("Plàtan", 10), ("Taronja", 4), ("Maduixa", 8)]

# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs</b>. Cada persona diu com ve a l'institut i posa un bloc a la seva columna.</div>
  <h1>Taules i gràfics</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <p style="font-size:16pt;font-weight:700;text-align:center;margin:.6rem 0 .2rem">Com venim a l'institut</p>
  <div class="figura neta">
{barres_d(INSTITUT, "Gràfic de barres, com venim a l'institut: a peu 12, bus 8, bici 6, cotxe 4", m=0.42).svg()}
  </div>
  <table style="margin-top:.4rem">
    <tr class="resolt"><td class="esq">Quants alumnes venen a peu?</td><td style="width:5.4cm">{ms("12")}</td></tr>
    <tr class="resolt"><td class="esq">Quina és la barra més baixa?</td><td>{ms("Cotxe")}</td></tr>
    <tr class="resolt"><td class="esq">Quants alumnes hi ha en total?</td><td>{ms("12 + 8 + 6 + 4 = 30")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Cada quadret és una persona.</p>
    <p style="margin:.2rem 0 0">On acaba la barra, l'eix diu quants alumnes són.</p>
  </div>''')

# ===================================================================== pàgina 2: llegeix el gràfic
P = [("a", "Quants alumnes prefereixen el futbol?", "9", True), ("b", "Quants alumnes prefereixen la natació?", "", False),
     ("c", "Quin és l'esport preferit?", "", False), ("d", "Quants alumnes més prefereixen el futbol que el bàsquet?", "", False)]
it = "\n".join(caixa(f'''      <p style="margin:0 0 .1rem"><span class="apartat">{l})</span> {t}</p>
      <p class="frase" style="margin:0">{ms(r_) if r else buit()}</p>''', r, ".25rem") for l, t, r_, r in P)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Mira el gràfic. Contesta les preguntes.</div></div>
    <p style="font-size:15pt;font-weight:700;text-align:center;margin:.2rem 0">L'esport preferit</p>
    <div class="figura neta">{barres_d(ESPORT, "Gràfic de barres, l'esport preferit: futbol 9, bàsquet 7, natació 5, dansa 6").svg("")}</div>
{it}
  </div>''')

# ===================================================================== pàgina 3: de la taula al gràfic
taula = "".join(f'<td style="text-align:center;font-size:17pt;font-weight:800">{v}</td>' for _, v in FRUITA)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Fes el gràfic de la taula. Pinta un quadret per cada alumne.</div></div>
    <table class="mini">
      <tr><th>Fruita</th>{"".join(f"<th>{e}</th>" for e, _ in FRUITA)}</tr>
      <tr><th>Alumnes</th>{taula}</tr>
    </table>
    <p style="font-size:15pt;font-weight:700;text-align:center;margin:.5rem 0 .2rem">La fruita preferida</p>
    <div class="figura neta">{barres_d(FRUITA, "Un gràfic per pintar, amb la barra de la poma ja pintada", m=0.55, buit=True, pintades=1, max_eix=10).svg("")}</div>
    <p class="frase" style="margin:.2rem 0 0">La barra més alta és la de {buit()}.</p>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
def dos(ini, a, b, aria):
    return barres_d([("Classe A", a), ("Classe B", b)], aria, m=0.55, ini=ini, max_eix=b + 1, pas=1 if b - ini < 8 else 2)


R = [("a", 20, 22, 24, "No", True), ("b", 10, 12, 16, "No", False)]
it = []
for l, ini, a, b, bona, r in R:
    it.append(caixa(f'''      <p style="margin:0 0 .1rem;font-size:15pt;font-weight:700"><span class="apartat">{l})</span> En Martí diu: a la classe B hi ha molts més alumnes. Diu que la barra és molt més alta.</p>
      <div style="display:flex;gap:.8cm;align-items:center">
        <div>{dos(ini, a, b, f"Un gràfic de dues barres amb l'eix que comença a {ini}: classe A {a}, classe B {b}").svg("")}</div>
        <div>
          <p class="frase" style="margin:0;font-size:15pt">Classe A: {ms(str(a)) if r else buit_curt()}. Classe B: {ms(str(b)) if r else buit_curt()}.</p>
          <p style="margin:.2rem 0 0;font-size:15pt">L'eix comença a 0?</p>
          {tria(["Sí", "No"], "No" if r else None, mida="14pt", ample="2.2cm")}
          <p style="margin:.2rem 0 0;font-size:15pt">Té raó en Martí?</p>
          {tria(["Sí", "No"], bona if r else None, mida="14pt", ample="2.2cm")}
        </div>
      </div>''', r, ".35rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Mira on comença l'eix. Té raó en Martí?</div></div>
{chr(10).join(it)}
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Mira sempre on comença l'eix.</p>
    <p style="margin:.2rem 0 0">Si l'eix no comença a 0, una barra pot semblar el doble. Però 24 no és el doble de 22.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
dies = ["Dl", "Dt", "Dc", "Dj", "Dv", "Ds", "Dg"]
pagina(f'''  <h2>A la vida de cada dia: el meu gràfic</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Durant una setmana, apunta quantes hores dorms cada nit. Després fes el gràfic.</div></div>
    <table class="mini">
      <tr><th>Dia</th>{"".join(f"<th>{x}</th>" for x in dies)}</tr>
      <tr><th>Hores</th>{'<td class="omplir"></td>' * 7}</tr>
    </table>
    <div class="figura neta" style="margin-top:.5rem">{barres_d([(x, 12) for x in dies], "Un gràfic buit per pintar les hores de son de cada dia", m=0.42, buit=True, max_eix=12, amp_b=1.9).svg("")}</div>
    <p class="frase" style="margin:.2rem 0 0">El dia que vaig dormir més: {buit()}.</p>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 7 · Taules i gràfics · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Només gràfics de barres i taules (la decisió de la unitat). Un gràfic de
    barres són columnes de quadrets: cada quadret és 1, com a la tasca 28 de la caixa. La targeta
    «Patrons i símbols» porta els quatre passos per llegir un gràfic.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs: quatre columnes a la taula (a peu, bus, bici, cotxe) i cada alumne del
  grup, o de la classe, hi posa un bloc. Surt el gràfic de barres amb blocs.</p>
  <h3>1. Llegeix el gràfic</h3>
  <p>b) 5. c) El futbol. d) 9 − 7 = 2.</p>
  <h3>2. De la taula al gràfic</h3>
  <p>Barres de 7, 10, 4 i 8 quadrets. La més alta, la del plàtan. <b>Error típic:</b> començar a pintar
  per dalt, o no arribar a la ratlla: que compti els quadrets de baix a dalt.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>3. En Martí · la regla trencada</h3>
  <p>a) Classe A, 22; classe B, 24. L'eix no comença a 0: la barra de la B sembla el doble, però 24 no és el
  doble de 22. En Martí no té raó. b) Classe A, 12; classe B, 16. L'eix comença a 10: la barra de la B sembla el triple,
  però només en són 4 més. <b>Error típic:</b> comparar l'alçada de les barres sense mirar on comença
  l'eix. És la regla trencada d'aquesta fitxa, i la «lectura crítica» del llibre. No l'expliqueu:
  que llegeixi el nombre de cada barra a l'eix. <b>Compta per als nivells alts, no per al mínim.</b></p>
  <h3>4. El meu gràfic</h3>
  <p>No hi ha una resposta única: és el gràfic del dossier del grup (un fenomen personal durant una
  setmana). Es mira que cada barra arribi a la ratlla del seu nombre.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=28</b> (28.1 Llegeix el
  gràfic; 28.2 Quantes persones?). La 28.2 dona un codi de verificació. L'enquesta de la pàgina 1 és la
  de la caixa i la del llibre.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (2.1, 3.1, 4.1, 5.1 i 7.2) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb miniblocs, fa un gràfic de barres d'una enquesta de la classe.</li>
    <li>Llegeix quants n'hi ha a cada barra, i compara dues barres (exercici 1).</li>
    <li>Fa un gràfic de barres a partir d'una taula (exercicis 2 i 4).</li>
    <li>Nivells alts: diu per què cal mirar on comença l'eix (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 7 · Taules i gràfics", """  FITXA · Unitat 7 · Llenguatge algebraic i patrons · Taules i gràfics
  La quarta fitxa de la unitat 7. Adapta l'activitat 5 de la situació (el llibre,
  UD8): llegir i fer gràfics de barres de quadrets. Els casos són els del llibre i
  els de la tasca 28 de la caixa (regla 8).

  La regla trencada és comparar l'alçada de les barres sense mirar on comença
  l'eix: en Martí, pàgina 4.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud7-grafics.html")
