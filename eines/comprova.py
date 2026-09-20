#!/usr/bin/env python3
"""Comprovacions del projecte. Es passa abans de publicar res.

    python3 eines/comprova.py

Verifica les regles que és fàcil trencar sense adonar-se'n: que les fitxes no
tinguin cap color, que l'HTML tanqui bé, que la numeració de pàgines sigui
seguida, que cada fitxa porti el rètol de material, la pregunta d'obertura i
la pàgina de la vida de cada dia, que els mòduls declarats al marcatge de
l'app siguin els que es registren, que els fulls d'estil tanquin totes les
claus i no facin servir variables que no existeixen, que les frases de
l'alumnat segueixin les regles de Lectura Fàcil que es poden comprovar soles,
i que els colors de la pantalla tinguin el contrast que demana la WCAG 2.2 AA.
"""
import re, sys, glob, os
from html.parser import HTMLParser

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUIDES = {'area','base','br','col','embed','hr','img','input','link','meta','source',
          'track','wbr','path','circle','rect','line','text','use','stop','polygon',
          'polyline','ellipse'}
falles = []

class Estructura(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pila, self.err = [], []

    def handle_starttag(self, t, a):
        if t not in BUIDES:
            self.pila.append(t)

    def handle_endtag(self, t):
        if t in BUIDES:
            return
        if self.pila and self.pila[-1] == t:
            self.pila.pop()
        else:
            self.err.append(t)

def rgb(h):
    h = h.lstrip('#')
    h = ''.join(c * 2 for c in h) if len(h) == 3 else h
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)

def cromatics(text):
    return sorted({h for h in re.findall(r'#[0-9A-Fa-f]{3,6}\b', text)
                   if len(set(rgb(h))) > 1})

def comprova(condicio, missatge):
    if not condicio:
        falles.append(missatge)
    return condicio

def ruta(*p):
    return os.path.join(ARREL, *p)

print("FITXES")
css_fitxa = open(ruta('css', 'fitxa.css'), encoding='utf-8').read()
comprova(not cromatics(css_fitxa), "css/fitxa.css conté color")
print(f"  css/fitxa.css                cap color: {not cromatics(css_fitxa)}")

for f in sorted(glob.glob(ruta('fitxes', '*.html'))):
    nom = os.path.basename(f)
    s = open(f, encoding='utf-8').read()
    e = Estructura(); e.feed(s)
    estructura = not e.err and not e.pila
    color = cromatics(s)
    pags = [int(n) for n in re.findall(r'· pàgina (\d+)</div>', s)]
    seguida = pags == list(range(1, len(pags) + 1))
    enllac = 'css/fitxa.css' in s
    inline = '<style>' in s

    comprova(estructura, f"{nom}: HTML mal tancat")
    comprova(not color, f"{nom}: hi ha color ({color})")
    comprova(seguida, f"{nom}: numeració de pàgines {pags}")
    comprova(enllac and not inline, f"{nom}: no enllaça css/fitxa.css o encara té <style>")
    comprova(s.count('class="previ"') == 1, f"{nom}: falta el rètol de material")
    comprova(s.count('Què hi veus?') == 1, f"{nom}: falta la pregunta d'obertura")
    # La pàgina de la vida de cada dia: un context real i una segona situació
    # amb la mateixa decisió, perquè el que s'aprèn no es quedi lligat a un cas.
    comprova(s.count('class="full vida"') == 1, f"{nom}: falta la pàgina «A la vida de cada dia»")
    print(f"  {nom:12} {len(pags)} pàg · html {'ok' if estructura else 'ERROR'}"
          f" · color {'cap' if not color else color} · css extern {enllac and not inline}")

print("\nCAIXA D'EINES")
app = open(ruta('caixa-eines.html'), encoding='utf-8').read()
e = Estructura(); e.feed(app)
comprova(not e.err and not e.pila, "caixa-eines.html: HTML mal tancat")

pestanyes = sorted({m for m in re.findall(r'data-mod="(\w+)"', app)})
seccions = sorted({m for m in re.findall(r'<section id="mod-(\w+)"', app)})
fitxers = sorted(glob.glob(ruta('js', 'moduls', '*.js')))
registrats = sorted({re.search(r'CE\.registra\("(\w+)"', open(x, encoding='utf-8').read()).group(1)
                     for x in fitxers})
