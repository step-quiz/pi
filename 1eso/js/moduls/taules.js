/* ============================================================================
   TAULES — mòdul «taules» de la caixa d'eines · tasca 0
   ----------------------------------------------------------------------------
   És la targeta de les taules (targetes/taules.html) a la pantalla, i surt
   sempre: als enllaços ?task=n és la primera pestanya. A l'altra caixa aquest
   lloc és de la calculadora; aquí no, perquè cap exercici no la necessita
   (docs/CRITERIS-DISSENY.md, regla C). El que cal és saber on mirar.

   0.1 · LA TAULA
     Es trien els dos números amb dues files de pastilles, i surt el rectangle a
     la taula de quadrets: 7 files de 8 quadrets. Al costat, la lectura i la
     clau de la targeta amb aquests números. S'obre amb 7 · 8, que és el cas de
     la clau de la cara 2 de la targeta: el mateix cas al paper i a la pantalla.
     Tota la taula, amb les files de la targeta (7 · 8 = 56) i la línia fina
     després de la cinquena, és plegada darrere d'un botó: així la pantalla
     ensenya una multiplicació i el seu dibuix, i prou (decisió del docent, 24
     de setembre de 2026). Oberta, tocar-hi una fila també tria el número.

   0.2 · BUSCA-HO A LA TAULA
     Una tasca tancada de cinc multiplicacions de les que costen (del 6 al 9).
     Es fa com diu la clau de la targeta: es tria la taula i es toca la fila.
     Triar la taula no és contestar; la resposta és la fila.
       · la fila bona                         → «Correcte.»
       · la fila girada (7 · 6 per 6 · 7)     → també «Correcte.»: és el mateix
         resultat, i el rectangle girat de la 1.3 ho ensenya;
       · primer error → la pista diu què falla: la taula o la fila;
       · segon error  → la caixa tria la taula bona i marca la fila.

   0.3 · EL NÚMERO QUE FALTA
     Una tasca tancada de cinc multiplicacions amb un forat: 7 · … = 56, o bé
     … · 4 = 20. És l'exercici de les activitats 1_1, 1_3 i 1_6 del grup, fet
     amb la targeta: es tria la taula del número que ja es té i es baixa fins
     que surt el resultat. La fila diu el número que falta. Tres passos tenen
     el forat al segon número i dos al primer.
       · la fila bona                        → «Correcte.», i el forat s'omple;
       · amb el forat al primer (… · 4 = 20), es busca a la taula del 4 i surt
         4 · 5 = 20: el rectangle girat. També és «Correcte.», i ho diu;
       · primer error → la pista diu què falla: la taula o la fila;
       · segon error  → la caixa tria la taula bona i marca la fila.
     Una altra fila amb el mateix resultat no val: per a 4 · … = 24, la fila
     3 · 8 = 24 no respon la pregunta, perquè no hi ha el 4.
   ========================================================================== */

