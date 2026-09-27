/* ============================================================================
   LA FRACCIÓ D'UN NOMBRE — mòdul «fraccnombre» de la caixa d'eines · tasca 14 ·
   unitat 4
   ----------------------------------------------------------------------------
   Una fracció d'un nombre és repartir els seus quadrets en grups iguals i
   pintar-ne els que calen: 1/3 de 12 és repartir 12 quadrets en 3 grups de 4,
   i pintar-ne 1 grup. Lliga amb repartir (unitat 2) i amb la fracció d'un
   rectangle (unitat 3). Activitats 2 i 3 de la situació «És gran l'ou del
   kiwi?».
   14.1 · REPARTEIX I PINTA   dos comptadors (el nombre i el denominador) i un
                              tercer amb els grups que es pinten (el numerador).
                              El nombre sempre es reparteix en grups exactes.
                              S'obre amb 1/3 de 12, el nucli de la unitat.
   14.2 · QUANT ÉS?           tasca tancada de cinc passos: es dona la fracció
                              i el nombre, i es tria el resultat entre tres
                              opcions. Les dolentes són les confusions de debò:
                              el nombre de grups en lloc del resultat, i
                              confondre numerador i denominador.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, quants, lectura } = CE;
  const Q = CE.q;
  const qu = n => quants(n, "comu.quadret", "comu.quadrets");

  /** El dibuix: `d` grups de `nombre / d` quadrets, un sota l'altre, amb els
      primers `n` grups pintats. Torna la mida feta servir. */
  function dibuixa(svg, nombre, n, d) {
    svg.textContent = "";
    const grup = nombre / d;
    const X0 = 90, AMP = 460, m = Math.max(9, Math.min(30, (AMP - X0 - 16) / grup, 300 / d));
    const y0 = 10;
    for (let g = 0; g < d; g++) Q.rectangle(svg, X0, y0 + g * m, 1, grup, m, g < n ? "q" : "q b");
    Q.clau(svg, X0 - 12, y0, X0 - 12, y0 + d * m, quants(d, "14.1.grup", "14.1.grups"), "esquerra");
    svg.setAttribute("viewBox", "0 0 " + AMP + " " + Math.round(y0 + d * m + 12));
  }

  function paraules(nombre, n, d) {
    const grup = nombre / d;
    return [
      txt("14.1.reparteixes", { quadrets: qu(nombre), d }),
      txt("14.1.cada_grup", { quadrets: qu(grup) }),
      n === 1 ? txt("14.1.pintes_un") : txt("14.1.pintes", { n }),
      txt("14.1.resultat", { quadrets: qu(n * grup) })
    ];
  }
  const igualtat = (nombre, n, d) => Q.htmlFraccio(n, d) + " " + txtPla("14.1.de") + " " + nombre + " = " + (n * nombre / d);

  /* ======================================== 14.1 · Reparteix i pinta ====== */

  const EX61 = { nombre: 12, n: 1, d: 3 };
  let nb1 = EX61.nombre, n1 = EX61.n, d1 = EX61.d, compt1 = null;

  function pinta1() {
    const svg = $("#fn-svg");
    dibuixa(svg, nb1, n1, d1);
    svg.setAttribute("aria-label", txtPla("14.1.aria", { n: n1, d: d1, nombre: nb1 }));
    $("#fn-lectura").innerHTML = lectura(paraules(nb1, n1, d1), igualtat(nb1, n1, d1));
    $("#fn-marca").hidden = !(nb1 === EX61.nombre && n1 === EX61.n && d1 === EX61.d);
  }

  /** Assegura que `nb1` es pugui repartir en `d1` grups exactes, tocant el
      mínim: si cal, apuja `nb1` al múltiple de `d1` més a prop. `n1` no passa
      mai de `d1 - 1` (fracció pròpia: la unitat és sempre el nombre sencer). */
  function ajusta() {
    const grup = Math.max(1, Math.round(nb1 / d1));
    nb1 = grup * d1;
    if (n1 > d1 - 1) n1 = d1 - 1;
    if (compt1) { compt1.d.posa(d1); compt1.n.activa(false); compt1.n.activa(true); }
  }

  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    const dCompt = CE.comptador($("#fn-d"), { et: txt("14.1.et_d"), min: 2, max: 6, valor: d1,
      aoCanviar: v => { d1 = v; ajusta(); n1 = Math.min(n1, d1 - 1); nCompt.posa(n1); nCompt.activa(true); pinta1(); } });
    const nCompt = CE.comptador($("#fn-n"), { et: txt("14.1.et_n"), min: 1, max: d1 - 1, valor: n1,
      aoCanviar: v => { n1 = v; pinta1(); } });
    const nbCompt = CE.comptador($("#fn-nombre"), { et: txt("14.1.et_nombre"), min: d1, max: 10 * d1, valor: nb1,
      aoCanviar: v => { nb1 = v; ajusta(); pinta1(); } });
    compt1 = { d: dCompt, n: nCompt, nombre: nbCompt };
    pinta1();
  }

  /* ==================================================== 14.2 · Quant és? ====== */

  // [numerador, denominador, nombre, resultat]: tots amb divisió exacta i
  // quocient de la targeta (fins a 10). El primer és el de l'obertura.
  const CASOS = [
    [1, 3, 12, 4], [2, 3, 12, 8], [1, 4, 20, 5], [3, 4, 20, 15], [1, 2, 14, 7],
    [2, 5, 20, 8], [1, 5, 30, 6], [3, 5, 30, 18], [1, 6, 24, 4], [5, 6, 24, 20]
  ];
  const N2 = 5;
  let t2 = null, c2 = null, i2 = 0, opcions2 = [];

  /** Les tres opcions: la bona, el nombre de grups (confondre-la amb el
      resultat) i el resultat fet amb l'altre número del denominador i
      numerador girats. */
  function opcionsDe(n, d, nombre, r) {
    const grup = nombre / d;
    const girada = Math.round((d * nombre) / n);
    return [["bona", r], ["grup", grup], ["girada", girada === r ? r + grup : girada]];
  }
  function pas2(i, e) {
    c2 = CASOS[e.extra.ordre[i]]; i2 = 0;
    const [n, d, nombre, r] = c2;
    $("#fq-pregunta").innerHTML = txt("14.2.pregunta", { f: Q.htmlFraccio(n, d), nombre });
    opcions2 = e.extra.torns[i].map(k => opcionsDe(n, d, nombre, r)[k]);
    const cont = $("#fq-opcions");
    cont.innerHTML = opcions2.map((o, k) => '<button type="button" class="btn opcio-sino opcio-fn" data-k="' + k + '">' +
      o[1] + "</button>").join("");
    $$(".opcio-fn", cont).forEach(b => { b.onclick = () => tria2(Number(b.dataset.k), b); });
    const svg = $("#fq-svg");
    if (t2.resolt()) mostraDibuix2(); else svg.setAttribute("hidden", "");
    const avis = $("#fq-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("14.2.comenca");
    $("#fq-seguent").disabled = !t2.resolt();
    $("#fq-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() { $$(".opcio-fn", $("#fq-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", opcions2[b.dataset.k][0] === "bona"); }); }
  function mostraDibuix2() {
    const [n, d, nombre] = c2, svg = $("#fq-svg");
    dibuixa(svg, nombre, n, d);
    svg.setAttribute("aria-label", txtPla("14.1.aria", { n, d, nombre }));
    svg.removeAttribute("hidden");
  }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const [n, d, nombre, r] = c2, o = opcions2[k], avis = $("#fq-avis");
    const frase = txt("14.2.encert", { f: Q.htmlFraccio(n, d), nombre, r });
    if (o[0] === "bona") { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); mostraDibuix2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(o[0] === "grup" ? "14.2.error_grup" : "14.2.error_girada"), txt("14.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); mostraDibuix2(); }
    $("#fq-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 14, sub: 2,
      recorregut: $("#fq-recorregut"), represa: $("#fq-represa"), final: $("#fq-final"), cos: [$("#fq-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => CASOS[i] !== undefined) && Array.isArray(e.extra.torns),
      nom: () => "14.2 · " + txtPla("14.2.nom"),
      pinta: pas2
    });
    $("#fq-seguent").onclick = () => t2.seguent();
    t2.inicia(() => ({ total: N2, extra: { ordre: CE.barreja(CASOS.map((_, i) => i)).slice(0, N2),
                                           torns: Array.from({ length: N2 }, () => CE.barreja([0, 1, 2])) } }));
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-fraccnombre");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(14) || 1);
  }
  CE.registra("fraccnombre", inicia);
  CE.registraCataleg("14.2", { nom: txtPla("14.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { fraccnombre: { EX61, CASOS } });
})();