carregats = re.findall(r'<script src="js/moduls/([\w-]+)\.js"', app)

comprova(pestanyes == seccions == registrats,
         f"identificadors descompassats: marcatge {pestanyes} · registrats {registrats}")
comprova(sorted(carregats) == sorted(os.path.basename(x)[:-3] for x in fitxers),
         "hi ha mòduls a js/moduls que no es carreguen, o a l'inrevés")
comprova(app.rindex('js/app.js') > max(app.rindex(f'js/moduls/{c}.js') for c in carregats),
         "js/app.js s'ha de carregar després de tots els mòduls")
print(f"  mòduls: {len(registrats)} · marcatge i registre coincideixen: {pestanyes == registrats}")
print(f"  app.js va l'últim: {app.rindex('js/app.js') > max(app.rindex(f'js/moduls/{c}.js') for c in carregats)}")

# Els números de tasca surten als enllaços que el docent envia (caixa-eines?task=n).
# Cada pestanya en porta un, sense repetir-se, i la tasca 0 va la primera perquè es
# mostra sempre. Un número ja enviat no es canvia mai: un mòdul nou pren el següent.
pestanyes_html = re.findall(r'<button[^>]*class="segment"[^>]*>', app)
numeros = [(re.search(r'data-tasca="([^"]*)"', b) or [None, None])[1] for b in pestanyes_html]
mods = [(re.search(r'data-mod="(\w+)"', b) or [None, '?'])[1] for b in pestanyes_html]
tasques_ok = (bool(numeros) and all(n is not None and re.fullmatch(r'0|[1-9]\d*', n) for n in numeros)
              and len(set(numeros)) == len(numeros) and numeros[0] == "0")
comprova(tasques_ok, f"data-tasca de les pestanyes: {numeros} "
                     "(cal un número a cada una, sense repetir, i el 0 el primer)")
print("  tasques: " + " · ".join(f"{n} {m}" for n, m in zip(numeros, mods)))

print("\nFRASES")
# Les frases viuen a dades/textos.js. El marcatge i el codi només hi apunten:
# si una clau no existeix, a la pantalla surt «[1.2.titol]», i això s'ha de
# detectar aquí i no a classe.
textos = open(ruta('dades', 'textos.js'), encoding='utf-8').read()
# Els grups poden ser «1.2» (una subtasca), «5» (una tasca sense subtasques) o
# «comu» (frases compartides). El nom del grup és tot el que va abans de
# l'últim punt de la clau, igual que fa CE.txt().
def claus_de(bloc):
    out = set()
    for grup, cos in re.findall(r'^  "([\w.]+)":\s*\{(.*?)\n  \}', bloc, re.S | re.M):
        for nom in re.findall(r'^\s{4}(\w+):', cos, re.M):
            out.add(grup + "." + nom)
    return out

tall = textos.index("window.TEXTOS_GUIA")
definides = claus_de(textos[:tall])
guiades = claus_de(textos[tall:])

# Les claus no sempre s'escriuen senceres: n'hi ha que es munten amb un
# prefix («1.3.» + quina) o amb el sufix «.nom» des del nucli. Si no es té en
# compte, l'avís d'orfes en delata vint que sí que es fan servir i s'acaba
# ignorant, que és pitjor que no tenir-lo.
grups = sorted({c.rsplit(".", 1)[0] for c in definides}, key=len, reverse=True)
g = "(?:" + "|".join(re.escape(x) for x in grups) + ")"
usades = set(re.findall(r'data-text="(' + g + r'\.\w+)"', app))
prefixos = set()
for f in sorted(glob.glob(ruta('js', '**', '*.js'), recursive=True)):
    codi = open(f, encoding='utf-8').read()
    # Una clau entre cometes que no va seguida d'un «+» (si hi va, és un prefix).
    # El nom comença per una lletra: així "0.01", que és un número, no compta
    # com a clau del grup «0».
    usades |= set(re.findall(r'"(' + g + r'\.[A-Za-z_]\w*)"(?!\s*\+)', codi))
    prefixos |= set(re.findall(r'"(' + g + r')\.\w*"\s*\+', codi))

