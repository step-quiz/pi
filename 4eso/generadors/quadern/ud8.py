"""Quadern d'activitats de la Unitat 8 · Mesura indirecta.

    python3 4eso/generadors/gen_quadern.py 8        (des de l'arrel)

Un bloc per cada exercici de la fitxa (u8/fitxa.html), en el mateix ordre: els blocs 1 a 5 són la
Part 1 (Semblança) i els blocs 6 a 10, la Part 2 (Pitàgores). A cada bloc, una activitat germana i
una de repte. Cada activitat té 13 apartats: l'a), resolt, i 12 per fer. El filtre en deixa 3
(petit), 6 (mitjà) o tots 12 (elevat), sempre els primers.

Com a la fitxa: semblança amb la taula Ombra | Alçada i el producte en creu; Pitàgores sempre amb
a² = b² + c² i la hipotenusa com a incògnita (cap catet); la calculadora fa els comptes. La regla
trencada (les ombres no es resten) és el bloc 4. Els números es calculen aquí, no s'escriuen a mà:
així el solucionari no es pot equivocar.
"""
import math

from quadern import act, taula, tria, nota, num
from peces import doble_ombra

NUM = 8
TITOL = "Mesura indirecta"   # el de dades/unitats.js (decisió V2)
AVALUAR = ("Com a la fitxa, l'objectiu no és calcular bé: és plantejar bé la taula (on va cada ombra i "
           "cada alçada) i triar el camí, ombra o triangle. Un error de calculadora no hauria de fer baixar "
           "la valoració si el plantejament és correcte. Les activitats de repte compten per als nivells "
           "alts (AN, AE), no per al mínim.")


def m(x, u="m"):
    return f"{num(x)} {u}"


def exacte(x):
    """Un resultat que ha de sortir amb dos decimals com a molt (el solucionari no arrodoneix)."""
    assert abs(round(x, 2) - x) < 1e-9, x
    return round(x, 2)


def creu(po, pa, oo):
    """L'alçada d'un objecte d'ombra oo, amb un pal d'ombra po i alçada pa: el producte en creu."""
    return exacte(pa * oo / po), f"{num(po)} · x = {num(pa)} · {num(oo)} = {num(pa * oo)}"


# ------------------------------------------------- 1 · la taula i el producte en creu --

B1 = [(3, 2, "Arbre", 12), (2, 1, "Fanal", 10), (4, 3, "Edifici", 12), (5, 2, "Campanar", 20),
      (2, 1, "Porteria", 4), (3, 1, "Tanca", 6), (4, 1, "Grua", 40), (3, 2, "Torre", 18),
      (5, 3, "Antena", 25), (2, 3, "Xemeneia", 8), (4, 5, "Font", 4), (6, 4, "Palmera", 15),
      (5, 4, "Cartell", 10)]


def fila1(po, pa, nom, oo):
    x, c = creu(po, pa, oo)
    return [nom, f"{num(po)} m · {num(pa)} m", m(oo), c, m(x)]


B1R = [("Arbre", 12, 8, 3), ("Edifici", 20, 15, 2), ("Fanal", 10, 5, 4), ("Torre", 18, 12, 3),
       ("Campanar", 30, 20, 3), ("Grua", 40, 10, 6), ("Antena", 25, 15, 5), ("Palmera", 15, 10, 3),
       ("Xemeneia", 8, 12, 2), ("Cartell", 10, 8, 5), ("Porteria", 4, 2, 2), ("Tanca", 6, 2, 3),
       ("Font", 4, 5, 4)]


def fila1r(nom, oo, oa, po):
    x = exacte(oa * po / oo)
    return [f"{nom}: {num(oo)} m · {num(oa)} m", m(po), f"{num(oo)} · x = {num(oa)} · {num(po)} = {num(oa * po)}", m(x)]


