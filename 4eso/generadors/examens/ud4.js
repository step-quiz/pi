#!/usr/bin/env node
/*
  4eso/generadors/examens/ud4.js · examen de la Unitat 4 (Equacions de 2n grau)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a comu/examens/nucli.js i les
  regles, a comu/docs/EXAMENS-DOCX.md. El model és ud1.js.

      node 4eso/generadors/examens/ud4.js   →  4eso/docx/examen-ud4-alumnat.docx
                                                4eso/docx/examen-ud4-solucionari.docx

  D'on surt cada cosa:
  · Els apartats a), b), c) i d), dels exercicis de fitxes/ud4.html i del seu solucionari.
    On la fitxa no en tenia prou, n'hi ha un de nou, i al solucionari porta la marca «nou».
  · Com la fitxa, l'examen no demana mai aïllar la x ni la fórmula general: la balança,
    comprovar, x² = k amb l'arrel i decidir quina solució té sentit.
  · Sense les preguntes obertes de la fitxa (6e i 7d). La balança, sense dibuix: l'equació
    sola, amb la frase de la balança al context.
  · La regla trencada de la fitxa (5d, el congelador a −3) hi és, com a apartat d) de l'exercici 5.
  Proposta del 30/9/2026, per validar amb el docent.
*/
"use strict";

const X = require("../../../comu/examens/nucli");
const { dada, ms, sol } = X;

const cal = (cond, msg) => { if (!cond) throw new Error("ud4.js: " + msg); };
const f = (x, d = 2) => String(Math.round(x * 10 ** d) / 10 ** d).replace(".", ",").replace("-", "−");
const nb = s => s.replace(/(\d) (?=m²|m\b|s\b|°C)/g, "$1 ").replace(/ = /g, " = ").replace(/([+−]) (?=\d)/g, "$1 ");
const txt = s => dada(nb(s), undefined, { esq: true });
const LL = ["b)", "c)", "d)"];

/* ------------------------------------------------------------ les dades -- */
const BALANCA = [["x + 2 = 6", 4], ["x + 3 = 8", 5], ["2x = 8", 4], ["x + 7 = 10", 3]];       // el d és nou
const PROVA = [["x + 3 = 7", 4, x => x + 3, 7], ["x + 5 = 12", 6, x => x + 5, 12],
               ["x + 5 = 12", 7, x => x + 5, 12], ["2x = 10", 4, x => 2 * x, 10]];
const ARREL = [36, 49, 100, 20];
const HORT = [36, 49, 81, 30];
const SENTIT = [["x² = 36. La x és el costat d'un hort.", 36, "6", "−6"], ["x² = 25. La x és l'edat d'un gos.", 25, "5", "−5"],
                ["x² = 64. La x és l'altura d'un arbre.", 64, "8", "−8"],
                ["x² = 9. La x és la temperatura d'un congelador.", 9, "−3", "3"]];
const P = x => x * x - 5 * x + 6;
const PROVES = [2, 3, 1, 4];
cal(PROVES.map(P).join() === "0,0,2,2", "x² − 5x + 6");
const VIDA = [["El terra quadrat d'una habitació fa 16 m². La x és el costat.", 16, "4 m"],
              ["Una pedra cau d'un pont. La x són els segons que triga.", 9, "3 s"],
              ["Un pàrquing a sota terra. La x és la planta on pares.", 4, "la planta −2"],
              ["Un submarí baixa sota el mar. La x és l'altura, en metres.", 100, "−10 m"]];      // el d és nou