comprova(not (usades - definides), f"frases que es demanen i no existeixen: {sorted(usades - definides)}")
comprova(not (definides - guiades), f"frases sense explicació a TEXTOS_GUIA: {sorted(definides - guiades)}")

orfes = sorted(c for c in definides - usades
               if not c.endswith(".nom")                 # les llegeix el nucli
               and c.rsplit(".", 1)[0] not in prefixos)  # clau muntada amb prefix
print(f"  frases definides: {len(definides)} · totes les que es demanen existeixen: {not (usades - definides)}")
print(f"  frases sense fer servir: {orfes if orfes else 'cap'}")

print("\nLECTURA FÀCIL")
# Les regles de la norma UNE 153101:2018 EX que es poden comprovar sense llegir.
# Les altres (una idea per frase, res de metàfores, la mateixa paraula per a la
# mateixa cosa) són a la capçalera de dades/textos.js i les ha de mirar una persona.
#   Falla: una frase de més de 20 paraules, una paraula repetida seguida
#          («situació situació»), «clica aquí», xifres romanes, hores de 24 h
#          o paraules senceres en majúscules que no siguin sigles conegudes.
#   Avisa: frases de més de 15 paraules, i parèntesis o punt i coma.
SIGLES = {"IVA", "EXE", "SHIFT", "FORMAT", "DEL", "AC", "CONFIG"}
ROMANS = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')

def frases_de(bloc):
    """{clau: text} de window.TEXTOS, desfent les cometes escapades."""
    out = {}
    for grup, cos in re.findall(r'^  "([\w.]+)":\s*\{(.*?)\n  \}', bloc, re.S | re.M):
        for nom, val in re.findall(r"^\s{4}(\w+):\s*'((?:[^'\\]|\\.)*)'", cos, re.M):
            out[grup + "." + nom] = re.sub(r"\\(.)", r"\1", val)
    return out

avisos_lf, falles_lf = [], []
for clau, t in frases_de(textos[:tall]).items():
    net = re.sub(r"\{\w+\}", "X", t.replace("*", ""))
    for frase in re.split(r"(?<=[.!?])\s+", net):
        paraules = re.findall(r"[\w·'’√π]+", frase)
        if len(paraules) > 20:
            falles_lf.append(f"{clau}: frase de {len(paraules)} paraules")
        elif len(paraules) > 15:
            avisos_lf.append(f"{clau}: frase de {len(paraules)} paraules")
    if re.search(r"\b(\w+)\s+\1\b", net, re.I):
        falles_lf.append(f"{clau}: paraula repetida («{re.search(r'\b(\w+)\s+\1\b', net, re.I).group(0)}»)")
    if re.search(r"\bclica\b|\bclic\b", net, re.I):
        falles_lf.append(f"{clau}: «clica aquí» no diu on porta")
    if re.search(r"\b([01]?\d|2[0-3]):[0-5]\d\b", net):
        falles_lf.append(f"{clau}: hora en format de 24 h")
    for p in re.findall(r"\b[A-ZÀ-Ú]{2,}\b", net):
        if p in SIGLES:
            continue
        if ROMANS.match(p):
            falles_lf.append(f"{clau}: xifra romana «{p}»")
        elif len(p) >= 3:
            falles_lf.append(f"{clau}: paraula en majúscules «{p}»")
    if re.search(r"[;()]", net):
        avisos_lf.append(f"{clau}: parèntesis o punt i coma")
for f in falles_lf:
    comprova(False, "Lectura Fàcil · " + f)
print(f"  frases revisades: {len(frases_de(textos[:tall]))} · errors: {len(falles_lf)} · avisos: {len(avisos_lf)}")
for a in avisos_lf:
    print("    avís ·", a)

