/* APLANAR — mòdul «mitjana» de la caixa d'eines (U6).
   Es registra sol; app.js no en sap res més que l'identificador.

   La mitjana com a aplanar abans que com a «sumar i dividir», com a la pàgina 3
   de la fitxa de la U6 i els cinc minuts de fitxes o taps a l'aula de suport.
   Cada dada és una columna de blocs. «Passa un bloc» en mou un de la columna més
   alta a la més baixa, fins que totes fan igual: aquella altura és la mitjana.
   La silueta discontínua guarda com estaven, perquè es vegi d'on ha sortit cada bloc.

   Els casos tenen la mitjana sencera, com el dibuix de la fitxa: el gest de
   repartir s'ha d'acabar amb totes les columnes iguals. El compte amb números
   (la suma i la divisió) només surt quan ja està aplanat. */
(function () {
  "use strict";
  const { $, num, el, pastilles, txt, omplirTextos } = CE;

  const CASOS = [
    { et: "Gols",       model: true, dades: [0, 1, 1, 1, 2, 2, 3, 4, 4] },   // la fitxa, p. 3
    { et: "Jugadora A",              dades: [4, 5, 5, 5, 5, 6] },            // la fitxa, p. 1
    { et: "Jugadora B",              dades: [1, 3, 5, 5, 7, 9] }
  ];
  let cas = CASOS[0], ara = [];

  const pla = () => Math.max(...ara) - Math.min(...ara) <= 0;

  function passaUn() {
    if (pla()) return;
    const alt = ara.indexOf(Math.max(...ara));
    const baix = ara.indexOf(Math.min(...ara));
    ara[alt]--; ara[baix]++;
  }

  function pinta() {
    const svg = $("#mj-svg"); svg.textContent = "";
    const n = ara.length, max = Math.max(...cas.dades);
    const base = 250, cel = Math.min(46, 200 / Math.max(max, 1)), amp = Math.min(56, 560 / n);
    const x0 = (660 - n * amp) / 2;

    // la línia de terra
    svg.appendChild(el("line", { x1: x0 - 10, y1: base, x2: x0 + n * amp + 10, y2: base,
      style: "stroke:var(--etiqueta)", "stroke-width": 3 }));
    ara.forEach((v, i) => {
      const x = x0 + i * amp + 4, w = amp - 8;
      // com estava: una silueta discontínua
      const h0 = cas.dades[i] * cel;
      if (h0) svg.appendChild(el("rect", { x, y: base - h0, width: w, height: h0, rx: 4, fill: "none",
        style: "stroke:var(--etiqueta-3)", "stroke-width": 2, "stroke-dasharray": "6 5" }));
      for (let k = 0; k < v; k++) {
        svg.appendChild(el("rect", { x: x + 2, y: base - (k + 1) * cel + 2, width: w - 4, height: cel - 4,
          rx: 5, style: "fill:var(--blau)" }));
      }
      // el valor que tenia, sota la columna
      svg.appendChild(el("text", { x: x + w / 2, y: base + 28, "text-anchor": "middle", "font-size": 18,
        style: "fill:var(--etiqueta-2)", "font-family": "inherit" }, num(cas.dades[i], 0)));
    });

    const suma = cas.dades.reduce((a, b) => a + b, 0), mitjana = suma / n;
    if (pla()) {
      const y = base - mitjana * cel;
      svg.appendChild(el("line", { x1: x0 - 10, y1: y, x2: x0 + n * amp + 10, y2: y,
        style: "stroke:var(--etiqueta)", "stroke-width": 3, "stroke-dasharray": "10 7" }));
      svg.appendChild(el("text", { x: x0 + n * amp + 18, y: y + 7, "font-size": 22, "font-weight": 700,
        style: "fill:var(--etiqueta)", "font-family": "inherit" }, num(mitjana, 0)));
    }

    $("#mj-lectura").innerHTML = pla()
      ? txt("8.pla", { m: num(mitjana, 0) })
      : txt("8.encara");
    $("#mj-lectura").className = "avis " + (pla() ? "be" : "neutre");
    $("#mj-escampat").innerHTML = txt("8.anaven", { min: num(Math.min(...cas.dades), 0),
                                                    max: num(Math.max(...cas.dades), 0) });
    $("#mj-simbolic").textContent = pla()
      ? "(" + cas.dades.join(" + ") + ") ÷ " + n + " = " + suma + " ÷ " + n + " = " + num(mitjana, 0)
      : txt("8.amagat");
    $("#mj-simbolic").style.opacity = pla() ? "1" : ".4";
    $("#mj-un").disabled = pla();
    $("#mj-tot").disabled = pla();
  }

  function tria(c) {
    cas = c; ara = c.dades.slice();
    $("#mj-marca").hidden = !c.model;
    pinta();
  }

  function inicia() {
    if ($("#mj-pastilles").children.length) return;
    omplirTextos($("#mod-mitjana"));
    pastilles($("#mj-pastilles"), CASOS, tria);
    $("#mj-un").onclick  = () => { passaUn(); pinta(); };
    $("#mj-tot").onclick = () => { while (!pla()) passaUn(); pinta(); };
    $("#mj-torna").onclick = () => tria(cas);
    tria(CASOS[0]);
  }

  CE.registra("mitjana", inicia);
})();