bloc1 = dict(
    titol="La taula i el producte en creu", mira=(1, 4),
    nota_sol="La taula sempre és Ombra | Alçada, amb el pal a dalt i l'objecte a baix. <b>Error típic:</b> "
             "multiplicar els dos números de la mateixa fila. Les diagonals de la pàgina 3 de la fitxa ho "
             "recorden: ombra del pal amb x, ombra de l'objecte amb l'alçada del pal.",
    acts=[
        act("Troba l'alçada de cada objecte amb el producte en creu.", [
            taula(["Objecte", "Pal (ombra · alçada)", "Ombra", "Resolem", "Alçada"],
                  [fila1(*f) for f in B1], omplir=(3, 4), amples=[16, 20, 12, 26, 14])], ico="calc"),
        act("Ara la x és l'alçada del pal: troba-la amb el producte en creu.", [
            taula(["Objecte (ombra · alçada)", "Ombra del pal", "Resolem", "Alçada del pal"],
                  [fila1r(*f) for f in B1R], omplir=(2, 3), amples=[30, 14, 28, 16], esq=(0,))],
            ico="calc", repte=True,
            nota_sol="La mateixa taula, amb la x a l'altra fila. Qui ha après «la x sempre va a baix» "
                     "s'hi encalla: cal omplir la taula amb el que diu cada fila."),
    ])


# ------------------------------------------------- 2 · amb la calculadora --

B2 = [(4, 3, "Torre", 36), (2, 1.5, "Porteria", 3.2), (3, 2, "Cartell", 4.5), (1.5, 1, "Xemeneia", 24),
      (2, 1.5, "Fanal", 8), (1.2, 0.8, "Arbre", 6), (2, 1.6, "Cistella", 3.75), (2.5, 1, "Edifici", 30),
      (0.8, 1.2, "Pi", 6), (1.5, 2, "Torre", 13.5), (2, 1.5, "Antena", 5.2), (3, 1.8, "Grua", 25),
      (1.6, 1.2, "Palmera", 10)]

B2R = [("Institut", 2, 1.5, 20), ("Biblioteca", 4, 3, 16), ("Hotel", 3, 2, 27), ("Casa", 2, 1, 12),
       ("Escola", 5, 3, 15), ("Hospital", 1.5, 1, 31.5), ("Ajuntament", 2, 1.5, 32), ("Oficines", 4, 3, 36),
       ("Torre de pisos", 3, 2, 45), ("Mercat", 2.5, 1.5, 15), ("Museu", 1, 1.2, 10), ("Estació", 2, 3, 10),
       ("Teatre", 0.5, 0.6, 15)]


def fila2r(nom, po, pa, oo):
    x, _ = creu(po, pa, oo)
    pisos = x / 3
    assert pisos == int(pisos), (nom, x)
    return [nom, f"{num(po)} m · {num(pa)} m", m(oo), m(x), f"{x:g} ÷ 3 = {int(pisos)}".replace(".", ",")]


bloc2 = dict(
    titol="Amb la calculadora", mira=(2, 6),
    nota_sol="Els mateixos passos, amb decimals: la calculadora fa el compte. <b>Error típic:</b> escriure "
             "1,5 · x = 24 i dividir 1,5 entre 24. El número que va sol (el de la x) és el que divideix.",
    acts=[
        act("Troba l'alçada de cada objecte amb la calculadora.", [
            taula(["Objecte", "Pal (ombra · alçada)", "Ombra", "Resolem", "Alçada"],
                  [fila1(*f) for f in B2], omplir=(3, 4), amples=[16, 20, 12, 26, 14])], ico="calc"),
        act("Calcula l'alçada de cada edifici i quants pisos de 3 m té.", [
            taula(["Edifici", "Pal (ombra · alçada)", "Ombra", "Alçada", "Pisos"],
                  [fila2r(*f) for f in B2R], omplir=(3, 4), amples=[20, 20, 14, 14, 20])],
            ico="calc", repte=True,
            nota_sol="Un pas més: després de l'alçada, dividir entre 3. Si l'alçada surt malament, els pisos "
                     "també, però el pas de dividir pot ser bo: mireu-los per separat."),
    ])


# ------------------------------------------------- 3 · la doble recta --

