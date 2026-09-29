#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud2-repartir.html: repartir en files (unitat 2, fitxa 2).

Adapta les activitats 2_2 (divisió entera) i 2_5 (pràctica de divisors) del grup.
Fa servir les peces de dibuix de la primera fitxa de la unitat 1 (genfitxa.py).
"""
import os
import sys

_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])       # Dibuix, ms, buit, buit_curt, ULL, colors…

PEU = "Unitat 2 · Repartir · pàgina"
MARCA = ('<svg viewBox="0 0 24 24" style="position:absolute;left:-3px;top:-6px;width:26px;height:26px">'
         '<path d="M4 13l5 6L21 3" fill="none" stroke="#3A3A3A" stroke-width="3.5" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')
pagines = []


def pagina(cos, classe="full"):
    n = len(pagines) + 1
    pagines.append(f'<div class="{classe}">\n{cos.rstrip()}\n  <div class="pag">{PEU} {n}</div>\n</div>')


def tria(opcions, bona=None, revisa=False, mida="15pt", columna=False, ample="3.5cm"):
    """Opcions per marcar, de costat. Amb `revisa`, cada opció va dins de .revisa: són
    igualtats que poden ser falses a posta, i eines/comprova.py no les comprova."""
    peces = []
    for o in opcions:
        text = f'<span class="revisa">{o}</span>' if revisa else o
        if o == bona:
            peces.append(f'<label style="min-width:{ample};white-space:nowrap;font-size:{mida};border-width:3px;border-color:var(--tinta)">'
                         f'<span class="quadret">{MARCA}</span>{text}</label>')
        else:
            peces.append(f'<label style="min-width:{ample};white-space:nowrap;font-size:{mida}"><span class="quadret"></span>{text}</label>')
    if columna:
        # Una fila per opció, com a peces_ud2.py: amb flex-direction:column, WeasyPrint estirava
        # les opcions i les encavalcava al PDF (exercici 4, trobat el 29/9/2026).
        return (f'<div style="margin:.25rem 0">' +
                "".join(f'<div class="tria" style="margin:0 0 .35rem;width:{ample}">{p}</div>' for p in peces) +
                "</div>")
    return f'<div class="tria" style="margin:.25rem 0;flex-wrap:wrap">' + "".join(peces) + "</div>"


files_plenes = lambda q: "1 fila plena" if q == 1 else f"{q} files plenes"
sobren = lambda r: "en sobra 1" if r == 1 else f"en sobren {r}"


def repartiment(n, k, m, aria, rotuls=True):
    """n quadrets en files de k, com a la tasca 6.1 de la caixa: les files plenes en
    gris; els que sobren, blancs amb la vora gruixuda; i els llocs que falten a la fila a
    mitges, amb traç discontinu. En blanc i negre es distingeixen per la vora."""
    q, r = divmod(n, k)
    esq = 3.7 if rotuls else 0.1
    dalt = 0.8 if rotuls else 0.1
    dreta = 3.1 if (rotuls and r) else 0.1
    files = q + (1 if r else 0)
    d = Dibuix(esq + k * m + dreta, dalt + files * m + 0.15, aria)
    d.rectangle(esq, dalt, q, k, m)
    y = dalt + q * m
    for c in range(k if r else 0):
        if c < r:
            d.quadret(esq + c * m, y, m, fons="#fff", traç=NEGRE, gruix=2.4)
        else:
            d.quadret(esq + c * m, y, m, fons="#fff", traç=G3, gruix=1.2, discontinu=True)
    if rotuls:
        if q:
            d.clau_esq(esq - 0.2, dalt, dalt + q * m, files_plenes(q))
        d.clau_dalt(esq, esq + k * m, dalt - 0.25, f"{k} a cada fila")
        if r:
            d.text(esq + k * m + 0.25, y + m / 2 + 0.15, sobren(r), 0.42, 700, ancora="start")
    return d


def igualtat(n, k):
    q, r = divmod(n, k)
    return f"{n} = {q} · {k} + {r}"


# ===================================================================== pàgina 1
d = repartiment(37, 7, 0.72, "37 quadrets en files de 7: 5 files plenes i en sobren 2")
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs</b>. Posar 37 miniblocs en files de 7. Comptar les files plenes i els que sobren.</div>
  <h1>Repartir en files</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div class="figura neta" style="margin-top:1rem">
{d.svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .8rem">Hi ha files plenes de 7 i una fila a mitges.</p>

  <table>
    <tr class="resolt"><td class="esq">Quants quadrets hi ha a cada fila?</td><td style="width:3.6cm">{ms("7")}</td></tr>
    <tr class="resolt"><td class="esq">Quantes files plenes hi ha?</td><td>{ms("5")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets sobren?</td><td>{ms("2")}</td></tr>
  </table>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">5 files de 7 són 5 · 7 = 35. I en sobren 2.</p>
    <p style="font-size:30pt;font-weight:800;margin:.3rem 0">37 = 5 · 7 + 2</p>
    <p style="margin:0;font-weight:700">Els quadrets que sobren són el residu.</p>
    <p style="margin:0">Si no en sobra cap, la divisió és exacta.</p>
  </div>''')

# ===================================================================== pàgina 2: reparteix
def graella_repartir(n, k, m, aria, resolt):
    """Una quadrícula de k columnes, amb una fila més de les que calen, per no donar la
    resposta. A l'apartat resolt, les files plenes i els que sobren, pintats a mà."""
    q, r = divmod(n, k)
    files = q + (1 if r else 0) + 1
    d = Dibuix(k * m + 0.1, files * m + 0.1, aria)
    d.graella(0.05, 0.05, files, k, m)
    if resolt:
        d.pintat(0.05, 0.05, q, k, m)
        if r:
            d.pintat(0.05, 0.05 + q * m, 1, r, m)
    return d


