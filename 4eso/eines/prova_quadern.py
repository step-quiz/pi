#!/usr/bin/env python3
"""
eines/prova_quadern.py · els quaderns d'activitats, provats en un navegador
===========================================================================

Obre cada uN/quadern.html en Chromium i prova el filtre com ho faria el docent.

    python3 4eso/eines/prova_quadern.py

Necessita Playwright amb Chromium:
    pip install playwright && python3 -m playwright install chromium

QUÈ COMPROVA
  · Cap error de JavaScript.
  · Les sis combinacions del filtre (petit, mitjà, elevat; amb repte i sense): el nombre
    d'activitats no canvia amb la quantitat, «Amb repte» n'afegeix una per bloc, i cada
    activitat té l'a) i 3, 6 o 12 apartats per fer, amb les lletres seguides.
  · Que el solucionari amaga exactament les mateixes entrades, perquè els números
    coincideixin, i que el comptador dels números se salta les activitats amagades.
  · Que l'adreça (?n=1&repte=1) obre el filtre posat, i que els botons l'hi escriuen.
  · A la impressió: el quadern no porta el solucionari, i «Imprimeix el solucionari»
    només porta el solucionari. La barra del filtre no s'imprimeix mai.
"""
import glob
import os
import pathlib
import sys

if os.path.isdir("/opt/pw-browsers"):
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("Cal Playwright: pip install playwright && python3 -m playwright install chromium")

ARREL = pathlib.Path(__file__).resolve().parent.parent
falles = []


def comprova(cond, msg):
    if not cond:
        falles.append(msg)
    return cond


ESTAT = r"""() => {
  const vis = s => [...document.querySelectorAll(s)].filter(e => !e.hidden);
  // De cada activitat visible: si és de repte i les lletres dels apartats que es veuen.
  const lletres = e => [...e.querySelectorAll('.ap')].filter(a => !a.hidden && !a.closest('[hidden]'))
    .map(a => ((a.querySelector('.apartat, td') || a).textContent.match(/([a-z])\)/) || ['', '?'])[1]).join('');
  const marca = e => (e.hasAttribute('data-repte') ? 'R' : 'G');
  const acts = vis('.act');
  return {
    acts: acts.map(marca),
    sols: vis('.sol-act').map(marca),
    lletres: acts.map(lletres),
    lletresSol: vis('.sol-act').map(lletres),
    // Els números són comptadors CSS i el seu valor no es pot llegir des de la pàgina: es
    // comprova el mecanisme. El comptador es reinicia al quadern, cada activitat visible
    // suma 1 i les amagades no es pinten (display: none no compta).
    comptador: getComputedStyle(document.querySelector('.alumnat')).counterReset +
      ' · ' + [...new Set(acts.map(e => getComputedStyle(e).counterIncrement))].join() +
      ' · ' + [...new Set([...document.querySelectorAll('.act[hidden]')].map(e => getComputedStyle(e).display))].join(),
    text: document.getElementById('recompte').textContent,
    premuts: [...document.querySelectorAll('.filtres [aria-checked="true"]')].map(b => b.closest('[data-filtre]').dataset.filtre + '=' + b.dataset.valor),
  };
}"""


