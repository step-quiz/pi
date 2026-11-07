#!/usr/bin/env python3
"""
comu/eines/prova_veu.py · la lectura en veu alta de les eines, provada en un navegador
=====================================================================================

Obre les eines de cada curs (CURS/eines.html) en Chromium, amb una veu catalana falsa (el
navegador de les proves no en té cap), i fa llegir la primera targeta de cada eina. La veu
falsa diu les paraules d'una en una, avisant on és (com Edge i Safari), i a cada paraula es mira
on és la franja groga.

    python3 comu/eines/prova_veu.py

Comprova, a cada targeta:
  · que la franja groga sempre és damunt del bloc que es diu, i mai damunt d'un altre;
  · que el títol amagat de la targeta (h2.repetit, perquè la barra ja el diu) es marca a la
    barra (.sub-rotul), on es veu, i no damunt de la consigna. Abans del 7/11/2026 el groc
    omplia la consigna mentre la veu deia el títol, i després tornava a començar: semblava
    que la lectura saltava enrere;
  · que la lectura acaba sola i deixa la targeta com era (sense franja ni res apagat).

Necessita Playwright amb Chromium, com les altres proves de navegador.
"""
import os
import pathlib
import sys

os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
from playwright.sync_api import sync_playwright  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
falles = []


def comprova(cond, msg):
    if not cond:
        falles.append(msg)


# La veu falsa: una veu catalana «natural», que diu cada paraula en 15 ms i avisa on és.
VEU = """
(() => {
  const veus = [{ name: "Joana (natural)", lang: "ca-ES", localService: false, default: false }];
  let actual = null;
  window.__dits = []; window.__mostres = [];
  const franges = () => [...document.querySelectorAll('.veu-retolador')]
    .filter(f => f.style.opacity !== '0' && parseFloat(f.style.width) > 0)
    .map(f => ({ l: parseFloat(f.style.left), t: parseFloat(f.style.top),
                 r: parseFloat(f.style.left) + parseFloat(f.style.width), b: parseFloat(f.style.top) + parseFloat(f.style.height) }));
  const fals = {
    speaking: false, pending: false,
    getVoices: () => veus,
    addEventListener() {}, removeEventListener() {},
    speak(u) {
      const meva = actual = {};
      window.__dits.push(u.text);
      const paraules = [...u.text.matchAll(/\\S+/g)];
      let i = 0;
      this.speaking = true;
      const pas = () => {
        if (actual !== meva) return;
        if (i < paraules.length) {
          u.onboundary && u.onboundary({ name: "word", charIndex: paraules[i].index });
          window.__mostres.push({ text: u.text, paraula: paraules[i][0], franges: franges() });
          i++; setTimeout(pas, 15);
        } else { this.speaking = false; actual = null; u.onend && u.onend({}); }
      };
      setTimeout(pas, 5);
    },
    cancel() { actual = null; this.speaking = false; },
  };
  Object.defineProperty(window, "speechSynthesis", { value: fals, configurable: true });
  // La frase falsa: el navegador no accepta una veu falsa a la de debò.
  window.SpeechSynthesisUtterance = class { constructor(text) { this.text = text; } };
})();
"""

# On ha de caure la franja de cada bloc: la caixa de l'element que es veu (el títol, a la barra).
ON_ES = """
(t) => {
  const net = s => s.replace(/\\s+/g, ' ').trim();
  const caixa = el => { const c = el.getBoundingClientRect();
    return { l: c.left + scrollX, t: c.top + scrollY, r: c.right + scrollX, b: c.bottom + scrollY }; };
  const fora = [...t.querySelectorAll('h2.repetit')].map(h => net(h.textContent));
  const rotul = [...document.querySelectorAll('.sub-rotul')].find(r => r.getClientRects().length);
  return CE.veu.blocs(t).map(b => ({
    text: b.text,
    titol: b.el.matches('h2.repetit'),
    caixa: b.el.matches('h2.repetit') ? (rotul ? caixa(rotul) : null) : caixa(b.el),
  }));
}
"""


