from reader import load_prospects
from logic import split_by_state
from writer import print_summary, write_synthesis
import os

FILEPATH = os.path.join("data", "prospects.xlsx")

def main():
    df = load_prospects(FILEPATH)
    groups = split_by_state(df)
    print_summary(groups)
    write_synthesis(groups)
    input("\nAppuyez sur Entrée pour fermer...")

if __name__ == "__main__":
    main()
