"""Quadern d'activitats de la Unitat 1 · Nombres naturals.

    python3 1eso/generadors/gen_quadern.py 1        (des de l'arrel)

La unitat té tres fitxes (Rectangles de quadrets, Centenes, desenes i unitats, L'ordre de les
operacions), i el quadern hi fa tres, dos i tres blocs, dels exercicis que en són el nucli i de la
regla trencada de cada fitxa (3² no és 6; «tres-cents cinc» no és 35; 2 + 3 · 4 no és 20). A cada
bloc, una activitat germana i una de repte. Cada activitat té 13 apartats: l'a), resolt, i 12 per
fer. El filtre en deixa 3, 6 o 12, sempre els primers.

Les regles del curs: la targeta de les taules al davant, sense calculadora, nombres de tres
xifres com a molt, «·» per multiplicar i el rectangle de quadrets com a únic dibuix. Els números es
calculen aquí: el solucionari no es pot equivocar.
"""
from quadern import act, taula, tria, nota, ms
from peces import rectangles, nom_nombre

NUM = 1
TITOL = "Nombres naturals"   # el de dades/unitats.js
AVALUAR = ("Sempre amb la targeta al davant. El que s'avalua és dir el que es veu (files i quadrets a cada "
           "fila; quadrats de 100, columnes de 10 i quadrets solts) i seguir l'ordre bo, no la memòria: si "
           "consulta la targeta, està bé. Les activitats de repte compten per als nivells alts (AN, AE), no "
           "per al mínim.")

FR, FN, FO = "Rectangles de quadrets", "Centenes, desenes i unitats", "L'ordre de les operacions"


def p(*f):
    return " · ".join(str(x) for x in f)


# ------------------------------------------------- 1 · el rectangle --

def fila_que_falta(f, total):
    c = total // f
    assert f * c == total and c <= 10
    return [str(f), str(total), str(c), f"{f} · {c} = {total}"]


bloc1 = dict(
    titol="El rectangle de quadrets", mira=(1, 2, FR),
    nota_sol="Primer es diu, després s'escriu: «3 files de 4 quadrets», 3 · 4 = 12. Es dona per bo el rectangle "
             "girat (4 · 3), que té els mateixos quadrets. <b>Error típic:</b> comptar malament els quadrets de "
             "la fila: que els compti amb el dit.",
    acts=[
        act("Mira cada rectangle. Escriu la multiplicació i quants quadrets hi ha.", [
            rectangles([(3, 4), (2, 5), (4, 3), (2, 7), (5, 2), (3, 6), (4, 4), (2, 9), (5, 5), (3, 8), (6, 4),
                        (4, 7), (3, 10)])]),
        act("Saps les files i el total. Quants quadrets hi ha a cada fila?", [
            taula(["Files", "Quadrets en total", "Quadrets a cada fila", "La multiplicació"],
                  [fila_que_falta(*r) for r in ((3, 15), (2, 8), (4, 12), (5, 10), (2, 14), (3, 18), (4, 20),
                                                (5, 30), (6, 24), (3, 27), (7, 28), (8, 40), (9, 36))],
                  omplir=(2, 3), amples=[18, 22, 22, 26], abans=nota("Busca-ho a la targeta de les taules."))],
            repte=True,
            nota_sol="El camí al revés: de les files i el total al rectangle. A la targeta es busca la taula de les "
                     "files fins que surt el total (3 · 5 = 15). Amb miniblocs: fer les files i repartir-hi els "
                     "quadrets."),
    ])


# ------------------------------------------------- 2 · partir pel 10 --

def parteix(f, n):
    deu, petit = f * 10, f * (n - 10)
    assert 10 < n < 20
    return [p(f, n), f"{p(f, 10)} = {deu}", f"{p(f, n - 10)} = {petit}", f"{deu} + {petit} = {deu + petit}"]


def parteix_gran(f, n):
    d, u = divmod(n, 10)
    a, b = f * d * 10, f * u
    return [p(f, n), f"{p(f, d * 10)} = {a}", f"{p(f, u)} = {b}", f"{a} + {b} = {a + b}"]


