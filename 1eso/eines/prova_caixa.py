#!/usr/bin/env python3
"""
eines/prova_caixa.py · la caixa d'eines, provada de debò en un navegador
=========================================================================

Obre caixa-eines.html en Chromium i fa el que faria l'alumnat: toca, s'equivoca,
llegeix la pista, s'hi torna i acaba les cinc tasques tancades. Després llegeix
els cinc codis a verifica.html. Si alguna cosa no respon com diu la
documentació, ho diu i acaba amb error.

    python3 1eso/eines/prova_caixa.py

Necessita Playwright amb Chromium:
    pip install playwright && python3 -m playwright install chromium

QUÈ COMPROVA
  · Cap error de JavaScript i cap frase sense definir («[1.2.titol]»).
  · Cap nombre de més de 999, cap «×» i cap «x» de multiplicar a la pantalla.
  · La gramàtica que es fa sola: «1 fila d'1 quadret», «5 files d'11 quadrets»,
    «la taula de l'1», «l'arrel quadrada d'11».
  · Com es llegeixen els nombres: vint-i-u, cent u, dos-cents quaranta-tres…
  · Les dades dels mòduls: sumes sense portar-ne, multiplicacions de la
    targeta, i cap cas que no es pugui fer amb el material.
  · Les cinc tasques tancades de punta a punta: encert, encert amb pista i
    resposta ensenyada, el resum i el codi, i que verifica.html el llegeix.
  · La represa d'una tasca a mitges, els enllaços ?task=n i ?task=n.m, i que
    totes les claus del navegador comencen per «pi1-».

No substitueix auditoria.py (contrast i mides, en clar i en fosc): el
complementa. Les dues s'han de passar abans de lliurar.
"""
import os
import pathlib
import re
import sys

# Només si hi és: al Codespace, Playwright desa el Chromium a la seva carpeta
# de sempre, i forçar-ne una altra el faria petar.
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


# ------------------------------------------------------------------ eines --
def obre(pg, url=CAIXA):
    pg.goto(url)
    pg.wait_for_timeout(250)


def modul(pg, mod, sub=1):
    """Obre la pestanya i hi va a la subtasca `sub` amb les fletxes."""
    pg.click(f'.segment[data-mod="{mod}"]')
    pg.wait_for_timeout(80)
    for _ in range(12):
        ara = pg.inner_text(f"#mod-{mod} .sub-rotul")
        n = int(re.match(r"\s*\d+\.(\d+)", ara).group(1))
        if n == sub:
            return
        pg.click(f"#mod-{mod} .sub-" + ("avant" if n < sub else "enrere"))
        pg.wait_for_timeout(80)


def text(pg, sel):
    return pg.inner_text(sel).replace("\u00a0", " ")


def toca_cella(pg, sel, f, c):
    """Toca el quadret de la fila f i la columna c de la taula de quadrets
    (viewBox 340, marge 36, quadret de 30: js/quadricula.js)."""
    caixa = pg.locator(sel).bounding_box()
    x = caixa["x"] + (36 + (c - 0.5) * 30) / 340 * caixa["width"]
    y = caixa["y"] + (36 + (f - 0.5) * 30) / 340 * caixa["height"]
    pg.mouse.click(x, y)
    pg.wait_for_timeout(60)


def final_de(pg, prefix):
    """El resum del final: {'passos': 5, 'primer': 3, …} i el codi."""
    fin = text(pg, f"#{prefix}-final")
    nums = dict(re.findall(r"(Passos|Correctes al primer intent|Correctes amb una pista|Amb la resposta ensenyada)\s*(\d+)", fin))
    codi = re.search(r"[0-9A-Z]{3}-[0-9A-Z]{3}-[0-9A-Z]{3}", fin)
    return nums, codi.group(0) if codi else None


def revisa_pantalla(pg, on):
    """Les regles del curs que es poden mirar al text que es veu."""
    visible = pg.evaluate("() => document.querySelector('.modul:not([hidden])').innerText")
    comprova(not re.search(r"\[[\w.]+\]", visible), f"{on}: frase sense definir: {re.findall(r'\[[\w.]+\]', visible)}")
    comprova("×" not in visible, f"{on}: surt «×»")
    comprova(not re.search(r"\d\s*[xX]\s*\d", visible), f"{on}: una «x» multiplica")
    grans = [int(n) for n in re.findall(r"\d+", visible) if int(n) > 999]
    comprova(not grans, f"{on}: nombres de més de 999: {grans}")


def llegeix_codi(pg, codi):
    obre(pg, VERIFICA)
    pg.fill("#codis", codi)
    pg.wait_for_timeout(100)
    return text(pg, "#resultats")


