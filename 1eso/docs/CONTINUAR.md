# Continuar

On és la feina de `1eso/` i què ve després. S'actualitza al final de cada sessió de treball.

---

## 1. Què hi ha (24 de setembre de 2026)

- **L'esquelet**: fulls d'estil, portada, dades de les set unitats i documentació.
- **Les eines**: el test (`eines/comprova.py`), la mesura de l'A4 (`eines/mesura.py`) i el
  generador de PDF (`generadors/gen_pdf.py`), que comparteixen `eines/paper.py`.
- **La lletra manuscrita dins del repositori**: `fonts/Caveat.ttf`, amb la llicència
  `fonts/OFL.txt`. És la mateixa dels exàmens DOCX.
- **La primera targeta de consulta**: les taules de multiplicar, en dues cares
  (`targetes/taules.html` i `pdf/targeta-taules.pdf`).
- **La caixa d'eines de la unitat 1** (`caixa-eines.html`): cinc eines (taules, rectangles,
  quadrats, nombres i ordre de les operacions), catorze subtasques i sis tasques tancades amb
  codi de verificació. Amb `verifica.html`, per llegir els codis, i `textos.html`, per canviar
  les frases. Com està feta: [`ARQUITECTURA.md`](ARQUITECTURA.md). Per què és així:
  [`CRITERIS-DISSENY.md`](CRITERIS-DISSENY.md), apartat 3. Què fa de cada activitat del grup:
  [`MAPA-ADAPTACIO.md`](MAPA-ADAPTACIO.md), apartat 5.
- **La caixa d'eines de la unitat 2**, a la mateixa pàgina: quatre eines més (múltiples,
  repartir, divisors i primers), deu subtasques i cinc tasques tancades (5.2, 5.4, 6.2, 7.2 i
  8.2). Són les tasques 5 a 8. En total, la caixa té 24 subtasques i onze tasques tancades.
- **Les cinc fitxes de la unitat 2**: els múltiples (`fitxes/ud2.html`), repartir en files
  (`ud2-repartir.html`), divisors i primers (`ud2-divisors.html`), la factorització
  (`ud2-factors.html`) i el repàs amb «Què he après?» (`ud2-repas.html`). I l'**examen de la
  unitat 2** (`generadors/examens/ud2.js`): vuit exercicis en 4 pàgines, i el solucionari en 2.
  La unitat 2 és acabada; només en falten els PDF
  ([`MAPA-ADAPTACIO.md`](MAPA-ADAPTACIO.md), apartat 6).
- **Els tests de la caixa**: `comprova.py` la revisa per dins, i dos tests nous la fan servir en
  un navegador: `eines/prova_caixa.py` (que funcioni) i `eines/auditoria.py` (accessibilitat).
- **La portada** enllaça la caixa i té els enllaços `?task=n` per a l'alumnat.
- **La subtasca 0.3**, el número que falta (24 de setembre de 2026), i els enllaços a un exercici
  concret sense fletxes per passar als altres.
- **La 0.1 i la 3.1, més lleugeres** (24 de setembre de 2026): a la 0.1 els dos números es trien
  amb pastilles i tota la taula és plegada darrere d'un botó; a la 3.1 el dibuix ja no repeteix
  els rètols dels comptadors.
- **Quatre fitxes de la unitat 1.** La 1 (`fitxes/ud1.html`), rectangles i quadrats: 9 pàgines i 3
  de solucionari, validada pel docent el 24 de setembre de 2026, amb la lletra manuscrita dels
  exemples resolts un 30% més gran. La 2 (`fitxes/ud1-nombres.html`), centenes, desenes i
  unitats, per a l'activitat 1_7 del grup: 6 pàgines i 2 de solucionari. La 3
  (`fitxes/ud1-ordre.html`), l'ordre de les operacions, per a l'activitat 1_14: 6 pàgines i 2 de
  solucionari. La 4 (`fitxes/ud1-repas.html`), el repàs i «Què he après?», per a les activitats
  1_1, 1_3, 1_5, 1_15 i 1_16: 6 pàgines i 2 de solucionari. **Encara no tenen els PDF**: vegeu
  l'apartat 4.
