#!/usr/bin/env python3
"""Auditoria d'accessibilitat de la caixa d'eines, dins d'un navegador de veritat.

    pip install playwright --break-system-packages
    python3 -m playwright install chromium
    python3 1eso/eines/auditoria.py              # escriu l'informe per pantalla
    python3 1eso/eines/auditoria.py --md FITXER  # i, a més, en Markdown

És la de la caixa de 4eso/, amb els estats d'aquesta. Què mira, a cada
subtasca i als estats difícils (un error amb pista, el resum final, el
rectangle girat…), en mode clar i fosc, a 320 px (el mòbil més estret) i a
1100 px; i també a verifica.html i a textos.html:

  DIANES (WCAG 2.2, SC 2.5.8, nivell AA)
    Cada botó, camp, pestanya o dibuix que es toca ha de fer com a mínim
    24 × 24 px. Els enllaços dins d'una frase en queden exempts, com diu la norma.

  CONTRAST (WCAG 2.2, SC 1.4.3)
    Cada text visible, amb el color que calcula el navegador i el fons real,
    compost capa a capa amb les transparències. Text normal ≥ 4,5:1; text gran
    (24 px, o 18,66 px en negreta) ≥ 3:1. Els botons desactivats en queden
    exempts, com diu la norma. També els textos dels dibuixos SVG: els números
    de la vora de la taula de quadrets, els rètols de les claus…

  FOCUS
    Que cap element que es pot enfocar no tingui l'outline anul·lat del tot.

  LLETRA AL PAPER
    Les fitxes i les targetes, maquetades com al PDF: cap text de l'alumnat per
    sota de 14 pt, i cap rètol de dibuix per sota de 12 pt (de moment, avís).

Per què no és dins d'eines/comprova.py: aquell test no té dependències i es pot
passar a qualsevol ordinador. Aquest necessita un navegador. El contrast de la
paleta sí que és a comprova.py; aquí es comprova com queda aplicat de debò.
Les proves de funcionament (tocar, equivocar-se, acabar) són a prova_caixa.py.
"""
import os, re, sys

# Només si hi és: al Codespace, Playwright desa el Chromium a la seva carpeta
# de sempre, i forçar-ne una altra el faria petar.
if os.path.isdir("/opt/pw-browsers"):
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("Falta Playwright:  pip install playwright --break-system-packages\n"
             "                   python3 -m playwright install chromium")

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = lambda f: "file://" + os.path.join(ARREL, f)
DIANA = 24

