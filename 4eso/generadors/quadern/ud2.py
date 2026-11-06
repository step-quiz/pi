"""Quadern d'activitats de la Unitat 2 · Percentatges i matemàtica financera.

    python3 4eso/generadors/gen_quadern.py 2        (des de l'arrel)

Un bloc per cada exercici de la fitxa (u2/fitxa.html), en el mateix ordre. A cada bloc, una
activitat germana i una de repte. Cada activitat té 13 apartats: l'a), resolt, i 12 per fer.

Com a la fitxa, tot passa pel factor (− 20 % → × 0,8; + 21 % → × 1,21): una sola multiplicació
dona el preu final. La regla trencada de la unitat, el pagament al comptat no sempre surt més
barat, surt ja entre els tres primers apartats del bloc 5. Els imports es calculen aquí amb
decimals exactes (Decimal), arrodonits al cèntim: el solucionari no es pot equivocar.
"""
from decimal import Decimal, ROUND_HALF_UP

from quadern import act, taula, nota

NUM = 2
TITOL = "Percentatges i matemàtica financera"   # el de dades/unitats.js (decisió V2)
AVALUAR = ("Com a la fitxa, el que s'avalua és el factor i la decisió: escriure el factor de cada canvi, "
           "fer servir una sola multiplicació i comparar dues maneres de pagar amb els dos comptes fets. Un "
           "error de calculadora no hauria de fer baixar la valoració si el factor és bo. Les activitats de "
           "repte compten per als nivells alts (AN, AE), no per al mínim.")

M = "−"
C = Decimal("0.01")


def D(x):
    return Decimal(str(x))


def fmt(x):
    """Un decimal en català, sense zeros de sobra: 0,8 · 1,21 · 0,968."""
    t = format(D(x).normalize(), "f")
    return t.replace(".", ",")


NB = "\u00a0"   # espai que no parteix la línia: «300 €», «− 20 %»


def eur(x):
    """Un import arrodonit al cèntim: 290,40 €. Els preus de partida sencers, sense cèntims: 300 €."""
    v = D(x)
    if v == v.to_integral_value() and v >= 0 and len(str(int(v))) <= 4 and not isinstance(x, Decimal):
        return f"{int(v)}{NB}€"
    return str(v.quantize(C, ROUND_HALF_UP)).replace(".", ",") + f"{NB}€"


def pct(p):
    """Un canvi en %: -20 → «− 20 %», 21 → «+ 21 %»."""
    return f"{M if p < 0 else '+'}{NB}{fmt(abs(p))}{NB}%"


def factor(p):
    return 1 + D(p) / 100


def xf(p):
    return f"×{NB}{fmt(factor(p))}"


def compte_f(p):
    """El compte que porta al factor, com a la fitxa: 1 − 0,20 · 1 + 0,21 · 1 − 0,05."""
    q = (D(abs(p)) / 100).quantize(C)
    return f"1 {M if p < 0 else '+'} {str(q).replace('.', ',')}"


def final(preu, *canvis):
    v = D(preu)
    for p in canvis:
        v = (v * factor(p)).quantize(C, ROUND_HALF_UP)
    return v


# ------------------------------------------------- 1 · el factor --

CANVIS1 = (-20, 21, -50, 10, -5, -30, 15, -25, 4, -15, 50, -12, 100)
FACTORS1 = (0.75, 1.21, 0.6, 1.1, 0.95, 1.5, 0.9, 1.04, 0.85, 1.3, 0.4, 1.07, 0.99)

