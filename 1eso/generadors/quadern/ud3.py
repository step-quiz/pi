"""Quadern d'activitats de la Unitat 3 · Com és de gran Gaza? (l'àrea i les fraccions).

    python3 1eso/generadors/gen_quadern.py 3        (des de l'arrel)

La unitat té sis fitxes (Mesurar l'àrea, Què és una fracció, Els tipus i comparar, Fraccions
equivalents, Sumar i restar, Quants km²?), i el quadern hi fa un o dos blocs per fitxa, dels
exercicis que en són el nucli i de la regla trencada. A cada bloc, una activitat germana i una de
repte. Cada activitat té 13 apartats: l'a), resolt, i 12 per fer. El filtre en deixa 3, 6 o 12,
sempre els primers: per això van de menys a més.

Les regles del curs: la targeta de les taules i la de les fraccions al davant, sense calculadora,
nombres de tres xifres com a molt i totes les fraccions dibuixades amb el mateix rectangle
(peces.py, que fa servir les peces de les fitxes). Els números es calculen aquí.
"""
from fractions import Fraction

from quadern import act, taula, tria, nota, llista, ms
from peces import F, fr, nom, fraccions_dibuix, talls_svg, parella_tires

NUM = 3
TITOL = "Com és de gran Gaza?"   # el de dades/unitats.js
AVALUAR = ("Sempre amb les dues targetes al davant. El que s'avalua és mirar el dibuix i decidir: quants "
           "quadrets, si els trossos són iguals, quin tros pintat és més gran, si dues fraccions pinten el "
           "mateix. Els noms no es demanen de memòria. Les activitats de repte compten per als nivells alts "
           "(AN, AE), no per al mínim.")

FA, FF, FC, FE, FS, FM = ("Mesurar l'àrea", "Què és una fracció", "Els tipus i comparar",
                          "Fraccions equivalents", "Sumar i restar", "Quants km²? Barcelona i Gaza")
SI, NO = "Sí", "No"


# ------------------------------------------------- 1 · l'àrea del rectangle --

def area(f, c):
    return [f"{f} files de {c} quadrets", f"{f} · {c} = {f * c} quadrets"]


def quin_ocupa(a, b, c, d):
    x, y = a * b, c * d
    return (f"A: {a} files de {b}. B: {c} files de {d}.", ["A", "B", "Igual"],
            0 if x > y else 1 if y > x else 2), f"A {a} · {b} = {x}, B {c} · {d} = {y}"


OCUPA = [quin_ocupa(*r) for r in ((3, 5, 4, 4), (2, 6, 3, 3), (5, 4, 3, 6), (2, 9, 4, 4), (3, 8, 5, 5),
                                  (2, 8, 4, 4), (6, 7, 5, 8), (4, 9, 6, 6), (3, 9, 5, 5), (7, 7, 6, 8),
                                  (2, 10, 4, 5), (8, 9, 7, 10), (9, 9, 8, 10))]

bloc1 = dict(
    titol="L'àrea del rectangle", mira=(3, 3, FA),
    nota_sol="L'àrea és quants quadrets ocupa: les files pels quadrets de cada fila, amb la targeta. És el "
             "rectangle de la unitat 1.",
    acts=[
        act("Calcula l'àrea de cada rectangle. Mira la targeta de les taules.", [
            taula(["Rectangle", "Àrea"],
                  [area(f, c) for f, c in ((2, 6), (4, 5), (3, 7), (6, 6), (5, 8), (7, 9), (2, 9), (8, 8),
                                           (4, 9), (6, 7), (9, 10), (5, 5), (3, 10))],
                  omplir=(1,), amples=[44, 44], esq=(0,))]),
        act("Quin rectangle ocupa més? Marca A, B o Igual.", [
            tria([o for o, _ in OCUPA], en_linia=True,
                 sol_nota="Les àrees: " + " · ".join(s for _, s in OCUPA) + ".")],
            repte=True,
            nota_sol="Una decisió nova: no es pot mirar quin és més llarg, cal comptar els quadrets dels dos. "
                     "Hi ha rectangles diferents que ocupen igual (2 files de 8 i 4 de 4). <b>Error típic:</b> "
                     "triar el que té el número més gran."),
    ])


