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

## Què hi ha

| | |
|---|---|
| `index.html` | La portada: les targetes de consulta i les set unitats |
| `targetes/` | Les targetes de consulta. Ara hi ha la de les taules de multiplicar |
| `fitxes/` | Les fitxes de cada unitat, quan es facin (`udN.html`) |
| `pdf/` | Els PDF per imprimir, i `empremtes.json`, que diu de quina versió de cada font surten |
| `dades/unitats.js` | Les set unitats i les targetes: el que llegeix la portada |
| `css/` | `tokens.css` (colors i lletres), `fitxa.css` (tot el paper) i `lloc.css` (la portada) |
| `js/lloc.js` | Pinta la portada a partir de les dades |
| `fonts/` | La lletra manuscrita, Caveat, i la seva llicència |
| `eines/` | El test, la mesura de l'A4 i `paper.py`, que comparteixen amb el generador |
| `generadors/gen_pdf.py` | Fa els PDF |
| `docs/` | Els criteris de disseny, el mapa d'adaptació i l'estat de la feina |

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
