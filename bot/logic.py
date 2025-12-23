def split_by_state(df):
    result = {
        "A_CONTACTER": df[df["etat"] == "A_CONTACTER"],
        "RELANCE": df[df["etat"] == "RELANCE"],
        "INACTIF": df[df["etat"] == "INACTIF"],
    }
    return result

