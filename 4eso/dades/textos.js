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

   COM S'ESCRIU (Lectura Fàcil, norma UNE 153101:2018 EX)
     · Una idea per frase. Frases curtes: el test avisa a partir de 15 paraules
       i falla a partir de 20.
     · Imperatiu i paraules de cada dia: «Tria», «Toca», «Mira».
     · Literal: res de frases fetes ni de metàfores. «Fes-hi un cop d'ull» no;
       «Mira la taula» sí.
     · La mateixa paraula per a la mateixa cosa, aquí i a les fitxes:
       «nombres sencers», no «enters» en un lloc i «sencers» en un altre.
     · Sense majúscules seguides, xifres romanes ni hores en format 24 h.
     · Una resposta equivocada es diu «Incorrecte» i va seguida d'una pista que
       proposa un camí diferent, no de la mateixa consigna repetida.

   Es pot editar a mà o amb textos.html, que és una pàgina per al professorat
   que ensenya cada frase en un camp, avisa si falta un forat i et dona el
   fitxer ja fet per substituir aquest.
   ========================================================================== */

window.TEXTOS = {

  "comu": {
    correcte:     '*Correcte.*',
    incorrecte:   '*Incorrecte.*',
    altra_manera: 'Ara provem-ho d\'una altra manera.',
    pista:        '*Pista:*',
    inici:        'Inici',
    final:        'Final',
    pas:          'Pas {n} de {total}',
    rotul_final:  'Tasca acabada',
    seguent:      'Següent pas',
    acaba:        'Acaba la tasca',
    exemple:      'Exemple',
    represa:      'Aquesta tasca no està acabada. Es va aturar al *pas {n} de {total}*.',
    represa_dia:  'Es va desar el {dia}.',
    continua:     'Continua al pas {n}',
    de_nou:       'Comença de nou',
    represa_nota: 'Si no l\'has començat tu, tria «Comença de nou».',
    has_acabat:   'Has acabat.',
    r_tasca:      'Tasca',
    r_dia:        'Dia',
    r_passos:     'Passos',
    r_primer:     'Correctes al primer intent',
    r_pista:      'Correctes amb una pista',
    r_mostrat:    'Amb la resposta ensenyada',
    nom_paper:    'Nom:',
    codi:         'Codi de verificació',
    ensenya_codi: 'Ensenya aquest codi al professorat.',
    imprimeix:    'Imprimeix el resum',
    torna:        'Torna a començar'
  },

  "0": {
    titol:     'Com es fa amb la calculadora',
    com_va:    'Prem la tecla a la teva calculadora. Després toca *Següent tecla*.',
    tecla:     'Tecla {n} de {total}: prem *{k}*',
    seguent:   'Següent tecla',
    enrere:    'Enrere',
    acaba:     'Acaba',
    nota_punt: 'A la calculadora, la coma dels decimals s\'escriu amb un punt.',
    teclat_pc: 'Amb l\'ordinador també pots prémer la mateixa tecla al teclat.',
    dalt:      'A dalt, amb les funcions',
    baix:      'A baix, amb els números',
    r_tecles:  'Tecles'
  },

  "1.1": {
    nom:       'On és el nombre a la recta?',
    titol:     'On és el nombre a la recta?',
    ajuda:     'Tria un nombre. Mira entre quins dos nombres sencers és.',
    marca:     '',
    situa:     'El nombre és entre *{baix}* i *{alt}*. És més a prop del *{prop}*.',
    titol2:    'Quants decimals fem servir?',
    ajuda2:    'Depèn de la situació. Tria una situació.',
    et_sencer: 'El nombre amb totes les xifres',
    et_queda:  'El nombre arrodonit',
    us_dic:    'Dic el nombre a una altra persona',
    us_compro: 'Pago una compra amb euros i cèntims',
    us_tallo:  'Tallo una fusta i mesuro els mil·límetres',
    decimal:   'decimal',
    decimals:  'decimals',
    puja:      'L\'última xifra puja 1, perquè la xifra següent és 5 o més.',
    igual:     'L\'última xifra no canvia, perquè la xifra següent és 4 o menys.'
  },

  "1.2": {
    nom:      'Situa el nombre a la recta',
    titol:    'Situa el nombre a la recta',
    ajuda:    'Toca la recta al lloc on és el nombre.',
    comenca:  'On és el nombre? Toca la recta.',
    aqui:     'has tocat aquí',
    encert:   '{nom} és entre {baix} i {alt}.',
    pista:    'El nombre és més a la *{banda}*. És entre *{baix}* i *{alt}*: toca entre aquests dos.',
    mostra:   'Mira on és *{nom}*: és entre *{baix}* i *{alt}*.',
    dreta:    'dreta',
    esquerra: 'esquerra'
  },

  "1.3": {
    nom:       'Els decimals s\'acaben?',
    titol:     'Els decimals s\'acaben?',
    ajuda:     'Mira els decimals de la pantalla. Després tria una resposta.',
    comenca:   'Tria una resposta.',
    boto_si:   'Els decimals s\'acaben',
    boto_no:   'Els decimals no s\'acaben mai',
    encert_si: '{nom} és exactament *{valor}*. Els decimals s\'acaben.',
    encert_no: '{nom} té decimals que no s\'acaben mai.',
    pista_si:  'Mira el final de la pantalla. No hi ha els tres punts «…». El nombre és *{valor}* i prou.',
    pista_no:  'Mira el final de la pantalla. Hi ha els tres punts «…». Vol dir que els decimals continuen.'
  },

  "1.4": {
    nom:           'Arrodoneix i calcula el preu',
    titol:         'Arrodoneix i calcula el preu',
    ajuda:         'La botiga només ven metres sencers: 1 m, 2 m, 3 m.',
    et_necessites: 'Necessites',
    mat_1:         'Corda',
    mat_2:         'Cinta',
    mat_3:         'Cable',
    mat_etiqueta:  '{nom} · {preu}/m',
    barra_just:    'Necessites {m} m',
    barra_amunt:   'Compres {m} m, arrodonit cap amunt',
    just:          'Són metres sencers. No pagues res de més.',
    de_mes:        'Pagues *{dif}* de més, perquè has arrodonit cap amunt.'
  },

  "1.5": {
    nom:        'Quant val cada xifra?',
    titol:      'Quant val cada xifra?',
    ajuda:      'Toca una xifra. Mira quant val.',
    comenca:    'Toca una xifra de la taula.',
    val:        'El *{xifra}* és a les *{lloc}*. Val *{quant}*.',
    et_suma:    'El mateix nombre, escrit com una suma',
    centenes:   'centenes',
    desenes:    'desenes',
    unitats:    'unitats',
    decimes:    'dècimes',
    centesimes: 'centèsimes',
    millesimes: 'mil·lèsimes'
  },

  "1.6": {
    nom:       'Canvia d\'unitat',
    titol:     'Canvia d\'unitat',
    ajuda:     'Tria una unitat. Mira on va la coma.',
    et_mesura: 'La mateixa longitud, amb una altra unitat',
    surto:     'comences aquí',
    igual:     '*{a}* i *{b}* són exactament la mateixa longitud.',
    valor:     'La longitud és *{a}*.',
    mateixa:   'És la unitat on comences. La coma no es mou.',
    dreta:     'La coma es mou *{graons}* llocs a la *dreta*.',
    esquerra:  'La coma es mou *{graons}* llocs a l\'*esquerra*.',
    dreta1:    'La coma es mou *1* lloc a la *dreta*.',
    esquerra1: 'La coma es mou *1* lloc a l\'*esquerra*.'
  },

  "5": {
    titol:     'Llegeix la paràbola',
    ajuda:     'Fes els tres passos. A cada pas, toca sobre el dibuix.',
    vertex:    'Toca el punt més alt de la corba.',
    talls:     'Toca els dos punts on la corba toca el terra.',
    eix:       'Toca el lloc on partiries la corba en dues meitats iguals.',
    toca:      'Toca sobre el dibuix.',
    exemple:   '*Exemple.* Aquest pas ja està fet. Toca *Següent pas*.',
    b_vertex:  '*El vèrtex.* {que}',
    b_talls:   '*Els punts de tall.* {que}',
    b_eix:     '*L\'eix de simetria.* {que}',
    un_tall:   'Ara toca l\'altre punt.',
    p_vertex:  'Segueix la corba amb el dit, d\'esquerra a dreta. Para on deixa de pujar.',
    p_talls:   'El terra és la línia de baix, on l\'altura és 0. Busca on la toca la corba.',
    p_eix:     'Primer busca el punt més alt. La línia passa per aquest punt, de dalt a baix.',
    mostra:    'Mira on és. Ara està marcat al dibuix.',
    tot:       'Aquí tens els tres elements de la paràbola.',
    repeteix:  'Torna a començar',
    mostra_tot:'Mostra-ho tot'
  },

  "6": {
    titol:       'Prova números a la balança',
    ajuda:       'Canvia la x. Mira si les dues bandes pesen igual.',
    x_val:       'La x val',
    es_sol:      '*x = {x} és una solució.* Les dues bandes valen {v}.',
    no_sol:      '*x = {x} no és una solució.* La banda {banda} pesa més.',
    esquerra:    'esquerra',
    dreta:       'dreta',
    p_mes:       'Prova un número més gran.',
    p_menys:     'Prova un número més petit.',
    exemple:     '*Exemple.* x = {x} és la solució. Tria una altra equació per provar-ho tu.',
    trobades:    'Solucions trobades: {fets} de {total}',
    r_solucions: 'Solucions trobades',
    r_proves:    'Números provats',
    solucions:   'Les solucions són {llista}.',
    solucio:     'La solució és {llista}.'
  }
};