def main():
    quaderns = sorted(glob.glob(str(ARREL / "u[0-9]*" / "quadern.html")))
    if not quaderns:
        sys.exit("No hi ha cap quadern a les carpetes uN/.")
    with sync_playwright() as pw:
        nav = pw.chromium.launch()
        pag = nav.new_page(viewport={"width": 1000, "height": 900})
        errors = []
        pag.on("pageerror", lambda e: errors.append(str(e)))
        for q in quaderns:
            nom = os.path.relpath(q, ARREL)
            url = pathlib.Path(q).as_uri()
            quants = {}
            for n in (1, 2, 3):
                for r in (0, 1):
                    pag.goto(f"{url}?n={n}&repte={r}")
                    e = pag.evaluate(ESTAT)
                    quants[n, r] = len(e["acts"])
                    comprova(e["acts"] == e["sols"], f"{nom} n={n} repte={r}: el solucionari no amaga les mateixes")
                    comprova(e["comptador"] in ("act 0 · act 1 · none", "act 0 · act 1 · "),
                             f"{nom} n={n} repte={r}: el comptador dels números no va bé ({e['comptador']})")
                    comprova(r or "R" not in e["acts"], f"{nom} n={n} repte={r}: surt una activitat de repte")
                    bones = "abcdefghijklm"[:1 + {1: 3, 2: 6, 3: 12}[n]]
                    dolentes = [l for l in e["lletres"] if l != bones]
                    comprova(not dolentes, f"{nom} n={n} repte={r}: apartats {dolentes[:2]} (han de ser {bones})")
                    comprova(e["lletresSol"] == e["lletres"], f"{nom} n={n} repte={r}: el solucionari no té els mateixos apartats")
                    comprova(e["text"].startswith(f"{len(e['acts'])} activitats") and f"· {bones and len(bones) - 1} apartats a cada una" in e["text"],
                             f"{nom}: el recompte diu «{e['text']}»")
                    comprova(sorted(e["premuts"]) == sorted([f"n={n}", f"repte={r}"]),
                             f"{nom}: l'adreça ?n={n}&repte={r} no marca els botons ({e['premuts']})")
            comprova(quants[1, 0] == quants[2, 0] == quants[3, 0], f"{nom}: el nombre d'activitats canvia amb la quantitat ({quants})")
            comprova(all(quants[n, 1] == 2 * quants[n, 0] for n in (1, 2, 3)), f"{nom}: «Amb repte» n'ha d'afegir una per bloc ({quants})")

            # Els botons: canvien el filtre i l'escriuen a l'adreça.
            pag.goto(url)
            comprova(sorted(pag.evaluate(ESTAT)["premuts"]) == ["n=2", "repte=0"],
                     f"{nom}: sense paràmetres s'ha d'obrir a «Mitjana» i «Semblants als de la fitxa»")
            pag.click('[data-filtre="n"] button[data-valor="3"]')
            pag.click('[data-filtre="repte"] button[data-valor="1"]')
            comprova(len(pag.evaluate(ESTAT)["acts"]) == quants[3, 1], f"{nom}: els botons no canvien el filtre")
            comprova("n=3" in pag.url and "repte=1" in pag.url, f"{nom}: els botons no escriuen l'adreça ({pag.url})")

            # Pantalla: el solucionari no es veu mai; només s'imprimeix (decisió S4, 6/11/2026).
            comprova(not pag.is_visible("#solucionari"), f"{nom}: el solucionari es veu a la pantalla")
            comprova(pag.query_selector("#mostra-sol") is None, f"{nom}: «Mostra el solucionari» ja no hi ha de ser")

            # Impressió.
            pag.emulate_media(media="print")
            vist = lambda s: pag.evaluate(f"getComputedStyle(document.querySelector('{s}')).display") != "none"
            comprova(vist(".alumnat") and not vist("#solucionari") and not vist(".filtres"),
                     f"{nom}: a la impressió normal hi ha d'haver les activitats i prou")
            pag.evaluate("document.body.classList.add('nomes-sol')")
            comprova(not vist(".alumnat") and vist("#solucionari"),
                     f"{nom}: «Imprimeix el solucionari» ha de portar només el solucionari")
            pag.emulate_media(media="screen")
            print(f"  {nom}: {quants[1, 0]} activitats ({quants[1, 1]} amb repte), de 3, 6 o 12 apartats"
                  f" · filtre, solucionari i impressió provats")
        comprova(not errors, f"errors de JavaScript: {errors}")
        nav.close()
    if falles:
        print(f"\n{len(falles)} PROBLEMES:")
        for f in falles:
            print("  ·", f)
        sys.exit(1)
    print("\nTot correcte.")


if __name__ == "__main__":
    main()
