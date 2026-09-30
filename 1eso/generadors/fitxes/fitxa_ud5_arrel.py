#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud5-arrel.html: quadrats perfectes i arrel quadrada (unitat 5, fitxa 5).

Adapta les activitats 1 («Què en sabem?», els quadrats de cartolina) i 5 («Quadrats perfectes i
arrel quadrada») de la situació «Decimals i arrel quadrada». L'arrel és el costat del quadrat, com
a la unitat 1 (tasca 2.3 de la caixa i fitxa ud1.html): √16 = 4 perquè 4 · 4 = 16. Si el nombre no
és un quadrat, l'arrel és entre dos nombres: 13 és entre 9 i 16, i √13 és entre 3 i 4. El dibuix de
les no exactes és el de la unitat 1 (`entre()` de fitxa_ud1.py).

Fins al 100: la targeta de les taules i la de «Decimals i arrels» acaben a 10 · 10. Aproximar amb
decimals (3,1² = 9,61) queda fora (el pla validat el 29/9/2026). Els casos són els del llibre (√4,
√49, √81, √50 entre 7 i 8, l'error del Joel) i els de la tasca 2.4 de la caixa.

La regla trencada (regla G): «l'arrel és la meitat» (√16 = 8, l'error del Joel), a la pàgina 4.
Les igualtats falses van dins de .revisa.
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
from peces_comunes import *  # noqa: F401,F403  # Dibuix, ms, buit, ULL, els colors
from peces_ud2 import *  # noqa: F401,F403  # tria, fes_pagina, document
from peces_fraccions import *  # noqa: F401,F403  # caixa

pagines = []
pagina = fes_pagina(pagines, "Unitat 5 · Quadrats i arrels · pàgina")


def quadrat(k, m, aria, clau=False):
    """Un quadrat de k per k quadrets. Amb `clau`, la clau del costat a dalt, amb el k."""
    dalt = 0.8 if clau else 0.1
    d = Dibuix(k * m + 0.2, k * m + dalt + 0.1, aria)
    d.rectangle(0.1, dalt, k, k, m)
    if clau:
        d.clau_dalt(0.1, 0.1 + k * m, 0.45, str(k), 0.5)
    return d


def entre(n, m, aria):
    """Com a la unitat 1 (fitxa_ud1.py): el quadrat més gran que es pot fer amb n quadrets, els que
    sobren a la vora del següent (blancs) i els llocs que falten per acabar-lo (discontinus)."""
    k = int(n ** 0.5)
    sob = n - k * k
    d = Dibuix((k + 1) * m + 0.2, (k + 1) * m + 0.2, aria)
    d.rectangle(0.1, 0.1, k, k, m)
    vora = [(fi, k) for fi in range(k)] + [(k, c) for c in range(k, -1, -1)]
    for i, (fi, c) in enumerate(vora):
        if i < sob:
            d.quadret(0.1 + c * m, 0.1 + fi * m, m, fons="#fff")
        else:
            d.quadret(0.1 + c * m, 0.1 + fi * m, m, fons="none", traç=G2, gruix=1.4, discontinu=True)
    return d


# ===================================================================== pàgina 1
d1 = quadrat(4, 0.85, "Un quadrat de 4 files de 4 quadrets, amb el costat marcat: 4", clau=True)
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>quadrats de cartolina</b> de 9, 16 i 25 quadrets. Comptar els quadrets del costat de cada un.</div>
  <h1>Quadrats i arrels</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div class="figura neta" style="margin-top:.8rem">
{d1.svg()}
  </div>

  <table style="margin-top:.6rem">
    <tr class="resolt"><td class="esq">Quants quadrets té el quadrat?</td><td style="width:4cm">{ms("16")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets té el costat?</td><td>{ms("4")}</td></tr>
    <tr class="resolt"><td class="esq">Quant és 4 · 4?</td><td>{ms("16")}</td></tr>
  </table>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">16 quadrets fan un quadrat de 4 per 4.</p>
    <p style="margin:0">L'arrel quadrada de 16 és el costat: 4.</p>
    <p style="margin:.2rem 0 0;font-size:28pt;font-weight:800">√16 = 4</p>
    <p style="margin:0">perquè 4 · 4 = 16.</p>
  </div>''')

# ===================================================================== pàgina 2: el costat del quadrat
E1 = [("a", 3, True), ("b", 5, False), ("c", 6, False), ("d", 7, False)]
it = []
for l, k, r in E1:
    dib = quadrat(k, 0.5, f"Apartat {l}: un quadrat de {k * k} quadrets")
    frase = (f"El costat té {ms(str(k))} quadrets.<br><span style=\"white-space:nowrap\">√{k * k} = {ms(str(k))}</span>" if r
             else f"El costat té {buit_curt()} quadrets.<br><span style=\"white-space:nowrap\">√{k * k} = {buit_curt()}</span>")
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-size:16pt;font-weight:700"><span class="apartat">{l})</span> {k * k} quadrets</p>
      <div style="width:{k * 0.5 + 0.3:.1f}cm">{dib.svg("")}</div>
      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">{frase}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Compta els quadrets del costat. Escriu l'arrel.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 3: l'arrel amb la targeta
E2 = [("a", 8, True), ("b", 9, False), ("c", 2, False), ("d", 10, False), ("e", 7, False)]
files_t = []
for l, k, r in E2:
    cel = (f'<td style="text-align:center">{ms(f"{k} · {k} = {k * k}")}</td><td style="text-align:center">{ms(str(k))}</td>'
           if r else '<td class="omplir" style="height:1.2cm"></td><td class="omplir" style="height:1.2cm"></td>')
    files_t.append(f'''      <tr{' class="resolt"' if r else ''}><td style="font-size:19pt;font-weight:800;padding:.2rem .6rem"><span class="apartat">{l})</span> √{k * k}</td>{cel}</tr>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Busca a la targeta quin nombre per ell mateix dona el de dins. Escriu l'arrel.</div></div>
    <div class="clau" style="margin:.3rem 0 .6rem"><p style="margin:0">√64: a la targeta, 8 · 8 = 64. L'arrel és 8.</p></div>
    <table class="mini">
      <tr><th style="width:4cm">L'arrel</th><th>A la targeta</th><th style="width:3.4cm">L'arrel és</th></tr>
{chr(10).join(files_t)}
    </table>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
