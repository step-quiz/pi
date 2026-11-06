"""Quadern d'activitats de la Unitat 2 · Divisibilitat.

    python3 1eso/generadors/gen_quadern.py 2        (des de l'arrel)

La unitat té quatre fitxes (Els múltiples, Repartir en files, Divisors i primers, La
factorització), i el quadern hi fa dos blocs per fitxa, dels exercicis que en són el nucli
(el camp «minim» de dades/unitats.js) i de la regla trencada. A cada bloc, una activitat germana
i una de repte. Cada activitat té 13 apartats: l'a), resolt, i 12 per fer. El filtre en deixa 3
(petit), 6 (mitjà) o tots 12 (elevat), sempre els primers: per això van de menys a més.

Les regles del curs (docs/CRITERIS-DISSENY.md): tot es fa amb la targeta de les taules al
davant, sense calculadora i amb nombres de tres xifres com a molt; es multiplica amb «·». Els
números es calculen aquí, no s'escriuen a mà: així el solucionari no es pot equivocar.
"""
from quadern import act, taula, tria, nota

NUM = 2
TITOL = "Divisibilitat"   # el de dades/unitats.js
AVALUAR = ("Sempre amb la targeta al davant. El que s'avalua és la decisió (és a la taula?, en sobren?, "
           "fa més d'un rectangle?, està acabada?), no la memòria: si consulta la targeta, està bé. Una "
           "suma de xifres mal feta no hauria de fer baixar la valoració si el camí és bo. Les activitats de "
           "repte compten per als nivells alts (AN, AE), no per al mínim.")

M1, M2, M3, M4 = "Els múltiples", "Repartir en files", "Divisors i primers", "La factorització"
SI, NO = "Sí", "No"


def sino(c):
    return SI if c else NO


def punt(*f):
    return " · ".join(str(x) for x in f)


# ------------------------------------------------- 1 · els múltiples --

def multiples(n, quants=5):
    return ", ".join(str(n * i) for i in range(quants))


def falta(n, pos):
    """Una llista de cinc múltiples amb un forat a la posició `pos`."""
    llista = [str(n * i) for i in range(5)]
    llista[pos] = "___"
    return [", ".join(llista), str(n * pos), f"del {n}"]


bloc1 = dict(
    titol="Els múltiples", mira=(1, 2, M1),
    nota_sol="Els múltiples d'un nombre són la seva taula: la columna de la targeta, de dalt a baix. "
             "<b>Error típic:</b> oblidar el 0, o saltar-se una fila de la targeta.",
    acts=[
        act("Escriu els cinc primers múltiples de cada nombre. Comença pel 0.", [
            taula(["Nombre", "Els cinc primers múltiples"],
                  [[f"Del {n}", multiples(n)] for n in (2, 5, 10, 3, 4, 6, 9, 8, 7, 1, 11, 20, 50)],
                  omplir=(1,), amples=[26, 62], abans=nota("Mira la targeta de les taules."),
                  sol_nota="Els de l'11, el 20 i el 50 no són a la targeta: es fan sumant cada vegada el "
                           "mateix nombre (0, 20, 40, 60, 80).")]),
        act("Escriu el múltiple que falta i de quin nombre són.", [
            taula(["La llista", "El que falta", "Són múltiples"],
                  [falta(n, p) for n, p in ((4, 3), (3, 2), (5, 4), (2, 1), (10, 3), (6, 2), (9, 4), (7, 3),
                                            (8, 1), (6, 4), (9, 2), (7, 4), (8, 3))],
                  omplir=(1, 2), amples=[44, 22, 22])],
            repte=True,
            nota_sol="El camí al revés: de la llista al nombre. El segon número de la llista ja diu de quin "
                     "nombre són (el primer és el 0). Si costa, que busqui la llista a la targeta."),
    ])


# ------------------------------------------------- 2 · el truc del 3 --

def suma_xifres(n):
    return sum(int(c) for c in str(n))


def truc3(n):
    s = suma_xifres(n)
    return [str(n), " + ".join(str(n)) + f" = {s}", sino(s % 3 == 0), sino(n % 3 == 0)]


