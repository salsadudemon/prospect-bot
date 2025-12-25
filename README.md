# Prospect Automation Bot

## Description
This project is a small Python tool designed to help manage freelance or business prospecting.

It reads a simple Excel file containing prospects, applies basic business rules
(follow-up delays, contact status), and generates a clear Excel report that shows
which prospects should be contacted, followed up, or considered inactive.

The goal is to avoid forgetting follow-ups and to keep prospecting organized.

---

## What this tool does
- Reads a prospect list from an Excel file
- Validates and cleans the data
- Automatically updates prospect status based on follow-up rules
- Generates an Excel report with:
  - a dated summary
  - one sheet per prospect status

---

## Expected Excel format

The input file must be named: prospects.xlsx


and placed in the `data/` folder.

### Required columns

| Column name              | Description |
|--------------------------|-------------|
| nom                      | Company or prospect name |
| localisation             | Location |
| contact                  | Email or phone |
| etat                     | Current status |
| date_dernier_contact     | Date of last contact (YYYY-MM-DD) |

### Allowed values for `etat`

- `A_CONTACTER`
- `ATTENTE_REPONSE`
- `RELANCE`
- `INACTIF`

---

## Business rule implemented

If a prospect is in `ATTENTE_REPONSE` and has not responded after 10 days
since the last contact, the status is automatically changed to `A_CONTACTER`.

This allows systematic follow-up without manual tracking.

---

## How to run the project

### Requirements
- Python 3
- pandas
- openpyxl

### Run
Open `bot/main.py` with IDLE or your Python editor and run the script.

The program will:
- display a summary in the console
- generate an Excel report named: rapport_prospection.xlsx


---

## Output
The generated report contains:
- a `Résumé` sheet with the current date and number of prospects per status
- one sheet per status (`A_CONTACTER`, `ATTENTE_REPONSE`, etc.)

---

## Project structure
prospect-bot/
├─ bot/
│ ├─ main.py
│ ├─ reader.py
│ ├─ logic.py
│ └─ writer.py
├─ data/
│ └─ prospects.xlsx
└─ README.md


---

## Limitations
- No graphical interface
- No automatic web data collection
- Designed as a local tool for personal or small-scale use

---

## Possible improvements
- Additional follow-up rules
- Priority scoring
- Executable version
- GUI or web interface

---

## Author
Personal learning project Tototuto– Python & automation.

