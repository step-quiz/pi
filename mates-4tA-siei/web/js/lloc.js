/* ============================================================================
   lloc.js · construeix els índexs a partir de dades/unitats.js
   ----------------------------------------------------------------------------
   Dues funcions, cadascuna busca el seu contenidor i no fa res si no hi és.
   Així el mateix fitxer serveix per a index.html i per a fitxes.html.
   ========================================================================== */

(function () {
  "use strict";
  const $ = s => document.querySelector(s);
  const nom = id => (window.MODULS && window.MODULS[id]) || id;

  /** Crea un node amb classe i contingut HTML ja compost. */
  function fes(etiqueta, classe, html) {
    const n = document.createElement(etiqueta);
    if (classe) n.className = classe;
    if (html != null) n.innerHTML = html;
    return n;
  }

  /* ---- index.html: una targeta per unitat ---- */
  function graellaUnitats(cont) {
    UNITATS.forEach(u => {
      const a = fes("a", "targeta");
      a.href = u.fitxa;
      a.innerHTML =
        '<span class="num">' + u.num + "</span>" +
        "<h3>" + u.titol + "</h3>" +
        "<p>" + u.objectiu + "</p>" +
        '<div class="etiquetes">' +
          '<span class="et">' + u.dates + "</span>" +
          '<span class="et fita">' + u.fita + "</span>" +
        "</div>";
      cont.appendChild(a);
    });
  }

  /* ---- fitxes.html: el detall complet de cada unitat ---- */
  function detallUnitats(cont) {
    UNITATS.forEach(u => {
      const d = fes("div", "detall");
      const moduls = u.moduls.length
        ? u.moduls.map(m => '<a href="caixa-eines.html">' + nom(m) + "</a>").join(", ")
        : "cap; l'eina d'aquesta unitat és el full de càlcul";
      d.innerHTML =
        '<h3 style="margin:0 0 .8rem"><span class="num" style="margin:0 .5rem 0 0">' + u.num +
          '</span>' + u.titol + "</h3>" +
        "<dl>" +
          "<dt>Fitxa</dt><dd><a href=\"" + u.fitxa + "\">obre-la</a> · " + u.dates +
            " · " + u.sessions + " sessions</dd>" +
          "<dt>Objectiu nuclear</dt><dd>" + u.objectiu + "</dd>" +
          "<dt>Cinc minuts abans</dt><dd>" + u.material + "</dd>" +
          "<dt>La regla trencada</dt><dd>" + u.trencada + "</dd>" +
          "<dt>Fita realista</dt><dd>" + u.fita + "</dd>" +
          "<dt>Caixa d'eines</dt><dd>" + moduls + "</dd>" +
          "<dt>Llibre digital</dt><dd><code>" + u.llibre + "</code></dd>" +
          "<dt>repas-main</dt><dd>" + u.repas +
            (u.evitar ? ' <span class="et avis">no obrir: ' + u.evitar + "</span>" : "") +
          "</dd>" +
        "</dl>";
      cont.appendChild(d);
    });
  }

  function arrenca() {
    if (typeof UNITATS === "undefined") {
      console.error("lloc.js: falta dades/unitats.js");
      return;
    }
    const g = $("#graella-unitats");   if (g) graellaUnitats(g);
    const d = $("#detall-unitats");    if (d) detallUnitats(d);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();
})();
