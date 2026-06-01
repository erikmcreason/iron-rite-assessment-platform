import json

brothers = []


def load_brothers():
    global brothers

    try:
        with open("brothers.json", "r") as file:
            brothers = json.load(file)

        print("Existing brothers loaded.")

    except FileNotFoundError:
        brothers = []
        print("No saved brothers found. Starting fresh.")


def save_brothers():
    with open("brothers.json", "w") as file:
        json.dump(brothers, file, indent=4)

    print("Brothers saved.")


def get_scores(brother):
    return {
        "Warrior": brother["warrior"],
        "King": brother["king"],
        "Magician": brother["magician"],
        "Lover": brother["lover"]
    }


def get_dominant_archetype(brother):
    scores = get_scores(brother)
    return max(scores, key=scores.get)


def get_growth_area(brother):
    scores = get_scores(brother)
    return min(scores, key=scores.get)


def get_average_score(brother):
    total = brother["warrior"] + brother["king"] + brother["magician"] + brother["lover"]
    return total / 4


def get_assessment_text(dominant, growth_area):
    assessment = ""

    if dominant == "Warrior":
        assessment += "Primary strength: disciplined action, courage, endurance, and execution.\n"
    elif dominant == "King":
        assessment += "Primary strength: leadership, order, responsibility, and vision.\n"
    elif dominant == "Magician":
        assessment += "Primary strength: insight, strategy, learning, and pattern recognition.\n"
    elif dominant == "Lover":
        assessment += "Primary strength: connection, creativity, beauty, emotion, and vitality.\n"

    if growth_area == "Warrior":
        assessment += "Primary growth area: stronger discipline, boundaries, physical action, and decisive movement."
    elif growth_area == "King":
        assessment += "Primary growth area: clearer leadership, structure, ownership, and long-term vision."
    elif growth_area == "Magician":
        assessment += "Primary growth area: deeper study, reflection, strategy, and self-awareness."
    elif growth_area == "Lover":
        assessment += "Primary growth area: deeper connection, emotional presence, play, beauty, and relational openness."

    return assessment


def get_recommendation(growth_area):
    if growth_area == "Warrior":
        return "Recommended practice: complete one difficult physical task today and set one firm boundary."

    elif growth_area == "King":
        return "Recommended practice: define one clear standard, make one leadership decision, and communicate it calmly."

    elif growth_area == "Magician":
        return "Recommended practice: spend 20 minutes studying, journaling, or mapping the pattern behind a current problem."

    elif growth_area == "Lover":
        return "Recommended practice: create one moment of connection, beauty, gratitude, or emotional presence today."

    else:
        return "Recommended practice: review the scores and choose one area for deliberate growth."


def add_brother():
    name = input("Enter brother name: ")

    warrior = int(input("Warrior score (1-10): "))
    king = int(input("King score (1-10): "))
    magician = int(input("Magician score (1-10): "))
    lover = int(input("Lover score (1-10): "))

    brother = {
        "name": name,
        "warrior": warrior,
        "king": king,
        "magician": magician,
        "lover": lover
    }

    brothers.append(brother)

    print("Brother added.")


def show_brothers():
    print("\nBrother Profiles")

    if len(brothers) == 0:
        print("No brothers stored.")
        return

    for brother in brothers:
        dominant = get_dominant_archetype(brother)
        growth_area = get_growth_area(brother)
        average = get_average_score(brother)

        print("\nName:", brother["name"])
        print("Warrior:", brother["warrior"])
        print("King:", brother["king"])
        print("Magician:", brother["magician"])
        print("Lover:", brother["lover"])
        print("Dominant Archetype:", dominant)
        print("Growth Area:", growth_area)
        print("Average Score:", average)


def generate_report():
    name = input("Enter brother name for report: ")

    for brother in brothers:
        if brother["name"] == name:
            dominant = get_dominant_archetype(brother)
            growth_area = get_growth_area(brother)
            average = get_average_score(brother)
            assessment = get_assessment_text(dominant, growth_area)
            recommendation = get_recommendation(growth_area)

            print("\nIRON RITE ARCHETYPE REPORT")
            print("--------------------------")
            print("Name:", brother["name"])
            print("Dominant Archetype:", dominant)
            print("Growth Area:", growth_area)
            print("Average Score:", average)
            print("\nAssessment:")
            print(assessment)
            print("\nRecommendation:")
            print(recommendation)

            return

    print("Brother not found.")


def update_brother():
    name = input("Enter brother name to update: ")

    for brother in brothers:
        if brother["name"] == name:
            brother["warrior"] = int(input("New Warrior score: "))
            brother["king"] = int(input("New King score: "))
            brother["magician"] = int(input("New Magician score: "))
            brother["lover"] = int(input("New Lover score: "))

            print("Brother updated.")
            return

    print("Brother not found.")


def delete_brother():
    name = input("Enter brother name to delete: ")

    for brother in brothers:
        if brother["name"] == name:
            brothers.remove(brother)
            print("Brother deleted.")
            return

    print("Brother not found.")


load_brothers()

while True:
    print("\nIRON RITE ARCHETYPE TRACKER")
    print("1. Add Brother")
    print("2. View Brothers")
    print("3. Generate Report")
    print("4. Update Brother")
    print("5. Delete Brother")
    print("6. Save")
    print("7. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_brother()

    elif choice == "2":
        show_brothers()

    elif choice == "3":
        generate_report()

    elif choice == "4":
        update_brother()

    elif choice == "5":
        delete_brother()

    elif choice == "6":
        save_brothers()

    elif choice == "7":
        save_brothers()
        print("Program ending.")
        break

    else:
        print("Invalid choice.")