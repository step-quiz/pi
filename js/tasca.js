/* ============================================================================
   tasca.js · les tasques amb passos
   ----------------------------------------------------------------------------
   Una tasca és una seqüència tancada: té un inici que es veu, un nombre de
   passos que se sap des del principi, un sol pas a la vista i un final que diu
   «Has acabat». Per a aquest alumnat això no és un detall de presentació: saber
   quant falta i quan s'ha acabat treu càrrega, i la càrrega és el coll
   d'ampolla, no la comprensió.

   AQUEST FITXER FA, PERQUÈ CAP MÒDUL NO HO HAGI DE REPETIR
     · el rètol de progrés:   Inici ● ● ○ ○ ○ Final   «Pas 2 de 5»
     · el progrés desat al navegador i la pregunta de si es continua;
     · el final: «Has acabat», el resum i el codi de verificació (js/codi.js);
     · la retroacció literal: «Correcte.» / «Incorrecte. Ara provem-ho d'una
       altra manera.» + una pista que obre un camí diferent.

   EL MÒDUL NOMÉS DIU
     · quants passos té la tasca i com es pinta el pas i;
     · quan un pas queda resolt i com: CE.tasca(...).anota("be" | "pista" | "mostrat").

   ÚS MÍNIM
     const t = CE.tasca({
       tasca: 1, sub: 2,                    // el número de ?task=1.2
       recorregut: $("#x-recorregut"),      // on va el rètol de progrés
       represa: $("#x-represa"),            // on va la pregunta de continuar
       final: $("#x-final"),                // on va el resum
       cos: [$("#x-cos")],                  // el que s'amaga mentre surt la represa
       nom: estat => "Situa el nombre",     // per al resum
       pinta: (i, estat) => { ... }         // ensenya el pas i
     });
     t.inicia(() => ({ total: 5, cas: 0, extra: {...} }));

   EL PROGRÉS DESAT
   Va a localStorage (dins de CE.memoria, que ja està protegit) amb la clau
   «pi-tasca:1.2». Al cap de 30 dies es descarta. Com que un ordinador de
   l'aula el fan servir moltes persones, mai no es reprèn sol: sempre es
   pregunta, amb el dia en què es va desar. Això val també als enllaços ?task=,
   on app.js no recorda el mòdul obert per la mateixa raó.
   ========================================================================== */

