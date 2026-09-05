#!/usr/bin/env python3
"""Comprovacions del projecte. Es passa abans de publicar res.

    python3 eines/comprova.py

Verifica les regles que és fàcil trencar sense adonar-se'n: que les fitxes no
tinguin cap color, que l'HTML tanqui bé, que la numeració de pàgines sigui
seguida, que cada fitxa porti el rètol de material i la pregunta d'obertura, i
que els mòduls declarats al marcatge de l'app siguin els que es registren.
"""
import re, sys, glob, os
from html.parser import HTMLParser

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB   = os.path.join(ARREL, 'web')   # el que es publica
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
    """Tot el que es comprova viu dins de web/, que és el que es publica."""
    return os.path.join(WEB, *p)


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
carregats = re.findall(r'js/moduls/([\w-]+)\.js', app)

comprova(pestanyes == seccions == registrats,
         f"identificadors descompassats: marcatge {pestanyes} · registrats {registrats}")
comprova(sorted(carregats) == sorted(os.path.basename(x)[:-3] for x in fitxers),
         "hi ha mòduls a js/moduls que no es carreguen, o a l'inrevés")
comprova(app.rindex('js/app.js') > max(app.rindex(f'js/moduls/{c}.js') for c in carregats),
         "js/app.js s'ha de carregar després de tots els mòduls")
print(f"  mòduls: {len(registrats)} · marcatge i registre coincideixen: {pestanyes == registrats}")
print(f"  app.js va l'últim: {app.rindex('js/app.js') > max(app.rindex(f'js/moduls/{c}.js') for c in carregats)}")

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

for necessari in ('_headers', 'robots.txt', '404.html', 'favicon.svg'):
    comprova(os.path.exists(ruta(necessari)), f"falta web/{necessari}")
comprova(os.path.exists(os.path.join(ARREL, '.gitignore')), "falta .gitignore")
print("  fitxers de desplegament: tots presents")

# La documentació de l'alumne no pot ser dins de web/, que és el que es publica.
comprova(not os.path.exists(ruta('..', 'web', 'docs')) and not os.path.isdir(os.path.join(WEB, 'docs')),
         "hi ha una carpeta docs/ dins de web/: es publicaria")
print(f"  docs/ fora de web/: {not os.path.isdir(os.path.join(WEB, 'docs'))}")

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
