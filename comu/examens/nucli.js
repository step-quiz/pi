/*
  comu/examens/nucli.js · la maquinària comuna dels exàmens en DOCX
  ---------------------------------------------------------------------------
  Cada unitat té un fitxer amb el seu contingut (ud1.js, ud2.js…), a la carpeta
  generadors/examens/ del seu curs (4eso/, 1eso/), i aquest nucli
  hi posa tot el que no depèn de la unitat: la pàgina, la lletra, els grisos,
  les peces (capçalera d'exercici, taula de resposta, opcions per marcar…), els
  dibuixos calculats i les comprovacions.

  Abans de tocar res, llegiu comu/docs/EXAMENS-DOCX.md. Hi ha les decisions que el
  docent va prendre en revisar l'examen de la UD1 (23/9/2026) i el perquè de
  cada peça. Les regles d'aquí dalt en són la traducció a codi.

  Tot el que hi ha en aquest fitxer ha de passar 4eso/eines/comprova.py: ni el
  curs ni el diagnòstic no hi poden sortir. Van a generadors/examens-privat.json,
  dins de la carpeta del curs, que no es puja mai (.gitignore el deixa fora).
*/
"use strict";

const fs = require("fs");
const path = require("path");
const docx = require("docx");
const sharp = require("sharp");
const JSZip = require(require.resolve("jszip", { paths: [path.dirname(require.resolve("docx"))] }));

const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell, Footer,
  WidthType, BorderStyle, ShadingType, AlignmentType, VerticalAlign, HeightRule,
  TableLayoutType, LineRuleType, PageNumber, LevelFormat, HeadingLevel,
} = docx;

/* ARREL és la carpeta del curs de l'examen que s'executa: per a
   4eso/generadors/examens/ud1.js, és 4eso/. El nucli és a comu/ i serveix per a tots. */
const ARREL = path.resolve(path.dirname(require.main ? require.main.filename : process.argv[1]), "..", "..");

/* ---------------------------------------------------------- dades privades -- */
/* Curs i adaptació: només a l'examen imprès, mai al repositori. */
const PRIVAT_PER_DEFECTE = {
  curs: "",                                             // p. ex. el nom del grup
  adaptacio: "alumnat amb dificultats de tipus cognitiu",
};
function llegeixPrivat() {
  const f = path.join(ARREL, "generadors", "examens-privat.json");
  if (!fs.existsSync(f)) return { ...PRIVAT_PER_DEFECTE, fitxer: null };
  return { ...PRIVAT_PER_DEFECTE, ...JSON.parse(fs.readFileSync(f, "utf8")), fitxer: f };
}

/* ---------------------------------------------------------------- unitats -- */
const CM = 567;                                   // twips per centímetre
const tw = punts => Math.round(punts * 20);       // punts → twips
const mig = punts => Math.round(punts * 2);       // punts → mitjos punts
const REM = 12;                                   // 1 rem de l'HTML = 12 pt
const vuitens = px => Math.round(px * 0.75 * 8);  // gruix de vora: px → vuitens de punt

const PAGINA = { w: 11906, h: 16838 };            // A4
const MARGE = { top: 737, bottom: 1134, left: 794, right: 794, header: 454, footer: 510 };
const AMPLE = PAGINA.w - MARGE.left - MARGE.right;          // 10318 twips = 18,2 cm

/* Només grisos: la paleta de paper de css/tokens.css, més el D9D9D9 que el
   docent fa servir per ressaltar l'opció triada a l'apartat resolt. */
const G = {
  tinta: "000000", gris1: "333333", gris2: "5E5E5E", gris3: "8A8A8A",
  vora: "8A8A8A", voraSuau: "BFBFBF", fons1: "F2F2F2", fons2: "E4E4E4",
  triat: "D9D9D9", manuscrit: "3A3A3A", blanc: "FFFFFF",
};

/* LA LLETRA. El docent edita a Google Docs: les tres fonts hi són.
   · Verdana per al text imprès.
   · Caveat per a la lletra manuscrita de l'apartat resolt, a 20 pt.
   · Nova Mono quan el text manuscrit porta un signe que Caveat no té
     (α β θ π ← → ∆ ∑ √ ∞ ⋅): el docent la va triar per a «√7 = 2,6457513…». */
const LLETRA = "Verdana";
const MANUSCRITA = "Caveat";
const MANUSCRITA_SIMBOLS = "Nova Mono";
const SENSE_CAVEAT = /[αβθπ←→∆∑√∞⋅]/;

/* LES MIDES, tal com les va deixar el docent. */
const MIDA = {
  consigna: 15.5,    // en rodona, mai en negreta
  avis: 15.5,        // l'avís de la calculadora, en rodona
  taula: 15,         // text i etiquetes de les taules
  dada: 15,          // la dada de l'enunciat, en negreta
  arrel: 16,         // una arrel sola com a dada (√7, √5)
  manuscrita: 20,    // la lletra manuscrita (Caveat és petita: 20 pt fan com 15 de Verdana)
  capTaula: 11,      // capçalera de columna
  etiqueta: 14,      // a), b)… fora de les taules
  pastilla: 19,      // nombres per marcar
  frase: 13,         // la frase d'una situació
  xifra: 17,         // la xifra d'una situació i les opcions
  context: 13,       // la frase de context sota la consigna, en gris
  previ: 10.5,       // la capçalera de la pàgina 1
  peu: 10.5,
};

