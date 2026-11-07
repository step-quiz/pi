/* ============================================================================
   comu/js/veu.js · reading each card of the student tools aloud
   ----------------------------------------------------------------------------
   Shared by the tools of every course (CURS/eines.html); it used to be two
   identical copies. Loaded after CURS/js/nucli.js (it uses CE.txt and CE.$$).

   Every card with a title carries, top right, a small button with a speaker.
   Tapping it, the browser reads the card aloud and marks the part being read.
   Tapping it again stops it. Tapping any other button (answering, changing tool
   or exercise) stops it too: the screen is about to change, and the voice must
   not read something that is no longer there.

   It uses the browser's speech synthesis (Web Speech API): no network, no
   server, nothing to install.
   THE BUTTON SHOWS ONLY WITH A CATALAN VOICE (decision I4 of 6/11/2026). Without
   one, the browser read with whatever voice it had, often with a Spanish accent:
   better no button than a bad reading. Browsers give the list of voices late
   (Chrome) or change it (ChromeOS loses language packs with its updates), so it
   is checked again on «voiceschanged» and a little after start.

   HOW IT READS, AND WHY
     · In Catalan (ca-ES), with the best Catalan voice of the computer: first
       the «natural» ones (Edge has two, Joana and Enric), then any other.
     · Slowly: VELOCITAT 0.85, a little below normal (1). Slower, the voice
       drags and sounds odd; faster, there is no time.
     · The natural pitch (TO 1). A higher pitch sounds childish.
     · One block at a time (the title, the instruction, each line of the
       reading, the notice) and a pause between blocks (PAUSA), so that each
       idea arrives alone: the rhythm Lectura Fàcil asks for, one idea per sentence.
     · Always the same and only when asked: nothing speaks by itself when a page
       opens, and there are no reward or error sounds.
     · Symbols are read as words: «3 · 4 = 12» is said «3 per 4 és igual a 12»;
       «7²», «7 al quadrat». Fractions and expressions with a gap carry their
       own reading (aria-label), and that is what is said.
     · Buttons, drawings, the «Exemple» labels and the «Inici» and «Final» of the
       progress rail are not read: only «Pas 2 de 5». A card title hidden because
       the bar already says it (class .repetit, see comu/js/tasca.js) is clipped,
       not removed, so it is still read. But it is MARKED ON THE BAR, where it is
       seen (7/11/2026): the clipped title lies, invisible, on top of the
       instruction, and the yellow band of the title was painted over the
       instruction while the voice said the title; then the instruction started
       and the band started again from its first word. It looked as if the reading
       jumped back. Now its words are taken from the bar title (.sub-rotul, without
       the number «1.1»), and if there is no bar, the title is said with no band.
     · Inputs and drop-downs (6/11/2026). If something is written or chosen, it is
       said in line, as if it were text: «El nombre √7 és entre 2 i 3» is said
       «El nombre l'arrel quadrada de 7 és entre 2 i 3». If they are empty (or the
       drop-down still says «…»), a short pause, with a comma, and no more:
       «El nombre, és entre, i.» Other kinds of field are skipped.

   HOW IT MARKS WHAT IT READS («focus and filling marker», 6/11/2026)
     · FOCUS. While reading, the rest of the card fades (class .veu-apagat,
       opacity 0.3) and the block being read stays as it is (.veu-bloc). It works
       in every browser and with every voice: it is what tells where it reads.
     · FILLING MARKER. If the voice says where it is (Edge and Safari do; Google's
       Android voice and many Chrome voices do not), the line is painted pale
       yellow, continuously, at the pace of the voice: up to the end of the word
       being said, and the word fills slowly while it is said. No rectangle jumps
       from word to word: the teacher asked for a smooth movement, because a jump
       makes the students wait for where the next one will appear instead of
       reading. If the voice does not say where it is, nothing is computed: only
       the focus, which is never wrong.
     · The yellow is a separate layer (.veu-retolador), above the text without
       touching it (mix-blend-mode: multiply), placed with each word's position on
       the page. It used to be CSS.highlights, which cannot be animated
       (23/10/2026: a soft blue nobody saw; then a yellow that jumped).
   ========================================================================== */

