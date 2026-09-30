#!/usr/bin/env node
/*
  1eso/generadors/examens/ud6.js · examen de la Unitat 6 (Sentit espacial)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a comu/examens/nucli.js i les
  regles, a comu/docs/EXAMENS-DOCX.md.

      node 1eso/generadors/examens/ud6.js   →  1eso/docx/examen-ud6-alumnat.docx
                                                1eso/docx/examen-ud6-solucionari.docx

  D'on surt cada cosa:
  · L'ordre, el de les sis fitxes de la unitat (el llibre en fa dos exàmens, un a la UD6 i un a
    la UD7; aquí la unitat és la SA6 sencera): els angles, les peces, els polígons, els
    triangles pels costats i pels angles, el perímetre (del rectangle i dels polígons regulars) i
    el radi i el diàmetre.
  · Els apartats a), b), c) i d), de les fitxes (fitxes/ud6*.html) i dels seus solucionaris. Els
    que no hi són porten la marca «nou» al solucionari (4 d i 7 d). Les regles trencades de les
    fitxes són l'«error típic» dels apartats.
  · Sense transportador ni graus (els angles es comparen amb la cantonada) i sense π = 3,14 (el
    pla validat el 29/9/2026). La targeta «Formes» i la de les taules, al davant.
  · Els angles de l'exercici 1 són dibuixos, amb la cantonada d'un quadret al vèrtex, com a les
    fitxes i a la caixa (tasca 22).
*/
"use strict";

const X = require("../../../comu/examens/nucli");
const { dada, ms, sol } = X;
const { TableRow, AlignmentType } = X.docx;

const cal = (cond, msg) => { if (!cond) throw new Error("ud6.js: " + msg); };
const LET = ["a)", "b)", "c)", "d)"];
const nomAngle = g => (g < 90 ? "Agut" : g === 90 ? "Recte" : g < 180 ? "Obtús" : "Pla");

/* ------------------------------------------------ els dibuixos dels angles -- */
const ANGLES = [40, 125, 90, 180];
const angleSvg = g => {
  const W = 300, H = 170, L = 120, vx = g > 90 ? 150 : 50, vy = g === 180 ? 110 : 150;
  const a = g * Math.PI / 180, x2 = vx + L * Math.cos(a), y2 = vy - L * Math.sin(a), r = 30;
  const ax = vx + r * Math.cos(a), ay = vy - r * Math.sin(a), f = n => Math.round(n * 10) / 10;
  return X.SVG(`0 0 ${W} ${H}`, W, H,
    `<path d="M${vx} ${vy} L${vx + r} ${vy} A${r} ${r} 0 0 0 ${f(ax)} ${f(ay)} Z" fill="#E4E4E4" stroke="#333" stroke-width="2"/>` +
    `<path d="M${vx + 44} ${vy} V${vy - 44} H${vx}" fill="none" stroke="#5E5E5E" stroke-width="2.5" stroke-dasharray="6 4"/>` +
    `<line x1="${vx}" y1="${vy}" x2="${vx + L}" y2="${vy}" stroke="#000" stroke-width="5" stroke-linecap="round"/>` +
    `<line x1="${vx}" y1="${vy}" x2="${f(x2)}" y2="${f(y2)}" stroke="#000" stroke-width="5" stroke-linecap="round"/>` +
    `<circle cx="${vx}" cy="${vy}" r="6" fill="#000"/>`);
};
ANGLES.forEach(g => X.registra(`angle_${g}`, angleSvg(g)));

/* Com taulaResposta, però la segona columna és un dibuix (com les graelles de l'examen de la
   unitat 4). Files: [etiqueta, nom del dibuix, text alternatiu, resposta]. */
