#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud6-repas.html: el repàs de la unitat 6 (fitxa 6).

Com el repàs de les unitats 4 i 5: «Una de cada» (un apartat per fitxa de la unitat) i «Què he
après?», amb la taula de «on es repassa» al solucionari. La pàgina de la vida és «La meva
Fotomàtica»: el projecte del grup (fotografiar l'entorn i analitzar-hi la geometria), amb una
plantilla de caselles. El mural es fa amb el grup.
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
pagina = fes_pagina(pagines, "Unitat 6 · Repàs · pàgina")

# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>el geoplà i un full</b>. Fer un rectangle i buscar-hi les cantonades amb el full.</div>
  <h1>Repàs de la unitat</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:.8rem">
{figura_quadrets(rectangle_cel(3, 4), 0.85, "Un rectangle de 3 files de 4 quadrets, amb la vora gruixuda", rotuls=True).svg()}
  </div>
  <table style="margin-top:.4rem">
    <tr class="resolt"><td class="esq">Quants costats té? Com es diu?</td><td style="width:5.6cm">{ms("4: quadrilàter")}</td></tr>
    <tr class="resolt"><td class="esq">Quants angles rectes té?</td><td>{ms("4")}</td></tr>
    <tr class="resolt"><td class="esq">Quin és el perímetre?</td><td>{ms("4 + 3 + 4 + 3 = 14")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Tota la unitat fa servir la cantonada d'un quadret.</p>
    <p style="margin:.2rem 0 0">Els angles es comparen amb la cantonada. El perímetre és la vora.</p>
  </div>''')


# ===================================================================== pàgina 2: una de cada
def item(l, recorda, cos, r=False):
    return caixa(f'''      <p style="margin:0;font-size:14pt;color:var(--gris-2)"><span class="apartat" style="color:var(--tinta)">{l})</span> {recorda}</p>
      <div class="frase" style="margin:0;font-size:16pt">{cos}</div>''', r, ".3rem")


fila = lambda dib, cos: f'<div style="display:flex;gap:.6cm;align-items:center"><div>{dib.svg("")}</div><div>{cos}</div></div>'
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Una de cada. Fes cada apartat amb el que ja saps.</div></div>
{item("a", "Els angles. Quin angle és?", fila(angle_d(130, "Un angle, amb la cantonada al vèrtex", llarg=1.4), tria(["Agut", "Recte", "Obtús", "Pla"], "Obtús", mida="14pt", ample="2.2cm")), True)}
{item("b", "Els polígons. Com es diu?", fila(geopla_d([[1, 0], [4, 0], [5, 2], [4, 4], [1, 4], [0, 2]], "Un polígon al geoplà", m=0.4), "Nom: " + buit()))}
{item("c", "Els triangles. Com es diu pels angles?", fila(triangle_d([(0, 0), (2.4, 0), (0, 1.6)], "Un triangle"), tria(["Rectangle", "Acutangle", "Obtusangle"], None, mida="14pt", ample="2.9cm", ajusta=True)))}
{item("d", "El perímetre. Compta la vora.", fila(figura_quadrets(rectangle_cel(2, 4), 0.45, "Un rectangle de 2 files de 4 quadrets", rotuls=True), "Perímetre: " + buit()))}
{item("e", "La circumferència. El radi fa 6 cm.", "El diàmetre fa " + buit_curt() + " cm.")}
  </div>''')

# ===================================================================== pàgina 3: què he après?
FR = [("Comparo un angle amb la cantonada d'un quadret.", "Més petit: agut. Més gran: obtús."),
      ("Dic el nom de les peces: punt, segment, semirecta i recta.", "La recta no té extrems."),
      ("Compto els costats d'un polígon i en dic el nom.", "5 costats: pentàgon"),
      ("Reconec un quadrat, encara que estigui girat.", "4 costats iguals i 4 cantonades"),
      ("Dic com és un triangle pels costats i pels angles.", "Equilàter, rectangle…"),
      ("Sé que els tres angles d'un triangle fan un angle pla.", "Retallats i junts, fan una recta"),
      ("Compto el perímetre: la vora, no els quadrets de dins.", "4 + 3 + 4 + 3 = 14"),
      ("Sé que el diàmetre és el doble del radi.", "Radi 3 cm, diàmetre 6 cm")]
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

