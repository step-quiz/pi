/* CALCULADORA CASIO fx-82SP CW — mòdul «calc» de la caixa d'eines.
   Es registra sol; app.js no en sap res més que l'identificador. */
(function () {
  "use strict";
  const { $, $$, num, fix, euros, el, icona, pastilles, memoria } = CE;

  /* AVÍS DE DISSENY: aquí només hi ha les tecles de les quals es pot estar segur
     —xifres, punt, les quatre operacions, =, AC, DEL— i que són justament les
     úniques que calen. El mètode del factor multiplicador NO fa servir la tecla
     de percentatge, i això és un dels seus avantatges.
     Les dues tecles de la zona de dalt (arrel i FORMAT) i la seva serigrafia
     convindria contrastar-les amb l'aparell real; si no coincideixen, només cal
     canviar l'etiqueta a TECLES_DALT i a la casella `k` del pas corresponent.

     SEPARADOR DECIMAL: si les vostres calculadores estan configurades amb coma,
     canvieu la constant de sota i es propaga a tot el mòdul. */
  const SEP_DECIMAL = ".";

  const TECLES_DALT = [{ k: "√", et: "√▢" }, { k: "FORMAT", et: "FORMAT", petita: true }];
  const TECLES_BAIX = [
    { k: "7" }, { k: "8" }, { k: "9" }, { k: "DEL", petita: true }, { k: "AC", petita: true },
    { k: "4" }, { k: "5" }, { k: "6" }, { k: "×", op: true }, { k: "÷", op: true },
    { k: "1" }, { k: "2" }, { k: "3" }, { k: "+", op: true }, { k: "−", op: true },
    { k: "0" }, { k: SEP_DECIMAL }, { k: "×10ˣ", petita: true }, { k: "Ans", petita: true },
    { k: "=", op: true }
  ];

  const CASOS_CALC = [
    { et: "Rebaixa del 20 %",
      context: "Una samarreta de 25 € amb un 20 % de descompte.",
      passos: [{ k: "2" }, { k: "5" }, { k: "×" }, { k: "0" }, { k: SEP_DECIMAL }, { k: "8" },
               { k: "=", res: "20" }],
      final: "La samarreta costa 20 €." },
    { et: "Afegir l'IVA",
      context: "Uns auriculars de 40 € sense IVA. L'IVA és del 21 %.",
      passos: [{ k: "4" }, { k: "0" }, { k: "×" }, { k: "1" }, { k: SEP_DECIMAL }, { k: "2" },
               { k: "1" }, { k: "=", res: "48.4" }],
      final: "Amb l'IVA costen 48,40 €." },
    { et: "Dos canvis seguits",
      context: "Una bici de 300 €: primer un 20 % de descompte i després el 21 % d'IVA.",
      passos: [{ k: "3" }, { k: "0" }, { k: "0" }, { k: "×" }, { k: "0" }, { k: SEP_DECIMAL },
               { k: "8" }, { k: "×" }, { k: "1" }, { k: SEP_DECIMAL }, { k: "2" }, { k: "1" },
               { k: "=", res: "290.4" }],
      final: "La bici costa 290,40 €." },
    { et: "Total a terminis",
      context: "Un mòbil a terminis: 12 quotes de 24 € cadascuna.",
      passos: [{ k: "1" }, { k: "2" }, { k: "×" }, { k: "2" }, { k: "4" }, { k: "=", res: "288" }],
      final: "En total pagues 288 €." },
    { et: "Arrel quadrada",
      context: "Quant fa √7?",
      passos: [{ k: "√" }, { k: "7" }, { k: "=", res: "√7" },
               { k: "FORMAT", res: "2.6457513" }],
      final: "√7 és 2,6457513…" }
  ];

  let cas = CASOS_CALC[0], pas = 0;

  /** Text de la línia d'entrada: totes les tecles premudes que s'escriuen. */
  function entradaFinsA(i) {
    return cas.passos.slice(0, i + 1)
      .map(p => p.k).filter(k => k !== "=" && k !== "FORMAT" && k !== "AC" && k !== "DEL")
      .join("");
  }
  function llegendaDe(k, i) {
    if (k === "=") return "Prem igual.";
    if (k === "FORMAT") return "Aquesta tecla ensenya els decimals.";
    if (k === "×") return "Prem multiplicar.";
    if (k === SEP_DECIMAL) return "El punt fa de coma.";
    if (k === "√") return "Prem l'arrel quadrada.";
    const jaHiHaOperador = cas.passos.slice(0, i).some(p => p.k === "×");
    return jaHiHaOperador ? "Escriu el factor, xifra a xifra." : "Escriu el número, xifra a xifra.";
  }

  function pintaCalc() {
    const actual = cas.passos[pas];
    $("#calc-entrada").textContent = entradaFinsA(pas) || "\u00A0";
    const res = cas.passos.slice(0, pas + 1).reduce((a, p) => p.res ?? a, null);
    $("#calc-res").textContent = res ?? "\u00A0";

    $$(".tecla").forEach(t => t.classList.toggle("ara", t.dataset.k === actual.k));
    $("#calc-llegenda").textContent = llegendaDe(actual.k, pas);
    $("#calc-progres").textContent = "Tecla " + (pas + 1) + " de " + cas.passos.length;
    $("#calc-arrere").disabled = pas === 0;
    $("#calc-endavant").disabled = pas === cas.passos.length - 1;
    $("#calc-endavant").textContent = pas === cas.passos.length - 1 ? "Ja està" : "Següent tecla";
    $("#calc-final").textContent = pas === cas.passos.length - 1 ? cas.final : "—";
  }

  function iniciaCalc() {
    if ($("#calc-pastilles").children.length) return;

    const munta = (cont, llista) => {
      llista.forEach(t => {
        const b = document.createElement("div");
        b.className = "tecla" + (t.op ? " op" : "") + (t.petita ? " petita" : "");
        b.dataset.k = t.k;
        b.textContent = t.et || t.k;
        cont.appendChild(b);
      });
    };
    munta($("#calc-dalt"), TECLES_DALT);
    munta($("#calc-baix"), TECLES_BAIX);

    pastilles($("#calc-pastilles"), CASOS_CALC, c => {
      cas = c; pas = 0;
      $("#calc-context").textContent = cas.context;
      pintaCalc();
    });

    $("#calc-arrere").onclick   = () => { if (pas > 0) { pas--; pintaCalc(); } };
    $("#calc-endavant").onclick = () => { if (pas < cas.passos.length - 1) { pas++; pintaCalc(); } };

    $("#calc-context").textContent = cas.context;
    pintaCalc();
  }

  CE.registra("calc", iniciaCalc);
})();