# ------------------------------------------------- 2 · la fracció del dibuix --

def iguals_q(talls, pintat, d):
    """Un apartat de la regla trencada: el rectangle, partit per `talls`, amb un tros pintat. És 1/d?"""
    trossos = [b - a for a, b in zip([0] + list(talls), list(talls) + [1])]
    bona = all(abs(t - 1 / d) < 1e-9 for t in trossos) and len(trossos) == d
    text = (f'<span style="display:inline-flex;align-items:center;gap:.7rem;vertical-align:middle">'
            f'{talls_svg(talls, pintat, W=5.0)}<span>És {fr(1, d)}?</span></span>')
    return (text, [SI, NO], 0 if bona else 1)


def parts(d):
    return [i / d for i in range(1, d)]


IGUALS = [iguals_q([.2, .45, .75], 1, 4), iguals_q(parts(3), 0, 3), iguals_q([.5, .75], 0, 3),
          iguals_q(parts(4), 2, 4), iguals_q([.25, .5, .7, .85], 4, 5), iguals_q(parts(5), 1, 5),
          iguals_q([.3, .6], 2, 3), iguals_q(parts(6), 3, 6), iguals_q([.5], 0, 2),
          iguals_q([.4], 1, 2), iguals_q([.15, .3, .65], 3, 4), iguals_q(parts(8), 5, 8),
          iguals_q([.2, .4, .6, .8], 0, 5)]

bloc2 = dict(
    titol="La fracció del dibuix", mira=(1, 2, FF),
    nota_sol="A dalt, els trossos pintats; a baix, tots els trossos. El nom, amb la targeta de les fraccions. "
             "<b>Error típic:</b> girar-la (5/2) o comptar els trossos blancs.",
    acts=[
        act("Escriu la fracció de cada dibuix. Després escriu com es llegeix.", [
            fraccions_dibuix([(3, 5), (2, 4), (1, 3), (5, 6), (3, 8), (4, 7), (2, 9), (7, 10), (1, 2),
                              (6, 8), (5, 12), (9, 10), (11, 12)])]),
        act("El tros pintat, és la fracció que diu? Mira si tots els trossos són iguals.", [
            tria(IGUALS, en_linia=True)],
            repte=True,
            nota_sol="<b>La regla trencada de la fitxa:</b> una fracció vol trossos iguals. Ja a l'a) els "
                     "trossos no són iguals. Si diu que sí perquè hi ha 4 trossos i un de pintat, que retalli el "
                     "rectangle i posi els trossos un damunt de l'altre."),
    ])


# ------------------------------------------------- 3 · el nom de la fracció --

NOMS = ((3, 4), (2, 5), (1, 2), (5, 8), (1, 3), (7, 10), (4, 9), (5, 6), (3, 7), (1, 4), (2, 3), (11, 12), (9, 10))
NOMS_R = ((2, 3), (4, 5), (1, 6), (3, 8), (7, 9), (1, 10), (5, 7), (3, 4), (6, 11), (1, 5), (9, 12), (2, 9), (5, 8))

bloc3 = dict(
    titol="Com es llegeix", mira=(4, 5, FF),
    nota_sol="Sempre amb la targeta de les fraccions: els noms no es demanen de memòria. 1/2 és «un mig», "
             "1/3 «un terç» i 1/4 «un quart»; a partir del 5, cinquens, sisens…",
    acts=[
        act("Escriu com es llegeix cada fracció. Mira la targeta.", [
            taula(["La fracció", "Es llegeix"], [[F(n, d), nom(n, d)] for n, d in NOMS],
                  omplir=(1,), amples=[30, 58])]),
        act("Ara al revés: escriu la fracció.", [
            taula(["Es llegeix", "La fracció"], [[nom(n, d), F(n, d)] for n, d in NOMS_R],
                  omplir=(1,), amples=[58, 30], esq=(0,))],
            repte=True,
            nota_sol="El camí al revés: de les paraules a la fracció. El primer número és el que es diu primer "
                     "(«cinc setens»: 5 a dalt), i el segon diu la mida dels trossos."),
    ])


