"""Torna a fer les captures de pantalla de les webs A i B, en format 16:9.

    pip install playwright
    python3 conference/presentacio/captures.py

Les captures surten a conference/Fast-build-A/captures/ i conference/Fast-build-B/captures/.
Fan 1024 × 576 píxels de pantalla (al doble de resolució), la mateixa forma que una
diapositiva: així ocupen tota la diapositiva. Els números de la web B surten a l'atzar;
aquí l'atzar està fixat perquè la captura surti sempre igual (l'equació 5x + 3 = 13).
"""
from pathlib import Path

from playwright.sync_api import sync_playwright

C = str(Path(__file__).resolve().parent.parent)
# Al Codespace, sense executable_path, Playwright fa servir el seu Chromium
NAVEGADOR = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
A=f'file://{C}/Fast-build-A/Fast-build-A-webapp.html'; B=f'file://{C}/Fast-build-B/Fast-build-B-webapp.html'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=NAVEGADOR) if Path(NAVEGADOR).exists() else p.chromium.launch()
    pg=b.new_page(viewport={"width":1024,"height":576},device_scale_factor=2)
    pg.add_init_script("let s=7;Math.random=()=>{s=(s*16807)%2147483647;return (s-1)/2147483646;}")
    d=f'{C}/Fast-build-A/captures/'
    pg.goto(A); pg.screenshot(path=d+'1-menu.png')
    pg.click("text=Exercicis"); pg.screenshot(path=d+'2-exercicis-amb-cronometre.png')
    pg.click("#exercises .back-btn"); pg.click("text=Percentatges"); pg.fill("#percent1","75"); pg.click("#percentages .exercise-btn >> nth=0")
    pg.evaluate("document.querySelector('#percentages h2').scrollIntoView(); window.scrollBy(0,-15)"); pg.screenshot(path=d+'3-percentatges-sense-correccio.png')
    pg.evaluate("window.scrollTo(0,0)"); pg.click("#percentages .back-btn"); pg.click("text=Exercicis"); pg.fill("#exercise0","8")
    for _ in range(12): pg.click("#exercisesContainer .exercise-btn >> nth=0")
    pg.evaluate("window.scrollTo(0,document.body.scrollHeight)"); pg.screenshot(path=d+'4-progres-150-per-cent.png')
    pg.evaluate("window.scrollTo(0,0)"); pg.click("#exercises .back-btn"); pg.click("text=Calculadora"); pg.fill("#num1","12"); pg.select_option("#operation","divide"); pg.fill("#num2","4"); pg.click(".calc-button")
    pg.evaluate("document.querySelector('#calculator h2').scrollIntoView(); window.scrollBy(0,-15)"); pg.screenshot(path=d+'5-calculadora-3.00.png')
    d=f'{C}/Fast-build-B/captures/'
    pg.goto(B); pg.screenshot(path=d+'1-menu.png')
    pg.click("text=Equacions"); print(pg.inner_text(".q")); pg.fill("#r","99"); pg.click("text=Comprova"); pg.screenshot(path=d+'2-gairebe-amb-resposta-99.png')
    pg.fill("#r","98"); pg.click("text=Comprova"); pg.screenshot(path=d+'3-pas-a-pas-despres-de-dos-errors.png')
    b.close()
