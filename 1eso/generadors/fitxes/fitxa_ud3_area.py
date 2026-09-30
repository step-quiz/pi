#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud3-area.html: mesurar l'àrea (unitat 3, la primera fitxa en ordre).
Adapta les activitats 2, 3, 4 i 5 de la situació «Com és de gran Gaza?»: què és més gran,
el metre i el quilòmetre (amb l'excepció «1 km = 1.000 m», decisió del docent del 26/9/2026),
l'àrea de rectangles i de figures irregulars amb quadrets sencers i mitjos."""
import os
import sys
from peces_comunes import *  # noqa: F401,F403
from peces_ud2 import *  # noqa: F401,F403
from peces_fraccions import *  # noqa: F401,F403
pagines = []
pagina = fes_pagina(pagines, "Unitat 3 · Àrea · pàgina")

# Les figures de la tasca 13 de la caixa (regla 8)
FIG = {"casa": [".◢##◣.", ".####.", ".####.", ".####."], "fletxa": ["..◢◣..", ".◢##◣.", "######", "..##.."],
       "rombe": [".◢◣.", "◢##◣", "◥##◤", ".◥◤."], "teulada": ["◢###◣", "#####", "#####"]}


def figura(files, m, aria):
    rows, cols = len(files), max(len(r) for r in files)
    D = Dibuix((cols + 2) * m + 0.1, (rows + 2) * m + 0.1, aria)
    for fi in range(rows + 2):
        for co in range(cols + 2):
            D.cru(f'<rect x="{D.px(0.05 + co * m)}" y="{D.px(0.05 + fi * m)}" width="{D.px(m)}" height="{D.px(m)}" fill="#fff" stroke="{G3}" stroke-width="0.8"/>')
    for fi, r in enumerate(files):
        for co, c in enumerate(r):
            x, y = 0.05 + (co + 1) * m, 0.05 + (fi + 1) * m
            if c == "#":
                D.cru(f'<rect x="{D.px(x)}" y="{D.px(y)}" width="{D.px(m)}" height="{D.px(m)}" fill="{F3}" stroke="{G1}" stroke-width="1.6"/>')
            tri = {"◢": [(x + m, y), (x + m, y + m), (x, y + m)], "◣": [(x, y), (x, y + m), (x + m, y + m)],
                   "◤": [(x, y), (x + m, y), (x, y + m)], "◥": [(x, y), (x + m, y), (x + m, y + m)]}.get(c)
            if tri:
                D.cru(f'<polygon points="{" ".join(f"{D.px(a)},{D.px(b)}" for a, b in tri)}" fill="{F3}" stroke="{G1}" stroke-width="1.6"/>')
    return D


def compta(files):
    s = sum(r.count("#") for r in files); m = sum(sum(r.count(c) for c in "◢◣◤◥") for r in files)
    return s, m, s + m // 2


def rect(files_, cols, m, aria):
    return figura(["#" * cols] * files_, m, aria)


# ===================================================================== pàgina 1
L = ["####.", "####.", "#####"]
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>paper quadriculat</b>. Retallar dues figures, posar-les una damunt de l'altra i comptar-ne els quadrets.</div>
  <h1>Mesurar l'àrea</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div style="display:flex;gap:1.4cm;justify-content:center;align-items:flex-end;margin-top:.6rem">
    <div style="width:5.2cm">{rect(3, 4, 0.8, "Un rectangle de 3 files de 4 quadrets").svg("")}</div>
    <div style="width:6cm">{figura(L, 0.8, "Una figura de 13 quadrets, amb forma de ela").svg("")}</div>
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .6rem">Són dues figures fetes de quadrets. Quina ocupa més?</p>
  <table>
    <tr class="resolt"><td class="esq">Quants quadrets té el rectangle?</td><td style="width:4.6cm">{ms("12")}</td></tr>
    <tr class="resolt"><td class="esq">I l'altra figura?</td><td>{ms("13")}</td></tr>
    <tr class="resolt"><td class="esq">Quina ocupa més?</td><td>{ms("L'altra")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-size:20pt;font-weight:800">L'àrea és quants quadrets ocupa una figura.</p>
    <p style="margin:.2rem 0 0">Per saber quina és més gran, compta'n els quadrets.</p>
  </div>''')

# ===================================================================== pàgina 2: el metre i el quilòmetre
def items(nums, opcions, llista):
    out = []
    for l, text, bona, r in llista:
        out.append(caixa(f'''      <p style="margin:0;font-size:15pt"><span class="apartat">{l})</span> {text}</p>
      {tria(opcions, bona if r else None, mida="14pt", ample="2.4cm")}''', r, ".2rem"))
    return "\n".join(out)


pagina(f'''  <div class="avis gruixut">
    <p style="margin:0">Un quilòmetre són mil metres: 1 km = 1.000 m.</p>
    <p style="margin:0">Un quadrat d'1 m de costat és <b>1 m²</b>. Un quadrat d'1 km de costat és <b>1 km²</b>.</p>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Quina unitat faries servir? Marca la resposta.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{items(1, ["m", "km"], [("a", "La llargada de la classe", "m", True), ("b", "De casa teva a Barcelona", "km", False),
                        ("c", "La llargada del pati", "m", False), ("d", "La llargada d'un riu", "km", False)])}
    </div>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">I l'àrea? Marca la resposta.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{items(2, ["m²", "km²"], [("a", "El terra de l'aula", "m²", True), ("b", "Una ciutat", "km²", False),
                          ("c", "Una pissarra", "m²", False), ("d", "Un país", "km²", False)])}
    </div>
  </div>''')

# ===================================================================== pàgina 3: el rectangle
R = [("a", 3, 4, True), ("b", 5, 6, False), ("c", 4, 7, False), ("d", 8, 9, False)]
it = []
for l, f_, c_, r in R:
    res = ms(f"{f_} · {c_} = {f_ * c_}") if r else f"{buit_curt()} · {buit_curt()} = {buit_curt()}"
    it.append(caixa(f'''      <p style="margin:0 0 .1rem;font-weight:700"><span class="apartat">{l})</span> {f_} files de {c_} quadrets</p>
      <div style="width:{min(7.6, (c_ + 2) * 0.55 + 0.1):.1f}cm">{rect(f_, c_, 0.55, f"Un rectangle de {f_} files de {c_} quadrets").svg("")}</div>
      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">Àrea: {res} quadrets</p>''', r, ".25rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Calcula l'àrea de cada rectangle. Mira la targeta de les taules.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Multiplica les files pels quadrets de cada fila. 3 files de 4 són 3 · 4 = 12.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 4: sencers i mitjos · la regla trencada
