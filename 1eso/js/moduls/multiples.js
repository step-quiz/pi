/* ============================================================================
   MÚLTIPLES — mòdul «multiples» de la caixa d'eines · tasca 5 · unitat 2
   ----------------------------------------------------------------------------
   Els múltiples d'un nombre són la seva taula de multiplicar: els de la targeta,
   i els que continuen. És l'activitat 2_1 del grup, amb la seva graella de 100,
   i els criteris de divisibilitat de la 2_3, sense calculadora (regla C).

   5.1 · LA GRAELLA DE 100
     Es tria un nombre del 2 al 10 i es pinten els seus múltiples a la graella,
     com a l'activitat del grup. Se'n veu la forma: els del 2, el 5 i el 10 fan
     columnes. Amb el 3 surt la regla trencada de la unitat: no tots acaben en
     3 (el 12 i el 21 també hi són). S'obre amb el 2.

   5.2 · ÉS MÚLTIPLE?
     Una tasca tancada de cinc passos: «24 és múltiple de 3?», Sí o No. Es
     comprova a la targeta: tots els casos hi són, a la taula o entre dues files.

   5.3 · ELS TRUCS
     Un nombre fins al 999, fet amb els comptadors de centenes, desenes i
     unitats, i els quatre trucs: el 2, el 5 i el 10 per l'última xifra, i el 3
     sumant les xifres. La suma sempre dona de l'1 al 27, i es busca a la taula
     del 3 de la targeta, que arriba fins al 30 (decisió del docent: cap suma
     que s'hagi de tornar a sumar). S'obre amb el 126.

   5.4 · MÚLTIPLE DE 3?
     Una tasca tancada de cinc passos: «123 és múltiple de 3?», Sí o No. La
     pista diu com: suma les xifres i busca el resultat a la taula del 3.
   ========================================================================== */