E3 = [("a", 16, True), ("b", 36, False), ("c", 4, False), ("d", 100, False)]
it = []
for l, n, r in E3:
    k = int(n ** 0.5)
    meitat = n // 2
    bo = meitat == k
    bona = ms(str(k)) if r else buit_curt()
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-size:16pt;font-weight:700"><span class="apartat">{l})</span> En Joel diu: <span class="revisa">√{n} = {meitat}</span></p>
      <p style="margin:0;font-size:15pt">Té raó?</p>
      {tria(["Sí", "No"], ("Sí" if bo else "No") if r else None, mida="14pt", ample="2.2cm")}
      <p class="frase" style="margin:0;font-size:15pt">Busca a la targeta. L'arrel és {bona}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">En Joel diu que l'arrel és la meitat. Té raó? Busca a la targeta.</div></div>
    <div style="display:flex;gap:.8cm;align-items:center;margin:.2rem 0 .5rem">
      <div style="flex:0 0 auto">{quadrat(4, 0.45, "Un quadrat de 4 per 4: el costat fa 4, no 8", clau=True).svg("")}</div>
      <div class="clau" style="flex:1 1 auto"><p style="margin:0">Un quadrat de 16 quadrets té 4 quadrets de costat. Amb 8 de costat, tindria 8 · 8 = 64 quadrets.</p></div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">L'arrel no és la meitat. L'arrel és el costat.</p>
    <p style="margin:.2rem 0 0">√16 = 4, perquè 4 · 4 = 16.</p>
  </div>''')

# ===================================================================== pàgina 5: les no exactes
E4 = [("a", 13, True), ("b", 20, False), ("c", 50, False), ("d", 90, False)]
it = []
for l, n, r in E4:
    k = int(n ** 0.5)
    if r:
        cos = f'''      <div style="width:3.2cm">{entre(n, 0.6, "13 quadrets: un quadrat de 3 per 3, 4 quadrets de més i 3 llocs buits per fer el de 4 per 4").svg("")}</div>
      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">{n} és entre {ms(str(k * k))} i {ms(str((k + 1) ** 2))}.</p>
      <p class="frase" style="margin:0;font-size:15pt">√{n} és entre {ms(str(k))} i {ms(str(k + 1))}.</p>'''
    else:
        cos = f'''      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">{n} és entre {buit_curt()} i {buit_curt()}.</p>
      <p class="frase" style="margin:0;font-size:15pt">√{n} és entre {buit_curt()} i {buit_curt()}.</p>'''
    it.append(caixa(f'''      <p style="margin:0 0 .1rem;font-size:17pt;font-weight:800"><span class="apartat">{l})</span> √{n}</p>
{cos}''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Aquests nombres no són a la llista de la targeta. Entre quins dos nombres és l'arrel?</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Busca a la targeta el quadrat d'abans i el de després.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 6: la vida
V = [("a", "Una catifa quadrada té 9 m².", 9, True), ("b", "Un hort quadrat té 64 m².", 64, False),
     ("c", "Un pati quadrat té 100 m².", 100, False)]
