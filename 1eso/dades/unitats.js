/* ============================================================================
   dades/unitats.js · les set unitats i les targetes de consulta
   ----------------------------------------------------------------------------
   Una unitat per situació d'aprenentatge (SA) de la programació del grup, amb
   els mateixos números i títols. Ho llegeix index.html, i eines/comprova.py
   comprova que el que diu aquí quadri amb el que hi ha al disc.

   Camps d'una unitat:
     num, titol   el número i el títol de la SA del grup
     dates        quan la fa el grup (orientatiu: el calendari no mana)
     sessions     sessions de la SA del grup
     nucli        l'única idea que es treballa, dibuixada a la quadrícula.
                  És una PROPOSTA: es valida unitat per unitat abans d'escriure
                  la fitxa (vegeu docs/MAPA-ADAPTACIO.md)
     material     el graó físic de l'aula de suport, abans de la fitxa
     criteris     els criteris de la SA del grup, com a referència. L'avaluació
                  es fa amb els criteris propis del PI
     fitxa        "fitxes/udN.html" quan existeixi; fins llavors, null

   Camps d'una targeta de consulta:
     id, titol, descripcio, fitxer (l'HTML), pdf, unitat (on neix)
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
    fitxa: null
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
    fitxa: null
  },
  {
    num: 3,
    titol: "Com és de gran Gaza?",
    dates: "del 23 de novembre al 18 de desembre",
    sessions: "15",
    nucli: "L'àrea és comptar quadrets. Mig quadret és 1/2.",
    material: "Quadrícula: comptar els quadrets d'una figura i ajuntar dues meitats.",
    criteris: "1.2, 5.2, 6.1, 9.1",
    fitxa: null
  },
  {
    num: 4,
    titol: "És gran l'ou del kiwi?",
    dates: "del 12 al 28 de gener",
    sessions: "11",
    nucli: "Un terç de 12 és repartir 12 quadrets en 3 grups iguals. " +
           "Un percentatge és quants quadrets de cada 100.",
    material: "Miniblocs: repartir 12 en 3 grups iguals. Quadrícula de 100: pintar-ne 25.",
    criteris: "1.3, 2.1, 5.1, 6.1",
    fitxa: null
  },
  {
    num: 5,
    titol: "Decimals i arrel quadrada",
    dates: "de l'1 al 15 de març",
    sessions: "7",
    nucli: "A la quadrícula de 100, una columna és 0,1 i un quadret és 0,01. " +
           "L'arrel és el costat del quadrat.",
    material: "Quadrícula de 100: pintar una columna i un quadret. Fer un quadrat de 9 miniblocs.",
    criteris: "5.1, 7.1, 8.1",
    fitxa: null
  },
  {
    num: 6,
    titol: "Sentit espacial",
    dates: "del 5 d'abril al 10 de maig",
    sessions: "16",
    nucli: "Polígons al geoplà. El perímetre és comptar costats de quadret.",
    material: "Geoplà: fer un rectangle i resseguir-ne la vora comptant.",
    criteris: "1.1, 3.1, 5.1, 6.1, 7.1, 9.1",
    fitxa: null
  },
  {
    num: 7,
    titol: "Patrons i llenguatge algebraic",
    dates: "del 19 de maig a l'1 de juny",
    sessions: "6",
    nucli: "Patrons de quadrets: quants en té la figura següent.",
    material: "Miniblocs: fer les tres primeres figures d'un patró i la quarta.",
    criteris: "2.1, 3.1, 4.1, 5.1, 7.2",
    fitxa: null
  }
];

window.TARGETES = [
  {
    id: "taules",
    titol: "Les taules de multiplicar",
    descripcio: "Les deu taules, en files com les de primària però amb el punt: " +
                "3 · 4 = 12. Es fa servir tot el curs, a les dues aules.",
    fitxer: "targetes/taules.html",
    pdf: "pdf/targeta-taules.pdf",
    unitat: 1
  }
];
