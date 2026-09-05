# Com posar això a step-quiz.net

Igual que qualsevol altre projecte estàtic teu. `index.html` és a l'arrel i no hi ha res
a compilar.

---

## Cloudflare Pages

Connectes el repositori i **deixes tots els camps del formulari buits**:

| Camp | Valor |
|---|---|
| Framework preset | None |
| Build command | *(buit)* |
| Build output directory | *(buit)* |
| Root directory | *(buit)* |

Després, a **Custom domains**, hi afegeixes `step-quiz.net`. El certificat el fa
Cloudflare tot sol.

I ja està. Els desplegaments següents surten sols amb cada push.

---

## Què es publica

**Tot el repositori**, inclosos `docs/`, `generadors/` i `eines/`. No fan cap mal: la
documentació ja està escrita en termes d'alumnat amb dificultats de tipus cognitiu, sense
cap referència al curs, al tipus d'aula ni a cap diagnòstic.

Si algun dia vols que només surti la part de material i no la documentació, cal moure el
que es publica a una carpeta i escriure-la al camp *Build output directory*. Però mentre
el contingut sigui anònim, no cal complicar-ho.

---

## Els cercadors

Ara mateix el lloc queda **fora de Google**, per dos camins:

- `robots.txt` diu `Disallow: /`
- `_headers` afegeix `X-Robots-Tag: noindex, nofollow`

Això ve d'una versió anterior, quan el material anomenava el curs i el tipus d'aula.
**Ara ja no cal.** Si vols que les fitxes siguin visibles i útils a altres docents:

1. esborra `robots.txt`
2. treu la línia `X-Robots-Tag` de `_headers`

És reversible i no afecta res més.

---

## Els fitxers de desplegament

| Fitxer | Per a què serveix |
|---|---|
| `404.html` | la pàgina que surt quan algú s'equivoca d'adreça; Cloudflare l'agafa sol |
| `favicon.svg` | la icona de la pestanya del navegador |
| `_headers` | capçaleres de seguretat i una hora de memòria cau |
| `robots.txt` | manté el lloc fora dels cercadors, si el vols fora |

---

## El test

`python3 eines/comprova.py` **no és una feina teva abans de publicar**. És una xarxa per
a qui toqui el material: comprova que les fitxes no tinguin color, que els mòduls de
l'aplicació quadrin amb el marcatge, que cap enllaç quedi penjat i que no hi hagi tornat
a entrar cap terme que trenqui l'anonimat. Si només fas push, no cal que l'obris mai.

---

## Coses que ja estan resoltes

**Majúscules.** Els servidors distingeixen `Fitxes/` de `fitxes/` i Windows no. Tots els
noms són en minúscules i sense accents.

**Cap dependència de fora.** Ni CDN, ni fonts de Google, ni biblioteques. El filtre del
centre no el pot trencar i funciona sense xarxa.

**Es continua podent obrir sense servidor.** Doble clic a `index.html` i va igual, des
d'un llapis de memòria.
