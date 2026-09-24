/* ============================================================================
   RECTANGLES — mòdul «rect» de la caixa d'eines · tasca 1
   ----------------------------------------------------------------------------
   El nucli de la unitat 1: multiplicar és fer un rectangle de quadrets.
   3 · 4 són 3 files de 4 quadrets. El primer número diu quantes files hi ha;
   el segon, quants quadrets té cada fila.

   1.1 · FES UN RECTANGLE
     La taula de quadrets. Es toca un quadret i el rectangle arriba fins allà;
     també es pot fer amb els comptadors i amb les fletxes. Sota del dibuix,
     primer les paraules i al final el símbol. S'obre amb 3 · 4. Amb 0 files
     no hi ha cap quadret: 0 · 4 = 0 es veu, no s'explica.

   1.2 · EL RECTANGLE D'UNA MULTIPLICACIÓ
     Una tasca tancada de cinc multiplicacions. Es toca el quadret on acaba el
     rectangle: tocar és contestar.
       · el rectangle bo, o el girat (5 files de 2 per 2 · 5) → «Correcte.»
         El girat també té els mateixos quadrets: al món de debò, amb
         miniblocs, un rectangle no té un costat de dalt;
       · primer error → diu què ha fet i la pista marca els dos números de la
         vora que s'han de mirar: compta files cap avall i quadrets cap a la
         dreta, que és un camí diferent de «fes el rectangle»;
       · segon error  → la caixa dibuixa el rectangle bo.

   1.3 · GIRA EL RECTANGLE (la propietat commutativa)
     El rectangle gira de debò, 90 graus, i els quadrets no canvien. La
     igualtat 3 · 4 = 4 · 3 només surt després de girar-lo: el símbol surt del
     dibuix (regla 5), no s'anuncia.

   1.4 · PARTEIX EL RECTANGLE (la propietat distributiva)
     3 · 12 no és a la targeta. Partit pel 10, són dues multiplicacions que sí
     que hi són: 3 · 10 = 30 i 3 · 2 = 6. Les dues sumes es fan sense portar-ne
     (regla D), i per això els casos són aquests i no uns altres.
   ========================================================================== */

