#!/usr/bin/env python3
"""Comprovacions del material de 1eso/. Es passa abans de publicar res.

    python3 1eso/eines/comprova.py      (des de l'arrel del repositori)

No necessita res més que Python 3.8 o posterior. Verifica les regles que és
fàcil trencar sense adonar-se'n:

  · el paper és en blanc i negre, l'HTML tanca bé i les pàgines van seguides;
  · a les pàgines de l'alumnat es multiplica amb «·», cap nombre passa de 999,
    les frases segueixen les regles de Lectura Fàcil que es poden comprovar
    soles, i cap multiplicació, suma o resta escrita no està malament;
  · el text manuscrit només porta caràcters que la lletra Caveat sap dibuixar;
  · cada PDF és el que sortiria ara de la seva font (empremtes.json);
  · els fulls d'estil tanquen les claus i no fan servir variables inexistents,
    i els colors de la pantalla tenen el contrast que demana la WCAG 2.2 AA;
  · cap enllaç queda penjat, cap fitxer depèn d'internet, cap text no anomena
    el curs, el tipus d'aula, un diagnòstic ni cap alumne concret, i les dades
    de dades/unitats.js quadren amb el que hi ha al disc.

Falla: el que s'ha d'arreglar abans de publicar. Avisa: el que cal mirar.
"""
import glob, json, os, re, struct, sys
from html.parser import HTMLParser

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # 1eso/
REPO = os.path.dirname(ARREL)                                          # l'arrel del repositori
sys.path.insert(0, os.path.join(ARREL, 'eines'))
import paper  # noqa: E402  (només biblioteca estàndard)

falles, avisos = [], []


def comprova(condicio, missatge):
    if not condicio:
        falles.append(missatge)
    return condicio


def avisa(condicio, missatge):
    if not condicio:
        avisos.append(missatge)
    return condicio


def ruta(*p):
    return os.path.join(ARREL, *p)


def rel(f):
    return os.path.relpath(f, ARREL)


def llegeix(f):
    with open(f, encoding='utf-8') as h:
        return h.read()


FITXES = sorted(glob.glob(ruta('fitxes', '*.html')))
TARGETES = sorted(glob.glob(ruta('targetes', '*.html')))
PAPER = FITXES + TARGETES

# --------------------------------------------------------------------------
# Eines
# --------------------------------------------------------------------------

BUIDES = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source',
          'track', 'wbr', 'path', 'circle', 'rect', 'line', 'use', 'stop', 'polygon',
          'polyline', 'ellipse'}


class Estructura(HTMLParser):
    """Comprova que cada etiqueta que s'obre es tanqui, i en l'ordre bo."""
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


# El text que es veu, partit en trossos: un per element de bloc. Cada tros
# recorda les classes de tots els elements que el contenen.
BLOC = {'p', 'div', 'li', 'td', 'th', 'tr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'br', 'table',
        'section', 'label', 'ul', 'ol', 'dt', 'dd', 'caption', 'figcaption', 'svg', 'text'}
AMAGAT = {'script', 'style', 'title', 'head'}
BUIDES_HTML = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta',
               'source', 'track', 'wbr'}
PER_A_L_ADULT = {'sol', 'previ', 'pag'}   # solucionari, rètol del graó físic i peu