def dins(f, c, marge=6):
    return f["l"] >= c["l"] - marge and f["r"] <= c["r"] + marge and f["t"] >= c["t"] - marge and f["b"] <= c["b"] + marge


def main():
    cursos = sorted(p for p in REPO.glob("[0-9]eso/eines.html"))
    with sync_playwright() as pw:
        nav = pw.chromium.launch()
        errors = []
        total = 0
        for eines in cursos:
            curs = eines.parent.name
            pag = nav.new_page(viewport={"width": 1000, "height": 900})
            pag.add_init_script(VEU)
            pag.on("pageerror", lambda e: errors.append(str(e)))
            pag.goto(eines.as_uri())
            pag.wait_for_timeout(900)
            # Cada eina és un botó amb data-mod (les pestanyes del menú d'eines).
            n_eines = pag.evaluate("document.querySelectorAll('button[data-mod]').length")
            provades = 0
            for k in range(n_eines):
                boto = pag.locator("button[data-mod]").nth(k)
                nom = boto.text_content().strip()
                if not boto.is_visible():
                    continue
                boto.click()
                pag.wait_for_timeout(300)
                t = pag.evaluate_handle("[...document.querySelectorAll('.targeta')].find(t => t.offsetParent && t.querySelector(':scope > .veu-boto:not([hidden])'))")
                if not pag.evaluate("t => !!t", t):
                    continue
                on = pag.evaluate(ON_ES, t)
                pag.evaluate("window.__dits = []; window.__mostres = []")
                pag.evaluate("t => t.querySelector(':scope > .veu-boto').click()", t)
                pag.wait_for_function("() => !document.querySelector('.veu-boto[aria-pressed=\"true\"]')", timeout=20000)
                pag.wait_for_timeout(450)
                dits = pag.evaluate("window.__dits")
                mostres = pag.evaluate("window.__mostres")
                comprova(dits == [b["text"] for b in on], f"{curs} · {nom}: no diu els blocs que toca ({dits[:3]}…)")
                per_text = {b["text"]: b for b in on}
                for m in mostres:
                    b = per_text.get(m["text"])
                    if not b or not b["caixa"]:
                        comprova(not m["franges"], f"{curs} · {nom}: hi ha franja groga per a «{m['text'][:40]}», que no es veu")
                        continue
                    for f in m["franges"]:
                        if not dins(f, b["caixa"]):
                            on_txt = "a la barra del títol" if b["titol"] else "damunt del seu bloc"
                            comprova(False, f"{curs} · {nom}: quan diu «{m['paraula']}» de «{m['text'][:40]}», "
                                            f"la franja groga no és {on_txt}")
                            break
                    else:
                        continue
                    break
                if any(b["titol"] for b in on):
                    comprova(any(m["franges"] for m in mostres if per_text.get(m["text"], {}).get("titol")),
                             f"{curs} · {nom}: el títol amagat es diu però no es marca a la barra")
                net = pag.evaluate("() => !document.querySelector('.veu-apagat') && "
                                   "![...document.querySelectorAll('.veu-retolador')].some(f => f.style.opacity !== '0')")
                comprova(net, f"{curs} · {nom}: després de llegir, la targeta no queda com era")
                provades += 1
            comprova(provades > 0, f"{curs}: no s'ha pogut fer llegir cap targeta")
            total += provades
            print(f"  {curs}/eines.html: {provades} targetes llegides, franja groga comprovada paraula a paraula")
            pag.close()
        nav.close()
    comprova(not errors, f"errors de JavaScript: {errors[:3]}")
    if falles:
        print(f"\n{len(falles)} PROBLEMES:")
        for f in falles[:40]:
            print("  ·", f)
        sys.exit(1)
    print("Tot correcte.")


if __name__ == "__main__":
    main()
