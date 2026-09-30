#!/usr/bin/env node
/*
  1eso/generadors/examens/ud7.js · examen de la Unitat 7 (Llenguatge algebraic i patrons)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a comu/examens/nucli.js i les
  regles, a comu/docs/EXAMENS-DOCX.md.

      node 1eso/generadors/examens/ud7.js   →  1eso/docx/examen-ud7-alumnat.docx
                                                1eso/docx/examen-ud7-solucionari.docx

  D'on surt cada cosa:
  · L'ordre, el de les fitxes de la unitat: els patrons (el nombre següent i quant creix), la regla
    (la figura 10 i escriure-la), els símbols (traduir i calcular) i els gràfics de barres. La
    programació no porta examen; el llibre, a la UD8, sí.
  · Els apartats a), b), c) i d), de les fitxes (fitxes/ud7*.html) i dels seus solucionaris. L'únic
    que no hi és (exercici 2, d) porta la marca «nou» al solucionari. Les regles trencades de les
    fitxes són l'«error típic» dels apartats.
  · Sempre amb el punt (2 · n), sense equacions, i només gràfics de barres (el pla validat el
    29/9/2026). La targeta «Patrons i símbols» i la de les taules, al davant.
*/
"use strict";

const X = require("../../../comu/examens/nucli");
const { dada, ms, sol } = X;
const { AlignmentType } = X.docx;

const cal = (cond, msg) => { if (!cond) throw new Error("ud7.js: " + msg); };
const LET = ["a)", "b)", "c)", "d)"];

/* ------------------------------------------------------------ les dades -- */
const SEGUENT = [[3, 5, 7, 9], [4, 8, 12, 16], [6, 11, 16, 21], [80, 72, 64, 56]];
const pas = s => s[1] - s[0];
SEGUENT.concat([[2, 5, 8, 11], [10, 20, 30, 40], [7, 9, 11, 13], [50, 45, 40, 35]]).forEach(s =>
  cal(s.every((v, i) => i === 0 || v - s[i - 1] === pas(s)), `${s} no creix sempre igual`));
const CREIX = [[2, 5, 8, 11], [10, 20, 30, 40], [7, 9, 11, 13], [50, 45, 40, 35]];      // el d és nou
const signe = d => (d > 0 ? `+ ${d}` : `− ${-d}`);

// [a, b]: la regla a · n + b
const REGLES = [[2, 0], [3, 1], [1, 5], [5, 0]];
const regla = ([a, b]) => (a === 1 ? "n" : `${a} · n`) + (b ? ` + ${b}` : "");
const figura = ([a, b], n) => a * n + b;
REGLES.forEach(r => cal(figura(r, 10) <= 999 && r[0] <= 10, `${regla(r)} surt de la targeta`));
const ESCRIU = [[[3, 5, 7, 9], [2, 1]], [[4, 8, 12, 16], [4, 0]], [[6, 7, 8, 9], [1, 5]], [[5, 8, 11, 14], [3, 2]]];
ESCRIU.forEach(([s, r]) => cal(s.every((v, i) => v === figura(r, i + 1)), `la regla ${regla(r)} no fa ${s}`));

const SIMBOLS = [["El triple d'un nombre", "3 · n"], ["Un nombre menys 7", "n − 7"],
                 ["La meitat d'un nombre", "n : 2"], ["El següent d'un nombre", "n + 1"]];
const CALCULA = [["3 · n", n => 3 * n], ["n + 12", n => n + 12], ["2 · n + 5", n => 2 * n + 5], ["10 · n", n => 10 * n]];
const N = 4;

