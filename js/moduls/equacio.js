/* EQUACIONS: LA BALANÇA — mòdul «equacio» de la caixa d'eines.
   Es registra sol; app.js no en sap res més que l'identificador. */
(function () {
  "use strict";
  const { $, $$, num, fix, euros, el, icona, pastilles, memoria } = CE;

  /* La balança és el model visual de 2n ESO amb què entra l'equació. Aquí no
     s'aïlla la incògnita: es PROVA un valor i es mira de quina banda cau, que és
     comprovar. Comprovar és substituir i comparar, i això sí que ho pot fer bé.
     Els casos són els mateixos que els exercicis 2, 3 i 6 de la fitxa. */
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
  let eq = EQUACIONS[0], eqX = 4;

  function pintaBalanca() {
    const svg = $("#eq-svg"); svg.textContent = "";
    const E = eq.esq(eqX), D = eq.dre(eqX), dif = E - D;
    const cx = 330, cy = 76, L = 248;

    // angle amb saturació: una diferència enorme no ha de fer capgirar el dibuix
    const graus = 13 * dif / (Math.abs(dif) + 5);
    const r = graus * Math.PI / 180;
    const xe = cx - L * Math.cos(r), ye = cy + L * Math.sin(r);
    const xd = cx + L * Math.cos(r), yd = cy - L * Math.sin(r);

    const peu = "var(--etiqueta-3)", tinta = "var(--etiqueta)";
    // columna i base
    svg.appendChild(el("rect", { x: cx - 8, y: cy, width: 16, height: 150, style: "fill:" + peu }));
    svg.appendChild(el("rect", { x: cx - 62, y: 226, width: 124, height: 16, rx: 6, style: "fill:" + peu }));
    // biga
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
    plat(xe, ye, E, eq.mostra(eqX), dif > 0);
    plat(xd, yd, D, eq.et.split("=")[1].trim(), dif < 0);

    $("#eq-valor").textContent = eqX;
    const avis = $("#eq-avis");
    if (Math.abs(dif) < 1e-9) {
      avis.className = "avis be";
      avis.innerHTML = "<b>Funciona.</b> Les dues bandes valen " + num(E, 2) + ".";
    } else {
      avis.className = "avis pensa";
      avis.textContent = "No funciona. Pesa més la banda " + (dif > 0 ? "esquerra" : "dreta") + ".";
    }
    $("#eq-menys").disabled = eqX <= eq.min;
    $("#eq-mes").disabled   = eqX >= eq.max;
  }

  function iniciaEquacio() {
    if ($("#eq-pastilles").children.length) return;
    pastilles($("#eq-pastilles"), EQUACIONS, e => {
      eq = e;
      eqX = e.model ?? e.min;
      $("#eq-marca").hidden = e.model === undefined;
      $("#eq-titol").textContent = eq.et;
      pintaBalanca();
    });
    $("#eq-menys").onclick = () => { if (eqX > eq.min) { eqX--; pintaBalanca(); } };
    $("#eq-mes").onclick   = () => { if (eqX < eq.max) { eqX++; pintaBalanca(); } };
    $("#eq-titol").textContent = eq.et;
    pintaBalanca();
  }

  CE.registra("equacio", iniciaEquacio);
})();