(function () {
  "use strict";
  const { $$, txt } = CE;
  const veu = window.speechSynthesis;
  if (!veu || !window.SpeechSynthesisUtterance) return;

  const VELOCITAT = 0.85;
  const TO = 1;
  const PAUSA = 450;   // milliseconds of silence between blocks

  /* --------------------------------------------------------- the voice ---- */
  function triaVeu() {
    const cat = veu.getVoices().filter(v => /^ca\b|^ca[-_]/i.test(v.lang));
    const bona = v => /natural|online|neural|enhanced|premium/i.test(v.name);
    return cat.find(bona) || cat.find(v => v.localService) || cat[0] || null;
  }

  /* -------------------------------------------- from symbols to words --
     Each word on screen is converted on its own. So every piece of what is said
     knows which word on screen it comes from, and can be marked. */
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
      // the raised dot multiplies, except inside a word: «col·lecció»
      .replace(/(?<!\p{L})·|·(?!\p{L})/gu, " per ")
      .replace(/×/g, " per ").replace(/÷/g, " dividit entre ")
      .replace(/(?<=\d)\+(?=\d)/g, " més ").replace(/(?<=\d)-(?=\d)/g, " menys ").replace(/−/g, " menys ")
      .replace(/≈/g, " és aproximadament ").replace(/≤/g, " és més petit o igual que ")
      .replace(/≥/g, " és més gran o igual que ").replace(/=/g, " és igual a ")
      .replace(/…/g, "").replace(/[—–]/g, ", ")
      .replace(/\s+/g, " ").trim();
  }

  /* ------------------------------------------------------ what is read ----
     The blocks of the card, in page order. A block is the nearest block element
     that holds the text. */
  const NO_ES_LLEGEIX = "button, svg, input, select, textarea, script, style, [aria-hidden='true'], .marca, .fita, .veu-boto";
  // The fields that are said (what is written, or a pause when empty). Others are skipped.
  const CAMP = "input[type='text'], input[type='number'], input:not([type]), select";
  const BLOC = "h1, h2, h3, h4, p, li, tr, dt, dd, figcaption, div";

  const visible = n => n.checkVisibility ? n.checkVisibility({ visibilityProperty: true })
                                         : n.getClientRects().length > 0;

  const net = s => s.replace(/\s+/g, " ").trim();

  /** The bar title that shows a clipped card title (.repetit): the visible .sub-rotul
      with the same name. Null if there is none on screen. */
  function rotulDe(h) {
    const nom = net(h.textContent);
    return Array.from(document.querySelectorAll(".sub-rotul"))
      .find(r => visible(r) && net(r.dataset.nom ? r.dataset.nom.replace(/<[^>]+>/g, "") : "") === nom) || null;
  }

  function blocs(targeta) {
    const llista = [];
    const del = new Map();
    function afegeix(bloc, peca) {
      if (!del.has(bloc)) { const b = { el: bloc, peces: [] }; del.set(bloc, b); llista.push(b); }
      del.get(bloc).peces.push(peca);
    }
    (function recorre(n) {
      for (const f of n.childNodes) {
        // The clipped title: said, but marked on the bar title, where it is seen. Its words
        // are the bar's text nodes, without the number in bold («1.1»).
        if (f.nodeType === 1 && f.matches("h2.repetit")) {
          const r = rotulDe(f);
          if (r) {
            const camina = m => { for (const x of m.childNodes) {
              if (x.nodeType === 3) { if (x.data.trim()) afegeix(f, { node: x }); }
              else if (x.nodeType === 1 && x.tagName !== "B" && !x.matches(NO_ES_LLEGEIX)) camina(x);
            } };
            camina(r);
          } else {
            for (const x of f.childNodes) if (x.nodeType === 3 && x.data.trim()) afegeix(f, { node: x, senseMarca: true });
          }
          continue;
        }
        if (f.nodeType === 3) {
          if (f.data.trim()) afegeix(f.parentElement.closest(BLOC) || targeta, { node: f });
        } else if (f.nodeType === 1) {
          if (f.matches(CAMP) && !f.matches("[aria-hidden='true']") && visible(f)) {
            afegeix(f.parentElement.closest(BLOC) || targeta, { camp: f });
            continue;
          }
          if (f.matches(NO_ES_LLEGEIX) || !visible(f)) continue;
          // a fraction or an expression with a gap: its reading is said
          if (f.getAttribute("role") === "img") {
            if (f.getAttribute("aria-label")) afegeix(f.matches(BLOC) ? f : (f.parentElement.closest(BLOC) || targeta), { el: f });
            continue;
          }
          recorre(f);
        }
      }
    })(targeta);
    return llista.map(fes).filter(b => b.trossos.length);   // a full stop alone is not said
  }

  /** What is said of a field: what is written or chosen, in words; empty if nothing. */
  function diuCamp(c) {
    if (c.tagName === "SELECT") return c.value === "" ? "" : diu((c.selectedOptions[0] || {}).text || "");
    let v = c.value.trim();
    if (c.type === "number") v = v.replace(/(\d)\.(\d)/g, "$1,$2");   // 8.5 → 8,5, as it is written here
    return diu(v);
  }

  /** Turns a block into the text that is said, and remembers where each piece comes from. */
  function fes(b) {
    let text = "";
    let pausa = false;      // an empty field came before: the next word goes after a comma
    const trossos = [];
    const posa = (dit, rang, camp) => {
      if (!dit) return;
      if (text) text += (pausa && !/[.,;:!?]$/.test(text)) ? ", " : " ";
      pausa = false;
      trossos.push({ ini: text.length, fi: text.length + dit.length, rang, camp });
      text += dit;
    };
    b.peces.forEach(p => {
      if (p.camp) {
        const dit = diuCamp(p.camp);
        if (!dit) { if (text) pausa = true; return; }
        const r = document.createRange(); r.selectNode(p.camp);
        posa(dit, r, p.camp);
        return;
      }
      if (p.el) {
        const r = document.createRange(); r.selectNodeContents(p.el);
        posa(diu(p.el.getAttribute("aria-label")), r);
        return;
      }
      for (const m of p.node.data.matchAll(/\S+/g)) {
        // a full stop or a colon stuck to the bold before it: «<b>3</b>.»
        if (/^[.,;:!?]+$/.test(m[0]) && !/\s/.test(p.node.data[m.index - 1] || "")) { text += m[0]; pausa = false; continue; }
        const r = document.createRange();
        r.setStart(p.node, m.index); r.setEnd(p.node, m.index + m[0].length);
        posa(diu(m[0]), r);
      }
    });
    return { el: b.el, text, trossos, senseMarca: b.peces.some(p => p.senseMarca) };
  }

  /* -------------------------------------------------------- the mark ---- */
  const quiet = () => window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* THE FOCUS: everything in the card fades except the path to the block being read
     (the siblings of each ancestor) and the speaker button. */
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

  /* THE FILLING MARKER: one yellow band per line, from the start of the block to the
     end of the word being said. The band of the last line grows during the time the
     word takes (linear transition), and the next word finds it wherever it is. */
  const capa = document.createElement("div");
  capa.className = "veu-capa";
  capa.setAttribute("aria-hidden", "true");
  let franges = [];

  function rectes(trossos) {
    // The boxes of the words, grouped by line: [{l, t, r, b}] in page coordinates.
    // An input is taller than the letters: its whole width counts, but only the height of one
    // line of text in its middle, so that the band does not suddenly grow when it gets there.
    const linies = [];
    trossos.forEach(({ rang, camp }) => {
      const mig = camp ? parseFloat(getComputedStyle(camp.parentElement).fontSize) * 0.62 : 0;
      for (const c of rang.getClientRects()) {
        if (!c.width) continue;
        const y = (c.top + c.bottom) / 2;
        const caixa = { l: c.left + scrollX, r: c.right + scrollX,
                        t: (camp ? y - mig : c.top) + scrollY, b: (camp ? y + mig : c.bottom) + scrollY };
        const l = linies.find(x => Math.abs((x.t + x.b) / 2 - (caixa.t + caixa.b) / 2) < (caixa.b - caixa.t) / 2);
        if (l) { l.l = Math.min(l.l, caixa.l); l.r = Math.max(l.r, caixa.r); l.t = Math.min(l.t, caixa.t); l.b = Math.max(l.b, caixa.b); }
        else linies.push(caixa);
      }
    });
    return linies;
  }

  function omple(bloc, fins, durada) {
    if (!capa.isConnected) document.body.appendChild(capa);
    const linies = rectes(bloc.trossos.slice(0, fins + 1).filter(t => t.rang));
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
      f.getBoundingClientRect();                   // so that the transition starts from where it is now
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

  /* The time a word takes: at 0.85 speed, about 75 ms per letter. It only stretches
     the band while the word is said; the next word puts it back in place. */
  const temps = dit => Math.max(180, Math.min(1400, (dit || "").length * 75));

  function apaga() {
    focus(null);
    esborra();
    targetaActiva = null;
    setTimeout(() => { if (!targetaActiva) $$(".veu-fos").forEach(x => x.classList.remove("veu-fos")); }, 400);
  }

  /* --------------------------------------------- reading and stopping ---- */
  let sessio = 0;          // each reading has a number: events of an old one do nothing
  let boto = null;         // the button of the card being read
  let frase = null;        // the utterance in progress (if not kept, Chrome loses it and never says it ended)
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
    if (llegint) return;                       // the same button: stop, and no more
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
        if (meva !== sessio || bloc.senseMarca || (e.name && e.name !== "word")) return;
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
    // Chrome sometimes loses the first utterance if it comes right after cancel().
    espera = setTimeout(seguent, 60);
  }

  /* -------------------------------------------------------- the button ---- */
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

  /* Shows or hides every speaker button, depending on whether there is a Catalan
     voice now (I4). A reading in progress is stopped if the voice goes away. */
  function mostraBotons() {
    const hiEs = !!triaVeu();
    $$(".veu-boto").forEach(b => { if (b.hidden === hiEs) b.hidden = !hiEs; });
    if (!hiEs && boto) para();
  }

  function arrenca() {
    $$(".targeta").forEach(t => {
      if (!t.querySelector("h2") || t.querySelector(":scope > .veu-boto")) return;
      const b = document.createElement("button");
      b.type = "button";
      b.className = "veu-boto";
      b.hidden = true;                         // until a Catalan voice is found
      posaEstat(b, false);
      b.onclick = () => llegeix(b, t);
      t.insertBefore(b, t.firstChild);
    });
    mostraBotons();
    if (veu.addEventListener) veu.addEventListener("voiceschanged", mostraBotons);
    setTimeout(mostraBotons, 800);
    setTimeout(mostraBotons, 3000);
    // Any other button stops the voice: the screen is about to change.
    document.addEventListener("click", e => {
      if (boto && e.target.closest("button, a, [role='tab'], .toca") && !e.target.closest(".veu-boto")) para();
    }, true);
    document.addEventListener("visibilitychange", () => { if (document.hidden) para(); });
    window.addEventListener("pagehide", para);
    window.addEventListener("resize", esborra);
    if (veu.speaking) veu.cancel();          // a reading left over from before a reload
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();

  CE.veu = { para, diu, blocs, amb: () => !!triaVeu() };   // for the console and the tests
})();
