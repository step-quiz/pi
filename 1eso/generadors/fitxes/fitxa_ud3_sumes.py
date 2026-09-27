#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud3-sumes.html: sumar i restar fraccions (unitat 3, fitxa 4).
Adapta les activitats Fraccions 7, 8 i 9 del grup, sempre amb el mateix denominador, i hi
afegeix el full que el docent va demanar el 26/9/2026: per què 1/2 + 1/4 no pot ser 2/6."""
import os
import sys
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_ud2.py"), encoding="utf-8").read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "peces_fraccions.py"), encoding="utf-8").read())
pagines = []
pagina = fes_pagina(pagines, "Unitat 3 · Sumes · pàgina")
op = lambda a, b, d, s="+": f"{fr(a, d)} {s} {fr(b, d)}"

# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>una tira de paper de 8 trossos</b>. Pintar-ne 3 amb un llapis i 2 amb un altre, i comptar-los tots.</div>
  <h1>Sumar i restar fraccions</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:1rem;width:10cm;margin-left:auto;margin-right:auto">
{tira(3, 8, "Un rectangle de 8 trossos: 3 pintats de gris clar i 2 de gris fosc", W=9.5, H=1.2, mes=2).svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.5rem 0 .8rem">Hi ha 3 trossos d'un gris i 2 d'un altre, al mateix rectangle.</p>
  <table>
    <tr class="resolt"><td class="esq">Quants trossos pintats hi ha en total?</td><td style="width:4cm">{ms("5")}</td></tr>
    <tr class="resolt"><td class="esq">Quants trossos té el rectangle?</td><td>{ms("8")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">Se sumen els de dalt: 3 + 2 = 5.</p>
    <p style="margin:0">El de baix no canvia: els trossos són els mateixos.</p>
    <p style="margin:.2rem 0">{fr(3, 8, "30pt")} + {fr(2, 8, "30pt")} = {fr(5, 8, "30pt")}</p>
  </div>''')

# ===================================================================== pàgina 2: pinta per sumar
E1 = [("a", 3, 2, 8, True), ("b", 1, 2, 4, False), ("c", 2, 1, 5, False), ("d", 3, 5, 7, False), ("e", 4, 3, 10, False)]
it = []
for l, a, b, d, r in E1:
    t = (tira(a, d, f"{a} de {d} i {b} més", W=7.4, H=0.75, mes=b, ma=True) if r
         else tira(a + b, d, f"Rectangles de {d} trossos, per pintar", W=7.4, H=0.75, buida=True))
    res = fr(a + b, d, ma=True) if r else fr_buit("13pt")
    it.append(caixa(f'''      <p class="frase" style="margin:0 0 .15rem"><span class="apartat">{l})</span> {op(a, b, d)} = {res}</p>
      <div style="width:7.6cm">{t.svg("")}</div>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Pinta per sumar. Després escriu el resultat.</div></div>
    <div class="avis puntejat" style="margin:.3rem 0 .5rem">Pinta la primera amb un llapis i la segona amb un altre. Si no hi caben, fes servir el segon rectangle.</div>
{chr(10).join(it)}
  </div>''')

# ===================================================================== pàgina 3: pinta per restar
E2 = [("a", 4, 1, 7, True), ("b", 5, 2, 6, False), ("c", 7, 3, 8, False), ("d", 9, 4, 12, False)]
it = []
for l, a, b, d, r in E2:
    t = tira(a, d, f"{a} trossos pintats de {d}" + (f", amb {b} de ratllats" if r else ""), W=7.4, H=0.8, treu=b if r else 0)
    res = fr(a - b, d, ma=True) if r else fr_buit("13pt")
    it.append(caixa(f'''      <p class="frase" style="margin:0 0 .15rem"><span class="apartat">{l})</span> {op(a, b, d, "−")} = {res}</p>
      <div style="width:7.6cm">{t.svg("")}</div>''', r, ".35rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Ratlla els trossos que treus. Després escriu el resultat.</div></div>
{chr(10).join(it)}
  </div>
  <div class="clau" style="margin-top:.5rem"><p style="margin:0">Quan restes, el de baix tampoc no canvia.</p></div>''')

# ===================================================================== pàgina 4: sense dibuix
E3 = [("a", 2, 5, 9, "+", True), ("b", 3, 4, 10, "+", False), ("c", 7, 2, 8, "−", False), ("d", 1, 4, 6, "+", False),
      ("e", 11, 5, 12, "−", False), ("f", 3, 4, 5, "+", False)]
f3 = "\n".join(f'''      <tr{' class="resolt"' if r else ''}><td class="apartat" style="font-size:16pt;white-space:nowrap">{l}) {op(a, b, d, s)} =</td>'''
               f'''<td style="text-align:center;height:1.7cm;width:3cm">{fr(a + b if s == "+" else a - b, d, ma=True) if r else fr_buit("13pt")}</td></tr>'''
               for l, a, b, d, s, r in E3)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Ara sense dibuix. Suma o resta els de dalt.</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">El de baix no canvia. Si dubtes, fes-ne el dibuix.</p></div>
    <table class="mini" style="margin-top:.2rem">
{f3}
    </table>
  </div>''')

# ===================================================================== pàgina 5: el full de 1/2 + 1/4
M = dict(W=7.8, H=0.62, meitat=True)
it4 = []
for l, text, bona_, r in [("a", f"{fr(1, 4)} + {fr(2, 4)} = {fr(3, 8)}", False, True),
                          ("b", f"{fr(1, 4)} + {fr(2, 4)} = {fr(3, 4)}", True, False),
                          ("c", f"{fr(2, 5)} + {fr(1, 5)} = {fr(3, 10)}", False, False)]:
    it4.append(caixa(f'''      <p class="frase" style="margin:0"><span class="apartat">{l})</span> <span class="revisa">{text}</span></p>
      {tria(["Bé", "Malament"], ("Bé" if bona_ else "Malament") if r else None, mida="14pt", ample="2.2cm", columna=True)}''', r, ".25rem"))
pagina(f'''  <h2>Per què {fr(1, 2, "15pt")} + {fr(1, 4, "15pt")} no pot ser mai {fr(2, 6, "15pt")}?</h2>
  <p style="margin:.2rem 0 .3rem">Hi ha qui suma els de dalt i els de baix: 1 + 1 = 2 i 2 + 4 = 6. Mira-ho amb el dibuix. La ratlla és la meitat del rectangle.</p>
  <div style="display:grid;grid-template-columns:2.2cm 1fr;gap:.3rem .4cm;align-items:center">
    <div>{fr(1, 2)}</div><div>{tira(1, 2, "La meitat del rectangle pintada", **M).svg("")}</div>
    <div>+ {fr(1, 4)}</div><div>{tira(1, 4, "Un quart del rectangle pintat", **M).svg("")}</div>
    <div>=</div><div>{tira(2, 4, "La meitat i un quart més: el tros passa de la ratlla", mes=1, **M).svg("")}</div>
  </div>
  <p style="margin:.3rem 0">Si a la meitat hi sumes un tros, el tros pintat passa de la ratlla. És més de la meitat.</p>
  <div style="display:grid;grid-template-columns:2.2cm 1fr;gap:.3rem .4cm;align-items:center">
    <div>{fr(2, 6)}</div><div>{tira(2, 6, "Dos sisens: el tros no arriba a la ratlla", **M).svg("")}</div>
  </div>
  <p style="margin:.3rem 0">I {fr(2, 6, "14pt")} no arriba a la ratlla: és menys de la meitat.</p>
  <div class="avis gruixut" style="text-align:center;margin:.3rem 0 .5rem">
    <p style="margin:0;font-weight:700">Sumant, no pots tenir menys del que tenies. Per això no pot ser {fr(2, 6, "14pt")}.</p>
    <p style="margin:.2rem 0 0">El de baix diu la mida dels trossos: no se suma. El dibuix diu que és {fr(3, 4, "14pt")}.</p>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Està bé? Marca la resposta.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:.2rem .4cm">
{chr(10).join(it4)}
    </div>
  </div>''')

# ===================================================================== pàgina 6: la vida
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Quina part se n'han menjat? Escriu la suma o la resta.</div></div>
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Una pizza de 8 trossos. Tu en menges 3 i la teva germana, 2.</p>
      <p class="frase" style="margin:0">{fr(3, 8, ma=True)} + {fr(2, 8, ma=True)} = {fr(5, 8, ma=True)} de pizza.</p>""", True)}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Un pastís de 6 trossos. Tu en menges 1 i un amic, 3.</p>
      <p class="frase" style="margin:0">{fr_buit("13pt")} + {fr_buit("13pt")} = {fr_buit("13pt")} de pastís.</p>""")}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">c)</span> Queden {fr(5, 6, "14pt")} del pastís, i se'n mengen {fr(2, 6, "14pt")}. Quant en queda?</p>
      <p class="frase" style="margin:0">{fr_buit("13pt")} − {fr_buit("13pt")} = {fr_buit("13pt")} de pastís.</p>""")}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 3 · Sumar i restar fraccions · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Sempre amb el mateix denominador (decisió del docent del 26/9/2026): se
    sumen o es resten els trossos pintats, i el de baix no canvia, perquè els trossos són els
    mateixos. Les sumes amb denominadors diferents del grup (activitats 10 a 12) queden fora; la
    pàgina 5 explica per què no se sumen els de baix. La caixa d'eines ho fa a la tasca 12.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb una tira de 8 trossos: pintar-ne 3 amb un llapis i 2 amb un altre. N'hi ha 5 de
  pintats, i la tira té encara 8 trossos.</p>
  <h3>1. Pinta per sumar</h3>
  <p>b) 3/4; c) 3/5; d) 8/7, que és més d'un rectangle (la de l'activitat Fraccions 7 del grup); e) 7/10.</p>
  <h3>2. Pinta per restar</h3>
  <p>b) 3/6; c) 4/8; d) 5/12. Es ratllen els últims trossos pintats, o els que vulgui: el que compta és quants.</p>
  <h3>3. Sense dibuix</h3>
  <p>b) 7/10; c) 5/8; d) 5/6; e) 6/12; f) 7/5. <b>Error típic:</b> sumar també els de baix.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>4. El full de 1/2 + 1/4 · la regla trencada</h3>
  <p>b) Bé; c) Malament: és 3/5. <b>Error típic:</b> sumar els de dalt i els de baix, que és
  la regla trencada d'aquesta fitxa. El full no fa servir el mínim comú múltiple: només compara
  amb la meitat. Si a mig rectangle hi afegeixes un tros, en tens més de la meitat, i 2/6 és un terç,
  menys de la meitat. La resposta bona, 3/4, surt del dibuix, sense cap regla nova.</p>
  <h3>5. A la vida de cada dia</h3>
  <p>b) 1/6 + 3/6 = 4/6. c) 5/6 − 2/6 = 3/6. Són els problemes de la pizza i del pastís de l'activitat
  Fraccions 8 del grup.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=12</b> (12.1 Suma i resta;
  12.2 Quant és?). La 12.2 dona un codi de verificació; una de les respostes falses és sumar els de
  baix. La 12.1 s'obre amb 3/8 + 2/8 = 5/8, com la pàgina 1.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb les dues targetes al davant. Els criteris de la SA del grup (1.2, 5.2, 6.1 i 9.1) són
  de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb una tira de paper, pinta una suma i diu el resultat (exercici 1).</li>
    <li>Ratlla una resta i diu el resultat (exercici 2).</li>
    <li>Suma i resta amb el mateix denominador, sense dibuix (exercici 3).</li>
    <li>Nivells alts: explica per què 1/2 + 1/4 no pot ser 2/6, amb el dibuix (pàgina 5).</li>
  </ul>
</div>''')

document("Unitat 3 · Sumar i restar fraccions", """  FITXA · Unitat 3 · Les fraccions · Sumar i restar
  La quarta fitxa de la unitat 3. Adapta les activitats Fraccions 7, 8 i 9 del
  grup, sempre amb el mateix denominador (decisió del docent del 26/9/2026), i
  hi afegeix el full que va demanar: per què 1/2 + 1/4 no pot ser 2/6, comparant
  amb la meitat del rectangle. Els casos són els de la tasca 12 de la caixa.

  La regla trencada és sumar els de dalt i els de baix (pàgina 5). Les sumes per
  revisar van dins de .revisa, perquè n'hi ha de falses a posta.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud3-sumes.html")
