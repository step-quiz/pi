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

Afegint el número de la subtasca s'hi va directament, i ja no es pot passar a cap altre
exercici: `caixa-eines?task=1.2` obre la 1.2 sense les fletxes de la barra. Amb
`caixa-eines?task=1`, l'eina sencera, amb les fletxes. Les tasques
tancades (0.2, 0.3, 1.2, 2.2, 3.2 i 4.2) acaben amb un codi de verificació, que es llegeix a
`verifica.html`. Les frases es canvien a `textos.html`.

Com està feta i com s'amplia: [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md).

---

## Què hi ha

| | |
|---|---|
| `index.html` | La portada: les targetes de consulta, la caixa d'eines i les set unitats |
| `caixa-eines.html` | La caixa d'eines. `verifica.html` llegeix els codis i `textos.html` canvia les frases |
| `dades/textos.js` | Totes les frases de la caixa, i què fa cadascuna |
| `js/` | La caixa: `nucli.js`, `codi.js`, `tasca.js`, `quadricula.js`, `app.js` i les cinc eines a `moduls/` |
| `targetes/` | Les targetes de consulta. Ara hi ha la de les taules de multiplicar |
| `fitxes/` | Les fitxes de cada unitat (`udN.html`). Ara hi ha la de la unitat 1: rectangles i quadrats |
| `pdf/` | Els PDF per imprimir, i `empremtes.json`, que diu de quina versió de cada font surten |
| `dades/unitats.js` | Les set unitats i les targetes: el que llegeix la portada |
| `css/` | `tokens.css` (colors i lletres), `fitxa.css` (tot el paper), `lloc.css` (la portada) i `app.css` (la caixa) |
| `js/lloc.js` | Pinta la portada a partir de les dades |
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
(`.full.sol`). A `dades/unitats.js`, `fitxa: "fitxes/udN.html"`. Després, `mesura.py`,
`gen_pdf.py` i `comprova.py`.

En tots dos casos, cada bloc `.full` acaba amb un `</div>` a principi de línia, i els `</div>`
de dins van sagnats: és com els generadors saben on acaba cada pàgina.

**Una eina o una subtasca de la caixa:** vegeu [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md),
apartat 7.

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
