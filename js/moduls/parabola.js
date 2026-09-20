/* PARÀBOLES — mòdul «parabola» de la caixa d'eines.
   Es registra sol; app.js no en sap res més que l'identificador.

   UNA TASCA DE TRES PASSOS: vèrtex, punts de tall i eix.
   Cada pas buida el dibuix: només hi ha la corba i el que demana aquest pas.
   El que s'ha trobat abans no es queda a la vista, perquè tres marques de
   colors que s'acumulen són càrrega que no aporta res. Al final, quan la
   lectura ja està feta, el dibuix sencer les ajunta totes: és la conclusió.

   ELS ERRORS
     1r → «Incorrecte. Ara provem-ho d'una altra manera.» + una pista que és un
          camí diferent (seguir la corba amb el dit, mirar la línia del terra…),
          i al dibuix hi apareix una ajuda: la línia del terra marcada, o el
          vèrtex, que és per on passa l'eix.
     2n → l'app ensenya la resposta i es pot passar al pas següent.

   TECLAT: el dibuix rep el focus amb el tabulador. Les fletxes ← → mouen un
   cursor per damunt de la corba, i Retorn o Espai «toquen» on és el cursor.
   El cursor fa 40 salts entre els dos talls, de manera que cau exactament al
   vèrtex (salt 20) i als talls (salts 0 i 40). */
