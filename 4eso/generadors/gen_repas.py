#!/usr/bin/env python3
"""Fa les fitxes de repàs de cada unitat: fitxes/udN-repas.html.

    python3 generadors/gen_repas.py          (des de 4eso/)

Una fitxa de repàs és curta i sempre igual, com a 1eso/:

    pàgina 1  el dibuix de la unitat, amb «Què hi veus?», i la idea que cal recordar
    pàgina 2  «Una de cada»: un apartat de cada tipus d'exercici de la fitxa, el a) fet
    pàgina 3  «Què he après?»: frases amb exemple per marcar Ho sé fer / L'he de
              repassar / Encara no
    pàgina 4  el solucionari, amb l'exercici de la fitxa d'on ve cada apartat

Es fa servir a l'última sessió de la unitat o abans de l'examen. El dibuix de la
pàgina 1 no es copia a mà: surt de la pàgina 1 de la fitxa de la unitat (un gràfic
amb marcador <!--grafic:NOM--> o un dibuix fet a mà), perquè sigui sempre el mateix.
Si el gràfic és d'un generador, posa_grafics.py el torna a posar al dia a totes dues.

Proposta del 30/9/2026, per validar amb el docent. Després de canviar res:
python3 eines/mesura.py, generadors/gen_pdf.py i eines/comprova.py.
"""
import os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
ARREL = os.path.dirname(AQUI)

# Els blancs per escriure i la lletra manuscrita del model.
B = "<u></u>"
def ms(t):
    return f'<span class="ms">{t}</span>'

