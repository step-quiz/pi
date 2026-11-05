/* ============================================================================
   comu/js/torna.js · l'enllaç «← unitat N» de les targetes de consulta
   ----------------------------------------------------------------------------
   Una targeta de consulta pot ser de més d'una unitat (la calculadora és de totes).
   La pàgina de cada unitat l'obre amb ?ud=N (targetes/calculadora.html?ud=3), i aquí
   l'enllaç de dalt es corregeix perquè torni a la unitat d'on ve l'usuari. Sense ?ud,
   o sense JavaScript, es queda el que porta el HTML: la unitat on neix la targeta.
   L'esquema és curs → unitat → fitxa, quadern o caixa; vegeu comu/js/unitat.js.
   ========================================================================== */
(function () {
  "use strict";
  var ud = new URLSearchParams(location.search).get("ud");
  var a = document.querySelector(".navega a[data-unitat]");
  if (!a || !/^\d+$/.test(ud || "")) return;
  a.href = "../unitat.html?ud=" + ud;
  a.textContent = "← unitat " + ud;
})();
