#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud3-equivalents.html: fraccions equivalents (unitat 3, fitxa 3).
Adapta les activitats Fraccions 3, 5 i 6 del grup."""
import os
import sys
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_ud2.py"), encoding="utf-8").read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_fraccions.py"), encoding="utf-8").read())
pagines = []
pagina = fes_pagina(pagines, "Unitat 3 · Equivalents · pàgina")


def dues(a, b, c, d, W=7.0, H=0.8, ma2=False, buida2=False, k=1):
    return (f'<div style="display:grid;grid-template-columns:auto 1fr;gap:.25rem .4cm;align-items:center">'
            f'<div>{fr(a, b, "15pt")}</div><div>{tira(a, b, f"{a} de {b}", W=W, H=H, k=k).svg("")}</div>'
            f'<div>{fr(c, d, "15pt", ma=ma2) if not buida2 else fr_buit("12pt")}</div>'
            f'<div>{tira(c, d, f"{c} de {d}", W=W, H=H, ma=ma2, buida=buida2).svg("")}</div></div>')


# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>una tira de paper</b>. Doblegar-la per la meitat i pintar-ne una meitat. Després, tornar-la a doblegar: ara hi ha 4 trossos, i 2 de pintats.</div>
  <h1>Fraccions equivalents</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:1rem;width:11cm;margin-left:auto;margin-right:auto">
{dues(1, 2, 2, 4, W=9.0, H=1.0)}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.5rem 0 .8rem">Són dos rectangles iguals. El de baix té els trossos partits per la meitat.</p>
  <table>
    <tr class="resolt"><td class="esq">Quin tros pintat és més llarg?</td><td style="width:6cm">{ms("Són iguals")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">{fr(1, 2, "15pt")} i {fr(2, 4, "15pt")} tenen el mateix tros pintat.</p>
    <p style="margin:.2rem 0">{fr(1, 2, "34pt")} = {fr(2, 4, "34pt")}</p>
    <p style="margin:0;font-weight:700">Són fraccions equivalents.</p>
  </div>''')

# ===================================================================== pàgina 2
E1 = [("a", 1, 2, 4, True), ("b", 1, 3, 6, False), ("c", 2, 3, 12, False), ("d", 3, 4, 8, False), ("e", 2, 5, 10, False)]
it = []
for l, n, d, d2, r in E1:
    n2 = n * d2 // d
    cos = dues(n, d, n2, d2, W=6.6, H=0.75, ma2=r, buida2=not r)
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span> Pinta el mateix tros amb {d2} trossos.</p>
{cos}''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Pinta el mateix tros al rectangle de baix. Escriu la fracció nova.</div></div>
{chr(10).join(it)}
  </div>''')

# ===================================================================== pàgina 3: amplificar
E2 = [("a", 2, 3, 4, True), ("b", 1, 2, 3, False), ("c", 3, 5, 2, False), ("d", 1, 4, 3, False), ("e", 2, 5, 2, False)]
f2 = "\n".join(f'''      <tr{' class="resolt"' if r else ''}><td class="apartat" style="font-size:16pt;white-space:nowrap">{l}) {fr(n, d)}</td>'''
               f'''<td style="text-align:center">per {k}</td>'''
               f'''<td style="text-align:center">{ms(f"{n} · {k} = {n * k}") if r else ""}</td>'''
               f'''<td style="text-align:center">{ms(f"{d} · {k} = {d * k}") if r else ""}</td>'''
               f'''<td style="text-align:center;height:1.6cm">{fr(n * k, d * k, ma=True) if r else fr_buit("12pt")}</td></tr>''' for l, n, d, k, r in E2)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Amplifica: multiplica el de dalt i el de baix pel mateix nombre. Mira la targeta.</div></div>
    <table class="mini" style="margin-top:.4rem">
      <tr><th>Fracció</th><th>Multiplica</th><th>El de dalt</th><th>El de baix</th><th>La nova</th></tr>
{f2}
    </table>
  </div>
  <div class="clau" style="margin-top:.6rem">
    <p style="margin:0">Partir cada tros en 4 és multiplicar per 4 dalt i baix. El tros pintat no canvia.</p>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
E3 = [("a", 1, 2, 2, 4, True), ("b", 2, 3, 4, 6, False), ("c", 1, 2, 2, 3, False), ("d", 1, 3, 2, 6, False), ("e", 1, 4, 2, 6, False)]
it = []
for l, a, b, c, d, r in E3:
    eq = a * d == b * c
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span> Són equivalents?</p>
{dues(a, b, c, d, W=6.0, H=0.7)}
      {tria(["Sí", "No"], ("Sí" if eq else "No") if r else None, mida="14pt", ample="2.5cm")}''', r, ".25rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Són equivalents? Marca la resposta. Mira si el tros pintat és igual de llarg.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Per fer una equivalent, es multiplica. No se suma.</p>
    <p style="margin:.2rem 0 0">Si sumes 1 dalt i baix, {fr(1, 2, "15pt")} es fa {fr(2, 3, "15pt")}. No és equivalent: el tros és més llarg.</p>
  </div>''')

# ===================================================================== pàgina 5: simplificar
E4 = [("a", 4, 8, 4, True), ("b", 6, 9, 3, False), ("c", 5, 10, 5, False), ("d", 8, 12, 4, False)]
f4 = "\n".join(f'''      <tr{' class="resolt"' if r else ''}><td class="apartat" style="font-size:16pt;white-space:nowrap">{l}) {fr(n, d)}</td>'''
               f'''<td style="text-align:center">entre {k}</td>'''
               f'''<td style="text-align:center;height:1.6cm">{fr(n // k, d // k, ma=True) if r else fr_buit("12pt")}</td></tr>''' for l, n, d, k, r in E4)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Simplifica: divideix el de dalt i el de baix pel mateix nombre.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem">
      <p style="margin:0">És el camí de tornada d'amplificar. Busca-ho a la targeta de les taules: 4 · 1 = 4 i 4 · 2 = 8.</p>
    </div>
    <table class="mini" style="margin-top:.2rem">
      <tr><th>Fracció</th><th>Divideix</th><th>La simplificada</th></tr>
{f4}
    </table>
  </div>''')

# ===================================================================== pàgina 6: la vida
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Menges el mateix? Les dues pizzes són iguals, però tallades diferent.</div></div>
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Una pizza de 4 trossos: en menges 2. D'una de 8 trossos, quants n'has de menjar?</p>
{dues(2, 4, 4, 8, ma2=True)}
      <p class="frase" style="margin:.2rem 0 0">{ms("4 trossos")}: {fr(2, 4, ma=True)} = {fr(4, 8, ma=True)}</p>""", True)}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Una xocolata de 12 quadradets. La meitat, quants quadradets són?</p>
{dues(1, 2, 0, 12, buida2=True)}
      <p class="frase" style="margin:.2rem 0 0">{buit_curt()} quadradets: {fr(1, 2)} = {fr_buit("13pt")}</p>""")}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 3 · Fraccions equivalents · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Dues fraccions són equivalents si pinten el mateix tros del mateix
    rectangle. Partir cada tros en trossos més petits és amplificar: dalt i baix, pel mateix nombre.
    La multiplicació en creu i el valor numèric del grup queden fora. La caixa d'eines ho fa a la
    tasca 10.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb una tira de paper: doblegar-la per la meitat i pintar-ne una meitat; tornar-la a
  doblegar i comptar: 2 trossos pintats de 4. El tros pintat és el mateix.</p>
  <h3>1. Pinta el mateix tros</h3>
  <p>b) 2/6; c) 8/12, l'exemple de l'activitat Fraccions 3 del grup; d) 6/8; e) 4/10.</p>
  <h3>2. Amplificar</h3>
  <p>b) 1 · 3 = 3 i 2 · 3 = 6: 3/6; c) 3 · 2 = 6 i 5 · 2 = 10: 6/10; d) 1 · 3 = 3 i 4 · 3 = 12: 3/12;
  e) 2 · 2 = 4 i 5 · 2 = 10: 4/10. Totes les multiplicacions són de la targeta.</p>
  <h3>3. Són equivalents?</h3>
  <p>b) Sí; c) No; d) Sí; e) No. <b>Error típic:</b> sumar el mateix dalt i baix (1/2 i 2/3). És la
  regla trencada d'aquesta fitxa. No l'expliqueu: que compari els trossos pintats, i veurà que el
  de 2/3 és més llarg. Són casos de la tasca 10.2 de la caixa.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>4. Simplificar · nivells alts</h3>
  <p>b) 2/3; c) 1/2; d) 2/3. És el camí de tornada, i els nombres són de la targeta: 3 · 2 = 6 i 3 · 3 = 9,
  5 · 1 = 5 i 5 · 2 = 10. Els nombres grans del grup (120/50) i els arbres per simplificar queden fora.
  <b>Compta per als nivells alts, no per al mínim.</b></p>
  <h3>5. A la vida de cada dia</h3>
  <p>b) 6 quadradets: 1/2 = 6/12. És la mateixa decisió que als exercicis: el mateix tros, partit en
  trossos més petits.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=10</b> (10.1 Parteix els
  trossos; 10.2 Són equivalents?). La 10.2 dona un codi de verificació. La 10.1 s'obre amb 2/3 = 8/12.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb les dues targetes al davant. Els criteris de la SA del grup (1.2, 5.2, 6.1 i 9.1) són
  de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb una tira de paper doblegada, ensenya que 1/2 = 2/4.</li>
    <li>Pinta una fracció equivalent amb més trossos (exercici 1).</li>
    <li>Amplifica una fracció amb la targeta (exercici 2).</li>
    <li>Diu si dues fraccions són equivalents mirant el dibuix (exercici 3).</li>
    <li>Nivells alts: simplifica una fracció fàcil (exercici 4).</li>
  </ul>
</div>''')

document("Unitat 3 · Fraccions equivalents", """  FITXA · Unitat 3 · Les fraccions · Fraccions equivalents
  La tercera fitxa de la unitat 3. Adapta les activitats Fraccions 3, 5 i 6 del
  grup: el mateix tros pintat, partit en trossos més petits; amplificar amb la
  targeta; i simplificar fàcil, per als nivells alts. La multiplicació en creu i
  el valor numèric queden fora. Els casos són els de la tasca 10 de la caixa.

  La regla trencada és sumar el mateix dalt i baix (1/2 i 2/3, exercici 3). Les
  fraccions van dins de .fr: comprova.py les llegeix.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud3-equivalents.html")
