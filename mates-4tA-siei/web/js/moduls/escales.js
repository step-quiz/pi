/* ESCALA I PLÀNOL — mòdul «escala» de la caixa d'eines.
   Es registra sol; app.js no en sap res més que l'identificador. */
(function () {
  "use strict";
  const { $, $$, num, fix, euros, el, icona, pastilles, memoria } = CE;

  const ESCALES = [{ et: "1 : 50", v: 50 }, { et: "1 : 100", v: 100 },
                   { et: "1 : 200", v: 200 }, { et: "1 : 500", v: 500 },
                   { et: "1 : 25 000", v: 25000 }];
  let escala = 100, bloqueig = false;

  function pintaEscala() {
    const pl = Number($("#e-planol").value) || 0;
    const re = Number($("#e-real").value) || 0;

    const cadena = $("#escala-cadena"); cadena.textContent = "";
    const posa = (txt, cls) => {
      const d = document.createElement("span"); d.className = "baula" + (cls ? " " + cls : "");
      d.textContent = txt; cadena.appendChild(d);
    };
    const op = txt => {
      const d = document.createElement("span"); d.className = "oper"; d.textContent = txt;
      cadena.appendChild(d);
    };
    posa(num(pl, 2) + " cm");  op("× " + escala.toLocaleString("ca-ES"));
    posa(num(pl * escala, 2) + " cm"); op("÷ 100");
    posa(num(re, 3) + " m", "final");

    const svg = $("#escala-svg"); svg.textContent = "";
    const w = Math.max(40, Math.min(430, pl * 34));
    svg.appendChild(el("rect", { x: 34, y: 40, width: w, height: 82, rx: 8,
      style: "fill:var(--camp)" }));
    svg.appendChild(el("line", { x1: 34, y1: 148, x2: 34 + w, y2: 148,
      style: "stroke:var(--blau)", "stroke-width": 3, "stroke-linecap": "round" }));
    svg.appendChild(el("line", { x1: 34, y1: 140, x2: 34, y2: 156, style: "stroke:var(--blau)", "stroke-width": 3 }));
    svg.appendChild(el("line", { x1: 34 + w, y1: 140, x2: 34 + w, y2: 156, style: "stroke:var(--blau)", "stroke-width": 3 }));
    svg.appendChild(el("text", { x: 34 + w / 2, y: 88, "text-anchor": "middle", "font-size": 20,
      "font-weight": 600, style: "fill:var(--etiqueta-2)", "font-family": "inherit" },
      num(pl, 2) + " cm al plànol"));
    svg.appendChild(el("text", { x: 34 + w / 2, y: 178, "text-anchor": "middle", "font-size": 22,
      "font-weight": 600, style: "fill:var(--blau)", "font-family": "inherit" },
      num(re, 2) + " m de veritat"));
  }

  function sincronitza(origen) {
    if (bloqueig) return;
    bloqueig = true;
    const pl = $("#e-planol"), re = $("#e-real");
    if (origen === "planol") re.value = +((Number(pl.value) || 0) * escala / 100).toFixed(3);
    else                     pl.value = +((Number(re.value) || 0) * 100 / escala).toFixed(3);
    bloqueig = false;
    pintaEscala();
  }

  function mostraRegla() {
    const m = escala / 100;
    $("#escala-regla").textContent = "1 cm = " + num(m, 2) + " m";
  }

  function iniciaEscala() {
    if ($("#escala-pastilles").children.length) return;
    pastilles($("#escala-pastilles"), ESCALES, it => {
      escala = it.v; mostraRegla(); sincronitza("planol");
    }, 1);
    $("#e-planol").oninput = () => sincronitza("planol");
    $("#e-real").oninput   = () => sincronitza("real");
    mostraRegla(); sincronitza("planol");
  }

  CE.registra("escala", iniciaEscala);
})();
