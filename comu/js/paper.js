/* ============================================================================
   comu/js/paper.js · the header of every paper page (sheet, review, workbook, card)
   ----------------------------------------------------------------------------
   A paper page carries, right after <body>, ONE screen-only bar written by its
   generator:

     <nav class="navega no-imprimir" aria-label="Navegació"><link rel="stylesheet"
       href="../../comu/css/web.css"><a href="index.html">Unitat 3</a><script
       src="../../comu/js/paper.js"></script></nav>

   Everything screen-only lives INSIDE that <nav>, because the PDF fingerprint
   (CURS/eines/empremta.py, 1eso/eines/paper.py: SENSE_PDF) strips exactly that
   element. Changing the header therefore never makes a PDF old.

   This script loads cursos.js, web.js and the course data (../dades/unitats.js;
   uN/ and targetes/ are both one level below the course), and then puts the
   violet header in the bar, followed by the PDF buttons:
     sheet or review   PDF alumnat · PDF solucionari
     card              PDF a doble cara (the unit comes from ?u=N)
     workbook          nothing: it has its own print buttons
   It also sets the tab title from the data (decision V2).
   ========================================================================== */

(function () {
  "use strict";
  const jo = document.currentScript;
  const barra = jo && jo.parentElement;
  const base = jo ? jo.src.replace(/paper\.js(\?.*)?$/, "") : "";

  function pinta() {
    const PI = window.PI;
    const lloc = PI.lloc();
    const curs = PI.curs(lloc.curs);
    const targeta = /\/targetes\/[^/]+$/.test(location.pathname.replace(/\/$/, ""));
    let u, que, botons = "";
    if (targeta) {
      const t = (window.TARGETES || []).find(x => x.nom === lloc.fitxer) || { titol: "Targeta", unitats: [] };
      const demanada = Number(new URLSearchParams(location.search).get("u"));
      u = PI.unitat((t.unitats || []).includes(demanada) ? demanada : (t.unitats || [])[0]);
      que = "Targeta";
      botons = PI.boto({ rol: "pdf", href: "../pdf/targeta-" + lloc.fitxer + ".pdf", descarrega: true,
        text: "PDF a doble cara", icona: "pdf", principal: true });
      document.title = t.titol;
    } else {
      u = PI.unitat(lloc.unitat);
      const cami = u ? "u" + u.num + "/" + lloc.fitxer + ".html" : "";
      const fitxes = u ? (u.fitxes || []) : [];
      const k = fitxes.findIndex(f => f.fitxa === cami);
      if (lloc.fitxer === "quadern") que = "Quadern d'activitats";
      else if (u && u.repas && u.repas.fitxa === cami) que = "Repàs";
      else que = fitxes.length > 1 && k >= 0 ? "Fitxa " + (k + 1) : "Fitxa";
      if (lloc.fitxer !== "quadern") {
        const b = PI.pdfBase(cami);
        botons = PI.boto({ rol: "pdf", href: "../pdf/" + b + "-alumnat.pdf", descarrega: true, text: "PDF alumnat", icona: "pdf", principal: true }) +
                 PI.boto({ rol: "pdf", href: "../pdf/" + b + "-solucionari.pdf", descarrega: true, text: "PDF solucionari", icona: "sol" });
      }
      if (u) document.title = que + " · Unitat " + u.num + " · " + u.titol;
    }
    const aUnitat = targeta ? "../u" + (u ? u.num : 1) + "/index.html" : "index.html";
    const passos = [["Inici", "../../index.html"], [curs.nom, "../index.html"]]
      .concat(u ? [["Unitat " + u.num, aUnitat]] : []).concat([[que, ""]]);
    const caixa = document.createElement("div");
    caixa.innerHTML = PI.capcalera(passos, { professorat: "../professorat.html" }) +
      (botons ? '<div class="w-barra-paper">' + botons + "</div>" : "");
    barra.querySelectorAll(":scope > a").forEach(a => a.remove());
    barra.appendChild(caixa);
  }

  if (!barra) return;
  const srcs = [];
  if (!(window.PI && window.PI.CURSOS)) srcs.push(base + "cursos.js");
  if (!(window.PI && window.PI.capcalera)) srcs.push(base + "web.js");
  const seguent = () => {
    if (window.UNITATS) { pinta(); return; }
    window.PI.carrega(["../dades/unitats.js"], pinta);
  };
  /* web.js brings PI.carrega; until then, a plain loader. */
  (function carrega(llista) {
    if (!llista.length) { seguent(); return; }
    const s = document.createElement("script");
    s.src = llista.shift();
    s.onload = () => carrega(llista);
    document.head.appendChild(s);
  })(srcs);
})();
