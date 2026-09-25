/* ============================================================================
   REPARTIR — mòdul «repartir» de la caixa d'eines · tasca 6 · unitat 2
   ----------------------------------------------------------------------------
   La divisió entera de l'activitat 2_2 del grup, amb el mateix dibuix de tot el
   curs. Les caixes plenes de boles del GeoGebra del grup són files plenes de
   quadrets: repartir 37 en caixes de 7 és fer files de 7 amb 37 quadrets. Si
   les files s'omplen, la divisió és exacta; si no, sobren quadrets, i els que
   sobren són el residu. La igualtat és la del grup: 37 = 5 · 7 + 2.

   6.1 · REPARTEIX EN FILES
     Dos comptadors: quants quadrets i quants a cada fila. Surten les files
     plenes, la fila a mitges amb els que sobren (i els llocs buits que li
     falten, amb traç discontinu) i, sota, les paraules i la igualtat. S'obre
     amb 37 en files de 7, l'exercici 5 del grup.

   6.2 · SOBREN QUADRETS?
     Una tasca tancada de cinc passos: tres en sobren i dos són exactes.
     Resposta Sí o No; la pista és buscar el nombre a la taula de la targeta.
     Després de contestar, surt el dibuix: la regla trencada («37 entre 7 són
     5», sense el residu) es desmunta mirant la fila a mitges.
   ========================================================================== */

