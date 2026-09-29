#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud5-repas.html: el repàs de la unitat 5 (fitxa 6).

Adapta les activitats 6 (el mapa conceptual del bloc numèric) i 7 (el projecte de les rajoles) de
la situació «Decimals i arrel quadrada». El mapa conceptual es fa amb el grup; aquí en fa el paper
«el carnet d'un nombre»: la fracció, el decimal, el percentatge i els quadrets de 100 són cares del
mateix nombre (el fil del llibre, «Un nombre, moltes cares»). Les rajoles, amb un plànol quadriculat
i les mesures donades (el mateix llibre ho proposa per a l'alumnat amb suports): files per columnes,
i si l'última fila és mitja rajola, en cal una de sencera.

Com el repàs de la unitat 4: «Una de cada» (un apartat per cada fitxa de la unitat) i «Què he
après?», amb la taula de «on es repassa» al solucionari.
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(AQUI, "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])                       # Dibuix, ms, buit, ULL, els colors
exec(open(os.path.join(AQUI, "peces_ud2.py"), encoding="utf-8").read())          # tria, fes_pagina, document
exec(open(os.path.join(AQUI, "peces_fraccions.py"), encoding="utf-8").read())    # fr, fr_buit, caixa

pagines = []
pagina = fes_pagina(pagines, "Unitat 5 · Repàs · pàgina")


def quadrat100(n, m, aria):
    """El quadrat de 100 pintat per columnes, com a la fitxa 4, a la caixa (tasca 21) i a la targeta."""
    d = Dibuix(10 * m + 0.2, 10 * m + 0.2, aria)
    x0 = y0 = 0.1
    for i in range(n):
        col, fila = divmod(i, 10)
        d.cru(f'<rect x="{d.px(x0 + col * m)}" y="{d.px(y0 + fila * m)}" width="{d.px(m)}" height="{d.px(m)}" '
              f'fill="{F3}" stroke="none"/>')
    for k in range(1, 10):
        d.cru(f'<line x1="{d.px(x0)}" y1="{d.px(y0 + k * m)}" x2="{d.px(x0 + 10 * m)}" y2="{d.px(y0 + k * m)}" '
              f'stroke="{G3}" stroke-width="0.9"/>')
        d.cru(f'<line x1="{d.px(x0 + k * m)}" y1="{d.px(y0)}" x2="{d.px(x0 + k * m)}" y2="{d.px(y0 + 10 * m)}" '
              f'stroke="{G3}" stroke-width="0.9"/>')
    d.cru(f'<rect x="{d.px(x0)}" y="{d.px(y0)}" width="{d.px(10 * m)}" height="{d.px(10 * m)}" fill="none" '
          f'stroke="{G1}" stroke-width="2"/>')
    return d


def planol(llarg, ample10, m, aria):
    """El plànol d'una habitació de `llarg` metres per `ample10`/10 metres, amb rajoles d'1 m: un
    quadret per rajola. Si l'amplada acaba en mig metre, l'última fila són rajoles senceres que
    sobresurten del plànol: la meitat de fora, discontínua, és el tros que es retalla."""
    files, mig = divmod(ample10, 10)
    esq, dalt = 1.9, 0.8
    alt = (files + (1 if mig else 0)) * m
    d = Dibuix(esq + llarg * m + 0.2, dalt + alt + 0.2, aria)
    d.rectangle(esq, dalt, files, llarg, m)
    if mig:
        y = dalt + files * m
        for c in range(llarg):
            x = esq + c * m
            d.cru(f'<rect x="{d.px(x + 0.05 * m)}" y="{d.px(y + 0.05 * m)}" width="{d.px(0.9 * m)}" height="{d.px(0.45 * m)}" '
                  f'fill="{F3}" stroke="{G1}" stroke-width="1.6"/>')
            d.cru(f'<rect x="{d.px(x + 0.05 * m)}" y="{d.px(y + 0.5 * m)}" width="{d.px(0.9 * m)}" height="{d.px(0.45 * m)}" '
                  f'fill="none" stroke="{G2}" stroke-width="1.3" stroke-dasharray="4 3"/>')
    # La vora de l'habitació, gruixuda
    d.cru(f'<rect x="{d.px(esq)}" y="{d.px(dalt)}" width="{d.px(llarg * m)}" height="{d.px(files * m + (0.5 * m if mig else 0))}" '
          f'fill="none" stroke="{NEGRE}" stroke-width="3"/>')
    d.clau_dalt(esq, esq + llarg * m, dalt - 0.3, f"{llarg} m", 0.45)
    ample = f"{files},5 m" if mig else f"{files} m"
    d.clau_esq(esq - 0.3, dalt, dalt + files * m + (0.5 * m if mig else 0), ample, 0.45)
    return d


# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>la quadrícula de 100</b>. Pintar-ne 25 quadrets i dir-ho de quatre maneres: un quart, 0,25, el 25 % i 25 quadrets.</div>
  <h1>Repàs de la unitat</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:.8rem;width:4.8cm;margin-left:auto;margin-right:auto">
{quadrat100(25, 0.45, "El quadrat de 100 amb 25 quadrets pintats").svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.5rem 0 .5rem">Un nombre, moltes cares.</p>
  <table class="mini">
    <tr><th>Fracció</th><th>Decimal</th><th>Percentatge</th><th>Quadrets de 100</th></tr>
    <tr class="resolt"><td style="text-align:center">{fr(1, 4, ma=True)}</td><td style="text-align:center">{ms("0,25")}</td>
      <td style="text-align:center">{ms("25 %")}</td><td style="text-align:center">{ms("25")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Tota la unitat fa servir el mateix quadrat de 100.</p>
    <p style="margin:.2rem 0 0">Una columna és 0,1. Un quadret és 0,01. El costat d'un quadrat és l'arrel.</p>
  </div>''')

# ===================================================================== pàgina 2: el carnet d'un nombre
# (fracció, decimal, percentatge, quadrets); quina casella ve donada.
CARNET = [("a", 1, 2, "0,5", 50, None, True), ("b", 3, 4, "0,75", 75, "decimal", False),
          ("c", 1, 5, "0,2", 20, "percentatge", False), ("d", 1, 10, "0,1", 10, "quadrets", False)]
files_c = []
for l, n, d, dc, p, donat, r in CARNET:
    def cel(tipus, valor_ma, imprès):
        if r:
            return f'<td style="text-align:center">{valor_ma}</td>'
        if tipus == donat or (donat is None and tipus == "fracció"):
            return f'<td style="text-align:center;font-size:18pt;font-weight:800">{imprès}</td>'
        return '<td class="omplir" style="height:1.4cm"></td>'
    fila = (cel("fracció", fr(n, d, ma=True), fr(n, d, "16pt")) + cel("decimal", ms(dc), dc) +
            cel("percentatge", ms(f"{p} %"), f"{p} %") + cel("quadrets", ms(str(p)), str(p)))
    if r:
        fila = (f'<td style="text-align:center;font-size:18pt;font-weight:800">{fr(n, d, "16pt")}</td>' +
                cel("decimal", ms(dc), dc) + cel("percentatge", ms(f"{p} %"), "") + cel("quadrets", ms(str(p)), ""))
    files_c.append(f'''      <tr{' class="resolt"' if r else ''}><td class="apartat" style="text-align:center">{l})</td>{fila}</tr>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">El carnet d'un nombre. Omple les caselles buides. Mira la targeta.</div></div>
    <div class="clau" style="margin:.3rem 0 .6rem"><p style="margin:0">Cada fila és un sol nombre, escrit de quatre maneres.</p></div>
    <table class="mini">
      <tr><th style="width:1.2cm"></th><th>Fracció</th><th>Decimal</th><th>Percentatge</th><th>Quadrets de 100</th></tr>
{chr(10).join(files_c)}
    </table>
  </div>''')


# ===================================================================== pàgina 3: una de cada
def item(l, recorda, cos, r=False):
    return caixa(f'''      <p style="margin:0;font-size:14pt;color:var(--gris-2)"><span class="apartat" style="color:var(--tinta)">{l})</span> {recorda}</p>
      <div class="frase" style="margin:0;font-size:16pt">{cos}</div>''', r, ".3rem")


pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Una de cada. Fes-les amb el que ja saps.</div></div>
{item("a", "Els decimals. Com es llegeix?", "3,04: " + ms("tres unitats i quatre centèsimes"), True)}
{item("b", "Comparar. Quin és més gran?", tria(["0,6", "0,55"], None, mida="15pt", ample="2.4cm"))}
{item("c", "Arrodonir a les dècimes.", "4,67 arrodonit és " + buit_curt())}
{item("d", "Sumar amb la coma sota la coma.", "2,3 + 1,45 = " + buit())}
{item("e", "De la fracció al decimal.", fr(3, 4, "15pt") + " = " + buit_curt())}
{item("f", "L'arrel. Busca a la targeta.", "√49 = " + buit_curt())}
  </div>''')

# ===================================================================== pàgina 4: què he après?
FR = [("Escric un decimal a partir dels blocs.", "2 quadrats, 4 columnes i 3 quadrets: 2,43"),
      ("Comparo dos decimals amb dues xifres després de la coma.", "0,80 és més gran que 0,75"),
      ("Arrodoneixo a les dècimes amb la recta.", "3,47 arrodonit és 3,5"),
      ("Sumo i resto amb la coma sota la coma.", "2,50 + 1,35 = 3,85"),
      ("Passo una fracció a decimal amb el quadrat de 100.", f"{fr(1, 4, '13pt')} = 0,25"),
      ("Passo un decimal a fracció.", f"0,3 = {fr(3, 10, '13pt')}"),
      ("Trobo l'arrel d'un quadrat de la targeta.", "√49 = 7"),
      ("Dic entre quins dos nombres és una arrel.", "√20 és entre 4 i 5")]
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

# ===================================================================== pàgina 5: la vida (les rajoles)
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Quantes rajoles d'1 metre calen per fer el terra? Cada quadret és una rajola.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Si falta mig metre, cal una rajola sencera. Se'n retalla la meitat.</p></div>
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Una habitació de 5 m per 3,5 m.</p>
      <div style="width:7.2cm">{planol(5, 35, 0.95, "El plànol: 5 rajoles per fila, 3 files senceres i una fila de mitges rajoles").svg("")}</div>
      <p class="frase" style="margin:0">Files: {ms("4")}. Rajoles: 5 · 4 = {ms("20")}</p>""", True, ".4rem")}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Una habitació de 4 m per 2,5 m.</p>
      <div style="width:6.2cm">{planol(4, 25, 0.95, "El plànol: 4 rajoles per fila, 2 files senceres i una fila de mitges rajoles").svg("")}</div>
      <p class="frase" style="margin:0">Files: {buit_curt()}. Rajoles: 4 · {buit_curt()} = {buit_curt()}</p>""", False, ".4rem")}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">c)</span> Una habitació de 6 m per 4 m. No hi ha dibuix.</p>
      <p class="frase" style="margin:0">Rajoles: {buit_curt()} · {buit_curt()} = {buit_curt()}</p>""", False, ".4rem")}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append(f'''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 5 · Repàs de la unitat · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> És la fitxa de repàs: va després de les altres cinc de la unitat. El
    carnet d'un nombre fa el paper del mapa conceptual del grup: la fracció, el decimal, el
    percentatge i els quadrets de 100 són cares del mateix nombre. «Una de cada» torna a cada fitxa, i
    «Què he après?» és la llista de comprovació. Les rajoles són el projecte del grup, amb les mesures
    donades. La targeta «Decimals i arrels» és al davant tota l'estona.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb la quadrícula de 100: pintar-ne 25 quadrets i dir-ho de quatre maneres (un quart,
  0,25, el 25 % i 25 quadrets). És el carnet de la pàgina 1.</p>
  <h3>1. El carnet d'un nombre</h3>
  <table>
    <tr><th></th><th>Fracció</th><th>Decimal</th><th>Percentatge</th><th>Quadrets</th></tr>
    <tr><td>b)</td><td>{fr(3, 4)}</td><td>0,75</td><td>75 %</td><td>75</td></tr>
    <tr><td>c)</td><td>{fr(1, 5)}</td><td>0,2</td><td>20 %</td><td>20</td></tr>
    <tr><td>d)</td><td>{fr(1, 10)}</td><td>0,1</td><td>10 %</td><td>10</td></tr>
  </table>
  <p>Les cinc fraccions de la targeta són les mateixes que les dels percentatges de la unitat 4.</p>
  <h3>2. Una de cada</h3>
  <p>b) 0,6 (0,60 és més que 0,55). c) 4,7. d) 2,30 + 1,45 = 3,75. e) 0,75. f) 7. Cada apartat torna a
  una fitxa de la unitat: si un no surt, aquella fitxa és la que cal repassar.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>La pàgina 4: «Què he après?»</h3>
  <p>L'alumnat marca una casella a cada frase. L'adult tria dues frases de «Ho sé fer» i li demana
  que ho ensenyi amb un exemple. Les de «Encara no» diuen què s'ha de repassar, i on:</p>
  <table>
    <tr><th>Frase</th><th>On es repassa</th></tr>
    <tr><td>1 i 2 · llegir, escriure i comparar decimals</td><td>Fitxa 1; caixa 18</td></tr>
    <tr><td>3 · arrodonir</td><td>Fitxa 2; caixa 19</td></tr>
    <tr><td>4 · sumar i restar</td><td>Fitxa 3; caixa 20</td></tr>
    <tr><td>5 i 6 · fracció i decimal</td><td>Fitxa 4; caixa 21</td></tr>
    <tr><td>7 i 8 · l'arrel</td><td>Fitxa 5; caixa 2.3 i 2.4</td></tr>
  </table>
  <h3>3. Les rajoles</h3>
  <p>b) 3 files: 4 · 3 = 12 rajoles. c) 6 · 4 = 24 rajoles. Quan l'amplada acaba en mig metre, l'última
  fila també és de rajoles senceres, perquè es retallen: es compta cap amunt. És el projecte del grup
  (activitat 7), amb les mesures donades. <b>L'apartat c, sense dibuix, compta per als nivells alts.</b></p>
  <h3>La caixa d'eines</h3>
  <p>Per repassar, amb l'ordinador: les tasques 18 a 21, i la 2.3 i la 2.4. Les tasques tancades
  (18.2, 18.3, 19.2, 20.2, 21.2 i 2.4) donen un codi de verificació, i es poden fer abans de l'examen.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (5.1, 7.1 i 8.1) són de referència:
  l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Escriu un mateix nombre com a fracció, decimal, percentatge i quadrets de 100 (exercici 1).</li>
    <li>Fa un apartat de cada tipus de la unitat (exercici 2).</li>
    <li>Diu en veu alta què sap fer i què ha de repassar, i ho ensenya amb un exemple (pàgina 4).</li>
    <li>Calcula les rajoles d'un terra amb el plànol, i compta mitja rajola com una de sencera (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 5 · Repàs de la unitat", """  FITXA · Unitat 5 · Decimals i arrel quadrada · Repàs de la unitat
  La sisena fitxa de la unitat 5, i l'última abans de l'examen. Adapta les
  activitats 6 (el mapa conceptual: aquí, el carnet d'un nombre) i 7 (les rajoles,
  amb un plànol quadriculat i les mesures donades). «Una de cada» torna a cada
  fitxa de la unitat, i «Què he après?» és la llista de comprovació.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud5-repas.html")
