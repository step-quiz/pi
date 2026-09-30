#!/usr/bin/env node
/*
  4eso/generadors/examens/ud2.js · examen de la Unitat 2 (Percentatges i matemàtica financera)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a comu/examens/nucli.js i les
  regles, a comu/docs/EXAMENS-DOCX.md. El model és ud1.js.

      node 4eso/generadors/examens/ud2.js   →  4eso/docx/examen-ud2-alumnat.docx
                                                4eso/docx/examen-ud2-solucionari.docx

  D'on surt cada cosa:
  · Els apartats a), b), c) i d), dels exercicis de fitxes/ud2.html i del seu solucionari.
    On la fitxa no en tenia prou, n'hi ha un de nou, i al solucionari porta la marca «nou».
  · Sense les preguntes de justificació oberta de la fitxa (6e i 7c).
  · La regla trencada de la fitxa (5c, el portàtil que surt més barat a terminis) hi és,
    com a apartat c) de l'exercici 5.
  · Cada xifra, calculada aquí i comprovada abans d'escriure-la (cal()).
  Proposta del 30/9/2026, per validar amb el docent.
*/
"use strict";

const X = require("../../../comu/examens/nucli");
const { dada, ms, sol } = X;

const cal = (cond, msg) => { if (!cond) throw new Error("ud2.js: " + msg); };
const e2 = x => x.toFixed(2).replace(".", ",") + " €";
const f = x => String(Math.round(x * 100) / 100).replace(".", ",");
const quasi = (a, b) => Math.abs(a - b) < 1e-9;
/* Espais que no es parteixen: «− 5 %» i «30 €» no poden quedar a dues línies. */
const nb = s => s.replace(/(\d) (?=€|%)/g, "$1\u00A0").replace(/− (?=\d)/g, "−\u00A0").replace(/(\d) × (?=\d)/g, "$1\u00A0×\u00A0");
const txt = (s, o) => dada(nb(s), undefined, { esq: true, ...o });

/* ------------------------------------------------------------ les dades -- */
// [preu, factor, preu final]
const UN_CANVI = [[300, 0.8], [80, 1.21], [45, 0.9], [120, 1.1]];
const DOS = [[300, 0.8, 1.21], [200, 0.7, 1.21], [50, 1.21, 0.9], [100, 0.9, 0.9]];
const PUJA_BAIXA = [[100, 1.1, 0.9], [200, 1.2, 0.8], [50, 0.5, 1.5], [80, 1.25, 0.75]];   // el d és nou
cal(PUJA_BAIXA.every(([p, a, b]) => p * a * b < p), "pujar i baixar ha de quedar per sota");
// [compra, preu, factor al comptat, quotes, quota]
const PAGAR = [["Un mòbil de 300 €", 300, 0.85, 12, 24], ["Una bici de 240 €", 240, 0.9, 6, 42],
               ["Un portàtil de 500 €", 500, 0.95, 10, 46], ["Una tele de 600 €", 600, 0.9, 12, 50]];
const guanya = ([, p, fa, q, u]) => (p * fa < q * u ? "Al comptat" : "A terminis");
cal(PAGAR.map(guanya).join() === "Al comptat,Al comptat,A terminis,Al comptat", "l'apartat c ha de trencar la regla");
const IVA = [[40, 1.21], [25, 1.21], [60, 1.21], [12, 1.1]];
cal(quasi(12 * 1.1, 13.2) && quasi(60 * 1.21, 72.6), "IVA");

