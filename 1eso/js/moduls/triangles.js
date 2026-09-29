/* ============================================================================
   ELS TRIANGLES — mòdul «triangles» de la caixa d'eines · tasca 24 · unitat 6
   ----------------------------------------------------------------------------
   Els tres angles d'un triangle, posats un al costat de l'altre, fan un angle
   pla: és el que el grup fa retallant cartolines (el llibre: UD6, activitat
   5). I un triangle es diu pels seus angles, comparats amb la cantonada del
   quadret: rectangle, obtusangle o acutangle. Els costats iguals (equilàter,
   isòsceles, escalè) es fan a la fitxa, amb marques.

   24.1 · ELS TRES ANGLES    cinc triangles al geoplà per triar, cada angle
                             amb el seu número, i els tres angles junts, que
                             fan un angle pla. N'hi ha un de petit i un de
                             gran: la regla trencada de la fitxa 3 és «un
                             triangle més gran té els angles més grans». Diu
                             quin triangle és pels angles.
   24.2 · QUIN TRIANGLE ÉS?  tasca tancada de cinc passos: un triangle i tres
                             noms. Un dels rectangles està girat: el tipus no
                             depèn de com està posat.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, lectura } = CE;
  const Q = CE.q;

  // 24.1: un de petit i un de gran (acutangles), un rectangle, un obtusangle i un girat.
  const TRIANGLES = [[[1, 3], [3, 3], [2, 1]], [[0, 5], [5, 5], [2, 0]], [[0, 4], [4, 4], [0, 0]],
                     [[0, 4], [5, 4], [1, 3]], [[2, 0], [5, 3], [0, 2]]];
  // 24.2: tres de cada tipus (el tipus es calcula; les proves ho comproven).
  const CASOS = [[[0, 4], [4, 4], [0, 0]], [[2, 0], [5, 3], [0, 2]], [[0, 3], [5, 3], [5, 0]],
                 [[0, 4], [4, 4], [2, 0]], [[0, 4], [5, 4], [3, 0]], [[1, 0], [5, 2], [0, 4]],
                 [[0, 4], [5, 4], [1, 3]], [[0, 1], [5, 4], [2, 4]], [[0, 3], [4, 0], [2, 2]]];
  const TIPUS = ["rectangle", "acutangle", "obtusangle"];

  /* =========================================== 24.1 · Els tres angles ====== */

  const EX241 = 2;                                         // el rectangle
  let k1 = EX241;
  function pinta1() {
    const pts = TRIANGLES[k1];
    Q.triangle($("#tr-svg"), pts, { arcs: true });
    $("#tr-svg").setAttribute("aria-label", txtPla("24.1.aria_tri"));
    Q.anglesJunts($("#tr-junts"), pts);
    $("#tr-junts").setAttribute("aria-label", txtPla("24.1.aria_junts"));
    $("#tr-lectura").innerHTML = lectura([txt("24.1.junts"), txt("24.1.sempre"), txt("24.1." + Q.tipusTriangle(pts))]);
    $("#tr-marca").hidden = k1 !== EX241;
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    CE.pastilles($("#tr-pastilles"), TRIANGLES.map((t, k) => ({ et: txtPla("24.1.triangle_n", { n: k + 1 }), k })),
      t => { k1 = t.k; pinta1(); }, EX241);
    pinta1();
  }

  /* ========================================= 24.2 · Quin triangle és? ====== */

  const N2 = 5;
  let t2 = null, pts2 = null, i2 = 0;
  function pas2(i, e) {
    pts2 = CASOS[e.extra.ordre[i]]; i2 = 0;
    Q.triangle($("#ts-svg"), pts2, { arcs: false });
    const as = Q.anglesTriangle(pts2).map(a => Math.round(a.g));
    $("#ts-svg").setAttribute("aria-label", txtPla("24.2.aria", { a: as[0], b: as[1], c: as[2] }));
    const cont = $("#ts-opcions");
    cont.innerHTML = TIPUS.map(t => '<button type="button" class="btn opcio-sino opcio-geo" data-t="' + t + '">' +
      txt("24.2.opcio_" + t) + "</button>").join("");
    $$(".opcio-geo", cont).forEach(b => { b.onclick = () => tria2(b.dataset.t, b); });
    const avis = $("#ts-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("24.2.comenca");
    $("#ts-seguent").disabled = !t2.resolt();
    $("#ts-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() {
    const bona = Q.tipusTriangle(pts2);
    $$(".opcio-geo", $("#ts-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", b.dataset.t === bona); });
    Q.triangle($("#ts-svg"), pts2, { arcs: true });
  }
  function tria2(t, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const bona = Q.tipusTriangle(pts2), avis = $("#ts-avis"), frase = txt("24.1." + bona);
    if (t === bona) { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      Q.triangle($("#ts-svg"), pts2, { arcs: true });             // la pista: els tres angles, marcats
      retroaccio(avis, "error", txt("24.2.error_" + t), txt("24.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); }
    $("#ts-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 24, sub: 2,
      recorregut: $("#ts-recorregut"), represa: $("#ts-represa"), final: $("#ts-final"), cos: [$("#ts-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => CASOS[i] !== undefined),
      nom: () => "24.2 · " + txtPla("24.2.nom"),
      pinta: pas2
    });
    $("#ts-seguent").onclick = () => t2.seguent();
    // Cinc passos: el rectangle girat sempre, un de cada tipus més, i un a l'atzar.
    t2.inicia(() => {
      const per = t => CE.barreja(CASOS.map((c, i) => i).filter(i => i !== 1 && Q.tipusTriangle(CASOS[i]) === t));
      const tres = TIPUS.map(t => per(t)[0]);
      const resta = CE.barreja(CASOS.map((c, i) => i).filter(i => i !== 1 && !tres.includes(i)))[0];
      return { total: N2, extra: { ordre: CE.barreja([1].concat(tres, [resta])) } };
    });
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-triangles");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(24) || 1);
  }
  CE.registra("triangles", inicia);
  CE.registraCataleg("24.2", { nom: txtPla("24.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { triangles: { TRIANGLES, CASOS } });
})();
