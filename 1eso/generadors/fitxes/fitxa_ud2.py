#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud2.html: els múltiples (unitat 2, fitxa 1).

Adapta les activitats 2_1 (múltiples) i 2_3 (criteris de divisibilitat) del grup.
Fa servir les peces de dibuix de la primera fitxa de la unitat 1 (genfitxa.py).
"""
import os
import sys

_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])       # Dibuix, ms, buit, buit_curt, ULL, colors…

PEU = "Unitat 2 · Múltiples · pàgina"
MARCA = ('<svg viewBox="0 0 24 24" style="position:absolute;left:-3px;top:-6px;width:26px;height:26px">'
         '<path d="M4 13l5 6L21 3" fill="none" stroke="#3A3A3A" stroke-width="3.5" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')
pagines = []


def pagina(cos, classe="full"):
    n = len(pagines) + 1
    pagines.append(f'<div class="{classe}">\n{cos.rstrip()}\n  <div class="pag">{PEU} {n}</div>\n</div>')


def tria(opcions, bona=None):
    """Les opcions per marcar, l'una al costat de l'altra: prou amples per marcar-les, i
    prou estretes perquè Sí i No càpiguen en mitja pàgina."""
    peces = []
    for o in opcions:
        if o == bona:
            peces.append(f'<label style="min-width:2.7cm;border-width:3px;border-color:var(--tinta)"><span class="quadret">{MARCA}</span>{o}</label>')
        else:
            peces.append(f'<label style="min-width:2.7cm"><span class="quadret"></span>{o}</label>')
    return '<div class="tria" style="margin:.25rem 0;flex-wrap:nowrap">' + "".join(peces) + "</div>"


def graella100(k, estil, aria, m=0.98):
    """La graella de 100 de l'activitat del grup, amb els nombres a 14 pt.
    estil: None (buida, per pintar), "imprès" (els múltiples de k, pintats en gris
    d'impremta) o "a_ma" (pintats a mà: l'apartat resolt)."""
    d = Dibuix(10 * m + 0.2, 10 * m + 0.2, aria)
    for n in range(1, 101):
        f, c = (n - 1) // 10, (n - 1) % 10
        x, y = 0.1 + c * m, 0.1 + f * m
        marcat = estil and n % k == 0
        fons = {None: "#fff", "imprès": F3, "a_ma": VORA_SUAU}[estil] if marcat else "#fff"
        traç = MS if (marcat and estil == "a_ma") else G2
        d.cru(f'<rect x="{d.px(x)}" y="{d.px(y)}" width="{d.px(m)}" height="{d.px(m)}" fill="{fons}" '
              f'stroke="{traç}" stroke-width="{2 if marcat else 1.1}"/>')
        # la lletra, a la mida del quadret: 14 pt amb el quadret d'1 cm
        mida = min(0.47, m * 0.46) * (0.85 if n == 100 else 1)
        d.text(x + m / 2, y + m / 2 + mida * 0.36, str(n), mida, 800 if marcat else 400)
    return d


def files_de(k, quantes, m=0.62, aria=""):
    """Rectangles de 1, 2, 3… files de k quadrets, un al costat de l'altre."""
    gap = 0.7
    amp = quantes * (k * m) + (quantes - 1) * gap + 0.2
    d = Dibuix(amp, quantes * m + 0.9, aria)
    x = 0.1
    for q in range(1, quantes + 1):
        d.rectangle(x, 0.1 + (quantes - q) * m, q, k, m)
        x += k * m + gap
    return d


