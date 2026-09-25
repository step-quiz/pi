/* ============================================================================
   DIVISORS — mòdul «divisors» de la caixa d'eines · tasca 7 · unitat 2
   ----------------------------------------------------------------------------
   El nucli de la unitat 2: els divisors de 12 surten dels rectangles que es
   poden fer amb 12 quadrets. 1 per 12, 2 per 6 i 3 per 4: cada rectangle en
   dona dos, les files i els quadrets de cada fila. És l'activitat 2_4 del grup
   (20 = 1 · 20 = 2 · 10 = 4 · 5), amb el dibuix de tot el curs.

   7.1 · ELS RECTANGLES D'UN NOMBRE
     Un comptador de l'1 al 48. Surten tots els rectangles, un sota l'altre i a
     la mateixa escala, i sota, quants n'hi ha, els divisors i si el nombre és
     primer: un primer només en fa un, una fila. El girat no compta dues
     vegades: 2 · 6 i 6 · 2 són el mateix rectangle. S'obre amb el 12.

   7.2 · TROBA ELS DIVISORS
     Una tasca tancada de cinc nombres. Es marquen tots els divisors i es toca
     «Comprova», perquè la resposta són molts tocs (docs/CRITERIS-DISSENY.md,
     regla P). Primer error: diu què sobra o si en falten, i la pista és buscar
     a la targeta les multiplicacions que donen el nombre. Segon error: la caixa
     marca els bons i en dibuixa els rectangles.
   ========================================================================== */

