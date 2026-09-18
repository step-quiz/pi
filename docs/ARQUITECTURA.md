# Arquitectura

Com està muntat el projecte i com ampliar-lo sense trencar res.

---

## 1. Les decisions de partida

**Estàtic i sense pas de compilació.** Igual que la resta del material del departament.
S'ha de poder obrir des d'un llapis de memòria, sense servidor i sense connexió.

**Scripts clàssics, no mòduls ES.** Els mòduls ES (`type="module"`) els bloqueja el
navegador per CORS quan s'obre un fitxer amb doble clic (`file://`). Per això: scripts
clàssics, un sol nom global (`CE`) i cada mòdul dins d'una funció que s'executa tota
sola. L'encapsulació la fa l'embolcall, no el sistema de mòduls.

**Cap dependència externa.** Ni CDN, ni fonts remotes, ni biblioteques. El filtre del
centre bloqueja recursos externs, i a més volem que funcioni sense xarxa.

**Dues paletes, mai barrejades.** El paper és blanc i negre; la pantalla té color.
Totes dues viuen a `css/tokens.css`, en seccions separades i documentades.

**Cap `@import` als fulls d'estil.** Encadenar CSS obliga el navegador a baixar-se un
fitxer, llegir-lo, descobrir l'import i baixar-se el segon: dues anades i tornades en
sèrie bloquejant el pintat. `tokens.css` s'enllaça des de l'HTML, abans del full que el
fa servir. El test ho comprova.

---

## 2. Els fitxers

```
├── _headers  robots.txt  404.html  favicon.svg
├── index.html              portada
├── fitxes.html             índex detallat de les set unitats
├── caixa-eines.html        l'aplicació: només marcatge
│
├── css/
│   ├── tokens.css          variables: paleta de paper, paleta de pantalla, mode fosc
│   ├── fitxa.css           les fitxes imprimibles          (importa tokens)
│   ├── app.css             la caixa d'eines                (importa tokens)
│   └── lloc.css            index.html i fitxes.html        (importa tokens)
│
├── js/
│   ├── nucli.js            l'objecte global CE i el registre de mòduls
│   ├── app.js              navegació de la caixa d'eines
│   ├── lloc.js             construeix els índexs a partir de les dades
│   └── moduls/             un fitxer per mòdul, vuit en total
│
├── dades/
│   └── unitats.js          font única: les set unitats amb tota la metadada
│
├── fitxes/                 ud1.html … ud7.html
├── generadors/             els scripts Python que dibuixen els SVG
├── eines/comprova.py       el test del projecte
├── generadors/             els scripts Python que dibuixen els SVG
└── docs/                   la documentació
```

**Qui depèn de qui.** Les fletxes van només en una direcció:

```
tokens.css ← s'enllaça des de l'HTML, ABANS de fitxa.css / app.css / lloc.css
nucli.js   ← js/moduls/*.js  ← app.js
unitats.js ← lloc.js
```

`app.js` no sap res del contingut dels mòduls: només els identificadors, que llegeix de
l'atribut `data-mod` del marcatge. `lloc.js` no sap res de les unitats: les llegeix de
`dades/unitats.js`.

---

## 3. El nucli: `CE`

`js/nucli.js` defineix l'únic objecte global i s'ha de carregar primer.

| | |
|---|---|
| `$`, `$$` | seleccionar un node o una llista |
| `num(x, dec)` | format català, coma decimal, sense zeros finals inútils |
| `fix(x, dec)` | com `num()` però conservant tots els decimals |
| `euros(x)` | `fix(x, 2) + " €"` |
| `el(nom, atributs, text)` | crea un node SVG |
| `icona(id, mida)` | instancia un pictograma declarat als `<symbol>` de la pàgina |
| `pastilles(cont, llista, aoTriar, inicial)` | fila de botons amb selecció exclusiva |
| `memoria` | `localStorage` protegit, amb objecte en memòria si no hi és |
| `registra(id, inicia)` | dona d'alta un mòdul |

**Detall que sembla trivial i no ho és.** `num()` només retalla els zeros que hi ha
*després* de la coma. Si els retallés sempre, «20» es convertiria en «2» i les marques
dels eixos mentirien. Va passar; per això hi ha el comentari al codi.

**Colors dins dels SVG.** Es passen com `style="fill:var(--blau)"` i no com atribut
`fill`. Així el mode fosc funciona sense duplicar codi.

