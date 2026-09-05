"""Genera les gràfiques de paràboles de la fitxa de la Unitat 5, en SVG i en
blanc i negre. Es dibuixen per càlcul i no a mà, perquè els vèrtexs, els talls
i les marques dels eixos caiguin exactament on toca."""

W, H = 560, 300
ML, MR, MT, MB = 54, 20, 26, 46


def graf(a, b, c, xmin, xmax, ymin, ymax, xstep, ystep,
         etiqx="", etiqy="", punts=None, eix=None, etiquetes=True, dec_x=0, dec_y=0):
    """punts: llista de (x, y, radi) a marcar. eix: x on dibuixar l'eix de simetria."""
    def px(x): return ML + (x - xmin) / (xmax - xmin) * (W - ML - MR)
    def py(y): return H - MB - (y - ymin) / (ymax - ymin) * (H - MB - MT)
    def n(v, d):
        s = f"{v:.{d}f}".rstrip("0").rstrip(".") if d else f"{v:.0f}"
        return (s or "0").replace(".", ",")

    o = []
    # graella
    x = xmin
    while x <= xmax + 1e-9:
        o.append(f'<line x1="{px(x):.1f}" y1="{py(ymin):.1f}" x2="{px(x):.1f}" y2="{py(ymax):.1f}" stroke="#D4D4D4" stroke-width="1"/>')
        x += xstep
    y = ymin
    while y <= ymax + 1e-9:
        o.append(f'<line x1="{px(xmin):.1f}" y1="{py(y):.1f}" x2="{px(xmax):.1f}" y2="{py(y):.1f}" stroke="#D4D4D4" stroke-width="1"/>')
        y += ystep

    # eixos: l'horitzontal a y=0 si el 0 hi és, si no a baix de tot
    y0 = 0 if ymin <= 0 <= ymax else ymin
    x0 = 0 if xmin <= 0 <= xmax else xmin
    o.append(f'<line x1="{px(xmin):.1f}" y1="{py(y0):.1f}" x2="{px(xmax):.1f}" y2="{py(y0):.1f}" stroke="#000" stroke-width="2.5"/>')
    o.append(f'<line x1="{px(x0):.1f}" y1="{py(ymin):.1f}" x2="{px(x0):.1f}" y2="{py(ymax):.1f}" stroke="#000" stroke-width="2.5"/>')

    if etiquetes:
        x = xmin
        while x <= xmax + 1e-9:
            if abs(x - x0) > 1e-9:
                o.append(f'<text x="{px(x):.1f}" y="{py(y0)+22:.0f}" text-anchor="middle" font-size="15" fill="#5E5E5E" font-family="system-ui">{n(x,dec_x)}</text>')
            x += xstep
        y = ymin
        while y <= ymax + 1e-9:
            if abs(y - y0) > 1e-9:
                o.append(f'<text x="{px(x0)-9:.1f}" y="{py(y)+5:.1f}" text-anchor="end" font-size="15" fill="#5E5E5E" font-family="system-ui">{n(y,dec_y)}</text>')
            y += ystep
    if etiqx:
        o.append(f'<text x="{W-MR:.0f}" y="{H-8:.0f}" text-anchor="end" font-size="15" fill="#5E5E5E" font-family="system-ui">{etiqx}</text>')
    if etiqy:
        o.append(f'<text x="{px(x0)-9:.0f}" y="{MT-8:.0f}" text-anchor="end" font-size="15" fill="#5E5E5E" font-family="system-ui">{etiqy}</text>')

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
            dy = p[4] if len(p) > 4 else 16
            ty = py(yv) - dy
            o.append(f'<text x="{px(xv):.1f}" y="{ty:.1f}" text-anchor="middle" font-size="16" font-weight="700" fill="#000" font-family="system-ui">{p[3]}</text>')
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Gràfica"><rect x="0" y="0" width="{W}" height="{H}" fill="#fff"/>' + "".join(o) + "</svg>"


# ---- les paràboles de la fitxa ----
G = {}

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
G["AVALL"] = graf(-1, 4, 0, -0.5, 4.5, -1, 5, 1, 1, "", "")
G["AMUNT"] = graf(1, -4, 4, -0.5, 4.5, -1, 5, 1, 1, "", "")

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
