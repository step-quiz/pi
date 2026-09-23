# Mapa d'adaptació

Com es passa de la programació del grup al material d'aquesta carpeta. Les regles concretes
del paper són a [`CRITERIS-DISSENY.md`](CRITERIS-DISSENY.md); aquí hi ha el perquè i el pla.

Material per a alumnat amb dificultats de tipus cognitiu, sobretot de memòria i de raonament
lògic. No hi consta res més, ni ha de constar-hi: el repositori es publica.

---

## 1. El punt de partida

Es descriu com a regles del material, no com a retrat de ningú.

| Què | El material ho resol així |
|---|---|
| **Nombres** | Es llegeixen i s'escriuen bé fins al 999. Cap nombre de l'alumnat no en passa |
| **Càlcul** | Sumes i restes sense portar-ne. Si un càlcul en necessita, es canvien les dades |
| **Taules de multiplicar** | Sempre al davant, a la targeta. Una taula apresa es pot perdre en pocs dies |
| **Lectura** | Frases simples, amb una sola consigna cadascuna |
| **Memòria** | Res no es demana de memòria: el que cal recordar és a les targetes de consulta, que s'acumulen |
| **Raonament lògic** | La regla trencada es desmunta amb el dibuix o el material, mai amb un argument |
| **Símbol de multiplicar** | Coneixen «3 × 4» de primària. El grup fa servir «3 · 4», i el material també |

---

## 2. Les dues aules

La meitat de les hores de matemàtiques són a l'aula de suport i l'altra meitat a l'aula
ordinària.

| | Aula de suport | Aula ordinària |
|---|---|---|
| Qui | Dos professionals de suport | El docent de matemàtiques, amb codocència quan n'hi ha |
| Què s'hi fa | El graó físic, la part de concepte de la fitxa i la consolidació | Els exercicis de la fitxa, al mateix temps que el grup |
| Calculadora | Sí, però només per comprovar | No, perquè no hi hagi greuge |
| Targeta de les taules | Sí | Sí: la programació ja la preveu per a tothom |

**L'aula de suport va per davant.** La idea es toca amb material abans que arribi a l'aula
ordinària. Com que la memòria és fràgil, també hi va per darrere: cada sessió comença mirant la
targeta de l'última vegada.

---

## 3. El model de tot el curs: la quadrícula

Un sol dibuix per a tot el curs, i la recta numèrica com a segon (per a l'ordre, els múltiples
com a salts, els decimals i l'arrodoniment). Amb el material que hi ha a l'aula: miniblocs,
quadrícules i geoplà.

| Unitat | Què és la quadrícula | Material |
|---|---|---|
| 1 | Multiplicar és fer un rectangle de quadrets. El quadrat d'un nombre és un quadrat de quadrets | Miniblocs |
| 2 | Els divisors d'un nombre surten dels rectangles que es poden fer amb aquells quadrets. Un primer només en fa un | Miniblocs |
| 3 | L'àrea és comptar quadrets. Mig quadret és 1/2 | Quadrícula |
| 4 | Una fracció d'un nombre és repartir quadrets en grups iguals. Un percentatge és quants quadrets de cada 100 | Miniblocs i quadrícula de 100 |
| 5 | A la quadrícula de 100, una columna és 0,1 i un quadret és 0,01. L'arrel és el costat del quadrat | Quadrícula de 100 i miniblocs |
| 6 | Polígons al geoplà. El perímetre és comptar costats de quadret | Geoplà |
| 7 | Patrons de quadrets: quants en té la figura següent | Miniblocs |

La programació del grup ja fa servir aquest objecte: mapes quadriculats a la unitat 3,
rectangles de 10 per 10 a la 4, quadrats de cartolina a la 5 i geoplans a la 6.

---

## 4. Unitat per unitat

Una unitat per situació d'aprenentatge del grup, amb els mateixos números i títols. El nucli de
cada una és una **proposta**: es valida amb el docent abans d'escriure la fitxa. Les dades són
a [`../dades/unitats.js`](../dades/unitats.js), que és el que llegeix la portada.

| Unitat | Dates del grup | Sessions | Criteris de la SA (referència) | Estat |
|---|---|---|---|---|
| 1 · Nombres naturals | des del 9 de setembre | 13 i un examen | 1.3, 2.1, 8.1 | Targeta de les taules feta. Fitxa per fer |
| 2 · Divisibilitat | 3–19 de novembre | 11 | 1.4, 3.2, 4.2, 5.2 | Per fer |
| 3 · Com és de gran Gaza? | 23 de novembre – 18 de desembre | 15 | 1.2, 5.2, 6.1, 9.1 | Per fer |
| 4 · És gran l'ou del kiwi? | 12–28 de gener | 11 | 1.3, 2.1, 5.1, 6.1 | Per fer |
| 5 · Decimals i arrel quadrada | 1–15 de març | 7 | 5.1, 7.1, 8.1 | Per fer |
| 6 · Sentit espacial | 5 d'abril – 10 de maig | 16 | 1.1, 3.1, 5.1, 6.1, 7.1, 9.1 | Per fer |
| 7 · Patrons i llenguatge algebraic | 19 de maig – 1 de juny | 6 | 2.1, 3.1, 4.1, 5.1, 7.2 | Per fer |

Els codis dels criteris són els de les SA del departament, i quadren, codi i text, amb la llista
oficial que porta la plantilla del Departament d'Educació. L'avaluació d'aquest alumnat es fa
amb els criteris propis del PI.

Les SA del grup són ambicioses (conjectures, algorismes, fraccions amb multiplicació i divisió,
decimals periòdics). De cada una només s'agafa el nucli. La resta no es rebaixa: no hi és.

---

## 5. L'avaluació

Amb els criteris del PI. Cada solucionari acaba amb «Què mirar per avaluar»: accions que es
veuen, sempre amb la targeta al davant, escrites perquè es puguin passar al PI tal com són.

Mai no s'avalua el que es recorda, sinó el que es fa amb la targeta al davant.

---

## 6. Els exàmens

Quan en calguin, amb el motor comú, [`../../comu/examens/nucli.js`](../../comu/examens/nucli.js),
i les regles de [`../../comu/docs/EXAMENS-DOCX.md`](../../comu/docs/EXAMENS-DOCX.md). El contingut
va a `generadors/examens/udN.js` i les dades privades, a `generadors/examens-privat.json`, que el
`.gitignore` de l'arrel ja deixa fora.
