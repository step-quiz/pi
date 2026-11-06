#!/usr/bin/env python3
"""
comu/eines/prova_portada.py · the whole site map, clicked in a browser
=====================================================================

    python3 comu/eines/prova_portada.py        (from the repository root)

Needs Playwright with Chromium:
    pip install playwright && python3 -m playwright install chromium

WHAT IT CHECKS (comu/docs/SITE-MAP.md, 6/11/2026)
  · Home page (index.html): «Curs AAAA-AA», one column per course of comu/js/cursos.js with
    all its units, and a «Professorat» button per course. No header bar.
  · Course page (CURS/index.html): the violet header Inici › course, and the units.
  · Each unit page (CURS/uN/index.html): the header Inici › course › Unitat N with
    «Professorat»; the title; every «Obre» opens a page whose header goes back to THIS unit,
    to the course and to Inici; every PDF link points at a file that exists; the workbook card
    is a link or says «Quadern d'activitats no disponible»; «Obre les eines» opens
    CURS/eines.html?u=N with exactly the tools of the unit (own first, then the always-there
    ones) and no link at all; every reference card opens with the header of this unit.
  · The teacher page (CURS/professorat.html): header without the «Professorat» button.
  · No JavaScript error anywhere.
"""
import os
import pathlib
import re
import sys
from urllib.parse import urlparse, unquote

if os.path.isdir("/opt/pw-browsers"):
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("Cal Playwright: pip install playwright && python3 -m playwright install chromium")

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
# La secció del professorat, oberta o tancada: la línia «PI.professorat = …» de comu/js/web.js.
PROF = re.search(r"PI\.professorat = (true|false);", (REPO / "comu/js/web.js").read_text(encoding="utf-8"))[1] == "true"
falles = []


def comprova(cond, msg):
    if not cond:
        falles.append(msg)
    return cond


def fitxer(url):
    """El fitxer d'una adreça file:// (sense ?consulta)."""
    return pathlib.Path(unquote(urlparse(url).path)).resolve()


def cami(pag):
    """Els textos i els enllaços de la capçalera violeta: [(text, href o None)]."""
    return pag.evaluate("""() => [...document.querySelectorAll('.w-cap .w-cami > a, .w-cap .w-cami > .w-aqui')]
        .map(e => [e.textContent.trim(), e.tagName === 'A' ? e.href : null])""")