class Visible(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pila, self.trossos, self.actual = [], [], []

    def _classes(self):
        return frozenset(c for _, cs in self.pila for c in cs)

    def _tanca(self):
        if self.actual:
            self.trossos.append(self.actual)
            self.actual = []

    def handle_starttag(self, t, a):
        if t in BLOC:
            self._tanca()
        if t not in BUIDES_HTML:
            self.pila.append((t, frozenset((dict(a).get('class') or '').split())))

    def handle_startendtag(self, t, a):
        if t in BLOC:
            self._tanca()

    def handle_endtag(self, t):
        if t in BLOC:
            self._tanca()
        for i in range(len(self.pila) - 1, -1, -1):
            if self.pila[i][0] == t:
                del self.pila[i:]
                break

    def handle_data(self, d):
        if not any(t in AMAGAT for t, _ in self.pila):
            self.actual.append((d, self._classes()))

    def close(self):
        super().close()
        self._tanca()


def trossos(fitxer):
    """[[(text, classes), ...], ...]: el text visible, un tros per bloc."""
    v = Visible()
    v.feed(llegeix(fitxer))
    v.close()
    return v.trossos


def frases_alumnat(fitxer, sense=frozenset()):
    """El text que llegeix l'alumnat, un element per bloc, sense el de l'adult."""
    fora = PER_A_L_ADULT | set(sense)
    out = []
    for tros in trossos(fitxer):
        text = ' '.join(''.join(t for t, c in tros if not (c & fora)).split())
        if text:
            out.append(text)
    return out


def tot_el_text(fitxer):
    """Tot el text visible, també el de l'adult, en una sola cadena."""
    return ' '.join(' '.join(''.join(t for t, _ in tros).split()) for tros in trossos(fitxer))


def rgb(h):
    h = h.lstrip('#')
    h = ''.join(c * 2 for c in h) if len(h) == 3 else h
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


NOMS_DE_COLOR = (r'red|green|blue|yellow|orange|purple|pink|brown|cyan|magenta|lime|navy|'
                 r'teal|olive|maroon|violet|indigo|gold|coral|salmon|crimson|tomato|orchid|'
                 r'turquoise|aqua|fuchsia')


def cromatics(text):
    """Colors que no són grisos, en qualsevol de les maneres d'escriure'ls."""
    text = re.sub(r'/\*.*?\*/|<!--.*?-->', '', text, flags=re.S)
    trobats = {h for h in re.findall(r'(?<![&\w])#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?\b', text)
               if len(set(rgb(h))) > 1}
    trobats |= {m.group(0) for m in re.finditer(r'rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)', text)
                if len({m.group(1), m.group(2), m.group(3)}) > 1}
    trobats |= {m.group(0) for m in re.finditer(r'hsla?\(\s*[\d.]+\w*\s*,\s*([\d.]+)%', text)
                if float(m.group(1)) > 0}
    trobats |= {m.group(0) for m in re.finditer(
        r'(?:color|fill|stroke|background(?:-color)?)\s*[:=]\s*["\']?(?:' + NOMS_DE_COLOR + r')\b',
        text, re.I)}
    return sorted(trobats)


def caracters_de_la_lletra(cami):
    """Codis Unicode que una lletra TrueType sap dibuixar (taula cmap, formats 4 i 12).

    Es llegeix a mà per no dependre de fontTools. Dona el mateix que
    fontTools.getBestCmap() amb Caveat (753 caràcters) i amb DejaVu Sans.
    """
    with open(cami, 'rb') as f:
        d = f.read()
    n_taules = struct.unpack('>H', d[4:6])[0]
    taules = {}
    for i in range(n_taules):
        etiqueta, _, desp, _ = struct.unpack('>4sIII', d[12 + 16 * i: 28 + 16 * i])
        taules[etiqueta] = desp
    base = taules[b'cmap']
    n = struct.unpack('>H', d[base + 2:base + 4])[0]
    codis = set()
    for i in range(n):
        plataforma, _, desp = struct.unpack('>HHI', d[base + 4 + 8 * i: base + 12 + 8 * i])
        if plataforma not in (0, 3):
            continue
        s = base + desp
        fmt = struct.unpack('>H', d[s:s + 2])[0]
        if fmt == 4:
            seg2 = struct.unpack('>H', d[s + 6:s + 8])[0]
            seg = seg2 // 2
            finals = struct.unpack(f'>{seg}H', d[s + 14: s + 14 + seg2])
            inicis = struct.unpack(f'>{seg}H', d[s + 16 + seg2: s + 16 + 2 * seg2])
            deltes = struct.unpack(f'>{seg}h', d[s + 16 + 2 * seg2: s + 16 + 3 * seg2])
            pos_ro = s + 16 + 3 * seg2
            ros = struct.unpack(f'>{seg}H', d[pos_ro: pos_ro + seg2])
            for k in range(seg):
                for c in range(inicis[k], finals[k] + 1):
                    if c == 0xFFFF:
                        continue
                    if ros[k] == 0:
                        glif = (c + deltes[k]) & 0xFFFF
                    else:
                        adr = pos_ro + 2 * k + ros[k] + 2 * (c - inicis[k])
                        glif = struct.unpack('>H', d[adr:adr + 2])[0]
                        if glif:
                            glif = (glif + deltes[k]) & 0xFFFF
                    if glif:
                        codis.add(c)
        elif fmt == 12:
            n_grups = struct.unpack('>I', d[s + 12:s + 16])[0]
            for g in range(n_grups):
                ini, fi, glif0 = struct.unpack('>III', d[s + 16 + 12 * g: s + 28 + 12 * g])
                for c in range(ini, fi + 1):
                    if glif0 + (c - ini):
                        codis.add(c)
    return codis


# --------------------------------------------------------------------------
print("FITXES I TARGETES")
# --------------------------------------------------------------------------
css_fitxa = llegeix(ruta('css', 'fitxa.css'))
comprova(not cromatics(css_fitxa), f"css/fitxa.css conté color: {cromatics(css_fitxa)}")
print(f"  css/fitxa.css                cap color: {not cromatics(css_fitxa)}")
if not FITXES:
    print("  encara no hi ha cap fitxa a fitxes/")

for f in PAPER:
    nom = rel(f)
    s = llegeix(f)
    e = Estructura()
    e.feed(s)
    estructura = not e.err and not e.pila
    color = cromatics(s)
    cap, alumnat, sol = paper.blocs(s)
    comprova(estructura, f"{nom}: HTML mal tancat ({e.err[:3] or e.pila[-3:]})")
    comprova(not color, f"{nom}: hi ha color ({color})")
    comprova('../css/tokens.css' in cap and '../css/fitxa.css' in cap and '<style' not in s,
             f"{nom}: ha d'enllaçar ../css/tokens.css i ../css/fitxa.css, i no pot dur <style>")
    comprova(len(re.findall(r'<div class="full[^"]*">', s)) == len(alumnat) + len(sol),
             f"{nom}: algun bloc .full no acaba amb un </div> a principi de línia")
    if f in FITXES:
        pags = [int(n) for n in re.findall(r'· pàgina (\d+)</div>', s)]
        comprova(pags == list(range(1, len(pags) + 1)), f"{nom}: numeració de pàgines {pags}")
        comprova(s.count('class="previ"') == 1, f"{nom}: falta el rètol del graó físic (.previ)")
        comprova(s.count('Què hi veus?') == 1, f"{nom}: falta la pregunta d'obertura")
        comprova(s.count('class="full vida"') == 1, f"{nom}: falta la pàgina «A la vida de cada dia»")
        comprova(bool(sol), f"{nom}: falta el solucionari (.full.sol)")
        detall = f"{len(pags)} pàg."
    else:
        cares = [int(n) for n in re.findall(r'· cara (\d+)</div>', s)]
        comprova(cares == list(range(1, len(alumnat) + 1)), f"{nom}: numeració de cares {cares}")
        detall = f"{len(cares)} cares"
    print(f"  {nom:28} {detall} · html {'ok' if estructura else 'ERROR'} · "
          f"color {'cap' if not color else color}")

# --------------------------------------------------------------------------
print("\nPÀGINES DE L'ALUMNAT")
# Regles del material (docs/CRITERIS-DISSENY.md) que es poden comprovar soles.
# --------------------------------------------------------------------------
SIGLES = {"PDF"}
ROMANS = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
# Les decisions de llenguatge de l'examen revisat pel docent (comu/docs/EXAMENS-DOCX.md, §5).
LLENGUATGE = [(r'\bEncercla\b', "«Encercla»: el verb és «Marca»"),
              (r'\bsencer(s|a|es)?\b', "«sencer»: el terme és «enter»"),
              (r'\bquant fa\b', "«quant fa»: fes servir el verb literal («quant és», «quant mesura»)"),
              (r'\bho \w+ries\b', "«ho …ries»: sense pronoms febles"),
              (r'\bnomés fas\b', "«només fas»: deixa de ser veritat si s'hi afegeixen apartats")]
NOMBRE = re.compile(r'(?<![\d.,])\d{1,3}(?:\.\d{3})+(?![\d,])|(?<![\d.,])\d+')

n_frases = n_operacions = 0
for f in PAPER:
    nom = rel(f)
    s = llegeix(f)
    sense_comentaris = re.sub(r'<!--.*?-->', '', s, flags=re.S)

    # Dignitat: cap pàgina de l'alumnat no diu que és adaptada, ni al títol.
    comprova(not re.search(r'adapta(t|da|ts|des|ció|cions)\b', sense_comentaris, re.I),
             f"{nom}: diu «adaptat» en algun lloc que es veu")

    # Per multiplicar, el punt de l'ESO. «×» només pot sortir dins de
    # .simbol-primaria, que és on la targeta de les taules fa el pont.
    for tros in trossos(f):
        for t, c in tros:
            if '×' in t and 'simbol-primaria' not in c:
                falles.append(f"{nom}: «×» fora de .simbol-primaria: «{' '.join(t.split())[:40]}»")
    for frase in frases_alumnat(f, sense={'simbol-primaria'}):
        m = re.search(r'\d\s*[xX]\s*\d', frase)
        comprova(not m, f"{nom}: multiplicació amb la lletra x: «{m.group(0) if m else ''}»")

    for frase in frases_alumnat(f):
        n_frases += 1
        for m in NOMBRE.finditer(frase):
            comprova(int(m.group(0).replace('.', '')) <= 999,
                     f"{nom}: el nombre {m.group(0)} passa de 999: «{frase[:50]}»")
        for tall in re.split(r'(?<=[.!?])\s+', frase):
            paraules = re.findall(r"[\w·'’]+", tall)
            comprova(len(paraules) <= 20, f"{nom}: frase de {len(paraules)} paraules: «{tall[:50]}…»")
            avisa(len(paraules) <= 15, f"{nom}: frase de {len(paraules)} paraules: «{tall[:50]}…»")
        rep = re.search(r'\b([^\W\d]+)\s+\1\b', frase, re.I)
        comprova(not rep, f"{nom}: paraula repetida («{rep.group(0) if rep else ''}»)")
        comprova(not re.search(r'\bclica\b|\bclic\b', frase, re.I), f"{nom}: «clica aquí» no diu on porta")
        comprova(not re.search(r'\b([01]?\d|2[0-3]):[0-5]\d\b', frase), f"{nom}: hora en format de 24 h")
        for p in re.findall(r'\b[A-ZÀ-Ú]{2,}\b', frase):
            if p in SIGLES:
                continue
            comprova(not ROMANS.match(p), f"{nom}: xifres romanes («{p}»)")
            comprova(len(p) < 3 or ROMANS.match(p), f"{nom}: paraula en majúscules («{p}»)")
        for patro, explicacio in LLENGUATGE:
            avisa(not re.search(patro, frase, re.I), f"{nom}: {explicacio}")

    # Cap operació escrita pot estar malament: ni a l'alumnat ni al solucionari.
    text = tot_el_text(f)
    for a, op, b, r in re.findall(r'(\d+)\s*([·+−-])\s*(\d+)\s*=\s*(\d+)', text):
        n_operacions += 1
        a, b, r = int(a), int(b), int(r)
        bo = {'·': a * b, '+': a + b, '−': a - b, '-': a - b}[op]
        comprova(bo == r, f"{nom}: {a} {op} {b} = {r} està malament (és {bo})")

    # La targeta de les taules ha de tenir les cent, ni una més ni una menys.
    if os.path.basename(f) == 'taules.html':
        parelles = sorted((int(a), int(b)) for a, b in re.findall(r'(\d+)\s*·\s*(\d+)\s*=\s*\d+', text))
        esperades = sorted((a, b) for a in range(1, 11) for b in range(1, 11))
        comprova(parelles == esperades, f"{nom}: no hi ha exactament les cent multiplicacions de l'1 al 10")
print(f"  {len(PAPER)} fitxers · {n_frases} frases de l'alumnat · {n_operacions} operacions comprovades")

# --------------------------------------------------------------------------
print("\nLLETRA MANUSCRITA")
# Sense la lletra al repositori, el PDF surt amb el model resolt en lletra
# d'impremta i no avisa ningú. I Caveat no té tots els caràcters.
# --------------------------------------------------------------------------
tokens = llegeix(ruta('css', 'tokens.css'))
cara_lletra = re.search(r'@font-face\s*\{[^}]*font-family:\s*"Caveat"[^}]*url\("([^"]+)"', tokens)
comprova(bool(cara_lletra), "css/tokens.css no declara la lletra Caveat amb @font-face")
fitxer_lletra = os.path.normpath(os.path.join(ruta('css'), cara_lletra.group(1))) if cara_lletra else ''
comprova(os.path.exists(fitxer_lletra), f"no hi ha el fitxer de la lletra: {rel(fitxer_lletra) if fitxer_lletra else '?'}")
comprova(os.path.exists(ruta('fonts', 'OFL.txt')), "falta fonts/OFL.txt: la llicència de Caveat ha d'anar amb la lletra")
comprova(re.search(r'--manuscrita:\s*"Caveat"', tokens) is not None,
         "--manuscrita ha de començar per \"Caveat\"")
if os.path.exists(fitxer_lletra):
    te = caracters_de_la_lletra(fitxer_lletra)
    n_ms = 0
    for f in PAPER:
        for tros in trossos(f):
            for t, c in tros:
                if c & {'ms', 'et-resolt'}:
                    n_ms += len(t.strip())
                    falten = sorted({ch for ch in t if not ch.isspace() and ord(ch) not in te})
                    comprova(not falten, f"{rel(f)}: text manuscrit amb caràcters que Caveat no té: "
                                         f"{' '.join(falten)} (a «{t.strip()[:30]}»)")
    print(f"  {rel(fitxer_lletra)}: {len(te)} caràcters · {n_ms} caràcters manuscrits comprovats")

# --------------------------------------------------------------------------
print("\nPDF")
# Cada PDF ha de ser el que sortiria ara de la seva font. gen_pdf.py desa
# l'empremta de la font i de tot el que en decideix l'aspecte.
# --------------------------------------------------------------------------
esperats = {}
for f in FITXES:
    n = os.path.basename(f)[:-5]
    esperats[f"{n}-alumnat.pdf"] = rel(f)
    esperats[f"{n}-solucionari.pdf"] = rel(f)
for f in TARGETES:
    esperats[f"targeta-{os.path.basename(f)[:-5]}.pdf"] = rel(f)
try:
    empremtes = json.loads(llegeix(ruta('pdf', 'empremtes.json')))
except FileNotFoundError:
    empremtes = {}
    comprova(not esperats, "falta pdf/empremtes.json: passa generadors/gen_pdf.py")
al_dia = 0
for pdf, font in sorted(esperats.items()):
    if not comprova(os.path.exists(ruta('pdf', pdf)), f"falta pdf/{pdf}: passa generadors/gen_pdf.py"):
        continue
    e = empremtes.get(pdf, {})
    if comprova(e.get('empremta') == paper.empremta(font),
                f"pdf/{pdf} és d'abans de l'últim canvi de {font} o dels estils: passa generadors/gen_pdf.py"):
        al_dia += 1
for pdf in sorted(set(empremtes) - set(esperats)):
    avisa(False, f"pdf/empremtes.json parla de {pdf}, que ja no té font")
for pdf in sorted(os.path.basename(p) for p in glob.glob(ruta('pdf', '*.pdf'))):
    avisa(pdf in esperats, f"pdf/{pdf} no surt de cap fitxa ni targeta")
print(f"  PDF al dia: {al_dia}/{len(esperats)}")

# --------------------------------------------------------------------------
print("\nFULLS D'ESTIL")
# Una clau sense tancar no dona cap error visible: el navegador la tanca al final
# del fitxer i tot el que ve després queda dins d'aquell bloc.
# --------------------------------------------------------------------------
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
    text = llegeix(c)
    errors = claus_desaparellades(text)
    comprova(not errors, f"{rel(c)}: " + "; ".join(errors))
    comprova('@import' not in text, f"{rel(c)} fa @import: enllaça els fulls des de l'HTML")
    print(f"  {rel(c):16} claus {'ok' if not errors else 'ERROR · ' + errors[0]}")

# Una variable que no existeix tampoc avisa: la propietat es queda sense efecte.
# Les que porten valor de reserva, var(--x, …), no compten.
fonts_css = fulls + glob.glob(ruta('**', '*.html'), recursive=True) + glob.glob(ruta('js', '*.js'))
textos = {f: llegeix(f) for f in fonts_css}
definides = {v for t in textos.values() for v in re.findall(r'(--[\w-]+)\s*:', t)}
sense_definir = {}
for f, t in textos.items():
    for v in re.findall(r'var\(\s*(--[\w-]+)\s*\)', t):
        if v not in definides:
            sense_definir.setdefault(v, set()).add(rel(f))
comprova(not sense_definir, "variables CSS que no estan definides enlloc: " +
         "; ".join(f"{v} a {', '.join(sorted(fs))}" for v, fs in sorted(sense_definir.items())))
print(f"  variables usades sense definir: {len(sense_definir)}")

# --------------------------------------------------------------------------
print("\nCONTRAST (WCAG 2.2 AA)")
# La paleta de pantalla de index.html, en mode clar i en mode fosc. Els colors
# amb transparència es componen sobre el fons on es fan servir de debò.
#   text normal ≥ 4,5:1   ·   elements gràfics ≥ 3:1
# --------------------------------------------------------------------------
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
    if re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", valor):
        return rgb(valor)
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+))?\s*\)", valor)
    if not m:
        raise ValueError(valor)
    alfa = float(m.group(4) or 1)
    return tuple(round(int(m.group(i + 1)) * alfa + sota[i] * (1 - alfa)) for i in range(3))


