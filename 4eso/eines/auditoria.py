#!/usr/bin/env python3
"""Auditoria d'accessibilitat de la caixa d'eines, dins d'un navegador de veritat.

    pip install playwright --break-system-packages
    python3 -m playwright install chromium
    python3 eines/auditoria.py              # escriu l'informe per pantalla
    python3 eines/auditoria.py --md FITXER  # i, a més, en Markdown

Què mira, a cada mòdul i a cada subtasca, en mode clar i fosc, a 320 px (el
mòbil més estret) i a 1100 px:

  DIANES (WCAG 2.2, SC 2.5.8, nivell AA)
    Cada botó, camp, pestanya o dibuix que es toca ha de fer com a mínim
    24 × 24 px. Els enllaços dins d'una frase en queden exempts, com diu la norma.

  CONTRAST (WCAG 2.2, SC 1.4.3)
    Cada text visible, amb el color que calcula el navegador i el fons real,
    compost capa a capa amb les transparències. Text normal ≥ 4,5:1; text gran
    (24 px, o 18,66 px en negreta) ≥ 3:1. Els botons desactivats en queden
    exempts, com diu la norma. També els textos dels dibuixos SVG.

  FOCUS
    Que cap element que es pot enfocar no tingui l'outline anul·lat del tot.

  LLETRA AL PAPER
    Les fitxes, maquetades com al PDF: cap text de l'alumnat per
    sota de 14 pt, i cap rètol de dibuix per sota de 12 pt.

Per què no és dins d'eines/comprova.py: aquell test no té dependències i es pot
passar a qualsevol ordinador. Aquest necessita un navegador. El contrast de la
paleta sí que és a comprova.py; aquí es comprova com queda aplicat de debò.
"""
import os, sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("Falta Playwright:  pip install playwright --break-system-packages\n"
             "                   python3 -m playwright install chromium")

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = "file://" + os.path.join(ARREL, "caixa-eines.html")
DIANA = 24

# Els estats que s'auditen: (etiqueta, adreça, què fer abans de mesurar).
# Els «què fer» provoquen l'estat difícil: un error amb pista, el resum final…
ESTATS = [
    ("0 Calculadora",               "?task=0",   None),
    ("0 Calculadora · resum",       "?task=0",   "calc_final"),
    ("1 Recta · amb fletxes",       "?task=1",   None),
    ("1.1 Recta",                   "?task=1.1", None),
    ("1.2 Situa · pista",           "?task=1.2", "posa_error"),
    ("1.3 S'acaba?",                "?task=1.3", None),
    ("1.4 Arrodonir",               "?task=1.4", None),
    ("1.5 Valor posicional",        "?task=1.5", None),
    ("1.6 Unitats",                 "?task=1.6", None),
    ("2 Doble recta",               "?task=2",   None),
    ("3 Percentatges",              "?task=3",   None),
    ("4 Escales",                   "?task=4",   None),
    ("5 Paràboles · pista",         "?task=5",   "par_error"),
    ("6 Equacions",                 "?task=6",   None),
    ("7 Com ho dic",                "?task=7",   None),
]

