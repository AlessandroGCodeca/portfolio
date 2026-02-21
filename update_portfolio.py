import re
import json

HTML_FILE = '/Users/alessandrocodeca/CVINDEX/index.html'
JS_FILE = '/Users/alessandrocodeca/CVINDEX/translations.js'

with open(HTML_FILE, 'r') as f:
    html = f.read()

with open(JS_FILE, 'r') as f:
    js = f.read()

# Replace projects in HTML
projects_html = """                <section id="projects">
                    <h2 class="section-title" data-translate="projectsTitle">Projects</h2>

                    <div class="timeline-item">
                        <div class="timeline-logo"><span style="font-size: 24px;">🍳</span></div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p1Title">CulinAI</div>
                                <span class="date">2026</span>
                            </div>
                            <ul class="description"><li data-translate="p1Desc">AI-powered culinary assistant for recipe generation and meal planning.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <div class="timeline-logo"><span style="font-size: 24px;">��</span></div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p2Title">MarketPulse</div>
                                <span class="date">2026</span>
                            </div>
                            <ul class="description"><li data-translate="p2Desc">Interactive dashboard for real-time market data visualization and financial analytics.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <div class="timeline-logo"><span style="font-size: 24px;">⏱️</span></div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p3Title">ChronoSnap</div>
                                <span class="date">2026</span>
                            </div>
                            <ul class="description"><li data-translate="p3Desc">Time management and temporal data tracking application.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <div class="timeline-logo"><span style="font-size: 24px;">🧬</span></div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p4Title">Human Genome Viewer</div>
                                <span class="date">2026</span>
                            </div>
                            <ul class="description"><li data-translate="p4Desc">Streamlit application for interactive genetic analysis, featuring 3D protein structures and mutation simulation.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <div class="timeline-logo"><span style="font-size: 24px;">📊</span></div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p5Title">Analysis TST</div>
                                <span class="date">2026</span>
                            </div>
                            <ul class="description"><li data-translate="p5Desc">Quantitative analysis and backtesting module for high-frequency trading strategies.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <div class="timeline-logo"><span style="font-size: 24px;">🚀</span></div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p6Title">Gemini Slingshot</div>
                                <span class="date">2026</span>
                            </div>
                            <ul class="description"><li data-translate="p6Desc">Advanced AI integration tool utilizing the Gemini model for automated data processing.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <div class="timeline-logo"><span style="font-size: 24px;">🌌</span></div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p7Title">Blackhole Simulator</div>
                                <span class="date">2026</span>
                            </div>
                            <ul class="description"><li data-translate="p7Desc">Educational simulation tool demonstrating gravitational physics and black hole mechanics.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>
                </section>"""

# Find the section and replace it
html = re.sub(r'<section id="projects">.*?</section>', projects_html, html, flags=re.DOTALL)

with open(HTML_FILE, 'w') as f:
    f.write(html)

