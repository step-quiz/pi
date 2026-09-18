/* ============================================================================
   dades/textos.js · TOTES les frases que llegeix l'alumnat
   ----------------------------------------------------------------------------
   Aquest és l'únic lloc on s'han de canviar les paraules. Ni el marcatge ni el
   codi en tenen cap: les llegeixen d'aquí.

   COM S'EDITA
     · Canvia només el text entre cometes.
     · *Entre asteriscs* surt en negreta.
     · {això} és un forat que s'omple sol amb un número o una paraula.
       NO el canviïs de nom ni l'esborris: si falta, la frase perd la dada.
     · Si vols una cometa simple dins del text, escriu-la amb barra: \'

   Es pot editar a mà o amb textos.html, que és una pàgina per al professorat
   que ensenya cada frase en un camp, avisa si falta un forat i et dona el
   fitxer ja fet per substituir aquest.
   ========================================================================== */

window.TEXTOS = {

  /* ---------------- 1.1 · observar on cau un nombre ---------------- */
  "1.1": {
    nom:       "On cau el nombre?",
    titol:     "On cau el nombre?",
    ajuda:     "Tria un nombre i mira entre quins sencers cau.",
    marca:     "Exemple",
    situa:     "És entre *{baix}* i *{alt}*, i més a prop del *{prop}*.",
    titol2:    "Quants decimals necessites?",
    ajuda2:    "Depèn del que n'hagis de fer. Tria una situació.",
    et_sencer: "El nombre sencer",
    et_queda:  "Com queda",
    us_dic:    "Ho dic",
    us_compro: "Ho compro",
    us_tallo:  "Ho tallo",
    decimal:   "decimal",
    decimals:  "decimals",
    puja:      "L'última xifra puja, perquè la següent és 5 o més.",
    igual:     "L'última xifra es queda igual."
  },

  /* ---------------- 1.2 · col·locar-lo a la recta ---------------- */
  "1.2": {
    nom:      "Posa'l a la recta",
    titol:    "Posa'l a la recta",
    ajuda:    "Toca la recta on et sembla que cau aquest nombre.",
    comenca:  "Toca la recta.",
    aqui:     "aquí",
    encert:   "*Molt bé.* {nom} cau entre {baix} i {alt}.",
    fallada:  "Era una mica més a la *{banda}*. Mira on cau.",
    dreta:    "dreta",
    esquerra: "esquerra",
    altre:    "Un altre nombre"
  },

  /* ---------------- 1.3 · s'acaba o no s'acaba ---------------- */
  "1.3": {
    nom:       "S'acaba o no s'acaba?",
    titol:     "S'acaba o no s'acaba?",
    ajuda:     "Mira els decimals de la pantalla i decideix.",
    comenca:   "Mira els decimals i tria.",
    boto_si:   "S'acaba",
    boto_no:   "No s'acaba",
    encert_si: "*Sí.* {nom} és exactament *{valor}*: s'acaba.",
    error_si:  "*No.* {nom} és exactament *{valor}*: s'acaba.",
    encert_no: "*Sí.* {nom} no s'acaba mai, per molts decimals que hi posis.",
    error_no:  "*No.* {nom} no s'acaba mai, per molts decimals que hi posis.",
    altre:     "Un altre"
  },

  /* ---------------- 1.4 · el preu d'arrodonir ---------------- */
  "1.4": {
    nom:           "Quant costa arrodonir",
    titol:         "Quant costa arrodonir",
    ajuda:         "Compres corda. Mira què passa si demanes metres sencers.",
    et_necessites: "Necessites",
    mat_1:         "Corda",
    mat_2:         "Cinta",
    mat_3:         "Cable",
    mat_etiqueta:  "{nom} · {preu}/m",
    barra_just:    "El que necessites: {m} m",
    barra_amunt:   "Arrodonit amunt: {m} m",
    just:          "Demanes metres justos: no pagues res de més.",
    de_mes:        "Pagues *{dif}* de més."
  },

  /* ---------------- 1.5 · el valor de cada xifra ---------------- */
  "1.5": {
    nom:        "Cada xifra val una cosa",
    titol:      "Cada xifra val una cosa",
    ajuda:      "Toca una xifra i mira quant val.",
    comenca:    "Toca una xifra de la taula.",
    val:        "El *{xifra}* és a les *{lloc}*. Val *{quant}*.",
    et_suma:    "El nombre, trossejat",
    centenes:   "centenes",
    desenes:    "desenes",
    unitats:    "unitats",
    decimes:    "dècimes",
    centesimes: "centèsimes",
    millesimes: "mil·lèsimes"
  },

  /* ---------------- 1.6 · canviar d'unitat mou la coma ---------------- */
  "1.6": {
    nom:       "Canviar d'unitat mou la coma",
    titol:     "Canviar d'unitat mou la coma",
    ajuda:     "Tria una unitat de l'escala i mira on va la coma.",
    et_mesura: "La mateixa llargada, escrita d'una altra manera",
    surto:     "surto d'aquí",
    igual:     "*{a}* i *{b}* són la mateixa llargada.",
    mateixa:   "Aquesta és la unitat de partida: la coma no es mou.",
    dreta:     "Has baixat *{graons}* graons: la coma es mou *{graons}* llocs a la *dreta*.",
    esquerra:  "Has pujat *{graons}* graons: la coma es mou *{graons}* llocs a l'*esquerra*."
  }
};

