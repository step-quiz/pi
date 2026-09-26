/* ============================================================================
   SUMA I RESTA — mòdul «sumes» de la caixa d'eines · tasca 12 · unitat 4
   ----------------------------------------------------------------------------
   Sempre amb el mateix denominador (decisió del docent del 26/9/2026): se sumen
   o es treuen els trossos pintats, i el denominador no canvia, perquè els
   trossos són els mateixos. Activitats 7 a 9 del grup, pintant.
   La regla trencada: «se sumen els de dalt i els de baix» (1/4 + 2/4 = 3/8).
   12.1 · SUMA I RESTA  s'obre amb 3/8 + 2/8 = 5/8.
   12.2 · QUANT ÉS?     tasca tancada de cinc passos, amb els trossos pintats i tres
                        resultats: el bo, el de sumar també els de baix, i un de més.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, lectura } = CE;
  const Q = CE.q;

  /** La suma pinta la primera en blau i la segona en taronja; la resta ratlla el que es treu. */
  function dibuixa(svg, a, b, d, resta) {
    svg.textContent = "";
    const h = resta ? Q.fraccio(svg, 10, 10, a, d, { treu: b }) : Q.fraccio(svg, 10, 10, a, d, { mes: b });
    svg.setAttribute("viewBox", "0 0 380 " + (h + 20));
  }
  const op = (a, b, d, resta) => Q.htmlFraccio(a, d) + (resta ? " − " : " + ") + Q.htmlFraccio(b, d);

  /* ============================================ 12.1 · Suma i resta ====== */
  const EX = { a: 3, b: 2, d: 8, resta: false };
  let a1 = EX.a, b1 = EX.b, d1 = EX.d, resta1 = EX.resta;
  function pinta1() {
    const bb = resta1 ? Math.min(b1, a1) : b1, r = resta1 ? a1 - bb : a1 + bb;
    dibuixa($("#sa-svg"), a1, bb, d1, resta1);
    $("#sa-svg").setAttribute("aria-label", Q.nomFraccio(a1, d1) + (resta1 ? " menys " : " més ") + Q.nomFraccio(bb, d1));
    const par = [resta1 ? txt("12.1.resta_frase", { a: a1, b: bb, s: r }) : txt("12.1.suma_frase", { a: a1, b: bb, s: r }), txt("12.1.mateix")];
    if (resta1 && b1 > a1) par.push(txt("12.1.no_es_pot"));
    $("#sa-lectura").innerHTML = lectura(par, op(a1, bb, d1, resta1) + " = " + Q.htmlFraccio(r, d1));
    $("#sa-marca").hidden = !(a1 === EX.a && b1 === EX.b && d1 === EX.d && resta1 === EX.resta);
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    CE.pastilles($("#sa-op"), [{ et: txtPla("12.1.suma"), resta: false }, { et: txtPla("12.1.resta"), resta: true }],
                 t => { resta1 = t.resta; pinta1(); }, 0);
    CE.comptador($("#sa-d"), { et: txt("12.1.et_d"), min: 2, max: 12, valor: d1, aoCanviar: v => { d1 = v; pinta1(); } });
    CE.comptador($("#sa-a"), { et: txt("12.1.et_a"), min: 0, max: 12, valor: a1, aoCanviar: v => { a1 = v; pinta1(); } });
    CE.comptador($("#sa-b"), { et: txt("12.1.et_b"), min: 0, max: 12, valor: b1, aoCanviar: v => { b1 = v; pinta1(); } });
    pinta1();
  }

  /* ================================================ 12.2 · Quant és? ====== */
  // [a, b, d, resta?]: les de les activitats 7 a 11 del grup, amb denominadors fins al 12.
  const OPERACIONS = [[3, 2, 8, false], [1, 2, 4, false], [2, 1, 5, false], [3, 5, 7, false], [4, 3, 10, false],
                      [4, 1, 7, true], [5, 2, 6, true], [7, 3, 8, true], [9, 3, 8, true], [9, 4, 12, true]];
  const N2 = 5;
  let t2 = null, c2 = null, i2 = 0, opcions2 = [];
  function opcionsDe([a, b, d, resta]) {
    const r = resta ? a - b : a + b;
    return [["bona", r, d], ["dalt_i_baix", r, resta ? d : 2 * d], ["un_mes", r + 1, d]]
      .filter((o, k, tot) => !(k === 1 && resta)).concat(resta ? [["suma", a + b, d]] : []);
  }
  function pas2(i, e) {
    c2 = OPERACIONS[e.extra.ordre[i]]; i2 = 0;
    const [a, b, d, resta] = c2;
    dibuixa($("#sb-svg"), a, b, d, resta);
    $("#sb-svg").setAttribute("aria-label", Q.nomFraccio(a, d) + (resta ? " menys " : " més ") + Q.nomFraccio(b, d));
    $("#sb-pregunta").innerHTML = op(a, b, d, resta) + " = ?";
    const totes = opcionsDe(c2);
    opcions2 = e.extra.torns[i].map(k => totes[k]);
    const cont = $("#sb-opcions");
    cont.innerHTML = opcions2.map((o, k) => '<button type="button" class="btn opcio-sino opcio-frac" data-k="' + k + '">' +
      Q.htmlFraccio(o[1], o[2]) + "</button>").join("");
    $$(".opcio-frac", cont).forEach(b => { b.onclick = () => tria2(Number(b.dataset.k), b); });
    const avis = $("#sb-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("12.2.comenca");
    $("#sb-seguent").disabled = !t2.resolt();
    $("#sb-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca();
  }
  function marca() { $$(".opcio-frac", $("#sb-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", opcions2[b.dataset.k][0] === "bona"); }); }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const [a, b, d, resta] = c2, r = resta ? a - b : a + b, o = opcions2[k], avis = $("#sb-avis");
    const frase = txt("12.2.encert", { op: op(a, b, d, resta), r: Q.htmlFraccio(r, d) });
    if (o[0] === "bona") { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(o[0] === "dalt_i_baix" ? "12.2.error_den" : "12.2.error"), txt("12.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca(); }
    $("#sb-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 12, sub: 2,
      recorregut: $("#sb-recorregut"), represa: $("#sb-represa"), final: $("#sb-final"), cos: [$("#sb-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => OPERACIONS[i] !== undefined) && Array.isArray(e.extra.torns),
      nom: () => "12.2 · " + txtPla("12.2.nom"),
      pinta: pas2
    });
    $("#sb-seguent").onclick = () => t2.seguent();
    t2.inicia(() => {
      const ordre = CE.barreja(CE.barreja([0, 1, 2, 3, 4]).slice(0, 3).concat(CE.barreja([5, 6, 7, 8, 9]).slice(0, 2)));
      return { total: N2, extra: { ordre, torns: ordre.map(() => CE.barreja([0, 1, 2])) } };
    });
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-sumes");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(12) || 1);
  }
  CE.registra("sumes", inicia);
  CE.registraCataleg("12.2", { nom: txtPla("12.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { sumes: { EX, OPERACIONS } });
})();
