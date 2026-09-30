/* ============================================================================
   lloc.js · construeix la portada a partir de dades/unitats.js
   ----------------------------------------------------------------------------
   Dues graelles, les targetes de consulta i les set unitats, i el detall de cada
   unitat per al docent (el nucli, el graó físic, el rol a l'aula ordinària, la fita,
   el camí mínim i les regles trencades). Una unitat sense
   fitxa encara surt a la graella, però no s'hi pot clicar. Si la unitat té
   tasques a la caixa d'eines, la targeta ho diu. Cada fitxa porta els seus dos
   PDF: el de l'alumnat i el del solucionari, que fa generadors/gen_pdf.py.
   ========================================================================== */

(function () {
  "use strict";

  /** Crea un node amb classe i contingut HTML ja compost. */
  function fes(etiqueta, classe, html) {
    const n = document.createElement(etiqueta);
    if (classe) n.className = classe;
    if (html != null) n.innerHTML = html;
    return n;
  }

  function graellaTargetes(cont) {
    TARGETES.forEach(function (t) {
      const d = fes("div", "targeta");
      d.innerHTML =
        "<h3>" + t.titol + "</h3>" +
        "<p>" + t.descripcio + "</p>" +
        '<p><a href="' + t.fitxer + '">Obre-la al navegador</a></p>' +
        '<div class="etiquetes"><a class="pdf" href="' + t.pdf + '" download>PDF per imprimir</a></div>';
      cont.appendChild(d);
    });
  }

  /** Els dos PDF d'una fitxa: fitxes/ud1-nombres.html → pdf/ud1-nombres-alumnat.pdf
      i pdf/ud1-nombres-solucionari.pdf. Els noms són els de generadors/gen_pdf.py. */
  function pdfs(f) {
    const base = "pdf/" + f.fitxa.replace(/^fitxes\//, "").replace(/\.html$/, "");
    return '<span class="pdfs-fitxa">' +
      '<a class="pdf petit" href="' + base + '-alumnat.pdf" download ' +
        'aria-label="PDF de l\'alumnat: ' + f.titol + '">PDF</a>' +
      '<a class="pdf petit sol" href="' + base + '-solucionari.pdf" download ' +
        'aria-label="PDF del solucionari: ' + f.titol + '">Solucionari</a>' +
      "</span>";
  }

  function graellaUnitats(cont) {
    UNITATS.forEach(function (u) {
      // Les fitxes de la unitat, en l'ordre de classe. Cada una porta el seu
      // enllaç i els seus dos PDF; per això la targeta no és un enllaç sencer,
      // ni quan la unitat només en té una.
      const fitxes = u.fitxes || (u.fitxa ? [{ fitxa: u.fitxa, titol: u.titol }] : []);
      const una = fitxes.length === 1;
      const d = fes("div", "targeta");
      const llista = fitxes.length
        ? '<ol class="enllacos-fitxes">' + fitxes.map(function (f) {
            return '<li><a href="' + f.fitxa + '">' + f.titol + "</a> " + pdfs(f) +
              (f.estat ? ' <span class="et estat">' + f.estat + "</span>" : "") + "</li>";
          }).join("") + "</ol>"
        : "";
      d.innerHTML =
        '<span class="num">' + u.num + "</span>" +
        "<h3>" + u.titol + "</h3>" +
        "<p>" + u.nucli + "</p>" + llista +
        '<div class="etiquetes">' +
          '<span class="et">' + u.dates + "</span>" +
          (fitxes.length ? '<span class="et fita">' + (una ? "Fitxa feta" : fitxes.length + " fitxes fetes") + "</span>"
                         : '<span class="et">En preparació</span>') +
          (u.tasques ? '<span class="et fita">Caixa d\'eines · tasques ' + u.tasques.join(", ") +
                       "</span>" : "") +
        "</div>";
      cont.appendChild(d);
    });
  }

  /** «1, 2 i 9» */
  const llista = ns => ns.length > 1 ? ns.slice(0, -1).join(", ") + " i " + ns[ns.length - 1] : String(ns[0]);

  /* ---- el detall de cada unitat, per al docent ----
     El camí mínim: les pàgines que són el nucli (minim a dades/unitats.js). La resta és
     ampliació: es fa si hi ha temps, i les regles trencades hi són per als nivells alts. */
  function detallUnitats(cont) {
    UNITATS.forEach(function (u) {
      const fitxes = u.fitxes || [];
      const minim = fitxes.reduce((a, f) => a + (f.minim || []).length, 0);
      const sessions = parseInt(u.sessions, 10);
      const cami = fitxes.length
        ? "<b>" + minim + " pàgines</b> per a " + sessions + " sessions del grup" +
          "<ul class=\"cami\">" + fitxes.map(f =>
            "<li>" + f.titol + ": pàgines " + llista(f.minim || []) + "</li>").join("") + "</ul>"
        : "—";
      const trencades = fitxes.filter(f => f.trencada);
      const d = fes("div", "detall");
      d.innerHTML =
        '<h3 style="margin:0 0 .8rem"><span class="num" style="margin:0 .5rem 0 0">' + u.num +
          "</span>" + u.titol + "</h3>" +
        "<dl>" +
          "<dt>El nucli</dt><dd>" + u.nucli + "</dd>" +
          "<dt>Cinc minuts abans</dt><dd>" + u.material + "</dd>" +
          (u.rol ? "<dt>A l'aula ordinària</dt><dd>" + u.rol + "</dd>" : "") +
          (u.fita ? "<dt>Fita realista</dt><dd>" + u.fita + "</dd>" : "") +
          "<dt>Criteris del grup</dt><dd>" + u.criteris + " (referència: s'avalua amb els del PI)</dd>" +
          "<dt>Camí mínim</dt><dd>" + cami + "</dd>" +
          (trencades.length ? "<dt>Regles trencades</dt><dd><ul class=\"cami\">" + trencades.map(f =>
            "<li>" + f.titol + " · " + f.trencada + "</li>").join("") + "</ul></dd>" : "") +
        "</dl>";
      cont.appendChild(d);
    });
  }

  function arrenca() {
    if (typeof UNITATS === "undefined" || typeof TARGETES === "undefined") {
      console.error("lloc.js: falta dades/unitats.js");
      return;
    }
    const t = document.getElementById("graella-targetes");
    if (t) graellaTargetes(t);
    const u = document.getElementById("graella-unitats");
    if (u) graellaUnitats(u);
    const d = document.getElementById("detall-unitats");
    if (d) detallUnitats(d);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", arrenca);
  else arrenca();
})();
