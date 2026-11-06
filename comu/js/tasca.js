/* ============================================================================
   comu/js/tasca.js · tasks with steps, and the guided path between exercises
   ----------------------------------------------------------------------------
   Shared by the tools of every course (CURS/eines.html) and by the code readers
   (CURS/verifica.html). It used to be one copy per course; the copies differed
   only in the browser-storage prefix, which now comes from the course:
   CE.prefix, set in CURS/js/nucli.js («pi1-» in 1eso/, «pi-» in 4eso/). Both
   tools are published on the same domain: without the prefix a task left half
   done in one would show up in the other. Loaded after CURS/js/nucli.js and
   CURS/js/codi.js.

   A task is a closed sequence: a start you can see, a number of steps known
   from the beginning, one step on screen at a time and an end that says
   «Has acabat». For these students it is not a detail of presentation: knowing
   how much is left and when it is over removes load, and load is the
   bottleneck, not understanding.

   THIS FILE DOES, SO THAT NO MODULE HAS TO REPEAT IT
     · the progress rail:     Inici ● ● ○ ○ ○ Final   «Pas 2 de 5»
     · the progress saved in the browser and the question whether to go on;
     · the end: «Has acabat», the summary and the verification code (js/codi.js);
     · literal feedback: «Correcte.» / «Incorrecte. Ara provem-ho d'una altra
       manera.» + a hint that opens a different way;
     · after an answer, the feedback and the next-step button are scrolled into
       view (decision I1 of 6/11/2026: on a Chromebook they were below the screen);
     · THE GUIDED PATH between the exercises of a tool (CE.cami, see below).

   THE MODULE ONLY SAYS
     · how many steps the task has and how step i is drawn;
     · when a step is solved and how: CE.tasca(...).anota("be" | "pista" | "mostrat").

   MINIMAL USE
     const t = CE.tasca({
       tasca: 1, sub: 2,                    // the number of ?task=1.2
       recorregut: $("#x-recorregut"),      // where the progress rail goes
       represa: $("#x-represa"),            // where the «go on?» question goes
       final: $("#x-final"),                // where the summary goes
       cos: [$("#x-cos")],                  // what is hidden while the question shows
       nom: estat => "Situa el nombre",     // for the summary
       pinta: (i, estat) => { ... }         // shows step i
     });
     t.inicia(() => ({ total: 5, cas: 0, extra: {...} }));

   THE SAVED PROGRESS
   Goes to localStorage (through CE.memoria, already protected) under the key
   CE.prefix + «tasca:1.2». After 30 days it is dropped. A classroom computer is
   used by many people, so it never resumes on its own: it always asks, with the
   day it was saved. The same holds for the ?task= links, where app.js does not
   remember the open module for the same reason.
   ========================================================================== */