# ===================================================================== pàgina 1
d = files_de(2, 5, 0.62, "Cinc rectangles de files de 2 quadrets: d'1 fila, de 2, de 3, de 4 i de 5 files")
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs</b>. Fer files de 2 miniblocs, una sota l'altra, i comptar-los cada vegada: 2, 4, 6, 8, 10.</div>
  <h1>Els múltiples</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div class="figura neta" style="margin-top:1rem">
{d.svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .8rem">Són rectangles amb files de 2. Cada un té una fila més.</p>

  <table>
    <tr class="resolt"><td class="esq">Quants quadrets té el rectangle d'1 fila?</td><td style="width:3.6cm">{ms("2")}</td></tr>
    <tr class="resolt"><td class="esq">I el de 2 files?</td><td>{ms("4")}</td></tr>
    <tr class="resolt"><td class="esq">I el de 3 files?</td><td>{ms("6")}</td></tr>
  </table>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">Són la taula del 2: 2 · 1 = 2, 2 · 2 = 4, 2 · 3 = 6…</p>
    <p style="margin:0">El 0 també hi és: 2 · 0 = 0.</p>
    <p style="font-size:24pt;font-weight:800;margin:.3rem 0">Múltiples del 2: 0, 2, 4, 6, 8, 10…</p>
    <p style="margin:0;font-weight:700">Els múltiples d'un nombre són la seva taula de multiplicar.</p>
  </div>''')

# ===================================================================== pàgina 2
def llista(lletra, k, resolt):
    vals = [k * i for i in range(11)]
    celes = "".join(
        f'<td style="text-align:center;padding:.2rem 0;height:1.25cm">{ms(str(v)) if resolt else ("0" if i == 0 else "")}</td>'
        for i, v in enumerate(vals))
    fons = ' class="resolt"' if resolt else ""
    return f'''    <p style="margin:.55rem 0 .15rem;font-size:16pt;font-weight:700"><span class="apartat">{lletra})</span> Múltiples del {k}:</p>
    <table class="mini" style="table-layout:fixed;margin:0"><tr{fons}>{celes}</tr></table>'''


pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Escriu els múltiples de cada nombre. Mira la targeta.</div></div>
    <div class="avis puntejat" style="margin:.3rem 0 .4rem">Comença pel 0. Després, la taula de la targeta, de dalt a baix.</div>
{llista("a", 10, True)}
{llista("b", 9, False)}
{llista("c", 8, False)}
{llista("d", 7, False)}
  </div>

  <div class="clau" style="margin-top:1rem">
    <p style="margin:0">La llista continua: després del 10 · 10 = 100 venen el 110, el 120…</p>
    <p style="margin:0">Els tres punts (…) volen dir que continua.</p>
  </div>''')

