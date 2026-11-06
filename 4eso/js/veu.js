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

   COM MARCA EL QUE LLEGEIX («focus i retolador que omple», 6/11/2026)
     · FOCUS. Mentre llegeix, la resta de la targeta s'apaga (classe .veu-apagat,
       opacitat 0,3) i el bloc que sona es queda tal com és (.veu-bloc). Funciona
       a tots els navegadors i amb totes les veus: és el que diu on es llegeix.
     · RETOLADOR QUE OMPLE. Si la veu diu per on va (Edge i Safari ho fan; la veu
       de Google d'Android i moltes de Chrome, no), la línia es va pintant de groc
       clar, contínua, al ritme de la veu: fins al final de la paraula que sona, i
       la paraula s'omple a poc a poc mentre es diu. No hi ha cap rectangle que
       salti d'una paraula a l'altra: el docent va demanar que el pas fos suau,
       perquè un salt fa que l'alumnat estigui pendent d'on sortirà el següent, i
       no llegeixi. Si la veu no diu per on va, no es calcula res: només el focus,
       que no s'equivoca mai.
     · El groc és una capa a part (.veu-retolador), a sobre del text i sense tocar-lo
       (mix-blend-mode: multiply), amb la posició de cada paraula a la pàgina. Abans
       es feia amb CSS.highlights, que no es pot animar (23/10/2026: un blau suau
       que no es veia; després, un groc que saltava de paraula en paraula).
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
  const quiet = () => window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* EL FOCUS: s'apaga tot el que hi ha a la targeta menys el camí fins al bloc que sona
     (els germans de cada avantpassat) i el botó de l'altaveu. */
  let targetaActiva = null;
  function focus(bloc) {
    $$(".veu-bloc").forEach(x => x.classList.remove("veu-bloc"));
    $$(".veu-apagat").forEach(x => x.classList.remove("veu-apagat"));
    if (!bloc || !targetaActiva) return;
    bloc.el.classList.add("veu-bloc");
    for (let n = bloc.el; n && n !== targetaActiva; n = n.parentElement) {
      for (const g of n.parentElement ? n.parentElement.children : []) {
        if (g !== n && !g.classList.contains("veu-boto")) g.classList.add("veu-apagat", "veu-fos");
      }
    }
  }

  /* EL RETOLADOR QUE OMPLE: una franja groga per línia, del principi del bloc fins al
     final de la paraula que sona. La de l'última línia s'allarga durant el temps que
     es triga a dir la paraula (transició lineal), i la següent paraula la retroba on sigui. */
  const capa = document.createElement("div");
  capa.className = "veu-capa";
  capa.setAttribute("aria-hidden", "true");
  let franges = [];

  function rectes(rangs) {
    // Les caixes de les paraules, agrupades per línia: [{l, t, r, b}] en coordenades de la pàgina.
    const linies = [];
    rangs.forEach(r => {
      for (const c of r.getClientRects()) {
        if (!c.width) continue;
        const caixa = { l: c.left + scrollX, t: c.top + scrollY, r: c.right + scrollX, b: c.bottom + scrollY };
        const l = linies.find(x => Math.abs((x.t + x.b) / 2 - (caixa.t + caixa.b) / 2) < (caixa.b - caixa.t) / 2);
        if (l) { l.l = Math.min(l.l, caixa.l); l.r = Math.max(l.r, caixa.r); l.t = Math.min(l.t, caixa.t); l.b = Math.max(l.b, caixa.b); }
        else linies.push(caixa);
      }
    });
    return linies;
  }

  function omple(bloc, fins, durada) {
    if (!capa.isConnected) document.body.appendChild(capa);
    const linies = rectes(bloc.trossos.slice(0, fins + 1).map(t => t.rang).filter(Boolean));
    while (franges.length < linies.length) {
      const f = document.createElement("div");
      f.className = "veu-retolador";
      f.style.width = "0px";
      capa.appendChild(f);
      franges.push(f);
    }
    linies.forEach((l, i) => {
      const f = franges[i], ultima = i === linies.length - 1;
      const amplada = (l.r - l.l + 4) + "px";
      Object.assign(f.style, { left: (l.l - 2) + "px", top: l.t + "px", height: (l.b - l.t) + "px" });
      f.style.transition = ultima && !quiet() ? "width " + durada + "ms linear, opacity .3s" : "none";
      f.getBoundingClientRect();                   // perquè la transició comenci des d'on és ara
      f.style.width = amplada;
      f.style.opacity = "1";
    });
  }

  function esborra() {
    franges.forEach(f => { f.style.transition = "opacity .3s"; f.style.opacity = "0"; });
    const velles = franges;
    franges = [];
    setTimeout(() => velles.forEach(f => f.remove()), 350);
  }

  /* El temps que es triga a dir una paraula: a 0,85 de velocitat, uns 75 ms per lletra.
     Només serveix per allargar la franja mentre es diu; la paraula següent la torna a posar al lloc. */
  const temps = dit => Math.max(180, Math.min(1400, (dit || "").length * 75));

  function apaga() {
    focus(null);
    esborra();
    targetaActiva = null;
    setTimeout(() => { if (!targetaActiva) $$(".veu-fos").forEach(x => x.classList.remove("veu-fos")); }, 400);
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
    apaga();
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
    targetaActiva = targeta;
    const meva = sessio;
    const v = triaVeu();
    let i = 0;
    function seguent() {
      if (meva !== sessio) return;
      if (i >= cua.length) { para(); return; }
      const bloc = cua[i++];
      esborra();
      focus(bloc);
      const u = new SpeechSynthesisUtterance(bloc.text);
      u.lang = v ? v.lang : "ca-ES";
      if (v) u.voice = v;
      u.rate = VELOCITAT; u.pitch = TO; u.volume = 1;
      u.onboundary = e => {
        if (meva !== sessio || (e.name && e.name !== "word")) return;
        const k = bloc.trossos.findIndex(x => e.charIndex < x.fi);
        if (k >= 0) omple(bloc, k, temps(bloc.text.slice(bloc.trossos[k].ini, bloc.trossos[k].fi)));
      };
      const acaba = () => {
        if (meva !== sessio) return;
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
    window.addEventListener("resize", esborra);
    if (veu.speaking) veu.cancel();          // una lectura que ha quedat d'abans de recarregar
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();

  CE.veu = { para, diu };   // per provar-ho des de la consola i des dels tests
})();
