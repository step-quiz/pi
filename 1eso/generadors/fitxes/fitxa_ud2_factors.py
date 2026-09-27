#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud2-factors.html: la factorització (unitat 2, fitxa 4).
Adapta les activitats 2_5 (factorització), 2_8 i «ADN dels nombres» del grup, amb la
decisió del docent del 25/9/2026: tres factors primers com a molt, sense potències."""
import os
import sys
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_ud2.py"), encoding="utf-8").read())

pagines = []
pagina = fes_pagina(pagines, "Unitat 2 · Factors · pàgina")

# Tots de tres factors primers com a molt, i cada pas és una multiplicació de la targeta.
# Conveni: a cada partició, el primer a l'esquerra i el que es torna a partir a la dreta.
ARBRES = {12: [(3, 4), (2, 2)], 18: [(2, 9), (3, 3)], 20: [(5, 4), (2, 2)], 30: [(5, 6), (2, 3)], 45: [(5, 9), (3, 3)]}
factors = lambda n: " · ".join(map(str, sorted(x for x in (ARBRES[n][0][0],) + ARBRES[n][1])))

# ===================================================================== pàgina 1
d = arbre(12, ARBRES[12], "L'arbre del 12: el 12 es parteix en 3 i 4, i el 4 en 2 i 2")
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs</b>. Fer un bloc de 12: 2 pisos, i a cada pis, 2 files de 3.</div>
  <h1>La factorització</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div class="figura neta" style="margin-top:.8rem;width:8cm;margin-left:auto;margin-right:auto">
{d.svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .8rem">És un arbre: el 12 es parteix en 3 i 4, i el 4 en 2 i 2.</p>

  <table>
    <tr class="resolt"><td class="esq">En quins dos nombres es parteix el 12?</td><td style="width:5.8cm">{ms("3 i 4")}</td></tr>
    <tr class="resolt"><td class="esq">El 3 es pot partir?</td><td>{ms("No: és primer")}</td></tr>
    <tr class="resolt"><td class="esq">I el 4?</td><td>{ms("Sí: 2 · 2")}</td></tr>
  </table>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">Les branques s'acaben quan hi ha un primer. Els primers tenen dos cercles.</p>
    <p style="font-size:30pt;font-weight:800;margin:.3rem 0">12 = 2 · 2 · 3</p>
    <p style="margin:0;font-weight:700">Això és la factorització del 12.</p>
  </div>''')

# ===================================================================== pàgina 2
caselles = []
for lletra, n, resolt in [("a", 18, True), ("b", 20, False), ("c", 30, False), ("d", 45, False)]:
    dib = arbre(n, ARBRES[n], f"L'arbre del {n}" + ("" if resolt else ", amb els cercles buits per omplir"),
                buit_=not resolt, m=0.9)
    final = ms(f"{n} = {factors(n)}") if resolt else f"{n} = {buit_curt()} · {buit_curt()} · {buit_curt()}"
    fons = ' class="resolt"' if resolt else ""
    caselles.append(f'''      <div{fons} style="border-radius:10px;padding:.35rem .5rem">
        <p style="margin:0;font-size:16pt;font-weight:700"><span class="apartat">{lletra})</span> L'arbre del {n}</p>
        <div style="width:6.2cm;margin:0 auto">
{dib.svg("          ")}
        </div>
        <p class="frase" style="margin:.1rem 0 0">{final}</p>
      </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Fes l'arbre de cada nombre. Mira la targeta.</div></div>
    <div class="clau" style="margin:.3rem 0 .6rem">
      <p style="margin:0">Busca a la targeta una multiplicació que doni el nombre.</p>
      <p style="margin:0">El primer, a l'esquerra. El que es torna a partir, a la dreta.</p>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.5rem .8cm">
{chr(10).join(caselles)}
    </div>
  </div>''')

# ===================================================================== pàgina 3: la regla trencada
ACABADA = [("a", "12 = 3 · 4", False, True), ("b", "18 = 2 · 3 · 3", True, False), ("c", "20 = 4 · 5", False, False),
           ("d", "30 = 2 · 3 · 5", True, False), ("e", "45 = 5 · 9", False, False), ("f", "15 = 3 · 5", True, False)]
caselles3 = []
for lletra, text, acabada, resolt in ACABADA:
    bona = ("Sí" if acabada else "No") if resolt else None
    extra = (f'<p class="frase" style="margin:0;font-size:14.5pt">El 4 = 2 · 2. {ms("12 = 2 · 2 · 3")}</p>' if resolt
             else f'<p class="frase" style="margin:0;font-size:14.5pt">Si no, acaba-la: {buit()}</p>')
    fons = ' class="resolt"' if resolt else ""
    caselles3.append(f'''      <div{fons} style="border-radius:10px;padding:.3rem .5rem">
        <p style="margin:0;font-size:18pt;font-weight:800"><span class="apartat" style="font-size:14pt">{lletra})</span> {text}</p>
        {tria(["Sí", "No"], bona, mida="14pt", ample="2.5cm")}
        {extra}
      </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Està acabada la factorització? Marca la resposta.</div></div>
    <div class="clau" style="margin:.3rem 0 .6rem">
      <p style="margin:0">Està acabada si tots els nombres són primers.</p>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.5rem .8cm">
{chr(10).join(caselles3)}
    </div>
  </div>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">12 = 3 · 4 és veritat, però no està acabada: el 4 no és primer.</p>
    <p style="margin:.2rem 0 0">Com que 4 = 2 · 2, la factorització del 12 és 12 = 2 · 2 · 3.</p>
  </div>''')

# ===================================================================== pàgina 4: l'ADN dels nombres
ADN = [("a", (2, 2, 3), True), ("b", (2, 3, 5), False), ("c", (3, 3, 5), False), ("d", (2, 2, 5), False),
       ("e", (2, 5, 5), False), ("f", (3, 3, 3), False), ("g", (2, 2, 2), False)]
files_adn = []
for lletra, fs, resolt in ADN:
    a, b, c = fs
    if resolt:
        cel = (f'<td style="text-align:center">{ms(f"{a} · {b} = {a * b}")}</td>'
               f'<td style="text-align:center">{ms(f"{a * b} · {c} = {a * b * c}")}</td>'
               f'<td style="text-align:center">{ms(str(a * b * c))}</td>')
    else:
        cel = '<td class="omplir" style="height:1.3cm"></td>' * 3
    files_adn.append(f'''      <tr{' class="resolt"' if resolt else ''}><td class="apartat" style="font-size:17pt;white-space:nowrap">{lletra}) {a} · {b} · {c}</td>{cel}</tr>''')
pagina(f'''  <h2>La recepta de cada nombre</h2>
  <div class="avis gruixut">
    <p style="margin:0">Cada nombre té una sola factorització. És com una recepta: amb aquests primers surt el nombre.</p>
    <p style="margin:0">Si tens la factorització, pots trobar el nombre.</p>
  </div>

  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Quin nombre és? Multiplica els dos primers. Després, pel tercer.</div></div>
    <table class="mini" style="margin-top:.4rem">
      <tr><th style="width:4.2cm">La factorització</th><th>Els dos primers</th><th>Pel tercer</th><th style="width:2.8cm">El nombre</th></tr>
{chr(10).join(files_adn)}
    </table>
  </div>''')

# ===================================================================== pàgina 5: la vida
def pisos(n_pisos, files, cols, aria, m=0.5):
    gap = 0.9
    amp = n_pisos * cols * m + (n_pisos - 1) * gap + 0.2
    d = Dibuix(amp, files * m + 0.85, aria)
    for p in range(n_pisos):
        x = 0.1 + p * (cols * m + gap)
        d.rectangle(x, 0.1, files, cols, m)
        d.text(x + cols * m / 2, files * m + 0.65, f"pis {p + 1}", 0.4, 700)
    return d


pagina(f'''  <h2>A la vida de cada dia</h2>

  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Les capses de bombons tenen pisos. Quants bombons hi ha?</div></div>
    <div class="resolt" style="border-radius:10px;padding:.4rem .6rem;margin-bottom:.5rem">
      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> 2 pisos. A cada pis, 2 files de 3 bombons.</p>
{pisos(2, 2, 3, "2 pisos de 2 files de 3 bombons").svg("      ")}
      <p class="frase" style="margin:.2rem 0 0">{ms("2 · 2 · 3 = 12")} bombons.</p>
    </div>
    <div style="padding:.4rem .6rem">
      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> 2 pisos. A cada pis, 3 files de 5 bombons.</p>
{pisos(2, 3, 5, "2 pisos de 3 files de 5 bombons").svg("      ")}
      <p class="frase" style="margin:.2rem 0 0">{buit_curt()} · {buit_curt()} · {buit_curt()} = {buit_curt()} bombons.</p>
    </div>
  </div>

  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Fes un bloc de miniblocs: 2 pisos de 2 files de 2. Quants miniblocs hi ha?</div></div>
    <p class="frase" style="margin:.2rem 0 0">{buit_curt()} · {buit_curt()} · {buit_curt()} = {buit_curt()} miniblocs.</p>
  </div>

  <div class="clau" style="margin-top:.8rem">
    <p style="margin:0">Els tres factors primers són els pisos, les files i els bombons de cada fila.</p>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 2 · La factorització · full per al professorat</p>

  <div class="abans">
    <b>Abans de començar.</b> Decisió del docent (25/9/2026): nombres ben fàcils, de tres factors
    primers com a molt, i sense potències (2 · 2 · 3, i no 2² · 3). Cada pas de l'arbre és una
    multiplicació de la targeta, i per això cap nombre passa del 100. El conveni de la fitxa: a
    cada partició, el primer a l'esquerra i el que es torna a partir a la dreta. Així totes les
    plantilles tenen la mateixa forma. La factorització s'escriu de petit a gran.
  </div>

  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs: fer el bloc de 12, de 2 pisos de 2 files de 3. Són els tres factors
  de 12 = 2 · 2 · 3, i la pàgina 5 hi torna amb les capses de bombons.</p>

  <h3>1. Els arbres</h3>
  <p>b) 20 = 5 · 4 i 4 = 2 · 2: 20 = 2 · 2 · 5. c) 30 = 5 · 6 i 6 = 2 · 3: 30 = 2 · 3 · 5. d) 45 = 5 · 9 i
  9 = 3 · 3: 45 = 3 · 3 · 5. Es dona per bo qualsevol arbre que acabi en primers: el 20 també es pot
  fer 2 · 10, i el 10 = 2 · 5. Surti com surti, al final hi ha els mateixos primers: és l'«ADN» de
  l'activitat del grup. <b>Error típic:</b> posar el nombre que es torna a partir a l'esquerra, i
  quedar-se sense cercles. Que el giri: el conveni és només perquè la plantilla hi quadri.</p>

  <h3>2. Està acabada?</h3>
  <p>b) Sí; c) No: 20 = 2 · 2 · 5; d) Sí; e) No: 45 = 3 · 3 · 5; f) Sí. <b>Error típic:</b> aturar-se
  massa aviat: «12 = 3 · 4 ja està». És la regla trencada d'aquesta fitxa. No l'expliqueu: que
  miri si el 4 fa més d'un rectangle (la fitxa 3). Si en fa més d'un, no és primer, i la branca
  continua.</p>
</div>''')

pagines.append('''<div class="full sol">
  <h3>3. La recepta de cada nombre</h3>
  <table>
    <tr><th></th><th>Els dos primers</th><th>Pel tercer</th><th>El nombre</th></tr>
    <tr><td>b) 2 · 3 · 5</td><td>2 · 3 = 6</td><td>6 · 5 = 30</td><td>30</td></tr>
    <tr><td>c) 3 · 3 · 5</td><td>3 · 3 = 9</td><td>9 · 5 = 45</td><td>45</td></tr>
    <tr><td>d) 2 · 2 · 5</td><td>2 · 2 = 4</td><td>4 · 5 = 20</td><td>20</td></tr>
    <tr><td>e) 2 · 5 · 5</td><td>2 · 5 = 10</td><td>10 · 5 = 50</td><td>50</td></tr>
    <tr><td>f) 3 · 3 · 3</td><td>3 · 3 = 9</td><td>9 · 3 = 27</td><td>27</td></tr>
    <tr><td>g) 2 · 2 · 2</td><td>2 · 2 = 4</td><td>4 · 2 = 8</td><td>8</td></tr>
  </table>
  <p>És el camí de tornada de l'arbre, i totes les multiplicacions són de la targeta. És l'«ADN dels
  nombres» de l'activitat del grup: a l'alumnat se li diu «recepta», perquè les sigles en
  majúscules no són de Lectura Fàcil.</p>

  <h3>4 i 5. A la vida de cada dia</h3>
  <p>4b) 2 · 3 · 5 = 30 bombons. 5) 2 · 2 · 2 = 8 miniblocs: és el cub més petit que es pot fer amb
  miniblocs, a part d'un de sol. Els tres factors primers són les tres mides de la capsa: els
  pisos, les files i els de cada fila.</p>

  <h3>La caixa d'eines</h3>
  <p>A la caixa no hi ha una eina per als arbres. La 7.1 (els rectangles d'un nombre) ajuda a
  trobar les multiplicacions de cada pas, i la 8.2 (és primer?), a saber on s'acaba una branca.</p>

  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (1.4, 3.2, 4.2 i 5.2) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb miniblocs, fa un bloc de pisos i files, i diu quants n'hi ha multiplicant.</li>
    <li>Fa l'arbre d'un nombre amb la targeta i n'escriu la factorització (exercici 1).</li>
    <li>Diu si una factorització està acabada, i l'acaba si cal (exercici 2).</li>
    <li>Troba el nombre a partir de la seva factorització (exercici 3).</li>
    <li>Nivells alts: explica per què 12 = 3 · 4 no està acabada (exercici 2).</li>
  </ul>
</div>''')

document("Unitat 2 · La factorització", """  FITXA · Unitat 2 · Divisibilitat · La factorització
  La quarta fitxa de la unitat 2. Adapta les activitats 2_5 (factorització),
  2_8 i «ADN dels nombres» del grup, amb la decisió del docent del 25/9/2026:
  nombres de tres factors primers com a molt, sense potències. Cada pas de
  l'arbre és una multiplicació de la targeta (cap nombre passa del 100).

  El conveni de la fitxa: a cada partició, el primer a l'esquerra i el que es
  torna a partir a la dreta.

  La regla trencada és aturar-se abans d'hora: «12 = 3 · 4 ja està» (exercici
  2). La pàgina acaba amb la forma bona a la vista.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud2-factors.html")
