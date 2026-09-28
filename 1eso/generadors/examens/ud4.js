#!/usr/bin/env node
/*
  1eso/generadors/examens/ud4.js · examen de la Unitat 4 (És gran l'ou del kiwi?)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a comu/examens/nucli.js i les
  regles, a comu/docs/EXAMENS-DOCX.md.

      node 1eso/generadors/examens/ud4.js   →  1eso/docx/examen-ud4-alumnat.docx
                                                1eso/docx/examen-ud4-solucionari.docx

  D'on surt cada cosa:
  · L'ordre, el de les cinc fitxes de la unitat: dos exercicis per cada part
    (la fracció d'un nombre, multiplicar fraccions, els percentatges i els dobles
    i triples). La programació no porta cap examen per a aquesta unitat (l'activitat
    11 és una avaluació individual i una autoavaluació): no hi ha ordre del grup a seguir.
  · Els apartats a), b), c) i d), de les fitxes (fitxes/ud4*.html) i dels seus
    solucionaris. L'únic que no hi és (exercici 6, d) porta la marca «nou» al
    solucionari. Les regles trencades de les fitxes no són exercicis apart:
    són l'«error típic» dels apartats, com a les unitats 2 i 3.
  · Fora: la comparació de l'ou i l'ocell (fitxa 4, exercici 3), perquè és una
    valoració qualitativa, i les regles del docent diuen que cap pregunta de
    justificació oberta no entra a l'examen.
  · Sense calculadora: les dues targetes al davant (taules i fraccions). Cada xifra
    es calcula aquí, i l'examen i el solucionari en surten: no poden discrepar.
    Multiplicacions de la targeta, denominadors fins a 12 i cap nombre de més de 999.
*/
"use strict";

const X = require("../../../comu/examens/nucli");
const { dada, ms, sol } = X;
const { TableRow, AlignmentType } = X.docx;

/* --------------------------------------------------- la calculadora, aquí -- */
const cal = (cond, msg) => { if (!cond) throw new Error("ud4.js: " + msg); };
const TARGETA = 10;                                    // les taules de la targeta arriben al 10 · 10
const LET = ["a)", "b)", "c)", "d)"];
const PCT = n => `${n}\u00A0%`;

// Exercicis 1 i 2 · la fracció d'un nombre (fitxa 1): [numerador, denominador, nombre]
const FN1 = [[1, 3, 12], [1, 4, 16], [1, 2, 14], [1, 5, 20]];
const FN2 = [[2, 3, 12], [3, 4, 16], [2, 5, 20], [3, 5, 25]];
const fn = ([n, d, t]) => {
  cal(t % d === 0, `${t} no es reparteix en ${d} grups iguals`);
  const g = t / d, r = n * g;
  cal(n < d && g <= TARGETA && n <= TARGETA && r <= 999, `${n}/${d} de ${t} surt de la targeta`);
  return { dada: `{${n}/${d}} de ${t} quadrets`, n, d, t, g, r };
};

// Exercicis 3 i 4 · multiplicar fraccions (fitxa 2): els dos denominadors, amb producte fins a 12
const TT1 = [[2, 3], [3, 2], [2, 5], [3, 3]];          // quants trossos petits
const TT2 = [[3, 4], [2, 4], [4, 2], [2, 6]];          // el resultat, com a fracció
const tt = ([a, b]) => {
  cal(a <= TARGETA && b <= TARGETA && a * b <= 12, `1/${a} de 1/${b} surt del límit de la unitat`);
  return { dada: `{1/${a}} de {1/${b}}`, a, b, dr: a * b };
};

// Exercicis 5 i 6 · els percentatges (fitxa 3)
const PCT_FRAC = { 10: [1, 10], 20: [1, 5], 25: [1, 4], 50: [1, 2], 75: [3, 4] };
Object.entries(PCT_FRAC).forEach(([p, [n, d]]) => cal(n * 100 === Number(p) * d, `${p} % no és ${n}/${d}`));
const GRAELLES = [50, 75, 10, 20];                     // el primer és el resolt
const PF = [50, 25, 75, 20];                           // el darrer és nou

