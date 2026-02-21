import re

html_file = '/Users/alessandrocodeca/CVINDEX/index.html'
with open(html_file, 'r') as f:
    html = f.read()

# Remove right column (languages, skills, certifications)
html = re.sub(r'<aside class="right-column">.*?</aside>', '', html, flags=re.DOTALL)

# Remove MarketPulse from projects
html = re.sub(r'<div class="timeline-item">\s*<div class="timeline-logo">\s*<img src="images/marketpulse_logo\.png".*?</div>\s*</div>', '', html, flags=re.DOTALL)

# Remove skills link from nav
html = re.sub(r'<li><a href="#skills".*?Skills</a></li>', '', html, flags=re.DOTALL)

with open(html_file, 'w') as f:
    f.write(html)
