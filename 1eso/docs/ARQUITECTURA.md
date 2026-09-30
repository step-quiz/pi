# Arquitectura de la caixa d'eines

Com està muntada la caixa d'eines d'aquesta carpeta i com ampliar-la sense trencar res. Les
regles de què es veu a la pantalla, i per què, són a [`CRITERIS-DISSENY.md`](CRITERIS-DISSENY.md),
apartat 3.

És la mateixa arquitectura que la caixa de `4eso/`, descrita a
[`../../4eso/docs/ARQUITECTURA.md`](../../4eso/docs/ARQUITECTURA.md). Aquest document diu el que és
igual en una línia i s'atura en el que canvia.

---

## 1. Què és igual que a l'altra caixa, i què no

**Igual.** Estàtica i sense pas de compilació: s'obre amb doble clic, sense servidor ni connexió.
Scripts clàssics i no mòduls ES, perquè el navegador bloqueja els mòduls quan s'obre un fitxer
amb doble clic. Un sol nom global, `CE`. Cap dependència externa. Les frases, totes a
`dades/textos.js`. El mateix motor de tasques tancades, el mateix codi de verificació i les
mateixes pàgines per llegir codis i per canviar frases.

**Els fitxers són còpies, no enllaços.** Si la caixa de `4eso/` canvia, aquesta no s'ha de moure.

**El que canvia:**

| | A l'altra caixa | Aquí |
|---|---|---|
| La tasca 0, la que surt sempre | La calculadora | La targeta de les taules: cap exercici no necessita calculadora |
| El dibuix | Cada mòdul el seu | Un de sol, la quadrícula, a `js/quadricula.js` |
| Subtasques | Només un mòdul en té | Tots en tenen. `?task=1.3` va lligat a la tasca 1 |
| Memòria del navegador | `pi-tasca:…`, `caixa-modul` | `pi1-tasca:…`, `pi1-caixa-modul` |
| Sal del codi de verificació | La seva | Una altra: un codi d'una caixa no val a l'altra |
| La gramàtica | A les frases | Al nucli: «1 quadret», «d'11 quadrets», «la taula de l'1» |

Les dues caixes es publiquen al mateix domini. Sense les claus `pi1-` i la sal pròpia,
compartirien la memòria del navegador, i un codi de l'una es llegiria com a vàlid a l'altra.
`eines/comprova.py` ho vigila.

---

## 2. Els fitxers

| Fitxer | Què fa |
|---|---|
| `caixa-eines.html` | El marcatge de les 29 eines. Cap frase: només `data-text="1.2.titol"` |
| `verifica.html` | Llegeix els codis de verificació, un o molts alhora |
| `textos.html` | Totes les frases en una pàgina, per canviar-les i baixar el fitxer nou |
| `dades/textos.js` | Totes les frases (`window.TEXTOS`) i què fa cadascuna (`window.TEXTOS_GUIA`) |
| `css/app.css` | Els estils de la pantalla. Fa servir els colors de `css/tokens.css` |
| `js/nucli.js` | L'objecte `CE`: el poc que comparteixen tots els mòduls |
| `js/codi.js` | El codi de verificació (`K7Q-M2X-9RT`) |
| `js/tasca.js` | El motor de les tasques tancades |
| `js/quadricula.js` | El dibuix de tot el curs: quadrets, rectangles, la taula de quadrets, els blocs |
| `js/moduls/*.js` | Les 29 eines, una per fitxer. Es carreguen quan s'obren (`CE.carrega`) |
| `js/app.js` | Les pestanyes i els enllaços `?task=n`. Va l'últim |

L'ordre de càrrega és aquest i no un altre, i el test el comprova:
`dades/textos.js` → `js/nucli.js` → `js/codi.js` → `js/tasca.js` → `js/quadricula.js` →
`js/app.js`.