def recta3(po, pa, n, ombres):
    return [[m(o), m(exacte(o * pa / po))] for o in ombres]


def recta3r(po, pa, n, alcades):
    return [[m(a), m(exacte(a * po / pa))] for a in alcades]


A3 = [44, 44]

bloc3 = dict(
    titol="La doble recta", mira=(3, 8),
    nota_sol="No cal calcular: es baixa la vertical i es continua la recta de baix de pas en pas. És la "
             "mateixa doble recta de la Unitat 3 i de les eines («Ombra i alçada»).",
    acts=[
        act("Baixa la vertical i escriu l'alçada que va amb cada ombra.", [
            taula(["Ombra", "Alçada"], recta3(3, 2, 5, [6, 9, 12, 15]), omplir=(1,), amples=A3,
                  abans=nota("Un pal de 2 m fa una ombra de 3 m.") + doble_ombra(3, 2, 5)),
            taula(["Ombra", "Alçada"], recta3(2, 1, 6, [6, 8, 12]), omplir=(1,), amples=A3,
                  abans=nota("Un pal d'1 m fa una ombra de 2 m.") + doble_ombra(2, 1, 6)),
            taula(["Ombra", "Alçada"], recta3(4, 3, 5, [8, 12, 20]), omplir=(1,), amples=A3,
                  abans=nota("Un pal de 3 m fa una ombra de 4 m.") + doble_ombra(4, 3, 5)),
            taula(["Ombra", "Alçada"], recta3(5, 2, 5, [10, 15, 25]), omplir=(1,), amples=A3,
                  abans=nota("Un pal de 2 m fa una ombra de 5 m.") + doble_ombra(5, 2, 5)),
        ], ico="regle"),
        act("Puja la vertical i escriu l'ombra que va amb cada alçada.", [
            taula(["Alçada", "Ombra"], recta3r(3, 2, 5, [4, 8, 5, 10]), omplir=(1,), amples=A3,
                  abans=nota("Un pal de 2 m fa una ombra de 3 m.") + doble_ombra(3, 2, 5, amaga="dalt")),
            taula(["Alçada", "Ombra"], recta3r(2, 1, 6, [3, 5, 2.5]), omplir=(1,), amples=A3,
                  abans=nota("Un pal d'1 m fa una ombra de 2 m.") + doble_ombra(2, 1, 6, amaga="dalt")),
            taula(["Alçada", "Ombra"], recta3r(4, 3, 5, [6, 12, 4.5]), omplir=(1,), amples=A3,
                  abans=nota("Un pal de 3 m fa una ombra de 4 m.") + doble_ombra(4, 3, 5, amaga="dalt")),
            taula(["Alçada", "Ombra"], recta3r(5, 2, 5, [6, 3, 9]), omplir=(1,), amples=A3,
                  abans=nota("Un pal de 2 m fa una ombra de 5 m.") + doble_ombra(5, 2, 5, amaga="dalt")),
        ], ico="regle", repte=True,
            nota_sol="El camí al revés: de baix a dalt. Les alçades que no cauen en una marca (5 m, 2,5 m, "
                     "4,5 m, 3 m) donen una ombra a mig camí entre dues marques."),
    ])


# ------------------------------------------------- 4 · la regla trencada --

B4 = [(3, 12, 2), (2, 10, 1), (4, 12, 3), (5, 20, 2), (2, 8, 1.5), (3, 15, 1), (2, 14, 1),
      (4, 20, 1.5), (3, 9, 2), (5, 30, 1), (2, 12, 2), (6, 24, 1.5), (1, 8, 1.2)]


def fila4(po, oo, pa):
    v = oo / po
    assert v == int(v), (po, oo)
    return [f"{num(po)} m · {num(oo)} m", f"{num(oo)} ÷ {num(po)} = {int(v)}", m(pa),
            f"{num(pa)} · {int(v)} = {m(exacte(pa * v))}"]


def frase4(pa, po, oo, diu):
    return f"Pal de {num(pa)} m amb {num(po)} m d'ombra; l'arbre fa {num(oo)} m d'ombra. «L'arbre fa {diu}.»"


