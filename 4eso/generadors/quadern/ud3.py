"""Quadern d'activitats de la Unitat 3 · Proporcionalitat i escales.

    python3 generadors/gen_quadern.py 3        (des de 4eso/)

Un bloc per cada exercici de la fitxa (fitxes/ud3.html), en el mateix ordre. A cada bloc,
una activitat germana i una de repte. Cada activitat té 13 apartats: l'a), resolt, i
12 per fer. El filtre en deixa 3 (petit), 6 (mitjà) o tots 12 (elevat), sempre els
primers: per això els apartats van de menys a més (els de 1 : 100 abans que els de
1 : 50, els que no cal continuar fora del dibuix abans que els que sí).

Els números es calculen aquí, no s'escriuen a mà: així el solucionari no es pot equivocar.
Com a la fitxa: la conversió va sempre amb la mateixa cadena (× l'escala, ÷ 100, o
× 100, ÷ l'escala), la calculadora fa el compte, i a les ofertes hi ha apartats on
guanya el format petit (la regla trencada de la unitat). Ja entre els tres primers,
perquè també surti a petit.
"""
from gen_quadern import act, taula, tria, taula_tria, ofertes, quadricula, planol, doble_recta, linies
from gen_quadern import num, eur, esc, nota

NUM = 3
TITOL = "Escales i proporcionalitat"
AVALUAR = ("Com a la fitxa, l'objectiu no és calcular bé: és saber en quin sentit va la conversió "
           "(del plànol a la realitat es multiplica, de la realitat al plànol es divideix) i decidir. "
           "Un error de divisió no hauria de fer baixar la valoració si la cadena és correcta. Les "
           "activitats de repte compten per als nivells alts (AN, AE), no per al mínim.")

A3 = [30, 30, 30]
A4 = [22, 22, 22, 22]


# ------------------------------------------------- 1 · quant val 1 cm del plànol --

