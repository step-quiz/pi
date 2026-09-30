#!/usr/bin/env node
/*
  4eso/generadors/examens/ud3.js · examen de la Unitat 3 (Proporcionalitat i escales)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a comu/examens/nucli.js i les
  regles, a comu/docs/EXAMENS-DOCX.md. El model és ud1.js.

      node 4eso/generadors/examens/ud3.js   →  4eso/docx/examen-ud3-alumnat.docx
                                                4eso/docx/examen-ud3-solucionari.docx

  D'on surt cada cosa:
  · Els apartats a), b), c) i d), dels exercicis de fitxes/ud3.html i del seu solucionari.
    On la fitxa no en tenia prou, n'hi ha un de nou, i al solucionari porta la marca «nou».
  · Sense la pregunta oberta de la fitxa (5e, encerclar al plànol) ni els dibuixos: el plànol
    i la doble recta del mapa són a la fitxa, i l'examen en fa servir només les mides.
  · La regla trencada de la fitxa (6c, l'ampolla petita que guanya la garrafa) hi és, com a
    apartat c) de l'exercici 6.
  Proposta del 30/9/2026, per validar amb el docent.
*/
"use strict";

const X = require("../../../comu/examens/nucli");
const { dada, ms, sol } = X;

const cal = (cond, msg) => { if (!cond) throw new Error("ud3.js: " + msg); };
const f = (x, d = 2) => String(Math.round(x * 10 ** d) / 10 ** d).replace(".", ",");
const e2 = x => x.toFixed(2).replace(".", ",") + " €";
const nb = s => s.replace(/(\d) (?=cm|m\b|€|%|g\b|L\b|kg\b)/g, "$1 ").replace(/(\d) × (?=\d)/g, "$1 × ");
const txt = s => dada(nb(s), undefined, { esq: true });
const esc = e => "1 : " + e.toLocaleString("ca-ES").replace(/\./g, " ");

/* ------------------------------------------------------------ les dades -- */
const UN_CM = [100, 50, 200, 500];
const VERITAT = [[100, 6], [100, 9.5], [50, 8], [200, 7]];           // [escala, cm al plànol]
const PLANOL = [[200, 8], [100, 5], [50, 3], [500, 45]];             // [escala, m de veritat]
const DI = [["Més quilos de pomes, més diners.", "Directa"], ["Més pintors, menys dies per pintar.", "Inversa"],
            ["Més hores de feina, més sou.", "Directa"], ["Més amics per repartir un pastís, menys tros per a cadascú.", "Inversa"]];
const PIS = [["Menjador", 5, 4], ["Habitació", 4, 3], ["Bany", 2, 2], ["Cuina", 3, 2.5]];
// [producte, frase, preu petit, quantitat petita, preu gran, quantitat gran, unitat]
const OFERTES = [["Llet", "Ampolla d'1 L per 0,90 €. Pack de 6 L per 5,10 €.", 0.9, 1, 5.1, 6, "L"],
                 ["Arròs", "Paquet d'1 kg per 1,80 €. Sac de 5 kg per 8,50 €.", 1.8, 1, 8.5, 5, "kg"],
                 ["Aigua", "Ampolla d'1,5 L per 0,60 €. Garrafa de 8 L per 3,60 €.", 0.6, 1.5, 3.6, 8, "L"],
                 ["Oli", "Ampolla d'1 L per 4,50 €. Garrafa de 3 L per 12,90 €.", 4.5, 1, 12.9, 3, "L"]];    // el d és nou
const guanyaGran = o => o[4] / o[5] < o[2] / o[3];
cal(OFERTES.map(guanyaGran).join() === "true,true,false,true", "l'apartat c ha de trencar la regla");
const MAPA = [["De casa a l'institut", 6], ["De casa al poliesportiu", 9], ["De casa a la parada del bus", 3.5],
              ["De casa al mercat", 4.5]];                                                          // el d és nou
cal(350 / 50 === 7, "la recepta");

