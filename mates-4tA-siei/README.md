# Matemàtiques 4t ESO Aplicades · material adaptat

Material per a un alumne de 4t d'ESO amb **discapacitat intel·lectual lleu** que fa la
meitat de les hores de matemàtiques a l'aula **SIEI** i l'altra meitat a l'itinerari
d'**Aplicades**.

Set fitxes imprimibles, una caixa d'eines digital i la documentació que explica per què
tot és com és.

---

## Com s'obre

Doble clic a `web/index.html`. No cal servidor, ni instal·lar res, ni cap dependència.

## On es publica

GitHub → Cloudflare Pages → `step-quiz.net`. **Tot el que es publica és dins de `web/`**;
a Cloudflare només cal posar `web` al camp *Build output directory* i deixar la resta
buida. Les altres carpetes es queden al repositori i no surten al web: `docs/` descriu
el perfil d'un alumne concret i no ha de ser pública. Vegeu `docs/DESPLEGAMENT.md`.

---

## Què hi ha

| | |
|---|---|
| `web/` | **tot el que es publica**: portada, índex, aplicació i fitxes |
| `web/index.html` | portada: les set unitats i les eines |
| `web/fitxes.html` | el detall de cada unitat: material previ, regla trencada, fita, recursos |
| `web/caixa-eines.html` | l'aplicació, amb vuit mòduls |
| `web/fitxes/ud1…ud7.html` | les fitxes imprimibles, en blanc i negre |
| `docs/` | mapa d'adaptació, criteris de disseny, arquitectura i feina pendent |
| `generadors/` | scripts Python que dibuixen els gràfics SVG de les fitxes |

---

## El principi

> Aquest alumne pot arribar a la **decisió** de 4t. No pot arribar al **càlcul** de 4t
> ni a la **redacció** de 4t.

I Matemàtiques Aplicades és, precisament, la matèria de decidir amb dades. Amb el càlcul
descarregat a la calculadora i l'expressió bastida amb frases model, la competència
nuclear li és accessible de veritat.

El perfil és desigual, i tot el material en surt:

| Canal | Nivell |
|---|---|
| Visió gràfica, esquemes, geometria | 2n ESO |
| Manipulació aritmètica i algebraica | 5è de primària |
| Expressar idees matemàtiques amb frases | 3r de primària |
| Informàtica i anglès | 4t ESO |

---

## Abans de tocar res

Llegeix **`docs/CRITERIS-DISSENY.md`**. Hi ha vuit regles que no són preferències
d'estil: són el resultat d'iterar amb el docent i algunes van sortir de correccions
seves. Les dues que més fàcilment es trenquen sense adonar-se'n:

- **Blanc i negre estricte a les fitxes.** S'imprimeixen en B/N i no se sap com quedarien
  els colors. Hi ha un test que ho comprova: `python3 eines/comprova.py`.
- **Cap paràgraf a les pàgines de l'alumne.** El dibuix explica, les paraules només
  etiqueten. Aquesta regla val per a les fitxes, no per als solucionaris ni per a les
  pàgines de navegació, que són per a l'adult.

---

## Comprovacions

```
python3 eines/comprova.py
```

Verifica que les fitxes no tinguin cap valor cromàtic, que l'HTML tanqui bé, que la
numeració de pàgines sigui seguida, que cada fitxa porti el rètol de material i
l'obertura, i que els mòduls declarats a `caixa-eines.html` coincideixin amb els que
es registren de debò.

---

## Estat

Set unitats completes. Vuit mòduls a la caixa d'eines.

**Pendent**, documentat a `docs/CONTINUAR.md`:

- comprovar si els mòduls de l'app acumulen o buiden la pantalla entre passos;
- contrastar el teclat del mòdul Calculadora amb una Casio fx-82SP CW real;
- no hi ha mòdul d'estadística ni d'atzar (per a la U6 l'eina és el full de càlcul).
