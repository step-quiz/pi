# Com posar això a step-quiz.net

---

## La idea, en una frase

Tot el que ha de sortir al web és **dins de la carpeta `web/`**. La resta de carpetes
(`docs/`, `generadors/`, `eines/`) es queden al repositori i no es publiquen.

```
mates-4tA-siei/
├── web/          ← això es publica
├── docs/         ← això NO
├── generadors/   ← això NO
└── eines/        ← això NO
```

---

## Els camps de Cloudflare

Quan connectes el repositori, Cloudflare Pages t'ensenya un formulari. Només n'has de
tocar un.

| Camp del formulari | Què hi poses | Per què |
|---|---|---|
| Framework preset | **None** | no fas servir cap framework |
| Build command | **deixa'l buit** | no hi ha res a compilar |
| Build output directory | **`web`** | ← l'únic que canvia |

Als teus altres projectes ho deixes tot buit i es publica el repositori sencer. Aquí
només hi ha una diferència: escriure `web` al camp de la carpeta de sortida. Això li diu
a Cloudflare «publica només aquesta carpeta».

Després, a **Custom domains**, hi afegeixes `step-quiz.net`. El certificat el fa
Cloudflare tot sol.

---

## Per què `docs/` no es publica

**Aquest material parla d'un alumne concret.** No hi surt cap nom, però en un institut hi
ha un sol alumne de SIEI a 4t d'ESO en l'itinerari d'Aplicades: el context l'identifica.

Els documents de `docs/` descriuen el seu perfil cognitiu canal per canal, les fites
d'avaluació que s'esperen d'ell i diuen que són la base del seu PI. Això no ha de ser
consultable des d'internet.

Les **fitxes** i la **caixa d'eines** no tenen aquest problema: són material de
matemàtiques i podrien ser útils a altra gent.

**Si el repositori de GitHub és públic**, `docs/` s'hi veurà igualment, encara que no es
publiqui al web. Si vols que no es vegi enlloc, **el repositori ha de ser privat**.
Cloudflare Pages funciona exactament igual amb repositoris privats.

---

## Els cercadors

El lloc també queda fora de Google, per dos camins alhora:

- `web/robots.txt` diu `Disallow: /`
- `web/_headers` afegeix la capçalera `X-Robots-Tag: noindex, nofollow`

Si algun dia vols que sigui públic i indexable: esborra `web/robots.txt` i treu la línia
`X-Robots-Tag` de `web/_headers`. Res més.

---

## Abans de publicar

```
python3 eines/comprova.py
```

Ha de dir **«Tot correcte»**. Entre altres coses comprova que no hi hagi cap carpeta
`docs/` dins de `web/`, que és l'error que faria públic el que no ha de ser-ho.

---

## Els altres fitxers que hi ha a `web/`

| Fitxer | Per a què serveix |
|---|---|
| `404.html` | la pàgina que surt quan algú s'equivoca d'adreça; Cloudflare l'agafa sol |
| `favicon.svg` | la icona de la pestanya del navegador |
| `robots.txt` | manté el lloc fora dels cercadors |
| `_headers` | capçaleres de seguretat i una hora de memòria cau |

---

## Coses que ja estan resoltes i no has de mirar

**Majúscules.** Els servidors distingeixen `Fitxes/` de `fitxes/`. Tots els noms són en
minúscules i sense accents, i el test avisa si algun enllaç queda penjat.

**Cap dependència de fora.** Ni CDN, ni fonts de Google, ni biblioteques. El filtre del
centre no el pot trencar i funciona sense xarxa.

**Es continua podent obrir sense servidor.** Doble clic a `web/index.html` i va igual,
des d'un llapis de memòria. És una sortida el dia que el web no funcioni.
