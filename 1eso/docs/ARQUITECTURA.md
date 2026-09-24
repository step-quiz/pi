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
| `caixa-eines.html` | El marcatge de les cinc eines. Cap frase: només `data-text="1.2.titol"` |
| `verifica.html` | Llegeix els codis de verificació, un o molts alhora |
| `textos.html` | Totes les frases en una pàgina, per canviar-les i baixar el fitxer nou |
| `dades/textos.js` | Totes les frases (`window.TEXTOS`) i què fa cadascuna (`window.TEXTOS_GUIA`) |
| `css/app.css` | Els estils de la pantalla. Fa servir els colors de `css/tokens.css` |
| `js/nucli.js` | L'objecte `CE`: el poc que comparteixen tots els mòduls |
| `js/codi.js` | El codi de verificació (`K7Q-M2X-9RT`) |
| `js/tasca.js` | El motor de les tasques tancades |
| `js/quadricula.js` | El dibuix de tot el curs: quadrets, rectangles, la taula de quadrets, els blocs |
| `js/moduls/*.js` | Les cinc eines, una per fitxer |
| `js/app.js` | Les pestanyes i els enllaços `?task=n`. Va l'últim |

L'ordre de càrrega és aquest i no un altre, i el test el comprova:
`dades/textos.js` → `js/nucli.js` → `js/codi.js` → `js/tasca.js` → `js/quadricula.js` →
`js/moduls/*.js` → `js/app.js`.

**No s'han de tocar** `css/tokens.css`, `css/fitxa.css`, `fonts/Caveat.ttf` ni `eines/paper.py`
per res de la caixa. Formen l'empremta del PDF de la targeta (`pdf/empremtes.json`): si en canvia
un, el test diu que el PDF és vell i cal tornar-lo a fer amb WeasyPrint. Els estils nous de la
pantalla van a `css/app.css`.

---

## 3. Les cinc eines

| Tasca | Pestanya | Fitxer | Subtasques | S'obre amb |
|---|---|---|---|---|
| 0 | Taules | `taules.js` | 0.1 La taula · **0.2 Troba el resultat a la taula** | 7 · 8 = 56, el cas de la clau de la targeta |
| 1 | Rectangles | `rectangles.js` | 1.1 Fes un rectangle · **1.2 El rectangle d'una multiplicació** · 1.3 Gira el rectangle · 1.4 Parteix el rectangle | 3 · 4; 3 · 12 a la 1.4 |
| 2 | Quadrats | `quadrats.js` | 2.1 El quadrat d'un nombre · **2.2 Quin dibuix és?** · 2.3 El costat del quadrat | 3² = 9; 16 quadrets a la 2.3 |
| 3 | Nombres | `nombres.js` | 3.1 Centenes, desenes i unitats · **3.2 Fes el nombre** | 243, «dos-cents quaranta-tres» |
| 4 | Ordre | `ordre.js` | 4.1 Mira l'ordre · **4.2 Què es fa primer?** | 2 + 3 · 4 = 14 |

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
| `blocs` | Quadrats de 100, columnes de 10 i quadrets solts, a la mateixa escala |

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
| `CE.subDemanada(tasca)` | La subtasca que demana l'enllaç (`?task=1.3`), només si és d'aquesta tasca. La pestanya Taules, que també surt, s'obre per la 0.1 |
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
| 1.2 | El quadret on acaba el rectangle | Es marquen els dos números de la vora | Es dibuixa el rectangle bo |
| 2.2 | Un dels dos dibuixos | El dibuix tocat es queda amb el seu rètol, «4 · 2 = 8. No és un quadrat» | No hi arriba: el segon intent és l'altre |
| 3.2 | Els blocs, i «Comprova» | Surt la taula de les xifres | Es posen els blocs bons |
| 4.2 | El signe de l'operació que va primer | La pista depèn de si hi ha parèntesi | No hi arriba: el segon intent és l'altre |

Tres detalls que valen per a totes:

- **El rectangle girat és bo.** A la 1.2, 5 files de 2 per 2 · 5 és correcte; a la 0.2, la fila
  7 · 6 per 6 · 7 també. Tenen els mateixos quadrets, i la 1.3 ho ensenya.
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

**Una eina nova:** un fitxer a `js/moduls/`, amb `CE.registra("id", inicia)`; el seu `<script>` a
`caixa-eines.html`, abans de `js/app.js`; la pestanya `<button class="segment" data-tasca="5"
data-mod="id">` amb el número lliure següent, i la `<section id="mod-id">`. `js/app.js` no es
toca. Si la unitat la fa servir, el número va a `tasques` de `dades/unitats.js`.

**Després, sempre:** els tres tests de l'apartat següent. A `eines/prova_caixa.py` i a
`eines/auditoria.py` s'hi afegeixen els estats de l'eina nova: el que no es prova no se sap si
funciona.

---

## 8. Comprovacions

| Test | Què fa | Què necessita |
|---|---|---|
| `eines/comprova.py` | Les regles que es poden llegir als fitxers: estructura, frases, Lectura Fàcil, subtasques, «·», fins a 999, contrast de la paleta, `pi1-`, sal pròpia | Només Python |
| `eines/prova_caixa.py` | La caixa, feta servir de debò: toca, s'equivoca, acaba les cinc tasques i llegeix els codis a `verifica.html` | Playwright i Chromium |
| `eines/auditoria.py` | L'accessibilitat aplicada: contrast real, mida de cada botó i focus, en clar i en fosc, a 320 i a 1100 px | Playwright i Chromium |

Tots tres han de dir que està bé («Tot correcte.» o «0 problemes») abans de lliurar res. Com
instal·lar Playwright al Codespace és al [`README.md`](../README.md).
