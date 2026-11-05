"""Quadern d'activitats de la Unitat 3 · Proporcionalitat i escales.

    python3 generadors/gen_quadern.py 3        (des de 4eso/)

Un bloc per cada exercici de la fitxa (fitxes/ud3.html), en el mateix ordre. A cada bloc:
quatre germanes (n = 1, 2, 3, 3) i dues de repte (la primera surt a petit o a mitjà,
la segona només a elevat). Els números es calculen aquí, no s'escriuen a mà: així el
solucionari no es pot equivocar.

Com a la fitxa: la conversió va sempre amb la mateixa cadena (× l'escala, ÷ 100, o
× 100, ÷ l'escala), la calculadora fa el compte, i a les ofertes hi ha apartats on
guanya el format petit (la regla trencada de la unitat: el paquet gran no sempre surt
més barat).
"""
from gen_quadern import act, taula, tria, ofertes, taula_fila, planol, doble_recta, linies, quadricula
from gen_quadern import num, eur, esc, ms, BUIT

NUM = 3
TITOL = "Escales i proporcionalitat"
AVALUAR = ("Com a la fitxa, l'objectiu no és calcular bé: és saber en quin sentit va la conversió "
           "(del plànol a la realitat es multiplica, de la realitat al plànol es divideix) i decidir. "
           "Un error de divisió no hauria de fer baixar la valoració si la cadena és correcta. Les "
           "activitats de repte compten per als nivells alts (AN, AE), no per al mínim.")


# ------------------------------------------------- 1 · quant val 1 cm del plànol --

def val_cm(*escales):
    return [[esc(e), f"{num(e)} cm", f"{num(e / 100)} m"] for e in escales]

CAP1 = ["Escala", "1 cm són… (cm)", "és a dir (m)"]
Q1 = "Escriu quant val un centímetre del plànol a cada escala."

bloc1 = dict(
    titol="Quant val 1 cm del plànol", mira=(1, 5),
    nota_sol="<b>Error típic:</b> amb escales com 1 : 50 o 1 : 20, dir que 50 cm són 5 m. Si passa, "
             "torneu a la taula de la pàgina 1 de la fitxa: 100 cm = 1 m.",
    acts=[
        act(1, taula(Q1, CAP1, val_cm(100, 300, 400, 1000), omplir=(1, 2), amples=[30, 30, 30])),
        act(2, taula(Q1, CAP1, val_cm(200, 600, 20, 5000), omplir=(1, 2), amples=[30, 30, 30])),
        act(3, taula(Q1, CAP1, val_cm(50, 150, 800, 10000), omplir=(1, 2), amples=[30, 30, 30])),
        act(3, taula(Q1, CAP1, val_cm(500, 250, 2000, 25), omplir=(1, 2), amples=[30, 30, 30])),
        act(2, taula("Escriu l'escala de cada plànol.",
                     ["1 cm són… (m)", "és a dir (cm)", "Escala"],
                     [[f"{num(e / 100)} m", f"{num(e)} cm", esc(e)] for e in (300, 200, 50, 1000)],
                     omplir=(1, 2), amples=[30, 30, 30]),
            repte=True,
            nota_sol="El camí al revés: de «1 cm són 3 m» a l'escala. Primer cal passar els metres a "
                     "centímetres (× 100), i aquest número és l'escala."),
        act(3, tria("Marca el plànol on la casa surt més gran.",
                    [(f"{esc(100)} o {esc(50)}?", [esc(100), esc(50)], 1),
                     (f"{esc(200)} o {esc(500)}?", [esc(200), esc(500)], 0),
                     (f"{esc(1000)} o {esc(100)}?", [esc(1000), esc(100)], 1),
                     (f"{esc(25)} o {esc(250)}?", [esc(25), esc(250)], 0)],
                    compacta=False),
            repte=True,
            nota_sol="No hi ha cap compte: és la frase de la pàgina 1 de la fitxa, «com més gran és el "
                     "número, més petit surt el dibuix». Si dubta, que digui quant val 1 cm a cada "
                     "escala: on 1 cm val menys, el dibuix ha de ser més gran."),
    ])


# ------------------------------------------------- 2 · del plànol a la realitat --

def a_veritat(*parells):
    return [[esc(e), f"{num(c)} cm", f"{num(c * e)} cm", f"{num(c * e / 100)} m"] for e, c in parells]

CAP2 = ["Escala", "Al plànol", "× escala", "De veritat"]
Q2 = "Calcula quant fa de veritat."
A2 = [22, 20, 24, 24]

