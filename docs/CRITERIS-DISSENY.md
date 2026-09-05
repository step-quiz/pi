# Criteris de disseny

Vuit regles. **No són preferències d'estil**: són el resultat d'iterar amb el docent, i
algunes van sortir de correccions seves. Qui toqui el material les ha de conèixer abans.

---

## 1. Blanc i negre estricte a les fitxes

Les fitxes s'imprimeixen en B/N al centre i no se sap com quedarien els colors. Cap
valor cromàtic: només negres, blancs i grisos. Les diferències es fan amb **nivells de
gris, gruix de línia i tipus de traç** (continu, discontinu, ratllat).

Les tres classes d'avís, per exemple, es distingeixen només pel traç: `.avis` és vora
fina, `.avis.puntejat` és discontinu i `.avis.gruixut` és vora de 3 px.

`eines/comprova.py` ho verifica. La regla val per a `fitxes/` i `css/fitxa.css`; les
pàgines de navegació i la caixa d'eines sí que tenen color, perquè no s'imprimeixen mai.

> Aquesta regla va arribar quan les fitxes ja estaven fetes en color. Es va haver de
> refer tot. Val la pena no tornar-hi.

## 2. Cap paràgraf a les pàgines de l'alumne

**El dibuix explica, les paraules només etiqueten.** El que seria una frase explicativa
ha de ser una pantalla de calculadora, una barra, una cadena de fletxes o un pictograma.

La densitat que funciona va de 181 paraules (Unitat 1) a 539 (Unitat 7, on els missatges
de les apostes s'han de citar literalment). Puja a les unitats amb molt context real; el
que no puja mai és la llargada de cada frase.

La regla val per a les pàgines de l'alumne. **No val** per als solucionaris ni per a les
pàgines de navegació, que són per a l'adult.

> La primera versió de la fitxa de la U1 tenia unes 700 paraules. El docent va dir que
> era impossible que l'alumne la llegís. Tenia raó, i d'aquí va sortir tot el format.

## 3. Consignes completes però curtes

En imperatiu i d'una sola frase, sense subordinades. «Encercla el nombre que té xifres
decimals que s'acaben», no «Encercla el que s'acaba».

> També és una correcció del docent: la primera versió era telegràfica i quedava
> ambigua. Curt no vol dir incomplet.

## 4. Cos de 14 pt cap amunt

Consignes a 15,5 pt, números de taula a 15 pt, xifres destacades a 20-26 pt. Interlineat
1,65. Caselles d'1,5 cm d'alçada per escriure-hi a mà amb comoditat.

## 5. El primer apartat, sempre resolt en lletra manuscrita

Veu el model abans de començar, amb una lletra que es distingeix de la impresa. Classes
`.ms`, `.resolt` i `.et-resolt`; la pila de fonts és a `tokens.css`.

**La caixa d'eines fa el mateix**: cada mòdul s'obre ja resolt amb un exemple, i un botó
el buida per al cas de l'alumne.

## 6. El símbol emergeix del dibuix, no s'anuncia al costat

L'ordre de les pàgines conceptuals va de concret a visual a simbòlic.

- A la **U2**, la pàgina 1 només parteix la barra i en surt «de cada 100 €, en queden
  80»; el factor 0,8 no apareix fins a la pàgina 2, com a conclusió.
- A la **U6**, el model d'àrea de la mitjana ponderada va abans de la taula de càlcul.
- A la caixa d'eines, el mòdul **Doble recta** manté l'expressió amb números amagada
  fins que l'alumne mou el punt.

**Conseqüència a l'aula:** si es dona la regla abans, la seqüència perd tot el sentit.
Els solucionaris de la U2 i la U6 hi porten un avís explícit.

## 7. La regla trencada

A cada unitat hi ha **un exercici que trenca la regla que l'alumne s'haurà fabricat** als
apartats anteriors. És el que distingeix calcular de recordar, i sol ser l'evidència
d'avaluació més valuosa de la fitxa.

| Unitat | La regla que es fabrica | L'exercici que la trenca |
|---|---|---|
| 1 | «arrodonir és tallar» | Ex. 3 · 2,64 s'arrodoneix a **2,65** |
| 2 | «al comptat sempre és millor» | Ex. 5c · el portàtil surt millor **a terminis** |
| 3 | «com més gran el paquet, més barat» | Ex. 6c · guanya **l'ampolla petita** |
| 4 | «el negatiu no val mai» | Ex. 5d · al congelador la bona és **−3 °C** |
| 5 | «el vèrtex és el punt més alt i sempre hi ha dos talls» | Ex. 2 · vèrtex **mínim** i **cap tall** |
| 6 | «els gràfics diuen la veritat» | Ex. 6 · l'eix que comença a **90 i no a 0** |
| 7 | «totes les combinacions són igual de probables» | Ex. 4c · **una cara i una creu** val el doble |

Si mai cal escurçar una fitxa, aquest exercici és l'últim que s'ha de treure.

## 8. Paper i pantalla mostren el mateix cas

Els pictogrames de precisió de la U1, els 300 € de la U2, el 1:100 amb 8 cm de la U3, el
`x+3=7` de la U4 i els tres fenòmens de la U5 són **idèntics** a la fitxa i al mòdul
corresponent de la caixa d'eines. No és estètic: evita que hagi d'aprendre dues vegades
el mateix.

---

## L'obertura i el graó físic

Dues coses que van entrar més tard i que completen el format.

**El graó físic.** Cada pàgina 1 porta a dalt de tot, abans del títol i clarament per a
l'adult, un rètol: «Cinc minuts abans, a la SIEI: monedes i bitllets de joguina». El
material concret de cada unitat és a `dades/unitats.js`, i cada solucionari explica què
fer-hi i amb quin dibuix enllaça.

**La pregunta d'obertura.** «Què hi veus? Digues-ho o assenyala-ho.» Es respon
assenyalant o de paraula, no té resposta incorrecta i no toca el coll d'ampolla de
l'expressió escrita.

**L'ordre importa:** pregunta → dibuix → frase que anomena la cosa. Si la frase va
abans del dibuix, la pregunta queda anul·lada perquè ja s'ha respost. Va passar a tres
fitxes i es va haver de corregir.
