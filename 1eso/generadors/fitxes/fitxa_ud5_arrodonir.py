#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud5-arrodonir.html: arrodonir i truncar (unitat 5, fitxa 2).

Adapta la segona part de l'activitat 2 de la situació «Decimals i arrel quadrada» (el llibre:
«Arrodonir i truncar»). Arrodonir a les dècimes és buscar la dècima més a prop; truncar és tallar
i prou. Es fa a la recta numèrica, el segon model del curs per a l'arrodoniment
(docs/MAPA-ADAPTACIO.md, apartat 3), com a la tasca 19 de la caixa.

El pont entre els dos models: la recta de 3,4 a 3,5 és una columna de 10 quadrets ajaguda, un
quadret per centèsima. 3,47 són 7 quadrets de la columna: més de mitja columna, i per això és més a
prop de 3,5.

Els casos són els de la tasca 19 de la caixa i els del llibre (5,86, 6,78, 3,47 i 0,96). Només a
les dècimes, i fins a 9,99 (decisió del docent del 29/9/2026).

La regla trencada (regla G): «arrodonir és tallar», o arrodonir sempre avall (pàgina 4).
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(AQUI, "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])                       # Dibuix, ms, buit, ULL, els colors
exec(open(os.path.join(AQUI, "peces_ud2.py"), encoding="utf-8").read())          # tria, fes_pagina, document
exec(open(os.path.join(AQUI, "peces_fraccions.py"), encoding="utf-8").read())    # caixa

pagines = []
pagina = fes_pagina(pagines, "Unitat 5 · Arrodonir i truncar · pàgina")


def dec(c, x=None):
    """Com CE.q.dec a la caixa: 347 → «3,47»; amb x=1, sempre una xifra decimal: 350 → «3,5», 100 → «1,0»."""
    u, r = divmod(c, 100)
    if x == 1:
        return f"{u},{r // 10}"
    if r == 0:
        return str(u)
    return f"{u},{r // 10}" if r % 10 == 0 else f"{u},{r:02d}"


def arrodonit(c):
    return c - c % 10 + (10 if c % 10 >= 5 else 0)


def truncat(c):
    return c - c % 10


def recta(c, amp, aria, punt=None, punt_ma=False, columna=False):
    """La recta de la dècima d'abans a la de després, com a la caixa (tasca 19): una ratlla per
    centèsima, la del mig discontínua i amb el seu nombre, i els extrems en negreta.
    `punt`: on va el punt (imprès, o a mà amb `punt_ma`). Amb `columna`, a sobre hi va la columna
    de 10 quadrets ajaguda, amb els quadrets de les centèsimes pintats: és el pont amb els blocs."""
    a = c - c % 10
    x0, x1 = 0.7, amp - 0.7
    pas = (x1 - x0) / 10
    dalt = 0.2
    if columna:
        m = pas
        dalt = 0.2 + m + 0.45
    y = dalt + 0.75
    d = Dibuix(amp, y + 1.25, aria)
    if columna:
        for k in range(10):
            pintat = punt is not None and k < punt - a
            d.quadret(x0 + k * m, 0.2, m, fons=F3 if pintat else "#fff", traç=G1 if pintat else G3,
                      gruix=1.6 if pintat else 1.1, aire=0.08)
    d.cru(f'<line x1="{d.px(x0 - 0.35)}" y1="{d.px(y)}" x2="{d.px(x1 + 0.35)}" y2="{d.px(y)}" '
          f'stroke="{G1}" stroke-width="2.4" stroke-linecap="round"/>')
    for k in range(11):
        x = x0 + k * pas
        gran, mig = k in (0, 10), k == 5
        h = 0.34 if gran else 0.26 if mig else 0.15
        dash = ' stroke-dasharray="3 2.5"' if mig else ""
        d.cru(f'<line x1="{d.px(x)}" y1="{d.px(y - h)}" x2="{d.px(x)}" y2="{d.px(y + h)}" stroke="{G1}" '
              f'stroke-width="{2.2 if gran else 1.8}"{dash}/>')
    d.text(x0, y + 0.95, dec(a, 1), 0.55, 800)
    d.text(x1, y + 0.95, dec(a + 10, 1), 0.55, 800)
    d.text((x0 + x1) / 2, y + 0.9, dec(a + 5), 0.45, 400, color=G2)
    if punt is not None:
        x = x0 + (punt - a) * pas
        cor = MS if punt_ma else G1
        d.cru(f'<circle cx="{d.px(x)}" cy="{d.px(y)}" r="{d.px(0.15)}" fill="{cor}" stroke="#fff" stroke-width="1.5"/>')
        d.text(x, y - 0.4, dec(punt), 0.5, 800, ma=punt_ma)
    return d


def aria_recta(c, punt=True):
    a = c - c % 10
    return (f"La recta de {dec(a, 1)} a {dec(a + 10, 1)}, amb una ratlla per centèsima" +
            (f" i el punt a {dec(c)}" if punt else ""))


# ===================================================================== pàgina 1
d1 = recta(347, 12.5, "Una columna de 10 quadrets ajaguda, amb 7 quadrets pintats, i a sota la recta de 3,4 a 3,5 "
                      "amb el punt a 3,47", punt=347, columna=True)
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>una tira de 10 quadrets</b> (una columna de la quadrícula), ajaguda. Va de 3,4 a 3,5. Marcar el mig i posar el dit al quadret 7.</div>
  <h1>Arrodonir i truncar</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div class="figura neta" style="margin-top:.8rem">
{d1.svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.3rem 0 .6rem">La recta és una columna ajaguda. Cada quadret és una centèsima.</p>

  <table>
    <tr class="resolt"><td class="esq">Entre quines dues dècimes és 3,47?</td><td style="width:4.4cm">{ms("3,4 i 3,5")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets hi ha pintats?</td><td>{ms("7")}</td></tr>
    <tr class="resolt"><td class="esq">Passa de la ratlla del mig?</td><td>{ms("Sí")}</td></tr>
  </table>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Arrodonir és buscar la dècima més a prop.</p>
    <p style="margin:0 0 .3rem">3,47 és més a prop de 3,5. Arrodonit a les dècimes, és <b>3,5</b>.</p>
    <p style="margin:0;font-weight:700">Truncar és tallar i prou.</p>
    <p style="margin:0">3,47 truncat a les dècimes és <b>3,4</b>.</p>
  </div>''')

# ===================================================================== pàgina 2: a la recta
E1 = [("a", 347, True), ("b", 586, False), ("c", 471, False), ("d", 234, False)]
it = []
for l, c, r in E1:
    a = c - c % 10
    dib = recta(c, 11.5, aria_recta(c, r), punt=c if r else None, punt_ma=True)
    prop = arrodonit(c)
    frase = (f'És més a prop de {ms(dec(prop, 1))}.' if r else f'És més a prop de {buit()}.')
    it.append(caixa(f'''      <div style="display:flex;gap:.6cm;align-items:center">
        <p style="margin:0;font-size:18pt;font-weight:800;min-width:2.4cm"><span class="apartat">{l})</span> {dec(c)}</p>
        <div style="width:11.5cm">{dib.svg("")}</div>
      </div>
      <p class="frase" style="margin:0 0 0 3rem;font-size:15pt">{frase}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Marca el decimal a la recta. Escriu de quina dècima és més a prop.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Cada ratlla petita és una centèsima. La ratlla del mig és discontínua.</p></div>
{chr(10).join(it)}
  </div>
  <div class="avis puntejat">
    <p style="margin:0">Passa de la ratlla del mig? És més a prop de la dècima de després.</p>
    <p style="margin:0">No arriba a la ratlla del mig? És més a prop de la dècima d'abans.</p>
  </div>''')

# ===================================================================== pàgina 3: arrodoneix i trunca
E2 = [("a", 586, True), ("b", 678, False), ("c", 342, False), ("d", 128, False), ("e", 255, False), ("f", 613, False)]
files_t = []
for l, c, r in E2:
    if r:
        cel = f'<td style="text-align:center">{ms(dec(arrodonit(c), 1))}</td><td style="text-align:center">{ms(dec(truncat(c), 1))}</td>'
    else:
        cel = '<td class="omplir" style="height:1.25cm"></td><td class="omplir" style="height:1.25cm"></td>'
    files_t.append(f'''      <tr{' class="resolt"' if r else ''}><td style="font-size:18pt;font-weight:800;padding:.2rem .6rem"><span class="apartat">{l})</span> {dec(c)}</td>{cel}</tr>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Arrodoneix i trunca a les dècimes. Mira la clau.</div></div>
    <div class="clau" style="margin:.3rem 0 .6rem">
      <p style="margin:0 0 .2rem"><b>Arrodonir.</b> Mira la xifra de les centèsimes.</p>
      <p style="margin:0 0 .2rem">5 o més: amunt. 5,86 arrodonit és 5,9.</p>
      <p style="margin:0 0 .2rem">Menys de 5: avall. 3,42 arrodonit és 3,4.</p>
      <p style="margin:0"><b>Truncar.</b> Talla i prou. 5,86 truncat és 5,8.</p>
    </div>
    <table class="mini">
      <tr><th style="width:4cm">El decimal</th><th>Arrodonit a les dècimes</th><th>Truncat a les dècimes</th></tr>
{chr(10).join(files_t)}
    </table>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
E3 = [("a", 347, 340, True), ("b", 675, 670, False), ("c", 234, 230, False), ("d", 586, 580, False)]
it = []
for l, c, diu, r in E3:
    bo = arrodonit(c) == diu
    dib = recta(c, 9.5, aria_recta(c), punt=c)
    it.append(caixa(f'''      <p style="margin:0;font-size:16pt;font-weight:700"><span class="apartat">{l})</span> L'Oriol diu: {dec(c)} arrodonit és {dec(diu, 1)}. Té raó?</p>
      <div style="display:flex;gap:.8cm;align-items:center">
        <div style="width:9.5cm">{dib.svg("")}</div>
        <div>{tria(["Sí", "No"], ("Sí" if bo else "No") if r else None, mida="15pt", ample="2.4cm")}</div>
      </div>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">L'Oriol sempre arrodoneix avall. Té raó? Mira la recta.</div></div>
{chr(10).join(it)}
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Arrodonir no és tallar.</p>
    <p style="margin:.2rem 0 0">Si les centèsimes són 5 o més, s'arrodoneix amunt: 3,47 arrodonit és 3,5.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
V = [("a", "El Pau fa 1,47 m d'alçada.", "m", 147, True),
     ("b", "La Mia ha corregut 2,38 km.", "km", 238, False),
     ("c", "Una bossa de pomes pesa 1,62 kg.", "kg", 162, False)]
it = []
for l, t_, u, c, r in V:
    res = ms(f"{dec(arrodonit(c), 1)} {u}") if r else f"{buit()} {u}"
    it.append(caixa(f'''      <p style="margin:0 0 .15rem"><span class="apartat">{l})</span> {t_}</p>
      <p class="frase" style="margin:0">Arrodonit a les dècimes: {res}</p>''', r, ".35rem"))
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Arrodoneix cada mesura a les dècimes.</div></div>
{chr(10).join(it)}
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Arrodoneix 0,96 a les dècimes. Mira la targeta.</div></div>
{caixa(f"""      <div style="width:11.5cm">{recta(96, 11.5, aria_recta(96), punt=96).svg("")}</div>
      <p class="frase" style="margin:0">0,96 arrodonit a les dècimes: {buit()}</p>""", False, ".35rem")}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 5 · Arrodonir i truncar · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Arrodonir a les dècimes és buscar la dècima més a prop; truncar és
    tallar i prou. Es fa a la recta, com a la tasca 19 de la caixa. La recta de 3,4 a 3,5 és una
    columna de 10 quadrets ajaguda, un quadret per centèsima: és el pont amb els blocs de la fitxa
    1. Només a les dècimes. La targeta «Decimals i arrels» porta la regla: 5 o més, amunt.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb una tira de 10 quadrets retallada d'una quadrícula, ajaguda. Escriure 3,4 a
  l'esquerra i 3,5 a la dreta, marcar el mig (5 quadrets) i posar el dit al quadret 7: és 3,47.
  Preguntar: «És més a prop del 3,4 o del 3,5?».</p>
  <h3>1. Marca el decimal a la recta</h3>
  <p>b) 5,86: entre 5,8 i 5,9, sisena ratlla; més a prop de 5,9. c) 4,71: primera ratlla; més a
  prop de 4,7. d) 2,34: quarta ratlla; més a prop de 2,3. <b>Error típic:</b> posar el punt
  comptant des de la dreta. Que compti les ratlles des de la dècima d'abans.</p>
  <h3>2. Arrodoneix i trunca</h3>
  <table>
    <tr><th></th><th>Arrodonit</th><th>Truncat</th></tr>
    <tr><td>b) 6,78</td><td>6,8</td><td>6,7</td></tr>
    <tr><td>c) 3,42</td><td>3,4</td><td>3,4</td></tr>
    <tr><td>d) 1,28</td><td>1,3</td><td>1,2</td></tr>
    <tr><td>e) 2,55</td><td>2,6</td><td>2,5</td></tr>
    <tr><td>f) 6,13</td><td>6,1</td><td>6,1</td></tr>
  </table>
  <p>Quan les centèsimes són menys de 5 (c i f), arrodonir i truncar donen el mateix. L'apartat e és
  just a la ratlla del mig: s'arrodoneix amunt.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>3. L'Oriol sempre arrodoneix avall · la regla trencada</h3>
  <p>b) No: 6,75 arrodonit és 6,8. c) Sí: 2,34 arrodonit és 2,3. d) No: 5,86 arrodonit és 5,9.
  <b>Error típic:</b> «arrodonir és tallar», que és el que fa l'Oriol: confondre arrodonir amb
  truncar. És la regla trencada d'aquesta fitxa. No l'expliqueu: que miri a la recta si el punt passa
  de la ratlla del mig. L'apartat c és a posta: de vegades l'Oriol encerta, perquè avall també pot
  ser la bona. <b>Compta per als nivells alts, no per al mínim.</b></p>
  <h3>4 i 5. A la vida de cada dia</h3>
  <p>4b) 2,4 km. 4c) 1,6 kg. 5) 1,0: 0,96 és més a prop d'1 que de 0,9, perquè passa de la ratlla
  del mig (0,95). El 9 de les dècimes puja a 10 dècimes, que fan 1 unitat: la targeta ho diu
  («10 columnes fan 1 quadrat»). És un cas del llibre. <b>Compta per als nivells alts.</b></p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=19</b> (19.1 El decimal a
  la recta; 19.2 Arrodoneix). La 19.2 dona un codi de verificació; les respostes falses són truncar
  en lloc d'arrodonir, anar amunt quan no toca i arrodonir a les unitats. L'exemple de la fitxa és el
  de la caixa, 3,47, i els casos surten de la llista de la 19.2.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la recta o la targeta al davant. Els criteris de la SA del grup (5.1, 7.1 i 8.1) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb la tira de 10 quadrets, diu si un decimal passa de la meitat.</li>
    <li>Marca un decimal a la recta i diu de quina dècima és més a prop (exercici 1).</li>
    <li>Arrodoneix i trunca a les dècimes amb la clau al davant (exercicis 2 i 4).</li>
    <li>Nivells alts: diu per què arrodonir no és tallar (exercici 3) i arrodoneix 0,96 a 1,0 (exercici 5).</li>
  </ul>
</div>''')

document("Unitat 5 · Arrodonir i truncar", """  FITXA · Unitat 5 · Decimals i arrel quadrada · Arrodonir i truncar
  La segona fitxa de la unitat 5. Adapta la segona part de l'activitat 2 de la
  situació (el llibre: «Arrodonir i truncar»). Arrodonir és buscar la dècima més
  a prop, a la recta; truncar és tallar i prou. La recta de 3,4 a 3,5 és una
  columna de 10 quadrets ajaguda. Els casos són els de la tasca 19 de la caixa i
  els del llibre (regla 8).

  La regla trencada és «arrodonir és tallar»: l'Oriol sempre arrodoneix avall
  (pàgina 4).""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud5-arrodonir.html")
