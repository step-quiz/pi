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

## Les eines

Les eines de pantalla, amb el mateix dibuix que el paper: la quadrícula. L'alumnat hi entra amb
l'enllaç que el docent copia a la pàgina de cada unitat, per exemple
`https://pi.step-quiz.net/1eso/eines?u=3`: només hi surten les eines de la unitat (camp `tasques`
de `dades/unitats.js`) i, després d'una ratlla, les Taules, que són la targeta de les taules a la
pantalla. La capçalera diu la unitat i no porta enlloc. Cada eina es carrega quan s'obre.

Cada eina té un número fix. `?task=n` (una sola eina) i `?task=n.m` (un sol exercici) encara
funcionen, però ja no s'enllacen enlloc: només els fan servir les proves.

| Número (`?task=`) | Què obre |
|---|---|
| `0` | Taules: 0.1 La taula · 0.2 Troba el resultat a la taula · 0.3 El número que falta |
| `1` | Rectangles: 1.1 Fes un rectangle · 1.2 El rectangle d'una multiplicació · 1.3 Gira el rectangle · 1.4 Parteix el rectangle |
| `2` | Quadrats: 2.1 El quadrat d'un nombre · 2.2 Quin dibuix és? · 2.3 El costat del quadrat · 2.4 Entre quins dos nombres? (unitat 5) |
| `3` | Nombres: 3.1 Centenes, desenes i unitats · 3.2 Fes el nombre |
| `4` | Ordre: 4.1 Mira l'ordre · 4.2 Què es fa primer? |
| `5` | Múltiples (unitat 2): 5.1 La graella de 100 · 5.2 És múltiple? · 5.3 Els trucs · 5.4 Múltiple de 3? |
| `6` | Repartir (unitat 2): 6.1 Reparteix en files · 6.2 Sobren quadrets? |
| `7` | Divisors (unitat 2): 7.1 Els rectangles d'un nombre · 7.2 Troba els divisors |
| `8` | Primers (unitat 2): 8.1 El garbell d'Eratòstenes · 8.2 És primer? |
| `9` | Fraccions (unitat 3): 9.1 Fes la fracció · 9.2 Quina fracció és? |
| `10` | Equivalents (unitat 3): 10.1 Parteix els trossos · 10.2 Són equivalents? |
| `11` | Compara (unitat 3): 11.1 Compara dues fraccions · 11.2 Quina és més gran? |
| `12` | Sumes (unitat 3): 12.1 Suma i resta · 12.2 Quant és? |
| `13` | Àrea (unitat 3): 13.1 Compta l'àrea · 13.2 Quina àrea té? |
| `14` | Fracció d'un nombre (unitat 4): 14.1 Reparteix i pinta · 14.2 Quant és? |
| `15` | Multiplicar fraccions (unitat 4): 15.1 El tros de tros · 15.2 Quin tros és? |
| `16` | Percentatges (unitat 4): 16.1 Pinta el percentatge · 16.2 Quin percentatge és? |
| `17` | Dobles i triples (unitat 4): 17.1 El doble i el triple · 17.2 Quantes vegades hi cap? |
| `18` | Decimals (unitat 5): 18.1 Fes el decimal · 18.2 Quin decimal és? · 18.3 Quin és més gran? |
| `19` | Arrodonir (unitat 5): 19.1 El decimal a la recta · 19.2 Arrodoneix |
| `20` | Sumar decimals (unitat 5): 20.1 Suma i resta · 20.2 Quant és? |
| `21` | Fracció i decimal (unitat 5): 21.1 Pinta la fracció · 21.2 De fracció a decimal |
| `22` | Angles (unitat 6): 22.1 Obre l'angle · 22.2 Quin angle és? |
| `23` | Polígons (unitat 6): 23.1 El polígon al geoplà · 23.2 Com es diu? |
| `24` | Triangles (unitat 6): 24.1 Els tres angles · 24.2 Quin triangle és? |
| `25` | Perímetre (unitat 6): 25.1 Perímetre i àrea · 25.2 Quin és el perímetre? |
| `26` | Patrons (unitat 7): 26.1 El patró · 26.2 Quants en té la següent? |
| `27` | Símbols (unitat 7): 27.1 La paraula i el símbol · 27.2 Quin és el símbol? |
| `28` | Gràfics (unitat 7): 28.1 Llegeix el gràfic · 28.2 Quantes persones? |

Afegint el número de la subtasca s'hi va directament, i ja no es pot passar a cap altre
exercici: `eines.html?task=1.2` obre la 1.2 sense les fletxes de la barra. Amb
`eines.html?task=1`, l'eina sencera, amb les fletxes. Les tasques
tancades (0.2, 0.3, 1.2, 2.2, 3.2 i 4.2; de la unitat 2, 5.2, 5.4, 6.2, 7.2 i 8.2; i de la unitat 3,
9.2, 10.2, 11.2, 12.2 i 13.2; de la unitat 4, 14.2, 15.2, 16.2 i 17.2; i de la unitat 5,
2.4, 18.2, 18.3, 19.2, 20.2 i 21.2; de la unitat 6, 22.2, 23.2, 24.2 i 25.2; i de la unitat 7, 26.2, 27.2 i 28.2) acaben amb
un codi de verificació, que es llegeix a
`verifica.html`. Les frases es canvien a `textos.html`.

