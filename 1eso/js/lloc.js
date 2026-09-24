/* ============================================================================
   lloc.js · construeix la portada a partir de dades/unitats.js
   ----------------------------------------------------------------------------
   Dues graelles: les targetes de consulta i les set unitats. Una unitat sense
   fitxa encara surt a la graella, però no s'hi pot clicar. Si la unitat té
   tasques a la caixa d'eines, la targeta ho diu.
   ========================================================================== */

(function () {
  "use strict";

  /** Crea un node amb classe i contingut HTML ja compost. */
  function fes(etiqueta, classe, html) {
    const n = document.createElement(etiqueta);
    if (classe) n.className = classe;
    if (html != null) n.innerHTML = html;
    return n;
  }

  function graellaTargetes(cont) {
    TARGETES.forEach(function (t) {
      const d = fes("div", "targeta");
      d.innerHTML =
        "<h3>" + t.titol + "</h3>" +
        "<p>" + t.descripcio + "</p>" +
        '<p><a href="' + t.fitxer + '">Obre-la al navegador</a></p>' +
        '<div class="etiquetes"><a class="pdf" href="' + t.pdf + '" download>PDF per imprimir</a></div>';
      cont.appendChild(d);
    });
  }

  function graellaUnitats(cont) {
    UNITATS.forEach(function (u) {
      const d = fes(u.fitxa ? "a" : "div", "targeta");
      if (u.fitxa) d.href = u.fitxa;
      d.innerHTML =
        '<span class="num">' + u.num + "</span>" +
        "<h3>" + u.titol + "</h3>" +
        "<p>" + u.nucli + "</p>" +
        '<div class="etiquetes">' +
          '<span class="et">' + u.dates + "</span>" +
          (u.fitxa ? '<span class="et fita">Fitxa feta</span>'
                   : '<span class="et">En preparació</span>') +
          // Sense enllaç: quan hi ha fitxa, la targeta sencera ja és un enllaç.
          (u.tasques ? '<span class="et fita">Caixa d\'eines · tasques ' + u.tasques.join(", ") +
                       "</span>" : "") +
        "</div>";
      cont.appendChild(d);
    });
  }

  function arrenca() {
    if (typeof UNITATS === "undefined" || typeof TARGETES === "undefined") {
      console.error("lloc.js: falta dades/unitats.js");
      return;
    }
    const t = document.getElementById("graella-targetes");
    if (t) graellaTargetes(t);
    const u = document.getElementById("graella-unitats");
    if (u) graellaUnitats(u);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();
})();