function taulaDibuixos(percents, capcalera, files) {
  files.forEach(f => X.anota(String(f[0])));
  return () => {
    const col = X.amples(percents);
    const PAD = { top: X.tw(0.4 * X.REM), bottom: X.tw(0.4 * X.REM), left: X.tw(0.55 * X.REM), right: X.tw(0.55 * X.REM) };
    const cap = new TableRow({ cantSplit: true, tableHeader: true, children: capcalera.map((t, i) =>
      X.cela(X.par(X.run(t, { bold: true, size: X.mig(X.MIDA.capTaula), color: X.G.gris1, characterSpacing: 4 }),
        { alignment: AlignmentType.CENTER, keepNext: true }), { w: col[i], fons: X.G.fons2, margins: PAD })) });
    const cos = files.map(([etiqueta, nom, alt, resposta], r) => {
      const seguir = r < files.length - 1, fonsFila = r === 0 ? X.G.fons1 : undefined;
      return new TableRow({ cantSplit: true, children: [
        X.cela(X.par(X.runsDe(etiqueta, X.MIDA.taula), { alignment: AlignmentType.CENTER, keepNext: seguir }), { w: col[0], fons: fonsFila, margins: PAD }),
        X.cela(X.par(X.imatge(nom, 4.2, 2.4, alt), { alignment: AlignmentType.CENTER, keepNext: seguir }), { w: col[1], fons: X.G.fons1, margins: PAD }),
        X.cela(X.par(X.runsDe(resposta, X.MIDA.taula), { alignment: AlignmentType.CENTER, keepNext: seguir }), { w: col[2], fons: fonsFila, margins: PAD }),
      ] });
    });
    return X.taula(col, [cap, ...cos], { borders: X.REIXA(X.vora(2, X.G.vora)) });
  };
}

/* ------------------------------------------------------------ les dades -- */
const PECES = [["Té dos extrems", "Segment"], ["No té cap extrem", "Recta"],
               ["Té un extrem i no s'acaba", "Semirecta"], ["Un lloc: no es pot mesurar", "Punt"]];
const NOMS = { 3: "Triangle", 4: "Quadrilàter", 5: "Pentàgon", 6: "Hexàgon", 7: "Heptàgon", 8: "Octàgon" };
const POLIGONS = [3, 5, 8, 6];
const COSTATS = [[4, 4, 4], [5, 5, 8], [3, 4, 6], [6, 6, 3]];            // el d és nou
const tipusCostats = ([a, b, c]) => (a === b && b === c ? "Equilàter" : a === b || b === c || a === c ? "Isòsceles" : "Escalè");
const PELS_ANGLES = [["Té un angle recte", "Rectangle"], ["Té un angle més gran que la cantonada", "Obtusangle"],
                     ["Els tres angles són més petits que la cantonada", "Acutangle"], ["Té un angle igual que la cantonada d'un full", "Rectangle"]];
const RECTANGLES = [[5, 3], [2, 5], [6, 4], [3, 3]];
const perimetre = ([c, f]) => 2 * (c + f);
RECTANGLES.forEach(r => cal(r[0] + r[1] <= 10, `${r} surt de la targeta`));
const REGULARS = [["Un quadrat", 4, 5], ["Un triangle equilàter", 3, 9], ["Un octàgon regular", 8, 4], ["Un hexàgon regular", 6, 3]];  // el d és nou
REGULARS.forEach(([, n, c]) => cal(n <= 10 && c <= 10, `${n} · ${c} surt de la targeta`));
const RADIS = [["El radi fa 3 cm", "El diàmetre", 6], ["El radi fa 5 cm", "El diàmetre", 10],
               ["El diàmetre fa 8 cm", "El radi", 4], ["El diàmetre fa 70 cm", "El radi", 35]];

