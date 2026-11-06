"""Quadern d'activitats de la Unitat 4 · Equacions de 2n grau.

    python3 4eso/generadors/gen_quadern.py 4        (des de l'arrel)

Un bloc per cada exercici de la fitxa (u4/fitxa.html), en el mateix ordre. A cada bloc, una
activitat germana i una de repte. Cada activitat té 13 apartats: l'a), resolt, i 12 per fer.
El filtre en deixa 3 (petit), 6 (mitjà) o tots 12 (elevat), sempre els primers: per això
els apartats van de menys a més.

Com a la fitxa, no s'aïlla mai la incògnita ni hi ha la fórmula general: la balança, comprovar
(substituir i mirar), l'arrel quadrada de la calculadora i, sobretot, decidir quina solució té
sentit. Els números es calculen aquí, no s'escriuen a mà: així el solucionari no es pot equivocar.

La regla trencada de la unitat (el negatiu de vegades és el bo: el congelador) surt ja entre els
tres primers apartats dels blocs 5 i 7, perquè també hi sigui amb la quantitat petita.
"""
import math

from quadern import act, taula, tria, nota, num
from peces import balances

NUM = 4
TITOL = "Equacions de 2n grau"   # el de dades/unitats.js (decisió V2)
AVALUAR = ("Com a la fitxa, no es demana aïllar ni la fórmula general: el que s'avalua és comprovar "
           "(substituir i comparar les dues bandes), resoldre x² = k amb la calculadora i, sobretot, "
           "decidir quina de les dues solucions té sentit. El bloc 5 i el 7 són l'evidència del fil de la "
           "SA. Un error de calculadora no hauria de fer baixar la valoració si el camí és bo. Les "
           "activitats de repte compten per als nivells alts (AN, AE), no per al mínim.")

M = "−"   # el signe menys tipogràfic, com a la fitxa


def neg(v):
    """Un enter amb el signe menys de la fitxa: −3."""
    return f"{M}{num(-v)}" if v < 0 else num(v)


# ------------------------------------------------- 1 · la balança --

bloc1 = dict(
    titol="La balança", mira=(1, 5),
    nota_sol="Si en treus d'una banda, n'has de treure de l'altra. <b>Error típic:</b> treure els daus "
             "només d'un costat i escriure x = 8 a «x + 3 = 8». Si passa, que ho faci amb objectes "
             "damunt la taula abans de tornar al paper.",
    acts=[
        act("Mira la balança i escriu quant val la x.", [
            balances([(1, a, b) for a, b in ((2, 6), (3, 8), (1, 5), (4, 7), (2, 9), (5, 10), (3, 11),
                                             (6, 12), (1, 9), (4, 12), (5, 8), (7, 11), (2, 12))])]),
        act("Les bosses pesen igual. Escriu quant val la x.", [
            balances([(2, 0, 8), (2, 0, 6), (3, 0, 9), (2, 0, 10), (3, 0, 12), (4, 0, 8), (2, 2, 8),
                      (2, 1, 7), (3, 3, 9), (2, 4, 10), (3, 0, 6), (2, 3, 11), (4, 0, 12)])],
            repte=True,
            nota_sol="Com l'apartat c de la fitxa: quan hi ha més d'una bossa, els daus es reparteixen "
                     "entre les bosses. Als últims, primer es treuen els daus de cada banda i després es "
                     "reparteix (2x + 2 = 8 → 2x = 6 → x = 3). Si es bloqueja, que ho faci amb objectes."),
    ])


# ------------------------------------------------- 2 · comprovar un número --

def prova(eq, f, dreta, x):
    """Una fila de comprovar: l'equació, el número, la banda esquerra (el compte i el resultat),
    la dreta i si funciona."""
    compte, val = f(x)
    return [eq, f"x = {neg(x)}", f"{compte} = {neg(val)}", neg(dreta), "sí" if val == dreta else "no"]


def mes(a):
    return lambda x: (f"{neg(x)} + {a}", x + a)