bloc2 = dict(
    titol="Partir pel 10", mira=(5, 5, FR),
    nota_sol="La targeta arriba fins al 10: el rectangle es parteix en la part de 10 i la part petita, i després "
             "s'ajunten. Les sumes es fan sense portar-ne. Si li costa, que tapi amb la mà la part de 10.",
    acts=[
        act("Parteix pel 10. Després ajunta les dues parts.", [
            taula(["La multiplicació", "La part de 10", "La part petita", "Ajunta-les"],
                  [parteix(*r) for r in ((3, 12), (4, 13), (2, 14), (5, 11), (3, 13), (2, 16), (4, 12), (6, 11),
                                         (3, 15), (2, 18), (5, 13), (4, 14), (3, 17))],
                  omplir=(1, 2, 3), amples=[18, 22, 22, 26])]),
        act("Ara la part gran és de 20, 30 o 40. Parteix i ajunta.", [
            taula(["La multiplicació", "La part gran", "La part petita", "Ajunta-les"],
                  [parteix_gran(*r) for r in ((2, 24), (3, 21), (2, 31), (4, 22), (3, 32), (2, 43), (5, 21),
                                              (2, 34), (3, 23), (4, 21), (2, 42), (3, 31), (5, 41))],
                  omplir=(1, 2, 3), amples=[18, 22, 22, 26],
                  abans=nota("3 · 20 és com 3 · 2, amb un 0 al final: 60."))],
            repte=True,
            nota_sol="Un pas més: la part gran ja no és de 10. 3 · 20 = 60 surt de 3 · 2 = 6 amb un zero, i és a "
                     "la targeta. Totes les sumes es fan sense portar-ne."),
    ])


# ------------------------------------------------- 3 · el quadrat --

def quadrat(text, n, k, es_quadrat):
    """Una tria com la de l'exercici 7: el resultat de n² o de n · k, amb les dues opcions."""
    q, r = n * n, n * k
    assert q != r
    bona = q if es_quadrat else r
    ops = sorted({q, r})
    return (f"{text} =", [str(x) for x in ops], ops.index(bona))


QUADRATS = [quadrat("3²", 3, 2, True), quadrat("4²", 4, 2, True), quadrat("5 · 2", 5, 2, False),
            quadrat("2²", 2, 3, True), quadrat("6²", 6, 2, True), quadrat("6 · 2", 6, 2, False),
            quadrat("7²", 7, 2, True), quadrat("8²", 8, 2, True), quadrat("3 · 2", 3, 2, False),
            quadrat("9²", 9, 2, True), quadrat("10²", 10, 2, True), quadrat("7 · 2", 7, 2, False),
            quadrat("5²", 5, 2, True)]


def costat(n):
    import math
    r = math.isqrt(n)
    if r * r == n:
        return [f"{n} quadrets", f"{r} quadrets", f"√{n} = {r}"]
    return [f"{n} quadrets", "no fa cap quadrat", f"entre {r} i {r + 1}"]


bloc3 = dict(
    titol="El quadrat d'un nombre", mira=(7, 7, FR),
    nota_sol="<b>La regla trencada de la fitxa:</b> 3² no és 3 · 2 = 6: és 3 · 3 = 9, un quadrat. Surt ja a "
             "l'a). La c (5 · 2) pregunta pel rectangle a posta: si sempre marca el número més gran, encara no "
             "mira el símbol. No l'expliqueu: que en compti els quadrets.",
    acts=[
        act("Marca el resultat de cada operació. Si dubtes, fes-ne el dibuix.", [
            tria(QUADRATS, en_linia=True)]),
        act("Fes un quadrat amb els quadrets. Quants quadrets té el costat?", [
            taula(["Tens", "El costat", "L'arrel"],
                  [costat(n) for n in (16, 9, 25, 4, 36, 49, 1, 64, 81, 100, 13, 20, 30)],
                  omplir=(1, 2), amples=[26, 30, 32],
                  abans=nota("Si no surt cap quadrat, escriu entre quins dos nombres és l'arrel."))],
            repte=True,
            nota_sol="El camí al revés: dels quadrets al costat, com l'exercici 8 de la fitxa. Els tres últims no fan "
                     "cap quadrat (exercici 9, nivells alts): 13 és entre el quadrat de 3 per 3 (9) i el de 4 per 4 (16)."),
    ])


# ------------------------------------------------- 4 · centenes, desenes i unitats --