- **L'examen de la unitat 1** (`generadors/examens/ud1.js`), en DOCX amb el motor comú: deu
  exercicis en 6 pàgines, i el solucionari en 3. Els DOCX surten a `docx/`, que no es puja.
  Per fer-lo possible, el motor comú (`comu/examens/nucli.js`) accepta ara la matèria, l'autor
  del fitxer i l'avís (el de la targeta, en lloc del de la calculadora). Les que falten de la unitat són a
  [`MAPA-ADAPTACIO.md`](MAPA-ADAPTACIO.md), apartat 5.

---

## 2. Què s'ha verificat, i com

| Afirmació | Com s'ha verificat | Confiança |
|---|---|---|
| Les dues cares de la targeta caben en un A4 | `mesura.py`: 25,4 cm de 27,1 a cada cara | Alta |
| El PDF porta la lletra manuscrita | `gen_pdf.py` llegeix quines lletres hi ha dins del PDF: Caveat, DejaVu Sans i DejaVu Sans Bold | Alta |
| Les cent multiplicacions de la targeta són correctes | `comprova.py` les refà totes | Alta |
| El test detecta el que ha de detectar | Quinze errors introduïts a posta, un per un: els quinze surten | Alta |
| La caixa funciona de punta a punta | `prova_caixa.py`, a Chromium: les 32 subtasques; les quinze tasques tancades amb encert, pista i resposta ensenyada; els quinze codis llegits a `verifica.html`; la represa; els enllaços `?task=`; cap error de JavaScript. De la unitat 2, a més: que els casos siguin de la targeta, que la suma de les xifres del criteri del 3 doni de l'1 al 30, que els senars de la 8.2 no siguin primers, el garbell pas a pas i els singulars («En sobra 1.», «L'11») | Alta |
| Cap frase de la caixa trenca les regles del curs | `comprova.py`: 186 frases, totes amb explicació; Lectura Fàcil; cap «×»; cap nombre de més de 999 | Alta |
| Les dades dels mòduls compleixen les regles | `prova_caixa.py`: sumes sense portar-ne, multiplicacions de la targeta, i els noms dels nombres de l'1 al 999 | Alta |
| Els tests de la caixa detecten el que han de detectar | Onze errors introduïts a posta, un per un (una «×», un 1000, una frase de 21 paraules, una clau que no existeix, la sal de l'altra caixa…): els onze surten | Alta |
| La caixa és accessible (WCAG 2.2 AA) | `auditoria.py`: 0 problemes en 180 estats (la caixa, les dues portades i les pàgines de codis i de frases), en clar i en fosc, a 320 i a 1100 px | Alta |
| La caixa es veu bé | Captures al mòbil i a l'ordinador, en clar i en fosc, mirades una per una | Mitjana: no substitueix veure-la fer servir |
| El test de `4eso/` continua dient «Tot correcte.» amb aquesta carpeta al repositori | Passat amb la carpeta ja posada | Alta |
| La targeta es llegeix bé en paper | Vista en pantalla, a partir del PDF. **El paper encara no** | Pendent |
| Les fitxes compleixen les regles del paper | `comprova.py`: blanc i negre, HTML, numeració, graó físic, obertura, pàgina de la vida, solucionari, Lectura Fàcil, fins a 999, «·», cap igualtat malament i els caràcters de la lletra manuscrita | Alta |
| Cap igualtat escrita està malament | `comprova.py` calcula cada igualtat sencera, amb l'ordre de les operacions: 217 a les cinc fitxes de paper. Les que l'alumnat ha de revisar, i que poden ser falses a posta (les multiplicacions mal fetes de la fitxa 4), van dins de `.revisa` i no es comproven. Vuit errors introduïts a posta, un per un (7 · 8 = 57 a la targeta, 2 + 3 · 4 = 20, (2 + 3) · 4 = 14, √16 = 5…): els sis dolents surten, i els dos bons (un error ratllat a posta i un buit per escriure) passen | Alta |
| Cada pàgina de les fitxes cap en un A4 | Mesurades amb Chromium i la geometria de `eines/paper.py`: la més alta fa 25,8 cm de 27,1. Chromium i WeasyPrint difereixen 1 mm a la targeta (25,3 i 25,4 cm). **La mesura bona és la de `mesura.py`**, que necessita WeasyPrint | Mitjana, fins que passi `mesura.py` |
| L'examen és correcte | Les 46 igualtats dels dos DOCX (9 a l'alumnat i 37 al solucionari), calculades amb l'ordre de les operacions: cap de malament. Cap nombre de més de 999, cap «×», totes les multiplicacions de la targeta i cap frase de més de 20 paraules. El motor avisa si falta algun apartat, si hi ha color o si surt «adaptat»: cap avís | Alta |
| L'examen es veu bé | Passat a PDF amb LibreOffice i mirat pàgina a pàgina: cada exercici sencer a la seva pàgina, cap taula partida. Aquí no hi ha Verdana ni Nova Mono, i s'hi posen unes altres: la mida bona és la de Google Docs | Mitjana |
| El motor canviat no canvia l'examen de `4eso/` | L'examen de `4eso/` fet abans i després del canvi: el mateix text, els mateixos dibuixos i les mateixes propietats, llevat de les dates | Alta |
| Canviar `.ms` no canvia la targeta | La targeta dibuixada abans i després del canvi: cap píxel diferent. El seu PDF, però, s'ha de tornar a fer, perquè `css/fitxa.css` forma part de l'empremta | Alta |

