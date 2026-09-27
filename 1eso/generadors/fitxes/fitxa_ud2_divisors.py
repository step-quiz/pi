#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud2-divisors.html: divisors i primers (unitat 2, fitxa 3).
Adapta les activitats 2_4 (divisors) i 2_7 (Eratòstenes, primers i compostos) del grup."""
import os
import sys
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_ud2.py"), encoding="utf-8").read())

pagines = []
pagina = fes_pagina(pagines, "Unitat 2 · Divisors · pàgina")

# ===================================================================== pàgina 1
d = dibuix_rectangles(12, 0.55, "Els tres rectangles de 12 quadrets: 1 per 12, 2 per 6 i 3 per 4")
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs</b>. Fer tots els rectangles de 12, i després els de 7.</div>
  <h1>Divisors i primers</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div class="figura neta" style="margin-top:1rem">
{d.svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .8rem">Són tots els rectangles que es poden fer amb 12 quadrets.</p>

  <table>
    <tr class="resolt"><td class="esq">Quants rectangles hi ha?</td><td style="width:7.6cm">{ms("3")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets tenen els costats?</td><td>{ms("1 i 12, 2 i 6, 3 i 4")}</td></tr>
  </table>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">Cada rectangle dona dos divisors: les files i els quadrets de cada fila.</p>
    <p style="font-size:24pt;font-weight:800;margin:.3rem 0">Divisors del 12: 1, 2, 3, 4, 6 i 12</p>
    <p style="margin:0">2 · 6 i 6 · 2 són el mateix rectangle, girat. Només compta un cop.</p>
  </div>''')

# ===================================================================== pàgina 2
MULTS = [("a", 20, True), ("b", 18, False), ("c", 16, False), ("d", 15, False)]
items = []
for lletra, n, resolt in MULTS:
    rs = rectangles_de(n)
    if resolt:
        cad = ms(f"{n} = " + " = ".join(f"{a} · {b}" for a, b in rs))
        dv = ms(", ".join(map(str, divisors_de(n)[:-1])) + " i " + str(n))
    else:
        cad = f"{n} = " + " = ".join(buit() for _ in range(3))
        dv = f'<u style="display:inline-block;min-width:9cm;padding:0"></u>'
    fons = ' class="resolt"' if resolt else ""
    items.append(f'''    <div{fons} style="border-radius:10px;padding:.35rem .6rem;margin-bottom:.4rem">
      <p style="margin:0;font-size:17pt;font-weight:800"><span class="apartat">{lletra})</span> {n}</p>
      <p class="frase" style="margin:0">{cad}</p>
      <p class="frase" style="margin:0">Divisors: {dv}</p>
    </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Busca a la targeta les multiplicacions que donen cada nombre. Després escriu els divisors.</div></div>
    <div class="clau" style="margin:.3rem 0 .6rem">
      <p style="margin:0">Sempre hi ha la fila d'1: 1 · 20. Després, busca a la targeta.</p>
      <p style="margin:0">Potser no faràs servir tots els buits.</p>
    </div>
{chr(10).join(items)}
  </div>''')

# ===================================================================== pàgina 3
MD = [("a", 6, True), ("b", 8, False), ("c", 10, False), ("d", 9, False)]
files_md = []
for lletra, n, resolt in MD:
    if resolt:
        cel = (f'<td style="text-align:center">{ms(", ".join(str(n * i) for i in (1, 2, 3)))}</td>'
               f'<td style="text-align:center">{ms(", ".join(map(str, divisors_de(n))))}</td>')
    else:
        cel = '<td class="omplir" style="height:1.4cm"></td><td class="omplir"></td>'
    files_md.append(f'''      <tr{' class="resolt"' if resolt else ''}><td class="apartat" style="font-size:17pt">{lletra}) {n}</td>{cel}</tr>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Escriu tres múltiples i tots els divisors de cada nombre.</div></div>
    <table class="mini" style="margin-top:.4rem">
      <tr><th style="width:3cm">Nombre</th><th>Tres múltiples</th><th>Tots els divisors</th></tr>
{chr(10).join(files_md)}
    </table>
  </div>

  <div class="avis gruixut">
    <p style="margin:0;font-weight:700">No els confonguis:</p>
    <p style="margin:0">Els múltiples són la taula de la targeta: 6, 12, 18… Són més grans.</p>
    <p style="margin:0">Els divisors són els costats dels rectangles: 1, 2, 3 i 6. Són més petits.</p>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
PR = [("a", 9, True), ("b", 7, False), ("c", 15, False), ("d", 11, False), ("e", 21, False), ("f", 2, False)]
caselles = []
for lletra, n, resolt in PR:
    primer = len(rectangles_de(n)) == 1
    bona = ("Sí" if primer else "No") if resolt else None
    extra = (f'<p class="frase" style="margin:0;font-size:14.5pt">{ms("9 = 3 · 3")}: un quadrat de 3 per 3.</p>' if resolt
             else f'<p class="frase" style="margin:0;font-size:14.5pt">La multiplicació: {buit_curt()}</p>')
    fons = ' class="resolt"' if resolt else ""
    caselles.append(f'''      <div{fons} style="border-radius:10px;padding:.3rem .5rem">
        <p style="margin:0;font-size:18pt;font-weight:800"><span class="apartat" style="font-size:14pt">{lletra})</span> {n} <span style="font-size:14pt;font-weight:400">és primer?</span></p>
        {tria(["Sí", "No"], bona, mida="14pt", ample="2.5cm")}
        {extra}
      </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">És primer? Marca la resposta. Escriu la multiplicació.</div></div>
    <div class="clau" style="margin:.3rem 0 .6rem">
      <p style="margin:0">Un nombre primer només fa un rectangle, una fila: 7 = 1 · 7.</p>
      <p style="margin:0">Si en fa més d'un, no és primer: 6 = 2 · 3.</p>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.5rem .8cm">
{chr(10).join(caselles)}
    </div>
  </div>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Els senars no sempre són primers: 9 = 3 · 3 i 15 = 3 · 5.</p>
    <p style="margin:.2rem 0 0">I el 2 és parell, i és primer: només fa una fila, 1 · 2.</p>
  </div>''')

# ===================================================================== pàgina 5: el garbell
def estil_garbell(n):
    if n == 1 or (n % 2 == 0 and n > 2):
        return "ratllat_ma"
    if n == 2:
        return "encerclat_ma"
    return None


g = graella100(estil_garbell, "Graella de 100: l'1 i els múltiples del 2 ja estan ratllats, i el 2 té un cercle", m=0.98)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Fes el garbell d'Eratòstenes. El 2 ja està fet.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem">
      <p style="margin:0">1. Ratlla l'1: no és primer.</p>
      <p style="margin:0">2. Fes un cercle al 2 i ratlla els seus múltiples.</p>
      <p style="margin:0">3. Fes el mateix amb el 3, el 5 i el 7.</p>
      <p style="margin:0">4. Fes un cercle als que no estan ratllats: són primers.</p>
    </div>
    <div class="resolt" style="width:10.4cm;margin:0 auto;border-radius:10px;padding:.2rem">
{g.svg("      ")}
    </div>
    <p class="frase" style="margin:.5rem 0 0">Els primers fins al 30: <u style="display:inline-block;min-width:10cm;padding:0"></u></p>
  </div>''')

# ===================================================================== pàgina 6: la vida
d9 = Dibuix(3 * 0.5 + 0.2, 3 * 0.5 + 0.2, "9 cadires en 3 files de 3")
d9.rectangle(0.1, 0.1, 3, 3, 0.5)
pagina(f'''  <h2>A la vida de cada dia</h2>

  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Es poden fer equips iguals? De quantes persones?</div></div>
    <div class="duo">
      <div class="resolt" style="border-radius:10px;padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Hi ha 12 persones.</p>
        <p class="frase" style="margin:0">{ms("12 = 2 · 6 = 3 · 4")}</p>
        <p class="frase" style="margin:0">Equips de {ms("2, 3, 4 o 6")}.</p>
      </div>
      <div style="padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Hi ha 18 persones.</p>
        <p class="frase" style="margin:0">18 = {buit_curt()} = {buit_curt()}</p>
        <p class="frase" style="margin:0">Equips de {buit()}.</p>
      </div>
    </div>
  </div>

  <div class="exercici">
    <div class="tasca"><div class="n">6</div><div class="q">Es poden posar les cadires en files iguals, de més d'una cadira?</div></div>
    <div class="duo">
      <div class="resolt" style="border-radius:10px;padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Hi ha 9 cadires.</p>
{d9.svg("        ")}
        {tria(["Sí", "No"], "Sí", mida="14pt", ample="2.6cm")}
        <p class="frase" style="margin:0">{ms("9 = 3 · 3")}: 3 files de 3.</p>
      </div>
      <div style="padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Hi ha 7 cadires.</p>
        {tria(["Sí", "No"], mida="14pt", ample="2.6cm")}
        <p class="frase" style="margin:0">La multiplicació: {buit_curt()}</p>
      </div>
    </div>
  </div>

  <div class="clau" style="margin-top:.8rem">
    <p style="margin:0">Els equips possibles són els divisors del nombre de persones.</p>
    <p style="margin:0">Amb un nombre primer, només hi ha una fila: 7 = 1 · 7.</p>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 2 · Divisors i primers · full per al professorat</p>

  <div class="abans">
    <b>Abans de començar.</b> Els divisors d'un nombre surten dels rectangles que es poden fer amb
    aquells quadrets: cada rectangle en dona dos. Es diu sempre igual: «els divisors del 12 són
    1, 2, 3, 4, 6 i 12». Un primer només fa un rectangle, una fila. La targeta és al davant: les
    multiplicacions que donen un nombre hi són totes, llevat de la fila d'1 (1 · 20).
  </div>

  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs: fer tots els rectangles de 12 (1 per 12, 2 per 6 i 3 per 4) i
  després intentar-ho amb 7: només surt una fila. És el material de la unitat
  (dades/unitats.js) i l'exemple de la tasca 7.1 de la caixa.</p>

  <h3>1. Les multiplicacions i els divisors</h3>
  <p>b) 18 = 1 · 18 = 2 · 9 = 3 · 6: divisors 1, 2, 3, 6, 9 i 18. c) 16 = 1 · 16 = 2 · 8 = 4 · 4:
  divisors 1, 2, 4, 8 i 16 (el 4 només un cop). d) 15 = 1 · 15 = 3 · 5: divisors 1, 3, 5 i 15. És
  el format de l'activitat 2_4 del grup (20 = 1 · 20 = 2 · 10 = 4 · 5). <b>Error típic:</b> deixar-se
  l'1 i el mateix nombre, o escriure dues vegades el 4 del 16.</p>

  <h3>2. Múltiples i divisors</h3>
  <p>b) 8, 16, 24 · 1, 2, 4 i 8. c) 10, 20, 30 · 1, 2, 5 i 10. d) 9, 18, 27 · 1, 3 i 9. Es dona per bo
  qualsevol trio de múltiples, si són de la taula. <b>Error típic:</b> confondre'ls. L'avís del
  final de la pàgina ho posa de costat: els múltiples són més grans i els divisors, més petits.</p>

  <h3>3. És primer?</h3>
  <p>b) 7, primer (1 · 7); c) 15, no (3 · 5); d) 11, primer (1 · 11); e) 21, no (3 · 7); f) 2, primer
  (1 · 2). <b>Error típic:</b> dir que tots els senars són primers. És la regla trencada d'aquesta
  fitxa, i per això hi ha el 9, el 15 i el 21. No l'expliqueu: que faci el rectangle del 9 amb
  miniblocs. Surt un quadrat de 3 per 3. També hi ha el 2, que és parell i és primer.</p>
</div>''')

pagines.append('''<div class="full sol">
  <h3>4. El garbell</h3>
  <p>Els primers fins al 30: 2, 3, 5, 7, 11, 13, 17, 19, 23 i 29. Fins al 100 n'hi ha 25. És l'exercici
  1 de l'activitat 2_7 del grup. El pas del 2 ja està fet, com a model. No cal passar del 7: el
  primer múltiple de l'11 que encara no està ratllat és l'11 · 11, i ja passa del 100. Si es perd,
  la tasca 8.1 de la caixa ho fa pas a pas.</p>

  <h3>5 i 6. A la vida de cada dia</h3>
  <p>5b) 18 = 2 · 9 = 3 · 6: equips de 2, 3, 6 o 9. També són bons els equips d'1 i de 18, però no
  són equips de debò. 6b) No: 7 = 1 · 7, i el 7 és primer. Només hi ha una fila de 7, o set files
  d'una cadira. És la mateixa decisió que als exercicis: quins rectangles es poden fer?</p>

  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=7</b> (7.1 Els rectangles
  d'un nombre; 7.2 Troba els divisors) i <b style="white-space:nowrap">?task=8</b> (8.1 El garbell
  d'Eratòstenes; 8.2 És primer?). La 7.2 i la 8.2 donen un codi de verificació. La 7.1 s'obre amb
  el 12, com la pàgina 1.</p>

  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (1.4, 3.2, 4.2 i 5.2) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb miniblocs, fa tots els rectangles d'un nombre i en diu els divisors.</li>
    <li>Escriu les multiplicacions que donen un nombre i en treu els divisors (exercici 1).</li>
    <li>Distingeix els múltiples dels divisors d'un mateix nombre (exercici 2).</li>
    <li>Diu si un nombre és primer, amb la multiplicació que ho demostra (exercici 3).</li>
    <li>Fa el garbell i troba els primers fins al 30 (exercici 4).</li>
    <li>Nivells alts: explica per què el 9 no és primer, encara que sigui senar (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 2 · Divisors i primers", """  FITXA · Unitat 2 · Divisibilitat · Divisors i primers
  La tercera fitxa de la unitat 2. Adapta les activitats 2_4 (divisors) i 2_7
  (Eratòstenes, primers i compostos) del grup. Els divisors surten dels
  rectangles que es poden fer amb els quadrets; un primer només en fa un.

  Els casos són els de les tasques 7 i 8 de la caixa (regla 8): el 12 de la 7.1,
  els nombres de la 7.2 i els primers i els senars de la 8.2.

  La regla trencada és «tots els senars són primers» (exercici 3). La pàgina
  acaba amb la forma bona a la vista.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud2-divisors.html")