/* L'AIRE entre blocs, en punts. Amb un exercici per pàgina hi ha lloc, i el
   docent el va deixar més ample que a la primera versió. */
const AIRE = {
  abansExercici1: 36,   // de l'avís de la calculadora a l'exercici 1
  sotaConsigna: 20,     // de la consigna al cos de l'exercici
  entreApartats: 22,    // entre dos apartats que no van en una sola taula
  mateixaPagina: 32,    // entre dos exercicis que comparteixen pàgina
};

/* ------------------------------------------------------------------ vores -- */
const vora = (px, color) => ({ style: BorderStyle.SINGLE, size: vuitens(px), color });
const CAP = { style: BorderStyle.NONE, size: 0, color: G.blanc };
const quatre = b => ({ top: b, bottom: b, left: b, right: b });
const SENSE = { top: CAP, bottom: CAP, left: CAP, right: CAP, insideHorizontal: CAP, insideVertical: CAP };
const REIXA = b => ({ top: b, bottom: b, left: b, right: b, insideHorizontal: b, insideVertical: b });

/* --------------------------------------------------------------- dibuixos -- */
/* Tot dibuix va en SVG i amb un PNG a 300 ppp. Google Docs fa servir el PNG;
   Word, l'SVG. Els dibuixos es calculen, no es fan a ull. */
const SVG = (vb, w, h, cos) =>
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}" width="${w}" height="${h}">${cos}</svg>`;

const ICONES = {
  calc: SVG("0 0 48 48", 48, 48,
    `<rect x="7" y="3" width="34" height="42" rx="6" fill="#000"/>
     <rect x="12" y="8" width="24" height="12" rx="3" fill="#E4E4E4"/>
     <g fill="#B0B0B0"><circle cx="16" cy="27" r="3"/><circle cx="24" cy="27" r="3"/><circle cx="32" cy="27" r="3"/>
     <circle cx="16" cy="36" r="3"/><circle cx="24" cy="36" r="3"/><circle cx="32" cy="36" r="3"/></g>`),
  parla: SVG("0 0 48 48", 48, 48,
    `<path d="M6 9a4 4 0 0 1 4-4h28a4 4 0 0 1 4 4v20a4 4 0 0 1-4 4H21l-10 9V33h-1a4 4 0 0 1-4-4z"
      fill="#F2F2F2" stroke="#000" stroke-width="3" stroke-linejoin="round"/>`),
  talla: SVG("0 0 48 48", 48, 48,
    `<rect x="4" y="18" width="30" height="10" fill="#F2F2F2" stroke="#000" stroke-width="3"/>
     <path d="M4 28l4 5 4-5 4 5 4-5 4 5 4-5 4 5 2-5" fill="none" stroke="#000" stroke-width="3" stroke-linejoin="round"/>
     <rect x="34" y="16" width="10" height="14" rx="3" fill="#000"/>`),
  compra: SVG("0 0 48 48", 48, 48,
    `<path d="M17 15V11a7 7 0 0 1 14 0v4" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round"/>
     <path d="M9 15h30l-3 28H12z" fill="#F2F2F2" stroke="#000" stroke-width="3" stroke-linejoin="round"/>`),
};
const ALT_ICONA = { calc: "Calculadora", parla: "Bombolla de parlar: dir-ho", talla: "Serra: tallar", compra: "Bossa: comprar" };

/* La casella de marcar (1,4 rem, vora de 2,5 px). La marcada porta el senyal
   fet a mà. Totes dues tenen el mateix llenç, perquè quedin a la mateixa altura. */
const quadret = marcat => SVG("-2 -3 27 27", 27, 27,
  `<rect x="1.25" y="1.25" width="19.9" height="19.9" rx="3.75" fill="#fff" stroke="#000" stroke-width="2.5"/>` +
  (marcat ? `<path d="M3.83 10.58L9.25 17.08L22.25 -0.25" fill="none" stroke="#3A3A3A" stroke-width="3.8"
              stroke-linecap="round" stroke-linejoin="round"/>` : ""));

/* Recta numèrica de `de` a `fins`, amb la geometria de les fitxes: 640 × 100,
   de x = 40 a x = 600. Si hi ha marca, la creu cau exactament al valor. */
function svgRecta({ de = 0, fins = 6, marca = null, etiqueta = "" } = {}) {
  const X0 = 40, X1 = 598, U = (X1 - X0) / (fins - de);
  const f = v => (Math.round(v * 100) / 100).toString();
  let s = `<line x1="40" y1="48" x2="600" y2="48" stroke="#000" stroke-width="3"/>`;
  for (let i = de; i <= fins; i++) {
    const x = X0 + U * (i - de);
    s += `<line x1="${f(x)}" y1="36" x2="${f(x)}" y2="60" stroke="#000" stroke-width="3"/>` +
         `<text x="${f(x)}" y="86" font-family="${LLETRA}" font-size="19" fill="#5E5E5E" text-anchor="middle">${i}</text>`;
  }
  if (marca !== null) {
    const x = X0 + U * (marca - de);
    s += `<g stroke="#3A3A3A" stroke-width="3.5" stroke-linecap="round">` +
         `<line x1="${f(x - 8)}" y1="36" x2="${f(x + 8)}" y2="59"/><line x1="${f(x + 9)}" y1="35" x2="${f(x - 9)}" y2="60"/></g>` +
         `<text x="${f(x)}" y="26" text-anchor="middle" font-size="19" fill="#3A3A3A" ` +
         `font-family="${SENSE_CAVEAT.test(etiqueta) ? MANUSCRITA_SIMBOLS : MANUSCRITA}">${etiqueta}</text>`;
  }
  return SVG("0 0 640 100", 640, 100, s);
}

