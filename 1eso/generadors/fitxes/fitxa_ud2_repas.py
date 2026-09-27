#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud2-repas.html: el repàs de la unitat 2 (fitxa 5).
Adapta el Repàs U2 del grup (amb el carnet d'identitat de cada nombre) i hi afegeix
«Què he après?», com a la unitat 1."""
import os
import sys
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_ud2.py"), encoding="utf-8").read())

pagines = []
pagina = fes_pagina(pagines, "Unitat 2 · Repàs · pàgina")
ARBRE12 = [(3, 4), (2, 2)]
FILES_CARNET = ["Tres múltiples", "Tots els divisors", "És primer?", "La factorització", "Els trucs"]


def carnet(n, valors=None):
    """El carnet d'identitat d'un nombre. Amb `valors`, ple a mà (el model)."""
    files = []
    for i, et in enumerate(FILES_CARNET):
        if valors:
            cel = f'<td class="esq" style="padding:.35rem .6rem">{ms(valors[i])}</td>'
        elif et == "Els trucs":
            cel = ('<td class="esq" style="padding:.35rem .6rem;font-size:14pt">Del 2: ' + buit_curt() + ' · Del 5: ' + buit_curt() +
                   ' · Del 10: ' + buit_curt() + ' · Del 3: ' + buit_curt() + '</td>')
        else:
            cel = '<td class="omplir" style="height:1.15cm"></td>'
        cls = ' class="resolt"' if valors else ""
        files.append(f'<tr{cls}><th class="esq" style="width:4.3cm;text-align:left">{et}</th>{cel}</tr>')
    return (f'<table class="mini" style="margin:.2rem 0 .6rem"><tr><th colspan="2" style="font-size:17pt;text-align:left">'
            f'El carnet del {n}</th></tr>' + "".join(files) + "</table>")


# ===================================================================== pàgina 1
d1 = dibuix_rectangles(12, 0.36, "Els tres rectangles del 12")
d2 = arbre(12, ARBRE12, "L'arbre del 12", m=0.72)
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>la targeta de les taules i miniblocs</b>. Fer els rectangles del 12 i dir-ne els divisors.</div>
  <h1>Repàs de la unitat</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div style="display:flex;gap:1.2cm;align-items:center;justify-content:center;margin-top:.6rem">
    <div style="flex:0 0 auto">
{d1.svg("      ")}
    </div>
    <div style="flex:0 0 4.8cm">
{d2.svg("      ")}
    </div>
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .5rem">Hi ha els rectangles del 12 i el seu arbre.</p>

  {carnet(12, ["12, 24, 36", "1, 2, 3, 4, 6 i 12", "No: fa 3 rectangles", "12 = 2 · 2 · 3",
               "Del 2: sí · Del 5: no · Del 10: no · Del 3: sí (1 + 2 = 3)"])}

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">El carnet d'identitat d'un nombre diu tot el que en saps.</p>
  </div>''')

# ===================================================================== pàgines 2 i 3: els carnets
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Fes el carnet d'identitat de cada nombre. Mira la targeta.</div></div>
    <div class="avis puntejat" style="margin:.3rem 0 .5rem">Fes-ho fila a fila, com el carnet del 12.</div>
    <p style="margin:.3rem 0 0;font-weight:700"><span class="apartat">a)</span></p>
    {carnet(18)}
    <p style="margin:.3rem 0 0;font-weight:700"><span class="apartat">b)</span></p>
    {carnet(20)}
  </div>''')

pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Continua: el carnet d'un nombre primer.</div></div>
    <p style="margin:.3rem 0 0;font-weight:700"><span class="apartat">c)</span></p>
    {carnet(7)}
  </div>

  <div class="clau" style="margin-top:.6rem">
    <p style="margin:0">Un nombre primer només té dos divisors: l'1 i ell mateix.</p>
    <p style="margin:0">La seva factorització és el mateix nombre: 7.</p>
  </div>''')

# ===================================================================== pàgina 4: una de cada
def item(lletra, recorda, cos, resolt=False):
    fons = (' class="resolt" style="border-radius:10px;padding:.3rem .6rem;margin-bottom:.35rem"' if resolt
            else ' style="padding:.3rem .6rem;margin-bottom:.35rem"')
    return f'''    <div{fons}>
      <p style="margin:0;font-size:14pt;color:var(--gris-2)"><span class="apartat" style="color:var(--tinta)">{lletra})</span> {recorda}</p>
      <p class="frase" style="margin:0;font-size:17pt">{cos}</p>
    </div>'''


pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Una de cada. Fes-les amb el que ja saps.</div></div>
{item("a", "Els múltiples són la taula.", "24 és múltiple de 3? " + ms("Sí: 3 · 8 = 24"), True)}
{item("b", "Files plenes i els que sobren.", "37 en files de 7: 37 = " + buit_curt() + " · 7 + " + buit_curt())}
{item("c", "Els divisors surten dels rectangles.", "Els divisors del 10: " + buit())}
{item("d", "Un primer només fa una fila.", "15 és primer? " + buit_curt())}
{item("e", "L'arbre, amb la targeta.", "20 = " + buit_curt() + " · " + buit_curt() + " · " + buit_curt())}
{item("f", "El truc del 3: suma les xifres.", "123: 1 + 2 + 3 = " + buit_curt() + ". És múltiple de 3? " + buit_curt())}
  </div>''')

# ===================================================================== pàgina 5: què he après?
FRASES = [
    ("Escric els múltiples d'un nombre.", "Múltiples del 3: 0, 3, 6, 9…"),
    ("Faig el truc de l'última xifra.", "340 acaba en 0: és múltiple de 10"),
    ("Faig el truc del 3.", "126: 1 + 2 + 6 = 9, és a la taula del 3"),
    ("Reparteixo en files i dic el residu.", "37 = 5 · 7 + 2"),
    ("Trobo tots els rectangles d'un nombre.", "12 = 1 · 12 = 2 · 6 = 3 · 4"),
    ("Escric els divisors d'un nombre.", "Divisors del 12: 1, 2, 3, 4, 6 i 12"),
    ("Sé si un nombre és primer.", "7 només fa una fila"),
    ("Faig el garbell.", "Els primers: 2, 3, 5, 7, 11…"),
    ("Faig l'arbre d'un nombre.", "12 = 2 · 2 · 3"),
    ("Faig el carnet d'un nombre.", "El carnet del 12"),
]
files_q = "\n".join(
    f'''      <tr><td class="esq" style="padding:.18rem .5rem;line-height:1.25">{fr}<br><span style="font-size:14pt;color:var(--gris-2)">{ex}</span></td>'''
    f'''<td><span class="quadret" style="margin:0"></span></td><td><span class="quadret" style="margin:0"></span></td>'''
    f'''<td><span class="quadret" style="margin:0"></span></td></tr>''' for fr, ex in FRASES)
pagina(f'''  <h2>Què he après?</h2>
  <p style="margin:.1rem 0 0">Llegeix cada frase. Marca una casella.</p>
  <table class="mini" style="margin-top:.4rem">
    <tr><th style="text-align:left">Què sé fer</th><th style="width:2.5cm">Ho sé fer</th><th style="width:2.5cm">L'he de repassar</th><th style="width:2.5cm">Encara no</th></tr>
{files_q}
  </table>
  <p class="frase" style="margin:.6rem 0 0;font-size:15pt">El que m'ha agradat més: <u style="display:inline-block;min-width:9cm;padding:0"></u></p>
  <p class="frase" style="margin:0;font-size:15pt">El que m'ha costat més: <u style="display:inline-block;min-width:9.4cm;padding:0"></u></p>''')

# ===================================================================== pàgina 6: la vida
pagina(f'''  <h2>A la vida de cada dia</h2>

  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Anem d'excursió 24 persones. Es poden fer grups iguals?</div></div>
    <div class="resolt" style="border-radius:10px;padding:.4rem .6rem;margin-bottom:.5rem">
      <p style="margin:0 0 .1rem"><span class="apartat">a)</span> Grups de 4.</p>
      {tria(["Sí", "No"], "Sí", mida="14pt", ample="2.5cm")}
      <p class="frase" style="margin:0">{ms("24 = 6 · 4")}: {ms("6")} grups. No en sobra cap.</p>
    </div>
    <div style="padding:.4rem .6rem">
      <p style="margin:0 0 .1rem"><span class="apartat">b)</span> Grups de 5.</p>
      {tria(["Sí", "No"], mida="14pt", ample="2.5cm")}
      <p class="frase" style="margin:0">24 = {buit_curt()} · 5 + {buit_curt()}</p>
    </div>
    <div style="padding:.4rem .6rem">
      <p style="margin:0 0 .1rem"><span class="apartat">c)</span> Grups de 6.</p>
      {tria(["Sí", "No"], mida="14pt", ample="2.5cm")}
      <p class="frase" style="margin:0">24 = {buit_curt()} · 6 + {buit_curt()}</p>
    </div>
  </div>

  <div class="clau" style="margin-top:.6rem">
    <p style="margin:0">Els grups iguals que es poden fer són els divisors del 24.</p>
    <p style="margin:0">Si en sobren, el nombre no és divisor.</p>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 2 · Repàs de la unitat · full per al professorat</p>

  <div class="abans">
    <b>Abans de començar.</b> És la fitxa de repàs: va després de les altres quatre de la unitat.
    El carnet d'identitat és el del Repàs U2 del grup (múltiples, divisors i factorització), amb
    dues files més: si és primer i els trucs. La targeta és al davant tota l'estona. La pàgina 5,
    «Què he après?», no es corregeix: serveix per parlar-ne, i per saber què s'ha de repassar
    abans de l'examen.
  </div>

  <h3>1. Els carnets</h3>
  <table>
    <tr><th></th><th>El 18</th><th>El 20</th><th>El 7</th></tr>
    <tr><td>Tres múltiples</td><td>18, 36, 54</td><td>20, 40, 60</td><td>7, 14, 21</td></tr>
    <tr><td>Tots els divisors</td><td>1, 2, 3, 6, 9 i 18</td><td>1, 2, 4, 5, 10 i 20</td><td>1 i 7</td></tr>
    <tr><td>És primer?</td><td>No</td><td>No</td><td>Sí</td></tr>
    <tr><td>La factorització</td><td>18 = 2 · 3 · 3</td><td>20 = 2 · 2 · 5</td><td>7 és primer</td></tr>
    <tr><td>Els trucs (2, 5, 10, 3)</td><td>Sí, no, no, sí (1 + 8 = 9)</td><td>Sí, sí, sí, no (2 + 0 = 2)</td><td>No, no, no, no</td></tr>
  </table>
  <p>El 18 i el 20 són els carnets de l'examen de la unitat 2 que ja feia servir el departament, i el
  7 hi és perquè hi hagi un primer. Es dona per bo qualsevol trio de múltiples, si són de la taula.</p>

  <h3>2. Una de cada</h3>
  <p>b) 37 = 5 · 7 + 2; c) 1, 2, 5 i 10; d) no: 15 = 3 · 5; e) 20 = 2 · 2 · 5; f) 6, i sí. Cada apartat
  torna a una fitxa de la unitat: si un no surt, aquella fitxa és la que cal repassar (vegeu la
  taula del full següent).</p>

  <h3>3. A la vida de cada dia</h3>
  <p>b) No: 24 = 4 · 5 + 4, en sobren 4. c) Sí: 24 = 4 · 6 + 0, 4 grups. Els grups iguals que es poden
  fer són els divisors del 24: 1, 2, 3, 4, 6, 8, 12 i 24.</p>
</div>''')

pagines.append('''<div class="full sol">
  <h3>La pàgina 5: «Què he après?»</h3>
  <p>L'alumnat marca una casella a cada frase. L'adult tria dues frases de «Ho sé fer» i li demana
  que ho ensenyi amb un exemple. Les de «Encara no» diuen què s'ha de repassar, i on:</p>
  <table>
    <tr><th>Frase</th><th>On es repassa</th></tr>
    <tr><td>1, 2 i 3 · els múltiples i els trucs</td><td>Fitxa 1; caixa 5.1 a 5.4</td></tr>
    <tr><td>4 · repartir, el residu</td><td>Fitxa 2; caixa 6.1 i 6.2</td></tr>
    <tr><td>5, 6 i 7 · els rectangles, els divisors, els primers</td><td>Fitxa 3; caixa 7.1, 7.2 i 8.2</td></tr>
    <tr><td>8 · el garbell</td><td>Fitxa 3, exercici 4; caixa 8.1</td></tr>
    <tr><td>9 · l'arbre</td><td>Fitxa 4</td></tr>
    <tr><td>10 · el carnet</td><td>Aquesta fitxa, exercici 1</td></tr>
  </table>

  <h3>La caixa d'eines</h3>
  <p>Per repassar, amb l'ordinador: les tasques de la 5 a la 8. Les cinc tasques tancades (5.2, 5.4,
  6.2, 7.2 i 8.2) donen un codi de verificació, i es poden fer abans de l'examen, en l'ordre de
  la taula de dalt.</p>

  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (1.4, 3.2, 4.2 i 5.2) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Fa el carnet d'identitat d'un nombre, fila a fila, amb la targeta (exercici 1).</li>
    <li>Fa una operació de cada tipus de la unitat (exercici 2).</li>
    <li>Diu en veu alta què sap fer i què ha de repassar, i ho ensenya amb un exemple (pàgina 5).</li>
    <li>Nivells alts: decideix si es poden fer grups iguals en una situació de debò (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 2 · Repàs de la unitat", """  FITXA · Unitat 2 · Divisibilitat · Repàs de la unitat
  La cinquena fitxa de la unitat 2, i l'última abans de l'examen. Adapta el
  Repàs U2 del grup, amb el carnet d'identitat de cada nombre (múltiples,
  divisors, primer, factorització i trucs), i hi afegeix «Què he après?», com
  a la unitat 1. Els nombres dels carnets (18 i 20) són els de l'examen de
  la unitat 2 que ja feia servir el departament; el 7, perquè hi hagi un primer.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud2-repas.html")
