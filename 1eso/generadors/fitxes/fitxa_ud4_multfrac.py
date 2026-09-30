#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud4-multfrac.html: multiplicar fraccions (unitat 4, fitxa 2).
Adapta les activitats 4 i 5 de la situació «És gran l'ou del kiwi?». Només amb
numerador 1 a cada fracció, i el resultat sempre amb denominador fins a 12
(decisió ja presa a la unitat 3): dividir fraccions queda fora (no té una
imatge senzilla amb quadrets)."""
import os
import sys
from peces_comunes import *  # noqa: F401,F403
from peces_ud2 import *  # noqa: F401,F403
from peces_fraccions import *  # noqa: F401,F403
pagines = []
pagina = fes_pagina(pagines, "Unitat 4 · Multiplicar fraccions · pàgina")


def tros_de_tros(d1, d2, m=None):
    """El rectangle de dues fraccions: d1 columnes (la primera, horitzontal) per
    d2 files (la segona, vertical). La primera columna es pinta d'un gris (la
    primera fracció) i la primera fila, d'un altre gris més fosc (la segona);
    la cantonada, on totes dues coincideixen, és el resultat, i queda pintada
    del gris més fosc I resseguida amb un traç gruixut, perquè el color no
    sigui l'única diferència. Sense `m`, la mida s'ajusta perquè el rectangle
    no passi de 3.4 cm d'alt ni de 6.4 cm d'ample."""
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
    # El resultat: la cantonada, ja pintada del gris fosc, es resseguix amb un traç gruixut.
    D.cru(f'<rect x="{D.px(esq + 0.05)}" y="{D.px(dalt + 0.05)}" width="{D.px(m - 0.1)}" height="{D.px(m - 0.1)}" '
          f'rx="{D.px(0.08)}" fill="none" stroke="{MS}" stroke-width="2.6"/>')
    D.clau_dalt(esq, esq + d1 * m, dalt, f"1 de {d1}")
    D.clau_esq(esq, dalt, dalt + d2 * m, f"1 de {d2}")
    return D


# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>paper quadriculat</b>. Pintar una columna de 2 i, a sobre, ratllar una fila de 4: el quadret de la cantonada és el tros de tros.</div>
  <h1>Multiplicar fraccions</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:1rem;width:7cm;margin-left:auto;margin-right:auto">
{tros_de_tros(2, 4, m=1.1).svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.5rem 0 .8rem">És un rectangle partit en 2 columnes i en 4 files. El quadret de la cantonada és pintat de les dues maneres.</p>
  <table>
    <tr class="resolt"><td class="esq">Quants trossos petits hi ha en total?</td><td style="width:4.4cm">{ms("8")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">Partir en 2 columnes i en 4 files fa 2 · 4 = 8 trossos petits.</p>
    <p style="margin:.2rem 0">{fr(1, 2, "30pt")} de {fr(1, 4, "30pt")} <b>és</b> {fr(1, 8, "30pt")}</p>
    <p style="margin:0;font-weight:700">Multiplicar fraccions és fer un tros de tros.</p>
  </div>''')

# ===================================================================== pàgina 2: el tros de tros
E1 = [("a", 2, 3, True), ("b", 3, 2, False), ("c", 2, 5, False), ("d", 3, 3, False)]
it = []
for l, d1, d2, r in E1:
    dr = d1 * d2
    cos = tros_de_tros(d1, d2)
    resultat = ms(str(dr)) if r else buit_curt()
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span> {fr(1, d1, "15pt")} de {fr(1, d2, "15pt")}. Parteix en {d1} columnes i en {d2} files.</p>
      <div style="width:{d1 * 0.85 + 1.2:.1f}cm">{cos.svg("")}</div>
      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">En total hi ha {resultat} trossos petits.</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Parteix el rectangle en columnes i en files. Compta els trossos petits.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Multiplica els dos denominadors. 2 columnes i 3 files fan 2 · 3 = 6.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 3: escriu el resultat
E2 = [("a", 3, 4, True), ("b", 2, 4, False), ("c", 4, 2, False), ("d", 2, 6, False)]
it = []
for l, d1, d2, r in E2:
    dr = d1 * d2
    cos = tros_de_tros(d1, d2)
    fresult = fr(1, dr, ma=True) if r else fr_buit("13pt")
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span> {fr(1, d1, "15pt")} de {fr(1, d2, "15pt")}</p>
      <div style="width:{d1 * 0.85 + 1.2:.1f}cm">{cos.svg("")}</div>
      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">{d1} · {d2} = {dr if r else buit_curt()}: {fresult}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Multiplica els dos denominadors. Escriu el resultat com a fracció.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
E3 = [("a", 2, 3, True), ("b", 3, 4, False), ("c", 2, 5, False)]
it = []
for l, d1, d2, r in E3:
    dr_bo = d1 * d2
    dr_mal = d1 + d2
    opcions_txt = [f"1 de {dr_mal}", f"1 de {dr_bo}"]
    bona = f"1 de {dr_bo}" if r else None
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span> {fr(1, d1, "15pt")} de {fr(1, d2, "15pt")}. Quin és el resultat?</p>
      {tria(opcions_txt, bona, mida="14pt", ample="3.6cm")}''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Quin és el resultat? Marca la resposta. Compta els trossos petits si cal.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:.3rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Els denominadors no se sumen: es multipliquen.</p>
    <p style="margin:.2rem 0 0">{fr(1, 2, "15pt")} de {fr(1, 3, "15pt")} no és 1 de 5. Compta els trossos: 2 · 3 = 6.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
V = [("a", f"Menges {fr(1, 2, '14pt')} d'una pizza. D'aquest tros, en menges {fr(1, 3, '14pt')}.", 2, 3, True),
     ("b", f"Un hort té {fr(1, 4, '14pt')} de flors. D'aquest tros, {fr(1, 2, '14pt')} són roses.", 4, 2, False)]
it = []
for l, t_, d1, d2, r in V:
    dr = d1 * d2
    frase = ms(f"1 de {dr}") if r else fr_buit("13pt")
    it.append(caixa(f'''      <p style="margin:0 0 .2rem"><span class="apartat">{l})</span> {t_}</p>
      <p class="frase" style="margin:0">{d1} · {d2} = {dr if r else buit_curt()}: {frase}</p>''', r, ".3rem"))
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Calcula quin tros és, en total. Mira la targeta de les taules.</div></div>
{chr(10).join(it)}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 4 · Multiplicar fraccions · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Multiplicar dues fraccions és fer un tros de tros: el rectangle es
    parteix en columnes per a la primera fracció i en files per a la segona, i el resultat és el
    tros que és a la vegada de les dues. Només es fa servir numerador 1 a cada fracció, i el
    resultat mai no passa de denominador 12 (decisió ja presa a la unitat 3): els casos són els de
    la tasca 15 de la caixa. Dividir fraccions (activitat 6 del grup) queda fora d'aquesta fitxa:
    no té una imatge senzilla amb quadrets.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb paper quadriculat: pintar una columna de 2 i, a sobre, ratllar una fila de 4.
  El quadret de la cantonada, pintat de les dues maneres, és el tros de tros. És l'exemple de la
  pàgina 1: 1/2 de 1/4 és 1/8.</p>
  <h3>1. El tros de tros</h3>
  <p>b) 6; c) 10; d) 9. Sempre es multiplica: columnes per files.</p>
  <h3>2. Escriu el resultat</h3>
  <p>b) 2 · 4 = 8: 1/8; c) 4 · 2 = 8: 1/8; d) 2 · 6 = 12: 1/12. El 1/12 és el cas més gran que es
  fa servir en aquesta unitat: no se'n passa mai, com a la unitat 3.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>3. Quin és el resultat?</h3>
  <p>b) 1 de 12; c) 1 de 10. <b>Error típic:</b> sumar els denominadors (1/2 de 1/3 fet «1 de 5»),
  que és la regla trencada d'aquesta fitxa. No l'expliqueu: que compti els trossos petits del
  dibuix, un per un, i vegi que en surten 6, no 5.</p>
  <h3>4. A la vida de cada dia</h3>
  <p>b) 4 · 2 = 8: 1/8.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=15</b> (15.1 El tros de
  tros; 15.2 Quin tros és?). La 15.2 dona un codi de verificació; les respostes falses són sumar
  els denominadors, i un dels denominadors sol.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta de les taules al davant. Els criteris de la SA del grup (1.3, 2.1, 5.1 i
  6.1) són de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb paper quadriculat, fa un tros de tros pintant columnes i files.</li>
    <li>Compta els trossos petits d'un tros de tros (exercici 1).</li>
    <li>Escriu el resultat com a fracció, multiplicant els denominadors (exercici 2).</li>
    <li>Nivells alts: diu per què els denominadors no se sumen (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 4 · Multiplicar fraccions", """  FITXA · Unitat 4 · És gran l'ou del kiwi? · Multiplicar fraccions
  La segona fitxa de la unitat 4. Adapta les activitats 4 i 5 de la situació:
  multiplicar dues fraccions és fer un tros de tros del mateix rectangle,
  partit en columnes i en files alhora. Només amb numerador 1, i el resultat
  mai no passa de denominador 12 (decisió ja presa a la unitat 3). Dividir
  fraccions (activitat 6) queda fora: no té una imatge senzilla amb quadrets.
  Els casos són els de la tasca 15 de la caixa (regla 8).

  La regla trencada és sumar els denominadors en lloc de multiplicar-los
  (exercici 3).""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud4-multfrac.html")