/* ------------------------------------------------------------- l'alumnat -- */
const alumnat = [
  ...X.exercici(1, "Escriu quant val un centímetre del plànol a cada escala.", {}, [
    X.taulaResposta([12, 28, 30, 30], ["", "Escala", "1 cm són… (cm)", "és a dir (m)"], [
      ["a)", ms(esc(100)), ms("100 cm"), ms("1 m")],
      ...UN_CM.slice(1).map((e, i) => [["b)", "c)", "d)"][i], dada(esc(e)), "", ""]),
    ]),
  ]),

  ...X.exercici(2, "Calcula quant mesura de veritat.", { calc: true }, [
    X.taulaResposta([10, 20, 20, 25, 25], ["", "Escala", "Al plànol", "× escala", "De veritat"], [
      ["a)", ms(esc(100)), ms("6 cm"), ms("600 cm"), ms("6 m")],
      ...VERITAT.slice(1).map(([e, c], i) => [["b)", "c)", "d)"][i], dada(esc(e)), dada(nb(`${f(c)} cm`)), "", ""]),
    ]),
  ]),

  ...X.exercici(3, "Calcula quant ha de mesurar al plànol.", { calc: true }, [
    X.taulaResposta([10, 20, 20, 25, 25], ["", "Escala", "De veritat", "× 100", "Al plànol"], [
      ["a)", ms(esc(200)), ms("8 m"), ms("800 cm"), ms("4 cm")],
      ...PLANOL.slice(1).map(([e, m], i) => [["b)", "c)", "d)"][i], dada(esc(e)), dada(nb(`${m} m`)), "", ""]),
    ]),
  ]),

  ...X.exercici(4, "Escriu si és proporcionalitat directa o inversa.", {}, [
    X.context("Digues la frase en veu alta: «més… i més…» o «més… i menys…»."),
    X.taulaResposta([10, 60, 30], ["", "Situació", "Directa o inversa?"], [
      ["a)", ms(DI[0][0], undefined, { esq: true }), ms("Directa")],
      ...DI.slice(1).map(([s], i) => [["b)", "c)", "d)"][i], txt(s), ""]),
    ]),
  ]),

  ...X.exercici(5, "Calcula les mides de veritat de cada espai.", {}, [
    X.context("Plànol d'un pis a escala 1 : 100."),
    X.taulaResposta([10, 30, 30, 30], ["", "Espai", "Al plànol", "De veritat"], [
      ["a)", ms("Menjador"), ms(nb("5 × 4 cm")), ms(nb("5 × 4 m"))],
      ...PIS.slice(1).map(([n, a, b], i) => [["b)", "c)", "d)"][i], dada(n), dada(nb(`${f(a)} × ${f(b)} cm`)), ""]),
    ]),
  ]),

  ...X.exercici(6, "Escriu quina oferta surt més a compte.", { calc: true }, [
    X.context("Primer baixa a una unitat: preu ÷ quantitat. Després compara."),
    X.taulaResposta([8, 38, 18, 18, 18], ["", "Oferta", "Petit: preu d'1", "Gran: preu d'1", "Guanya"], [
      ["a)", ms(nb(OFERTES[0][1]), undefined, { esq: true }), ms(nb("0,90 €")), ms(nb("0,85 €")), ms("El pack")],
      ...OFERTES.slice(1).map((o, i) => [["b)", "c)", "d)"][i], txt(o[1]), "", "", ""]),
    ]),
  ]),

  ...X.exercici(7, "Calcula les distàncies de veritat al mapa.", { calc: true }, [
    X.context("Al mapa del barri, 1 cm són 50 m de veritat."),
    X.taulaResposta([10, 50, 20, 20], ["", "Recorregut", "Al mapa", "De veritat"], [
      ["a)", ms(MAPA[0][0], undefined, { esq: true }), ms("6 cm"), ms("300 m")],
      ...MAPA.slice(1).map(([r, c], i) => [["b)", "c)", "d)"][i], txt(r), dada(nb(`${f(c)} cm`)), ""]),
    ]),
  ]),

  ...X.exercici(8, "Baixa a una persona i després calcula.", { calc: true }, [
    X.context("Una recepta de creps per a 4 persones porta 200 g de farina."),
    X.taulaResposta([10, 60, 30], ["", "Pregunta", "Resposta"], [
      ["a)", ms("Quanta farina cal per a 1 persona?", undefined, { esq: true }), ms(nb("200 ÷ 4 = 50 g"))],
      ["b)", txt("I per a 10 persones?"), ""],
      ["c)", txt("Amb 350 g, per a quantes persones n'hi ha prou?"), ""],
      ["d)", txt("Més persones, més farina. És directa o inversa?"), ""],
    ]),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const LET = ["a) resolt", "b)", "c)", "d)"];
const solucionari = privat => [
  ...sol.titol(3),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Fita d'assoliment esperada: *AS* al criteri 1.1, amb *AN* a la part d'escales. Calculadora disponible a tot l'examen.`,
    "*Com s'ha construït:* a cada exercici, l'apartat a) resolt com a model i tres apartats per fer, amb els ítems de la fitxa (_fitxes/ud3.html_) i del seu solucionari. Sense la pregunta oberta de la fitxa (5e). Els apartats marcats «nou» no són a la fitxa: revisa'ls abans de fer servir l'examen.",
    "*Dues valoracions separades:* puntua per separat si la *decisió* és correcta i si el *càlcul* és correcte. Un error aritmètic no hauria de fer baixar la valoració de la decisió.",
  ]),

  sol.h3("1. Quant val 1 cm del plànol"),
  ...sol.taula([19, 27, 27, 27], [["", "Escala", "1 cm són… (cm)", "és a dir (m)"]].concat(
    UN_CM.map((e, i) => [LET[i], esc(e), `${e} cm`, `${f(e / 100)} m`]))),
  sol.p("*Error típic:* a l'apartat b, dir que 50 cm són 5 m. Si passa, val la pena tornar a la relació 100 cm = 1 m."),

  sol.h3("2. Quant mesura de veritat — criteri 1.1"),
  ...sol.taula([19, 20, 20, 20, 21], [["", "Escala", "Al plànol", "× escala", "De veritat"]].concat(
    VERITAT.map(([e, c], i) => [LET[i], esc(e), `${f(c)} cm`, `${f(c * e)} cm`, `*${f(c * e / 100)} m*`]))),

  sol.h3("3. Quant ha de mesurar al plànol — criteri 1.1"),
  ...sol.taula([19, 20, 20, 20, 21], [["", "Escala", "De veritat", "× 100", "Al plànol"]].concat(
    PLANOL.map(([e, m], i) => [LET[i], esc(e), `${m} m`, `${f(m * 100)} cm`, `*${f(m * 100 / e)} cm*`]))),
  sol.p("*Atenció a l'apartat c:* a escala 1 : 50 el dibuix surt més gran que a 1 : 100. 3 m fan 6 cm, no 3 cm."),

  sol.h3("4. Directa o inversa — criteri 1.1"),
  sol.p(DI.map(([, r], i) => `${"abcd"[i]}) *${r}*`).join("  ·  "), { spacing: { before: X.tw(5), after: X.tw(8) } }),
  sol.p("Si dubta, que digui en veu alta les dues meitats de la frase. La paraula «menys» ja li dona la resposta."),

  sol.h3("5. El pis a escala 1 : 100"),
  ...sol.taula([19, 27, 27, 27], [["", "Espai", "Al plànol", "De veritat"]].concat(
    PIS.map(([n, a, b], i) => [LET[i], n, `${f(a)} × ${f(b)} cm`, `*${f(a)} × ${f(b)} m*`]))),
  sol.p("A escala 1 : 100, els centímetres del plànol són els metres de veritat. Si ho veu, no cal cap càlcul."),

  sol.h3("6. Quina oferta surt més a compte — criteri 1.1"),
  ...sol.taula([13, 16, 25, 25, 21], [["", "Producte", "Petit: preu d'1", "Gran: preu d'1", "Guanya"]].concat(
    OFERTES.map((o, i) => [(i === 3 ? "d) nou" : LET[i]), o[0],
      `${e2(o[2]).slice(0, -2)} ÷ ${f(o[3])} = ${e2(o[2] / o[3])}/${o[6]}`, `${e2(o[4]).slice(0, -2)} ÷ ${o[5]} = ${e2(o[4] / o[5])}/${o[6]}`,
      `*${guanyaGran(o) ? "El gran" : "El petit"}*`]))),
  sol.p("*L'apartat c) és el més important de l'examen*, igual que el 5c de la Unitat 2. Als apartats a) i b) guanya el format gran, i l'alumnat se'n fabrica la regla «com més gran, més barat». Al c), l'ampolla petita surt millor. Si tria la garrafa sense dividir, és que recorda en lloc de calcular. Compta per als nivells alts (AN, AE), no per al mínim."),

  sol.h3("7. Les distàncies del mapa — criteri 1.1"),
  ...sol.taula([13, 45, 20, 22], [["", "Recorregut", "Al mapa", "De veritat"]].concat(
    MAPA.map(([r, c], i) => [(i === 3 ? "d) nou" : LET[i]), r, `${f(c)} cm`, `${f(c)} × 50 = *${f(c * 50)} m*`]))),

  sol.h3("8. La recepta — criteri 1.1"),
  ...sol.taula([19, 51, 30], [
    ["", "Pregunta", "Resposta"],
    ["a) resolt", "Farina per a 1 persona", "200 ÷ 4 = 50 g"],
    ["b)", "Per a 10 persones", "10 × 50 = *500 g*"],
    ["c)", "Amb 350 g", "350 ÷ 50 = *7 persones*"],
    ["d)", "Directa o inversa", "*Directa*"],
  ]),
  sol.p("És el mateix moviment de l'exercici 6 (baixar a 1) en una altra situació: primer quant per a 1, després quant per a tots."),

  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Exercicis 1, 2, 3, 5 i 7 → llegir i fer servir una escala. És on pot arribar a *AN*.",
    "Exercicis 4, 6 i 8 → criteri *1.1*, decidir en una situació real.",
    "El mínim (AS) és fer bé els apartats b) dels exercicis 1, 2 i 3. L'apartat 6c compta per als nivells alts.",
  ]),
];

X.genera({ unitat: 3, alumnat, solucionari }).catch(e => { console.error(e.message); process.exit(1); });