# ------------------------------------------------- 4 · els tipus --

def tipus(n, d):
    return "nul·la" if n == 0 else "pròpia" if n < d else "unitat" if n == d else "impròpia"


TIPUS = ((5, 4), (3, 4), (7, 7), (9, 5), (0, 6), (2, 9), (12, 10), (1, 3), (8, 8), (0, 3), (6, 5), (4, 10), (11, 6))
DEMANA = (("Pròpia", 5), ("Impròpia", 3), ("Unitat", 4), ("Nul·la", 7), ("Pròpia", 8), ("Impròpia", 6),
          ("Unitat", 10), ("Pròpia", 2), ("Impròpia", 4), ("Nul·la", 9), ("Pròpia", 12), ("Impròpia", 10),
          ("Unitat", 6))


def exemple(t, d):
    n = {"Pròpia": 1, "Impròpia": d + 1, "Unitat": d, "Nul·la": 0}[t]
    assert tipus(n, d) == t.lower()
    return [t, str(d), (fr(n, d), {"Pròpia": f"de 1/{d} a {d - 1}/{d}" if d > 2 else "1/2", "Impròpia": f"{d + 1}/{d} o més",
                                   "Unitat": f"{d}/{d}", "Nul·la": f"0/{d}"}[t], fr(n, d, ma=True))]


bloc4 = dict(
    titol="Els tipus de fraccions", mira=(1, 2, FC),
    nota_sol="Es mira el de dalt i el de baix: 0 a dalt, nul·la; més petit, pròpia (menys d'un rectangle); "
             "iguals, unitat; més gran, impròpia (més d'un rectangle). Si no ho veu clar, que la pinti en tires "
             "de paper.",
    acts=[
        act("Quin tipus de fracció és? Escriu-lo.", [
            taula(["Fracció", "El tipus"], [[F(n, d), tipus(n, d)] for n, d in TIPUS],
                  omplir=(1,), amples=[30, 58], abans=nota("Nul·la, pròpia, unitat o impròpia."))]),
        act("Escriu una fracció del tipus que diu, amb aquest de baix.", [
            taula(["El tipus", "El de baix", "La fracció"], [exemple(t, d) for t, d in DEMANA],
                  omplir=(2,), amples=[30, 26, 32],
                  sol_nota="Hi ha moltes respostes bones: el solucionari diu quines.")],
            repte=True,
            nota_sol="El camí al revés: del tipus a la fracció. Ara ha de decidir el de dalt (més petit, igual "
                     "o més gran que el de baix). La unitat i la nul·la només tenen una resposta."),
    ])


# ------------------------------------------------- 5 · quina és més gran --

def mes_gran(a, b, c, d):
    x, y = Fraction(a, b), Fraction(c, d)
    assert x != y
    return (f"{fr(a, b)} o {fr(c, d)}", [F(a, b), F(c, d)], 0 if x > y else 1)


GRAN = [mes_gran(*r) for r in ((2, 6, 5, 6), (3, 5, 4, 5), (1, 3, 1, 5), (7, 10, 4, 10), (2, 8, 1, 8),
                               (2, 5, 2, 7), (5, 9, 8, 9), (1, 4, 1, 6), (3, 4, 2, 4), (3, 8, 3, 5),
                               (6, 12, 9, 12), (1, 10, 1, 2), (4, 9, 4, 7))]


def ordena(*fs):
    s = sorted(fs, key=lambda p: Fraction(*p))
    return [(" &nbsp; &nbsp; ".join(fr(n, d) for n, d in fs), ", ".join(f"{n}/{d}" for n, d in fs), " &nbsp; &nbsp; ".join(fr(n, d, ma=True) for n, d in fs)),
            (" < ".join(fr(n, d) for n, d in s), " < ".join(f"{n}/{d}" for n, d in s),
             " < ".join(fr(n, d, ma=True) for n, d in s))]


