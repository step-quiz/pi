# Criteris de disseny

Les regles de tot el material de `1eso/`: el que s'imprimeix (les fitxes i les targetes de
consulta) i la caixa d'eines de la pantalla. Cada regla porta el seu perquè. Si una regla s'ha de
trencar, primer es canvia aquí.

Hi ha dues menes de regles: les que venen del material de `4eso/`, que es mantenen, i les
pròpies d'aquest material, que surten del punt de partida descrit a
[`MAPA-ADAPTACIO.md`](MAPA-ADAPTACIO.md).

Els tests vigilen les que es poden comprovar soles. La llista és al final.

---

## 1. Les regles que es mantenen

| # | Regla | Per què |
|---|---|---|
| 1 | **Blanc i negre estricte.** Les diferències es fan amb grisos, gruix i tipus de traç | S'imprimeix en B/N al centre |
| 2 | **Cap paràgraf** a les pàgines de l'alumnat | Un paràgraf és una barrera abans de començar |
| 3 | **Cos de 14 pt cap amunt**, i molt d'aire | Llegibilitat |
| 4 | **El primer apartat de cada exercici ja ve resolt, en lletra manuscrita**, un 30% més gran que la d'impremta del voltant (`.ms`, a `css/fitxa.css`) | És el model: ensenya com es fa sense explicar-ho, i ha de destacar. La mida la va decidir el docent el 24 de setembre de 2026, veient la primera fitxa |
| 5 | **El símbol surt del dibuix.** Primer el dibuix, després la paraula, i el símbol al final. Mai s'anuncia al costat | El símbol sense dibuix no s'agafa a res |
| 6 | **Obertura: «Què hi veus?»**, abans del primer dibuix. Es respon mirant i dient | Comença per on tothom pot entrar |
| 7 | **El graó físic**: cinc minuts amb material de debò a l'aula de suport, abans de la fitxa. Una línia per a l'adult a dalt de la primera pàgina (`.previ`) | La fitxa arriba quan la idea ja s'ha tocat |
| 8 | **El mateix cas al paper i a la pantalla**, i el mateix objecte que fa servir el grup | Qui canvia d'aula no canvia de problema |
| 9 | **«A la vida de cada dia»**: una pàgina per unitat amb un context real i una segona situació amb la mateixa decisió | El que s'aprèn no es queda lligat a un sol cas |
| 10 | **La regla trencada**: un exercici on el procediment que s'acaba de fer no serveix. Aquí amb condicions: vegeu la regla G | Obliga a mirar, no a repetir |

---

## 2. Les regles d'aquest material

### A. Un sol model per a tot el curs

**La quadrícula de quadrets, i la recta numèrica com a segon model. Res més.**

Cada model nou és una cosa més per oblidar. Amb un de sol, cada unitat reactiva el mateix record
en lloc d'obrir-ne un de nou. La programació del grup ja fa servir la quadrícula a gairebé totes
les unitats, i així l'alumnat treballa amb el mateix objecte que la resta de la classe.
[`MAPA-ADAPTACIO.md`](MAPA-ADAPTACIO.md) diu què fa la quadrícula a cada unitat.

### B. Res no es demana de memòria

**Tot el que s'ha de recordar és en una targeta de consulta.** Les targetes s'acumulen al llarg
del curs i es queden a la taula, a les dues aules. Cada sessió comença mirant la targeta de
l'última vegada.

No es demana recordar: es dona on mirar. Una taula apresa es pot perdre en pocs dies, i una
tasca que en depengui avalua la memòria, no el que es vol avaluar.

Una targeta és una ajuda per consultar, no una pàgina per aprendre: no porta dibuixos nous ni
anuncia símbols. El model neix a la fitxa (regla 5) i, un cop après, pot passar a la targeta.

### C. Sense calculadora

**Cada fitxa es pot fer amb la targeta de les taules i prou.** A l'aula ordinària no hi ha
calculadora, perquè no hi hagi greuge amb la resta del grup. A l'aula de suport sí, però només
per comprovar: cap exercici no la necessita.

La targeta de les taules no fa greuge: la programació del grup ja preveu les taules
plastificades per a tothom.

### D. Els nombres

- **Fins a 999.** Cap nombre de les pàgines de l'alumnat no en passa.
- **Sumes i restes sense portar-ne.** Si un càlcul en necessita, es canvien les dades.
- **Multiplicacions: les de la targeta**, d'una xifra per una xifra o per 10.

### E. Per multiplicar, el punt

**3 · 4 = 12**, amb el punt volat del teclat (`·`, el de la ela geminada). És el que fa servir
el grup. «×» només surt a la clau de la targeta de les taules, que fa el pont amb el símbol de
primària, i va dins de `.simbol-primaria`. La lletra `x` mai no multiplica: a la unitat 7 serà
una lletra de l'àlgebra.

