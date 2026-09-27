#!/usr/bin/env python3
"""Genera l'esborrany de 1eso/fitxes/ud1.html: rectangles i quadrats.

Els dibuixos es fan aquí perquè tots els quadrets tinguin la mateixa mida i el
mateix aire, com a la caixa d'eines. El resultat és un HTML de paper normal.
"""
import sys

CM = 37.795            # píxels CSS per centímetre
NEGRE, G1, G2, G3 = "#000", "#333", "#5E5E5E", "#8A8A8A"
VORA_SUAU, F1, F2, F3, F4 = "#BFBFBF", "#F2F2F2", "#E4E4E4", "#D4D4D4", "#C4C4C4"
MS = "#3A3A3A"         # la tinta de la lletra manuscrita


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


class Dibuix:
    """Un SVG amb mides en centímetres. Tot es dibuixa en cm i es passa a px."""

    def __init__(self, amp, alt, aria, estil=""):
        self.amp, self.alt, self.aria, self.estil = amp, alt, aria, estil
        self.el = []

    def px(self, v):
        return f(v * CM)

    def quadret(self, x, y, m, fons=F3, traç=NEGRE, gruix=1.6, discontinu=False, aire=0.1):
        a = m * aire
        d = ' stroke-dasharray="4 3"' if discontinu else ""
        self.el.append(f'<rect x="{self.px(x + a / 2)}" y="{self.px(y + a / 2)}" width="{self.px(m - a)}" '
                       f'height="{self.px(m - a)}" rx="{self.px(m * 0.13)}" fill="{fons}" stroke="{traç}" '
                       f'stroke-width="{gruix}"{d}/>')

    def rectangle(self, x, y, files, cols, m, **k):
        for fi in range(files):
            for c in range(cols):
                self.quadret(x + c * m, y + fi * m, m, **k)

    def graella(self, x, y, files, cols, m):
        """La quadrícula buida per pintar-hi a mà."""
        self.el.append(f'<rect x="{self.px(x)}" y="{self.px(y)}" width="{self.px(cols * m)}" '
                       f'height="{self.px(files * m)}" fill="#fff" stroke="{G2}" stroke-width="1.6"/>')
        for fi in range(1, files):
            self.el.append(f'<line x1="{self.px(x)}" y1="{self.px(y + fi * m)}" x2="{self.px(x + cols * m)}" '
                           f'y2="{self.px(y + fi * m)}" stroke="{G3}" stroke-width="1"/>')
        for c in range(1, cols):
            self.el.append(f'<line x1="{self.px(x + c * m)}" y1="{self.px(y)}" x2="{self.px(x + c * m)}" '
                           f'y2="{self.px(y + files * m)}" stroke="{G3}" stroke-width="1"/>')

    def pintat(self, x, y, files, cols, m):
        """Un rectangle pintat a mà dins de la quadrícula: gris de llapis i la vora resseguida."""
        self.el.append(f'<rect x="{self.px(x)}" y="{self.px(y)}" width="{self.px(cols * m)}" '
                       f'height="{self.px(files * m)}" fill="{VORA_SUAU}" stroke="none"/>')
        for fi in range(1, files):
            self.el.append(f'<line x1="{self.px(x)}" y1="{self.px(y + fi * m)}" x2="{self.px(x + cols * m)}" '
                           f'y2="{self.px(y + fi * m)}" stroke="{G2}" stroke-width="1"/>')
        for c in range(1, cols):
            self.el.append(f'<line x1="{self.px(x + c * m)}" y1="{self.px(y)}" x2="{self.px(x + c * m)}" '
                           f'y2="{self.px(y + files * m)}" stroke="{G2}" stroke-width="1"/>')
        self.el.append(f'<rect x="{self.px(x)}" y="{self.px(y)}" width="{self.px(cols * m)}" '
                       f'height="{self.px(files * m)}" fill="none" stroke="{MS}" stroke-width="2.6" '
                       f'stroke-linejoin="round"/>')

    def text(self, x, y, t, mida=0.5, pes=400, ancora="middle", ma=False, color=NEGRE):
        """Un text. `mida` en cm. Amb ma=True, en lletra manuscrita."""
        estil = ' style="font-family:var(--manuscrita)"' if ma else ""
        c = MS if ma else color
        self.el.append(f'<text x="{self.px(x)}" y="{self.px(y)}" font-size="{self.px(mida)}" '
                       f'font-weight="{pes}" text-anchor="{ancora}" fill="{c}"{estil}>{t}</text>')

    def clau_dalt(self, x1, x2, y, t, mida=0.42):
        self.el.append(f'<path d="M{self.px(x1)} {self.px(y + 0.2)} V{self.px(y)} H{self.px(x2)} '
                       f'V{self.px(y + 0.2)}" fill="none" stroke="{G2}" stroke-width="1.6"/>')
        self.text((x1 + x2) / 2, y - 0.15, t, mida, color=G1)

    def clau_esq(self, x, y1, y2, t, mida=0.42):
        self.el.append(f'<path d="M{self.px(x + 0.2)} {self.px(y1)} H{self.px(x)} V{self.px(y2)} '
                       f'H{self.px(x + 0.2)}" fill="none" stroke="{G2}" stroke-width="1.6"/>')
        self.text(x - 0.15, (y1 + y2) / 2 + mida * 0.35, t, mida, ancora="end", color=G1)

    def cercle_ma(self, cx, cy, rx, ry):
        """Un encerclat fet a mà al voltant d'un dibuix."""
        self.el.append(f'<ellipse cx="{self.px(cx)}" cy="{self.px(cy)}" rx="{self.px(rx)}" ry="{self.px(ry)}" '
                       f'fill="none" stroke="{MS}" stroke-width="3" transform="rotate(-4 {self.px(cx)} '
                       f'{self.px(cy)})"/>')

    def cru(self, s):
        self.el.append(s)

    def svg(self, sagnat="    "):
        cap = (f'<svg viewBox="0 0 {self.px(self.amp)} {self.px(self.alt)}" '
               f'style="width:{f(self.amp)}cm;max-width:100%;margin:0 auto;{self.estil}" '
               f'role="img" aria-label="{self.aria}">')
        return sagnat + cap + "\n" + "\n".join(sagnat + "  " + e for e in self.el) + "\n" + sagnat + "</svg>"


