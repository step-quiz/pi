"""Genera les gràfiques de paràboles de la fitxa de la Unitat 5, en SVG i en
blanc i negre. Es dibuixen per càlcul i no a mà, perquè els vèrtexs, els talls
i les marques dels eixos caiguin exactament on toca."""

W, H = 560, 300
ML, MR = 54, 20

# La lletra dels rètols, en unitats del dibuix (560 d'ample). Al PDF, un gràfic
# d'amplada sencera fa uns 12,2 cm: 20 unitats hi són 12,4 pt. Abans eren 15
# (9,3 pt), i als dos gràfics de costat de les pàgines 3 i 9, 6,5 pt. Els que
# van de costat (8,5 cm) es criden amb fs=28. El mínim és 12 pt, i
# eines/auditoria.py el vigila (29/9/2026).
FS = 20


def marques(vmin, vmax, pas):
    """Els valors de les marques: els múltiples de `pas` que hi ha entre vmin i vmax.
    Abans es començava a comptar des de vmin: amb vmin = -0,5 les marques queien a
    -0,5, 0,5, 1,5… i, arrodonides, deien «-0, 0, 2, 2, 4, 4»; amb vmin = -0,4 cada
    número quedava desplaçat respecte del seu lloc (29/9/2026)."""
    import math
    k = math.ceil(vmin / pas - 1e-9)
    out = []
    while k * pas <= vmax + 1e-9:
        out.append(round(k * pas, 10))
        k += 1
    return out


def rotul(x, y, text, fs, ancora="middle", gruix=400, color="#5E5E5E"):
    """Un rètol amb un halo blanc a sota: el mateix text, en blanc i amb un traç gruixut.
    Així es llegeix encara que la corba o una línia de la graella hi passin per sobre.
    No fa servir paint-order: el motor dels PDF no el garanteix."""
    comu = (f'x="{x:.1f}" y="{y:.1f}" text-anchor="{ancora}" font-size="{fs}" '
            f'font-weight="{gruix}" font-family="system-ui"')
    return (f'<text {comu} fill="#fff" stroke="#fff" stroke-width="{fs * 0.28:.1f}" '
            f'stroke-linejoin="round" aria-hidden="true">{text}</text>'
            f'<text {comu} fill="{color}">{text}</text>')


def graf(a, b, c, xmin, xmax, ymin, ymax, xstep, ystep,
         etiqx="", etiqy="", punts=None, eix=None, etiquetes=True, dec_x=0, dec_y=0, fs=FS):
    """punts: llista de (x, y, radi) a marcar. eix: x on dibuixar l'eix de simetria.
    fs: la mida dels rètols. Si dos rètols seguits no hi caben, se'n posa un de cada dos:
    la marca i la línia de la graella hi continuen sent."""
    MT = fs + 14                     # a dalt, el nom de l'eix vertical
    MB = 2 * fs + 16                 # a baix, els números i el nom de l'eix horitzontal
    def px(x): return ML + (x - xmin) / (xmax - xmin) * (W - ML - MR)
    def py(y): return H - MB - (y - ymin) / (ymax - ymin) * (H - MB - MT)
    def n(v, d):
        s = f"{v:.{d}f}".rstrip("0").rstrip(".") if d else f"{v:.0f}"
        s = s or "0"
        return ("0" if s in ("-0", "0") else s).replace(".", ",").replace("-", "−")

    xs, ys = marques(xmin, xmax, xstep), marques(ymin, ymax, ystep)
    o = []
    # graella, a les marques
    for x in xs:
        o.append(f'<line x1="{px(x):.1f}" y1="{py(ymin):.1f}" x2="{px(x):.1f}" y2="{py(ymax):.1f}" stroke="#D4D4D4" stroke-width="1"/>')
    for y in ys:
        o.append(f'<line x1="{px(xmin):.1f}" y1="{py(y):.1f}" x2="{px(xmax):.1f}" y2="{py(y):.1f}" stroke="#D4D4D4" stroke-width="1"/>')

    # eixos: l'horitzontal a y=0 si el 0 hi és, si no a baix de tot
    y0 = 0 if ymin <= 0 <= ymax else ymin
    x0 = 0 if xmin <= 0 <= xmax else xmin
    o.append(f'<line x1="{px(xmin):.1f}" y1="{py(y0):.1f}" x2="{px(xmax):.1f}" y2="{py(y0):.1f}" stroke="#000" stroke-width="2.5"/>')
    o.append(f'<line x1="{px(x0):.1f}" y1="{py(ymin):.1f}" x2="{px(x0):.1f}" y2="{py(ymax):.1f}" stroke="#000" stroke-width="2.5"/>')

    rotuls = []                      # es dibuixen al final, damunt de la corba
    if etiquetes:
        # Un rètol de cada `cada_x` marques, perquè no es trepitgin: el més ample, i un espai.
        ample_x = max(len(n(x, dec_x)) for x in xs) * fs * 0.62 + fs * 0.6
        cada_x = 1 if px(xs[1]) - px(xs[0]) >= ample_x else 2
        cada_y = 1 if py(ys[0]) - py(ys[1]) >= fs * 1.25 else 2
        for i, x in enumerate(xs):
            if abs(x - x0) > 1e-9 and round(x / xstep) % cada_x == 0:
                rotuls.append(rotul(px(x), py(y0) + fs + 6, n(x, dec_x), fs))
        for y in ys:
            if abs(y - y0) > 1e-9 and round(y / ystep) % cada_y == 0:
                rotuls.append(rotul(px(x0) - 8, py(y) + fs * 0.35, n(y, dec_y), fs, "end"))
    if etiqx:
        rotuls.append(rotul(W - MR, H - 8, etiqx, fs, "end"))
    if etiqy:
        # A la dreta de l'eix i cap endins. Abans anava a l'esquerra i acabava
        # al marge: «altura (m)» sortia fora del dibuix i es llegia «ra (m)».
        rotuls.append(rotul(px(x0) + 8, MT - 10, etiqy, fs, "start"))

    # corba, retallada al marc
    trams, actual = [], []
    for i in range(801):
        xv = xmin + (xmax - xmin) * i / 800
        yv = a * xv * xv + b * xv + c
        if ymin - 1e-9 <= yv <= ymax + 1e-9:
            actual.append(f"{px(xv):.1f},{py(yv):.1f}")
        elif actual:
            trams.append(actual); actual = []
    if actual:
        trams.append(actual)
    for t in trams:
        o.append(f'<polyline points="{" ".join(t)}" fill="none" stroke="#000" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')

    if eix is not None:
        o.append(f'<line x1="{px(eix):.1f}" y1="{py(ymin):.1f}" x2="{px(eix):.1f}" y2="{py(ymax):.1f}" stroke="#000" stroke-width="2" stroke-dasharray="8 6"/>')
    for p in (punts or []):
        xv, yv, r = p[0], p[1], p[2]
        o.append(f'<circle cx="{px(xv):.1f}" cy="{py(yv):.1f}" r="{r}" fill="#000"/>')
        if len(p) > 3 and p[3]:
            dy = p[4] if len(p) > 4 else fs
            ty = py(yv) - dy
            rotuls.append(rotul(px(xv), ty, p[3], fs + 1, gruix=700, color="#000"))
    o += rotuls
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Gràfica"><rect x="0" y="0" width="{W}" height="{H}" fill="#fff"/>' + "".join(o) + "</svg>"