bloc2 = dict(
    titol="Del plànol a la realitat", mira=(2, 5),
    nota_sol="Sempre la mateixa cadena: <i>× l'escala</i> i després <i>÷ 100</i>. <b>Error típic:</b> "
             "oblidar el segon pas i deixar el resultat en centímetres (600 m en lloc de 6 m).",
    acts=[
        act(1, taula(Q2, CAP2, a_veritat((100, 4), (100, 7), (100, 3.5), (50, 6)), omplir=(2, 3), ico="calc", amples=A2)),
        act(2, taula(Q2, CAP2, a_veritat((200, 3), (200, 5), (50, 10), (100, 12)), omplir=(2, 3), ico="calc", amples=A2)),
        act(3, taula(Q2, CAP2, a_veritat((50, 4), (500, 3), (100, 8.5), (200, 4.5)), omplir=(2, 3), ico="calc", amples=A2)),
        act(3, taula(Q2, CAP2, a_veritat((300, 2), (300, 5), (50, 9), (1000, 4)), omplir=(2, 3), ico="calc", amples=A2)),
        act(1, taula("Mesura cada línia amb el regle i calcula quant fa de veritat.",
                     ["Línia", "Mesura", "De veritat"],
                     [[l, f"{num(c)} cm", f"{num(c)} m"] for l, c in zip("ABCD", (4, 6, 2.5, 8))],
                     omplir=(1, 2), ico="regle", amples=[26, 32, 32],
                     abans='    <p class="nota-act">Plànol a escala 1 : 100.</p>\n' + linies([4, 6, 2.5, 8]),
                     sol_nota="Les línies són de mida real si s'imprimeix al 100 %, sense «ajustar a la "
                              "pàgina». Si la impressora escala el full, accepteu la mesura que surti i "
                              "mireu només la conversió."),
            repte=True,
            nota_sol="La dada no la dona el paper: l'ha de mesurar. És el graó físic de la unitat (la cinta "
                     "mètrica) portat al quadern."),
        act(3, taula("Calcula quant fa de veritat en aquest mapa.",
                     ["Al mapa", "× 25 000", "De veritat"],
                     [[f"{num(c)} cm", f"{num(c * 25000)} cm", f"{num(c * 250)} m"] for c in (2, 4, 6, 3)],
                     omplir=(1, 2), ico="calc", amples=[26, 32, 32],
                     abans='    <p class="nota-act">Mapa a escala 1 : 25 000.</p>\n'),
            repte=True,
            nota_sol="La mateixa cadena amb números molt grans: és l'apartat e de l'exercici 1 de la fitxa. "
                     "La calculadora fa el compte; el que costa és no perdre's amb els zeros."),
    ])


# ------------------------------------------------- 3 · de la realitat al plànol --

def al_planol(*parells):
    return [[esc(e), f"{num(m)} m", f"{num(m * 100)} cm", f"{num(m * 100 / e)} cm"] for e, m in parells]

CAP3 = ["Escala", "De veritat", "× 100", "Al plànol"]
Q3 = "Calcula quant ha de fer al plànol."

