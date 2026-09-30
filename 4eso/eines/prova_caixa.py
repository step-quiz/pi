#!/usr/bin/env python3
"""
eines/prova_caixa.py · la caixa d'eines, provada de debò en un navegador
=========================================================================

Obre caixa-eines.html en Chromium i fa el que faria l'alumnat: obre cada
pestanya, mou els punts, prova valors i acaba una tasca tancada. Després llegeix
el codi a verifica.html. Si alguna cosa no respon com diu la documentació, ho
diu i acaba amb error. Com a 1eso/eines/prova_caixa.py (30/9/2026).

    python3 4eso/eines/prova_caixa.py

Necessita Playwright amb Chromium:
    pip install playwright && python3 -m playwright install chromium

QUÈ COMPROVA
  · Cap error de JavaScript i cap frase sense definir («[5.titol]»), a cap pestanya.
  · Els enllaços ?task=n: només la Calculadora i la tasca n. ?task=1.2 obre
    l'exercici 2 sense les fletxes per passar als altres.
  · Que cada mòdul respon: la doble recta es mou alhora, l'escala es calcula
    en els dos sentits, la balança diu quan equilibra, aplanar acaba a la
    mitjana i la barra del dau dona el tant per cent de Laplace.
  · Una tasca tancada de punta a punta (les equacions, x² = 36): el comptador,
    el resum, el codi i que verifica.html el llegeix i hi posa nom.

No substitueix auditoria.py (contrast i mides, en clar i en fosc): el
complementa. Les dues s'han de passar abans de lliurar.
"""
import os
import pathlib
import re
import sys

if os.path.isdir("/opt/pw-browsers"):
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("Cal Playwright: pip install playwright && python3 -m playwright install chromium")

ARREL = pathlib.Path(__file__).resolve().parent.parent
CAIXA = (ARREL / "caixa-eines.html").as_uri()
VERIFICA = (ARREL / "verifica.html").as_uri()

errors = []


def comprova(condicio, missatge):
    if not condicio:
        errors.append(missatge)
        print("  ✗", missatge)
    return condicio


def titol(t):
    print("\n" + t)


def obre(pg, url=CAIXA):
    pg.goto(url)
    pg.evaluate("localStorage.clear()")
    pg.goto(url)
    pg.wait_for_timeout(200)


def text(pg, sel):
    return pg.inner_text(sel).replace(" ", " ")


def revisa_pantalla(pg, on):
    visible = pg.evaluate("() => (document.querySelector('.modul:not([hidden])') || document.body).innerText")
    sense_definir = re.findall(r"\[[\w.]+\]", visible)
    comprova(not sense_definir, f"{on}: frase sense definir: {sense_definir}")
    comprova("undefined" not in visible and "NaN" not in visible, f"{on}: surt «undefined» o «NaN»")


