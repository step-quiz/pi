/* ============================================================================
   MULTIPLICAR FRACCIONS — mòdul «multfrac» de la caixa d'eines · tasca 15 ·
   unitat 4
   ----------------------------------------------------------------------------
   Multiplicar dues fraccions és fer un tros de tros: el rectangle es parteix
   en columnes per a la primera fracció i en files per a la segona, i el
   resultat és el tros que és a la vegada de les dues (js/quadricula.js,
   `graella2D`). Lliga amb l'àrea (unitat 3) i amb els rectangles (unitat 1).
   Activitats 4 i 5 de la situació «És gran l'ou del kiwi?». Només amb
   numerador 1 a cada fracció, i el resultat sempre amb denominador fins a 12
   (docs/MAPA-ADAPTACIO.md, unitat 3): així el tros de tros no passa mai de la
   quadrícula que ja coneix l'alumnat.
   15.1 · EL TROS DE TROS   dos comptadors, un per cada denominador (2 a 6, i
                            mai més de 12 entre els dos). El dibuix i el nom
                            del resultat. S'obre amb 1/2 de 1/4, com l'exemple
                            de la fitxa.
   15.2 · QUIN TROS ÉS?     tasca tancada de cinc passos: es donen les dues
                            fraccions i es tria el resultat entre tres. Les
                            dolentes són les confusions de debò: sumar els
                            denominadors en lloc de multiplicar-los, i confondre
                            el resultat amb un dels denominadors.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, lectura } = CE;
  const Q = CE.q;

  function dibuixa(svg, d1, d2) {
    svg.textContent = "";
    Q.graella2D(svg, d1, 1, d2, 1);
    svg.setAttribute("aria-label", txtPla("15.1.aria", { d1, d2, dr: d1 * d2 }));
  }

  function paraules(d1, d2) {
    const dr = d1 * d2;
    return [
      txt("15.1.parteixes_amples", { d1 }),
      txt("15.1.parteixes_alts", { d2 }),
      txt("15.1.trossos", { dr })
    ];
  }
  const igualtat = (d1, d2) => "1/" + d1 + " · 1/" + d2 + " = 1/" + (d1 * d2);

  /* ========================================== 15.1 · El tros de tros ====== */

  // Els vuit parells amb d1*d2 <= 12: mai passa de la quadrícula coneguda.
  const PARELLS = [[2, 2], [2, 3], [3, 2], [2, 4], [4, 2], [3, 3], [2, 5], [5, 2], [3, 4], [4, 3], [2, 6], [6, 2]];
  const EX151 = { d1: 2, d2: 4 };
  let d1_1 = EX151.d1, d2_1 = EX151.d2;

  function pinta1() {
    dibuixa($("#mf-svg"), d1_1, d2_1);
    $("#mf-lectura").innerHTML = lectura(paraules(d1_1, d2_1), igualtat(d1_1, d2_1));
    $("#mf-marca").hidden = !(d1_1 === EX151.d1 && d2_1 === EX151.d2);
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    CE.pastilles($("#mf-parells"), PARELLS.map((p, k) => ({ et: "1/" + p[0] + "  ·  1/" + p[1], k })),
      t => { [d1_1, d2_1] = PARELLS[t.k]; pinta1(); },
      PARELLS.findIndex(p => p[0] === EX151.d1 && p[1] === EX151.d2));
    pinta1();
  }

  /* ============================================ 15.2 · Quin tros és? ====== */

  // [d1, d2, resultat]: tots dins de PARELLS, amb el resultat exacte.
  const CASOS = PARELLS.map(([d1, d2]) => [d1, d2, d1 * d2]);
  const N2 = 5;
  let t2 = null, c2 = null, i2 = 0, opcions2 = [];

  /** Les tres opcions: la bona, sumar els denominadors, i un dels denominadors
      sols (confondre'l amb el resultat). */
  function opcionsDe(d1, d2, dr) {
    const suma = d1 + d2;
    return [["bona", dr], ["suma", suma === dr ? dr + 1 : suma], ["un_dels", d1 === dr ? d2 : d1]];
  }
  function pas2(i, e) {
    c2 = CASOS[e.extra.ordre[i]]; i2 = 0;
    const [d1, d2, dr] = c2;
    $("#mg-pregunta").textContent = txtPla("15.2.pregunta", { d1, d2 });
    opcions2 = e.extra.torns[i].map(k => opcionsDe(d1, d2, dr)[k]);
    const cont = $("#mg-opcions");
    cont.innerHTML = opcions2.map((o, k) => '<button type="button" class="btn opcio-sino opcio-tf" data-k="' + k + '">' +
      "1/" + o[1] + "</button>").join("");
    $$(".opcio-tf", cont).forEach(b => { b.onclick = () => tria2(Number(b.dataset.k), b); });
    const svg = $("#mg-svg");
    if (t2.resolt()) mostraDibuix2(); else svg.setAttribute("hidden", "");
    const avis = $("#mg-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("15.2.comenca");
    $("#mg-seguent").disabled = !t2.resolt();
    $("#mg-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() { $$(".opcio-tf", $("#mg-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", opcions2[b.dataset.k][0] === "bona"); }); }
  function mostraDibuix2() {
    const [d1, d2] = c2, svg = $("#mg-svg");
    dibuixa(svg, d1, d2);
    svg.removeAttribute("hidden");
  }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const [d1, d2, dr] = c2, o = opcions2[k], avis = $("#mg-avis");
    const frase = txt("15.2.encert", { d1, d2, dr });
    if (o[0] === "bona") { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); mostraDibuix2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(o[0] === "suma" ? "15.2.error_suma" : "15.2.error_un_dels"), txt("15.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); mostraDibuix2(); }
    $("#mg-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 15, sub: 2,
      recorregut: $("#mg-recorregut"), represa: $("#mg-represa"), final: $("#mg-final"), cos: [$("#mg-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => CASOS[i] !== undefined) && Array.isArray(e.extra.torns),
      nom: () => "15.2 · " + txtPla("15.2.nom"),
      pinta: pas2
    });
    $("#mg-seguent").onclick = () => t2.seguent();
    t2.inicia(() => ({ total: N2, extra: { ordre: CE.barreja(CASOS.map((_, i) => i)).slice(0, N2),
                                           torns: Array.from({ length: N2 }, () => CE.barreja([0, 1, 2])) } }));
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-multfrac");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(15) || 1);
  }
  CE.registra("multfrac", inicia);
  CE.registraCataleg("15.2", { nom: txtPla("15.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { multfrac: { PARELLS, CASOS } });
})();