**Les eines es carreguen quan s'obren** (30/9/2026). Abans la pàgina carregava les 29 d'entrada.
Ara cada pestanya diu el fitxer del seu mòdul a `data-src`, i `CE.carrega(id)` (a `js/nucli.js`)
el carrega la primera vegada que s'obre. Si una eina fa servir una funció d'una altra (els botons
Sí i No, `CE.botonsSiNo`, són de `multiples.js`), la pestanya ho diu a `data-cal="multiples"` i
aquella es carrega abans. `comprova.py` ho vigila. Les proves (`prova_caixa.py`, `auditoria.py`)
les carreguen totes d'entrada amb `CE.carregaTots()`.

**La tria d'unitat.** A sobre de les pestanyes, «Totes · Unitat 1 · … · Unitat 7» deixa veure només
les eines d'una unitat. Cada pestanya diu de quines unitats és a `data-unitats` (les `tasques` de
`dades/unitats.js`). Als enllaços `?task=n` no surt.

**No s'han de tocar** `css/tokens.css`, `css/fitxa.css`, `fonts/Caveat.ttf` ni `eines/paper.py`
per res de la caixa. Formen l'empremta del PDF de la targeta (`pdf/empremtes.json`): si en canvia
un, el test diu que el PDF és vell i cal tornar-lo a fer amb WeasyPrint. Els estils nous de la
pantalla van a `css/app.css`.

---

## 3. Les eines

| Tasca | Pestanya | Fitxer | Subtasques | S'obre amb |
|---|---|---|---|---|
| 0 | Taules | `taules.js` | 0.1 La taula · **0.2 Troba el resultat a la taula** · **0.3 El número que falta** | 7 · 8 = 56, el cas de la clau de la targeta |
| 1 | Rectangles | `rectangles.js` | 1.1 Fes un rectangle · **1.2 El rectangle d'una multiplicació** · 1.3 Gira el rectangle · 1.4 Parteix el rectangle | 3 · 4; 3 · 12 a la 1.4 |
| 2 | Quadrats | `quadrats.js` | 2.1 El quadrat d'un nombre · **2.2 Quin dibuix és?** · 2.3 El costat del quadrat · **2.4 Entre quins dos nombres?** (unitat 5) | 3² = 9; 16 quadrets a la 2.3 |
| 3 | Nombres | `nombres.js` | 3.1 Centenes, desenes i unitats · **3.2 Fes el nombre** | 243, «dos-cents quaranta-tres» |
| 4 | Ordre | `ordre.js` | 4.1 Mira l'ordre · **4.2 Què es fa primer?** | 2 + 3 · 4 = 14 |
| 5 | Múltiples | `multiples.js` | 5.1 La graella de 100 · **5.2 És múltiple?** · 5.3 Els trucs · **5.4 Múltiple de 3?** | Els múltiples del 2; el 126 a la 5.3 |
| 6 | Repartir | `repartir.js` | 6.1 Reparteix en files · **6.2 Sobren quadrets?** | 37 en files de 7: 37 = 5 · 7 + 2 |
| 7 | Divisors | `divisors.js` | 7.1 Els rectangles d'un nombre · **7.2 Troba els divisors** | Els 3 rectangles del 12 |
| 8 | Primers | `primers.js` | 8.1 El garbell d'Eratòstenes · **8.2 És primer?** | El garbell acabat: 25 primers |
| 9 | Fraccions | `fraccio.js` | 9.1 Fes la fracció · **9.2 Quina fracció és?** | 4/9, com l'activitat 0 del grup |
| 10 | Equivalents | `equivalents.js` | 10.1 Parteix els trossos · **10.2 Són equivalents?** | 2/3 = 8/12, com l'activitat 3 |
| 11 | Compara | `compara.js` | 11.1 Compara dues fraccions · **11.2 Quina és més gran?** | 1/3 i 1/5: la regla trencada |
| 12 | Sumes | `sumes.js` | 12.1 Suma i resta · **12.2 Quant és?** | 3/8 + 2/8 = 5/8 |
| 13 | Àrea | `area.js` | 13.1 Compta l'àrea · **13.2 Quina àrea té?** | La casa: 14 sencers i 2 mitjos, 15 quadrets |
| 14 | Fracció d'un nombre | `fraccnombre.js` | 14.1 Reparteix i pinta · **14.2 Quant és?** | 1/3 de 12: 3 grups de 4 quadrets |
| 15 | Multiplicar fraccions | `multfrac.js` | 15.1 El tros de tros · **15.2 Quin tros és?** | 1/2 de 1/4: 8 trossos, 1/8 |
| 16 | Percentatges | `percentatges.js` | 16.1 Pinta el percentatge · **16.2 Quin percentatge és?** | El 25 %: 25 quadrets de 100 |
| 17 | Dobles i triples | `dobletriple.js` | 17.1 El doble i el triple · **17.2 Quantes vegades hi cap?** | 3 i 6 quadrets: el doble |
| 18 | Decimals | `decimals.js` | 18.1 Fes el decimal · **18.2 Quin decimal és?** · **18.3 Quin és més gran?** | 2,43: els blocs del 243, amb el quadrat de 100 com a unitat |
| 19 | Arrodonir | `arrodonir.js` | 19.1 El decimal a la recta · **19.2 Arrodoneix** | 3,47: més a prop de 3,5; truncat, 3,4 |
| 20 | Sumar decimals | `sumadec.js` | 20.1 Suma i resta · **20.2 Quant és?** | 2,5 + 1,35 = 3,85, la regla trencada de la fitxa |
| 21 | Fracció i decimal | `fracdec.js` | 21.1 Pinta la fracció · **21.2 De fracció a decimal** | 1/4 = 0,25: 25 quadrets de 100 |
| 22 | Angles | `angles.js` | 22.1 Obre l'angle · **22.2 Quin angle és?** | Un angle agut de costats llargs, amb la cantonada |
| 23 | Polígons | `poligons.js` | 23.1 El polígon al geoplà · **23.2 Com es diu?** | El rectangle |
| 24 | Triangles | `triangles.js` | 24.1 Els tres angles · **24.2 Quin triangle és?** | El triangle rectangle: 90 + 45 + 45 |
| 25 | Perímetre | `perimetre.js` | 25.1 Perímetre i àrea · **25.2 Quin és el perímetre?** | 3 per 4: perímetre 14, àrea 12 |
| 26 | Patrons | `patrons.js` | 26.1 El patró · **26.2 Quants en té la següent?** | 2 · n + 1, figura 3: 7 quadrets |
| 27 | Símbols | `simbols.js` | 27.1 La paraula i el símbol · **27.2 Quin és el símbol?** | El triple, n = 4: 3 · 4 = 12 |
| 28 | Gràfics | `grafics.js` | 28.1 Llegeix el gràfic · **28.2 Quantes persones?** | Com venim a l'institut: 12, 8, 6 i 4 |

