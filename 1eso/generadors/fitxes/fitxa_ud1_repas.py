#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud1-repas.html: el repàs de la unitat 1 i «Què he après?».

És la quarta fitxa de la unitat 1. Adapta les activitats 1_1 i 1_3 (el número que
falta), 1_5 i 1_15 (el repàs: les multiplicacions mal fetes, una de cada) i 1_16
(«Què he après?») del grup. Fa servir les peces de dibuix de la primera fitxa.
"""
import os
import sys

from peces_comunes import *  # noqa: F401,F403  # Dibuix, ms, buit, buit_curt, ULL, colors…

PEU = "Unitat 1 · Repàs · pàgina"
pagines = []


def pagina(cos, classe="full"):
    n = len(pagines) + 1
    pagines.append(f'<div class="{classe}">\n{cos.rstrip()}\n  <div class="pag">{PEU} {n}</div>\n</div>')


def forat(dins=""):
    """El forat del número que falta: una caixa de traç discontinu, com a la caixa
    d'eines. A l'apartat resolt, porta el número escrit a mà."""
    return (f'<span style="display:inline-block;min-width:1.4cm;height:1.3cm;line-height:1.3cm;'
            f'border:2.5px dashed {G2};border-radius:8px;text-align:center;vertical-align:middle;'
            f'margin:0 .15rem">{dins}</span>')


def buit_op(cm=4.5):
    return f'<u style="display:inline-block;min-width:{cm}cm;padding:0"></u>'


# ===================================================================== pàgina 1
d = Dibuix(10.6, 4.9, "4 files de quadrets, amb un paper que en tapa una part. En total hi ha 24 quadrets")
m = 0.8
x0, y0 = 2.3, 1.2
d.rectangle(x0, y0, 4, 6, m)
d.clau_esq(x0 - 0.2, y0, y0 + 4 * m, "4 files")
d.clau_dalt(x0, x0 + 6 * m, y0 - 0.25, "24 quadrets en total")
# el paper que tapa les columnes 3 a 6
d.cru(f'<rect x="{d.px(x0 + 2 * m - 0.05)}" y="{d.px(y0 - 0.12)}" width="{d.px(4 * m + 0.35)}" '
      f'height="{d.px(4 * m + 0.24)}" rx="{d.px(0.12)}" fill="{F4}" stroke="{G1}" stroke-width="2.4" '
      f'transform="rotate(-2 {d.px(x0 + 4 * m)} {d.px(y0 + 2 * m)})"/>')
d.text(x0 + 4.2 * m, y0 + 2 * m + 0.3, "?", 0.95, 800, color=G1)
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs</b>. Posar 24 miniblocs en 4 files iguals i comptar els d'una fila.</div>
  <h1>Repàs de la unitat</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div class="figura neta" style="margin-top:1rem">
{d.svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.4rem 0 .8rem">Hi ha 24 quadrets en 4 files iguals. Un paper en tapa una part.</p>

  <table>
    <tr class="resolt"><td class="esq">Quantes files hi ha?</td><td style="width:4cm">{ms("4")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets hi ha en total?</td><td>{ms("24")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets té cada fila?</td><td>{ms("6")}</td></tr>
  </table>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">Busca la taula del 4 a la targeta.</p>
    <p style="margin:0">Baixa fins que surti el 24.</p>
    <p style="font-size:30pt;font-weight:800;margin:.3rem 0">4 · 6 = 24</p>
    <p style="margin:0;font-weight:700">El número que falta és el 6.</p>
  </div>''')

# ===================================================================== pàgina 2
# de la llista de la tasca 0.3 de la caixa: (primer, segon, on és el forat)
FALTA = [("a", 7, 8, "b", True), ("b", 6, 7, "b", False), ("c", 8, 4, "b", False), ("d", 3, 9, "b", False),
         ("e", 5, 4, "a", False), ("f", 7, 6, "a", False), ("g", 3, 8, "a", False), ("h", 4, 7, "a", False)]
caselles = []
for lletra, a, b, on, resolt in FALTA:
    x = a if on == "a" else b
    caixeta = forat(ms(str(x)) if resolt else "")   # no «f»: és la funció que escriu les mides
    expr = f"{caixeta} · {b} = {a * b}" if on == "a" else f"{a} · {caixeta} = {a * b}"
    fons = ' class="resolt"' if resolt else ""
    caselles.append(f'''      <div{fons} style="border-radius:10px;padding:.35rem .6rem">
        <p style="margin:0;font-size:22pt;font-weight:800;white-space:nowrap"><span class="apartat" style="font-size:14pt">{lletra})</span> {expr}</p>
      </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Busca el número que falta. Mira la targeta.</div></div>
    <div class="avis puntejat" style="margin:.3rem 0 .7rem">
      <p style="margin:0">Tria la taula del número que ja tens.</p>
      <p style="margin:0">Baixa fins que surti el resultat.</p>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.9rem .8cm">
{chr(10).join(caselles)}
    </div>
  </div>

  <div class="clau" style="margin-top:1.1rem">
    <p style="margin:0">Si el forat és al davant, gira el rectangle.</p>
    <p style="margin:0">{forat()} · 4 = 20 és el mateix que 4 · {forat()} = 20.</p>
  </div>''')

# ===================================================================== pàgina 3
# de l'activitat 1_15 del grup: cinc de bones i cinc de mal fetes
MAL = [("a", 7, 3, 12, True), ("b", 8, 8, 64, False), ("c", 9, 7, 81, False), ("d", 8, 5, 45, False),
       ("e", 3, 8, 24, False), ("f", 8, 4, 24, False), ("g", 6, 4, 24, False), ("h", 5, 5, 25, False),
       ("i", 9, 4, 36, False), ("j", 4, 4, 32, False)]
caselles3 = []
for lletra, a, b, r, resolt in MAL:
    expr = f'<span class="revisa">{a} · {b} = {r}</span>'
    if resolt:
        expr = f'<span class="encerclat" style="padding:.05rem .5rem">{expr}</span>'
        bo = ms(str(a * b))
    else:
        bo = buit_curt()
    fons = ' class="resolt"' if resolt else ""
    caselles3.append(f'''      <div{fons} style="border-radius:10px;padding:.3rem .6rem">
        <p class="frase" style="margin:0;font-size:20pt;font-weight:800;white-space:nowrap"><span class="apartat" style="font-size:14pt">{lletra})</span> {expr} <span style="font-size:14pt;font-weight:400;color:var(--gris-2)">Bé:</span> {bo}</p>
      </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Marca les multiplicacions mal fetes. Escriu el resultat bo al costat.</div></div>
    <div class="avis puntejat" style="margin:.3rem 0 .7rem">Mira cada una a la targeta. N'hi ha de bones i de mal fetes.</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.7rem .8cm">
{chr(10).join(caselles3)}
    </div>
  </div>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Si no ho saps segur, mira la targeta.</p>
    <p style="margin:.2rem 0 0">7 · 3 = 21: és a la taula del 7, a la fila 3.</p>
  </div>''')

# ===================================================================== pàgina 4
def apartat4(lletra, recorda, cos, resolt=False):
    fons = (' class="resolt" style="border-radius:10px;padding:.35rem .6rem;margin-bottom:.45rem"' if resolt
            else ' style="padding:.35rem .6rem;margin-bottom:.45rem"')
    return f'''    <div{fons}>
      <p style="margin:0;font-size:14pt;color:var(--gris-2)"><span class="apartat" style="color:var(--tinta)">{lletra})</span> {recorda}</p>
{cos}
    </div>'''


fr = lambda t, mida=17: f'      <p class="frase" style="margin:.05rem 0 0;font-size:{mida}pt">{t}</p>'
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Una de cada. Fes-les amb el que ja saps.</div></div>
{apartat4("a", "Si gires el rectangle, els quadrets no canvien.",
          fr("Saps que 6 · 8 = 48.") + chr(10) + fr("8 · 6 = " + ms("48")), True)}
{apartat4("b", "La targeta arriba fins al 10. Parteix el rectangle pel 10.",
          fr("4 · 12. La part de 10: 4 · 10 = " + buit_curt() + ". La part petita: 4 · 2 = " + buit_curt() + ".", 15) + chr(10) +
          fr("Ajunta-les: " + buit_curt() + " + " + buit_curt() + " = " + buit_curt() + ".", 15))}
{apartat4("c", "5² vol dir 5 · 5.", fr("5² = " + buit_curt()))}
{apartat4("d", "L'arrel és el costat del quadrat.", fr("√36 = " + buit_curt()))}
{apartat4("e", "El 0 també s'escriu.", fr("3 centenes, 0 desenes i 7 unitats: " + buit_curt(), 16))}
{apartat4("f", "Sense parèntesis, primer es multiplica.", fr("1 + 3 · 2 = " + buit_curt()))}
  </div>''')

# ===================================================================== pàgina 5: què he après?
FILES_QHA = [
    ("Busco una multiplicació a la targeta.", "7 · 8 = 56"),
    ("Busco el número que falta.", "7 · … = 56"),
    ("Faig el rectangle d'una multiplicació.", "3 · 4: 3 files de 4 quadrets"),
    ("Giro un rectangle.", "3 · 4 = 4 · 3: els quadrets no canvien"),
    ("Parteixo un rectangle pel 10.", "3 · 12 = 30 + 6"),
    ("Faig el quadrat d'un nombre.", "3² = 9"),
    ("Trobo el costat d'un quadrat.", "√16 = 4"),
    ("Faig un nombre amb blocs.", "2 centenes, 4 desenes i 3 unitats: 243"),
    ("Escric el nom d'un nombre.", "243: dos-cents quaranta-tres"),
    ("Sé què es fa primer.", "2 + 3 · 4 = 14"),
]
files_q = "\n".join(
    f'''      <tr><td class="esq" style="padding:.18rem .5rem;line-height:1.25">{frase}<br><span style="font-size:14pt;color:var(--gris-2)">{ex}</span></td>'''
    f'''<td><span class="quadret" style="margin:0"></span></td><td><span class="quadret" style="margin:0"></span></td>'''
    f'''<td><span class="quadret" style="margin:0"></span></td></tr>'''
    for frase, ex in FILES_QHA)
pagina(f'''  <h2>Què he après?</h2>
  <p style="margin:.1rem 0 0">Llegeix cada frase. Marca una casella.</p>
  <table class="mini" style="margin-top:.4rem">
    <tr><th style="text-align:left">Què sé fer</th><th style="width:2.5cm">Ho sé fer</th><th style="width:2.5cm">L'he de repassar</th><th style="width:2.5cm">Encara no</th></tr>
{files_q}
  </table>
  <p class="frase" style="margin:.6rem 0 0;font-size:15pt">El que m'ha agradat més: <u style="display:inline-block;min-width:9cm;padding:0"></u></p>
  <p class="frase" style="margin:0;font-size:15pt">El que m'ha costat més: <u style="display:inline-block;min-width:9.4cm;padding:0"></u></p>''')

# ===================================================================== pàgina 6: la vida
def cadira(d, x, y, s=0.46):
    d.cru(f'<rect x="{d.px(x + 0.06)}" y="{d.px(y)}" width="{d.px(s - 0.12)}" height="{d.px(s * 0.62)}" '
          f'rx="{d.px(0.05)}" fill="#fff" stroke="{G1}" stroke-width="1.6"/>')
    d.cru(f'<rect x="{d.px(x)}" y="{d.px(y + s * 0.62)}" width="{d.px(s)}" height="{d.px(s * 0.18)}" '
          f'fill="{G3}" stroke="{G1}" stroke-width="1.4"/>')
    for dx in (0.05, s - 0.05):
        d.cru(f'<line x1="{d.px(x + dx)}" y1="{d.px(y + s * 0.8)}" x2="{d.px(x + dx)}" y2="{d.px(y + s * 1.15)}" '
              f'stroke="{G1}" stroke-width="1.6"/>')


def files_iguals(n_files, per_fila, aria, dibuixa=True, cosa="cadira"):
    """n files iguals. Si no es dibuixa, surten només les files buides."""
    s = 0.6
    alt_f, pas = 0.8, 0.92
    amp_f = max(per_fila, 6) * (s + 0.2) + 0.4
    d = Dibuix(amp_f + 1.9, n_files * pas + 0.2, aria)
    for fi_ in range(n_files):
        y = 0.1 + fi_ * pas
        d.text(0.8, y + 0.56, f"fila {fi_ + 1}", 0.5, 400, color=G2)
        d.cru(f'<rect x="{d.px(1.65)}" y="{d.px(y)}" width="{d.px(amp_f)}" height="{d.px(alt_f)}" rx="{d.px(0.08)}" '
              f'fill="none" stroke="{G3}" stroke-width="1.2" stroke-dasharray="5 4"/>')
        if dibuixa:
            for k in range(per_fila):
                if cosa == "cadira":
                    cadira(d, 1.85 + k * (s + 0.2), y + 0.04, s)
                else:
                    x = 1.85 + k * (s + 0.2)
                    d.cru(f'<path d="M{d.px(x)} {d.px(y + 0.08)} H{d.px(x + s)} L{d.px(x + s - 0.07)} {d.px(y + 0.54)} '
                          f'H{d.px(x + 0.07)} Z" fill="#fff" stroke="{G1}" stroke-width="1.6"/>')
    return d


def capsa_ous(aria):
    d = Dibuix(2.3, 1.55, aria)
    d.cru(f'<rect x="{d.px(0.1)}" y="{d.px(0.1)}" width="{d.px(2.1)}" height="{d.px(1.35)}" rx="{d.px(0.15)}" '
          f'fill="{F2}" stroke="{G2}" stroke-width="1.4"/>')
    for fi_ in range(2):
        for co in range(3):
            d.cru(f'<ellipse cx="{d.px(0.52 + co * 0.62)}" cy="{d.px(0.45 + fi_ * 0.65)}" rx="{d.px(0.24)}" '
                  f'ry="{d.px(0.29)}" fill="#fff" stroke="{G1}" stroke-width="1.8"/>')
    return d


def capsa_llapis(aria):
    d = Dibuix(2.3, 1.55, aria)
    d.cru(f'<rect x="{d.px(0.1)}" y="{d.px(0.4)}" width="{d.px(2.1)}" height="{d.px(1.05)}" rx="{d.px(0.12)}" '
          f'fill="{F2}" stroke="{G2}" stroke-width="1.4"/>')
    for k in range(4):
        x = 0.35 + k * 0.47
        d.cru(f'<rect x="{d.px(x)}" y="{d.px(0.25)}" width="{d.px(0.26)}" height="{d.px(0.95)}" fill="#fff" '
              f'stroke="{G1}" stroke-width="1.4"/>')
        d.cru(f'<path d="M{d.px(x)} {d.px(0.25)} L{d.px(x + 0.13)} {d.px(0.02)} L{d.px(x + 0.26)} {d.px(0.25)} Z" '
              f'fill="{G3}" stroke="{G1}" stroke-width="1.2"/>')
    return d


pagina(f'''  <h2>A la vida de cada dia</h2>

  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Quants n'hi ha a cada fila? Mira la targeta.</div></div>
    <div class="duo">
      <div class="resolt" style="border-radius:10px;padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Hi ha 24 cadires en 4 files iguals.</p>
{files_iguals(4, 6, "4 files de 6 cadires").svg("        ")}
        <p class="frase" style="margin:.1rem 0 0">{ms("4 · 6 = 24")}.</p>
        <p class="frase" style="margin:0">A cada fila hi ha {ms("6")} cadires.</p>
      </div>
      <div style="padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Hi ha 30 gots en 5 files iguals.</p>
{files_iguals(5, 6, "5 files buides per als gots", dibuixa=False).svg("        ")}
        <p class="frase" style="margin:.1rem 0 0">5 · {buit_curt()} = 30.</p>
        <p class="frase" style="margin:0">A cada fila hi ha {buit_curt()} gots.</p>
      </div>
    </div>
  </div>

  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Quantes capses hi ha?</div></div>
    <div class="duo">
      <div class="resolt" style="border-radius:10px;padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">a)</span> Hi ha 42 ous. A cada capsa n'hi ha 6.</p>
{capsa_ous("Una capsa de 6 ous").svg("        ")}
        <p class="frase" style="margin:.1rem 0 0">{ms("7 · 6 = 42")}.</p>
        <p class="frase" style="margin:0">Hi ha {ms("7")} capses.</p>
      </div>
      <div style="padding:.4rem .6rem">
        <p style="margin:0 0 .2rem"><span class="apartat">b)</span> Hi ha 36 llapis. A cada capsa n'hi ha 4.</p>
{capsa_llapis("Una capsa de 4 llapis").svg("        ")}
        <p class="frase" style="margin:.1rem 0 0">{buit_curt()} · 4 = 36.</p>
        <p class="frase" style="margin:0">Hi ha {buit_curt()} capses.</p>
      </div>
    </div>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 1 · Repàs de la unitat · full per al professorat</p>

  <div class="abans">
    <b>Abans de començar.</b> És la fitxa de repàs: va després de les altres tres de la unitat. La
    targeta de les taules és al davant tota l'estona. La pàgina 5, «Què he après?», no es corregeix:
    serveix per parlar-ne, i per saber què s'ha de repassar abans de l'examen.
  </div>

  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs: posar 24 miniblocs en 4 files iguals, repartint-los d'un en un, i
  comptar els d'una fila: 6. Després, buscar a la targeta la taula del 4 i baixar fins al 24: 4 · 6
  = 24. El número que falta és el que diu quants n'hi ha a cada fila.</p>

  <h3>1. El número que falta</h3>
  <p>b) 6 · 7 = 42; c) 8 · 4 = 32; d) 3 · 9 = 27; e) 5 · 4 = 20; f) 7 · 6 = 42; g) 3 · 8 = 24;
  h) 4 · 7 = 28. <b>Error típic:</b> escriure el resultat en lloc del número que falta, o buscar-lo
  a la taula de l'altre número. Als apartats de l'e a l'h, el forat és al davant: es busca a la taula del número
  que es té, i surt el rectangle girat (4 · 5 = 20 per al forat de l'apartat e).</p>

  <h3>2. Les multiplicacions mal fetes</h3>
  <table>
    <tr><th>Mal fetes</th><th>El resultat bo</th><th>Ben fetes</th></tr>
    <tr><td>a) 7 · 3</td><td>7 · 3 = 21</td><td>b) 8 · 8 = 64</td></tr>
    <tr><td>c) 9 · 7</td><td>9 · 7 = 63</td><td>e) 3 · 8 = 24</td></tr>
    <tr><td>d) 8 · 5</td><td>8 · 5 = 40</td><td>g) 6 · 4 = 24</td></tr>
    <tr><td>f) 8 · 4</td><td>8 · 4 = 32</td><td>h) 5 · 5 = 25</td></tr>
    <tr><td>j) 4 · 4</td><td>4 · 4 = 16</td><td>i) 9 · 4 = 36</td></tr>
  </table>
  <p>Són les de l'activitat 1_15 del grup. <b>Error típic:</b> marcar-les totes, o cap, sense
  mirar-les. Cal comprovar-les una per una a la targeta: és el que es fa servir de debò quan un
  resultat no quadra.</p>

  <h3>3. Una de cada</h3>
  <p>b) 4 · 10 = 40 i 4 · 2 = 8; ajuntades, 40 + 8 = 48, i per tant 4 · 12 = 48. c) 5² = 25.
  d) √36 = 6. e) 307. f) 1 + 3 · 2 = 7. Cada apartat torna a una de les tres fitxes: si un no surt,
  aquella fitxa és la que cal repassar (vegeu la taula del full següent).</p>
</div>''')

pagines.append('''<div class="full sol">
  <h3>4 i 5. A la vida de cada dia</h3>
  <p>4b) 5 · 6 = 30: a cada fila hi ha 6 gots. 5b) 9 · 4 = 36: hi ha 9 capses. És el número que
  falta, en una situació de debò: quants n'hi ha a cada fila, o quantes capses. <b>Nivells
  alts.</b> Si li costa, que faci les files amb miniblocs, com al graó físic.</p>

  <h3>La pàgina 5: «Què he après?»</h3>
  <p>L'alumnat marca una casella a cada frase. L'adult tria dues frases de «Ho sé fer» i li demana
  que ho ensenyi amb un exemple: així la marca es converteix en una cosa que es veu. Les de
  «Encara no» diuen què s'ha de repassar, i on:</p>
  <table>
    <tr><th>Frase</th><th>On es repassa</th></tr>
    <tr><td>1 i 2 · la targeta, el número que falta</td><td>Caixa 0.1, 0.2 i 0.3; aquesta fitxa, exercici 1</td></tr>
    <tr><td>3 i 4 · el rectangle, girar-lo</td><td>Fitxa 1, exercicis 1 a 4; caixa 1.1, 1.2 i 1.3</td></tr>
    <tr><td>5 · partir pel 10</td><td>Fitxa 1, exercici 5; caixa 1.4</td></tr>
    <tr><td>6 i 7 · el quadrat, el costat</td><td>Fitxa 1, exercicis 6 a 9; caixa 2.1, 2.2 i 2.3</td></tr>
    <tr><td>8 i 9 · centenes, desenes i unitats, el nom</td><td>Fitxa 2; caixa 3.1 i 3.2</td></tr>
    <tr><td>10 · què es fa primer</td><td>Fitxa 3; caixa 4.1 i 4.2</td></tr>
  </table>
  <p>Tres columnes, i no les quatre de l'activitat 1_16 del grup, i frases que diuen què es fa, no
  el nom de la propietat. Amb l'ordinador, el número que falta és a
  <b style="white-space:nowrap">?task=0.3</b>, i totes les tasques tancades donen un codi.</p>

  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (1.3, 2.1 i 8.1) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb la targeta, troba el número que falta, també quan és el primer (exercici 1).</li>
    <li>Troba les multiplicacions mal fetes i en diu el resultat bo (exercici 2).</li>
    <li>Fa una operació de cada tipus de la unitat (exercici 3).</li>
    <li>Diu en veu alta què sap fer i què ha de repassar, i ho ensenya amb un exemple (pàgina 5).</li>
    <li>Nivells alts: troba quants n'hi ha a cada fila en una situació de debò (exercicis 4 i 5).</li>
  </ul>
</div>''')

# ===================================================================== el document
cap = '''<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Unitat 1 · Repàs de la unitat</title>
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
</head>
<body>
<!--
  FITXA · Unitat 1 · Nombres naturals · Repàs de la unitat
  La quarta fitxa de la unitat, i l'última abans de l'examen. Adapta les
  activitats 1_1 i 1_3 (el número que falta), 1_5 i 1_15 (el repàs) i 1_16
  («Què he après?») del grup. Els nombres grans, els milers i la propietat
  associativa de les activitats del grup queden fora (docs/MAPA-ADAPTACIO.md).

  El número que falta es busca a la targeta, com a la tasca 0.3 de la caixa,
  i els casos són els de la seva llista. Les multiplicacions mal fetes són les
  de l'activitat 1_15 del grup. Van dins de .revisa: poden ser falses a posta,
  i eines/comprova.py no les comprova. Les bones són al solucionari.

  Cada bloc .full acaba amb un </div> a principi de línia; els de dins van
  sagnats. Les regles són a docs/CRITERIS-DISSENY.md. Després de canviar
  res: eines/mesura.py, generadors/gen_pdf.py i eines/comprova.py.
-->

'''
html = cap + "\n\n".join(pagines) + "\n\n</body>\n</html>\n"
sortida = sys.argv[1] if len(sys.argv) > 1 else "ud1-repas.html"
desa(html, sortida)
print(sortida, len(pagines), "blocs")
