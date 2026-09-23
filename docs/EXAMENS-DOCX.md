# Exàmens en DOCX

Com es fa l'examen adaptat de cada unitat en Word. El model és el de la UD1, tal com el
va revisar el docent a Google Docs el 23/9/2026: tot el que diu aquest document surt
d'aquella revisió, i on una regla és una decisió seva, s'hi diu.

Aquest document no substitueix `CRITERIS-DISSENY.md` ni l'apartat 8 de
`MAPA-ADAPTACIO.md`: els aplica a l'examen.

---

## 1. Els fitxers

| Fitxer | Què hi ha |
|---|---|
| `generadors/examens/nucli.js` | La maquinària comuna: pàgina, lletra, grisos, peces, dibuixos i comprovacions |
| `generadors/examens/ud1.js` | El contingut de la UD1. És el model per a les altres unitats |
| `generadors/examens-privat.json` | El curs i l'adaptació. **No es puja mai**: el `.gitignore` ja el deixa fora |
| `docx/` | On surten els dos DOCX. Tampoc es puja, perquè porten les dades privades |

Per fer l'examen d'una unitat, des de l'arrel del repositori, al Codespace:

```bash
npm install --prefix /tmp/eines docx@9.6.1 sharp@0.34.5
NODE_PATH=/tmp/eines/node_modules node generadors/examens/ud1.js
```

Les llibreries s'instal·len a `/tmp`, fora del repositori, perquè no hi entri cap
`node_modules/`. A l'entorn de Claude ja hi són, i n'hi ha prou amb la segona línia sense
`NODE_PATH`. Si es passa una carpeta com a argument, els DOCX surten allà.

---

## 2. D'on surt el contingut

- **Els ítems, de la fitxa de la unitat i del seu solucionari**, que estan validats.
  L'examen no inventa si no cal.
- **Quatre apartats per exercici**: a) resolt, i b), c) i d) per fer. És decisió del
  docent. Si la fitxa en té menys, se n'afegeix un de nou amb la mateixa idea, i al
  solucionari porta la marca «nou» perquè el docent el revisi.
- **Cap pregunta de justificació oberta** (mapa, apartat 8). Si la fitxa en té una,
  a l'examen no hi entra.
- **Cada xifra, comprovada amb la calculadora** abans d'escriure-la, al solucionari i a
  l'alumnat.

---

## 3. L'estructura

- **Pàgina 1**: a dalt, «Matemàtiques Aplicades [curs] · Unitat N»; a sota, Nom i Data;
  l'avís de la calculadora; l'exercici 1. El curs surt del fitxer privat.
- **Ni «adaptat» ni títol.** L'examen té l'aspecte d'un examen com els altres.
- **Un sol avís**, el de la calculadora. El de «l'apartat a) ja està fet» no hi va: el
  model en lletra manuscrita ja ho diu tot sol.
- **Un exercici per pàgina.** Dos de curts poden compartir-la si hi caben sencers (a la
  UD1, el 6 i el 7): `exercici(7, …, { mateixaPagina: true }, …)`.
- **Peu**: «pàgina N de M».
- **El solucionari**, en un document a part.

---

## 4. El format

| Element | Lletra | Mida | Negreta |
|---|---|---|---|
| Consigna | Verdana | 15,5 | no |
| Avís de la calculadora | Verdana | 15,5 | no |
| Etiqueta a), b)… dins d'una taula o d'una caixa | Verdana | 15 o 14 | no |
| Etiqueta a), b)… d'un apartat solt (les rectes) | Verdana | 14 | sí |
| Dada de l'enunciat | Verdana | 15 (una arrel sola, 16) | sí, sobre gris F2F2F2 |
| Resposta de l'apartat resolt | Caveat | 20 | no, en gris 3A3A3A |
| Capçalera de columna | Verdana | 11 | sí, gris 333333 sobre E4E4E4 |
| Nombres per marcar | Verdana | 19 | sí |
| Frase d'una situació | Verdana | 13 | no |
| Xifra d'una situació i opcions de marcar | Verdana | 17 | sí |
| Frase de context sota la consigna | Verdana | 13 | no, en gris 5E5E5E |

- **La negreta només marca les dades** (i el número de l'exercici i les capçaleres). Les
  consignes i les etiquetes van en rodona.
- **La lletra manuscrita és Caveat**, que no té α β θ π ← → ∆ ∑ √ ∞ ⋅. Si el text en porta
  un, va sencer en **Nova Mono**, com va fer el docent amb «√7 = 2,6457513…». El nucli
  tria la lletra sol: `ms("…")`.
- **L'opció triada a l'apartat resolt** porta fons gris D9D9D9 i la vora fosca.
- **Caselles per escriure d'1,5 cm** d'alçada.
- **Blanc i negre estricte**, com a les fitxes.

---

## 5. El llenguatge

Els canvis que el docent va fer a les frases de la UD1 segueixen un patró, i valen per a
tots els exàmens:

| Principi | Abans | Després |
|---|---|---|
| El terme matemàtic correcte | dos nombres sencers | dos nombres enters |
| Un sol verb per marcar | Encercla el nombre… | Marca el nombre… |
| Sense pronoms febles ni construccions indirectes | Marca amb quants decimals ho escriuries en cada situació. | Marca quants decimals faries servir en cada cas. |
| Verbs literals | quant fa la diagonal | quant mesura la diagonal |
| La restricció, dita en clar | només pots comprar coses senceres | només pots comprar quantitats enteres, sense decimals |
| Les unitats, sempre | 2,3 | 2,3 pots |
| Frases que valguin per a tots els apartats | A totes dues… | En tots els casos… |

L'última és la que costa més de veure: en passar de dos apartats a quatre, «totes
dues» i «només fas el b)» van deixar de ser veritat.

