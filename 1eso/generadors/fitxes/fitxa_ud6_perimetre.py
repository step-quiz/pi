#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud6-perimetre.html: el perímetre (unitat 6, fitxa 4).

Adapta l'activitat de perímetres de la situació «Sentit espacial» (el llibre, UD7, activitat 5).
El perímetre és comptar els costats de quadret de la vora; l'àrea (unitat 3) és comptar els quadrets
de dins. Sense quadrícula, el perímetre és la suma dels costats, i en un polígon regular, el costat
per quants costats té (la targeta). Els casos són els del llibre (l'octàgon de 4 cm, el triangle
equilàter de 9, la figura en forma d'L, l'error de la Carlota: el rectangle de 5 per 3 amb un
perímetre de 15) i els de la tasca 25 de la caixa.

La regla trencada (regla G): donar l'àrea en lloc del perímetre (pàgina 4).
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(AQUI, "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(AQUI, "peces_ud2.py"), encoding="utf-8").read())
exec(open(os.path.join(AQUI, "peces_fraccions.py"), encoding="utf-8").read())
exec(open(os.path.join(AQUI, "peces_geo.py"), encoding="utf-8").read())

pagines = []
pagina = fes_pagina(pagines, "Unitat 6 · El perímetre · pàgina")
per = lambda f, c: 2 * (f + c)
suma = lambda f, c: f"{c} + {f} + {c} + {f} = {per(f, c)}"
L = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]               # la figura en forma d'L

# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>el geoplà</b>. Fer un rectangle amb una goma i resseguir-ne la vora amb el dit, comptant els costats.</div>
  <h1>El perímetre</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:.8rem">
{figura_quadrets(rectangle_cel(3, 4), 0.95, "Un rectangle de 3 files de 4 quadrets, amb la vora gruixuda", rotuls=True).svg()}
  </div>
  <table style="margin-top:.4rem">
    <tr class="resolt"><td class="esq">Quants costats de quadret té la vora?</td><td style="width:6.6cm">{ms(suma(3, 4))}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets hi ha a dins?</td><td>{ms("3 · 4 = 12")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">La vora és el <b>perímetre</b>: 14 costats de quadret.</p>
    <p style="margin:0">Els quadrets de dins són l'<b>àrea</b>: 12 quadrets.</p>
  </div>''')

# ===================================================================== pàgina 2: compta la vora
E1 = [("a", rectangle_cel(2, 5), (2, 5), True), ("b", rectangle_cel(3, 3), (3, 3), False),
      ("c", rectangle_cel(1, 6), (1, 6), False), ("d", L, None, False)]
it = []
for l, cel, fc, r in E1:
    dib = figura_quadrets(cel, 0.55, f"Apartat {l}: una figura de quadrets amb la vora gruixuda", rotuls=bool(fc))
    res = ms(suma(*fc)) if r else buit()
    it.append(caixa(f'''      <p class="apartat" style="margin:0">{l})</p>
      <div style="display:flex;justify-content:center">{dib.svg("")}</div>
      <p class="frase" style="margin:.1rem 0 0;font-size:15pt">Perímetre: {res}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Compta els costats de quadret de la vora. Escriu el perímetre.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Posa el dit a una cantonada i dona tota la volta, comptant.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>''')


# ===================================================================== pàgina 3: sense quadrícula
E2 = [("a", "Un quadrat de 5 cm de costat", poligon_d([(0, 0), (1.8, 0), (1.8, 1.8), (0, 1.8)], "Un quadrat de 5 cm de costat", fons=F2), "5 + 5 + 5 + 5 = 20 cm", True),
      ("b", "Un rectangle de 6 cm i 3 cm", poligon_d([(0, 0), (2.8, 0), (2.8, 1.4), (0, 1.4)], "Un rectangle de 6 cm i 3 cm", fons=F2), "", False),
      ("c", "Un triangle equilàter de 9 cm de costat", poligon_d(regular(3, 1.2), "Un triangle equilàter de 9 cm de costat", fons=F2), "", False),
      ("d", "Un octàgon regular de 4 cm de costat", poligon_d(regular(8, 1.1), "Un octàgon regular de 4 cm de costat", fons=F2), "", False)]
it = []
for l, t, dib, res, r in E2:
    it.append(caixa(f'''      <p style="margin:0 0 .1rem"><span class="apartat">{l})</span> {t}</p>
      <div style="display:flex;gap:.5cm;align-items:center">
        <div style="width:3cm;display:flex;justify-content:center">{dib.svg("")}</div>
        <p class="frase" style="margin:0;font-size:15pt">{ms(res) if r else buit() + " cm"}</p>
      </div>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Suma els costats. Escriu el perímetre.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Si tots els costats són iguals, es pot multiplicar. Per exemple, 8 costats de 4 cm: 8 · 4.</p></div>
{chr(10).join(it)}
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
E3 = [("a", 3, 5, 15, True), ("b", 2, 4, 8, False), ("c", 4, 4, 16, False), ("d", 1, 5, 5, False)]
it = []
for l, fi, co, diu, r in E3:
    bo = per(fi, co) == diu
    dib = figura_quadrets(rectangle_cel(fi, co), 0.45, f"Apartat {l}: un rectangle de {fi} files de {co} quadrets", rotuls=True)
    it.append(caixa(f'''      <p style="margin:0 0 .1rem;font-size:15pt;font-weight:700"><span class="apartat">{l})</span> La Carlota diu: el perímetre és {diu}.</p>
      <div style="display:flex;gap:.5cm;align-items:center">
        <div>{dib.svg("")}</div>
        <div>
          <p style="margin:0;font-size:15pt">Té raó?</p>
          {tria(["Sí", "No"], ("Sí" if bo else "No") if r else None, mida="14pt", ample="2.2cm", columna=True)}
        </div>
      </div>
      <p class="frase" style="margin:0;font-size:15pt">El perímetre és {ms(str(per(fi, co))) if r else buit_curt()}</p>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">La Carlota compta els quadrets de dins. Té raó? Compta la vora.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">El perímetre és la vora, no els quadrets de dins.</p>
    <p style="margin:.2rem 0 0">Els quadrets de dins són l'àrea.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida
V = [("a", "Un hort de 6 m per 4 m. Quants metres de tanca calen?", "6 + 4 + 6 + 4 = 20 m", True),
     ("b", "Un marc de foto de 5 cm per 3 cm. Quants centímetres fa la vora?", "", False),
     ("c", "Una pista quadrada de 9 m de costat. Quants metres fa una volta?", "", False)]
it = []
for l, t, res, r in V:
    it.append(caixa(f'''      <p style="margin:0 0 .15rem"><span class="apartat">{l})</span> {t}</p>
      <p class="frase" style="margin:0">{ms(res) if r else buit()}</p>''', r, ".3rem"))
iguals = "".join(f'''<div style="text-align:center"><div>{figura_quadrets(rectangle_cel(f, c), 0.45, f"Un rectangle de {f} per {c}").svg("")}</div>
        <p class="frase" style="margin:.1rem 0 0;font-size:14pt;line-height:1.8">{f} per {c}: {buit_curt()}</p></div>''' for f, c in [(1, 12), (2, 6), (3, 4)])
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Calcula el perímetre.</div></div>
{chr(10).join(it)}
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Els tres rectangles tenen 12 quadrets. Escriu el perímetre de cada un.</div></div>
    <div style="display:flex;gap:.6cm;align-items:flex-end;justify-content:center;flex-wrap:wrap">{iguals}</div>
    <p class="frase" style="margin:.2rem 0 0">El de perímetre més petit és el de {buit_curt()} per {buit_curt()}.</p>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 6 · El perímetre · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> El perímetre és comptar els costats de quadret de la vora; l'àrea, de la
    unitat 3, és comptar els quadrets de dins. Al rectangle, la vora és dalt, dreta, baix i esquerra:
    4 + 3 + 4 + 3. Sense quadrícula, es sumen els costats; si són tots iguals, es multiplica amb la
    targeta. És la tasca 25 de la caixa.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb el geoplà: un rectangle amb una goma, i resseguir la vora amb el dit comptant els
  costats d'un clau a l'altre. Després, comptar els quadrets de dins: són dues coses diferents.</p>
  <h3>1. Compta la vora</h3>
  <p>b) 3 + 3 + 3 + 3 = 12. c) 6 + 1 + 6 + 1 = 14. d) 12: la figura en forma d'L té el mateix perímetre
  que el quadrat de 3 per 3, encara que té menys quadrets (el cas del llibre). <b>Error típic:</b>
  comptar dues vegades els costats de les cantonades.</p>
  <h3>2. Sense quadrícula</h3>
  <p>b) 6 + 3 + 6 + 3 = 18 cm. c) 9 + 9 + 9 = 27 cm (3 · 9). d) 8 · 4 = 32 cm (els casos del llibre).</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>3. La Carlota · la regla trencada</h3>
  <p>b) No: 12. c) Sí: 16 (al quadrat de 4 per 4, el perímetre i l'àrea fan 16, per casualitat).
  d) No: 12. <b>Error típic:</b> donar l'àrea en lloc del perímetre, com la Carlota del llibre. És la
  regla trencada d'aquesta fitxa. No l'expliqueu: que ressegueixi la vora amb el dit. L'apartat c és a
  posta. <b>Compta per als nivells alts, no per al mínim.</b></p>
  <h3>4 i 5. A la vida de cada dia</h3>
  <p>4b) 5 + 3 + 5 + 3 = 16 cm. 4c) 9 · 4 = 36 m. 5) 1 per 12: 26; 2 per 6: 16; 3 per 4: 14. El de perímetre
  més petit és el de 3 per 4: tenen la mateixa àrea i perímetres diferents. <b>L'exercici 5 compta per
  als nivells alts</b>: es pot fer comptant la vora.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=25</b> (25.1 Perímetre i
  àrea; 25.2 Quin és el perímetre?). La 25.2 dona un codi de verificació; les respostes falses són la de
  la Carlota (l'àrea) i sumar només dos costats. L'exemple de la fitxa és el de la caixa: 3 per 4.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta «Formes» al davant. Els criteris de la SA del grup (1.1, 3.1, 5.1, 6.1, 7.1 i
  9.1) són de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb el geoplà, ressegueix la vora d'un rectangle i en compta els costats.</li>
    <li>Compta el perímetre d'una figura de quadrets (exercici 1).</li>
    <li>Calcula el perímetre sumant els costats, o multiplicant si són iguals (exercicis 2 i 4).</li>
    <li>Nivells alts: distingeix el perímetre de l'àrea (exercicis 3 i 5).</li>
  </ul>
</div>''')

document("Unitat 6 · El perímetre", """  FITXA · Unitat 6 · Sentit espacial · El perímetre
  La quarta fitxa de la unitat 6. Adapta l'activitat de perímetres (el llibre, UD7,
  activitat 5): el perímetre és la vora; l'àrea, els quadrets de dins. Els casos són
  els del llibre i els de la tasca 25 de la caixa (regla 8).

  La regla trencada és donar l'àrea en lloc del perímetre: la Carlota, pàgina 4.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud6-perimetre.html")
