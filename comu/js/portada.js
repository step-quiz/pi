/* ============================================================================
   comu/js/portada.js · the home page (index.html at the repository root)
   ----------------------------------------------------------------------------
   «Curs 2026-27», the title, and one column per course of comu/js/cursos.js with
   its units (CURS/uN/index.html) and its «Professorat» button (CURS/professorat.html).
   No header bar here: this page is «Inici» (decision of 6/11/2026).

   Each course keeps its data in CURS/dades/unitats.js, and every one of those files
   is called window.UNITATS. They are loaded one after the other and copied.
   ========================================================================== */

(function () {
  "use strict";
  const PI = window.PI;

  function columna(c, unitats) {
    return '<section class="w-curs" aria-labelledby="h-' + c.id + '"><div class="w-curs-cap"><h2 id="h-' + c.id + '">' +
      PI.esc(c.nom) + "</h2>" +
      PI.boto({ rol: "nav", href: c.id + "/professorat.html", text: "Professorat", icona: "docent", classe: "w-prof" }) +
      '</div><ol class="w-unitats">' + unitats.map(u => '<li><a class="w-b w-nav" href="' + c.id + "/u" + u.num +
        '/index.html"><span class="w-num">' + u.num + "</span>" + PI.esc(u.titol) + "</a></li>").join("") +
      "</ol></section>";
  }

  function arrenca() {
    const web = document.getElementById("w-web");
    if (!web || new URLSearchParams(location.search).get("other-versions") === "1") return;
    const dades = {};
    const cursos = PI.CURSOS.slice();
    (function seguent(i) {
      if (i === cursos.length) {
        web.innerHTML = '<p class="w-curs-escolar">' + PI.cursEscolar(new Date()) + "</p>" +
          '<h1 class="w-titol">Material adaptat de matemàtiques</h1><div class="w-cursos">' +
          cursos.map(c => columna(c, dades[c.id] || [])).join("") + "</div>";
        return;
      }
      window.UNITATS = undefined;
      PI.carrega([cursos[i].id + "/dades/unitats.js"], () => {
        dades[cursos[i].id] = window.UNITATS || [];
        seguent(i + 1);
      });
    })(0);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();
})();