def cas4(pa, po, oo, bo):
    """Una afirmació sobre l'arbre: la bona (pa · vegades) o la de restar les ombres."""
    v = int(oo / po)
    if bo:
        return (frase4(pa, po, oo, f"{num(pa)} · {v} = {m(exacte(pa * v))}"), ["Té raó", "No té raó"], 0)
    return (frase4(pa, po, oo, f"{num(oo)} − {num(po)} = {m(oo - po)} més que el pal"), ["Té raó", "No té raó"], 1)


B4R = [(2, 3, 12, False), (2, 3, 12, True), (1, 2, 10, False), (3, 4, 12, True), (2, 5, 20, False),
       (1, 3, 15, True), (1.5, 2, 8, False), (1, 2, 14, True), (2, 3, 9, False), (2, 4, 16, True),
       (1, 5, 30, False), (1.5, 6, 24, True), (2, 2, 12, False)]

bloc4 = dict(
    titol="Les ombres no es resten", mira=(4, 9),
    nota_sol="<b>La regla trencada de la unitat.</b> L'ombra del pal hi cap unes quantes vegades, i l'alçada "
             "també: es multiplica, no es resta. Si dubta, que dibuixi l'ombra partida en trossos iguals, "
             "com a la pàgina 9 de la fitxa.",
    acts=[
        act("Compta quantes vegades hi cap l'ombra del pal i calcula l'alçada de l'objecte.", [
            taula(["Ombres (pal · objecte)", "Hi cap", "Alçada del pal", "Alçada de l'objecte"],
                  [fila4(*f) for f in B4], omplir=(1, 3), amples=[24, 20, 18, 26])], ico="calc"),
        act("Marca si té raó qui ho diu.", [
            tria([cas4(*f) for f in B4R], en_linia=True)], repte=True,
            nota_sol="Les afirmacions que resten les ombres no tenen mai raó; les que multipliquen, sí. "
                     "Barrejades, i sense cap pista a l'enunciat."),
    ])


# ------------------------------------------------- 5 · a la vida de cada dia · l'escombra --

def fila5(po, pa, nom, oo):
    x, c = creu(po, pa, oo)
    return [nom, m(oo), c, m(x)]


bloc5 = dict(
    titol="A la vida de cada dia · l'escombra", mira=(5, 10),
    nota_sol="Al migdia les ombres són curtes i a la tarda són llargues, però l'edifici fa sempre 15 m: "
             "si a la mateixa activitat li surten alçades diferents per al mateix objecte, hi ha un error. "
             "<b>Error típic:</b> posar l'alçada de l'escombra (1,5) a la columna de l'ombra.",
    acts=[
        act("Calcula l'alçada de cada cosa del pati amb l'ombra de l'escombra.", [
            taula(["Què és", "Ombra", "Resolem", "Alçada"],
                  [fila5(2, 1.5, *f) for f in (("Edifici", 20), ("Porteria", 3.2), ("Arbre", 8), ("Fanal", 10))],
                  omplir=(2, 3), amples=[20, 14, 36, 18],
                  abans=nota("A les 10 h, l'escombra (1,5 m) fa una ombra de 2 m.")),
            taula(["Què és", "Ombra", "Resolem", "Alçada"],
                  [fila5(1, 1.5, *f) for f in (("Edifici", 10), ("Porteria", 1.6), ("Arbre", 4))],
                  omplir=(2, 3), amples=[20, 14, 36, 18],
                  abans=nota("A les 12 h, l'escombra fa una ombra d'1 m.")),
            taula(["Què és", "Ombra", "Resolem", "Alçada"],
                  [fila5(3, 1.5, *f) for f in (("Edifici", 30), ("Arbre", 12), ("Cistella", 6))],
                  omplir=(2, 3), amples=[20, 14, 36, 18],
                  abans=nota("A les 17 h, l'escombra fa una ombra de 3 m.")),
            taula(["Què és", "Ombra", "Resolem", "Alçada"],
                  [fila5(0.5, 1.5, *f) for f in (("Edifici", 5), ("Fanal", 2.5), ("Porteria", 0.8))],
                  omplir=(2, 3), amples=[20, 14, 36, 18],
                  abans=nota("A les 13 h, l'escombra fa una ombra de 0,5 m.")),
        ], ico="calc"),
        act("Calcula quina ombra fa cada cosa al costat del fanal.", [
            taula(["Què és", "Alçada", "Resolem", "Ombra"],
                  [[nom, m(a), f"6 · x = 9 · {num(a)} = {num(exacte(9 * a))}", m(exacte(9 * a / 6))]
                   for nom, a in (("La teva amiga", 1.6), ("Un gos", 0.4), ("Una bicicleta", 1), ("Un nen", 1.2),
                                  ("La porteria", 2.4), ("Un arbre", 8), ("La tanca", 2), ("La cistella", 3),
                                  ("Una furgoneta", 2.6), ("L'escombra", 1.5), ("Un cartell", 4),
                                  ("El professor", 1.8), ("Una palmera", 10))],
                  omplir=(2, 3), amples=[24, 14, 34, 16], esq=(0,),
                  abans=nota("Un fanal de 6 m fa una ombra de 9 m."))],
            ico="calc", repte=True,
            nota_sol="<b>Això és el que mostra si ho ha entès:</b> la x és a la columna de l'ombra, no a la de "
                     "l'alçada, com a l'exercici 5b de la fitxa. Totes les ombres fan una vegada i mitja "
                     "l'alçada, perquè 9 és una vegada i mitja 6."),
    ])