def marca_nombre(c, d, u):
    n = 100 * c + 10 * d + u
    ops = sorted({n, int(f"{c}{u}"), int(f"{c}{u}{d}")}) if d == 0 else sorted({n, int(f"{c}{d}"), int(f"{c}0{d}")})
    assert n in ops and len(ops) == 3, (c, d, u, ops)
    t = f"{c} centenes, {d} desenes i {u} unitats" if c > 1 else f"{c} centena, {d} desenes i {u} unitats"
    t = t.replace(" 1 desenes", " 1 desena").replace(" 1 unitats", " 1 unitat")
    return (t, [str(x) for x in ops], ops.index(n))


MARCA = [marca_nombre(*r) for r in ((3, 0, 5), (1, 0, 8), (5, 1, 0), (2, 0, 7), (6, 4, 0), (4, 0, 2),
                                    (7, 3, 0), (9, 0, 1), (2, 5, 0), (8, 0, 6), (1, 2, 0), (6, 0, 9), (3, 7, 0))]


def blocs(n):
    c, r = divmod(n, 100)
    d, u = divmod(r, 10)
    return [str(n), str(c), str(d), str(u)]


bloc4 = dict(
    titol="Centenes, desenes i unitats", mira=(4, 5, FN),
    nota_sol="<b>La regla trencada de la fitxa:</b> el zero manté el lloc. «Tres-cents cinc» no és 35: és 305, "
             "3 centenes, cap desena i 5 unitats. Les opcions són les confusions de debò: el zero que falta i el "
             "zero que canvia de lloc. No l'expliqueu: que ompli la taula de centenes, desenes i unitats.",
    acts=[
        act("Marca el nombre que diu cada frase.", [tria(MARCA, en_linia=True)]),
        act("Escriu quants quadrats de 100, columnes de 10 i quadrets solts té cada nombre.", [
            taula(["Nombre", "Quadrats de 100", "Columnes de 10", "Quadrets solts"],
                  [blocs(n) for n in (243, 305, 124, 36, 510, 708, 99, 400, 61, 830, 107, 999, 20)],
                  omplir=(1, 2, 3), amples=[22, 22, 22, 22],
                  abans=nota("Si no n'hi ha cap, escriu un 0."))],
            repte=True,
            nota_sol="El camí al revés: del nombre als blocs. Els zeros són els que costen (708: cap columna; 36: "
                     "cap quadrat de 100). Si s'hi perd, que faci el nombre amb material de base 10."),
    ])


# ------------------------------------------------- 5 · el nom del nombre --

NOMS = (243, 510, 222, 108, 471, 35, 305, 610, 99, 128, 760, 404, 999)
NOMS_R = (305, 243, 150, 18, 702, 621, 90, 333, 840, 517, 26, 409, 111)

bloc5 = dict(
    titol="El nom del nombre", mira=(3, 4, FN),
    nota_sol="Sempre amb la clau de la pàgina 4 de la fitxa al davant. El guionet va entre les desenes i les "
             "unitats (quaranta-tres) i entre les unitats i les centenes (dos-cents); del 21 al 29, amb una i "
             "(vint-i-dos). Es dona per bo «setanta-un» per «setanta-u».",
    acts=[
        act("Escriu el nom de cada nombre. Mira la clau de la fitxa.", [
            taula(["Nombre", "Es llegeix"], [[str(n), nom_nombre(n)] for n in NOMS],
                  omplir=(1,), amples=[22, 66])]),
        act("Ara al revés: escriu el nombre amb xifres.", [
            taula(["Es llegeix", "El nombre"], [[nom_nombre(n), str(n)] for n in NOMS_R],
                  omplir=(1,), amples=[66, 22], esq=(0,))],
            repte=True,
            nota_sol="El camí al revés, on surt la regla trencada: «tres-cents cinc» és 305, no 35. Si li costa, que "
                     "ompli primer la taula de centenes, desenes i unitats."),
    ])


# ------------------------------------------------- 6 · sense parèntesi --

def ordre(a, b, c, mult_primer):
    """a + b · c (mult_primer=False vol dir a · b + c)."""
    if not mult_primer:
        return [f"{a} + {p(b, c)}", f"{p(b, c)} = {b * c}", f"{a} + {b * c} = {a + b * c}"]
    return [f"{p(a, b)} + {c}", f"{p(a, b)} = {a * b}", f"{a * b} + {c} = {a * b + c}"]