(function () {
  "use strict";
  const { $, $$, num, el, txt, omplirTextos, retroaccio } = CE;

  /* El primer fenomen és el model: s'obre amb el primer pas ja resolt, igual
     que el primer apartat de les fitxes. Les frases del fenomen van amb els
     seus números, al codi, perquè no es puguin desaparellar. */
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
  const PASSOS = ["vertex", "talls", "eix"];
  const SALTS = 40;                  // posicions del cursor de teclat entre els talls

  let fen = FENOMENS[0], tasca = null;
  let tallsFets = [], errors = 0, ajuda = false, cursor = null;

  const C = () => {
    const e = 56, d = 22, dalt = 30, baix = 50, A = 660, H = 400;
    return {
      px: x => e + x / fen.xMax * (A - e - d),
      py: y => H - baix - y / fen.yMax * (H - baix - dalt),
      ix: p => (p - e) / (A - e - d) * fen.xMax,
      iy: p => (H - baix - p) / (H - baix - dalt) * fen.yMax
    };
  };
  const f = x => fen.a * x * x + fen.b * x + fen.c;
  const vertexDe = () => { const x = -fen.b / (2 * fen.a); return { x, y: f(x) }; };
  const tallsDe  = () => { const d = Math.sqrt(fen.b * fen.b - 4 * fen.a * fen.c);
    return [(-fen.b + d) / (2 * fen.a), (-fen.b - d) / (2 * fen.a)].sort((p, q) => p - q).map(v => v === 0 ? 0 : v); };
  const xCursor = () => { const T = tallsDe(); return T[0] + (T[1] - T[0]) * cursor / SALTS; };

  /* ------------------------------------------------------------ dibuix -- */
  function dibuixa() {
    const e = tasca.estat();
    const svg = $("#par-svg"); svg.textContent = "";
    const c = C(), V = vertexDe(), T = tallsDe();
    const sec = "var(--etiqueta-2)", gris = "var(--etiqueta-3)";
    const acabada = e.acabada, resolt = e.res[e.pas] != null;

    // Què es veu: la corba i, com a molt, el que demana el pas d'ara.
    const veure = {
      vertex: acabada || (e.pas === 0 && resolt),
      talls:  acabada || (e.pas === 1 && resolt) ? T : (e.pas === 1 ? tallsFets : []),
      eix:    acabada || (e.pas === 2 && resolt),
      terra:  !acabada && !resolt && e.pas === 1 && ajuda,      // pista del pas 2
      guia:   !acabada && !resolt && e.pas === 2 && ajuda       // pista del pas 3
    };

    // eixos; el del terra, més gruixut i en color quan fa de pista
    svg.appendChild(el("line", { x1: c.px(0), y1: c.py(0), x2: c.px(fen.xMax), y2: c.py(0),
      style: "stroke:" + (veure.terra ? "var(--taronja)" : gris), "stroke-width": veure.terra ? 6 : 2 }));
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
      d += (i ? " L " : "M ") + c.px(x).toFixed(1) + " " + c.py(f(x)).toFixed(1);
    }
    svg.appendChild(el("path", { d, fill: "none", style: "stroke:var(--blau)",
      "stroke-width": 4, "stroke-linecap": "round" }));

    if (veure.guia) {                 // pista de l'eix: el vèrtex, buit i en gris
      svg.appendChild(el("circle", { cx: c.px(V.x), cy: c.py(V.y), r: 11, fill: "none",
        style: "stroke:var(--etiqueta-2)", "stroke-width": 3, "stroke-dasharray": "4 3" }));
    }
    if (veure.eix) svg.appendChild(el("line", { x1: c.px(V.x), y1: c.py(0), x2: c.px(V.x),
      y2: c.py(fen.yMax), style: "stroke:var(--taronja)", "stroke-width": 2.5, "stroke-dasharray": "8 6" }));
    veure.talls.forEach(t => svg.appendChild(el("circle", { cx: c.px(t), cy: c.py(0), r: 9,
      style: "fill:var(--verd)" })));
    if (veure.vertex) {
      svg.appendChild(el("circle", { cx: c.px(V.x), cy: c.py(V.y), r: 10, style: "fill:var(--vermell)" }));
      svg.appendChild(el("text", { x: c.px(V.x), y: c.py(V.y) - 18, "text-anchor": "middle",
        "font-size": 17, "font-weight": 600, style: "fill:var(--etiqueta)", "font-family": "inherit" },
        "(" + num(V.x, 1) + " , " + num(V.y, 1) + ")"));
    }
    if (cursor !== null && !acabada) {  // el cursor de teclat, damunt la corba
      const x = xCursor();
      svg.appendChild(el("circle", { cx: c.px(x), cy: c.py(f(x)), r: 13, fill: "none",
        style: "stroke:var(--etiqueta)", "stroke-width": 3 }));
    }

    const capa = el("rect", { x: 0, y: 0, width: 660, height: 400, fill: "transparent",
      style: "cursor:crosshair" });
    capa.addEventListener("click", ev => {
      const r = svg.getBoundingClientRect();
      toca(c.ix((ev.clientX - r.left) / r.width * 660), c.iy((ev.clientY - r.top) / r.height * 400));
    });
    svg.appendChild(capa);
  }

  /* ------------------------------------------------------- respondre -- */
  function toca(x, y) {
    const e = tasca.estat();
    if (!e || e.acabada || tasca.resolt()) return;
    const V = vertexDe(), T = tallsDe(), tx = fen.xMax * 0.09, ty = fen.yMax * 0.12;
    const avis = $("#par-avis");

    if (e.pas === 1) {
      const p = T.find(t => Math.abs(x - t) < tx && Math.abs(y) < ty);
      if (p != null && tallsFets.some(t => Math.abs(t - p) < 1e-6)) return;   // ja trobat
      if (p != null) {
        tallsFets.push(p);
        if (tallsFets.length < 2) {
          retroaccio(avis, "encert", txt("5.un_tall"));
          dibuixa();
          return;
        }
        resol(errors === 0 ? "be" : "pista");
        return;
      }
    } else if (e.pas === 0 ? (Math.abs(x - V.x) < tx && Math.abs(y - V.y) < ty)
                           : Math.abs(x - V.x) < tx) {
      resol(errors === 0 ? "be" : "pista");
      return;
    }
    falla();
  }

  const descripcio = pas => txt("5.b_" + PASSOS[pas], { que: fen[PASSOS[pas]] });

  function resol(resultat) {
    const e = tasca.estat();
    tasca.anota(resultat);
    retroaccio($("#par-avis"), "encert", descripcio(e.pas));
    $("#par-seguent").disabled = false;
    dibuixa();
  }

  function falla() {
    const e = tasca.estat();
    errors++;
    if (errors === 1) {
      ajuda = true;
      retroaccio($("#par-avis"), "error", "", txt("5.p_" + PASSOS[e.pas]));
    } else {
      tasca.anota("mostrat");
      retroaccio($("#par-avis"), "mostra", txt("5.mostra") + " " + descripcio(e.pas));
      $("#par-seguent").disabled = false;
    }
    dibuixa();
  }

  /* ------------------------------------------------- el pas visible -- */
  function pintaPas(pas, e) {
    fen = FENOMENS[e.cas] || FENOMENS[0];
    marcaPastilla(e.cas);
    tallsFets = []; errors = 0; ajuda = false;
    const resolt = e.res[pas] != null;

    $("#par-tasca").textContent = txt("5." + PASSOS[pas]);
    $("#par-marca").hidden = !(fen.model && pas === 0);
    $("#par-botons").hidden = false;
    const seguent = $("#par-seguent");
    seguent.disabled = !resolt;
    seguent.innerHTML = txt(tasca.esUltim() ? "comu.acaba" : "comu.seguent");

    const avis = $("#par-avis");
    if (e.res[pas] === "exemple") retroaccio(avis, "info", txt("5.exemple") + " " + descripcio(pas));
    else if (resolt) retroaccio(avis, "encert", descripcio(pas));
    else retroaccio(avis, "info", txt("5.toca"));
    dibuixa();
  }

  function enAcabar() {
    $("#par-tasca").textContent = txt("5.tot");
    $("#par-marca").hidden = true;
    $("#par-botons").hidden = true;          // el resum ja porta «Torna a començar»
    const a = $("#par-avis"); a.className = "avis neutre";
    a.innerHTML = PASSOS.map(p => txt("5.b_" + p, { que: fen[p] })).join("<br>");
    cursor = null;
    dibuixa();
  }

  function marcaPastilla(i) {
    $$(".pastilla", $("#par-pastilles")).forEach((b, j) => b.setAttribute("aria-pressed", String(i === j)));
  }

  /** Les dades per començar el fenomen triat. El model porta el primer pas fet. */
  const dadesNoves = () => ({ total: PASSOS.length, cas: FENOMENS.indexOf(fen),
                              resultats: fen.model ? ["exemple"] : [] });

  /* ------------------------------------------------------------ teclat -- */
  function teclat(ev) {
    const e = tasca.estat();
    if (!e || e.acabada) return;
    const pas = { ArrowLeft: -1, ArrowRight: 1, ArrowDown: -1, ArrowUp: 1 }[ev.key];
    if (pas) {
      ev.preventDefault();
      cursor = Math.max(0, Math.min(SALTS, (cursor ?? 0) + pas * (ev.shiftKey ? 5 : 1)));
      dibuixa();
    } else if (ev.key === "Enter" || ev.key === " ") {
      ev.preventDefault();
      if (cursor === null) { cursor = 0; dibuixa(); return; }
      const x = xCursor();
      toca(x, f(x));
    }
  }

  function iniciaParabola() {
    if ($("#par-pastilles").children.length) return;
    omplirTextos($("#mod-parabola"));

    tasca = CE.tasca({
      tasca: 5,
      recorregut: $("#par-recorregut"),
      represa: $("#par-represa"),
      final: $("#par-final"),
      cos: [$("#par-cos")],
      amagaEnAcabar: false,              // al final es queda el dibuix sencer
      desa: true,
      valida: e => e.total === PASSOS.length && FENOMENS[e.cas] !== undefined,
      nom: e => txt("5.titol") + " · " + FENOMENS[e.cas].et,
      pinta: pintaPas,
      enAcabar
    });

    CE.pastilles($("#par-pastilles"), FENOMENS, it => { fen = it; cursor = null; tasca.comenca(dadesNoves()); });
    $("#par-seguent").onclick = () => { cursor = null; tasca.seguent(); };
    $("#par-repeteix").onclick = () => { cursor = null; tasca.comenca(dadesNoves()); };
    $("#par-mostra").onclick = () => tasca.acaba("mostrat");

    const svg = $("#par-svg");
    svg.addEventListener("keydown", teclat);
    svg.addEventListener("blur", () => { if (cursor !== null) { cursor = null; if (tasca.estat()) dibuixa(); } });

    tasca.inicia(dadesNoves);
  }

  CE.registra("parabola", iniciaParabola);
  CE.registraCataleg("5", { nom: txt("5.titol"), casos: FENOMENS.map(f => f.et),
                            recomptes: [txt("comu.r_passos"), txt("comu.r_primer"), txt("comu.r_pista")],
                            resta: txt("comu.r_mostrat") });
})();