print("\nSUBTASQUES")
# Un mòdul partit en 1.1, 1.2… necessita la barra de fletxes i panells numerats
# de manera seguida des de l'1, perquè els enllaços ?task=1.3 apuntin on toca.
for m in re.findall(r'<section id="mod-(\w+)"[^>]*>(.*?)</section>', app, re.S):
    nom, cos = m
    subs = [int(x) for x in re.findall(r'class="subtasca"[^>]*data-sub="(\d+)"', cos)]
    if not subs:
        continue
    comprova(subs == list(range(1, len(subs) + 1)),
             f"mod-{nom}: les subtasques van {subs}, han d'anar 1, 2, 3…")
    comprova(len(set(subs)) == len(subs), f"mod-{nom}: hi ha subtasques repetides")
    for peca in ("sub-enrere", "sub-avant", "sub-rotul"):
        comprova(peca in cos, f"mod-{nom} té subtasques però li falta .{peca}")
    pestanya = re.search(r'data-tasca="(\d+)" data-mod="' + nom + '"', app)
    if pestanya:
        for n in subs:
            clau = pestanya.group(1) + "." + str(n) + ".nom"
            comprova(clau in definides, f"falta la frase {clau} a dades/textos.js")
    print(f"  mod-{nom}: {len(subs)} subtasques, numerades bé i amb nom a textos.js")
if not re.search(r'class="subtasca"', app):
    print("  cap mòdul en té")

print("\nPDF")
# Un PDF per unitat i per destinatari. Es generen amb generadors/gen_pdf.py.
falten = []
for u in range(1, 8):
    if not os.path.exists(ruta('fitxes', f'ud{u}.html')):
        continue
    for mena in ('alumnat', 'solucionari'):
        f = ruta('pdf', f'ud{u}-{mena}.pdf')
        if not os.path.exists(f) or os.path.getsize(f) < 2000:
            falten.append(f'ud{u}-{mena}.pdf')
comprova(not falten, f"PDF que falten o buits: {falten}")

# El recompte de pàgines NO es fa aquí: WeasyPrint comprimeix els objectes del
# PDF i qualsevol intent de comptar-les llegint els bytes dona zero i deixa
# passar errors sense dir res. Qui ho comprova de debò és generadors/gen_pdf.py,
# que compara les pàgines generades amb els blocs .full de la fitxa i s'atura si
# no quadren.
print(f"  PDF presents: {14 - len(falten)}/14")

print("\nFULLS D'ESTIL")
# Una clau sense tancar no dona cap error visible: el navegador la tanca al final
# del fitxer i tot el que ve després queda dins d'aquell bloc. Així es va trencar
# app.css: un «@media (prefers-color-scheme:dark){» obert a dalt de tot feia que
# la caixa d'eines només tingués estils amb el mode fosc activat.
def claus_desaparellades(text):
    """Problemes de claus, amb la línia on són. Salta comentaris i cadenes."""
    linies, pila, errors = text.split('\n'), [], []
    i, n, linia = 0, len(text), 1
    while i < n:
        c = text[i]
        if text.startswith('/*', i):
            fi = text.find('*/', i + 2)
            if fi == -1:
                errors.append(f"comentari obert a la línia {linia} que no es tanca mai")
                break
            linia += text.count('\n', i, fi)
            i = fi + 2
            continue
        if c in '"\'':
            fi = i + 1
            while fi < n and text[fi] not in (c, '\n'):
                fi += 2 if text[fi] == '\\' else 1
            linia += text.count('\n', i, fi)
            i = fi + 1 if fi < n and text[fi] == c else fi
            continue
        if c == '\n':
            linia += 1
        elif c == '{':
            pila.append(linia)
        elif c == '}':
            if pila:
                pila.pop()
            else:
                errors.append(f"clau de tancament sobrant a la línia {linia}")
        i += 1
    errors += [f"clau oberta a la línia {l} que no es tanca mai: «{linies[l - 1].strip()[:50]}»"
               for l in pila]
    return errors

fulls = sorted(glob.glob(ruta('css', '*.css')))
for c in fulls:
    errors = claus_desaparellades(open(c, encoding='utf-8').read())
    comprova(not errors, f"{os.path.basename(c)}: " + "; ".join(errors))
    print(f"  {os.path.basename(c):12} claus {'ok' if not errors else 'ERROR · ' + errors[0]}")

# Una variable que no existeix tampoc avisa: la propietat es queda sense efecte.
# Així la barra de pestanyes s'havia quedat sense fons (--segment-fons). Les que
# porten valor de reserva, var(--x, …), no compten.
fonts = (fulls + glob.glob(ruta('js', '**', '*.js'), recursive=True)
         + glob.glob(ruta('*.html')) + glob.glob(ruta('fitxes', '*.html')))
