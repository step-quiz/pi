"""Quadern d'activitats de la Unitat 3 · Proporcionalitat i escales.

    python3 4eso/generadors/gen_quadern.py 3        (des de l'arrel)

Un bloc per cada exercici de la fitxa (u3/fitxa.html), en el mateix ordre. A cada bloc,
una activitat germana i una de repte. Cada activitat té 13 apartats: l'a), resolt, i
12 per fer. El filtre en deixa 3 (petit), 6 (mitjà) o tots 12 (elevat), sempre els
primers: per això els apartats van de menys a més.

Refet el 24/11/2026, amb la fitxa: el centre ja no són les escales sinó la proporcionalitat.
  · Blocs 1-3, la directa: quant val 1, el preu d'1 a les ofertes (la regla trencada de la unitat:
    hi ha apartats on guanya el format petit, ja entre els tres primers) i la proporció
    x / c = a / b amb el producte en creu (b · x = c · a, es calcula c · a i es divideix per b).
  · Blocs 4-6, la inversa a ull (el doble, el triple, la meitat; cap equació) i distingir-les.
  · Blocs 7-8, a la vida de cada dia de la Part 1: les creps (directa) i els globus (inversa).
  · Blocs 9-12, la Part 2, escales i plànols: només del plànol a la realitat, i el mapa del barri.
Com la fitxa (24/11/2026), en dues parts: primer tota la proporcionalitat, després les escales.
Les frases són completes: «Per fer una truita per a més persones, necessites més ous», no
«més persones, més ous» (correcció del docent, 24/11/2026).

Els números es calculen aquí, no s'escriuen a mà: així el solucionari no es pot equivocar.
"""
from fractions import Fraction

from quadern import act, taula, tria, taula_tria, ofertes, planol, doble_recta, linies
from quadern import num, eur, esc, nota

NUM = 3
TITOL = "Proporcionalitat i escales"   # el de dades/unitats.js (decisió V2)
AVALUAR = ("Com a la fitxa, l'objectiu no és calcular bé: és saber si la resposta ha de ser més gran o més "
           "petita, triar el camí (quant val 1, el producte en creu o el doble i la meitat) i decidir. Un "
           "error de divisió no hauria de fer baixar la valoració si el plantejament és correcte. Les "
           "activitats de repte compten per als nivells alts (AN, AE), no per al mínim.")

A3 = [30, 30, 30]
A4 = [22, 22, 22, 22]


def exacte(x):
    """Un resultat que ha de sortir amb dos decimals com a molt (el solucionari no arrodoneix)."""
    assert abs(round(x, 2) - x) < 1e-9, x
    return round(x, 2)


# ------------------------------------------------- 1 · primer, quant val 1 --

def eu(x):
    """Diners com a la fitxa: «21 €» si són euros justos, «7,50 €» si no."""
    return f"{num(x)} €" if x == int(x) else eur(x)


def n_eu(x):
    """El mateix sense el símbol, per als comptes: «21» o «7,50»."""
    return eu(x)[:-2]


CAP1 = ["Què sabem", "Quant val 1", "Pregunta", "Resposta"]
A1 = [28, 20, 20, 20]

B1 = [(3, "entrades", 21, 5), (4, "iogurts", 2, 10), (5, "llibretes", 7.50, 4), (2, "pizzes", 16, 3),
      (6, "ous", 1.80, 12), (10, "llapis", 4, 3), (4, "cafès", 6, 7), (3, "barres de pa", 3.60, 5),
      (5, "bolígrafs", 4.50, 8), (8, "entrades", 60, 3), (6, "llaunes", 4.20, 10), (4, "samarretes", 26, 6),
      (12, "galetes", 3, 5)]


def preu1(quants, que, preu, demana):
    u = exacte(preu / quants)
    r = exacte(u * demana)
    return [f"{num(quants)} {que} costen {eu(preu)}.", f"{n_eu(preu)} ÷ {num(quants)} = {eu(u)}",
            f"I {num(demana)} {que}?", f"{n_eu(u)} × {num(demana)} = {eu(r)}"]


MASCULI = {"iogurts", "ous", "llapis", "cafès", "bolígrafs"}


def quantes(quants, que, preu, diners):
    """El camí al revés: amb uns diners, quantes en pots comprar."""
    u = exacte(preu / quants)
    n = diners / u
    assert abs(n - round(n)) < 1e-9, (que, diners, u)
    return [f"{num(quants)} {que} costen {eu(preu)}.", f"{n_eu(preu)} ÷ {num(quants)} = {eu(u)}",
            f"Amb {eu(diners)}, {'quants' if que in MASCULI else 'quantes'} {que} pots comprar?", f"{n_eu(diners)} ÷ {n_eu(u)} = {num(round(n))} {que}"]


B1R = [(3, "entrades", 21, 49), (4, "iogurts", 2, 4), (2, "pizzes", 16, 40), (5, "llibretes", 7.50, 12),
       (10, "llapis", 4, 2), (4, "cafès", 6, 9), (3, "barres de pa", 3.60, 6), (6, "llaunes", 4.20, 7),
       (8, "entrades", 60, 45), (5, "bolígrafs", 4.50, 9), (4, "samarretes", 26, 39), (12, "galetes", 3, 2),
       (6, "ous", 1.80, 3)]

bloc1 = dict(
    titol="Primer, quant val 1", mira=(1, 3),
    nota_sol="Sempre els dos passos de la pàgina 2 de la fitxa: <i>dividir</i> per saber quant val 1 i "
             "després <i>multiplicar</i>. <b>Error típic:</b> dividir al revés (4 ÷ 2 en lloc de 2 ÷ 4). Si "
             "passa, que digui en veu alta si un sol iogurt ha de costar més o menys que tot el pack.",
    acts=[
        act("Calcula primer quant val 1. Després respon la pregunta.", [
            taula(CAP1, [preu1(*f) for f in B1], omplir=(1, 3), amples=A1, esq=(0, 2))], ico="calc"),
        act("Calcula primer quant val 1. Després calcula quantes en pots comprar.", [
            taula(["Què sabem", "Quant val 1", "Pregunta", "Resposta"], [quantes(*f) for f in B1R],
                  omplir=(1, 3), amples=[22, 18, 28, 20], esq=(0, 2))],
            ico="calc", repte=True,
            nota_sol="El camí al revés: ara se sap quants diners hi ha i es demana quantes se'n poden comprar. "
                     "El primer pas és el mateix (quant val 1); el segon és una divisió, no una multiplicació. "
                     "Si costa, que provi amb la multiplicació: 7 € × quantes entrades fan 49 €?"),
    ])


# ------------------------------------------------- 2 · quina oferta surt més a compte --

def op(nom, diu, preu, quantitat, unitat):
    """Una oferta: el preu d'1 es calcula (i ha de ser exacte, amb dos decimals)."""
    u = round(preu / quantitat, 2)
    assert abs(u * quantitat - preu) < 1e-9, (nom, preu, quantitat)
    return dict(nom=nom, diu=diu, compte=f"{eur(preu)[:-2]} ÷ {num(quantitat)}", val=f"{eur(u)} {unitat}", u=u)

