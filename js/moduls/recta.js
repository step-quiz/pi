/* RECTA I ESTIMACIÓ — mòdul «recta» de la caixa d'eines.
   Es registra sol; app.js no en sap res més que l'identificador. */
(function () {
  "use strict";
  const { $, $$, num, fix, euros, el, icona, pastilles, memoria } = CE;

  /* El primer nombre és el model, el mateix √7 de la fitxa de la Unitat 1. */
  const NOMBRES = [
    { et: "√7",  v: Math.sqrt(7)  },
    { et: "√5",  v: Math.sqrt(5)  },
    { et: "π",   v: Math.PI       },
    { et: "√11", v: Math.sqrt(11) },
    { et: "√30", v: Math.sqrt(30) }
  ];
  /* Els mateixos tres usos que a la fitxa impresa, amb els mateixos decimals. */
  const USOS = [
    { id: "parla",  et: "Ho dic",     dec: 1, frase: "De paraula no cal ser exacte." },
    { id: "compra", et: "Ho compro",  dec: 2, frase: "A la botiga es ven per centímetres." },
    { id: "talla",  et: "Ho tallo",   dec: 3, frase: "Si talles, el mil·límetre compta." }
  ];
  let rectaV = NOMBRES[0].v, rectaUs = null, rectaModel = true;

  function pintaRecta() {
    const svg = $("#recta-svg"); svg.textContent = "";
    const x0 = 34, x1 = 626, y = 76, max = 6;
    const px = t => x0 + t / max * (x1 - x0);
    const gris = "var(--etiqueta-3)", tinta = "var(--etiqueta)", sec = "var(--etiqueta-2)";

    const baix = Math.floor(rectaV), alt = baix + 1;
    svg.appendChild(el("rect", { x: px(baix), y: y - 13, width: px(alt) - px(baix), height: 26,
      rx: 6, style: "fill:var(--blau-suau)" }));
    svg.appendChild(el("line", { x1: x0, y1: y, x2: x1, y2: y, style: "stroke:" + gris,
      "stroke-width": 2 }));
    for (let i = 0; i <= max; i++) {
      svg.appendChild(el("line", { x1: px(i), y1: y - 8, x2: px(i), y2: y + 8,
        style: "stroke:" + gris, "stroke-width": 2 }));
      svg.appendChild(el("text", { x: px(i), y: y + 34, "text-anchor": "middle", "font-size": 18,
        style: "fill:" + sec, "font-family": "inherit" }, i));
    }
    svg.appendChild(el("line", { x1: px(rectaV), y1: y - 40, x2: px(rectaV), y2: y + 8,
      style: "stroke:var(--blau)", "stroke-width": 3, "stroke-linecap": "round" }));
    svg.appendChild(el("circle", { cx: px(rectaV), cy: y, r: 8, style: "fill:var(--blau)" }));
    svg.appendChild(el("text", { x: px(rectaV), y: y - 50, "text-anchor": "middle", "font-size": 21,
      "font-weight": 600, style: "fill:" + tinta, "font-family": "inherit" }, fix(rectaV, 4)));

    const prop = (rectaV - baix) < 0.5 ? baix : alt;
    $("#recta-avis").innerHTML = "És entre <b>" + baix + "</b> i <b>" + alt +
      "</b>, i més a prop del <b>" + prop + "</b>.";
  }

  function pintaTira() {
    const tira = $("#recta-tira"); tira.textContent = "";
    const dec = rectaUs ? rectaUs.dec : null;
    const s = fix(rectaV, 7);
    const coma = s.indexOf(",");
    const tall = dec === null ? s.length : coma + 1 + dec;   // sense tria, tot viu
    [...s].forEach((c, i) => {
      if (dec !== null && i === tall) {
        tira.appendChild(Object.assign(document.createElement("span"), { className: "tall" }));
      }
      const sp = document.createElement("span");
      sp.className = (dec === null || i < tall) ? "viu" : "mort";
      sp.textContent = c;
      tira.appendChild(sp);
    });
    const p = document.createElement("span"); p.className = "mort"; p.textContent = "…";
    tira.appendChild(p);

    $("#recta-resultat").textContent = dec === null ? "—" : fix(rectaV, dec);

    /* Arrodonir no és tallar: si la xifra següent és 5 o més, l'última puja.
       És l'error típic de la fitxa, i aquí es veu comparant la tira amb el
       resultat (per exemple, es conserva 2,64 però queda 2,65). */
    const nota = $("#recta-nota");
    if (dec === null) { nota.textContent = ""; return; }
    nota.textContent = (fix(rectaV, dec) !== s.slice(0, tall))
      ? "L'última xifra puja, perquè la següent és 5 o més."
      : "L'última xifra es queda igual.";
  }

  function iniciaRecta() {
    if ($("#recta-pastilles").children.length) return;

    pastilles($("#recta-pastilles"), NOMBRES, it => {
      rectaV = it.v;
      rectaModel = (it === NOMBRES[0]);
      $("#recta-marca").hidden = !rectaModel;
      pintaRecta(); pintaTira();
    });

    const cont = $("#recta-precisio");
    USOS.forEach((u, i) => {
      const b = document.createElement("button");
      b.setAttribute("aria-pressed", i === 1);         // el model: «Ho compro», 2 decimals
      b.appendChild(icona("i-" + u.id, 28));
      const e = document.createElement("div"); e.className = "et"; e.textContent = u.et;
      const d = document.createElement("div"); d.style.fontWeight = 600;
      d.textContent = u.dec + (u.dec === 1 ? " decimal" : " decimals");
      b.append(e, d);
      b.onclick = () => {
        $$("button", cont).forEach(x => x.setAttribute("aria-pressed", "false"));
        b.setAttribute("aria-pressed", "true");
        rectaUs = u; pintaTira();
      };
      cont.appendChild(b);
    });

    rectaUs = USOS[1];
    pintaRecta(); pintaTira();
  }


  /* ==================== 1.2 · Posa'l a la recta ====================
     Col·locar un nombre és pur canal visual, que és el punt fort d'aquest
     alumnat. El valor decimal es dona fet: aquí no s'avalua calcular, sinó
     situar. */
  const PER_POSAR = [
    { et: "√5",  v: Math.sqrt(5) },  { et: "√7",  v: Math.sqrt(7) },
    { et: "√11", v: Math.sqrt(11) }, { et: "π",   v: Math.PI },
    { et: "√20", v: Math.sqrt(20) }, { et: "√30", v: Math.sqrt(30) },
    { et: "7/2", v: 3.5 },           { et: "√2",  v: Math.SQRT2 }
  ];
  const POSA_MAX = 6, POSA_TOL = 0.25;
  let posaAra = null, posaFets = 0, posaEncerts = 0, posaTocat = null;

  function pintaPosa() {
    const svg = $("#posa-svg"); svg.textContent = "";
    const x0 = 34, x1 = 626, y = 84;
    const px = t => x0 + t / POSA_MAX * (x1 - x0);
    const gris = "var(--etiqueta-3)", sec = "var(--etiqueta-2)";

    svg.appendChild(el("line", { x1: x0, y1: y, x2: x1, y2: y,
      style: "stroke:" + gris, "stroke-width": 3, "stroke-linecap": "round" }));
    for (let i = 0; i <= POSA_MAX; i++) {
      svg.appendChild(el("line", { x1: px(i), y1: y - 10, x2: px(i), y2: y + 10,
        style: "stroke:" + gris, "stroke-width": 2 }));
      svg.appendChild(el("text", { x: px(i), y: y + 38, "text-anchor": "middle",
        "font-size": 19, style: "fill:" + sec, "font-family": "inherit" }, i));
    }
    if (posaTocat !== null) {
      const encert = Math.abs(posaTocat - posaAra.v) <= POSA_TOL;
      svg.appendChild(el("line", { x1: px(posaTocat), y1: y - 34, x2: px(posaTocat), y2: y + 10,
        style: "stroke:var(--" + (encert ? "verd" : "taronja") + ")", "stroke-width": 4,
        "stroke-linecap": "round" }));
      svg.appendChild(el("text", { x: px(posaTocat), y: y - 42, "text-anchor": "middle",
        "font-size": 17, "font-weight": 700,
        style: "fill:var(--" + (encert ? "verd" : "taronja") + ")",
        "font-family": "inherit" }, "aquí"));
      if (!encert) {   // ensenyar on era, per veure la distància
        svg.appendChild(el("circle", { cx: px(posaAra.v), cy: y, r: 9, style: "fill:var(--blau)" }));
        svg.appendChild(el("text", { x: px(posaAra.v), y: y + 62, "text-anchor": "middle",
          "font-size": 17, "font-weight": 700, style: "fill:var(--blau)",
          "font-family": "inherit" }, posaAra.et));
      }
    }
    const capa = el("rect", { x: 0, y: 0, width: 660, height: 160, fill: "transparent",
      style: "cursor:pointer" });
    capa.addEventListener("click", ev => {
      if (posaTocat !== null) return;                 // ja contestat
      const r = svg.getBoundingClientRect();
      const t = ((ev.clientX - r.left) / r.width * 660 - x0) / (x1 - x0) * POSA_MAX;
      posaTocat = Math.max(0, Math.min(POSA_MAX, t));
      posaFets++;
      const d = Math.abs(posaTocat - posaAra.v);
      const avis = $("#posa-avis");
      if (d <= POSA_TOL) {
        posaEncerts++;
        avis.className = "avis be";
        avis.innerHTML = "<b>Molt bé.</b> " + posaAra.et + " cau entre " +
          Math.floor(posaAra.v) + " i " + (Math.floor(posaAra.v) + 1) + ".";
      } else {
        avis.className = "avis pensa";
        avis.innerHTML = "Era una mica més a la <b>" +
          (posaTocat < posaAra.v ? "dreta" : "esquerra") + "</b>. Mira on cau.";
      }
      pintaPosa(); marcadorPosa();
    });
    svg.appendChild(capa);
  }

  function marcadorPosa() {
    $("#posa-compte").textContent = posaFets ? posaEncerts + " de " + posaFets : "";
  }

  function nouPosa() {
    let n; do { n = PER_POSAR[Math.floor(Math.random() * PER_POSAR.length)]; }
    while (posaAra && n.et === posaAra.et);
    posaAra = n; posaTocat = null;
    $("#posa-nom").textContent = n.et;
    $("#posa-valor").textContent = fix(n.v, 4);
    const avis = $("#posa-avis");
    avis.className = "avis neutre";
    avis.textContent = "Toca la recta.";
    pintaPosa(); marcadorPosa();
  }

  function iniciaPosa() {
    $("#posa-altre").onclick = nouPosa;
    nouPosa();
  }

  /* ==================== 1.3 · S'acaba o no s'acaba? ====================
     L'arrel d'un quadrat perfecte dona un nombre exacte; la resta, no. És una
     decisió de sí o no, sense escriure res, i de passada s'aprèn la llista de
     quadrats perfectes. */
  const ARRELS = [
    { et: "√9", v: 3, acaba: true },   { et: "√16", v: 4, acaba: true },
    { et: "√25", v: 5, acaba: true },  { et: "√36", v: 6, acaba: true },
    { et: "√49", v: 7, acaba: true },  { et: "√64", v: 8, acaba: true },
    { et: "√2", v: Math.SQRT2 },       { et: "√5", v: Math.sqrt(5) },
    { et: "√7", v: Math.sqrt(7) },     { et: "√10", v: Math.sqrt(10) },
    { et: "√20", v: Math.sqrt(20) },   { et: "π", v: Math.PI }
  ];
  let acabaAra = null, acabaFets = 0, acabaEncerts = 0, acabaTancat = false;

  function nouAcaba() {
    let n; do { n = ARRELS[Math.floor(Math.random() * ARRELS.length)]; }
    while (acabaAra && n.et === acabaAra.et);
    acabaAra = n; acabaTancat = false;
    $("#acaba-nom").textContent = n.et;
    $("#acaba-valor").textContent = n.acaba ? fix(n.v, 0) : fix(n.v, 7) + "…";
    const avis = $("#acaba-avis");
    avis.className = "avis neutre";
    avis.textContent = "Mira els decimals i tria.";
  }

  function responAcaba(diuQueAcaba) {
    if (acabaTancat) return;
    acabaTancat = true; acabaFets++;
    const bo = diuQueAcaba === !!acabaAra.acaba;
    if (bo) acabaEncerts++;
    const avis = $("#acaba-avis");
    avis.className = bo ? "avis be" : "avis pensa";
    avis.innerHTML = (bo ? "<b>Sí.</b> " : "<b>No.</b> ") + (acabaAra.acaba
      ? acabaAra.et + " és exactament <b>" + fix(acabaAra.v, 0) + "</b>: s'acaba."
      : acabaAra.et + " no s'acaba mai, per molts decimals que hi posis.");
    $("#acaba-compte").textContent = acabaEncerts + " de " + acabaFets;
  }

  function iniciaAcaba() {
    $$('#mod-recta .tria-gran .btn').forEach(b => {
      b.onclick = () => responAcaba(b.dataset.resp === "si");
    });
    $("#acaba-altre").onclick = nouAcaba;
    nouAcaba();
  }

  /* ==================== 1.4 · Quant costa arrodonir ====================
     Arrodonir cap amunt no és gratis. És l'exercici 6 de la fitxa, i enllaça
     amb la Unitat 2: una decisió que té preu. */
  const PREUS = [{ et: "Corda · 2,35 €/m", v: 2.35 }, { et: "Cinta · 1,80 €/m", v: 1.80 },
                 { et: "Cable · 0,90 €/m", v: 0.90 }];
  let costPreu = PREUS[0].v, costM = 3.7;

  function pintaCost() {
    $("#cost-metres").textContent = num(costM, 1) + " m";
    // A la caixa es cobra en cèntims: s'arrodoneix cada import ABANS de restar.
    // Si es restés en cru sortiria 0,71 € on la fitxa de la unitat diu 0,70 €.
    const cents = v => Math.round(v * 100) / 100;
    const just = cents(costM * costPreu);
    const amunt = cents(Math.ceil(costM - 1e-9) * costPreu);
    const maxim = Math.max(just, amunt, 0.01);
    const cont = $("#cost-barres"); cont.textContent = "";

    [["El que necessites: " + num(costM, 1) + " m", just, "base"],
     ["Arrodonit amunt: " + Math.ceil(costM - 1e-9) + " m", amunt, "amunt"]
    ].forEach(([et, v, cl]) => {
      const d = document.createElement("div"); d.className = "pas";
      d.innerHTML = '<div class="pas-cap"><span>' + et + "</span><b>" + euros(v) + "</b></div>";
      const b = document.createElement("div");
      b.className = "barra " + cl;
      b.style.width = Math.max(2, v / maxim * 100) + "%";
      d.appendChild(b); cont.appendChild(d);
    });

    const dif = amunt - just;
    $("#cost-avis").innerHTML = dif < 0.005
      ? "Demanes metres justos: no pagues res de més."
      : "Pagues <b>" + euros(dif) + "</b> de més.";
  }

  function iniciaCost() {
    pastilles($("#cost-preus"), PREUS, it => { costPreu = it.v; pintaCost(); });
    $("#cost-menys").onclick = () => { costM = Math.max(0.1, +(costM - 0.1).toFixed(1)); pintaCost(); };
    $("#cost-mes").onclick = () => { costM = Math.min(9.9, +(costM + 0.1).toFixed(1)); pintaCost(); };
    pintaCost();
  }

  /* ---- navegació entre 1.1, 1.2, 1.3 i 1.4 ---- */
  const ARRENCA = { 1: iniciaRecta, 2: iniciaPosa, 3: iniciaAcaba, 4: iniciaCost };
  const jaFetes = new Set();
  let subActual = null;

  function iniciaTasca1() {
    const subs = CE.subtasques($("#mod-recta"), n => {
      subActual = n;
      if (!jaFetes.has(n)) { ARRENCA[n](); jaFetes.add(n); }
    });
    subs.mostra(subActual || CE.subDemanada || 1);
  }

  CE.registra("recta", iniciaTasca1);
})();
