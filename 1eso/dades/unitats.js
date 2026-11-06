/* ============================================================================
   dades/unitats.js · les set unitats i les targetes de consulta
   ----------------------------------------------------------------------------
   Una unitat per situació d'aprenentatge (SA) de la programació del grup, amb
   els mateixos números i títols. Ho llegeixen totes les pàgines del curs, i eines/comprova.py
   comprova que el que diu aquí quadri amb el que hi ha al disc.

   Camps d'una unitat:
     num, titol   el número i el títol de la SA del grup
     dates        quan la fa el grup (orientatiu: el calendari no mana)
     sessions     sessions de la SA del grup
     nucli        l'única idea que es treballa, dibuixada a la quadrícula.
                  El docent el va validar unitat per unitat abans d'escriure
                  la fitxa (vegeu docs/MAPA-ADAPTACIO.md)
     material     el graó físic de l'aula de suport, abans de la fitxa
     criteris     els criteris de la SA del grup, com a referència. L'avaluació
                  es fa amb els criteris propis del PI
     (La fita, el nivell d'assoliment realista, i el rol a l'aula ordinària ja no són aquí des del
      6/11/2026: el repositori i el web són públics. Són al fitxer privat del docent.)
     fitxes       les fitxes de la unitat, en l'ordre de classe. Cada una té dos
                  camps: fitxa (el camí: uN/fitxa.html la principal, uN/NOM.html les altres)
                  i titol. A més:
                    estat     «per revisar» (feta, el docent encara no l'ha mirada),
                              «revisada» o «provada a l'aula». Es canvia a mà. Les de
                              les unitats 5 a 7 es van revisar el 30/9/2026, per encàrrec
                              del docent. «Provada a l'aula» la posa el docent
                    minim     el camí mínim: les pàgines de l'alumnat que són el nucli.
                              La resta és ampliació. La unitat sencera (amb el repàs) no
                              passa de dues pàgines per sessió del grup (eines/comprova.py)
                    trencada  on és la regla trencada de la fitxa i quina és
     repas        la fitxa de repàs (uN/repas.html), amb els mateixos camps que una fitxa,
                  menys trencada
     quadern      el quadern d'activitats (uN/quadern.html), si en té. Opcional
     tasques      les eines de la unitat (el data-tasca de cada pestanya d'eines.html), en
                  l'ordre en què surten: eines.html?u=N només ensenya aquestes, i amb una sola
                  no hi ha pestanyes. Les Taules (0) només hi són on cal (unitat 1), des del
                  6/11/2026: menys llocs on clicar. eines/comprova.py mira que existeixin

   Camps d'una targeta de consulta (el mateix model a tots els cursos):
     nom          el fitxer, targetes/NOM.html, i el PDF, pdf/targeta-NOM.pdf
     titol, descripcio
     unitats      a quines unitats surt; la primera és on neix
   ========================================================================== */