def oferta(producte, *ops):
    us = [o["u"] for o in ops]
    assert len(set(us)) == len(us), producte          # cap empat
    return (producte, list(ops), us.index(min(us)))

L, KG, U = "el litre", "el quilo", "cada un"

bloc2 = dict(
    titol="Quina oferta surt més a compte", mira=(2, 4),
    nota_sol="<b>La regla trencada de la unitat:</b> el format gran no sempre guanya. A cada activitat hi ha "
             "apartats on guanya el petit, i el primer ja surt entre els tres de petit. Si tria el gran "
             "sense dividir, és aquí on cal aturar-se: el preu d'1 és el que decideix.",
    acts=[
        act("Marca quina oferta surt més a compte.", [ofertes([
            oferta("Suc.", op("El brik", "Brik d'1 L per 1,20 €", 1.20, 1, L), op("El pack", "Pack de 3 L per 3,30 €", 3.30, 3, L)),
            oferta("Iogurts.", op("L'1", "1 iogurt per 0,50 €", 0.50, 1, U), op("El pack", "Pack de 4 per 1,80 €", 1.80, 4, U)),
            oferta("Oli.", op("L'ampolla", "Ampolla d'1 L per 4 €", 4, 1, L), op("La garrafa", "Garrafa de 5 L per 21 €", 21, 5, L)),
            oferta("Patates.", op("La bossa", "Bossa d'1 kg per 1,50 €", 1.50, 1, KG), op("El sac", "Sac de 3 kg per 3,90 €", 3.90, 3, KG)),
            oferta("Llapis.", op("L'1", "1 llapis per 0,60 €", 0.60, 1, U), op("La capsa", "Capsa de 10 per 5 €", 5, 10, U)),
            oferta("Sabó.", op("L'ampolla", "Ampolla de 2 L per 6 €", 6, 2, L), op("La garrafa", "Garrafa de 5 L per 16 €", 16, 5, L)),
            oferta("Tomàquets.", op("1 kg", "1 kg per 2,40 €", 2.40, 1, KG), op("2 kg", "2 kg per 4,60 €", 4.60, 2, KG)),
            oferta("Aigua amb gas.", op("L'ampolla", "Ampolla d'1 L per 0,80 €", 0.80, 1, L), op("El pack", "Pack de 6 L per 5,40 €", 5.40, 6, L)),
            oferta("Pomes.", op("1 kg", "1 kg per 1,90 €", 1.90, 1, KG), op("La caixa", "Caixa de 5 kg per 8 €", 8, 5, KG)),
            oferta("Farina.", op("1 kg", "1 kg per 1 €", 1, 1, KG), op("5 kg", "5 kg per 4,50 €", 4.50, 5, KG)),
            oferta("Llet de civada.", op("1 L", "1 L per 1,60 €", 1.60, 1, L), op("El pack", "Pack de 6 L per 10,20 €", 10.20, 6, L)),
            oferta("Retoladors.", op("L'1", "1 retolador per 1,20 €", 1.20, 1, U), op("La capsa", "Capsa de 12 per 12 €", 12, 12, U)),
            oferta("Galetes.", op("El paquet", "1 paquet per 1,50 €", 1.50, 1, U), op("El pack", "Pack de 3 per 4,80 €", 4.80, 3, U)),
        ])], ico="calc"),
        act("Marca quina de les tres ofertes surt més a compte.", [ofertes([
            oferta("Aigua.", op("1 L", "1 L per 0,50 €", 0.50, 1, L), op("2 L", "2 L per 0,80 €", 0.80, 2, L), op("5 L", "5 L per 2,75 €", 2.75, 5, L)),
            oferta("Llet.", op("1 L", "1 L per 1 €", 1, 1, L), op("4 L", "4 L per 3,60 €", 3.60, 4, L), op("6 L", "6 L per 5,70 €", 5.70, 6, L)),
            oferta("Suc.", op("1 L", "1 L per 1,20 €", 1.20, 1, L), op("2 L", "2 L per 2,60 €", 2.60, 2, L), op("4 L", "4 L per 5 €", 5, 4, L)),
            oferta("Arròs.", op("1 kg", "1 kg per 1,80 €", 1.80, 1, KG), op("2 kg", "2 kg per 3,40 €", 3.40, 2, KG), op("5 kg", "5 kg per 8 €", 8, 5, KG)),
            oferta("Sabó de rentar.", op("1 L", "1 L per 2 €", 2, 1, L), op("3 L", "3 L per 5,10 €", 5.10, 3, L), op("5 L", "5 L per 9 €", 9, 5, L)),
            oferta("Patates.", op("1 kg", "1 kg per 1,50 €", 1.50, 1, KG), op("3 kg", "3 kg per 3,90 €", 3.90, 3, KG), op("5 kg", "5 kg per 7 €", 7, 5, KG)),
            oferta("Iogurts.", op("1", "1 per 0,50 €", 0.50, 1, U), op("4", "4 per 1,80 €", 1.80, 4, U), op("8", "8 per 3,20 €", 3.20, 8, U)),
            oferta("Oli.", op("1 L", "1 L per 4 €", 4, 1, L), op("2 L", "2 L per 7,60 €", 7.60, 2, L), op("5 L", "5 L per 21 €", 21, 5, L)),
            oferta("Llapis.", op("1", "1 per 0,60 €", 0.60, 1, U), op("5", "5 per 2,50 €", 2.50, 5, U), op("10", "10 per 5,50 €", 5.50, 10, U)),
            oferta("Farina.", op("1 kg", "1 kg per 1 €", 1, 1, KG), op("2 kg", "2 kg per 1,90 €", 1.90, 2, KG), op("5 kg", "5 kg per 4,50 €", 4.50, 5, KG)),
            oferta("Tomàquets.", op("1 kg", "1 kg per 2,40 €", 2.40, 1, KG), op("2 kg", "2 kg per 4,60 €", 4.60, 2, KG), op("3 kg", "3 kg per 7,50 €", 7.50, 3, KG)),
            oferta("Pomes.", op("1 kg", "1 kg per 1,90 €", 1.90, 1, KG), op("3 kg", "3 kg per 5,40 €", 5.40, 3, KG), op("5 kg", "5 kg per 8 €", 8, 5, KG)),
            oferta("Aigua amb gas.", op("1 L", "1 L per 0,80 €", 0.80, 1, L), op("2 L", "2 L per 1,80 €", 1.80, 2, L), op("6 L", "6 L per 5,10 €", 5.10, 6, L)),
        ])], ico="calc", repte=True,
            nota_sol="Tres opcions en lloc de dues, i guanya tant la petita com la del mig o la gran. Qui "
                     "aplica una regla («el gran» o «el petit») s'equivoca sovint: cal dividir les tres."),
    ])


# ------------------------------------------------- 3 · la proporció i el producte en creu --

