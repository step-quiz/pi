/* ============================================================================
   app.js · navegació de la caixa d'eines
   ----------------------------------------------------------------------------
   L'única feina d'aquest fitxer és ensenyar una secció i amagar les altres.
   No sap res del que fa cada mòdul: només l'identificador, que llegeix de
   l'atribut data-mod dels botons. Afegir un mòdul no obliga a tocar-lo.

   ENLLAÇOS FILTRATS PER A L'ALUMNAT · caixa-eines?task=n
   Només es veuen dues pestanyes: la tasca 0 (la Calculadora), sempre la
   primera, i la tasca n. Els números són l'atribut data-tasca de cada botó.
     - Sense ?task es veu la caixa sencera, com sempre.
     - ?task=0, o un número que no existeix: només la tasca 0.
     - S'obre directament la tasca n.
     - No es llegeix ni s'escriu el mòdul desat: en un ordinador compartit,
       cada persona entraria on ho va deixar l'anterior.
     - S'amaga l'enllaç a l'inici, que és una pàgina per al docent.
   ========================================================================== */

(function () {
  "use strict";
  const { $, $$, moduls, memoria } = CE;

  const CLAU = "caixa-modul";      // últim mòdul obert, per recuperar-lo
  let permesos = null;             // null: totes les pestanyes; si no, els data-mod visibles

  function obre(id) {
    if (permesos && !permesos.includes(id)) return;
    $$(".modul").forEach(s => { s.hidden = true; });
    $$(".segment[data-mod]").forEach(p => p.setAttribute("aria-selected", String(p.dataset.mod === id)));

    const sec = $("#mod-" + id);
    if (!sec) return;
    sec.hidden = false;

    const inicia = moduls[id];
    if (inicia) inicia();
    else console.warn("CE: no hi ha cap mòdul registrat amb l'identificador «" + id + "»");

    if (!permesos) memoria.set(CLAU, id);
  }

  /** Llegeix ?task=n i amaga la resta de pestanyes. Retorna el mòdul que s'ha
      d'obrir, o null si l'adreça no porta filtre. */
  function aplicaFiltre(botons) {
    const valor = new URLSearchParams(location.search).get("task");
    if (valor === null) return null;

    const tasca = n => botons.find(b => b.dataset.tasca === n);
    const base = tasca("0");
    const triada = /^\d+$/.test(valor.trim()) ? tasca(String(Number(valor))) : undefined;
    if (!triada) console.warn("CE: ?task=" + valor + " no és cap tasca; només es mostra la tasca 0");

    const visibles = [...new Set([base, triada])].filter(Boolean);
    if (!visibles.length) return null;   // marcatge sense tasca 0: millor ensenyar-ho tot que res

    permesos = visibles.map(b => b.dataset.mod);
    botons.forEach(b => { b.hidden = !permesos.includes(b.dataset.mod); });
    const tornar = $(".tornar");
    if (tornar) tornar.hidden = true;
    return (triada || base).dataset.mod;
  }

  function arrenca() {
    const botons = $$(".segment[data-mod]");
    botons.forEach(p => { p.onclick = () => obre(p.dataset.mod); });

    let inicial = aplicaFiltre(botons);
    if (!inicial) {
      const desat = memoria.get(CLAU);
      inicial = (desat && moduls[desat]) ? desat : (botons[0] && botons[0].dataset.mod);
    }
    if (inicial) obre(inicial);
  }

  // Els mòduls s'han de poder registrar abans que això s'executi, i per això
  // app.js va l'últim de tots els <script> de la pàgina.
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();

  CE.obre = obre;                  // útil per provar-ho des de la consola
})();
