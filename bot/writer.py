import pandas as pd
def print_summary(groups):
    print("Résumé des prospects")
    print("--------------------")

    for state, df in groups.items():
        print(f"{state}: {len(df)}")


def write_synthesis(groups, output_path="synthese_prospects.xlsx"):
    with pd.ExcelWriter(output_path) as writer:
        for state, df in groups.items():
            df.to_excel(writer, sheet_name=state, index=False)

