#!/usr/bin/env node
/*
  1eso/generadors/examens/ud1.js · examen de la Unitat 1 (Nombres naturals)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a comu/examens/nucli.js i les
  regles, a comu/docs/EXAMENS-DOCX.md, les mateixes que a l'altre curs.

      node 1eso/generadors/examens/ud1.js   →  1eso/docx/examen-ud1-alumnat.docx
                                                1eso/docx/examen-ud1-solucionari.docx

  D'on surt cada cosa:
  · L'ordre dels exercicis, de l'examen de la unitat 1 del grup. Els seus
    exercicis 7 i 8 (propietats de les potències i potències de 10) queden
    fora, com a docs/MAPA-ADAPTACIO.md.
  · Els apartats a), b), c) i d), de les quatre fitxes de la unitat
    (fitxes/ud1.html, ud1-nombres.html, ud1-ordre.html i ud1-repas.html) i dels
    seus solucionaris, que estan validats. Els dos que no hi són (exercici 7,
    c i d) porten la marca «nou» al solucionari.
  · Sense calculadora: l'avís és el de la targeta de les taules. Totes les
    multiplicacions són de la targeta, les sumes es fan sense portar-ne i cap
    nombre passa de 999.
*/
"use strict";

const X = require("../../../comu/examens/nucli");
const { dada, ms, sol, MIDA } = X;

/* ------------------------------------------ la clau dels noms (exercici 9) --
   La mateixa de la fitxa 2: res no es demana de memòria. Una sola taula de deu
   files, perquè les quatre columnes quedin alineades, amb la vora per fora. */
const NOMS = [
  [[1, "u"], [2, "dos"], [3, "tres"], [4, "quatre"], [5, "cinc"], [6, "sis"], [7, "set"], [8, "vuit"], [9, "nou"]],
  [[10, "deu"], [11, "onze"], [12, "dotze"], [13, "tretze"], [14, "catorze"], [15, "quinze"], [16, "setze"],
   [17, "disset"], [18, "divuit"], [19, "dinou"]],
  [[20, "vint"], [30, "trenta"], [40, "quaranta"], [50, "cinquanta"], [60, "seixanta"], [70, "setanta"],
   [80, "vuitanta"], [90, "noranta"]],
  [[100, "cent"], [200, "dos-cents"], [300, "tres-cents"], [400, "quatre-cents"], [500, "cinc-cents"],
   [600, "sis-cents"], [700, "set-cents"], [800, "vuit-cents"], [900, "nou-cents"]],
];
const MIDA_CLAU = 13;
function clauNoms() {
  return () => {
    const par = X.AMPLE / 4;
    const col = [];
    for (let i = 0; i < 4; i++) col.push(Math.round(par * 0.3), Math.round(par * 0.7));
    col[col.length - 1] += X.AMPLE - col.reduce((a, b) => a + b, 0);
    const b = X.vora(2, X.G.tinta);
    const files = [];
    for (let r = 0; r < 10; r++) {
      const celes = [];
      NOMS.forEach((llista, k) => {
        const [n, nom] = llista[r] || ["", ""];
        const pad = { top: r === 0 ? X.tw(0.5 * X.REM) : 20, bottom: r === 9 ? X.tw(0.5 * X.REM) : 20, left: 0, right: 0 };
        celes.push(X.cela(X.par(X.run(String(n), { bold: true, size: X.mig(MIDA_CLAU) }),
                                { alignment: X.docx.AlignmentType.RIGHT }), { w: col[2 * k], margins: { ...pad, right: X.tw(0.4 * X.REM) } }));
        celes.push(X.cela(X.par(X.run(nom, { size: X.mig(MIDA_CLAU) })), { w: col[2 * k + 1], margins: pad }));
      });
      files.push(new X.docx.TableRow({ cantSplit: true, children: celes }));
    }
    return X.taula(col, files, { borders: { top: b, bottom: b, left: b, right: b, insideHorizontal: X.CAP, insideVertical: X.CAP } });
  };
}

