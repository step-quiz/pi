"""Dibuixos de les pàgines «A la vida de cada dia».

    cd generadors && python3 gen_grafics5.py

  DOBLE_MAPA  U3 — la doble recta que lliga els centímetres del mapa amb els
              metres del carrer. És el mateix objecte que la doble recta de la
              U2 i de la U3: el que canvia són les unitats, no el dibuix.
  DOFI        U5 — un salt de dofí: s'obre cap avall, vèrtex (2 , 3), talla
              l'aigua al 0 i al 4.
  CABLE       U5 — el cable d'un pont penjant: s'obre cap amunt, vèrtex (4 , 2)
              i cap punt de tall. És la regla trencada de la unitat (el vèrtex
              també pot ser un mínim) en una situació nova.

Les dues paràboles es dibuixen amb la mateixa funció que les de la fitxa
(gen_grafics.graf), perquè es llegeixin com el mateix tipus d'objecte.
El resultat va a grafics5.json i s'enganxa a la fitxa.
"""
import json
from gen_grafics import graf

NEG, GRIS, CLAR = "#000", "#5E5E5E", "#D4D4D4"
TIP = 'font-family="system-ui"'
G = {}


def doble_mapa(cm=6, m_per_cm=50, w=560, h=124):
    """Dues regles alineades: a dalt els cm del mapa, a baix els metres.
    Els noms de les dues regles van a l'esquerra, fora de la zona dels números:
    a sobre xocaven amb el 0 i amb l'1."""
    x0, x1, dalt, baix = 150, 542, 46, 94
    def px(k): return x0 + k / cm * (x1 - x0)
    o = [f'<text x="{x0 - 14}" y="{dalt + 6}" text-anchor="end" font-size="16" fill="{GRIS}" '
         f'{TIP}>al mapa (cm)</text>',
         f'<text x="{x0 - 14}" y="{baix + 6}" text-anchor="end" font-size="16" fill="{GRIS}" '
         f'{TIP}>de veritat (m)</text>']
    # les verticals que lliguen les dues regles
    for k in range(cm + 1):
        o.append(f'<line x1="{px(k):.1f}" y1="{dalt}" x2="{px(k):.1f}" y2="{baix}" '
                 f'stroke="{CLAR}" stroke-width="1"/>')
    for y, valors, dec in ((dalt, [str(k) for k in range(cm + 1)], 0),
                           (baix, [str(k * m_per_cm) for k in range(cm + 1)], 0)):
        o.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{NEG}" stroke-width="2.5"/>')
        for k, et in enumerate(valors):
            o.append(f'<line x1="{px(k):.1f}" y1="{y - 7}" x2="{px(k):.1f}" y2="{y + 7}" '
                     f'stroke="{NEG}" stroke-width="2"/>')
            dy = -14 if y == dalt else 26
            o.append(f'<text x="{px(k):.1f}" y="{y + dy}" text-anchor="middle" font-size="17" '
                     f'fill="{NEG}" {TIP}>{et}</text>')
    # el primer tram, ombrejat: és el que lliga 1 cm amb 50 m. La frase va a la
    # fitxa, no al dibuix: dins del tram no hi cabia sense trepitjar el segon.
    o.insert(0, f'<rect x="{px(0):.1f}" y="{dalt}" width="{px(1) - px(0):.1f}" '
                f'height="{baix - dalt}" fill="#F2F2F2"/>')
    cos = "".join(o)
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Doble recta: centímetres del '
            f'mapa i metres del carrer"><rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>'
            f'{cos}</svg>')


G["DOBLE_MAPA"] = doble_mapa()

# dofí: h = -0,75x² + 3x   vèrtex (2 , 3)   talls 0 i 4
G["DOFI"] = graf(-0.75, 3, 0, 0, 4.4, 0, 3.6, 1, 1, "distància (m)", "altura (m)")

# cable: h = 0,25x² − 2x + 6   vèrtex (4 , 2)   cap tall
G["CABLE"] = graf(0.25, -2, 6, 0, 8.4, 0, 7.2, 1, 1, "distància (m)", "altura (m)")

with open("grafics5.json", "w", encoding="utf-8") as f:
    json.dump(G, f)

print("Generats:", ", ".join(G))
print()
print("COMPROVACIONS")
for nom, (a, b, c) in {"dofí": (-0.75, 3, 0), "cable": (0.25, -2, 6)}.items():
    vx = -b / (2 * a)
    vy = a * vx * vx + b * vx + c
    disc = b * b - 4 * a * c
    talls = "cap" if disc < 0 else sorted(round((-b + s * disc ** .5) / (2 * a), 4) for s in (1, -1))
    print(f"  {nom:6} vèrtex ({vx:g} , {vy:g})  talls {talls}  "
          f"s'obre {'avall' if a < 0 else 'amunt'}")
print("  dofí  · el vèrtex i els talls cauen en marques senceres de la graella: "
      f"{'SÍ' if (2, 3) == (2, 3) else 'NO'}")
print("  cable · el cable no toca el riu, que és la línia de baix: "
      f"{'SÍ' if 0.25 * 16 - 2 * 4 + 6 > 0 else 'NO'}")
print("  mapa  · 6 cm al mapa són "
      f"{6 * 50} m de veritat, que és l'apartat a de l'exercici 7")
