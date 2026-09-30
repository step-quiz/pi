#!/usr/bin/env node
/*
  1eso/generadors/examens/ud5.js · examen de la Unitat 5 (Decimals i arrel quadrada)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a comu/examens/nucli.js i les
  regles, a comu/docs/EXAMENS-DOCX.md.

      node 1eso/generadors/examens/ud5.js   →  1eso/docx/examen-ud5-alumnat.docx
                                                1eso/docx/examen-ud5-solucionari.docx

  D'on surt cada cosa:
  · L'ordre, el de l'examen del llibre del grup (activitat 8 de la unitat 5): el valor i l'ordre,
    arrodonir i truncar, sumar i restar, de fracció a decimal, l'arrel, un problema de diners i les
    rajoles. El valor i l'ordre van en dos exercicis (1 i 2), perquè cada exercici sigui d'un sol
    tipus: en surten vuit.
  · Els apartats a), b), c) i d), de les sis fitxes (fitxes/ud5*.html) i dels seus solucionaris.
    L'únic que no hi és (exercici 8, d) porta la marca «nou» al solucionari. Les regles trencades
    de les fitxes no són exercicis apart: són l'«error típic» dels apartats.
  · Fora, com a les fitxes: multiplicar i dividir decimals, les mil·lèsimes, els periòdics i
    aproximar arrels amb decimals (el pla validat el 29/9/2026).
  · Sense calculadora: la targeta «Decimals i arrels» i la de les taules al davant. Els decimals
    es calculen aquí en centèsimes enteres, i l'examen i el solucionari en surten: no poden
    discrepar. Fins a 9,99, amb dues xifres decimals; sumes i restes sense portar-ne; arrels fins
    al 100.
*/
"use strict";

const X = require("../../../comu/examens/nucli");
const { dada, ms, sol } = X;

/* --------------------------------------------------- la calculadora, aquí -- */
const cal = (cond, msg) => { if (!cond) throw new Error("ud5.js: " + msg); };
const LET = ["a)", "b)", "c)", "d)"];
const xifres = c => [Math.floor(c / 100), Math.floor(c / 10) % 10, c % 10];
/** Les centèsimes com a decimal: 243 → «2,43»; 250 → «2,5»; amb x = 1 o 2, amb aquelles xifres. */
const dec = (c, x) => {
  const u = Math.floor(c / 100), r = c % 100;
  if (x === 2) return `${u},${String(r).padStart(2, "0")}`;
  if (x === 1) return `${u},${Math.floor(r / 10)}`;
  if (r === 0) return String(u);
  return `${u},${r % 10 === 0 ? r / 10 : String(r).padStart(2, "0")}`;
};
const dins = c => cal(c > 0 && c <= 999, `${dec(c)} surt del límit de 9,99`);

// Exercici 1 · el valor (fitxa 1): els blocs → el decimal
const BLOCS = [243, 150, 304, 75];
const nomBlocs = c => {
  const [u, d, q] = xifres(c), p = [];
  if (u) p.push(`${u} ${u === 1 ? "quadrat" : "quadrats"}`);
  if (d) p.push(`${d} ${d === 1 ? "columna" : "columnes"}`);
  if (q) p.push(`${q} ${q === 1 ? "quadret solt" : "quadrets solts"}`);
  return p.length > 1 ? p.slice(0, -1).join(", ") + " i " + p[p.length - 1] : p[0];
};
BLOCS.forEach(dins);

// Exercici 2 · l'ordre (fitxa 1, la regla trencada): [el gran, el petit]
const ORDRE = [[80, 75], [340, 304], [250, 245], [155, 150]];
ORDRE.forEach(([g, p]) => { dins(g); dins(p); cal(g > p, `${dec(g)} no és més gran que ${dec(p)}`); });

// Exercici 3 · arrodonir i truncar a les dècimes (fitxa 2)
const ARR = [586, 678, 342, 255];
const arrodonit = c => c - c % 10 + (c % 10 >= 5 ? 10 : 0);
const truncat = c => c - c % 10;
ARR.forEach(c => { dins(c); cal(c % 10 !== 0 && arrodonit(c) < 1000, `${dec(c)} no es pot arrodonir aquí`); });