bloc3 = dict(
    titol="De la realitat al plànol", mira=(3, 6),
    nota_sol="Ara la cadena va al revés: <i>× 100</i> per passar a centímetres i <i>÷ l'escala</i>. "
             "<b>Atenció a les escales 1 : 50:</b> el dibuix surt més gran que a 1 : 100 (3 m fan 6 cm, "
             "no 3 cm), com l'apartat c de la fitxa.",
    acts=[
        act(1, taula(Q3, CAP3, al_planol((100, 4), (100, 7), (100, 2.5), (200, 6)), omplir=(2, 3), ico="calc", amples=A2)),
        act(2, taula(Q3, CAP3, al_planol((200, 10), (200, 8), (50, 2), (500, 30)), omplir=(2, 3), ico="calc", amples=A2)),
        act(3, taula(Q3, CAP3, al_planol((50, 3), (50, 1.5), (500, 20), (100, 9.5)), omplir=(2, 3), ico="calc", amples=A2)),
        act(3, taula(Q3, CAP3, al_planol((200, 12), (1000, 50), (50, 4.5), (200, 5)), omplir=(2, 3), ico="calc", amples=A2)),
        act(1, (
            '    <div class="tasca"><div class="n"></div>ESTRELLA\n'
            '      <div class="q">Dibuixa cada paret a escala 1 : 100.\n'
            '        <svg class="ico" style="margin-left:.4rem"><use href="#i-llapis"/></svg></div></div>\n'
            '    <p class="nota-act">Cada quadret fa 1 cm.</p>\n'
            + quadricula([("5 m", 5), ("3 m", None), ("8 m", None), ("6,5 m", None)]),
            "<p>a) <b>5 cm</b> (5 quadrets) &nbsp;·&nbsp; b) <b>3 cm</b> &nbsp;·&nbsp; c) <b>8 cm</b>"
            " &nbsp;·&nbsp; d) <b>6,5 cm</b> (sis quadrets i mig)</p>"),
            repte=True,
            nota_sol="El resultat no s'escriu: es dibuixa. A 1 : 100, 1 m de veritat és 1 cm, o sigui un "
                     "quadret. Si s'imprimeix escalat, els quadrets continuen sent la unitat: compteu "
                     "quadrets, no centímetres."),
        act(3, taula("Calcula quant fa al plànol i escriu si hi cap.",
                     ["Escala", "De veritat", "Al plànol", "Hi cap?"],
                     [[esc(e), f"{num(m)} m", f"{num(m * 100 / e)} cm", "Sí" if m * 100 / e <= 20 else "No"]
                      for e, m in ((100, 15), (100, 30), (200, 30), (500, 120))],
                     omplir=(2, 3), ico="calc", amples=[22, 22, 22, 22],
                     abans='    <p class="nota-act">El full fa 20 cm de llarg.</p>\n'),
            repte=True,
            nota_sol="Després del compte hi ha una decisió. Els apartats b i c tenen la mateixa paret de "
                     "30 m: a 1 : 100 no hi cap i a 1 : 200 sí. És per això que els plànols grans es fan "
                     "amb escales de número gran."),
    ])


# ------------------------------------------------- 4 · directa o inversa --

DI = ["Directa", "Inversa"]
Q4 = "Marca si és proporcionalitat directa o inversa."

bloc4 = dict(
    titol="Directa o inversa?", mira=(4, 6),
    nota_sol="Com a la fitxa: si dubta, que digui en veu alta les dues meitats, «més… i més…» o "
             "«més… i menys…». La paraula «menys» ja li dona la resposta.",
    acts=[
        act(1, tria(Q4, [("Més litres de gasolina, més diners.", DI, 0),
                         ("Més velocitat, menys temps per arribar.", DI, 1),
                         ("Més entrades de cinema, més diners.", DI, 0)])),
        act(2, tria(Q4, [("Més aixetes obertes, menys temps per omplir la banyera.", DI, 1),
                         ("Més pàgines, més temps per llegir el llibre.", DI, 0),
                         ("Més amics per pagar un regal, menys diners cadascú.", DI, 1)])),
        act(3, tria(Q4, [("Més quilos de taronges, més diners.", DI, 0),
                         ("Més paletes, menys dies per fer el mur.", DI, 1),
                         ("Més quilòmetres en cotxe, més gasolina.", DI, 0)])),
        act(3, tria(Q4, [("Més persones a la festa, més pizzes.", DI, 0),
                         ("Més autobusos, menys persones a cada autobús.", DI, 1),
                         ("Més minuts de trucada, més diners.", DI, 0)])),
        act(2, tria("Mira la taula i marca si és directa o inversa.",
                    [("Les pomes.<br>" + taula_fila(["Quilos", "Preu"], [["1", "2", "3"], ["3 €", "6 €", "9 €"]]), DI, 0),
                     ("Un pastís.<br>" + taula_fila(["Amics", "Trossos"], [["2", "4", "8"], ["8", "4", "2"]]), DI, 1),
                     ("La bicicleta.<br>" + taula_fila(["Hores", "Quilòmetres"], [["1", "2", "4"], ["5", "10", "20"]]), DI, 0)]),
            repte=True,
            nota_sol="No hi ha frase: la relació s'ha de llegir als números. És el pas de la pàgina 4 de la "
                     "fitxa, on les fletxes ↑ ↓ de sota de cada taula ho deien. Si costa, que hi dibuixi les "
                     "fletxes."),
        act(3, (
            '    <div class="tasca"><div class="n"></div>ESTRELLA\n'
            '      <div class="q">Completa cada taula.\n'
            '        <svg class="ico" style="margin-left:.4rem"><use href="#i-calc"/></svg></div></div>\n'
            '    <div style="margin-top:.6rem"><span class="apartat">a)</span> Les pomes. Directa.</div>\n'
            + taula_fila(["Quilos", "Preu"], [["1", "2", "3", "4"], ["2 €", "4 €", "6 €", "8 €"]], resolts=(2, 3)) +
            '    <div style="margin-top:1rem"><span class="apartat">b)</span> Les entrades. Directa.</div>\n'
            + taula_fila(["Entrades", "Preu"], [["1", "2", "3", "5"], ["8 €", "16 €", "", ""]], buits=(2, 3)) +
            '    <div style="margin-top:1rem"><span class="apartat">c)</span> Els pintors. Inversa.</div>\n'
            + taula_fila(["Pintors", "Dies"], [["1", "2", "3", "6"], ["12", "6", "", ""]], buits=(2, 3)) +
            '    <div class="avis puntejat" style="margin-top:.8rem">A la inversa es divideix: 12 dies ÷ els pintors.</div>\n',
            "<p>a) 6 € i 8 € (resolt) &nbsp;·&nbsp; b) <b>24 €</b> i <b>40 €</b> &nbsp;·&nbsp; "
            "c) <b>4 dies</b> i <b>2 dies</b></p>"),
            repte=True,
            nota_sol="Ara no només es reconeix la relació: s'ha de fer servir. A la inversa el truc és el "
                     "producte fix: 1 pintor tarda 12 dies, i la feina es reparteix entre els pintors."),
    ])