textos = {f: open(f, encoding='utf-8').read() for f in fonts}
definides = {v for t in textos.values() for v in re.findall(r'(--[\w-]+)\s*:', t)}
sense_definir = {}
for f, t in textos.items():
    for v in re.findall(r'var\(\s*(--[\w-]+)\s*\)', t):
        if v not in definides:
            sense_definir.setdefault(v, set()).add(os.path.relpath(f, ARREL))
comprova(not sense_definir, "variables CSS que no estan definides enlloc: " +
         "; ".join(f"{v} a {', '.join(sorted(fs))}" for v, fs in sorted(sense_definir.items())))
print(f"  variables usades sense definir: {len(sense_definir)}")

print("\nCONTRAST (WCAG 2.2 AA)")
# Es calcula a partir de css/tokens.css, en mode clar i en mode fosc. Els colors
# amb transparència es componen sobre el fons on es fan servir de debò.
#   text normal ≥ 4,5:1   ·   xifres grans i elements gràfics ≥ 3:1
# Si canvies un color de la paleta de pantalla, aquest és l'avís que ho detecta.
def lineal(c):
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

def lluminancia(r):
    return 0.2126 * lineal(r[0]) + 0.7152 * lineal(r[1]) + 0.0722 * lineal(r[2])

def contrast(a, b):
    la, lb = lluminancia(a), lluminancia(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)

def a_rgb(valor, sota=(255, 255, 255)):
    valor = valor.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", valor)
    if m:
        return rgb(valor)
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+))?\s*\)", valor)
    if not m:
        raise ValueError(valor)
    alfa = float(m.group(4) or 1)
    return tuple(round(int(m.group(i + 1)) * alfa + sota[i] * (1 - alfa)) for i in range(3))

tokens = open(ruta('css', 'tokens.css'), encoding='utf-8').read()
clar = dict(re.findall(r"(--[\w-]+):\s*([^;]+);", tokens[:tokens.index("@media")]))
fosc = dict(clar, **dict(re.findall(r"(--[\w-]+):\s*([^;]+);", tokens[tokens.index("@media"):])))

PARELLES = [   # (primer pla, fons, mínim, on es fa servir)
    ("--etiqueta",   "--superficie", 4.5, "text principal"),
    ("--etiqueta-2", "--superficie", 4.5, "text secundari: ajudes, rètols"),
    ("--etiqueta-2", "--fons",       4.5, "text secundari sobre el fons de la pàgina"),
    ("--etiqueta-2", "--camp",       4.5, "avisos neutres i pastilles"),
    ("--etiqueta-3", "--superficie", 3.0, "traços dels eixos i xifres apagades (grans)"),
    ("#FFFFFF",      "--blau",       4.5, "lletra dels botons blaus"),
    ("--blau",       "--superficie", 3.0, "punts i línies blaves dels dibuixos"),
    ("--blau-text",  "--superficie", 4.5, "lletra blava: enllaços, marques"),
    ("--blau-text",  "--fons",       4.5, "enllaços sobre el fons de la pàgina"),
    ("--blau-text",  "--blau-suau",  4.5, "botons tenyits i etiqueta «Exemple»"),
    ("--blau-text",  "--camp",       4.5, "tecles d'operació de la calculadora"),
    ("--superficie", "--verd",       4.5, "rètol «Final» quan la tasca s'ha acabat"),
    ("--verd",       "--superficie", 4.5, "lletra verda dels dibuixos"),
    ("--taronja",    "--superficie", 4.5, "lletra taronja dels dibuixos"),
    ("--vermell",    "--superficie", 4.5, "xifres vermelles de la balança"),
    ("--etiqueta",   "--verd-suau",  4.5, "avisos de «Correcte»"),
    ("--etiqueta",   "--taronja-suau", 4.5, "avisos de «Incorrecte» i notes"),
]
for nom_mode, paleta in (("clar", clar), ("fosc", fosc)):
    sup = a_rgb(paleta["--superficie"])
    def valor(v, sota):
        return a_rgb(v if v.startswith("#") else paleta[v], sota)
    pitjor = None
    for pp, fons, minim, on in PARELLES:
        base = a_rgb(paleta[fons]) if fons in ("--fons", "--camp") else sup
        fons_rgb = valor(fons, sup)
        r = contrast(valor(pp, fons_rgb if fons in ("--fons", "--camp") else base), fons_rgb)
        comprova(r >= minim, f"contrast en mode {nom_mode}: {pp} sobre {fons} fa {r:.2f}:1 "
                             f"i en cal {minim}:1 ({on})")
        if pitjor is None or r / minim < pitjor[0] / pitjor[1]:
            pitjor = (r, minim, pp, fons)
    print(f"  mode {nom_mode}: {len(PARELLES)} parelles · la més justa, {pitjor[2]} sobre "
          f"{pitjor[3]}: {pitjor[0]:.2f}:1 (mínim {pitjor[1]}:1)")