# ------------------------------------------------- 6 · Pitàgores amb la taula --

def pit(b, c):
    a = math.hypot(b, c)
    return a


def fila6(b, c, u=""):
    a = pit(b, c)
    assert abs(a - round(a, 2)) < 1e-9, (b, c)
    return [f"{num(b)} i {num(c)}", f"{num(b * b)} + {num(c * c)}", num(exacte(b * b + c * c)), num(round(a, 2)) + u]


B6 = [(3, 4), (6, 8), (5, 12), (9, 12), (12, 16), (8, 15), (15, 20), (7, 24), (10, 24), (20, 21),
      (12, 35), (9, 40), (16, 30)]
B6R = [(2, 3), (1, 2), (1, 3), (2, 4), (3, 5), (4, 5), (2, 5), (3, 7), (5, 6), (4, 7), (6, 7), (1, 5), (5, 8)]


def fila6r(b, c):
    q = b * b + c * c
    a = math.sqrt(q)
    assert abs(a * 10 % 1 - 0.5) > 0.05, (b, c)              # cap dubte en arrodonir
    return [f"{num(b)} i {num(c)}", f"{num(b * b)} + {num(c * c)}", num(q), f"√{num(q)} ≈ {num(round(a, 1))}"]


bloc6 = dict(
    titol="Pitàgores amb la taula", mira=(6, 12),
    nota_sol="Sempre a² = b² + c², amb <b>a</b> el costat llarg. <b>Error típic:</b> parar a a² i dir que "
             "a = 25. Cal l'arrel (tecla √ de la calculadora).",
    acts=[
        act("Calcula el costat llarg a amb a² = b² + c².", [
            taula(["b i c", "b² + c²", "a²", "a"], [fila6(*f) for f in B6], omplir=(1, 2, 3),
                  amples=[20, 26, 20, 22])], ico="calc"),
        act("Calcula el costat llarg a i arrodoneix-lo a les dècimes.", [
            taula(["b i c", "b² + c²", "a²", "a"], [fila6r(*f) for f in B6R], omplir=(1, 2, 3),
                  amples=[20, 24, 18, 26])], ico="calc", repte=True,
            nota_sol="Ara l'arrel no és exacta: la calculadora dona molts decimals i se'n deixa un. Accepteu "
                     "també el resultat amb dos decimals."),
    ])


# ------------------------------------------------- 7 · els casos --