const REGISTRE = new Map();          // nom → { svg, png }
function registra(nom, svg) {
  if (!REGISTRE.has(nom)) REGISTRE.set(nom, { svg: Buffer.from(svg), png: null });
  return nom;
}
for (const [nom, svg] of Object.entries(ICONES)) registra(nom, svg);
registra("quadret", quadret(false));
registra("quadretMarcat", quadret(true));

async function preparaImatges() {
  for (const [nom, im] of REGISTRE) {
    if (im.png) continue;
    const svg = im.svg.toString();
    const amplePx = Number(svg.match(/ width="([\d.]+)"/)[1]);
    const escala = amplePx > 200 ? 2150 / amplePx : 8;              // ~300 ppp
    /* Amb fons transparent: sobre una cel·la grisa, un fons blanc es veuria com
       un quadrat (a Google Docs, que fa servir el PNG, passava). */
    const png = await sharp(im.svg, { density: 72 * escala }).png().toBuffer();
    const { data, info } = await sharp(png).ensureAlpha().raw().toBuffer({ resolveWithObject: true });
    for (let i = 0; i < data.length; i += info.channels) {
      if (data[i + 3] === 0) continue;
      if (Math.abs(data[i] - data[i + 1]) > 2 || Math.abs(data[i + 1] - data[i + 2]) > 2) {
        throw new Error(`el dibuix «${nom}» té píxels de color`);
      }
    }
    im.png = png;
  }
}

function imatge(nom, ampleCm, altCm, alt) {
  const im = REGISTRE.get(nom);
  if (!im || !im.png) throw new Error(`falta preparar el dibuix «${nom}»`);
  const px = cm => Math.round(cm / 2.54 * 96 * 100) / 100;
  return new ImageRun({
    type: "svg", data: im.svg, fallback: { type: "png", data: im.png },
    transformation: { width: px(ampleCm), height: px(altCm) },
    altText: { name: nom, title: alt, description: alt },
  });
}

/* ------------------------------------------------------------------ text -- */
/* Un tros de text es pot donar de tres maneres:
     "text"            imprès, en rodona
     dada("√5")        la dada de l'enunciat, en negreta (sobre gris a les taules)
     ms("2,6457513…")  la resposta ja feta, en lletra manuscrita               */
const dada = (text, mida, o = {}) => ({ tipus: "dada", text, mida, ...o });
const ms = (text, mida, o = {}) => ({ tipus: "ms", text, mida, ...o });

const run = (text, o = {}) => new TextRun({ text, ...o });
function runManuscrit(text, punts = MIDA.manuscrita) {
  const font = SENSE_CAVEAT.test(text) ? MANUSCRITA_SIMBOLS : MANUSCRITA;
  return new TextRun({ text, font, color: G.manuscrit, size: mig(punts) });
}
function runsDe(tros, midaBase) {
  if (tros === null || tros === undefined || tros === "") return [];
  if (typeof tros === "string") return [run(tros, { size: mig(midaBase) })];
  if (tros.tipus === "ms") return [runManuscrit(tros.text, tros.mida || MIDA.manuscrita)];
  if (tros.tipus === "dada") return [run(tros.text, { bold: true, size: mig(tros.mida || midaBase) })];
  throw new Error("tros de text desconegut");
}

const SIMPLE = { line: 240, lineRule: LineRuleType.AUTO };      // interlineat senzill, com a Google Docs
function par(children, o = {}) {
  return new Paragraph({ children: Array.isArray(children) ? children : [children], ...o,
                         spacing: { before: 0, after: 0, ...SIMPLE, ...(o.spacing || {}) } });
}

/* Espai vertical: un paràgraf buit amb lletra d'1 pt i «espai abans». Google Docs
   no respecta l'interlineat exacte (el converteix en un múltiple i els espais es
   disparen), però sí l'espai abans en punts. També separa dues taules seguides,
   que sense un paràgraf al mig Word les fondria. */
function espai(punts, o = {}) {
  return new Paragraph({ children: [], run: { size: 2 }, ...o,
                         spacing: { before: tw(punts), after: 0, ...SIMPLE } });
}
const salt = () => espai(0, { pageBreakBefore: true });

