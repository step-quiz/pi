/* RECTA I ESTIMACIÓ — mòdul «recta» de la caixa d'eines.
   Es registra sol; app.js no en sap res més que l'identificador. */
(function () {
  "use strict";
  const { $, $$, num, fix, euros, el, icona, pastilles, memoria } = CE;

  /* El primer nombre és el model, el mateix √7 de la fitxa de la Unitat 1. */
  const NOMBRES = [
    { et: "√7",  v: Math.sqrt(7)  },
    { et: "√5",  v: Math.sqrt(5)  },
    { et: "π",   v: Math.PI       },
    { et: "√11", v: Math.sqrt(11) },
    { et: "√30", v: Math.sqrt(30) }
  ];
  /* Els mateixos tres usos que a la fitxa impresa, amb els mateixos decimals. */
  const USOS = [
    { id: "parla",  et: "Ho dic",     dec: 1, frase: "De paraula no cal ser exacte." },
    { id: "compra", et: "Ho compro",  dec: 2, frase: "A la botiga es ven per centímetres." },
    { id: "talla",  et: "Ho tallo",   dec: 3, frase: "Si talles, el mil·límetre compta." }
  ];
  let rectaV = NOMBRES[0].v, rectaUs = null, rectaModel = true;

  function pintaRecta() {
    const svg = $("#recta-svg"); svg.textContent = "";
    const x0 = 34, x1 = 626, y = 76, max = 6;
    const px = t => x0 + t / max * (x1 - x0);
    const gris = "var(--etiqueta-3)", tinta = "var(--etiqueta)", sec = "var(--etiqueta-2)";

    const baix = Math.floor(rectaV), alt = baix + 1;
    svg.appendChild(el("rect", { x: px(baix), y: y - 13, width: px(alt) - px(baix), height: 26,
      rx: 6, style: "fill:var(--blau-suau)" }));
    svg.appendChild(el("line", { x1: x0, y1: y, x2: x1, y2: y, style: "stroke:" + gris,
      "stroke-width": 2 }));
    for (let i = 0; i <= max; i++) {
      svg.appendChild(el("line", { x1: px(i), y1: y - 8, x2: px(i), y2: y + 8,
        style: "stroke:" + gris, "stroke-width": 2 }));
      svg.appendChild(el("text", { x: px(i), y: y + 34, "text-anchor": "middle", "font-size": 18,
        style: "fill:" + sec, "font-family": "inherit" }, i));
    }
    svg.appendChild(el("line", { x1: px(rectaV), y1: y - 40, x2: px(rectaV), y2: y + 8,
      style: "stroke:var(--blau)", "stroke-width": 3, "stroke-linecap": "round" }));
    svg.appendChild(el("circle", { cx: px(rectaV), cy: y, r: 8, style: "fill:var(--blau)" }));
    svg.appendChild(el("text", { x: px(rectaV), y: y - 50, "text-anchor": "middle", "font-size": 21,
      "font-weight": 600, style: "fill:" + tinta, "font-family": "inherit" }, fix(rectaV, 4)));

    const prop = (rectaV - baix) < 0.5 ? baix : alt;
    $("#recta-avis").innerHTML = "És entre <b>" + baix + "</b> i <b>" + alt +
      "</b>, i més a prop del <b>" + prop + "</b>.";
  }

  function pintaTira() {
    const tira = $("#recta-tira"); tira.textContent = "";
    const dec = rectaUs ? rectaUs.dec : null;
    const s = fix(rectaV, 7);
    const coma = s.indexOf(",");
    const tall = dec === null ? s.length : coma + 1 + dec;   // sense tria, tot viu
    [...s].forEach((c, i) => {
      if (dec !== null && i === tall) {
        tira.appendChild(Object.assign(document.createElement("span"), { className: "tall" }));
      }
      const sp = document.createElement("span");
      sp.className = (dec === null || i < tall) ? "viu" : "mort";
      sp.textContent = c;
      tira.appendChild(sp);
    });
    const p = document.createElement("span"); p.className = "mort"; p.textContent = "…";
    tira.appendChild(p);

    $("#recta-resultat").textContent = dec === null ? "—" : fix(rectaV, dec);

    /* Arrodonir no és tallar: si la xifra següent és 5 o més, l'última puja.
       És l'error típic de la fitxa, i aquí es veu comparant la tira amb el
       resultat (per exemple, es conserva 2,64 però queda 2,65). */
    const nota = $("#recta-nota");
    if (dec === null) { nota.textContent = ""; return; }
    nota.textContent = (fix(rectaV, dec) !== s.slice(0, tall))
      ? "L'última xifra puja, perquè la següent és 5 o més."
      : "L'última xifra es queda igual.";
  }

  function iniciaRecta() {
    if ($("#recta-pastilles").children.length) return;

    pastilles($("#recta-pastilles"), NOMBRES, it => {
      rectaV = it.v;
      rectaModel = (it === NOMBRES[0]);
      $("#recta-marca").hidden = !rectaModel;
      pintaRecta(); pintaTira();
    });

    const cont = $("#recta-precisio");
    USOS.forEach((u, i) => {
      const b = document.createElement("button");
      b.setAttribute("aria-pressed", i === 1);         // el model: «Ho compro», 2 decimals
      b.appendChild(icona("i-" + u.id, 28));
      const e = document.createElement("div"); e.className = "et"; e.textContent = u.et;
      const d = document.createElement("div"); d.style.fontWeight = 600;
      d.textContent = u.dec + (u.dec === 1 ? " decimal" : " decimals");
      b.append(e, d);
      b.onclick = () => {
        $$("button", cont).forEach(x => x.setAttribute("aria-pressed", "false"));
        b.setAttribute("aria-pressed", "true");
        rectaUs = u; pintaTira();
      };
      cont.appendChild(b);
    });

    rectaUs = USOS[1];
    pintaRecta(); pintaTira();
  }

  CE.registra("recta", iniciaRecta);
})();