REP = [("a", 37, 7, True), ("b", 20, 4, False), ("c", 23, 9, False), ("d", 20, 6, False)]
caselles2 = []
for lletra, n, k, resolt in REP:
    q, r = divmod(n, k)
    g = graella_repartir(n, k, 0.62, f"Quadrícula de {k} columnes per repartir-hi {n} quadrets", resolt)
    plens = ms(str(q)) if resolt else buit_curt()
    sob = ms(str(r)) if resolt else buit_curt()
    fons = ' class="resolt"' if resolt else ""
    caselles2.append(f'''      <div{fons} style="border-radius:10px;padding:.35rem .5rem">
        <p style="margin:0 0 .2rem;font-size:15pt;font-weight:700"><span class="apartat">{lletra})</span> {n} en files de {k}</p>
{g.svg("        ")}
        <p class="frase" style="margin:.2rem 0 0;font-size:14.5pt">Files plenes: {plens}</p>
        <p class="frase" style="margin:0;font-size:14.5pt">En sobren: {sob}</p>
      </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Pinta els quadrets, fila a fila. Després escriu les files plenes i els que sobren.</div></div>
    <div class="avis puntejat" style="margin:.3rem 0 .6rem">Omple una fila sencera abans de començar-ne una altra.</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.6rem .8cm">
{chr(10).join(caselles2)}
    </div>
  </div>''')

# ===================================================================== pàgina 3: exacta o no
EXACTA = [("a", 30, 9, True), ("b", 20, 5, False), ("c", 56, 7, False), ("d", 45, 6, False),
          ("e", 10, 3, False), ("f", 48, 8, False)]
caselles3 = []
for lletra, n, k, resolt in EXACTA:
    q, r = divmod(n, k)
    bona = ("En sobren" if r else "És exacta") if resolt else None
    extra = f'<p class="frase" style="margin:0;font-size:14.5pt">{ms(igualtat(n, k))}</p>' if resolt else \
            f'<p class="frase" style="margin:0;font-size:14.5pt">En sobren: {buit_curt()}</p>'
    fons = ' class="resolt"' if resolt else ""
    caselles3.append(f'''      <div{fons} style="border-radius:10px;padding:.3rem .5rem">
        <p style="margin:0;font-size:16pt;font-weight:700"><span class="apartat">{lletra})</span> {n} en files de {k}</p>
        {tria(["En sobren", "És exacta"], bona, mida="14pt", ample="3.6cm")}
        {extra}
      </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Sobren quadrets? Marca la resposta. Mira la targeta.</div></div>
    <div class="clau" style="margin:.3rem 0 .7rem">
      <p style="margin:0">Busca el nombre a la taula de la targeta.</p>
      <p style="margin:0">Si hi és, la divisió és exacta. Si no hi és, en sobren.</p>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.55rem .8cm">
{chr(10).join(caselles3)}
    </div>
  </div>''')

