/* ============================================================================
   dades/textos.js · TOTES les frases que llegeix l'alumnat a la caixa d'eines
   ----------------------------------------------------------------------------
   Aquest és l'únic lloc on s'han de canviar les paraules. Ni el marcatge ni el
   codi en tenen cap: les llegeixen d'aquí.

   COM S'EDITA
     · Canvia només el text entre cometes.
     · *Entre asteriscs* surt en negreta.
     · {això} és un forat que s'omple sol amb un número o unes paraules.
       NO el canviïs de nom ni l'esborris: si falta, la frase perd la dada.
       {rect} s'omple amb la lectura del rectangle: «3 files de 4 quadrets».
       {quadrets} s'omple amb el número i la paraula: «12 quadrets», «1 quadret».
       {de} s'omple amb «del 7» o «de l'1».
     · Si vols una cometa simple dins del text, escriu-la amb barra: \'

   COM S'ESCRIU (Lectura Fàcil, norma UNE 153101:2018 EX, i les regles de
   docs/CRITERIS-DISSENY.md)
     · Una consigna per frase. Frases curtes: el test avisa a partir de 15
       paraules i falla a partir de 20.
     · Imperatiu i paraules de cada dia: «Tria», «Toca», «Mira», «Marca».
     · Literal: «quant és», no «quant fa». Sense «ho» ni «hi» que obliguin a
       buscar de què es parla.
     · La mateixa paraula per a la mateixa cosa, aquí i a les fitxes: «quadret»,
       «fila», «rectangle», «taula». Les unitats, sempre: «12 quadrets».
     · El punt volat per multiplicar: 3 · 4. La creu i la lletra x, mai.
     · Cap nombre de més de 999.
     · Una resposta equivocada es diu «Incorrecte» i va seguida d'una pista que
       proposa un camí diferent, no de la mateixa consigna repetida.

   Es pot editar a mà o amb textos.html, que és una pàgina per al professorat
   que ensenya cada frase en un camp, avisa si falta un forat i et dona el
   fitxer ja fet per substituir aquest.
   ========================================================================== */