// Exercicis 7 i 8 · dobles i triples (fitxa 4): [nombre, vegades]
const DT1 = [[3, 2], [5, 2], [4, 3], [2, 3]];
const DT2 = [[3, 3], [6, 2], [5, 3], [3, 2]];
const nomK = k => (k === 2 ? "doble" : "triple");
[...DT1, ...DT2].forEach(([n, k]) => cal(n <= TARGETA && (k === 2 || k === 3) && n * k <= 999, `${n} · ${k} surt de la targeta`));

/* ------------------------------------------- la peça nova: graella de 100 -- */
/* Una graella de 10 × 10 amb els primers `p` quadrets pintats, en grisos. Serveix
   per comptar quadrets i dir el percentatge (fitxa 3, exercici 2). */
const graellaSvg = p => {
  const m = 30, marge = 2, W = 10 * m + 2 * marge;
  let s = "";
  for (let i = 0; i < 100; i++) {
    const x = marge + (i % 10) * m, y = marge + Math.floor(i / 10) * m, pintat = i < p;
    s += `<rect x="${x}" y="${y}" width="${m}" height="${m}" fill="${pintat ? "#BFBFBF" : "#FFFFFF"}" ` +
         `stroke="${pintat ? "#3A3A3A" : "#5E5E5E"}" stroke-width="${pintat ? 1.8 : 1.2}"/>`;
  }
  return X.SVG(`0 0 ${W} ${W}`, W, W, s);
};
GRAELLES.forEach(p => X.registra(`graella_${p}`, graellaSvg(p)));

/* Com taulaResposta, però la segona columna és una graella. Files: [etiqueta, percentatge, resposta]. */
function taulaGraelles(percents, capcalera, files) {
  files.forEach(f => X.anota(String(f[0])));
  return () => {
    const col = X.amples(percents);
    const PAD = { top: X.tw(0.5 * X.REM), bottom: X.tw(0.5 * X.REM), left: X.tw(0.55 * X.REM), right: X.tw(0.55 * X.REM) };
    const cap = new TableRow({ cantSplit: true, tableHeader: true, children: capcalera.map((t, i) =>
      X.cela(X.par(X.run(t, { bold: true, size: X.mig(X.MIDA.capTaula), color: X.G.gris1, characterSpacing: 4 }),
        { alignment: AlignmentType.CENTER, keepNext: true }), { w: col[i], fons: X.G.fons2, margins: PAD })) });
    const cos = files.map(([etiqueta, p, resposta], r) => {
      const seguir = r < files.length - 1, fonsFila = r === 0 ? X.G.fons1 : undefined;
      return new TableRow({ cantSplit: true, children: [
        X.cela(X.par(X.runsDe(etiqueta, X.MIDA.taula), { alignment: AlignmentType.CENTER, keepNext: seguir }), { w: col[0], fons: fonsFila, margins: PAD }),
        X.cela(X.par(X.imatge(`graella_${p}`, 3.5, 3.5, `Graella de 100 quadrets, amb ${p} de pintats`),
          { alignment: AlignmentType.CENTER, keepNext: seguir }), { w: col[1], fons: X.G.fons1, margins: PAD }),
        X.cela(X.par(X.runsDe(resposta, X.MIDA.taula), { alignment: AlignmentType.CENTER, keepNext: seguir }), { w: col[2], fons: fonsFila, margins: PAD }),
      ] });
    });
    return X.taula(col, [cap, ...cos], { borders: X.REIXA(X.vora(2, X.G.vora)) });
  };
}