def rect_sol(files, cols, m, aria, marge=0.1):
    d = Dibuix(cols * m + 2 * marge, files * m + 2 * marge, aria)
    d.rectangle(marge, marge, files, cols, m)
    return d


def graella_per_pintar(files, cols, m, aria, pinta=None):
    d = Dibuix(cols * m + 0.1, files * m + 0.1, aria)
    d.graella(0.05, 0.05, files, cols, m)
    if pinta:
        d.pintat(0.05, 0.05, pinta[0], pinta[1], m)
    return d


ULL = ('<svg class="ull" viewBox="0 0 48 48" aria-hidden="true"><path d="M3 24s8-13 21-13 21 13 21 13-8 '
       '13-21 13S3 24 3 24z" fill="#F2F2F2" stroke="#000" stroke-width="3" stroke-linejoin="round"/>'
       '<circle cx="24" cy="24" r="7" fill="#000"/></svg>')


def ms(t):
    return f'<span class="ms">{t}</span>'


def buit():
    return "<u></u>"


def buit_curt():
    """Un buit per a un número d'una o dues xifres: prou llarg per escriure-hi a mà,
    i prou curt perquè la frase no es parteixi en dues línies."""
    return '<u style="padding:0 1.1rem"></u>'


pagines = []


def pagina(cos, classe="full", peu=True):
    n = len([p for p in pagines if p[1]]) + 1
    peu_html = f'\n  <div class="pag">Unitat 1 · pàgina {n}</div>' if peu else ""
    pagines.append((f'<div class="{classe}">\n{cos.rstrip()}{peu_html}\n</div>', peu))


# ===================================================================== pàgina 1
d = Dibuix(8.2, 6.2, "Un rectangle de 3 files de 4 quadrets")
d.rectangle(0.1, 0.1, 3, 4, 2.0)
pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>miniblocs</b>. Fer el rectangle de 3 per 4 i comptar-ne els quadrets.</div>
  <h1>Rectangles de quadrets</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div class="figura neta" style="margin-top:1.1rem">
{d.svg()}
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.5rem 0 1rem">És un rectangle de quadrets.</p>

  <table>
    <tr class="resolt"><td class="esq">Quantes files hi ha?</td><td style="width:4cm">{ms("3")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets té cada fila?</td><td>{ms("4")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets hi ha en total?</td><td>{ms("12")}</td></tr>
  </table>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">3 files de 4 quadrets són 12 quadrets.</p>
    <p style="font-size:30pt;font-weight:800;margin:.3rem 0">3 · 4 = 12</p>
    <p style="margin:0">Es llegeix: 3 per 4.</p>
  </div>''')

# ===================================================================== pàgina 2
m = 0.85
dib = []
for lletra, (fi, co) in zip("abcd", [(3, 4), (2, 5), (5, 3), (2, 7)]):
    dd = rect_sol(fi, co, m, f"Apartat {lletra}: un rectangle de quadrets")
    dib.append((lletra, dd))
cel = "\n".join(f'''      <div style="text-align:center">
        <p class="apartat" style="margin:0 0 .2rem">{l})</p>
{dd.svg("        ")}
      </div>''' for l, dd in dib)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Mira cada rectangle. Omple la taula.</div></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.5cm .8cm;align-items:end;margin:.6rem 0 1rem">
{cel}
    </div>
    <table>
      <tr><th></th><th>Files</th><th>Quadrets a cada fila</th><th>Quadrets en total</th><th>La multiplicació</th></tr>
      <tr class="resolt"><td class="apartat">a)</td><td>{ms("3")}</td><td>{ms("4")}</td><td>{ms("12")}</td><td>{ms("3 · 4 = 12")}</td></tr>
      <tr><td class="apartat">b)</td><td class="omplir"></td><td class="omplir"></td><td class="omplir"></td><td class="omplir"></td></tr>
      <tr><td class="apartat">c)</td><td class="omplir"></td><td class="omplir"></td><td class="omplir"></td><td class="omplir"></td></tr>
      <tr><td class="apartat">d)</td><td class="omplir"></td><td class="omplir"></td><td class="omplir"></td><td class="omplir"></td></tr>
    </table>
  </div>

  <div class="avis puntejat">Comprova els resultats a la targeta de les taules.</div>''')