El punt matemàtic (`⋅`) no s'hi val: la lletra manuscrita no el té.

### F. Una sola consigna per frase

Frases simples, amb un sol verb que mana. «Busca la taula del 7.» i no «Busca la taula del 7 i
digues quant fa 7 per 8». Si una tasca té dos passos, té dues frases.

### G. La regla trencada es desmunta amb el dibuix

La regla trencada provoca l'error per desfer-lo després. Si el que es queda és l'error, s'ha fet
mal. Per això:

1. **La refutació surt del dibuix o del material**, dins del mateix exercici, no d'un
   raonament. Exemple: «senar vol dir primer» cau quan 9 quadrets fan un quadrat de 3 per 3.
2. **La pàgina acaba amb la forma correcta a la vista.**
3. **A l'avaluació compta per als nivells alts, no per al mínim.**

### H. Cap resultat intermedi al cap

Cada pas d'un càlcul té la seva casella. Si un resultat s'ha de fer servir després, és escrit en
algun lloc de la pàgina.

### I. El llenguatge

Les decisions que va prendre el docent en revisar l'examen de la UD1 de `4eso/`
([`comu/docs/EXAMENS-DOCX.md`](../../comu/docs/EXAMENS-DOCX.md), §5) valen també aquí:

| Principi | Així no | Així sí |
|---|---|---|
| El terme matemàtic correcte | nombres sencers | nombres enters |
| Un sol verb per marcar | Encercla | Marca |
| Sense pronoms febles ni construccions indirectes | Marca amb quants decimals ho escriuries | Marca quants decimals faries servir |
| Verbs literals | quant fa | quant és, quant mesura |
| La restricció, dita en clar | només coses senceres | només quantitats enteres, sense decimals |
| Les unitats, sempre | 12 | 12 quadrets |
| Frases que valguin per a tots els apartats | A totes dues… | En tots els casos… |

I la mateixa paraula per a la mateixa cosa a tot el material: si és «quadret» a la unitat 1,
és «quadret» a la 7.

### J. Cap «adaptat» a les pàgines de l'alumnat

Ni al títol de la pestanya. Una fitxa o una targeta tenen l'aspecte de qualsevol material de
classe.

### K. El solucionari és per a qualsevol adult

A l'aula de suport hi treballen professionals que no han de ser de matemàtiques. El
solucionari s'ha de poder seguir sense ser-ne: què fer, què dir i què mirar, en frases concretes.

Acaba amb **«Què mirar per avaluar»**, en accions que es veuen i amb la targeta al davant.
Per exemple: «Amb la targeta al davant, fa amb miniblocs tots els rectangles de 12». Estan
escrites perquè es puguin passar tal com són als criteris del PI.

### L. Una unitat per situació d'aprenentatge, amb un sol nucli

Els mateixos números i títols que la programació del grup. De cada situació se'n tria una sola
idea, dibuixada a la quadrícula, i es valida amb el docent abans d'escriure la fitxa.

---

## 3. La pantalla: la caixa d'eines

Totes les regles del paper valen igual a la pantalla: un sol model (A), res de memòria (B),
sense calculadora (C), els nombres (D), el punt (E), una consigna per frase (F), la regla
trencada (G), el llenguatge (I) i cap «adaptat», ni al títol de la pestanya (J). A més, la
pantalla té les seves. Com està feta la caixa és a [`ARQUITECTURA.md`](ARQUITECTURA.md).