# Els estats que s'auditen: (etiqueta, pàgina, adreça, què fer abans de mesurar).
# Els «què fer» provoquen l'estat difícil: un error amb pista, el resum final…
ESTATS = [
    ("0.1 La taula",                     "caixa-eines.html", "?task=0.1", None),
    ("0.1 La taula · tota la taula",     "caixa-eines.html", "?task=0.1", "taula_oberta"),
    ("0.2 Troba-ho · pista",             "caixa-eines.html", "?task=0.2", "taula_error"),
    ("0.2 Troba-ho · resum",             "caixa-eines.html", "?task=0.2", "taula_final"),
    ("0.3 El número que falta · pista",  "caixa-eines.html", "?task=0.3", "falta_error"),
    ("0.3 El número que falta · resolt", "caixa-eines.html", "?task=0.3", "falta_be"),
    ("1.1 Fes un rectangle",             "caixa-eines.html", "?task=1.1", None),
    ("1.2 El rectangle · pista",         "caixa-eines.html", "?task=1.2", "rect_error"),
    ("1.2 El rectangle · ensenyat",      "caixa-eines.html", "?task=1.2", "rect_dos_errors"),
    ("1.3 Gira · girat",                 "caixa-eines.html", "?task=1.3", "gira"),
    ("1.4 Parteix · partit",             "caixa-eines.html", "?task=1.4", "parteix"),
    ("2.1 El quadrat",                   "caixa-eines.html", "?task=2.1", None),
    ("2.2 Quin dibuix és? · error",      "caixa-eines.html", "?task=2.2", "dibuix_error"),
    ("2.3 El costat · 13 quadrets",      "caixa-eines.html", "?task=2.3", "tretze"),
    ("3.1 Centenes, desenes i unitats",  "caixa-eines.html", "?task=3.1", None),
    ("3.2 Fes el nombre · pista",        "caixa-eines.html", "?task=3.2", "nombre_error"),
    ("4.1 Mira l'ordre",                 "caixa-eines.html", "?task=4.1", None),
    ("4.2 Què es fa primer? · pista",    "caixa-eines.html", "?task=4.2", "ordre_error"),
    ("4.2 Què es fa primer? · resum",    "caixa-eines.html", "?task=4.2", "ordre_final"),
    ("5.1 La graella de 100 · el 3",     "caixa-eines.html", "?task=5.1", "graella_3"),
    ("5.2 És múltiple? · pista",         "caixa-eines.html", "?task=5.2", "sino_m2"),
    ("5.3 Els trucs",                    "caixa-eines.html", "?task=5.3", None),
    ("5.4 Múltiple de 3? · pista",       "caixa-eines.html", "?task=5.4", "sino_m4"),
    ("6.1 Reparteix en files",           "caixa-eines.html", "?task=6.1", None),
    ("6.2 Sobren quadrets? · pista",     "caixa-eines.html", "?task=6.2", "sino_s6"),
    ("6.2 Sobren quadrets? · resolt",    "caixa-eines.html", "?task=6.2", "sino_s6_be"),
    ("7.1 Els rectangles d'un nombre",   "caixa-eines.html", "?task=7.1", None),
    ("7.2 Troba els divisors · intrús",  "caixa-eines.html", "?task=7.2", "divisors_error"),
    ("7.2 Troba els divisors · resolt",  "caixa-eines.html", "?task=7.2", "divisors_be"),
    ("8.1 El garbell · acabat",          "caixa-eines.html", "?task=8.1", None),
    ("8.1 El garbell · al pas del 3",    "caixa-eines.html", "?task=8.1", "garbell_3"),
    ("8.2 És primer? · resolt",          "caixa-eines.html", "?task=8.2", "sino_p8_be"),
    ("9.1 Fes la fracció",               "caixa-eines.html", "?task=9.1", None),
    ("9.2 Quina fracció és? · tocada",   "caixa-eines.html", "?task=9.2", "primera_fb"),
    ("10.1 Parteix els trossos",         "caixa-eines.html", "?task=10.1", None),
    ("10.2 Són equivalents? · pista",    "caixa-eines.html", "?task=10.2", "sino_eb"),
    ("11.1 Compara dues fraccions",      "caixa-eines.html", "?task=11.1", None),
    ("11.2 Quina és més gran? · tocada", "caixa-eines.html", "?task=11.2", "primera_cb"),
    ("12.1 Suma i resta · la resta",     "caixa-eines.html", "?task=12.1", "resta_sa"),
    ("12.2 Quant és? · tocada",          "caixa-eines.html", "?task=12.2", "primera_sb"),
    ("13.1 Compta l'àrea",               "caixa-eines.html", "?task=13.1", None),
    ("13.2 Quina àrea té? · tocada",     "caixa-eines.html", "?task=13.2", "area_ab"),
    # Unitat 4: no hi eren (29/9/2026).
    ("14.1 Reparteix i pinta",           "caixa-eines.html", "?task=14.1", None),
    ("14.2 Quant és? · tocada",          "caixa-eines.html", "?task=14.2", "boto_fq"),
    ("15.1 El tros de tros",             "caixa-eines.html", "?task=15.1", None),
    ("15.2 Quin tros és? · tocada",      "caixa-eines.html", "?task=15.2", "boto_mg"),
    ("16.1 Pinta el percentatge",        "caixa-eines.html", "?task=16.1", None),
    ("16.2 Quin percentatge és? · tocada", "caixa-eines.html", "?task=16.2", "boto_pq"),
    ("17.1 El doble i el triple",        "caixa-eines.html", "?task=17.1", None),
    ("17.2 Quantes vegades? · tocada",   "caixa-eines.html", "?task=17.2", "boto_dq"),
    # Unitat 5.
    ("2.4 Entre quins dos nombres? · tocada", "caixa-eines.html", "?task=2.4", "boto_q4"),
    ("18.1 Fes el decimal",              "caixa-eines.html", "?task=18.1", None),
    ("18.2 Quin decimal és? · tocada",   "caixa-eines.html", "?task=18.2", "boto_xb"),
    ("18.3 Quin és més gran? · tocada",  "caixa-eines.html", "?task=18.3", "boto_xc"),
    ("19.1 El decimal a la recta",       "caixa-eines.html", "?task=19.1", None),
    ("19.2 Arrodoneix · tocada",         "caixa-eines.html", "?task=19.2", "boto_rb"),
    ("20.1 Suma i resta · la resta",     "caixa-eines.html", "?task=20.1", "resta_sc"),
    ("20.2 Quant és? · tocada",          "caixa-eines.html", "?task=20.2", "boto_sd"),
    ("21.1 Pinta la fracció",            "caixa-eines.html", "?task=21.1", None),
    ("21.2 De fracció a decimal · tocada", "caixa-eines.html", "?task=21.2", "boto_fd"),
    # Unitat 6.
    ("22.1 Obre l'angle",                "caixa-eines.html", "?task=22.1", None),
    ("22.2 Quin angle és? · tocada",     "caixa-eines.html", "?task=22.2", "boto_ao"),
    ("23.1 El polígon al geoplà",        "caixa-eines.html", "?task=23.1", None),
    ("23.2 Com es diu? · tocada",        "caixa-eines.html", "?task=23.2", "boto_pp"),
    ("24.1 Els tres angles",             "caixa-eines.html", "?task=24.1", None),
    ("24.2 Quin triangle és? · tocada",  "caixa-eines.html", "?task=24.2", "boto_ts"),
    ("25.1 Perímetre i àrea",            "caixa-eines.html", "?task=25.1", None),
    ("25.2 Quin és el perímetre? · tocada", "caixa-eines.html", "?task=25.2", "boto_pf"),
    # Unitat 7.
    ("26.1 El patró",                    "caixa-eines.html", "?task=26.1", None),
    ("26.2 Quants en té la següent? · tocada", "caixa-eines.html", "?task=26.2", "boto_pu"),
    ("27.1 La paraula i el símbol",      "caixa-eines.html", "?task=27.1", None),
    ("27.2 Quin és el símbol? · tocada", "caixa-eines.html", "?task=27.2", "boto_sz"),
    ("28.1 Llegeix el gràfic",           "caixa-eines.html", "?task=28.1", None),
    ("28.2 Quantes persones? · tocada",    "caixa-eines.html", "?task=28.2", "boto_gs"),
    ("Tota la caixa",                    "caixa-eines.html", "",          None),
    ("La portada",                       "index.html",       "",          None),
    ("Fitxes",                           "fitxes.html",      "",          None),
    ("Llegir codis",                     "verifica.html",    "",          None),
    ("Canviar les frases",               "textos.html",      "",          None),
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

def toca_cella(pg, sel, f, c):
    """El quadret de la fila f i la columna c de la taula de quadrets."""
    caixa = pg.locator(sel).bounding_box()
    pg.mouse.click(caixa["x"] + (36 + (c - 0.5) * 30) / 340 * caixa["width"],
                   caixa["y"] + (36 + (f - 0.5) * 30) / 340 * caixa["height"])


def dos_numeros(pg, sel):
    return [int(x) for x in re.findall(r"\d+", pg.inner_text(sel))][:2]


def prepara(pg, accio):
    """Porta la pàgina a l'estat difícil que es vol auditar."""
    if accio == "taula_oberta":
        pg.click("#tt-veure")
    elif accio in ("taula_error", "taula_final"):
        for pas in range(5 if accio == "taula_final" else 1):
            a, b = dos_numeros(pg, "#tb-pregunta")
            if accio == "taula_error":
                pg.click(f"#tb-pastilles .pastilla >> nth={(a % 10)}")      # una altra taula
                pg.click("#tb-llista .fila-taula >> nth=0")
                break
            pg.click(f"#tb-pastilles .pastilla >> nth={a - 1}")
            pg.click(f"#tb-llista .fila-taula >> nth={b - 1}")
            pg.click("#tb-seguent")
    elif accio in ("falta_error", "falta_be"):
        k, p_ = dos_numeros(pg, "#tf-expr")
        if accio == "falta_error":
            pg.click(f"#tf-pastilles .pastilla >> nth={(k % 10)}")        # una altra taula
            pg.click("#tf-llista .fila-taula >> nth=0")
        else:
            pg.click(f"#tf-pastilles .pastilla >> nth={k - 1}")
            pg.click(f"#tf-llista .fila-taula >> nth={p_ // k - 1}")
    elif accio in ("rect_error", "rect_dos_errors"):
        toca_cella(pg, "#r2-svg", 9, 9)
        if accio == "rect_dos_errors":
            toca_cella(pg, "#r2-svg", 10, 10)
    elif accio == "gira":
        pg.click("#r3-gira")
    elif accio == "parteix":
        pg.click("#r4-parteix")
    elif accio == "dibuix_error":
        dolent = "d" if "²" in pg.inner_text("#q2-pregunta") else "q"
        pg.click(f'#q2-opcions .opcio-dibuix[data-o="{dolent}"]')
    elif accio == "tretze":
        for _ in range(3):
            pg.click("#q3-quants [data-f=menys]")
    elif accio == "nombre_error":
        pg.click("#n2-comprova")
    elif accio in ("ordre_error", "ordre_final"):
        for pas in range(5 if accio == "ordre_final" else 1):
            par = "(" in pg.inner_text("#o2-expr")
            bo, dolent = ("suma", "mult") if par else ("mult", "suma")
            if accio == "ordre_error":
                pg.click(f'#o2-expr .signe[data-op="{dolent}"]')
                break
            pg.click(f'#o2-expr .signe[data-op="{bo}"]')
            pg.click("#o2-seguent")
    elif accio == "graella_3":
        pg.click("#m1-pastilles .pastilla >> nth=1")
    elif accio and accio.startswith("sino_"):
        # una tasca de Sí o No: la resposta dolenta (la pista) o la bona (el dibuix)
        pref = accio.split("_")[1]
        nums = [int(x) for x in re.findall(r"\d+", pg.inner_text(f"#{pref}-pregunta"))]
        bo = {"m2": lambda: nums[0] % nums[1] == 0, "m4": lambda: nums[0] % 3 == 0,
              "s6": lambda: nums[0] % nums[1] != 0,
              "p8": lambda: nums[0] > 1 and all(nums[0] % q for q in range(2, int(nums[0] ** 0.5) + 1)),
              "eb": lambda: nums[0] * nums[3] == nums[1] * nums[2]}[pref]()
        resp = bo if accio.endswith("_be") else not bo
        pg.click(f'#{pref}-opcions .opcio-sino[data-v="{"si" if resp else "no"}"]')
    elif accio in ("divisors_error", "divisors_be"):
        n = int(re.findall(r"\d+", pg.inner_text("#d8-pregunta"))[0])
        for v in range(1, n + 1):
            if n % v == 0 or (accio == "divisors_error" and v == next(x for x in range(2, n) if n % x)):
                pg.click(f'#d8-pastilles .pastilla[data-v="{v}"]')
        pg.click("#d8-comprova")
    elif accio and accio.startswith("primera_"):
        # una tasca de triar una fracció: la primera opció, encertada o no
        pg.click(f"#{accio.split('_')[1]}-opcions .opcio-frac >> nth=0")
    elif accio == "area_ab":
        pg.click("#ab-opcions .opcio-area >> nth=0")
    elif accio == "resta_sa":
        pg.click("#sa-op .pastilla >> nth=1")
    elif accio and accio.startswith("boto_"):
        # una tasca de triar entre botons (unitats 4 i 5): la primera opció, encertada o no
        pg.click(f"#{accio.split('_')[1]}-opcions button >> nth=0")
    elif accio == "resta_sc":
        pg.click("#sc-ops .pastilla >> nth=3")
    elif accio == "garbell_3":
        pg.click("#g8-comenca")
        for _ in range(3):
            pg.click("#g8-avant")
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
    return (sorted(glob.glob(os.path.join(ARREL, "fitxes", "ud*.html")))
            + sorted(glob.glob(os.path.join(ARREL, "targetes", "*.html"))))


def CSS_PDF():
    """El full d'estil dels PDF, el mateix d'eines/paper.py (que només fa servir la
    biblioteca estàndard: no cal WeasyPrint)."""
    import re
    sys.path.insert(0, os.path.join(ARREL, "eines"))
    import paper
    return re.sub(r"@page\s*\{[^}]*\}", "", paper.FULL_PDF)


# Als rètols dels dibuixos, de moment només avisa: els números de dins de les
# graelles de 100 (unitats 2 i 4) i els dels angles dels triangles de la unitat 6
# són més petits, i fer-los créixer demana redibuixar-los. La resta ja fan 12 pt
# (6/10/2026). Quan estiguin fets, es posa a True.
DIBUIXOS_OBLIGATORIS = False

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
                for etiqueta, pagina, adreca, accio in ESTATS:
                    pg.goto(URL(pagina) + adreca)
                    pg.evaluate("localStorage.clear()")
                    pg.goto(URL(pagina) + adreca)
                    # A la caixa, les eines es carreguen quan s'obren (CE.carrega): s'espera
                    # que ja hi siguin abans de mesurar res.
                    pg.evaluate("async () => { if (window.CE && CE.carregaTots) await CE.carregaTots(); }")
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
