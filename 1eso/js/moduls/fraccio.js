/* ============================================================================
   LA FRACCIÓ — mòdul «fraccio» de la caixa d'eines · tasca 9 · unitat 4
   ----------------------------------------------------------------------------
   Una fracció és un rectangle partit en trossos iguals: el denominador diu quants
   trossos hi ha, i el numerador, quants se'n pinten. Activitats 0 i 2 del grup.
   9.1 · FES LA FRACCIÓ   dos comptadors; el dibuix, el nom (amb la targeta de les
                          fraccions) i el tipus. S'obre amb 4/9, com l'activitat 0.
   9.2 · QUINA FRACCIÓ ÉS? tasca tancada de cinc passos: un dibuix i tres fraccions.
                          Les dolentes són les dues confusions de debò: els nombres
                          girats i comptar els trossos blancs.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, quants, lectura } = CE;
  const Q = CE.q;

  function dibuixa(svg, n, d) {
    svg.textContent = "";
    const h = Q.fraccio(svg, 10, 10, n, d);
    svg.setAttribute("viewBox", "0 0 380 " + (h + 20));
    svg.setAttribute("aria-label", txtPla("9.2.aria", { n, d }));
  }
  CE.dibuixaFraccio = dibuixa;

  /* ============================================ 9.1 · Fes la fracció ====== */
  const EX = { n: 4, d: 9 };
  let n1 = EX.n, d1 = EX.d;
  function pinta1() {
    dibuixa($("#fa-svg"), n1, d1);
    const t = Q.tipusFraccio(n1, d1);
    $("#fa-lectura").innerHTML = lectura([
      txt("9.1.total", { d: d1 }),
      txt("9.1.pintats", { pintats: quants(n1, "9.1.tros_pintat", "9.1.trossos_pintats"), n: n1 }),
      txt("9.1.llegeix", { nom: Q.nomFraccio(n1, d1) }),
      txt({ nulla: "9.1.nulla", propia: "9.1.propia", unitat: "9.1.unitat", impropia: "9.1.impropia" }[t]),
    ], Q.htmlFraccio(n1, d1));
    $("#fa-marca").hidden = !(n1 === EX.n && d1 === EX.d);
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    CE.comptador($("#fa-d"), { et: txt("9.1.et_d"), min: 2, max: 12, valor: d1, aoCanviar: v => { d1 = v; pinta1(); } });
    CE.comptador($("#fa-n"), { et: txt("9.1.et_n"), min: 0, max: 24, valor: n1, aoCanviar: v => { n1 = v; pinta1(); } });
    pinta1();
  }

  /* ========================================= 9.2 · Quina fracció és? ====== */
  const CASOS = [[4, 9], [3, 4], [2, 5], [5, 8], [1, 3], [2, 3], [7, 10], [5, 6], [3, 8], [1, 4]];
  const N2 = 5;
  let t2 = null, c2 = null, i2 = 0, opcions2 = [];
  /** Les tres opcions: la bona, la girada i la dels trossos blancs. */
  function opcionsDe(n, d) {
    const blancs = d - n !== n ? [d - n, d] : [n, d + 1];
    return [["bona", n, d], ["girada", d, n], ["blancs", blancs[0], blancs[1]]];
  }
  function pas2(i, e) {
    c2 = CASOS[e.extra.ordre[i]]; i2 = 0;
    const [n, d] = c2;
    dibuixa($("#fb-svg"), n, d);
    opcions2 = e.extra.torns[i].map(k => opcionsDe(n, d)[k]);
    const cont = $("#fb-opcions");
    cont.innerHTML = opcions2.map((o, k) => '<button type="button" class="btn opcio-sino opcio-frac" data-k="' + k + '">' +
      Q.htmlFraccio(o[1], o[2]) + "</button>").join("");
    $$(".opcio-frac", cont).forEach(b => { b.onclick = () => tria2(Number(b.dataset.k), b); });
    const avis = $("#fb-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("9.2.comenca");
    $("#fb-seguent").disabled = !t2.resolt();
    $("#fb-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) $$(".opcio-frac", cont).forEach(b => { b.disabled = true; b.classList.toggle("bona", opcions2[b.dataset.k][0] === "bona"); });
  }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const [n, d] = c2, o = opcions2[k], avis = $("#fb-avis");
    const encert = txt("9.2.encert", { f: Q.htmlFraccio(n, d), n, d, nom: Q.nomFraccio(n, d) });
    if (o[0] === "bona") {
      t2.anota(i2 === 0 ? "be" : "pista");
      retroaccio(avis, "encert", encert);
    } else if (i2 === 0) {
      i2 = 1;
      boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(o[0] === "girada" ? "9.2.error_girada" : "9.2.error_blancs"), txt("9.2.pista"));
    } else {
      t2.anota("mostrat");
      retroaccio(avis, "mostra", txt("9.2.mostra", { f: Q.htmlFraccio(n, d), n, d }));
    }
    if (t2.resolt()) $$(".opcio-frac", $("#fb-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", opcions2[b.dataset.k][0] === "bona"); });
    $("#fb-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 9, sub: 2,
      recorregut: $("#fb-recorregut"), represa: $("#fb-represa"), final: $("#fb-final"), cos: [$("#fb-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => CASOS[i] !== undefined) && Array.isArray(e.extra.torns),
      nom: () => "9.2 · " + txtPla("9.2.nom"),
      pinta: pas2
    });
    $("#fb-seguent").onclick = () => t2.seguent();
    t2.inicia(() => ({ total: N2, extra: { ordre: CE.barreja(CASOS.map((_, i) => i)).slice(0, N2),
                                           torns: Array.from({ length: N2 }, () => CE.barreja([0, 1, 2])) } }));
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-fraccio");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(9) || 1);
  }
  CE.registra("fraccio", inicia);
  CE.registraCataleg("9.2", { nom: txtPla("9.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { fraccio: { EX, CASOS } });
})();
