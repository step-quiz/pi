/* ============================================================================
   comu/js/web.js · the shared helpers of the screen shell
   ----------------------------------------------------------------------------
   Loaded before every page script (portada.js, curs.js, unitat.js, professorat.js,
   paper.js, alumne.js). Everything hangs from window.PI:

     PI.esc(text)              HTML-escape
     PI.frases(text)           escape + a forced line break after every sentence
     PI.ic(nom)                one icon of the shared set, as inline SVG
     PI.boto(opcions)          a button or link with the shell button classes
     PI.capcalera(passos, op)  the violet header of every teacher page
     PI.cursEscolar(data)      «Curs 2026-27» (the year changes on 1 September)
     PI.pdfBase(cami)          "u3/fitxa.html" → "ud3", "u3/area.html" → "ud3-area"
     PI.lloc()                 {curs, unitat, fitxer} read from the page address
     PI.curs(id)               the registry entry of a course (comu/js/cursos.js)
     PI.unitat(n)              the unit n of the data already loaded (window.UNITATS)
     PI.carrega(srcs, fet)     loads scripts one after the other (works with file://)

   Nothing here writes styles: the look is in comu/css/web.css.
   ========================================================================== */

(function () {
  "use strict";
  const PI = window.PI = window.PI || {};

  PI.esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

  /* One sentence per line (decision of 6/11/2026). The break goes after a full stop,
     question or exclamation mark followed by a capital, a digit, «« or «(». Not after
     «Ex.», which is followed by an exercise number. */
  PI.frases = t => PI.esc(t).replace(/(?<!\bEx)([.!?])\s+(?=[A-ZÀÈÉÍÏÒÓÚÜÇ0-9«(])/g, "$1<br>");

  /* The icon set (decision D2): 24 × 24 grid, 2 px stroke, round caps, one colour.
     The pictograms printed on paper are a different set and live in the sheets. */
  const ICONES = {
    fitxa:   '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h4"/>',
    quadern: '<path d="M5 4h11a2 2 0 0 1 2 2v14H7a2 2 0 0 1-2-2z"/><path d="M5 18a2 2 0 0 1 2-2h11M9 8h5M9 11h3"/>',
    repas:   '<path d="M4 12a8 8 0 1 0 2.4-5.7"/><path d="M4 4v4h4M9 12l2 2 4-4"/>',
    eines:   '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8M12 17v4M7 13l3-3 2 2 4-4"/>',
    targeta: '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M7 10h4M7 14h7"/>',
    docent:  '<circle cx="12" cy="8" r="3.5"/><path d="M5 20a7 7 0 0 1 14 0"/>',
    pdf:     '<path d="M12 4v11M7 10l5 5 5-5M5 20h14"/>',
    sol:     '<path d="M6 3h8l4 4v14H6z"/><path d="M9 13l2 2 4-4"/>',
    impr:    '<path d="M7 9V3h10v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M7 14h10v7H7z"/>',
    enllac:  '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    text:    '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M13 7l4 4"/>',
    codi:    '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 10v4M10 10v4M13 10v4M17 10v4"/>',
    doc:     '<path d="M4 5a2 2 0 0 1 2-2h12v16H6a2 2 0 0 0-2 2z"/><path d="M4 21V5M8 7h6"/>'
  };
  PI.ic = nom => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" ' +
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + (ICONES[nom] || "") + "</svg>";

  /* A button. rol: "nav" | "mat" | "pdf" | "eina" (the four functions of D4).
     With href it is a link; without, a <button>. «descarrega» adds the download attribute. */
  PI.boto = function (o) {
    const cls = "w-b w-" + o.rol + (o.principal ? " w-principal" : "") + (o.classe ? " " + o.classe : "");
    const cos = (o.icona ? PI.ic(o.icona) : "") + PI.esc(o.text);
    const extra = o.atributs || "";
    if (o.href) {
      return '<a class="' + cls + '" href="' + PI.esc(o.href) + '"' + (o.descarrega ? " download" : "") + extra + ">" + cos + "</a>";
    }
    return '<button type="button" class="' + cls + '"' + extra + ">" + cos + "</button>";
  };

  /* The header of every teacher page. passos: [[text, href], …]; the last one is the
     current page and is never a link. op.professorat: the href of the «Professorat»
     button (none on the teacher page itself). */
  PI.capcalera = function (passos, op) {
    const cami = passos.map((p, i) => {
      const sep = i ? '<span class="w-sep" aria-hidden="true">›</span>' : "";
      if (i === passos.length - 1) return sep + '<span class="w-aqui" aria-current="page">' + PI.esc(p[0]) + "</span>";
      return sep + '<a href="' + PI.esc(p[1]) + '">' + PI.esc(p[0]) + "</a>";
    }).join("");
    const prof = op && op.professorat
      ? PI.boto({ rol: "nav", href: op.professorat, text: "Professorat", icona: "docent", classe: "w-prof" }) : "";
    return '<header class="w-cap"><div class="w-cap-esq"><span class="w-segell" aria-hidden="true">' + PI.ic("docent") +
      '</span><nav class="w-cami" aria-label="Camí">' + cami + "</nav></div>" + prof + "</header>";
  };

  /* The school year changes on 1 September: until 31 August 2027 it says «Curs 2026-27». */
  PI.cursEscolar = function (avui) {
    const any = avui.getFullYear(), inici = avui.getMonth() >= 8 ? any : any - 1;
    return "Curs " + inici + "-" + String(inici + 1).slice(-2);
  };

  /* The PDFs keep their names: the main sheet of unit 3 is pdf/ud3-…, the others
     pdf/ud3-SLUG-… (the same rule as generadors/gen_pdf.py). */
  PI.pdfBase = function (cami) {
    const m = String(cami).match(/u(\d+)\/([\w-]+)\.html$/);
    if (!m) return "";
    return "ud" + m[1] + (m[2] === "fitxa" ? "" : "-" + m[2]);
  };

  PI.curs = id => (PI.CURSOS || []).find(c => c.id === id) || { id: id, nom: id };

  /* Where the page is: the course folder, the unit folder (uN) and the file. It works
     both published (/CURS/u3/fitxa) and opened with a double click (file:///…/CURS/u3/fitxa.html). */
  PI.lloc = function () {
    const trossos = decodeURIComponent(location.pathname).split("/");
    const ids = (PI.CURSOS || []).map(c => c.id);
    let i = trossos.length - 1;
    while (i >= 0 && !ids.includes(trossos[i])) i--;
    const fitxer = (trossos[trossos.length - 1] || "index").replace(/\.html$/, "") || "index";
    if (i < 0) return { curs: null, unitat: null, fitxer: fitxer };
    const u = (trossos[i + 1] || "").match(/^u(\d+)$/);
    return { curs: trossos[i], unitat: u ? Number(u[1]) : null, fitxer: fitxer };
  };

  PI.unitat = n => (window.UNITATS || []).find(u => u.num === Number(n)) || null;

  /* Loads scripts in order. document.write is not allowed and fetch does not work
     with file://, so each script is a <script> element added after the previous one. */
  PI.carrega = function (srcs, fet) {
    const llista = srcs.slice();
    (function seguent() {
      if (!llista.length) { if (fet) fet(); return; }
      const s = document.createElement("script");
      s.src = llista.shift();
      s.onload = seguent;
      s.onerror = () => { console.error("PI: no s'ha pogut carregar " + s.src); seguent(); };
      document.head.appendChild(s);
    })();
  };

  /* Copies a text and tells the button: «Enllaç copiat», olive (decision of 6/11/2026). */
  PI.copia = function (boto, text) {
    const fet = () => { boto.classList.add("w-copiat"); boto.innerHTML = PI.ic("enllac") + "Enllaç copiat"; };
    const noEsPot = () => { boto.innerHTML = PI.ic("enllac") + PI.esc(text); };
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(fet, noEsPot);
      else noEsPot();
    } catch (e) { noEsPot(); }
  };
})();
