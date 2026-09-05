/* ============================================================================
   app.js · navegació de la caixa d'eines
   ----------------------------------------------------------------------------
   L'única feina d'aquest fitxer és ensenyar una secció i amagar les altres.
   No sap res del que fa cada mòdul: només l'identificador, que llegeix de
   l'atribut data-mod dels botons. Afegir un mòdul no obliga a tocar-lo.
   ========================================================================== */

(function () {
  "use strict";
  const { $, $$, moduls, memoria } = CE;

  const CLAU = "caixa-modul";      // últim mòdul obert, per recuperar-lo

  function obre(id) {
    $$(".modul").forEach(s => { s.hidden = true; });
    $$(".segment[data-mod]").forEach(p => p.setAttribute("aria-selected", String(p.dataset.mod === id)));

    const sec = $("#mod-" + id);
    if (!sec) return;
    sec.hidden = false;

    const inicia = moduls[id];
    if (inicia) inicia();
    else console.warn("CE: no hi ha cap mòdul registrat amb l'identificador «" + id + "»");

    memoria.set(CLAU, id);
  }

  function arrenca() {
    const botons = $$(".segment[data-mod]");
    botons.forEach(p => { p.onclick = () => obre(p.dataset.mod); });

    const desat = memoria.get(CLAU);
    const inicial = (desat && moduls[desat]) ? desat : (botons[0] && botons[0].dataset.mod);
    if (inicial) obre(inicial);
  }

  // Els mòduls s'han de poder registrar abans que això s'executi, i per això
  // app.js va l'últim de tots els <script> de la pàgina.
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();

  CE.obre = obre;                  // útil per provar-ho des de la consola
})();