# ------------------------------------------------- 5 · el plànol --

def mides(espais, factor):
    """[nom, «w × h cm», «W × H m»] per a cada espai d'un plànol, amb el factor de l'escala."""
    return [[e[0], f"{num(e[3])} × {num(e[4])} cm", f"{num(e[3] * factor)} × {num(e[4] * factor)} m"]
            for e in espais]

Q5 = "Calcula les mides de veritat de cada espai."
CAP5 = ["Espai", "Al plànol", "De veritat"]

PIS = [("Sala", 0, 0, 6, 4), ("Habitació", 6, 0, 3, 3), ("Bany", 6, 3, 3, 1.5), ("Cuina", 0, 4, 4, 2)]
BOTIGA = [("Botiga", 0, 0, 7, 5), ("Magatzem", 7, 0, 3, 3), ("Lavabo", 7, 3, 3, 2)]
APARTAMENT = [("Menjador", 0, 0, 3, 2), ("Habitació", 3, 0, 2, 2), ("Cuina", 0, 2, 2, 1.5), ("Bany", 2, 2, 1.5, 1.5)]
HABITACIO = [("Habitació", 0, 0, 8, 6), ("Llit", 0.4, 0.4, 4, 2, "moble"),
             ("Armari", 4.8, 0.4, 3, 1, "moble"), ("Taula", 5.2, 4.4, 2.4, 1.2, "moble")]
CASA = [("Sala", 0, 0, 5, 4), ("Habitació", 5, 0, 4, 3), ("Bany", 5, 3, 2, 2), ("Cuina", 0, 4, 3, 2)]