# ===================================================================== pàgina 3
m = 0.75
caselles = []
for lletra, (fi, co), resolt in [("a", (3, 4), True), ("b", (6, 2), False), ("c", (4, 5), False), ("d", (2, 8), False)]:
    g = graella_per_pintar(7, 9, m, f"Apartat {lletra}: una quadrícula per pintar el rectangle de {fi} · {co}",
                           pinta=(fi, co) if resolt else None)
    total = ms(str(fi * co)) if resolt else ""
    caselles.append(f'''      <div>
        <p style="margin:0 0 .25rem;font-size:16pt;font-weight:700"><span class="apartat">{lletra})</span> {fi} · {co}</p>
{g.svg("        ")}
        <div class="caixa-buida" style="margin-top:.35rem"><div class="et">Quadrets en total</div><div class="q" style="height:1.5cm;display:flex;align-items:center;justify-content:center">{total}</div></div>
      </div>''')
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">2</div><div class="q">Pinta el rectangle de cada multiplicació. Escriu quants quadrets hi ha.</div></div>
    <div class="duo" style="margin-top:.5rem">
{caselles[0]}
{caselles[1]}
    </div>
    <div class="duo" style="margin-top:.9rem">
{caselles[2]}
{caselles[3]}
    </div>
  </div>

  <div class="avis puntejat">Comprova els resultats a la targeta de les taules.</div>''')

# ===================================================================== pàgina 4
def gira(fi, co, m, aria, resolt):
    amp = co * m + fi * m + 2.6
    alt = max(fi, co) * m + 0.3
    d = Dibuix(amp, alt, aria)
    y1 = (alt - fi * m) / 2
    d.rectangle(0.1, y1, fi, co, m)
    x2 = 0.1 + co * m + 2.3
    y2 = (alt - co * m) / 2
    d.rectangle(x2, y2, co, fi, m)
    xa, xb, yc = 0.1 + co * m + 0.35, x2 - 0.35, alt / 2
    d.cru(f'<path d="M{d.px(xa)} {d.px(yc)} Q{d.px((xa + xb) / 2)} {d.px(yc - 1.2)} {d.px(xb)} {d.px(yc)}" '
          f'fill="none" stroke="#000" stroke-width="3" stroke-linecap="round"/>')
    d.cru(f'<path d="M{d.px(xb - 0.35)} {d.px(yc - 0.28)} L{d.px(xb)} {d.px(yc)} L{d.px(xb - 0.05)} '
          f'{d.px(yc - 0.42)}" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" '
          f'stroke-linejoin="round"/>')
    d.text((xa + xb) / 2, yc - 0.75, "gira", 0.45, 700)
    return d, (0.1 + co * m / 2), (x2 + fi * m / 2)


g_a, ca1, ca2 = gira(3, 4, 0.7, "Un rectangle de 3 files de 4 quadrets i el mateix rectangle girat: 4 files de 3", True)
g_b, cb1, cb2 = gira(2, 5, 0.7, "Un rectangle de 2 files de 5 quadrets i el mateix rectangle girat: 5 files de 2", False)
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">Gira el rectangle. Compta els quadrets.</div></div>

    <p class="apartat" style="margin:.4rem 0 .1rem">a)</p>
    <div class="resolt" style="border-radius:10px;padding:.4rem .6rem">
{g_a.svg("      ")}
      <div style="display:flex;justify-content:space-around;font-size:16.5pt;margin-top:.3rem">
        <p style="margin:0">{ms("3 · 4 = 12 quadrets")}</p>
        <p style="margin:0">{ms("4 · 3 = 12 quadrets")}</p>
      </div>
      <p style="text-align:center;margin:.3rem 0 0;font-weight:700">Hi ha els mateixos quadrets.</p>
    </div>

    <p class="apartat" style="margin:1rem 0 .1rem">b)</p>
{g_b.svg("    ")}
    <div style="display:flex;justify-content:space-around">
      <p class="frase" style="margin:0">2 · 5 = {buit()} quadrets</p>
      <p class="frase" style="margin:0">5 · 2 = {buit()} quadrets</p>
    </div>
  </div>

  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Fes servir el que ja saps.</div></div>
    <div class="duo">
      <div>
        <p style="margin:0"><span class="apartat">a)</span> Saps que 7 · 8 = 56.</p>
        <p class="frase" style="margin:.2rem 0">8 · 7 = {ms("56")}</p>
      </div>
      <div>
        <p style="margin:0"><span class="apartat">b)</span> Saps que 6 · 9 = 54.</p>
        <p class="frase" style="margin:.2rem 0">9 · 6 = {buit()}</p>
      </div>
    </div>
  </div>

  <div class="avis gruixut" style="text-align:center;font-weight:700">Si gires el rectangle, els quadrets no canvien.</div>''')

