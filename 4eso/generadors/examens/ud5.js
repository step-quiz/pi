#!/usr/bin/env node
/*
  4eso/generadors/examens/ud5.js · examen de la Unitat 5 (La paràbola)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a comu/examens/nucli.js i les
  regles, a comu/docs/EXAMENS-DOCX.md. El model és ud1.js.

      node 4eso/generadors/examens/ud5.js   →  4eso/docx/examen-ud5-alumnat.docx
                                                4eso/docx/examen-ud5-solucionari.docx

  D'on surt cada cosa:
  · Els apartats a), b), c) i d), dels exercicis de fitxes/ud5.html i del seu solucionari.
    On la fitxa no en tenia prou, n'hi ha un de nou, i al solucionari porta la marca «nou».
  · Les gràfiques es dibuixen aquí amb la mateixa funció que generadors/gen_grafics.py
    (graf(), portada a JavaScript) i els mateixos paràmetres: són les de la fitxa. Les que
    van de dues en dues porten la lletra a 28, com les de costat de la fitxa, perquè al
    paper no baixi de 12 pt. Les noves (la pilota de bàsquet, el salt de granota i dues
    funcions de l'exercici 7) segueixen el mateix patró.
  · Sense les preguntes obertes de la fitxa (6f, 7c i 8e).
  · La regla trencada de la fitxa (ex. 2, el vèrtex que és un mínim i sense talls) hi és.
  Proposta del 30/9/2026, per validar amb el docent.
*/
"use strict";

const X = require("../../../comu/examens/nucli");
const { dada, ms, sol } = X;
const { AlignmentType, TableRow } = X.docx;

const cal = (cond, msg) => { if (!cond) throw new Error("ud5.js: " + msg); };
const nb = s => s.replace(/ = /g, " = ").replace(/([+−]) (?=\d)/g, "$1 ");
const txt = s => dada(nb(s), undefined, { esq: true });
const LL = ["b)", "c)", "d)"];

/* ------------------------------------------------ les gràfiques (graf) -- */
/* La mateixa geometria de generadors/gen_grafics.py: 560 × 300, marges 54 i 20,
   graella a les marques, halo blanc sota els rètols. */