bloc1 = dict(
    titol="Quant val 1 cm del plànol", mira=(1, 5),
    nota_sol="<b>Error típic:</b> amb escales com 1 : 50 o 1 : 20, dir que 50 cm són 5 m. Si passa, "
             "torneu a la taula de la pàgina 1 de la fitxa: 100 cm = 1 m.",
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


# ------------------------------------------------- 2 · del plànol a la realitat --

bloc2 = dict(
    titol="Del plànol a la realitat", mira=(2, 5),
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


# ------------------------------------------------- 3 · de la realitat al plànol --

bloc3 = dict(
    titol="De la realitat al plànol", mira=(3, 6),
    nota_sol="Ara la cadena va al revés: <i>× 100</i> per passar a centímetres i <i>÷ l'escala</i>. "
             "<b>Atenció a les escales 1 : 50:</b> el dibuix surt més gran que a 1 : 100 (3 m fan 6 cm, "
             "no 3 cm), com l'apartat c de la fitxa.",
    acts=[
        act("Calcula quant ha de fer al plànol.", [
            taula(["Escala", "De veritat", "× 100", "Al plànol"],
                  [[esc(e), f"{num(m)} m", f"{num(m * 100)} cm", f"{num(m * 100 / e)} cm"]
                   for e, m in ((100, 4), (100, 7), (100, 2.5), (200, 6), (200, 10), (50, 2), (500, 30),
                                (50, 3), (50, 1.5), (500, 20), (100, 9.5), (1000, 50), (200, 5))],
                  omplir=(2, 3), amples=A4)], ico="calc"),
        act("Dibuixa cada paret a escala 1 : 100.", [
            quadricula([5, 3, 8, 6.5, 4, 9, 2.5, 7, 10, 5.5, 11, 1.5, 7.5], abans=nota("Cada quadret fa 1 cm."))],
            ico="llapis", repte=True,
            nota_sol="El resultat no s'escriu: es dibuixa. A 1 : 100, 1 m de veritat és 1 cm, o sigui un "
                     "quadret. Si s'imprimeix escalat, els quadrets continuen sent la unitat: compteu "
                     "quadrets, no centímetres."),
    ])


# ------------------------------------------------- 4 · directa o inversa --

DI = ["Directa", "Inversa"]
D, I = 0, 1

bloc4 = dict(
    titol="Directa o inversa?", mira=(4, 6),
    nota_sol="Com a la fitxa: si dubta, que digui en veu alta les dues meitats, «més… i més…» o "
             "«més… i menys…». La paraula «menys» ja li dona la resposta.",
    acts=[
        act("Marca si és proporcionalitat directa o inversa.", [
            tria([(t, DI, r) for t, r in (
                ("Més litres de gasolina, més diners.", D),
                ("Més velocitat, menys temps per arribar.", I),
                ("Més entrades de cinema, més diners.", D),
                ("Més aixetes obertes, menys temps per omplir la banyera.", I),
                ("Més pàgines, més temps per llegir el llibre.", D),
                ("Més amics per pagar un regal, menys diners cadascú.", I),
                ("Més quilos de taronges, més diners.", D),
                ("Més paletes, menys dies per fer el mur.", I),
                ("Més quilòmetres en cotxe, més gasolina.", D),
                ("Més persones a la festa, més pizzes.", D),
                ("Més autobusos, menys persones a cada autobús.", I),
                ("Més minuts de trucada, més diners.", D),
                ("Més ampolles per repartir l'aigua, menys aigua a cada ampolla.", I))],
                en_linia=True)]),
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
            nota_sol="No hi ha frase: la relació s'ha de llegir als números. És el pas de la pàgina 4 de la "
                     "fitxa, on les fletxes ↑ ↓ de sota de cada taula ho deien. Si costa, que hi dibuixi les "
                     "fletxes."),
    ])


# ------------------------------------------------- 5 · el plànol --

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

bloc5 = dict(
    titol="El plànol", mira=(5, 7),
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


# ------------------------------------------------- 6 · quina oferta surt més a compte --

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

bloc6 = dict(
    titol="Quina oferta surt més a compte", mira=(6, 8),
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


# ------------------------------------------------- 7 · el mapa --

def mapa(per_cm, *recorreguts):
    return [[r, f"{num(c)} cm", f"{num(c * per_cm)} m"] for r, c in recorreguts]

CAP7 = ["Recorregut", "Al mapa", "De veritat"]
A7 = [52, 18, 18]

def al_mapa(per_cm, *metres):
    return [[f"{num(m)} m", f"{num(m)} ÷ {num(per_cm)}", f"{num(m / per_cm)} cm"] for m in metres]

CAP7R = ["De veritat", "Compte", "Al mapa"]

bloc7 = dict(
    titol="A la vida de cada dia · el mapa", mira=(7, 9),
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


# ------------------------------------------------- 8 · baixar a un --

CAP8 = ["Pregunta", "Resposta"]
A8 = [62, 26]

def preguntes(*files, context, sol_nota=""):
    return taula(CAP8, [list(f) for f in files], omplir=(1,), amples=A8, esq=(0,),
                 abans=nota(context), sol_nota=sol_nota)

bloc8 = dict(
    titol="A la vida de cada dia · baixar a un", mira=(8, 9),
    nota_sol="Sempre el mateix pas: baixar a un (una persona, una entrada) dividint, i després multiplicar. "
             "Les preguntes que van al revés («amb 10 ous, per a quantes persones?»), com el 350 g de la "
             "fitxa, són les que mostren si ho ha entès.",
    acts=[
        act("Baixa a un i després calcula.", [
            preguntes(("Quants ous calen per a 1 persona?", "8 ÷ 4 = 2 ous"),
                      ("I per a 6 persones?", "2 × 6 = 12 ous"),
                      ("Amb 10 ous, per a quantes persones n'hi ha prou?", "10 ÷ 2 = 5 persones"),
                      ("Més persones, més ous. És directa o inversa?", "Directa"),
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
        act("Baixa a un i després calcula.", [
            preguntes(("Quants dies tardaria 1 pintor sol?", "6 × 2 = 12 dies"),
                      ("I 3 pintors?", "12 ÷ 3 = 4 dies"),
                      ("I 4 pintors?", "12 ÷ 4 = 3 dies"),
                      ("Més pintors, menys dies. És directa o inversa?", "Inversa"),
                      context="2 pintors pinten una casa en 6 dies."),
            preguntes(("Quantes hores tardaria 1 aixeta sola?", "4 × 3 = 12 hores"),
                      ("I 6 aixetes?", "12 ÷ 6 = 2 hores"),
                      ("I 2 aixetes?", "12 ÷ 2 = 6 hores"),
                      context="3 aixetes omplen una piscina en 4 hores."),
            preguntes(("Quant pagaria 1 amic sol?", "6 × 4 = 24 €"),
                      ("I si són 8 amics?", "24 ÷ 8 = 3 € cadascú"),
                      ("I si són 3 amics?", "24 ÷ 3 = 8 € cadascú"),
                      context="4 amics paguen un regal: 6 € cadascú."),
            preguntes(("Quants viatges faria 1 cotxe sol?", "6 × 2 = 12 viatges"),
                      ("I 3 cotxes?", "12 ÷ 3 = 4 viatges"),
                      ("I 4 cotxes?", "12 ÷ 4 = 3 viatges"),
                      context="Per portar les caixes, 2 cotxes fan 6 viatges."),
        ], ico="calc", repte=True,
            nota_sol="La mateixa idea de baixar a un, en una inversa: un sol pintor tarda <b>més</b>, i per "
                     "això aquí primer es multiplica (6 × 2) i després es divideix. <b>Error típic:</b> "
                     "6 ÷ 2 = 3 dies per a 1 pintor. Si passa, que digui en veu alta si un pintor sol ha de "
                     "tardar més o menys."),
    ])


BLOCS = [bloc1, bloc2, bloc3, bloc4, bloc5, bloc6, bloc7, bloc8]