# ===================================================================== pàgina 5
def parteix(fi, n, m, aria, separat):
    u = n - 10
    gap = 0.45 if separat else 0
    amp = n * m + gap + 0.3
    alt = fi * m + 0.35
    d = Dibuix(amp, alt, aria)
    d.rectangle(0.1, 0.1, fi, 10, m)
    d.rectangle(0.1 + 10 * m + gap, 0.1, fi, u, m, fons="#fff")
    if not separat:
        x = 0.1 + 10 * m
        d.cru(f'<line x1="{d.px(x)}" y1="{d.px(0)}" x2="{d.px(x)}" y2="{d.px(0.2 + fi * m)}" stroke="#000" '
              f'stroke-width="2.6" stroke-dasharray="6 4"/>')
    return d


p_a = parteix(3, 12, 0.46, "Un rectangle de 3 files de 12 quadrets, partit en 3 files de 10 i 3 files de 2", True)
p_b = parteix(4, 13, 0.46, "Un rectangle de 4 files de 13 quadrets, amb una ratlla després del quadret 10", False)
p_c = parteix(2, 14, 0.46, "Un rectangle de 2 files de 14 quadrets, amb una ratlla després del quadret 10", False)
def passos(a, u, resolt):
    """Els quatre passos, un per línia i amb el rètol davant: així cap buit no queda
    enganxat a l'operació següent."""
    if resolt:
        linies = [("La part de 10", ms(f"{a} · 10 = {a * 10} quadrets")),
                  ("La part petita", ms(f"{a} · {u} = {a * u} quadrets")),
                  ("Ajunta-les", ms(f"{a * 10} + {a * u} = {a * (10 + u)}")),
                  ("El resultat", ms(f"{a} · {10 + u} = {a * (10 + u)}"))]
    else:
        linies = [("La part de 10", f"{a} · 10 = {buit_curt()} quadrets"),
                  ("La part petita", f"{a} · {u} = {buit_curt()} quadrets"),
                  ("Ajunta-les", f"{buit_curt()} + {buit_curt()} = {buit_curt()}"),
                  ("El resultat", f"{a} · {10 + u} = {buit_curt()}")]
    return "\n".join(f'        <p class="frase" style="margin:0;font-size:14.5pt;line-height:1.95;white-space:nowrap"><span style="font-size:12pt;color:var(--gris-2)">{et}:</span> {v}</p>'
                     for et, v in linies)


def apartat5(lletra, titol, dib, a, u, resolt):
    fons = ' class="resolt" style="border-radius:10px;padding:.35rem .5rem;margin-bottom:.5rem"' if resolt else ' style="padding:.35rem .5rem;margin-bottom:.5rem"'
    return f'''    <div{fons}>
      <p class="apartat" style="margin:0 0 .2rem">{lletra}) {titol}</p>
      <div style="display:flex;gap:.8cm;align-items:center">
        <div style="flex:0 0 auto">
{dib.svg("          ")}
        </div>
        <div>
{passos(a, u, resolt)}
        </div>
      </div>
    </div>'''


pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">5</div><div class="q">Parteix el rectangle pel 10. Després ajunta les dues parts.</div></div>
    <p style="margin:.1rem 0 .5rem">La targeta arriba fins al 10.</p>
{apartat5("a", "3 · 12", p_a, 3, 2, True)}
{apartat5("b", "4 · 13", p_b, 4, 3, False)}
{apartat5("c", "2 · 14", p_c, 2, 4, False)}
  </div>''')

# ===================================================================== pàgina 6
d = Dibuix(6.3, 4.3, "Un quadrat de 3 files de 3 quadrets")
d.rectangle(2.9, 1.0, 3, 3, 1.0)
d.clau_dalt(2.9, 2.9 + 3.0, 0.75, "3 quadrets")
d.clau_esq(2.7, 1.0, 1.0 + 3.0, "3 quadrets")
q_caselles = []
for lletra, n, resolt in [("a", 2, True), ("b", 4, False), ("c", 5, False)]:
    g = graella_per_pintar(6, 6, 0.55, f"Apartat {lletra}: una quadrícula per pintar el quadrat de {n}",
                           pinta=(n, n) if resolt else None)
    if resolt:
        res = (f'<p class="frase" style="margin:.1rem 0;font-size:15pt;white-space:nowrap">{ms(f"{n} · {n} = {n * n}")}</p>\n'
               f'        <p class="frase" style="margin:0;font-size:15pt;white-space:nowrap">Més curt: {ms(f"{n}² = {n * n}")}</p>')
    else:
        res = (f'<p class="frase" style="margin:.1rem 0;font-size:15pt;white-space:nowrap">{n} · {n} = {buit_curt()}</p>\n'
               f'        <p class="frase" style="margin:0;font-size:15pt;white-space:nowrap">Més curt: {n}² = {buit_curt()}</p>')
    q_caselles.append(f'''      <div style="text-align:center">
        <p style="margin:0 0 .2rem;font-size:16pt;font-weight:700"><span class="apartat">{lletra})</span> {n}²</p>
{g.svg("        ")}
        {res}
      </div>''')
pagina(f'''  <h2>El quadrat d'un nombre</h2>
  <div class="figura neta">
{d.svg()}
  </div>
  <div style="text-align:center">
    <p style="margin:.2rem 0 0">3 files de 3 quadrets.</p>
    <p style="margin:0">En total, 9 quadrets.</p>
    <p style="font-size:26pt;font-weight:800;margin:.1rem 0 .3rem">3 · 3 = 9</p>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0">Ho escrivim més curt:</p>
    <p style="font-size:30pt;font-weight:800;margin:.1rem 0">3² = 9</p>
    <p style="margin:0">Es llegeix: 3 al quadrat.</p>
  </div>

  <div class="exercici">
    <div class="tasca"><div class="n">6</div><div class="q">Pinta el quadrat. Escriu quants quadrets hi ha.</div></div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:.5cm">
{chr(10).join(q_caselles)}
    </div>
  </div>''')

# ===================================================================== pàgina 7
def opcio(n, cols, m, encerclat, aria):
    """Un dibuix d'opció: n files de cols quadrets. Tots a la mateixa escala."""
    d = Dibuix(5 * m + 0.9, n * m + 0.5, aria)
    x0 = (d.amp - cols * m) / 2
    d.rectangle(x0, 0.25, n, cols, m)
    if encerclat:
        d.cercle_ma(d.amp / 2, 0.25 + n * m / 2, cols * m / 2 + 0.32, n * m / 2 + 0.2)
    return d


def parella(lletra, titol, n, quadrat_primer, marca, resolt, m=0.62):
    ordre = ["q", "r"] if quadrat_primer else ["r", "q"]
    cols = []
    for t in ordre:
        c = n if t == "q" else 2
        dd = opcio(n, c, m, marca == t, f"{n} files de {c} quadrets")
        compte = ms(str(n * c)) if resolt else buit()
        cols.append(f'''        <div style="text-align:center">
{dd.svg("          ")}
          <p class="frase" style="margin:.1rem 0 0;font-size:15pt">Quadrets: {compte}</p>
        </div>''')
    fons = ' class="resolt" style="border-radius:10px;padding:.3rem .5rem"' if resolt else ""
    return f'''    <p style="margin:.7rem 0 .1rem;font-size:17pt;font-weight:800"><span class="apartat">{lletra})</span> {titol}</p>
    <div{fons}>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:.6cm;align-items:end">
{chr(10).join(cols)}
      </div>
    </div>'''


pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">7</div><div class="q">Marca el dibuix de cada operació. Compta els quadrets dels dos dibuixos.</div></div>
{parella("a", "3²", 3, True, "q", True)}
{parella("b", "4²", 4, False, None, False)}
{parella("c", "5 · 2", 5, True, None, False)}
  </div>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">3² vol dir 3 · 3 = 9. És un quadrat.</p>
    <p style="margin:.2rem 0 0">3 · 2 = 6 és un rectangle de 3 files de 2.</p>
  </div>''')

# ===================================================================== pàgina 8
def arrel_exacta(n, resolt, lletra):
    k = int(n ** 0.5)
    g = graella_per_pintar(6, 6, 0.55, f"Apartat {lletra}: una quadrícula per fer el quadrat amb {n} quadrets",
                           pinta=(k, k) if resolt else None)
    if resolt:
        res = (f'<p style="margin:.2rem 0 0;font-size:14pt;line-height:1.8">Costat: {ms(str(k))} quadrets</p>'
               f'<p class="frase" style="margin:0">√{n} = {ms(str(k))}</p>')
    else:
        res = (f'<p class="frase" style="margin:.2rem 0 0;font-size:14pt;line-height:1.8">Costat: {buit_curt()} quadrets</p>'
               f'<p class="frase" style="margin:0">√{n} = {buit_curt()}</p>')
    return f'''      <div style="text-align:center">
        <p style="margin:0 0 .2rem;font-size:16pt;font-weight:700"><span class="apartat">{lletra})</span> {n} quadrets</p>
{g.svg("        ")}
        {res}
      </div>'''


def entre(n, m, aria):
    k = int(n ** 0.5)
    sob = n - k * k
    d = Dibuix((k + 1) * m + 0.2, (k + 1) * m + 0.2, aria)
    d.rectangle(0.1, 0.1, k, k, m)
    vora = [(fi, k) for fi in range(k)] + [(k, c) for c in range(k, -1, -1)]
    for i, (fi, c) in enumerate(vora):
        if i < sob:
            d.quadret(0.1 + c * m, 0.1 + fi * m, m, fons="#fff")
        else:
            d.quadret(0.1 + c * m, 0.1 + fi * m, m, fons="none", traç=G2, gruix=1.4, discontinu=True)
    return d


