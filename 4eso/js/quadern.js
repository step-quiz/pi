/* ============================================================================
   quadern.js · el filtre del quadern d'activitats (uN/quadern.html)
   ----------------------------------------------------------------------------
   Dues marques, a les activitats i al solucionari:
     data-n="1|2|3"  a cada apartat (i a cada secció amb un dibuix): a partir de quina
                     quantitat surt. Petita deixa l'a) i 3 apartats per fer, mitjana 6 i
                     alta 12. El nombre d'activitats no canvia.
     data-repte      a les activitats de repte (.act i .sol-act): només amb «Afegint
                     exercicis diferents que suposen un repte».
   Els apartats que s'amaguen sempre són els últims, i les lletres queden seguides. Els
   números de les activitats són comptadors CSS (css/quadern.css), que se salten les
   activitats amagades.

   L'estat es llegeix i s'escriu a l'adreça (?n=2&repte=1), perquè el docent pugui
   enviar l'enllaç amb el filtre posat. Sense JavaScript surt tot.
   ========================================================================== */

(function () {
  "use strict";
  const estat = { n: "2", repte: "0" };

  function llegeixAdreca() {
    try {
      const p = new URLSearchParams(location.search);
      if (/^[123]$/.test(p.get("n") || "")) estat.n = p.get("n");
      if (/^[01]$/.test(p.get("repte") || "")) estat.repte = p.get("repte");
    } catch (e) { /* sense adreça llegible: es queda el que hi ha per defecte */ }
  }

  function escriuAdreca() {
    try {
      const p = new URLSearchParams(location.search);
      p.set("n", estat.n);
      p.set("repte", estat.repte);
      history.replaceState(null, "", location.pathname + "?" + p.toString() + location.hash);
    } catch (e) { /* file:// en alguns navegadors: el filtre funciona igual */ }
  }

  function aplica() {
    const n = Number(estat.n), ambRepte = estat.repte === "1";
    document.querySelectorAll("[data-n]").forEach(el => { el.hidden = Number(el.dataset.n) > n; });
    document.querySelectorAll(".act[data-repte], .sol-act[data-repte]").forEach(el => { el.hidden = !ambRepte; });
    const vistes = document.querySelectorAll(".act:not([hidden])").length;
    const reptes = document.querySelectorAll(".act[data-repte]:not([hidden])").length;
    const primera = document.querySelector(".act");
    const perFer = primera ? primera.querySelectorAll(".ap:not([hidden])").length - 1 : 0;
    document.body.classList.toggle("amb-repte", ambRepte);
    document.querySelectorAll(".filtres [data-filtre]").forEach(grup => {
      grup.querySelectorAll("button").forEach(b => {
        b.setAttribute("aria-checked", String(b.dataset.valor === estat[grup.dataset.filtre]));
      });
    });
    const r = document.getElementById("recompte");
    if (r) r.textContent = vistes + " activitats" + (reptes ? " (" + reptes + " de repte)" : "") +
      " · " + perFer + " apartats a cada una";
  }

  function imprimeix(nomesSol) {
    document.body.classList.toggle("nomes-sol", nomesSol);
    window.print();
  }

  function arrenca() {
    llegeixAdreca();
    document.querySelectorAll(".filtres [data-filtre]").forEach(grup => {
      grup.addEventListener("click", ev => {
        const b = ev.target.closest("button");
        if (!b) return;
        estat[grup.dataset.filtre] = b.dataset.valor;
        aplica();
        escriuAdreca();
      });
    });
    const boto = id => document.getElementById(id);
    if (boto("imprimeix")) boto("imprimeix").addEventListener("click", () => imprimeix(false));
    if (boto("imprimeix-sol")) boto("imprimeix-sol").addEventListener("click", () => imprimeix(true));
    // Ctrl+P sense botó: les activitats, mai el solucionari.
    window.addEventListener("afterprint", () => document.body.classList.remove("nomes-sol"));
    aplica();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();
})();