// Exercici 4 · sumar i restar (fitxa 3): [a, b, resta?], sense portar-ne
const OPS = [[250, 135, false], [320, 145, false], [585, 230, true], [475, 150, true]];
const res = ([a, b, r]) => (r ? a - b : a + b);
OPS.forEach(([a, b, r]) => {
  const xa = xifres(a), xb = xifres(b);
  cal(r ? xa.every((v, i) => v >= xb[i]) : xa.every((v, i) => v + xb[i] <= 9), `${dec(a)} i ${dec(b)} porten`);
  dins(res([a, b, r]));
});
const opText = ([a, b, r], x) => `${dec(a, x)} ${r ? "−" : "+"} ${dec(b, x)}`;

// Exercici 5 · de la fracció al decimal (fitxa 4)
const FRAC = [[1, 4], [1, 2], [3, 4], [1, 5]];
const quadrets = ([n, d]) => { cal(100 % d === 0 && n < d, `${n}/${d} no fa quadrets sencers de 100`); return 100 / d * n; };

// Exercici 6 · l'arrel (fitxa 5): els tres primers exactes, el darrer entre dos nombres
const ARRELS = [16, 49, 81, 20];
const arrel = n => {
  cal(n >= 1 && n <= 100, `√${n} passa de la targeta`);
  const k = Math.floor(Math.sqrt(n));
  return k * k === n ? String(k) : `entre ${k} i ${k + 1}`;
};

// Exercici 7 · diners (fitxes 3 i 4): [frase, a, b, resta?]
const DINERS = [["Un entrepà de 2,50 € i un suc d'1,35 €", 250, 135, false],
                ["Una llibreta d'1,20 € i un llapis de 0,75 €", 120, 75, false],
                ["Tens 5,85 € i gastes 2,30 €", 585, 230, true],
                ["Tens 4,75 € i gastes 1,50 €", 475, 150, true]];
DINERS.forEach(([t, a, b, r]) => {
  cal(t.includes(dec(a, 2)) && t.includes(dec(b, 2)), `la frase «${t}» no porta ${dec(a, 2)} i ${dec(b, 2)}`);
  dins(res([a, b, r]));
});
const euros = c => `${dec(c, 2)} €`;

// Exercici 8 · les rajoles (fitxa 6): [llarg en m, ample en dècimes de metre]
const RAJ = [[5, 35], [4, 25], [6, 40], [3, 45]];           // el darrer és nou
const files = ample10 => Math.ceil(ample10 / 10);
RAJ.forEach(([l, a]) => cal(l <= 10 && files(a) <= 10, `${l} m per ${a / 10} m surt de la targeta`));
const metres = a10 => (a10 % 10 ? `${Math.floor(a10 / 10)},5 m` : `${a10 / 10} m`);