F4 = [("a", "casa", True), ("b", "fletxa", False), ("c", "rombe", False), ("d", "teulada", False)]
it = []
for l, nom_, r in F4:
    s_, m_, a_ = compta(FIG[nom_])
    cel = (f'{ms(str(s_))} sencers · {ms(str(m_))} mitjos · els mitjos fan {ms(str(m_ // 2))} · àrea: {ms(str(a_))}' if r else
           f'{buit_curt()} sencers · {buit_curt()} mitjos · els mitjos fan {buit_curt()} · àrea: {buit_curt()}')
    it.append(caixa(f'''      <div style="display:flex;gap:.5cm;align-items:center">
        <p style="margin:0;font-weight:700"><span class="apartat">{l})</span></p>
        <div style="width:{(len(FIG[nom_][0]) + 2) * 0.7 + 0.1:.1f}cm">{figura(FIG[nom_], 0.7, f"Una figura de quadrets sencers i mitjos").svg("")}</div>
        <p class="frase" style="margin:0;font-size:14.5pt;line-height:2">{cel}</p>
      </div>''', r, ".25rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Compta els quadrets sencers i els mitjos. Després escriu l'àrea.</div></div>
{chr(10).join(it)}
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Un mig no és un quadret sencer. Dos mitjos fan un quadret:</p>
    <p style="margin:.2rem 0 0">{fr(1, 2, "15pt")} + {fr(1, 2, "15pt")} = 1</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
V = [("a", "Una habitació de 3 m per 4 m.", 3, 4, True), ("b", "L'aula: 8 m per 9 m.", 8, 9, False), ("c", "Un balcó de 2 m per 5 m.", 2, 5, False)]
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Quants m² fa el terra? Cada quadret és 1 m².</div></div>
{chr(10).join(caixa(f"""      <p style="margin:0 0 .15rem"><span class="apartat">{l})</span> {t}</p>
      <div style="width:{(c_ + 2) * 0.5 + 0.1:.1f}cm">{rect(f_, c_, 0.5, t).svg("")}</div>
      <p class="frase" style="margin:.1rem 0 0">{ms(f"{f_} · {c_} = {f_ * c_}") if r else f"{buit_curt()} · {buit_curt()} = {buit_curt()}"} m²</p>""", r, ".3rem") for l, t, f_, c_, r in V)}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 3 · Mesurar l'àrea · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> És la primera fitxa de la unitat 3, abans de les fraccions, com a la
    programació: l'àrea és quants quadrets ocupa una figura. «1 km = 1.000 m» és l'única excepció a
    la regla dels 999 (decisió del docent del 26/9/2026); el 1.000.000 dels km² queda fora: el km²
    es dibuixa, però no es converteix. La caixa d'eines ho fa a la tasca 13.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb paper quadriculat: retallar el rectangle de 3 per 4 i la ela de 13, posar-los un
  damunt de l'altre i comptar. És l'activitat «Què és més gran?» de la programació.</p>
  <h3>1 i 2. Les unitats</h3>
  <p>1b) km; 1c) m; 1d) km. 2b) km²; 2c) m²; 2d) km². Són les de l'activitat «La història del metre i
  del quilòmetre».</p>
  <h3>3. L'àrea del rectangle</h3>
  <p>b) 5 · 6 = 30; c) 4 · 7 = 28; d) 8 · 9 = 72. És el rectangle de la unitat 1: les files pels
  quadrets de cada fila, amb la targeta.</p>
  <h3>4. Sencers i mitjos</h3>
  <p>b) 10 sencers, 4 mitjos, que fan 2: 12. c) 4 sencers, 8 mitjos, que fan 4: 8. d) 13 sencers, 2
  mitjos, que fan 1: 14. Són les figures de la tasca 13 de la caixa. <b>Error típic:</b> comptar
  cada mig com un quadret sencer, que és la regla trencada d'aquesta fitxa. No l'expliqueu: que
  retalli dos mitjos i els ajunti. Fan un quadret.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>5. A la vida de cada dia</h3>
  <p>b) 8 · 9 = 72 m². c) 2 · 5 = 10 m². És el mateix càlcul que a l'exercici 3, amb metres quadrats.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=13</b> (13.1 Compta l'àrea;
  13.2 Quina àrea té?). La 13.2 dona un codi de verificació; les respostes falses són les dues
  confusions: comptar els mitjos com a sencers, o no comptar-los.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (1.2, 5.2, 6.1 i 9.1) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb paper quadriculat, diu quina figura ocupa més, comptant quadrets.</li>
    <li>Tria la unitat: m o km, m² o km² (exercicis 1 i 2).</li>
    <li>Calcula l'àrea d'un rectangle amb la targeta (exercici 3).</li>
    <li>Compta l'àrea d'una figura amb quadrets sencers i mitjos (exercici 4).</li>
    <li>Nivells alts: explica per què dos mitjos fan un quadret (exercici 4).</li>
  </ul>
</div>''')

document("Unitat 3 · Mesurar l'àrea", """  FITXA · Unitat 3 · Com és de gran Gaza? · Mesurar l'àrea
  La primera fitxa de la unitat 3 en l'ordre de la programació: activitats 2 a
  5 (què és més gran, el metre i el quilòmetre, com mesurar àrees, sumar àrees
  amb fraccions). L'única excepció a la regla dels 999 és «1 km = 1.000 m»
  (decisió del docent del 26/9/2026). Les figures són les de la tasca 13 de la
  caixa (regla 8).

  La regla trencada és comptar un mig com un quadret sencer (exercici 4).""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud3-area.html")