def frac(dalt, baix):
    """Una fracció dibuixada, com a la fitxa: el numerador damunt d'una ratlla."""
    return ('<span style="display:inline-block;text-align:center;vertical-align:middle;margin:0 .15rem">'
            f'<span style="display:block;border-bottom:2px solid #000;padding:0 .25rem">{dalt}</span>'
            f'<span style="display:block;padding:0 .25rem">{baix}</span></span>')


def creu(sabem, a, b, c, ua, ub, resposta):
    """x / c = a / b → b · x = c · a → x = (c · a) / b, com a la fitxa (24/11/2026): cada pas en una
    línia, i la divisió escrita com una fracció. ua: la unitat de la x (i de a); ub: la de b i c."""
    k = c * a
    x = exacte(k / b)
    prop = f"{frac('x', num(c))} = {frac(num(a), num(b))}"
    pas = f"{num(b)} · x = {num(c)} · {num(a)}<br>{num(b)} · x = {num(k)}"
    xx = f"x = {frac(num(k), num(b))}<br>x = {num(x)} {ua}"
    return [sabem, (prop, prop, prop), (pas, pas, pas), (xx, xx, xx)]


B3 = [creu("4 kg de taronges costen 6 €. Quant costen 10 kg?", 6, 4, 10, "€", "kg", None),
      creu("5 m de corda costen 8 €. Quant costen 12 m?", 8, 5, 12, "€", "m", None),
      creu("2 L de pintura pinten 18 m². Quants m² pinten 5 L?", 18, 2, 5, "m²", "L", None),
      creu("Un cotxe gasta 6 L cada 100 km. Quants litres gasta en 250 km?", 6, 100, 250, "L", "km", None),
      creu("3 kg de pomes costen 4,50 €. Quant costen 8 kg?", 4.5, 3, 8, "€", "kg", None),
      creu("4 m de tela costen 10 €. Quant costen 6 m?", 10, 4, 6, "€", "m", None),
      creu("En 2 hores, una màquina fa 150 peces. Quantes en fa en 6 hores?", 150, 2, 6, "peces", "h", None),
      creu("5 L de gasolina costen 8 €. Quant costen 30 L?", 8, 5, 30, "€", "L", None),
      creu("Per a 4 persones calen 300 g d'arròs. Quant en cal per a 10 persones?", 300, 4, 10, "g", "persones", None),
      creu("6 m² de terra costen 90 €. Quant costen 15 m²?", 90, 6, 15, "€", "m²", None),
      creu("Una aixeta omple 40 L en 5 minuts. Quants litres omple en 12 minuts?", 40, 5, 12, "L", "min", None),
      creu("8 kg de pinso costen 20 €. Quant costen 3 kg?", 20, 8, 3, "€", "kg", None),
      creu("Una impressora fa 45 còpies en 3 minuts. Quantes en fa en 7 minuts?", 45, 3, 7, "còpies", "min", None)]

B3R = [creu("6 € són 4 kg de taronges. Amb 15 €, quants kg en compres?", 4, 6, 15, "kg", "€", None),
       creu("8 € són 5 m de corda. Amb 20 €, quants metres en compres?", 5, 8, 20, "m", "€", None),
       creu("18 m² es pinten amb 2 L. Quants litres calen per a 45 m²?", 2, 18, 45, "L", "m²", None),
       creu("En 100 km es gasten 6 L. Quants km es fan amb 9 L?", 100, 6, 9, "km", "L", None),
       creu("4,50 € són 3 kg de pomes. Amb 12 €, quants kg en compres?", 3, 4.5, 12, "kg", "€", None),
       creu("150 peces es fan en 2 hores. Quantes hores calen per a 600 peces?", 2, 150, 600, "h", "peces", None),
       creu("300 g d'arròs són per a 4 persones. Amb 750 g, per a quantes persones n'hi ha?", 4, 300, 750, "persones", "g", None),
       creu("8 € són 5 L de gasolina. Amb 40 €, quants litres en compres?", 5, 8, 40, "L", "€", None),
       creu("90 € són 6 m² de terra. Amb 240 €, quants m² en compres?", 6, 90, 240, "m²", "€", None),
       creu("40 L s'omplen en 5 minuts. Quants minuts calen per a 100 L?", 5, 40, 100, "min", "L", None),
       creu("20 € són 8 kg de pinso. Amb 35 €, quants kg en compres?", 8, 20, 35, "kg", "€", None),
       creu("45 còpies es fan en 3 minuts. Quants minuts calen per a 120 còpies?", 3, 45, 120, "min", "còpies", None),
       creu("10 € són 4 m de tela. Amb 25 €, quants metres en compres?", 4, 10, 25, "m", "€", None)]

CAP3 = ["Què sabem", "Proporció", "En creu", "La x"]
A3C = [30, 20, 20, 18]

bloc3 = dict(
    titol="La proporció i el producte en creu", mira=(3, 6),
    nota_sol="Sempre igual: la x a dalt a l'esquerra, a sota el número que va amb ella, i a la dreta la parella "
             "que ja sabem. Es multiplica en creu, es fa el compte de la dreta i es divideix pel número de la x. "
             "<b>Error típic:</b> posar una magnitud a dalt d'una fracció i a baix de l'altra. Si el producte en "
             "creu no agafa, «quant val 1» (bloc 1) resol els mateixos problemes.",
    acts=[
        act("Escriu la proporció, multiplica en creu i troba la x.", [
            taula(CAP3, B3, omplir=(1, 2, 3), amples=A3C, esq=(0,))], ico="calc"),
        act("Ara la x són quilos, metres o litres. Escriu la proporció i troba la x.", [
            taula(CAP3, B3R, omplir=(1, 2, 3), amples=A3C, esq=(0,))],
            ico="calc", repte=True,
            nota_sol="La mateixa proporció, amb la pregunta girada: ara la x no són euros. La regla de la fitxa "
                     "ho resol: <b>a dalt, la mateixa magnitud que la x</b>. Qui ha après «els euros sempre a "
                     "dalt» s'equivoca aquí."),
    ])


# ------------------------------------------------- 4 · la inversa, a ull --

F = Fraction
VEGADES = {F(2): ("el doble", "la meitat"), F(3): ("el triple", "un terç"), F(4): ("el quàdruple", "un quart"),
           F(1, 2): ("la meitat", "el doble"), F(1, 3): ("un terç", "el triple"), F(1, 4): ("un quart", "el quàdruple")}


def inv(sabem, ara, n0, n1, t0, que):
    """Inversa: n0 persones (màquines…) triguen t0; amb n1, triguen t0 · n0 / n1."""
    mes, menys = VEGADES[F(n1, n0)]
    t1 = t0 * n0 / n1
    assert t1 == int(t1), (sabem, t1)
    return [sabem, ara, mes, f"{menys}: {num(t1)} {que}"]


