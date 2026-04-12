from reportlab.pdfgen import canvas

def generate_pdf():

    c = canvas.Canvas("report.pdf")
    c.drawString(100,750,"Vulnerability Report")
    c.save()