(function () {
  "use strict";
  const { $, txt, txtPla, omplirTextos, retroaccio, quants, delNombre, lectura } = CE;
  const Q = CE.q;
  const qu = n => quants(n, "comu.quadret", "comu.quadrets");
  const files = n => quants(n, "6.1.fila_plena", "6.1.files_plenes");

  /** El dibuix: q files plenes de k quadrets i una fila a mitges amb r quadrets,
      amb els llocs que li falten buits. Torna la mida que ha fet servir. */
  function dibuixa(svg, n, k) {
    svg.textContent = "";
    const q = Math.floor(n / k), r = n % k, fs = q + (r ? 1 : 0);
    // A l'esquerra, lloc per a «12 files plenes»; a la dreta, per a «en sobren 9».
    const X0 = 158, AMP = 500, m = Math.max(9, Math.min(30, (AMP - X0 - 128) / k, 380 / Math.max(fs, 1)));
    const y0 = 34;
    Q.rectangle(svg, X0, y0, q, k, m, "q");
    const yr = y0 + q * m;
    for (let c = 0; c < k && r; c++) Q.quadret(svg, X0 + c * m, yr, m, c < r ? "q b" : "q falta");
    if (q) Q.clau(svg, X0 - 12, y0, X0 - 12, y0 + q * m, files(q), "esquerra");
    Q.clau(svg, X0, y0 - 10, X0 + k * m, y0 - 10, txtPla("6.1.a_cada_fila", { k }), "dalt");
    if (r) Q.text(svg, X0 + k * m + 12, yr + m / 2 + 1, txtPla(r === 1 ? "6.1.sobra_dibuix" : "6.1.sobren_dibuix", { r }),
                  "q-text fort", 16, "start");
    svg.setAttribute("viewBox", "0 0 " + AMP + " " + Math.round(y0 + fs * m + 16));
  }

  /** La igualtat del grup: «37 = 5 · 7 + 2», o «35 = 5 · 7» si és exacta. */
  const igualtat = (n, k) => {
    const q = Math.floor(n / k), r = n % k;
    return r ? n + " = " + q + " · " + k + " + " + r : n + " = " + q + " · " + k;
  };

  function paraules(n, k) {
    const q = Math.floor(n / k), r = n % k;
    const p = [txt("6.1.reparteixes", { quadrets: qu(n), k })];
    p.push(q ? txt("6.1.fas", { files: files(q) }) : txt("6.1.cap_fila"));
    p.push(!r ? txt("6.1.exacta") : txt(r === 1 ? "6.1.sobra_1" : "6.1.sobren", { r }));
    if (r) p.push(txt("6.1.residu"));
    return p;
  }

  /* ========================================= 6.1 · Reparteix en files ====== */

  const EX61 = { n: 37, k: 7 };
  let n61 = EX61.n, k61 = EX61.k;

  function pinta61() {
    const svg = $("#r6-svg");
    dibuixa(svg, n61, k61);
    svg.setAttribute("aria-label", paraules(n61, k61).map(t => t.replace(/<[^>]+>/g, "")).join(" "));
    $("#r6-lectura").innerHTML = lectura(paraules(n61, k61), igualtat(n61, k61));
    $("#r6-marca").hidden = !(n61 === EX61.n && k61 === EX61.k);
  }

  let fet61 = false;
  function inicia61() {
    if (fet61) return;
    fet61 = true;
    CE.comptador($("#r6-n"), { et: txt("6.1.et_n"), min: 1, max: 60, valor: n61, aoCanviar: v => { n61 = v; pinta61(); } });
    CE.comptador($("#r6-k"), { et: txt("6.1.et_k"), min: 2, max: 10, valor: k61, aoCanviar: v => { k61 = v; pinta61(); } });
    pinta61();
  }

  /* ========================================== 6.2 · Sobren quadrets? ====== */

  // [quadrets, a cada fila]: els de l'activitat i l'examen del grup, i tots dins de la targeta
  const REPARTIMENTS = [[30, 9], [45, 6], [10, 3], [20, 6], [23, 9], [41, 6], [27, 4], [50, 7],
                        [20, 5], [20, 4], [56, 7], [40, 5], [35, 5], [48, 8]];
  const N62 = 5;
  let t62 = null, c62 = null, i62 = 0, triat62 = null;

  function pas62(i, e) {
    c62 = REPARTIMENTS[e.extra.ordre[i]];
    i62 = 0; triat62 = null;
    $("#s6-pregunta").textContent = txtPla("6.2.pregunta", { n: c62[0], k: c62[1] });
    CE.botonsSiNo($("#s6-opcions"), tria62);
    const svg = $("#s6-svg");
    if (t62.resolt()) mostraDibuix62(); else svg.setAttribute("hidden", "");
    const avis = $("#s6-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t62.resolt() ? txt("comu.ja_fet") : txt("6.2.comenca");
    const seg = $("#s6-seguent");
    seg.disabled = !t62.resolt();
    seg.innerHTML = txt(t62.esUltim() ? "comu.acaba" : "comu.seguent");
    CE.pintaSiNo($("#s6-opcions"), null, c62[0] % c62[1] !== 0, t62.resolt());
  }

  function mostraDibuix62() {
    const svg = $("#s6-svg");
    dibuixa(svg, c62[0], c62[1]);
    svg.setAttribute("aria-label", paraules(c62[0], c62[1]).map(t => t.replace(/<[^>]+>/g, "")).join(" "));
    svg.removeAttribute("hidden");
  }

  function explica62() {
    const [n, k] = c62, r = n % k;
    return igualtat(n, k) + ". " + (!r ? txt("6.1.exacta") : txt(r === 1 ? "6.1.sobra_1" : "6.1.sobren", { r }));
  }

  function tria62(si) {
    const e = t62.estat();
    if (!e || e.acabada || t62.resolt()) return;
    const [n, k] = c62, bo = n % k !== 0, avis = $("#s6-avis");
    triat62 = si;
    if (si === bo) {
      t62.anota(i62 === 0 ? "be" : "pista");
      retroaccio(avis, "encert", explica62());
      mostraDibuix62();
    } else if (i62 === 0) {
      i62 = 1;
      retroaccio(avis, "error", txt(si ? "6.2.has_dit_si" : "6.2.has_dit_no"), txt("6.2.pista", { n, de: delNombre(k) }));
    } else {
      t62.anota("mostrat");
      retroaccio(avis, "mostra", explica62());
      mostraDibuix62();
    }
    CE.pintaSiNo($("#s6-opcions"), triat62, bo, t62.resolt());
    $("#s6-seguent").disabled = !t62.resolt();
  }

  /** Cinc passos: tres en sobren i dos són exactes, barrejats. */
  function nouOrdre62() {
    const idx = REPARTIMENTS.map((_, i) => i);
    const sobren = CE.barreja(idx.filter(i => REPARTIMENTS[i][0] % REPARTIMENTS[i][1] !== 0)).slice(0, 3);
    const exactes = CE.barreja(idx.filter(i => REPARTIMENTS[i][0] % REPARTIMENTS[i][1] === 0)).slice(0, 2);
    return CE.barreja(sobren.concat(exactes));
  }

  let fet62 = false;
  function inicia62() {
    if (fet62) return;
    fet62 = true;
    t62 = CE.tasca({
      tasca: 6, sub: 2,
      recorregut: $("#s6-recorregut"), represa: $("#s6-represa"), final: $("#s6-final"), cos: [$("#s6-cos")],
      desa: true,
      valida: e => e.total === N62 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N62 &&
                   e.extra.ordre.every(i => REPARTIMENTS[i] !== undefined),
      nom: () => "6.2 · " + txtPla("6.2.nom"),
      pinta: pas62
    });
    $("#s6-seguent").onclick = () => t62.seguent();
    t62.inicia(() => ({ total: N62, extra: { ordre: nouOrdre62() } }));
  }

  /* ==================================================== arrencada ====== */

  const ARRENCA = { 1: inicia61, 2: inicia62 };
  let subs = null, subActual = null;

  function inicia() {
    const arrel = $("#mod-repartir");
    if (!subs) {
      omplirTextos(arrel);
      subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); });
    }
    subs.mostra(subActual || CE.subDemanada(6) || 1);
  }

  CE.registra("repartir", inicia);
  CE.registraCataleg("6.2", { nom: txtPla("6.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")],
    resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { repartir: { EX61, REPARTIMENTS, igualtat } });
})();
