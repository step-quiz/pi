/* ============================================================================
   comu/js/unitat.js · la pàgina d'una unitat (1eso/unitat.html, 4eso/unitat.html)
   ----------------------------------------------------------------------------
   unitat.html?ud=N ensenya tres opcions per a la unitat N del curs:

     Fitxes d'activitats   les fitxes de la unitat (menys la de repàs)
     Quadern d'activitats  el quadern de la unitat (camp quadern), o apagat si no n'hi ha
                           (aquestes dues, en una sola bombolla: fitxes a l'esquerra, quadern a la dreta)
     Caixa d'eines         la caixa amb només les eines de la unitat (camp tasques):
                           caixa-eines.html?ud=N&tasques=0,2,4 (a sota de la bombolla)
     Més eines             desplegable, sempre plegat: la fitxa de repàs i les targetes de consulta
     Per al professorat    desplegable, sempre plegat: el detall de la unitat

   Cada fitxa, targeta i quadern és un botó que porta a la seva pàgina; els PDF no es ressenyen
   aquí, es baixen des de la fitxa.
   Les dades són les de dades/unitats.js del curs. Els dos cursos no les escriuen
   igual: a 1eso/ cada unitat té una llista de fitxes (camp fitxes); a 4eso/, una
   fitxa (fitxa) i la de repàs (tancament). Aquí es llegeixen totes dues formes.

   L'ESQUEMA DE NAVEGACIÓ (5/11/2026, per encàrrec del docent). Sempre tres nivells:
     1. curs         la portada de l'arrel (index.html)
     2. unitat       aquesta pàgina (unitat.html?ud=N)
     3. fitxa, quadern o caixa d'eines
   Tot el que és del tercer nivell torna a la unitat («← unitat N»), i la unitat torna a
   la portada. No hi ha pàgines planes que se saltin la unitat: les targetes de consulta
   (camp unitat o unitats de TARGETES) i el detall per al docent són aquí. Les targetes
   s'obren amb ?ud=N, perquè una targeta de més d'una unitat sàpiga a quina torna
   (comu/js/torna.js).
   ========================================================================== */

