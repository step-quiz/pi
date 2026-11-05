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
  · L'ESQUEMA curs → unitat → fitxa, quadern o caixa (5/11/2026): des de la unitat s'obre
    cada fitxa, targeta de consulta, quadern i la caixa d'eines, i l'enllaç de dalt de
    cadascuna (el que clica l'usuari) torna a la pàgina d'aquella mateixa unitat; la unitat
    torna a la portada; i el detall per al docent surt a la unitat.
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


def mateixa(a, b):
    """Dues adreces són la mateixa pàgina: mateix fitxer i mateixa consulta (?ud=N)."""
    pa, pb = urlparse(a), urlparse(b)
    return (pa.path, pa.query) == (pb.path, pb.query)


def puja(pag, desti, unitat_url, on):
    """Obre una pàgina del tercer nivell, clica l'enllaç de dalt i comprova que arriba a la unitat."""
    pag.goto(desti)
    pag.wait_for_timeout(200)
    enllac = pag.query_selector(".navega a:visible, .tornar a:visible")
    if not comprova(enllac is not None, f"{on}: {desti.rsplit('/', 1)[-1]} no té cap enllaç per tornar"):
        return
    pag.evaluate("() => document.querySelector('.navega a, .tornar a').scrollIntoView()")
    enllac.click()
    pag.wait_for_load_state()
    comprova(mateixa(pag.url, unitat_url),
             f"{on}: des de {desti.split('/')[-1].split('?')[0]} l'enllaç de dalt porta a {pag.url.split('/')[-1]} "
             f"i havia de portar a la unitat ({unitat_url.split('/')[-1]})")


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
                # El detall per al docent és a la unitat (abans era a fitxes.html).
                pag.goto(href)
                pag.wait_for_timeout(150)
                files = pag.evaluate("() => document.querySelectorAll('#docent:not([hidden]) #detall-unitat dt').length")
                comprova(files >= 4, f"{on}: el detall per al docent surt amb {files} files i en calen almenys 4")
                # Cada pàgina del tercer nivell (fitxes, targetes, quadern i caixa) torna a ESTA unitat.
                tercer = pag.evaluate("""() => [...document.querySelectorAll('#opcions a')]
                    .map(a => a.href).filter(h => !/\\.pdf(\\?|$)/.test(h))""")
                comprova(len(tercer) >= 2, f"{on}: la unitat només enllaça {len(tercer)} pàgines")
                for desti in tercer:
                    puja(pag, desti, href, on)
                # Enrere i endavant del navegador: unitat → fitxa → enrere = unitat → endavant = fitxa.
                pag.goto(href)
                pag.goto(tercer[0])
                pag.go_back()
                comprova(mateixa(pag.url, href), f"{on}: «enrere» des de {tercer[0].split('/')[-1]} no torna a la unitat")
                pag.go_forward()
                comprova(mateixa(pag.url, tercer[0]), f"{on}: «endavant» no torna a {tercer[0].split('/')[-1]}")
                # I la unitat torna a la portada.
                pag.goto(href)
                pag.click(".tornar a")
                comprova(mateixa(pag.url, (REPO / "index.html").as_uri()), f"{on}: «← inici» no porta a la portada ({pag.url})")
            print(f"  {curs['dir']}: {len(curs['unitats'])} unitats · fitxes, PDF, quadern i caixa d'eines provats")
        # La branca del professorat: portada → pàgina del curs → caixa sencera, i cap pàgina plana.
        for curs in cursos:
            index = (REPO / curs["dir"] / "index.html").as_uri()
            pag.goto(index)
            tria = pag.evaluate("() => [...document.querySelectorAll('.tria a')].map(a => a.getAttribute('href'))")
            comprova(not any(h in ("fitxes.html", "quadern.html") for h in tria),
                     f"{curs['dir']}/index.html enllaça una llista plana: {tria}")
            pag.click(".tornar a")
            comprova(mateixa(pag.url, (REPO / "index.html").as_uri()), f"{curs['dir']}/index.html: «← inici» no porta a la portada")
            pag.goto((REPO / curs["dir"] / "caixa-eines.html").as_uri())
            pag.wait_for_timeout(300)
            pag.click(".tornar a")
            comprova(mateixa(pag.url, index), f"{curs['dir']}/caixa-eines.html sense unitat: «← inici» ha de portar a {curs['dir']}/index.html i porta a {pag.url}")
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
