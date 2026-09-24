/* ============================================================================
   NOMBRES — mòdul «cdu» de la caixa d'eines · tasca 3
   ----------------------------------------------------------------------------
   Centenes, desenes i unitats amb la mateixa quadrícula: un quadret és 1, una
   columna de 10 quadrets és 10, i un quadrat de 10 files de 10 quadrets és
   100. És el rectangle de la tasca 1 (10 · 10 = 100) i el quadrat de la
   tasca 2 (10² = 100): no hi ha cap material nou.

   Fins al 999 i prou (docs/CRITERIS-DISSENY.md, regla D). Per això cada
   comptador va del 0 al 9 i no es pot passar de 9: amb 10 quadrets solts
   caldria fer una columna, i això és portar-ne.

   3.1 · CENTENES, DESENES I UNITATS
     Tres comptadors, els blocs, la taula de posicions, el nombre i com es
     llegeix. S'obre amb 243: dos-cents quaranta-tres.

   3.2 · FES EL NOMBRE
     Una tasca tancada de cinc nombres. Es posen els blocs i es toca Comprova.
     Mentre es fa, el nombre no surt: si sortís, n'hi hauria prou de moure els
     comptadors fins que coincidís. Tres dels cinc nombres tenen un zero
     (305, 250, 60…), que és on hi ha l'error: 305 fet com a 35.
       · bé al primer intent  → «Correcte.» i com es llegeix;
       · primer error → diu quin nombre ha fet i la pista és la taula de
         posicions del nombre demanat: un camí diferent, la taula del grup;
       · segon error  → la caixa posa els blocs bons.

   COM ES LLEGEIX UN NOMBRE
     Les paraules són dades, com els números, i no frases: per això són aquí i
     no a dades/textos.js. Es fa servir el guionet de la regla D-U-C: entre
     les desenes i les unitats (quaranta-tres), entre les unitats i les
     centenes (dos-cents), i vint-i-u. L'1 de nom és «u»: «cent u», «vint-i-u».
   ========================================================================== */