window.UNITATS = [
  {
    num: 1,
    titol: "Nombres naturals",
    dates: "des del 9 de setembre",
    sessions: "13 i un examen",
    nucli: "Multiplicar és fer un rectangle de quadrets: 3 · 4 són 3 files de 4. " +
           "3² és un quadrat de 3 per 3.",
    material: "Miniblocs: fer el rectangle de 3 per 4 i comptar-ne els quadrets.",
    criteris: "1.3, 2.1, 8.1",
    fitxes: [
      { fitxa: "u1/fitxa.html", titol: "Rectangles de quadrets", estat: "revisada", minim: [1, 2, 6, 9],
        trencada: "Ex. 7 · 3² no és 3 · 2 = 6: és 3 · 3" },
      { fitxa: "u1/nombres.html", titol: "Centenes, desenes i unitats", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 4 · «tres-cents cinc» no és 35: el zero manté el lloc" },
      { fitxa: "u1/ordre.html", titol: "L'ordre de les operacions", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 4 · 2 + 3 · 4 no és 20: primer la multiplicació" }
    ],
    repas: { fitxa: "u1/repas.html", titol: "Repàs de la unitat i «Què he après?»", estat: "revisada", minim: [4, 5] },
    quadern: "u1/quadern.html",
    tasques: [1, 2, 3, 4, 0]
  },
  {
    num: 2,
    titol: "Divisibilitat",
    dates: "del 3 al 19 de novembre",
    sessions: "11",
    nucli: "Els divisors de 12 surten dels rectangles que es poden fer amb 12 quadrets. " +
           "Un nombre primer només en fa un: una fila.",
    material: "Miniblocs: fer tots els rectangles de 12, i després els de 7.",
    criteris: "1.4, 3.2, 4.2, 5.2",
    fitxes: [
      { fitxa: "u2/fitxa.html", titol: "Els múltiples", estat: "revisada", minim: [1, 2, 7],
        trencada: "Ex. 3 · el 13 i el 23 acaben en 3 i no són múltiples del 3" },
      { fitxa: "u2/repartir.html", titol: "Repartir en files", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 4 · 37 entre 7 no és «5»: en sobren 2" },
      { fitxa: "u2/divisors.html", titol: "Divisors i primers", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 3 · no tots els senars són primers (9, 15, 21)" },
      { fitxa: "u2/factors.html", titol: "La factorització", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 2 · 12 = 3 · 4 encara no està acabada" }
    ],
    repas: { fitxa: "u2/repas.html", titol: "Repàs de la unitat i «Què he après?»", estat: "revisada", minim: [4, 5] },
    quadern: "u2/quadern.html",
    tasques: [5, 6, 7, 8]
  },
  {
    num: 3,
    titol: "Com és de gran Gaza?",
    dates: "del 23 de novembre al 18 de desembre",
    sessions: "15",
    nucli: "L'àrea és comptar quadrets. Una fracció és un rectangle partit en trossos iguals: " +
           "el de baix diu quants n'hi ha, i el de dalt, quants se'n pinten.",
    material: "Quadrícula i tires de paper: comptar els quadrets d'una figura, ajuntar dues meitats i doblegar una tira en trossos iguals.",
    criteris: "1.2, 5.2, 6.1, 9.1",
    fitxes: [
      { fitxa: "u3/area.html", titol: "Mesurar l'àrea", estat: "revisada", minim: [1, 3],
        trencada: "Ex. 4 · mig quadret no és un quadret sencer" },
      { fitxa: "u3/fitxa.html", titol: "Què és una fracció", estat: "revisada", minim: [1, 2, 6],
        trencada: "Ex. 3 · 3 trossos que no són iguals no fan terços" },
      { fitxa: "u3/compara.html", titol: "Els tipus i comparar", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 3 · 1/5 no és més gran que 1/3" },
      { fitxa: "u3/equivalents.html", titol: "Fraccions equivalents", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 3 · sumar el mateix a dalt i a baix no dona una equivalent (1/2 i 2/3)" },
      { fitxa: "u3/sumes.html", titol: "Sumar i restar", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 4 · 1/2 + 1/4 no és 2/6: no se sumen els de baix" },
      { fitxa: "u3/mapes.html", titol: "Quants km²? Barcelona i Gaza", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 2 · una franja estreta no vol dir petita" }
    ],
    repas: { fitxa: "u3/repas.html", titol: "Repàs de la unitat i «Què he après?»", estat: "revisada", minim: [3, 4] },
    quadern: "u3/quadern.html",
    tasques: [9, 10, 11, 12, 13]
  },
  {
    num: 4,
    titol: "És gran l'ou del kiwi?",
    dates: "del 12 al 28 de gener",
    sessions: "11",
    nucli: "Un terç de 12 és repartir 12 quadrets en 3 grups iguals. " +
           "Multiplicar dues fraccions és fer un tros de tros del mateix rectangle. " +
           "Un percentatge és quants quadrets de cada 100. " +
           "El doble i el triple es llegeixen en dues files de quadrets, una sota l'altra.",
    material: "Miniblocs: repartir 12 en 3 grups iguals. Quadrícula de 100: pintar-ne 25. " +
              "El tros de tros: un rectangle partit en columnes i en files alhora. " +
              "Dues files de quadrets per comparar mides.",
    criteris: "1.3, 2.1, 5.1, 6.1",
    fitxes: [
      { fitxa: "u4/fitxa.html", titol: "La fracció d'un nombre", estat: "revisada", minim: [1, 2, 5],
        trencada: "Ex. 3 · grups amb quadrets diferents no són grups iguals" },
      { fitxa: "u4/multfrac.html", titol: "Multiplicar fraccions", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 3 · 1/2 de 1/3 no és «1 de 5»: es multipliquen els de baix" },
      { fitxa: "u4/percentatges.html", titol: "Els percentatges", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 4 · molts quadrets pintats no és el 100 %: cal comptar-los" },
      { fitxa: "u4/dobletriple.html", titol: "Dobles i triples", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 3 · l'ou de kiwi fa el doble, però el kiwi no és el doble de gran" }
    ],
    repas: { fitxa: "u4/repas.html", titol: "Repàs de la unitat", estat: "revisada", minim: [2, 3] },
    tasques: [14, 15, 16, 17]
  },
  {
    num: 5,
    titol: "Decimals i arrel quadrada",
    dates: "de l'1 al 15 de març",
    sessions: "7",
    nucli: "El quadrat de 100 quadrets és 1: una columna és 0,1 (una dècima) i un quadret és 0,01 " +
           "(una centèsima). 2,43 són 2 quadrats, 4 columnes i 3 quadrets. " +
           "L'arrel és el costat del quadrat.",
    material: "Quadrícula de 100: pintar una columna i un quadret. " +
              "Quadrats de cartolina: buscar el costat d'un quadrat de 9 i de 16 quadrets.",
    criteris: "5.1, 7.1, 8.1",
    fitxes: [
      { fitxa: "u5/fitxa.html", titol: "Els decimals", estat: "revisada", minim: [1, 2, 7],
        trencada: "Ex. 5 · més xifres no vol dir més gran: 0,8 és més que 0,75" },
      { fitxa: "u5/arrodonir.html", titol: "Arrodonir i truncar", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 3 · l'Oriol sempre arrodoneix avall (3,47 → 3,4)" },
      { fitxa: "u5/sumes.html", titol: "Sumar i restar decimals", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 3 · la Júlia no alinea la coma (2,5 + 1,35 = 1,60)" },
      { fitxa: "u5/fraccions.html", titol: "De la fracció al decimal", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 3 · en Pol diu que 1/4 = 0,4" },
      { fitxa: "u5/arrel.html", titol: "Quadrats i arrels", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 3 · en Joel diu que l'arrel és la meitat (√16 = 8)" }
    ],
    repas: { fitxa: "u5/repas.html", titol: "Repàs de la unitat", estat: "revisada", minim: [3, 4] },
    tasques: [2, 18, 19, 20, 21]
  },
  {
    num: 6,
    titol: "Sentit espacial",
    dates: "del 5 d'abril al 10 de maig",
    sessions: "16",
    nucli: "La cantonada d'un quadret és l'angle recte: agut és més petit, obtús és més gran. " +
           "Polígons al geoplà. El perímetre és comptar els costats de quadret de la vora; " +
           "l'àrea, els quadrets de dins.",
    material: "Geoplà: fer un rectangle i resseguir-ne la vora comptant. " +
              "Un full: la cantonada és l'angle recte.",
    criteris: "1.1, 3.1, 5.1, 6.1, 7.1, 9.1",
    fitxes: [
      { fitxa: "u6/fitxa.html", titol: "Punts, rectes i angles", estat: "revisada", minim: [1, 2, 6],
        trencada: "Ex. 5 · en Marc: costats més llargs, angle més gran" },
      { fitxa: "u6/poligons.html", titol: "Polígons", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 5 · en Nil: un quadrat girat ja no és un quadrat" },
      { fitxa: "u6/triangles.html", titol: "Triangles", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 4 · en Pau: un triangle més gran té els angles més grans" },
      { fitxa: "u6/perimetre.html", titol: "El perímetre", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 3 · la Carlota compta els quadrets de dins" },
      { fitxa: "u6/cercle.html", titol: "La circumferència", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 3 · la Nerea calcula la vora amb el radi" }
    ],
    repas: { fitxa: "u6/repas.html", titol: "Repàs de la unitat", estat: "revisada", minim: [2, 3] },
    tasques: [22, 23, 24, 25, 13]
  },
  {
    num: 7,
    titol: "Patrons i llenguatge algebraic",
    dates: "del 19 de maig a l'1 de juny",
    sessions: "6",
    nucli: "Patrons de quadrets: què hi ha de fix i què s'hi afegeix, i quants en té la figura següent. " +
           "El triple d'un nombre s'escriu 3 · n. Un gràfic de barres són columnes de quadrets.",
    material: "Miniblocs: fer les tres primeres figures d'un patró i la quarta.",
    criteris: "2.1, 3.1, 4.1, 5.1, 7.2",
    fitxes: [
      { fitxa: "u7/fitxa.html", titol: "Patrons de quadrets", estat: "revisada", minim: [1, 2, 5],
        trencada: "Ex. 3 · en Pau: 2, 4, 6, 8 «creix multiplicant per 2»" },
      { fitxa: "u7/regla.html", titol: "La regla del patró", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 3 · la Ivet oblida la part fixa (5, 8, 11, 14 no és 3 · n)" },
      { fitxa: "u7/simbols.html", titol: "De la paraula al símbol", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 4 · la Zoe: si n = 3, 2n no és 23" },
      { fitxa: "u7/grafics.html", titol: "Taules i gràfics", estat: "revisada", minim: [1, 2],
        trencada: "Ex. 3 · en Martí: l'eix no comença a zero" }
    ],
    repas: { fitxa: "u7/repas.html", titol: "Repàs i el meu curs", estat: "revisada", minim: [2, 3, 4] },
    tasques: [26, 27, 28]
  }
];

window.TARGETES = [
  {
    nom: "taules",
    titol: "Les taules de multiplicar",
    unitats: [1],
    descripcio: "Les deu taules, en files com les de primària però amb el punt: " +
                "3 · 4 = 12. Es fa servir tot el curs, a les dues aules."
  },
  {
    nom: "fraccions",
    titol: "Els noms de les fraccions",
    unitats: [3],
    descripcio: "Del mig al dotzè, amb el plural i el dibuix de cada una. A l'altra cara, " +
                "com es llegeix una fracció, els tipus, les equivalents i com se suma."
  },
  {
    nom: "decimals",
    titol: "Decimals i arrels",
    unitats: [5],
    descripcio: "El quadrat de 100 és 1: la columna és 0,1 i el quadret, 0,01. Com es llegeix un " +
                "decimal, i com es compara, s'arrodoneix i se suma. A l'altra cara, la fracció, el " +
                "decimal i el percentatge al mateix quadrat, i els quadrats i les arrels fins al 100."
  },
  {
    nom: "formes",
    titol: "Formes",
    unitats: [6],
    descripcio: "La cantonada d'un quadret és l'angle recte: agut, recte, obtús i pla. Punt, segment, " +
                "semirecta i recta. A l'altra cara, els noms dels polígons, els triangles pels costats " +
                "i pels angles, el perímetre i la circumferència."
  },
  {
    nom: "patrons",
    titol: "Patrons i símbols",
    unitats: [7],
    descripcio: "Un patró creix sempre igual: què és fix i què creix, i la regla, com 2 · n + 1. A " +
                "l'altra cara, de la paraula al símbol (el doble, el triple, la meitat…), sempre amb el " +
                "punt, i com es llegeix un gràfic de barres."
  }
];
