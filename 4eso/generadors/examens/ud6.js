#!/usr/bin/env node
/*
  4eso/generadors/examens/ud6.js · examen de la Unitat 6 (Estadística amb dades reals)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a comu/examens/nucli.js i les
  regles, a comu/docs/EXAMENS-DOCX.md. El model és ud1.js.

      node 4eso/generadors/examens/ud6.js   →  4eso/docx/examen-ud6-alumnat.docx
                                                4eso/docx/examen-ud6-solucionari.docx

  D'on surt cada cosa:
  · Els apartats a), b), c) i d), dels exercicis de fitxes/ud6.html i del seu solucionari.
    On la fitxa no en tenia prou, n'hi ha un de nou, i al solucionari porta la marca «nou».
  · Els gràfics són els de la fitxa, llegits dels seus marcadors <!--grafic:NOM-->: així
    l'examen ensenya exactament el que s'ha treballat a la fitxa.
  · Sense les preguntes obertes de la fitxa (3e, 4e, 6f i 7e).
  · La regla trencada de la fitxa (6, el gràfic que comença a 90) hi és, com a exercici 6.
  Proposta del 30/9/2026, per validar amb el docent.
*/
"use strict";

const fs = require("fs");
const path = require("path");
const X = require("../../../comu/examens/nucli");
const { dada, ms, sol } = X;
const { AlignmentType, TableRow } = X.docx;

const cal = (cond, msg) => { if (!cond) throw new Error("ud6.js: " + msg); };
const f = (x, d = 2) => String(Math.round(x * 10 ** d) / 10 ** d).replace(".", ",");
const txt = s => dada(s, undefined, { esq: true });

/* Un gràfic de la fitxa, tal com hi és. Se li afegeix l'espai de noms i la mida, que
   el motor dels PNG necessita. Torna [amplada, alçada] del viewBox. */
const FITXA = fs.readFileSync(path.join(__dirname, "..", "..", "fitxes", "ud6.html"), "utf8");
function deFitxa(nom) {
  const m = FITXA.match(new RegExp(`<!--grafic:${nom}--><svg viewBox="0 0 ([\\d.]+) ([\\d.]+)"[^>]*>([\\s\\S]*?)</svg><!--/grafic-->`));
  if (!m) throw new Error(`ud6.js: el gràfic ${nom} no és a fitxes/ud6.html`);
  X.registra(nom, X.SVG(`0 0 ${m[1]} ${m[2]}`, +m[1], +m[2], m[3]));
  return [+m[1], +m[2]];
}
const MIDES = Object.fromEntries(["DOT_A", "DOT_B", "TRANSPORT", "ENGANY_0", "ENGANY_90"].map(n => [n, deFitxa(n)]));
const una = (nom, cm, alt) => () => X.par(X.imatge(nom, cm, cm * MIDES[nom][1] / MIDES[nom][0], alt),
                                          { alignment: AlignmentType.CENTER, keepNext: true });
function duo(a, b, cm, alts) {
  return () => {
    const w = Math.floor(X.AMPLE / 2);
    const cel = (nom, alt) => X.cela(X.par(X.imatge(nom, cm, cm * MIDES[nom][1] / MIDES[nom][0], alt),
                                           { alignment: AlignmentType.CENTER, keepNext: true }), { w });
    return X.taula([w, X.AMPLE - w], [new TableRow({ cantSplit: true, children: [cel(a, alts[0]), cel(b, alts[1])] })]);
  };
}

/* ------------------------------------------------------------ les dades -- */
const GOLS = [2, 0, 3, 2, 1, 0, 2, 3, 1, 2];
const vegades = v => GOLS.filter(g => g === v).length;
const ORD = [...GOLS].sort((a, b) => a - b);
cal(ORD.join(" ") === "0 0 1 1 2 2 2 2 3 3", "les dades ordenades");
cal(GOLS.reduce((a, b) => a + b, 0) === 16, "la suma");
const PESOS = [["Projecte", 9, 0.5], ["Prova", 4, 0.3], ["Feina diària", 6, 0.2]];
const FINAL = PESOS.reduce((s, [, n, p]) => s + n * p, 0);
cal(Math.abs(FINAL - 6.9) < 1e-9, "la nota final");
const BUS = [8, 9, 8, 10, 30], CAMI = [12, 13, 12, 14, 13];
const mediana = l => [...l].sort((a, b) => a - b)[Math.floor(l.length / 2)];
const mitjana = l => l.reduce((a, b) => a + b, 0) / l.length;
cal(mediana(BUS) === 9 && mediana(CAMI) === 13 && mitjana(BUS) === 13 && Math.abs(mitjana(CAMI) - 12.8) < 1e-9, "bus i camí");

