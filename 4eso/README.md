# Matemàtiques Aplicades · material adaptat

> Aquest és el material de la carpeta `4eso/`. L'estructura de tot el repositori és al
> `README.md` de l'arrel. Les ordres d'aquest document s'executen des d'aquí: `cd 4eso/`.

Material de matemàtiques per a **alumnat amb dificultats de tipus cognitiu** que fa una
part de les hores a l'**aula de suport** i l'altra a l'aula ordinària, en l'itinerari
d'**Aplicades**.

Set fitxes imprimibles, una caixa d'eines digital i la documentació que explica per què
tot és com és.

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
| `fitxes.html` | índex de les set unitats: tria ràpida i, per a cada una, material previ, regla trencada, fita, recursos |
| `caixa-eines.html` | l'aplicació, amb vuit mòduls |
| `verifica.html` | pàgina per llegir els codis de verificació que dona la caixa d'eines |
| `fitxes/ud1…ud7.html` | les fitxes imprimibles, en blanc i negre |
| `dades/textos.js` | **totes les frases** que llegeix l'alumnat; és l'únic lloc on s'editen |
| `textos.html` | pàgina per canviar-les sense tocar codi |
| `pdf/` | dos PDF per unitat: un per a l'alumnat i un per al professorat |
| `docs/` | mapa d'adaptació, criteris de disseny, arquitectura i feina pendent |
| `generadors/` | scripts Python que dibuixen els gràfics SVG i generen els PDF; a `examens/`, el contingut de cada examen DOCX |
| `eines/` | el test del projecte, la mesura de les pàgines i l'auditoria d'accessibilitat |

---

## Enllaços per a l'alumnat

Per enviar una sola eina, afegeix `?task=n` a l'adreça de la caixa d'eines, per exemple
`https://pi.step-quiz.net/4eso/caixa-eines?task=2`. Es veuen dues pestanyes: la Calculadora,
sempre la primera, i la tasca triada, que és la que s'obre. Sense `?task` es veu tot. Els enllaços d'abans,
sense `/4eso`, continuen funcionant: la `404.html` de l'arrel els porta aquí.

| n | tasca |
|---|---|
| 0 | Calculadora (surt sempre) |
| 1 | Recta · té 6 exercicis: `?task=1.1` a `?task=1.6` |
| 2 | Doble recta |
| 3 | Percentatges |
| 4 | Escales |
| 5 | Paràboles |
| 6 | Equacions |
| 7 | Com ho dic |

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

Llegeix **`docs/CRITERIS-DISSENY.md`**. Hi ha vuit regles que no són preferències
d'estil: són el resultat d'iterar amb el docent i algunes van sortir de correccions
seves. Les dues que més fàcilment es trenquen sense adonar-se'n:

- **Blanc i negre estricte a les fitxes.** S'imprimeixen en B/N i no se sap com quedarien
  els colors. Hi ha un test que ho comprova: `python3 eines/comprova.py`.
- **Cap paràgraf a les pàgines de l'alumnat.** El dibuix explica, les paraules només
  etiqueten. Aquesta regla val per a les fitxes, no per als solucionaris ni per a les
  pàgines de navegació, que són per a l'adult.

---

## Els PDF

Cada unitat té dos PDF a `pdf/`, enllaçats des de `fitxes.html`:

| | |
|---|---|
| `udN-alumnat.pdf` | les pàgines que es reparteixen |
| `udN-solucionari.pdf` | el full del professorat, amb els errors típics i els criteris |

Es tornen a generar amb:

```
pip install weasyprint --break-system-packages
python3 generadors/gen_pdf.py
```

**Si has afegit contingut a una fitxa**, passa abans `python3 eines/mesura.py`: comprova
que cada pàgina segueixi cabent en un A4. Si alguna vessa, la solució no és encongir la
lletra —el cos de 14 pt és una restricció del projecte— sinó treure contingut o partir
la pàgina en dues.

> ⚠ **Els PDF d'ara no porten la pàgina «A la vida de cada dia».** Es va afegir a les set
> fitxes i els PDF no s'han pogut regenerar (calen WeasyPrint i la font Carlito). Fes
> `python3 eines/mesura.py` i després `python3 generadors/gen_pdf.py` abans de repartir-ne
> cap. Les pàgines noves es van mesurar amb Chromium i totes queden per sota de les
> pàgines més plenes que ja hi havia, però qui mana és `mesura.py`.

---

## Comprovacions

```
python3 eines/comprova.py
```

Verifica que les fitxes no tinguin cap valor cromàtic, que l'HTML tanqui bé, que la
numeració de pàgines sigui seguida, que cada fitxa porti el rètol de material, l'obertura
i la pàgina «A la vida de cada dia», i que els mòduls declarats a `caixa-eines.html`
coincideixin amb els que es registren de debò. També revisa les frases de l'alumnat amb
les regles de Lectura Fàcil que es poden comprovar soles i calcula el contrast de la
paleta de pantalla (WCAG 2.2 AA).

```
pip install playwright --break-system-packages && python3 -m playwright install chromium
python3 eines/auditoria.py
```

Obre l'app en un navegador de veritat i mesura les dianes tàctils i el contrast real de
cada text, en mode clar i fosc, a 320 px i a escriptori. Ara mateix: **0 problemes en 56
estats**.

---

## Estat

Set unitats completes. Vuit mòduls a la caixa d'eines.

Cada fitxa acaba amb una pàgina **«A la vida de cada dia»**: un context real i una segona
situació on la mateixa decisió s'ha de tornar a prendre en un escenari diferent. Cinc
tasques de la caixa d'eines (Calculadora, 1.2, 1.3, Paràboles i Equacions) són tasques
tancades, amb passos, retroacció literal, resum final i un codi de verificació que es
llegeix a `verifica.html`.

**Pendent**, documentat a `docs/CONTINUAR.md`:

- **regenerar els catorze PDF** perquè incloguin la pàgina nova (`mesura.py` i `gen_pdf.py`);
- contrastar el teclat del mòdul Calculadora amb una Casio fx-82SP CW real;
- no hi ha mòdul d'estadística ni d'atzar (per a la U6 l'eina és el full de càlcul).

<!-- atribucio-centre:inici -->

---

Material desenvolupat per **David Arso Civil** per al Departament de Matemàtiques de l'INS Miquel Tarradell.
Contingut sota CC BY-NC-SA 4.0, codi sota llicència MIT. Vegeu [`LLICENCIA.md`](LLICENCIA.md).

<!-- atribucio-centre:final -->
