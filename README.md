# Material adaptat de matemàtiques

Material de matemàtiques per a **alumnat amb dificultats de tipus cognitiu**: fitxes
imprimibles, una caixa d'eines digital, exàmens adaptats en Word i la documentació que
explica per què tot és com és.

Cada curs té la seva carpeta, perquè els recursos d'un curs i els de l'altre no són els
mateixos. El que serveix per a tots dos és a `comu/`.

---

## L'estructura

**El mapa del lloc, l'aspecte i les regles són a [`comu/docs/SITE-MAP.md`](comu/docs/SITE-MAP.md)**
(en anglès, per a qui hi arribi de nou, persona o IA). Si el codi i aquell document no coincideixen,
s'arregla el document en el mateix commit.

| Carpeta o fitxer | Què hi ha |
|---|---|
| `4eso/` | El material de Matemàtiques Aplicades: una carpeta per unitat (`u1/` … `u7/`) amb la pàgina de la unitat, la fitxa, el repàs i, a la `u3/`, el quadern d'activitats; les targetes, les eines de l'alumnat, la pàgina del professorat, els PDF, els exàmens, la documentació, els generadors i les proves. Vegeu [`4eso/README.md`](4eso/README.md) |
| `1eso/` | El material de Matemàtiques, amb la mateixa estructura: a cada carpeta d'unitat, totes les seves fitxes i el repàs. Vegeu [`1eso/README.md`](1eso/README.md) |
| `comu/` | El que comparteixen els cursos: la closca de pantalla (`comu/css/web.css` i `comu/js/`), el registre de cursos (`comu/js/cursos.js`), la prova del mapa (`comu/eines/mapa.py`), el motor dels exàmens DOCX i la documentació general. Vegeu [`comu/README.md`](comu/README.md) |
| `index.html` | La portada: «Curs 2026-27», el títol i una columna per curs amb les seves unitats (i el botó «Professorat», ara amagat). La fa `comu/js/portada.js` |
| `other-versions/` | Dues versions de molta menys qualitat fetes amb una IA, per comparar-les amb aquest projecte. Només s'hi arriba des de `index.html?other-versions=1`. Es deixen tal com les va fer la IA, i per això la comprovació de l'anonimat no hi mira |
| `404.html` | La pàgina d'adreça equivocada. No redirigeix res: el mapa va començar de zero el 6/11/2026 |
| `_headers`, `robots.txt`, `favicon.svg` | El desplegament a Cloudflare Pages: vegeu [`comu/docs/DESPLEGAMENT.md`](comu/docs/DESPLEGAMENT.md) |
| `LICENSE`, `LLICENCIA.md` | Les llicències |
| `_uploads/`, `.github/` | La pujada de fitxers en zip des del web de GitHub, i les comprovacions automàtiques. Si es pugen dos zip seguits, el segon espera el primer; i si les comprovacions fallen, no es desa res i el zip es queda a `_uploads/`. Un zip no pot esborrar fitxers: per moure'n o esborrar-ne cal un commit des del Codespace |

---

## Com s'obre

Doble clic a `index.html`, o `https://pi.step-quiz.net/`. No cal servidor ni instal·lar res.

### El mapa (6/11/2026)

```
Inici (index.html)
 └ curs (4eso/index.html)
    └ Unitat N (4eso/uN/index.html) ── per al docent
       ├ 1 Fitxa (uN/fitxa.html, i a 1eso/ les altres fitxes de la unitat)
       ├ 2 Quadern d'activitats (uN/quadern.html), o «Quadern d'activitats no disponible»
       ├ 3 Repàs (uN/repas.html)
       ├ 4 Eines → 4eso/eines.html?u=N ── per a l'alumnat: un espai tancat, sense cap enllaç
       ├ 5 Targetes (targetes/NOM.html?u=N)
       └ Abans de la classe (plegat): el material, l'objectiu i la regla trencada
 Professorat (4eso/professorat.html): canviar les frases, llegir codis, les notes generals
   ── TANCAT des del 6/11/2026: vegeu més avall
```

- **La secció del professorat és tancada** (6/11/2026), però no s'ha esborrat: potser tornarà.
  No hi ha cap botó «Professorat», i `professorat.html`, `textos.html` i `verifica.html` porten a
  la pàgina del curs (amb `?obert` al final de l'adreça s'obren igualment). Per tornar-la a obrir,
  només cal canviar `PI.professorat = false;` per `true` a `comu/js/web.js`. Detalls a
  [`comu/docs/SITE-MAP.md`](comu/docs/SITE-MAP.md), «The teacher section is CLOSED».