const W = 560, H = 300, ML = 54, MR = 20;
function marques(vmin, vmax, pas) {
  let k = Math.ceil(vmin / pas - 1e-9); const out = [];
  while (k * pas <= vmax + 1e-9) { out.push(Math.round(k * pas * 1e10) / 1e10); k++; }
  return out;
}
function rotul(x, y, text, fs, ancora = "middle", gruix = 400, color = "#5E5E5E") {
  const comu = `x="${x.toFixed(1)}" y="${y.toFixed(1)}" text-anchor="${ancora}" font-size="${fs}" font-weight="${gruix}" font-family="Verdana"`;
  return `<text ${comu} fill="#fff" stroke="#fff" stroke-width="${(fs * 0.28).toFixed(1)}" stroke-linejoin="round">${text}</text>` +
         `<text ${comu} fill="${color}">${text}</text>`;
}
function graf(a, b, c, xmin, xmax, ymin, ymax, xstep, ystep, etiqx, etiqy, { decX = 0, decY = 0, fs = 20 } = {}) {
  const MT = fs + 14, MB = 2 * fs + 16;
  const px = x => ML + (x - xmin) / (xmax - xmin) * (W - ML - MR);
  const py = y => H - MB - (y - ymin) / (ymax - ymin) * (H - MB - MT);
  const n = (v, d) => { let s = v.toFixed(d); if (d) s = s.replace(/0+$/, "").replace(/\.$/, "");
                        return (s === "-0" ? "0" : s).replace(".", ",").replace("-", "−"); };
  const xs = marques(xmin, xmax, xstep), ys = marques(ymin, ymax, ystep);
  const o = [];
  xs.forEach(x => o.push(`<line x1="${px(x).toFixed(1)}" y1="${py(ymin).toFixed(1)}" x2="${px(x).toFixed(1)}" y2="${py(ymax).toFixed(1)}" stroke="#D4D4D4" stroke-width="1"/>`));
  ys.forEach(y => o.push(`<line x1="${px(xmin).toFixed(1)}" y1="${py(y).toFixed(1)}" x2="${px(xmax).toFixed(1)}" y2="${py(y).toFixed(1)}" stroke="#D4D4D4" stroke-width="1"/>`));
  const y0 = ymin <= 0 && 0 <= ymax ? 0 : ymin, x0 = xmin <= 0 && 0 <= xmax ? 0 : xmin;
  o.push(`<line x1="${px(xmin).toFixed(1)}" y1="${py(y0).toFixed(1)}" x2="${px(xmax).toFixed(1)}" y2="${py(y0).toFixed(1)}" stroke="#000" stroke-width="2.5"/>`);
  o.push(`<line x1="${px(x0).toFixed(1)}" y1="${py(ymin).toFixed(1)}" x2="${px(x0).toFixed(1)}" y2="${py(ymax).toFixed(1)}" stroke="#000" stroke-width="2.5"/>`);
  const r = [];
  const ampleX = Math.max(...xs.map(x => n(x, decX).length)) * fs * 0.62 + fs * 0.6;
  const cadaX = px(xs[1]) - px(xs[0]) >= ampleX ? 1 : 2;
  const cadaY = py(ys[0]) - py(ys[1]) >= fs * 1.25 ? 1 : 2;
  xs.forEach(x => { if (Math.abs(x - x0) > 1e-9 && Math.round(x / xstep) % cadaX === 0) r.push(rotul(px(x), py(y0) + fs + 6, n(x, decX), fs)); });
  ys.forEach(y => { if (Math.abs(y - y0) > 1e-9 && Math.round(y / ystep) % cadaY === 0) r.push(rotul(px(x0) - 8, py(y) + fs * 0.35, n(y, decY), fs, "end")); });
  if (etiqx) r.push(rotul(W - MR, H - 8, etiqx, fs, "end"));
  if (etiqy) r.push(rotul(px(x0) + 8, MT - 10, etiqy, fs, "start"));
  const trams = []; let ara = [];
  for (let i = 0; i <= 800; i++) {
    const xv = xmin + (xmax - xmin) * i / 800, yv = a * xv * xv + b * xv + c;
    if (yv >= ymin - 1e-9 && yv <= ymax + 1e-9) ara.push(`${px(xv).toFixed(1)},${py(yv).toFixed(1)}`);
    else if (ara.length) { trams.push(ara); ara = []; }
  }
  if (ara.length) trams.push(ara);
  trams.forEach(t => o.push(`<polyline points="${t.join(" ")}" fill="none" stroke="#000" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>`));
  return X.SVG(`0 0 ${W} ${H}`, W, H, `<rect x="0" y="0" width="${W}" height="${H}" fill="#fff"/>` + o.join("") + r.join(""));
}