B4 = [inv("2 pintors pinten la casa en 6 dies.", "I 4 pintors?", 2, 4, 6, "dies"),
      inv("3 aixetes omplen la piscina en 8 hores.", "I 6 aixetes?", 3, 6, 8, "hores"),
      inv("1 paleta fa el mur en 9 dies.", "I 3 paletes?", 1, 3, 9, "dies"),
      inv("2 cotxes fan 12 viatges per portar les caixes.", "I 4 cotxes?", 2, 4, 12, "viatges"),
      inv("4 amics paguen un regal: 10 € cadascú.", "I si són 8 amics?", 4, 8, 10, "€ cadascú"),
      inv("2 màquines fan la comanda en 12 hores.", "I 6 màquines?", 2, 6, 12, "hores"),
      inv("3 jardiners poden el parc en 10 dies.", "I 6 jardiners?", 3, 6, 10, "dies"),
      inv("1 autobús porta 60 persones de cada viatge.", "I si són 3 autobusos?", 1, 3, 60, "persones a cada un"),
      inv("2 amics inflen els globus en 20 minuts.", "I 4 amics?", 2, 4, 20, "minuts"),
      inv("5 persones munten l'envelat en 4 hores.", "I 10 persones?", 5, 10, 4, "hores"),
      inv("2 impressores fan les còpies en 30 minuts.", "I 6 impressores?", 2, 6, 30, "minuts"),
      inv("4 paletes fan el mur en 3 dies.", "I només 2 paletes?", 4, 2, 3, "dies"),
      inv("6 amics paguen el sopar: 8 € cadascú.", "I si només són 3 amics?", 6, 3, 8, "€ cadascú")]

B4R = [inv("2 pintors pinten la casa en 6 dies.", "I només 1 pintor?", 2, 1, 6, "dies"),
       inv("1 paleta fa el mur en 12 dies.", "I 4 paletes?", 1, 4, 12, "dies"),
       inv("6 aixetes omplen la piscina en 2 hores.", "I només 2 aixetes?", 6, 2, 2, "hores"),
       inv("3 cotxes fan 4 viatges per portar les caixes.", "I només 1 cotxe?", 3, 1, 4, "viatges"),
       inv("2 màquines fan la comanda en 8 hores.", "I 8 màquines?", 2, 8, 8, "hores"),
       inv("4 amics paguen un regal: 6 € cadascú.", "I si només són 2 amics?", 4, 2, 6, "€ cadascú"),
       inv("9 jardiners poden el parc en 2 dies.", "I només 3 jardiners?", 9, 3, 2, "dies"),
       inv("1 persona munta l'envelat en 20 hores.", "I 4 persones?", 1, 4, 20, "hores"),
       inv("8 amics inflen els globus en 5 minuts.", "I només 4 amics?", 8, 4, 5, "minuts"),
       inv("3 autobusos porten 40 persones cadascun.", "I si només n'hi ha 1?", 3, 1, 40, "persones"),
       inv("2 impressores fan les còpies en 40 minuts.", "I 8 impressores?", 2, 8, 40, "minuts"),
       inv("10 persones netegen la platja en 3 hores.", "I només 5 persones?", 10, 5, 3, "hores"),
       inv("12 amics paguen el sopar: 5 € cadascú.", "I si només són 4 amics?", 12, 4, 5, "€ cadascú")]

CAP4 = ["Què sabem", "I ara?", "Quantes vegades?", "Resposta"]
A4I = [34, 18, 16, 20]

bloc4 = dict(
    titol="La inversa, a ull", mira=(4, 9),
    nota_sol="Cap equació: el doble de persones triguen la meitat; el triple, un terç; la meitat, el doble. "
             "És el dibuix dels pintors de la pàgina 8 de la fitxa. Tots els números surten exactes. "
             "<b>Error típic:</b> amb menys gent, dir menys temps. Si passa, que digui en veu alta si menys gent "
             "ha de trigar més o menys.",
    acts=[
        act("Pensa si n'hi ha el doble, el triple o la meitat. Després escriu la resposta.", [
            taula(CAP4, B4, omplir=(2, 3), amples=A4I, esq=(0, 1))]),
        act("Ara n'hi pot haver menys, o quatre vegades més. Escriu la resposta.", [
            taula(CAP4, B4R, omplir=(2, 3), amples=A4I, esq=(0, 1))],
            repte=True,
            nota_sol="Hi surten el quàdruple (un quart del temps) i molts casos amb <b>menys</b> gent, on el temps "
                     "creix: un terç de les aixetes triguen el triple. És el pas que mostra si la inversa s'ha "
                     "entès o només s'ha memoritzat «el doble i la meitat»."),
    ])


# ------------------------------------------------- 5 · directa o inversa --

DI = ["Directa", "Inversa"]
D, I = 0, 1

bloc5 = dict(
    titol="Directa o inversa?", mira=(5, 10),
    nota_sol="Com a la fitxa: que es pregunti què passa amb el doble. El doble de litres, el doble de diners "
             "(directa); el doble d'aixetes, la meitat de temps (inversa).",
    acts=[
        act("Llegeix cada frase i marca si és proporcionalitat directa o inversa.", [
            tria([(t, DI, r) for t, r in (
                ("Si poses més litres de gasolina, pagues més diners.", D),
                ("Si un cotxe va més de pressa, triga menys temps a arribar.", I),
                ("Si compres més entrades de cinema, pagues més diners.", D),
                ("Si obres més aixetes, la banyera s'omple en menys temps.", I),
                ("Si un llibre té més pàgines, trigues més temps a llegir-lo.", D),
                ("Si hi ha més amics per pagar un regal, cadascú paga menys diners.", I),
                ("Si compres més quilos de taronges, pagues més diners.", D),
                ("Si hi ha més paletes per fer el mur, triguen menys dies.", I),
                ("Si fas més quilòmetres en cotxe, gastes més gasolina.", D),
                ("Si vénen més persones a la festa, necessites més pizzes.", D),
                ("Si hi ha més autobusos per a la mateixa excursió, a cada autobús hi va menys gent.", I),
                ("Si una trucada dura més minuts, costa més diners.", D),
                ("Si reparteixes l'aigua en més ampolles, a cada ampolla hi ha menys aigua.", I))])]),
        act("Mira la taula i marca si és directa o inversa.", [
            taula_tria([
                ("Les pomes.", ["Quilos", "Preu"], [["1", "2", "3"], ["3 €", "6 €", "9 €"]], D),
                ("Un pastís.", ["Amics", "Trossos"], [["2", "4", "8"], ["8", "4", "2"]], I),
                ("La bicicleta.", ["Hores", "Quilòmetres"], [["1", "2", "4"], ["5", "10", "20"]], D),
                ("Els pintors.", ["Pintors", "Dies"], [["1", "2", "4"], ["8", "4", "2"]], I),
                ("Les entrades.", ["Entrades", "Preu"], [["1", "2", "3"], ["5 €", "10 €", "15 €"]], D),
                ("La piscina.", ["Aixetes", "Hores"], [["1", "2", "3"], ["6", "3", "2"]], I),
                ("El suc.", ["Litres", "Preu"], [["2", "4", "6"], ["3 €", "6 €", "9 €"]], D),
                ("La mudança.", ["Cotxes", "Viatges"], [["1", "2", "4"], ["8", "4", "2"]], I),
                ("El llibre.", ["Pàgines", "Minuts"], [["10", "20", "30"], ["5", "10", "15"]], D),
                ("El regal.", ["Amics", "Cadascú paga"], [["2", "3", "6"], ["18 €", "12 €", "6 €"]], I),
                ("Les caixes.", ["Caixes", "Quilos"], [["1", "3", "5"], ["4", "12", "20"]], D),
                ("L'excursió.", ["Autobusos", "Persones a cada un"], [["1", "2", "5"], ["50", "25", "10"]], I),
                ("El viatge.", ["Velocitat (km/h)", "Minuts"], [["20", "40", "80"], ["120", "60", "30"]], I),
            ], DI)],
            repte=True,
            nota_sol="No hi ha frase: la relació s'ha de llegir als números. Que miri què passa quan la primera "
                     "fila es fa el doble: si la segona també es fa el doble, és directa; si es fa la meitat, és "
                     "inversa."),
    ])