clar = dict(re.findall(r"(--[\w-]+):\s*([^;]+);", tokens[:tokens.index("@media")]))
fosc = dict(clar, **dict(re.findall(r"(--[\w-]+):\s*([^;]+);", tokens[tokens.index("@media"):])))
PARELLES = [   # (primer pla, fons, mínim, on es fa servir a index.html)
    ("--etiqueta",   "--superficie",   4.5, "text de les targetes"),
    ("--etiqueta-2", "--superficie",   4.5, "text secundari de les targetes"),
    ("--etiqueta-2", "--fons",         4.5, "subtítol, entradeta i peu"),
    ("--etiqueta-2", "--camp",         4.5, "etiquetes grises"),
    ("#FFFFFF",      "--blau",         4.5, "lletra dels botons dels PDF"),
    ("--blau-text",  "--superficie",   4.5, "enllaços dins de les targetes"),
    ("--blau-text",  "--fons",         4.5, "enllaços sobre el fons"),
    ("--blau-text",  "--blau-suau",    4.5, "número de la unitat"),
    ("--etiqueta",   "--verd-suau",    4.5, "etiqueta verda"),
    ("--etiqueta",   "--taronja-suau", 4.5, "nota taronja"),
]
for nom_mode, paleta in (("clar", clar), ("fosc", fosc)):
    sup = a_rgb(paleta["--superficie"])
    pitjor = None
    for pp, fons, minim, on in PARELLES:
        base = a_rgb(paleta[fons]) if fons in ("--fons", "--camp") else sup
        fons_rgb = a_rgb(paleta[fons], sup) if not fons.startswith('#') else rgb(fons)
        pp_rgb = rgb(pp) if pp.startswith('#') else a_rgb(paleta[pp], fons_rgb if fons in ("--fons", "--camp") else base)
        r = contrast(pp_rgb, fons_rgb)
        comprova(r >= minim, f"contrast en mode {nom_mode}: {pp} sobre {fons} fa {r:.2f}:1 "
                             f"i en cal {minim}:1 ({on})")
        if pitjor is None or r / minim < pitjor[0] / pitjor[1]:
            pitjor = (r, minim, pp, fons)
    print(f"  mode {nom_mode}: {len(PARELLES)} parelles · la més justa, {pitjor[2]} sobre "
          f"{pitjor[3]}: {pitjor[0]:.2f}:1 (mínim {pitjor[1]}:1)")