| # | Regla | Per què |
|---|---|---|
| M | **Cada eina s'obre ja resolta**, amb la marca «Exemple». El cas és el del paper: 7 · 8 a les taules, 3 · 4 als rectangles, 3² als quadrats, 243 als nombres i 2 + 3 · 4 a l'ordre | És la regla 4 a la pantalla, i la regla 8: qui passa del paper a la pantalla troba el mateix cas |
| N | **La tasca 0 és la targeta de les taules**, i surt sempre al costat de l'eina triada. Un enllaç a un exercici concret (`?task=1.2`) porta a aquell exercici i prou: sense fletxes per passar als altres | No hi ha calculadora (regla C): l'eina de tot el curs és la targeta (regla B). I qui rep un enllaç a un exercici no s'ha de perdre pels del costat |
| O | **La creu «×» no surt a la pantalla.** El pont amb la creu de primària es fa una sola vegada, a la clau de la targeta de paper | Un sol lloc per al pont. A la pantalla, el punt i prou |
| P | **Tocar és contestar.** Només quan la resposta demana diversos tocs hi ha un botó «Comprova» (la 3.2) | Cap pas amagat entre fer i contestar |
| Q | **La resposta no es veu mentre es fa.** La 3.2 no ensenya el nombre fins que es comprova; la 2.2 no ensenya els rètols fins que es toca | Si es veu, la tasca es resol provant fins que coincideix |
| R | **El que és bo és bo.** El rectangle girat (5 files de 2 per 2 · 5) i la fila girada (7 · 6 per 6 · 7) compten com a correctes | Tenen els mateixos quadrets. Dir «Incorrecte» a una resposta bona ensenya una regla falsa |
| S | **Les tasques tancades**: cinc passos, un a la vista, amb l'inici i el final marcats. «Correcte.», o bé «Incorrecte.» seguit d'«Ara provem-ho d'una altra manera.» i d'una pista que és un camí diferent. Al segon error, la caixa ensenya la resposta. Acaben amb un resum i un codi de verificació | Saber quant falta i quan s'ha acabat treu càrrega. El codi deixa rastre de la feina sense haver-la de corregir en directe |
| T | **La regla trencada surt del dibuix.** El dibuix tocat es queda amb el seu rètol («4 · 2 = 8. No és un quadrat») i el pas acaba amb les dues formes a la vista. A la 2.2, les preguntes n² i n · 2 van barrejades | És la regla G. Si totes fossin n², tocar sempre el dibuix més gran encertaria |
| U | **Les frases són a `dades/textos.js`**, en Lectura Fàcil, i es poden canviar sense tocar el codi, des de `textos.html` | Qui coneix l'alumnat ha de poder canviar una paraula sense programar |
| V | **Accessible**: WCAG 2.2 AA (contrast, botons de 24 × 24 px com a mínim, focus visible), amb el teclat, en clar i en fosc, i sense animacions si el sistema demana moviment reduït | S'ha de poder fer servir amb qualsevol aparell i de qualsevol manera |
| W | **A la vista, el que l'exercici fa servir, i prou.** El que només cal de tant en tant es plega darrere d'un botó (tota la taula, a la 0.1), i el que ja diu una altra peça no es repeteix (els rètols del dibuix de la 3.1, que ja deien els comptadors) | Són les regles 2 i 3 (cap paràgraf, molt d'aire) portades a la pantalla. Decisió del docent el 24 de setembre de 2026, a partir d'una revisió externa |

---

## 4. Què comproven els tests i què no

**`eines/comprova.py` ho comprova sol:** el blanc i negre; que l'HTML tanqui; la numeració de pàgines i de cares;
el rètol del graó físic, l'obertura, la pàgina de la vida i el solucionari de cada fitxa; el
punt per multiplicar; que cap nombre de l'alumnat passi de 999; frases de més de 20 paraules
(i avís a partir de 15), paraules repetides, majúscules i xifres romanes; el llenguatge de la
taula de la regla I (com a avís); «adaptat»; que cada multiplicació, suma i resta escrita
estigui bé, també al solucionari; que el text manuscrit només porti caràcters que Caveat té;
que cada PDF sigui el que sortiria ara; els fulls d'estil; el contrast de la pantalla; els
enllaços; l'anonimat; les dependències externes, i les dades. De la caixa d'eines: que
pestanyes, seccions i mòduls coincideixin i es carreguin en l'ordre bo; els números de tasca;
que cada frase que es demana existeixi i tingui explicació; les regles de Lectura Fàcil a totes
les frases; les subtasques; que no hi hagi «×» ni «x» de multiplicar, cap nombre de més de 999
ni cap «adaptat», i que la memòria del navegador comenci per `pi1-` i la sal sigui pròpia.

**Amb un navegador** (`eines/prova_caixa.py` i `eines/auditoria.py`): que la caixa funcioni de
punta a punta, amb encerts, errors, pistes, resums i codis; que el text que surt de debò no
trenqui cap regla (cap frase sense definir, cap «×», fins a 999); que les sumes de les dades no
portin i les multiplicacions siguin de la targeta; el contrast aplicat, la mida de cada botó i el
focus, en clar i en fosc, al mòbil i a l'ordinador.

**Ho ha de mirar una persona:** que hi hagi una sola consigna per frase; que les sumes i restes
no portin; que el model sigui la quadrícula; que el símbol surti del dibuix; que la regla
trencada es desmunti amb el dibuix; la mateixa paraula per a la mateixa cosa; que el
solucionari es pugui seguir sense ser de matemàtiques. De la caixa: que s'entengui què s'ha de
tocar; que cinc passos sigui la mida bona; que les pistes ajudin de debò. I sobretot, **el
paper**: imprimir-ho i mirar-ho; i **l'aula**: veure-ho fer servir.
