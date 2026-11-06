# comu

El que fan servir tots els cursos (`1eso/`, `4eso/` i els que vinguin). El mapa del lloc, la
closca de pantalla i les seves regles són a [`docs/SITE-MAP.md`](docs/SITE-MAP.md), en anglès.

| Fitxer | Què és |
|---|---|
| `css/web.css` | La closca de pantalla de tots els cursos: colors, botons, la capçalera violeta, el tick del que està triat. Totes les classes comencen per `w-` |
| `js/cursos.js` | El registre de cursos: l'únic fitxer amb el nom de cada curs |
| `js/web.js` | Les peces comunes dels scripts de pantalla (icones, botons, capçalera, curs escolar…) |
| `js/portada.js` | La portada de l'arrel (`index.html`) |
| `js/curs.js` | La pàgina de cada curs (`CURS/index.html`) |
| `js/unitat.js` | La pàgina de cada unitat (`CURS/uN/index.html`), per al docent |
| `js/professorat.js` | La pàgina del professorat i la capçalera de `textos.html` i `verifica.html` |
| `js/paper.js` | La capçalera de les fitxes, els repassos, el quadern i les targetes, amb els botons dels PDF |
| `js/alumne.js` | La capçalera tancada de les eines de l'alumnat (`CURS/eines.html?u=N`) |
| `eines/unitat.html` | La pàgina d'unitat de referència: tots els `CURS/uN/index.html` en són una còpia exacta |
| `eines/mapa.py` | La prova del mapa del lloc. La criden els `comprova.py` dels cursos |
| `eines/prova_portada.py` | Clica tot el mapa en un navegador: portada, cursos, unitats, paper i eines |
| `examens/nucli.js` | El motor dels exàmens DOCX. Cada curs hi posa el contingut a `generadors/examens/udN.js` |
| `docs/SITE-MAP.md` | El mapa, el model de dades, la closca, com s'afegeix un curs i els errors que no s'han de repetir |
| `docs/EXAMENS-DOCX.md` | Les regles i el procediment dels exàmens |
| `docs/DESPLEGAMENT.md` | Com es publica el repositori a Cloudflare Pages |
| `eines/diferencies.py` | Les diferències entre les còpies de `1eso/` i `4eso/`: quins fitxers s'han separat i com |

**Si toques el motor**, torna a generar l'examen de la UD1 de `4eso/` i comprova que surt
igual que abans.