/* ============================================================================
   D'AQUÍ CAP AVALL NO CAL TOCAR RES.
   Són les explicacions que fa servir textos.html per dir on surt cada frase i
   quins forats {} necessita. Si algun dia s'afegeix una frase nova, afegeix-hi
   també la seva línia: el test de eines/comprova.py avisa si en falta alguna.
   ========================================================================== */

window.TEXTOS_GUIA = {
  "1.1": {
    nom:       ["Nom a la barra de fletxes", []],
    titol:     ["Títol de la primera targeta", []],
    ajuda:     ["Línia sota el títol", []],
    marca:     ["Etiqueta del cas que ve resolt", []],
    situa:     ["Resposta sota la recta", ["baix", "alt", "prop"]],
    titol2:    ["Títol de la segona targeta", []],
    ajuda2:    ["Línia sota el segon títol", []],
    et_sencer: ["Rètol de la tira de xifres", []],
    et_queda:  ["Rètol del resultat arrodonit", []],
    us_dic:    ["Targeta de precisió: parlar", []],
    us_compro: ["Targeta de precisió: comprar", []],
    us_tallo:  ["Targeta de precisió: tallar", []],
    decimal:   ["Paraula en singular, a les targetes", []],
    decimals:  ["Paraula en plural, a les targetes", []],
    puja:      ["Avís quan l'arrodoniment fa pujar l'última xifra", []],
    igual:     ["Avís quan l'última xifra no canvia", []]
  },
  "1.2": {
    nom:      ["Nom a la barra de fletxes", []],
    titol:    ["Títol de la targeta", []],
    ajuda:    ["Línia sota el títol", []],
    comenca:  ["Avís abans de tocar la recta", []],
    aqui:     ["Etiqueta del punt tocat, damunt la recta", []],
    encert:   ["Quan encerta", ["nom", "baix", "alt"]],
    fallada:  ["Quan falla", ["banda"]],
    dreta:    ["Paraula que omple {banda}", []],
    esquerra: ["Paraula que omple {banda}", []],
    altre:    ["Botó per canviar de nombre", []]
  },
  "1.3": {
    nom:       ["Nom a la barra de fletxes", []],
    titol:     ["Títol de la targeta", []],
    ajuda:     ["Línia sota el títol", []],
    comenca:   ["Avís abans de contestar", []],
    boto_si:   ["Botó de l'esquerra", []],
    boto_no:   ["Botó de la dreta", []],
    encert_si: ["Encerta i el nombre s'acaba", ["nom", "valor"]],
    error_si:  ["Falla i el nombre s'acaba", ["nom", "valor"]],
    encert_no: ["Encerta i el nombre no s'acaba", ["nom"]],
    error_no:  ["Falla i el nombre no s'acaba", ["nom"]],
    altre:     ["Botó per canviar d'arrel", []]
  },
  "1.4": {
    nom:           ["Nom a la barra de fletxes", []],
    titol:         ["Títol de la targeta", []],
    ajuda:         ["Línia sota el títol", []],
    et_necessites: ["Rètol sobre els metres", []],
    mat_1:         ["Nom del primer material", []],
    mat_2:         ["Nom del segon material", []],
    mat_3:         ["Nom del tercer material", []],
    mat_etiqueta:  ["Com es munta l'etiqueta. El preu surt del codi, no d'aquí", ["nom", "preu"]],
    barra_just:    ["Etiqueta de la primera barra", ["m"]],
    barra_amunt:   ["Etiqueta de la segona barra", ["m"]],
    just:          ["Quan els metres ja són sencers", []],
    de_mes:        ["Quant es paga de més", ["dif"]]
  },
  "1.5": {
    nom:        ["Nom a la barra de fletxes", []],
    titol:      ["Títol de la targeta", []],
    ajuda:      ["Línia sota el títol", []],
    comenca:    ["Avís abans de tocar cap xifra", []],
    val:        ["Què val la xifra que ha tocat", ["xifra", "lloc", "quant"]],
    et_suma:    ["Rètol sobre la descomposició", []],
    centenes:   ["Nom de la columna", []],
    desenes:    ["Nom de la columna", []],
    unitats:    ["Nom de la columna", []],
    decimes:    ["Nom de la columna", []],
    centesimes: ["Nom de la columna", []],
    millesimes: ["Nom de la columna", []]
  },
  "1.6": {
    nom:       ["Nom a la barra de fletxes", []],
    titol:     ["Títol de la targeta", []],
    ajuda:     ["Línia sota el títol", []],
    et_mesura: ["Rètol sobre la mesura gran", []],
    surto:     ["Nota damunt la unitat de partida", []],
    igual:     ["Les dues escriptures són la mateixa llargada", ["a", "b"]],
    mateixa:   ["Quan la unitat triada ja és la de partida", []],
    dreta:     ["Baixant graons per l'escala", ["graons"]],
    esquerra:  ["Pujant graons per l'escala", ["graons"]]
  }
};