projects_trans = {
    'en': '''p1Title: "CulinAI",
        p1Desc: "AI-powered culinary assistant for recipe generation and meal planning.",
        p2Title: "MarketPulse",
        p2Desc: "Interactive dashboard for real-time market data visualization and financial analytics.",
        p3Title: "ChronoSnap",
        p3Desc: "Time management and temporal data tracking application.",
        p4Title: "Human Genome Viewer",
        p4Desc: "Streamlit application for interactive genetic analysis, featuring 3D protein structures and mutation simulation.",
        p5Title: "Analysis TST",
        p5Desc: "Quantitative analysis and backtesting module for high-frequency trading strategies.",
        p6Title: "Gemini Slingshot",
        p6Desc: "Advanced AI integration tool utilizing the Gemini model for automated data processing.",
        p7Title: "Blackhole Simulator",
        p7Desc: "Educational simulation tool demonstrating gravitational physics and black hole mechanics.",''',
    
    'it': '''p1Title: "CulinAI",
        p1Desc: "Assistente culinario basato sull'IA per la generazione di ricette e la pianificazione dei pasti.",
        p2Title: "MarketPulse",
        p2Desc: "Dashboard interattiva per la visualizzazione dei dati di mercato in tempo reale e analisi finanziarie.",
        p3Title: "ChronoSnap",
        p3Desc: "Applicazione per la gestione del tempo e il tracciamento dei dati temporali.",
        p4Title: "Human Genome Viewer",
        p4Desc: "Applicazione Streamlit per l'analisi genetica interattiva, con strutture proteiche 3D e simulazione di mutazioni.",
        p5Title: "Analysis TST",
        p5Desc: "Modulo di analisi quantitativa e backtesting per strategie di trading ad alta frequenza.",
        p6Title: "Gemini Slingshot",
        p6Desc: "Strumento avanzato di integrazione IA che utilizza il modello Gemini per l'elaborazione dati automatizzata.",
        p7Title: "Simulatore di Buchi Neri",
        p7Desc: "Strumento di simulazione educativa che dimostra la fisica gravitazionale e la meccanica dei buchi neri.",''',

    'sk': '''p1Title: "CulinAI",
        p1Desc: "Kulinársky asistent poháňaný umelou inteligenciou pre generovanie receptov a plánovanie jedál.",
        p2Title: "MarketPulse",
        p2Desc: "Interaktívny panel pre vizualizáciu trhových dát v reálnom čase a finančnú analytiku.",
        p3Title: "ChronoSnap",
        p3Desc: "Aplikácia na riadenie času a sledovanie časových údajov.",
        p4Title: "Prehliadač ľudského genómu",
        p4Desc: "Aplikácia Streamlit pre interaktívnu genetickú analýzu s 3D štruktúrami proteínov a simuláciou mutácií.",
        p5Title: "Analysis TST",
        p5Desc: "Kvantitatívna analýza a modul pre spätné testovanie vysokofrekvenčných obchodných stratégií.",
        p6Title: "Gemini Slingshot",
        p6Desc: "Pokročilý nástroj na integráciu AI využívajúci model Gemini na automatizované spracovanie dát.",
        p7Title: "Simulátor čiernej diery",
        p7Desc: "Vzdelávací simulačný nástroj demonštrujúci gravitačnú fyziku a mechaniku čiernych dier.",''',

    'cs': '''p1Title: "CulinAI",
        p1Desc: "Kulinářský asistent poháněný umělou inteligencí pro generování receptů a plánování jídel.",
        p2Title: "MarketPulse",
        p2Desc: "Interaktivní panel pro vizualizaci tržních dat v reálném čase a finanční analytiku.",
        p3Title: "ChronoSnap",
        p3Desc: "Aplikace pro řízení času a sledování časových údajů.",
        p4Title: "Prohlížeč lidského genomu",
        p4Desc: "Aplikace Streamlit pro interaktivní genetickou analýzu, obsahující 3D struktury proteinů a simulaci mutací.",
        p5Title: "Analysis TST",
        p5Desc: "Kvantitativní analýza a modul pro zpětné testování vysokofrekvenčních obchodních strategií.",
        p6Title: "Gemini Slingshot",
        p6Desc: "Pokročilý nástroj pro integraci AI využívající model Gemini k automatizovanému zpracování dat.",
        p7Title: "Simulátor Černé Díry",
        p7Desc: "Vzdělávací simulační nástroj demonstrující gravitační fyziku a mechaniku černých děr.",''',

    'de': '''p1Title: "CulinAI",
        p1Desc: "KI-gestützter kulinarischer Assistent für die Rezeptgenerierung und Essensplanung.",
        p2Title: "MarketPulse",
        p2Desc: "Interaktives Dashboard für Echtzeit-Marktdatenvisualisierung und Finanzanalyse.",
        p3Title: "ChronoSnap",
        p3Desc: "Anwendung für Zeitmanagement und zeitliche Datenverfolgung.",
        p4Title: "Human Genome Viewer",
        p4Desc: "Streamlit-Anwendung für interaktive genetische Analysen mit 3D-Proteinstrukturen und Mutationssimulation.",
        p5Title: "Analysis TST",
        p5Desc: "Quantitatives Analyse- und Backtesting-Modul für Hochfrequenz-Tradingstrategien.",
        p6Title: "Gemini Slingshot",
        p6Desc: "Fortschrittliches KI-Integrationstool, das das Gemini-Modell zur automatisierten Datenverarbeitung nutzt.",
        p7Title: "Schwarzes Loch Simulator",
        p7Desc: "Pädagogisches Simulationswerkzeug, das Gravitationsphysik und die Mechanik von Schwarzen Löchern demonstriert.",''',

    'es': '''p1Title: "CulinAI",
        p1Desc: "Asistente culinario impulsado por IA para la generación de recetas y planificación de comidas.",
        p2Title: "MarketPulse",
        p2Desc: "Panel interactivo para la visualización de datos de mercado en tiempo real y análisis financiero.",
        p3Title: "ChronoSnap",
        p3Desc: "Aplicación para la gestión del tiempo y seguimiento de datos temporales.",
        p4Title: "Visor del Genoma Humano",
        p4Desc: "Aplicación Streamlit para análisis genético interactivo, con estructuras de proteínas en 3D y simulación de mutaciones.",
        p5Title: "Analysis TST",
        p5Desc: "Módulo de análisis cuantitativo y backtesting para estrategias de negociación de alta frecuencia.",
        p6Title: "Gemini Slingshot",
        p6Desc: "Avanzada herramienta de integración de IA que utiliza el modelo Gemini para procesamiento de datos automatizado.",
        p7Title: "Simulador de Agujero Negro",
        p7Desc: "Herramienta de simulación educativa que demuestra la física gravitacional y la mecánica de los agujeros negros.",''',

    'fr': '''p1Title: "CulinAI",
        p1Desc: "Assistant culinaire alimenté par l'IA pour la génération de recettes et la planification des repas.",
        p2Title: "MarketPulse",
        p2Desc: "Tableau de bord interactif pour la visualisation des données de marché en temps réel et l'analyse financière.",
        p3Title: "ChronoSnap",
        p3Desc: "Application de gestion du temps et de suivi des données temporelles.",
        p4Title: "Visionneuse de Génome Humain",
        p4Desc: "Application Streamlit pour l'analyse génétique interactive, avec structures protéiques en 3D et simulation de mutations.",
        p5Title: "Analysis TST",
        p5Desc: "Module d'analyse quantitative et de backtesting pour les stratégies de trading à haute fréquence.",
        p6Title: "Gemini Slingshot",
        p6Desc: "Outil d'intégration d'IA avancé utilisant le modèle Gemini pour le traitement de données automatisé.",
        p7Title: "Simulateur de Trou Noir",
        p7Desc: "Outil de simulation pédagogique démontrant la physique gravitationnelle et la mécanique des trous noirs.",'''
}

# Replace project1Title/Desc and project2Title/Desc with p1-p7
for lang, text in projects_trans.items():
    js = re.sub(r'project1Title: ".*?project2Desc: ".*?",', text, js, flags=re.DOTALL)

with open(JS_FILE, 'w') as f:
    f.write(js)