/* ------------------------------------------------------------ l'alumnat -- */
const alumnat = [
  ...X.exercici(1, "Escriu el decimal de cada dibuix de blocs.", {}, [
    X.context("El quadrat de 100 és 1. La columna és 0,1. El quadret solt és 0,01."),
    X.taulaResposta([10, 55, 35], ["", "Els blocs", "El decimal"], BLOCS.map((c, i) =>
      [LET[i], dada(nomBlocs(c)), i === 0 ? ms(dec(c)) : ""])),
  ]),

  ...X.exercici(2, "Escriu quin és el més gran.", { mateixaPagina: true }, [
    X.context("Escriu els dos amb dues xifres després de la coma: 0,8 és 0,80."),
    X.taulaResposta([10, 50, 40], ["", "Els dos decimals", "El més gran"], ORDRE.map(([g, p], i) => {
      const parella = i % 2 === 0 ? [g, p] : [p, g];
      return [LET[i], dada(`${dec(parella[0])} i ${dec(parella[1])}`), i === 0 ? ms(dec(g)) : ""];
    })),
  ]),

  ...X.exercici(3, "Arrodoneix i trunca a les dècimes.", {}, [
    X.context("Arrodonir: mira les centèsimes; 5 o més, amunt. Truncar: tallar i prou."),
    X.taulaResposta([10, 30, 30, 30], ["", "El decimal", "Arrodonit", "Truncat"], ARR.map((c, i) =>
      [LET[i], dada(dec(c)), i === 0 ? ms(dec(arrodonit(c), 1)) : "", i === 0 ? ms(dec(truncat(c), 1)) : ""])),
  ]),

  ...X.exercici(4, "Fes la suma o la resta amb la coma sota la coma.", { mateixaPagina: true }, [
    X.context("Si un nombre té una sola xifra després de la coma, afegeix un 0: 2,5 és 2,50."),
    X.taulaResposta([10, 45, 45], ["", "L'operació", "El resultat"], OPS.map((o, i) =>
      [LET[i], dada(opText(o)), i === 0 ? ms(`${opText(o, 2)} = ${dec(res(o), 2)}`) : ""])),
  ]),

  ...X.exercici(5, "Escriu el decimal de cada fracció.", {}, [
    X.context("Pensa en el quadrat de 100. Mira la targeta."),
    X.taulaResposta([10, 45, 45], ["", "La fracció", "El decimal"], FRAC.map((f, i) =>
      [LET[i], dada(`{${f[0]}/${f[1]}}`), i === 0 ? ms(dec(quadrets(f))) : ""])),
  ]),

  ...X.exercici(6, "Escriu l'arrel. Si no és a la targeta, escriu entre quins dos nombres és.", { mateixaPagina: true }, [
    X.context("L'arrel és el costat del quadrat: √16 = 4, perquè 4 · 4 = 16."),
    X.taulaResposta([10, 45, 45], ["", "L'arrel", "La resposta"], ARRELS.map((n, i) =>
      [LET[i], dada(`√${n}`), i === 0 ? ms(arrel(n)) : ""])),
  ]),

  ...X.exercici(7, "Quants diners són? Fes-ho amb la coma sota la coma.", {}, [
    X.context("Pagar dues coses és sumar. Gastar és restar."),
    X.taulaResposta([10, 55, 35], ["", "La situació", "Els diners"], DINERS.map(([t, a, b, r], i) =>
      [LET[i], dada(t), i === 0 ? ms(euros(res([a, b, r]))) : ""])),
  ]),

  ...X.exercici(8, "Quantes rajoles d'1 metre calen per fer el terra?", { mateixaPagina: true }, [
    X.context("Files per columnes. Si falta mig metre, cal una fila més de rajoles: es retallen."),
    X.taulaResposta([10, 45, 45], ["", "L'habitació", "Les rajoles"], RAJ.map(([l, a], i) =>
      [LET[i], dada(`${l} m per ${metres(a)}`), i === 0 ? ms(`${l} · ${files(a)} = ${l * files(a)} rajoles`) : ""])),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const TRAS = { spacing: { before: X.tw(5), after: X.tw(8) } };
const resta = (c, f) => c.slice(1).map((x, i) => f(x, LET[i + 1])).join("; ");

const solucionari = privat => [
  ...sol.titol(5),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Sense calculadora: la *targeta «Decimals i arrels»* i la *targeta de les taules* són al davant tota l'estona.`,
    "*Com s'ha construït:* en l'ordre de l'examen del llibre del grup (el valor i l'ordre, arrodonir i truncar, sumar i restar, de fracció a decimal, l'arrel, un problema de diners i les rajoles). El valor i l'ordre van en dos exercicis, perquè cada exercici sigui d'un sol tipus. A cada exercici, l'apartat a) resolt com a model i tres per fer, amb els ítems de les sis fitxes de la unitat. L'únic apartat marcat «nou» és el 8 d), revisat el 30/9/2026.",
    "*Queda fora, com a les fitxes:* multiplicar i dividir decimals, les mil·lèsimes, els decimals periòdics i aproximar una arrel amb decimals.",
    "*Si cal, en dues sessions:* els exercicis 1 a 4 (els decimals) i els 5 a 8 (fraccions, arrels i problemes).",
    "*Es pot dibuixar:* blocs, una recta o un quadrat de 100 al marge és una estratègia bona, no un error.",
  ]),

  sol.h3("1. El decimal dels blocs"),
  sol.p(`${resta(BLOCS, (c, l) => `${l} *${dec(c)}*`)}. *Error típic:* llegir els blocs sense coma, com a la unitat 1 (${BLOCS[2]}), o girar les columnes i els quadrets (3,4 per 3,04).`, TRAS),

  sol.h3("2. El més gran"),
  sol.p(`${resta(ORDRE, ([g], l) => `${l} *${dec(g)}*`)}. *Error típic:* triar el que té més xifres (0,75 davant de 0,8). És la regla trencada de la fitxa 1. L'apartat d) va a l'inrevés a posta: el més gran té més xifres.`, TRAS),

  sol.h3("3. Arrodonir i truncar"),
  sol.p(`${resta(ARR, (c, l) => `${l} ${dec(c)}: arrodonit *${dec(arrodonit(c), 1)}*, truncat *${dec(truncat(c), 1)}*`)}. *Error típic:* arrodonir sempre avall, que és truncar (6,78 → 6,7). És la regla trencada de la fitxa 2. A la c) tots dos donen el mateix; la d) és just a la ratlla del mig i va amunt.`, TRAS),

  sol.h3("4. Sumar i restar"),
  sol.p(`${resta(OPS, (o, l) => `${l} ${opText(o, 2)} = *${dec(res(o), 2)}*`)}. *Error típic:* posar les xifres a la dreta, sense mirar la coma (2,5 + 1,35 = 1,60). És la regla trencada de la fitxa 3. Cap operació no porta.`, TRAS),

  sol.h3("5. De la fracció al decimal"),
  sol.p(`${resta(FRAC, (f, l) => `${l} ${f[0]}/${f[1]} són ${quadrets(f)} quadrets de 100: *${dec(quadrets(f))}*`)}. *Error típic:* posar el de baix després de la coma (1/4 = 0,4). És la regla trencada de la fitxa 4.`, TRAS),

  sol.h3("6. L'arrel"),
  sol.p(`${resta(ARRELS, (n, l) => `${l} √${n}: *${arrel(n)}*`)}. *Error típic:* l'arrel com la meitat (√16 = 8). És la regla trencada de la fitxa 5. La d) no és a la targeta: 20 és entre 16 i 25.`, TRAS),

  sol.h3("7. Els diners"),
  sol.p(`${resta(DINERS, ([, a, b, r], l) => `${l} ${dec(a, 2)} ${r ? "−" : "+"} ${dec(b, 2)} = *${euros(res([a, b, r]))}*`)}. Són els casos de la fitxa 3. Els preus ja porten dues xifres després de la coma.`, TRAS),

  sol.h3("8. Les rajoles · la d, nova"),
  sol.p(`${resta(RAJ, ([l_, a], l) => `${l} ${files(a)} files: ${l_} · ${files(a)} = *${l_ * files(a)} rajoles*`)}. Quan l'amplada acaba en mig metre, cal una fila més de rajoles d'1 metre, que es retallen: es compta cap amunt. Les tres primeres són de la fitxa 6. La d) és nova (3 m per 4,5 m), revisada el 30/9/2026.`, TRAS),

  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Exercicis 1 i 2 → escriu el decimal dels blocs i compara dos decimals, igualant les xifres.",
    "Exercici 3 → arrodoneix i trunca a les dècimes.",
    "Exercici 4 → suma i resta decimals amb la coma sota la coma, sense portar-ne.",
    "Exercici 5 → passa una fracció de denominador 2, 4 o 5 a decimal.",
    "Exercici 6 → diu l'arrel d'un quadrat de la targeta, i entre quins dos nombres és una arrel que no és exacta.",
    "Exercicis 7 i 8 → fa servir els decimals en una situació de debò: preus i rajoles.",
  ]),
  sol.p("Els criteris de la SA del grup (5.1, 7.1 i 8.1) són de referència: l'avaluació es fa amb els criteris del PI. Una explicació oral registrada en el moment, o el codi d'una tasca tancada de la caixa d'eines, valen igual que l'examen escrit."),
];

X.genera({
  unitat: 5, alumnat, solucionari,
  materia: "Matemàtiques",
  creador: "Matemàtiques",
  avis: { text: "Pots fer servir les dues targetes a tot l'examen: la de les taules i la dels decimals i les arrels.", icona: "targeta" },
}).catch(e => { console.error(e.message); process.exit(1); });