# ------------------------------------------------- 6 · decideix i calcula --

def dec(situacio, tipus, resposta):
    return [situacio, tipus, resposta]


B6 = [dec("3 kg de pomes costen 6 €. Quant costen 6 kg?", "Directa", "el doble: 12 €"),
      dec("2 pintors pinten una casa en 8 dies. Quants dies triguen 4 pintors?", "Inversa", "la meitat: 4 dies"),
      dec("Per a 4 persones calen 2 ous. Quants ous calen per a 12 persones?", "Directa", "el triple: 6 ous"),
      dec("3 aixetes omplen una piscina en 6 hores. Quantes hores triga 1 aixeta?", "Inversa", "el triple: 18 hores"),
      dec("6 entrades costen 30 €. Quant costen 3 entrades?", "Directa", "la meitat: 15 €"),
      dec("2 màquines fan una comanda en 10 hores. Quantes hores triguen 4 màquines?", "Inversa", "la meitat: 5 hores"),
      dec("Un cotxe gasta 5 L en 100 km. Quants litres gasta en 200 km?", "Directa", "el doble: 10 L"),
      dec("4 amics paguen un regal: 9 € cadascú. Quant paga cadascú si són 12 amics?", "Inversa", "un terç: 3 €"),
      dec("2 L de pintura pinten 16 m². Quants m² pinten 6 L?", "Directa", "el triple: 48 m²"),
      dec("6 paletes fan un mur en 4 dies. Quants dies triguen 3 paletes?", "Inversa", "el doble: 8 dies"),
      dec("Per a 8 persones calen 400 g de pasta. Quanta en cal per a 4 persones?", "Directa", "la meitat: 200 g"),
      dec("1 aixeta omple la banyera en 30 minuts. Quants minuts triguen 3 aixetes?", "Inversa", "un terç: 10 minuts"),
      dec("5 llibretes costen 4 €. Quant costen 10 llibretes?", "Directa", "el doble: 8 €")]

B6R = [dec("3 kg de pomes costen 6 €. Quant costen 5 kg?", "Directa", "1 kg val 2 €: 10 €"),
       dec("2 pintors pinten una casa en 12 dies. Quants dies triguen 6 pintors?", "Inversa", "un terç: 4 dies"),
       dec("4 entrades costen 18 €. Quant costen 6 entrades?", "Directa", "1 entrada val 4,50 €: 27 €"),
       dec("8 amics paguen el sopar: 5 € cadascú. Quant paga cadascú si són 4 amics?", "Inversa", "el doble: 10 €"),
       dec("Per a 4 persones calen 300 g d'arròs. Quant en cal per a 6 persones?", "Directa", "1 persona, 75 g: 450 g"),
       dec("1 màquina fa la comanda en 20 hores. Quantes hores triguen 4 màquines?", "Inversa", "un quart: 5 hores"),
       dec("5 L de gasolina costen 8 €. Quant costen 7 L?", "Directa", "1 L val 1,60 €: 11,20 €"),
       dec("9 jardiners poden el parc en 2 dies. Quants dies triguen 3 jardiners?", "Inversa", "el triple: 6 dies"),
       dec("2 kg de taronges costen 3 €. Quant costen 5 kg?", "Directa", "1 kg val 1,50 €: 7,50 €"),
       dec("3 autobusos porten 50 persones cadascun. Quantes en porta cada un si són 6?", "Inversa", "la meitat: 25"),
       dec("6 iogurts costen 2,40 €. Quant costen 4 iogurts?", "Directa", "1 iogurt val 0,40 €: 1,60 €"),
       dec("4 aixetes omplen la piscina en 3 hores. Quantes hores triga 1 aixeta?", "Inversa", "el quàdruple: 12 hores"),
       dec("10 m de corda costen 15 €. Quant costen 4 m?", "Directa", "1 m val 1,50 €: 6 €")]

CAP6 = ["Situació", "Directa o inversa?", "Resposta"]
A6 = [50, 16, 22]

bloc6 = dict(
    titol="Decideix i calcula", mira=(6, 11),
    nota_sol="Primer es decideix, després es calcula. Totes les d'aquesta activitat es fan a ull (el doble, el "
             "triple, la meitat). <b>Error típic:</b> amb una aixeta sola, dir menys temps (fer-ho com si fos "
             "directa). L'avís de la fitxa és l'antídot: la resposta ha de ser més gran o més petita?",
    acts=[
        act("Primer decideix si és directa o inversa. Després calcula la resposta.", [
            taula(CAP6, B6, omplir=(1, 2), amples=A6, esq=(0,))]),
        act("Primer decideix si és directa o inversa. Després calcula la resposta.", [
            taula(CAP6, B6R, omplir=(1, 2), amples=A6, esq=(0,))],
            ico="calc", repte=True,
            nota_sol="Les inverses encara es fan a ull, però les directes ja no són el doble ni el triple: cal "
                     "passar per quant val 1 (o pel producte en creu). Decidir el camí és el repte."),
    ])


# ------------------------------------------------- 9 · quant val 1 cm del plànol --

bloc7 = dict(
    titol="Quant val 1 cm del plànol", mira=(9, 14),
    nota_sol="<b>Error típic:</b> amb escales com 1 : 50 o 1 : 20, dir que 50 cm són 5 m. Si passa, "
             "torneu a la taula de la pàgina 13 de la fitxa: 100 cm = 1 m.",
    acts=[
        act("Escriu quant val un centímetre del plànol a cada escala.", [
            taula(["Escala", "1 cm són… (cm)", "és a dir (m)"],
                  [[esc(e), f"{num(e)} cm", f"{num(e / 100)} m"]
                   for e in (100, 300, 400, 1000, 200, 600, 500, 50, 150, 800, 10000, 250, 2000)],
                  omplir=(1, 2), amples=A3)]),
        act("Escriu l'escala de cada plànol.", [
            taula(["1 cm són… (m)", "és a dir (cm)", "Escala"],
                  [[f"{num(e / 100)} m", f"{num(e)} cm", esc(e)]
                   for e in (300, 200, 1000, 400, 500, 250, 50, 2000, 150, 5000, 25, 10000, 20)],
                  omplir=(1, 2), amples=A3)],
            repte=True,
            nota_sol="El camí al revés: de «1 cm són 3 m» a l'escala. Primer cal passar els metres a "
                     "centímetres (× 100), i aquest número és l'escala. Els d'escala petita (50, 25, 20) "
                     "surten de mig metre o menys: són els que costen més."),
    ])


