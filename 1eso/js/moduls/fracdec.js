/* ============================================================================
   FRACCIÓ I DECIMAL — mòdul «fracdec» de la caixa d'eines · tasca 21 · unitat 5
   ----------------------------------------------------------------------------
   Una fracció es passa a decimal al quadrat de 100: 1/4 de 100 quadrets són
   25 quadrets (la fracció d'un nombre, unitat 4), i 25 quadrets són 2
   columnes i 5 quadrets: 0,25. És el mateix quadrat dels percentatges (25 %).
   «Un mateix nombre, moltes cares», el fil del llibre. Activitat 4 de la
   situació «Decimals i arrel quadrada».

   Només les fraccions que fan quadrets sencers de 100, amb els denominadors
   de la targeta de les fraccions (2, 4, 5 i 10): són els decimals exactes
   del nivell 1 del criteri 5.1. Els periòdics queden fora (decisió del docent
   del 29/9/2026).

   21.1 · PINTA LA FRACCIÓ     nou fraccions per triar. El quadrat de 100 amb
                               els quadrets pintats columna a columna, quantes
                               columnes i quadrets són, el decimal i el
                               percentatge. S'obre amb 1/4 = 0,25.
   21.2 · DE FRACCIÓ A DECIMAL tasca tancada de cinc passos: una fracció i tres
                               decimals. Les dolentes són les confusions de
                               debò: la regla trencada de la fitxa, posar el de
                               baix després de la coma (1/4 = 0,4), i llegir la
                               barra com una coma (1/4 = 1,4). En contestar,
                               surt el quadrat pintat.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, quants, lectura } = CE;
  const Q = CE.q;
  const dec = Q.dec;

  const FRACCIONS = [[1, 2], [1, 4], [3, 4], [1, 5], [2, 5], [3, 5], [1, 10], [3, 10], [7, 10]];
  // A la tasca tancada, sense el 10: amb 1/10, «el de baix després de la coma» (0,10)
  // és el mateix nombre que la resposta bona.
  const CASOS2 = [[1, 2], [1, 4], [3, 4], [1, 5], [2, 5], [3, 5], [4, 5]];
  const quadretsDe = ([n, d]) => (100 / d) * n;

  function lectures(f) {
    const q = quadretsDe(f), col = Math.floor(q / 10), qs = q % 10;
    const fh = Q.htmlFraccio(f[0], f[1]);
    const par = [txt("21.1.quadrets", { f: fh, quadrets: quants(q, "comu.quadret", "comu.quadrets") })];
    const cols = quants(col, "comu.columna", "comu.columnes"), d = quants(col, "comu.decima", "comu.decimes");
    par.push(qs ? txt("21.1.columnes", { col: cols, qs: quants(qs, "comu.quadret", "comu.quadrets"), d,
                                         c: quants(qs, "comu.centesima", "comu.centesimes") })
                : txt("21.1.columnes_sol", { col: cols, d }));
    par.push(txt("21.1.percent", { p: q }));
    return lectura(par, fh + " = " + dec(q));
  }
  function dibuixa(svg, f) {
    Q.quadrat100(svg, quadretsDe(f));
    svg.setAttribute("aria-label", txtPla("21.1.aria", { n: quadretsDe(f) }));
  }

  /* ============================================ 21.1 · Pinta la fracció ====== */

  const EX211 = 1;                                       // 1/4
  let k1 = EX211;
  function pinta1() {
    dibuixa($("#fc-svg"), FRACCIONS[k1]);
    $("#fc-lectura").innerHTML = lectures(FRACCIONS[k1]);
    $("#fc-marca").hidden = k1 !== EX211;
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    CE.pastilles($("#fc-pastilles"), FRACCIONS.map(([n, d], k) => ({ et: n + "/" + d, aria: Q.nomFraccio(n, d), k })),
      t => { k1 = t.k; pinta1(); }, EX211);
    pinta1();
  }

  /* ========================================= 21.2 · De fracció a decimal ====== */

  const N2 = 5;
  let t2 = null, f2 = null, i2 = 0, opcions2 = [];
  /** La bona; el de baix després de la coma (1/4 → 0,4); i la barra com una coma (1/4 → 1,4). */
  function opcionsDe([n, d]) {
    return [["bona", dec(quadretsDe([n, d]))], ["baix", "0," + d], ["barra", n + "," + d]];
  }
  function pas2(i, e) {
    f2 = CASOS2[e.extra.ordre[i]]; i2 = 0;
    $("#fd-pregunta").innerHTML = txt("21.2.pregunta", { f: Q.htmlFraccio(f2[0], f2[1]) });
    opcions2 = e.extra.torns[i].map(k => opcionsDe(f2)[k]);
    const cont = $("#fd-opcions");
    cont.innerHTML = opcions2.map((op, k) => '<button type="button" class="btn opcio-sino opcio-dec" data-k="' + k + '">' +
      op[1] + "</button>").join("");
    $$(".opcio-dec", cont).forEach(b => { b.onclick = () => tria2(Number(b.dataset.k), b); });
    dibuixa($("#fd-svg"), f2);
    $("#fd-svg").toggleAttribute("hidden", !t2.resolt());
    const avis = $("#fd-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("21.2.comenca");
    $("#fd-seguent").disabled = !t2.resolt();
    $("#fd-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() {
    $$(".opcio-dec", $("#fd-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", opcions2[b.dataset.k][0] === "bona"); });
    // El quadrat pintat, només quan ja s'ha contestat: si no, la resposta es veuria.
    // Un <svg> no té .hidden: cal l'atribut (docs/ARQUITECTURA.md, apartat 4).
    $("#fd-svg").toggleAttribute("hidden", false);
  }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const op = opcions2[k], avis = $("#fd-avis"), fh = Q.htmlFraccio(f2[0], f2[1]), q = quadretsDe(f2);
    const frase = txt("21.2.encert", { f: fh, q, r: dec(q) });
    if (op[0] === "bona") { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(op[0] === "baix" ? "21.2.error_baix" : "21.2.error_barra"), txt("21.2.pista", { f: fh }));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); }
    $("#fd-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 21, sub: 2,
      recorregut: $("#fd-recorregut"), represa: $("#fd-represa"), final: $("#fd-final"), cos: [$("#fd-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => CASOS2[i] !== undefined) && Array.isArray(e.extra.torns),
      nom: () => "21.2 · " + txtPla("21.2.nom"),
      pinta: pas2
    });
    $("#fd-seguent").onclick = () => t2.seguent();
    t2.inicia(() => {
      const ordre = CE.barreja(CASOS2.map((c, i) => i)).slice(0, N2);
      return { total: N2, extra: { ordre, torns: ordre.map(() => CE.barreja([0, 1, 2])) } };
    });
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-fracdec");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(21) || 1);
  }
  CE.registra("fracdec", inicia);
  CE.registraCataleg("21.2", { nom: txtPla("21.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { fracdec: { FRACCIONS, CASOS2, opcionsDe, quadretsDe } });
})();
