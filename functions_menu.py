import json


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


while True:
    print("\nIRON RITE ASSESSMENT PLATFORM")
    print("1. Run Assessment")
    print("2. View Saved Assessments")
    print("3. Search Assessment")
    print("4. Update Assessment Name")
    print("5. Delete Assessment")
    print("6. Quit")

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
        print("Program ending.")
        break

    else:
        print("Invalid choice.")