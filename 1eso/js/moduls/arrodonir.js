/* ============================================================================
   ARRODONIR — mòdul «arrodonir» de la caixa d'eines · tasca 19 · unitat 5
   ----------------------------------------------------------------------------
   Arrodonir a les dècimes és buscar la dècima més a prop: 3,47 és entre 3,4 i
   3,5, i passa de la ratlla del mig (3,45), per això s'arrodoneix a 3,5.
   Truncar és tallar i prou: 3,4. Es fa a la recta numèrica, que és el segon
   model del curs per als decimals i l'arrodoniment (docs/MAPA-ADAPTACIO.md,
   apartat 3). Activitat 2 de la situació «Decimals i arrel quadrada».

   19.1 · EL DECIMAL A LA RECTA   tres comptadors (unitats, dècimes i
                                  centèsimes) i la recta de la dècima d'abans
                                  a la de després, amb una ratlla per cada
                                  centèsima i la del mig més llarga. Diu de
                                  quina dècima és més a prop, i l'arrodonit i
                                  el truncat. S'obre amb 3,47, l'exemple del
                                  llibre. Les unitats van del 0 al 8: 8,99
                                  arrodonit és 9,0, i no es passa de 9,99.
   19.2 · ARRODONEIX              tasca tancada de cinc passos: el decimal a la
                                  recta, i tres respostes. Les dolentes són les
                                  confusions de debò: la regla trencada
                                  «arrodonir és tallar» (3,47 → 3,4), o anar
                                  amunt quan no toca, i arrodonir a les
                                  unitats en lloc de les dècimes. Tres casos
                                  van amunt i dos avall, perquè «sempre amunt»
                                  tampoc no encerti.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, lectura } = CE;
  const Q = CE.q;
  const dec = Q.dec;

  /** La dècima d'abans, la de després i l'arrodonida, en centèsimes. */
  function decimes(c) {
    const a = c - c % 10, b = a + 10;
    return { a, b, mig: a + 5, r: c % 10 >= 5 ? b : a };
  }
  function dibuixa(svg, c) {
    const x = decimes(c);
    Q.recta(svg, x.a, x.b, 1, { mig: true, punt: c });
    svg.setAttribute("aria-label", txtPla("19.1.aria", { a: dec(x.a, 1), b: dec(x.b, 1), n: dec(c) }));
  }

  /* ======================================= 19.1 · El decimal a la recta ====== */

  const EX191 = 347;
  function pinta1(c) {
    const x = decimes(c), n = dec(c), a = dec(x.a, 1), b = dec(x.b, 1);
    dibuixa($("#ra-svg"), c);
    let html;
    if (c % 10 === 0) {
      html = lectura([txt("19.1.ja_decima", { n })]);
    } else {
      const cap = c % 10 > 5 ? "amunt" : c % 10 === 5 ? "justa" : "avall";
      html = lectura([txt("19.1.entre", { n, a, b }), txt("19.1.mig", { m: dec(x.mig) }), txt("19.1." + cap, { n, a, b })],
                     a + " < " + n + " < " + b) +
             lectura([txt("19.1.arrodonit", { r: dec(x.r, 1) }), txt("19.1.truncat", { t: a })]);
    }
    $("#ra-lectura").innerHTML = html;
    $("#ra-marca").hidden = c !== EX191;
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    const o = { u: 3, d: 4, c: 7 }, valor = () => o.u * 100 + o.d * 10 + o.c;
    ["u", "d", "c"].forEach(k => CE.comptador($("#ra-" + k), { et: txt("18.1.et_" + k), min: 0, max: k === "u" ? 8 : 9,
      valor: o[k], aoCanviar: v => { o[k] = v; pinta1(valor()); } }));
    pinta1(valor());
  }

  /* ================================================ 19.2 · Arrodoneix ====== */

  const AMUNT = [347, 586, 128, 675, 255];
  const AVALL = [342, 613, 471, 234];
  const N2 = 5;
  let t2 = null, c2 = 0, i2 = 0, opcions2 = [];

  /** La bona; l'altra dècima (truncar, si anava amunt, o pujar, si anava avall); i
      arrodonir a les unitats. */
  function opcionsDe(c) {
    const x = decimes(c);
    return [["bona", dec(x.r, 1)], ["altra", dec(x.r === x.a ? x.b : x.a, 1)], ["unitat", String(Math.round(c / 100))]];
  }
  function pas2(i, e) {
    c2 = e.extra.casos[i]; i2 = 0;
    $("#rb-pregunta").textContent = txtPla("19.2.pregunta", { n: dec(c2) });
    dibuixa($("#rb-svg"), c2);
    opcions2 = e.extra.torns[i].map(k => opcionsDe(c2)[k]);
    const cont = $("#rb-opcions");
    cont.innerHTML = opcions2.map((op, k) => '<button type="button" class="btn opcio-sino opcio-dec" data-k="' + k + '">' +
      op[1] + "</button>").join("");
    $$(".opcio-dec", cont).forEach(b => { b.onclick = () => tria2(Number(b.dataset.k), b); });
    const avis = $("#rb-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("19.2.comenca");
    $("#rb-seguent").disabled = !t2.resolt();
    $("#rb-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() {
    $$(".opcio-dec", $("#rb-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", opcions2[b.dataset.k][0] === "bona"); });
  }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const op = opcions2[k], avis = $("#rb-avis"), x = decimes(c2), n = dec(c2), r = dec(x.r, 1);
    const frase = txt(c2 % 10 === 5 ? "19.2.encert_justa" : "19.2.encert", { n, r });
    if (op[0] === "bona") { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      const error = op[0] === "unitat" ? "19.2.error_unitat" : x.r === x.b ? "19.2.error_truncat" : "19.2.error_amunt";
      retroaccio(avis, "error", txt(error, { n }), txt("19.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); }
    $("#rb-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    const tots = AMUNT.concat(AVALL);
    t2 = CE.tasca({
      tasca: 19, sub: 2,
      recorregut: $("#rb-recorregut"), represa: $("#rb-represa"), final: $("#rb-final"), cos: [$("#rb-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.casos) && e.extra.casos.length === N2 &&
                   e.extra.casos.every(c => tots.includes(c)) && Array.isArray(e.extra.torns),
      nom: () => "19.2 · " + txtPla("19.2.nom"),
      pinta: pas2
    });
    $("#rb-seguent").onclick = () => t2.seguent();
    // Cinc passos: tres que van amunt i dos avall, barrejats.
    t2.inicia(() => {
      const casos = CE.barreja(CE.barreja(AMUNT).slice(0, 3).concat(CE.barreja(AVALL).slice(0, 2)));
      return { total: N2, extra: { casos, torns: casos.map(() => CE.barreja([0, 1, 2])) } };
    });
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-arrodonir");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(19) || 1);
  }
  CE.registra("arrodonir", inicia);
  CE.registraCataleg("19.2", { nom: txtPla("19.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { arrodonir: { EX191, AMUNT, AVALL, opcionsDe, decimes } });
})();
