#!/usr/bin/env python3
"""Genera 1eso/fitxes/ud5-sumes.html: sumar i restar decimals (unitat 5, fitxa 3).

Adapta la primera part de l'activitat 3 de la situació «Decimals i arrel quadrada» (el llibre:
«Sumar i restar: la coma sota la coma»). Sumar decimals és sumar quadrats amb quadrats, columnes
amb columnes i quadrets amb quadrets: per això la coma va sota la coma. Són els blocs de la fitxa 1
i de la tasca 20 de la caixa.

Sempre sense portar-ne (regla D). Multiplicar i dividir decimals queden fora (el pla validat el
29/9/2026). Els casos són els de la tasca 20 de la caixa i els del llibre (2,50 + 1,35 = 3,85 i
3,2 + 1,45 = 4,65). A la vida, euros i cèntims: un euro són 100 cèntims, com el quadrat de 100.

La regla trencada (regla G): posar les xifres a la dreta, sense mirar la coma
(2,5 + 1,35 = 1,60), a la pàgina 4. Les operacions mal fetes van dins de .revisa, perquè
eines/comprova.py no les doni per errors.
"""
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(AQUI, "fitxa_ud1.py"), encoding="utf-8").read()
exec(_src[:_src.index("pagines = []")])                       # Dibuix, ms, buit, ULL, els colors
exec(open(os.path.join(AQUI, "peces_ud2.py"), encoding="utf-8").read())          # tria, fes_pagina, document
exec(open(os.path.join(AQUI, "peces_fraccions.py"), encoding="utf-8").read())    # caixa
_nombres = open(os.path.join(AQUI, "fitxa_ud1_nombres.py"), encoding="utf-8").read()
exec(_nombres[_nombres.index("def peca("):_nombres.index("def taula_xifres(")])  # peca() i blocs()

pagines = []
pagina = fes_pagina(pagines, "Unitat 5 · Sumar i restar decimals · pàgina")


def xifres(c):
    return c // 100, c // 10 % 10, c % 10


def dec(c, x=None):
    """Com CE.q.dec a la caixa: 250 → «2,5»; amb x=2, sempre dues xifres decimals: «2,50»."""
    u, r = divmod(c, 100)
    if x == 2:
        return f"{u},{r:02d}"
    if r == 0:
        return str(u)
    return f"{u},{r // 10}" if r % 10 == 0 else f"{u},{r:02d}"


def columna(a, b, resta, estat, cel="1.25cm"):
    """L'operació en columna, amb la coma sota la coma: una casella per xifra i la coma impresa.
    estat: "resolt" (les xifres a mà, amb el zero que iguala), "imprès" (el model, en lletra
    d'impremta) o "buit" (les caselles per omplir)."""
    signe = "−" if resta else "+"
    r = a - b if resta else a + b
    td = f'style="width:{cel};height:1.05cm;text-align:center;font-size:17pt"'
    coma = '<td style="border:0;width:.45cm;text-align:center;font-size:20pt;font-weight:800;background:none">,</td>'
    op = lambda s: f'<td style="border:0;width:.8cm;text-align:center;font-size:18pt;font-weight:800;background:none">{s}</td>'

    def fila(c, s, ultima=False):
        vora = ' style="border-top:3px solid var(--tinta)"' if ultima else ""
        if estat in ("resolt", "imprès"):
            u, dd, q = xifres(c)
            v_ = (lambda t: ms(str(t))) if estat == "resolt" else (lambda t: f"<b>{t}</b>")
            cel_ = [f'<td {td}>{v_(v)}</td>' for v in (u, dd, q)]
        else:
            cel_ = [f'<td class="omplir" {td}></td>'] * 3
        return f'<tr{vora}>{op(s)}{cel_[0]}{coma}{cel_[1]}{cel_[2]}</tr>'
    cap = ('<tr><th style="border:0;background:none"></th><th style="font-size:11.5pt">Unitats</th>'
           '<th style="border:0;background:none"></th><th style="font-size:11.5pt">Dècimes</th>'
           '<th style="font-size:11.5pt">Centèsimes</th></tr>')
    # Dins de .revisa: les xifres van en caselles separades, i el verificador no les pot llegir
    # com una igualtat. L'operació sencera va escrita a la frase del costat, i aquesta sí que es
    # comprova.
    return (f'<table class="mini revisa" style="width:auto;margin:0">{cap}{fila(a, "")}{fila(b, signe)}'
            f'{fila(r, "=", True)}</table>')


# ===================================================================== pàgina 1
def a_lesquerra(d):
    """Els blocs, arrambats a l'esquerra: els de 2,5 i els de 1,35, quadrats sota quadrats."""
    d.estil = "margin-left:0"
    return d


