/* ============================================================================
   quadricula.js · el dibuix de tot el curs: la quadrícula de quadrets
   ----------------------------------------------------------------------------
   Tots els mòduls dibuixen amb aquestes peces, i per això un quadret és igual
   a tot arreu: la mateixa forma, el mateix aire entre quadrets i els mateixos
   colors. Un sol model per a tot el curs (docs/CRITERIS-DISSENY.md, regla A)
   vol dir també un sol dibuix a la pantalla.

   LA TAULA DE QUADRETS
   La quadrícula de 10 per 10 amb els números de l'1 al 10 a dalt i a
   l'esquerra. És el mateix objecte que la taula de multiplicar: el quadret de
   la fila 3 i la columna 4 és la cantonada del rectangle de 3 · 4. La fan
   servir la 0.1, la 1.1, la 1.2, la 2.1 i la 2.3.

   ELS COLORS VAN EN CLASSES (css/app.css), no en atributs: així el mode fosc
   funciona sense duplicar res. Mai no hi ha només el color per distingir dues
   coses: també hi ha aire, un traç discontinu o un rètol.
     q          un quadret del rectangle que es compta
     q b        la segona part: el tros que es parteix, els quadrets solts
     q mal      un intent equivocat
     q falta    un lloc buit, amb traç discontinu
   ========================================================================== */