# --------------------------------------------------------------------------
print("\nENLLAÇOS")
# Tot va amb rutes relatives: així funciona igual publicat que des d'un llapis
# de memòria. Una ruta que comença per «/» apuntaria a l'arrel del lloc, fora
# de 1eso/. I el navegador no mostra Markdown: el baixa.
# --------------------------------------------------------------------------
n_enllacos = 0
for f in glob.glob(ruta('**', '*.html'), recursive=True) + fulls:
    text = re.sub(r'<!--.*?-->|/\*.*?\*/', '', llegeix(f), flags=re.S)
    destins = re.findall(r'(?:href|src)="([^"]+)"', text) + re.findall(r'url\(\s*["\']?([^"\')]+)', text)
    for d in destins:
        if re.match(r'(https?:|mailto:|data:|javascript:|#)', d):
            continue
        n_enllacos += 1
        net = d.split('#')[0].split('?')[0]
        comprova(not net.startswith('/'), f"{rel(f)}: ruta absoluta «{d}»: fes-la relativa")
        comprova(os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), net))),
                 f"{rel(f)}: l'enllaç «{d}» no porta enlloc")
        comprova(not net.endswith('.md') or f.endswith('.css'), f"{rel(f)}: enllaç a Markdown «{d}»")
print(f"  enllaços relatius comprovats: {n_enllacos}")

