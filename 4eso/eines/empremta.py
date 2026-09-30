"""L'empremta d'un PDF: si encara és el que sortiria ara de la seva font.

Com a 1eso/eines/paper.py (30/9/2026). generadors/gen_pdf.py desa a pdf/empremtes.json,
per a cada PDF, l'SHA-256 de la seva font HTML i de tot el que en decideix l'aspecte:
els dos fulls d'estil, la lletra manuscrita i el full d'estil del PDF (FULL_PDF, que és
dins de gen_pdf.py). eines/comprova.py torna a calcular-la: si no coincideix, el PDF és
vell i cal tornar a passar gen_pdf.py.

Només fa servir la biblioteca estàndard: comprova.py no necessita WeasyPrint.
"""
import hashlib
import os
import re

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEPENDENCIES = ["css/tokens.css", "css/fitxa.css", "fonts/Caveat.ttf"]


def full_pdf():
    """El full d'estil dels PDF, llegit de gen_pdf.py sense importar-lo."""
    font = open(os.path.join(ARREL, "generadors", "gen_pdf.py"), encoding="utf-8").read()
    return re.search(r'FULL_PDF = """(.*?)"""', font, re.S).group(1)


def empremta(font_rel):
    """SHA-256 de la font i de les dependències. Els salts de línia es normalitzen:
    un checkout a Windows no ha de fer creure que el PDF és vell."""
    h = hashlib.sha256()
    for rel in [font_rel] + DEPENDENCIES:
        with open(os.path.join(ARREL, rel), "rb") as f:
            dades = f.read()
        if not rel.endswith(".ttf"):
            dades = dades.replace(b"\r\n", b"\n")
        h.update(rel.encode() + b"\0" + dades + b"\0")
    h.update(b"FULL_PDF\0" + full_pdf().replace("\r\n", "\n").encode())
    return h.hexdigest()
