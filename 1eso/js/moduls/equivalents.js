/* ============================================================================
   EQUIVALENTS — mòdul «equivalents» de la caixa d'eines · tasca 10 · unitat 4
   ----------------------------------------------------------------------------
   Dues fraccions són equivalents si pinten el mateix tros del mateix rectangle.
   Partir cada tros en k és amplificar: dalt i baix, per k. Activitats 3, 5 i 6.
   10.1 · PARTEIX ELS TROSSOS  una fracció i «parteix cada tros en k»; a sota, la
                               fracció nova. Cap denominador passa de 12. S'obre
                               amb 2/3 = 8/12, l'exemple de l'activitat 3 del grup.
   10.2 · SÓN EQUIVALENTS?     tasca tancada de cinc passos, amb els dos dibuixos.
   ========================================================================== */
(function () {
  "use strict";
  const { $, txt, txtPla, omplirTextos, retroaccio, lectura } = CE;
  const Q = CE.q;

  function dues(svg, a, b, c, d, k) {
    svg.textContent = "";
    // A l'esquerra de cada rectangle, la seva fracció: el de dalt és la primera.
    const y2 = 10 + Q.TIRA.H + 22;
    Q.text(svg, 38, 10 + Q.TIRA.H / 2 + 1, a + "/" + b, "q-text fort", 20);
    Q.text(svg, 38, y2 + Q.TIRA.H / 2 + 1, c + "/" + d, "q-text fort", 20);
    Q.tira(svg, 70, 10, b, a, { k: k || 1, W: 300 });
    Q.tira(svg, 70, y2, d, c, { W: 300 });
    svg.setAttribute("viewBox", "0 0 380 " + (Q.TIRA.H * 2 + 42));
    svg.setAttribute("aria-label", Q.nomFraccio(a, b) + " i " + Q.nomFraccio(c, d));
  }

  /* ======================================= 10.1 · Parteix els trossos ====== */
  const EX = { n: 2, d: 3, k: 4 };
  let n1 = EX.n, d1 = EX.d, k1 = EX.k;
  const cfgN = { min: 1, max: 5, valor: n1 }, cfgK = { min: 1, max: 4, valor: k1 };
  let comptN = null, comptK = null;
  function pinta1() {
    cfgN.max = d1 - 1;
    if (n1 > cfgN.max) { n1 = cfgN.max; comptN.posa(n1); }
    cfgK.max = Math.max(1, Math.floor(12 / d1));
    if (k1 > cfgK.max) { k1 = cfgK.max; comptK.posa(k1); }
    comptN.posa(n1); comptK.posa(k1);
    dues($("#ea-svg"), n1, d1, n1 * k1, d1 * k1, k1);
    const f1 = Q.htmlFraccio(n1, d1), f2 = Q.htmlFraccio(n1 * k1, d1 * k1);
    $("#ea-lectura").innerHTML = lectura(k1 === 1 ? [txt("10.1.mateixa")] : [
      txt("10.1.iguals", { f1, f2 }),
      txt("10.1.com", { k: k1, n: n1, d: d1, nk: n1 * k1, dk: d1 * k1 }),
      txt("10.1.amplificar"),
    ], k1 === 1 ? f1 : f1 + " = " + f2);
    $("#ea-marca").hidden = !(n1 === EX.n && d1 === EX.d && k1 === EX.k);
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    CE.comptador($("#ea-d"), { et: txt("10.1.et_d"), min: 2, max: 6, valor: d1, aoCanviar: v => { d1 = v; pinta1(); } });
    comptN = CE.comptador($("#ea-n"), Object.assign(cfgN, { et: txt("10.1.et_n"), aoCanviar: v => { n1 = v; pinta1(); } }));
    comptK = CE.comptador($("#ea-k"), Object.assign(cfgK, { et: txt("10.1.et_k"), aoCanviar: v => { k1 = v; pinta1(); } }));
    pinta1();
  }

  /* ======================================== 10.2 · Són equivalents? ====== */
  const PARELLES = [[1, 2, 2, 4], [2, 3, 4, 6], [1, 3, 2, 6], [3, 4, 6, 8], [2, 5, 4, 10], [2, 4, 3, 6],
                    [1, 2, 2, 3], [2, 3, 3, 4], [1, 4, 2, 6], [3, 5, 5, 10]];
  const N2 = 5;
  let t2 = null, c2 = null, i2 = 0, triat2 = null;
  const iguals = ([a, b, c, d]) => a * d === b * c;
  function pas2(i, e) {
    c2 = PARELLES[e.extra.ordre[i]]; i2 = 0; triat2 = null;
    const [a, b, c, d] = c2;
    dues($("#eb-svg"), a, b, c, d);
    $("#eb-pregunta").innerHTML = txt("10.2.pregunta", { f1: Q.htmlFraccio(a, b), f2: Q.htmlFraccio(c, d) });
    CE.botonsSiNo($("#eb-opcions"), tria2);
    const avis = $("#eb-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("10.2.comenca");
    $("#eb-seguent").disabled = !t2.resolt();
    $("#eb-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    CE.pintaSiNo($("#eb-opcions"), null, iguals(c2), t2.resolt());
  }
  function tria2(si) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const bo = iguals(c2), avis = $("#eb-avis");
    triat2 = si;
    if (si === bo) { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", txt(bo ? "10.2.es" : "10.2.no_es")); }
    else if (i2 === 0) { i2 = 1; retroaccio(avis, "error", txt(si ? "10.2.has_dit_si" : "10.2.has_dit_no"), txt("10.2.pista")); }
    else { t2.anota("mostrat"); retroaccio(avis, "mostra", txt(bo ? "10.2.es" : "10.2.no_es")); }
    CE.pintaSiNo($("#eb-opcions"), triat2, bo, t2.resolt());
    $("#eb-seguent").disabled = !t2.resolt();
  }
  function nouOrdre2() {
    const idx = PARELLES.map((_, i) => i);
    return CE.barreja(CE.barreja(idx.filter(i => iguals(PARELLES[i]))).slice(0, 3)
      .concat(CE.barreja(idx.filter(i => !iguals(PARELLES[i]))).slice(0, 2)));
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 10, sub: 2,
      recorregut: $("#eb-recorregut"), represa: $("#eb-represa"), final: $("#eb-final"), cos: [$("#eb-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => PARELLES[i] !== undefined),
      nom: () => "10.2 · " + txtPla("10.2.nom"),
      pinta: pas2
    });
    $("#eb-seguent").onclick = () => t2.seguent();
    t2.inicia(() => ({ total: N2, extra: { ordre: nouOrdre2() } }));
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-equivalents");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(10) || 1);
  }
  CE.registra("equivalents", inicia);
  CE.registraCataleg("10.2", { nom: txtPla("10.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { equivalents: { EX, PARELLES } });
})();
