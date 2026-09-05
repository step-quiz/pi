/* ============================================================================
   dades/unitats.js · la font única de veritat del curs
   ----------------------------------------------------------------------------
   index.html i fitxes.html es construeixen a partir d'aquí. Si canvia una data,
   una fita o el material d'una unitat, es canvia AQUÍ i enlloc més.

   Per afegir una unitat: una entrada nova + la fitxa a fitxes/. Res més.

   Camps:
     num        número de la unitat a la programació (no el del llibre, que
                divergeix a partir del febrer: vegeu docs/MAPA-ADAPTACIO.md)
     titol      com es diu a la programació
     fitxa      ruta de la fitxa imprimible
     dates      finestra a la programació 2026-27
     sessions   sessions previstes per al grup
     objectiu   què s'espera d'AQUEST alumnat, no del grup
     material   el graó físic dels cinc minuts previs a l'aula de suport
     trencada   l'exercici que trenca la regla que s'haurà fabricat
     fita       nivell d'assoliment realista
     moduls     identificadors dels mòduls de la caixa d'eines relacionats
     llibre     unitat corresponent del llibre digital
     repas      blocs de repas-main que se li poden obrir
     evitar     el que NO se li ha d'obrir (buit si no hi ha res)
   ========================================================================== */

window.UNITATS = [
  {
    num: 1, titol: "Nombres reals des de l'estimació", fitxa: "fitxes/ud1.html",
    dates: "14–30 de setembre", sessions: 6,
    objectiu: "Situar nombres a la recta i decidir quants decimals calen a cada situació.",
    material: "una cinta mètrica i un objecte llarg per mesurar",
    trencada: "Ex. 3 · arrodonir no és tallar: 2,64 es converteix en 2,65",
    fita: "AS", moduls: ["recta"], llibre: "llibre · unitat 1",
    repas: "full 1 · decimals, fraccions", evitar: ""
  },
  {
    num: 2, titol: "Percentatges i matemàtica financera", fitxa: "fitxes/ud2.html",
    dates: "6 d'octubre – 3 de novembre", sessions: 15,
    objectiu: "Comparar dues maneres de pagar amb el factor multiplicador i decidir.",
    material: "monedes i bitllets de joguina",
    trencada: "Ex. 5c · el portàtil surt més barat a terminis, no al comptat",
    fita: "AS", moduls: ["doble", "factor", "calc"], llibre: "llibre · unitat 2",
    repas: "full 6 · percentatges, factor_multiplicador", evitar: ""
  },
  {
    num: 3, titol: "Proporcionalitat i escales", fitxa: "fitxes/ud3.html",
    dates: "12–27 de gener", sessions: 7,
    objectiu: "Llegir una escala, passar de plànol a realitat i distingir directa d'inversa.",
    material: "una cinta mètrica i un full quadriculat",
    trencada: "Ex. 6c · guanya l'ampolla petita, no la garrafa",
    fita: "AS, AN a escales", moduls: ["doble", "escala"], llibre: "llibre · unitat 3",
    repas: "full 8 · escales, escales_calcul · full 6 · directa_inversa", evitar: ""
  },
  {
    num: 4, titol: "Equacions de 2n grau", fitxa: "fitxes/ud4.html",
    dates: "2 de febrer – 3 de març", sessions: 12,
    objectiu: "Comprovar solucions i decidir quina té sentit. No s'aïlla la incògnita.",
    material: "una bossa opaca i fitxes iguals",
    trencada: "Ex. 5d · al congelador la solució bona és −3, no 3",
    fita: "NA o AS", moduls: ["equacio"], llibre: "llibre · unitat 5",
    repas: "full 5 · primer_grau", evitar: "formula_general, factoritzacio"
  },
  {
    num: 5, titol: "La paràbola", fitxa: "fitxes/ud5.html",
    dates: "9–26 de març", sessions: 8,
    objectiu: "Llegir vèrtex, talls i eix, i dir què volen dir en el fenomen.",
    material: "una pilota i espai per llançar-la",
    trencada: "Ex. 2 · el vèrtex és un mínim i no hi ha cap punt de tall",
    fita: "AN, AE possible", moduls: ["parabola"], llibre: "llibre · unitat 6",
    repas: "full 10 · funcions_quadratiques, només lectura de gràfica", evitar: ""
  },
  {
    num: 6, titol: "Estadística amb dades reals", fitxa: "fitxes/ud6.html",
    dates: "13 d'abril – 6 de maig", sessions: 10,
    objectiu: "Fer taula i gràfic amb el full de càlcul i dir si les dades estan escampades.",
    material: "fitxes o taps per fer munts",
    trencada: "Ex. 6 · el gràfic que comença a 90 i no a 0",
    fita: "AS, AN a representació", moduls: [], llibre: "llibre · unitat 8",
    repas: "full 11 · frequencies, grafics, centralitzacio", evitar: "dispersio"
  },
  {
    num: 7, titol: "Atzar i decisions", fitxa: "fitxes/ud7.html",
    dates: "13 de maig – 10 de juny", sessions: 10,
    objectiu: "Comptar amb arbre, calcular amb Laplace i entendre per què la casa guanya.",
    material: "un dau i una moneda",
    trencada: "Ex. 4c · una cara i una creu val el doble que dues cares",
    fita: "AS, AN al recompte", moduls: ["doble"], llibre: "llibre · unitat 9",
    repas: "full 12 · espais_mostrals, laplace", evitar: "probabilitat_composta, condicionada"
  }
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
  frases:   "Com ho dic"
};