(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, quants, elNombre, lectura } = CE;
  const Q = CE.q;
  const majuscula = t => t.charAt(0).toUpperCase() + t.slice(1);

  /** «1, 2, 3, 4, 6 i 12». */
  const llista = xs => xs.length === 1 ? String(xs[0]) : xs.slice(0, -1).join(", ") + " " + txtPla("comu.i") + " " + xs[xs.length - 1];

  /** El que diu si és primer: «El 7 només fa un rectangle, una fila: és primer.» */
  function primerOno(n) {
    const rs = Q.rectanglesDe(n), el = majuscula(elNombre(n));
    if (n === 1) return txt("7.1.u");
    return rs.length === 1 ? txt("7.1.primer", { el_n: el }) : txt("7.1.no_primer", { el_n: el });
  }
  CE.primerOno = primerOno;

  /* ============================== 7.1 · Els rectangles d'un nombre ====== */

  const EX71 = 12;
  let n71 = EX71;

  function pinta71() {
    const n = n71, svg = $("#d7-svg");
    const rs = Q.dibuixaRectangles(svg, n);
    const ds = Q.divisorsDe(n);
    const paraules = [
      txt(rs.length === 1 ? "7.1.es_pot" : "7.1.es_poden",
          { quadrets: quants(n, "comu.quadret", "comu.quadrets"), rectangles: quants(rs.length, "7.1.rectangle", "7.1.rectangles") }),
      n === 1 ? txt("7.1.divisor_u") : txt("7.1.divisors", { de_n: CE.deN(n), llista: llista(ds) }),
      n > 1 ? txt("7.1.cada_un") : "",
      primerOno(n),
    ];
    $("#d7-lectura").innerHTML = lectura(paraules);
    svg.setAttribute("aria-label", txtPla("7.1.aria", { n, llista: rs.map(r => r[0] + " per " + r[1]).join(", ") }));
    $("#d7-marca").hidden = n !== EX71;
  }

  let fet71 = false;
  function inicia71() {
    if (fet71) return;
    fet71 = true;
    CE.comptador($("#d7-n"), { et: txt("7.1.et"), min: 1, max: 48, valor: n71, aoCanviar: v => { n71 = v; pinta71(); } });
    pinta71();
  }

  /* ========================================== 7.2 · Troba els divisors ====== */

  const DIVIDIR = [12, 18, 20, 15, 16, 10, 14, 24, 30, 28];
  const N72 = 5;
  let t72 = null, n72 = 0, i72 = 0, triats = new Set();

  function pintaTria() {
    const resolt = t72.resolt(), bons = new Set(Q.divisorsDe(n72));
    $$(".pastilla", $("#d8-pastilles")).forEach(b => {
      const v = Number(b.dataset.v), marcat = triats.has(v);
      b.setAttribute("aria-pressed", String(marcat));
      b.classList.toggle("bona", resolt && bons.has(v));
      b.classList.toggle("mal", resolt && marcat && !bons.has(v));
      b.disabled = resolt;
    });
    $("#d8-comprova").disabled = resolt;
  }

  function pas72(i, e) {
    n72 = DIVIDIR[e.extra.ordre[i]];
    i72 = 0;
    triats = t72.resolt() ? new Set(Q.divisorsDe(n72)) : new Set();
    $("#d8-pregunta").textContent = txtPla("7.2.pregunta", { de_n: CE.deN(n72) });
    const cont = $("#d8-pastilles");
    cont.textContent = "";
    for (let v = 1; v <= n72; v++) {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "pastilla";
      b.dataset.v = String(v);
      b.textContent = String(v);
      b.onclick = () => { if (t72.resolt()) return; triats.has(v) ? triats.delete(v) : triats.add(v); pintaTria(); };
      cont.appendChild(b);
    }
    const svg = $("#d8-svg");
    if (t72.resolt()) Q.dibuixaRectangles(svg, n72) && svg.removeAttribute("hidden"); else svg.setAttribute("hidden", "");
    const avis = $("#d8-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t72.resolt() ? txt("comu.ja_fet") : txt("7.2.comenca");
    const seg = $("#d8-seguent");
    seg.disabled = !t72.resolt();
    seg.innerHTML = txt(t72.esUltim() ? "comu.acaba" : "comu.seguent");
    pintaTria();
  }

  function comprova72() {
    const e = t72.estat();
    if (!e || e.acabada || t72.resolt()) return;
    const bons = Q.divisorsDe(n72), avis = $("#d8-avis");
    const sobra = [...triats].filter(v => !bons.includes(v)).sort((a, b) => a - b);
    const falten = bons.filter(v => !triats.has(v));
    const svg = $("#d8-svg");
    if (!sobra.length && !falten.length) {
      t72.anota(i72 === 0 ? "be" : "pista");
      retroaccio(avis, "encert", txt("7.2.encert", { de_n: CE.deN(n72), llista: llista(bons) }));
      Q.dibuixaRectangles(svg, n72); svg.removeAttribute("hidden");
    } else if (i72 === 0) {
      i72 = 1;
      const x = sobra[0];
      const cos = x !== undefined
        ? txt(n72 % x === 1 ? "7.2.sobra_1" : "7.2.sobra", { el_x: majuscula(elNombre(x)), de_n: CE.deN(n72), x, r: n72 % x })
        : txt(falten.length === 1 ? "7.2.falta_1" : "7.2.falten", { n: falten.length });
      retroaccio(avis, "error", cos, txt("7.2.pista", { n: n72 }));
    } else {
      t72.anota("mostrat");
      triats = new Set(bons);
      retroaccio(avis, "mostra", txt("7.2.mostra", { de_n: CE.deN(n72), llista: llista(bons) }));
      Q.dibuixaRectangles(svg, n72); svg.removeAttribute("hidden");
    }
    pintaTria();
    $("#d8-seguent").disabled = !t72.resolt();
  }

  let fet72 = false;
  function inicia72() {
    if (fet72) return;
    fet72 = true;
    t72 = CE.tasca({
      tasca: 7, sub: 2,
      recorregut: $("#d8-recorregut"), represa: $("#d8-represa"), final: $("#d8-final"), cos: [$("#d8-cos")],
      desa: true,
      valida: e => e.total === N72 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N72 &&
                   e.extra.ordre.every(i => DIVIDIR[i] !== undefined),
      nom: () => "7.2 · " + txtPla("7.2.nom"),
      pinta: pas72
    });
    $("#d8-comprova").onclick = comprova72;
    $("#d8-seguent").onclick = () => t72.seguent();
    t72.inicia(() => ({ total: N72, extra: { ordre: CE.barreja(DIVIDIR.map((_, i) => i)).slice(0, N72) } }));
  }

  /* ==================================================== arrencada ====== */

  const ARRENCA = { 1: inicia71, 2: inicia72 };
  let subs = null, subActual = null;

  function inicia() {
    const arrel = $("#mod-divisors");
    if (!subs) {
      omplirTextos(arrel);
      subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); });
    }
    subs.mostra(subActual || CE.subDemanada(7) || 1);
  }

  CE.registra("divisors", inicia);
  CE.registraCataleg("7.2", { nom: txtPla("7.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")],
    resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { divisors: { EX71, DIVIDIR } });
})();
