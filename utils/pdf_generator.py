from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import markdown2

def generate_pdf(notes_md, quiz_md):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            leftMargin=40, rightMargin=40,
                            topMargin=50, bottomMargin=50)

    styles = getSampleStyleSheet()
    story = []

    full_md = f"# **Lecture Notes**\n\n{notes_md}\n\n# **Quiz Questions**\n\n{quiz_md}"
    html = markdown2.markdown(full_md)

    for line in html.split('\n'):
        if line.strip():
            story.append(Paragraph(line, styles['Normal']))
            story.append(Spacer(1, 6))

    doc.build(story)
    buffer.seek(0)
    return buffer
