# Mapa d'adaptació — Matemàtiques Aplicades

**Alumne amb dificultats de tipus cognitiu · 50 % a l'aula de suport i 50 % a l'aula ordinària · curs 2026-27**
**Quarta versió.** La segona es va refer un cop preparades les set unitats i incorporant
el principi de fer emergir el símbol del dibuix. Aquesta hi afegeix el graó físic previ,
l'obertura per pregunta i tres precisions per unitat, un cop contrastat l'enfocament amb
material publicat de raonament visual (`VERIFICACIO-MATHISVISUAL.md`).

La primera versió d'aquest document era una hipòtesi de treball. Aquesta ja no:
recull el que s'ha decidit unitat per unitat, el material que existeix i els
criteris de disseny que han anat sortint del procés i que convé mantenir.

**El que s'ha tocat de les fitxes en aquesta versió.** Quatre insercions, cap
redisseny: l'obertura a la pàgina 1 de les set, la doble recta a la U2, el pas del preu
unitari a la U3, el repartiment a la U6 i la barra de probabilitat a la U7. Ni un estil
nou fora de `.obertura`, ni una pàgina moguda de lloc, ni un exercici tocat. Tot està
generat per `generadors/aplica_millores.py`, que es pot tornar a executar sense duplicar
res i que deixa marcadors `§…§` allà on ha entrat.

---

## 1. El perfil, llegit en clau matemàtica

No és un perfil «dos cursos per sota». És un perfil **desigual**, i això ho canvia tot.

| Canal | Nivell | Què vol dir a classe de mates |
|---|---|---|
| Visió gràfica, esquemes, geometria | **2n ESO** | Via d'entrada principal. Tot concepte nou arriba primer com a dibuix, recta, barra, gràfica, balança o arbre. |
| Manipulació aritmètica i algebraica | **5è primària** | Coll d'ampolla. Es descarrega amb calculadora, full de càlcul i nombres amables. |
| Expressar idees matemàtiques amb frases | **3r primària** | Coll d'ampolla més sever. Una justificació escrita oberta li tanca la porta encara que tingui la idea correcta. |
| Informàtica i anglès | **el del grup** | Palanca. GeoGebra, Desmos, full de càlcul i qualsevol eina digital, al nivell del grup. |

> **Aquest alumnat pot arribar a la DECISIÓ del nivell del grup. No pot arribar al CÀLCUL ni a la REDACCIÓ del nivell del grup.**

I Matemàtiques Aplicades és, precisament, la matèria de decidir amb dades. Els set
productes finals són decisions: quina opció em surt més a compte, quina solució té
sentit, em convé jugar. Amb el càlcul descarregat i l'expressió bastida, la
competència nuclear li és accessible de veritat.

**Fortaleses i colls d'ampolla per competència.** CE4 (pensament computacional) i
CE5 (connectar representacions) es poden treballar gairebé al nivell del grup: aquí
no cal baixar el llistó. CE1, CE3, CE6, CE8 i CE9 són accessibles amb suport visual
i temps. CE2 (argumentar) i CE7 (comunicar) són el coll d'ampolla real, i s'adapten
canviant **el format de l'evidència**, no l'exigència cognitiva.

---

## 2. El principi: separar l'objectiu del vehicle

Abans de demanar-li res, val la pena respondre: en aquesta tasca, què avaluo de debò?

- Si l'objectiu és **decidir, interpretar o triar**, el càlcul és el vehicle. Cap
  error aritmètic no hauria de fer baixar la valoració.
- Si l'objectiu és **comunicar**, el canal escrit obert és el vehicle. Oral,
  assenyalar, ordenar targetes, triar entre frases model o ensenyar la captura del
  GeoGebra valen exactament igual.
- L'única cosa que no es rebaixa és **la idea matemàtica**. Amb menys casos, amb
  nombres més amables i amb més suport, però la idea sencera.

---

## 3. Com articular el 50 % aula de suport + 50 % aula ordinària

**L'aula de suport ha d'anar per davant, no per darrere.** Si l'aula de suport és el lloc on es repassa
el que no s'ha entès a l'aula, l'alumnat arriba sempre tard i viu l'aula com un lloc
on no s'assabenta.