/* ---------------------------------------------------------------- taules -- */
function amples(percents, total = AMPLE) {
  const w = percents.map(p => Math.round(total * p / 100));
  w[w.length - 1] += total - w.reduce((a, b) => a + b, 0);
  return w;
}
function taula(columnes, files, o = {}) {
  return new Table({
    width: { size: columnes.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: columnes, layout: TableLayoutType.FIXED,
    borders: o.borders || SENSE, rows: files,
  });
}
function cela(children, o) {
  const opc = {
    children: Array.isArray(children) ? children : [children],
    width: { size: o.w, type: WidthType.DXA },
    verticalAlign: o.va || VerticalAlign.CENTER,
    margins: o.margins || { top: 0, bottom: 0, left: 0, right: 0 },
  };
  if (o.borders) opc.borders = o.borders;
  if (o.fons) opc.shading = { type: ShadingType.CLEAR, color: "auto", fill: o.fons };
  return new TableCell(opc);
}

/* -------------------------------------------------- registre d'apartats -- */
/* Cada peça anota els apartats que porta, i exercici() els assigna al seu
   número. Serveix per avisar si un exercici no té a), b), c) i d). */
let APARTATS_PENDENTS = [];
const EXERCICIS = [];
const anota = etiqueta => { APARTATS_PENDENTS.push(etiqueta.replace(/\W/g, "")); };

/* ----------------------------------------------------------- l'alumnat -- */
/* Les peces tornen funcions: el document es munta quan ja hi ha els PNG fets. */

/* Pàgina 1, a dalt: «Matemàtiques Aplicades [curs] · Unitat N». Ni «adaptat» ni
   títol: l'examen té l'aspecte d'un examen com els altres. */
function capcalera(unitat, curs) {
  const text = ["Matemàtiques Aplicades", curs].filter(Boolean).join(" ") + ` · Unitat ${unitat}`;
  return par(run(text, { size: mig(MIDA.previ), color: G.gris2, characterSpacing: 2 }), {
    border: { bottom: { style: BorderStyle.SINGLE, size: vuitens(1), color: G.voraSuau, space: 4 } },
    spacing: { after: tw(0.8 * REM) },
  });
}

function nomData() {
  const et = text => par(run(text, { size: mig(13), color: G.gris2 }));
  const ratlla = { top: CAP, left: CAP, right: CAP, bottom: vora(2, G.voraSuau) };
  const col = [900, Math.round(8 * CM), tw(2.2 * REM), 920, Math.round(3.4 * CM)];
  return taula(col, [new TableRow({ children: [
    cela(et("Nom:"), { w: col[0], va: VerticalAlign.BOTTOM }),
    cela(par([]), { w: col[1], va: VerticalAlign.BOTTOM, borders: ratlla }),
    cela(par([]), { w: col[2] }),
    cela(et("Data:"), { w: col[3], va: VerticalAlign.BOTTOM }),
    cela(par([]), { w: col[4], va: VerticalAlign.BOTTOM, borders: ratlla }),
  ] })]);
}

/* L'únic avís de l'examen. L'altre («l'apartat a) ja està fet») el docent el
   va treure: el model en lletra manuscrita ja ho diu tot sol. */
function avisCalculadora(text = "Pots fer servir la calculadora a tot l'examen.") {
  const b = vora(3, G.tinta);
  const pad = { top: tw(0.75 * REM), bottom: tw(0.75 * REM) };
  const wi = tw(1 * REM) + tw(3 * REM) + tw(0.9 * REM);
  return taula([wi, AMPLE - wi], [new TableRow({ cantSplit: true, children: [
    cela(par(imatge("calc", 1.27, 1.27, ALT_ICONA.calc)), { w: wi, fons: G.fons1,
      margins: { ...pad, left: tw(1 * REM), right: tw(0.9 * REM) }, borders: { top: b, bottom: b, left: b, right: CAP } }),
    cela(par(run(text, { size: mig(MIDA.avis) })), { w: AMPLE - wi, fons: G.fons1,
      margins: { ...pad, left: 0, right: tw(1 * REM) }, borders: { top: b, bottom: b, left: CAP, right: b } }),
  ] })]);
}

/* Capçalera d'exercici: el número dins d'un quadrat d'1 cm i la consigna al
   costat, en rodona. El quadrat és una taula petita dins de la cel·la: així no
   s'estira quan la consigna fa dues línies, ni a Word ni a Google Docs. La
   calculadora, quan hi és, va a sota del text. */
const COSTAT = tw(2.4 * REM);                                  // 576 twips = 1,02 cm
function tasca(n, consigna, calc) {
  const w2 = AMPLE - COSTAT;
  const quadrat = taula([COSTAT], [new TableRow({
    height: { value: COSTAT, rule: HeightRule.ATLEAST }, cantSplit: true,
    children: [cela(par(run(String(n), { bold: true, size: mig(18) }), { alignment: AlignmentType.CENTER, keepNext: true }),
      { w: COSTAT, borders: quatre(vora(3, G.tinta)) })],
  })]);
  const text = [par(run(consigna, { size: mig(MIDA.consigna) }), { keepNext: true, keepLines: true })];
  if (calc) {
    text.push(par(imatge("calc", 0.85, 0.85, "Calculadora: aquest exercici es pot fer amb calculadora"),
      { indent: { left: tw(0.4 * REM) }, spacing: { before: 40 }, keepNext: true }));
  }
  return taula([COSTAT, w2], [new TableRow({ cantSplit: true, children: [
    cela([quadrat, espai(0, { keepNext: true })], { w: COSTAT, va: VerticalAlign.TOP }),
    cela(text, { w: w2, va: VerticalAlign.TOP, margins: { top: tw(1.8), bottom: 0, left: tw(0.85 * REM), right: 0 } }),
  ] })]);
}

/* Un exercici sencer. Per defecte comença pàgina (decisió del docent: un
   exercici per pàgina); amb { mateixaPagina: true } va a sota de l'anterior. */
function exercici(n, consigna, opcions, cos) {
  const { calc = false, mateixaPagina = false } = opcions || {};
  EXERCICIS.push({ n, apartats: APARTATS_PENDENTS });
  APARTATS_PENDENTS = [];
  const inici = n === 1 ? [() => espai(AIRE.abansExercici1)]
              : mateixaPagina ? [() => espai(AIRE.mateixaPagina)] : [() => salt()];
  return [...inici, () => tasca(n, consigna, calc), () => espai(AIRE.sotaConsigna, { keepNext: true }), ...cos];
}

/* Taula de resposta. La primera fila és sempre l'apartat resolt (a), amb fons
   gris clar. Cel·les: "" és una casella buida per escriure-hi a mà (1,5 cm
   d'alçada), dada() és la dada de l'enunciat i ms() la resposta feta. */
const PAD = { top: tw(0.5 * REM), bottom: tw(0.5 * REM), left: tw(0.55 * REM), right: tw(0.55 * REM) };
function taulaResposta(percents, capcalera, files) {
  files.forEach(f => anota(String(f[0])));
  return () => {
    const col = amples(percents);
    const cap = new TableRow({ cantSplit: true, tableHeader: true, children: capcalera.map((t, i) =>
      cela(par(run(t, { bold: true, size: mig(MIDA.capTaula), color: G.gris1, characterSpacing: 4 }),
        { alignment: AlignmentType.CENTER, keepNext: true }), { w: col[i], fons: G.fons2, margins: PAD })) });
    const cos = files.map((f, r) => new TableRow({
      cantSplit: true,
      height: r > 0 ? { value: Math.round(1.5 * CM), rule: HeightRule.ATLEAST } : undefined,
      children: f.map((c, i) => {
        const esq = c && typeof c === "object" && c.esq;
        const fons = r === 0 || (c && c.tipus === "dada") ? G.fons1 : undefined;
        return cela(par(runsDe(c, MIDA.taula), {
          alignment: esq ? AlignmentType.LEFT : AlignmentType.CENTER, keepNext: r < files.length - 1,
        }), { w: col[i], fons, margins: PAD });
      }),
    }));
    return taula(col, [cap, ...cos], { borders: REIXA(vora(2, G.vora)) });
  };
}

/* Un apartat amb recta numèrica. L'etiqueta va en negreta perquè l'apartat
   no té cap caixa que el separi dels altres (el docent la va deixar així). */
function recta(etiqueta, enunciat, { marca = null, etiquetaMarca = "", de = 0, fins = 6, primer = false } = {}) {
  anota(etiqueta);
  const nom = registra(`recta_${de}_${fins}_${marca === null ? "buida" : marca.toFixed(6)}`,
                       svgRecta({ de, fins, marca, etiqueta: etiquetaMarca }));
  const alt = marca === null ? `Recta numèrica buida del ${de} al ${fins}`
    : `Recta numèrica del ${de} al ${fins} amb ${etiquetaMarca} ja marcat amb una creu`;
  return [
    () => par([run(etiqueta, { bold: true, size: mig(MIDA.etiqueta) }), run("\u00A0\u00A0", { size: mig(MIDA.etiqueta) }),
               ...runsDe(enunciat, MIDA.etiqueta)], { keepNext: true, spacing: { before: primer ? 0 : tw(AIRE.entreApartats) } }),
    () => par(imatge(nom, 18.2, 18.2 * 100 / 640, alt)),
  ];
}

/* Nombres per marcar. L'opció triada a l'apartat resolt porta fons gris i la
   vora fosca; la nota del costat, en lletra manuscrita. */
const ENC = { etiqueta: 624, pastilla: Math.round(2.5 * CM), buit: tw(1 * REM) };
function encercla(etiqueta, nombres, { triat = null, nota = null, seguir = true } = {}) {
  anota(etiqueta);
  return () => {
    const col = [ENC.etiqueta];
    const celes = [cela(par(run(etiqueta, { size: mig(MIDA.etiqueta) })), { w: ENC.etiqueta })];
    nombres.forEach(n => {
      const marcat = n === triat;
      celes.push(cela(par(run(n, { bold: true, size: mig(MIDA.pastilla) }), { alignment: AlignmentType.CENTER, keepNext: seguir }), {
        w: ENC.pastilla, fons: marcat ? G.triat : undefined,
        borders: quatre(marcat ? vora(2.5, G.manuscrit) : vora(2, G.voraSuau)),
        margins: { top: tw(0.5 * REM), bottom: tw(0.5 * REM), left: 0, right: 0 },
      }));
      col.push(ENC.pastilla);
      celes.push(cela(par([]), { w: ENC.buit }));
      col.push(ENC.buit);
    });
    const resta = AMPLE - col.reduce((a, b) => a + b, 0);
    col.push(resta);
    celes.push(cela(par(nota ? [runManuscrit(nota)] : []), { w: resta, margins: { top: 0, bottom: 0, left: tw(0.4 * REM), right: 0 } }));
    return taula(col, [new TableRow({ cantSplit: true, children: celes })]);
  };
}

/* Una situació: etiqueta, pictograma, frase curta i la xifra. */
function situacio(etiqueta, icona, frase, valor, { resolt = false } = {}) {
  anota(etiqueta);
  return () => {
    const col = [570, 900, 0, 3220];
    col[2] = AMPLE - col[0] - col[1] - col[3];
    const fons = resolt ? G.fons1 : undefined;
    const pad = { top: tw(0.8 * REM), bottom: tw(0.8 * REM) };
    const b = vora(2, G.voraSuau);
    return taula(col, [new TableRow({ cantSplit: true, children: [
      cela(par(run(etiqueta, { size: mig(MIDA.etiqueta) }), { keepNext: true }), { w: col[0], fons, margins: { ...pad, left: tw(0.9 * REM), right: 0 } }),
      cela(par(imatge(icona, 1.27, 1.27, ALT_ICONA[icona] || icona), { alignment: AlignmentType.CENTER, keepNext: true }),
        { w: col[1], fons, margins: { ...pad, left: 90, right: 90 } }),
      cela(par(run(frase, { size: mig(MIDA.frase) }), { keepNext: true }), { w: col[2], fons, margins: { ...pad, left: 90, right: 90 } }),
      cela(par(run(valor.replace(/ (?=m$|€$|L$)/, "\u00A0"), { bold: true, size: mig(MIDA.xifra) }),
        { alignment: AlignmentType.RIGHT, keepNext: true }), { w: col[3], fons, margins: { ...pad, left: 0, right: tw(0.9 * REM) } }),
    ] })], { borders: { top: b, bottom: b, left: b, right: b, insideHorizontal: CAP, insideVertical: CAP } });
  };
}

/* Les tres opcions de marcar. La ja marcada porta la vora negra de 3 px. */
function tria(opcions, { marcada = null, seguir = true } = {}) {
  return () => {
    const buit = tw(0.8 * REM);
    const w = Math.floor((AMPLE - 2 * buit) / 3);
    const col = [w, buit, w, buit, AMPLE - 2 * w - 2 * buit];
    const celes = [];
    opcions.forEach((o, i) => {
      const triada = o === marcada;
      celes.push(cela(par([
        imatge(triada ? "quadretMarcat" : "quadret", 0.714, 0.714, triada ? "Casella marcada" : "Casella per marcar"),
        run("\u00A0" + o, { bold: true, size: mig(MIDA.xifra) }),
      ], { alignment: AlignmentType.CENTER, keepNext: seguir }), {
        w: col[i * 2], borders: quatre(triada ? vora(3, G.tinta) : vora(2, G.vora)),
        margins: { top: tw(0.5 * REM), bottom: tw(0.5 * REM), left: tw(0.5 * REM), right: tw(0.5 * REM) },
      }));
      if (i < opcions.length - 1) celes.push(cela(par([]), { w: buit }));
    });
    return taula(col, [new TableRow({ cantSplit: true, children: celes })]);
  };
}

/* Situació + les seves tres opcions, amb l'aire que toca. */
function situacioAmbTria(etiqueta, icona, frase, valor, opcions, { marcada = null, primer = false, ultim = false } = {}) {
  return [
    () => espai(primer ? 0 : AIRE.entreApartats, { keepNext: true }),
    situacio(etiqueta, icona, frase, valor, { resolt: marcada !== null }),
    () => espai(0.6 * REM, { keepNext: true }),
    tria(opcions, { marcada, seguir: !ultim }),
  ];
}

function context(text) {
  return () => par(run(text, { size: mig(MIDA.context), color: G.gris2 }), { keepNext: true, spacing: { after: tw(0.5 * REM) } });
}

/* ------------------------------------------------------- el solucionari -- */
/* Per a l'adult: aquí sí que hi ha text seguit. */
const S = 11.5;
function marcat(text, base = {}) {             // *negreta* i _cursiva_
  const out = [];
  for (const tros of text.split(/(\*[^*]+\*|_[^_]+_)/)) {
    if (!tros) continue;
    if (tros.startsWith("*")) out.push(run(tros.slice(1, -1), { ...base, bold: true }));
    else if (tros.startsWith("_")) out.push(run(tros.slice(1, -1), { ...base, italics: true }));
    else out.push(run(tros, base));
  }
  return out;
}
const sol = {
  p: (text, o = {}) => () => new Paragraph({ children: marcat(text), style: "Sol", ...o }),
  h3: text => () => new Paragraph({ children: [run(text)], heading: HeadingLevel.HEADING_3 }),
  titol: unitat => [
    () => new Paragraph({ children: [run("Solucionari")], heading: HeadingLevel.HEADING_1 }),
    () => new Paragraph({ children: [run(`Examen · Unitat ${unitat} · full per al professorat`, { color: G.gris2 })],
                          style: "Sol", spacing: { before: tw(2), after: 0 } }),
    () => espai(0.8 * REM),
  ],
  caixa: textos => [() => taula([AMPLE], [new TableRow({ cantSplit: true, children: [cela(
    textos.map((t, i) => new Paragraph({ children: marcat(t), style: "Sol",
                                         spacing: { after: i < textos.length - 1 ? tw(0.4 * REM) : 0 } })),
    { w: AMPLE, borders: quatre(vora(2, G.tinta)),
      margins: { top: tw(0.6 * REM), bottom: tw(0.6 * REM), left: tw(0.8 * REM), right: tw(0.8 * REM) } })] })]),
    () => espai(10)],
  taula: (percents, files) => [() => {
    const col = amples(percents);
    const pad = { top: tw(0.32 * REM), bottom: tw(0.32 * REM), left: tw(0.5 * REM), right: tw(0.5 * REM) };
    return taula(col, files.map((f, r) => new TableRow({
      cantSplit: true, tableHeader: r === 0,
      children: f.map((c, i) => cela(new Paragraph({ children: r === 0 ? [run(c, { bold: true, color: G.gris1 })] : marcat(c),
        style: "SolTaula", keepNext: r < files.length - 1 }), { w: col[i], fons: r === 0 ? G.fons2 : undefined, margins: pad })),
    })), { borders: REIXA(vora(2, G.vora)) });
  }, () => espai(10)],
  vinyetes: textos => textos.map((t, i) => () => new Paragraph({ children: marcat(t), style: "Sol",
    numbering: { reference: "vinyetes", level: 0 }, spacing: { before: 0, after: i === textos.length - 1 ? tw(10) : 0 } })),
};

/* ------------------------------------------------------------ document -- */
function document({ titol, tema, mida, fills, peu }) {
  const seccio = {
    properties: { page: { size: { width: PAGINA.w, height: PAGINA.h }, margin: peu ? MARGE : { ...MARGE, bottom: 737 } } },
    children: fills,
  };
  /* Peu: «pàgina N de M», com el va deixar el docent. Cada tros en un run
     propi: si els camps comparteixen run amb el text, LibreOffice perd el format. */
  const fmt = { size: mig(MIDA.peu), color: G.gris3 };
  if (peu) seccio.footers = { default: new Footer({ children: [new Paragraph({
    children: [new TextRun({ text: "pàgina ", ...fmt }), new TextRun({ children: [PageNumber.CURRENT], ...fmt }),
               new TextRun({ text: " de ", ...fmt }), new TextRun({ children: [PageNumber.TOTAL_PAGES], ...fmt })],
    run: fmt, style: "Peu",
    border: { top: { style: BorderStyle.SINGLE, size: vuitens(1), color: G.voraSuau, space: 10 } },
  })] }) };

  /* Els estils de títol de Word vénen en blau: aquí tots van en negre. */
  return new Document({
    creator: "Matemàtiques Aplicades · material adaptat", title: titol, subject: tema,
    description: "Generat amb comu/examens/nucli.js (comu/docs/EXAMENS-DOCX.md).",
    styles: {
      default: {
        document: { run: { font: LLETRA, size: mig(mida), color: G.tinta, language: { value: "ca-ES" } },
                    paragraph: { spacing: { before: 0, after: 0, ...SIMPLE } } },
        title: { run: { font: LLETRA, color: G.tinta } },
        heading1: { run: { font: LLETRA, bold: true, size: mig(19), color: G.tinta }, paragraph: { keepNext: true, spacing: { before: 0, after: 0 } } },
        heading2: { run: { font: LLETRA, bold: true, size: mig(15), color: G.tinta }, paragraph: { keepNext: true } },
        heading3: { run: { font: LLETRA, bold: true, size: mig(13.5), color: G.tinta },
                    paragraph: { keepNext: true, keepLines: true, spacing: { before: tw(4), after: tw(5), ...SIMPLE } } },
        heading4: { run: { font: LLETRA, bold: true, color: G.tinta } },
        heading5: { run: { font: LLETRA, color: G.tinta } },
        heading6: { run: { font: LLETRA, color: G.tinta } },
        hyperlink: { run: { color: G.tinta, underline: {} } },
      },
      paragraphStyles: [
        { id: "Peu", name: "Peu de l'examen", basedOn: "Normal", quickFormat: true,
          run: { size: mig(MIDA.peu), color: G.gris3 } },
        { id: "Sol", name: "Text del solucionari", basedOn: "Normal", next: "Sol", quickFormat: true,
          run: { size: mig(S) }, paragraph: { spacing: { before: 0, after: tw(8), line: 300, lineRule: LineRuleType.AUTO } } },
        { id: "SolTaula", name: "Taula del solucionari", basedOn: "Normal", quickFormat: true,
          run: { size: mig(S) }, paragraph: { spacing: { before: 0, after: 0, line: 276, lineRule: LineRuleType.AUTO } } },
      ],
    },
    numbering: { config: [{ reference: "vinyetes", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•",
      alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: tw(1.2 * REM) + 60, hanging: tw(1.2 * REM) - 40 } } } }] }] },
    sections: [seccio],
  });
}