(function () {
  "use strict";
  const { txt, memoria, diaLlarg } = CE;
  if (!CE.prefix) console.error("CE: CURS/js/nucli.js must set CE.prefix (pi1- or pi-) before comu/js/tasca.js");

  const quiet = () => !!(window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches);

  /* Scrolling follows the student's own gestures only: a module that writes a
     notice while it opens (an example shown solved) must not move the page. */
  let gest = -1e9;
  ["pointerdown", "keydown"].forEach(t => document.addEventListener(t, () => { gest = performance.now(); }, true));
  const perGest = () => performance.now() - gest < 1500;

  /* Brings an element into view only if it is not entirely visible, and only
     as far as needed («nearest»). Waits one frame: the module usually redraws
     right after writing the feedback, and the layout must be the final one. */
  function aLaVista(el) {
    if (!el || !el.scrollIntoView || !perGest()) return;
    requestAnimationFrame(() => {
      if (!el.isConnected || !el.getClientRects().length) return;
      el.scrollIntoView({ block: "nearest", behavior: quiet() ? "auto" : "smooth" });
    });
  }

  /* After an answer: the visible next-step button of the same card if there is
     one below the feedback (showing it shows the feedback above it too), and
     the feedback otherwise. */
  function mostraResposta(avis) {
    const caixa = avis.closest(".subtasca, .targeta, .modul") || avis.parentElement;
    const boto = caixa && Array.from(caixa.querySelectorAll(".passa .btn"))
      .find(b => b.getClientRects().length && (avis.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING));
    aLaVista(boto || avis);
  }

  /* ======================================================= literal feedback == */

  const CLASSE = { encert: "be", be: "be", error: "pensa", mostra: "pensa", no: "pensa",
                   info: "neutre" };

  /** Writes the feedback in a notice, always with the same shape.
       encert → «Correcte.» and what happened
       error  → «Incorrecte.» + «Ara provem-ho d'una altra manera.» + the hint
       mostra → «Incorrecte.» and the answer, when no tries are left
       be     → a good state that is not an answer («x = 4 és una solució»)
       no     → a state that is not the good one and is not an answer either
                («x = 2 no és una solució»): no «Incorrecte», because trying a
                value on the balance is not answering
       info   → a neutral indication
     The word «Incorrecte» is there on purpose: a wrong answer is said plainly,
     without euphemisms. What softens it is what follows, which does not repeat
     the instruction but offers a different way.
     Answers (encert, error, mostra, be, no) bring the notice into view. */
  function retroaccio(node, tipus, cos, pista) {
    node.className = "avis " + (CLASSE[tipus] || "neutre");
    const trossos = [];
    if (tipus === "encert") trossos.push(txt("comu.correcte"));
    if (tipus === "error" || tipus === "mostra") trossos.push(txt("comu.incorrecte"));
    if (cos) trossos.push(cos);
    if (tipus === "error")  trossos.push(txt("comu.altra_manera"));
    let html = trossos.join(" ");
    if (pista) html += '<span class="pista">' + txt("comu.pista") + " " + pista + "</span>";
    node.innerHTML = html;
    if (tipus !== "info") mostraResposta(node);
  }

  /* ================================================== tasks with steps == */

  const CADUCA = 30 * 86400000;          // progress older than a month is not offered
  const clau = cfg => CE.prefix + "tasca:" + cfg.tasca + (cfg.sub ? "." + cfg.sub : "");

  function tasca(cfg) {
    const comptador = cfg.comptador || "comu.pas";
    const cos = cfg.cos || [];
    let estat = null;      // { cas, total, pas, res[], extra{}, acabada }
    let fesNou = null;     // returns { total, cas, extra } to start from zero

    /* ---- the progress rail ---- */
    const rail = cfg.recorregut;
    if (rail) {
      rail.classList.add("recorregut");
      rail.innerHTML =
        '<span class="fita">' + txt("comu.inici") + "</span>" +
        '<span class="punts-pas" aria-hidden="true"></span>' +
        '<span class="fita fi">' + txt("comu.final") + "</span>" +
        '<span class="rotul-pas" aria-live="polite"></span>';
    }

    const resolts = () => estat.res.filter(r => r != null && r !== "exemple").length;

    function pintaRecorregut() {
      if (!rail || !estat) return;
      const punts = rail.querySelector(".punts-pas");
      punts.textContent = "";
      estat.res.forEach((r, i) => {
        const p = document.createElement("i");
        if (r != null) p.classList.add("fet");
        if (i === estat.pas && !estat.acabada && cfg.ambPasActual !== false) p.classList.add("ara");
        punts.appendChild(p);
      });
      rail.classList.toggle("acabat", estat.acabada);
      rail.querySelector(".rotul-pas").innerHTML = estat.acabada
        ? txt("comu.rotul_final")
        : txt(comptador, { n: estat.pas + 1, fets: resolts(), total: estat.total,
                           ...(cfg.forats ? cfg.forats(estat) : {}) });
    }

    /* ---- the saved progress ---- */
    function desa() {
      if (!cfg.desa) return;
      if (!estat || estat.acabada) { memoria.esborra(clau(cfg)); return; }
      memoria.set(clau(cfg), JSON.stringify(Object.assign({ v: 1, desat: Date.now() }, estat)));
    }

    function llegeixDesat() {
      if (!cfg.desa) return null;
      try {
        const e = JSON.parse(memoria.get(clau(cfg)) || "null");
        const valid = e && e.v === 1 && !e.acabada && Number.isInteger(e.total) && e.total > 0 &&
                      Number.isInteger(e.pas) && e.pas >= 0 && e.pas < e.total &&
                      Array.isArray(e.res) && e.res.length === e.total &&
                      (!cfg.valida || cfg.valida(e));
        if (!valid) return null;
        if (Date.now() - e.desat > CADUCA) { memoria.esborra(clau(cfg)); return null; }
        // with no step done there is nothing to go on with: better start without asking
        if (!e.res.some(r => r != null && r !== "exemple")) return null;
        return e;
      } catch (err) {
        return null;                                  // a broken JSON must not stop the app
      }
    }

    /* ---- the visible step ---- */
    function mostraPas() {
      estat.acabada = false;
      if (rail) rail.hidden = false;
      if (cfg.represa) cfg.represa.hidden = true;
      if (cfg.final) cfg.final.hidden = true;
      cos.forEach(c => { c.hidden = false; });
      pintaRecorregut();
      cfg.pinta(estat.pas, estat);
      desa();
    }

    /** Starts from zero. Takes the data, or a function that returns them; in the
        second case that function becomes the one of «Torna a començar», and it
        is where the module resets what is its own (the tries, the value of x…). */
    function comenca(dades) {
      if (typeof dades === "function") fesNou = dades;
      const d = (typeof dades === "function" ? dades() : dades) || fesNou();
      estat = { cas: d.cas || 0, total: d.total, pas: 0,
                res: new Array(d.total).fill(null), extra: d.extra || {}, acabada: false };
      if (d.resultats) d.resultats.forEach((r, i) => { estat.res[i] = r; });
      if (d.pas) estat.pas = d.pas;
      mostraPas();
    }

    /** The entry point: if a task is half done, it asks; if not, it starts. */
    function inicia(nou) {
      fesNou = nou;
      const desat = llegeixDesat();
      if (desat) ofereixRepresa(desat);
      else comenca();
    }

    function ofereixRepresa(desat) {
      if (!cfg.represa) { comenca(); return; }
      cos.forEach(c => { c.hidden = true; });
      if (rail) rail.hidden = true;                  // one thing on screen: the question
      if (cfg.final) cfg.final.hidden = true;
      const r = cfg.represa;
      r.innerHTML =
        '<p class="represa-q">' + txt("comu.represa", { n: desat.pas + 1, total: desat.total }) + "</p>" +
        '<p class="represa-dia">' + txt("comu.represa_dia", { dia: diaLlarg(new Date(desat.desat)) }) + "</p>" +
        '<div class="represa-botons">' +
          '<button class="btn gran" data-f="continua">' + txt("comu.continua", { n: desat.pas + 1 }) + "</button>" +
          '<button class="btn gran tenyit" data-f="nou">' + txt("comu.de_nou") + "</button>" +
        "</div>" +
        '<p class="represa-nota">' + txt("comu.represa_nota") + "</p>";
      r.hidden = false;
      r.querySelector('[data-f="continua"]').onclick = () => {
        estat = { cas: desat.cas, total: desat.total, pas: desat.pas, res: desat.res,
                  extra: desat.extra || {}, acabada: false };
        mostraPas();
      };
      r.querySelector('[data-f="nou"]').onclick = () => comenca();
      r.querySelector("button").focus({ preventScroll: true });
    }

    /* ---- moving on ---- */
    function anota(resultat) {
      estat.res[estat.pas] = resultat;
      pintaRecorregut();
      desa();
    }
    const resolt = () => !!estat && estat.res[estat.pas] != null;
    const esUltim = () => !!estat && estat.pas === estat.total - 1;

    /* A new step starts at the top of the task: after an answer the page may
       have scrolled down to the button, and the new question is above. */
    const alPrincipi = () => aLaVista(rail || cos[0]);

    function seguent() {
      if (!estat || estat.acabada) return;
      if (estat.pas < estat.total - 1) { estat.pas++; mostraPas(); alPrincipi(); }
      else acaba();
    }
    function enrere() {
      if (estat && !estat.acabada && estat.pas > 0) { estat.pas--; mostraPas(); alPrincipi(); }
    }

    /* ---- the end ----
       `pendents` fills the steps not done: «Mostra-ho tot» ends the task with
       acaba("mostrat"), and the summary says it as it went. */
    function acaba(pendents) {
      if (pendents) estat.res = estat.res.map(r => (r == null ? pendents : r));
      estat.acabada = true;
      desa();                                          // when it ends, it is deleted
      pintaRecorregut();
      if (cfg.amagaEnAcabar !== false) cos.forEach(c => { c.hidden = true; });
      if (cfg.enAcabar) cfg.enAcabar(estat);
      pintaFinal();
    }

    /** The summary that suits nearly every task: steps, right at the first try,
        with a hint and with the answer shown. A module that counts something
        else (the equation counts solutions and tries) brings its own. */
    function resumPerDefecte(e) {
      const compta = r => e.res.filter(x => x === r).length;
      const passos = e.res.filter(x => x !== "exemple").length;
      return {
        files: [[txt("comu.r_passos"), passos],
                [txt("comu.r_primer"), compta("be")],
                [txt("comu.r_pista"), compta("pista")],
                [txt("comu.r_mostrat"), compta("mostrat")]],
        codi: { a: passos, b: compta("be"), c: compta("pista") }
      };
    }

    function pintaFinal() {
      if (!cfg.final) return;
      const r = (cfg.resum || resumPerDefecte)(estat);
      const codi = CE.codi.fes({ tasca: cfg.tasca, sub: cfg.sub || 0, cas: estat.cas,
                                 a: r.codi.a, b: r.codi.b, c: r.codi.c });
      const fila = (et, val) => "<dt>" + et + "</dt><dd>" + val + "</dd>";
      const f = cfg.final;
      f.innerHTML =
        '<h3 class="final-cap">' + txt("comu.has_acabat") + "</h3>" +
        (r.frase ? '<p class="final-frase">' + r.frase + "</p>" : "") +
        '<dl class="final-dades">' +
          fila(txt("comu.r_tasca"), cfg.nom(estat)) +
          fila(txt("comu.r_dia"), diaLlarg(new Date())) +
          r.files.map(([et, val]) => fila(et, val)).join("") +
        "</dl>" +
        '<p class="final-nom">' + txt("comu.nom_paper") + "</p>" +
        '<div class="final-codi"><span>' + txt("comu.codi") + "</span><b>" + codi + "</b></div>" +
        '<p class="final-nota">' + txt("comu.ensenya_codi") + "</p>" +
        '<div class="final-botons">' +
          '<button class="btn" data-f="imprimeix">' + txt("comu.imprimeix") + "</button>" +
          '<button class="btn tenyit" data-f="torna">' + txt("comu.torna") + "</button>" +
        "</div>";
      f.hidden = false;
      f.setAttribute("tabindex", "-1");
      f.querySelector('[data-f="imprimeix"]').onclick = () => imprimeix(f);
      f.querySelector('[data-f="torna"]').onclick = () => comenca();
      // focus goes to the summary so that a screen reader says it, and it is
      // made visible without jumping if it already is
      f.focus({ preventScroll: true });
      if (f.scrollIntoView) f.scrollIntoView({ block: "nearest" });
    }

    return { inicia, comenca, anota, resolt, esUltim, seguent, enrere, acaba,
             pintaRecorregut, estat: () => estat };
  }

  /** Prints only the summary. A copy goes to #zona-impressio, a direct child of
      <body>, and a class on <body> makes the @media print of app.css hide the
      rest. A copy and not the original, because the summary sits inside cards
      and modules that must be hidden. */
  function imprimeix(node) {
    let zona = document.getElementById("zona-impressio");
    if (!zona) {
      zona = document.createElement("div");
      zona.id = "zona-impressio";
      document.body.appendChild(zona);
    }
    zona.textContent = "";
    const copia = node.cloneNode(true);
    copia.removeAttribute("id");
    copia.removeAttribute("tabindex");
    zona.appendChild(copia);
    document.body.classList.add("imprimeix-resum");
    const neteja = () => {
      document.body.classList.remove("imprimeix-resum");
      zona.textContent = "";
    };
    window.addEventListener("afterprint", neteja, { once: true });
    // Some browsers (Safari on the iPad) print without blocking and do not
    // always say when they are done. Then it is cleaned at the next gesture:
    // removing the class before the dialog has read the page would print the
    // whole toolbox.
    setTimeout(() => {
      window.addEventListener("pointerdown", neteja, { once: true });
      window.addEventListener("keydown", neteja, { once: true });
    }, 0);
    window.print();
  }

  /** Shuffles a list without touching the original (Fisher-Yates). */
  function barreja(llista) {
    const c = llista.slice();
    for (let i = c.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [c[i], c[j]] = [c[j], c[i]];
    }
    return c;
  }

  /* ==================================================== THE GUIDED PATH ==
     Decision of 6/11/2026 («too many places to click»): inside a tool there are
     no arrows to jump between exercises any more. The exercises go one after
     the other, and ONE button at the very bottom, «Exercici següent», leads to
     the next one:
       · in an exercise to explore (no progress rail) it is always there;
       · in a closed task it appears when the task is over (the rail says
         «acabat»), next to the summary and the code;
       · on the last exercise, and with a link to one exercise (?task=1.2),
         there is none.
     The bar on top keeps only the name, «1.2 El rectangle d'una multiplicació».
     Two more things, so that the same words do not appear twice (decision I2):
       · a card title equal to that name is hidden from sight (the voice still
         reads it: it is clipped, not removed);
       · if the exercise shows the name again as its question («Quina fracció
         és?»), the bar keeps only the number.
     CE.cami(arrel, sub, fixa) is called by CE.subtasques (CURS/js/nucli.js)
     once per tool; it returns the function to call after each change of
     exercise. */
  function cami(arrel, control, fixa) {
    // A tool may set up its exercises more than once: one footer and one observer each.
    if (arrel._cami) { arrel._cami.sub = control; return arrel._cami.actualitza; }
    const estat = { sub: control };
    const sub = { mostra: n => estat.sub.mostra(n), get quantes() { return estat.sub.quantes; },
                  actual: () => estat.sub.actual() };
    arrel.querySelectorAll(".sub-enrere, .sub-avant").forEach(b => { b.hidden = true; });
    const rotul = arrel.querySelector(".sub-rotul");
    let peu = null;
    if (!fixa && sub.quantes > 1) {
      peu = document.createElement("div");
      peu.className = "sub-peu";
      peu.innerHTML = '<button type="button" class="btn gran sub-seguent">' + txt("comu.exercici_seguent") + "</button>";
      arrel.appendChild(peu);
      peu.querySelector("button").onclick = () => {
        sub.mostra(sub.actual() + 1);
        const dalt = arrel.querySelector(".subbarra") || arrel;
        requestAnimationFrame(() => dalt.scrollIntoView({ block: "start", behavior: quiet() ? "auto" : "smooth" }));
      };
    }
    const panell = () => Array.from(arrel.querySelectorAll(".subtasca")).find(p => !p.hidden);
    const net = t => String(t || "").replace(/\s+/g, " ").trim();

    /* Every write below happens only on a real change: the observer watches
       this same subtree, and writing the same value again would wake it up. */
    function botoPeu() {
      if (!peu) return;
      const p = panell();
      const rail = p && p.querySelector(".recorregut");
      const acabada = !rail || rail.classList.contains("acabat");
      const amaga = !p || sub.actual() >= sub.quantes || !acabada;
      if (peu.hidden === amaga) return;
      peu.hidden = amaga;
      if (!amaga && rail) aLaVista(peu.querySelector("button"));
    }

    /* The bar is written by CE.subtasques as «<b>1.2</b> name», with the name in
       data-nom and «0|name» in data-escrit. It is rewritten here only when that
       state changes (comparing innerHTML would not do: &nbsp; and the like). */
    function titols() {
      const p = panell();
      if (!p || !rotul) return;
      const nomHtml = rotul.dataset.nom || "";
      const nom = net(nomHtml.replace(/<[^>]+>/g, ""));
      p.querySelectorAll(".targeta h2").forEach(h => {
        const repetit = !!nom && net(h.textContent) === nom;
        if (h.classList.contains("repetit") !== repetit) h.classList.toggle("repetit", repetit);
      });
      const pregunta = Array.from(p.querySelectorAll("[id$='-pregunta'], .pregunta-gran")).find(x => x.getClientRects().length);
      const doble = !!nom && !!pregunta && net(pregunta.textContent) === nom;
      const estat = (doble ? "1" : "0") + "|" + nomHtml;
      const num = rotul.querySelector("b");
      if (!num || rotul.dataset.escrit === estat) return;
      rotul.dataset.escrit = estat;
      rotul.innerHTML = num.outerHTML + (doble ? "" : " " + nomHtml);
    }

    let pendent = false;
    function actualitza() {
      if (pendent) return;
      pendent = true;
      requestAnimationFrame(() => { pendent = false; botoPeu(); titols(); });
    }
    new MutationObserver(actualitza).observe(arrel,
      { subtree: true, childList: true, attributes: true, attributeFilter: ["class", "hidden"] });
    estat.actualitza = actualitza;
    arrel._cami = estat;
    return actualitza;
  }

  Object.assign(CE, { tasca, retroaccio, barreja, cami });
})();
