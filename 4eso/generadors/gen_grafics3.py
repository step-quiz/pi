"""Dibuixos nous: les barres de percentatge de la U2 (perquè el factor emergeixi
del dibuix en comptes d'anunciar-se) i el model d'àrea de la mitjana ponderada
de la U6."""
import json

NEG, GRIS, CLAR, FONS, MIG = "#000", "#5E5E5E", "#D4D4D4", "#F2F2F2", "#C4C4C4"
TIP = 'font-family="system-ui"'
G = {}


def env(cos, w, h):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Dibuix">'
            f'<rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>{cos}</svg>')


# ---------- U2: la barra sencera ----------
def barra_sencera(total=300):
    w, h, x0, x1, y, alt = 560, 130, 30, 530, 46, 54
    o = [f'<rect x="{x0}" y="{y}" width="{x1-x0}" height="{alt}" fill="{FONS}" stroke="{NEG}" stroke-width="3"/>']
    o.append(f'<text x="{(x0+x1)/2}" y="{y+36}" text-anchor="middle" font-size="24" font-weight="800" fill="{NEG}" {TIP}>{total} €</text>')
    o.append(f'<text x="{(x0+x1)/2}" y="{y-14}" text-anchor="middle" font-size="18" fill="{GRIS}" {TIP}>tota la bici · 100 %</text>')
    return env("".join(o), w, h)


# ---------- U2: la barra partida ----------
def barra_partida(total=300, treu=20):
    w, h, x0, x1, y, alt = 560, 175, 30, 530, 56, 54
    queda = 100 - treu
    xtall = x0 + (x1 - x0) * queda / 100
    o = [f'<rect x="{x0}" y="{y}" width="{xtall-x0}" height="{alt}" fill="{FONS}" stroke="{NEG}" stroke-width="3"/>']
    o.append(f'<rect x="{xtall}" y="{y}" width="{x1-xtall}" height="{alt}" fill="{MIG}" stroke="{NEG}" stroke-width="3"/>')
    # ratllat sobre el tros que se'n va
    n = 0
    while True:
        xa = xtall + n * 13
        if xa > x1: break
        xb = min(xa + alt, x1)
        o.append(f'<line x1="{xa:.1f}" y1="{y+alt}" x2="{xb:.1f}" y2="{y+alt-(xb-xa):.1f}" stroke="{NEG}" stroke-width="1.6"/>')
        n += 1
    o.append(f'<text x="{(x0+xtall)/2:.1f}" y="{y-16}" text-anchor="middle" font-size="20" font-weight="800" fill="{NEG}" {TIP}>{queda} %</text>')
    o.append(f'<text x="{(xtall+x1)/2:.1f}" y="{y-16}" text-anchor="middle" font-size="20" font-weight="800" fill="{NEG}" {TIP}>{treu} %</text>')
    o.append(f'<text x="{(x0+xtall)/2:.1f}" y="{y+35}" text-anchor="middle" font-size="24" font-weight="800" fill="{NEG}" {TIP}>{total*queda//100} €</text>')
    o.append(f'<text x="{(xtall+x1)/2:.1f}" y="{y+35}" text-anchor="middle" font-size="22" font-weight="800" fill="{NEG}" {TIP}>{total*treu//100} €</text>')
    o.append(f'<text x="{(x0+xtall)/2:.1f}" y="{y+alt+30}" text-anchor="middle" font-size="19" fill="{GRIS}" {TIP}>això queda</text>')
    o.append(f'<text x="{(xtall+x1)/2:.1f}" y="{y+alt+30}" text-anchor="middle" font-size="19" fill="{GRIS}" {TIP}>això se&#39;n va</text>')
    return env("".join(o), w, h)


G["BARRA_SENCERA"] = barra_sencera()
G["BARRA_PARTIDA"] = barra_partida()


