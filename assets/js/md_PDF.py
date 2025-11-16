# script for turning md file into formatted pdf
import markdown
from weasyprint import HTML

# path to my cv (or whatevs i want to change)
with open("assets/attatchments/cv/cv.md", "r", encoding="utf-8") as f:
    md_text = f.read()

# converter func
html_content = markdown.markdown(md_text, extensions=["extra"])

html_full = f"""
<html>
<head>
  <meta charset="UTF-8">
</head>
<body>
{html_content}
</body>
</html>
"""

# format css
css_path = "assets/css/cv_format.css"

# output
output_path = "assets/attatchments/cv/CV.pdf"
HTML(string=html_full).write_pdf(output_path)