window.TEXTOS = {

  /* ---------------------------------------------------- comunes a tot ---- */
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
    buida:        'Buida-ho',
    comprova:     'Comprova',
    treu:         'treu-ne un',
    afegeix:      'afegeix-ne un',
    ja_fet:       'Aquest pas ja està fet. Toca *Següent pas*.',
    fila:         'fila',
    files:        'files',
    quadret:      'quadret',
    quadrets:     'quadrets',
    centena:      'centena',
    centenes:     'centenes',
    desena:       'desena',
    desenes:      'desenes',
    unitat:       'unitat',
    unitats:      'unitats',
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

  /* ------------------------------------------------ 0 · Taules ---------- */
  "0.1": {
    nom:          'La taula',
    titol:        'Les taules de multiplicar',
    ajuda:        'Tria una taula. Després toca una fila.',
    taula:        'La taula {de}',
    fila_aria:    '{a} per {b} és igual a {p}',
    files:        '{rect}.',
    total:        'En total, {quadrets}.',
    dibuix:       'Rectangle de {rect}. En total, {quadrets}.',
    clau_q:       'Vols saber quant és {a} · {b}?',
    clau_1:       'Busca la taula {de}.',
    clau_2:       'Baixa fins a {a} · {b}.',
    clau_3:       'La resposta és *{p}*.'
  },
  "0.2": {
    nom:          'Troba el resultat a la taula',
    titol:        'Troba el resultat a la taula',
    ajuda:        'Busca el resultat com diu la targeta.',
    pregunta:     'Quant és {a} · {b}?',
    comenca:      'Tria una taula.',
    toca_fila:    'Ara toca una fila.',
    encert:       '{a} · {b} = {p}.',
    encert_girat: '{b} · {a} = {p}. És el mateix que {a} · {b}.',
    fet:          'Has tocat {t} · {b} = {q}.',
    p_taula:      'El primer número és el {a}. Tria la taula {de}.',
    p_fila:       'Ara baixa per la taula fins a {a} · {b}.',
    mostra:       'Mira la fila marcada: {a} · {b} = {p}.'
  },

  /* --------------------------------------------- 1 · Rectangles ---------- */
  "1.1": {
    nom:          'Fes un rectangle',
    titol:        'Multiplicar és fer un rectangle',
    ajuda:        'Toca un quadret de la quadrícula. El rectangle arriba fins allà.',
    et_files:     'Files',
    et_cols:      'Quadrets a cada fila',
    buit:         'Toca un quadret de la quadrícula.',
    files:        '{rect}.',
    total:        'En total, {quadrets}.'
  },
  "1.2": {
    nom:          'El rectangle d\'una multiplicació',
    titol:        'El rectangle d\'una multiplicació',
    ajuda:        'Toca el quadret on acaba el rectangle.',
    pregunta:     'Fes el rectangle de {a} · {b}.',
    comenca:      'Toca un quadret de la quadrícula.',
    encert:       '{rect}. En total, {quadrets}: {a} · {b} = {p}.',
    encert_girat: 'Has fet el rectangle girat: {rect}. També són {quadrets}.',
    fet:          'Has fet {rect}.',
    pista:        'Compta {a} files cap avall. Després compta {b} quadrets cap a la dreta.',
    mostra:       'Mira el rectangle: {rect}.'
  },
  "1.3": {
    nom:          'Gira el rectangle',
    titol:        'Gira el rectangle',
    ajuda:        'Toca el botó. Mira si canvia el nombre de quadrets.',
    gira:         'Gira el rectangle',
    torna:        'Torna a girar-lo',
    files:        '{rect}.',
    total:        'En total, {quadrets}.',
    iguals:       'Hi ha els mateixos quadrets.'
  },
  "1.4": {
    nom:          'Parteix el rectangle',
    titol:        'Parteix el rectangle',
    ajuda:        'Toca el botó. El rectangle es parteix pel 10.',
    parteix:      'Parteix pel 10',
    ajunta:       'Torna a ajuntar-lo',
    abans:        '{rect}.',
    fora:         'La targeta només arriba fins al 10.',
    dues:         'Ara són dues multiplicacions de la targeta.',
    suma:         'Suma les dues parts: {p1} + {p2} = {p}.',
    total:        'En total, {quadrets}.',
    aria_partit:  'Dues parts: {a} · 10 = {p1} i {a} · {u} = {p2}.'
  },

  /* ----------------------------------------------- 2 · Quadrats ---------- */
  "2.1": {
    nom:          'El quadrat d\'un nombre',
    titol:        'El quadrat d\'un nombre',
    ajuda:        'Tria quants quadrets té el costat.',
    files:        '{rect}.',
    total:        'En total, {quadrets}.',
    curt:         'Escrit més curt:',
    llegeix:      'Es llegeix: {n} al quadrat.'
  },
  "2.2": {
    nom:          'Quin dibuix és?',
    titol:        'Quin dibuix és?',
    ajuda:        'Llegeix la pregunta. Després toca un dibuix.',
    pregunta_q:   'Quin dibuix és {n}²?',
    pregunta_d:   'Quin dibuix és {n} · 2?',
    comenca:      'Mira quantes files té cada dibuix.',
    encert_q:     '{n}² = {n} · {n} = {q}. És un quadrat de {n} per {n}.',
    encert_d:     '{n} · 2 = {d}. Són {n} files de 2 quadrets.',
    es_q:         'Aquest dibuix és {n}² = {q}.',
    es_d:         'Aquest dibuix és {n} · 2 = {d}. No és un quadrat.',
    p_q:          '{n}² vol dir {n} · {n}. Busca {n} files de {n} quadrets.',
    p_d:          '{n} · 2 vol dir {n} files de 2 quadrets.',
    aria:         'Dibuix de {rect}'
  },
  "2.3": {
    nom:          'El costat del quadrat',
    titol:        'El costat del quadrat',
    ajuda:        'Tria quants quadrets tens. Mira si fan un quadrat.',
    et:           'Quadrets',
    exacte:       'Amb {quadrets} fas un quadrat {de_k} per {k}.',
    costat:       'El costat té {costat}.',
    llegeix:      'Es llegeix: l\'arrel quadrada {de_n} és {k}.',
    no_fa:        'Amb {quadrets} no pots fer cap quadrat.',
    petit:        'El quadrat {de_k} per {k} té {quadrets}.',
    gran:         'Per fer el quadrat {de_k} per {k}, calen {quadrets}.',
    entre:        '{n} és entre {q1} i {q2}.',
    arrel:        'L\'arrel quadrada {de_n} és entre {k} i {k2}.'
  },

  /* ------------------------------------------------ 3 · Nombres ---------- */
  "3.1": {
    nom:          'Centenes, desenes i unitats',
    titol:        'Centenes, desenes i unitats',
    ajuda:        'Posa quadrats, columnes i quadrets. Mira quin nombre surt.',
    et_c:         'Centenes',
    sub_c:        'quadrats de 100',
    et_d:         'Desenes',
    sub_d:        'columnes de 10',
    et_u:         'Unitats',
    sub_u:        'quadrets solts',
    quadrat:      'quadrat de 100',
    quadrats:     'quadrats de 100',
    columna:      'columna de 10',
    columnes:     'columnes de 10',
    solt:         'quadret solt',
    solts:        'quadrets solts',
    compta:       '{c}, {d} i {u}.',
    llegeix:      'Es llegeix: *{nom}*.',
    llegenda_u:   'Un quadret val 1.',
    llegenda_d:   'Una columna té 10 quadrets. Val 10.',
    llegenda_c:   'Un quadrat té 10 files de 10 quadrets: 10 · 10 = 100.'
  },
  "3.2": {
    nom:          'Fes el nombre',
    titol:        'Fes el nombre',
    ajuda:        'Els blocs són quadrats de 100, columnes de 10 i quadrets solts.',
    pregunta:     'Fes el nombre {n}.',
    comenca:      'Posa els blocs. Després toca *Comprova*.',
    encert:       '{compta} Es llegeix: *{nom}*.',
    fet:          'Has fet {el_m}.',
    pista:        'Mira la taula. Cada xifra diu quants blocs cal posar.',
    mostra:       'Mira els blocs: {compta} Es llegeix: *{nom}*.'
  },

  /* -------------------------------------------------- 4 · Ordre ---------- */
  "4.1": {
    nom:          'Mira l\'ordre',
    titol:        'L\'ordre de les operacions',
    ajuda:        'Tria una operació. Mira què es fa primer.',
    primer_m:     'Primer, la multiplicació: {op} = {r}.',
    primer_p:     'Primer, el parèntesi: {op} = {r}.',
    despres_s:    'Després, la suma: {op} = {r}.',
    despres_m:    'Després, la multiplicació: {op} = {r}.',
    total:        'En total, {quadrets}.',
    regla_m:      'Sense parèntesis, primer es multiplica.',
    regla_p:      'Amb parèntesis, primer es fa el parèntesi.'
  },
  "4.2": {
    nom:          'Què es fa primer?',
    titol:        'Què es fa primer?',
    ajuda:        'Toca el signe de l\'operació que es fa primer.',
    comenca:      'Toca el signe + o el punt.',
    encert:       'Primer, {op1} = {r1}. Després, {op2} = {r2}.',
    fet_s:        'Has triat la suma.',
    fet_m:        'Has triat la multiplicació.',
    p_mult:       'Sense parèntesis, primer es multiplica. Busca el punt.',
    p_par:        'Hi ha un parèntesi. El que hi ha a dins es fa primer.',
    aria_suma:    '{a} més {b}',
    aria_mult:    '{a} per {b}'
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
    buida:        ["Botó que deixa la quadrícula buida", []],
    comprova:     ["Botó per comprovar el nombre fet amb blocs", []],
    treu:         ["Lector de pantalla: el botó − d'un comptador", []],
    afegeix:      ["Lector de pantalla: el botó + d'un comptador", []],
    ja_fet:       ["Quan es reprèn una tasca en un pas que ja estava contestat", []],
    fila:         ["Paraula: una fila del rectangle (1 fila)", []],
    files:        ["Paraula: més d'una fila (3 files)", []],
    quadret:      ["Paraula: un quadret (1 quadret)", []],
    quadrets:     ["Paraula: més d'un quadret (12 quadrets)", []],
    centena:      ["Paraula: 1 centena", []],
    centenes:     ["Paraula: 2 centenes, 0 centenes", []],
    desena:       ["Paraula: 1 desena", []],
    desenes:      ["Paraula: 4 desenes, 0 desenes", []],
    unitat:       ["Paraula: 1 unitat", []],
    unitats:      ["Paraula: 3 unitats, 0 unitats", []],
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
  "0.1": {
    nom:          ["Nom de la subtasca a la barra de fletxes", []],
    titol:        ["Títol de la targeta", []],
    ajuda:        ["Consigna sota el títol", []],
    taula:        ["Títol de la taula triada: «La taula del 7»", ["de"]],
    fila_aria:    ["Lector de pantalla: el que diu cada fila de la taula", ["a", "b", "p"]],
    files:        ["Sota el dibuix: la lectura del rectangle", ["rect"]],
    total:        ["Sota el dibuix: quants quadrets hi ha", ["quadrets"]],
    dibuix:       ["Lector de pantalla: el que diu el dibuix", ["rect", "quadrets"]],
    clau_q:       ["Clau de la targeta: la pregunta", ["a", "b"]],
    clau_1:       ["Clau de la targeta: primer pas", ["de"]],
    clau_2:       ["Clau de la targeta: segon pas", ["a", "b"]],
    clau_3:       ["Clau de la targeta: tercer pas", ["p"]]
  },
  "0.2": {
    nom:          ["Nom de la subtasca a la barra de fletxes", []],
    titol:        ["Títol de la targeta", []],
    ajuda:        ["Consigna sota el títol", []],
    pregunta:     ["La multiplicació que s'ha de buscar", ["a", "b"]],
    comenca:      ["Avís abans de triar la taula", []],
    toca_fila:    ["Avís quan ja s'ha triat la taula", []],
    encert:       ["Resposta correcta", ["a", "b", "p"]],
    encert_girat: ["Resposta correcta buscada a l'altra taula: 7 · 6 per 6 · 7", ["a", "b", "p"]],
    fet:          ["Resposta equivocada: la fila que ha tocat", ["t", "b", "q"]],
    p_taula:      ["Pista quan la taula no és la bona", ["a", "de"]],
    p_fila:       ["Pista quan la taula és bona però la fila no", ["a", "b"]],
    mostra:       ["Segon error: la caixa marca la fila bona", ["a", "b", "p"]]
  },
  "1.1": {
    nom:          ["Nom de la subtasca a la barra de fletxes", []],
    titol:        ["Títol de la targeta", []],
    ajuda:        ["Consigna sota el títol", []],
    et_files:     ["Rètol del comptador de files", []],
    et_cols:      ["Rètol del comptador de quadrets de cada fila", []],
    buit:         ["Sota la quadrícula buida", []],
    files:        ["Sota el dibuix: la lectura del rectangle", ["rect"]],
    total:        ["Sota el dibuix: quants quadrets hi ha", ["quadrets"]]
  },
  "1.2": {
    nom:          ["Nom de la subtasca a la barra de fletxes", []],
    titol:        ["Títol de la targeta", []],
    ajuda:        ["Consigna sota el títol", []],
    pregunta:     ["El rectangle que s'ha de fer", ["a", "b"]],
    comenca:      ["Avís abans de contestar", []],
    encert:       ["Resposta correcta", ["rect", "quadrets", "a", "b", "p"]],
    encert_girat: ["Resposta correcta amb el rectangle girat", ["rect", "quadrets"]],
    fet:          ["Resposta equivocada: el rectangle que ha fet", ["rect"]],
    pista:        ["Pista del primer error", ["a", "b"]],
    mostra:       ["Segon error: la caixa dibuixa el rectangle bo", ["rect"]]
  },
  "1.3": {
    nom:          ["Nom de la subtasca a la barra de fletxes", []],
    titol:        ["Títol de la targeta", []],
    ajuda:        ["Consigna sota el títol", []],
    gira:         ["Botó per girar el rectangle", []],
    torna:        ["El mateix botó, quan ja està girat", []],
    files:        ["Sota el dibuix: la lectura del rectangle", ["rect"]],
    total:        ["Sota el dibuix: quants quadrets hi ha", ["quadrets"]],
    iguals:       ["Sota el dibuix, un cop girat", []]
  },
  "1.4": {
    nom:          ["Nom de la subtasca a la barra de fletxes", []],
    titol:        ["Títol de la targeta", []],
    ajuda:        ["Consigna sota el títol", []],
    parteix:      ["Botó per partir el rectangle", []],
    ajunta:       ["El mateix botó, quan ja està partit", []],
    abans:        ["Sota el dibuix sencer: la lectura del rectangle", ["rect"]],
    fora:         ["Per què s'ha de partir", []],
    dues:         ["Sota el dibuix partit", []],
    suma:         ["Sota el dibuix partit: la suma de les dues parts", ["p1", "p2", "p"]],
    total:        ["Sota el dibuix partit: quants quadrets hi ha", ["quadrets"]],
    aria_partit:  ["Lector de pantalla: el dibuix partit", ["a", "u", "p1", "p2"]]
  },
  "2.1": {
    nom:          ["Nom de la subtasca a la barra de fletxes", []],
    titol:        ["Títol de la targeta", []],
    ajuda:        ["Consigna sota el títol", []],
    files:        ["Sota el dibuix: la lectura del quadrat", ["rect"]],
    total:        ["Sota el dibuix: quants quadrets hi ha", ["quadrets"]],
    curt:         ["Davant de 3² = 9", []],
    llegeix:      ["Com es llegeix 3²", ["n"]]
  },
  "2.2": {
    nom:          ["Nom de la subtasca a la barra de fletxes", []],
    titol:        ["Títol de la targeta", []],
    ajuda:        ["Consigna sota el títol", []],
    pregunta_q:   ["Pregunta quan es busca el quadrat", ["n"]],
    pregunta_d:   ["Pregunta quan es busca el rectangle de n files de 2", ["n"]],
    comenca:      ["Avís abans de contestar", []],
    encert_q:     ["Resposta correcta: el quadrat", ["n", "q"]],
    encert_d:     ["Resposta correcta: el rectangle", ["n", "d"]],
    es_q:         ["Resposta equivocada: ha tocat el quadrat", ["n", "q"]],
    es_d:         ["Resposta equivocada: ha tocat el rectangle", ["n", "d"]],
    p_q:          ["Pista quan es buscava el quadrat", ["n"]],
    p_d:          ["Pista quan es buscava el rectangle", ["n"]],
    aria:         ["Lector de pantalla: el que diu cada dibuix", ["rect"]]
  },
  "2.3": {
    nom:          ["Nom de la subtasca a la barra de fletxes", []],
    titol:        ["Títol de la targeta", []],
    ajuda:        ["Consigna sota el títol", []],
    et:           ["Rètol del comptador de quadrets", []],
    exacte:       ["Quan els quadrets fan un quadrat", ["quadrets", "de_k", "k"]],
    costat:       ["Quan fan un quadrat: quants quadrets té el costat", ["costat"]],
    llegeix:      ["Com es llegeix √16 = 4", ["de_n", "k"]],
    no_fa:        ["Quan els quadrets no fan cap quadrat", ["quadrets"]],
    petit:        ["El quadrat més gran que es pot fer", ["de_k", "k", "quadrets"]],
    gran:         ["El quadrat següent, que no es pot acabar", ["de_k", "k", "quadrets"]],
    entre:        ["Entre quins quadrats és", ["n", "q1", "q2"]],
    arrel:        ["Entre quins nombres és l'arrel", ["de_n", "k", "k2"]]
  },
  "3.1": {
    nom:          ["Nom de la subtasca a la barra de fletxes", []],
    titol:        ["Títol de la targeta", []],
    ajuda:        ["Consigna sota el títol", []],
    et_c:         ["Rètol: comptador, zona dels blocs i columna de la taula", []],
    sub_c:        ["Sota el rètol del comptador de centenes", []],
    et_d:         ["Rètol: comptador, zona dels blocs i columna de la taula", []],
    sub_d:        ["Sota el rètol del comptador de desenes", []],
    et_u:         ["Rètol: comptador, zona dels blocs i columna de la taula", []],
    sub_u:        ["Sota el rètol del comptador d'unitats", []],
    quadrat:      ["Sota els blocs: 1 quadrat de 100", []],
    quadrats:     ["Sota els blocs: 2 quadrats de 100", []],
    columna:      ["Sota els blocs: 1 columna de 10", []],
    columnes:     ["Sota els blocs: 4 columnes de 10", []],
    solt:         ["Sota els blocs: 1 quadret solt", []],
    solts:        ["Sota els blocs: 3 quadrets solts", []],
    compta:       ["Quantes centenes, desenes i unitats hi ha", ["c", "d", "u"]],
    llegeix:      ["Com es llegeix el nombre", ["nom"]],
    llegenda_u:   ["Llegenda: què val un quadret", []],
    llegenda_d:   ["Llegenda: què val una columna", []],
    llegenda_c:   ["Llegenda: què val un quadrat", []]
  },
  "3.2": {
    nom:          ["Nom de la subtasca a la barra de fletxes", []],
    titol:        ["Títol de la targeta", []],
    ajuda:        ["Consigna sota el títol", []],
    pregunta:     ["El nombre que s'ha de fer", ["n"]],
    comenca:      ["Avís abans de contestar", []],
    encert:       ["Resposta correcta", ["compta", "nom"]],
    fet:          ["Resposta equivocada: el nombre que ha fet", ["el_m"]],
    pista:        ["Pista del primer error, amb la taula a la vista", []],
    mostra:       ["Segon error: la caixa posa els blocs bons", ["compta", "nom"]]
  },
  "4.1": {
    nom:          ["Nom de la subtasca a la barra de fletxes", []],
    titol:        ["Títol de la targeta", []],
    ajuda:        ["Consigna sota el títol", []],
    primer_m:     ["Primer pas, quan és una multiplicació", ["op", "r"]],
    primer_p:     ["Primer pas, quan és un parèntesi", ["op", "r"]],
    despres_s:    ["Segon pas, quan és una suma", ["op", "r"]],
    despres_m:    ["Segon pas, quan és una multiplicació", ["op", "r"]],
    total:        ["Sota el dibuix: quants quadrets hi ha", ["quadrets"]],
    regla_m:      ["La regla, quan no hi ha parèntesis", []],
    regla_p:      ["La regla, quan hi ha parèntesis", []]
  },
  "4.2": {
    nom:          ["Nom de la subtasca a la barra de fletxes", []],
    titol:        ["Títol de la targeta", []],
    ajuda:        ["Consigna sota el títol", []],
    comenca:      ["Avís abans de contestar", []],
    encert:       ["Resposta correcta: els dos passos", ["op1", "r1", "op2", "r2"]],
    fet_s:        ["Resposta equivocada: ha tocat el signe +", []],
    fet_m:        ["Resposta equivocada: ha tocat el punt", []],
    p_mult:       ["Pista quan no hi ha parèntesis", []],
    p_par:        ["Pista quan hi ha parèntesis", []],
    aria_suma:    ["Lector de pantalla: el signe +", ["a", "b"]],
    aria_mult:    ["Lector de pantalla: el punt de multiplicar", ["a", "b"]]
  }
};
