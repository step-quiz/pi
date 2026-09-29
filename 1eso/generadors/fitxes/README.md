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

Les peces comunes: `fitxa_ud1.py` (la classe `Dibuix`, `ms()`, `buit()`, els colors: els altres
n'executen la primera part), `peces_ud2.py` (opcions per marcar, pàgines, el document, la graella
de 100, els rectangles, l'arbre de factors) i `peces_fraccions.py` (`fr()`, les tires, les caixes).
Si canvies una fitxa a mà, el generador ja no la farà igual: canvia-la sempre al generador.
