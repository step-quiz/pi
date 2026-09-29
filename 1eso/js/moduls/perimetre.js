/* ============================================================================
   PERÍMETRE I ÀREA — mòdul «perimetre» de la caixa d'eines · tasca 25 · unitat 6
   ----------------------------------------------------------------------------
   El perímetre és comptar els costats de quadret de la vora; l'àrea (unitat 3,
   tasca 13) és comptar els quadrets de dins. Al rectangle de 3 files de 4
   quadrets, la vora fa 4 + 3 + 4 + 3 = 14 i a dins hi ha 3 · 4 = 12 quadrets.
   Activitat «Perímetres» de la situació «Sentit espacial» (el llibre: UD7,
   activitat 5).

   Files + columnes fins a 10 (a la 25.1, fins a 4 files i 6 columnes): el
   perímetre, que és el doble de files + columnes, és a la targeta (10 · 2).

   25.1 · PERÍMETRE I ÀREA       dos comptadors (files i columnes), el rectangle
                                 amb la vora gruixuda i els costats numerats
                                 per fora, el perímetre i l'àrea. S'obre amb 3
                                 per 4.
   25.2 · QUIN ÉS EL PERÍMETRE?  tasca tancada de cinc passos: un rectangle i
                                 tres respostes. Les dolentes són les
                                 confusions de debò: donar l'àrea (la regla
                                 trencada de la fitxa 4) i sumar només dos
                                 costats (files + columnes). Cap cas no té el
                                 perímetre igual que l'àrea.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, lectura } = CE;
  const Q = CE.q;
  const vora = (f, c) => c + " + " + f + " + " + c + " + " + f + " = " + 2 * (f + c);
  const dins = (f, c) => f + " · " + c + " = " + f * c;

  function dibuixa(svg, f, c) {
    Q.vora(svg, f, c);
    svg.setAttribute("aria-label", txtPla("25.1.aria", { f, c }));
  }

  /* ========================================== 25.1 · Perímetre i àrea ====== */

  const EX251 = { f: 3, c: 4 };
  function pinta1(o) {
    dibuixa($("#pe-svg"), o.f, o.c);
    $("#pe-lectura").innerHTML = lectura([txt("25.1.vora", { calcul: vora(o.f, o.c) }), txt("25.1.perimetre", { p: 2 * (o.f + o.c) })]) +
                                 lectura([txt("25.1.dins", { calcul: dins(o.f, o.c) }), txt("25.1.area", { a: o.f * o.c })]);
    $("#pe-marca").hidden = !(o.f === EX251.f && o.c === EX251.c);
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    const o = Object.assign({}, EX251);
    // Fins a 4 files i 6 columnes: files + columnes no passa de 10.
    CE.comptador($("#pe-f"), { et: txt("25.1.et_f"), min: 1, max: 4, valor: o.f, aoCanviar: v => { o.f = v; pinta1(o); } });
    CE.comptador($("#pe-c"), { et: txt("25.1.et_c"), min: 1, max: 6, valor: o.c, aoCanviar: v => { o.c = v; pinta1(o); } });
    pinta1(o);
  }

  /* ====================================== 25.2 · Quin és el perímetre? ====== */

  const CASOS = [[3, 4], [2, 5], [3, 3], [4, 5], [2, 6], [1, 4], [3, 5], [2, 7]];
  const N2 = 5;
  let t2 = null, cas = null, i2 = 0, opcions2 = [];
  /** La bona; l'àrea; i només dos costats (files + columnes). */
  const opcionsDe = ([f, c]) => [["bona", 2 * (f + c)], ["area", f * c], ["meitat", f + c]];

  function pas2(i, e) {
    cas = CASOS[e.extra.ordre[i]]; i2 = 0;
    dibuixa($("#pf-svg"), cas[0], cas[1]);
    opcions2 = e.extra.torns[i].map(k => opcionsDe(cas)[k]);
    const cont = $("#pf-opcions");
    cont.innerHTML = opcions2.map((op, k) => '<button type="button" class="btn opcio-sino opcio-dec" data-k="' + k + '">' +
      op[1] + "</button>").join("");
    $$(".opcio-dec", cont).forEach(b => { b.onclick = () => tria2(Number(b.dataset.k), b); });
    const avis = $("#pf-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("25.2.comenca");
    $("#pf-seguent").disabled = !t2.resolt();
    $("#pf-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() {
    $$(".opcio-dec", $("#pf-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", opcions2[b.dataset.k][0] === "bona"); });
  }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const op = opcions2[k], avis = $("#pf-avis"), [f, c] = cas;
    const frase = txt("25.2.encert", { calcul: vora(f, c), p: 2 * (f + c) });
    if (op[0] === "bona") { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(op[0] === "area" ? "25.2.error_area" : "25.2.error_meitat"), txt("25.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); }
    $("#pf-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 25, sub: 2,
      recorregut: $("#pf-recorregut"), represa: $("#pf-represa"), final: $("#pf-final"), cos: [$("#pf-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => CASOS[i] !== undefined) && Array.isArray(e.extra.torns),
      nom: () => "25.2 · " + txtPla("25.2.nom"),
      pinta: pas2
    });
    $("#pf-seguent").onclick = () => t2.seguent();
    t2.inicia(() => {
      const ordre = CE.barreja(CASOS.map((c, i) => i)).slice(0, N2);
      return { total: N2, extra: { ordre, torns: ordre.map(() => CE.barreja([0, 1, 2])) } };
    });
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-perimetre");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(25) || 1);
  }
  CE.registra("perimetre", inicia);
  CE.registraCataleg("25.2", { nom: txtPla("25.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { perimetre: { EX251, CASOS, opcionsDe } });
})();