bloc5 = dict(
    titol="El plànol", mira=(5, 7),
    nota_sol="A 1 : 100, els centímetres del plànol són els metres de veritat: el número no canvia. A les "
             "escales 1 : 200 i 1 : 50 sí que canvia, i és on es veu si ha entès la cadena. "
             "Els plànols a 1 : 100 són de mida real si s'imprimeix al 100 %; el de 1 : 200 està dibuixat "
             "el doble de gran perquè hi càpiguen els noms.",
    acts=[
        act(1, taula(Q5, CAP5, mides(PIS, 1), omplir=(2,), ico="regle", amples=[30, 30, 30],
                     abans='    <p class="nota-act">Plànol d\'un pis a escala 1 : 100.</p>\n'
                           + planol(PIS, aria="Plànol d'un pis amb quatre espais"),
                     despres='    <div class="avis puntejat"><span class="apartat">e)</span> '
                             'Quin espai és el més gran? Encercla\'l al plànol.</div>\n',
                     sol_nota="e) La <b>sala</b>. Es pot decidir mirant el plànol, sense calcular.")),
        act(2, taula(Q5, CAP5, mides(BOTIGA, 1), omplir=(2,), ico="regle", amples=[30, 30, 30],
                     abans='    <p class="nota-act">Plànol d\'una botiga a escala 1 : 100.</p>\n'
                           + planol(BOTIGA, aria="Plànol d'una botiga amb tres espais"))),
        act(3, taula(Q5, CAP5, mides(APARTAMENT, 2), omplir=(2,), ico="calc", amples=[30, 30, 30],
                     abans='    <p class="nota-act">Plànol d\'un apartament a escala 1 : 200.</p>\n'
                           + planol(APARTAMENT, zoom=2, aria="Plànol d'un apartament amb quatre espais"),
                     sol_nota="A 1 : 200, cada centímetre són 2 m: es multiplica per 2. <b>Error típic:</b> "
                              "copiar els números del plànol com si fos 1 : 100.")),
        act(3, taula("Calcula les mides de veritat de cada cosa.", ["Què és", "Al plànol", "De veritat"],
                     mides([HABITACIO[1], HABITACIO[2], HABITACIO[3], HABITACIO[0]], 0.5),
                     omplir=(2,), ico="calc", amples=[30, 30, 30],
                     abans='    <p class="nota-act">Plànol d\'una habitació a escala 1 : 50.</p>\n'
                           + planol(HABITACIO, mides=False, aria="Plànol d'una habitació amb un llit, un armari i una taula"),
                     sol_nota="A 1 : 50, cada centímetre són 0,5 m: el que és de veritat fa la meitat del "
                              "número del plànol.")),
        act(2, taula("Calcula la superfície de veritat de cada espai.",
                     ["Espai", "Al plànol", "De veritat", "Superfície"],
                     [[e[0], f"{num(e[3])} × {num(e[4])} cm", f"{num(e[3])} × {num(e[4])} m",
                       f"{num(e[3] * e[4])} m²"] for e in CASA],
                     omplir=(2, 3), ico="calc", amples=[22, 22, 22, 22],
                     abans='    <p class="nota-act">Plànol d\'una casa a escala 1 : 100.</p>\n'
                           + planol(CASA, aria="Plànol d'una casa amb quatre espais"),
                     sol_nota="Tota la casa: 20 + 12 + 4 + 6 = <b>42 m²</b>, per si voleu allargar-ho."),
            repte=True,
            nota_sol="Un pas més que la fitxa: després de les mides, la superfície (llarg × ample). És la "
                     "columna que el solucionari de la fitxa deixava com a ampliació."),
        act(3, taula("Calcula quant fa la paret de veritat i escriu si hi cap el moble.",
                     ["Paret al plànol", "De veritat", "El moble", "Hi cap?"],
                     [[f"{num(c)} cm", f"{num(c / 2)} m", f"{nom} de {num(m)} m", "Sí" if m <= c / 2 else "No"]
                      for c, nom, m in ((5, "Sofà", 2), (3, "Llit", 2), (4, "Armari", 1.8), (6, "Taula", 3.2))],
                     omplir=(1, 3), ico="calc", amples=[22, 22, 22, 22], esq=(2,),
                     abans='    <p class="nota-act">Plànol a escala 1 : 50.</p>\n'),
            repte=True,
            nota_sol="La conversió serveix per decidir. A 1 : 50 cada centímetre són 0,5 m. Els apartats b i "
                     "d no hi caben: és el «no» que delata qui ha respost sense calcular."),
    ])


# ------------------------------------------------- 6 · quina oferta surt més a compte --

def op(nom, diu, preu, quantitat, unitat):
    """Una oferta: el preu d'1 es calcula (i ha de ser exacte, amb dos decimals)."""
    u = round(preu / quantitat, 2)
    assert abs(u * quantitat - preu) < 1e-9, (nom, preu, quantitat)
    return dict(nom=nom, diu=diu, compte=f"{eur(preu)[:-2]} ÷ {num(quantitat)}", val=f"{eur(u)} {unitat}", u=u)

def ap(producte, *ops):
    us = [o["u"] for o in ops]
    assert len(set(us)) == len(us), producte          # cap empat
    return (producte, list(ops), us.index(min(us)))

Q6 = "Marca quina oferta surt més a compte."
L, KG, U = "el litre", "el quilo", "cada un"

