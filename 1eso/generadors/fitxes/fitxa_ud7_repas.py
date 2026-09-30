#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud7-repas.html: el repàs de la unitat 7 i «El meu curs» (fitxa 5).

L'última fitxa del curs. Com els repassos de les unitats 4 a 6: «Una de cada» i «Què he après?». I
«El meu curs», que fa el paper del mapa conceptual final del grup (activitat 6 de la SA7): un
exemple de cada unitat de l'any, amb el mateix model de quadrets. La pàgina de la vida és un patró
trobat a l'entorn, que és el dossier del grup (activitat 7).
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
from peces_comunes import *  # noqa: F401,F403
from peces_ud2 import *  # noqa: F401,F403
from peces_fraccions import *  # noqa: F401,F403
from peces_geo import *  # noqa: F401,F403

pagines = []
pagina = fes_pagina(pagines, "Unitat 7 · Repàs · pàgina")

# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs</b>. Fer les figures 1, 2 i 3 del patró 3 · n + 1 i dir la figura 4.</div>
  <h1>Repàs de la unitat</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div style="display:flex;gap:1.2cm;align-items:flex-end;justify-content:center;margin-top:.8rem">
    {figures_d(3, 1, 3, 0.5, "El patró 3 · n + 1")}
  </div>
  <table style="margin-top:.6rem">
    <tr class="resolt"><td class="esq">Quants quadrets té cada figura?</td><td style="width:4.6cm">{ms("4, 7 i 10")}</td></tr>
    <tr class="resolt"><td class="esq">La regla</td><td>{ms("3 · n + 1")}</td></tr>
    <tr class="resolt"><td class="esq">La figura 10</td><td>{ms("3 · 10 + 1 = 31")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Tota la unitat fa servir els quadrets.</p>
    <p style="margin:.2rem 0 0">Els patrons creixen de quadrets en quadrets. Un gràfic de barres són columnes de quadrets.</p>
  </div>''')


# ===================================================================== pàgina 2: una de cada
def item(l, recorda, cos, r=False):
    return caixa(f'''      <p style="margin:0;font-size:14pt;color:var(--gris-2)"><span class="apartat" style="color:var(--tinta)">{l})</span> {recorda}</p>
      <div class="frase" style="margin:0;font-size:16pt">{cos}</div>''', r, ".3rem")


pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Una de cada. Fes cada apartat amb el que ja saps.</div></div>
{item("a", "El patró. Quin és el nombre següent?", "4, 7, 10, 13, " + ms("16"), True)}
{item("b", "La regla. Escriu la regla del patró 5, 7, 9, 11.", "La regla: " + buit())}
{item("c", "El símbol. Escriu el triple d'un nombre.", "El símbol: " + buit())}
{item("d", "Calcula. Si n és 5, quant és 2 · n + 1?", "2 · 5 + 1 = " + buit_curt())}
{item("e", "El gràfic. Mira la barra de la bici.", '<div style="display:flex;gap:.6cm;align-items:center"><div>' + barres_d([("A peu", 12), ("Bus", 8), ("Bici", 6), ("Cotxe", 4)], "Gràfic de barres: a peu 12, bus 8, bici 6, cotxe 4", m=0.28).svg("") + "</div><div>Bici: " + buit_curt() + " alumnes</div></div>")}
  </div>''')

# ===================================================================== pàgina 3: què he après?
FR = [("Dic quants quadrets té la figura següent d'un patró.", "3, 5, 7: la següent, 9"),
      ("Dic què és fix i què creix en un patró.", "El quadret blanc és fix"),
      ("Faig servir una regla per saber una figura.", "2 · n + 1: la figura 10 té 21"),
      ("Escric la regla d'un patró, amb la part fixa.", "5, 8, 11: 3 · n + 2"),
      ("Escric una frase amb símbols.", "El triple d'un nombre: 3 · n"),
      ("Calculo per a un valor de n.", "Si n és 4: 3 · 4 = 12"),
      ("Llegeixo un gràfic de barres.", "A peu: 12 alumnes"),
      ("Miro on comença l'eix d'un gràfic.", "Ha de començar a 0")]
files_q = "\n".join(
    f'''      <tr><td class="esq" style="padding:.15rem .5rem;line-height:1.3">{f_}<br><span style="font-size:14pt;color:var(--gris-2)">{ex}</span></td>'''
    f'''<td><span class="quadret" style="margin:0"></span></td><td><span class="quadret" style="margin:0"></span></td>'''
    f'''<td><span class="quadret" style="margin:0"></span></td></tr>''' for f_, ex in FR)
pagina(f'''  <h2>Què he après?</h2>
  <p style="margin:.1rem 0 0">Llegeix cada frase. Marca una casella.</p>
  <table class="mini" style="margin-top:.3rem">
    <tr><th style="text-align:left">Què sé fer</th><th style="width:2.4cm">Ho sé fer</th><th style="width:2.4cm">L'he de repassar</th><th style="width:2.4cm">Encara no</th></tr>
{files_q}
  </table>''')

# ===================================================================== pàgina 4: el meu curs
CURS = [("1 · Nombres naturals", "Multiplicar és fer un rectangle de quadrets.", "3 · 4 =", True),
        ("2 · Divisibilitat", "Els divisors són els costats dels rectangles.", "Els divisors de 6:", False),
        ("3 · Fraccions", "Una fracció és un tros d'una tira.", f"{fr(1, 4, '14pt')} + {fr(2, 4, '14pt')} =", False),
        ("4 · Percentatges", "El percentatge són quadrets de cada 100.", "El 25 % de 100 quadrets:", False),
        ("5 · Decimals", "El quadrat de 100 és 1: la columna és 0,1.", "2,5 + 1,3 =", False),
        ("6 · Formes", "El perímetre és la vora.", "El perímetre d'un rectangle de 3 per 4:", False),
        ("7 · Patrons", "El triple d'un nombre és 3 · n.", "Si n és 5, 3 · n =", False)]