def menys(a):
    return lambda x: (f"{neg(x)} {M} {a}", x - a)


def per(k):
    return lambda x: (f"{k} × {neg(x)}", k * x)


CAP2 = ["Equació", "Provo", "Banda esquerra", "Banda dreta", "Funciona?"]
A2 = [22, 14, 22, 15, 15]

bloc2 = dict(
    titol="Comprovar un número", mira=(2, 6),
    nota_sol="Comprovar és substituir i comparar: no cal aïllar res. <b>Error típic:</b> amb «2x», "
             "escriure 2 i el número enganxats (24 en lloc de 2 × 4). Que digui «2 vegades el 4».",
    acts=[
        act("Comprova si el número és la solució.", [
            taula(CAP2, [prova(*r) for r in (
                ("x + 3 = 7", mes(3), 7, 4),
                ("x + 4 = 10", mes(4), 10, 5), ("x + 4 = 10", mes(4), 10, 6), ("3x = 12", per(3), 12, 3),
                ("3x = 12", per(3), 12, 4), (f"x {M} 4 = 6", menys(4), 6, 10), ("2x = 14", per(2), 14, 6),
                ("x + 8 = 15", mes(8), 15, 7), (f"x {M} 2 = 9", menys(2), 9, 7), ("4x = 20", per(4), 20, 5),
                ("5x = 30", per(5), 30, 5), (f"x {M} 6 = 3", menys(6), 3, 9), ("2x = 18", per(2), 18, 8))],
                  omplir=(2, 3, 4), amples=A2)], ico="calc"),
        act("Comprova si el número és la solució. Hi ha x a les dues bandes.", [
            taula(CAP2, [[eq, f"x = {x}", f"{fe(x)[0]} = {fe(x)[1]}", f"{fd(x)[0]} = {fd(x)[1]}",
                          "sí" if fe(x)[1] == fd(x)[1] else "no"]
                         for eq, fe, fd, x in (
                ("2x + 1 = x + 4", lambda x: (f"2 × {x} + 1", 2 * x + 1), mes(4), 3),
                ("2x + 3 = x + 5", lambda x: (f"2 × {x} + 3", 2 * x + 3), mes(5), 2),
                ("2x + 3 = x + 5", lambda x: (f"2 × {x} + 3", 2 * x + 3), mes(5), 3),
                ("3x = x + 8", per(3), mes(8), 4),
                ("3x = x + 8", per(3), mes(8), 2),
                ("2x + 2 = x + 7", lambda x: (f"2 × {x} + 2", 2 * x + 2), mes(7), 5),
                ("4x = 2x + 6", per(4), lambda x: (f"2 × {x} + 6", 2 * x + 6), 3),
                ("3x + 1 = x + 9", lambda x: (f"3 × {x} + 1", 3 * x + 1), mes(9), 3),
                ("3x + 1 = x + 9", lambda x: (f"3 × {x} + 1", 3 * x + 1), mes(9), 4),
                ("5x = 2x + 12", per(5), lambda x: (f"2 × {x} + 12", 2 * x + 12), 4),
                ("2x + 6 = 4x", lambda x: (f"2 × {x} + 6", 2 * x + 6), per(4), 2),
                ("3x + 2 = 2x + 7", lambda x: (f"3 × {x} + 2", 3 * x + 2), lambda x: (f"2 × {x} + 7", 2 * x + 7), 5),
                ("3x + 2 = 2x + 7", lambda x: (f"3 × {x} + 2", 3 * x + 2), lambda x: (f"2 × {x} + 7", 2 * x + 7), 6))],
                  omplir=(2, 3, 4), amples=A2)], ico="calc", repte=True,
            nota_sol="Un pas més: ara la banda dreta també s'ha de calcular. El camí és el mateix: posar el "
                     "número a les dues x i mirar si surt igual. Ningú no ha d'aïllar la x."),
    ])


# ------------------------------------------------- 3 · l'arrel quadrada --