bloc1 = dict(
    titol="El factor de cada canvi", mira=(1, 4),
    nota_sol="Si baixa, 1 menys; si puja, 1 més. <b>Error típic:</b> escriure × 0,5 per a un − 5 % (confondre "
             "0,05 amb 0,5). Que llegeixi el percentatge en veu alta: «cinc centèsimes».",
    acts=[
        act("Escriu el factor que correspon a cada canvi de preu.", [
            taula(["Canvi", "Compte", "Factor"], [[pct(p), compte_f(p), xf(p)] for p in CANVIS1],
                  omplir=(1, 2), amples=[28, 30, 30])]),
        act("Ara al revés: escriu quin canvi de preu fa cada factor.", [
            taula(["Factor", "Puja o baixa?", "Canvi"],
                  [[f"× {fmt(f)}", "baixa" if f < 1 else "puja", pct((D(f) - 1) * 100)] for f in FACTORS1],
                  omplir=(1, 2), amples=[28, 30, 30])],
            repte=True,
            nota_sol="El camí al revés: per sota d'1, baixa; per sobre, puja. El que falta per arribar a 1 (o el que "
                     "en sobra) és el percentatge: × 0,75 → − 25 %. <b>Error típic:</b> × 1,04 → + 40 %."),
    ])


# ------------------------------------------------- 2 · un canvi --

UN = ((300, -20), (80, 21), (45, -10), (120, 10), (60, -25), (250, 21), (90, -50), (15, 10), (400, -15),
      (35, 21), (1200, -5), (64, -30), (19.90, 21))
ABANS = ((240, -20), (96.80, 21), (40.50, -10), (132, 10), (45, -25), (121, 21), (50, -50), (210, -30),
         (66, 10), (340, -15), (60.50, 21), (85.50, -5), (24.20, 21))

bloc2 = dict(
    titol="Un sol canvi", mira=(2, 4),
    nota_sol="El factor ja dona el preu final: no cal calcular el descompte i restar-lo. <b>Error típic:</b> "
             "multiplicar per 0,2 en lloc de 0,8 i quedar-se amb el descompte.",
    acts=[
        act("Calcula el preu final amb el factor.", [
            taula(["Preu", "Canvi", "Factor", "Preu final"],
                  [[eur(p), pct(c), xf(c), eur(final(p, c))] for p, c in UN],
                  omplir=(2, 3), amples=[22, 22, 22, 22])], ico="calc"),
        act("Ara al revés: saps el preu final. Quant valia abans?", [
            taula(["Preu final", "Canvi", "Factor", "Abans valia"],
                  [[eur(p), pct(c), xf(c), eur(D(p) / factor(c))] for p, c in ABANS],
                  omplir=(2, 3), amples=[22, 22, 22, 22],
                  abans=nota("Per tornar enrere, divideix pel factor."))],
            ico="calc", repte=True,
            nota_sol="El camí al revés: si per anar es multiplica pel factor, per tornar es divideix (240 ÷ 0,8 = "
                     "300). <b>Error típic:</b> sumar-hi el 20 % (240 + 48 = 288)."),
    ])


# ------------------------------------------------- 3 · dos canvis --

DOS = ((300, -20, 21), (200, -30, 21), (50, 21, -10), (100, -10, -10), (400, -25, 10), (80, -50, 21),
       (150, 10, -20), (60, -15, 21), (500, 20, -20), (250, -40, 10), (90, 21, -25), (1000, -5, -10),
       (36, 50, -50))
UNIC = ((-20, 21), (-10, -10), (-30, 21), (10, -10), (-25, 10), (-50, 21), (20, -20), (-15, 10), (-5, 21),
        (50, -50), (-40, 50), (21, -21), (-10, -20))


def un_sol(a, b):
    f = factor(a) * factor(b)
    canvi = (f - 1) * 100
    return [f"{pct(a)} i {pct(b)}", f"{xf(a)}   {xf(b)}", f"× {fmt(f)}", pct(canvi)]


