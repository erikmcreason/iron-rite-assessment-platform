from reportlab.pdfgen import canvas

pdf = canvas.Canvas("reports/test_pdf_report.pdf")

pdf.drawString(100, 750, "THE IRON RITE")
pdf.drawString(100, 725, "PDF export test successful.")

pdf.save()

print("PDF created: reports/test_pdf_report.pdf")