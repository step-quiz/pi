/* ============================================================================
   comu/js/quadern.js · el filtre del quadern d'activitats (CURS/uN/quadern.html)
   ----------------------------------------------------------------------------
   Dues marques, a les activitats i al solucionari:
     data-n="1|2|3"  a cada apartat (i a cada secció amb un dibuix): a partir de quina
                     quantitat surt. Petita deixa l'a) i 3 apartats per fer, mitjana 6 i
                     alta 12. El nombre d'activitats no canvia.
     data-repte      a les activitats de repte (.act i .sol-act): només amb «Afegir-hi
                     reptes».
   Els apartats que s'amaguen sempre són els últims, i les lletres queden seguides. Els
   números de les activitats són comptadors CSS (comu/css/quadern.css), que se salten les
   activitats amagades.

   L'estat es llegeix i s'escriu a l'adreça (?n=2&repte=1), perquè el docent pugui
   enviar l'enllaç amb el filtre posat. Sense JavaScript surt tot.

   Els PDF (6/11/2026): els botons són els de totes les pàgines de paper, «PDF alumnat» i
   «PDF solucionari», però el quadern no té PDF fets d'abans, perquè depèn del filtre. Cada
   botó obre el diàleg d'imprimir amb el filtre posat (allà es tria «Desa com a PDF»), i
   mentrestant el títol de la pestanya, que és el nom que el navegador proposa per al
   fitxer, diu què és: «… · alumnat» o «… · solucionari». Comú a tots els cursos des del
   6/11/2026 (abans era 4eso/js/quadern.js).
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
    document.body.classList.toggle("amb-repte", ambRepte);
    document.querySelectorAll(".filtres [data-filtre]").forEach(grup => {
      grup.querySelectorAll("button").forEach(b => {
        b.setAttribute("aria-checked", String(b.dataset.valor === estat[grup.dataset.filtre]));
      });
    });
  }

  let titol = null;
  function pdf(nomesSol) {
    document.body.classList.toggle("nomes-sol", nomesSol);
    titol = document.title;
    document.title = titol + (nomesSol ? " · solucionari" : " · alumnat");
    window.print();
  }
  function despres() {
    document.body.classList.remove("nomes-sol");
    if (titol !== null) { document.title = titol; titol = null; }
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
    if (boto("pdf-alumnat")) boto("pdf-alumnat").addEventListener("click", () => pdf(false));
    if (boto("pdf-solucionari")) boto("pdf-solucionari").addEventListener("click", () => pdf(true));
    // Ctrl+P sense botó: les activitats, mai el solucionari.
    window.addEventListener("afterprint", despres);
    aplica();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();
})();
