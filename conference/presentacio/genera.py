"""Fabrica la presentació a partir de conference/diapositives.txt.

    python3 conference/presentacio/genera.py

Escriu conference/presentacio/Conferencia-ABEAM-2026.pptx, que es pot pujar a Google Drive
i obrir amb Google Slides. Les regles per escriure el txt són a LLEGEIX-ME.txt.

Cada diapositiva del txt es converteix en una sèrie de diapositives, com un JPG animat:
la primera només té el títol, i cada una de les següents hi afegeix un pas.
"""
import math
import re
import sys
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

AQUI = Path(__file__).resolve().parent
CONF = AQUI.parent
REC = AQUI / "recursos"
TXT = CONF / "diapositives.txt"
SORTIDA = AQUI / "Conferencia-ABEAM-2026.pptx"

# Pocs colors: negre, gris fosc i lila. Blau només per als enllaços.
NEGRE = RGBColor(0x00, 0x00, 0x00)
TEXT = RGBColor(0x23, 0x39, 0x3A)
GRIS = RGBColor(0x66, 0x66, 0x66)
VORA = RGBColor(0x8A, 0x9A, 0x9B)
LILA = RGBColor(0x6B, 0x4F, 0xBB)
PLAFO = RGBColor(0xEF, 0xE8, 0xFF)
BLAU = RGBColor(0x00, 0x00, 0xFF)
TITOL_PORTADA = BLAU

LLETRA = "Arial"
LEMA = "Matemàtiques per a tothom"
FIGURES = [f"figura-{i}.png" for i in range(1, 9)]

# Mides en polzades (diapositiva de 16:9)
AMPLE, ALT = 10.0, 5.625
PLAFO_X, PLAFO_Y, PLAFO_W, PLAFO_H = 1.15, 0.8, 8.55, 4.6
COS_X, COS_W = 1.45, 7.95
TITOL_Y = 0.95
FONS_COS = 5.25          # on acaba el contingut, a dins del plafó
MARGE_IMATGE = 0.15     # marge al voltant d'una imatge a pantalla completa
MIDA_TITOL, MIDA_COS = 24, 24

ENLLAC = re.compile(r"\[([^\]]+)\]\(([^\s)]+)\)")


# ----------------------------------------------------------------------------
# Lectura del txt
# ----------------------------------------------------------------------------

def llegeix(txt):
    """Retorna la portada (o None) i la llista de diapositives."""
    linies = txt.splitlines()
    blocs, actual = [], None
    i = 0
    while i < len(linies):
        if linies[i].startswith("====") and i + 2 < len(linies) and linies[i + 2].startswith("===="):
            actual = {"capcalera": linies[i + 1].strip(), "linies": []}
            blocs.append(actual)
            i += 3
            continue
        if actual is not None:
            actual["linies"].append(linies[i])
        i += 1

    portada, diapositives = None, []
    for b in blocs:
        seccions = seccions_de(b["linies"])
        if b["capcalera"] == "PORTADA":
            portada = {k: [l for l in v if l] for k, v in seccions.items()}
        elif b["capcalera"].startswith("DIAPOSITIVA"):
            m = re.search(r"·\s*(.+)$", b["capcalera"])
            seccions["minut"] = m.group(1).strip() if m else ""
            diapositives.append(seccions)
    return portada, diapositives


def seccions_de(linies):
    """Agrupa les línies sota les etiquetes en majúscules (PANTALLA, IMATGE, DIC…).

    Es conserven les línies en blanc de dins de cada secció: separen els passos.
    """
    seccions, clau = {}, None
    for l in linies:
        if re.fullmatch(r"[A-ZÀÈÉÍÒÓÚÇ]+", l.strip()):
            clau = l.strip()
            seccions[clau] = []
        elif clau:
            seccions[clau].append(l.rstrip())
    for clau, ls in seccions.items():
        while ls and not ls[0]:
            ls.pop(0)
        while ls and not ls[-1]:
            ls.pop()
    return seccions


def grups(linies):
    """Separa les línies en grups per les línies en blanc."""
    sortida = [[]]
    for l in linies:
        if l.strip():
            sortida[-1].append(l)
        elif sortida[-1]:
            sortida.append([])
    return [g for g in sortida if g]


def paragrafs(linies):
    """Converteix les línies d'un pas en paràgrafs.

    Cada paràgraf és [tipus, [línies]]: «punt» per a les línies que comencen amb «- »,
    «num» per a les que comencen amb «1. », «2. »…, i «text» per a la resta.
    Una línia sagnada continua el paràgraf anterior en una línia nova.
    """
    sortida = []
    for l in linies:
        if l.startswith("- "):
            sortida.append(["punt", [l[2:].strip()]])
        elif re.match(r"\d+\. ", l):
            sortida.append(["num", [l.strip()]])
        elif l.startswith(" ") and sortida:
            sortida[-1][1].append(l.strip())
        else:
            sortida.append(["text", [l.strip()]])
    return sortida


