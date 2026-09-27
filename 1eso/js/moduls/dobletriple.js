/* ============================================================================
   DOBLES I TRIPLES — mòdul «dobletriple» de la caixa d'eines · tasca 17 ·
   unitat 4
   ----------------------------------------------------------------------------
   El doble i el triple es llegeixen en dues files de quadrets, una sota
   l'altra i començant al mateix lloc: la fila de dalt és el nombre petit, la
   de baix és el doble o el triple. Les ratlles fines parteixen la fila de
   baix en trossos de la mida de la fila de dalt, perquè es vegi quantes
   vegades hi cap. Serveix per comparar mides relatives, com l'ou i l'ocell de
   la situació «És gran l'ou del kiwi?»: un ou pot ser petit i, alhora, el
   doble d'un altre ou petit. Activitats 1, 2 i 8 de la situació.
   17.1 · EL DOBLE I EL TRIPLE   un comptador (el nombre petit) i unes
                                 pastilles (doble o triple). Les dues files,
                                 amb la mida de cada una i les vegades que hi
                                 cap. S'obre amb 3 i el seu doble, 6.
   17.2 · QUANTES VEGADES HI CAP?  tasca tancada de cinc passos: les dues
                                   files ja dibuixades, i es tria si la de
                                   baix és el doble o el triple de la de
                                   dalt. Les dolentes són les confusions de
                                   debò: mirar només si «és més gran» sense
                                   comptar les vegades, i confondre'l amb
                                   sumar-hi el mateix nombre en lloc de
                                   multiplicar-lo.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, quants, lectura, el } = CE;
  const Q = CE.q;
  const qu = n => quants(n, "comu.quadret", "comu.quadrets");

  /** Dues files de quadrets, alineades a l'esquerra: `n` quadrets a dalt,
      `n * k` a baix, amb ratlles fines a la fila de baix cada `n` quadrets. */
  function dibuixa(svg, n, k) {
    svg.textContent = "";
    const gran = n * k;
    const X0 = 14, AMP = 460, m = Math.max(9, Math.min(30, (AMP - X0 - 16) / gran));
    const y0 = 10, salt = m + 20;
    Q.rectangle(svg, X0, y0, 1, n, m, "q");
    Q.rectangle(svg, X0, y0 + salt, 1, gran, m, "q b");
    for (let i = 1; i < k; i++) {
      const x = X0 + i * n * m;
      svg.appendChild(el("line", { x1: x, y1: y0 + salt + 3, x2: x, y2: y0 + salt + m - 3, class: "q-fina" }));
    }
    Q.text(svg, X0 + (n * m) / 2, y0 + m + 14, qu(n), "q-num", 14);
    Q.text(svg, X0 + (gran * m) / 2, y0 + salt + m + 14, qu(gran), "q-num", 14);
    svg.setAttribute("viewBox", "0 0 " + AMP + " " + Math.round(y0 + salt + m + 30));
  }

  function paraules(n, k) {
    return [
      txt("17.1.la_fila", { quadrets: qu(n) }),
      txt(k === 2 ? "17.1.el_doble" : "17.1.el_triple", { quadrets: qu(n * k) }),
      txt("17.1.hi_cap", { vegades: quants(k, "17.1.vegada", "17.1.vegades"), quadrets: qu(n) })
    ];
  }
  const igualtat = (n, k) => n + " · " + k + " = " + (n * k);

  /* ==================================== 17.1 · El doble i el triple ====== */

  const KS = [{ et: txtPla("17.1.doble"), k: 2 }, { et: txtPla("17.1.triple"), k: 3 }];
  const EX171 = { n: 3, k: 2 };
  let n1 = EX171.n, k1 = EX171.k;

  function pinta1() {
    dibuixa($("#dt-svg"), n1, k1);
    $("#dt-svg").setAttribute("aria-label", txtPla(k1 === 2 ? "17.1.aria_doble" : "17.1.aria_triple", { n: n1, r: n1 * k1 }));
    $("#dt-lectura").innerHTML = lectura(paraules(n1, k1), igualtat(n1, k1));
    $("#dt-marca").hidden = !(n1 === EX171.n && k1 === EX171.k);
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    CE.comptador($("#dt-n"), { et: txt("17.1.et_n"), min: 2, max: 9, valor: n1, aoCanviar: v => { n1 = v; pinta1(); } });
    CE.pastilles($("#dt-pastilles"), KS.map((o, k) => ({ et: o.et, k })), t => { k1 = KS[t.k].k; pinta1(); },
      KS.findIndex(o => o.k === EX171.k));
    pinta1();
  }

  /* ============================== 17.2 · Quantes vegades hi cap? ====== */

  // [n, k]: deu casos, amb n de 2 a 9 i k de 2 o 3, tots dins de la targeta.
  const CASOS = [[3, 2], [3, 3], [5, 2], [5, 3], [7, 2], [4, 3], [6, 2], [8, 2], [9, 2], [2, 3]];
  const N2 = 5;
  let t2 = null, c2 = null, i2 = 0;

  function pas2(i, e) {
    c2 = CASOS[e.extra.ordre[i]]; i2 = 0;
    const [n, k] = c2;
    dibuixa($("#dq-svg"), n, k);
    $("#dq-svg").setAttribute("aria-label", txtPla("17.2.aria", { n, r: n * k }));
    const cont = $("#dq-opcions");
    cont.innerHTML = KS.map((o, kk) => '<button type="button" class="btn opcio-sino opcio-dt" data-k="' + kk + '">' +
      o.et + "</button>").join("");
    $$(".opcio-dt", cont).forEach(b => { b.onclick = () => tria2(KS[Number(b.dataset.k)].k, b); });
    const avis = $("#dq-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("17.2.comenca");
    $("#dq-seguent").disabled = !t2.resolt();
    $("#dq-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() {
    const [, k] = c2;
    $$(".opcio-dt", $("#dq-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", KS[Number(b.dataset.k)].k === k); });
  }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const [n, kBo] = c2, avis = $("#dq-avis");
    const frase = txt("17.2.encert", { n, r: n * kBo, k: kBo });
    if (k === kBo) { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt("17.2.error"), txt("17.2.pista", { n }));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); }
    $("#dq-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 17, sub: 2,
      recorregut: $("#dq-recorregut"), represa: $("#dq-represa"), final: $("#dq-final"), cos: [$("#dq-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => CASOS[i] !== undefined),
      nom: () => "17.2 · " + txtPla("17.2.nom"),
      pinta: pas2
    });
    $("#dq-seguent").onclick = () => t2.seguent();
    // Cinc passos: tres dobles i dos triples, barrejats (hi ha 7 dobles i 3 triples als CASOS).
    t2.inicia(() => {
      const idx = CASOS.map((_, i) => i);
      const dobles = CE.barreja(idx.filter(i => CASOS[i][1] === 2)).slice(0, 3);
      const triples = CE.barreja(idx.filter(i => CASOS[i][1] === 3)).slice(0, 2);
      return { total: N2, extra: { ordre: CE.barreja(dobles.concat(triples)) } };
    });
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-dobletriple");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(17) || 1);
  }
  CE.registra("dobletriple", inicia);
  CE.registraCataleg("17.2", { nom: txtPla("17.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { dobletriple: { EX171, CASOS } });
})();