(function () {
  "use strict";

  function fitxesDe(u) {
    if (Array.isArray(u.fitxes)) return u.fitxes.map(f => ({ fitxa: f.fitxa, titol: f.titol }));
    const l = [];
    if (u.fitxa) l.push({ fitxa: u.fitxa, titol: "Fitxa de la unitat" });
    if (u.tancament) l.push({ fitxa: u.tancament, titol: "Fitxa de repàs" });
    return l;
  }

  /** Un enllaç de la unitat, com un botó. El PDF de l'alumnat i el del solucionari es baixen des
      de la barra de dalt de la mateixa fitxa: aquí no hi són (6/11/2026, per encàrrec del docent). */
  function fitxa(f) {
    return '<li><a class="enllac" href="' + f.fitxa + '">' + f.titol + "</a></li>";
  }

  /** Les targetes de consulta de la unitat. A 1eso/ cada targeta té una unitat (unitat);
      a 4eso/ pot tenir-ne més d'una (unitats). Els camps tampoc es diuen igual. */
  function targetesDe(u) {
    return (window.TARGETES || []).filter(t =>
      (Array.isArray(t.unitats) ? t.unitats : [t.unitat]).includes(u.num)).map(t => ({
        fitxa: (t.fitxer || "targetes/" + t.nom + ".html") + "?ud=" + u.num,
        titol: t.titol,
        text: t.descripcio || t.per || ""
      }));
  }

  function targeta(t) {
    return '<li><a class="enllac" href="' + t.fitxa + '" title="' + t.text.replace(/"/g, "&quot;") + '">' +
      t.titol + "</a></li>";
  }

  /** «1, 2 i 9» */
  const llista = ns => ns.length > 1 ? ns.slice(0, -1).join(", ") + " i " + ns[ns.length - 1] : String(ns[0]);

  /* ---- el detall per al docent (abans era a fitxes.html, que ja no hi és) ---- */
  function filesDetall(u) {
    const f = [];
    const afegeix = (dt, dd) => { if (dd) f.push("<dt>" + dt + "</dt><dd>" + dd + "</dd>"); };
    if (Array.isArray(u.fitxes)) {                       // la forma de 1eso/
      const fitxes = u.fitxes;
      const minim = fitxes.reduce((a, x) => a + (x.minim || []).length, 0);
      const trencades = fitxes.filter(x => x.trencada);
      afegeix("El nucli", u.nucli);
      afegeix("Cinc minuts abans", u.material);
      afegeix("A l'aula ordinària", u.rol);
      afegeix("Fita realista", u.fita);
      afegeix("Criteris del grup", u.criteris + " (referència: s'avalua amb els del PI)");
      afegeix("Dates", u.dates + " · " + u.sessions + " sessions del grup");
      afegeix("Camí mínim", fitxes.length
        ? "<b>" + minim + " pàgines</b> per a " + parseInt(u.sessions, 10) + " sessions del grup" +
          '<ul class="cami">' + fitxes.map(x => "<li>" + x.titol + ": pàgines " + llista(x.minim || []) +
            (x.estat ? ' <span class="et estat">' + x.estat + "</span>" : "") + "</li>").join("") + "</ul>"
        : "");
      afegeix("Regles trencades", trencades.length
        ? '<ul class="cami">' + trencades.map(x => "<li>" + x.titol + " · " + x.trencada + "</li>").join("") + "</ul>"
        : "");
    } else {                                             // la forma de 4eso/
      const nom = m => (window.MODULS && window.MODULS[m]) || m;
      afegeix("Dates", u.dates + " · " + u.sessions + " sessions");
      afegeix("Objectiu nuclear", u.objectiu);
      afegeix("Cinc minuts abans", u.material);
      afegeix("La regla trencada", u.trencada);
      afegeix("Fita realista", u.fita);
      afegeix("Caixa d'eines", (u.moduls || []).length
        ? u.moduls.map(nom).join(", ") : "cap; l'eina d'aquesta unitat és el full de càlcul");
      afegeix("Llibre digital", u.llibre ? "<code>" + u.llibre + "</code>" : "");
      afegeix("repas-main", u.repas ? u.repas + (u.evitar ? ' <span class="et avis">no obrir: ' + u.evitar + "</span>" : "") : "");
    }
    return "<dl>" + f.join("") + "</dl>";
  }

  const ICONA = {
    fitxes: '<path d="M8 4h11l7 7v17a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/><path d="M19 4v7h7"/>' +
            '<path d="M11 17h10M11 21.5h10M11 26h6"/>',
    quadern: '<path d="M9 4h16a2 2 0 0 1 2 2v20a2 2 0 0 1-2 2H9z"/><path d="M9 4H7a2 2 0 0 0-2 2v20a2 2 0 0 0 2 2h2"/>' +
             '<path d="M14 11h8M14 15.5h8M14 20h5"/>',
    caixa: '<path d="M4 13h24v13a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/><path d="M11 13V9a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v4"/>' +
           '<path d="M4 19h7M21 19h7"/><rect x="13" y="18.5" width="6" height="5" rx="1"/>'
  };
  const icona = nom => '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.2" ' +
    'stroke-linejoin="round" stroke-linecap="round" aria-hidden="true">' + ICONA[nom] + "</svg>";

  /** El quadern, a la dreta de la bombolla: un enllaç, o apagat si encara no n'hi ha. */
  function quadern(href) {
    const cos = icona("quadern") + "<h2>Quadern d'activitats</h2>";
    return href
      ? '<a class="quadern" href="' + href + '">' + cos + "<p>Per practicar després de la fitxa.</p></a>"
      : '<div class="quadern apagat">' + cos + "<p>Encara no n'hi ha.</p></div>";
  }

  /** La caixa d'eines, a sota de la bombolla: un enllaç, o apagada si la unitat no té tasques. */
  function caixa(href) {
    const cos = icona("caixa") + "<div><h2>Caixa d'eines</h2><p>" +
      (href ? "Només les eines d'aquesta unitat." : "Encara no n'hi ha.") + "</p></div>";
    return href ? '<a class="caixa" href="' + href + '">' + cos + "</a>"
                : '<div class="caixa apagada">' + cos + "</div>";
  }

  const esRepas = f => /-repas\.html$/.test(f.fitxa);
  const llistaFitxes = fs => '<ul class="fitxes">' + fs.map(fitxa).join("") + "</ul>";

  function arrenca() {
    const n = Number(new URLSearchParams(location.search).get("ud"));
    const u = (window.UNITATS || []).find(x => x.num === n);
    const titol = document.getElementById("titol");
    const opcions = document.getElementById("opcions");
    if (!u) {
      titol.textContent = "Aquesta unitat no existeix";
      opcions.innerHTML = '<p><a class="torna-boto" href="../index.html">← inici</a> Tria una unitat.</p>';
      return;
    }
    titol.textContent = "Unitat " + u.num + " · " + u.titol;
    document.title = "Unitat " + u.num + " · " + u.titol + " · " + document.body.dataset.materia;

    const fitxes = fitxesDe(u);
    const principals = fitxes.filter(f => !esRepas(f));
    const repassos = fitxes.filter(esRepas);
    const targetes = targetesDe(u);
    const tasques = Array.isArray(u.tasques) ? u.tasques : [];

    // 1. Una sola bombolla: les fitxes d'activitats a l'esquerra, el quadern a la dreta.
    // 2. La caixa d'eines, a sota.
    // 3. «Més eines», plegat: la fitxa de repàs i les targetes de consulta.
    const mes = (repassos.length ? "<h3>Fitxa de repàs</h3>" + llistaFitxes(repassos) : "") +
                (targetes.length ? "<h3>Targetes de consulta</h3>" +
                  '<ul class="fitxes">' + targetes.map(targeta).join("") + "</ul>" : "");
    opcions.innerHTML =
      '<div class="bombolla">' +
        '<section><h2>' + icona("fitxes") + "Fitxes d'activitats</h2>" +
          (principals.length ? llistaFitxes(principals) : "<p>Encara no n'hi ha.</p>") + "</section>" +
        quadern(u.quadern) +
      "</div>" +
      caixa(tasques.length ? "caixa-eines.html?ud=" + u.num + "&tasques=" + tasques.join(",") : "") +
      (mes ? '<details class="desplegable mes-eines"><summary>Més eines</summary>' + mes + "</details>" : "");

    // El detall per al docent: un altre desplegable, sempre plegat. El text general és a unitat.html.
    const docent = document.getElementById("docent");
    const detall = document.getElementById("detall-unitat");
    if (docent && detall) {
      detall.innerHTML = filesDetall(u);
      docent.hidden = false;
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();
})();