def imatges_de(linies):
    """Els grups d'imatges (un per pas) i el text de IMATGE que no és cap ruta."""
    passos, resta = [], []
    for g in grups(linies):
        rutes = []
        for l in g:
            trobades = re.findall(r"(\S+\.(?:png|jpe?g))\b", l, re.I)
            for r in trobades:
                p = CONF / r
                if p.exists():
                    rutes.append(p)
                else:
                    print(f"  Atenció: no trobo la imatge {r}", file=sys.stderr)
            if not trobades:
                resta.append(l.strip())
        if rutes:
            passos.append(rutes)
    return passos, resta


# ----------------------------------------------------------------------------
# Peces de la diapositiva
# ----------------------------------------------------------------------------

def caixa_text(diapo, x, y, w, h, ancoratge=MSO_ANCHOR.TOP):
    tb = diapo.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = ancoratge
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    return tf


def escriu(p, text, mida, color=TEXT, negreta=False, cursiva=False):
    """Escriu el text. Els enllaços [text](adreça) surten en blau i subratllats."""
    pos = 0
    for m in list(ENLLAC.finditer(text)) + [None]:
        tros = text[pos:m.start()] if m else text[pos:]
        if tros:
            _run(p, tros, mida, color, negreta, cursiva)
        if m:
            r = _run(p, m.group(1), mida, BLAU, negreta, cursiva)
            r.font.underline = True
            r.hyperlink.address = m.group(2)
            pos = m.end()


def _run(p, text, mida, color, negreta, cursiva):
    r = p.add_run()
    r.text = text
    f = r.font
    f.name, f.size, f.bold, f.italic = LLETRA, Pt(mida), negreta, cursiva
    f.color.rgb = color
    return r


def sense_enllacos(text):
    return ENLLAC.sub(r"\1", text)


def vinyeta(p, tipus, mida):
    pPr = p._p.get_or_add_pPr()
    if tipus == "num":
        sagnat = int(Pt(mida) * 1.4)
        pPr.set("marL", str(sagnat))
        pPr.set("indent", str(-sagnat))
        pPr.append(pPr.makeelement(qn("a:buNone"), {}))
    elif tipus == "punt":
        sagnat = int(Pt(mida) * 1.1)
        pPr.set("marL", str(sagnat))
        pPr.set("indent", str(-sagnat))
        buclr = pPr.makeelement(qn("a:buClr"), {})
        buclr.append(buclr.makeelement(qn("a:srgbClr"), {"val": str(LILA)}))
        pPr.append(buclr)
        pPr.append(pPr.makeelement(qn("a:buFont"), {"typeface": LLETRA}))
        pPr.append(pPr.makeelement(qn("a:buChar"), {"char": "•"}))
    else:
        pPr.set("marL", "0")
        pPr.set("indent", "0")
        pPr.append(pPr.makeelement(qn("a:buNone"), {}))


def linies_necessaries(text, ample, mida):
    caracters = max(8, int(ample * 72 / (mida * 0.5)))
    return max(1, math.ceil(len(sense_enllacos(text)) / caracters))


def mida_que_hi_cap(pars, ample, alt):
    """La lletra més gran (de 24 a 14 pt) amb què tot el text cap a la caixa."""
    for mida in (MIDA_COS, 22, 20, 18, 17, 16, 15, 14):
        linies = 0
        for tipus, ls in pars:
            sagnat = {"punt": 1.1, "num": 1.4}.get(tipus, 0) * mida / 72
            linies += sum(linies_necessaries(l, ample - sagnat, mida) for l in ls)
        alçada = linies * mida * 1.2 / 72 + len(pars) * mida * 0.4 / 72
        if alçada <= alt:
            return mida
    return 14


def posa_cos(diapo, pars, visibles, x, y, w, h, mida):
    """Escriu els primers «visibles» paràgrafs. La caixa és la mateixa a tots els passos."""
    if not visibles:
        return
    tf = caixa_text(diapo, x, y, w, h)
    hi_ha_punts = False
    for k, (tipus, ls) in enumerate(pars[:visibles]):
        p = tf.paragraphs[0] if k == 0 else tf.add_paragraph()
        p.space_after = Pt(mida * 0.4)
        p.line_spacing = 1.05
        # Una frase sense guió, després d'una llista, és la idea que es vol remarcar
        destacat = tipus == "text" and hi_ha_punts and not any(ENLLAC.search(l) for l in ls)
        hi_ha_punts = hi_ha_punts or tipus == "punt"
        vinyeta(p, tipus, mida)
        for j, l in enumerate(ls):
            if j:
                p.add_line_break()
            escriu(p, l, mida, LILA if destacat else TEXT, negreta=destacat)