# ===================================================================== pàgina 4: la igualtat
IGUAL = [("a", 37, 7, True), ("b", 40, 6, False), ("c", 35, 7, False), ("d", 20, 6, False), ("e", 10, 3, False)]
files4 = []
for lletra, n, k, resolt in IGUAL:
    q, r = divmod(n, k)
    cos = (f"{n} = {ms(str(q))} · {k} + {ms(str(r))}" if resolt
           else f"{n} = {buit_curt()} · {k} + {buit_curt()}")
    fons = ' class="resolt"' if resolt else ""
    files4.append(f'''    <div{fons} style="border-radius:10px;padding:.35rem .6rem;margin-bottom:.35rem">
      <p style="margin:0;font-size:14pt;color:var(--gris-2)"><span class="apartat" style="color:var(--tinta)">{lletra})</span> {n} quadrets en files de {k}</p>
      <p class="frase" style="margin:.05rem 0 0;font-size:22pt;font-weight:800">{cos}</p>
    </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Completa la igualtat.</div></div>
    <div class="clau" style="margin:.3rem 0 .7rem">
      <p style="margin:0">Al primer forat, les files plenes. Al segon, els que sobren.</p>
      <p style="margin:0">Si no en sobra cap, escriu un 0.</p>
    </div>
{chr(10).join(files4)}
  </div>''')

# ===================================================================== pàgina 5: la regla trencada
TRENCADA = [("a", 37, 7, True, False), ("b", 23, 9, False, True), ("c", 20, 5, False, False), ("d", 50, 7, False, False)]
caselles5 = []
for lletra, n, k, resolt, bona_primer in TRENCADA:
    q, r = divmod(n, k)
    bona = igualtat(n, k) if r else f"{n} = {q} · {k}"
    dolenta = f"{n} = {q} · {k}" if r else f"{n} = {q} · {k} + 1"
    opcions = [bona, dolenta] if bona_primer else [dolenta, bona]
    dib = repartiment(n, k, 0.42, f"{n} quadrets en files de {k}", rotuls=False)
    fons = ' class="resolt"' if resolt else ""
    caselles5.append(f'''      <div{fons} style="border-radius:10px;padding:.35rem .5rem">
        <p style="margin:0 0 .2rem;font-size:15pt;font-weight:700"><span class="apartat">{lletra})</span> {n} en files de {k}</p>
{dib.svg("        ")}
        {tria(opcions, bona if resolt else None, revisa=True, mida="15pt", columna=True, ample="5.2cm")}
      </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Marca la igualtat bona. Mira el dibuix.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.6rem .8cm;margin-top:.4rem">
{chr(10).join(caselles5)}
    </div>
  </div>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">37 en files de 7 no són 5 i prou.</p>
    <p style="margin:.2rem 0 0">Fas 5 files plenes, i en sobren 2: 37 = 5 · 7 + 2.</p>
  </div>''')

# ===================================================================== pàgina 6: la vida
def caramels(files, cols, aria, m=0.33):
    d = Dibuix(cols * m + 0.2, files * m + 0.2, aria)
    for fi in range(files):
        for c in range(cols):
            cx, cy = 0.1 + c * m + m / 2, 0.1 + fi * m + m / 2
            d.cru(f'<circle cx="{d.px(cx)}" cy="{d.px(cy)}" r="{d.px(m * 0.36)}" fill="{F3}" stroke="{G1}" stroke-width="1.4"/>')
    return d