B7 = [("Cable d'una tirolina", 8, 15, "m"), ("Cable d'una antena", 15, 20, "m"),
      ("Diagonal d'una pantalla", 30, 40, "cm"), ("Rampa del pàrquing", 7, 24, "m"),
      ("Diagonal d'un mòbil", 6, 8, "cm"), ("Diagonal d'un camp", 30, 40, "m"),
      ("Cable d'un pal de la llum", 9, 12, "m"), ("Diagonal d'una tauleta", 12, 16, "cm"),
      ("Corda d'una tenda", 1.2, 1.6, "m"), ("Diagonal d'una rajola", 15, 20, "cm"),
      ("Cable d'un fanal", 5, 12, "m"), ("Diagonal d'un llibre", 21, 28, "cm"), ("Tobogan", 2.4, 3.2, "m")]


def fila7(cas, b, c, u):
    return [cas, f"{num(b)} {u} i {num(c)} {u}", m(exacte(pit(b, c)), u)]


B7R = [("Una tirolina: una torre de 12 m, fins a 35 m del peu", 12, 35, "m"),
       ("Una antena de 16 m, amb un cable clavat a 12 m del peu", 12, 16, "m"),
       ("Una rampa que puja 0,7 m en 2,4 m", 0.7, 2.4, "m"),
       ("La diagonal d'un camp de 60 m per 80 m", 60, 80, "m"),
       ("Una pantalla de 36 cm per 48 cm", 36, 48, "cm"),
       ("Un pal de 6 m, amb un cable clavat a 8 m", 6, 8, "m"),
       ("Una tirolina: una torre de 9 m, fins a 40 m del peu", 9, 40, "m"),
       ("Un mòbil de 9 cm per 12 cm", 9, 12, "cm"),
       ("Una rampa que puja 1,5 m en 2 m", 1.5, 2, "m"),
       ("Una finestra de 0,9 m per 1,2 m", 0.9, 1.2, "m"),
       ("Un solar de 20 m per 21 m", 20, 21, "m"),
       ("Un pal de 15 m, amb un cable clavat a 8 m", 8, 15, "m"),
       ("Una tauleta de 18 cm per 24 cm", 18, 24, "cm")]


def fila7r(cas, b, c, u):
    return [cas, m(b, u), m(c, u), m(exacte(pit(b, c)), u)]


bloc7 = dict(
    titol="Els casos", mira=(7, 12),
    nota_sol="Pitàgores només quan els dos costats curts es coneixen de debò: es mesuren a terra o ja se "
             "saben (l'alçada d'una torre és als plànols). Mai per trobar una alçada que no es pot mesurar.",
    acts=[
        act("Calcula a, el costat llarg, de cada cas.", [
            taula(["Cas", "b i c", "a"], [fila7(*f) for f in B7], omplir=(2,), amples=[44, 26, 18],
                  esq=(0,))], ico="calc"),
        act("Troba b i c a cada frase i calcula el costat llarg a.", [
            taula(["Cas", "b", "c", "a"], [fila7r(*f) for f in B7R], omplir=(1, 2, 3), amples=[46, 14, 14, 14],
                  esq=(0,))], ico="calc", repte=True,
            nota_sol="Els números no surten ordenats en una taula: s'han de treure de la frase. L'ordre de b i "
                     "c no importa."),
    ])


# ------------------------------------------------- 8 · ombra o triangle --

OT = ["Ombra", "Triangle"]
O, T = 0, 1

B8 = [("L'alçada d'un arbre, un dia de sol.", O),
      ("El cable d'una tirolina, d'una torre de 12 m fins a 35 m.", T),
      ("L'alçada d'un fanal, amb una escombra al costat.", O),
      ("La diagonal d'un camp de 40 m per 30 m.", T),
      ("L'alçada del campanar del poble, al migdia.", O),
      ("La diagonal d'una pantalla de 30 cm per 40 cm.", T),
      ("L'alçada d'una grua, amb un pal d'1 m al costat.", O),
      ("Una rampa que puja 2 m en 5 m: quant fa de llarg?", T),
      ("L'alçada de l'institut, amb la teva ombra.", O),
      ("El cable d'una antena de 15 m, clavat a 20 m.", T),
      ("L'alçada d'una palmera, a la tarda.", O),
      ("La diagonal d'una bassa que pots vorejar.", T),
      ("L'alçada d'una xemeneia, amb un pal i el sol.", O)]