/* ============================================================================
   D'AQUÍ CAP AVALL NO CAL TOCAR RES.
   Són les explicacions que fa servir textos.html per dir on surt cada frase i
   quins forats {} necessita. Si algun dia s'afegeix una frase nova, afegeix-hi
   també la seva línia: el test de eines/comprova.py avisa si en falta alguna.
   ========================================================================== */

window.TEXTOS_GUIA = {
  "comu": {
    correcte:     ["Comença la resposta quan és correcta", []],
    incorrecte:   ["Comença la resposta quan és incorrecta", []],
    altra_manera: ["Va just després de «Incorrecte»", []],
    pista:        ["Etiqueta davant de cada pista", []],
    inici:        ["Primer extrem del rètol de progrés", []],
    final:        ["Últim extrem del rètol de progrés", []],
    pas:          ["Comptador del rètol de progrés", ["n", "total"]],
    rotul_final:  ["Comptador quan la tasca ja s'ha acabat", []],
    seguent:      ["Botó per passar al pas següent", []],
    acaba:        ["El mateix botó, a l'últim pas", []],
    exemple:      ["Etiqueta del cas que ve resolt", []],
    represa:      ["Pregunta quan hi ha una tasca a mitges", ["n", "total"]],
    represa_dia:  ["Dia en què es va desar la tasca a mitges", ["dia"]],
    continua:     ["Botó per continuar la tasca a mitges", ["n"]],
    de_nou:       ["Botó per començar de zero", []],
    represa_nota: ["Nota per a un ordinador que fa servir més gent", []],
    has_acabat:   ["Títol del resum final", []],
    r_tasca:      ["Resum: fila del nom de la tasca", []],
    r_dia:        ["Resum: fila del dia", []],
    r_passos:     ["Resum: quants passos té la tasca", []],
    r_primer:     ["Resum: correctes sense cap pista", []],
    r_pista:      ["Resum: correctes després d'una pista", []],
    r_mostrat:    ["Resum: passos en què l'app ha ensenyat la resposta", []],
    nom_paper:    ["Línia per escriure el nom, només al paper imprès", []],
    codi:         ["Rètol del codi de verificació", []],
    ensenya_codi: ["Què ha de fer amb el codi", []],
    imprimeix:    ["Botó per imprimir el resum", []],
    torna:        ["Botó per començar la tasca de nou", []]
  },
  "0": {
    titol:     ["Títol de la columna dels casos", []],
    com_va:    ["La instrucció del bucle, sempre a la vista", []],
    tecla:     ["Comptador de tecles, amb el nom de la tecla", ["n", "total", "k"]],
    seguent:   ["Botó per passar a la tecla següent", []],
    enrere:    ["Botó per tornar a la tecla anterior", []],
    acaba:     ["El botó de la tecla següent, a l'última tecla", []],
    nota_punt: ["Nota de la coma decimal, a la columna dels casos", []],
    teclat_pc: ["Nota del teclat, només amb ratolí", []],
    dalt:      ["Rètol de la zona de dalt del teclat", []],
    baix:      ["Rètol de la zona de baix del teclat", []],
    r_tecles:  ["Resum: quantes tecles té el cas", []]
  },
  "1.1": {
    nom:       ["Nom a la barra de fletxes", []],
    titol:     ["Títol de la primera targeta", []],
    ajuda:     ["Línia sota el títol", []],
    marca:     ["Etiqueta del cas que ve resolt (buida: no surt)", []],
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
    encert:   ["Quan encerta (va després de «Correcte.»)", ["nom", "baix", "alt"]],
    pista:    ["Pista del primer error", ["banda", "baix", "alt"]],
    mostra:   ["Al segon error: l'app ensenya on és", ["nom", "baix", "alt"]],
    dreta:    ["Paraula que omple {banda}", []],
    esquerra: ["Paraula que omple {banda}", []]
  },
  "1.3": {
    nom:       ["Nom a la barra de fletxes", []],
    titol:     ["Títol de la targeta", []],
    ajuda:     ["Línia sota el títol", []],
    comenca:   ["Avís abans de contestar", []],
    boto_si:   ["Botó de l'esquerra", []],
    boto_no:   ["Botó de la dreta", []],
    encert_si: ["Encerta i el nombre s'acaba", ["nom", "valor"]],
    encert_no: ["Encerta i el nombre no s'acaba", ["nom"]],
    pista_si:  ["Pista quan diu que no s'acaba i sí que s'acaba", ["valor"]],
    pista_no:  ["Pista quan diu que s'acaba i no s'acaba", []]
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
  },
  "5": {
    titol:     ["Títol de la targeta", []],
    ajuda:     ["Línia sota el títol", []],
    vertex:    ["Consigna del pas 1", []],
    talls:     ["Consigna del pas 2", []],
    eix:       ["Consigna del pas 3", []],
    toca:      ["Avís abans de tocar", []],
    exemple:   ["Avís del pas que ja ve fet a la pilota", []],
    b_vertex:  ["Quan troba el vèrtex (el fenomen omple {que})", ["que"]],
    b_talls:   ["Quan troba els dos talls", ["que"]],
    b_eix:     ["Quan troba l'eix", ["que"]],
    un_tall:   ["Quan ha trobat el primer dels dos talls", []],
    p_vertex:  ["Pista del pas 1", []],
    p_talls:   ["Pista del pas 2", []],
    p_eix:     ["Pista del pas 3", []],
    mostra:    ["Al segon error: l'app marca la resposta", []],
    tot:       ["Frase del final, amb el dibuix sencer", []],
    repeteix:  ["Botó per tornar a començar", []],
    mostra_tot:["Botó per ensenyar-ho tot i acabar", []]
  },
  "6": {
    titol:       ["Títol de la targeta", []],
    ajuda:       ["Línia sota el títol", []],
    x_val:       ["Rètol sobre el valor de la x", []],
    es_sol:      ["Quan el valor provat és solució", ["x", "v"]],
    no_sol:      ["Quan el valor provat no és solució", ["x", "banda"]],
    esquerra:    ["Paraula que omple {banda}", []],
    dreta:       ["Paraula que omple {banda}", []],
    p_mes:       ["Pista quan cal un número més gran", []],
    p_menys:     ["Pista quan cal un número més petit", []],
    exemple:     ["Avís de l'equació d'exemple", ["x"]],
    trobades:    ["Comptador de solucions", ["fets", "total"]],
    r_solucions: ["Resum: quantes solucions ha trobat", []],
    r_proves:    ["Resum: quants valors ha provat", []],
    solucions:   ["Frase del final amb dues solucions o més", ["llista"]],
    solucio:     ["Frase del final amb una sola solució", ["llista"]]
  }
};
