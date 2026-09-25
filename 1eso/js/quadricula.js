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
      `o` = {c, d, u} i, si es vol, {peus: [text C, text D, text U], ets: [...]} */
  function blocs(cont, o) {
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
    const S = 10 * m, fc = Math.max(1, Math.ceil(o.c / 3));
    dibuixa(0, 3 * S + 2 * aire, fc * S + (fc - 1) * aire, svg => {
      for (let i = 0; i < o.c; i++) {
        const x = (i % 3) * (S + aire), y = Math.floor(i / 3) * (S + aire);
        rectangle(svg, x, y, 10, 10, m, "q");
      }
      if (!o.c) svg.appendChild(el("rect", { x: 1, y: 1, width: S - 2, height: S - 2, rx: 6, class: "q falta" }));
    });
    // desenes: columnes de 10, de dalt a baix
    dibuixa(1, Math.max(1, o.d) * (m + 5), S, svg => {
      for (let i = 0; i < o.d; i++) rectangle(svg, i * (m + 5), 0, 10, 1, m, "q");
      if (!o.d) svg.appendChild(el("rect", { x: 1, y: 1, width: m - 2, height: S - 2, rx: 3, class: "q falta" }));
    });
    // unitats: tres per fila, com els punts d'un dau
    const fu = Math.max(1, Math.ceil(o.u / 3));
    dibuixa(2, 3 * (m + 3), fu * (m + 3), svg => {
      for (let i = 0; i < o.u; i++) quadret(svg, (i % 3) * (m + 3), Math.floor(i / 3) * (m + 3), m, "q");
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

  CE.q = { quadret, rectangle, graella, text, clau, taula, cellaTocada, fletxa, blocs, T,
           graella100, rectanglesDe, divisorsDe, dibuixaRectangles };
})();
