#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud3-mapes.html: quants km²? (unitat 3, l'última fitxa en ordre).
Adapta les activitats 8 i 9 de la situació «Com és de gran Gaza?»: els km² de Barcelona i de
Gaza en un mapa amb quadrícula, amb el contorn esquemàtic (decisió del docent del 26/9/2026).
Cada quadret és 1 km², i els quadrets es llegeixen en centenes, desenes i unitats (unitat 1)."""
import os
import sys
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_ud2.py"), encoding="utf-8").read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_fraccions.py"), encoding="utf-8").read())
pagines = []
pagina = fes_pagina(pagines, "Unitat 3 · Km² · pàgina")


def mapa(cols, extra, m, aria):
    """Un territori de 10 files i `cols` columnes, i `extra` quadrets més en una columna a la
    dreta, a baix. Una ratlla més gruixuda cada 10 columnes: els quadrats de 100."""
    W, H = (cols + 3) * m, 12 * m
    D = Dibuix(W + 0.1, H + 0.1, aria)
    for fi in range(12):
        for co in range(cols + 3):
            dins = 1 <= fi <= 10 and (1 <= co <= cols or (co == cols + 1 and fi > 10 - extra))
            D.cru(f'<rect x="{D.px(0.05 + co * m)}" y="{D.px(0.05 + fi * m)}" width="{D.px(m)}" height="{D.px(m)}" '
                  f'fill="{F3 if dins else "#fff"}" stroke="{G2 if dins else G3}" stroke-width="{1.1 if dins else 0.7}"/>')
    for k in range(0, cols + 1, 10):
        x = 0.05 + (k + 1) * m
        D.cru(f'<line x1="{D.px(x)}" y1="{D.px(0.05 + m)}" x2="{D.px(x)}" y2="{D.px(0.05 + 11 * m)}" stroke="{NEGRE}" stroke-width="3"/>')
    D.cru(f'<rect x="{D.px(0.05 + m)}" y="{D.px(0.05 + m)}" width="{D.px(cols * m)}" height="{D.px(10 * m)}" fill="none" stroke="{NEGRE}" stroke-width="3"/>')
    return D


# ===================================================================== pàgina 1: Barcelona
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>la graella de 100</b> de la unitat 2. És un quadrat de 10 per 10: 100 quadrets.</div>
  <h1>Quants km²?</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div style="width:6.2cm;margin:.6rem auto 0">{mapa(10, 1, 0.47, "Barcelona dibuixada amb quadrets: un quadrat de 10 per 10 i un quadret més").svg("")}</div>
  <p style="text-align:center;margin:0;font-size:13pt;color:var(--gris-2)">Barcelona, dibuixada amb quadrets. És un esquema: no és la forma de debò.</p>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .6rem">Cada quadret és 1 km².</p>
  <table>
    <tr class="resolt"><td class="esq">Quants quadrets té el quadrat de 10 per 10?</td><td style="width:4.2cm">{ms("100")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets més hi ha?</td><td>{ms("1")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">1 centena, 0 desenes i 1 unitat: 101.</p>
    <p style="margin:.2rem 0 0;font-size:20pt;font-weight:800">Barcelona fa uns 101 km².</p>
  </div>''')

# ===================================================================== pàgina 2: Gaza (la vida)
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div style="width:17.8cm">{mapa(36, 5, 0.45, "Gaza dibuixada amb quadrets: una franja de 10 files i 36 columnes, i 5 quadrets més").svg("")}</div>
  <p style="text-align:center;margin:0;font-size:13pt;color:var(--gris-2)">Gaza, dibuixada amb quadrets. És un esquema: no és la forma de debò. Cada quadret és 1 km².</p>
  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Quants km² fa Gaza? Compta per quadrats de 100, columnes de 10 i quadrets solts.</div></div>
    <table style="margin-top:.2rem">
      <tr class="resolt"><td class="esq"><span class="apartat">a)</span> Quants quadrats de 10 per 10 hi ha?</td><td style="width:3.6cm">{ms("3")}</td></tr>
      <tr><td class="esq"><span class="apartat">b)</span> Quantes columnes de 10 hi ha, a més?</td><td class="omplir"></td></tr>
      <tr><td class="esq"><span class="apartat">c)</span> Quants quadrets solts hi ha?</td><td class="omplir"></td></tr>
      <tr><td class="esq"><span class="apartat">d)</span> Quants km² fa Gaza?</td><td class="omplir"></td></tr>
    </table>
  </div>''', classe="full vida")

# ===================================================================== pàgina 3: compara
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Compara Gaza i Barcelona. Mira els dos dibuixos.</div></div>
{caixa(f"""      <p class="frase" style="margin:0"><span class="apartat">a)</span> Quina és més gran? {ms("Gaza")}</p>""", True, ".2rem")}
{caixa(f"""      <p class="frase" style="margin:0"><span class="apartat">b)</span> Quants quadrats de 100 hi ha a Gaza? {buit_curt()} I a Barcelona? {buit_curt()}</p>""", False, ".2rem")}
{caixa(f"""      <p style="margin:0;font-size:15pt"><span class="apartat">c)</span> Gaza és estreta. Vol dir que és petita?</p>
      {tria(["Sí", "No"], mida="14pt", ample="2.4cm")}""", False, ".2rem")}
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Estret no vol dir petit. L'àrea es compta amb quadrets.</p>
    <p style="margin:.2rem 0 0">Gaza és estreta, però fa més de 3 vegades Barcelona.</p>
  </div>''')

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 3 · Quants km²? · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> És l'última fitxa de la unitat 3, la de la tasca final de la programació
    («Quants km² medeix Barcelona?» i «Com és de gran Gaza?»). Els dos contorns són esquemes, i així
    ho diu la fitxa: no és la forma de debò, sinó la mateixa àrea feta amb quadrets d'1 km². Les dades
    són aproximades: Barcelona fa uns 101 km², i Gaza, uns 365 km². La fitxa només porta les dades
    de mesura; el context de la situació d'aprenentatge es treballa a l'aula, amb el docent.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>La graella de 100 de la unitat 2: és un quadrat de 10 per 10, i per tant 100 km² si cada quadret
  és 1 km². Els quadrets es llegeixen com els blocs de la unitat 1: quadrats de 100, columnes de 10
  i quadrets solts.</p>
  <h3>1. Els km² de Gaza</h3>
  <p>b) 6 columnes de 10; c) 5 quadrets solts; d) 365 km²: 3 centenes, 6 desenes i 5 unitats.</p>
  <h3>2. Compara</h3>
  <p>b) 3 a Gaza, 1 a Barcelona. c) No. <b>Error típic:</b> pensar que una franja estreta és petita.
  És la regla trencada d'aquesta fitxa. No l'expliqueu: que compti els quadrats de 100 de cadascuna.
  Nivells alts: hi cap Barcelona més de 3 vegades, però no 4, perquè 4 · 100 = 400.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Els criteris de la SA del grup (1.2, 5.2, 6.1 i 9.1) són de referència: l'avaluació es fa amb
  els criteris del PI.</p>
  <ul>
    <li>Llegeix una àrea en quadrats de 100, columnes de 10 i quadrets solts (exercici 1).</li>
    <li>Compara dues àrees comptant quadrets, i no per la forma (exercici 2).</li>
  </ul>
</div>''')

document("Unitat 3 · Quants km²?", """  FITXA · Unitat 3 · Com és de gran Gaza? · Quants km²?
  L'última fitxa de la unitat 3 en l'ordre de la programació: activitats 8 i 9,
  la tasca final. Els km² de Barcelona (uns 101) i de Gaza (uns 365) en un mapa
  amb quadrícula i contorn esquemàtic (decisió del docent del 26/9/2026). Cada
  quadret és 1 km², i es compta per quadrats de 100, columnes de 10 i quadrets
  solts, com els blocs de la unitat 1. Només les dades de mesura.

  La regla trencada és «estret vol dir petit» (exercici 2).""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud3-mapes.html")