pagina(f'''  <h2>A la vida de cada dia</h2>

  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Reparteix els caramels. Tothom en té els mateixos, i no se'n trenca cap.</div></div>
    <div class="clau" style="margin:.2rem 0 .5rem">
      <p style="margin:0">Si la divisió és exacta, el nombre és <b>divisor</b>: 9 és divisor de 63.</p>
    </div>
    <div class="resolt" style="border-radius:10px;padding:.4rem .6rem;margin-bottom:.4rem">
      <p style="margin:0 0 .2rem"><span class="apartat">a)</span> 63 caramels entre 9 persones.</p>
      <div style="display:flex;gap:.9cm;align-items:center">
        <div style="flex:0 0 auto">
{caramels(9, 7, "9 files de 7 caramels: una fila per a cada persona").svg("          ")}
        </div>
        <div>
          <p class="frase" style="margin:0">{ms("9 · 7 = 63")}</p>
          <p class="frase" style="margin:0">Cadascú en té {ms("7")}. En sobren {ms("0")}.</p>
          <p class="frase" style="margin:0">9 és divisor de 63? {ms("Sí")}</p>
        </div>
      </div>
    </div>
    <div style="padding:.4rem .6rem">
      <p style="margin:0 0 .2rem"><span class="apartat">b)</span> 60 caramels entre 9 persones.</p>
      <p class="frase" style="margin:0">9 · {buit_curt()} = {buit_curt()}</p>
      <p class="frase" style="margin:0">Cadascú en té {buit_curt()}. En sobren {buit_curt()}.</p>
      <p class="frase" style="margin:0">9 és divisor de 60? {buit_curt()}</p>
    </div>
  </div>

  <div class="exercici">
    <div class="tasca"><div class="n">6</div><div class="q">Les barques són de 4 persones. Quantes barques s'omplen?</div></div>
    <div class="duo">
      <div class="resolt" style="border-radius:10px;padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Hi ha 26 persones.</p>
        <p class="frase" style="margin:0">{ms("26 = 6 · 4 + 2")}</p>
        <p class="frase" style="margin:0">S'omplen {ms("6")} barques.</p>
        <p class="frase" style="margin:0">En sobren {ms("2")}.</p>
      </div>
      <div style="padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Hi ha 30 persones.</p>
        <p class="frase" style="margin:0">30 = {buit_curt()} · 4 + {buit_curt()}</p>
        <p class="frase" style="margin:0">S'omplen {buit_curt()} barques.</p>
        <p class="frase" style="margin:0">En sobren {buit_curt()} persones.</p>
      </div>
    </div>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 2 · Repartir en files · full per al professorat</p>

  <div class="abans">
    <b>Abans de començar.</b> Les caixes plenes de boles del GeoGebra del grup són les files
    plenes de quadrets: «repartir 37 boles en caixes de 7» és «posar 37 quadrets en files de 7».
    Es diu sempre igual: «files plenes», «a cada fila» i «en sobren». La paraula del grup, el
    <b>residu</b>, surt a la pàgina 1. El residu no es calcula restant: es compta, al dibuix o
    comptant endavant des de l'últim resultat de la taula (del 36 al 40: 37, 38, 39, 40, en sobren 4).
  </div>

  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs: posar els 37 en files de 7, i comptar les files plenes (5) i els
  que sobren (2). És l'exercici 5 de l'activitat 2_2 del grup, i l'exemple de la tasca 6.1 de la
  caixa.</p>

  <h3>1. Pinta i escriu</h3>
  <p>b) 20 en files de 4: 5 files plenes, en sobren 0 (exacta). c) 23 en files de 9: 2 files
  plenes, en sobren 5. d) 20 en files de 6: 3 files plenes, en sobren 2. La quadrícula té una fila
  més de les que calen, a posta: si la hi donés justa, ja diria si en sobren. <b>Error típic:</b>
  començar una fila nova abans d'acabar l'anterior.</p>

  <h3>2. Sobren quadrets?</h3>
  <p>b) exacta (5 · 4 = 20); c) exacta (7 · 8 = 56); d) en sobren 3 (45 = 7 · 6 + 3); e) en sobra 1
  (10 = 3 · 3 + 1); f) exacta (6 · 8 = 48). Són els casos de la tasca 6.2 de la caixa. Si hi és a la
  taula de la targeta, és exacta: no cal fer el dibuix.</p>

  <h3>3. La igualtat</h3>
  <p>b) 40 = 6 · 6 + 4; c) 35 = 5 · 7 + 0; d) 20 = 3 · 6 + 2; e) 10 = 3 · 3 + 1. Són les de
  l'exercici 10 de l'activitat 2_2 del grup, amb les files plenes al primer lloc, com a tot el
  curs (3 · 4 són 3 files de 4). El grup ho escriu al revés (40 = 6 · … + 4): és el mateix, perquè
  el rectangle es pot girar.</p>
</div>''')