Les tasques 0 a 4 són de la unitat 1; les 5 a 8, de la unitat 2, i les 9 a 13, de la unitat 3 (les fraccions i l'àrea), les 14 a 17, de la unitat 4, i les 18 a 21 i la 2.4, de la unitat 5 (els decimals i l'arrel), les 22 a 25, de la unitat 6 (angles, polígons, triangles i perímetre), i les 26 a 28, de la unitat 7 (patrons, símbols i gràfics). La tasca 15 fa servir una peça nova de `js/quadricula.js`, `graella2D`, la primera de dues dimensions: la primera fracció es pinta per columnes, la segona es ressegueix per files, i el resultat, on coincideixen, porta un traç gruixut, perquè el color no sigui l'única diferència. La 0 (les taules) es veu
sempre, perquè és la targeta a la pantalla.

En negreta, les tasques tancades: cinc passos, resum i codi de verificació. Les altres són
eines per explorar: s'obren resoltes amb un exemple (la marca «Exemple») i no s'acaben mai.

Cada fitxer de mòdul explica a la capçalera què fa cada subtasca, com respon a un encert i a un
error, i per què els casos són aquests i no uns altres. Els casos estan triats perquè les sumes
no portin, les multiplicacions siguin de la targeta i cap nombre passi de 999.

**Els números de tasca no es canvien mai**: surten als enllaços que es donen a l'alumnat. Una
eina nova pren el número següent.

---