JS_MESURA = r"""
(DIANA) => {
  const visible = el => {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) return false;
    for (let n = el; n && n.nodeType === 1; n = n.parentElement) {
      const s = getComputedStyle(n);
      if (s.display === "none" || s.visibility === "hidden" || +s.opacity === 0) return false;
    }
    return true;
  };
  const nom = el => (el.id ? "#" + el.id : el.tagName.toLowerCase() +
    (el.className && typeof el.className === "string" ? "." + el.className.trim().split(/\s+/).join(".") : "")) +
    (el.textContent.trim() ? " «" + el.textContent.trim().slice(0, 28) + "»" : "");

  // ---- dianes
  const dianes = [];
  const tocables = [...document.querySelectorAll(
    "button, a[href], input, select, textarea, [role=tab], [tabindex='0'], .tecla.ara")];
  // les capes de clic dels dibuixos: un <rect> transparent amb cursor de mà
  document.querySelectorAll("svg rect[fill=transparent]").forEach(r => tocables.push(r));
  for (const el of tocables) {
    if (!visible(el)) continue;
    const r = el.getBoundingClientRect();
    const dinsFrase = el.tagName === "A" && getComputedStyle(el).display === "inline";
    if (!dinsFrase && (r.width < DIANA - 0.5 || r.height < DIANA - 0.5))
      dianes.push({ el: nom(el), w: Math.round(r.width), h: Math.round(r.height) });
  }

  // ---- contrast
  const rgba = t => { const m = t.match(/rgba?\(([^)]+)\)/); if (!m) return null;
    const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number);
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 }; };
  const sobre = (c, f) => ({ r: c.r * c.a + f.r * (1 - c.a), g: c.g * c.a + f.g * (1 - c.a),
                             b: c.b * c.a + f.b * (1 - c.a), a: 1 });
  const fonsDe = el => {                       // compon totes les capes de fons
    const capes = [];
    for (let n = el; n && n.nodeType === 1; n = n.parentElement) {
      const c = rgba(getComputedStyle(n).backgroundColor);
      if (c && c.a > 0) capes.push(c);
    }
    let f = { r: 255, g: 255, b: 255, a: 1 };
    const html = rgba(getComputedStyle(document.documentElement).backgroundColor);
    const body = rgba(getComputedStyle(document.body).backgroundColor);
    if (body && body.a > 0) f = sobre(body, f); else if (html && html.a > 0) f = sobre(html, f);
    for (let i = capes.length - 1; i >= 0; i--) f = sobre(capes[i], f);
    return f;
  };
  const lin = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
  const L = c => 0.2126 * lin(c.r) + 0.7152 * lin(c.g) + 0.0722 * lin(c.b);
  const ratio = (a, b) => { const x = L(a), y = L(b); return (Math.max(x, y) + .05) / (Math.min(x, y) + .05); };

  const textos = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const vistos = new Set();
  let nt;
  while ((nt = walker.nextNode())) {
    const el = nt.parentElement;
    if (!el || vistos.has(el) || !nt.textContent.trim()) continue;
    vistos.add(el);
    if (!visible(el)) continue;
    if (el.closest("button:disabled")) continue;          // inactiu: exempt
    const s = getComputedStyle(el);
    const svg = el.closest("svg");
    let color = rgba(svg ? (s.fill && s.fill !== "none" ? s.fill : s.color) : s.color);
    if (!color) continue;
    let fons = fonsDe(svg ? svg : el);
    if (svg) {                  // el fons real d'un text SVG: la forma de sota, si n'hi ha
      const b = el.getBoundingClientRect();
      const sota = document.elementsFromPoint(b.x + b.width / 2, b.y + b.height / 2)
        .find(n => n !== el && n.closest("svg") === svg && /^(rect|circle|path)$/.test(n.tagName) &&
                   (rgba(getComputedStyle(n).fill) || { a: 0 }).a > 0);
      if (sota) fons = sobre(rgba(getComputedStyle(sota).fill), fons);
    }
    color = sobre(color, fons);
    const mida = parseFloat(s.fontSize) * (svg ? svg.getBoundingClientRect().width / svg.viewBox.baseVal.width : 1);
    const negreta = parseInt(s.fontWeight, 10) >= 700 || (svg && parseInt(el.getAttribute("font-weight") || "0", 10) >= 700);
    const gran = mida >= 24 || (negreta && mida >= 18.66);
    const minim = gran ? 3 : 4.5;
    const r = ratio(color, fons);
    if (r < minim - 0.005) textos.push({ el: nom(el), r: +r.toFixed(2), minim, mida: +mida.toFixed(1) });
  }

  // ---- focus: cap outline anul·lat sense alternativa
  const focus = [];
  for (const el of document.querySelectorAll("button, a[href], input, select, [tabindex='0']")) {
    if (!visible(el)) continue;
    el.focus({ preventScroll: true });
    const s = getComputedStyle(el);
    if (el.matches(":focus-visible") && s.outlineStyle === "none" && s.boxShadow === "none")
      focus.push(nom(el));
  }
  if (document.activeElement) document.activeElement.blur();
  return { dianes, textos, focus, n: tocables.length };
}
"""


