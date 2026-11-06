/* ============================================================================
   dades/unitats.js · la font única de veritat del curs
   ----------------------------------------------------------------------------
   La pàgina de cada unitat (uN/index.html), la del curs, la portada, la capçalera de les
   fitxes i les eines de l'alumnat (eines.html?u=N) es construeixen a partir d'aquí. Si
   canvia una data o el material d'una unitat, es canvia AQUÍ i enlloc més.
   Els camps comuns a tots els cursos són a comu/docs/SITE-MAP.md («Data model»).

   Per afegir una unitat: una entrada nova, la carpeta uN/ amb el seu index.html i la fitxa.

   Camps:
     num        número de la unitat a la programació (no el del llibre, que
                divergeix a partir del febrer: vegeu docs/MAPA-ADAPTACIO.md)
     titol      com es diu a la programació. És el títol de la unitat a tot arreu
     fitxes     les fitxes de la unitat, en l'ordre de classe: fitxa (el camí, uN/fitxa.html)
                i titol (el nom propi de la fitxa, el del seu <h1>)
     repas      la fitxa de repàs («Una de cada» i «Què he après?»): fitxa (uN/repas.html) i
                titol. Per al final de la unitat o per abans de l'examen. No és el camp
                «repas_main», que parla dels blocs de repas-main
     quadern    el quadern d'activitats per practicar després de la fitxa (uN/quadern.html),
                amb el filtre de quantitat i de tipologia. Opcional: si no hi és, la pàgina
                de la unitat diu «Quadern d'activitats no disponible». El fa
                generadors/gen_quadern.py
     dates      finestra a la programació 2026-27
     sessions   sessions previstes per al grup
     objectiu   què s'espera d'AQUEST alumnat, no del grup
     material   el graó físic dels cinc minuts previs a l'aula de suport
     trencada   l'exercici que trenca la regla que s'haurà fabricat
     (la fita, el nivell d'assoliment realista, ja no és aquí des del 6/11/2026: el repositori i
      el web són públics. És al fitxer privat del docent.)
     moduls     identificadors dels mòduls de la caixa d'eines relacionats
     tasques    les pestanyes de les eines de la unitat (el data-tasca de cada una), en
                l'ordre en què surten: eines.html?u=N només ensenya aquestes, i amb una sola
                no hi ha pestanyes. Des del 6/11/2026 (menys llocs on clicar), la Calculadora (0)
                només hi és a les unitats on la fitxa la fa servir, i Com ho dic (7), enlloc
     llibre     unitat corresponent del llibre digital
     repas_main blocs de repas-main que se li poden obrir
     evitar     el que NO se li ha d'obrir (buit si no hi ha res)
   ========================================================================== */

