"""Gràfics en blanc i negre per a les fitxes de les unitats 6 (estadística) i
7 (atzar). Es generen per càlcul perquè les barres, els punts i les branques
caiguin exactament on toca."""
import json

G = {}
NEG, GRIS, CLAR, FONS = "#000", "#5E5E5E", "#D4D4D4", "#F2F2F2"
TIP = 'font-family="system-ui"'


def env(cos, w=560, h=300):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Gràfic">'
            f'<rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>{cos}</svg>')


# ---------- U6: diagrames de punts ----------
def punts(dades, xmin=0, xmax=10, titol="", w=560, h=190):
    ml, mr, mb = 40, 24, 46
    def px(x): return ml + (x - xmin) / (xmax - xmin) * (w - ml - mr)
    o = [f'<text x="{ml}" y="20" font-size="17" font-weight="700" fill="{NEG}" {TIP}>{titol}</text>']
    o.append(f'<line x1="{px(xmin)}" y1="{h-mb}" x2="{px(xmax)}" y2="{h-mb}" stroke="{NEG}" stroke-width="2.5"/>')
    for x in range(xmin, xmax + 1):
        o.append(f'<line x1="{px(x):.1f}" y1="{h-mb}" x2="{px(x):.1f}" y2="{h-mb+7}" stroke="{NEG}" stroke-width="2"/>')
        o.append(f'<text x="{px(x):.1f}" y="{h-mb+28}" text-anchor="middle" font-size="16" fill="{GRIS}" {TIP}>{x}</text>')
    compte = {}
    for d in sorted(dades):
        compte[d] = compte.get(d, 0) + 1
        o.append(f'<circle cx="{px(d):.1f}" cy="{h-mb-13-(compte[d]-1)*24:.1f}" r="9" fill="{NEG}"/>')
    mitjana = sum(dades) / len(dades)
    o.append(f'<line x1="{px(mitjana):.1f}" y1="{h-mb+2}" x2="{px(mitjana):.1f}" y2="30" stroke="{NEG}" stroke-width="2" stroke-dasharray="7 5"/>')
    o.append(f'<text x="{px(mitjana):.1f}" y="26" text-anchor="middle" font-size="15" fill="{GRIS}" {TIP}>mitjana {mitjana:g}</text>')
    return env("".join(o), w, h)


G["DOT_A"] = punts([4, 5, 5, 5, 5, 6], titol="Jugadora A")
G["DOT_B"] = punts([1, 3, 5, 5, 7, 9], titol="Jugadora B")


# ---------- U6: gràfic de barres ----------
def barres(etiquetes, valors, ymin, ymax, ystep, titol="", w=560, h=300, ample=54):
    ml, mr, mt, mb = 58, 20, 34, 54
    def py(v): return h - mb - (v - ymin) / (ymax - ymin) * (h - mb - mt)
    n = len(valors)
    pas = (w - ml - mr) / n
    o = [f'<text x="{ml}" y="22" font-size="17" font-weight="700" fill="{NEG}" {TIP}>{titol}</text>']
    v = ymin
    while v <= ymax + 1e-9:
        o.append(f'<line x1="{ml}" y1="{py(v):.1f}" x2="{w-mr}" y2="{py(v):.1f}" stroke="{CLAR}" stroke-width="1"/>')
        o.append(f'<text x="{ml-10}" y="{py(v)+5:.1f}" text-anchor="end" font-size="15" fill="{GRIS}" {TIP}>{v:g}</text>')
        v += ystep
    o.append(f'<line x1="{ml}" y1="{py(ymin):.1f}" x2="{w-mr}" y2="{py(ymin):.1f}" stroke="{NEG}" stroke-width="2.5"/>')
    o.append(f'<line x1="{ml}" y1="{py(ymin):.1f}" x2="{ml}" y2="{mt-6}" stroke="{NEG}" stroke-width="2.5"/>')
    for i, (e, val) in enumerate(zip(etiquetes, valors)):
        cx = ml + pas * (i + .5)
        alt = py(ymin) - py(val)
        o.append(f'<rect x="{cx-ample/2:.1f}" y="{py(val):.1f}" width="{ample}" height="{alt:.1f}" fill="{FONS}" stroke="{NEG}" stroke-width="2.5"/>')
        o.append(f'<text x="{cx:.1f}" y="{py(val)-10:.1f}" text-anchor="middle" font-size="17" font-weight="700" fill="{NEG}" {TIP}>{val:g}</text>')
        o.append(f'<text x="{cx:.1f}" y="{h-mb+26:.0f}" text-anchor="middle" font-size="16" fill="{GRIS}" {TIP}>{e}</text>')
    return env("".join(o), w, h)


G["TRANSPORT"] = barres(["a peu", "bus", "cotxe", "bici"], [12, 9, 5, 4], 0, 14, 2,
                        titol="Com venen a l'institut")
G["ENGANY_0"] = barres(["Marca A", "Marca B"], [95, 100], 0, 110, 20,
                       titol="Gràfic 1", w=270, h=250, ample=52)
