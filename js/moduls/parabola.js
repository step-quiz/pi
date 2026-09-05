/* PARÀBOLES — mòdul «parabola» de la caixa d'eines.
   Es registra sol; app.js no en sap res més que l'identificador. */
(function () {
  "use strict";
  const { $, $$, num, fix, euros, el, icona, pastilles, memoria } = CE;

  /* El primer fenomen és el model: s'obre amb el vèrtex ja marcat, igual que
     el primer apartat resolt de les fitxes. */
  const FENOMENS = [
    { et: "Pilota", model: true, a: -5, b: 10, c: 0, xMax: 2.3, yMax: 6,
      xNom: "temps (s)", yNom: "altura (m)",
      vertex: "Puja fins a 5 m, al segon 1.",
      talls:  "Surt de terra al segon 0 i hi torna al segon 2.",
      eix:    "Triga el mateix a pujar que a baixar." },
    { et: "Pont", a: -0.02, b: 0.8, c: 0, xMax: 44, yMax: 10,
      xNom: "distància (m)", yNom: "altura (m)",
      vertex: "El punt més alt és a 8 m, al mig del pont.",
      talls:  "L'arc va del metre 0 al metre 40.",
      eix:    "Una meitat és el mirall de l'altra." },
    { et: "Sortidor", a: -0.5, b: 2, c: 0, xMax: 4.6, yMax: 2.6,
      xNom: "distància (m)", yNom: "altura (m)",
      vertex: "L'aigua puja fins a 2 m, als 2 m de distància.",
      talls:  "Surt al metre 0 i cau al metre 4.",
      eix:    "Pujada i baixada són iguals." }
  ];
  const TASQUES = [
    { consigna: "Toca el punt més alt de la corba." },
    { consigna: "Toca els dos punts on la corba toca el terra." },
    { consigna: "Toca la línia que parteix la corba per la meitat." }
  ];
  let fen = FENOMENS[0], tasca = 0, tallsFets = [], totVisible = false;

  const C = () => {
    const e = 56, d = 22, dalt = 30, baix = 50, A = 660, H = 400;
    return {
      px: x => e + x / fen.xMax * (A - e - d),
      py: y => H - baix - y / fen.yMax * (H - baix - dalt),
      ix: p => (p - e) / (A - e - d) * fen.xMax,
      iy: p => (H - baix - p) / (H - baix - dalt) * fen.yMax
    };
  };
  const vertexDe = () => { const x = -fen.b / (2 * fen.a); return { x, y: fen.a * x * x + fen.b * x + fen.c }; };
  const tallsDe  = () => { const d = Math.sqrt(fen.b * fen.b - 4 * fen.a * fen.c);
    return [(-fen.b + d) / (2 * fen.a), (-fen.b - d) / (2 * fen.a)].sort((p, q) => p - q).map(v => v === 0 ? 0 : v); };

  function pintaParabola() {
    const svg = $("#par-svg"); svg.textContent = "";
    const c = C(), V = vertexDe(), T = tallsDe();
    const sec = "var(--etiqueta-2)", gris = "var(--etiqueta-3)";

    svg.appendChild(el("line", { x1: c.px(0), y1: c.py(0), x2: c.px(fen.xMax), y2: c.py(0),
      style: "stroke:" + gris, "stroke-width": 2 }));
    svg.appendChild(el("line", { x1: c.px(0), y1: c.py(0), x2: c.px(0), y2: c.py(fen.yMax),
      style: "stroke:" + gris, "stroke-width": 2 }));
    svg.appendChild(el("text", { x: c.px(fen.xMax), y: c.py(0) + 36, "text-anchor": "end",
      "font-size": 16, style: "fill:" + sec, "font-family": "inherit" }, fen.xNom));
    svg.appendChild(el("text", { x: c.px(0) - 6, y: c.py(fen.yMax) - 10, "font-size": 16,
      style: "fill:" + sec, "font-family": "inherit" }, fen.yNom));

    const pX = fen.xMax > 20 ? 10 : 1, pY = fen.yMax > 8 ? 2 : 1;
    for (let x = 0; x <= fen.xMax + 1e-9; x += pX)
      svg.appendChild(el("text", { x: c.px(x), y: c.py(0) + 24, "text-anchor": "middle",
        "font-size": 15, style: "fill:" + sec, "font-family": "inherit" }, num(x, 0)));
    for (let y = pY; y <= fen.yMax + 1e-9; y += pY)
      svg.appendChild(el("text", { x: c.px(0) - 12, y: c.py(y) + 5, "text-anchor": "end",
        "font-size": 15, style: "fill:" + sec, "font-family": "inherit" }, num(y, 0)));

    let d = "";
    for (let i = 0; i <= 180; i++) {
      const x = T[0] + (T[1] - T[0]) * i / 180;
      d += (i ? " L " : "M ") + c.px(x).toFixed(1) + " " + c.py(fen.a * x * x + fen.b * x + fen.c).toFixed(1);
    }
    svg.appendChild(el("path", { d, fill: "none", style: "stroke:var(--blau)",
      "stroke-width": 4, "stroke-linecap": "round" }));

    const fet = i => totVisible || tasca > i;
    if (fet(2)) svg.appendChild(el("line", { x1: c.px(V.x), y1: c.py(0), x2: c.px(V.x),
      y2: c.py(fen.yMax), style: "stroke:var(--taronja)", "stroke-width": 2.5, "stroke-dasharray": "8 6" }));
    if (fet(1)) T.forEach(t => svg.appendChild(el("circle", { cx: c.px(t), cy: c.py(0), r: 9,
      style: "fill:var(--verd)" })));
    else tallsFets.forEach(t => svg.appendChild(el("circle", { cx: c.px(t), cy: c.py(0), r: 9,
      style: "fill:var(--verd)" })));
    if (fet(0)) {
      svg.appendChild(el("circle", { cx: c.px(V.x), cy: c.py(V.y), r: 10, style: "fill:var(--vermell)" }));
      svg.appendChild(el("text", { x: c.px(V.x), y: c.py(V.y) - 18, "text-anchor": "middle",
        "font-size": 17, "font-weight": 600, style: "fill:var(--etiqueta)", "font-family": "inherit" },
        "(" + num(V.x, 1) + " , " + num(V.y, 1) + ")"));
    }

    const capa = el("rect", { x: 0, y: 0, width: 660, height: 400, fill: "transparent",
      style: "cursor:crosshair" });
    capa.addEventListener("click", clicParabola);
    svg.appendChild(capa);

    $("#par-tasca").textContent = totVisible ? "Això és el que hi havia."
      : (tasca > 2 ? "Ja l'has llegida sencera." : TASQUES[tasca].consigna);
    const p = $("#par-punts"); p.textContent = "";
    for (let i = 0; i < 3; i++) {
      const n = document.createElement("i");
      if (totVisible || tasca > i) n.className = "fet";
      p.appendChild(n);
    }
  }

  function clicParabola(ev) {
    if (totVisible || tasca > 2) return;
    const svg = $("#par-svg"), r = svg.getBoundingClientRect(), c = C();
    const x = c.ix((ev.clientX - r.left) / r.width * 660);
    const y = c.iy((ev.clientY - r.top) / r.height * 400);
    const tx = fen.xMax * 0.09, ty = fen.yMax * 0.12;
    const V = vertexDe(), T = tallsDe(), avis = $("#par-avis");
    const be = t => { avis.className = "avis be"; avis.innerHTML = t; };
    const no = t => { avis.className = "avis pensa"; avis.textContent = t; };

    if (tasca === 0) {
      if (Math.abs(x - V.x) < tx && Math.abs(y - V.y) < ty) { tasca = 1; be("<b>El vèrtex.</b> " + fen.vertex); }
      else no("Encara no. Busca on deixa de pujar.");
    } else if (tasca === 1) {
      const p = T.find(t => Math.abs(x - t) < tx && Math.abs(y) < ty);
      if (p != null && !tallsFets.some(t => Math.abs(t - p) < 1e-6)) {
        tallsFets.push(p);
        if (tallsFets.length === 2) { tasca = 2; be("<b>Els punts de tall.</b> " + fen.talls); }
        else { avis.className = "avis neutre"; avis.textContent = "Molt bé. Ara l'altre."; }
      } else no("Encara no. Són damunt la línia del terra.");
    } else {
      if (Math.abs(x - V.x) < tx) { tasca = 3; be("<b>L'eix de simetria.</b> " + fen.eix); }
      else no("Encara no. Passa just pel vèrtex.");
    }
    pintaParabola();
  }

  function reiniciaPar() {
    totVisible = false; tallsFets = [];
    tasca = fen.model ? 1 : 0;               // el model ja porta el vèrtex marcat
    const avis = $("#par-avis");
    avis.className = "avis neutre";
    avis.innerHTML = fen.model
      ? "<b>Exemple:</b> el vèrtex ja està marcat. " + fen.vertex
      : "Toca directament sobre el dibuix.";
    pintaParabola();
  }

  function iniciaParabola() {
    if ($("#par-pastilles").children.length) return;
    pastilles($("#par-pastilles"), FENOMENS, f => { fen = f; reiniciaPar(); });
    $("#par-repeteix").onclick = reiniciaPar;
    $("#par-mostra").onclick = () => {
      totVisible = true;
      const a = $("#par-avis"); a.className = "avis neutre";
      a.innerHTML = "<b>Vèrtex.</b> " + fen.vertex + "<br><b>Talls.</b> " + fen.talls +
        "<br><b>Eix.</b> " + fen.eix;
      pintaParabola();
    };
    reiniciaPar();
  }

  CE.registra("parabola", iniciaParabola);
})();
