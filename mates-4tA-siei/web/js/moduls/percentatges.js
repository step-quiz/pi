/* PERCENTATGES: FACTOR I QUOTES — mòdul «factor» de la caixa d'eines.
   Es registra sol; app.js no en sap res més que l'identificador. */
(function () {
  "use strict";
  const { $, $$, num, fix, euros, el, icona, pastilles, memoria } = CE;

  /* Dues maneres de pagar la mateixa compra:
     - mode «canvis»: preu de sortida i percentatges encadenats (el factor);
     - mode «quotes»: nombre de quotes per import de cada quota.
     El segon mode fa falta per a l'exercici 5 de la fitxa i per al producte
     final de la unitat, que compara comptat contra terminis. */
  const CANVIS = [
    { et: "+ IVA 21 %", p:  21 }, { et: "+ IVA 10 %", p:  10 },
    { et: "− 10 %",     p: -10 }, { et: "− 20 %",     p: -20 },
    { et: "− 30 %",     p: -30 }, { et: "− 50 %",     p: -50 }
  ];
  const opcions = {};

  function creaOpcio(id, cfg) {
    const arrel = $("#opcio-" + id);
    const estat = { mode: cfg.mode || "canvis", nom: cfg.nom,
                    preu: cfg.preu || 0, canvis: (cfg.canvis || []).slice(),
                    quotes: cfg.quotes || 0, import_: cfg.import_ || 0, final: 0 };

    arrel.innerHTML =
      '<h2>Opció ' + id + '</h2><p class="ajuda" id="n' + id + '"></p>' +
      '<div class="segments" style="margin:.2rem 0 1rem">' +
        '<button class="segment" data-m="canvis">Preu i canvis</button>' +
        '<button class="segment" data-m="quotes">Quotes</button></div>' +
      '<div id="mc' + id + '">' +
        '<span class="camp-et">Preu de sortida (€)</span>' +
        '<input type="number" id="p' + id + '" min="0" step="0.01" inputmode="decimal">' +
        '<div class="pastilles" id="x' + id + '" style="margin-top:.8rem"></div>' +
        '<ul class="canvis" id="l' + id + '"></ul>' +
        '<div class="passos" id="b' + id + '"></div>' +
      '</div>' +
      '<div id="mq' + id + '" hidden><div class="fila">' +
        '<div><span class="camp-et">Quantes quotes</span>' +
        '<input type="number" id="q' + id + '" min="0" step="1" inputmode="numeric"></div>' +
        '<div><span class="camp-et">Cada quota (€)</span>' +
        '<input type="number" id="i' + id + '" min="0" step="0.01" inputmode="decimal"></div>' +
        '</div><div class="passos" id="bq' + id + '"></div></div>' +
      '<hr class="divisor"><div class="et" id="f' + id + '"></div>' +
      '<div class="gran" id="t' + id + '" aria-live="polite"></div>';

    $("#n" + id).textContent = estat.nom;
    const pr = $("#p" + id), qt = $("#q" + id), im = $("#i" + id);
    pr.value = estat.preu; qt.value = estat.quotes; im.value = estat.import_;
    pr.oninput = () => { estat.preu    = Math.max(0, Number(pr.value) || 0); pinta(); };
    qt.oninput = () => { estat.quotes  = Math.max(0, Number(qt.value) || 0); pinta(); };
    im.oninput = () => { estat.import_ = Math.max(0, Number(im.value) || 0); pinta(); };

    $$(".segment", arrel).forEach(b => b.onclick = () => { estat.mode = b.dataset.m; pinta(); });

    const cx = $("#x" + id);
    CANVIS.forEach(c => {
      const b = document.createElement("button");
      b.className = "pastilla"; b.textContent = c.et;
      b.onclick = () => { estat.canvis.push(c.p); pinta(); };
      cx.appendChild(b);
    });

    /** Una fila de barra: etiqueta, import i barra proporcional. */
    function barra(cont, et, valor, maxim, classe) {
      const d = document.createElement("div"); d.className = "pas";
      d.innerHTML = '<div class="pas-cap"><span>' + et + "</span><b>" + euros(valor) + "</b></div>";
      const b = document.createElement("div");
      b.className = "barra " + classe;
      b.style.width = Math.max(2, valor / maxim * 100) + "%";
      d.appendChild(b); cont.appendChild(d);
    }

    function pinta() {
      const esCanvis = estat.mode === "canvis";
      $("#mc" + id).hidden = !esCanvis;
      $("#mq" + id).hidden = esCanvis;
      $$(".segment", arrel).forEach(b =>
        b.setAttribute("aria-selected", String(b.dataset.m === estat.mode)));

      if (esCanvis) {
        const llista = $("#l" + id); llista.textContent = "";
        if (!estat.canvis.length) {
          const li = document.createElement("li");
          li.className = "buit"; li.textContent = "Cap canvi encara.";
          llista.appendChild(li);
        }
        estat.canvis.forEach((p, i) => {
          const li = document.createElement("li");
          li.innerHTML = "<span>" + (p > 0 ? "+" : "−") + Math.abs(p) +
            ' %</span><span class="factor">× ' + num(1 + p / 100, 4) + "</span>";
          const x = document.createElement("button");
          x.className = "btn discret mini"; x.textContent = "Treu";
          x.setAttribute("aria-label", "Treu el canvi del " + p + " per cent");
          x.onclick = () => { estat.canvis.splice(i, 1); pinta(); };
          li.appendChild(x); llista.appendChild(li);
        });

        const vals = [estat.preu];
        estat.canvis.forEach(p => vals.push(vals[vals.length - 1] * (1 + p / 100)));
        const maxim = Math.max(...vals, 1);
        const cont = $("#b" + id); cont.textContent = "";
        vals.forEach((v, i) => barra(cont,
          i === 0 ? "Preu de sortida"
                  : (estat.canvis[i - 1] > 0 ? "+" : "−") + Math.abs(estat.canvis[i - 1]) + " %",
          v, maxim, i === 0 ? "base" : (estat.canvis[i - 1] > 0 ? "amunt" : "avall")));

        const total = estat.canvis.reduce((a, p) => a * (1 + p / 100), 1);
        estat.final = estat.preu * total;
        $("#f" + id).textContent = estat.canvis.length ? "Tot junt: × " + num(total, 4) : "Sense canvis";
      } else {
        estat.final = estat.quotes * estat.import_;
        const cont = $("#bq" + id); cont.textContent = "";
        const maxim = Math.max(estat.final, 1);
        barra(cont, "Cada quota", estat.import_, maxim, "base");
        barra(cont, estat.quotes + " quotes en total", estat.final, maxim, "amunt");
        $("#f" + id).textContent = estat.quotes + " × " + euros(estat.import_);
      }

      $("#t" + id).textContent = euros(estat.final);
      veredicte();
    }

    pinta();
    return estat;
  }

  function veredicte() {
    const A = opcions.A, B = opcions.B;
    if (!A || !B) return;
    const dif = Math.abs(A.final - B.final), cont = $("#veredicte");
    if (A.final === 0 && B.final === 0) { cont.innerHTML =
      '<div class="avis neutre">Omple les dues opcions.</div>'; return; }
    if (dif < 0.005) { cont.innerHTML =
      '<div class="avis pensa">Les dues costen el mateix.</div>'; return; }
    const g = A.final < B.final ? "A" : "B";
    cont.innerHTML =
      '<div class="et">Guanya</div><div class="gran">Opció ' + g + "</div>" +
      '<div class="avis be">Estalvies <b>' + euros(dif) + "</b>.</div>" +
      '<div class="avis neutre">«L\'opció ' + g + " surt més a compte perquè costa " +
      euros(dif) + ' menys.»</div>';
  }

  /* S'obre amb el cas de la pàgina 7 de la fitxa: el mòbil de 300 €. */
  const MODEL_A = { nom: "Al comptat, amb un 15 % de descompte", mode: "canvis",
                    preu: 300, canvis: [-15] };
  const MODEL_B = { nom: "A terminis, 12 quotes de 24 €", mode: "quotes",
                    quotes: 12, import_: 24 };

  function iniciaFactor() {
    if (opcions.A) return;
    opcions.A = creaOpcio("A", MODEL_A);
    opcions.B = creaOpcio("B", MODEL_B);
    veredicte();
    $("#factor-buida").onclick = () => {
      opcions.A = creaOpcio("A", { nom: "La teva opció", mode: "canvis", preu: 0, canvis: [] });
      opcions.B = creaOpcio("B", { nom: "La teva opció", mode: "quotes", quotes: 0, import_: 0 });
      $("#factor-marca").hidden = true;
      veredicte();
    };
  }

  CE.registra("factor", iniciaFactor);
})();