(function () {
  "use strict";
  const { txt, memoria, diaLlarg } = CE;

  /* ================================================== retroacció literal == */

  const CLASSE = { encert: "be", be: "be", error: "pensa", mostra: "pensa", no: "pensa",
                   info: "neutre" };

  /** Escriu la retroacció en un avís, sempre amb la mateixa forma.
       encert → «Correcte.» i què ha passat
       error  → «Incorrecte.» + «Ara provem-ho d'una altra manera.» + la pista
       mostra → «Incorrecte.» i la resposta, quan ja no queden intents
       be     → un estat bo que no és una resposta («x = 4 és una solució»)
       no     → un estat que no és el bo i que tampoc no és una resposta
                («x = 2 no és una solució»): sense «Incorrecte», perquè provar
                un valor a la balança no és contestar
       info   → una indicació neutra
     La paraula «Incorrecte» hi és a posta: una resposta equivocada es diu
     clarament, sense eufemismes. El que suavitza és el que ve després, que no
     repeteix la consigna sinó que proposa un camí diferent. */
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
  }

  /* ============================================== tasques amb passos == */

  const CADUCA = 30 * 86400000;          // un progrés de fa més d'un mes ja no es proposa
  const clau = cfg => "pi-tasca:" + cfg.tasca + (cfg.sub ? "." + cfg.sub : "");

  function tasca(cfg) {
    const comptador = cfg.comptador || "comu.pas";
    const cos = cfg.cos || [];
    let estat = null;      // { cas, total, pas, res[], extra{}, acabada }
    let fesNou = null;     // retorna { total, cas, extra } per començar de zero

    /* ---- el rètol de progrés ---- */
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

    /* ---- el progrés desat ---- */
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
        // sense cap pas fet no hi ha res a continuar: millor començar sense preguntar
        if (!e.res.some(r => r != null && r !== "exemple")) return null;
        return e;
      } catch (err) {
        return null;                                  // un JSON trencat no ha de parar l'app
      }
    }

    /* ---- el pas visible ---- */
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

    /** Comença de zero. Accepta les dades, o una funció que les retorna; en el
        segon cas, aquesta funció passa a ser la de «Torna a començar», i és el
        lloc on el mòdul posa a zero el que és seu (les proves, el valor de x…). */
    function comenca(dades) {
      if (typeof dades === "function") fesNou = dades;
      const d = (typeof dades === "function" ? dades() : dades) || fesNou();
      estat = { cas: d.cas || 0, total: d.total, pas: 0,
                res: new Array(d.total).fill(null), extra: d.extra || {}, acabada: false };
      if (d.resultats) d.resultats.forEach((r, i) => { estat.res[i] = r; });
      if (d.pas) estat.pas = d.pas;
      mostraPas();
    }

    /** El punt d'entrada: si hi ha una tasca a mitges, pregunta; si no, comença. */
    function inicia(nou) {
      fesNou = nou;
      const desat = llegeixDesat();
      if (desat) ofereixRepresa(desat);
      else comenca();
    }

    function ofereixRepresa(desat) {
      if (!cfg.represa) { comenca(); return; }
      cos.forEach(c => { c.hidden = true; });
      if (rail) rail.hidden = true;                  // una sola cosa a la vista: la pregunta
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

    /* ---- avançar ---- */
    function anota(resultat) {
      estat.res[estat.pas] = resultat;
      pintaRecorregut();
      desa();
    }
    const resolt = () => !!estat && estat.res[estat.pas] != null;
    const esUltim = () => !!estat && estat.pas === estat.total - 1;

    function seguent() {
      if (!estat || estat.acabada) return;
      if (estat.pas < estat.total - 1) { estat.pas++; mostraPas(); }
      else acaba();
    }
    function enrere() {
      if (estat && !estat.acabada && estat.pas > 0) { estat.pas--; mostraPas(); }
    }

    /* ---- el final ----
       `pendents` omple els passos que no s'han fet: «Mostra-ho tot» acaba la
       tasca amb acaba("mostrat"), i el resum ho diu tal com ha anat. */
    function acaba(pendents) {
      if (pendents) estat.res = estat.res.map(r => (r == null ? pendents : r));
      estat.acabada = true;
      desa();                                          // en acabar, s'esborra
      pintaRecorregut();
      if (cfg.amagaEnAcabar !== false) cos.forEach(c => { c.hidden = true; });
      if (cfg.enAcabar) cfg.enAcabar(estat);
      pintaFinal();
    }

    /** El resum que val per a gairebé totes les tasques: passos, encerts al
        primer intent, amb pista i amb la resposta ensenyada. Un mòdul que compti
        una altra cosa (l'equació compta solucions i proves) en porta un de propi. */
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
      // el focus va al resum perquè el lector de pantalla el digui, i es fa
      // visible sense saltar si ja ho és
      f.focus({ preventScroll: true });
      if (f.scrollIntoView) f.scrollIntoView({ block: "nearest" });
    }

    return { inicia, comenca, anota, resolt, esUltim, seguent, enrere, acaba,
             pintaRecorregut, estat: () => estat };
  }

  /** Imprimeix només el resum. Se'n posa una còpia a #zona-impressio, fill
      directe del <body>, i una classe al <body> fa que el @media print d'app.css
      amagui tota la resta. Una còpia i no l'original, perquè el resum és dins
      de targetes i mòduls que s'han d'amagar. */
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
    // Hi ha navegadors (Safari a l'iPad) que imprimeixen sense bloquejar i no
    // sempre avisen en acabar. Llavors es neteja al gest següent: treure la
    // classe abans que el diàleg hagi llegit la pàgina imprimiria la caixa sencera.
    setTimeout(() => {
      window.addEventListener("pointerdown", neteja, { once: true });
      window.addEventListener("keydown", neteja, { once: true });
    }, 0);
    window.print();
  }

  /** Barreja una llista sense tocar l'original (Fisher-Yates). */
  function barreja(llista) {
    const c = llista.slice();
    for (let i = c.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [c[i], c[j]] = [c[j], c[i]];
    }
    return c;
  }

  Object.assign(CE, { tasca, retroaccio, barreja });
})();
