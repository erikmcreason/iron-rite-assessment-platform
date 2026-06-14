# Iron Rite Assessment Platform

## Project Purpose

The Iron Rite Assessment Platform is a Python-based assessment application designed to evaluate archetypal development across the King, Warrior, Magician, and Lover archetypes.

The project serves two purposes:

1. A real-world software engineering learning project.
2. The foundation for a future Iron Rite assessment product.

---

## Current Status

Version: V1

Application Type:
- Python Command Line Application (CLI)

Status:
- Functional
- Tested
- Stable

---

## Completed Features

### Assessment Engine

- Run Assessment
- Score Assessment
- Dominant Archetype Calculation
- Growth Area Calculation
- Recommendations

### Data Storage

- JSON Persistence
- Save Assessments
- Load Assessments

### CRUD Operations

- Create Assessment
- View Assessments
- Search Assessment
- Update Assessment Name
- Delete Assessment

### Identification

- Email-Based User Identification

### Scoring

- Archetype Scoring
- Dimension Scoring

---

## Current Files

### Core Application

functions_menu.py

### Data

questions.json

### Runtime Data

brothers.json

### Documentation

README.md

PROJECT_HANDOFF.md

---

## Current Data Model

Assessment Record Structure

```python
{
    "name": "Erik",
    "email": "erikmcreason@gmail.com",

    "scores": {
        "King": 10.0,
        "Warrior": 9.2,
        "Magician": 9.0,
        "Lover": 7.8
    },

    "dominant": "King",
    "growth_area": "Lover",

    "dimension_scores": {
        ...
    },

    "recommendation": "..."
}
```

---

## GitHub Repository

Repository:

iron-rite-assessment-platform

Status:

Connected through GitHub web uploads.

NOTE:

The local VS Code project is NOT currently connected to Git via a .git folder.

Future Task:

- Clone repository locally
- Reconnect project properly
- Begin using git add / commit / push workflow

---

## Closed Issues

- Dimension Scoring Engine V1
- Search Assessment V1
- Update Assessment V1

---

## Open Issues

### Export Assessment Report V1

Requirements:

- Search assessment by email
- Create reports folder if needed
- Generate report file

Filename format:

<Name>_Assessment_Report.txt

Example:

Erik_Assessment_Report.txt

Report should include:

- Name
- Email
- Dominant Archetype
- Growth Area
- Archetype Scores
- Dimension Scores
- Recommendation

Success Message:

Report exported successfully.

---

## Planned Roadmap

### Version 1.1

Export Assessment Report V1

### Version 1.2

Reconnect Local Git Repository

### Version 1.3

Build Executable (.exe)

Goal:

Allow family and friends to run the assessment without installing Python.

### Version 2.0

GUI Version

Potential technologies:

- Tkinter
- PyQt
- Web Interface

### Version 3.0

Website Version

Potential:

- User Accounts
- Progress Tracking
- Assessment History
- Reporting Dashboard

---

## Learning Preferences

The user learns best using:

1. Official terminology first
2. Analogy second
3. Real project examples third

Example:

Key = official term

Shelf label = analogy

Dictionary = official term

Warehouse = analogy

Avoid replacing official programming terms.

Use analogies to reinforce concepts, not replace terminology.

---

## Important Concepts Learned

### Dictionary

Stores key-value pairs.

Example:

```python
{
    "King": 10
}
```

Key:
"King"

Value:
10

### List

Stores multiple values.

Example:

```python
[8, 9, 10]
```

### append()

Adds an item to a list.

### pop()

Removes an item from a list.

### CRUD

Create
Read
Update
Delete

### JSON

Used for persistent storage.

### Repository

A project managed by Git/GitHub.

---

## Next Session Starting Point

1. Verify Export Assessment Report V1 issue.
2. Build export_report() function.
3. Add menu option for export.
4. Create reports folder automatically.
5. Generate Erik_Assessment_Report.txt.
6. Test export feature.
7. Reconnect local Git repository properly.