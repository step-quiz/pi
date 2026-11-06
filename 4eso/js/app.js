/* ============================================================================
   app.js · navegació de la caixa d'eines
   ----------------------------------------------------------------------------
   L'única feina d'aquest fitxer és ensenyar una secció i amagar les altres.
   No sap res del que fa cada mòdul: només l'identificador, que llegeix de
   l'atribut data-mod dels botons. Afegir un mòdul no obliga a tocar-lo.

   UNA SOLA EINA, PER A LES PROVES · eines.html?task=n
   Ja no s'enllaça enlloc (6/11/2026): l'alumnat entra amb eines.html?u=N (més avall).
   Només es veuen dues pestanyes: la tasca 0 (la Calculadora), sempre la
   primera, i la tasca n. Els números són l'atribut data-tasca de cada botó.
     - Sense ?task es veu la caixa sencera, com sempre.
     - ?task=0, o un número que no existeix: només la tasca 0.
     - ?task=1.2 obre la tasca 1 directament per la subtasca 2.
     - S'obre directament la tasca n.
     - No es llegeix ni s'escriu el mòdul desat: en un ordinador compartit,
       cada persona entraria on ho va deixar l'anterior.

   LES EINES D'UNA UNITAT · eines.html?u=N
   L'enllaç que el docent copia a la pàgina de la unitat i envia a l'alumnat. Només es
   veuen les eines de la unitat N, i la capçalera no porta cap enllaç. Vegeu aplicaUnitat().
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

    // «1» obre la tasca 1; «1.2» obre directament la subtasca 1.2, que és el que
    // permet enviar un exercici concret i no la tasca sencera.
    const parts = valor.trim().split(".");
    const bo = parts.length <= 2 && parts.every(x => /^\d+$/.test(x));
    CE.subDemanada = (bo && parts.length === 2) ? Number(parts[1]) : null;

    const tasca = n => botons.find(b => b.dataset.tasca === n);
    const base = tasca("0");
    const triada = bo ? tasca(String(Number(parts[0]))) : undefined;
    if (!triada) console.warn("CE: ?task=" + valor + " no és cap tasca; només es mostra la tasca 0");

    const visibles = [...new Set([base, triada])].filter(Boolean);
    if (!visibles.length) return null;   // marcatge sense tasca 0: millor ensenyar-ho tot que res

    permesos = visibles.map(b => b.dataset.mod);
    botons.forEach(b => { b.hidden = !permesos.includes(b.dataset.mod); });
    return (triada || base).dataset.mod;
  }

  /** eines.html?u=N: l'enllaç que el docent envia a l'alumnat (6/11/2026). ../comu/js/alumne.js
      ja ha llegit la unitat (PI.einesUnitat). Només es veuen les eines del camp tasques de
      dades/unitats.js, en aquest ordre, i s'obre la primera. Com amb ?task, no es desa res.
      MENYS LLOCS ON CLICAR (6/11/2026): les eines «de sempre» (data-comuna: Calculadora i Com ho
      dic) ja no surten totes soles; només on les posa tasques. I amb una sola eina no hi ha pestanyes. */
  function aplicaUnitat(botons) {
    const u = window.PI && window.PI.einesUnitat;
    if (!u) return null;
    const nums = (u.tasques || []).map(String);
    const visibles = nums.map(n => botons.find(b => b.dataset.tasca === n)).filter(Boolean);
    if (!visibles.length) return null;
    permesos = visibles.map(b => b.dataset.mod);
    botons.forEach(b => { b.hidden = !permesos.includes(b.dataset.mod); });
    const barra = visibles[0].parentElement;
    visibles.forEach(b => barra.appendChild(b));
    // Amb una sola eina, cap pestanya: no hi ha res a triar.
    barra.hidden = visibles.length === 1;
    return visibles[0].dataset.mod;
  }


  function arrenca() {
    const botons = $$(".segment[data-mod]");
    botons.forEach(p => { p.onclick = () => obre(p.dataset.mod); });

    let inicial = aplicaFiltre(botons) || aplicaUnitat(botons);
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