/* ------------------------------------------------------ el gràfic de barres -- */
const INSTITUT = [["A peu", 12], ["Bus", 8], ["Bici", 6], ["Cotxe", 4]];
const graficSvg = () => {
  const m = 14, x0 = 44, y0 = 220, amp = 70, max = 12;
  let s = "";
  for (let v = 0; v <= max; v += 2) {
    s += `<line x1="${x0}" y1="${y0 - v * m}" x2="${x0 + INSTITUT.length * amp}" y2="${y0 - v * m}" stroke="#8A8A8A" stroke-width="1"/>`;
    s += `<text x="${x0 - 8}" y="${y0 - v * m + 5}" font-size="14" text-anchor="end" fill="#333">${v}</text>`;
  }
  s += `<line x1="${x0}" y1="${y0}" x2="${x0}" y2="${y0 - max * m - 6}" stroke="#333" stroke-width="2.5"/>`;
  s += `<line x1="${x0}" y1="${y0}" x2="${x0 + INSTITUT.length * amp}" y2="${y0}" stroke="#333" stroke-width="2.5"/>`;
  INSTITUT.forEach(([et, v], i) => {
    const x = x0 + i * amp + (amp - m) / 2;
    for (let k = 0; k < v; k++) s += `<rect x="${x}" y="${y0 - (k + 1) * m}" width="${m}" height="${m}" fill="#D4D4D4" stroke="#333" stroke-width="1.4"/>`;
    s += `<text x="${x0 + i * amp + amp / 2}" y="${y0 + 22}" font-size="15" font-weight="700" text-anchor="middle" fill="#000">${et}</text>`;
  });
  return X.SVG(`0 0 ${x0 + INSTITUT.length * amp + 10} ${y0 + 32}`, x0 + INSTITUT.length * amp + 10, y0 + 32, s);
};
X.registra("grafic_institut", graficSvg());
// L'amplada i l'alçada, a la proporció del dibuix (334 per 252).
const grafic = (cm = 13) => () => X.par(X.imatge("grafic_institut", cm, Math.round(cm * 252 / 334 * 10) / 10,
  "Gràfic de barres, com venim a l'institut: a peu 12, bus 8, bici 6, cotxe 4"), { alignment: AlignmentType.CENTER });
const valor = et => INSTITUT.find(x => x[0] === et)[1];
const DIFS = [["A peu", "Bus"], ["Bus", "Cotxe"], ["Bici", "Cotxe"], ["A peu", "Cotxe"]];