def prepara(pg, accio):
    """Porta la pàgina a l'estat difícil que es vol auditar."""
    if accio == "calc_final":
        for k in ["2", "5", "x", "0", ".", "8", "Enter"]:
            pg.keyboard.press(k)
    elif accio == "posa_error":
        v = float(pg.inner_text("#posa-valor").replace(",", "."))
        box = pg.locator("#posa-svg").bounding_box()
        t = 5.8 if v < 3 else 0.2
        pg.mouse.click(box["x"] + (34 + t / 6 * 592) / 660 * box["width"],
                       box["y"] + 84 / 160 * box["height"])
    elif accio == "par_error":
        pg.click("#par-seguent")                       # de l'exemple al pas 2
        box = pg.locator("#par-svg").bounding_box()
        pg.mouse.click(box["x"] + box["width"] * .45, box["y"] + box["height"] * .3)
    pg.wait_for_timeout(80)



# ------------------------------------------------------------------ el paper
# LA LLETRA AL PAPER (29/9/2026). La regla 4 (cos de 14 pt cap amunt) només es
# podia mirar a ull. Aquí es mesura cada text de les pàgines de l'alumnat tal com
# surt al PDF: amb el full d'estil dels PDF i l'amplada útil d'un A4 (18,2 cm).
# Els dibuixos (SVG) s'escalen: un rètol de 15 en un dibuix de 560 d'ample que
# ocupa 12 cm fa 9 pt, encara que el codi digui «15». El solucionari, el rètol
# del graó físic (.previ) i el peu de pàgina són per a l'adult i no hi compten.
PAPER_MIN_TEXT = 14          # el text de l'alumnat
PAPER_MIN_DIBUIX = 12        # els rètols dels dibuixos
AMPLE_A4 = round((21 - 2 * 1.4) / 2.54 * 96)     # l'amplada útil d'un A4, en px

JS_LLETRA = r"""
() => {
  const res = [];
  const fulls = [...document.querySelectorAll('.full')];
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n;
  while ((n = w.nextNode())) {
    const t = n.textContent.trim(); if (!t) continue;
    const el = n.parentElement, full = el.closest('.full');
    if (!full || full.classList.contains('sol') || el.closest('.previ, .pag, .no-imprimir')) continue;
    if (el.closest('[aria-hidden="true"]') && el.closest('svg')) continue;   // els halos blancs
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    let px = parseFloat(cs.fontSize); const svg = !!el.closest('svg');
    if (svg) { const m = el.getScreenCTM(); if (m) px *= Math.hypot(m.a, m.b); }
    res.push([Math.round(px * 0.75 * 10) / 10, svg, fulls.indexOf(full) + 1, t.slice(0, 24)]);
  }
  return res;
}
"""


def lletra_al_paper(nav):
    """Torna (quants textos, problemes, avisos) de totes les pàgines de paper."""
    import glob
    fitxers = FITXERS_PAPER()
    ctx = nav.new_context(viewport={"width": AMPLE_A4, "height": 1000})
    pg = ctx.new_page()
    pg.emulate_media(media="print")
    n, problemes, avisos = 0, [], []
    for f in fitxers:
        pg.goto("file://" + f)
        pg.add_style_tag(content=CSS_PDF() + " html, body { margin: 0 !important; padding: 0 !important }")
        pg.wait_for_timeout(60)
        petits_dibuix = []
        for pt, svg, pag, text in pg.evaluate(JS_LLETRA):
            n += 1
            nom = os.path.relpath(f, ARREL)
            if not svg and pt < PAPER_MIN_TEXT - .05:
                problemes.append(f"- {nom}, pàgina {pag}: «{text}» fa {pt} pt (el mínim és {PAPER_MIN_TEXT})")
            elif svg and pt < PAPER_MIN_DIBUIX - .05:
                petits_dibuix.append((pt, pag, text))
        if petits_dibuix:
            pitjor = min(petits_dibuix)
            linia = (f"- {os.path.relpath(f, ARREL)}: {len(petits_dibuix)} rètols de dibuix per sota de "
                     f"{PAPER_MIN_DIBUIX} pt (el més petit, «{pitjor[2]}», fa {pitjor[0]} pt, pàgina {pitjor[1]})")
            (problemes if DIBUIXOS_OBLIGATORIS else avisos).append(linia)
    ctx.close()
    return n, problemes, avisos