G["ENGANY_90"] = barres(["Marca A", "Marca B"], [95, 100], 90, 102, 2,
                        titol="Gràfic 2", w=270, h=250, ample=52)


# ---------- U7: la línia de la probabilitat ----------
def linia_prob():
    w, h, ml, mr, y = 560, 170, 46, 46, 78
    def px(p): return ml + p / 100 * (w - ml - mr)
    o = [f'<line x1="{ml}" y1="{y}" x2="{w-mr}" y2="{y}" stroke="{NEG}" stroke-width="4"/>']
    for p, et in [(0, "0 %"), (25, "25 %"), (50, "50 %"), (75, "75 %"), (100, "100 %")]:
        o.append(f'<line x1="{px(p):.1f}" y1="{y-11}" x2="{px(p):.1f}" y2="{y+11}" stroke="{NEG}" stroke-width="3"/>')
        o.append(f'<text x="{px(p):.1f}" y="{y+36}" text-anchor="middle" font-size="17" fill="{GRIS}" {TIP}>{et}</text>')
    for p, et, dy in [(0, "impossible", -26), (50, "pot passar", -26), (100, "segur", -26)]:
        o.append(f'<text x="{px(p):.1f}" y="{y+dy}" text-anchor="middle" font-size="18" font-weight="700" fill="{NEG}" {TIP}>{et}</text>')
    o.append(f'<text x="{ml}" y="{y+74}" font-size="16" fill="{GRIS}" {TIP}>com més a la dreta, més fàcil que passi</text>')
    return env("".join(o), w, h)


G["LINIA_PROB"] = linia_prob()


# ---------- U7: diagrames d'arbre ----------
def arbre(nivell1, nivell2, resultats=True, w=560, h=330):
    """Arbre de dos nivells. Si `resultats`, escriu les combinacions a la dreta."""
    o = []
    x0, x1, x2, x3 = 40, 190, 330, 360
    n1, n2 = len(nivell1), len(nivell2)
    total = n1 * n2
    alt = h - 40
    o.append(f'<circle cx="{x0}" cy="{h/2:.0f}" r="7" fill="{NEG}"/>')
    k = 0
    for i, a in enumerate(nivell1):
        ya = 30 + alt * (i + .5) / n1
        o.append(f'<line x1="{x0}" y1="{h/2:.0f}" x2="{x1}" y2="{ya:.1f}" stroke="{NEG}" stroke-width="2.5"/>')
        etq = a if a else ""
        o.append(f'<rect x="{x1}" y="{ya-17:.1f}" width="118" height="34" rx="7" fill="{FONS if a else "#fff"}" stroke="{NEG}" stroke-width="2.5"/>')
        if etq:
            o.append(f'<text x="{x1+59}" y="{ya+7:.1f}" text-anchor="middle" font-size="17" font-weight="700" fill="{NEG}" {TIP}>{etq}</text>')
        for j, b in enumerate(nivell2):
            yb = 30 + alt * (k + .5) / total
            k += 1
            o.append(f'<line x1="{x1+118}" y1="{ya:.1f}" x2="{x2}" y2="{yb:.1f}" stroke="{NEG}" stroke-width="2.5"/>')
            o.append(f'<rect x="{x2}" y="{yb-15:.1f}" width="112" height="30" rx="7" fill="{FONS if b else "#fff"}" stroke="{NEG}" stroke-width="2.5"/>')
            if b:
                o.append(f'<text x="{x2+56}" y="{yb+6:.1f}" text-anchor="middle" font-size="16" font-weight="700" fill="{NEG}" {TIP}>{b}</text>')
            if resultats and a and b:
                o.append(f'<text x="{x2+124}" y="{yb+6:.1f}" font-size="15" fill="{GRIS}" {TIP}>{a} + {b}</text>')
            elif not resultats:
                o.append(f'<rect x="{x2+122}" y="{yb-15:.1f}" width="72" height="30" rx="7" fill="#fff" stroke="{CLAR}" stroke-width="2"/>')
    return env("".join(o), w, h)


G["ARBRE_MENU"] = arbre(["Sopa", "Amanida"], ["Pollastre", "Peix", "Pasta"])
G["ARBRE_BUIT"] = arbre(["", ""], ["", ""], resultats=False, h=280)

with open("grafics2.json", "w", encoding="utf-8") as f:
    json.dump(G, f)

print("Generats:", ", ".join(G))
print()
print("COMPROVACIONS")
A, B = [4, 5, 5, 5, 5, 6], [1, 3, 5, 5, 7, 9]
print(f"  Jugadora A {A} → mitjana {sum(A)/len(A):g}, recorregut {max(A)-min(A)}")
print(f"  Jugadora B {B} → mitjana {sum(B)/len(B):g}, recorregut {max(B)-min(B)}")
t = [12, 9, 5, 4]
print(f"  Transport {t} → total {sum(t)}, a peu menys cotxe = {t[0]-t[2]}")
print(f"  Engany: A=95 B=100 → diferència {100-95}; el gràfic 2 comença a 90 i no a 0")
print(f"  Arbre menú: 2 primers × 3 segons = {2*3} menús")
print(f"  Arbre buit: 2 × 2 = {2*2} resultats")
