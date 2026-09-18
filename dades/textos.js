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

  "1.1": {
    nom:       'On està situat el nombre?',
    titol:     'On està situat el nombre?',
    ajuda:     'Escull un nombre. Observa entre quins nombres enters està situat.',
    marca:     '',
    situa:     'El nombre està entre *{baix}* i *{alt}*, més a prop del *{prop}*.',
    titol2:    'Si volem aproximar el nombre 2,6457513, quants decimals fem servir?',
    ajuda2:    'Depèn de la situació situació, fem servir més decimals o menys decimals. Exemples:',
    et_sencer: 'El nombre',
    et_queda:  'Hem aproximat el nombre',
    us_dic:    'Dic el nombre a una altra persona',
    us_compro: 'Faig una compra i necessito dir els € però també els cèntims',
    us_tallo:  'Vull tallar una fusta i necessito 3 decimals',
    decimal:   'decimal',
    decimals:  'decimals',
    puja:      'L\'última xifra puja, perquè la següent xifra és 5 o més.',
    igual:     'L\'última xifra es queda igual.'
  },

  "1.2": {
    nom:      'Situa un nombre a la recta real',
    titol:    'Situa un nombre a la recta real',
    ajuda:    'Has de tocar el lloc de la recta horitzontal on tu creus que hi haurà aquest nombre.',
    comenca:  'On creus que hi haurà el nombre?',
    aqui:     'aquí',
    encert:   '*Molt bé.* {nom} està situat entre els nombres {baix} i {alt}.',
    fallada:  'Era una mica més cap a la *{banda}*. Mira bé la recta i el nombre.',
    dreta:    'dreta',
    esquerra: 'esquerra',
    altre:    'Un altre nombre'
  },

  "1.3": {
    nom:       'Té infinits decimals, o no?',
    titol:     'Té infinits decimals, o no?',
    ajuda:     'Mira els decimals de la pantalla i decideix la teva resposta.',
    comenca:   'Escull una resposta',
    boto_si:   'El nombre de decimals s\'acaba',
    boto_no:   'El nombre de decimals no s\'acaba mai',
    encert_si: '*Sí.* {nom} és exactament *{valor}*: el nombre de decimals s\'acaba.',
    error_si:  '*No.* {nom} és exactament *{valor}*: el nombre de decimals s\'acaba.',
    encert_no: '*Sí.* {nom} no s\'acaba mai, per molts decimals que hi posis.',
    error_no:  '*No.* {nom} no s\'acaba mai, per molts decimals que hi posis.',
    altre:     'Un altre exemple? Clica aquí'
  },

  "1.4": {
    nom:           'Arrodonim i calculem preus',
    titol:         'Arrodonim i calculem preus',
    ajuda:         'Necessites comprar corda, però a la botiga només venen per metres sencers: 1m, o 2m, o 3m, ...',
    et_necessites: 'Necessites',
    mat_1:         'Corda',
    mat_2:         'Cinta',
    mat_3:         'Cable',
    mat_etiqueta:  '{nom} · {preu}/m',
    barra_just:    'Necessites exactament això: {m} m',
    barra_amunt:   'Però has de comprar això (arrodonit cap amunt): {m} m',
    just:          'Demanes metres justos: no pagues res de més.',
    de_mes:        'Pagues *{dif}* de més, perquè has hagut d\'arrodonir.'
  },

  "1.5": {
    nom:        'Cada xifra significa una cosa diferents',
    titol:      'Cada xifra significa una cosa diferents',
    ajuda:      'Selecciona una xifra i mira quin és el seu valor.',
    comenca:    'Selecciona una xifra de la taula.',
    val:        'El *{xifra}* és a les *{lloc}*. Val *{quant}*.',
    et_suma:    'Aquí tenim el nombre explicat d\'una altra manera',
    centenes:   'centenes',
    desenes:    'desenes',
    unitats:    'unitats',
    decimes:    'dècimes',
    centesimes: 'centèsimes',
    millesimes: 'mil·lèsimes'
  },

  "1.6": {
    nom:       'Canvis d\'unitats',
    titol:     'Canvis d\'unitats',
    ajuda:     'Tria una unitat i observa què passa amb la coma decimal.',
    et_mesura: 'És la mateixa longitud, però amb una unitat diferent',
    surto:     'surto d\'aquí',
    igual:     '*{a}* i *{b}* són exactament la mateixa longitud.',
    valor:     'La longitud val *{a}*.',
    mateixa:   'Aquesta és la unitat de partida: la coma no es mou.',
    dreta:     'La coma es mou *{graons}* llocs a la *dreta*.',
    esquerra:  'La coma es mou *{graons}* llocs a l\'*esquerra*.',
    dreta1:    'La coma es mou *1* lloc a la *dreta*.',
    esquerra1: 'La coma es mou *1* lloc a l\'*esquerra*.'
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
    valor:     ["Quan encara no s'ha canviat d'unitat", ["a"]],
    mateixa:   ["Quan la unitat triada ja és la de partida", []],
    dreta:     ["Baixant dos graons o més", ["graons"]],
    esquerra:  ["Pujant dos graons o més", ["graons"]],
    dreta1:    ["Baixant un sol graó, en singular", []],
    esquerra1: ["Pujant un sol graó, en singular", []]
  }
};
