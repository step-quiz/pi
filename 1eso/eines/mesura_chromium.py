"""L'alçada de cada bloc .full, en cm, amb la geometria dels PDF (eines/paper.py).
Com mesura.py, però amb Chromium en lloc de WeasyPrint: només per a esborranys.
Per a entorns sense WeasyPrint (el de Claude): python3 eines/mesura_chromium.py fitxes/ud3.html"""
import os, sys
if os.path.isdir("/opt/pw-browsers"):
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paper
from playwright.sync_api import sync_playwright
font = sys.argv[1]
s = open(font, encoding="utf-8").read()
cap, alumnat, sol = paper.blocs(s)
doc = cap.replace("</head>", "<style>" + paper.FULL_PDF + " body{background:#fff;margin:0}</style></head>") + \
      "\n".join(alumnat + sol) + "</body></html>"
tmp = os.path.join(os.path.dirname(os.path.abspath(font)), "_mesura.html")
open(tmp, "w", encoding="utf-8").write(doc)
with sync_playwright() as p:
    nav = p.chromium.launch()
    pg = nav.new_page(viewport={"width": round(18.2 * 37.795), "height": 1000})
    pg.emulate_media(media="print")
    pg.goto("file://" + tmp); pg.wait_for_timeout(400)
    alts = pg.evaluate("""() => [...document.querySelectorAll('.full')].map(f => {
        const r = f.getBoundingClientRect(); let fons = r.top;
        f.querySelectorAll('*').forEach(e => { const b = e.getBoundingClientRect(); if (b.height) fons = Math.max(fons, b.bottom); });
        return { cm: (fons - r.top) / 37.795, sol: f.classList.contains('sol'), vida: f.classList.contains('vida') };
    })""")
    nav.close()
os.remove(tmp)
n = 0
for i, a in enumerate(alts, 1):
    tipus = "solucionari" if a["sol"] else ("vida" if a["vida"] else "alumnat")
    marca = "ok" if a["cm"] <= paper.UTIL_CM else "NO CAP"
    print(f"  bloc {i:2} ({tipus:11}) {a['cm']:5.1f} cm de {paper.UTIL_CM:.1f}  {marca}")
    n += a["cm"] > paper.UTIL_CM
print("Tot cap." if not n else f"{n} pàgines no caben.")