def quatre(n):
    return [str(n), sino(n % 2 == 0), sino(n % 5 == 0), sino(n % 10 == 0), sino(n % 3 == 0)]


bloc2 = dict(
    titol="El truc del 3", mira=(4, 5, M1),
    nota_sol="<b>La regla trencada de la fitxa:</b> acabar en 3 no vol dir ser múltiple del 3. Ja a "
             "l'apartat b (el 13) i a la d (el 23) passa, perquè també surti a la quantitat petita. Si diu "
             "que sí sense sumar, que busqui la suma a la taula del 3 de la targeta.",
    acts=[
        act("Fes el truc del 3 amb cada nombre. Ves a poc a poc.", [
            taula(["Nombre", "Suma de les xifres", "És a la taula del 3?", "És múltiple del 3?"],
                  [truc3(n) for n in (132, 13, 213, 23, 51, 74, 102, 53, 225, 98, 303, 145, 471)],
                  omplir=(1, 2, 3), amples=[16, 28, 22, 22],
                  abans=nota("La taula del 3: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30."))]),
        act("Fes els quatre trucs. Escriu Sí o No.", [
            taula(["Nombre", "Múltiple del 2?", "Múltiple del 5?", "Múltiple del 10?", "Múltiple del 3?"],
                  [quatre(n) for n in (120, 35, 64, 90, 33, 75, 48, 100, 51, 210, 87, 15, 400)],
                  omplir=(1, 2, 3, 4), amples=[16, 18, 18, 18, 18],
                  abans=nota("El 2, el 5 i el 10: mira l'última xifra. El 3: suma les xifres."))],
            repte=True,
            nota_sol="Com l'exercici 5 de la fitxa: quatre decisions per a cada nombre, i cada una amb el seu "
                     "truc. <b>Error típic:</b> fer servir l'última xifra també per al 3 (el 33 i el 51)."),
    ])


# ------------------------------------------------- 3 · sobren quadrets? --

EXACTA, SOBREN = "És exacta", "En sobren"


def reparteix(n, k):
    return divmod(n, k)


def igualtat(n, k):
    q, r = divmod(n, k)
    return f"{n} = {q} · {k} + {r}"


SOBREN3 = ((25, 4), (24, 6), (17, 5), (35, 7), (40, 8), (22, 3), (36, 9), (50, 7), (42, 6), (29, 10),
           (64, 8), (31, 4), (45, 5))

