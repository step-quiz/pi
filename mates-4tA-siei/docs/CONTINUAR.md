# Feina pendent

*(Abans es deia `handout.md`. Conserva la traça del que queda obert.)*

**Per a:** una altra IA (o una altra persona) que reprengui aquest projecte.
**De:** Claude, en una sessió sense accés a la cerca web.
**Data del paquet:** 4 de setembre de 2026.

---

## 0. En una frase

Hi ha material de Matemàtiques de 4t ESO Aplicades adaptat per a un alumne amb
discapacitat intel·lectual lleu.

> **ACTUALITZACIÓ · 4 de setembre de 2026.** La feina pendent que descrivia l'apartat 4
> **ja està feta**. Es va poder accedir a `mathisvisual.com` i les troballes són a
> `VERIFICACIO-MATHISVISUAL.md`. Les que valien la pena ja estan incorporades al mapa
> (tercera versió). Els apartats 4, 5 i 6 d'aquest handout queden com a registre històric:
> **no cal tornar a fer aquella feina.**
>
> Queda **una sola cosa oberta** i necessita el docent: el graó de percentatge de la U2,
> descrit a l'apartat 5 del mapa.

---

## 1. Context

**L'alumne.** 15 anys, DIL, fa la meitat de les hores de matemàtiques a l'aula SIEI i
l'altra meitat a 4t ESO en l'itinerari d'Aplicades. El seu perfil és molt desigual, i
això condiciona tot el material:

| Canal | Nivell |
|---|---|
| Visió gràfica, esquemes, geometria | 2n ESO |
| Manipulació aritmètica i algebraica | 5è de primària |
| Expressar idees matemàtiques amb frases | 3r de primària |
| Informàtica i anglès | 4t ESO |

**El principi de tot el material:** aquest alumne pot arribar a la *decisió* de 4t, però
no al *càlcul* ni a la *redacció* de 4t. Com que Matemàtiques Aplicades és la matèria de
decidir amb dades, la competència nuclear li és accessible si es descarrega el càlcul a
la calculadora i es basteix l'expressió amb frases model.

**El docent** té el seu propi ecosistema: un llibre digital amb activitats en PDF de 1r a
4t ESO, un banc d'exercicis autocorrectius (`repas-main`) i les programacions didàctiques
en full de càlcul. El material adaptat s'hi recolza en comptes de substituir-lo.

---

## 2. Què hi ha en aquest paquet

El projecte ja no és una carpeta de fitxers solts: vegeu `docs/ARQUITECTURA.md`.
Els documents que importen són `README.md`, `docs/CRITERIS-DISSENY.md` i
`docs/MAPA-ADAPTACIO.md`.

**El mapa** és el document de referència. Conté el perfil, el principi d'adaptació,
l'articulació SIEI/aula ordinària, els criteris de disseny, l'inventari i el detall
unitat per unitat amb les fites d'avaluació.

**Les set fitxes** segueixen totes la mateixa estructura: pàgines de concepte sense text
seguit, sis o set exercicis amb el primer apartat ja resolt, i un solucionari per al
professorat amb els errors típics i la traça als criteris d'avaluació.

**L'aplicació** té vuit mòduls: Recta, Doble recta, Percentatges, Escales, Paràboles,
Equacions, Calculadora i Com ho dic.

---

## 3. Restriccions que NO s'han de trencar

Aquestes no són preferències: són el resultat d'iterar amb el docent, i algunes van
sortir de correccions seves.

**A les fitxes:**

1. **Blanc i negre estricte.** S'imprimeixen en B/N i no se sap com quedaran els colors.
   Cap valor cromàtic a cap fitxa: només negres, blancs i grisos. Les diferències es fan
   amb nivells de gris, gruix de línia i tipus de traç. *Hi ha un test que ho comprova;
   mantén-lo.*
2. **Cap paràgraf a les pàgines de l'alumne.** El dibuix explica, les paraules només
   etiqueten. El que seria una frase explicativa ha de ser una pantalla de calculadora,
   una barra, una cadena de fletxes o un pictograma.
3. **Consignes completes però curtes**, en imperatiu. «Encercla el nombre que té xifres
   decimals que s'acaben», no «Encercla el que s'acaba». El docent va demanar
   explícitament que fossin una mica més llargues i precises, no telegràfiques.
4. **Cos de 14 pt cap amunt**, molt d'aire, caselles d'1,5 cm per escriure.
5. **El primer apartat de cada exercici, resolt en lletra manuscrita** (classe `.ms`, amb
   una pila de fonts cursives i `cursive` com a últim recurs).
6. **Els gràfics es generen per càlcul**, mai a mà, perquè vèrtexs, barres i marques dels
   eixos caiguin exactament on toca. Els scripts són a `generadors/`.