def disposicio_imatges(rutes, x, y, w, h):
    """On va cada imatge: la graella que les fa més grans, alineada a dalt."""
    mides = [Image.open(r).size for r in rutes]
    n = len(rutes)
    millor = None
    for cols in range(1, n + 1):
        files = math.ceil(n / cols)
        cw = (w - 0.15 * (cols - 1)) / cols
        ch = (h - 0.15 * (files - 1)) / files
        area = sum(min(cw / iw, ch / ih) ** 2 * iw * ih for iw, ih in mides)
        if millor is None or area > millor[0]:
            millor = (area, cols, cw, ch)
    _, cols, cw, ch = millor
    llocs = []
    for k, (iw, ih) in enumerate(mides):
        f, c = divmod(k, cols)
        esc = min(cw / iw, ch / ih)
        pw, ph = iw * esc, ih * esc
        llocs.append((x + c * (cw + 0.15) + (cw - pw) / 2, y + f * (ch + 0.15), pw, ph))
    return llocs


def posa_imatge(diapo, ruta, lloc, vora=True):
    px, py, pw, ph = lloc
    pic = diapo.shapes.add_picture(str(ruta), Inches(px), Inches(py), Inches(pw), Inches(ph))
    if vora:
        pic.line.color.rgb = VORA
        pic.line.width = Pt(0.75)


def posa_imatge_ajustada(diapo, ruta, x, y, w, h, ancoratge="centre"):
    iw, ih = Image.open(ruta).size
    esc = min(w / iw, h / ih)
    pw, ph = iw * esc, ih * esc
    py = y + (h - ph) if ancoratge == "baix" else y + (h - ph) / 2
    posa_imatge(diapo, ruta, (x + (w - pw) / 2, py, pw, ph), vora=False)


def marc(diapo, numero):
    """El que comparteixen totes les diapositives de contingut: lema, logo, figura i plafó."""
    tf = caixa_text(diapo, PLAFO_X, 0.2, 5.0, 0.45, MSO_ANCHOR.MIDDLE)
    escriu(tf.paragraphs[0], LEMA, 16, GRIS, cursiva=True)
    posa_imatge_ajustada(diapo, REC / "abeam.png", 8.45, 0.12, 1.25, 0.55)
    posa_imatge_ajustada(diapo, REC / FIGURES[numero % len(FIGURES)], 0.1, 2.6, 0.95, 2.8, "baix")
    pl = diapo.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(PLAFO_X), Inches(PLAFO_Y),
                                Inches(PLAFO_W), Inches(PLAFO_H))
    pl.adjustments[0] = 0.06
    pl.fill.solid()
    pl.fill.fore_color.rgb = PLAFO
    pl.line.fill.background()
    pl.shadow.inherit = False


def notes(diapo, text):
    diapo.notes_slide.notes_text_frame.text = text


# ----------------------------------------------------------------------------
# Diapositives
# ----------------------------------------------------------------------------

def fes_portada(prs, portada):
    d = prs.slides.add_slide(prs.slide_layouts[6])
    jornada = portada.get("JORNADA", [])
    titol = " ".join(portada.get("TÍTOL", []))
    autor = portada.get("AUTOR", [])

    tf = caixa_text(d, 0.6, 0.45, 6.4, 0.95)
    for k, l in enumerate(jornada):
        p = tf.paragraphs[0] if k == 0 else tf.add_paragraph()
        p.space_after = Pt(4)
        if k == 0:
            escriu(p, l, 20, NEGRE, negreta=True)
        elif re.search(r"\d{4}$", l):
            escriu(p, l, 14, NEGRE)
        else:
            escriu(p, l, 16, NEGRE, cursiva=True)

    tf = caixa_text(d, 0.6, 1.95, 7.0, 0.9)
    escriu(tf.paragraphs[0], titol, 28, TITOL_PORTADA)

    tf = caixa_text(d, 0.6, 2.97, 4.4, 1.6)
    for k, l in enumerate(autor):
        p = tf.paragraphs[0] if k == 0 else tf.add_paragraph()
        p.space_after = Pt(2)
        if k == 0:
            escriu(p, l, 16, TEXT, negreta=True)
            p.space_after = Pt(16)
        else:
            escriu(p, l, 13, TEXT)

    posa_imatge_ajustada(d, REC / "abeam.png", 7.79, 0.36, 1.9, 0.83)
    posa_imatge_ajustada(d, REC / "portada.png", 8.27, 1.35, 1.42, 3.89)
    notes(d, "Portada. Presenta't en una frase i passa a la diapositiva 1.")


def es_ruta_imatge(linia):
    return re.fullmatch(r"\S+\.(?:png|jpe?g)", linia.strip(), re.I) is not None


