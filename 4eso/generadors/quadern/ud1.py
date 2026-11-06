"""Quadern d'activitats de la Unitat 1 · Nombres reals des de l'estimació.

    python3 4eso/generadors/gen_quadern.py 1        (des de l'arrel)

Un bloc per cada exercici de la fitxa (u1/fitxa.html), en el mateix ordre. A cada bloc, una
activitat germana i una de repte. Cada activitat té 13 apartats: l'a), resolt, i 12 per fer.
El filtre en deixa 3 (petit), 6 (mitjà) o tots 12 (elevat), sempre els primers.

Com a la fitxa: la calculadora dona el número, i l'alumnat decideix (entre quins enters cau, on és
a la recta, quants decimals cal escriure, amunt o avall). La regla trencada de la unitat, arrodonir
no és tallar (2,6457… a 2 decimals és 2,65, no 2,64), surt ja entre els tres primers apartats del
bloc 3. Els números es calculen aquí: el solucionari no es pot equivocar.
"""
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN

from quadern import act, taula, tria, nota, llista, ms, num, eur
from peces import recta

NUM = 1
TITOL = "Nombres reals des de l'estimació"   # el de dades/unitats.js (decisió V2)
AVALUAR = ("Com a la fitxa, el càlcul el fa la calculadora: el que s'avalua és la decisió. Entre quins "
           "enters cau un nombre, on és a la recta, quants decimals té sentit escriure i si cal arrodonir "
           "amunt o avall. L'error que importa és tallar en lloc d'arrodonir (bloc 3). Les activitats de "
           "repte compten per als nivells alts (AN, AE), no per al mínim.")


def d(x):
    return Decimal(repr(x))


def surt(x, k=7):
    """El que surt a la calculadora, tallat i amb punts suspensius: 2,6457513…"""
    return f"{d(x).quantize(Decimal(1).scaleb(-k), ROUND_DOWN)}…".replace(".", ",")


def arr(x, k):
    """Arrodonit a k decimals, amb els zeros del final (1,70)."""
    return str(d(x).quantize(Decimal(1).scaleb(-k), ROUND_HALF_UP)).replace(".", ",")


def tall(x, k):
    return str(d(x).quantize(Decimal(1).scaleb(-k), ROUND_DOWN)).replace(".", ",")


def arrel(n):
    return f"√{n}"


# ------------------------------------------------- 1 · entre quins dos enters --

ENTRE = (10, 3, 15, 40, 2, 50, 20, 60, 90, 12, 99, 72, 150)

bloc1 = dict(
    titol="Entre quins dos enters", mira=(1, 4),
    nota_sol="Primer la calculadora, després la decisió: el número enter de davant de la coma és el de sota, "
             "i el següent, el de sobre. <b>Error típic:</b> confondre el número de dins de l'arrel amb el "
             "resultat (√15 entre 14 i 16).",
    acts=[
        act("Escriu entre quins dos nombres enters cau cada nombre.", [
            taula(["Número", "Surt", "Entre", "i"],
                  [[arrel(n), surt(math.sqrt(n)), str(int(math.sqrt(n))), str(int(math.sqrt(n)) + 1)]
                   for n in ENTRE], omplir=(1, 2, 3), amples=[18, 34, 18, 18])], ico="calc"),
        act("Sense calculadora: busca els dos quadrats i escriu entre quins enters cau.", [
            taula(["Número", "El quadrat de sota", "El de sobre", "Entre", "i"],
                  [[arrel(n), f"{r * r} = {r}²", f"{(r + 1) ** 2} = {r + 1}²", str(r), str(r + 1)]
                   for n in (20, 10, 30, 50, 5, 70, 40, 90, 13, 60, 99, 80, 3) for r in [int(math.sqrt(n))]],
                  omplir=(1, 2, 3, 4), amples=[14, 22, 22, 15, 15],
                  abans=nota("Els quadrats: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100."))],
            repte=True,
            nota_sol="El camí sense calculadora, com el de 1r: √20 és entre √16 i √25, o sigui entre 4 i 5. "
                     "Després la calculadora ho pot comprovar."),
    ])


# ------------------------------------------------- 2 · a la recta --

RECTA = (7, 5, 30, 3, 11, 20, 2, 45, 8, 14, 60, 18, 85)


def marca(lletra, n, resolt):
    x = math.sqrt(n)
    a = int(x)
    txt = f'<div style="flex:1 1 auto;margin-top:.3rem"><b>{arrel(n)}</b> = {surt(x)}</div>'
    return f'{lletra}{txt}<div style="flex:0 0 100%">{recta(a, x if resolt else None, ma=True)}</div>'


