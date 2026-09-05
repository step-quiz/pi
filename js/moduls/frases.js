/* COM HO DIC — mòdul «frases» de la caixa d'eines.
   Es registra sol; app.js no en sap res més que l'identificador. */
(function () {
  "use strict";
  const { $, $$, num, fix, euros, el, icona, pastilles, memoria } = CE;

  /* Cada tros és text fix, un buit { b } o una tria tancada { t }.
     El camp `m` és el model: el valor amb què s'obre la frase, ja resolta. */
  const FRASES = {
    "Unitat 1": [
      ["El nombre ", { b: 1, w: "5rem", m: "√7" }, " és entre ", { b: 1, w: "4rem", m: "2" },
       " i ", { b: 1, w: "4rem", m: "3" }, "."],
      ["L'he escrit amb ", { t: ["0", "1", "2", "3"], m: "2" }, " decimals."],
      ["Ho he fet així perquè ", { t: ["només ho havia de dir", "ho he de comprar", "ho he de tallar"],
        m: "ho he de comprar" }, "."]
    ],
    "Unitat 2": [
      ["He multiplicat per ", { b: 1, w: "5rem", m: "0,8" }, " perquè hi ha un ",
       { b: 1, w: "4rem", m: "20" }, " % ", { t: ["de descompte", "d'IVA", "de pujada"], m: "de descompte" }, "."],
      ["L'opció ", { t: ["A", "B"], m: "A" }, " costa ", { b: 1, w: "6rem", m: "290,40" }, " € en total."],
      ["Surt més a compte l'opció ", { t: ["A", "B"], m: "A" }, ", perquè costa ",
       { b: 1, w: "6rem", m: "108,90" }, " € menys."]
    ],
    "Unitat 3": [
      ["L'escala del plànol és 1 : ", { b: 1, w: "6rem", m: "100" }, "."],
      ["Cada centímetre del paper són ", { b: 1, w: "5rem", m: "1" }, " metres de veritat."],
      ["Al plànol fa ", { b: 1, w: "5rem", m: "8" }, " cm, o sigui ", { b: 1, w: "5rem", m: "8" }, " m de veritat."]
    ],
    "Unitat 6": [
      ["El punt més alt és a ", { b: 1, w: "5rem", m: "5" }, " metres."],
      ["Hi arriba al segon ", { b: 1, w: "4rem", m: "1" }, "."],
      ["Toca terra quan han passat ", { b: 1, w: "4rem", m: "2" }, " segons."]
    ],
    "Unitat 9": [
      ["En total hi ha ", { b: 1, w: "5rem", m: "8" }, " possibilitats."],
      ["D'aquestes, ", { b: 1, w: "5rem", m: "3" }, " em van bé."],
      ["La probabilitat és del ", { b: 1, w: "5rem", m: "37,5" }, " %."],
      [{ t: ["No em convé jugar", "Em convé jugar"], m: "No em convé jugar" }, ", perquè ",
       { t: ["tinc poques possibilitats de guanyar", "tinc moltes possibilitats de guanyar"],
         m: "tinc poques possibilitats de guanyar" }, "."]
    ]
  };
  let frasesClau = "Unitat 1";

  function pintaFrases(ambModel) {
    const cos = $("#frases-cos"); cos.textContent = "";
    FRASES[frasesClau].forEach((trossos, iF) => {
      const p = document.createElement("p"); p.className = "frase";
      trossos.forEach(tr => {
        if (typeof tr === "string") { p.appendChild(document.createTextNode(tr)); return; }
        // només la primera frase s'obre resolta, com el primer apartat de les fitxes
        const val = (ambModel && iF === 0) ? (tr.m ?? "") : "";
        if (tr.t) {
          const s = document.createElement("select");
          s.appendChild(new Option("…", ""));
          tr.t.forEach(o => s.appendChild(new Option(o, o)));
          s.value = val;
          p.appendChild(s);
        } else {
          const i = document.createElement("input");
          i.type = "text"; i.inputMode = "decimal"; i.style.width = tr.w;
          i.value = val; i.setAttribute("aria-label", "buit per omplir");
          p.appendChild(i);
        }
      });
      cos.appendChild(p);
    });
    $("#frases-avis").textContent = "";
  }

  function textFrases() {
    return $$(".frase", $("#frases-cos")).map(p => {
      let t = "";
      p.childNodes.forEach(n => {
        if (n.nodeType === 3) t += n.textContent;
        else if (n.tagName === "INPUT")  t += (n.value.trim() || "…");
        else if (n.tagName === "SELECT") t += (n.value || "…");
      });
      return t.replace(/\s+/g, " ").trim();
    }).join("\n");
  }

  function iniciaFrases() {
    if ($("#frases-pastilles").children.length) return;
    pastilles($("#frases-pastilles"), Object.keys(FRASES).map(k => ({ et: k })),
      it => { frasesClau = it.et; pintaFrases(it.et === "Unitat 1"); });
    pintaFrases(true);

    $("#frases-buida").onclick = () => pintaFrases(false);
    $("#frases-copia").onclick = async () => {
      const text = textFrases();
      try { await navigator.clipboard.writeText(text); $("#frases-avis").textContent = "Copiat."; }
      catch (e) {
        const ta = document.createElement("textarea");
        ta.value = text; document.body.appendChild(ta); ta.select();
        try { document.execCommand("copy"); $("#frases-avis").textContent = "Copiat."; }
        catch (e2) { $("#frases-avis").textContent = "Selecciona el text a mà."; }
        ta.remove();
      }
    };
  }

  CE.registra("frases", iniciaFrases);
})();
