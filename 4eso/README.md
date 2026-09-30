# Matemàtiques Aplicades · material adaptat

> Aquest és el material de la carpeta `4eso/`. L'estructura de tot el repositori és al
> `README.md` de l'arrel. Les ordres d'aquest document s'executen des d'aquí: `cd 4eso/`.

Material de matemàtiques per a **alumnat amb dificultats de tipus cognitiu** que fa una
part de les hores a l'**aula de suport** i l'altra a l'aula ordinària, en l'itinerari
d'**Aplicades**.

Set fitxes imprimibles, amb una fitxa de repàs per unitat, tres targetes de consulta, una
caixa d'eines digital i la documentació que explica per què tot és com és.

---

## Com s'obre

Doble clic a `index.html`. No cal servidor, ni instal·lar res, ni cap dependència.

## On es publica

GitHub → Cloudflare Pages → `step-quiz.net`, amb **tots els camps del formulari buits**.
És un lloc estàtic corrent: no hi ha res a compilar. Vegeu `../comu/docs/DESPLEGAMENT.md`.

---

## Què hi ha

| | |
|---|---|
| `index.html` | portada: tria entre les fitxes i la caixa d'eines |
| `fitxes.html` | índex de les set unitats: tria ràpida i, per a cada una, material previ, regla trencada, fita, recursos, fitxa de repàs; al final, les targetes de consulta |
| `caixa-eines.html` | l'aplicació, amb deu mòduls |
| `verifica.html` | pàgina per llegir els codis de verificació que dona la caixa d'eines |
| `fitxes/ud1…ud7.html` | les fitxes imprimibles, en blanc i negre |
| `fitxes/udN-repas.html` | la fitxa de repàs de cada unitat: el dibuix de la unitat, «Una de cada» i «Què he après?». No s'editen a mà: les fa `generadors/gen_repas.py` |
| `targetes/` | tres targetes de consulta per tenir a la taula (calculadora, percentatges i escales, paràboles, dades i atzar), a doble cara |
| `dades/textos.js` | **totes les frases** que llegeix l'alumnat; és l'únic lloc on s'editen |
| `textos.html` | pàgina per canviar-les sense tocar codi |
| `pdf/` | dos PDF per fitxa (alumnat i professorat) i un per targeta |
| `docs/` | mapa d'adaptació, criteris de disseny, arquitectura i feina pendent |
| `generadors/` | scripts Python que dibuixen els gràfics SVG (`posa_grafics.py` els posa a les fitxes) i generen els PDF; a `examens/`, el contingut de cada examen DOCX |
| `eines/` | el test del projecte, la mesura de les pàgines i l'auditoria d'accessibilitat |
| `fonts/` | la lletra manuscrita, Caveat, i la seva llicència |

---

## Enllaços per a l'alumnat

Per enviar una sola eina, afegeix `?task=n` a l'adreça de la caixa d'eines, per exemple
`https://pi.step-quiz.net/4eso/caixa-eines?task=2`. Es veuen dues pestanyes: la Calculadora,
sempre la primera, i la tasca triada, que és la que s'obre. Sense `?task` es veu tot. Els enllaços d'abans,
sense `/4eso`, continuen funcionant: la `404.html` de l'arrel els porta aquí.

| n | tasca |
|---|---|
| 0 | Calculadora (surt sempre) |
| 1 | Recta · té 6 exercicis: `?task=1.1` a `?task=1.6`. Amb el número de l'exercici s'obre aquell i prou, sense les fletxes per passar als altres |
| 2 | Doble recta |
| 3 | Percentatges |
| 4 | Escales |
| 5 | Paràboles |
| 6 | Equacions |
| 7 | Com ho dic |
| 8 | Aplanar · la mitjana de la U6 |
| 9 | Probabilitat · la barra del dau de la U7 |

Els números no canvien mai, perquè ja poden ser en enllaços enviats.

---

## El principi

