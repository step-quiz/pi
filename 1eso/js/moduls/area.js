/* ============================================================================
   L'ÀREA — mòdul «area» de la caixa d'eines · tasca 13 · unitat 3
   ----------------------------------------------------------------------------
   L'àrea és quants quadrets ocupa una figura. Els trossos de mig quadret es
   compten de dos en dos: dos mitjos fan un quadret (1/2 + 1/2 = 1). Activitats
   «Com podem mesurar àrees?» i «Sumem àrees irregulars usant les fraccions» de
   la situació d'aprenentatge «Com és de gran Gaza?».
   13.1 · COMPTA L'ÀREA   cinc figures fetes de quadrets sencers i mitjos. S'obre
                          amb la casa: 14 sencers i 2 mitjos, 15 quadrets.
   13.2 · QUINA ÀREA TÉ?  tasca tancada de cinc passos. Les dues respostes falses
                          són les confusions de debò: comptar els mitjos com a
                          sencers, i no comptar-los.
   ========================================================================== */
(function () {
  "use strict";
  const { $, $$, txt, txtPla, omplirTextos, retroaccio, lectura, quants } = CE;
  const Q = CE.q;
  // Cada figura, fila a fila: «#» un quadret sencer; ◢ ◣ ◤ ◥ mig quadret (el triangle ple).
  const FIGURES = [
    { nom: "casa",    files: [".◢##◣.", ".####.", ".####.", ".####."] },
    { nom: "fletxa",  files: ["..◢◣..", ".◢##◣.", "######", "..##.."] },
    { nom: "rombe",   files: [".◢◣.", "◢##◣", "◥##◤", ".◥◤."] },
    { nom: "vaixell", files: ["...#...", "..##...", ".###...", "#######", ".◥###◤."] },
    { nom: "ela",     files: ["##...", "##...", "##...", "#####"] },
    { nom: "teulada", files: ["◢###◣", "#####", "#####"] },
  ];
  const MEITATS = "◢◣◤◥";
  function compta(f) {
    let s = 0, m = 0;
    f.files.forEach(r => [...r].forEach(c => { if (c === "#") s++; else if (MEITATS.includes(c)) m++; }));
    return { s, m, area: s + m / 2 };
  }
  CE.comptaArea = compta;

  function dibuixa(svg, f) {
    svg.textContent = "";
    const rows = f.files.length, cols = Math.max(...f.files.map(r => [...r].length));
    const m = Math.min(46, 360 / (cols + 2), 300 / (rows + 2)), x0 = m, y0 = m;
    Q.graella(svg, 0, 0, rows + 2, cols + 2, m);
    f.files.forEach((r, fi) => [...r].forEach((c, co) => {
      const x = x0 + co * m, y = y0 + fi * m;
      if (c === "#") Q.quadret(svg, x, y, m, "q");
      const tri = { "◢": [[x + m, y], [x + m, y + m], [x, y + m]], "◣": [[x, y], [x, y + m], [x + m, y + m]],
                    "◤": [[x, y], [x + m, y], [x, y + m]], "◥": [[x, y], [x + m, y], [x + m, y + m]] }[c];
      if (tri) {
        const p = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        p.setAttribute("points", tri.map(q => q.join(",")).join(" "));
        p.setAttribute("class", "q");
        svg.appendChild(p);
      }
    }));
    svg.setAttribute("viewBox", "0 0 " + Math.round((cols + 2) * m) + " " + Math.round((rows + 2) * m));
  }

  /** «2 mitjos fan 1 quadret» (o «3 mitjos fan 1 quadret i mig»). */
  function mitjos(m) {
    const q = n => quants(n, "13.1.quadret", "13.1.quadrets");
    return m % 2 === 0 ? txt("13.1.mitjos_fan", { m, q: q(m / 2) }) : txt("13.1.mitjos_fan_mig", { m, q: q((m - 1) / 2) });
  }

  /* ============================================== 13.1 · Compta l'àrea ====== */
  let i1 = 0;
  function pinta1() {
    const f = FIGURES[i1], c = compta(f);
    dibuixa($("#aa-svg"), f);
    $("#aa-svg").setAttribute("aria-label", txtPla("13.1.aria", { nom: txtPla("13.1.fig_" + f.nom), s: c.s, m: c.m }));
    const par = [txt("13.1.sencers", { s: c.s }), c.m ? txt("13.1.hi_ha_mitjos", { m: c.m }) : txt("13.1.cap_mig")];
    if (c.m) par.push(mitjos(c.m));
    par.push(txt("13.1.km2", { a: c.area }));
    $("#aa-lectura").innerHTML = lectura(par, txt("13.1.area", { a: c.area }));
    $("#aa-marca").hidden = i1 !== 0;
  }
  let fet1 = false;
  function inicia1() {
    if (fet1) return; fet1 = true;
    CE.pastilles($("#aa-figures"), FIGURES.map((f, k) => ({ et: txtPla("13.1.fig_" + f.nom), k })), t => { i1 = t.k; pinta1(); }, 0);
    pinta1();
  }

  /* ============================================ 13.2 · Quina àrea té? ====== */
  const AMB_MITJOS = FIGURES.map((f, k) => k).filter(k => compta(FIGURES[k]).m > 0);
  const N2 = 5;
  let t2 = null, f2 = null, i2 = 0, opcions2 = [];
  function pas2(i, e) {
    f2 = FIGURES[e.extra.ordre[i]]; i2 = 0;
    dibuixa($("#ab-svg"), f2);
    const c = compta(f2);
    const totes = [["bona", c.area], ["sencers", c.s + c.m], ["sense", c.s]];
    opcions2 = e.extra.torns[i].map(k => totes[k]);
    const cont = $("#ab-opcions");
    cont.innerHTML = opcions2.map((o, k) => '<button type="button" class="btn opcio-sino opcio-area" data-k="' + k + '">' +
      txt("13.2.opcio", { a: o[1] }) + "</button>").join("");
    $$(".opcio-area", cont).forEach(b => { b.onclick = () => tria2(Number(b.dataset.k), b); });
    const avis = $("#ab-avis");
    avis.className = "avis neutre";
    avis.innerHTML = t2.resolt() ? txt("comu.ja_fet") : txt("13.2.comenca");
    $("#ab-seguent").disabled = !t2.resolt();
    $("#ab-seguent").innerHTML = txt(t2.esUltim() ? "comu.acaba" : "comu.seguent");
    if (t2.resolt()) marca();
  }
  function marca() { $$(".opcio-area", $("#ab-opcions")).forEach(b => { b.disabled = true; b.classList.toggle("bona", opcions2[b.dataset.k][0] === "bona"); }); }
  function tria2(k, boto) {
    const e = t2.estat();
    if (!e || e.acabada || t2.resolt()) return;
    const c = compta(f2), o = opcions2[k], avis = $("#ab-avis");
    const frase = txt("13.2.encert", { s: c.s, m: c.m, a: c.area });
    if (o[0] === "bona") { t2.anota(i2 === 0 ? "be" : "pista"); retroaccio(avis, "encert", frase); marca(); }
    else if (i2 === 0) {
      i2 = 1; boto.classList.add("mal"); boto.disabled = true;
      retroaccio(avis, "error", txt(o[0] === "sencers" ? "13.2.error_sencers" : "13.2.error_sense"), txt("13.2.pista"));
    } else { t2.anota("mostrat"); retroaccio(avis, "mostra", frase); marca(); }
    $("#ab-seguent").disabled = !t2.resolt();
  }
  let fet2 = false;
  function inicia2() {
    if (fet2) return; fet2 = true;
    t2 = CE.tasca({
      tasca: 13, sub: 2,
      recorregut: $("#ab-recorregut"), represa: $("#ab-represa"), final: $("#ab-final"), cos: [$("#ab-cos")],
      desa: true,
      valida: e => e.total === N2 && e.extra && Array.isArray(e.extra.ordre) && e.extra.ordre.length === N2 &&
                   e.extra.ordre.every(i => FIGURES[i] !== undefined) && Array.isArray(e.extra.torns),
      nom: () => "13.2 · " + txtPla("13.2.nom"),
      pinta: pas2
    });
    $("#ab-seguent").onclick = () => t2.seguent();
    t2.inicia(() => {
      const ordre = CE.barreja(AMB_MITJOS).slice(0, N2);
      return { total: N2, extra: { ordre, torns: ordre.map(() => CE.barreja([0, 1, 2])) } };
    });
  }

  const ARRENCA = { 1: inicia1, 2: inicia2 };
  let subs = null, subActual = null;
  function inicia() {
    const arrel = $("#mod-area");
    if (!subs) { omplirTextos(arrel); subs = CE.subtasques(arrel, n => { subActual = n; ARRENCA[n](); }); }
    subs.mostra(subActual || CE.subDemanada(13) || 1);
  }
  CE.registra("area", inicia);
  CE.registraCataleg("13.2", { nom: txtPla("13.2.nom"),
    recomptes: [txtPla("comu.r_passos"), txtPla("comu.r_primer"), txtPla("comu.r_pista")], resta: txtPla("comu.r_mostrat") });
  CE.dades = Object.assign(CE.dades || {}, { area: { FIGURES, AMB_MITJOS } });
})();
