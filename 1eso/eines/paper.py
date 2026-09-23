"""La maquinària comuna del paper: la fan servir mesura.py, gen_pdf.py i comprova.py.

Abans, mesura.py i gen_pdf.py duien cadascun la seva còpia del full d'estil
dels PDF. Si una canviava i l'altra no, la mesura deixava de dir la veritat.
Aquí n'hi ha una de sola.

Aquest fitxer només importa la biblioteca estàndard: comprova.py el pot fer
servir sense WeasyPrint. WeasyPrint es carrega a dins de les funcions que el
necessiten.
"""
import hashlib, os, re

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # 1eso/
UTIL_CM = 29.7 - 2.6        # alçada útil d'un A4 amb marges d'1,3 cm

# El full d'estil dels PDF. Fixa la geometria de la pàgina amb @page i treu el
# padding de .full, que a pantalla fa de marge del full i en PDF el duplicaria.
# El cos de 14 pt NO es toca: si una pàgina no cap, s'arregla la pàgina.
# La lletra NO es fixa aquí: surt de tokens.css, igual que a la pantalla.
FULL_PDF = """
@page { size: A4; margin: 1.3cm 1.4cm; }
.full { min-height: 0 !important; max-width: none !important;
        padding: 0 !important; margin: 0 !important; display: block !important;
        break-after: page; page-break-after: always; }
.full:last-child { break-after: auto; page-break-after: auto; }
.no-imprimir { display: none !important; }
"""

# Per mesurar: la mateixa geometria, però en una pàgina de dos metres d'alt.
FULL_ALT = FULL_PDF.replace("size: A4;", "size: 21cm 200cm;")

# Tot el que decideix com surt un PDF. Si en canvia qualsevol, el PDF que hi
# ha al repositori ja no és el que sortiria ara: comprova.py ho detecta.
DEPENDENCIES = ["css/tokens.css", "css/fitxa.css", "fonts/Caveat.ttf", "eines/paper.py"]


def blocs(html):
    """Separa la capçalera i els blocs .full d'una pàgina HTML.

    Torna (capçalera, [blocs de l'alumnat], [blocs del solucionari]).
    Cada bloc comença amb <div class="full..."> i acaba amb un </div> a
    principi de línia: els </div> de dins han d'anar sagnats.
    """
    cap = html[:html.index("<body>") + 6]
    fulls = re.findall(r'<div class="full[^"]*">.*?\n</div>', html, re.S)
    alumnat = [f for f in fulls if not re.match(r'<div class="full[^"]*\bsol\b', f)]
    solucionari = [f for f in fulls if re.match(r'<div class="full[^"]*\bsol\b', f)]
    return cap, alumnat, solucionari


def empremta(font_rel):
    """SHA-256 de la font HTML i de tot el que decideix com surt el PDF.

    Els salts de línia es normalitzen: un checkout a Windows no ha de fer
    creure que el PDF està desactualitzat.
    """
    h = hashlib.sha256()
    for rel in [font_rel] + DEPENDENCIES:
        with open(os.path.join(ARREL, rel), "rb") as f:
            dades = f.read()
        if not rel.endswith(".ttf"):
            dades = dades.replace(b"\r\n", b"\n")
        h.update(rel.encode() + b"\0" + dades + b"\0")
    return h.hexdigest()


def document(cap, fulls, carpeta):
    """Renderitza uns blocs amb el full d'estil dels PDF. Necessita WeasyPrint."""
    from weasyprint import HTML, CSS
    html = cap + "\n".join(fulls) + "</body></html>"
    return HTML(string=html, base_url=carpeta + "/").render(stylesheets=[CSS(string=FULL_PDF)])


def alcada_cm(cap, full, carpeta):
    """Alçada del contingut d'un bloc .full, en cm, sense els marges de la pàgina."""
    from weasyprint import HTML, CSS
    doc = HTML(string=cap + full + "</body></html>", base_url=carpeta + "/").render(
        stylesheets=[CSS(string=FULL_ALT)])

    def fons(caixa, m=0.0):
        if getattr(caixa, "element_tag", None) not in (None, "html"):
            m = max(m, caixa.position_y + caixa.height)
        for fill in getattr(caixa, "children", []):
            m = fons(fill, m)
        return m
    return fons(doc.pages[0]._page_box) / 96 * 2.54 - 1.3


def lletres_del_pdf(cami):
    """Noms de les lletres incrustades en un PDF.

    Els diccionaris de les lletres poden anar dins de fluxos comprimits, i per
    això es busquen als bytes i a cada flux descomprimit. Només biblioteca
    estàndard: el nom surt amb un prefix de subconjunt, /ABCDEF+Caveat.
    """
    import zlib
    with open(cami, "rb") as f:
        dades = f.read()
    trossos = [dades]
    for m in re.finditer(rb"stream\r?\n", dades):
        fi = dades.find(b"endstream", m.end())
        try:
            trossos.append(zlib.decompress(dades[m.end():fi]))
        except zlib.error:
            pass
    noms = set()
    for tros in trossos:
        noms |= {n.decode("latin-1") for n in re.findall(rb"/BaseFont\s*/[A-Z]{6}\+([\w-]+)", tros)}
    return sorted(noms)