> Aquest alumnat pot arribar a la **decisió** que demana el currículum. No pot arribar
> al **càlcul** ni a la **redacció** del nivell del grup.

I Matemàtiques Aplicades és, precisament, la matèria de decidir amb dades. Amb el càlcul
descarregat a la calculadora i l'expressió bastida amb frases model, la competència
nuclear li és accessible de veritat.

El perfil és desigual, i tot el material en surt:

| Canal | Nivell |
|---|---|
| Visió gràfica, esquemes, geometria | 2n ESO |
| Manipulació aritmètica i algebraica | 5è de primària |
| Expressar idees matemàtiques amb frases | 3r de primària |
| Informàtica i anglès | el del grup |

---

## Abans de tocar res

Llegeix **`docs/CRITERIS-DISSENY.md`**. Hi ha deu regles que no són preferències
d'estil: són el resultat d'iterar amb el docent i algunes van sortir de correccions
seves. Les dues que més fàcilment es trenquen sense adonar-se'n:

- **Blanc i negre estricte a les fitxes.** S'imprimeixen en B/N i no se sap com quedarien
  els colors. Hi ha un test que ho comprova: `python3 eines/comprova.py`.
- **Cap paràgraf a les pàgines de l'alumnat.** El dibuix explica, les paraules només
  etiqueten. Aquesta regla val per a les fitxes, no per als solucionaris ni per a les
  pàgines de navegació, que són per a l'adult.

---

## Els PDF

Cada fitxa té dos PDF a `pdf/`, enllaçats des de `fitxes.html`:

| | |
|---|---|
| `udN-alumnat.pdf` | les pàgines que es reparteixen |
| `udN-solucionari.pdf` | el full del professorat, amb els errors típics i els criteris |
| `udN-repas-alumnat.pdf`, `udN-repas-solucionari.pdf` | el mateix, per a la fitxa de repàs |
| `targeta-NOM.pdf` | les dues cares d'una targeta, per imprimir a doble cara |

Es tornen a generar amb:

```
pip install weasyprint --break-system-packages
python3 generadors/gen_pdf.py
```

