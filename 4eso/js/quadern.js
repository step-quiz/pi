/* ============================================================================
   quadern.js · el filtre del quadern d'activitats (quadern/udN.html)
   ----------------------------------------------------------------------------
   Cada activitat (.act) i cada entrada del solucionari (.sol-act) porta:
     data-n="1|2|3"  a partir de quina quantitat surt (1 petit, 2 mitjà, 3 elevat)
     data-repte      si és de repte
   El filtre amaga les que no toquen. Els números no els posa aquest fitxer: són
   comptadors CSS (css/quadern.css), que se salten el que està amagat.

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
    let vistes = 0, reptes = 0;
    document.querySelectorAll(".act, .sol-act").forEach(el => {
      const surt = Number(el.dataset.n) <= n && (ambRepte || !el.hasAttribute("data-repte"));
      el.hidden = !surt;
      if (surt && el.classList.contains("act")) {
        vistes++;
        if (el.hasAttribute("data-repte")) reptes++;
      }
    });
    document.body.classList.toggle("amb-repte", ambRepte);
    document.querySelectorAll(".filtres [data-filtre]").forEach(grup => {
      grup.querySelectorAll("button").forEach(b => {
        b.setAttribute("aria-pressed", String(b.dataset.valor === estat[grup.dataset.filtre]));
      });
    });
    const r = document.getElementById("recompte");
    if (r) r.textContent = "Surten " + vistes + " activitats" +
      (reptes ? ", " + reptes + " de repte." : ".");
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
    const mostra = boto("mostra-sol");
    if (mostra) mostra.addEventListener("click", () => {
      const veu = document.body.classList.toggle("veu-sol");
      mostra.setAttribute("aria-expanded", String(veu));
      mostra.textContent = veu ? "Amaga el solucionari" : "Mostra el solucionari";
      if (veu) document.getElementById("solucionari").scrollIntoView({ behavior: "smooth" });
    });
    aplica();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();
})();
