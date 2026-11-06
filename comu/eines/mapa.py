#!/usr/bin/env python3
"""The site map check: every course follows comu/docs/SITE-MAP.md.

    python3 comu/eines/mapa.py          (from the repository root: every course)

Both course checkers (CURS/eines/comprova.py, section NAVEGACIÓ) call comprova_curs() for
their own course, so the GitHub check and the ZIP workflow run it too. Standard library only.

What it checks, for one course folder (1eso/, 4eso/…):
  · the course is in the registry comu/js/cursos.js;
  · the course pages exist and load the shared shell: index.html (curs.js),
    professorat.html (professorat.js), eines.html (alumne.js before js/app.js, no link out);
  · every unit of dades/unitats.js has its folder uN/ with the unit page, identical to the
    canonical one (UNITAT below), and every page declared in the data exists;
  · every page in uN/ (except index.html) is declared in the data;
  · every paper page (uN/*.html except index.html, and targetes/*.html) has exactly one screen
    bar right after <body>, «<nav class="navega no-imprimir" …>…</nav>», with the shared
    stylesheet and paper.js INSIDE it (the PDF fingerprint strips exactly that element);
  · nothing still points at the pages removed on 6/11/2026 (unitat.html, caixa-eines.html,
    fitxes/, quadern/udN.html, comu/js/torna.js) or at an absolute path.
"""
import glob
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# The unit page: every uN/index.html of every course is exactly this file.
UNITAT = open(os.path.join(REPO, "comu", "eines", "unitat.html"), encoding="utf-8").read()

BARRA = re.compile(r'<body[^>]*>\s*(<nav class="navega no-imprimir"[^>]*>(.*?)</nav>)\n', re.S)
VELLS = re.compile(r'unitat\.html|caixa-eines|torna\.js|(?<![\w/.])fitxes/|quadern/ud\d|\?ud=|tasques=')


def llegeix(f):
    with open(f, encoding="utf-8") as h:
        return h.read()


def cursos_registrats():
    return re.findall(r'\{\s*id:\s*"([\w-]+)"', llegeix(os.path.join(REPO, "comu", "js", "cursos.js")))


def camins_de_les_dades(dades):
    """{num: [camins de la unitat]} i les targetes, llegits de dades/unitats.js sense executar-lo."""
    unitats = {}
    for bloc in re.findall(r'^  \{\n?(.*?)^  \},?$', dades, re.S | re.M):
        n = re.search(r'\bnum:\s*(\d+)', bloc)
        if n:
            unitats[int(n[1])] = (re.findall(r'\bfitxa:\s*"([^"]+)"', bloc)
                                  + re.findall(r'\bquadern:\s*"([^"]+)"', bloc))
    targetes = re.findall(r'\bnom:\s*"([\w-]+)"', dades[dades.index("window.TARGETES"):]) \
        if "window.TARGETES" in dades else []
    return unitats, targetes