---

## 3. El que només pot verificar el docent

| Què | Com |
|---|---|
| Que a doble cara les dues cares quedin bé l'una darrere l'altra | Imprimir `pdf/targeta-taules.pdf` a doble cara, girant per la vora llarga |
| Que el «56» de la cara 2 sembli escrit a mà | Mirar-lo en paper |
| Que la clau del punt («3 × 4 és el mateix que 3 · 4») s'entengui | A l'aula de suport, en el primer ús |
| Que la línia entre la cinquena i la sisena fila ajudi a trobar la fila | A l'aula, amb el dit |
| Que s'entengui què s'ha de tocar a cada eina | A l'aula, la primera vegada que es fa servir cada una |
| Que cinc passos per tasca tancada sigui la mida bona | A l'aula |
| Que les pistes ajudin de debò | Mirant què es fa just després d'una pista |
| Que el dibuix de la 1.4 es llegeixi a l'aparell de classe. Al mòbil queda petit, tot i que la lectura de sota ho repeteix en lletra gran | Amb l'aparell de classe |
| Que el punt de multiplicar surti rodó. A les captures de l'entorn de proves sortia quadrat, per la lletra que hi havia instal·lada | Mirant-lo a l'aparell de classe |

---

## 4. Pendent

1. **Treure del repositori els dos DOCX de l'examen de la unitat 1**, que hi van quedar el 25 de
   setembre de 2026 a `generadors/examens/`. Tot el repositori es publica al web, i s'hi podrien
   obrir l'examen i el solucionari abans de l'examen. Són la versió anònima, sense cap dada
   privada. `comprova.py` ho avisa fins que no hi siguin.
2. **Imprimir la targeta** i dir què s'hi ha de canviar.
3. **Provar la caixa a l'aula** i dir què s'hi ha de canviar. Els enllaços per a l'alumnat són a
   la portada, a «Per al professorat».
4. **Els PDF de les cinc fitxes de la unitat 2**, al Codespace, amb `eines/mesura.py` i
   `generadors/gen_pdf.py`, que necessiten WeasyPrint. Els de la unitat 1 i el de la targeta ja
   hi són (25 de setembre de 2026). Fins que es facin els de la unitat 2, `comprova.py` en diu
   deu problemes, i és el que toca. Després, imprimir-les i mirar
   si les quadrícules i les graelles de 100 es poden pintar bé a mà.