def arrel(k):
    """La x de x² = k, i com s'escriu: exacta, o arrodonida a 2 decimals."""
    r = math.sqrt(k)
    if r == int(r):
        return num(int(r)), num(int(r))
    return num(round(r, 2)), f"{num(int(r * 1e6) / 1e6)}… → {num(round(r, 2))}"


def fila_arrel(k):
    curt, llarg = arrel(k)
    return [f"x² = {num(k)}", f"√{num(k)}", curt], llarg


CAP3 = ["Equació", "A la calculadora", "x val"]

QUADRATS3 = (36, 25, 64, 81, 16, 121, 40, 9, 144, 30, 50, 10, 200)
bloc3 = dict(
    titol="Amb l'arrel quadrada", mira=(3, 6),
    nota_sol="L'arrel quadrada de la calculadora fa tota la feina. Quan l'arrel no s'acaba (com l'apartat d "
             "de la fitxa), s'arrodoneix a 2 decimals: és la decisió de la Unitat 1. En aquest bloc només es "
             "demana el número positiu; el negatiu surt al bloc 5.",
    acts=[
        act("Resol amb l'arrel quadrada de la calculadora.", [
            taula(CAP3, [fila_arrel(k)[0] for k in QUADRATS3], omplir=(1, 2), amples=[30, 30, 28],
                  abans=nota("Si l'arrel no s'acaba, arrodoneix a 2 decimals."),
                  sol_nota="Les que no s'acaben: " + " · ".join(
                      f"√{num(k)} = {fila_arrel(k)[1]}" for k in QUADRATS3 if "…" in fila_arrel(k)[1]) + ".")],
            ico="calc"),
        act("Deixa la x² sola i després fes l'arrel quadrada.", [
            taula(["Equació", "x² =", "A la calculadora", "x val"],
                  [[f"x² + {a} = {b}", num(b - a), f"√{num(b - a)}", arrel(b - a)[0]]
                   for a, b in ((4, 29), (1, 50), (10, 74), (6, 22), (19, 100), (36, 100), (11, 47),
                                (5, 14), (21, 121), (3, 147), (20, 30), (50, 150), (15, 64))],
                  omplir=(1, 2, 3), amples=[28, 18, 24, 18],
                  sol_nota=f"L'apartat k no s'acaba: √10 = {arrel(10)[1]}.")],
            ico="calc", repte=True,
            nota_sol="Un pas abans de l'arrel: treure el número que acompanya la x², com a la balança. "
                     "<b>Error típic:</b> fer l'arrel de tot (√29 a l'apartat a). Si passa, que ho comprovi: "
                     "5 × 5 + 4 = 29."),
    ])


# ------------------------------------------------- 4 · l'hort quadrat --

def costat(que, k, u):
    curt, llarg = arrel(k)
    return [que, f"{num(k)} {u}²", f"x² = {num(k)}", f"{curt} {u}"], llarg


HORTS = (("Un hort", 36, "m"), ("Una habitació", 16, "m"), ("Un pati", 100, "m"), ("Una catifa", 4, "m"),
         ("Un camp", 400, "m"), ("Una rajola", 900, "cm"), ("Una plaça", 2500, "m"),
         ("Un tauler d'escacs", 1600, "cm"), ("Un jardí", 225, "m"), ("Una piscina", 144, "m"),
         ("Un hort", 50, "m"), ("Una pista", 625, "m"), ("Un mocador", 30, "cm"))

