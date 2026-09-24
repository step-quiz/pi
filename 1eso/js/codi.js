/* ============================================================================
   codi.js · el codi de verificació que surt en acabar una tasca
   ----------------------------------------------------------------------------
   Còpia del de la caixa de 4eso/, amb una sola diferència: la SAL. És el que
   fa que un codi d'aquesta caixa no sigui vàlid a l'altra, i a l'inrevés.

   PER QUÈ UN CODI
   L'alumnat acaba una tasca a la caixa d'eines i el docent n'ha de poder tenir
   l'evidència sense servidor, sense comptes i sense guardar cap nom. El codi
   porta a dins la tasca, el dia i els resultats, i verifica.html el llegeix.
   És el mateix format d'evidència que ja fa servir repas-main.

   COM ÉS
   Nou caràcters en tres grups de tres: «K7Q-M2X-9RT». L'alfabet és el Base32
   de Crockford, que no té I, L, O ni U: són les lletres que es confonen amb
   1, 0 i V quan es copien a mà. Si algú escriu una O o una I, es llegeix com a
   0 o 1, perquè és el que volia dir.

   QUÈ HI HA A DINS (45 bits)
     versió  2 bits   0-3       per poder canviar el format sense trencar res
     tasca   4 bits   0-15      el número de ?task=
     sub     3 bits   0-7       la subtasca (0 si no n'hi ha)
     cas     3 bits   0-7       el cas triat dins del mòdul
     dia     9 bits   0-511     dies des de l'1 de setembre del curs
     a, b, c 5 bits   0-31      tres recomptes; què vol dir cadascun ho diu
                                el catàleg de cada mòdul (CE.cataleg)
     control 9 bits             detecta una xifra mal copiada

   Abans d'escriure'l, la càrrega es barreja amb una màscara que surt del
   control. Sense això, els codis de la mateixa tasca començaven tots igual
   («000-…» a la Calculadora) i semblaven un error. La barreja es desfà en
   llegir-lo, perquè el control viatja sense barrejar.

   QUÈ NO ÉS
   No és xifratge. Qui llegeixi aquest fitxer pot fabricar un codi vàlid. Serveix
   per detectar errors de còpia i per fer que canviar-ne un caràcter a l'atzar
   no passi (hi ha 1 possibilitat entre 512). Per a l'ús que té, n'hi ha prou.
   ========================================================================== */

