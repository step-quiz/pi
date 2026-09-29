/* ============================================================================
   ELS POLÍGONS — mòdul «poligons» de la caixa d'eines · tasca 23 · unitat 6
   ----------------------------------------------------------------------------
   Els polígons al geoplà (una quadrícula de punts): quants costats i quants
   vèrtexs tenen, i com es diuen. Activitat «Polígons» de la situació «Sentit
   espacial» (el llibre: UD6, activitat 4).

   23.1 · EL POLÍGON AL GEOPLÀ  set polígons per triar. Diu quants costats i
                                vèrtexs té, el nom, i si és un quadrat (també
                                girat: la regla trencada de la fitxa 2, «un
                                quadrat girat ja no és un quadrat»), un
                                rectangle o un còncau. S'obre amb el rectangle.
   23.2 · COM ES DIU?           tasca tancada de cinc passos: un polígon al
                                geoplà i quatre noms (triangle, quadrilàter,
                                pentàgon i hexàgon). Hi ha quadrats girats i
                                polígons còncaus, que són on es compta malament.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, quants, lectura } = CE;
  const Q = CE.q;

  // [clau del nom a la pastilla, vèrtexs al geoplà, nota]
  const FORMES = [
    ["p_triangle", [[1, 4], [4, 4], [2, 1]], null],
    ["p_quadrat", [[1, 1], [4, 1], [4, 4], [1, 4]], "nota_quadrat"],
    ["p_rectangle", [[0, 1], [5, 1], [5, 4], [0, 4]], "nota_rectangle"],
    ["p_girat", [[2, 0], [4, 2], [2, 4], [0, 2]], "nota_girat"],
    ["p_pentagon", [[2, 0], [5, 2], [4, 5], [1, 5], [0, 2]], null],
    ["p_hexagon", [[1, 0], [4, 0], [5, 2], [4, 4], [1, 4], [0, 2]], null],
    ["p_concau", [[0, 0], [5, 0], [5, 5], [3, 5], [3, 2], [0, 2]], "nota_concau"]
  ];
  const NOMS = { 3: "nom_3", 4: "nom_4", 5: "nom_5", 6: "nom_6" };

  function dibuixa(svg, pts) {
    Q.geopla(svg, pts);
    svg.setAttribute("aria-label", txtPla("23.1.aria", { n: pts.length }));
  }

  /* ========================================= 23.1 · El polígon al geoplà ====== */

  const EX231 = 2;                                         // el rectangle
  let k1 = EX231;
  function pinta1() {
    const [, pts, nota] = FORMES[k1], n = pts.length;
    dibuixa($("#po-svg"), pts);
    const par = [txt("23.1.te", { costats: quants(n, "comu.costat", "comu.costats"), vertexs: quants(n, "comu.vertex", "comu.vertexs") }),
                 txt("23.1.es", { nom: txtPla("23.1." + NOMS[n]) })];
    if (nota) par.push(txt("23.1." + nota));
    $("#po-lectura").innerHTML = lectura(par);
    $("#po-marca").hidden = k1 !== EX231;
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    CE.pastilles($("#po-pastilles"), FORMES.map((f, k) => ({ et: txtPla("23.1." + f[0]), k })), t => { k1 = t.k; pinta1(); }, EX231);
    pinta1();
  }

  /* ================================================== 23.2 · Com es diu? ====== */

  // Els polígons de la tasca tancada: índexs de FORMES, i dos de més (un triangle girat i
  // un pentàgon còncau), perquè no sempre siguin els de la 23.1.
  const EXTRA = [[[0, 0], [5, 2], [1, 5]], [[0, 0], [5, 0], [5, 5], [2, 3], [0, 5]]];
  const CASOS = FORMES.map(f => f[1]).concat(EXTRA);
  const OPCIONS = [3, 4, 5, 6];
  const N2 = 5;
  let t2 = null, pts2 = null, i2 = 0;

  function pas2(i, e) {
    pts2 = CASOS[e.extra.ordre[i]]; i2 = 0;
    dibuixa($("#pp-svg"), pts2);
    const cont = $("#pp-opcions");
    cont.innerHTML = OPCIONS.map(n => '<button type="button" class="btn opcio-sino opcio-geo" data-n="' + n + '">' +
      txt("23.1." + NOMS[n]) + "</button>").join("");
    $$(".opcio-geo", cont).forEach(b => { b.onclick = () => tria2(Number(b.dataset.n), b); });
    const avis = $("#pp-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("23.2.comenca");
    $("#pp-seguent").disabled = !t2.resolt();
    $("#pp-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() {
    $$(".opcio-geo", $("#pp-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", Number(b.dataset.n) === pts2.length); });
  }
  function tria2(n, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const bona = pts2.length, avis = $("#pp-avis");
    const frase = txt("23.2.encert", { costats: quants(bona, "comu.costat", "comu.costats"), nom: txtPla("23.1." + NOMS[bona]) });
    if (n === bona) { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(n < bona ? "23.2.error_menys" : "23.2.error_mes"), txt("23.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); }
    $("#pp-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 23, sub: 2,
      recorregut: $("#pp-recorregut"), represa: $("#pp-represa"), final: $("#pp-final"), cos: [$("#pp-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => CASOS[i] !== undefined),
      nom: () => "23.2 · " + txtPla("23.2.nom"),
      pinta: pas2
    });
    $("#pp-seguent").onclick = () => t2.seguent();
    // Cinc passos: el quadrat girat i un còncau sempre, i tres més.
    t2.inicia(() => {
      const fixos = [3, 6], resta = CE.barreja(CASOS.map((c, i) => i).filter(i => !fixos.includes(i))).slice(0, 3);
      return { total: N2, extra: { ordre: CE.barreja(fixos.concat(resta)) } };
    });
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-poligons");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(23) || 1);
  }
  CE.registra("poligons", inicia);
  CE.registraCataleg("23.2", { nom: txtPla("23.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { poligons: { FORMES, CASOS } });
})();
