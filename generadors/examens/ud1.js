#!/usr/bin/env node
/*
  generadors/examens/ud1.js · examen de la Unitat 1 (Nombres reals)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a nucli.js i les regles, a
  docs/EXAMENS-DOCX.md. És el model de referència per a les altres unitats.

      node generadors/examens/ud1.js        →  docx/examen-ud1-alumnat.docx
                                                docx/examen-ud1-solucionari.docx

  D'on surt cada cosa:
  · El format i les frases, de la revisió que el docent va fer de l'examen a
    Google Docs el 23/9/2026.
  · Els apartats a), b), c) i d), dels exercicis de fitxes/ud1.html i del seu
    solucionari, que estan validats. On la fitxa no en tenia prou, n'hi ha un de
    nou, i al solucionari porta la marca «nou» perquè el docent el revisi.
*/
"use strict";

const X = require("./nucli");
const { dada, ms, sol, MIDA } = X;

const alumnat = [
  ...X.exercici(1, "Escriu entre quins dos nombres enters cau cada nombre.", { calc: true }, [
    X.taulaResposta([16, 16, 32, 18, 18], ["", "Número", "Surt", "Entre", "i"], [
      ["a)", dada("√7", MIDA.arrel), ms("2,6457513…"), ms("2"), ms("3")],
      ["b)", dada("√5", MIDA.arrel), "", "", ""],
      ["c)", dada("√11", MIDA.arrel), "", "", ""],
      ["d)", dada("π", MIDA.arrel), "", "", ""],
    ]),
  ]),

  ...X.exercici(2, "Marca amb una creu on cau cada nombre a la recta.", {}, [
    ...X.recta("a)", ms("√7 = 2,6457513…"), { marca: Math.sqrt(7), etiquetaMarca: "√7", primer: true }),
    ...X.recta("b)", "√5 = 2,2360679…"),
    ...X.recta("c)", "√30 = 5,4772255…"),
    ...X.recta("d)", "√11 = 3,3166247…"),                       // nou
  ]),

  ...X.exercici(3, "Arrodoneix cada nombre amb els decimals que et demanen.", { calc: true }, [
    X.taulaResposta([12, 34, 18, 18, 18], ["", "Número", "0 decimals", "1 decimal", "2 decimals"], [
      ["a)", ms("2,6457513…"), ms("3"), ms("2,6"), ms("2,65")],
      ["b)", dada("1,6970562…"), "", "", ""],
      ["c)", dada("4,2857142…"), "", "", ""],
      ["d)", dada("3,1415926…"), "", "", ""],
    ]),
  ]),

  ...X.exercici(4, "Marca el nombre que té xifres decimals que s'acaben.", { calc: true }, [
    X.encercla("a)", ["√2", "√9", "π", "√5"], { triat: "√9", nota: "√9 = 3" }),
    () => X.espai(X.AIRE.entreApartats, { keepNext: true }),
    X.encercla("b)", ["√3", "√16", "√20", "√7"]),
    () => X.espai(X.AIRE.entreApartats, { keepNext: true }),
    X.encercla("c)", ["√8", "√10", "√25", "π"]),
    () => X.espai(X.AIRE.entreApartats, { keepNext: true }),
    X.encercla("d)", ["√12", "√36", "√2", "√18"], { seguir: false }),
  ]),

  ...X.exercici(5, "Marca quants decimals faries servir en cada cas.", {}, [
    ...X.situacioAmbTria("a)", "talla", "Has de tallar el parquet d'una habitació.", "4,28571… m",
      ["4 m", "4,3 m", "4,29 m"], { marcada: "4,29 m", primer: true }),
    ...X.situacioAmbTria("b)", "parla", "Li dius a un amic quant mesura la diagonal de la tele.", "1,0735455… m",
      ["1 m", "1,1 m", "1,07 m"]),
    ...X.situacioAmbTria("c)", "compra", "Compres tela per tapar una taula. Es ven per centímetres.", "1,6970562… m",
      ["1,7 m", "1,70 m", "1,697 m"]),
    ...X.situacioAmbTria("d)", "compra", "Compres una catifa. A la botiga, les catifes fan 2 m, 3 m o 4 m.", "3,4285714… m",
      ["3 m", "3,4 m", "3,43 m"], { ultim: true }),               // nou
  ]),

  ...X.exercici(6, "Calcula quants diners de més pagues si arrodoneixes cap amunt.", { calc: true }, [
    X.context("A la ferreteria, la corda val 2,35 € el metre."),
    X.taulaResposta([10, 20, 22, 16, 16, 16], ["", "Necessites", "Costa", "Compres", "Pagues", "De més"], [
      ["a)", ms("3,7 m"), ms("8,70 €"), ms("4 m"), ms("9,40 €"), ms("0,70 €")],
      ["b)", dada("5,2 m"), "", dada("6 m"), "", ""],
      ["c)", dada("2,4 m"), "", dada("3 m"), "", ""],
      ["d)", dada("6,6 m"), "", dada("7 m"), "", ""],              // nou
    ]),
  ]),

  /* El 6 i el 7 van a la mateixa pàgina, com els va deixar el docent. */
  ...X.exercici(7, "Decideix si has d'arrodonir cap amunt o cap avall.", { calc: true, mateixaPagina: true }, [
    X.context("En tots els casos només pots comprar quantitats enteres, sense decimals."),
    X.taulaResposta([8, 42, 18, 16, 16], ["", "Situació", "Surt", "Amunt o avall?", "Resposta"], [
      ["a)", ms("Necessites 2,3 L de pintura. Els pots són d'1 L.", undefined, { esq: true }),
             ms("2,3 pots"), ms("amunt"), ms("3 pots")],
      ["b)", dada("Tens 11 €. Una entrada de cine val 3 €.", undefined, { esq: true }), "", "", ""],
      ["c)", dada("Sou 22 persones. A cada cotxe hi caben 5.", undefined, { esq: true }), "", "", ""],
      ["d)", dada("Tens 15 €. Un got de suc val 4 €.", undefined, { esq: true }), "", "", ""],   // nou
    ]),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const TRAS_TITOL = { spacing: { before: X.tw(5), after: X.tw(8) } };

const solucionari = privat => [
  ...sol.titol(1),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Fita d'assoliment esperada: *AS* (Assolit Satisfactòriament). Calculadora disponible a tot l'examen.`,
    "*Com s'ha construït:* a cada exercici, l'apartat a) resolt com a model i tres apartats per fer, amb els ítems de la fitxa (_fitxes/ud1.html_) i del seu solucionari. Cap pregunta de justificació oberta. Els apartats marcats «nou» no són a la fitxa: revisa'ls abans de fer servir l'examen.",
    "*Dues valoracions separades:* puntua per separat si la *decisió* és correcta i si el *càlcul* és correcte. Un error aritmètic no hauria de fer baixar la valoració de la decisió.",
  ]),

  sol.h3("1. Entre quins dos nombres enters cau — criteri 5.1"),
  ...sol.taula([19, 20, 31, 17, 13], [
    ["", "Número", "Surt", "Entre", "i"],
    ["a) resolt", "√7", "2,6457513…", "2", "3"],
    ["b)", "√5", "2,2360679…", "2", "3"],
    ["c)", "√11", "3,3166247…", "3", "4"],
    ["d)", "π", "3,1415926…", "3", "4"],
  ]),
  sol.p("*Error típic:* dir que √11 cau entre 10 i 12, confonent el nombre de dins de l'arrel amb el resultat. Si passa, torneu a la pàgina 2 de la fitxa i repetiu-la amb √5."),

  sol.h3("2. Marcar a la recta — criteri 5.1"),
  sol.p("b) √5 = 2,236 → entre el 2 i el 3, just a l'esquerra del 2 i quart. Es dona per bo qualsevol punt entre 2,1 i 2,4.", TRAS_TITOL),
  sol.p("c) √30 = 5,477 → entre el 5 i el 6, cap a la meitat. Es dona per bo entre 5,3 i 5,7."),
  sol.p("d) nou · √11 = 3,317 → entre el 3 i el 4, a prop del 3 i un terç. Es dona per bo entre 3,2 i 3,5."),
  sol.p("Els apartats b i d són nombres de l'exercici 1, ara com un punt a la recta. Si aquí fallen i a l'1 no, el que costa és passar del nombre al dibuix, no el càlcul."),

  sol.h3("3. Arrodonir — criteri 5.1"),
  ...sol.taula([16, 24, 20, 20, 20], [
    ["", "Número", "0 decimals", "1 decimal", "2 decimals"],
    ["a) resolt", "2,6457513…", "3", "2,6", "2,65"],
    ["b)", "1,6970562…", "2", "1,7", "1,70"],
    ["c)", "4,2857142…", "4", "4,3", "4,29"],
    ["d)", "3,1415926…", "3", "3,1", "3,14"],
  ]),
  sol.p("*Error típic:* tallar en comptes d'arrodonir (escriure 1,69 a l'apartat b, o 4,28 al c)."),
  sol.p("*Atenció* a l'apartat b: a 2 decimals és *1,70*, no *1,7*. El zero final hi ha de ser perquè indica la precisió amb què s'ha mesurat."),

  sol.h3("4. El nombre amb decimals que s'acaben — criteri 5.1"),
  sol.p("a) resolt: *√9 = 3* \u00A0·\u00A0 b) *√16 = 4* \u00A0·\u00A0 c) *√25 = 5* \u00A0·\u00A0 d) *√36 = 6*", TRAS_TITOL),
  sol.p("Tots quatre són arrels de quadrats perfectes. Si en falla més d'un, val la pena repassar la llista de quadrats perfectes (1, 4, 9, 16, 25, 36…) abans de continuar."),

  sol.h3("5. Quants decimals — criteri 1.1"),
  ...sol.taula([19, 51, 30], [
    ["", "Situació", "Resposta"],
    ["a) resolt", "Tallar el parquet", "*4,29 m* (2 decimals)"],
    ["b)", "Dir-ho a un amic", "*1,1 m* (1 decimal)"],
    ["c)", "Tela, es ven per centímetres", "*1,70 m* (2 decimals)"],
    ["d) nou", "Catifa, només de 2 m, 3 m o 4 m", "*3 m* (cap decimal)"],
  ]),
  sol.p("Es valora *la tria*, no la xifra exacta. A l'apartat b, «1 m» també es dona per bo si ho justifica de paraula. Entre tots quatre hi ha les tres precisions: dos decimals (a i c), un (b) i cap (d)."),

  sol.h3("6. La corda, a 2,35 € el metre — criteri 8.3"),
  ...sol.taula([16, 20, 15, 18, 15, 16], [
    ["", "Necessites", "Costa", "Compres", "Pagues", "De més"],
    ["a) resolt", "3,7 m", "8,70 €", "4 m", "9,40 €", "0,70 €"],
    ["b)", "5,2 m", "12,22 €", "6 m", "14,10 €", "1,88 €"],
    ["c)", "2,4 m", "5,64 €", "3 m", "7,05 €", "1,41 €"],
    ["d) nou", "6,6 m", "15,51 €", "7 m", "16,45 €", "0,94 €"],
  ]),
  sol.p("A l'apartat a, 3,7 × 2,35 = 8,695, que arrodonit són 8,70 €. Si ho refà amb la calculadora sense arrodonir, li sortirà 0,705 €: totes dues respostes són bones."),

  sol.h3("7. Amunt o avall — criteri 6.1"),
  ...sol.taula([14, 30, 22, 17, 17], [
    ["", "Situació", "Surt", "Amunt o avall", "Resposta"],
    ["a) resolt", "Pintura, pots d'1 L", "2,3 pots", "amunt", "3 pots"],
    ["b)", "11 €, entrades de 3 €", "11 ÷ 3 = 3,666…", "*avall*", "3 entrades"],
    ["c)", "22 persones, cotxes de 5", "22 ÷ 5 = 4,4", "*amunt*", "5 cotxes"],
    ["d) nou", "15 €, gots de suc de 4 €", "15 ÷ 4 = 3,75", "*avall*", "3 gots"],
  ]),
  sol.p("*Error típic:* arrodonir sempre cap amunt, perquè és el que s'ha fet a l'exercici 6, o arrodonir al més a prop i contestar 4 entrades a l'apartat b (3,666… és més a prop de 4) o 4 gots al d. Les dues coses són el mateix error: aplicar una regla sense mirar la situació."),
  sol.p("*Això és el que mostra si ho ha entès:* als apartats b i c el compte és igual i la decisió és la contrària. Si c surt bé i b no, encara depèn de la regla «sempre amunt». Val la pena fer-ho de paraula: «quantes entrades pots pagar de veritat?»."),

  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Exercicis 1, 2, 3 i 4 → criteri *5.1*, passar d'una representació a una altra.",
    "Exercici 5 → criteri *1.1*, decidir en una situació real.",
    "Exercici 6 → criteri *8.3*, veure les conseqüències del propi arrodoniment.",
    "Exercici 7 → criteri *6.1*, decidir l'arrodoniment en situacions noves; és el criteri on l'alumnat pot lluir més (vegeu docs/MAPA-ADAPTACIO.md, apartat 8).",
  ]),
  sol.p("L'objectiu de l'examen *no és calcular bé*: és situar un nombre i decidir la precisió. Els errors de càlcul no haurien de fer baixar la valoració de la decisió."),
];

X.genera({ unitat: 1, alumnat, solucionari }).catch(e => { console.error(e.message); process.exit(1); });