window.UNITATS = [
  {
    num: 1, titol: "Nombres reals des de l'estimació", fitxes: [{ fitxa: "u1/fitxa.html", titol: "Números que no s'acaben" }],
    repas: { fitxa: "u1/repas.html", titol: "Repàs · Nombres reals" },
    dates: "14–30 de setembre", sessions: 6,
    objectiu: "Situar nombres a la recta i decidir quants decimals calen a cada situació.",
    material: "una cinta mètrica i un objecte llarg per mesurar",
    trencada: "Ex. 3 · arrodonir no és tallar: 2,64 es converteix en 2,65",
    moduls: ["recta"], tasques: [1, 0], llibre: "llibre · unitat 1",
    repas_main: "full 1 · decimals, fraccions", evitar: ""
  },
  {
    num: 2, titol: "Percentatges i matemàtica financera", fitxes: [{ fitxa: "u2/fitxa.html", titol: "Què queda quan rebaixen?" }],
    repas: { fitxa: "u2/repas.html", titol: "Repàs · Percentatges" },
    dates: "6 d'octubre – 3 de novembre", sessions: 15,
    objectiu: "Comparar dues maneres de pagar amb el factor multiplicador i decidir.",
    material: "monedes i bitllets de joguina",
    trencada: "Ex. 5c · el portàtil surt més barat a terminis, no al comptat",
    moduls: ["doble", "factor", "calc"], tasques: [2, 3, 0], llibre: "llibre · unitat 2",
    repas_main: "full 6 · percentatges, factor_multiplicador", evitar: ""
  },
  {
    num: 3, titol: "Proporcionalitat i escales", fitxes: [{ fitxa: "u3/fitxa.html", titol: "El món, fet petit" }],
    repas: { fitxa: "u3/repas.html", titol: "Repàs · Escales" },
    quadern: "u3/quadern.html",
    dates: "12–27 de gener", sessions: 7,
    objectiu: "Llegir una escala, passar de plànol a realitat i distingir directa d'inversa.",
    material: "una cinta mètrica i un full quadriculat",
    trencada: "Ex. 6c · guanya l'ampolla petita, no la garrafa",
    moduls: ["doble", "escala"], tasques: [2, 4, 0], llibre: "llibre · unitat 3",
    repas_main: "full 8 · escales, escales_calcul · full 6 · directa_inversa", evitar: ""
  },
  {
    num: 4, titol: "Equacions de 2n grau", fitxes: [{ fitxa: "u4/fitxa.html", titol: "Quin número ho fa funcionar?" }],
    repas: { fitxa: "u4/repas.html", titol: "Repàs · Equacions" },
    dates: "2 de febrer – 3 de març", sessions: 12,
    objectiu: "Comprovar solucions i decidir quina té sentit. No s'aïlla la incògnita.",
    material: "una bossa opaca i fitxes iguals",
    trencada: "Ex. 5d · al congelador la solució bona és −3, no 3",
    moduls: ["equacio"], tasques: [6, 0], llibre: "llibre · unitat 5",
    repas_main: "full 5 · primer_grau", evitar: "formula_general, factoritzacio"
  },
  {
    num: 5, titol: "La paràbola", fitxes: [{ fitxa: "u5/fitxa.html", titol: "On és el punt més alt?" }],
    repas: { fitxa: "u5/repas.html", titol: "Repàs · La paràbola" },
    dates: "9–26 de març", sessions: 8,
    objectiu: "Llegir vèrtex, talls i eix, i dir què volen dir en el fenomen.",
    material: "una pilota i espai per llançar-la",
    trencada: "Ex. 2 · el vèrtex és un mínim i no hi ha cap punt de tall",
    moduls: ["parabola"], tasques: [5], llibre: "llibre · unitat 6",
    repas_main: "full 10 · funcions_quadratiques, només lectura de gràfica", evitar: ""
  },
  {
    num: 6, titol: "Estadística amb dades reals", fitxes: [{ fitxa: "u6/fitxa.html", titol: "La mitjana no ho explica tot" }],
    repas: { fitxa: "u6/repas.html", titol: "Repàs · Estadística" },
    dates: "13 d'abril – 6 de maig", sessions: 10,
    objectiu: "Fer taula i gràfic amb el full de càlcul i dir si les dades estan escampades.",
    material: "fitxes o taps per fer munts",
    trencada: "Ex. 6 · el gràfic que comença a 90 i no a 0",
    moduls: ["mitjana"], tasques: [8, 0], llibre: "llibre · unitat 8",
    repas_main: "full 11 · frequencies, grafics, centralitzacio", evitar: "dispersio"
  },
  {
    num: 7, titol: "Atzar i decisions", fitxes: [{ fitxa: "u7/fitxa.html", titol: "Em convé jugar?" }],
    repas: { fitxa: "u7/repas.html", titol: "Repàs · Atzar" },
    dates: "13 de maig – 10 de juny", sessions: 10,
    objectiu: "Comptar amb arbre, calcular amb Laplace i entendre per què la casa guanya.",
    material: "un dau i una moneda",
    trencada: "Ex. 4c · una cara i una creu val el doble que dues cares",
    moduls: ["doble", "atzar"], tasques: [2, 9, 0], llibre: "llibre · unitat 9",
    repas_main: "full 12 · espais_mostrals, laplace", evitar: "probabilitat_composta, condicionada"
  }
];

/* Les targetes de consulta: una cartolina per tenir a la taula mentre es treballa.
   Cada targeta és un fitxer de targetes/ (targetes/NOM.html) i un sol PDF amb les dues
   cares (pdf/targeta-NOM.pdf). unitats: a quines pàgines d'unitat surt. S'obre amb ?u=N, i
   la capçalera diu la unitat d'on ve; sense ?u, la primera de la llista. */
window.TARGETES = [
  { nom: "percentatges", titol: "Percentatges i escales", unitats: [2, 3],
    descripcio: "La taula del factor, dos canvis seguits, la cadena de l'escala i el preu d'1." },
  { nom: "grafiques",    titol: "Paràboles, dades i atzar", unitats: [5, 6, 7],
    descripcio: "Les parts de la paràbola, mitjana, mediana i moda, i la probabilitat en dos passos." }
];

/* Els mòduls de la caixa d'eines, per poder-los anomenar des dels índexs. */
window.MODULS = {
  recta:    "Recta i estimació",
  doble:    "Doble recta",
  factor:   "Percentatges",
  escala:   "Escales",
  parabola: "Paràboles",
  equacio:  "Equacions",
  calc:     "Calculadora",
  frases:   "Com ho dic",
  mitjana:  "Aplanar",
  atzar:    "Probabilitat"
};
