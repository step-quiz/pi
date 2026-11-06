/* ============================================================================
   comu/js/unitat.js · the page of one unit (CURS/uN/index.html)
   ----------------------------------------------------------------------------
   The page is for the teacher (decision F1: the students only open the tools).
   From top to bottom:

     header        Inici › course › Unitat N, and the «Professorat» button
     title         «Unitat N · title» (no date: decision 4 of the mockup review)
     the cards     one grid of three equal columns (decision of 6/11/2026: the eye follows one
                   rhythm). Numbered in order, with no icon in the heading:
                   1 Fitxa (or 1 Fitxes, numbered, when there are several: then it takes a whole row) ·
                   2 Quadern d'activitats (greyed out, «no disponible», when missing) ·
                   3 Repàs, each one with Obre, PDF alumnat, PDF solucionari ·
                   4 Eines: «Obre les eines» and «Copia l'enllaç» (CURS/eines.html?u=N) ·
                   5 Targetes: the reference cards of the unit, with their PDF.
                   A missing card (no Repàs, no tools, no card) is skipped and the numbers close up.
     Abans de la classe   a <details>, always folded when the page opens: material,
                   objective or core idea, broken rule

   The data are the course's dades/unitats.js, loaded before this script, with the
   same fields in every course (comu/docs/SITE-MAP.md, «Data model»).
   ========================================================================== */