(function () {
  "use strict";
  const { $, txt, txtPla, omplirTextos, retroaccio, quants, elNombre, lectura } = CE;
  const Q = CE.q;

  const UNITATS = ["zero", "u", "dos", "tres", "quatre", "cinc", "sis", "set", "vuit", "nou", "deu",
                   "onze", "dotze", "tretze", "catorze", "quinze", "setze", "disset", "divuit", "dinou"];
  const DESENES = [null, null, "vint", "trenta", "quaranta", "cinquanta", "seixanta", "setanta",
                   "vuitanta", "noranta"];
  const CENTENES = [null, "cent", "dos-cents", "tres-cents", "quatre-cents", "cinc-cents", "sis-cents",
                    "set-cents", "vuit-cents", "nou-cents"];

  /** Com es llegeix un nombre del 0 al 999. */
  function nomDe(n) {
    if (n === 0) return UNITATS[0];
    const c = Math.floor(n / 100), r = n % 100;
    let resta = "";
    if (r > 0 && r < 20) resta = UNITATS[r];
    else if (r >= 20) {
      const d = Math.floor(r / 10), u = r % 10;
      resta = DESENES[d] + (u ? (d === 2 ? "-i-" : "-") + UNITATS[u] : "");
    }
    return [c ? CENTENES[c] : "", resta].filter(Boolean).join(" ");
  }

  const valor = o => o.c * 100 + o.d * 10 + o.u;
  const xifres = n => ({ c: Math.floor(n / 100), d: Math.floor(n / 10) % 10, u: n % 10 });
  /** «2 centenes, 4 desenes i 3 unitats» */
  const compta = o => txt("3.1.compta", {
    c: quants(o.c, "comu.centena", "comu.centenes"),
    d: quants(o.d, "comu.desena", "comu.desenes"),
    u: quants(o.u, "comu.unitat", "comu.unitats") });

  /** La taula de posicions: Centenes | Desenes | Unitats, com a la fitxa del grup. */
  function taulaPos(o) {
    const col = (k, v) => '<div class="vp-col vp-' + k + '"><span class="vp-nom">' + txt("3.1.et_" + k) +
                          '</span><span class="vp-cel">' + v + "</span></div>";
    return '<div class="posicional">' + col("c", o.c) + col("d", o.d) + col("u", o.u) + "</div>";
  }

  /** Els blocs, amb el nom de cada zona i quants n'hi ha. */
  function pintaBlocs(cont, o) {
    Q.blocs(cont, {
      c: o.c, d: o.d, u: o.u,
      ets: [txt("3.1.et_c"), txt("3.1.et_d"), txt("3.1.et_u")],
      peus: [quants(o.c, "3.1.quadrat", "3.1.quadrats"), quants(o.d, "3.1.columna", "3.1.columnes"),
             quants(o.u, "3.1.solt", "3.1.solts")] });
  }

  /** Els tres comptadors d'un panell. `aoCanviar(o)` rep {c, d, u}. */
  function comptadors(prefix, inici, aoCanviar) {
    const o = Object.assign({}, inici), cs = {};
    ["c", "d", "u"].forEach(k => {
      cs[k] = CE.comptador($("#" + prefix + "-" + k), { et: txt("3.1.et_" + k), sub: txt("3.1.sub_" + k),
        min: 0, max: 9, valor: o[k], aoCanviar: v => { o[k] = v; aoCanviar(o); } });
    });
    return {
      o,
      posa: nou => { Object.assign(o, nou); ["c", "d", "u"].forEach(k => cs[k].posa(o[k])); },
      activa: b => ["c", "d", "u"].forEach(k => cs[k].activa(b))
    };
  }

  /* =============================== 3.1 · Centenes, desenes i unitats ====== */

  const EX31 = { c: 2, d: 4, u: 3 };

  function pinta31(o) {
    const n = valor(o);
    pintaBlocs($("#n1-blocs"), o);
    $("#n1-lectura").innerHTML = lectura([compta(o)]);
    $("#n1-taula").innerHTML = taulaPos(o);
    $("#n1-nombre").innerHTML = lectura(null, String(n)) + lectura([txt("3.1.llegeix", { nom: nomDe(n) })]);
    $("#n1-marca").hidden = !(o.c === EX31.c && o.d === EX31.d && o.u === EX31.u);
    $("#n1-blocs").setAttribute("aria-label", txtPla("3.1.compta", {
      c: quants(o.c, "comu.centena", "comu.centenes"), d: quants(o.d, "comu.desena", "comu.desenes"),
      u: quants(o.u, "comu.unitat", "comu.unitats") }));
  }

  let fet31 = false;
  function inicia31() {
    if (fet31) return;
    fet31 = true;
    const cs = comptadors("n1", EX31, pinta31);
    pinta31(cs.o);
  }

  /* =========================================== 3.2 · Fes el nombre ====== */

  const AMB_ZERO = [305, 250, 403, 510, 108, 60, 900];
  const SENSE_ZERO = [124, 36, 222, 471, 17];
  const N32 = 5;
  let fes = null, nAra = 0, nIntents = 0, cs32 = null;

  function comprova32() {
    const e = fes.estat();
    if (!e || e.acabada || fes.resolt()) return;
    const o = cs32.o, fet = valor(o), bo = xifres(nAra), avis = $("#n2-avis");
    if (fet === nAra) {
      fes.anota(nIntents === 0 ? "be" : "pista");
      retroaccio(avis, "encert", txt("3.2.encert", { compta: compta(o), nom: nomDe(nAra) }));
      acaba32();
    } else if (nIntents === 0) {
      nIntents = 1;
      $("#n2-taula").innerHTML = taulaPos(bo);
      $("#n2-taula").hidden = false;
      retroaccio(avis, "error", txt("3.2.fet", { el_m: elNombre(fet) }), txt("3.2.pista"));
    } else {
      fes.anota("mostrat");
      cs32.posa(bo);
      pintaBlocs($("#n2-blocs"), bo);
      retroaccio(avis, "mostra", txt("3.2.mostra", { compta: compta(bo), nom: nomDe(nAra) }));
      acaba32();
    }
  }

  function acaba32() {
    cs32.activa(false);
    $("#n2-taula").innerHTML = taulaPos(xifres(nAra));
    $("#n2-taula").hidden = false;
    $("#n2-comprova").disabled = true;
    $("#n2-seguent").disabled = false;
  }

  function pas32(i, e) {
    nAra = e.extra.nombres[i];
    nIntents = 0;
    $("#n2-pregunta").textContent = txtPla("3.2.pregunta", { n: nAra });
    const resolt = fes.resolt();
    const inici = resolt ? xifres(nAra) : { c: 0, d: 0, u: 0 };
    cs32.posa(inici);
    cs32.activa(!resolt);
    pintaBlocs($("#n2-blocs"), inici);
    $("#n2-taula").hidden = !resolt;
    if (resolt) $("#n2-taula").innerHTML = taulaPos(inici);
    $("#n2-comprova").disabled = resolt;
    const avis = $("#n2-avis");
    avis.className = "avis neutre";
    avis.innerHTML = resolt ? txt("comu.ja_fet") : txt("3.2.comenca");
    const seguent = $("#n2-seguent");
    seguent.disabled = !resolt;
    seguent.innerHTML = txt(fes.esUltim() ? "comu.acaba" : "comu.seguent");
  }

  let fet32 = false;
  function inicia32() {
    if (fet32) return;
    fet32 = true;
    cs32 = comptadors("n2", { c: 0, d: 0, u: 0 }, o => pintaBlocs($("#n2-blocs"), o));
    fes = CE.tasca({
      tasca: 3, sub: 2,
      recorregut: $("#n2-recorregut"),
      represa: $("#n2-represa"),
      final: $("#n2-final"),
      cos: [$("#n2-cos")],
      desa: true,
      valida: e => e.total === N32 && e.extra && Array.isArray(e.extra.nombres) &&
                   e.extra.nombres.length === N32 &&
                   e.extra.nombres.every(n => AMB_ZERO.includes(n) || SENSE_ZERO.includes(n)),
      nom: () => "3.2 · " + txtPla("3.2.nom"),
      pinta: pas32
    });
    $("#n2-comprova").onclick = comprova32;
    $("#n2-seguent").onclick = () => fes.seguent();
    fes.inicia(() => ({ total: N32, extra: { nombres: CE.barreja(
      CE.barreja(AMB_ZERO).slice(0, 3).concat(CE.barreja(SENSE_ZERO).slice(0, 2))) } }));
  }

  /* ==================================================== arrencada ====== */

  const ARRENCA = { 1: inicia31, 2: inicia32 };
  let subs = null, subActual = null;

  function inicia() {
    const arrel = $("#mod-cdu");
    if (!subs) {
      omplirTextos(arrel);
      subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); });
    }
    subs.mostra(subActual || CE.subDemanada(3) || 1);
  }

  CE.registra("cdu", inicia);
  CE.registraCataleg("3.2", { nom: txtPla("3.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")],
    resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { cdu: { EX31, AMB_ZERO, SENSE_ZERO, nomDe } });
})();