(function () {
  "use strict";
  const { el } = CE;

  /** Un quadret, amb una mica d'aire perquè es pugui comptar. */
  function quadret(pare, x, y, m, classe) {
    const aire = Math.max(1, m * 0.1);
    return pare.appendChild(el("rect", {
      x: x + aire / 2, y: y + aire / 2, width: m - aire, height: m - aire,
      rx: Math.min(4, m * 0.14), class: classe || "q" }));
  }

  /** Un rectangle de quadrets: `files` files de `cols` quadrets. */
  function rectangle(pare, x, y, files, cols, m, classe) {
    for (let f = 0; f < files; f++)
      for (let c = 0; c < cols; c++) quadret(pare, x + c * m, y + f * m, m, classe);
  }

  /** La quadrícula buida: el fons i les línies. */
  function graella(pare, x, y, files, cols, m) {
    pare.appendChild(el("rect", { x, y, width: cols * m, height: files * m, class: "q-fons" }));
    for (let f = 0; f <= files; f++)
      pare.appendChild(el("line", { x1: x, y1: y + f * m, x2: x + cols * m, y2: y + f * m, class: "q-linia" }));
    for (let c = 0; c <= cols; c++)
      pare.appendChild(el("line", { x1: x + c * m, y1: y, x2: x + c * m, y2: y + files * m, class: "q-linia" }));
  }

  /** Un text centrat al punt (x, y). */
  function text(pare, x, y, t, classe, mida, ancora) {
    return pare.appendChild(el("text", { x, y, class: classe || "q-text", "font-size": mida || 17,
      "text-anchor": ancora || "middle", "dominant-baseline": "central" }, t));
  }

  /** Una clau: una línia amb dues potes i el rètol al costat.
      `costat` és "dalt" (línia horitzontal, rètol a sobre) o "esquerra"
      (línia vertical, rètol a l'esquerra, en horitzontal: no es gira mai la
      lletra, que costa de llegir). */
  function clau(pare, x1, y1, x2, y2, t, costat, classe) {
    const g = pare.appendChild(el("g", { class: "q-clau" + (classe ? " " + classe : "") }));
    if (costat === "esquerra") {
      g.appendChild(el("path", { d: "M" + (x1 + 7) + " " + y1 + " H" + x1 + " V" + y2 + " H" + (x1 + 7) }));
      text(g, x1 - 8, (y1 + y2) / 2, t, "q-text", 17, "end");
    } else {
      g.appendChild(el("path", { d: "M" + x1 + " " + (y1 + 7) + " V" + y1 + " H" + x2 + " V" + (y1 + 7) }));
      text(g, (x1 + x2) / 2, y1 - 14, t, "q-text", 17, "middle");
    }
    return g;
  }

  /* ======================================================= la taula ====== */

  const T = { m: 30, x: 36, y: 36, n: 10, mida: 340 };       // viewBox 0 0 340 340

  /** La taula de quadrets. `o`:
        f, c       el rectangle ple (files i quadrets a cada fila)
        classe     la classe dels seus quadrets ("q" si no es diu)
        contorn    {f, c}: un rectangle només resseguit, amb traç discontinu
        cursor     {f, c}: on és el cursor del teclat
        pista      {f, c}: els dos números de la vora que s'han de mirar
        extra      funció (svg, T) que hi dibuixa a sobre
      Els números de la vora que entren al rectangle es destaquen: així
      «3 files» es llegeix sense haver de comptar. */
  function taula(svg, o) {
    o = o || {};
    svg.textContent = "";
    graella(svg, T.x, T.y, T.n, T.n, T.m);
    const fViu = o.f || 0, cViu = o.c || 0;
    for (let i = 1; i <= T.n; i++) {
      const cx = T.x + (i - 0.5) * T.m, cy = T.y + (i - 0.5) * T.m;
      if (o.pista && o.pista.c === i) svg.appendChild(el("circle", { cx, cy: T.y / 2, r: 14, class: "q-pista" }));
      if (o.pista && o.pista.f === i) svg.appendChild(el("circle", { cx: T.x / 2, cy, r: 14, class: "q-pista" }));
      text(svg, cx, T.y / 2, i, "q-num" + (i <= cViu ? " viu" : ""), 15);
      text(svg, T.x / 2, cy, i, "q-num" + (i <= fViu ? " viu" : ""), 15);
    }
    if (o.f > 0 && o.c > 0) rectangle(svg, T.x, T.y, o.f, o.c, T.m, o.classe || "q");
    if (o.contorn) svg.appendChild(el("rect", { x: T.x + 1.5, y: T.y + 1.5,
      width: o.contorn.c * T.m - 3, height: o.contorn.f * T.m - 3, rx: 4, class: "q-contorn" }));
    if (o.cursor) svg.appendChild(el("rect", { x: T.x + 1.5, y: T.y + 1.5,
      width: o.cursor.c * T.m - 3, height: o.cursor.f * T.m - 3, rx: 4, class: "q-cursor" }));
    if (o.extra) o.extra(svg, T);
  }

  /** On s'ha tocat la taula: {f, c} de l'1 al 10, o null si és fora. */
  function cellaTocada(svg, ev) {
    const r = svg.getBoundingClientRect();
    if (!r.width) return null;
    const x = (ev.clientX - r.left) / r.width * T.mida;
    const y = (ev.clientY - r.top) / r.height * T.mida;
    const c = Math.floor((x - T.x) / T.m) + 1, f = Math.floor((y - T.y) / T.m) + 1;
    return (f >= 1 && f <= T.n && c >= 1 && c <= T.n) ? { f, c } : null;
  }

  /** Les fletxes mouen una cantonada dins de la taula. Retorna la nova, o null
      si la tecla no és una fletxa. Amb la taula buida es comença a la 1, 1 i ja
      s'hi aplica la fletxa: dreta, 1 fila de 2; avall, 2 files d'1. Cap costat
      no baixa de 1 ni passa de 10. */
  function fletxa(tecla, p) {
    const d = { ArrowUp: [-1, 0], ArrowDown: [1, 0], ArrowLeft: [0, -1], ArrowRight: [0, 1] }[tecla];
    if (!d) return null;
    const base = (!p || (!p.f && !p.c)) ? { f: 1, c: 1 } : p;
    const fixa = v => Math.max(1, Math.min(T.n, v));
    return { f: fixa(base.f + d[0]), c: fixa(base.c + d[1]) };
  }

  /* ================================= centenes, desenes i unitats ====== */

  /** Els blocs d'un nombre: quadrats de 100, columnes de 10 i quadrets solts.
      Cada zona és un SVG a part dins de `cont`, perquè a la pantalla estreta
      baixin de línia en lloc d'encongir-se. La mida del quadret és la mateixa
      a les tres zones: un quadrat de 100 és de debò deu columnes de 10.
      `o` = {c, d, u} i, si es vol, {peus: [text C, text D, text U], ets: [...]}.
      Amb `o.b` = {c, d, u}, les últimes peces de cada zona són la segona part
      (unitat 5): el segon sumand, amb la classe «q b nou» (un altre color i el
      traç discontinu), o, amb `o.treu`, el que es resta: buit, amb el traç
      discontinu i una ratlla, com el que es treu de les fraccions. */
  function blocs(cont, o) {
    const b = o.b || { c: 0, d: 0, u: 0 };
    const classe = (i, total, k) => (i >= total - b[k] ? (o.treu ? "q falta" : "q b nou") : "q");
    const ratlla = (svg, x, y, w, h, i, total, k) => {
      if (o.treu && i >= total - b[k])
        svg.appendChild(el("line", { x1: x + 2, y1: y + h - 2, x2: x + w - 2, y2: y + 2, class: "q-ratlla" }));
    };
    const m = (cont.clientWidth || 300) >= 560 ? 9 : 7;
    const aire = 8;
    if (!cont.children.length) {
      ["c", "d", "u"].forEach(k => {
        const z = document.createElement("div");
        z.className = "zona zona-" + k;
        z.innerHTML = '<div class="zona-et"></div><div class="zona-dibuix"></div><div class="zona-peu"></div>';
        cont.appendChild(z);
      });
    }
    const zones = cont.children;
    const dibuixa = (i, amp, alt, pinta) => {
      const caixa = zones[i].querySelector(".zona-dibuix");
      caixa.textContent = "";
      const svg = el("svg", { viewBox: "0 0 " + amp + " " + alt, width: amp, height: alt,
                              "aria-hidden": "true", focusable: "false" });
      pinta(svg);
      caixa.appendChild(svg);
    };
    // centenes: tres per fila
    // L'amplada, la dels quadrats que hi ha (tres com a molt per fila): amb 0 o 1
    // quadrat, les columnes no queden lluny (unitat 5, on sovint no n'hi ha cap).
    const S = 10 * m, fc = Math.max(1, Math.ceil(o.c / 3)), ac = Math.max(1, Math.min(3, o.c));
    dibuixa(0, ac * S + (ac - 1) * aire, fc * S + (fc - 1) * aire, svg => {
      for (let i = 0; i < o.c; i++) {
        const x = (i % 3) * (S + aire), y = Math.floor(i / 3) * (S + aire);
        rectangle(svg, x, y, 10, 10, m, classe(i, o.c, "c"));
        ratlla(svg, x, y, S, S, i, o.c, "c");
      }
      if (!o.c) svg.appendChild(el("rect", { x: 1, y: 1, width: S - 2, height: S - 2, rx: 6, class: "q falta" }));
    });
    // desenes: columnes de 10, de dalt a baix
    dibuixa(1, Math.max(1, o.d) * (m + 5), S, svg => {
      for (let i = 0; i < o.d; i++) {
        rectangle(svg, i * (m + 5), 0, 10, 1, m, classe(i, o.d, "d"));
        ratlla(svg, i * (m + 5), 0, m, S, i, o.d, "d");
      }
      if (!o.d) svg.appendChild(el("rect", { x: 1, y: 1, width: m - 2, height: S - 2, rx: 3, class: "q falta" }));
    });
    // unitats: tres per fila, com els punts d'un dau
    const fu = Math.max(1, Math.ceil(o.u / 3));
    dibuixa(2, 3 * (m + 3), fu * (m + 3), svg => {
      for (let i = 0; i < o.u; i++) {
        const x = (i % 3) * (m + 3), y = Math.floor(i / 3) * (m + 3);
        quadret(svg, x, y, m, classe(i, o.u, "u"));
        ratlla(svg, x, y, m, m, i, o.u, "u");
      }
      if (!o.u) svg.appendChild(el("rect", { x: 1, y: 1, width: m - 2, height: m - 2, rx: 2, class: "q falta" }));
    });
    ["c", "d", "u"].forEach((k, i) => {
      zones[i].querySelector(".zona-et").innerHTML = (o.ets || [])[i] || "";
      zones[i].querySelector(".zona-peu").innerHTML = (o.peus || [])[i] || "";
    });
  }

  /* =================================================== la graella de 100 ====== */

  /* La graella de 100 de l'activitat dels múltiples del grup: els nombres de l'1 al
     100 en deu files de deu. La fan servir la 5.1 (els múltiples) i la 8.1 (el
     garbell). `estil(n)` diu com va cada nombre:
       "marca"    pintat, com un quadret del rectangle
       "primer"   pintat i encerclat
       "ratllat"  amb una ratlla al damunt: ja no compta
       null       tal com és                                                      */
  const C = { m: 36, x: 10, y: 10, mida: 380 };                // viewBox 0 0 380 380
  function graella100(svg, estil) {
    svg.textContent = "";
    graella(svg, C.x, C.y, 10, 10, C.m);
    for (let n = 1; n <= 100; n++) {
      const x = C.x + ((n - 1) % 10) * C.m, y = C.y + Math.floor((n - 1) / 10) * C.m;
      const e = estil ? estil(n) : null;
      if (e === "marca" || e === "primer") quadret(svg, x, y, C.m, "q");
      if (e === "primer") svg.appendChild(el("circle", { cx: x + C.m / 2, cy: y + C.m / 2, r: C.m * 0.42, class: "q-cercle" }));
      if (e === "ratllat") svg.appendChild(el("line", { x1: x + 5, y1: y + C.m - 5, x2: x + C.m - 5, y2: y + 5, class: "q-ratlla" }));
      text(svg, x + C.m / 2, y + C.m / 2 + 1, n, e === "marca" || e === "primer" ? "q-text fort" : "q-num", n === 100 ? 12 : 14);
    }
  }

  /* ============================================ els rectangles d'un nombre ====== */

  /** Els rectangles que es poden fer amb n quadrets: [files, quadrets a cada fila],
      amb files ≤ quadrets a cada fila, perquè el girat és el mateix rectangle. */
  function rectanglesDe(n) {
    const r = [];
    for (let a = 1; a * a <= n; a++) if (n % a === 0) r.push([a, n / a]);
    return r;
  }
  /** Els divisors de n, de petit a gran. */
  function divisorsDe(n) {
    const d = [];
    rectanglesDe(n).forEach(([a, b]) => { d.push(a); if (b !== a) d.push(b); });
    return d.sort((x, y) => x - y);
  }
  /** Tots els rectangles de n, un sota l'altre i a la mateixa escala, amb el seu
      rètol («2 · 6»). La fila d'1 és la més llarga: mana la mida del quadret. */
  function dibuixaRectangles(svg, n) {
    svg.textContent = "";
    const rs = rectanglesDe(n);
    const ETIQ = 64, AMP = 420, AIRE = 16;
    const m = Math.max(7, Math.min(26, (AMP - ETIQ - 8) / n));
    let y = 8;
    rs.forEach(([a, b]) => {
      text(svg, ETIQ - 12, y + (a * m) / 2 + 1, a + " · " + b, "q-text fort", 16, "end");
      rectangle(svg, ETIQ, y, a, b, m, "q");
      y += a * m + AIRE;
    });
    svg.setAttribute("viewBox", "0 0 " + AMP + " " + Math.max(40, Math.round(y - AIRE + 8)));
    return rs;
  }

  /* ================================================ els decimals (unitat 5) ===== */

  /* El quadrat de 100 és 1: una columna és 0,1 (una dècima) i un quadret és 0,01 (una
     centèsima). Els decimals es guarden com a centèsimes enteres (2,43 és 243), perquè
     els comptes surtin exactes. Fins a 9,99, amb dues xifres decimals com a molt
     (decisió del docent del 29/9/2026): 999 centèsimes, el mateix límit de sempre. */

  /** Les centèsimes escrites com a decimal, amb coma: dec(243) és «2,43». Amb `x`
      (1 o 2), sempre amb aquelles xifres decimals: dec(350, 1) és «3,5» i dec(100, 1)
      és «1,0». Sense `x`, les justes: dec(240) és «2,4» i dec(300) és «3». */
  function dec(c, x) {
    const u = Math.floor(c / 100), r = c % 100;
    if (x === 2) return u + "," + String(r).padStart(2, "0");
    if (x === 1) return u + "," + Math.round(r / 10);
    if (r === 0) return String(u);
    return u + "," + (r % 10 === 0 ? String(r / 10) : String(r).padStart(2, "0"));
  }

  /** El quadrat de 100 amb `n` quadrets pintats, columna a columna i de dalt a baix:
      2 columnes i 5 quadrets són 0,25. Sense números a dins, perquè el que es compta
      són les columnes. Els llocs buits de la columna a mig fer van amb traç
      discontinu. viewBox 0 0 340 340, com la taula de quadrets. */
  const Q100 = { m: 30, x: 20, y: 20, mida: 340 };
  function quadrat100(svg, n) {
    svg.textContent = "";
    graella(svg, Q100.x, Q100.y, 10, 10, Q100.m);
    const plenes = Math.floor(n / 10);
    for (let i = 0; i < 100; i++) {
      const col = Math.floor(i / 10), fila = i % 10;
      const x = Q100.x + col * Q100.m, y = Q100.y + fila * Q100.m;
      if (i < n) quadret(svg, x, y, Q100.m, "q");
      else if (col === plenes && n % 10) quadret(svg, x, y, Q100.m, "q falta");
    }
    svg.appendChild(el("rect", { x: Q100.x, y: Q100.y, width: 10 * Q100.m, height: 10 * Q100.m, class: "q-vora" }));
    svg.setAttribute("viewBox", "0 0 " + Q100.mida + " " + Q100.mida);
  }

  /** La recta numèrica, el segon model del curs (docs/MAPA-ADAPTACIO.md, apartat 3): de
      `ini` a `fi`, en centèsimes, amb una ratlla cada `pas`. `o`:
        mig      la ratlla del mig, més llarga i amb el seu nombre: on es decideix cap a
                 on s'arrodoneix
        punt     on va el punt, amb el seu nombre a sobre
      Els dos extrems porten el nombre a sota, en negreta. viewBox 0 0 320 130: estreta i
      amb la lletra gran, perquè al mòbil els nombres es llegeixin. */
  const RECTA = { x0: 30, x1: 290, y: 68, mida: [320, 130] };
  function recta(svg, ini, fi, pas, o) {
    o = o || {};
    svg.textContent = "";
    const X = v => RECTA.x0 + (v - ini) / (fi - ini) * (RECTA.x1 - RECTA.x0), y = RECTA.y;
    svg.appendChild(el("line", { x1: RECTA.x0 - 14, y1: y, x2: RECTA.x1 + 14, y2: y, class: "q-eix" }));
    const mig = (ini + fi) / 2;
    for (let v = ini; v <= fi; v += pas) {
      const gran = v === ini || v === fi, esMig = o.mig && v === mig;
      const h = gran ? 13 : esMig ? 11 : 6;
      svg.appendChild(el("line", { x1: X(v), y1: y - h, x2: X(v), y2: y + h, class: "q-eix" + (esMig ? " mig" : "") }));
      if (gran || esMig) text(svg, X(v), y + 34, dec(v, gran && fi - ini < 100 ? 1 : undefined),
                              "q-text" + (gran ? " fort" : ""), gran ? 24 : 20);
    }
    if (o.punt != null) {
      svg.appendChild(el("circle", { cx: X(o.punt), cy: y, r: 7, class: "q-punt" }));
      text(svg, X(o.punt), y - 34, dec(o.punt), "q-text fort", 24);
    }
    svg.setAttribute("viewBox", "0 0 " + RECTA.mida.join(" "));
  }

  /* ============================================== la geometria (unitat 6) ===== */

  /* La cantonada d'un quadret és l'angle recte: un angle agut és més petit que la
     cantonada, un obtús és més gran i un de pla és una recta (decisió del docent del
     29/9/2026: els angles es comparen amb la cantonada, sense transportador). */

  /** Un angle: el vèrtex al mig de baix, un costat cap a la dreta i l'altre obert `graus`
      (de 0 a 180). `o`:
        llarg      la llargada dels costats (per defecte, 120): no canvia l'angle
        cantonada  la cantonada d'un quadret al vèrtex, discontínua: l'angle recte
      viewBox 0 0 360 200. */
  const ANGLE = { vx: 180, vy: 185, mida: [360, 200] };
  function angle(svg, graus, o) {
    o = o || {};
    svg.textContent = "";
    const L = o.llarg || 120, a = graus * Math.PI / 180, r = 34, { vx, vy } = ANGLE;
    const px = x => Math.round(x * 10) / 10;
    const x2 = px(vx + L * Math.cos(a)), y2 = px(vy - L * Math.sin(a));
    const ax = px(vx + r * Math.cos(a)), ay = px(vy - r * Math.sin(a));
    svg.appendChild(el("path", { d: `M${vx} ${vy} L${vx + r} ${vy} A${r} ${r} 0 0 0 ${ax} ${ay} Z`, class: "angle-sector" }));
    if (o.cantonada) svg.appendChild(el("path", { d: `M${vx + 46} ${vy} V${vy - 46} H${vx}`, class: "cantonada" }));
    svg.appendChild(el("line", { x1: vx, y1: vy, x2: vx + L, y2: vy, class: "angle-costat" }));
    svg.appendChild(el("line", { x1: vx, y1: vy, x2: x2, y2: y2, class: "angle-costat" }));
    svg.appendChild(el("circle", { cx: vx, cy: vy, r: 5, class: "angle-vertex" }));
    svg.setAttribute("viewBox", "0 0 " + ANGLE.mida.join(" "));
  }
  /** El tipus d'un angle, pel que fa a la cantonada: "agut", "recte", "obtus" o "pla". */
  const tipusAngle = g => (g < 90 ? "agut" : g === 90 ? "recte" : g < 180 ? "obtus" : "pla");

  /** El geoplà: una quadrícula de punts de 6 per 6 i un polígon pels punts `pts`, cada un
      [x, y] de 0 a 5 (y cap avall). Els vèrtexs, més marcats. viewBox 0 0 340 340. */
  const GEO = { n: 6, m: 56, x0: 30, mida: 340 };
  function geopla(svg, pts, o) {
    o = o || {};
    svg.textContent = "";
    const X = v => GEO.x0 + v * GEO.m;
    for (let i = 0; i < GEO.n; i++)
      for (let j = 0; j < GEO.n; j++)
        svg.appendChild(el("circle", { cx: X(i), cy: X(j), r: 3.5, class: "geo-punt" }));
    if (pts && pts.length) {
      svg.appendChild(el("polygon", { points: pts.map(([x, y]) => X(x) + "," + X(y)).join(" "),
                                      class: o.classe || "poligon" }));
      pts.forEach(([x, y]) => svg.appendChild(el("circle", { cx: X(x), cy: X(y), r: 7, class: "angle-vertex" })));
    }
    svg.setAttribute("viewBox", "0 0 " + GEO.mida + " " + GEO.mida);
  }

  /** Els angles d'un triangle de vèrtexs enters, en graus, i si n'hi ha cap de recte o
      d'obtús: amb enters, el producte escalar diu si és recte (0) o obtús (negatiu) sense
      arrodonir res. */
  function anglesTriangle(pts) {
    return pts.map((p, i) => {
      const a = pts[(i + 1) % 3], b = pts[(i + 2) % 3];
      const u = [a[0] - p[0], a[1] - p[1]], v = [b[0] - p[0], b[1] - p[1]];
      const pe = u[0] * v[0] + u[1] * v[1];
      const g = Math.acos(pe / (Math.hypot(...u) * Math.hypot(...v))) * 180 / Math.PI;
      return { g, pe };
    });
  }
  const tipusTriangle = pts => {
    const as = anglesTriangle(pts);
    return as.some(a => a.pe === 0) ? "rectangle" : as.some(a => a.pe < 0) ? "obtusangle" : "acutangle";
  };

  /** Un triangle al geoplà, amb un arc numerat a cada angle (1, 2 i 3: el número, i no
      només el color, diu quin és cada un). viewBox 0 0 340 340. */
  function triangle(svg, pts, o) {
    o = o || {};
    geopla(svg, pts, { classe: "poligon" });
    const X = v => GEO.x0 + v * GEO.m, r = 30;
    if (!o.arcs) return;
    pts.forEach((p, i) => {
      const a = pts[(i + 1) % 3], b = pts[(i + 2) % 3];
      let t1 = Math.atan2(-(a[1] - p[1]), a[0] - p[0]), t2 = Math.atan2(-(b[1] - p[1]), b[0] - p[0]);
      let d = t2 - t1;
      while (d <= -Math.PI) d += 2 * Math.PI;
      while (d > Math.PI) d -= 2 * Math.PI;
      const cx = X(p[0]), cy = X(p[1]);
      const pt = t => [Math.round((cx + r * Math.cos(t)) * 10) / 10, Math.round((cy - r * Math.sin(t)) * 10) / 10];
      const [x1, y1] = pt(t1), [x2, y2] = pt(t1 + d), m = t1 + d / 2;
      svg.appendChild(el("path", { d: `M${cx} ${cy} L${x1} ${y1} A${r} ${r} 0 0 ${d > 0 ? 0 : 1} ${x2} ${y2} Z`,
                                   class: "ang ang" + (i + 1) }));
      // El número, sobre un cercle del color del fons: es llegeix sobre qualsevol to.
      svg.appendChild(el("circle", { cx: cx + 48 * Math.cos(m), cy: cy - 48 * Math.sin(m), r: 12, class: "ang-fons" }));
      text(svg, cx + 48 * Math.cos(m), cy - 48 * Math.sin(m) + 6, String(i + 1), "q-text fort", 18);
    });
  }

  /** Els tres angles d'un triangle, un al costat de l'altre al mateix punt: fan un angle
      pla. Amb els mateixos números i les mateixes classes que `triangle`. viewBox 0 0 360 180. */
  function anglesJunts(svg, pts) {
    svg.textContent = "";
    const as = anglesTriangle(pts).map(a => a.g), cx = 180, cy = 160, r = 120;
    svg.appendChild(el("line", { x1: 20, y1: cy, x2: 340, y2: cy, class: "angle-costat" }));
    let ini = 0;
    as.forEach((g, i) => {
      const t1 = ini * Math.PI / 180, t2 = (ini + g) * Math.PI / 180, m = (t1 + t2) / 2;
      const pt = t => [Math.round((cx + r * Math.cos(t)) * 10) / 10, Math.round((cy - r * Math.sin(t)) * 10) / 10];
      const [x1, y1] = pt(t1), [x2, y2] = pt(t2);
      svg.appendChild(el("path", { d: `M${cx} ${cy} L${x1} ${y1} A${r} ${r} 0 0 0 ${x2} ${y2} Z`, class: "ang ang" + (i + 1) }));
      svg.appendChild(el("circle", { cx: cx + 78 * Math.cos(m), cy: cy - 78 * Math.sin(m), r: 14, class: "ang-fons" }));
      text(svg, cx + 78 * Math.cos(m), cy - 78 * Math.sin(m) + 7, String(i + 1), "q-text fort", 20);
      ini += g;
    });
    svg.appendChild(el("circle", { cx, cy, r: 5, class: "angle-vertex" }));
    svg.setAttribute("viewBox", "0 0 360 180");
  }

  /** Un rectangle de f files i c columnes de quadrets, amb la vora gruixuda i els costats
      numerats per fora: c a dalt i a baix, f a l'esquerra i a la dreta. El perímetre és
      la vora; l'àrea, els quadrets de dins. viewBox 0 0 340 300. */
  function vora(svg, f, c) {
    svg.textContent = "";
    const m = Math.min(40, Math.floor(230 / Math.max(f, c))), x0 = 170 - c * m / 2, y0 = 150 - f * m / 2;
    for (let i = 0; i < f; i++) for (let j = 0; j < c; j++) quadret(svg, x0 + j * m, y0 + i * m, m, "q");
    svg.appendChild(el("rect", { x: x0, y: y0, width: c * m, height: f * m, class: "vora-gruixuda" }));
    text(svg, 170, y0 - 12, String(c), "q-text fort", 20);
    text(svg, 170, y0 + f * m + 28, String(c), "q-text fort", 20);
    text(svg, x0 - 18, 157, String(f), "q-text fort", 20);
    text(svg, x0 + c * m + 18, 157, String(f), "q-text fort", 20);
    svg.setAttribute("viewBox", "0 0 340 300");
  }

  /* ================================================ els patrons (unitat 7) ===== */

  /** Una figura d'un patró de quadrets «a · n + b»: la part fixa (b quadrets, taronja i
      discontinus, en una columna a l'esquerra) i a files de n quadrets. Així es veu què hi ha
      de fix i què s'hi afegeix a cada figura. `o.m`: la mida del quadret (per defecte, la que
      hi cap). viewBox 0 0 W H, calculat. */
  function patro(svg, a, b, n, o) {
    o = o || {};
    svg.textContent = "";
    const m = o.m || Math.min(34, Math.floor(300 / (n + (b ? 1.4 : 0))), Math.floor(130 / Math.max(a, b, 1)));
    let x = 6;
    const H = Math.max(a, b) * m + 12, y0 = H - 6;
    for (let i = 0; i < b; i++) quadret(svg, x, y0 - (i + 1) * m, m, "q b nou");
    if (b) x += m * 1.4;
    for (let f = 0; f < a; f++) for (let c = 0; c < n; c++) quadret(svg, x + c * m, y0 - (f + 1) * m, m, "q");
    const W = Math.max(x + n * m + 6, 60);
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    svg.setAttribute("width", W);
    return { W, H };
  }

  /** Un gràfic de barres fet de quadrets: cada quadret és 1. `dades` = [[etiqueta, valor]].
      L'eix, amb un nombre cada 2, comença a zero. viewBox 0 0 360 300. */
  function barres(svg, dades, o) {
    o = o || {};
    svg.textContent = "";
    const max = Math.max(...dades.map(d => d[1])), m = Math.min(18, Math.floor(220 / Math.max(max, 10)));
    const x0 = 44, y0 = 250, amp = Math.min(60, Math.floor(300 / dades.length)), bw = m;
    for (let v = 0; v <= max + 1; v += 2) {
      svg.appendChild(el("line", { x1: x0, y1: y0 - v * m, x2: x0 + dades.length * amp + 8, y2: y0 - v * m, class: "q-linia" }));
      text(svg, x0 - 10, y0 - v * m + 5, String(v), "q-num", 13);
    }
    svg.appendChild(el("line", { x1: x0, y1: y0, x2: x0, y2: y0 - (max + 1) * m, class: "q-eix" }));
    svg.appendChild(el("line", { x1: x0, y1: y0, x2: x0 + dades.length * amp + 8, y2: y0, class: "q-eix" }));
    dades.forEach(([et, v], i) => {
      const x = x0 + i * amp + (amp - bw) / 2;
      for (let k = 0; k < v; k++) quadret(svg, x, y0 - (k + 1) * m, m, o.destaca === i ? "q b" : "q");
      text(svg, x0 + i * amp + amp / 2, y0 + 20, et, "q-text", 13);
    });
    svg.setAttribute("viewBox", "0 0 360 280");
  }

  /* ======================================================= les fraccions ===== */

  /* El rectangle de les fraccions (unitat 3): sempre de la mateixa mida, perquè dues
     fraccions es puguin comparar, com fan els cercles del grup. Es parteix en d trossos
     iguals, i se'n pinten uns quants. Els `mes` següents van en taronja (el segon
     sumand); els `treu` darrers pintats, ratllats (el que es resta). Amb `k` > 1, cada
     tros es parteix en k amb línies fines (les equivalents). */
  const TIRA = { W: 360, H: 54, aire: 14 };
  function tira(svg, x, y, d, pintats, o) {
    o = o || {};
    const W = o.W || TIRA.W, H = o.H || TIRA.H, w = W / d;
    for (let i = 0; i < d; i++) {
      const cls = i < pintats ? "q" : i < pintats + (o.mes || 0) ? "q b" : "q-buit";
      svg.appendChild(el("rect", { x: x + i * w, y, width: w, height: H, class: cls }));
      if (o.treu && i >= pintats - o.treu && i < pintats)
        svg.appendChild(el("line", { x1: x + i * w + 5, y1: y + H - 5, x2: x + (i + 1) * w - 5, y2: y + 5, class: "q-ratlla" }));
    }
    if (o.k > 1) for (let i = 1; i < d * o.k; i++) if (i % o.k) {
      const xx = x + (i * w) / o.k;
      svg.appendChild(el("line", { x1: xx, y1: y + 4, x2: xx, y2: y + H - 4, class: "q-fina" }));
    }
    svg.appendChild(el("rect", { x, y, width: W, height: H, class: "q-vora" }));
  }
  /** n/d amb els rectangles que calguin (almenys un), un sota l'altre. Torna l'alçada. */
  function fraccio(svg, x, y, n, d, o) {
    o = o || {};
    const unitats = Math.max(1, Math.ceil((n + (o.mes || 0)) / d));
    const H = o.H || TIRA.H;
    let resta = n, mes = o.mes || 0;
    for (let u = 0; u < unitats; u++) {
      const p = Math.min(d, resta); resta -= p;
      const m = Math.min(d - p, mes); mes -= m;
      tira(svg, x, y + u * (H + TIRA.aire), d, p, Object.assign({}, o, { mes: m, treu: u === unitats - 1 ? o.treu : 0 }));
    }
    return unitats * (H + TIRA.aire) - TIRA.aire;
  }
  /* ================================================ multiplicar fraccions ===== */

  /* El rectangle de dues fraccions (unitat 4): d1 columnes per d2 files, sempre
     de la mateixa mida perquè el resultat es pugui comparar amb el de les
     fraccions soles (unitat 3). Les primeres n1 columnes es pinten («la
     primera fracció»), i les primeres n2 files queden resseguides amb un
     contorn («la segona fracció»): el tros que és a la vegada pintat i dins
     del contorn (n1 columnes per n2 files) és el resultat, marcat amb el color
     I el contorn perquè el color no sigui l'única diferència (docs/
     CRITERIS-DISSENY.md, els colors de quadricula.js). */
  const G2D = { m: 40, x: 70, y: 34 };
  function graella2D(svg, d1, n1, d2, n2) {
    svg.textContent = "";
    const m = Math.min(G2D.m, 300 / d1, 220 / d2);
    graella(svg, G2D.x, G2D.y, d2, d1, m);
    if (n1 > 0) rectangle(svg, G2D.x, G2D.y, d2, n1, m, "q");
    if (n1 > 0 && n2 > 0) svg.appendChild(el("rect", { x: G2D.x + 1.5, y: G2D.y + 1.5,
      width: n1 * m - 3, height: n2 * m - 3, rx: 4, class: "q-contorn" }));
    clau(svg, G2D.x, G2D.y - 10, G2D.x + d1 * m, G2D.y - 10, n1 + "/" + d1, "dalt");
    clau(svg, G2D.x - 12, G2D.y, G2D.x - 12, G2D.y + d2 * m, n2 + "/" + d2, "esquerra");
    svg.setAttribute("viewBox", "0 0 " + Math.round(G2D.x + d1 * m + 20) + " " + Math.round(G2D.y + d2 * m + 16));
  }

  const NUMS = ["zero", "un", "dos", "tres", "quatre", "cinc", "sis", "set", "vuit", "nou", "deu", "onze", "dotze",
    "tretze", "catorze", "quinze", "setze", "disset", "divuit", "dinou", "vint", "vint-i-un", "vint-i-dos",
    "vint-i-tres", "vint-i-quatre"];
  /** «quatre novens», «un mig»: el nom, amb els de la targeta de les fraccions. */
  function nomFraccio(n, d) {
    return NUMS[n] + " " + (n === 1 ? CE.txtPla("frac.s_" + d) : CE.txtPla("frac.p_" + d));
  }
  /** La fracció escrita com a fracció: el numerador damunt del denominador. */
  function htmlFraccio(n, d) {
    return '<span class="frac" role="img" aria-label="' + nomFraccio(n, d) + '"><span aria-hidden="true">' + n +
      '</span><span aria-hidden="true">' + d + "</span></span>";
  }
  /** nul·la, pròpia, unitat o impròpia */
  const tipusFraccio = (n, d) => (n === 0 ? "nulla" : n < d ? "propia" : n === d ? "unitat" : "impropia");

  CE.q = { quadret, rectangle, graella, text, clau, taula, cellaTocada, fletxa, blocs, T,
           graella100, rectanglesDe, divisorsDe, dibuixaRectangles,
           TIRA, tira, fraccio, nomFraccio, htmlFraccio, tipusFraccio, graella2D,
           dec, Q100, quadrat100, RECTA, recta,
           ANGLE, angle, tipusAngle, GEO, geopla, anglesTriangle, tipusTriangle, triangle, anglesJunts, vora,
           patro, barres };
})();
