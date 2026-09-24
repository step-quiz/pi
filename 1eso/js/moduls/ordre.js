/* ============================================================================
   ORDRE — mòdul «ordre» de la caixa d'eines · tasca 4
   ----------------------------------------------------------------------------
   Què es fa primer? Sense parèntesis, primer es multiplica. Amb parèntesis,
   primer es fa el que hi ha a dins. El dibuix ho explica: 2 + 3 · 4 són un
   rectangle de 3 files de 4 quadrets i 2 quadrets solts, 14 quadrets; en
   canvi, (2 + 3) · 4 són 5 files de 4 quadrets, 20 quadrets.

   Només sumes i multiplicacions, amb números petits: les multiplicacions són
   de la targeta i les sumes es fan sense portar-ne (regla D). Les potències,
   les restes i les divisions de l'exercici del grup es queden fora.

   Cada expressió és d'un d'aquests quatre tipus:
     sm   a + b · c       la multiplicació és a la dreta
     ms   b · c + a       la multiplicació és a l'esquerra
     pm   (a + b) · c     el parèntesi va primer
     mp   c · (a + b)
   L'error típic és fer-ho d'esquerra a dreta, i només es veu amb «sm»; amb
   «ms» d'esquerra a dreta també surt bé. Per això la tasca tancada en porta
   de tots quatre.

   4.1 · MIRA L'ORDRE
     Es tria una expressió i surten els dos passos, primer i després, el dibuix
     i el total. S'obre amb 2 + 3 · 4, i la segona pastilla és (2 + 3) · 4: la
     parella que ensenya que el parèntesi canvia el resultat.

   4.2 · QUÈ ES FA PRIMER?
     Una tasca tancada de cinc expressions: dues «sm», una «ms» i dues amb
     parèntesi. Es toca el signe de l'operació que es fa primer.
       · el signe bo al primer intent → «Correcte.», els dos passos i el dibuix;
       · el signe dolent → diu què ha triat i la pista, que depèn del tipus;
       · amb dos signes, el segon intent sempre és l'altre: compta com a
         correcte amb pista.
   ========================================================================== */

