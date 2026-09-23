/* CALCULADORA CASIO fx-82SP CW — mòdul «calc» de la caixa d'eines.
   Es registra sol; app.js no en sap res més que l'identificador.

   EL BUCLE: l'alumnat prem la tecla a la calculadora de veritat i avança aquí.
   Per això el que es veu a la pantalla ha de ser exactament el que surt a
   l'aparell, i la tecla s'ha de dir igual que la serigrafia.

   CONTRASTAT AMB EL MANUAL OFICIAL DE CASIO (fx-82SP CW / fx-85SP CW)
     · La tecla d'executar és EXE. No hi ha cap tecla «=».
     · La pantalla dona 10 xifres: √7 surt 2.645751311.
     · En escriure, el decimal SEMPRE és un punt. El menú «Símbolo decimal»
       només canvia com surten els resultats.
     · De fàbrica (Entrada/Salida = E Mat/S Mat) la calculadora prefereix les
       fraccions: 40 × 1.21 EXE dona 242/5. Per veure 48.4 cal prémer SHIFT i
       després EXE (≈) en comptes d'EXE, o tenir-la configurada en E Mat/S Decimal.
     · FORMAT obre un menú (Estándar, Decimal…). Amb E Mat/S Decimal no cal,
       i per això aquí no surt: només hi ha les tecles que fan falta de debò.
   El que el manual no pot dir i s'ha de mirar a l'aparell és a docs/CONTINUAR.md.

   TECLAT DE L'ORDINADOR: prémer la mateixa tecla també avança (vegeu TECLAT).
   Així el gest de «prem aquesta tecla» és el mateix a tot arreu. */