# ===================================================================== pàgina 4: la vida (la meva Fotomàtica)
cas = lambda t, h="2.2cm": f'<tr><td class="esq" style="width:7cm">{t}</td><td class="omplir" style="height:{h}"></td></tr>'
pagina(f'''  <h2>A la vida de cada dia: la meva Fotomàtica</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Fes una foto d'una cosa de casa o del barri que tingui formes. Enganxa la foto o fes un dibuix.</div></div>
    <div style="border:2.5px dashed var(--vora);border-radius:12px;height:6.5cm;display:flex;align-items:center;justify-content:center;color:var(--gris-2);font-size:14pt">La foto o el dibuix</div>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Mira la foto. Omple les caselles. Mira la targeta.</div></div>
    <table>
      {cas("Quines formes hi veus?")}
      {cas("Quants costats té la forma més gran?", "1.5cm")}
      {cas("Hi ha angles rectes? On?", "1.8cm")}
      {cas("Hi ha rectes paral·leles? On?", "1.8cm")}
    </table>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 6 · Repàs de la unitat · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> És la fitxa de repàs: va després de les altres cinc de la unitat. «Una de
    cada» torna a cada fitxa, i «Què he après?» és la llista de comprovació. «La meva Fotomàtica» és
    el projecte del grup, amb una plantilla de caselles: la foto es pot fer a casa, o triar-ne una de
    les del centre. La targeta «Formes» és al davant tota l'estona.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb el geoplà i un full: fer un rectangle i posar la cantonada del full a cada
  cantonada. Totes quatre són angles rectes.</p>
  <h3>1. Una de cada</h3>
  <p>b) hexàgon (6 costats). c) rectangle. d) 4 + 2 + 4 + 2 = 12. e) 12 cm. Cada apartat torna a una
  fitxa de la unitat: si un no surt, aquella fitxa és la que cal repassar.</p>
  <h3>2 i 3. La meva Fotomàtica</h3>
  <p>No hi ha una resposta única. Es mira que faci servir les paraules de la targeta (polígon, costat,
  angle recte, paral·leles) i que el que diu es vegi a la foto. Si ho explica de paraula, val igual:
  la programació ho preveu (text, àudio o dibuix). <b>Compta per als nivells alts</b> que en calculi
  un perímetre.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>La pàgina 3: «Què he après?»</h3>
  <p>L'alumnat marca una casella a cada frase. L'adult tria dues frases de «Ho sé fer» i li demana que
  ho ensenyi amb un exemple. Les de «Encara no» diuen què s'ha de repassar, i on:</p>
  <table>
    <tr><th>Frase</th><th>On es repassa</th></tr>
    <tr><td>1 i 2 · angles i peces</td><td>Fitxa 1; caixa 22</td></tr>
    <tr><td>3 i 4 · polígons</td><td>Fitxa 2; caixa 23</td></tr>
    <tr><td>5 i 6 · triangles</td><td>Fitxa 3; caixa 24</td></tr>
    <tr><td>7 · perímetre</td><td>Fitxa 4; caixa 25</td></tr>
    <tr><td>8 · circumferència</td><td>Fitxa 5</td></tr>
  </table>
  <h3>La caixa d'eines</h3>
  <p>Per repassar, amb l'ordinador: les tasques 22 a 25. Les tasques tancades (22.2, 23.2, 24.2 i 25.2)
  donen un codi de verificació, i es poden fer abans de l'examen.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta «Formes» al davant. Els criteris de la SA del grup (1.1, 3.1, 5.1, 6.1, 7.1 i
  9.1) són de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Fa un apartat de cada tipus de la unitat (exercici 1).</li>
    <li>Diu en veu alta què sap fer i què ha de repassar, i ho ensenya amb un exemple (pàgina 3).</li>
    <li>Descriu una foto del seu entorn amb les paraules de la geometria (exercicis 2 i 3).</li>
  </ul>
</div>''')

document("Unitat 6 · Repàs de la unitat", """  FITXA · Unitat 6 · Sentit espacial · Repàs de la unitat
  La sisena fitxa de la unitat 6, i l'última abans de l'examen. «Una de cada»
  torna a cada fitxa, «Què he après?» és la llista de comprovació, i «La meva
  Fotomàtica» és el projecte del grup, amb una plantilla de caselles.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud6-repas.html")