# ===================================================================== pàgina 3
g2 = graella100(2, "a_ma", "Graella de 100 amb els múltiples del 2 pintats: fan columnes", m=0.64)
g5 = graella100(5, None, "Graella de 100 buida, per pintar-hi els múltiples del 5", m=1.0)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Pinta els múltiples del 5 a la graella. Mira quina forma fan.</div></div>
    <div style="display:flex;gap:.35cm;align-items:flex-start">
      <div class="resolt" style="flex:0 0 6.9cm;border-radius:10px;padding:.35rem .45rem">
        <p style="margin:0 0 .2rem;font-weight:700"><span class="apartat">a)</span> Els múltiples del 2</p>
{g2.svg("        ")}
        <p class="frase" style="margin:.2rem 0 0">Forma: {ms("columnes")}</p>
      </div>
      <div style="flex:0 0 10.6cm;padding:.35rem .2rem">
        <p style="margin:0 0 .2rem;font-weight:700"><span class="apartat">b)</span> Els múltiples del 5</p>
{g5.svg("        ")}
        <p class="frase" style="margin:.2rem 0 0">Forma: {buit()}</p>
      </div>
    </div>
  </div>

  <div class="avis gruixut">
    <p style="margin:0;font-weight:700">El truc de l'última xifra:</p>
    <p style="margin:0">Els múltiples del 2 acaben en 0, 2, 4, 6 o 8.</p>
    <p style="margin:0">Els múltiples del 5 acaben en 0 o en 5.</p>
    <p style="margin:0">Els múltiples del 10 acaben en 0.</p>
  </div>''')

# ===================================================================== pàgina 4: la regla trencada
g3 = graella100(3, "imprès", "Graella de 100 amb els múltiples del 3 pintats: fan diagonals", m=0.95)
TRES = [("a", 12, True), ("b", 13, False), ("c", 21, False), ("d", 23, False), ("e", 3, False), ("f", 27, False)]
items = []
for lletra, n, resolt in TRES:
    si = n % 3 == 0
    fons = ' class="resolt"' if resolt else ""
    extra = f'<p class="frase" style="margin:0;font-size:14pt">{ms("3 · 4 = 12")}</p>' if resolt else ""
    items.append(f'''      <div{fons} style="border-radius:10px;padding:.25rem .5rem">
        <p style="margin:0;font-size:18pt;font-weight:800"><span class="apartat" style="font-size:14pt">{lletra})</span> {n}</p>
        {tria(["Sí", "No"], ("Sí" if si else "No") if resolt else None)}{extra}
      </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">És múltiple del 3? Marca Sí o No. Mira la taula del 3 de la targeta.</div></div>
    <div style="width:9.7cm;margin:.3rem auto 0">
{g3.svg("      ")}
      <p style="margin:.1rem 0 .4rem;font-size:14pt;color:var(--gris-2);text-align:center">Els múltiples del 3, pintats.</p>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:.35rem .4cm">
{chr(10).join(items)}
    </div>
  </div>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Els múltiples del 3 no sempre acaben en 3.</p>
    <p style="margin:.2rem 0 0">El 12 i el 21 ho són. El 13 i el 23 acaben en 3, i no ho són.</p>
  </div>''')

# ===================================================================== pàgina 5: el truc del 3
# de la llista de la tasca 5.4 de la caixa; el 126 és l'exemple de la 5.3
SUMES = [("a", 126, True), ("b", 123, False), ("c", 214, False), ("d", 405, False), ("e", 88, False),
         ("f", 312, False), ("g", 71, False)]
files_s = []
for lletra, n, resolt in SUMES:
    xs = [int(x) for x in str(n)]
    if resolt:
        cel = (f'<td style="text-align:center">{ms(" + ".join(map(str, xs)) + " = " + str(sum(xs)))}</td>'
               f'<td style="text-align:center">{ms("Sí")}</td><td style="text-align:center">{ms("Sí")}</td>')
    else:
        cel = '<td class="omplir" style="height:1.3cm"></td><td class="omplir"></td><td class="omplir"></td>'
    files_s.append(f'''      <tr{' class="resolt"' if resolt else ''}><td class="apartat" style="font-size:17pt;white-space:nowrap">{lletra}) {n}</td>{cel}</tr>''')
pagina(f'''  <h2>El truc del 3</h2>
  <div class="avis gruixut">
    <p style="margin:0">Vols saber si 126 és múltiple del 3.</p>
    <p style="margin:0">1. Suma les xifres, d'una en una: 1 + 2 + 6 = 9.</p>
    <p style="margin:0">2. Busca el 9 a la taula del 3 de la targeta. Hi és.</p>
    <p style="margin:0;font-weight:700">3. Per tant, 126 és múltiple del 3.</p>
  </div>

  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Fes el truc del 3 amb cada nombre. Ves a poc a poc.</div></div>
    <table class="mini" style="margin-top:.4rem">
      <tr><th style="width:3.3cm">Nombre</th><th>Suma de les xifres</th><th style="width:3.6cm">És a la taula del 3?</th><th style="width:3.6cm">És múltiple del 3?</th></tr>
{chr(10).join(files_s)}
    </table>
  </div>

  <div class="clau" style="margin-top:.8rem">
    <p style="margin:0">La taula del 3: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30.</p>
  </div>''')

# ===================================================================== pàgina 6: els quatre trucs
# els nombres de la taula de l'activitat 2_3 del grup (sense el 110.000.001)
QUATRE = [("a", 160, True), ("b", 945, False), ("c", 60, False), ("d", 23, False), ("e", 42, False), ("f", 550, False)]
files_q = []
for lletra, n, resolt in QUATRE:
    if resolt:
        r = [n % 2 == 0, n % 5 == 0, n % 10 == 0, n % 3 == 0]
        cel = "".join(f'<td style="text-align:center">{ms("Sí" if v else "No")}</td>' for v in r)
    else:
        cel = '<td class="omplir" style="height:1.25cm"></td>' * 4
    files_q.append(f'''      <tr{' class="resolt"' if resolt else ''}><td class="apartat" style="font-size:17pt;white-space:nowrap">{lletra}) {n}</td>{cel}</tr>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Fes els quatre trucs. Escriu Sí o No.</div></div>
    <table class="mini" style="margin-top:.4rem">
      <tr><th style="width:3.3cm">Nombre</th><th>Múltiple del 2?</th><th>Múltiple del 5?</th><th>Múltiple del 10?</th><th>Múltiple del 3?</th></tr>
{chr(10).join(files_q)}
    </table>
    <div class="avis puntejat" style="margin-top:.6rem">
      <p style="margin:0">El 2, el 5 i el 10: mira l'última xifra.</p>
      <p style="margin:0">El 3: suma les xifres i mira la taula del 3.</p>
    </div>
  </div>

  <div class="clau" style="margin-top:1rem">
    <p style="margin:0">A classe també es diu <b>divisible</b>.</p>
    <p style="margin:0">«126 és múltiple del 3» vol dir el mateix que «126 és divisible entre 3».</p>
  </div>''')

# ===================================================================== pàgina 7: la vida
def capsa_ous(d, x, y):
    d.cru(f'<rect x="{d.px(x)}" y="{d.px(y)}" width="{d.px(2.1)}" height="{d.px(1.35)}" rx="{d.px(0.15)}" '
          f'fill="{F2}" stroke="{G2}" stroke-width="1.4"/>')
    for fi in range(2):
        for co in range(3):
            d.cru(f'<ellipse cx="{d.px(x + 0.42 + co * 0.62)}" cy="{d.px(y + 0.35 + fi * 0.65)}" rx="{d.px(0.24)}" '
                  f'ry="{d.px(0.29)}" fill="#fff" stroke="{G1}" stroke-width="1.8"/>')


def capses(n, aria):
    d = Dibuix(n * 2.45 + 0.1, 1.55, aria)
    for i in range(n):
        capsa_ous(d, 0.1 + i * 2.45, 0.1)
    return d


def monedes(n, aria):
    r = 0.5
    d = Dibuix(n * (2 * r + 0.18) + 0.1, 2 * r + 0.2, aria)
    for i in range(n):
        cx = 0.1 + r + i * (2 * r + 0.18)
        d.cru(f'<circle cx="{d.px(cx)}" cy="{d.px(0.1 + r)}" r="{d.px(r)}" fill="{F2}" stroke="{G1}" stroke-width="2"/>')
        d.cru(f'<circle cx="{d.px(cx)}" cy="{d.px(0.1 + r)}" r="{d.px(r - 0.1)}" fill="none" stroke="{G3}" stroke-width="1"/>')
        d.text(cx, 0.1 + r + 0.14, "2 €", 0.36, 800)
    return d


pagina(f'''  <h2>A la vida de cada dia</h2>

  <div class="exercici">
    <div class="tasca"><div class="n">6</div><div class="q">Els ous van en capses de 6. Es poden comprar sense obrir cap capsa?</div></div>
    <div class="duo">
      <div class="resolt" style="border-radius:10px;padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Vols 18 ous.</p>
{capses(3, "Tres capses de 6 ous").svg("        ")}
        {tria(["Sí", "No"], "Sí")}
        <p class="frase" style="margin:0">{ms("6 · 3 = 18")}. Són {ms("3")} capses.</p>
      </div>
      <div style="padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Vols 20 ous.</p>
{capses(1, "Una capsa de 6 ous").svg("        ")}
        {tria(["Sí", "No"])}
        <p class="frase" style="margin:0">La taula del 6: 6 · {buit_curt()} = {buit_curt()}</p>
      </div>
    </div>
  </div>

  <div class="exercici">
    <div class="tasca"><div class="n">7</div><div class="q">Tens monedes de 2 €. Pots pagar el preu just, sense canvi?</div></div>
    <div class="duo">
      <div class="resolt" style="border-radius:10px;padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Un llibre de 14 €.</p>
{monedes(7, "Set monedes de 2 euros").svg("        ")}
        {tria(["Sí", "No"], "Sí")}
        <p class="frase" style="margin:0">Acaba en 4. {ms("2 · 7 = 14")}: {ms("7")} monedes.</p>
      </div>
      <div style="padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Una samarreta de 15 €.</p>
{monedes(1, "Una moneda de 2 euros").svg("        ")}
        {tria(["Sí", "No"])}
        <p class="frase" style="margin:0">Acaba en {buit_curt()}.</p>
      </div>
    </div>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 2 · Els múltiples · full per al professorat</p>

  <div class="abans">
    <b>Abans de començar.</b> Es diu sempre igual: «els múltiples del 3 són la taula del 3». La
    targeta és al davant tota l'estona: una llista de múltiples és una columna de la targeta, i
    «és múltiple?» és «és a la taula?». El 0 és múltiple de tots, com a les llistes del grup. El
    truc del 3 es fa a poc a poc: primer la suma, xifra a xifra, i després la taula. La suma sempre
    dona de l'1 al 27, i la taula del 3 de la targeta arriba fins al 30.
  </div>

  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs: fer una fila de 2, i anar-ne afegint una a sota, comptant-los tots
  cada vegada: 2, 4, 6, 8, 10. Són els rectangles de la pàgina 1, i la taula del 2.</p>

  <h3>1. Les llistes de múltiples</h3>
  <p>b) 0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90. c) 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80.
  d) 0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70. Són els de l'activitat 2_1 del grup, sense el 19 i
  el 600, que no són a la targeta. <b>Error típic:</b> oblidar el 0, o saltar-se una fila de la
  targeta.</p>

  <h3>2. La graella de 100</h3>
  <p>b) Els múltiples del 5 fan dues columnes: la del 5 i la del 10. Com els del 2, fan columnes
  perquè sempre acaben en la mateixa xifra. Es dona per bona qualsevol manera de dir-ho: «ratlles»,
  «files de dalt a baix».</p>

  <h3>3. És múltiple del 3?</h3>
  <p>a) Sí (3 · 4 = 12); b) No; c) Sí (3 · 7 = 21); d) No; e) Sí (3 · 1 = 3); f) Sí (3 · 9 = 27).
  <b>Error típic:</b> dir que sí al 13 i al 23 perquè acaben en 3. És la regla trencada d'aquesta
  fitxa: el truc de l'última xifra serveix per al 2, el 5 i el 10, però no per al 3. No
  l'expliqueu: que miri la graella de la mateixa pàgina, on els del 3 fan diagonals, i que busqui
  el 13 a la taula del 3 de la targeta.</p>
