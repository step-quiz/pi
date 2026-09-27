"""Fa un PDF d'un HTML de paper amb Chromium, amb la mateixa geometria que gen_pdf.py
(el full d'estil FULL_PDF de eines/paper.py). Només per veure esborranys.
Ús: python3 eines/pdf_chromium.py fitxes/ud3.html /tmp/ud3.pdf"""
import os, sys
if os.path.isdir("/opt/pw-browsers"):
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paper
from playwright.sync_api import sync_playwright

def fes(html_path, sortida, nomes=None):
    s = open(html_path, encoding="utf-8").read()
    cap, alumnat, sol = paper.blocs(s)
    fulls = {"alumnat": alumnat, "sol": sol, None: alumnat + sol}[nomes]
    doc = cap.replace("</head>", "<style>" + paper.FULL_PDF + "</style></head>") + "\n".join(fulls) + "</body></html>"
    tmp = os.path.join(os.path.dirname(os.path.abspath(html_path)), "_tmp_pdf.html")
    open(tmp, "w", encoding="utf-8").write(doc)
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pg = nav.new_page()
        pg.goto("file://" + tmp); pg.wait_for_timeout(300)
        pg.emulate_media(media="print")
        pg.pdf(path=sortida, prefer_css_page_size=True, print_background=True)
        nav.close()
    os.remove(tmp)

if __name__ == "__main__":
    fes(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
