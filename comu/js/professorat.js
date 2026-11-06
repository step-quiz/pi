/* ============================================================================
   comu/js/professorat.js · the teacher page of a course (CURS/professorat.html)
   ----------------------------------------------------------------------------
   The content (the cards and the notes) is static HTML in each course's page,
   because it is different in every course. This script only adds what cannot be
   written there:
     · the header (Inici › course › Professorat), with no «Professorat» button;
     · the title «Professorat · <course>» (the course name lives only in cursos.js);
     · one sentence per line in every element marked data-w-frases.
   The two helper pages of the teacher (textos.html, verifica.html) use it too: their #w-cap
   says data-w-pagina="…", and the header becomes Inici › course › Professorat › that page.
   ========================================================================== */

(function () {
  "use strict";
  const PI = window.PI;

  function arrenca() {
    const curs = PI.curs(PI.lloc().curs);
    const cap = document.getElementById("w-cap");
    const pagina = cap && cap.dataset.wPagina;
    if (!pagina) document.title = "Professorat · " + curs.nom;
    const passos = [["Inici", "../index.html"], [curs.nom, "index.html"]].concat(
      pagina ? [["Professorat", "professorat.html"], [pagina, ""]] : [["Professorat", ""]]);
    if (cap) cap.outerHTML = PI.capcalera(passos, {});
    const titol = document.getElementById("w-titol");
    if (titol) titol.textContent = "Professorat · " + curs.nom;
    document.querySelectorAll("[data-w-frases]").forEach(el => { el.innerHTML = PI.frases(el.textContent.trim().replace(/\s+/g, " ")); });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();
})();