/* ------------------------------------------------------------ l'alumnat -- */
const alumnat = [
  ...X.exercici(1, "Reparteix en grups iguals. Escriu quants quadrets té un grup.", {}, [
    X.context("El de baix diu en quants grups es reparteix. Mira la targeta de les taules."),
    X.taulaResposta([10, 45, 45], ["", "La fracció", "Un grup"], FN1.map(fn).map((c, i) =>
      [LET[i], dada(c.dada), i === 0 ? ms(`${c.g} quadrets`) : ""])),
  ]),

  ...X.exercici(2, "Escriu quants quadrets són. Primer reparteix; després multiplica.", {}, [
    X.context("El de dalt diu quants grups es compten."),
    X.taulaResposta([10, 42, 48], ["", "La fracció", "El càlcul"], FN2.map(fn).map((c, i) =>
      [LET[i], dada(c.dada), i === 0 ? ms(`${c.n} · ${c.g} = ${c.r} quadrets`) : ""])),
  ]),

  ...X.exercici(3, "Fes un tros de tros. Escriu quants trossos petits hi ha.", {}, [
    X.context("Multiplica els dos de baix. Si ho necessites, fes el rectangle al marge."),
    X.taulaResposta([10, 45, 45], ["", "Les dues fraccions", "Trossos petits"], TT1.map(tt).map((c, i) =>
      [LET[i], dada(c.dada), i === 0 ? ms(`${c.a} · ${c.b} = ${c.dr} trossos`) : ""])),
  ]),

  ...X.exercici(4, "Escriu el resultat com a fracció.", { mateixaPagina: true }, [
    X.context("Multiplica els dos de baix. El resultat té 1 a dalt."),
    X.taulaResposta([10, 45, 45], ["", "Les dues fraccions", "El resultat"], TT2.map(tt).map((c, i) =>
      [LET[i], dada(c.dada), i === 0 ? ms(`{1/${c.dr}}`) : ""])),
  ]),

  ...X.exercici(5, "Compta els quadrets pintats. Escriu quin percentatge és.", {}, [
    X.context("Cada quadret pintat és l'1 %. Cada fila té 10 quadrets."),
    taulaGraelles([10, 50, 40], ["", "Els quadrets pintats", "El percentatge"], GRAELLES.map((p, i) =>
      [LET[i], p, i === 0 ? ms(PCT(p)) : ""])),
  ]),

  ...X.exercici(6, "Escriu la fracció de cada percentatge. Mira les targetes.", {}, [
    X.context("Pensa en la graella de 100. Quina part és dels 100 quadrets?"),
    X.taulaResposta([10, 45, 45], ["", "El percentatge", "La fracció"], PF.map((p, i) =>
      [LET[i], dada(PCT(p)), i === 0 ? ms(`{${PCT_FRAC[p][0]}/${PCT_FRAC[p][1]}}`) : ""])),      // el d) és nou
  ]),

  ...X.exercici(7, "Fes el doble o el triple de la fila. Escriu quants quadrets té.", {}, [
    X.context("El doble és 2 vegades. El triple és 3 vegades."),
    X.taulaResposta([10, 45, 45], ["", "Què fas", "La fila gran"], DT1.map(([n, k], i) =>
      [LET[i], dada(`El ${nomK(k)} de ${n} quadrets`), i === 0 ? ms(`${n} · ${k} = ${n * k} quadrets`) : ""])),
  ]),

  ...X.exercici(8, "La fila gran és el doble o el triple de la petita? Escriu El doble o El triple.", { mateixaPagina: true }, [
    X.context("Mira quantes vegades hi cap la fila petita dins de la gran."),
    X.taulaResposta([10, 45, 45], ["", "Fila petita i fila gran", "La fila gran és"], DT2.map(([n, k], i) =>
      [LET[i], dada(`${n} quadrets i ${n * k} quadrets`), i === 0 ? ms(`El ${nomK(k)}`) : ""])),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const TRAS = { spacing: { before: X.tw(5), after: X.tw(8) } };
const resta = (c, f) => c.slice(1).map((x, i) => f(x, LET[i + 1])).join("; ");
const NG = fn([1, 3, 12]);

const solucionari = privat => [
  ...sol.titol(4),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Sense calculadora: la *targeta de les taules* i la *targeta dels noms de les fraccions* són al davant tota l'estona.`,
    "*Com s'ha construït:* la programació d'aquesta unitat no porta cap examen (l'activitat 11 és una avaluació individual i una autoavaluació), així que l'examen té dos exercicis per cada part de la unitat: la fracció d'un nombre, multiplicar fraccions, els percentatges i els dobles i triples, en l'ordre de les fitxes. A cada exercici, l'apartat a) resolt com a model i tres per fer, amb els ítems de les cinc fitxes de la unitat. Cap pregunta de justificació oberta: la comparació de l'ou i l'ocell (fitxa 4, exercici 3) hi queda fora, perquè és una valoració qualitativa. L'únic apartat marcat «nou» és el 6 d): revisa'l abans de fer servir l'examen.",
    "*Si cal, en dues sessions:* els exercicis 1 a 4 (la fracció d'un nombre i multiplicar fraccions) i els 5 a 8 (els percentatges i els dobles i triples).",
    "*Es pot dibuixar:* un rectangle, o files de quadrets, al marge, per repartir o per fer el tros de tros, és una estratègia bona, no un error.",
  ]),

  sol.h3("1. La fracció d'un nombre: un grup"),
  sol.p(`${resta(FN1.map(fn), (c, l) => `${l} ${c.g} · ${c.d} = ${c.t}: *${c.g} quadrets*`)}. Es reparteix el nombre en grups iguals, amb la targeta de les taules. *Error típic:* dir el nombre de grups (${NG.d}) en lloc dels quadrets d'un grup (${NG.g}).`, TRAS),

  sol.h3("2. La fracció d'un nombre: més d'un grup"),
  sol.p(`${resta(FN2.map(fn), (c, l) => `${l} ${c.n} · ${c.g} = *${c.r}*`)}. Primer es reparteix, després es multipliquen els grups que es compten. *Error típic:* donar els quadrets d'un sol grup, sense multiplicar.`, TRAS),

  sol.h3("3. El tros de tros"),
  sol.p(`${resta(TT1.map(tt), (c, l) => `${l} ${c.a} · ${c.b} = *${c.dr} trossos*`)}. Columnes per files. Són els apartats de la fitxa 2.`, TRAS),

  sol.h3("4. El resultat, com a fracció"),
  sol.p(`${resta(TT2.map(tt), (c, l) => `${l} ${c.a} · ${c.b} = ${c.dr}: *1/${c.dr}*`)}. *Error típic:* sumar els de baix (1/3 de 1/4 fet 1/7). És la regla trencada de la fitxa 2: els de baix es multipliquen. El resultat no passa mai del 12, com a la unitat 3.`, TRAS),

  sol.h3("5. Quin percentatge és"),
  sol.p(`${resta(GRAELLES, (p, l) => `${l} *${PCT(p)}*`)}. Cada fila de la graella té 10 quadrets. *Error típic:* dir els quadrets que falten (25 % en lloc de 75 %), o dir 100 % encara que no estigui tot pintat. És la regla trencada de la fitxa 3.`, TRAS),

  sol.h3("6. La fracció del percentatge · la d, nova"),
  sol.p(`b) ${PCT(25)} és *1/4*; c) ${PCT(75)} és *3/4*; d) nou: ${PCT(20)} és *1/5*. Els tres primers són de la fitxa 3. La d) és nova: el 20 % és a la llista de percentatges de la unitat (10, 20, 25, 50 i 75 %), però la fitxa no el porta com a apartat. Revisa-la abans de fer servir l'examen.`, TRAS),

  sol.h3("7. El doble i el triple"),
  sol.p(`${resta(DT1, ([n, k], l) => `${l} ${n} · ${k} = *${n * k}*`)}. El doble és 2 vegades; el triple, 3 vegades. Són els apartats de la fitxa 4.`, TRAS),

  sol.h3("8. Quantes vegades hi cap"),
  sol.p(`${resta(DT2, ([n, k], l) => `${l} *El ${nomK(k)}* (${n} · ${k} = ${n * k})`)}. Es compta de tants en tants quadrets com la fila petita, des de l'esquerra.`, TRAS),

  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Exercicis 1 i 2 → reparteix un nombre en grups iguals i compta els grups que diu la fracció, amb la targeta.",
    "Exercicis 3 i 4 → fa un tros de tros: multiplica els dos de baix i escriu el resultat com a fracció.",
    "Exercici 5 → compta els quadrets pintats d'una graella de 100 i diu el percentatge.",
    "Exercici 6 → relaciona un percentatge amb la seva fracció.",
    "Exercicis 7 i 8 → fa el doble i el triple d'una fila, i diu quantes vegades hi cap la fila petita.",
  ]),
  sol.p("Els criteris de la SA del grup (1.3, 2.1, 5.1 i 6.1) són de referència: l'avaluació es fa amb els criteris del PI. Una explicació oral registrada en el moment, o el codi d'una tasca tancada de la caixa d'eines, valen igual que l'examen escrit."),
];

X.genera({
  unitat: 4, alumnat, solucionari,
  materia: "Matemàtiques",
  creador: "Matemàtiques",
  avis: { text: "Pots fer servir les dues targetes a tot l'examen: la de les taules i la de les fraccions.", icona: "targeta" },
}).catch(e => { console.error(e.message); process.exit(1); });
