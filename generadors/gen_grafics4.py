"""Dibuixos nous del tercer repàs.

Tots tres tapen un graó que faltava entre el concret i el símbol:

  BARRA_ESCALA  U2 p.1 — la barra amb l'escala de 0 a 100 % al costat, perquè
                el percentatge sigui una POSICIÓ abans de ser un factor.
  REPARTIMENT   U6 p.3 — la mitjana com a aplanar, abans que com a «sumar i dividir».
  BARRA_PROB    U7 p.3 — la probabilitat com a un tros d'una barra partida en parts
                iguals, amb la mateixa escala de percentatge de la U2.

Els tres fan servir la mateixa geometria que els dibuixos que ja hi ha a la
pàgina on entren, perquè es llegeixin com el mateix objecte i no com un de nou.
"""
import json

NEG, GRIS, CLAR, FONS, MIG = "#000", "#5E5E5E", "#D4D4D4", "#F2F2F2", "#C4C4C4"
TIP = 'font-family="system-ui"'
G = {}


def env(cos, w, h):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Dibuix">'
            f'<rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>{cos}</svg>')


# ---------- U2: la doble recta sota la barra ----------
def barra_escala(total=300, treu=20, passos=5):
    """No repeteix la barra: hi posa a sota les dues regles alineades, amb els
    mateixos x0/x1 que BARRA_SENCERA i BARRA_PARTIDA. Així es veu que 240 € i
    80 % cauen al mateix lloc, que és exactament el mòdul Doble recta de l'app."""
    w, h = 560, 126
    x0, x1 = 30, 530
    y_eur, y_pct = 40, 88
    queda = 100 - treu

    def x(p):
        return x0 + (x1 - x0) * p / 100

    xt = x(queda)
    o = []

    # eix de dalt: euros
    o.append(f'<line x1="{x0}" y1="{y_eur}" x2="{x1}" y2="{y_eur}" stroke="{NEG}" stroke-width="2.5"/>')
    for i in range(passos + 1):
        p = 100 * i / passos
        val = round(total * p / 100)
        fort = (val == total * queda // 100)
        o.append(f'<line x1="{x(p):.1f}" y1="{y_eur-7}" x2="{x(p):.1f}" y2="{y_eur}" stroke="{NEG}" stroke-width="2"/>')
        o.append(f'<text x="{x(p):.1f}" y="{y_eur-14}" text-anchor="middle" font-size="17" '
                 f'font-weight="{"800" if fort else "400"}" fill="{NEG if fort else GRIS}" {TIP}>{val}</text>')
    o.append(f'<text x="{x0-8}" y="{y_eur+5}" text-anchor="end" font-size="16" fill="{GRIS}" {TIP}>€</text>')

    # eix de baix: percentatge
    o.append(f'<line x1="{x0}" y1="{y_pct}" x2="{x1}" y2="{y_pct}" stroke="{NEG}" stroke-width="2.5"/>')
    for i in range(passos + 1):
        p = 100 * i / passos
        fort = abs(p - queda) < 1e-9
        o.append(f'<line x1="{x(p):.1f}" y1="{y_pct}" x2="{x(p):.1f}" y2="{y_pct+7}" stroke="{NEG}" stroke-width="2"/>')
        o.append(f'<text x="{x(p):.1f}" y="{y_pct+27}" text-anchor="middle" font-size="17" '
                 f'font-weight="{"800" if fort else "400"}" fill="{NEG if fort else GRIS}" {TIP}>{p:g}</text>')
    o.append(f'<text x="{x0-8}" y="{y_pct+5}" text-anchor="end" font-size="16" fill="{GRIS}" {TIP}>%</text>')

    # la vertical que lliga els dos eixos: 240 € i 80 % són el mateix lloc
    o.append(f'<line x1="{xt:.1f}" y1="{y_eur}" x2="{xt:.1f}" y2="{y_pct}" stroke="{NEG}" '
             f'stroke-width="3" stroke-dasharray="8 5"/>')
    o.append(f'<circle cx="{xt:.1f}" cy="{y_eur}" r="5.5" fill="{NEG}"/>')
    o.append(f'<circle cx="{xt:.1f}" cy="{y_pct}" r="5.5" fill="{NEG}"/>')
    return env("".join(o), w, h), xt


# ---------- U6: la mitjana com a aplanar ----------
def repartiment(dades):
    """Columnes de quadrets que es reparteixen fins que totes són iguals.
    L'altura final és la mitjana, sense sumar ni dividir."""
    w, h = 560, 204
    cel, gap = 20, 3
    pas = cel + gap
    base = 150
    mitjana = sum(dades) / len(dades)
    assert mitjana == int(mitjana), "per al dibuix cal que la mitjana sigui entera"
    mitjana = int(mitjana)

    def panell(x0, valors, trama):
        """Cada grup deixa marca encara que tingui zero peces: si no, el partit
        de 0 gols desapareix i a l'esquerra se'n compten 8 i a la dreta 9, que
        és justament el que el gest de repartir no ha de fer."""
        p = []
        for i, v in enumerate(valors):
            x = x0 + i * pas
            for k in range(v):
                p.append(f'<rect x="{x}" y="{base-(k+1)*pas}" width="{cel}" height="{cel}" '
                         f'fill="{trama}" stroke="{NEG}" stroke-width="2"/>')
            if v == 0:                      # casella buida, de contorn discontinu
                p.append(f'<rect x="{x}" y="{base-pas}" width="{cel}" height="{cel}" '
                         f'fill="#fff" stroke="{GRIS}" stroke-width="2" stroke-dasharray="4 3"/>')
            # marca de grup sota la línia, perquè es puguin comptar a totes dues bandes
            p.append(f'<line x1="{x+cel/2:.1f}" y1="{base}" x2="{x+cel/2:.1f}" y2="{base+7}" '
                     f'stroke="{NEG}" stroke-width="2"/>')
        p.append(f'<line x1="{x0-6}" y1="{base}" x2="{x0+len(valors)*pas-gap+6}" y2="{base}" '
                 f'stroke="{NEG}" stroke-width="3"/>')
        return p

    amp = len(dades) * pas - gap
    xa, xb = 32, 32 + amp + 56
    o = panell(xa, dades, FONS)
    o += panell(xb, [mitjana] * len(dades), MIG)

    # la fletxa del mig
    xf = xa + amp + 28
    o.append(f'<path d="M{xf-19} {base-46}h30m0 0l-11-9m11 9l-11 9" fill="none" stroke="{NEG}" '
             f'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')

    # el nivell on queda tot
    ym = base - mitjana * pas
    o.append(f'<line x1="{xb-10}" y1="{ym}" x2="{xb+amp+14}" y2="{ym}" stroke="{NEG}" '
             f'stroke-width="3" stroke-dasharray="9 6"/>')
    o.append(f'<text x="{xb+amp+18}" y="{ym+6}" font-size="20" font-weight="800" fill="{NEG}" {TIP}>{mitjana}</text>')
    o.append(f'<text x="{xa+amp/2:.0f}" y="{base+34}" text-anchor="middle" font-size="16" fill="{GRIS}" {TIP}>'
             f'com estan</text>')
    o.append(f'<text x="{xb+amp/2:.0f}" y="{base+34}" text-anchor="middle" font-size="16" fill="{GRIS}" {TIP}>'
             f'repartits igual</text>')
    return env("".join(o), w, h), mitjana


# ---------- U7: la probabilitat com un tros de la barra ----------
def barra_prob(cares=6, bona=5):
    """La mateixa escala de 0 a 100 % de la U2, aplicada a un dau."""
    w, h = 560, 168
    x0, x1 = 30, 530
    y, alt, y_pct = 34, 50, 116
    amp = (x1 - x0) / cares
    o = []
    for i in range(cares):
        xa = x0 + i * amp
        ple = MIG if i + 1 == bona else "#fff"
        o.append(f'<rect x="{xa:.1f}" y="{y}" width="{amp:.1f}" height="{alt}" fill="{ple}" '
                 f'stroke="{NEG}" stroke-width="{3 if i+1 == bona else 2}"/>')
        o.append(f'<text x="{xa+amp/2:.1f}" y="{y+33}" text-anchor="middle" font-size="21" '
                 f'font-weight="{"800" if i+1 == bona else "400"}" fill="{NEG}" {TIP}>{i+1}</text>')

    # l'escala de percentatge, la mateixa de la U2
    o.append(f'<line x1="{x0}" y1="{y_pct}" x2="{x1}" y2="{y_pct}" stroke="{NEG}" stroke-width="2.5"/>')
    for i in range(cares + 1):
        xa = x0 + i * amp
        o.append(f'<line x1="{xa:.1f}" y1="{y_pct}" x2="{xa:.1f}" y2="{y_pct+7}" stroke="{NEG}" stroke-width="2"/>')
    for p, et in ((0, "0"), (100, "100")):
        o.append(f'<text x="{x0+(x1-x0)*p/100:.1f}" y="{y_pct+27}" text-anchor="middle" font-size="16" '
                 f'fill="{GRIS}" {TIP}>{et}</text>')
    o.append(f'<text x="{x1+2}" y="{y_pct+27}" text-anchor="start" font-size="14" fill="{GRIS}" {TIP}>%</text>')

    # el tros que val: una casella, amidada contra l'escala
    xa = x0 + (bona - 1) * amp
    pct = 100 / cares
    o.append(f'<line x1="{xa:.1f}" y1="{y+alt}" x2="{xa:.1f}" y2="{y_pct}" stroke="{NEG}" '
             f'stroke-width="2" stroke-dasharray="7 5"/>')
    o.append(f'<line x1="{xa+amp:.1f}" y1="{y+alt}" x2="{xa+amp:.1f}" y2="{y_pct}" stroke="{NEG}" '
             f'stroke-width="2" stroke-dasharray="7 5"/>')
    o.append(f'<text x="{xa+amp/2:.1f}" y="{h-8}" text-anchor="middle" font-size="19" '
             f'font-weight="800" fill="{NEG}" {TIP}>{("%.1f" % pct).replace(".", ",")} %</text>')
    return env("".join(o), w, h), pct


DADES_U6 = [0, 1, 1, 1, 2, 2, 3, 4, 4]

G["BARRA_ESCALA"], xt = barra_escala()
G["REPARTIMENT"], mitj = repartiment(DADES_U6)
G["BARRA_PROB"], pct = barra_prob()

with open("grafics4.json", "w", encoding="utf-8") as f:
    json.dump(G, f)

print("Generats:", ", ".join(G))
print()
print("COMPROVACIONS")
print(f"  U2 · la vertical cau a x={xt:.0f} px, igual que el tall de BARRA_PARTIDA (430)")
print(f"  U2 · 240 € i 80 % han de compartir posició: {'SÍ' if abs(xt-430) < .01 else 'NO'}")
print(f"  U2 · els dos eixos tenen 5 trams: 300/5 = {300//5} € per tram, 100/5 = {100//5} % per tram")
print(f"  U6 · dades {DADES_U6} · suma {sum(DADES_U6)} · entre {len(DADES_U6)} = {mitj}")
print(f"  U6 · coincideix amb la taula de la pàgina 3 (18 ÷ 9 = 2): "
      f"{'SÍ' if sum(DADES_U6) == 18 and mitj == 2 else 'NO'}")
print(f"  U7 · 1 casella de {6} = {pct:.4f} % · arrodonit a la fitxa: {('%.1f' % pct).replace('.', ',')} %")
print(f"  U7 · coincideix amb la cadena de la pàgina 3 (16,7 %): "
      f"{'SÍ' if ('%.1f' % pct) == '16.7' else 'NO'}")
