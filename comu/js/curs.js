/* ============================================================================
   comu/js/curs.js · the page of one course (CURS/index.html)
   ----------------------------------------------------------------------------
   The header (Inici › course), the course name and its units. It is the page the
   course link of every header leads to (decision 13 of the mockup review).
   The page loads ../comu/js/cursos.js, ../comu/js/web.js and dades/unitats.js first.
   ========================================================================== */

(function () {
  "use strict";
  const PI = window.PI;

  function arrenca() {
    const web = document.getElementById("w-web");
    const curs = PI.curs(PI.lloc().curs);
    document.title = curs.nom;
    web.innerHTML = PI.capcalera([["Inici", "../index.html"], [curs.nom, ""]], { professorat: "professorat.html" }) +
      '<h1 class="w-titol">' + PI.esc(curs.nom) + '</h1><section class="w-curs" style="max-width:40rem">' +
      '<ol class="w-unitats">' + (window.UNITATS || []).map(u => '<li><a class="w-b w-nav" href="u' + u.num +
        '/index.html"><span class="w-num">' + u.num + "</span>" + PI.esc(u.titol) + "</a></li>").join("") +
      "</ol></section>";
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();
})();