| Moment | On | Què hi fa |
|---|---|---|
| **1. Anticipació** | aula de suport | Abans que el grup comenci: **cinc minuts de material físic**, després el vocabulari, l'esquema visual i **un exemple resolt sencer**. Les pàgines de concepte de cada fitxa serveixen exactament per a això. |
| **2. Participació** | Aula ordinària | L'activitat del grup. Aquí no s'adapta la tasca, s'adapta el **rol** dins la parella. |
| **3. Pràctica guiada** | Aula ordinària | Els exercicis de la fitxa. Calculadora sempre sobre la taula. |
| **4. Consolidació** | aula de suport | Caixa d'eines i, molt selectivament, `repas-main`. La frase model de la unitat. |

Amb 4 hores setmanals són 2 sessions de suport i 2 d'aula. **La sessió d'anticipació ha
de caure abans de la sessió d'aula on s'introdueix el saber nou**; val la pena
negociar-ho amb l'horari mentre s'hi sigui a temps. És la peça amb més impacte de tot
aquest document.

### El graó físic que faltava, i on és ara

**Ja no és només una recomanació escrita.** Cada fitxa porta, a dalt de tot de la pàgina 1
i abans del títol, un rètol per a l'adult: «Cinc minuts abans, a l'aula de suport: …» amb el
material concret. I cada solucionari té un apartat que diu què fer-hi amb aquell material
i amb quin dibuix de la fitxa enllaça.

| Unitat | Material | El gest |
|---|---|---|
| 1 | cinta mètrica i un objecte llarg | mesurar i mirar entre quines marques cau |
| 2 | monedes i bitllets de joguina | apartar la rebaixa i veure què queda |
| 3 | cinta mètrica i full quadriculat | mesurar una paret i decidir quants quadrets fa un metre |
| 4 | bossa opaca i fitxes iguals | endevinar quantes n'hi ha a dins |
| 5 | una pilota | seguir amb el dit el punt més alt |
| 6 | fitxes o taps | fer munts desiguals i aplanar-los |
| 7 | un dau i una moneda | tirar vint vegades i anotar |

### El graó físic que faltava

Tot aquest material comença al dibuix. Li falta la baula d'abans: **tocar-ho**. La
seqüència completa és **físic → visual → simbòlic**, i nosaltres n'estàvem fent només els
dos últims trams.

No demana material nou ni cap canvi a les fitxes: són cinc minuts al principi de la
sessió d'anticipació, amb el mateix cas que després sortirà a la pàgina 1.

| Unitat | Què se li posa a les mans | Què n'ha de sortir |
|---|---|---|
| 1 | Un metre i una balança de cuina | Que la precisió que cal depèn de l'ús |
| 2 | 300 € en bitllets de 100, 20 i 10 | Repartir el descompte sense calcular-lo |
| 3 | Cinta mètrica i el plànol imprès | Que el pas de paper a realitat és el mateix sempre |
| 4 | Una balança de plats i pesos iguals | Que treure d'una banda obliga a treure de l'altra |
| 5 | Una pilota i el vídeo del bot | Que hi ha un punt més alt i que baixa igual que puja |
| 6 | Fitxes en piles desiguals | Aplanar-les fins que totes siguin iguals |
| 7 | Un dau i 60 tirades reals | Que sortir un 6 no és cada sis tirades |

**Per què val la pena.** Té la visió gràfica a 2n d'ESO, però el gest físic no passa per
cap dels dos colls d'ampolla: ni pel càlcul ni per la frase. És l'única entrada que no li
demana res del que li costa.

---

## 4. Les regles fixes del curs

Cinc mesures que es compleixin sempre valen més que vint que es diluiran al novembre.

1. **La calculadora no es negocia mai.** Científica, des del primer dia i a totes les
   activitats i proves. És la mesura que li obre l'accés, i per això té un
   mòdul propi a la caixa d'eines.
2. **Un exemple resolt sencer, sempre visible.** És la mesura amb més impacte i la més
   barata. A les fitxes està incorporada: el primer apartat de cada exercici ja ve fet.
3. **Un sol pas nou per sessió.** Els seus colls d'ampolla no són de comprensió, són de
   càrrega. Dues novetats el mateix dia fan que se'n perdin les dues.
4. **Mai una justificació escrita en blanc.** Sempre una de tres sortides: frases model
   per completar, tria entre opcions, o explicació oral que registres tu.
