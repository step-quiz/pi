/* ============================================================================
   nucli.js · el poc que comparteixen tots els mòduls
   ----------------------------------------------------------------------------
   Aquest fitxer defineix l'únic objecte global del projecte, `CE`, i s'ha de
   carregar abans que cap mòdul.

   PER QUÈ SCRIPTS CLÀSSICS I NO MÒDULS ES
   Els mòduls ES (`type="module"`) no funcionen obrint el fitxer amb doble clic
   (`file://`) perquè el navegador els bloqueja per CORS. Aquest projecte s'ha
   de poder obrir des d'un llapis de memòria i sense servidor, igual que la
   resta del material del departament. Per això: scripts clàssics, cada mòdul
   dins d'una funció que s'executa tota sola, i un sol nom global.

   AFEGIR UN MÒDUL NOU
     1. crea js/moduls/<nom>.js amb l'embolcall
        (function(){ "use strict"; const {$, ...} = CE;  ...  CE.registra("id", inicia); })();
     2. posa-hi el <script src> a caixa-eines.html;
     3. afegeix el <button class="segment" data-mod="id"> i la <section id="mod-id">.
   No cal tocar app.js.
   ========================================================================== */

window.CE = (function () {
  "use strict";

  const $  = (s, arrel = document) => arrel.querySelector(s);
  const $$ = (s, arrel = document) => Array.from(arrel.querySelectorAll(s));

  /** Format català: coma decimal i sense zeros finals inútils.
      Compte: els zeros només es retallen DESPRÉS de la coma. Si es retallessin
      sempre, "20" es convertiria en "2" i les marques dels eixos mentirien. */
  function num(x, dec = 2) {
    if (x === 0) x = 0;                 // normalitza el -0 de resoldre equacions
    let s = Number(x).toFixed(dec);
    if (s.includes(".")) s = s.replace(/0+$/, "").replace(/\.$/, "");
    return s.replace(".", ",");
  }
  /** Com num(), però conservant tots els decimals demanats. */
  const fix   = (x, dec) => Number(x).toFixed(dec).replace(".", ",");
  const euros = x => fix(x, 2) + " €";

  /** localStorage protegit: en previsualitzacions o amb cookies bloquejades no
      existeix, i llavors es fa servir un objecte en memòria. */
  const memoria = (() => {
    try {
      localStorage.setItem("__p", "1"); localStorage.removeItem("__p");
      return { get: k => localStorage.getItem(k), set: (k, v) => localStorage.setItem(k, v) };
    } catch (e) {
      const m = {};
      return { get: k => m[k] ?? null, set: (k, v) => { m[k] = v; } };
    }
  })();

  const SVGNS = "http://www.w3.org/2000/svg";
  /** Crea un node SVG. Els colors es passen dins de `style` amb var(--…) perquè
      el mode fosc funcioni sense duplicar codi. */
  function el(nom, atr = {}, text) {
    const n = document.createElementNS(SVGNS, nom);
    for (const k in atr) n.setAttribute(k, atr[k]);
    if (text != null) n.textContent = text;
    return n;
  }
  /** Instància d'un pictograma declarat als <symbol> de la pàgina. */
  function icona(id, mida) {
    const s = el("svg", { viewBox: "0 0 32 32", width: mida, height: mida });
    s.appendChild(el("use", { href: "#" + id }));
    return s;
  }

  /** Fila de pastilles amb selecció exclusiva. `aoTriar` rep (element, índex). */
  function pastilles(cont, llista, aoTriar, iniciX = 0) {
    cont.textContent = "";
    llista.forEach((it, i) => {
      const b = document.createElement("button");
      b.className = "pastilla";
      b.textContent = it.et;
      b.setAttribute("aria-pressed", i === iniciX);
      b.onclick = () => {
        $$(".pastilla", cont).forEach(x => x.setAttribute("aria-pressed", "false"));
        b.setAttribute("aria-pressed", "true");
        aoTriar(it, i);
      };
      cont.appendChild(b);
    });
  }

  const moduls = {};
  /** Cada mòdul es dona d'alta amb el seu identificador i la funció d'arrencada.
      La funció s'ha de poder cridar diverses vegades sense duplicar res. */
  function registra(id, inicia) {
    if (moduls[id]) console.warn("CE: el mòdul «" + id + "» ja estava registrat");
    moduls[id] = inicia;
  }

  return { $, $$, num, fix, euros, memoria, el, icona, pastilles, moduls, registra };
})();
