#!/usr/bin/env python3
"""Les regles dels quaderns d'activitats (CURS/uN/quadern.html), les mateixes a tots els cursos.

    python3 comu/eines/quaderns.py            (tots els cursos)

També es passa dins de cada CURS/eines/comprova.py (secció QUADERNS), com comu/eines/mapa.py.
Abans (fins al 6/11/2026) era una secció de 4eso/eines/comprova.py, i només hi havia el quadern
de la UD3 de 4eso/. Només fa servir la biblioteca estàndard.

Què mira, a cada quadern:
  · que surti del generador (comu/generadors/quadern.py amb CURS/generadors/quadern/udN.py):
    no s'edita a mà, i el fitxer publicat ha de ser exactament el que surt;
  · que hi hagi un quadern per a cada contingut i que dades/unitats.js els declari tots;
  · HTML ben tancat, blanc i negre estricte (el quadern i comu/css/quadern.css);
  · que enllaci el fitxa.css del curs, comu/css/quadern.css i comu/js/quadern.js;
  · que les activitats i el solucionari portin les mateixes marques (data-repte), i cada
    activitat l'a) i 12 apartats per fer, marcats 1 1 1 1 2 2 2 3 3 3 3 3 3 (petit, mitjà, alt);
  · els botons dels PDF, amb el mateix text que a les altres pàgines de paper;
  · consignes d'una frase i de 20 paraules com a molt; ni «adaptat» ni «sencer» parlant de
    nombres al que llegeix l'alumnat.
"""
import glob, os, re, sys
from html.parser import HTMLParser

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(REPO, "comu", "generadors"))
import quadern as motor  # noqa: E402

BUIDES = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source',
          'track', 'wbr', 'path', 'circle', 'rect', 'line', 'text', 'use', 'stop', 'polygon',
          'polyline', 'ellipse'}
ESPERAT = ['1'] * 4 + ['2'] * 3 + ['3'] * 6
SENCER = re.compile(r'\b(nombres?|quantitats?|coses?|xifres?|dos)\s+sencer(s|a|es)?\b', re.I)


class Estructura(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pila, self.err = [], []

    def handle_starttag(self, t, a):
        if t not in BUIDES:
            self.pila.append(t)

    def handle_startendtag(self, t, a):
        pass

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
    text = re.sub(r'/\*.*?\*/|<!--.*?-->', '', text, flags=re.S)
    return sorted({h for h in re.findall(r'(?<![&\w])#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?\b', text)
                   if len(set(rgb(h))) > 1})


def comprova_comu():
    """El que és de tots els cursos: el full d'estil del quadern, en blanc i negre."""
    css = open(os.path.join(REPO, 'comu', 'css', 'quadern.css'), encoding='utf-8').read()
    color = cromatics(css)
    return [f"comu/css/quadern.css conté color ({color})"] if color else []


def comprova_curs(curs):
    """Torna (problemes, línies de resum) dels quaderns d'un curs."""
    falles, resum = [], []

    def comprova(cond, msg):
        if not cond:
            falles.append(msg)
        return cond

    arrel = os.path.join(REPO, curs)
    fonts = motor.unitats(curs)
    fitxers = sorted(glob.glob(os.path.join(arrel, 'u[0-9]*', 'quadern.html')))
    nums = sorted(int(re.search(r'u(\d+)', os.path.relpath(f, arrel))[1]) for f in fitxers)
    comprova(fonts == nums, f"{curs}: generadors/quadern/ té {fonts} i les carpetes uN/ en tenen {nums}")
    dades = open(os.path.join(arrel, 'dades', 'unitats.js'), encoding='utf-8').read()
    declarats = sorted(re.findall(r'quadern: "(u\d+/quadern\.html)"', dades))
    comprova(declarats == sorted(f"u{n}/quadern.html" for n in nums),
             f"{curs}: els quaderns de dades/unitats.js ({declarats}) no són els de les carpetes uN/")

    for f in fitxers:
        nom = os.path.relpath(f, REPO).replace(os.sep, '/')
        s = open(f, encoding='utf-8').read()
        e = Estructura()
        e.feed(s)
        estructura = not e.err and not e.pila
        color = cromatics(s)
        acts = re.findall(r'<div class="exercici act"( data-repte)?>', s)
        sols = re.findall(r'<div class="sol-act"( data-repte)?>', s)
        comprova(estructura, f"{nom}: HTML mal tancat")
        comprova(not color, f"{nom}: hi ha color ({color})")
        comprova('../css/fitxa.css' in s and '../../comu/css/quadern.css' in s and '../../comu/js/quadern.js' in s,
                 f"{nom}: ha d'enllaçar css/fitxa.css, comu/css/quadern.css i comu/js/quadern.js")
        comprova(acts and acts == sols, f"{nom}: les activitats i el solucionari no porten les mateixes marques")
        comprova('id="pdf-alumnat">' in s and s.count('PDF alumnat</button>') == 1
                 and 'id="pdf-solucionari">' in s and s.count('PDF solucionari</button>') == 1,
                 f"{nom}: els botons han de ser «PDF alumnat» i «PDF solucionari», com a les altres pàgines de paper")
        tall = s.index('<div class="quadern sol"')
        for part, marca, on in ((s[:tall], '<div class="exercici act"', "l'activitat"),
                                (s[tall:], '<div class="sol-act"', "el solucionari de l'activitat")):
            for i, tros in enumerate(part.split(marca)[1:], 1):
                marques = re.findall(r'class="ap[^"]*" data-n="(\d)"', tros)
                comprova(marques == ESPERAT, f"{nom}: {on} {i} té els apartats {''.join(marques)}"
                                             f" (han de ser {''.join(ESPERAT)})")
        for q in re.findall(r'<div class="q">(.*?)(?:\n|</div>)', s):
            q = re.sub(r'<[^>]+>', '', q)
            comprova(len(re.findall(r"[\w·'’]+", q)) <= 20, f"{nom}: consigna de més de 20 paraules: «{q}»")
        alumnat = re.sub(r'<!--.*?-->', '', s[:tall], flags=re.S)
        comprova(not re.search(r'adapta(t|da|ts|des|ció|cions)\b', alumnat, re.I),
                 f"{nom}: l'alumnat no ha de llegir «adaptat»")
        comprova(not SENCER.search(alumnat), f"{nom}: «sencer» parlant de nombres (el terme és «enter»)")
        n = int(re.search(r'u(\d+)', nom)[1])
        if n in fonts:
            try:
                igual = motor.genera(curs, n) == s
            except AssertionError as err:
                igual = comprova(False, f"{nom}: el generador s'atura: {err}")
            comprova(igual, f"{nom} no és el que surt de {curs}/generadors/quadern/ud{n}.py "
                            f"(no s'edita a mà: passa python3 {curs}/generadors/gen_quadern.py {n})")
        resum.append(f"  {nom:22} html {'ok' if estructura else 'ERROR'} · color {'cap' if not color else color}"
                     f" · {sum(1 for r in acts if not r)} activitats i {sum(1 for r in acts if r)} de repte,"
                     f" de 3, 6 o 12 apartats")
    return falles, resum


def main():
    falles = comprova_comu()
    for curs in motor.CURSOS:
        f, r = comprova_curs(curs)
        falles += f
        print("\n".join(r))
    if falles:
        print(f"\n{len(falles)} PROBLEMES:")
        for f in falles:
            print("  ·", f)
        sys.exit(1)
    print("Quaderns: correcte.")


if __name__ == "__main__":
    main()
