/* ============================================================================
   nucli.js · el poc que comparteixen tots els mòduls de la caixa d'eines
   ----------------------------------------------------------------------------
   Còpia del nucli de la caixa de 4eso/, no un enllaç: si aquell canvia, aquest
   no s'ha de moure. Defineix l'únic objecte global, `CE`, i s'ha de carregar
   abans que cap mòdul.

   PER QUÈ SCRIPTS CLÀSSICS I NO MÒDULS ES
   Els mòduls ES (`type="module"`) no funcionen obrint el fitxer amb doble clic
   (`file://`): el navegador els bloqueja per CORS. Aquesta caixa s'ha de poder
   obrir des d'un llapis de memòria i sense servidor. Per això: scripts
   clàssics, cada mòdul dins d'una funció que s'executa tota sola, i un sol nom
   global.

   AFEGIR UN MÒDUL NOU
     1. crea js/moduls/<nom>.js amb l'embolcall
        (function(){ "use strict"; const {$, ...} = CE;  ...  CE.registra("id", inicia); })();
     2. posa-hi el <script src> a caixa-eines.html, abans de js/app.js;
     3. afegeix el <button class="segment" data-tasca="n" data-mod="id">, amb el
        següent número lliure (surt als enllaços ?task=n i no es renumera mai),
        i la <section id="mod-id">.
     Cada exercici del mòdul va dins d'un <div class="subtasca" data-sub="n">.
     No cal tocar app.js.

   LES FRASES NO VAN AL CODI NI AL MARCATGE
     Viuen a dades/textos.js. Al marcatge, data-text="1.2.titol"; al codi,
     CE.txt("1.2.encert", { a: 3 }).

   QUÈ HI HA DE NOU RESPECTE DE L'ORIGINAL
     · quants(), rect(), deN() i delNombre(): «1 quadret» i «12 quadrets»,
       «3 files de 4 quadrets» i «5 files d'11 quadrets», «la taula de l'1» i
       «la taula del 7». La gramàtica es fa aquí i no a les frases: si no,
       cada frase hauria de tenir una versió per al singular i una per a l'1.
     · lectura(): el bloc que va sota de cada dibuix. Primer les paraules i al
       final el símbol, en aquest ordre (docs/CRITERIS-DISSENY.md, regla 5).
     · comptador(): el control [−] 3 [+], igual a tots els mòduls.
     · subDemanada(tasca): ?task=1.3 obre la subtasca 3 NOMÉS de la tasca 1.
       A l'original només un mòdul tenia subtasques; aquí en tenen tots. Amb
       un enllaç així, la barra de subtasques no té fletxes (.subbarra.fixa).
   ========================================================================== */

