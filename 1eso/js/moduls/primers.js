/* ============================================================================
   PRIMERS — mòdul «primers» de la caixa d'eines · tasca 8 · unitat 2
   ----------------------------------------------------------------------------
   Un nombre primer només fa un rectangle: una fila (1 · 7). Un nombre compost
   en fa més d'un. És l'activitat 2_7 del grup: el garbell d'Eratòstenes fins
   al 100, i primer o compost.

   8.1 · EL GARBELL D'ERATÒSTENES
     La graella de 100, pas a pas, com al grup: es ratlla l'1; s'encercla el 2 i
     es ratllen els seus múltiples; després el 3, el 5 i el 7. Els que queden
     són primers: 25. S'obre acabat (és l'exemple), i es pot tornar a fer pas a
     pas. No cal passar del 7: el primer múltiple de l'11 que no està ratllat
     seria l'11 · 11, i ja passa del 100.

   8.2 · ÉS PRIMER?
     Una tasca tancada de cinc passos: dos primers i tres senars que no ho són.
     És la regla trencada de la unitat: «tots els senars són primers». El 9 fa
     un quadrat de 3 per 3, i el dibuix ho ensenya. Tots els compostos es poden
     trobar a la targeta (3 · 3, 3 · 5, 7 · 7…): per això no hi ha el 33 ni el
     39, que no hi són.
   ========================================================================== */

