from datetime import datetime, timedelta
import pandas as pd


FOLLOW_UP_DELAY_DAYS = 10


def apply_follow_up_rule(df):
    """
    Business rule:
    If a prospect is in ATTENTE_REPONSE and the last contact date
    is older than FOLLOW_UP_DELAY_DAYS, move it back to A_CONTACTER.
    """
    today = datetime.today()

    def should_be_recontacted(row):
        if row["etat"] != "ATTENTE_REPONSE":
            return row["etat"]

        if pd.isna(row["date_dernier_contact"]):
            return "A_CONTACTER"

        days_since_contact = (today - row["date_dernier_contact"]).days

        if days_since_contact >= FOLLOW_UP_DELAY_DAYS:
            return "A_CONTACTER"

        return "ATTENTE_REPONSE"

    df["etat"] = df.apply(should_be_recontacted, axis=1)
    return df


def split_by_state(df):
    """
    Group prospects by their current state.
    """
    return {
        "A_CONTACTER": df[df["etat"] == "A_CONTACTER"],
        "ATTENTE_REPONSE": df[df["etat"] == "ATTENTE_REPONSE"],
        "RELANCE": df[df["etat"] == "RELANCE"],
        "INACTIF": df[df["etat"] == "INACTIF"],
    }