/* ------------------------------------------------------------- l'alumnat -- */
const alumnat = [
  ...X.exercici(1, "Escriu el factor que correspon a cada canvi de preu.", { calc: true }, [
    X.taulaResposta([12, 24, 32, 32], ["", "Canvi", "Compte", "Factor"], [
      ["a)", ms(nb("− 20 %")), ms(nb("1 − 0,20")), ms("× 0,8")],
      ["b)", dada(nb("+ 21 %")), "", ""],
      ["c)", dada(nb("− 50 %")), "", ""],
      ["d)", dada(nb("− 5 %")), "", ""],
    ]),
  ]),

  ...X.exercici(2, "Calcula el preu final quan hi ha un sol canvi.", { calc: true }, [
    X.taulaResposta([10, 20, 20, 22, 28], ["", "Preu", "Canvi", "Factor", "Preu final"], [
      ["a)", ms(nb("300 €")), ms(nb("− 20 %")), ms("× 0,8"), ms(nb("240,00 €"))],
      ["b)", dada(nb("80 €")), dada(nb("+ 21 %")), "", ""],
      ["c)", dada(nb("45 €")), dada(nb("− 10 %")), "", ""],
      ["d)", dada(nb("120 €")), dada(nb("+ 10 %")), "", ""],
    ]),
  ]),

  ...X.exercici(3, "Calcula el preu final quan hi ha dos canvis seguits.", { calc: true }, [
    X.context("Multiplica pel primer factor i, al resultat, multiplica pel segon."),
    X.taulaResposta([8, 15, 15, 15, 25, 22], ["", "Preu", "1r canvi", "2n canvi", "Els dos factors", "Preu final"], [
      ["a)", ms(nb("300 €")), ms(nb("− 20 %")), ms(nb("+ 21 %")), ms("× 0,8  × 1,21"), ms(nb("290,40 €"))],
      ["b)", dada(nb("200 €")), dada(nb("− 30 %")), dada(nb("+ 21 %")), "", ""],
      ["c)", dada(nb("50 €")), dada(nb("+ 21 %")), dada(nb("− 10 %")), "", ""],
      ["d)", dada(nb("100 €")), dada(nb("− 10 %")), dada(nb("− 10 %")), "", ""],
    ]),
  ]),

  ...X.exercici(4, "Comprova si pujar i baixar el mateix percentatge torna al preu de sortida.", { calc: true }, [
    X.taulaResposta([8, 14, 14, 16, 14, 16, 18], ["", "Preu", "Primer", "Queda", "Després", "Final", "Torna?"], [
      ["a)", ms(nb("100 €")), ms("× 1,1"), ms(nb("110 €")), ms("× 0,9"), ms(nb("99 €")), ms("No")],
      ["b)", dada(nb("200 €")), dada("× 1,2"), "", dada("× 0,8"), "", ""],
      ["c)", dada(nb("50 €")), dada("× 0,5"), "", dada("× 1,5"), "", ""],
      ["d)", dada(nb("80 €")), dada("× 1,25"), "", dada("× 0,75"), "", ""],               // nou
    ]),
  ]),

  ...X.exercici(5, "Escriu quina manera de pagar surt més a compte.", { calc: true }, [
    X.context("Al comptat hi ha un descompte. A terminis pagues en quotes."),
    X.taulaResposta([8, 38, 18, 18, 18], ["", "Compra", "Al comptat", "A terminis", "Guanya"], [
      ["a)", ms(nb("Un mòbil de 300 €. Al comptat, − 15 %. O 12 quotes de 24 €."), undefined, { esq: true }),
             ms(nb("255 €")), ms(nb("288 €")), ms("Al comptat")],
      ["b)", txt("Una bici de 240 €. Al comptat, − 10 %. O 6 quotes de 42 €."), "", "", ""],
      ["c)", txt("Un portàtil de 500 €. Al comptat, − 5 %. O 10 quotes de 46 €."), "", "", ""],
      ["d)", txt("Una tele de 600 €. Al comptat, − 10 %. O 12 quotes de 50 €."), "", "", ""],  // nou
    ]),
  ]),

  ...X.exercici(6, "Calcula el preu amb IVA.", { calc: true }, [
    X.taulaResposta([10, 24, 18, 22, 26], ["", "Sense IVA", "IVA", "Factor", "Amb IVA"], [
      ["a)", ms(nb("40 €")), ms(nb("21 %")), ms("× 1,21"), ms(nb("48,40 €"))],
      ["b)", dada(nb("25 €")), dada(nb("21 %")), "", ""],
      ["c)", dada(nb("60 €")), dada(nb("21 %")), "", ""],
      ["d)", dada(nb("12 €")), dada(nb("10 %")), "", ""],
    ]),
  ]),

  ...X.exercici(7, "Calcula què pagues de cada manera i marca la més barata.", { calc: true }, [
    X.taulaResposta([8, 38, 18, 18, 18], ["", "Situació", "Una manera", "L'altra", "Més barata"], [
      ["a)", ms(nb("Bambes. A la botiga, 80 € amb − 20 %. Per internet, 70 € amb − 10 %."), undefined, { esq: true }),
             ms(nb("64 €")), ms(nb("63 €")), ms("Per internet")],
      ["b)", txt("Gimnàs, un mes. Abonament de 40 € amb − 25 %. O 12 entrades de 3 €."), "", "", ""],
      ["c)", txt("Un llibre. A la llibreria, 20 € amb − 5 %. Per internet, 18 € i 2 € d'enviament."), "", "", ""], // nou
      ["d)", txt("Cinema. 5 entrades de 8 €. O un carnet de 5 entrades per 30 €."), "", "", ""],                  // nou
    ]),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const TRAS_TITOL = { spacing: { before: X.tw(5), after: X.tw(8) } };
const LET = ["a) resolt", "b)", "c)", "d)"];

const solucionari = privat => [
  ...sol.titol(2),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Fita d'assoliment esperada: *AS* als criteris 1.1 i 5.1. Calculadora disponible a tot l'examen.`,
    "*Com s'ha construït:* a cada exercici, l'apartat a) resolt com a model i tres apartats per fer, amb els ítems de la fitxa (_fitxes/ud2.html_) i del seu solucionari. Sense les dues preguntes de justificació oberta de la fitxa (6e i 7c). Els apartats marcats «nou» no són a la fitxa: revisa'ls abans de fer servir l'examen.",
    "*Dues valoracions separades:* puntua per separat si la *decisió* és correcta i si el *càlcul* és correcte. Un error aritmètic no hauria de fer baixar la valoració de la decisió.",
  ]),

  sol.h3("1. El factor de cada canvi — criteri 5.1"),
  ...sol.taula([19, 22, 30, 29], [
    ["", "Canvi", "Compte", "Factor"],
    ["a) resolt", "− 20 %", "1 − 0,20", "× 0,8"],
    ["b)", "+ 21 %", "1 + 0,21", "× 1,21"],
    ["c)", "− 50 %", "1 − 0,50", "× 0,5"],
    ["d)", "− 5 %", "1 − 0,05", "× 0,95"],
  ]),
  sol.p("*Error típic:* escriure × 0,5 per a un − 5 % (confondre 0,05 amb 0,5). Si passa, feu-li llegir el percentatge en veu alta: «cinc centèsimes», no «cinc dècimes»."),

  sol.h3("2. Un sol canvi — criteri 5.1"),
  ...sol.taula([19, 18, 18, 20, 25],
    [["", "Preu", "Canvi", "Factor", "Preu final"]].concat(UN_CANVI.map(([p, fa], i) =>
      [LET[i], `${p} €`, fa > 1 ? `+ ${Math.round((fa - 1) * 100)} %` : `− ${Math.round((1 - fa) * 100)} %`,
       `× ${f(fa)}`, e2(p * fa)]))),
  sol.p("*Error típic:* multiplicar per 0,2 en comptes de 0,8, és a dir, calcular el descompte i quedar-s'hi. El factor ja dona el preu final."),

  sol.h3("3. Dos canvis seguits — criteri 5.1"),
  ...sol.taula([19, 15, 36, 30],
    [["", "Preu", "Els dos factors", "Preu final"]].concat(DOS.map(([p, a, b], i) =>
      [LET[i], `${p} €`, `× ${f(a)} × ${f(b)}`, e2(p * a * b)]))),
  sol.p("L'apartat d) és el que val més: dos descomptes del 10 % no fan un 20 %. Queden 81 €, no 80 €."),

  sol.h3("4. Pujar i baixar el mateix — criteri 1.1"),
  ...sol.taula([19, 15, 22, 18, 26],
    [["", "Preu", "Passos", "Final", "Torna?"]].concat(PUJA_BAIXA.map(([p, a, b], i) =>
      [(i === 3 ? "d) nou" : LET[i]), `${p} €`, `× ${f(a)} → ${f(p * a)} € × ${f(b)}`, e2(p * a * b),
       `No, en falten ${e2(p - p * a * b)}`]))),
  sol.p("Sempre queda per sota, perquè el segon percentatge s'aplica sobre un preu diferent. No cal que ho justifiqui: n'hi ha prou que ho vegi en els quatre casos."),

  sol.h3("5. Quina manera de pagar surt més a compte — criteri 1.1"),
  ...sol.taula([13, 23, 22, 20, 22],
    [["", "Compra", "Al comptat", "A terminis", "Guanya"]].concat(PAGAR.map(([c, p, fa, q, u], i) =>
      [(i === 3 ? "d) nou" : LET[i]), c.replace(/^Un[a]? /, ""), `${p} × ${f(fa)} = ${f(p * fa)} €`,
       `${q} × ${u} = ${q * u} €`, `*${guanya(PAGAR[i])}*`]))),
  sol.p("*L'apartat c) és el més important de l'examen.* Trenca la regla «al comptat sempre és millor» que l'alumnat s'haurà fabricat amb a) i b): el portàtil surt 15 € més barat a terminis. Si tria «al comptat» sense fer els números, és que recorda en lloc de calcular. Compta per als nivells alts (AN, AE), no per al mínim."),

  sol.h3("6. El preu amb IVA — criteri 5.1"),
  ...sol.taula([19, 22, 16, 20, 23],
    [["", "Sense IVA", "IVA", "Factor", "Amb IVA"]].concat(IVA.map(([p, fa], i) =>
      [LET[i], `${p} €`, `${Math.round((fa - 1) * 100)} %`, `× ${f(fa)}`, e2(p * fa)]))),
  sol.p("A l'apartat d), l'IVA és el reduït (10 %): el factor és × 1,1 i no × 1,21. Si hi posa 1,21, és que copia el factor de dalt sense mirar el percentatge."),

  sol.h3("7. Què pagues de cada manera — criteri 1.1"),
  ...sol.taula([13, 27, 22, 20, 18], [
    ["", "Situació", "Una manera", "L'altra", "Més barata"],
    ["a) resolt", "Bambes", "80 × 0,8 = 64 €", "70 × 0,9 = 63 €", "*Per internet*"],
    ["b)", "Gimnàs", "40 × 0,75 = 30 €", "12 × 3 = 36 €", "*L'abonament*"],
    ["c) nou", "Llibre", "20 × 0,95 = 19 €", "18 + 2 = 20 €", "*La llibreria*"],
    ["d) nou", "Cinema", "5 × 8 = 40 €", "30 €", "*El carnet*"],
  ]),
  sol.p("A l'apartat a), el descompte més gran (20 %) no guanya: és la mateixa idea de l'exercici 5c en una altra situació. Al c), el preu més baix per internet (18 €) tampoc: cal sumar-hi l'enviament."),

  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Exercicis 1, 2, 3 i 6 → criteri *5.1*, fer servir el factor multiplicador amb la calculadora.",
    "Exercicis 4, 5 i 7 → criteri *1.1*, decidir en una situació real amb els números fets.",
    "El mínim (AS) és fer bé els apartats b) dels exercicis 1, 2, 5 i 6. Els apartats 5c i 7a compten per als nivells alts.",
  ]),
  sol.p("L'objectiu de l'examen *no és calcular bé*: és triar la manera de pagar amb els comptes fets. Els errors de càlcul no haurien de fer baixar la valoració de la decisió."),
];

X.genera({ unitat: 2, alumnat, solucionari }).catch(e => { console.error(e.message); process.exit(1); });
