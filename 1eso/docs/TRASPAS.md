# Traspàs: com continuar la carpeta `1eso/` (unitats 5 a 7)

Escrit el 26 de setembre de 2026 per la IA que va fer les unitats 1, 2 i 3, i posat al dia el 28 de
setembre de 2026 amb la unitat 4, perquè una altra conversa, que comença de zero, pugui fer les
unitats 5, 6 i 7 amb el mateix mètode i la mateixa qualitat. Llegeix-lo sencer abans de tocar res. Després llegeix, per aquest ordre:
[`CONTINUAR.md`](CONTINUAR.md), [`MAPA-ADAPTACIO.md`](MAPA-ADAPTACIO.md),
[`CRITERIS-DISSENY.md`](CRITERIS-DISSENY.md), [`ARQUITECTURA.md`](ARQUITECTURA.md), el
[`README.md`](../README.md) de `1eso/` i [`comu/docs/EXAMENS-DOCX.md`](../../comu/docs/EXAMENS-DOCX.md).

---

## 1. Qui, què i com hi treballa el docent

- **El docent** és professor de Matemàtiques a Catalunya. Parla en català: respon-li sempre en
  català. Entén l'anglès, però el material és en català.
- **El material** és per a l'alumnat amb dificultats de tipus cognitiu del grup, a l'aula de
  suport i a l'ordinària. El mateix contingut que el grup, unitat per unitat, amb tres regles:
  un sol dibuix per a tot el curs (la quadrícula de quadrets), res que s'hagi de recordar de
  memòria (és a les targetes de consulta) i cap exercici que necessiti la calculadora.
- **Com treballa:** li agrada que li proposis un pla i que el validi abans de construir. Fes-li
  **com a molt tres preguntes** per decisió, amb l'eina de preguntes de botons, i deixa-li triar.
  Quan decideix, apunta la decisió amb la data a `MAPA-ADAPTACIO.md`.
- **El repositori:** GitHub, publicat al web amb Cloudflare Pages. El docent **no** fa servir la
  línia d'ordres amb soltura (nivell mitjà en Git, HTML, CSS i JS). Tot el que hagi de fer al
  Codespace (pull, commit, push, esborrar fitxers, fer PDF) s'ha d'explicar pas a pas, amb el
  text **per copiar i enganxar**.
- **Com puja la feina:** tu li lliures un **ZIP**; ell el puja a la carpeta `_uploads` del
  repositori, i una acció de GitHub el descomprimeix a l'arrel i en fa el commit. El ZIP s'ha de
  poder descomprimir amb l'estructura de carpetes bona (`1eso/...`, `comu/...`). Li has de dir el
  missatge del commit i que esperi la marca verda a **Actions**.
- **Un ZIP no pot esborrar fitxers.** Si canvies un nom o treus un fitxer, dona-li l'ordre
  `git rm --ignore-unmatch ...` per al Codespace, i simula-la abans (apartat 6).
- **El descans:** si veus que són entre les 23 h i les 7 h, digues-li-ho una vegada, amb tacte,
  al final de la resposta, i continua fent la feina.

## 2. On som (29/9/2026)

| Unitat | Estat |
|---|---|
| 1 · Nombres naturals | Feta: caixa (tasques 0 a 4), quatre fitxes, targeta de les taules, examen. PDF fets |
| 2 · Divisibilitat | Feta: caixa (5 a 8), cinc fitxes, examen. PDF fets |
| 3 · Com és de gran Gaza? | Feta: caixa (9 a 13), set fitxes (l'àrea, les fraccions, els km²), targeta de les fraccions, examen. PDF fets |
| 4 · És gran l'ou del kiwi? | Feta: caixa (14 a 17), cinc fitxes (la fracció d'un nombre, multiplicar fraccions, els percentatges, dobles i triples, i el repàs), examen. PDF fets |
| 5 · Decimals i arrel quadrada | **Feta** (29/9/2026): caixa (18 a 21, i la 2.4), targeta «Decimals i arrels», sis fitxes i examen (`generadors/examens/ud5.js`). El pla sencer i les decisions: `MAPA-ADAPTACIO.md`, apartat 8 bis |
| 6 · Sentit espacial | **Feta** (29/9/2026): caixa (22 a 25), targeta «Formes», sis fitxes i examen (`generadors/examens/ud6.js`). El pla: `MAPA-ADAPTACIO.md`, apartat 8 ter |
| 7 · Patrons i llenguatge algebraic | **Feta** (29/9/2026): caixa (26 a 28), targeta «Patrons i símbols», cinc fitxes i examen (`generadors/examens/ud7.js`). |

