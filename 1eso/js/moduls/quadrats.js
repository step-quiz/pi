/* ============================================================================
   QUADRATS — mòdul «quadrat» de la caixa d'eines · tasca 2
   ----------------------------------------------------------------------------
   3² és un quadrat de 3 per 3. És el mateix rectangle de la tasca 1, amb
   tantes files com quadrets té cada fila. I l'arrel quadrada és el camí
   invers: tens els quadrets i busques el costat.

   2.1 · EL QUADRAT D'UN NOMBRE
     Es tria el costat, de l'1 al 10, i surt el quadrat a la taula de quadrets.
     Sota, primer les paraules, després 3 · 3 = 9 i al final 3² = 9, que és la
     manera curta d'escriure el que ja s'ha vist (regla 5). S'obre amb 3.

   2.2 · QUIN DIBUIX ÉS?  (la regla trencada: 3² no és 3 · 2)
     Una tasca tancada de cinc passos. Dos dibuixos: el quadrat de n per n i el
     rectangle de n files de 2. Tres passos pregunten n² i dos pregunten n · 2,
     barrejats: si tots preguntessin n², tocar sempre el més gran encertaria.
     L'error «3² = 6» es desmunta amb el dibuix: el que s'ha tocat es queda amb
     el seu rètol, «3 · 2 = 6. No és un quadrat», i la pàgina acaba amb les dues
     formes a la vista (regla G). Amb dos dibuixos, el segon intent sempre és
     l'altre: compta com a correcte amb pista. El 2 no hi surt, perquè 2² i
     2 · 2 són el mateix dibuix.

   2.3 · EL COSTAT DEL QUADRAT  (l'arrel quadrada)
     Es tria quants quadrets hi ha, de l'1 al 100, i es fa el quadrat més gran
     que es pot. Si en sobren, van a la vora del quadrat següent, i els llocs
     que falten per acabar-lo es veuen buits. Així 13 és entre 9 i 16, i l'arrel
     de 13 és entre 3 i 4: és l'exercici del grup, dit amb el dibuix.

   2.4 · ENTRE QUINS DOS NOMBRES?  (unitat 5: les arrels no exactes)
     Una tasca tancada de cinc passos: √20, i tres parelles de nombres. Les
     dolentes són les confusions de debò: la regla trencada de la fitxa de la
     unitat 5, «l'arrel és la meitat» (l'error del Joel del llibre: √16 = 8),
     que aquí dona 10 i 11; i passar-se d'un (5 i 6), sense mirar que 5 · 5 ja
     passa de 20. Tots els nombres, fins al 100: els quadrats hi són a la
     targeta, de 1 · 1 a 10 · 10. En contestar, surt el dibuix de la 2.3.
   ========================================================================== */