/* ------------------------------------------------------------ l'alumnat -- */
const alumnat = [
  ...X.exercici(1, "Quin angle és? Escriu Agut, Recte, Obtús o Pla.", {}, [
    X.context("La línia discontínua és la cantonada d'un quadret: l'angle recte."),
    taulaDibuixos([10, 50, 40], ["", "L'angle", "Com es diu"], ANGLES.map((g, i) =>
      [LET[i], `angle_${g}`, `Un angle, amb la cantonada d'un quadret al vèrtex`, i === 0 ? ms(nomAngle(g)) : ""])),
  ]),

  ...X.exercici(2, "Com es diu? Escriu Punt, Segment, Semirecta o Recta.", {}, [
    X.context("Mira la targeta."),
    X.taulaResposta([10, 55, 35], ["", "Com és", "Com es diu"], PECES.map(([t, n], i) =>
      [LET[i], dada(t), i === 0 ? ms(n) : ""])),
  ]),

  ...X.exercici(3, "Escriu el nom del polígon.", { mateixaPagina: true }, [
    X.context("El nom diu quants costats té. Mira la targeta."),
    X.taulaResposta([10, 45, 45], ["", "Els costats", "El nom"], POLIGONS.map((n, i) =>
      [LET[i], dada(`${n} costats`), i === 0 ? ms(NOMS[n]) : ""])),
  ]),

  ...X.exercici(4, "Com es diu el triangle pels costats?", {}, [
    X.context("Equilàter: 3 costats iguals. Isòsceles: 2 iguals. Escalè: cap igual."),
    X.taulaResposta([10, 45, 45], ["", "Els tres costats", "El triangle"], COSTATS.map((c, i) =>
      [LET[i], dada(`${c[0]}, ${c[1]} i ${c[2]} cm`), i === 0 ? ms(tipusCostats(c)) : ""])),
  ]),

  ...X.exercici(5, "Com es diu el triangle pels angles?", { mateixaPagina: true }, [
    X.context("Rectangle, acutangle o obtusangle. Mira la targeta."),
    X.taulaResposta([10, 55, 35], ["", "Com són els angles", "El triangle"], PELS_ANGLES.map(([t, n], i) =>
      [LET[i], dada(t), i === 0 ? ms(n) : ""])),
  ]),

  ...X.exercici(6, "Calcula el perímetre del rectangle.", {}, [
    X.context("El perímetre és la vora: dalt, dreta, baix i esquerra."),
    X.taulaResposta([10, 40, 50], ["", "El rectangle", "El perímetre"], RECTANGLES.map(([c, f], i) =>
      [LET[i], dada(`${c} cm per ${f} cm`), i === 0 ? ms(`${c} + ${f} + ${c} + ${f} = ${perimetre([c, f])} cm`) : ""])),
  ]),

  ...X.exercici(7, "Calcula el perímetre. Tots els costats són iguals.", { mateixaPagina: true }, [
    X.context("Suma els costats, o multiplica: quants costats per quant mesura cada un."),
    X.taulaResposta([10, 50, 40], ["", "El polígon", "El perímetre"], REGULARS.map(([t, n, c], i) =>
      [LET[i], dada(`${t} de ${c} cm de costat`), i === 0 ? ms(`${n} · ${c} = ${n * c} cm`) : ""])),
  ]),

  ...X.exercici(8, "Escriu el radi o el diàmetre.", {}, [
    X.context("El diàmetre és el doble del radi. El radi és la meitat del diàmetre."),
    X.taulaResposta([10, 45, 20, 25], ["", "La dada", "Què falta", "La resposta"], RADIS.map(([t, q, v], i) =>
      [LET[i], dada(t), q, i === 0 ? ms(`${v} cm`) : ""])),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const TRAS = { spacing: { before: X.tw(5), after: X.tw(8) } };
const resta = (c, f) => c.slice(1).map((x, i) => f(x, LET[i + 1])).join("; ");

const solucionari = privat => [
  ...sol.titol(6),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Sense transportador ni calculadora: la *targeta «Formes»* i la *targeta de les taules* són al davant tota l'estona, i es pot fer servir la cantonada d'un full.`,
    "*Com s'ha construït:* en l'ordre de les sis fitxes de la unitat (els angles, les peces, els polígons, els triangles pels costats i pels angles, el perímetre i el radi i el diàmetre). A cada exercici, l'apartat a) resolt com a model i tres per fer, amb els ítems de les fitxes. Els apartats marcats «nou» són el 4 d) i el 7 d), revisats el 30/9/2026.",
    "*Queda fora, com a les fitxes:* els graus i el transportador, π = 3,14, la condició d'existència del triangle i les àrees amb fórmules.",
    "*Si cal, en dues sessions:* els exercicis 1 a 5 (les formes) i els 6 a 8 (les mesures).",
  ]),

  sol.h3("1. Els angles"),
  sol.p(`${resta(ANGLES, (g, l) => `${l} *${nomAngle(g)}*`)}. *Error típic:* decidir per la llargada dels costats, que és la regla trencada de la fitxa 1. Amb la cantonada d'un full al vèrtex es veu.`, TRAS),
  sol.h3("2. Les peces"),
  sol.p(`${resta(PECES, ([, n], l) => `${l} *${n}*`)}. Són les definicions de la targeta.`, TRAS),
  sol.h3("3. Els polígons"),
  sol.p(`${resta(POLIGONS, (n, l) => `${l} *${NOMS[n]}*`)} (els casos del llibre). *Error típic:* comptar un vèrtex de menys; el polígon té tants vèrtexs com costats.`, TRAS),
  sol.h3("4. Els triangles pels costats · la d, nova"),
  sol.p(`${resta(COSTATS, (c, l) => `${l} *${tipusCostats(c)}*`)}. Els tres primers són del llibre. La d) és nova (6, 6 i 3 cm), revisada el 30/9/2026: el triangle es pot fer (3 + 6 és més que 6).`, TRAS),
  sol.h3("5. Els triangles pels angles"),
  sol.p(`${resta(PELS_ANGLES, ([, n], l) => `${l} *${n}*`)}. La d) diu el mateix que la a) amb altres paraules: la cantonada d'un full és un angle recte.`, TRAS),
  sol.h3("6. El perímetre del rectangle"),
  sol.p(`${resta(RECTANGLES, ([c, f], l) => `${l} ${c} + ${f} + ${c} + ${f} = *${perimetre([c, f])} cm*`)}. *Error típic:* donar l'àrea (5 · 3 = 15), com la Carlota de la fitxa 4; és la regla trencada. A la d) (3 per 3) el perímetre, 12, no és l'àrea, 9.`, TRAS),
  sol.h3("7. El perímetre dels polígons regulars · la d, nova"),
  sol.p(`${resta(REGULARS, ([, n, c], l) => `${l} ${n} · ${c} = *${n * c} cm*`)}. Els tres primers són de la fitxa 4 i del llibre. La d) és nova, revisada el 30/9/2026: 6 · 3 és de la targeta de les taules.`, TRAS),
  sol.h3("8. El radi i el diàmetre"),
  sol.p(`${resta(RADIS, ([, q, v], l) => `${l} ${q.toLowerCase()}: *${v} cm*`)}. La d) és la roda de bicicleta del llibre. *Error típic:* fer el doble quan toca la meitat.`, TRAS),

  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Exercici 1 → diu si un angle és agut, recte, obtús o pla, comparant-lo amb la cantonada.",
    "Exercicis 2 i 3 → diu el nom de les peces bàsiques i dels polígons, amb la targeta.",
    "Exercicis 4 i 5 → diu com és un triangle pels costats i pels angles.",
    "Exercicis 6 i 7 → calcula el perímetre sumant la vora, o multiplicant si els costats són iguals.",
    "Exercici 8 → passa del radi al diàmetre i al revés.",
  ]),
  sol.p("Els criteris de la SA del grup (1.1, 3.1, 5.1, 6.1, 7.1 i 9.1) són de referència: l'avaluació es fa amb els criteris del PI. Una explicació oral registrada en el moment, «La meva Fotomàtica» o el codi d'una tasca tancada de la caixa d'eines valen igual que l'examen escrit."),
];

X.genera({
  unitat: 6, alumnat, solucionari,
  materia: "Matemàtiques",
  creador: "Matemàtiques",
  avis: { text: "Pots fer servir les dues targetes a tot l'examen: la de les taules i la de les formes. També la cantonada d'un full.", icona: "targeta" },
}).catch(e => { console.error(e.message); process.exit(1); });
