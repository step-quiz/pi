# Matemàtiques Aplicades · material adaptat

> Aquest és el material de la carpeta `4eso/`. L'estructura de tot el repositori és al
> `README.md` de l'arrel. Les ordres d'aquest document s'executen des d'aquí: `cd 4eso/`.

Material de matemàtiques per a **alumnat amb dificultats de tipus cognitiu** que fa una
part de les hores a l'**aula de suport** i l'altra a l'aula ordinària, en l'itinerari
d'**Aplicades**.

Set fitxes imprimibles, amb una fitxa de repàs per unitat, un quadern d'activitats per
practicar (de moment, el de la UD3), tres targetes de consulta, una caixa d'eines digital i
la documentació que explica per què tot és com és.

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
| `index.html` | la pàgina del curs: les seves unitats. La fa `../comu/js/curs.js` |
| `u1/` … `u7/` | una carpeta per unitat. `index.html`, la pàgina de la unitat, per al docent (una còpia de `../comu/eines/unitat.html`, que fa `../comu/js/unitat.js`): 1 Fitxa · 2 Quadern d'activitats · 3 Repàs, amb els PDF; les eines i les targetes de la unitat; i «Abans de la classe». `fitxa.html`, la fitxa imprimible, en blanc i negre. `repas.html`, la fitxa de repàs: el dibuix de la unitat, «Una de cada» i «Què he après?»; no s'edita a mà, la fa `generadors/gen_repas.py`. A la `u3/`, `quadern.html`, el quadern d'activitats, amb el filtre de quantitat i de tipologia; no s'edita a mà, el fa `generadors/gen_quadern.py` a partir de `generadors/quadern/udN.py` |
| `eines.html` | les eines de l'alumnat, amb deu mòduls. S'obre amb `eines.html?u=N`: només les eines de la unitat N, i cap enllaç cap a la resta del web |
| `professorat.html` | la pàgina del professorat: canviar les frases, llegir els codis i les notes generals |
| `verifica.html` | pàgina per llegir els codis de verificació que donen les eines |
| `targetes/` | dues targetes de consulta per tenir a la taula (percentatges i escales; paràboles, dades i atzar), a doble cara. La de la calculadora es va treure el 6/11/2026 |
| `dades/textos.js` | **totes les frases** que llegeix l'alumnat; és l'únic lloc on s'editen |
| `textos.html` | pàgina per canviar-les sense tocar codi |
| `pdf/` | dos PDF per fitxa (alumnat i professorat) i un per targeta |
| `docs/` | mapa d'adaptació, criteris de disseny, arquitectura i feina pendent |
| `generadors/` | scripts Python que dibuixen els gràfics SVG (`posa_grafics.py` els posa a les fitxes) i generen els PDF; a `examens/`, el contingut de cada examen DOCX |
| `eines/` | el test del projecte, la mesura de les pàgines i l'auditoria d'accessibilitat |
| `fonts/` | la lletra manuscrita, Caveat, i la seva llicència |

---

## Les eines de cada unitat

L'alumnat entra a les eines amb l'enllaç que el docent copia a la pàgina de la unitat («Copia
l'enllaç per a l'alumnat»), per exemple `https://pi.step-quiz.net/4eso/eines?u=3`. Hi surten
només les eines de la unitat (camp `tasques` de `dades/unitats.js`): primer les seves i, després
d'una ratlla, la Calculadora i Com ho dic. La capçalera diu la unitat i no porta enlloc.

Cada eina té un número fix (`data-tasca`). `?task=n` (una sola eina) i `?task=n.m` (un sol
exercici) encara funcionen, però ja no s'enllacen enlloc: només els fan servir les proves.

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

## La lectura en veu alta

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

Cada fitxa té dos PDF a `pdf/`, enllaçats des de la pàgina de la unitat (`uN/index.html`) i des de la mateixa fitxa:

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

**Els quaderns d'activitats tampoc.** Vegeu l'apartat següent.

**Si canvies un gràfic**, canvia el seu generador (`generadors/gen_grafics*.py`) i passa
`python3 generadors/posa_grafics.py`: torna a fer tots els gràfics i els posa a les fitxes,
on cada un va entre dos marcadors (`<!--grafic:NOM-->…<!--/grafic-->`). Després,
`mesura.py` i `gen_pdf.py`.

---

## El quadern d'activitats

