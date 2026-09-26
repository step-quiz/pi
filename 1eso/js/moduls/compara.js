/* ============================================================================
   COMPARA — mòdul «compara» de la caixa d'eines · tasca 11 · unitat 4
   ----------------------------------------------------------------------------
   Quina fracció és més gran? Amb el mateix rectangle, la que té el tros pintat
   més llarg. Activitats 2 i 4 del grup, sense el valor numèric (regla C).
   La regla trencada: «com més gran és el de baix, més gran és la fracció».
   11.1 · COMPARA DUES FRACCIONS  s'obre amb 1/3 i 1/5, la regla trencada.
   11.2 · QUINA ÉS MÉS GRAN?      tasca tancada de cinc passos, amb els dibuixos.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, lectura } = CE;
  const Q = CE.q;

  function dues(svg, a, b, c, d) {
    svg.textContent = "";
    // A l'esquerra de cada rectangle, la seva fracció: el de dalt és la primera.
    const y2 = 10 + Q.TIRA.H + 22;
    Q.text(svg, 38, 10 + Q.TIRA.H / 2 + 1, a + "/" + b, "q-text fort", 20);
    Q.text(svg, 38, y2 + Q.TIRA.H / 2 + 1, c + "/" + d, "q-text fort", 20);
    Q.tira(svg, 70, 10, b, a, { W: 300 });
    Q.tira(svg, 70, y2, d, c, { W: 300 });
    svg.setAttribute("viewBox", "0 0 380 " + (Q.TIRA.H * 2 + 42));
    svg.setAttribute("aria-label", Q.nomFraccio(a, b) + " i " + Q.nomFraccio(c, d));
  }
  const compara = (a, b, c, d) => Math.sign(a * d - c * b);    // 1: la primera és més gran

  /* ===================================== 11.1 · Compara dues fraccions ====== */
  const EX = [1, 3, 1, 5];
  let v = EX.slice();
  function pinta1() {
    const [a, b, c, d] = v;
    dues($("#ca-svg"), a, b, c, d);
    const f1 = Q.htmlFraccio(a, b), f2 = Q.htmlFraccio(c, d), s = compara(a, b, c, d);
    const par = [s > 0 ? txt("11.1.gran", { f1, f2 }) : s < 0 ? txt("11.1.petita", { f1, f2 }) : txt("11.1.iguals", { f1, f2 })];
    if (b === d && a !== c) par.push(txt("11.1.mateix_den"));
    if (a === c && b !== d) par.push(txt("11.1.mateix_num"));
    $("#ca-lectura").innerHTML = lectura(par);
    $("#ca-marca").hidden = v.join() !== EX.join();
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    const fes = (id, i, et, sub, min, max) => CE.comptador($(id), { et: txt(et), sub: txt(sub), min, max, valor: v[i],
      aoCanviar: x => { v[i] = x; pinta1(); } });
    fes("#ca-a", 0, "11.1.pintats", "11.1.primera", 0, 12); fes("#ca-b", 1, "11.1.trossos", "11.1.primera", 2, 12);
    fes("#ca-c", 2, "11.1.pintats", "11.1.segona", 0, 12); fes("#ca-d", 3, "11.1.trossos", "11.1.segona", 2, 12);
    pinta1();
  }

  /* ======================================== 11.2 · Quina és més gran? ====== */
  // [a, b, c, d]: cap parell igual. Els quatre primers tenen el mateix numerador: la regla trencada.
  const PARELLES = [[1, 3, 1, 5], [2, 7, 2, 5], [1, 6, 1, 4], [3, 8, 3, 5],
                    [3, 5, 2, 5], [3, 4, 2, 3], [1, 2, 3, 8], [5, 6, 2, 3], [1, 6, 2, 5], [4, 9, 1, 2]];
  const N2 = 5;
  let t2 = null, c2 = null, i2 = 0;
  function pas2(i, e) {
    c2 = PARELLES[e.extra.ordre[i]]; i2 = 0;
    const [a, b, c, d] = c2;
    dues($("#cb-svg"), a, b, c, d);
    const cont = $("#cb-opcions");
    cont.innerHTML = [[a, b], [c, d]].map((f, k) => '<button type="button" class="btn opcio-sino opcio-frac" data-k="' + k + '">' +
      Q.htmlFraccio(f[0], f[1]) + "</button>").join("");
    $$(".opcio-frac", cont).forEach(b => { b.onclick = () => tria2(Number(b.dataset.k), b); });
    const avis = $("#cb-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("11.2.comenca");
    $("#cb-seguent").disabled = !t2.resolt();
    $("#cb-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca();
  }
  const bona = () => (compara(...c2) > 0 ? 0 : 1);
  function marca() { $$(".opcio-frac", $("#cb-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", Number(b.dataset.k) === bona()); }); }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const [a, b, c, d] = c2, avis = $("#cb-avis");
    const gran = bona() === 0 ? [a, b, c, d] : [c, d, a, b];
    const frase = txt("11.2.encert", { f1: Q.htmlFraccio(gran[0], gran[1]), f2: Q.htmlFraccio(gran[2], gran[3]) });
    if (k === bona()) { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca(); }
    else if (i2 === 0) { i2 = 1; boto.classList.add("mal"); boto.disabled = true; retroaccio(avis, "error", txt("11.2.error"), txt("11.2.pista")); }
    else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca(); }
    $("#cb-seguent").disabled = !t2.resolt();
  }
  function nouOrdre2() {
    const idx = PARELLES.map((_, i) => i);
    return CE.barreja(CE.barreja(idx.slice(0, 4)).slice(0, 2).concat(CE.barreja(idx.slice(4)).slice(0, 3)));
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 11, sub: 2,
      recorregut: $("#cb-recorregut"), represa: $("#cb-represa"), final: $("#cb-final"), cos: [$("#cb-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => PARELLES[i] !== undefined),
      nom: () => "11.2 · " + txtPla("11.2.nom"),
      pinta: pas2
    });
    $("#cb-seguent").onclick = () => t2.seguent();
    t2.inicia(() => ({ total: N2, extra: { ordre: nouOrdre2() } }));
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-compara");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(11) || 1);
  }
  CE.registra("compara", inicia);
  CE.registraCataleg("11.2", { nom: txtPla("11.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { compara: { EX, PARELLES } });
})();