def main():
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pg = nav.new_page(viewport={"width": 1100, "height": 900})
        consola = []
        pg.on("pageerror", lambda e: consola.append("error de pàgina: " + str(e)))
        pg.on("console", lambda m: consola.append(m.text) if m.type == "error" else None)

        # ------------------------------------------------------------------
        titol("TOTES LES PESTANYES S'OBREN")
        obre(pg)
        botons = pg.eval_on_selector_all(".segment[data-mod]",
                                         "bs => bs.map(b => [b.dataset.tasca, b.dataset.mod, b.textContent.trim()])")
        for tasca, mod, nom in botons:
            pg.click(f'.segment[data-mod="{mod}"]')
            pg.wait_for_timeout(120)
            comprova(pg.is_visible(f"#mod-{mod}"), f"la pestanya {nom} no ensenya #mod-{mod}")
            revisa_pantalla(pg, f"tasca {tasca} ({nom})")
        print(f"  pestanyes obertes: {len(botons)}")

        # ------------------------------------------------------------------
        titol("ENLLAÇOS ?task=n")
        for tasca, mod, nom in botons:
            obre(pg, CAIXA + f"?task={tasca}")
            visibles = pg.eval_on_selector_all(".segment[data-mod]", "bs => bs.filter(b => !b.hidden).map(b => b.dataset.tasca)")
            esperat = ["0"] if tasca == "0" else ["0", tasca]
            comprova(visibles == esperat, f"?task={tasca}: es veuen les pestanyes {visibles}, i n'havien de ser {esperat}")
            comprova(pg.is_visible(f"#mod-{mod}"), f"?task={tasca} no obre {nom}")
        obre(pg, CAIXA + "?task=1.2")
        comprova(not pg.is_visible("#mod-recta .sub-avant") and not pg.is_visible("#mod-recta .sub-enrere"),
                 "?task=1.2 ensenya les fletxes per passar als altres exercicis")
        comprova(re.match(r"\s*1\.2", text(pg, "#mod-recta .sub-rotul")), "?task=1.2 no obre l'exercici 1.2")
        revisa_pantalla(pg, "?task=1.2")
        print(f"  enllaços provats: {len(botons) + 1}")

        # ------------------------------------------------------------------
        titol("ELS MÒDULS RESPONEN")
        # La doble recta: el cas d'exemple són 300 € i 80 %; un pas més a la dreta ho mou tot.
        obre(pg, CAIXA + "?task=2")
        abans = text(pg, "#dr-lectura")
        pg.click("#dr-mes"); pg.wait_for_timeout(60)
        despres = text(pg, "#dr-lectura")
        comprova(abans != despres and "%" in despres, f"doble recta: el punt no es mou ({abans} → {despres})")
        pg.click("#dr-pastilles .pastilla >> text=Equació x + 3 = 7"); pg.wait_for_timeout(60)
        comprova("x + 3" in pg.text_content("#dr-svg"),
                 "doble recta: el cas de l'equació no dibuixa la recta de x + 3")

        # L'escala: 8 cm a 1 : 100 són 8 m, i al revés.
        obre(pg, CAIXA + "?task=4")
        pg.fill("#e-planol", "8"); pg.dispatch_event("#e-planol", "input"); pg.wait_for_timeout(60)
        comprova(pg.input_value("#e-real") == "8", f"escala 1 : 100: 8 cm haurien de ser 8 m, i surt {pg.input_value('#e-real')}")
        pg.fill("#e-real", "5"); pg.dispatch_event("#e-real", "input"); pg.wait_for_timeout(60)
        comprova(pg.input_value("#e-planol") == "5", f"escala 1 : 100: 5 m haurien de ser 5 cm, i surt {pg.input_value('#e-planol')}")

        # Aplanar (U6): les columnes dels gols acaben a 2, la mitjana.
        obre(pg, CAIXA + "?task=8")
        comprova("Encara" in text(pg, "#mj-lectura"), "aplanar: al principi ja diu que fan igual")
        pg.click("#mj-tot"); pg.wait_for_timeout(60)
        comprova("La mitjana és 2" in text(pg, "#mj-lectura"), f"aplanar: la mitjana dels gols no surt 2 ({text(pg, '#mj-lectura')})")
        comprova("18 ÷ 9 = 2" in text(pg, "#mj-simbolic"), "aplanar: el compte no diu 18 ÷ 9 = 2")

        # La barra del dau (U7): un parell són 3 de 6, el 50 %.
        obre(pg, CAIXA + "?task=9")
        comprova("16,7 %" in text(pg, "#at-lectura"), "probabilitat: el cas d'exemple (un 5) no diu 16,7 %")
        pg.click("#at-pastilles .pastilla >> nth=1")
        for n in (1, 3, 5):
            pg.click(f"#at-cares .pastilla >> nth={n}")
        comprova("Correcte" in text(pg, "#at-lectura") and "50 %" in text(pg, "#at-lectura"),
                 f"probabilitat: un parell hauria de ser «Correcte» i 50 % ({text(pg, '#at-lectura')})")

        # ------------------------------------------------------------------
        titol("UNA TASCA TANCADA DE PUNTA A PUNTA · x² = 36")
        obre(pg, CAIXA + "?task=6")
        pg.click("#eq-pastilles .pastilla >> text=x² = 36"); pg.wait_for_timeout(80)
        comprova("0 de 2" in text(pg, "#eq-recorregut"), f"equacions: el comptador no comença a 0 de 2 ({text(pg, '#eq-recorregut')})")
        for _ in range(16):
            if pg.is_visible("#eq-final"):
                break
            if pg.is_disabled("#eq-mes"):
                break
            pg.click("#eq-mes"); pg.wait_for_timeout(40)
        comprova(pg.is_visible("#eq-final"), "equacions: la tasca no s'acaba després de trobar −6 i 6")
        final = text(pg, "#eq-final")
        comprova("x = -6 i x = 6" in final or "x = −6 i x = 6" in final, f"equacions: el resum no diu les dues solucions ({final[:120]})")
        codi = re.search(r"[0-9A-Z]{3}-[0-9A-Z]{3}-[0-9A-Z]{3}", final)
        if comprova(codi, "equacions: el resum no porta codi de verificació"):
            pg.goto(VERIFICA); pg.wait_for_timeout(150)
            pg.fill("#codis", codi.group(0)); pg.wait_for_timeout(150)
            llegit = text(pg, "#resultats")
            comprova("x² = 36" in llegit, f"verifica.html no posa nom al codi {codi.group(0)}: {llegit[:160]}")
        print(f"  codi: {codi.group(0) if codi else '—'}")

        comprova(not consola, f"errors a la consola: {consola[:5]}")
        nav.close()

    print()
    if errors:
        print(f"{len(errors)} PROBLEMES")
        sys.exit(1)
    print("Tot correcte.")


if __name__ == "__main__":
    main()
