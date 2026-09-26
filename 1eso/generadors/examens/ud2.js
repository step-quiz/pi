#!/usr/bin/env node
/*
  1eso/generadors/examens/ud2.js · examen de la Unitat 2 (Divisibilitat)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a comu/examens/nucli.js i les
  regles, a comu/docs/EXAMENS-DOCX.md.

      node 1eso/generadors/examens/ud2.js   →  1eso/docx/examen-ud2-alumnat.docx
                                                1eso/docx/examen-ud2-solucionari.docx

  D'on surt cada cosa:
  · L'ordre, dels vuit exercicis de l'examen de la unitat 2 del grup (múltiples,
    caixes i boles, divisibilitat, criteris, arbres, primers). El carnet
    d'identitat del grup es treballa a la fitxa de repàs, i no hi és.
  · Els apartats a), b), c) i d), de les cinc fitxes de la unitat (fitxes/ud2*.html)
    i dels seus solucionaris. L'únic que no hi és (exercici 8, d) porta la marca
    «nou» al solucionari.
  · Sense calculadora: l'avís és el de la targeta de les taules. Totes les
    multiplicacions són de la targeta, i cap nombre passa de 999.
*/
"use strict";

const X = require("../../../comu/examens/nucli");
const { dada, ms, sol } = X;

