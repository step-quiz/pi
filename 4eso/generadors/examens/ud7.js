#!/usr/bin/env node
/*
  4eso/generadors/examens/ud7.js · examen de la Unitat 7 (Atzar i decisions)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a comu/examens/nucli.js i les
  regles, a comu/docs/EXAMENS-DOCX.md. El model és ud1.js.

      node 4eso/generadors/examens/ud7.js   →  4eso/docx/examen-ud7-alumnat.docx
                                                4eso/docx/examen-ud7-solucionari.docx

  D'on surt cada cosa:
  · Els apartats a), b), c) i d), dels exercicis de fitxes/ud7.html i del seu solucionari.
    On la fitxa no en tenia prou, n'hi ha un de nou, i al solucionari porta la marca «nou».
  · L'arbre de les dues monedes és el de la fitxa, llegit del seu marcador <!--grafic:NOM-->.
  · Sense les preguntes obertes de la fitxa (5f, 6f i 7e).
  · La regla trencada de la fitxa (4c, una cara i una creu val el doble) hi és, com a
    apartat c) de l'exercici 4, amb l'arbre al costat per comptar-hi les branques.
  Fet el 30/9/2026. Els apartats «nou», revisats el mateix dia per encàrrec del docent.
*/
"use strict";

const fs = require("fs");
const path = require("path");
const X = require("../../../comu/examens/nucli");
const { dada, ms, sol } = X;
const { AlignmentType } = X.docx;

const cal = (cond, msg) => { if (!cond) throw new Error("ud7.js: " + msg); };
const pc = x => (Math.round(x * 1000) / 10).toString().replace(".", ",") + " %";
const nb = s => s.replace(/(\d) (?=€|%)/g, "$1 ").replace(/(\d) ([×÷]) (?=\d)/g, "$1 $2 ");
const txt = s => dada(nb(s), undefined, { esq: true });
const LL = ["b)", "c)", "d)"];

const FITXA = fs.readFileSync(path.join(__dirname, "..", "..", "fitxes", "ud7.html"), "utf8");
const m = FITXA.match(/<!--grafic:ARBRE_MONEDES--><svg viewBox="0 0 ([\d.]+) ([\d.]+)"[^>]*>([\s\S]*?)<\/svg><!--\/grafic-->/);
cal(m, "l'arbre de les monedes no és a fitxes/ud7.html");
X.registra("arbre", X.SVG(`0 0 ${m[1]} ${m[2]}`, +m[1], +m[2], m[3]));
const ARBRE_CM = 11;

/* Un apartat solt amb les tres opcions de marcar a sota. */
function ambTria(etiqueta, frase, marcada, { primer = false, ultim = false } = {}) {
  X.anota(etiqueta);
  return [
    () => X.par([X.run(etiqueta, { size: X.mig(X.MIDA.etiqueta) }), X.run("  "),
                 X.run(frase, { size: X.mig(X.MIDA.etiqueta) })],
                { keepNext: true, spacing: { before: primer ? 0 : X.tw(X.AIRE.entreApartats), after: X.tw(6) } }),
    X.tria(["Impossible", "Pot passar", "Segur"], { marcada, seguir: !ultim }),
  ];
}

/* ------------------------------------------------------------ les dades -- */
const DAU = [["un 5", [5]], ["un parell", [2, 4, 6]], ["més de 4", [5, 6]], ["un número de l'1 al 6", [1, 2, 3, 4, 5, 6]]];
const ARBRE = [["Un menú amb 2 primers i 3 segons", 2, 3], ["Un menú amb 3 primers i 4 segons", 3, 4],
               ["Un codi de 2 xifres amb els números 1, 2 i 3", 3, 3], ["Tirar un dau i una moneda", 6, 2]];