# --------------------------------------------------------------------------
print("\nDESPLEGAMENT")
# Els fitxers de publicació són a l'arrel del repositori i no són de 1eso/.
# Si en falta cap, no és feina d'aquesta carpeta, però cal saber-ho.
# --------------------------------------------------------------------------
for necessari in ('_headers', 'robots.txt', '404.html', 'favicon.svg', '.gitignore'):
    avisa(os.path.exists(os.path.join(REPO, necessari)), f"falta {necessari} a l'arrel del repositori")
print(f"  fitxers de desplegament a l'arrel: "
      f"{sum(os.path.exists(os.path.join(REPO, n)) for n in ('_headers', 'robots.txt', '404.html', 'favicon.svg', '.gitignore'))}/5")

# --------------------------------------------------------------------------
print("\nANONIMAT")
# Cap fitxer de 1eso/ no anomena el curs, el tipus d'aula ni cap diagnòstic, ni
# parla d'un alumne o d'una alumna en concret. Es descriu alumnat amb
# dificultats de tipus cognitiu, i prou. L'única excepció és el nom de la
# carpeta, que surt a les adreces: «1eso» passa dins d'una ruta, amb una barra
# al costat. Hi ha també els termes que vigila el test de 4eso/, que mira tot
# el repositori.
# --------------------------------------------------------------------------
PROHIBITS = [
    r"\b1r\s+ESO\b", r"\b1r\s+d'ESO\b", r"(?<![/\w])1eso(?![/\w])", r"\bprimer\s+d'ESO\b", r"\bde 1r\b",
    r"4t ESO", r"(?<![/\w])4eso(?![/\w])", r"4t d'ESO", r"4t A\b", r"\bde 4t\b",
    r"\bSIEI\b", r"\bUSEE\b", r"\bDIL\b", r"\bTEA\b", r"discapacitat", r"autis", r"trastorn", r"s[íi]ndrome",
    r"\bl'alumne\b", r"\bun alumne\b", r"\baquest alumne\b",
    r"\bl'alumna\b", r"\buna alumna\b", r"\baquesta alumna\b",
    r"\bdos alumnes\b", r"\bdues alumnes\b",
]
trobats = []
for f in sorted(glob.glob(ruta('**', '*.*'), recursive=True)):
    if os.path.splitext(f)[1] not in ('.md', '.html', '.js', '.css', '.json', '.txt') or f.endswith('OFL.txt'):
        continue
    text = llegeix(f)
    for patro in PROHIBITS:
        for m in re.finditer(patro, text, re.I):
            trobats.append((rel(f), m.group(0)))