# ------------------------------------------------- 10 · del plànol a la realitat --

bloc8 = dict(
    titol="Del plànol a la realitat", mira=(10, 14),
    nota_sol="Sempre la mateixa cadena: <i>× l'escala</i> i després <i>÷ 100</i>. <b>Error típic:</b> "
             "oblidar el segon pas i deixar el resultat en centímetres (600 m en lloc de 6 m).",
    acts=[
        act("Calcula quant fa de veritat.", [
            taula(["Escala", "Al plànol", "× escala", "De veritat"],
                  [[esc(e), f"{num(c)} cm", f"{num(c * e)} cm", f"{num(c * e / 100)} m"]
                   for e, c in ((100, 4), (100, 7), (100, 3.5), (50, 6), (200, 3), (200, 5), (50, 10),
                                (500, 3), (100, 8.5), (200, 4.5), (300, 2), (50, 9), (1000, 4))],
                  omplir=(2, 3), amples=A4)], ico="calc"),
        act("Mesura cada línia amb el regle i calcula quant fa de veritat.", [
            taula(["Línia", "Mesura", "De veritat"],
                  [[l, f"{num(c)} cm", f"{num(c)} m"] for l, c in zip("ABCD", (4, 6, 2.5, 8))],
                  omplir=(1, 2), amples=A3, abans=nota("Plànol a escala 1 : 100.") + linies([4, 6, 2.5, 8])),
            taula(["Línia", "Mesura", "De veritat"],
                  [[l, f"{num(c)} cm", f"{num(c)} m"] for l, c in zip("EFG", (5, 3.5, 7))],
                  omplir=(1, 2), amples=A3, abans=linies([5, 3.5, 7], primera=4)),
            taula(["Línia", "Mesura", "De veritat"],
                  [[l, f"{num(c)} cm", f"{num(c)} m"] for l, c in zip("HIJKLM", (9, 1.5, 4.5, 6.5, 10, 3))],
                  omplir=(1, 2), amples=A3, abans=linies([9, 1.5, 4.5, 6.5, 10, 3], primera=7),
                  sol_nota="Les línies són de mida real si s'imprimeix al 100 %, sense «ajustar a la "
                           "pàgina». Si la impressora escala el full, accepteu la mesura que surti i mireu "
                           "només la conversió.")],
            ico="regle", repte=True,
            nota_sol="La dada no la dona el paper: l'ha de mesurar. És el graó físic de la unitat (la cinta "
                     "mètrica) portat al quadern. A 1 : 100, els centímetres que mesura són els metres."),
    ])


# ------------------------------------------------- 11 · el plànol --

def mides(espais, factor):
    """[nom, «w × h cm», «W × H m»] per a cada espai d'un plànol, amb el factor de l'escala."""
    return [[e[0], f"{num(e[3])} × {num(e[4])} cm", f"{num(e[3] * factor)} × {num(e[4] * factor)} m"]
            for e in espais]

CAP5 = ["Què és", "Al plànol", "De veritat"]
PIS = [("Sala", 0, 0, 6, 4), ("Habitació", 6, 0, 3, 3), ("Bany", 6, 3, 3, 1.5), ("Cuina", 0, 4, 4, 2)]
BOTIGA = [("Botiga", 0, 0, 7, 5), ("Magatzem", 7, 0, 3, 3), ("Lavabo", 7, 3, 3, 2)]
APARTAMENT = [("Menjador", 0, 0, 3, 2), ("Habitació", 3, 0, 2, 2), ("Cuina", 0, 2, 3, 1.5)]
HABITACIO = [("Habitació", 0, 0, 8, 6), ("Llit", 0.4, 0.4, 4, 2, "moble"),
             ("Armari", 4.8, 0.4, 3, 1, "moble"), ("Taula", 5.2, 4.4, 2.4, 1.2, "moble")]

CASA = [("Sala", 0, 0, 5, 4), ("Habitació", 5, 0, 4, 3), ("Bany", 5, 3, 2, 2), ("Cuina", 0, 4, 3, 2)]
PIS2 = [("Sala", 0, 0, 4, 4), ("Habitació", 4, 0, 3, 3), ("Rebedor", 4, 3, 3, 1.5)]
BOTIGA2 = [("Botiga", 0, 0, 6, 5), ("Magatzem", 6, 0, 3, 2), ("Lavabo", 6, 2, 2, 2)]
ESCOLA = [("Aula", 0, 0, 8, 6), ("Despatx", 8, 0, 3, 3), ("Passadís", 0, 6, 8, 2)]

def superficies(espais):
    return [[e[0], f"{num(e[3])} × {num(e[4])} cm", f"{num(e[3])} × {num(e[4])} m", f"{num(e[3] * e[4])} m²"]
            for e in espais]

CAP5R = ["Espai", "Al plànol", "De veritat", "Superfície"]

bloc9 = dict(
    titol="El plànol", mira=(11, 15),
    nota_sol="A 1 : 100, els centímetres del plànol són els metres de veritat: el número no canvia. A les "
             "escales 1 : 200 i 1 : 50 (només a elevat) sí que canvia, i és on es veu si ha entès la cadena. "
             "Els plànols a 1 : 100 són de mida real si s'imprimeix al 100 %; el de 1 : 200 està dibuixat "
             "el doble de gran perquè hi càpiguen els noms.",
    acts=[
        act("Calcula les mides de veritat.", [
            taula(CAP5, mides(PIS, 1), omplir=(2,), amples=A3,
                  abans=nota("Plànol d'un pis a escala 1 : 100.") + planol(PIS, aria="Plànol d'un pis")),
            taula(CAP5, mides(BOTIGA, 1), omplir=(2,), amples=A3,
                  abans=nota("Plànol d'una botiga a escala 1 : 100.") + planol(BOTIGA, aria="Plànol d'una botiga")),
            taula(CAP5, mides(APARTAMENT, 2), omplir=(2,), amples=A3,
                  abans=nota("Plànol d'un apartament a escala 1 : 200.")
                        + planol(APARTAMENT, zoom=2, aria="Plànol d'un apartament"),
                  sol_nota="A 1 : 200, cada centímetre són 2 m: es multiplica per 2. <b>Error típic:</b> "
                           "copiar els números del plànol com si fos 1 : 100."),
            taula(CAP5, mides(HABITACIO[1:], 0.5), omplir=(2,), amples=A3,
                  abans=nota("Plànol d'una habitació a escala 1 : 50.")
                        + planol(HABITACIO, mides=False, aria="Plànol d'una habitació amb un llit, un armari i una taula"),
                  sol_nota="A 1 : 50, cada centímetre són 0,5 m: el que és de veritat fa la meitat del "
                           "número del plànol."),
        ], ico="regle"),
        act("Calcula la superfície de veritat de cada espai.", [
            taula(CAP5R, superficies(CASA), omplir=(2, 3), amples=A4,
                  abans=nota("Plànol d'una casa a escala 1 : 100.") + planol(CASA, aria="Plànol d'una casa")),
            taula(CAP5R, superficies(PIS2), omplir=(2, 3), amples=A4,
                  abans=nota("Plànol d'un pis a escala 1 : 100.") + planol(PIS2, aria="Plànol d'un pis")),
            taula(CAP5R, superficies(BOTIGA2), omplir=(2, 3), amples=A4,
                  abans=nota("Plànol d'una botiga a escala 1 : 100.") + planol(BOTIGA2, aria="Plànol d'una botiga")),
            taula(CAP5R, superficies(ESCOLA), omplir=(2, 3), amples=A4,
                  abans=nota("Plànol d'una escola a escala 1 : 100.") + planol(ESCOLA, aria="Plànol d'una escola")),
        ], ico="calc", repte=True,
            nota_sol="Un pas més que la fitxa: després de les mides, la superfície (llarg × ample). És la "
                     "columna que el solucionari de la fitxa deixava com a ampliació."),
    ])