bloc4 = dict(
    titol="El costat d'un quadrat", mira=(4, 7),
    nota_sol="L'equació sempre té la mateixa forma: x² = l'àrea. El costat és l'arrel, i porta la unitat "
             "sense el quadrat (m² → m). <b>Error típic:</b> dividir l'àrea entre 2 o entre 4.",
    acts=[
        act("Tot és quadrat. Escriu l'equació i troba el costat.", [
            taula(["Què és", "Àrea", "L'equació", "El costat"], [costat(*h)[0] for h in HORTS],
                  omplir=(2, 3), amples=[30, 18, 22, 18], esq=(0,),
                  sol_nota="Els que no s'acaben: " + " · ".join(
                      f"{h[0].lower()} de {num(h[1])} {h[2]}², {costat(*h)[1]} {h[2]}"
                      for h in HORTS if "…" in costat(*h)[1]) + ".")],
            ico="calc"),
        act("Troba el costat de cada hort quadrat i quants metres de tanca calen.", [
            taula(["Àrea", "El costat", "La tanca"],
                  [[f"{num(k)} m²", f"{num(int(math.sqrt(k)))} m", f"{num(4 * int(math.sqrt(k)))} m"]
                   for k in (36, 49, 100, 25, 64, 81, 16, 144, 400, 9, 121, 225, 900)],
                  omplir=(1, 2), amples=[30, 30, 28])],
            ico="calc", repte=True,
            nota_sol="Un pas més: després del costat, la tanca, que són els quatre costats (4 × el costat). "
                     "<b>Error típic:</b> fer 4 × l'àrea. Si passa, que dibuixi l'hort i hi escrigui el "
                     "costat a cada banda."),
    ])


# ------------------------------------------------- 5 · quina solució té sentit --

def sentit(k, que, bona):
    """Un apartat de marcar: x² = k, què és la x, i quina té sentit (1 el positiu, -1 el negatiu,
    0 totes dues)."""
    r = int(math.sqrt(k))
    assert r * r == k
    verb = "són" if que.split()[0] in ("els", "les") else "és"
    return f"x² = {num(k)}. La x {verb} {que}.", bona


def opcions_sentit(apartats, totes=False):
    files = []
    for k, que, bona in apartats:
        text, b = sentit(k, que, bona)
        r = int(math.sqrt(k))
        ops = [f"x = {r}", f"x = {M}{r}"] + (["Totes dues"] if totes else [])
        files.append((text, ops, {1: 0, -1: 1, 0: 2}[b]))
    return files


bloc5 = dict(
    titol="Quina solució té sentit?", mira=(5, 7),
    nota_sol="<b>La regla trencada de la unitat:</b> el negatiu no sempre es descarta. Ja a l'apartat c "
             "(el congelador) la bona és la negativa, perquè també surti a la quantitat petita. Si marca "
             "sempre el positiu sense llegir, és aquí on cal aturar-se: què és la x?",
    acts=[
        act("Marca la solució que té sentit.", [
            tria(opcions_sentit([
                (36, "el costat d'un hort", 1), (25, "l'edat d'un gos", 1),
                (9, "la temperatura d'un congelador", -1), (64, "l'altura d'un arbre, en metres", 1),
                (4, "la planta d'un pàrquing sota terra", -1), (49, "el preu d'una entrada, en euros", 1),
                (100, "la temperatura a l'Antàrtida a l'hivern", -1), (81, "els segons que tarda un ascensor", 1),
                (16, "la llargada d'un cable, en metres", 1), (64, "la temperatura d'una nit de molt fred", -1),
                (25, "les persones que van en un cotxe", 1), (1, "la planta d'un soterrani", -1),
                (144, "els quilòmetres d'una excursió", 1)]), en_linia=True)]),
        act("Marca la solució que té sentit. De vegades en tenen totes dues.", [
            tria(opcions_sentit([
                (4, "una planta d'un edifici amb pisos i soterranis", 0), (9, "els anys d'un cotxe", 1),
                (16, "la temperatura d'un congelador", -1), (1, "el pis on para un ascensor que va del −2 al 6", 0),
                (36, "el costat d'una plaça quadrada", 1), (49, "un nombre enter", 0),
                (81, "les persones d'un autobús", 1), (25, "la temperatura a l'Antàrtida a l'hivern", -1),
                (9, "la planta d'un hotel amb tres soterranis i deu pisos", 0), (64, "l'altura d'un edifici, en metres", 1),
                (400, "un nombre enter", 0), (49, "la temperatura d'un congelador", -1),
                (121, "els jugadors d'un equip de futbol", 1)], totes=True), en_linia=True)],
            repte=True,
            nota_sol="Una decisió nova: de vegades no se'n descarta cap. Un edifici amb soterranis té la planta "
                     "2 i la −2; un nombre enter pot ser positiu o negatiu. <b>Error típic:</b> triar sempre una "
                     "de les dues. Que digui en veu alta si les dues poden passar de debò."),
    ])