bloc3 = dict(
    titol="Sobren quadrets?", mira=(2, 3, M2),
    nota_sol="Si el nombre és a la taula de la targeta, la divisió és exacta; si no hi és, en sobren. No "
             "cal fer el dibuix, però si dubta, que el faci.",
    acts=[
        act("Sobren quadrets? Marca la resposta. Mira la targeta.", [
            tria([(f"{n} quadrets en files de {k}", [SOBREN, EXACTA], 0 if n % k else 1) for n, k in SOBREN3],
                 en_linia=True,
                 sol_nota="Les igualtats: " + " · ".join(igualtat(n, k) for n, k in SOBREN3) + ".")]),
        act("Escriu les files plenes i els quadrets que sobren.", [
            taula(["Quadrets", "En files de", "Files plenes", "En sobren"],
                  [[str(n), str(k), str(n // k), str(n % k)]
                   for n, k in ((38, 6), (47, 5), (29, 9), (53, 8), (61, 7), (44, 10), (70, 9), (33, 4),
                                (59, 6), (80, 7), (67, 8), (95, 10), (26, 3))],
                  omplir=(2, 3), amples=[22, 22, 22, 22])],
            repte=True,
            nota_sol="Un pas més: no només si en sobren, sinó quants. Es busca a la taula de la targeta el "
                     "més gran que no passa del nombre (6 · 6 = 36 per al 38) i es compta endavant fins al "
                     "nombre: 37, 38, en sobren 2."),
    ])


# ------------------------------------------------- 4 · la igualtat --

def plantilla(n, k):
    forat = '<span class="buit" style="min-width:1.3cm"></span>'
    return (f"{n} = {forat} · {k} + {forat}", igualtat(n, k))


IGUALTATS = ((38, 6), (40, 6), (35, 7), (20, 6), (10, 3), (23, 4), (45, 9), (30, 8), (27, 5), (56, 7),
             (19, 2), (60, 10), (75, 9))


def situacio(text, n, k, que):
    q, r = divmod(n, k)
    return [text, igualtat(n, k), f"{q + (1 if r else 0)} {que}"]


bloc4 = dict(
    titol="La igualtat", mira=(3, 4, M2),
    nota_sol="<b>La regla trencada de la fitxa:</b> el residu no s'oblida. Al primer forat hi van les files "
             "plenes; al segon, els que sobren, i un 0 si no en sobra cap (l'apartat c). Si escriu «35 = 5 · 7» "
             "sense el + 0, és bo, però que digui que no en sobra cap.",
    acts=[
        act("Completa la igualtat. Al primer forat, les files plenes. Al segon, els que sobren.", [
            taula(["Quadrets", "En files de", "La igualtat"],
                  [[str(n), str(k), igualtat(n, k) if i == 0 else plantilla(n, k)]
                   for i, (n, k) in enumerate(IGUALTATS)],
                  omplir=(), amples=[18, 18, 52])]),
        act("Escriu la igualtat i quants en calen perquè hi càpiguen tots.", [
            taula(["Situació", "La igualtat", "Quants en calen?"],
                  [situacio(*s) for s in (
                      ("26 persones. Les barques són de 4.", 26, 4, "barques"),
                      ("30 persones. Els cotxes són de 5.", 30, 5, "cotxes"),
                      ("20 ous. Les capses són de 6.", 20, 6, "capses"),
                      ("35 alumnes. Les taules són de 4.", 35, 4, "taules"),
                      ("24 llapis. Les capses són de 8.", 24, 8, "capses"),
                      ("50 persones. Les barques són de 6.", 50, 6, "barques"),
                      ("17 pomes. Les bosses són de 3.", 17, 3, "bosses"),
                      ("63 cadires. Les files són de 9.", 63, 9, "files"),
                      ("41 cromos. Les pàgines són de 6.", 41, 6, "pàgines"),
                      ("28 persones. Les taules són de 6.", 28, 6, "taules"),
                      ("70 ous. Les capses són de 10.", 70, 10, "capses"),
                      ("38 persones. Els cotxes són de 5.", 38, 5, "cotxes"),
                      ("55 persones. Les barques són de 7.", 55, 7, "barques"))],
                  omplir=(1, 2), amples=[40, 28, 20], esq=(0,))],
            repte=True,
            nota_sol="Una decisió nova, com les barques de la fitxa: els que sobren també han de cabre, i "
                     "per això cal una barca més (26 = 6 · 4 + 2: 7 barques). Si la divisió és exacta, no cal "
                     "cap més. <b>Error típic:</b> respondre les files plenes (6 barques)."),
    ])


# ------------------------------------------------- 5 · els divisors --

def parelles(n):
    """Les multiplicacions que donen n, sense girar-les: 1 · n i les de la targeta."""
    return [(a, n // a) for a in range(1, int(n ** 0.5) + 1) if n % a == 0]


def divisors(n):
    return sorted({x for p in parelles(n) for x in p})


def llista_i(v):
    v = [str(x) for x in v]
    return ", ".join(v[:-1]) + " i " + v[-1] if len(v) > 1 else v[0]


def fila_divisors(n):
    ps = parelles(n)
    assert all(b <= 10 for a, b in ps[1:]), n   # totes són a la targeta, menys la fila d'1
    return [str(n), f"{n} = " + " = ".join(punt(a, b) for a, b in ps), llista_i(divisors(n))]


bloc5 = dict(
    titol="Els divisors", mira=(1, 2, M3),
    nota_sol="Cada rectangle dona dos divisors: les files i els quadrets de cada fila. La fila d'1 hi és "
             "sempre (1 · 12). <b>Error típic:</b> deixar-se l'1 i el mateix nombre, o escriure dues vegades "
             "el 4 del 16.",
    acts=[
        act("Escriu les multiplicacions que donen cada nombre i els seus divisors.", [
            taula(["Nombre", "Les multiplicacions", "Els divisors"],
                  [fila_divisors(n) for n in (12, 6, 8, 10, 14, 15, 16, 18, 21, 25, 27, 35, 49)],
                  omplir=(1, 2), amples=[12, 50, 26], abans=nota("Sempre hi ha la fila d'1. Després, busca a la targeta."))]),
        act("Escriu tres múltiples i tots els divisors de cada nombre.", [
            taula(["Nombre", "Tres múltiples", "Tots els divisors"],
                  [[str(n), f"{n}, {2 * n}, {3 * n}", llista_i(divisors(n))]
                   for n in (4, 3, 5, 7, 12, 15, 2, 10, 14, 16, 20, 18, 11)],
                  omplir=(1, 2), amples=[16, 36, 36],
                  sol_nota="Es dona per bo qualsevol trio de múltiples, si són de la taula (sense el 0).")],
            repte=True,
            nota_sol="No els confonguis: els múltiples són la taula (més grans), i els divisors, els costats "
                     "dels rectangles (més petits). <b>Error típic:</b> escriure els divisors a la columna dels "
                     "múltiples. L'11 no és a la targeta: només fa una fila, 1 · 11."),
    ])


# ------------------------------------------------- 6 · és primer? --

def primer(n):
    return n > 1 and all(n % a for a in range(2, n))


def mult(n):
    p = parelles(n)
    a, b = p[-1] if len(p) > 1 else p[0]
    return punt(a, b)


PRIMERS = (15, 5, 9, 13, 21, 3, 25, 17, 27, 19, 35, 2, 49)
CADIRES = (12, 7, 15, 11, 20, 13, 9, 17, 25, 23, 27, 19, 29)

bloc6 = dict(
    titol="És primer?", mira=(3, 4, M3),
    nota_sol="<b>La regla trencada de la fitxa:</b> no tots els senars són primers. L'a) (el 15) i la c "
             "(el 9) són senars i no ho són. Si diu que sí, que en faci el rectangle amb miniblocs. El 2 és "
             "parell i és primer.",
    acts=[
        act("És primer? Marca la resposta.", [
            tria([(f"{n} és primer?", [SI, NO], 0 if primer(n) else 1) for n in PRIMERS], en_linia=True,
                 sol_nota="Les multiplicacions: " + " · ".join(f"{n} = {mult(n)}" for n in PRIMERS) + ".")]),
        act("Es poden posar les cadires en files iguals, de més d'una cadira?", [
            tria([(f"Hi ha {n} cadires.", [SI, NO], 1 if primer(n) else 0) for n in CADIRES], en_linia=True,
                 sol_nota="Les files: " + " · ".join(f"{n} = {mult(n)}" for n in CADIRES) + ".")],
            repte=True,
            nota_sol="La mateixa decisió que «és primer?», amb cadires de debò: amb un nombre primer només hi "
                     "ha una fila (7 = 1 · 7). Que digui la multiplicació de les files quan es pot."),
    ])


# ------------------------------------------------- 7 · està acabada? --

ACABADA = (("18 = 2 · 9", "2 · 3 · 3"), ("20 = 2 · 2 · 5", None), ("12 = 2 · 6", "2 · 2 · 3"),
           ("30 = 5 · 6", "2 · 3 · 5"), ("27 = 3 · 3 · 3", None), ("8 = 2 · 4", "2 · 2 · 2"),
           ("45 = 3 · 3 · 5", None), ("28 = 4 · 7", "2 · 2 · 7"), ("50 = 2 · 5 · 5", None),
           ("63 = 7 · 9", "3 · 3 · 7"), ("42 = 2 · 3 · 7", None), ("75 = 3 · 25", "3 · 5 · 5"),
           ("98 = 2 · 49", "2 · 7 · 7"))


def comprova_fact(text, bona):
    n, f = text.split(" = ")
    factors = [int(x) for x in f.split(" · ")]
    prod = 1
    for x in factors:
        prod *= x
    assert prod == int(n), text
    assert all(primer(x) for x in factors) == (bona is None), text
    if bona:
        p = 1
        for x in bona.split(" · "):
            assert primer(int(x)), bona
            p *= int(x)
        assert p == int(n), bona
    return text


ACABAR = ("20 = 4 · 5", "18 = 3 · 6", "30 = 3 · 10", "8 = 2 · 4", "45 = 5 · 9", "28 = 7 · 4", "50 = 5 · 10",
          "27 = 3 · 9", "12 = 2 · 6", "42 = 6 · 7", "63 = 7 · 9", "36 = 4 · 9", "24 = 4 · 6")


def factoritza(n):
    f, d = [], 2
    while n > 1:
        while n % d == 0:
            f.append(d)
            n //= d
        d += 1
    return f


bloc7 = dict(
    titol="Està acabada?", mira=(2, 3, M4),
    nota_sol="<b>La regla trencada de la fitxa:</b> una multiplicació que dona el nombre encara no és la "
             "factorització si hi queda algun nombre que no és primer. Ja a l'a) (2 · 9) passa. Si diu que sí, "
             "que miri si el 9 fa més d'un rectangle.",
    acts=[
        act("Està acabada la factorització? Marca la resposta.", [
            tria([(comprova_fact(t, b), [SI, NO], 0 if b is None else 1) for t, b in ACABADA], en_linia=True,
                 sol_nota="Les que no estan acabades: " + " · ".join(
                     f"{t.split(' = ')[0]} = {b}" for t, b in ACABADA if b) + ".")],
            ),
        act("Acaba la factorització. Tots han de ser primers.", [
            taula(["La que tens", "Acabada"],
                  [[t, f"{t.split(' = ')[0]} = " + punt(*factoritza(int(t.split(' = ')[0])))] for t in ACABAR],
                  omplir=(1,), amples=[40, 48])],
            repte=True,
            nota_sol="Un pas més: no només dir que no està acabada, sinó acabar-la. Cada nombre que no és primer "
                     "es torna a partir amb la targeta. Els dos últims (36 i 24) tenen quatre factors: "
                     "36 = 2 · 2 · 3 · 3."),
    ])


# ------------------------------------------------- 8 · la recepta --

def recepta(a, b, c):
    return [punt(a, b, c), f"{punt(a, b)} = {a * b}", f"{a * b} · {c} = {a * b * c}", str(a * b * c)]


RECEPTES = ((2, 3, 3), (2, 2, 5), (3, 3, 5), (2, 5, 5), (2, 2, 7), (2, 3, 5), (3, 3, 3), (2, 2, 2),
            (2, 3, 7), (3, 3, 7), (2, 5, 7), (2, 2, 3), (2, 2, 11))

bloc8 = dict(
    titol="Quin nombre és?", mira=(3, 4, M4),
    nota_sol="És el camí de tornada de l'arbre: multiplicar els dos primers i després pel tercer. Totes les "
             "multiplicacions són de la targeta, menys l'última (4 · 11 = 44), que es fa sumant: 11 + 11 + 11 + 11.",
    acts=[
        act("Quin nombre és? Multiplica els dos primers. Després, pel tercer.", [
            taula(["La factorització", "Els dos primers", "Pel tercer", "El nombre"],
                  [recepta(*r) for r in RECEPTES], omplir=(1, 2, 3), amples=[24, 22, 24, 18])]),
        act("Escriu la factorització de cada nombre. Busca a la targeta.", [
            taula(["Nombre", "La factorització"],
                  [[str(n), f"{n} = " + punt(*factoritza(n))]
                   for n in (18, 12, 20, 30, 8, 27, 45, 50, 28, 42, 63, 24, 36)],
                  omplir=(1,), amples=[30, 58],
                  sol_nota="Es pot fer amb l'arbre: es dona per bo qualsevol camí, si acaba en primers. La "
                           "factorització s'escriu de petit a gran.")],
            repte=True,
            nota_sol="El camí d'anada, sense la plantilla de l'arbre: cada pas és buscar a la targeta una "
                     "multiplicació que doni el nombre. Si es perd, que faci l'arbre al marge."),
    ])


BLOCS = [bloc1, bloc2, bloc3, bloc4, bloc5, bloc6, bloc7, bloc8]
