/* ============================================================================
   SUMAR DECIMALS — mòdul «sumadec» de la caixa d'eines · tasca 20 · unitat 5
   ----------------------------------------------------------------------------
   Sumar decimals és sumar quadrats amb quadrats, columnes amb columnes i
   quadrets amb quadrets: és posar la coma sota la coma. Restar és treure'n.
   Són els blocs de la tasca 18, i les sumes de la unitat 1 (centenes, desenes
   i unitats), un lloc més a la dreta. Activitat 3 de la situació «Decimals i
   arrel quadrada» (el llibre: «Operacions amb decimals»).

   Sempre sense portar-ne (docs/CRITERIS-DISSENY.md, regla D): cap xifra de
   cap lloc no passa de 9, i a les restes cap xifra de dalt no és més petita
   que la de sota. Multiplicar i dividir decimals queden fora (el pla validat
   el 29/9/2026).

   20.1 · SUMA I RESTA   cinc operacions per triar. La suma o la resta en
                         columna, amb la coma sota la coma i el zero que
                         iguala les xifres (2,5 és 2,50), els blocs del
                         resultat (el segon sumand, amb un altre color i el
                         traç discontinu; el que es resta, buit i ratllat) i
                         el compte de cada lloc. S'obre amb 2,5 + 1,35, el cas
                         de la regla trencada de la fitxa.
   20.2 · QUANT ÉS?      tasca tancada de cinc passos: una operació i tres
                         resultats. Les dolentes són les confusions de debò:
                         posar les xifres a la dreta, sense mirar la coma
                         (2,5 + 1,35 = 1,60), i sumar els trossos de després
                         de la coma com si fossin de la mateixa mena (5 + 35 =
                         40, i 3,40). En contestar, surt
                         l'operació en columna.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, lectura } = CE;
  const Q = CE.q;
  const dec = Q.dec;
  const xifres = c => ({ u: Math.floor(c / 100), d: Math.floor(c / 10) % 10, c: c % 10 });

  // [a, b, resta?] en centèsimes. Cap de les operacions no porta.
  const OPS = [[250, 135, false], [320, 145, false], [150, 225, false], [585, 230, true], [475, 150, true]];
  const CASOS2 = [[250, 135, false], [320, 145, false], [150, 225, false], [410, 135, false],
                  [585, 230, true], [475, 150, true], [368, 140, true]];

  const resultat = ([a, b, r]) => (r ? a - b : a + b);
  const signe = r => (r ? "−" : "+");

  /** L'operació en columna: la coma sota la coma, i tots amb dues xifres decimals. */
  function columna([a, b, r]) {
    const fila = (op, c, cls) => {
      const x = xifres(c);
      return '<tr' + (cls ? ' class="' + cls + '"' : "") + '><td class="op">' + op + "</td><td>" + x.u +
        "</td><td>,</td><td>" + x.d + "</td><td>" + x.c + "</td></tr>";
    };
    return '<table class="columna" aria-label="' + dec(a, 2) + " " + signe(r) + " " + dec(b, 2) + " = " +
      dec(resultat([a, b, r]), 2) + '"><tbody>' + fila("", a) + fila(signe(r), b) +
      fila("=", resultat([a, b, r]), "resultat") + "</tbody></table>";
  }
  const escrit = ([a, b, r]) => dec(a) + " " + signe(r) + " " + dec(b);

  /* ============================================== 20.1 · Suma i resta ====== */

  let k1 = 0;
  function pinta1() {
    const op = OPS[k1], [a, b, r] = op, x = xifres(a), y = xifres(b), z = xifres(resultat(op));
    $("#sc-columna").innerHTML = columna(op);
    // Suma: els blocs del resultat, amb el segon sumand marcat. Resta: els del primer,
    // amb el que es treu buit i ratllat.
    Q.blocs($("#sc-blocs"), r ? { c: x.u, d: x.d, u: x.c, b: { c: y.u, d: y.d, u: y.c }, treu: true }
                              : { c: z.u, d: z.d, u: z.c, b: { c: y.u, d: y.d, u: y.c } });
    $("#sc-blocs").setAttribute("aria-label", txtPla(r ? "20.1.aria_resta" : "20.1.aria_suma",
      { a: dec(a), b: dec(b), r: dec(resultat(op)) }));
    const s = signe(r), par = [txt(r ? "20.1.resta" : "20.1.suma")];
    [a, b].forEach(c => { if (c % 10 === 0 && c % 100) par.push(txt("20.1.zero", { n: dec(c), n2: dec(c, 2) })); });
    const calcul = (a_, b_, r_) => ({ calcul: a_ + " " + s + " " + b_ + " = " + r_ });
    par.push(txt("20.1.u", calcul(x.u, y.u, z.u)), txt("20.1.d", calcul(x.d, y.d, z.d)),
             txt("20.1.c", calcul(x.c, y.c, z.c)));
    $("#sc-lectura").innerHTML = lectura(par, escrit(op) + " = " + dec(resultat(op)));
    $("#sc-marca").hidden = k1 !== 0;
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    CE.pastilles($("#sc-ops"), OPS.map((op, k) => ({ et: escrit(op), k })), t => { k1 = t.k; pinta1(); }, 0);
    pinta1();
  }

  /* ================================================== 20.2 · Quant és? ====== */

  const N2 = 5;
  let t2 = null, op2 = null, i2 = 0, opcions2 = [];
  /** Les xifres d'un decimal escrit, sense la coma: «2,5» → 25. */
  const senseComa = c => Number(dec(c).replace(",", ""));
  /** La bona; les xifres a la dreta, sense mirar la coma (25 + 135 = 160 → 1,60); i
      sumar els trossos de després de la coma com si fossin iguals (5 + 35 = 40 → 3,40). */
  function opcionsDe(op) {
    const [a, b, r] = op, fa = c => Number((dec(c).split(",")[1] || "0"));
    const dreta = r ? senseComa(a) - senseComa(b) : senseComa(a) + senseComa(b);
    const ua = Math.floor(a / 100), ub = Math.floor(b / 100);
    const parts = (r ? ua - ub : ua + ub) * 100 + (r ? fa(a) - fa(b) : fa(a) + fa(b));
    return [["bona", dec(resultat(op))], ["dreta", dec(dreta)], ["parts", dec(parts)]];
  }
  function pas2(i, e) {
    op2 = CASOS2[e.extra.ordre[i]]; i2 = 0;
    $("#sd-pregunta").textContent = escrit(op2);
    opcions2 = e.extra.torns[i].map(k => opcionsDe(op2)[k]);
    const cont = $("#sd-opcions");
    cont.innerHTML = opcions2.map((op, k) => '<button type="button" class="btn opcio-sino opcio-dec" data-k="' + k + '">' +
      op[1] + "</button>").join("");
    $$(".opcio-dec", cont).forEach(b => { b.onclick = () => tria2(Number(b.dataset.k), b); });
    $("#sd-columna").innerHTML = columna(op2);
    $("#sd-columna").hidden = !t2.resolt();
    const avis = $("#sd-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("20.2.comenca");
    $("#sd-seguent").disabled = !t2.resolt();
    $("#sd-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca2();
  }
  function marca2() {
    $$(".opcio-dec", $("#sd-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", opcions2[b.dataset.k][0] === "bona"); });
    // L'operació en columna, amb la coma sota la coma: és el que desmunta l'error.
    $("#sd-columna").hidden = false;
  }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const op = opcions2[k], avis = $("#sd-avis"), [a, b, r] = op2;
    const frase = txt("20.2.encert", { calcul: dec(a, 2) + " " + signe(r) + " " + dec(b, 2) + " = " + dec(resultat(op2), 2) });
    if (op[0] === "bona") { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca2(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(op[0] === "dreta" ? "20.2.error_dreta" : "20.2.error_parts"),
                 txt("18.3.pista", { a: dec(a, 2), b: dec(b, 2) }));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca2(); }
    $("#sd-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 20, sub: 2,
      recorregut: $("#sd-recorregut"), represa: $("#sd-represa"), final: $("#sd-final"), cos: [$("#sd-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => CASOS2[i] !== undefined) && Array.isArray(e.extra.torns),
      nom: () => "20.2 · " + txtPla("20.2.nom"),
      pinta: pas2
    });
    $("#sd-seguent").onclick = () => t2.seguent();
    // Cinc passos: tres sumes i dues restes, barrejades.
    t2.inicia(() => {
      const sumes = CASOS2.map((c, i) => i).filter(i => !CASOS2[i][2]);
      const restes = CASOS2.map((c, i) => i).filter(i => CASOS2[i][2]);
      const ordre = CE.barreja(CE.barreja(sumes).slice(0, 3).concat(CE.barreja(restes).slice(0, 2)));
      return { total: N2, extra: { ordre, torns: ordre.map(() => CE.barreja([0, 1, 2])) } };
    });
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-sumadec");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(20) || 1);
  }
  CE.registra("sumadec", inicia);
  CE.registraCataleg("20.2", { nom: txtPla("20.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { sumadec: { OPS, CASOS2, opcionsDe } });
})();
