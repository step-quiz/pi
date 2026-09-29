#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud4-percentatges.html: els percentatges (unitat 4, fitxa 3).
Adapta l'activitat 7 de la situació «És gran l'ou del kiwi?»."""
import os
import sys
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_ud2.py"), encoding="utf-8").read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_fraccions.py"), encoding="utf-8").read())
pagines = []
pagina = fes_pagina(pagines, "Unitat 4 · Percentatges · pàgina")

# El percentatge → la fracció coneguda (unitat 3, denominador fins a 12), com a la caixa d'eines.
FRAC_PCT = {10: (1, 10), 20: (1, 5), 25: (1, 4), 50: (1, 2), 75: (3, 4)}


def percentatge(p, m=0.5):
    """La graella de 100 amb els primers `p` quadrets pintats (imprès)."""
    return graella100(lambda n: "imprès" if n <= p else None, f"{p} quadrets pintats de 100", m=m)


# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>la graella de 100</b>. Pintar-ne 25 quadrets i comptar-los.</div>
  <h1>Els percentatges</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:1rem;width:7cm;margin-left:auto;margin-right:auto">
{percentatge(25, m=0.68).svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.5rem 0 .8rem">Són 25 quadrets pintats de 100.</p>
  <table>
    <tr class="resolt"><td class="esq">Quants quadrets hi ha pintats?</td><td style="width:4.4cm">{ms("25")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">25 quadrets pintats de 100 és el 25%.</p>
    <p style="margin:.2rem 0;font-size:30pt;font-weight:800">25%</p>
    <p style="margin:0">El 25% és el mateix que {fr(1, 4, "17pt")}.</p>
  </div>''')

# ===================================================================== pàgina 2: quants quadrets és
E1 = [("a", 50, True), ("b", 10, False), ("c", 75, False), ("d", 20, False)]
it = []
for l, p, r in E1:
    cos = percentatge(p)
    resultat = ms(str(p)) if r else buit_curt()
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span> El {p}%. Pinta els quadrets.</p>
      <div style="width:5.4cm">{cos.svg("")}</div>
      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">Hi ha {resultat} quadrets pintats.</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Pinta els quadrets que et diu el percentatge. Compta'ls.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">El percentatge diu quants quadrets de 100 es pinten.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 3: quin percentatge és
E2 = [("a", 50, True), ("b", 75, False), ("c", 10, False), ("d", 20, False)]
it = []
for l, p, r in E2:
    cos = percentatge(p)
    resultat = ms(f"{p} %") if r else buit_curt()
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span> Compta els quadrets pintats.</p>
      <div style="width:5.4cm">{cos.svg("")}</div>
      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">És el {resultat}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Compta els quadrets pintats. Escriu quin percentatge és.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 4: percentatge i fracció, i la regla trencada
E3 = [("a", 50, 1, 2, True), ("b", 25, 1, 4, False), ("c", 75, 3, 4, False)]
it = []
for l, p, n, d, r in E3:
    fresult = fr(n, d, ma=True) if r else fr_buit("13pt")
    it.append(caixa(f'''      <p style="margin:0;font-size:16pt;font-weight:700"><span class="apartat">{l})</span> El {p}%, quina fracció és?</p>
      <p class="frase" style="margin:.15rem 0 0">{p}% = {fresult}</p>''', r, ".25rem"))
E4 = [("a", 25, False, True), ("b", 100, True, False)]
it2 = []
for l, p, bo, r in E4:
    cos = percentatge(p, m=0.42)
    bona = ("Sí" if bo else "No") if r else None
    it2.append(caixa(f'''      <p style="margin:0 0 .1rem;font-size:15pt;font-weight:700"><span class="apartat">{l})</span> És el 100%?</p>
      <div style="width:4.6cm">{cos.svg("")}</div>
      {tria(["Sí", "No"], bona, mida="14pt", ample="2.1cm")}''', r, ".2rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Escriu la fracció de cada percentatge. Mira la targeta.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">És el 100%? Marca la resposta. Mira si estan pintats tots els quadrets.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{chr(10).join(it2)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">El 100% és quan estan pintats tots els quadrets.</p>
    <p style="margin:.2rem 0 0">Si en falta algun de pintar, no és el 100%.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
V = [("a", "D'una classe de 100 alumnes, en falten 25 avui.", 25, True),
     ("b", "En una botiga, el 20% dels productes són rebaixats.", 20, False)]
it = []
for l, t_, p, r in V:
    resultat = ms(f"{p} %") if r else buit_curt()
    it.append(caixa(f'''      <p style="margin:0 0 .2rem"><span class="apartat">{l})</span> {t_}</p>
      <p class="frase" style="margin:0">Percentatge: {resultat}</p>''', r, ".3rem"))
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Digues el percentatge de cada situació.</div></div>
{chr(10).join(it)}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 4 · Els percentatges · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Un percentatge és quants quadrets de cada 100: el 25% és 25 quadrets
    pintats de 100. Els percentatges habituals es relacionen amb la fracció que ja es coneix: 50% és
    1/2, 25% és 1/4, 75% és 3/4, 20% és 1/5 i 10% és 1/10. Els casos són els de la tasca 16 de la
    caixa.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb la graella de 100: pintar-ne 25 quadrets i comptar-los. És l'exemple de la
  pàgina 1: 25 quadrets pintats de 100 és el 25%.</p>
  <h3>1. Quants quadrets és</h3>
  <p>b) 10; c) 75; d) 20. El percentatge diu directament quants quadrets es pinten, dels primers en
  endavant.</p>
  <h3>2. Quin percentatge és</h3>
  <p>b) 75%; c) 10%; d) 20%. Es compten els quadrets pintats, un per un si cal.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>3. Percentatge i fracció</h3>
  <p>b) 1/4; c) 3/4. Són les cinc fraccions de la targeta que corresponen als percentatges
  habituals.</p>
  <h3>4. És el 100%?</h3>
  <p>b) Sí. <b>Error típic:</b> dir que el 25% (apartat a) també és el 100% perquè «hi ha molts
  quadrets pintats», sense comptar-los. És la regla trencada d'aquesta fitxa. No l'expliqueu: que
  compti si li falta cap quadret per pintar.</p>
  <h3>5. A la vida de cada dia</h3>
  <p>b) 20%.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=16</b> (16.1 Pinta el
  percentatge; 16.2 Quin percentatge és?). La 16.2 dona un codi de verificació; les respostes
  falses són confondre el que hi ha amb el que falta, i dir sempre el 100%.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta de les fraccions al davant. Els criteris de la SA del grup (1.3, 2.1, 5.1
  i 6.1) són de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb la graella de 100, pinta un percentatge i el compta.</li>
    <li>Diu quin percentatge és, comptant els quadrets pintats (exercici 2).</li>
    <li>Relaciona un percentatge amb la seva fracció coneguda (exercici 3).</li>
    <li>Nivells alts: diu per què un percentatge no és el 100% si en falta algun (exercici 4).</li>
  </ul>
</div>''')

document("Unitat 4 · Els percentatges", """  FITXA · Unitat 4 · És gran l'ou del kiwi? · Els percentatges
  La tercera fitxa de la unitat 4. Adapta l'activitat 7 de la situació: un
  percentatge és quants quadrets de cada 100, i els percentatges habituals es
  relacionen amb la fracció que ja es coneix (50%=1/2, 25%=1/4, 75%=3/4,
  20%=1/5, 10%=1/10). Els casos són els de la tasca 16 de la caixa (regla 8).

  La regla trencada és confondre un percentatge parcial amb el 100% sense
  comptar els quadrets (exercici 4).""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud4-percentatges.html")