e13 = entre(13, 0.6, "13 quadrets: un quadrat de 3 per 3, 4 quadrets de més i 3 llocs buits per fer el de 4 per 4")
e20 = entre(20, 0.55, "20 quadrets: un quadrat de 4 per 4, 4 quadrets de més i 5 llocs buits per fer el de 5 per 5")
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">8</div><div class="q">Fes un quadrat amb els quadrets. Escriu quants quadrets té el costat.</div></div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:.5cm">
{arrel_exacta(16, True, "a")}
{arrel_exacta(9, False, "b")}
{arrel_exacta(25, False, "c")}
    </div>
    <p style="margin:.6rem 0 0;font-size:13pt;color:var(--gris-2)">√16 es llegeix: l'arrel quadrada de 16.</p>
  </div>

  <div class="exercici">
    <div class="tasca"><div class="n">9</div><div class="q">Hi ha quadrets que no fan cap quadrat. Mira el dibuix.</div></div>
    <div class="resolt" style="border-radius:10px;padding:.35rem .6rem;margin-bottom:.5rem">
      <p style="margin:0 0 .2rem;font-weight:700"><span class="apartat">a)</span> 13 quadrets</p>
      <div style="display:flex;gap:.9cm;align-items:center">
        <div style="flex:0 0 auto">
{e13.svg("          ")}
        </div>
        <div>
          <p style="margin:0;font-size:14pt;line-height:1.9">El quadrat de 3 per 3 té {ms("9")} quadrets.</p>
          <p style="margin:0;font-size:14pt;line-height:1.9">El quadrat de 4 per 4 té {ms("16")} quadrets.</p>
          <p style="margin:0;font-size:14pt;line-height:1.9">L'arrel de 13 és entre {ms("3")} i {ms("4")}.</p>
        </div>
      </div>
    </div>
    <div style="padding:.35rem .6rem">
      <p style="margin:0 0 .2rem;font-weight:700"><span class="apartat">b)</span> 20 quadrets</p>
      <div style="display:flex;gap:.9cm;align-items:center">
        <div style="flex:0 0 auto">
{e20.svg("          ")}
        </div>
        <div>
          <p class="frase" style="margin:0;font-size:14pt;line-height:1.9">El quadrat de 4 per 4 té {buit_curt()} quadrets.</p>
          <p class="frase" style="margin:0;font-size:14pt;line-height:1.9">El quadrat de 5 per 5 té {buit_curt()} quadrets.</p>
          <p class="frase" style="margin:0;font-size:14pt;line-height:1.9">L'arrel de 20 és entre {buit_curt()} i {buit_curt()}.</p>
        </div>
      </div>
    </div>
  </div>''')

# ===================================================================== pàgina 9: la vida
def xocolata():
    d = Dibuix(7.2, 5.0, "Una rajola de xocolata de 3 files de 4 trossos")
    d.cru(f'<rect x="{d.px(0.1)}" y="{d.px(0.1)}" width="{d.px(7.0)}" height="{d.px(4.8)}" rx="{d.px(0.35)}" '
          f'fill="{F2}" stroke="{G1}" stroke-width="2.4"/>')
    for fi in range(3):
        for c in range(4):
            x, y = 0.45 + c * 1.6, 0.45 + fi * 1.4
            d.cru(f'<rect x="{d.px(x)}" y="{d.px(y)}" width="{d.px(1.4)}" height="{d.px(1.2)}" rx="{d.px(0.18)}" '
                  f'fill="{G3}" stroke="{G1}" stroke-width="1.6"/>')
            d.cru(f'<rect x="{d.px(x + 0.18)}" y="{d.px(y + 0.16)}" width="{d.px(1.04)}" height="{d.px(0.88)}" '
                  f'rx="{d.px(0.12)}" fill="none" stroke="{F3}" stroke-width="1.2"/>')
    return d


def ous():
    d = Dibuix(8.6, 3.4, "Un cartró d'ous de 2 files de 6 ous")
    d.cru(f'<rect x="{d.px(0.1)}" y="{d.px(0.1)}" width="{d.px(8.4)}" height="{d.px(3.2)}" rx="{d.px(0.3)}" '
          f'fill="{F2}" stroke="{G1}" stroke-width="2.4"/>')
    for fi in range(2):
        for c in range(6):
            cx, cy = 0.95 + c * 1.35, 0.95 + fi * 1.5
            d.cru(f'<ellipse cx="{d.px(cx)}" cy="{d.px(cy)}" rx="{d.px(0.5)}" ry="{d.px(0.62)}" fill="#fff" '
                  f'stroke="{G1}" stroke-width="1.8"/>')
    return d


def rajoles(n, aria):
    m = 0.75
    d = Dibuix(n * m + 0.2, n * m + 0.2, aria)
    for fi in range(n):
        for c in range(n):
            d.cru(f'<rect x="{d.px(0.1 + c * m)}" y="{d.px(0.1 + fi * m)}" width="{d.px(m)}" height="{d.px(m)}" '
                  f'fill="{F2 if (fi + c) % 2 else "#fff"}" stroke="{G2}" stroke-width="1.4"/>')
    d.cru(f'<rect x="{d.px(0.1)}" y="{d.px(0.1)}" width="{d.px(n * m)}" height="{d.px(n * m)}" fill="none" '
          f'stroke="{G1}" stroke-width="2.6"/>')
    return d


pagina(f'''  <h2>A la vida de cada dia</h2>

  <div class="exercici">
    <div class="tasca"><div class="n">10</div><div class="q">Quants n'hi ha?</div></div>
    <div class="duo">
      <div class="resolt" style="border-radius:10px;padding:.4rem .6rem">
        <p style="margin:0"><span class="apartat">a)</span> La rajola té 3 files de 4 trossos.</p>
{xocolata().svg("        ")}
        <p class="frase" style="margin:.2rem 0 0">{ms("3 · 4 = 12 trossos")}</p>
      </div>
      <div style="padding:.4rem .6rem">
        <p style="margin:0"><span class="apartat">b)</span> El cartró té 2 files de 6 ous.</p>
{ous().svg("        ")}
        <p class="frase" style="margin:.2rem 0 0">Hi ha {buit()} ous.</p>
      </div>
    </div>
  </div>

  <div class="exercici">
    <div class="tasca"><div class="n">11</div><div class="q">Les rajoles d'un terra quadrat.</div></div>
    <div class="duo">
      <div class="resolt" style="border-radius:10px;padding:.4rem .6rem">
        <p style="margin:0"><span class="apartat">a)</span> Cada costat té 4 rajoles. Quantes rajoles hi ha?</p>
{rajoles(4, "Un terra quadrat de 4 rajoles per 4 rajoles").svg("        ")}
        <p class="frase" style="margin:.2rem 0 0">{ms("4² = 16 rajoles")}</p>
      </div>
      <div style="padding:.4rem .6rem">
        <p style="margin:0"><span class="apartat">b)</span> Un altre terra quadrat té 25 rajoles. Quantes rajoles té cada costat?</p>
        <div class="caixa-buida" style="margin-top:.6rem"><div class="et">Rajoles de cada costat</div><div class="q"></div></div>
        <p style="margin:.6rem 0 0;font-size:13pt;color:var(--gris-2)">Pots fer el quadrat amb miniblocs.</p>
      </div>
    </div>
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append(('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 1 · Rectangles de quadrets · full per al professorat</p>

  <div class="abans">
    <b>Abans de començar.</b> La targeta de les taules és al davant tota l'estona, i els miniblocs, a
    mà. Es diu sempre igual: «files» i «quadrets a cada fila». Primer es mira el dibuix, després es
    diu amb paraules, i el símbol s'escriu al final. Demaneu que ho digui en veu alta abans
    d'escriure-ho: «3 files de 4 quadrets». Si no es recorda una multiplicació, es busca a la
    targeta: no és un error, és el que s'ha de fer.
  </div>

  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb miniblocs: fer el rectangle de 3 files de 4 i comptar els quadrets d'un en
  un, amb el dit. Després, girar-lo sobre la taula i tornar-los a comptar. La pàgina 1 és aquest
  mateix rectangle dibuixat. A la pregunta d'obertura es respon mirant i dient, no escrivint.</p>

  <h3>1. Mira cada rectangle</h3>
  <table>
    <tr><th></th><th>Files</th><th>Quadrets a cada fila</th><th>Quadrets en total</th><th>La multiplicació</th></tr>
    <tr><td>b)</td><td>2</td><td>5</td><td>10</td><td>2 · 5 = 10</td></tr>
    <tr><td>c)</td><td>5</td><td>3</td><td>15</td><td>5 · 3 = 15</td></tr>
    <tr><td>d)</td><td>2</td><td>7</td><td>14</td><td>2 · 7 = 14</td></tr>
  </table>
  <p><b>Error típic:</b> comptar malament els quadrets de la fila. Que els compti amb el dit, fila per
  fila. Si posa les files i els quadrets al revés (3 i 5 a l'apartat c), el total és el mateix: no
  és un error greu, però demaneu-li que ho digui amb el dit al dibuix.</p>

  <h3>2. Pinta el rectangle</h3>
  <p>b) 6 · 2 = 12; c) 4 · 5 = 20; d) 2 · 8 = 16. <b>Es dona per bo el rectangle girat</b>: 2 files
  de 6 per a 6 · 2 té els mateixos quadrets. El que compta és que el rectangle tingui les dues
  mides i el total sigui bo.</p>

  <h3>3 i 4. Gira el rectangle</h3>
  <p>3b) 2 · 5 = 10 i 5 · 2 = 10; 4b) 9 · 6 = 54. Es pot comprovar girant el full, o els miniblocs.
  Si busca 9 · 6 a la targeta, també està bé: és el que farà quan no la tingui clara.</p>
