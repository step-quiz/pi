#!/usr/bin/env python3
"""
comu/eines/prova_portada.py · la portada i les pàgines de cada unitat, en un navegador
====================================================================================

    python3 comu/eines/prova_portada.py        (des de l'arrel del repositori)

Necessita Playwright amb Chromium:
    pip install playwright && python3 -m playwright install chromium

QUÈ COMPROVA
  · La portada (index.html): una columna per curs, amb totes les unitats de cada un.
  · Cada unitat (1eso/unitat.html?ud=N, 4eso/unitat.html?ud=N): el títol, que cada
    fitxa i cada PDF enllaçats existeixen, que el quadern porta al seu fitxer o surt
    apagat, i que la caixa d'eines s'obre amb exactament les pestanyes de la unitat i
    l'enllaç de tornada a la unitat.
  · Cap error de JavaScript.
"""
import os
import pathlib
import sys
from urllib.parse import urlparse, unquote

if os.path.isdir("/opt/pw-browsers"):
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("Cal Playwright: pip install playwright && python3 -m playwright install chromium")

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
falles = []


def comprova(cond, msg):
    if not cond:
        falles.append(msg)
    return cond


def fitxer(url):
    """El camí al disc d'un enllaç file://, sense la part de l'adreça que va després de ?."""
    return pathlib.Path(unquote(urlparse(url).path))


def main():
    with sync_playwright() as pw:
        nav = pw.chromium.launch()
        pag = nav.new_page(viewport={"width": 1000, "height": 900})
        errors = []
        pag.on("pageerror", lambda e: errors.append(str(e)))
        pag.goto((REPO / "index.html").as_uri())
        cursos = pag.evaluate("""() => [...document.querySelectorAll('.curs')].map(c => ({
            dir: c.dataset.dir, unitats: [...c.querySelectorAll('a.unitat')].map(a => a.href),
            esperades: (window[c.dataset.unitats] || []).length}))""")
        comprova(len(cursos) == 2, f"la portada ha de tenir dues columnes i en té {len(cursos)}")
        for curs in cursos:
            esperades = curs["esperades"]
            comprova(len(curs["unitats"]) == esperades and esperades,
                     f"{curs['dir']}: la portada té {len(curs['unitats'])} unitats i n'hi ha {esperades}")
            for href in curs["unitats"]:
                pag.goto(href)
                u = pag.evaluate("""() => {
                  const n = Number(new URLSearchParams(location.search).get('ud'));
                  const u = UNITATS.find(x => x.num === n);
                  return { n, tasques: u.tasques || [], quadern: u.quadern || '',
                    titol: document.querySelector('h1').textContent,
                    enllacos: [...document.querySelectorAll('#opcions a')].map(a => a.href),
                    caixa: (document.querySelector('a.tria-opcio[href*=caixa]') || {}).href || '',
                    quadernVist: (document.querySelector('a.tria-opcio[href*=quadern]') || {}).href || '' };
                }""")
                on = f"{curs['dir']}/unitat.html?ud={u['n']}"
                comprova(u["titol"].startswith(f"Unitat {u['n']} · "), f"{on}: el títol és «{u['titol']}»")
                for e in u["enllacos"]:
                    comprova(fitxer(e).exists(), f"{on}: l'enllaç {fitxer(e).relative_to(REPO)} no existeix")
                comprova(bool(u["quadernVist"]) == bool(u["quadern"]), f"{on}: el quadern no surt com toca")
                if u["tasques"]:
                    pag.goto(u["caixa"])
                    pag.wait_for_timeout(300)
                    vistes = pag.evaluate("""() => [...document.querySelectorAll('.segment[data-mod]')]
                        .filter(b => !b.hidden).map(b => Number(b.dataset.tasca))""")
                    comprova(sorted(vistes) == sorted(u["tasques"]),
                             f"{on}: la caixa ensenya les tasques {vistes} i havien de ser {u['tasques']}")
                    tornar = pag.get_attribute(".tornar a", "href")
                    comprova(tornar == f"unitat.html?ud={u['n']}", f"{on}: la caixa torna a «{tornar}»")
            print(f"  {curs['dir']}: {len(curs['unitats'])} unitats · fitxes, PDF, quadern i caixa d'eines provats")
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
