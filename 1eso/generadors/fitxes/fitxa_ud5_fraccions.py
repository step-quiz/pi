#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud5-fraccions.html: de la fracció al decimal (unitat 5, fitxa 4).

Adapta l'activitat 4 de la situació «Decimals i arrel quadrada». Una fracció es passa a decimal al
quadrat de 100: 1/4 de 100 quadrets són 25 quadrets (la fracció d'un nombre, unitat 4), i 25
quadrets són 2 columnes i 5 quadrets: 0,25. És el quadrat dels percentatges (25 %). I al revés:
0,3 són 3 columnes, 3/10.

Només les fraccions que fan quadrets sencers de 100, amb denominador 2, 4, 5 o 10: els decimals
exactes del nivell 1 del criteri 5.1. Els periòdics queden fora (decisió del docent del 29/9/2026).
Els casos són els de la tasca 21 de la caixa.

La regla trencada (regla G): posar el de baix després de la coma (1/4 = 0,4), a la pàgina 4. Les
igualtats falses van dins de .revisa.
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(AQUI, "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])                       # Dibuix, ms, buit, ULL, els colors
exec(open(os.path.join(AQUI, "peces_ud2.py"), encoding="utf-8").read())          # tria, fes_pagina, document
exec(open(os.path.join(AQUI, "peces_fraccions.py"), encoding="utf-8").read())    # fr, fr_buit, caixa

pagines = []
pagina = fes_pagina(pagines, "Unitat 5 · De la fracció al decimal · pàgina")


def dec(c):
    u, r = divmod(c, 100)
    if r == 0:
        return str(u)
    return f"{u},{r // 10}" if r % 10 == 0 else f"{u},{r:02d}"


def quadrets(n, d):
    return 100 // d * n


def quadrat100(n, m, aria, ma=False):
    """El quadrat de 100 amb n quadrets pintats, columna a columna i de dalt a baix, com a la caixa
    (tasca 21) i a la targeta. Sense números. Amb n=0, buit per pintar-hi. Amb `ma`, pintat a mà."""
    d = Dibuix(10 * m + 0.2, 10 * m + 0.2, aria)
    x0 = y0 = 0.1
    fons = VORA_SUAU if ma else F3
    for i in range(n):
        col, fila = divmod(i, 10)
        d.cru(f'<rect x="{d.px(x0 + col * m)}" y="{d.px(y0 + fila * m)}" width="{d.px(m)}" height="{d.px(m)}" '
              f'fill="{fons}" stroke="none"/>')
    for k in range(1, 10):
        d.cru(f'<line x1="{d.px(x0)}" y1="{d.px(y0 + k * m)}" x2="{d.px(x0 + 10 * m)}" y2="{d.px(y0 + k * m)}" '
              f'stroke="{G3}" stroke-width="0.9"/>')
        d.cru(f'<line x1="{d.px(x0 + k * m)}" y1="{d.px(y0)}" x2="{d.px(x0 + k * m)}" y2="{d.px(y0 + 10 * m)}" '
              f'stroke="{G3}" stroke-width="0.9"/>')
    d.cru(f'<rect x="{d.px(x0)}" y="{d.px(y0)}" width="{d.px(10 * m)}" height="{d.px(10 * m)}" fill="none" '
          f'stroke="{G1}" stroke-width="2"/>')
    return d


# ===================================================================== pàgina 1
d1 = quadrat100(25, 0.55, "El quadrat de 100 amb 25 quadrets pintats: 2 columnes i 5 quadrets")
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>la quadrícula de 100</b>. Repartir-la en 4 parts iguals. Cada part són 25 quadrets.</div>
  <h1>De la fracció al decimal</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div class="figura neta" style="margin-top:.8rem;width:5.8cm;margin-left:auto;margin-right:auto">
{d1.svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .5rem">És {fr(1, 4, "15pt")} del quadrat de 100.</p>

  <table>
    <tr class="resolt"><td class="esq">Quants quadrets hi ha pintats?</td><td style="width:4cm">{ms("25")}</td></tr>
    <tr class="resolt"><td class="esq">Quantes columnes plenes hi ha?</td><td>{ms("2")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets solts hi ha?</td><td>{ms("5")}</td></tr>
  </table>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">{fr(1, 4, "14pt")} de 100 quadrets són 25 quadrets.</p>
    <p style="margin:0">2 columnes i 5 quadrets: 2 dècimes i 5 centèsimes.</p>
    <p style="margin:.2rem 0 0;font-size:28pt;font-weight:800">{fr(1, 4, "22pt")} = 0,25</p>
    <p style="margin:0">És el 25 %, com a la unitat 4.</p>
  </div>''')

# ===================================================================== pàgina 2: pinta i escriu el decimal
E1 = [("a", 1, 2, True), ("b", 1, 5, False), ("c", 3, 4, False), ("d", 3, 10, False)]
it = []
for l, n, d, r in E1:
    q = quadrets(n, d)
    dib = quadrat100(q if r else 0, 0.4, f"Apartat {l}: el quadrat de 100" + (f", amb {q} quadrets pintats" if r else ", per pintar"), ma=r)
    frase = (f"Són {ms(str(q))} quadrets. {fr(n, d, '14pt')} = {ms(dec(q))}" if r
             else f"Són {buit_curt()} quadrets. {fr(n, d, '14pt')} = {buit_curt()}")
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-size:16pt;font-weight:700"><span class="apartat">{l})</span> {fr(n, d, "15pt")}</p>
      <div style="width:4.2cm">{dib.svg("")}</div>
      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">{frase}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Pinta la fracció al quadrat de 100, columna a columna. Escriu el decimal.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Una columna és 0,1. Un quadret és 0,01. Mira la targeta.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 3: del decimal a la fracció
E2 = [("a", 30, 3, 10, True), ("b", 70, 7, 10, False), ("c", 50, 1, 2, False), ("d", 25, 1, 4, False)]
it = []
for l, c, n, d, r in E2:
    dib = quadrat100(c, 0.3, f"Apartat {l}: el quadrat de 100 amb {c} quadrets pintats")
    res = fr(n, d, ma=True) if r else fr_buit("13pt")
    it.append(caixa(f'''      <div style="display:flex;gap:.6cm;align-items:center">
        <div style="width:3.2cm">{dib.svg("")}</div>
        <p class="frase" style="margin:0;font-size:17pt"><span class="apartat">{l})</span> {dec(c)} = {res}</p>
      </div>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Escriu la fracció de cada decimal. Mira el dibuix i la targeta.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">0,3 són 3 columnes de 10. Com que hi ha 10 columnes, és {fr(3, 10, "14pt")}.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
E3 = [("a", 1, 4, "0,4", True), ("b", 1, 2, "0,2", False), ("c", 1, 5, "0,5", False), ("d", 1, 10, "0,1", False)]
it = []
for l, n, d, diu, r in E3:
    q = quadrets(n, d)
    bo = dec(q) == diu
    dib = quadrat100(q, 0.3, f"Apartat {l}: el quadrat de 100 amb {q} quadrets pintats")
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-size:16pt;font-weight:700"><span class="apartat">{l})</span> En Pol diu: <span class="revisa">{fr(n, d, "15pt")} = {diu}</span></p>
      <div style="display:flex;gap:.6cm;align-items:center">
        <div style="width:3.2cm">{dib.svg("")}</div>
        <div>
          <p style="margin:0;font-size:15pt">Té raó?</p>
          {tria(["Sí", "No"], ("Sí" if bo else "No") if r else None, mida="14pt", ample="2.2cm")}
        </div>
      </div>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">En Pol posa el de baix després de la coma. Té raó? Compta les columnes.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">El de baix no va després de la coma.</p>
    <p style="margin:.2rem 0 0">{fr(1, 4, "14pt")} de 100 quadrets són 25 quadrets. Per això {fr(1, 4, "14pt")} = 0,25.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida (fraccions d'euro)
V = [("a", 1, 4, "0,25", True), ("b", 1, 2, "0,50", False), ("c", 3, 4, "0,75", False), ("d", 1, 10, "0,10", False)]
it = []
for l, n, d, res, r in V:
    q = quadrets(n, d)
    it.append(caixa(f'''      <p class="frase" style="margin:0;font-size:16pt"><span class="apartat">{l})</span> {fr(n, d, "15pt")} d'euro són {ms(str(q)) if r else buit_curt()} cèntims: {ms(res) if r else buit_curt()} €</p>''', r, ".3rem"))
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="clau" style="margin:.2rem 0 .6rem">
    <p style="margin:0">Un euro són 100 cèntims, com el quadrat de 100 quadrets.</p>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Quants cèntims són? Escriu també quants euros són.</div></div>
{chr(10).join(it)}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append(f'''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 5 · De la fracció al decimal · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Una fracció es passa a decimal al quadrat de 100: 1/4 de 100 quadrets
    són 25 quadrets (la fracció d'un nombre de la unitat 4), i 25 quadrets són 2 columnes i 5
    quadrets, 0,25. És el quadrat dels percentatges. Només denominadors 2, 4, 5 i 10: els decimals
    exactes. Els periòdics (1/3) queden fora. La targeta «Decimals i arrels» porta les cinc fraccions
    de sempre amb el decimal i el percentatge.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb una quadrícula de 100: repartir-la en 4 parts iguals (per exemple, doblegant-la)
  i comptar els quadrets d'una part, 25. Dir-ho de les tres maneres: un quart, 0,25 i el 25 %.</p>
  <h3>1. Pinta i escriu el decimal</h3>
  <p>b) 20 quadrets, 0,2. c) 75 quadrets, 0,75. d) 30 quadrets, 0,3. Es pinta columna a columna, com
  a la caixa: així les columnes plenes són les dècimes. <b>Error típic:</b> pintar per files; es dona
  per bo si el nombre de quadrets és el correcte.</p>
  <h3>2. Del decimal a la fracció</h3>
  <p>b) {fr(7, 10)}. c) {fr(1, 2)} (també {fr(5, 10)}). d) {fr(1, 4)} (també {fr(25, 100)}). Les formes
  de la targeta són les que es demanen; les equivalents es donen per bones.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>3. En Pol posa el de baix després de la coma · la regla trencada</h3>
  <p>b) No: 1/2 són 50 quadrets, 0,5. c) No: 1/5 són 20 quadrets, 0,2. d) Sí: 1/10 són 10 quadrets,
  una columna, 0,1. <b>Error típic:</b> posar el de baix després de la coma (1/4 = 0,4), o fer de la
  barra una coma (1/4 = 1,4). És la regla trencada d'aquesta fitxa. No l'expliqueu: que compti les
  columnes del dibuix. L'apartat d és a posta: amb 1/10 la regla del Pol encerta per casualitat.
  <b>Compta per als nivells alts, no per al mínim.</b></p>
  <h3>4. A la vida de cada dia</h3>
  <p>b) 50 cèntims, 0,50 €. c) 75 cèntims, 0,75 €. d) 10 cèntims, 0,10 €. Els preus s'escriuen
  sempre amb dues xifres: 0,50 € és el mateix que 0,5.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=21</b> (21.1 Pinta la
  fracció; 21.2 De fracció a decimal). La 21.2 dona un codi de verificació; les respostes falses són
  les del Pol (el de baix després de la coma) i la barra com una coma. L'exemple de la fitxa és el
  de la caixa, 1/4 = 0,25.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb el quadrat de 100 o la targeta al davant. Els criteris de la SA del grup (5.1, 7.1 i
  8.1) són de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb la quadrícula de 100, pinta una fracció i diu quants quadrets són.</li>
    <li>Passa una fracció de denominador 2, 4, 5 o 10 a decimal, amb el quadrat de 100 (exercici 1).</li>
    <li>Passa un decimal a fracció, amb el dibuix o la targeta (exercici 2).</li>
    <li>Diu quants cèntims són un quart, mig i tres quarts d'euro (exercici 4).</li>
    <li>Nivells alts: diu per què 1/4 no és 0,4 (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 5 · De la fracció al decimal", """  FITXA · Unitat 5 · Decimals i arrel quadrada · De la fracció al decimal
  La quarta fitxa de la unitat 5. Adapta l'activitat 4 de la situació: una fracció
  es passa a decimal al quadrat de 100 (1/4 són 25 quadrets, 0,25), i al revés
  (0,3 són 3 columnes, 3/10). Només decimals exactes. Els casos són els de la
  tasca 21 de la caixa (regla 8).

  La regla trencada és posar el de baix després de la coma (1/4 = 0,4): en Pol,
  pàgina 4. Les igualtats falses van dins de .revisa.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud5-fraccions.html")