</div>''', False))

pagines.append(('''<div class="full sol">
  <h3>5. Parteix el rectangle pel 10</h3>
  <table>
    <tr><th></th><th>La part de 10</th><th>La part petita</th><th>Ajunta-les</th><th>El resultat</th></tr>
    <tr><td>b)</td><td>4 · 10 = 40</td><td>4 · 3 = 12</td><td>40 + 12 = 52</td><td>4 · 13 = 52</td></tr>
    <tr><td>c)</td><td>2 · 10 = 20</td><td>2 · 4 = 8</td><td>20 + 8 = 28</td><td>2 · 14 = 28</td></tr>
  </table>
  <p>Les dues sumes es fan sense portar-ne. La ratlla discontínua del dibuix marca on es parteix.
  Si li costa, que tapi amb la mà la part de 10 i compti només la part petita.</p>

  <h3>6. El quadrat d'un nombre</h3>
  <p>b) 4 · 4 = 16 i 4² = 16; c) 5 · 5 = 25 i 5² = 25. El 2 petit diu quantes vegades es
  multiplica el número per ell mateix: 3² és 3 · 3. Es llegeix «3 al quadrat».</p>

  <h3>7. Marca el dibuix de cada operació</h3>
  <p>b) 4²: el quadrat, amb 16 quadrets. El rectangle en té 8. c) 5 · 2: <b>el rectangle</b>, amb
  10 quadrets. El quadrat en té 25.</p>
  <p><b>Error típic:</b> dir que <span class="ratllat">3² = 6</span>, perquè fa 3 · 2. És la regla trencada d'aquesta fitxa.
  No l'expliqueu: feu comptar els quadrets dels dos dibuixos. El dibuix de 3² té 9 quadrets, i
  no és el de 6. L'apartat c pregunta pel rectangle a posta: si sempre marca el dibuix més gran,
  encara no mira el símbol. <b>Compta per als nivells alts, no per al mínim.</b></p>

  <h3>8. El costat del quadrat</h3>
  <p>b) 9 quadrets: el costat té 3 quadrets, √9 = 3. c) 25 quadrets: el costat té 5 quadrets,
  √25 = 5. Amb miniblocs es veu millor: es fan files fins que surt un quadrat.</p>