---

## 4. Afegir un mòdul a la caixa d'eines

Tres passos i no cal tocar `app.js`.

**1.** Crea `js/moduls/<nom>.js`:

```js
(function () {
  "use strict";
  const { $, $$, num, euros, el, pastilles } = CE;

  function inicia() {
    if ($("#xxx-pastilles").children.length) return;   // idempotent: es pot cridar dos cops
    // …
  }

  CE.registra("xxx", inicia);
})();
```

**2.** A `caixa-eines.html`, el botó i la secció. El botó porta el següent número de
tasca lliure:

```html
<button class="segment" role="tab" data-tasca="8" data-mod="xxx" aria-selected="false">Nom</button>
...
<section id="mod-xxx" class="modul" hidden> … </section>
```

**3.** El `<script src>`, **abans** de `js/app.js`, que ha d'anar sempre l'últim.

**La funció d'arrencada s'ha de poder cridar diverses vegades.** `app.js` la crida cada
vegada que s'obre la pestanya. Per això tots els mòduls comencen comprovant si ja estan
muntats.

**Convenció que fan servir tots.** El mòdul **s'obre ja resolt** amb un exemple marcat
amb `<span class="marca">Exemple</span>`, i un botó el buida per al cas de l'alumnat.
És el mateix criteri que «el primer apartat ja resolt» de les fitxes.

**Enllaços filtrats per a l'alumnat.** `caixa-eines.html?task=n` mostra només la tasca 0
(la Calculadora), sempre la primera, i la tasca `n`, que és la que s'obre. Sense `?task`
es veu la caixa sencera; amb `?task=0` o un número que no existeix, només la Calculadora.
En mode filtrat no es fa servir el mòdul desat a `localStorage` i s'amaga l'enllaç a
l'inici. Els números viuen a l'atribut `data-tasca` i ja són en enllaços enviats: **no es
renumeren mai**, ni quan es treu un mòdul. El test comprova que no se'n repeteixi cap i que
la tasca 0 vagi la primera.

---

## 3b. Les frases: `dades/textos.js`

**Cap frase que llegeixi l'alumnat viu al codi ni al marcatge.** Totes són a
`dades/textos.js`, en un sol objecte. El marcatge hi apunta i el codi les demana:

```html
<h2 data-text="1.2.titol"></h2>
```
```js
avis.innerHTML = txt("1.2.encert", { nom: "√5", baix: 2, alt: 3 });
```

`CE.omplirTextos(arrel)` omple tots els `[data-text]` d'un tros de pàgina, i es
crida un cop quan arrenca el mòdul.

**Dues convencions** que fan que les frases es puguin editar sense saber
programar: `*entre asteriscs*` surt en negreta, i `{això}` és un forat que
s'omple amb una dada. Si una clau no existeix, `txt()` retorna `[1.2.titol]`, que
canta prou per adonar-se'n de seguida sense petar.

**`textos.html`** és una pàgina per al professorat: ensenya cada frase en un camp
amb una nota de on surt, avisa en vermell si hi falta un forat, i dona el fitxer
ja muntat per substituir `dades/textos.js`. La capçalera i el bloc `TEXTOS_GUIA`
del fitxer es tornen a escriure tal com són: la pàgina només canvia les frases.

**On no van les frases.** Els `aria-label` es queden al marcatge: són text
d'accessibilitat, no el que es llegeix a la pantalla. I les dades que mouen un
càlcul —els preus del material de l'exercici 1.4, per exemple— es queden al codi;
de `textos.js` en surt només el nom, de manera que canviar-ne el text no pot fer
que l'etiqueta digui un preu que no és.

**El test** comprova que tota clau que es demana existeixi, que cada frase tingui
la seva línia a `TEXTOS_GUIA` i que no n'hi hagi cap sense fer servir. Compte: hi
ha claus que es munten (`"1.3." + quina`, o el `.nom` que llegeix el nucli), i la
comprovació les té en compte; si no, delataria vint frases que sí que s'usen.

## 4a. Subtasques: una tasca partida en 1.1, 1.2, 1.3…

Un mòdul pot tenir diversos exercicis dins. La navegació és genèrica i està al
nucli, de manera que qualsevol mòdul ho pot fer sense codi propi.

**Marcatge.** Dins de la `<section>`, una barra i els panells:

```html
<div class="subbarra">
  <button class="btn tenyit mini sub-enrere" aria-label="Exercici anterior">‹</button>
  <span class="sub-rotul"></span>
  <button class="btn mini sub-avant" aria-label="Exercici següent">›</button>
</div>
<div class="subtasca" data-sub="1" data-nom="Nom curt">…</div>
<div class="subtasca" data-sub="2" data-nom="Nom curt" hidden>…</div>
```

**Al mòdul**, una sola crida. La funció d'arrencada de cada panell es crida el
primer cop que s'ensenya, no abans:

```js
const ARRENCA = { 1: iniciaA, 2: iniciaB, 3: iniciaC };
const jaFetes = new Set();
let subActual = null;

function inicia() {
  const subs = CE.subtasques($("#mod-xxx"), n => {
    subActual = n;
    if (!jaFetes.has(n)) { ARRENCA[n](); jaFetes.add(n); }
  });
  subs.mostra(subActual || CE.subDemanada || 1);
}
```

`subActual` fa que, en tornar a la pestanya, es reprengui on s'estava.

**Enllaços.** `?task=1` obre la tasca 1 per l'exercici 1; **`?task=1.3` obre
directament el tercer**. És el que permet enviar un exercici concret i no la
tasca sencera. Si el número no existeix o el format no és `n` ni `n.m`, es cau a
la tasca 0, com sempre.

**El número de subtasca no es renumera mai**, per la mateixa raó que el de tasca:
els enllaços viuen en fulls fotocopiats. Si una subtasca es retira, el seu número
es deixa buit. El test comprova que vagin seguides des de l'1 i que cadascuna
tingui `data-nom`.

## 4c. El valor posicional i el sistema mètric (1.5 i 1.6)

Aquests dos exercicis són **el mateix objecte vist dues vegades**, i per això van
seguits: canviar d'unitat no canvia la llargada, només mou la coma dins de la
taula de columnes.

- **1.5** ensenya la taula (centenes → mil·lèsimes) amb una xifra per columna.
  Tocar-ne una diu què val, i a sota hi ha la descomposició: `3 + 0,4 + 0,07`.
  Un nombre decimal és una suma, i aquí es veu.
- **1.6** posa la mateixa mesura a l'escala `km hm dam m dm cm mm`. Es toca un
  graó i la mesura es reescriu; es diu quants graons s'han mogut i cap a on va
  la coma.

**Res de tot això fa servir aritmètica de coma flotant.** Les mesures es guarden
com a **xifres + exponent** (`{ d: "347", e: -2 }` és 3,47) i la funció
`decimal(xifres, exp)` escriu el resultat movent la coma sobre la cadena. Dos
motius: és exactament l'operació que s'està ensenyant, i és exacta. Amb càlcul
normal, `3,47 × 10` dona `34.699999999999996` i la pantalla mentiria.

Dos casos que s'han hagut d'arreglar i que convé no desfer:

- `decimal("0", exp)` retornava `"00"` per a l'exponent 1, i tocant el zero de
  105,3 deia «val 00». El zero val zero a qualsevol columna.
- A 1.4, el preu del material no surt de `textos.js` sinó del codi, perquè
  canviar-ne el text no pugui fer que l'etiqueta digui un preu que no és.

Les 28 conversions possibles (4 mesures × 7 unitats) es comproven contra el
càlcul normal i coincideixen totes.

## 4b. El mòdul de la calculadora: un pas, una pantalla

Aquest mòdul té una restricció que els altres no tenen: **un pas ha de cabre sencer
a la finestra, sense fer scroll**. El bucle és «prem la tecla a la calculadora de
veritat i avança aquí», i si per veure el teclat i el botó cal moure la pàgina, es
perd el lligam entre les dues coses.

**Dues columnes.** `#mod-calc` és una graella: el triador de casos va en un
`<aside class="triador">` enganxat a l'esquerra i el pas a la dreta. Amb el triador
a sobre, el pas començava a 190 px de l'inici i no hi cabia. Per sota de 46 rem
les dues columnes s'apilen i les pastilles tornen a fila.

**Ordre dins del pas:** la frase que diu el bucle, la pantalla de la calculadora,
els botons i, al final, el mapa del teclat, que serveix per **situar** la tecla a
l'aparell. El pas fa uns 440 px.