# ------------------------------------------------- 7 · a la vida de cada dia · les creps --

CAP10 = ["Pregunta", "Resposta"]
A10 = [62, 26]

def preguntes(*files, context, sol_nota="", recta=None):
    """recta = (marques, grams per persona, què és): la doble recta persones | grams, com a la fitxa."""
    dib = ""
    if recta:
        n, g, que = recta
        dib = doble_recta(n, g, dalt="persones", baix=f"{que} (g)", aria=f"Doble recta: persones i grams de {que}")
    return taula(CAP10, [list(f) for f in files], omplir=(1,), amples=A10, esq=(0,),
                 abans=nota(context) + dib, sol_nota=sol_nota)

bloc10 = dict(
    titol="A la vida de cada dia · les creps", mira=(7, 12),
    nota_sol="Sempre el mateix pas: quant val 1 (una persona) dividint, i després multiplicar. Les preguntes "
             "que van al revés («amb 10 ous, per a quantes persones?»), com els 350 g de la fitxa, són les que "
             "mostren si ho ha entès.",
    acts=[
        act("Calcula primer quant en cal per a 1 persona. Després respon.", [
            preguntes(("Quants ous calen per a 1 persona?", "8 ÷ 4 = 2 ous"),
                      ("I per a 6 persones?", "2 × 6 = 12 ous"),
                      ("Amb 10 ous, per a quantes persones n'hi ha prou?", "10 ÷ 2 = 5 persones"),
                      ("Per fer una truita per a més persones, necessites més ous. És directa o inversa?", "Directa"),
                      context="Una truita per a 4 persones porta 8 ous."),
            preguntes(("Quanta pasta cal per a 1 persona?", "400 ÷ 4 = 100 g"),
                      ("I per a 3 persones?", "100 × 3 = 300 g"),
                      ("Amb 700 g, per a quantes persones n'hi ha prou?", "700 ÷ 100 = 7 persones"),
                      context="Uns macarrons per a 4 persones porten 400 g de pasta."),
            preguntes(("Quanta llet cal per a 1 persona?", "300 ÷ 2 = 150 mL"),
                      ("I per a 5 persones?", "150 × 5 = 750 mL"),
                      ("Amb 900 mL, per a quantes persones n'hi ha prou?", "900 ÷ 150 = 6 persones"),
                      context="Un batut per a 2 persones porta 300 mL de llet."),
            preguntes(("Quant val 1 entrada?", "35 ÷ 5 = 7 €"),
                      ("I 8 entrades?", "7 × 8 = 56 €"),
                      ("Amb 49 €, quantes entrades pots comprar?", "49 ÷ 7 = 7 entrades"),
                      context="5 entrades de cinema costen 35 €."),
        ], ico="calc"),
        act("Fes servir la doble recta per respondre.", [
            preguntes(("Quanta farina cal per a 1 persona?", "50 g"),
                      ("I per a 6 persones?", "300 g"),
                      ("I per a 9 persones?", "450 g"),
                      ("Amb 250 g, per a quantes persones n'hi ha prou?", "5 persones"),
                      context="Unes creps per a 4 persones porten 200 g de farina.", recta=(8, 50, "farina")),
            preguntes(("Quant sucre cal per a 1 persona?", "20 g"),
                      ("I per a 5 persones?", "100 g"),
                      ("Amb 120 g, per a quantes persones n'hi ha prou?", "6 persones"),
                      context="Un pastís per a 3 persones porta 60 g de sucre.", recta=(6, 20, "sucre")),
            preguntes(("Quants grams de xocolata calen per a 1 persona?", "25 g"),
                      ("I per a 8 persones?", "200 g"),
                      ("Amb 150 g, per a quantes persones n'hi ha prou?", "6 persones"),
                      context="Unes galetes per a 2 persones porten 50 g de xocolata.", recta=(8, 25, "xocolata")),
            preguntes(("Quant arròs cal per a 1 persona?", "75 g"),
                      ("I per a 6 persones?", "450 g"),
                      ("Amb 375 g, per a quantes persones n'hi ha prou?", "5 persones"),
                      context="Una paella per a 4 persones porta 300 g d'arròs.", recta=(6, 75, "arròs")),
        ], repte=True,
            nota_sol="La doble recta lliga persones i grams (com a la fitxa): 1 persona a dalt, els seus grams a "
                     "baix. Les preguntes al revés es llegeixen de baix a dalt. Qui no la necessiti pot fer els "
                     "comptes."),
    ])


# ------------------------------------------------- 8 · a la vida de cada dia · els globus --

def amics(context, *files, sol_nota=""):
    return preguntes(*files, context=context, sol_nota=sol_nota)