// Els paràmetres de generadors/gen_grafics.py i gen_grafics5.py. Les de costat, amb fs 28.
const DOS = { fs: 28 };
X.registra("pilota",   graf(-5, 10, 0, 0, 2.4, 0, 6, 0.5, 1, "temps (s)", "altura (m)", { decX: 1, ...DOS }));
X.registra("sortidor", graf(-0.5, 2, 0, 0, 4.6, 0, 3, 1, 0.5, "distància (m)", "altura (m)", { decY: 1, ...DOS }));
X.registra("basquet",  graf(-1, 6, 0, 0, 6.6, 0, 10, 1, 2, "temps (s)", "altura (m)", DOS));              // nou
X.registra("granota",  graf(-2, 4, 0, 0, 2.4, 0, 3, 0.5, 1, "distància (m)", "altura (m)", { decX: 1, ...DOS }));  // nou
X.registra("tarifa",   graf(1, -8, 20, 0, 8, 0, 22, 1, 2, "peces", "cost (€)"));
X.registra("coet",     graf(-5, 20, 0, 0, 4.4, 0, 22, 1, 2, "temps (s)", "altura (m)"));
X.registra("eq1",      graf(1, -5, 6, -0.4, 5.4, -2, 7, 1, 1, "x", "y", DOS));
X.registra("eq2",      graf(1, 0, -4, -3.2, 3.2, -5, 6, 1, 1, "x", "y", DOS));
X.registra("eq3",      graf(1, -6, 8, -0.4, 6.4, -2, 9, 1, 1, "x", "y", DOS));                          // nou
X.registra("eq4",      graf(1, 0, -1, -2.4, 2.4, -2, 5, 1, 1, "x", "y", DOS));                          // nou
X.registra("dofi",     graf(-0.75, 3, 0, 0, 4.4, 0, 3.6, 1, 1, "distància (m)", "altura (m)", DOS));
X.registra("cable",    graf(0.25, -2, 6, 0, 8.4, 0, 7.2, 1, 1, "distància (m)", "altura (m)", DOS));

// Els vèrtexs i els talls que es demanen, comprovats amb la fórmula.
const vertex = (a, b, c) => [-b / (2 * a), c - b * b / (4 * a)];
const talls = (a, b, c) => { const d = b * b - 4 * a * c; if (d < 0) return [];
  return [(-b - Math.sqrt(d)) / (2 * a), (-b + Math.sqrt(d)) / (2 * a)].sort((p, q) => p - q); };
cal(vertex(-1, 6, 0).join() === "3,9" && talls(-1, 6, 0).join() === "0,6", "bàsquet");
cal(vertex(-2, 4, 0).join() === "1,2" && talls(-2, 4, 0).join() === "0,2", "granota");
cal(talls(1, -6, 8).join() === "2,4" && talls(1, 0, -1).join() === "-1,1", "eq3 i eq4");
cal(talls(1, -8, 20).length === 0 && talls(0.25, -2, 6).length === 0, "tarifa i cable no tallen");

/* Dues gràfiques de costat, cadascuna amb el seu rètol a sobre. */
const COSTAT = 8.9;
function duo(parells) {
  return () => {
    const w = Math.floor(X.AMPLE / 2);
    const cel = ([nom, rot, alt]) => X.cela([
      X.par(X.run(rot, { size: X.mig(X.MIDA.context), color: X.G.gris2 }), { keepNext: true, spacing: { after: X.tw(3) } }),
      X.par(X.imatge(nom, COSTAT, COSTAT * H / W, alt), { alignment: AlignmentType.CENTER, keepNext: true }),
    ], { w, va: X.docx.VerticalAlign.TOP });
    const files = [];
    for (let i = 0; i < parells.length; i += 2)
      files.push(new TableRow({ cantSplit: true, children: [cel(parells[i]), cel(parells[i + 1])] }));
    return X.taula([w, X.AMPLE - w], files);
  };
}
const una = (nom, cm, alt) => () => X.par(X.imatge(nom, cm, cm * H / W, alt), { alignment: AlignmentType.CENTER, keepNext: true });

