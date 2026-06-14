import json
import os


def load_questions():
    try:
        with open("questions.json", "r") as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print("questions.json not found.")
        return []


def load_assessments():
    try:
        with open("brothers.json", "r") as file:
            assessments = json.load(file)
        return assessments
    except FileNotFoundError:
        return []


def save_assessments(assessments):
    with open("brothers.json", "w") as file:
        json.dump(assessments, file, indent=4)

    print("Assessments saved.")


def create_reports_folder():
    os.makedirs("reports", exist_ok=True)


def create_test_report():
    with open("reports/test_report.txt", "w") as file:
        file.write("This is a test report.")


def export_assessment_report():
    create_reports_folder()
    assessments = load_assessments()

    if len(assessments) == 0:
        print("\nNo saved assessments to export.")
        return

    email = input("Enter email address for the report: ")

    for assessment in assessments:
        stored_email = assessment.get("email", "")

        if stored_email.lower() == email.lower():
            file_name = assessment["name"] + "_Assessment_Report.txt"
            file_path = "reports/" + file_name

            ranked_scores = sorted(
                assessment["scores"].items(),
                key=lambda item: item[1],
                reverse=True
            )

            report_text = "THE IRON RITE ASSESSMENT REPORT\n"
            report_text += "================================\n\n"

            report_text += "EXECUTIVE SUMMARY\n"
            report_text += "-----------------\n"
            report_text += "This assessment indicates a dominant " + assessment["dominant"] + " archetype with " + assessment["growth_area"] + " identified as the primary growth area.\n\n"
            report_text += "The strongest archetype pattern reflects the current center of strength, instinct, and development. The growth area represents the archetype most likely to produce meaningful improvement through deliberate practice.\n\n"
            report_text += "Overall, this report is designed to help translate assessment results into awareness, reflection, and practical next action.\n\n"

            report_text += "YOUR TOP STRENGTHS\n"
            report_text += "------------------\n\n"

            top_three = ranked_scores[:3]

            for rank, (archetype, score) in enumerate(top_three, start=1):
                report_text += f"#{rank} {archetype.upper()} ({score})\n"

                if archetype == "King":
                    report_text += "Exceptional responsibility, leadership, vision, order, and service.\n\n"
                elif archetype == "Warrior":
                    report_text += "Strong discipline, courage, action orientation, boundaries, and perseverance.\n\n"
                elif archetype == "Magician":
                    report_text += "Strong strategic thinking, awareness, insight, pattern recognition, and problem solving.\n\n"
                elif archetype == "Lover":
                    report_text += "Strong connection, creativity, empathy, vitality, and emotional presence.\n\n"

            report_text += "ARCHETYPE RANKING\n"
            report_text += "-----------------\n\n"

            for rank, (archetype, score) in enumerate(ranked_scores, start=1):
                report_text += f"#{rank} {archetype:<10} {score}\n"

            report_text += "\n"

            report_text += "PARTICIPANT INFORMATION\n"
            report_text += "-----------------------\n"
            report_text += "Name: " + assessment["name"] + "\n"
            report_text += "Email: " + assessment["email"] + "\n\n"

            report_text += "ARCHETYPE SUMMARY\n"
            report_text += "-----------------\n"
            report_text += "Dominant Archetype: " + assessment["dominant"] + "\n"
            report_text += "Primary Growth Area: " + assessment["growth_area"] + "\n\n"

            report_text += "DIMENSION SCORES\n"
            report_text += "----------------\n"

            for category, dimensions in assessment["dimension_scores"].items():
                report_text += "\n" + category.upper() + "\n"

                for dimension, score in dimensions.items():
                    report_text += "  " + dimension + ": " + str(score) + "\n"

            report_text += "\nDOMINANT ARCHETYPE INTERPRETATION\n"
            report_text += "---------------------------------\n"

            if assessment["dominant"] == "King":
                report_text += "The King archetype represents order, responsibility, vision, leadership, and service. A strong King score suggests the ability to create structure, make decisions, and hold a standard for yourself and others.\n"
            elif assessment["dominant"] == "Warrior":
                report_text += "The Warrior archetype represents discipline, courage, action, boundaries, and endurance. A strong Warrior score suggests the ability to take action, face resistance, and move toward difficult goals.\n"
            elif assessment["dominant"] == "Magician":
                report_text += "The Magician archetype represents knowledge, insight, strategy, awareness, and problem solving. A strong Magician score suggests the ability to see patterns, understand systems, and think clearly under pressure.\n"
            elif assessment["dominant"] == "Lover":
                report_text += "The Lover archetype represents connection, creativity, empathy, presence, and vitality. A strong Lover score suggests the ability to feel deeply, connect meaningfully, and stay alive to beauty, relationship, and purpose.\n"
            else:
                report_text += "The dominant archetype represents the strongest current pattern in this assessment.\n"

            report_text += "\nGROWTH AREA INTERPRETATION\n"
            report_text += "--------------------------\n"

            if assessment["growth_area"] == "King":
                report_text += "Growth in the King archetype may involve creating more order, making clearer decisions, setting stronger standards, and leading with calm responsibility.\n"
            elif assessment["growth_area"] == "Warrior":
                report_text += "Growth in the Warrior archetype may involve increasing discipline, strengthening boundaries, taking action faster, and building endurance through chosen hardship.\n"
            elif assessment["growth_area"] == "Magician":
                report_text += "Growth in the Magician archetype may involve deeper study, clearer reflection, better strategy, and more awareness of the patterns behind problems.\n"
            elif assessment["growth_area"] == "Lover":
                report_text += "Growth in the Lover archetype may involve increasing connection, creativity, emotional presence, vitality, gratitude, and appreciation for beauty.\n"
            else:
                report_text += "The growth area represents the archetype with the most room for deliberate development.\n"

            report_text += "\nRECOMMENDATION\n"
            report_text += "--------------\n"
            report_text += assessment["recommendation"] + "\n\n"

            report_text += "DEVELOPMENT PATH\n"
            report_text += "----------------\n"

            if assessment["growth_area"] == "King":
                report_text += "Focus:\n"
                report_text += "Order, responsibility, leadership, decision-making, and standards.\n\n"
                report_text += "24 Hour Action:\n"
                report_text += "Make one clear decision you have been delaying and communicate it calmly.\n\n"
                report_text += "7 Day Practice:\n"
                report_text += "Create one daily structure that brings more order to your life, home, work, or relationships.\n\n"
                report_text += "Reflection Question:\n"
                report_text += "Where am I avoiding responsibility, structure, or clear leadership?\n"
            elif assessment["growth_area"] == "Warrior":
                report_text += "Focus:\n"
                report_text += "Discipline, courage, action, boundaries, and endurance.\n\n"
                report_text += "24 Hour Action:\n"
                report_text += "Complete one difficult task you have been avoiding.\n\n"
                report_text += "7 Day Practice:\n"
                report_text += "Do one intentionally difficult thing each day to train follow-through and self-command.\n\n"
                report_text += "Reflection Question:\n"
                report_text += "Where am I allowing comfort, fear, or hesitation to replace action?\n"
            elif assessment["growth_area"] == "Magician":
                report_text += "Focus:\n"
                report_text += "Knowledge, insight, strategy, awareness, and problem solving.\n\n"
                report_text += "24 Hour Action:\n"
                report_text += "Study one problem deeply and write down the pattern behind it.\n\n"
                report_text += "7 Day Practice:\n"
                report_text += "Spend ten minutes each day studying, mapping, or reflecting on a system you need to understand better.\n\n"
                report_text += "Reflection Question:\n"
                report_text += "Where do I need more clarity, knowledge, strategy, or awareness before acting?\n"
            elif assessment["growth_area"] == "Lover":
                report_text += "Focus:\n"
                report_text += "Connection, presence, vitality, creativity, beauty, and emotional openness.\n\n"
                report_text += "24 Hour Action:\n"
                report_text += "Give one person your complete attention in a conversation without multitasking.\n\n"
                report_text += "7 Day Practice:\n"
                report_text += "Perform one intentional act of gratitude, creativity, connection, or beauty each day.\n\n"
                report_text += "Reflection Question:\n"
                report_text += "Where am I withholding connection, appreciation, vitality, or emotional presence?\n"
            else:
                report_text += "Focus:\n"
                report_text += "Choose one area for deliberate development.\n\n"
                report_text += "24 Hour Action:\n"
                report_text += "Take one practical step toward growth.\n\n"
                report_text += "7 Day Practice:\n"
                report_text += "Repeat one small growth action daily.\n\n"
                report_text += "Reflection Question:\n"
                report_text += "What pattern needs my attention right now?\n"

            report_text += "\nNEXT STEP\n"
            report_text += "---------\n"
            report_text += "Choose one practical action connected to your growth area and complete it within the next 24 hours. The goal is not perfection. The goal is movement, awareness, and disciplined follow-through.\n"

            with open(file_path, "w") as file:
                file.write(report_text)

            print("\nReport exported successfully.")
            print("File:", file_path)
            return

    print("No assessment found with that email.")


