/* ============================================================================
   veu.js · la lectura en veu alta de cada targeta de la caixa d'eines
   ----------------------------------------------------------------------------
   Cada targeta amb títol porta, a dalt a la dreta, un botó petit amb un
   altaveu. En tocar-lo, el navegador llegeix la targeta en veu alta i marca
   el tros que llegeix. Tornar-lo a tocar la para. Tocar qualsevol altre botó
   (respondre, canviar d'eina o d'exercici) també la para: la pantalla canvia,
   i la veu no ha de llegir una cosa que ja no hi és.

   És el mateix fitxer a 1eso/ i a 4eso/. Fa servir la síntesi de veu del
   navegador (Web Speech API): no cal xarxa, ni servidor, ni instal·lar res.
   Si el navegador no en té, el botó no surt.

   COM LLEGEIX, I PER QUÈ
     · En català (ca-ES), amb la millor veu catalana de l'ordinador: primer les
       «naturals» (Edge en porta dues, Joana i Enric), després qualsevol altra.
     · A poc a poc: VELOCITAT 0,85, una mica per sota de la normal (1). Més
       lenta, la veu s'arrossega i es fa estranya; més ràpida, no dona temps.
     · El to de la veu, el natural (TO 1). Un to més agut sona infantil.
     · Un bloc cada vegada (el títol, la consigna, cada línia de la lectura,
       l'avís) i una pausa entre bloc i bloc (PAUSA), perquè cada idea arribi
       sola. És el mateix ritme que demana Lectura Fàcil: una idea per frase.
     · Sempre igual i només quan es demana: res no parla sol en obrir una
       pàgina, ni hi ha sons de premi o d'error.
     · Els símbols es llegeixen amb paraules: «3 · 4 = 12» es diu «3 per 4 és
       igual a 12»; «7²», «7 al quadrat». Les fraccions i les expressions amb
       forat ja porten la seva lectura (aria-label), i es diu aquesta.
     · No es llegeixen els botons, els dibuixos, les etiquetes «Exemple» ni
       l'«Inici» i el «Final» del rètol de progrés: només «Pas 2 de 5».

   COM MARCA EL QUE LLEGEIX
     · El bloc que sona té un fons groc clar, com de retolador: la classe
       .veu-bloc (al final de css/app.css). És una classe normal i funciona a
       tots els navegadors. Abans es feia amb CSS.highlights i un blau molt
       suau, i a la pràctica no es veia res, ni a Windows ni a Android
       (23/10/2026).
     · Si la veu diu per on va (Edge i Safari ho fan; la veu de Google
       d'Android i moltes de Chrome, no), la paraula que sona té, a més, un
       groc més fort. Aquesta sí que es fa amb CSS.highlights, que no toca el
       text: on no n'hi ha, es queda la marca del bloc, que ja n'hi ha prou.
   ========================================================================== */

