# Matemàtiques · material adaptat de `1eso/`

> L'estructura de tot el repositori és al `README.md` de l'arrel. Les ordres d'aquest document
> s'executen des de l'arrel del repositori.

Material de matemàtiques per a **alumnat amb dificultats de tipus cognitiu** que fa la meitat
de les hores a l'**aula de suport** i l'altra meitat a l'aula ordinària. Segueix la programació
del grup, una unitat per situació d'aprenentatge, amb tres regles de fons:

- **un sol dibuix per a tot el curs**, la quadrícula de quadrets;
- **res no es demana de memòria**: el que cal recordar és a les targetes de consulta;
- **cap exercici no necessita la calculadora.**

El perquè de tot plegat és a [`docs/`](docs/).

---

## Com s'obre

Doble clic a `index.html`. No cal servidor ni instal·lar res. Publicat, és a
`https://pi.step-quiz.net/1eso/`.

---

## La caixa d'eines

Les eines de pantalla de la unitat 1, amb el mateix dibuix que el paper: la quadrícula. S'obre
amb doble clic a `caixa-eines.html`. Publicada, és a `https://pi.step-quiz.net/1eso/caixa-eines`.

Per a l'alumnat es fa servir un enllaç que només ensenya una eina. Sempre hi surt també la
pestanya Taules, que és la targeta de les taules a la pantalla:

| Enllaç | Què obre |
|---|---|
| `caixa-eines?task=0` | Taules: 0.1 La taula · 0.2 Troba el resultat a la taula · 0.3 El número que falta |
| `caixa-eines?task=1` | Rectangles: 1.1 Fes un rectangle · 1.2 El rectangle d'una multiplicació · 1.3 Gira el rectangle · 1.4 Parteix el rectangle |
| `caixa-eines?task=2` | Quadrats: 2.1 El quadrat d'un nombre · 2.2 Quin dibuix és? · 2.3 El costat del quadrat |
| `caixa-eines?task=3` | Nombres: 3.1 Centenes, desenes i unitats · 3.2 Fes el nombre |
| `caixa-eines?task=4` | Ordre: 4.1 Mira l'ordre · 4.2 Què es fa primer? |
| `caixa-eines?task=5` | Múltiples (unitat 2): 5.1 La graella de 100 · 5.2 És múltiple? · 5.3 Els trucs · 5.4 Múltiple de 3? |
| `caixa-eines?task=6` | Repartir (unitat 2): 6.1 Reparteix en files · 6.2 Sobren quadrets? |
| `caixa-eines?task=7` | Divisors (unitat 2): 7.1 Els rectangles d'un nombre · 7.2 Troba els divisors |
| `caixa-eines?task=8` | Primers (unitat 2): 8.1 El garbell d'Eratòstenes · 8.2 És primer? |
| `caixa-eines?task=9` | Fraccions (unitat 4): 9.1 Fes la fracció · 9.2 Quina fracció és? |
| `caixa-eines?task=10` | Equivalents (unitat 4): 10.1 Parteix els trossos · 10.2 Són equivalents? |
| `caixa-eines?task=11` | Compara (unitat 4): 11.1 Compara dues fraccions · 11.2 Quina és més gran? |
| `caixa-eines?task=12` | Sumes (unitat 4): 12.1 Suma i resta · 12.2 Quant és? |

Afegint el número de la subtasca s'hi va directament, i ja no es pot passar a cap altre
exercici: `caixa-eines?task=1.2` obre la 1.2 sense les fletxes de la barra. Amb
`caixa-eines?task=1`, l'eina sencera, amb les fletxes. Les tasques
tancades (0.2, 0.3, 1.2, 2.2, 3.2 i 4.2; de la unitat 2, 5.2, 5.4, 6.2, 7.2 i 8.2; i de la unitat 4,
9.2, 10.2, 11.2 i 12.2) acaben amb
un codi de verificació, que es llegeix a
`verifica.html`. Les frases es canvien a `textos.html`.

Com està feta i com s'amplia: [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md).

---

## Què hi ha

| | |
|---|---|
| `index.html` | La portada: tria entre les fitxes i la caixa d'eines, i a sota, «Per al professorat» |
| `fitxes.html` | Índex de les targetes de consulta i de les set unitats |
| `caixa-eines.html` | La caixa d'eines. `verifica.html` llegeix els codis i `textos.html` canvia les frases |
| `dades/textos.js` | Totes les frases de la caixa, i què fa cadascuna |
| `js/` | La caixa: `nucli.js`, `codi.js`, `tasca.js`, `quadricula.js`, `app.js` i les cinc eines a `moduls/` |
| `targetes/` | Les targetes de consulta: la de les taules de multiplicar (unitat 1) i la dels noms de les fraccions (unitat 4) |
| `fitxes/` | Les fitxes de cada unitat (`udN.html`, i `udN-nom.html` si en té més d'una). Ara hi ha les quatre de la unitat 1 (rectangles i quadrats; centenes, desenes i unitats; l'ordre de les operacions, i el repàs) i les cinc de la unitat 2 (els múltiples, repartir en files, divisors i primers, la factorització, i el repàs) |
| `pdf/` | Els PDF per imprimir, i `empremtes.json`, que diu de quina versió de cada font surten |
| `dades/unitats.js` | Les set unitats i les targetes: el que llegeix `fitxes.html` |
| `css/` | `tokens.css` (colors i lletres), `fitxa.css` (tot el paper), `lloc.css` (la portada i `fitxes.html`) i `app.css` (la caixa) |
| `js/lloc.js` | Pinta `fitxes.html` a partir de les dades |
| `fonts/` | La lletra manuscrita, Caveat, i la seva llicència |
| `eines/` | El test, la mesura de l'A4, `paper.py` (que comparteixen amb el generador) i els dos tests de la caixa |
| `generadors/gen_pdf.py` | Fa els PDF |
| `docs/` | Els criteris de disseny, el mapa d'adaptació, l'arquitectura de la caixa i l'estat de la feina |

