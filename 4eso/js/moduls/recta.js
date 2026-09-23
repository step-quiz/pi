/* RECTA I ESTIMACIÓ — mòdul «recta» de la caixa d'eines.
   Es registra sol; app.js no en sap res més que l'identificador. */
(function () {
  "use strict";
  const { $, $$, num, fix, euros, el, icona, pastilles, txt,
          omplirTextos, retroaccio } = CE;

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
    { id: "parla",  clau: "1.1.us_dic",    dec: 1 },
    { id: "compra", clau: "1.1.us_compro", dec: 2 },
    { id: "talla",  clau: "1.1.us_tallo",  dec: 3 }
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
    $("#recta-avis").innerHTML = txt("1.1.situa", { baix, alt, prop });
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
    nota.innerHTML = txt(fix(rectaV, dec) !== s.slice(0, tall) ? "1.1.puja" : "1.1.igual");
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
      const e = document.createElement("div"); e.className = "et";
      e.innerHTML = txt(u.clau);
      const d = document.createElement("div"); d.style.fontWeight = 600;
      d.innerHTML = u.dec + " " + txt(u.dec === 1 ? "1.1.decimal" : "1.1.decimals");
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


  /* ==================== 1.2 · Situa el nombre a la recta ====================
     Col·locar un nombre és pur canal visual, que és el punt fort d'aquest
     alumnat. El valor decimal es dona fet: aquí no s'avalua calcular, sinó
     situar.

     UNA TASCA TANCADA DE CINC NOMBRES, un cada vegada: Inici ● ○ ○ ○ ○ Final.
       · encert al primer intent            → «Correcte.»
       · primer error → «Incorrecte. Ara provem-ho d'una altra manera.» i la
         pista: la recta marca l'interval entre els dos nombres sencers, que és
         l'estratègia de l'exercici 1.1, i diu cap a quina banda és;
       · segon error  → l'app ensenya on és, i es passa al següent.
     Amb el teclat: el tabulador porta a la recta, les fletxes mouen el cursor
     d'una dècima (amb Maj., de mitja unitat) i Retorn o Espai el deixen anar. */
  const PER_POSAR = [
    { et: "√5",  v: Math.sqrt(5) },  { et: "√7",  v: Math.sqrt(7) },
    { et: "√11", v: Math.sqrt(11) }, { et: "π",   v: Math.PI },
    { et: "√20", v: Math.sqrt(20) }, { et: "√30", v: Math.sqrt(30) },
    { et: "7/2", v: 3.5 },           { et: "√2",  v: Math.SQRT2 }
  ];
  const POSA_MAX = 6, POSA_TOL = 0.25, POSA_N = 5;
  let posa = null;                                   // la tasca de passos
  let posaAra = null, posaTocat = null, posaIntents = 0, posaCursor = null;

  function pintaPosa() {
    const svg = $("#posa-svg"); svg.textContent = "";
    const x0 = 34, x1 = 626, y = 84;
    const px = t => x0 + t / POSA_MAX * (x1 - x0);
    const gris = "var(--etiqueta-3)", sec = "var(--etiqueta-2)";
    const e = posa.estat(), res = e.res[e.pas];
    const baix = Math.floor(posaAra.v);
    // prop de les vores, l'etiqueta s'alinea cap endins perquè no es talli
    const ancora = x => (x > 560 ? "end" : x < 100 ? "start" : "middle");

    // la pista del primer error: l'interval entre els dos nombres sencers
    if (posaIntents >= 1 && res !== "be" && res !== "pista") {
      svg.appendChild(el("rect", { x: px(baix), y: y - 16, width: px(baix + 1) - px(baix), height: 32,
        rx: 7, style: "fill:var(--blau-suau)" }));
    }
    svg.appendChild(el("line", { x1: x0, y1: y, x2: x1, y2: y,
      style: "stroke:" + gris, "stroke-width": 3, "stroke-linecap": "round" }));
    for (let i = 0; i <= POSA_MAX; i++) {
      svg.appendChild(el("line", { x1: px(i), y1: y - 10, x2: px(i), y2: y + 10,
        style: "stroke:" + gris, "stroke-width": 2 }));
      svg.appendChild(el("text", { x: px(i), y: y + 38, "text-anchor": "middle",
        "font-size": 19, style: "fill:" + sec, "font-family": "inherit" }, i));
    }
    if (posaTocat !== null) {
      const bo = res === "be" || res === "pista";
      const color = "var(--" + (bo ? "verd" : "taronja") + ")";
      svg.appendChild(el("line", { x1: px(posaTocat), y1: y - 34, x2: px(posaTocat), y2: y + 10,
        style: "stroke:" + color, "stroke-width": 4, "stroke-linecap": "round" }));
      svg.appendChild(el("text", { x: px(posaTocat), y: y - 42, "text-anchor": ancora(px(posaTocat)),
        "font-size": 17, "font-weight": 700, style: "fill:" + color,
        "font-family": "inherit" }, txt("1.2.aqui")));
    }
    if (res === "mostrat") {                        // on era, per veure la distància
      svg.appendChild(el("circle", { cx: px(posaAra.v), cy: y, r: 9, style: "fill:var(--blau)" }));
      svg.appendChild(el("text", { x: px(posaAra.v), y: y + 62, "text-anchor": ancora(px(posaAra.v)),
        "font-size": 17, "font-weight": 700, style: "fill:var(--blau-text)",
        "font-family": "inherit" }, posaAra.et));
    }
    if (posaCursor !== null && res == null) {       // el cursor de teclat
      svg.appendChild(el("line", { x1: px(posaCursor), y1: y - 30, x2: px(posaCursor), y2: y + 12,
        style: "stroke:var(--etiqueta)", "stroke-width": 3, "stroke-dasharray": "5 4" }));
    }
    const capa = el("rect", { x: 0, y: 0, width: 660, height: 160, fill: "transparent",
      style: "cursor:pointer" });
    capa.addEventListener("click", ev => {
      const r = svg.getBoundingClientRect();
      tocaPosa(((ev.clientX - r.left) / r.width * 660 - x0) / (x1 - x0) * POSA_MAX);
    });
    svg.appendChild(capa);
  }

  function tocaPosa(t) {
    const e = posa.estat();
    if (!e || e.acabada || posa.resolt()) return;
    posaTocat = Math.max(0, Math.min(POSA_MAX, t));
    const baix = Math.floor(posaAra.v), alt = baix + 1, avis = $("#posa-avis");

    if (Math.abs(posaTocat - posaAra.v) <= POSA_TOL) {
      posa.anota(posaIntents === 0 ? "be" : "pista");
      retroaccio(avis, "encert", txt("1.2.encert", { nom: posaAra.et, baix, alt }));
    } else if (posaIntents === 0) {
      posaIntents = 1;
      retroaccio(avis, "error", "", txt("1.2.pista", { baix, alt,
        banda: txt(posaTocat < posaAra.v ? "1.2.dreta" : "1.2.esquerra") }));
    } else {
      posaIntents = 2;
      posa.anota("mostrat");
      retroaccio(avis, "mostra", txt("1.2.mostra", { nom: posaAra.et, baix, alt }));
    }
    $("#posa-seguent").disabled = !posa.resolt();
    pintaPosa();
  }

  function pasPosa(i, e) {
    posaAra = PER_POSAR[e.extra.ordre[i]];
    posaTocat = null; posaIntents = 0; posaCursor = null;
    $("#posa-nom").textContent = posaAra.et;
    $("#posa-valor").textContent = fix(posaAra.v, 4);
    const avis = $("#posa-avis");
    avis.className = "avis neutre";
    avis.innerHTML = txt("1.2.comenca");
    const seguent = $("#posa-seguent");
    seguent.disabled = true;
    seguent.innerHTML = txt(posa.esUltim() ? "comu.acaba" : "comu.seguent");
    pintaPosa();
  }

  function teclatPosa(ev) {
    const e = posa.estat();
    if (!e || e.acabada || posa.resolt()) return;
    const dir = { ArrowLeft: -1, ArrowDown: -1, ArrowRight: 1, ArrowUp: 1 }[ev.key];
    if (dir) {
      ev.preventDefault();
      const salt = ev.shiftKey ? 0.5 : 0.1;
      posaCursor = Math.round(Math.max(0, Math.min(POSA_MAX, (posaCursor ?? 0) + dir * salt)) * 10) / 10;
      pintaPosa();
    } else if (ev.key === "Home" || ev.key === "End") {
      ev.preventDefault();
      posaCursor = ev.key === "Home" ? 0 : POSA_MAX;
      pintaPosa();
    } else if (ev.key === "Enter" || ev.key === " ") {
      ev.preventDefault();
      if (posaCursor === null) { posaCursor = 0; pintaPosa(); return; }
      tocaPosa(posaCursor);
    }
  }

  function iniciaPosa() {
    posa = CE.tasca({
      tasca: 1, sub: 2,
      recorregut: $("#posa-recorregut"),
      represa: $("#posa-represa"),
      final: $("#posa-final"),
      cos: [$("#posa-cos")],
      desa: true,
      valida: e => e.total === POSA_N && Array.isArray(e.extra.ordre) &&
                   e.extra.ordre.every(i => PER_POSAR[i] !== undefined),
      nom: () => "1.2 · " + txt("1.2.nom"),
      pinta: pasPosa
    });
    $("#posa-seguent").onclick = () => posa.seguent();
    const svg = $("#posa-svg");
    svg.addEventListener("keydown", teclatPosa);
    svg.addEventListener("blur", () => { if (posaCursor !== null) { posaCursor = null; pintaPosa(); } });
    // cinc nombres diferents, en un ordre nou cada vegada
    posa.inicia(() => ({ total: POSA_N, extra: {
      ordre: CE.barreja(PER_POSAR.map((_, i) => i)).slice(0, POSA_N) } }));
  }

  /* ==================== 1.3 · Els decimals s'acaben? ====================
     L'arrel d'un quadrat perfecte dona un nombre exacte; la resta, no. És una
     decisió de sí o no, sense escriure res, i de passada s'aprèn la llista de
     quadrats perfectes.

     UNA TASCA TANCADA DE SIS ARRELS: tres que s'acaben i tres que no, barrejades.
     Si són totes del mateix tipus, contestar sempre el mateix botó encerta, i
     això no és el que es vol veure.
       · primer error → «Incorrecte. Ara provem-ho d'una altra manera.» i la
         pista porta a mirar els tres punts (…) del final de la pantalla;
       · el segon intent ja és l'altre botó, i compta com a encert amb pista. */
  const ARRELS = [
    { et: "√9", v: 3, acaba: true },   { et: "√16", v: 4, acaba: true },
    { et: "√25", v: 5, acaba: true },  { et: "√36", v: 6, acaba: true },
    { et: "√49", v: 7, acaba: true },  { et: "√64", v: 8, acaba: true },
    { et: "√2", v: Math.SQRT2 },       { et: "√5", v: Math.sqrt(5) },
    { et: "√7", v: Math.sqrt(7) },     { et: "√10", v: Math.sqrt(10) },
    { et: "√20", v: Math.sqrt(20) },   { et: "π", v: Math.PI }
  ];
  const ACABA_N = 6;
  let acaba = null, acabaAra = null, acabaErrors = 0;

  function pasAcaba(i, e) {
    acabaAra = ARRELS[e.extra.ordre[i]];
    acabaErrors = 0;
    $("#acaba-nom").textContent = acabaAra.et;
    $("#acaba-valor").textContent = acabaAra.acaba ? fix(acabaAra.v, 0) : fix(acabaAra.v, 7) + "…";
    const avis = $("#acaba-avis");
    avis.className = "avis neutre";
    avis.innerHTML = txt("1.3.comenca");
    const seguent = $("#acaba-seguent");
    seguent.disabled = true;
    seguent.innerHTML = txt(acaba.esUltim() ? "comu.acaba" : "comu.seguent");
  }

  function responAcaba(diuQueAcaba) {
    const e = acaba.estat();
    if (!e || e.acabada || acaba.resolt()) return;
    const avis = $("#acaba-avis");
    const valors = { nom: acabaAra.et, valor: fix(acabaAra.v, 0) };
    const explica = txt(acabaAra.acaba ? "1.3.encert_si" : "1.3.encert_no", valors);

    if (diuQueAcaba === !!acabaAra.acaba) {
      acaba.anota(acabaErrors === 0 ? "be" : "pista");
      retroaccio(avis, "encert", explica);
    } else if (acabaErrors === 0) {
      acabaErrors = 1;
      retroaccio(avis, "error", "", txt(acabaAra.acaba ? "1.3.pista_si" : "1.3.pista_no", valors));
    } else {                                        // el mateix botó equivocat dues vegades
      acaba.anota("mostrat");
      retroaccio(avis, "mostra", explica);
    }
    $("#acaba-seguent").disabled = !acaba.resolt();
  }

  function iniciaAcaba() {
    acaba = CE.tasca({
      tasca: 1, sub: 3,
      recorregut: $("#acaba-recorregut"),
      represa: $("#acaba-represa"),
      final: $("#acaba-final"),
      cos: [$("#acaba-cos")],
      desa: true,
      valida: e => e.total === ACABA_N && Array.isArray(e.extra.ordre) &&
                   e.extra.ordre.every(i => ARRELS[i] !== undefined),
      nom: () => "1.3 · " + txt("1.3.nom"),
      pinta: pasAcaba
    });
    $$('#mod-recta .tria-gran .btn').forEach(b => {
      b.onclick = () => responAcaba(b.dataset.resp === "si");
    });
    $("#acaba-seguent").onclick = () => acaba.seguent();

    const exactes = ARRELS.map((a, i) => i).filter(i => ARRELS[i].acaba);
    const infinits = ARRELS.map((a, i) => i).filter(i => !ARRELS[i].acaba);
    acaba.inicia(() => ({ total: ACABA_N, extra: { ordre: CE.barreja(
      CE.barreja(exactes).slice(0, ACABA_N / 2).concat(CE.barreja(infinits).slice(0, ACABA_N / 2))) } }));
  }

  /* ==================== 1.4 · Quant costa arrodonir ====================
     Arrodonir cap amunt no és gratis. És l'exercici 6 de la fitxa, i enllaça
     amb la Unitat 2: una decisió que té preu. */
  // El preu és dada del codi; de textos.js només en surt el nom, de manera que
  // canviar-ne el text no pot fer que l'etiqueta digui un preu que no és.
  const PREUS = [{ clau: "1.4.mat_1", v: 2.35 },
                 { clau: "1.4.mat_2", v: 1.80 },
                 { clau: "1.4.mat_3", v: 0.90 }]
    .map(m => Object.assign({}, m, {
      get et() { return txt("1.4.mat_etiqueta", { nom: txt(m.clau), preu: euros(m.v) }); }
    }));
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

    [[txt("1.4.barra_just",  { m: num(costM, 1) }),              just,  "base"],
     [txt("1.4.barra_amunt", { m: Math.ceil(costM - 1e-9) }), amunt, "amunt"]
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
      ? txt("1.4.just")
      : txt("1.4.de_mes", { dif: euros(dif) });
  }

  function iniciaCost() {
    pastilles($("#cost-preus"), PREUS, it => { costPreu = it.v; pintaCost(); });
    $("#cost-menys").onclick = () => { costM = Math.max(0.1, +(costM - 0.1).toFixed(1)); pintaCost(); };
    $("#cost-mes").onclick = () => { costM = Math.min(9.9, +(costM + 0.1).toFixed(1)); pintaCost(); };
    pintaCost();
  }


  /* ==================== 1.5 · Cada xifra val una cosa ====================
     El valor posicional, amb la taula de columnes com a objecte visual. Cada
     xifra es pot tocar i diu què val. La descomposició de sota (3 + 0,4 + 0,07)
     és el contingut de debò: un nombre decimal és una suma. */

  // Els nombres es guarden com a xifres + exponent: 347 amb exp −2 és 3,47.
  // Així tota la feina és moure la coma, mai multiplicar decimals, que és
  // justament on es perd aquest alumnat.
  const LLOCS = { 2: "1.5.centenes", 1: "1.5.desenes", 0: "1.5.unitats",
                  "-1": "1.5.decimes", "-2": "1.5.centesimes", "-3": "1.5.millesimes" };
  const COLUMNES = [2, 1, 0, -1, -2, -3];
  const NOMBRES_VP = [
    { et: "3,47",  d: "347",  e: -2 },
    { et: "12,5",  d: "125",  e: -1 },
    { et: "0,08",  d: "8",    e: -2 },
    { et: "105,3", d: "1053", e: -1 },
    { et: "2,015", d: "2015", e: -3 }
  ];
  let vpAra = NOMBRES_VP[0], vpTriada = null;

  /** Escriu xifres × 10^exp com a decimal, movent la coma i sense fer servir
      aritmètica de coma flotant, que arrossegaria errors. */
  function decimal(xifres, exp) {
    if (/^0+$/.test(xifres)) return "0";     // el zero val zero a qualsevol columna
    let d = xifres.replace(/^0+(?=\d)/, "");
    if (exp >= 0) return d + "0".repeat(exp);
    const k = -exp;
    if (d.length > k) {
      const ent = d.slice(0, d.length - k), dec = d.slice(d.length - k).replace(/0+$/, "");
      return dec ? ent + "," + dec : ent;
    }
    const dec = ("0".repeat(k - d.length) + d).replace(/0+$/, "");
    return dec ? "0," + dec : "0";
  }

  /** L'exponent de cada xifra: la de més a la dreta té l'exponent del nombre. */
  const expDe = (i, n) => n.e + (n.d.length - 1 - i);

  function pintaValor() {
    const taula = $("#valor-taula"); taula.textContent = "";
    const ocupades = {};
    [...vpAra.d].forEach((x, i) => { ocupades[expDe(i, vpAra)] = { x, i }; });

    COLUMNES.forEach(exp => {
      if (exp === -1) {                                 // la columna de la coma
        const c = document.createElement("div");
        c.className = "vp-coma"; c.textContent = ",";
        taula.appendChild(c);
      }
      const col = document.createElement("div");
      col.className = "vp-col";
      const cap = document.createElement("div");
      cap.className = "vp-nom"; cap.innerHTML = txt(LLOCS[exp]);
      const cel = document.createElement("div");
      cel.className = "vp-cel";
      const dada = ocupades[exp];
      if (dada) {
        cel.textContent = dada.x;
        cel.classList.add("plena");
        if (vpTriada === dada.i) cel.classList.add("triada");
        cel.onclick = () => { vpTriada = dada.i; pintaValor(); };
      }
      col.append(cap, cel);
      taula.appendChild(col);
    });

    const avis = $("#valor-avis");
    if (vpTriada === null) {
      avis.className = "avis neutre";
      avis.innerHTML = txt("1.5.comenca");
    } else {
      const exp = expDe(vpTriada, vpAra);
      avis.className = "avis be";
      avis.innerHTML = txt("1.5.val", {
        xifra: vpAra.d[vpTriada],
        lloc: txt(LLOCS[exp]),
        quant: decimal(vpAra.d[vpTriada], exp)
      });
    }

    const suma = $("#valor-suma"); suma.textContent = "";
    [...vpAra.d].forEach((x, i) => {
      if (x === "0") return;
      const t = document.createElement("span");
      t.className = "tros" + (vpTriada === i ? " triada" : "");
      t.textContent = decimal(x, expDe(i, vpAra));
      if (suma.children.length) {
        const mes = document.createElement("span");
        mes.className = "mes"; mes.textContent = "+";
        suma.appendChild(mes);
      }
      suma.appendChild(t);
    });
    const ig = document.createElement("span");
    ig.className = "mes"; ig.textContent = "=";
    const tot = document.createElement("span");
    tot.className = "tros total"; tot.textContent = vpAra.et;
    suma.append(ig, tot);
  }

  function iniciaValor() {
    pastilles($("#valor-nombres"), NOMBRES_VP, it => {
      vpAra = it; vpTriada = null; pintaValor();
    });
    pintaValor();
  }

  /* ==================== 1.6 · Canviar d'unitat mou la coma ====================
     La mateixa llargada escrita de set maneres. Cada graó de l'escala és un lloc
     de coma, i per això aquest exercici i el 1.5 són el mateix objecte: el que
     canvia de columna és la xifra, no la quantitat. */
  const ESCALA = [
    { et: "km", p: 3 }, { et: "hm", p: 2 }, { et: "dam", p: 1 }, { et: "m", p: 0 },
    { et: "dm", p: -1 }, { et: "cm", p: -2 }, { et: "mm", p: -3 }
  ];
  const MESURES = [
    { et: "3,47 m", d: "347", e: -2 }, { et: "0,8 m", d: "8", e: -1 },
    { et: "12,5 m", d: "125", e: -1 }, { et: "250 m", d: "250", e: 0 }
  ];
  let uMesura = MESURES[0], uUnitat = 3;      // índex 3 = metres, la de partida

  function pintaUnitat() {
    const u = ESCALA[uUnitat];
    const valor = decimal(uMesura.d, uMesura.e - u.p);
    $("#unitat-gran").textContent = valor + " " + u.et;

    // l'escala, amb la unitat de partida i la triada marcades
    const svg = $("#unitat-escala"); svg.textContent = "";
    const x0 = 30, ample = (600 - 30) / ESCALA.length, y = 42, alt = 46;
    ESCALA.forEach((e, i) => {
      const x = x0 + i * ample;
      const tria = i === uUnitat, sortida = i === 3;
      svg.appendChild(el("rect", { x: x + 3, y, width: ample - 6, height: alt, rx: 9,
        style: "fill:var(--" + (tria ? "blau" : "camp") + ")" }));
      svg.appendChild(el("text", { x: x + ample / 2, y: y + 30, "text-anchor": "middle",
        "font-size": 20, "font-weight": 700, "font-family": "inherit",
        style: "fill:" + (tria ? "#fff" : "var(--etiqueta)") }, e.et));
      if (sortida && !tria) {
        svg.appendChild(el("text", { x: x + ample / 2, y: y - 10, "text-anchor": "middle",
          "font-size": 14, "font-family": "inherit",
          style: "fill:var(--etiqueta-2)" }, txt("1.6.surto")));
      }
      // cada graó es pot tocar: és com es tria la unitat
      const zona = el("rect", { x: x + 3, y: y - 16, width: ample - 6, height: alt + 32,
        fill: "transparent", style: "cursor:pointer" });
      zona.addEventListener("click", () => { uUnitat = i; pintaUnitat(); });
      svg.appendChild(zona);
    });
    // L'índex creix cap avall de l'escala (0 = km … 3 = m … 6 = mm), de manera
    // que baixar és restar-hi la posició del metre, no al revés. Amb el signe
    // canviat, l'app deia que de m a cm es puja i la coma va a l'esquerra.
    const graons = uUnitat - 3;                 // positiu: baixar per l'escala
    if (graons !== 0) {
      const xa = x0 + 3 * ample + ample / 2, xb = x0 + uUnitat * ample + ample / 2;
      svg.appendChild(el("path", {
        d: "M " + xa + " " + (y + alt + 14) + " L " + xb + " " + (y + alt + 14),
        style: "stroke:var(--taronja)", "stroke-width": 3, "stroke-linecap": "round" }));
      svg.appendChild(el("text", { x: (xa + xb) / 2, y: y + alt + 38, "text-anchor": "middle",
        "font-size": 16, "font-weight": 700, "font-family": "inherit",
        style: "fill:var(--taronja)" }, (graons > 0 ? "▶ " : "◀ ") + Math.abs(graons)));
    }

    const mov = $("#unitat-moviment");
    if (graons === 0) {
      mov.className = "avis neutre"; mov.innerHTML = txt("1.6.mateixa");
    } else {
      mov.className = "avis pensa";
      // amb un sol graó cal el singular: «1 graons» no es pot deixar passar
      const quants = Math.abs(graons);
      mov.innerHTML = txt("1.6." + (graons > 0 ? "dreta" : "esquerra") +
        (quants === 1 ? "1" : ""), { graons: quants });
    }
    // Sense canvi d'unitat, «3,47 m i 3,47 m són la mateixa llargada» no diu res.
    $("#unitat-igual").innerHTML = graons === 0
      ? txt("1.6.valor", { a: uMesura.et })
      : txt("1.6.igual", { a: uMesura.et, b: valor + " " + u.et });
  }

  function iniciaUnitat() {
    pastilles($("#unitat-mesures"), MESURES, it => { uMesura = it; pintaUnitat(); });
    pintaUnitat();
  }

  /* ---- navegació entre les subtasques ---- */
  const ARRENCA = { 1: iniciaRecta, 2: iniciaPosa, 3: iniciaAcaba, 4: iniciaCost,
                    5: iniciaValor, 6: iniciaUnitat };
  const jaFetes = new Set();
  let subActual = null;

  function iniciaTasca1() {
    omplirTextos($("#mod-recta"));      // les frases del marcatge, de textos.js
    const subs = CE.subtasques($("#mod-recta"), n => {
      subActual = n;
      if (!jaFetes.has(n)) { ARRENCA[n](); jaFetes.add(n); }
    });
    subs.mostra(subActual || CE.subDemanada || 1);
  }

  CE.registra("recta", iniciaTasca1);

  // Les dues subtasques que donen codi de verificació, per a verifica.html.
  const RECOMPTES = [txt("comu.r_passos"), txt("comu.r_primer"), txt("comu.r_pista")];
  CE.registraCataleg("1.2", { nom: txt("1.2.nom"), recomptes: RECOMPTES, resta: txt("comu.r_mostrat") });
  CE.registraCataleg("1.3", { nom: txt("1.3.nom"), recomptes: RECOMPTES, resta: txt("comu.r_mostrat") });
})();