(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, quants, lectura } = CE;
  const Q = CE.q;
  const qu = n => quants(n, "comu.quadret", "comu.quadrets");
  const fi = n => quants(n, "comu.fila", "comu.files");

  const EXPR = [
    { t: "sm", a: 2, b: 3, c: 4 }, { t: "sm", a: 1, b: 2, c: 5 }, { t: "sm", a: 3, b: 2, c: 3 },
    { t: "sm", a: 2, b: 4, c: 3 }, { t: "sm", a: 1, b: 3, c: 2 },
    { t: "ms", a: 3, b: 5, c: 2 }, { t: "ms", a: 1, b: 2, c: 4 }, { t: "ms", a: 2, b: 3, c: 2 },
    { t: "pm", a: 2, b: 3, c: 4 }, { t: "pm", a: 1, b: 4, c: 2 }, { t: "pm", a: 3, b: 1, c: 2 },
    { t: "mp", a: 1, b: 2, c: 4 }, { t: "mp", a: 2, b: 2, c: 3 }
  ];
  const ambParentesi = e => e.t === "pm" || e.t === "mp";

  /** L'expressió escrita: «2 + 3 · 4». */
  function escriu(e) {
    const { t, a, b, c } = e;
    if (t === "sm") return a + " + " + b + " · " + c;
    if (t === "ms") return b + " · " + c + " + " + a;
    if (t === "pm") return "(" + a + " + " + b + ") · " + c;
    return c + " · (" + a + " + " + b + ")";
  }

  /** Els dos passos. k1: «m» la multiplicació o «p» el parèntesi; k2: «s» la
      suma o «m» la multiplicació. */
  function passos(e) {
    const { t, a, b, c } = e;
    if (t === "sm") return { op1: b + " · " + c, r1: b * c, k1: "m", op2: a + " + " + b * c, r2: a + b * c, k2: "s" };
    if (t === "ms") return { op1: b + " · " + c, r1: b * c, k1: "m", op2: b * c + " + " + a, r2: b * c + a, k2: "s" };
    if (t === "pm") return { op1: a + " + " + b, r1: a + b, k1: "p", op2: (a + b) + " · " + c, r2: (a + b) * c, k2: "m" };
    return { op1: a + " + " + b, r1: a + b, k1: "p", op2: c + " · " + (a + b), r2: c * (a + b), k2: "m" };
  }

  /** Les peces de l'expressió. `primer` marca les que es fan primer; els signes
      porten quina operació són («suma» o «mult») i què sumen o multipliquen. */
  function peces(e) {
    const { t, a, b, c } = e;
    const n = (v, p) => ({ k: "n", v, primer: !!p });
    const par = (v, p) => ({ k: "par", v, primer: !!p });
    const suma = (x, y, p) => ({ k: "op", v: "+", op: "suma", x, y, primer: !!p });
    const mult = (x, y, p) => ({ k: "op", v: "·", op: "mult", x, y, primer: !!p });
    if (t === "sm") return [n(a), suma(a, b), n(b, 1), mult(b, c, 1), n(c, 1)];
    if (t === "ms") return [n(b, 1), mult(b, c, 1), n(c, 1), suma(c, a), n(a)];
    if (t === "pm") return [par("(", 1), n(a, 1), suma(a, b, 1), n(b, 1), par(")", 1), mult(b, c), n(c)];
    return [n(c), mult(c, a), par("(", 1), n(a, 1), suma(a, b, 1), n(b, 1), par(")", 1)];
  }

  /** L'expressió en HTML. Amb `botons`, els signes es poden tocar; amb
      `marca`, el que es fa primer va ressaltat. */
  function expressio(e, o) {
    o = o || {};
    let html = "", dins = false;
    peces(e).forEach((p, i) => {
      if (o.marca && p.primer && !dins) { html += '<mark class="primer">'; dins = true; }
      if (o.marca && !p.primer && dins) { html += "</mark>"; dins = false; }
      if (p.k === "op" && o.botons) {
        const aria = txtPla(p.op === "suma" ? "4.2.aria_suma" : "4.2.aria_mult", { a: p.x, b: p.y });
        html += '<button type="button" class="signe" data-op="' + p.op + '" data-i="' + i +
                '" aria-label="' + aria + '">' + p.v + "</button>";
      } else {
        html += '<span class="' + (p.k === "op" ? "op" : p.k) + '">' + p.v + "</span>";
      }
    });
    if (dins) html += "</mark>";
    return html;
  }

  /** El dibuix de l'expressió. */
  function dibuixa(svg, e) {
    svg.textContent = "";
    const { t, a, b, c } = e, M = 30, x0 = 96, y0 = 56, G = 10;
    let amp, alt;
    if (t === "sm" || t === "ms") {
      // El rectangle de la multiplicació i els quadrets solts, cadascun al costat
      // on és a l'expressió: 2 + 3 · 4, els solts a l'esquerra; 5 · 2 + 3, a la dreta.
      const solts = t === "sm" ? "esquerra" : "dreta";
      const xr = solts === "esquerra" ? 50 + a * M + 95 : x0;
      const xs = solts === "esquerra" ? 50 : xr + c * M + 40, ys = y0 + (b - 1) * M;
      Q.rectangle(svg, xr, y0, b, c, M, "q");
      Q.rectangle(svg, xs, ys, 1, a, M, "q b");
      Q.clau(svg, xr, y0 - 12, xr + c * M, y0 - 12, qu(c), "dalt");
      Q.clau(svg, xr - 12, y0, xr - 12, y0 + b * M, fi(b), "esquerra");
      const baix = y0 + b * M + 26;
      Q.text(svg, xr + c * M / 2, baix, b + " · " + c + " = " + b * c, "q-text fort", 18);
      Q.text(svg, xs + a * M / 2, baix, qu(a), "q-text fort", 18);
      amp = Math.max(xr + c * M, xs + a * M) + 56; alt = baix + 22;
    } else if (t === "pm") {
      // (a + b) files de c quadrets: les a files i les b files, amb una mica d'aire
      const s = a + b;
      Q.rectangle(svg, x0, y0, a, c, M, "q");
      Q.rectangle(svg, x0, y0 + a * M + G, b, c, M, "q");
      Q.clau(svg, x0, y0 - 12, x0 + c * M, y0 - 12, qu(c), "dalt");
      Q.clau(svg, x0 - 12, y0, x0 - 12, y0 + a * M, fi(a), "esquerra");
      Q.clau(svg, x0 - 12, y0 + a * M + G, x0 - 12, y0 + s * M + G, fi(b), "esquerra");
      amp = x0 + c * M + 40; alt = y0 + s * M + G + 24;
    } else {
      // c files de (a + b) quadrets: les a columnes i les b columnes, amb aire
      const s = a + b;
      Q.rectangle(svg, x0, y0, c, a, M, "q");
      Q.rectangle(svg, x0 + a * M + G, y0, c, b, M, "q");
      Q.clau(svg, x0, y0 - 12, x0 + s * M + G, y0 - 12, qu(s), "dalt");
      Q.clau(svg, x0 - 12, y0, x0 - 12, y0 + c * M, fi(c), "esquerra");
      amp = x0 + s * M + G + 56; alt = y0 + c * M + 24;
    }
    svg.setAttribute("viewBox", "0 0 " + Math.max(amp, 240) + " " + alt);
    svg.setAttribute("aria-label", txtPla("4.1.total", { quadrets: qu(passos(e).r2) }));
  }

  /** Les frases dels dos passos i el total. */
  function frases(e) {
    const p = passos(e);
    return [
      txt(p.k1 === "m" ? "4.1.primer_m" : "4.1.primer_p", { op: p.op1, r: p.r1 }),
      txt(p.k2 === "s" ? "4.1.despres_s" : "4.1.despres_m", { op: p.op2, r: p.r2 }),
      txt("4.1.total", { quadrets: qu(p.r2) })
    ];
  }

  /* =============================================== 4.1 · Mira l'ordre ====== */

  const EXPLORA = [0, 8, 5, 11].map(i => Object.assign({ et: escriu(EXPR[i]) }, EXPR[i]));
  let oCas = EXPLORA[0];

  function pinta41() {
    const e = oCas;
    $("#o1-expr").innerHTML = expressio(e, { marca: true });
    dibuixa($("#o1-svg"), e);
    $("#o1-lectura").innerHTML =
      lectura(frases(e)) +
      lectura([txt(ambParentesi(e) ? "4.1.regla_p" : "4.1.regla_m")], escriu(e) + " = " + passos(e).r2);
    $("#o1-marca").hidden = oCas !== EXPLORA[0];
  }

  let fet41 = false;
  function inicia41() {
    if (fet41) return;
    fet41 = true;
    CE.pastilles($("#o1-pastilles"), EXPLORA, c => { oCas = c; pinta41(); });
    pinta41();
  }

  /* ========================================== 4.2 · Què es fa primer? ====== */

  const N42 = 5;
  let quin = null, eAra = null, oIntents = 0, oTriat = null;
  const primerOp = e => ambParentesi(e) ? "suma" : "mult";

  function pinta42() {
    const e = quin.estat(), resolt = e.res[e.pas] != null;
    const cont = $("#o2-expr");
    cont.innerHTML = expressio(eAra, { botons: !resolt, marca: resolt });
    $$(".signe", cont).forEach(b => {
      if (b.dataset.op === oTriat) { b.classList.add("mal"); b.disabled = true; }
      b.onclick = () => tria42(b.dataset.op);
    });
    const svg = $("#o2-svg"), passes = $("#o2-passos");
    // Un <svg> no té la propietat .hidden (només la tenen els elements HTML):
    // cal posar i treure l'atribut.
    svg.toggleAttribute("hidden", !resolt);
    passes.hidden = !resolt;
    if (resolt) {
      dibuixa(svg, eAra);
      passes.innerHTML = lectura(frases(eAra), escriu(eAra) + " = " + passos(eAra).r2);
    }
  }

  function tria42(op) {
    const e = quin.estat();
    if (!e || e.acabada || quin.resolt()) return;
    const avis = $("#o2-avis"), p = passos(eAra);
    if (op === primerOp(eAra)) {
      quin.anota(oIntents === 0 ? "be" : "pista");
      retroaccio(avis, "encert", txt("4.2.encert", { op1: p.op1, r1: p.r1, op2: p.op2, r2: p.r2 }));
    } else if (oIntents === 0) {
      oIntents = 1;
      oTriat = op;
      retroaccio(avis, "error", txt(op === "suma" ? "4.2.fet_s" : "4.2.fet_m"),
                 txt(ambParentesi(eAra) ? "4.2.p_par" : "4.2.p_mult"));
    } else {                                   // no hi arriba: el signe dolent queda desactivat
      quin.anota("mostrat");
      retroaccio(avis, "mostra", txt("4.2.encert", { op1: p.op1, r1: p.r1, op2: p.op2, r2: p.r2 }));
    }
    $("#o2-seguent").disabled = !quin.resolt();
    pinta42();
    // refer l'expressió treu el focus: es posa a l'altre signe o a «Següent pas»
    const altre = $("#o2-expr .signe:not([disabled])");
    if (quin.resolt()) $("#o2-seguent").focus(); else if (altre) altre.focus();
  }

  function pas42(i, e) {
    eAra = EXPR[e.extra.ordre[i]];
    oIntents = 0; oTriat = null;
    const avis = $("#o2-avis");
    avis.className = "avis neutre";
    avis.innerHTML = quin.resolt() ? txt("comu.ja_fet") : txt("4.2.comenca");
    const seguent = $("#o2-seguent");
    seguent.disabled = !quin.resolt();
    seguent.innerHTML = txt(quin.esUltim() ? "comu.acaba" : "comu.seguent");
    pinta42();
  }

  /** Dues «sm», una «ms» i dues amb parèntesi, barrejades. */
  function nouOrdre() {
    const de = t => CE.barreja(EXPR.map((x, i) => i).filter(i => t.includes(EXPR[i].t)));
    return CE.barreja(de(["sm"]).slice(0, 2).concat(de(["ms"]).slice(0, 1), de(["pm", "mp"]).slice(0, 2)));
  }

  let fet42 = false;
  function inicia42() {
    if (fet42) return;
    fet42 = true;
    quin = CE.tasca({
      tasca: 4, sub: 2,
      recorregut: $("#o2-recorregut"),
      represa: $("#o2-represa"),
      final: $("#o2-final"),
      cos: [$("#o2-cos")],
      desa: true,
      valida: e => e.total === N42 && e.extra && Array.isArray(e.extra.ordre) &&
                   e.extra.ordre.length === N42 && e.extra.ordre.every(i => EXPR[i] !== undefined),
      nom: () => "4.2 · " + txtPla("4.2.nom"),
      pinta: pas42
    });
    $("#o2-seguent").onclick = () => quin.seguent();
    quin.inicia(() => ({ total: N42, extra: { ordre: nouOrdre() } }));
  }

  /* ==================================================== arrencada ====== */

  const ARRENCA = { 1: inicia41, 2: inicia42 };
  let subs = null, subActual = null;

  function inicia() {
    const arrel = $("#mod-ordre");
    if (!subs) {
      omplirTextos(arrel);
      subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); });
    }
    subs.mostra(subActual || CE.subDemanada(4) || 1);
  }

  CE.registra("ordre", inicia);
  CE.registraCataleg("4.2", { nom: txtPla("4.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")],
    resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { ordre: { EXPR, escriu, passos } });
})();