ORDRE = [ordena(*r) for r in (((3, 5), (1, 5), (4, 5)), ((2, 6), (5, 6), (1, 6)), ((1, 2), (1, 4), (1, 3)),
                              ((7, 9), (2, 9), (5, 9)), ((1, 5), (1, 2), (1, 8)), ((3, 10), (9, 10), (6, 10)),
                              ((2, 3), (2, 7), (2, 5)), ((4, 8), (7, 8), (1, 8)), ((1, 6), (1, 3), (1, 10)),
                              ((5, 12), (11, 12), (2, 12)), ((3, 4), (3, 8), (3, 5)), ((1, 9), (1, 4), (1, 7)),
                              ((2, 9), (2, 3), (2, 5)))]

bloc5 = dict(
    titol="Quina és més gran?", mira=(3, 4, FC),
    nota_sol="<b>La regla trencada de la fitxa:</b> amb el mateix de dalt, és més gran la del de baix més petit "
             "(1/3 és més gran que 1/5), perquè els trossos són més grans. Surt a l'apartat c. Si tria la del "
             "número més gran, que les pinti al mateix rectangle.",
    acts=[
        act("Quina és més gran? Marca-la. Si dubtes, fes-ne el dibuix.", [
            tria(GRAN, en_linia=True)]),
        act("Ordena les fraccions, de més petita a més gran.", [
            taula(["Les fraccions", "De més petita a més gran"], ORDRE, omplir=(1,), amples=[40, 48])],
            repte=True,
            nota_sol="Tres alhora, i a cada apartat totes tenen el mateix de baix o el mateix de dalt. Amb el "
                     "mateix de baix, l'ordre és el dels de dalt; amb el mateix de dalt, va al revés."),
    ])


# ------------------------------------------------- 6 · amplificar --

def amplifica(n, d, k):
    return [F(n, d), f"per {k}", f"{n} · {k} = {n * k}", f"{d} · {k} = {d * k}", F(n * k, d * k)]