bloc6 = dict(
    titol="Quina oferta surt més a compte", mira=(6, 8),
    nota_sol="<b>La regla trencada de la unitat:</b> el format gran no sempre guanya. A cada activitat hi ha "
             "algun apartat on guanya el petit (al solucionari, és on guanya l'ampolla, el brik o l'1). "
             "Si tria el gran sense dividir, és aquí on cal aturar-se: el preu d'1 és el que decideix.",
    acts=[
        act(1, ofertes(Q6, [
            ap("Suc.", op("El brik", "Brik d'1 L per 1,20 €", 1.20, 1, L), op("El pack", "Pack de 3 L per 3,30 €", 3.30, 3, L)),
            ap("Iogurts.", op("L'1", "1 iogurt per 0,50 €", 0.50, 1, U), op("El pack", "Pack de 4 per 1,80 €", 1.80, 4, U)),
            ap("Oli.", op("L'ampolla", "Ampolla d'1 L per 4 €", 4, 1, L), op("La garrafa", "Garrafa de 5 L per 21 €", 21, 5, L)),
        ])),
        act(2, ofertes(Q6, [
            ap("Patates.", op("La bossa", "Bossa d'1 kg per 1,50 €", 1.50, 1, KG), op("El sac", "Sac de 3 kg per 3,90 €", 3.90, 3, KG)),
            ap("Llapis.", op("L'1", "1 llapis per 0,60 €", 0.60, 1, U), op("La capsa", "Capsa de 10 per 5 €", 5, 10, U)),
            ap("Sabó.", op("L'ampolla", "Ampolla de 2 L per 6 €", 6, 2, L), op("La garrafa", "Garrafa de 5 L per 16 €", 16, 5, L)),
        ])),
        act(3, ofertes(Q6, [
            ap("Tomàquets.", op("1 kg", "1 kg per 2,40 €", 2.40, 1, KG), op("2 kg", "2 kg per 4,60 €", 4.60, 2, KG)),
            ap("Aigua amb gas.", op("L'ampolla", "Ampolla d'1 L per 0,80 €", 0.80, 1, L), op("El pack", "Pack de 6 L per 5,40 €", 5.40, 6, L)),
            ap("Pomes.", op("1 kg", "1 kg per 1,90 €", 1.90, 1, KG), op("La caixa", "Caixa de 5 kg per 8 €", 8, 5, KG)),
        ])),
        act(3, ofertes(Q6, [
            ap("Farina.", op("1 kg", "1 kg per 1 €", 1, 1, KG), op("5 kg", "5 kg per 4,50 €", 4.50, 5, KG)),
            ap("Llet de civada.", op("1 L", "1 L per 1,60 €", 1.60, 1, L), op("El pack", "Pack de 6 L per 10,20 €", 10.20, 6, L)),
            ap("Retoladors.", op("L'1", "1 retolador per 1,20 €", 1.20, 1, U), op("La capsa", "Capsa de 12 per 12 €", 12, 12, U)),
        ])),
        act(1, ofertes("Marca quina de les tres ofertes surt més a compte.", [
            ap("Aigua.", op("1 L", "1 L per 0,50 €", 0.50, 1, L), op("2 L", "2 L per 0,80 €", 0.80, 2, L),
               op("5 L", "5 L per 2,75 €", 2.75, 5, L)),
            ap("Llet.", op("1 L", "1 L per 1 €", 1, 1, L), op("4 L", "4 L per 3,60 €", 3.60, 4, L),
               op("6 L", "6 L per 5,70 €", 5.70, 6, L)),
            ap("Sabó de rentar.", op("1 L", "1 L per 2 €", 2, 1, L), op("3 L", "3 L per 5,10 €", 5.10, 3, L),
               op("5 L", "5 L per 9 €", 9, 5, L)),
        ]),
            repte=True,
            nota_sol="Tres opcions en lloc de dues, i a tots tres apartats guanya la del mig: ni la més "
                     "petita ni la més gran. Qui aplica una regla («el gran» o «el petit») s'equivoca sempre."),
        act(3, ofertes("Calcula el preu d'1 i marca quina botiga surt més a compte.", [
            ("Iogurts.", [
                dict(nom="El 3 × 2", diu="3 × 2: te n'emportes 3 i en pagues 2. Cada un val 0,60 €.",
                     compte="0,60 × 2 = 1,20 € · 1,20 ÷ 3", val="0,40 € cada un",
                     buit=f"Pagues {BUIT} · 1 val {BUIT}"),
                dict(nom="L'altra botiga", diu="Una altra botiga: 0,45 € cada un.", compte="", val="0,45 € cada un", buit=""),
            ], 0),
            ("Croissants.", [
                dict(nom="El 3 × 2", diu="3 × 2: te n'emportes 3 i en pagues 2. Cada un val 0,90 €.",
                     compte="0,90 × 2 = 1,80 € · 1,80 ÷ 3", val="0,60 € cada un",
                     buit=f"Pagues {BUIT} · 1 val {BUIT}"),
                dict(nom="La caixa", diu="Una altra botiga: caixa de 6 per 3,30 €.", compte="3,30 ÷ 6", val="0,55 € cada un"),
            ], 1),
            ("Sucs.", [
                dict(nom="La segona a meitat", diu="El segon, a meitat de preu. Cada un val 2 €.",
                     compte="2 + 1 = 3 € · 3 ÷ 2", val="1,50 € cada un",
                     buit=f"Pagues {BUIT} · 1 val {BUIT}"),
                dict(nom="L'altra botiga", diu="Una altra botiga: 1,40 € cada un.", compte="", val="1,40 € cada un", buit=""),
            ], 1),
        ]),
            repte=True,
            nota_sol="Les ofertes del súper: abans de dividir, cal saber quant es paga de veritat. Al 3 × 2 "
                     "es paguen 2 i te n'emportes 3. Als apartats b i c, l'oferta que sembla bona no guanya."),
    ])


