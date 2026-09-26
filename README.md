# Material adaptat de matemàtiques

Material de matemàtiques per a **alumnat amb dificultats de tipus cognitiu**: fitxes
imprimibles, una caixa d'eines digital, exàmens adaptats en Word i la documentació que
explica per què tot és com és.

Cada curs té la seva carpeta, perquè els recursos d'un curs i els de l'altre no són els
mateixos. El que serveix per a tots dos és a `comu/`.

---

## L'estructura

| Carpeta o fitxer | Què hi ha |
|---|---|
| `4eso/` | Tot el material de Matemàtiques Aplicades: les set fitxes, la caixa d'eines, els PDF, els exàmens, la documentació, els generadors i el test. Vegeu [`4eso/README.md`](4eso/README.md) |
| `1eso/` | Tot el material de Matemàtiques: les targetes de consulta, les fitxes, la caixa d'eines i el test. Vegeu [`1eso/README.md`](1eso/README.md) |
| `comu/` | El que comparteixen els dos materials: el motor dels exàmens DOCX i la documentació general. Vegeu [`comu/README.md`](comu/README.md) |
| `index.html` | La porta d'entrada: deixa triar entre `4eso/` i `1eso/` |
| `404.html` | La pàgina d'adreça equivocada. Les adreces d'abans de la reorganització porten a `4eso/`, perquè és on vivien |
| `_headers`, `robots.txt`, `favicon.svg` | El desplegament a Cloudflare Pages: vegeu [`comu/docs/DESPLEGAMENT.md`](comu/docs/DESPLEGAMENT.md) |
| `LICENSE`, `LLICENCIA.md` | Les llicències |
| `_uploads/`, `.github/` | La pujada de fitxers en zip des del web de GitHub |

Dins de `4eso/`, l'estructura és la de sempre: `fitxes/`, `css/`, `js/`, `dades/`, `pdf/`,
`docs/`, `eines/` i `generadors/`. Les ordres de la seva documentació s'executen des de
dins: `cd 4eso/`.

---

## Com s'obre

Doble clic a `index.html`: deixa triar el material (Matemàtiques o Matemàtiques Aplicades) i
porta a la seva portada. No cal servidor ni instal·lar res. Cada portada, al seu torn, deixa
triar entre les fitxes i la caixa d'eines: vegeu els `README.md` de `4eso/` i `1eso/`.

## On es publica

GitHub → Cloudflare Pages → `pi.step-quiz.net`, amb tots els camps del formulari buits: es
publica tot el repositori. La caixa d'eines de `4eso/` és a
`https://pi.step-quiz.net/4eso/caixa-eines`, i la de `1eso/` a
`https://pi.step-quiz.net/1eso/caixa-eines`.

**Els enllaços que ja s'han enviat a l'alumnat continuen funcionant.** Una adreça d'abans,
com `https://pi.step-quiz.net/caixa-eines?task=2`, porta sola a la mateixa pàgina dins de
`4eso/`, amb el `?task` inclòs. Ho fa la `404.html` de l'arrel.

---

## Els exàmens en DOCX

Cada unitat pot tenir un examen adaptat en Word: un document per a l'alumnat i un
solucionari per al professorat. Es fan amb un programa perquè una IA no escriu un DOCX a
mà: sempre escriu un programa que el fabrica. El programa té dues peces, i les regles són
en un document a part:

| Fitxer | Què hi ha |
|---|---|
| `comu/examens/nucli.js` | El motor: la pàgina, les lletres, els grisos, les peces de l'examen, els dibuixos i les comprovacions. És el mateix per a tots els cursos |
| `4eso/generadors/examens/ud1.js` | El contingut de l'examen de la UD1. Cada unitat té el seu fitxer: `ud2.js`, `ud3.js`… |
| `comu/docs/EXAMENS-DOCX.md` | Les regles: com ha de ser l'examen i per què, i el procediment pas a pas |
| `4eso/generadors/examens-privat.json` | El curs i l'adaptació que surten a l'examen imprès. Només a l'ordinador de qui genera l'examen: no es puja mai |

Ara hi ha l'examen de la **UD1**. Les unitats 2 a 7 encara no en tenen.