bloc11 = dict(
    titol="A la vida de cada dia · els globus", mira=(8, 12),
    nota_sol="La inversa a ull, en el context de la festa. Com a la fitxa, totes comencen per «més amics», però "
             "aquí el temps baixa: el doble d'amics triguen la meitat.",
    acts=[
        act("Calcula quant temps triguen. Pensa en el doble, el triple o la meitat.", [
            amics("2 amics inflen tots els globus en 30 minuts.",
                  ("I si són 4 amics?", "la meitat: 15 minuts"),
                  ("I si només hi ha 1 amic?", "el doble: 60 minuts"),
                  ("I si són 6 amics?", "un terç: 10 minuts"),
                  ("Si hi ha més amics per inflar els globus, triguen menys temps. És directa o inversa?", "Inversa")),
            amics("3 amics paren les taules en 12 minuts.",
                  ("I si són 6 amics?", "la meitat: 6 minuts"),
                  ("I si són 9 amics?", "un terç: 4 minuts"),
                  ("I si només hi ha 1 amic?", "el triple: 36 minuts")),
            amics("2 amics netegen la sala en 40 minuts.",
                  ("I si són 4 amics?", "la meitat: 20 minuts"),
                  ("I si són 8 amics?", "un quart: 10 minuts"),
                  ("I si només hi ha 1 amic?", "el doble: 80 minuts")),
            amics("4 amics paguen el pastís: 6 € cadascú.",
                  ("I si són 8 amics?", "la meitat: 3 € cadascú"),
                  ("I si són 12 amics?", "un terç: 2 € cadascú"),
                  ("I si només són 2 amics?", "el doble: 12 € cadascú")),
        ]),
        act("Primer decideix si és directa o inversa. Després respon.", [
            taula(CAP6, [
                dec("A la festa, 4 amics mengen 2 pizzes. Quantes pizzes mengen 8 amics?", "Directa", "el doble: 4 pizzes"),
                dec("2 amics inflen els globus en 30 minuts. Quant triguen 6 amics?", "Inversa", "un terç: 10 minuts"),
                dec("Per a 5 persones calen 2 L de refresc. Quants litres calen per a 10?", "Directa", "el doble: 4 L"),
                dec("4 amics paguen el pastís: 6 € cadascú. Quant paga cadascú si són 8?", "Inversa", "la meitat: 3 €"),
                dec("3 amics fan 60 entrepans en 1 hora. Quants en fan 6 amics en 1 hora?", "Directa", "el doble: 120"),
                dec("3 amics fan 60 entrepans en 1 hora. Quant triguen 6 amics a fer-ne 60?", "Inversa", "la meitat: 30 minuts"),
                dec("Un got de suc per persona: 10 persones, 10 gots. I 25 persones?", "Directa", "25 gots"),
                dec("2 amics paren les taules en 20 minuts. Quant triguen 4 amics?", "Inversa", "la meitat: 10 minuts"),
                dec("6 globus costen 3 €. Quant costen 18 globus?", "Directa", "el triple: 9 €"),
                dec("1 amic sol neteja la sala en 60 minuts. Quant triguen 3 amics?", "Inversa", "un terç: 20 minuts"),
                dec("Per a 4 persones calen 2 bosses de patates. Quantes per a 12?", "Directa", "el triple: 6 bosses"),
                dec("6 amics paguen la música: 5 € cadascú. Quant paga cadascú si només són 3?", "Inversa", "el doble: 10 €"),
                dec("Per a 3 persones calen 300 g de pastís. Quant en cal per a 9?", "Directa", "el triple: 900 g"),
            ], omplir=(1, 2), amples=A6, esq=(0,))],
            repte=True,
            nota_sol="Directes i inverses barrejades, totes de la mateixa festa. Els apartats e) i f) són la mateixa "
                     "situació amb dues preguntes: més amics fan <b>més</b> entrepans en una hora (directa), i "
                     "triguen <b>menys</b> a fer-ne els mateixos (inversa)."),
    ])


# ------------------------------------------------- 12 · a la vida de cada dia · el mapa --

def mapa(per_cm, *recorreguts):
    return [[r, f"{num(c)} cm", f"{num(c * per_cm)} m"] for r, c in recorreguts]

CAP7 = ["Recorregut", "Al mapa", "De veritat"]
A7 = [52, 18, 18]
def al_mapa(per_cm, *metres):
    return [[f"{num(m)} m", f"{num(m)} ÷ {num(per_cm)}", f"{num(m / per_cm)} cm"] for m in metres]

CAP7R = ["De veritat", "Compte", "Al mapa"]

bloc12 = dict(
    titol="A la vida de cada dia · el mapa", mira=(12, 16),
    nota_sol="La doble recta només arriba fins a uns quants centímetres: els apartats que en surten s'han "
             "de continuar fora del dibuix, multiplicant. Si la vol allargar amb el regle, deixeu-l'hi fer.",
    acts=[
        act("Calcula les distàncies de veritat al mapa.", [
            taula(CAP7, mapa(100, ("De casa a l'escola", 4), ("De casa al parc", 3), ("De casa a la piscina", 7),
                             ("De casa a la biblioteca", 2.5)), omplir=(2,), amples=A7, esq=(0,),
                  abans=nota("Al mapa del barri, 1 cm són 100 m de veritat.") + doble_recta(5, 100)),
            taula(CAP7, mapa(20, ("Fins a la font", 3), ("Fins als gronxadors", 5), ("Fins al bar", 8)),
                  omplir=(2,), amples=A7, esq=(0,),
                  abans=nota("Al mapa del parc, 1 cm són 20 m de veritat.") + doble_recta(6, 20)),
            taula(CAP7, mapa(50, ("De casa al mercat", 4), ("De casa a la farmàcia", 2), ("De casa a l'estació", 10)),
                  omplir=(2,), amples=A7, esq=(0,),
                  abans=nota("Al mapa del poble, 1 cm són 50 m de veritat.") + doble_recta(6, 50)),
            taula(CAP7, mapa(200, ("Del poble al riu", 3), ("Del poble a l'ermita", 5), ("Del poble al càmping", 1.5)),
                  omplir=(2,), amples=A7, esq=(0,),
                  abans=nota("Al mapa de la comarca, 1 cm són 200 m de veritat.") + doble_recta(5, 200)),
        ], ico="regle"),
        act("Calcula quants centímetres fa cada distància al mapa.", [
            taula(CAP7R, al_mapa(50, 150, 250, 400, 75), omplir=(1, 2), amples=A3,
                  abans=nota("Al mapa, 1 cm són 50 m de veritat.") + doble_recta(6, 50)),
            taula(CAP7R, al_mapa(100, 300, 650, 1000), omplir=(1, 2), amples=A3,
                  abans=nota("En un altre mapa, 1 cm són 100 m de veritat.")),
            taula(CAP7R, al_mapa(20, 60, 100, 30), omplir=(1, 2), amples=A3,
                  abans=nota("Al mapa del parc, 1 cm són 20 m de veritat.")),
            taula(CAP7R, al_mapa(200, 800, 1200, 300), omplir=(1, 2), amples=A3,
                  abans=nota("Al mapa de la comarca, 1 cm són 200 m de veritat.")),
        ], ico="calc", repte=True,
            nota_sol="El camí al revés: dels metres al mapa es divideix. A la doble recta, és llegir de baix a "
                     "dalt. Els que surten amb decimals (75 m → 1,5 cm, 650 m → 6,5 cm) cauen entre dues "
                     "marques."),
    ])


# El mateix ordre que la fitxa: Part 1 (blocs dels exercicis 1-8) i Part 2 (9-12).
BLOCS = [bloc1, bloc2, bloc3, bloc4, bloc5, bloc6, bloc10, bloc11, bloc7, bloc8, bloc9, bloc12]
