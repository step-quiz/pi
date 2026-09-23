# Com posar això a step-quiz.net

Igual que qualsevol altre projecte estàtic teu. `index.html` és a l'arrel (ara porta a
`4eso/`) i no hi ha res a compilar.

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

## Les adreces

El lloc de `4eso/` és a `https://pi.step-quiz.net/4eso/`. L'`index.html` de l'arrel hi porta
sol, i la `404.html` de l'arrel porta les adreces d'abans de les carpetes (per exemple
`/caixa-eines?task=2`) a la mateixa pàgina dins de `4eso/`, amb el `?task` inclòs: els
enllaços ja enviats a l'alumnat no es trenquen. Ho fa amb JavaScript i no amb un fitxer
`_redirects`, perquè així és segur que el `?task` no es perd pel camí.

Quan hi hagi material de `1eso/`, l'`index.html` de l'arrel ha de passar a ser una portada
que deixi triar el curs.

---

## Què es publica

**Tot el repositori**: `4eso/`, `1eso/` i `comu/`, inclosos els `docs/`, els `generadors/` i
les `eines/` de cada curs. La documentació està escrita en termes d'alumnat amb dificultats
de tipus cognitiu, sense cap referència al tipus d'aula ni a cap diagnòstic.

**El curs, en canvi, surt a les adreces**, perquè les carpetes es diuen `4eso/` i `1eso/`.
El text continua sense anomenar-lo, i `comprova.py` ho vigila, però qualsevol adreça el
mostra. Si et preocupa, pots fer el repositori privat a GitHub: Cloudflare Pages el
continua publicant igual, i ningú no hi arriba des de GitHub.

Si algun dia vols que només surti la part de material i no la documentació, cal moure el
que es publica a una carpeta i escriure-la al camp *Build output directory*. Però mentre
el contingut sigui anònim, no cal complicar-ho.

---

## Els cercadors

Ara mateix el lloc queda **fora de Google**, per dos camins:

- `robots.txt` diu `Disallow: /`
- `_headers` afegeix `X-Robots-Tag: noindex, nofollow`

Això ve d'una versió anterior, quan el material anomenava el curs i el tipus d'aula. Ara
el curs torna a sortir a les adreces (`4eso/`), i per això és millor deixar-ho com està.
Si algun dia vols que les fitxes siguin visibles i útils a altres docents:

1. esborra `robots.txt`
2. treu la línia `X-Robots-Tag` de `_headers`

És reversible i no afecta res més.

---

## Els fitxers de desplegament

Tots són a l'arrel del repositori, fora de les carpetes dels cursos.

| Fitxer | Per a què serveix |
|---|---|
| `index.html` | la porta d'entrada: porta a `4eso/` |
| `404.html` | la pàgina que surt quan algú s'equivoca d'adreça; Cloudflare l'agafa sol. També porta les adreces d'abans a `4eso/` |
| `favicon.svg` | la icona de la pestanya del navegador |
| `_headers` | capçaleres de seguretat i una hora de memòria cau |
| `robots.txt` | manté el lloc fora dels cercadors, si el vols fora |

---

## El test

`python3 4eso/eines/comprova.py` **no és una feina teva abans de publicar**. És una xarxa per
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