(function () {
  "use strict";
  const { $, $$, el, txt, txtPla, omplirTextos, retroaccio, quants, rect, deN, lectura } = CE;
  const Q = CE.q;
  const qu = n => quants(n, "comu.quadret", "comu.quadrets");

  /* ===================================== 2.1 · El quadrat d'un nombre ====== */

  const COSTATS = Array.from({ length: 10 }, (_, i) => ({ et: String(i + 1), n: i + 1 }));
  const EX21 = 3;
  let q1 = EX21;

  function pinta21() {
    const n = q1, svg = $("#q1-svg");
    Q.taula(svg, { f: n, c: n });
    svg.setAttribute("aria-label", txtPla("2.1.files", { rect: rect(n, n) }) + " " +
                                   txtPla("2.1.total", { quadrets: qu(n * n) }));
    $("#q1-lectura").innerHTML =
      lectura([txt("2.1.files", { rect: rect(n, n) }), txt("2.1.total", { quadrets: qu(n * n) })],
              n + " · " + n + " = " + n * n) +
      lectura([txt("2.1.curt")], n + "² = " + n * n) +
      lectura([txt("2.1.llegeix", { n })]);
    $("#q1-marca").hidden = n !== EX21;
  }

  let fet21 = false;
  function inicia21() {
    if (fet21) return;
    fet21 = true;
    CE.pastilles($("#q1-pastilles"), COSTATS, c => { q1 = c.n; pinta21(); }, EX21 - 1);
    pinta21();
  }

  /* ========================================== 2.2 · Quin dibuix és? ====== */

  const NS = [3, 4, 5, 6, 7];
  const N22 = 5, M22 = 24, V22 = 7 * M22 + 16;
  let tria = null, tAra = null, tIntents = 0, tTriat = null;

  /** Un dibuix d'opció: el quadrat («q») o el rectangle de n files de 2 («d»).
      Els dos a la mateixa escala, perquè la mida també és informació. */
  function dibuix(n, o) {
    const cols = o === "q" ? n : 2;
    const svg = el("svg", { viewBox: "0 0 " + V22 + " " + V22, "aria-hidden": "true", focusable: "false" });
    const x = (V22 - cols * M22) / 2, y = (V22 - n * M22) / 2;
    Q.rectangle(svg, x, y, n, cols, M22, "q");
    return svg;
  }

  function pinta22() {
    const e = tria.estat(), resolt = e.res[e.pas] != null;
    const { n, tipus, esq } = tAra;
    const cont = $("#q2-opcions");
    cont.textContent = "";
    (esq === "q" ? ["q", "d"] : ["d", "q"]).forEach(o => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "opcio-dibuix";
      b.dataset.o = o;
      b.appendChild(dibuix(n, o));
      const peu = document.createElement("span");
      peu.className = "peu-dibuix";
      peu.textContent = o === "q" ? n + "² = " + n * n : n + " · 2 = " + 2 * n;
      // el rètol només surt quan ja s'ha tocat: si no, la resposta seria llegir-lo
      peu.hidden = !(resolt || o === tTriat);
      b.appendChild(peu);
      b.setAttribute("aria-label", txtPla("2.2.aria", { rect: rect(n, o === "q" ? n : 2) }));
      if (resolt && o === tipus) b.classList.add("bona");
      if (o === tTriat && o !== tipus) { b.classList.add("mal"); b.disabled = true; }
      if (resolt) b.disabled = true;
      b.onclick = () => tria22(o);
      cont.appendChild(b);
    });
  }

  function tria22(o) {
    const e = tria.estat();
    if (!e || e.acabada || tria.resolt()) return;
    tTriat = o;
    const { n, tipus } = tAra, avis = $("#q2-avis");
    const d = { n, q: n * n, d: 2 * n };
    if (o === tipus) {
      tria.anota(tIntents === 0 ? "be" : "pista");
      retroaccio(avis, "encert", txt(tipus === "q" ? "2.2.encert_q" : "2.2.encert_d", d));
    } else if (tIntents === 0) {
      tIntents = 1;
      retroaccio(avis, "error", txt(o === "q" ? "2.2.es_q" : "2.2.es_d", d),
                 txt(tipus === "q" ? "2.2.p_q" : "2.2.p_d", d));
    } else {                                  // no hi arriba: el dibuix dolent queda desactivat
      tria.anota("mostrat");
      retroaccio(avis, "mostra", txt(tipus === "q" ? "2.2.encert_q" : "2.2.encert_d", d));
    }
    $("#q2-seguent").disabled = !tria.resolt();
    pinta22();
    // refer els dibuixos treu el focus: es posa a l'altre dibuix o a «Següent pas»
    const seguent = $("#q2-seguent"), altre = $("#q2-opcions .opcio-dibuix:not([disabled])");
    if (tria.resolt()) seguent.focus(); else if (altre) altre.focus();
  }

  function pas22(i, e) {
    tAra = e.extra.passos[i];
    tIntents = 0; tTriat = null;
    $("#q2-pregunta").textContent = txtPla(tAra.tipus === "q" ? "2.2.pregunta_q" : "2.2.pregunta_d",
                                           { n: tAra.n });
    const avis = $("#q2-avis");
    avis.className = "avis neutre";
    avis.innerHTML = tria.resolt() ? txt("comu.ja_fet") : txt("2.2.comenca");
    const seguent = $("#q2-seguent");
    seguent.disabled = !tria.resolt();
    seguent.innerHTML = txt(tria.esUltim() ? "comu.acaba" : "comu.seguent");
    pinta22();
  }

  /** Cinc passos: tres de n² i dos de n · 2, amb el quadrat a una banda o a
      l'altra a l'atzar. */
  function nousPassos() {
    const tipus = CE.barreja(["q", "q", "q", "d", "d"]);
    return CE.barreja(NS).slice(0, N22).map((n, i) => ({ n, tipus: tipus[i],
      esq: Math.random() < 0.5 ? "q" : "d" }));
  }

  let fet22 = false;
  function inicia22() {
    if (fet22) return;
    fet22 = true;
    tria = CE.tasca({
      tasca: 2, sub: 2,
      recorregut: $("#q2-recorregut"),
      represa: $("#q2-represa"),
      final: $("#q2-final"),
      cos: [$("#q2-cos")],
      desa: true,
      valida: e => e.total === N22 && e.extra && Array.isArray(e.extra.passos) &&
                   e.extra.passos.length === N22 &&
                   e.extra.passos.every(p => NS.includes(p.n) && /^[qd]$/.test(p.tipus) && /^[qd]$/.test(p.esq)),
      nom: () => "2.2 · " + txtPla("2.2.nom"),
      pinta: pas22
    });
    $("#q2-seguent").onclick = () => tria.seguent();
    tria.inicia(() => ({ total: N22, extra: { passos: nousPassos() } }));
  }

  /* ==================================== 2.3 · El costat del quadrat ====== */

  const EX23 = 16;
  let q3 = EX23, q3Comptador = null;

  /** Les caselles de la vora del quadrat següent, en l'ordre en què s'omplen:
      la columna de la dreta de dalt a baix, i després la fila de sota de
      dreta a esquerra. Són 2k + 1, que és el que va de k² a (k + 1)². */
  function vora(k) {
    const v = [];
    for (let f = 0; f < k; f++) v.push({ f, c: k });
    for (let c = k; c >= 0; c--) v.push({ f: k, c });
    return v;
  }

  /** El quadrat més gran que es pot fer amb n quadrets, i els que sobren a la vora
      del següent. El fan servir la 2.3 i la 2.4. */
  function dibuixaCostat(svg, n) {
    const k = Math.floor(Math.sqrt(n)), sobren = n - k * k;
    Q.taula(svg, { f: k, c: k, extra: (s, T) => {
      if (!sobren) return;
      vora(k).forEach((p, i) => Q.quadret(s, T.x + p.c * T.m, T.y + p.f * T.m, T.m, i < sobren ? "q b" : "q falta"));
    } });
  }

  function pinta23() {
    const n = q3, k = Math.floor(Math.sqrt(n)), sobren = n - k * k, svg = $("#q3-svg");
    dibuixaCostat(svg, n);
    const k2 = k + 1, q1 = k * k, q2 = k2 * k2;
    let paraules, simbols;
    if (!sobren) {
      paraules = [txt("2.3.exacte", { quadrets: qu(n), de_k: deN(k), k }),
                  txt("2.3.costat", { costat: qu(k) })];
      simbols = "√" + n + " = " + k;
      $("#q3-lectura").innerHTML = lectura(paraules, simbols) +
        lectura([txt("2.3.llegeix", { de_n: deN(n), k })]);
    } else {
      paraules = [txt("2.3.no_fa", { quadrets: qu(n) }),
                  txt("2.3.petit", { de_k: deN(k), k, quadrets: qu(q1) }),
                  txt("2.3.gran", { de_k: deN(k2), k: k2, quadrets: qu(q2) }),
                  txt("2.3.entre", { n, q1, q2 })];
      $("#q3-lectura").innerHTML = lectura(paraules) +
        lectura([txt("2.3.arrel", { de_n: deN(n), k, k2 })], k + " < √" + n + " < " + k2);
    }
    svg.setAttribute("aria-label", sobren
      ? txtPla("2.3.no_fa", { quadrets: qu(n) }) + " " + txtPla("2.3.arrel", { de_n: deN(n), k, k2 })
      : txtPla("2.3.exacte", { quadrets: qu(n), de_k: deN(k), k }));
    $("#q3-marca").hidden = n !== EX23;
  }

  let fet23 = false;
  function inicia23() {
    if (fet23) return;
    fet23 = true;
    q3Comptador = CE.comptador($("#q3-quants"), { et: txt("2.3.et"), min: 1, max: 100, valor: q3,
      aoCanviar: v => { q3 = v; pinta23(); } });
    pinta23();
  }

  /* ================================ 2.4 · Entre quins dos nombres? ====== */

  const NS24 = [10, 13, 20, 30, 40, 50, 70, 90];
  const N24 = 5;
  let t4 = null, n4 = 0, i4 = 0, opcions4 = [];

  /** La bona (4 i 5 per a √20); la meitat (10 i 11), la regla trencada; i passar-se
      d'un (5 i 6). */
  function opcionsDe24(n) {
    const k = Math.floor(Math.sqrt(n)), m = Math.floor(n / 2);
    return [["bona", k, k + 1], ["meitat", m, m + 1], ["dalt", k + 1, k + 2]];
  }
  function pas24(i, e) {
    n4 = e.extra.ns[i]; i4 = 0;
    $("#q4-pregunta").textContent = txtPla("2.4.pregunta", { n: n4 });
    opcions4 = e.extra.torns[i].map(k => opcionsDe24(n4)[k]);
    const cont = $("#q4-opcions");
    cont.innerHTML = opcions4.map((o, k) => '<button type="button" class="btn opcio-sino opcio-arrel" data-k="' + k + '">' +
      txt("2.4.opcio", { a: o[1], b: o[2] }) + "</button>").join("");
    $$(".opcio-arrel", cont).forEach(b => { b.onclick = () => tria24(Number(b.dataset.k), b); });
    dibuixaCostat($("#q4-svg"), n4);
    const k = Math.floor(Math.sqrt(n4));
    $("#q4-svg").setAttribute("aria-label", txtPla("2.3.no_fa", { quadrets: qu(n4) }) + " " +
                                           txtPla("2.3.arrel", { de_n: deN(n4), k, k2: k + 1 }));
    $("#q4-svg").toggleAttribute("hidden", !t4.resolt());
    const avis = $("#q4-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t4.resolt() ? txt("comu.ja_fet") : txt("2.4.comenca", { n: n4 });
    $("#q4-seguent").disabled = !t4.resolt();
    $("#q4-seguent").innerHTML = txt(t4.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t4.resolt()) marca24();
  }
  function marca24() {
    $$(".opcio-arrel", $("#q4-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", opcions4[b.dataset.k][0] === "bona"); });
    // El dibuix de la 2.3, només quan ja s'ha contestat: si no, la resposta es veuria.
    $("#q4-svg").toggleAttribute("hidden", false);
  }
  function tria24(kk, boto) {
    const e = t4.estat();
    if (!e || e.acabada || t4.resolt()) return;
    const o = opcions4[kk], avis = $("#q4-avis"), k = Math.floor(Math.sqrt(n4));
    const frase = txt("2.3.entre", { n: n4, q1: k * k, q2: (k + 1) * (k + 1) }) + " " +
                  txt("2.3.arrel", { de_n: deN(n4), k, k2: k + 1 });
    if (o[0] === "bona") { t4.anota(i4 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca24(); }
    else if (i4 === 0) {
      i4 = 1; boto.classList.add("mal"); boto.disabled = true;
      const cos = o[0] === "meitat" ? txt("2.4.error_meitat", { n: n4 })
                                    : txt("2.4.error_dalt", { k: k + 1, q: (k + 1) * (k + 1), n: n4 });
      retroaccio(avis, "error", cos, txt("2.4.pista", { n: n4 }));
    } else { t4.anota("mostrat"); retroaccio(avis, "mostra", frase); marca24(); }
    $("#q4-seguent").disabled = !t4.resolt();
  }
  let fet24 = false;
  function inicia24() {
    if (fet24) return;
    fet24 = true;
    t4 = CE.tasca({
      tasca: 2, sub: 4,
      recorregut: $("#q4-recorregut"), represa: $("#q4-represa"), final: $("#q4-final"), cos: [$("#q4-cos")],
      desa: true,
      valida: e => e.total === N24 && e.extra && Array.isArray(e.extra.ns) && e.extra.ns.length === N24 &&
                   e.extra.ns.every(n => NS24.includes(n)) && Array.isArray(e.extra.torns),
      nom: () => "2.4 · " + txtPla("2.4.nom"),
      pinta: pas24
    });
    $("#q4-seguent").onclick = () => t4.seguent();
    t4.inicia(() => {
      const ns = CE.barreja(NS24).slice(0, N24);
      return { total: N24, extra: { ns, torns: ns.map(() => CE.barreja([0, 1, 2])) } };
    });
  }

  /* ==================================================== arrencada ====== */

  const ARRENCA = { 1: inicia21, 2: inicia22, 3: inicia23, 4: inicia24 };
  let subs = null, subActual = null;

  function inicia() {
    const arrel = $("#mod-quadrat");
    if (!subs) {
      omplirTextos(arrel);
      subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); });
    }
    subs.mostra(subActual || CE.subDemanada(2) || 1);
  }

  CE.registra("quadrat", inicia);
  CE.registraCataleg("2.2", { nom: txtPla("2.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")],
    resta: txtPla("comu.r_mostrat") });
  CE.registraCataleg("2.4", { nom: txtPla("2.4.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")],
    resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { quadrat: { EX21, NS, EX23, NS24, opcionsDe24 } });
})();