(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, delNombre, elNombre, lectura } = CE;
  const majuscula = t => t.charAt(0).toUpperCase() + t.slice(1);
  const Q = CE.q;

  const NOMBRES = Array.from({ length: 9 }, (_, i) => ({ et: String(i + 2), n: i + 2 }));

  /** Els botons Sí i No d'una tasca tancada. `aoTriar(sí)` rep true o false. */
  function botonsSiNo(cont, aoTriar) {
    cont.innerHTML =
      '<button type="button" class="btn opcio-sino" data-v="si">' + txt("comu.si") + "</button>" +
      '<button type="button" class="btn opcio-sino" data-v="no">' + txt("comu.no") + "</button>";
    $$(".opcio-sino", cont).forEach(b => { b.onclick = () => aoTriar(b.dataset.v === "si", b); });
  }
  /** Marca el botó triat: el bo en verd, el dolent en taronja i desactivat. */
  function pintaSiNo(cont, triat, bo, resolt) {
    $$(".opcio-sino", cont).forEach(b => {
      const v = b.dataset.v === "si";
      b.classList.toggle("bona", resolt && v === bo);
      b.classList.toggle("mal", triat !== null && v === triat && v !== bo);
      b.disabled = resolt || (triat !== null && v === triat && v !== bo);
    });
  }
  CE.botonsSiNo = botonsSiNo;
  CE.pintaSiNo = pintaSiNo;

  /* ========================================= 5.1 · La graella de 100 ====== */

  const EX51 = 2;
  let k51 = EX51;

  function pinta51() {
    const k = k51, svg = $("#m1-svg");
    Q.graella100(svg, n => (n % k === 0 ? "marca" : null));
    const n100 = Math.floor(100 / k);
    const llista = [1, 2, 3, 4, 5].map(i => i * k).join(", ") + "…";
    const paraules = [txt("5.1.taula", { de: delNombre(k), llista }), txt("5.1.quants", { n: n100 })];
    const truc = { 2: "5.1.acaben_2", 5: "5.1.acaben_5", 10: "5.1.acaben_10", 3: "5.1.no_acaben_3" }[k];
    if (truc) paraules.push(txt(truc));
    paraules.push(txt("5.1.zero", { k }));
    $("#m1-lectura").innerHTML = lectura(paraules);
    svg.setAttribute("aria-label", txtPla("5.1.aria", { k }));
    $("#m1-marca").hidden = k !== EX51;
  }

  let fet51 = false;
  function inicia51() {
    if (fet51) return;
    fet51 = true;
    CE.pastilles($("#m1-pastilles"), NOMBRES, t => { k51 = t.n; pinta51(); }, EX51 - 2);
    pinta51();
  }

  /* ============================================== 5.2 · És múltiple? ====== */

  // [nombre, de]: tots dins de la targeta (el nombre no passa de 10 vegades). Els quatre
  // últims són els de la regla trencada de la fitxa 1 de la unitat 2: el 12 i el 21 són
  // múltiples del 3 i no acaben en 3; el 13 i el 23 hi acaben i no ho són. Van al final
  // perquè una tasca desada a mitges guarda les posicions de la llista.
  const MULT = [[24, 3], [25, 3], [35, 5], [36, 5], [42, 6], [44, 6], [56, 7], [58, 7], [72, 8], [76, 8],
                [81, 9], [84, 9], [14, 2], [15, 2], [30, 10], [35, 10], [12, 3], [13, 3], [21, 3], [23, 3]];
  const N52 = 5;
  let t52 = null, c52 = null, i52 = 0, triat52 = null;

  /** «3 · 8 = 24» si hi és; si no, les dues files del voltant. */
  function explica52(n, k) {
    const q = Math.floor(n / k);
    return n % k === 0 ? txt("5.2.hi_es", { n, k, q, de: delNombre(k) })
                       : txt("5.2.no_hi_es", { n, k, q, p1: k * q, q2: q + 1, p2: k * (q + 1), de: delNombre(k) });
  }

  function pas52(i, e) {
    c52 = MULT[e.extra.ordre[i]];
    i52 = 0; triat52 = null;
    $("#m2-pregunta").textContent = txtPla("5.2.pregunta", { n: c52[0], k: c52[1] });
    botonsSiNo($("#m2-opcions"), tria52);
    const avis = $("#m2-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t52.resolt() ? txt("comu.ja_fet") : txt("5.2.comenca");
    const seg = $("#m2-seguent");
    seg.disabled = !t52.resolt();
    seg.innerHTML = txt(t52.esUltim() ? "comu.acaba" : "comu.seguent");
    pintaSiNo($("#m2-opcions"), null, c52[0] % c52[1] === 0, t52.resolt());
  }

  function tria52(si) {
    const e = t52.estat();
    if (!e || e.acabada || t52.resolt()) return;
    const [n, k] = c52, bo = n % k === 0, avis = $("#m2-avis");
    triat52 = si;
    if (si === bo) {
      t52.anota(i52 === 0 ? "be" : "pista");
      retroaccio(avis, "encert", explica52(n, k));
    } else if (i52 === 0) {
      i52 = 1;
      retroaccio(avis, "error", txt(si ? "5.2.has_dit_si" : "5.2.has_dit_no", { n, k }),
                 txt("5.2.pista", { n, de: delNombre(k) }));
    } else {
      t52.anota("mostrat");
      retroaccio(avis, "mostra", explica52(n, k));
    }
    pintaSiNo($("#m2-opcions"), triat52, bo, t52.resolt());
    $("#m2-seguent").disabled = !t52.resolt();
  }

  /** Cinc passos: tres de «sí» i dos de «no», barrejats. */
  function nouOrdre52() {
    const idx = MULT.map((_, i) => i);
    const si = CE.barreja(idx.filter(i => MULT[i][0] % MULT[i][1] === 0)).slice(0, 3);
    const no = CE.barreja(idx.filter(i => MULT[i][0] % MULT[i][1] !== 0)).slice(0, 2);
    return CE.barreja(si.concat(no));
  }

  let fet52 = false;
  function inicia52() {
    if (fet52) return;
    fet52 = true;
    t52 = CE.tasca({
      tasca: 5, sub: 2,
      recorregut: $("#m2-recorregut"), represa: $("#m2-represa"), final: $("#m2-final"), cos: [$("#m2-cos")],
      desa: true,
      valida: e => e.total === N52 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N52 &&
                   e.extra.ordre.every(i => MULT[i] !== undefined),
      nom: () => "5.2 · " + txtPla("5.2.nom"),
      pinta: pas52
    });
    $("#m2-seguent").onclick = () => t52.seguent();
    t52.inicia(() => ({ total: N52, extra: { ordre: nouOrdre52() } }));
  }

  /* ================================================== 5.3 · Els trucs ====== */

  const EX53 = { c: 1, d: 2, u: 6 };
  let n53 = Object.assign({}, EX53), compt53 = null;

  /** «1 + 2 + 6 = 9», només amb les xifres que hi ha (36 → «3 + 6 = 9»). */
  function sumaXifres(n) {
    const xs = String(n).split("").map(Number);
    return { text: xs.join(" + "), suma: xs.reduce((a, b) => a + b, 0), xifres: xs.length };
  }

  function fila53(k, si, rao) {
    return '<tr><th scope="row">' + txt("5.3.multiple_de", { k }) + "</th>" +
      '<td class="' + (si ? "si" : "no") + '">' + txt(si ? "comu.si" : "comu.no") + "</td><td>" + rao + "</td></tr>";
  }

  function pinta53() {
    const n = n53.c * 100 + n53.d * 10 + n53.u, u = n % 10;
    $("#t3-nombre").textContent = String(n);
    $("#t3-marca").hidden = !(n53.c === EX53.c && n53.d === EX53.d && n53.u === EX53.u);
    const taula = $("#t3-trucs");
    if (n === 0) {
      taula.innerHTML = '<p class="paraules">' + txt("5.3.zero") + "</p>";
      return;
    }
    const s = sumaXifres(n), de3 = s.suma % 3 === 0;
    const rao3 = (s.xifres > 1 ? txt("5.3.suma", { suma: s.text + " = " + s.suma }) + " " : "") +
      txt(de3 ? "5.3.a_la_taula" : "5.3.no_a_la_taula", { el_s: majuscula(elNombre(s.suma)) });
    taula.innerHTML = '<table class="trucs"><tbody>' +
      fila53(2, u % 2 === 0, txt(u % 2 === 0 ? "5.3.acaba_parell" : "5.3.acaba_senar", { u })) +
      fila53(5, u % 5 === 0, txt(u % 5 === 0 ? "5.3.acaba_0_5" : "5.3.no_acaba_0_5", { u })) +
      fila53(10, u === 0, txt(u === 0 ? "5.3.acaba_0" : "5.3.no_acaba_0", { u })) +
      fila53(3, de3, rao3) +
      "</tbody></table>";
  }

  let fet53 = false;
  function inicia53() {
    if (fet53) return;
    fet53 = true;
    const fes = (k, et) => CE.comptador($("#t3-" + k), { et: txt(et), min: 0, max: 9, valor: n53[k],
      aoCanviar: v => { n53[k] = v; pinta53(); } });
    compt53 = { c: fes("c", "3.1.et_c"), d: fes("d", "3.1.et_d"), u: fes("u", "3.1.et_u") };
    pinta53();
  }

  /* ============================================ 5.4 · Múltiple de 3? ====== */

  // Fins al 999: la suma de les xifres dona com a molt 27, i es busca a la taula del 3.
  const TRES = [123, 214, 405, 88, 111, 520, 312, 71, 255, 403, 36, 58, 147, 202, 600, 710];
  const N54 = 5;
  let t54 = null, n54 = 0, i54 = 0, triat54 = null;

  function explica54(n) {
    const s = sumaXifres(n), si = s.suma % 3 === 0;
    return txt("5.4.suma", { suma: s.text + " = " + s.suma }) + " " +
           txt(si ? "5.4.es" : "5.4.no_es", { el_s: majuscula(elNombre(s.suma)), el_n: elNombre(n) });
  }

  function pas54(i, e) {
    n54 = TRES[e.extra.ordre[i]];
    i54 = 0; triat54 = null;
    $("#m4-pregunta").textContent = txtPla("5.4.pregunta", { n: n54 });
    botonsSiNo($("#m4-opcions"), tria54);
    const avis = $("#m4-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t54.resolt() ? txt("comu.ja_fet") : txt("5.4.comenca");
    const seg = $("#m4-seguent");
    seg.disabled = !t54.resolt();
    seg.innerHTML = txt(t54.esUltim() ? "comu.acaba" : "comu.seguent");
    pintaSiNo($("#m4-opcions"), null, n54 % 3 === 0, t54.resolt());
  }

  function tria54(si) {
    const e = t54.estat();
    if (!e || e.acabada || t54.resolt()) return;
    const bo = n54 % 3 === 0, avis = $("#m4-avis");
    triat54 = si;
    if (si === bo) {
      t54.anota(i54 === 0 ? "be" : "pista");
      retroaccio(avis, "encert", explica54(n54));
    } else if (i54 === 0) {
      i54 = 1;
      retroaccio(avis, "error", txt(si ? "5.4.has_dit_si" : "5.4.has_dit_no", { n: n54 }), txt("5.4.pista", { n: n54 }));
    } else {
      t54.anota("mostrat");
      retroaccio(avis, "mostra", explica54(n54));
    }
    pintaSiNo($("#m4-opcions"), triat54, bo, t54.resolt());
    $("#m4-seguent").disabled = !t54.resolt();
  }

  function nouOrdre54() {
    const idx = TRES.map((_, i) => i);
    const si = CE.barreja(idx.filter(i => TRES[i] % 3 === 0)).slice(0, 3);
    const no = CE.barreja(idx.filter(i => TRES[i] % 3 !== 0)).slice(0, 2);
    return CE.barreja(si.concat(no));
  }

  let fet54 = false;
  function inicia54() {
    if (fet54) return;
    fet54 = true;
    t54 = CE.tasca({
      tasca: 5, sub: 4,
      recorregut: $("#m4-recorregut"), represa: $("#m4-represa"), final: $("#m4-final"), cos: [$("#m4-cos")],
      desa: true,
      valida: e => e.total === N54 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N54 &&
                   e.extra.ordre.every(i => TRES[i] !== undefined),
      nom: () => "5.4 · " + txtPla("5.4.nom"),
      pinta: pas54
    });
    $("#m4-seguent").onclick = () => t54.seguent();
    t54.inicia(() => ({ total: N54, extra: { ordre: nouOrdre54() } }));
  }

  /* ==================================================== arrencada ====== */

  const ARRENCA = { 1: inicia51, 2: inicia52, 3: inicia53, 4: inicia54 };
  let subs = null, subActual = null;

  function inicia() {
    const arrel = $("#mod-multiples");
    if (!subs) {
      omplirTextos(arrel);
      subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); });
    }
    subs.mostra(subActual || CE.subDemanada(5) || 1);
  }

  CE.registra("multiples", inicia);
  const RECOMPTES = () => ({ recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")],
                             resta: txtPla("comu.r_mostrat") });
  CE.registraCataleg("5.2", Object.assign({ nom: txtPla("5.2.nom") }, RECOMPTES()));
  CE.registraCataleg("5.4", Object.assign({ nom: txtPla("5.4.nom") }, RECOMPTES()));
  CE.dades = Object.assign(CE.dades || {}, { multiples: { EX51, MULT, EX53, TRES } });
})();
