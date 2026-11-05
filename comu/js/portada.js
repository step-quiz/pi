/* ============================================================================
   comu/js/portada.js · la portada del lloc (index.html de l'arrel)
   ----------------------------------------------------------------------------
   Una columna per curs, amb les seves unitats. Cada unitat porta a la pàgina de
   la unitat del seu curs (1eso/unitat.html?ud=N, 4eso/unitat.html?ud=N).

   Les dades són les de cada curs (1eso/dades/unitats.js i 4eso/dades/unitats.js).
   Totes dues es diuen window.UNITATS: index.html les carrega una darrere l'altra i
   en desa una còpia a cada columna (data-unitats="U_1ESO"…). El nom del curs és
   a index.html, l'única pàgina on pot sortir (vegeu ANONIMAT a 4eso/eines/comprova.py).
   ========================================================================== */

(function () {
  "use strict";

  function columna(col) {
    const unitats = window[col.dataset.unitats] || [];
    const llista = document.createElement("ol");
    llista.className = "unitats";
    unitats.forEach(u => {
      const li = document.createElement("li");
      li.innerHTML = '<a class="unitat" href="' + col.dataset.dir + "/unitat.html?ud=" + u.num + '">' +
        '<span class="num">' + u.num + "</span><span>" + u.titol + "</span></a>";
      llista.appendChild(li);
    });
    col.appendChild(llista);
  }

  function arrenca() {
    document.querySelectorAll(".curs[data-unitats]").forEach(columna);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();
})();