(function () {
  "use strict";
  const { $$, txt } = CE;
  const veu = window.speechSynthesis;
  if (!veu || !window.SpeechSynthesisUtterance) return;

  const VELOCITAT = 0.85;
  const TO = 1;
  const PAUSA = 450;   // mil·lisegons de silenci entre bloc i bloc

  /* ---------------------------------------------------------- la veu ---- */
  function triaVeu() {
    const cat = veu.getVoices().filter(v => /^ca\b|^ca[-_]/i.test(v.lang));
    const bona = v => /natural|online|neural|enhanced|premium/i.test(v.name);
    return cat.find(bona) || cat.find(v => v.localService) || cat[0] || null;
  }
  // Chrome dona la llista de veus més tard, no d'entrada.
  if (veu.addEventListener) veu.addEventListener("voiceschanged", () => {});

  /* ---------------------------------------------- dels símbols a paraules --
     Cada paraula de la pantalla es converteix tota sola. Així, cada tros del
     que es diu sap de quina paraula de la pantalla surt, i es pot marcar. */
  const QUADRATS = { km: "quilòmetres quadrats", dm: "decímetres quadrats", cm: "centímetres quadrats",
                     mm: "mil·límetres quadrats", m: "metres quadrats" };
  const SOLS = { ":": "dividit entre", "/": "dividit entre", "+": "més", "-": "menys", "?": "",
                 "<": "és més petit que", ">": "és més gran que" };
  function diu(p) {
    if (p in SOLS) return SOLS[p];
    return p
      .replace(/[→←◢◣◤◥○●▢▶◀‹›]/g, "")
      .replace(/(km|dm|cm|mm|m)²/g, (_, u) => " " + QUADRATS[u])
      .replace(/²/g, " al quadrat").replace(/³/g, " al cub")
      .replace(/√/g, " l'arrel quadrada de ")
      .replace(/π/g, " pi ")
      .replace(/%/g, " per cent").replace(/€/g, " euros")
      // el punt volat multiplica, menys dins d'una paraula: «col·lecció»
      .replace(/(?<!\p{L})·|·(?!\p{L})/gu, " per ")
      .replace(/×/g, " per ").replace(/÷/g, " dividit entre ")
      .replace(/(?<=\d)\+(?=\d)/g, " més ").replace(/(?<=\d)-(?=\d)/g, " menys ").replace(/−/g, " menys ")
      .replace(/≈/g, " és aproximadament ").replace(/≤/g, " és més petit o igual que ")
      .replace(/≥/g, " és més gran o igual que ").replace(/=/g, " és igual a ")
      .replace(/…/g, "").replace(/[—–]/g, ", ")
      .replace(/\s+/g, " ").trim();
  }

  /* ------------------------------------------------- què es llegeix ----
     Els blocs de la targeta, en l'ordre de la pàgina. Un bloc és l'element de
     bloc més proper que conté el text. */
  const NO_ES_LLEGEIX = "button, svg, input, select, textarea, script, style, [aria-hidden='true'], .marca, .fita, .veu-boto";
  const BLOC = "h1, h2, h3, h4, p, li, tr, dt, dd, figcaption, div";

  const visible = n => n.checkVisibility ? n.checkVisibility({ visibilityProperty: true })
                                         : n.getClientRects().length > 0;

  function blocs(targeta) {
    const llista = [];
    const del = new Map();
    function afegeix(bloc, peca) {
      if (!del.has(bloc)) { const b = { el: bloc, peces: [] }; del.set(bloc, b); llista.push(b); }
      del.get(bloc).peces.push(peca);
    }
    (function recorre(n) {
      for (const f of n.childNodes) {
        if (f.nodeType === 3) {
          if (f.data.trim()) afegeix(f.parentElement.closest(BLOC) || targeta, { node: f });
        } else if (f.nodeType === 1) {
          if (f.matches(NO_ES_LLEGEIX) || !visible(f)) continue;
          // una fracció o una expressió amb forat: es diu la seva lectura
          if (f.getAttribute("role") === "img") {
            if (f.getAttribute("aria-label")) afegeix(f.matches(BLOC) ? f : (f.parentElement.closest(BLOC) || targeta), { el: f });
            continue;
          }
          recorre(f);
        }
      }
    })(targeta);
    return llista.map(fes).filter(b => b.trossos.length);   // un punt tot sol no es diu
  }

  /** Converteix un bloc en el text que es diu, i recorda d'on surt cada tros. */
  function fes(b) {
    let text = "";
    const trossos = [];
    const posa = (dit, rang) => {
      if (!dit) return;
      if (text) text += " ";
      trossos.push({ ini: text.length, fi: text.length + dit.length, rang });
      text += dit;
    };
    b.peces.forEach(p => {
      if (p.el) {
        const r = document.createRange(); r.selectNodeContents(p.el);
        posa(diu(p.el.getAttribute("aria-label")), r);
        return;
      }
      for (const m of p.node.data.matchAll(/\S+/g)) {
        // un punt o uns dos punts enganxats a la negreta d'abans: «<b>3</b>.»
        if (/^[.,;:!?]+$/.test(m[0]) && !/\s/.test(p.node.data[m.index - 1] || "")) { text += m[0]; continue; }
        const r = document.createRange();
        r.setStart(p.node, m.index); r.setEnd(p.node, m.index + m[0].length);
        posa(diu(m[0]), r);
      }
    });
    return { el: b.el, text, trossos };
  }

  /* --------------------------------------------------------- la marca ---- */
  const potMarcar = !!(window.CSS && CSS.highlights && window.Highlight);
  function marcaParaula(rang) {
    if (!potMarcar) return;
    if (rang) CSS.highlights.set("veu-paraula", new Highlight(rang));
    else CSS.highlights.delete("veu-paraula");
  }
  function marcaBloc(bloc) {
    $$(".veu-bloc").forEach(x => x.classList.remove("veu-bloc"));
    if (bloc) bloc.el.classList.add("veu-bloc");
  }

  /* ------------------------------------------------- llegir i parar ---- */
  let sessio = 0;          // cada lectura té un número: els avisos d'una de vella no fan res
  let boto = null;         // el botó de la targeta que s'està llegint
  let frase = null;        // la frase en curs (si no es guarda, Chrome la perd i no avisa del final)
  let espera = null;

  function para() {
    sessio++;
    clearTimeout(espera);
    if (veu.speaking || veu.pending) veu.cancel();
    frase = null;
    marcaBloc(null); marcaParaula(null);
    if (boto) posaEstat(boto, false);
    boto = null;
  }

  function llegeix(b, targeta) {
    const llegint = boto === b;
    para();
    if (llegint) return;                       // el mateix botó: para i prou
    const cua = blocs(targeta);
    if (!cua.length) return;
    boto = b; posaEstat(b, true);
    const meva = sessio;
    const v = triaVeu();
    let i = 0;
    function seguent() {
      if (meva !== sessio) return;
      if (i >= cua.length) { para(); return; }
      const bloc = cua[i++];
      marcaBloc(bloc); marcaParaula(null);
      const u = new SpeechSynthesisUtterance(bloc.text);
      u.lang = v ? v.lang : "ca-ES";
      if (v) u.voice = v;
      u.rate = VELOCITAT; u.pitch = TO; u.volume = 1;
      u.onboundary = e => {
        if (meva !== sessio || (e.name && e.name !== "word")) return;
        const t = bloc.trossos.find(x => e.charIndex < x.fi);
        marcaParaula(t && t.rang);
      };
      const acaba = () => {
        if (meva !== sessio) return;
        marcaParaula(null);
        espera = setTimeout(seguent, PAUSA);
      };
      u.onend = acaba;
      u.onerror = acaba;
      frase = u;
      veu.speak(u);
    }
    // Chrome, a vegades, perd la primera frase si arriba just després de cancel().
    espera = setTimeout(seguent, 60);
  }

  /* ---------------------------------------------------------- el botó ---- */
  const ICONA_ALTAVEU =
    '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false">' +
    '<path d="M4 9.5h3.2L12 5.6v12.8l-4.8-3.9H4z" fill="currentColor"/>' +
    '<path d="M15.5 9a4.2 4.2 0 0 1 0 6M18 6.6a7.6 7.6 0 0 1 0 10.8" fill="none" stroke="currentColor" ' +
    'stroke-width="1.8" stroke-linecap="round"/></svg>';
  const ICONA_PARA =
    '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false">' +
    '<rect x="6.5" y="6.5" width="11" height="11" rx="2" fill="currentColor"/></svg>';

  function posaEstat(b, llegint) {
    b.innerHTML = llegint ? ICONA_PARA : ICONA_ALTAVEU;
    b.setAttribute("aria-pressed", String(llegint));
    const nom = txt(llegint ? "comu.veu_para" : "comu.veu_escolta").replace(/<[^>]+>/g, "");
    b.setAttribute("aria-label", nom);
    b.title = nom;
  }

  function arrenca() {
    $$(".targeta").forEach(t => {
      if (!t.querySelector("h2") || t.querySelector(":scope > .veu-boto")) return;
      const b = document.createElement("button");
      b.type = "button";
      b.className = "veu-boto";
      posaEstat(b, false);
      b.onclick = () => llegeix(b, t);
      t.insertBefore(b, t.firstChild);
    });
    // Qualsevol altre botó para la veu: la pantalla està a punt de canviar.
    document.addEventListener("click", e => {
      if (boto && e.target.closest("button, a, [role='tab'], .toca") && !e.target.closest(".veu-boto")) para();
    }, true);
    document.addEventListener("visibilitychange", () => { if (document.hidden) para(); });
    window.addEventListener("pagehide", para);
    if (veu.speaking) veu.cancel();          // una lectura que ha quedat d'abans de recarregar
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();

  CE.veu = { para, diu };   // per provar-ho des de la consola i des dels tests
})();
