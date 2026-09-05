/* DOBLE RECTA NUMÈRICA — mòdul «doble» de la caixa d'eines.
   Es registra sol; app.js no en sap res més que l'identificador. */
(function () {
  "use strict";
  const { $, $$, num, fix, euros, el, icona, pastilles, memoria } = CE;

  /* Un sol dibuix per a tres unitats: percentatges (U2), escales (U3) i
     probabilitat (U7). Dues magnituds que van juntes, alineades, i el punt es mou
     a totes dues alhora.

     L'EXPRESSIÓ AMB NÚMEROS ESTÀ AMAGADA FINS QUE L'ALUMNE MOU EL PUNT.
     És a posta: el símbol ha d'emergir del dibuix, no aparèixer al seu costat.
     El cas d'exemple s'obre ja revelat, com la resta d'eines. */
  const DOBLES = [
    { et: "Percentatges", model: true,
      nomA: "euros",      maxA: 300, unA: " €",  decA: 2,
      nomB: "per cent",   maxB: 100, unB: " %",  decB: 0,
      passos: 20, marques: 5, inici: 16,                 // 16/20 = 80 %
      simbolic: (a, b) => "300 × " + num(b / 100, 2) + " = " + num(a, 2) + " €" },
    { et: "Escala 1 : 200",
      nomA: "cm al plànol", maxA: 10, unA: " cm", decA: 1,
      nomB: "m de veritat", maxB: 20, unB: " m",  decB: 1,
      passos: 20, marques: 5, inici: 8,                  // 4 cm → 8 m
      simbolic: (a, b) => num(a, 1) + " cm × 2 = " + num(b, 1) + " m" },
    { et: "Probabilitat",
      nomA: "casos que em van bé", maxA: 6,   unA: "",   decA: 0,
      nomB: "probabilitat",        maxB: 100, unB: " %", decB: 1,
      passos: 6, marques: 6, inici: 3,                   // 3 de 6 → 50 %
      simbolic: (a, b) => num(a, 0) + " ÷ 6 = " + num(b / 100, 3) + " → " + num(b, 1) + " %" }
  ];
  let dr = DOBLES[0], drPas = DOBLES[0].inici, drRevelat = true;

  function pintaDoble() {
    const svg = $("#dr-svg"); svg.textContent = "";
    const x0 = 74, x1 = 596, yA = 96, yB = 214;
    const t = drPas / dr.passos;
    const px = u => x0 + u * (x1 - x0);
    const A = dr.maxA * t, B = dr.maxB * t;
    const gris = "var(--etiqueta-3)", sec = "var(--etiqueta-2)";

    const recta = (y, nom, maxim, unitat, dec, aDalt) => {
      svg.appendChild(el("line", { x1: x0, y1: y, x2: x1, y2: y,
        style: "stroke:" + gris, "stroke-width": 3, "stroke-linecap": "round" }));
      for (let k = 0; k <= dr.marques; k++) {
        const u = k / dr.marques;
        svg.appendChild(el("line", { x1: px(u), y1: y - 9, x2: px(u), y2: y + 9,
          style: "stroke:" + gris, "stroke-width": 2 }));
        svg.appendChild(el("text", { x: px(u), y: y + (aDalt ? -20 : 34), "text-anchor": "middle",
          "font-size": 15, style: "fill:" + sec, "font-family": "inherit" },
          num(maxim * u, dec) + unitat));
      }
      svg.appendChild(el("text", { x: x0 - 14, y: y + 6, "text-anchor": "end", "font-size": 15,
        style: "fill:" + sec, "font-family": "inherit" }, nom));
    };

    // el connector vertical és el que fa veure que les dues rectes van lligades
    svg.appendChild(el("line", { x1: px(t), y1: yA, x2: px(t), y2: yB,
      style: "stroke:var(--blau)", "stroke-width": 3, "stroke-dasharray": "7 6" }));

    recta(yA, dr.nomA, dr.maxA, dr.unA, dr.decA, true);
    recta(yB, dr.nomB, dr.maxB, dr.unB, dr.decB, false);

    [[yA, A, dr.unA, dr.decA, -34], [yB, B, dr.unB, dr.decB, 52]].forEach(([y, v, u, d, dy]) => {
      svg.appendChild(el("circle", { cx: px(t), cy: y, r: 11, style: "fill:var(--blau)" }));
      svg.appendChild(el("text", { x: px(t), y: y + dy, "text-anchor": "middle", "font-size": 24,
        "font-weight": 700, style: "fill:var(--etiqueta)", "font-family": "inherit" },
        num(v, d) + u));
    });

    // capa de clics: també s'hi pot tocar directament
    const capa = el("rect", { x: 0, y: 0, width: 660, height: 300, fill: "transparent",
      style: "cursor:pointer" });
    capa.addEventListener("click", ev => {
      const r = svg.getBoundingClientRect();
      const u = ((ev.clientX - r.left) / r.width * 660 - x0) / (x1 - x0);
      drPas = Math.max(0, Math.min(dr.passos, Math.round(u * dr.passos)));
      drRevelat = true;
      pintaDoble();
    });
    svg.appendChild(capa);

    $("#dr-et-dalt").textContent = dr.nomA;
    $("#dr-val-dalt").textContent = num(A, dr.decA) + dr.unA;
    $("#dr-lectura").innerHTML = "<b>" + num(A, dr.decA) + dr.unA + "</b> es corresponen amb <b>" +
      num(B, dr.decB) + dr.unB + "</b>.";
    $("#dr-simbolic").textContent = drRevelat ? dr.simbolic(A, B) : "Mou el punt per veure-ho.";
    $("#dr-simbolic").style.opacity = drRevelat ? "1" : ".4";
    $("#dr-menys").disabled = drPas <= 0;
    $("#dr-mes").disabled = drPas >= dr.passos;
  }

  function iniciaDoble() {
    if ($("#dr-pastilles").children.length) return;
    pastilles($("#dr-pastilles"), DOBLES, d => {
      dr = d; drPas = d.inici; drRevelat = !!d.model;
      $("#dr-marca").hidden = !d.model;
      pintaDoble();
    });
    $("#dr-menys").onclick = () => { if (drPas > 0) { drPas--; drRevelat = true; pintaDoble(); } };
    $("#dr-mes").onclick   = () => { if (drPas < dr.passos) { drPas++; drRevelat = true; pintaDoble(); } };
    pintaDoble();
  }

  CE.registra("doble", iniciaDoble);
})();
