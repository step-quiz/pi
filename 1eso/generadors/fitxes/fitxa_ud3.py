#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud3.html: què és una fracció (unitat 3, fitxa 1).
Adapta les activitats Fraccions 0 i 2 del grup."""
import os
import sys
from peces_comunes import *  # noqa: F401,F403
from peces_ud2 import *  # noqa: F401,F403
from peces_fraccions import *  # noqa: F401,F403
pagines = []
pagina = fes_pagina(pagines, "Unitat 3 · Fraccions · pàgina")

# ===================================================================== pàgina 1
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>tires de paper</b>. Doblegar una tira en 4 trossos iguals i pintar-ne 3. I tenir a mà la targeta de les fraccions.</div>
  <h1>Què és una fracció</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura neta" style="margin-top:1rem;width:10cm;margin-left:auto;margin-right:auto">
{tira(3, 4, "Un rectangle partit en 4 trossos iguals, amb 3 de pintats", W=9.5, H=1.3).svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.5rem 0 .8rem">És un rectangle partit en 4 trossos iguals. N'hi ha 3 de pintats.</p>
  <table>
    <tr class="resolt"><td class="esq">Quants trossos hi ha?</td><td style="width:4cm">{ms("4")}</td></tr>
    <tr class="resolt"><td class="esq">Quants n'hi ha de pintats?</td><td>{ms("3")}</td></tr>
  </table>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">3 trossos pintats de 4 s'escriu així:</p>
    <p style="margin:.2rem 0">{fr(3, 4, "40pt")}</p>
    <p style="margin:0">El de dalt és el <b>numerador</b>: els trossos pintats.</p>
    <p style="margin:0">El de baix és el <b>denominador</b>: tots els trossos.</p>
    <p style="margin:.2rem 0 0;font-weight:700">Es llegeix: tres quarts. Mira la targeta.</p>
  </div>''')

# ===================================================================== pàgina 2
E1 = [("a", 4, 9, True), ("b", 2, 5, False), ("c", 5, 8, False), ("d", 1, 3, False), ("e", 7, 10, False), ("f", 5, 6, False)]
it = []
for l, n, d, r in E1:
    f_ = fr(n, d, ma=True) if r else fr_buit()
    nm = ms(nom(n, d)) if r else '<u style="display:inline-block;min-width:4.2cm;padding:0"></u>'
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-weight:700"><span class="apartat">{l})</span></p>
      <div style="display:flex;gap:.6cm;align-items:center">
        <div style="flex:0 0 5.4cm">{tira(n, d, f"Un rectangle de {d} trossos, amb {n} de pintats", W=5.2, H=0.8).svg("")}</div>
        <div>{f_}</div>
      </div>
      <p class="frase" style="margin:.15rem 0 0;font-size:14.5pt">Es llegeix: {nm}</p>''', r))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Escriu la fracció de cada dibuix. Després escriu com es llegeix.</div></div>
    <div class="avis puntejat" style="margin:.3rem 0 .5rem">A dalt, els trossos pintats. A baix, tots els trossos.</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.2rem .6cm">
{chr(10).join(it)}
    </div>
  </div>''')

# ===================================================================== pàgina 3
E2 = [("a", 4, 9, True), ("b", 3, 4, False), ("c", 2, 3, False), ("d", 5, 8, False), ("e", 7, 10, False), ("f", 1, 6, False)]
it = []
for l, n, d, r in E2:
    t = tira(n, d, f"Un rectangle de {d} trossos" + (f", amb {n} pintats a mà" if r else ", per pintar"), W=7.2, H=0.9,
             ma=r, buida=not r)
    it.append(caixa(f'''      <div style="display:flex;gap:.6cm;align-items:center">
        <p style="margin:0;font-weight:700;min-width:2.4cm"><span class="apartat">{l})</span> {fr(n, d)}</p>
        <div style="flex:1">{t.svg("")}</div>
      </div>''', r, ".35rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Pinta la fracció. Compta els trossos.</div></div>
{chr(10).join(it)}
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
E3 = [("a", [0.12, 0.36, 0.7], 0, False, True), ("b", [0.25, 0.5, 0.75], 0, True, False),
      ("c", [0.2, 0.62], 1, False, False), ("d", [1 / 3, 2 / 3], 1, True, False)]
it = []
for l, talls, p, iguals, r in E3:
    n_trossos = len(talls) + 1
    bona = ("Sí" if iguals else "No") if r else None
    extra = (f'<p class="frase" style="margin:0;font-size:14.5pt">{ms("No")}: els trossos no són iguals.</p>' if r else "")
    it.append(caixa(f'''      <p style="margin:0;font-size:16pt;font-weight:700"><span class="apartat">{l})</span> És {fr(1, n_trossos)}?</p>
      <div style="width:7.2cm">{tira_talls(talls, p, f"Un rectangle partit en {n_trossos} trossos, amb un de pintat", W=7.0).svg("")}</div>
      {tria(["Sí", "No"], bona, mida="14pt", ample="2.5cm")}{extra}''', r, ".2rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">El tros pintat, és la fracció que diu? Marca la resposta.</div></div>
    <div class="clau" style="margin:.3rem 0 .6rem"><p style="margin:0">Mira si tots els trossos són iguals.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.3rem .6cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Una fracció vol trossos iguals.</p>
    <p style="margin:.2rem 0 0">Si els 4 trossos no són iguals, el tros pintat no és {fr(1, 4, "15pt")}.</p>
  </div>''')

# ===================================================================== pàgina 5: el nom
A = [("a", 3, 4, True), ("b", 2, 5, False), ("c", 1, 2, False), ("d", 5, 8, False)]
B = [("e", 4, 9, True), ("f", 1, 3, False), ("g", 7, 10, False), ("h", 5, 6, False)]
fa = "\n".join(f'''      <tr{' class="resolt"' if r else ''}><td style="text-align:center;width:2.4cm">{fr(n, d)}</td>'''
               f'''<td class="esq" style="font-size:15pt">{ms(nom(n, d)) if r else ""}</td></tr>''' for l, n, d, r in A)
fb = "\n".join(f'''      <tr{' class="resolt"' if r else ''}><td class="esq" style="font-size:15pt">{nom(n, d)}</td>'''
               f'''<td style="text-align:center;width:2.6cm;height:1.5cm">{fr(n, d, ma=True) if r else fr_buit("14pt")}</td></tr>''' for l, n, d, r in B)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Escriu com es llegeix cada fracció. Mira la targeta.</div></div>
    <table class="mini" style="margin-top:.4rem">
      <tr><th>La fracció</th><th>Es llegeix</th></tr>
{fa}
    </table>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Ara al revés: escriu la fracció.</div></div>
    <table class="mini" style="margin-top:.4rem">
      <tr><th>Es llegeix</th><th>La fracció</th></tr>
{fb}
    </table>
  </div>''')

# ===================================================================== pàgina 6: la vida
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="exercici">
    <div class="tasca"><div class="n">6</div><div class="q">Quina part us heu menjat? Escriu la fracció.</div></div>
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Una pizza rectangular de 8 trossos. Us n'heu menjat 3.</p>
      <div style="width:8.2cm">{tira(3, 8, "Una pizza de 8 trossos, amb 3 de menjats", W=8.0).svg("")}</div>
      <p class="frase" style="margin:.2rem 0 0">{fr(3, 8, ma=True)} : {ms("tres vuitens")}</p>""", True)}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Una xocolata de 12 quadradets. Us n'heu menjat 5.</p>
      <div style="width:8.2cm">{tira(5, 12, "Una xocolata de 12 quadradets, amb 5 de menjats", W=8.0).svg("")}</div>
      <p class="frase" style="margin:.2rem 0 0">{fr_buit()} : <u style="display:inline-block;min-width:4.6cm;padding:0"></u></p>""")}
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">7</div><div class="q">Un hort està partit en 5 trossos iguals. En un tros hi ha tomàquets.</div></div>
{caixa(f"""      <p class="frase" style="margin:0"><span class="apartat">a)</span> Amb una fracció: {fr(1, 5, ma=True)}</p>""", True)}
{caixa(f"""      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Pinta-ho: l'hort és tot el rectangle.</p>
      <div style="width:8.2cm">{tira(0, 5, "Un rectangle de 5 trossos, per pintar", W=8.0, buida=True).svg("")}</div>""")}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 3 · Què és una fracció · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Una fracció és un rectangle partit en trossos iguals: el de baix
    (denominador) diu quants trossos hi ha, i el de dalt (numerador), quants se'n pinten. La
    targeta de les fraccions és al davant tota l'estona: els noms no es demanen de memòria. Totes
    les fraccions es dibuixen amb el mateix rectangle, com a la caixa d'eines (tasca 9).
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb tires de paper: doblegar-ne una per la meitat i una altra vegada (4 trossos
  iguals) i pintar-ne 3. Són els 3/4 de la pàgina 1.</p>
  <h3>1. La fracció de cada dibuix</h3>
  <p>b) 2/5, dos cinquens; c) 5/8, cinc vuitens; d) 1/3, un terç; e) 7/10, set desens; f) 5/6, cinc
  sisens. Són els casos de la tasca 9.2 de la caixa. <b>Error típic:</b> girar-los (5/2) o comptar
  els trossos blancs (3/8 en lloc de 5/8).</p>
  <h3>2. Pinta la fracció</h3>
  <p>Es dona per bo qualsevol tros pintat, no cal que siguin els primers: el que compta és quants.</p>
  <h3>3. Trossos iguals</h3>
  <p>b) Sí; c) No; d) Sí. <b>Error típic:</b> dir que sí a l'apartat c perquè hi ha 3 trossos i un
  de pintat. És la regla trencada d'aquesta fitxa, que és l'exercici 2 de l'activitat Fraccions 0
  del grup. No l'expliqueu: que retalli el rectangle i posi els trossos un damunt de l'altre.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>4 i 5. El nom</h3>
  <p>4b) dos cinquens; 4c) un mig; 4d) cinc vuitens. 5f) 1/3; 5g) 7/10; 5h) 5/6. Sempre amb la targeta.</p>
  <h3>6 i 7. A la vida de cada dia</h3>
  <p>6b) 5/12, cinc dotzens. 7b) un tros pintat de 5: la cinquena part de l'hort. Els trossos d'un
  terreny són la manera com la situació d'aprenentatge del grup, «Com és de gran Gaza?», arriba a les
  fraccions: sumant trossos d'àrea.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=9</b> (9.1 Fes la fracció;
  9.2 Quina fracció és?). La 9.2 dona un codi de verificació. La 9.1 s'obre amb 4/9, com l'exercici 1.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (1.2, 5.2, 6.1 i 9.1) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb una tira de paper, fa 4 trossos iguals i en pinta 3.</li>
    <li>Escriu la fracció d'un dibuix, amb el numerador i el denominador al seu lloc (exercici 1).</li>
    <li>Pinta una fracció en un rectangle (exercici 2).</li>
    <li>Diu el nom d'una fracció amb la targeta, en tots dos sentits (exercicis 4 i 5).</li>
    <li>Nivells alts: explica per què un tros de 4 desiguals no és 1/4 (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 3 · Què és una fracció", """  FITXA · Unitat 3 · Les fraccions · Què és una fracció
  La primera fitxa de la unitat 3. Adapta les activitats Fraccions 0 i 2 del
  grup: una fracció és un rectangle partit en trossos iguals; el de baix diu
  quants n'hi ha, i el de dalt, quants se'n pinten. El nom, amb la targeta de
  les fraccions. Els casos són els de la tasca 9 de la caixa (regla 8).

  La regla trencada és «un tros de quatre és 1/4 encara que no siguin iguals»
  (exercici 3). Les fraccions van dins de .fr: comprova.py les llegeix.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud3.html")