5. **Revisar l'examen de la unitat 1** a Google Docs. Si es vol amb el curs a la capçalera,
   es fa al Codespace amb el fitxer privat (vegeu el `README.md`, «L'examen»).
6. **La unitat 2 (Divisibilitat), del 3 al 19 de novembre: feta.** La caixa (tasques 5 a 8), les
   cinc fitxes i l'examen. Falta: provar-la a l'aula, fer-ne els PDF (punt 4) i revisar l'examen
   a Google Docs.
   **La unitat 4 (les fraccions del grup), del 12 al 28 de gener.** El pla és validat (26/9/2026) i
   la caixa hi és (tasques 9 a 12), i la targeta «Els noms de les fraccions» (`targetes/fraccions.html`)
   també: cal fer-ne el PDF amb `gen_pdf.py`, imprimir-la a doble cara i plastificar-la. Falten les cinc fitxes
   (amb el full que explica per què 1/2 + 1/4 no pot donar 2/6) i l'examen
   ([`MAPA-ADAPTACIO.md`](MAPA-ADAPTACIO.md), apartat 7). La unitat 3 espera les activitats del grup.
7. **Per decidir: la lletra petita de la fitxa 1.** La regla 3 demana 14 pt com a mínim. A la
   fitxa 1 hi ha rètols de 12 pt a la pàgina 5 i dues línies de 13 pt a les pàgines 8 i 9; i, des
   de `css/fitxa.css`, les capçaleres de les taules a 11 pt i els rètols de les caixes per escriure
   a 11,5 pt. Les fitxes 2, 3 i 4 ja són totes a 14 pt com a mínim, amb `.mini` a les taules.
   Canviar-ho a la fitxa 1 la canviaria una mica, i ja està validada.
8. **La revisió externa del 24 de setembre de 2026: tot decidit.** Aplicat: la 0.3; els
   enllaços a un exercici concret, sense fletxes; la fitxa només amb rectangles i quadrats; al
   solucionari, una acció per dir en veu alta («3 files de 4 quadrets»); la 0.1 amb tota la taula
   plegada, i la 3.1 sense repeticions (regla W). Decidit que no, de moment: que `verifica.html`
   ensenyi l'evolució de diversos codis d'una mateixa tasca. No es fan, i la revisió hi està
   d'acord: les tasques d'ampliació per a qui acaba abans, i qualsevol seguiment digital amb nom.
9. ~~**L'arrel del repositori.**~~ **RESOLT · 25 de setembre de 2026.** La portada de l'arrel
   (`index.html`) ara deixa triar entre els dos materials. Els títols hi diuen el curs: el
   docent ho va decidir el 26/9/2026, perquè allà no cal amagar-lo. És l'única pàgina on surt, i
   el test de `4eso/` en té l'excepció. Cada portada de material, al seu torn, deixa
   triar entre «Fitxes» i «Caixa d'eines», amb la resta d'enllaços (frases, codis, enllaços per a
   l'alumnat, documentació) sota «Per al professorat». `1eso/fitxes.html` és nou: hi ha les
   targetes de consulta i les set unitats, que abans eren a la portada. `_headers` ja té les
   línies de memòria cau de `/1eso/`, i la fila de `1eso/` del `README.md` de l'arrel ja no diu
   «quan es faci». Els enllaços per a l'alumnat, a «Per al professorat», van agrupats per unitat.

---

## 5. Com es treballa

- **Tot el que es lliura és un ZIP amb la carpeta `1eso/` a dins.** Es puja a `_uploads/` des del
  web de GitHub i l'acció del repositori el descomprimeix a l'arrel. Després, al Codespace,
  `git pull`.
- **El ZIP no porta mai la carpeta `pdf/`.** Els PDF es fan al Codespace amb `gen_pdf.py`, i un
  ZIP que en portés una còpia vella els trepitjaria.
- **Abans de lliurar res**, des de l'arrel del repositori:

  ```bash
  python3 1eso/eines/comprova.py
  python3 1eso/eines/prova_caixa.py
  python3 1eso/eines/auditoria.py
  python3 1eso/eines/mesura.py
  python3 1eso/generadors/gen_pdf.py
  python3 4eso/eines/comprova.py
  ```

  El primer i l'últim no necessiten res. Els dos de la caixa necessiten Playwright, i els dos del
  paper, WeasyPrint: com s'instal·len és al [`README.md`](../README.md). Si només s'ha tocat la
  caixa, n'hi ha prou amb els tres primers i l'últim. Si només s'ha tocat el paper, amb el
  primer, els dos del paper i l'últim.
- **El paper mana.** El que es veu en pantalla no garanteix res: el que compta és el que surt
  de la impressora.
- **Les claus `pi1-` i la sal de `js/codi.js` no es canvien.** Les dues caixes es publiquen al
  mateix domini: sense les claus pròpies compartirien la memòria del navegador, i canviar la
  sal faria que els codis ja donats deixessin de valer.
