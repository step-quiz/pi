/* ============================================================================
   GRÀFICS DE BARRES — mòdul «grafics» de la caixa d'eines · tasca 28 · unitat 7
   ----------------------------------------------------------------------------
   Un gràfic de barres fet de quadrets: cada quadret és 1, i la barra és una
   columna de quadrets. Només barres i taules (decisió del docent del
   29/9/2026). Activitat 5 de la situació «Llenguatge algebraic i patrons» (el
   llibre, UD8: «Interpretar gràfics i taules»). L'enquesta de com venen a
   l'institut (12, 8, 6 i 4) és la del llibre.

   28.1 · LLEGEIX EL GRÀFIC  tres enquestes per triar. El gràfic, la barra més
                             alta i la més baixa, i el total.
   28.2 · QUANTS N'HI HA?    tasca tancada de cinc passos: un gràfic, una
                             barra marcada i tres nombres. Les dolentes són
                             llegir la ratlla de sobre o la de sota.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, lectura } = CE;
  const Q = CE.q;

  // [clau del títol, [[clau de l'etiqueta, valor]]]
  const ENQUESTES = [["institut", [["peu", 12], ["bus", 8], ["bici", 6], ["cotxe", 4]]],
                     ["esport", [["futbol", 9], ["basquet", 7], ["natacio", 5], ["dansa", 6]]],
                     ["fruita", [["poma", 7], ["platan", 10], ["taronja", 4], ["maduixa", 8]]]];
  const dadesDe = e => e[1].map(([k, v]) => [txtPla("28.1.e_" + k), v]);

  /* ============================================== 28.1 · Llegeix el gràfic ====== */

  const EX281 = 0;
  let k1 = EX281;
  function pinta1() {
    const e = ENQUESTES[k1], d = dadesDe(e), vals = d.map(x => x[1]);
    Q.barres($("#gr-svg"), d);
    $("#gr-svg").setAttribute("aria-label", txtPla("28.1.aria", { titol: txtPla("28.1.t_" + e[0]),
      dades: d.map(([et, v]) => et + " " + v).join(", ") }));
    const mx = d[vals.indexOf(Math.max(...vals))], mn = d[vals.indexOf(Math.min(...vals))];
    $("#gr-lectura").innerHTML = lectura([txt("28.1.titol_enquesta", { titol: txt("28.1.t_" + e[0]) }),
      txt("28.1.alta", { et: mx[0], v: mx[1] }), txt("28.1.baixa", { et: mn[0], v: mn[1] }),
      txt("28.1.total", { calcul: vals.join(" + ") + " = " + vals.reduce((a, b) => a + b, 0) })]);
    $("#gr-marca").hidden = k1 !== EX281;
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    CE.pastilles($("#gr-pastilles"), ENQUESTES.map((e, k) => ({ et: txtPla("28.1.t_" + e[0]), k })), t => { k1 = t.k; pinta1(); }, EX281);
    pinta1();
  }

  /* ================================================= 28.2 · Quantes persones? ====== */

  const N2 = 5;
  let t2 = null, cas = null, i2 = 0, opcions2 = [];
  const CASOS = [];
  ENQUESTES.forEach((e, ie) => e[1].forEach((x, ib) => CASOS.push([ie, ib])));
  function pas2(i, e) {
    cas = CASOS[e.extra.ordre[i]]; i2 = 0;
    const enq = ENQUESTES[cas[0]], d = dadesDe(enq), [et, v] = d[cas[1]];
    Q.barres($("#gs-svg"), d, { destaca: cas[1] });
    $("#gs-svg").setAttribute("aria-label", txtPla("28.1.aria", { titol: txtPla("28.1.t_" + enq[0]),
      dades: d.map(([a, b]) => a + " " + b).join(", ") }));
    $("#gs-pregunta").textContent = txtPla("28.2.pregunta", { et });
    opcions2 = e.extra.torns[i].map(k => [["bona", v], ["dalt", v + 1], ["baix", v - 1]][k]);
    const cont = $("#gs-opcions");
    cont.innerHTML = opcions2.map((op, k) => '<button type="button" class="btn opcio-sino opcio-dec" data-k="' + k + '">' +
      op[1] + "</button>").join("");
    $$(".opcio-dec", cont).forEach(bt => { bt.onclick = () => tria2(Number(bt.dataset.k), bt); });
    const avis = $("#gs-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("28.2.comenca");
    $("#gs-seguent").disabled = !t2.resolt();
    $("#gs-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() {
    $$(".opcio-dec", $("#gs-opcions")).forEach(bt => { bt.disabled = true; bt.classList.toggle("bona", opcions2[bt.dataset.k][0] === "bona"); });
  }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const op = opcions2[k], avis = $("#gs-avis"), [et, v] = dadesDe(ENQUESTES[cas[0]])[cas[1]];
    const frase = txt("28.2.encert", { et, v });
    if (op[0] === "bona") { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(op[0] === "dalt" ? "28.2.error_dalt" : "28.2.error_baix"), txt("28.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); }
    $("#gs-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 28, sub: 2,
      recorregut: $("#gs-recorregut"), represa: $("#gs-represa"), final: $("#gs-final"), cos: [$("#gs-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => CASOS[i] !== undefined) && Array.isArray(e.extra.torns),
      nom: () => "28.2 · " + txtPla("28.2.nom"),
      pinta: pas2
    });
    $("#gs-seguent").onclick = () => t2.seguent();
    t2.inicia(() => {
      const ordre = CE.barreja(CASOS.map((c, i) => i)).slice(0, N2);
      return { total: N2, extra: { ordre, torns: ordre.map(() => CE.barreja([0, 1, 2])) } };
    });
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-grafics");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(28) || 1);
  }
  CE.registra("grafics", inicia);
  CE.registraCataleg("28.2", { nom: txtPla("28.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { grafics: { ENQUESTES, CASOS } });
})();
