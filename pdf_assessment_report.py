import json
import os

from reportlab.pdfgen import canvas


def create_reports_folder():
    os.makedirs("reports", exist_ok=True)


def load_assessments():
    try:
        with open("brothers.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def export_pdf_report():
    create_reports_folder()
    assessments = load_assessments()

    if len(assessments) == 0:
        print("No saved assessments found.")
        return

    email = input("Enter email address for PDF report: ")

    for assessment in assessments:
        stored_email = assessment.get("email", "")

        if stored_email.lower() == email.lower():
            file_name = assessment["name"] + "_Assessment_Report.pdf"
            file_path = "reports/" + file_name

            pdf = canvas.Canvas(file_path)

            y = 800

            pdf.setFont("Helvetica-Bold", 18)
            pdf.drawString(72, y, "THE IRON RITE ASSESSMENT REPORT")
            y -= 40

            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(72, y, "Participant Information")
            y -= 20

            pdf.setFont("Helvetica", 11)
            pdf.drawString(72, y, "Name: " + assessment["name"])
            y -= 16
            pdf.drawString(72, y, "Email: " + assessment["email"])
            y -= 30

            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(72, y, "Archetype Summary")
            y -= 20

            pdf.setFont("Helvetica", 11)
            pdf.drawString(72, y, "Dominant Archetype: " + assessment["dominant"])
            y -= 16
            pdf.drawString(72, y, "Primary Growth Area: " + assessment["growth_area"])
            y -= 30

            ranked_scores = sorted(
                assessment["scores"].items(),
                key=lambda item: item[1],
                reverse=True
            )

            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(72, y, "Archetype Ranking")
            y -= 20

            pdf.setFont("Helvetica", 11)

            for rank, (archetype, score) in enumerate(ranked_scores, start=1):
                pdf.drawString(72, y, "#" + str(rank) + " " + archetype + ": " + str(score))
                y -= 16

            y -= 14

            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(72, y, "Recommendation")
            y -= 20

            pdf.setFont("Helvetica", 11)
            pdf.drawString(72, y, assessment["recommendation"])

            pdf.save()

            print("PDF report created:", file_path)
            return

    print("No assessment found with that email.")


export_pdf_report()