(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, quants, rect, delNombre, elNombre, lectura } = CE;
  const Q = CE.q;

  const TAULES = Array.from({ length: 10 }, (_, i) => ({ et: String(i + 1), n: i + 1 }));

  /** Les deu files d'una taula, com a la targeta. Cada fila és un botó.
      `aoTocar(b)` rep el segon número. */
  function llista(cont, a, aoTocar) {
    cont.textContent = "";
    for (let b = 1; b <= 10; b++) {
      const p = a * b;
      const boto = document.createElement("button");
      boto.type = "button";
      boto.className = "fila-taula" + (b === 5 ? " cinc" : "");
      boto.dataset.b = String(b);
      boto.innerHTML = '<span class="a">' + a + '</span><span class="op">·</span><span class="b">' + b +
        '</span><span class="eq">=</span><span class="p">' + p + "</span>";
      boto.setAttribute("aria-label", txtPla("0.1.fila_aria", { a, b, p }));
      boto.onclick = () => aoTocar(b);
      cont.appendChild(boto);
    }
  }

  /* ================================================ 0.1 · La taula ====== */

  const EXEMPLE = { a: 7, b: 8 };
  let tA = EXEMPLE.a, tB = EXEMPLE.b, oberta = false;

  /** Tota la taula, com a la targeta. Es pinta encara que sigui plegada: així,
      quan s'obre, ja hi és. Tocar-hi una fila tria el segon número, igual que
      la segona fila de pastilles. */
  function pintaTaula() {
    $("#tt-nom").textContent = txtPla("0.1.taula", { de: delNombre(tA) });
    llista($("#tt-llista"), tA, b => {
      tB = b;
      CE.premPastilla($("#tt-per"), b - 1);
      pintaFila();
      const lect = $("#tt-lectura");
      if (lect.scrollIntoView) lect.scrollIntoView({ block: "nearest", behavior: CE.quiet() ? "auto" : "smooth" });
    });
    pintaFila();
  }

  function pintaFila() {
    $$(".fila-taula", $("#tt-llista")).forEach(x =>
      x.setAttribute("aria-pressed", String(Number(x.dataset.b) === tB)));
    const p = tA * tB, svg = $("#tt-svg");
    const quadrets = quants(p, "comu.quadret", "comu.quadrets");
    Q.taula(svg, { f: tA, c: tB });
    svg.setAttribute("aria-label", txtPla("0.1.dibuix", { rect: rect(tA, tB), quadrets }));
    $("#tt-lectura").innerHTML = lectura(
      [txt("0.1.files", { rect: rect(tA, tB) }), txt("0.1.total", { quadrets })],
      tA + " · " + tB + " = " + p);
    $("#tt-marca").hidden = !(tA === EXEMPLE.a && tB === EXEMPLE.b);
    $("#tt-clau").innerHTML =
      '<p class="clau-q">' + txt("0.1.clau_q", { a: tA, b: tB }) + "</p><ol>" +
      "<li>" + txt("0.1.clau_1", { de: delNombre(tA) }) + "</li>" +
      "<li>" + txt("0.1.clau_2", { a: tA, b: tB }) + "</li>" +
      "<li>" + txt("0.1.clau_3", { p }) + "</li></ol>";
  }

  function obre01(si) {
    oberta = si;
    const boto = $("#tt-veure");
    $("#tt-sencera").hidden = !si;
    boto.setAttribute("aria-expanded", String(si));
    boto.innerHTML = txt(si ? "0.1.amaga" : "0.1.veure");
  }

  let fet01 = false;
  function inicia01() {
    if (fet01) return;
    fet01 = true;
    CE.pastilles($("#tt-pastilles"), TAULES.map(t => Object.assign({ aria: txtPla("0.1.taula", { de: delNombre(t.n) }) }, t)),
      t => { tA = t.n; pintaTaula(); }, tA - 1);
    CE.pastilles($("#tt-per"), TAULES, t => { tB = t.n; pintaFila(); }, tB - 1);
    $("#tt-veure").onclick = () => obre01(!oberta);
    obre01(false);
    pintaTaula();
  }

  /* ======================================= 0.2 · Busca-ho a la taula ====== */

  const DIFICILS = [[6, 7], [7, 8], [8, 6], [9, 7], [6, 9], [7, 7], [8, 9], [9, 6], [6, 8], [8, 7],
                    [7, 9], [9, 8]];
  const N = 5;
  let busca = null, bAra = null, bTaula = null, bIntents = 0, bTocada = null, llistaDe = null;

  const esBona = (t, b) => (t === bAra[0] && b === bAra[1]) || (t === bAra[1] && b === bAra[0]);

  function pintaBusca() {
    const cont = $("#tb-llista"), nom = $("#tb-nom");
    if (bTaula === null) {
      nom.textContent = "";
      cont.textContent = "";
      llistaDe = null;
      return;
    }
    nom.textContent = txtPla("0.1.taula", { de: delNombre(bTaula) });
    // Només es refà si ha canviat la taula: refer-la trauria el focus de la fila.
    if (llistaDe !== bTaula) { llista(cont, bTaula, tocaFila); llistaDe = bTaula; }
    const e = busca.estat(), resolt = e && e.res[e.pas] != null;
    $$(".fila-taula", cont).forEach(x => {
      const b = Number(x.dataset.b);
      const tocada = !!bTocada && bTocada.t === bTaula && bTocada.b === b;
      x.classList.toggle("tocada", tocada && !esBona(bTaula, b));
      x.classList.toggle("bona", resolt && esBona(bTaula, b));
      x.setAttribute("aria-pressed", String(tocada));
    });
  }

  function tocaFila(b) {
    const e = busca.estat();
    if (!e || e.acabada || busca.resolt()) return;
    bTocada = { t: bTaula, b };
    const [a, c] = bAra, p = a * c, avis = $("#tb-avis");
    if (esBona(bTaula, b)) {
      busca.anota(bIntents === 0 ? "be" : "pista");
      retroaccio(avis, "encert", txt(bTaula === a && b === c ? "0.2.encert" : "0.2.encert_girat",
        { a, b: c, p }));
    } else if (bIntents === 0) {
      bIntents = 1;
      let pista;
      if (bTaula === a) pista = txt("0.2.p_fila", { a, b: c });
      else if (bTaula === c) pista = txt("0.2.p_fila", { a: c, b: a });
      else pista = txt("0.2.p_taula", { a, de: delNombre(a) });
      retroaccio(avis, "error", txt("0.2.fet", { t: bTaula, b, q: bTaula * b }), pista);
    } else {
      busca.anota("mostrat");
      bTaula = a;
      bTocada = null;
      CE.premPastilla($("#tb-pastilles"), a - 1);
      retroaccio(avis, "mostra", txt("0.2.mostra", { a, b: c, p }));
    }
    $("#tb-seguent").disabled = !busca.resolt();
    pintaBusca();
    if (busca.resolt()) $("#tb-seguent").focus();
  }

  function pasBusca(i, e) {
    bAra = DIFICILS[e.extra.ordre[i]];
    bTaula = null; bIntents = 0; bTocada = null; llistaDe = null;
    $("#tb-pregunta").textContent = txtPla("0.2.pregunta", { a: bAra[0], b: bAra[1] });
    CE.pastilles($("#tb-pastilles"),
      TAULES.map(t => Object.assign({ aria: txtPla("0.1.taula", { de: delNombre(t.n) }) }, t)),
      t => {
        bTaula = t.n;
        // la guia avança: ara toca la fila (si hi ha una pista a la vista, es queda)
        if (bIntents === 0 && !busca.resolt()) $("#tb-avis").innerHTML = txt("0.2.toca_fila");
        pintaBusca();
      }, -1);
    const avis = $("#tb-avis");
    avis.className = "avis neutre";
    avis.innerHTML = busca.resolt() ? txt("comu.ja_fet") : txt("0.2.comenca");
    const seguent = $("#tb-seguent");
    seguent.disabled = !busca.resolt();
    seguent.innerHTML = txt(busca.esUltim() ? "comu.acaba" : "comu.seguent");
    pintaBusca();
  }

  let fet02 = false;
  function inicia02() {
    if (fet02) return;
    fet02 = true;
    busca = CE.tasca({
      tasca: 0, sub: 2,
      recorregut: $("#tb-recorregut"),
      represa: $("#tb-represa"),
      final: $("#tb-final"),
      cos: [$("#tb-cos")],
      desa: true,
      valida: e => e.total === N && e.extra && Array.isArray(e.extra.ordre) &&
                   e.extra.ordre.length === N && e.extra.ordre.every(i => DIFICILS[i] !== undefined),
      nom: () => "0.2 · " + txtPla("0.2.nom"),
      pinta: pasBusca
    });
    $("#tb-seguent").onclick = () => busca.seguent();
    busca.inicia(() => ({ total: N, extra: { ordre: CE.barreja(DIFICILS.map((_, i) => i)).slice(0, N) } }));
  }

  /* =========================================== 0.3 · El número que falta ====== */

  // falta: "b" → 7 · … = 56 (es té el primer); "a" → … · 4 = 20 (es té el segon)
  const FALTA = [
    { a: 7, b: 8, falta: "b" }, { a: 6, b: 7, falta: "b" }, { a: 9, b: 6, falta: "b" },
    { a: 8, b: 4, falta: "b" }, { a: 4, b: 6, falta: "b" }, { a: 3, b: 9, falta: "b" },
    { a: 7, b: 5, falta: "b" },
    { a: 5, b: 4, falta: "a" }, { a: 3, b: 8, falta: "a" }, { a: 9, b: 3, falta: "a" },
    { a: 7, b: 6, falta: "a" }, { a: 4, b: 7, falta: "a" }, { a: 6, b: 9, falta: "a" }
  ];
  const N3 = 5;
  let falta = null, fAra = null, fTaula = null, fIntents = 0, fTocada = null, fLlistaDe = null;

  const sap = c => c.falta === "a" ? c.b : c.a;         // el número que ja es té
  const busca3 = c => c.falta === "a" ? c.a : c.b;      // el que falta
  // Bona: la fila que fa la multiplicació, escrita d'una manera o de l'altra.
  const esBona3 = (t, r) => (t === fAra.a && r === fAra.b) || (t === fAra.b && r === fAra.a);

  /** 7 · … = 56, amb el forat en una caixa. Resolt, el forat porta el número. */
  function expressio3(resolt) {
    const c = fAra, x = busca3(c);
    const forat = '<span class="forat' + (resolt ? " ple" : "") + '">' + (resolt ? x : "…") + "</span>";
    const el = $("#tf-expr");
    el.innerHTML = (c.falta === "a" ? forat : c.a) + " · " + (c.falta === "b" ? forat : c.b) + " = " + c.a * c.b;
    el.setAttribute("aria-label", resolt ? c.a + " · " + c.b + " = " + c.a * c.b
      : txtPla(c.falta === "b" ? "0.3.aria_b" : "0.3.aria_a", { a: c.a, b: c.b, p: c.a * c.b }));
  }

  function pintaFalta() {
    const cont = $("#tf-llista"), nom = $("#tf-nom");
    const e = falta.estat(), resolt = e && e.res[e.pas] != null;
    expressio3(resolt);
    if (fTaula === null) {
      nom.textContent = "";
      cont.textContent = "";
      fLlistaDe = null;
      return;
    }
    nom.textContent = txtPla("0.1.taula", { de: delNombre(fTaula) });
    if (fLlistaDe !== fTaula) { llista(cont, fTaula, tocaFalta); fLlistaDe = fTaula; }
    $$(".fila-taula", cont).forEach(x => {
      const r = Number(x.dataset.b);
      const tocada = !!fTocada && fTocada.t === fTaula && fTocada.r === r;
      x.classList.toggle("tocada", tocada && !esBona3(fTaula, r));
      x.classList.toggle("bona", resolt && esBona3(fTaula, r));
      x.setAttribute("aria-pressed", String(tocada));
    });
  }

  function tocaFalta(r) {
    const e = falta.estat();
    if (!e || e.acabada || falta.resolt()) return;
    fTocada = { t: fTaula, r };
    const c = fAra, p = c.a * c.b, k = sap(c), x = busca3(c), avis = $("#tf-avis");
    const dades = { t: fTaula, r, p, a: c.a, b: c.b, el_x: elNombre(x) };
    if (esBona3(fTaula, r)) {
      falta.anota(fIntents === 0 ? "be" : "pista");
      retroaccio(avis, "encert", txt(fTaula === c.a && r === c.b ? "0.3.encert" : "0.3.encert_girat", dades));
    } else if (fIntents === 0) {
      fIntents = 1;
      const pista = (fTaula === c.a || fTaula === c.b)
        ? txt("0.3.p_fila", { el_p: elNombre(p) })
        : txt("0.3.p_taula", { el_k: elNombre(k), de: delNombre(k) });
      retroaccio(avis, "error", txt("0.3.fet", { t: fTaula, r, q: fTaula * r }), pista);
    } else {
      falta.anota("mostrat");
      fTaula = k;
      fTocada = null;
      CE.premPastilla($("#tf-pastilles"), k - 1);
      retroaccio(avis, "mostra", txt("0.3.mostra", { t: k, r: x, p, el_x: elNombre(x) }));
    }
    $("#tf-seguent").disabled = !falta.resolt();
    pintaFalta();
    if (falta.resolt()) $("#tf-seguent").focus();
  }

  function pasFalta(i, e) {
    fAra = FALTA[e.extra.ordre[i]];
    fTaula = null; fIntents = 0; fTocada = null; fLlistaDe = null;
    CE.pastilles($("#tf-pastilles"),
      TAULES.map(t => Object.assign({ aria: txtPla("0.1.taula", { de: delNombre(t.n) }) }, t)),
      t => {
        fTaula = t.n;
        if (fIntents === 0 && !falta.resolt())
          $("#tf-avis").innerHTML = txt("0.3.toca_fila", { el_p: elNombre(fAra.a * fAra.b) });
        pintaFalta();
      }, -1);
    const avis = $("#tf-avis");
    avis.className = "avis neutre";
    avis.innerHTML = falta.resolt() ? txt("comu.ja_fet") : txt("0.3.comenca");
    const seguent = $("#tf-seguent");
    seguent.disabled = !falta.resolt();
    seguent.innerHTML = txt(falta.esUltim() ? "comu.acaba" : "comu.seguent");
    pintaFalta();
  }

  /** Cinc passos: tres amb el forat al segon número i dos amb el forat al primer. */
  function nouOrdre3() {
    const de = f => CE.barreja(FALTA.map((_, i) => i).filter(i => FALTA[i].falta === f));
    return CE.barreja(de("b").slice(0, 3).concat(de("a").slice(0, 2)));
  }

  let fet03 = false;
  function inicia03() {
    if (fet03) return;
    fet03 = true;
    falta = CE.tasca({
      tasca: 0, sub: 3,
      recorregut: $("#tf-recorregut"),
      represa: $("#tf-represa"),
      final: $("#tf-final"),
      cos: [$("#tf-cos")],
      desa: true,
      valida: e => e.total === N3 && e.extra && Array.isArray(e.extra.ordre) &&
                   e.extra.ordre.length === N3 && e.extra.ordre.every(i => FALTA[i] !== undefined),
      nom: () => "0.3 · " + txtPla("0.3.nom"),
      pinta: pasFalta
    });
    $("#tf-seguent").onclick = () => falta.seguent();
    falta.inicia(() => ({ total: N3, extra: { ordre: nouOrdre3() } }));
  }

  /* ==================================================== arrencada ====== */

  const ARRENCA = { 1: inicia01, 2: inicia02, 3: inicia03 };
  let subs = null, subActual = null;

  function inicia() {
    const arrel = $("#mod-taules");
    if (!subs) {
      omplirTextos(arrel);
      subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); });
    }
    subs.mostra(subActual || CE.subDemanada(0) || 1);
  }

  CE.registra("taules", inicia);
  CE.registraCataleg("0.2", { nom: txtPla("0.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")],
    resta: txtPla("comu.r_mostrat") });
  CE.registraCataleg("0.3", { nom: txtPla("0.3.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")],
    resta: txtPla("comu.r_mostrat") });
  // Per a les proves automàtiques (eines/prova_caixa.py): les dades, no l'estat.
  CE.dades = Object.assign(CE.dades || {}, { taules: { EXEMPLE, DIFICILS, FALTA } });
})();