const FIRA = { paga: 2, premi: 8, tirades: 60 };
const guanyades = FIRA.tirades / 6;
cal(guanyades === 10 && FIRA.tirades * FIRA.paga - guanyades * FIRA.premi === 40, "el joc de fira");
const RASCA = { vegades: 20, cada: 5, premi: 2 }, RULETA = { vegades: 20, cada: 4, premi: 3 };
const guanya = j => j.vegades / j.cada, cobra = j => guanya(j) * j.premi, perd = j => j.vegades - cobra(j);
cal(perd(RASCA) === 12 && perd(RULETA) === 5, "la rasca i la ruleta");

/* ------------------------------------------------------------- l'alumnat -- */
const alumnat = [
  ...X.exercici(1, "Marca si és impossible, si pot passar o si és segur.", {}, [
    ...ambTria("a)", "Treure un 7 amb un dau de 6 cares.", "Impossible", { primer: true }),
    ...ambTria("b)", "Treure un número parell amb un dau.", null),
    ...ambTria("c)", "Que un dau caigui mostrant un número de l'1 al 6.", null),
    ...ambTria("d)", "Treure una bola verda d'una bossa amb boles blanques i negres.", null, { ultim: true }),
  ]),

  ...X.exercici(2, "Compta les possibilitats amb l'arbre.", { calc: true }, [
    X.context("Multiplica: les branques del primer pas × les del segon pas."),
    X.taulaResposta([8, 62, 30], ["", "Quantes possibilitats hi ha?", "Compte"], [
      ["a)", ms(ARBRE[0][0], undefined, { esq: true }), ms(nb("2 × 3 = 6"))],
      ...ARBRE.slice(1).map(([s], i) => [LL[i], txt(s), ""]),
    ]),
  ]),

  ...X.exercici(3, "Calcula la probabilitat en tant per cent.", { calc: true }, [
    X.context("Amb un dau de 6 cares."),
    X.taulaResposta([8, 28, 15, 15, 16, 18], ["", "Vull treure…", "Em van bé", "Poden sortir", "Divisió", "%"], [
      ["a)", ms("un 5"), ms("1"), ms("6"), ms(nb("1 ÷ 6")), ms(nb("16,7 %"))],
      ...DAU.slice(1).map(([s], i) => [LL[i], txt(s), "", "", "", ""]),
    ]),
  ]),

  ...X.exercici(4, "Escriu quin dels dos fets és més probable.", { calc: true }, [
    X.context("L'arbre de dues monedes. Cada branca és una possibilitat."),
    () => X.par(X.imatge("arbre", ARBRE_CM, ARBRE_CM * +m[2] / +m[1], "Arbre de dues monedes amb quatre branques: cara-cara, cara-creu, creu-cara i creu-creu"),
                { alignment: AlignmentType.CENTER, keepNext: true }),
    () => X.espai(10, { keepNext: true }),
    X.taulaResposta([8, 62, 30], ["", "Quin és més probable?", "Resposta"], [
      ["a)", ms("Amb un dau: treure parell o treure un 6?", undefined, { esq: true }), ms("Treure parell")],
      ["b)", txt("Amb un dau: treure més de 2 o treure menys de 3?"), ""],
      ["c)", txt("Amb dues monedes: dues cares o una cara i una creu?"), ""],
      ["d)", txt("D'una bossa amb 3 boles blanques i 1 de negra: blanca o negra?"), ""],     // nou
    ]),
  ]),

  ...X.exercici(5, "Analitza aquest joc de fira.", { calc: true }, [
    X.context("Pagues 2 € per tirar un dau. Si surt un 6, et donen 8 €."),
    X.taulaResposta([8, 62, 30], ["", "Pregunta", "Resposta"], [
      ["a)", ms("Quina probabilitat hi ha de guanyar?", undefined, { esq: true }), ms(nb("16,7 %"))],
      ["b)", txt("Si tires 60 vegades, quantes en guanyaràs?"), ""],
      ["c)", txt("Quant hauràs pagat en 60 tirades?"), ""],
      ["d)", txt("Quant hauràs cobrat?"), ""],
    ]),
  ]),

  ...X.exercici(6, "Escriu si el missatge enganya o si diu la veritat.", {}, [
    X.taulaResposta([8, 62, 30], ["", "Algú diu…", "Enganya o és veritat?"], [
      ["a)", ms("«Ja han sortit 5 vermells seguits, ara toca negre.»", undefined, { esq: true }), ms("Enganya")],
      ["b)", txt("«Com més hi jugues, més possibilitats tens de guanyar.»"), ""],
      ["c)", txt("«Guanyar la loteria és molt difícil.»"), ""],
      ["d)", txt("«Aquest número no ha sortit mai, ara li toca.»"), ""],
    ]),
  ]),

  ...X.exercici(7, "Calcula què passa si hi jugues 20 vegades.", { calc: true }, [
    X.context("La rasca: cada butlleta val 1 €. 1 de cada 5 dona 2 €."),
    X.context("La ruleta d'un joc de mòbil: cada tirada val 1 moneda. 1 de cada 4 dona 3 monedes."),
    X.taulaResposta([8, 44, 24, 24], ["", "Pregunta", "La rasca", "La ruleta"], [
      ["a)", ms("Quant pagues en 20 vegades?", undefined, { esq: true }), ms(nb("20 €")), ms("20 monedes")],
      ["b)", txt("Quantes vegades guanyaràs?"), "", ""],
      ["c)", txt("Quant cobraràs?"), "", ""],
      ["d)", txt("Hi guanyes o hi perds? Quant?"), "", ""],
    ]),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const LET = ["a) resolt", "b)", "c)", "d)"];
const solucionari = privat => [
  ...sol.titol(7),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Fita d'assoliment esperada: *AS*, amb *AN* al recompte (criteris 1.1 i 2.1). Calculadora disponible a tot l'examen.`,
    "*Com s'ha construït:* a cada exercici, l'apartat a) resolt com a model i tres apartats per fer, amb els ítems de la fitxa (_fitxes/ud7.html_) i del seu solucionari. Sense les preguntes obertes de la fitxa (5f, 6f i 7e). Els apartats marcats «nou» no són a la fitxa; es van revisar el 30/9/2026 (el mateix tipus d'ítem que la fitxa, amb les xifres comprovades).",
    "*Els exercicis 5, 6 i 7* són el nucli de la unitat per a aquest alumnat: apostes, sortejos i jocs. Convé que els faci sencers encara que la resta hagi anat més just.",
  ]),

  sol.h3("1. Impossible, pot passar o segur"),
  sol.p("a) resolt: Impossible  ·  b) *Pot passar*  ·  c) *Segur*  ·  d) *Impossible*",
        { spacing: { before: X.tw(5), after: X.tw(8) } }),
  sol.p("L'apartat d) és el que costa més: si a la bossa no hi ha boles verdes, no en pot sortir cap."),

  sol.h3("2. Comptar amb l'arbre — criteri 2.1"),
  ...sol.taula([19, 51, 30], [["", "Situació", "Compte"]].concat(
    ARBRE.map(([s, p, q], i) => [LET[i], s, `${p} × ${q} = *${p * q}*`]))),
  sol.p("*Error típic a l'apartat c:* respondre 6 (sumant 3 + 3). Ajuda escriure la llista: 11, 12, 13, 21, 22, 23, 31, 32, 33."),

  sol.h3("3. Probabilitat amb el dau — criteri 1.1"),
  ...sol.taula([19, 29, 13, 13, 13, 13], [["", "Vull treure", "Bé", "Poden", "Divisió", "%"]].concat(
    DAU.map(([s, b], i) => [LET[i], s, String(b.length), "6", `${b.length} ÷ 6`, `*${pc(b.length / 6)}*`]))),
  sol.p("*Error típic a l'apartat c:* comptar el 4 dins de «més de 4». L'apartat d) és el fet segur de l'exercici 1: el 100 %."),

  sol.h3("4. Quin és més probable — criteri 1.1"),
  ...sol.taula([19, 51, 30], [
    ["", "Opcions", "Més probable"],
    ["a) resolt", "parell (50 %) o un 6 (16,7 %)", "Parell"],
    ["b)", "més de 2 (66,7 %) o menys de 3 (33,3 %)", "*Més de 2*"],
    ["c)", "dues cares (25 %) o una cara i una creu (50 %)", "*Una cara i una creu*"],
    ["d) nou", "blanca (75 %) o negra (25 %)", "*Blanca*"],
  ]),
  sol.p("*L'apartat c) és la regla trencada de la unitat.* Sembla que dues cares i «una de cada» haurien de ser igual de probables, però «una de cada» es pot donar de dues maneres: cara-creu i creu-cara. L'arbre és a la mateixa pàgina: només cal comptar-hi les branques. Compta per als nivells alts (AN, AE)."),

  sol.h3("5. El joc de fira — criteri 1.1"),
  ...sol.taula([19, 51, 30], [
    ["", "Pregunta", "Resposta"],
    ["a) resolt", "Probabilitat de guanyar", "1 ÷ 6 = 16,7 %"],
    ["b)", "Guanyades en 60 tirades", "*60 ÷ 6 = 10*"],
    ["c)", "Pagat en total", "*60 × 2 = 120 €*"],
    ["d)", "Cobrat", "*10 × 8 = 80 €*"],
  ]),
  sol.p("Hi perd 40 €. El joc sembla generós (8 € per 2 €, quatre vegades el que pagues) i tot i així s'hi perd: és la sensació que fan servir les apostes de veritat. Si voleu, pregunteu-li de paraula si li convé jugar-hi."),

  sol.h3("6. Els missatges"),
  ...sol.taula([19, 51, 30], [
    ["", "Missatge", "Veredicte"],
    ["a) resolt", "«Ara toca negre»", "Enganya: la ruleta no recorda res"],
    ["b)", "«Com més hi jugues, més possibilitats»", "*Enganya*: com més hi jugues, més hi perds"],
    ["c)", "«La loteria és molt difícil»", "*És veritat*"],
    ["d)", "«Ara li toca»", "*Enganya*: el bombo no recorda res"],
  ]),

  sol.h3("7. La rasca i la ruleta — criteri 1.1"),
  ...sol.taula([19, 37, 22, 22], [
    ["", "Pregunta", "La rasca", "La ruleta"],
    ["a) resolt", "Pagues en 20 vegades", "20 €", "20 monedes"],
    ["b)", "Vegades que guanyes", `*20 ÷ 5 = ${guanya(RASCA)}*`, `*20 ÷ 4 = ${guanya(RULETA)}*`],
    ["c)", "Cobres", `*${guanya(RASCA)} × 2 = ${cobra(RASCA)} €*`, `*${guanya(RULETA)} × 3 = ${cobra(RULETA)} monedes*`],
    ["d)", "Guanyes o perds", `*Perds ${perd(RASCA)} €*`, `*Perds ${perd(RULETA)} monedes*`],
  ]),
  sol.p("Totes dues perden, i és el que ha de veure: la casa sempre guanya. A la ruleta el premi sembla més gran (3 monedes), però també s'hi perd."),

  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Exercici 2 → criteri *2.1*, comptar amb l'arbre. És on pot arribar a *AN*.",
    "Exercicis 3, 4, 5 i 7 → criteri *1.1*, calcular la probabilitat i decidir.",
    "El mínim (AS) és l'exercici 1, els apartats b) del 2 i del 3 i l'exercici 5. L'apartat 4c compta per als nivells alts.",
  ]),
];

X.genera({ unitat: 7, alumnat, solucionari }).catch(e => { console.error(e.message); process.exit(1); });
