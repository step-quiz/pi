/* ============================================================================
   ELS DECIMALS — mòdul «decimals» de la caixa d'eines · tasca 18 · unitat 5
   ----------------------------------------------------------------------------
   El quadrat de 100 quadrets és 1 unitat: una columna de 10 quadrets és 0,1
   (una dècima) i un quadret solt és 0,01 (una centèsima). Són els blocs de la
   unitat 1 (js/quadricula.js, `blocs`), amb el quadrat com a unitat: el 243
   de la tasca 3 aquí és 2,43. Activitats 1 i 2 de la situació «Decimals i
   arrel quadrada» (el llibre: «Què en sabem?» i «Els decimals»).

   Fins a 9,99, amb dues xifres decimals com a molt (decisió del docent del
   29/9/2026): cada comptador va del 0 al 9, com a la tasca 3. Els decimals es
   guarden com a centèsimes enteres (2,43 és 243).

   18.1 · FES EL DECIMAL      tres comptadors (quadrats, columnes i quadrets),
                              els blocs, la taula de posicions amb la coma, el
                              decimal i com es llegeix. S'obre amb 2,43.
   18.2 · QUIN DECIMAL ÉS?    tasca tancada de cinc passos: els blocs, i tres
                              decimals per triar. Les dolentes són les
                              confusions de debò: girar les columnes i els
                              quadrets (2,34 per 2,43, i 3,4 per 3,04: el zero
                              que manté el lloc), i llegir els blocs com a la
                              unitat 1, sense coma (243).
   18.3 · QUIN ÉS MÉS GRAN?   tasca tancada de cinc passos: dos decimals i es
                              toca el més gran. La regla trencada del llibre
                              (l'error de la Berta): «més xifres vol dir més
                              gran», i 0,75 sembla més gran que 0,8. Tres
                              parelles la fan fallar i dues no, perquè tampoc
                              «menys xifres» sigui una regla. En contestar,
                              surten els blocs de tots dos: 80 quadrets i 75.
                              Amb dues opcions, el segon intent sempre és
                              l'altre: compta com a correcte amb pista.

   COM ES LLEGEIX UN DECIMAL
     Com al llibre: les unitats, i la part decimal en l'última posició que hi
     ha. 2,43 és «dues unitats i quaranta-tres centèsimes»; 3,4 és «tres
     unitats i quatre dècimes». Unitat, dècima i centèsima són femenines: «una»,
     «dues», «vint-i-una». Les paraules són dades, com a la tasca 3.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, quants, lectura } = CE;
  const Q = CE.q;
  const dec = Q.dec;

  /* ------------------------------------------------ com es llegeix ------ */
  const UNS = ["zero", "una", "dues", "tres", "quatre", "cinc", "sis", "set", "vuit", "nou", "deu",
               "onze", "dotze", "tretze", "catorze", "quinze", "setze", "disset", "divuit", "dinou"];
  const DESENES = [null, null, "vint", "trenta", "quaranta", "cinquanta", "seixanta", "setanta",
                   "vuitanta", "noranta"];
  /** Del 0 al 99, en femení: «una», «vint-i-una», «trenta-dues». */
  function nomF(n) {
    if (n < 20) return UNS[n];
    const d = Math.floor(n / 10), u = n % 10;
    return DESENES[d] + (u ? (d === 2 ? "-i-" : "-") + UNS[u] : "");
  }
  /** «dues unitats i quaranta-tres centèsimes», «quatre dècimes», «una unitat». */
  function nomDecimal(c) {
    const u = Math.floor(c / 100), r = c % 100, parts = [];
    if (u) parts.push(nomF(u) + " " + txtPla(u === 1 ? "comu.unitat" : "comu.unitats"));
    if (r && r % 10 === 0) parts.push(nomF(r / 10) + " " + txtPla(r === 10 ? "comu.decima" : "comu.decimes"));
    else if (r) parts.push(nomF(r) + " " + txtPla(r === 1 ? "comu.centesima" : "comu.centesimes"));
    return parts.length ? parts.join(" " + txtPla("comu.i") + " ") : UNS[0];
  }

  const xifres = c => ({ u: Math.floor(c / 100), d: Math.floor(c / 10) % 10, c: c % 10 });
  const valor = o => o.u * 100 + o.d * 10 + o.c;
  /** «2 unitats», «4 dècimes», «3 centèsimes»: els forats de 18.1.compta. */
  const compta = o => ({
    u: quants(o.u, "comu.unitat", "comu.unitats"),
    d: quants(o.d, "comu.decima", "comu.decimes"),
    c: quants(o.c, "comu.centesima", "comu.centesimes") });

  /** La taula de posicions dels decimals: Unitats | , | Dècimes | Centèsimes. */
  function taulaPos(o) {
    const col = (k, v) => '<div class="vp-col vp-' + k + '"><span class="vp-nom">' + txt("18.1.et_" + k) +
                          '</span><span class="vp-cel">' + v + "</span></div>";
    return '<div class="posicional">' + col("u", o.u) +
      '<div class="vp-col vp-coma" aria-hidden="true"><span class="vp-nom">&nbsp;</span><span class="vp-cel">,</span></div>' +
      col("d", o.d) + col("c", o.c) + "</div>";
  }
  const pintaBlocs = (cont, o) => Q.blocs(cont, { c: o.u, d: o.d, u: o.c });
  const ariaBlocs = o => txtPla("18.2.aria", { q: o.u, col: o.d, qs: o.c });

  /* ============================================= 18.1 · Fes el decimal ====== */

  const EX181 = { u: 2, d: 4, c: 3 };
  function pinta1(o) {
    const n = valor(o);
    pintaBlocs($("#xa-blocs"), o);
    $("#xa-blocs").setAttribute("aria-label", ariaBlocs(o));
    $("#xa-taula").innerHTML = taulaPos(o);
    $("#xa-lectura").innerHTML =
      lectura([txt("18.1.compta", compta(o)),
               txt("18.1.total", { quadrets: quants(n, "comu.quadret", "comu.quadrets"),
                                   cent: quants(n, "comu.centesima", "comu.centesimes") })], dec(n)) +
      lectura([txt("18.1.llegeix", { nom: nomDecimal(n) })]);
    $("#xa-marca").hidden = !(o.u === EX181.u && o.d === EX181.d && o.c === EX181.c);
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    const o = Object.assign({}, EX181);
    ["u", "d", "c"].forEach(k => CE.comptador($("#xa-" + k), { et: txt("18.1.et_" + k), sub: txt("18.1.sub_" + k),
      min: 0, max: 9, valor: o[k], aoCanviar: v => { o[k] = v; pinta1(o); } }));
    pinta1(o);
  }

  /* ========================================== 18.2 · Quin decimal és? ====== */

  // Amb un zero a les dècimes (3,04): és on hi ha l'error de girar-les.
  const ZERO_MIG = [304, 208, 105];
  const ALTRES = [243, 150, 75, 612, 490];
  const N2 = 5;
  let t2 = null, c2 = 0, i2 = 0, opcions2 = [];

  /** La bona; girar les columnes i els quadrets (2,43 → 2,34; 3,04 → 3,4); i llegir
      els blocs sense coma, com a la unitat 1 (243). */
  function opcionsDe(c) {
    const x = xifres(c);
    return [["bona", dec(c)], ["girat", dec(x.u * 100 + x.c * 10 + x.d)], ["natural", String(c)]];
  }
  function pas2(i, e) {
    c2 = e.extra.casos[i]; i2 = 0;
    const o = xifres(c2);
    pintaBlocs($("#xb-blocs"), o);
    $("#xb-blocs").setAttribute("aria-label", ariaBlocs(o));
    opcions2 = e.extra.torns[i].map(k => opcionsDe(c2)[k]);
    const cont = $("#xb-opcions");
    cont.innerHTML = opcions2.map((op, k) => '<button type="button" class="btn opcio-sino opcio-dec" data-k="' + k + '">' +
      op[1] + "</button>").join("");
    $$(".opcio-dec", cont).forEach(b => { b.onclick = () => tria2(Number(b.dataset.k), b); });
    const avis = $("#xb-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("18.2.comenca");
    $("#xb-seguent").disabled = !t2.resolt();
    $("#xb-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() {
    $$(".opcio-dec", $("#xb-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", opcions2[b.dataset.k][0] === "bona"); });
  }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const op = opcions2[k], avis = $("#xb-avis");
    const frase = txt("18.2.encert", Object.assign(compta(xifres(c2)), { n: dec(c2) }));
    if (op[0] === "bona") { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(op[0] === "girat" ? "18.2.error_girat" : "18.2.error_natural"), txt("18.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); }
    $("#xb-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    const tots = ZERO_MIG.concat(ALTRES);
    t2 = CE.tasca({
      tasca: 18, sub: 2,
      recorregut: $("#xb-recorregut"), represa: $("#xb-represa"), final: $("#xb-final"), cos: [$("#xb-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.casos) && e.extra.casos.length === N2 &&
                   e.extra.casos.every(c => tots.includes(c)) && Array.isArray(e.extra.torns),
      nom: () => "18.2 · " + txtPla("18.2.nom"),
      pinta: pas2
    });
    $("#xb-seguent").onclick = () => t2.seguent();
    // Cinc passos: dos amb el zero a les dècimes i tres més, barrejats.
    t2.inicia(() => {
      const casos = CE.barreja(CE.barreja(ZERO_MIG).slice(0, 2).concat(CE.barreja(ALTRES).slice(0, 3)));
      return { total: N2, extra: { casos, torns: casos.map(() => CE.barreja([0, 1, 2])) } };
    });
  }

  /* ========================================= 18.3 · Quin és més gran? ====== */

  // [el més gran, el més petit]. Les «trencades»: el més gran té menys xifres (0,8 i
  // 0,75, l'error de la Berta del llibre). Les altres: el més gran en té més.
  const TRENCADES = [[80, 75], [340, 304], [250, 245], [130, 125], [60, 56]];
  const CONTROL = [[155, 150], [85, 80], [248, 240]];
  const N3 = 5;
  let t3 = null, p3 = null, i3 = 0, ordre3 = [];
  const xifresDec = c => dec(c).split(",")[1] ? dec(c).split(",")[1].length : 0;

  function pas3(i, e) {
    p3 = e.extra.parelles[i]; i3 = 0;
    const [g, p] = p3, ordre = e.extra.esq[i] ? [g, p] : [p, g];
    ordre3 = ordre;
    const cont = $("#xc-opcions");
    cont.innerHTML = ordre.map(c => '<button type="button" class="btn opcio-sino opcio-dec" data-c="' + c + '">' +
      dec(c) + "</button>").join("");
    $$(".opcio-dec", cont).forEach(b => { b.onclick = () => tria3(Number(b.dataset.c), b); });
    const avis = $("#xc-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t3.resolt() ? txt("comu.ja_fet") : txt("18.3.comenca");
    $("#xc-seguent").disabled = !t3.resolt();
    $("#xc-seguent").innerHTML = txt(t3.esUltim() ? "comu.acaba" : "comu.seguent");
    // Els blocs de tots dos, només quan ja s'ha contestat: si no, la resposta es veuria.
    $("#xc-dibuix").hidden = true;
    if (t3.resolt()) marca3();
  }
  /** Ensenya els blocs dels dos decimals. Es dibuixen en ensenyar-los, perquè la mida
      del quadret depèn de l'amplada que hi ha (js/quadricula.js, `blocs`). */
  function ensenyaDibuix3() {
    $("#xc-dibuix").hidden = false;
    pintaDibuix3(ordre3);
  }
  function pintaDibuix3(ordre) {
    ordre.forEach((c, k) => {
      const cap = $("#xc-cap-" + k), cont = $("#xc-blocs-" + k);
      cap.textContent = dec(c);
      pintaBlocs(cont, xifres(c));
      cont.setAttribute("aria-label", dec(c) + ": " + ariaBlocs(xifres(c)));
    });
  }
  function marca3() {
    $$(".opcio-dec", $("#xc-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", Number(b.dataset.c) === p3[0]); });
    ensenyaDibuix3();
  }
  function tria3(c, boto) {
    const e = t3.estat();
    if (!e || e.acabada || t3.resolt()) return;
    const [g, p] = p3, avis = $("#xc-avis");
    const frase = txt("18.3.encert", { g: dec(g), cg: g, p: dec(p), cp: p });
    if (c === g) { t3.anota(i3 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca3(); }
    else {
      // Amb dues opcions, el segon intent sempre és l'altre: el primer error ja porta
      // la pista, i els blocs de tots dos surten ara mateix (regla G).
      i3 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(xifresDec(p) > xifresDec(g) ? "18.3.error_llarg" : "18.3.error_curt"),
                 txt("18.3.pista", { a: dec(g, 2), b: dec(p, 2) }));
      ensenyaDibuix3();
    }
    $("#xc-seguent").disabled = !t3.resolt();
  }
  let fet3 = false;
  function inicia3() {
    if (fet3) return; fet3 = true;
    const totes = TRENCADES.concat(CONTROL).map(x => x.join("-"));
    t3 = CE.tasca({
      tasca: 18, sub: 3,
      recorregut: $("#xc-recorregut"), represa: $("#xc-represa"), final: $("#xc-final"), cos: [$("#xc-cos")],
      desa: true,
      valida: e => e.total === N3 && e.extra && Array.isArray(e.extra.parelles) && e.extra.parelles.length === N3 &&
                   e.extra.parelles.every(x => Array.isArray(x) && totes.includes(x.join("-"))) &&
                   Array.isArray(e.extra.esq),
      nom: () => "18.3 · " + txtPla("18.3.nom"),
      pinta: pas3
    });
    $("#xc-seguent").onclick = () => t3.seguent();
    // Cinc passos: tres parelles que fan fallar la regla «més xifres, més gran» i dues que no.
    t3.inicia(() => {
      const parelles = CE.barreja(CE.barreja(TRENCADES).slice(0, 3).concat(CE.barreja(CONTROL).slice(0, 2)));
      return { total: N3, extra: { parelles, esq: parelles.map(() => Math.random() < 0.5) } };
    });
  }

  /* ==================================================== arrencada ====== */

  const ARRENCA = { 1: inicia1, 2: inicia2, 3: inicia3 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-decimals");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(18) || 1);
  }
  CE.registra("decimals", inicia);
  const recomptes = [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")];
  CE.registraCataleg("18.2", { nom: txtPla("18.2.nom"), recomptes, resta: txtPla("comu.r_mostrat") });
  CE.registraCataleg("18.3", { nom: txtPla("18.3.nom"), recomptes, resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { decimals: { EX181, ZERO_MIG, ALTRES, TRENCADES, CONTROL, nomDecimal, opcionsDe } });
})();
