#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud4.html: la fracció d'un nombre (unitat 4, fitxa 1).
Adapta l'activitat 3 (Fracció d'un nombre) de la situació «És gran l'ou del kiwi?»."""
import os
import sys
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_ud2.py"), encoding="utf-8").read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_fraccions.py"), encoding="utf-8").read())
pagines = []
pagina = fes_pagina(pagines, "Unitat 4 · Fracció d'un nombre · pàgina")


def grups(nombre, n, d, m=None, ma=False, buida=False):
    """`nombre` quadrets repartits en `d` files iguals; les primeres `n`, pintades.
    Amb `ma`, la vora del pintat resseguida a mà; amb `buida`, totes blanques.
    Sense `m`, la mida del quadret s'ajusta perquè el dibuix no passi de 3.4 cm
    d'alt ni de 6.2 cm d'ample (per cabre en una columna de la graella). El
    marge esquerre (1.9 cm) deixa lloc al text de la clau, com «6 grups»."""
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
    D.clau_esq(esq - 0.15, 0.1, 0.1 + d * (m + 0.16) - 0.16, quants(d, "grup", "grups"))
    return D


def quants(n, s, p):
    return f"{n} {s if n == 1 else p}"


# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>12 miniblocs</b>. Repartir-los en 3 grups iguals i comptar-ne un grup.</div>
  <h1>La fracció d'un nombre</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:1rem;width:7cm;margin-left:auto;margin-right:auto">
{grups(12, 1, 3, m=0.95).svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.5rem 0 .8rem">Són 12 quadrets, repartits en 3 grups iguals. N'hi ha 1 grup pintat.</p>
  <table>
    <tr class="resolt"><td class="esq">Quants quadrets té cada grup?</td><td style="width:4.4cm">{ms("4")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets hi ha pintats?</td><td>{ms("4")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">Repartir 12 en 3 grups iguals: cada grup té 4.</p>
    <p style="margin:.2rem 0">{fr(1, 3, "34pt")} de 12 <b>és</b> 4</p>
    <p style="margin:0;font-weight:700">Pintar 1 grup de 3 és la fracció {fr(1, 3, "17pt")}.</p>
  </div>''')

# ===================================================================== pàgina 2: repartir i pintar 1 grup
E1 = [("a", 1, 3, 12, True), ("b", 1, 4, 16, False), ("c", 1, 2, 14, False), ("d", 1, 5, 20, False)]
it = []
for l, n, d, t, r in E1:
    grup = t // d
    cos = grups(t, n, d, ma=r, buida=not r)
    resultat = ms(str(grup)) if r else buit_curt()
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span> {fr(n, d, "15pt")} de {t}. Reparteix en {d} grups i pinta'n 1.</p>
      <div style="width:{cos.amp:.1f}cm">{cos.svg("")}</div>
      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">Cada grup té {resultat} quadrets.</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Reparteix en grups iguals. Pinta'n 1 grup. Escriu quants quadrets té.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Divideix el nombre entre els grups. 12 entre 3 és 4.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 3: pintar-ne més d'un grup
E2 = [("a", 2, 3, 12, True), ("b", 3, 4, 16, False), ("c", 2, 5, 20, False), ("d", 3, 5, 25, False)]
it = []
for l, n, d, t, r in E2:
    grup = t // d
    resultat = n * grup
    cos = grups(t, n, d, ma=r, buida=not r)
    frase = ms(f"{n} · {grup} = {resultat}") if r else f"{buit_curt()} · {buit_curt()} = {buit_curt()}"
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span> {fr(n, d, "15pt")} de {t}. Pinta {n} grups.</p>
      <div style="width:{cos.amp:.1f}cm">{cos.svg("")}</div>
      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">{frase}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Reparteix en grups iguals. Pinta els grups que et diu la fracció. Multiplica per saber quants quadrets són.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Primer reparteix. Després multiplica els grups pintats pels quadrets de cada grup.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
E3 = [("a", 12, [5, 3, 4], 1, True), ("b", 15, [5, 5, 5], 1, False), ("c", 18, [6, 4, 8], 0, False)]
it = []
for l, t, gs, bo, r in E3:
    aria = f"{t} quadrets repartits en grups desiguals"
    m = 0.7
    D = Dibuix(max(gs) * m + 0.2, len(gs) * (m + 0.16) - 0.16 + 0.2, aria)
    for fi, g in enumerate(gs):
        y = 0.1 + fi * (m + 0.16)
        for co in range(g):
            fons, traç, gruix = (F3, G1, 1.6) if fi == bo else ("#fff", G2, 1.2)
            D.quadret(0.1 + co * m, y, m, fons=fons, traç=traç, gruix=gruix)
    bona = "No" if r else None
    it.append(caixa(f'''      <p style="margin:0;font-size:16pt;font-weight:700"><span class="apartat">{l})</span> Són grups iguals?</p>
      <div style="width:{max(gs) * m + 0.6:.1f}cm">{D.svg("")}</div>
      {tria(["Sí", "No"], bona, mida="14pt", ample="2.5cm")}''', r, ".2rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Són grups iguals? Marca la resposta.</div></div>
    <div class="clau" style="margin:.3rem 0 .6rem"><p style="margin:0">Compta els quadrets de cada grup. Han de ser tots iguals.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:.3rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Per fer una fracció d'un nombre, els grups han de ser iguals.</p>
    <p style="margin:.2rem 0 0">Si els grups no són iguals, no es pot dir quin tros és cada un.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
V = [("a", "Una capsa de 20 llapis. En un terç hi ha llapis vermells.", 1, 4, 20, True),
     ("b", "24 alumnes a la classe. Una sisena part porta ulleres.", 1, 6, 24, False),
     ("c", "30 cromos. En repartim tres cinquenes parts a un amic.", 3, 5, 30, False)]
it = []
for l, t_, n, d, t, r in V:
    grup = t // d
    resultat = n * grup
    frase = ms(f"{n} · {grup} = {resultat}") if r else f"{buit_curt()} · {buit_curt()} = {buit_curt()}"
    it.append(caixa(f'''      <p style="margin:0 0 .2rem"><span class="apartat">{l})</span> {t_}</p>
      <p class="frase" style="margin:0">{fr(n, d)} de {t}: {frase}</p>''', r, ".3rem"))
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Calcula la fracció d'un nombre. Mira la targeta.</div></div>
{chr(10).join(it)}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 4 · La fracció d'un nombre · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> La fracció d'un nombre és repartir-lo en grups iguals: el denominador diu
    en quants grups, i el numerador, quants grups es pinten. 1/3 de 12 és repartir 12 en 3 grups de 4, i
    pintar-ne 1. La caixa d'eines ho fa a la tasca 14.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb 12 miniblocs: repartir-los en 3 grups iguals de 4, i comptar-ne un grup. És
  l'exemple de la pàgina 1.</p>
  <h3>1. Reparteix i pinta 1 grup</h3>
  <p>b) 4; c) 7; d) 4. Sempre amb divisió exacta, i el resultat és de la targeta de les taules.</p>
  <h3>2. Pinta més d'un grup</h3>
  <p>b) 3 · 4 = 12; c) 2 · 4 = 8; d) 3 · 5 = 15. Primer es reparteix (divisió), després es
  multiplica el resultat pels grups que es pinten.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>3. Grups iguals</h3>
  <p>b) Sí; c) No. <b>Error típic:</b> dir que sí encara que els grups tinguin nombres diferents de
  quadrets. És la regla trencada d'aquesta fitxa. No l'expliqueu: que compti els quadrets de cada
  grup, un per un, i vegi que no coincideixen.</p>
  <h3>4. A la vida de cada dia</h3>
  <p>b) 6 · 4 = 24; c) 5 · 6 = 30, i 6 · 3 = 18.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=14</b> (14.1 Reparteix i
  pinta; 14.2 Quant és?). La 14.2 dona un codi de verificació; les respostes falses són les dues
  confusions: dir el nombre d'un grup en lloc del resultat, i una altra confusió propera.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta de les taules al davant. Els criteris de la SA del grup (1.3, 2.1, 5.1 i
  6.1) són de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb miniblocs, reparteix un nombre en grups iguals.</li>
    <li>Pinta 1 grup i diu quants quadrets té (exercici 1).</li>
    <li>Pinta més d'un grup i calcula el resultat amb una multiplicació (exercici 2).</li>
    <li>Nivells alts: diu per què els grups han de ser iguals (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 4 · La fracció d'un nombre", """  FITXA · Unitat 4 · És gran l'ou del kiwi? · La fracció d'un nombre
  La primera fitxa de la unitat 4. Adapta l'activitat 3 de la situació:
  una fracció d'un nombre és repartir-lo en grups iguals i pintar-ne els que
  calen. Els casos són els de la tasca 14 de la caixa (regla 8).

  La regla trencada és repartir en grups desiguals (exercici 3).""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud4.html")