const aplana = blocs => blocs.flat(Infinity).map(b => (typeof b === "function" ? b() : b)).flat(Infinity);

/* -------------------------------------------------------- comprovacions -- */
/* Blanc i negre: cap color amb R, G i B diferents, ni al text ni als dibuixos. */
function cromatics(text) {
  const out = new Set();
  for (const m of text.matchAll(/(?:w:(?:color|fill|val)="|#)([0-9A-Fa-f]{6})\b/g)) {
    const [r, g, b] = [0, 2, 4].map(i => parseInt(m[1].slice(i, i + 2), 16));
    if (!(r === g && g === b)) out.add(m[1]);
  }
  return [...out];
}

/* Llenguatge: el que el docent va canviar a la UD1. Són avisos, no errors,
   llevat d'«adaptat», que l'alumnat no ha de veure mai. */
const LLENGUATGE = [
  [/\badaptat/i, "error", "l'alumnat no ha de veure «adaptat»"],
  [/\bsencer(s|a|es)?\b/i, "avís", "en matemàtiques, «enter», «enters», «enteres»"],
  [/\bencercla\b/i, "avís", "el docent fa servir «Marca»"],
  [/\bquant fa\b/i, "avís", "un verb literal: «quant mesura», «quant costa»"],
  [/\bho \w+ries\b|\bho \w+ria\b/i, "avís", "sense pronoms febles: digues què"],
  [/\bnomés fas\b/i, "avís", "l'avís de «només fas el b)» ja no hi va"],
];
function revisaText(text) {
  const trobats = [];
  for (const [re, grau, consell] of LLENGUATGE) {
    const m = text.match(re);
    if (m) trobats.push(`${grau === "error" ? "ERROR" : "avís"}: «${m[0]}» → ${consell}`);
  }
  return trobats;
}

async function desa(doc, desti, { alumnat = false } = {}) {
  const buf = await Packer.toBuffer(doc);
  const zip = await JSZip.loadAsync(buf);
  /* Retocs que docx-js no sap fer: la casella centrada amb el text (Word), i la
     taula de fonts dient que Caveat és manuscrita, per si l'ordinador no la té. */
  let xml = await zip.file("word/document.xml").async("string");
  xml = xml.replace(/<w:p>(?:(?!<\/w:p>)[\s\S])*?<\/w:p>/g, p => !p.includes('name="quadret') ? p :
    p.replace('<w:jc w:val="center"/>', '<w:jc w:val="center"/><w:textAlignment w:val="center"/>'));
  zip.file("word/document.xml", xml);
  let fonts = await zip.file("word/fontTable.xml").async("string");
  fonts = fonts.replace(/<w:fonts([^>]*?)\s*\/>\s*$/, `<w:fonts$1>` +
    `<w:font w:name="${LLETRA}"><w:panose1 w:val="020B0604030504040204"/><w:charset w:val="00"/><w:family w:val="swiss"/><w:pitch w:val="variable"/></w:font>` +
    `<w:font w:name="${MANUSCRITA}"><w:charset w:val="00"/><w:family w:val="script"/><w:pitch w:val="variable"/></w:font>` +
    `<w:font w:name="${MANUSCRITA_SIMBOLS}"><w:charset w:val="00"/><w:family w:val="modern"/><w:pitch w:val="fixed"/></w:font></w:fonts>`);
  zip.file("word/fontTable.xml", fonts);
  const sortida = await zip.generateAsync({ type: "nodebuffer", compression: "DEFLATE" });

  const z2 = await JSZip.loadAsync(sortida);
  const parts = Object.keys(z2.files).filter(n => /^word\/.*\.xml$/.test(n));
  const xmls = await Promise.all(parts.map(n => z2.file(n).async("string")));
  const svgs = [...REGISTRE.values()].map(i => i.svg.toString()).join("\n");
  const colors = [...new Set([...xmls.flatMap(cromatics), ...cromatics(svgs)])];
  if (colors.length) throw new Error(`${path.basename(desti)}: hi ha colors que no són grisos: ${colors.join(", ")}`);

  const avisos = [];
  if (alumnat) {
    const text = (await z2.file("word/document.xml").async("string")).replace(/<[^>]+>/g, "");
    avisos.push(...revisaText(text));
    for (const e of EXERCICIS) {
      const esperat = ["a", "b", "c", "d"];
      if (e.apartats.join() !== esperat.join()) avisos.push(`avís: l'exercici ${e.n} té ${e.apartats.join(", ") || "cap apartat"} (el model en porta a, b, c i d)`);
    }
  }
  fs.mkdirSync(path.dirname(desti), { recursive: true });
  fs.writeFileSync(desti, sortida);
  return avisos;
}

/* ------------------------------------------------------------------ tot -- */
/* genera({ unitat, alumnat, solucionari }) fa els dos DOCX a docx/ (o a la carpeta
   que es passi com a primer argument de la línia d'ordres). */
async function genera({ unitat, alumnat, solucionari }) {
  const privat = llegeixPrivat();
  const carpeta = process.argv[2] ? path.resolve(process.argv[2]) : path.join(ARREL, "docx");
  await preparaImatges();
  const cap = [() => capcalera(unitat, privat.curs), () => espai(1 * REM), () => nomData(),
               () => espai(1.3 * REM), () => avisCalculadora()];
  const docA = document({ titol: `Examen · Unitat ${unitat}`, tema: `Matemàtiques Aplicades · Unitat ${unitat} · alumnat`,
                          mida: 14, fills: aplana([...cap, ...alumnat, () => espai(1)]), peu: true });
  const docS = document({ titol: `Solucionari · Examen Unitat ${unitat}`, tema: `Matemàtiques Aplicades · Unitat ${unitat} · professorat`,
                          mida: S, fills: aplana(solucionari(privat)), peu: false });
  const a = path.join(carpeta, `examen-ud${unitat}-alumnat.docx`);
  const s = path.join(carpeta, `examen-ud${unitat}-solucionari.docx`);
  const avisos = await desa(docA, a, { alumnat: true });
  await desa(docS, s);
  console.log(`Fets, en blanc i negre (dades privades: ${privat.fitxer ? path.relative(ARREL, privat.fitxer) : "cap, versió anònima"}):`);
  console.log("  " + path.relative(process.cwd(), a));
  console.log("  " + path.relative(process.cwd(), s));
  if (avisos.length) { console.log("\nRevisa:"); avisos.forEach(x => console.log("  " + x)); }
  if (avisos.some(x => x.startsWith("ERROR"))) process.exitCode = 1;
}

module.exports = {
  // l'examen
  genera, exercici, taulaResposta, recta, encercla, situacioAmbTria, situacio, tria, context,
  dada, ms, sol,
  // per fer peces noves (UD2: cadena de baules, barra de preu, tiquet…)
  par, run, runManuscrit, runsDe, espai, salt, taula, cela, amples, imatge, registra, SVG, svgRecta,
  vora, quatre, CAP, SENSE, REIXA, G, MIDA, AIRE, AMPLE, CM, REM, tw, mig, anota,
  LLETRA, MANUSCRITA, MANUSCRITA_SIMBOLS, SENSE_CAVEAT,
  docx,
};