bloc3 = dict(
    titol="Dos canvis seguits", mira=(3, 5),
    nota_sol="Multiplica pel primer factor i, al resultat, pel segon. <b>La trampa:</b> − 20 % i + 21 % no és "
             "+ 1 %. Si suma els percentatges, que compari el seu resultat amb el de la calculadora.",
    acts=[
        act("Calcula el preu final quan hi ha dos canvis seguits.", [
            taula(["Preu", "1r canvi", "2n canvi", "Els dos factors", "Preu final"],
                  [[eur(p), pct(a), pct(b), f"{xf(a)}   {xf(b)}", eur(final(p, a, b))] for p, a, b in DOS],
                  omplir=(3, 4), amples=[16, 16, 16, 24, 16])], ico="calc"),
        act("Multiplica els dos factors: fan un sol factor. Quin canvi és?", [
            taula(["Els dos canvis", "Els dos factors", "Un sol factor", "És un canvi de"],
                  [un_sol(a, b) for a, b in UNIC], omplir=(1, 2, 3), amples=[24, 24, 20, 20])],
            ico="calc", repte=True,
            nota_sol="Un pas més: els dos factors multiplicats fan el factor de tot el camí (0,8 × 1,21 = 0,968, és a "
                     "dir − 3,2 %). Mai no és la suma dels percentatges: − 20 % i + 21 % no és + 1 %."),
    ])


# ------------------------------------------------- 4 · pujar i baixar --

PB = ((100, 10), (200, 20), (50, 50), (80, 25), (300, 10), (40, 30), (120, 5), (500, 40), (60, 15), (90, 20),
      (250, 50), (1000, 1), (75, 100))


def puja_baixa(preu, p):
    pujat = final(preu, p)
    baixat = final(preu, p, -p)
    return [eur(preu), f"{pct(p)} i {pct(-p)}", eur(pujat), eur(baixat), eur(D(preu) - baixat)]


def dos_ordres(preu, p, q):
    return [eur(preu), f"{pct(p)} i {pct(q)}", eur(final(preu, p, q)), eur(final(preu, q, p)),
            "sí" if final(preu, p, q) == final(preu, q, p) else "no"]


bloc4 = dict(
    titol="Pujar i baixar el mateix", mira=(4, 6),
    nota_sol="Pujar i baixar el mateix percentatge no torna mai al preu de sortida: el segon percentatge es fa "
             "sobre un preu diferent. Sempre en falta (la columna «Hi perds»).",
    acts=[
        act("Puja i després baixa el mateix percentatge. Quant hi perds?", [
            taula(["Preu", "Canvis", "Després de pujar", "Després de baixar", "Hi perds"],
                  [puja_baixa(*r) for r in PB], omplir=(2, 3, 4), amples=[16, 22, 18, 18, 14])], ico="calc"),
        act("Fes els dos canvis en un ordre i en l'altre. Surt el mateix?", [
            taula(["Preu", "Canvis", "En aquest ordre", "Al revés", "El mateix?"],
                  [dos_ordres(*r) for r in ((100, -20, 21), (200, 10, -10), (50, -50, 50), (80, 25, -20),
                                            (300, -15, 21), (40, 30, -30), (120, -10, 5), (500, 40, -25),
                                            (60, 21, -50), (90, -20, 20), (250, 10, 10), (1000, -5, 21),
                                            (75, 100, -50))],
                  omplir=(2, 3, 4), amples=[16, 22, 18, 18, 14])],
            ico="calc", repte=True,
            nota_sol="Una decisió nova: l'ordre no canvia el resultat, perquè és la mateixa multiplicació (0,8 × 1,21 "
                     "= 1,21 × 0,8). Si surt algun cèntim diferent és per l'arrodoniment del preu del mig."),
    ])


# ------------------------------------------------- 5 · al comptat o a terminis --

def paga(preu, desc, quotes, quota, entrada=0):
    comptat = final(preu, -desc)
    terminis = entrada + quotes * D(quota)
    assert comptat != terminis
    t = f"{entrada} + {quotes} × {fmt(quota)}" if entrada else f"{quotes} × {fmt(quota)}"
    return [f"{eur(preu)}, {pct(-desc)}", f"{quotes} quotes de {eur(quota)}" +
            (f" i {eur(entrada)} d'entrada" if entrada else ""),
            eur(comptat), f"{t} = {eur(terminis)}", "al comptat" if comptat < terminis else "a terminis"]