7. **A cada unitat hi ha «la regla trencada»**: un exercici que trenca la regla que
   l'alumne s'haurà fabricat als apartats anteriors. Està documentat al mapa, apartat 5.
   És l'evidència d'avaluació més valuosa de cada fitxa. No l'eliminis en simplificar.

**A l'aplicació:**

8. **Fitxer únic, vainilla, sense CDN ni dependències.** El filtre del centre bloqueja
   recursos externs. `localStorage` va dins d'un embolcall protegit.
9. **Cada eina s'obre ja resolta** amb un exemple marcat i un botó que la buida.
10. **Paper i pantalla mostren el mateix cas.** Els 300 € de la U2, el 1:100 amb 8 cm de
    la U3, el `x+3=7` de la U4 i els tres fenòmens de la U5 són idèntics a la fitxa i a
    l'app, perquè no hagi d'aprendre dues vegades el mateix.

---

## 4. La feina pendent, i per què no l'he pogut fer

> **RESOLT.** Vegeu `VERIFICACIO-MATHISVISUAL.md`. Es conserva el que segueix perquè
> explica d'on venien les afirmacions i per què calia comprovar-les.

El docent em va presentar **`https://mathisvisual.com/`** com un recurs que podria
millorar aquests materials. **No hi he pogut accedir.** Ho vaig intentar per dues vies i
totes dues van fallar:

- **No tenia cap eina de cerca web.** El docent va dir que l'activava, però en buscar
  entre les eines disponibles només apareixien les de Google Drive. Cap eina de cerca ni
  de lectura de pàgines.
- **El contenidor bloqueja el domini.** `curl` a `https://mathisvisual.com/` i a
  `https://www.mathisvisual.com/` retorna **403 amb la capçalera
  `x-deny-reason: host_not_allowed`**. La llista de dominis permesos només inclou
  repositoris de paquets (PyPI, npm, GitHub, Ubuntu) i `api.anthropic.com`.

Per tant, **tot el que vaig dir sobre aquell lloc surt de la meva memòria d'entrenament,
no d'haver-lo consultat.** Ho vaig advertir al docent, però queda escrit aquí perquè no
es propagui com si fos verificat.

---

## 5. El que vaig afirmar de memòria i que cal comprovar

| Afirmació | Confiança | Cal verificar |
|---|---|---|
| És un projecte de Kyle Pearce, de l'entorn de Make Math Moments amb Jon Orr | mitjana | autoria i vinculació |
| El seu artefacte central són animacions silencioses, sense narració i amb text mínim | mitjana-alta | format real dels recursos |
| El marc de fons és el *concreteness fading*: concret → visual → simbòlic | mitjana | si ho anomenen així i com ho estructuren |
| Prioritzen models com la recta numèrica doble, les matrius i el model d'àrea | mitjana-baixa | quins models fan servir de debò i en quin ordre |
| Condicions de reutilització del material | **no comprovat** | llicència; no assumeixis que es pot reutilitzar |

**Important:** els dos canvis que vaig fer inspirats en aquesta idea —reordenar les dues
primeres pàgines de la U2 i afegir el model d'àrea a la U6— **no depenen que aquestes
afirmacions siguin certes**. Es fonamenten en didàctica del raonament proporcional i en
el model d'àrea, que estan ben establerts pel seu compte. Si en revisar el web resulta
que la meva memòria era imprecisa, **no desfacis aquests canvis**: revisa'ls, però no els
donis per invàlids.

---

## 6. Què buscar concretament

Quan hi puguis accedir, no cal un resum del lloc. Cal respondre aquestes preguntes:

1. **Quins models visuals fan servir i amb quina freqüència?** Concretament: doble recta
   numèrica, model d'àrea, matrius, barres, taules de raons. Ens interessa saber quins
   models es repeteixen entre temes, perquè per a aquest alumne **reutilitzar el mateix
   model val més que tenir-ne molts**.
2. **En quin ordre presenten concret, visual i simbòlic?** Hi ha algun pas intermedi que
   nosaltres ens saltem?
3. **Com formulen les preguntes d'obertura?** Si són del tipus «què hi notes», és
   directament aprofitable: aquest alumne té l'expressió escrita a nivell de 3r de
   primària i qualsevol resposta que es pugui donar assenyalant o oralment li obre la porta.
4. **Tracten percentatges, escales o probabilitat?** Són les nostres U2, U3 i U7, i les
   tres comparteixen ara el mòdul de la doble recta.
5. **Quina és la llicència?** Determina si es pot fer res més que adoptar-ne l'enfocament.

---

## 7. On aniria a parar cada troballa