pagina(f'''  <div class="previ">Cinc minuts abans, a l'aula de suport: <b>el material de base 10</b>, amb la placa com a 1. Fer 2,5 i 1,35, i ajuntar plaques amb plaques, barres amb barres i cubs amb cubs.</div>
  <h1>Sumar i restar decimals</h1>
  <p class="nom">Nom: <span></span></p>
  <div class="obertura">{ULL}<div class="q">Què hi veus? <span class="com">Digues-ho o assenyala-ho.</span></div></div>

  <div style="display:grid;grid-template-columns:auto 1fr;gap:.25rem .6cm;align-items:center;margin:.8rem 0 .3rem">
    <p style="margin:0;font-size:20pt;font-weight:800">2,5</p>
    <div>{a_lesquerra(blocs(2, 5, 0, 0.15, "2,5: 2 quadrats de 100 i 5 columnes de 10")).svg("")}</div>
    <p style="margin:0;font-size:20pt;font-weight:800">1,35</p>
    <div>{a_lesquerra(blocs(1, 3, 5, 0.15, "1,35: 1 quadrat de 100, 3 columnes de 10 i 5 quadrets solts")).svg("")}</div>
  </div>
  <p style="font-size:16.5pt;font-weight:700;text-align:center;margin:.2rem 0 .5rem">Ajuntem les peces iguals.</p>

  <table>
    <tr class="resolt"><td class="esq">Quants quadrats de 100 hi ha en total?</td><td style="width:4cm">{ms("3")}</td></tr>
    <tr class="resolt"><td class="esq">Quantes columnes de 10 hi ha en total?</td><td>{ms("8")}</td></tr>
    <tr class="resolt"><td class="esq">Quants quadrets solts hi ha en total?</td><td>{ms("5")}</td></tr>
  </table>

  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">Per això la coma va sota la coma.</p>
    <p style="margin:0 0 .4rem">2,5 és el mateix que 2,50: el zero no canvia res.</p>
    <div style="display:flex;justify-content:center;align-items:center;gap:1cm">
      <div>{columna(250, 135, False, "imprès")}</div>
      <p style="font-size:24pt;font-weight:800;margin:0">2,50 + 1,35<br>= 3,85</p>
    </div>
  </div>''')