(function () {
  "use strict";
  const { $, $$, txt, omplirTextos } = CE;

  /* ============ COM ESTAN CONFIGURADES LES CALCULADORES DEL CENTRE ============
     Menú de la calculadora: CONFIG → Config cálculo → Entrada/Salida.
       "E Mat/S Decimal"  els resultats surten en decimal. És el que recomanem:
                          el material treballa amb decimals i així la pantalla
                          de l'app i la de l'aparell coincideixen sempre.
       "E Mat/S Mat"      el valor de fàbrica. Els resultats amb decimals surten
                          en fracció, i els casos afegeixen SHIFT abans d'EXE (≈). */
  const ENTRADA_SORTIDA = "E Mat/S Decimal";

  /* Menú CONFIG → Símbolo decimal. Posa-hi "," si les calculadores ensenyen
     els resultats amb coma. Només afecta la línia del resultat: l'entrada i la
     tecla sempre són un punt, perquè l'aparell ho fa així. */
  const SEP_DECIMAL = ".";

  const AMB_FRACCIONS = ENTRADA_SORTIDA === "E Mat/S Mat";

  /* Les tecles del mapa, amb la mateixa serigrafia que l'aparell. Només les que
     fan servir els casos: un mapa amb tecles que no es premen mai és soroll. */
  const TECLES_DALT = (AMB_FRACCIONS ? [{ k: "SHIFT", petita: true }] : [])
    .concat([{ k: "√", et: "√▢" }]);
  const TECLES_BAIX = [
    { k: "7" }, { k: "8" }, { k: "9" }, { k: "DEL", petita: true }, { k: "AC", petita: true },
    { k: "4" }, { k: "5" }, { k: "6" }, { k: "×", op: true }, { k: "÷", op: true },
    { k: "1" }, { k: "2" }, { k: "3" }, { k: "+", op: true }, { k: "−", op: true },
    { k: "0" }, { k: "." }, { k: "×10ˣ", petita: true }, { k: "Ans", ans: true },
    { k: "EXE", op: true, petita: true }
  ];

  /* Els casos. `tecles` és el que s'escriu; l'execució (EXE, o SHIFT i EXE) la
     posa passosDe() segons la configuració. `res` és la pantalla de l'aparell
     amb E Mat/S Decimal i punt decimal, tal qual.
     Les frases i els números van junts al codi, com els preus de l'exercici 1.4:
     si es poguessin canviar per separat, la frase podria dir un preu que no és. */
  const CASOS_CALC = [
    { et: "Rebaixa 20 %",
      context: "Una samarreta de 25 € amb un 20 % de descompte.",
      tecles: ["2", "5", "×", "0", ".", "8"], res: "20",
      final: "La samarreta costa 20 €." },
    { et: "IVA",
      context: "Uns auriculars de 40 € sense IVA. L'IVA és del 21 %.",
      tecles: ["4", "0", "×", "1", ".", "2", "1"], res: "48.4",
      final: "Amb l'IVA costen 48,40 €." },
    { et: "Dos canvis",
      context: "Una bici de 300 €. Primer, un 20 % de descompte. Després, el 21 % d'IVA.",
      tecles: ["3", "0", "0", "×", "0", ".", "8", "×", "1", ".", "2", "1"], res: "290.4",
      final: "La bici costa 290,40 €." },
    { et: "Terminis",
      context: "Un mòbil a terminis: 12 quotes de 24 € cadascuna.",
      tecles: ["1", "2", "×", "2", "4"], res: "288",
      final: "En total pagues 288 €." },
    { et: "Arrel",
      context: "Quant fa √7?",
      tecles: ["√", "7"], res: "2.645751311",
      final: "√7 és 2,645751311… Els decimals no s'acaben." }
  ];

  /** Les tecles d'un cas, amb l'execució que toca segons la configuració.
      Amb fraccions, un resultat que no és sencer es demana amb SHIFT i EXE (≈),
      que és el que diu el manual per obtenir-lo directament en decimal. */
  function passosDe(c) {
    const escriu = c.tecles.map(k => ({ k }));
    const decimal = !/^\d+$/.test(c.res);
    const executa = (AMB_FRACCIONS && decimal)
      ? [{ k: "SHIFT" }, { k: "EXE", res: c.res }]
      : [{ k: "EXE", res: c.res }];
    return escriu.concat(executa);
  }

  /* TECLAT DE L'ORDINADOR → tecla de la calculadora. La coma també val per al
     punt, perquè és la tecla que busca qui escriu decimals en català. Les tecles
     que no tenen equivalent (√, SHIFT…) s'avancen amb el botó o amb la fletxa →. */
  const TECLAT = {
    "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
    "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
    ".": ".", ",": ".", "Decimal": ".",
    "*": "×", "x": "×", "X": "×", "/": "÷", ":": "÷", "+": "+", "-": "−",
    "Enter": "EXE", "=": "EXE", "Backspace": "DEL", "Delete": "DEL", "Escape": "AC"
  };

  let cas = CASOS_CALC[0], passos = passosDe(cas), tasca = null;

  /** Text de la línia d'entrada: les tecles que escriuen alguna cosa. */
  function entradaFinsA(i) {
    return passos.slice(0, i + 1).map(p => p.k)
      .filter(k => !["EXE", "SHIFT", "AC", "DEL"].includes(k)).join("");
  }
  const perPantalla = res => res.replace(".", SEP_DECIMAL);

  function pintaPas(i) {
    const actual = passos[i];
    $("#calc-entrada").textContent = entradaFinsA(i) || "\u00A0";
    const res = passos.slice(0, i + 1).reduce((a, p) => p.res ?? a, null);
    $("#calc-res").textContent = res ? perPantalla(res) : "\u00A0";

    // la tecla del pas batega i es pot tocar per avançar
    $$("#mod-calc .tecla").forEach(t => t.classList.toggle("ara", t.dataset.k === actual.k));

    $("#calc-arrere").disabled = i === 0;
    const endavant = $("#calc-endavant");
    endavant.innerHTML = txt(i === passos.length - 1 ? "0.acaba" : "0.seguent");
    // mentre queden tecles, el botó demana que el toquin
    endavant.classList.toggle("crida", i < passos.length - 1);
  }

  /** Cada tecla s'anota com a feta en passar-la: aquí no hi ha res a encertar. */
  function avanca() {
    const e = tasca.estat();
    if (!e || e.acabada) return;
    tasca.anota("be");
    tasca.seguent();
  }

  function nouCas(c) {
    cas = c; passos = passosDe(cas);
    $("#calc-context").textContent = cas.context;
    tasca.comenca({ total: passos.length, cas: CASOS_CALC.indexOf(cas) });
    // el focus va al botó del pas: és el que es fa servir tot seguit
    $("#calc-endavant").focus({ preventScroll: true });
  }

  /** Avança només si la tecla premuda és la del pas. Una tecla equivocada no fa
      res ni diu res: aquí no s'avalua, només s'acompanya. */
  function teclaFisica(ev) {
    const e = tasca && tasca.estat();
    if ($("#mod-calc").hidden || !e || e.acabada) return;
    if (ev.ctrlKey || ev.metaKey || ev.altKey) return;
    const on = ev.target;
    if (on && (on.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(on.tagName))) return;

    if (ev.key === "ArrowRight") { ev.preventDefault(); avanca(); return; }
    if (ev.key === "ArrowLeft")  { ev.preventDefault(); tasca.enrere(); return; }
    // Retorn damunt d'un botó del pas fa el que fa el botó. En qualsevol altre
    // lloc és EXE: si no, qui acabava de triar el cas amb el ratolí tenia el
    // focus a la pastilla, i en prémer Retorn el cas tornava a començar.
    if (ev.key === "Enter" && on && on.tagName === "BUTTON" && on.closest(".pas-calc")) return;

    const k = TECLAT[ev.key];
    if (!k || k !== passos[e.pas].k) return;
    ev.preventDefault();
    const tecla = $("#mod-calc .tecla.ara");
    if (tecla) {                                   // un flaix: la tecla s'ha premut
      tecla.classList.add("premuda");
      setTimeout(() => tecla.classList.remove("premuda"), 180);
    }
    avanca();
  }

  function iniciaCalc() {
    if ($("#calc-pastilles").children.length) return;
    omplirTextos($("#mod-calc"));

    const munta = (cont, llista) => llista.forEach(t => {
      const b = document.createElement("div");
      b.className = "tecla" + (t.op ? " op" : "") + (t.ans ? " ans" : "") + (t.petita ? " petita" : "");
      b.dataset.k = t.k;
      b.textContent = t.et || t.k;
      cont.appendChild(b);
    });
    munta($("#calc-dalt"), TECLES_DALT);
    munta($("#calc-baix"), TECLES_BAIX);

    // Autocomprovació: cap cas no pot demanar una tecla que no surti al mapa.
    const alMapa = new Set(TECLES_DALT.concat(TECLES_BAIX).map(t => t.k));
    CASOS_CALC.forEach(c => passosDe(c).forEach(p => {
      if (!alMapa.has(p.k)) console.warn("CE calc: el cas «" + c.et + "» demana «" + p.k + "», que no és al mapa");
    }));

    tasca = CE.tasca({
      tasca: 0,
      recorregut: $("#calc-recorregut"),
      final: $("#calc-final"),
      cos: [$("#calc-cos")],
      comptador: "0.tecla",
      forats: e => ({ k: passos[e.pas].k }),
      desa: false,                        // un cas dura un minut: no cal reprendre'l
      nom: e => txt("0.titol") + " · " + CASOS_CALC[e.cas].et,
      pinta: i => pintaPas(i),
      resum: e => ({ frase: CASOS_CALC[e.cas].final,
                     files: [[txt("0.r_tecles"), e.total]],
                     codi: { a: e.total, b: 0, c: 0 } })
    });

    CE.pastilles($("#calc-pastilles"), CASOS_CALC, c => nouCas(c));
    $("#calc-arrere").onclick = () => tasca.enrere();
    $("#calc-endavant").onclick = avanca;
    // tocar la tecla que batega fa el mateix que el botó
    $("#mod-calc .mapa").addEventListener("click", ev => {
      if (ev.target.classList && ev.target.classList.contains("ara")) avanca();
    });
    document.addEventListener("keydown", teclaFisica);

    // la nota del teclat només té sentit on hi ha ratolí, és a dir, teclat
    const nota = $("#calc-nota-teclat");
    if (nota) nota.hidden = !(window.matchMedia && matchMedia("(pointer: fine)").matches);

    $("#calc-context").textContent = cas.context;
    tasca.inicia(() => ({ total: passos.length, cas: CASOS_CALC.indexOf(cas) }));
  }

  CE.registra("calc", iniciaCalc);
  CE.registraCataleg("0", { nom: "Calculadora", casos: CASOS_CALC.map(c => c.et),
                            recomptes: ["tecles"] });
})();