def ombra8(text, po, pa, oo):
    x, _ = creu(po, pa, oo)
    return [text, "Ombra", m(x)]


def tri8(text, b, c, u="m"):
    return [text, "Triangle", m(exacte(pit(b, c)), u)]


B8R = [ombra8("Arbre: pal de 2 m amb 3 m d'ombra; l'arbre fa 12 m d'ombra", 3, 2, 12),
       tri8("Tirolina: torre de 12 m, fins a 35 m del peu", 12, 35),
       ombra8("Fanal: escombra d'1,5 m amb 2 m d'ombra; el fanal fa 8 m d'ombra", 2, 1.5, 8),
       tri8("La diagonal d'un camp de 40 m per 30 m", 30, 40),
       ombra8("Campanar: pal d'1 m amb 2 m d'ombra; el campanar fa 40 m d'ombra", 2, 1, 40),
       tri8("La diagonal d'una pantalla de 30 cm per 40 cm", 30, 40, "cm"),
       ombra8("Grua: pal d'1 m amb 0,5 m d'ombra; la grua fa 15 m d'ombra", 0.5, 1, 15),
       tri8("Una rampa que puja 7 m en 24 m", 7, 24),
       ombra8("Institut: tu fas 1,6 m i 2 m d'ombra; l'institut fa 15 m d'ombra", 2, 1.6, 15),
       tri8("Una antena de 15 m, amb un cable clavat a 20 m", 15, 20),
       ombra8("Palmera: pal de 2 m amb 4 m d'ombra; la palmera fa 18 m d'ombra", 4, 2, 18),
       tri8("La diagonal d'una bassa de 10 m per 24 m", 10, 24),
       ombra8("Xemeneia: pal de 3 m amb 2 m d'ombra; la xemeneia fa 10 m d'ombra", 2, 3, 10)]

bloc8 = dict(
    titol="Ombra o triangle?", mira=(8, 13),
    nota_sol="Una alçada que no es pot mesurar, amb sol o amb un pal al costat → ombra. Un angle recte amb "
             "dos costats que es coneixen → triangle. L'error que delata és fer servir Pitàgores per a una "
             "alçada.",
    acts=[
        act("Marca el camí per calcular-ho: ombra o triangle.", [
            tria([(t, OT, r) for t, r in B8], en_linia=True)]),
        act("Tria el camí i calcula-ho.", [
            taula(["Què vull saber", "Camí", "Resultat"], B8R, omplir=(1, 2), amples=[56, 16, 16], esq=(0,))],
            ico="calc", repte=True,
            nota_sol="Un pas més que la fitxa: a més de triar, calcular. Si tria bé i calcula malament, el que "
                     "falla és el compte, no la decisió."),
    ])


# ------------------------------------------------- 9 · a la vida de cada dia · les diagonals --

B9 = [("Bassa", 6, 8), ("Bassa", 10, 24), ("Camp", 30, 40), ("Pati", 12, 16), ("Piscina", 9, 12),
      ("Hort", 5, 12), ("Pista", 20, 21), ("Jardí", 8, 15), ("Plaça", 24, 32), ("Terrassa", 3, 4),
      ("Parc", 60, 80), ("Solar", 7, 24), ("Bassa", 15, 20)]


def fila9(nom, b, c):
    return [nom, f"{num(b)} m per {num(c)} m"] + fila6(b, c, " m")[1:]


