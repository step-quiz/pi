# Continuar

On és la feina de `1eso/` i què ve després. S'actualitza al final de cada sessió de treball.

---

## 1. Què hi ha (23 de setembre de 2026)

- **L'esquelet**: fulls d'estil, portada, dades de les set unitats i documentació.
- **Les eines**: el test (`eines/comprova.py`), la mesura de l'A4 (`eines/mesura.py`) i el
  generador de PDF (`generadors/gen_pdf.py`), que comparteixen `eines/paper.py`.
- **La lletra manuscrita dins del repositori**: `fonts/Caveat.ttf`, amb la llicència
  `fonts/OFL.txt`. És la mateixa dels exàmens DOCX.
- **La primera targeta de consulta**: les taules de multiplicar, en dues cares
  (`targetes/taules.html` i `pdf/targeta-taules.pdf`).
- **Cap fitxa encara.**

---

## 2. Què s'ha verificat, i com

| Afirmació | Com s'ha verificat | Confiança |
|---|---|---|
| Les dues cares de la targeta caben en un A4 | `mesura.py`: 25,4 cm de 27,1 a cada cara | Alta |
| El PDF porta la lletra manuscrita | `gen_pdf.py` llegeix quines lletres hi ha dins del PDF: Caveat, DejaVu Sans i DejaVu Sans Bold | Alta |
| Les cent multiplicacions són correctes | `comprova.py` les refà totes | Alta |
| El test detecta el que ha de detectar | Quinze errors introduïts a posta, un per un: els quinze surten | Alta |
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

---

## 4. Pendent

1. **Imprimir la targeta** i dir què s'hi ha de canviar.
2. **Validar el nucli de la unitat 1** ([`MAPA-ADAPTACIO.md`](MAPA-ADAPTACIO.md), apartat 4), i
   després escriure la fitxa `fitxes/ud1.html` amb el seu solucionari.
3. **La portada de l'arrel del repositori.** Ara porta a `4eso/`. Quan hi hagi la primera fitxa,
   ha de deixar triar el curs, i `_headers` ha de tenir les línies de memòria cau de `/1eso/`.
   Són fitxers de l'arrel, fora d'aquesta carpeta: ho decideix el docent.
4. **Si mai hi ha caixa d'eines** en aquesta carpeta: les claus que es desen al navegador han de
   començar per `pi1-` i la sal de `codi.js` ha de ser una altra que la de `4eso/`. Les dues
   caixes es publiquen al mateix domini: si no, compartirien la memòria del navegador, i un codi
   de verificació de l'una es llegiria com a vàlid a l'altra.

---

## 5. Com es treballa

- **Tot el que es lliura és un ZIP amb la carpeta `1eso/` a dins.** Es puja a `_uploads/` des del
  web de GitHub i l'acció del repositori el descomprimeix a l'arrel. Després, al Codespace,
  `git pull`.
- **Abans de lliurar res**, des de l'arrel del repositori:

  ```bash
  python3 1eso/eines/comprova.py
  python3 1eso/eines/mesura.py
  python3 1eso/generadors/gen_pdf.py
  python3 4eso/eines/comprova.py
  ```

  El primer i l'últim no necessiten res. Els dos del mig necessiten WeasyPrint
  (`pip install weasyprint --break-system-packages`).
- **El paper mana.** El que es veu en pantalla no garanteix res: el que compta és el que surt
  de la impressora.
