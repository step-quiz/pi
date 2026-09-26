#!/usr/bin/env node
/*
  1eso/generadors/examens/ud3.js · examen de la Unitat 3 (les fraccions del grup)
  ---------------------------------------------------------------------------
  Només hi ha el contingut: la maquinària és a comu/examens/nucli.js i les
  regles, a comu/docs/EXAMENS-DOCX.md. Dins d'una cel·la, «{3/4}» s'escriu com a
  fracció, amb el numerador damunt del denominador, com a les fitxes.

      node 1eso/generadors/examens/ud3.js   →  1eso/docx/examen-ud3-alumnat.docx
                                                1eso/docx/examen-ud3-solucionari.docx

  D'on surt cada cosa:
  · El que avalua, de l'examen de fraccions del grup (13/3/2026): el nom, el tipus,
    comparar, les equivalents i les sumes. El valor numèric, la multiplicació en
    creu, les irreductibles de nombres grans i les sumes amb denominadors
    diferents queden fora, com a docs/MAPA-ADAPTACIO.md. La segona adaptació de
    l'examen que ja existeix és la referència de mida.
  · Els apartats a), b), c) i d), de les cinc fitxes de la unitat (fitxes/ud3*.html)
    i dels seus solucionaris. Cap apartat és nou.
  · Sempre amb el mateix denominador (decisió del docent del 26/9/2026), i les
    dues targetes al davant: la de les taules i la dels noms de les fraccions.
*/
"use strict";

const X = require("../../../comu/examens/nucli");
const { dada, ms, sol } = X;

/* ------------------------------------------------------------ l'alumnat -- */
const alumnat = [
  ...X.exercici(1, "Escriu com es llegeix cada fracció. Mira la targeta de les fraccions.", {}, [
    X.taulaResposta([10, 25, 65], ["", "Fracció", "Es llegeix"], [
      ["a)", dada("{3/4}"), ms("tres quarts")],
      ["b)", dada("{2/5}"), ""],
      ["c)", dada("{5/8}"), ""],
      ["d)", dada("{1/2}"), ""],
    ]),
  ]),

  /* Amb les fraccions, les files són més altes: l'1 va sol amb la capçalera, i després, de dos en dos. */
  ...X.exercici(2, "Ara al revés: escriu la fracció.", {}, [
    X.taulaResposta([10, 60, 30], ["", "Es llegeix", "Fracció"], [
      ["a)", dada("quatre novens"), ms("{4/9}")],
      ["b)", dada("un terç"), ""],
      ["c)", dada("set desens"), ""],
      ["d)", dada("cinc sisens"), ""],
    ]),
  ]),

  ...X.exercici(3, "Escriu el tipus de cada fracció: nul·la, pròpia, unitat o impròpia.", { mateixaPagina: true }, [
    X.context("Mira el de dalt i el de baix."),
    X.taulaResposta([10, 30, 60], ["", "Fracció", "El tipus"], [
      ["a)", dada("{3/4}"), ms("pròpia")],
      ["b)", dada("{7/7}"), ""],
      ["c)", dada("{9/5}"), ""],
      ["d)", dada("{0/6}"), ""],
    ]),
  ]),

  ...X.exercici(4, "Escriu la fracció més gran de cada parella.", {}, [
    X.context("Si ho necessites, fes el dibuix al marge, amb dos rectangles iguals."),
    X.taulaResposta([10, 50, 40], ["", "Les dues fraccions", "La més gran"], [
      ["a)", dada("{3/5} i {2/5}"), ms("{3/5}")],
      ["b)", dada("{1/8} i {5/8}"), ""],
      ["c)", dada("{1/3} i {1/5}"), ""],
      ["d)", dada("{2/7} i {2/5}"), ""],
    ]),
  ]),

  ...X.exercici(5, "Amplifica: multiplica el de dalt i el de baix pel mateix nombre.", { mateixaPagina: true }, [
    X.taulaResposta([10, 25, 25, 40], ["", "Fracció", "Multiplica", "La nova"], [
      ["a)", dada("{2/3}"), dada("per 4"), ms("{8/12}")],
      ["b)", dada("{1/2}"), dada("per 3"), ""],
      ["c)", dada("{3/5}"), dada("per 2"), ""],
      ["d)", dada("{1/4}"), dada("per 3"), ""],
    ]),
  ]),

  ...X.exercici(6, "Són equivalents? Escriu Sí o No.", {}, [
    X.context("Prova de multiplicar la primera, dalt i baix, pel mateix nombre. Si surt l'altra, són equivalents."),
    X.taulaResposta([10, 55, 35], ["", "Les dues fraccions", "Són equivalents?"], [
      ["a)", dada("{1/2} i {2/4}"), ms("Sí")],
      ["b)", dada("{2/3} i {4/6}"), ""],
      ["c)", dada("{1/2} i {2/3}"), ""],
      ["d)", dada("{1/3} i {2/6}"), ""],
    ]),
  ]),

  ...X.exercici(7, "Suma o resta. El de baix no canvia.", { mateixaPagina: true }, [
    X.taulaResposta([10, 55, 35], ["", "Operació", "Resultat"], [
      ["a)", dada("{3/8} + {2/8}"), ms("{5/8}")],
      ["b)", dada("{1/4} + {2/4}"), ""],
      ["c)", dada("{7/8} − {3/8}"), ""],
      ["d)", dada("{3/7} + {5/7}"), ""],
    ]),
  ]),

  ...X.exercici(8, "Està ben feta la suma? Escriu Bé o Malament.", {}, [
    X.context("Si sumes, no pots tenir menys del que tenies."),
    X.taulaResposta([10, 60, 30], ["", "La suma", "Bé o malament?"], [
      ["a)", dada("{1/4} + {2/4} = {3/8}"), ms("Malament")],
      ["b)", dada("{2/5} + {1/5} = {3/5}"), ""],
      ["c)", dada("{1/2} + {1/4} = {2/6}"), ""],
      ["d)", dada("{3/10} + {4/10} = {7/10}"), ""],
    ]),
  ]),
];