files_c = "\n".join(f'''      <tr{' class="resolt"' if r else ''}><td style="padding:.25rem .4rem;font-weight:800;font-size:14pt;text-align:left">{u}</td>
        <td style="padding:.25rem .4rem;font-size:14pt;text-align:left">{idea}</td>
        <td style="padding:.25rem .4rem;font-size:14pt;text-align:left">{ex}{" " + ms("12") if r else ""}</td></tr>''' for u, idea, ex, r in CURS)
pagina(f'''  <h2>El meu curs</h2>
  <p style="margin:.1rem 0 .3rem">Aquest curs has fet servir sempre els quadrets. Fes l'exemple de cada unitat.</p>
  <table class="mini" style="width:100%;table-layout:fixed">
    <tr><th style="width:4.3cm">Unitat</th><th>La idea</th><th style="width:6.4cm">Un exemple</th></tr>
{files_c}
  </table>''')

# ===================================================================== pàgina 5: la vida (el meu patró)
cas = lambda t, h="1.6cm": f'<tr><td class="esq" style="width:6.5cm">{t}</td><td class="omplir" style="height:{h}"></td></tr>'
pagina(f'''  <h2>A la vida de cada dia: el meu patró</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Busca un patró a casa o al carrer: unes rajoles, una escala, una tanca. Dibuixa tres figures del patró.</div></div>
    <div style="border:2.5px dashed var(--vora);border-radius:12px;height:6cm;display:flex;align-items:center;justify-content:center;color:var(--gris-2);font-size:14pt">El dibuix o la foto</div>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Omple les caselles.</div></div>
    <table>
      {cas("Què és fix?")}
      {cas("Què creix a cada figura?")}
      {cas("Quants en té la figura 4?")}
      {cas("La regla (si la saps)")}
    </table>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append(f'''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 7 · Repàs i el meu curs · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> És l'última fitxa del curs. «Una de cada» torna a cada fitxa de la unitat,
    «Què he après?» és la llista de comprovació, i «El meu curs» fa el paper del mapa conceptual final
    del grup: una idea i un exemple de cada unitat, tots amb quadrets. «El meu patró» és el dossier del
    grup. Totes les targetes són al davant.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs: el patró 3 · n + 1, amb el bloc fix d'un altre color.</p>
  <h3>1. Una de cada</h3>
  <p>b) 2 · n + 3. c) 3 · n. d) 11. e) 6 alumnes. Cada apartat torna a una fitxa de la unitat.</p>
  <h3>La pàgina 4: el meu curs</h3>
  <p>2) 1, 2, 3 i 6 (els rectangles de 6 quadrets). 3) {fr(3, 4)}. 4) 25 quadrets. 5) 3,8. 6) 14. 7) 15.
  Si un exemple no surt, és la unitat que cal repassar abans de 2n: la targeta de cada unitat i la seva
  tasca de la caixa hi ajuden.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>La pàgina 3: «Què he après?»</h3>
  <p>L'alumnat marca una casella a cada frase. L'adult tria dues frases de «Ho sé fer» i li demana que
  ho ensenyi amb un exemple. Les de «Encara no» diuen què s'ha de repassar, i on:</p>
  <table>
    <tr><th>Frase</th><th>On es repassa</th></tr>
    <tr><td>1 i 2 · patrons</td><td>Fitxa 1; caixa 26</td></tr>
    <tr><td>3 i 4 · la regla</td><td>Fitxa 2; caixa 26.1</td></tr>
    <tr><td>5 i 6 · els símbols</td><td>Fitxa 3; caixa 27</td></tr>
    <tr><td>7 i 8 · els gràfics</td><td>Fitxa 4; caixa 28</td></tr>
  </table>
  <h3>2 i 3. El meu patró</h3>
  <p>No hi ha una resposta única. Es mira que distingeixi què és fix i què creix, i que la figura 4 surti
  bé. La regla compta per als nivells alts. Si ho explica de paraula o amb una foto, val igual: la
  programació ho preveu.</p>
  <h3>La caixa d'eines</h3>
  <p>Per repassar, amb l'ordinador: les tasques 26 a 28. Les tasques tancades (26.2, 27.2 i 28.2) donen
  un codi de verificació, i es poden fer abans de l'examen.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb les targetes al davant. Els criteris de la SA del grup (2.1, 3.1, 4.1, 5.1 i 7.2) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Fa un apartat de cada tipus de la unitat (exercici 1).</li>
    <li>Diu en veu alta què sap fer i què ha de repassar, i ho ensenya amb un exemple (pàgina 3).</li>
    <li>Fa un exemple de cada unitat del curs (pàgina 4).</li>
    <li>Troba un patró al seu entorn i en diu què és fix i què creix (exercicis 2 i 3).</li>
  </ul>
</div>''')

document("Unitat 7 · Repàs i el meu curs", """  FITXA · Unitat 7 · Llenguatge algebraic i patrons · Repàs i el meu curs
  L'última fitxa del curs. «Una de cada», «Què he après?», «El meu curs» (una idea
  i un exemple de cada unitat, en lloc del mapa conceptual del grup) i «El meu
  patró» (el dossier del grup).""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud7-repas.html")
