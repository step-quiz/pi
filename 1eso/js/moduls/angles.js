/* ============================================================================
   ELS ANGLES — mòdul «angles» de la caixa d'eines · tasca 22 · unitat 6
   ----------------------------------------------------------------------------
   La cantonada d'un quadret és l'angle recte. Un angle agut és més petit que la
   cantonada, un obtús és més gran, i un de pla és una recta. Sense
   transportador (decisió del docent del 29/9/2026). Activitat «Angles» de la
   situació «Sentit espacial» (el llibre: UD6, activitat 3).

   22.1 · OBRE L'ANGLE    dos comptadors: obrir o tancar l'angle (de 15 en 15
                          graus, sense ensenyar-ne el nombre) i la llargada dels
                          costats. La cantonada del quadret, discontínua, al
                          vèrtex. Diu quin angle és. La llargada dels costats no
                          canvia l'angle: és la regla trencada de la fitxa 1
                          («costats més llargs, angle més gran»). S'obre amb un
                          angle agut de costats llargs.
   22.2 · QUIN ANGLE ÉS?  tasca tancada de cinc passos: un angle, i quatre
                          respostes (agut, recte, obtús i pla). Els costats de
                          vegades són llargs i de vegades curts, perquè la
                          llargada no decideixi. La pista posa la cantonada al
                          vèrtex.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, lectura } = CE;
  const Q = CE.q;
  const LLARGS = [70, 105, 150];

  /* =============================================== 22.1 · Obre l'angle ====== */

  const EX221 = { k: 4, l: 3 };                        // 60 graus, costats llargs
  function pinta1(o) {
    const g = o.k * 15, t = Q.tipusAngle(g);
    Q.angle($("#an-svg"), g, { llarg: LLARGS[o.l - 1], cantonada: true });
    $("#an-svg").setAttribute("aria-label", txtPla("22.1.aria", { g }));
    $("#an-lectura").innerHTML = lectura([txt("22.1." + t), txt("22.1.llarg")], txtPla("22.1.nom_" + t));
    $("#an-marca").hidden = !(o.k === EX221.k && o.l === EX221.l);
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    const o = Object.assign({}, EX221);
    CE.comptador($("#an-k"), { et: txt("22.1.et_obre"), sub: txt("22.1.sub_obre"), min: 1, max: 12, valor: o.k,
      aoCanviar: v => { o.k = v; pinta1(o); } });
    $("#an-k output").hidden = true;             // el nombre de passos no vol dir res: es mira el dibuix
    CE.comptador($("#an-l"), { et: txt("22.1.et_llarg"), sub: txt("22.1.sub_llarg"), min: 1, max: 3, valor: o.l,
      aoCanviar: v => { o.l = v; pinta1(o); } });
    pinta1(o);
  }

  /* ============================================== 22.2 · Quin angle és? ====== */

  const CASOS = [30, 45, 60, 75, 90, 105, 120, 150, 180];
  const TIPUS = ["agut", "recte", "obtus", "pla"];
  const N2 = 5;
  let t2 = null, cas = null, i2 = 0;

  function pas2(i, e) {
    cas = e.extra.casos[i]; i2 = 0;
    Q.angle($("#ao-svg"), cas.g, { llarg: LLARGS[cas.l] });
    $("#ao-svg").setAttribute("aria-label", txtPla("22.1.aria", { g: cas.g }));
    const cont = $("#ao-opcions");
    cont.innerHTML = TIPUS.map(t => '<button type="button" class="btn opcio-sino opcio-geo" data-t="' + t + '">' +
      txt("22.2.opcio_" + t) + "</button>").join("");
    $$(".opcio-geo", cont).forEach(b => { b.onclick = () => tria2(b.dataset.t, b); });
    const avis = $("#ao-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("22.2.comenca");
    $("#ao-seguent").disabled = !t2.resolt();
    $("#ao-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() {
    const bona = Q.tipusAngle(cas.g);
    $$(".opcio-geo", $("#ao-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", b.dataset.t === bona); });
    Q.angle($("#ao-svg"), cas.g, { llarg: LLARGS[cas.l], cantonada: true });
  }
  function tria2(t, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const bona = Q.tipusAngle(cas.g), avis = $("#ao-avis"), frase = txt("22.1." + bona);
    if (t === bona) { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      // La pista és un camí diferent: la cantonada del quadret, dibuixada al vèrtex.
      Q.angle($("#ao-svg"), cas.g, { llarg: LLARGS[cas.l], cantonada: true });
      retroaccio(avis, "error", txt("22.2.error_" + t), txt("22.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); }
    $("#ao-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 22, sub: 2,
      recorregut: $("#ao-recorregut"), represa: $("#ao-represa"), final: $("#ao-final"), cos: [$("#ao-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.casos) && e.extra.casos.length === N2 &&
                   e.extra.casos.every(c => c && CASOS.includes(c.g) && [0, 1, 2].includes(c.l)),
      nom: () => "22.2 · " + txtPla("22.2.nom"),
      pinta: pas2
    });
    $("#ao-seguent").onclick = () => t2.seguent();
    // Cinc passos: un de cada tipus i un més, barrejats; la llargada dels costats, a l'atzar.
    t2.inicia(() => {
      const per = t => CE.barreja(CASOS.filter(g => Q.tipusAngle(g) === t));
      const gs = [per("agut")[0], 90, per("obtus")[0], 180, CE.barreja([per("agut")[1], per("obtus")[1]])[0]];
      const casos = CE.barreja(gs).map(g => ({ g, l: Math.floor(Math.random() * 3) }));
      return { total: N2, extra: { casos } };
    });
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-angles");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(22) || 1);
  }
  CE.registra("angles", inicia);
  CE.registraCataleg("22.2", { nom: txtPla("22.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { angles: { EX221, CASOS, TIPUS } });
})();