(function () {
  "use strict";
  const PI = window.PI;

  /* A unit folder holds its own pages: "u3/fitxa.html" is opened as "fitxa.html". */
  const aqui = cami => String(cami).split("/").pop();

  function pdfs(cami) {
    const base = PI.pdfBase(cami);
    return PI.boto({ rol: "pdf", href: "../pdf/" + base + "-alumnat.pdf", descarrega: true, text: "PDF alumnat", icona: "pdf" }) +
           PI.boto({ rol: "pdf", href: "../pdf/" + base + "-solucionari.pdf", descarrega: true, text: "PDF solucionari", icona: "sol" });
  }

  /* The heading of a card: its number in the path and the title, no icon (decision of 6/11/2026).
     The numbers are given in order as the cards are written: see arrenca(). */
  let pas = 0;
  const cap = (icona, _, titol) => '<div class="w-carta-cap"><span class="w-pas">' + (++pas) + "</span><h2>" +
    PI.esc(titol) + "</h2></div>";

  function cartaFitxes(u) {
    const fs = u.fitxes || [];
    if (fs.length === 1) {
      return '<section class="w-carta w-mat">' + cap("fitxa", 1, "Fitxa") + '<div class="w-accions">' +
        PI.boto({ rol: "mat", href: aqui(fs[0].fitxa), text: "Obre la fitxa", icona: "fitxa", principal: true }) +
        pdfs(fs[0].fitxa) + "</div></section>";
    }
    return '<section class="w-carta w-mat w-tota">' + cap("fitxa", 1, "Fitxes") + '<ol class="w-fitxes-llista">' +
      fs.map((f, i) => '<li><div class="w-fn"><span>' + (i + 1) + "</span>" + PI.esc(f.titol) + '</div><div class="w-accions">' +
        PI.boto({ rol: "mat", href: aqui(f.fitxa), text: "Obre", icona: "fitxa", principal: true }) + pdfs(f.fitxa) +
        "</div></li>").join("") + "</ol></section>";
  }

  /* When a unit has no workbook, the card stays, greyed out (decision U3). */
  function cartaQuadern(u) {
    if (!u.quadern) {
      return '<section class="w-carta w-mat w-apagada">' + cap("quadern", 2, "Quadern d'activitats") +
        '<p class="w-nom">Quadern d\'activitats no disponible</p></section>';
    }
    return '<section class="w-carta w-mat">' + cap("quadern", 2, "Quadern d'activitats") + '<div class="w-accions">' +
      PI.boto({ rol: "mat", href: aqui(u.quadern), text: "Obre el quadern", icona: "quadern", principal: true }) + "</div></section>";
  }

  function cartaRepas(u) {
    if (!u.repas) return "";
    return '<section class="w-carta w-mat">' + cap("repas", 3, "Repàs") + '<div class="w-accions">' +
      PI.boto({ rol: "mat", href: aqui(u.repas.fitxa), text: "Obre el repàs", icona: "repas", principal: true }) +
      pdfs(u.repas.fitxa) + "</div></section>";
  }

  /* The address the teacher sends to the students. Published, without «.html». */
  function enllacAlumnat(u) {
    const url = new URL("../eines.html?u=" + u.num, location.href).href;
    return /^https?:/.test(url) ? url.replace(/\.html(?=\?|$)/, "") : url;
  }

  function cartaEines(u) {
    if (!(u.tasques || []).length) return "";
    return '<section class="w-carta w-eina">' + cap("eines", 0, "Eines") + '<div class="w-accions">' +
      PI.boto({ rol: "eina", href: "../eines.html?u=" + u.num, text: "Obre les eines", icona: "eines", principal: true }) +
      PI.boto({ rol: "eina", text: "Copia l'enllaç", icona: "enllac",
        atributs: ' title="L\'enllaç per a l\'alumnat" data-w-copia="' + PI.esc(enllacAlumnat(u)) + '"' }) +
      "</div></section>";
  }

  /* Only one card: no name (decision 6). Several: each with its name. */
  function cartaTargetes(u) {
    const ts = (window.TARGETES || []).filter(t => (t.unitats || []).includes(u.num));
    if (!ts.length) return "";
    return '<section class="w-carta w-mat">' + cap("targeta", 0, "Targetes") + ts.map(t =>
      (ts.length > 1 ? '<p class="w-nom">' + PI.esc(t.titol) + "</p>" : "") + '<div class="w-accions">' +
      PI.boto({ rol: "mat", href: "../targetes/" + t.nom + ".html?u=" + u.num, text: "Obre la targeta", icona: "targeta", principal: true }) +
      PI.boto({ rol: "pdf", href: "../pdf/targeta-" + t.nom + ".pdf", descarrega: true, text: "PDF", icona: "pdf" }) +
      "</div>").join("") + "</section>";
  }

  /* «una cinta mètrica» (the data are written to go inside a sentence) → «Una cinta mètrica.» */
  const frase = t => { t = String(t).trim(); t = t.charAt(0).toUpperCase() + t.slice(1); return /[.!?»]$/.test(t) ? t : t + "."; };

  function abans(u) {
    const files = [["Material", u.material], ["Objectiu", u.objectiu], ["La idea", u.nucli], ["La regla trencada", u.trencada]]
      .filter(f => f[1]);
    if (!files.length) return "";
    // Folded when the page opens, always (decision of 6/11/2026): no «open» attribute, and nothing remembered.
    return '<details class="w-abans"><summary><h2>Abans de la classe</h2></summary><dl>' +
      files.map(f => "<dt>" + f[0] + "</dt><dd>" + PI.frases(frase(f[1])) + "</dd>").join("") + "</dl></details>";
  }

  function arrenca() {
    const web = document.getElementById("w-web");
    const lloc = PI.lloc();
    const curs = PI.curs(lloc.curs);
    const u = PI.unitat(lloc.unitat);
    if (!u) {
      web.innerHTML = PI.capcalera([["Inici", "../../index.html"], [curs.nom, "../index.html"], ["Unitat", ""]], {}) +
        '<h1 class="w-titol">Aquesta unitat no existeix</h1>';
      return;
    }
    document.title = "Unitat " + u.num + " · " + u.titol;
    web.classList.add("w-u");   // the narrower column and the unit look, in web.css
    pas = 0;
    const cartes = cartaFitxes(u) + cartaQuadern(u) + cartaRepas(u) + cartaEines(u) + cartaTargetes(u);
    web.innerHTML =
      PI.capcalera([["Inici", "../../index.html"], [curs.nom, "../index.html"], ["Unitat " + u.num, ""]], { professorat: "../professorat.html" }) +
      '<h1 class="w-titol">Unitat ' + u.num + " · " + PI.esc(u.titol) + '</h1><div class="w-cartes">' + cartes + "</div>" + abans(u);

    web.addEventListener("click", ev => {
      const b = ev.target.closest("[data-w-copia]");
      if (b) PI.copia(b, b.dataset.wCopia);
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();
})();
