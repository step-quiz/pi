# Els generadors de les fitxes

Cada fitxa de `fitxes/` i la targeta de les fraccions surten d'un script d'aquesta carpeta. Per
refer-ne una, o fer-ne una de nova a partir de la més semblant:

```bash
python3 1eso/generadors/fitxes/fitxa_ud3_area.py 1eso/fitxes/ud3-area.html
python3 1eso/eines/mesura_chromium.py 1eso/fitxes/ud3-area.html     # cada pàgina, en un A4?
python3 1eso/eines/comprova.py                                     # l'estructura, la llengua i els càlculs
```

| Generador | Fa | Generador | Fa |
|---|---|---|---|
| `fitxa_ud1.py` | `ud1.html` (i les peces de dibuix de tots) | `fitxa_ud3.py` | `ud3.html` |
| `fitxa_ud1_nombres.py` | `ud1-nombres.html` | `fitxa_ud3_area.py` | `ud3-area.html` |
| `fitxa_ud1_ordre.py` | `ud1-ordre.html` | `fitxa_ud3_compara.py` | `ud3-compara.html` |
| `fitxa_ud1_repas.py` | `ud1-repas.html` | `fitxa_ud3_equivalents.py` | `ud3-equivalents.html` |
| `fitxa_ud2.py` | `ud2.html` | `fitxa_ud3_sumes.py` | `ud3-sumes.html` |
| `fitxa_ud2_repartir.py` | `ud2-repartir.html` | `fitxa_ud3_mapes.py` | `ud3-mapes.html` |
| `fitxa_ud2_divisors.py` | `ud2-divisors.html` | `fitxa_ud3_repas.py` | `ud3-repas.html` |
| `fitxa_ud2_factors.py` | `ud2-factors.html` | `targeta_fraccions.py` | `targetes/fraccions.html` |
| `fitxa_ud2_repas.py` | `ud2-repas.html` | `targeta_decimals.py` | `targetes/decimals.html` |
| `fitxa_ud4.py` | `ud4.html` | `fitxa_ud5.py` | `ud5.html` |
| `fitxa_ud4_multfrac.py` | `ud4-multfrac.html` | `fitxa_ud5_arrodonir.py` | `ud5-arrodonir.html` |
| `fitxa_ud4_percentatges.py` | `ud4-percentatges.html` | `fitxa_ud5_sumes.py` | `ud5-sumes.html` |
| `fitxa_ud4_dobletriple.py` | `ud4-dobletriple.html` | `fitxa_ud5_fraccions.py` | `ud5-fraccions.html` |
| `fitxa_ud4_repas.py` | `ud4-repas.html` | `fitxa_ud5_arrel.py` | `ud5-arrel.html` |
| | | `fitxa_ud5_repas.py` | `ud5-repas.html` |
| `fitxa_ud6.py` | `ud6.html` | `targeta_formes.py` | `targetes/formes.html` |
| `fitxa_ud6_poligons.py` | `ud6-poligons.html` | `peces_geo.py` | (les peces de dibuix de la unitat 6) |
| `fitxa_ud6_triangles.py` | `ud6-triangles.html` | `fitxa_ud6_cercle.py` | `ud6-cercle.html` |
| `fitxa_ud6_perimetre.py` | `ud6-perimetre.html` | `fitxa_ud6_repas.py` | `ud6-repas.html` |
| `fitxa_ud7.py` | `ud7.html` | `targeta_patrons.py` | `targetes/patrons.html` |
| `fitxa_ud7_regla.py` | `ud7-regla.html` | `fitxa_ud7_simbols.py` | `ud7-simbols.html` |
| `fitxa_ud7_grafics.py` | `ud7-grafics.html` | `fitxa_ud7_repas.py` | `ud7-repas.html` |

Les peces comunes són mòduls, i cada generador les importa (`from peces_comunes import *`):

| Mòdul | Què hi ha |
|---|---|
| `peces_comunes.py` | la classe `Dibuix`, els colors, `ms()`, `buit()`, `ULL` i `desa()`, que escriu l'HTML |
| `peces_ud2.py` | opcions per marcar, pàgines, el document, la graella de 100, els rectangles, l'arbre de factors |
| `peces_fraccions.py` | `fr()`, les tires, les caixes |
| `peces_nombres.py` | `peca()` i `blocs()`: centenes, desenes i unitats |
| `peces_geo.py` | les peces de dibuix de la unitat 6 |

Fins al 30/9/2026 no eren mòduls: els generadors executaven amb `exec()` un tros de
`fitxa_ud1.py` (fins a la línia `pagines = []`) i dels altres fitxers. Si aquella línia es movia,
deixaven de funcionar. `eines/comprova.py` vigila que no torni a passar.

**Cada HTML diu de quin generador surt**, a la segona línia: `<!-- Generat per … -->`. Si canvies
una fitxa a mà, el generador ja no la farà igual i el canvi es perdrà: canvia-la sempre al
generador. L'única feta a mà és la targeta de les taules (`targetes/taules.html`).
