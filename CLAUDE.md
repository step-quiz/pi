# CLAUDE.md — pi

<!-- regles-comunes:inici -->
## Regles comunes de Step Quiz

*Aquest bloc és igual a tots els repositoris de `step-quiz`. Les regles específiques d'aquest
repositori, si n'hi ha més avall, manen sobre aquestes quan diuen una altra cosa.*

- **Llengua.** Parla amb l'usuari en català. Tot el que veu l'alumnat, també en català.
- **L'usuari.** David, llicenciat en Matemàtiques i professor d'ESO i Batxillerat a Catalunya.
  Programa en C i dissenya algorismes; d'HTML, CSS, JS, Git, GitHub, Codespaces i LaTeX en sap
  el que cal per fer-los servir, no més. Quan hagi de fer alguna cosa (pull, push, commit, pujar
  un ZIP, compilar…), dona-li els passos numerats, amb les ordres o els textos per copiar i
  enganxar, i explica què fa cada pas.
- **ZIP.** Els ZIP que lliuris, l'usuari els puja a `_uploads/` (GitHub → `_uploads/` →
  *Add file* → *Upload files*), i el workflow `unzip-upload.yml` els descomprimeix a l'arrel i en
  fa commit. Per tant, les rutes de dins del ZIP comencen a l'arrel del repositori (`js/app.js`,
  no `projecte/js/app.js`): cap carpeta que ho contingui tot. El que hi hagi a `.github/` s'ignora;
  els workflows es canvien des del web de GitHub.
- **Publicació.** Els webs es publiquen amb Cloudflare Pages a cada commit de `main`. Cap missatge
  de commit pot portar `[skip ci]`, `[ci skip]` ni `[cf-pages-skip]`, tampoc els dels workflows
  que desen fitxers generats: Cloudflare no publicaria aquell commit.
- **Webs estàtiques.** HTML, CSS i JavaScript sense compilació ni servidor, si aquest repositori
  no diu el contrari. Cap dada personal de l'alumnat en un repositori públic.
- **Documentació.** Si canvies el comportament, posa al dia el README i els documents que el
  descriuen en el mateix commit. Si el codi i un document no coincideixen, el que s'ha
  d'arreglar és el document.
- **Proves.** Abans de lliurar res, passa les proves del repositori i digues-ne el resultat.
<!-- regles-comunes:fi -->

## Aquest repositori

**Material adaptat de matemàtiques.** Llegeix primer:

- [`README.md`](README.md)

**El mapa del lloc (no es trenca).** Llegeix [`comu/docs/SITE-MAP.md`](comu/docs/SITE-MAP.md) abans de
tocar cap pàgina: el mapa (Inici → curs → unitat `uN/` → fitxa, quadern o repàs; el professorat a
part; les eines de l'alumnat, `eines.html?u=N`, un espai tancat), els noms, el model de dades, la
closca comuna (`comu/css/web.css`, `comu/js/`), la barra de pantalla del paper i els errors que no
s'han de repetir. Una pàgina nova ha de sortir a `dades/unitats.js`, i `comu/eines/mapa.py` (dins de
cada `comprova.py`) ho vigila. El nom dels cursos només és a `comu/js/cursos.js`.

Proves (des de l'arrel del repositori):

```
python3 1eso/eines/comprova.py
python3 4eso/eines/comprova.py
python3 comu/eines/mapa.py            # el mapa del lloc (també dins de cada comprova.py)
python3 comu/eines/prova_portada.py   # tot el mapa, en un navegador (Playwright)
```

Si alguna comprovació falla, el workflow dels ZIP no desa res.

**Pull request.** Quan acabis una feina i n'hagis fet el push a la branca de treball, obre
sempre la pull request cap a `main`, sense preguntar-ho (ho va demanar l'usuari el 5/11/2026).
L'usuari la revisa i la fusiona. No la vigilis: no t'hi subscriguis ni ho ofereixis.