def sol_recta(n):
    x = d(math.sqrt(n))
    sota = x.quantize(Decimal("0.1"), ROUND_DOWN)
    return f"{arrel(n)} = {surt(math.sqrt(n), 3)}, entre {str(sota).replace('.', ',')} i {str(sota + Decimal('0.1')).replace('.', ',')}"


LLEGIR = (2.6, 3.4, 1.8, 5.5, 0.3, 4.7, 7.2, 2.15, 6.85, 1.05, 8.45, 3.95, 9.65)


def llegeix(lletra, x, resolt):
    a = int(x)
    resp = (ms(num(x)) if resolt else '<span class="buit" style="min-width:3cm"></span>')
    return f'{lletra}{recta(a, x)}<div class="resposta">La creu és al {resp}</div>'


bloc2 = dict(
    titol="On cau el número?", mira=(2, 4),
    nota_sol="La recta va d'un enter al següent i està partida en desenes: la primera xifra decimal diu quina "
             "ratlla. Es dona per bo qualsevol punt entre la desena de sota i la de sobre (√7 = 2,64…: entre el "
             "2,6 i el 2,7).",
    acts=[
        act("Marca amb una creu on cau cada nombre a la recta.", [
            llista(RECTA, marca, sol_recta)],
            ico="calc"),
        act("Ara al revés: escriu el número que marca cada creu.", [
            llista(LLEGIR, llegeix, num)],
            repte=True,
            nota_sol="El camí al revés: de la recta al número. Les dels apartats h, i, j, k, l i m cauen entre dues "
                     "ratlles: es dona per bona qualsevol de les dues desenes, o el número del mig."),
    ])


# ------------------------------------------------- 3 · arrodonir --

ARROD = (math.sqrt(7), math.sqrt(3), 12 / 7, math.pi, math.sqrt(2), 25 / 6, math.sqrt(19), 2 / 3,
         math.sqrt(48), 17 / 9, math.sqrt(99), 50 / 7, math.sqrt(120))

bloc3 = dict(
    titol="Arrodonir", mira=(3, 5),
    nota_sol="<b>La regla trencada de la unitat:</b> arrodonir no és tallar. Ja a l'apartat b (1,7320… a 0 decimals és 2, no 1) "
             "i a la c (1,7142… → 2) cal mirar la xifra següent. Si talla, recordeu-li que "
             "2,646 és més a prop del 2,65 que del 2,64. Els zeros del final (1,70) es mantenen.",
    acts=[
        act("Arrodoneix cada nombre amb els decimals que et demanen.", [
            taula(["Número", "0 decimals", "1 decimal", "2 decimals"],
                  [[surt(x), arr(x, 0), arr(x, 1), arr(x, 2)] for x in ARROD],
                  omplir=(1, 2, 3), amples=[28, 20, 20, 20])], ico="calc"),
        act("Talla i arrodoneix a 2 decimals. Marca si surt el mateix.", [
            taula(["Número", "Tallat", "Arrodonit", "El mateix?"],
                  [[surt(x), tall(x, 2), arr(x, 2), "sí" if tall(x, 2) == arr(x, 2) else "no"]
                   for x in (math.sqrt(7), math.sqrt(10), 2 / 3, math.sqrt(5), 4 / 9, math.sqrt(8), math.pi,
                             5 / 7, math.sqrt(13), 1 / 6, math.sqrt(50), 7 / 3, math.sqrt(17))],
                  omplir=(1, 2, 3), amples=[28, 20, 20, 20])],
            ico="calc", repte=True,
            nota_sol="Un pas més: les dues coses de costat. Surt el mateix quan la xifra següent és 0, 1, 2, 3 o 4; "
                     "si és 5 o més, l'arrodonit és més gran. Que miri sempre la tercera xifra decimal."),
    ])


# ------------------------------------------------- 4 · decimals que s'acaben --

def opcions_arrel(ns):
    exactes = [n for n in ns if math.isqrt(n) ** 2 == n]
    assert len(exactes) == 1, ns
    return ("", [arrel(n) for n in ns], ns.index(exactes[0]))


OPC4 = [(20, 49, 8, 3), (6, 15, 64, 2), (100, 50, 30, 7), (5, 11, 13, 81), (10, 36, 40, 27), (12, 18, 24, 121),
        (45, 144, 60, 90), (400, 200, 80, 300), (14, 21, 26, 169), (75, 99, 225, 150), (500, 900, 600, 700),
        (31, 33, 35, 196), (1000, 2500, 3000, 2000)]