def comprova_curs(curs):
    """Torna la llista de problemes del curs (buida si tot és correcte)."""
    falles = []
    arrel = os.path.join(REPO, curs)
    ruta = lambda *p: os.path.join(arrel, *p)
    if curs not in cursos_registrats():
        falles.append(f"{curs}/ no és a comu/js/cursos.js")

    # Les pàgines del curs
    for pagina, script in (("index.html", "../comu/js/curs.js"), ("professorat.html", "../comu/js/professorat.js"),
                           ("eines.html", "../comu/js/alumne.js")):
        if not os.path.exists(ruta(pagina)):
            falles.append(f"{curs}/{pagina}: no hi és")
            continue
        t = llegeix(ruta(pagina))
        if f'<script src="{script}"></script>' not in t or '../comu/css/web.css' not in t:
            falles.append(f"{curs}/{pagina}: ha de carregar ../comu/css/web.css i {script}")
    if os.path.exists(ruta("eines.html")):
        t = llegeix(ruta("eines.html"))
        if not (0 <= t.find('src="dades/unitats.js"') < t.find('src="../comu/js/alumne.js"') < t.find('src="js/app.js"')):
            falles.append(f"{curs}/eines.html: l'ordre ha de ser dades/unitats.js, ../comu/js/alumne.js i js/app.js")
        cos = re.sub(r'<!--.*?-->', '', t, flags=re.S)
        enllacos = [h for h in re.findall(r'<a [^>]*href="([^"]+)"', cos)]
        if enllacos:
            falles.append(f"{curs}/eines.html: l'espai de l'alumnat no porta cap enllaç, i n'hi ha: {enllacos[:3]}")

    # Les unitats
    dades = llegeix(ruta("dades", "unitats.js"))
    unitats, targetes = camins_de_les_dades(dades)
    declarats = set()
    for n, camins in sorted(unitats.items()):
        index = ruta(f"u{n}", "index.html")
        if not os.path.exists(index):
            falles.append(f"{curs}/u{n}/index.html: no hi és (copia comu/eines/unitat.html)")
        elif llegeix(index) != UNITAT:
            falles.append(f"{curs}/u{n}/index.html: no és igual que comu/eines/unitat.html")
        for c in camins:
            declarats.add(c)
            if not re.fullmatch(rf"u{n}/[\w-]+\.html", c):
                falles.append(f"{curs}/dades/unitats.js: {c} no és a la carpeta de la unitat {n} (u{n}/)")
            elif not os.path.exists(ruta(c)):
                falles.append(f"{curs}/dades/unitats.js apunta a {c}, que no existeix")
    for f in sorted(glob.glob(ruta("u*", "*.html"))):
        rel = os.path.relpath(f, arrel).replace(os.sep, "/")
        if not rel.endswith("/index.html") and rel not in declarats:
            falles.append(f"{curs}/{rel}: no surt a dades/unitats.js")
    for d in sorted(glob.glob(ruta("u*"))):
        if os.path.isdir(d) and not re.fullmatch(r"u\d+", os.path.basename(d)):
            falles.append(f"{curs}/{os.path.basename(d)}/: les carpetes d'unitat es diuen uN")
        elif os.path.isdir(d) and int(os.path.basename(d)[1:]) not in unitats:
            falles.append(f"{curs}/{os.path.basename(d)}/: és una carpeta d'unitat que no surt a dades/unitats.js")
    for t in targetes:
        if not os.path.exists(ruta("targetes", t + ".html")):
            falles.append(f"{curs}/dades/unitats.js apunta a la targeta {t}, que no existeix")
    for f in glob.glob(ruta("targetes", "*.html")):
        if os.path.basename(f)[:-5] not in targetes:
            falles.append(f"{curs}/targetes/{os.path.basename(f)}: no surt a dades/unitats.js")

    # La barra de pantalla de cada pàgina de paper
    paper = [f for f in glob.glob(ruta("u*", "*.html")) if os.path.basename(f) != "index.html"] \
        + glob.glob(ruta("targetes", "*.html"))
    for f in sorted(paper):
        rel = os.path.relpath(f, arrel).replace(os.sep, "/")
        t = llegeix(f)
        m = BARRA.search(t)
        if t.count('<nav class="navega') != 1 or not m:
            falles.append(f"{curs}/{rel}: ha de tenir una sola barra <nav class=\"navega no-imprimir\"> just després de <body>")
            continue
        dins = m[2]
        if '<link rel="stylesheet" href="../../comu/css/web.css">' not in dins \
                or '<script src="../../comu/js/paper.js"></script>' not in dins:
            falles.append(f"{curs}/{rel}: la barra ha de portar a dins ../../comu/css/web.css i ../../comu/js/paper.js")
        fora = t.replace(m[1], "")
        if "comu/js/" in fora or "comu/css/" in fora:
            falles.append(f"{curs}/{rel}: hi ha peces de pantalla fora de la barra (farien vell el PDF)")

    # Res no apunta a les pàgines d'abans
    fonts = (glob.glob(ruta("**", "*.html"), recursive=True) + glob.glob(ruta("js", "**", "*.js"), recursive=True)
             + [ruta("dades", "unitats.js")])
    for f in sorted(fonts):
        rel = os.path.relpath(f, arrel).replace(os.sep, "/")
        t = re.sub(r'<!--.*?-->|/\*.*?\*/', '', llegeix(f), flags=re.S)
        for m in VELLS.finditer(t):
            falles.append(f"{curs}/{rel}: encara parla d'una pàgina d'abans del 6/11/2026 («{m[0]}»)")
            break
        for d in re.findall(r'(?:href|src)="(/[^"]*)"', t):
            falles.append(f"{curs}/{rel}: ruta absoluta «{d}»: les pàgines s'obren també amb doble clic")
    return falles


def comprova_comu():
    """El que és de tots els cursos: comu/js no apunta a pàgines d'abans."""
    falles = []
    for f in sorted(glob.glob(os.path.join(REPO, "comu", "js", "*.js")) + [os.path.join(REPO, "index.html")]):
        t = re.sub(r'/\*.*?\*/|<!--.*?-->', '', llegeix(f), flags=re.S)
        m = VELLS.search(t)
        if m:
            falles.append(f"{os.path.relpath(f, REPO)}: encara parla d'una pàgina d'abans del 6/11/2026 («{m[0]}»)")
    return falles


if __name__ == "__main__":
    tots = comprova_comu()
    for c in cursos_registrats():
        tots += comprova_curs(c)
    for f in tots:
        print("  ·", f)
    print("Mapa del lloc: " + ("correcte." if not tots else f"{len(tots)} problemes."))
    sys.exit(1 if tots else 0)
