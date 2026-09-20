/* EQUACIONS: LA BALANÇA — mòdul «equacio» de la caixa d'eines.
   Es registra sol; app.js no en sap res més que l'identificador. */
(function () {
  "use strict";
  const { $, $$, num, el, txt, omplirTextos, retroaccio } = CE;

  /* La balança és el model visual de 2n ESO amb què entra l'equació. Aquí no
     s'aïlla la incògnita: es PROVA un valor i es mira de quina banda cau, que és
     comprovar. Comprovar és substituir i comparar, i això sí que ho pot fer bé.
     Els casos són els mateixos que els exercicis 2, 3 i 6 de la fitxa.

     PROVAR NO ÉS CONTESTAR. Per això aquí no surt mai «Incorrecte»: un valor
     que no equilibra la balança es diu tal com és, «x = 2 no és una solució»,
     amb la banda que pesa més. La pista es calcula: compara les dues bandes a
     x − 1 i a x + 1 i diu cap on queden més iguals. Així és certa també a les
     equacions de segon grau, on «més gran» no sempre vol dir «més a prop».

     EL FINAL. Cada equació és una tasca tancada: «Solucions trobades: 1 de 2».
     Quan les ha trobades totes, surt el resum amb el codi de verificació. */

  /* `mostra` escriu la banda esquerra amb el número ja substituït. Cal que sigui
     una funció pròpia de cada equació: no es pot fer amb un reemplaçament de
     text, perquè «2x» amb x=4 donaria «24» en comptes de «2 × 4». */
  const par = x => (x < 0 ? "(" + x + ")" : String(x));
  const EQUACIONS = [
    { et: "x + 3 = 7",  esq: x => x + 3, dre: () => 7,  min: 0,  max: 10, model: 4,
      mostra: x => par(x) + " + 3" },
    { et: "x + 5 = 12", esq: x => x + 5, dre: () => 12, min: 0,  max: 14,
      mostra: x => par(x) + " + 5" },
    { et: "2x = 10",    esq: x => 2 * x, dre: () => 10, min: 0,  max: 10,
      mostra: x => "2 × " + par(x) },
    { et: "x² = 36",    esq: x => x * x, dre: () => 36, min: -8, max: 8,
      mostra: x => par(x) + "²" },
    { et: "x² − 5x + 6 = 0", esq: x => x * x - 5 * x + 6, dre: () => 0, min: -1, max: 6,
      mostra: x => par(x) + "² − 5×" + par(x) + " + 6" }
  ];
  let eq = EQUACIONS[0], eqX = 4, tasca = null;
  let trobades = [], proves = 0;

  const dif = x => eq.esq(x) - eq.dre(x);
  const esSolucio = x => Math.abs(dif(x)) < 1e-9;
  /** Les solucions senceres dins del rang dels botons: el que es pot trobar. */
  const solucions = e => {
    const s = [];
    for (let x = e.min; x <= e.max; x++) if (Math.abs(e.esq(x) - e.dre(x)) < 1e-9) s.push(x);
    return s;
  };
  /** «Prova un número més gran» o «més petit», segons on les bandes queden més
      iguals. Si queden igual de lluny a les dues bandes, les dues valen; es diu
      «més gran» per no deixar la pista en blanc. */
  function pistaDe(x) {
    const a = x - 1 >= eq.min ? Math.abs(dif(x - 1)) : Infinity;
    const b = x + 1 <= eq.max ? Math.abs(dif(x + 1)) : Infinity;
    if (a === Infinity && b === Infinity) return "";
    return txt(b <= a ? "6.p_mes" : "6.p_menys");
  }

  function pintaBalanca() {
    const svg = $("#eq-svg"); svg.textContent = "";
    const E = eq.esq(eqX), D = eq.dre(eqX), d = E - D;
    const cx = 330, cy = 76, L = 248;

    // angle amb saturació: una diferència enorme no ha de fer capgirar el dibuix
    const graus = 13 * d / (Math.abs(d) + 5);
    const r = graus * Math.PI / 180;
    const xe = cx - L * Math.cos(r), ye = cy + L * Math.sin(r);
    const xd = cx + L * Math.cos(r), yd = cy - L * Math.sin(r);

    const peu = "var(--etiqueta-3)", tinta = "var(--etiqueta)";
    svg.appendChild(el("rect", { x: cx - 8, y: cy, width: 16, height: 150, style: "fill:" + peu }));
    svg.appendChild(el("rect", { x: cx - 62, y: 226, width: 124, height: 16, rx: 6, style: "fill:" + peu }));
    svg.appendChild(el("line", { x1: xe, y1: ye, x2: xd, y2: yd, style: "stroke:" + tinta,
      "stroke-width": 7, "stroke-linecap": "round" }));
    svg.appendChild(el("circle", { cx, cy, r: 9, style: "fill:" + tinta }));

    // dos plats, penjant rectes des dels extrems
    const plat = (px, py, valor, etiqueta, mesPesat) => {
      const baix = py + 62;
      svg.appendChild(el("line", { x1: px, y1: py, x2: px, y2: baix,
        style: "stroke:" + peu, "stroke-width": 3 }));
      svg.appendChild(el("path", { d: "M " + (px - 72) + " " + baix + " h 144 l -14 22 h -116 z",
        style: "fill:var(--camp);stroke:" + peu, "stroke-width": 2, "stroke-linejoin": "round" }));
      svg.appendChild(el("text", { x: px, y: baix - 14, "text-anchor": "middle", "font-size": 15,
        style: "fill:var(--etiqueta-2)", "font-family": "inherit" }, etiqueta));
      svg.appendChild(el("text", { x: px, y: baix + 60, "text-anchor": "middle", "font-size": 34,
        "font-weight": 700, "font-family": "inherit",
        style: "fill:" + (mesPesat ? "var(--vermell)" : tinta) }, num(valor, 2)));
    };
    plat(xe, ye, E, eq.mostra(eqX), d > 0);
    plat(xd, yd, D, eq.et.split("=")[1].trim(), d < 0);

    $("#eq-valor").textContent = eqX;
    const avis = $("#eq-avis");
    if (eq.model !== undefined && eqX === eq.model) {
      retroaccio(avis, "be", txt("6.exemple", { x: eqX }));
    } else if (esSolucio(eqX)) {
      retroaccio(avis, "be", txt("6.es_sol", { x: par(eqX), v: num(E, 2) }));
    } else {
      retroaccio(avis, "no", txt("6.no_sol", { x: par(eqX),
        banda: txt(d > 0 ? "6.esquerra" : "6.dreta") }), pistaDe(eqX));
    }
    $("#eq-menys").disabled = eqX <= eq.min;
    $("#eq-mes").disabled   = eqX >= eq.max;
  }

  /** Cada vegada que es mou la x és una prova. Si és una solució que encara no
      havia sortit, compta com a trobada i avança el comptador. */
  function mou(pas) {
    const nou = eqX + pas;
    if (nou < eq.min || nou > eq.max) return;
    eqX = nou;
    const e = tasca.estat();
    if (eq.model === undefined && e && !e.acabada) {
      proves++;
      if (esSolucio(eqX) && !trobades.includes(eqX)) {
        trobades.push(eqX);
        tasca.anota("be");
        tasca.seguent();                  // a l'última solució, això acaba la tasca
      }
    }
    pintaBalanca();
  }

  function triaEquacio(e) {
    eq = e;
    $("#eq-marca").hidden = e.model === undefined;
    $("#eq-titol").textContent = eq.et;
    // l'exemple no es fa: ja ve resolt, i no té comptador ni final
    $("#eq-recorregut").hidden = e.model !== undefined;
    $("#eq-final").hidden = true;
    if (e.model !== undefined) { eqX = e.model; pintaBalanca(); return; }
    // aquesta funció també és la de «Torna a començar» del resum
    tasca.comenca(() => {
      eqX = eq.min; trobades = []; proves = 0;
      return { total: solucions(eq).length, cas: EQUACIONS.indexOf(eq) };
    });
  }

  function iniciaEquacio() {
    if ($("#eq-pastilles").children.length) return;
    omplirTextos($("#mod-equacio"));

    tasca = CE.tasca({
      tasca: 6,
      recorregut: $("#eq-recorregut"),
      final: $("#eq-final"),
      cos: [$("#eq-cos")],
      comptador: "6.trobades",
      ambPasActual: false,             // aquí no hi ha «pas d'ara»: es busca lliurement
      amagaEnAcabar: false,            // la balança es queda i es pot continuar provant
      desa: false,
      nom: e => txt("6.titol") + " · " + EQUACIONS[e.cas].et,
      pinta: () => pintaBalanca(),
      resum: e => {
        const llista = trobades.slice().sort((a, b) => a - b).map(x => "x = " + x);
        const junta = llista.length > 1
          ? llista.slice(0, -1).join(", ") + " i " + llista[llista.length - 1] : llista[0];
        return {
          frase: txt(llista.length > 1 ? "6.solucions" : "6.solucio", { llista: junta }),
          files: [[txt("6.r_solucions"), trobades.length], [txt("6.r_proves"), proves]],
          codi: { a: trobades.length, b: proves, c: 0 }
        };
      }
    });

    CE.pastilles($("#eq-pastilles"), EQUACIONS, triaEquacio);
    $("#eq-menys").onclick = () => mou(-1);
    $("#eq-mes").onclick   = () => mou(+1);
    triaEquacio(EQUACIONS[0]);
  }

  CE.registra("equacio", iniciaEquacio);
  CE.registraCataleg("6", { nom: txt("6.titol"), casos: EQUACIONS.map(e => e.et),
                            recomptes: [txt("6.r_solucions"), txt("6.r_proves")] });
})();