# ------------------------------------------------- 6 · comprovar una equació de 2n grau --

def segon(b, c, provats, signe=M):
    """Una taula de comprovar per a x² − bx + c = 0 (signe «−») o x² + bx − c = 0 (signe «+»),
    amb els números `provats`. A la fitxa: x² − 5x + 6 = 0."""
    bx = "x" if b == 1 else f"{b}x"
    if signe == M:
        eq = f"x² {M} {bx} + {c} = 0"
        val = lambda x: x * x - b * x + c                                         # noqa: E731
        expr = lambda x: f"{num(x * x)} {M} {neg(b * x)} + {c}"                   # noqa: E731
    else:
        eq = f"x² + {bx} {M} {c} = 0"
        val = lambda x: x * x + b * x - c                                         # noqa: E731
        expr = lambda x: f"{num(x * x)} + {('(' + neg(b * x) + ')') if b * x < 0 else neg(b * x)} {M} {c}"  # noqa: E731
    files = [[f"x = {neg(x)}", num(x * x), neg(b * x), f"{expr(x)} = {neg(val(x))}", "sí" if val(x) == 0 else "no"]
             for x in provats]
    return eq, ["Provo", "x²", bx, eq[:-4], "És 0?"], files


def taula_segon(b, c, provats, signe=M):
    eq, cap, files = segon(b, c, provats, signe)
    bones = [f[0][4:] for f in files if f[-1] == "sí"]
    return taula(cap, files, omplir=(1, 2, 3, 4), amples=[16, 14, 14, 30, 14],
                 abans=f'    <div class="equacio" style="margin:.4rem 0 .2rem">{eq}</div>\n',
                 sol_nota=f"De {eq}, són solució: {' i '.join(bones)}." if bones else "")


bloc6 = dict(
    titol="Comprovar una equació de 2n grau", mira=(6, 8),
    nota_sol="Com a la fitxa, l'equació de 2n grau entra per la comprovació, no per la resolució. Cada "
             "columna és una sola tecla de calculadora: primer x², després el terme de la x, i al final "
             "el compte sencer. <b>Error típic:</b> fer x² com «x × 2».",
    acts=[
        act("Comprova quins números són solució de cada equació.", [
            taula_segon(7, 12, (3, 4, 2, 5)),
            taula_segon(6, 8, (2, 4, 3)),
            taula_segon(9, 20, (4, 5, 3)),
            taula_segon(10, 21, (3, 7, 5)),
        ], ico="calc"),
        act("Comprova quins números són solució. Ara hi ha números negatius.", [
            taula_segon(1, 6, (2, -3, 3, -2), signe="+"),
            taula_segon(2, 8, (-4, 2, 4), signe="+"),
            taula_segon(3, 10, (-5, 5, 2), signe="+"),
            taula_segon(1, 12, (3, -3, -4), signe="+"),
        ], ico="calc", repte=True,
            nota_sol="Una de les dues solucions és negativa. Amb la calculadora, el número negatiu s'escriu "
                     "entre parèntesis: (−3)² = 9, no −9. <b>Error típic:</b> escriure −3² a la calculadora, que "
                     "dona −9."),
    ])


# ------------------------------------------------- 7 · a la vida de cada dia --

def vida(situacio, k, que, u=""):
    """Una fila: la situació, l'equació, les dues solucions i la que té sentit (que = 1 el
    positiu, -1 el negatiu)."""
    r = int(math.sqrt(k))
    assert r * r == k
    v = r if que == 1 else -r
    return [situacio, f"x² = {num(k)}", f"{num(r)} i {M}{num(r)}", f"{neg(v)}{' ' + u if u else ''}"]