### La lectura en veu alta

Cada targeta de la caixa té, a dalt a la dreta, un botó petit amb un altaveu. En tocar-lo, la
targeta es llegeix en veu alta, a poc a poc i un bloc cada vegada, i el bloc que s'està llegint
queda ben clar mentre la resta de la targeta s'esvaeix. Si la veu de l'ordinador diu per on va,
un retolador groc omple la línia a poc a poc, al ritme de la veu. Tornar-lo a tocar la para. Funciona sense xarxa i sense instal·lar res.

La veu és la de l'ordinador, i n'hi ha de més bones que d'altres:

- **Microsoft Edge** porta dues veus catalanes naturals (Joana i Enric). És el que sona millor,
  i, a més del bloc, també marca
  la paraula que es diu.
- **Chrome a Windows** fa servir les veus de Windows. Si no n'hi ha cap de catalana: Configuració
  → Hora i idioma → Idioma i regió → Afegeix un idioma → Català, amb la casella de la veu.
- **Chromebooks, tauletes i mòbils**: si llegeix amb accent castellà, cal instal·lar la veu
  catalana a la configuració de «Text a veu» del dispositiu.

Com està fet i per què: [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md), apartat «La veu».

Com està feta i com s'amplia: [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md).

---

## Què hi ha

| | |
|---|---|
| `index.html` | La pàgina del curs: les seves unitats. La fa `../comu/js/curs.js` |
| `u1/` … `u7/` | Una carpeta per unitat. `index.html`, la pàgina de la unitat, per al docent (una còpia de `../comu/eines/unitat.html`, que fa `../comu/js/unitat.js`): les fitxes numerades, el quadern d'activitats (o «no disponible») i el repàs, amb els PDF; les eines i la targeta de la unitat; i «Abans de la classe». A dins, les fitxes: `fitxa.html` la principal, `NOM.html` les altres, i `repas.html` |
| `eines.html` | Les eines de l'alumnat (`eines.html?u=N`). `verifica.html` llegeix els codis i `textos.html` canvia les frases |
| `professorat.html` | **Tancada des del 6/11/2026** (s'obre amb `?obert`; vegeu `../comu/docs/SITE-MAP.md`). La pàgina del professorat: canviar les frases, llegir els codis i les notes generals |
| `dades/textos.js` | Totes les frases de la caixa, i què fa cadascuna |
| `js/` | La caixa: `nucli.js`, `codi.js`, `tasca.js`, `quadricula.js`, `app.js` i les 29 eines a `moduls/`, una per fitxer |
| `targetes/` | Les targetes de consulta: la de les taules de multiplicar (unitat 1), la dels noms de les fraccions (unitat 3), la dels decimals i les arrels (unitat 5), la de les formes (unitat 6) i la dels patrons i els símbols (unitat 7) |
| `pdf/` | Els PDF per imprimir, i `empremtes.json`, que diu de quina versió de cada font surten |
| `dades/unitats.js` | Les set unitats i les targetes: el que llegeixen totes les pàgines del curs |
| `css/` | `tokens.css` (colors i lletres), `fitxa.css` (tot el paper), `lloc.css` (`textos.html` i `verifica.html`) i `app.css` (les eines). La closca de pantalla és comuna: `../comu/css/web.css` |
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
python3 1eso/eines/mesura.py                        # cada pàgina cap en un A4, d'alt i d'ample?
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
python3 1eso/eines/auditoria.py                     # accessibilitat i lletra al paper: ha de dir «0 problemes»
```

---

## Com s'afegeix

**Una targeta de consulta:** un fitxer a `targetes/`, amb una cara per bloc
`<div class="full targeta">` i el peu `Targeta de … · cara N`. Una línia a `window.TARGETES`
de `dades/unitats.js`. Després, `gen_pdf.py` i `comprova.py`.

**Una fitxa:** `uN/fitxa.html`, amb el rètol del graó físic (`.previ`), l'obertura «Què hi
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
NODE_PATH=/tmp/eines/node_modules node 1eso/generadors/examens/ud3.js
NODE_PATH=/tmp/eines/node_modules node 1eso/generadors/examens/ud4.js
NODE_PATH=/tmp/eines/node_modules node 1eso/generadors/examens/ud5.js
NODE_PATH=/tmp/eines/node_modules node 1eso/generadors/examens/ud6.js
NODE_PATH=/tmp/eines/node_modules node 1eso/generadors/examens/ud7.js
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