**Dues coses criden l'atenció sense molestar.** La tecla del pas batega
(`@keyframes bategar`) i **es pot tocar per avançar**, igual que el botó: així el
gest de «prem aquesta tecla» i el d'avançar són el mateix. El botó fa una sacsejada
curta cada 3,4 s amb un anell que s'esvaeix (`@keyframes crida`). Totes dues
s'aturen amb `prefers-reduced-motion`.

**Mides que no s'han de tocar sense demanar-ho.** La pantalla de la calculadora i
les tecles d'operació tenen mides fixades pel docent: l'entrada un 30 % més gran que
la base, el rètol del resultat un 10 % més baix i les tecles `× ÷ + − Ans =` un 30 %
més grans. El cos de la pantalla és gris fosc, no negre.

**Què no hi ha, i és a posta.** No hi ha cap rètol que expliqui pas per pas què vol
dir la tecla: hi era i es va treure perquè afegia text a una pantalla que n'havia de
tenir poc. Qui guia és la tecla que batega, la frase del bucle i el comptador
«Tecla n de m». L'única nota que queda és la de la coma decimal, i viu a la columna
del triador, on no competeix amb el pas.

## 5. Afegir una unitat

**1.** Una entrada a `dades/unitats.js`. Els índexs es refan sols.
**2.** La fitxa a `fitxes/udN.html`, amb `<link rel="stylesheet" href="../css/fitxa.css">`.
**3.** Si porta dibuixos nous, un generador a `generadors/`.

L'esquelet d'una fitxa:

```html
<div class="full">
  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>material</b></div>
  <h1>Un títol que és una pregunta</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">…<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>
  <div class="figura"> <!-- l'SVG --> </div>
  <p>La frase que anomena la cosa, SEMPRE després del dibuix.</p>
  <div class="pag">Unitat N · pàgina 1</div>
</div>
```

L'ordre importa: pregunta → dibuix → nom de la cosa. Si la frase va abans del dibuix,
la pregunta d'obertura queda anul·lada. Va passar a tres fitxes i es va corregir.

---

## 6. Els gràfics

**No es dibuixen a mà.** Els SVG de les fitxes els generen els scripts de `generadors/`,
perquè els vèrtexs, les barres, els punts i les marques dels eixos caiguin exactament on
toca. Cada script **imprimeix les seves pròpies comprovacions numèriques** en executar-se.

| Script | Què dibuixa |
|---|---|
| `gen_grafics.py` | les paràboles de la U5 |
| `gen_grafics2.py` | diagrames de punts, barres i arbres de la U6 i la U7 |
| `gen_grafics3.py` | barres de percentatge de la U2 i model d'àrea de la U6 |
| `gen_grafics4.py` | doble recta de la U2, repartiment de la U6, barra de la U7 |
| `gen_pdf.py` | els catorze PDF, partint cada fitxa en alumnat i solucionari |

## 6b. Els PDF i l'alçada de les pàgines

Cada bloc `.full` de l'alumnat ha de ser **exactament una pàgina A4**. Això mai s'havia
verificat amb un motor de paginació, i quan es va fer resulta que set pàgines vessaven,
entre mig centímetre i vuit.

`eines/mesura.py` renderitza cada pàgina en un full molt alt, mira on acaba el contingut
i ho compara amb els 27,1 cm útils d'un A4. `generadors/gen_pdf.py` falla si el PDF de
l'alumnat no té tantes pàgines com blocs té la fitxa.

L'ajust es va fer al `@media print` de `fitxa.css`: dibuixos més petits i ritme vertical
més estret. **El cos de 14 pt no s'hi toca.** Si una pàgina no cap, s'arregla la fitxa.

Escriuen un `.json` amb els SVG, que s'incrusten a les fitxes substituint marcadors
`§NOM§`. Els fitxers publicats ja tenen les substitucions fetes; els marcadors que hi
queden són comentaris HTML de traça (`<!--§obertura p.1§-->`) que serveixen per trobar
i desfer una inserció.

---

## 7. Comprovacions

`python3 eines/comprova.py` verifica, per a les set fitxes: cap valor cromàtic, HTML ben
tancat, numeració de pàgines seguida, rètol de material i obertura presents. I per a
l'app: que els identificadors del marcatge coincideixin amb els mòduls registrats i que
no hi hagi recursos remots.

Convé passar-lo abans de publicar res.