Els fulls d'estil són una còpia dels de `4eso/`, no un enllaç: si aquells canvien, aquests no
s'han de moure.

---

## Comprovacions

```bash
python3 1eso/eines/comprova.py
```

Ha de dir «Tot correcte.». No necessita res més que Python. Si canvies una fitxa, una targeta o
un full d'estil, també:

```bash
pip install weasyprint --break-system-packages     # només el primer cop de cada Codespace
python3 1eso/eines/mesura.py                        # cada pàgina cap en un A4?
python3 1eso/generadors/gen_pdf.py                  # torna a fer els PDF
```

`comprova.py` sap si un PDF és d'abans de l'últim canvi, i ho diu. Què comprova i què no és al
final de [`docs/CRITERIS-DISSENY.md`](docs/CRITERIS-DISSENY.md).

Si canvies la caixa d'eines, també els dos tests que la fan servir en un navegador. Necessiten
Playwright i Chromium:

```bash
pip install playwright --break-system-packages      # només el primer cop de cada Codespace
python3 -m playwright install --with-deps chromium  # ídem
python3 1eso/eines/prova_caixa.py                   # que funcioni: ha de dir «Tot correcte.»
python3 1eso/eines/auditoria.py                     # accessibilitat: ha de dir «0 problemes»
```

---

## Com s'afegeix

**Una targeta de consulta:** un fitxer a `targetes/`, amb una cara per bloc
`<div class="full targeta">` i el peu `Targeta de … · cara N`. Una línia a `window.TARGETES`
de `dades/unitats.js`. Després, `gen_pdf.py` i `comprova.py`.

**Una fitxa:** `fitxes/udN.html`, amb el rètol del graó físic (`.previ`), l'obertura «Què hi
veus?», les pàgines de la unitat, «A la vida de cada dia» (`.full.vida`) i el solucionari
(`.full.sol`). A `dades/unitats.js`, a la llista `fitxes` de la unitat, amb el camí i el títol.
Una unitat en pot tenir més d'una, en l'ordre de classe: la segona i les següents es diuen
`udN-nom.html` (per exemple, `ud1-nombres.html`). Després, `mesura.py`, `gen_pdf.py` i
`comprova.py`.

En tots dos casos, cada bloc `.full` acaba amb un `</div>` a principi de línia, i els `</div>`
de dins van sagnats: és com els generadors saben on acaba cada pàgina.

**Una eina o una subtasca de la caixa:** vegeu [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md),
apartat 7.

---

## L'examen

Cada unitat té el seu a `generadors/examens/udN.js`, amb el motor comú de
[`../comu/examens/nucli.js`](../comu/examens/nucli.js) i les regles de
[`../comu/docs/EXAMENS-DOCX.md`](../comu/docs/EXAMENS-DOCX.md). Al Codespace, des de l'arrel del
repositori:

```bash
npm install --prefix /tmp/eines docx@9.6.1 sharp@0.34.5     # només el primer cop de cada Codespace
NODE_PATH=/tmp/eines/node_modules node 1eso/generadors/examens/ud1.js
NODE_PATH=/tmp/eines/node_modules node 1eso/generadors/examens/ud2.js
```

Surten dos DOCX a `1eso/docx/`: l'examen i el solucionari. **No es pugen mai**: el `.gitignore`
els deixa fora. Per posar el curs a la capçalera, abans es crea
`1eso/generadors/examens-privat.json`, que tampoc no es puja: Tot el
repositori es publica al web: un DOCX que hi quedés, fins i tot als `generadors/`, es podria obrir
abans de l'examen. Per això `comprova.py` avisa si en troba cap fora de `docx/`, i el `.gitignore`
deixa fora també els DOCX dels `generadors/`.

```json
{ "curs": "el nom del grup", "adaptacio": "el que ha de dir el solucionari" }
```

Sense aquest fitxer, l'examen surt sense curs, i el solucionari diu «alumnat amb dificultats de
tipus cognitiu».

---

## La lletra manuscrita

`fonts/Caveat.ttf` és la lletra Caveat, de The Caveat Project Authors, sota la llicència SIL
Open Font License 1.1 (`fonts/OFL.txt`). No és part del codi ni del contingut d'aquest
material, i no li afecta la llicència de sota. Va dins del repositori perquè el PDF surti amb
lletra manuscrita a qualsevol ordinador.

<!-- atribucio-centre:inici -->

---

Material desenvolupat per **David Arso Civil** per al Departament de Matemàtiques de l'INS Miquel Tarradell.
Contingut sota CC BY-NC-SA 4.0, codi sota llicència MIT. Vegeu [`LLICENCIA.md`](../LLICENCIA.md).

<!-- atribucio-centre:final -->