# Cada unitat:
#   material   el graó físic (el mateix de la fitxa, dades/unitats.js)
#   dibuix     quins dibuixos de la pàgina 1 de la fitxa (per ordre, sense l'ull
#              de l'obertura) es reprodueixen
#   diu        la frase que anomena el dibuix: va després, mai abans
#   recorda    la idea de la unitat, amb la forma bona de la regla trencada
#   trencada   la lletra de l'apartat d'«Una de cada» que torna a la regla trencada
#   una        (pista, frase, resposta, exercici de la fitxa). La primera ja va feta.
#   apres      (què sé fer, exemple, exercici de la fitxa)
UNITATS = {
  1: dict(
    titol="Nombres reals", material="una cinta mètrica i un objecte llarg per mesurar",
    dibuix=[0], diu="Els nombres que ja coneixes. Els irracionals tenen decimals que no s'acaben.",
    recorda="Arrodonir no és tallar. Primer pensa per a què ho vols.",
    trencada="b",
    una=[
      ("Entre quins dos nombres sencers cau.", f"√7 = 2,6457… cau entre {ms('2')} i {ms('3')}.", "2 i 3", 1),
      ("Arrodoneix a 1 decimal.", f"3,4817… → {B}", "3,5", 3),
      ("Els decimals que s'acaben.", f"√10, √49 o π? El que s'acaba: {B}", "√49 = 7", 4),
      ("Ho compro: 2 decimals.", f"Tela, per centímetres: 2,4851… m. En demano {B} m.", "2,49 m", 5),
      ("Arrodonir cap amunt costa diners.", f"Corda a 2 € el metre. Cal 3,4 m i en compro 4 m. Pago de més: {B} €", "0,6 × 2 = 1,20 €", 6),
      ("Amunt o avall?", f"Som 17. A cada taxi hi caben 4. Calen {B} taxis.", "17 ÷ 4 = 4,25 → amunt: 5 taxis", 7),
    ],
    apres=[
      ("Dic entre quins dos sencers cau un nombre.", "√7 és entre 2 i 3", 1),
      ("Marco un nombre a la recta.", "√7 cau prop del 3", 2),
      ("Arrodoneixo amb els decimals que em demanen.", "2,6457… → 2,65", 3),
      ("Sé quins nombres tenen decimals que s'acaben.", "√9 = 3", 4),
      ("Trio quants decimals calen.", "Ho dic 1,7 · ho compro 1,70", 5),
      ("Decideixo si arrodoneixo amunt o avall.", "2,3 L de pintura → 3 pots", 7),
    ]),
  2: dict(
    titol="Percentatges", material="monedes i bitllets de joguina",
    dibuix=[0, 1, 2], diu="Una bici de 300 €, amb un 20 % de descompte. Amb la regla de 0 a 100 a sota: de cada 100 €, en queden 80.",
    recorda="Al comptat no sempre és més barat. Fes els dos comptes.",
    trencada="g",
    una=[
      ("El factor d'un descompte.", f"−20 % → × {ms('0,8')}", "× 0,8", 1),
      ("El factor d'una pujada.", f"+15 % → × {B}", "× 1,15", 1),
      ("Un sol canvi: multiplica pel factor.", f"Jaqueta de 60 € amb −25 %: 60 × {B} = {B} €", "60 × 0,75 = 45,00 €", 2),
      ("Dos canvis: dos factors.", f"100 €, −10 % i després −10 %: 100 × 0,9 × 0,9 = {B} €", "81,00 €, no 80 €", 3),
      ("Pujar i baixar el mateix no torna.", f"200 €, +10 % i després −10 %: {B} €. Torna a 200? {B}", "198,00 €. No.", 4),
      ("L'IVA és una pujada.", f"30 € sense IVA, amb el 21 %: 30 × 1,21 = {B} €", "36,30 €", 6),
      ("Fes els dos comptes.", f"Al comptat: 400 €. A terminis: 10 × 38 €. A terminis: {B} €. Guanya: {B}", "380 €. Guanya a terminis.", 5),
    ],
    apres=[
      ("Escric el factor d'un descompte.", "−20 % → × 0,8", 1),
      ("Escric el factor d'una pujada.", "+21 % → × 1,21", 1),
      ("Calculo el preu final amb el factor.", "300 × 0,8 = 240 €", 2),
      ("Faig dos canvis seguits.", "100 × 0,9 × 0,9 = 81 €", 3),
      ("Sé que pujar i baixar el mateix no torna.", "100 → 110 → 99 €", 4),
      ("Comparo dues maneres de pagar.", "al comptat o a terminis", 5),
      ("Calculo el preu amb IVA.", "40 × 1,21 = 48,40 €", 6),
    ]),
  3: dict(
    titol="Escales", material="una cinta mètrica i un full quadriculat",
    dibuix=[0], diu="A escala 1 : 100, 1 cm del plànol són 100 cm de veritat: 1 m.",
    recorda="El paquet gran no sempre surt més barat. Compara el preu d'1 litre.",
    trencada="f",
    una=[
      ("Quant val 1 cm del plànol.", f"1 : 200 → 1 cm són {ms('200 cm = 2 m')}", "2 m", 1),
      ("Del plànol a la realitat: multiplica.", f"1 : 100. Al plànol, 7 cm. De veritat: {B} m", "700 cm = 7 m", 2),
      ("De la realitat al plànol: divideix.", f"1 : 50. De veritat, 4 m. Al plànol: {B} cm", "400 ÷ 50 = 8 cm", 3),
      ("Directa o inversa?", f"Més pintors, menys dies per pintar la casa: {B}", "inversa", 4),
      ("Les mides d'un plànol 1 : 100.", f"Al plànol, 6 × 3 cm. De veritat: {B} × {B} m", "6 × 3 m (18 m²)", 5),
      ("El preu d'1 litre.", f"Oli: 1 L a 4,50 € o 3 L a 12,90 €. 1 L del gran: {B} €. Guanya: {B}", "12,90 ÷ 3 = 4,30 €. Guanya el gran.", 6),
    ],
    apres=[
      ("Dic quant val 1 cm del plànol.", "1 : 200 → 2 m", 1),
      ("Passo del plànol a la realitat.", "1 : 100, 6 cm → 6 m", 2),
      ("Passo de la realitat al plànol.", "1 : 200, 8 m → 4 cm", 3),
      ("Distingeixo directa d'inversa.", "més… i més… · més… i menys…", 4),
      ("Trobo les mides de veritat d'un plànol.", "5 × 4 cm → 5 × 4 m", 5),
      ("Comparo ofertes amb el preu d'1 litre.", "0,40 €/L i 0,45 €/L", 6),
      ("Faig servir la doble recta del mapa.", "1 cm → 50 m", 7),
    ]),
  4: dict(
    titol="Equacions", material="una bossa opaca i fitxes iguals",
    dibuix=[0], diu="Una equació és una balança: x + 2 = 6. Les dues bandes pesen igual.",
    recorda="El negatiu no sempre es ratlla. Mira què vol dir la x.",
    trencada="f",
    una=[
      ("La balança: treu el mateix de cada banda.", f"x + 3 = 9 → x = {ms('6')}", "x = 6", 1),
      ("Comprovar: posa el número i compara.", f"x + 4 = 10. Provo x = 5: 5 + 4 = {B}. Funciona? {B}", "9. No.", 2),
      ("Amb l'arrel quadrada.", f"x² = 81 → x = √81 = {B}", "9", 3),
      ("L'hort quadrat.", f"Un hort de 64 m². L'equació: {B}. El costat: {B} m", "x² = 64. 8 m", 4),
      ("Dues solucions: quina té sentit?", f"x² = 25. Solucions: {B} i {B}. L'edat d'un gat: {B} anys", "5 i −5. 5 anys", 5),
      ("El negatiu també pot valer.", f"x² = 16. Una planta sota terra: la planta {B}", "4 i −4. La planta −4.", 7),
      ("Comprova una de 2n grau.", f"x² − 5x + 6 = 0. Provo x = 3: 9 − 15 + 6 = {B}. És solució? {B}", "0. Sí.", 6),
    ],
    apres=[
      ("Trobo la x amb la balança.", "x + 2 = 6 → x = 4", 1),
      ("Comprovo si un número és la solució.", "4 + 3 = 7: sí", 2),
      ("Resolc x² = k amb l'arrel quadrada.", "x² = 36 → x = 6", 3),
      ("Escric l'equació d'un hort quadrat.", "36 m² → x² = 36", 4),
      ("Sé que x² = k té dues solucions.", "6 i −6", 5),
      ("Decideixo quina solució té sentit.", "congelador: −3 °C", 5),
      ("Comprovo una equació de 2n grau.", "x = 2: 4 − 10 + 6 = 0", 6),
    ]),
  5: dict(
    titol="La paràbola", material="una pilota i espai per llançar-la",
    dibuix=[0], diu="La pilota puja, arriba dalt de tot i baixa. La corba es diu paràbola.",
    recorda="El vèrtex no sempre és el punt més alt. De vegades no hi ha cap tall.",
    trencada="g",
    una=[
      ("Cap on s'obre: mira el signe de x².", f"y = −2x² + 8x → s'obre cap {ms('avall')}", "avall", 3),
      ("Cap on s'obre.", f"y = 3x² − 6 → s'obre cap {B}", "amunt", 3),
      ("El vèrtex: el punt de dalt de tot.", f"La pilota de la pàgina 1. Vèrtex: ( {B} , {B} )", "(1 , 5)", 1),
      ("Els talls: on toca a terra.", f"La pilota toca a terra al segon {B} i al segon {B}", "0 i 2", 1),
      ("La paràbola és simètrica.", f"Al segon 0,5 la pilota fa 3,75 m. Al segon 1,5 fa {B} m", "3,75 m", 6),
      ("Els talls són les solucions.", f"y = x² − 4 talla a −2 i a 2. Solucions de x² − 4 = 0: {B} i {B}", "x = −2 i x = 2", 7),
      ("Sense cap tall.", f"La paràbola no toca la línia de baix. Talls: {B}", "cap", 2),
    ],
    apres=[
      ("Dic cap on s'obre mirant el signe de x².", "−5x² → avall", 3),
      ("Llegeixo el vèrtex.", "la pilota: (1 , 5)", 1),
      ("Sé si el vèrtex és el més alt o el més baix.", "s'obre amunt → el més baix", 2),
      ("Llegeixo els punts de tall.", "la pilota: 0 i 2", 1),
      ("Dic què vol dir cada element.", "el vèrtex: l'altura màxima", 4),
      ("Faig servir la simetria.", "segon 1 i segon 3: 15 m", 6),
      ("Sé que els talls són les solucions.", "talla a 2 i 3 → x = 2, x = 3", 7),
    ]),
  6: dict(
    titol="Estadística", material="fitxes o taps per fer munts",
    dibuix=[0, 1], diu="Dues jugadores amb la mateixa mitjana, 5. La A és regular; la B, escampada.",
    recorda="La mitjana no ho explica tot. Mira també si les dades estan juntes o escampades.",
    trencada="g",
    una=[
      ("Taula de vegades: compta.", f"2 3 2 4 2 3 → el 2 surt {ms('3')} vegades", "3", 1),
      ("La mitjana: suma i divideix.", f"4 6 5 5 → (4 + 6 + 5 + 5) ÷ 4 = {B}", "20 ÷ 4 = 5", 2),
      ("La mediana: ordena i agafa la del mig.", f"7 2 9 4 5 → ordenades: {B}. Mediana: {B}", "2 4 5 7 9. Mediana 5", 2),
      ("La moda: la que surt més.", f"1 3 3 2 3 1 → moda: {B}", "3", 2),
      ("Una nota que pesa més.", f"Projecte 8 (pesa 0,6) i prova 4 (pesa 0,4): 8 × 0,6 + 4 × 0,4 = {B}", "4,8 + 1,6 = 6,4", 3),
      ("Juntes o escampades?", f"A: 5 5 6 5 · B: 1 9 2 8. Les més escampades: {B}", "la B", 4),
      ("El gràfic ha de començar a 0.", f"Un gràfic de barres comença al 90. Pot enganyar? {B}", "Sí", 6),
    ],
    apres=[
      ("Faig la taula de vegades.", "les vegades sumen el total", 1),
      ("Calculo la mitjana.", "16 ÷ 10 = 1,6", 2),
      ("Trobo la mediana i la moda.", "ordeno i agafo la del mig", 2),
      ("Calculo una nota amb pesos.", "9 × 0,5 + 4 × 0,3 + 6 × 0,2", 3),
      ("Dic si les dades estan juntes o escampades.", "A de 4 a 6 · B de 1 a 9", 4),
      ("Llegeixo un gràfic de barres.", "a peu: 12", 5),
      ("Veig quan un gràfic enganya.", "comença al 90, no al 0", 6),
    ]),
  7: dict(
    titol="Atzar", material="un dau i una moneda",
    dibuix=[0], diu="Tot el que pot passar cau en algun punt d'aquesta línia: d'impossible a segur.",
    recorda="Una cara i una creu surt de 2 maneres. La casa sempre guanya.",
    trencada="e",
    una=[
      ("Impossible, pot passar o segur.", f"Treure un 7 amb un dau: {ms('impossible')}", "impossible", 1),
      ("L'arbre: multiplica les branques.", f"3 primers i 2 postres: {B} × {B} = {B} menús", "3 × 2 = 6", 2),
      ("Laplace: em van bé ÷ poden sortir.", f"Treure un 1 o un 2 amb un dau: 2 ÷ 6 = {B} %", "33,3 %", 3),
      ("Quin és més probable?", f"Amb un dau: un parell o un 6? {B}", "un parell (50 % i 16,7 %)", 4),
      ("Una cara i una creu: 2 branques de 4.", f"Dues monedes. Una cara i una creu: 2 ÷ 4 = {B} %", "50 %", 4),
      ("El joc de fira: fes els comptes.", f"Tirar costa 1 €. Si surt un 6, et donen 4 €. En 60 tirades pagues {B} € i cobres {B} €", "60 € i 10 × 4 = 40 €. Hi perds 20 €.", 5),
      ("La ruleta no recorda.", f"Han sortit 5 vermells. «Ara toca negre». Enganya? {B}", "Sí, enganya.", 6),
    ],
    apres=[
      ("Dic si és impossible, si pot passar o si és segur.", "un 7 amb un dau: impossible", 1),
      ("Compto amb l'arbre.", "2 monedes: 2 × 2 = 4", 2),
      ("Calculo una probabilitat en tant per cent.", "un 5: 1 ÷ 6 = 16,7 %", 3),
      ("Dic quin fet és més probable.", "parell 50 % · un 6 16,7 %", 4),
      ("Sé per què una cara i una creu val el doble.", "2 branques de 4", 4),
      ("Calculo què passa en un joc de fira.", "pago 120 €, cobro 80 €", 5),
      ("Descobreixo un missatge que enganya.", "«ara toca negre»", 6),
    ]),
}