# ===================================================================== pàgines 2 i 3: suma i resta
def pagina_ops(n, consigna, clau, casos, resta):
    it = []
    for l, a, b, r in casos:
        s = "−" if resta else "+"
        frase = (f'<p style="margin:.25rem 0 0;font-size:15pt">{dec(a)} {s} {dec(b)} = {ms(dec(a - b if resta else a + b))}</p>'
                 if r else f'<p style="margin:.25rem 0 0;font-size:15pt">{dec(a)} {s} {dec(b)} = {buit()}</p>')
        it.append(caixa(f'''      <p style="margin:0 0 .2rem;font-size:18pt;font-weight:800"><span class="apartat">{l})</span> {dec(a)} {s} {dec(b)}</p>
      {columna(a, b, resta, "resolt" if r else "buit")}
      {frase}''', r, ".3rem"))
    pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">{n}</div><div class="q">{consigna}</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem">{clau}</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.3rem .5cm">
{chr(10).join(it)}
    </div>
  </div>''')


pagina_ops(1, "Escriu els dos nombres a la taula, amb la coma sota la coma. Després suma.",
           '<p style="margin:0">Si un nombre té una sola xifra després de la coma, afegeix un 0. Per exemple, 3,2 és 3,20.</p>',
           [("a", 250, 135, True), ("b", 320, 145, False), ("c", 150, 225, False), ("d", 410, 135, False)], False)
pagina_ops(2, "Escriu els dos nombres a la taula, amb la coma sota la coma. Després resta.",
           '<p style="margin:0">Es treuen quadrats de quadrats, columnes de columnes i quadrets de quadrets.</p>',
           [("a", 585, 230, True), ("b", 475, 150, False), ("c", 368, 140, False), ("d", 690, 250, False)], True)


# ===================================================================== pàgina 4: la regla trencada
def malament(a, b):
    """La suma de la Júlia: les xifres a la dreta, sense mirar la coma, i la coma on la té el
    nombre amb més xifres decimals (2,5 + 1,35 → 25 + 135 = 160 → 1,60). Si tots dos tenen les
    mateixes xifres decimals, surt bé (2,4 + 3,5 = 5,9). Va dins de .revisa: pot ser falsa a posta."""
    sa, sb = dec(a), dec(b)
    xa, xb = int(sa.replace(",", "")), int(sb.replace(",", ""))
    nd = max(len(sa.partition(",")[2]), len(sb.partition(",")[2]))
    r = xa + xb
    rr = f"{r // 10 ** nd},{r % 10 ** nd:0{nd}d}"
    fila = lambda s_, t: (f'<tr><td style="border:0;width:.8cm;text-align:center;font-size:18pt;font-weight:800">{s_}</td>'
                          f'<td style="border:0;text-align:right;font-size:25pt;font-family:var(--manuscrita);'
                          f'color:var(--manuscrit);padding:0 .3rem;letter-spacing:.12em">{t}</td></tr>')
    taula = (f'<table class="revisa" style="border-collapse:collapse;margin:0">{fila("", sa)}{fila("+", sb)}'
             f'<tr><td style="border:0"></td><td style="border:0;border-top:3px solid var(--tinta)"></td></tr>'
             f'{fila("=", rr)}</table>')
    bo = xa + xb == (a + b) * 10 ** nd // 100
    return taula, rr, bo


E3 = [("a", 250, 135, True), ("b", 320, 145, False), ("c", 240, 350, False), ("d", 410, 135, False)]
it = []
for l, a, b, r in E3:
    taula, rr, bo = malament(a, b)
    it.append(caixa(f'''      <p style="margin:0 0 .15rem;font-size:15.5pt;font-weight:700"><span class="apartat">{l})</span> La suma de la Júlia:</p>
      <div style="display:flex;gap:.8cm;align-items:center">
        <div>{taula}</div>
        <div>
          <p style="margin:0;font-size:15pt">Està bé?</p>
          {tria(["Sí", "No"], ("Sí" if bo else "No") if r else None, mida="14pt", ample="2.2cm")}
        </div>
      </div>''', r, ".3rem"))
pagina(f'''  <div class="exercici">
    <div class="tasca"><div class="n">3</div><div class="q">La Júlia posa les xifres a la dreta, sense mirar la coma. Està bé la seva suma?</div></div>
    <div class="clau" style="margin:.3rem 0 .5rem"><p style="margin:0">Mira el resultat. Si és més petit que un dels dos nombres, la suma està malament.</p></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.3rem .5cm">
{chr(10).join(it)}
    </div>
  </div>
  <div class="avis gruixut" style="text-align:center">
    <p style="margin:0;font-weight:700">La coma va sota la coma.</p>
    <p style="margin:.2rem 0 0">2,5 és 2,50. Per això 2,50 + 1,35 = 3,85.</p>
  </div>''')

# ===================================================================== pàgina 5: la vida (euros i cèntims)
V = [("a", "Un entrepà costa 2,50 € i un suc costa 1,35 €. Quant pagues?", "3,85", True),
     ("b", "Una llibreta costa 1,20 € i un llapis costa 0,75 €. Quant pagues?", "1,95", False),
     ("c", "Tens 5,85 €. Gastes 2,30 €. Quants diners tens ara?", "3,55", False),
     ("d", "Tens 4,75 €. Compres un pastís d'1,50 €. Quants diners tens ara?", "3,25", False)]
it = []
for l, t_, res, r in V:
    it.append(caixa(f'''      <p style="margin:0 0 .15rem"><span class="apartat">{l})</span> {t_}</p>
      <p class="frase" style="margin:0">{ms(res + " €") if r else buit() + " €"}</p>''', r, ".3rem"))
pagina(f'''  <h2>A la vida de cada dia</h2>
  <div class="clau" style="margin:.2rem 0 .6rem">
    <p style="margin:0">Un euro són 100 cèntims, com el quadrat de 100 quadrets.</p>
    <p style="margin:0">Una moneda de 10 cèntims és una columna. Una moneda d'1 cèntim és un quadret.</p>
  </div>
  <div class="exercici">
    <div class="tasca"><div class="n">4</div><div class="q">Fes la suma o la resta amb la coma sota la coma.</div></div>
{chr(10).join(it)}
  </div>''', classe="full vida")

# ===================================================================== solucionari
pagines.append('''<div class="full sol">
  <h1 style="font-size:19pt">Solucionari</h1>
  <p style="color:var(--gris-2);margin-top:.15rem">Unitat 5 · Sumar i restar decimals · full per al professorat</p>
  <div class="abans">
    <b>Abans de començar.</b> Sumar decimals és sumar quadrats amb quadrats, columnes amb columnes i
    quadrets amb quadrets: per això la coma va sota la coma. Són els blocs de la fitxa 1. Cap
    operació no porta: cap lloc no passa de 9, i a les restes cap xifra de dalt no és més petita
    que la de sota. Multiplicar i dividir decimals queden fora. La targeta «Decimals i arrels» porta
    la regla.
  </div>
  <h3>El graó físic, abans de la pàgina 1</h3>
  <p>Cinc minuts amb el material de base 10, dient que la placa és 1: una barra és 0,1 i un cub és
  0,01. Fer 2,5 (2 plaques i 5 barres) i 1,35 (1 placa, 3 barres i 5 cubs), i ajuntar-los peça amb
  peça: 3 plaques, 8 barres i 5 cubs, 3,85. Si no hi ha material, serveixen les monedes: 1 €,
  10 cèntims i 1 cèntim.</p>
  <h3>1. Suma amb la coma sota la coma</h3>
  <p>b) 3,20 + 1,45 = 4,65 (el cas del llibre). c) 1,50 + 2,25 = 3,75. d) 4,10 + 1,35 = 5,45.
  <b>Error típic:</b> escriure 3,2 a la dreta de tot, sota el 5 de 1,45. La clau de dalt diu que
  s'hi posi un zero: 3,20.</p>
  <h3>2. Resta amb la coma sota la coma</h3>
  <p>b) 4,75 − 1,50 = 3,25. c) 3,68 − 1,40 = 2,28. d) 6,90 − 2,50 = 4,4 (o 4,40). Amb els blocs,
  es treuen: de 4 quadrats, 7 columnes i 5 quadrets, se'n treuen 1 quadrat i 5 columnes.</p>
