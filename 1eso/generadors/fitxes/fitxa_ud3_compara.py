#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud3-compara.html: els tipus i comparar (unitat 3, fitxa 2).
Adapta les activitats Fraccions 2, 4, 5 i 6 del grup."""
import os
import sys
from peces_comunes import *  # noqa: F401,F403
from peces_ud2 import *  # noqa: F401,F403
from peces_fraccions import *  # noqa: F401,F403
pagines = []
pagina = fes_pagina(pagines, "Unitat 3 · Compara · pàgina")
TIPUS = {"nulla": "nul·la", "propia": "pròpia", "unitat": "unitat", "impropia": "impròpia"}
tipus = lambda n, d: "nulla" if n == 0 else "propia" if n < d else "unitat" if n == d else "impropia"


def dues(a, b, c, d, W=7.0, H=0.8):
    return (f'<div style="display:grid;grid-template-columns:auto 1fr;gap:.25rem .4cm;align-items:center">'
            f'<div>{fr(a, b, "15pt")}</div><div>{tira(a, b, f"{a} de {b}", W=W, H=H).svg("")}</div>'
            f'<div>{fr(c, d, "15pt")}</div><div>{tira(c, d, f"{c} de {d}", W=W, H=H).svg("")}</div></div>')


# ===================================================================== pàgina 1
files = "\n".join(f'''    <tr class="resolt"><td style="text-align:center;width:2cm">{fr(n, 4)}</td>
      <td style="width:6.2cm">{tira(n, 4, f"{n} trossos pintats de 4", W=5.8, H=0.6).svg("")}</td>
      <td class="esq">{ms(TIPUS[tipus(n, 4)])}</td></tr>''' for n in (0, 3, 4, 5))
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>dues tires de paper</b>, doblegades en 4 trossos. Pintar-ne 5 trossos: en una sola tira no hi caben. I la targeta de les fraccions.</div>
  <h1>Els tipus i comparar</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <table class="mini" style="margin-top:.6rem">
    <tr><th>Fracció</th><th>El dibuix</th><th>El tipus</th></tr>
{files}
  </table>
  <div class="avis gruixut">
    <p style="margin:0"><b>Nul·la</b>: el de dalt és 0. No hi ha res pintat.</p>
    <p style="margin:0"><b>Pròpia</b>: el de dalt és més petit que el de baix. És menys d'un rectangle.</p>
    <p style="margin:0"><b>Unitat</b>: dalt i baix són iguals. És tot el rectangle.</p>
    <p style="margin:0"><b>Impròpia</b>: el de dalt és més gran. És més d'un rectangle.</p>
  </div>''')

# ===================================================================== pàgina 2
E1 = [("a", 3, 4, True), ("b", 7, 7, False), ("c", 9, 5, False), ("d", 0, 6, False), ("e", 2, 9, False), ("f", 12, 10, False)]
f1 = "\n".join(f'''      <tr{' class="resolt"' if r else ''}><td class="apartat" style="font-size:16pt;width:3cm">{l}) {fr(n, d)}</td>'''
               f'''<td class="esq">{ms(TIPUS[tipus(n, d)]) if r else ""}</td></tr>''' for l, n, d, r in E1)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Quin tipus de fracció és? Escriu-lo. Mira el de dalt i el de baix.</div></div>
    <table class="mini" style="margin-top:.4rem">
      <tr><th>Fracció</th><th>El tipus</th></tr>
{f1}
    </table>
  </div>
  <div class="clau" style="margin-top:.6rem">
    <p style="margin:0">Si no ho veus clar, pinta-la en una tira de paper.</p>
  </div>''')

# ===================================================================== pàgina 3: mateix denominador
E2 = [("a", 3, 5, 2, 5, True), ("b", 1, 8, 5, 8, False), ("c", 4, 6, 3, 6, False), ("d", 7, 10, 9, 10, False)]
it = []
for l, a, b, c, d, r in E2:
    gran = (a, b) if a * d > c * b else (c, d)
    ops = [f"{a}/{b}", f"{c}/{d}"]
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span></p>
{dues(a, b, c, d, W=5.0, H=0.6)}
      <p class="frase" style="margin:.2rem 0 0;font-size:14.5pt">La més gran: {fr(*gran, ma=True) if r else fr_buit("13pt")}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Quina és més gran? Escriu-la. Els dos rectangles són iguals.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Mateix denominador: és més gran la que té més trossos pintats.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
E3 = [("a", 1, 3, 1, 5, True), ("b", 2, 7, 2, 5, False), ("c", 1, 6, 1, 4, False), ("d", 3, 8, 3, 5, False)]
it = []
for l, a, b, c, d, r in E3:
    gran = (a, b) if a * d > c * b else (c, d)
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span></p>
{dues(a, b, c, d, W=5.0, H=0.6)}
      <p class="frase" style="margin:.2rem 0 0;font-size:14.5pt">La més gran: {fr(*gran, ma=True) if r else fr_buit("13pt")}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">I ara? Tenen el mateix numerador. Quina és més gran?</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Com més gran és el de baix, més petits són els trossos.</p>
    <p style="margin:.2rem 0 0">{fr(1, 5, "15pt")} és més petit que {fr(1, 3, "15pt")}, encara que 5 sigui més gran que 3.</p>
  </div>''')

# ===================================================================== pàgina 5: ordenar
E4 = [("a", [(3, 4), (1, 4), (2, 4)], True), ("b", [(1, 3), (1, 6), (1, 2)], False), ("c", [(5, 8), (7, 8), (2, 8)], False)]
it = []
for l, fs, r in E4:
    ordenades = sorted(fs, key=lambda x: x[0] / x[1])
    dib = "".join(f'<div>{fr(n, d, "15pt")}</div><div>{tira(n, d, f"{n} de {d}", W=6.4, H=0.7).svg("")}</div>' for n, d in fs)
    res = " &lt; ".join(fr(n, d, ma=True) for n, d in ordenades) if r else " &lt; ".join(fr_buit("13pt") for _ in fs)
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span></p>
      <div style="display:grid;grid-template-columns:auto 1fr;gap:.2rem .4cm;align-items:center">{dib}</div>
      <p class="frase" style="margin:.25rem 0 0;font-size:14.5pt">De més petita a més gran: {res}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Ordena les fraccions, de més petita a més gran. Mira els dibuixos.</div></div>
{chr(10).join(it)}
  </div>''')

# ===================================================================== pàgina 6: la vida
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Qui n'ha menjat més? El pastís i la pizza són iguals per a tothom.</div></div>
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Del pastís, tu en menges {fr(3, 8, "14pt")} i una amiga, {fr(2, 8, "14pt")}.</p>
{dues(3, 8, 2, 8)}
      <p class="frase" style="margin:.2rem 0 0">{ms("Jo")}: {fr(3, 8, ma=True)} és més gran.</p>""", True)}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> De la pizza, tu en menges {fr(1, 3, "14pt")} i un amic, {fr(1, 4, "14pt")}.</p>
{dues(1, 3, 1, 4)}
      <p class="frase" style="margin:.2rem 0 0">N'ha menjat més: <u style="display:inline-block;min-width:4cm;padding:0"></u></p>""")}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 3 · Els tipus i comparar · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Per comparar, les dues fraccions es dibuixen sempre amb el mateix
    rectangle: si no, la comparació no té sentit. Sense decimals (el valor numèric del grup queda
    fora): es compara el tros pintat. La caixa d'eines ho fa a la tasca 11.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb dues tires de paper de 4 trossos: pintar-ne 5. En una tira no hi caben: 5/4 és
  més d'un rectangle, i per això és impròpia.</p>
  <h3>1. Els tipus</h3>
  <p>b) 7/7, unitat; c) 9/5, impròpia; d) 0/6, nul·la; e) 2/9, pròpia; f) 12/10, impròpia. Són els
  tipus de l'activitat Fraccions 5 del grup.</p>
  <h3>2. Mateix denominador</h3>
  <p>b) 5/8; c) 4/6; d) 9/10. Més trossos pintats del mateix rectangle.</p>
  <h3>3. Mateix numerador</h3>
  <p>b) 2/5; c) 1/4; d) 3/5. <b>Error típic:</b> triar la del nombre de baix més gran (1/5 més gran
  que 1/3). És la regla trencada d'aquesta fitxa. No l'expliqueu: que miri el dibuix, on els trossos
  del 5 són més petits. Són els casos de la tasca 11.2 de la caixa.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>4. Ordenar</h3>
  <p>b) 1/6 &lt; 1/3 &lt; 1/2; c) 2/8 &lt; 5/8 &lt; 7/8. Amb el mateix numerador, l'ordre va al revés
  dels de baix; amb el mateix denominador, com els de dalt.</p>
  <h3>5. A la vida de cada dia</h3>
  <p>b) Jo: 1/3 és més gran que 1/4, i l'amic en menja menys. És la regla trencada en una situació de
  debò, com els problemes del pastís i del tortell de l'activitat Fraccions 4 del grup.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=11</b> (11.1 Compara dues
  fraccions; 11.2 Quina és més gran?). La 11.2 dona un codi de verificació. La 11.1 s'obre amb 1/3 i
  1/5, la regla trencada. Els tipus també surten a la 9.1.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (1.2, 5.2, 6.1 i 9.1) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Diu de quin tipus és una fracció, mirant el de dalt i el de baix (exercici 1).</li>
    <li>Compara dues fraccions amb el mateix denominador (exercici 2).</li>
    <li>Compara dues fraccions amb el mateix numerador, amb el dibuix (exercici 3).</li>
    <li>Ordena tres fraccions amb el dibuix (exercici 4).</li>
    <li>Nivells alts: explica per què 1/5 és més petit que 1/3 (exercicis 3 i 5).</li>
  </ul>
</div>''')

document("Unitat 3 · Els tipus i comparar", """  FITXA · Unitat 3 · Les fraccions · Els tipus i comparar
  La segona fitxa de la unitat 3. Adapta les activitats Fraccions 2, 4, 5 i 6
  del grup: els quatre tipus (nul·la, pròpia, unitat, impròpia) i comparar amb
  el mateix rectangle, sense el valor numèric (regla C). Els casos de comparar
  són els de la tasca 11 de la caixa (regla 8).

  La regla trencada és «com més gran és el de baix, més gran és la fracció»
  (exercici 3). Les fraccions van dins de .fr: comprova.py les llegeix.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud3-compara.html")
