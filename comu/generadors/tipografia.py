"""Tipografia comuna dels generadors: que un número no quedi mai sol a final de línia.

    from tipografia import lliga
    html = lliga(html)

El docent ho va demanar el 24/11/2026: a la taula del quadern de la UD3 de 4eso/, «21 €» es partia
en dues línies («21» a dalt i «€» a sota), i «I 5 entrades?» també. La regla:

  · un número va lligat a la paraula o al símbol que el segueix: «21 €», «5 entrades», «4 kg»;
  · una escala no es parteix: «1 : 100»;
  · un signe que en separa dos (×, ÷, ·, =, +, −) va lligat al número de després: «7 × 5», «4 · x»;
  · una paraula d'una sola lletra va lligada al número que la segueix: «I 5 entrades?», «x 10».

Només es toca el text que es veu: no els atributs, els comentaris, els <script>, els <style> ni els
dibuixos (<svg>), on el text no es parteix mai. L'espai lligat és el caràcter U+00A0, que es veu igual
que un espai normal.
"""
import re

NBSP = " "
_PROTEGIT = re.compile(r"(<!--.*?-->|<script\b.*?</script>|<style\b.*?</style>|<svg\b.*?</svg>|<[^>]+>)", re.S)
_NUM_PARAULA = re.compile(r"(\d) (?=[A-Za-zÀ-ÿ€%²³])")
_ESCALA = re.compile(r"(\d) : (\d)")
_SIGNE = re.compile(r" ([×÷·=+−]) (?=[\dx(])")
_LLETRA = re.compile(r"(?<![\wÀ-ÿ'’])([A-Za-zÀ-ÿ]) (?=\d)")


def _text(t):
    t = _ESCALA.sub(lambda m: f"{m[1]}{NBSP}:{NBSP}{m[2]}", t)
    t = _NUM_PARAULA.sub(lambda m: m[1] + NBSP, t)
    t = _SIGNE.sub(lambda m: f" {m[1]}{NBSP}", t)
    t = _LLETRA.sub(lambda m: m[1] + NBSP, t)
    return t


def lliga(html):
    """Torna l'html amb els espais lligats al text visible (vegeu la capçalera)."""
    trossos = _PROTEGIT.split(html)
    return "".join(t if i % 2 else _text(t) for i, t in enumerate(trossos))