/* ------------------------------------------------------------- l'alumnat -- */
const alumnat = [
  ...X.exercici(1, "Pensa en la balança i escriu quant val la x.", {}, [
    X.context("Una equació és una balança. El que treus d'una banda, ho treus de l'altra."),
    X.taulaResposta([10, 45, 45], ["", "Equació", "x val"], [
      ["a)", ms(nb("x + 2 = 6")), ms(nb("x = 4"))],
      ...BALANCA.slice(1).map(([e], i) => [LL[i], dada(nb(e)), ""]),
    ]),
  ]),

  ...X.exercici(2, "Comprova si el número és la solució.", { calc: true }, [
    X.taulaResposta([8, 20, 14, 22, 16, 20], ["", "Equació", "Provo", "Banda esquerra", "Banda dreta", "Funciona?"], [
      ["a)", ms(nb("x + 3 = 7")), ms(nb("x = 4")), ms(nb("4 + 3 = 7")), ms("7"), ms("sí")],
      ...PROVA.slice(1).map(([e, v, , d], i) => [LL[i], dada(nb(e)), dada(nb(`x = ${v}`)), "", dada(String(d)), ""]),
    ]),
  ]),

  ...X.exercici(3, "Resol amb l'arrel quadrada de la calculadora.", { calc: true }, [
    X.context("A l'apartat d), arrodoneix a 2 decimals."),
    X.taulaResposta([10, 30, 30, 30], ["", "Equació", "A la calculadora", "x val"], [
      ["a)", ms(nb("x² = 36")), ms("√36"), ms("6")],
      ...ARREL.slice(1).map((k, i) => [LL[i], dada(nb(`x² = ${k}`)), "", ""]),
    ]),
  ]),

  ...X.exercici(4, "Un hort quadrat. Escriu l'equació i troba el costat.", { calc: true }, [
    X.context("A l'apartat d), arrodoneix a 2 decimals."),
    X.taulaResposta([10, 30, 30, 30], ["", "Àrea", "L'equació", "El costat"], [
      ["a)", ms(nb("36 m²")), ms(nb("x² = 36")), ms(nb("6 m"))],
      ...HORT.slice(1).map((k, i) => [LL[i], dada(nb(`${k} m²`)), "", ""]),
    ]),
  ]),

  ...X.exercici(5, "Escriu les dues solucions i la que té sentit.", {}, [
    X.taulaResposta([8, 52, 22, 18], ["", "Situació", "Solucions", "Té sentit"], [
      ["a)", ms(nb(SENTIT[0][0]), undefined, { esq: true }), ms(nb("6 i −6")), ms("6")],
      ...SENTIT.slice(1).map(([s], i) => [LL[i], txt(s), "", ""]),
    ]),
  ]),

  ...X.exercici(6, "Comprova quins números són solució d'aquesta equació.", { calc: true }, [
    X.context("x² − 5x + 6 = 0. Omple una columna cada vegada. La calculadora fa la feina."),
    X.taulaResposta([8, 14, 14, 14, 34, 16], ["", "Provo", "x²", "5x", "x² − 5x + 6", "És 0?"], [
      ["a)", ms(nb("x = 2")), ms("4"), ms("10"), ms(nb("4 − 10 + 6 = 0")), ms("sí")],
      ...PROVES.slice(1).map((v, i) => [LL[i], dada(nb(`x = ${v}`)), "", "", "", ""]),
    ]),
  ]),

  ...X.exercici(7, "Escriu l'equació, les dues solucions i la que té sentit.", {}, [
    X.taulaResposta([8, 40, 20, 16, 16], ["", "Situació", "Equació", "Solucions", "Té sentit"], [
      ["a)", ms(nb(VIDA[0][0]), undefined, { esq: true }), ms(nb("x² = 16")), ms(nb("4 i −4")), ms(nb("4 m"))],
      ...VIDA.slice(1).map(([s, k], i) => [LL[i], txt(s), dada(nb(`x² = ${k}`)), "", ""]),
    ]),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const LET = ["a) resolt", "b)", "c)", "d)"];
const solucionari = privat => [
  ...sol.titol(4),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Fita d'assoliment esperada: *NA o AS*; el criteri on més pot lluir és l'1.1, interpretar les solucions. Calculadora disponible a tot l'examen.`,
    "*Com s'ha construït:* a cada exercici, l'apartat a) resolt com a model i tres apartats per fer, amb els ítems de la fitxa (_fitxes/ud4.html_) i del seu solucionari. No es demana mai aïllar la incògnita ni la fórmula general, com a la fitxa. Sense les preguntes obertes de la fitxa (6e i 7d). Els apartats marcats «nou» no són a la fitxa: revisa'ls abans de fer servir l'examen.",
    "*Dues valoracions separades:* puntua per separat si la *decisió* és correcta i si el *càlcul* és correcte. Un error aritmètic no hauria de fer baixar la valoració de la decisió.",
  ]),

  sol.h3("1. La balança"),
  sol.p(BALANCA.map(([e, v], i) => `${"abcd"[i]}) ${e} → *x = ${v}*${i === 3 ? " (nou)" : ""}`).join("  ·  "),
        { spacing: { before: X.tw(5), after: X.tw(8) } }),
  sol.p("A l'apartat c) hi ha dues bosses iguals i vuit daus: es reparteixen els daus entre les dues bosses. Si es bloqueja, que ho faci amb objectes damunt la taula. Si la balança no li diu res, la doble recta de la caixa d'eines té el cas «Equació x + 3 = 7»."),

  sol.h3("2. Comprovar — criteri 1.1"),
  ...sol.taula([16, 20, 14, 20, 14, 16], [["", "Equació", "Provo", "Esquerra", "Dreta", "Funciona?"]].concat(
    PROVA.map(([e, v, fe, d], i) => [LET[i], e, `x = ${v}`, `${fe(v)}`, `${d}`, `*${fe(v) === d ? "sí" : "no"}*`]))),
  sol.p("Comprovar és substituir i comparar, sense manipulació algebraica. És l'exercici on més pot lluir."),

  sol.h3("3. Amb l'arrel quadrada"),
  ...sol.taula([19, 27, 27, 27], [["", "Equació", "A la calculadora", "x val"]].concat(
    ARREL.map((k, i) => [LET[i], `x² = ${k}`, `√${k}`, Number.isInteger(Math.sqrt(k)) ? `*${Math.sqrt(k)}*`
                                                            : `${f(Math.sqrt(k), 7)}… → *${f(Math.sqrt(k))}*`]))),
  sol.p("L'apartat d) enllaça amb la Unitat 1: un nombre que no s'acaba i quants decimals s'hi escriuen."),

  sol.h3("4. L'hort quadrat"),
  ...sol.taula([19, 27, 27, 27], [["", "Àrea", "L'equació", "El costat"]].concat(
    HORT.map((k, i) => [LET[i], `${k} m²`, `x² = ${k}`, Number.isInteger(Math.sqrt(k)) ? `*${Math.sqrt(k)} m*`
                                                         : `${f(Math.sqrt(k), 3)}… → *${f(Math.sqrt(k))} m*`]))),

  sol.h3("5. Quina solució té sentit — criteri 1.1"),
  ...sol.taula([16, 44, 20, 20], [["", "Situació", "Solucions", "Té sentit"]].concat(
    SENTIT.map(([s, , bo, dolent], i) => [LET[i], s, `${bo.replace("−", "")} i −${bo.replace("−", "")}`, `*${bo}*`]))),
  sol.p("*L'apartat d) és el més important de l'examen.* Als apartats a, b i c es descarta sempre el negatiu, i l'alumnat se'n fabrica la regla «el negatiu no val mai». Al d), un congelador és sota zero: la solució bona és −3 °C. Si ratlla el −3 sense pensar, és on cal aturar-se. Compta per als nivells alts (AN, AE), no per al mínim."),

  sol.h3("6. Comprovar una equació de 2n grau"),
  ...sol.taula([16, 14, 14, 14, 26, 16], [["", "Provo", "x²", "5x", "x² − 5x + 6", "És 0?"]].concat(
    PROVES.map((v, i) => [LET[i], `x = ${v}`, `${v * v}`, `${5 * v}`, `${v * v} − ${5 * v} + 6 = ${P(v)}`,
                           `*${P(v) === 0 ? "sí" : "no"}*`]))),
  sol.p("Les solucions són el 2 i el 3. Entra en una equació de 2n grau completa per la comprovació, no per la resolució: cada casella és una sola tecla de calculadora."),

  sol.h3("7. A la vida de cada dia — criteri 1.1"),
  ...sol.taula([13, 43, 14, 14, 16], [["", "Situació", "Equació", "Solucions", "Té sentit"]].concat(
    VIDA.map(([s, k, r], i) => [(i === 3 ? "d) nou" : LET[i]), s, `x² = ${k}`, `${Math.sqrt(k)} i −${Math.sqrt(k)}`, `*${r}*`]))),
  sol.p("Als apartats a i b es descarta el negatiu; als c i d, el positiu. Qui hagi entès que «el negatiu no val mai» fallarà el c i el d. És la mateixa idea del congelador (5d) en situacions noves."),

  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Exercicis 2 i 6 → comprovar. És on pot lluir, i és aritmètica de calculadora.",
    "Exercicis 5 i 7 → criteri *1.1*, decidir quina solució té sentit. És el fil de la SA.",
    "El mínim (AS) és fer bé l'exercici 2 i els apartats b) i c) del 3 i del 5. Els apartats 5d, 7c i 7d compten per als nivells alts.",
  ]),
  sol.p("Aquesta és la unitat difícil del curs. Un NA aquí no és un fracàs sobrevingut: el PI ja ho preveu."),
];

X.genera({ unitat: 4, alumnat, solucionari }).catch(e => { console.error(e.message); process.exit(1); });