</div>''')

pagines.append('''<div class="full sol">
  <h3>4. El truc del 3</h3>
  <table>
    <tr><th></th><th>Suma de les xifres</th><th>És a la taula del 3?</th><th>És múltiple del 3?</th></tr>
    <tr><td>b) 123</td><td>1 + 2 + 3 = 6</td><td>Sí</td><td>Sí</td></tr>
    <tr><td>c) 214</td><td>2 + 1 + 4 = 7</td><td>No</td><td>No</td></tr>
    <tr><td>d) 405</td><td>4 + 0 + 5 = 9</td><td>Sí</td><td>Sí</td></tr>
    <tr><td>e) 88</td><td>8 + 8 = 16</td><td>No</td><td>No</td></tr>
    <tr><td>f) 312</td><td>3 + 1 + 2 = 6</td><td>Sí</td><td>Sí</td></tr>
    <tr><td>g) 71</td><td>7 + 1 = 8</td><td>No</td><td>No</td></tr>
  </table>
  <p>Els nombres són els de la tasca 5.4 de la caixa. <b>Error típic:</b> una suma mal feta, sobretot
  8 + 8. Que compti amb els dits o amb els miniblocs: aquí la suma és la feina, i és una bona
  ocasió per fer-ne. Si la suma està bé i s'equivoca en la taula, que la busqui a la targeta.</p>

  <h3>5. Els quatre trucs</h3>
  <table>
    <tr><th></th><th>Del 2</th><th>Del 5</th><th>Del 10</th><th>Del 3</th></tr>
    <tr><td>b) 945</td><td>No</td><td>Sí</td><td>No</td><td>Sí (9 + 4 + 5 = 18)</td></tr>
    <tr><td>c) 60</td><td>Sí</td><td>Sí</td><td>Sí</td><td>Sí (6 + 0 = 6)</td></tr>
    <tr><td>d) 23</td><td>No</td><td>No</td><td>No</td><td>No (2 + 3 = 5)</td></tr>
    <tr><td>e) 42</td><td>Sí</td><td>No</td><td>No</td><td>Sí (4 + 2 = 6)</td></tr>
    <tr><td>f) 550</td><td>Sí</td><td>Sí</td><td>Sí</td><td>No (5 + 5 + 0 = 10)</td></tr>
  </table>
  <p>Són els nombres de la taula de l'activitat 2_3 del grup, sense el 110.000.001. Els criteris
  del 6 i del 9 queden fora (docs/MAPA-ADAPTACIO.md). La clau del final lliga «múltiple» amb
  «divisible», la paraula que farà servir el grup.</p>

  <h3>6 i 7. A la vida de cada dia</h3>
  <p>6b) No: 6 · 3 = 18 i 6 · 4 = 24; el 20 no és a la taula del 6. 7b) No: acaba en 5, i els
  múltiples del 2 acaben en 0, 2, 4, 6 o 8. És la mateixa decisió que als exercicis: és a la taula?</p>