| Si trobes… | Va a parar a… |
|---|---|
| Un model visual millor per a percentatges | `fitxes/ud2.html` pàgines 1-2 i mòdul Doble recta |
| Un model per a escales o raons | `fitxes/ud3.html` i mòdul Doble recta |
| Una manera millor de presentar la mitjana ponderada | `fitxes/ud6.html` pàgina 4 (model d'àrea) |
| Un model per a probabilitat | `fitxes/ud7.html` i mòdul Doble recta |
| Un patró d'obertura silenciosa | totes les pàgines 1 de les fitxes |
| Una progressió d'animació aprofitable | mòduls de l'app, que ja fan revelació pas a pas |

**Dos buits coneguts de l'app:** no hi ha mòdul d'estadística ni d'atzar. Per a la U6
l'eina és el full de càlcul mateix, que l'alumne ja fa servir al nivell del grup; per a
la U7, un arbre interactiu seria l'addició natural.

**Un punt pendent i independent d'això:** la disposició de tecles i l'etiqueta `FORMAT`
del mòdul Calculadora estan pendents de contrastar amb una Casio fx-82SP CW real. Hi ha
una constant `SEP_DECIMAL` per si les calculadores del centre estan configurades amb coma
en comptes de punt.

---

## 8. Com regenerar els gràfics

Els SVG estan incrustats a les fitxes, però es generen amb scripts:

```
generadors/gen_grafics.py    → paràboles de la U5
generadors/gen_grafics2.py   → diagrames de punts, barres i arbres de la U6 i la U7
generadors/gen_grafics3.py   → barres de percentatge de la U2 i model d'àrea de la U6
generadors/gen_grafics4.py   → doble recta de la U2, repartiment de la U6, barra d'atzar de la U7
generadors/aplica_millores.py → insereix aquests tres a les fitxes i hi posa l'obertura
```

`aplica_millores.py` és diferent dels altres: no dibuixa, **modifica les fitxes**. Es pot
tornar a executar tantes vegades com calgui, perquè comprova els marcadors `§…§` que ell
mateix deixa i salta el que ja hi és. Si un ancoratge no hi és o hi és dues vegades,
s'atura en comptes d'endevinar.

Cada script escriu un `.json` amb els SVG i **imprimeix les comprovacions numèriques**
(vèrtexs, talls, sumes, percentatges). Si en modifiques un, mira que les comprovacions
segueixin quadrant abans de tornar a incrustar-los.

Per incrustar-los, les fitxes fan servir marcadors `§NOM§` que se substitueixen pel
contingut del JSON. Els fitxers d'aquest paquet ja tenen les substitucions fetes.

---

## 9. Una última cosa

El docent d'aquest projecte corregeix bé i de pressa. Dues correccions seves que van
canviar el rumb del material, per si serveixen d'orientació sobre com treballa:

- La primera versió de la fitxa de la U1 tenia unes 700 paraules i em va dir que era
  **impossible** que l'alumne la llegís. Tenia raó, i d'aquí va sortir tot el criteri de
  disseny.
- Va demanar el blanc i negre quan les fitxes ja estaven fetes en color, perquè
  s'imprimeixen així al centre. També tenia raó.

Si dubtes entre fer una cosa i preguntar-la, **fes-la i explica què has decidit i per
què**, però no toquis l'ordre de les pàgines conceptuals d'una fitxa ja validada sense
dir-l'hi: aquesta sí que la va voler aprovar.

---

## 10. Estat després de reorganitzar el projecte

El material s'ha convertit en un projecte estàtic amb responsabilitats separades: el CSS
de les fitxes era duplicat set vegades i ara és un sol full; la caixa d'eines era un
fitxer de 63 KB amb tot a dins i ara són vuit mòduls independents que es registren sols.
Res del contingut ha canviat en aquesta reorganització.

**El que continua obert**, per ordre de valor:

1. **Si els mòduls de l'app acumulen o buiden la pantalla entre passos.** És l'única
   troballa de `VERIFICACIO-MATHISVISUAL.md` que segueix sense comprovar. Buidar redueix
   la càrrega, i la càrrega és el coll d'ampolla d'aquest alumne.
2. **El teclat del mòdul Calculadora**, pendent de contrastar amb una Casio fx-82SP CW
   real: la disposició de tecles i l'etiqueta `FORMAT`. Hi ha la constant `SEP_DECIMAL`
   per si les calculadores del centre estan configurades amb coma.
3. **No hi ha mòdul d'estadística ni d'atzar.** Per a la U6 l'eina és el full de càlcul,
   que l'alumne ja fa servir al nivell del grup. Per a la U7, un arbre interactiu seria
   l'addició natural, i `VERIFICACIO-MATHISVISUAL.md` §6 avisa que allà no hi ha res per
   copiar de fora.
4. **El graó «raó → taxa» de la U3.** Ja hi ha el pas del preu unitari, però es podria
   marcar més com a pas propi.