Per practicar **després** de la fitxa. S'hi arriba des de la pàgina de la unitat
(portada → unitat → «Quadern d'activitats»), i el quadern torna a la unitat («← la unitat»).

Hi ha un bloc per cada exercici de la fitxa, en el mateix ordre, i el subtítol de cada bloc
diu quin exercici és i a quina pàgina («Com l'exercici 2 de la fitxa, a la pàgina 5»). Cada
bloc té **una activitat germana** (el mateix exercici amb altres números i contextos) i
**una de repte** (el camí al revés, un pas més o una decisió nova), marcada amb una
estrella. Té els mateixos criteris que la fitxa: blanc i negre, cap paràgraf, 14 pt cap
amunt i l'apartat a) de cada activitat resolt en lletra manuscrita.

A dalt de la pàgina, només a la pantalla, hi ha el filtre. **El nombre d'activitats no
canvia amb la quantitat: el que canvia és quants apartats té cada una** (decisió del
docent, 5/11/2026):

| | |
|---|---|
| **Apartats de cada activitat** | **Petit**: a) resolt i 3 per fer (b, c, d). **Mitjà**: a) i 6 (b a g). **Elevat**: a) i 12 (b a m) |
| **Activitats** | **Com les de la fitxa**: una per bloc. **Amb repte**: s'hi afegeix la de repte de cada bloc, que també té 3, 6 o 12 apartats |

| UD3 | Petit | Mitjà | Elevat |
|---|---|---|---|
| Com les de la fitxa (8 activitats) | 6 pàgines | 10 pàgines | 15 pàgines |
| Amb repte (16 activitats) | 10 pàgines | 17 pàgines | 31 pàgines |

Els apartats van de menys a més dins de cada activitat (per exemple, els de 1 : 100 abans
que els de 1 : 50), perquè els que s'amaguen són sempre els últims.

Hi ha tres botons: **Imprimeix el quadern** (les activitats, sense el solucionari; Ctrl+P fa
el mateix), **Imprimeix el solucionari** (només el solucionari, amb els mateixos apartats
del filtre) i **Mostra el solucionari** (a la pantalla està amagat). Una taula, o un dibuix
amb la seva taula, no es parteix entre dues pàgines si hi cap en una. El número de pàgina
surt al peu.

El filtre queda a l'adreça, i es pot enviar un enllaç amb el filtre posat:
`u3/quadern.html?n=1&repte=1` (`n`: 1 quantitat petita, 2 mitjana, 3 alta; `repte`: 0 o 1).

**Com es canvia o s'amplia.** El contingut és a `generadors/quadern/udN.py`: cada activitat
té 13 apartats (l'a i 12 per fer, en ordre de menys a més): el motor hi posa sol la marca
de la quantitat (els 3 primers per fer, petit; els 3 següents, mitjà; els 6 últims, elevat).
Si una activitat no en té 13, el generador s'atura. Les de repte porten `repte=True`. Els
números de les respostes es calculen al mateix fitxer, i el solucionari surt de les
mateixes dades. Després:

```
python3 generadors/gen_quadern.py
python3 eines/comprova.py
python3 eines/prova_quadern.py
```

Per fer el quadern d'una altra unitat, es copia `generadors/quadern/ud3.py` a `udN.py`, es
canvia el contingut i s'afegeix `quadern: "uN/quadern.html"` a la unitat de
`dades/unitats.js`. Les peces que hi ha (taules, opcions per marcar, ofertes, plànols, doble
recta, línies per mesurar, quadrícula) són a `generadors/gen_quadern.py`.

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
les targetes siguin en B/N amb les cares numerades, que hi hagi tots els PDF, i que els mòduls declarats a `eines.html`
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
python3 eines/prova_quadern.py
```

`prova_quadern.py` prova el filtre de cada quadern en Chromium: les sis combinacions, que
cada activitat tingui els apartats que toquen amb les lletres seguides, que el solucionari
amagui els mateixos, l'adreça amb el filtre i què s'imprimeix. `comprova.py` també mira els
quaderns: B/N, que cada activitat tingui l'a) i 12 apartats marcats de menys a més (també
al solucionari), que les consignes siguin curtes i que el fitxer de `quadern/` sigui el que
surt del generador.

Prova les eines de punta a punta en Chromium: obre totes les pestanyes i els enllaços `?task=n`,
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
- el quadern d'activitats de les unitats 1, 2, 4, 5, 6 i 7, quan el de la UD3 s'hagi
  provat a l'aula.

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