</div>''')

pagines.append('''<div class="full sol">
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=5</b> (5.1 La graella de
  100; 5.2 És múltiple?; 5.3 Els trucs; 5.4 Múltiple de 3?). La 5.2 i la 5.4 donen un codi de
  verificació. La graella de la 5.1 s'obre amb els múltiples del 2, com la pàgina 1, i la 5.3 amb el
  126, com la pàgina 5.</p>

  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (1.4, 3.2, 4.2 i 5.2) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb miniblocs, fa files de 2 i diu els múltiples del 2 comptant-los.</li>
    <li>Escriu els múltiples d'un nombre, començant pel 0, amb la targeta (exercici 1).</li>
    <li>Pinta els múltiples a la graella de 100 i diu quina forma fan (exercici 2).</li>
    <li>Diu si un nombre és múltiple del 2, del 5 o del 10 per l'última xifra (exercici 5).</li>
    <li>Fa el truc del 3: suma les xifres i busca la suma a la taula del 3 (exercici 4).</li>
    <li>Nivells alts: explica per què el 13 no és múltiple del 3, encara que acabi en 3 (exercici 3).</li>
  </ul>
</div>''')

# ===================================================================== el document
cap = '''<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Unitat 2 · Els múltiples</title>
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
</head>
<body>
<!--
  FITXA · Unitat 2 · Divisibilitat · Els múltiples
  La primera fitxa de la unitat 2. Adapta les activitats 2_1 (múltiples) i 2_3
  (criteris de divisibilitat) del grup: els múltiples són la taula de la
  targeta; la graella de 100, com al grup; el truc de l'última xifra per al 2,
  el 5 i el 10, i el truc del 3, sumant les xifres (decisió del docent del
  25/9/2026: la suma dona directament de l'1 al 30). Sense calculadora.

  Els casos són els de la tasca 5 de la caixa (regla 8): els múltiples del 2
  de la 5.1, el 126 de la 5.3 i els nombres de la 5.4. Els de l'exercici 5 són
  els de la taula de l'activitat 2_3 del grup.

  La regla trencada és «un múltiple del 3 acaba en 3» (exercici 3). La pàgina
  acaba amb la forma bona a la vista.

  Cada bloc .full acaba amb un </div> a principi de línia; els de dins van
  sagnats. Les regles són a docs/CRITERIS-DISSENY.md. Després de canviar
  res: eines/mesura.py, generadors/gen_pdf.py i eines/comprova.py.
-->

'''
html = cap + "\n\n".join(pagines) + "\n\n</body>\n</html>\n"
sortida = sys.argv[1] if len(sys.argv) > 1 else "ud2.html"
open(sortida, "w", encoding="utf-8").write(html)
print(sortida, len(pagines), "blocs")