# ---- les paràboles de la fitxa ----
G = {}

# Les gràfiques només es generen quan s'executa l'script. Així gen_grafics5.py
# pot importar graf() i dibuixar-ne de noves amb exactament el mateix aspecte.
if __name__ == "__main__":
    # pilota: h = -5t^2 + 10t   vèrtex (1,5)  talls 0 i 2
    G["PILOTA_GRAN"] = graf(-5, 10, 0, 0, 2.4, 0, 6, 0.5, 1, "temps (s)", "altura (m)",
                            punts=[(1, 5, 8, "(1 , 5)"), (0, 0, 7, ""), (2, 0, 7, "")], eix=1, dec_x=1)
    G["PILOTA"] = graf(-5, 10, 0, 0, 2.4, 0, 6, 0.5, 1, "temps (s)", "altura (m)", dec_x=1)

    # sortidor: h = -0.5x^2 + 2x   vèrtex (2,2)  talls 0 i 4
    G["SORTIDOR"] = graf(-0.5, 2, 0, 0, 4.6, 0, 3, 1, 0.5, "distància (m)", "altura (m)", dec_y=1)

    # tarifa: c = x^2 - 8x + 20   vèrtex (4,4)  cap tall
    G["TARIFA"] = graf(1, -8, 20, 0, 8, 0, 22, 1, 2, "peces", "cost (€)")

    # coet: h = -5t^2 + 20t   vèrtex (2,20)  talls 0 i 4
    G["COET"] = graf(-5, 20, 0, 0, 4.4, 0, 22, 1, 2, "temps (s)", "altura (m)")

    # obertures
    # van de costat a la fitxa (8,5 cm cadascun): lletra més gran
    G["AVALL"] = graf(-1, 4, 0, -0.5, 4.5, -1, 5, 1, 1, "", "", fs=28)
    G["AMUNT"] = graf(1, -4, 4, -0.5, 4.5, -1, 5, 1, 1, "", "", fs=28)

    # talls = solucions
    G["EQ1"] = graf(1, -5, 6, -0.4, 5.4, -2, 7, 1, 1, "x", "y")
    G["EQ2"] = graf(1, 0, -4, -3.2, 3.2, -5, 6, 1, 1, "x", "y")

    import json, pathlib
    pathlib.Path("grafics.json").write_text(json.dumps(G), encoding="utf-8")

    print("Gràfiques generades:", ", ".join(G))
    for nom, (a, b, c) in {"pilota": (-5, 10, 0), "sortidor": (-0.5, 2, 0), "tarifa": (1, -8, 20),
                           "coet": (-5, 20, 0), "EQ1": (1, -5, 6), "EQ2": (1, 0, -4)}.items():
        vx = -b / (2 * a); vy = a * vx * vx + b * vx + c
        disc = b * b - 4 * a * c
        if disc >= 0:
            r = disc ** .5
            talls = sorted([(-b + r) / (2 * a), (-b - r) / (2 * a)])
            talls = [round(t + 0, 4) for t in talls]
        else:
            talls = "cap"
        print(f"  {nom:9} vèrtex ({vx:g} , {vy:g})  talls {talls}  s'obre {'avall' if a < 0 else 'amunt'}")