B9R = [(1.2, 1.6, 1.8), (0.6, 0.8, 1.2), (1.5, 2, 2.4), (0.9, 1.2, 1.6), (1.8, 2.4, 2.8), (0.7, 2.4, 2.6),
       (1, 2.4, 2.8), (0.5, 1.2, 1.2), (2, 2.1, 3), (0.8, 1.5, 1.6), (1.2, 3.5, 3.8), (0.9, 4, 4),
       (1.6, 3, 3.5)]


def fila9r(b, c, t):
    d = exacte(pit(b, c))
    assert abs(d - t) > 1e-9, (b, c, t)                    # cap empat
    return [f"{num(b)} m per {num(c)} m", m(d), m(t), "Sí" if t < d else "No"]


bloc9 = dict(
    titol="A la vida de cada dia · les diagonals", mira=(9, 14),
    nota_sol="La diagonal d'un rectangle és el costat llarg del triangle que fan dos costats seguits. Els "
             "costats es poden mesurar caminant; la diagonal, no sempre.",
    acts=[
        act("Calcula la diagonal a de cada lloc.", [
            taula(["Lloc", "Costats", "b² + c²", "a²", "a"], [fila9(*f) for f in B9], omplir=(2, 3, 4),
                  amples=[13, 27, 18, 13, 17])], ico="calc"),
        act("Calcula la diagonal del forat i digues si el tauler hi passa de biaix.", [
            taula(["Forat", "Diagonal", "Tauler", "Hi passa?"], [fila9r(*f) for f in B9R], omplir=(1, 3),
                  amples=[30, 20, 18, 20],
                  abans=nota("Un tauler prim hi passa de biaix si és més curt que la diagonal del forat."))],
            ico="calc", repte=True,
            nota_sol="Una decisió nova: comparar la diagonal amb el tauler. Hi passa quan el tauler és més curt "
                     "que la diagonal. Hi ha tant «Sí» com «No», barrejats."),
    ])


# ------------------------------------------------- 10 · a la vida de cada dia · la drecera --

B10 = [(12, 16), (6, 8), (9, 12), (5, 12), (8, 15), (15, 20), (7, 24), (20, 21), (30, 40), (10, 24),
       (24, 32), (12, 35), (9, 40)]


def fila10(b, c):
    d = round(pit(b, c))
    return [f"{num(b)} m per {num(c)} m", f"{num(b)} + {num(c)} = {m(b + c)}", m(d), f"{num(b + c)} − {num(d)} = {m(b + c - d)}"]


B10R = [(12, 16, 10), (6, 8, 10), (9, 12, 4), (5, 12, 6), (8, 15, 2), (15, 20, 4), (7, 24, 10),
        (20, 21, 2), (30, 40, 6), (10, 24, 4), (24, 32, 2), (12, 35, 6), (9, 40, 10)]


def fila10r(b, c, v):
    d = round(pit(b, c))
    e = b + c - d
    return [f"{num(b)} m per {num(c)} m", m(e), str(v), f"{num(e)} · {v} = {m(e * v)}"]


bloc10 = dict(
    titol="A la vida de cada dia · la drecera", mira=(10, 14),
    nota_sol="<b>Això és el que mostra si ho ha entès:</b> la resposta no és la diagonal sola, sinó "
             "comparar-la amb el camí per les parets (b + c).",
    acts=[
        act("Calcula quants metres t'estalvies anant per la diagonal del pati.", [
            taula(["Pati", "Per les parets", "En diagonal", "T'estalvies"], [fila10(*f) for f in B10],
                  omplir=(1, 2, 3), amples=[26, 22, 16, 24])], ico="calc"),
        act("Calcula quants metres t'estalvies en tota una setmana.", [
            taula(["Pati", "En un viatge", "Viatges", "En una setmana"], [fila10r(*f) for f in B10R],
                  omplir=(1, 3), amples=[26, 18, 14, 30])], ico="calc", repte=True,
            nota_sol="Un pas més: l'estalvi d'un viatge (parets − diagonal) multiplicat pels viatges de la "
                     "setmana."),
    ])


BLOCS = [bloc1, bloc2, bloc3, bloc4, bloc5, bloc6, bloc7, bloc8, bloc9, bloc10]