## 4. La quadrícula: `js/quadricula.js`

Tots els mòduls dibuixen amb les mateixes peces, i per això un quadret és igual a tot arreu.
Deixa a `CE.q`:

| Peça | Què dibuixa |
|---|---|
| `quadret`, `rectangle` | Un quadret, o un rectangle de quadrets, amb aire entre ells perquè es puguin comptar |
| `graella`, `text`, `clau` | La quadrícula buida, un rètol i una clau amb el seu rètol («3 files») |
| `taula` | La **taula de quadrets**: 10 per 10 amb els números de l'1 al 10 a dalt i a l'esquerra. La fan servir la 0.1, la 1.1, la 1.2, la 2.1 i la 2.3 |
| `cellaTocada`, `fletxa` | On s'ha tocat la taula, i com la mouen les fletxes del teclat |
| `blocs` | Quadrats de 100, columnes de 10 i quadrets solts, a la mateixa escala. Amb `b`, les últimes peces són la segona part: el segon sumand (`q b nou`, taronja i discontinu) o, amb `treu`, el que es resta (buit i ratllat). Ho fa servir la 20.1 |
| `graella100` | La graella de 100 de l'activitat dels múltiples del grup: cada nombre pot anar pintat, encerclat (un primer) o ratllat. La fan servir la 5.1 i la 8.1 |
| `rectanglesDe`, `divisorsDe` | Els rectangles que es poden fer amb n quadrets (sense comptar el girat dues vegades), i els divisors que en surten |
| `dibuixaRectangles` | Tots els rectangles de n, un sota l'altre i a la mateixa escala, amb el rètol «2 · 6». La fan servir la 7.1, la 7.2 i la 8.2 |
| `tira`, `fraccio` | El rectangle de les fraccions, sempre de la mateixa mida perquè es puguin comparar, partit en trossos iguals: pintats, del segon sumand (taronja), ratllats (el que es resta) o partits en trossos més petits (les equivalents). `fraccio` en posa tants com calguin per a una impròpia |
| `dec` | Un decimal escrit amb coma, a partir de les centèsimes: `dec(243)` és «2,43», `dec(350, 1)` és «3,5». Els decimals es guarden com a centèsimes enteres, fins a 999 (9,99): així els comptes surten exactes |
| `quadrat100` | El quadrat de 100 dels decimals, pintat columna a columna i sense números: 25 quadrets són 2 columnes i 5 quadrets, 0,25. La fan servir la 21.1 i la 21.2 |
| `recta` | La recta numèrica, el segon model del curs: de la dècima d'abans a la de després, una ratlla per centèsima, la del mig discontínua i el punt. La fan servir la 19.1 i la 19.2 |
| `angle`, `tipusAngle` | Un angle amb el vèrtex a baix i, si es vol, la cantonada d'un quadret al vèrtex (l'angle recte de referència). El tipus: agut, recte, obtús o pla |
| `geopla` | El geoplà de 6 per 6 punts i un polígon pels punts que es diguin |
| `triangle`, `anglesTriangle`, `tipusTriangle`, `anglesJunts` | Un triangle al geoplà amb els angles numerats, els seus angles (amb enters, el producte escalar diu si n'hi ha de recte o d'obtús sense arrodonir) i els tres angles junts, que fan un angle pla |
| `vora` | Un rectangle de quadrets amb la vora gruixuda i els costats numerats: el perímetre |
| `patro` | Una figura d'un patró a · n + b: la part fixa en taronja i discontínua, i a files de n quadrets |
| `barres` | Un gràfic de barres fet de quadrets, amb l'eix que comença a zero |
| `nomFraccio`, `htmlFraccio`, `tipusFraccio` | El nom («quatre novens», amb els noms de la targeta de les fraccions, a `frac.s_N` i `frac.p_N` de les frases), la fracció escrita com a fracció, i si és nul·la, pròpia, unitat o impròpia |

La taula de quadrets és el mateix objecte que la taula de multiplicar: el quadret de la fila 3 i
la columna 4 és la cantonada del rectangle de 3 · 4.