**Pendent al Codespace** (recorda-li-ho si no ho ha fet; comprova-ho al ZIP del repositori que et
passi): treure del repositori els vuit DOCX dels exàmens de les unitats 1 a 4
(`generadors/examens/examen-ud*-*.docx`), que es publiquen al web. Les ordres: `git rm --cached` i
moure'ls a `docx/` (`CONTINUAR.md`, apartat 4). **No esborris els `fitxes/ud4*.html` ni `generadors/examens/ud4.js`:** les fitxes velles d'una
antiga unitat 4 (les fraccions) ja no hi són, i els que hi ha ara són els de la unitat 4 de debò.
Les ordres exactes són a `CONTINUAR.md`.

**El material del grup per a les unitats 5 a 7**: la **programació** (set fulls de càlcul, un per
situació d'aprenentatge) i, des del 29/9/2026, el **llibre del grup** (`llibre_1ESO`, en LaTeX: una
carpeta per unitat, `1eso/udN/1eso-udN-M.tex`). Demana tots dos ZIP. Els casos surten del llibre
(regla 8). **Compte:** el llibre té vuit unitats i la programació set. La SA6 hi és partida en dues
(UD6 formes i UD7 mesura), i la SA7 hi és la UD8. El material segueix les SA (apartat 8).

## 3. L'entorn on treballes