/* ------------------------------------------------------------ l'alumnat -- */
const alumnat = [
  ...X.exercici(1, "Busca a la targeta el resultat de cada multiplicació.", {}, [
    X.taulaResposta([16, 42, 42], ["", "Multiplicació", "Resultat"], [
      ["a)", dada("7 · 8"), ms("56")],
      ["b)", dada("9 · 7"), ""],
      ["c)", dada("8 · 5"), ""],
      ["d)", dada("8 · 4"), ""],
    ]),
  ]),

  ...X.exercici(2, "Busca a la targeta el número que falta.", { mateixaPagina: true }, [
    X.context("Tria la taula del número que ja tens. Si el forat és al davant, gira el rectangle."),
    X.taulaResposta([16, 42, 42], ["", "Multiplicació", "El número que falta"], [
      ["a)", dada("7 · … = 56"), ms("8")],
      ["b)", dada("6 · … = 42"), ""],
      ["c)", dada("… · 4 = 20"), ""],
      ["d)", dada("… · 7 = 28"), ""],
    ]),
  ]),

  ...X.exercici(3, "Escriu el resultat sense tornar a fer la multiplicació.", {}, [
    X.context("Si gires el rectangle, els quadrets no canvien."),
    X.taulaResposta([14, 36, 25, 25], ["", "Ja saps que", "Quant és?", "Resultat"], [
      ["a)", dada("7 · 8 = 56"), dada("8 · 7"), ms("56")],
      ["b)", dada("6 · 9 = 54"), dada("9 · 6"), ""],
      ["c)", dada("6 · 8 = 48"), dada("8 · 6"), ""],
      ["d)", dada("2 · 5 = 10"), dada("5 · 2"), ""],
    ]),
  ]),

  ...X.exercici(4, "Parteix el rectangle pel 10. Després ajunta les dues parts.", { mateixaPagina: true }, [
    X.context("La targeta arriba fins al 10."),
    X.taulaResposta([9, 22, 23, 23, 23], ["", "Multiplicació", "La part de 10", "La part petita", "Ajunta-les"], [
      ["a)", dada("3 · 12"), ms("3 · 10 = 30"), ms("3 · 2 = 6"), ms("30 + 6 = 36")],
      ["b)", dada("4 · 13"), "", "", ""],
      ["c)", dada("2 · 14"), "", "", ""],
      ["d)", dada("4 · 12"), "", "", ""],
    ]),
  ]),

  ...X.exercici(5, "Escriu com es llegeix cada quadrat, la multiplicació i el resultat.", {}, [
    X.context("3² vol dir 3 · 3: un quadrat de 3 per 3."),
    X.taulaResposta([10, 18, 30, 24, 18], ["", "Quadrat", "Es llegeix", "Multiplicació", "Resultat"], [
      ["a)", dada("3²"), ms("3 al quadrat"), ms("3 · 3"), ms("9")],
      ["b)", dada("2²"), "", "", ""],
      ["c)", dada("4²"), "", "", ""],
      ["d)", dada("5²"), "", "", ""],
    ]),
  ]),

  ...X.exercici(6, "Escriu el resultat de cada arrel.", { mateixaPagina: true }, [
    X.context("L'arrel és el costat del quadrat: amb 16 quadrets, el costat en té 4."),
    X.taulaResposta([16, 42, 42], ["", "Arrel", "Resultat"], [
      ["a)", dada("√16", MIDA.arrel), ms("4")],
      ["b)", dada("√9", MIDA.arrel), ""],
      ["c)", dada("√25", MIDA.arrel), ""],
      ["d)", dada("√36", MIDA.arrel), ""],
    ]),
  ]),

  ...X.exercici(7, "Escriu entre quins dos nombres és cada arrel.", {}, [
    X.context("Mira els quadrats: 9, 16, 25, 36, 49 i 64."),
    X.taulaResposta([16, 28, 28, 28], ["", "Arrel", "Entre", "i"], [
      ["a)", dada("√13", MIDA.arrel), ms("3"), ms("4")],
      ["b)", dada("√20", MIDA.arrel), "", ""],
      ["c)", dada("√30", MIDA.arrel), "", ""],           // nou
      ["d)", dada("√50", MIDA.arrel), "", ""],           // nou
    ]),
  ]),

  ...X.exercici(8, "Escriu el nombre que fan les centenes, les desenes i les unitats.", { mateixaPagina: true }, [
    X.taulaResposta([10, 22, 22, 22, 24], ["", "Centenes", "Desenes", "Unitats", "El nombre"], [
      ["a)", dada("2"), dada("4"), dada("3"), ms("243")],
      ["b)", dada("3"), dada("0"), dada("5"), ""],
      ["c)", dada("1"), dada("2"), dada("4"), ""],
      ["d)", dada("0"), dada("3"), dada("6"), ""],
    ]),
  ]),

  ...X.exercici(9, "Escriu com es diu cada nombre. Mira la clau.", {}, [
    clauNoms(),
    () => X.espai(8, { keepNext: true }),
    X.context("El guionet va entre les desenes i les unitats, i entre les unitats i les centenes. Del 21 al 29, amb una i."),
    X.taulaResposta([10, 18, 72], ["", "Nombre", "Es diu"], [
      ["a)", dada("243"), ms("dos-cents quaranta-tres")],
      ["b)", dada("510"), ""],
      ["c)", dada("222"), ""],
      ["d)", dada("108"), ""],
    ]),
  ]),

  /* El 10 va sol: amb la clau dels noms, el 9 ja omple la pàgina. */
  ...X.exercici(10, "Fes primer el que toca. Després fes l'altra operació.", {}, [
    X.context("Sense parèntesis, primer es multiplica. Amb parèntesis, primer es fa el parèntesi."),
    X.taulaResposta([10, 30, 30, 30], ["", "Operació", "Primer", "Després"], [
      ["a)", dada("2 + 3 · 4"), ms("3 · 4 = 12"), ms("2 + 12 = 14")],
      ["b)", dada("1 + 2 · 5"), "", ""],
      ["c)", dada("(2 + 3) · 4"), "", ""],
      ["d)", dada("4 · (1 + 2)"), "", ""],
    ]),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const TRAS_TITOL = { spacing: { before: X.tw(5), after: X.tw(8) } };

const solucionari = privat => [
  ...sol.titol(1),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Sense calculadora: la *targeta de les taules* és al davant tota l'estona, i a l'exercici 9 hi ha la clau dels noms.`,
    "*Com s'ha construït:* l'ordre dels exercicis és el de l'examen del grup, sense els exercicis de propietats de les potències i de potències de 10. A cada exercici, l'apartat a) resolt com a model i tres per fer, amb els ítems de les quatre fitxes de la unitat. Cap pregunta de justificació oberta. Els apartats marcats «nou» no són a les fitxes: revisa'ls abans de fer servir l'examen.",
    "*Si cal, en dues sessions:* els exercicis 1 a 5 (la multiplicació) i els 6 a 10 (quadrats, arrels, nombres i ordre).",
    "*Dues valoracions separades:* si falla un resultat, mira si ha triat bé què fer (la taula, la part de 10, l'operació que va primer) i si ha buscat bé a la targeta. Un error de targeta no hauria de fer baixar la valoració del que ha decidit.",
  ]),

  sol.h3("1. Buscar a la targeta"),
  sol.p("a) resolt: *7 · 8 = 56*; b) *9 · 7 = 63*; c) *8 · 5 = 40*; d) *8 · 4 = 32*. Són les de la pàgina 3 de la fitxa de repàs.", TRAS_TITOL),

  sol.h3("2. El número que falta"),
  sol.p("a) resolt: *7 · 8 = 56*, falta el 8; b) *6 · 7 = 42*, el 7; c) *5 · 4 = 20*, el 5; d) *4 · 7 = 28*, el 4.", TRAS_TITOL),
  sol.p("*Error típic:* escriure el resultat en lloc del número que falta. Als apartats c i d el forat és al davant: es busca a la taula del número que es té, i surt el rectangle girat (4 · 5 = 20)."),

  sol.h3("3. Girar el rectangle"),
  sol.p("a) resolt: *8 · 7 = 56*; b) *9 · 6 = 54*; c) *8 · 6 = 48*; d) *5 · 2 = 10*. Si ho busca a la targeta en lloc de girar el rectangle, també està bé: surt el mateix.", TRAS_TITOL),

  sol.h3("4. Partir el rectangle pel 10"),
  ...sol.taula([16, 21, 21, 22, 20], [
    ["", "Multiplicació", "La part de 10", "La part petita", "Ajunta-les"],
    ["a) resolt", "3 · 12", "3 · 10 = 30", "3 · 2 = 6", "30 + 6 = 36"],
    ["b)", "4 · 13", "4 · 10 = 40", "4 · 3 = 12", "40 + 12 = 52"],
    ["c)", "2 · 14", "2 · 10 = 20", "2 · 4 = 8", "20 + 8 = 28"],
    ["d)", "4 · 12", "4 · 10 = 40", "4 · 2 = 8", "40 + 8 = 48"],
  ]),
  sol.p("Les sumes es fan sense portar-ne. Si ho fa bé però s'equivoca en una part, que la busqui a la targeta."),

  sol.h3("5. El quadrat d'un nombre"),
  ...sol.taula([16, 16, 28, 20, 20], [
    ["", "Quadrat", "Es llegeix", "Multiplicació", "Resultat"],
    ["a) resolt", "3²", "3 al quadrat", "3 · 3", "9"],
    ["b)", "2²", "2 al quadrat", "2 · 2", "4"],
    ["c)", "4²", "4 al quadrat", "4 · 4", "16"],
    ["d)", "5²", "5 al quadrat", "5 · 5", "25"],
  ]),
  sol.p("*Error típic:* dir que 3² és 6, fent 3 · 2. És la regla trencada de la fitxa 1. Es dona per bo «3 elevat a 2» a la columna del mig."),

  sol.h3("6. El costat del quadrat"),
  sol.p("a) resolt: *√16 = 4*; b) *√9 = 3*; c) *√25 = 5*; d) *√36 = 6*. Si li costa, que busqui a la targeta la multiplicació amb els dos números iguals: 6 · 6 = 36.", TRAS_TITOL),

  sol.h3("7. Entre quins dos nombres · nivells alts"),
  ...sol.taula([20, 20, 30, 30], [
    ["", "Arrel", "Entre", "i"],
    ["a) resolt", "√13", "3 (3² = 9)", "4 (4² = 16)"],
    ["b)", "√20", "4 (4² = 16)", "5 (5² = 25)"],
    ["c) nou", "√30", "5 (5² = 25)", "6 (6² = 36)"],
    ["d) nou", "√50", "7 (7² = 49)", "8 (8² = 64)"],
  ]),
  sol.p("És l'exercici 9 de la fitxa 1, sense el dibuix. *Compta per als nivells alts, no per al mínim.*"),

  sol.h3("8. Centenes, desenes i unitats"),
  sol.p("a) resolt: *243*; b) *305*; c) *124*; d) *36*. *Error típic:* a l'apartat b, escriure 35, sense el zero de les desenes. A l'apartat d, el 0 de les centenes no s'escriu: és 36, no 036.", TRAS_TITOL),

  sol.h3("9. El nom del nombre"),
  sol.p("a) resolt: *dos-cents quaranta-tres*; b) *cinc-cents deu*; c) *dos-cents vint-i-dos*; d) *cent vuit*. *Error típic:* el guionet. Entre la centena i la resta no n'hi va: «cent vuit», i no «cent-vuit».", TRAS_TITOL),

  sol.h3("10. Què es fa primer"),
  ...sol.taula([22, 26, 26, 26], [
    ["", "Operació", "Primer", "Després"],
    ["a) resolt", "2 + 3 · 4", "3 · 4 = 12", "2 + 12 = 14"],
    ["b)", "1 + 2 · 5", "2 · 5 = 10", "1 + 10 = 11"],
    ["c)", "(2 + 3) · 4", "2 + 3 = 5", "5 · 4 = 20"],
    ["d)", "4 · (1 + 2)", "1 + 2 = 3", "4 · 3 = 12"],
  ]),
  sol.p("*Error típic:* fer-ho d'esquerra a dreta, com es llegeix, i escriure 15 a l'apartat b. És la regla trencada de la fitxa 3."),

  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Exercicis 1 i 2 → busca a la targeta una multiplicació i el número que falta.",
    "Exercicis 3 i 4 → fa servir el rectangle: el gira i el parteix pel 10.",
    "Exercicis 5 i 6 → el quadrat d'un nombre i el seu costat.",
    "Exercici 7 → *nivells alts*: entre quins dos nombres és una arrel.",
    "Exercicis 8 i 9 → centenes, desenes i unitats fins al 999, i el nom del nombre, amb el zero.",
    "Exercici 10 → l'ordre de les operacions, amb parèntesi i sense.",
  ]),
  sol.p("Els criteris de la SA del grup (1.3, 2.1 i 8.1) són de referència: l'avaluació es fa amb els criteris del PI. Una explicació oral registrada en el moment, o el codi d'una tasca tancada de la caixa d'eines, valen igual que l'examen escrit."),
];

X.genera({
  unitat: 1, alumnat, solucionari,
  materia: "Matemàtiques",
  creador: "Matemàtiques",
  avis: { text: "Pots fer servir la targeta de les taules a tot l'examen.", icona: "targeta" },
}).catch(e => { console.error(e.message); process.exit(1); });