/* ------------------------------------------------------------ l'alumnat -- */
const alumnat = [
  ...X.exercici(1, "Escriu el nombre següent del patró.", {}, [
    X.context("Mira quant creix cada vegada."),
    X.taulaResposta([10, 50, 40], ["", "El patró", "El següent"], SEGUENT.map((s, i) =>
      [LET[i], dada(s.join(", ")), i === 0 ? ms(String(s[3] + pas(s))) : ""])),
  ]),

  ...X.exercici(2, "Quant creix o decreix cada vegada?", { mateixaPagina: true }, [
    X.context("Escriu + 3 si se suma 3, o − 3 si es resta 3."),
    X.taulaResposta([10, 50, 40], ["", "El patró", "Cada vegada"], CREIX.map((s, i) =>
      [LET[i], dada(s.join(", ")), i === 0 ? ms(signe(pas(s))) : ""])),
  ]),

  ...X.exercici(3, "Fes servir la regla. Quants quadrets té la figura 10?", {}, [
    X.context("Posa el 10 on hi ha la n. Primer multiplica, després suma."),
    X.taulaResposta([10, 40, 50], ["", "La regla", "La figura 10"], REGLES.map((r, i) =>
      [LET[i], dada(regla(r)), i === 0 ? ms(`${regla(r).replace("n", "10")} = ${figura(r, 10)}`) : ""])),
  ]),

  ...X.exercici(4, "Escriu la regla del patró.", { mateixaPagina: true }, [
    X.context("El que creix va davant de la n. El que és fix va al final. Comprova la regla amb la figura 1."),
    X.taulaResposta([10, 50, 40], ["", "El patró", "La regla"], ESCRIU.map(([s, r], i) =>
      [LET[i], dada(s.join(", ")), i === 0 ? ms(regla(r)) : ""])),
  ]),

  ...X.exercici(5, "Escriu el símbol. Fes servir la lletra n.", {}, [
    X.context("Mira la targeta. El punt vol dir multiplicar."),
    X.taulaResposta([10, 55, 35], ["", "La frase", "El símbol"], SIMBOLS.map(([f, s], i) =>
      [LET[i], dada(f), i === 0 ? ms(s) : ""])),
  ]),

  ...X.exercici(6, `Calcula. La n val ${N}.`, { mateixaPagina: true }, [
    X.context(`Posa el ${N} on hi ha la n.`),
    X.taulaResposta([10, 40, 50], ["", "El símbol", "El càlcul"], CALCULA.map(([s, fn], i) =>
      [LET[i], dada(s), i === 0 ? ms(`${s.replace("n", String(N))} = ${fn(N)}`) : ""])),
  ]),

  ...X.exercici(7, "Mira el gràfic. Quants alumnes venen de cada manera?", {}, [
    X.context("Com venim a l'institut. Cada quadret és una persona."),
    grafic(13),
    X.taulaResposta([10, 50, 40], ["", "Com venen", "Quants alumnes"], INSTITUT.map(([et, v], i) =>
      [LET[i], dada(et), i === 0 ? ms(String(v)) : ""])),
  ]),

  ...X.exercici(8, "Quants alumnes més? Mira el gràfic.", {}, [
    X.context("Resta els dos nombres."),
    grafic(10),
    X.taulaResposta([10, 50, 40], ["", "Les dues barres", "Quants més"], DIFS.map(([a, b], i) =>
      [LET[i], dada(`${a} i ${b.toLowerCase()}`), i === 0 ? ms(`${valor(a)} − ${valor(b)} = ${valor(a) - valor(b)}`) : ""])),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const TRAS = { spacing: { before: X.tw(5), after: X.tw(8) } };
const resta = (c, f) => c.slice(1).map((x, i) => f(x, LET[i + 1])).join("; ");

const solucionari = privat => [
  ...sol.titol(7),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Sense calculadora: la *targeta «Patrons i símbols»* i la *targeta de les taules* són al davant tota l'estona.`,
    "*Com s'ha construït:* en l'ordre de les fitxes de la unitat (els patrons, la regla, els símbols i els gràfics), dos exercicis per part. A cada exercici, l'apartat a) resolt com a model i tres per fer, amb els ítems de les fitxes i del llibre. L'únic apartat marcat «nou» és el 2 d), revisat el 30/9/2026.",
    "*Queda fora, com a les fitxes:* les equacions, Fibonacci, els gràfics de línia i els termes com n². El producte s'escriu sempre amb el punt: 2 · n.",
    "*Si cal, en dues sessions:* els exercicis 1 a 4 (els patrons) i els 5 a 8 (els símbols i els gràfics).",
  ]),
  sol.h3("1. El nombre següent"),
  sol.p(`${resta(SEGUENT, (s, l) => `${l} *${s[3] + pas(s)}*`)}. *Error típic:* multiplicar per 2 en lloc de sumar sempre el mateix, com en Pau de la fitxa 1.`, TRAS),
  sol.h3("2. Quant creix · la d, nova"),
  sol.p(`${resta(CREIX, (s, l) => `${l} *${signe(pas(s))}*`)}. La d) és nova (decreix de 5 en 5), revisada el 30/9/2026: com la d) de l'exercici 1, que també baixa.`, TRAS),
  sol.h3("3. La figura 10"),
  sol.p(`${resta(REGLES, (r, l) => `${l} ${regla(r).replace("n", "10")} = *${figura(r, 10)}*`)}. *Error típic:* sumar abans de multiplicar.`, TRAS),
  sol.h3("4. La regla"),
  sol.p(`${resta(ESCRIU, ([, r], l) => `${l} *${regla(r)}*`)}. *Error típic:* oblidar la part fixa (3 · n per a 5, 8, 11, 14), com la Ivet de la fitxa 2: la regla es comprova amb la figura 1.`, TRAS),
  sol.h3("5. El símbol"),
  sol.p(`${resta(SIMBOLS, ([, s], l) => `${l} *${s}*`)}. Són els casos del llibre.`, TRAS),
  sol.h3("6. Calcula"),
  sol.p(`${resta(CALCULA, ([s, fn], l) => `${l} ${s.replace("n", String(N))} = *${fn(N)}*`)}. *Error típic:* posar el nombre al costat (3 · n amb n = 4, 34), com la Zoe de la fitxa 3.`, TRAS),
  sol.h3("7. El gràfic"),
  sol.p(`${resta(INSTITUT, ([et, v], l) => `${l} ${et}: *${v}*`)}. És l'enquesta del llibre. *Error típic:* llegir la ratlla de sobre o la de sota.`, TRAS),
  sol.h3("8. Quants més"),
  sol.p(`${resta(DIFS, ([a, b], l) => `${l} ${valor(a)} − ${valor(b)} = *${valor(a) - valor(b)}*`)}.`, TRAS),
  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Exercicis 1 i 2 → continua un patró i diu quant creix.",
    "Exercicis 3 i 4 → fa servir una regla i l'escriu, amb la part fixa.",
    "Exercicis 5 i 6 → escriu una frase amb símbols i la calcula per a un valor.",
    "Exercicis 7 i 8 → llegeix un gràfic de barres i compara dues barres.",
  ]),
  sol.p("Els criteris de la SA del grup (2.1, 3.1, 4.1, 5.1 i 7.2) són de referència: l'avaluació es fa amb els criteris del PI. Una explicació oral registrada en el moment, «El meu patró» o el codi d'una tasca tancada de la caixa d'eines valen igual que l'examen escrit."),
];

X.genera({
  unitat: 7, alumnat, solucionari,
  materia: "Matemàtiques",
  creador: "Matemàtiques",
  avis: { text: "Pots fer servir les dues targetes a tot l'examen: la de les taules i la dels patrons i els símbols.", icona: "targeta" },
}).catch(e => { console.error(e.message); process.exit(1); });
