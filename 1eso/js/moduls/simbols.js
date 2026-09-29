/* ============================================================================
   DE LA PARAULA AL SÍMBOL — mòdul «simbols» de la caixa d'eines · tasca 27 · unitat 7
   ----------------------------------------------------------------------------
   «El triple d'un nombre» s'escriu 3 · n: la lletra n és un nombre qualsevol.
   Sempre amb el punt (decisió del docent del 29/9/2026): així no pot passar
   l'error de la Zoe del llibre («si n = 3, 2n = 23»). Activitat 3 de la
   situació «Llenguatge algebraic i patrons» (el llibre, UD8: «De la paraula
   al símbol»). Sense equacions: només traduir i calcular per a un valor.

   27.1 · LA PARAULA I EL SÍMBOL  cinc frases per triar i un comptador de n
                                  (de l'1 al 10). El dibuix de quadrets (n en
                                  blau; el que s'hi afegeix, en taronja; el que
                                  es treu, ratllat), el símbol i el càlcul per
                                  a aquella n. S'obre amb el triple i n = 4.
   27.2 · QUIN ÉS EL SÍMBOL?      tasca tancada de cinc passos: una frase i
                                  tres símbols. Les dolentes són les confusions de
                                  debò: el triple fet suma (n + 3), el més fet
                                  multiplicació (5 · n), i al revés (1 − n).
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, lectura } = CE;
  const Q = CE.q;

  // [clau de la frase, símbol, càlcul(n)]
  const FRASES = [["doble", "2 · n", n => 2 * n], ["triple", "3 · n", n => 3 * n], ["mes5", "n + 5", n => n + 5],
                  ["menys1", "n − 1", n => n - 1], ["seguent", "n + 1", n => n + 1]];
  const calcul = (k, n) => FRASES[k][1].replace("n", String(n)) + " = " + FRASES[k][2](n);

  /** El dibuix: n quadrets (blau). El doble i el triple, en files; el que se suma, en
      taronja; el que es resta, buit i ratllat. */
  function dibuixa(svg, clau, n) {
    svg.textContent = "";
    const m = 26, x0 = 6;
    const files = clau === "doble" ? 2 : clau === "triple" ? 3 : 1;
    const extra = clau === "mes5" ? 5 : clau === "seguent" ? 1 : 0;
    for (let f = 0; f < files; f++) for (let c = 0; c < n; c++)
      Q.quadret(svg, x0 + c * m, 6 + f * m, m, clau === "menys1" && c === n - 1 ? "q falta" : "q");
    for (let c = 0; c < extra; c++) Q.quadret(svg, x0 + (n + c) * m + 8, 6, m, "q b nou");
    if (clau === "menys1") {
      const x = x0 + (n - 1) * m;
      svg.appendChild(CE.el("line", { x1: x + 3, y1: 6 + m - 3, x2: x + m - 3, y2: 9, class: "q-ratlla" }));
    }
    const W = x0 + (n + extra) * m + 20, H = files * m + 12;
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    svg.setAttribute("width", W);
  }

  /* ========================================= 27.1 · La paraula i el símbol ====== */

  const EX271 = { k: 1, n: 4 };
  function pinta1(o) {
    const [clau, simbol] = FRASES[o.k];
    dibuixa($("#sy-svg"), clau, o.n);
    $("#sy-svg").setAttribute("aria-label", txtPla("27.1.aria", { frase: txtPla("27.1.f_" + clau), n: o.n }));
    $("#sy-lectura").innerHTML = lectura([txt("27.1.es", { frase: txt("27.1.f_" + clau), simbol }),
                                          txt("27.1.si", { n: o.n, calcul: calcul(o.k, o.n) })], simbol);
    $("#sy-marca").hidden = !(o.k === EX271.k && o.n === EX271.n);
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    const o = Object.assign({}, EX271);
    CE.pastilles($("#sy-pastilles"), FRASES.map((f, k) => ({ et: txtPla("27.1.f_" + f[0]), k })),
      t => { o.k = t.k; pinta1(o); }, EX271.k);
    CE.comptador($("#sy-n"), { et: "n", sub: txt("27.1.sub_n"), min: 2, max: 10, valor: o.n, aoCanviar: v => { o.n = v; pinta1(o); } });
    pinta1(o);
  }

  /* ============================================= 27.2 · Quin és el símbol? ====== */

  // [clau de la frase, la bona, dues confusions]
  const CASOS = [["doble", "2 · n", "n + 2", "n · n"], ["triple", "3 · n", "n + 3", "n · n"],
                 ["mes5", "n + 5", "5 · n", "n − 5"], ["menys1", "n − 1", "1 − n", "n + 1"],
                 ["seguent", "n + 1", "n − 1", "1 · n"], ["mes3", "n + 3", "3 · n", "n − 3"]];
  const N2 = 5;
  let t2 = null, c2 = null, i2 = 0, opcions2 = [];
  function pas2(i, e) {
    c2 = CASOS[e.extra.ordre[i]]; i2 = 0;
    $("#sz-pregunta").innerHTML = txt("27.1.f_" + c2[0]);
    opcions2 = e.extra.torns[i].map(k => c2[k + 1]);
    const cont = $("#sz-opcions");
    cont.innerHTML = opcions2.map((op, k) => '<button type="button" class="btn opcio-sino opcio-dec" data-k="' + k + '">' +
      op + "</button>").join("");
    $$(".opcio-dec", cont).forEach(bt => { bt.onclick = () => tria2(Number(bt.dataset.k), bt); });
    const avis = $("#sz-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("27.2.comenca");
    $("#sz-seguent").disabled = !t2.resolt();
    $("#sz-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() {
    $$(".opcio-dec", $("#sz-opcions")).forEach(bt => { bt.disabled = true; bt.classList.toggle("bona", opcions2[bt.dataset.k] === c2[1]); });
  }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const avis = $("#sz-avis"), frase = txt("27.1.es", { frase: txt("27.1.f_" + c2[0]), simbol: c2[1] });
    if (opcions2[k] === c2[1]) { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt("27.2.error"), txt("27.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); }
    $("#sz-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 27, sub: 2,
      recorregut: $("#sz-recorregut"), represa: $("#sz-represa"), final: $("#sz-final"), cos: [$("#sz-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => CASOS[i] !== undefined) && Array.isArray(e.extra.torns),
      nom: () => "27.2 · " + txtPla("27.2.nom"),
      pinta: pas2
    });
    $("#sz-seguent").onclick = () => t2.seguent();
    t2.inicia(() => {
      const ordre = CE.barreja(CASOS.map((c, i) => i)).slice(0, N2);
      return { total: N2, extra: { ordre, torns: ordre.map(() => CE.barreja([0, 1, 2])) } };
    });
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-simbols");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(27) || 1);
  }
  CE.registra("simbols", inicia);
  CE.registraCataleg("27.2", { nom: txtPla("27.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { simbols: { FRASES, CASOS } });
})();
