import re
import shutil

src_img = '/Users/alessandrocodeca/.gemini/antigravity/brain/ec2dd6b3-7170-4198-85f3-a698392509c2/marketpulse_logo_1771687363708.png'
dest_img = '/Users/alessandrocodeca/CVINDEX/images/marketpulse_logo.png'
shutil.copy(src_img, dest_img)

html_file = '/Users/alessandrocodeca/CVINDEX/index.html'
with open(html_file, 'r') as f:
    html = f.read()

projects_html = """                <section id="projects">
                    <h2 class="section-title" data-translate="projectsTitle">Projects</h2>

                    <div class="timeline-item">
                        <div class="timeline-logo">
                            <img src="images/marketpulse_logo.png" alt="MarketPulse Logo" loading="lazy">
                        </div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p2Title">MarketPulse</div>
                            </div>
                            <ul class="description"><li data-translate="p2Desc">Interactive dashboard for real-time market data visualization and financial analytics.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <div class="timeline-logo"><span style="font-size: 24px;">🧬</span></div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p4Title">Human Genome Viewer</div>
                            </div>
                            <ul class="description"><li data-translate="p4Desc">Streamlit application for interactive genetic analysis, featuring 3D protein structures and mutation simulation.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <div class="timeline-logo"><span style="font-size: 24px;">🚀</span></div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p6Title">Gemini Slingshot</div>
                            </div>
                            <ul class="description"><li data-translate="p6Desc">Advanced AI integration tool utilizing the Gemini model for automated data processing.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <div class="timeline-logo"><span style="font-size: 24px;">📊</span></div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p5Title">Analysis TST</div>
                            </div>
                            <ul class="description"><li data-translate="p5Desc">Quantitative analysis and backtesting module for high-frequency trading strategies.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <div class="timeline-logo"><span style="font-size: 24px;">🍳</span></div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p1Title">CulinAI</div>
                            </div>
                            <ul class="description"><li data-translate="p1Desc">AI-powered culinary assistant for recipe generation and meal planning.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <div class="timeline-logo"><span style="font-size: 24px;">🌌</span></div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p7Title">Blackhole Simulator</div>
                            </div>
                            <ul class="description"><li data-translate="p7Desc">Educational simulation tool demonstrating gravitational physics and black hole mechanics.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>

                    <div class="timeline-item">
                        <div class="timeline-logo"><span style="font-size: 24px;">⏱️</span></div>
                        <div class="timeline-content">
                            <div class="timeline-header">
                                <div class="job-title" data-translate="p3Title">ChronoSnap</div>
                            </div>
                            <ul class="description"><li data-translate="p3Desc">Time management and temporal data tracking application.</li></ul>
                            <a href="https://github.com/AlessandroGCodeca" target="_blank" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem; margin-top: 10px; display: inline-block;" data-translate="viewCodeBtn">View Code</a>
                        </div>
                    </div>
                </section>"""

html = re.sub(r'<section id="projects">.*?</section>', projects_html, html, flags=re.DOTALL)

with open(html_file, 'w') as f:
    f.write(html)
