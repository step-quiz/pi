/* LA BARRA DE LA PROBABILITAT — mòdul «atzar» de la caixa d'eines (U7).
   Es registra sol; app.js no en sap res més que l'identificador.

   La probabilitat com un tros d'una barra, com a la pàgina 3 de la fitxa de la U7:
   la barra té una casella per cara del dau, i les cares que em van bé s'omplen.
   A sota hi ha la mateixa escala de 0 a 100 % de la U2, amb els tres mots de la
   pàgina 1: impossible, pot passar, segur. Així la regla de Laplace (em van bé ÷
   poden sortir) surt del dibuix i no d'una fórmula.

   Es toquen les cares per marcar-les o desmarcar-les. El compte amb números només
   surt quan hi ha alguna cara tocada; el cas d'exemple (un 5) ja ve marcat. */
(function () {
  "use strict";
  const { $, $$, num, el, pastilles, txt, omplirTextos } = CE;

  const CASOS = [
    { et: "Un 5",         model: true, bones: [5] },               // la fitxa, p. 3: 16,7 %
    { et: "Un parell",                 bones: [2, 4, 6] },
    { et: "Més de 4",                  bones: [5, 6] },
    { et: "De l'1 al 6",               bones: [1, 2, 3, 4, 5, 6] },
    { et: "Un 7",                      bones: [] }
  ];
  const CARES = 6;
  let cas = CASOS[0], marcades = new Set(), tocat = true;

  function paraula(p) {
    if (p === 0) return txt("9.impossible");
    if (p === 100) return txt("9.segur");
    return txt("9.pot_passar");
  }

  function pinta() {
    const svg = $("#at-svg"); svg.textContent = "";
    const x0 = 60, x1 = 600, y = 40, alt = 70, yp = 190;
    const amp = (x1 - x0) / CARES;
    const p = marcades.size / CARES * 100;

    for (let i = 0; i < CARES; i++) {
      const bona = marcades.has(i + 1);
      svg.appendChild(el("rect", { x: x0 + i * amp, y, width: amp, height: alt,
        style: "fill:" + (bona ? "var(--blau)" : "var(--camp)") + ";stroke:var(--etiqueta)", "stroke-width": 2 }));
      svg.appendChild(el("text", { x: x0 + i * amp + amp / 2, y: y + alt / 2 + 9, "text-anchor": "middle",
        "font-size": 26, "font-weight": 700, style: "fill:" + (bona ? "#fff" : "var(--etiqueta)"),
        "font-family": "inherit" }, String(i + 1)));
    }

    // l'escala de 0 a 100 %, la mateixa de la U2
    svg.appendChild(el("line", { x1: x0, y1: yp, x2: x1, y2: yp, style: "stroke:var(--etiqueta)", "stroke-width": 3 }));
    [0, 25, 50, 75, 100].forEach(v => {
      const x = x0 + (x1 - x0) * v / 100;
      svg.appendChild(el("line", { x1: x, y1: yp - 8, x2: x, y2: yp + 8, style: "stroke:var(--etiqueta)", "stroke-width": 2 }));
      svg.appendChild(el("text", { x, y: yp + 32, "text-anchor": "middle", "font-size": 17,
        style: "fill:var(--etiqueta-2)", "font-family": "inherit" }, v + " %"));
    });
    [[0, "9.impossible"], [50, "9.pot_passar"], [100, "9.segur"]].forEach(([v, c]) => {
      svg.appendChild(el("text", { x: x0 + (x1 - x0) * v / 100, y: yp + 58, "text-anchor": "middle",
        "font-size": 17, "font-weight": 700, style: "fill:var(--etiqueta-2)", "font-family": "inherit" },
        txt(c)));
    });

    // el tros pintat, portat sobre l'escala: fins on arriba és la probabilitat
    const xp = x0 + (x1 - x0) * p / 100;
    svg.appendChild(el("line", { x1: xp, y1: y + alt, x2: xp, y2: yp, style: "stroke:var(--blau)",
      "stroke-width": 3, "stroke-dasharray": "7 6" }));
    svg.appendChild(el("circle", { cx: xp, cy: yp, r: 10, style: "fill:var(--blau)" }));

    $("#at-pregunta").innerHTML = txt("9.vull", { que: cas.et.toLowerCase() });
    const encert = tocat && !cas.model && marcades.size === cas.bones.length &&
                   cas.bones.every(b => marcades.has(b));
    $("#at-lectura").className = "avis " + (encert ? "be" : "neutre");
    const lectura = txt("9.lectura", { b: marcades.size, t: CARES, p: num(p, 1), paraula: paraula(p) });
    $("#at-lectura").innerHTML = !tocat ? txt("9.amagat")
                               : (encert ? txt("comu.correcte") + " " : "") + lectura;
    $("#at-simbolic").textContent = tocat
      ? marcades.size + " ÷ " + CARES + " = " + num(marcades.size / CARES, 3) + " → " + num(p, 1) + " %"
      : txt("9.amagat");
    $("#at-simbolic").style.opacity = tocat ? "1" : ".4";
    $$("#at-cares .pastilla").forEach((b, i) => b.setAttribute("aria-pressed", String(marcades.has(i + 1))));
  }

  function inicia() {
    if ($("#at-pastilles").children.length) return;
    omplirTextos($("#mod-atzar"));
    const cares = $("#at-cares");
    for (let i = 1; i <= CARES; i++) {
      const b = document.createElement("button");
      b.className = "pastilla"; b.textContent = String(i);
      b.setAttribute("aria-label", txt("9.cara", { n: i }));
      b.onclick = () => {
        if (marcades.has(i)) marcades.delete(i); else marcades.add(i);
        tocat = true; pinta();
      };
      cares.appendChild(b);
    }
    pastilles($("#at-pastilles"), CASOS, c => {
      cas = c; tocat = !!c.model;
      marcades = new Set(c.model ? c.bones : []);
      $("#at-marca").hidden = !c.model;
      pinta();
    });
    $("#at-buida").onclick = () => { marcades.clear(); tocat = true; pinta(); };
    marcades = new Set(CASOS[0].bones);
    pinta();
  }

  CE.registra("atzar", inicia);
})();