def ask_question(question):
    while True:
        print("\n" + question["question"])
        print("Category:", question["category"])
        print("Dimension:", question["dimension"])

        answer = input("Score 1-10: ")

        if answer.isdigit():
            answer = int(answer)
            if answer >= 1 and answer <= 10:
                return answer

        print("Invalid answer. Enter a number from 1 to 10.")


def calculate_average(scores):
    return sum(scores) / len(scores)


def get_recommendation(growth_area):
    if growth_area == "Warrior":
        return "Build discipline through one difficult physical action and one clear boundary."
    elif growth_area == "King":
        return "Create order by making one leadership decision and communicating one clear standard."
    elif growth_area == "Magician":
        return "Strengthen insight through study, reflection, and mapping the pattern behind one problem."
    elif growth_area == "Lover":
        return "Increase connection through presence, gratitude, beauty, creativity, or emotional openness."
    else:
        return "Review your results and choose one area for deliberate growth."


def run_assessment():
    questions = load_questions()

    if len(questions) == 0:
        print("No questions loaded.")
        return

    name = input("Enter your name: ")
    email = input("Enter your email: ")

    category_results = {}
    dimension_results = {}

    print("\nIRON RITE ASSESSMENT")
    print("--------------------")
    print("Answer each question from 1 to 10.")
    print("1 = Strongly disagree")
    print("10 = Strongly agree")

    for question in questions:
        category = question["category"]
        dimension = question["dimension"]
        answer = ask_question(question)

        if category not in category_results:
            category_results[category] = []

        category_results[category].append(answer)

        if category not in dimension_results:
            dimension_results[category] = {}

        if dimension not in dimension_results[category]:
            dimension_results[category][dimension] = []

        dimension_results[category][dimension].append(answer)

    category_scores = {}

    for category, scores in category_results.items():
        category_scores[category] = round(calculate_average(scores), 2)

    dimension_scores = {}

    for category, dimensions in dimension_results.items():
        dimension_scores[category] = {}

        for dimension, scores in dimensions.items():
            dimension_scores[category][dimension] = round(calculate_average(scores), 2)

    ranked_scores = sorted(
        category_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    dominant = ranked_scores[0][0]
    growth_area = ranked_scores[-1][0]
    recommendation = get_recommendation(growth_area)

    assessment_record = {
        "name": name,
        "email": email,
        "scores": category_scores,
        "dimension_scores": dimension_scores,
        "dominant": dominant,
        "growth_area": growth_area,
        "recommendation": recommendation
    }

    assessments = load_assessments()
    assessments.append(assessment_record)
    save_assessments(assessments)

    print_assessment_result(assessment_record)


def print_assessment_result(assessment):
    print("\nIRON RITE ASSESSMENT RESULTS")
    print("----------------------------")
    print("Name:", assessment["name"])
    print("Email:", assessment["email"])

    ranked_scores = sorted(
        assessment["scores"].items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\nArchetype Scores:")

    for category, score in ranked_scores:
        print(category + ":", score)

    print("\nDimension Scores:")

    for category, dimensions in assessment["dimension_scores"].items():
        print("\n" + category)

        for dimension, score in dimensions.items():
            print("  " + dimension + ":", score)

    print("\nDominant Archetype:", assessment["dominant"])
    print("Growth Area:", assessment["growth_area"])

    print("\nRecommendation:")
    print(assessment["recommendation"])


def view_saved_assessments():
    assessments = load_assessments()

    print("\nSAVED ASSESSMENTS")
    print("-----------------")

    if len(assessments) == 0:
        print("No saved assessments found.")
        return

    for index, assessment in enumerate(assessments):
        print("\nRecord Number:", index + 1)
        print("Name:", assessment.get("name", "Unknown"))
        print("Email:", assessment.get("email", "No email saved"))
        print("Dominant Archetype:", assessment["dominant"])
        print("Growth Area:", assessment["growth_area"])

        print("\nArchetype Scores:")

        for category, score in assessment["scores"].items():
            print(category + ":", score)


def search_assessment():
    assessments = load_assessments()

    if len(assessments) == 0:
        print("\nNo saved assessments to search.")
        return

    search_text = input("Enter name or email to search: ")
    found_any = False

    print("\nSEARCH RESULTS")
    print("--------------")

    for index, assessment in enumerate(assessments):
        stored_name = assessment.get("name", "")
        stored_email = assessment.get("email", "")

        if search_text.lower() in stored_name.lower() or search_text.lower() in stored_email.lower():
            found_any = True

            print("\nRecord Number:", index + 1)
            print("Name:", assessment.get("name", "Unknown"))
            print("Email:", assessment.get("email", "No email saved"))
            print("Dominant Archetype:", assessment["dominant"])
            print("Growth Area:", assessment["growth_area"])

    if found_any == False:
        print("No matching assessments found.")


def update_assessment_name():
    assessments = load_assessments()

    if len(assessments) == 0:
        print("\nNo saved assessments to update.")
        return

    email = input("Enter email address for the assessment to update: ")

    for assessment in assessments:
        stored_email = assessment.get("email", "")

        if stored_email.lower() == email.lower():
            print("\nCurrent name:", assessment["name"])
            new_name = input("Enter corrected name: ")

            assessment["name"] = new_name

            save_assessments(assessments)

            print("\nAssessment name updated.")
            return

    print("No assessment found with that email.")


def delete_assessment():
    assessments = load_assessments()

    if len(assessments) == 0:
        print("\nNo saved assessments to delete.")
        return

    view_saved_assessments()

    choice = input("\nEnter the record number to delete: ")

    if not choice.isdigit():
        print("Invalid choice. Enter a number.")
        return

    record_number = int(choice)

    if record_number < 1 or record_number > len(assessments):
        print("Invalid record number.")
        return

    deleted_assessment = assessments.pop(record_number - 1)

    save_assessments(assessments)

    print("\nDeleted assessment for:", deleted_assessment["name"])


create_reports_folder()

while True:
    print("\nIRON RITE ASSESSMENT PLATFORM")
    print("1. Run Assessment")
    print("2. View Saved Assessments")
    print("3. Search Assessment")
    print("4. Update Assessment Name")
    print("5. Delete Assessment")
    print("6. Export Assessment Report")
    print("7. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        run_assessment()

    elif choice == "2":
        view_saved_assessments()

    elif choice == "3":
        search_assessment()

    elif choice == "4":
        update_assessment_name()

    elif choice == "5":
        delete_assessment()

    elif choice == "6":
        export_assessment_report()

    elif choice == "7":
        print("Program ending.")
        break

    else:
        print("Invalid choice.")