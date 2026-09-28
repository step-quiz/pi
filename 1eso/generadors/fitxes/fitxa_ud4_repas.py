#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud4-repas.html: el repàs de la unitat 4 (fitxa 5), amb
«Una de cada» (un apartat per cada fitxa de la unitat) i «Què he après?»."""
import os
import sys
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_ud2.py"), encoding="utf-8").read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_fraccions.py"), encoding="utf-8").read())
pagines = []
pagina = fes_pagina(pagines, "Unitat 4 · Repàs · pàgina")

# Les mateixes peces de dibuix que a les altres quatre fitxes de la unitat (fitxa
# per fitxa, com demana el README dels generadors: cada fitxa es refà des del
# seu propi generador, sense dependre que una altra fitxa no canviï d'estil).


def grups(nombre, n, d, m=None, ma=False, buida=False):
    """`nombre` quadrets repartits en `d` files iguals; les primeres `n`, pintades."""
    gran = nombre // d
    esq = 1.9
    if m is None:
        m = min(0.85, (3.4 + 0.16) / d - 0.16, (6.2 - esq - 0.1) / gran)
    D = Dibuix(esq + gran * m + 0.1, d * (m + 0.16) - 0.16 + 0.2, f"{nombre} quadrets repartits en {d} grups de {gran}")
    for fi in range(d):
        y = 0.1 + fi * (m + 0.16)
        for co in range(gran):
            if buida:
                fons, traç, gruix = "#fff", G2, 1.2
            elif fi < n:
                fons, traç, gruix = (VORA_SUAU, MS, 1.8) if ma else (F3, G1, 1.6)
            else:
                fons, traç, gruix = "#fff", G2, 1.2
            D.quadret(esq + co * m, y, m, fons=fons, traç=traç, gruix=gruix)
    D.clau_esq(esq - 0.15, 0.1, 0.1 + d * (m + 0.16) - 0.16, quants_(d, "grup", "grups"))
    return D


def quants_(n, s, p):
    return f"{n} {s if n == 1 else p}"


def tros_de_tros(d1, d2, m=None):
    """El rectangle de dues fraccions: d1 columnes per d2 files."""
    esq, dalt, marge_dr, marge_ba = 1.75, 0.7, 0.15, 0.15
    if m is None:
        m = min(0.85, (3.4 - dalt - marge_ba) / d2, (6.4 - esq - marge_dr) / d1)
    D = Dibuix(esq + d1 * m + marge_dr, dalt + d2 * m + marge_ba, f"Un tros de {d1} de {d2}: el resultat és 1 de {d1 * d2}")
    for fi in range(d2):
        for co in range(d1):
            columna, fila = co == 0, fi == 0
            if columna and fila:
                fons, traç, gruix = F4, G1, 1.6
            elif columna:
                fons, traç, gruix = F3, G1, 1.6
            elif fila:
                fons, traç, gruix = F4, G1, 1.6
            else:
                fons, traç, gruix = "#fff", G2, 1.2
            D.quadret(esq + co * m, dalt + fi * m, m, fons=fons, traç=traç, gruix=gruix)
    D.cru(f'<rect x="{D.px(esq + 0.05)}" y="{D.px(dalt + 0.05)}" width="{D.px(m - 0.1)}" height="{D.px(m - 0.1)}" '
          f'rx="{D.px(0.08)}" fill="none" stroke="{MS}" stroke-width="2.6"/>')
    D.clau_dalt(esq, esq + d1 * m, dalt, f"1 de {d1}")
    D.clau_esq(esq, dalt, dalt + d2 * m, f"1 de {d2}")
    return D


def percentatge(p, m=0.5):
    return graella100(lambda n: "imprès" if n <= p else None, f"{p} quadrets pintats de 100", m=m)


def dobles(n, k, m=None):
    gran = n * k
    if m is None:
        m = min(0.6, 6.2 / gran)
    aire = 0.16
    D = Dibuix(gran * m + 0.2, 2 * m + aire + 0.2, f"Una fila de {n} quadrets, i una altra de {gran}")
    D.rectangle(0.1, 0.1, 1, n, m, fons=F3)
    D.rectangle(0.1, 0.1 + m + aire, 1, gran, m, fons=F4)
    for i in range(1, k):
        x = 0.1 + i * n * m
        D.cru(f'<line x1="{D.px(x)}" y1="{D.px(0.1 + m + aire + 0.06)}" x2="{D.px(x)}" '
              f'y2="{D.px(0.1 + 2 * m + aire - 0.06)}" stroke="{G1}" stroke-width="1.6" stroke-dasharray="4 3"/>')
    return D


# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs i la graella de 100</b>. Repartir 15 en 3 grups, i pintar 25 quadrets de la graella.</div>
  <h1>Repàs de la unitat</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div style="display:flex;gap:.8cm;justify-content:center;align-items:flex-end;margin-top:.6rem;flex-wrap:wrap">
    <div style="width:4.8cm">{grups(12, 1, 3, m=0.7).svg("")}</div>
    <div style="width:3.4cm">{percentatge(25, m=0.32).svg("")}</div>
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.5rem 0 .5rem">Repartir en grups, i pintar quadrets de 100. Són dues maneres de fer servir la quadrícula.</p>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Tota la unitat fa servir la mateixa quadrícula.</p>
    <p style="margin:.2rem 0 0">Repartir, fer un tros de tros, pintar percentatges, i comparar files.</p>
  </div>''')

# ===================================================================== pàgina 2: una de cada
def item(l, recorda, cos, r=False):
    return caixa(f'''      <p style="margin:0;font-size:14pt;color:var(--gris-2)"><span class="apartat" style="color:var(--tinta)">{l})</span> {recorda}</p>
      <div class="frase" style="margin:0;font-size:16pt">{cos}</div>''', r, ".3rem")


pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Una de cada. Fes-les amb el que ja saps.</div></div>
{item("a", "Fracció d'un nombre. Reparteix i pinta.", fr(1, 3, "15pt") + " de 15: " + ms("5") + '<div style="width:6.2cm;display:inline-block;vertical-align:middle;margin-left:.4cm">' + grups(15, 1, 3, ma=True).svg("") + "</div>", True)}
{item("b", "Multiplicar fraccions. Fes el tros de tros.", fr(1, 2, "15pt") + " de " + fr(1, 3, "15pt") + '<div style="width:4.6cm;display:inline-block;vertical-align:middle;margin-left:.4cm">' + tros_de_tros(2, 3).svg("") + "</div>")}
{item("c", "Percentatges. Pinta els quadrets.", "Pinta el 50%" + '<div style="width:4.6cm;display:inline-block;vertical-align:middle;margin-left:.4cm">' + percentatge(0, m=0.32).svg("") + "</div>")}
{item("d", "Dobles i triples. Fes el triple.", "Fila de 4" + '<div style="width:4.6cm;display:inline-block;vertical-align:middle;margin-left:.4cm">' + dobles(4, 3, m=0.45).svg("") + "</div>")}
  </div>''')

# ===================================================================== pàgina 3: què he après?
FR = [("Reparteixo un nombre en grups iguals.", f"{fr(1, 3, '13pt')} de 12: 4"),
      ("Pinto els grups que em diu la fracció.", f"{fr(2, 3, '13pt')} de 12: 8"),
      ("Faig un tros de tros amb dues fraccions.", f"{fr(1, 2, '13pt')} de {fr(1, 4, '13pt')} és {fr(1, 8, '13pt')}"),
      ("Multiplico els dos denominadors.", "2 · 4 = 8"),
      ("Pinto un percentatge a la graella de 100.", "25% = 25 quadrets"),
      ("Compto quants quadrets és un percentatge.", "50 quadrets = 50%"),
      ("Faig el doble o el triple d'una fila.", "El doble de 3 és 6"),
      ("Sé que una mida petita pot ser gran en relatiu.", "L'ou del kiwi")]
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

# ===================================================================== pàgina 4: la vida
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Mira la targeta de les taules i de les fraccions.</div></div>
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Una capsa de 20 llapis. Un quart són vermells. Quants llapis vermells hi ha?</p>
      <p class="frase" style="margin:0">{fr(1, 4, ma=True)} de 20: {ms("5")}</p>""", True)}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> En una botiga, el 10% dels productes són rebaixats. De 100 productes, quants són rebaixats?</p>
      <p class="frase" style="margin:0">{buit_curt()} productes</p>""")}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">c)</span> Una planta fa 5 cm. Al cap d'un mes en fa el triple. Quant mesura ara?</p>
      <p class="frase" style="margin:0">5 · 3 = {buit_curt()} cm</p>""")}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 4 · Repàs de la unitat · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> És la fitxa de repàs: va després de les altres quatre de la unitat. Fa
    un apartat de cada tipus (fracció d'un nombre, multiplicar fraccions, percentatges, dobles i
    triples), i «Què he après?» és la llista de comprovació de la situació d'aprenentatge, en frases
    que diuen què es fa. Les dues targetes són al davant tota l'estona.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs i la graella de 100: repartir 15 en 3 grups, i pintar 25 quadrets de
  la graella. Tota la unitat fa servir la mateixa quadrícula, de maneres diferents.</p>
  <h3>1. Una de cada</h3>
  <p>b) 1/2 de 1/3 és 1/6: 2 · 3 = 6. c) 50 quadrets pintats de 100. d) El triple de 4 és 12. Cada
  apartat torna a una fitxa de la unitat: si un no surt, aquella fitxa és la que cal repassar
  (vegeu la taula del full següent).</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>La pàgina 3: «Què he après?»</h3>
  <p>L'alumnat marca una casella a cada frase. L'adult tria dues frases de «Ho sé fer» i li demana
  que ho ensenyi amb un exemple. Les de «Encara no» diuen què s'ha de repassar, i on:</p>
  <table>
    <tr><th>Frase</th><th>On es repassa</th></tr>
    <tr><td>1 i 2 · repartir i pintar grups</td><td>Fitxa 1; caixa 14.1 i 14.2</td></tr>
    <tr><td>3 i 4 · el tros de tros</td><td>Fitxa 2; caixa 15.1 i 15.2</td></tr>
    <tr><td>5 i 6 · els percentatges</td><td>Fitxa 3; caixa 16.1 i 16.2</td></tr>
    <tr><td>7 i 8 · dobles, triples i mides relatives</td><td>Fitxa 4; caixa 17.1 i 17.2</td></tr>
  </table>
  <h3>2. A la vida de cada dia</h3>
  <p>b) 10 productes. c) 15 cm.</p>
  <h3>La caixa d'eines</h3>
  <p>Per repassar, amb l'ordinador: les tasques de la 14 a la 17. Les quatre tasques tancades (14.2,
  15.2, 16.2 i 17.2) donen un codi de verificació, i es poden fer abans de l'examen.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb les dues targetes al davant. Els criteris de la SA del grup (1.3, 2.1, 5.1 i 6.1) són
  de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Fa un apartat de cada tipus de la unitat (exercici 1).</li>
    <li>Diu en veu alta què sap fer i què ha de repassar, i ho ensenya amb un exemple (pàgina 3).</li>
    <li>Nivells alts: fa servir el que ha après en una situació de debò (exercici 2).</li>
  </ul>
</div>''')

document("Unitat 4 · Repàs de la unitat", """  FITXA · Unitat 4 · És gran l'ou del kiwi? · Repàs de la unitat
  La cinquena fitxa de la unitat 4, i l'última abans de l'examen. Fa un
  apartat de cada tipus (fracció d'un nombre, multiplicar fraccions,
  percentatges, dobles i triples), i «Què he après?», amb la llista de
  comprovació de la situació d'aprenentatge.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud4-repas.html")