</div>''', False))

pagines.append(('''<div class="full sol">
  <h3>9. Quadrets que no fan cap quadrat</h3>
  <p>b) El quadrat de 4 per 4 té 16 quadrets. El de 5 per 5 en té 25. L'arrel de 20 és entre 4 i
  5. Al dibuix, els quadrets blancs són els que sobren, i els de traç discontinu, els que falten
  per fer el quadrat següent. <b>Nivells alts.</b></p>

  <h3>10 i 11. A la vida de cada dia</h3>
  <p>10b) 2 · 6 = 12 ous. 11b) 5 rajoles a cada costat, perquè 5 · 5 = 25. És la mateixa
  decisió que als exercicis 8 i 1: si el terra és quadrat, el costat és l'arrel.</p>

  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=1</b> (rectangles: fer-los,
  girar-los i partir-los) i <b style="white-space:nowrap">?task=2</b> (quadrats i arrels). Per a un
  sol exercici, sense poder passar als altres: <b style="white-space:nowrap">?task=1.2</b>.
  Les tasques tancades 1.2 i 2.2 donen un codi de
  verificació, que es llegeix a la pàgina de llegir codis. Els casos resolts de la fitxa són els
  mateixos que els exemples de la caixa: 3 · 4, 3 · 12, 3², 16 quadrets.</p>

  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la targeta al davant. Els criteris de la SA del grup (1.3, 2.1 i 8.1) són de
  referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Davant d'un rectangle dibuixat, diu en veu alta quantes files té i quants quadrets hi ha a cada fila: «3 files de 4 quadrets» (exercici 1).</li>
    <li>Diu quantes files i quants quadrets a cada fila té un rectangle, i n'escriu la multiplicació (exercicis 1 i 2).</li>
    <li>Fa amb miniblocs el rectangle d'una multiplicació de la targeta, en qualsevol posició (exercici 2).</li>
    <li>Gira un rectangle i diu que té els mateixos quadrets (exercicis 3 i 4).</li>
    <li>Parteix pel 10 un rectangle de més de 10 quadrets a cada fila, i en troba el total (exercici 5).</li>
    <li>Pinta el quadrat d'un nombre i l'escriu amb el 2 petit (exercici 6).</li>
    <li>Amb 16 quadrets fa el quadrat i diu que el costat té 4 quadrets (exercici 8).</li>
    <li>Nivells alts: tria el dibuix de 4² entre el quadrat i el rectangle de 4 per 2 (exercici 7), i diu entre quins dos nombres és l'arrel de 20 (exercici 9).</li>
  </ul>
</div>''', False))

# ===================================================================== el document
cap = '''<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Unitat 1 · Rectangles de quadrets</title>
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
</head>
<body>
<!--
  FITXA · Unitat 1 · Nombres naturals · Rectangles de quadrets
  Validada pel docent el 24 de setembre de 2026. De la unitat, de moment,
  només els rectangles i els quadrats: els nombres (centenes, desenes i
  unitats) i l'ordre de les operacions es treballen amb la caixa d'eines.

  Els dibuixos de quadrets tenen tots la mateixa mida de quadret per pàgina i
  el mateix aire entre quadrets, com a la caixa. Es poden retocar aquí mateix:
  cada <rect> és un quadret.

  El nucli: multiplicar és fer un rectangle de quadrets. 3 · 4 són 3 files de
  4 quadrets. 3² és un quadrat de 3 per 3, i l'arrel és el costat.

  Els casos resolts són els mateixos que els exemples de la caixa d'eines
  (regla 8): 3 · 4, 3 · 12, 3², 16 quadrets i 13 quadrets.

  Cada bloc .full acaba amb un </div> a principi de línia; els de dins van
  sagnats. Les regles són a docs/CRITERIS-DISSENY.md. Després de canviar
  res: eines/mesura.py, generadors/gen_pdf.py i eines/comprova.py.
-->

'''
html = cap + "\n\n".join(p for p, _ in pagines) + "\n\n</body>\n</html>\n"
sortida = sys.argv[1] if len(sys.argv) > 1 else "ud1.html"
open(sortida, "w", encoding="utf-8").write(html)
print(sortida, len(pagines), "blocs")