**Els colors van en classes**, a `css/app.css`, i mai en atributs: així el mode fosc no demana
res més. `q` és un quadret, `q b` la segona part (el tros partit, els quadrets solts), `q mal` un
intent equivocat i `q falta` un lloc buit amb traç discontinu. El color mai no és l'única
diferència: també hi ha aire, traç discontinu o un rètol.

**Moviment.** El rectangle de la 1.3 gira de debò i el de la 1.4 es parteix amb una transició.
Amb el moviment reduït del sistema (`CE.quiet()`) no hi ha animació: es passa directament al
final.

> **Compte amb `hidden` en un `<svg>`.** Els elements SVG no tenen la propietat `.hidden` dels
> elements HTML: `svg.hidden = false` no treu l'atribut i el dibuix no surt mai. Cal
> `svg.toggleAttribute("hidden", …)`. Va passar a la 4.2 i ho van trobar les proves.

---

## 5. El nucli: el que hi ha de nou

`js/nucli.js` és el de l'altra caixa, amb aquestes peces afegides:

| Peça | Per a què |
|---|---|
| `CE.subDemanada(tasca)` | La subtasca que demana l'enllaç (`?task=1.3`), només si és d'aquesta tasca. La pestanya Taules, que també surt, s'obre per la 0.1. Amb un enllaç així, la barra de subtasques no té fletxes (`.subbarra.fixa`): l'enllaç porta a aquell exercici i prou |
| `quants`, `rect`, `deN`, `delNombre`, `elNombre` | La gramàtica: «1 quadret» i «12 quadrets», «3 files de 4 quadrets» i «5 files d'11 quadrets», «la taula de l'1» i «la taula del 7», «l'11» |
| `lectura(paraules, símbols)` | El bloc de sota de cada dibuix: primer les paraules i al final el símbol |
| `comptador(cont, …)` | El control [−] 3 [+], amb els extrems desactivats |
| `pastilles(…, -1)`, `premPastilla` | Pastilles sense cap de premuda (a la 0.2, triar la taula és el primer pas) i marcar-ne una sense disparar-la |
| `quiet()` | Si el sistema demana moviment reduït |

Davant de l'1 (u) i de l'11 (onze) s'apostrofa. Són els únics nombres de la caixa que es llegeixen
començant per vocal, i per això la gramàtica és al nucli: si fos a les frases, cada frase
necessitaria una versió per a cada cas.

---

## 6. Les tasques tancades

El motor és el de l'altra caixa (`js/tasca.js`): `Inici ● ○ ○ ○ ○ Final` i «Pas 2 de 5», un
sol pas a la vista, la retroacció sempre amb la mateixa forma i un final amb resum i codi.

| | Què es contesta | Primer error | Segon error |
|---|---|---|---|
| 0.2 | La fila de la taula | La pista diu si falla la taula o la fila | Es marca la fila bona |
| 0.3 | La fila on surt el resultat | La pista diu si falla la taula o la fila | Es marca la fila bona i s'omple el forat |
| 1.2 | El quadret on acaba el rectangle | Es marquen els dos números de la vora | Es dibuixa el rectangle bo |
| 2.2 | Un dels dos dibuixos | El dibuix tocat es queda amb el seu rètol, «4 · 2 = 8. No és un quadrat» | No hi arriba: el segon intent és l'altre |
| 3.2 | Els blocs, i «Comprova» | Surt la taula de les xifres | Es posen els blocs bons |
| 4.2 | El signe de l'operació que va primer | La pista depèn de si hi ha parèntesi | No hi arriba: el segon intent és l'altre |

Tres detalls que valen per a totes:

- **El rectangle girat és bo.** A la 1.2, 5 files de 2 per 2 · 5 és correcte; a la 0.2, la fila
  7 · 6 per 6 · 7 també, i a la 0.3, la fila 4 · 5 = 20 per … · 4 = 20. Tenen els mateixos quadrets, i la 1.3 ho ensenya.
- **La resposta no es veu mentre es fa.** A la 3.2 el nombre no surt fins que es comprova; a la
  2.2 els rètols no surten fins que es toca. Si no, n'hi hauria prou amb provar fins que
  coincidís.
