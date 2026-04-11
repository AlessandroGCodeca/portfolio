#!/usr/bin/env python3
"""
Push README.md files to all portfolio project repos.
Usage:
    python push_readmes.py <YOUR_GITHUB_TOKEN>
    or:
    GITHUB_TOKEN=ghp_xxx python push_readmes.py
"""

import sys
import os
import json
import base64
import urllib.request
import urllib.error

GITHUB_USER = "AlessandroGCodeca"
TOKEN = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("GITHUB_TOKEN", "")

if not TOKEN:
    print("Error: provide your GitHub token as an argument or set GITHUB_TOKEN env var.")
    print("  python push_readmes.py ghp_yourtoken")
    sys.exit(1)

READMES = {
    "AnalysisTST": """\
# 📊 Analysis TST

Advanced cryptocurrency market analysis dashboard built with Python and Streamlit.

## About
Analysis TST provides an interactive interface for deep crypto market research. It implements
DCC-GARCH volatility modelling to capture dynamic correlations between assets, wavelet coherence
analysis to detect multi-scale co-movement patterns and a backtesting engine to evaluate
algorithmic trading strategies on historical data.

## Tech Stack
- **Python** — core language
- **Streamlit** — interactive dashboard framework
- **statsmodels / arch** — GARCH volatility modelling
- **PyWavelets** — wavelet coherence analysis
- **pandas / numpy** — data processing
- **Plotly** — interactive charts

## Features
- DCC-GARCH dynamic correlation modelling
- Wavelet coherence heatmaps across time and frequency
- Algorithmic strategy backtesting with performance metrics
- Multi-asset comparison and portfolio analytics
- Fully interactive Streamlit UI

## Author
[Alessandro Giovanni Codecà](https://alessandrogcodeca.github.io/portfolio/) — [@AlessandroGCodeca](https://github.com/AlessandroGCodeca)
""",

    "human_genome_viewer": """\
# 🧬 Human Genome Viewer

Interactive genetic analysis application with 3D protein structure visualisation.

## About
Human Genome Viewer is a Streamlit application that makes genomic data accessible and visual.
Users can explore gene sequences, visualise protein structures in 3D and run mutation simulations
to observe the structural and functional consequences of genetic variants.

## Tech Stack
- **Python** — core language
- **Streamlit** — web application framework
- **Biopython** — sequence parsing and biological computation
- **py3Dmol / 3Dmol.js** — 3D protein structure rendering
- **pandas** — data handling

## Features
- Interactive gene sequence exploration
- 3D protein structure visualisation
- Mutation simulation with structural impact preview
- FASTA / PDB file support
- Clean, browser-based UI requiring no local setup

## Author
[Alessandro Giovanni Codecà](https://alessandrogcodeca.github.io/portfolio/) — [@AlessandroGCodeca](https://github.com/AlessandroGCodeca)
""",

    "MarketPulse": """\
# 📈 MarketPulse

Real-time financial market data dashboard with interactive analytics.

## About
MarketPulse is a JavaScript dashboard for monitoring financial markets at a glance.
It pulls live market data and presents it through interactive charts and analytics panels,
making it easy to track price movements, volume trends and key indicators in one place.

## Tech Stack
- **JavaScript** — core language
- **Chart.js** — interactive data visualisation
- **REST APIs** — live market data feeds
- **HTML / CSS** — responsive UI

## Features
- Real-time price and volume charts
- Multi-asset tracking across equities and crypto
- Interactive zoom and time-range selection
- Clean responsive layout

## Author
[Alessandro Giovanni Codecà](https://alessandrogcodeca.github.io/portfolio/) — [@AlessandroGCodeca](https://github.com/AlessandroGCodeca)
""",

    "Gemini-Slingshot": """\
# 🚀 Gemini Slingshot

Webcam-powered slingshot game that tracks your hand movements using the Gemini API.

## About
Gemini Slingshot uses your webcam and Google's Gemini API to track hand position in real time,
translating physical gestures into slingshot aim and release mechanics. Point, pull back
and let go — no controller needed.

## Tech Stack
- **TypeScript** — core language
- **Gemini API** — real-time hand tracking and gesture recognition
- **MediaPipe** — computer vision pipeline
- **Canvas API** — game rendering

## Features
- Real-time hand position tracking via webcam
- Gesture-based slingshot aim and fire mechanics
- Physics-based projectile simulation
- Runs entirely in the browser

## Getting Started
1. Clone the repo
2. Add your Gemini API key to the config
3. `npm install && npm run dev`
4. Allow webcam access and play

## Author
[Alessandro Giovanni Codecà](https://alessandrogcodeca.github.io/portfolio/) — [@AlessandroGCodeca](https://github.com/AlessandroGCodeca)
""",

    "ChronoSnap": """\
# ⏱️ ChronoSnap

AI-powered temporal imaging system that transforms photos into historical or futuristic eras.

## About
ChronoSnap uses Gemini 2.5 to reimagine any uploaded photograph as if it were taken in a
different point in time — from ancient civilisations to far-future landscapes. Upload a photo,
choose an era and watch the scene transform while preserving its core composition.

## Tech Stack
- **TypeScript** — core language
- **Gemini 2.5 API** — multimodal image generation and understanding
- **Node.js** — server runtime

## Features
- Era selection: historical periods to sci-fi futures
- Composition-preserving transformation
- Side-by-side before/after comparison
- Fast processing via Gemini 2.5 multimodal API

## Getting Started
1. Clone the repo
2. Add your Gemini API key to `.env`
3. `npm install && npm run dev`

## Author
[Alessandro Giovanni Codecà](https://alessandrogcodeca.github.io/portfolio/) — [@AlessandroGCodeca](https://github.com/AlessandroGCodeca)
""",

    "CulinAI": """\
# 🍳 CulinAI

AI-powered culinary assistant for personalised recipe generation and meal planning.

## About
CulinAI takes your available ingredients, dietary preferences and nutritional goals
and generates tailored recipes with step-by-step instructions. It can build weekly
meal plans and suggest ingredient substitutions — making home cooking smarter and
less wasteful.

## Tech Stack
- **TypeScript** — core language
- **AI / LLM API** — recipe generation and planning logic
- **Node.js** — server runtime

## Features
- Ingredient-based recipe generation
- Dietary preference and allergen filtering
- Weekly meal plan builder
- Ingredient substitution suggestions
- Nutritional overview per recipe

## Getting Started
1. Clone the repo
2. Add your API key to `.env`
3. `npm install && npm run dev`

## Author
[Alessandro Giovanni Codecà](https://alessandrogcodeca.github.io/portfolio/) — [@AlessandroGCodeca](https://github.com/AlessandroGCodeca)
""",

    "BlackHoleSimulation": """\
# 🌌 Black Hole Simulation

Interactive educational simulation of gravitational physics and black hole mechanics.

## About
Black Hole Simulation is a browser-based physics visualisation built with vanilla
HTML, CSS and JavaScript. It models gravitational lensing, accretion disc dynamics
and object trajectories near a simulated black hole — designed as an educational
tool for exploring relativistic concepts interactively.

## Tech Stack
- **HTML / CSS / JavaScript** — no frameworks, no dependencies
- **Canvas API** — real-time physics rendering

## Features
- Real-time gravitational trajectory simulation
- Visual gravitational lensing effect
- Adjustable mass and simulation speed
- Particle accretion modelling
- Runs entirely in the browser — just open `index.html`

## Getting Started
No installation required. Clone the repo and open `index.html` in any modern browser.

## Author
[Alessandro Giovanni Codecà](https://alessandrogcodeca.github.io/portfolio/) — [@AlessandroGCodeca](https://github.com/AlessandroGCodeca)
""",
}


def get_existing_sha(repo: str, token: str) -> str | None:
    """Return the blob SHA of the existing README.md, or None if it doesn't exist."""
    url = f"https://api.github.com/repos/{GITHUB_USER}/{repo}/contents/README.md"
    req = urllib.request.Request(url, headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())["sha"]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def push_readme(repo: str, content: str, token: str) -> None:
    sha = get_existing_sha(repo, token)
    url = f"https://api.github.com/repos/{GITHUB_USER}/{repo}/contents/README.md"
    payload = {
        "message": "Add README.md",
        "content": base64.b64encode(content.encode()).decode(),
    }
    if sha:
        payload["message"] = "Update README.md"
        payload["sha"] = sha

    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, method="PUT", headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    try:
        with urllib.request.urlopen(req) as resp:
            resp.read()
        action = "Updated" if sha else "Created"
        print(f"  ✓  {action}: {GITHUB_USER}/{repo}/README.md")
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  ✗  Failed {repo}: {e.code} — {body[:120]}")


if __name__ == "__main__":
    print(f"Pushing READMEs to {len(READMES)} repos under @{GITHUB_USER}...\n")
    for repo, content in READMES.items():
        push_readme(repo, content, TOKEN)
    print("\nDone.")
