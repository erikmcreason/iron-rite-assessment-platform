import json

with open("people.json", "r") as file:
    people = json.load(file)

print("\nLoaded Data:\n")

for person in people:
    print(person)

print("\nAdult Names:\n")

for person in people:
    if person["age"] >= 18:
        print(person["name"])