### Fer l'examen d'una unitat nova amb una IA

És la manera recomanada: no cal instal·lar res.

1. Baixa el repositori en zip: a GitHub, «Code» → «Download ZIP».
2. Obre una conversa nova i adjunta-hi dos fitxers: el zip del repositori i l'examen de la
   UD1 tal com l'has deixat a Google Docs, baixat en DOCX («Fitxer» → «Baixa» →
   «Microsoft Word»). És el model, i porta a dins les fonts Caveat i Nova Mono.
3. Enganxa-hi aquesta instrucció. Canvia `N` pel número de la unitat i omple les dues
   dades privades, que no són en cap fitxer del repositori:

   ```
   Fes l'examen adaptat de la UDN en DOCX (alumnat i solucionari).

   T'adjunto el repositori i l'examen de la UD1 exportat de Google Docs. És el model,
   i porta les fonts Caveat i Nova Mono a word/fonts/.

   1. Llegeix comu/docs/EXAMENS-DOCX.md i segueix-lo pas a pas.
   2. El contingut surt de 4eso/fitxes/udN.html i del seu solucionari. Quatre apartats
      per exercici: a) resolt, i b), c) i d). Al solucionari, marca «nou» els que no
      siguin a la fitxa.
   3. Fes 4eso/generadors/examens/udN.js a partir de ud1.js, amb el motor comú
      comu/examens/nucli.js. Si toques el motor, ud1.js ha de continuar sortint igual.
   4. Les dades privades van només a 4eso/generadors/examens-privat.json, mai en cap
      altre fitxer. Curs: «…». Adaptació: «…».
   5. Passa els DOCX a PDF, mira cada pàgina i passa python3 4eso/eines/comprova.py.
   6. Lliura'm els dos DOCX, la llista d'apartats nous i un zip per pujar a _uploads/
      amb els fitxers nous o canviats, amb els camins des de l'arrel del repositori.
   ```

4. Revisa els dos DOCX a Google Docs.
5. Puja a la carpeta `_uploads/` el zip que et doni la IA, des del web de GitHub: «Add
   file» → «Upload files» → «Commit changes». En un minut, els fitxers queden al seu lloc,
   i la unitat nova ja té el seu `udN.js` per a la pròxima vegada.

### Tornar a fer un examen que ja existeix

Si la unitat ja té el seu `udN.js` (per exemple, per canviar-hi un número), també ho pot
fer una IA: adjunta el zip del repositori i demana-li «Genera l'examen de la UDN amb
4eso/generadors/examens/udN.js», amb les dues dades privades.

També es pot fer al Codespace, des de l'arrel del repositori:

```bash
npm install --prefix /tmp/eines docx@9.6.1 sharp@0.34.5
NODE_PATH=/tmp/eines/node_modules node 4eso/generadors/examens/ud1.js
```

La primera línia instal·la les dues llibreries fora del repositori, i només cal el primer
cop de cada Codespace. La segona fa els dos DOCX a `4eso/docx/`: clic dret → «Download».
Per posar-hi el curs i l'adaptació, abans cal crear `4eso/generadors/examens-privat.json`
(vegeu l'apartat 10 de `comu/docs/EXAMENS-DOCX.md`); sense aquest fitxer, l'examen surt
en versió anònima.

---

## Comprovacions

```bash
python3 4eso/eines/comprova.py
python3 1eso/eines/comprova.py
```

Cada una ha de dir «Tot correcte.». Comproven les fitxes, la caixa d'eines i el
desplegament, i que cap fitxer del repositori anomeni el curs, el tipus d'aula o un
diagnòstic. Els noms de carpeta `4eso/` i `1eso/` en són l'única excepció: fan visible el
curs a les adreces, i és una decisió presa.

---

<!-- atribucio-centre:inici -->

---

Material desenvolupat per **David Arso Civil** per al Departament de Matemàtiques de l'INS Miquel Tarradell.
Contingut sota CC BY-NC-SA 4.0, codi sota llicència MIT. Vegeu [`LLICENCIA.md`](LLICENCIA.md).

<!-- atribucio-centre:final -->