/* ------------------------------------------------------------- l'alumnat -- */
const alumnat = [
  ...X.exercici(1, "Completa la taula de vegades.", {}, [
    X.context("Gols d'un equip en 10 partits:  " + GOLS.join("   ")),
    X.taulaResposta([10, 20, 40, 30], ["", "Gols", "Compte", "Vegades"], [
      ["a)", ms("0"), ms("| |"), ms("2")],
      ["b)", dada("1"), "", ""],
      ["c)", dada("2"), "", ""],
      ["d)", dada("3"), "", ""],
    ]),
  ]),

  ...X.exercici(2, "Amb les mateixes dades, calcula les mesures.", { calc: true }, [
    X.context("Ordenades:  " + ORD.join("   ")),
    X.taulaResposta([10, 30, 34, 26], ["", "Mesura", "Com es fa", "Val"], [
      ["a)", ms("Mitjana"), ms("16 ÷ 10"), ms("1,6")],
      ["b)", dada("Mediana"), dada("la del mig"), ""],
      ["c)", dada("Moda"), dada("la que surt més"), ""],
      ["d)", dada("La més petita i la més gran"), dada("mira els extrems"), ""],     // nou
    ]),
  ]),

  ...X.exercici(3, "Calcula la nota final amb els pesos.", { calc: true }, [
    X.taulaResposta([10, 30, 18, 18, 24], ["", "Part", "Nota", "Pes", "Nota × pes"], [
      ["a)", ms("Projecte"), ms("9"), ms("0,5"), ms("4,5")],
      ["b)", dada("Prova"), dada("4"), dada("0,3"), ""],
      ["c)", dada("Feina diària"), dada("6"), dada("0,2"), ""],
      ["d)", dada("Nota final: suma"), "", "", ""],
    ]),
  ]),

  ...X.exercici(4, "Mira els dos gràfics i contesta.", {}, [
    X.context("Dues jugadores de bàsquet. Punts de cada partit."),
    una("DOT_A", 12, "Punts de la jugadora A: 4, 5, 5, 5, 5 i 6"),
    una("DOT_B", 12, "Punts de la jugadora B: 1, 3, 5, 5, 7 i 9"),
    () => X.espai(10, { keepNext: true }),
    X.taulaResposta([10, 60, 30], ["", "Pregunta", "Resposta"], [
      ["a)", ms("Quina mitjana té la jugadora A?", undefined, { esq: true }), ms("5")],
      ["b)", txt("I la jugadora B?"), ""],
      ["c)", txt("Quina té les dades més escampades?"), ""],
      ["d)", txt("Quina fa sempre més o menys el mateix?"), ""],
    ]),
  ]),

  ...X.exercici(5, "Llegeix el gràfic i contesta.", {}, [
    una("TRANSPORT", 12.5, "Gràfic de barres: a peu 12, bus 9, cotxe 5, bici 4"),
    () => X.espai(10, { keepNext: true }),
    X.taulaResposta([10, 60, 30], ["", "Pregunta", "Resposta"], [
      ["a)", ms("Quants van a peu?", undefined, { esq: true }), ms("12")],
      ["b)", txt("Quants van en bici?"), ""],
      ["c)", txt("Quin és el mitjà més usat?"), ""],
      ["d)", txt("Quants alumnes hi ha en total?"), ""],
    ]),
  ]),

  ...X.exercici(6, "Els dos gràfics tenen les mateixes dades. Contesta.", {}, [
    X.context("Ampolles venudes de dues marques."),
    duo("ENGANY_0", "ENGANY_90", 7.5, ["Gràfic 1: les barres comencen al 0", "Gràfic 2: les barres comencen al 90"]),
    () => X.espai(10, { keepNext: true }),
    X.taulaResposta([10, 60, 30], ["", "Pregunta", "Resposta"], [
      ["a)", ms("A quin gràfic sembla que B ven molt més?", undefined, { esq: true }), ms("al 2")],
      ["b)", txt("Quantes en ven la marca A?"), ""],
      ["c)", txt("Quantes en ven la marca B?"), ""],
      ["d)", txt("On comença la línia de baix del gràfic 2?"), ""],
    ]),
  ]),

  ...X.exercici(7, "Decideix quin número explica millor cada llista.", { calc: true }, [
    X.context("El bus: minuts d'espera, 5 dies:  " + BUS.join(" · ")),
    X.context("El camí: minuts fins a l'institut, 5 dies:  " + CAMI.join(" · ")),
    X.taulaResposta([8, 44, 24, 24], ["", "Pregunta", "El bus", "El camí"], [
      ["a)", ms("Mitjana", undefined, { esq: true }), ms("65 ÷ 5 = 13"), ms("64 ÷ 5 = 12,8")],
      ["b)", txt("Mediana"), "", ""],
      ["c)", txt("Les dades estan juntes o escampades?"), "", ""],
      ["d)", txt("Què ho explica millor: mitjana o mediana?"), "", ""],
    ]),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const LET = ["a) resolt", "b)", "c)", "d)"];
const solucionari = privat => [
  ...sol.titol(6),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Fita d'assoliment esperada: *AS* sòlid, amb *AN* a la representació (criteris 5.1 i 2.1). Calculadora disponible a tot l'examen.`,
    "*Com s'ha construït:* a cada exercici, l'apartat a) resolt com a model i tres apartats per fer, amb els ítems i els gràfics de la fitxa (_fitxes/ud6.html_) i del seu solucionari. Sense les preguntes obertes de la fitxa (3e, 4e, 6f i 7e). Els apartats marcats «nou» no són a la fitxa: revisa'ls abans de fer servir l'examen.",
    "*La dispersió, com a idea visual:* «juntes» o «escampades». No es demana cap fórmula de dispersió.",
  ]),

  sol.h3("1. La taula de vegades — criteri 2.1"),
  ...sol.taula([19, 20, 36, 25], [["", "Gols", "Compte", "Vegades"]].concat(
    [0, 1, 2, 3].map((v, i) => [LET[i], String(v), "| ".repeat(vegades(v)).trim(), `*${vegades(v)}*`]))),
  sol.p("Les vegades han de sumar 10, el nombre de partits. Si no, hi ha un error de recompte."),

  sol.h3("2. Les mesures — criteri 5.1"),
  ...sol.taula([19, 30, 31, 20], [
    ["", "Mesura", "Com es fa", "Val"],
    ["a) resolt", "Mitjana", "16 ÷ 10", "1,6"],
    ["b)", "Mediana", "10 dades: les dues del mig són 2 i 2", "*2*"],
    ["c)", "Moda", "el 2 surt 4 vegades", "*2*"],
    ["d) nou", "La més petita i la més gran", "els extrems de la llista ordenada", "*0 i 3*"],
  ]),
  sol.p("*Atenció a la mediana:* amb 10 dades no n'hi ha una sola del mig. Aquí les dues centrals són 2, i la resposta surt neta."),

  sol.h3("3. La nota amb pesos — criteri 5.1"),
  ...sol.taula([19, 27, 16, 16, 22], [["", "Part", "Nota", "Pes", "Nota × pes"]].concat(
    PESOS.map(([p, n, w], i) => [LET[i], p, String(n), f(w), `*${f(n * w)}*`]),
    [["d)", "Nota final", "", "", `*${f(FINAL)}*`]])),
  sol.p("*Error típic:* sumar les tres notes i dividir entre 3 (19 ÷ 3 = 6,3). És el reflex de la mitjana normal. Si passa, torneu a la pàgina 4 de la fitxa: el rectangle del projecte ocupa la meitat del total."),

  sol.h3("4. Les dues jugadores — criteri 5.1"),
  ...sol.taula([19, 51, 30], [
    ["", "Pregunta", "Resposta"],
    ["a) resolt", "Mitjana de A", "5"],
    ["b)", "Mitjana de B", "*5, la mateixa*"],
    ["c)", "Més escampades", "*la B* (va de 1 a 9)"],
    ["d)", "Sempre igual", "*la A* (va de 4 a 6)"],
  ]),

  sol.h3("5. El gràfic de barres — criteri 2.1"),
  ...sol.taula([19, 51, 30], [
    ["", "Pregunta", "Resposta"],
    ["a) resolt", "A peu", "12"],
    ["b)", "En bici", "*4*"],
    ["c)", "El més usat", "*a peu*"],
    ["d)", "Total", "*12 + 9 + 5 + 4 = 30*"],
  ]),

  sol.h3("6. El gràfic enganyós — criteri 2.1"),
  ...sol.taula([19, 51, 30], [
    ["", "Pregunta", "Resposta"],
    ["a) resolt", "On sembla que B ven molt més", "al gràfic 2"],
    ["b)", "Ven la marca A", "*95*"],
    ["c)", "Ven la marca B", "*100*"],
    ["d)", "On comença el gràfic 2", "*al 90, no al 0*"],
  ]),
  sol.p("*És la regla trencada de la unitat* i l'exercici més valuós fora de l'aula. La diferència real és de 5 ampolles, però al gràfic 2 la barra de B sembla molt més del doble. Si ho vol dir de paraula, assolit amb «no comença a zero». Compta per als nivells alts (AN, AE)."),

  sol.h3("7. Quin número ho explica millor — criteri 5.1"),
  ...sol.taula([19, 37, 22, 22], [
    ["", "Pregunta", "El bus", "El camí"],
    ["a) resolt", "Mitjana", "65 ÷ 5 = 13", "64 ÷ 5 = 12,8"],
    ["b)", "Mediana", "*8 8 9 10 30 → 9*", "*12 12 13 13 14 → 13*"],
    ["c)", "Juntes o escampades", "*escampades*", "*juntes*"],
    ["d)", "Què ho explica millor", "*la mediana*", "*la mitjana*"],
  ]),
  sol.p("Això és el que mostra si ho ha entès: la resposta canvia d'una llista a l'altra. El dia dels 30 minuts s'endú la mitjana del bus cap amunt; la mediana (9) diu el que sol passar."),

  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Exercicis 1, 5 i 6 → criteri *2.1*, organitzar i llegir dades en taula i gràfic.",
    "Exercicis 2, 3, 4 i 7 → criteri *5.1*, resumir les dades i dir si estan juntes o escampades.",
    "El mínim (AS) és l'exercici 1, la mitjana i la moda de l'exercici 2 i l'exercici 5. L'exercici 6 i la columna del bus del 7 compten per als nivells alts.",
  ]),
];

X.genera({ unitat: 6, alumnat, solucionari }).catch(e => { console.error(e.message); process.exit(1); });