(function () {
  "use strict";
  const { $, $$, el, txt, txtPla, omplirTextos, retroaccio, quants, rect, lectura } = CE;
  const Q = CE.q;
  const qu = n => quants(n, "comu.quadret", "comu.quadrets");

  /* ========================================== 1.1 · Fes un rectangle ====== */

  const EX11 = { f: 3, c: 4 };
  let r1 = Object.assign({}, EX11), r1Files = null, r1Cols = null;

  function pinta11() {
    const { f, c } = r1, svg = $("#r1-svg");
    Q.taula(svg, { f, c });
    r1Files.posa(f);
    r1Cols.posa(c);
    $("#r1-marca").hidden = !(f === EX11.f && c === EX11.c);
    const lect = $("#r1-lectura");
    if (!f && !c) {
      lect.innerHTML = lectura([txt("1.1.buit")]);
      svg.setAttribute("aria-label", txtPla("1.1.buit"));
      return;
    }
    lect.innerHTML = lectura([txt("1.1.files", { rect: rect(f, c) }), txt("1.1.total", { quadrets: qu(f * c) })],
                             f + " · " + c + " = " + f * c);
    svg.setAttribute("aria-label", txtPla("1.1.files", { rect: rect(f, c) }) + " " +
                                   txtPla("1.1.total", { quadrets: qu(f * c) }));
  }

  let fet11 = false;
  function inicia11() {
    if (fet11) return;
    fet11 = true;
    r1Files = CE.comptador($("#r1-files"), { et: txt("1.1.et_files"), min: 0, max: 10, valor: r1.f,
      aoCanviar: v => { r1.f = v; pinta11(); } });
    r1Cols = CE.comptador($("#r1-cols"), { et: txt("1.1.et_cols"), min: 0, max: 10, valor: r1.c,
      aoCanviar: v => { r1.c = v; pinta11(); } });
    const svg = $("#r1-svg");
    svg.addEventListener("click", ev => {
      const p = Q.cellaTocada(svg, ev);
      if (p) { r1 = p; pinta11(); }
    });
    svg.addEventListener("keydown", ev => {
      const p = Q.fletxa(ev.key, r1);
      if (!p) return;
      ev.preventDefault();
      r1 = p;
      pinta11();
    });
    $("#r1-buida").onclick = () => { r1 = { f: 0, c: 0 }; pinta11(); };
    pinta11();
  }

  /* ============================ 1.2 · El rectangle d'una multiplicació ====== */

  const PER_FER = [[2, 5], [3, 6], [4, 4], [5, 3], [2, 7], [6, 2], [3, 3], [4, 5], [2, 8], [3, 7]];
  const N12 = 5;
  let fer = null, fAra = null, fIntents = 0, fTocat = null, fCursor = null;

  function pinta12() {
    const e = fer.estat(), res = e.res[e.pas], [a, b] = fAra;
    const o = {};
    if (res === "mostrat") Object.assign(o, { f: a, c: b });
    else if (fTocat) Object.assign(o, { f: fTocat.f, c: fTocat.c, classe: res ? "q" : "q mal" });
    if (fIntents >= 1 && res == null) o.pista = { f: a, c: b };
    if (fCursor && res == null) o.cursor = fCursor;
    Q.taula($("#r2-svg"), o);
  }

  function toca12(p) {
    const e = fer.estat();
    if (!e || e.acabada || fer.resolt()) return;
    fTocat = p;
    fCursor = null;
    const [a, b] = fAra, avis = $("#r2-avis");
    const dades = { rect: rect(p.f, p.c), quadrets: qu(a * b), a, b, p: a * b };
    const recte = p.f === a && p.c === b, girat = p.f === b && p.c === a;
    if (recte || girat) {
      fer.anota(fIntents === 0 ? "be" : "pista");
      retroaccio(avis, "encert", txt(recte ? "1.2.encert" : "1.2.encert_girat", dades));
    } else if (fIntents === 0) {
      fIntents = 1;
      retroaccio(avis, "error", txt("1.2.fet", dades), txt("1.2.pista", { a, b }));
    } else {
      fer.anota("mostrat");
      retroaccio(avis, "mostra", txt("1.2.mostra", { rect: rect(a, b), a, b, p: a * b }));
    }
    $("#r2-seguent").disabled = !fer.resolt();
    pinta12();
  }

  function pas12(i, e) {
    fAra = PER_FER[e.extra.ordre[i]];
    fIntents = 0; fTocat = null; fCursor = null;
    $("#r2-pregunta").textContent = txtPla("1.2.pregunta", { a: fAra[0], b: fAra[1] });
    const avis = $("#r2-avis");
    avis.className = "avis neutre";
    avis.innerHTML = fer.resolt() ? txt("comu.ja_fet") : txt("1.2.comenca");
    const seguent = $("#r2-seguent");
    seguent.disabled = !fer.resolt();
    seguent.innerHTML = txt(fer.esUltim() ? "comu.acaba" : "comu.seguent");
    pinta12();
  }

  let fet12 = false;
  function inicia12() {
    if (fet12) return;
    fet12 = true;
    fer = CE.tasca({
      tasca: 1, sub: 2,
      recorregut: $("#r2-recorregut"),
      represa: $("#r2-represa"),
      final: $("#r2-final"),
      cos: [$("#r2-cos")],
      desa: true,
      valida: e => e.total === N12 && e.extra && Array.isArray(e.extra.ordre) &&
                   e.extra.ordre.length === N12 && e.extra.ordre.every(i => PER_FER[i] !== undefined),
      nom: () => "1.2 · " + txtPla("1.2.nom"),
      pinta: pas12
    });
    $("#r2-seguent").onclick = () => fer.seguent();
    const svg = $("#r2-svg");
    svg.addEventListener("click", ev => { const p = Q.cellaTocada(svg, ev); if (p) toca12(p); });
    svg.addEventListener("keydown", ev => {
      if (fer.resolt()) return;
      if (ev.key === "Enter" || ev.key === " ") {
        ev.preventDefault();
        if (fCursor) toca12(fCursor);
        else { fCursor = { f: 1, c: 1 }; pinta12(); }
        return;
      }
      const p = Q.fletxa(ev.key, fCursor);
      if (!p) return;
      ev.preventDefault();
      fCursor = p;
      pinta12();
    });
    svg.addEventListener("blur", () => { if (fCursor) { fCursor = null; pinta12(); } });
    fer.inicia(() => ({ total: N12, extra: { ordre: CE.barreja(PER_FER.map((_, i) => i)).slice(0, N12) } }));
  }

  /* ======================================== 1.3 · Gira el rectangle ====== */

  const GIRA = [{ a: 3, b: 4 }, { a: 2, b: 5 }, { a: 4, b: 6 }, { a: 3, b: 7 }];
  GIRA.forEach(g => { g.et = g.a + " · " + g.b; });
  // viewBox 0 0 370 320: hi cap el de 7 quadrets girat, amb els rètols
  const M3 = 36, CX3 = 222, CY3 = 178;
  let gCas = GIRA[0], girat = false, girant = false;

  function pinta13() {
    const svg = $("#r3-svg");
    svg.textContent = "";
    const { a, b } = gCas, files = girat ? b : a, cols = girat ? a : b;
    const w = cols * M3, h = files * M3, x = CX3 - w / 2, y = CY3 - h / 2;
    const g = svg.appendChild(el("g", { class: "gira" }));
    Q.rectangle(g, x, y, files, cols, M3, "q");
    Q.clau(svg, x, y - 14, x + w, y - 14, qu(cols), "dalt");
    Q.clau(svg, x - 14, y, x - 14, y + h, quants(files, "comu.fila", "comu.files"), "esquerra");
    svg.setAttribute("aria-label", txtPla("1.3.files", { rect: rect(files, cols) }) + " " +
                                   txtPla("1.3.total", { quadrets: qu(a * b) }));
    const paraules = [txt("1.3.files", { rect: rect(files, cols) }), txt("1.3.total", { quadrets: qu(a * b) })];
    const simbols = [files + " · " + cols + " = " + a * b];
    if (girat) {
      paraules.push(txt("1.3.iguals"));
      simbols.push(a + " · " + b + " = " + b + " · " + a);
    }
    $("#r3-lectura").innerHTML = lectura(paraules, simbols);
    $("#r3-gira").innerHTML = txt(girat ? "1.3.torna" : "1.3.gira");
    $("#r3-marca").hidden = gCas !== GIRA[0];
  }

  function gira() {
    if (girant) return;
    const acaba = () => { girant = false; girat = !girat; pinta13(); };
    const g = $("#r3-svg .gira");
    if (CE.quiet() || !g) { acaba(); return; }
    girant = true;
    $$("#r3-svg .q-clau").forEach(x => x.remove());      // els rètols, fora mentre gira
    g.classList.add("girant");
    setTimeout(acaba, 750);
  }

  let fet13 = false;
  function inicia13() {
    if (fet13) return;
    fet13 = true;
    CE.pastilles($("#r3-pastilles"), GIRA, c => { gCas = c; girat = false; pinta13(); });
    $("#r3-gira").onclick = gira;
    pinta13();
  }

  /* ===================================== 1.4 · Parteix el rectangle ====== */

  const PARTEIX = [{ a: 3, n: 12 }, { a: 4, n: 13 }, { a: 7, n: 12 }, { a: 5, n: 11 }, { a: 2, n: 14 }];
  PARTEIX.forEach(p => { p.et = p.a + " · " + p.n; });
  const M4 = 26, X4 = 96, Y4 = 58, AIRE4 = 18;
  let pCas = PARTEIX[0], partit = false;

  function pinta14() {
    const svg = $("#r4-svg");
    svg.textContent = "";
    const { a, n } = pCas, u = n - 10;
    // a la dreta hi ha d'haver lloc per al rètol de la part petita, «5 · 1 = 5»
    const amp = X4 + n * M4 + AIRE4 + 72, alt = Y4 + a * M4 + 64;
    svg.setAttribute("viewBox", "0 0 " + amp + " " + alt);
    svg.classList.toggle("partit", partit);
    const g1 = svg.appendChild(el("g"));
    const g2 = svg.appendChild(el("g", { class: "tros" }));
    Q.rectangle(g1, X4, Y4, a, 10, M4, "q");
    Q.rectangle(g2, X4 + 10 * M4, Y4, a, u, M4, "q");   // es torna taronja en partir-lo (CSS)
    // el tall: una línia discontínua després de la columna 10
    svg.appendChild(el("line", { x1: X4 + 10 * M4, y1: Y4 - 6, x2: X4 + 10 * M4, y2: Y4 + a * M4 + 6,
                                 class: "q-tall nomes-sencer" }));
    Q.clau(svg, X4 - 12, Y4, X4 - 12, Y4 + a * M4, quants(a, "comu.fila", "comu.files"), "esquerra");
    // a dalt: sencer, «12 quadrets»; partit, «10» i «2»
    Q.clau(svg, X4, Y4 - 12, X4 + n * M4, Y4 - 12, qu(n), "dalt", "nomes-sencer");
    Q.clau(svg, X4, Y4 - 12, X4 + 10 * M4, Y4 - 12, qu(10), "dalt", "nomes-partit");
    Q.clau(svg, X4 + 10 * M4 + AIRE4, Y4 - 12, X4 + n * M4 + AIRE4, Y4 - 12, qu(u), "dalt", "nomes-partit");
    // a sota, quan està partit, les dues multiplicacions de la targeta
    const baix = Y4 + a * M4 + 30;
    Q.text(svg, X4 + 5 * M4, baix, a + " · 10 = " + a * 10, "q-text fort nomes-partit", 19);
    Q.text(svg, X4 + 10 * M4 + AIRE4 + u * M4 / 2, baix, a + " · " + u + " = " + a * u,
           "q-text fort nomes-partit", 19);
    lectura14();
  }

  function lectura14() {
    const { a, n } = pCas, u = n - 10, p1 = a * 10, p2 = a * u, p = a * n;
    const lect = $("#r4-lectura");
    if (!partit) {
      lect.innerHTML = lectura([txt("1.4.abans", { rect: rect(a, n) }), txt("1.4.fora", { n })]);
    } else {
      lect.innerHTML = lectura(
        [txt("1.4.dues"), txt("1.4.suma", { p1, p2, p }), txt("1.4.total", { quadrets: qu(p) })],
        [a + " · " + n + " = " + a + " · 10 + " + a + " · " + u, a + " · " + n + " = " + p]);
    }
    const svg = $("#r4-svg");
    svg.setAttribute("aria-label", partit
      ? txtPla("1.4.aria_partit", { a, u, p1, p2 })
      : txtPla("1.4.abans", { rect: rect(a, n) }));
    $("#r4-parteix").innerHTML = txt(partit ? "1.4.ajunta" : "1.4.parteix");
    $("#r4-marca").hidden = pCas !== PARTEIX[0];
  }

  function parteix() {
    partit = !partit;
    $("#r4-svg").classList.toggle("partit", partit);   // la transició la fa el CSS
    lectura14();
  }

  let fet14 = false;
  function inicia14() {
    if (fet14) return;
    fet14 = true;
    CE.pastilles($("#r4-pastilles"), PARTEIX, c => { pCas = c; partit = false; pinta14(); });
    $("#r4-parteix").onclick = parteix;
    pinta14();
  }

  /* ==================================================== arrencada ====== */

  const ARRENCA = { 1: inicia11, 2: inicia12, 3: inicia13, 4: inicia14 };
  let subs = null, subActual = null;

  function inicia() {
    const arrel = $("#mod-rect");
    if (!subs) {
      omplirTextos(arrel);
      subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); });
    }
    subs.mostra(subActual || CE.subDemanada(1) || 1);
  }

  CE.registra("rect", inicia);
  CE.registraCataleg("1.2", { nom: txtPla("1.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")],
    resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { rect: { EX11, PER_FER, GIRA, PARTEIX } });
})();
