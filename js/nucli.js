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
     Si el mòdul té subtasques, cada panell va dins d'un
     <div class="subtasca" data-sub="n"> i s'hi crida CE.subtasques().

   LES FRASES NO VAN AL CODI NI AL MARCATGE
     Viuen a dades/textos.js. Al marcatge, data-text="1.2.titol"; al codi,
     CE.txt("1.2.encert", { nom: "√5" }). Així es poden canviar totes des d'un
     sol fitxer, o des de textos.html.

     3. afegeix el <button class="segment" data-tasca="n" data-mod="id">, amb el
        següent número lliure (surt als enllaços ?task=n i no es renumera mai),
        i la <section id="mod-id">.
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

  /** Una frase de dades/textos.js, amb els forats {x} omplerts i els
      *asteriscs* convertits en negreta. La clau és «grup.nom»: txt("1.2.encert").
      Si la frase no hi és, retorna la clau entre claudàtors, que canta prou
      per adonar-se'n de seguida sense petar. */
  function txt(clau, valors) {
    const i = clau.lastIndexOf(".");
    const grup = (window.TEXTOS || {})[clau.slice(0, i)] || {};
    let t = grup[clau.slice(i + 1)];
    if (t == null) return "[" + clau + "]";
    if (valors) for (const k in valors) t = t.split("{" + k + "}").join(valors[k]);
    return t.replace(/\*([^*]+)\*/g, "<b>$1</b>");
  }

  /** Omple tots els elements amb data-text="clau" d'un tros de pàgina.
      Així el marcatge no porta cap frase a dins. */
  function omplirTextos(arrel) {
    $$("[data-text]", arrel).forEach(n => { n.innerHTML = txt(n.dataset.text); });
  }

  /** Panells numerats dins d'un mòdul: la «tasca 1» passa a ser 1.1, 1.2, 1.3…
      Cada panell és un <div class="subtasca" data-sub="n" data-nom="…">, i la
      barra de fletxes és .sub-enrere / .sub-rotul / .sub-avant.
      El mòdul només ha de dir què vol fer quan se n'ensenya un; la navegació,
      el rètol i els botons desactivats van d'aquí.
      Es pot cridar diverses vegades: torna a lligar els botons i prou. */
  function subtasques(arrel, aoMostrar) {
    const panells = $$(".subtasca", arrel);
    if (!panells.length) return null;

    const enrere = $(".sub-enrere", arrel);
    const avant = $(".sub-avant", arrel);
    const rotul = $(".sub-rotul", arrel);
    // el número de tasca surt de la pestanya, per no repetir-lo al marcatge
    const pestanya = $('.segment[data-mod="' + arrel.id.replace("mod-", "") + '"]');
    const tasca = pestanya ? pestanya.dataset.tasca : "";
    let ara = 1;

    function mostra(n) {
      ara = Math.max(1, Math.min(panells.length, Number(n) || 1));
      panells.forEach(p => { p.hidden = Number(p.dataset.sub) !== ara; });
      if (enrere) enrere.disabled = ara === 1;
      if (avant) avant.disabled = ara === panells.length;
      if (rotul) {
        rotul.innerHTML = "<b>" + tasca + "." + ara + "</b> " +
          txt(tasca + "." + ara + ".nom").replace(/^\[.*\]$/, "");
      }
      if (aoMostrar) aoMostrar(ara);
    }

    if (enrere) enrere.onclick = () => mostra(ara - 1);
    if (avant) avant.onclick = () => mostra(ara + 1);
    return { mostra, quantes: panells.length, actual: () => ara };
  }

  const moduls = {};
  /** Cada mòdul es dona d'alta amb el seu identificador i la funció d'arrencada.
      La funció s'ha de poder cridar diverses vegades sense duplicar res. */
  function registra(id, inicia) {
    if (moduls[id]) console.warn("CE: el mòdul «" + id + "» ja estava registrat");
    moduls[id] = inicia;
  }

  return { $, $$, num, fix, euros, memoria, el, icona, pastilles,
           txt, omplirTextos, subtasques, moduls, registra };
})();
