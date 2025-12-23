import os
from reader import load_prospects
from logic import split_by_state
from writer import print_summary, write_report

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILEPATH = os.path.join(BASE_DIR, "data", "prospects.xlsx")


def main():
    """
    Entry point of the prospect automation bot

    Business purpose:
    - Manage and track prospecting efforts
    - Classify prospects by contact status
    - Generate a usable Excel report
    """
    df = load_prospects(FILEPATH)
    from logic import apply_follow_up_rule, split_by_state

    df = apply_follow_up_rule(df)
    groups = split_by_state(df)
    # Business rule: prospects are handled differently depending on their status
    groups = split_by_state(df)

    print_summary(groups)
    write_report(groups)

if __name__ == "__main__":
    main()
