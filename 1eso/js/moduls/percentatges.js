/* ============================================================================
   ELS PERCENTATGES — mòdul «percentatges» de la caixa d'eines · tasca 16 ·
   unitat 4
   ----------------------------------------------------------------------------
   Un percentatge és quants quadrets de cada 100: el 25% és 25 quadrets de 100
   pintats a la graella (lliga amb la graella de 100 dels múltiples, unitat 2).
   Els percentatges habituals es relacionen amb la fracció que ja es coneix:
   50% és 1/2, 25% és 1/4, 75% és 3/4, 20% és 1/5 i 10% és 1/10. Activitat 7 de
   la situació «És gran l'ou del kiwi?».
   16.1 · PINTA EL PERCENTATGE   pastilles amb els cinc percentatges habituals;
                                 la graella de 100 amb els quadrets pintats i
                                 la fracció coneguda. S'obre amb el 25%.
   16.2 · QUIN PERCENTATGE ÉS?   tasca tancada de cinc passos: una graella ja
                                 pintada i tres percentatges per triar. Les
                                 dolentes són les confusions de debò: comptar
                                 les files pintades en lloc dels quadrets, i
                                 dir sempre 100% encara que no estigui plena.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, lectura } = CE;
  const Q = CE.q;

  // Percentatge → la fracció coneguda (unitat 3, denominador fins a 12).
  const FRACCIO = { 10: [1, 10], 20: [1, 5], 25: [1, 4], 50: [1, 2], 75: [3, 4] };
  const HABITUALS = [10, 20, 25, 50, 75];

  function dibuixa(svg, p) {
    svg.textContent = "";
    Q.graella100(svg, n => (n <= p ? "marca" : null));
    svg.setAttribute("aria-label", txtPla("16.1.aria", { p }));
  }

  function paraules(p) {
    const f = FRACCIO[p];
    const p1 = [txt("16.1.quants", { p })];
    if (f) p1.push(txt("16.1.es_la_fraccio", { f: Q.htmlFraccio(f[0], f[1]) }));
    return p1;
  }

  /* ==================================== 16.1 · Pinta el percentatge ====== */

  const EX161 = 25;
  let p1 = EX161;
  function pinta1() {
    dibuixa($("#pc-svg"), p1);
    $("#pc-lectura").innerHTML = lectura(paraules(p1), p1 + " %");
    $("#pc-marca").hidden = p1 !== EX161;
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    CE.pastilles($("#pc-pastilles"), HABITUALS.map((p, k) => ({ et: p + " %", k })),
      t => { p1 = HABITUALS[t.k]; pinta1(); }, HABITUALS.indexOf(EX161));
    pinta1();
  }

  /* ================================= 16.2 · Quin percentatge és? ====== */

  const N2 = 5;
  let t2 = null, p2 = 0, i2 = 0, opcions2 = [];

  /** Les tres opcions: la bona, confondre el que hi ha amb el que falta
      (100 − p: pintar 25 i dir «75%»; amb el 50%, on coincidirien, la
      confusió és el 25% del costat), i dir 100% sempre encara que la
      graella no estigui plena. */
  function opcionsDe(p) {
    return [["bona", p], ["falta", p === 50 ? 25 : 100 - p], ["cent", 100]];
  }
  function pas2(i, e) {
    p2 = HABITUALS[e.extra.ordre[i]]; i2 = 0;
    dibuixa($("#pq-svg"), p2);
    opcions2 = e.extra.torns[i].map(k => opcionsDe(p2)[k]);
    const cont = $("#pq-opcions");
    cont.innerHTML = opcions2.map((o, k) => '<button type="button" class="btn opcio-sino opcio-pc" data-k="' + k + '">' +
      o[1] + " %</button>").join("");
    $$(".opcio-pc", cont).forEach(b => { b.onclick = () => tria2(Number(b.dataset.k), b); });
    const avis = $("#pq-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("16.2.comenca");
    $("#pq-seguent").disabled = !t2.resolt();
    $("#pq-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() { $$(".opcio-pc", $("#pq-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", opcions2[b.dataset.k][0] === "bona"); }); }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const o = opcions2[k], avis = $("#pq-avis");
    const frase = txt("16.2.encert", { p: p2 });
    if (o[0] === "bona") { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(o[0] === "falta" ? "16.2.error_falta" : "16.2.error_cent"), txt("16.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); }
    $("#pq-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 16, sub: 2,
      recorregut: $("#pq-recorregut"), represa: $("#pq-represa"), final: $("#pq-final"), cos: [$("#pq-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => HABITUALS[i] !== undefined) && Array.isArray(e.extra.torns),
      nom: () => "16.2 · " + txtPla("16.2.nom"),
      pinta: pas2
    });
    $("#pq-seguent").onclick = () => t2.seguent();
    // Cinc passos amb els cinc percentatges habituals, un cop cadascun, barrejats.
    t2.inicia(() => ({ total: N2, extra: { ordre: CE.barreja(HABITUALS.map((_, i) => i)),
                                           torns: Array.from({ length: N2 }, () => CE.barreja([0, 1, 2])) } }));
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-percentatges");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(16) || 1);
  }
  CE.registra("percentatges", inicia);
  CE.registraCataleg("16.2", { nom: txtPla("16.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { percentatges: { HABITUALS, FRACCIO } });
})();