(function () {
  "use strict";

  const ALFABET = "0123456789ABCDEFGHJKMNPQRSTVWXYZ";   // Crockford, sense I L O U
  // Una altra sal que la de l'altra caixa d'eines: les dues es publiquen al
  // mateix domini, i sense això un codi de l'una es llegiria com a vàlid a
  // l'altra. Canviar-la invalida tots els codis que ja s'hagin donat.
  const SAL = "pi.step-quiz · caixa d'eines · quadrícula";
  const VERSIO = 0;

  // Mida de cada camp, en l'ordre en què s'empaqueten.
  const CAMPS = [["versio", 4], ["tasca", 16], ["sub", 8], ["cas", 8],
                 ["dia", 512], ["a", 32], ["b", 32], ["c", 32]];
  const CONTROL = 512;

  /** FNV-1a de 32 bits: petit, sense dependències i prou bo per a un control. */
  function fnv(text) {
    let h = 0x811c9dc5;
    for (let i = 0; i < text.length; i++) {
      h ^= text.charCodeAt(i);
      h = Math.imul(h, 0x01000193) >>> 0;
    }
    return h >>> 0;
  }

  /** L'1 de setembre del curs en què cau una data. */
  function iniciCurs(data) {
    const any = data.getMonth() >= 8 ? data.getFullYear() : data.getFullYear() - 1;
    return new Date(any, 8, 1);
  }

  /** Dies sencers entre dues dates, sense que el canvi d'hora hi faci res. */
  function diesEntre(a, b) {
    const utc = d => Date.UTC(d.getFullYear(), d.getMonth(), d.getDate());
    return Math.round((utc(b) - utc(a)) / 86400000);
  }

  /** Empaqueta els camps en un enter. Tots els camps cabien en 36 bits i el
      control n'hi afegeix 9: 45 bits, per sota dels 53 que un Number representa
      sense perdre res. Per això no cal BigInt. */
  function empaqueta(v) {
    return CAMPS.reduce((acc, [nom, mida]) => acc * mida + v[nom], 0);
  }

  function desempaqueta(n) {
    const v = {};
    for (let i = CAMPS.length - 1; i >= 0; i--) {
      const [nom, mida] = CAMPS[i];
      v[nom] = n % mida;
      n = Math.floor(n / mida);
    }
    return v;
  }

  const control = carrega => fnv(SAL + ":" + carrega) % CONTROL;

  /** Barreja reversible: la càrrega (36 bits) es parteix en dues meitats de 18
      i cadascuna es fa XOR amb un tros del hash del control. Fer-ho dues vegades
      amb el mateix control torna la càrrega original. */
  const MEITAT = 262144;                      // 2^18
  function barreja(carrega, ctl) {
    const h = fnv("barreja:" + ctl);
    const alt = Math.floor(carrega / MEITAT) ^ (h & 0x3FFFF);
    const baix = (carrega % MEITAT) ^ ((h >>> 14) & 0x3FFFF);
    return alt * MEITAT + baix;
  }

  /** Fa el codi. `dades` = { tasca, sub, cas, a, b, c } i, si es vol, `data`
      (per defecte, avui). Els valors que no caben es retallen al màxim del camp:
      un 40 és impossible de representar en 5 bits i val més un 31 que un error. */
  function fes(dades) {
    const avui = dades.data || new Date();
    const v = { versio: VERSIO, dia: diesEntre(iniciCurs(avui), avui) };
    CAMPS.forEach(([nom, mida]) => {
      if (nom === "versio" || nom === "dia") return;
      v[nom] = Math.max(0, Math.min(mida - 1, Math.round(Number(dades[nom]) || 0)));
    });
    const carrega = empaqueta(v);
    const ctl = control(carrega);
    let n = barreja(carrega, ctl) * CONTROL + ctl;

    let text = "";
    for (let i = 0; i < 9; i++) {
      text = ALFABET[n % 32] + text;
      n = Math.floor(n / 32);
    }
    return text.slice(0, 3) + "-" + text.slice(3, 6) + "-" + text.slice(6);
  }

  /** Llegeix un codi tal com l'escriu una persona: amb guions o sense, en
      minúscules, amb O en comptes de 0... Retorna null si no és vàlid.
      `avui` serveix per saber de quin curs és el dia (per defecte, avui). */
  function llegeix(text, avui) {
    const net = String(text || "").toUpperCase()
      .replace(/[^0-9A-Z]/g, "")
      .replace(/O/g, "0").replace(/[IL]/g, "1");
    if (net.length !== 9) return null;

    let n = 0;
    for (const car of net) {
      const i = ALFABET.indexOf(car);
      if (i < 0) return null;                 // una U, per exemple
      n = n * 32 + i;
    }
    const ctl = n % CONTROL;
    const carrega = barreja(Math.floor(n / CONTROL), ctl);
    if (ctl !== control(carrega)) return null;

    const v = desempaqueta(carrega);
    if (v.versio !== VERSIO) return null;

    // El dia es compta des de l'inici del curs d'avui. Si surt una data futura,
    // el codi és del curs passat.
    const ref = avui || new Date();
    let inici = iniciCurs(ref);
    let data = new Date(inici.getFullYear(), 8, 1 + v.dia);
    if (diesEntre(ref, data) > 0) {
      inici = new Date(inici.getFullYear() - 1, 8, 1);
      data = new Date(inici.getFullYear(), 8, 1 + v.dia);
    }
    return { tasca: v.tasca, sub: v.sub, cas: v.cas, a: v.a, b: v.b, c: v.c, data };
  }

  window.CE.codi = { fes, llegeix };
})();