print("\nDESPLEGAMENT")
# Encadenar CSS amb @import bloqueja el pintat: tokens.css s'enllaça des de l'HTML.
for c in sorted(glob.glob(ruta('css', '*.css'))):
    comprova('@import' not in open(c, encoding='utf-8').read(),
             f"{os.path.basename(c)} fa @import; enllaça tokens.css des de l'HTML")
print(f"  cap @import als fulls d'estil: {all('@import' not in open(c, encoding='utf-8').read() for c in glob.glob(ruta('css','*.css')))}")

# El navegador no renderitza Markdown: se'l baixa.
md = []
for f in glob.glob(ruta('*.html')):
    md += [(os.path.basename(f), u) for u in re.findall(r'href="([^"]+\.md)"', open(f, encoding='utf-8').read())]
comprova(not md, f"hi ha enllaços a Markdown des de les pàgines: {md}")
print(f"  enllaços a .md des de les pàgines: {len(md)}")

for necessari in ('_headers', 'robots.txt', '404.html', 'favicon.svg', '.gitignore'):
    comprova(os.path.exists(ruta(necessari)), f"falta {necessari}")
print("  fitxers de desplegament: tots presents")

print("\nANONIMAT")
# El material no ha d'anomenar mai el curs, el tipus d'aula ni el diagnòstic,
# ni parlar d'un alumne en singular. Es descriu alumnat amb dificultats de
# tipus cognitiu, i prou.
PROHIBITS = [r"4t ESO", r"4ESO", r"4t d'ESO", r"4t A\b", r"\bde 4t\b",
             r"\bSIEI\b", r"\bDIL\b", r"4eso", r"discapacitat intel",
             r"\bl'alumne\b", r"\bun alumne\b", r"\baquest alumne\b"]
trobats = []
for f in (glob.glob(os.path.join(ARREL, '**', '*.md'), recursive=True)
          + glob.glob(os.path.join(ARREL, '**', '*.html'), recursive=True)
          + glob.glob(os.path.join(ARREL, '**', '*.js'), recursive=True)
          + glob.glob(os.path.join(ARREL, '**', '*.css'), recursive=True)):
    text = open(f, encoding='utf-8').read()
    for patro in PROHIBITS:
        for m in re.finditer(patro, text, re.I):
            trobats.append((os.path.relpath(f, ARREL), m.group(0)))
comprova(not trobats, f"termes que trenquen l'anonimat: {trobats[:6]}")
print(f"  termes que trencarien l'anonimat: {len(trobats)}")

print("\nDEPENDÈNCIES EXTERNES")
remots = []
for f in glob.glob(ruta('**', '*.html'), recursive=True) + glob.glob(ruta('css', '*.css')):
    for u in re.findall(r'(?:src|href)="(https?://[^"]+)"', open(f, encoding='utf-8').read()):
        remots.append((os.path.relpath(f, ARREL), u))
comprova(not remots, f"recursos remots: {remots}")
print(f"  recursos remots: {len(remots)}")

print("\nDADES")
dades = open(ruta('dades', 'unitats.js'), encoding='utf-8').read()
unitats = re.findall(r'fitxa: "(fitxes/\w+\.html)"', dades)
for u in unitats:
    comprova(os.path.exists(ruta(u)), f"dades/unitats.js apunta a {u}, que no existeix")
comprova(len(unitats) == len(glob.glob(ruta('fitxes', '*.html'))),
         "el nombre d'unitats no coincideix amb el de fitxes")
print(f"  unitats declarades: {len(unitats)} · fitxes al disc: {len(glob.glob(ruta('fitxes','*.html')))}")

print()
if falles:
    print(f"{len(falles)} PROBLEMES:")
    for f in falles:
        print("  ·", f)
    sys.exit(1)
print("Tot correcte.")
