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
- **Els tests de la caixa**: `comprova.py` la revisa per dins, i dos tests nous la fan servir en
  un navegador: `eines/prova_caixa.py` (que funcioni) i `eines/auditoria.py` (accessibilitat).
- **La portada** enllaça la caixa i té els enllaços `?task=n` per a l'alumnat.
- **La subtasca 0.3**, el número que falta (24 de setembre de 2026), i els enllaços a un exercici
  concret sense fletxes per passar als altres.
- **La 0.1 i la 3.1, més lleugeres** (24 de setembre de 2026): a la 0.1 els dos números es trien
  amb pastilles i tota la taula és plegada darrere d'un botó; a la 3.1 el dibuix ja no repeteix
  els rètols dels comptadors.
- **Un esborrany de la fitxa de la unitat 1**, només amb rectangles i quadrats, per veure com
  queda: 9 pàgines i 3 de solucionari. **Encara no és al repositori**: primer l'ha de mirar el
  docent. Vegeu l'apartat 4.

---

## 2. Què s'ha verificat, i com

| Afirmació | Com s'ha verificat | Confiança |
|---|---|---|
| Les dues cares de la targeta caben en un A4 | `mesura.py`: 25,4 cm de 27,1 a cada cara | Alta |
| El PDF porta la lletra manuscrita | `gen_pdf.py` llegeix quines lletres hi ha dins del PDF: Caveat, DejaVu Sans i DejaVu Sans Bold | Alta |
| Les cent multiplicacions de la targeta són correctes | `comprova.py` les refà totes | Alta |
| El test detecta el que ha de detectar | Quinze errors introduïts a posta, un per un: els quinze surten | Alta |
| La caixa funciona de punta a punta | `prova_caixa.py`, a Chromium: les catorze subtasques; les sis tasques tancades amb encert, pista i resposta ensenyada; els sis codis llegits a `verifica.html`; la represa; els enllaços `?task=`; cap error de JavaScript | Alta |
| Cap frase de la caixa trenca les regles del curs | `comprova.py`: 186 frases, totes amb explicació; Lectura Fàcil; cap «×»; cap nombre de més de 999 | Alta |
| Les dades dels mòduls compleixen les regles | `prova_caixa.py`: sumes sense portar-ne, multiplicacions de la targeta, i els noms dels nombres de l'1 al 999 | Alta |
| Els tests de la caixa detecten el que han de detectar | Onze errors introduïts a posta, un per un (una «×», un 1000, una frase de 21 paraules, una clau que no existeix, la sal de l'altra caixa…): els onze surten | Alta |
| La caixa és accessible (WCAG 2.2 AA) | `auditoria.py`: 0 problemes en 88 estats, en clar i en fosc, a 320 i a 1100 px | Alta |
| La caixa es veu bé | Captures al mòbil i a l'ordinador, en clar i en fosc, mirades una per una | Mitjana: no substitueix veure-la fer servir |
| El test de `4eso/` continua dient «Tot correcte.» amb aquesta carpeta al repositori | Passat amb la carpeta ja posada | Alta |
| La targeta es llegeix bé en paper | Vista en pantalla, a partir del PDF. **El paper encara no** | Pendent |

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

1. **Imprimir la targeta** i dir què s'hi ha de canviar.
2. **Provar la caixa a l'aula** i dir què s'hi ha de canviar. Els enllaços per a l'alumnat són a
   la portada, a «Caixa d'eines».
3. **La fitxa de la unitat 1.** Hi ha un esborrany (rectangles i quadrats) que el docent ha de
   mirar. Quan el validi, entra al repositori com a `fitxes/ud1.html`, la unitat 1 de
   `dades/unitats.js` passa a tenir `fitxa: "fitxes/ud1.html"`, i els dos PDF definitius
   (`ud1-alumnat.pdf` i `ud1-solucionari.pdf`) es fan al Codespace amb `generadors/gen_pdf.py`,
   que necessita WeasyPrint. Fins que no hi siguin, `comprova.py` diu que falten, i és correcte.
4. **L'examen de la unitat 1** en DOCX, amb el motor comú.
5. **La revisió externa del 24 de setembre de 2026: tot decidit.** Aplicat: la 0.3; els
   enllaços a un exercici concret, sense fletxes; la fitxa només amb rectangles i quadrats; al
   solucionari, una acció per dir en veu alta («3 files de 4 quadrets»); la 0.1 amb tota la taula
   plegada, i la 3.1 sense repeticions (regla W). Decidit que no, de moment: que `verifica.html`
   ensenyi l'evolució de diversos codis d'una mateixa tasca. No es fan, i la revisió hi està
   d'acord: les tasques d'ampliació per a qui acaba abans, i qualsevol seguiment digital amb nom.
6. **L'arrel del repositori.** La portada de l'arrel porta a `4eso/`, `_headers` no té les línies
   de memòria cau de `/1eso/`, i la fila de `1eso/` del `README.md` de l'arrel encara diu «quan
   es faci». Són fitxers de l'arrel, fora d'aquesta carpeta: ho decideix el docent.

---

## 5. Com es treballa

- **Tot el que es lliura és un ZIP amb la carpeta `1eso/` a dins.** Es puja a `_uploads/` des del
  web de GitHub i l'acció del repositori el descomprimeix a l'arrel. Després, al Codespace,
  `git pull`.
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