def rutes_de(grup):
    rutes = []
    for l in grup:
        p = CONF / l.strip()
        if p.exists():
            rutes.append(p)
        else:
            print(f"  Atenció: no trobo la imatge {l.strip()}", file=sys.stderr)
    return rutes


def fes_imatge(prs, rutes, text_notes):
    """Una diapositiva només amb la imatge (o les imatges), tan grans com es pugui."""
    d = prs.slides.add_slide(prs.slide_layouts[6])
    x, y, w, h = MARGE_IMATGE, MARGE_IMATGE, AMPLE - 2 * MARGE_IMATGE, ALT - 2 * MARGE_IMATGE
    llocs = disposicio_imatges(rutes, x, y, w, h)
    if len({round(py, 3) for _, py, _, _ in llocs}) == 1:
        # Totes en una fila: juntes, centrades a la diapositiva
        ample_total = sum(pw for _, _, pw, _ in llocs) + 0.15 * (len(llocs) - 1)
        px = x + (w - ample_total) / 2
        for r, (_, _, pw, ph) in zip(rutes, llocs):
            posa_imatge(d, r, (px, y + (h - ph) / 2, pw, ph))
            px += pw + 0.15
    else:
        baix = max(py + ph for _, py, _, ph in llocs)
        despl = (y + h - baix) / 2
        for r, (px, py, pw, ph) in zip(rutes, llocs):
            posa_imatge(d, r, (px, py + despl, pw, ph))
    notes(d, text_notes)


def fes_diapositiva(prs, numero, s):
    """Una diapositiva del txt: tantes diapositives com passos.

    Els passos són el títol, cada grup de línies de PANTALLA i cada imatge. Una imatge
    ocupa tota la diapositiva; després, el text continua on s'havia quedat.
    """
    linies = s.get("PANTALLA", [])
    titol = linies[0].strip().rstrip(".") if linies else ""
    imatges_antigues, resta = imatges_de(s.get("IMATGE", []))
    passos = [("imatge", g) for g in imatges_antigues]
    for g in grups(linies[1:]):
        if all(es_ruta_imatge(l) for l in g):
            rutes = rutes_de(g)
            if rutes:
                passos.append(("imatge", rutes))
        else:
            passos.append(("text", paragrafs(g)))
    tots = [p for tipus, b in passos if tipus == "text" for p in b]

    # La disposició del text es calcula una vegada, amb tot el text, perquè no es mogui res
    mida_titol = MIDA_TITOL
    dues = linies_necessaries(titol, COS_W, mida_titol) > 1
    alt_titol = 0.67 if dues else 0.45
    cos_y = TITOL_Y + alt_titol + 0.2
    cos_h = FONS_COS - cos_y
    text_x, text_w = COS_X + 0.4, COS_W - 0.8
    mida = mida_que_hi_cap(tots, text_w, cos_h)

    dic = []
    for l in s.get("DIC", []):
        if l.startswith("- ") or not dic:
            dic.append(l.lstrip("- ").strip())
        elif l.strip():
            dic[-1] += " " + l.strip()
    resta = [l for l in resta if l.lower() not in ("cap.", "cap")]

    total = 1 + len(passos)

    def text_notes(pas):
        ls = [f"Minut {s['minut']} · pas {pas} de {total}", ""]
        ls += [f"• {l}" for l in dic]
        if resta:
            ls += ["", "Imatge o demostració:"] + resta
        return "\n".join(ls)

    def fes_text(visibles, pas):
        d = prs.slides.add_slide(prs.slide_layouts[6])
        marc(d, numero)
        tf = caixa_text(d, COS_X, TITOL_Y, COS_W, alt_titol, MSO_ANCHOR.MIDDLE)
        tf.paragraphs[0].alignment = PP_ALIGN.CENTER
        escriu(tf.paragraphs[0], titol, mida_titol, NEGRE, negreta=True)
        posa_cos(d, tots, visibles, text_x, cos_y, text_w, cos_h, mida)
        notes(d, text_notes(pas))

    visibles = 0
    fes_text(visibles, 1)
    for k, (tipus, contingut) in enumerate(passos, start=2):
        if tipus == "imatge":
            fes_imatge(prs, contingut, text_notes(k))
        else:
            visibles += len(contingut)
            fes_text(visibles, k)


def main():
    portada, diapositives = llegeix(TXT.read_text(encoding="utf-8"))
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(AMPLE), Inches(ALT)
    if portada:
        fes_portada(prs, portada)
    for n, s in enumerate(diapositives, start=1):
        fes_diapositiva(prs, n, s)
    prs.save(SORTIDA)
    print(f"Fet: {SORTIDA.relative_to(CONF.parent)} ({len(prs.slides)} diapositives)")


if __name__ == "__main__":
    main()