</div>''')
pagines.append('''<div class="full sol">
  <h3>3. La suma de la Júlia · la regla trencada</h3>
  <p>b) No: la Júlia escriu 1,77, i és 4,65. c) Sí: 2,4 + 3,5 = 5,9. Quan els dos nombres tenen les
  mateixes xifres després de la coma, posar-les a la dreta ja deixa la coma sota la coma. d) No: la
  Júlia escriu 1,76, i és 5,45. <b>Error típic:</b> posar les xifres a la dreta, com amb els
  nombres de la unitat 1. És la regla trencada d'aquesta fitxa. No l'expliqueu: que miri si el
  resultat és més petit que un dels dos nombres (1,60 és menys que 2,5, i sumant no es fa més
  petit), i que ho faci amb els blocs. L'apartat c és a posta. <b>Compta per als nivells alts, no
  per al mínim.</b></p>
  <h3>4. A la vida de cada dia</h3>
  <p>b) 1,95 €. c) 3,55 €. d) 3,25 €. Els preus ja porten sempre dues xifres: la coma queda sola
  sota la coma. Un euro són 100 cèntims, com el quadrat de 100: una moneda de 10 cèntims és una
  columna i una d'1 cèntim és un quadret.</p>
  <h3>La caixa d'eines</h3>
  <p>Per consolidar, amb l'ordinador: <b style="white-space:nowrap">?task=20</b> (20.1 Suma i resta;
  20.2 Quant és?). La 20.2 dona un codi de verificació; les respostes falses són posar les xifres a
  la dreta (la de la Júlia) i sumar el que hi ha després de la coma com si fos igual (5 + 35 = 40, i
  3,40). L'exemple de la fitxa és el de la caixa, 2,5 + 1,35, i els casos surten de la llista de la
  20.2.</p>
  <h3>Què mirar per avaluar</h3>
  <p>Sempre amb la taula o els blocs al davant. Els criteris de la SA del grup (5.1, 7.1 i 8.1) són
  de referència: l'avaluació es fa amb els criteris del PI.</p>
  <ul>
    <li>Amb el material de base 10, suma dos decimals ajuntant peça amb peça.</li>
    <li>Escriu dos decimals a la taula amb la coma sota la coma, amb el zero que iguala (exercicis 1 i 2).</li>
    <li>Suma i resta decimals sense portar-ne (exercicis 1 i 2).</li>
    <li>Suma i resta preus en euros (exercici 4).</li>
    <li>Nivells alts: diu per què la suma de la Júlia està malament (exercici 3).</li>
  </ul>
</div>''')

document("Unitat 5 · Sumar i restar decimals", """  FITXA · Unitat 5 · Decimals i arrel quadrada · Sumar i restar decimals
  La tercera fitxa de la unitat 5. Adapta la primera part de l'activitat 3 de la
  situació (el llibre: «Sumar i restar: la coma sota la coma»). Es sumen quadrats
  amb quadrats, columnes amb columnes i quadrets amb quadrets: la coma va sota la
  coma. Sense portar-ne. Els casos són els de la tasca 20 de la caixa i els del
  llibre (regla 8).

  La regla trencada és posar les xifres a la dreta, sense mirar la coma (la
  Júlia, pàgina 4). Les operacions mal fetes van dins de .revisa.""", pagines,
    sys.argv[1] if len(sys.argv) > 1 else "ud5-sumes.html")