# ---------- U6: model d'àrea de la mitjana ponderada ----------
def area_ponderada(parts, nota_max=10):
    """parts: llista de (nom, nota, pes). L'amplada és el pes i l'altura la nota,
    de manera que l'àrea de cada rectangle és nota × pes i el total és la nota final."""
    w, h = 560, 310
    ml, mr, mt, mb = 62, 24, 30, 62
    def px(p): return ml + p * (w - ml - mr)
    def py(n): return h - mb - n / nota_max * (h - mb - mt)
    o = []
    for n in range(0, nota_max + 1, 2):
        o.append(f'<line x1="{ml}" y1="{py(n):.1f}" x2="{w-mr}" y2="{py(n):.1f}" stroke="{CLAR}" stroke-width="1"/>')
        o.append(f'<text x="{ml-10}" y="{py(n)+5:.1f}" text-anchor="end" font-size="15" fill="{GRIS}" {TIP}>{n}</text>')
    acc, total = 0.0, 0.0
    for i, (nom, nota, pes) in enumerate(parts):
        xa, xb = px(acc), px(acc + pes)
        o.append(f'<rect x="{xa:.1f}" y="{py(nota):.1f}" width="{xb-xa:.1f}" height="{py(0)-py(nota):.1f}" '
                 f'fill="{FONS if i % 2 == 0 else MIG}" stroke="{NEG}" stroke-width="3"/>')
        o.append(f'<text x="{(xa+xb)/2:.1f}" y="{py(nota)+26:.1f}" text-anchor="middle" font-size="19" font-weight="800" fill="{NEG}" {TIP}>{nota:g}</text>')
        o.append(f'<text x="{(xa+xb)/2:.1f}" y="{py(0)+24:.0f}" text-anchor="middle" font-size="15" fill="{NEG}" {TIP}>{nom}</text>')
        o.append(f'<text x="{(xa+xb)/2:.1f}" y="{py(0)+44:.0f}" text-anchor="middle" font-size="15" fill="{GRIS}" {TIP}>pes {pes:g}</text>')
        acc += pes; total += nota * pes
    o.append(f'<line x1="{ml}" y1="{py(0):.1f}" x2="{w-mr}" y2="{py(0):.1f}" stroke="{NEG}" stroke-width="3"/>')
    o.append(f'<line x1="{ml}" y1="{py(0):.1f}" x2="{ml}" y2="{mt-4}" stroke="{NEG}" stroke-width="3"/>')
    # la nota final és l'altura que tindria un sol rectangle de la mateixa àrea
    o.append(f'<line x1="{ml}" y1="{py(total):.1f}" x2="{w-mr}" y2="{py(total):.1f}" stroke="{NEG}" stroke-width="3" stroke-dasharray="10 6"/>')
    o.append(f'<text x="{w-mr}" y="{py(total)-12:.1f}" text-anchor="end" font-size="18" font-weight="800" fill="{NEG}" {TIP}>nota final {total:g}</text>')
    return env("".join(o), w, h), total


G["AREA_PONDERADA"], total = area_ponderada([("Projecte", 7, .5), ("Prova", 5, .3), ("Feina diària", 8, .2)])

with open("grafics3.json", "w", encoding="utf-8") as f:
    json.dump(G, f)

print("Generats:", ", ".join(G))
print()
print("COMPROVACIONS")
print(f"  Barra: 300 € · 80 % queden = {300*80//100} € · 20 % se'n van = {300*20//100} €")
print(f"  Amplada de la barra 500 px → el tall a 80 % cau a {30 + 500*0.8:.0f} px")
for nom, n, p in [("Projecte", 7, .5), ("Prova", 5, .3), ("Feina diària", 8, .2)]:
    print(f"  Àrea {nom:13} {n} × {p} = {n*p:g}")
print(f"  Suma de pesos: {.5+.3+.2:g}  ·  Nota final (àrea total): {total:g}")
print(f"  Mitjana simple (error típic): {(7+5+8)/3:.2f}")