def main():
    cursos = re.findall(r'\{\s*id:\s*"([\w-]+)",\s*nom:\s*"([^"]+)"', (REPO / "comu" / "js" / "cursos.js").read_text(encoding="utf-8"))
    with sync_playwright() as pw:
        nav = pw.chromium.launch()
        pag = nav.new_page(viewport={"width": 1366, "height": 900})
        errors = []
        pag.on("pageerror", lambda e: errors.append(f"{pag.url}: {e}"))
        index = (REPO / "index.html").as_uri()

        print("PORTADA")
        pag.goto(index)
        pag.wait_for_selector(".w-curs")
        comprova(re.fullmatch(r"Curs \d{4}-\d{2}", pag.inner_text(".w-curs-escolar")), "portada: falta «Curs AAAA-AA»")
        comprova(pag.query_selector(".w-cap") is None, "portada: no ha de tenir la barra de la capçalera")
        unitats_de = {}
        for cid, nom in cursos:
            col = pag.query_selector(f'section.w-curs:has(h2:text-is("{nom}"))')
            if not comprova(col is not None, f"portada: falta la columna de {nom}"):
                continue
            hrefs = [a.get_attribute("href") for a in col.query_selector_all(".w-unitats a")]
            unitats_de[cid] = [int(re.search(r"/u(\d+)/", h)[1]) for h in hrefs]
            comprova(hrefs and all(re.fullmatch(cid + r"/u\d+/index\.html", h) for h in hrefs), f"portada: enllaços d'unitat de {cid}: {hrefs}")
            comprova((col.query_selector(f'a.w-prof[href="{cid}/professorat.html"]') is not None) == PROF, f"portada: «Professorat» de {cid} (obert: {PROF})")
            print(f"  {nom}: {len(hrefs)} unitats")

        for cid, nom in cursos:
            arrel = REPO / cid
            print(f"\n{cid}/")
            pag.goto((arrel / "index.html").as_uri())
            pag.wait_for_selector(".w-unitats")
            c = cami(pag)
            comprova([t for t, _ in c] == ["Inici", nom], f"{cid}/index.html: el camí és {c}")
            comprova(len(pag.query_selector_all(".w-unitats a")) == len(unitats_de.get(cid, [])), f"{cid}/index.html: no hi són totes les unitats")

            for n in unitats_de.get(cid, []):
                on = f"{cid}/u{n}/"
                unitat = (arrel / f"u{n}" / "index.html").as_uri()
                pag.goto(unitat)
                pag.wait_for_selector(".w-carta")
                c = cami(pag)
                comprova([t for t, _ in c] == ["Inici", nom, f"Unitat {n}"], f"{on}: el camí és {[t for t, _ in c]}")
                comprova(c and fitxer(c[0][1]) == fitxer(index), f"{on}: «Inici» no porta a la portada")
                comprova(len(c) > 1 and fitxer(c[1][1]) == (arrel / "index.html").resolve(), f"{on}: el curs no porta a {cid}/index.html")
                comprova((pag.query_selector('.w-cap a.w-prof') is not None) == PROF, f"{on}: «Professorat» (obert: {PROF})")
                comprova(pag.inner_text("h1").startswith(f"Unitat {n} · "), f"{on}: el títol és «{pag.inner_text('h1')}»")
                for a in pag.query_selector_all("a[download]"):
                    comprova(fitxer(a.evaluate("e => e.href")).exists(), f"{on}: el PDF {a.get_attribute('href')} no hi és")
                quadern = pag.query_selector('.w-carta:has(h2:text-is("Quadern d\'activitats"))')
                comprova(quadern is not None and (quadern.query_selector("a") is not None
                         or "Quadern d'activitats no disponible" in quadern.inner_text()), f"{on}: la targeta del quadern no és bona")
                obre = [a.evaluate("e => e.href") for a in pag.query_selector_all("a.w-principal")]
                eines = [h for h in obre if "/eines.html" in h]
                obre = [h for h in obre if "/eines.html" not in h]
                comprova(len(eines) == 1 and eines[0].endswith(f"eines.html?u={n}"), f"{on}: «Obre les eines» porta a {eines}")
                comprova(pag.query_selector("[data-w-copia]") is not None, f"{on}: falta «Copia l'enllaç»")

                # Cada pàgina de paper: la capçalera torna a aquesta unitat, al curs i a l'inici.
                for h in obre:
                    pag.goto(h)
                    pag.wait_for_selector("nav.navega .w-cap")
                    c = cami(pag)
                    desti = h.rsplit("/", 2)[-2] + "/" + h.rsplit("/", 1)[-1]
                    comprova(len(c) == 4 and c[2][0] == f"Unitat {n}" and fitxer(c[2][1]) == fitxer(unitat),
                             f"{on}: {desti} no torna a la unitat {n} ({[t for t, _ in c]})")
                    comprova(len(c) == 4 and fitxer(c[1][1]) == (arrel / "index.html").resolve() and fitxer(c[0][1]) == fitxer(index),
                             f"{on}: {desti}: el camí no porta al curs i a l'inici")
                    for a in pag.query_selector_all("nav.navega a[download]"):
                        comprova(fitxer(a.evaluate("e => e.href")).exists(), f"{on}: {desti}: el PDF {a.get_attribute('href')} no hi és")

                # Les eines de l'alumnat: només les de la unitat, i cap enllaç.
                dades = (arrel / "dades" / "unitats.js").read_text(encoding="utf-8")
                bloc = re.search(r"\bnum:\s*%d\b.*?tasques:\s*\[([^\]]*)\]" % n, dades, re.S)
                volgudes = [t.strip() for t in bloc[1].split(",") if t.strip()] if bloc else []
                pag.goto(eines[0] if eines else unitat)
                pag.wait_for_selector(".segment", state="attached"); pag.wait_for_timeout(150)
                # Menys llocs on clicar (6/11/2026): les eines del camp tasques, en aquest ordre, i cap més;
                # amb una sola, cap pestanya.
                visibles = pag.evaluate("() => [...document.querySelectorAll('.segment')].filter(b => !b.hidden).map(b => b.dataset.tasca)")
                comprova(visibles == volgudes, f"{on}: les eines són {visibles} i han de ser {volgudes}, en aquest ordre")
                barra = pag.evaluate("() => { const s = document.querySelector('.segments'); return !!s && !s.hidden && !s.closest('[hidden]'); }")
                comprova(barra == (len(volgudes) > 1), f"{on}: amb {len(volgudes)} eines, la fila de pestanyes {'no ' if not barra else ''}hi és")
                comprova(pag.inner_text("#w-cap-alumne").startswith(f"Unitat {n} · "), f"{on}: la capçalera de l'alumnat diu «{pag.inner_text('#w-cap-alumne')}»")
                enllacos = pag.evaluate("() => [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href'))")
                comprova(not enllacos, f"{on}: les eines de l'alumnat porten enllaços: {enllacos[:3]}")

                # Les targetes de la unitat: s'obren amb la capçalera d'aquesta unitat.
                pag.goto(unitat)
                pag.wait_for_selector(".w-carta")
                for h in [a.evaluate("e => e.href") for a in pag.query_selector_all('a[href*="/targetes/"]')]:
                    pag.goto(h)
                    pag.wait_for_selector("nav.navega .w-cap")
                    c = cami(pag)
                    comprova(len(c) == 4 and c[2][0] == f"Unitat {n}" and fitxer(c[2][1]) == fitxer(unitat),
                             f"{on}: la targeta {h.rsplit('/', 1)[-1]} no torna a la unitat {n}")
            print(f"  {len(unitats_de.get(cid, []))} unitats: fitxes, repassos, quaderns, targetes, PDF i eines provats")

            if not PROF:
                pag.goto((arrel / "professorat.html").as_uri())
                pag.wait_for_selector(".w-unitats")
                comprova(fitxer(pag.url) == (arrel / "index.html").resolve(), f"{cid}/professorat.html no torna al curs: {pag.url}")
                print("  professorat: tancat, torna a la pàgina del curs")
            pag.goto((arrel / "professorat.html").as_uri() + "?obert")
            pag.wait_for_selector(".w-cap")
            c = cami(pag)
            comprova([t for t, _ in c] == ["Inici", nom, "Professorat"], f"{cid}/professorat.html: el camí és {c}")
            comprova(pag.query_selector(".w-cap a.w-prof") is None, f"{cid}/professorat.html: no ha de tenir el botó «Professorat»")
            comprova(pag.inner_text("h1") == f"Professorat · {nom}", f"{cid}/professorat.html: el títol és «{pag.inner_text('h1')}»")
            print("  professorat: camí i títol")

        comprova(not errors, f"errors de JavaScript: {errors[:3]}")
        nav.close()
    falles[:] = [f for f in falles if f]
    if falles:
        print(f"\n{len(falles)} PROBLEMES:")
        for f in falles:
            print("  ·", f)
        sys.exit(1)
    print("\nTot correcte.")


if __name__ == "__main__":
    main()