/* ------------------------------------------------------------ l'alumnat -- */
const alumnat = [
  ...X.exercici(1, "Escriu els sis primers múltiples de cada nombre. Mira la targeta.", {}, [
    X.context("Comença pel 0."),
    X.taulaResposta([10, 18, 72], ["", "Nombre", "Els múltiples"], [
      ["a)", dada("10"), ms("0, 10, 20, 30, 40, 50")],
      ["b)", dada("9"), ""],
      ["c)", dada("8"), ""],
      ["d)", dada("7"), ""],
    ]),
  ]),

  ...X.exercici(2, "Reparteix els quadrets en files. Omple la taula.", { mateixaPagina: true }, [
    X.taulaResposta([10, 22, 22, 23, 23], ["", "Quadrets", "A cada fila", "Files plenes", "En sobren"], [
      ["a)", dada("37"), dada("7"), ms("5"), ms("2")],
      ["b)", dada("20"), dada("4"), "", ""],
      ["c)", dada("23"), dada("9"), "", ""],
      ["d)", dada("20"), dada("6"), "", ""],
    ]),
  ]),

  ...X.exercici(3, "Sobren quadrets? Escriu la igualtat.", {}, [
    X.context("Busca el nombre a la taula de la targeta. Si hi és, no en sobra cap."),
    X.taulaResposta([10, 30, 22, 38], ["", "Repartiment", "Sobren?", "La igualtat"], [
      ["a)", dada("30 en files de 9"), ms("Sí, 3"), ms("30 = 3 · 9 + 3")],
      ["b)", dada("20 en files de 5"), "", ""],
      ["c)", dada("45 en files de 6"), "", ""],
      ["d)", dada("56 en files de 7"), "", ""],
    ]),
  ]),

  ...X.exercici(4, "Fes els quatre trucs. Escriu Sí o No.", { mateixaPagina: true }, [
    X.context("El 2, el 5 i el 10: mira l'última xifra. El 3: suma les xifres."),
    X.taulaResposta([10, 18, 18, 18, 18, 18], ["", "Nombre", "Del 2", "Del 5", "Del 10", "Del 3"], [
      ["a)", dada("160"), ms("Sí"), ms("Sí"), ms("Sí"), ms("No")],
      ["b)", dada("945"), "", "", "", ""],
      ["c)", dada("42"), "", "", "", ""],
      ["d)", dada("550"), "", "", "", ""],
    ]),
  ]),

  ...X.exercici(5, "Escriu les multiplicacions que donen cada nombre. Després escriu els divisors.", {}, [
    X.context("Sempre hi ha la fila d'1. Les altres, a la targeta."),
    X.taulaResposta([10, 14, 38, 38], ["", "Nombre", "Les multiplicacions", "Els divisors"], [
      ["a)", dada("20"), ms("1 · 20, 2 · 10, 4 · 5"), ms("1, 2, 4, 5, 10 i 20")],
      ["b)", dada("18"), "", ""],
      ["c)", dada("16"), "", ""],
      ["d)", dada("15"), "", ""],
    ]),
  ]),

  ...X.exercici(6, "És primer? Escriu la multiplicació.", { mateixaPagina: true }, [
    X.context("Un nombre primer només fa un rectangle, una fila."),
    X.taulaResposta([10, 20, 30, 40], ["", "Nombre", "És primer?", "La multiplicació"], [
      ["a)", dada("9"), ms("No"), ms("9 = 3 · 3")],
      ["b)", dada("7"), "", ""],
      ["c)", dada("15"), "", ""],
      ["d)", dada("11"), "", ""],
    ]),
  ]),

  ...X.exercici(7, "Escriu la factorització de cada nombre.", {}, [
    X.context("Pots fer l'arbre al marge: el primer a l'esquerra, i el que es torna a partir a la dreta."),
    X.taulaResposta([10, 20, 70], ["", "Nombre", "La factorització"], [
      ["a)", dada("12"), ms("12 = 2 · 2 · 3")],
      ["b)", dada("18"), ""],
      ["c)", dada("20"), ""],
      ["d)", dada("45"), ""],
    ]),
  ]),

  ...X.exercici(8, "Escriu els nombres primers de cada fila.", { mateixaPagina: true }, [
    X.context("Pensa en el garbell: ratlla l'1 i els múltiples del 2, el 3, el 5 i el 7."),
    X.taulaResposta([10, 35, 55], ["", "Nombres", "Els primers"], [
      ["a)", dada("De l'1 al 10"), ms("2, 3, 5 i 7")],
      ["b)", dada("De l'11 al 20"), ""],
      ["c)", dada("Del 21 al 30"), ""],
      ["d)", dada("Del 31 al 40"), ""],                    // nou
    ]),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const TRAS = { spacing: { before: X.tw(5), after: X.tw(8) } };

const solucionari = privat => [
  ...sol.titol(2),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Sense calculadora: la *targeta de les taules* és al davant tota l'estona.`,
    "*Com s'ha construït:* l'ordre és el dels vuit exercicis de l'examen del grup. El carnet d'identitat es treballa a la fitxa de repàs, i no hi és. A cada exercici, l'apartat a) resolt com a model i tres per fer, amb els ítems de les cinc fitxes de la unitat. Cap pregunta de justificació oberta. L'apartat marcat «nou» no és a les fitxes: revisa'l abans de fer servir l'examen.",
    "*Si cal, en dues sessions:* els exercicis 1 a 4 (múltiples, repartir i trucs) i els 5 a 8 (divisors, primers i factorització).",
    "*Dues valoracions separades:* si falla un resultat, mira si ha triat bé què fer (la taula, el truc, el rectangle) i si ha buscat bé a la targeta. Un error de targeta no hauria de fer baixar la valoració del que ha decidit.",
  ]),

  sol.h3("1. Els múltiples"),
  sol.p("b) *0, 9, 18, 27, 36, 45*; c) *0, 8, 16, 24, 32, 40*; d) *0, 7, 14, 21, 28, 35*. Són les llistes de la fitxa 1. *Error típic:* oblidar el 0.", TRAS),

  sol.h3("2. Repartir en files"),
  sol.p("b) 20 en files de 4: *5 files plenes, en sobren 0*. c) 23 en files de 9: *2 files plenes, en sobren 5*. d) 20 en files de 6: *3 files plenes, en sobren 2*. *Error típic:* no escriure el 0 quan no en sobra cap.", TRAS),

  sol.h3("3. Sobren quadrets?"),
  ...sol.taula([30, 25, 45], [
    ["", "Sobren?", "La igualtat"],
    ["a) resolt · 30 en files de 9", "Sí, 3", "30 = 3 · 9 + 3"],
    ["b) 20 en files de 5", "No", "20 = 4 · 5"],
    ["c) 45 en files de 6", "Sí, 3", "45 = 7 · 6 + 3"],
    ["d) 56 en files de 7", "No", "56 = 8 · 7"],
  ]),
  sol.p("Es dona per bona la igualtat exacta amb «+ 0» (20 = 4 · 5 + 0). *Error típic:* oblidar el residu: és la regla trencada de la fitxa 2."),

  sol.h3("4. Els quatre trucs"),
  ...sol.taula([20, 20, 20, 20, 20], [
    ["", "Del 2", "Del 5", "Del 10", "Del 3"],
    ["b) 945", "No", "Sí", "No", "Sí (9 + 4 + 5 = 18)"],
    ["c) 42", "Sí", "No", "No", "Sí (4 + 2 = 6)"],
    ["d) 550", "Sí", "Sí", "Sí", "No (5 + 5 + 0 = 10)"],
  ]),
  sol.p("Són els nombres de la taula de l'activitat 2_3 del grup, i de la fitxa 1."),

  sol.h3("5. Els divisors"),
  sol.p("b) 18: *1 · 18, 2 · 9, 3 · 6*; divisors *1, 2, 3, 6, 9 i 18*. c) 16: *1 · 16, 2 · 8, 4 · 4*; divisors *1, 2, 4, 8 i 16*. d) 15: *1 · 15, 3 · 5*; divisors *1, 3, 5 i 15*. *Error típic:* deixar-se l'1 i el mateix nombre, o escriure dos cops el 4 del 16.", TRAS),

  sol.h3("6. És primer?"),
  sol.p("b) 7: *sí*, 7 = 1 · 7. c) 15: *no*, 15 = 3 · 5. d) 11: *sí*, 11 = 1 · 11. *Error típic:* dir que el 9 o el 15 són primers perquè són senars: és la regla trencada de la fitxa 3.", TRAS),

  sol.h3("7. La factorització"),
  sol.p("b) *18 = 2 · 3 · 3*; c) *20 = 2 · 2 · 5*; d) *45 = 3 · 3 · 5*. Tots tenen tres factors primers com a molt, i cada pas de l'arbre és de la targeta (decisió del docent). Es dona per bo qualsevol ordre dels factors. *Error típic:* aturar-se abans d'hora (20 = 4 · 5): és la regla trencada de la fitxa 4.", TRAS),

  sol.h3("8. Els primers · la d, nou"),
  sol.p("b) *11, 13, 17 i 19*; c) *23 i 29*; d) nou: *31 i 37*. És el garbell de la fitxa 3. La fitxa demanava els primers fins al 30; la d) va una mica més enllà, amb el garbell sencer. *Compta per als nivells alts, no per al mínim.*", TRAS),

  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Exercici 1 → escriu els múltiples d'un nombre amb la targeta.",
    "Exercicis 2 i 3 → reparteix en files i diu el residu, i si la divisió és exacta.",
    "Exercici 4 → els trucs del 2, el 5, el 10 i el 3.",
    "Exercicis 5 i 6 → els divisors d'un nombre, i si és primer.",
    "Exercici 7 → la factorització, amb tres factors primers com a molt.",
    "Exercici 8 → els primers, amb el garbell. La d), *nivells alts*.",
  ]),
  sol.p("Els criteris de la SA del grup (1.4, 3.2, 4.2 i 5.2) són de referència: l'avaluació es fa amb els criteris del PI. Una explicació oral registrada en el moment, o el codi d'una tasca tancada de la caixa d'eines, valen igual que l'examen escrit."),
];

X.genera({
  unitat: 2, alumnat, solucionari,
  materia: "Matemàtiques",
  creador: "Matemàtiques",
  avis: { text: "Pots fer servir la targeta de les taules a tot l'examen.", icona: "targeta" },
}).catch(e => { console.error(e.message); process.exit(1); });