/* ---------------------------------------------------------- solucionari -- */
const TRAS = { spacing: { before: X.tw(5), after: X.tw(8) } };

const solucionari = privat => [
  ...sol.titol(3),
  ...sol.caixa([
    `*Adaptació:* ${privat.adaptacio}. Sense calculadora: la *targeta de les taules* i la *targeta dels noms de les fraccions* són al davant tota l'estona.`,
    "*Com s'ha construït:* avalua el mateix que l'examen de fraccions del grup (el nom, el tipus, comparar, les equivalents i les sumes), sense el valor numèric, la multiplicació en creu, les irreductibles de nombres grans ni les sumes amb denominadors diferents. A cada exercici, l'apartat a) resolt com a model i tres per fer, amb els ítems de les cinc fitxes de la unitat. Cap apartat és nou.",
    "*Si cal, en dues sessions:* els exercicis 1 a 4 (el nom, el tipus i comparar) i els 5 a 8 (les equivalents i les sumes).",
    "*Es pot dibuixar:* un rectangle al marge, per comparar o per sumar, és una estratègia bona, no un error.",
  ]),

  sol.h3("1 i 2. El nom"),
  sol.p("1b) *dos cinquens*; 1c) *cinc vuitens*; 1d) *un mig*. 2b) *1/3*; 2c) *7/10*; 2d) *5/6*. Sempre amb la targeta.", TRAS),

  sol.h3("3. El tipus"),
  sol.p("b) 7/7, *unitat*; c) 9/5, *impròpia*; d) 0/6, *nul·la*.", TRAS),

  sol.h3("4. La més gran"),
  sol.p("b) *5/8*; c) *1/3*; d) *2/5*. *Error típic:* triar 1/5 a l'apartat c, perquè 5 és més gran que 3. És la regla trencada de la fitxa 2: amb més trossos, cada tros és més petit.", TRAS),

  sol.h3("5. Amplificar"),
  sol.p("b) 1 · 3 = 3 i 2 · 3 = 6: *3/6*. c) 3 · 2 = 6 i 5 · 2 = 10: *6/10*. d) 1 · 3 = 3 i 4 · 3 = 12: *3/12*.", TRAS),

  sol.h3("6. Equivalents"),
  sol.p("b) *Sí* (2/3 per 2 és 4/6); c) *No*; d) *Sí* (1/3 per 2 és 2/6). *Error típic:* dir que sí a la c, perquè s'hi ha sumat 1 dalt i baix. És la regla trencada de la fitxa 3.", TRAS),

  sol.h3("7. Suma i resta"),
  sol.p("b) *3/4*; c) *4/8*; d) *8/7*, que és més d'un rectangle. *Error típic:* sumar també els de baix (3/8 a l'apartat b).", TRAS),

  sol.h3("8. Està ben feta?"),
  sol.p("b) *Bé*; c) *Malament*: és 3/4, i 2/6 és menys de la meitat; d) *Bé*. És el full de la pàgina 5 de la fitxa 4: si a la meitat hi sumes un tros, en tens més de la meitat. *Compta per als nivells alts, no per al mínim.*", TRAS),

  sol.h3("Què mirar per avaluar"),
  ...sol.vinyetes([
    "Exercicis 1 i 2 → el nom d'una fracció, en tots dos sentits, amb la targeta.",
    "Exercici 3 → el tipus: nul·la, pròpia, unitat o impròpia.",
    "Exercici 4 → compara dues fraccions, amb el mateix de baix i amb el mateix de dalt.",
    "Exercicis 5 i 6 → amplifica, i diu si dues fraccions són equivalents.",
    "Exercici 7 → suma i resta amb el mateix denominador.",
    "Exercici 8 → *nivells alts*: reconeix una suma mal feta.",
  ]),
  sol.p("Els criteris de la SA del grup (1.2, 5.2, 6.1 i 9.1) són de referència: l'avaluació es fa amb els criteris del PI. Una explicació oral registrada en el moment, o el codi d'una tasca tancada de la caixa d'eines, valen igual que l'examen escrit."),
];

X.genera({
  unitat: 3, alumnat, solucionari,
  materia: "Matemàtiques",
  creador: "Matemàtiques",
  avis: { text: "Pots fer servir les dues targetes a tot l'examen: la de les taules i la de les fraccions.", icona: "targeta" },
}).catch(e => { console.error(e.message); process.exit(1); });