def simplifica(n, d, k):
    assert n % k == 0 and d % k == 0
    return [F(n, d), f"entre {k}", F(n // k, d // k)]


bloc6 = dict(
    titol="Amplificar", mira=(2, 3, FE),
    nota_sol="Partir cada tros en trossos més petits és multiplicar el de dalt i el de baix pel mateix "
             "nombre. Totes les multiplicacions són de la targeta.",
    acts=[
        act("Amplifica: multiplica el de dalt i el de baix pel mateix nombre.", [
            taula(["Fracció", "Multiplica", "El de dalt", "El de baix", "La nova"],
                  [amplifica(*r) for r in ((1, 3, 4), (1, 2, 4), (2, 5, 3), (3, 4, 2), (2, 3, 5), (1, 5, 2),
                                           (3, 8, 2), (4, 5, 2), (2, 7, 3), (5, 6, 2), (1, 4, 5), (3, 10, 3),
                                           (7, 9, 2))],
                  omplir=(2, 3, 4), amples=[16, 16, 20, 20, 16])]),
        act("Simplifica: divideix el de dalt i el de baix pel mateix nombre.", [
            taula(["Fracció", "Divideix", "La simplificada"],
                  [simplifica(*r) for r in ((6, 8, 2), (3, 9, 3), (4, 10, 2), (5, 10, 5), (2, 6, 2), (6, 9, 3),
                                            (8, 12, 4), (10, 15, 5), (4, 6, 2), (9, 12, 3), (14, 21, 7),
                                            (12, 18, 6), (20, 30, 10))],
                  omplir=(2,), amples=[30, 28, 30], abans=nota("Busca-ho a la targeta de les taules."))],
            repte=True,
            nota_sol="El camí de tornada d'amplificar, com l'exercici 4 de la fitxa (nivells alts). Els "
                     "nombres són de la targeta: 2 · 3 = 6 i 2 · 4 = 8, per tant 6/8 = 3/4."),
    ])


# ------------------------------------------------- 7 · són equivalents? --

def equiv(a, b, c, d):
    return (f'<span style="display:inline-block;vertical-align:middle;width:7.2cm">'
            f'{parella_tires((a, b), (c, d), W=5.0)}</span>', [SI, NO], 0 if Fraction(a, b) == Fraction(c, d) else 1)


EQUIV = [equiv(*r) for r in ((2, 3, 3, 4), (1, 3, 2, 6), (1, 2, 2, 3), (3, 4, 6, 8), (2, 5, 4, 10),
                             (1, 4, 2, 5), (2, 3, 4, 6), (3, 5, 4, 6), (1, 2, 3, 6), (1, 2, 5, 10),
                             (2, 4, 3, 5), (4, 5, 8, 10), (3, 6, 4, 7))]


def falta(n, d, k, dalt):
    """1/2 = ?/8 (dalt=True: falta el de dalt) o 1/2 = 4/? (falta el de baix)."""
    forat = '<span class="buit" style="min-width:1.2cm"></span>'
    if dalt:
        return [(f"{fr(n, d)} = {forat} / {d * k}", f"{n}/{d} = ?/{d * k}",
                 f"{fr(n, d, ma=True)} = {fr(n * k, d * k, ma=True)}"), str(n * k)]
    return [(f"{fr(n, d)} = {n * k} / {forat}", f"{n}/{d} = {n * k}/?",
             f"{fr(n, d, ma=True)} = {fr(n * k, d * k, ma=True)}"), str(d * k)]


bloc7 = dict(
    titol="Són equivalents?", mira=(3, 4, FE),
    nota_sol="<b>La regla trencada de la fitxa:</b> per fer una equivalent es multiplica, no se suma. A l'a) "
             "(2/3 i 3/4) s'ha sumat 1 a dalt i a baix, i el tros pintat és més llarg. Que compari els trossos "
             "pintats: els dos rectangles són iguals.",
    acts=[
        act("Són equivalents? Mira si el tros pintat és igual de llarg.", [
            tria(EQUIV, en_linia=True)]),
        act("Escriu el número que falta perquè siguin equivalents.", [
            taula(["Les dues fraccions", "El que falta"],
                  [falta(*r) for r in ((1, 2, 4, True), (1, 3, 2, True), (2, 5, 2, False), (3, 4, 2, True),
                                       (1, 4, 3, False), (2, 3, 4, True), (1, 5, 2, False), (3, 5, 3, True),
                                       (5, 6, 2, False), (2, 7, 3, True), (3, 8, 2, False), (4, 9, 2, True),
                                       (7, 10, 2, False))],
                  omplir=(1,), amples=[56, 32])],
            repte=True,
            nota_sol="Primer cal trobar per quant s'ha multiplicat l'altre número (de 2 a 8, per 4), i després "
                     "fer el mateix amb el que falta. <b>Error típic:</b> sumar (1/2 = 7/8 perquè 2 + 6 = 8)."),
    ])


# ------------------------------------------------- 8 · sumar i restar --

def opera(a, d, b, signe):
    r = a + b if signe == "+" else a - b
    assert 0 <= r
    return [(f"{fr(a, d)} {signe} {fr(b, d)} =", f"{a}/{d} {signe} {b}/{d}",
             f"{fr(a, d, ma=True)} {signe} {fr(b, d, ma=True)} ="), F(r, d)]


def esta_be(a, d, b, signe, bona):
    """Una suma o resta ja feta: la bona (el de baix no canvia) o la de la regla trencada (operar
    també els de baix)."""
    r = a + b if signe == "+" else a - b
    dr = d if bona else (d + d if signe == "+" else 0)
    if not bona and signe == "−":
        return None
    return (f"{fr(a, d)} {signe} {fr(b, d)} = {fr(r, dr)}", ["Bé", "Malament"], 0 if bona else 1)


BE = [esta_be(*r) for r in ((1, 4, 2, "+", False), (1, 4, 2, "+", True), (2, 5, 1, "+", False),
                            (3, 8, 4, "+", True), (2, 6, 3, "+", False), (5, 7, 2, "−", True),
                            (1, 3, 1, "+", False), (4, 9, 3, "+", True), (3, 10, 5, "+", False),
                            (7, 12, 2, "−", True), (2, 9, 5, "+", False), (1, 6, 4, "+", True),
                            (3, 5, 1, "+", False))]

bloc8 = dict(
    titol="Sumar i restar", mira=(3, 4, FS),
    nota_sol="Se sumen o es resten els de dalt, i el de baix no canvia, perquè els trossos són els mateixos. "
             "Si dubta, que en faci el dibuix: pintar per sumar, ratllar per restar.",
    acts=[
        act("Suma o resta els de dalt. El de baix no canvia.", [
            taula(["L'operació", "El resultat"],
                  [opera(*r) for r in ((2, 9, 5, "+"), (3, 10, 4, "+"), (7, 8, 2, "−"), (1, 6, 4, "+"),
                                       (5, 7, 3, "−"), (2, 5, 2, "+"), (9, 12, 4, "−"), (3, 8, 3, "+"),
                                       (6, 9, 1, "−"), (4, 10, 5, "+"), (11, 12, 6, "−"), (3, 5, 4, "+"),
                                       (8, 10, 8, "−"))],
                  omplir=(1,), amples=[56, 32],
                  sol_nota="L'apartat l (7/5) és més d'un rectangle, i la m dona 0/10: no en queda res.")]),
        act("Està bé? Marca la resposta. Si dubtes, fes-ne el dibuix.", [
            tria([b for b in BE if b], en_linia=True)],
            repte=True,
            nota_sol="<b>La regla trencada de la fitxa:</b> el de baix no se suma. Ja a l'a) (1/4 + 2/4 = 3/8) "
                     "està malament. Que ho compari amb la meitat, com a la pàgina 5 de la fitxa: si sumes, no "
                     "pots tenir menys del que tenies."),
    ])


# ------------------------------------------------- 9 · quants km²? --

def km2(c, d, u):
    return [str(c), str(d), str(u), f"{100 * c + 10 * d + u} km²"]


def descompon(n):
    c, r = divmod(n, 100)
    d, u = divmod(r, 10)
    return [f"{n} km²", str(c), str(d), str(u)]


bloc9 = dict(
    titol="Quants km²?", mira=(1, 2, FM),
    nota_sol="Els quadrets es llegeixen com els blocs de la unitat 1: quadrats de 100 (centenes), columnes de "
             "10 (desenes) i quadrets solts (unitats). Gaza fa 3, 6 i 5: 365 km².",
    acts=[
        act("Cada quadret és 1 km². Quants km² fa cada mapa?", [
            taula(["Quadrats de 100", "Columnes de 10", "Quadrets solts", "km²"],
                  [km2(*r) for r in ((2, 4, 3), (1, 0, 1), (3, 6, 5), (1, 5, 0), (4, 2, 7), (2, 0, 9),
                                     (5, 3, 1), (6, 8, 4), (3, 0, 0), (7, 1, 6), (1, 9, 9), (8, 0, 5), (9, 4, 2))],
                  omplir=(3,), amples=[22, 22, 22, 22])]),
        act("Ara al revés: quants quadrats de 100, columnes de 10 i quadrets solts?", [
            taula(["km²", "Quadrats de 100", "Columnes de 10", "Quadrets solts"],
                  [descompon(n) for n in (365, 101, 248, 530, 712, 406, 189, 900, 623, 57, 840, 999, 305)],
                  omplir=(1, 2, 3), amples=[22, 22, 22, 22])],
            repte=True,
            nota_sol="El camí al revés: del nombre al dibuix. El zero és el que costa (406: 4 quadrats, cap "
                     "columna i 6 quadrets; 57: cap quadrat de 100). És la regla del zero de la unitat 1."),
    ])


BLOCS = [bloc1, bloc2, bloc3, bloc4, bloc5, bloc6, bloc7, bloc8, bloc9]