pagines.append('''<div class="full sol">
  <h3>4. Marca la igualtat bona</h3>
  <p>b) 23 = 2 · 9 + 5; c) 20 = 4 · 5, que és exacta; d) 50 = 7 · 7 + 1. <b>Error típic:</b>
  oblidar el residu: «37 entre 7 són 5». És la regla trencada d'aquesta fitxa. No l'expliqueu: que
  compti tots els quadrets del dibuix. Amb 5 · 7 només n'hi ha 35, i al dibuix en són 37. L'apartat
  c és exacte a posta: si sempre tria la que té «+», encara no mira el dibuix.</p>

  <h3>5 i 6. A la vida de cada dia</h3>
  <p>5b) 9 · 6 = 54: cadascú en té 6, en sobren 6, i 9 no és divisor de 60. Són els caramels de
  l'activitat 2_5 del grup. 6a i 6b: les persones que sobren necessiten una barca més (7 i 8
  barques en total). 6b) 30 = 7 · 4 + 2: s'omplen 7 barques i en sobren 2 persones. El 30 no és a la taula del 4: 4 · 7 = 28 i 4 · 8 = 32.</p>

  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=6</b> (6.1 Reparteix en
  files; 6.2 Sobren quadrets?). La 6.2 dona un codi de verificació. La 6.1 s'obre amb el 37 en
  files de 7, com la pàgina 1.</p>

  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (1.4, 3.2, 4.2 i 5.2) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb miniblocs, reparteix un nombre en files iguals i diu les files plenes i els que sobren.</li>
    <li>Pinta un repartiment a la quadrícula, fila a fila (exercici 1).</li>
    <li>Diu si una divisió és exacta mirant la taula de la targeta (exercici 2).</li>
    <li>Completa la igualtat amb les files plenes i el residu (exercici 3).</li>
    <li>Nivells alts: tria la igualtat bona, també quan és exacta, i diu si un nombre és divisor d'un altre (exercicis 4 i 5).</li>
  </ul>
</div>''')

# ===================================================================== el document
cap = '''<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Unitat 2 · Repartir en files</title>
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
</head>
<body>
<!--
  FITXA · Unitat 2 · Divisibilitat · Repartir en files
  La segona fitxa de la unitat 2. Adapta les activitats 2_2 (divisió entera: les
  caixes i les boles del GeoGebra) i 2_5 (la pràctica de divisors, amb caramels)
  del grup. Les caixes plenes són files plenes de quadrets; les boles que
  sobren, el residu. La igualtat és la del grup, amb les files plenes al primer
  lloc, com a tot el curs: 37 = 5 · 7 + 2.

  Els casos són els de la tasca 6 de la caixa (regla 8): el 37 en files de 7 de
  la 6.1 i els repartiments de la 6.2. Els de l'exercici 3 són els de
  l'exercici 10 de l'activitat 2_2 del grup.

  La regla trencada és oblidar el residu: «37 entre 7 són 5» (exercici 4). Les
  igualtats per triar van dins de .revisa, perquè n'hi ha de falses a posta. La
  pàgina acaba amb la forma bona a la vista.

  Cada bloc .full acaba amb un </div> a principi de línia; els de dins van
  sagnats. Les regles són a docs/CRITERIS-DISSENY.md. Després de canviar
  res: eines/mesura.py, generadors/gen_pdf.py i eines/comprova.py.
-->

'''
html = cap + "\n\n".join(pagines) + "\n\n</body>\n</html>\n"
sortida = sys.argv[1] if len(sys.argv) > 1 else "ud2-repartir.html"
open(sortida, "w", encoding="utf-8").write(html)
print(sortida, len(pagines), "blocs")