El nucli avisa si troba «sencer», «Encercla», «quant fa», «ho …ries» o «només fas», i
s'atura si troba «adaptat».

---

## 6. La tècnica: el docent edita a Google Docs

L'examen es genera en DOCX, però qui el retoca ho fa a Google Docs, i Google Docs no
llegeix tot el que Word llegeix. Per això:

- **Les tres lletres hi són**: Verdana, Caveat i Nova Mono.
- **No hi ha interlineat exacte.** Google Docs el converteix en un múltiple i els espais
  es disparen. L'espai vertical es fa amb `espai(punts)`: un paràgraf buit d'1 pt amb
  «espai abans».
- **No hi ha alçades de fila exactes.** Per això el quadrat del número és una taula petita
  dins de la cel·la, i no s'estira quan la consigna fa dues línies.
- **Els dibuixos van en SVG i en PNG a 300 ppp.** Word fa servir l'SVG; Google Docs, el
  PNG. El PNG té el fons transparent: un fons blanc, sobre una cel·la grisa, es veu com un
  quadrat.
- **Els estils de Word desapareixen.** Per canviar tota la lletra manuscrita alhora a
  Google Docs: clic dret sobre un tros → «Selecciona tot el text coincident».
- **Sempre hi ha un `espai()` entre dues taules**, perquè Word no les fongui.
- **Les caixes són vores de taula**, no formes: les cantonades són rectes, però tot es
  pot editar.

Si l'examen s'obre amb Word i l'ordinador no té Caveat ni Nova Mono, Word en posa unes
altres. Totes dues són gratuïtes a Google Fonts.

---

## 7. Com es fa l'examen d'una unitat nova

1. **Llegir** aquest document, `CRITERIS-DISSENY.md`, l'apartat 8 de
   `MAPA-ADAPTACIO.md`, la fitxa de la unitat i el seu solucionari.
2. **Triar els apartats**: per a cada exercici de la fitxa, l'a) resolt i tres més.
   Anotar quins són nous.
3. **Copiar `ud1.js` a `udN.js`** i canviar-hi el contingut. Les peces que el nucli no té
   es fan a `udN.js` amb les eines del nucli (`taula`, `cela`, `vora`, `G`, `MIDA`, `AIRE`,
   `imatge`, `registra`, `anota`). Si una peça serveix per a més d'una unitat, passa al
   nucli. A la UD2 caldran la cadena de baules, la barra de preu, la doble recta, el
   tiquet, les dues maneres de pagar una al costat de l'altra i les frases model.
   - Una peça és una funció que torna una altra funció (`() => taula(…)`): el document
     es munta quan els PNG ja són fets.
   - Un dibuix nou es registra en declarar la peça (`registra("nom", svg)`) i es posa
     dins de la funció (`imatge("nom", ampleCm, altCm, "text alternatiu")`).
   - Cada peça que porta un apartat crida `anota("b)")`: així el nucli comprova que hi
     hagi a), b), c) i d).
4. **Executar** i llegir els avisos.
5. **Mirar-lo**: passar els DOCX a PDF amb LibreOffice i revisar cada pàgina. Cada
   exercici, sencer a la seva pàgina; cap taula partida; cap apartat sense opcions.
6. **Repassar el text**: cada xifra i cada frase triada de la fitxa hi és i està bé, i el
   solucionari quadra amb l'alumnat.
7. **Passar `python3 eines/comprova.py`.**
8. **Lliurar** els dos DOCX i dir quins apartats són nous.

---

## 8. Comprovacions

**Les fa el nucli**, cada cop que genera:
- blanc i negre: cap color amb R, G i B diferents, ni a l'XML, ni als SVG, ni als PNG,
  píxel a píxel;
- que cada exercici tingui a), b), c) i d);
- el llenguatge de l'apartat 5, i «adaptat».

**Es fan a mà**: el PDF pàgina a pàgina, el text contra la fitxa i `comprova.py`.

Per previsualitzar amb LibreOffice cal tenir Caveat i Nova Mono instal·lades: si no hi
són, se'n posa unes altres i la previsualització enganya. Es copien a `~/.fonts` i
`fc-cache -f`. Un DOCX exportat de Google Docs les porta a dins, a `word/fonts/`.

---

## 9. Errors que ja s'han vist

- Text a 12 pt i apartats resolts en negreta en lloc de lletra manuscrita.
- Un apartat sense opcions per marcar.
- Una taula partida entre dues pàgines, amb l'apartat que més diu sol a l'última.
- Nombres i caixes fets com a imatges: queden bonics, però no es poden editar.
- Interlineat exacte: a Google Docs els espais es disparen.
- Oblidar que Caveat no té √.
- Frases que deixen de ser veritat en afegir apartats.
- El curs o el diagnòstic dins d'un fitxer del repositori: `comprova.py` s'atura, i
  quedaria publicat a la web.

---

## 10. Les dades privades

`generadors/examens-privat.json`, només a l'ordinador de qui genera l'examen:

```json
{
  "curs": "…",
  "adaptacio": "…"
}
```

Sense aquest fitxer, l'examen surt en versió anònima: la capçalera sense curs i, al
solucionari, «alumnat amb dificultats de tipus cognitiu».