- **Tota pàgina del docent** porta la mateixa capçalera violeta, `Inici › curs › Unitat N › pàgina`,
  i el botó «Professorat» (amagat mentre la secció és tancada). Cada fitxa, repàs, quadern i targeta hi té, a sobre del full, els
  botons «PDF alumnat» i «PDF solucionari» (o «PDF a doble cara»).
- **L'alumnat només obre les eines**, amb l'enllaç que el docent copia a la pàgina de la unitat
  («Copia l'enllaç»): `https://pi.step-quiz.net/4eso/eines?u=3`. Hi surten només les
  eines d'aquella unitat, i la capçalera no porta enlloc: així l'alumnat no pot arribar als
  solucionaris.
- **El nom de cada curs** només és a `comu/js/cursos.js`. Les pàgines el llegeixen d'allà.

**Si canvies el CSS o el JS**, no cal fer res més: `_headers` fa que el navegador els torni a
validar a cada visita (5/11/2026: amb una hora de memòria, la pàgina nova sortia amb l'estil vell).

Les eines poden llegir cada targeta en veu alta: el botó petit de l'altaveu, a dalt a la dreta de
la targeta. Quina veu sona millor a cada ordinador, als `README.md` de cada curs.

## On es publica

GitHub → Cloudflare Pages → `pi.step-quiz.net`, amb tots els camps del formulari buits: es publica
tot el repositori. Cloudflare treu el `.html` de les adreces (`/4eso/u3/fitxa`), però els enllaços
de dins porten sempre el nom del fitxer, perquè també funcioni amb doble clic.

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

Les set unitats ja tenen examen als dos cursos: `4eso/generadors/examens/ud1.js` a `ud7.js` i
`1eso/generadors/examens/ud1.js` a `ud7.js`. Els passos de sota serveixen per fer-ne un de nou
o per tornar a fer un examen que ja existeix.

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

Cada una ha de dir «Tot correcte.». Comproven les fitxes, les eines, el desplegament i el mapa
del lloc (`comu/eines/mapa.py`, que també es pot passar sol), i que cap fitxer del repositori
anomeni el curs, el tipus d'aula o un diagnòstic. Les excepcions són els noms de carpeta `4eso/` i
`1eso/`, que fan visible el curs a les adreces, i `comu/js/cursos.js`, l'únic lloc on és el nom
de cada curs.

**GitHub les passa soles** a cada pujada i a cada pull request (`.github/workflows/comprova.yml`).
A la pàgina del repositori, al costat de cada commit, surt una marca verda (tot correcte) o una
creu vermella: clicant-hi es veu quina comprovació ha fallat i per què. Funcionen amb Python
3.11 o més nou, sense instal·lar res.

Les proves que obren un navegador (Playwright) es passen a mà, abans de lliurar:

```bash
python3 1eso/eines/prova_caixa.py      # les eines de 1eso/, de punta a punta
python3 4eso/eines/prova_caixa.py      # les eines de 4eso/
python3 4eso/eines/prova_quadern.py    # el filtre dels quaderns d'activitats de 4eso/
python3 comu/eines/prova_portada.py    # tot el mapa, clicat en un navegador: portada, cursos, unitats, paper i eines
python3 1eso/eines/auditoria.py        # contrast, dianes i lletra al paper
python3 4eso/eines/auditoria.py
```

**Les còpies dels dos cursos.** La closca de pantalla és comuna (`comu/`), però cada curs encara té la seva còpia dels fitxers de les eines i del paper.
Per veure com s'han separat, i si un arreglament d'un curs també cal a l'altre:

```bash
python3 comu/eines/diferencies.py              # la taula
python3 comu/eines/diferencies.py js/codi.js   # un fitxer, línia a línia
```

---

<!-- atribucio-centre:inici -->

---

Material desenvolupat per **David Arso Civil** per al Departament de Matemàtiques de l'INS Miquel Tarradell.
Contingut sota CC BY-NC-SA 4.0, codi sota llicència MIT. Vegeu [`LLICENCIA.md`](LLICENCIA.md).

<!-- atribucio-centre:final -->