ESTA = [(2, 3, 4, 20), (1, 2, 5, 11), (3, 2, 3, 15), (4, 5, 2, 14), (5, 2, 4, 28), (2, 4, 3, 14), (6, 3, 2, 12),
        (1, 4, 4, 20), (3, 5, 2, 13), (7, 2, 5, 45), (2, 6, 3, 20), (4, 3, 3, 21), (5, 4, 2, 13)]


def esta_be(a, b, c, r):
    bo = a + b * c
    return (f"{a} + {p(b, c)} = {r}", ["Bé", "Malament"], 0 if r == bo else 1)


bloc6 = dict(
    titol="Primer, la multiplicació", mira=(1, 2, FO),
    nota_sol="Es diu sempre igual: «Primer, la multiplicació. Després, la suma.» Que busqui el punt abans de fer "
             "res. A les que comencen per la multiplicació, fer-ho en ordre de lectura també surt bé; a les "
             "altres, no.",
    acts=[
        act("Fes primer la multiplicació. Després fes la suma.", [
            taula(["L'operació", "Primer, la multiplicació", "Després, la suma"],
                  [ordre(*r) for r in ((2, 3, 4, False), (1, 2, 5, False), (5, 2, 3, True), (3, 2, 3, False),
                                       (2, 4, 1, True), (4, 3, 5, False), (6, 2, 2, True), (1, 5, 4, False),
                                       (3, 3, 4, True), (7, 2, 6, False), (2, 6, 5, True), (5, 4, 3, False),
                                       (4, 4, 6, True))],
                  omplir=(1, 2), amples=[24, 32, 32],
                  abans=nota("Sense parèntesis, primer es multiplica. Busca el punt."))]),
        act("Està bé? Marca la resposta.", [
            tria([esta_be(*r) for r in ESTA], en_linia=True,
                 sol_nota="Les bones: " + " · ".join(f"{a} + {p(b, c)} = {a + b * c}" for a, b, c, _ in ESTA) + ".")],
            repte=True,
            nota_sol="<b>La regla trencada de la fitxa:</b> fer-ho d'esquerra a dreta, com es llegeix (2 + 3 · 4 = 20). "
                     "Les dolentes són exactament aquest error. Si diu que està bé, que faci el dibuix: 3 files de 4 "
                     "i 2 quadrets solts."),
    ])


# ------------------------------------------------- 7 · amb parèntesi --

def parentesi(a, b, c, davant):
    """(a + b) · c, o c · (a + b) si `davant`."""
    t = f"{c} · ({a} + {b})" if davant else f"({a} + {b}) · {c}"
    s = a + b
    m = f"{c} · {s}" if davant else f"{s} · {c}"
    return [t, f"{a} + {b} = {s}", f"{m} = {s * c}"]


def posa(a, b, c):
    """Posa el parèntesi perquè doni el resultat: 2 + 3 · 4 = 20 → (2 + 3) · 4."""
    return [f"{a} + {p(b, c)} = {(a + b) * c}", f"({a} + {b}) · {c}"]


bloc7 = dict(
    titol="Primer, el parèntesi", mira=(2, 3, FO),
    nota_sol="Amb parèntesi, primer es fa el parèntesi: «Primer, el parèntesi. Després, la multiplicació.» Totes "
             "les sumes es fan sense portar-ne, i les multiplicacions són de la targeta.",
    acts=[
        act("Fes primer el parèntesi. Després fes la multiplicació.", [
            taula(["L'operació", "Primer, el parèntesi", "Després, la multiplicació"],
                  [parentesi(*r) for r in ((1, 4, 2, False), (1, 2, 4, True), (3, 1, 2, False), (2, 2, 3, True),
                                           (2, 3, 4, False), (4, 1, 5, True), (3, 3, 2, False), (1, 6, 3, True),
                                           (5, 2, 4, False), (2, 4, 6, True), (3, 4, 5, False), (4, 4, 2, True),
                                           (6, 3, 3, False))],
                  omplir=(1, 2), amples=[24, 32, 32])]),
        act("Posa un parèntesi perquè doni el resultat que diu.", [
            taula(["L'operació", "Amb el parèntesi"],
                  [posa(*r) for r in ((2, 3, 4), (1, 2, 5), (3, 2, 3), (4, 1, 2), (1, 4, 3), (2, 2, 5), (5, 1, 4),
                                      (3, 3, 2), (1, 5, 6), (6, 2, 3), (2, 7, 2), (4, 4, 5), (3, 6, 4))],
                  omplir=(1,), amples=[44, 44])],
            repte=True,
            nota_sol="El camí al revés: de 20 al parèntesi. Sense parèntesi, 2 + 3 · 4 fa 14; perquè faci 20, primer "
                     "s'ha de sumar: (2 + 3) · 4. Que ho comprovi fent els dos comptes."),
    ])