window.CE = (function () {
  "use strict";

  const $  = (s, arrel = document) => arrel.querySelector(s);
  const $$ = (s, arrel = document) => Array.from(arrel.querySelectorAll(s));

  /** localStorage protegit: en previsualitzacions o amb cookies bloquejades no
      existeix, i llavors es fa servir un objecte en memòria. Cada operació va
      dins d'un try: el disc ple o una pestanya privada no han de trencar l'app. */
  const memoria = (() => {
    try {
      localStorage.setItem("__p", "1"); localStorage.removeItem("__p");
      const prova = f => { try { return f(); } catch (e) { return null; } };
      return { get: k => prova(() => localStorage.getItem(k)),
               set: (k, v) => prova(() => localStorage.setItem(k, v)),
               esborra: k => prova(() => localStorage.removeItem(k)) };
    } catch (e) {
      const m = {};
      return { get: k => m[k] ?? null, set: (k, v) => { m[k] = v; },
               esborra: k => { delete m[k]; } };
    }
  })();

  /** Una data escrita sencera: «dilluns 21 de setembre de 2026». Lectura Fàcil
      demana els dies i els mesos amb lletres. Es fa a mà i no amb Intl perquè
      cada navegador hi posa comes o majúscules diferents. */
  const DIES = ["diumenge", "dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte"];
  const MESOS = ["de gener", "de febrer", "de març", "d'abril", "de maig", "de juny", "de juliol",
                 "d'agost", "de setembre", "d'octubre", "de novembre", "de desembre"];
  const diaLlarg = d => DIES[d.getDay()] + " " + d.getDate() + " " + MESOS[d.getMonth()] +
                        " de " + d.getFullYear();

  /** El catàleg de tasques que donen codi de verificació. Cada mòdul hi diu el
      nom de la tasca i què vol dir cada recompte; verifica.html el llegeix. */
  const cataleg = {};
  function registraCataleg(id, fitxa) { cataleg[id] = fitxa; }

  const SVGNS = "http://www.w3.org/2000/svg";
  /** Crea un node SVG. Els colors van en classes de css/app.css, perquè el mode
      fosc funcioni sense duplicar codi. */
  function el(nom, atr = {}, text) {
    const n = document.createElementNS(SVGNS, nom);
    for (const k in atr) n.setAttribute(k, atr[k]);
    if (text != null) n.textContent = text;
    return n;
  }

  /** Fila de pastilles amb selecció exclusiva. `aoTriar` rep (element, índex).
      Amb iniciX = -1 no n'hi ha cap de premuda: ho fa servir la 0.2, on triar
      la taula és el primer pas de la tasca. */
  function pastilles(cont, llista, aoTriar, iniciX = 0) {
    cont.textContent = "";
    llista.forEach((it, i) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "pastilla";
      b.textContent = it.et;
      if (it.aria) b.setAttribute("aria-label", it.aria);
      b.setAttribute("aria-pressed", String(i === iniciX));
      b.onclick = () => {
        $$(".pastilla", cont).forEach(x => x.setAttribute("aria-pressed", "false"));
        b.setAttribute("aria-pressed", "true");
        aoTriar(it, i);
      };
      cont.appendChild(b);
    });
  }
  /** Marca una pastilla com a premuda sense disparar-la. */
  function premPastilla(cont, index) {
    $$(".pastilla", cont).forEach((x, i) => x.setAttribute("aria-pressed", String(i === index)));
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
  /** La mateixa frase, sense negretes: per als aria-label. */
  const txtPla = (clau, valors) => txt(clau, valors).replace(/<[^>]+>/g, "");

  /** Omple tots els elements amb data-text="clau" d'un tros de pàgina. */
  function omplirTextos(arrel) {
    $$("[data-text]", arrel).forEach(n => { n.innerHTML = txt(n.dataset.text); });
  }

  /* ---------------------------------------------------------- gramàtica --
     Davant de l'1 (u) i de l'11 (onze) s'apostrofa: «d'1 quadret», «la taula
     de l'1», «l'arrel quadrada d'11». Són els únics nombres d'aquesta caixa que
     es llegeixen començant per vocal. */
  const vocal = n => n === 1 || n === 11;
  /** «1 quadret», «12 quadrets», «0 quadrets». `sing` i `plur` són claus. */
  const quants = (n, sing, plur) => n + " " + txt(n === 1 ? sing : plur);
  /** «de 4», «d'1», «d'11». */
  const deN = n => (vocal(n) ? "d'" : "de ") + n;
  /** «del 7», «de l'1». */
  const delNombre = n => (vocal(n) ? "de l'" : "del ") + n;
  /** «el 305», «l'11». */
  const elNombre = n => (vocal(n) ? "l'" : "el ") + n;
  /** «3 files de 4 quadrets», «1 fila d'1 quadret»: la lectura del rectangle. */
  const rect = (files, cols) => quants(files, "comu.fila", "comu.files") + " " +
    (vocal(cols) ? "d'" : "de ") + quants(cols, "comu.quadret", "comu.quadrets");

  /** El bloc de sota del dibuix: primer les paraules, al final el símbol.
      `paraules` i `simbols` són llistes de frases ja compostes. */
  function lectura(paraules, simbols) {
    const p = (paraules || []).filter(Boolean).map(t => '<p class="paraules">' + t + "</p>").join("");
    const s = [].concat(simbols || []).filter(Boolean)
      .map(t => '<p class="simbol' + (t.length > 16 ? " llarg" : "") + '">' + t + "</p>").join("");
    return p + s;
  }

  /** El control [−] 3 [+]. `cfg`: { et, sub, min, max, valor, aoCanviar }.
      Retorna { valor(), posa(n), activa(sí/no) }. Als extrems, el botó es
      desactiva: un botó que no fa res ha de semblar que no fa res. */
  function comptador(cont, cfg) {
    cont.classList.add("comptador");
    cont.innerHTML =
      '<span class="comptador-et">' + cfg.et + (cfg.sub ? "<small>" + cfg.sub + "</small>" : "") + "</span>" +
      '<span class="comptador-fila">' +
        '<button type="button" class="btn tenyit rodo" data-f="menys">−</button>' +
        '<output class="comptador-valor" aria-live="polite"></output>' +
        '<button type="button" class="btn tenyit rodo" data-f="mes">+</button>' +
      "</span>";
    const menys = $('[data-f="menys"]', cont), mes = $('[data-f="mes"]', cont);
    const sortida = $("output", cont);
    const nom = String(cfg.et).replace(/<[^>]+>/g, "");
    menys.setAttribute("aria-label", nom + ": " + txtPla("comu.treu"));
    mes.setAttribute("aria-label", nom + ": " + txtPla("comu.afegeix"));
    let v = cfg.valor, actiu = true;
    function pinta() {
      sortida.textContent = v;
      menys.disabled = !actiu || v <= cfg.min;
      mes.disabled = !actiu || v >= cfg.max;
    }
    function canvia(d) {
      const n = Math.max(cfg.min, Math.min(cfg.max, v + d));
      if (n === v) return;
      v = n; pinta();
      if (cfg.aoCanviar) cfg.aoCanviar(v);
    }
    menys.onclick = () => canvia(-1);
    mes.onclick = () => canvia(+1);
    pinta();
    return { valor: () => v, posa: n => { v = n; pinta(); }, activa: b => { actiu = b; pinta(); } };
  }

  /** Panells numerats dins d'un mòdul: la «tasca 1» passa a ser 1.1, 1.2, 1.3…
      Cada panell és un <div class="subtasca" data-sub="n">, i la barra de
      fletxes és .sub-enrere / .sub-rotul / .sub-avant. El nom de cada panell
      surt de la frase «tasca.sub.nom» de dades/textos.js. */
  function subtasques(arrel, aoMostrar) {
    const panells = $$(".subtasca", arrel);
    if (!panells.length) return null;

    const enrere = $(".sub-enrere", arrel);
    const avant = $(".sub-avant", arrel);
    const rotul = $(".sub-rotul", arrel);
    // Un enllaç a un exercici concret (?task=1.2) porta a aquell exercici i prou:
    // la barra diu on s'és, però les fletxes no hi són. Val per a totes les
    // pestanyes, també per a Taules, que s'obre per la 0.1. Amb l'enllaç a tota
    // l'eina (?task=1) les fletxes hi són.
    const barra = $(".subbarra", arrel);
    if (barra && window.CE.demanada) barra.classList.add("fixa");
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

  /** La subtasca que demana l'enllaç (?task=1.3), només si és d'aquesta tasca. */
  function subDemanada(tasca) {
    const d = window.CE.demanada;
    return d && d.tasca === String(tasca) ? d.sub : null;
  }

  /** Fa servir el moviment reduït del sistema? Llavors no hi ha animacions. */
  const quiet = () => !!(window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches);

  const moduls = {};
  /** Cada mòdul es dona d'alta amb el seu identificador i la funció d'arrencada.
      La funció s'ha de poder cridar diverses vegades sense duplicar res. */
  function registra(id, inicia) {
    if (moduls[id]) console.warn("CE: el mòdul «" + id + "» ja estava registrat");
    moduls[id] = inicia;
  }

  return { $, $$, memoria, el, pastilles, premPastilla, txt, txtPla, omplirTextos,
           subtasques, subDemanada, moduls, registra, diaLlarg, cataleg, registraCataleg,
           quants, deN, delNombre, elNombre, rect, lectura, comptador, quiet, demanada: null };
})();