def FITXERS_PAPER():
    import glob
    return sorted(glob.glob(os.path.join(ARREL, "fitxes", "ud*.html")))


def CSS_PDF():
    """El full d'estil dels PDF, llegit de generadors/gen_pdf.py sense importar-lo:
    importar-lo demanaria WeasyPrint, i aquesta auditoria no el necessita."""
    import re
    font = open(os.path.join(ARREL, "generadors", "gen_pdf.py"), encoding="utf-8").read()
    css = re.search(r'FULL_PDF = """(.*?)"""', font, re.S).group(1)
    return re.sub(r"@page\s*\{[^}]*\}", "", css)


# Als rètols dels dibuixos, el mínim de 12 pt és obligatori: tots els gràfics de les
# fitxes surten de generadors/ i s'hi van ajustar el 29/9/2026.
DIBUIXOS_OBLIGATORIS = True

def main():
    md = sys.argv[sys.argv.index("--md") + 1] if "--md" in sys.argv else None
    files, problemes = [], 0
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for mode in ("light", "dark"):
            for ample in (320, 1100):
                ctx = nav.new_context(viewport={"width": ample, "height": 900}, color_scheme=mode,
                                      reduced_motion="reduce")
                pg = ctx.new_page()
                for etiqueta, adreca, accio in ESTATS:
                    pg.goto(URL + adreca)
                    pg.evaluate("localStorage.clear()")
                    pg.goto(URL + adreca)
                    pg.wait_for_timeout(120)
                    prepara(pg, accio)
                    r = pg.evaluate(JS_MESURA, DIANA)
                    n = len(r["dianes"]) + len(r["textos"]) + len(r["focus"])
                    problemes += n
                    files.append((mode, ample, etiqueta, r))
                ctx.close()
        n_paper, prob_paper, avisos_paper = lletra_al_paper(nav)
        nav.close()

    linies = ["| Mode | Amplada | Estat | Dianes < 24 px | Textos sense contrast | Focus anul·lat |",
              "|---|---|---|---|---|---|"]
    detall = []
    for mode, ample, etiqueta, r in files:
        linies.append(f"| {'clar' if mode == 'light' else 'fosc'} | {ample} | {etiqueta} | "
                      f"{len(r['dianes'])} | {len(r['textos'])} | {len(r['focus'])} |")
        for d in r["dianes"]:
            detall.append(f"- {etiqueta} ({mode}, {ample} px): diana {d['el']} fa {d['w']}×{d['h']} px")
        for t in r["textos"]:
            detall.append(f"- {etiqueta} ({mode}, {ample} px): {t['el']} fa {t['r']}:1 "
                          f"(en cal {t['minim']}:1, lletra de {t['mida']} px)")
        for f in r["focus"]:
            detall.append(f"- {etiqueta} ({mode}, {ample} px): {f} no té indicador de focus")
    informe = "\n".join(linies) + "\n\n" + ("\n".join(detall) if detall else "Cap problema.") + "\n"
    problemes += len(prob_paper)
    informe += (f"\nLLETRA AL PAPER (com al PDF): {n_paper} textos de l'alumnat. Text: {PAPER_MIN_TEXT} pt "
                f"com a mínim; rètols dels dibuixos: {PAPER_MIN_DIBUIX} pt"
                f"{'' if DIBUIXOS_OBLIGATORIS else ' (de moment, només avís)'}.\n")
    informe += ("\n".join(prob_paper) if prob_paper else "Cap problema.") + "\n"
    if avisos_paper:
        informe += "\nAvisos (no compten com a problema):\n" + "\n".join(avisos_paper) + "\n"
    print(informe)
    if md:
        open(md, "w", encoding="utf-8").write(informe)
    print(f"{problemes} problemes en {len(files)} estats auditats i {len(FITXERS_PAPER())} pàgines de paper.")
    sys.exit(1 if problemes else 0)


if __name__ == "__main__":
    main()
