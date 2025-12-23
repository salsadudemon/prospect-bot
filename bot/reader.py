import pandas as pd

REQUIRED_COLUMNS = {"nom", "localisation", "contact", "etat"}
VALID_STATES = {"A_CONTACTER", "RELANCE", "INACTIF"}


def load_prospects(filepath: str) -> pd.DataFrame:
    """
    Load and validate prospect data from an Excel file.
    """https://github.com/salsadudemon/prospect-bot/blob/main/bot/reader.py
    try:
        df = pd.read_excel(filepath, parse_dates=["date_dernier_contact"])
    except Exception as e:
        raise RuntimeError(f"Unable to read Excel file: {e}")

    # Check required columns
    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Normalize text fields
    for col in REQUIRED_COLUMNS:
        df[col] = df[col].astype(str).str.strip()

    # Validate states
    invalid_states = set(df["etat"]) - VALID_STATES
    if invalid_states:
        raise ValueError(f"Invalid state values found: {invalid_states}")

    return df