DIBUIX = re.compile(r"<!--grafic:\w+-->.*?<!--/grafic-->|<svg\b.*?</svg>", re.S)


def dibuixos(n, quins):
    """Els dibuixos de la pàgina 1 de la fitxa, sense l'ull de l'obertura."""
    fitxa = open(os.path.join(ARREL, "fitxes", f"ud{n}.html"), encoding="utf-8").read()
    full1 = re.findall(r'<div class="full[^"]*">.*?\n</div>', fitxa, re.S)[0]
    tots = [d for d in DIBUIX.findall(full1) if 'class="ull"' not in d[:80]]
    return [tots[i] for i in quins]


def fitxa(n, u):
    pag = lambda k: f'  <div class="pag">Unitat {n} · Repàs · pàgina {k}</div>\n</div>\n'
    ull = ('<svg class="ull" viewBox="0 0 48 48" aria-hidden="true"><path d="M3 24s8-13 21-13 21 13 21 13-8 13-21 13S3 24 3 24z" '
           'fill="#F2F2F2" stroke="#000" stroke-width="3" stroke-linejoin="round"/><circle cx="24" cy="24" r="7" fill="#000"/></svg>')
    # Com a la fitxa: els gràfics dels generadors van dins de .figura; els dibuixos fets
    # a mà, en un bloc sense límit d'amplada, perquè al paper la lletra no baixi de 12 pt.
    fig = "\n".join(f'  <div class="figura neta" style="margin-top:1rem">{d}</div>' if d.startswith("<!--")
                    else f'  <div style="margin-top:1rem">{d}</div>' for d in dibuixos(n, u["dibuix"]))

    h = f"""<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Unitat {n} · Repàs</title>
<!--
  Fitxa de repàs de la unitat {n}. NO S'EDITA A MÀ: la fa generadors/gen_repas.py.
  Una pàgina amb el dibuix de la unitat, «Una de cada», «Què he après?» i el solucionari.
  Les regles són a docs/CRITERIS-DISSENY.md. Després de canviar res:
  eines/mesura.py, generadors/gen_pdf.py i eines/comprova.py.
-->
<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/fitxa.css">
</head>
<body>

<nav class="navega no-imprimir" aria-label="Navegació"><a href="../fitxes.html">← totes les fitxes</a><a class="pdf" href="../pdf/ud{n}-repas-alumnat.pdf" download>PDF de l'alumnat</a><a class="pdf" href="../pdf/ud{n}-repas-solucionari.pdf" download>PDF del solucionari</a></nav>

<!-- ==================== FULL 1 ==================== -->
<div class="full">
  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>{u["material"]}</b></div>
  <h1>Repàs · {u["titol"]}</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ull}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

{fig}
  <p style="font-size:14pt;color:var(--gris-2);margin:.6rem 0 0">{u["diu"]}</p>

  <div class="avis gruixut" style="margin-top:1.4rem;text-align:center;font-size:17pt;font-weight:700">
    {u["recorda"]}
  </div>
{pag(1)}
<!-- ==================== FULL 2: UNA DE CADA ==================== -->
<div class="full">
  <div class="exercici">
    <div class="tasca"><div class="n">1</div><div class="q">Una de cada. Fes-les amb el que ja saps.</div></div>
"""
    for i, (pista, frase, _, _) in enumerate(u["una"]):
        lletra = "abcdefgh"[i]
        classe = ' class="resolt" style="border-radius:10px;' if i == 0 else ' style="'
        h += (f'    <div{classe}padding:.3rem .6rem;margin-bottom:.35rem">\n'
              f'      <p style="margin:0;font-size:14pt;color:var(--gris-2)"><span class="apartat">{lletra})</span>{pista}</p>\n'
              f'      <p class="frase" style="margin:0;font-size:16.5pt">{frase}</p>\n'
              f'    </div>\n')
    h += "  </div>\n" + pag(2)

    h += """
<!-- ==================== FULL 3: QUÈ HE APRÈS? ==================== -->
<div class="full">
  <h2>Què he après?</h2>
  <p style="margin:0;font-size:14pt;color:var(--gris-2)">Llegeix cada frase. Marca una casella.</p>
  <table class="mini" style="margin-top:.5rem">
    <tr><th style="width:46%">Què sé fer</th><th style="width:18%">Ho sé fer</th><th style="width:18%">L'he de repassar</th><th style="width:18%">Encara no</th></tr>
"""
    for frase, exemple, _ in u["apres"]:
        h += (f'    <tr><td class="esq" style="line-height:1.3"><b>{frase}</b><br>'
              f'<span style="color:var(--gris-2)">{exemple}</span></td><td></td><td></td><td></td></tr>\n')
    h += f"""  </table>
  <p class="frase" style="margin-top:1rem">El que m'ha costat més: <u style="padding:0 4.5cm"></u></p>
  <p class="frase">El que ara sé fer: <u style="padding:0 5.2cm"></u></p>
{pag(3)}
<!-- ==================== FULL 4: SOLUCIONARI ==================== -->
<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat {n} · Repàs · full per al professorat</p>

  <div class="abans">
    <b>Quan.</b> A l'última sessió de la unitat o la sessió abans de l'examen. Es fa amb la
    fitxa de la unitat i la targeta de consulta a la taula: no és un examen.
    <b>Una de cada</b> té un apartat de cada tipus d'exercici de la fitxa. Si en falla un,
    la columna «Fitxa» diu a quin exercici tornar. <b>Què he après?</b> no es puntua: és
    la seva lectura del que sap. Si marca «Encara no» en una frase que a l'examen és el
    mínim, aquella és la feina de la sessió següent.
  </div>

  <h3>1. Una de cada</h3>
  <table>
    <tr><th></th><th>Resposta</th><th>Fitxa</th></tr>
"""
    for i, (_, _, resposta, ex) in enumerate(u["una"]):
        h += f'    <tr><td>{"abcdefgh"[i]})</td><td>{resposta}</td><td>ex. {ex}</td></tr>\n'
    h += """  </table>

  <h3>Què he après?</h3>
  <table>
    <tr><th>Frase</th><th>Si marca «Encara no», torneu a</th></tr>
"""
    for frase, _, ex in u["apres"]:
        h += f'    <tr><td>{frase}</td><td>la fitxa, ex. {ex}</td></tr>\n'
    h += f"""  </table>
  <p><b>Per avaluar:</b> el repàs no és evidència d'avaluació. Si es vol fer servir, l'apartat
  {u["trencada"]}) és el que val més: és la regla trencada de la fitxa (exercici {u["una"]["abcdefgh".index(u["trencada"])][3]}).</p>
</div>

</body>
</html>
"""
    return h


def main():
    for n, u in UNITATS.items():
        desti = os.path.join(ARREL, "fitxes", f"ud{n}-repas.html")
        with open(desti, "w", encoding="utf-8") as f:
            f.write(fitxa(n, u))
        print(f"  fitxes/ud{n}-repas.html: {len(u['una'])} apartats, {len(u['apres'])} frases")


if __name__ == "__main__":
    main()
