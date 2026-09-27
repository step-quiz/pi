#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud3-repas.html: el repàs de la unitat 3 (fitxa 5), amb el carnet de
cada fracció i «Què he après?» fet a partir de la llista de comprovació del grup."""
import os
import sys
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_ud2.py"), encoding="utf-8").read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_fraccions.py"), encoding="utf-8").read())
pagines = []
pagina = fes_pagina(pagines, "Unitat 3 · Repàs · pàgina")
FILES = ["El dibuix", "Es llegeix", "El tipus", "Una equivalent", "Més o menys que la meitat?"]


def carnet(n, d, valors=None):
    files = []
    for i, et in enumerate(FILES):
        if i == 0:
            cel = f'<td style="padding:.3rem .5rem">{tira(n, d, f"{n} de {d}", W=7.0, H=0.7, ma=bool(valors), buida=not valors).svg("")}</td>'
        elif valors:
            cel = f'<td class="esq" style="padding:.3rem .6rem">{valors[i]}</td>'
        else:
            cel = '<td class="omplir" style="height:1.2cm"></td>'
        cls = ' class="resolt"' if valors else ""
        files.append(f'<tr{cls}><th class="esq" style="width:4.6cm;text-align:left">{et}</th>{cel}</tr>')
    return (f'<table class="mini" style="margin:.2rem 0 .5rem"><tr><th colspan="2" style="font-size:17pt;text-align:left">'
            f'El carnet de {fr(n, d, "15pt")}</th></tr>' + "".join(files) + "</table>")


# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>les dues targetes i una tira de paper</b>. Doblegar-la en 4, pintar-ne 3, i tornar-la a doblegar: 6 trossos pintats de 8.</div>
  <h1>Repàs de la unitat</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div style="width:10cm;margin:.6rem auto 0">
{tira(3, 4, "3 de 4", W=9.5, H=0.8).svg()}
{tira(6, 8, "6 de 8", W=9.5, H=0.8).svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .5rem">Hi ha dos rectangles iguals, amb el mateix tros pintat.</p>
  {carnet(3, 4, [None, ms("tres quarts"), ms("pròpia"), fr(6, 8, ma=True), ms("més")])}
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">El carnet d'una fracció diu tot el que en saps.</p>
  </div>''')

# ===================================================================== pàgina 2: carnets
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Fes el carnet de cada fracció. Mira les dues targetes.</div></div>
    <p style="margin:.3rem 0 0;font-weight:700"><span class="apartat">a)</span></p>
    {carnet(2, 5)}
    <p style="margin:.3rem 0 0;font-weight:700"><span class="apartat">b)</span></p>
    {carnet(5, 4)}
  </div>''')

# ===================================================================== pàgina 3: una de cada
def item(l, recorda, cos, r=False):
    return caixa(f'''      <p style="margin:0;font-size:14pt;color:var(--gris-2)"><span class="apartat" style="color:var(--tinta)">{l})</span> {recorda}</p>
      <div class="frase" style="margin:0;font-size:16pt">{cos}</div>''', r, ".3rem")


pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Una de cada. Fes-les amb el que ja saps.</div></div>
{item("a", "El nom, amb la targeta.", fr(5, 8) + " es llegeix " + ms("cinc vuitens"), True)}
{item("b", "Pinta la fracció.", fr(2, 3) + '<div style="width:7.2cm;display:inline-block;vertical-align:middle;margin-left:.4cm">' + tira(0, 3, "3 trossos per pintar", W=7.0, H=0.7, buida=True).svg("") + "</div>")}
{item("c", "Mira el de dalt i el de baix.", fr(7, 7) + " és una fracció " + '<u style="display:inline-block;min-width:4cm;padding:0"></u>')}
{item("d", "Amb el mateix numerador, els trossos més petits són els del nombre gran.", "La més gran: " + fr(1, 4) + " o " + fr(1, 6) + "? " + fr_buit("13pt"))}
{item("e", "Parteix cada tros en 2.", fr(1, 3) + " = " + fr_buit("13pt"))}
{item("f", "El de baix no canvia.", fr(2, 7) + " + " + fr(3, 7) + " = " + fr_buit("13pt"))}
  </div>''')

# ===================================================================== pàgina 4: què he après?
FR = [("Sé què diuen el de dalt i el de baix.", f"{fr(3, 4, '13pt')}: 3 trossos pintats de 4"),
      ("Pinto una fracció en un rectangle.", "Trossos iguals"),
      ("Dic el nom d'una fracció amb la targeta.", f"{fr(4, 9, '13pt')}: quatre novens"),
      ("Sé si és nul·la, pròpia, unitat o impròpia.", f"{fr(5, 4, '13pt')}: impròpia"),
      ("Comparo fraccions amb el mateix de baix.", f"{fr(3, 5, '13pt')} és més gran que {fr(2, 5, '13pt')}"),
      ("Comparo fraccions amb el mateix de dalt.", f"{fr(1, 3, '13pt')} és més gran que {fr(1, 5, '13pt')}"),
      ("Trobo una fracció equivalent pintant.", f"{fr(1, 2, '13pt')} = {fr(2, 4, '13pt')}"),
      ("Amplifico: multiplico dalt i baix.", f"{fr(2, 3, '13pt')} = {fr(8, 12, '13pt')}"),
      ("Sumo i resto amb el mateix de baix.", f"{fr(3, 8, '13pt')} + {fr(2, 8, '13pt')} = {fr(5, 8, '13pt')}"),
      ("Sé per què no se sumen els de baix.", "La pàgina 5 de la fitxa de sumes")]
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

# ===================================================================== pàgina 5: la vida
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">A la cuina. Mira les dues targetes.</div></div>
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> La recepta diu {fr(1, 2, "14pt")} litre de llet i {fr(1, 4, "14pt")} de litre d'aigua. De què n'hi ha més?</p>
      <p class="frase" style="margin:0">{ms("De llet")}: {fr(1, 2, ma=True)} és més gran que {fr(1, 4, ma=True)}.</p>""", True)}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Queden {fr(3, 4, "14pt")} del pastís. En menges {fr(1, 4, "14pt")}. Quant en queda?</p>
      <p class="frase" style="margin:0">{fr(3, 4)} − {fr(1, 4)} = {fr_buit("13pt")}</p>""")}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">c)</span> Mig quilo de farina i {fr(2, 4, "14pt")} de quilo, pesen el mateix?</p>
      {tria(["Sí", "No"], mida="14pt", ample="2.5cm")}""")}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 3 · Repàs de la unitat · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> És la fitxa de repàs: va després de les altres quatre de la unitat. El
    carnet de cada fracció recull tot el que es treballa a la unitat, i «Què he après?» és la llista
    de comprovació del grup, en frases que diuen què es fa. Les dues targetes són al davant tota
    l'estona.
  </div>
  <h3>1. Els carnets</h3>
  <table>
    <tr><th></th><th>2/5</th><th>5/4</th></tr>
    <tr><td>El dibuix</td><td>2 trossos pintats de 5</td><td>Un rectangle sencer i 1 tros més, de 4</td></tr>
    <tr><td>Es llegeix</td><td>dos cinquens</td><td>cinc quarts</td></tr>
    <tr><td>El tipus</td><td>pròpia</td><td>impròpia</td></tr>
    <tr><td>Una equivalent</td><td>4/10, per exemple</td><td>10/8, per exemple</td></tr>
    <tr><td>Més o menys que la meitat?</td><td>menys</td><td>més: és més d'un rectangle</td></tr>
  </table>
  <p>Es dona per bona qualsevol equivalent ben amplificada.</p>
  <h3>2. Una de cada</h3>
  <p>b) 2 trossos pintats de 3; c) unitat; d) 1/4; e) 2/6; f) 5/7. Cada apartat torna a una fitxa de
  la unitat: si un no surt, aquella fitxa és la que cal repassar (vegeu la taula del full següent).</p>
  <h3>3. A la vida de cada dia</h3>
  <p>b) 3/4 − 1/4 = 2/4. c) Sí: mig quilo és 1/2, i 1/2 = 2/4.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>La pàgina 4: «Què he après?»</h3>
  <p>L'alumnat marca una casella a cada frase. L'adult tria dues frases de «Ho sé fer» i li demana
  que ho ensenyi amb un exemple. Les de «Encara no» diuen què s'ha de repassar, i on:</p>
  <table>
    <tr><th>Frase</th><th>On es repassa</th></tr>
    <tr><td>1, 2 i 3 · el de dalt i el de baix, pintar, el nom</td><td>Fitxa 1; caixa 9.1 i 9.2</td></tr>
    <tr><td>4, 5 i 6 · els tipus i comparar</td><td>Fitxa 2; caixa 9.1, 11.1 i 11.2</td></tr>
    <tr><td>7 i 8 · equivalents i amplificar</td><td>Fitxa 3; caixa 10.1 i 10.2</td></tr>
    <tr><td>9 i 10 · sumar i restar</td><td>Fitxa 4; caixa 12.1 i 12.2</td></tr>
  </table>
  <h3>La caixa d'eines</h3>
  <p>Per repassar, amb l'ordinador: les tasques de la 9 a la 12. Les quatre tasques tancades (9.2,
  10.2, 11.2 i 12.2) donen un codi de verificació, i es poden fer abans de l'examen.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb les dues targetes al davant. Els criteris de la SA del grup (1.2, 5.2, 6.1 i 9.1) són
  de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Fa el carnet d'una fracció, fila a fila (exercici 1).</li>
    <li>Fa un apartat de cada tipus de la unitat (exercici 2).</li>
    <li>Diu en veu alta què sap fer i què ha de repassar, i ho ensenya amb un exemple (pàgina 4).</li>
    <li>Nivells alts: fa servir les fraccions en una situació de debò, a la cuina (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 3 · Repàs de la unitat", """  FITXA · Unitat 3 · Les fraccions · Repàs de la unitat
  La cinquena fitxa de la unitat 3, i l'última abans de l'examen. Adapta el
  repàs del grup, amb el carnet de cada fracció (el dibuix, el nom, el tipus,
  una equivalent i si és més o menys que la meitat), i «Què he après?», fet a
  partir de la llista de comprovació del grup.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud3-repas.html")
