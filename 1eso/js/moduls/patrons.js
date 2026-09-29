/* ============================================================================
   ELS PATRONS — mòdul «patrons» de la caixa d'eines · tasca 26 · unitat 7
   ----------------------------------------------------------------------------
   Un patró de quadrets «a · n + b»: la part fixa (b quadrets, taronja) i a
   quadrets de més a cada figura. La figura n té a · n + b quadrets. Sempre amb
   el punt, a · n (decisió del docent del 29/9/2026). Activitats 2 i 4 de la
   situació «Llenguatge algebraic i patrons» (el llibre, UD8: patrons i terme
   general). Figures fins a la 10: 3 · 10 + 2 = 32 quadrets.

   26.1 · EL PATRÓ               cinc patrons per triar i un comptador de la
                                 figura (de l'1 al 10). Diu quants quadrets té,
                                 què hi ha de fix, què s'hi afegeix i la regla.
                                 S'obre amb la cadena del llibre: 3, 5, 7, 9
                                 (2 · n + 1), figura 3.
   26.2 · QUANTS EN TÉ LA SEGÜENT?  tasca tancada de cinc passos: les figures
                                 1, 2 i 3, i quants quadrets té la 4. Les
                                 dolentes són les confusions de debò: sumar-ne
                                 sempre 1 i multiplicar per 2 (en Pau del
                                 llibre).
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, quants, lectura } = CE;
  const Q = CE.q;
  const PATRONS = [[1, 0], [2, 0], [3, 0], [2, 1], [3, 2]];     // [a, b]
  const quadrets = ([a, b], n) => a * n + b;
  const regla = ([a, b]) => (a === 1 ? "n" : a + " · n") + (b ? " + " + b : "");

  /* ================================================== 26.1 · El patró ====== */

  const EX261 = { k: 3, n: 3 };                  // 2 · n + 1, figura 3
  function pinta1(o) {
    const p = PATRONS[o.k], [a, b] = p, q = quadrets(p, o.n);
    Q.patro($("#pt-svg"), a, b, o.n);
    $("#pt-svg").setAttribute("aria-label", txtPla("26.1.aria", { n: o.n, q }));
    $("#pt-taula").innerHTML = '<table class="patro-taula"><tr><th>' + txt("26.1.figura") + "</th>" +
      [1, 2, 3, 4].map(n => "<td>" + n + "</td>").join("") + "</tr><tr><th>" + txt("26.1.quadrets") + "</th>" +
      [1, 2, 3, 4].map(n => "<td>" + quadrets(p, n) + "</td>").join("") + "</tr></table>";
    const par = [txt("26.1.te", { n: o.n, quadrets: quants(q, "comu.quadret", "comu.quadrets") })];
    if (b) par.push(txt("26.1.fixos", { b }));
    par.push(txt("26.1.afegeix", { quadrets: quants(a, "comu.quadret", "comu.quadrets") }));
    $("#pt-lectura").innerHTML = lectura(par, regla(p));
    $("#pt-marca").hidden = !(o.k === EX261.k && o.n === EX261.n);
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    const o = Object.assign({}, EX261);
    CE.pastilles($("#pt-pastilles"), PATRONS.map((p, k) => ({ et: txtPla("26.1.patro_n", { n: k + 1 }), k })),
      t => { o.k = t.k; pinta1(o); }, EX261.k);
    CE.comptador($("#pt-n"), { et: txt("26.1.et_figura"), min: 1, max: 10, valor: o.n, aoCanviar: v => { o.n = v; pinta1(o); } });
    pinta1(o);
  }

  /* ================================== 26.2 · Quants en té la següent? ====== */

  // Sense a = 1: amb 1 · n, «sumar-ne 1» seria la bona.
  const CASOS = [[2, 0], [3, 0], [2, 1], [3, 1], [3, 2], [2, 2]];
  const N2 = 5;
  let t2 = null, p2 = null, i2 = 0, opcions2 = [];
  /** La bona; sumar-ne sempre 1; i multiplicar per 2. */
  const opcionsDe = p => [["bona", quadrets(p, 4)], ["mes1", quadrets(p, 3) + 1], ["doble", quadrets(p, 3) * 2]];

  function pas2(i, e) {
    p2 = CASOS[e.extra.ordre[i]]; i2 = 0;
    const [a, b] = p2;
    [1, 2, 3].forEach(n => {
      Q.patro($("#pu-f" + n), a, b, n, { m: 22 });
      $("#pu-f" + n).setAttribute("aria-label", txtPla("26.1.aria", { n, q: quadrets(p2, n) }));
    });
    opcions2 = e.extra.torns[i].map(k => opcionsDe(p2)[k]);
    const cont = $("#pu-opcions");
    cont.innerHTML = opcions2.map((op, k) => '<button type="button" class="btn opcio-sino opcio-dec" data-k="' + k + '">' +
      op[1] + "</button>").join("");
    $$(".opcio-dec", cont).forEach(bt => { bt.onclick = () => tria2(Number(bt.dataset.k), bt); });
    const avis = $("#pu-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("26.2.comenca");
    $("#pu-seguent").disabled = !t2.resolt();
    $("#pu-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() {
    $$(".opcio-dec", $("#pu-opcions")).forEach(bt => { bt.disabled = true; bt.classList.toggle("bona", opcions2[bt.dataset.k][0] === "bona"); });
  }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const op = opcions2[k], avis = $("#pu-avis"), [a] = p2;
    const frase = txt("26.2.encert", { q3: quadrets(p2, 3), a, q4: quadrets(p2, 4) });
    if (op[0] === "bona") { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(op[0] === "mes1" ? "26.2.error_mes1" : "26.2.error_doble", { a }), txt("26.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); }
    $("#pu-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 26, sub: 2,
      recorregut: $("#pu-recorregut"), represa: $("#pu-represa"), final: $("#pu-final"), cos: [$("#pu-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => CASOS[i] !== undefined) && Array.isArray(e.extra.torns),
      nom: () => "26.2 · " + txtPla("26.2.nom"),
      pinta: pas2
    });
    $("#pu-seguent").onclick = () => t2.seguent();
    t2.inicia(() => {
      const ordre = CE.barreja(CASOS.map((c, i) => i)).slice(0, N2);
      return { total: N2, extra: { ordre, torns: ordre.map(() => CE.barreja([0, 1, 2])) } };
    });
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-patrons");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(26) || 1);
  }
  CE.registra("patrons", inicia);
  CE.registraCataleg("26.2", { nom: txtPla("26.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { patrons: { PATRONS, CASOS, opcionsDe } });
})();