**Si has afegit contingut a una fitxa**, passa abans `python3 eines/mesura.py`: comprova
que cada pàgina segueixi cabent en un A4, d'alt i d'ample (res no pot sortir pel marge
dret, ni el text d'una opció de la seva capsa). Si alguna vessa, la solució no és encongir
la lletra —el cos de 14 pt és una restricció del projecte— sinó treure contingut o partir
la pàgina en dues.

Els PDF són al dia (30/9/2026): els catorze de les unitats, els catorze de les fitxes de
repàs i els tres de les targetes. `gen_pdf.py` s'atura si un PDF amb text manuscrit no
porta la lletra Caveat a dins.

**Les fitxes de repàs no s'editen a mà.** Es canvien a `generadors/gen_repas.py` i es
tornen a fer amb `python3 generadors/gen_repas.py`. El dibuix de la seva pàgina 1 surt de la
pàgina 1 de la fitxa de la unitat: si aquesta canvia, cal tornar a passar `gen_repas.py`.

**Si canvies un gràfic**, canvia el seu generador (`generadors/gen_grafics*.py`) i passa
`python3 generadors/posa_grafics.py`: torna a fer tots els gràfics i els posa a les fitxes,
on cada un va entre dos marcadors (`<!--grafic:NOM-->…<!--/grafic-->`). Després,
`mesura.py` i `gen_pdf.py`.

---

## Els exàmens

Hi ha un examen en DOCX per unitat, de la UD1 a la UD7: el contingut és a
`generadors/examens/udN.js` i la maquinària i les regles, a `../comu/examens/nucli.js` i
`../comu/docs/EXAMENS-DOCX.md`. Des de l'arrel del repositori:

```
npm install --prefix /tmp/eines docx@9.6.1 sharp@0.34.5
NODE_PATH=/tmp/eines/node_modules node 4eso/generadors/examens/ud2.js
```

Surten a `docx/`, que no es puja mai. Els de la UD2 a la UD7 són del 30/9/2026: els apartats
nous porten la marca «nou» al solucionari, i es van revisar el mateix dia.

---

## Comprovacions

```
python3 eines/comprova.py
```

Verifica que les fitxes no tinguin cap valor cromàtic, que l'HTML tanqui bé, que la
numeració de pàgines sigui seguida, que cada fitxa porti el rètol de material, l'obertura
i la pàgina «A la vida de cada dia» (a les de repàs, «Una de cada» i «Què he après?»), que
les targetes siguin en B/N amb les cares numerades, que hi hagi tots els PDF, i que els mòduls declarats a `caixa-eines.html`
coincideixin amb els que es registren de debò. També revisa les frases de l'alumnat amb
les regles de Lectura Fàcil que es poden comprovar soles i calcula el contrast de la
paleta de pantalla (WCAG 2.2 AA).

```
pip install playwright --break-system-packages && python3 -m playwright install chromium
python3 eines/auditoria.py
```

Obre l'app en un navegador de veritat i mesura les dianes tàctils i el contrast real de
cada text, en mode clar i fosc, a 320 px i a escriptori. També mesura la lletra de les
fitxes tal com surt al PDF: cap text de l'alumnat per sota de 14 pt i cap rètol de gràfic
per sota de 12 pt. Ara mateix: **0 problemes en 68 estats i 17 fitxes o targetes**.

```
python3 eines/prova_caixa.py
```

Prova la caixa de punta a punta en Chromium: obre totes les pestanyes i els enllaços `?task=n`,
mou els mòduls i acaba una tasca tancada (x² = 36), fins a llegir-ne el codi a `verifica.html`.

`comprova.py` també mira que cap PDF sigui vell: `gen_pdf.py` desa a `pdf/empremtes.json`
l'empremta de la fitxa i dels estils de cada PDF, i si la fitxa canvia i el PDF no, ho diu.

`comprova.py` funciona amb Python 3.11 o més nou, sense cap dependència. GitHub el passa sol a
cada pujada (`.github/workflows/comprova.yml`): a la pàgina del repositori, cada commit porta una
marca verda o una creu vermella.

---

## Estat

Set unitats completes, amb una fitxa de repàs per unitat i tres targetes de consulta. Deu mòduls a la caixa d'eines.

Cada fitxa acaba amb una pàgina **«A la vida de cada dia»**: un context real i una segona
situació on la mateixa decisió s'ha de tornar a prendre en un escenari diferent. Cinc
tasques de la caixa d'eines (Calculadora, 1.2, 1.3, Paràboles i Equacions) són tasques
tancades, amb passos, retroacció literal, resum final i un codi de verificació que es
llegeix a `verifica.html`.

**Pendent**, documentat a `docs/CONTINUAR.md`:

- contrastar el teclat del mòdul Calculadora amb una Casio fx-82SP CW real;
- no hi ha mòdul d'estadística ni d'atzar (per a la U6 l'eina és el full de càlcul).

---

## La lletra manuscrita

`fonts/Caveat.ttf` és la lletra Caveat, de The Caveat Project Authors, sota la llicència SIL
Open Font License 1.1 (`fonts/OFL.txt`). És la mateixa de `1eso/` i dels exàmens DOCX. No és
part del codi ni del contingut d'aquest material, i no li afecta la llicència de sota. Va dins
del repositori perquè el model resolt surti en lletra manuscrita a qualsevol ordinador i al
PDF: fins al 29/9/2026 depenia de les lletres de cada ordinador, i els PDF el treien en lletra
d'impremta.

<!-- atribucio-centre:inici -->

---

Material desenvolupat per **David Arso Civil** per al Departament de Matemàtiques de l'INS Miquel Tarradell.
Contingut sota CC BY-NC-SA 4.0, codi sota llicència MIT. Vegeu [`LLICENCIA.md`](../LLICENCIA.md), a l'arrel.

<!-- atribucio-centre:final -->
