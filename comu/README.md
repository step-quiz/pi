# comu

El que fan servir tots dos cursos, `4eso/` i `1eso/`. Si un curs necessita canviar-ne
alguna cosa que l'altre no vol, se'n fa una còpia a la carpeta d'aquell curs i l'original
no es toca.

| Fitxer | Què és |
|---|---|
| `js/portada.js` | La portada de l'arrel (`index.html`): una columna per curs amb les seves unitats |
| `js/unitat.js` | La pàgina de cada unitat (`1eso/unitat.html` i `4eso/unitat.html`): fitxes, targetes de consulta, quadern i caixa d'eines de la unitat, i el detall per al docent |
| `js/torna.js` | L'enllaç «← unitat N» de les targetes de consulta: les obre `unitat.js` amb `?ud=N`, i aquí es corregeix perquè tornin a la unitat d'on vénen |
| `eines/prova_portada.py` | Prova la portada i les 14 pàgines d'unitat en un navegador, i que cada fitxa, targeta, quadern i caixa torni a la seva unitat |
| `examens/nucli.js` | El motor dels exàmens DOCX. Cada curs hi posa el contingut a `generadors/examens/udN.js` |
| `docs/EXAMENS-DOCX.md` | Les regles i el procediment dels exàmens |
| `docs/DESPLEGAMENT.md` | Com es publica el repositori a Cloudflare Pages |
| `eines/diferencies.py` | Les diferències entre les còpies de `1eso/` i `4eso/`: quins fitxers s'han separat i com |

**Si toques el motor**, torna a generar l'examen de la UD1 de `4eso/` i comprova que surt
igual que abans.