it = []
for l, t_, n, r in V:
    k = int(n ** 0.5)
    it.append(caixa(f'''      <p style="margin:0 0 .1rem"><span class="apartat">{l})</span> {t_} Quants metres mesura el costat?</p>
      <p class="frase" style="margin:0">El costat mesura {ms(f"{k} m") if r else buit_curt() + " m"}.</p>''', r, ".3rem"))
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Quant mesura el costat? Busca l'arrel a la targeta.</div></div>
{chr(10).join(it)}
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">6</div><div class="q">Tens 30 rajoles quadrades. Pots fer un quadrat amb totes?</div></div>
{caixa(f"""      {tria(["Sí", "No"], None, mida="14pt", ample="2.2cm")}
      <p class="frase" style="margin:0">Amb 25 rajoles fas un quadrat de {buit_curt()} per {buit_curt()}. En sobren {buit_curt()}.</p>""", False, ".3rem")}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 5 · Quadrats i arrels · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> L'arrel quadrada és el costat del quadrat, com a la unitat 1: √16 = 4
    perquè 4 · 4 = 16. Els quadrats perfectes, de 1 · 1 a 10 · 10, són a la targeta «Decimals i
    arrels» i a la de les taules. Si un nombre no hi és, l'arrel és entre dos nombres. Tot fins al
    100. Aproximar l'arrel amb decimals (3,1² = 9,61) queda fora: demana multiplicar decimals.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb quadrats de cartolina (o retallats d'una quadrícula) de 9, 16 i 25 quadrets:
  comptar els quadrets del costat de cada un (3, 4 i 5). És la primera sessió del grup («Què en
  sabem?»).</p>
  <h3>1. Compta el costat</h3>
  <p>b) 5, √25 = 5. c) 6, √36 = 6. d) 7, √49 = 7.</p>
  <h3>2. L'arrel amb la targeta</h3>
  <p>b) 9 · 9 = 81, √81 = 9. c) 2 · 2 = 4, √4 = 2. d) 10 · 10 = 100, √100 = 10. e) 7 · 7 = 49,
  √49 = 7 (els casos del llibre). A la targeta de les taules, els quadrats són els de la diagonal:
  el mateix nombre per ell mateix.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>3. En Joel diu que l'arrel és la meitat · la regla trencada</h3>
  <p>b) No: l'arrel de 36 és 6. c) Sí: l'arrel de 4 és 2, i també és la meitat. d) No: l'arrel de 100
  és 10. <b>Error típic:</b> «l'arrel és la meitat», l'error del Joel del llibre. És la regla trencada
  d'aquesta fitxa. No l'expliqueu: que compti el costat del quadrat de 16 (4, no 8) o que busqui a la
  targeta quin nombre per ell mateix dona el de dins. L'apartat c és a posta: amb el 4, la meitat
  encerta per casualitat. <b>Compta per als nivells alts, no per al mínim.</b></p>
  <h3>4. Entre quins dos nombres</h3>
  <p>b) 20 és entre 16 i 25: √20 és entre 4 i 5. c) 50 és entre 49 i 64: √50 és entre 7 i 8 (l'exemple
  del llibre). d) 90 és entre 81 i 100: √90 és entre 9 i 10. Es pot fer amb quadrets, com l'apartat a:
  el quadrat més gran que surt, i els quadrets que sobren.</p>
  <h3>5 i 6. A la vida de cada dia</h3>
  <p>5b) 8 m. 5c) 10 m. 6) No: amb 25 rajoles es fa un quadrat de 5 per 5, i en sobren 5. 30 no és a la
  llista de quadrats: √30 és entre 5 i 6. <b>Compta per als nivells alts.</b></p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=2</b> (2.3 El costat del
  quadrat; 2.4 Entre quins dos nombres?). La 2.4 dona un codi de verificació; les respostes falses
  són la del Joel (la meitat) i passar-se d'un. Els nombres dels exercicis 3 i 4 surten de la llista
  de la 2.4.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (5.1, 7.1 i 8.1) són de referència:
  l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb un quadrat de cartolina, compta els quadrets del costat.</li>
    <li>Diu l'arrel d'un quadrat perfecte fins al 100, amb el dibuix o la targeta (exercicis 1 i 2).</li>
    <li>Diu entre quins dos nombres és una arrel que no és exacta (exercici 4).</li>
    <li>Diu el costat d'un terreny quadrat a partir dels metres quadrats (exercici 5).</li>
    <li>Nivells alts: diu per què l'arrel no és la meitat (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 5 · Quadrats i arrels", """  FITXA · Unitat 5 · Decimals i arrel quadrada · Quadrats i arrels
  La cinquena fitxa de la unitat 5. Adapta les activitats 1 i 5 de la situació
  (els quadrats de cartolina i «Quadrats perfectes i arrel quadrada»). L'arrel és
  el costat del quadrat, com a la unitat 1: √16 = 4. Si el nombre no és un quadrat,
  l'arrel és entre dos nombres. Fins al 100. Els casos són els del llibre i els de
  la tasca 2.4 de la caixa (regla 8).

  La regla trencada és «l'arrel és la meitat» (√16 = 8, l'error del Joel del
  llibre), pàgina 4. Les igualtats falses van dins de .revisa.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud5-arrel.html")
