import pandas as pd
from datetime import date


def print_summary(groups):
    print("Résumé des prospects")
    print("--------------------")

    for state, df in groups.items():
        print(f"{state}: {len(df)}")


def build_summary_dataframe(groups):
    """
    Build a summary table with:
    - current date
    - prospect status
    - number of prospects per status
    """
    today = date.today().isoformat()
    rows = []

    for state, df in groups.items():
        rows.append({
            "date": today,
            "etat": state,
            "nombre": len(df)
        })

    return pd.DataFrame(rows)


def write_report(groups, output_path="rapport_prospection.xlsx"):
    """
    Generate the final Excel report:
    - One 'Résumé' sheet
    - One sheet per prospect status
    """
    summary_df = build_summary_dataframe(groups)

    with pd.ExcelWriter(output_path) as writer:
        summary_df.to_excel(writer, sheet_name="Résumé", index=False)

        for state, df in groups.items():
            df.to_excel(writer, sheet_name=state, index=False)