def acaba(text, val, s):
    return [text, "sí" if s else "no", val]


ACABEN = [acaba("√49", "7", True), acaba("√50", surt(math.sqrt(50)), False), acaba("1 ÷ 4", "0,25", True),
          acaba("1 ÷ 3", surt(1 / 3), False), acaba("√81", "9", True), acaba("√10", surt(math.sqrt(10)), False),
          acaba("3 ÷ 4", "0,75", True), acaba("2 ÷ 3", surt(2 / 3), False), acaba("π", surt(math.pi), False),
          acaba("√144", "12", True), acaba("1 ÷ 8", "0,125", True), acaba("5 ÷ 6", surt(5 / 6), False),
          acaba("√2,25", "1,5", True)]

bloc4 = dict(
    titol="Decimals que s'acaben", mira=(4, 5),
    nota_sol="Només són exactes les arrels dels quadrats perfectes (1, 4, 9, 16, 25, 36, 49, 64, 81, 100…). Si en "
             "falla més d'un, val la pena repassar la llista de quadrats.",
    acts=[
        act("Marca el nombre que té xifres decimals que s'acaben.", [
            tria([(f"Quina arrel s'acaba?", o[1], o[2]) for o in (opcions_arrel(list(x)) for x in OPC4)],
                 en_linia=True,
                 sol_nota="Són els quadrats perfectes: " + " · ".join(
                     f"√{x} = {math.isqrt(x)}" for t in OPC4 for x in t if math.isqrt(x) ** 2 == x) + ".")],
            ico="calc"),
        act("Fes-ho amb la calculadora. S'acaba? Escriu què surt.", [
            taula(["Número", "S'acaba?", "Surt"], ACABEN, omplir=(1, 2), amples=[26, 22, 40])],
            ico="calc", repte=True,
            nota_sol="Un pas més: també les divisions. 1 ÷ 4 s'acaba (0,25); 1 ÷ 3 no (0,333…). Si la calculadora "
                     "omple la pantalla i l'última xifra no s'atura, no s'acaba."),
    ])


# ------------------------------------------------- 5 · quants decimals --

PER = {0: "per metres sencers", 1: "per pams de 10 cm", 2: "per centímetres", 3: "per mil·límetres"}


def precisio(que, x, k, altres):
    ops = sorted({k} | set(altres))
    return (f"{que}: {surt(x, 5)} m. Es mesura {PER[k]}.", [f"{arr(x, j)} m" for j in ops], ops.index(k))


PRECISIO = [precisio("Una cortina", 2.34567, 2, (1, 3)), precisio("Un tauler", 1.23456, 3, (1, 2)),
            precisio("Una corda", 4.28571, 0, (1, 2)), precisio("Un cable", 3.16227, 1, (0, 2)),
            precisio("Una tela", 1.69705, 2, (1, 3)), precisio("Un llistó", 0.89442, 3, (1, 2)),
            precisio("Una tanca", 12.6491, 0, (1, 2)), precisio("Una catifa", 2.44948, 1, (0, 2)),
            precisio("Un tub", 1.41421, 3, (1, 2)), precisio("Una cinta", 5.47722, 2, (0, 1)),
            precisio("Una barra", 2.64575, 1, (2, 3)), precisio("Un vidre", 0.70710, 3, (1, 2)),
            precisio("Una mànega", 8.36660, 0, (1, 2))]


def qd(que, x, k):
    return [que, surt(x, 5), PER[k], f"{arr(x, k)} m"]


bloc5 = dict(
    titol="Quants decimals?", mira=(5, 6),
    nota_sol="Com la pàgina 3 de la fitxa: quants decimals depèn de com es mesura. En metres, la primera xifra "
             "decimal són els pams de 10 cm, la segona els centímetres i la tercera els mil·límetres.",
    acts=[
        act("Marca com ho escriuries.", [tria(PRECISIO, en_linia=True)], ico="calc"),
        act("Escriu-ho amb els decimals que calen.", [
            taula(["Què és", "Surt", "Es mesura", "Ho escric"],
                  [qd(*r) for r in (("Una cortina", 1.73205, 2), ("Un tauler", 2.23606, 3), ("Una corda", 3.60555, 0),
                                    ("Una tela", 0.94868, 1), ("Un cable", 4.47213, 2), ("Un llistó", 1.11803, 3),
                                    ("Una tanca", 9.48683, 0), ("Una catifa", 2.82842, 1), ("Un tub", 0.31622, 3),
                                    ("Una cinta", 6.32455, 2), ("Una barra", 3.87298, 1), ("Una mànega", 15.4919, 0),
                                    ("Un vidre", 1.95959, 3))],
                  omplir=(3,), amples=[20, 20, 28, 20], esq=(0,))],
            ico="calc", repte=True,
            nota_sol="Ara no hi ha opcions: ha d'arrodonir ell, i amb els zeros que calguin. <b>Error típic:</b> "
                     "a «per mil·límetres», escriure 2,236 com a 2,24."),
    ])