# ------------------------------------------------- 7 · el mapa --

def mapa(per_cm, *recorreguts):
    return [[r, f"{num(c)} cm", f"{num(c * per_cm)} m"] for r, c in recorreguts]

Q7 = "Calcula les distàncies de veritat al mapa."
CAP7 = ["Recorregut", "Al mapa", "De veritat"]
A7 = [52, 18, 18]

bloc7 = dict(
    titol="A la vida de cada dia · el mapa", mira=(7, 9),
    nota_sol="La doble recta només arriba fins a uns quants centímetres: els apartats que en surten s'han "
             "de continuar fora del dibuix, multiplicant. Si la vol allargar amb el regle, deixeu-l'hi fer.",
    acts=[
        act(1, taula(Q7, CAP7, mapa(100, ("De casa a l'escola", 4), ("De casa a la piscina", 7),
                                    ("De casa a la biblioteca", 2.5)),
                     omplir=(2,), ico="regle", amples=A7, esq=(0,),
                     abans='    <p class="nota-act">Al mapa del barri, 1 cm són 100 m de veritat.</p>\n'
                           + doble_recta(5, 100))),
        act(2, taula(Q7, CAP7, mapa(20, ("Fins a la font", 3), ("Fins als gronxadors", 5), ("Fins al bar", 8)),
                     omplir=(2,), ico="regle", amples=A7, esq=(0,),
                     abans='    <p class="nota-act">Al mapa del parc, 1 cm són 20 m de veritat.</p>\n'
                           + doble_recta(6, 20))),
        act(3, taula(Q7, CAP7, mapa(50, ("De casa al mercat", 4), ("De casa a la farmàcia", 2),
                                    ("De casa a l'estació", 10), ("De casa al camp de futbol", 5.5)),
                     omplir=(2,), ico="regle", amples=A7, esq=(0,),
                     abans='    <p class="nota-act">Al mapa del barri, 1 cm són 50 m de veritat.</p>\n'
                           + doble_recta(6, 50))),
        act(3, taula(Q7, CAP7, mapa(200, ("Del poble al riu", 3), ("Del poble a l'ermita", 5),
                                    ("Del poble al càmping", 1.5)),
                     omplir=(2,), ico="regle", amples=A7, esq=(0,),
                     abans='    <p class="nota-act">Al mapa de la comarca, 1 cm són 200 m de veritat.</p>\n'
                           + doble_recta(5, 200))),
        act(2, taula("Calcula quants centímetres fa cada distància al mapa.",
                     ["De veritat", "÷ 50", "Al mapa"],
                     [[f"{num(m)} m", f"{num(m)} ÷ 50", f"{num(m / 50)} cm"] for m in (150, 250, 400, 75)],
                     omplir=(1, 2), ico="calc", amples=[30, 30, 30],
                     abans='    <p class="nota-act">Al mapa, 1 cm són 50 m de veritat.</p>\n' + doble_recta(6, 50)),
            repte=True,
            nota_sol="El camí al revés: dels metres al mapa es divideix. A la doble recta, és llegir de baix a "
                     "dalt. L'apartat d (75 m → 1,5 cm) cau entre dues marques."),
        act(3, taula("Troba quant val 1 cm i després calcula.",
                     ["Al mapa", "De veritat"],
                     [["1 cm", "100 ÷ 2 = 50 m"]] + [[f"{num(c)} cm", f"{num(c * 50)} m"] for c in (6, 3, 9)],
                     omplir=(1,), ico="calc", amples=[44, 44],
                     abans='    <p class="nota-act">Al mapa, 2 cm són 100 m de veritat.</p>\n'),
            repte=True,
            nota_sol="L'escala no diu quant val 1 cm: primer cal baixar a 1 cm (100 ÷ 2 = 50 m), que és el "
                     "pas de la recepta de l'exercici 8 de la fitxa. Després, com sempre: × 50."),
    ])


# ------------------------------------------------- 8 · baixar a un --

CAP8 = ["Pregunta", "Resposta"]
A8 = [62, 26]

