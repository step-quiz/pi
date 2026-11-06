# SITE-MAP.md — the map, the shell and the rules of the site

> **Read this first.** It is the single source of truth for how the site is organised and how it
> looks. It was written on 6/11/2026, when the whole navigation was rebuilt from scratch after a
> review with the teacher (40 decisions, IDs like F1, N5, D4 quoted below). It is meant for an AI
> or a developer arriving cold — for instance to add the courses `2eso/` and `3eso/` in September
> 2027. If the code and this document disagree, fix this document in the same commit.

The site is **pi.step-quiz.net**: adapted maths material for students with cognitive
difficulties. Static HTML, CSS and vanilla JavaScript; no build step, no server, no external
resource. Published by Cloudflare Pages from `main`; it must also work when opened with a double
click (`file://`). The repository is public: **github.com/step-quiz/pi** (the teacher page links to
each course's `docs/` there). Everything the user reads is in Catalan; code comments in `comu/` are in English,
the rest of the repository is in Catalan.

---

## 1. Who reads what

| Reader | Pages | Device |
|---|---|---|
| **Teacher** (and colleagues of the same school, F4) | everything except the student tools | any |
| **Students** | only `CURS/eines.html?u=N`, through the link the teacher sends | Chromebook, touch or mouse, never a phone (F3) |

Consequences, all enforced:

- The unit page, the sheets and the answer keys are teacher pages. They can show PDFs of answer keys.
- The student tools are a **closed space**: no link to anything (F1). A student who had a link out
  could reach the answer keys.
- Targets are at least 48 px high and nothing depends on hover only (F3).

## 2. The map

`CURS` is a course folder (`1eso/`, `4eso/`…). Published URLs drop `.html` (Cloudflare Pages
«pretty URLs»); **links in the HTML always use the real file name** (`index.html`, `fitxa.html`)
so that the double click works. Every link is relative; the only absolute paths are in `404.html`.

```
/                          index.html               Home («Inici»): «Curs 2026-27», title, one column per course
                                                    (its units and a «Professorat» button). No header bar.
/CURS/                     CURS/index.html          Course: header + its units
/CURS/uN/                  CURS/uN/index.html       Unit (teacher): one grid of three equal cards, numbered,
                                                    no heading icon: 1 Fitxa · 2 Quadern d'activitats ·
                                                    3 Repàs · 4 Eines · 5 Targetes (missing cards are
                                                    skipped, numbers close up); then «Abans de la
                                                    classe», a <details> folded on every load.
                                                    «Abans de la classe» is the grid's last item, as
                                                    wide as one card. Column 60rem; title 1.8rem; card
                                                    border 1.8px #8E929C, button border 1.15px; card
                                                    buttons hover pale blue (--w-eina-h), PDF buttons
                                                    brown (--w-pdf-h), «Copia l'enllaç» grey
                                                    (--w-nav-h). Decision of 6/11/2026.
/CURS/uN/fitxa             CURS/uN/fitxa.html       main sheet of the unit (paper)
/CURS/uN/NOM               CURS/uN/NOM.html         other sheets of the unit (1eso/ has up to six per unit)
/CURS/uN/repas             CURS/uN/repas.html       review sheet (paper)
/CURS/uN/quadern           CURS/uN/quadern.html     workbook with filters (optional; printed from the browser)
/CURS/targetes/NOM?u=N     CURS/targetes/NOM.html   reference card (may serve several units; ?u says which)
/CURS/eines?u=N            CURS/eines.html          STUDENT tools of unit N — closed space
/CURS/professorat          CURS/professorat.html    Teacher page: «Canviar les frases», «Llegir codis», notes
/CURS/textos, /verifica    CURS/textos.html …       the two teacher helper pages
/CURS/pdf/…                CURS/pdf/*.pdf           PDFs. Names never changed: see §6
```

There are **no redirects and no old addresses** (decision P4: the site started from zero on
6/11/2026). `404.html` is a plain page. `index.html?other-versions=1` shows the two AI-made
versions kept for comparison (`other-versions/`); they are outside the map and never checked.

### The teacher section is CLOSED (6/11/2026)

Decided by the owner on 6/11/2026: for now, the teacher section is not reachable. It is **kept,
not deleted**, because it may come back.

- One switch: `PI.professorat = false;` at the top of `comu/js/web.js`.
- While false: no «Professorat» button anywhere (home page, course page, unit page, paper pages:
  `PI.capcalera` and `comu/js/portada.js` both read the switch).
- `CURS/professorat.html`, `CURS/textos.html` and `CURS/verifica.html` are untouched, but
  `comu/js/professorat.js` (loaded by all three) sends the visitor to `CURS/index.html` with
  `location.replace`. Adding `?obert` to the address opens the page anyway; the tests use it
  (`prova_caixa.py` for `verifica.html`, `auditoria.py`).
- `comu/eines/prova_portada.py` reads the switch: closed, it checks there is no button and that
  `professorat.html` lands on the course page; open, it checks the button is on every page.
- **To reopen:** set `PI.professorat = true;`, run `comu/eines/prova_portada.py`. Nothing else.
  Everything below that mentions the «Professorat» button describes the section when open.

Every page that is not the home page or the student tools has the **same header** (N1): a violet
bar `Inici › course › Unitat N › page`, with the **«Professorat»** button on the right (F2; hidden
while the section is closed, see above). The
course in the path is a link to the course page. The last step is never a link and never bold.

## 3. Vocabulary (V1, V2, V3)

One name per thing, everywhere (pages, PDFs, docs):

| Name | What | Never call it |
|---|---|---|
| **Fitxa** / **Fitxes** | the paper sheet(s) of the unit | fitxa d'activitats, fitxa de la unitat |
| **Quadern d'activitats** | the workbook; greyed out «Quadern d'activitats no disponible» when missing (U3) | pràctica |
| **Repàs** | the review sheet | fitxa de repàs |
| **Eines** | the student tools on screen | caixa d'eines, més eines |
| **Targetes** | the laminated reference cards | targetes de consulta (in the UI) |
| **Professorat** | the teacher page and button | |

- The **unit title** comes from `dades/unitats.js` everywhere (header, tab title, workbook). A
  sheet keeps its own name («El món, fet petit») as the sheet title.
- The **course names** live in ONE file, `comu/js/cursos.js`, and are inserted at run time. The
  anonymity check forbids them anywhere else (§9).

## 4. Data model — `CURS/dades/unitats.js`

The same fields in every course. Every page of the course reads this file; nothing else
describes the units.

```js
window.UNITATS = [{
  num: 3, titol: "Proporcionalitat i escales",
  fitxes: [{ fitxa: "u3/fitxa.html", titol: "El món, fet petit" }],   // class order; first is uN/fitxa.html
  repas:  { fitxa: "u3/repas.html", titol: "Repàs · Escales" },
  quadern: "u3/quadern.html",          // optional
  tasques: [0, 2, 4, 7],               // the tabs of eines.html shown for this unit (data-tasca)
  material: "…", objectiu: "…",        // «Abans de la classe»: material, objectiu or nucli, trencada
  nucli: "…", trencada: "…",
  // course-specific fields are allowed (1eso/: estat, minim, criteris, fita, rol…; 4eso/: moduls, llibre…)
}];
window.TARGETES = [{ nom: "percentatges", titol: "…", unitats: [2, 3], descripcio: "…" }];
```

Rules: every page in `uN/` (except `index.html`) is declared here; every declared path exists;
paths of a unit live in its own folder `uN/`; a card is `targetes/NOM.html` + `pdf/targeta-NOM.pdf`.

## 5. The shell — `comu/`

### Files and responsibilities

| File | Job |
|---|---|
| `comu/css/web.css` | The whole screen look of the shell. Every class starts with `w-`. Colour variables `--w-*`. |
| `comu/js/cursos.js` | The course registry: `PI.CURSOS = [{id, nom}]`. The only file with course names. |
| `comu/js/web.js` | Helpers on `window.PI`: `esc`, `frases`, `ic` (icons), `boto`, `capcalera`, `cursEscolar`, `pdfBase`, `lloc`, `curs`, `unitat`, `carrega`, `copia`. |
| `comu/js/portada.js` | Home page. Loads each course's data one after the other (all are `window.UNITATS`). |
| `comu/js/curs.js` | Course page. |
| `comu/js/unitat.js` | Unit page (`uN/index.html`). The unit number comes from the folder name. |
| `comu/js/professorat.js` | Teacher page and the header of `textos.html` / `verifica.html` (`data-w-pagina`). |
| `comu/js/paper.js` | Header of every paper page (§6). Loads `cursos.js`, `web.js` and `../dades/unitats.js` itself. |
| `comu/js/alumne.js` | Closed header of the student tools; sets `PI.einesUnitat` from `?u=N`. Runs before `js/app.js`. |
| `comu/eines/unitat.html` | The canonical unit page. Every `CURS/uN/index.html` is an exact copy. |
| `comu/eines/mapa.py` | The site-map check (§9). |

### Contract between HTML, CSS and JS

- **HTML** carries structure and `data-*` attributes only. Thin pages (course, unit) are an empty
  `<main id="w-web">` plus scripts; they contain no course name and no unit number.
- **CSS** reads classes and variables. Base rules use `:where()` (zero specificity) so any
  component rule wins. Course stylesheets never use the `w-` prefix.
- **JS** never writes styles; it writes markup with `w-` classes. No `fetch()` (it fails on
  `file://`); scripts are loaded with `<script>` elements (`PI.carrega`).
- **Data** lives in `dades/unitats.js`; **words** the students read in the tools live in
  `dades/textos.js` (edited from `textos.html`).

### Design system (decisions D1–D5 and the mockup review of 6/11/2026)

- One light theme for the shell. Font: the system stack. Weights 400 / 500 / 600 only — never 700+
  (Segoe UI renders them «Black»). Titles are weight 400.
- **Buttons** (`.w-b`): min-height 48 px, radius 10 px, 1 px border `#D5D8DE`. Three kinds:
  principal (`.w-principal`, weight 600, same background as the others), secondary, and the path
  links of the header. Inside cards, buttons are **75 % of the card width, aligned left**.
- **Four functions, four hover tints** (D4): navigate `--w-nav-h #E8E9ED`, open a material
  `--w-mat-h #EBE3F7`, download or print `--w-pdf-h #F3E8DB`, tools `--w-eina-h #DDE5F1`. The icon
  takes the dark tone of its function.
- **Hover and keyboard focus** (the teacher's global rule): pure black border, thick
  (`border-color:#000` + `box-shadow:0 0 0 1px #000`), light background, nothing moves or resizes.
- **Selected** (`aria-selected` / `aria-checked`, and `.pastilla[aria-pressed]` in the tools):
  background unchanged, thick black border and a **black round tick** in the top-left corner.
  Never a black or dark background.
- «Professorat» button: background 15 % darker (`#D9DADE`). «Copia l'enllaç» (unit page)
  becomes olive grey-green (`#C6C9AE`) and says «Enllaç copiat».
- **Header of every teacher page**: pale violet `#F3EEFC`, 2 px border `#6A3FC4`, a thicker violet
  stripe on the left, a round violet seal with the teacher icon.
- **One icon set** (D2), in `web.js`: 24 × 24 grid, 2 px stroke, round caps. The pictograms printed
  on paper are a different, untouched set.
- Text: one sentence per line in prose blocks (`PI.frases`, forced break after each full stop,
  except after «Ex.»). The home page shows «Curs AAAA-AA», which changes on 1 September.
- No disclosure widgets (`<details>`), no dates on the unit page, no descriptive subtitles on
  cards, no developer text on pages (S2, S3, U1, decisions 4–6 of the mockup review).

## 6. Paper pages (sheets, reviews, workbook, cards)

The white A4 sheet on grey is kept. Above it, **one screen-only bar**, written by the generator
right after `<body>`:

```html
<nav class="navega no-imprimir" aria-label="Navegació"><link rel="stylesheet" href="../../comu/css/web.css"><a href="index.html">Unitat 3</a><script src="../../comu/js/paper.js"></script></nav>
```

**Everything screen-only goes INSIDE that `<nav>`**, because the PDF fingerprint
(`4eso/eines/empremta.py` and `1eso/eines/paper.py`, regex `SENSE_PDF`) strips exactly that
element. Changing the header therefore never makes a PDF old. `paper.js` replaces the fallback
link with the violet header and the buttons («PDF alumnat» · «PDF solucionari», or «PDF a doble
cara» for a card; nothing for the workbook, which has its own print buttons), and sets the tab
title from the data.

- **PDF names never changed**: `uN/fitxa.html → pdf/udN-alumnat.pdf / udN-solucionari.pdf`,
  `uN/NOM.html → pdf/udN-NOM-…`, `targetes/NOM.html → pdf/targeta-NOM.pdf` (`PI.pdfBase`,
  `gen_pdf.py`).
- The fingerprint also covers `css/tokens.css`, `css/fitxa.css`, `fonts/Caveat.ttf`, the PDF
  stylesheet and (in `1eso/`) `eines/paper.py`. **Editing any of them makes every PDF of the
  course old**; PDFs can only be rebuilt with WeasyPrint (`pip install weasyprint`, then
  `python3 CURS/generadors/gen_pdf.py`), which is possible in a Codespace.
- Generated pages are never edited by hand: `1eso/generadors/fitxes/*.py` (each writes its own
  destination, see `desa()` in `peces_comunes.py`), `4eso/generadors/gen_repas.py`,
  `gen_quadern.py`. The 4eso/ main sheets and the cards are hand-made.

## 7. Student tools — `CURS/eines.html?u=N`

- `comu/js/alumne.js` reads `?u=N`, writes «Unitat N · title» in `#w-cap-alumne` and sets
  `PI.einesUnitat`. `js/app.js` (`aplicaUnitat`) shows only the tabs listed in `tasques`: first the
  unit's own tools in data order, then a thin separator, then the always-there tools
  (`data-comuna`: Calculadora and Com ho dic in `4eso/`, Taules in `1eso/`).
- The teacher gets the link from the unit page («Copia l'enllaç»), published
  without `.html`: `https://pi.step-quiz.net/4eso/eines?u=3`.
- Inside a tool, examples belong to units too: the double number line (`js/moduls/doble.js`) has
  `unitats` per example and shows only those of the unit; with one example, no chooser (E1).
- `?task=n` and `?task=n.m` still open one tool or one exercise, **only for the browser tests and
  the audits**; nothing links to them. Without any parameter the page shows every tool (tests only).
- The «Exemple» badge is hidden by CSS (S5); the modules still set it, the tests check that.

## 8. Adding a unit / adding a course

**A unit:** add its object to `dades/unitats.js`; create `uN/` with a copy of
`comu/eines/unitat.html` as `uN/index.html`; put the sheets in `uN/` (generator or by hand, with
the screen bar of §6); run the generators and `gen_pdf.py`; add the tools to `tasques`.

**A course** (e.g. `2eso/`):
1. Add `{ id: "2eso", nom: "2ESO" }` to `comu/js/cursos.js`.
2. Create the folder with the same layout as `1eso/` (the more generic one): `index.html` (copy of
   another course's, unchanged), `professorat.html` (adapt the notes), `eines.html` + `css/`,
   `js/`, `dades/unitats.js`, `dades/textos.js`, `uN/`, `targetes/`, `pdf/`, `fonts/`, `eines/`,
   `generadors/`, `docs/`.
3. Copy and adapt `eines/comprova.py`: add the new course name patterns to the **anonymity**
   lists of **every** course checker (`2n ESO`, `2eso` outside a path…), keeping the exemption for
   `comu/js/cursos.js` and `index.html`. Its section NAVEGACIÓ calls `mapa.comprova_curs()`.
4. Add the course to both workflows (`.github/workflows/comprova.yml`, `unzip-upload.yml`). The
   ZIP upload ignores `.github/`: change workflows from the GitHub web or a Codespace.
5. Run every check of §9.

## 9. Checks — run them before delivering anything

```bash
python3 1eso/eines/comprova.py          # each course: paper, tools, words, contrast, anonymity, data, map
python3 4eso/eines/comprova.py
python3 comu/eines/mapa.py              # the map of every course (also run inside each comprova.py)
python3 comu/eines/prova_portada.py     # clicks the whole map in Chromium (Playwright)
python3 1eso/eines/prova_caixa.py       # the tools, end to end
python3 4eso/eines/prova_caixa.py
python3 4eso/eines/prova_quadern.py     # the workbook filters
python3 1eso/eines/auditoria.py         # contrast, targets, paper font size
python3 4eso/eines/auditoria.py
```

GitHub runs both `comprova.py` on every push; the ZIP workflow refuses to save if they fail.

## 10. Known debt (not done on 6/11/2026)

- **S1 is pending**: the student sheets still print «Cinc minuts abans, a l'aula de suport: …» at
  the top (`class="previ"`). Removing it changes every PDF, so it needs a Codespace with
  WeasyPrint. The teacher postponed it.
- Each course still has its own copies of `tokens.css`, `app.css`, `fitxa.css`, `nucli.js`,
  `tasca.js`, `codi.js`, `veu.js` (`comu/eines/diferencies.py` lists what differs). Merging them
  touches the PDF fingerprints (§6) and the tools; do it course by course, with the tests.
- `textos.html` and `verifica.html` still use the course `css/lloc.css`, with the shell header on top.
- The `<title>` written inside the paper pages is the old one (it is part of the PDF
  fingerprint); `paper.js` sets the right one on screen.

## 11. Mistakes that already happened — do not repeat them

- **Two names for one thing** (unit titles, «Fitxes d'activitats» vs «Fitxa de la unitat», «Més
  eines» holding no tools). Use §3.
- **Screen-only markup outside the paper `<nav>`** makes every PDF «old» in the check. Put it inside.
- **Editing `tokens.css` or `fitxa.css` for a screen tweak** makes every PDF old. Override from
  `comu/css/web.css` with a more specific selector (`nav.navega …`), as done for the old 3D
  «← inici» key style.
- **Writing a course name in a page, script or doc** fails the anonymity check. Use `cursos.js`.
  In prose, write course folders as paths (`4eso/`), never as a bare word.
- **The singular «l' + alumne»** is forbidden in every file (anonymity check): write «l'alumnat».
- **Colour in `fitxa.css` or `quadern.css`** fails the paper check: paper is black and white.
- **Stale CSS after a deploy** (5/11/2026): `_headers` makes CSS and JS revalidate on every visit;
  keep it that way for `comu/` and every course.
- **Global names**: a top-level `const` called like something the host page defines breaks the
  whole script. Wrap scripts in an IIFE and hang shared things from `window.PI`.
- **Specificity**: a base rule like `.w-pagina h1 { margin: 0 }` silently beat `.w-titol`. Base
  rules go in `:where()`.
- **The ZIP upload cannot delete files.** Moving or removing files needs a commit from a
  Codespace (or a pull request).
- **Hover only** is not enough on touch Chromebooks; **black backgrounds** for selected states are
  «too aggressive» for the teacher; **pill-shaped full-width buttons** look like «sausages».
