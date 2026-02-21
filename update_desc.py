import sys

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Analysis TST desc
old_p5 = """<li data-translate="p5Desc">Quantitative analysis and backtesting module for
                                    high-frequency trading strategies.</li>"""
new_p5 = """<li data-translate="p5Desc">Advanced Streamlit dashboard for cryptocurrency market analysis, featuring DCC-GARCH volatility modeling, wavelet coherence, and algorithmic backtesting.</li>"""
html = html.replace(old_p5, new_p5)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update translations.js
with open('translations.js', 'r', encoding='utf-8') as f:
    js = f.read()

# We replace the exact strings for p5Desc
replacements = [
    ('en', 'Advanced Streamlit dashboard for cryptocurrency market analysis, featuring DCC-GARCH volatility modeling, wavelet coherence, and algorithmic backtesting.'),
    ('it', 'Dashboard avanzata Streamlit per l\'analisi del mercato delle criptovalute, con modellazione della volatilità DCC-GARCH, coerenza wavelet e backtesting algoritmico.'),
    ('sk', 'Pokročilý Streamlit dashboard pre analýzu trhu s kryptomenami, s modelovaním volatility DCC-GARCH, waveletovou koherenciou a algoritmickým backtestingom.'),
    ('cs', 'Pokročilý Streamlit dashboard pro analýzu trhu s kryptoměnami, s modelováním volatility DCC-GARCH, waveletovou koherencí a algoritmickým backtestingem.'),
    ('de', 'Erweitertes Streamlit-Dashboard für die Analyse des Kryptowährungsmarktes mit DCC-GARCH-Volatilitätsmodellierung, Wavelet-Kohärenz und algorithmischem Backtesting.'),
    ('es', 'Tablero avanzado de Streamlit para el análisis del mercado de criptomonedas, que presenta modelado de volatilidad DCC-GARCH, coherencia de ondas y backtesting algorítmico.'),
    ('fr', 'Tableau de bord Streamlit avancé pour l\'analyse du marché des crypto-monnaies, comprenant une modélisation de la volatilité DCC-GARCH, une cohérence d\'ondelettes et un backtesting algorithmique.')
]

# Quick hack to replace each occurrence sequentially
parts = js.split('p5Desc: "Quantitative analysis and backtesting module for high-frequency trading strategies."')
if len(parts) == 8:
    new_js = parts[0]
    for i in range(7):
        new_js += f'p5Desc: "{replacements[i][1]}"' + parts[i+1]
    with open('translations.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("translations.js updated successfully")
else:
    print(f"Failed to find 7 exact matches for p5Desc. Found {len(parts)-1}")