bloc8 = dict(
    titol="A la vida de cada dia · baixar a un", mira=(8, 9),
    nota_sol="Sempre el mateix pas: baixar a una persona (o a una entrada) dividint, i després multiplicar. "
             "<b>L'apartat c de cada activitat va al revés</b> (de la quantitat a les persones), com el "
             "350 g de la fitxa: és el que mostra si ho ha entès.",
    acts=[
        act(1, taula("Baixa a una persona i després calcula.", CAP8, [
            ["Quants ous calen per a 1 persona?", "8 ÷ 4 = 2 ous"],
            ["I per a 6 persones?", "2 × 6 = 12 ous"],
            ["Amb 10 ous, per a quantes persones n'hi ha prou?", "10 ÷ 2 = 5 persones"],
            ["Més persones, més ous. És directa o inversa?", "Directa"]],
            omplir=(1,), ico="calc", amples=A8, esq=(0,),
            abans='    <p class="nota-act">Una truita per a 4 persones porta 8 ous.</p>\n')),
        act(2, taula("Baixa a una persona i després calcula.", CAP8, [
            ["Quants macarrons calen per a 1 persona?", "400 ÷ 4 = 100 g"],
            ["I per a 3 persones?", "100 × 3 = 300 g"],
            ["Amb 700 g, per a quantes persones n'hi ha prou?", "700 ÷ 100 = 7 persones"]],
            omplir=(1,), ico="calc", amples=A8, esq=(0,),
            abans='    <p class="nota-act">Uns macarrons per a 4 persones porten 400 g de pasta.</p>\n')),
        act(3, taula("Baixa a una persona i després calcula.", CAP8, [
            ["Quanta llet cal per a 1 persona?", "300 ÷ 2 = 150 mL"],
            ["I per a 5 persones?", "150 × 5 = 750 mL"],
            ["Amb 900 mL, per a quantes persones n'hi ha prou?", "900 ÷ 150 = 6 persones"]],
            omplir=(1,), ico="calc", amples=A8, esq=(0,),
            abans='    <p class="nota-act">Un batut per a 2 persones porta 300 mL de llet.</p>\n')),
        act(3, taula("Baixa a una entrada i després calcula.", CAP8, [
            ["Quant val 1 entrada?", "35 ÷ 5 = 7 €"],
            ["I 8 entrades?", "7 × 8 = 56 €"],
            ["Amb 49 €, quantes entrades pots comprar?", "49 ÷ 7 = 7 entrades"],
            ["Més entrades, més diners. És directa o inversa?", "Directa"]],
            omplir=(1,), ico="calc", amples=A8, esq=(0,),
            abans='    <p class="nota-act">5 entrades de cinema costen 35 €.</p>\n')),
        act(1, taula("Baixa a un pintor i després calcula.", CAP8, [
            ["Quants dies tardaria 1 pintor sol?", "6 × 2 = 12 dies"],
            ["I 3 pintors?", "12 ÷ 3 = 4 dies"],
            ["I 4 pintors?", "12 ÷ 4 = 3 dies"],
            ["Més pintors, menys dies. És directa o inversa?", "Inversa"]],
            omplir=(1,), ico="calc", amples=A8, esq=(0,),
            abans='    <p class="nota-act">2 pintors pinten una casa en 6 dies.</p>\n'),
            repte=True,
            nota_sol="La mateixa idea de baixar a un, en una inversa: 1 pintor sol tarda <b>més</b>, i per "
                     "això aquí es multiplica (6 × 2) i després es divideix. <b>Error típic:</b> 6 ÷ 2 = 3 "
                     "dies per a 1 pintor. Si passa, que digui en veu alta si un pintor sol ha de tardar més "
                     "o menys."),
        act(3, taula("Baixa a una persona i calcula la recepta per a 6.",
                     ["Ingredient", "Per a 4", "Per a 1", "Per a 6"],
                     [[nom, f"{num(q)} {u}", f"{num(q / 4)} {u}", f"{num(q / 4 * 6)} {u}"]
                      for nom, q, u in (("Farina", 200, "g"), ("Llet", 400, "mL"), ("Sucre", 80, "g"), ("Mantega", 40, "g"))],
                     omplir=(2, 3), ico="calc", amples=[22, 22, 22, 22],
                     abans='    <p class="nota-act">La recepta de les creps és per a 4 persones.</p>\n'),
            repte=True,
            nota_sol="Quatre ingredients amb el mateix camí: ÷ 4 i després × 6. És la recepta de la fitxa "
                     "completa, i fa veure que el pas de baixar a un serveix per a tot."),
    ])


BLOCS = [bloc1, bloc2, bloc3, bloc4, bloc5, bloc6, bloc7, bloc8]