PAGA = ((300, 15, 12, 24), (240, 10, 6, 42), (500, 5, 10, 46), (800, 10, 12, 65), (150, 20, 3, 45),
        (60, 5, 4, 14), (1000, 15, 24, 40), (90, 10, 3, 28), (400, 5, 8, 47), (1200, 20, 10, 99),
        (350, 10, 6, 52), (75, 5, 5, 15), (650, 15, 12, 45))
PAGA_E = ((300, 15, 10, 20, 50), (500, 10, 12, 30, 100), (240, 5, 6, 30, 50), (800, 20, 10, 50, 100),
          (150, 10, 4, 25, 30), (1000, 15, 20, 34, 150), (90, 20, 3, 20, 10), (400, 10, 8, 36, 80),
          (60, 5, 5, 10, 5), (1200, 10, 12, 80, 100), (350, 15, 6, 45, 40), (720, 5, 10, 60, 50),
          (2000, 25, 24, 55, 300))

bloc5 = dict(
    titol="Al comptat o a terminis?", mira=(5, 7),
    nota_sol="<b>La regla trencada de la unitat:</b> al comptat no sempre és més barat. Ja a l'apartat c (el "
             "portàtil) guanyen els terminis, perquè el descompte és petit. Si tria «al comptat» sense fer els "
             "dos comptes, és aquí on cal aturar-se.",
    acts=[
        act("Fes els dos comptes i escriu quina manera de pagar surt més a compte.", [
            taula(["Al comptat, amb descompte", "A terminis", "Al comptat (€)", "A terminis (€)", "Guanya"],
                  [paga(*r) for r in PAGA], omplir=(2, 3, 4), amples=[22, 22, 14, 18, 12], esq=(0, 1))],
            ico="calc"),
        act("Ara els terminis tenen una entrada. Fes els dos comptes i decideix.", [
            taula(["Al comptat, amb descompte", "A terminis", "Al comptat (€)", "A terminis (€)", "Guanya"],
                  [paga(*r) for r in PAGA_E], omplir=(2, 3, 4), amples=[22, 22, 14, 18, 12], esq=(0, 1))],
            ico="calc", repte=True,
            nota_sol="Un pas més: l'entrada es paga a part, i s'ha de sumar a les quotes (50 + 10 × 20). <b>Error "
                     "típic:</b> oblidar l'entrada."),
    ])


# ------------------------------------------------- 6 · l'IVA --

IVA = ((40, 21), (25, 21), (60, 21), (12, 10), (80, 21), (5, 10), (150, 21), (18, 4), (9.90, 21), (32, 10),
       (2.50, 4), (499, 21), (14.50, 10))
SENSE = ((48.40, 21), (30.25, 21), (13.20, 10), (72.60, 21), (5.20, 4), (121, 21), (22, 10), (181.50, 21),
         (3.12, 4), (6.60, 10), (605, 21), (12.10, 21), (1.04, 4))

bloc6 = dict(
    titol="L'IVA", mira=(6, 8),
    nota_sol="L'IVA és un + %: el general és el 21 % (× 1,21), el reduït el 10 % (× 1,1) i el superreduït el "
             "4 % (× 1,04), per al pa, la llet o els llibres. <b>Error típic:</b> × 1,4 per al 4 %.",
    acts=[
        act("Calcula el preu amb IVA.", [
            taula(["Sense IVA", "IVA", "Factor", "Amb IVA"],
                  [[eur(p), f"{i} %", xf(i), eur(final(p, i))] for p, i in IVA],
                  omplir=(2, 3), amples=[22, 22, 22, 22])], ico="calc"),
        act("Ara al revés: el tiquet diu el preu amb IVA. Quant val sense IVA?", [
            taula(["Amb IVA", "IVA", "Factor", "Sense IVA"],
                  [[eur(p), f"{i} %", xf(i), eur(D(p) / factor(i))] for p, i in SENSE],
                  omplir=(2, 3), amples=[22, 22, 22, 22], abans=nota("Per treure l'IVA, divideix pel factor."))],
            ico="calc", repte=True,
            nota_sol="El camí al revés: dividir pel factor (48,40 ÷ 1,21 = 40). <b>Error típic:</b> restar el 21 % "
                     "del preu amb IVA (48,40 × 0,79 = 38,24 €), que no torna als 40 €."),
    ])