# ------------------------------------------------- 6 · pagar de més --

def eurd(x):
    return str(x.quantize(Decimal("0.01"), ROUND_HALF_UP)).replace(".", ",") + " €"


def corda(m, preu):
    compres = math.ceil(m)
    costa, paga = d(m) * d(preu), d(compres) * d(preu)
    return [f"{num(m)} m", eurd(costa), f"{compres} m", eurd(paga), eurd(paga - costa.quantize(Decimal("0.01"), ROUND_HALF_UP))]


def rotlles(m, llarg, preu):
    n = math.ceil(m / llarg)
    return [f"{num(m)} m", str(n), eur(n * preu), f"{num(round(n * llarg - m, 2))} m"]


CAP6 = ["Necessites", "Costa", "Compres", "Pagues", "De més"]
A6 = [18, 18, 17, 18, 17]

bloc6 = dict(
    titol="Pagar de més", mira=(6, 7),
    nota_sol="Es compra per metres sencers, sempre cap amunt. El que es paga de més és la diferència entre el que "
             "pagues i el que costaria exactament. <b>Error típic:</b> arrodonir cap avall (3,7 m → 3 m) i quedar-se curt.",
    acts=[
        act("Calcula quants diners de més pagues si arrodoneixes cap amunt.", [
            taula(CAP6, [corda(m, 2.35) for m in (3.7, 5.2, 2.4, 1.5)], omplir=(1, 2, 3, 4), amples=A6,
                  abans=nota("La corda val 2,35 € el metre.")),
            taula(CAP6, [corda(m, 1.80) for m in (4.5, 2.2, 6.8)], omplir=(1, 2, 3, 4), amples=A6,
                  abans=nota("El cable val 1,80 € el metre.")),
            taula(CAP6, [corda(m, 4.50) for m in (1.3, 3.6, 2.9, 0.4, 7.1, 5.5)], omplir=(1, 2, 3, 4), amples=A6,
                  abans=nota("La tela val 4,50 € el metre.")),
        ], ico="calc"),
        act("Es ven en rotlles sencers. Quants en compres i quants metres et sobren?", [
            taula(["Necessites", "Rotlles", "Pagues", "Et sobren"],
                  [rotlles(m, 5, 9) for m in (7, 12, 4.5, 16)], omplir=(1, 2, 3), amples=[22, 22, 22, 22],
                  abans=nota("Els rotlles de cable són de 5 m i valen 9 €.")),
            taula(["Necessites", "Rotlles", "Pagues", "Et sobren"],
                  [rotlles(m, 10, 15) for m in (23, 8, 31)], omplir=(1, 2, 3), amples=[22, 22, 22, 22],
                  abans=nota("Els rotlles de tela són de 10 m i valen 15 €.")),
            taula(["Necessites", "Rotlles", "Pagues", "Et sobren"],
                  [rotlles(m, 2.5, 4) for m in (6, 3, 8.2, 1.5, 11, 5)], omplir=(1, 2, 3), amples=[22, 22, 22, 22],
                  abans=nota("Els rotlles de cinta són de 2,5 m i valen 4 €.")),
        ], ico="calc", repte=True,
            nota_sol="Un pas més: ja no es compra per metres sinó per rotlles. Primer cal dividir (7 ÷ 5 = 1,4) i "
                     "arrodonir cap amunt (2 rotlles). Els que sobren són els que es poden guardar."),
    ])


# ------------------------------------------------- 7 · amunt o avall --

def amunt(text, a, b, sentit, que):
    x = a / b
    r = math.ceil(x) if sentit == "amunt" else math.floor(x)
    return [text, f"{num(round(x, 2)) if x == round(x, 2) else surt(x, 2)}", sentit, f"{r} {que}"]