- Tens un Linux sense xarxa. Hi ha Python 3.12 (python-docx, openpyxl, pypdf, PIL), Node amb la
  llibreria `docx`, Playwright amb Chromium (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`) i
  LibreOffice (`soffice`). **No hi ha WeasyPrint**: per mesurar i previsualitzar el paper, fes
  servir `eines/mesura_chromium.py` i `eines/pdf_chromium.py` (fan el mateix que `mesura.py` i
  `gen_pdf.py`, amb Chromium). Els PDF de debò els fa el docent al Codespace.
- El docent et passarà el repositori en un ZIP (`pi-main.zip`). Descomprimeix-lo en una carpeta de
  treball i treballa-hi. Al final, fes-ne el ZIP de lliurament (apartat 6).
- Desa una còpia de la carpeta abans de canvis grans. Les converses llargues es compacten: escriu
  les decisions als documents del repositori, no només a la conversa.

## 4. El mètode, pas a pas (el que ha funcionat a les unitats 1 a 3)

1. **Llegir.** De la programació, el full de la situació d'aprenentatge: les pestanyes `INICI`
   (el context i el repte), `SABERS`, `OBJECTIUS-CRITERIS`, `ACTIVITATS` (la seqüència, amb
   dates) i **`INCLUSIÓ`** (les mesures del departament: sovint ja proposen el model de quadrícula).
   Les pestanyes amb «OCULT» o «FILTRE» són el currículum sencer: no cal llegir-les.
2. **Proposar el pla** en un missatge curt: les eines noves de la caixa (amb una tasca tancada
   cadascuna), si cal una targeta nova, les fitxes (una per bloc d'activitats, en l'ordre de la
   programació, i un repàs amb «Què he après?»), l'examen, el que **queda fora i per què**, i les
   **regles trencades** (un error típic per fitxa, que el dibuix desmunta). Acaba amb com a molt
   tres preguntes de botons. No construeixis res fins que el docent validi.
3. **La caixa d'eines** (vegeu 5.1), amb les proves i l'auditoria.
4. **La targeta**, si el pla en porta (vegeu 5.3).
5. **Les fitxes** (vegeu 5.2), una a una: generar, verificar, mesurar, mirar-les en imatge i
   arreglar el que no quedi bé.
6. **L'examen** en DOCX (vegeu 5.4), mirat amb LibreOffice.
7. **La documentació**: `MAPA-ADAPTACIO.md` (la unitat activitat per activitat, les decisions amb
   data, les regles trencades), `CONTINUAR.md` (l'estat), el `README.md` (taules de tasques i
   fitxes) i `ARQUITECTURA.md` (les eines).
8. **Les proves i el lliurament** (apartat 6), i un missatge final clar: què hi ha, què s'ha
   comprovat, com pujar-ho (amb el text del commit) i què ve després.

Treballa per trossos que es puguin lliurar: normalment, la caixa en un lliurament, la targeta en
un altre, les fitxes en un o dos, i l'examen al final.

## 5. Com es fa cada peça

### 5.1 La caixa d'eines (`caixa-eines.html`)

- **Cada eina és un mòdul** de `js/moduls/`. El més recent i net és `area.js` (tasca 13): copia'n
  l'estructura. Una eina té una subtasca d'explorar (comptadors o pastilles, un dibuix, una lectura
  en frases, i la marca «Exemple» quan és l'exemple de la fitxa) i una **tasca tancada** de cinc
  passos, amb una pista al primer error, la resposta ensenyada al segon, i un codi de verificació
  al final. Les respostes falses de les tasques tancades són **les confusions de debò** de l'alumnat.
- **Els prefixos dels identificadors** (`aa-`, `ab-`...) han de ser únics: comprova-ho amb `grep`
  abans. Els números de tasca són fixos: la 14 és la primera lliure.
- **Les frases** són a `dades/textos.js`: el text a `window.TEXTOS["N.M"]` i l'explicació a
  `window.TEXTOS_GUIA["N.M"]`, amb les mateixes claus. Si una clau es construeix a trossos, el
  prefix ha d'acabar en `_` (`"13.1.fig_" + nom`), perquè el verificador sàpiga que es fa servir.
  Les claus s'alineen amb espais: per editar-les, fes servir expressions regulars, no text exacte.
- **El marcatge**: una pestanya (`data-tasca="N" data-mod="nom"`), una `<section id="mod-nom">` amb la
  subbarra i les subtasques (copia la de l'àrea), i el `<script>` al final de `caixa-eines.html` i de
  `verifica.html`, en l'ordre de les tasques. Afegeix la tasca a `dades/unitats.js` (`tasques`), a
  la portada `index.html` («Per al professorat», els enllaços agrupats per unitat), al `README.md`
  i a `ARQUITECTURA.md`.
- **El dibuix** és a `js/quadricula.js` (`CE.q`): quadrets, rectangles, graelles, la graella de 100,
  els rectangles d'un nombre, la tira de les fraccions i el nom d'una fracció. Afegeix-hi les
  peces noves que puguin servir a més d'una eina.
- **Les proves**: `eines/prova_caixa.py` (afegeix-hi una secció per eina i la subtasca a la llista
  de mòduls; en SVG, llegeix el text amb `textContent`, no amb `inner_text`) i `eines/auditoria.py`
  (afegeix els estats nous a `ESTATS`, amb una acció si cal tocar alguna cosa).
- **El nucli**: `js/nucli.js` té l'API (`CE.comptador`, `CE.pastilles`, `CE.tasca`, `CE.retroaccio`,
  `CE.lectura`, `CE.quants`, `CE.botonsSiNo`, `CE.pintaSiNo`, `CE.barreja`, `CE.registra`,
  `CE.registraCataleg`...). Mira com les fa servir `area.js` o `multiples.js`.

### 5.2 Les fitxes de paper (`fitxes/`)

- **Es fan amb generadors** de Python, a `generadors/fitxes/` (vegeu-ne el README). Cada un fa una
  fitxa: `python3 1eso/generadors/fitxes/fitxa_ud3_area.py 1eso/fitxes/ud3-area.html`. Fes-ne un de
  nou copiant el més semblant. Les peces comunes són a `fitxa_ud1.py` (la classe `Dibuix`, `ms()` per
  a l'escrit a mà, `buit()` i `buit_curt()` per als forats, `ULL`, els colors), `peces_ud2.py`
  (`tria()`, `fes_pagina()`, `document()`, la graella de 100, els rectangles, l'arbre de factors) i
  `peces_fraccions.py` (`fr()` per a les fraccions, `fr_buit()`, `tira()`, `caixa()`).
- **L'estructura d'una fitxa** (la vigila `eines/comprova.py`): el «previ» (el graó físic, cinc
  minuts abans, amb material de debò), el títol, el nom, l'obertura «Què hi veus?», el **model
  resolt**, els exercicis amb **l'apartat a) resolt** en lletra manuscrita, **una pàgina amb la regla
  trencada** que acaba amb la forma bona a la vista, **una pàgina «A la vida de cada dia»**
  (`classe="full vida"`) i el **solucionari** (Abans de començar, el graó físic, les respostes amb
  l'error típic, la caixa d'eines, i «Què mirar per avaluar» amb els criteris de la situació).
- **El peu**: «Unitat N · Tema · pàgina N». El fitxer: `udN.html` o `udN-tema.html`; l'ordre de
  classe el dona la llista `fitxes` de la unitat a `dades/unitats.js`.
- **Cada pàgina ha de cabre en un A4**: `python3 1eso/eines/mesura_chromium.py 1eso/fitxes/X.html`
  (fins a 27,1 cm; deixa-hi marge). Si no hi cap, dues columnes, dibuixos més petits o partir la
  pàgina. **Mira-les sempre en imatge** (`pdf_chromium.py` i `pdftoppm`): la mesura no veu una
  paraula tallada ni un dibuix que no s'entén.
- **Les fraccions** en paper van dins d'un `<span class="fr">` (fes servir `fr()`): el verificador
  les llegeix com «3/4» i en calcula les igualtats exactes. Una igualtat falsa a posta (per revisar)
  va dins de `.revisa`, o de `.ratllat` si surt ratllada.
- **No toquis** `css/tokens.css`, `css/fitxa.css`, `fonts/Caveat.ttf` ni `eines/paper.py`: en surten
  les empremtes dels PDF, i caducarien tots. Si una peça necessita estil, posa'l a l'element.

### 5.3 Les targetes de consulta (`targetes/`)

Dues cares (dos blocs `.full targeta`), el títol `h1.cara-titol` i el peu «Targeta de … · cara N».
S'afegeixen a `TARGETES` de `dades/unitats.js`, amb la unitat i el PDF. El model més recent és
`targetes/fraccions.html` (generador `targeta_fraccions.py`).

### 5.4 Els exàmens en DOCX (`generadors/examens/udN.js`)

- Només hi ha el contingut; el motor és `comu/examens/nucli.js`. Copia `ud3.js`. Cada exercici té
  **quatre apartats: l'a) resolt** (`ms(...)`) i tres per fer, amb ítems de les fitxes de la unitat.
  L'ordre dels exercicis és el de l'examen del grup o el de les fitxes. `mateixaPagina: true` fa
  que un exercici comparteixi pàgina amb l'anterior: cap exercici no pot quedar partit.
- Dins d'una cel·la, `{3/4}` s'escriu com a fracció (una taula petita: no facis servir les
  fraccions de Word, que LibreOffice no llegeix).
- `node 1eso/generadors/examens/udN.js` escriu a `1eso/docx/`. Converteix-lo amb
  `soffice --headless --convert-to pdf` i mira'n les pàgines. El motor avisa de problemes de
  llengua (pronoms febles, paraules difícils): corregeix-los.
- **Els DOCX no es pugen mai** al repositori (es publicaria el solucionari). Lliura'ls a part.

## 6. Les proves i el lliurament

Abans de lliurar, **sempre**:

```bash
python3 1eso/eines/comprova.py      # només hi poden quedar PDF que falten
python3 4eso/eines/comprova.py      # «Tot correcte.»
timeout 1500 python3 1eso/eines/prova_caixa.py    # «Tot correcte.» (si has tocat la caixa)
timeout 1800 python3 1eso/eines/auditoria.py      # «0 problemes en N estats» (si has tocat la caixa)
```

El **ZIP** porta la carpeta `1eso/` sense `pdf/` ni `docx/`, els fitxers de `comu/` i de l'arrel que
hagis tocat, i res més. Una ordre que ha funcionat:

```bash
zip -r -X -q sortida.zip 1eso/ comu/examens/nucli.js comu/docs/EXAMENS-DOCX.md \
    -x "*/__pycache__/*" "*.pyc" "1eso/pdf/*" "1eso/docx/*"
```

Després, **simula la pujada**: descomprimeix el ZIP del repositori que t'ha passat el docent en una
carpeta a part, fes-hi `git init` i un commit, descomprimeix-hi el teu ZIP a sobre, aplica-hi les
ordres `git rm` que li donaràs, i passa-hi els verificadors. Si hi surt res que no sigui un PDF que
falta, arregla-ho abans de lliurar.

## 7. Les regles que no es poden trencar

Són a `CRITERIS-DISSENY.md`; aquestes són les que més fàcilment es trenquen:

- **Un sol model:** la quadrícula de quadrets (rectangles, graella de 100, tires). Res de cercles de
  pastís ni de dibuixos nous si la quadrícula ho pot fer.
- **Sense calculadora; amb les targetes al davant.** Totes les multiplicacions, de la targeta de les
  taules (fins a 10 · 10). Les sumes, sense portar-ne.
- **Fins a 999.** L'única excepció és «1 km = 1.000 m» (unitat 3). Els decimals, fins a 9,99 i amb
  dues xifres decimals com a molt (decisió del 29/9/2026): 999 centèsimes.
- **Lectura Fàcil** a tot el que llegeix l'alumnat: frases de 20 paraules com a molt, sense pronoms
  febles a les consignes («ho», «-ho»: digues què), sense sigles en majúscules, verbs concrets
  («Marca», «Pinta», «Escriu»), «pels» i no «per els». Multiplicar s'escriu amb «·», mai «×» ni «x».
- **Blanc i negre**, lletra de 14 punts com a mínim, i l'escrit a mà dels apartats resolts, en
  Caveat (`ms()`).
- **La regla 8:** els mateixos casos al paper i a la pantalla. L'exemple de cada eina és el de la
  fitxa, i els casos de les tasques tancades surten a les fitxes.
- **L'anonimat:** res del diagnòstic, ni noms, ni el curs escrit, ni el nom de la carpeta sense la
  barra, ni frases que parlin d'una sola persona: els verificadors en tenen la llista, a l'apartat
  ANONIMAT. Parla sempre de «l'alumnat». La portada de l'arrel és l'única que pot dir el curs.
- **Les claus del navegador** comencen per `pi1-`. L'ordre dels scripts de la caixa és fix:
  `textos.js`, `nucli.js`, `codi.js`, `tasca.js`, `quadricula.js`, els mòduls i `app.js`.

## 8. Les unitats que falten, segons la programació

Demana al docent el ZIP de la programació (els set fulls de càlcul) si no te l'ha passat. Es
llegeixen amb `openpyxl`:

```python
import openpyxl
wb = openpyxl.load_workbook(FITXER_DE_LA_SA4, data_only=True)   # el full que acaba en «SA4_…kiwi.xlsx»
for nom in ["INICI", "SABERS", "ACTIVITATS", "INCLUSIÓ"]:
    celes = [" ".join(str(c.value).split()) for fila in wb[nom].iter_rows() for c in fila if c.value]
    print(nom, " | ".join(celes)[:3000])
```

El que ja se'n sap, i el nucli que hi ha a `dades/unitats.js` (una **proposta** per validar):

- **Unitat 4 · És gran l'ou del kiwi?** (del 12 al 28 de gener, 11 sessions, criteris 1.3, 2.1, 5.1
  i 6.1). Fa servir les fraccions de la unitat 3: la fracció d'un nombre, la fracció d'una fracció,
  multiplicar i dividir fraccions, la proporcionalitat directa (dobles i triples) i els
  percentatges. El context: l'ou del kiwi pesa una part molt gran del pes de la mare. Nucli
  proposat: «Un terç de 12 és repartir 12 quadrets en 3 grups iguals» (lliga amb repartir, de la
  unitat 2) i «un percentatge és quants quadrets de cada 100» (la graella de 100 de la unitat 2).
  Idea de pla per validar: eines 14 (la fracció d'un nombre), 15 (percentatges a la graella de 100)
  i 16 (dobles i triples en una taula); multiplicar i dividir fraccions, probablement fora o per a
  nivells alts: **pregunta-ho**.
- **Unitat 5 · Decimals i arrel quadrada**: feta el 29/9/2026 (`MAPA-ADAPTACIO.md`, apartat 8 bis).
- **Unitat 6 · Sentit espacial** (del 5 d'abril al 10 de maig). Polígons, perímetres, àrees i
  escales. **Compte:** el llibre del grup la parteix en dues unitats (UD6 formes i UD7 mesura); el
  material segueix la SA6, però els casos es treuen de les dues. Nucli proposat: polígons al geoplà; el perímetre és comptar costats de quadret (lliga amb
  l'àrea de la unitat 3).
- **Unitat 7 · Patrons i llenguatge algebraic** (del 19 de maig a l'1 de juny). Patrons, regla de
  formació i símbols. Nucli proposat: patrons de quadrets; quants quadrets té la figura següent.

## 9. Lliçons apreses (errors que ja vam fer i com evitar-los)

- **Confirma la unitat amb la programació abans de construir.** Les fraccions es van fer primer
  com a unitat 4 i eren de la 3: va costar un canvi de noms a tot arreu.
- **Les substitucions globals trenquen coses**: canviar «ud4» per «ud3» a tot arreu va canviar
  també el nom d'un mòdul de peces. Fes canvis concrets, i comprova'n el nombre d'aparicions.
- **Un script que s'atura a mitges** pot haver escrit uns fitxers i altres no: torna a mirar
  l'estat abans de repetir-lo.
- **Els verificadors tenen raó gairebé sempre**: una frase de 21 paraules, una sigla en
  majúscules, «adaptat» en un solucionari, un pronom feble. No els desactivis: arregla el text.
  Si cal una excepció (com el 1.000 del quilòmetre), que la decideixi el docent, i escriu-la al
  verificador de manera estreta i documentada.
- **Mira-ho en imatge.** Moltes coses que les proves no veuen (una opció tallada, un rètol
  retallat, un nombre massa petit, una fracció a mà massa petita) només surten a la imatge.
- **Els textos d'un SVG** es llegeixen amb `textContent`; les fraccions de Word no les llegeix
  LibreOffice; les fitxes llargues no cabran si hi poses tot en una columna.
- **Les dades delicades** (la unitat 3 parla de Gaza): només dades de mesura al material, i el
  context, a l'aula amb el docent. Digues-ho al solucionari.

## 10. Per començar la conversa nova

El docent et passarà el ZIP del repositori i el de la programació, i et dirà per quina unitat
començar. **Les set unitats del curs són fetes (29/9/2026).** El que queda és el que el docent vegi
en provar-les a l'aula: canvis a fitxes concretes, els apartats «nous» dels exàmens (unitats 5, 6 i
7), els nou avisos de frases llargues de les unitats 2 a 4, i el pronom de «Busca-ho» de
`ud3-equivalents.html`. Abans de lliurar qualsevol fitxa, mira'n el PDF fet amb WeasyPrint.
Un primer missatge que pot fer servir:

> Llegeix `1eso/docs/TRASPAS.md` i els documents que diu. Després, t'explico què he vist a l'aula
> i què cal canviar.

## 11. Coses que van fallar a la unitat 4 (i com evitar-les)

- **Mira els PDF i els DOCX en imatge** (`pdftoppm -png -r 80`, i LibreOffice per als DOCX).
  `mesura.py` i `comprova.py` no veuen un text tallat pels costats, ni una consigna separada de la
  seva taula: només l'alçada. Aquests dos errors només es van veure mirant-ho.
- **`comprova.py` i les igualtats amb «de» o «entre»:** «1/2 de 1/4 = 1/8» fa un fals error, perquè
  llegeix només el tros després de la paraula. Escriu «és», o la multiplicació inversa.
- **Un dibuix amb clau a l'esquerra** (`clau_esq`) necessita 1,9 cm de marge; amb 1,1, «3 grups»
  surt tallat. Fes servir l'amplada real del dibuix (`cos.amp`), no una fórmula a mà.
- **Amb dibuixos de grups en files, quatre casos per pàgina, no cinc:** `.frase` té interlineat 2,3.
- **Comprova el número de cada activitat a la programació** abans d'escriure «adapta les activitats…»:
  a la unitat 4 dues estaven mal assignades.
- **Les xifres d'un context real** (un ou, un ocell) s'han de comprovar: no n'inventis.
- **El ZIP porta `1eso/` sense `pdf/` ni `docx/`** (apartat 6): els PDF els fa el docent al Codespace.

**Trobat el 29/9/2026, en començar la unitat 5** (les proves no tenien la unitat 4, i per això
ningú no ho havia vist):

- **La tasca 15 no dibuixava.** Feia servir els prefixos `tt-` i `tf-`, que ja eren de la tasca 0:
  `$("#tt-svg")` trobava la taula de les taules. Ara s'hi diuen `mf-` i `mg-`, i `comprova.py` falla
  amb qualsevol identificador repetit.
- **Les tasques 16 i 17 donaven el codi de la 15.** El codi només tenia 4 bits per a la tasca (de
  la 0 a la 15). Ara hi caben fins a la 63, i els codis de les tasques 0 a 15 són els d'abans.
- **`fitxes.html` no ensenyava les fitxes de la unitat 4.** A `dades/unitats.js` hi havia
  `fitxes: [...]` i, més avall, `fitxes: []`: el navegador es queda amb l'últim. `comprova.py`
  ara falla amb qualsevol camp repetit.
- **Lliçó:** cada eina nova entra a `prova_caixa.py` i a `auditoria.py` el mateix dia. El que no es
  prova no se sap si funciona.

**Trobat el 29/9/2026, en pujar les fitxes 5 i 6 de la unitat 5:** l'acció de `_uploads/`
desempaqueta cada ZIP a sobre del repositori, i l'últim que s'aplica guanya. Els dos ZIP portaven
`dades/unitats.js` i els documents; el de la fitxa 5, més vell, es va aplicar després del de la
fitxa 6, i en va desfer els canvis (`fitxes/ud5-repas.html` no sortia a `dades/unitats.js`).
**Lliçó:** cada ZIP porta la versió al dia dels fitxers compartits (`dades/unitats.js`, els
documents), i el docent en puja un i espera la marca verda abans de pujar-ne un altre. Si en queden
dos per pujar, se'n fa un de sol.

**Trobat el 29/9/2026, en fer les fitxes de la unitat 6:** les opcions per marcar en columna
(`tria(..., columna=True)`) es veien bé amb Chromium, però WeasyPrint, que és el que fa els PDF,
les estirava i les encavalcava. Els PDF publicats d'`ud2-repartir` (pàgina 5, exercici 4: no es
podia fer) i d'`ud3-sumes` (pàgina 5, caselles estirades) sortien malament. Ara cada opció va en una
fila pròpia, a `peces_ud2.py` i a la còpia de `tria()` de `fitxa_ud2_repartir.py`. **Lliçó:** abans
de lliurar una fitxa, mira'n el PDF fet amb WeasyPrint (`eines/mesura.py` i `generadors/gen_pdf.py`,
amb `pip install weasyprint`), no només la imatge de Chromium: els dos motors no fan igual el
`flex` en columna, i les mesures poden diferir 5 cm.
- **Als generadors, no facis servir `f` com a variable.** `fitxa_ud1.py` hi té la funció `f()` que
  escriu els nombres dels dibuixos: una variable `f` a nivell de mòdul la tapa i el dibuix peta
  (29/9/2026, fitxa del perímetre).
