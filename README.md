# Matemàtiques Aplicades · material adaptat

Material de matemàtiques per a **alumnat amb dificultats de tipus cognitiu** que fa una
part de les hores a l'**aula de suport** i l'altra a l'aula ordinària, en l'itinerari
d'**Aplicades**.

Set fitxes imprimibles, una caixa d'eines digital i la documentació que explica per què
tot és com és.

---

## Com s'obre

Doble clic a `index.html`. No cal servidor, ni instal·lar res, ni cap dependència.

## On es publica

GitHub → Cloudflare Pages → `step-quiz.net`, amb **tots els camps del formulari buits**.
És un lloc estàtic corrent: no hi ha res a compilar. Vegeu `docs/DESPLEGAMENT.md`.

---

## Què hi ha

| | |
|---|---|
| `index.html` | portada: les set unitats i les eines |
| `fitxes.html` | el detall de cada unitat: material previ, regla trencada, fita, recursos |
| `caixa-eines.html` | l'aplicació, amb vuit mòduls |
| `fitxes/ud1…ud7.html` | les fitxes imprimibles, en blanc i negre |
| `docs/` | mapa d'adaptació, criteris de disseny, arquitectura i feina pendent |
| `generadors/` | scripts Python que dibuixen els gràfics SVG de les fitxes |

---

## El principi

> Aquest alumnat pot arribar a la **decisió** que demana el currículum. No pot arribar
> al **càlcul** ni a la **redacció** del nivell del grup.

I Matemàtiques Aplicades és, precisament, la matèria de decidir amb dades. Amb el càlcul
descarregat a la calculadora i l'expressió bastida amb frases model, la competència
nuclear li és accessible de veritat.

El perfil és desigual, i tot el material en surt:

| Canal | Nivell |
|---|---|
| Visió gràfica, esquemes, geometria | 2n ESO |
| Manipulació aritmètica i algebraica | 5è de primària |
| Expressar idees matemàtiques amb frases | 3r de primària |
| Informàtica i anglès | el del grup |

---

## Abans de tocar res

Llegeix **`docs/CRITERIS-DISSENY.md`**. Hi ha vuit regles que no són preferències
d'estil: són el resultat d'iterar amb el docent i algunes van sortir de correccions
seves. Les dues que més fàcilment es trenquen sense adonar-se'n:

- **Blanc i negre estricte a les fitxes.** S'imprimeixen en B/N i no se sap com quedarien
  els colors. Hi ha un test que ho comprova: `python3 eines/comprova.py`.
- **Cap paràgraf a les pàgines de l'alumnat.** El dibuix explica, les paraules només
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