# ------------------------------------------------- 8 · quin dibuix és? --

def quin(a, b, c, amb):
    """2 + 3 · 4 o (2 + 3) · 4: les dues respostes possibles, i la bona."""
    sense, ambp = a + b * c, (a + b) * c
    assert sense != ambp
    t = f"({a} + {b}) · {c}" if amb else f"{a} + {p(b, c)}"
    ops = sorted([sense, ambp])
    return (f"{t} =", [str(x) for x in ops], ops.index(ambp if amb else sense))


QUIN = [quin(2, 3, 4, False), quin(1, 2, 5, True), quin(1, 2, 5, False), quin(3, 1, 4, True), quin(2, 4, 3, False),
        quin(4, 2, 2, True), quin(3, 2, 5, False), quin(2, 2, 6, True), quin(5, 3, 2, False), quin(1, 3, 7, True),
        quin(4, 4, 3, False), quin(6, 2, 3, True), quin(3, 5, 2, False)]


def situacio(text, op, total, que):
    return [text, op, f"{total} {que}"]


bloc8 = dict(
    titol="A la vida de cada dia", mira=(4, 5, FO),
    nota_sol="<b>La regla trencada de la fitxa:</b> sense parèntesi, primer es multiplica. A l'a) (2 + 3 · 4) la "
             "resposta de qui ho fa d'esquerra a dreta, 20, també hi és. La b demana el parèntesi a posta. Si "
             "s'equivoca, que en faci el dibuix i compti els quadrets.",
    acts=[
        act("Marca el resultat bo. Mira si hi ha parèntesi.", [tria(QUIN, en_linia=True)]),
        act("Quants n'hi ha? Escriu l'operació.", [
            taula(["Situació", "L'operació", "Quants n'hi ha"],
                  [situacio(*r) for r in (
                      ("2 iogurts solts i 3 paquets de 4 iogurts.", "2 + 3 · 4", 14, "iogurts"),
                      ("3 ous solts i 2 capses de 6 ous.", "3 + 2 · 6", 15, "ous"),
                      ("2 bosses. A cada bossa, 3 pomes i 1 pera.", "2 · (3 + 1)", 8, "peces"),
                      ("1 llapis solt i 4 capses de 5 llapis.", "1 + 4 · 5", 21, "llapis"),
                      ("3 bosses. A cada bossa, 2 pomes i 2 peres.", "3 · (2 + 2)", 12, "peces"),
                      ("5 cromos solts i 2 sobres de 10 cromos.", "5 + 2 · 10", 25, "cromos"),
                      ("4 plats. A cada plat, 2 galetes i 3 maduixes.", "4 · (2 + 3)", 20, "peces"),
                      ("6 ampolles soltes i 3 caixes de 6 ampolles.", "6 + 3 · 6", 24, "ampolles"),
                      ("2 taules. A cada taula, 4 nens i 2 nenes.", "2 · (4 + 2)", 12, "persones"),
                      ("3 cotxes. A cada cotxe, 1 adult i 3 nens.", "3 · (1 + 3)", 12, "persones"),
                      ("7 boles soltes i 5 capses de 4 boles.", "7 + 5 · 4", 27, "boles"),
                      ("5 caixes. A cada caixa, 6 pomes i 4 peres.", "5 · (6 + 4)", 50, "peces"),
                      ("9 llibres solts i 4 piles de 10 llibres.", "9 + 4 · 10", 49, "llibres"))],
                  omplir=(1, 2), amples=[48, 22, 18], esq=(0,))],
            repte=True,
            nota_sol="Escriure l'operació d'una situació, com els exercicis 5 i 6 de la fitxa. Es donen per bones les "
                     "operacions escrites en un altre ordre si surt el mateix (3 · 4 + 2). El que compta és que la "
                     "multiplicació surti de les capses o de les bosses, i que el parèntesi hi sigui quan cal."),
    ])


BLOCS = [bloc1, bloc2, bloc3, bloc4, bloc5, bloc6, bloc7, bloc8]
