import pandas as pd

def load_scope(path):
    df = pd.read_excel(path)

    df.columns = [str(col).strip().lower() for col in df.columns]

    rename_map = {
        "discipline": "discipline",
        "scope item": "scope_item",
        "assumptions / clarifications": "assumptions",
        "exclusions": "exclusions",
        "arup comments": "comments",
        "accepted": "accepted"
    }

    df = df.rename(columns=rename_map)

    df = df.dropna(how="all")

    if "discipline" in df.columns:
        df["discipline"] = df["discipline"].ffill()

    df["id"] = range(1, len(df) + 1)

    df["full_text"] = (
        df.get("scope_item", "").astype(str) + " " +
        df.get("assumptions", "").astype(str) + " " +
        df.get("comments", "").astype(str)
    )

    return df