# ------------------------------------------------- 7 · a la vida de cada dia --

def dues(a_txt, a_preu, a_desc, b_txt, b_preu, b_desc):
    a, b = final(a_preu, -a_desc), final(b_preu, -b_desc)
    assert a != b
    return [f"{eur(a_preu)}, {pct(-a_desc)}", f"{eur(b_preu)}, {pct(-b_desc)}",
            eur(a), eur(b), a_txt if a < b else b_txt]


VIDA = [dues("Botiga", 80, 20, "Internet", 70, 10), dues("Botiga", 120, 25, "Internet", 95, 5),
        dues("Botiga", 60, 30, "Internet", 45, 5), dues("Botiga", 200, 10, "Internet", 190, 5),
        dues("Botiga", 50, 40, "Internet", 35, 10), dues("Botiga", 300, 15, "Internet", 270, 10),
        dues("Botiga", 90, 50, "Internet", 50, 5), dues("Botiga", 40, 10, "Internet", 38, 5),
        dues("Botiga", 150, 30, "Internet", 120, 10), dues("Botiga", 75, 20, "Internet", 62, 5),
        dues("Botiga", 500, 20, "Internet", 450, 10), dues("Botiga", 30, 50, "Internet", 20, 20),
        dues("Botiga", 1000, 25, "Internet", 800, 5)]


def dies(entrada, abonament, d_ab, n):
    a = final(abonament, -d_ab)
    b = D(entrada) * n
    assert a != b, (abonament, n)
    return [f"{n} dies", eur(a), eur(b), "l'abonament" if a < b else "les entrades"]


def gimnas(entrada, abonament, d_ab, quants):
    return taula(["Hi vas", "Abonament (€)", "Entrades (€)", "Surt més a compte"],
                 [dies(entrada, abonament, d_ab, n) for n in quants], omplir=(1, 2, 3), amples=[16, 24, 24, 24],
                 abans=nota(f"Abonament de {eur(abonament)} amb un {d_ab}{NB}% de descompte, "
                            f"o entrada de dia a {eur(entrada)}."))


bloc7 = dict(
    titol="A la vida de cada dia", mira=(7, 9),
    nota_sol="El descompte més gran no sempre guanya: depèn del preu de sortida. Ja a l'apartat a la botiga fa un "
             "20 % i surt més cara que internet, amb un 10 %. Que faci sempre els dos comptes.",
    acts=[
        act("Calcula què pagues a cada lloc i escriu on surt més barat.", [
            taula(["A la botiga", "Per internet", "Botiga (€)", "Internet (€)", "Més barat"], VIDA,
                  omplir=(2, 3, 4), amples=[22, 22, 15, 15, 14], esq=(0, 1))], ico="calc"),
        act("El gimnàs durant un mes: abonament amb descompte o entrada de dia?", [
            gimnas(3, 40, 25, (12, 8, 9, 15)), gimnas(4, 30, 10, (6, 9, 5)),
            gimnas(2.5, 45, 20, (15, 12, 20)), gimnas(5, 50, 30, (8, 5, 6))],
            ico="calc", repte=True,
            nota_sol="Una decisió nova: depèn de quants dies hi vas. Amb pocs dies guanyen les entrades; amb molts, "
                     "l'abonament. Hi ha un nombre de dies a partir del qual canvia (amb 3 € i 30 €, a partir de 10)."),
    ])


BLOCS = [bloc1, bloc2, bloc3, bloc4, bloc5, bloc6, bloc7]