- **Un pas ja contestat que es reprèn** diu «Aquest pas ja està fet» (`comu.ja_fet`) i deixa el
  botó «Següent pas» actiu.

Cada tasca tancada es dona d'alta al catàleg (`CE.registraCataleg`), i així `verifica.html`
posa nom al codi. Cada mòdul deixa també les seves dades a `CE.dades` (els casos, no l'estat),
perquè les proves comprovin que cap cas trenca les regles.

---

## 7. Afegir una eina o una subtasca

**Una subtasca nova dins d'una eina:**

1. Al marcatge, un `<div class="subtasca" data-sub="n">` al final de la secció, amb el número
   següent.
2. Al mòdul, la seva funció d'arrencada a `ARRENCA`. Ha de poder-se cridar dues vegades sense
   duplicar res.
3. A `dades/textos.js`, el grup `"t.n"` amb `nom` (el que surt a la barra), `titol`, `ajuda` i la
   resta, i la seva explicació a `TEXTOS_GUIA`.
4. Si és tancada: `CE.tasca({ tasca, sub, … })` i `CE.registraCataleg("t.n", …)`.

**Els prefixos dels identificadors, únics.** Cada subtasca fa servir un prefix de dues lletres
(`xa-`, `rb-`…). Si dues eines en comparteixen un, `$("#…")` troba el primer element i una eina
dibuixa dins de l'altra: la tasca 15 (unitat 4) escrivia a la taula de la tasca 0 perquè totes
dues feien servir `tt-` i `tf-`. Ara s'hi diuen `mf-` i `mg-`, i `comprova.py` falla si hi ha
cap identificador repetit (29/9/2026).

**El número de la tasca, fins al 63.** El codi de verificació (`js/codi.js`) té 4 bits per a la
tasca i 2 per al bloc de 16: fins al 63. Abans eren 4 bits i prou, i les tasques 16 i 17 donaven
el codi de la 15. Els codis de les tasques 0 a 15 no han canviat.

**Una eina nova:** un fitxer a `js/moduls/`, amb `CE.registra("id", inicia)`; la pestanya
`<button class="segment" data-tasca="5" data-unitats="2" data-mod="id" data-src="js/moduls/id.js">`
amb el número lliure següent (i `data-cal` si fa servir una altra eina), i la `<section id="mod-id">`.
No porta `<script>`: es carrega quan s'obre. `js/app.js` no es
toca. Si la unitat la fa servir, el número va a `tasques` de `dades/unitats.js`, i l'enllaç
`?task=n`, a la llista «Enllaços per a l'alumnat» de la portada (`index.html`), sota la seva
unitat i amb el nom de la pestanya. `comprova.py` falla si hi falta (29/9/2026: s'aturava a
la unitat 3 i ningú no ho veia).

**Després, sempre:** els tres tests de l'apartat següent. A `eines/prova_caixa.py` i a
`eines/auditoria.py` s'hi afegeixen els estats de l'eina nova: el que no es prova no se sap si
funciona.

---

## 8. Comprovacions

| Test | Què fa | Què necessita |
|---|---|---|
| `eines/comprova.py` | Les regles que es poden llegir als fitxers: estructura, frases, Lectura Fàcil, subtasques, «·», fins a 999 i decimals fins a 9,99, contrast de la paleta, `pi1-`, sal pròpia, identificadors sense repetir i cap camp repetit a `dades/unitats.js` | Només Python |
| `eines/prova_caixa.py` | La caixa, feta servir de debò: toca, s'equivoca, acaba totes les tasques tancades (33) i llegeix els codis a `verifica.html` | Playwright i Chromium |
| `eines/auditoria.py` | L'accessibilitat aplicada: contrast real, mida de cada botó i focus, en clar i en fosc, a 320 i a 1100 px | Playwright i Chromium |

Tots tres han de dir que està bé («Tot correcte.» o «0 problemes») abans de lliurar res. Com
instal·lar Playwright al Codespace és al [`README.md`](../README.md).
