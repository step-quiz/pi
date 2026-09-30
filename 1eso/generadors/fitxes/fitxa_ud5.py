#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud5.html: els decimals (unitat 5, fitxa 1).

Adapta les activitats 1 i 2 de la situació «Decimals i arrel quadrada» (el llibre: «Què en sabem?»
i «Els decimals»). És la fitxa de centenes, desenes i unitats de la unitat 1 (fitxa_ud1_nombres.py),
amb els mateixos blocs: ara el quadrat de 100 és 1 unitat, la columna és 1 dècima i el quadret
solt és 1 centèsima. El 243 d'allà aquí és 2,43.

Fins a 9,99 i amb dues xifres decimals com a molt (decisió del docent del 29/9/2026). Els casos
són els de la tasca 18 de la caixa, i del llibre: el valor del 7 (0,7, 0,07, 5,17 i 7,2), 3,4 i
3,04, l'error de la Berta (0,8 i 0,75) i ordenar 2,5, 2,05 i 2,55.

La regla trencada (regla G): «més xifres vol dir més gran» (pàgina 6). El zero que guarda el lloc
(3,04 fet com a 3,4) és a la pàgina 5.
"""
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
from peces_comunes import *  # noqa: F401,F403  # Dibuix, ms, buit, ULL, els colors
from peces_ud2 import *  # noqa: F401,F403  # tria, fes_pagina, document
from peces_fraccions import *  # noqa: F401,F403  # caixa
from peces_nombres import peca, blocs  # noqa: F401

pagines = []
pagina = fes_pagina(pagines, "Unitat 5 · Els decimals · pàgina")


def xifres(c):
    """Les centèsimes (243) → (unitats, dècimes, centèsimes): (2, 4, 3)."""
    return c // 100, c // 10 % 10, c % 10


def dec(c):
    """243 → «2,43»; 150 → «1,5»; 300 → «3». Com CE.q.dec a la caixa."""
    u, r = divmod(c, 100)
    if r == 0:
        return str(u)
    return f"{u},{r // 10}" if r % 10 == 0 else f"{u},{r:02d}"


def taula_dec(u, d, c, ma=False, cel="2.3cm", buida=False):
    """La taula de posicions dels decimals: Unitats | , | Dècimes | Centèsimes (com la caixa, tasca 18)."""
    v = (lambda t: ms(str(t))) if ma else str
    td = 'style="text-align:center;font-size:17pt;font-weight:800;height:1.1cm"'
    coma = '<td style="border:0;text-align:center;font-size:20pt;font-weight:800;width:.5cm">,</td>'
    if buida:
        cos = f'<td class="omplir" style="height:1.1cm"></td>{coma}<td class="omplir" style="height:1.1cm"></td><td class="omplir" style="height:1.1cm"></td>'
    else:
        cos = f'<td {td}>{v(u)}</td>{coma}<td {td}>{v(d)}</td><td {td}>{v(c)}</td>'
    return (f'<table class="mini" style="width:auto;margin:0 auto"><tr><th style="width:{cel}">Unitats</th>'
            f'<th style="border:0;background:none"></th><th style="width:{cel}">Dècimes</th>'
            f'<th style="width:{cel}">Centèsimes</th></tr><tr>{cos}</tr></table>')


def aria(c, lletra=None):
    u, d, q = xifres(c)
    cap = f"Apartat {lletra}: " if lletra else ""
    return f"{cap}{u} quadrats de 100, {d} columnes de 10 i {q} quadrets solts"


# ===================================================================== pàgina 1
d1 = blocs(2, 4, 3, 0.2, aria(243))
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>la quadrícula de 100</b>. És 1. Pintar-ne una columna: és 0,1. Pintar-ne un quadret: és 0,01.</div>
  <h1>Els decimals</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div class="figura neta" style="margin-top:1rem">
{d1.svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .5rem">Ara el quadrat de 100 és 1.</p>

  <table>
    <tr class="resolt"><td class="esq">Quants quadrats de 100 hi ha?</td><td style="width:4cm">{ms("2")}</td></tr>
    <tr class="resolt"><td class="esq">Quantes columnes de 10 hi ha?</td><td>{ms("4")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets solts hi ha?</td><td>{ms("3")}</td></tr>
  </table>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">El quadrat de 100 és 1 unitat.</p>
    <p style="margin:0">La columna és 1 dècima: 0,1.</p>
    <p style="margin:0 0 .5rem">El quadret solt és 1 centèsima: 0,01.</p>
    {taula_dec(2, 4, 3)}
    <p style="font-size:30pt;font-weight:800;margin:.3rem 0 0">2,43</p>
    <p style="margin:0">Es llegeix: dues unitats i quaranta-tres centèsimes.</p>
  </div>''')

# ===================================================================== pàgina 2: mira els blocs
files_t = []
for lletra, c, resolt in [("a", 243, True), ("b", 150, False), ("c", 304, False), ("d", 75, False)]:
    u, d, q = xifres(c)
    # A 0,145 i no a 0,16: amb les capçaleres a 14 pt, la taula sortia pel marge dret (29/9/2026).
    dib = blocs(u, d, q, 0.145, aria(c, lletra))
    if resolt:
        cel = "".join(f'<td style="text-align:center">{ms(str(v))}</td>' for v in (u, d, q)) + \
              f'<td style="text-align:center">{ms(dec(c))}</td>'
    else:
        cel = '<td class="omplir"></td>' * 4
    files_t.append(f'''      <tr{' class="resolt"' if resolt else ''}>
        <td style="padding:.3rem .4rem"><span class="apartat">{lletra})</span>
{dib.svg("          ")}
        </td>
        {cel}
      </tr>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Mira els blocs. Escriu quants n'hi ha de cada. Després escriu el decimal.</div></div>
    <table class="mini" style="margin-top:.5rem">
      <tr><th>Els blocs</th><th style="width:2.3cm">Unitats</th><th style="width:2.3cm">Dècimes</th><th style="width:2.3cm">Centèsimes</th><th style="width:2.6cm">El decimal</th></tr>
{chr(10).join(files_t)}
    </table>
  </div>

  <div class="avis puntejat">
    <p style="margin:0">Compta els blocs amb el dit.</p>
    <p style="margin:0">Si no n'hi ha cap, escriu un 0.</p>
    <p style="margin:0">La coma va just després de les unitats.</p>
  </div>''')

# ===================================================================== pàgina 3: escriu les xifres i pinta
files_p = []
for lletra, c, resolt in [("a", 243, True), ("b", 105, False), ("c", 208, False), ("d", 60, False)]:
    u, d, q = xifres(c)
    dib = blocs(0, 0, 0, 0.16, f"Apartat {lletra}: 3 quadrats de 100, 9 columnes de 10 i 9 quadrets per pintar",
                buits=(3, 9, 9), pinta=(u, d, q) if resolt else None)
    petita = taula_dec(u, d, q, ma=True, cel="2.1cm") if resolt else taula_dec(0, 0, 0, cel="2.1cm", buida=True)
    fons = (' class="resolt" style="border-radius:10px;padding:.35rem .5rem;margin-bottom:.45rem"' if resolt
            else ' style="padding:.35rem .5rem;margin-bottom:.45rem"')
    files_p.append(f'''    <div{fons}>
      <div style="display:flex;gap:.8cm;align-items:center;margin-bottom:.35rem">
        <p style="margin:0;font-size:17pt;font-weight:800;min-width:2.2cm"><span class="apartat">{lletra})</span> {dec(c)}</p>
        <div style="flex:0 0 auto">{petita}</div>
      </div>
{dib.svg("      ")}
    </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Escriu les xifres a la taula. Després pinta els blocs.</div></div>
{chr(10).join(files_p)}
  </div>''')

# ===================================================================== pàgina 4: què val el 7 (el llibre, activitat 2)
VAL = [("a", "0,7", "7 dècimes", True), ("b", "0,07", "7 centèsimes", False), ("c", "5,17", "7 centèsimes", False),
       ("d", "7,2", "7 unitats", False)]
it = []
for lletra, n, bona, resolt in VAL:
    u, _, resta = n.partition(",")
    d, q = (resta + "0")[:2]
    it.append(caixa(f'''      <div style="display:flex;gap:.8cm;align-items:center">
        <p style="margin:0;font-size:20pt;font-weight:800;min-width:2.6cm"><span class="apartat">{lletra})</span> {n}</p>
        <div style="flex:0 0 auto">{taula_dec(u, d, q, ma=True, cel="2.1cm") if resolt else taula_dec(0, 0, 0, cel="2.1cm", buida=True)}</div>
      </div>
      <p style="margin:.3rem 0 0;font-size:15pt">Què val el 7?</p>
      {tria(["7 unitats", "7 dècimes", "7 centèsimes"], bona if resolt else None, mida="14pt", ample="3.6cm")}''',
                    resolt, ".35rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Escriu cada decimal a la taula. Marca què val el 7.</div></div>
{chr(10).join(it)}
  </div>''')

# ===================================================================== pàgina 5: marca el decimal (el zero)
QUIN = [("a", 304, ["3,4", "3,04", "304"], True), ("b", 105, ["1,05", "1,5", "105"], False),
        ("c", 490, ["49", "4,09", "4,9"], False), ("d", 612, ["6,12", "612", "6,21"], False)]
items_q = []
for lletra, c, opcions, resolt in QUIN:
    u, d, q = xifres(c)
    dib = blocs(u, d, q, 0.15, aria(c, lletra))
    fons = (' class="resolt" style="border-radius:10px;padding:.3rem .6rem;margin-bottom:.35rem"' if resolt
            else ' style="padding:.3rem .6rem;margin-bottom:.35rem"')
    explica = (f'\n      <p style="margin:.15rem 0 0;font-size:14pt">{u} unitats, cap dècima i {q} centèsimes.</p>'
               if resolt else "")
    items_q.append(f'''    <div{fons}>
      <div style="display:flex;gap:.6cm;align-items:center">
        <p class="apartat" style="margin:0">{lletra})</p>
        <div style="flex:0 0 auto">
{dib.svg("          ")}
        </div>
      </div>
      {tria(opcions, dec(c) if resolt else None, mida="16pt", ample="2.6cm")}{explica}
    </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Marca el decimal de cada dibuix.</div></div>
{chr(10).join(items_q)}
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">El 0 guarda el lloc de les dècimes.</p>
    <p style="margin:.2rem 0 0">3,04 té 3 quadrats de 100, cap columna i 4 quadrets solts.</p>
  </div>''')

# ===================================================================== pàgina 6: quin és més gran (la regla trencada)
COMP = [("a", 80, 75, True), ("b", 340, 304, False), ("c", 250, 245, False), ("d", 155, 150, False)]
it = []
for lletra, g, p, resolt in COMP:
    parts = []
    for c in (g, p) if lletra in "ac" else (p, g):
        u, d, q = xifres(c)
        parts.append(f'''        <div style="display:flex;gap:.4cm;align-items:center;margin:.1rem 0">
          <p style="margin:0;font-size:17pt;font-weight:800;min-width:1.6cm">{dec(c)}</p>
          <div>{blocs(u, d, q, 0.13, f"{dec(c)}: {u} quadrats de 100, {d} columnes de 10 i {q} quadrets solts").svg("")}</div>
        </div>''')
    opcions = [dec(g), dec(p)] if lletra in "ac" else [dec(p), dec(g)]
    it.append(caixa(f'''      <p style="margin:0 0 .1rem;font-size:15pt;font-weight:700"><span class="apartat">{lletra})</span> Quin és més gran?</p>
{chr(10).join(parts)}
      {tria(opcions, dec(g) if resolt else None, mida="15pt", ample="2.3cm")}''', resolt, ".25rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Quin és més gran? Mira els blocs. Marca el més gran.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">La Berta diu que 0,75 és més gran, perquè té més xifres. Mira els blocs.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Tenir més xifres no vol dir ser més gran.</p>
    <p style="margin:.2rem 0 0">Escriu els dos amb dues xifres: 0,8 és 0,80. Com que 80 és més que 75, 0,8 és més gran.</p>
  </div>''')

# ===================================================================== pàgina 7: la vida
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">6</div><div class="q">Escriu els dos nombres amb dues xifres després de la coma. Després compara.</div></div>
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Al salt de llargada, la Nora salta 2,5 m. El Pau salta 2,45 m. Qui salta més lluny?</p>
      <p class="frase" style="margin:0">2,50 i 2,45. Salta més lluny {ms("la Nora")}.</p>""", True, ".4rem")}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> La Laia fa 1,5 m d'alçada i el Joan fa 1,48 m. Qui és més alt?</p>
      <p class="frase" style="margin:0">{buit()} i {buit()}. És més alt {buit()}.</p>""", False, ".4rem")}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">c)</span> L'ampolla de l'Arnau té 1,5 litres d'aigua. L'ampolla de la Mia té 1,25 litres. Quina té més aigua?</p>
      <p class="frase" style="margin:0">{buit()} i {buit()}. Té més aigua l'ampolla {buit()}.</p>""", False, ".4rem")}
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">7</div><div class="q">Ordena els salts, de més curt a més llarg.</div></div>
{caixa(f"""      <p style="margin:0 0 .2rem">Tres salts: 2,5 m, 2,05 m i 2,55 m.</p>
      <p class="frase" style="margin:0">{buit()} m, {buit()} m, {buit()} m</p>""", False, ".4rem")}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 5 · Els decimals · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Són els blocs de la unitat 1, i es diuen igual: «quadrats de 100»,
    «columnes de 10» i «quadrets solts». Canvia una sola cosa: ara el quadrat de 100 és 1 unitat, la
    columna és 1 dècima i el quadret solt és 1 centèsima. El 243 de la unitat 1 aquí és 2,43. La
    targeta «Decimals i arrels» és al davant tota l'estona. Tots els decimals van fins a 9,99, amb dues
    xifres com a molt.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb una quadrícula de 100 retallada: dir que tota la quadrícula és 1, pintar-ne una
  columna i dir «0,1, una dècima», i pintar-ne un quadret i dir «0,01, una centèsima». Serveixen les
  quadrícules de la unitat 1, o les dels percentatges de la unitat 4.</p>
  <h3>1. Mira els blocs</h3>
  <table>
    <tr><th></th><th>Unitats</th><th>Dècimes</th><th>Centèsimes</th><th>El decimal</th></tr>
    <tr><td>b)</td><td>1</td><td>5</td><td>0</td><td>1,5</td></tr>
    <tr><td>c)</td><td>3</td><td>0</td><td>4</td><td>3,04</td></tr>
    <tr><td>d)</td><td>0</td><td>7</td><td>5</td><td>0,75</td></tr>
  </table>
  <p>Es dona per bo 1,50: és el mateix nombre que 1,5. <b>Error típic:</b> llegir els blocs com a la
  unitat 1, sense coma (150, 304, 75). L'avís del final de la pàgina recorda on va la coma.</p>
  <h3>2. Escriu les xifres i pinta els blocs</h3>
  <p>b) 1,05: 1 quadrat, cap columna i 5 quadrets. c) 2,08: 2 quadrats, cap columna i 8 quadrets.
  d) 0,6: cap quadrat, 6 columnes i cap quadret. Hi ha més siluetes de les que cal, a posta: triar
  quantes se'n pinten és la feina.</p>
  <h3>3. Què val el 7</h3>
  <p>b) 7 centèsimes (0 unitats, 0 dècimes i 7 centèsimes); c) 7 centèsimes (5, 1 i 7); d) 7 unitats
  (7, 2 i 0). La taula ho resol: el lloc on cau el 7 diu què val. Són els casos del llibre.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>4. Marca el decimal de cada dibuix</h3>
  <p>b) 1,05; c) 4,9; d) 6,12. Les opcions són les confusions de debò: girar les columnes i els
  quadrets (1,5 per 1,05; 4,09 per 4,9; 6,21 per 6,12) i llegir els blocs sense coma (105, 612).
  <b>Error típic:</b> el zero. 3,04 fet com a 3,4 és el mateix error que el 305 fet com a 35 de la
  unitat 1: que compti les columnes, i el 0 surt sol.</p>
  <h3>5. Quin és més gran · la regla trencada</h3>
  <p>b) 3,4; c) 2,5; d) 1,55. <b>Error típic:</b> triar el que té més xifres (0,75 davant de 0,8;
  3,04 davant de 3,4; 2,45 davant de 2,5). És la regla trencada d'aquesta fitxa, l'error de la Berta
  del llibre. No l'expliqueu: que compti les columnes de cada un als blocs (8 i 7). L'apartat d va a
  l'inrevés a posta (el més gran té més xifres), perquè «menys xifres, més gran» tampoc no és una
  regla. <b>Compta per als nivells alts, no per al mínim.</b></p>
  <h3>6 i 7. A la vida de cada dia</h3>
  <p>6b) 1,50 i 1,48: és més alta la Laia. 6c) 1,50 i 1,25: té més aigua l'ampolla de l'Arnau.
  7) 2,05 m, 2,5 m, 2,55 m (els casos del llibre; 2,05 és el més curt perquè no té cap dècima).</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=18</b> (18.1 Fes el decimal;
  18.2 Quin decimal és?; 18.3 Quin és més gran?). La 18.2 i la 18.3 donen un codi de verificació.
  L'exemple de la fitxa és el de la caixa, 2,43, i els casos dels exercicis 1, 4 i 5 surten de les
  llistes de la 18.2 i la 18.3.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb els blocs, la taula o la targeta al davant. Els criteris de la SA del grup (5.1, 7.1
  i 8.1) són de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb la quadrícula de 100, diu que tota és 1, que una columna és 0,1 i que un quadret és 0,01.</li>
    <li>Diu quants quadrats, columnes i quadrets té un dibuix, i escriu el decimal amb la coma (exercici 1).</li>
    <li>Escriu les xifres d'un decimal a la taula i en pinta els blocs, també quan té un zero (exercici 2).</li>
    <li>Diu què val una xifra segons el lloc on és (exercici 3).</li>
    <li>Nivells alts: compara dos decimals amb diferent nombre de xifres, igualant-les (exercicis 5 i 6).</li>
  </ul>
</div>''')

document("Unitat 5 · Els decimals", """  FITXA · Unitat 5 · Decimals i arrel quadrada · Els decimals
  La primera fitxa de la unitat 5. Adapta les activitats 1 i 2 de la situació (el
  llibre: «Què en sabem?» i «Els decimals»). Són els blocs de la unitat 1 amb el
  quadrat de 100 com a unitat: la columna és 0,1 i el quadret solt, 0,01. Els
  casos són els de la tasca 18 de la caixa i els del llibre (regla 8).

  La regla trencada és «més xifres vol dir més gran» (pàgina 6, l'error de la
  Berta del llibre). El zero que guarda el lloc és a la pàgina 5.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud5.html")