(function () {
  "use strict";
  const { $, txt, txtPla, omplirTextos, retroaccio, quants, elNombre, lectura } = CE;
  const Q = CE.q;
  const majuscula = t => t.charAt(0).toUpperCase() + t.slice(1);

  /* ============================== 8.1 · El garbell d'Eratòstenes ====== */

  const GARBELL = [2, 3, 5, 7];
  const PASSOS = GARBELL.length + 2;                 // 0 tots, 1 l'1, 2-5 els primers, 6 el final
  let pas81 = PASSOS;

  /** Com va cada nombre al pas p. */
  function estat81(p) {
    const ratllats = new Set(), primers = new Set(), nous = [];
    if (p >= 1) ratllats.add(1);
    GARBELL.forEach((q, i) => {
      if (p < i + 2) return;
      primers.add(q);
      for (let m = 2 * q; m <= 100; m += q) {
        if (!ratllats.has(m) && i + 2 === p) nous.push(m);
        ratllats.add(m);
      }
    });
    if (p >= PASSOS) for (let n = 2; n <= 100; n++) if (!ratllats.has(n)) primers.add(n);
    return { ratllats, primers, nous };
  }

  function pinta81() {
    const p = Math.min(pas81, PASSOS), svg = $("#g8-svg"), e = estat81(p);
    Q.graella100(svg, n => (e.primers.has(n) ? "primer" : e.ratllats.has(n) ? "ratllat" : null));
    let frase;
    if (p === 0) frase = txt("8.1.p0");
    else if (p === 1) frase = txt("8.1.p1");
    else if (p < PASSOS) {
      const q = GARBELL[p - 2];
      frase = txt(p === 2 ? "8.1.p_primer" : "8.1.p_seguent",
                  { el_q: elNombre(q), llista: e.nous.slice(0, 3).join(", ") + (e.nous.length > 3 ? "…" : "") });
    } else frase = txt("8.1.final", { n: e.primers.size });
    $("#g8-lectura").innerHTML = lectura([txt("comu.pas", { n: p, total: PASSOS }), frase]);
    svg.setAttribute("aria-label", txtPla("8.1.aria", { primers: [...e.primers].sort((a, b) => a - b).join(", ") || "cap" }));
    $("#g8-enrere").disabled = p === 0;
    $("#g8-avant").disabled = p === PASSOS;
    $("#g8-marca").hidden = p !== PASSOS;
  }

  let fet81 = false;
  function inicia81() {
    if (fet81) return;
    fet81 = true;
    $("#g8-enrere").onclick = () => { pas81 = Math.max(0, pas81 - 1); pinta81(); };
    $("#g8-avant").onclick = () => { pas81 = Math.min(PASSOS, pas81 + 1); pinta81(); };
    $("#g8-comenca").onclick = () => { pas81 = 0; pinta81(); };
    pinta81();
  }

  /* ============================================== 8.2 · És primer? ====== */

  const PRIMERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47];
  // Senars que no són primers, i que es troben a la targeta: 3 · 3, 3 · 5…
  const SENARS = [9, 15, 21, 25, 27, 35, 45, 49];
  const N82 = 5;
  let t82 = null, n82 = 0, i82 = 0, triat82 = null;

  /** «El 9 fa 2 rectangles: 1 · 9 i 3 · 3. No és primer.» */
  function explica82(n) {
    const rs = Q.rectanglesDe(n), el = majuscula(elNombre(n));
    const ll = rs.map(r => r[0] + " · " + r[1]);
    const text = ll.length === 1 ? ll[0] : ll.slice(0, -1).join(", ") + " " + txtPla("comu.i") + " " + ll[ll.length - 1];
    return rs.length === 1 ? txt("8.2.es", { el_n: el, r: text })
                           : txt("8.2.no_es", { el_n: el, rectangles: quants(rs.length, "7.1.rectangle", "7.1.rectangles"), r: text });
  }

  function mostraDibuix82() {
    const svg = $("#p8-svg");
    Q.dibuixaRectangles(svg, n82);
    svg.setAttribute("aria-label", explica82(n82).replace(/<[^>]+>/g, ""));
    svg.removeAttribute("hidden");
  }

  function pas82(i, e) {
    n82 = e.extra.nombres[i];
    i82 = 0; triat82 = null;
    $("#p8-pregunta").textContent = txtPla("8.2.pregunta", { n: n82 });
    CE.botonsSiNo($("#p8-opcions"), tria82);
    if (t82.resolt()) mostraDibuix82(); else $("#p8-svg").setAttribute("hidden", "");
    const avis = $("#p8-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t82.resolt() ? txt("comu.ja_fet") : txt("8.2.comenca");
    const seg = $("#p8-seguent");
    seg.disabled = !t82.resolt();
    seg.innerHTML = txt(t82.esUltim() ? "comu.acaba" : "comu.seguent");
    CE.pintaSiNo($("#p8-opcions"), null, PRIMERS.includes(n82), t82.resolt());
  }

  function tria82(si) {
    const e = t82.estat();
    if (!e || e.acabada || t82.resolt()) return;
    const bo = PRIMERS.includes(n82), avis = $("#p8-avis");
    triat82 = si;
    if (si === bo) {
      t82.anota(i82 === 0 ? "be" : "pista");
      retroaccio(avis, "encert", explica82(n82));
      mostraDibuix82();
    } else if (i82 === 0) {
      i82 = 1;
      retroaccio(avis, "error", txt(si ? "8.2.has_dit_si" : "8.2.has_dit_no"), txt("8.2.pista", { n: n82 }));
    } else {
      t82.anota("mostrat");
      retroaccio(avis, "mostra", explica82(n82));
      mostraDibuix82();
    }
    CE.pintaSiNo($("#p8-opcions"), triat82, bo, t82.resolt());
    $("#p8-seguent").disabled = !t82.resolt();
  }

  /** Dos primers i tres senars que no ho són, barrejats. */
  const nousNombres82 = () => CE.barreja(CE.barreja(PRIMERS).slice(0, 2).concat(CE.barreja(SENARS).slice(0, 3)));

  let fet82 = false;
  function inicia82() {
    if (fet82) return;
    fet82 = true;
    t82 = CE.tasca({
      tasca: 8, sub: 2,
      recorregut: $("#p8-recorregut"), represa: $("#p8-represa"), final: $("#p8-final"), cos: [$("#p8-cos")],
      desa: true,
      valida: e => e.total === N82 && e.extra && Array.isArray(e.extra.nombres) && e.extra.nombres.length === N82 &&
                   e.extra.nombres.every(n => PRIMERS.includes(n) || SENARS.includes(n)),
      nom: () => "8.2 · " + txtPla("8.2.nom"),
      pinta: pas82
    });
    $("#p8-seguent").onclick = () => t82.seguent();
    t82.inicia(() => ({ total: N82, extra: { nombres: nousNombres82() } }));
  }

  /* ==================================================== arrencada ====== */

  const ARRENCA = { 1: inicia81, 2: inicia82 };
  let subs = null, subActual = null;

  function inicia() {
    const arrel = $("#mod-primers");
    if (!subs) {
      omplirTextos(arrel);
      subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); });
    }
    subs.mostra(subActual || CE.subDemanada(8) || 1);
  }

  CE.registra("primers", inicia);
  CE.registraCataleg("8.2", { nom: txtPla("8.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")],
    resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { primers: { PRIMERS, SENARS, GARBELL } });
})();