/* ------------------------------------------------------------- l'alumnat -- */
const alumnat = [
  ...X.exercici(1, "Llegeix el vèrtex i els punts de tall de cada gràfica.", {}, [
    duo([["pilota", "a) Una pilota xutada.", "Paràbola de la pilota: puja de 0 a 5 metres i torna a terra al segon 2"],
         ["sortidor", "b) Un sortidor d'aigua.", "Paràbola del sortidor, de 0 a 4 metres de distància"],
         ["basquet", "c) Una pilota de bàsquet.", "Paràbola de la pilota de bàsquet, de 0 a 6 segons"],
         ["granota", "d) El salt d'una granota.", "Paràbola del salt de la granota, de 0 a 2 metres"]]),
    () => X.espai(12, { keepNext: true }),
    X.taulaResposta([10, 30, 30, 30], ["", "Vèrtex", "Primer tall", "Segon tall"], [
      ["a)", ms("(1 , 5)"), ms("0"), ms("2")],
      ["b)", "", "", ""], ["c)", "", "", ""], ["d)", "", "", ""],
    ]),
  ]),

  ...X.exercici(2, "Llegeix aquesta gràfica. Compte, que aquesta s'obre cap amunt.", {}, [
    X.context("El cost de fabricar peces en un taller."),
    una("tarifa", 12.5, "Paràbola del cost, que s'obre cap amunt i no toca la línia de baix"),
    () => X.espai(10, { keepNext: true }),
    X.taulaResposta([10, 55, 35], ["", "Pregunta", "Resposta"], [
      ["a)", ms("Cap on s'obre?", undefined, { esq: true }), ms("Cap amunt")],
      ["b)", txt("Quin és el vèrtex?"), ""],
      ["c)", txt("És el punt més alt o el més baix?"), ""],
      ["d)", txt("Quants punts de tall té?"), ""],
    ]),
  ]),

  ...X.exercici(3, "Mira el número de davant de x² i digues cap on s'obre.", {}, [
    X.taulaResposta([10, 55, 35], ["", "L'expressió", "S'obre cap…"], [
      ["a)", ms(nb("y = −5x² + 10x")), ms("avall")],
      ["b)", dada(nb("y = x² − 8x + 20")), ""],
      ["c)", dada(nb("y = −0,5x² + 2x")), ""],
      ["d)", dada(nb("y = 3x² − 12x")), ""],
    ]),
  ]),

  ...X.exercici(4, "Escriu el número del significat que correspon a cada element.", {}, [
    X.context("Torna a mirar la pilota de l'exercici 1."),
    X.context("1. La pilota surt de terra.   2. La pilota arriba al punt més alt."),
    X.context("3. La pilota torna a tocar terra.   4. Triga el mateix a pujar que a baixar."),
    X.taulaResposta([10, 60, 30], ["", "Element", "Número"], [
      ["a)", ms("El vèrtex", undefined, { esq: true }), ms("2")],
      ["b)", txt("El tall de l'esquerra"), ""],
      ["c)", txt("El tall de la dreta"), ""],
      ["d)", txt("L'eix de simetria"), ""],
    ]),
  ]),

  ...X.exercici(5, "Escriu si la lectura és correcta.", {}, [
    X.context("Sobre la gràfica de la pilota de l'exercici 1."),
    X.taulaResposta([10, 60, 30], ["", "Algú diu…", "Bé o malament?"], [
      ["a)", ms(nb("El vèrtex és (5 , 1)."), undefined, { esq: true }), ms("Malament")],
      ["b)", txt("La pilota puja fins a 5 metres."), ""],
      ["c)", txt("La pilota toca terra al segon 5."), ""],
      ["d)", txt("L'eix de simetria passa pel segon 1."), ""],
    ]),
  ]),

  ...X.exercici(6, "Llegeix la gràfica del coet i contesta.", {}, [
    X.context("Un coet d'aigua llançat des de terra."),
    una("coet", 12.5, "Paràbola del coet: puja fins a 20 metres i torna a terra al segon 4"),
    () => X.espai(10, { keepNext: true }),
    X.taulaResposta([10, 55, 35], ["", "Pregunta", "Resposta"], [
      ["a)", ms("Quina altura màxima arriba?", undefined, { esq: true }), ms("20 m")],
      ["b)", txt("En quin segon hi arriba?"), ""],
      ["c)", txt("Quan torna a terra?"), ""],
      ["d)", txt("Quina altura té al segon 1?"), ""],
    ]),
  ]),

  ...X.exercici(7, "Els punts de tall són les solucions de l'equació.", {}, [
    duo([["eq1", nb("a) y = x² − 5x + 6"), "Paràbola que talla la línia de baix al 2 i al 3"],
         ["eq2", nb("b) y = x² − 4"), "Paràbola que talla la línia de baix a dos punts"],
         ["eq3", nb("c) y = x² − 6x + 8"), "Paràbola que talla la línia de baix a dos punts"],
         ["eq4", nb("d) y = x² − 1"), "Paràbola que talla la línia de baix a dos punts"]]),
    () => X.espai(12, { keepNext: true }),
    X.taulaResposta([10, 45, 45], ["", "Talla al… i al…", "Les solucions de … = 0"], [
      ["a)", ms("2 i 3"), ms(nb("x = 2 i x = 3"))],
      ["b)", "", ""], ["c)", "", ""], ["d)", "", ""],
    ]),
  ]),

  ...X.exercici(8, "Llegeix les dues gràfiques i completa la taula.", {}, [
    duo([["dofi", "Un dofí que salta fora de l'aigua.", "Paràbola del salt del dofí, que s'obre cap avall"],
         ["cable", "El cable d'un pont, sobre el riu.", "Paràbola del cable, que s'obre cap amunt i no toca el riu"]]),
    () => X.espai(12, { keepNext: true }),
    X.taulaResposta([8, 44, 24, 24], ["", "Pregunta", "El dofí", "El cable"], [
      ["a)", ms("On és el vèrtex?", undefined, { esq: true }), ms("(2 , 3)"), ms("(4 , 2)")],
      ["b)", txt("És el punt més alt o el més baix?"), "", ""],
      ["c)", txt("Quants punts de tall té?"), "", ""],
      ["d)", txt("On talla la línia de baix?"), "", ""],
    ]),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const LET = ["a) resolt", "b)", "c)", "d)"];
const solucionari = privat => [
  ...sol.titol(5),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Fita d'assoliment esperada: *AN*, i AE possible al criteri 5.1. És la unitat on més pot lluir.`,
    "*Com s'ha construït:* a cada exercici, l'apartat a) resolt com a model i tres apartats per fer, amb els ítems i les gràfiques de la fitxa (_fitxes/ud5.html_) i del seu solucionari. Sense les preguntes obertes de la fitxa (6f, 7c i 8e). Els apartats marcats «nou» no són a la fitxa: revisa'ls abans de fer servir l'examen.",
    "*No cal calcular res:* tot l'examen és lectura de gràfiques. Si fa servir la calculadora, és per comprovar, no per resoldre.",
  ]),

  sol.h3("1. Vèrtex i punts de tall — criteri 5.1"),
  ...sol.taula([19, 27, 27, 27], [
    ["", "Vèrtex", "Primer tall", "Segon tall"],
    ["a) resolt · pilota", "(1 , 5)", "0", "2"],
    ["b) sortidor", "*(2 , 2)*", "*0*", "*4*"],
    ["c) nou · bàsquet", "*(3 , 9)*", "*0*", "*6*"],
    ["d) nou · granota", "*(1 , 2)*", "*0*", "*2*"],
  ]),
  sol.p("*Error típic:* escriure les coordenades del vèrtex a l'inrevés, (5 , 1). És l'apartat a) de l'exercici 5."),

  sol.h3("2. La gràfica que s'obre cap amunt — criteri 5.1"),
  ...sol.taula([19, 51, 30], [
    ["", "Pregunta", "Resposta"],
    ["a) resolt", "Cap on s'obre?", "Cap amunt"],
    ["b)", "Quin és el vèrtex?", "*(4 , 4)*"],
    ["c)", "És el més alt o el més baix?", "*El més baix* (el cost mínim)"],
    ["d)", "Quants punts de tall té?", "*Cap*"],
  ]),
  sol.p("*És la regla trencada de la unitat.* Si respon «el més alt» o s'inventa dos talls, és que aplica el que ha vist a les paràboles que s'obren cap avall. Els apartats c) i d) compten per als nivells alts (AN, AE)."),

  sol.h3("3. Cap on s'obre"),
  sol.p("a) resolt: avall (−5)  ·  b) *amunt* (+1)  ·  c) *avall* (−0,5)  ·  d) *amunt* (+3)",
        { spacing: { before: X.tw(5), after: X.tw(8) } }),
  sol.p("Només cal mirar el signe. A l'apartat b), el «+1» no s'escriu: si dubta, pregunteu-li quin número hi ha davant de x²."),

  sol.h3("4. Què vol dir cada element — criteri 5.1"),
  sol.p("a) resolt: 2  ·  b) *1*  ·  c) *3*  ·  d) *4*", { spacing: { before: X.tw(5), after: X.tw(8) } }),

  sol.h3("5. Lectures correctes i incorrectes"),
  ...sol.taula([19, 41, 16, 24], [
    ["", "Diu", "Veredicte", "Per què"],
    ["a) resolt", "El vèrtex és (5 , 1)", "Malament", "Números canviats: és (1 , 5)."],
    ["b)", "Puja fins a 5 metres", "*Bé*", ""],
    ["c)", "Toca terra al segon 5", "*Malament*", "Toca terra al segon 2. El 5 són metres."],
    ["d)", "L'eix passa pel segon 1", "*Bé*", ""],
  ]),

  sol.h3("6. El coet"),
  ...sol.taula([19, 51, 30], [
    ["", "Pregunta", "Resposta"],
    ["a) resolt", "Altura màxima", "20 m"],
    ["b)", "Quan hi arriba", "*al segon 2*"],
    ["c)", "Quan torna a terra", "*al segon 4*"],
    ["d)", "Altura al segon 1", "*15 m*"],
  ]),
  sol.p("L'apartat d) es llegeix a la gràfica. Si voleu estirar-lo de paraula: al segon 3 també fa 15 m, perquè la corba és simètrica."),

  sol.h3("7. Els talls són les solucions — criteri 5.1"),
  ...sol.taula([19, 33, 24, 24], [
    ["", "Funció", "Talla al… i al…", "Solucions"],
    ["a) resolt", "y = x² − 5x + 6", "2 i 3", "x = 2 i x = 3"],
    ["b)", "y = x² − 4", "*−2 i 2*", "*x = −2 i x = 2*"],
    ["c) nou", "y = x² − 6x + 8", "*2 i 4*", "*x = 2 i x = 4*"],
    ["d) nou", "y = x² − 1", "*−1 i 1*", "*x = −1 i x = 1*"],
  ]),
  sol.p("L'apartat a) és l'equació que va comprovar a la Unitat 4 (exercici 6). Ara ho veu a la gràfica."),

  sol.h3("8. El dofí i el cable"),
  ...sol.taula([19, 37, 22, 22], [
    ["", "Pregunta", "El dofí", "El cable"],
    ["a) resolt", "Vèrtex", "(2 , 3)", "(4 , 2)"],
    ["b)", "Més alt o més baix", "*el més alt*", "*el més baix*"],
    ["c)", "Quants punts de tall", "*2*", "*cap*"],
    ["d)", "On talla", "*al 0 i al 4*", "*enlloc: no toca el riu*"],
  ]),
  sol.p("És la regla trencada de l'exercici 2 en una situació nova i sense avís: el cable s'obre cap amunt i no té cap tall."),

  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Tot l'examen → criteri *5.1*, llegir la gràfica i dir què vol dir cada element en el fenomen.",
    "El mínim (AS) és l'exercici 1 i l'exercici 3. Els exercicis 2 i 8 (el vèrtex que és un mínim, sense talls) compten per a AN i AE.",
  ]),
];

X.genera({ unitat: 5, alumnat, solucionari }).catch(e => { console.error(e.message); process.exit(1); });