# ================================================================ proves ==
def main():
    with sync_playwright() as p:
        nav = p.chromium.launch()
        ctx = nav.new_context(viewport={"width": 1100, "height": 900})
        pg = ctx.new_page()
        consola = []
        pg.on("pageerror", lambda e: consola.append("error de pàgina: " + str(e)))
        pg.on("console", lambda m: consola.append(m.text) if m.type == "error" else None)
        codis = {}

        # ------------------------------------------------------------------
        titol("TOTES LES SUBTASQUES S'OBREN")
        obre(pg)
        for mod, n in [("taules", 3), ("rect", 4), ("quadrat", 3), ("cdu", 2), ("ordre", 2)]:
            for sub in range(1, n + 1):
                modul(pg, mod, sub)
                pg.wait_for_timeout(120)
                revisa_pantalla(pg, f"{mod} {sub}")
        print(f"  14 subtasques, cap frase sense definir ni cap nombre de més de 999: {not errors}")

        # ------------------------------------------------------------------
        titol("DADES DELS MÒDULS")
        d = pg.evaluate("""() => ({
            parteix: CE.dades.rect.PARTEIX, per_fer: CE.dades.rect.PER_FER,
            gira: CE.dades.rect.GIRA, dificils: CE.dades.taules.DIFICILS, falta: CE.dades.taules.FALTA,
            ns: CE.dades.quadrat.NS, zero: CE.dades.cdu.AMB_ZERO, sense: CE.dades.cdu.SENSE_ZERO,
            expr: CE.dades.ordre.EXPR.map(e => Object.assign({ passos: CE.dades.ordre.passos(e),
                                                              escrit: CE.dades.ordre.escriu(e) }, e)) })""")

        def sense_portar(x, y):
            while x or y:
                if x % 10 + y % 10 > 9:
                    return False
                x, y = x // 10, y // 10
            return True

        for c in d["parteix"]:
            a, n = c["a"], c["n"]
            comprova(10 < n < 20 and a <= 10, f"1.4: {a} · {n} no es parteix en 10 + una xifra")
            comprova(sense_portar(a * 10, a * (n - 10)), f"1.4: {a * 10} + {a * (n - 10)} s'ha de portar")
        for a, b in d["per_fer"] + [[g["a"], g["b"]] for g in d["gira"]]:
            comprova(1 < a <= 10 and 1 < b <= 10, f"rectangles: {a} · {b} no és de la targeta")
        comprova(all(6 <= a <= 9 and 6 <= b <= 9 for a, b in d["dificils"]), "0.2: hi ha multiplicacions fàcils")
        comprova(all(2 <= c["a"] <= 9 and 2 <= c["b"] <= 9 and c["a"] != c["b"] for c in d["falta"]),
                 "0.3: hi ha multiplicacions que no són de la targeta, o amb els dos números iguals")
        comprova(sum(c["falta"] == "b" for c in d["falta"]) >= 3 and sum(c["falta"] == "a" for c in d["falta"]) >= 2,
                 "0.3: calen com a mínim tres casos amb el forat al segon número i dos al primer")
        comprova(2 not in d["ns"], "2.2: el 2 no hi pot ser (2² i 2 · 2 són el mateix dibuix)")
        comprova(all("0" in str(n) for n in d["zero"]), "3.2: AMB_ZERO té nombres sense zero")
        comprova(all(n <= 999 for n in d["zero"] + d["sense"]), "3.2: nombres de més de 999")
        for e in d["expr"]:
            p_ = e["passos"]
            if e["t"] in ("sm", "ms"):
                comprova(e["b"] <= 10 and e["c"] <= 10 and sense_portar(e["a"], e["b"] * e["c"]),
                         f"4: {e['escrit']} demana portar-ne o surt de la targeta")
            else:
                comprova(sense_portar(e["a"], e["b"]) and e["a"] + e["b"] <= 10 and e["c"] <= 10,
                         f"4: {e['escrit']} demana portar-ne o surt de la targeta")
            comprova(p_["r2"] <= 100, f"4: {e['escrit']} = {p_['r2']} és massa gran")
        print("  1.4 i 4 sense portar-ne; multiplicacions de la targeta; 3.2 amb zeros: "
              f"{not [x for x in errors if x[:3] in ('1.4', '4: ', '0.2', '2.2', '3.2', 'rec')]}")

        # ------------------------------------------------------------------
        titol("COM ES LLEGEIXEN ELS NOMBRES")
        noms = {0: "zero", 1: "u", 11: "onze", 16: "setze", 17: "disset", 18: "divuit", 19: "dinou",
                20: "vint", 21: "vint-i-u", 29: "vint-i-nou", 30: "trenta", 31: "trenta-u",
                45: "quaranta-cinc", 80: "vuitanta", 99: "noranta-nou", 100: "cent", 101: "cent u",
                110: "cent deu", 121: "cent vint-i-u", 200: "dos-cents", 243: "dos-cents quaranta-tres",
                305: "tres-cents cinc", 510: "cinc-cents deu", 999: "nou-cents noranta-nou"}
        for n, esperat in noms.items():
            fet = pg.evaluate(f"CE.dades.cdu.nomDe({n})")
            comprova(fet == esperat, f"nom del {n}: «{fet}» i hauria de ser «{esperat}»")
        tots = pg.evaluate("Array.from({length: 1000}, (_, i) => CE.dades.cdu.nomDe(i))")
        comprova(len(set(tots)) == 1000, "dos nombres es llegeixen igual")
        comprova(all(re.fullmatch(r"[a-z]+(-[a-z]+)*( [a-z]+(-i?-?[a-z]+)*)?", t) for t in tots),
                 "algun nom té espais o guions de més")
        print(f"  {len(noms)} nombres de mostra i els 1.000 de l'1 al 999, tots diferents")

        # ------------------------------------------------------------------
        titol("0.1 · LA TAULA")
        obre(pg)
        modul(pg, "taules", 1)
        comprova("7 · 8 = 56" in text(pg, "#tt-lectura"), "0.1 no s'obre amb 7 · 8 = 56")
        comprova("Busca la taula del 7." in text(pg, "#tt-clau"), "0.1: la clau no és la de la targeta")
        comprova(pg.is_hidden("#tt-sencera") and pg.get_attribute("#tt-veure", "aria-expanded") == "false"
                 and text(pg, "#tt-veure") == "Veure tota la taula", "0.1: la taula ha de començar plegada")
        pg.click("#tt-pastilles .pastilla >> nth=0")
        pg.click("#tt-per .pastilla >> nth=0")
        comprova("1 fila d'1 quadret." in text(pg, "#tt-lectura"), "0.1: «1 fila d'1 quadret.»")
        comprova("En total, 1 quadret." in text(pg, "#tt-lectura"), "0.1: «En total, 1 quadret.»")
        pg.click("#tt-veure")
        comprova(pg.is_visible("#tt-sencera") and pg.get_attribute("#tt-veure", "aria-expanded") == "true"
                 and text(pg, "#tt-veure") == "Amaga la taula", "0.1: el botó no obre la taula")
        comprova(text(pg, "#tt-nom") == "La taula de l'1", "0.1: «La taula de l'1»")
        pg.click("#tt-pastilles .pastilla >> nth=9")
        pg.click("#tt-llista .fila-taula >> nth=9")
        comprova("10 · 10 = 100" in text(pg, "#tt-lectura"), "0.1: 10 · 10 = 100")
        comprova(pg.get_attribute("#tt-per .pastilla >> nth=9", "aria-pressed") == "true",
                 "0.1: tocar una fila de la taula no marca el segon número")
        comprova(pg.is_hidden("#tt-marca"), "0.1: la marca «Exemple» es queda amb un altre cas")
        pg.click("#tt-veure")
        comprova(pg.is_hidden("#tt-sencera"), "0.1: el botó no plega la taula")
        print("  s'obre amb 7 · 8 i la taula plegada; «de l'1», «d'1 quadret»; la fila i la pastilla, lligades")

        # ------------------------------------------------------------------
        titol("0.2 · TROBA EL RESULTAT A LA TAULA")
        modul(pg, "taules", 2)

        def pregunta_02():
            a, b = map(int, re.findall(r"\d+", text(pg, "#tb-pregunta")))
            return a, b

        def taula(n):
            pg.click(f"#tb-pastilles .pastilla >> nth={n - 1}")
            pg.wait_for_timeout(40)

        def fila(n):
            pg.click(f"#tb-llista .fila-taula >> nth={n - 1}")
            pg.wait_for_timeout(40)

        # pas 1: taula dolenta, i després bé → correcte amb pista
        a, b = pregunta_02()
        comprova(text(pg, "#tb-avis") == "Tria una taula.", "0.2: l'avís del principi")
        comprova(pg.locator("#tb-seguent").is_disabled(), "0.2: «Següent pas» actiu abans de contestar")
        taula(2)
        comprova(text(pg, "#tb-avis") == "Ara toca una fila.", "0.2: l'avís després de triar la taula")
        fila(3)
        av = text(pg, "#tb-avis")
        comprova(av.startswith("Incorrecte.") and "Tria la taula del" in av, f"0.2: pista de la taula: «{av}»")
        taula(a); fila(b)
        comprova(text(pg, "#tb-avis").startswith("Correcte."), "0.2: correcte després de la pista")
        pg.click("#tb-seguent")
        # pas 2: bé a la primera
        a, b = pregunta_02(); taula(a); fila(b)
        comprova(text(pg, "#tb-avis") == f"Correcte. {a} · {b} = {a * b}.", "0.2: resposta correcta")
        pg.click("#tb-seguent")
        # pas 3: dos errors → la caixa ensenya la fila
        a, b = pregunta_02(); taula(a); fila(b % 10 + 1)
        comprova("Ara baixa per la taula" in text(pg, "#tb-avis"), "0.2: pista de la fila")
        fila((b + 1) % 10 + 1)
        av = text(pg, "#tb-avis")
        comprova(av.startswith("Incorrecte. Mira la fila marcada"), f"0.2: segon error: «{av}»")
        comprova(pg.locator("#tb-llista .fila-taula.bona").count() == 1, "0.2: no es marca la fila bona")
        pg.click("#tb-seguent")
        # pas 4: la fila girada
        a, b = pregunta_02(); taula(b); fila(a)
        av = text(pg, "#tb-avis")
        # Amb 7 · 7 la fila girada és la mateixa fila: la caixa no ha de dir que és girada.
        comprova(av.startswith("Correcte.") and (("És el mateix que" in av) == (a != b)),
                 f"0.2: la fila girada no compta: «{av}»")
        pg.click("#tb-seguent")
        # pas 5
        a, b = pregunta_02(); taula(a); fila(b)
        pg.click("#tb-seguent")
        nums, codi = final_de(pg, "tb")
        comprova(nums == {"Passos": "5", "Correctes al primer intent": "3", "Correctes amb una pista": "1",
                          "Amb la resposta ensenyada": "1"}, f"0.2: el resum no quadra: {nums}")
        comprova(bool(codi), "0.2: no surt el codi")
        codis["0.2"] = (codi, "Troba el resultat a la taula", (5, 3, 1, 1))
        print(f"  pista de la taula, pista de la fila, fila girada, fila ensenyada; codi {codi}")

        # ------------------------------------------------------------------
        titol("0.3 · EL NÚMERO QUE FALTA")
        obre(pg)
        modul(pg, "taules", 3)

        def pregunta_03():
            """(el número que es té, el que falta, el resultat, si falta el primer)"""
            t = text(pg, "#tf-expr")
            k, p_ = [int(x) for x in re.findall(r"\d+", t)]
            return k, p_ // k, p_, t.strip().startswith("…")

        def taula3(n):
            pg.click(f"#tf-pastilles .pastilla >> nth={n - 1}")
            pg.wait_for_timeout(40)

        def fila3(n):
            pg.click(f"#tf-llista .fila-taula >> nth={n - 1}")
            pg.wait_for_timeout(40)

        vist_primer = vist_segon = False
        # pas 1: la taula dolenta, i després bé → correcte amb pista
        k, x, p_, fp = pregunta_03()
        vist_primer |= fp; vist_segon |= not fp
        comprova(text(pg, "#tf-avis") == "Tria una taula.", "0.3: l'avís del principi")
        comprova("…" in text(pg, "#tf-expr"), "0.3: el forat no es veu")
        taula3(next(n for n in range(2, 11) if n not in (k, x)))
        comprova(text(pg, "#tf-avis") == f"Ara busca la fila on surt el {p_}.", "0.3: l'avís després de triar la taula")
        fila3(1)
        av = text(pg, "#tf-avis")
        comprova(av.startswith("Incorrecte.") and f"Tria la taula del {k}" in av, f"0.3: pista de la taula: «{av}»")
        taula3(k); fila3(x)
        av = text(pg, "#tf-avis")
        comprova(av.startswith("Correcte.") and f"El número que falta és el {x}." in av, f"0.3: correcte amb pista: «{av}»")
        comprova("…" not in text(pg, "#tf-expr") and str(x) in text(pg, "#tf-expr"), "0.3: el forat no s'omple")
        comprova(("És el mateix que" in av) == fp, "0.3: el girat només s'ha de dir quan falta el primer número")
        pg.click("#tf-seguent")
        # pas 2: bé a la primera
        k, x, p_, fp = pregunta_03(); vist_primer |= fp; vist_segon |= not fp
        taula3(k); fila3(x)
        comprova(text(pg, "#tf-avis").startswith("Correcte."), "0.3: resposta correcta")
        pg.click("#tf-seguent")
        # pas 3: dos errors → la caixa ensenya la fila
        k, x, p_, fp = pregunta_03(); vist_primer |= fp; vist_segon |= not fp
        taula3(k); fila3(x % 10 + 1)
        comprova(f"Baixa per la taula fins que trobis el {p_}." in text(pg, "#tf-avis"), "0.3: pista de la fila")
        fila3((x + 1) % 10 + 1)
        av = text(pg, "#tf-avis")
        comprova(av.startswith("Incorrecte. Mira la fila marcada") and f"el {x}." in av, f"0.3: segon error: «{av}»")
        comprova(pg.locator("#tf-llista .fila-taula.bona").count() == 1, "0.3: no es marca la fila bona")
        pg.click("#tf-seguent")
        # passos 4 i 5: bé
        for _ in range(2):
            k, x, p_, fp = pregunta_03(); vist_primer |= fp; vist_segon |= not fp
            taula3(k); fila3(x)
            pg.click("#tf-seguent")
        comprova(vist_primer and vist_segon, "0.3: han de sortir forats al primer i al segon número")
        nums, codi = final_de(pg, "tf")
        comprova(nums == {"Passos": "5", "Correctes al primer intent": "3", "Correctes amb una pista": "1",
                          "Amb la resposta ensenyada": "1"}, f"0.3: el resum no quadra: {nums}")
        comprova(bool(codi), "0.3: no surt el codi")
        codis["0.3"] = (codi, "El número que falta", (5, 3, 1, 1))
        print(f"  forat al primer i al segon número, pista de la taula i de la fila, ensenyat; codi {codi}")

        # ------------------------------------------------------------------
        titol("1.1 · FES UN RECTANGLE")
        obre(pg)
        modul(pg, "rect", 1)
        comprova("3 · 4 = 12" in text(pg, "#r1-lectura"), "1.1 no s'obre amb 3 · 4")
        toca_cella(pg, "#r1-svg", 5, 6)
        lect = text(pg, "#r1-lectura")
        comprova("5 files de 6 quadrets." in lect and "En total, 30 quadrets." in lect and "5 · 6 = 30" in lect,
                 f"1.1: tocar el quadret 5, 6: «{lect}»")
        pg.click("#r1-files [data-f=menys]")
        comprova("4 · 6 = 24" in text(pg, "#r1-lectura"), "1.1: el comptador de files")
        for _ in range(4):
            pg.click("#r1-files [data-f=menys]")
        comprova("0 · 6 = 0" in text(pg, "#r1-lectura"), "1.1: 0 files → 0 · 6 = 0")
        comprova(pg.locator("#r1-files [data-f=menys]").is_disabled(), "1.1: el − no s'apaga al 0")
        pg.click("#r1-buida")
        comprova(text(pg, "#r1-lectura") == "Toca un quadret de la quadrícula.", "1.1: buida-ho")
        pg.focus("#r1-svg"); pg.keyboard.press("ArrowRight"); pg.keyboard.press("ArrowDown")
        comprova("2 files de 2 quadrets." in text(pg, "#r1-lectura"), "1.1: les fletxes")
        print("  tocar, comptadors, zero, buida-ho i fletxes")

        # ------------------------------------------------------------------
        titol("1.2 · EL RECTANGLE D'UNA MULTIPLICACIÓ")
        modul(pg, "rect", 2)

        def pregunta_12():
            a, b = map(int, re.findall(r"\d+", text(pg, "#r2-pregunta")))
            return a, b

        a, b = pregunta_12(); toca_cella(pg, "#r2-svg", a, b)                      # bé
        comprova(text(pg, "#r2-avis").startswith("Correcte."), "1.2: rectangle bo")
        pg.click("#r2-seguent")
        a, b = pregunta_12(); toca_cella(pg, "#r2-svg", b, a)                      # girat
        comprova("rectangle girat" in text(pg, "#r2-avis") or a == b, "1.2: el girat no compta")
        pg.click("#r2-seguent")
        a, b = pregunta_12(); toca_cella(pg, "#r2-svg", 9, 9)                      # error → pista
        av = text(pg, "#r2-avis")
        comprova(av.startswith("Incorrecte. Has fet 9 files de 9 quadrets.") and "Compta" in av,
                 f"1.2: el primer error: «{av}»")
        comprova(pg.locator("#r2-svg .q-pista").count() == 2, "1.2: la pista no marca els dos números")
        toca_cella(pg, "#r2-svg", a, b)
        comprova(text(pg, "#r2-avis").startswith("Correcte."), "1.2: correcte amb pista")
        pg.click("#r2-seguent")
        a, b = pregunta_12(); toca_cella(pg, "#r2-svg", 10, 10); toca_cella(pg, "#r2-svg", 10, 9)
        av = text(pg, "#r2-avis")
        comprova(av.startswith("Incorrecte. Mira el rectangle"), f"1.2: el segon error: «{av}»")
        comprova(pg.locator("#r2-svg .q").count() == a * b, "1.2: no es dibuixa el rectangle bo")
        pg.click("#r2-seguent")
        a, b = pregunta_12()                                                          # amb el teclat
        pg.focus("#r2-svg"); pg.keyboard.press("Enter")
        for _ in range(a - 1):
            pg.keyboard.press("ArrowDown")
        for _ in range(b - 1):
            pg.keyboard.press("ArrowRight")
        pg.keyboard.press("Enter")
        comprova(text(pg, "#r2-avis").startswith("Correcte."), "1.2: amb el teclat")
        pg.click("#r2-seguent")
        nums, codi = final_de(pg, "r2")
        comprova(nums == {"Passos": "5", "Correctes al primer intent": "3", "Correctes amb una pista": "1",
                          "Amb la resposta ensenyada": "1"}, f"1.2: el resum no quadra: {nums}")
        codis["1.2"] = (codi, "El rectangle d'una multiplicació", (5, 3, 1, 1))
        print(f"  bo, girat, pista amb els números de la vora, ensenyat i amb el teclat; codi {codi}")

        # ------------------------------------------------------------------
        titol("1.3 · GIRA EL RECTANGLE")
        modul(pg, "rect", 3)
        comprova("3 · 4 = 4 · 3" not in text(pg, "#r3-lectura"), "1.3: la igualtat surt abans de girar")
        pg.click("#r3-gira"); pg.wait_for_timeout(900)
        lect = text(pg, "#r3-lectura")
        comprova("4 files de 3 quadrets." in lect and "Hi ha els mateixos quadrets." in lect
                 and "3 · 4 = 4 · 3" in lect, f"1.3: després de girar: «{lect}»")
        comprova(text(pg, "#r3-gira") == "Torna a girar-lo", "1.3: el botó no canvia")
        pg.click("#r3-pastilles .pastilla >> nth=1")
        comprova("2 files de 5 quadrets." in text(pg, "#r3-lectura"), "1.3: canviar de cas no torna a començar")
        print("  la igualtat només surt després de girar-lo")

        # ------------------------------------------------------------------
        titol("1.4 · PARTEIX EL RECTANGLE")
        modul(pg, "rect", 4)
        comprova("3 files de 12 quadrets." in text(pg, "#r4-lectura"), "1.4 no s'obre amb 3 · 12")
        pg.click("#r4-parteix"); pg.wait_for_timeout(700)
        lect = text(pg, "#r4-lectura")
        comprova("30 + 6 = 36" in lect and "3 · 12 = 36" in lect, f"1.4: partit: «{lect}»")
        pg.click("#r4-pastilles .pastilla >> nth=3")
        comprova("5 files d'11 quadrets." in text(pg, "#r4-lectura"), "1.4: «5 files d'11 quadrets»")
        print("  30 + 6 = 36; «d'11 quadrets»")

        # ------------------------------------------------------------------
        titol("2.1 · EL QUADRAT D'UN NOMBRE")
        modul(pg, "quadrat", 1)
        lect = text(pg, "#q1-lectura")
        comprova("3 · 3 = 9" in lect and "3² = 9" in lect and lect.index("3 · 3") < lect.index("3²"),
                 "2.1: primer 3 · 3 = 9 i després 3² = 9")
        pg.click("#q1-pastilles .pastilla >> nth=0")
        comprova("1 fila d'1 quadret." in text(pg, "#q1-lectura") and "1² = 1" in text(pg, "#q1-lectura"),
                 "2.1: el quadrat de l'1")
        print("  el símbol surt després del dibuix i de les paraules")

        # ------------------------------------------------------------------
        titol("2.2 · QUIN DIBUIX ÉS?")
        modul(pg, "quadrat", 2)
        tipus_vistos = set()
        for pas in range(5):
            q = text(pg, "#q2-pregunta")
            bo = "q" if "²" in q else "d"
            tipus_vistos.add(bo)
            comprova(pg.locator("#q2-opcions .peu-dibuix:visible").count() == 0,
                     "2.2: el rètol del dibuix es veu abans de tocar")
            if pas == 1:
                pg.click(f'#q2-opcions .opcio-dibuix[data-o="{"d" if bo == "q" else "q"}"]')
                av = text(pg, "#q2-avis")
                comprova(av.startswith("Incorrecte. Aquest dibuix és"), f"2.2: el primer error: «{av}»")
                comprova(pg.locator("#q2-opcions .opcio-dibuix.mal").is_disabled(),
                         "2.2: el dibuix dolent no s'apaga")
            pg.click(f'#q2-opcions .opcio-dibuix[data-o="{bo}"]')
            comprova(text(pg, "#q2-avis").startswith("Correcte."), f"2.2: pas {pas + 1}")
            comprova(pg.locator("#q2-opcions .peu-dibuix:visible").count() == 2,
                     "2.2: al final no es veuen les dues formes")
            pg.click("#q2-seguent")
        comprova(tipus_vistos == {"q", "d"}, "2.2: no hi ha preguntes dels dos tipus")
        nums, codi = final_de(pg, "q2")
        comprova(nums == {"Passos": "5", "Correctes al primer intent": "4", "Correctes amb una pista": "1",
                          "Amb la resposta ensenyada": "0"}, f"2.2: el resum no quadra: {nums}")
        codis["2.2"] = (codi, "Quin dibuix és?", (5, 4, 1, 0))
        print(f"  n² i n · 2 barrejats; el rètol surt en tocar; codi {codi}")

        # ------------------------------------------------------------------
        titol("2.3 · EL COSTAT DEL QUADRAT")
        modul(pg, "quadrat", 3)
        comprova("√16 = 4" in text(pg, "#q3-lectura"), "2.3 no s'obre amb 16")
        for _ in range(3):
            pg.click("#q3-quants [data-f=menys]")
        lect = text(pg, "#q3-lectura")
        comprova("Amb 13 quadrets no pots fer cap quadrat." in lect and "3 < √13 < 4" in lect
                 and "13 és entre 9 i 16." in lect, f"2.3: 13: «{lect}»")
        comprova(pg.locator("#q3-svg .q.b").count() == 4 and pg.locator("#q3-svg .q.falta").count() == 3,
                 "2.3: 13 → 4 quadrets de més i 3 llocs buits")
        for _ in range(2):
            pg.click("#q3-quants [data-f=menys]")
        comprova("L'arrel quadrada d'11 és entre 3 i 4." in text(pg, "#q3-lectura"), "2.3: «d'11»")
        print("  16 exacte; 13 entre 3 i 4, amb els que sobren i els que falten; «d'11»")

        # ------------------------------------------------------------------
        titol("3.1 · CENTENES, DESENES I UNITATS")
        modul(pg, "cdu", 1)
        comprova("dos-cents quaranta-tres" in text(pg, "#n1-nombre"), "3.1 no s'obre amb 243")
        for _ in range(2):
            pg.click("#n1-c [data-f=menys]")
        for _ in range(2):
            pg.click("#n1-d [data-f=menys]")
        for _ in range(2):
            pg.click("#n1-u [data-f=menys]")
        comprova("vint-i-u" in text(pg, "#n1-nombre")
                 and "0 centenes, 2 desenes i 1 unitat." in (pg.get_attribute("#n1-blocs", "aria-label") or ""),
                 "3.1: 21 → vint-i-u, «1 unitat»")
        comprova(pg.locator("#n1-blocs .zona-et:visible, #n1-blocs .zona-peu:visible").count() == 0,
                 "3.1: el dibuix torna a portar rètols o peus, que repeteixen els comptadors")
        for _ in range(12):                      # fins que el + s'apagui: ha de ser al 9
            if pg.locator("#n1-u [data-f=mes]").is_disabled():
                break
            pg.click("#n1-u [data-f=mes]")
        comprova(text(pg, "#n1-u output") == "9" and pg.locator("#n1-u [data-f=mes]").is_disabled(),
                 "3.1: el + de les unitats no s'apaga al 9")
        print("  243; 21 en singular; sense rètols repetits; no es pot passar de 9")

        # ------------------------------------------------------------------
        titol("3.2 · FES EL NOMBRE")
        modul(pg, "cdu", 2)

        def posa(c, dd, u):
            for k, v in (("c", c), ("d", dd), ("u", u)):
                ara = int(text(pg, f"#n2-{k} output"))
                boto = "mes" if v > ara else "menys"
                for _ in range(abs(v - ara)):
                    pg.click(f"#n2-{k} [data-f={boto}]")

        for pas in range(5):
            n = int(re.search(r"\d+", text(pg, "#n2-pregunta")).group(0))
            c, dd, u = n // 100, n // 10 % 10, n % 10
            if pas == 0:                                  # l'error del zero: 305 fet com a 35
                posa(0, c, u if dd == 0 else dd)
                pg.click("#n2-comprova")
                av = text(pg, "#n2-avis")
                comprova(av.startswith("Incorrecte. Has fet"), f"3.2: el primer error: «{av}»")
                comprova(pg.is_visible("#n2-taula"), "3.2: la pista no ensenya la taula")
            posa(c, dd, u)
            pg.click("#n2-comprova")
            comprova(text(pg, "#n2-avis").startswith("Correcte."), f"3.2: pas {pas + 1} amb {n}")
            pg.click("#n2-seguent")
        nums, codi = final_de(pg, "n2")
        comprova(nums == {"Passos": "5", "Correctes al primer intent": "4", "Correctes amb una pista": "1",
                          "Amb la resposta ensenyada": "0"}, f"3.2: el resum no quadra: {nums}")
        codis["3.2"] = (codi, "Fes el nombre", (5, 4, 1, 0))
        print(f"  el nombre no es veu mentre es fa; la pista és la taula; codi {codi}")

        # ------------------------------------------------------------------
        titol("4.1 · MIRA L'ORDRE")
        modul(pg, "ordre", 1)
        for i, esperat in enumerate(["2 + 3 · 4 = 14", "(2 + 3) · 4 = 20", "5 · 2 + 3 = 13", "4 · (1 + 2) = 12"]):
            pg.click(f"#o1-pastilles .pastilla >> nth={i}")
            comprova(esperat in text(pg, "#o1-lectura"), f"4.1: {esperat}")
        print("  les quatre expressions, amb el total que surt del dibuix")

        # ------------------------------------------------------------------
        titol("4.2 · QUÈ ES FA PRIMER?")
        modul(pg, "ordre", 2)
        amb_par = 0
        for pas in range(5):
            expr = text(pg, "#o2-expr")
            par = "(" in expr
            amb_par += par
            bo, dolent = ("suma", "mult") if par else ("mult", "suma")
            if pas == 2:
                pg.click(f'#o2-expr .signe[data-op="{dolent}"]')
                av = text(pg, "#o2-avis")
                comprova(av.startswith("Incorrecte.") and ("parèntesi" in av if par else "Busca el punt" in av),
                         f"4.2: la pista: «{av}»")
            pg.click(f'#o2-expr .signe[data-op="{bo}"]')
            comprova(text(pg, "#o2-avis").startswith("Correcte. Primer,"), f"4.2: pas {pas + 1}")
            comprova(pg.is_visible("#o2-svg"), "4.2: el dibuix no surt en contestar")
            pg.click("#o2-seguent")
        comprova(amb_par == 2, f"4.2: hi ha d'haver dos passos amb parèntesi, i n'hi ha {amb_par}")
        nums, codi = final_de(pg, "o2")
        comprova(nums == {"Passos": "5", "Correctes al primer intent": "4", "Correctes amb una pista": "1",
                          "Amb la resposta ensenyada": "0"}, f"4.2: el resum no quadra: {nums}")
        codis["4.2"] = (codi, "Què es fa primer?", (5, 4, 1, 0))
        print(f"  dos passos amb parèntesi; la pista depèn del tipus; codi {codi}")

        # ------------------------------------------------------------------
        titol("CODIS A verifica.html")
        for id_, (codi, nom, (pas, be, pista, most)) in codis.items():
            res = llegeix_codi(pg, codi or "")
            comprova("Vàlid" in res and "No vàlid" not in res, f"{id_}: el codi {codi} no és vàlid")
            comprova(f"{id_} · {nom}" in res, f"{id_}: verifica.html no diu el nom de la tasca")
            comprova(f"Passos: {pas}" in res and f"Correctes al primer intent: {be}" in res
                     and f"Correctes amb una pista: {pista}" in res and f"Amb la resposta ensenyada: {most}" in res,
                     f"{id_}: verifica.html no llegeix els recomptes: {res!r}")
        res = llegeix_codi(pg, "AAA-AAA-AAA")
        comprova("No vàlid" in res, "verifica.html accepta un codi inventat")
        print(f"  {len(codis)} codis llegits, amb el nom i els recomptes; un codi inventat no passa")

        # ------------------------------------------------------------------
        titol("REPRESA, ENLLAÇOS I MEMÒRIA")
        pg.evaluate("localStorage.clear()")
        obre(pg)
        modul(pg, "rect", 2)
        a, b = map(int, re.findall(r"\d+", text(pg, "#r2-pregunta")))
        toca_cella(pg, "#r2-svg", a, b)
        pg.click("#r2-seguent")
        obre(pg)
        modul(pg, "rect", 2)
        comprova(pg.is_visible("#r2-represa") and "pas 2 de 5" in text(pg, "#r2-represa"),
                 "1.2: no es proposa continuar la tasca a mitges")
        pg.click("#r2-represa .btn >> nth=0")
        comprova("Pas 2 de 5" in text(pg, "#r2-recorregut"), "1.2: continuar no porta al pas 2")
        claus = pg.evaluate("Object.keys(localStorage)")
        comprova(claus and all(k.startswith("pi1-") for k in claus), f"claus del navegador sense «pi1-»: {claus}")

        obre(pg, CAIXA + "?task=1.3")
        visibles = pg.evaluate("[...document.querySelectorAll('.segment')].filter(b => !b.hidden).map(b => b.dataset.mod)")
        comprova(visibles == ["taules", "rect"], f"?task=1.3: pestanyes {visibles}")
        comprova(text(pg, "#mod-rect .sub-rotul").startswith("1.3"), "?task=1.3 no obre la 1.3")
        comprova(pg.is_hidden(".tornar"), "?task=1.3: l'enllaç a l'inici es veu")
        pg.click('.segment[data-mod="taules"]')
        comprova(text(pg, "#mod-taules .sub-rotul").startswith("0.1"), "?task=1.3: les Taules no s'obren per la 0.1")
        comprova(not pg.is_visible("#mod-taules .sub-avant"), "?task=1.3: a les Taules es veuen les fletxes")
        pg.click('.segment[data-mod="rect"]')
        comprova(not pg.is_visible("#mod-rect .sub-avant") and not pg.is_visible("#mod-rect .sub-enrere"),
                 "?task=1.3: es veuen les fletxes per passar a un altre exercici")
        obre(pg, CAIXA + "?task=3")
        comprova(text(pg, "#mod-cdu .sub-rotul").startswith("3.1"), "?task=3 no obre la 3.1")
        comprova(pg.is_visible("#mod-cdu .sub-avant"), "?task=3: amb l'enllaç a tota l'eina, les fletxes hi han de ser")
        obre(pg, CAIXA + "?task=0.2")
        comprova(text(pg, "#mod-taules .sub-rotul").startswith("0.2"), "?task=0.2 no obre la 0.2")
        print("  represa al pas 2; claus pi1-; ?task=1.3 sense fletxes, ?task=3 amb fletxes, ?task=0.2")

        # ------------------------------------------------------------------
        titol("CONSOLA")
        comprova(not consola, f"errors a la consola: {consola}")
        print(f"  errors: {len(consola)}")
        nav.close()

    print()
    if errors:
        print(f"{len(errors)} proves han fallat.")
        sys.exit(1)
    print("Tot correcte.")


if __name__ == "__main__":
    main()