VIDA = [amunt("Necessites 7 L de pintura. Els pots són de 2 L.", 7, 2, "amunt", "pots"),
        amunt("Sou 22 persones. A cada cotxe hi caben 5.", 22, 5, "amunt", "cotxes"),
        amunt("Tens 11 €. Una entrada de cine val 3 €.", 11, 3, "avall", "entrades"),
        amunt("Sou 30 alumnes. A cada taula hi caben 4.", 30, 4, "amunt", "taules"),
        amunt("Tens 20 €. Un llibre val 6 €.", 20, 6, "avall", "llibres"),
        amunt("Tens 50 m de corda. Cada comba necessita 3 m.", 50, 3, "avall", "combes"),
        amunt("Has de portar 45 cadires. En una furgoneta n'hi caben 10.", 45, 10, "amunt", "viatges"),
        amunt("Tens 2 L de suc. Cada got és de 0,3 L.", 2, 0.3, "avall", "gots plens"),
        amunt("Hi ha 63 ous. Les capses són de 12.", 63, 12, "amunt", "capses"),
        amunt("Tens 15 €. Un pa val 1,20 €.", 15, 1.2, "avall", "pans"),
        amunt("Sou 52 persones. Un autobús és de 25 places.", 52, 25, "amunt", "autobusos"),
        amunt("Tens 7 m de tela. Cada coixí en necessita 0,8 m.", 7, 0.8, "avall", "coixins"),
        amunt("Has de llegir 130 pàgines. Cada dia en llegeixes 15.", 130, 15, "amunt", "dies")]


def sobra(text, a, b, que, unitat):
    n = math.ceil(a / b)
    return [text, str(n), f"{num(round(n * b - a, 2))} {unitat}"]


bloc7 = dict(
    titol="A la vida de cada dia · amunt o avall", mira=(7, 8),
    nota_sol="<b>La regla trencada:</b> no sempre s'arrodoneix cap amunt. Ja a l'apartat c (les entrades) cal "
             "anar cap avall: amb 11 € no arribes a la quarta. Si arrodoneix sempre amunt, que digui en veu alta "
             "si li arriben els diners.",
    acts=[
        act("Fes la divisió i decideix si has d'arrodonir cap amunt o cap avall.", [
            taula(["Situació", "Surt", "Amunt o avall?", "Resposta"], VIDA, omplir=(1, 2, 3),
                  amples=[44, 14, 15, 15], esq=(0,))], ico="calc"),
        act("Calcula quants en calen i quantes places sobren.", [
            taula(["Situació", "En calen", "Sobren"],
                  [sobra(*r) for r in (
                      ("Sou 22 persones. A cada cotxe hi caben 5.", 22, 5, "cotxes", "places"),
                      ("Sou 30 alumnes. A cada taula hi caben 4.", 30, 4, "taules", "places"),
                      ("Sou 52 persones. Els autobusos són de 25.", 52, 25, "autobusos", "places"),
                      ("Hi ha 63 ous. Les capses són de 12.", 63, 12, "capses", "llocs"),
                      ("Has de portar 45 cadires. En una furgoneta n'hi caben 10.", 45, 10, "viatges", "llocs"),
                      ("Sou 17 persones. Les barques són de 4.", 17, 4, "barques", "places"),
                      ("Sou 40 persones. Les taules són de 6.", 40, 6, "taules", "places"),
                      ("Hi ha 100 llibres. Cada caixa en porta 8.", 100, 8, "caixes", "llocs"),
                      ("Sou 75 persones. Un vagó és de 20 seients.", 75, 20, "vagons", "seients"),
                      ("Sou 33 persones. Les tendes són de 4.", 33, 4, "tendes", "llocs"),
                      ("Hi ha 58 pomes. Les bosses són de 6.", 58, 6, "bosses", "llocs"),
                      ("Sou 120 persones. Els autobusos són de 55.", 120, 55, "autobusos", "places"),
                      ("Hi ha 26 ampolles. Les caixes són de 6.", 26, 6, "caixes", "llocs"))],
                  omplir=(1, 2), amples=[56, 16, 16], esq=(0,))],
            ico="calc", repte=True,
            nota_sol="Un pas més: després d'arrodonir amunt, quant sobra. 22 ÷ 5 = 4,4 → 5 cotxes, i 5 × 5 = 25 "
                     "places: en sobren 3."),
    ])


BLOCS = [bloc1, bloc2, bloc3, bloc4, bloc5, bloc6, bloc7]