comprova(not trobats, f"termes que trenquen l'anonimat: {trobats[:6]}")
print(f"  termes que trencarien l'anonimat: {len(trobats)}")

# --------------------------------------------------------------------------
print("\nDEPENDÈNCIES EXTERNES")
# Ni CDN ni lletres de Google: el filtre del centre no ho pot trencar, i
# funciona sense xarxa.
# --------------------------------------------------------------------------
remots = []
for f in glob.glob(ruta('**', '*.html'), recursive=True) + fulls:
    text = llegeix(f)
    remots += [(rel(f), u) for u in re.findall(r'(?:src|href)="(https?://[^"]+)"', text)]
    remots += [(rel(f), u) for u in re.findall(r'url\(\s*["\']?(https?://[^"\')]+)', text)]
comprova(not remots, f"recursos remots: {remots}")
print(f"  recursos remots: {len(remots)}")

# --------------------------------------------------------------------------
print("\nDADES")
# dades/unitats.js és el que llegeix index.html. Ha de quadrar amb el disc.
# --------------------------------------------------------------------------
dades = llegeix(ruta('dades', 'unitats.js'))
nums = [int(n) for n in re.findall(r'\bnum:\s*(\d+)', dades)]
comprova(nums == list(range(1, len(nums) + 1)), f"dades/unitats.js: les unitats no van seguides ({nums})")
fitxes_dades = re.findall(r'fitxa:\s*"([^"]+)"', dades)
for u in fitxes_dades:
    comprova(os.path.exists(ruta(u)), f"dades/unitats.js apunta a {u}, que no existeix")
for f in FITXES:
    comprova(rel(f) in fitxes_dades, f"{rel(f)} no surt a dades/unitats.js")
fitxers_t = re.findall(r'fitxer:\s*"([^"]+)"', dades)
pdfs_t = re.findall(r'pdf:\s*"([^"]+)"', dades)
for u in fitxers_t + pdfs_t:
    comprova(os.path.exists(ruta(u)), f"dades/unitats.js apunta a {u}, que no existeix")
for f in TARGETES:
    comprova(rel(f) in fitxers_t, f"{rel(f)} no surt a dades/unitats.js")
print(f"  unitats: {len(nums)} · amb fitxa: {len(fitxes_dades)} · targetes: {len(fitxers_t)}")

# --------------------------------------------------------------------------
print()
if avisos:
    print(f"{len(avisos)} AVISOS (no aturen res, però cal mirar-los):")
    for a in avisos:
        print("  ·", a)
    print()
if falles:
    print(f"{len(falles)} PROBLEMES:")
    for f in falles:
        print("  ·", f)
    sys.exit(1)
print("Tot correcte.")