CAP7 = ["Situació", "L'equació", "Solucions", "Té sentit"]
A7 = [48, 15, 13, 12]

bloc7 = dict(
    titol="A la vida de cada dia", mira=(7, 9),
    nota_sol="La matemàtica dona dos números; la situació en tria un. Ja a l'apartat c (el pàrquing) el bo "
             "és el negatiu. <b>Error típic:</b> descartar sempre el negatiu, la regla que es fabrica als "
             "apartats a i b.",
    acts=[
        act("Escriu les dues solucions i la que té sentit.", [
            taula(CAP7, [vida(*v) for v in (
                ("El terra quadrat d'una habitació fa 25 m². La x és el costat.", 25, 1, "m"),
                ("Una pedra cau d'un pont. La x són els segons que tarda.", 4, 1, "s"),
                ("Un pàrquing és sota terra. La x és la planta on pares.", 9, -1),
                ("Una rajola quadrada fa 1 m². La x és el costat.", 1, 1, "m"),
                ("Una nit d'hivern a la muntanya. La x és la temperatura.", 16, -1, "°C"),
                ("Una catifa quadrada fa 9 m². La x és el costat.", 9, 1, "m"),
                ("Un ascensor baixa al soterrani. La x és la planta on para.", 1, -1),
                ("Una plaça quadrada fa 400 m². La x és el costat.", 400, 1, "m"),
                ("Un congelador. La x és la temperatura.", 324, -1, "°C"),
                ("Un quadre quadrat fa 2 500 cm². La x és el costat.", 2500, 1, "cm"),
                ("Una sala quadrada fa 36 m². La x és el costat.", 36, 1, "m"),
                ("Un dia d'hivern a Sibèria. La x és la temperatura.", 900, -1, "°C"),
                ("Un pati quadrat fa 225 m². La x és el costat.", 225, 1, "m"))],
                  omplir=(2, 3), amples=A7, esq=(0,))], ico="calc"),
        act("Escriu l'equació, les dues solucions i la que té sentit.", [
            taula(CAP7, [vida(*v) for v in (
                ("Un hort quadrat fa 49 m². La x és el costat.", 49, 1, "m"),
                ("Una rajola quadrada fa 400 cm². La x és el costat.", 400, 1, "cm"),
                ("Un congelador. La temperatura, multiplicada per ella mateixa, fa 16.", 16, -1, "°C"),
                ("Una catifa quadrada fa 4 m². La x és el costat.", 4, 1, "m"),
                ("Un pàrquing sota terra. La planta, multiplicada per ella mateixa, fa 9.", 9, -1),
                ("Un pati quadrat fa 144 m². La x és el costat.", 144, 1, "m"),
                ("L'edat d'un nen, multiplicada per ella mateixa, fa 64.", 64, 1, "anys"),
                ("Una plaça quadrada fa 900 m². La x és el costat.", 900, 1, "m"),
                ("L'Antàrtida a l'hivern. La temperatura, multiplicada per ella mateixa, fa 400.", 400, -1, "°C"),
                ("Un camp quadrat fa 10 000 m². La x és el costat.", 10000, 1, "m"),
                ("Un quadre quadrat fa 2 500 cm². La x és el costat.", 2500, 1, "cm"),
                ("Una pedra cau. Els segons, multiplicats per ells mateixos, fan 9.", 9, 1, "s"),
                ("Una finestra quadrada fa 1 m². La x és el costat.", 1, 1, "m"))],
                  omplir=(1, 2, 3), amples=A7, esq=(0,))], ico="calc", repte=True,
            nota_sol="Un pas més: l'equació no la dona el paper. Si és un quadrat, x² = l'àrea; si diu "
                     "«multiplicada per ella mateixa», també és x². Després, com sempre, decidir."),
    ])


BLOCS = [bloc1, bloc2, bloc3, bloc4, bloc5, bloc6, bloc7]