5. **El seu rol al grup surt del seu punt fort.** És qui dibuixa, qui mesura, qui fa el
   gràfic i qui porta l'ordinador. Amb la informàtica al nivell del grup, el full de càlcul i el
   GeoGebra del producte final els pot fer de debò.

---

## 5. El criteri de disseny de les fitxes

Això no hi era a la primera versió: ha sortit del procés, i convé escriure-ho perquè
qualsevol material nou el segueixi.

**El dibuix explica, les paraules només etiqueten.** Cap paràgraf a les pàgines de
l'alumnat. El que seria una frase explicativa es converteix en una pantalla de
calculadora, una barra, una cadena de fletxes o un pictograma. La densitat que ha
funcionat va de **181 paraules** (Unitat 1, la més neta) a **539** (Unitat 7, on els
missatges de les apostes s'han de citar literalment perquè els reconegui). Les
unitats amb molt context real —escales, estadística, atzar— pugen inevitablement;
el que no puja és la llargada de cada frase.

**Consignes completes però curtes.** «Encercla el nombre que té xifres decimals que
s'acaben», no «Encercla el que s'acaba». Frase sencera, sense subordinades.

**Cos de 14 pt cap amunt, molt d'aire i caselles de 1,5 cm** per escriure-hi còmodament.

**Blanc i negre.** Cap color a cap fitxa: les diferències es fan amb nivells de gris,
gruix de línia i tipus de traç. Està comprovat fitxer per fitxer que no hi ha ni un
sol valor cromàtic.

**El primer apartat de cada exercici, resolt en lletra manuscrita.** Veu el model
abans de començar, amb una lletra que es distingeix de la impresa.

**Els gràfics es generen per càlcul, no es dibuixen a mà**, perquè els vèrtexs, les
barres, els punts i les marques dels eixos caiguin exactament on toca.

**El símbol emergeix del dibuix, no s'anuncia al seu costat.** L'ordre de les pàgines
conceptuals ha d'anar de concret a visual a simbòlic. A la U2 la pàgina 1 només parteix
la barra i en surt «de cada 100 €, en queden 80»; el factor 0,8 no apareix fins a la
pàgina 2, com a conclusió. A la U6 el model d'àrea de la mitjana ponderada va abans de
la taula de càlcul. A la caixa d'eines, el mòdul de la doble recta manté l'expressió
amb números amagada fins que l'alumnat mou el punt.

**El graó que faltava a la U2, ara hi és.** La pàgina 1 anava de la barra partida
directament a «de cada 100, en queden 80», i la pàgina 2 en treia el 0,8. Ara, entre les
dues, hi ha **la doble recta**: els euros de 0 a 300 a dalt, el percentatge de 0 a 100 a
baix, i una vertical que ensenya que **240 € i 80 % cauen exactament al mateix lloc**.
Els extrems coincideixen amb els de la barra de sobre, de manera que es llegeix com el
mateix objecte amb una regla al costat i no com un dibuix nou.

Amb això el percentatge és **una posició** abans de ser un factor, i el 0,8 de la pàgina 2
arriba com a conclusió d'una cosa que ja ha vist, no com a pas nou. I és literalment el
mòdul Doble recta de la caixa d'eines: paper i pantalla, el mateix cas.

**No expliquis el factor abans d'aquestes dues rectes.** L'avís que ja hi havia val ara
per als tres dibuixos, no per als dos primers.

### L'obertura és una pregunta, no un títol

Cada pàgina 1 s'obre ara amb **una pregunta sense resposta incorrecta**, dins d'una caixa
de traç discontinu amb un ull dibuixat, abans que aparegui cap consigna:

> **Què hi veus?** · Digues-ho o assenyala-ho.

Sembla poca cosa i no ho és. Amb expressió escrita a 3r de primària, qualsevol pregunta
d'obertura que demani una frase li tanca la porta a la primera línia de la fitxa. Una
pregunta de mirar es respon **assenyalant o en veu alta**, no té resposta dolenta, i el
docent hi guanya trenta segons de diagnòstic gratuït sobre què ha vist abans de començar.

És compatible amb la regla de «cap paràgraf»: **set paraules a tota la caixa**, i és de
les poques frases de la fitxa que no etiqueta res sinó que demana. Les set fitxes han
crescut entre 6 i 27 paraules amb tots els canvis d'aquesta versió, de manera que la
densitat que ja funcionava es manté.

**Si algun dia el docent la vol treure**, és una sola línia per fitxa i està marcada amb
`<!--§obertura p.1§-->`.

### Una cosa cada vegada, i la pantalla neta

Quan una explicació té passos, **cada pas esborra l'anterior** en comptes d'acumular-s'hi
al costat. Els mòduls de l'app ja revelen pas a pas; el que cal vigilar és que el pas 3 no
deixi a la vista l'1 i el 2. Els seus colls d'ampolla no són de comprensió, són de càrrega,
i una pantalla que acumula és càrrega que no aporta res.

### La regla trencada

A cada unitat hi ha **un exercici que trenca la regla que l'alumnat s'haurà fabricat
als apartats anteriors**. No és un adorn: és el que distingeix calcular de recordar,
i sol ser l'evidència d'avaluació més valuosa de la fitxa.

| Unitat | La regla que es fabrica | L'exercici que la trenca |
|---|---|---|
| 1 | «Arrodonir és tallar» | Ex. 3: 2,64 s'arrodoneix a **2,65** |
| 2 | «Al comptat sempre és millor» | Ex. 5c: el portàtil surt millor **a terminis** |
| 3 | «Com més gran el paquet, més barat» | Ex. 6c: guanya **l'ampolla petita** |
| 4 | «El negatiu no val mai» | Ex. 5d: al congelador la bona és **−3 °C** |
| 5 | «El vèrtex és el punt més alt i sempre hi ha dos talls» | Ex. 2: vèrtex **mínim** i **cap tall** |
| 6 | «Els gràfics diuen la veritat» | Ex. 6: l'eix que comença a **90 i no a 0** |
| 7 | «Totes les combinacions són igual de probables» | Ex. 4c: **una cara i una creu** val el doble |

---

## 6. El material que hi ha

**Set fitxes imprimibles**, una per unitat, totes amb la mateixa estructura: pàgines
de concepte sense text seguit, sis o set exercicis amb el primer apartat resolt, i un
**solucionari per al professorat** amb els errors típics anotats i la traça als
criteris d'avaluació.

**La caixa d'eines** (`caixa-eines.html`): fitxer únic, vainilla, sense CDN ni
dependències, amb vuit mòduls. Cada eina **s'obre ja resolta** amb un exemple i un botó
la buida per al cas de l'alumnat.

| Mòdul | Unitat | Què fa |
|---|---|---|
| Recta | 1 | Situa el nombre i ensenya l'arrodoniment amb una tira de xifres que s'apaguen |
| Doble recta | 2, 3 i 7 | Dues magnituds alineades; l'expressió amb números apareix quan mou el punt |
| Percentatges | 2 | Factor multiplicador i mode de quotes; compara dues maneres de pagar |
| Escales | 3 | Cadena de conversió visible: 8 cm → ×100 → 800 cm → ÷100 → 8 m |
| Equacions | 4 | Balança que es mou; prova valors i mira de quina banda cau |
| Paràboles | 5 | Toca el vèrtex, els talls i l'eix sobre tres fenòmens reals |
| Calculadora | totes | Demostració tecla a tecla de la Casio fx-82SP CW |
| Com ho dic | totes | Frases model per completar i copiar |

**Paper i pantalla mostren el mateix cas.** Els pictogrames de precisió de la U1, els
300 € de la U2, el 1:100 amb 8 cm de la U3, el x+3=7 de la U4 i els tres fenòmens de la
U5 són idèntics a la fitxa i a l'app. No és estètic: evita que hagi d'aprendre dues
vegades el mateix.

**El que falta.** No hi ha mòdul d'estadística ni d'atzar. Per a la U6 l'eina és el
full de càlcul mateix, que ja fa servir al nivell del grup; per a la U7, un mòdul
d'arbre interactiu seria l'addició natural si es veu que li cal.

**Avís permanent sobre `repas-main`.** Està calibrat per a alumnat que entra a
batxillerat. **No li passis ni el diagnòstic inicial ni l'itinerari automàtic**: el
situarien en fals. Només els blocs concrets que s'indiquen a cada unitat.

---

## 7. Mapa unitat per unitat

> **Nota de numeració.** La programació té 7 SA i el llibre té 9 UD, i a partir del
> febrer divergeixen. La **U4 de la programació és Equacions**, mentre que la **UD4 del
> llibre és Mesura indirecta**. Les fitxes segueixen la numeració de la programació.

---

### U1 · Nombres reals des de l'estimació
**14–30 setembre · 6 sessions · llibre `llibre · unitat 1`**

**Objectiu nuclear:** situar nombres a la recta, estimar abans de calcular i decidir
quants decimals calen a cada situació.

**Encaix:** bo. La recta és visual; el que costa és operar-hi, i això va a la calculadora.

**Base prèvia (aula de suport):** `1eso-ud5-2`, `1eso-ud5-5` (decimals i quadrats perfectes),
`2eso-ud1-2` (la recta de terra), `1eso-ud5-6` (el mapa dels nombres).
**`repas-main`:** full 1, blocs `decimals` i `fraccions`, només els primers ítems.

**A la fitxa:** el mapa dels nombres, √2 que no s'acaba contra √9 que sí, i els tres
usos amb pictograma (ho dic / ho compro / ho tallo) que després reapareixen a l'app.

**Fita:** AS al criteri 5.1, amb AN possible al 8.3.

---

### U2 · Percentatges i matemàtica financera
**6 octubre – 3 novembre · 15 sessions · llibre `llibre · unitat 2`**

**Objectiu nuclear:** fer servir el factor multiplicador amb la calculadora per
comparar dues maneres de pagar una compra i dir quina surt més a compte.

**Encaix:** millor del que sembla. **El factor multiplicador és la millor adaptació del
curs i ja la tenies dissenyada per a tothom**: converteix tot el treball de percentatges
en una sola multiplicació i elimina el pas on alumnat amb aritmètica de 5è es perd.

**Base prèvia (aula de suport):** `1eso-ud4-7`, `2eso-ud2-3`, `2eso-ud2-5`.
**`repas-main`:** full 6, blocs `percentatges` i `factor_multiplicador`; `encadenats`
només si els anteriors van rodats.

**A la fitxa:** la pàgina 1 parteix la barra de 300 € i en fa sortir «de cada 100, en
queden 80»; el factor 0,8 apareix a la pàgina 2 com a conclusió, no com a recepta. Després
la trampa dels encadenats (303 € ≠ 290,40 €). L'exercici 5 compara comptat contra quotes,
que és el producte final de la unitat.

**No expliquis la regla del factor abans de la barra.** Si es dona primer, la seqüència
de les dues primeres pàgines perd tot el sentit.

**Producte «Informe de decisió de compra»:** **és qui munta el full de càlcul i el diagrama
de sectors del grup.** És la representació que demana el producte, feta al nivell que toca.

**Fita:** AS al 1.1 i al 5.1. Per durada, és on més evidència pots recollir.

---

### U3 · Proporcionalitat i escales
**12–27 gener · 7 sessions · llibre `llibre · unitat 3`**

**Objectiu nuclear:** llegir una escala, passar de plànol a realitat i decidir si una
situació és de proporcionalitat directa o inversa.

**Encaix:** molt bo. Plànols i escales són geometria visual pura.

**Base prèvia (aula de suport):** `2eso-ud2-1`, `2eso-ud2-2`, `2eso-ud2-4`, `2eso-ud5-3`,
`2eso-ud5-12`.
**`repas-main`:** full 8, blocs `escales` i `escales_calcul`; full 6, `directa_inversa`.

**A la fitxa:** la cadena de tres baules sempre igual, les taules amb fletxes per a
directa/inversa, i un **plànol dibuixat a escala 1:100 real** que pot mesurar amb regle
si s'imprimeix al 100 %. L'exercici 6 treballa el preu unitari, que la programació demana
com a lectura crítica d'ofertes.

**Truc útil:** per a directa/inversa, fer-li dir en veu alta «més… i més…» o «més… i
menys…». La paraula *menys* ja li dona la resposta sense raonament abstracte.

**El «per unitat» ja és un pas propi.** L'exercici 6 ajuntava dues coses diferents en una
sola consigna: arribar a **quant costa 1** i **fer servir aquest 1 per comparar**. Ara la
consigna són dues frases («Primer baixa a una unitat. Després compara.») i hi ha una cadena
de tres baules a sobre: *preu ÷ quantitat → preu d'1 → compara*. Baixar a la unitat és el
moviment que fa comparables dues coses que no ho eren; si va enganxat a la comparació, el
que se li queda és una recepta, i si va separat, se li queda l'eina.

**Producte «A escala real»:** és qui fa el mesurament i el dibuix del plànol.

**Fita:** AS al 1.1, amb AN a la part d'escales si es valora el plànol produït.

---

### U4 · Equacions de 2n grau
**2 febrer – 3 març · 12 sessions · llibre `llibre · unitat 5`**

**Aquesta és la unitat difícil, i la fitxa ho assumeix explícitament.** No li demana en
cap moment aïllar la incògnita ni aplicar la fórmula general: amb manipulació algebraica
de 5è, aquesta distància no es tanca amb suports.

**Objectiu nuclear (retallat, però real):** entendre l'equació amb la balança; comprovar
si un número és solució; resoldre x² = k amb l'arrel; i **decidir quina de les dues
solucions té sentit**. Aquesta última part és el fil de la SA («i té sentit?») i és
avaluable pel criteri 1.1 sense àlgebra.

**On lluirà:** comprovar. Substituir un valor i comparar les dues bandes és aritmètica
de calculadora, sense manipulació. Val la pena que se n'adoni.

**Si la balança no acaba d'agafar, hi ha sortida i no és estrenar res.** La U4 és
l'única unitat que introdueix un model nou en el pitjor moment del curs. Si es veu que la
balança no li diu res, **l'alternativa és fer l'equació per la doble recta**, que al febrer
ja portarà treballada des de la U2 i la U3. No és millor model: és el model que ja té.
Estrenar-ne un de nou al febrer és el que convé evitar, no la balança en si.

**Base prèvia (aula de suport, i amb temps):** `2eso-ud4-1` (la balança), `2eso-ud4-3` (solució i
comprovació), `2eso-ud4-7`.
**`repas-main`:** full 5, bloc `primer_grau` **únicament**. No obris `formula_general`
ni `factoritzacio`.

**A la fitxa:** balances dibuixades, comprovació en columnes, x² = k amb l'arrel, i
l'exercici 6 que toca una equació de 2n grau completa **entrant-hi per la comprovació**,
amb la taula trossejada perquè cada casella sigui una sola tecla.

**Fita: NA o AS.** El PI ho ha de recollir des d'ara perquè al febrer no es llegeixi com
un fracàs sobrevingut. Ve just abans de la seva millor unitat.

---

### U5 · La paràbola
**9–26 març · 8 sessions · llibre `llibre · unitat 6`**

**La seva millor unitat del curs, i la fitxa no està rebaixada.** La programació ja
prioritza «la lectura i la interpretació gràfica per sobre de l'estudi analític», i això
és exactament el canal on té nivell de 2n ESO, treballat amb GeoGebra, on va al nivell del grup.

**Objectiu nuclear:** llegir orientació, vèrtex, talls i eix de simetria, i dir què
significa cada element en el fenomen.

**Base prèvia (aula de suport):** `2eso-ud3-2`, `2eso-ud3-3`, `3eso-ud6-2`.
**`repas-main`:** full 10, `funcions_quadratiques`, només ítems de lectura de gràfica.

**A la fitxa:** set exercicis, gairebé tots de lectura pura. L'exercici 5 fa validar
lectures amb els dos errors més freqüents de la unitat: el vèrtex amb les coordenades
canviades i confondre l'eix vertical amb l'horitzontal. L'exercici 7a és la mateixa
equació que va comprovar a la U4: val la pena posar les dues fitxes juntes damunt la taula.

**Producte «El fenomen parabòlic»: el pot fer sencer i sol, amb GeoGebra.** És el moment
del curs per dir-li-ho i perquè el grup ho vegi.

**Fita: AN**, i AE no és impensable al criteri 5.1.

---

### U6 · Estadística amb dades reals
**13 abril – 6 maig · 10 sessions · llibre `llibre · unitat 8`**

**Objectiu nuclear:** recollir dades, organitzar-les en taula i gràfic amb el full de
càlcul, i dir si estan juntes o escampades.

**Encaix:** molt bo. Gràfics (canal fort) més full de càlcul (canal molt fort).

**La dispersió hi entra com a idea visual, no com a fórmula.** «Aquestes dades estan
més escampades que aquelles» és estadística de veritat i és el que se li ha d'avaluar.

**La mitjana simple ja entra pel mateix gest, a la pàgina 3.** Al costat de la fila que
deia «sumar-ho tot i dividir entre 9» hi ha ara el dibuix del **repartiment**: les nou
columnes de gols tal com estan, una fletxa, i les mateixes nou columnes aplanades a 2.
Són **les dades que ja hi havia en aquella pàgina** (0 1 1 1 2 2 3 4 4, que sumen 18), de
manera que el dibuix no afegeix cas nou: dona sentit al que la taula ja deia.

Amb això la unitat té una rampa de dos graons en comptes d'un: **pàgina 3, aplanar coses
que pesen igual; pàgina 4, aplanar coses que pesen diferent.** El model d'àrea de la
ponderada no ha canviat, però ara arriba amb el gest ja après.

**La mitjana ponderada entra per un model d'àrea** (pàgina 4): cada part és un rectangle
d'amplada el pes i altura la nota, i la nota final és l'altura que quedaria si s'aplanés
tot. Es veu d'un cop d'ull que el projecte, amb un 7 i pes 0,5, pesa més que la feina
diària amb un 8 i pes 0,2. Això explica en un dibuix per què no es pot sumar i dividir
entre tres, que és l'error típic. La taula de càlcul ve després.

**Base prèvia (aula de suport):** la unitat `2eso-ud6` **sencera**, «Dades que parlen». És de les
poques vegades que una unitat de 2n cobreix gairebé tot el nucli de la del nivell del grup: no la
fragmentis.
**`repas-main`:** full 11, blocs `frequencies`, `grafics` i `centralitzacio`. El bloc
`dispersio` **no**: és de nivell de batxillerat.

**A la fitxa:** dues jugadores amb la mateixa mitjana i dispersió diferent, i
l'exercici del gràfic enganyós amb l'eix truncat, que és **el més valuós de la fitxa fora
de l'aula**: li servirà cada vegada que vegi un gràfic en una notícia.

**Producte «Estudi estadístic propi»:** és el responsable de dades i gràfics del grup.

**Fita:** AS sòlid, amb AN a la part de representació.

---

### U7 · Atzar i decisions
**13 maig – 10 juny · 10 sessions · llibre `llibre · unitat 9`**

**Objectiu nuclear:** comptar amb arbre, dir quin fet és més probable i entendre per què
la casa guanya.

**Encaix:** bo. L'arbre és visual i la unitat exclou els nombres combinatoris: comptar
branques és comptar, no calcular. Laplace es fa amb calculadora i s'expressa en
percentatge, format que ja domina des de la U2.

**Base prèvia (aula de suport):** `3eso-ud2-2` (el llenguatge de l'atzar), `3eso-ud2-3` (comptar
sense oblidar-se de res), `3eso-ud2-5` (Laplace).
**`repas-main`:** full 12, blocs `espais_mostrals` i `laplace`. No `probabilitat_composta`
ni `condicionada`.

**A la fitxa, la probabilitat s'amida abans de calcular-se.** A la pàgina 3, abans de la
taula que compta casos, hi ha la barra partida en sis trossos iguals amb el 5 marcat i
l'escala de percentatge a sota: es veu que un tros de sis és 16,7 % **abans** que la
cadena ho divideixi. És la mateixa escala de la U2, i per això el mòdul Doble recta li
serveix també aquí.

**Això no toca l'arbre.** L'arbre continua sent per a **comptar**, que és una altra feina.
La barra respon «quant val», l'arbre respon «quants n'hi ha».

**A la fitxa:** la línia de la probabilitat, l'arbre del menú, i **el joc de fira**: pagues
2 €, en cobres 8 si surt un 6, i en 60 tirades hi perds 40 €. Tot són multiplicacions i
restes amb calculadora, i el resultat és una decisió clara. El joc sembla generós i tot i
així s'hi perd: és exactament la sensació que exploten les apostes reals.

**Va més enllà de les matemàtiques.** Un perfil amb dificultats de tipus cognitiu té més vulnerabilitat davant
d'apostes i sortejos. Els exercicis 5 i 6 (els paranys i la fal·làcia del jugador)
convé que els faci sencers encara que la resta hagi anat més just.

**Fita:** AS, amb AN possible al recompte amb arbre.

---

### Dues unitats del llibre sense fitxa de programació

- **UD4 «Mesura indirecta»** (`llibre · unitat 4`) — semblança, ombres i Pitàgores. Si la fas,
  **és la segona millor unitat del curs per a aquest alumnat**: sortir a mesurar l'institut
  amb ombres i triangles és 100 % visual i manipulatiu. Base directa a `2eso-ud5-4`,
  `2eso-ud5-5` i tota la `3eso-ud3`.
- **UD7 «Funcions: llegir i interpretar gràfics»** (`llibre · unitat 7`) — també molt
  favorable, i la detecció de gràfics enganyosos (7.4) enllaça amb la U6.

**Si en algun moment cal retallar temari, retalla de la U4 (equacions) i no
d'aquestes.**

---

## 8. Avaluació

**El que no canvia:** els criteris del currículum, amb els mateixos codis.

**El que canvia són dues coses:**

1. **El nivell d'assoliment esperat**, unitat per unitat. El PI l'ha de recollir perquè
   es pugui avaluar amb referència a aquest nivell i no al del grup.

   | Unitat | Fita | Criteri on més pot lluir |
   |---|---|---|
   | 1 Nombres reals | AS | 5.1, i 8.3 possible |
   | 2 Financera | AS | 1.1 i 5.1 |
   | 3 Escales | AS, AN a escales | 1.1 |
   | 4 Equacions | **NA o AS** | 1.1 (interpretar solucions) |
   | 5 Paràbola | **AN, AE possible** | 5.1 |
   | 6 Estadística | AS sòlid, AN a representació | 5.1 i 2.1 |
   | 7 Atzar | AS, AN al recompte | 1.1 i 2.1 |

2. **El format de l'evidència.** Valen exactament igual que un examen escrit: explicació
   oral registrada en el moment, assenyalar sobre una gràfica o un plànol, ordenar
   targetes, triar la frase correcta entre tres, la captura del GeoGebra o del full de
   càlcul que ha construït, i el codi de verificació de `repas-main`.

**Dues valoracions separades al cap.** En qualsevol tasca, mira per separat si la
**decisió** és correcta i si el **càlcul** és correcte. Quan l'objectiu és decidir, només
la primera compta. Sense aquesta separació explícita, els errors aritmètics de nivell de
5è s'ho empassaran tot i la nota no dirà res del que sap.

**Les proves.** Meitat d'ítems, calculadora, exemple resolt visible, enunciats d'una sola
frase i cap pregunta de justificació oberta. Els solucionaris de les fitxes ja porten la
traça als criteris, i serveixen directament per construir-les.

---

## 9. El que caldrà vigilar

- **La franja horària de l'aula de suport.** Si cau *després* de la introducció del tema a l'aula,
  tot aquest plantejament perd la meitat de la força. És el que val la pena negociar primer.
- **El material visual de fora ve amb la calculadora prohibida.** Gairebé tot el bon
  material de raonament visual que hi ha publicat està pensat per construir fluïdesa
  mental en alumnat de primària i secundària baixa, i per això els seus enunciats diuen
  «sense calculadora» i «convenç-me». **Cap de les dues coses es transfereix aquí.** Per a
  aquest alumnat el càlcul és el vehicle, no l'objectiu, i l'argumentació oberta és el coll
  d'ampolla, no l'evidència. S'agafa el model i es deixa la consigna: la calculadora es
  queda sobre la taula i el «convenç-me» es tradueix a frase model o tria entre tres.
- **La calculadora no ha de ser una crossa opaca.** La pregunta «què has demanat a la
  calculadora, i per què?» és la que manté viva la comprensió.
- **El febrer.** La U4 coincideix amb el moment de més acumulació de frustració. La fita
  baixa ja hi és prevista, i la paràbola ve just després.
- **Revisió del PI al desembre.** Les tres primeres unitats et diran si el nivell de 5è
  en aritmètica és estable o si amb calculadora funciona per sobre del que sembla. És el
  moment de recalibrar les fites de la taula de l'apartat 8.
- **La lletra manuscrita de les fitxes.** Depèn de les fonts instal·lades als ordinadors
  del centre. Si no surt lligada, hi ha un bloc `@font-face` comentat al principi del CSS
  de cada fitxa: només cal desar un `.woff2` al costat i descomentar-lo.
- **El teclat de la calculadora a l'app.** La disposició de tecles i l'etiqueta `FORMAT`
  estan pendents de contrastar amb una fx-82SP CW real. Hi ha una constant `SEP_DECIMAL`
  per si les vostres unitats estan configurades amb coma en comptes de punt.
