/* ============================================================================
   comu/js/alumne.js · the closed header of the student tools (CURS/eines.html)
   ----------------------------------------------------------------------------
   The students open the tools only through the link the teacher sends
   (CURS/eines?u=N). Their page is a closed space: no link to the rest of the
   site, which holds the answer keys (decision F1, confirmed on 6/11/2026).

   This script runs after dades/unitats.js and BEFORE the course's js/app.js:
     · it reads ?u=N and leaves the unit in PI.einesUnitat (null if there is none);
     · it writes «Unitat N · title» in the header #w-cap-alumne.
   js/app.js then shows only the tools of that unit (the field «tasques»).
   ========================================================================== */

(function () {
  "use strict";
  const PI = window.PI = window.PI || {};
  const n = Number(new URLSearchParams(location.search).get("u"));
  const u = (window.UNITATS || []).find(x => x.num === n) || null;
  PI.einesUnitat = u;
  const cap = document.getElementById("w-cap-alumne");
  if (!cap) return;
  const icona = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" ' +
    'stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="12" rx="2"/>' +
    '<path d="M8 21h8M12 17v4M7 13l3-3 2 2 4-4"/></svg>';
  const text = u ? "Unitat " + u.num + " · " + u.titol : "Eines";
  cap.innerHTML = icona + "<span></span>";
  cap.querySelector("span").textContent = text;
  document.title = u ? "Eines · Unitat " + u.num : "Eines";
})();
